# D₃ exacta — simetría hexafacial de la UMI

## 1. Corrección estructural

Las seis caras pueden escribirse como conjunto

\[
\mathcal F_6=\{M,m\}\times\{-,0,+\},
\]

pero su ley interna **no** es el producto directo abeliano
\(\mathbb Z_2\times\mathbb Z_3\cong C_6\).

La simetría correcta es el producto semidirecto

\[
\boxed{
D_3\cong\mathbb Z_3\rtimes_{\iota}\mathbb Z_2,
\qquad
\iota(1)(k)=-k.
}
\]

Equivalentemente,

\[
\boxed{
D_3=\langle r,s\mid r^3=s^2=e,\ srs=r^{-1}\rangle.
}
\]

## 2. Etiquetado de caras

Representamos cada elemento como

\[
g_{\varepsilon,k}=r^k s^{\varepsilon},
\qquad
\varepsilon\in\mathbb Z_2,
\quad
k\in\mathbb Z_3.
\]

La multiplicación es

\[
\boxed{
(\varepsilon,k)(\eta,\ell)
=
\bigl(\varepsilon+\eta,\ k+(-1)^\varepsilon\ell\bigr),
}
\]

con las componentes tomadas módulo 2 y módulo 3.

Usamos la identificación

\[
0\leftrightarrow0,
\qquad
+\leftrightarrow1,
\qquad
-\leftrightarrow2=-1\pmod3.
\]

Las seis caras son

\[
\begin{array}{lll}
(M,0)=e, & (M,+)=r, & (M,-)=r^2,\\
(m,0)=s, & (m,+)=rs, & (m,-)=r^2s.
\end{array}
\]

## 3. Cambio de plano

La acción del cambio de plano es la multiplicación izquierda por \(s\):

\[
\boxed{
S(P,k)=(\bar P,-k).
}
\]

Por tanto

\[
(M,+)\leftrightarrow(m,-),
\]

\[
(M,-)\leftrightarrow(m,+),
\]

\[
(M,0)\leftrightarrow(m,0).
\]

El centrum trifásico queda fijo; las dos polaridades se intercambian.

## 4. Expresión numérica tripolar

Con la corrección vinculante

\[
U_{n,\sigma}
=
C_n\left(1+\frac{\sigma}{15}\right),
\qquad
\sigma\in\{-1,0,+1\},
\]

la involución de plano actúa como

\[
\boxed{
U_{n,\sigma}\longmapsto U_{n,-\sigma}=2C_n-U_{n,\sigma}.
}
\]

En la normalización unitaria

\[
\left(\frac{14}{15},1,\frac{16}{15}\right),
\]

la acción es

\[
\boxed{x\longmapsto2-x.}
\]

Así, \(14/15\leftrightarrow16/15\) y \(1\) permanece fijo.

## 5. Representación sobre seis caras

En la base \(|P,k\rangle\), definimos

\[
R|P,k\rangle=|P,k+1\rangle,
\]

\[
S|P,k\rangle=|\bar P,-k\rangle.
\]

Entonces

\[
R^3=S^2=I,
\qquad
SRS=R^{-1}.
\]

Esta representación expresa simultáneamente:

- dos planos;
- tres fases;
- inversión polar al cambiar de plano;
- no conmutatividad del orden de las operaciones.

## 6. Koch

La envolvente convencionalmente llamada copo de Koch posee simetría global \(D_3\): tres rotaciones y tres reflexiones. En la lectura UMI, las reflexiones implementan el cambio de plano con inversión de polaridad y las tres clases rotacionales implementan la expresión trifásica.

## 7. Estatuto

**Estado:** `CLOSED_EXACT_D3_SEMIDIRECT_SYMMETRY`.

La hexafacialidad es \(2\times3\) como cardinalidad y \(\mathbb Z_3\rtimes\mathbb Z_2\) como ley. No debe sustituirse por \(C_6\).