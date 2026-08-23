# R008 complex analysis — translation unit U013

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **961–972**, the upper-half-plane definition and its
  equivalence with the unit disc.
- Source slice (UTF-8 with LF): 362 bytes;
  SHA-256 `e8933656d70f275200beab9e05f47315b30e1932eb88e943d8a49ee0f2e64d5c`.
- Target: `translation/complex-analysis/ca-upper-half-plane-id.tex`.
- Target translated payload: lines **7–20** (provenance header/comments are
  lines 1–6); 412 bytes UTF-8 with LF;
  SHA-256 `d5f507703d913435b6b5b18290ea1c6071a98c6eab4f6f2ee7c1af9d9538d93c`.
- Target file: 785 bytes;
  SHA-256 `8c243c571f2b433d80c2efa22bf7dafdcbced03c02747f57561811eed81c60d9`.

## Structural QA

- 2 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 10 opening and 10 closing braces; 4 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`equation*`); exact `\\bH`, `\\D`, `\\C`,
  `\\Im`, `\\glsadd{not:H}`, and index/quote hooks preserved.
- No unmatched delimiters, mojibake, or changed set notation.

## Terminology decisions

- `upper half-plane` → **setengah bidang atas**; `equivalent` → **ekuivalen**;
  `version` → **versi**.
- The source's distinction between the unit disc and upper half-plane remains
  explicit and reader-facing.

## Next cursor

The next contiguous R008 unit begins at source line **974** (`The following
definition ...`), after the blank separator at line 973. Continue in a new file
under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
