# Scientific status

**Canonical date:** 29 October 2026  
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

The exact multiscale atlas contains:

| D | states | edges | SCCs | closed SCCs | safe SCCs | safe states |
|---:|---:|---:|---:|---:|---:|---:|
| 500 | 76,094 | 109,254 | 23,176 | 153 | 1,502 | 1,624 |
| 2,500 | 1,899,856 | 2,735,455 | 565,564 | 248 | 5,483 | 5,933 |
| 5,000 | 7,600,436 | 10,944,352 | 2,255,011 | 314 | 9,672 | 10,418 |
| 10,000 | 30,397,464 | 43,771,910 | 9,009,037 | 467 | 17,094 | 18,472 |

The denominator-10,000 audit is exact and bounded. It does not constitute a
global theorem that every finite trap occurs below this denominator. The
modular-skeleton theorem characterizes the anatomy of finite traps; a fully
parameterized unbounded family theorem remains open.

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

Stage A classified all 89 first divergences:

- 23 inadmissible branches;
- 4 immediate terminal branches;
- 3 exact finite-trap basins;
- 59 residual bulk branches after the \(D=10{,}000\) cut.

The exact joint search contains no depth-five hit through time 185. The
first-arrival phase reached 932,586,690 unique states through time 171; the
complete level envelope ends at time 185 with 2,462,600,671 states. The compact
Stage A evidence, exact source and independent checker are now integrated under
`data/stage_a/`, `scripts/stage_a/`, and `docs/stage_a/`.

The binding gate is **RGΦ–GLOBAL–TRAP–CUT–088 Stage B2**. It requires the verified checkpoint at time 185 and propagation through times 186–211.

Binding outcomes:

- `HIT`: produces a witness shorter than 212;
- `NO_HIT through 211`: proves \(\tau_5=212\);
- interrupted run: preserves checkpoint, residual frontier, and hashes without a scientific conclusion beyond the completed horizon.

Stage B2 is not considered executed without the verified 19.7 GB checkpoint payload and its 128 bucket hashes.

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
- **U5-HD/HM, EO, ODT, BQ, OMNI and HDH — `EXPERIMENTAL_ISOLATED`**: abstract or empirical research with no retroactive authority over RGΦ and no automatic physical, cosmological or ontological promotion.

The experimental genealogy is under `research/experimental/`.

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

1. Locate, verify and execute the exact Stage B2 checkpoint.
2. Freeze Paper I for specialist external review and pre-DOI release.
3. Publish Stage A, Stage B2 and experimental bundles as citable release assets.
4. Complete independent clean-room replication.
5. Prove an unbounded theorem-family for modular traps or a minimal sufficient hidden state.
6. Continue HDH-014 only under its preregistered experimental boundary.
7. Preserve all refutations, abstentions, HOLD states, and superseded evidence.

See [the strategic centrum](canon/CENTRUM_2026-10-28.md), [Stage A status](STAGE_A_STATUS_2026-10-28.md), and [open problems](OPEN_PROBLEMS.md).

## 13. Integrated experimental archive

The archive includes, without mainline promotion:

- **ODT-008/009**: resolution-dependent support, hierarchical architecture,
  replication failure of O5, and no global U5 promotion;
- **BQ-009/010A**: exact 31-symbol signed-permutation optimum and no-go of the
  nonadaptive root-first `4+31` route; unrestricted `35 <= M_3 <= 36` remains open;
- **HM-001…010** and **EO-001**: local atlas, holonomy, higher cocycles, and
  stabilized nonsplit interface;
- **OMNI-002…008**: composite formal/provenance lineage;
- **HDH-013**: exact full-kernel Schur/Kron RG closure, exact composition and
  Green restriction, together with refutation of scalar spectral closure on
  defective holdouts. HDH-014 is preregistered and open.

All remain `EXPERIMENTAL_ISOLATED`. Large generated tables and ZIP bundles are
release assets identified by SHA-256 rather than ordinary Git blobs.
