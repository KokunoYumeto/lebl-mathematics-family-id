# R006 local Fourier-convergence exercise - U418

Status: **PASS**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID: `ra.v2.fourier-series.exercises.local-fourier-convergence`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5317-5322,
  six LF-terminated lines / 285 bytes, SHA-256
  `326b0d3cc399e26a38d4b50c95af7e0d2ff98f7f7beb54946c6207925ba9033b`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5331-5336,
  six LF-terminated lines / 339 bytes, SHA-256
  `7e292ea7ee9d21d332364b99120084d671c8c40f42279289157d70a8782f70db`.
- Full target after admission: 197,790 bytes, SHA-256
  `e97e19de0a3004bc83910e7245aea3a3ba728029f56a1544843e49944e3a8a65`.
- The exact next untranslated boundary is the piecewise-smooth convergence
  exercise at source raw line 5324 / target raw line 5338. No prose from that
  exercise is included.

The unit is one complete exercise. It assumes a Riemann-integrable
`2pi`-periodic function that is continuously differentiable on an open
interval and asks for convergence of its symmetric Fourier partial sums at
every point of that interval.

## Mathematical and source-correction QA

The mathematical claim is valid. For each point in the open interval, choose
a closed subinterval around it that remains inside the given interval.
Continuity of the derivative makes the derivative bounded on that compact
subinterval, so the mean value theorem gives the local Lipschitz condition
used by the preceding Fourier localization result. No extra hypothesis is
introduced into the reader text.

The source hypothesis is grammatically incomplete: `Suppose that a ...
function that is ... and such that f is ...` has no main predicate and does
not explicitly bind the initially described function to `f`. High-confidence
event `LEBL-ID-ADV-0267` records the repair. The Indonesian derivative says
that the described function is denoted by `f` and then states the same two
hypotheses in a complete sentence. This changes no mathematical condition,
conclusion, formula, or exercise task.

Automated comparison gives exact equality for all six ordered inline-math
payloads, all ten ordered TeX control sequences, both environment events, all
twelve dollar delimiters, and three opening plus three closing braces. The
topology is exactly one `exercise`. There are no labels, references, display
environments, comments, footnotes, citations, or assets.

## Indonesian-language, terminology, and O001 QA

Independent language review passed the reader wording. The unit reuses
admitted terminology: `interval terbuka`, `diferensiabel secara kontinu`,
`terintegralkan secara Riemann`, `periodik`, and the established semantics of
`s_N` as a symmetric partial sum. No new logical terminology row is needed.

`LEBL-O001-R006-0023` maps the unlabeled exercise to
`ra.v2.fourier-series.exercise.local-fourier-convergence`. The source contains
neither hint nor solution, and the translation invents neither.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in the fresh directory
`tmp/r006-u418-build-20260828` with the bound complete Indonesian Volume-I
auxiliary label set. Six passes were run, with index and glossary regeneration
on the first three; all seven tracked auxiliary products were byte-identical
between passes five and six. The non-release integration PDF is 241 pages /
2,427,570 bytes, SHA-256
`62a74a72b96798d3c942e5ab36495b9df2ad1ec457de37a6309f8ce6e065fecf`.
The final log is 104,268 bytes, SHA-256
`9440f4acc40195c9e327687b35abd8718416fc483d635484170749df71f966cb`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U417 exactly in count, location, and width and all lie
outside U418; there are zero overfull vertical boxes.

Physical pages 230 and 231 were rendered at 144 dpi and visually inspected.
The complete Indonesian exercise is legible on page 230, aligns with the
exercise block, wraps naturally, and has no clipping, overlap, or margin
breach. The following still-English exercise remains visibly outside U418.
Page 231 preserves the centered Weierstrass figure and confirms the following
exercise boundary. Transient render PNGs were removed after inspection. This
integration PDF remains build evidence and does not replace the verified U397
reader release.

U418 is ready for manifest admission and two deterministic backend replays.
The public U417 source/backend and controls checkpoint and U397 reader release
remain unchanged until those gates pass.
