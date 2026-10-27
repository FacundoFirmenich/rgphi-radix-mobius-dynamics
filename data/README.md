# Exact research data

The data directory contains machine-readable evidence used by the public mathematical claims.

## thresholds/

Exact first-hit and robustness evidence:

- benchmark-robustness.csv — exact \(\kappa\)-intervals preserving each benchmark first-hit time;
- exact-bfs-depth-0-162.csv — exact level summaries through the depth-four closure horizon;
- greedy-failure.csv — scalar-height failure examples;
- latent-precursors.csv — states illustrating delayed extremal value;
- nonnesting-robustness.csv — exact common robustness intervals for the nonnesting claims;
- portal-continuation-costs.csv — exact continuation times from earlier optima;
- robustness-result.json — machine-readable summary;
- threshold-atlas-piecewise-m1-m4.csv — piecewise parameter atlas;
- threshold-profiles.csv — exact target profiles.

## traps/

Finite modular-trap evidence:

- C8-exact-audit.csv — full audit of the canonical eight-state trap;
- trap-atlas-result-D500.json — canonical denominator-\(\le500\) counts;
- closed-sccs-D500.csv — SCCs closed modulo terminal components;
- forward-closures-D500.csv — exact finite forward-invariant closures;
- trap-scc-classification-D500.csv — structural SCC classification;
- trap-classification-audit-result.json — theorem-audit summary.

## certificates/

Compact records from exact searches retained for auditability.

## Numeric policy

The theorem-critical fields are exact integers or rational strings.

Decimal values may appear as convenience columns only and should never be used to reconstruct logical decisions when an exact field is available.

## Scope policy

Finite atlases prove statements about their declared finite domain. They are not silently extrapolated to all rational states.
