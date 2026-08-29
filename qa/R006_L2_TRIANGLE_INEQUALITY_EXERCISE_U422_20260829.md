# R006 L2 triangle-inequality exercise - U422

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.l2-triangle-inequality`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5350-5356,
  seven LF-terminated lines / 232 bytes, SHA-256
  `3d79e611cc644f6d06a35f696cbfb3ebf7ebbd3cda7abb350c4fd7bdae9c4a44`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5364-5370,
  seven LF-terminated lines / 276 bytes, SHA-256
  `d1e0edcfc4ac0000fb81db8e0bfcf800a3b413a623951116a8d198d88774106f`.
- Full target after translation: 197,967 bytes, SHA-256
  `30a7ef6c6675cae45949b3de4e325d0934289238e6789ebcc3c99be431059f2d`.
- The exact next untranslated boundary is the following unlabeled sequence and
  differential-equation exercise beginning at source raw line 5358 / target
  raw line 5372. No prose or formula from that exercise is included.

The admitted unit is one complete labeled exercise. It asks for the triangle
inequality for the `L^2` norm on Riemann-integrable functions over
`[-\pi,\pi]`.

## Mathematical, structural, and source QA

The source statement is mathematically coherent in the surrounding chapter:
the displayed quantity has just been introduced and the preceding exercise
establishes the integral Cauchy--Bunyakovsky--Schwarz inequality used in the
standard proof. The source later calls this quantity the `L^2` norm; the
already-admitted nearby remark separately explains its seminorm nuance on raw
Riemann-integrable representatives. U422 therefore needs no new source
correction or adverse-ledger event.

The display from `\begin{equation*}` through `\end{equation*}` is
byte-identical in source and target. Automated comparison found the exact
ordered 11-command stream, all four environment events, the label
`exercise:L2triangleineq`, eight opening and eight closing braces, and four
dollar delimiters on each side. The label occurs exactly once in each complete
file. There are no references, citations, comments, footnotes, or assets in
the unit. The translation changes reader-facing prose only and introduces no
formula, command, topology, or mathematical-content delta.

## Indonesian-language, terminology, and O001 QA

The wording `Buktikan bahwa norma $L^2$ memenuhi ketaksamaan segitiga untuk
fungsi-fungsi yang terintegralkan secara Riemann pada $[-\pi,\pi]$` is
natural, concise, and faithful. It follows LEBL-TERM-0779 (`norma L^2`), the
established `ketaksamaan segitiga` wording, and LEBL-TERM-0272
(`terintegralkan secara Riemann`). It also agrees with the preceding Indonesian
exposition. An independent bounded mathematical and Indonesian-language audit
passed without correction. No new terminology row is needed.

`LEBL-O001-R006-0027` maps the labeled exercise to
`ra.v2.fourier-series.exercise.l2-triangle-inequality`. The source supplies no
explicit hint and no solution. Although the preceding Cauchy exercise is
mathematically useful, the source does not link it as a hint; the earlier
exposition merely forward-references this triangle-inequality exercise.
Accordingly the gap is classified as no-hint and solution-absent, and the
translation invents no answer, proof, or support.

## Deterministic integration build and visual QA

The verified U421 build tree was copied to the isolated
`tmp/r006-u422-build-20260829` directory, retaining the bound complete
Indonesian Volume-I auxiliary label set. Index and glossary generation both
completed successfully and reproduced their U421 bytes. The final pair of TeX
passes used the fixed reproducible build epoch `1787961600`; all seven tracked
auxiliary products and the PDF were byte-identical across passes 20 and 21.

The final non-release integration PDF is 241 pages / 2,427,736 bytes,
SHA-256
`a45a0e4e7b4cf7fad3c6cc9a7c112eb486ef8a5391567cb4a7239a8bd75436ef`.
The final log is 104,309 bytes, SHA-256
`adc74d19eeaebba40ea4d9024d7d649b30ebf0b4d76b820d423fb5b29bf14765`;
the final console transcript is 35,349 bytes, SHA-256
`26d4b357076ae0229ffc2bd1951fa8dc843e290f1dce59977319a9dc6c7db352`.
The log contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U421 exactly in count, location, and width and lie
outside this unit; there are zero overfull vertical boxes.

Physical pages 230 and 231 were rendered at 144 dpi and visually inspected.
The preceding Parseval proof and exercises remain legible. Exercise 11.8.6 is
fully localized on page 231; its label heading, complete Indonesian statement,
interval, `L^2` notation, inequality sign, plus signs, and subscripts are crisp
and centered. Line wrapping and spacing are natural, with no clipping,
overlap, crowding, margin breach, or displaced display. The following
still-English Exercise 11.8.7 remains visibly outside U422. The transient PNG
files were removed after inspection. This integration PDF remains build
evidence and does not replace the independently verified public U397 reader
release.

U422 is ready for manifest and O001 admission followed by two deterministic
backend replays. Public U421 source/backend/controls and the U397 reader release
remain unchanged until those gates pass.
