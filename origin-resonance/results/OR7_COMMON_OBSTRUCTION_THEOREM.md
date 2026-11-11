# OR-7 — common-obstruction / defect-completion theorem

For a point on one of the Round-019 cubics put

\[
C=2A-z,
\qquad
D=2A-w,
\]

\[
f=(2z-3w)(2z-w),
\qquad
g=(7z+2w)(11z-2w).
\]

On `F_n=0` the exact identity is

\[
gD-fC+(5w+85z-nA)CD=0.
\]

Let

\[
d=\gcd(C,D),
\qquad C=dc,
\qquad D=de,
\qquad \gcd(c,e)=1.
\]

Dividing by `d` and reducing modulo `c` and `e` gives

\[
\boxed{C/d\mid g},
\qquad
\boxed{D/d\mid f}.
\]

Therefore the reduced denominators of

\[
g/C,
\qquad
f/D
\]

both divide the single common obstruction `d`.

The coprime-completion theorem is the special case `d=1`.

## Round-020 point

For

\[
(A,z,w)=(64233,11741,1138),
\]

we have

\[
C=116725,
\qquad D=127328,
\qquad d=23.
\]

Moreover

\[
f/D=80997/23,
\qquad
g/C=2111575/23.
\]

Thus both reduced defect denominators equal `d` rather than merely dividing it.

Status: `CLOSED_SYMBOLIC`.
