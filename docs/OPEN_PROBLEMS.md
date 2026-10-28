# Open problems and next research frontier

The project is deliberately not presented as complete. This document orders the unresolved problems by current scientific leverage.

## 1. Execute Stage B2 and determine the exact depth-five hitting time

Current rigorous interval:

\[
\boxed{186\le\tau_5\le212.}
\]

GLOBAL-TRAP-CUT-088 Stage A classified every first divergence before the exact Bellman suffix and excluded all hits through time 185. The remaining exact question is binary:

- find a portal in one of the complete level envelopes at times 186–211; or
- prove no hit through 211, yielding \(\tau_5=212\).

The certified input checkpoint at time 185 has 2,462,600,671 states in 128 buckets. Its identity is fixed by `data/stage_b2/`, but the raw 19.7 GB payloads are not stored in this lightweight repository.

The immediate material task is therefore:

1. recover or mount the exact 128 payloads;
2. validate every SHA-256 and the total state count;
3. run the transactional external-memory pipeline in `scripts/stage_b2/`.

Serial one-parent-at-a-time closure is no longer the preferred strategy.

## 2. Infinite-family trap theorem

The finite atlases show many terminal-relative recurrent structures, but a finite census is not a global theorem.

Target result:

> identify arithmetic conditions on denominators, radix cycles, and \(S_B\)-couplings that generate infinite families of traps.

A successful theorem should explain the SCC families rather than merely enumerate them.

## 3. Basin classification

Given a finite trap \(F\), characterize the rational states whose admissible descendants are forced into \(F\) or terminal components before reaching a specified portal.

This would convert trap discovery into a global pruning theorem.

## 4. Hidden Farey/\(p\)-adic control

The project contains exact evidence that visible portal height is not a sufficient value coordinate and that additional Farey/\(p\)-adic information can alter future control decisions.

Target result:

> identify a minimal Markov-complete arithmetic state augmentation, or prove lower bounds on the information required.

## 5. Base-\(B\) universality

The symbolic framework is defined for general integer \(B\), but the strongest theorems remain concentrated in the decimal benchmark.

Questions include:

- Which bases exhibit robust nonnesting?
- Which prime factorizations promote finite traps?
- How do reduction ledgers depend on \(v_p(B)\)?
- Are there base-dependent universality classes?

The U5-HD/ODT campaigns are experimental side branches and do not modify the RGΦ canon without their own promotion gates.

## 6. Threshold phase diagram

For fixed base and seed, classify all critical \(\kappa\) values at which first-hit chronology or optimal precursor identity changes.

The current Paper I robustness interval is one exact cell of a broader phase diagram.

## 7. Asymptotics

Determine whether \(\tau_m\) has a stable growth law, subadditive structure, or regime-dependent scaling. The presently closed depths are insufficient for a defensible asymptotic theorem.

## 8. Contextual algebraic structure

The local prime-wise modes form Boolean blocks with a natural complement. It remains open whether the global pasted structure is best formalized as an orthomodular poset, an orthoalgebra/effect algebra, or another partial algebraic structure.

No global orthomodular-lattice claim is made.

## 9. Independent replication

A clean-room implementation by a researcher who did not participate in the original code development is a priority before stronger computer-assisted claims are submitted.

## 10. Literature closure

Before high-tier journal submission, complete:

- MathSciNet and zbMATH citation chaining;
- current journal and arXiv searches in arithmetic dynamics and Farey/continued-fraction systems;
- specialist review of the hidden-state and trap claims;
- explicit comparison with nearby semigroup and open-dynamical-system literature.
