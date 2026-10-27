# RGΦ — Auditoría de literatura, prioridad y novedad v1.0

**Fecha de corte:** 27 de octubre de 2026  
**Cobertura:** corpus canónico sin restricción temporal + frontera 2024–2026  
**Estado:** auditoría abierta completada; verificación cerrada en MathSciNet/zbMATH/Scopus pendiente de acceso institucional  
**Objeto:** determinar qué partes de RGΦ son antecedentes conocidos, cuáles son recombinaciones legítimas y cuáles constituyen claims de novedad defendibles.

---

## 0. Dictamen ejecutivo

La auditoría modifica el encuadre, pero no desactiva el programa.

Los ingredientes individuales de RGΦ tienen literaturas maduras:

- transformaciones radix y beta-expansions: Rényi–Parry y desarrollos posteriores;
- mapas de Farey/Gauss, natural extensions y codificación geodésica: Nakada, Series y una línea extensa;
- semigrupos de transformaciones Möbius y matrices racionales;
- dinámica y codificación p-ádica mediante cilindros y shifts;
- programación dinámica, estado suficiente y recompensas no markovianas;
- sistemas abiertos, survivor sets y escape;
- ortoposets, OMPs, effect algebras y bloques booleanos;
- proof certificates y computación reproducible;
- problemas de Artin/Kummer y densidades de raíces primitivas.

Por ello RGΦ **no puede reclamar prioridad sobre ninguno de esos ingredientes aisladamente**.

La contribución potencialmente original reside en el acoplamiento exacto de:

\[
\boxed{
\text{radix}
+\text{conjugación Möbius}
+\text{sombras Farey}
+\text{fase }p\text{-ádica}
+\text{objetivos Bellman no anidados}
+\text{traps modulares certificados}
}
\]

sobre un mismo semigrupo racional, con resultados exactos y computación certificada.

El barrido abierto no localizó un antecedente que contenga simultáneamente:

1. una filtración de objetivos extremales racionales con tiempos exactos;
2. una demostración de que los primeros hits no forman una cadena óptima;
3. una coordenada Farey/10-ádica oculta que cambia el control desde el mismo racional visible;
4. una ley prime-wise de transporte del defecto;
5. traps finitos modularmente clasificables que implican valor Bellman infinito;
6. certificados exhaustivos de reachability/no-reachability a la escala usada por RGΦ.

La ausencia de un match en una revisión abierta **no equivale a prueba de prioridad**. El claim de prioridad deberá permanecer como:

> “To the best of our knowledge, after the systematic search protocol reported in the supplement…”

hasta completar bases bibliográficas cerradas, búsqueda por citas y revisión externa.

---

# 1. Protocolo de búsqueda

## 1.1. Capas temporales

### Corpus canónico

Sin restricción temporal. Incluye resultados fundacionales y monografías en:

- beta-expansions;
- continued fractions;
- Farey/Gauss maps;
- Möbius and matrix semigroups;
- arithmetic and p-adic dynamics;
- dynamic programming;
- open systems;
- quantum logics/effect algebras;
- Artin-type density problems;
- proof certificates and reproducibility.

### Frontera reciente

Ventana prioritaria:

\[
\boxed{1\text{ enero }2024\;\text{--}\;27\text{ octubre }2026.}
\]

Se añadieron trabajos previos cuando son antecedente directo.

## 1.2. Fuentes consultadas en esta fase

- arXiv;
- páginas DOI y de editoriales accesibles;
- índices y buscadores académicos abiertos;
- referencias backward/forward identificables desde los trabajos hallados;
- corpus interno RGΦ y sus claims canónicos.

## 1.3. Segunda pasada todavía obligatoria

- MathSciNet;
- zbMATH Open con búsqueda por MSC y citas;
- Scopus/Web of Science para citation chaining;
- Google Scholar con variantes lexicales;
- búsqueda de tesis doctorales y proceedings;
- consulta directa a especialistas en continued fractions, arithmetic dynamics y effect algebras.

## 1.4. Familias de query

Se congelan en `RGPHI_SYSTEMATIC_SEARCH_PROTOCOL_v1.md`. Las principales son:

- `beta transformation rational periodic orbit Möbius conjugacy`;
- `Farey map hidden state p-adic coding rational dynamics`;
- `non nested hitting times Bellman arithmetic dynamics`;
- `finite rational trap forward invariant continued fraction map`;
- `orthomodular poset p-adic budget effect algebra`;
- `proof certificate exact reachability rational dynamical system`;
- `Artin primitive root simultaneous maximal order density`.

---

# 2. Mapa del corpus canónico

## 2.1. Transformaciones radix y beta-expansions

Rényi y Parry constituyen la base inevitable. La literatura posterior estudia admisibilidad, periodicidad, bases algebraicas, natural extensions y representaciones de racionales.

### Implicación para RGΦ

No es defendible presentar

\[
T_B(x)=\{Bx\}
\]

como una construcción novedosa. Sí es defendible estudiar el semigrupo concreto generado por `T_B` y su conjugado Möbius, con reducción primitiva, objetivos portal y estado Farey oculto.

### Riesgo de prioridad

**Alto para el ingrediente; bajo–medio para el acoplamiento.**

## 2.2. Continued fractions, Farey maps y natural extensions

Series y Nakada son referencias rectoras. La frontera reciente incluye clasificación de mapas de Farey, first-return systems, estadísticas de órbitas racionales finitas y natural extensions multidimensionales.

### Implicación

Las expresiones “Farey map”, “geodesic coding”, “natural extension”, “synchronization” y “first return” deben usarse en arreglo estricto a esta literatura. Las sombras RGΦ no deben presentarse como primera aparición de coordenadas Farey auxiliares; la novedad a demostrar es su papel como estado suficiente para el control Bellman del semigrupo concreto.

### Riesgo

**Alto.** El trabajo de Panti de 2025 hace especialmente peligrosa cualquier clasificación amplia de mapas de Farey sin comparación explícita.

## 2.3. Semigrupos Möbius y dinámica aritmética

Las acciones de matrices fraccionales lineales y la dinámica aritmética poseen corpus propio. La contribución RGΦ no es que existan matrices de rama ni que no conmuten, sino que su reducción aritmética alimenta una ley de defecto, un ledger prime-wise y objetivos extremales no anidados.

### Riesgo

**Alto para formulaciones generales; medio para los teoremas RGΦ específicos.**

## 2.4. Dinámica p-ádica, cilindros y transductores

La conjugación con shifts p-ádicos, los automata congruenciales y los cilindros son antecedentes directos. El trabajo de Pérez-Buendía de 2026 hace particularmente importante no reclamar como novedoso el concepto general de intérprete racional p-ádico o de cylinder partition.

### Novedad defendible

La fórmula exacta que acopla:

- racional visible;
- vecino Farey;
- defecto `h`;
- factores de reducción `g,k`;
- objetivo Bellman;
- trap/escape;

no fue localizada como paquete previo.

## 2.5. Bellman, estado suficiente y no-Markovianidad

La necesidad de ampliar el estado para recuperar optimalidad es un principio conocido. También se conocen compilaciones de recompensas no markovianas en modelos markovianos aumentados.

### Novedad RGΦ

No debe formularse como “descubrimiento de que Bellman necesita estado suficiente”. Debe formularse como:

> construcción aritmética exacta en la que la variable visible y la profundidad del objetivo son insuficientes, acompañada por coordenadas mínimas candidatas y contraejemplos cuantificados.

## 2.6. Sistemas abiertos, survivor sets y traps

Los sistemas con agujeros, survivor sets, escape rates y conjuntos invariantes son una literatura madura. RGΦ aporta un ángulo discreto-racional exacto:

- traps finitos;
- explicación por órdenes multiplicativos;
- enlaces mediante el segundo generador;
- valor Bellman infinito;
- certificados exhaustivos.

### Riesgo

**Medio.** El término “trap” es genérico; el teorema debe ser la clasificación modular específica.

## 2.7. Ortoposets, orthomodularity y effect algebras

La terminología es técnicamente exigente. Los cuadrados prime-wise de RGΦ son bloques booleanos locales. No está demostrado aún que su pasting global sea un orthomodular poset o lattice.

### Decisión terminológica inmediata

Hasta completar los axiomas, usar:

\[
\boxed{
\text{orthocomplemented contextual }2/5\text{-adic semantics}
}
\]

como denominación principal.

“Orthomodular” puede conservarse como **programa de formalización** o como propiedad condicional, no como teorema global cerrado.

## 2.8. Artin/Kummer

Es la línea con mayor riesgo de prioridad. Las densidades de órdenes, index maps y constantes de Artin tienen una literatura extensa y técnicamente profunda.

### Decisión

La línea RGΦ debe:

1. formularse como especialización Artin-type;
2. identificar con exactitud el grupo/subgrupo y la condición local;
3. derivar la constante desde campos de división/Kummer;
4. separar resultados incondicionales, bajo GRH y puramente computacionales.

No debe presentarse la constante empírica como paradigma nuevo antes de esa reducción.

## 2.9. Computación certificada y reproducibilidad

Hashes, motores independientes y aritmética exacta son excelentes, pero los proof certificates y los estándares FAIR/RO-Crate son anteriores.

### Acción

RGΦ debe elevar sus logs a certificados consumibles por un checker mínimo y empaquetar cada ejecución mediante Workflow Run RO-Crate.

---

# 3. Frontera 2024–2026 que cambia el posicionamiento

La frontera reciente más relevante incluye:

- clasificación de projective Farey IFS en 2025;
- first-return systems para continued fractions en 2025;
- estadísticas multidimensionales de órbitas racionales finitas en 2025;
- open systems con agujeros radix móviles en 2025;
- natural extension de `(-β)` en 2026;
- intérpretes racionales p-ádicos y CRT dinámico en 2026;
- continued fractions de Romik y Farey graphs complejos en 2026;
- desarrollos categóricos recientes de orthomodular posets;
- formalización Lean de Möbius transformations en 2026;
- resultados uniformes recientes en Artin/Hooley.

Estas referencias no refutan RGΦ, pero elevan la exigencia:

1. generalizar base y semillas;
2. distinguir claramente mapas, natural extensions y codificaciones;
3. convertir “shadow” en objeto definido universalmente;
4. formalizar traps como theorem family;
5. evitar claims amplios de p-adic interpreter u orthomodularity sin prueba.

---

# 4. Prioridad claim por claim

La tabla completa está en `RGPHI_CLAIM_TO_LITERATURE_MAP_v1.csv`.

## 4.1. Claims con riesgo bajo o controlable

### Nonnested portal filtration

No se localizó un antecedente directo de la misma construcción aritmética exacta con primeros hits que dejan de ser precursores óptimos al aumentar el objetivo.

**Prioridad provisional:** alta.

### Exact hidden Farey phase controlling Bellman actions

Existen coordenadas Farey, natural extensions y codificaciones p-ádicas. No se localizó el mismo mecanismo exacto en el que una cifra de la fase cambia la acción desde el mismo racional y modifica el hitting time portal.

**Prioridad provisional:** alta para el acoplamiento, no para los ingredientes.

### Finite mixed modular traps with infinite portal value

Los closed classes y survivor sets son conocidos. No se localizó una clasificación idéntica de traps racionales mixtos `T/S` explicados por órdenes multiplicativos y usados para probar valor Bellman infinito.

**Prioridad provisional:** media–alta, pendiente del Trap Atlas y búsqueda específica.

## 4.2. Claims con riesgo medio

- cone–bulk–reset;
- 10-adic compiler;
- antichain compression;
- exact first-divergence certificates;
- destructive portal renewal.

Todos requieren comparación con natural extensions, transducers, automata y open-system inducing.

## 4.3. Claims con riesgo alto

- “nuevo Farey map”;
- “nueva orthomodular logic”;
- “nuevo p-adic interpreter”;
- “nueva constante tipo Artin”;
- “primer vínculo entre beta-transformations y continued fractions”.

Esas formulaciones no son aceptables.

---

# 5. Frontera de novedad recomendada

La frase rectora para abstracts es:

> We study a noncommutative rational semigroup obtained by coupling an integer-base expansion map with a Möbius-conjugate branch map. The novelty lies not in the individual ingredients, but in the exact interaction between primitive reduction, Farey-neighbor coordinates, hidden p-adic phase, nonnested extremal hitting objectives, and finite modular traps.

En español:

> Estudiamos un semigrupo racional no conmutativo que acopla una transformación de expansión en base entera con una rama Möbius-conjugada. La novedad no reside en los ingredientes aislados, sino en su interacción exacta con reducción primitiva, coordenadas vecinas de Farey, fase p-ádica oculta, objetivos extremales no anidados y traps modulares finitos.

---

# 6. Claims expresamente prohibidos

No usar en papers, abstracts, talks ni notas de prensa:

1. “descubrimos una correlación entre las cifras de φ y 1/17”;
2. “inventamos una nueva beta-transformation”;
3. “introducimos por primera vez sombras de Farey”;
4. “la dinámica es cuántica porque es ortomodular”;
5. “probamos la conjetura de Artin”;
6. “τ5=212” mientras el intervalo siga abierto;
7. “la fase 10-ádica es única en general” sin especificar contexto;
8. “clasificamos todos los traps” antes del atlas completo;
9. “el sistema visible no es Markoviano” sin aclarar la elección del estado y del objetivo;
10. “top-tier breakthrough” como autoevaluación editorial.

---

# 7. Estado de cobertura y limitaciones

## Cubierto en esta versión

- 55 referencias rectoras;
- nueve clusters bibliográficos;
- corpus clásico y frontera 2024–2026;
- mapa claim→antecedente→riesgo→acción;
- bibliografía BibTeX reproducible;
- queries y criterios de screening.

## Pendiente antes de submission

1. MathSciNet y zbMATH por MSC;
2. forward citation search de 15 referencias núcleo;
3. búsqueda por similitud de fórmulas/matrices;
4. revisión de tesis y literatura no inglesa;
5. consulta a tres especialistas externos;
6. declaración explícita de la fecha final de search;
7. actualización living-review antes de cada envío.

---

# 8. Revisión del scoring tras la auditoría

La literatura reduce la novedad atribuible a ingredientes aislados, pero mejora la definición del claim y aumenta la generalidad al activar la formulación base-`B`.

| Dimensión | Antes | Después de esta fase | Justificación |
|---|---:|---:|---|
| Originalidad conceptual | 8,8 | 8,4 | Prior art amplio en ingredientes; acoplamiento aún distintivo |
| Rigor simbólico | 9,0 | 9,2 | Teoremas base-B y ledger general formulados |
| Rigor computacional | 9,5 | 9,5 | Sin cambio |
| Generalidad | 6,4 | 7,5 | Base B, familias de semillas y umbral paramétrico |
| Posicionamiento bibliográfico | 4,5 | 7,6 | Auditoría abierta sustantiva; faltan bases cerradas |
| Madurez editorial | 7,3 | 8,0 | Arquitectura de papers y claim hygiene más precisas |
| Validación externa | 3,2 | 3,5 | Protocolo definido, todavía no ejecutado por terceros |
| Score compuesto | 7,8 | **8,2** | Mejora real, no cosmética |

**Techo tras Trap Atlas, formalización y réplica externa:** `9,1–9,3/10`.

---

# 9. Decisión de prioridad

## Puede reivindicarse provisionalmente

- exact nonnested extremal portals in this rational Möbius semigroup;
- explicit Farey/p-adic hidden control of portal hitting paths;
- exact mixed modular trap certificates and their Bellman consequences;
- the coupled theorem package connecting these layers.

## No puede reivindicarse

- novelty of radix maps, Farey maps, p-adic cylinders, Möbius semigroups, Bellman augmentation, orthomodular structures, effect algebras, Artin densities or proof certificates individually.

---

# 10. Dictamen

La principal vulnerabilidad de RGΦ ya no es “falta de bibliografía”, sino la necesidad de convertir esta auditoría en **delimitación matemática verificable** dentro de los manuscripts.

El programa es publicable si su novedad se presenta como:

\[
\boxed{
\text{un nuevo teorema de acoplamiento y sus consecuencias exactas},
}
\]

no como una suma de ingredientes pretendidamente inéditos.
