# Teorema T013‑A — Complejidad temporal sensible a la salida

Sea

\[
w_j=8^{\ell-|C(K_0\,343^j)|}C(K_0\,343^j)
\]

el candidato de rango \(j<A_h(\ell)\).

Denotemos por \(\mathsf M(n)\) el coste de multiplicar enteros de \(n\) bits y por \(\mathsf D_{10}(n)\) el coste de conversión decimal.

## Decodificación

Un algoritmo exacto calcula \(K_0\), \(343^j\), \(K_j=K_0 343^j\), el representante canónico y los prefijos. Su coste es

\[
T_{\rm dec}(\ell,j)
=O\!\left(\mathsf M(n)\log(j+2)+\mathsf D_{10}(n)+\ell\right),
\qquad n=\Theta(\ell).
\]

Como \(j=O(\ell)\), con aritmética rápida:

\[
\boxed{T_{\rm dec}(\ell)=\widetilde O(\ell).}
\]

Toda reconstrucción explícita debe escribir \(\ell\) cifras, luego

\[
\boxed{T_{\rm dec}(\ell)=\Omega(\ell).}
\]

La reconstrucción es output-optimal salvo factores polilogarítmicos.

## Enumeración de una fibra

Para \(A=A_h(\ell)\), la salida contiene \(A\ell\) cifras:

\[
\Omega(A\ell)\le T_{\rm list}\le\widetilde O(A\ell).
\]

Como \(A=O(\ell)\), el peor caso es cuasi-cuadrático y sensible a la salida.

## Lenguajes condicionantes

Si pertenecer a \(L\) cuesta \(T_L(\ell)\), el inverso condicionado se resuelve en

\[
O\!\left(A_h(\ell)[T_{\rm dec}(\ell)+T_L(\ell)]\right).
\]

## Boundary

FST‑13 cerró la optimalidad informacional. Este resultado no demuestra una cota temporal exacta \(\Theta(\ell)\) en todos los modelos; deja una brecha polilogarítmica dependiente de multiplicación y conversión de base.
