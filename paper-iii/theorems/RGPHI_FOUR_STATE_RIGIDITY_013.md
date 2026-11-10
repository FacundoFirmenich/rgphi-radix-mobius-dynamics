# RGΦ Four-State Closure Rigidity 013

Let \(F\subset\mathbb Q\cap(1/2,1)\) be a closed strongly connected
component of cardinality four for
\[
T_B(x)=\{Bx\},\qquad
S_B=H\circ T_B\circ H^{-1},\qquad
H(x)=\frac1{1+x}.
\]

Round 012 proves that if either restricted generator is nonpermutational, then
there is a Hamiltonian four-cycle with exactly two \(T\)-edges, two
\(S\)-edges, total reduction product \(r\in\{2,3\}\), and all other cycle
edges unreduced.  Up to cyclic rotation, the word is \(TTSS\) or \(TSTS\).

# Theorem 013-A - the word TTSS is impossible

Write the cycle as
\[
x_0\xrightarrow{T}x_1\xrightarrow{T}x_2
\xrightarrow{S}x_3\xrightarrow{S}x_0.
\]

If the strict edge is one of the two \(T\)-edges, the other \(T\)-edge is
unreduced and the two \(S\)-edges preserve numerator.  Hence \(x_0\) and
\(x_2\) have the same numerator while their denominators differ by the
strict factor \(r\).  Therefore
\[
x_2=r x_0>1,
\]
since \(x_0>1/2\).

If the strict edge is one of the two \(S\)-edges, the dual statement holds:
the two \(T\)-edges preserve denominator, while the strict \(S\)-edge changes
one of the equal numerators by the factor \(r\).  Again
\[
x_2=r x_0>1.
\]

Thus no all-high closed SCC can contain a strict Hamiltonian cycle of word
\(TTSS\).

# Theorem 013-B - TSTS with strict T reduction is impossible

Orient the cycle as
\[
x_0\xrightarrow{T_r}x_1\xrightarrow{S}x_2
\xrightarrow{T}x_3\xrightarrow{S}x_0,
\]
where the subscript denotes the unique strict reduction factor
\(r\in\{2,3\}\).

Because the other three cycle edges are unreduced, there are coprime reduced
coordinates
\[
x_0=\frac{C}{rQ},\qquad
x_1=\frac{A}{Q},\qquad
x_2=\frac{A}{D},\qquad
x_3=\frac{C}{D}.
\]

The high-domain inequalities imply
\[
A<Q<2A,\qquad A<D<2A,\qquad A<C<D<2A.
\]

## Forced alternate edges

Closure leaves no freedom:

1. \(S(x_0)\neq x_0\).  Otherwise \(C\mid B-1\), and
   \(S(x_3)=x_0\) would force \(D\equiv rQ\pmod C\).  Both denominators lie
   in \((C,2C)\), so \(D=rQ\), giving \(x_3=x_0\).
   Hence \(S(x_0)=x_3\).

2. \(S(x_2)\neq x_2\).  Otherwise \(A\mid B-1\), and
   \(S(x_1)=x_2\) would force \(D\equiv Q\pmod A\).  Since
   \(Q,D\in(A,2A)\), this gives \(D=Q\), hence \(x_2=x_1\).
   Therefore \(S(x_2)=x_1\).

3. \(T(x_3)\neq x_3\).  Otherwise \(D\mid B-1\), and
   \(T(x_2)=x_3\) would force \(C\equiv A\pmod D\).  Since
   \(A,C<D\), this gives \(C=A\).  Hence \(T(x_3)=x_2\).

4. \(T(x_1)\) cannot enter the \(D\)-denominator fibre.  Its reduced
   denominator would be \(Q/g\), \(g=\gcd(Q,B)\).  If \(g\ge2\), then
   \(Q/g<A<D\); if \(g=1\), then \(D=Q\) and \(x_2=x_1\).  Thus
   \(T(x_1)=x_1\).

Consequently
\[
Q\mid B-1,
\]
and the alternate restrictions are
\[
S:(x_0\ x_3)(x_1\ x_2),\qquad
T:x_1\text{ fixed},\ (x_2\ x_3).
\]

## Normal form

The strict \(T\)-edge gives
\[
C\equiv rA\pmod Q.
\]
For \(r=2\), the only representatives compatible with
\(A<C<2A\) and \(A<Q<2A\) are \(2A\) and \(2A-Q<A\), both impossible.
Therefore
\[
\boxed{r=3}.
\]

The unique compatible representative is
\[
C=3A-Q.
\]
Write
\[
Q=A+u,\qquad C=2A-u.
\]
The condition \(x_0>1/2\) gives
\[
\boxed{A>5u}.
\]
Since \(C<D<2A\), write
\[
D=2A-t,\qquad 0<t<u,
\]
and put
\[
s=u-t.
\]

The two forced 2-cycles imply
\[
\boxed{A\mid u^2-t^2}
\]
and
\[
\boxed{D\mid A^2-s^2}.
\]
Let
\[
u^2-t^2=kA,\qquad A^2-s^2=lD.
\]
Because \(\gcd(A,t)=1\), reduction modulo \(A\) gives
\[
s^2\equiv lt\pmod A.
\]
But \(u^2\equiv t^2\pmod A\), so
\[
s^2=(u-t)^2\equiv-2ts\pmod A.
\]
Hence
\[
l\equiv-2s\pmod A.
\]
Now \(0<l<A\) and \(0<2s<A\), so
\[
\boxed{l=A-2s}.
\]
Substitution into the second divisibility equation yields
\[
A=4u-3t-k<4u,
\]
contradicting \(A>5u\).

Thus the strict-\(T\) version of \(TSTS\) is impossible.

# Theorem 013-C - TSTS with strict S reduction is impossible

Orient the cycle as
\[
x_0\xrightarrow{S_r}x_1\xrightarrow{T}x_2
\xrightarrow{S}x_3\xrightarrow{T}x_0.
\]
Then
\[
x_0=\frac{rA}{D},\qquad
x_1=\frac{A}{Q},\qquad
x_2=\frac{C}{Q},\qquad
x_3=\frac{C}{D}.
\]

## Forced alternate edges

Closure again determines the full functional pattern:

- \(T\) swaps \(x_0,x_3\);
- \(T\) swaps \(x_1,x_2\);
- \(S\) swaps \(x_2,x_3\);
- \(S(x_1)=x_1\).

The first three statements follow because a fixed alternate edge would combine
with its cycle edge and the corresponding fixed-point divisibility to identify
two distinct states.  For the last statement, the reduced numerator of
\(S(x_1)\) is \(A/\gcd(A,B)\).  It cannot increase to \(rA\).  If it fell to
\(C\), then \(C\le A/2<Q/2\), contradicting that \(x_2\) is high.  Hence
\[
A\mid B-1.
\]

Set
\[
Q=A+P.
\]
Write
\[
D=rA+N.
\]
Passing to \(H^{-1}\)-coordinates on the strict edge gives
\[
N\equiv rP\pmod A.
\]
Since the two \(C\)-numerator states are high,
\[
D<2Q.
\]
It follows that
\[
\begin{array}{c|c|c}
r&\text{range}&N\\ \hline
2&P>A/2&2P-A\\
3&P>2A/3&3P-2A.
\end{array}
\]
Thus in both cases
\[
\boxed{D=A+rP}.
\]

The high inequalities force
\[
C=A+W,\qquad 0<W<P,
\]
with
\[
W>P-A/2\quad(r=2),
\]
\[
W>(3P-A)/2\quad(r=3).
\]

The three forced 2-cycles now give
\[
A+P\mid W(2A+W),
\]
\[
A+rP\mid r^2A^2-(A+W)^2,
\]
\[
A+W\mid(r-1)P\bigl((r+1)P-2W\bigr).
\]
Define the first two positive quotients by
\[
W(2A+W)=k(A+P),
\]
\[
r^2A^2-(A+W)^2=l(A+rP).
\]
Adding these identities gives
\[
P(k+rl)=A\bigl(A(r^2-1)-k-l\bigr).
\]
Since \(\gcd(A,P)=1\), write
\[
k+rl=mA.
\]

## Case r=2

Positivity forces \(m=2\), and therefore
\[
k=4(A-P),\qquad l=2P-A.
\]
The first quotient identity becomes
\[
\boxed{C^2+4P^2=5A^2},\qquad C=A+W.
\]
This implies \(\gcd(C,P)=1\).
The third 2-cycle condition says
\[
C\mid P(3P-2W).
\]
Put \(E=3P-2W\).  The range of \(W\) gives
\[
0<E<2C.
\]
Hence \(E=C\).  Writing \(d=P-W\), this gives \(A=3d\), and the conic reduces
to
\[
5P^2+4Pd-41d^2=0.
\]
Its discriminant is
\[
4\cdot209\,d^2,
\]
which is not a square.  Contradiction.

## Case r=3

The quotient bounds give
\[
m\in\{5,6,7\}.
\]
The case \(m=5\) is impossible because
\[
k=\frac{19A-15P}{2}<2W<2P
\]
would imply \(A<P\).

### Subcase m=6

Here
\[
\boxed{C^2+9P^2=10A^2}.
\]
Thus \(\gcd(C,P)=1\), and parity forces \(C,P\) odd.  The third cycle condition
is
\[
C\mid4P(2P-W).
\]
But
\[
0<2P-W<A<C,
\]
and \(\gcd(C,4P)=1\), contradiction.

### Subcase m=7

Here
\[
\boxed{2C^2+21P^2+4AP=19A^2}.
\]
Again \(C\) is odd, and
\[
d=\gcd(C,P)\mid19.
\]
If \(d=1\), the preceding argument applies directly.

If \(d=19\), write
\[
C=19c,\qquad P=19p,
\]
with \(\gcd(c,p)=1\).  The third cycle condition gives
\[
E=2P-W=jc,
\qquad1\le j\le37.
\]
Eliminating \(A\) yields
\[
1197p^2-(80j+1520)pc+(j^2+38j+323)c^2=0.
\]
Its discriminant is
\[
4c^2\bigl(403j^2+15314j+190969\bigr).
\]
For \(1\le j\le37\), the integer
\[
403j^2+15314j+190969
\]
is never a square.  An exact modular certificate is supplied in the bundle:
moduli \(68,55,71\) exclude all 37 values.

Thus the strict-\(S\) version is also impossible.

# Corollary 013-D - four-state all-high permutation rigidity

Every four-state all-high closed SCC satisfies
\[
\boxed{T_B|_F\text{ and }S_B|_F\text{ are permutations}.}
\]

Indeed every nonpermutation candidate would contain a strict Hamiltonian cycle
of word \(TTSS\) or \(TSTS\), and all cases have now been excluded.

# Evidence boundary

This theorem closes cardinality four only.

It does not yet prove all-high permutation rigidity for arbitrary finite
cardinality.  Any minimal counterexample must have at least five states and,
by the Round-012 budget, must occur over a base divisible by 2 or 3.