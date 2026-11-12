# Fixed-base bounded-cardinality decision theorem

For integers `B>=2` and `n>=1`, define

`N_{B,n}=B^(n-1) lcm_{1<=k<=n}(B^k-1)`.

If a nonempty reduced rational set `F` is closed under both generators and `|F|<=n`, then every state `p/q in F` satisfies `p | N_{B,n}` and `q | N_{B,n}`.

## Proof

The radix orbit reaches a cycle after at most `n-1` steps. On a radix cycle denominators are constant, and a period-`k` denominator divides `B^k-1`. The preperiod contributes only divisors of `B^(n-1)`. Apply the same argument to the conjugate coordinate `(q-p)/p` to control `p`.

Thus every candidate belongs to an explicit finite divisor universe. Exact evaluation of both maps, closure pruning and terminal SCC extraction decide the bounded problem for each fixed pair `(B,n)`.

## Boundary

This does not imply polynomial complexity, a uniform classification in `B`, or finite `n_min(B)` for every base.
