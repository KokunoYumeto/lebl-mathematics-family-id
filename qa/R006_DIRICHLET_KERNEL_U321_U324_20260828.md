# R006 Dirichlet kernel and approximate delta functions — U321–U324 QA receipt

Date: 2026-08-28  
Resource: R006, Jiří Lebl, *Basic Analysis I–II* v6.3  
Units: `ra.v2.fourier-series.dirichlet-kernel.opening`,
`ra.v2.fourier-series.dirichlet-kernel.closed-form`,
`ra.v2.fourier-series.dirichlet-kernel.convolution`, and
`ra.v2.fourier-series.dirichlet-kernel.approximate-delta-functions`  
Result: PASS after declared source corrections ADV-0260 and ADV-0261

## Bound ranges

The complete subsection is frozen source raw lines 4852–4980 and Indonesian
target raw lines 4866–4994, both 129 LF lines. The source slice is 4,497 bytes,
SHA-256 `8d5b499eff41ee8b8f79843234f0d535c870e7f28963e45b7da41764e8a5c7bb`;
the target slice is 4,837 bytes, SHA-256
`0ec4733c3be902edb0f7412cd566296199efc32af6c27fc79fecbc13bbaadfb7`.

| Unit | Source range / bytes / SHA-256 | Target range / bytes / SHA-256 |
|---|---|---|
| U321 opening | 4852–4897 / 1,464 / `77a6f8d4736fb3f38ffd1efcbc850075ea93183e343bc995229b5e92df3e2c78` | 4866–4911 / 1,561 / `39e79cac9d641fb2bd5d9123532a96e55218acbabf3103b2a42fe8f25a9f9727` |
| U322 closed form | 4899–4924 / 733 / `811a800e3865508db326321ac98fd56112880df7f5b1db79e4a6c8d7ae029f8c` | 4913–4938 / 793 / `f1bf0138f4fd9cdc7e1574d08cb4a60a4b156f9107ae162b20da30475a6b3887` |
| U323 convolution | 4926–4944 / 619 / `2b94613bab9e6957f928698fdc42262e08a3b1d1a6e261bb7f931e5eb3a976c0` | 4940–4958 / 641 / `22f7188704b1afa3dad2488ec68a18e4721572aa3c1035f4e17b49d1f38719ee` |
| U324 approximate delta | 4946–4980 / 1,678 / `bab347ced0ec635920afe3539d8ce7c23c989d9f5d15f39639fe6289dd7b851a` | 4960–4994 / 1,839 / `b822a79e69eec62315cf76b016a1ae1211955fd47c22b000494a3b54afe86801` |

The complete frozen source remains 5,473 lines / 179,961 bytes, SHA-256
`13877cfa45bee3abf1bfc285a7651e6ffaabc2c4a65ca32708d5546ece93f240`.
The live target is 5,487 lines / 196,651 bytes, SHA-256
`5cfac7475255872ad5b08b9fedbe8d8387289d60f1777d5b2f4c8ed2e65d4807`.

## Deterministic mathematical and structural audit

- After applying only the three declared `n=1,2,...` → `n\in\mathbb Z`
  source-witness corrections, the ordered 180-command streams are exact,
  aggregate SHA-256
  `158784be6764406b8c40d6b8869ba34b714747c9d9cf2e01fbf3b46ef1c3195d`.
- All 24 environment events are identical and ordered.
- All 34 inline-math payloads are exact after those same three corrections,
  aggregate SHA-256
  `5134019c9488305a088a5bdae952d7d638b2e7823e4fb5b40d7a4974433aff17`.
- All 11 display payloads are exact after localizing only the literal words
  `with` and `where` to `dengan`, aggregate target SHA-256
  `8570e00ae865f6eefc7dfbab966e49a093a5cbbbf2e07c5e7892d0362754ade1`.
- Source and target each have balanced 119/119 unescaped braces and 68
  unescaped dollar delimiters.
- The asset call, reference, label, caption topology, and localized accessible
  description for `fig:approxdeltas` are preserved. Source and target copies of
  `approxdeltas.pdf` are byte-identical at 13,445 bytes, SHA-256
  `02c39a4490a49a65a0c7c2e458799958eb4677b38891f45669b28fe1f10569de`;
  their XP sources are byte-identical at 798 bytes, SHA-256
  `e0ffb80943889fbdb0e0c0b5fdb70350c9e17c94a119f18ccf1629aff30e2d78`.

Independent final mathematical, Indonesian-language, terminology, figure,
asset, accessibility, and structural review passed all 45 mathematical spans,
the normalized inner product, Fourier coefficients, Bessel bound, closed-form
Dirichlet kernel, convolution identities, and deliberately heuristic delta
discussion. No unintended English reader prose remains.

## Indonesian terminology and declared corrections

The terminology ledger admits TERM-0786 `Dirichlet kernel` → `kernel
Dirichlet`, TERM-0787 `delta function` → `fungsi delta`, and TERM-0788
`trigonometric Fourier series` → `deret Fourier trigonometri`; TERM-0737
continues to bind `approximate delta function` → `fungsi delta hampiran`.
The field-facing `Kernel Dirichlet` form is independently attested in Veronika
Fitri Rianasari, *Deret Fourier dan Pemakaiannya* (Universitas Sanata Dharma,
2008), page 70:
`https://repository.usd.ac.id/23386/2/041414012_Full.pdf`.
The ledger now has 788 data rows / 125,083 bytes, SHA-256
`13cc3a055ddea1f48f591badec9e4d15e19b65c77ee3c4709a4aa973b23cddd8`.

- ADV-0260 corrects the three positive-only exponential-system indices to
  `n\in\mathbb Z`, matching the immediately ensuing bilateral series,
  coefficients, symmetric sums, and Bessel bound.
- ADV-0261 corrects only the source alt-text typo `mius pi` to the intended
  `minus pi` while localizing the complete description.

The adverse ledger has 261 rows / 241,612 bytes, SHA-256
`e31566004b39d688d5bb4bea5fd06a5777ede6714c1d9427cb9dcbe8584f088a`.
No exercise, solution, or O001 gap occurs in these units.

## Bounded integration build

Two consecutive `pdflatex -halt-on-error` passes over the complete Volume II
driver succeeded. The second pass produced a 235-page, 2,317,112-byte
non-release integration PDF, SHA-256
`2220590b9e4f86cac2c163a36db662edfa49bd288c813bebe297df1df81e44a4`,
with zero hard TeX errors. `fig:approxdeltas` and its PDF asset resolved. Ten
remaining warning lines concern pre-existing external Volume-I references in
the complete mixed driver, not this subsection. The generated build directory
is transient and is not a release artifact.

Next exact boundary: frozen source raw line 4982 / live target raw line 4996,
the Localization subsection.
