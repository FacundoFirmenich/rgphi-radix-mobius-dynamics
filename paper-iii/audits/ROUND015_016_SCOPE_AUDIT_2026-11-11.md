# RGΦ Paper III — auditoría de jurisdicción Round 015/016 (11-XI-2026)

## Resultado de la comprobación

Se recuperó el bundle Round 015 y se ejecutó su trusted checker en el entorno local. Salida: PASS; 560 clases de entrada, 540 etiquetadas como eliminadas, 20 formas de incidencia/defecto uno. Esta prueba informática comprueba la contabilidad y las invariantes programadas; no constituye demostración de exhaustividad lógica respecto de todas las SCC all-high de cinco estados.

## Distinción crítica

El presupuesto de reducción Round 012 garantiza que, **sobre un ciclo testigo elegido**, el producto de reducciones es 2 o 3 y las restantes aristas **de ese ciclo** son unreduced. No demuestra que exista **una única arista estricta en todo el grafo de diez aristas funcionales** de una SCC de cinco estados.

El teorema lollipop Round 015 presupone expresamente que una sola arista global es estricta y que todas las demás aristas de ambos generadores son unreduced. Bajo esa hipótesis la conclusión de fuente transitoria, permutación en el complemento y otro generador permutacional es válida.

Por tanto, la reducción 560 → 20 no es promovible como eliminación exhaustiva de los posibles contraejemplos globales hasta que se demuestre que todas las clases excluidas incumplen una condición **necesaria** válida sin la hipótesis de unicidad, o hasta que se demuestre un lema de unicidad global de la reducción estricta.

## Reconciliación documental

El repositorio tenía una tabla histórica de 24 clases y 12 formas, mientras que el bundle efectivamente comprobado Round 015 declara 20 formas. Round 016 ya reconoció el reemplazo de la jurisdicción 24/12 por la de 20. Los resultados Round 016 (7 formas cerradas, 13 abiertas y 15 ramas aritméticas) son resultados **dentro de la jurisdicción condicionada**; no prueban rigidez global n=5.

## Política de claims

- Rigidez all-high n=2,3,4: sin cambios.
- Defect-one lollipop 015: teorema exacto **condicional a unicidad global**.
- Clasificación 560 → 20: auditoría condicionada, globalmente PENDING.
- Siete cierres Round 016: condicionales al dominio de 20 formas y sujetos a revisión matemática independiente.
- Rigidez all-high n=5 y general: OPEN.
- No modificar Paper I, Paper II ni otros proyectos.

## Siguiente gate correcto

(1) Probar o refutar la unicidad global de arista estricta en una SCC all-high mínima de n=5. (2) Reprocesar las 560 arquitecturas permitiendo múltiples aristas estrictas fuera del ciclo testigo y aplicando las leyes exactas de gcd a cada una. (3) Sólo entonces establecer un quotient diofántico globalmente exhaustivo.
