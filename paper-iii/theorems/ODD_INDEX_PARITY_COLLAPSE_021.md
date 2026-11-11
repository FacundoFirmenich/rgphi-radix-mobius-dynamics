# RGΦ Round 021-A — odd-index parity collapse

For \(n\in\{1,\ldots,19\}\), write
\[
F_n(A,z,w)=A H_n-4(z^3+w^3),
\]
where
\[
H_n=4nA^2-2nA(w+z)+nwz-20Aw-340Az+24w^2+148wz+24z^2.
\]
Assume \(F_n=0\) and the primitive condition \(\gcd(A,zw)=1\).

## Theorem 021-A

If \(n\) is odd, then
\[
\boxed{A\mid z^3+w^3\iff A\text{ is odd}.}
\]
More precisely, if \(A\) is even, then
\[
\boxed{\frac{A}{\gcd(A,z^3+w^3)}=4.}
\]

## Proof

The identity \(AH_n=4(z^3+w^3)\) always gives \(A\mid4(z^3+w^3)\). If \(A\) is odd, four is invertible modulo \(A\), so \(A\mid z^3+w^3\).

If \(A\) is even, primitivity forces \(z,w\) odd. For odd \(n\), \(H_n\equiv nwz\equiv1\pmod2\), so \(H_n\) is odd and
\[
v_2(A)=2+v_2(z^3+w^3).
\]
For every odd prime \(\ell\), the equality \(AH_n=4(z^3+w^3)\) implies \(v_\ell(A)\le v_\ell(z^3+w^3)\). Hence the exact defect is four.

## Consequences

- On the ten odd-index curves, cubic divisibility reduces to the parity of \(A\).
- The Round-020 point on \(F_{17}\) has odd \(A\) and passes.
- The exact point \(44P\) has even \(A\), lies in the chamber and fails by factor four.

For even \(n\) and even \(A\), this parity argument is not decisive.
