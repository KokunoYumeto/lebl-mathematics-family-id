$ErrorActionPreference = 'Stop'

$repo = 'C:\Users\Floris\Documents\interlanguage\04_mirrors\id\lebl-mathematics-family-id'
$build = Join-Path $repo 'qa\builds\ra-id-volume2-stone-weierstrass-section-complete-reader-u393-20260826'
$source = Join-Path $repo 'translation\ra\ch-approximate.tex'
$partial = Join-Path $build 'ch-approximate.partial-v2.tex'
$installed = Join-Path $build 'ch-approximate.tex'
$expectedSourceSha = 'f78bb158c48d33deb40424c18855a369ded1122929cdbc532de9d389c28e0fdc'
$expectedPrefixSha = 'fcaf7baefb0a3356be1c1bc1625b90f90e899c8334ba11337f320c71a1b8fa21'
$expectedPartialSha = '1bc05e5e8b0b31e21fe89cabbbedafbc0e95f9b013106dac32f2483a60df786b'

$sourceSha = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
if ($sourceSha -ne $expectedSourceSha) {
    throw "Unexpected live source SHA-256: $sourceSha"
}
$lines = [System.IO.File]::ReadAllLines($source)
if ($lines.Count -ne 5481) {
    throw "Unexpected source length: $($lines.Count) lines"
}
if ($lines[4204] -ne '\end{exercise}') {
    throw "Unexpected target line 4205: $($lines[4204])"
}
if ($lines[4205] -ne '') {
    throw 'Unexpected target line 4206; expected blank line'
}
if ($lines[4206] -notmatch '^%{78}$' -or $lines[4207] -ne '') {
    throw 'Unexpected section-closing separator at target lines 4207-4208'
}
if ($lines[4208] -ne '\sectionnewpage') {
    throw "Unexpected target line 4209: $($lines[4208])"
}
if ($lines[4209] -ne '\section{Fourier series}') {
    throw "Unexpected target line 4210: $($lines[4209])"
}
if ($lines[4210] -ne '\label{sec:fourier}') {
    throw "Unexpected target line 4211: $($lines[4210])"
}

$prefix = (($lines[0..4207] -join "`n") + "`n")
$prefixBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($prefix)
$sha256 = [System.Security.Cryptography.SHA256]::Create()
try {
    $prefixSha = ([BitConverter]::ToString($sha256.ComputeHash($prefixBytes))).Replace('-', '').ToLowerInvariant()
}
finally {
    $sha256.Dispose()
}
if ($prefixSha -ne $expectedPrefixSha) {
    throw "Unexpected admitted-prefix SHA-256: $prefixSha"
}

$payload = $prefix + "% Deterministic reader cutoff after the admitted Stone--Weierstrass section.`n"
[System.IO.File]::WriteAllText($partial, $payload, [System.Text.UTF8Encoding]::new($false))
$partialSha = (Get-FileHash -LiteralPath $partial -Algorithm SHA256).Hash.ToLowerInvariant()
if ($partialSha -ne $expectedPartialSha) {
    throw "Unexpected partial SHA-256: $partialSha"
}
Copy-Item -LiteralPath $partial -Destination $installed -Force
if ((Get-FileHash -LiteralPath $installed -Algorithm SHA256).Hash.ToLowerInvariant() -ne $expectedPartialSha) {
    throw 'Installed chapter does not match deterministic partial'
}

Push-Location $build
$priorErrorActionPreference = $ErrorActionPreference
$ErrorActionPreference = 'Continue'
try {
    & perl '.\convert-to-mbx.pl' 2>&1 | Tee-Object -FilePath '.\converter.console.txt' | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Converter failed with exit code $LASTEXITCODE" }

    $stabilityFiles = @(
        'realanal2.aux', 'realanal2.toc', 'realanal2.out', 'realanal2.idx',
        'realanal2.glo', 'realanal2.ind', 'realanal2.gls'
    )
    $pass8Hashes = @{}
    for ($pass = 1; $pass -le 9; $pass++) {
        & pdflatex '-interaction=nonstopmode' '-halt-on-error' 'realanal2.tex' 2>&1 |
            Tee-Object -FilePath ('.\pdflatex-pass-{0}.console.txt' -f $pass) | Out-Null
        if ($LASTEXITCODE -ne 0) { throw "pdflatex pass $pass failed with exit code $LASTEXITCODE" }

        if ($pass -le 4) {
            & makeindex 'realanal2.idx' 2>&1 |
                Tee-Object -FilePath ('.\makeindex-pass-{0}.console.txt' -f $pass) | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "makeindex pass $pass failed with exit code $LASTEXITCODE" }

            & makeglossaries 'realanal2' 2>&1 |
                Tee-Object -FilePath ('.\makeglossaries-pass-{0}.console.txt' -f $pass) | Out-Null
            if ($LASTEXITCODE -ne 0) { throw "makeglossaries pass $pass failed with exit code $LASTEXITCODE" }
        }

        if ($pass -eq 8) {
            foreach ($name in $stabilityFiles) {
                $pass8Hashes[$name] = (Get-FileHash -LiteralPath $name -Algorithm SHA256).Hash.ToLowerInvariant()
            }
        }
    }

    foreach ($name in $stabilityFiles) {
        $pass9Hash = (Get-FileHash -LiteralPath $name -Algorithm SHA256).Hash.ToLowerInvariant()
        if ($pass9Hash -ne $pass8Hashes[$name]) {
            throw "Auxiliary file did not stabilize across passes 8 and 9: $name"
        }
    }
}
finally {
    $ErrorActionPreference = $priorErrorActionPreference
    Pop-Location
}
