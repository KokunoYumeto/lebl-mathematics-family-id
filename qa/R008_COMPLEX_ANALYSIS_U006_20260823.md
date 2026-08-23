# R008 complex analysis — translation unit U006

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **837–866**, the geometry/topology subsection through
  the statement of the Cauchy–Schwarz and triangle inequalities proposition.
- Source slice (UTF-8 with LF): 1,133 bytes;
  SHA-256 `4da4f1d55d1822fa40fd5b9b6623ab2c6a6cf4f91611e3df7f8f8b25ffcdc362`.
- Target: `translation/complex-analysis/ca-geometry-modulus-id.tex`.
- Target translated payload: lines **7–38** (provenance header/comments are
  lines 1–6); 1,193 bytes UTF-8 with LF;
  SHA-256 `aa7d9971117bfb258b9b50067ef8b63de22a05a3c4608950b354929acb8838c4`.
- Target file: 1,584 bytes;
  SHA-256 `07bfd22e8bdad3f93edcefe7f390cec2490d6e2cf12195bf3717474c6bfd0ebd`.

## Structural QA

- 11 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 35 opening and 35 closing braces; 22 unescaped math-dollar delimiters.
- 3 `\\begin`/`\\end` pairs (`equation*`, `prop`, `enumerate`).
- Exact source command inventory, including 10 `\\sabs`, 4 `\\bar`, 2
  `\\Re`, both `\\index` keys, `\\glsadd{not:mod}`, and all inequality/
  environment commands.
- No unmatched delimiters, mojibake, or changed notation/index hooks.

## Terminology decisions

- `modulus` → **modulus**; `Euclidean distance` → **jarak Euclidean**;
  `origin` → **titik asal**.
- `Cauchy--Schwarz inequality` → **ketaksamaan Cauchy--Schwarz**;
  `triangle inequality` → **ketaksamaan segitiga**; `dot product` → **hasil
  kali titik**.
- The source naming footnote is translated faithfully, including its
  Cauchy–Bunyakovsky–Schwarz qualification; index keys remain source-stable.

## Next cursor

The next contiguous R008 unit begins at source line **868**:
`\\begin{proof}` for the proposition just stated. Continue in a new file under
`translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
