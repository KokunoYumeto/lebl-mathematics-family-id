# R006 Volume I complete translation checkpoint — 2026-08-21

## Boundary and claim

The Indonesian translation of R006 Volume I, *Basic Analysis I*, is complete through the end of Chapter 7. This checkpoint proves the complete Volume I LaTeX/PDF build and the combined PreTeXt converter boundary. It does **not** claim that R006 is complete: Volume II translation has begun, and the final accessible HTML reader remains a later full-edition gate.

## Reproducible build

The final build was produced in the bounded directory `qa/builds/ra-id-volume1-complete-20260821-final` from the admitted `translation/ra` sources. The build sequence was:

1. run `convert-to-mbx.pl` against the combined Indonesian driver;
2. run four rounds of `pdflatex`, `makeindex`, and `makeglossaries`;
3. run a fifth and final `pdflatex` pass.

The converter ended with the exact status `Done! (number of errors 0)`. The final TeX log contains zero LaTeX errors, emergency stops, fatal errors, undefined control sequences, unresolved references or citations, rerun warnings, missing files, and missing-character warnings.

## Frozen final artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `realanal-volume1-id.pdf` | 2,871,094 | `18aad665c92f5a15e76bedd412f5694e800e8d48c6e150e6d7916dc6bebf4483` |
| `realanal-out.xml` | 1,654,092 | `2199e5881abe8082b0ab6b90ea96acc78a18ce99039c92dec4a541d2d64c044b` |
| `realanal.log` | 111,771 | `c511ddbfdd5c04cae09dc59603d1a93f4a07b31e569133e88cccb51741973d68` |
| `pdflatex-pass-5.console.log` | 36,233 | `fccc105786fb2f92f1c74050cc7cb4cdf7521e3ba464c31a44aa96741a19e351` |
| `converter.console.log` | 1,464,436 | `d552780b6e997f031a834eadbfc5183ef38173199f5bf76dd550fea32190d3e3` |
| `alttexts.txt` | 64,162 | `8c2f0692aec7daa6435a3d453f992603aa78d8661b187e2eaff4eb7361cb9471` |
| `translation/ra/convert-to-mbx.pl` | 52,543 | `3237805eafa1e024e1e0b0637fd0975dcc5d05894e8512dec65f449c297bacfb` |

## PreTeXt/XML gate

The generated document parses as well-formed XML. Its root is `pretext`, its language is `id-ID`, and it contains 32,740 elements, 672 IDs, 672 unique IDs, zero duplicate IDs, 952 cross-references, and zero unresolved cross-references. The converter now escapes literal ampersands and less-than signs only while serializing TeX macro character data; parsing recovers the original TeX payload, including the literal `<10` test.

## PDF structural gate

The final PDF has 334 Letter pages and is unencrypted. Metadata reads:

- title: `Analisis Dasar: Pengantar Analisis Real`;
- subject: `Analisis Real`;
- author: `Jiří Lebl`;
- catalog language: `id-ID`.

All 142 font rows are embedded. Ninety-five rows lack a Unicode map, an upstream TeX-font limitation; visual glyph rendering is complete. The PDF is not structurally tagged. That limitation is disclosed rather than treated as solved: the final R006 release still requires the accessible PreTeXt/HTML reader gate.

The final log contains 17 overfull horizontal boxes, none at or above 20 pt; the maximum is 19.30838 pt. It contains zero overfull vertical boxes, two underfull horizontal boxes, and one underfull vertical box. Every reported location was included in the all-page visual review and none clips the physical page. A PDF-text scan found no generated English UI label; the only relevant English phrase was the proper cited title *Book of Proof*.

## Exhaustive visual gate

All 334 physical pages were rendered at 72 dpi. The initial build was inspected through 17 contact sheets. Two hard clipping defects were found and corrected: the long ten-term sequence on physical page 64 and the popcorn-function condition on physical page 136. A 33.79503 pt display overflow on physical page 160 was also reflowed.

Pixel comparison proved that the first correction changed only pages 64–66 and 136, and the last correction changed only page 160. Those changed final pages were inspected directly at high resolution; every other final page is byte-identical at the rendered-pixel level to its already inspected predecessor. The final render set contains 334 PNG files totaling 39,525,828 bytes. Its deterministic logical manifest—one UTF-8 LF line per page in the form `page,size,sha256`—has SHA-256 `1b7c04519fe3de63a84adf48e5a0388b9b87231db8f06fd718a2171a9e26e65b`.

Final visual result: zero clipping, overlap, broken or missing page, missing figure, missing glyph, or header/footer/page-number defect.

## Corrections bound to this checkpoint

- `ch-seq-ser.tex` unit `ra.v1.sequences-series.sequences-limits.tail`: ten terms retained in exact order and split across two aligned rows; target unit SHA-256 `d927797987e938bcf7b2940dea7a9d7e10bcdcdfd34f7c69cdb4a3ccca3c2da4`.
- `ch-contfunc.tex` unit `ra.v1.continuous-functions.continuity.discontinuous-functions`: the equivalent relatively-prime denominator condition is split across two aligned rows; target unit SHA-256 `c1881332876cbd62a9e853c90329c49a8281ba1533c486e674f38d8b73936c9b`.
- `ch-contfunc.tex` unit `ra.v1.continuous-functions.limits-at-infinity.exercises`: the sequential characterization is split across two aligned rows; target unit SHA-256 `8c0533c3b230b2fd265417e1722ab52acf57210c8ecb4aea2c8d448ca2b8d4cb`.
- `convert-to-mbx.pl`: XML-safe macro serialization described above; whole-file SHA-256 `3237805eafa1e024e1e0b0637fd0975dcc5d05894e8512dec65f449c297bacfb`.

These changes are recorded in `TRANSLATION_MANIFEST.jsonl` and adverse events `LEBL-ID-ADV-0078` through `LEBL-ID-ADV-0081`.

## Continuation

The next production boundary is R006 Volume II, Chapter 1, *Several Variables and Partial Derivatives*. The first unit, Vector Spaces, is translated through the line immediately preceding `\subsection{Linear combinations and dimension}`. R007 and R008 remain queued behind completion of R006.
