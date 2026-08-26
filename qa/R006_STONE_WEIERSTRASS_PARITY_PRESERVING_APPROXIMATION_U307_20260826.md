# R006 Stone–Weierstrass parity-preserving polynomial approximation — U307

Status: **PASS; translated and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.stone-weierstrass.exercises.parity-preserving-polynomial-approximation`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4163–4176 inclusive; 14 LF-terminated lines, 492 bytes, SHA-256 `2e802d0c96f6ec88c31b4b6668c7330bc8c1fd9e2224d277fc2abfd4a74afab9`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4170–4183 inclusive; 14 LF-terminated lines, 510 bytes, SHA-256 `eaf2f7ac102cc614fe73b506c4ab648479b52f3dec176f5abd87249b8dd7e00e`.
- Full target after U307: 194,062 bytes, 5,480 LF lines, SHA-256 `743a0297b26bf548a4981d45d9a2e38121e7ec2e0890bd740adc1afd97507f7d`.

## Mathematical and structural QA

- Ordered TeX controls: 16 source / 16 target, exact.
- Ordered environments: four exact events: one `exercise` pair and one `enumerate` pair.
- List topology: two `\item` entries on both sides.
- Ordered inline mathematics: four payloads, byte-identical after whitespace normalization.
- Braces: six opening / six closing on each side, balanced.
- Exercise state: one exercise, no label, no source hint, no `\exsol`, and no invented answer or solution.

The first part preserves uniform approximation of an even function by polynomials containing only even powers, through terminal exponent `2k`. The second preserves the odd analogue, through terminal exponent `2k-1`. The source is coherent, so no mathematical correction is required.

## Indonesian QA and terminology

Independent mathematical and language review passed without correction. Established `fungsi genap` (`LEBL-TERM-0285`) and `fungsi ganjil` (`LEBL-TERM-0284`) are used consistently. No new terminology row is required. There is no reader-facing English residue, mojibake, or solution leakage.

## O001 and cursor

`LEBL-O001-R006-0020` records the no-hint/no-solution source state. The next contiguous source boundary is raw line 4178, and the target boundary is raw line 4185, at the labeled two-part exercise on polynomial approximation while interpolating finitely many prescribed values; the source includes one hint.
