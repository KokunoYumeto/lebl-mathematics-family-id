# R006 coefficient decay and continuity — U316 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.decay.absolute-uniform-continuity`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4539–4566
  inclusive, 28 LF lines, 1,218 bytes, SHA-256
  `a8ac1e6ed75dc915a90cfd1565059eb1001aa1b1194248ceff5950da546d8d51`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4547–4574 inclusive, 28 LF lines, 1,319 bytes, SHA-256
  `af2082f356ba7638497f0dd3e27134dc5f16976e857d33377f103843db468316`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.

## Deterministic structural and mathematical audit

- Both ranges contain 28 lines, 29 TeX command occurrences, three
  environments, 18 balanced brace pairs, and 12 unescaped dollar delimiters.
- The two display-math payloads are exact after localizing only the literal
  phrase `\text{for all }` as `\text{untuk setiap }`.
- The bilateral Fourier series, exclusion of `n=0`, coefficient bound,
  hypothesis `alpha>1`, absolute and uniform convergence, continuity
  conclusion, and both theorem references are preserved exactly.
- Independent review confirmed that the bilateral Weierstrass M-test argument
  is sound: the finite `c_0` term is harmless and both nonzero tails are
  controlled by the convergent p-series.

## Indonesian and terminology audit

The prose is natural Indonesian and contains no unintended English
reader-facing residue. The translation distinguishes the regularity of a
function from the decay rate of its coefficients and preserves the source's
progression from the motivating sine series to the general criterion.

New bindings:

- `LEBL-TERM-0773`: regularity → `regularitas`;
- `LEBL-TERM-0774`: rate of decay → `laju peluruhan`;
- `LEBL-TERM-0775`: Weierstrass M-test → `uji M Weierstrass`.

The terminology ledger has 775 data rows / 120,808 bytes, no duplicate IDs,
SHA-256 `f66d54dafb0ae30c610a070e398131dde648198f75dacd5088969ad6714da05f`.
No source correction, asset, exercise, solution, or O001 gap occurs in this
unit.

Independent mathematical, structural, and Indonesian-language review passed
without correction. Next exact boundary: frozen source raw line 4568 / live
target raw line 4576, the differentiability and higher-regularity consequence.
