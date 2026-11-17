# T006-C — asymptotic access-rate polytope

Let `G=(V,E)` be a finite all-high SCC, with prime receipt `a_e` on each edge. Define the stationary edge-flow polytope
\[
\mathcal C_G=\{f\ge0:\partial f=0,\ \sum_e f_e=1\}
\]
and its access-rate image
\[
\boxed{\mathcal A_F=W(\mathcal C_G).}
\]

## Cycle decomposition

Every nonnegative circulation decomposes into directed cycles. Therefore
\[
\boxed{
\mathcal A_F=
\operatorname{conv}\left\{
\frac{\boldsymbol\nu(C)}{|C|}:C\text{ simple directed cycle}
\right\}.
}
\]
Every linear access objective is optimized on a directed cycle; the scalar problem is a maximum-cycle-mean problem.

## Ergodic realization

For a stationary ergodic Markov policy, empirical prime content satisfies almost surely
\[
\frac1m\boldsymbol\nu(W_m)\longrightarrow Wf\in\mathcal A_F.
\]
Thus `A_F` is the exact long-run prime-content acquisition region.

## Rigidity

Because receipts are nonnegative and every edge lies on a cycle,
\[
\boxed{\mathcal A_F=\{0\}\iff F\text{ is permutational}.}
\]

## Known five-state component

All simple cycles have zero receipt except the strict four-cycle, with rate `e_3/4`. Hence
\[
\boxed{\mathcal A_F=[0,e_3/4].}
\]
The normalized 3-channel interval is `[0,e_3/16]`, the scalar log-rate interval is
\[
[0,\log3/4],
\]
and the radix-normalized scalar interval is
\[
\left[0,\frac{\log3}{4\log B}\right].
\]
