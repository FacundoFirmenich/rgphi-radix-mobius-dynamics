# RGΦ — Arquitectura editorial y scoring v2.0

## 0. Decisión editorial

La auditoría recomienda **tres papers principales**, un companion computacional y una línea Artin/Kummer separada.

No conviene publicar seis fragmentos débiles. Conviene concentrar los claims en unidades teóricas autocontenidas.

---

# Paper I — Nonnested extremal targets in a rational Möbius semigroup

## Tesis

En un semigrupo racional no conmutativo generado por una transformación radix y una rama Möbius-conjugada, los primeros hits de objetivos extremales pueden dejar de ser precursores óptimos de objetivos más profundos.

## Contenido

- definición base-B;
- semigrupo y ramas;
- objetivos `P_m(B,κ)`;
- `τ1–τ4` para el caso benchmark;
- contraejemplos exactos de nonnesting;
- insuficiencia de altura y profundidad;
- augmented state;
- threshold robustness;
- protocolo computacional.

## Claims que no necesita

- optimalidad global de `τ5`;
- formalización ortomodular completa;
- Artin/Kummer;
- Trap Atlas completo.

## Score actual

| Dimensión | /10 |
|---|---:|
| Novedad después de prior art | 8,7 |
| Rigor | 9,3 |
| Generalidad tras base-B | 8,0 |
| Madurez | 8,8 |
| Riesgo de referee | 2,5 |
| Score global | **8,7** |

## Destinos

1. Journal of Modern Dynamics.
2. Experimental Mathematics.
3. Nonlinearity, si threshold robustness y theorem general quedan fuertes.

---

# Paper II — Farey shadows and hidden p-adic control

## Tesis

El estado racional visible no determina por sí solo el control extremal. Una coordenada Farey/p-adic exacta puede seleccionar acciones distintas desde el mismo racional y cambiar hitting times globales.

## Contenido

- vecinos Farey y defecto;
- ley `Δ'=BΔ/(gk)`;
- coordenadas canónicas `(h,t)`;
- ledger prime-wise;
- compiladores 212/217;
- flip de una cifra;
- cone–bulk–reset;
- suficiencia del estado aumentado;
- relación con p-adic shifts/interpreters.

## Bloqueo actual

Debe formularse como theorem family en base B y comparar exhaustivamente con natural extensions y p-adic coding.

## Score

| Dimensión | /10 |
|---|---:|
| Novedad conceptual | 9,0 |
| Rigor | 8,7 |
| Generalidad | 7,5 |
| Madurez | 8,0 |
| Riesgo de prioridad | 4,5 |
| Score global | **8,3** |

## Destinos

1. Journal of Modern Dynamics.
2. Journal of Number Theory.
3. Ergodic Theory and Dynamical Systems tras teorema general y natural extension.

---

# Paper III — Finite modular traps and exact portal escape

## Tesis

Los valores Bellman infinitos del semigrupo pueden certificarse mediante traps racionales finitos cuya estructura combina ciclos radix modulares y enlaces Möbius.

## Contenido

- criterio general de trap;
- `C8`;
- Trap Atlas;
- closed SCCs y cierres forward-invariant;
- órdenes multiplicativos;
- basins;
- cotas de altura;
- interacción con global first-divergence cut;
- familias infinitas si se obtienen.

## Resultado nuevo de esta fase

Atlas exacto `D≤500`:

- 76.094 estados;
- 153 SCCs cerradas módulo terminales;
- 1.502 cierres finitos exactos de tamaño ≤100;
- recuperación exacta de `C8`.

## Score

| Estado | /10 |
|---|---:|
| Con C8 solamente | 7,0 |
| Con atlas D500 | 8,0 |
| Con familia/criterio de clasificación | **9,1** |

## Destinos

1. Journal of Modern Dynamics.
2. Nonlinearity.
3. Ergodic Theory and Dynamical Systems, si hay teorema de familia.

---

# Companion — Certified computation for rational semigroup dynamics

## Tesis

Una arquitectura exacta de reachability/no-reachability, con poda demostrada, hashes, proof certificates y engines independientes, permite resolver hitting-time statements de gran escala en grafos racionales.

## Contenido

- aritmética packed-rational;
- external hash/sort;
- viability bounds;
- first-divergence union;
- certificate formats;
- trusted checker;
- benchmarks;
- reproducibilidad RO-Crate.

## Score

\[
\boxed{8,2/10}
\]

Potencial `9/10` si el engine y sus cotas se generalizan y un equipo externo replica los resultados.

## Destinos

- Experimental Mathematics;
- Journal of Computational Dynamics;
- Mathematics of Computation, sólo con theorem algorítmico/complexity y validación externa.

---

# Paper ortocomplementario / effect algebra

## Estado

No submission-ready.

## Score

\[
\boxed{5,8/10\text{ actual};\quad8,7/10\text{ potencial}.}
\]

## Gate

Probar OMP/effect algebra o abandonar terminología ortomodular fuerte.

---

# Artin/Kummer paper

## Separación obligatoria

No mezclar con los papers dinámicos salvo una motivación breve.

## Score

- computacional/conjectural: `7,2/10`;
- con reducción analítica Artin-type y densidad demostrada bajo GRH: `8,8–9,1/10`.

## Destinos

- Experimental Mathematics;
- Research in Number Theory;
- Journal of Number Theory;
- Acta Arithmetica tras teorema.

---

# Scoring global actualizado

| Dimensión | /100 |
|---|---:|
| Originalidad del acoplamiento | 84 |
| Rigor simbólico | 92 |
| Rigor computacional | 95 |
| Generalidad | 75 |
| Literatura/posicionamiento | 76 |
| Madurez editorial | 80 |
| Reproducibilidad interna | 91 |
| Validación externa | 35 |
| Control de overclaiming | 92 |
| Potencial | 93 |

## Score compuesto actual

\[
\boxed{82/100.}
\]

## Nivel

- programa especializado: `A−`;
- paquete editorial inmediato: `A−/B+`;
- techo tras atlas, formalización y réplica: `A/A+` especializado;
- no comparable todavía con Annals/Inventiones/JAMS.

---

# Orden recomendado

1. Paper I.
2. Paper III tras ampliar Trap Atlas.
3. Paper II.
4. Companion computacional.
5. Artin/Kummer.
6. Formalización contextual sólo cuando el objeto algebraico esté probado.

---

# Política de títulos

## Permitidos

- rational Möbius semigroup;
- nonnested extremal hitting times;
- hidden Farey/p-adic control;
- finite modular traps;
- certified rational dynamics.

## No permitidos

- golden-ratio correlation;
- quantum dynamics;
- universal Farey map;
- proof of Artin;
- orthomodular lattice, salvo teorema.
