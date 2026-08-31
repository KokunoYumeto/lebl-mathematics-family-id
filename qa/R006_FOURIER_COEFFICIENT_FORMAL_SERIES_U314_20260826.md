# R006 Fourier coefficients and formal series — U314 QA receipt

Date: 2026-08-26  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.coefficients-and-formal-series`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4400–4422
  inclusive, 23 LF lines, 943 bytes, SHA-256
  `5df442036896a96d2b1eec09d3c560485aac25a3d7d972390ba9a3c01480d564`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4408–4430 inclusive, 23 LF lines, 1,104 bytes, SHA-256
  `6e35830ffa9e955f10b59ca6259858ed1b4aaa35c76bdb4d1d9513f9ab763b58`.
- Full frozen source remains 5,473 lines, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target is 5,481 lines / 194,881 bytes, SHA-256
  `629bcfb960a00fe27c8ef3826fe39282d47e21e9c0d6d4920a92e13dfc5cd878`.

## Deterministic structural audit

- TeX command streams: 27 source / 27 target, exact ordered equality.
- Environment streams: four events / two balanced `equation*` displays in
  each, exact ordered equality.
- Inline mathematics: three source / three target payloads, exact equality.
- Display mathematics: two source / two target payloads, exact equality.
- Brace balance: 15 opening / 15 closing in each range.
- Unescaped dollar delimiters: six in each range.
- One footnote is preserved, and `\glsadd{not:FS}` remains exact.
- The factor `1/(2\pi)`, bounds `[-\pi,\pi]`, exponent `e^{-inx}` in the
  coefficient formula, exponent `e^{inx}` in the formal series, complex
  codomain, and hat notation are unchanged.

## Mathematical and language audit

An independent audit passed without correction. The explanation of `\sim`
correctly states that it creates only a formal association; it asserts neither
equality nor convergence. The Indonesian prose is natural, and no unintended
English residue remains.

Terminology bindings:

- existing `LEBL-TERM-0767`: Fourier coefficient → `koefisien Fourier`;
- new `LEBL-TERM-0769`: Fourier transform → `transformasi Fourier`;
- new `LEBL-TERM-0770`: formal series → `deret formal`.

The terminology ledger now has 770 data rows / 119,005 bytes, no duplicate
term IDs, SHA-256
`05ff9fa34e3e1e0388dc4fd54c1dab1d25a5abc4934648e33a48db400cd57896`.

No source correction, exercise, asset, solution, or O001 gap occurs. Provenance
remains OpenAI Codex gpt-5.6-sol, Ultra, acting on the user's instruction;
source authorship and licensing remain unchanged.

Next exact boundary: frozen source raw line 4424 / live target raw line 4432,
the complete step-function and absolute-value examples with their localized
figure description.
