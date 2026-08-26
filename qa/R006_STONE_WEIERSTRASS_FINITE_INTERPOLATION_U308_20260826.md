# R006 Stone–Weierstrass finite-point interpolation exercise — U308

Status: **PASS; translated, source defect repaired, and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.stone-weierstrass.exercises.finite-point-interpolation`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4178–4197 inclusive; 20 LF-terminated lines, 835 bytes, SHA-256 `6800527510a6193254939334c8957f869ae7158bbb419478554a6db4de19e462`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4185–4205 inclusive; 21 LF-terminated lines, 1,012 bytes, SHA-256 `bffb3bef2a4162831f6c7aa8975c511230e2f021a20500f4efda8553b240f855`.
- Full target after U308: 194,239 bytes, 5,481 LF lines, SHA-256 `f78bb158c48d33deb40424c18855a369ded1122929cdbc532de9d389c28e0fdc`.

## Mathematical and structural QA

- Ordered TeX controls in the unmodified comparison: 30 source / 30 target after removing the repair sentence; exact.
- Ordered environments: four exact events: one `exercise` pair and one `enumerate` pair.
- List topology: two `\item` entries on both sides.
- Explicit linebreak: one on both sides.
- Original ordered inline-math payloads: 17, byte-identical after removing the repair sentence; the repair adds exactly one explicit point-list payload.
- Label `exercise:finitelymanyweierequal` is exact.
- Braces: 11 opening / 11 closing on each side; dollar delimiters balanced (36/36 in the target).
- Exercise state: one source hint, one target `Petunjuk`, no `\exsol`, and no invented answer or solution.

## Source correction

The source's part (b) does not state that the interpolation points are pairwise distinct, yet its hint claims the product omitting index `\ell` is nonzero at `x_\ell`. That claim fails when points repeat. Adverse event `LEBL-ID-ADV-0256` records this high-confidence defect. The target adds the minimal qualification: `Setelah membuang titik-titik yang berulang, andaikan $x_1,x_2,\ldots,x_k$ berbeda sepasang-sepasang.` Repeated points can be discarded because their prescribed values are identical; under pairwise distinctness the displayed product has the claimed zero/nonzero behavior. No other mathematical content changes.

## Indonesian QA and terminology

Independent mathematical and Indonesian-language review passed without correction. Established interpolation terminology (`LEBL-TERM-0748`) is used consistently, and the repair sentence is natural and explicit. There is no reader-facing English residue, mojibake, or solution leakage.

## O001 and cursor

`LEBL-O001-R006-0021` records the source's hint-present/no-solution state. The next contiguous source boundary is raw line 4201, and the target boundary is raw line 4209, at the Section 11.7 Fourier-series heading and trigonometric-polynomial subsection opening.
