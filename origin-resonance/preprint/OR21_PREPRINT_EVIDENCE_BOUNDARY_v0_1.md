# OR-21: Radial monodromy and thermodynamic rigidity — preprint v0.1

Date: 2026-11-11. Status: BRANCH-LEVEL EXACT DERIVATIONS; NOT EXTERNALLY REFEREED.

## Provenance
- Canonical input `main` commit `5b9c424c2749de16f3d3246dc20607a106a76774`.
- Origin–Resonance input commit `188ac5db3c2021cd15b65f8d9b6f4bfc3123a928`.
- Paper: `Origin_Resonance_Radial_Monodromy_v0_1.tex` and compiled 10-page PDF.
- Executable finite witness checker: `verify_resonance_preprint.py` plus JSON receipt.

## New exact branch derivations
1. For finite, closed, strongly connected high RGΦ components, permutation of both generators iff every edge has unit content iff every directed closed walk has Delta=1 iff the edge log-content is a vertex coboundary. Failure of these is equivalent to a strictly positive radial monodromy on some simple cycle.
2. On a fixed strongly connected labelled graph, equality of all closed-path content products for two positive rational decorations is equivalent to a rational vertex gauge `d'_e=d_e*a_target/a_source`; transfer matrices are diagonally similar for all real parameters.
3. For `L(t)[i,j]=sum_{e:i->j} d_e^t`, with `P(t)=log rho(L(t))` and two outgoing labelled edges, `P(0)=log 2`, and `P'(0)=sum_i(pi_i/2)*sum_g log(d_g(i))`, where `pi` is the rational stationary distribution of `L(0)/2`. The component is nonpermutation iff `P'(0)>0` iff `P(t)>log 2` for all `t>0`.
4. The prime-valuation vector `(v_p(Delta))_{p|B}` is additive; normalized periodic share `alpha=log Delta/(m log B)` is rational iff the valuations of `Delta` and `B` are rationally proportional. Every prime-power-base periodic share is rational.
5. Minimum and maximum periodic log pitch per edge are attained on simple cycles, and candidate comparisons can be exact with integer powers.
6. Using the canonical bound `d<2^floor(n/2)` and `d|B`, if the least prime factor of `B` is at least `2^floor(n/2)` then every closed SCC of cardinality at most n is permutation. Nonpermutation n=5 requires 2 or 3 dividing B; n=6 requires one of 2,3,5,7 dividing B.
7. For canonical five-state progression `B_n=88011536665779+n*223336848698040`, `L(t)` has the symbolic polynomial `lambda^5-lambda^4-4lambda^3+3lambda^2+3lambda-1-(lambda-1)*3^t`; stationary vector `(2/7,3/14,1/7,1/14,2/7)`; mean `P'(0)=log(3)/28`; second cumulant `P''(0)=3(log 3)^2/112`. Simple cycle extrema are 0 and log(3)/4 per step. The maximum normalized share `log(3)/(4 log(B_n))` tends to zero although nonpermutation and unnormalized pressure derivative persist. At n=0 the maximal periodic share is irrational.

## Evidence and non-contamination
- Proofs in the LaTeX manuscript. Standalone checker reproduces exact five-state transitions at n=0,1,2; six abstract simple cycles; stationary fractions; determinant polynomial (SymPy cross-check); B=19 permutation control.
- Known finite audit B=2..40 n<=5: 890,417 candidate states, 16 closed components, all permutation. Separately archived RC2 B=2..17: 82,387 candidates, four closed components. These are bounded, not global.
- No OR-4, OR-5, or OR-19 preregistered endpoint adjudicated; 19 elliptic curves remain a uniform open jurisdiction. F17 positive-rank lower bound does not complete the rank/torsion profile; F19 admissibility and coprime-integral points remain open.
- No identification of log content or alpha with the general hyperaccess concept; no physical helical claim. Golden conjugacy and dual one-ninth stay existing derived/built-in structures, not independent evidence.
- No canonical claims reinterpreted or promoted. Novelty beyond known literature not independently established. Intended for adversarial review prior to preprint submission.