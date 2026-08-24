# R006 Volume II reader U333 — build and visual-QA receipt

Status: **PASS / reader checkpoint accepted**  
Date: 2026-08-24  
Coverage: admitted Indonesian text through Section 11.4.1, *Eksponensial
kompleks*, ending after target/source raw line 1862. The next subsection,
*Fungsi trigonometri dan pi*, and all later material are explicitly excluded.

## Bound input and deterministic cutoff

- Live target: `translation/ra/ch-approximate.tex`, 5,472 lines, 184,745
  bytes, SHA-256
  `ea35f4bbbc3bb4a00b780339e59b45b57eca2a539da93ccc386f010c5c99cbfa`.
- Admitted target prefix, lines 1–1862 joined with LF and one terminal LF:
  66,475 bytes, SHA-256
  `c44b27e4a29305d492c66e2c22a21a45346b40a070c197a3f113a6c71149439f`.
- Frozen upstream source: `source/ra-v6.3/ch-approximate.tex`, 5,473
  lines, 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Corresponding source prefix through line 1862: 61,690 bytes, SHA-256
  `509d688b97d7fb59128cc81c4df7dec4f96297964bb6db4d9aea7ffa9f1ef2a1`.
- The cutoff assertion requires line 1863 to equal
  `\subsection{Trigonometric functions and $\pi$}`. It writes the admitted
  prefix plus one non-reader-facing deterministic cutoff comment to
  `ch-approximate.partial-v2.tex`, 66,543 bytes, SHA-256
  `468729fb18049785586a0638872cd049ffc61762de4149013685c354cb4daaf0`.
- Build script: `build_u333.ps1`, 2,189 bytes, SHA-256
  `1364cdc758972d69e93d04c7a6eb3a7f4fb0d0b9fd8252aad5631af13b93cebc`.

## Build convergence and generated structures

The source-to-PreTeXt converter exited 0 and ended with `Done! (number of
errors 0)`. The generated `realanal-out.xml` is 1,569,388 bytes, SHA-256
`42ae98de80a83883bf73ceb5128c43b2aa395b52b99243d911903028aaaba385`.
Its root is `pretext`, its language is `id-ID`, all 638 XML identifiers are
unique, and 908 reference attributes resolve except the two intentional
beyond-cutoff references `sec_arzelaascoli` and `sec_stoneweier`.

Five halted-on-error pdfLaTeX passes completed. Passes 4 and 5 have identical
33,708-byte console output, SHA-256
`f7b02949b996b9684c9528075918eb4c8e9e0e4a5e3d3419521e121364fc3f75`.
The final log is 98,996 bytes, SHA-256
`00aa5f5dbd4d99921a16d32e7d27652d84f82539a8169b5051067bb61a9c21ad`.
There are no undefined references, rerun requests, missing glyphs, duplicate
destinations, fatal errors, or package errors.

The index accepted 201 entries and rejected none. Its 265-line output is 8,856
bytes, SHA-256
`60452e0a641371f17d5b92bc82d9917ea50d2ff2b9871fac11b1dc6c02fab63d`.
The glossary accepted 52 entries and rejected none. Its 104-line output is
5,557 bytes, SHA-256
`f16737afa3ceca474ac0d5b532f07cc6883e56ad34d0db394794f55a965a255e`.
An extra freshness run left both hashes unchanged.

The final log retains eight known nonblocking warnings: one missing Indonesian
glossaries language module, two `tracklang` notices for the same unsupported
dialect, three empty-target link suppressions, and two inherited `\qedhere`
placement cautions. The 14 inherited overfull boxes occur on 13 pages
(2, 11, 17, 20, 78, 82, 85, 94, 102, 105, 125, 168, and 170); the largest is
18.71684 pt. Every affected page was rendered and inspected, and none clips,
overlaps, escapes the paper, or reduces mathematical legibility.

## PDF structure, extraction, and privacy

The reader `realanal2.pdf` is 192 pages, 2,058,059 bytes, SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.
It is unencrypted PDF 1.5 on 612×792 pt letter pages, with zero AcroForm fields
and no JavaScript. It has 748 annotations: 556 links and 192 tiny package-made
`pbs@ARFix` reset widgets, one at the extreme corner of each page; the catalog
contains no `/AcroForm`, `/AA`, or JavaScript action. Its 29 outline
destinations are arranged beneath nine top-level destinations, and it has
1,040 named destinations. Metadata preserves the source author Jiří Lebl and
the Indonesian title.

All 80 font rows are embedded; 79 are subsetted. Twenty-six `pdffonts` rows
provide
explicit ToUnicode maps, while the remaining mathematical font rows do not.
The extracted text nevertheless contains zero U+FFFD replacement characters
and zero literal unresolved `??` markers. The extraction is 642,660 bytes,
SHA-256
`59833afad1da6d8f63e64c5d307589afbbffc04fcff0f75916a1cb4697d00c29`.
The exact provenance string `OpenAI Codex gpt-5.6-sol, Ultra` appears once.
No local filesystem path, token marker, English section heading, or obsolete
Figure 11.6 label survives in reader-facing text. The PDF is not tagged and
its mathematical fonts have incomplete ToUnicode coverage; these are recorded
nonblocking accessibility limitations rather than hidden completion claims.

## Visual inspection

Fresh 144-dpi renders cover every page from 170 through 192 and every page
named by an overfull box. These were inspected both in contact sheets and,
where density or a montage artifact could obscure detail, individually at
original render resolution.

- Pages 170–182 preserve the previously accepted end of Section 11.3 and its
  exercises without clipping or reflow regression.
- Page 183 begins Section 11.4 and Subsection 11.4.1. The heading hierarchy,
  formulas, proof, margins, and line spacing are centered and legible.
- Page 184 contains the complete two-panel Figure 11.7 and the closing power
  series at an arbitrary center. Both surfaces, their left/right meaning,
  caption bounds, bold real-axis slice, and final equation are readable and
  fully inside the live area.
- Pages 185–192 contain the intentional cutoff transition and back matter;
  sparse pages are structurally intentional, while the glossary, notation,
  and index remain centered and readable.
- The independently rendered overfull-page set shows no clipping, overlap,
  off-page material, or materially narrowed/uncentered text block.

## Stable reader and decision

The accepted binary was copied byte-for-byte to:

`output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.4.1_Eksponensial_Kompleks.pdf`

It remains 2,058,059 bytes with SHA-256
`6f1f38221af120d6459cdc217e789ca1f7a9d4f353f5720db00ff271ce637061`.
The U333 reader gate passes. Publication must retain truthful `partial` status,
333 admitted units (R006 268, R007 15, R008 50), separate source identities
and rights, and the existing GitHub/Zenodo lineages. No author was contacted.
