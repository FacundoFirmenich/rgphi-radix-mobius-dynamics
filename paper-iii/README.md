# RGΦ Paper III — estado canónico revisado

Objeto exclusivo: trampas modulares, SCC racionales, cuencas universales y rigidez all-high de Paper III. No modificar la autoridad de Paper I, II, Stage B2 u otras ramas.

**Teoremas all-high sin modificación:** rigidez en cardinalidades 2, 3 y 4. **n=5 y rigidez global: OPEN.**

## Frontera de cinco estados

Round 014 proporciona 560 clases de arquitecturas combinatorias bajo restricciones necesarias de un ciclo testigo. El bundle Round 015 comprobado produce 20 formas bajo una hipótesis adicional: **exactamente una arista estricta en todo el grafo**. El presupuesto Round 012 establece unicidad sólo en el ciclo testigo, no en las restantes aristas de la SCC.

El checker de Round 015 dio PASS (560 entradas, 540 descartes contables, 20 formas), pero dicho PASS no convierte la restricción adicional en teorema global. Round 016 tiene 7 cierres y 13 formas abiertas, todos dentro del subconjunto condicionado. No promover `FIVE_STATE_RIGIDITY`.

La tabla histórica de 24 clases / 12 formas está supersedida para este gate por el bundle de 20 formas, sin borrar los archivos históricos.

Ver [auditoría de jurisdicción](audits/ROUND015_016_SCOPE_AUDIT_2026-11-11.md), [fuentes Round 015](round-015/), [Round 016](round-016/) y [estado computable](CURRENT_STATE.json).

## Siguiente objetivo

Resolver la exhaustividad global de aristas estrictas en cinco estados, o ampliar el quotient para permitir varias aristas estrictas fuera del ciclo testigo. Los tests numéricos siguen siendo evidencia subsidiaria, nunca pruebas globales.
