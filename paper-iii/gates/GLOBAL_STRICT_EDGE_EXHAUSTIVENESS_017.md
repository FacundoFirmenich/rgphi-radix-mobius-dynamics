# Global Strict-Edge Exhaustiveness 017 — gate vinculante Paper III

**Estado:** OPEN.

El presupuesto de reducción obliga a una arista estricta en un ciclo simple high y acota las demás aristas *de ese ciclo*. No establece por sí mismo unicidad global de arista estricta en el par de mapas T/S de la SCC.

## Test decisivo

1. Probar un lema de unicidad de arista estricta en un contraejemplo all-high mínimo de cinco estados, usando clausura completa y el presupuesto en todos los ciclos.
2. Si falla, enumerar asignaciones de reducciones para las aristas externas al ciclo testigo; imponer gcd por fuente y leyes exactas de imagen.
3. En cada clase, demostrar incongruencia o construir una familia exacta, sin cutoffs de denominador como sustitutos de prueba.
4. Aplicar luego la rama lollipop/20 formas sólo a las clases donde la unicidad global haya quedado establecida.

**Boundary:** Five-state and global rigidity OPEN.
