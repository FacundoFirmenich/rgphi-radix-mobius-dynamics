# Open problems and next research frontier

The project is deliberately not presented as complete. This document lists the highest-value unresolved problems.

## 1. Exact depth-five hitting time

Current rigorous interval:

\[
179\le\tau_5\le212.
\]

The correct objective is either:

- prove \(\tau_5=212\), or
- produce a shorter exact witness.

Serial one-parent-at-a-time Bellman closure is not considered the preferred strategy. The active structural alternatives are first-divergence cuts, trap/basin elimination, and meet-in-the-middle constructions.

## 2. Infinite-family trap theorem

The denominator-\(\le500\) atlas shows many finite structures, but a finite census is not a global theorem.

Target result:

> identify arithmetic conditions on denominators, radix cycles, and \(S_B\)-couplings that generate infinite families of terminal-relative traps.

A successful theorem should explain, not merely enumerate, the observed SCC families.

## 3. Basin classification

Given a finite trap \(F\), characterize the set of rational states whose admissible descendants are forced into \(F\) or terminal components before reaching a specified portal.

This would convert trap discovery into a global pruning theorem.

## 4. Hidden Farey/\(p\)-adic control

The project contains strong exact evidence that two histories reaching the same visible rational state can have different future controls when additional Farey/\(p\)-adic information is retained.

Target result:

> identify a minimal Markov-complete arithmetic state augmentation, or prove lower bounds on the information required.

## 5. Base-\(B\) universality

The symbolic framework is defined for general integer \(B\), but the strongest finite theorems are currently concentrated in the decimal benchmark.

Questions:

- Which bases exhibit robust nonnesting?
- Which prime factorizations promote finite traps?
- How do reduction ledgers depend on \(v_p(B)\)?
- Are there base-dependent universality classes?

## 6. Threshold phase diagram

For fixed base and seed, classify all critical \(\kappa\) values at which first-hit chronology or optimal precursor identity changes.

The current Paper I interval is one exact cell of a broader phase diagram.

## 7. Asymptotics

Determine whether \(\tau_m\) has a stable asymptotic growth law, subadditive structure, or regime-dependent scaling.

At present the available depths are insufficient for a defensible asymptotic theorem.

## 8. Contextual algebraic structure

The local prime-wise modes form Boolean blocks with a natural complement. It remains open whether the global pasted structure is best formalized as:

- an orthomodular poset;
- an orthoalgebra/effect algebra;
- another partial algebraic structure.

No global orthomodular-lattice claim is made.

## 9. Independent replication

A clean-room implementation by a researcher who did not participate in the original code development is a priority before stronger computer-assisted claims are submitted.

## 10. Literature closure

Before high-tier journal submission, the project should complete:

- MathSciNet and zbMATH citation chaining;
- recent arXiv/ journal searches in arithmetic dynamics and continued-fraction/Farey systems;
- specialist review of the hidden-state and trap claims;
- explicit comparison with nearby open-system and semigroup literature.
