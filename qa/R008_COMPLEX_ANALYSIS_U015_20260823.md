# R008 complex analysis — translation unit U015

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **987–1001**, introduction to complex-valued
  functions and decomposition into real components.
- Source slice (UTF-8 with LF): 658 bytes;
  SHA-256 `35fc6f343832a93300f122251f8a839a90804077dae36cf7b5fa8229841e03fb`.
- Target: `translation/complex-analysis/ca-complex-valued-functions-id.tex`.
- Target translated payload: lines **7–21** (provenance header/comments are
  lines 1–6); 651 bytes UTF-8 with LF;
  SHA-256 `fcc2b6f3a810c879790405666f19595b73a210acfd8fb7d8d4ad2ac7b3101b4d`.
- Target file: 1,033 bytes;
  SHA-256 `16cad7938d26bea2db6380cda78a8eba23e722a0858102d1d07685be3e13fb0b`.

## Structural QA

- 9 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 3 opening and 3 closing braces; 18 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`equation*`); exact `\\R`, `\\C`, `\\Re`,
  `\\Im`, `\\colon`, and `\\to` command inventory.
- No unmatched delimiters, mojibake, or changed component equation.

## Terminology decisions

- `complex-valued function` → **fungsi bernilai kompleks**;
  `real-valued function` → **fungsi bernilai real**; `component` → **komponen**.
- `real vector space` → **ruang vektor real**; `separately` → **secara
  terpisah**.

## Next cursor

The next contiguous R008 unit begins at source line **1003** (`If $X \subset
\C$, we think of $X \subset \R^2$ ...`); line 1002 is blank. Continue in a new
file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
