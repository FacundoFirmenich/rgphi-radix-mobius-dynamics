# RGΦ Five-State Closure 014 — first exact advance

## Status

`OPEN_PARTIAL`

This round does **not** claim five-state rigidity. It closes two of the four binding architecture families and produces an exact canonical census of the remaining two.

## Theorem 014-A — Hamiltonian `TTSSS` is impossible

Consider a five-cycle with two consecutive `T` edges and three consecutive `S` edges, with exactly one strict reduction factor \(r\in\{2,3\}\) and every other cycle edge unreduced.

If the strict edge is a `T` edge, the two-edge `T` block changes the denominator by the factor \(r\), while the three `S` edges preserve the numerator. Two cycle states therefore satisfy \(x_j=r x_i\); since \(x_i>1/2\), this gives \(x_j>1\).

If the strict edge is an `S` edge, the dual argument applies: the `T` block preserves denominator while the `S` block changes numerator by \(r\), again forcing one state to be \(r\) times another and hence above one.

Thus no all-high closed SCC can contain a strict Hamiltonian cycle of word `TTSSS`.

## Corollary 014-A1 — `TTSS` core plus a fifth state is impossible

The contradiction occurs on the marked four-cycle itself and is independent of alternate closure edges. Adding a fifth state cannot repair a strict `TTSS` core.

## Remaining exact architecture census

The only binding families left are:

1. Hamiltonian `TSTSS`;
2. a strict `TSTS` four-cycle whose alternate closure uses a fifth high state.

The generator exhausts all alternate functional assignments, all marked strict positions, factors 2 and 3, and quotients by vertex relabeling and `T/S` duality. Every survivor satisfies:

- strong connectivity;
- absence of forbidden mixed `T/S` two-cycles;
- directed diameter greater than two;
- fibre injectivity on every forced unreduced fibre;
- the cycle-reduction budget on every simple cycle containing the marked strict edge;
- exact nonempty high-domain rational polytope, certified by a rational witness.

### Results

- Hamiltonian `TSTSS`: **228** canonical candidate classes.
- `TSTS` core plus one closure state: **332** canonical candidate classes.
- Total unresolved canonical classes: **560**.

These are not denominator-bounded dynamical scans. They are exhaustive finite combinatorial classes under the declared five-state gate and its necessary arithmetic constraints.

## Next symbolic task

For each surviving class, impose the exact radix congruences on the numerator and denominator fibres. The next reduction target is to quotient the 560 classes into a much smaller set of Diophantine normal forms, then eliminate every form or construct an exact counterfamily.
