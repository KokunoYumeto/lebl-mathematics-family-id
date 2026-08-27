# R006 orthonormal-systems opening — U318 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.orthonormal-systems.inner-product-and-expansion`  
Result: PASS after declared mathematical correction ADV-0259

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4612–4711
  inclusive, 100 LF lines, 3,304 bytes, SHA-256
  `dc93b2f987d543163b598eae221531cb04585e6bc51a6e5094a979b58b76dd94`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4620–4725 inclusive, 106 LF lines, 3,967 bytes, SHA-256
  `ac657ef99317cd4719e92058b486b1f9f996010aecbfa7873e37a51639b12ff9`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target is 5,487 lines / 196,147 bytes, SHA-256
  `7a687eec16cf291edc5a331fe7b37695cd42ec071175af258a0d9a363e505524`.

## Deterministic structural and mathematical audit

- All 25 original inline-math payloads are byte-identical and ordered.
- All nine original display payloads are exact after localizing only the two
  literal case labels `if` and `otherwise` as `jika` and `selain itu`.
- The source has 115 TeX command occurrences and 24 environment events. The
  target preserves them in order and adds only one declared `remark` pair,
  yielding 117 commands and 26 environment events.
- Brace balance is 67/67 in the source and 69/69 in the target; both ranges
  contain 50 unescaped dollar delimiters and one corresponding prose comment.
- Inner-product argument order and conjugation, both `L^2` formulas, finite-
  dimensional sums, orthonormal/orthogonal cases, all index bounds, the
  normalization factor, Fourier coefficients, formal series, and projection
  analogy passed independent mathematical review.

## Indonesian and terminology audit

The prose is natural Indonesian, uses the established preferred form
`terintegralkan secara Riemann`, and contains no unintended English
reader-facing residue. New bindings are:

- `LEBL-TERM-0776`: function space → `ruang fungsi`;
- `LEBL-TERM-0777`: inner product → `hasil kali dalam`;
- `LEBL-TERM-0778`: Hermitian inner product →
  `hasil kali dalam Hermitian`;
- `LEBL-TERM-0779`: L2 norm → `norma L^2`;
- `LEBL-TERM-0780`: orthonormal system → `sistem ortonormal`;
- `LEBL-TERM-0781`: orthogonal system → `sistem ortogonal`;
- `LEBL-TERM-0782`: orthogonal projection → `proyeksi ortogonal`;
- `LEBL-TERM-0783`: seminorm → `seminorma`.

The terminology ledger has 783 data rows / 123,213 bytes, no duplicate IDs,
SHA-256 `417e6cad97095f38393d342b6e376537b993b108d3858cd029ba0059f6edb082`.

## Declared source correction

ADV-0259 records a P2 mathematical defect. On pointwise-defined Riemann-
integrable functions, the displayed pairing is degenerate: a nonzero function
supported at one point has integral of its squared modulus equal to zero.
Consequently the induced quantity is a seminorm, not a norm. Both become a
genuine inner product and norm after functions equal almost everywhere are
identified. The Indonesian derivative adds one concise remark giving the
counterexample and quotient remedy; it changes none of the original formulas
or claims outside this qualification.

The adverse ledger now has 259 rows / 239,015 bytes, SHA-256
`91eaef05792c68e935aa9a923219783ca296e7de1d84a0f9488fff714b2b84d5`.
Independent final mathematical, structural, and Indonesian-language review
judged the correction exact and minimal. No asset, exercise, solution, or O001
gap occurs in this unit.

Next exact boundary: frozen source raw line 4713 / live target raw line 4727,
the best-`L^2`-approximation theorem and proof.
