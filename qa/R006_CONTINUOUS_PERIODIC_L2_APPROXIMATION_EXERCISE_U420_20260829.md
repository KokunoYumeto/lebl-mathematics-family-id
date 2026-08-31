# R006 continuous-periodic L2-approximation exercise - U420

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.continuous-periodic-l2-approximation`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5331-5337,
  seven LF-terminated lines / 292 bytes, SHA-256
  `ed17fcb490e03332967408bddf0d5f03a93c94b2a3bb9218157c869fbe958add`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5345-5351,
  seven LF-terminated lines / 325 bytes, SHA-256
  `9e86d262314828970003c93b39afd3032a371d889609df05cd30f11eaf64a0eb`.
- Full target after admission: 197,901 bytes, SHA-256
  `c0d3310ba9e8eaf4e5cbb25be6fd901b9a64c142905bfec9bbb7a11fd288a045`.
- The exact next untranslated boundary is the labeled
  Cauchy--Bunyakovsky--Schwarz exercise at source raw lines 5339-5348 / target
  raw lines 5353-5362. No prose or formula from that exercise is included.

The admitted unit is one complete labeled exercise. It asks for approximation,
in the chapter's normalized `L^2` norm, of an arbitrary Riemann-integrable
complex-valued `2pi`-periodic function by a continuous complex-valued
`2pi`-periodic function.

## Mathematical, structural, and source QA

The statement is mathematically coherent and supplies every hypothesis needed
by the Parseval proof that cites it at source raw line 5188. Continuous
periodic functions are dense in the Riemann-integrable periodic functions for
the `L^2` norm; the stated epsilon approximation is the standard finite-step
approximation followed by continuous interpolation near finitely many
partition boundaries. No source defect, missing hypothesis, or content repair
is present, so no adverse-ledger event is added.

Automated comparison found seven identical ordered inline-math payloads in
source and target, including both function signatures, the exact interval,
epsilon inequality, and complete norm inequality. All 14 dollar delimiters,
the exact ordered 18-command stream, both exercise-environment events, the
label `exercise:contL2close`, and all four opening plus four closing braces are
byte-preserved. There are no displays, references, citations, comments,
footnotes, or assets in the unit. The translation changes reader-facing prose
only and introduces no formula, command, topology, or mathematical-content
delta.

## Indonesian-language, terminology, and O001 QA

Independent language review passed the wording. It uses the established forms
`fungsi kontinu`, `periodik`, `terintegralkan secara Riemann`, and the existing
normalized-norm notation. The construction `terdapat suatu fungsi kontinu
$2\pi$-periodik ... sedemikian sehingga` matches the already admitted Parseval
proof that cites this exercise. No new logical terminology row is needed.

`LEBL-O001-R006-0025` maps the labeled exercise to
`ra.v2.fourier-series.exercise.continuous-periodic-l2-approximation`. The
source contains neither a hint nor a solution. The earlier Parseval proof uses
the result but does not prove it and is not reclassified as source support.
The translation invents no answer, proof, hint, or solution.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in
`tmp/r006-u420-build-20260828` with the bound complete Indonesian Volume-I
auxiliary label set, SHA-256
`8696b0f4e80ddfe0093da26955f868304892bf081eb01c04d21feedd1815d5c2`.
The initial seven TeX passes completed. An observation interruption then
truncated only the derived pass-eight auxiliary outputs; no source or canonical
artifact changed. The exact derived auxiliary set was restored from the
verified U419 build, pass eight was rerun with index and glossary generation,
and passes nine through eleven completed. All seven tracked auxiliary products
were byte-identical before and after pass eleven.

The final non-release integration PDF is 241 pages / 2,427,704 bytes,
SHA-256
`3f7d8136e55582e794260719bd23cdfbe9e9b7d4cd8b25647fd699cd63349139`.
The final log is 104,309 bytes, SHA-256
`a0768e3623a55a733b2be08c2faa0a9216c34e93affc1b17fe4e0187db5ca1e4`;
the final console transcript is 35,349 bytes, SHA-256
`f52e8df5a5d84ec4310d4c5a610cac553ffb1577aac75fbfca61a9af919d7fb3`.
The log contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U419 exactly in count, location, and width and lie
outside this unit; there are zero overfull vertical boxes.

Physical pages 230 and 231 were rendered at 144 dpi and visually inspected.
The complete Indonesian exercise appears as Exercise 11.8.4 on page 231 with
legible mathematical symbols, natural wrapping, consistent indentation, and
no clipping, overlap, crowding, or margin breach. Page 230 preserves the prior
exercise boundary, and page 231 shows that the following still-English
exercise remains outside U420. The transient PNGs were removed after
inspection. This integration PDF remains build evidence and does not replace
the independently verified public U397 reader release.

U420 is ready for manifest and O001 admission followed by two deterministic
backend replays. Public U419 source/backend/controls and the U397 reader release
remain unchanged until those gates pass.
