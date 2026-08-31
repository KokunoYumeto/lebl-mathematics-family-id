# R006 Fourier differentiability and higher regularity — U317 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.decay.differentiability-and-higher-regularity`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4568–4610
  inclusive, 43 LF lines, 1,437 bytes, SHA-256
  `0c4e5ac8362298bbe33e528a8c3e0c73368e35ab0f8614b3b937a2dc93184138`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4576–4618 inclusive, 43 LF lines, 1,661 bytes, SHA-256
  `8c9881fdcf9e5070867de119556d597d93d47713fd4592b746fb9c968af2698d`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.

## Deterministic structural and mathematical audit

- All 12 inline-math payloads are byte-identical. All four display payloads
  are exact after localizing only `\text{for all }` as
  `\text{untuk setiap }`.
- The ordered TeX control stream and all ten environment events are exact;
  both ranges have 33 opening and 33 closing braces and 24 unescaped dollar
  delimiters. `\avoidbreak` and the sole cross-reference
  `\thmref{thm:dersconvergecomplex}` are preserved.
- Independent review passed the complete argument: `alpha>2`, the nonzero-index
  coefficient bound, derivative coefficients `i n c_n`, exponent shift to
  `alpha-1`, uniform convergence by the M-test, convergence at one point,
  identification of the derivative series, and iteration under
  `alpha>k+1` to obtain continuous differentiability through order `k`.

## Indonesian and terminology audit

The prose is natural Indonesian and contains no unintended English
reader-facing residue. It consistently reuses:

- `LEBL-TERM-0247`: continuously differentiable →
  `diferensiabel secara kontinu`;
- `LEBL-TERM-0480`: k-times continuously differentiable →
  `diferensiabel secara kontinu hingga orde k`;
- `LEBL-TERM-0773`: regularity → `regularitas`.

No new term, source correction, asset, exercise, solution, or O001 gap occurs
in this unit. Independent mathematical, structural, and Indonesian-language
review passed without correction.

Next exact boundary: frozen source raw line 4612 / live target raw line 4620,
the subsection `Orthonormal systems` / `Sistem ortonormal`.
