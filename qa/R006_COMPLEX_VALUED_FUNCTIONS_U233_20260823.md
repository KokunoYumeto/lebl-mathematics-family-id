# R006 complex-valued-functions translation receipt — U233 — 2026-08-23

This is a bounded translation-slice receipt, not a whole-volume build claim.
It records the contiguous definition unit after U232.

## Exact boundary

- Source: `source/ra/ch-approximate.tex`, raw lines 246–280 inclusive
- Source normalized-LF bytes/SHA-256: `1285` /
  `63dde7115463dcdafca3f485895fe387a8f8a8fa7a33f372e3b4d88f449143d8`
- Target: `translation/ra/ch-approximate.tex`, raw lines 242–275 inclusive
- Target normalized-LF bytes/SHA-256: `1452` /
  `f38c8592e5cebe56f0be61815e9746fcf7c7bef754492c767bcf7ba70c8f2b6f`
- Full target file: `180523` bytes, SHA-256
  `8bf815a9e22b52ca236298be9ced84e54fc06b5d5a037954e68408fc897be6fa`

The unit defines complex-valued functions, componentwise Riemann integration,
and componentwise differentiation through the derivative identity. It ends
before the Exercises subsection (source line 283; target line 278).

## Translation and structural QA

- 22 inline mathematical payloads are ordered-identical.
- Four environment-boundary tokens, two index commands, and the glossary hook
  `\glsadd{not:mvder}` preserve their topology.
- 35 command names are ordered-identical; one nonbreaking `~` is preserved; each
  slice has 10 opening and 10 closing braces.
- Reader-facing English residue: `0`; mojibake: `0`.
- No high-confidence source issue was found.

Natural id-ID choices are `fungsi bernilai kompleks`, `fungsi bernilai real`,
`terintegralkan secara Riemann`, `diferensiabel`, and `turunan`. The edition and
repository identify the runtime as **OpenAI Codex gpt-5.6-sol, Ultra**, acting on
the user's instruction. Jiří Lebl remains the source author; all source and
human-contributor credits are preserved.

## Next cursor

Continue at the Exercises subsection after source raw line 280 (the subsection
begins at source line 283; target line 278). A full converter/TeX/PDF gate
remains deferred to a meaningful chapter boundary.
