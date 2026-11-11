# P2 PRIME-005 external-runner scope

This isolated branch contains a standalone C++17 reimplementation of two P2-05 results:

1. the general composite-base CRT classification of `(gcd(t,B), gcd(t-1,B))` for every residue and every `2 <= B <= 2000`;
2. an explicit collision showing that the deterministic compiler lift is not injective.

The GitHub-hosted run is an external execution environment and an independently written implementation. It is not an independent research-team review and does not recompute the large step-147 Bellman closure search.
