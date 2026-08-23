# R006 complex-series translation receipt — U232 — 2026-08-23

This is a bounded translation-slice receipt, not a whole-volume build claim.
It records the contiguous unit after the U231 continuity proposition.

## Exact boundary

- Source: `source/ra/ch-approximate.tex`, raw lines 197–245 inclusive
- Source normalized-LF bytes/SHA-256: `1906` /
  `9571434b183fe3e01e7132348a96836c321011b3433e96ddeabf8aff984d1c65`
- Target: `translation/ra/ch-approximate.tex`, raw lines 195–240 inclusive
- Target normalized-LF bytes/SHA-256: `1993` /
  `c2be5901e701810c6f4df2c376a23beed5d43b78b655da19c756ac82fe27f668`
- Full target file: `180356` bytes, SHA-256
  `7c648af03da7fe28655c675ee0bba9cc7cf51d481ebdf613c97940cce5fbf6c0`

The unit covers convergence in `\C` and `\R^2`, definitions of complex-series,
absolute, and Cauchy convergence, both propositions, and the transfer of real
convergence tests to the modulus series. It ends before the source subsection
`Complex-valued functions` (source line 246; target line 242).

## Translation and structural QA

- 14 inline mathematical payloads are ordered-identical.
- 10 environment-boundary tokens are ordered-identical.
- Labels `prop:cachysercomplex` and `prop:absconvmeansconv` are preserved.
- Three index commands and 50 command names preserve topology; one literal
  backslash-space is preserved; each slice has 34 opening and 34 closing
  braces.
- Reader-facing English residue: `0`; mojibake: `0`.
- No mathematical/content defect was found.

The source identifier `prop:cachysercomplex` is a high-confidence spelling typo
for “Cauchy” and is referenced later. It is preserved verbatim for compatibility
and recorded as `LEBL-ID-ADV-0223`; no source mutation or author contact was
made.

The edition/repository provenance is explicit: **OpenAI Codex gpt-5.6-sol,
Ultra**, acting on the user's instruction. Jiří Lebl remains the source author;
all source and human-contributor credits are preserved.

## Next cursor

Continue at `\subsection{Complex-valued functions}` immediately after source
raw line 245 (source line 246; target line 242). A full converter/TeX/PDF gate
remains deferred to a meaningful chapter boundary.
