# R006 U274 — polynomial growth at infinity

Status: **PASS for semantic/backend admission**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2376–2431
  inclusive, 56 LF-serialized lines, 1,702 bytes, SHA-256
  `2efaded4d1f603020275b0f16b09c98f21b6b8724fc98efe12d4ee7f39f69c6b`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2386–2441 inclusive, 56 LF-serialized lines, 1,851 bytes, SHA-256
  `81de558e8ef7b7aba434418c7331118527e36794652a872c3dc03aa29c8020f0`.
- The unit contains the complete polynomial-growth lemma, proof, analytic
  counterexample, and degree-`d` asymptotic heuristic.
- The next unit begins at source raw line 2433 / target raw line 2443 with the
  fundamental theorem of algebra.

## Verification

Owner comparison and independent mathematical and final Indonesian-language
audits pass. Source and target preserve the exact 63-command sequence, ten
ordered environment boundaries, twenty-one inline-math payloads, two display
blocks, every coefficient and exponent, and balanced 52/52 braces. The
reverse-triangle estimate, eventual positivity of the parenthesized factor,
the lower bound `R^d |a_d|/2`, and the distinction between polynomials and
entire analytic functions are mathematically unchanged. No reader-facing
English remains and no source correction is introduced.

Terminology entries `LEBL-TERM-0716` through `LEBL-TERM-0718` bind polynomial
growth at infinity, degree, and highest-degree term. The complete terminology
ledger has 722 unique rows, 102,557 bytes, SHA-256
`dfd2ac7e8c5b572d224238164dd7c6414d95a2f1ea703706ed655d371072c511`.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.maximum-principle-fundamental-algebra.polynomial-growth-at-infinity`.
No author was contacted.
