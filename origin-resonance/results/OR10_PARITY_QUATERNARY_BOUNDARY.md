# OR-10 — parity-to-quaternary lift and the `1:2:2` boundary

For the Round-019 cubics write

\[
F_n=A H_n-4S,
\qquad S=z^3+w^3.
\]

Under

\[
F_n=0,
\qquad \gcd(A,zw)=1,
\]

Round 021 proves that for odd `n`:

\[
A\mid S\iff A\text{ is odd},
\]

and if `A` is even,

\[
\boxed{A/\gcd(A,S)=4}.
\]

The mechanism is exact: primitivity forces `z,w` odd, `H_n` is odd, and

\[
v_2(A)=v_2(S)+2.
\]

Thus a binary parity split produces a two-adic valuation gap of exactly two and therefore the quaternary factor

\[
\boxed{2^2=4}.
\]

This is a local theorem of the elliptic family, not a universal theorem that every binary code is quaternary.

## Boundary point

The coprimality forms are

\[
C=2A-z,
\qquad D=2A-w.
\]

Their simultaneous vanishing gives

\[
\boxed{R=[1:2:2]}.
\]

The exact algebraic content is the ratio `1:2:2` and the simultaneous vanishing of `C,D`. Under the normalization `A=1`,

\[
1+2+2=5,
\qquad2+2=4.
\]

The interpretation as one centrum plus two equal dual dyads is a branch-level resonance hypothesis, not a canonical Paper-III claim.

Status:

- parity defect four: `CLOSED_SYMBOLIC`;
- architectural interpretation: `STRUCTURAL_RESONANCE_CANDIDATE`.
