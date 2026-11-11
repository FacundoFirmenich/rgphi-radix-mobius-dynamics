# P2 PRIME-004 external-runner replication

This isolated branch contains a standalone C++17 reimplementation of the new P2-04 theorem audit.

It checks:

- every residue for the power-of-two Bellman-alignment family at `B=8,...,4096`;
- all three exact target regimes at horizon two;
- the base-six CRT quotient and its minimality witnesses;
- the two rational children at the RGΦ shared step-147 state.

The checker imports neither the Python generator nor the `rgphi` package. GitHub Actions supplies an external execution environment. This is **not** represented as an independent research-team replication and does not recompute the archived large Bellman searches.
