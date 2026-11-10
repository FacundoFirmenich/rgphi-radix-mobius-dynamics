# RGΦ Closure Rigidity 012-A — rigidity at directed diameter at most two

Let \(F\subset\mathbb Q\cap[1/2,1)\) be finite, closed under \(T_B,S_B\),
and strongly connected.  Write each state in reduced form \(p/q\).

The exact reduction laws are
\[
\operatorname{den}(T_B(p/q))=\frac q{\gcd(q,B)},
\qquad
\operatorname{num}(S_B(p/q))=\frac p{\gcd(p,B)}.
\]
Therefore a strict \(T\)-edge decreases both denominator and numerator, and a
strict \(S\)-edge decreases both numerator and denominator.  Indeed, after a
strict reduction the reduced coordinate is at most one half of the source
coordinate, while every state remains high.

## Theorem

If the directed \(T/S\)-graph of \(F\) has diameter at most two, then
\[
\boxed{T_B|_F\text{ and }S_B|_F\text{ are permutations}.}
\]

## Proof

Suppose \(x_0=p_0/q_0\xrightarrow{T}x_1=p_1/q_1\) is strict. Then
\[
q_1\le q_0/2,\qquad p_1<q_1\le q_0/2<p_0.
\]
A return in one step is impossible: \(T\) cannot increase denominator and
\(S\) cannot increase numerator.

For a two-step return:

- \(TT\) cannot restore \(q_0\);
- \(SS\) cannot restore \(p_0\);
- after \(TS\), the intermediate denominator is at most \(q_1\), hence its
  numerator is below \(q_0/2<p_0\), and the final \(S\) cannot restore
  \(p_0\);
- after \(ST\), the intermediate numerator is at most \(p_1\), so its
  denominator is below \(2p_1<q_0\), and the final \(T\) cannot restore
  \(q_0\).

Thus no strict \(T\)-edge can occur.  The argument with numerator and
denominator interchanged excludes strict \(S\)-edges.  On a finite set, an
endomap with no reduction is injective and therefore a permutation. ∎

This theorem contains the ternary all-high rigidity of Round 010 as a special
case, but applies to arbitrary cardinality whenever directed diameter is at
most two.