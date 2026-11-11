# RGΦ Round 019-C — elliptic reduction of DF015-0015

The strict-T factor-three form has A>5z>w>0, C=2A-z, D=2A-w and

D | C^2-A^2,  C | (A+4z)^2-(z-w)^2,  A | z^3+w^3.

Set

f=(2z-3w)(2z-w),  g=(7z+2w)(11z-2w),

h=f/D,  j=g/C.

## Linear quotient theorem

The defining identities and A|(z^3+w^3) imply

A | L:=j-h+5w+85z.

Moreover |h|<4z/9 and 0<j<9z, so 0<L<100z. Since A>5z,

L=nA for one n in {1,...,19}.

## Nineteen plane cubics

Eliminating h and j yields

F_n(A,z,w)=4nA^3-2nA^2(w+z)+nAwz-20A^2w-340A^2z
+24Aw^2+148Awz+24Az^2-4(z^3+w^3)=0.

Every global realization lies on one of these nineteen curves and must additionally satisfy the original divisor, primitive and high conditions.

## Smoothness and elliptic structure

For every n=1,...,19, exact Groebner elimination of ∂_A F_n=∂_z F_n=∂_w F_n=0 in each projective affine chart returns the unit ideal. Thus F_n=0 is a smooth projective plane cubic. It contains [0:1:-1], hence each curve is an elliptic curve over Q once that point is selected as origin.

Projection from [0:1:-1] gives a binary quartic Y^2=Δ_n(m), where

Δ_n(m)=-48m^4+(8n+1952)m^3+(n^2+200n+10960)m^2
-(8n^2+1328n+72000)m+16n^2+1600n+102400.

## Boundary

This is a structural reduction, not a no-go theorem. Rational points must still satisfy h,j integrality, the original divisibilities, reducedness and the high inequalities. DF015-0015 remains OPEN_ELLIPTIC_REDUCED.
