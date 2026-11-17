# Teorema T013‑C — Composición de la cuadrícula FST con las caras \(D_3\)

Sea \(\mathcal F_{h,\ell}=\{w:H(w)=h,|w|=\ell\}\), con cardinalidad \(A_h(\ell)\), y sea \(G=D_3\), \(|G|=6\).

Para profundidad \(N\):

\[
\mathcal X_{h,\ell,N}=\mathcal F_{h,\ell}\times G^N.
\]

## Historia completa

Observando sólo \((h,\ell)\), la fibra contiene

\[
\boxed{A_h(\ell)6^N}
\]

completitudes. Su recuperación es superacceso extensivo.

## Producto total

Sea \(G_N=g_N\cdots g_1\). Para cada valor fijado de \(G_N\), la aplicación \(G^N\to G\) tiene exactamente

\[
\boxed{6^{N-1}}
\]

preimágenes. Por tanto, observando \((h,\ell,G_N)\), la fibra contiene

\[
\boxed{A_h(\ell)6^{N-1}}
\]

estados.

El producto total no recupera la historia.

## Torre coherente

Si \(g_1=\cdots=g_N=g\), sólo existen seis torres. La llave cuesta

\[
\log_2 6
\]

bits y su tasa \(\log_2(6)/N\to0\): hiperacceso hexafacial fuerte.

Si sólo queda indeterminada la fase biplanar, la llave cuesta \(\log_2 3\) bits.

## Composición con FST

Con longitud exacta y cara global desconocida hay \(6A_h(\ell)\) completitudes; con sólo la fase desconocida hay \(3A_h(\ell)\).

## Boundary

Esta construcción es un producto de fibras. No se ha demostrado una acción no trivial de \(D_3\) sobre \((j,t)\); una extensión semidirecta sigue abierta.
