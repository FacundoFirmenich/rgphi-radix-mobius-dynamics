# HA-005-C — global no-go in the minimal rank-two six-state jurisdiction

## Jurisdiction

Six-state strongly connected functional graphs satisfying:

1. exactly two strict edges globally;
2. strict factors exactly `2` and `3`;
3. all other defects equal one;
4. every simple cycle satisfies the strict high-cycle budget;
5. the prime-valuation cycle module has rank two;
6. quotient by vertex relabelling and generator exchange.

HA-004 exhaustively enumerated this jurisdiction:

\[
46,656,000\text{ labelled profiles}
\longrightarrow839\text{ canonical classes}.
\]

It then eliminated 383 by forced state collision and 354 by exact Gordan certificates, leaving 102 high-feasible fibre profiles.

## Theorem

\[
\boxed{
\text{No RGΦ realization exists in the declared minimal rank-two }2/3\text{ jurisdiction.}
}
\]

## Proof stack

\[
839=383+354+102.
\]

HA-005 partitions the 102 arithmetic survivors as

\[
102=80+22.
\]

- The 80 generic profiles are eliminated by 160 integer Laurent-Nullstellensatz component certificates plus an exhaustive 278-case divisor/high closure.
- The 22 residual profiles are eliminated by exact linear divisibility strips; seven require the additional primitive-state contradiction.

Thus

\[
\boxed{839=383+354+80+22}
\]

with every class assigned an exact impossibility certificate.

## Boundary

This is not a global six-state nonexistence theorem. It does not cover defects `4,5,6,7`, three or more strict edges, two independent prime directions living on different cycle architectures outside the declared exactly-two-strict `2/3` class, or the complete six-state decorated catalogue.
