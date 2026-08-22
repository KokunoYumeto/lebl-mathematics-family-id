# R006 Volume II Green-section Jordan-measurability checkpoint — 2026-08-22

## Scope

- Lane: R006, *Basic Analysis II* / *Analisis Dasar II*.
- Completed unit: `ra.v2.green-theorem.jordan-measurability`.
- Frozen source slice: `source/ra/ch-multivar-int.tex`, raw lines
  3182–3211 inclusive, the complete proposition and proof.
- Live target slice: `translation/ra/ch-multivar-int.tex`, raw lines
  3199–3228 inclusive, the complete localized proposition and proof.
- Isolated build directory:
  `qa/builds/ra-id-volume2-green-jordan-measurability-20260822`.

The isolated build contains the exact live target chapter: 146,315 bytes,
SHA-256 `b78ed52fff4b0ba39f6d6da5a0de0544961e58ef2955b248efb221cd503a3d44`.
The converter, index, glossary, and all TeX passes exited zero. The known
validated Volume I auxiliary file was bound so every external reference
resolves. Final TeX passes 4 and 5 have byte-identical console logs and prove
convergence. This is a contiguous proposition checkpoint, not the complete
Green section, Chapter 3, Volume II, R006, or three-book lane.

## Unit binding and topology

- Source slice: 30 lines, 1,005 bytes; SHA-256
  `5db4b7969c04a5145fe82c6b57ec1eb29d197fc3d2877b63ee4c81e5e6d95d21`.
- Target slice: 30 lines, 1,200 bytes; SHA-256
  `e800535091c24882dd5ee089a927e4a57a0c5c9ac4a99cbd3e6949352ea92d09`.
- Exact environment order and nesting are preserved: one proposition, one
  proof, and one `equation*` display. All three begins and ends balance.
- The sole reference `propref{prop:imagenull}` is preserved. Neither slice has
  labels, index/glossary hooks, figures, assets, URLs, lists, or footnotes.
- Both slices have 10 opening and 10 closing braces and 32 dollar delimiters.
  The displayed map, its domain and codomain, zero-section image identity,
  endpoint argument, and all nullity conclusions are exact; only
  `text{as}`→`text{dengan}` localizes mathematical prose.
- Three independent final audits passed: full mathematical replay; natural
  formal id-ID and ledger consistency; and environment/formula/xref topology.
  No source correction was needed. Reader-facing English residue and
  U+0133/U+FFFD inside the admitted boundary are zero.

## Converter, TeX, and visual gates

- Converter final status: `Done! (number of errors 0)`.
- `realanal-out.xml` parses; root `pretext`; declared locale `id-ID`; 672 IDs,
  672 unique, zero duplicates; 952 references, zero unresolved.
- Final TeX passes 4–5 exited zero and have identical 33,083-byte console logs,
  SHA-256
  `7a67c4821f5313c5be8530d7dee38f1f775896bdcf8ba59cb855944ebe8c7baf`.
  There are zero rerun or undefined-reference warnings.
- Index: 253 accepted, zero rejected, zero warnings. Glossary: 59 accepted,
  zero rejected, zero warnings.
- Final log: zero TeX control errors, undefined control sequences, emergency
  stops, fatal errors, missing-character diagnostics, undefined references,
  multiply-defined labels, rerun warnings, and overfull vboxes. One inherited
  underfull vbox remains in the whole driver and is visually harmless.
- Twelve inherited overfull hboxes remain in the whole driver; maximum
  18.71684 pt, below the 20 pt checkpoint threshold.
- PDF: 233 pages, letter size, unencrypted, `/Lang(id-ID)`, all 97 font
  instances embedded, and 26 instances with explicit ToUnicode maps. Text
  replay reports zero U+0133 and U+FFFD.
- Physical pages 144–145 were rendered at 144 dpi after final convergence and
  inspected at original detail. The proposition begins cleanly on page 144;
  the proof continues under the carried orientation figure on page 145 and
  ends before the next theorem. Text, display, link, proof mark, figure,
  running heads, and page numbers are centered in the reading area, readable,
  unclipped, and nonoverlapping. The English Green theorem beginning below the
  proof is strictly beyond this unit's cursor.

## Artifact hashes

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `ch-multivar-int.tex` | 146,315 | `b78ed52fff4b0ba39f6d6da5a0de0544961e58ef2955b248efb221cd503a3d44` |
| `converter.console.log` | 1,504,549 | `b2ba51030bd80816ccf014a5773d9937ddaf93cafc049fa16eaa811118d0ca69` |
| `pdflatex-pass-4.console.log` | 33,083 | `7a67c4821f5313c5be8530d7dee38f1f775896bdcf8ba59cb855944ebe8c7baf` |
| `pdflatex-pass-5.console.log` | 33,083 | `7a67c4821f5313c5be8530d7dee38f1f775896bdcf8ba59cb855944ebe8c7baf` |
| `makeindex-index.console.log` | 324 | `6189a2ec1fcce39fd1d11c9c334bb5a78ca776b563dc3985454e80ae4335ef0e` |
| `makeindex-glossary.console.log` | 427 | `a5eb1dd64c7a6375ce2fe40c91f6c7b1bf239d1cd72ad2994173f58dc89d4a7b` |
| `realanal.aux` | 210,971 | `dccb4b49f305206fac22db12760c9fbcd03d209c267a18301ddbd8f821ca521c` |
| `realanal2.log` | 101,677 | `19fb98e7c1bb93cde62b663b40f7cadfa7d86eaef140d068d6baf80219f55d1d` |
| `realanal2.pdf` | 2,180,808 | `d59b9c8ca5843952cbb0b9499cd31b45d68a3cbb197e922e0913c21ee5e3e736` |
| `realanal-out.xml` | 1,696,271 | `a9504a958c6f4960187b0aa60e51dfc60f68038d6a74620aad31482177fb3a38` |
| `realanal2.idx` | 11,865 | `5ce94ae88eca0baa89f12e5a7f6ae4fc0b05628e29ea9c71265082c70375b5e1` |
| `realanal2.ind` | 11,257 | `3a9bb0323fbeffebd5085c660529d31a54febd717306b79d71a8203354cf0bfe` |
| `realanal2.glo` | 5,596 | `c9e69c64131559eea532e31e7071571739736c22b341385ddeaf585990265eb0` |
| `realanal2.gls` | 6,287 | `258cd827db811d211ca573e3b6e5a3e95e2bcfada77b78a54e8d656afb28c7bd` |
