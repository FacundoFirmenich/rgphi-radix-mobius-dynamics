# Teorema T013‑B — Fuentes no uniformes y codificación adaptada

Sea \(W_\ell\) una fuente arbitraria y \(Y_\ell=(H(W_\ell),\ell)\). Para cada fibra \(\mathcal F_y\), sea \(p_y\) la distribución posterior.

\[
\boxed{H(W_\ell\mid Y_\ell)=\sum_y\Pr(Y_\ell=y)H(p_y).}
\]

La constante uniforme de FST‑13 es sólo un caso particular.

## Huffman condicionado

Para cada fibra ambigua existe un código Huffman con

\[
H(p_y)\le L_y<H(p_y)+1,
\]

y \(L_y=0\) para fibras unitarias. Por tanto

\[
\boxed{H(W_\ell\mid Y_\ell)\le\mathbb E[L]<H(W_\ell\mid Y_\ell)+\Pr(|\mathcal F_{Y_\ell}|\ge2).}
\]

## Fuente uniforme

Con \(q=343\) y

\[
p_f=\frac{f(q-1)^2}{q^{f+1}},
\]

la longitud Huffman media de una fibra uniforme de tamaño \(f\) es

\[
L_H(f)=k_f+2-\frac{2^{k_f+1}}f,
\qquad k_f=\lfloor\log_2 f\rfloor.
\]

Así

\[
\boxed{L_{H,\infty}=0.005839403722087393457897486756\ldots\text{ bits}.}
\]

Y

\[
H_\infty<L_{H,\infty}<\bar B_\infty.
\]

## Fuentes geométricas y Markovianas

Para un posterior geométrico truncado

\[
p(j)=\frac{(1-r)r^j}{1-r^A},
\]

la entropía es

\[
H_A(r)=\log_2\frac{1-r^A}{1-r}-\mathbb E[j]\log_2r.
\]

En el límite

\[
H_\infty(r)=-\log_2(1-r)-\frac{r}{1-r}\log_2r.
\]

Para una fuente Markoviana de primer orden, los \(A_h(\ell)=O(\ell)\) candidatos permiten calcular el posterior y su entropía en \(O(\ell^2)\) operaciones elementales por observación.

## Boundary

No existe una única entropía de hiperacceso independiente de fuente, observación, posterior y código.
