# R006 complex-plane exercises translation receipt — U234 — 2026-08-23

This is a bounded translation-slice receipt, not a whole-volume build claim.
It records the complete Exercises subsection following the complex-valued
functions unit.

## Exact boundary

- Source: `source/ra/ch-approximate.tex`, raw lines 283–359 inclusive
- Source normalized-LF bytes/SHA-256: `2480` /
  `f6b4dc6ca25c5244295e56c03ec70012d0f1233b725cbcede0e27241f680d084`
- Target: `translation/ra/ch-approximate.tex`, raw lines 278–354 inclusive
- Target normalized-LF bytes/SHA-256: `2626` /
  `ef853c1fc02fb9c40bb4ff806c9b7075bcddca1a807906ebe8da2ea5c5d33aa1`
- Full target file: `180669` bytes, SHA-256
  `35f14935f0f359f7be0f3974c6b67e9ee8cbd9a3f5327b0dc1bc829366205f00`

The unit translates all eight exercises: the field and modulus checks, the
continuity/Cauchy/absolute-convergence propositions, the matrix model of
complex numbers, Bolzano–Weierstrass, two mean-value counterexamples, and the
complex integral counterexample. It ends before `\sectionnewpage` (source
line 359; target line 359; next section begins at source line 360).

## Translation and structural QA

- 34 inline mathematical payloads are ordered-identical.
- 28 environment-boundary tokens and three proposition references preserve
  their topology.
- 77 command names are ordered-identical; two literal backslash-space tokens
  are preserved; each slice has 44 opening and 44 closing braces.
- Reader-facing English residue: `0`; mojibake: `0`.
- No glossary or index hooks occur in this unit.

Natural id-ID choices include `lapangan`, `nilai eigen`, `barisan kompleks`,
`subbarisan`, `teorema nilai rata-rata`, and `fungsi bernilai kompleks`. The
edition and repository identify the runtime as **OpenAI Codex gpt-5.6-sol,
Ultra**, acting on the user's instruction. Jiří Lebl remains the source
author; all source and human-contributor credits are preserved.

## Source note

The matrix exercise item (b) has the source prose “is the same multiplying”
(raw line 311; the sentence continues at line 312), which is missing “as”.
The Indonesian derivative preserves the intended mathematical meaning without
mutating the frozen source. This is recorded as `LEBL-ID-ADV-0224` for the
single deduplicated upstream disposition after all three assigned books are
complete; no author or maintainer was contacted.

## Next cursor

Continue at the next section after the `\sectionnewpage` boundary (source raw
line 360; target raw line 359), beginning `Swapping limits`. A full
converter/TeX/PDF gate remains deferred to a meaningful chapter boundary.
