# Teorema T012‑C — Frontera exacta entre superacceso e hiperacceso

Para un conjunto finito de primos \(E\), sea

\[
\Pi_E(N)=\frac{N}{\prod_{p\in E}p^{v_p(N)}}.
\]

Para una familia \(E_1,\ldots,E_r\),

\[
\boxed{
\operatorname{sgn}(N)\operatorname{mcm}_i|\Pi_{E_i}(N)|
=\Pi_{\cap_iE_i}(N).
}
\]

Sobre la imagen \(K(\Sigma^*)=8+9\mathbb Z\), todos los enteros se recuperan uniformemente si y sólo si

\[
\boxed{\bigcap_iE_i\subseteq\{3\}.}
\]

Esto es **superacceso**: recuperación de la magnitud aritmética interna \(K\).

Sin embargo, todas las palabras

\[
C(K),\ 8C(K),\ 88C(K),\ldots
\]

poseen el mismo \(K\). En consecuencia, ninguna cantidad de observables que factoricen exclusivamente por \(K\) puede recuperar el prefijo \(t\).

La información residual es **hiperacceso**:

- con longitud exacta, el rango \(j\) selecciona la palabra y determina \(t\);
- con una ventana, un rango ordena los pares \((j,t)\);
- con un lenguaje regular, la órbita de prefijos selecciona los \(t\) admisibles.

El diagrama exacto es

\[
\boxed{
\text{observables primitivos}
\overset{\rm superacceso}{\longrightarrow}K
\overset{\rm hiperacceso}{\longrightarrow}w.
}
\]

La primera flecha completa la aritmética; la segunda sincroniza esa aritmética con su escritura literal exacta.