# Teorema T013‑D — Frontera natural y observadores analíticos

Para una etiqueta admisible \(h\):

\[
B_h(z)=\sum_{j\ge0}z^{\ell_{h,j}},
\qquad
F_h(z)=\frac{B_h(z)}{1-z}.
\]

FST‑12 demuestra que \(|z|=1\) es frontera natural de ambas series.

## Observadores \(D\)-finitos

Ningún procedimiento que represente exactamente el espectro global mediante una función \(D\)-finita puede producir \(B_h\) o \(F_h\): una función \(D\)-finita sólo tiene finitas singularidades en el plano finito, mientras aquí cada punto del círculo unidad bloquea la continuación.

Por inclusión, tampoco existen representaciones globales exactas racionales, algebraicas ni por recurrencia lineal fija.

## Aproximación local

Sea

\[
B_{h,N}(z)=\sum_{\ell_{h,j}\le N}z^{\ell_{h,j}}.
\]

Para \(|z|\le r<1\):

\[
\boxed{|B_h(z)-B_{h,N}(z)|\le\frac{r^{N+1}}{1-r}.}
\]

Y

\[
\boxed{|F_h(z)-B_{h,N}(z)/(1-z)|\le\frac{r^{N+1}}{(1-r)^2}.}
\]

Toda región compacta interior admite aproximación exponencialmente precisa.

## Consultas locales

Cada coeficiente \([z^n]B_h\) puede decidirse aritméticamente. Coexisten consulta local exacta e imposibilidad de una síntesis analítica global dentro de la clase declarada.

## Boundary

La frontera natural es una imposibilidad de representación para observadores analíticos específicos; no una frontera ontológica, física o computacional absoluta.
