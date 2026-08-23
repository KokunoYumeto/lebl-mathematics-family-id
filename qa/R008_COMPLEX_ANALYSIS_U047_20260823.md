# R008 complex analysis — translation unit U047

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **1414–1452**, completing the exponential mapping
  subsection through its figure and closing separator.
- Source slice (UTF-8 with LF): 1,449 bytes;
  SHA-256 `726e78aa3ec80c75aaba119bbddc73157da16f17a70122ee8156584286cbe3a5`.
- Target: `translation/complex-analysis/ca-exponential-lines-strips-id.tex`.
- Target translated payload: lines **7–45** (provenance header/comments are
  lines 1–6); 1,533 bytes UTF-8 with LF;
  SHA-256 `e3f8bd5a48431b9d6bda8e385bd61acb32ab99138865f25ca8c934fe719115ed`.
- Target file: 1,931 bytes;
  SHA-256 `cf9c27cb0cfc73e1ed69aec4e1d5801748426bab3100c0f1b3ed703043b86acf`.

## Structural QA

- Eighteen ordered math parts (inline expressions plus three displayed
  equations) match the source after whitespace normalization: **18/18**.
- 20 opening and 20 closing braces; 30 unescaped math-dollar delimiters.
- Four `\\begin`/`\\end` pairs (three `equation*`, one `myfig`); exact
  `\\sabs`, `\\figureref`, `\\bigl`, `\\bigr`, `\\in`, `\\C`,
  `\\theta`, `\\arg`, `\\pi`, `\\Im`, `\\leq`, `\\exerciseref`,
  `\\setminus`, `\\includegraphics`, `\\caption`, and `\\label`
  inventories match the source.
- Figure asset `figures/expplotlines`, both `fig:expplotlines` references,
  label `fig:expplotlines`, and exercise reference
  `exercise:exponetoonestrip` are preserved exactly.
- The complete reader-facing figure caption is translated; the 78-character
  subsection separator comment is byte-for-byte identical. No mojibake markers
  or unintended reader-facing English residue were found.

## Terminology decisions

- `vertical/horizontal line` → **garis vertikal/horizontal**.
- `strip` → **pita**; `annulus` → **anulus**; `sector` → **sektor**.
- `ray from the origin` → **sinar dari titik asal**.
- `one-to-one fashion` → **secara satu-ke-satu**.

## Next cursor

The next contiguous R008 unit begins at source line **1454**
(`\\section{The Riemann sphere}`). Continue in a new file under
`translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
