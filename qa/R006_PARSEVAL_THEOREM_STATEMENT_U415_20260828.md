# R006 Parseval opening and theorem statement — U415

Status: **PASS; no mathematical source correction required**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact admitted unit

- Unit: `ra.v2.fourier-series.parseval.opening-and-theorem`
- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 5132–5185,
  54 LF lines / 1,175 bytes, SHA-256
  `45fec3cd6fc0717e06bc8464064225293d03cd10a5b1113a32a901ce60bdc2de`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  5146–5199, 54 LF lines / 1,238 bytes, SHA-256
  `4796979fe34dae501dac8711c1a7ee00708e00e0493ce94db6c5f743aa262ee0`.
- Full live R006 target after the unit: 5,487 LF lines / 197,479 bytes,
  SHA-256
  `8fd73d3e7d9fd746e16f9a3da26d799833eddfe7d9436a3fba4d8af075db92cc`.

## Mathematical and structural audit

The unit preserves the claim of convergence in the `L^2` sense, the formal
bilateral Fourier series for `f` and `g`, convergence of the partial sums in
the integral squared-modulus quantity, the integral inner-product identity,
and the Parseval norm identity. Conjugation remains on the second argument
`g` and coefficient `d_n`; every bilateral bound, factor `1/(2\pi)`, and the
distinction between `s_N(f)` and `s_N(f;x)` is exact. No high-confidence
mathematical source defect was found.

All five inline-math payloads are byte-identical. The unit contains four
display blocks: displays two through four are byte-identical, while the first
differs only by the intended reader-text localization
`\text{and}` → `\text{dan}`. After that one normalization, all four complete
display payloads are exact. The ordered 71-control-sequence stream, twelve
environment events, four balanced `equation*` environments inside one
balanced `thm` and one balanced `samepage`, 42/42 brace pairs, ten dollar
delimiters, and the footnote line-continuation `%` are preserved. The title,
index entry, footnote prose, and theorem connectives are localized; the URL,
proper name, and dates are unchanged.

Two independent no-edit reviews confirmed the mathematics, boundary, and TeX
topology. One justified wording correction was applied: the closed-up and
awkward `takhingga` phrasing was replaced by the natural
`dengan tak berhingga banyak komponen`. A deterministic replay after the edit
again passed every structural and mathematical comparison. Target raw line
5201 is exactly the untouched `\begin{proof}` and its English proof prose
begins at line 5202.

## Indonesian terminology and ledgers

TERM-0794 admits `Parseval's theorem` → `teorema Parseval`; TERM-0795 admits
`L2 convergence` → `konvergensi L^2`, with
`konvergen dalam pengertian L^2` as the contextual prose form. Established
entries for Fourier coefficient, inner product, `L^2` norm, periodic function,
Riemann integrability, and complex conjugation are reused.

At this boundary the terminology ledger has 795 unique data rows / 127,626
bytes, SHA-256
`a695a97595c7b43198d8ad2751065e79683470b36a710259afc80086657223df`.
The adverse ledger is unchanged at 265 unique events / 246,894 bytes,
SHA-256
`50ef0ed79107f617b356e59a22176d216ed6b40cfeffa2813324ba953f96bd7d`.
There is no exercise, solution, asset, or O001 solution gap in this unit.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in a fresh directory with the bound
complete Indonesian Volume-I auxiliary label set. After index and glossary
generation and two final `pdflatex -halt-on-error` passes, the non-release
integration PDF is 241 pages / 2,428,355 bytes, SHA-256
`7a63a231dffa818f591f710631556f9b67be3a1635025495f207a796a6981aad`.
The final log is 104,268 bytes, SHA-256
`3d6f34a4a44e9dbc66d44afbe97feb86dc3fbc57158eaebb04f0cb4d85477c68`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. The 15 overfull
horizontal boxes are inherited outside U415; there are zero overfull vertical
boxes.

Physical pages 229–230 were rendered at 144 dpi and visually inspected. The
U415 theorem on page 229 is centered, readable, properly spaced, and unclipped;
the footnote, hyperlink, four displayed identities, conjugation bars, and
page boundary are intact. Page 230 cleanly continues the exact untranslated
proof and exercises. Poppler's optional-content diagnostics on these pages are
identical in kind and count to the verified U414 integration PDF, both
extractions exit successfully, and no visible U415 defect is present. The
render PNGs were removed after inspection. The integration PDF remains
transient build evidence and is not a replacement for the verified U397
reader release.

Next exact boundary: frozen source raw line 5187 / live target raw line 5201,
the complete proof of Parseval's theorem.
