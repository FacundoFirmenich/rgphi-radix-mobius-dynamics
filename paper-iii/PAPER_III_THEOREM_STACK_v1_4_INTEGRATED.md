# Paper III theorem stack v1.4 — canon integrado

## A. Resultados estructurales cerrados

1. Clasificación completa de SCC binarias.
2. Clasificación completa de SCC ternarias.
3. Clasificación de SCC all-low para cardinalidad arbitraria mediante necklaces primitivas.
4. Clasificación con exactamente un estado high para cardinalidad arbitraria.
5. Cálculo exacto de predecesores universales.
6. Cuencas forzadas, Bellman infinito y skeleton Cantor.
7. Profundidad high arbitraria al variar la base.
8. Finitud del sector high para cada base fija mediante reducción a S-units.
9. Bounds fixed-base explícitos, aunque no sharp.
10. Rigidez all-high cuando el diámetro dirigido es <=2.
11. Cycle reduction budget y criterio por menor primo de la base.
12. Rigidez all-high completa para cardinalidades 2, 3 y 4.

## B. Nuevo teorema integrado: cardinalidad cuatro

Toda SCC cerrada all-high de cuatro estados satisface

\[
T_B|_F,\ S_B|_F\in\operatorname{Sym}(F).
\]

La prueba usa:

- reducción de todo candidato no permutacional a `TTSS` o `TSTS`;
- no-go de escala para `TTSS`;
- contradicción `A>5u` frente a `A<4u` para `TSTS` strict-T;
- eliminación diofántica y certificado modular para `TSTS` strict-S.

## C. Estado global honesto

\[
\boxed{
\text{rigidez all-high probada para }|F|\le4,
\text{ abierta para }|F|\ge5.
}
\]

Además, para cardinalidad arbitraria la rigidez está probada cuando:

- uno de los generadores es transitivo sobre F;
- el diámetro dirigido es <=2;
- el criterio del menor primo de la base satisface el cycle budget.

## D. Frontera mínima

Todo contraejemplo mínimo no permutacional debe cumplir:

- |F|>=5;
- 2|B o 3|B;
- una arista estricta sobre ciclo simple de longitud 4 o 5;
- producto de reducción 2 o 3;
- todas las otras aristas del ciclo unreduced.

## E. Evidencia y autoridad

| Resultado | Autoridad |
|---|---|
| cycle reduction budget | SYMBOLIC EXACT |
| diameter <=2 rigidity | SYMBOLIC EXACT |
| four-state TTSS no-go | SYMBOLIC EXACT |
| four-state TSTS strict-T | SYMBOLIC EXACT |
| four-state TSTS strict-S | SYMBOLIC + FINITE MODULAR CERTIFICATE |
| global all-high rigidity | OPEN |
| five-state classification | OPEN / NEXT GATE |

## F. Producto editorial

El archivo `PAPER_III_v1_3.pdf` recibido es sólo una página. La siguiente versión editorial debe compilar un manuscrito real con:

1. cycle budget;
2. cardinality obstruction;
3. full four-state theorem;
4. certificate appendix;
5. five-state frontier;
6. explicit evidence boundary.
