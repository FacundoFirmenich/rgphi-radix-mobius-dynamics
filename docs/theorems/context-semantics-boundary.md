# RGΦ — Decisión de formalización ortomodular v1.0

## Dictamen

La estructura local prime-wise es rigurosamente un bloque booleano de cuatro modos. La estructura global RGΦ todavía **no está demostrada** como orthomodular poset ni orthomodular lattice.

Por tanto:

\[
\boxed{
\text{“orthomodular” pasa de claim cerrado a programa formal.}
}
\]

La denominación inmediata recomendada es:

> **orthocomplemented contextual 2/5-adic budget semantics**.

---

## 1. Bloque local

Para cada primo `p∈{2,5}`:

\[
(s_p,\kappa_p)\in\{0,1\}^2.
\]

El complemento es:

\[
(s_p,\kappa_p)^\perp=(1-s_p,1-\kappa_p).
\]

Este conjunto es un álgebra booleana de cuatro elementos.

Para los dos primos, el producto local tiene 16 modos.

---

## 2. Lo que falta globalmente

Debe definirse una colección de proposiciones/eventos con:

- orden parcial;
- cero y uno;
- involución ortocomplementaria;
- noción de ortogonalidad;
- joins de elementos ortogonales;
- compatibilidad o commuting;
- bloques booleanos;
- ley ortomodular.

No basta con que cada bloque local sea booleano.

---

## 3. Tres destinos posibles

### Opción A — Orthomodular poset

Se demuestra que:

- cada par ortogonal tiene join;
- la involución invierte el orden;
- se cumple la ley ortomodular en el sentido poset.

### Opción B — Effect algebra / orthoalgebra

Si las operaciones son parciales y el pegado no produce todos los joins requeridos, ésta es probablemente la formalización correcta.

### Opción C — Contextual presheaf / pasted Boolean blocks

Si el valor principal está en la familia de contextos compatibles y sus intersecciones, puede ser más natural evitar el claim OMP.

---

## 4. Plan de prueba

1. Definir un universo finito de eventos a profundidad `H`.
2. Construir bloques por elecciones prime-wise compatibles.
3. Definir pasting por estados racionales compartidos.
4. Verificar computacionalmente axiomas para `H≤40`.
5. Buscar contraejemplos mínimos.
6. Formular la estructura abstracta que generaliza el patrón finito.
7. Formalizar en Lean.

---

## 5. Criterio editorial

### Permitido ahora

- orthocomplemented modes;
- Boolean prime-wise blocks;
- contextual incompatibility;
- antichain preservation;
- effect-algebra candidate.

### No permitido todavía

- “RGΦ forms an orthomodular lattice”;
- “quantum logic of the dynamics”;
- claims físicos derivados de la terminología.

---

## 6. Criterio PASS

El término “orthomodular” vuelve al título de un paper sólo si existe:

- definición abstracta;
- teorema de axiomas;
- ejemplo no trivial;
- contraejemplo que muestre por qué distributividad falla;
- comparación explícita con OMP/effect-algebra literature;
- formalización machine-checked o al menos checker finito independiente.
