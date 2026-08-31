param(
    [string]$Root = '',
    [string]$Stage = '',
    [switch]$ReusePrepared,
    [switch]$OnlyR007,
    [switch]$OnlyR008
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if ([string]::IsNullOrWhiteSpace($Root)) {
    $Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
}
if ([string]::IsNullOrWhiteSpace($Stage)) {
    $Stage = Join-Path $Root 'tmp\pdfs\terminology-patch-20260831'
}

function Copy-OverlayTree {
    param([string]$Source, [string]$Overlay, [string]$Destination, [string[]]$SkipNames)
    if (Test-Path -LiteralPath $Destination) {
        throw "Refusing to overwrite build tree: $Destination"
    }
    New-Item -ItemType Directory -Path $Destination | Out-Null
    foreach ($item in Get-ChildItem -LiteralPath $Source -Force) {
        if ($SkipNames -contains $item.Name) { continue }
        Copy-Item -LiteralPath $item.FullName -Destination $Destination -Recurse
    }
    foreach ($item in Get-ChildItem -LiteralPath $Overlay -Force) {
        $target = Join-Path $Destination $item.Name
        if ($item.PSIsContainer) {
            if (-not (Test-Path -LiteralPath $target)) {
                New-Item -ItemType Directory -Path $target | Out-Null
            }
            foreach ($child in Get-ChildItem -LiteralPath $item.FullName -Force) {
                Copy-Item -LiteralPath $child.FullName -Destination $target -Recurse -Force
            }
        } else {
            Copy-Item -LiteralPath $item.FullName -Destination $target -Force
        }
    }
}

function Add-PinnedBuildDependencies {
    param([string]$BuildName, [string]$Destination)
    $dependencies = @()
    if ($BuildName -like 'r007-*') {
        $dependencies = @(
            @{ Relative='qa\terminology_qa\tex-deps\tasks-v1.4a\tasks.sty'; Sha256='2e36d1338e5634939be9303ca0f8bdaab20e7e5aa067da36e124b7c6bcf41dac' },
            @{ Relative='qa\terminology_qa\tex-deps\tasks-v1.4a\tasks.cfg'; Sha256='f0fb11ea45bb2145138d482d8b850244133150dea9fcad98c91df0b076b34d61' }
        )
    } elseif ($BuildName -like 'r008-*') {
        $dependencies = @(
            @{ Relative='qa\terminology_qa\tex-deps\faktor-v0.1b\faktor.sty'; Sha256='56bb3be229f581c618360841571836a83d4aa4b2136b9ac541140e0a5671f0ad' }
        )
    }
    foreach ($dependency in $dependencies) {
        $source = Join-Path $Root $dependency.Relative
        $actual = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($actual -ne $dependency.Sha256) {
            throw "Pinned TeX dependency hash mismatch: $($dependency.Relative)"
        }
        Copy-Item -LiteralPath $source -Destination $Destination -Force
    }
}

function Invoke-Captured {
    param([string]$File, [string[]]$Arguments, [string]$WorkingDirectory, [string]$LogBase)
    $stdout = "$LogBase.stdout.txt"
    $stderr = "$LogBase.stderr.txt"
    $process = Start-Process -FilePath $File -ArgumentList $Arguments `
        -WorkingDirectory $WorkingDirectory -NoNewWindow -Wait -PassThru `
        -RedirectStandardOutput $stdout -RedirectStandardError $stderr
    if ($process.ExitCode -ne 0) {
        throw "Native command failed ($($process.ExitCode)): $File $($Arguments -join ' ')"
    }
}

function Build-Reader {
    param([string]$Directory, [string]$Master, [bool]$Glossary)
    $pdflatex = (Get-Command pdflatex).Source
    $makeindex = (Get-Command makeindex).Source
    $makeglossaries = (Get-Command makeglossaries).Source
    if ($Master -eq 'diffyqs' -and -not (Test-Path -LiteralPath (Join-Path $Directory 'diffyqs.aux'))) {
        # perpage learns the physical-page reset map from the first AUX pass. The
        # source intentionally uses symbolic footnotes, whose finite symbol set
        # overflows before that map exists. Use Arabic markers for this discarded
        # bootstrap pass only, then restore the exact canonical driver bytes.
        $driver = Join-Path $Directory 'diffyqs.tex'
        $original = [IO.File]::ReadAllText($driver)
        $marker = '\usepackage{diffyqssetup}'
        if ($original.IndexOf($marker, [StringComparison]::Ordinal) -lt 0) {
            throw 'Diffy Qs bootstrap marker not found'
        }
        $bootstrap = $original.Replace($marker, "$marker`r`n% Build-only first-pass footnote bootstrap.`r`n\renewcommand{\thefootnote}{\arabic{footnote}}")
        [IO.File]::WriteAllText($driver, $bootstrap, [Text.UTF8Encoding]::new($false))
        try {
            Invoke-Captured $pdflatex @('-interaction=nonstopmode','-halt-on-error','-file-line-error','diffyqs.tex') $Directory (Join-Path $Directory 'pass-0-footnote-bootstrap')
        } finally {
            [IO.File]::WriteAllText($driver, $original, [Text.UTF8Encoding]::new($false))
        }
        if (-not (Test-Path -LiteralPath (Join-Path $Directory 'diffyqs.aux'))) {
            throw 'Diffy Qs footnote bootstrap did not create its AUX map'
        }
    }
    if ($Master -eq 'ca' -and -not (Test-Path -LiteralPath (Join-Path $Directory 'ca.aux'))) {
        # The Complex Analysis driver also resets symbolic footnotes per page.
        # Before perpage has written its first AUX map, the global symbol count
        # overflows. Discard one Arabic-marker bootstrap pass, then restore the
        # exact canonical driver bytes before every retained build pass.
        $driver = Join-Path $Directory 'ca.tex'
        $original = [IO.File]::ReadAllText($driver)
        $marker = '\renewcommand{\thefootnote}{\fnsymbol{footnote}}'
        if ($original.IndexOf($marker, [StringComparison]::Ordinal) -lt 0) {
            throw 'Complex Analysis footnote bootstrap marker not found'
        }
        $bootstrap = $original.Replace($marker, '\renewcommand{\thefootnote}{\arabic{footnote}}')
        [IO.File]::WriteAllText($driver, $bootstrap, [Text.UTF8Encoding]::new($false))
        try {
            Invoke-Captured $pdflatex @('-interaction=nonstopmode','-halt-on-error','-file-line-error','ca.tex') $Directory (Join-Path $Directory 'pass-0-footnote-bootstrap')
        } finally {
            [IO.File]::WriteAllText($driver, $original, [Text.UTF8Encoding]::new($false))
        }
        if (-not (Test-Path -LiteralPath (Join-Path $Directory 'ca.aux'))) {
            throw 'Complex Analysis footnote bootstrap did not create its AUX map'
        }
    }
    for ($pass = 1; $pass -le 4; $pass++) {
        Invoke-Captured $pdflatex @('-interaction=nonstopmode','-halt-on-error','-file-line-error',"$Master.tex") $Directory (Join-Path $Directory "pass-$pass-pdflatex")
        Invoke-Captured $makeindex @($Master) $Directory (Join-Path $Directory "pass-$pass-makeindex")
        if ($Glossary) {
            Invoke-Captured $makeglossaries @($Master) $Directory (Join-Path $Directory "pass-$pass-makeglossaries")
        }
    }
    Invoke-Captured $pdflatex @('-interaction=nonstopmode','-halt-on-error','-file-line-error',"$Master.tex") $Directory (Join-Path $Directory 'pass-5-pdflatex')
    $log = Join-Path $Directory "$Master.log"
    $critical = Select-String -LiteralPath $log -Pattern 'There were undefined references|Rerun to get cross-references right|undefined citations|Missing character|Fatal error' -CaseSensitive:$false
    if ($critical) {
        throw "Critical final-log warning in $log`: $($critical.Line -join ' | ')"
    }
    $pdf = Join-Path $Directory "$Master.pdf"
    if (-not (Test-Path -LiteralPath $pdf)) { throw "Expected PDF missing: $pdf" }
    return $pdf
}

$builds = @(
    @{ Name='r007-a'; Source=(Join-Path $Root 'source\diffyqs-v6.11'); Overlay=(Join-Path $Root 'translation\diffyqs'); Master='diffyqs'; Glossary=$false; Skip=@('$out','old','slides') },
    @{ Name='r007-b'; Source=(Join-Path $Root 'source\diffyqs-v6.11'); Overlay=(Join-Path $Root 'translation\diffyqs'); Master='diffyqs'; Glossary=$false; Skip=@('$out','old','slides') },
    @{ Name='r008-a'; Source=(Join-Path $Root 'source\ca-v1.9'); Overlay=(Join-Path $Root 'translation\complex-analysis'); Master='ca'; Glossary=$true; Skip=@('$out','slides') },
    @{ Name='r008-b'; Source=(Join-Path $Root 'source\ca-v1.9'); Overlay=(Join-Path $Root 'translation\complex-analysis'); Master='ca'; Glossary=$true; Skip=@('$out','slides') }
)

if ($OnlyR007 -and $OnlyR008) {
    throw 'OnlyR007 and OnlyR008 are mutually exclusive'
}
if ($OnlyR007) {
    $builds = @($builds | Where-Object { $_.Name -like 'r007-*' })
} elseif ($OnlyR008) {
    $builds = @($builds | Where-Object { $_.Name -like 'r008-*' })
}

if ($ReusePrepared) {
    if (-not (Test-Path -LiteralPath $Stage)) { throw "Prepared stage missing: $Stage" }
    if (Test-Path -LiteralPath (Join-Path $Stage 'BUILD_RECEIPT.json')) {
        throw 'Prepared stage already has a terminal build receipt'
    }
    foreach ($build in $builds) {
        $directory = Join-Path $Stage $build.Name
        if (-not (Test-Path -LiteralPath $directory)) { throw "Prepared build tree missing: $directory" }
        if (Test-Path -LiteralPath (Join-Path $directory "$($build.Master).log")) {
            throw "Prepared build tree already contains TeX output: $directory"
        }
        Add-PinnedBuildDependencies $build.Name $directory
    }
} else {
    if (Test-Path -LiteralPath $Stage) {
        throw "Refusing to overwrite build stage: $Stage"
    }
    New-Item -ItemType Directory -Path $Stage | Out-Null
    foreach ($build in $builds) {
        $directory = Join-Path $Stage $build.Name
        Copy-OverlayTree $build.Source $build.Overlay $directory $build.Skip
        Add-PinnedBuildDependencies $build.Name $directory
    }
}

$oldEpoch = $env:SOURCE_DATE_EPOCH
$oldForce = $env:FORCE_SOURCE_DATE
$oldTimezone = $env:TZ
$mutex = [Threading.Mutex]::new($false, 'Global\InterlanguageTeXSlotV1')
$acquired = $false
$abandoned = $false
try {
    try {
        $acquired = $mutex.WaitOne([TimeSpan]::FromSeconds(120))
    } catch [Threading.AbandonedMutexException] {
        $acquired = $true
        $abandoned = $true
    }
    if (-not $acquired) { throw 'Timed out acquiring Global\InterlanguageTeXSlotV1' }
    $env:SOURCE_DATE_EPOCH = '1788134400'
    $env:FORCE_SOURCE_DATE = '1'
    $env:TZ = 'UTC'
    $results = @()
    foreach ($build in $builds) {
        $directory = Join-Path $Stage $build.Name
        $pdf = Build-Reader $directory $build.Master $build.Glossary
        $item = Get-Item -LiteralPath $pdf
        $results += [ordered]@{
            build = $build.Name
            pdf = $pdf
            bytes = [int64]$item.Length
            sha256 = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
        }
    }
} finally {
    if ($null -eq $oldEpoch) { Remove-Item Env:SOURCE_DATE_EPOCH -ErrorAction SilentlyContinue } else { $env:SOURCE_DATE_EPOCH = $oldEpoch }
    if ($null -eq $oldForce) { Remove-Item Env:FORCE_SOURCE_DATE -ErrorAction SilentlyContinue } else { $env:FORCE_SOURCE_DATE = $oldForce }
    if ($null -eq $oldTimezone) { Remove-Item Env:TZ -ErrorAction SilentlyContinue } else { $env:TZ = $oldTimezone }
    if ($acquired) { $mutex.ReleaseMutex() }
    $mutex.Dispose()
}

if ($OnlyR008) {
    $r007Results = @()
    foreach ($name in @('r007-a','r007-b')) {
        $pdf = Join-Path $Stage "$name\diffyqs.pdf"
        if (-not (Test-Path -LiteralPath $pdf)) {
            throw "Required completed R007 PDF missing: $pdf"
        }
        $item = Get-Item -LiteralPath $pdf
        $r007Results += [ordered]@{
            build = $name
            pdf = $pdf
            bytes = [int64]$item.Length
            sha256 = (Get-FileHash -LiteralPath $pdf -Algorithm SHA256).Hash.ToLowerInvariant()
        }
    }
    $results = @($r007Results) + @($results)
}

if ($OnlyR007) {
    if ($results.Count -ne 2) {
        throw "Expected two independent R007 build results, found $($results.Count)"
    }
    if ($results[0].sha256 -ne $results[1].sha256 -or $results[0].bytes -ne $results[1].bytes) {
        throw 'R007 independent PDFs are not byte-identical'
    }
    $receiptName = 'BUILD_RECEIPT_R007.json'
} else {
    if ($results.Count -ne 4) {
        throw "Expected four independent build results, found $($results.Count)"
    }
    if ($results[0].sha256 -ne $results[1].sha256 -or $results[0].bytes -ne $results[1].bytes) {
        throw 'R007 independent PDFs are not byte-identical'
    }
    if ($results[2].sha256 -ne $results[3].sha256 -or $results[2].bytes -ne $results[3].bytes) {
        throw 'R008 independent PDFs are not byte-identical'
    }
    $receiptName = 'BUILD_RECEIPT.json'
}

$receipt = [ordered]@{
    schema = 'lebl-terminology-patch-reader-build-v1'
    status = 'pass'
    mutex = 'Global\InterlanguageTeXSlotV1'
    abandoned_mutex_recovered = $abandoned
    source_date_epoch = 1788134400
    builds = $results
}
$receiptJson = $receipt | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText(
    (Join-Path $Stage $receiptName),
    $receiptJson + [Environment]::NewLine,
    [Text.UTF8Encoding]::new($false)
)
$receiptJson
