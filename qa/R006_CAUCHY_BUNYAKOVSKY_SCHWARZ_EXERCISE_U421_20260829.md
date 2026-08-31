# R006 Cauchy--Bunyakovsky--Schwarz exercise - U421

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.cauchy-bunyakovsky-schwarz`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5339-5348,
  ten LF-terminated lines / 288 bytes, SHA-256
  `8d0d24039889219641fb364fa847df02b2c945867b5b14124015305219f213e4`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5353-5362,
  ten LF-terminated lines / 310 bytes, SHA-256
  `bb751a2e384452a4b4dc901d5e980e73a015b23d2805849c05d185feb811df8a`.
- Full target after admission: 197,923 bytes, SHA-256
  `cebfa8f8e595391551175380f82cb3d63bc7e430c39b5201d5ac4b3c6706df88`.
- The exact next untranslated boundary is the labeled `L^2` triangle-
  inequality exercise at source raw lines 5350-5356 / target raw lines
  5364-5370. No prose or formula from that exercise is included.

The admitted unit is one complete labeled exercise. It asks for the
Cauchy--Bunyakovsky--Schwarz inequality for Riemann-integrable functions and
retains the source's complex-conjugate integral form.

## Mathematical, structural, and source QA

The displayed inequality is mathematically coherent in the surrounding
chapter context: `f` and `g` are complex-valued Riemann-integrable functions
on `[a,b]`, and the conjugation on `g` makes the left side the modulus squared
of their integral pairing. It is precisely the inequality invoked in the
preceding Parseval proof. No hypothesis, symbol, endpoint, exponent, or
conjugation is missing from the source-bound statement, so no adverse-ledger
event is added.

The complete display, from `\begin{equation*}` through
`\end{equation*}`, is byte-identical in source and target. Automated
comparison found the exact ordered 17-command stream, all four environment
events, the label `exercise:L2cauchyschwarz`, ten opening and ten closing
braces, and zero dollar delimiters on each side. There are no references,
citations, comments, footnotes, or assets in the unit. The translation changes
reader-facing prose only and introduces no formula, command, topology, or
mathematical-content delta.

## Indonesian-language, terminology, and O001 QA

The wording `Buktikan ketaksamaan Cauchy--Bunyakovsky--Schwarz untuk
fungsi-fungsi yang terintegralkan secara Riemann` is concise, grammatical,
and consistent with the surrounding chapter. It follows TERM-0626 for a named
inequality and the already admitted Cauchy--Schwarz concept in TERM-0329 and
TERM-0403. The longer source proper name is preserved exactly and agrees with
the nearby Indonesian Parseval proof. No new logical terminology row is
needed.

`LEBL-O001-R006-0026` maps the labeled exercise to
`ra.v2.fourier-series.exercise.cauchy-bunyakovsky-schwarz`. The exercise block
contains no inline hint, but the preceding Parseval proof binds this exact
label and says that its proof is not much different from the finite-dimensional
version. That is source-supplied methodological support, so the gap is
correctly classified as hint-present and solution-absent. The translation
preserves that contextual hint and invents no answer, proof, or solution.
The exact contextual hint components are source raw lines 5266-5268, 123
bytes, SHA-256
`fb1547ee20670fdd5bf3c395ab4e4f8cfd0a2c3266aab28ff1b8653849de9bd6`,
and target raw lines 5280-5282, 132 bytes, SHA-256
`96ad757925a1a87955a010d1f068dbfc0c6811521cda08701ea3a1d79198005c`.

## Deterministic integration build and visual QA

The verified U420 build tree was copied to the isolated
`tmp/r006-u421-build-20260829` directory, retaining the bound complete
Indonesian Volume-I auxiliary label set. An initial native-command invocation
passed the output variable literally and therefore wrote only into an isolated
task-local scratch directory under `translation/ra`; the intended U421 build
and all canonical files were untouched. That exact eight-file scratch tree was
removed, and the build was rerun with the output argument quoted explicitly.

The corrected pass 12, index and glossary generation, and corrected passes 13
and 14 completed successfully. All seven tracked auxiliary products were
byte-identical before and after pass 14. The final non-release integration PDF
is 241 pages / 2,427,760 bytes, SHA-256
`cba29b8d352bc38e545e151ec0ecbdccedb2bd526fce3136230fd8dba689d350`.
The final log is 104,309 bytes, SHA-256
`e74b9c4145cc2ff30197240290b4f382ddaa9883a692db064633a70beaeb6641`;
the final console transcript is 35,349 bytes, SHA-256
`b61e7b8116e9ef22835f8f3cacba0e36f9b842dede23a4e959e00e043d69cfae`.
The log contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U420 exactly in count, location, and width and lie
outside this unit; there are zero overfull vertical boxes.

Physical pages 230 and 231 were rendered at 144 dpi and visually inspected.
The preceding Parseval proof and link to Exercise 11.8.5 remain legible on page
230. The complete Indonesian exercise appears as Exercise 11.8.5 on page 231,
with the full proper name, display, bounds, conjugation, exponents, and
parentheses legible and centered. Line wrapping and hyphenation are natural;
there is no clipping, overlap, crowding, margin breach, or displaced display.
The following still-English Exercise 11.8.6 remains visibly outside U421. The
transient PNG and extracted-text files were removed after inspection. This
integration PDF remains build evidence and does not replace the independently
verified public U397 reader release.

U421 is ready for manifest and O001 admission followed by two deterministic
backend replays. Public U420 source/backend/controls and the U397 reader release
remain unchanged until those gates pass.
