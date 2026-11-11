# RGΦ Round 019-B — universal CRT realization theorem

Let x_i=p_i/q_i be pairwise distinct reduced rationals. Prescribe maps τ,σ and positive integer reduction factors g_i,h_i. Assume

q_i=g_i q_{τ(i)},  p_i=h_i p_{σ(i)}.

Put c_i=q_i-p_i and define

r_i^T ≡ g_i p_{τ(i)} p_i^{-1} (mod q_i),

r_i^S ≡ h_i c_{σ(i)} c_i^{-1} (mod p_i).

## Theorem 019-B

An integer base B realizes exactly

T_B(x_i)=x_{τ(i)},  S_B(x_i)=x_{σ(i)}

with exact reduction factors g_i,h_i iff

B≡r_i^T (mod q_i),  B≡r_i^S (mod p_i)

for every i, and

gcd(r_i^T,q_i)=g_i,  gcd(r_i^S,p_i)=h_i.

Consequently a fixed primitive state tuple is either unrealizable or is realized by one complete arithmetic progression

B≡B_* mod lcm(p_1,q_1,...,p_n,q_n).

The progression exists precisely when every pair of congruences satisfies generalized CRT compatibility.

## Proof

For T, primitive reduction gives Bp_i≡g_i p_{τ(i)} mod q_i, while the exact denominator drop is gcd(B,q_i)=g_i. Applying the same argument to H^{-1}(x_i)=c_i/p_i gives the S congruence and exact numerator reduction. The final statement is the generalized Chinese remainder theorem.

## Consequence

All remaining five-state classification work is state-side Diophantine analysis. Once a state tuple survives, its complete base family is automatic.
