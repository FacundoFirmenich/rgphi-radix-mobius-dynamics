# RGΦ–GLOBAL–TRAP–CUT–088 · Stage A

## Corte estructural de primeras divergencias y exclusión global hasta `t = 185`

**Fecha canónica:** 28 de octubre de 2026  
**Estado:** `PASS_WITH_BOUNDARY`  
**Línea:** RGΦ principal, base diez, semilla `17/19`  
**Ramas experimentales:** conservadas en paralelo; no intervienen en este resultado.

---

# 1. Centrum vivo

La línea principal estudia el sistema racional no conmutativo

\[
T(x)=\{10x\},\qquad H(x)=\frac1{1+x},\qquad S=HTH^{-1},
\]

con semilla

\[
x_0=\frac{17}{19}.
\]

Para la profundidad cinco, el objetivo es

\[
P_5=\left\{x\in[0,1):\frac1{1-x}>1\,100\,000\right\}.
\]

El canon al inicio de este gate era

\[
\tau_1=45,\quad \tau_2=85,\quad \tau_3=120,\quad \tau_4=162,
\]

\[
179\le \tau_5\le212,
\]

y

\[
V_5(x_t)=212-t\qquad(89\le t\le212).
\]

El objetivo estratégico no era continuar otra rama padre por padre, sino clasificar conjuntamente las 89 primeras divergencias de la política testigo y compartir sus descendencias.

---

# 2. Pregunta exacta del macro-gate

Toda política que mejore el testigo de 212 acciones posee una primera divergencia respecto de él en algún tiempo

\[
t\in\{0,\ldots,88\}.
\]

Para cada tiempo se toma la acción alternativa a la del testigo. El conjunto de fuentes queda particionado en:

1. acción alternativa inadmisible;
2. entrada inmediata en componente terminal;
3. cuenca finita cerrada sin acceso a `P5`;
4. bulk residual que debe desplegarse temporalmente.

Una exclusión completa hasta un tiempo `N` para la unión de esas fuentes demuestra

\[
\tau_5>N.
\]

---

# 3. Corte estructural exacto de las 89 divergencias

El corte exacto produce:

| Clase | Cantidad |
|---|---:|
| Alternativa inadmisible | **23** |
| Terminal inmediata | **4** |
| Cuenca finita exacta | **3** |
| Bulk residual | **59** |
| **Total** | **89** |

Por tanto, antes de cualquier búsqueda masiva se eliminan estructuralmente

\[
\boxed{30/89}
\]

de las primeras divergencias.

## 3.1 Alternativas inadmisibles

Los tiempos son:

\[
87,86,81,61,60,57,49,44,43,42,37,36,35,34,31,30,24,23,22,18,17,16,13.
\]

No generan una fuente válida.

## 3.2 Entradas terminales inmediatas

| Profundidad | Estado alternativo |
|---:|---:|
| 40 | `7/10` |
| 5 | `4/5` |
| 3 | `2/3` |
| 2 | `1/2` |

## 3.3 Tres cuencas finitas exactas

### Fuente `4/9`, profundidad 7

\[
T_4(4/9)=4/9.
\]

Es un punto fijo, con altura máxima `9/5`; por tanto `V5(4/9)=∞`.

### Fuente `5/16`, profundidad 9

\[
\frac5{16}\xrightarrow{T_3}\frac18
\xrightarrow{T_1}\frac14
\xrightarrow{T_2}\frac12.
\]

La clausura no terminal tiene tres estados y termina en la componente terminal `1/2`.

### Fuente `1/14`, profundidad 4

La clausura no terminal exacta es

\[
\left\{\frac1{14},\frac17,\frac27,\frac37,\frac47,\frac57,\frac67,\frac35\right\}.
\]

Todas sus aristas permanecen en el conjunto o entran en `0`, `1` o `2/3`, ya certificados como terminales. Su altura máxima es 7. Por tanto

\[
V_5(1/14)=∞.
\]

---

# 4. Trap Atlas exacto hasta denominador 10.000

Se enumeró el grafo completo de racionales reducidos no terminales con denominador acotado por `D`, generando toda arista `T/S` admisible y calculando SCC, condensación y clausura relativa al conjunto terminal.

| `D` | Estados | Aristas | SCC | SCC cerradas | SCC seguras | Estados seguros |
|---:|---:|---:|---:|---:|---:|---:|
| 500 | 76.094 | 109.254 | 23.176 | 153 | 1.502 | 1.624 |
| 2.500 | 1.899.856 | 2.735.455 | 565.564 | 248 | 5.483 | 5.933 |
| 5.000 | 7.600.436 | 10.944.352 | 2.255.011 | 314 | 9.672 | 10.418 |
| 10.000 | **30.397.464** | **43.771.910** | **9.009.037** | **467** | **17.094** | **18.472** |

El atlas `D=10.000` confirma que ninguna de las 59 fuentes residuales entra en una trap finita contenida en ese rango. Esto no prueba que jamás alcancen una trap de denominador mayor; sí prueba que el bulk restante no es un artefacto de haber usado un atlas pequeño.

Las 467 SCC cerradas tienen tamaños máximos 12. La distribución completa queda en los artefactos del gate.

---

# 5. Teorema de dominancia por primera llegada

Sea una misma fracción racional `x` alcanzada en tiempos globales

\[
t_1<t_2.
\]

Toda continuación admisible de longitud `L` desde `x` es independiente de la genealogía anterior. Si la llegada tardía alcanza `P5` en `t_2+L`, la llegada temprana ejecuta la misma continuación y alcanza `P5` en `t_1+L<t_2+L`.

Por tanto, para una pregunta de primera llegada antes de un horizonte fijo:

\[
\boxed{\text{la llegada más temprana domina todas las posteriores}.}
\]

Esto autoriza una búsqueda conjunta sobre estados `x`, conservando sólo su menor tiempo global.

---

# 6. Arquitectura exacta de dos etapas

## Stage A — primera llegada, tiempos 1–171

Se inyectaron las 59 fuentes residuales en sus tiempos globales reales. Se mantuvo un conjunto histórico exacto de estados ya vistos y se descartaron únicamente:

- llegadas posteriores dominadas;
- 23 estados terminales;
- 5.933 estados pertenecientes a cuencas finitas exactas del atlas `D=2.500`;
- estados que incumplen la cota rigurosa de viabilidad por denominador.

El resultado en `t=171` fue:

\[
\boxed{94\,848\,409}
\]

estados de primera llegada en la frontera y

\[
\boxed{932\,586\,690}
\]

estados únicos acumulados.

No se encontró ningún hit.

### Cross-check independiente

En `t=120`, dos implementaciones independientes produjeron exactamente:

\[
\boxed{414\,800}
\]

estados en la frontera y

\[
\boxed{4\,141\,395}
\]

estados únicos acumulados.

SHA-256 canónico de la frontera ordenada:

```text
7ff6d942f676d87528de8c495f0bb9354d58ec173096b181a55a9bba721facc6
```

## Stage B — envolvente completa por niveles, tiempos 172–185

A partir de la frontera exacta de primera llegada en `t=171`, se propagó la envolvente completa por niveles.

La suficiencia es exacta: si una trayectoria mínima alcanzara por primera vez el objetivo después de 171, todos sus prefijos serían llegadas mínimas a sus estados. Su estado en `t=171` tendría que pertenecer a la frontera exacta del Stage A. El Stage B contiene todas sus continuaciones.

No se sustraen revisitas históricas en esta fase; el resultado es una sobreenvolvente, nunca una subaproximación.

---

# 7. Resultado temporal exacto

| `t` | Frontera exacta | Hijos brutos | Podas viabilidad | Podas trap | `q_max` | Hits |
|---:|---:|---:|---:|---:|---:|---:|
| 171 | 94.848.409 | — | — | — | 165.797 | 0 |
| 172 | 150.811.478 | 154.362.893 | 0 | 692 | 263.613 | 0 |
| 173 | 231.838.926 | 253.345.126 | 0 | 8.827 | 209.601 | 0 |
| 174 | 328.841.566 | 389.318.236 | 0 | 21.889 | 252.617 | 0 |
| 175 | 440.274.694 | 549.263.657 | 0 | 30.597 | 252.417 | 0 |
| 176 | 566.049.954 | 732.075.535 | 0 | 36.257 | 374.287 | 0 |
| 177 | 706.046.668 | 937.677.048 | 0 | 39.650 | 266.859 | 0 |
| 178 | 860.515.122 | 1.165.963.877 | 0 | 41.632 | 349.129 | 0 |
| 179 | 1.030.084.742 | 1.417.426.056 | 120 | 42.877 | 292.197 | 0 |
| 180 | 1.215.906.806 | 1.693.194.201 | 120 | 43.921 | 435.729 | 0 |
| 181 | 1.419.634.497 | 1.995.221.385 | 3.214 | 44.973 | **482.677** | 0 |
| 182 | 1.643.419.948 | 2.326.277.328 | 2.994 | 45.949 | 368.889 | 0 |
| 183 | 1.889.816.920 | 2.689.950.568 | 16.955 | 46.820 | 386.303 | 0 |
| 184 | 2.161.762.060 | 3.090.449.553 | 15.853 | 47.492 | 450.501 | 0 |
| 185 | **2.462.600.671** | **3.532.552.326** | 74.585 | 48.407 | 482.331 | **0** |

El mayor `q` de toda esta fase es

\[
\boxed{482\,677}
\]

en `t=181`, todavía muy por debajo de `1.100.000`.

---

# 8. Nuevo intervalo canónico

La exclusión conjunta de todas las primeras divergencias hasta `t=185` demuestra:

\[
\boxed{\tau_5\ge186.}
\]

El testigo exacto de 212 acciones permanece vigente. Por tanto:

\[
\boxed{186\le\tau_5\le212.}
\]

El lower bound mejora en siete acciones respecto del canon inicial de este turno:

\[
179\longrightarrow186.
\]

La escalera Bellman exacta ya certificada continúa siendo

\[
V_5(x_t)=212-t\qquad(89\le t\le212).
\]

Este gate todavía no la extiende hacia atrás, porque las 59 fuentes residuales no han sido excluidas hasta el horizonte completo 211.

---

# 9. Checkpoint exacto de la frontera 185

La frontera contiene:

\[
\boxed{2\,462\,600\,671}
\]

estados empaquetados en 128 buckets ordenados y deduplicados, con un tamaño total de

\[
\boxed{19\,700\,805\,368\text{ bytes}}.
\]

El SHA-256 del manifiesto de hashes de los 128 buckets es:

```text
dbd2f4adda52315e05261b9328c03f8a44d2a31b8e293f3dd3ff7b80b3d2a6b7
```

El checkpoint masivo se conserva localmente, pero no se incluye en el ZIP liviano. El bundle contiene su manifiesto completo y los hashes de todos los buckets.

---

# 10. Resultado negativo útil: cono inverso ingenuo

La preimagen intervalar directa de `P5` crece así:

\[
19,\ 329,\ 6\,001,\ 111\,656,\ 2\,090\,493,\ 39\,239\,785,\ldots
\]

La siguiente profundidad excedió la memoria disponible. Esta ruta no fue usada para ninguna prueba.

La conclusión metodológica es que el reverse cone debe incorporar desde el inicio restricciones Farey, 10-ádicas y de presupuesto `2/5`; la unión geométrica desnuda de intervalos no es competitiva.

---

# 11. Demarcación crítica

## Cerrado en este gate

- partición exacta de las 89 primeras divergencias;
- tres cuencas finitas nuevas con valor portal infinito;
- Trap Atlas exacto hasta denominador 10.000;
- teorema de dominancia de primera llegada;
- frontera exacta de primeras llegadas hasta `t=171`;
- envolvente completa por niveles hasta `t=185`;
- exclusión global de hits hasta `t=185`;
- mejora rigurosa del lower bound:
  \[
  \tau_5\ge186.
  \]

## No cerrado

- `NO_HIT` global hasta 211;
- igualdad `τ5=212`;
- clasificación de las 59 fuentes como trap o escape;
- extensión Bellman anterior a `t=89`;
- archivo de los 128 payloads binarios fuera del entorno que los produjo.

El veredicto correcto es:

\[
\boxed{\texttt{PASS\_WITH\_BOUNDARY}.}
\]

---

# 12. Frontera siguiente

El siguiente gate principal es

\[
\boxed{\text{RGΦ–GLOBAL–TRAP–CUT–088 · Stage B2}.}
\]

Debe continuar desde el checkpoint `t=185`, pero el motor simple necesita materializar más de 3.5 mil millones de hijos por nivel y alcanza el límite físico del contenedor.

La solución técnica vinculante es un motor de runs ordenados y comprimidos:

1. generación por bloques de buckets fuente;
2. ordenación y deduplicación local;
3. compresión Zstandard de runs;
4. merge multiway exacto por bucket destino;
5. borrado progresivo de runs;
6. commit transaccional de cada nivel;
7. verifier independiente sobre hashes y conteos.

El objetivo científico sigue siendo binario:

- un hit produce un testigo de menos de 212 acciones;
- `NO_HIT` hasta 211 demuestra
  \[
  \boxed{\tau_5=212}
  \]
  y extiende la escalera Bellman hasta `t=0` mediante la clasificación de todas las primeras divergencias.

---

# 13. Centrum preservado

Nada de este gate depende de U5-HD, HM, GEN ni Artin/Kummer. Esas ramas continúan vivas y aisladas.

El centrum de la línea principal permanece:

\[
\boxed{
\text{geodésicas exactas de escape}
\quad\text{versus}\quad
\text{cuencas modulares finitas de captura}
}
\]

en el semigrupo racional radix–Möbius controlado por Bellman.
