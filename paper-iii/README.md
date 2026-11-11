# RGΦ Paper III — estado canónico v1.9 (2026-11-11)

Objeto exclusivo: trampas modulares, SCC racionales, cuencas universales y rigidez all-high. Paper I, Paper II, Stage B2 y otras líneas no se modifican.

## Resultado principal

- Rigidez all-high probada para cardinalidades 2, 3 y 4.
- Round 017: contrafamilia infinita exacta de cardinalidad cinco; umbral mínimo de ruptura = **5**; rigidez permutacional global **REFUTADA**.
- Round 018: unicidad global de la arista estricta para una SCC all-high no permutacional de cinco estados, bajo certificado combinatorio y racional exacto (teorema asistido por ordenador).
- El quotient defect-one/lollipop de Round 015 ya tiene resuelta para n=5 su hipótesis adicional de unicidad; conservar la auditoría histórica sin borrarla.
- Clasificación CRT completa de las bases para cada tupla primitiva que realice el grafo conocido; **no** se prueba unicidad global de la tupla.
- La rama excepcional de DF015-0015 está cerrada; su sector general continúa **OPEN_REDUCED**.

## Canon de Round 018

- [Teorema de unicidad strict-edge](theorems/FIVE_STATE_STRICT_EDGE_UNIQUENESS_018.md)
- [Clasificación CRT del grafo realizado](theorems/COUNTERGRAPH_CRT_CLASSIFICATION_018.md)
- [Reducción de divisores DF015-0015](theorems/DF015_0015_DIVISOR_REDUCTION_018.md)
- [Theorem stack v1.9](PAPER_III_THEOREM_STACK_v1_9.md)
- [Certificados y verificación Round 018](round-018/)
- [Gate 019](gates/RGPHI_FIVE_STATE_CLASSIFICATION_019.md)

## Controles de autoridad

- `FIVE_STATE_GLOBAL_STRICT_EDGE_UNIQUENESS = CLOSED_COMPUTER_ASSISTED_EXACT`;
- `GLOBAL_ALL_HIGH_PERMUTATION_RIGIDITY = REFUTED`;
- `COMPLETE_FIVE_STATE_CLASSIFICATION = OPEN`;
- `DF015_0015_NONEXCEPTIONAL = OPEN_REDUCED`;
- `EXISTENCE_FOR_EVERY_N_GE5 = OPEN`.

La prueba asistida por ordenador depende de la exhaustividad del generador de perfiles y de los certificados correspondientes. El bundle fuente íntegro Round 018 sigue identificado por SHA-256 en `round-018/README.md`, incluidos los componentes de auditoría no duplicados en este mirror de trabajo.
