# Cara 1 — Multifractalización efectiva Koch–UMI

La rama activa de Koch posee cuatro similitudes de razón `1/3` y soporte de dimensión

\[
D_K=\frac{\log4}{\log3}.
\]

La sombra UMI corregida es `(14,15,16)`. Sobre los cuatro subsegmentos definimos

\[
w^+=\frac1{60}(15,14,16,15),
\qquad
w^-=\frac1{60}(15,16,14,15).
\]

La fase latente usa `w^0=(1/4,1/4,1/4,1/4)`.

Para las fases activas, la función de masa es

\[
\boxed{
\tau(q)
=-\frac{\log\left[2(1/4)^q+(7/30)^q+(4/15)^q\right]}{\log3}.
}
\]

Si `mu_q(j) propto w_j^q`, entonces

\[
\boxed{
\tau''(q)
=-\frac{\operatorname{Var}_{\mu_q}(\log w_j)}{\log3}<0,
}
\]

porque los pesos no son todos iguales. Por tanto el endpoint preregistrado `tau'' != 0` queda satisfecho.

Las dimensiones generalizadas son

\[
D_q=\frac{\tau(q)}{q-1},
\qquad
D_1=-\frac{\sum_j w_j\log w_j}{\log3}.
\]

La fase `0` es un segmento latente de dimensión uno. Las fases `+/-` soportan una medida multifractal sobre la geometría Koch.

**Boundary:** el resultado es exacto para la medida auto-semejante estándar. Proyecciones con solapamientos adicionales requieren auditoría específica.
