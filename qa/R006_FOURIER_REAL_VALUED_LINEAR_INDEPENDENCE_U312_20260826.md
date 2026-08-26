# R006 Fourier real-valued criterion and linear independence — U312

Status: **PASS; translated and independently verified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.fourier-series.trigonometric-polynomials.real-valued-criterion-and-linear-independence`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4307–4361 inclusive; 55 LF-terminated lines, 1,308 bytes, SHA-256 `1f1df63e3dbaf654c6f1a55a4b27075aec4081ef69a0e866c2dc26a84db35634`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4315–4369 inclusive; 55 LF-terminated lines, 1,353 bytes, SHA-256 `3ba524f76f9108be2dd3043dd314aa01eb4e7a58152eb9d017c129f3142a28dc`.
- Full live R006 target after U312: 194,506 bytes, 5,481 LF lines, SHA-256 `3de28aaac5ce08b69e97060ea01fe7f1d0e7b9d1c024e2fad49e9ece3893b839`.

## Mathematical and structural QA

- Ordered TeX controls are exact: 56 source / 56 target.
- Environment topology is exact: fourteen events comprising two `prop` pairs, two `proof` pairs, and three `equation*` pairs.
- All fifteen inline-math payloads and all three display payloads are byte-identical and ordered.
- Source and target each have 56 opening / 56 closing braces and 30 balanced dollar delimiters.
- Independent post-correction audit confirms necessity through coefficient recovery and conjugation under the integral, sufficiency through pairing the `m` and `-m` terms plus real `c_0`, and linear independence through the coefficient formula.

## Indonesian QA and terminology

The one initial English residue `then` was replaced by `maka`, and the universal quantifier is rendered explicitly as `untuk setiap x real`. Independent re-read then passed with no other English residue. Established terminology is exact: `polinom trigonometri`, `bernilai real`, `konjugat kompleks`, `bagian real`, `bagian imajiner`, and `bebas linear`. No new term, source correction, asset, exercise, solution, or O001 gap is introduced.

The next contiguous boundary begins at source raw line 4363 / target raw line 4371 with the `Fourier series` subsection.

