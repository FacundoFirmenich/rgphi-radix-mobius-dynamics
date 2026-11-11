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

## Hallazgos mayores resueltos

1. Relabelings incompatibles de la contrafamilia: normalizados.
2. Hipótesis implícita de unicidad global del strict edge en cuatro estados: cerrada por un nuevo lema simbólico.
3. Reducción a `TTSS/TSTS`: incorporada como lema explícito.
4. Patrones alternativos forzados: demostraciones expandidas.
5. Bounds de cocientes diofánticos: explicitados.
6. Argumentos gcd/paridad: añadidos.
7. Dominio parcial y endpoint: corregidos.
8. `Phi` descrita erróneamente como involución: corregido.
9. MSC primaria incorrecta: corregida.
10. Prior art Möbius/`×b`: incorporado y novelty boundary acotado.
11. Toy checker de finite type: eliminado.
12. Build BibTeX y dependencia falsa del diagrama: corregidos.

## Auditoría matemática

- objeto y leyes locales: PASS;
- cociclo y espectro: PASS;
- cycle budget: PASS;
- rigidez en cuatro estados: PASS;
- certificado de 37 discriminantes: PASS;
- contrafamilia CRT y sharp threshold: PASS;
- finite types y fibra CRT: PASS.

## Auditoría computacional

```text
canonical_labeling=PASS
nonsquare_certificate_rows=37
counterfamily_bases_checked=1001
Python exact replay=PASS
C++ exact replay=PASS
spectral certificate=PASS
```

## Auditoría PDF/build

- artículo: 16 páginas;
- suplemento: 4 páginas;
- openable: sí;
- encrypted: no;
- scanned: no;
- undefined references: 0;
- overfull boxes: 0;
- BibTeX warnings: 0;
- extracción textual clean-room idéntica: PASS.

## Gates externos vinculantes

1. Confirmación autoral de afiliación, current address, ORCID y email.
2. Revisión escrita de Daniel Barraco.
3. Revisión independiente en arithmetic dynamics/number theory.
4. Reproducción clean-room por una persona y entorno independientes.
5. Priority chaining final en MathSciNet/zbMATH.
6. Sólo después: release inmutable y envío.

## Conclusión

```text
INTERNAL MATHEMATICAL AUDIT: PASS
PRE-SUBMISSION RC1: GO_WITH_EXTERNAL_GATES
EXTERNAL VALIDATION: PENDING
SUBMISSION: NOT YET
```
