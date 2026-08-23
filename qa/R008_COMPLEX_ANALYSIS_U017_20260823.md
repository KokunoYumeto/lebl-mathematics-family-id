# R008 complex analysis — translation unit U017

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **1016–1036**, one-real-variable derivatives,
  component-wise complex integration, and the basic modulus integral bound.
- Source slice (UTF-8 with LF): 932 bytes;
  SHA-256 `5b4f27c2f33147487572cba0850e34178c98ce9fc32e8ed254a410fd13abe30d`.
- Target: `translation/complex-analysis/ca-complex-integration-setup-id.tex`.
- Target translated payload: lines **7–28** (provenance header/comments are
  lines 1–6); 1,028 bytes UTF-8 with LF;
  SHA-256 `432430c0c4f45374f8fbabfdfe9f482a7231ae895442a890626c7a16f4d63e49`.
- Target file: 1,414 bytes;
  SHA-256 `21cb2a0948dad3ab89bbb53ef169eee921c6177e6777d8fcdaed5a6fc4e63662`.

## Structural QA

- 19 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 5 opening and 5 closing braces; 38 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`equation*`); exact command inventory (`\\int`
  5, `\\abs` 2, `\\sabs` 1, `\\R` 6, `\\C` 3, `\\leq`, and all mappings).
- No unmatched delimiters, mojibake, or changed integration equation/inequality.

## Terminology decisions

- `integrable` → **terintegralkan**; `Riemann integrable` → **terintegralkan
  (Riemann)**; `vector-valued function` → **fungsi bernilai vektor**.
- `one real variable` → **satu variabel real**; `column vector` → **vektor
  kolom**; `basic analysis` → **analisis dasar**.

## Next cursor

The next contiguous R008 unit begins at source line **1038** (`\\begin{prop}`
with label `prop:inttriangleineq`); line 1037 is blank. Continue in a new file
under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
