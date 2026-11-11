# RGΦ-I · Respuesta adversarial integrada RC2

**Corte:** 11-11-2026. **Estado editorial:** `REVISED_INTERNAL / NOT_SUBMISSION_READY_GENERALIST`.

## Decisiones matemáticas verificadas

1. **Cota excepcional:** en la rama `r=3, m=7, gcd(C,P)=19`, la condición `W>(3P-A)/2`, junto con `C=A+W=19c`, implica `0<2P-W<19c`. Como `2P-W=jc`, necesariamente `1≤j≤18` (no hace falta el superconjunto de 37 casos).
2. **Certificado modular manual:** para `Q(j)=403j²+15314j+190969`, todo `j` impar da `Q(j)≡2 (mod 4)`. Los pares `4,8,14,18` quedan excluidos módulo 5; `2,12,16` módulo 11; `6,10` módulo 17. Los 18 casos fueron rechecados con enteros exactos.
3. **Divisibilidades §5.2:** los 2-ciclos `S` dan `Bu≡-t`, `B(-t)≡u (mod A)` y por tanto `A | u²-t²`. Los 2-ciclos `T` dan `BA≡C`, `BC≡A (mod D)` y por tanto `D | A²-C²=D | A²-s²`.
4. **Divisibilidades §5.3:** `T` en denominador `Q=A+P` da `Q | C²-A²`; `T` en denominador `D=A+rP` da `D | r²A²-C²`; `S` en numerador `C=A+W` da `C | (rP-W)²-(P-W)²`.
5. **Cotas uniformes para m:** se incorporaron las derivadas en `w` y desigualdades factorizadas en ambas fronteras para `r=2,3`; ya no se supone que variar `p` no altere el bound.
6. **Paridad en `m=7`, `gcd(C,P)=1`:** de `2C²+21P²+4AP=19A²` se deduce `A,P` impares módulo 2 y `C` impar módulo 8; esto justifica `gcd(C,4P)=1`.
7. **Identidad exacta del presupuesto:** `R_C=∏_T x_{i+1}/x_i=∏_S x_i/x_{i+1}`, por telescopado de numeradores.
8. **Nuevo teorema general:** a base `B` y cardinalidad máxima `n` fijas, todos los estados cerrados tienen numerador y denominador divisores de `N=B^(n−1) lcm_{k≤n}(B^k−1)`; de aquí un procedimiento de decisión exacta y finita.
9. **Censo derivado:** ejecutado con Python/SymPy, `B=2..17`, `n≤5`: 82.387 estados candidatos examinados en los 16 universos, cuatro SCC cerradas en total, ninguna no permutacional de tamaño ≤5. El script y el JSONL íntegro están en este paquete. Es un censo de ventana declarada, no una cota global sobre la base mínima. No hay réplica independiente de este censo.
10. **Alcance y retórica:** eliminado el subapartado de analogías físicas; corregida la supuesta simetría `T↔S`; la identidad espectral se separa del presupuesto de ciclos, del que no es premisa; añadido contraste técnico con Kůrka, Calta–Kraaikamp–Schmidt, Li–Li–Wu y alturas/resultantes.

## Matriz de cierre frente a los cuatro dictámenes

| Bloque consolidado | Estado RC2 | Evidencia / bloqueo |
|---|---|---|
| M1: congruencias de §5.2 | **Corregido** | Derivación de dos ciclos en ambos idiomas |
| M2: tres divisibilidades de §5.3 | **Corregido** | Expansión por fibras `Q,D,C` |
| M3: cota de `j` | **Corregido** | `j≤18` derivado, no supuesto |
| M4: 37 discriminantes | **Mejorado** | Prueba manual con 4,5,11,17; 37 como regresión |
| M5: estimaciones `m(p,w)` | **Corregido localmente** | Factorizaciones uniformes verificadas simbólicamente |
| M6: paridad caso `m=7` | **Corregido** | Argumento módulo 2/8 |
| M7: aristas paralelas / clausura forzada | **Revisión independiente pendiente** | Los lemas siguen necesitando un segundo auditor de casos |
| M8: caso dual diámetro ≤2 | **Revisión independiente pendiente** | La prueba resumida original requiere explicitación de cada retorno |
| M9: CRT / gcd / `B≥2` | **Parcial** | Se explicitó `B≥2`; falta auditar la redacción de condiciones gcd y casos degenerados |
| M10: simetría `T↔S` | **Corregido** | Eliminada como hipótesis falsa |
| M11: exactitud del presupuesto | **Mejorado** | Nueva identidad de cociclo sobre ciclos |
| M12: base fija / cardinalidad | **Nuevo teorema** | Universo divisor y algoritmo exacto |
| M13: base mínima global | **Abierto** | Sólo censo exacto `B≤17`, `n≤5` |
| M14: tipos realizables `n=5` | **Abierto** | No se declara clasificación inexistente |
| M15: familia para todo `n≥5` | **Abierto** | No se presupone posibilidad de extensión |
| M16: otros conos / conjugaciones | **Abierto** | No se extrapola el umbral |
| M17: cociclo en palabras no periódicas | **Abierto** | No se inventan presión ni exponentes |
| M18: conexiones con alturas/resultantes | **Contextualizado** | Sin reclamar una nueva teoría de alturas |
| M19: comparación con Kůrka | **Mejorada** | Sección técnica y tres referencias próximas |
| M20: Calta–Kraaikamp–Schmidt | **Actualizado** | Publicación de 2024, DOI verificado |
| M21: supervivientes ×B | **Contextualizado** | Inclusión del conjunto cerrado en el superviviente |
| M22: Hecke/Schreier/dessins | **No incorporado como resultado** | Analogías sin teorema de equivalencia; requieren trabajo nuevo |
| M23: curvas elípticas | **Desinflado** | No se identifica una curva sin derivación |
| M24: referencias cruzadas | **Compilación limpia** | Dos pasadas pdflatex, sin referencias indefinidas |
| M25: presentación bilingüe | **Producido** | Artículo y suplemento, EN/ES, TeX/PDF |
| M26: auditoría externa / prioridad | **Pendiente** | Revisión clean-room y búsqueda exhaustiva MathSciNet/zbMATH |
| M27: generalista élite | **No alcanzado** | Falta teorema de impacto externo/clasificación estructural |

## Advertencias científicas necesarias

- **La corrección documental de una demostración no sustituye su arbitraje externo.** La sección de cuatro estados sigue necesitando una auditoría clean-room de los lemas combinatorios y de las conicas, aunque las derivaciones indicadas se han ampliado.
- **La clasificación completa de cinco estados no está demostrada.** Tampoco se conoce aquí la base mínima global ni un teorema de realización universal de semigrupos.
- **La nueva decidibilidad es un resultado matemático sustantivo, pero su algoritmo no tiene cota de complejidad eficiente demostrada.**
- **No existe una calificación objetiva «11/10» ni una garantía de aceptación editorial.** El paquete es una revisión de investigación, no una certificación de envío a Annals/Inventiones.
- **El manuscrito y su suplemento no se han incorporado al repositorio GitHub**, que sólo recibe pruebas, checkers y ledger.

## Próximo gate obligatorio para submission-ready

Revisar de manera independiente todas las bifurcaciones del argumento `TTSS/TSTS` y los lemas de clausura; terminar el análisis aritmético de cinco estados o un teorema general de realizabilidad/obstrucción; obtener un referee técnico externo; refrescar bibliografía y formatos del journal elegido; cerrar metadatos, DOI y anexos. Hasta entonces, estado `MAJOR_REVISION_REQUIRED`.
