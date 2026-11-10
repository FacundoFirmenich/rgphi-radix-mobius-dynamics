# RGΦ Five-State Closure 014 — gate revisado e integrado

## 1. Estado inicial

La rigidez all-high queda probada para cardinalidades 2, 3 y 4. Cualquier contraejemplo mínimo tiene al menos cinco estados.

Por el cycle reduction budget, un candidato mínimo de cinco estados debe:

- ocurrir sobre una base divisible por 2 o 3;
- contener una única reducción estricta de factor 2 o 3 en el ciclo elegido;
- tener las demás aristas del ciclo unreduced;
- contener un ciclo simple de longitud 4 o 5.

## 2. Jurisdicciones obligatorias

### A. Extensión por un vértice de un core de cuatro

Core word:

- `TTSS`, o
- `TSTS`.

El quinto estado no define una sola arquitectura. Hay que enumerar todos los pares de endomorfismos T,S sobre cinco vértices que:

1. contienen el core marcado;
2. son cerrados;
3. son fuertemente conexos;
4. respetan la orientación high y las leyes de reducción;
5. son mínimos: ningún subconjunto propio es ya el contraejemplo;
6. se quotientan por isomorfía que preserve las etiquetas T/S, rotación del core y dualidad T<->S.

La salida de esta fase debe ser una lista canónica exhaustiva de closure extensions, no sólo los nombres TTSS/TSTS.

### B. Ciclo Hamiltoniano de cinco estados

Up to cyclic rotation and T/S exchange, los dos necklace words con multiplicidad 2/3 son:

\[
TTSSS,\qquad TSTSS.
\]

Para cada word deben tratarse:

- strict-T y strict-S;
- factor 2 y factor 3;
- todas las asignaciones de aristas alternativas compatibles con clausura;
- identificaciones o colapsos que reduzcan la cardinalidad.

## 3. Ruta simbólica

Para cada clase canónica:

1. derivar una normal form por fibras de numerador y denominador;
2. imponer el cycle reduction budget;
3. convertir alternate closure edges en congruencias/divisibilidades;
4. usar intervalos high para acotar representantes;
5. eliminar por desigualdad, divisibilidad, conics o certificados modulares;
6. si sobrevive, construir una familia exacta y verificar toda su clausura.

## 4. Ruta global paralela

Construir una formulación por stationary flow/cycle cover del presupuesto de reducción. El objetivo es demostrar que todo counterexample mínimo contiene un minor de cuatro estados ya prohibido, o identificar la obstrucción que impide esa reducción.

## 5. Reglas de promoción

`PASS_FIVE_STATE_RIGIDITY` sólo si:

- la enumeración combinatoria está certificada como exhaustiva;
- cada clase se elimina simbólicamente o se realiza exactamente;
- los certificados finitos poseen checker independiente;
- no se usa un scan acotado como prueba global.

Hasta entonces:

`GLOBAL_ALL_HIGH_RIGIDITY = OPEN`.
