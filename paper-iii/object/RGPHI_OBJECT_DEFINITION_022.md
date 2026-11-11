# RGΦ Round 022 — definición canónica del objeto matemático

## 1. Retícula proyectiva primitiva

Sea
\[
\Lambda=\{(p,q)\in\mathbb Z_{>0}^2:\ 0<p<q,\ \gcd(p,q)=1\},
\]
y su cono high
\[
\Lambda^+=\{(p,q)\in\Lambda:\ q/2<p<q\}.
\]
La proyección racional es \(\pi(p,q)=p/q\). Para un vector entero no nulo \(u\), definimos
\[
\operatorname{cont}(u)=\gcd(|u_1|,|u_2|),\qquad
\operatorname{prim}(u)=u/\operatorname{cont}(u).
\]

## 2. Matrices de rama

Fijada una base \(B\ge2\), para \(0\le k\le B-1\) definimos
\[
A_k=\begin{pmatrix}B&-k\\0&1\end{pmatrix},\qquad
C_k=\begin{pmatrix}1&0\\1-B-k&B\end{pmatrix}.
\]
Ambas tienen determinante \(B\), y \(C_k=HA_kH^{-1}\) con
\[
H=\begin{pmatrix}0&1\\1&1\end{pmatrix}.
\]

Para \(v=(p,q)\in\Lambda\), ponemos
\[
\kappa_T(v)=\left\lfloor\frac{Bp}{q}\right\rfloor,
\]
y, para \(v\in\Lambda^+\),
\[
\kappa_S(v)=\left\lfloor\frac{B(q-p)}{p}\right\rfloor.
\]
Los operadores primitivos son
\[
\widehat T_B(v)=\operatorname{prim}(A_{\kappa_T(v)}v),\qquad
\widehat S_B(v)=\operatorname{prim}(C_{\kappa_S(v)}v).
\]

## 3. Cociclo de defecto

Definimos
\[
\delta_T(v)=\operatorname{cont}(A_{\kappa_T(v)}v),\qquad
\delta_S(v)=\operatorname{cont}(C_{\kappa_S(v)}v).
\]
Para \(v=(p,q)\) primitivo,
\[
\boxed{\delta_T(v)=\gcd(q,B)},\qquad
\boxed{\delta_S(v)=\gcd(p,B)}.
\]

## 4. Objeto ambiente

El **sistema proyectivo de reducción de contenido radix–Möbius** es
\[
\boxed{\mathfrak{RG}_{\Phi}(B)=(\Lambda^+,\widehat T_B,\widehat S_B,\kappa_T,\kappa_S,\delta_T,\delta_S).}
\]
Es un autómata determinista de dos letras sobre rayos primitivos de la retícula, equipado con una representación matricial por ramas y un cociclo entero multiplicativo de contenido.

## 5. Equivalencia exacta con la dinámica racional

Para \(x=p/q\) reducido,
\[
T_B(x)=\{Bx\},\qquad S_B=\Phi\circ T_B\circ\Phi^{-1},\qquad \Phi(x)=\frac1{1+x}.
\]
Entonces
\[
\boxed{\pi\circ\widehat T_B=T_B\circ\pi,\qquad \pi\circ\widehat S_B=S_B\circ\pi.}
\]

## 6. Objetos finitos

Un **objeto RGΦ finito high** es un subconjunto finito \(F\subset\Lambda^+\) cerrado bajo ambos operadores y cuyo digrafo etiquetado por \(T,S\) es fuertemente conexo. Equivale exactamente a una SCC racional cerrada all-high.

Dos objetos son isomorfos si una biyección de estados entrelaza ambos operadores y preserva los defectos. La dualidad \(T\leftrightarrow S\) es inducida por \(\Phi\).

## Freeze conceptual

Desde Round 022 el objeto deja de ser provisional:

> RGΦ estudia subautómatas finitos, invariantes y transitivos de una acción proyectiva entera por matrices de determinante \(B\), seguida de normalización primitiva, junto con su cociclo de contenido.

Lo que permanece abierto no es la definición, sino la clasificación aritmética de sus realizaciones finitas.
