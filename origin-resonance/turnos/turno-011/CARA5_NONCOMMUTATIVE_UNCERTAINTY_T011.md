# Cara 5 — Indeterminación no conmutativa de seis caras

Definimos el espacio condicional

\[
\mathcal H_6=\mathbb C^2\otimes\mathbb C^3
\]

con base

\[
|\varepsilon,\sigma\rangle,
\qquad
\varepsilon\in\{0,1\},
\quad
\sigma\in\{-1,0,+1\}.
\]

El operador tripolar es

\[
Z|\varepsilon,\sigma\rangle=\sigma|\varepsilon,\sigma\rangle.
\]

El cambio de plano con inversión polar es

\[
S|\varepsilon,\sigma\rangle=|1-\varepsilon,-\sigma\rangle.
\]

Entonces

\[
S^2=I,
\qquad
SZS=-Z,
\]

por lo que

\[
\boxed{\{S,Z\}=0},
\qquad
\boxed{[Z,S]=2ZS\neq0.}
\]

Con

\[
C_n=\frac{5\pi}{3}10^n,
\qquad
a_n=\frac{\pi}{9}10^n,
\]

definimos

\[
\widehat U_n=C_nI+a_nZ,
\qquad
\widehat V_n=a_nS.
\]

Para cualquier estado:

\[
\Delta U_n\Delta V_n
\ge
\frac12\left|\langle[\widehat U_n,\widehat V_n]\rangle\right|.
\]

En el subespacio generado por `|0,+>` y `|1,->`, el estado

\[
|\psi_*\rangle=\frac{|0,+\rangle+i|1,-\rangle}{\sqrt2}
\]

satisface

\[
\Delta U_n=\Delta V_n=a_n,
\]

\[
\frac12\left|\langle[\widehat U_n,\widehat V_n]\rangle\right|=a_n^2.
\]

Por tanto la desigualdad se satura.

**Boundary:** la oscilación geométrica sola es clásica. La relación de indeterminación surge al añadir esta álgebra no conmutativa. No se afirma una realización cuántica física.
