# RGΦ Round 022-A — teorema del cociclo matricial de contenido

Sea \(v_0\in\Lambda^+\) y sea \(w=g_m\cdots g_1\), con \(g_i\in\{T,S\}\), una palabra admisible a lo largo de la órbita \(v_i=\widehat g_i(v_{i-1})\). Sea \(M_i\) la matriz de rama correspondiente y \(d_i=\delta_{g_i}(v_{i-1})\). Definimos
\[
M_w=M_m\cdots M_1,\qquad \Delta_w=\prod_{i=1}^m d_i.
\]

## Teorema 022-A

\[
\boxed{M_wv_0=\Delta_wv_m.}
\]

Cada paso satisface \(M_iv_{i-1}=d_iv_i\); la composición telescópica prueba la identidad.

## Consecuencias

1. \(\Delta\) es un cociclo multiplicativo sobre las palabras admisibles.
2. \(\det M_w=B^m\).
3. Toda órbita se traduce a un producto matricial entero más un cociclo escalar.
4. La pérdida de primitividad es una coordenada estructural del sistema, no ruido computacional.
