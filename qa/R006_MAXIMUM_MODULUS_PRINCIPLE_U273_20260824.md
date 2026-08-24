# R006 U273 — maximum-modulus principle, real counterexample, and local heuristic

Status: **PASS for semantic/backend admission**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2343–2374
  inclusive, 32 LF-serialized lines, 1,436 bytes, SHA-256
  `d38581cc9ff1bf8c44daa50d5c2c9bf7839e0c087fe58a0bd5c4629950e3dd7b`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2353–2384 inclusive, 32 LF-serialized lines, 1,624 bytes, SHA-256
  `8a553e73048c549661687a6bed5a8cd64307abef0dc3478b00359d030afec788`.
- The unit explains the minimum-modulus principle, derives and states the
  maximum-modulus principle, preserves the connectedness hypothesis, gives the
  real-number counterexample, and records the local `1+az^k` heuristic.
- The theorem label `thm:maxprinciple` and forward exercise reference
  `exercise:maxprinciple` are preserved.
- The next untranslated lemma begins at frozen source raw line 2376 and live
  target raw line 2386.
- Full live target: 5,483 lines, 187,802 bytes, SHA-256
  `eaf4ed5d3f4805baedce9d159d1789be7fdbe60cd4d7624185d05f1b397f5827`.

## Verification

Owner comparison and independent mathematical and final Indonesian-language
audits pass. Source and target preserve the exact 23-command sequence, four
ordered environment boundaries (`thm`, `remark`), nineteen inline-math
payloads, one label, one reference, two comments, and zero display-math blocks.
Braces balance 16/16 in both slices. The final target has no reader-facing
English residue.

The reciprocal argument keeps `1/f` analytic near a point where `f` is
nonzero. The identity-theorem step, open connected domain, relative maximum,
constant-function conclusion, complex choice `w=i\epsilon`, and the local
higher-order-term argument are unchanged. The final wording uses the admitted
forms *prinsip modulus minimum*, *prinsip modulus maksimum*, *prinsip
maksimum*, and *polinom*. No source correction is introduced.

The terminology ledger has 715 unique rows, 101,311 bytes, SHA-256
`d5d3e55d73edbbc82a7568850927d0bc0a69037e25a6daafdc25232215adf6d8`.
New terms `LEBL-TERM-0713` through `LEBL-TERM-0715` bind the three principle
names. The adverse ledger remains at 239 unique events, 214,052 bytes,
SHA-256 `efeb7598e55e6a78ddb272627dcc4c37d0973fe36b787da534649a4dad27a484`.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.maximum-principle-fundamental-algebra.maximum-modulus-principle-real-counterexample-local-heuristic`.
Continue contiguously at the polynomial-growth lemma, source raw line 2376 /
target raw line 2386. No author was contacted. A full reader rebuild remains
deferred to the next coherent section boundary.
