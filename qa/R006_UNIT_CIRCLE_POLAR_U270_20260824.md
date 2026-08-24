# R006 U270 — unit circle and polar coordinates

Status: **PASS for semantic/backend admission**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2097–2140
  inclusive, 44 LF-serialized lines, 1,377 bytes, SHA-256
  `0ea3bf79ec4becf219dd77923cc2d59b5d6c19e04711660c888c390b1903389e`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2107–2150 inclusive, 44 LF-serialized lines, 1,719 bytes, SHA-256
  `70ed7d0192a0157cdbd03f9c15e3467149af8401a8b6a3c3e992ae576f73af83`.
- The next contiguous unit begins at source raw line 2141 and target raw line
  2151, the complete exercise subsection.
- Full frozen source file: 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target after U270 and U271: 187,510 bytes, SHA-256
  `7efdde57494518efc8f3ac61b868783459245939c77ec41cb66120a3aac999d6`.

## Verification

Owner comparison and two independent final audits pass. Source and target each
contain one subsection, eight ordered environment tokens, four exact displayed
formula payloads, and one localized index hook. Braces and environments are
balanced, and no formula, map, domain, or structural element was lost. The
final Indonesian uses the preferred noun `parametrisasi`, distinguishes the
half-open bijective parametrization from the closed full-turn length
parametrization, and contains no reader-facing English residue.

Three source qualifications are recorded transparently as
`LEBL-ID-ADV-0234` through `LEBL-ID-ADV-0236`: regularity for the arc-length
formula; the half-open/closed endpoint distinction; and the exponent domain in
the polar power identity. Independent mathematical review verified the
piecewise-smooth hypothesis, the two parametrization roles, and the statements
for `n` natural or, when `r>0`, integral. The four displayed formulas remain
unchanged.

The shared terminology ledger admits the reusable section terms through
`LEBL-TERM-0684`. It has 684 unique rows, 95,647 bytes, SHA-256
`a7f382c563865b45f9756afa0f64fa91b701f6abf4b63363248186bcc44d1408`.
The adverse ledger has 239 unique events, 214,052 bytes, SHA-256
`efeb7598e55e6a78ddb272627dcc4c37d0973fe36b787da534649a4dad27a484`.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.complex-exponential.unit-circle-polar-coordinates`.
No author was contacted. Continue into the already translated exercise block
and validate the complete section reader at its semantic boundary.
