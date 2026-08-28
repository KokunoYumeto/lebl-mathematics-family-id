# R006 localization Lipschitz-theorem proof — U413

Status: **PASS after three minimal source-side precision corrections**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact admitted unit

- Unit: `ra.v2.fourier-series.localization.lipschitz-theorem-proof`
- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 5025–5096,
  72 LF lines / 2,447 bytes, SHA-256
  `714ffcb35f5a4b9100b27aa8bd83dc39f9751d1321dca205040c9f5533994829`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  5039–5110, 72 LF lines / 2,872 bytes, SHA-256
  `fb1c2507f7d7556d94f95707b4b2a790e4d83f1fa7c8c6b172c9d47c8328af53`.
- Full live R006 target after the unit: 5,487 LF lines / 197,213 bytes,
  SHA-256
  `3cc19965fdba33b110cbc1da31abc17f6b4966595b462a71dcab4d94999f4cfa`.

## Mathematical and structural audit

The proof preserves the Dirichlet-kernel normalization, the convolution
identity for `s_N(f;x)-f(x)`, the pointwise Lipschitz estimate, the
trigonometric decomposition, the Bessel-inequality argument, and the final
pointwise convergence conclusion. All 22 inline-math payloads and all five
displayed-math payloads are byte-identical. The ordered 144-command streams,
all environment events, 93/93 brace pairs, and 44 dollar delimiters are exact.
The proof environment and both theorem references are unchanged.

An independent no-edit audit confirmed the mathematical argument and natural
Indonesian prose. Its two copyedits were applied: the Bessel sentence now has
an unambiguous antecedent, and the final Indonesian `yaitu` construction has
the correct punctuation. A second deterministic replay after those edits
again proved exact math, command, environment, brace, and delimiter topology.
There is no English reader prose inside the admitted unit.

## Declared source corrections

1. ADV-0263: the source calls
   `M|t|/|sin(t/2)|` continuous at the origin even though the displayed
   quotient is undefined there. The target says it has a finite limit and
   therefore extends continuously to the origin.
2. ADV-0264: the source calls
   `(f(x-t)-f(x))/sin(t/2)` Riemann integrable on the closed interval before
   defining it at `t=0`. The target assigns an arbitrary value at that single
   point before applying the bounded one-point extension argument. This does
   not change the integral.
3. ADV-0265: for the normalized inner product defined by the source,
   `sin(Nt)` and `cos(Nt)` have squared norm `1/2`, so they are orthogonal but
   not orthonormal. The target applies Bessel after normalization and states
   that the displayed integrals are constant multiples of the normalized real
   Fourier coefficients. The conclusion is unchanged.

No formula changed and no upstream contact occurred.

## Indonesian terminology and ledgers

TERM-0792 admits `normalization` → `normalisasi`, with `menormalisasi` and
`dinormalisasi` as contextual forms. Established entries for Fourier
coefficient, inner product, orthogonal system, orthonormal system, norm,
Riemann integrability, trigonometric identity, and origin are reused.

At this boundary the terminology ledger has 792 unique data rows / 126,603
bytes, SHA-256
`445f4bc852a845fdd026f27f40ec37e2b2b45d3d90463cee921e4cedf82eb340`.
The adverse ledger has 265 unique events / 246,894 bytes, SHA-256
`50ef0ed79107f617b356e59a22176d216ed6b40cfeffa2813324ba953f96bd7d`.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt with the bound complete Indonesian
Volume-I auxiliary label set `realanal.aux`, 354,013 bytes, SHA-256
`8696b0f4e80ddfe0093da26955f868304892bf081eb01c04d21feedd1815d5c2`.
After index and glossary generation and two final `pdflatex -halt-on-error`
passes, the non-release integration PDF is 241 pages / 2,428,768 bytes,
SHA-256
`897b37083b7a3f0887244b707fabffca3b35caa2ee718afc1b95347f0ddf631e`.
The final log is 104,268 bytes, SHA-256
`33730ab704003fd08cf3c48c2dd211e5855284fd3e789aead1fa457433a699cd`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. The 15 overfull
horizontal boxes are inherited outside U413; there are zero overfull vertical
boxes.

Pages 227–228 were rendered at 144 dpi and visually inspected. The theorem,
proof displays, page break, prose, and proof terminator are readable, aligned,
and unclipped. The English text beginning immediately after the proof on page
228 is the exact next untranslated source boundary, not residue inside U413.
The generated PDF and render directory are transient integration evidence, not
release artifacts; the render PNGs were removed after inspection.

Next exact boundary: frozen source raw line 5098 / live target raw line 5112,
the locality consequence and its corollary.
