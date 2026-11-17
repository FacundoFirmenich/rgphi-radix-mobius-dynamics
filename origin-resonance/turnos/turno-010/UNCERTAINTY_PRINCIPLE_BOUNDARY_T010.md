# Auditoría T010-G RC1 — Oscilación e incertidumbre

La semiamplitud correcta es

\[
a_n=\frac{\pi}{9}10^n.
\]

Con pesos uniformes sobre los tres hitos:

\[
\boxed{\operatorname{Var}(U)=\frac23a_n^2=\frac{2\pi^2}{243}10^{2n}.}
\]

Con fase continua uniforme:

\[
\boxed{\operatorname{Var}(U)=\frac12a_n^2=\frac{\pi^2}{162}10^{2n}.}
\]

Esto es dispersión clásica.

Para un modelo no conmutativo condicional, sea

\[
J_z=\operatorname{diag}(-1,0,1),
\qquad
J_x=F_3J_zF_3^\dagger.
\]

Definimos

\[
\widehat U_n=C_nI+a_nJ_z,
\qquad
\widehat V_n=a_nJ_x.
\]

Entonces

\[
[\widehat U_n,\widehat V_n]=a_n^2[J_z,J_x]\neq0
\]

y

\[
\Delta U_n\Delta V_n\ge\frac12\left|\langle[\widehat U_n,\widehat V_n]\rangle\right|.
\]

No se afirma una realización física.
