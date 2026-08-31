param(
    [string]$RepositoryRoot = '',
    [string]$BuildDirectory = $PSScriptRoot
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$expectedCommit = 'e55907983ca54bb2c94d90230eb949b64a6ee7ff'
$expectedTree = '97cc963dc211728a20be1c18f9c8890f01790ae9'
$expectedChapterBytes = 198362
$expectedChapterSha = 'cfaa1339706c31f16255642adcccb33903343808bc2d1bf195d70d3f25004133'
$expectedDriverBytes = 20444
$expectedDriverSha = '99670a3938d6cd54b7e37158c88185d3baaf9116f2927ff73e57fee5ac1ed03f'
$expectedPdfBytes = 2427379
$expectedPdfSha = 'e70c74bb7edc466a7cb6ff0eff0de33dfcc7b3bc63010d018aff758a14d2dea3'
$expectedPages = 241
$sourceDateEpoch = '1787961600'

function Get-LowerSha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Assert-FileIdentity(
    [string]$Path,
    [long]$ExpectedBytes,
    [string]$ExpectedSha,
    [string]$Label
) {
    $item = Get-Item -LiteralPath $Path
    if ($item.PSIsContainer -or $item.Length -ne $ExpectedBytes) {
        throw "$Label byte identity mismatch: $($item.Length)"
    }
    $actualSha = Get-LowerSha256 $Path
    if ($actualSha -ne $ExpectedSha) {
        throw "$Label SHA-256 mismatch: $actualSha"
    }
}

function Invoke-Checked([string]$Program, [string[]]$Arguments, [string]$LogPath) {
    & $Program @Arguments 2>&1 | Tee-Object -FilePath $LogPath | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "$Program failed with exit code $LASTEXITCODE; see $LogPath"
    }
}

$build = [System.IO.Path]::GetFullPath($BuildDirectory)
if (-not (Test-Path -LiteralPath $build -PathType Container)) {
    throw "Build directory does not exist: $build"
}

if ($RepositoryRoot) {
    $repo = [System.IO.Path]::GetFullPath($RepositoryRoot)
}
else {
    $candidates = @(
        [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..')),
        [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..\..'))
    )
    $repo = $null
    foreach ($candidate in $candidates) {
        if (Test-Path -LiteralPath (Join-Path $candidate 'translation\ra\ch-approximate.tex') -PathType Leaf) {
            $repo = $candidate
            break
        }
    }
    if (-not $repo) {
        throw 'Cannot resolve repository/package root; pass -RepositoryRoot explicitly'
    }
}

$sourceChapter = Join-Path $repo 'translation\ra\ch-approximate.tex'
$overlayChapter = Join-Path $PSScriptRoot 'ch-approximate.tex'
$overlayDriver = Join-Path $PSScriptRoot 'realanal2.tex'
Assert-FileIdentity $sourceChapter $expectedChapterBytes $expectedChapterSha 'live U429 chapter'
Assert-FileIdentity $overlayChapter $expectedChapterBytes $expectedChapterSha 'overlay U429 chapter'
Assert-FileIdentity $overlayDriver $expectedDriverBytes $expectedDriverSha 'overlay U429 driver'

$installedChapter = Join-Path $build 'ch-approximate.tex'
$installedDriver = Join-Path $build 'realanal2.tex'
if ([System.IO.Path]::GetFullPath($overlayChapter) -ne [System.IO.Path]::GetFullPath($installedChapter)) {
    Copy-Item -LiteralPath $overlayChapter -Destination $installedChapter -Force
}
if ([System.IO.Path]::GetFullPath($overlayDriver) -ne [System.IO.Path]::GetFullPath($installedDriver)) {
    Copy-Item -LiteralPath $overlayDriver -Destination $installedDriver -Force
}
Assert-FileIdentity $installedChapter $expectedChapterBytes $expectedChapterSha 'installed U429 chapter'
Assert-FileIdentity $installedDriver $expectedDriverBytes $expectedDriverSha 'installed U429 driver'

foreach ($required in @('convert-to-mbx.pl', 'realanal.tex', 'realanal.aux')) {
    if (-not (Test-Path -LiteralPath (Join-Path $build $required) -PathType Leaf)) {
        throw "Missing required build input $required. Build Volume I first in the same tree."
    }
}

$oldEpoch = $env:SOURCE_DATE_EPOCH
$oldForceDate = $env:FORCE_SOURCE_DATE
$oldTz = $env:TZ
$env:SOURCE_DATE_EPOCH = $sourceDateEpoch
$env:FORCE_SOURCE_DATE = '1'
$env:TZ = 'UTC'

$stabilityFiles = @(
    'realanal2.pdf', 'realanal2.aux', 'realanal2.toc', 'realanal2.out',
    'realanal2.idx', 'realanal2.glo', 'realanal2.ind', 'realanal2.gls'
)
$pass8Hashes = @{}

Push-Location $build
try {
    Invoke-Checked 'perl' @('.\convert-to-mbx.pl') '.\converter.console.txt'
    for ($pass = 1; $pass -le 9; $pass++) {
        Invoke-Checked 'pdflatex' @('-interaction=nonstopmode', '-halt-on-error', 'realanal2.tex') ('.\pdflatex-pass-{0}.console.txt' -f $pass)
        if ($pass -le 4) {
            Invoke-Checked 'makeindex' @('realanal2.idx') ('.\makeindex-pass-{0}.console.txt' -f $pass)
            Invoke-Checked 'makeglossaries' @('realanal2') ('.\makeglossaries-pass-{0}.console.txt' -f $pass)
        }
        if ($pass -eq 8) {
            foreach ($name in $stabilityFiles) {
                $pass8Hashes[$name] = Get-LowerSha256 (Join-Path $build $name)
            }
        }
    }

    foreach ($name in $stabilityFiles) {
        $pass9Sha = Get-LowerSha256 (Join-Path $build $name)
        if ($pass9Sha -ne $pass8Hashes[$name]) {
            throw "Build product did not stabilize across passes 8 and 9: $name"
        }
    }

    $logText = Get-Content -LiteralPath '.\realanal2.log' -Raw
    foreach ($forbidden in @(
        'Fatal error', 'Undefined control sequence', 'LaTeX Error:',
        'There were undefined references', 'Rerun to get cross-references right',
        'multiply-defined labels', 'Missing character:'
    )) {
        if ($logText -match [regex]::Escape($forbidden)) {
            throw "Forbidden TeX log marker: $forbidden"
        }
    }

    $pdfInfo = (& pdfinfo '.\realanal2.pdf' 2>&1 | Out-String)
    if ($LASTEXITCODE -ne 0 -or $pdfInfo -notmatch "(?m)^Pages:\s+$expectedPages\s*$") {
        throw 'PDF page-count verification failed'
    }
    $fontRows = & pdffonts '.\realanal2.pdf' 2>&1
    if ($LASTEXITCODE -ne 0) { throw 'pdffonts failed' }
    $fontData = $fontRows | Select-Object -Skip 2 | Where-Object { $_.Trim() }
    if (-not $fontData -or ($fontData | Where-Object { $_ -match '\sno\s' })) {
        throw 'One or more PDF fonts are not embedded'
    }
    Invoke-Checked 'pdftotext' @('.\realanal2.pdf', '.\realanal2.txt') '.\pdftotext.console.txt'
    $text = Get-Content -LiteralPath '.\realanal2.txt' -Raw -Encoding UTF8
    if ($text.Contains([char]0xfffd)) {
        throw 'PDF text extraction contains replacement characters'
    }

    Assert-FileIdentity '.\realanal2.pdf' $expectedPdfBytes $expectedPdfSha 'final U429 Volume II PDF'
    [ordered]@{
        status = 'pass'
        source_commit = $expectedCommit
        source_tree = $expectedTree
        source_date_epoch = [long]$sourceDateEpoch
        pages = $expectedPages
        bytes = $expectedPdfBytes
        sha256 = $expectedPdfSha
        stable_products = $stabilityFiles.Count
    } | ConvertTo-Json -Compress
}
finally {
    Pop-Location
    $env:SOURCE_DATE_EPOCH = $oldEpoch
    $env:FORCE_SOURCE_DATE = $oldForceDate
    $env:TZ = $oldTz
}
