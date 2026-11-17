# Origin–Resonance · Turno 013 · Seguimiento conectado seno–π/FST v0.5–v0.6 (2026-11-17)

**Jurisdicción:** monitor prospectivo de la rama `research/origin-resonance-001`, **sin autoridad sobre** RGΦ `main`, seno–π/FST externo ni anteriores resultados FST.  
**Clase:** `INDEPENDENT_NARROW_MATH_CHECK / UPSTREAM_CI_FAILURE / NO_CANONICAL_PROMOTION`.

## Identificación Git exacta

- RGΦ `main`: `c25857e53eea8585a4f10e0a5a42295a315151ec`, comparación idéntica a referencia.
- Resonancia al iniciar este control: `ad682292f834bb4fd1a6ad091e5766a2b3a3728b`, idéntica a referencia anterior.
- `FacundoFirmenich/sinus-math` — `research/sinus-pi-centrum-v0.5.0`: `4e4ccdb874c1ff31e62dc23713c6c1f29561d124`, **9 commits** nuevos respecto de `cb644a66045a15b8c1de4756a214020f42676f25`. Publicó texto fuente original FST-14, el auditor local de fases, el certificado decimal de π y el estado de replay que faltaban en el corte anterior.
- `research/sinus-pi-centrum-v0.6.0`: `b368a8e365ae2c3d79da975c4755825073990a5d`, **15 commits** por delante de la cabeza v0.5. Añade `LOCAL_THEOREM_v0.6_ES.md`, `audit_borrow_inverse_v06.py`, `BORROW_INVERSE_CERTIFICATE_v0.6.json` y generación de tres niveles del subcentrum.
- Referencias: [v0.5](https://github.com/FacundoFirmenich/sinus-math/commit/4e4ccdb874c1ff31e62dc23713c6c1f29561d124), [v0.6](https://github.com/FacundoFirmenich/sinus-math/commit/b368a8e365ae2c3d79da975c4755825073990a5d).

## Resultado matemático independiente, exactamente delimitado

Se revisó el **código publicado** de v0.6 y se realizó una comprobación independiente con fracciones exactas. Para el conjunto de 37 cifras en base 100 declarado por el teorema local, sus 37 por 5 celdas de multiplicadores `m=(5,9,10,12,15)` cumplen la separación estricta. El menor margen racional comprobado es **89/1131900 > 0**. La cota usa únicamente `π<22/7` y `0<x−sin(x)<x³/6`. La invariancia del alfabeto por el mapa de desplazamiento `T(z)={100z}` proporciona un conjunto autosimilar de itinerarios de cinco marcas constantemente cero. Sus contracciones disjuntas implican exactamente

`dim_H C_D = log(37)/log(100) = 0.7841008620334974...`.

**Interpretación:** la fibra observacional de esa secuencia simbólica común contiene una familia no numerable de fases con dimensión al menos ese valor. Es una **no inyectividad en el círculo de fases arbitrarias**, no un resultado sobre las cifras particulares de π, las series históricas, SUPERACCESS del código íntegro, ni una identidad con FST-13. La fuente local reporta 13 códigos de una etapa; **condicionada a ese conteo previo**, la entropía condicional bajo fase uniforme satisface `H(U_t|Y_0,...,Y_(t-1)) ≥ t log₂(100/13)` y la tasa de éxito del mejor decodificador de prefijos de base 100 queda acotada por `(13/100)^t`. La cota numérica es `2.9434164716336326...` bits por paso. No es entropía residual FST, ni evidencia sobre normalidad de π.

La recurrencia independiente `a_t=2+J_(t−1)−J_t`, con `b_t=1{J_t>0}` y `J_t≥0`, se reconstruye como `J_t=C+D_t`. **Un cero en b** fuerza el ancla `C`, que produce una trayectoria única o inconsistencia. **Solo unos en b**, sin cota exterior superior, dejan infinitos `C` admisibles. Se contrastó contra búsqueda explícita de estados iniciales en **45.242 contratos finitos** de hasta cuatro avances `a∈{0,...,5}`: 1.555 únicos, 1.555 no identificables, 42.132 inconsistentes. La generalidad de la clasificación descansa en la identidad lineal explícita y no en la prueba finita.

La distinción `b_t=0` (sin préstamo) versus `a_t=0` (sin avance) es esencial. Las ventanas históricas reportadas para el evento 6084 tienen anclajes en 0,03° y 0,024°; las de 0,018° y 0,01° no resultan identificables desde `a,b` solos. **No** se repitió el censo histórico de tres millones.

**Reproducción:** `python origin-resonance/turnos/turno-013/check_connected_sinus_v06_T013.py`. Resultado previo a publicación: `PASS_T013_CONNECTED_SINUS_V06_INDEPENDENT_NARROW`. Este checker no importa el proyecto externo y audita las condiciones matemáticas limitadas, no su pipeline editorial.

## Negativo adicional de infraestructura: CI no certificada

Las dos nuevas ejecuciones de GitHub Actions del repo conectado concluyeron **`failure`**:

- [v0.5, run 44140178760](https://github.com/FacundoFirmenich/sinus-math/actions/runs/44140178760), 17-XI 17:43 UTC, `failure`, `head_sha=4e4ccdb`.
- [v0.6, run 44147596941](https://github.com/FacundoFirmenich/sinus-math/actions/runs/44147596941), 17-XI 18:25 UTC, `failure`, `head_sha=b368a8e`.

Las respuestas de pasos están vacías y el endpoint de logs devolvió `BlobNotFound`; **no se conoce la causa del fallo** y no puede atribuirse a la matemática, al runner ni a permisos sin evidencia. Por tanto, los `40/40` y `48/48` declarados en los README siguen siendo **resultados locales declarados, no CI PASS**. La incorporación de fuentes hace posible inspección de código que anteriormente era imposible en Git, pero **no** reejecuta por sí misma los 1.051 casos FST-14, las 120 inversiones de fase de π ni la suite legada 50/50.

## Transferencia a Origin–Resonance y reservas

- **SUPERACCESS**: reconstruye información interna aritmética, subsistémica o histórica. **HYPERACCESS**: llave residual sin error que selecciona un representante exacto de una fibra de observación. El no-go de las cinco marcas muestra el tamaño de una fibra de un **observable parcial diferente**: no prueba ni niega un teorema general de hiperacceso ni invalida otras familias de observables.
- **Nota02 sin cambio:** derivación directa de `00583733` desde 168 mantisas **negativa** en las cinco jurisdicciones congeladas: directa, una operación, dos operaciones, órbita directa de 343 y sufijo FST-14. No se reejecutó el barrido. La escalera `N=π/q_obs=18`, `Φ₁=17`, `Φ₂=19`, `Φ₃=343=7³=(111)₁₈`, `343=9·36+19=10·36−17`, `343²≡1 (mod 36)` permanece identidad entera verificada. `H∞=E(343)=0.005837332402614633262...` permanece identidad exacta FST-13, con interpretación entrópica **dependiente de la fuente**, sin promoción causal UMI.
- **No hay recurrencia independiente preregistrada** de la escalera ciclotómica. RC28 sigue `POST_HOC`; las obligaciones de FST-14 inversión terminal y frontera de subgrupo 10-ádico mantienen sus dominios propios. El operador `T_{100}` no hereda el grupo de unidades generado por 343.
- Composición FST×D₃, entropías Markov asintóticas, interpretación analítica global de frontera natural y redundancia minimax de códigos residuales **no reciben nuevos cierres** de este resultado. Tampoco se modifica jurisdicción alguna de RGΦ Paper III.

**Decisión de monitor:** se incorpora esta evidencia matemática local y el negativo de reproducibilidad **solo** como seguimiento de resonancia. Sin promoción a los endpoints originales, sin modificación de premisas o archivos canónicos, y conservando correcciones y etiquetas post hoc.
