# R006 Volume II public WIP reader receipt — Unit 219 — 2026-08-23

## Claim and exact boundary

This receipt proves the privacy-safe public work-in-progress reader for
*Analisis Dasar II*. It is not the complete Volume II. The reader contains the
contiguous Indonesian translation through the end of Section 10.6, Green's
theorem, including the vortex-field application, harmonic mean-value example,
and all seven exercises. It ends on physical page 150. Section 10.7, change of
variables, is not presented as reader content.

The isolated release build differs from the live tree only in release framing:

1. PDF metadata and the visible title page state the U219 WIP boundary.
2. The introduction uses plain-language topic names where the partial reader
   omits later chapters, avoiding broken reader-facing links.
3. `\end{document}` follows the final `\end{exercise}` of Section 10.6.
4. The exact validated Volume I auxiliary map is supplied to resolve legitimate
   cross-volume references in the standalone Volume II reader.

The release slices for units U217–U219 are text-identical to their admitted
live target slices. Their 87 inline and eight displayed mathematical payloads
are preserved exactly. Dormant source for Section 10.7 remains after
`\end{document}` for reproducibility and cannot enter the reader.

## Converter and structural gates

- Converter terminal status: `Done! (number of errors 0)`.
- The converter log contains three locale-warning header lines and 59 failed
  optional `svgo-ll` lookups. The XML's 121 source paths resolve to one logo,
  60 PDF/TeX overlays, and 60 pre-generated SVGs; every path is relative,
  traversal-free, and present. The final PDF renders successfully.
- The release XML parses with root `pretext`, 594 unique XML IDs, zero duplicate
  IDs, and 833 reference occurrences.
- Eleven nonlocal XML-reference occurrences spanning seven target IDs remain by
  design because the WIP cut omits the end-of-book bibliography: `biblio-BS`,
  `biblio-DW`, `biblio-GIAM`,
  `biblio-Hammack`, `biblio-Rosenlicht`, `biblio-Rudin_baby`, and
  `biblio-Trench`. The public source package retains the untruncated live tree.
- The standalone TeX reader has zero undefined references after importing the
  exact validated Volume I auxiliary map.
- Index: 167 entries accepted, zero rejected, zero warnings.
- Glossary: 44 entries accepted, zero rejected, zero warnings.
  The intentional WIP cutoff precedes the back matter, so neither list is
  printed in this reader.

## TeX, PDF, extraction, privacy, and visual gates

- TeX passes 1–5 exited zero. Passes 4 and 5 are byte-identical: 31,130 bytes,
  SHA-256
  `f3b532b759dbff03f0983d4dfea7ff1bdbf5f410b1e4625876f9fc51d6d61a66`.
- Final PDF: 1,660,232 bytes, 150 letter pages, unencrypted, `/Lang (id-ID)`;
  SHA-256
  `ddf89a837d740fd8d84887b7adc1ebafcf2c0777d9cd529314050961be1fc2cc`.
- All 66 reported font instances are embedded; 25 have explicit ToUnicode maps.
  Full UTF-8 extraction contains zero U+0133 and zero U+FFFD.
- Log scan: zero fatal errors, undefined control sequences, undefined
  references, multiply-defined labels, missing characters, overfull vboxes,
  underfull hboxes, or convergence requests. Two inherited underfull vboxes are
  harmless. Twelve inherited overfull hboxes remain; the maximum is 18.71684 pt,
  below the established 20-pt checkpoint threshold.
- Extracted text contains the exact provenance string
  `OpenAI Codex gpt-5.6-sol, Ultra` once and generic attribution to the user's
  instruction once. Personal-name matches are zero.
- Physical pages 1, 2, 149, and 150 were rendered at 144 dpi and inspected at
  original detail after the final converged build. The WIP notice, provenance,
  prose, formulas, running heads, exercise block, and final-page boundary are
  readable, centered in the established text block, unclipped, and
  nonoverlapping.
- Independent release-content audit reproduced every U217–U219 slice hash,
  confirmed all mathematical payloads, and found no attribution or content loss.

## Frozen identities

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.tex` | 20,707 | `0a0b1921567f6c02739870f9d09cf8c0dab4cb6593b2b8b18442ff0ba3c23e60` |
| `frag-vol2-intro.tex` | 3,702 | `c94fef51d856c913cb7b717a88945510cb4a6fbeadcc8ae8cda64f8f17f7295e` |
| `ch-multivar-int.tex` | 147,420 | `e8420ff221c90f7068311a95d4527bde38638b6ad69ff5ab3a79878ae9da7e40` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `converter-release-u219.console.log` | 1,306,457 | `400e2be421ab1e5ca1293d70f4ab1c23ace6762948a23bd90ec0cca77d83c5c5` |
| `converter-release-u219.stderr.log` | 6,175 | `a4bbd7fbaadc7d4a0b2c62602b0ae613b9dc8866af7372a907a19a38508e6f50` |
| `realanal-out.xml` | 1,475,546 | `0839dc0d4926c097fa623907b79cdb4d472c675001f0d8e21c586793f7564674` |
| `realanal2.log` | 94,241 | `9d5e23b4b00f9a31077797cf7973fd108ec1ff4ad0bb5dc969450b8805d510f0` |
| `realanal2.pdf` | 1,660,232 | `ddf89a837d740fd8d84887b7adc1ebafcf2c0777d9cd529314050961be1fc2cc` |
| `pdflatex-release-u219-pass-4.console.log` | 31,130 | `f3b532b759dbff03f0983d4dfea7ff1bdbf5f410b1e4625876f9fc51d6d61a66` |
| `pdflatex-release-u219-pass-5.console.log` | 31,130 | `f3b532b759dbff03f0983d4dfea7ff1bdbf5f410b1e4625876f9fc51d6d61a66` |
| `makeindex-release-u219-index.stderr.log` | 323 | `e83fad03ffc6b7c8e52a7379b5a71013ee177487671258c8746dc2ae015cc868` |
| `makeindex-release-u219-glossary.stderr.log` | 426 | `f24c69eb63a8fdab13109b0cbef36de69ab784efc94bf561a35c2c61ab483ce5` |
| `visual-qa/front-001.png` | 59,485 | `b02bdcd353c3db8b5939fb13dd5882bcd6281dad56d8a6593c4421b1316c56e1` |
| `visual-qa/front-002.png` | 302,688 | `715418873022420ecbe300fab4edce05e103ddc25a0550e7784d663a62aa8ad3` |
| `visual-qa/tail-149.png` | 287,407 | `4ddcc5a38563108dcaacc7c37927db7218bc9a947ea96ab1ff0ab37a2f45b16a` |
| `visual-qa/tail-150.png` | 165,418 | `4201efa3d97f97f4809a70e2934efa261fd1b7e15ced2edc25eb9f27d61987cb` |
