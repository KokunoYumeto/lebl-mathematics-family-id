# R008 complex analysis — translation unit U004

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **761–786**, real-number embedding, the imaginary unit,
  Cartesian form, and the first statement about polynomial roots.
- Source slice (UTF-8 with LF): 1,057 bytes;
  SHA-256 `a4d6df9d0980ddbb96eda2c26b404dc973ce914abed6f06bc78a8a71ecfe9e15`.
- Target: `translation/complex-analysis/ca-imaginary-unit-id.tex`.
- Target translated payload: lines **7–33** (provenance header/comments are
  lines 1–6); 1,126 bytes UTF-8 with LF;
  SHA-256 `b6a6d2a3d5e9ea71ac88e4c2057dbbfa3cf2999a9d64b9e6811b191a790dbca0`.
- Target file: 1,511 bytes;
  SHA-256 `59229a86dcccdcd337109be466dea66b2760772e7d61239b00c376237df9c4a2`.

## Structural QA

- 18 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 19 opening and 19 closing braces; 36 unescaped math-dollar delimiters.
- 2 `\\begin`/`\\end` pairs (`equation*`), with both footnotes preserved.
- Exact source command inventory, including `\\glsadd{not:i}`, both
  `\\myindex` and `\\myquote` hooks, `\\overset`, and all set/mathematical
  commands.
- No unmatched delimiters, mojibake, or changed notation.

## Terminology decisions

- `imaginary unit` → **satuan imajiner**; `Cartesian form` → **bentuk
  Kartesius**; `square root` → **akar kuadrat**; `solution` → **solusi**.
- `real number`/`complex number` → **bilangan real**/**bilangan kompleks**;
  `polynomial` → **polinom**.
- The engineer and head-whacking jokes remain explicit; the source's English
  `imaginary` is retained inside the quoted footnote solely to preserve its
  letter-joke, while all surrounding prose is Indonesian.

## Next cursor

The next contiguous R008 unit begins at source line **788** (`Given a complex
number $z=x+iy$ ...`), after the blank separator at line 787. Continue in a new
file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
