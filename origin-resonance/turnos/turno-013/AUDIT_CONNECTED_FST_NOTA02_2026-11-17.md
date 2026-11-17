# Origin–Resonance · Turno 013 · Auditoría independiente de Nota02 y FST conectado

**Fecha:** 2026-11-17. **Jurisdicción:** SOLO `research/origin-resonance-001`.
**Clase:** `INDEPENDENT_FINITE_CHECK / SOURCE_BOUNDARY / NO_POST_HOC_PROMOTION`.
**Autoridad:** `SEPARATE_PROSPECTIVE_NO_CANONICAL_OVERRIDE`.

## Identidad de las fuentes examinadas

- RGΦ `main`: `c25857e53eea8585a4f10e0a5a42295a315151ec`, sin nuevos commits contra la referencia previa.
- Origin–Resonance antes de esta auditoría: `5b89e6afbb2df15ff6fe8c69dab78af30d7e5d0b`, **13 commits por delante** de `d3de36718ce4ebeeebe6988af62190725a57c49a`, con nuevas piezas de Turno 013 y apertura de Turno 014.
- FST/seno–π conectado: `FacundoFirmenich/sinus-math`, rama privada `research/sinus-pi-centrum-v0.5.0`, commit `cb644a66045a15b8c1de4756a214020f42676f25`; **10 commits por delante** de `research/sinus-pi-centrum-v0.4.0`. El default `Ulalito's-Island` continúa en `a771a6115f31859587e2995c56d2c0802a9be9d5`.

Se examinaron las fuentes de las seis líneas del Turno 013, Nota02, el script `check_nota02_qobs_343.py` y los manuscritos y registros textuales de seno–π v0.5.0. No se ha escrito en ninguna rama ajena a resonancia.

## Nota02: cálculo independiente y fronteras

Para `q_obs=pi/18`, `N=pi/q_obs=18`:

```
Phi1(18)=17; Phi2(18)=19; Phi3(18)=18^2+18+1=343=7^3=(111)_18
343=9*36+19=10*36-17
343^2 ≡ 1 (mod 36)
```

La multiplicación por `343 mod 36` fija cada clase **par** y traslada cada clase **impar** en 18 posiciones. El comprobador independiente ratifica estas igualdades enteras, más la expansión decimal de `E(343)`:

```
H_infinity = E(343) = 0.00583733240261463326217059819536603...
L_Huff,infinity = 0.00583940372208739345789748675622534...
```

En el script la serie se suma hasta `f=24` en 72 cifras decimales; esa truncación basta holgadamente para los 30 decimales comparados, **sin representar una demostración simbólica nueva de la identidad FST-13**. Se conserva la identidad FST-13 exacta ya establecida.

**Negativo preservado, no reejecutado:** la derivación directa de `00583733` desde 168 mantisas continúa como `REFUTED_IN_DECLARED_JURISDICTION` para los dominios directo, una operación, dos operaciones, órbita directa de 343 y sufijo FST-14. El archivo `check_nota02_qobs_343.py` verifica identidades y entropía, no reproduce las 113.799.168 expresiones del barrido; aquí **no** se reivindica una segunda auditoría exhaustiva de esas búsquedas. No existe nueva recurrencia independiente preregistrada de la escalera, ni inferencia UMI causal: `POST_HOC / INDEPENDENT_RECURRENCE_OPEN / CAUSAL_UMI_OPEN`.

## FST-14 conectado: resultados precisos de fase, sin transferencia ilegítima

La rama v0.5 sostiene el mapa seno–π `z_(n+1)={100 z_n}` y la observación de familias `theta_m={m z}`, con `m={5,9,10,12,15}`. Su comparación con el operador FST-14 por `343^j` es **externa**: `100` no es unidad 10-ádica.

En el círculo de fases completas, `z -> ({m_1z},...,{m_rz})` tiene kernel de cardinal `gcd(m_1,...,m_r)`; la unicidad requiere gcd uno. Para `(15,12,5)`, gcd uno; ninguna pareja que contenga `15` sirve por sí sola.

Para prefijos, con `10^d z=k+u` y `b_m=(m k+floor(m u)) mod 10^d`, se enumeraron **exhaustivamente y por fracciones exactas** los puntos de corte del acarreo común:

| Jurisdicción exacta | Intervalos de acarreo | Configuraciones | Prefijos `k` ambiguos |
|---|---:|---:|---:|
| `m=(5,12), d=2` | 16 | 1.600 | 0 |
| `m=(5,12), d=3` | 16 | 16.000 | 0 |
| `m=(15,12,5), d=1` | 24 | 240 | 0 |

Para `(5,12), d=1` existen colisiones, que se retienen como resultado negativo. El resultado general `d>=2` está formulado en el manuscrito local; esta auditoría **corrobora d=2,3**, no reejecuta su demostración completa ni convierte estos prefijos en recuperación de la fase real exacta.

### Frontera 10-ádica de 343

Los índices `phi(10^d)/ord_(10^d)(343)` comprobados son `1,10,20,40,80,80,80` para `d=1,...,7`. Además, `v_5(343^4-1)=2`, `v_2(343^2-1)=4`; aplicando LTE y CRT, el **índice del subgrupo generado por 343 es 80 para todo d>=5**. Esto pertenece exclusivamente a FST-14, no al mapa `z->{100z}` de seno–π.

**Boundary de reproducibilidad:** el árbol Git visible de `sinus-math` v0.5 contiene manuscritos, registros y README, pero **no** incluye los `src/*.py`, `history/originals`, certificados ni `data/REPLAY_STATUS_v0.5.json` citados en el README. La declaración 40/40 y la evidencia externa de 120 fases de π, 1051 pruebas seleccionadas de FST-14 y el replay integral quedan **NO_INDEPENDENT_REPLAY** desde esa instantánea. El propio README registra que el replay integral quedó interrumpido; no se interpreta como `FULL_PASS`.

## Taxonomía y aperturas

- **SUPERACCESS** reconstruye información aritmética o histórica interna oculta por la observación.
- **HYPERACCESS** es la llave residual de completitud sin error que selecciona el representante exacto en la fibra observacional; su coste normalizado puede tender a cero. No es sinónimo de compresión total de palabra.
- La identidad `H_infinity=E(343)` es de FST-13 y condicionada por la fuente uniforme en su interpretación entrópica; no es constante universal de compresión ni prueba de causalidad UMI.
- El producto FST×D3, el límite del observador D-finito, la codificación universal y las complejidades temporales del Turno 013 mantienen sus **jurisdicciones declaradas**. La demostración de una acción semidirecta genuina, los límites Markov asintóticos, los costes minimax universales y el cierre temporal exacto permanecen abiertos.
- Nota02 y RC28 se conservan como **post hoc** donde corresponde. No se modificó ningún endpoint preregistrado.

## Reproducción

`python origin-resonance/turnos/turno-013/check_connected_fst_nota02_T013.py`

Resultado local anterior a publicación: `PASS_T013_CONNECTED_FST_NOTA02_FINITE_EXACT`.

**Conclusión:** nueva evidencia aritmética y finita de interoperabilidad FST/seno–π en resonancia; sin autoridad para reescribir RGΦ `main`, FST upstream ni adjudicar causalidad UMI. Se preservan expresamente los límites, los negativos y lo no reejecutado.
