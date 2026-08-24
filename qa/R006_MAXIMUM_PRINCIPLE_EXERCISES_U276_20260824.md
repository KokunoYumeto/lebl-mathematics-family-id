# R006 U276 — maximum-principle exercises and rational singularities

Status: **PASS for semantic/backend admission; two declared inherited-source corrections**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2454–2536
  inclusive, 83 LF-serialized lines, 3,008 bytes, SHA-256
  `4207c4f68ad5aae1a1bfa98c6e7e6abd33941d0db5a7a541e412fa78c76217f8`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2464–2546 inclusive, 83 LF-serialized lines, 3,491 bytes, SHA-256
  `f7896cc02dcfcc3f9c7883ba0b206ec3945a9cc9ed740d1b2a1df990adeafda7`.
- The unit preserves seven exercises, four source hints, zero source answers,
  and zero source solutions. All seven unresolved solution needs are mapped to
  O001 without inventing solutions.
- The next section begins at source raw line 2542 / target raw line 2552:
  equicontinuity and the Arzelà–Ascoli theorem.
- Full live target: 5,483 lines, 188,535 bytes, SHA-256
  `004bb76d7a48fcf842073d49649303d7ab96a65c0782d374094a381eaffbf974`.

## Verification

Owner comparison and independent mathematical and final Indonesian-language
audits pass. Source and target preserve the 83-command sequence, eighteen
ordered environment boundaries, seven exercise environments, one `exnote`,
five label/reference hooks, one display block, and balanced 55/55 braces. All
fifty-three ordered inline-math payloads match except the single intentional
center repair described below. The definitions of rational function, zero,
isolated singularity, removable singularity, pole, and pole at infinity; both
limit formulations; the degree bound; cancellation exercise; singularity
dichotomy; and final iff characterization are faithful. No reader-facing
English remains.

Two inherited source defects are transparently corrected:

- `LEBL-ID-ADV-0240`: for an arbitrary zero `z_0`, the source's punctured
  neighborhood `0 < |z| < epsilon` is corrected to
  `0 < |z-z_0| < epsilon`.
- `LEBL-ID-ADV-0241`: the unconditional isolated-zero sentence is qualified
  by the local identically-zero alternative, and the polynomial specialization
  is restricted to polynomials that are not identically zero.

The adverse ledger has 241 unique parseable events, 216,589 bytes, SHA-256
`724d21f2dce15ce3b4cd49498e1dce1ad4bb9445833d94e952b0362b531bf04f`.
The O001 ledger has seven unique open gaps, four with source hints and none
with source solutions; it is 4,708 bytes, SHA-256
`06d3cb8a5616f3f2009c36336e19a05f429e9336257f451ea33adb117166da4e`.
Terminology entries `LEBL-TERM-0719` through `LEBL-TERM-0722` bind isolated
zero, isolated singularity, pole, and pole at infinity.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.maximum-principle-fundamental-algebra.exercises-rational-functions-and-isolated-singularities`.
This closes the complete maximum-principle/fundamental-algebra section. No
author was contacted.
