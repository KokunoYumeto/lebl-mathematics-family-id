# R006 Volume II swapping-limits section reader - 2026-08-23/24

## Completion and scope

Status: complete and promoted. The Indonesian reader ends at target raw line
1030, after all ten exercises in Subsection 11.2.4 and the complete Section
11.2, `Pertukaran limit`. It excludes the page break and still-English Section
11.3 beginning at target raw lines 1034-1035.

- Template: proved closure
  `qa/builds/ra-id-volume2-continuity-reader-20260823`.
- Build directory:
  `qa/builds/ra-id-volume2-swapping-limits-section-reader-20260823`.
- Stable reader:
  `output/pdf/Analisis_Dasar_II_Bahasa_Indonesia_v6.3_WIP_sampai_11.2_Latihan.pdf`.
- A final visual audit found five English course-path list residues on physical
  page 5. They were corrected in the live source, installed in both build
  trees, recorded in the translation manifest, and followed by fresh converter
  and five-pass PDF builds. This receipt describes only the corrected build.

## Exact semantic boundary and source correction

All hashes below are SHA-256.

- Current live hybrid target component: 182,186 bytes;
  `b06e83c2a6508e059bea6e21bd41fed65b5c75545f7221da12090e59b7713e61`.
- Newly admitted upstream unit, source raw lines 726-1035 inclusive: 9,038
  bytes; `7731e53793c3be13e11c184781ffa6da2b20768c91e9e538344ba3c27f5c7ee1`.
- Newly admitted Indonesian unit, target raw lines 721-1030 inclusive: 9,596
  bytes; `9131c940199521fae5840ba2fb0ea648ba2d83b0c7e9a68c09dc1a9a93bfe3a9`.
- Raw target prefix, lines 1-1030 without helper trailer: 35,712 bytes;
  `c530f9fca2303b5655ae32c57b56eb6157e0a60581a644a1c0e9d4b48ee9b227`.
- Generated and installed partial component: 35,780 bytes;
  `63edb3e4c91c3f015f84d641fbf67947f0434b870930d42c4700ce67d4c4b7a4`.
- Corrected `frag-vol2-intro.tex`: 3,831 bytes;
  `26c1a2869d7b5bf66b7877bfe26b768ef7903c0e120fa852cf729dc1e9bd2700`.
  The five course-path items now use `Bab`, `dan`, and `mungkin`; labels and
  references are unchanged.
- Corrected `translation/TRANSLATION_MANIFEST.jsonl`: 319 valid rows, zero
  duplicate semantic IDs, 452,035 bytes;
  `0718642d139d80c505605d6cd47d5f836ba15dd0bde7a7f02e344922fee4d703`.
- Target line 1030 is `\end{exercise}`. The prefix has 19 exercise begins and
  19 exercise ends, an empty non-comment environment stack, and zero
  environment mismatches. Section 11.2 contains ten complete exercises.
- The untranslated tail from target raw line 1031 is byte-identical to pinned
  upstream source raw line 1036 onward: 146,474 bytes;
  `cdc1dc70e380127fabc59d16c451ebf2ad74837672f4f8a81c78ae63130d65da`.
- Next source cursor: raw line 1040, `Power series and analytic functions`.
  Next target insertion point: raw line 1035.

## Credits, license, and provenance

The driver preserves the title and author, original copyright, source URLs,
dual-license notice, acknowledgments, bibliography, and human credits. The
derivative edition selects the CC BY-SA 4.0 route and states that it is
independent and not endorsed by the source author or publisher. The exact
provenance string `OpenAI Codex gpt-5.6-sol, Ultra` occurs once in extracted
reader text.

## Full-tail integration gate

`full-tail-integration` used the complete current 182,186-byte hybrid
component. It is QA evidence, not a reader artifact.

- Converter exit zero; final message `Done! (number of errors 0)`.
- Converter console: 1,508,928 bytes;
  `bae6f2231d02676e8fd2d46b49b0dedc1078e310d2a35f087462d98f30e4c6b0`.
- `realanal-out.xml`: 1,700,862 bytes;
  `ace90cd2a1099f2f2a43a22e6011dd5d79a4c61d73d992dd295b463dddb73ac0`;
  root `pretext`, locale `id-ID`, 672 IDs all unique, 952 internal references,
  and zero unresolved internal targets.
- Five TeX passes completed. Passes 4 and 5 are byte-identical: 33,972 bytes;
  `5ec60bcb450d872e6df1cc01859657953db73796dd403965f0cd152f72b6b540`.
- Final log: 102,526 bytes;
  `2e1c94b58ee973e55b3bb8bc912a5745a6d022f0d71891fbdfef1b66fb158720`;
  zero blocking LaTeX, reference, rerun, or glyph diagnostics.
- Full-tail PDF: 235 letter-size, unencrypted pages; 2,410,056 bytes;
  `5a4f1fa64bbafc206001d482b6bc0e4d6ef893b11c334d5aff477e8dc739802c`.
- All 98 font rows are embedded.
- Extracted text: 814,819 bytes;
  `8d320331aa0f52c2328a3d33433bb6e5c675b50eff03775b002796c445d92f7e`;
  zero U+FFFD, zero literal `??`, exact provenance once, and no course-path
  `Chapter`/`Chapters`/`chapter`/`maybe` residue.

The final full-tail auxiliary file proves
`exercise:CXCnormedspace = 11.2.3`, `sec:arzelaascoli = 11.6`, and
`sec:stoneweier = 11.7`. The partial reader therefore freezes only the two
genuinely beyond-boundary sections.

## Partial-reader converter and reference gate

- Converter exit zero; final message `Done! (number of errors 0)`.
- Converter console: 1,356,278 bytes;
  `eb986fc36752e564c9d10a8243e7a7c48af775b83df2331f33032b6cbc8143a9`.
- `realanal-out.xml`: 1,534,972 bytes;
  `dacdd2045bd20dd700ad8b677fd297dc437f9465cb741238ea86cca6b2d1d426`;
  root `pretext`, locale `id-ID`, 627 IDs all unique, and 893 internal
  references. The only two unresolved internal targets are exactly
  `sec_arzelaascoli` and `sec_stoneweier`, both intentional beyond-boundary
  targets. `exercise_CXCnormedspace` resolves normally.

## PDF, extraction, font, index, and warning gates

- Five TeX passes completed. Passes 4 and 5 are byte-identical: 33,392 bytes;
  `d5f7725f22376a71a52c4e00081198eb98d134c548bd8edc41cd48b2d03f25f5`.
- Final log: 97,272 bytes;
  `8128fc6f3f6882d1ab349cd5f9467bde11a5dbc2ed1c7c934f7de71fb75d79f8`;
  zero blocking LaTeX, reference, rerun, or glyph diagnostics.
- Index: 193 accepted entries, zero rejected, 256 output lines, zero warnings.
  Glossary: 51 accepted entries, zero rejected, 102 output lines, zero
  warnings. A freshness rerun left `.ind` and `.gls` byte-identical.
- Final reader: 180 letter-size, unencrypted pages; 1,909,146 bytes;
  `303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`.
- All 76 font rows are embedded; 75 are subset; 26 expose ToUnicode.
- Extracted text: 594,005 bytes;
  `fed5e5bd0cb0621b5788221bb6fe4f8346a924f7b27b22eaeb268a906fd8c134`.
  It contains zero U+FFFD, zero literal `??`, exact provenance once, all ten
  `Latihan 11.2.x` headings, no Section 11.3 heading, and no course-path
  `Chapter`/`Chapters`/`chapter`/`maybe` residue. The sole English `and` is
  inside the preserved bibliography series title `Pure and Applied
  Mathematics`, not translated prose.
- Fourteen bounded overfull boxes remain, maximum 18.71684 pt. Every location
  was rendered and checked; all content remains inside the physical page.

## Rendered visual QA

The corrected PDF was rendered at 144 dpi. Pages 1-6 and 167-180 were freshly
inspected after the front-matter correction; inherited overfull locations had
already been inspected on pages 11, 17, 20, 78, 82, 85, 94, 102, 105, and 125.
The reader uses a centered, full-width readable text block. Display mathematics,
figures, references, index, and notation pages are legible. There is no
clipping, overlap, edge collision, broken glyph, black box, cut line,
placeholder, or unreadable formula. Pages 172, 174, and 178 are intentional
open-right transition pages with running heads; page 171 is a sparse but
complete final exercise page.

## Principal artifact identities

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.pdf` | 1,909,146 | `303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725` |
| `realanal2.extracted.txt` | 594,005 | `fed5e5bd0cb0621b5788221bb6fe4f8346a924f7b27b22eaeb268a906fd8c134` |
| `realanal-out.xml` | 1,534,972 | `dacdd2045bd20dd700ad8b677fd297dc437f9465cb741238ea86cca6b2d1d426` |
| `realanal2.log` | 97,272 | `8128fc6f3f6882d1ab349cd5f9467bde11a5dbc2ed1c7c934f7de71fb75d79f8` |
| `realanal2.tex` | 20,878 | `cb243cafd3cb790afab91206235477a3e187733a85af494e40c097b9bdfcf66f` |
| `ch-approximate.partial-v2.tex` | 35,780 | `63edb3e4c91c3f015f84d641fbf67947f0434b870930d42c4700ce67d4c4b7a4` |
| `frag-vol2-intro.tex` | 3,831 | `26c1a2869d7b5bf66b7877bfe26b768ef7903c0e120fa852cf729dc1e9bd2700` |

The stable output was reopened after copying and is byte-identical to
`realanal2.pdf`: 180 pages, 1,909,146 bytes, SHA-256
`303ec82e16d133e938247f6611e31e36cb435ff0285a7b33fbbf4f8a5eb91725`.
No blocking defect remains at this boundary.
