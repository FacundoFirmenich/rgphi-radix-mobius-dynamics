# Teorema T012‑A — Geometría escalonada de la UMI‑FST

Sea

\[
K(w)=8\,10^{|w|}-9\operatorname{val}(w),
\qquad
H(w)=\Pi_7(K(w)).
\]

Para cada etiqueta admisible \(h\), existe \(K_0=7^{a_0(h)}h\), y toda palabra de su fibra posee representación única

\[
\boxed{w=8^tC(K_0\,343^j),\qquad(j,t)\in\mathbb N_0^2.}
\]

Definimos la UMI de fibra

\[
\mathcal U_h=\mathbb N_0^2
\]

con ejes latentes:

- \(j\): profundidad multiplicativa \(343^j\);
- \(t\): profundidad literal de prefijación por ocho.

Si \(\ell_{h,j}=|C(K_0\,343^j)|\), la longitud total es

\[
\boxed{L_h(j,t)=\ell_{h,j}+t.}
\]

A longitud exacta \(\ell\), la sección observacional es

\[
\mathcal S_{h,\ell}=\{(j,t):L_h(j,t)=\ell\}.
\]

Como \(t=\ell-\ell_{h,j}\), queda parametrizada por los \(j\) con \(\ell_{h,j}\le\ell\), y

\[
\boxed{|\mathcal S_{h,\ell}|=A_h(\ell).}
\]

Así:

- observar sólo \(h\) deja visible toda la cuadrícula \(\mathbb N_0^2\);
- observar \((h,\ell)\) la corta mediante una sección finita;
- añadir el rango \(j\) selecciona un único punto y determina \(t\).

Las longitudes canónicas satisfacen

\[
\#\{j:\ell_{h,j}\le N\}=\frac{N}{\log_{10}343}+O_h(1),
\]

con pendiente irracional. La frontera escalonada no es finalmente periódica.