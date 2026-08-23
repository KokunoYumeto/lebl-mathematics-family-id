# R008 complex analysis — translation unit U016

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **1003–1014**, component-wise partial derivatives of a
  complex-valued function.
- Source slice (UTF-8 with LF): 420 bytes;
  SHA-256 `e155015cb7761bec5b9a251ed7903b4ffe2dad299add89dc80235d72fb6b0105`.
- Target: `translation/complex-analysis/ca-component-derivatives-id.tex`.
- Target translated payload: lines **7–18** (provenance header/comments are
  lines 1–6); 439 bytes UTF-8 with LF;
  SHA-256 `1b156b0fc42563cfe1f0119581eea0595692209be9421245704febc6055ec4bc`.
- Target file: 810 bytes;
  SHA-256 `c64963dca8bd9b4b7ba9162f63fb56bd8a6e0f595cd27ac59bed51836950954b`.

## Structural QA

- 7 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 15 opening and 15 closing braces; 14 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`equation*`); exact `\\partial` (12), `\\frac`
  (6), `\\subset`, `\\C`, `\\R`, `\\qquad`, and text-command inventory.
- No unmatched delimiters, mojibake, or changed derivative equation.

## Terminology decisions

- `derivative in $x$ or $y$` → **turunan terhadap $x$ atau $y$**;
  `component` → **komponen**; `real vector space` → **ruang vektor real**.
- The source's parenthetical “as if $f$ were valued in $\R^2$” is retained as
  **seolah-olah $f$ bernilai di $\R^2$**.

## Next cursor

The next contiguous R008 unit begins at source line **1016** (`If $X \subset
\R$, that is, if $f$ is a complex-valued ...`); line 1015 is blank. Continue in
a new file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
