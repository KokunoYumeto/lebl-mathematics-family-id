# R006 U361 — Section 11.5 reader build and visual QA

Status: **PASS; promoted reader checkpoint**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact reader boundary

- Reader: `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.5_Latihan.pdf`
- Coverage: complete admitted R006 Volume II text through Section 11.5,
  *Prinsip maksimum dan teorema dasar aljabar*, including all seven exercises.
- The cutoff is before target raw line 2552, `\sectionnewpage`, and therefore
  exposes no untranslated Arzelà–Ascoli text.
- Final PDF: 200 letter-size pages, 2,112,324 bytes, SHA-256
  `3e03748a32b19a7fabc38be7dbc9f1c8bc845eb99f5896dd5d93877176ceab72`.
- Deterministic partial chapter: 92,306 bytes, SHA-256
  `ec1579da1191ec1d9a083fe16642fafd081b33af5aa5e797e04c36d0d006223a`.
- Its admitted live prefix through target raw line 2551 is 92,210 bytes,
  SHA-256
  `36009a672867a5fd811217696e546e3d1daaf61a58953f4a7a4efd9c8cdcfd69`.

## Deterministic build

`qa/builds/ra-id-volume2-maximum-principle-section-complete-reader-u361-20260824/build_u361.ps1`
(3,699 bytes, SHA-256
`5548f95153514563f7d19a75d50c9de084ff0b0a9c5fd6583fa3ed91b86c25ef`)
hash-pins the 5,483-line live chapter, the semantic cutoff, and the installed
partial. It performs the converter followed by five `pdflatex` passes and four
`makeindex`/`makeglossaries` passes. The retained Volume I auxiliary witness is
359,397 bytes, SHA-256
`f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda`.

The converter finishes with `number of errors 0`. Its console is 1,413,583
bytes, SHA-256
`3184787ddcaea8333f055e880908c41955426c23da768444106aa83d8b017a94`.
The final TeX pass has zero LaTeX errors, zero undefined references or
citations, and zero rerun warnings; its console is 33,831 bytes, SHA-256
`a1b6f30a86f1ee3c7a708fc2e2df1d3aa86e54c6e5fb65d86d6f7ac1d1523e5b`.
All 80 fonts are embedded. Text extraction contains zero literal `??`
placeholders and no reader-facing English in physical pages 190–192.

The fourteen overfull horizontal-box diagnostics are byte-position-equivalent
to the already inspected U336 reader. One 3.85408-point vertical-box diagnostic
occurs at the expanded index boundary; visual inspection confirms no clipping,
collision, or missing entry.

## Visual inspection

Fresh 120-dpi renders cover physical pages 184–200, plus the title and rights
pages. The complete contact sheet and full-size inspection of pages 190–193,
197, and 200 verify the new section opening, both proofs, all exercises and
hints, bibliography transition, index, and notation table. Page blocks fill the
usable measure consistently; headings, margins, page numbers, hyperlinks,
formulas, and rule boxes remain aligned. No clipped text, overlap, black square,
unreadable glyph, or off-center content was found.

## Decision

Promote this 200-page PDF as the current R006 Volume II reader. The previous
Section 11.4 checkpoint remains a preserved historical artifact. Continue
translation at source raw line 2542 / target raw line 2552, the Arzelà–Ascoli
section. No author was contacted.
