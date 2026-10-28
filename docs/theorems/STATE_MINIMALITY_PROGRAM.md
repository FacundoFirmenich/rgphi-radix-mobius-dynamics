# Hidden-state minimality — formal program

## Future equivalence

For admissible histories `h_1,h_2`, define `h_1 ≡ h_2` iff for every future control word `w`:

- `w` is admissible after `h_1` iff it is admissible after `h_2`;
- the resulting portal-entry vector and Bellman costs coincide.

This is a right congruence. Its quotient is the minimal deterministic future controller in the Myhill–Nerode sense.

## RGΦ question

Determine whether the tuple

`(rational state, Farey-neighbor shadow, e_2, e_5, sparse phase/holes)`

is sufficient to identify the quotient class. If sufficient, prove it. If not, construct two histories with the same tuple and different futures.

## Minimality target

Show that removing any one coordinate merges two inequivalent histories, or establish an information lower bound on every sufficient encoding.

## Current evidence

- Target depth alone fails.
- Current height fails.
- Short height lookahead fails.
- Rational state plus prime budgets alone fails in non-pure contexts.
- A corrected exact representation uses antichain hull, sparse holes and phase.

These are lower-bound witnesses, not yet a sufficiency theorem.
