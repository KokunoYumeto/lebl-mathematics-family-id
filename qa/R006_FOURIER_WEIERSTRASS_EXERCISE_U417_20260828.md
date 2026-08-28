# R006 Fourier-series Weierstrass exercise — U417

Status: **PASS**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID: `ra.v2.fourier-series.exercises.weierstrass-function`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5290–5315,
  26 LF-terminated lines / 1,022 bytes, SHA-256
  `e9b61b524ec2c512c771e2622de5886c9b091c71c59018d901a0d6b12a7f62e3`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5304–5329,
  26 LF-terminated lines / 1,125 bytes, SHA-256
  `624bbea5c380a5a7519651fc895cbc73e53af6f0054b8a0e1d28a100c0a9422e`.
- Full target after admission: 197,736 bytes, SHA-256
  `5556d4a54f83b736e42b72a9a273238913673e0cedf6fb43755aee4e09576696`.
- The exact next untranslated boundary is the local Fourier-convergence
  exercise at source raw line 5317 / target raw line 5331. No prose from that
  exercise was included.

The unit contains the Exercises subsection heading and the complete labeled
first exercise: series, convergence task, nowhere-differentiability remark,
Hardy citation, coefficient observation, figure reference, accessible figure
description, caption, and environment close.

## Mathematical and source-correction QA

The displayed series

`sum_(k=1)^infinity (1/2^k) sin(2^k x)`

is unchanged. The required task remains exactly to prove uniform and absolute
convergence to a continuous function; the source explicitly says that proving
nowhere differentiability is not required.

One high-confidence source convention error is repaired transparently as
`LEBL-ID-ADV-0266`. The chapter defines complex Fourier coefficients by
`c_m=(1/(2pi)) integral f(x)e^(-imx) dx`. For the summand
`(1/2^k)sin(2^k x)` and `n=2^k`, the positive complex coefficient is
`1/(2in)` and the negative one is `-1/(2in)`. The value `1/n` stated in the
source is the positive-frequency sine coefficient `b_n`, not the complex
Fourier coefficient `c_n`. The Indonesian derivative therefore says
`koefisien sinus ke-n` while preserving the value, decay observation, and
every formula. This is a local terminology correction, not an alteration of
the exercise's mathematics.

Automated source/target comparison gives exact equality for all 29 ordered
TeX control sequences, all six environment events, all five inline-math
spans, all ten dollar delimiters, both percent tokens, and 26 opening plus 26
closing braces. The topology is one `exercise`, one `equation*`, and one
`myfigureht`. The label `exercise:fsweierser`, figure reference and label
`fig:fourierserweier`, and asset base `fourierserweier` are exact.

## Indonesian-language, terminology, and O001 QA

The reader text uses natural admitted forms: `konvergen secara seragam dan
mutlak ke suatu fungsi kontinu`, `tidak diferensiabel di mana pun`, and
`koefisien sinus`. New logical term `LEBL-TERM-0796` binds
`nowhere differentiable` to `tidak diferensiabel di mana pun`, consistent
with the existing `diferensiabel` terminology family; the passive draft form
`tidak terdiferensialkan di mana pun` is explicitly rejected.

`LEBL-O001-R006-0022` maps `exercise:fsweierser` to
`ra.v2.fourier-series.exercise.weierstrass-nowhere-differentiable-series`.
The source contains neither hint nor solution. The gap record states that the
nowhere-differentiability assertion is excluded from the required proof, and
the translation invents no hint, answer, or solution.

The existing localized reader and build-provenance assets are reused
byte-for-byte:

- `translation/ra/figures/fourierserweier.pdf`: 13,966 bytes, SHA-256
  `ec93b5a43a67fb602737a40c9da781130f7eef92c699615dea2da73c058c74ff`;
- `translation/ra/figures/fourierserweier.xp`: 699 bytes, SHA-256
  `10addc815b37a725f655784be736fa74fb0e6f0bc5162a4fc2d41850121b511a`.

No isolated asset record is manufactured because the current generic R006
builder does not admit this legacy figure class; the exact manifest slice,
this receipt, and the figure hash bind it without changing backend semantics.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in the fresh directory
`tmp/r006-u417-build-20260828` with the bound complete Indonesian Volume-I
auxiliary label set. After index and glossary generation and three converged
final passes, the non-release integration PDF is 241 pages / 2,427,593 bytes,
SHA-256
`9323a0990fd18440566557aad94d8b1a7e016c941add2522f39042020c0cd34d`.
The final log is 104,309 bytes, SHA-256
`0765d1ba25c7edc04869c4127eed0001502fecf21761764ea400b59f0dd60e57`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes match U416 exactly in count, location, and width and all lie
outside U417; there are zero overfull vertical boxes.

Physical pages 230–232 were rendered at 144 dpi and visually inspected. The
exercise begins cleanly after the Parseval proof on page 230, its formula is
centered, the footnote is complete and readable, and no line is clipped. The
figure on page 231 is centered, sharp, correctly labeled, and fills its natural
content width without distortion. Page 232 confirms that later untranslated
exercise prose remains outside U417. The transient render PNGs were removed
after inspection. This integration PDF remains build evidence and does not
replace the verified U397 reader release.

U417 is ready for two deterministic backend replays. The public U416
source/backend checkpoint and U397 reader release remain unchanged until the
backend and publication gates pass.
