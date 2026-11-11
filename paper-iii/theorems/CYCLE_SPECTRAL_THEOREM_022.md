# RGΦ Round 022-B — teorema espectral de ciclos

Supongamos que una palabra admisible de longitud \(m\) regresa al estado primitivo inicial: \(v_m=v_0\).

## Teorema 022-B

El vector \(v_0\) es un autovector entero del producto de ramas \(M_w\), con autovalor igual al producto de defectos:
\[
M_wv_0=\Delta_wv_0.
\]
Como \(\det M_w=B^m\), el segundo autovalor es \(B^m/\Delta_w\). Por tanto
\[
\boxed{\operatorname{tr}(M_w)=\Delta_w+\frac{B^m}{\Delta_w}}
\]
y
\[
\boxed{\operatorname{tr}(M_w)^2-4B^m=\left(\frac{B^m}{\Delta_w}-\Delta_w\right)^2.}
\]

## Obstrucción espectral cuadrada

Toda secuencia de ramas que soporte un ciclo racional debe satisfacer que
\[
\boxed{\operatorname{tr}(M_w)^2-4\det(M_w)}
\]
sea un cuadrado entero perfecto.

## Criterio recíproco

Si un producto de ramas posee un rayo propio racional positivo, su vector primitivo atraviesa los dominios de rama declarados y la órbita primitiva regresa al inicio, entonces define un ciclo RGΦ y el autovalor positivo es exactamente el producto de defectos.

Para
\[
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
el punto fijo proyectivo satisface
\[
\boxed{cx^2+(d-a)x-b=0,}
\]
de modo que la racionalidad vuelve a exigir el mismo discriminante cuadrado.
