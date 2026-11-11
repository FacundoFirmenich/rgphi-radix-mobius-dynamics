# RGΦ Paper III — estado canónico v1.11 (2026-11-11)

Objeto exclusivo: trampas modulares, SCC racionales, cuencas universales y estructura all-high. Paper I, Paper II, Stage B2 y otras líneas no se modifican.

## Resultado central

- Rigidez all-high probada para cardinalidades 2, 3 y 4.
- Cardinalidad 5 admite una contrafamilia infinita exacta no permutacional; el umbral mínimo de ruptura es 5 y la rigidez global está refutada.
- La ruptura de cinco estados posee una única arista estricta global y un catálogo combinatorio exhaustivo de veinte formas.
- Para cualquier tupla primitiva fija, la realización en bases es una dicotomía CRT exacta.
- `DF015-0015` se reduce a diecinueve curvas elípticas; Round 020 prueba coprime completion sobre esas curvas.
- La curva F_17 tiene torsión racional trivial, rango al menos uno e infinitos puntos racionales en la cámara A>5z>w>0.
- El punto [64233:11741:1138] satisface la cúbica y A|z^3+w^3, pero no realiza RGΦ porque gcd(2A-z,2A-w)=23.

## Estado aritmético

- Clasificación combinatoria de cinco estados: CLOSED.
- Clasificación aritmética de las veinte formas: OPEN.
- Unicidad global de la tupla Round 017: OPEN.
- DF015-0015: OPEN_COPRIME_INTEGRAL_ELLIPTIC.
- Existencia para todas las cardinalidades n>=6: OPEN.

## Canon Round 020

- [Coprime-completion theorem](theorems/DF015_0015_COPRIME_COMPLETION_020.md)
- [Positive-rank chamber theorem](theorems/DF015_0015_N17_POSITIVE_RANK_CHAMBER_020.md)
- [Theorem stack v1.11](PAPER_III_THEOREM_STACK_v1_11.md)
- [Round 020](round-020/)
- [Gate 021](gates/RGPHI_COPRIME_INTEGRAL_POINTS_021.md)

## Controles de autoridad

- `FIVE_STATE_ARITHMETIC_REALIZABILITY_CLASSIFICATION = OPEN`;
- `ROUND017_STATE_TUPLE_GLOBAL_UNIQUENESS = OPEN`;
- `DF015_0015_REAL_CHAMBER_NONEMPTY_AND_POSITIVE_RANK = CLOSED`;
- `DF015_0015_RGPHI_REALIZATION = OPEN`;
- `N6_NONEXISTENCE = NOT_CLAIMED`.
