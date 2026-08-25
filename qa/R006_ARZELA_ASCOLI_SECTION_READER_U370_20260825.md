# R006 U370 — Section 11.6 reader build and visual QA

Status: **PASS; promoted reader checkpoint**  
Date: 2026-08-25  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact reader boundary

- Reader:
  `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.6_Latihan.pdf`.
- Coverage: complete admitted R006 Volume II text through Section 11.6,
  *Ekuikontinuitas dan teorema Arzelà--Ascoli*, including all eleven exercises.
- The cutoff is before target raw line 3148, `\sectionnewpage`, and therefore
  exposes no untranslated Stone--Weierstrass text.
- Final PDF: 208 letter-size pages, 2,161,063 bytes, SHA-256
  `00fde02788a34292a44f38fed3146df2dbb4db8d942672e59fd54c9e362b51b7`.
- Deterministic partial chapter: 115,926 bytes, SHA-256
  `0e492bdf9f4116d967b43ecb15fa0ba3db501c45defdb7f244a5d3b823a62ce6`.
- Its admitted live prefix through target raw line 3147 is 115,853 bytes,
  SHA-256
  `3a54147196f64d34694aa7d240ef7d445a2c1fef3aa593569ba82c91fd3fcfee`.

## Deterministic build

`qa/builds/ra-id-volume2-arzela-ascoli-section-complete-reader-u370-20260825/build_u370.ps1`
(4,349 bytes, SHA-256
`da557125530dad4b83b0496d58d2253d3d386c1a03f3d4669b4efe815043d7bf`)
hash-pins the 5,485-line live chapter, semantic cutoff, and installed partial.
It performs the converter, four index/glossary passes, and nine TeX passes.

The converter finishes with `number of errors 0`; its console is 1,437,249
bytes, SHA-256
`7e909c16e0c5c03765a815fb9042295e3cb27b38fb28f5ebb603bf01646e0508`.
The final TeX pass has zero LaTeX errors, zero undefined references or
citations, and zero undefined control sequences. Its console is 34,265 bytes,
SHA-256
`bcae9b7aaa6fc76c8dca510903cd74a617801f64c895a27cd5be75abae7aea7e`.

The document class emits a persistent generic `Label(s) may have changed`
warning. This is a false-positive convergence signal here: all seven material
auxiliary products (`aux`, `toc`, `out`, `idx`, `glo`, `ind`, and `gls`) are
byte-identical across passes 8 and 9. There are no missing destinations: all
585 internal links and 31 outline destinations resolve, alongside 19 external
links and 1,141 named destinations. Strict PDF parsing opens all 208 pages.

All 80 font entries are embedded. Text extraction from physical pages 193–200
contains zero literal `??` placeholders and zero hits for the audited English
source phrases. The fifteen horizontal overfull diagnostics consist of the
fourteen already visually accepted legacy locations plus one 9.64963-point
line in the Section 11.6 proof; the four underfull diagnostics are non-clipping
page/glossary spacing. Full-size visual review confirms that none crosses the
printable page boundary or impairs reading.

## Visual inspection

Fresh 150-dpi renders cover physical pages 1–2 and 190–208. The 21 final-pass
PNGs are pixel-identical to the initially inspected set; their canonical
inventory is 2,414 bytes with SHA-256
`108028e32a424bdc92dfb57beaef12b0611bae689a4a48d881772c4a7d850158`.
Contact sheets plus full-size inspection of pages 193, 195, 197, 199, 200,
201, 203, and 208 verify the complete section, theorem/proof, corollaries,
applications, all exercises, bibliography transition, index, and notation
table. Text blocks fill the usable measure and are centered consistently.
There is no clipping, overlap, broken glyph, black square, off-center content,
or unreadable formula. Page 200 is intentionally sparse because it contains
only the end of the final exercise at the clean section cutoff.

## Decision

Promote this 208-page PDF as the current R006 Volume II reader. Preserve the
Section 11.5 checkpoint as a historical artifact. Publish U370 to the existing
GitHub and Zenodo lineages, verify public bytes anonymously, then continue at
source raw line 3137 / target raw line 3149 with Section 11.7. No author was
contacted.
