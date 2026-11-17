# Teorema T012‑D — Distribución y aguja media de hiperacceso

Sea \(q=343\). Si \(W_\ell\) es uniforme entre las palabras de longitud \(\ell\), y \(F_\ell\) es el tamaño de su fibra \((H,\ell)\), entonces

\[
\boxed{
\Pr(F_\ell=f)\longrightarrow
p_f=\frac{f(q-1)^2}{q^{f+1}}.
}
\]

La unicidad asintótica vale

\[
\boxed{
p_1=\frac{342^2}{343^2}=0.994177596069664\ldots
}
\]

y la probabilidad de ambigüedad es

\[
\boxed{
\Pr(F\ge2)=\frac{685}{117649}=0.005822403930335\ldots
}
\]

La entropía residual converge a

\[
\boxed{
H_\infty=
\sum_{f\ge2}\frac{f(q-1)^2}{q^{f+1}}\log_2f
=0.005837332402614633262\ldots\text{ bits}.
}
\]

La media de bits de un código binario de longitud fija por fibra converge a

\[
\boxed{0.005847854308123188049\ldots\text{ bits}.}
\]

Condicionado a que exista ambigüedad, el coste entrópico medio es

\[
1.002563970562\ldots\text{ bits},
\]

por lo que las ambigüedades son raras y casi siempre binarias.

Esta constante depende de la distribución uniforme de palabras de longitud fija. No es una constante universal; sí es una realización exacta de una aguja informacional de coste medio muy pequeño y efecto cualitativo decisivo.