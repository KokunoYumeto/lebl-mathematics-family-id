# R006 Bessel inequality — U320 QA receipt

Date: 2026-08-27  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Unit: `ra.v2.fourier-series.orthonormal-systems.bessel-inequality`  
Result: PASS

## Bound range

- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4805–4850
  inclusive, 46 LF lines, 1,161 bytes, SHA-256
  `0d8d5d1fbf9601af8c05c7222344e517cc352889d050f1564517062093e883d9`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  4819–4864 inclusive, 46 LF lines, 1,252 bytes, SHA-256
  `042e46ce7c8a45b24c0f3f321c26eee1c786c65e72a563eb406a4f797729283d`.
- Full frozen source remains 5,473 lines / 179,961 bytes, SHA-256
  `13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
- Full live target is 5,487 lines / 196,311 bytes, SHA-256
  `f878c2862a574a3544ed740cafbdbd30faa1cd76cdd459b4984f4ba387a5bd67`.

## Deterministic structural and mathematical audit

- The ordered 54-command sequence is identical, SHA-256
  `50d8e4daeacbef5b0e56761e0f0f3fe7891042557ce47ded191883d8a543776d`.
- All seven inline-math payloads are byte-identical, with aggregate SHA-256
  `9b50ec362329d3bbf3644601cee2ceae599d3af9216c5e08a445b9307ee7e8bd`.
- All six display-math payloads are byte-identical, with aggregate SHA-256
  `04e211a0f84e2f3038a8c3711709b216d440ae0f6b36f3ee4cfe6c87fa31a41c`.
- Environment order, theorem label `thm:bessels`, Friedrich Bessel hyperlink,
  linked name, footnote topology, dates, and biographical roles are preserved.
- Both ranges have balanced 39/39 braces and 14 unescaped dollar delimiters.
- Independent review confirmed the finite-sum identity, Bessel bound,
  hypotheses, infinite-series inequality, convergence claim, and
  `c_k \to 0` consequence are mathematically exact.

## Indonesian and terminology audit

The reader-facing prose is natural Indonesian and has no unintended English
residue. The theorem title and index entry use `ketaksamaan Bessel`, consistent
with the general named-inequality preference in TERM-0626. One new binding is
admitted:

- `LEBL-TERM-0785`: Bessel's inequality → `ketaksamaan Bessel`.

The terminology ledger has 785 data rows / 123,911 bytes, no duplicate IDs,
SHA-256 `edcf8188f05a4604e36c63e4d3b547c4211e8489855916da29ce5ba3ef425164`.
Independent final mathematical, Indonesian-language, footnote, hyperlink, and
structural review returned PASS.

No source correction, asset, exercise, solution, or O001 gap occurs in this
unit. The seminorm/quotient qualification recorded as ADV-0259 remains the
governing context for the displayed `L^2` quantity.

Next exact boundary: frozen source raw line 4852 / live target raw line 4866,
the Dirichlet-kernel and approximate-delta-functions subsection.
