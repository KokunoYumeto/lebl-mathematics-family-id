# R006 decaying-sine-series and forced-ODE exercise — U423

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.decaying-sine-series-forced-ode`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5358–5385,
  28 LF-terminated lines / 774 bytes, SHA-256
  `9d34b8d673c7983231eca78947006519e71b5bdfb65a1f37672dcc5c0e602ded`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5372–5399,
  28 LF-terminated lines / 873 bytes, SHA-256
  `fe3e35c58f96b3e14c29e23a820479792e524545e581e01aac11989820af2934`.
- Full target after translation: 198,066 bytes, SHA-256
  `434495045cbfd83b0d0b0ff265339d94710b7a8eea592f9f010b743108a5bab4`.
- The next source boundary begins after raw line 5385; no later prose or
  formula is included in this unit.

The admitted unit is one complete unlabeled exercise with three enumerated
subparts: continuity of a decaying sine series, a formal forced-ODE Fourier
coefficient calculation, and analytic justification of the resulting solution.

## Mathematical, structural, and source QA

The source statement is mathematically coherent. Since `alpha > 1`, the bound
on `a_n` gives absolute and uniform convergence of the sine series by the
Weierstrass M-test, hence continuity of `g`. Formal coefficient comparison gives
`(2-n^2)b_n=a_n`, so `b_n=a_n/(2-n^2)` for every integer `n >= 1`; there is no
integer resonance because `n^2` is never 2. The resulting coefficients satisfy
`b_n=O(n^(-alpha-2))`, and the twice-differentiated coefficients are
`n^2 b_n=O(n^(-alpha))`, which is summable. Uniform convergence of the series
and its first two differentiated series therefore yields a twice continuously
differentiable `y` that satisfies the displayed equation. The conventional
omission of an explicit `C > 0` is harmless: the displayed bound itself forces
the relevant nonnegative bound whenever such a sequence exists. No source
correction or adverse-ledger event is required.

The target preserves all 28 source lines and changes reader-facing prose only.
The ordered TeX command stream and all environment boundaries are identical;
the three display payloads and seven inline-math payloads are byte-identical.
There are 17 opening and 17 closing braces and 14 dollar delimiters on each
side, with `pagebreak[3]`, `enumerate[a)]`, both `item` markers, and all display
and exercise topology retained. The exercise has no label, reference, comment,
footnote, citation, or asset.

## Indonesian-language, terminology, and O001 QA

The wording is natural and faithful: `barisan bilangan real`, `kontinu`,
`mendiferensialkan deret tersebut suku demi suku`, `persamaan diferensial`,
`konvergensi`, and `diferensiabel secara kontinu hingga orde dua` follow the
existing shared register (including LEBL-TERM-0480 and LEBL-TERM-0630). The new
admitted glossary row LEBL-TERM-0797 maps `formal solution` to `solusi formal`,
with an explicit note that it is only a coefficientwise candidate until
convergence and termwise differentiation are justified. An independent
mathematical, Indonesian-language, and structural audit found no refinement
needed.

`LEBL-O001-R006-0028` maps this exercise to O001. The source supplies no
explicit hint and no solution. The a→b→c progression is intrinsic exercise
scaffolding, not a detachable hint; nearby coefficient-decay exposition is
context, not a source-linked hint. The translation invents neither an answer,
proof, nor support.

## Deterministic integration build and visual QA

The complete-volume integration build was run in the isolated directory
`tmp/r006-u423-build-20260829` with `SOURCE_DATE_EPOCH=1787961600` and
`TZ=UTC`. The converter exited 0 (1,534,030-byte console,
SHA-256 `4d2ba4f419a28e2382f211e5c1097f10958920d682585bb6315ac71948773689`).
Nine pdflatex/index/glossary passes plus an independent pass 10 all exited 0;
the pass-8/9/10 pdflatex consoles are identical (34,834 bytes, SHA-256
`15746ee56be79b32709407a1a175db1d50e2830fbfbc55713bdb35c8650751d7`). The
final reader is 241 pages / 2,427,666 bytes, SHA-256
`fd0830a19e94eaed0b53106adac197bec3665daf3e7a0b408a4018ac155ea504`; the
converged log is 103,379 bytes, SHA-256
`a4b7ae748553222e118b31ed3ffb0bd559067c280a5ad43934d4c6dd8c59a622`.
The final auxiliary products (`aux`, `toc`, `out`, `idx`, `glo`, `ind`, `gls`)
were byte-identical between passes 9 and 10. There were zero fatal/LaTeX,
undefined-reference, missing-character, or unresolved-link errors. Inherited
layout notices comprise 15 overfull hboxes, 0 overfull vboxes, 3 underfull
hboxes, and 2 underfull vboxes; there are five package-warning lines and one
final rerun-file-check notice. No new clipping or overflow occurs at this unit.
The PDF has 98 embedded font rows, and `pdftotext` succeeds for all pages.

Pages 230--233 were rendered at 144 dpi with `pdftoppm` and inspected. All
four pages are centered and readable with no clipping, overlap, or margin
breach. Page 231 contains the complete Indonesian Latihan 11.8.7, including
the displayed series and all three subparts; page 232 begins the untouched
English Latihan 11.8.8 exactly at the admitted boundary. Render hashes are:
page 230 `46b844a97f9c5c8ef88a28680e1d66c774f680cadfecea670432120ede548d07`,
231 `76c50c1f13566246d07de3c52f7033cfa458d9bb9a66b637b8fae1f85cc7ecfd`,
232 `072412b4da94e9bc797bca7d13cf31551029465e9454ee2c473ce8134c769abd`, and
233 `f78e3fc4fa8dd1016fefa526abfd99ef4c46c01d6fafaf47ce645918d9e19f51`.
The build and visual gates therefore pass for U423; the reader release remains
the separately preserved U397 public artifact until a reader-cut release is
explicitly bounded.
