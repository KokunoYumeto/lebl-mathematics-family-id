# R006 exponentially decaying sine-series smoothness exercise — U426

Status: **PASS**  
Date: 2026-08-29  
Runtime provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact contiguous boundary

- Stable unit ID:
  `ra.v2.fourier-series.exercises.exponentially-decaying-sine-series-smoothness`.
- Frozen source: `source/ra-v6.3/ch-approximate.tex` raw lines 5407–5413,
  seven LF-terminated lines / 163 bytes, SHA-256
  `e85f6f5ad566c4f41aebcbaf37528bf0918a24f371a279d027ce2254b11c8270`.
- Indonesian target: `translation/ra/ch-approximate.tex` raw lines 5421–5427,
  seven LF-terminated lines / 182 bytes, SHA-256
  `e6a529ed4843e1e1652e6481cd87977ed759518308ba9505f0e037c8cac8f5f9`.
- Full target after translation: 198,142 bytes, SHA-256
  `9d0626aa2c1d8cbee2c6740acef767a8e0a4726ca841239c823c6b626e17b993`.
- The exact next untranslated boundary follows blank source line 5414 /
  target line 5428. The next labeled exercise begins at source raw lines
  5415–5426 / target raw lines 5429–5440 and remains untouched.

The admitted unit is one complete unlabeled exercise. It asks the reader to
show that the displayed exponentially decaying sine series converges to an
infinitely differentiable function.

## Mathematical, structural, and source QA

The statement is mathematically coherent. For every derivative order `k`,
termwise differentiation is justified because the differentiated coefficients
are bounded by `n^k e^{-n}`, whose sum converges. Uniform convergence of each
derivative series gives a `C^\infty` limit, so the Indonesian phrase
`diferensiabel tak berhingga kali` preserves the source claim. No source
correction or adverse-ledger event is warranted.

Automated and independent comparison found the exact ordered seven-command
stream (`\\begin`, `\\begin`, `\\sum`, `\\infty`, `\\sin`, `\\end`,
`\\end`), four environment events, the exact display-math payload, six
opening and six closing braces, and zero dollar delimiters. There are no
labels, references, citations, comments, footnotes, assets, or hidden
solution material. Every mathematical token is byte-identical between source
and target; only the two reader-facing English sentences are translated.

## Indonesian-language, terminology, manifest, and O001 QA

The wording uses natural formal Indonesian: `Tunjukkan bahwa`, `konvergen ke
suatu fungsi`, and the established formal term `diferensiabel tak berhingga
kali` (LEBL-TERM-0255). No new terminology row is needed. An independent
mathematical, Indonesian-language, structural, and terminology audit passed.

The source supplies no hint and no solution. O001 gap
`LEBL-O001-R006-0031` records the missing solution without inventing an answer,
proof, or explanatory text. The exercise's displayed series is the complete
source support; it is not promoted to a detachable hint.

The deterministic backend, integration build, and visual reader checks were
performed after the manifest and O001 rows were admitted; their closure is
recorded by the companion U426 backend receipt and the live controls.

## Recovery

Continue at source raw line 5415 / target raw line 5429 with the labeled
`exercise:fsdiffmindecay` unit. Preserve R007 and R008 cursors, the public U425
source and controls commits, the U397 reader release, and the finalized U425
receipt. No author contact or upstream issue is allowed before all three
assigned books are complete.
