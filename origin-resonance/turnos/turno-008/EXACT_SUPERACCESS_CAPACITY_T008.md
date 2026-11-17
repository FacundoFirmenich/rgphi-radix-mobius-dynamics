# Exact superaccess capacities of the canonical five-state component

Fix `T=(1,0,3,2,4)` and `S=(4,2,1,0,0)`, with receipt `1` only on the strict edge `S:3->0`.

## Complete internal path

There are exactly `2^n` labelled generator paths of length `n` from a fixed start and only five endpoints. Hence the maximum endpoint fibre is between `2^n/5` and `2^n`, so

\[
C_{full}=1\text{ bit per edge}.
\]

## Receipt history

The deterministic subset automaton has six reachable states. Its adjacency matrix has characteristic polynomial

\[
x^6-x^5-x^2+x-1.
\]

If `rho=1.338350132242277...` is its largest real root, then the generating function for distinct receipt histories is

\[
\sum_{n\ge0}a_nz^n=\frac1{1-z-z^4+z^5-z^6},
\]

and

\[
C_{receipt}=\log_2rho=0.420455595776494...\text{ bit per edge}.
\]

Conditioning on endpoint changes counts by at most a factor five and preserves the rate.

## Terminal holonomy

After `n` steps there are at most `n+1` accumulated strict-edge counts, hence

\[
C_{terminal}=0.
\]

Therefore

\[
1>\log_2rho>0
\]

are the exact full-path, receipt-history and terminal superaccess scales.

Status: `CLOSED_EXACT_T008`.
