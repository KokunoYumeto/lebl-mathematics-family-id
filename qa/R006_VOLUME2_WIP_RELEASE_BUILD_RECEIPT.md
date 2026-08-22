# R006 Volume II public WIP reader receipt — Unit 216 — 2026-08-22

## Claim and exact boundary

This receipt proves the privacy-safe public work-in-progress reader for
*Analisis Dasar II*. It is not the complete Volume II. The reader contains the
contiguous Indonesian translation through the complete proof of Green's
theorem for a type-III domain (Theorem 10.6.4), ending on physical page 147.
The following vortex-field application and example are not present, and no
untranslated tail is presented as Indonesian content.

The isolated release build differs from the live tree only in release framing:

1. PDF metadata and the visible title page state the U216 WIP boundary.
2. The introduction uses plain-language topic names where the partial reader
   omits later chapters, avoiding broken reader-facing links.
3. `\end{document}` follows the admitted Type III proof.
4. The exact validated Volume I auxiliary map is supplied to resolve legitimate
   cross-volume references in the standalone Volume II reader.

The mathematics is the same material admitted as unit
`ra.v2.green-theorem.type-iii-proof` in the live translation manifest.

## Converter and structural gates

- Converter terminal status: `Done! (number of errors 0)`.
- The converter log contains three locale-warning header lines and 59 failed
  optional `svgo-ll` lookups. Every corresponding SVG already exists, is
  nonempty, and parses as XML, so no figure input is missing.
- The release XML parses with root `pretext`, 592 unique XML IDs, and 831
  reference occurrences.
- Seven nonlocal XML references remain by design because the WIP cut omits the
  end-of-book bibliography: `biblio-BS`, `biblio-DW`, `biblio-GIAM`,
  `biblio-Hammack`, `biblio-Rosenlicht`, `biblio-Rudin_baby`, and
  `biblio-Trench`. The public source package retains the untruncated live tree.
- The standalone TeX reader has zero undefined references after importing the
  exact validated Volume I auxiliary map.
- Index: 162 entries accepted, zero rejected, zero warnings.
- Glossary: 44 entries accepted, zero rejected, zero warnings.
  The index and glossary streams are valid build inputs; the intentional WIP
  cutoff precedes the back matter, so neither list is printed in this reader.

## TeX, PDF, extraction, privacy, and visual gates

- TeX passes 1–5 exited zero. Passes 4 and 5 are byte-identical: 31,471 bytes,
  SHA-256
  `3333e8c2d87519bbbaa13dba8b4904419dbfe8816e9411831fd307878c7c3b29`.
- Final PDF: 147 letter pages, unencrypted, `/Lang (id-ID)`.
- All 66 reported font instances are embedded; 25 have explicit ToUnicode
  maps.
- Log scan: zero fatal errors, undefined control sequences, undefined
  references, multiply-defined labels, missing characters, overfull vboxes,
  underfull hboxes, or convergence requests. One inherited underfull vbox is
  harmless. Twelve inherited overfull hboxes remain, maximum 18.71684 pt,
  below the established 20-pt checkpoint threshold.
- Extracted text contains the exact provenance string
  `OpenAI Codex gpt-5.6-sol, Ultra` once and generic attribution to the user's
  instruction once. Personal-name matches are zero in the release PDF and XML.
- Extracted text contains zero U+0133 and U+FFFD, zero occurrences of the first
  omitted English application sentence, and zero occurrences of the omitted
  English vortex-field term.
- Physical pages 1, 2, 146, and 147 were rendered at 144 dpi and inspected at
  original detail after the final converged build. The WIP notice, provenance,
  figure, prose, formulas, running heads, proof mark, and final-page boundary
  are readable, centered in the established text block, unclipped, and
  nonoverlapping.

## Frozen identities

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.tex` | 20,719 | `52233af3820e3ce192ec1773bb6f3c07a57deff4c7e210b86245f1f66bd4202c` |
| `frag-vol2-intro.tex` | 3,702 | `c94fef51d856c913cb7b717a88945510cb4a6fbeadcc8ae8cda64f8f17f7295e` |
| `ch-multivar-int.tex` | 146,587 | `c0e1a10c1c6cdfcde3f6ad6260b81d160e6d8d41ecd25495fcdfbacb12b0ddc0` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `converter-release-u216.console.log` | 1,303,145 | `ae76eb9891c525cfda6555ec281d0d91fea4ab9d6915ef64c90450977047dec7` |
| `realanal-out.xml` | 1,464,804 | `8c34199718ec623a35e05a4bb12d6bcf6731095ea58f3b654c062ad171a366e7` |
| `realanal2.log` | 93,822 | `259eeb66849d7f4043be6ba0a240930053d339e7b879953a67e5ed553cd77242` |
| `realanal2.pdf` | 1,641,445 | `152eec620c0d42a01a12f6b7f4b3e6e18d914359e164e573fffcad040c09ddb2` |
| `pdflatex-release-u216-pass-4.console.log` | 31,471 | `3333e8c2d87519bbbaa13dba8b4904419dbfe8816e9411831fd307878c7c3b29` |
| `pdflatex-release-u216-pass-5.console.log` | 31,471 | `3333e8c2d87519bbbaa13dba8b4904419dbfe8816e9411831fd307878c7c3b29` |
| `makeindex-release-u216-index.console.log` | 323 | `f75c5c560a0ebe4a21aa78a0e163c2044aa31f307687a08fac47a52f712a0ddd` |
| `makeindex-release-u216-glossary.console.log` | 426 | `f24c69eb63a8fdab13109b0cbef36de69ab784efc94bf561a35c2c61ab483ce5` |
