# R006 piecewise-smooth Fourier-convergence exercise - U419

Status: **PASS**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.piecewise-smooth-convergence`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5324-5329,
  six LF-terminated lines / 251 bytes, SHA-256
  `506975f495f979aad4477024a78bcdfb4b8d756121017d6505222badd0105dc0`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5338-5343,
  six LF-terminated lines / 329 bytes, SHA-256
  `509ed8952c0b8c18a114602408de6c3650f75b944c06f5ab93f644799e283b4b`.
- Full target after admission: 197,868 bytes, SHA-256
  `f8c15d5162e33b13ab6cf96b6461fb90cab3d903e34eee425d75f206eb56ddf1`.
- The exact next untranslated boundary is the labeled continuous-periodic
  approximation exercise at source raw line 5331 / target raw line 5345. No
  prose from that exercise is included.

The unit is one complete exercise. It asks for the already stated local
piecewise-smooth Fourier-convergence corollary and retains the source hint to
use the preceding exercise.

## Mathematical and source-correction QA

The referenced `\corref{cor:fourierpiecewisesmooth}` explicitly assumes that
`f` is globally Riemann integrable on `[-pi,pi]`, in addition to being
continuous and piecewise smooth near the evaluation point. The exercise calls
its restatement “that is” but omits that global integrability hypothesis and
never binds its unnamed periodic function to the `f` used in the conclusion.
Without global integrability the chapter's Riemann-defined Fourier
coefficients, hence `s_N(f;x)`, need not be defined.

High-confidence event `LEBL-ID-ADV-0268` records the source-backed repair. The
Indonesian derivative names the function `f` and restores exactly the
referenced corollary's Riemann-integrability assumption on `[-pi,pi]`. It does
not change the periodicity, local continuity/piecewise-smoothness condition,
convergence formula, reference, or hint.

The mathematical implication is sound. On the finite local smooth partition,
each continuously differentiable restriction has bounded derivative. Together
with continuity across the partition points, summing the resulting interval
bounds gives a local Lipschitz estimate at the evaluation point; the preceding
exercise's localization argument then yields the displayed convergence.

Automated comparison confirms that all three original ordered inline-math
payloads (`2\pi`, `x`, and the complete limit equality) occur byte-exactly and
in order in the target. The declared repair adds only the binding `$f$` and
the source-backed interval `$[-\pi,\pi]$`. The original eight-command stream
is an ordered subsequence of the target ten-command stream; the two added
commands are the two `\pi` tokens in the restored interval. Both environment
events and all four opening plus four closing braces are exact. Dollar
delimiters increase from six to ten solely for the two declared additions.
There are no labels, displays, comments, footnotes, citations, or assets.

## Indonesian-language, terminology, and O001 QA

Independent language review passed the reader wording. It reuses admitted
`LEBL-TERM-0791`, `continuous piecewise smooth` -> `kontinu dan mulus
sepotong-sepotong`, as well as `terintegralkan secara Riemann`, `periodik`, and
the established `Petunjuk` register. No new logical terminology row is needed.

`LEBL-O001-R006-0024` maps the unlabeled exercise to
`ra.v2.fourier-series.exercise.piecewise-smooth-convergence`. The source has a
hint but no solution. The translation preserves that hint and invents no
answer, proof, or solution.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in the fresh directory
`tmp/r006-u419-build-20260828` with the bound complete Indonesian Volume-I
auxiliary label set (SHA-256
`8696b0f4e80ddfe0093da26955f868304892bf081eb01c04d21feedd1815d5c2`).
Seven TeX passes were run, with index and glossary regeneration on the first
three. All seven tracked auxiliary products were byte-identical before and
after pass seven. The non-release integration PDF is 241 pages / 2,427,627
bytes, SHA-256
`0461751d24fc7fa6cc2b2c2dfa547a972c11e398aaae2ab67db0dbe593e97bd2`.
The final log is 104,309 bytes, SHA-256
`8219ffcd28b9bad6b6cd9754ce9c24f6d7a9de38c9475459f2d47f41ca493c9c`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U418 exactly in count, location, and width and all lie
outside U419; there are zero overfull vertical boxes.

Physical pages 230 and 231 were rendered at 144 dpi and visually inspected.
The complete Indonesian exercise is legible on page 230, aligns with the
exercise block, wraps naturally, and has no clipping, overlap, or margin
breach. Page 231 preserves the centered Weierstrass figure and confirms that
the following still-English exercise remains outside U419. Transient render
PNGs were removed after inspection. This integration PDF remains build
evidence and does not replace the verified U397 reader release.

U419 is ready for manifest admission and two deterministic backend replays.
The public U418 source/backend and controls checkpoint and U397 reader release
remain unchanged until those gates pass.
