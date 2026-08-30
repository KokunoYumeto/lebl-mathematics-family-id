# R007 U430 Translation QA — Definite vs. Indefinite Integrals and Closed Form

Date: 2026-08-30

Stable unit: `diffyqs.v6.11.first-order.integrals-as-solutions.definite-vs-indefinite-and-closed-form`

## Exact boundary

- Source: `source/diffyqs-v6.11/ch-first-order-ode.tex`, raw lines 89–98 inclusive.
- Target: `translation/diffyqs/ch-first-order-ode.tex`, raw lines 89–98 inclusive.
- Alignment: source and target raw line 88 are the blank separator.
- Next cursor: source raw line 100 and target raw line 100; raw line 99 is the blank separator to be added with the next unit.
- Slice normalization: UTF-8, LF line endings, exactly one trailing LF.

| Slice/artifact | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| Source unit | 10 | 601 | `ef332a9ff33ceacb440cb57ef6275302f14ba5b2c517d67e2fc0722f6c0658e1` |
| Indonesian unit | 10 | 680 | `f6919302a02ca3aeb96c904e2a8de6f9eb18d7dd25393e8510beaf6da2c44c84` |
| Full current target | 98 | 4,158 | `dd10809f0a5714c8dc050e3878de7156dbaa138ca541dc35349261a245304451` |

## Deterministic structural QA

- PASS — source and target each contain exactly 10 aligned raw lines.
- PASS — ordered TeX command stream is identical: `\eqref`, `\myindex`, `\footnote`.
- PASS — cross-reference key `int:eqdef` is preserved exactly.
- PASS — three opening and three closing braces occur in each slice; target nesting is balanced.
- PASS — neither slice contains a math delimiter or environment; no formula payload is introduced, removed, or changed.
- PASS — the full target is strict UTF-8 without BOM, uses LF line endings, and ends with LF.
- PASS — no label, figure, asset, exercise, hint, proof, or solution state occurs in this unit.

## Language, terminology, and meaning QA

- `definite integral` → `integral tentu`, `indefinite integral` → `integral tak tentu`, and `antidifferentiation` → `mencari antiturunan` continue the established chapter terminology.
- `closed form` → `bentuk tertutup` is bound as `LEBL-TERM-0798`, consistent with existing R006/R007 reader usage.
- The defining footnote is translated as “rumus yang dinyatakan dengan fungsi-fungsi yang dikenal, tanpa integral atau limit,” preserving the source-local definition without claiming a universal formal boundary.
- Independent bilingual review caught and removed the unidiomatic draft phrase `rumus dalam fungsi-fungsi`; the corrected target is natural and faithful.
- The source’s contrast, computability claim, graphing claim, and statement that a closed-form antiderivative is not always crucial are all preserved.

No source correction, adverse event, O001 solution gap, asset, or rights change is introduced. Original author/source credits and the edition provenance note identifying OpenAI Codex gpt-5.6-sol, Ultra remain preserved by the edition controls.
