# HA-005-A — integer Laurent-Nullstellensatz certificates for the 80 generic profiles

## Setting

For a fixed denominator fibre component with underlying modulus `Q_c`, compatibility of the base residue yields divisibilities

\[
Q_c\mid f_1(P),\ldots,Q_c\mid f_s(P),
\]

where each `f_i` is a monomial or binomial in the transverse numerator-component variables. Primitiveness of every source state in the component makes the source numerator product invertible modulo `Q_c`. The numerator-fibre statement is dual.

## Compact certificate

Write a binomial as `f_i=A_i-B_i`. If an integer vector `lambda` satisfies

\[
\sum_i \lambda_i(\deg A_i-\deg B_i)=0,
\]

then the products selected by the positive and negative parts of `lambda` have the same monomial exponent. The telescoping product identity gives

\[
N X^e\in(f_1,\ldots,f_s).
\]

Because `X^e` is invertible modulo the fibre modulus,

\[
\boxed{Q_c\mid N}
\]

(or `P_c | N` on a numerator fibre).

## Exhaustive result

The 80 generic profiles yield 160 independently checkable integer toric/monomial certificates, component constants supported on `{2,3,5,13,19}`, and 278 total positive divisor assignments. Exact propagation of the strict high inequalities rejects all 278 assignments before CRT. Therefore all 80 profiles are globally impossible over the integers.
