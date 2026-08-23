# R008 complex analysis — translation unit U008

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **892–898**, the polarization-identity exercise.
- Source slice (UTF-8 with LF): 204 bytes;
  SHA-256 `0663ef914db22da27dfffa7762db42333a2cf279c68eb5ec63725d8a523cb896`.
- Target: `translation/complex-analysis/ca-polarization-exercise-id.tex`.
- Target translated payload: lines **7–13** (provenance header/comments are
  lines 1–6); 203 bytes UTF-8 with LF;
  SHA-256 `c1d7848d18b6085d7065c5ba34548bf12ab95f4844075dd9ac0ae6d0a97e64dd`.
- Target file: 586 bytes;
  SHA-256 `55a441d35ca77df06f0a9224062627e114051fc7bd8544a5167a44c4c55ca3c7`.

## Structural QA

- One ordered math-mode segment; the polarization-identity payload matches the
  source after whitespace normalization.
- 15 opening and 15 closing braces; 2 unescaped math-dollar delimiters.
- 2 `\\begin`/`\\end` pairs (`exbox`, `exercise`); exact command inventory,
  including all four `\\sabs` calls and the `\\myindex` hook.
- No unmatched delimiters, mojibake, or changed formula structure.

## Terminology decisions

- `polarization identity` → **identitas polarisasi**.
- The exercise remains an exercise (not a solution); all mathematical notation
  and source indexing are unchanged.

## Next cursor

The next contiguous R008 unit begins at source line **900** (`The distance
between two numbers $z$ and $w$ ...`); line 899 is blank. Continue in a new file
under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
