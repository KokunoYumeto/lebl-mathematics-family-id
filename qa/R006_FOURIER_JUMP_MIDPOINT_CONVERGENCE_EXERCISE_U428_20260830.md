# R006 Fourier jump-midpoint convergence exercise — U428

Status: **PASS**  
Date: 2026-08-30  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.symmetric-partial-sums-jump-one-sided-limit-average`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5428–5458,
  31 LF-terminated lines / 910 bytes, SHA-256
  `322b590d17072290cb02092c8b14e840523f24bb6f02560a8de4e75b5ad95c2f`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5442–5472,
  31 LF-terminated lines / 1,007 bytes, SHA-256
  `e39ce52a989ffee0660f9ff67b7897ac5d4e384fb7155caed2920b3c7d3a47d8`.
- Full target after translation: 198,306 bytes, SHA-256
  `0ea422821552511f443ac628af80d41020fa1cc99d879bbd302f1bdcc75ee90e`.
- The exact next untranslated exercise occupies source raw lines 5460–5473 /
  target raw lines 5474–5487 and remains untouched.

The admitted unit is one complete two-part exercise. Part (a) asks for the
value of symmetric Fourier partial sums at the jump of a periodic step
function. Part (b) states the corresponding average-of-one-sided-limits result
under local one-sided continuously differentiable representatives.

## Mathematical and source QA

The statement is coherent. Changing the two isolated point values in part (a)
does not change the Riemann integrals defining the Fourier coefficients, and
the midpoint value at the jump is `(0+1)/2`. Part (b) is the standard local
Fourier convergence conclusion: global Riemann integrability supplies the
coefficients, while the one-sided `C^1` representatives provide the local
regularity needed for convergence to `(g(x)+h(x))/2`, equivalently the average
of the two one-sided limits. The translation does not add a proof, answer, or
stronger convergence claim. No source correction or adverse-ledger event is
warranted.

Independent structural comparison found the same ordered 61 TeX commands,
six ordered environment events, 21 exact inline-math payloads, the exact
display payload, 17 opening and 17 closing braces, 42 dollar delimiters, and
two `\item` events in source and target. There are no labels, references,
citations, comments, footnotes, figures, or hidden solution assets in the unit.

## Indonesian-language, terminology, manifest, and O001 QA

The wording is natural formal Indonesian. It reuses `periodik`
(LEBL-TERM-0663), `terintegralkan secara Riemann` (LEBL-TERM-0272),
`diferensiabel secara kontinu` (LEBL-TERM-0247), `limit sepihak`
(LEBL-TERM-0192), `jumlah parsial simetris` (LEBL-TERM-0768), and the
established jump-discontinuity concept LEBL-TERM-0771. No new terminology row
is needed. A bounded independent translation review agreed with the complete
31-line Indonesian body, stable unit, single-unit topology, and term reuse.

The source supplies no hint and no solution for either part. One O001 row,
`LEBL-O001-R006-0033`, covers the complete two-part exercise without
artificially splitting its semantic identity and without inventing an answer,
proof, or explanatory support.

The deterministic U428 backend has 4,015 records and 856 embedded expressions.
Its two fresh 27-file / 18,151,570-byte trees are byte-identical; their
3,292-byte ordinal-POSIX inventory has SHA-256
`77e1b2128513b78305740126ff974949efe6e220c720b66e65b8a09521802275`.
Schema, referential-integrity, 428 manifest-binding, 370 direct-component, and
all 15 lossless CSV round-trip checks pass.

The fixed-epoch complete-volume integration build passes at 241 pages /
2,427,826 bytes, PDF SHA-256
`b566883b66b32b84edd186a97ae643d7371b4474c3b543b6a6ed0df7f128329f`.
Passes 3 and 4 after index and glossary regeneration are byte-identical across
the PDF and seven auxiliary products. The log is 103,420 bytes, SHA-256
`193a709b44af014894e4aafbf541f510ae16e6847509fcc8043ffdedf89500e3`;
it has zero fatal, LaTeX, undefined-control, missing-character,
undefined-reference, multiply-defined-label, invalid-link, or bad-outline
errors. Text extraction has zero replacement characters; all 687 links have
valid destinations, all 33 outline entries have valid pages, and all 98 listed
font objects are embedded. Rendered pages 231–233 pass visual QA: page 232 is
centered and contains complete Indonesian U428 followed by the exact English
U429 boundary; pages 231 and 233 remain clean and unclipped.

## Recovery

Continue with the complete next exercise at source raw lines 5460–5473 /
target raw lines 5474–5487. Preserve the public U427 source and controls
commits, the U397 reader release, and the R007/R008 cursors. Carry the finalized
local U427 receipt with the next substantive GitHub source/backend checkpoint.
No author contact or upstream issue is allowed before all three assigned books
are complete.
