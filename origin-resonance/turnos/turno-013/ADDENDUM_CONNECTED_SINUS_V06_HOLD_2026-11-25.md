# Origin–Resonance · T013 · Addendum de integridad conectado (2026-11-25)

**Autoridad:** RESONANCE_ONLY_NO_CANONICAL_OVERRIDE. **Clase:** UPSTREAM_HISTORICAL_HOLD_SOURCE_VERIFIED / GIT_TREE_CHECK / NO_ENDPOINT_PROMOTION. Registro append-only; no sustituye el monitor ni el resultado matemático estrecho T013.

## Procedencia y temporalidad

El corte T013 `2931c05d395e7424ee2a38072e418b5fb0a9ceee` se publicó el 17-XI-2026 a las 18:51:31 UTC. Se recuperó ahora un artefacto posterior de ese mismo día (22:57:47 UTC), preexistente a este control, no una nueva ejecución de CI:
- Repositorio conectado: sinus-math, rama `research/sinus-pi-centrum-v0.6.0-hold-replay-20261117`, commit `38dbab6e8b4ea70129679f8c9fc004b976c66a99`.
- [Auditoría HOLD](https://github.com/FacundoFirmenich/sinus-math/blob/38dbab6e8b4ea70129679f8c9fc004b976c66a99/centrum-local/audits/HOLD_AUDIT_v0.6.0_2026-11-17.md), blob `b1620fa8f2da33d45213fe89820c5c477be74a3b`.
- Base v0.6 `b368a8e365ae2c3d79da975c4755825073990a5d`; v0.5 `4e4ccdb874c1ff31e62dc23713c6c1f29561d124`; RGΦ main `c25857e53eea8585a4f10e0a5a42295a315151ec`. Los tres cortes, y Resonance antes de este addendum, devolvieron identical frente a referencias.

## Evidencia verificada en este control

Se inspeccionaron los dos árboles Git completos (truncated=false) de v0.6 y HOLD. En ambos consta `centrum-local/proofs/LOCAL_THEOREM_v0.6_ES.md` (blob `3efffbae949b4992ec855d024cb38e46a514a73a`), `centrum-local/src/audit_borrow_inverse_v06.py` (blob `7654465b7f1a5d3afe68469c148d660a935dfd94`) y `centrum-local/data/CORRECTIONS_APPEND_ONLY.jsonl` (blob `2cb3b9dacbbea1f2d59e51e001b64fa005003665`, 13 líneas no vacías según lectura). No constan archivos con los nombres `check_local.py`, `build_local.py` ni `SHA256SUMS.txt` en esos árboles. La rama HOLD no corrige esos faltantes. Esto distingue la prueba presente en Git de la prueba ausente en el ZIP según la auditoría.

La auditoría histórica upstream documenta: ZIP v0.6 de 3.682.146 bytes, SHA-256 `c4e9d422f8613c52b186cd7b8ca74a13b8f5b08b6383be22fa8ac4090b0e032d`; 72/72 hashes de manifiesto, pero prueba exigida omitida; 47/48 tests del ZIP intacto, 48/48 solo en copia con prueba restaurada; 185 desigualdades, margen 89/1131900 y reconstrucción local en copia restaurada. Reporta 0/15 blobs byte-idénticos a Biblioteca, 14/15 tras retirar LF final y divergencia del ledger (13 frente a 15 entradas, IDs SINUS-011 y SINUS-012 reutilizados). **Estos resultados de archivo se atribuyen al documento upstream; el ZIP, sus bytes y sus tests no fueron reejecutados ni revalidados en este control.** No se identifica causalmente el fallo CI con la omisión del ZIP.

GitHub Actions: las últimas ejecuciones RGΦ (13-XI) siguen exitosas; los dos runs FST (17-XI, 44140178760 y 44147596941) siguen en failure, sin artefactos. Los metadatos de los dos artefactos históricos RGΦ siguen disponibles (digests registrados; bytes no revalidados). No hay nueva release ni incidencia actualizada desde 24-XI UTC en los repositorios consultados.

## Adjudicación y límites

- Añadir HOLD de integridad/replay integral a la interpretación de la afirmación upstream 48/48: no es certificado del ZIP original ni CI PASS. El PASS_T013_CONNECTED_SINUS_V06_INDEPENDENT_NARROW histórico permanece acotado; no se refuta por el negativo editorial. No se promueve G0/G1/G2, no se establece sincronización byte a byte. No se altera ni se reejecuta el checker T013.
- SUPERACCESS = reconstrucción de información interna, subsistémica o histórica oculta; HYPERACCESS = llave residual de completitud zero-error. El no-go de cinco marcas parciales conserva su dominio de fases arbitrarias.
- Nota02: derivación de 00583733 desde 168 mantisas negativa en directa, una operación, dos operaciones, órbita directa de 343 y sufijo FST-14. N=π/q_obs=18; Φ1(18)=17, Φ2(18)=19, Φ3(18)=343=7³=(111)₁₈; 343=9·36+19=10·36−17; 343²≡1 mod 36. H∞=E(343)=0.005837332402614633262... es identidad exacta FST-13; UMI abierta/post hoc, no causal. Búsqueda bibliográfica pública acotada no aportó recurrencia prospectiva independiente admisible; no se modifica el preregistro ni se cuenta la auditoría HOLD como componente RC28.
- FST-14 inversión terminal y frontera del subgrupo 10-ádico, entropía residual dependiente de fuente, composición FST×D3, límites analíticos de frontera natural y codificación residual universal conservan sus obligaciones y jurisdicciones T013/T014. No se cierra ninguna obligación ni se cambia ningún endpoint.

**Decisión:** MATERIAL_RESONANCE_PROVENANCE_UPDATE / NO_NEW_MATH_ENDPOINT_EVIDENCE / NO_FALSIFICATION. Este archivo es la única actualización autorizada. Preservar monitor T013 y todas las correcciones/negativos. En futuros controles, reconocer este addendum y la fuente HOLD fijada como evidencia ya registrada, no notificarla nuevamente si no cambian.