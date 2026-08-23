# R008 complex analysis — translation unit U005

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **788–835**, complex conjugation, real/imaginary
  components, and equivalent expressions in $z,\bar z$ versus $x,y$.
- Source slice (UTF-8 with LF): 1,456 bytes;
  SHA-256 `e7806e77ec918c9916678389b5e2f491fb925cae42fd56cebfdb06a2183be021`.
- Target: `translation/complex-analysis/ca-conjugate-components-id.tex`.
- Target translated payload: lines **7–55** (provenance header/comments are
  lines 1–6); 1,480 bytes UTF-8 with LF;
  SHA-256 `019fc1b86373279a288253f674fdd26a1711b92c6cdca06c6c52846ab21e62d1`.
- Target file: 1,866 bytes;
  SHA-256 `18841a2af38e2a5207f14b916cf4376300695d653074819f03fe61f41d591fd4`.

## Structural QA

- 19 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 55 opening and 55 closing braces; 38 unescaped math-dollar delimiters.
- 4 `\\begin`/`\\end` pairs (`equation*` × 4).
- Exact source command inventory: `\\bar` 15, `\\frac` 6, `\\left`/`\\right`
  4 each, `\\Re` 2, `\\Im` 2, `\\glsadd` 3, `\\myindex` 3,
  `\\myquote` 2, and all remaining commands unchanged.
- No unmatched delimiters, mojibake, or changed notation/glossary hooks.

## Terminology decisions

- `complex conjugate` → **konjugat kompleks**; `real part` → **bagian real**;
  `imaginary part` → **bagian imajiner**.
- `independent variables` → **variabel-variabel yang independen**; the source's
  playful `evil twin` is retained as **kembaran jahat**.
- All equation content and source notation remain byte-auditable modulo the
  intentionally translated prose and whitespace.

## Next cursor

The next contiguous R008 unit begins at source line **837**:
`\\subsection{The geometry and topology of the plane}` (line 836 is blank).
Continue in a new file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
