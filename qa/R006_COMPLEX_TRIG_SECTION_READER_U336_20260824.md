# R006 U336 — section-complete Volume II reader

Status: **PASS and promoted**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Deterministic cutoff and conversion

Build directory:
`qa/builds/ra-id-volume2-complex-trigonometry-section-complete-reader-u336-20260824`.
The build script is 3,348 bytes, SHA-256
`24146b6ed63cf694156d7e0fcf0a2239125ba264b59eea0a59fb42448ed596cf`.
It binds the admitted target prefix through raw line 2271, verifies that raw
line 2272 is `\sectionnewpage` and that the next heading/label are the frozen
maximum-principle boundary, then writes the partial deterministically.

The bound prefix is 81,734 bytes, SHA-256
`30dcec5183dbb5f092d7be4c351509a3c5dc0e8f929748d6cc8f969f19331b57`.
The installed partial chapter is 81,802 bytes, SHA-256
`362969b9ce085c1e454cd3c8d7eeaa6ce2ab185c3fbc98a624c21f8c06814920`.
The converter exits zero with zero reported errors. Generated PreTeXt XML is
1,586,796 bytes, SHA-256
`edff7ae502ff34facbac60d2d55803a690b2d9b408e29709a3dcd41e1e9df618`.
Its `pretext` root has locale `id-ID`, 639 unique identifiers, no duplicate
identifier, and 909 xrefs. The new stable identifier
`exercise_cossinidentity` occurs once and its one incoming xref resolves. The
only missing XML targets are the two inherited beyond-cutoff sections
`sec_arzelaascoli` and `sec_stoneweier`.

## TeX and PDF verification

Five halted-on-error pdfLaTeX passes complete. Passes 3, 4, and 5 have the
same 33,744-byte console transcript with SHA-256
`cf958b4f96489d3e739ed7664367d1d2921e55045ab4c94e313cbfc156f1c025`.
There are no undefined references, rerun requests, fatal/package errors,
missing glyphs, or duplicate destinations. The index accepts 208 entries and
rejects none; the glossary accepts 55 and rejects none. Independent freshness
runs leave the index SHA-256
`c03ae7b2b6ce118f41880af04b9deb6720f3219e12fd38fbb4c81bb46c677bc8`
and glossary SHA-256
`87f3e1a6580fc479d543dc4f466c03860813b82c36f98e48dfebc121e8136aa9`
unchanged.

The promoted reader is 198 pages, 2,091,363 bytes, SHA-256
`78543d4e8087e68589e8f15d0a3a969b3282247c7c9c2cdcb6f658dfa4b68e4f`.
It is an unencrypted PDF 1.5 on 612 x 792 pt pages, with no form, catalog
additional actions, or JavaScript. Its sole open action is an ordinary `GoTo`
page-fit destination. Its 765 annotations comprise 567 links and 198 tiny
package-made widgets. It has 29 outline items, nine top-level outline
destinations, and 1,085 named destinations. All 80 fonts are embedded, 79 are
subsetted, and 26 expose ToUnicode maps. The file remains untagged and several
mathematical fonts retain incomplete ToUnicode, as in the inherited reader.

Layout-preserving extraction is 662,667 bytes, SHA-256
`98311009e4b392597a82d0e4bb34f159ed12585ae6ebec3bd6ff2a8ac59b7be7`.
It contains zero replacement characters, the exact provenance string once,
and zero literal `??` placeholders. Thus the forward-reference defect visible
in the U334 inspection build is resolved.

## Visual inspection and promotion

Fresh 144-dpi renders of physical pages 185–193 were inspected. Pages 188–189
contain the complete new unit-circle/polar-coordinate subsection and all eleven
exercises. Their text blocks are centered and fill the intended page width;
headings, formulas, labels, margins, line breaks, and page numbers are legible,
with no clipping, overlap, black boxes, or broken references. Pages 190 and 192
are intentional verso blanks; pages 191 and 193 begin the reading list and
index cleanly. No new overfull box occurs in the newly admitted pages.

The byte-identical promoted artifact is:
`output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4_Latihan.pdf`.
This is a coherent section-complete reader and supersedes the U333 Volume II
reader for the next public checkpoint. No author was contacted.
