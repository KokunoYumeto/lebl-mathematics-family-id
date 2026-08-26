# R006 Stone–Weierstrass polynomial approximation in C^k — U306

Status: **PASS; translated and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.stone-weierstrass.exercises.polynomial-approximation-in-c-k-norm`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4141–4161 inclusive; 21 LF-terminated lines, 701 bytes, SHA-256 `57513aab0a4ea4bf34dd6b75deb825ecef9006b76ed554afc290477d4db98909`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4148–4168 inclusive; 21 LF-terminated lines, 701 bytes, SHA-256 `645e63faeb096756e388cd32503e8d7b16ddb4041d563fa50031067b5fa06b7d`.
- Full target after U306: 194,044 bytes, 5,480 LF lines, SHA-256 `3952280117059464b331e63547627c5e432dfa013a1642504182f8afb09ce552`.

## Mathematical and structural QA

- Ordered TeX controls: 35 source / 35 target, exact.
- Ordered environments: six exact events: one `exercise` pair, one `enumerate` pair, and one `equation*` pair.
- List topology: two `\item` entries on both sides.
- Ordered inline mathematics: 11 payloads, byte-identical after whitespace normalization.
- Display mathematics preserves the exact derivative sum, bounds, norm subscripts, and limit; only the prose node `\text{as}` is localized as `\text{ketika}`.
- Braces: 20 opening / 20 closing on each side, balanced.
- Exercise state: one exercise, no label, no source hint, no `\exsol`, and no invented answer or solution.

Both parts retain their exact mathematical force: polynomial approximation of a continuously differentiable complex-valued function in the `C^1` norm, followed by the order-`k` result in the `C^k` norm with the displayed sum of derivative errors. The source is coherent, so no mathematical correction is required.

## Indonesian QA and terminology

Independent mathematical and language review passed without correction. Established `diferensiabel secara kontinu` (`LEBL-TERM-0247`) and `diferensiabel secara kontinu hingga orde k` (`LEBL-TERM-0480`) are preserved. New entry `LEBL-TERM-0760` admits `norma C^k`, with `C^1` as its `k=1` instance. Spreadsheet import, exact-row inspection, formula-error scan, XLSX export, reinspection, and two-panel visual QA pass. The 760-row ledger is 115,790 bytes with SHA-256 `f9e5f6fa14972e139fed5c0d4afbd6a1d2ee20c3f16d0131e1617d26621e31c1`. There is no reader-facing English residue, mojibake, or solution leakage.

## O001 and cursor

`LEBL-O001-R006-0019` records the no-hint/no-solution source state. The next contiguous source boundary is raw line 4163, and the target boundary is raw line 4170, at the two-part exercise on uniformly approximating even and odd functions by polynomials of matching parity.
