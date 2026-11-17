# Origin–Resonance · Turno 011 · Auditoría de fibras de observación y frontera FST
Fecha: 2026-11-17. Jurisdicción: modelo simbólico UMI/Koch de Turno 010 y observador que registra únicamente extremos de células indexadas. Autoridad: SEPARATE_PROSPECTIVE_NO_CANONICAL_OVERRIDE.

## 1. Invariantes de entrada (sin reinterpretación)
- Semilla latente literal: \`(pi/6)*10^(+n_scalar)\`; en símbolos, \(\lambda_n=(\pi/6)10^n\).
- Ley tripolar: \(\displaystyle U_{n,\sigma}=(\pi/24)(40\,10^n+3\sigma)\), con \(\sigma\in\{-1,0,1\}\).
- SUPERACCESS reconstruye información interna oculta; HYPERACCESS aporta la llave cualitativa de completitud de error cero, cuyo coste normalizado *puede* tender a cero.
- El cociente monoescalar \(1/10\) no demuestra multifractalidad; la extensión precisa contracciones dependientes de rama y una \(\tau(q)\) no lineal.
- La oscilación clásica no implica incertidumbre de Heisenberg; el modelo qutrit es matemático y condicional.
- RC28 sigue siendo resonancia post hoc y la prueba independiente preregistrada está abierta; el operador ramanujiano (dominio/composición/invariantes) sigue abierto.

## 2. Teorema condicional T011-H1: complejidad de la llave versus variación por célula
Tomemos \(N\ge1\) células **indexadas** cuyos generadores \(G_{\sigma}\) son los de Nota 00: los tres estados \(\sigma=-1,0,+1\) comparten sus extremos inicial/final. Sea \(\mathcal A_N\subseteq\{-1,0,+1\}^{N}\) el conjunto **no vacío** de configuraciones admitidas y sea \(O_N\) el observador que conserva solamente esos extremos. Su lectura coincide para todos los elementos de \(\mathcal A_N\).

**Resultado exacto:** el coste mínimo de una llave binaria de longitud fija que identifica sin error la configuración, una vez realizada la observación, es
\[
c_N=\lceil\log_2|\mathcal A_N|\rceil.
\]
**Demostración:** todos los elementos pertenecen a la misma fibra de \(O_N\). Una llave de \(b\) bits tiene como máximo \(2^b\) valores; la identificación inyectiva exige \(2^b\ge|\mathcal A_N|\). La asignación de códigos distintos logra la cota.

**Dos regímenes distintos:**
- Coherencia global \(\sigma_1=\cdots=\sigma_N\): \(|\mathcal A_N|=3\), \(c_N=2\) bits (un trit), \(c_N/N\to0\).
- Selección independiente sin restricciones: \(|\mathcal A_N|=3^N\), \(c_N=\lceil N\log_2 3\rceil\), y \(c_N/N\to\log_2 3>0\).

Más generalmente, \(c_N/N\to0\) **si y sólo si** \(\log|\mathcal A_N|=o(N)\) para estas fibras y esta normalización. Por tanto la selección variable por célula **no hereda automáticamente** el hiperacceso global de un trit del Turno 010. Un generador de configuraciones fuertemente restringido puede ser simultáneamente dependiente de rama y subextensivo; no se ha demostrado incompatibilidad universal entre multifractalidad e hiperacceso.

**Límite crucial:** esta prueba trata únicamente la observación de extremos; un observador que resuelve segmentos interiores puede distinguir configuraciones. La variable \(N\) cuenta células, mientras \(n\) denota el exponente escalar: sus normalizaciones no se identifican.

## 3. Control aritmético T010 (jurisdicción explícita)
La terna \((40\,10^n-3,40\,10^n,40\,10^n+3)\) es entera primitiva para todo \(n\in\mathbb Z_{\ge0}\), ya que \(\gcd(40\,10^n,3)=1\). La escritura «para integer n» sin cota inferior no está justificada (por ejemplo, \(n=-2\) genera una terna no entera). Este ajuste de jurisdicción **no modifica** el teorema T010-A, que sí fija \(n\ge0\).

El límite proyectivo \([1:1:1]\) es exacto. Para un observador con precisión arbitraria a cada \(n\) finito, las ramas siguen separadas; la fibra ternaria de hiperacceso requiere un cociente/resolución observacional declarados. La tasa \(\log_2 3/(n+1)\to0\) utiliza la escala descriptiva elegida \(n+1\), sin demostrar una tasa operacional independiente de esa elección.

La comprobación independiente de 50 sombras primitivas \(0\le n<50\), norma del conmutador qutrit \(\|[J_z,F_3J_zF_3^\dagger]\|_F=2\), y varianzas \(\pi^2/96,\pi^2/128\) es consistente con los enunciados. Un cálculo finito no sustituye demostraciones simbólicas ni una realización cuántica.

## 4. Línea FST conectada: comprobación de procedencia
Se inspeccionó \`FacundoFirmenich/sinus-math\` en \`a771a6115f31859587e2995c56d2c0802a9be9d5\` (2026-11-17, 14:45:03 UTC). El árbol Git disponible contiene **únicamente README.md**. Aunque ese README anuncia 24/24 pruebas PASS y un motor FST-11 histórico preservado, no están versionados en ese commit \`src/check_local.py\`, los supuestos certificados, ni el código FST-11; la lectura directa de \`src/check_local.py\` devolvió 404. Resultado: \`PROVENANCE_GAP / CLAIM_UNVERIFIED_IN_CONNECTED_SNAPSHOT\`, **no** refutación de los resultados FST-11 ni del Turno 009. No se transfieren resultados no inspeccionables a la autoridad canónica o de resonancia.
Referencia: https://github.com/FacundoFirmenich/sinus-math/commit/a771a6115f31859587e2995c56d2c0802a9be9d5

## 5. Endpoints y prohibiciones de promoción
- T010_MF_UMI_NONLINEAR_TAU: **OPEN**; variar estados o anchos no sustituye construir medida, contracciones dependientes de rama, \(\tau(q)\) y verificar no-linealidad.
- T010_TRIPOLAR_HYPERACCESS_INDEPENDENT_REALIZATION: **PARTIAL_CONDITIONAL**; T011-H1 establece la restricción combinatoria, sin una nueva realización independiente.
- T010_BIPLANAR_PHASE_LOCK: **OPEN_DYNAMIC**; el mínimo de \(E_\kappa\) sobre la diagonal es estático, no un teorema de estabilidad para dinámica con retardos.
- T010_NONCOMMUTATIVE_UNCERTAINTY_MODEL: **CONDITIONAL_MATHEMATICAL**; el conmutador es no nulo, sin afirmación física.
- FST-11: permanece la distinción SUPERACCESS/HYPERACCESS de Turno 009; reproducción completa del motor histórico no confirmada aquí.
- Royal Cubit/RC28: gauge histórico y coincidencia post hoc; control independiente RC28 abierto.
- Ramanujan: operador exacto y teorema de composición pendientes.

**No contaminación:** \`main\` no se altera; quedan intactos errores históricos identificados, resultados negativos, dominios finitos y etiquetas post hoc. El presente documento es un certificado nuevo de la rama de resonancia, no un teorema del Paper III.
