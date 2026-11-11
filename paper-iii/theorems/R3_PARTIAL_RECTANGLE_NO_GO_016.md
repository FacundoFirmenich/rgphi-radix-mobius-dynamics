# RGΦ Round 016-C — factor-three partial-rectangle no-go

## Statement

There are no reduced high rationals
\[
\frac{c}{3q},\quad \frac{a}{q},\quad \frac{a}{d},\quad \frac{c}{d}
\]
with the following actions:

1. \(c/(3q)\xrightarrow{T_3}a/q\);
2. \(a/q\) is fixed by \(T\);
3. \(a/d\) and \(c/d\) form a \(T\)-2-cycle;
4. \(a/q\) and \(a/d\) form an \(S\)-2-cycle.

This is exactly the strict-\(T\), factor-three partial rectangle present in `DF015-0016`.

## Normal form

The predecessor-shift theorem gives
\[
c=3a\pm q.
\]
The plus sign is impossible because \(q>a\) would give \(c>4a\), whereas the shared high denominator \(d\) requires \(c<d<2a\). Therefore
\[
\boxed{c=3a-q.}
\]
Write
\[
q=a+z,\qquad c=2a-z.
\]
The strict source is high iff
\[
2c>3q,
\]
which is equivalent to
\[
\boxed{0<z<a/5.}
\]
Since \(c<d<2a\), write
\[
d=2a-w,
\qquad 0<w<z.
\]

The \(S\)-2-cycle gives
\[
a\mid(q-a)^2-(d-a)^2=z^2-w^2.
\]
Put
\[
\boxed{z^2-w^2=ma},\qquad m\in\mathbb Z_{>0}.
\]
Then
\[
0<m<z/5.
\]
The \(T\)-2-cycle gives
\[
d\mid c^2-a^2.
\]
Reducedness of \(a/d\) gives
\[
\gcd(a,w)=1.
\]

## Odd \(w\)

If \(w\) is odd, then \(d=2a-w\) is odd and
\[
\gcd(d,w)=1.
\]
A direct reduction using \(z^2-w^2=ma\) gives
\[
4(c^2-a^2)\equiv-wL\pmod d,
\]
where
\[
L=8z-7w-2m.
\]
Thus \(d\mid L\). But
\[
L>8z-7z-2z/5=3z/5>0,
\]
and
\[
L<8z<8a/5<2a-w=d,
\]
a contradiction.

## Even \(w\)

Let \(w=2W\). Then \(a\) is odd. Set
\[
D=d/2=a-W.
\]
We have \(\gcd(D,W)=1\). Since \(d\mid c^2-a^2\), also \(D\mid c^2-a^2\). Modulo \(D\), using \(a\equiv W\) and
\[
z^2-4W^2=ma,
\]
we obtain
\[
c^2-a^2\equiv W(m+7W-4z)\pmod D.
\]
Hence
\[
D\mid E:=m+7W-4z.
\]
However
\[
E<z/5+7z/2-4z=-3z/10<0,
\]
while
\[
E>-4z>-4a/5
\]
and
\[
D=a-W>a-z/2>9a/10.
\]
Thus
\[
-D<E<0,
\]
again impossible.

Therefore the partial rectangle cannot exist, and
\[
\boxed{\texttt{DF015-0016 is globally impossible}.}
\]
