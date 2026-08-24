# R006 U271 — complex exponential and trigonometric exercises

Status: **PASS for semantic/backend admission**  
Date: 2026-08-24  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Bound unit

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 2141–2261
  inclusive, 121 LF-serialized lines, 3,492 bytes, SHA-256
  `74cde11c2693ab14134b6bdc8182cfa01fec8e2cfa30303ce7da3d842639024b`.
- Live Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  2151–2271 inclusive, 121 LF-serialized lines, 4,013 bytes, SHA-256
  `1d52d278fee44849d5c50361ba03571d8c6e92d64318c6a90228718b1bdd3c0a`.
- Combined U270–U271 target: raw lines 2107–2271, SHA-256
  `81a30143c245a70d899b052bd554f871770321037b203b9d9b0f2ce5aa27ab9a`.
- The exact next boundary is target raw line 2272/source raw line 2262,
  `\sectionnewpage`; the next section heading is the maximum principle and
  fundamental theorem of algebra.
- Full live target: 5,483 lines, 187,510 bytes, SHA-256
  `7efdde57494518efc8f3ac61b868783459245939c77ec41cb66120a3aac999d6`.

## Verification

Owner comparison and two independent final audits pass. Source and target each
preserve eleven unsolved exercises, one `exnote`, two enumerations, eight
items, three exact display payloads, one stable label
`exercise:cossinidentity`, two ordered index hooks, and the closing separator.
The ordered 34 environment tokens match exactly; braces balance; there are no
solution, proof, or answer environments. All formula changes are confined to
explicitly recorded domain qualifications in prose. No reader-facing English
residue remains, and the final convergence sentence explicitly names the
right-hand series as its subject.

The exercise corrections are recorded as `LEBL-ID-ADV-0237` through
`LEBL-ID-ADV-0239`: the domain of the tangent quotient, the real domains of the
inverse-trigonometric derivatives, and the ambiguous convergence predicate.
Independent mathematical review verified `cos(x) != 0`, differentiability of
arcsine on `(-1,1)`, differentiability of arctangent on the real line, and the
unchanged endpoint-inclusive series objective. The explicit exponential-map
wording is a clarity refinement and not separately classified as a source
defect.

The terminology ledger has 684 unique rows, 95,647 bytes, SHA-256
`a7f382c563865b45f9756afa0f64fa91b701f6abf4b63363248186bcc44d1408`.
The adverse ledger has 239 unique events, 214,052 bytes, SHA-256
`efeb7598e55e6a78ddb272627dcc4c37d0973fe36b787da534649a4dad27a484`.

## Decision

Admit the unit under stable ID
`ra.v2.functions-as-limits.complex-exponential.exercises`. The exercise block
resolves the deliberate forward reference left in the preceding partial-reader
checkpoint. No author was contacted. Build and inspect the section-complete
reader before promotion or publication.
