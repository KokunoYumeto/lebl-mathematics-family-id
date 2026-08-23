# R008 complex analysis — translation unit U012

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **936–959**, basic neighborhoods/discs, the radius-$r$
  disc, and the unit disc.
- Source slice (UTF-8 with LF): 657 bytes;
  SHA-256 `34f336e90a516ba322994348705067ba07b7789f5fafc5ef2b8cb7a454425729`.
- Target: `translation/complex-analysis/ca-discs-id.tex`.
- Target translated payload: lines **7–29** (provenance header/comments are
  lines 1–6); 689 bytes UTF-8 with LF;
  SHA-256 `434cc4f2693c98c329d85ee35b286ee5a521a21d23af717a8b9adc19a5957a07`.
- Target file: 1,062 bytes;
  SHA-256 `da961423eef288a4eae1c099c7c5b06f9728a7a28e6876d40d21d0f2c00acde0`.

## Structural QA

- 6 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 20 opening and 20 closing braces; 12 unescaped math-dollar delimiters.
- 2 `\\begin`/`\\end` pairs (`equation*` × 2); exact command inventory,
  including `\\glsadd{not:disc}`, `\\glsadd{not:D}`, `\\Delta`, `\\D`, and
  both `\\myindex` hooks.
- No unmatched delimiters, mojibake, or changed notation/glossary keys.

## Terminology decisions

- `neighborhood` → **lingkungan**; `open ball` → **bola terbuka**;
  `disc` → **cakram**; `unit disc` → **cakram satuan**.
- `radius` → **jari-jari**; `centered at the origin` → **berpusat di titik
  asal**. Index display terms are Indonesian while source glossary keys remain
  stable.

## Next cursor

The next contiguous R008 unit begins at source line **961** (`A useful
\myquote{version} of the unit disc ...`), after the blank separator at line
960. Continue in a new file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
