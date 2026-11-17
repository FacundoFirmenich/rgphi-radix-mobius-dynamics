# Auditoría T010-G — Oscilación e incertidumbre

Una oscilación clásica con fase desconocida produce dispersión estadística, pero no es automáticamente el principio de incertidumbre de Heisenberg.

La tripolaridad demuestra \(\operatorname{Var}(U)>0\) bajo una distribución no degenerada. Eso es incertidumbre clásica o epistémica.

Para obtener una relación cuántica genuina se añade condicionalmente un modelo qutrit. Sea

\[
J_z=\operatorname{diag}(-1,0,1)
\]

y sea \(F_3\) la transformada discreta de Fourier de dimensión tres. Definimos

\[
J_x=F_3J_zF_3^\dagger,
\qquad
\widehat U_n=C_nI+aJ_z,
\qquad
\widehat V=aJ_x.
\]

Entonces

\[
[J_z,J_x]\neq0
\]

y, para cualquier estado,

\[
\boxed{\Delta U_n\,\Delta V\ge\frac12|\langle[\widehat U_n,\widehat V]\rangle|.}
\]

Las dos bases son mutuamente insesgadas, por lo que sus entropías obedecen

\[
\boxed{H_z+H_x\ge\log3.}
\]

Corolario autorizado:

- oscilación intrínseca sola: dispersión clásica;
- tripolaridad cuantizada con observable conjugado: incertidumbre no conmutativa genuina del modelo.

No se afirma que la UMI sea físicamente un qutrit.
