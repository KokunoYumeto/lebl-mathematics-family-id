# R006 Volume II public WIP reader receipt — Unit 214 — 2026-08-22

## Claim and boundary

This receipt proves the current public work-in-progress reader for *Analisis
Dasar II*. It is not the complete Volume II. The reader contains translated
material contiguously through Proposition 10.6.3 and its proof at the opening
of Section 10.6, ending on physical page 145 before the statement of Green's
theorem. No untranslated theorem or later material is present.

The release build is isolated from the live translation tree. Its only
publication-specific changes are:

1. PDF metadata and the visible title page identify a dated work-in-progress
   ending at Proposition 10.6.3 and explicitly state that the following Green
   theorem is not included.
2. The introduction replaces cross-references into omitted later chapters with
   equivalent plain-language topic names, so the partial reader has no broken
   reader-facing chapter links or English `Chapter` residue.
3. `\end{document}` is inserted immediately after the admitted proof. The
   command itself flushes the pending orientation figure, avoiding a redundant
   `\clearpage` that the source converter cannot interpret.

These changes affect release framing only. The admitted mathematics is the
same content bound through unit
`ra.v2.green-theorem.jordan-measurability` in the live manifest.

## Gates

- Release converter: `Done! (number of errors 0)`.
- The truncated release XML parses with 591 unique IDs and 829 references. Its
  seven nonlocal references are exclusively bibliography IDs (`biblio-BS`,
  `biblio-DW`, `biblio-GIAM`, `biblio-Hammack`, `biblio-Rosenlicht`,
  `biblio-Rudin_baby`, `biblio-Trench`) because the WIP cut intentionally
  omits the end-of-book bibliography. The public source/backend ZIP carries the
  untruncated live tree; this release XML is build evidence, not a published
  standalone machine-readable edition.
- Final PDF: 145 letter pages, unencrypted, `/Lang(id-ID)`.
- All 64 reported font instances are embedded; 24 have explicit ToUnicode maps.
- Final TeX log: zero control errors, undefined control sequences, missing
  characters, undefined references, multiply-defined labels, rerun warnings,
  overfull vboxes, emergency stops, and fatal errors. One inherited underfull
  vbox is visually harmless.
- Final passes 4 and 5 exited zero and have byte-identical 31,429-byte console
  logs, SHA-256
  `b6589d55f1e87bd460e7ecb57eb39c09d149a2a9d212be718930d7abf031e4e4`,
  proving convergence.
- Index: 158 entries accepted, zero rejected, zero warnings. Glossary: 44
  entries accepted, zero rejected, zero warnings.
- Twelve inherited overfull hboxes remain; maximum 18.71684 pt, below the
  established 20-pt checkpoint threshold.
- Full PDF text replay contains zero U+0133 and U+FFFD. Searches for the omitted
  tail phrases `Suppose U`, `We stated Green`, `Proof of Green`, `piecewise
  smooth boundary`, `Jordan measurable`, `is a null set`, and `Then U is` all
  return zero.
- Physical pages 1, 5, 6, 144, and 145 were rendered at 144 dpi and inspected
  at original detail after convergence. The WIP notice, localized introduction,
  terminal definitions/proposition/proof, carried figure, footnote, running
  heads, and final page are centered in the reading area, readable, unclipped,
  and nonoverlapping. The final page ends cleanly after the proof mark.

## Final identities

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.tex` | 20,670 | `e679bd167d3e51ae39f8077a69b5d2340827521bb13d45c293b3acb291204a7d` |
| `frag-vol2-intro.tex` | 3,702 | `c94fef51d856c913cb7b717a88945510cb4a6fbeadcc8ae8cda64f8f17f7295e` |
| `ch-multivar-int.tex` | 146,331 | `2023dbe1729acb689233cdb3c952a06a775b15f9a608bba1eb456065b3f0e879` |
| `converter-release-u214.console.log` | 1,289,548 | `26c10bdd130d7e824ffdb97ca9983e2bdf83ac91c291a812be3e23ce163ba525` |
| `realanal2.log` | 93,535 | `fdac5c35a3110b21b7161c7567c629ad9437b21749ff636ffb73e94f8a5fd3fb` |
| `realanal2.pdf` | 1,403,109 | `3754752a6f8764b7e4ead731e7d72fbd4de41641c6f6899d1f1ad37df0d6d330` |
| `realanal-out.xml` | 1,459,732 | `31ea38dcae43b96c8a5647d8dcc4f1d9180b333d5343e945392c9dd993f4097d` |
| `pdflatex-release-u214-pass-4.console.log` | 31,429 | `b6589d55f1e87bd460e7ecb57eb39c09d149a2a9d212be718930d7abf031e4e4` |
| `pdflatex-release-u214-pass-5.console.log` | 31,429 | `b6589d55f1e87bd460e7ecb57eb39c09d149a2a9d212be718930d7abf031e4e4` |
| `makeindex-release-u214-index.console.log` | 323 | `77ee2a1e51df5412ffe1c9093d909e2c896862cc57fc09da74e8c2741ce8d29d` |
| `makeindex-release-u214-glossary.console.log` | 426 | `f24c69eb63a8fdab13109b0cbef36de69ab784efc94bf561a35c2c61ab483ce5` |
