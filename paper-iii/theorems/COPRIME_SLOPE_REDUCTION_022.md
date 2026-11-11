# RGΦ Round 022-E — reducción coprima por pendiente

Sea \([A:C:D]\) una solución integral primitiva de la forma frontera, con \(\gcd(C,D)=1\) y \(0<C<D\). Escribimos la pendiente reducida
\[
m=D/C=r/s,\qquad \gcd(r,s)=1.
\]
Entonces necesariamente
\[
\boxed{C=s,\qquad D=r.}
\]

## Ecuación cuadrática de escala

La cúbica frontera se convierte en
\[
\boxed{(4s+324r)A^2-(n+148)rsA-4(s^3+r^3)=0.}
\]
Por tanto
\[
\boxed{\Delta_n(r,s)=(n+148)^2r^2s^2+16(4s+324r)(s^3+r^3)}
\]
debe ser un cuadrado perfecto, y
\[
\boxed{A=\frac{(n+148)rs\pm\sqrt{\Delta_n(r,s)}}{2(4s+324r)}}
\]
debe ser entero.

## Cámara

\[
\boxed{\frac{9A}{5}<s<r<2A,}
\]
y por tanto
\[
\boxed{1<r/s<10/9.}
\]

Para \(n\) impar, el teorema de paridad de Round 021 reduce la divisibilidad cúbica al filtro \(A\) impar.

La enumeración efectiva de puntos relativos-integrales queda así convertida en un problema explícito de cuadrados perfectos y divisibilidad para pares coprimos en una banda estrecha de pendientes.
