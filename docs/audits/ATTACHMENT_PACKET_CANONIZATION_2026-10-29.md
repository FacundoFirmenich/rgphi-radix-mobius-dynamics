# Canonización del paquete adjunto RGΦ — 29 de octubre de 2026

## 1. Alcance

Se auditaron conjuntamente:

- Paper I v1.1: TeX, suplemento, claim-evidence matrix y cover letter;
- prompt de sesión fresca;
- handoff operativo de Stage B2;
- manifiesto SHA-256 de los 128 buckets del checkpoint `t=185`;
- documento de cierre operativo en DOCX;
- supercierre canónico/handoff ZIP;
- bundle integral `MULTIFRONT-005`.

La auditoría compara el paquete con la rama canónica pública `main`, cuyo punto de partida fue el commit firmado
`91dbf2c707856c3597ff5bdd9e1ffdda9ae5e2b3`.

## 2. Dictamen de autoridad

El paquete adjunto no constituye un tercer canon. Contiene tres estratos:

1. **freeze editorial Paper I v1.1**;
2. **handoff operativo y supercierre histórico** asociado principalmente al commit `725c1ae4...`;
3. **rama multifrente posterior** con ODT-009, BQ-010A y HM-010.

La autoridad final permanece:

1. `main` del repositorio público;
2. Paper I como `PUBLICATION_TRACK` subordinado al canon;
3. Stage B2 como gate mainline abierto;
4. MULTIFRONT/U5-HD/HM/BQ/ODT como `EXPERIMENTAL_ISOLATED`.

## 3. Aportes genuinos integrados

### 3.1 Suplemento Paper I

El suplemento adjunto aporta una nota de estado no dependiente sobre

`186 <= tau5 <= 212`

y la ausencia del checkpoint de 19.7 GB en el paquete ligero. Se integró como `S9`, corrigiendo además el carácter espurio `e` que precedía al terminal set.

### 3.2 Cover letter

Se integraron:

- enlace explícito al repositorio público;
- separación clara entre Paper I y Stage B2;
- formulación más precisa de los artefactos auditables: código, certificados compactos, replay, ledgers y hashes;
- exclusión explícita del payload de 19.7 GB del paquete ligero y del grafo de dependencia de los teoremas del paper.

### 3.3 Claim P10

Se conservó la matriz canónica P1–P14 y se enriqueció exclusivamente P10:

- intervalo `186..212`;
- Stage A exacto hasta `t=185`;
- Stage B2 abierto y condicionado al payload verificado de 128 buckets;
- prohibición de afirmar un valor exacto de `tau5`.

## 4. Material que no debe sustituir al canon

### 4.1 Paper I TeX adjunto

No debe reemplazar `paper/main.tex`. Aunque actualiza correctamente el intervalo de `tau5`, es editorialmente más débil que la versión vigente porque elimina o reduce:

- el dominio parcial explícito de `S_B`;
- la auditoría de 46 ramas del terminal set;
- referencias recientes y posicionamiento bibliográfico;
- la limitación clean-room externa;
- metadatos y afiliación institucional más completos.

Se conserva como snapshot histórico de v1.1.

### 4.2 Prompt de sesión fresca adjunto

Está supersedido:

- fija el commit antiguo `725c1ae4...`;
- invoca `verify_checkpoint.py --full`, que no es el comando del repositorio canónico.

La versión válida es `docs/FRESH_SESSION_HANDOFF_2026-10-28.md`.

### 4.3 Handoff Stage B2 adjunto

Su semántica científica es correcta y valiosa, pero sus comandos son inválidos para la estructura actual:

- `cd 03_STAGE_B2` no corresponde al repositorio;
- `verify_checkpoint.py` no existe en `main`;
- `RUN_STAGE_B2.sh` no existe en `main`.

Los comandos canónicos son:

```bash
scripts/stage_b2/locate_checkpoint.sh /mnt /srv /data /home /root
python scripts/stage_b2/validate_checkpoint.py /path/to/checkpoint \
  --hash-manifest data/stage_b2/RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt \
  --mode full --output CHECKPOINT_READINESS_FULL.json
scripts/stage_b2/run_stage_b2.sh
```

La fuente operativa válida es `docs/STAGE_B2_RUNBOOK.md`.

## 5. Duplicados y snapshots históricos

### 5.1 SHA-256 de buckets

El archivo adjunto `RGPHI_FRONTIER185_BUCKET_SHA256SUMS.txt` es una copia exacta del archivo canónico bajo `data/stage_b2/`. Debe existir una sola copia canónica en Git; las demás son copias de transporte.

### 5.2 Reviewer bundles

El supercierre contiene:

- un wrapper corto que vuelve a incluir el bundle completo;
- el bundle completo del commit `725c1ae4...`.

Ambos son históricos. El bundle antiguo conserva una inconsistencia: status en `186..212`, pero TeX/PDF/claim matrix en `179..212`. No deben circular como paquete de revisión vigente.

### 5.3 MULTIFRONT-005

El bundle completo es un activo de Release/Zenodo identificado por SHA-256. Sus deltas científicos ODT-009, BQ-010A y HM-010 ya están incorporados en el repositorio bajo autoridad `EXPERIMENTAL_ISOLATED`. No corresponde reimportar sus tablas masivas ni wrappers narrativos como blobs ordinarios.

## 6. Hallazgos en HOLD

El documento de cierre reporta atlas de trampas para denominadores 2,500, 5,000 y 10,000. En el paquete adjunto y en el repositorio canónico sólo se localizaron artefactos verificables del atlas `D=500`.

Por tanto, los conteos mayores quedan:

`HOLD_UNVERIFIED_ARTIFACT_MISSING`.

Pueden promoverse únicamente cuando aparezcan los CSV/JSON, código, comandos y hashes correspondientes.

## 7. Inconsistencias editoriales pendientes

- La cover letter está dirigida a *Journal of Modern Dynamics*.
- El scorecard adjunto prioriza *Dynamical Systems* y *Ergodic Theory and Dynamical Systems*, y no evalúa explícitamente JMD.

Antes del envío debe cerrarse una decisión editorial única y documentar por qué el target elegido domina a las alternativas.

## 8. Incidencia de gobernanza activa

El repositorio declara `main` como rama canónica en la documentación, pero la rama por defecto de GitHub continúa siendo `Ulalito's-Island`, todavía anclada al commit histórico `725c1ae4...` al inicio de esta auditoría.

Esto puede mostrar al visitante una versión anterior del objeto científico. Debe:

1. cambiarse la rama por defecto a `main`; o, como mitigación mínima,
2. mantenerse `Ulalito's-Island` fast-forward a la cabeza de `main` hasta poder cambiar la configuración.

## 9. Corpus rector recomendado

### Canon activo

- `metadata/CANONICAL_STATE.json`;
- `docs/SCIENTIFIC_STATUS.md`;
- `docs/canon/CENTRUM_2026-10-28.md`;
- `paper/main.tex`, `paper/supplement.md`, claim matrix y cover letter;
- `docs/STAGE_B2_RUNBOOK.md`;
- `docs/FRESH_SESSION_HANDOFF_2026-10-28.md`.

### Activos de publicación/release

- Paper I PDF y reviewer bundle reconstruidos por CI;
- Stage B2 production kit y hashes;
- bundles experimentales por SHA-256;
- supercierre y cierre DOCX como provenance snapshots, no como fuente de verdad.

### Material descartable por duplicación

- wrappers que contienen otros ZIPs idénticos;
- copias adicionales del hash manifest;
- componentes ya contenidos sin modificación dentro de MULTIFRONT-005;
- narrativas anteriores que contradicen el estado legible por máquina.

## 10. Frontera científica vigente

No cambia el canon:

- `tau1=45`, `tau2=85`, `tau3=120`, `tau4=162`;
- `186 <= tau5 <= 212`;
- testigo superior en 212 acciones;
- Stage B2 abierto y no ejecutado sin payload;
- Paper I independiente de `tau5` exacto;
- ramas experimentales sin autoridad retroactiva.

El resultado de la canonización es un corpus más pequeño, más coherente y con menos riesgo de doble canon, sin perder ninguno de los aportes científicos verificables del paquete.
