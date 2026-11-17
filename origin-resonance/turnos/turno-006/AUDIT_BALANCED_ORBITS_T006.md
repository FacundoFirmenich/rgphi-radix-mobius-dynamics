# Turno 006 independent audit — balanced six-letter orbit jurisdiction

**Date:** 2026-11-17. **Authority:** isolated Origin–Resonance branch only.
**Disposition:** `AUDIT_HOLD` for the claim that three balanced *necklaces*
exhaust oriented six-state Hamiltonian words; no canonical assertion is altered.

For a binary word of length six containing exactly three `T` and three
`S` symbols, there are `binom(6,3)=20` marked words.
The action of the cyclic group `C_6` has four orbits, represented by

- `TTTSSS` (orbit size 6);
- `TTSTSS` (orbit size 6);
- `TTSSTS` (orbit size 6);
- `TSTSTS` (orbit size 2).

Burnside's lemma gives `(20+2+2)/6=4` necklaces. The middle two
are mutually reflected, **not cyclic rotations**. The action of the
dihedral group, which also permits reversing word order, instead has
three *bracelet* classes. The Turno-006 file
`SIX_STATE_BALANCED_SKELETONS_T006.md` enumerates these three
bracelets but calls them necklaces.

**Crucial jurisdictional distinction.** A directed, `T/S`-labelled
Hamiltonian cycle is normally identified under orientation-preserving
rotation, not reflection. Merely having `S=H T H^{-1}` supplies no theorem
that reversing the directed cycle, or interchanging `T` and `S`,
preserves the claimed high-defect component class. Any nonstandard
quotient must be specified and proved before the number `2160` is
certified as a complete oriented count.

If the stated `720` back-edge completions apply independently to
**each** of the four rotation classes, the corresponding formal
per-necklace product is `4*720=2880` and the four-defect decoration
product is `4*2880=11520`. These are **conditional recalculations**,
not certified counts of distinct arithmetically realizable components:
the marked-source quotient, periodicity and graph equivalence still
require an explicit audit. In particular, multiplying uniformly by
six to obtain a raw count deserves separate treatment for the
period-two alternating word.

The conditional `DUAL_TRIAD` exclusion based on directed distance five
and the word-level `ALTERNATING_HEXAGON iff TSTSTS` characterization
are not negated by the missing word class. The previously published
`720 of 2160` and `2160/8640` totals, however, must not be treated
as independently closed exhaustive rotational classifications.

**Checker:** `check_balanced_necklace_orbits_T006.py` independently
enumerates all 20 balanced words, computes both group orbit spaces
and fails closed against the existing three-row table.

Preserve the original Turno-006 text, numerical claims, negative
results and post-hoc labels as historical records. Mark the
exhaustiveness claim `AUDIT_HOLD_ORIENTATION_QUOTIENT` in the live
resonance ledgers until a formal equivalence and a corrected
exhaustive catalogue are established. No result here is promoted to
canonical `main`.
