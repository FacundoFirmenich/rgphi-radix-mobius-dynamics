# RGΦ Round 022-D — forma normal elíptica en coordenadas de frontera

Introducimos la transformación unimodular
\[
C=2A-z,\qquad D=2A-w,
\]
con inversa \(z=2A-C\), \(w=2A-D\).

## Cúbica de frontera

La ecuación secundaria \(F_n(A,z,w)=0\) se reduce exactamente a
\[
\boxed{4C^3+4D^3+(n+148)ACD-4A^2C-324A^2D=0.}
\]

La cámara \(A>5z>w>0\) equivale a
\[
\boxed{\frac{9A}{5}<C<D<2A.}
\]
La condición coprima es \(\gcd(C,D)=1\). El punto universal \([A:z:w]=[1:2:2]\) se convierte en \([A:C:D]=[1:0:0]\). Además
\[
A\mid z^3+w^3\iff A\mid C^3+D^3.
\]

## Proyección cuártica desde la frontera

En la carta \(A=1\), escribimos \(x=C/A\) y \(m=D/C\). Fuera del punto frontera,
\[
4(1+m^3)x^2+(n+148)mx-(4+324m)=0.
\]
Definiendo
\[
Y=8(1+m^3)x+(n+148)m,
\]
obtenemos
\[
\boxed{Y^2=5184m^4+64m^3+(n+148)^2m^2+5184m+64.}
\]
La inversa es
\[
\boxed{x=\frac{Y-(n+148)m}{8(1+m^3)},\qquad D/A=mx.}
\]

Esta es una representación birracional más simple del frente elíptico, salvo los puntos excepcionales de la proyección.
