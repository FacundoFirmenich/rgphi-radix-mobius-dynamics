# RGΦ Five-State Diophantine Quotient 015 — defect-one functional theorem

Let \(F\subset\mathbb Q\cap(1/2,1)\) be finite, closed and strongly connected. Assume exactly one edge of one generator has reduction factor \(r>1\), while all remaining generator edges are unreduced.

## Theorem 015-A — permutation/lollipop normal form

If the strict edge is a \(T_B\)-edge with source \(s\), then:

1. \(S_B|_F\) is a permutation;
2. \(s\) has no \(T_B\)-preimage in \(F\);
3. \(T_B\) restricted to \(F\setminus\{s\}\) is a permutation;
4. if \(t=T_B(s)\), then \(t\) has exactly two \(T_B\)-preimages, one from the permutation and the strict source;
5. every other vertex has exactly one \(T_B\)-preimage.

Thus the strict generator is a defect-one **lollipop**: one transient source feeding a permutation. The other generator is a permutation. The strict-\(S_B\) statement is dual.

### Proof

All \(S_B\)-edges are unreduced. They preserve the reduced numerator \(p\), and on a fixed numerator fibre the complementary residues \(q-p\) are multiplied by \(B\bmod p\). Since unreduced means \(\gcd(p,B)=1\), that action is injective. Distinct numerator fibres cannot collide. Hence \(S_B|_F\) is injective and therefore a permutation.

For \(T_B\), all sources except \(s\) are unreduced, so the same denominator-fibre argument makes the restriction to \(F\setminus\{s\}\) injective. If some \(u\ne s\) satisfied \(T_B(u)=s\), then the unreduced edge would give \(\operatorname{den}(u)=\operatorname{den}(s)\), while its reduction factor would be one. But the strict edge at \(s\) gives \(\gcd(\operatorname{den}(s),B)=r>1\), a contradiction. Therefore \(s\) is outside the image. The \(|F|-1\) non-strict sources map injectively into the \(|F|-1\) vertices \(F\setminus\{s\}\), hence bijectively. Adding the strict edge gives the claimed lollipop indegrees.

## Corollary 015-B — defect-one incidence representation

Normalize by duality so that \(T_B\) is strict. Let the cycles of the permutation \(T_B|_{F\setminus\{s\}}\) be the denominator-fibre vertices, and the cycles of \(S_B|_F\) be the numerator-fibre vertices. Every ordinary state is an edge between its denominator and numerator fibres. The exceptional source is an edge attached to the denominator fibre of its strict target, but with denominator multiplied by \(r\).

Delete the exceptional source edge and retain the four ordinary state-edges. The action graph is strongly connected iff this **ordinary incidence graph** is connected. In particular, the source cannot be fixed by the permutation generator: its numerator fibre must contain another ordinary state. The exceptional edge is directed from the source into the denominator permutation and cannot by itself repair a disconnected ordinary incidence graph.

## Corollary 015-C — forbidden exceptional parallel edge

The exceptional source cannot share both its numerator fibre and the target denominator fibre with an ordinary state. Otherwise the two states would be \(P/(rQ)\) and \(P/Q\). Highness of the first gives \(P>rQ/2\ge Q\), while the second being below one gives \(P<Q\), a contradiction.

## Diophantine edge equations

For a normalized strict-\(T\) class, write ordinary states as \(P_a/Q_b\) according to their incidence edge and the source as \(P_{a_s}/(rQ_{b_t})\). Then

- ordinary \(T:i\to j\): \(B P_i\equiv P_j\pmod{Q_i}\);
- strict \(T:s\to t\): \(B P_s\equiv rP_t\pmod{rQ_t}\), with \(\gcd(rQ_t,B)=r\);
- \(S:i\to j\): \(B(Q_i-P_i)\equiv Q_j-P_j\pmod{P_i}\);
- every ordinary denominator and every numerator is coprime to \(B\).

These equations, together with \(P_i<Q_i<2P_i\), are the canonical Diophantine form of the remaining five-state problem.

## Evidence boundary

This theorem reduces the certified five-state architecture list to defect-one incidence/Diophantine forms. It does not yet eliminate every surviving form and does not promote five-state rigidity.