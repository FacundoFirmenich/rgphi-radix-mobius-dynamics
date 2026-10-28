# Auditoría comparativa e integración RGΦ — 28 de octubre de 2026

## 1. Objeto de la auditoría

Se compararon dos líneas de la misma investigación:

1. **Línea canónica pública**: repositorio `FacundoFirmenich/rgphi-radix-mobius-dynamics`, commit fijado `725c1ae4944a5ec913f0acb9c24a1e9f5a7b2223`.
2. **Línea viva multifrente**: corpus local MULTIFRONT-005 y sus bundles ODT-009, BQ-010A y HM-010.

La auditoría cubre matemática, claims, código, tests, CI, paper, evidencia, Stage B2, gobernanza, reproducibilidad, publicación y frentes experimentales.

## 2. Dictamen

\[
\boxed{\text{línea principal}=\text{repositorio canónico de GitHub}}
\]

Puntuación ponderada:

- repositorio canónico: **83.9/100**;
- línea viva multifrente: **73.4/100**.

La línea viva supera al repo en profundidad experimental; el repo la supera ampliamente como objeto científico público, auditable, publicable y mantenible.

## 3. Por qué gana el repositorio

- jerarquía explícita de evidencia simbólica, finita, computer-assisted y abierta;
- package Python, CLI, tests, CI en Python 3.11/3.12, paper y reviewer packet;
- canon actual en \(186\le\tau_5\le212\);
- motor, validador, smoke tests y contrato operativo para Stage B2;
- separación entre RGΦ mainline, GEN, Artin–Kummer y U5-HD/HM;
- conservación de refutaciones, HOLD, resultados supersedidos y gates externos;
- commit canónico firmado y workflows públicos verdes.

## 4. Incidencia crítica de sincronización

El repo no está todavía internamente cerrado:

- `docs/SCIENTIFIC_STATUS.md` y el README usan \(186\le\tau_5\le212\);
- `paper/main.tex` dice \(179\le\tau_5\le212\);
- `paper/main.pdf` renderiza el mismo intervalo antiguo;
- `paper/claim-evidence-matrix.csv` conserva `interval 179..212`;
- la issue de release conserva texto histórico.

La ciencia mainline no queda refutada, pero el paquete de revisión externa no puede considerarse sincronizado hasta reparar esta discrepancia.

## 5. Auditoría del código y verificación

### Fortalezas

- dinámica exacta con `Fraction`;
- ramas \(T_B\) y \(S_B\) con reducción primitiva explícita;
- determinante de rama comprobado en runtime;
- target membership exacta;
- terminal set de 23 estados;
- verificador de intervalos de robustez y atlas de traps;
- workflows de lint, tests, package build, paper, integridad, reviewer bundle y Stage B2 smoke.

### Gap

`verify_repository()` comprueba que `main.tex` y `main.pdf` existen, pero no que los claims canónicos coincidan entre README, status, paper y claim matrix. Por eso los workflows pueden estar verdes mientras el paper está científicamente desfasado.

## 6. Estado Stage B2

El repositorio posee la arquitectura superior: worker C++ de memoria externa, orchestrator, validación del checkpoint, semántica `HIT / NO_HIT / interrupted`, smoke tests y workflow.

La línea viva no aporta una implementación superior. El único bloqueo real es material: faltan los 128 buckets del checkpoint \(t=185\), con 2.462.600.671 estados y 19.700.805.368 bytes.

## 7. Aportes de la línea secundaria que deben integrarse

### ODT-009

- segundo shell prospectivo `81<=b<=120`;
- 72.600 semillas, 2.448 hits y 9 bases activas;
- réplica positiva de arquitectura jerárquica;
- fallo de réplica de O5;
- mejora pentádica estrecha sólo frente a un modelo enriquecido fallido;
- no promoción global U5;
- cross-check independiente.

### BQ-010A

- teorema exacto \(L_4^{\rm nonadaptive}=4\);
- no-go de la arquitectura `4 root-only + 31`;
- conservación rigurosa de \(35\le M_3\le36\);
- exclusión sólo de la ruta block-separable, no del problema global.

### HM-010

- no-go de ideal unital para una extensión no escindida;
- estabilización \(C^*(D_\infty)\otimes\mathcal K\);
- \(KK^1(B,J)\cong M_{3\times2}(\mathbb Z)\);
- boundary map species-separating;
- \(K_0(E)=\mathbb Z^3,\ K_1(E)=0\);
- half-shift retenido como invariante secundario;
- estatuto explícito `EXPERIMENTAL_ISOLATED`.

## 8. Qué no debe fusionarse al canon

- narrativas de portfolio duplicadas;
- outcomes masivos como blobs ordinarios;
- afirmaciones físicas, ontológicas o cosmológicas;
- promoción U5;
- cierre de \(\tau_5\);
- un segundo motor Stage B2 redundante;
- claims experimentales dentro del Paper I.

## 9. Fusión recomendada

1. corregir intervalos y claim matrix;
2. añadir test automático de consistencia canónica;
3. compilar el PDF dentro del workflow de reviewer bundle;
4. archivar ODT-009, BQ-010A y HM-010 bajo `research/experimental`;
5. registrar hashes de bundles en manifests;
6. abrir PR draft sin cambiar claims de Paper I salvo la actualización factual del intervalo;
7. mantener Stage B2 y validación externa como gates abiertos;
8. cambiar manualmente la rama por defecto a `main`.

## 10. Estado posterior a la fusión

\[
\boxed{
\text{repo canónico}
+
\text{deltas experimentales verificados}
-
\text{contaminación de autoridad}
}
\]

Ésa es la línea superadora: el repositorio público como sustrato rector y la línea viva como fuente de deltas experimentalmente valiosos.
