# R006 U275 — fundamental theorem of algebra

Status: **PASS for semantic/backend admission**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2433–2452
  inclusive, 20 LF-serialized lines, 994 bytes, SHA-256
  `7fdac5e4055c3601312004add6f29e261743eb674ae570eec13ced77f842ce2a`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2443–2462 inclusive, 20 LF-serialized lines, 1,095 bytes, SHA-256
  `329509372b62c0a2101c13824dc63825b7085201c80e0112c1e5fe8bd827cc1c`.
- The theorem, complete compactness/minimum proof, and exponential-function
  counterexample to analytic generalization are all included.
- The exercise subsection begins at source raw line 2454 / target raw line
  2464.

## Verification

Owner comparison and independent mathematical and final Indonesian-language
audits pass. Source and target preserve the exact 41-command sequence, four
ordered environment boundaries, twenty-two inline-math payloads, the index
hook and comment, and balanced 17/17 braces. The proof retains the infimum
`mu`, the growth-based radius, compact closed ball, attainment of the minimum,
and application of the preceding minimum-modulus lemma. No reader-facing
English remains and no source correction is introduced.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.maximum-principle-fundamental-algebra.fundamental-theorem-of-algebra-proof`.
No author was contacted.
