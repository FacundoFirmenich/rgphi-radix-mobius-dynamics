# RGΦ — Protocolo de reproducibilidad, certificación y réplica externa v1.0

## 1. Principio

Un paper computacional no queda reproducido por adjuntar código. Deben preservarse:

- código;
- entorno;
- entradas;
- ejecución;
- outputs;
- provenance;
- claims;
- verificador.

---

## 2. Estructura del repositorio

```text
rgphi/
  README.md
  LICENSES/
  CITATION.cff
  codemeta.json
  pyproject.toml / CMakeLists.txt
  lockfiles/
  container/
  src/
    exact_core/
    engines/
    certificate_writer/
    trusted_checker/
  proofs/
  experiments/
    tau1_tau4/
    witness212/
    traps/
    base_b/
  data/
    inputs/
    expected/
  ro-crate-metadata.json
  claims/claims.json
  scripts/build
  scripts/run
  scripts/verify
  tests/
```

---

## 3. Identidad persistente

Cada release debe tener:

- tag Git firmado;
- commit SHA;
- DOI Zenodo;
- SWHID;
- digest OCI;
- SHA-256 de cada artefacto;
- versión del claim registry.

---

## 4. Entorno

- imagen OCI apineada por digest;
- compilador y flags registrados;
- lockfiles de dependencias;
- SBOM CycloneDX o SPDX;
- arquitectura y endianness;
- límites de memoria/disco;
- número de threads;
- determinismo declarado.

---

## 5. Provenance

Cada run debe producir Workflow Run RO-Crate con:

- input hashes;
- command line;
- environment digest;
- source commit;
- start/end timestamps;
- hardware metadata;
- outputs y hashes;
- claim IDs afectados;
- exit status;
- logs completos.

---

## 6. Proof certificates

### Reachability

- palabra de control;
- replay exacto;
- estado final;
- target predicate.

### Non-reachability finita

- capas o commitments Merkle por capa;
- reglas de transición;
- terminal set;
- certificados de poda;
- total de estados/hijos;
- root hash final.

### Trap

- lista finita de estados;
- tabla completa de hijos;
- clasificación inside/terminal;
- prueba de disjunción con target.

### Bellman

- padre;
- acciones;
- valores de sucesores;
- inferencia mínima.

---

## 7. Trusted checker

El checker debe ser sustancialmente menor que el engine y no compartir su lógica de optimización.

Requisitos:

- aritmética entera exacta;
- sin red;
- sin dependencias científicas grandes;
- verificación streaming;
- mensajes de error localizados;
- test vectors adversariales.

---

## 8. Clean-room replication

### Información entregada

- definición matemática;
- claim registry;
- protocolo;
- formatos de certificate;
- casos pequeños de entrenamiento.

### Información retenida

- implementación del engine;
- estructuras internas;
- resultados de checkpoints holdout.

### Casos holdout

1. uno de `τ1–τ4`;
2. un no-hit gate medio;
3. un no-hit gate grande;
4. un trap no publicado en el texto principal;
5. una base `B≠10`;
6. una semilla paramétrica.

---

## 9. Criterios de réplica

- igualdad exacta de estados finales;
- igualdad de cardinalidades por capa;
- igualdad de hashes preregistrados;
- reproducción de todos los claims cerrados seleccionados;
- explicación pública de cualquier discrepancia.

---

## 10. Publicación de la réplica

Opciones:

- ReScience C;
- companion technical report;
- reproducibility appendix firmado por equipo externo;
- artifact evaluation de la conferencia/revista si existe.

---

## 11. FAIR4RS

El software debe ser:

- Findable: DOI, SWHID, metadata;
- Accessible: repositorio y archive;
- Interoperable: formatos abiertos, RO-Crate, JSON/CSV;
- Reusable: licencia, documentación, tests, ejemplos.

---

## 12. Gate de publicación

Ningún manuscript que dependa centralmente de un cálculo masivo se marca `submission-ready` hasta que:

1. el run esté empaquetado;
2. el checker pase;
3. exista una ejecución limpia;
4. al menos un subconjunto haya sido replicado externamente.
