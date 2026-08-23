# R008 complex analysis — translation unit U001

Status: translated, bounded QA passed; not yet integrated into the R008 full
driver or any publication surface.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **556–667** (the complete `Introduction` chapter,
  including its epigraph, prose, dependency diagram, labels, and references).
- Source slice (UTF-8 with LF): 4,986 bytes;
  SHA-256 `6b7d346e0120c43958c910a1fed25aaf5668c3017076adb4c1f9dafc7e1dbe65`.
- Target: `translation/complex-analysis/ca-introduction-id.tex`.
- Target translated payload: lines **8–114** (header/provenance comments are
  lines 1–6); 5,440 bytes UTF-8 with LF;
  SHA-256 `8f69f74b169b2305bd2464c9d0b086213ae03241e7259172d5c1d9f01561dc8d`.
- Target file: 5,893 bytes;
  SHA-256 `4ffb0459d02ba11875e8331bf585f3b4d7984db5309dd30528942c5b2d324eb3`.

## Structural QA

The translated payload preserves the source's structural command inventory:

- 65 opening and 65 closing braces;
- 12 unescaped math-dollar delimiters;
- 3 `\\begin` and 3 `\\end` environments (`myepigraph`, `equation*`,
  `tikzcd`);
- 1 chapter label and all source cross-reference/bibliography keys;
- command counts match the source slice for `\\Chdotref` (10), `\\ref` (9),
  `\\myquote` (5), `\\text` (10), `\\arrow` (9), `\\R` (2), and every other
  command (including the TikZ dependency diagram).

No unmatched braces/environments, mojibake, or accidental source mutation was
found. English-looking tokens in the file are limited to intentional LaTeX
commands/provenance metadata and proper names (Oscar Wilde, Oklahoma State
University, Wirtinger, Cauchy--Riemann, Weierstrass, Runge, Montel, Riemann).

## Terminology decisions

- `complex analysis` → **analisis kompleks**.
- `holomorphic function` → **fungsi holomorf**; `line integral` → **integral
  garis**; `metric space` → **ruang metrik**; `harmonic analysis` → **analisis
  harmonik**.
- `differentiable` → **diferensiabel**, with `complex differentiable` rendered
  **diferensiabel kompleks** and the real-sense clarification retained.
- `mapping of the plane` → **pemetaan bidang**; `cycle homologous to zero` →
  **siklus yang homolog dengan nol**.

The source's mathematical notation, labels, citation keys, and diagram graph
were not translated or renamed.

## Next cursor

The next contiguous R008 reader-facing unit begins at source line **673**:
`\\chapter{The Complex Plane}` (the introduction ends at line 667; lines
668–672 are separator comments). Continue in a new unit file under
`translation/complex-analysis/`, preserving all source labels and macros.

Provenance retained in the target comments and this receipt: **OpenAI Codex
gpt-5.6-sol, Ultra**, acting on the user's request. No author contact or
publication was performed here.
