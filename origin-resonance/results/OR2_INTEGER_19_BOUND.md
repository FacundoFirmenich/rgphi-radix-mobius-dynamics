# OR-2 result — 19 survives sharpening and is real-geometrically active

With

\[
a=A/z>5,\qquad t=w/z\in(0,1),
\]

we have

\[
\frac jz=\frac{(7+2t)(11-2t)}{2a-1}.
\]

The exact one-sided bounds relevant to

\[
L=j-h+5w+85z
\]

are

\[
\frac jz<9,
\qquad
-\frac hz<\frac19,
\qquad
5\frac wz<5.
\]

The second bound uses only the branch where `h<0`; when `h>=0`, `-h<=0`.
Therefore

\[
\frac Lz<9+\frac19+5+85=\frac{892}{9}.
\]

Since `A/z>5`,

\[
\boxed{\frac LA<\frac{892}{45}<20}.
\]

As `L=nA` with positive integer `n`, the sharpened conclusion remains

\[
\boxed{n\in\{1,\ldots,19\}}.
\]

As `a->5+` and `t->1-`, the ratio `L/A` tends to `892/45`. Hence this is the exact continuous supremum of the argument.

## `n=19` is active over the real chamber

Set `z=1000`, `w=900`. Exact evaluation gives

\[
F_{19}(5170,1000,900)=-1733592000<0,
\]

\[
F_{19}(5171,1000,900)=106817836>0.
\]

By continuity, there is a real `A in (5170,5171)` with

\[
F_{19}(A,1000,900)=0.
\]

This point lies in the strict chamber because `A>5000=5z>w>0`.

Therefore `19` is not merely a loose integer ceiling: the nineteenth cubic meets the real chamber. Rational/integral admissibility together with the original divisor and primitive conditions remains open.

Status:

- integer range: `CLOSED_SYMBOLIC`;
- real chamber activity of `n=19`: `CLOSED_REAL`;
- rational/integral realization: `OPEN`.
