# Teorema T012‑B — Complejidad óptima del hiperacceso

## Longitud exacta

Con \(h\) y \(\ell\) conocidos, existen exactamente \(A_h(\ell)\) palabras compatibles. El coste zero‑error mínimo y suficiente es

\[
\boxed{B_h(\ell)=\lceil\log_2A_h(\ell)\rceil.}
\]

La llave óptima es el rango \(j\).

## Minimax

Sea \(\alpha=\log_{10}343\). Entonces

\[
\boxed{A_{\max}(\ell)=1+\left\lfloor\frac{\ell}{\alpha}\right\rfloor}
\]

y

\[
\boxed{B_{\max}(\ell)=\left\lceil\log_2\left(1+\left\lfloor\frac{\ell}{\alpha}\right\rfloor\right)\right\rceil.}
\]

Por tanto

\[
B_{\max}(\ell)=\log_2\ell-\log_2\alpha+O(1),
\qquad
\frac{B_{\max}(\ell)}{\ell}\to0.
\]

## Longitud sólo acotada

Si sólo se conoce \(|w|\le L\),

\[
\boxed{S_{\max}(L)=\sum_{\ell=0}^{L}\left(1+\left\lfloor\frac{\ell}{\alpha}\right\rfloor\right)}
\]

y

\[
S_{\max}(L)=\frac{L^2}{2\alpha}+O(L),
\qquad
B_{\max}^{\le}(L)=2\log_2L+O(1).
\]

También \(B_{\max}^{\le}(L)/L\to0\).

Sin cota de longitud, la fibra de prefijos es infinita y no existe llave finita uniforme.

## Dimensión hiperaccesible

Definiendo

\[
d_{\rm hyp}=\limsup_{L\to\infty}\frac{B(L)}{\log_2L},
\]

se obtiene

\[
\boxed{d_{\rm hyp}=1}
\]

con longitud exacta, y

\[
\boxed{d_{\rm hyp}=2}
\]

con longitud sólo acotada. El coeficiente logarítmico cuenta las coordenadas internas no resueltas.