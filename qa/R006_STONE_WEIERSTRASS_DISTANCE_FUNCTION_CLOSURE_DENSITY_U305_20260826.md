# R006 Stone–Weierstrass distance-function closure density exercise — U305

Status: **PASS; translated and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.stone-weierstrass.exercises.distance-functions-in-closure-imply-density`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4133–4139 inclusive; seven LF-terminated lines, 300 bytes, SHA-256 `d7797303820c3963151c1805a56c86f4e58e60e5a597975c88a19a6d9e36d69d`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4140–4146 inclusive; seven LF-terminated lines, 332 bytes, SHA-256 `bf642a667f4f4bcd4a93c0e8c5b464513a8f56f91430fe801bdfdbd3d6b1ef77`.
- Full target after U305: 194,044 bytes, 5,480 LF lines, SHA-256 `d11fb7072ae0b3dd45600a47c13dd2c2414a5d05cff4ac2e07c6a2d41386fe2f`.

## Mathematical and structural QA

- Ordered TeX controls: 13 source / 13 target, exact.
- Ordered environments: one exact `exercise` pair.
- Ordered inline mathematics: six payloads, byte-identical after whitespace normalization.
- Braces: four opening / four closing on each side, balanced.
- Exercise state: one exercise, no label, no source hint, no `\exsol`, and no invented answer or solution.

The translation preserves compactness, the at-least-two-points hypothesis, the real-algebra hypothesis, the universal quantifier over `y`, membership of each distance function in the closure, and the conclusion that the closure equals `C(X,\R)`. The source is coherent, so no mathematical correction is required.

## Indonesian QA and terminology

Independent mathematical and language review passed without correction. Established terms `fungsi jarak` (`LEBL-TERM-0323`) and `penutupan` (`LEBL-TERM-0348`) are used consistently. No new terminology row is required. There is no reader-facing English residue, mojibake, or solution leakage.

## O001 and cursor

`LEBL-O001-R006-0018` records the no-hint/no-solution source state. The next contiguous source boundary is raw line 4141, and the target boundary is raw line 4148, at the two-part exercise on polynomial approximation in the `C^1` and `C^k` norms.
