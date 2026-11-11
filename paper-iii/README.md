# RGΦ Paper III — estado canónico revisado

Objeto exclusivo: trampas modulares, SCC racionales, cuencas universales y rigidez all-high de Paper III. No modificar la autoridad de Paper I, II, Stage B2 u otras ramas.

## Teorema central actualizado

La rigidez all-high está probada para cardinalidades 2, 3 y 4. Round 017 construye una familia infinita exacta de SCC all-high cerradas de cardinalidad 5 con `S_B` no permutacional. Por tanto:

\[
\boxed{|F|\le4\Rightarrow T_B|_F,S_B|_F\text{ son permutaciones},}
\]

mientras que cardinalidad 5 ya admite fallo exacto. La cardinalidad mínima de fallo es **cinco** y la conjetura global de rigidez permutacional all-high queda **refutada**.

## Contrafamilia exacta

\[
B_t=88\,011\,536\,665\,779+t\,223\,336\,848\,698\,040,
\qquad t\ge0,
\]
con estados

\[
406/731,\quad712/731,\quad712/1265,\quad1218/1265,\quad406/557.
\]

La tabla de acciones, el certificado CRT y dos checkers independientes están en [`round-017/`](round-017/). La familia realiza la rama condicionada `DF015-0007-B2`, pero el contraejemplo y el teorema de umbral son independientes de que el quotient Round 015/016 sea globalmente exhaustivo.

## Boundary Round 015/016

Round 014 proporciona 560 clases de arquitecturas combinatorias bajo restricciones necesarias de un ciclo testigo. El bundle Round 015 comprobado produce 20 formas bajo una hipótesis adicional: **exactamente una arista estricta en todo el grafo**. El presupuesto Round 012 establece unicidad sólo en el ciclo testigo, no en las restantes aristas de la SCC.

El checker de Round 015 dio PASS contable, pero no convierte esa restricción adicional en un teorema global. Los cierres Round 016 siguen siendo resultados condicionados a esa jurisdicción. Esta cautela permanece vigente para la **clasificación completa**, aunque ya no afecta al contraejemplo exacto de Round 017.

Ver [auditoría de jurisdicción](audits/ROUND015_016_SCOPE_AUDIT_2026-11-11.md), [Round 016](round-016/) y [Round 017](round-017/).

## Fronteras abiertas

1. Clasificación completa de las SCC all-high no permutacionales de cinco estados, incluyendo arquitecturas con múltiples aristas estrictas fuera del ciclo testigo.
2. Adjudicación de las ramas condicionadas restantes.
3. Resolución global de `DF015-0015`; Round 017 sólo cierra un subcaso y una jurisdicción finita `z<=5000`.
4. Extensión de existencia a cardinalidades mayores o identificación de nuevas obstrucciones.

El gate vinculante es [`gates/RGPHI_FIVE_STATE_CLASSIFICATION_018.md`](gates/RGPHI_FIVE_STATE_CLASSIFICATION_018.md).

## Política de claims

- rigidez all-high para 2,3,4: `CLOSED`;
- contrafamilia de cardinalidad 5: `CLOSED_SYMBOLIC_PLUS_CRT`;
- cardinalidad mínima de fallo = 5: `CLOSED`;
- rigidez all-high global: `REFUTED`;
- clasificación completa de cardinalidad 5: `OPEN`;
- quotient defect-one Round 015/016: `CONDITIONAL_SCOPE`.
