# Scientific status

**Canonical date:** 28 October 2026  
**Repository status:** public pre-DOI release candidate  
**Primary manuscript:** *Nonnested extremal targets in a rational radix–Möbius semigroup*

This document is the authoritative boundary between **proved**, **finite exhaustive**, **large computer-assisted**, **open**, **superseded**, and **experimental-isolated** statements in the repository.

## 1. Canonical mainline

For integer \(B\ge2\),

\[
T_B(x)=\{Bx\},\qquad
H(x)=\frac1{1+x},\qquad
S_B=H\circ T_B\circ H^{-1}.
\]

For reduced \(x=a/b<1\),

\[
q(x)=\frac{b}{b-a},
\qquad
P_m(B,\kappa)=\{x:q(x)>\kappa B^m\}.
\]

The benchmark jurisdiction is \(B=10\), seed \(17/19\), threshold coefficient \(\kappa=11\).

## 2. Closed symbolic results

The branch matrices are

\[
M_{T_B}(d)=\begin{pmatrix}B&-d\\0&1\end{pmatrix},
\qquad
M_{S_B}(d)=\begin{pmatrix}1&0\\-(B-1+d)&B\end{pmatrix},
\]

both with determinant \(B\).

For the seed family \(x_{N,r}=N/(N+r)\), if \(s\equiv Br\pmod N\), then

\[
S_B(x_{N,r})=\frac{N}{N+s}.
\]

For reduced \(a/q\),

\[
\operatorname{den}(T_B^n(a/q))=\frac{q}{\gcd(q,B^n)}.
\]

## 3. Closed finite-exhaustive benchmark results

\[
\boxed{\tau_1=45,\quad\tau_2=85,\quad\tau_3=120,\quad\tau_4=162.}
\]

The first-hit states fail nested optimality at three consecutive levels:

\[
45\to87>85,\qquad85\to139>120,\qquad120\to168>162.
\]

The complete chronology is stable on

\[
\boxed{\kappa\in[10.6197,11.643),}
\]

and all three nonnesting inequalities persist on

\[
\boxed{\kappa\in[10.6197,11.01).}
\]

## 4. Finite modular traps

The canonical set

\[
C_8=\left\{1/13,3/13,4/13,5/11,6/11,9/13,10/13,12/13\right\}
\]

is forward-invariant modulo the terminal set, with maximum portal height 13. Hence

\[
\boxed{V_5(7/260)=\infty.}
\]

The exact denominator-bound-500 atlas contains:

- 76,094 nonterminal states;
- 109,254 directed nonterminal edges;
- 23,176 SCCs;
- 153 SCCs closed modulo the terminal set;
- 1,502 exact finite forward-invariant closures.

These counts certify the finite atlas only; they are not a global trap-classification theorem.

## 5. Current depth-five status

The exact upper witness reaches

\[
\frac{1350416}{1350417}
\]

at time 212.

The current rigorous interval is

\[
\boxed{186\le\tau_5\le212.}
\]

The exact Bellman ladder on the certified witness suffix is

\[
\boxed{V_5(x_t)=212-t,\qquad89\le t\le212.}
\]

The repository does **not** currently claim \(\tau_5=212\).

## 6. Global trap-cut program

Stage A classified the first 89 divergences:

- 23 inadmissible branches;
- 4 immediate terminal branches;
- 3 finite-trap basins;
- 59 unresolved bulk branches under the \(D=10{,}000\) cut;
- exact search completed through time 185.

The binding gate is **RGΦ–GLOBAL–TRAP–CUT–088 Stage B2**. It requires the verified checkpoint at time 185 and propagation through times 186–211.

Binding outcomes:

- `HIT`: produces a witness shorter than 212;
- `NO_HIT through 211`: proves \(\tau_5=212\);
- interrupted run: preserves checkpoint, residual frontier, and hashes without a scientific conclusion beyond the completed horizon.

Stage B2 is not considered executed without the verified checkpoint and its bucket hashes.

## 7. Hidden-state program

Exact evidence shows that visible portal height is not a sufficient value coordinate. Farey defects, residue classes, primitive-reduction factors, and prime-wise budgets can change future control decisions.

The hidden-state program is scientifically active but separate from the headline claim of Paper I. Stronger claims require a general theorem and a completed literature comparison.

## 8. Role of the golden ratio

The project makes no direct decimal-digit-correlation claim involving \(\phi\). The legitimate connection is operatorial and spectral:

\[
Q=\begin{pmatrix}0&1\\1&1\end{pmatrix},
\qquad Q^2=Q+I,
\]

with eigenvalues \(\phi\) and \(-\phi^{-1}\), together with an exact rational Fibonacci-renewal component.

## 9. Program topology and authority

- **RGΦ mainline — `CANONICAL_ACTIVE`**: may update canonical scientific claims.
- **Paper I — `PUBLICATION_TRACK`**: publishable independently of the exact value of \(\tau_5\).
- **RGΦ-GEN — `PARALLEL_ISOLATED`**: external generalization with preregistered holdouts.
- **Artin–Kummer — `PARALLEL_ISOLATED`**: separate arithmetic program.
- **U5-HD/HM and related branches — `EXPERIMENTAL_ISOLATED`**: abstract mathematical work with no retroactive authority over RGΦ and no physical, cosmological, or ontological promotion.

The archived U5-HD-HM gates are under `research/experimental/u5-hd-hm/`.

## 10. Superseded statements retained for genealogy

- The 217-step depth-five witness remains a valid local construction but is superseded by the 212-step witness.
- The historical lower bound 179 is superseded by the current lower bound 186.
- Historical negative and HOLD results remain preserved and may not be rescued post hoc.

## 11. Paper I boundary

Paper I may claim:

- exact system definition;
- exact first-hit times through depth four;
- three consecutive nonnesting counterexamples;
- exact robustness intervals;
- exact evidence and reproducibility protocol.

Paper I must not claim:

- a solved value of \(\tau_5\);
- a complete trap classification over all denominators;
- a completed hidden-state theory;
- physical, quantum, cosmological, or ontological implications.

## 12. Immediate priorities

1. Verify and execute Stage B2.
2. Freeze Paper I for specialist external review and pre-DOI release.
3. Separate the trusted checker from the search generator.
4. Resume preregistered RGΦ-GEN holdouts after the main checkpoint.
5. Keep U5-HD-HM mathematically bounded and experimentally isolated.
6. Preserve all refutations, abstentions, HOLD states, and superseded evidence.

See [the strategic centrum](canon/CENTRUM_2026-10-28.md) and [open problems](OPEN_PROBLEMS.md).

## 13. Integrated experimental delta archive

The audit branch integrates three later experimental results without changing
mainline RGΦ authority:

- **ODT-009**: the hierarchical architecture replicates on a second resolution
  shell; local arithmetic O5 does not replicate; a narrow pentadic increment
  does not beat the strongest baseline and receives no global promotion.
- **BQ-010A**: exact obstruction to the nonadaptive root-first `4+31` route;
  the unrestricted interval remains `35 <= M_3 <= 36`.
- **HM-010**: stabilized nonsplit extension class with a nonzero bulk-to-endpoint
  boundary map; the explicit Busby/spectral/APS refinement remains open.

All three remain `EXPERIMENTAL_ISOLATED`. Their reports, claim ledgers, compact
evidence tables, source and verifiers are archived under `research/experimental/`.
Large generated tables and ZIP bundles remain release assets identified by
SHA-256 rather than ordinary Git blobs.
