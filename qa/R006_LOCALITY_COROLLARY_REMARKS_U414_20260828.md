# R006 locality consequence, corollary, and remarks — U414

Status: **PASS; no mathematical source correction required**  
Date: 2026-08-28  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact admitted unit

- Unit: `ra.v2.fourier-series.localization.locality-corollary-and-remarks`
- Frozen source: `source/ra-v6.3/ch-approximate.tex`, raw lines 5098–5130,
  33 LF lines / 1,427 bytes, SHA-256
  `b345eb906e6ceaf082cf7315d2c3c74291e62496116192681997ab78c56ff04a`.
- Indonesian target: `translation/ra/ch-approximate.tex`, raw lines
  5112–5144, 33 LF lines / 1,630 bytes, SHA-256
  `85331de3072f636dc85120567d57cab88b58b9292c4043d8f13211b407292f43`.
- Full live R006 target after the unit: 5,487 LF lines / 197,416 bytes,
  SHA-256
  `5f85aa1a7902c516573ddfede0801eea2319a746f9237a5c7d6c6cda480b6289`.

## Mathematical and structural audit

The unit preserves the locality consequence, the open-interval zero-function
corollary, its equivalent two-function statement, the linearity argument for
`f-g`, the distinction between local convergence and globally affected
convergence rate, and the Stone--Weierstrass comparison. Openness of `J`
supplies a neighborhood contained in `J`, so the use of `M=0` is valid at
every stated point. Since the Fourier sums of `f-g` tend to zero, convergence
of either sequence is equivalent to convergence of the other. No
high-confidence mathematical source defect was found.

All 32 inline-math payloads are byte-identical; the unit has no displayed
math. The complete ordered 30-control-sequence stream, the single balanced
`cor` environment, 9/9 brace pairs, and 64 dollar delimiters are exact. The
source's conversational English inversion in “how fast does ... converge” is
regularized as natural Indonesian prose without changing content. There is no
English reader prose inside the admitted boundary.

An independent no-edit review confirmed the argument and the Indonesian
translation. Its two language corrections were applied: the established
`fungsi $2\pi$-periodik` word order is used, and the plural
`polinom-polinom trigonometri` is preserved. A deterministic replay after
those edits again proved exact math, command, environment, brace, and
delimiter topology.

## Indonesian terminology and ledgers

TERM-0793 admits `rate of convergence` → `laju konvergensi`, with
`kecepatan konvergensi` recorded as a variant. Established entries for local
behavior, neighborhood, localization, partial sum, periodic function,
uniform approximation, Riemann integrability, and Stone--Weierstrass are
reused.

At this boundary the terminology ledger has 793 unique data rows / 126,988
bytes, SHA-256
`345fd7515955411d56409e4cb0eb0c9975458e489efe89c7ee6d371def3d22bb`.
The adverse ledger is unchanged at 265 unique events / 246,894 bytes,
SHA-256
`50ef0ed79107f617b356e59a22176d216ed6b40cfeffa2813324ba953f96bd7d`.
There is no exercise, solution, asset, or O001 solution gap in this unit.

## Deterministic integration build and visual QA

The complete Volume-II driver was rebuilt in a fresh directory with the bound
complete Indonesian Volume-I auxiliary label set. After index and glossary
generation and two final `pdflatex -halt-on-error` passes, the non-release
integration PDF is 241 pages / 2,428,965 bytes, SHA-256
`6ebfad542fc2edbaafbc757bd9cb32c7dba3c00d46a2b58ea63ad3761c3b9385`.
The final log is 104,268 bytes, SHA-256
`512967c69e5f5b8972479f05b2969794997b8f27f81333a737541c50ffcab8b5`.
It contains zero undefined references, multiply-defined labels, rerun
warnings, missing-character warnings, undefined control sequences,
LaTeX/package errors, fatal errors, or emergency stops. The 15 overfull
horizontal boxes are inherited outside U414; there are zero overfull vertical
boxes.

Physical pages 228–229 were rendered at 144 dpi and visually inspected. U414
on page 228 is centered, readable, properly spaced, and unclipped; the
corollary, formulas, hyperlink, and page boundary are intact. Page 229 begins
the exact next untranslated subsection without overlap. The render PNGs were
removed after inspection. The integration PDF remains transient build
evidence and is not a replacement for the verified U397 reader release.

Next exact boundary: frozen source raw line 5132 / live target raw line 5146,
the Parseval-theorem subsection.
