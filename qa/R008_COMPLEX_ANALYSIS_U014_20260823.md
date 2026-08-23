# R008 complex analysis — translation unit U014

Status: translated, bounded structural QA passed; not integrated into the R008
full driver and not published.

## Boundaries and identity

- Work: Jiří Lebl, *Guide to Cultivating Complex Analysis: Working the Complex Field*.
- Bound source: `source/ca-v1.9/ca.tex`, v1.9 commit
  `a4d25d9ba37a486a5a020219eb8bd4e6602fd14c`.
- Source unit: raw lines **974–985**, definition and topological meaning of a
  domain.
- Source slice (UTF-8 with LF): 613 bytes;
  SHA-256 `3956bc4c862df48a2d9e64a255f7ea0f69657d5c6a6fe1246cdb5a6d569fa4b6`.
- Target: `translation/complex-analysis/ca-domain-definition-id.tex`.
- Target translated payload: lines **7–18** (provenance header/comments are
  lines 1–6); 638 bytes UTF-8 with LF;
  SHA-256 `cf739c368a94eced317e1fa57cef1439a2912fb182cf5bf855917a9b9b9215c1`.
- Target file: 1,024 bytes;
  SHA-256 `d15a4e2bfc0dd163b3429c90bd1a5d81bfaaffb61b060ec405b6dbc69ac35e49`.

## Structural QA

- 4 ordered math-mode segments; all mathematical payloads match the source
  after whitespace normalization.
- 9 opening and 9 closing braces; 8 unescaped math-dollar delimiters.
- 1 `\\begin`/`\\end` pair (`defn`); exact `\\subset`, `\\colon`, `\\to`,
  index/quote, and both footnote structures preserved.
- No unmatched delimiters, mojibake, or changed definition structure.

## Terminology decisions

- `open and connected` → **terbuka dan terhubung**; `domain` remains **domain**
  (standard Indonesian topology/complex-analysis usage).
- `vacuous` → **benar secara hampa**, retaining the logical qualification for
  empty sets.

## Next cursor

The next contiguous R008 unit begins at source line **987**:
`\\subsection{Complex-valued functions}` (lines 986 is blank). Continue in a
new file under `translation/complex-analysis/`.

Translation provenance: **OpenAI Codex gpt-5.6-sol, Ultra**, acting on the
user's request. No author contact or publication was performed.
