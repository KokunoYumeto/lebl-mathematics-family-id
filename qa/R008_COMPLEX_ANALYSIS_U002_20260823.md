# R008 complex analysis — translation unit U002

Status: translated, bounded structural QA passed; not integrated into the
R008 full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **673–733**, from `\\chapter{The Complex Plane}`
  through the end of the opening section (immediately before source line 734,
  `\\subsection{The complex numbers as the plane}`).
- Source slice (UTF-8 with LF): 2,640 bytes;
  SHA-256 `4f4e9cb0411c8c3c72e7dd0484a7e6fd31edf8d786efd20ab827933a5b41797c`.
- Target: `translation/complex-analysis/ca-complex-plane-opening-id.tex`.
- Target translated payload: lines **7–70** (provenance header/comments are
  lines 1–6); 3,053 bytes UTF-8 with LF;
  SHA-256 `0d0b0a076e82fe81c284560e524e3dc497608ad7ea8c7189cc2302bd7d927863`.
- Target file: 3,438 bytes;
  SHA-256 `b8429ed41de648809b77a549c58aeb9fd453007bab9806a9034a9a2bf9d66b37`.

## Structural QA

- 16 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 26 opening and 26 closing braces; 32 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`myepigraph`).
- Exact source command inventory: `\\chapter` 1, `\\section` 1,
  `\\label` 2, `\\footnote` 3, `\\glsadd` 5, `\\myquote` 5,
  `\\nicefrac` 2, `\\N` 1, `\\Z` 2, `\\Q` 2, `\\R` 1,
  `\\sqrt` 1, and all remaining commands unchanged.
- No unmatched delimiters, mojibake, or changed glossary hooks/labels.

## Terminology decisions

- `complex plane` → **bidang kompleks**; `complex numbers` → **bilangan
  kompleks**.
- `natural numbers` → **bilangan asli** (the conventional Indonesian field
  term); `integers` → **bilangan bulat**; `rational numbers` → **bilangan
  rasional**; `real numbers` → **bilangan real**.
- `root` → **akar**; `polynomial` → **polinom**; `complex analysis` →
  **analisis kompleks**; `counterexample` → **contoh tandingan**.
- The source's humorous tone and all attribution/footnote content are retained;
  mathematical notation and glossary keys are untouched.

## Next cursor

The next contiguous R008 unit begins at source line **734**:
`\\subsection{The complex numbers as the plane}`. Continue in a new file under
`translation/complex-analysis/`, preserving the source's labels, glossary
hooks, exercises, and equation structure.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
