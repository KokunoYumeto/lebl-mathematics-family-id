# R006 Parseval inverse-square-sum exercise — U424

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.parseval-inverse-square-sum`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5387–5394,
  eight LF-terminated lines / 229 bytes, SHA-256
  `432d8ce695cfacd212eb6af3f8d81dd32a2eef7b51b1fb476f1659dd1012f314`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5401–5408,
  eight LF-terminated lines / 256 bytes, SHA-256
  `2b9a298bc2c7f9c28df47872b7f7b106fb3450545af8dca5e7477b1a4eebe0c7`.
- Full target after translation: 198,093 bytes, SHA-256
  `955e4fd2b360096266939f1b6ada5a493eb6c30af6ffba894086d8d4c518c55b`.
- The exact next untranslated boundary follows the blank source line 5395 /
  target line 5409: the analytic closed-unit-disc exercise begins at source
  raw line 5396 / target raw line 5410. No prose or formula from that exercise
  is included.

The admitted unit is one complete unlabeled exercise. It asks the reader to
apply Parseval's theorem to the `2\pi`-periodic sawtooth function that equals
`x` on `(0,2\pi)` and derive the inverse-square sum `\pi^2/6`.

## Mathematical, structural, and source QA

The source is mathematically coherent under the chapter's normalization. On
`[0,2\pi]`, its complex Fourier coefficients are `c_0=\pi` and `c_n=i/n` for
nonzero integer `n`. Parseval therefore gives
`(1/(2\pi))\int_0^{2\pi}x^2\,dx=4\pi^2/3=\pi^2+2\sum_{n\ge1}1/n^2`, hence the
displayed `\sum_{n\ge1}1/n^2=\pi^2/6`. The periodic endpoint value is immaterial
to the Riemann integral. No correction or adverse-ledger event is warranted.

Automated comparison found the exact ordered 11-command stream, all four
environment events (`exercise` and `equation*`), all four inline-math payloads,
the byte-identical display payload, nine opening and nine closing braces, and
eight dollar delimiters on each side. There are no labels, references,
citations, comments, footnotes, or assets. The translation changes only the
three reader-facing prose lines and introduces no formula, command, topology,
or mathematical-content delta.

## Indonesian-language, terminology, manifest, and O001 QA

The wording `Misalkan $f$ adalah fungsi $2\pi$-periodik sedemikian sehingga`
and `Gunakan teorema Parseval untuk memperoleh` is natural and faithful. It
reuses LEBL-TERM-0663 (`periodik`) and LEBL-TERM-0794 (`teorema Parseval`), so
no new terminology row is needed. An independent mathematical and Indonesian-
language audit passed. It recommended the more idiomatic metadata title
`Latihan: teorema Parseval dan deret kebalikan kuadrat`; that correction was
applied before backend construction and changes no reader text.

The manifest now has 424 unique units: R006 339, R007 35, R008 50. It is
660,713 bytes, SHA-256
`f2f89261ea4691d176924fb4a01b94c0134fa618ea75919043045d4059184f1e`.
The terminology ledger remains 797 rows / 128,552 bytes, SHA-256
`4c965c8a7d39320a3b59f7aea3fa8342c5499ef364ee9aff38de86b58743b9a9`;
the adverse ledger remains 268 rows / 250,881 bytes, SHA-256
`97574309b30de27a14b388c6ef06bab7d9a09a8f2af7c8613ccfcbe405609f6b`.

`LEBL-O001-R006-0029` maps the exercise to
`ra.v2.fourier-series.exercise.parseval-inverse-square-sum`. The instruction
to use Parseval's theorem is an intrinsic required method, not a separately
supplied source hint. The source supplies no hint and no solution; the
translation invents no answer, proof, or support. The O001 ledger now has 29
unique rows / 21,910 bytes, SHA-256
`e7ffce76e11638c78927e7d465339c637dd60e71f7d4e47e384a14ab6bec9edb`.

## Deterministic backend gates

Two current-input builds at
`backend/production/v0.4-live-2026.08.29-u424-a` and `-u424-b` are identical
across exactly 27 files / 17,971,333 bytes. Their canonical 3,292-byte ordinal-
POSIX inventory has SHA-256
`fa1c2d90fdafed7e5042e027d95d7d1cb104e7ecf3c9d74b744ca559516de63a`.
Both `records.jsonl` files are 5,753,630 bytes, SHA-256
`61bc6ef2632467d7e36c4b11285c2ee499e19313bc9d82467120dd3c35bd7b0c`.

Both builds pass schema and referential validation, all 424 manifest bindings,
362 direct component checks, and all 15 lossless CSV round trips over 3,997
records / 848 embedded expressions. The exact U423-to-U424 delta is four new
stable records—live unit, bilingual title segment, QA event, and no-hint O001
unit—with zero removals and only the manifest-artifact record refreshed. The
independently rechecked backend receipt is
`qa/BACKEND_V0_4_LIVE_U424_20260829.md`, 4,263 bytes, SHA-256
`580dfe415274a5cef9518377a97a01f7173f912fe9fe20f3a660029f16ecc77b`.

## Deterministic integration build and visual QA

The isolated build at `tmp/r006-u424-build-20260829` used
`SOURCE_DATE_EPOCH=1787961600` and `TZ=UTC`, with the hash-bound complete
Volume-I auxiliary labels. The converter, index and glossary generation,
`pdflatex` passes 1–9, and an independent pass 10 all exited successfully.
The PDF and all seven tracked auxiliary products are byte-identical from pass
9 to pass 10.

The final non-release integration PDF is 241 pages / 2,427,693 bytes, SHA-256
`e6bb4b925793e0fc27cd3b69b01c126712ebf40d5e4e1bed64dbdd392e90fe8e`.
The final log is 103,379 bytes, SHA-256
`30c70bab0c6f48807a75a4e0a417684e7e07dc2a8b6f63d70b09ca2d29f98d1a`.
There are zero fatal, LaTeX, emergency-stop, undefined-control-sequence,
missing-character, undefined-reference, multiply-defined-label, invalid-link,
or bad-outline-destination errors. The inherited source-wide diagnostics are
15 overfull horizontal boxes, zero overfull vertical boxes, three underfull
horizontal boxes, two underfull vertical boxes, five package-warning lines,
and one final rerun-file-check occurrence with the output file unchanged.

Full text extraction succeeds without replacement characters. All 687 links
(662 internal, 25 external) are valid; all 33 outline items resolve. All 98
font rows are embedded (97 subset), with the expected legacy Type-1 math-font
Unicode-map limitations. Pages 230–233 were rendered at 144 dpi and visually
inspected: they are centered, crisp, and free of clipping, overlap, crowding,
or margin breach. Page 232 contains complete Indonesian Latihan 11.8.8 and
then begins untouched English Latihan 11.8.9, proving the exact next boundary.
This integration PDF is evidence only and does not replace the independently
verified public U397 reader release.

U424 passes translation, mathematical, structural, terminology, O001,
deterministic-backend, reader-build, and visual admission. Public preservation
remains U423 source plus controls until the bounded U424 transaction completes.
