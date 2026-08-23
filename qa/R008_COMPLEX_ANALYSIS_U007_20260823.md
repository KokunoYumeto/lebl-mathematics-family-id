# R008 complex analysis — translation unit U007

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **868–890**, proof of the Cauchy–Schwarz and triangle
  inequalities proposition.
- Source slice (UTF-8 with LF): 833 bytes;
  SHA-256 `eb60f7868564bcf3b1bd6d3c88c5e688942b827215a0d650aa80f068923c0d82`.
- Target: `translation/complex-analysis/ca-geometry-proof-id.tex`.
- Target translated payload: lines **7–29** (provenance header/comments are
  lines 1–6); 852 bytes UTF-8 with LF;
  SHA-256 `6097d9c70194478ee34f3898ff772fa3e254914cfe0e4b043f58018843361562`.
- Target file: 1,218 bytes;
  SHA-256 `812405c726f280b3e2721b07b471c9742f22e46c7358ce640c9b32ab8b7e9b28`.

## Structural QA

- Both `equation*` blocks (including their `split` structures) have ordered,
  whitespace-normalized mathematical payloads identical to the source.
- 47 opening and 47 closing braces; no dollar-delimited math in this source
  slice (all formulae are inside display environments).
- 5 `\\begin`/`\\end` pairs; exact command inventory (`\\sabs` 8,
  `\\bar` 23, `\\bigl`/`\\bigr` 3 each, `\\leq` 2, `\\Re`, `\\qedhere`,
  and all environment commands).
- No unmatched delimiters, mojibake, or changed equation structure.

## Terminology decisions

- `modulus squared` → **kuadrat modulus**; `nonnegative` → **taknegatif**;
  `triangle inequality` → **ketaksamaan segitiga**.
- The proof's logical connectors (`Thus`, `This proves`, `via`) are rendered as
  **Dengan demikian**, **Ini membuktikan**, and **melalui** without changing
  mathematical scope.

## Next cursor

The next contiguous R008 unit begins at source line **892** (`\\begin{exbox}`
for the polarization-identity exercise); line 891 is blank. Continue in a new
file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
