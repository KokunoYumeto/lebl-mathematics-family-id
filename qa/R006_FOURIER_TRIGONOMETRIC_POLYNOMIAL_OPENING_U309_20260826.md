# R006 Fourier-series opening and trigonometric-polynomial representation — U309

Status: **PASS; translated and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.fourier-series.trigonometric-polynomials.opening-and-laurent-representation`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4201–4241 inclusive; 41 LF-terminated lines, 1,344 bytes, SHA-256 `1d188bf1dd6f3e299de9164d4cca96f443976f17e3972f294e288c3a2f0a7cfb`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4209–4249 inclusive; 41 LF-terminated lines, 1,383 bytes, SHA-256 `4225dffa12bc0d4cf29064c48b3988cf172916ed6e5d42f2321952f963f1cc11`.
- Full target after U309: 194,278 bytes, 5,481 LF lines, SHA-256 `213a40cf14411ee1e7bc59d00a17ca17eed00b97e3ca08428d5aa75ab8a71a35`.

## Mathematical and structural QA

- Ordered TeX command stream: 31 source / 31 target, byte-identical by command name.
- Ordered environments: six exact events forming three balanced `equation*` displays.
- Ordered inline-math payloads: 5 source / 5 target, byte-identical.
- Ordered display payloads: 3 source / 3 target, byte-identical after whitespace normalization.
- Exact topology retained: `\sectionnewpage`, one section, one subsection, `%mbxINTROSUBSECTION`, and `\sectionnotes`.
- Label `sec:fourier`, the Fourier biography URL and visible name, one footnote with line-continuation control, and one index entry are preserved.
- Braces are balanced at 24 opening / 24 closing on both sides; target dollar delimiters are balanced at 10/10.
- The sine/cosine and finite complex-exponential forms remain equivalent via Euler's formula. On `|z|=1`, substitution `z=e^{ix}` gives the exact finite Laurent polynomial displayed by the source. Calling it a rational function evaluated on the unit circle is correct; no coefficient-field qualification or domain correction was added.
- There are no figures, other assets, internal cross-references, exercises, hints, answers, or solutions in this unit.

## Indonesian QA and terminology

Two independent read-only audits passed without correction. The translation is natural formal `id-ID` and preserves the source's emphasis and deliberate decision not to pursue the Laurent-series connection further. There is no reader-facing English prose residue; only proper names and the preserved URL remain.

The terminology ledger adds:

- `LEBL-TERM-0761`: `Fourier series` → `deret Fourier`;
- `LEBL-TERM-0762`: `trigonometric polynomial` → `polinom trigonometri`;
- `LEBL-TERM-0763`: `Laurent series` → `deret Laurent`.

The 763-row CSV parses with all 11 columns, unique term IDs, no blank concept IDs, 116,764 bytes, and SHA-256 `b2cbe138d4a8787cba1bac5248630999c321bb22d9b4e8938563c9e555e77633`.

## Correction and cursor

No source correction or O001 solution-gap entry is required. The next source boundary is raw line 4243 and the next target boundary is raw line 4251, beginning with `\medskip` before the eigenfunction motivation paragraph.

