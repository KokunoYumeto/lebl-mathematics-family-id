# R006 step and absolute-value Fourier examples — U315 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.examples.step-and-absolute-value`  
Result: PASS after declared source accessibility correction ADV-0258

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4424–4537
  inclusive, 114 LF lines, 4,207 bytes, SHA-256
  `e3a9c3c861b88a6b88a7db8ab6c0edd2ca5d1662a1dbc76dd8fee2e35941e937`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4432–4545 inclusive, 114 LF lines, 4,485 bytes, SHA-256
  `cd86847834b817b98965b46f75a1cb2af8bf67a59edad385a14a0d72c5a8bd1a`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.

## Deterministic structural and mathematical audit

- TeX command streams: 110 source / 110 target, exact ordered equality.
- Environment streams: 16 events in each range, exact ordered equality.
- Inline mathematics: 30 source / 30 target payloads, exact equality.
- Four `equation*` payloads are exact after only localizing the two literal
  `\text{for }` fragments to `\text{untuk }`.
- Fourteen `%mbx...` conversion comments are byte-identical and ordered.
- Brace balance is 71/71 in each range; unescaped dollar delimiters are 60 in
  each range.
- Both figure references, asset call `fourierheavi_csaw`, label
  `fig:fourierheavicsaw`, caption topology, and example boundary are preserved.
- Every sign, factor, bound, coefficient, symmetric partial sum, convergence
  claim, coefficient-decay comparison, and endpoint-continuity claim passed
  independent review.

## Indonesian and accessibility audit

Independent review passed the final prose, caption, and full localized figure
description. Two initially awkward alt-text clauses were rewritten into natural
Indonesian without changing the described geometry. No unintended English
reader prose remains. Ledger terms include `fungsi tangga`, `jumlah parsial
simetris`, `limit sepihak`, `kontinu Lipschitz`, and preferred
`diskontinuitas lompatan`.

New bindings:

- `LEBL-TERM-0771`: jump discontinuity → `diskontinuitas lompatan`;
- `LEBL-TERM-0772`: periodic extension → `perluasan periodik`.

The terminology ledger has 772 data rows / 119,837 bytes, no duplicate IDs,
SHA-256 `4d376cc62f440c74be375666331cd97f557f9bb33ed7554c02c234350dc2f0f0`.

## Declared source correction

ADV-0258 records a P3 accessibility defect. The source defines `h=1` on
`[0,pi]`, `h=-1` on `(-pi,0)`, and extends periodically, so
`h(-pi)=h(pi)=1`. Its figure description says the negative segment runs “from
minus pi to 0,” which reads as including the wrong left endpoint. The Indonesian
alt text minimally states that the negative segment is the open interval from
minus pi to 0. The plotted asset, function, formulas, caption, and all other
description content are unchanged. Independent mathematical, structural,
asset, caption, and language audits confirm the repair.

The adverse ledger now has 258 rows / 237,360 bytes, SHA-256
`eade5d479fba456dcdd92c09f7fbf540331ecce67fb752645aed6919969c3753`.
No exercise, solution, or O001 gap occurs in this unit.

Next exact boundary: frozen source raw line 4539 / live target raw line 4547,
the coefficient-decay criterion and first convergence proposition.
