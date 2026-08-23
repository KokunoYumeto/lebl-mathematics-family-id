# R008 complex analysis — translation unit U011

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **930–934**, the exercise asking the reader to prove
  the preceding continuity proposition.
- Source slice (UTF-8 with LF): 97 bytes;
  SHA-256 `fb84885907feb395d4fc128d40bd77ada3a1a8275a4f1ababb5ca860057ca1cd`.
- Target: `translation/complex-analysis/ca-continuity-exercise-id.tex`.
- Target translated payload: lines **7–11** (provenance header/comments are
  lines 1–6); 103 bytes UTF-8 with LF;
  SHA-256 `e2b7463bd14c88aa0781dcc1acbd76b3247b6fa38dd77840f65efef9e6738c4d`.
- Target file: 463 bytes;
  SHA-256 `4811b6dc90dbc9ca25b6386e529d66adb416d3d15d558932cc4a053d766e60ba`.

## Structural QA

- No math delimiters in the source unit; 4 opening and 4 closing braces.
- 2 `\\begin`/`\\end` pairs (`exbox`, `exercise`); exact `\\neededexmark`
  option hook preserved.
- No unmatched delimiters or mojibake; the exercise remains an exercise and no
  solution was introduced.

## Terminology decisions

- `Prove the proposition` → **Buktikan proposisi tersebut**.

## Next cursor

The next contiguous R008 unit begins at source line **936** (`The basic
neighborhood ...`); line 935 is blank. Continue in a new file under
`translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
