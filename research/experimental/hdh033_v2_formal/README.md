# HDH-033-V2 fresh formal replay

This project reuses byte-identical `TransportCovariance.lean` source (Git
blob `48f9bd2b1fd07c8eb090b62a311a5fe1a4e3296b`) from the already
machine-checked HDH-032 branch. The patched Paper A ancillary copy has exactly
that same blob identity; the Lean version is `4.35.0`, Mathlib is `v4.35.0`.

The CI gate compiles all theorems with `lake build --wfail` and rejects proof
placeholders. It establishes only noncommutative algebraic covariance of
hidden-block inverse and memory derivative. It does **not** formalize the new
HDH-033 conditional energy spectral bound, PDE/FEM consistency, experiments or
external replication.

Authority: `EXPERIMENTAL_ISOLATED`.
