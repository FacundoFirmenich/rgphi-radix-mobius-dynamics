# OR-12 — finite-field boundary return at 83 and autonomous selection of 88

On `F_17`, let

\[
P=[64233:11741:1138],
\quad O=[0:1:-1],
\quad R=[1:2:2].
\]

The exact rational multiple `44P` reduces modulo 83 to

\[
(60,37,37),
\]

and hence, projectively,

\[
\boxed{[44]P=R\pmod{83}}.
\]

Exact projective enumeration gives

\[
\boxed{\#F_{17}(\mathbb F_{83})=89},
\]

and the reduction is smooth. Since 89 is prime and `P mod 83` is nonzero,

\[
\operatorname{ord}(P\bmod83)=89.
\]

Therefore

\[
89P=O,
\qquad88P=-P,
\]

and, because `44P=R`,

\[
\boxed{2R=-P\pmod{83}}.
\]

## Exact circuit

\[
44=\frac{89-1}{2},
\qquad
88=89-1=2\cdot44.
\]

The Frobenius trace is

\[
a_{83}=83+1-89=-5.
\]

Thus

\[
88=83+5.
\]

Under the canonical normalization of the boundary point,

\[
1+2+2=5.
\]

Consequently

\[
\boxed{2\cdot44=88=\#F_{17}(\mathbb F_{83})-1=83+(1+2+2)}.
\]

The finite-field identities are `CLOSED_EXACT`. The equality between trace magnitude and normalized coordinate sum is an exact post-hoc resonance; no causal theorem is claimed.
