# RGΦ Paper III — estado canónico v1.12 (2026-11-11)

Objeto exclusivo: trampas modulares, SCC racionales, cuencas universales y estructura all-high. Paper I, Paper II, Stage B2 y otras líneas no se modifican.

## Resultado central

- Rigidez all-high probada para cardinalidades 2, 3 y 4.
- Cardinalidad 5 admite una contrafamilia infinita exacta no permutacional; el umbral mínimo de ruptura es 5 y la rigidez global está refutada.
- La ruptura de cinco estados posee una única arista estricta global y un catálogo combinatorio exhaustivo de veinte formas.
- Para cualquier tupla primitiva fija, la realización en bases es una dicotomía CRT exacta.
- `DF015-0015` se reduce a diecinueve curvas elípticas; \(F_{17}\) tiene rango positivo e infinitos puntos racionales en la cámara.
- En las curvas de índice impar, la divisibilidad cúbica equivale exactamente a \(A\) impar; si \(A\) es par, el defecto es cuatro.
- La coprimalidad \(\gcd(2A-z,2A-w)=1\) equivale a evitar el punto universal \(R=[1:2:2]\) en toda reducción. Por Siegel, cada curva tiene sólo finitos candidatos coprimos relativos-integrales.
- El punto exacto \(44P\) sobre \(F_{17}\) está en la cámara, tiene defecto cuatro y colisión frontera en el primo 83.
- Las formas densas quedan reducidas a asignaciones casi coprimas de divisores.
- La tupla Round 017 no admite ninguna extensión de seis estados por subdivisión de una sola arista: 66 perfiles exhaustivos, diez supervivientes estructurales y 3.206 tests CRT sin hit.

## Estado abierto

- Clasificación aritmética de las veinte formas: OPEN.
- Enumeración efectiva de los puntos relativos-integrales: OPEN.
- Unicidad global de la tupla Round 017: OPEN.
- Clasificación completa en cardinalidad seis: OPEN.

## Canon Round 021

- [Odd-index parity collapse](theorems/ODD_INDEX_PARITY_COLLAPSE_021.md)
- [Boundary point and relative-integral finiteness](theorems/BOUNDARY_POINT_S_INTEGRAL_FINITE_021.md)
- [Dense-form splitting](theorems/FOUR_FIBRE_NEAR_COPRIME_SPLITTING_021.md)
- [Countergraph divisor allocation](theorems/COUNTERGRAPH_DIVISOR_ALLOCATION_021.md)
- [One-edge-subdivision catalogue](theorems/N6_ONE_EDGE_SUBDIVISION_021.md)
- [Theorem stack v1.12](PAPER_III_THEOREM_STACK_v1_12.md)
- [Round 021](round-021/)
- [Gate 022](gates/RGPHI_EFFECTIVE_RELATIVE_INTEGRAL_022.md)

## Controles de autoridad

- `RELATIVE_INTEGRAL_CANDIDATES_FINITE = CLOSED_USING_SIEGEL`;
- `EFFECTIVE_RELATIVE_INTEGRAL_LIST = OPEN`;
- `ROUND017_STATE_TUPLE_GLOBAL_UNIQUENESS = OPEN`;
- `N6_ONE_EDGE_SUBDIVISION_EXTENSION = CLOSED_NEGATIVE_FOR_FIXED_TUPLE`;
- `N6_GLOBAL_CLASSIFICATION = OPEN`.
