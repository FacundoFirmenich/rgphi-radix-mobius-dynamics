# HA-005-E — factor splitting in the elliptic boundary normal form

Let

\[
G_n(A,C,D)=4C^3+4D^3+(n+148)ACD-4A^2C-324A^2D=0
\]

be the boundary-coordinate cubic for `DF015-0015`. For a valid primitive candidate assume

\[
\gcd(A,C)=\gcd(A,D)=\gcd(C,D)=1
\]

and `A | C^3+D^3`.

Reducing the cubic modulo the three coordinates gives

\[
\boxed{D\mid4(C-A)(C+A)},
\]

\[
\boxed{C\mid4(D-9A)(D+9A)},
\]

\[
\boxed{A\mid(C+D)(C^2-CD+D^2)}.
\]

The overlaps satisfy

\[
\gcd(D,C-A,C+A)\mid2,
\]

\[
\gcd(C,D-9A,D+9A)\mid18,
\]

\[
\gcd(A,C+D,C^2-CD+D^2)\mid3.
\]

Hence every odd prime power of `D` allocates uniquely between `C-A` and `C+A`; every prime power `ell>=5` of `C` allocates uniquely between `D-9A` and `D+9A`; and every prime power `ell!=3` of `A` allocates uniquely between the two factors of `C^3+D^3`.

This sharpens the effective relative-integral search but does not enumerate the finite candidate set.
