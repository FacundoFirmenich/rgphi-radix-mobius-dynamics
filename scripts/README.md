# Independent verification and search scripts

This directory contains scripts that are deliberately separable from the small installable reference package.

## base_b_audit.py

Audits the general base-\(B\) symbolic formulas over a finite exact parameter grid.

Purpose: regression verification, not replacement for the symbolic proofs.

## trap_atlas.py

Builds the finite rational-state graph and computes the reference trap atlas.

Canonical public benchmark:

\[
\operatorname{denominator}\le500.
\]

## compact_bfs.cpp

Compact exact target-BFS kernel retained for auditability and high-volume experiments.

Any pruning used in a proof-relevant run must be justified mathematically and reported with the result.

## verify_legacy_unit.py

Checks compatibility with the preceding internal scientific-unit bundle.

This is a migration/audit tool, not a current headline verifier.

## Preferred small verifier

For ordinary repository validation, use:

~~~bash
rgphi verify
~~~

The small verifier under src/rgphi is easier to inspect independently than the historical large-search engines.
