# R006 best-`L^2`-approximation theorem — U319 QA receipt

Date: 2026-08-27  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.orthonormal-systems.best-l2-approximation`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4713–4803
  inclusive, 91 LF lines, 1,839 bytes, SHA-256
  `d7a6f84cad7991287755446c64c08f40ba59294a8fdc479ec61644f26730984a`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4727–4817 inclusive, 91 LF lines, 1,912 bytes, SHA-256
  `c636447d9871178b31265bab1a8db543d0b261428c9d137b313fd653083dc07b`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target is 5,487 lines / 196,220 bytes, SHA-256
  `fee5eec4f67c6f2bd9ff434afb7165cbae05f98c5d27d1fd55b4ac9d5f052491`.

## Deterministic structural and mathematical audit

- Source and target each contain 111 TeX command occurrences. Their ordered
  command streams are identical, SHA-256
  `7060a9c7b25537908dcac2bcd6c093f78c7937ea81377aceb914049dd78a3dfe`.
- Each range has 20 balanced and identically ordered environment markers and
  the exact label `thm:l2bestapprox`.
- All nine inline-math payloads are byte-identical and ordered, sequence
  SHA-256
  `25c9b0a080e87751d37972b1171bd44d05eb7901ea308d70c2a36c7d533a26ff`.
- All seven display blocks are byte-identical after localizing only the literal
  `\text{and}` as `\text{dan}`; their normalized sequence SHA-256 is
  `544ddfc8c01195fd0ca39e5a3d68799e39f5ec1212234322e470da0fce8c7c0e`.
- Both ranges have balanced 71/71 braces and 18 unescaped dollar delimiters.
- Independent review confirmed the hypotheses, inequality direction,
  coefficient ranges, conjugations, expansion of the squared error, equality
  condition, and exact minimizer are mathematically preserved.

## Indonesian and terminology audit

The reader-facing prose is natural Indonesian and contains no unintended
English residue. `Terintegralkan secara Riemann`, `sistem ortonormal`, `norma
L^2`, and related expressions reuse admitted terminology. One new binding is
admitted:

- `LEBL-TERM-0784`: best approximation → `aproksimasi terbaik`.

The terminology ledger has 784 data rows / 123,576 bytes, no duplicate IDs,
SHA-256 `af0ba42110cfb023733d256e2b0cc1d0998c1dd69385aea44e650f485dcf0e9b`.
Independent final mathematical and Indonesian-language review returned PASS.

No source correction, asset, exercise, solution, or O001 gap occurs in this
unit. The formulas remain governed by the seminorm/quotient qualification
already recorded as ADV-0259 in U318; U319 introduces no further change.

Next exact boundary: frozen source raw line 4805 / live target raw line 4819,
the finite-sum estimate leading to Bessel's inequality.
