# R006 localization opening, Lipschitz theorem, and piecewise-smooth corollary — U410–U412

Status: **PASS after one minimal source-side precision correction**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact admitted units

1. `ra.v2.fourier-series.localization.opening`
   - frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4982–4985, 4 LF lines / 127 bytes, SHA-256 `e8f78e8d509d91581dcd8a2c22abc51fa8a1c928509d75497b964a687bd8169b`;
   - Indonesian target: `translation/ra/ch-approximate.tex`, raw lines 4996–4999, 4 LF lines / 124 bytes, SHA-256 `4228eae59be812de85338279b8d4f23ca598cc8368b4f7b1675a4154fa9334d7`.
2. `ra.v2.fourier-series.localization.lipschitz-theorem`
   - frozen source: raw lines 4987–4998, 12 LF lines / 381 bytes, SHA-256 `21904abd2891278211d0289e2026bcdd313738751d61d62769758137e1737bb7`;
   - Indonesian target: raw lines 5001–5012, 12 LF lines / 413 bytes, SHA-256 `e39ecfea98d224411a98ddafd3dfd2b7787913ae3a1303fc60faf6e0dbe53dc0`.
3. `ra.v2.fourier-series.localization.piecewise-smooth-corollary`
   - frozen source: raw lines 5000–5023, 24 LF lines / 869 bytes, SHA-256 `6be70f4a160f96fe1fc374d90b5e895035e593e0c6e8d370acf891408475c5b5`;
   - Indonesian target: raw lines 5014–5037, 24 LF lines / 977 bytes, SHA-256 `f5bb8c1762539e0d92cb81ae7a082a21d8ac6d6a4c7f45d255b61d83631ad8a1`.

The live target after these units is 5,487 LF lines / 196,788 bytes, SHA-256
`ea1aaae66fc5d19826392aebfea0bac8cb0ca29e94a7c384d21d605fd82106b4`.

## Mathematical and structural audit

An independent no-edit source/target audit found that the translation preserves
the localization claim, the pointwise Lipschitz hypothesis, both displayed
Fourier-series formulas, the continuous piecewise-smooth definition, and the
corollary's arithmetic-mean convergence conclusion. The `thm`, `cor`, and three
`equation*` environment pairs occur in exactly the same order. Labels
`thm:fourierlocalization` and `cor:fourierpiecewisesmooth`, both index commands,
and all theorem/corollary boundaries are unchanged.

Across the three units there are 23 inline-math spans and three displayed-math
payloads. The three displays and 22 inline payloads are byte-identical. The sole
inline difference is the declared correction ADV-0262: source `$j$` becomes
target `$j=0,1,\ldots,k-1$`. The source command stream has 44 commands and the
target has 45; after removing the correction's added `\ldots`, the ordered
streams are identical. No formula, hypothesis, conclusion, label, or reference
changed otherwise.

## Declared source correction

After defining `x_0=a<x_1<...<x_k=b`, the source requires continuous
differentiability on `[x_j,x_{j+1}]` “for every j.” Literally, `j=k` refers to
undefined `x_{k+1}`. ADV-0262 makes the intended finite-partition range explicit
as `j=0,1,...,k-1`. This is the minimal mathematically necessary repair; the
definition and corollary are otherwise preserved verbatim in mathematical
content. No upstream contact occurred.

## Indonesian terminology and reader quality

The independent audit judged the prose natural and complete. The ledger admits
TERM-0789 `localization` → `lokalisasi`, TERM-0790 `Lipschitz condition` →
`syarat Lipschitz`, and TERM-0791 `continuous piecewise smooth` → `kontinu dan
mulus sepotong-sepotong`. The latter keeps global continuity distinct from
continuous differentiability on each closed subinterval. No reader-facing
English residue, exercise, solution, asset, or O001 solution gap occurs here.

At this boundary the terminology ledger has 791 data rows / 126,226 bytes,
SHA-256 `831ccd8437d2d06b787cf9fa5fe6a410af413cc7369ccad76ec64cf909c8e778`.
The adverse ledger has 262 rows / 242,925 bytes, SHA-256
`b5a51f070101ca61e52d76ab96c82d89b30aaa6d029c98e085d56c77b624c4ed`.

## Deterministic integration build

The complete Volume-II driver was built with the bound complete Indonesian
Volume-I auxiliary label set `realanal.aux`, 354,013 bytes, SHA-256
`8696b0f4e80ddfe0093da26955f868304892bf081eb01c04d21feedd1815d5c2`.
After `makeindex`, `makeglossaries`, and two final `pdflatex -halt-on-error`
passes, the non-release integration PDF is 241 pages / 2,428,467 bytes,
SHA-256 `3972f7d275c6d21f007149428a87c2755ffb19e3427c28d3f9a540430e596199`.
The final log is 104,268 bytes, SHA-256
`54e8101b857372b61c3d069f5bd7217c5b15e77d2392942ceb1a2cda40609726`.
It contains zero undefined references, multiply-defined labels, rerun warnings,
missing-character warnings, undefined control sequences, LaTeX/package errors,
fatal errors, or emergency stops. The 15 overfull horizontal boxes are inherited
outside this unit; there are zero overfull vertical boxes. The generated build
directory is transient and is not a release artifact.

Next exact boundary: frozen source raw line 5025 / live target raw line 5039,
the proof of the Lipschitz localization theorem.
