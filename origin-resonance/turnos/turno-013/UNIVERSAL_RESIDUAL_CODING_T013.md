# Teorema T013‑F — Codificación residual universal

Sea una fibra ordenada \(\mathcal F_{h,\ell}=\{w_0,\ldots,w_{A-1}\}\).

## Minimax conocido

Con \(A\) conocido, el código fijo zero-error óptimo requiere

\[
\boxed{\lceil\log_2A\rceil}
\]

bits.

## Código universal de rango

Codificamos \(n=j+1\) mediante Elias delta. Si \(L=\lfloor\log_2n\rfloor+1\), la longitud es

\[
\ell_\delta(n)=L+2\lfloor\log_2L\rfloor.
\]

Como \(n\le A\):

\[
\boxed{\ell_\delta(j+1)\le\log_2A+2\log_2\log_2A+O(1).}
\]

Para \(A=\Theta(\ell)\):

\[
\boxed{\ell_\delta=\log_2\ell+2\log_2\log_2\ell+O(1).}
\]

La tasa por cifra tiende a cero.

## Longitud sólo acotada

El rango de los pares \((j,t)\) es \(S_{\max}(L)=\Theta(L^2)\). Un código delta universal usa

\[
\boxed{2\log_2L+2\log_2\log_2L+O(1)}
\]

bits.

## Fuente conocida

Huffman minimiza la longitud media prefix-free; la codificación aritmética por bloques aproxima la entropía condicional.

Bajo la fuente uniforme:

\[
H_\infty=0.005837332402614633262\ldots,
\]

\[
L_{\rm Huff,\infty}=0.005839403722087393458\ldots,
\]

\[
\bar B_\infty=0.005847854308123188049\ldots,
\]

con

\[
\boxed{H_\infty<L_{\rm Huff,\infty}<\bar B_\infty.}
\]

## Boundary

Estos códigos presuponen que la etiqueta y el marco de longitud están disponibles. No comprimen la palabra arbitraria completa a \(O(\log\ell)\) bits.
