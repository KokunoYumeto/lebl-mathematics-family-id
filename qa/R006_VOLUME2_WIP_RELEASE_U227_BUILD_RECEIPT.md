# R006 Volume II public WIP reader receipt - Unit 227 - 2026-08-23

## Claim and exact boundary

This receipt proves the public work-in-progress reader for *Analisis Dasar II*
at manifest unit U227. It is not the complete Volume II. The reader contains
the contiguous Indonesian translation through Proposition 10.7.1, Theorem
10.7.2, and the theorem's complete proof. It ends on physical page 154 after
the QED. The Section 10.7 exercises begin after the cut and are not included.
Volume I is complete; R007 and R008 remain untranslated.

The isolated release build is a source cut, not a page-truncated PDF. It starts
from the live U227 chapter source and differs only in release framing:

1. PDF metadata and the visible title page state the exact U227 WIP boundary.
2. The partial-reader introduction uses plain topic names where later chapters
   are omitted, avoiding broken reader-facing links.
3. The three proof references to Exercises 10.7.2-10.7.4 are rendered as plain
   exercise numbers with an explicit note that they lie outside this excerpt;
   this preserves the references without dead PDF links.
4. Exactly one `\end{document}` follows the final `\end{proof}`, before
   the untranslated exercise subsection.
5. The exact validated Volume I auxiliary map resolves legitimate cross-volume
   references in the standalone Volume II reader.

Dormant later source remains after `\end{document}` for reproducibility and
cannot enter the reader. All mathematical payloads in U221-U227 remain
byte-identical to the admitted live target slices. The only release-overlay
changes inside those units are the three plain, explicitly out-of-scope
exercise references above.

## Converter, XML, and source-asset gates

- Converter exited zero and ended `Done! (number of errors 0)`.
- `realanal-out.xml` parses as `pretext` with locale `id-ID`, 28,969
  elements, 597 unique IDs, zero duplicate IDs, and 839 reference occurrences.
- Seven bibliography IDs are nonlocal in the release XML because the deliberate
  WIP cut omits the end-of-book bibliography: `biblio-BS`, `biblio-DW`,
  `biblio-GIAM`, `biblio-Hammack`, `biblio-Rosenlicht`,
  `biblio-Rudin_baby`, and `biblio-Trench`. The public source archive
  retains the complete live tree.
- All 121 unique image-source descriptors resolve under the release directory
  with format-aware lookup: 59 pre-generated SVGs, 61 TeX/PDF overlay pairs,
  and one logo asset. Optional generated `*-mbxpdft.svg` variants are not
  claimed; the complete TeX/PDF build path is closed and reproducible.
- Converter stderr contains only the known Windows Perl locale fallback.

## TeX, index, glossary, link, and reader gates

- TeX passes 1-5 exited zero. Passes 4 and 5 have byte-identical 31,217-byte
  console logs, SHA-256
  `2438472158b85d03530b05203e09189add591d4a90ccb819cf323d726958f214`.
- The final log has zero LaTeX errors, undefined controls/references,
  multiply-defined labels, convergence requests, or missing characters. It
  retains 12 bounded inherited overfull hboxes, maximum 18.71684 pt, and two
  harmless inherited underfull vboxes.
- Index generation accepted 167 entries; glossary generation accepted 44.
  Both rejected zero entries and emitted zero warnings. The WIP cutoff precedes
  the printed back matter.
- The 154-page PDF contains 221 internal link annotations and 21 outline
  destinations. Every retained link and outline destination resolves to a page
  inside the reader; there are zero destinations beyond the cut.
- Final PDF: 1,687,583 bytes, 154 US-letter pages, unencrypted, `/Lang
  (id-ID)`; SHA-256
  `b4da246e79fb30ea74e8fcf48ec0fa50aa2680f52585f6b89f66762d7f7876ed`.
- All 66 reported font instances are embedded; 25 have explicit ToUnicode
  maps. Full UTF-8 extraction has zero U+FFFD and U+0133 characters.
- Extracted text contains the exact provenance string `OpenAI Codex
  gpt-5.6-sol, Ultra` once and generic user-instruction attribution once.
  Source authorship, copyright, dual-license notice, NSF acknowledgment,
  bibliography/source URLs, and human credits are preserved. User
  personal-name matches are zero.
- Physical pages 1, 2, and 151-154 were rendered at 144 dpi and inspected at
  original detail. The title and license pages, proposition, theorem, proof,
  revised Figure 10.17 caption, plain out-of-scope exercise references, and
  final QED are centered in the established text block, readable, unclipped,
  and nonoverlapping. No English exercise heading or post-boundary content is
  present.

## Principal artifact identities

All hashes are SHA-256.

| File | Bytes | SHA-256 |
|---|---:|---|
| `realanal2.tex` | 20,708 | `af6b1c24c3f510c5e984ec460e0c3bd4bacb9fa788d15952bb1c3b9df4e8f410` |
| `frag-vol2-intro.tex` | 3,702 | `c94fef51d856c913cb7b717a88945510cb4a6fbeadcc8ae8cda64f8f17f7295e` |
| `ch-multivar-int.tex` | 148,308 | `a99f2be96c6e1eacaf72c795d53db737bc226c7323a2aa69160a29c85c1bc8e1` |
| `realanal.aux` | 359,397 | `f7d44a16a503d8100180e3f5bcd4502a6770fe2eb40994ba4319a01ffc8dffda` |
| `converter-release-u227.console.log` | 1,315,519 | `7fd53755e72a30fc791a4df68b73d0c557b1d3a4939fbddfb57493f5ee3a8a2a` |
| `converter-release-u227.stderr.log` | 393 | `57183f2646e20faf44dfd55c212cfffb98328b1d5d3de478116a3bede3a033be` |
| `realanal-out.xml` | 1,488,799 | `a7056e0282a1fa63c74c84e1e8fc6f8020619085ea3b89cae0edfbcfa53a1845` |
| `realanal2.log` | 94,625 | `98a42651f1956fec41de79caedd65bf305d2b2168b01e77ca970fffe91526887` |
| `realanal2.pdf` | 1,687,583 | `b4da246e79fb30ea74e8fcf48ec0fa50aa2680f52585f6b89f66762d7f7876ed` |
| `realanal2.extracted.txt` | 532,140 | `205e77a1b83006290c63c431a2178b423c198a176b0324e9a958d1c8770d9138` |
| `visual-qa/u227-front-001.png` | 58,933 | `2e0864ba50d7710e20d849ee2fbd1a2ea0b02629bc6265630118997d04684018` |
| `visual-qa/u227-front-002.png` | 302,688 | `715418873022420ecbe300fab4edce05e103ddc25a0550e7784d663a62aa8ad3` |
| `visual-qa/u227-tail-151.png` | 350,893 | `c78cb0ad2dfc5c23929fcc85598491ac4f2c14805082eee1348813b3b9a4baef` |
| `visual-qa/u227-tail-152.png` | 430,194 | `bc223751d2b7be7d1a635ec23ba0a0111214e9bad190dc8f4b55613d64bc8f58` |
| `visual-qa/u227-tail-153.png` | 215,646 | `0aa50d2014db80e1171f0b035963741d1143b2ee69f20d7be498d3843322ee72` |
| `visual-qa/u227-tail-154.png` | 233,730 | `48522e000b77cd741421b2ba700b6aa06732036acdce206088e76ca2183fce17` |
