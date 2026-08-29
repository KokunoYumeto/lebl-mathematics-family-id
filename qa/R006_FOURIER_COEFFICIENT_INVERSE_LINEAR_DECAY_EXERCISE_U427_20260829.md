# R006 Fourier-coefficient inverse-linear decay exercise — U427

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.integral-representation-fourier-coefficient-inverse-linear-decay`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5415–5426,
  twelve LF-terminated lines / 397 bytes, SHA-256
  `c1ae7208737060a162f6fd9b6062a3239689f2a42dcd2ad36f223351ef2ac7a0`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5429–5440,
  twelve LF-terminated lines / 464 bytes, SHA-256
  `25e7b22f29911161b05f50d2f5d6436e38ab3d683323bf08e421217b9bae3d68`.
- Full target after translation: 198,209 bytes, SHA-256
  `39bf28512e7f98a00b2cbdbc4fb7824794168c7ceca041052a469d36958d407e`.
- The exact next untranslated boundary follows blank source line 5427 / target
  line 5441. The next complete two-part exercise occupies source raw lines
  5428–5458 / target raw lines 5442–5472 and remains untouched.

The admitted unit is the complete labeled `exercise:fsdiffmindecay` exercise.
It assumes a periodic integral representation and asks for the inverse-linear
bound on every nonzero complex Fourier coefficient.

## Mathematical and source QA

The statement is coherent. The integral representation makes `f` absolutely
continuous on compact intervals with integrable derivative `g`. For nonzero
integer `n`, integration by parts in the Fourier-coefficient integral produces
a boundary term that vanishes by `2\pi`-periodicity; the remaining integral is
bounded by a constant times `1/|n|`. This supports precisely the stated
existence of `C>0`. The tilde remains the source's formal Fourier-series
relation and is not interpreted as pointwise, uniform, or `L^2` convergence.
No source correction or adverse-ledger event is warranted.

Independent structural comparison found the same ordered fifteen TeX
control-word commands (plus the literal `\,` spacing control), four environment
events, seven exact inline-math payloads, the exact display payload, eleven
opening and eleven closing braces, fourteen dollar delimiters, and the exact
label in source and target. There are no references, citations, comments,
footnotes, figures, or hidden solution assets.

## Indonesian-language, terminology, manifest, and O001 QA

The wording is natural formal Indonesian. It reuses `fungsi` (LEBL-TERM-0029),
`periodik` (LEBL-TERM-0663), and `terintegralkan secara Riemann`
(LEBL-TERM-0272); the context also binds the established `koefisien Fourier`
(LEBL-TERM-0767) and `deret formal` (LEBL-TERM-0770). No new terminology row is
needed. An independent owner audit passed the body and recommended the clearer
metadata title `peluruhan koefisien Fourier dengan laju 1/|n|`, which is now
used in the manifest.

The source supplies no hint and no solution. O001 gap
`LEBL-O001-R006-0032` records that missing solution without inventing an answer,
proof, or explanatory support. The labeled statement itself is not promoted to
a detachable hint.

The deterministic U427 backend has 4,011 records and 854 embedded expressions.
Its two fresh 27-file / 18,108,960-byte trees are byte-identical; their
3,292-byte ordinal-POSIX inventory has SHA-256
`48132a45901e66eb0216d2df08b5e2ea03d3e6897a48a865dd2446238c6386a1`.
Schema, referential-integrity, 427 manifest-binding, 368 direct-component, and
all 15 lossless CSV round-trip checks pass.

The fixed-epoch complete-volume integration build passes at 241 pages /
2,427,815 bytes, PDF SHA-256
`3161b210f7654b1ae6abb7b9c2c8387ebdf9af2e6a4164eef9029aa0236864a2`.
The final two passes are byte-identical across the PDF and seven auxiliary
products. The log has zero fatal, LaTeX, undefined-control, missing-character,
undefined-reference, multiply-defined-label, invalid-link, or bad-outline
errors. Text extraction has zero replacement characters; 687 links and all
98 listed font objects are embedded. Rendered pages 231–233 pass visual QA:
page 232 is centered and contains complete Indonesian U427 followed by the
exact English U428 boundary.

## Recovery

Continue with the complete two-part exercise at source raw lines 5428–5458 /
target raw lines 5442–5472. Preserve the now-public U426 source and controls
commits, the U397 reader release, and the R007/R008 cursors. Carry the finalized
local U426 receipt with the next substantive GitHub source/backend checkpoint.
No author contact or upstream issue is allowed before all three assigned books
are complete.
