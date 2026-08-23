# R006 Volume II Section 10.7 exercises checkpoint — 2026-08-23

## Scope and exact boundary

This checkpoint translates and admits the complete six-exercise block at the
end of Section 10.7, Change of variables. It completes the section and the
source file `ch-multivar-int.tex`.

- Unit: `ra.v2.change-of-variables.exercises`
- Source: raw lines 3946–4016 inclusive; 2,517 UTF-8 bytes; SHA-256
  `2d20c15321633882dad192def59d1e2837a610c2e4c51041aad26a96c92db94a`
- Target: raw lines 3960–4031 inclusive; 2,811 UTF-8 bytes; SHA-256
  `03d28786a637f0dbe6624cccd0020fa3f327755ef6783334079b5cccf4eb0710`
- Complete live target: 148,566 bytes; SHA-256
  `65c8bdb840c9ac573b94b9cc9f971c63fe40d1f07b0ac1f2d595a85b9ca07dd2`
- Next source component in the Volume II driver: `ch-approximate.tex`.

## Translation, mathematics, and topology QA

- The source and target each contain exactly six exercise environments, three
  labels, one proposition reference, one `pagebreak[2]`, 40 inline-math spans,
  and three `equation*` displays.
- All 40 inline payloads, all three display payloads, and all 23 structural
  tokens are byte-identical and identically ordered. No English reader prose
  remains inside the admitted target slice.
- Independent review approved the natural formal Indonesian wording and the
  established terms `terukur Jordan`, `persegi panjang tertutup`,
  `subpersegi panjang`, `pemetaan`, `injektif`, `diferensiabel secara kontinu`,
  `tumpuan`, `bertumpuan kompak`, and `gabungan menaik`.
- Exercise 10.7.5 contains a high-confidence source defect: the source equates
  being outside `U` with nondifferentiability of a globally defined map. The
  localized text preserves every formula but states the intended zero
  extension outside the relevant neighborhood. This bounded correction is
  recorded as `LEBL-ID-ADV-0221`.
- Exercise 10.7.6 is false under the chapter's ordinary bounded-function
  definition of Riemann integration. The counterexample `n=1`, `S=(0,1)`,
  `g(x)=sqrt(x)`, `f=1` satisfies the printed hypotheses while the pulled-back
  integrand is unbounded. Because a correct repair requires either stronger
  hypotheses or an explicit improper/exhaustion interpretation, the source
  exercise is preserved rather than silently rewritten; the issue is recorded
  as `LEBL-ID-ADV-0222` for edition metadata and the one final deduplicated
  upstream disposition. No author or maintainer was contacted.

## Terminology evidence and provenance

The one-time field-usage QA remains current. arXiv:2008.00182 was downloaded
with its TeX source and rejected as terminology evidence because the TeX is in
English. The inspected Indonesian fallback sources remain Universitas Terbuka
MATA4217 *Analisis I* and the UAD Press book *Dasar-dasar Matematika Diskrit
dan Graf*. The corrected terminology report is 7,495 bytes with SHA-256
`8c0d8a44e1391cda486cb491053d07a564c23239483a42511c6099c0c8f8c3ee`;
no new glossary change was warranted by this exercise unit.

The reader driver retains the exact provenance identification `OpenAI Codex
gpt-5.6-sol, Ultra` once, with generic user-instruction attribution. Jiří Lebl
remains the source author, and the original copyright, source URLs, dual-license
notice, bibliography, acknowledgments, and human credits remain intact.

## Converter and build gates

- Direct `perl convert-to-mbx.pl` exited zero and ended with
  `Done! (number of errors 0)`. `realanal-out.xml` is 1,698,586 bytes, SHA-256
  `04f48cb0a07ccca6c5887df79093d5bf8b9179975394c811ff8e666e6262e09d`,
  parses as `pretext` with locale `id-ID`, and contains 672 unique IDs and 952
  references with zero duplicate or unresolved IDs.
- Index generation accepted 253 entries and glossary generation accepted 59;
  both rejected zero entries and emitted zero warnings.
- Five TeX passes completed. Passes 4 and 5 are byte-identical 32,356-byte
  logs with SHA-256
  `a03bba473e8b362cd2a4b8668ecda6735daeec1083016670644ec1fcd8b87646`.
  The final log contains no LaTeX error, undefined control sequence or
  reference, rerun warning, or missing character. The 12 inherited bounded
  overfull boxes remain unchanged; the maximum is 18.71684 pt.
- Full-tail QA PDF: 235 letter-size pages, unencrypted, 2,410,331 bytes,
  SHA-256
  `35e41821d12fbcca964d6000e58acaa3d178f6ced5b0a0d533402bedce742adf`.
  All 98 font rows are embedded; 27 have ToUnicode. Extraction is 812,925
  bytes with zero U+FFFD and contains the exact model provenance once.
- Physical pages 154–157 were rendered from the final PDF at 144 dpi and
  inspected. Page 154 closes the localized theorem proof; page 155 contains
  all six exercises with centered, full-width, readable layout and no clipping,
  overlap, broken glyph, or margin defect. Page 156 is the expected blank
  chapter transition, and untranslated Chapter 11 begins on page 157, strictly
  outside this checkpoint. A public U228 reader must use a source-level cutoff
  immediately after the final exercise rather than PDF-page truncation.

## Principal artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 148,566 | `65c8bdb840c9ac573b94b9cc9f971c63fe40d1f07b0ac1f2d595a85b9ca07dd2` |
| `converter.console.log` | 1,506,314 | `8391e9bbc49a8181c3b75b64badda60d552b84be2b56e7f3dce651c852183d37` |
| `converter.stderr.log` | 393 | `57183f2646e20faf44dfd55c212cfffb98328b1d5d3de478116a3bede3a033be` |
| `realanal-out.xml` | 1,698,586 | `04f48cb0a07ccca6c5887df79093d5bf8b9179975394c811ff8e666e6262e09d` |
| `realanal2.log` | 101,721 | `2fccc7cb217fd6d513d23f18acd489df0cef695cb74ef7b374c59a8319a1944d` |
| `realanal2.pdf` | 2,410,331 | `35e41821d12fbcca964d6000e58acaa3d178f6ced5b0a0d533402bedce742adf` |
| `realanal2.extracted.txt` | 812,925 | `0cd09e4f24efaff29932399aa535548e9963e84269411363b1324e3b710ca822` |
| `render-exercises/page-155.png` | 309,987 | `7b32d7cc17c7ee0215cb2f063f0ce5c2d1e564d2c39663a8f6cb29abdb176529` |

