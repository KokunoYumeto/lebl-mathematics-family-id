# R006 Volume II power-series analytic reader U330 - 2026-08-24

## Completion and scope

Status: complete, visually verified, and promoted to the stable reader path.
This Indonesian checkpoint ends after the complete Subsection 11.3.4, `Deret
pangkat sebagai fungsi analitik`. It excludes the untranslated identity-theorem
opening and every later source line.

- Proved template:
  `qa/builds/ra-id-volume2-swapping-limits-section-reader-20260823`.
- Build directory:
  `qa/builds/ra-id-volume2-power-series-analytic-reader-u330-20260824`.
- Stable reader:
  `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.3.4_Deret_Pangkat_Analitik.pdf`.
- Reproducible build driver: `build_u330.ps1`, 2,166 bytes;
  `e332585b7796dbded0841a26fe0abf34bf61c46049a66d57bc1274a25097b2bd`.

## Exact semantic boundary

All hashes below are SHA-256.

- Live hybrid target `translation/ra/ch-approximate.tex`: 5,468 raw lines,
  183,610 bytes;
  `aa51a8032b1babc9a530e0b68ebdaa1087932d66bf60162f42b775576a5fdedb`.
- Reader prefix, target raw lines 1-1549 inclusive with its final LF: 54,865
  bytes; `da80a2fe3f1b7f48d500127c2ac714d700b1eddb5c68a22f0ce8c1a5525ee972`.
- Generated partial component, including only the deterministic cutoff comment:
  54,933 bytes;
  `f466efb755040b41da42989f3ff9a95321f528769ba8fcb540e2c8094ae77073`.
- Target raw line 1549 is `Dapatkah Anda melihat alasannya? (latihan)`.
  Raw line 1550 is blank. Raw line 1551 is the excluded
  `\subsection{Identity theorem for analytic functions}`.
- The partial has 175 environment starts and 175 matching ends, zero
  mismatches, an empty final stack, and 19 complete exercise environments.

## Credits, license, provenance, and localized figure

The driver preserves the title and author, original copyright, source URLs,
dual-license notice, acknowledgments, bibliography, and all human credits. The
derivative edition selects the CC BY-SA 4.0 route and identifies itself as an
independent, non-endorsed translation. The exact provenance string
`OpenAI Codex gpt-5.6-sol, Ultra` occurs once in extracted reader text.

The canonical Figure 11.6 assets were copied from `translation/ra/figures`
after their Indonesian label correction. Mathematical geometry and symbols are
unchanged; the reader now says `deret / konvergen` and `deret / tidak
konvergen`, not the former English labels.

- `figures/radiusconvcomplex.pdf_t`: 1,176 bytes;
  `7ee6864434d06a45723b8e9e496a26882f6e0cbb6916e6356f2d2bad61eb7f37`.
- `figures/radiusconvcomplex.fig`: 1,983 bytes;
  `3fe8c73357a4aef584b0f0e4d735885abc7c6f669a290712b8eee8c8ee815937`.
- Page 174 was freshly rendered after the canonical asset replacement and
  shows both Indonesian labels fully visible and centered around the diagram.

## Converter and reference gate

- Converter exit zero and final message `Done! (number of errors 0)`.
- Converter console: 1,375,406 bytes;
  `d307c572d011a4b23e7e02fabee0c96a6c13321dbf022cad1deed020c79fc0fe`.
  Its only environmental diagnostic is the inherited Windows Perl locale
  fallback; conversion succeeds deterministically.
- `realanal-out.xml`: 1,555,834 bytes;
  `8b1fca05ab242c7a68642b540a8cbc33fc0f689297e3d76c408fdd87fed4b1de`.
  The parsed root is `pretext`, locale is `id-ID`, all 635 IDs are unique, and
  there are 904 internal references. The only unresolved targets are exactly
  `sec_arzelaascoli` and `sec_stoneweier`, both intentional beyond-boundary
  targets whose printed numbers are frozen in the partial-reader driver.

## TeX, index, glossary, and warning gates

- Five `pdflatex` passes completed. Passes 4 and 5 are byte-identical: 33,604
  bytes;
  `af661277d1ac15f45531fa6092fd9d00b8b1a7b81b501a693e419d93164cb4fa`.
- Final log: 98,356 bytes;
  `29f91551bed2676f8b50f3e64a6caa2e22e8f92e09ee3e701181bc80670139aa`.
  It contains zero blocking LaTeX, undefined-reference, rerun, missing-glyph,
  duplicate-destination, or package-error diagnostics.
- Index: 199 accepted entries, zero rejected, 263 output lines, zero warnings.
  The final `.ind` hash is
  `f1a4be1e2cbc419de4f26d69d3c40b5ec3384f317aeb7e8b9d17c8eb78c8ca56`.
- Glossary: 51 accepted entries, zero rejected, 102 output lines, zero
  warnings. The final `.gls` hash is
  `f651a53c4366d0883fc472879899cbc189f0d051619d55d1bf9ee11e262f302b`.
- A freshness rerun left both `.ind` and `.gls` byte-identical.
- Fourteen bounded overfull boxes remain, maximum 18.71684 pt. Every affected
  physical page was rendered: 2, 11, 17, 20, 78, 82, 85, 94, 102, 105, 125,
  168, and 170. Page 17 contains two locations. All content remains inside the
  physical page.

## PDF, extraction, font, structure, and privacy gates

- Final reader: 188 unencrypted letter-size pages; 1,991,475 bytes;
  `28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.
- Metadata title is `Analisis Dasar II: Pengantar Analisis Real, Jilid II` and
  author is Jiří Lebl. All 188 pages are 612 x 792 pt with zero rotation.
- The reopened PDF has 737 annotations, 13 top-level outline entries, no
  AcroForm, and no JavaScript.
- All 78 font rows are embedded; 77 are subset; 26 expose ToUnicode maps.
- Extracted text: 626,525 bytes;
  `3cc3fad7c65ee4efc55892e9f0fcbf1fe8d44c949f93a5446f58e3c80f791938`.
  It contains zero U+FFFD, zero literal `??`, exact provenance once, no English
  Section 11.3 or identity-theorem heading, and no former English Figure 11.6
  labels. A page-bounded extraction of page 174 confirms `deret`, `konvergen`,
  and `tidak konvergen`.
- Extracted reader text contains no local user path or credential-marker
  residue.

## Rendered visual QA

The final, canonical-asset PDF was rendered at 144 dpi after the last rebuild.
All new tail pages 170-188 were inspected. The overfull-page set listed above
was also rendered; page 170 is covered by the tail set. This produced 19 tail
page PNGs, 12 additional overfull-page PNGs, five tail contact sheets, and
three overfull contact sheets.

The reader uses a centered, full-width, readable text block. Section 11.3 and
Subsections 11.3.1-11.3.4 have consistent hierarchy. Display mathematics,
proof endings, two-column back matter, index, notation tables, and figure
captions are legible. Figure 11.6 has the corrected Indonesian labels. There is
no clipping, overlap, edge collision, black box, broken glyph, cut line,
placeholder, or unreadable formula. Page 171 is a sparse but complete final
exercise page; pages 182 and 186 are intentional open-right continuation pages
with running heads, not missing content.

## Principal artifact identities

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.pdf` | 1,991,475 | `28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1` |
| `realanal2.extracted.txt` | 626,525 | `3cc3fad7c65ee4efc55892e9f0fcbf1fe8d44c949f93a5446f58e3c80f791938` |
| `realanal-out.xml` | 1,555,834 | `8b1fca05ab242c7a68642b540a8cbc33fc0f689297e3d76c408fdd87fed4b1de` |
| `realanal2.log` | 98,356 | `29f91551bed2676f8b50f3e64a6caa2e22e8f92e09ee3e701181bc80670139aa` |
| `realanal2.tex` | 20,878 | `cb243cafd3cb790afab91206235477a3e187733a85af494e40c097b9bdfcf66f` |
| `ch-approximate.partial-v2.tex` | 54,933 | `f466efb755040b41da42989f3ff9a95321f528769ba8fcb540e2c8094ae77073` |
| `frag-vol2-intro.tex` | 3,831 | `26c1a2869d7b5bf66b7877bfe26b768ef7903c0e120fa852cf729dc1e9bd2700` |

The stable output was reopened after copying and is byte-identical to the
build PDF: 188 pages, 1,991,475 bytes, SHA-256
`28c0844666712d94bed82789e014faf8dbbba32c2384b77cd745423c4f845aa1`.
No blocking defect remains at this boundary.
