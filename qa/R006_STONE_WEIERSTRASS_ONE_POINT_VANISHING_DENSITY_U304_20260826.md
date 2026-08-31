# R006 Stone–Weierstrass one-point-vanishing density exercise — U304

Status: **PASS; translated and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.stone-weierstrass.exercises.one-point-vanishing-algebra-density`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4122–4131 inclusive; 10 LF-terminated lines, 449 bytes, SHA-256 `ca040b3df79788014a0ebbb49d4a9dd5cec336668fb2573dc0d4fca977586959`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4129–4138 inclusive; 10 LF-terminated lines, 549 bytes, SHA-256 `3e9e3ab0ca7e323c368765bc4f1d02de6856fb237a4a5a1e87b6769e9fc3bbf4`.
- Full target after U304: 194,012 bytes, 5,480 LF lines, SHA-256 `bc2ae019708aea08b4274c92216639957e3311fe2618219054d8fc86d7dbb163`.

## Mathematical and structural QA

- Ordered TeX controls: 20 source / 20 target, exact.
- Ordered environments: one exact `exercise` pair.
- Ordered inline mathematics: 11 payloads, byte-identical after whitespace normalization.
- Braces: three opening / three closing on each side, balanced.
- Exercise state: one exercise, no label, no source hint, no `\exsol`, and no invented answer or solution.

The translation preserves every quantifier and the common-zero-set meaning: every `f \in \sA` vanishes at `x_0`, whereas for each `y \ne x_0` there is some `\varphi \in \sA` that is nonzero at `y`. It also preserves point separation and the conclusion that every continuous real-valued function vanishing at `x_0` is a uniform limit of functions from `\sA`. The source is coherent, so no mathematical correction is required.

## Indonesian QA and terminology

Independent mathematical and language review passed without correction. The phrase `semua fungsinya bernilai nol secara serentak tepat di satu titik` states the joint-vanishing condition without implying that each member has no other zeros; the following quantified sentences make the condition explicit. Established choices `memisahkan titik-titik` and `limit seragam` are used consistently. No new terminology row is required. There is no reader-facing English residue, mojibake, or solution leakage.

## O001 and cursor

`LEBL-O001-R006-0017` records the no-hint/no-solution source state. The next contiguous source boundary is raw line 4133, and the target boundary is raw line 4140, at the exercise on distance functions lying in the closure of a real algebra.
