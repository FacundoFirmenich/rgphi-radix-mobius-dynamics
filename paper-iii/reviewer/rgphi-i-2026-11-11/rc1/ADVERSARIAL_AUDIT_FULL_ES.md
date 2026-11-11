# RGΦ I · Auditoría adversarial pre-submission y dictamen RC1

## Dictamen

```text
FATAL ENCONTRADOS: 0
MAJOR ENCONTRADOS: 12
MAJOR RESUELTOS EN RC1: 12
MAJOR ABIERTOS: 0
MINOR INTERNOS ABIERTOS: 0
GATES EXTERNOS ABIERTOS: 4
CLAIMS MATEMÁTICOS ABIERTOS DENTRO DEL SCOPE DEL PAPER: 0
DECISIÓN: GO_WITH_EXTERNAL_GATES
```

La decisión no significa “submit now”. Significa que el contenido interno puede congelarse y pasar a revisión externa sin añadir ciencia nueva.

## 1. Hallazgos mayores y resolución

| ID | Hallazgo | Riesgo | Resolución RC1 | Estado |
|---|---|---|---|---|
| M01 | Dos relabelings distintos de la contrafamilia entre artículo y certificados | Reproducibilidad literal fallida | Convención única `T=[1,0,3,2,4]`, `S=[4,2,1,0,0]`, `S3:x3->x0`; checker cruzado | RESUELTO |
| M02 | El proof de cuatro estados usaba alternates unreduced sin demostrar unicidad global del strict edge | Laguna lógica | Nuevo Lemma 5.2, demostración simbólica mediante ciclos cortos y conteo `3/1` | RESUELTO |
| M03 | Reducción inicial a `TTSS/TSTS` afirmada, no demostrada en el manuscrito | Dependencia opaca | Nuevo Lemma 5.1 con cycle budget completo | RESUELTO |
| M04 | Forced alternate patterns demasiado comprimidos | Riesgo de circularidad | Pruebas expandidas para strict `T` y strict `S` | RESUELTO |
| M05 | Bounds de los cocientes `m` omitidos | Paso diofántico no auditable | Fórmulas normalizadas y bounds abiertos explícitos | RESUELTO |
| M06 | Justificaciones gcd/paridad omitidas en las cónicas | Riesgo local de validez | Argumentos añadidos | RESUELTO |
| M07 | Dominio presentado como total; endpoint `1/2` problemático | Objeto mal definido | Sistema ambiente parcial; componente finita como subsistema invariante completo; dominio estricto | RESUELTO |
| M08 | `Phi` llamada involución | Afirmación falsa | Reemplazada por cambio de coordenada proyectivo | RESUELTO |
| M09 | MSC primaria `37P25` incorrecta | Indexación editorial errónea | Primaria `37E05`; secundarias `11A07,11A55,11A63,37B10,20M20` | RESUELTO |
| M10 | Prior art Möbius/`×b` insuficiente | Riesgo de prioridad/framing | Kůrka 2009, Kůrka–Kazda 2010, Li–Li–Wu 2023 añadidos y claim acotado | RESUELTO |
| M11 | Checker de finite-type era un toy check | Evidencia computacional inflada | Eliminado; theorem authority únicamente simbólica | RESUELTO |
| M12 | Orden de compilación BibTeX incorrecto y diagrama con dependencia falsa | Build y lógica editorial | `make pdf`; arrow eliminada | RESUELTO |

## 2. Auditoría matemática

### 2.1 Objeto y leyes locales

- branch formulae: PASS;
- reducción exacta de denominador/numerador: PASS;
- formulación proyectiva primitiva: PASS;
- conjugación matricial: PASS;
- distinción entre sistema parcial y subcomponente completo: PASS.

### 2.2 Cociclo y espectro

- orden de composición matricial: PASS;
- identidad telescópica: PASS;
- divisibilidad del producto de defectos: PASS;
- determinante `B^m`: PASS;
- trace/discriminant identity: PASS.

### 2.3 Cycle budget

- multiplicación de ratios de numeradores: PASS;
- argumento dual en denominadores: PASS;
- desigualdad estricta por `rho_C<2`: PASS;
- least-prime/cardinality consequence: PASS;
- directed-diameter consequence: PASS.

### 2.4 Rigidez en cuatro estados

- reducción a ciclo Hamiltoniano `2T/2S`: PASS;
- factor estricto `2` o `3`: PASS;
- unicidad global de strict edge: PASS;
- `TTSS`: PASS;
- `TSTS` strict `T`: PASS;
- `TSTS` strict `S`, factor `2`: PASS;
- factor `3`, branch `m=6`: PASS;
- factor `3`, branch `m=7`: PASS;
- certificado de 37 discriminantes: PASS.

### 2.5 Contrafamilia y sharp threshold

- estados primitivos, distintos y high: PASS;
- seis congruencias CRT: PASS;
- diez acciones exactas: PASS;
- único factor strict `3`: PASS;
- clausura: PASS;
- fuerte conexidad: PASS;
- no inyectividad de `S`: PASS;
- infinitud por CRT: PASS;
- minimalidad `5` por combinación con rigidez `<=4`: PASS.

### 2.6 Finite types y fibra CRT

- finitud combinatoria de endomapas: PASS;
- bound finito sobre defectos: PASS;
- formulación aritmética de realización: PASS;
- exactitud de gcd en el theorem CRT: PASS;
- salida vacía o una clase aritmética: PASS.

## 3. Auditoría computacional

```text
canonical_labeling=PASS
nonsquare_certificate_rows=37
counterfamily_bases_checked=1001
Python exact replay=PASS
C++ exact replay=PASS
spectral certificate=PASS
```

El replay de 1.001 bases no se usa como prueba de infinitud. El checker ya no afirma por sí mismo la minimalidad cardinal.

## 4. Auditoría de exposición

- theorem package explícito en la introducción: PASS;
- scope negativo concentrado y no repetitivo: PASS;
- física presentada como interfaz, no claim: PASS;
- dependencia lógica de la figura: PASS;
- bookmarks y títulos matemáticos: PASS;
- referencias y bibliografía: PASS, sujeto a closed-database review externo.

## 5. Auditoría PDF/build

- artículo: 16 páginas;
- suplemento: 4 páginas;
- openable: sí;
- encrypted: no;
- scanned: no;
- undefined references: 0;
- overfull boxes: 0;
- BibTeX warnings: 0;
- extracción textual clean-room idéntica: PASS.

## 6. Gates externos todavía vinculantes

1. Confirmación autoral de afiliación, current address, ORCID y email.
2. Revisión escrita de Daniel Barraco.
3. Revisión independiente en arithmetic dynamics/number theory.
4. Reproducción clean-room por una persona y entorno independientes.
5. Priority chaining final en MathSciNet/zbMATH.
6. Sólo después: release inmutable y envío.

Los primeros cuatro son los únicos asuntos legítimos para el último turno. Ninguno requiere abrir resultados nuevos.

## 7. Conclusión

RC1 ya no presenta deuda interna conocida dentro del scope declarado. La formulación correcta es:

```text
INTERNAL MATHEMATICAL AUDIT: PASS
PRE-SUBMISSION RC1: GO_WITH_EXTERNAL_GATES
EXTERNAL VALIDATION: PENDING
SUBMISSION: NOT YET
```
