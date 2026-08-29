# R006 one-sided-series analytic-unit-disc exercise — U425

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.one-sided-series-analytic-unit-disc-extension`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5396–5405,
  ten LF-terminated lines / 490 bytes, SHA-256
  `22c9a47d6e095ebf12acd7a5d6562712eee872d5a569093bcc676419202adeea`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5410–5419,
  ten LF-terminated lines / 520 bytes, SHA-256
  `7e6d0f5b214f350d6a143b38b518198944fa56cac9e7089c8d38a4e1459d3dc5`.
- Full target after translation: 198,123 bytes, SHA-256
  `1c51b2b3490f84c2016ff0e2ac4e347f268fb4568f187773147b3c9703151157`.
- The exact next untranslated boundary follows blank source line 5406 /
  target line 5420. The next unlabeled exercise occupies source raw lines
  5407–5413 / target raw lines 5421–5427. Its untouched source slice is 163
  bytes, SHA-256
  `e85f6f5ad566c4f41aebcbaf37528bf0918a24f371a279d027ce2254b11c8270`.

The admitted unit is one complete unlabeled exercise. It asks the reader to
show that an absolutely summable one-sided coefficient sequence defines a
function continuous on the closed unit disc, analytic on the open unit disc,
and equal to the stated Fourier series on the boundary.

## Mathematical, structural, and source QA

The source is mathematically coherent. Define
`f(z)=\sum_{n\ge0}c_nz^n`. Since `\sum|c_n|` converges, the Weierstrass
M-test gives uniform convergence on the closed unit disc and hence continuity
there; the power series is analytic on the open unit disc. Substitution
`z=e^{i\theta}` yields the required boundary series. The condition `c_n=0`
for negative integers records one-sided Fourier support and is not defective.
Under the book's metric notation, `C(0,1)` is the closed ball and therefore
equals `\overline{B(0,1)}` in `\mathbb C`. No correction or adverse-ledger
event is warranted.

Automated and independent comparison found the exact ordered 24-command
stream, both environment events, all 11 inline-math payloads, eleven opening
and eleven closing braces, 22 dollar delimiters, and the literal terminal
`\\` after the boundary formula on each side. There are no displays, labels,
references, citations, comments, footnotes, or assets. Every mathematical
token—including `\D`, `B(0,1)`, `C(0,1)`, all sums and exponents, and the hint
formula—is preserved exactly.

## Indonesian-language, terminology, manifest, and O001 QA

The wording uses natural formal Indonesian: `Andaikan bahwa`, `cakram satuan`,
`cakram satuan tertutup`, `terdapat suatu fungsi kontinu`, `analitik pada`,
and `pada batas ... berlaku`. The explicit `Petunjuk` is concise and faithful.
It reuses LEBL-TERM-0164, -0188, -0257, -0350, and -0651; no new terminology
row is needed. An independent mathematical, Indonesian-language, terminology,
and topology audit passed without correction.

The manifest has 425 unique units: R006 340, R007 35, R008 50. It is 662,792
bytes, SHA-256
`d689bac08ef5909b8edb2730dbedfa6ea1910d5ed6b50221fe09fc1293dd2ffe`.
The terminology ledger remains 797 rows / 128,552 bytes, SHA-256
`4c965c8a7d39320a3b59f7aea3fa8342c5499ef364ee9aff38de86b58743b9a9`;
the adverse ledger remains 268 rows / 250,881 bytes, SHA-256
`97574309b30de27a14b388c6ef06bab7d9a09a8f2af7c8613ccfcbe405609f6b`.

`LEBL-O001-R006-0030` maps the exercise to
`ra.v2.fourier-series.exercise.one-sided-series-analytic-unit-disc-extension`.
The explicit source hint at raw line 5404 is 58 bytes, SHA-256
`75a28bc1762ec343058deee0e9c4dd2070b4dc61a56062c3de4a8775f00ba9cd`;
its target at raw line 5418 is 64 bytes, SHA-256
`e8a6144fdc1fdb8ac3ef8db927faa92e2dd6a1f2fb21bf7179c347c6fb70b6f0`.
The hint is support, not a solution. The source supplies no solution, and the
translation invents no answer or proof. The O001 ledger has 30 unique rows /
22,919 bytes, SHA-256
`c339b9cc841ecdf8e450818b1a6287134345ef766557020e209302a8a8ce42fb`.

## Deterministic backend gates

Two current-input builds at
`backend/production/v0.4-live-2026.08.29-u425-a` and `-u425-b` are identical
across exactly 27 files / 18,027,168 bytes. Their canonical 3,292-byte ordinal-
POSIX inventory has SHA-256
`729587820f9ea940bb7f25377705ceb3ed37015e15c3b86d557d541823e3b9e2`.
Both `records.jsonl` files are 5,768,800 bytes, SHA-256
`7a501666aa2f4053bb42daa4b275b2e9e480fe356bfd376f934fca16955da83c`.

Both builds pass schema and referential validation, all 425 manifest bindings,
364 direct component checks, and all 15 lossless CSV round trips over 4,003
records / 850 embedded expressions. The exact U424-to-U425 delta is six new
stable records—live unit, bilingual title segment, QA event, O001 exercise,
explicit-hint unit, and hint relation—with zero removals and only the
manifest-artifact record refreshed. Independent recomputation found no
discrepancy. The backend receipt is
`qa/BACKEND_V0_4_LIVE_U425_20260829.md`, 3,670 bytes, SHA-256
`592b8e75350029cd73123010c8986d3f6a70e6df2a153683aacf5b8d266f5877`.

## Deterministic integration build and visual QA

The isolated build at `tmp/r006-u425-build-20260829` used
`SOURCE_DATE_EPOCH=1787961600` and `TZ=UTC`, with the hash-bound complete
Volume-I auxiliary labels. The converter completed with zero reported errors;
four index/glossary cycles and `pdflatex` passes 1–11 all exited successfully.

The after-pass-10 stability snapshot is:

- `realanal2.pdf`: 2,427,763 bytes,
  `2166d72eaedfb0bece00d2df99902694c39a0151eb2e8243f568e68587623ba7`;
- `realanal2.aux`: `3e3b8e0cc8ba0e34a2c24adb27862674a5a439e6e90f31cdeec1587cf5a7b62b`;
- `realanal2.glo`: `0541d84431e0605ae6267361f42ae3454caa45629f634546bcd02da9fb1ee781`;
- `realanal2.gls`: `b06efc4add108fb03f49408fc2bb9132b7ccb7afed39a5035216463999620aa8`;
- `realanal2.idx`: `d5e72163b0d3c644cfaace043e91682ef1cefac442daa0c3457d3d38dd4746df`;
- `realanal2.ind`: `65fb6555e016ff14c2c50e32dcc71fbcfb609e2fc89614d0a4af802e81f16ae9`;
- `realanal2.out`: `2c065e08f11ed6602a5c81dabff68821589b3b97f938805ed1138d51d21b158b`;
- `realanal2.toc`: `62db0180d6323a0af694909fef47ea5684950861278a792597faed88fae513ec`.

The pass-10 PDF has 241 pages. Its pass-10 log is 103,379 bytes, SHA-256
`906578a29969a1d2d2ae838367746e2b61fa1c64d552872566138f9f5592364a`.
There are zero fatal, LaTeX, emergency-stop, undefined-control-sequence,
missing-character, undefined-reference, multiply-defined-label, invalid-link,
or bad-outline-destination errors. The inherited source-wide diagnostics are
15 overfull horizontal boxes, zero overfull vertical boxes, three underfull
horizontal boxes, two underfull vertical boxes, five package-warning lines,
and one rerun occurrence.

Full text extraction is 826,395 bytes with zero replacement characters. All
687 links (662 internal, 25 external) are valid; all 33 outline items resolve.
All 98 font rows are embedded and 97 are subset. Pages 230–233 were rendered
at 144 dpi and independently inspected: they are centered, crisp, readable,
and free of clipping, overlap, crowding, or margin breach. Page 232 contains
complete Indonesian Latihan 11.8.9 including `Petunjuk`, followed by the exact
untouched English boundary at Latihan 11.8.10. This integration PDF is evidence
only and does not replace the independently verified public U397 reader.

Independent pass 11 exactly reproduced all eight after-pass-10 byte strings
listed above. Its final log is 103,379 bytes, SHA-256
`5b2bd59e4982b8e91027271deffa71a2e158c5a2343aa6123c469e3018a2d683`;
an independent closure audit confirmed the final diagnostics and all eight
stability identities. U425 therefore passes translation, mathematical, structural,
terminology, O001, deterministic-backend, reader-build, stability, text,
font, link, outline, and visual admission. Public preservation remains U424
source plus its controls overlay until the bounded U425 transaction completes.
