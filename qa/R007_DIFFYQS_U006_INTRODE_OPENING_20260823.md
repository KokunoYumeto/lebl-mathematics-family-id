# R007 Diffy Qs — U006 bounded translation receipt

Status: translated locally; not published; no author contact.

## Bound

- Source: `source/diffyqs-v6.11/ch-intro.tex`, raw lines 317–355, from `\\sectionnewpage` and `\\section{Introduction to differential equations}` through the opening `Differential equations` subsection and its cooling-law example.
- Target: `translation/diffyqs/ch-intro.tex`, raw lines 305–340 (translation reflow changes prose line count).
- Source unit UTF-8 bytes: 1,694.
- Source unit SHA-256: `d700a087a9b6c27efd4897cfd01bfefc4f77cf73d718da6b4670b782c6c4ae2a`.
- Target unit UTF-8 bytes: 1,713.
- Target unit SHA-256: `726fe8ba2ec0354c08242fc2b43865969c74b9c325603682db333a7e2bff5acb`.
- Target file after U001–U006: 12,826 bytes; SHA-256 `c600d627b86ffde011d9e3e90892be5cde61c5f0c8bf08363fa0598e62849a30`.

## QA

- TeX control sequences: 24 / 24; command multiset identical.
- Command counts: `\\sectionnewpage` 1, `\\section` 1, `\\sectionnotes` 1, `\\subsection` 1, `\\EPref`/`\\BDref` 1/1, `\\cite` 2, `\\begin`/`\\end` 1/1, `\\label` 2, `\\eqref` 1, `\\frac` 1, `\\cos` 1, `\\emph` 4, `\\myindex` 4, `\\S` 1.
- Braces: 22 opening and 22 closing in each unit.
- Environment boundaries: 2 / 2.
- Inline math markers: 8 / 8; ordered payloads identical: `x`, `t`, `x`, `t`.
- Equation payload preserved exactly: `\\frac{dx}{dt} + x = 2 \\cos t .` (1 / 1).
- Labels retained: `introde:section`, `eq1`; mojibake scan: 0 hits.
- Reader-facing prose and index terms were translated into natural Indonesian; mathematical symbols, macros, citation keys, and equation content were unchanged.

## Cursor and provenance

- Next source cursor: raw line 356, `\\subsection{Solutions of differential equations}`.
- Next target action: append the Indonesian solutions subsection after target line 341's terminal blank line.
- Translation tooling provenance: `OpenAI Codex gpt-5.6-sol, Ultra`.
- This is a local production receipt only; no upstream issue or author communication was initiated.
