$ErrorActionPreference = 'Stop'

$repo = 'C:\Users\Floris\Documents\interlanguage\04_mirrors\id\lebl-mathematics-family-id'
$build = Join-Path $repo 'qa\builds\ra-id-volume2-arzela-ascoli-section-complete-reader-u370-20260825'
$source = Join-Path $repo 'translation\ra\ch-approximate.tex'
$partial = Join-Path $build 'ch-approximate.partial-v2.tex'
$installed = Join-Path $build 'ch-approximate.tex'
$expectedSourceSha = '8207bf35bf21bdcb65ac1947c92c51951b65e4faad5c348ac40796663bd36ac2'
$expectedPrefixSha = '3a54147196f64d34694aa7d240ef7d445a2c1fef3aa593569ba82c91fd3fcfee'
$expectedPartialSha = '0e492bdf9f4116d967b43ecb15fa0ba3db501c45defdb7f244a5d3b823a62ce6'

$sourceSha = (Get-FileHash -LiteralPath $source -Algorithm SHA256).Hash.ToLowerInvariant()
if ($sourceSha -ne $expectedSourceSha) {
    throw "Unexpected live source SHA-256: $sourceSha"
}
$lines = [System.IO.File]::ReadAllLines($source)
if ($lines.Count -ne 5485) {
    throw "Unexpected source length: $($lines.Count) lines"
}
if ($lines[3143] -ne '\end{exercise}') {
    throw "Unexpected target line 3144: $($lines[3143])"
}
if ($lines[3145] -notmatch '^%{78}$' -or $lines[3146] -ne '') {
    throw 'Unexpected section-closing separator at target lines 3146-3147'
}
if ($lines[3147] -ne '\sectionnewpage') {
    throw "Unexpected target line 3148: $($lines[3147])"
}
if ($lines[3148] -ne '\section{The Stone--Weierstrass theorem}') {
    throw "Unexpected target line 3149: $($lines[3148])"
}
if ($lines[3149] -ne '\label{sec:stoneweier}') {
    throw "Unexpected target line 3150: $($lines[3149])"
}

$prefix = (($lines[0..3146] -join "`n") + "`n")
$prefixBytes = [System.Text.UTF8Encoding]::new($false).GetBytes($prefix)
$prefixSha = [Convert]::ToHexString(
    [System.Security.Cryptography.SHA256]::HashData($prefixBytes)
).ToLowerInvariant()
if ($prefixSha -ne $expectedPrefixSha) {
    throw "Unexpected admitted-prefix SHA-256: $prefixSha"
}

$payload = $prefix + "% Deterministic reader cutoff after the admitted Arzela--Ascoli section.`n"
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
    Pop-Location
}
