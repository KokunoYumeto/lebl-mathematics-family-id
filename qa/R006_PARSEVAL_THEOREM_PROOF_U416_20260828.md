# R006 Parseval theorem proof — U416

Status: **PASS**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID: `ra.v2.fourier-series.parseval.proof`
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5187–5288,
  102 LF-terminated lines / 2,424 bytes, SHA-256
  `e9ab2313154502ee7728b87f020d9dc774d76d18bf705bd1e755fa20b8d0e87c`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5201–5302,
  102 LF-terminated lines / 2,578 bytes, SHA-256
  `91f8ed576a7fc556efca465c34f094a702bfd5dcca02ba7cd6fd88953e808034`.
- Full target after admission: 197,633 bytes, SHA-256
  `9854b5dbd54879fe072ec502f4062d5b3dbe3220978daa681f87aa07ba7ec08c`.
- The exact next untranslated boundary is the Exercises subsection at source
  raw line 5290 / target raw line 5304. No exercise prose was included.

## Mathematical and structural QA

The proof preserves its complete seven-step argument:

1. approximate `f` in `L^2` by a continuous periodic `h`;
2. approximate `h` uniformly by a trigonometric polynomial `P`;
3. use best approximation and the Bessel contraction bound;
4. apply the triangle inequality to obtain the `3\epsilon` estimate;
5. compute the finite inner product as the coefficient sum;
6. apply Cauchy--Schwarz and the first statement to pass to the limit;
7. set `g=f` to obtain the final Parseval identity.

Automated source/target comparison gives exact equality for all 135 ordered
TeX control sequences, all 20 environment events, all 19 inline-math spans,
80 opening and 80 closing braces, and 38 dollar signs. The topology contains
one `proof`, eight `equation*` environments, and one nested `split`. Both
commented inequality lines and all six references are unchanged:
`exercise:contL2close`, `thm:SWcomplex`, `exercise:trigpolydense`,
`thm:l2bestapprox`, `exercise:L2triangleineq`, and
`exercise:L2cauchyschwarz`.

Conjugation, finite and bilateral bounds, normalized versus unnormalized
integrals, square roots, exponents, `s_N(h-f)`, the `3\epsilon` estimate, and
the final substitution `g=f` are exact. Independent mathematical review found
the argument valid. The source omits `dx` in eight integrals in its
Cauchy--Schwarz display and application; this is consistent shorthand, not a
high-confidence defect, so the target preserves it and no adverse event is
added.

## Indonesian-language QA

The translation uses the admitted forms `polinom trigonometri`, `derajat
polinom`, `aproksimasi terbaik`, `ketaksamaan Bessel`, `ketaksamaan segitiga`,
`ketaksamaan Cauchy--Schwarz`, and `berdimensi hingga`. The proof's connective
logic is explicit and natural: `Berdasarkan`, `Oleh karena itu`, `Dengan
demikian`, `Selanjutnya`, and `Artinya`. No new logical terminology row is
needed because every technical term is already represented in the live
ledger. No exercise, asset, correction, or O001 solution-gap record is added.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in the fresh directory
`tmp/r006-u416-build-20260828` with the bound complete Indonesian Volume-I
auxiliary label set. After index and glossary generation and converged final
passes, the non-release integration PDF is 241 pages / 2,428,003 bytes,
SHA-256
`e2cfc54203c523b77415a2754d5e2f67a02fb039ed760ad11993799ea524816f`.
The final log is 104,268 bytes, SHA-256
`42933a776f5565fcbf89fac0eca966709235ef64fa77d4f3e96043fbfad58137`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. Its 15 overfull
horizontal boxes have exactly the same locations and widths as U415 and all
lie outside U416; there are zero overfull vertical boxes.

Physical pages 229–231 were rendered at 144 dpi and visually inspected. The
proof begins cleanly under the theorem on page 229, continues without clipping
on page 230, and closes before the Exercises heading. Every display is centered
and readable, links and conjugation bars remain visible, line and page breaks
are sound, and the page block fills the usable page width. The English exercise
prose beginning after the exact U416 boundary remains intentionally untouched.
Page 231 confirms the inherited exercise figure and following source prose are
unaffected. The render PNGs were removed after inspection. The integration PDF
remains transient build evidence and does not replace the verified U397 reader.

U416 is ready for two deterministic backend replays. The public U415
source/backend and controls and the U397 reader release remain unchanged until
those backend and publication gates pass.
