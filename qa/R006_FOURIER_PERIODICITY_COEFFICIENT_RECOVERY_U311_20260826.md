# R006 Fourier periodicity and coefficient recovery — U311

Status: **PASS; translated, source defect repaired, and independently reverified**  
Date: 2026-08-26  
Provenance: `OpenAI Codex gpt-5.6-sol, Ultra`

## Exact bound

- Stable unit: `ra.v2.fourier-series.trigonometric-polynomials.periodicity-and-coefficient-recovery`.
- Source: `source/ra-v6.3/ch-approximate.tex`, raw lines 4260–4305 inclusive; 46 LF-terminated lines, 1,121 bytes, SHA-256 `57b0efb54f666e2a6a1f1795a95e11bfb581b9a995dbe076b17a0bed09c805dd`.
- Target: `translation/ra/ch-approximate.tex`, raw lines 4268–4313 inclusive; 46 LF-terminated lines, 1,258 bytes, SHA-256 `eb131e56a22e82f30f00bee78f7bed84f40da58d5f1e54017fc336c7d40ce61a`.

## Mathematical and structural QA

- All source formulas occur unchanged and in order. The target adds only the two explicit repair payloads `$n \neq 0$` and `$n=0$`; the ordered control stream therefore preserves all 54 source controls and adds exactly one `\neq` control.
- Environment topology is exact: ten ordered events comprising three `equation*` displays, the nested `cases` pair, and the commented `aligned` topology.
- The fourteen original inline-math payloads are byte-identical and ordered; the target has sixteen after the two repair payloads.
- All three displays are exact after normalizing only `\text{jika }` / `\text{selainnya.}` to the source-language case labels.
- All five `%mbxlatex` comments are byte-identical. Source and target each have 37 opening / 37 closing braces; target dollar delimiters are balanced at 32 / 32.
- Independent post-correction mathematical/topology audit confirms the periodicity, integer-exponential integral, orthogonality computation, coefficient recovery, zero extension, and clean unit boundary.

## Source correction

`LEBL-ID-ADV-0257` records that the source states `e^{inx}/(in)` as an antiderivative without excluding `n=0`, where that expression is undefined. The Indonesian derivative minimally says that this antiderivative formula applies for `n \neq 0` and that for `n=0` the integrand is identically one. The following definite-integral cases and every other formula remain unchanged.

## Indonesian QA, terminology, and cursor

Independent Indonesian-language review passed on the corrected snapshot with no remaining reader-facing English residue. Established terms are reused: `periodik`, `periode`, `antiturunan`, `koefisien`, and `polinom trigonometri`; no new terminology row is needed. No exercise, hint, solution, O001 gap, or asset occurs.

The next contiguous boundary begins at source raw line 4307 / target raw line 4315 with the real-valued conjugate-coefficient criterion and linear-independence propositions.

