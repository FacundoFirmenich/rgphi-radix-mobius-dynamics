# Teorema T013‑E — Órbitas de prefijos para lenguajes libres de contexto

Fijemos una palabra canónica \(c=C(K)\) y definamos

\[
T_{K,L}=\{t\ge0:8^tc\in L\}.
\]

## Teorema

Si \(L\) es libre de contexto, entonces \(T_{K,L}\) es finalmente periódico.

## Demostración

1. El cociente derecho \(L/\{c\}=\{x:xc\in L\}\) es libre de contexto.
2. Su intersección con el regular \(8^*\) sigue siendo libre de contexto.
3. Bajo el homomorfismo \(8\mapsto a\), se obtiene un lenguaje unario libre de contexto.
4. Todo lenguaje unario libre de contexto es regular por semilinealidad de Parikh.

Por tanto, el conjunto de índices es una cola finita más progresiones aritméticas.

## Longitud fija

Para cualquier lenguaje con pertenencia de coste \(T_L(\ell)\), la fibra condicionada se obtiene en

\[
O\!\left(A_h(\ell)[T_{\rm dec}(\ell)+T_L(\ell)]\right).
\]

La llave mínima sigue siendo

\[
\left\lceil\log_2|\mathcal F_{h,\ell}\cap L|\right\rceil.
\]

## Frontera

La periodicidad no se extiende a todos los lenguajes decidibles. Para

\[
L_\square=\{8^{n^2}c:n\ge0\},
\]

se tiene \(T_{K,L_\square}=\{n^2:n\ge0\}\), que no es finalmente periódico porque sus gaps \(2n+1\) son no acotados. Este lenguaje es decidible en espacio logarítmico y, por tanto, pertenece al dominio context-sensitive.
