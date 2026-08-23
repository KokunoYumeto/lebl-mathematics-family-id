# R007 Diffy Qs — U012 bounded translation receipt

Status: translated and QA-verified locally; not published; no author contact.

## Bound

- Source: source/diffyqs-v6.11/ch-intro.tex, raw lines 1114–1208, the complete classification Exercises subsection through the end of the source component.
- Target: translation/diffyqs/ch-intro.tex, raw lines 1069–1163.
- Source unit UTF-8 bytes: 3,395.
- Source unit SHA-256: d85c8182cea9e432e3c8d06068cc4b5d8233ce8d7538ec85ebb361449c980cb1.
- Target unit UTF-8 bytes: 3,527.
- Target unit SHA-256: 1930b6477b53bc68db33a779f62285867644a09f3fb2f9a38221867d39ae99ff.
- Target file after U001–U012: 43,914 bytes; SHA-256 fecf316e42669a7cceef4338b5aae23dd6c6825cc8c512b2263e226614bbfadf.

## QA

- TeX control sequences: 141 / 141; command multiset identical.
- Braces: 87 opening and 87 closing in each unit.
- Ordered environment tokens: 18 / 18 and identical.
- Exercise topology: 7 / 7 exercise environments; 12 / 12 `\task` entries; the `\setcounter{exercise}{100}` transition retained.
- Supplied-solution state: all three source `\exsol` blocks retained in order, while the four source exercises without supplied solutions remain without invented solutions.
- Dollar-delimited math markers: 66 / 66; all 33 ordered math payloads are byte-identical, including the classification equations, divergence/curl formulas, source ordinal notation, and final answer formulas.
- The six-part classification answer preserves every source determination: ODE/PDE, equation/system, order, linearity, homogeneity, coefficient type, and autonomy where applicable.
- UTF-8/mojibake check: passed; target mojibake hits: 0.
- Reader-facing prompts, hints, and supplied solution prose were translated into natural Indonesian without altering mathematical expressions or answer values.

## Cursor and provenance

- `source/diffyqs-v6.11/ch-intro.tex` is now complete through its final raw line 1208.
- The pinned master `source/diffyqs-v6.11/diffyqs.tex` next includes `ch-first-order-ode.tex` at raw line 281, after `ch-intro.tex` at raw line 276.
- Next source cursor: source/diffyqs-v6.11/ch-first-order-ode.tex, raw line 1; the 4,180-line source component exists, and no Indonesian target component exists yet at translation/diffyqs/ch-first-order-ode.tex.
- Translation tooling provenance: OpenAI Codex gpt-5.6-sol, Ultra.
- This is a local production receipt only; no upstream issue or author communication was initiated.
