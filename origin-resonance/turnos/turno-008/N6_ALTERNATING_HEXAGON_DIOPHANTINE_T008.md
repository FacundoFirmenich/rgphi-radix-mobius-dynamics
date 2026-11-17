# Six-state alternating hexagon — divisor parameterization and exact audit

After the orientation repair, `TSTSTS` is forced within the declared high-defect lollipop jurisdiction. The state tuple is

\[
P/(dQ),\ A/Q,\ A/D,\ C/D,\ C/E,\ P/E,
\]

with `d in {4,5,6,7}` and `P=dA+kQ`, `0<2|k|<d`.

Primitivity implies

\[
\gcd(d,Q)=\gcd(k,d)=1.
\]

The first three divisibilities are parameterized completely by square roots of one:

\[
(DQ^{-1})^2=1\pmod A,\quad
(CA^{-1})^2=1\pmod D,\quad
(ED^{-1})^2=1\pmod C,
\]

with the high intervals selecting unique representatives. The final two divisibilities and all twelve generalized-CRT residues are then checked exactly.

For `2<=Q<=5000`, the exhaustive audit reports:

```text
primitive_QA                 = 3,800,228
D_candidates                 = 18,767,985
C_candidates                 = 44,608,395
E_candidates                 = 257,165,637
primitive_state_candidates   = 4,105,538
full_divisibility_candidates = 3
CRT_hits                     = 0
```

The three fully divisible tuples `(Q,A,D,C,E,P;d,k)` are

```text
(201,184,351,275,549,518;5,-2)
(2733,2315,4122,4097,6723,6527;4,-1)
(4733,3912,6677,6340,12383,10915;4,-1)
```

Every tuple fails generalized CRT compatibility. This closes only the declared finite jurisdiction.

Status: `FINITE_EXHAUSTIVE_Q_LE_5000 / GLOBAL_OPEN`.
