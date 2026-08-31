# R006 Fourier-series opening — U313 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.fourier-series-opening`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4363–4396
  inclusive, 34 LF lines, 1,325 bytes, SHA-256
  `1c8189f1deabbc39951c037c4ea4e78468e7bdfdae5508efdcd1a04be3858fbb`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4371–4404 inclusive, 34 LF lines, 1,539 bytes, SHA-256
  `596845448d6e02570c2eaabee4a280e7e2c0c04e57d6376ed3f712b58a654662`.
- Full frozen source remains 5,473 lines, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target is 5,481 lines / 194,720 bytes, SHA-256
  `32a2bb212fb03203423c032cb5b3fcf868cbf4d8a4d43f07a58348a3b9c958bc`.

## Deterministic structural audit

- TeX command streams: 35 source / 35 target, exact ordered equality.
- Environment streams: six events / three balanced `equation*` displays in
  each, exact ordered equality.
- Inline mathematics: four source / four target payloads, exact ordered
  equality.
- Display mathematics: three source / three target payloads, exact equality.
- Brace balance: 23 opening / 23 closing in each range.
- Unescaped dollar delimiters: eight in each range.
- The notation anchor `\glsadd{not:FSsympartsum}` is preserved exactly.
- The bilateral bounds, symmetric truncation, definition of `s_N(f;x)`, and
  every formula are unchanged.

## Mathematical and language audit

An independent source–target review found no discrepancy. The Indonesian is
natural and preserves the distinction between a bilateral Fourier series and
its symmetric partial sums. The source phrase “the series has two limits” is
rendered explicitly as the index tending to infinity in two directions; this
clarifies the same mathematical meaning without changing the summation rule.
No unintended English residue remains; `Fourier` and `Euler` are proper names.

Terminology bindings:

- existing `LEBL-TERM-0761`: Fourier series → `deret Fourier`;
- new `LEBL-TERM-0767`: Fourier coefficient → `koefisien Fourier`;
- new `LEBL-TERM-0768`: symmetric partial sum → `jumlah parsial simetris`;
- existing convergence terminology remains `konvergensi mutlak` and
  `konvergensi seragam`.

The terminology ledger now has 768 data rows / 118,342 bytes, no duplicate
term IDs, SHA-256
`98ba26d70ee665bc1b9325462adf6320aee78427005462b7a37a6ace94cff78f`.

No source correction, exercise, asset, solution, or O001 gap occurs in this
unit. Translation provenance remains OpenAI Codex gpt-5.6-sol, Ultra, acting on
the user's instruction; source authorship and licensing remain unchanged.

Next exact boundary: frozen source raw line 4400 / live target raw line 4408,
beginning the converse definition and integral formula for Fourier
coefficients.
