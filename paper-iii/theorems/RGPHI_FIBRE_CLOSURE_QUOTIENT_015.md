# RGΦ Five-State Diophantine Quotient 015 — fibre closure theorem

## Status

`OPEN_PARTIAL`

The 560 canonical architecture classes from Round 014 are not yet exact Diophantine forms: their LP witnesses did not impose every equality forced by the arithmetic reduction laws, did not prohibit all state collisions, and did not reapply the cycle budget to strict edges propagated by fibre closure.

## Theorem 015-A — denominator-fibre closure

For a reduced state \(x_i=p_i/q_i\),
\[
q_{T(i)}=\frac{q_i}{\gcd(q_i,B)}.
\]
Hence every directed `T` cycle has one common reduced denominator and every edge on that cycle is unreduced. Moreover,
\[
q_i=q_j\Longrightarrow q_{T(i)}=q_{T(j)}.
\]
Thus denominator equality is closed under forward `T`.

## Theorem 015-B — numerator-fibre closure

Dually,
\[
p_{S(i)}=\frac{p_i}{\gcd(p_i,B)},
\]
so every directed `S` cycle has one common numerator and
\[
p_i=p_j\Longrightarrow p_{S(i)}=p_{S(j)}.
\]

## Corollary 015-C — exact contradiction tests

After the least simultaneous fibre closure:

1. a marked strict edge cannot have equal source and target fibre in its reduced coordinate;
2. two labels with the same numerator and denominator fibres are the same rational state;
3. `T` is injective on an unreduced denominator fibre, and `S` is injective on an unreduced numerator fibre;
4. every newly forced strict edge must enter the reduction budget of every simple high cycle containing it.

## Exact quotient

| adjudication | classes |
|---|---:|
| state collision after fibre closure | 432 |
| marked strict-edge/fibre conflict | 60 |
| unreduced-fibre injectivity conflict | 34 |
| additional cycle-budget conflict | 10 |
| exact survivors | 24 |

The 24 survivors occur in factor-2/factor-3 pairs and quotient to exactly
\[
\boxed{12}
\]
structural Diophantine normal forms:

- 3 Hamiltonian forms with strict `T`;
- 2 Hamiltonian forms with strict `S`;
- 7 `TSTS`-core-plus-one forms with strict `S`.

No strict-`T` core-plus-one form survives.

## Exact edge equations

For a `T` edge \(i\to j\), set \(g_{ij}=q_i/q_j=\gcd(q_i,B)\). Then
\[
q_i=g_{ij}q_j,\qquad \gcd(B/g_{ij},q_j)=1,
\]
\[
(B/g_{ij})p_i\equiv p_j\pmod{q_j}.
\]
For an `S` edge set \(h_{ij}=p_i/p_j=\gcd(p_i,B)\). Then
\[
p_i=h_{ij}p_j,\qquad \gcd(B/h_{ij},p_j)=1,
\]
\[
(B/h_{ij})(q_i-p_i)\equiv q_j-p_j\pmod{p_j}.
\]

`DIOPHANTINE_NORMAL_FORMS_12.json.gz` instantiates these equations, high-domain inequalities, reducedness and pairwise state-distinctness for all surviving forms.

## Evidence boundary

This round proves the exact quotient from 560 classes to 12 forms. It does not eliminate those 12 forms and therefore does not prove five-state rigidity.
