# Superaccess channel theorem

Let `W` be a random admissible path, `R(W)` its complete local receipt history, `N(W)` its terminal prime-valued holonomy and `O(W)` the observer's data. Define

\[
S^{path}_\mu(O)=H_\mu(R(W)\mid O(W)),
\qquad
S^{term}_\mu(O)=H_\mu(N(W)\mid O(W)).
\]

These are the path and terminal superaccess requirements. Since terminal holonomy is a function of the receipt history,

\[
S^{path}_\mu(O)\ge S^{term}_\mu(O)\ge0.
\]

Observer refinement obeys data processing.

## Exact block subchannel

At `x_0`, the return blocks

\[
a=TTTT,\qquad b=TSTS
\]

have the same length and endpoint, but receipts `0` and `e_3`. For `N` independently chosen blocks, all `2^N` paths have the same initial state, endpoint and length `4N`.

* Full hidden receipt histories require exactly `N` bits: an exact subchannel rate of `1/4` bit per edge.
* Terminal holonomy has only `N+1` values, hence zero exponential zero-error rate.

Under independent fair generator choices on the canonical graph, the stationary distribution is `(2/7,3/14,1/7,1/14,2/7)`, the mean log receipt is `log(3)/28`, and the asymptotic variance is `3(log(3))^2/112`.

These are superaccess statistics, not hyperaccess.
