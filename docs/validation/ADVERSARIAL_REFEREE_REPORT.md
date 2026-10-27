# Adversarial referee simulation — internal pre-review

**Status:** internal quality-control exercise; **not external validation**.

## Overall verdict

The Paper I result is coherent and potentially publishable, but a strong referee would immediately probe the exact domain of the partial generator, the terminal-set convention, the computational evidence boundary, benchmark dependence, and the priority claim.

The current repository revision resolves or explicitly scopes these objections.

## Major issue 1 — What exactly is the semigroup?

### Objection

The notation \(S_B=H\circ T_B\circ H^{-1}\) can be misleading if readers assume a total self-map on the whole unit interval.

### Resolution

The manuscript now states:

\[
D_S=H([0,1])=[1/2,1]
\]

and identifies the object as a semigroup of **partial rational transformations**. A word is admissible only when each partial generator is defined at the current state.

### Status

Resolved.

## Major issue 2 — Is the terminal set an arbitrary pruning device?

### Objection

Removing 23 states could invalidate the hitting-time theorem unless forward invariance is independently established.

### Resolution

A complete machine-readable audit now records all 23 states and all 46 attempted T/S branches. There are zero admissible escapes.

### Status

Resolved for the declared benchmark convention.

## Major issue 3 — Could the nonnesting be a threshold artifact?

### Objection

The phenomenon might disappear under an arbitrarily small perturbation of \(\kappa=11\).

### Resolution

Exact positive-width intervals are proved:

\[
[10.6197,11.643)
\]

for the full chronology and

\[
[10.6197,11.01)
\]

for simultaneous three-level nonnesting.

### Status

Resolved.

## Major issue 4 — Is “Bellman failure” overclaimed?

### Objection

Dynamic programming already requires a sufficient Markov state; showing that a compressed observable fails is not a new principle.

### Resolution

The manuscript explicitly disclaims novelty for Bellman state sufficiency. The contribution is the exact arithmetic counterexample in this semigroup and its robust quantitative structure.

### Status

Resolved by framing.

## Major issue 5 — Is nearby continued-fraction literature close enough to anticipate the claim?

### Objection

Farey/projective systems, induced maps, rational semigroup actions, finite rational orbits, and hitting-time theory are extensive.

### Resolution

The manuscript and repository now compare directly with recent work by Panti; Schmidt; Dajani–Kraaikamp–Sanderson; Berthé–Cantrell–Lee–Pollicott; Javaheri; Chen–Dajani–Hu–Kraaikamp; Fox–Garrity; and Nakada–Natsui–Thuswaldner.

The novelty language remains “we are not aware of,” not absolute priority.

### Status

Internally resolved; external specialist priority check still required.

## Major issue 6 — Can the 329-million-state layer claim be trusted?

### Objection

A massive enumeration is not made trustworthy merely by publishing a CSV summary.

### Resolution

The project uses exact arithmetic, deterministic state semantics, source code, CI, compact independent search kernels, claim/evidence mapping, and clean-room replication targets.

### Remaining gap

A third-party clean-room reimplementation has not yet reproduced the main finite chronology.

### Status

Open external-validation item.

## Major issue 7 — Benchmark specificity

### Objection

A single seed/base/terminal convention may have limited theoretical significance.

### Resolution

The symbolic system is base-\(B\), and the threshold is parameterized. Paper I explicitly limits its finite theorem to the benchmark and treats family-level generalization as open.

### Status

Acceptable for a first experimental/arithmetic dynamics paper; a family theorem would substantially raise the ceiling.

## Major issue 8 — Why should a dynamics journal care?

### Positive case

The manuscript supplies:

- a clean partial semigroup;
- exact extremal hitting times;
- a robust failure of nested optimality;
- explicit arithmetic mechanisms;
- reproducible finite evidence.

### Risk

Without external specialist confirmation, the result may be judged too computational or too benchmark-specific for a top dynamics venue.

### Recommendation

Seek specialist feedback before DOI freeze and journal submission.

## Internal recommendation

Proceed to external review. Do not expand Paper I with the entire hidden-state or trap program; use those as separate papers.
