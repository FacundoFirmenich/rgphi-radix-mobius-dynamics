# Cara 6 — Operador ramanujiano de subanidación UMI

## Boundary del nombre

«Ramanujiano» es una denominación interna. No se atribuye este operador a la obra histórica de Srinivasa Ramanujan.

## Dominio

Un segmento orientado es

\[
S=(x,v,g),
\]

donde `x in R^2`, `v != 0` y `g in D3`.

Sea `sigma(g) in {-1,0,+1}`. Definimos

\[
r_0=1/4,
\qquad
r_\pm=1/3,
\]

\[
\theta_\sigma=(0,\sigma\pi/3,-\sigma\pi/3,0).
\]

## Operador elemental

Los hijos son

\[
v_j=r_{\sigma(g)}R_{\theta_{\sigma(g),j}}v,
\]

\[
x_0=x,
\qquad
x_j=x+\sum_{k<j}v_k.
\]

Definimos

\[
\boxed{\mathscr R_g(S)=\{(x_j,v_j,g):j=0,1,2,3\}.}
\]

## Invariante endpoint

\[
\boxed{\sum_{j=0}^{3}v_j=v.}
\]

La geometría interna cambia sin alterar los extremos del padre.

## Forma matricial

Cada hijo posee una matriz afín homogénea

\[
M_{g,j}=
\begin{pmatrix}
r_{\sigma(g)}R_{\theta_{\sigma(g),j}}&t_{g,j}\\
0\;0&1
\end{pmatrix}.
\]

Para una dirección

\[
\omega=((g_1,j_1),\ldots,(g_n,j_n)),
\]

\[
\boxed{M_\omega=M_{g_1,j_1}\cdots M_{g_n,j_n}.}
\]

## Cociclos

Escala:

\[
\boxed{\rho(\omega)=\prod_{k=1}^{n}r_{\sigma(g_k)}.}
\]

Cara:

\[
\boxed{G(\omega)=g_n\cdots g_1\in D_3.}
\]

La concatenación satisface

\[
M_{\omega\eta}=M_\omega M_\eta,
\qquad
\rho(\omega\eta)=\rho(\omega)\rho(\eta).
\]

## Realizaciones

- fase activa constante: curva de Koch;
- cierre triangular y órbita `D3`: copo de Koch;
- fase latente constante: segmento;
- fase variable: UMI no estacionaria;
- pesos no uniformes: medida multifractal.

El operador queda definido por dominio, sustitución, composición, invariante endpoint, cociclo de escala, cociclo de cara y criterio de multifractalidad.
