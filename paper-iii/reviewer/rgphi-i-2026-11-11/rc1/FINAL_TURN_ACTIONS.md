# Lista cerrada para el último turno

El último turno no debe añadir teoremas, ejemplos, generalizaciones ni ramas físicas.

## Acciones permitidas

1. Incorporar correcciones concretas surgidas de la lectura RC1.
2. Confirmar o corregir afiliación, dirección, ORCID y email.
3. Resolver observaciones externas clasificadas `FATAL/MAJOR/MINOR`.
4. Ejecutar clean-room externo.
5. Ejecutar el priority chain final y corregir sólo framing/citas.
6. Recompilar, correr `make verify`, preflight y render.
7. Generar RC2/final candidate, hashes y tag inmutable.

## Criterio de salida

```text
FATAL=0
MAJOR=0
CHECKERS=PASS
CLEAN_ROOM_EXTERNAL=PASS
PRIORITY_CHAIN=PASS
AUTHOR_METADATA=CONFIRMED
DECISION=RELEASE_CANDIDATE_FINAL
```

Si aparece una objeción matemática mayor, el último turno se dedica exclusivamente a esa reparación y el release se difiere.
