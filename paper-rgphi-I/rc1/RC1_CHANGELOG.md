# RGΦ I RC1 — changelog

## Mathematical corrections

- Added the four-state normal-form lemma and a symbolic global-strict-edge uniqueness lemma.
- Expanded strict-`T` and strict-`S` forced-edge proofs.
- Added quotient formulae, interval bounds, gcd and parity justifications.
- Made the ambient system explicitly partial.
- Replaced an imprecise quasi-affine formulation by exact arithmetic realization conditions.

## Canonical consistency

- Normalized all five-state artifacts to `T=[1,0,3,2,4]`, `S=[4,2,1,0,0]`, strict `S_3:x_3->x_0`.
- Added a literal cross-artifact consistency checker.
- Corrected the spectral certificate labelling.

## Literature and classification

- Corrected primary MSC `37P25` to `37E05` and added `11A07`.
- Added nearest-neighbour references on Möbius number systems and `×b`-invariant sets.
- Corrected the description of `Phi`.

## Reproducibility and build

- Removed the toy finite-type checker and unsupported minimality output.
- Added `make verify`, `make pdf`, clean-room simulation and PDF preflight.
- Corrected BibTeX order and removed a false theorem-dependency arrow.
