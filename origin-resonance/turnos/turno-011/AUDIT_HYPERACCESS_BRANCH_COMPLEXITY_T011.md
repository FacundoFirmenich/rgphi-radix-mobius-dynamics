# Origin–Resonance · Turno 011 · Auditoría de fibras de observación

Fecha: 2026-11-17. Jurisdicción: modelo simbólico UMI/Koch y observador que registra únicamente extremos de células indexadas.

## 1. Invariantes corregidos

- Semilla latente:
  \[
  \lambda_n=(\pi/6)10^n.
  \]
- Centrum:
  \[
  C_n=(5\pi/3)10^n.
  \]
- Cota lateral vinculante:
  \[
  a_n=(2/30)C_n=(\pi/9)10^n.
  \]
- Ley tripolar:
  \[
  U_{n,\sigma}=(\pi/9)10^n(15+\sigma).
  \]
- Sombra proyectiva:
  \[
  [14:15:16].
  \]

Las fórmulas anteriores con `pi/8` y el geocolapso hacia `[1:1:1]` quedan supersedidas.

## 2. Complejidad zero-error de una fibra celular

Sean `N>=1` células indexadas cuyos tres generadores `sigma=-1,0,+1` comparten los extremos observados. Sea

\[
\mathcal A_N\subseteq\{-1,0,+1\}^N
\]

el conjunto no vacío de configuraciones admitidas.

El coste mínimo de una llave binaria fija que identifica la configuración es

\[
\boxed{c_N=\lceil\log_2|\mathcal A_N|\rceil.}
\]

### Regímenes

- Coherencia global:
  \[
  |\mathcal A_N|=3,
  \quad c_N=2,
  \quad c_N/N\to0.
  \]
- Selección independiente:
  \[
  |\mathcal A_N|=3^N,
  \quad c_N=\lceil N\log_2 3\rceil,
  \quad c_N/N\to\log_2 3.
  \]

Más generalmente:

\[
\boxed{c_N/N\to0\iff\log|\mathcal A_N|=o(N).}
\]

Por tanto, la variación por célula no hereda automáticamente hiperacceso global. Sí puede coexistir con multifractalidad cuando la gramática restringe subexponencialmente las configuraciones.

## 3. Seis caras

Para caras completas

\[
\mathcal F_6=\{M,m\}\times\{-,0,+\},
\]

la versión libre posee `6^N` historias y tasa `log2(6)`. Una cara coherente para toda la torre cuesta `log2(6)` bits en total y tasa nula.

## 4. Multifractalidad

La ley escalar radial por diez no es por sí sola multifractal. El Turno 011 introduce una medida Koch activa con pesos

\[
(15,14,16,15)/60,
\]

cuyo `tau(q)` es no lineal. Éste es el endpoint multifractal efectivo; no la mera existencia de tres fases.

## 5. FST

El snapshot externo inspeccionado de `sinus-math` no contiene el motor completo anunciado. Eso constituye un gap de procedencia de ese snapshot, no una refutación.

Separadamente, el corpus FST-11 entregado por el usuario en esta conversación contiene manuscrito, motor y protocolo; sus resultados se usan con sus boundaries declarados. En particular, el manuscrito prueba la forma normal única `(h,j,t)`, y distingue el entero recuperado de la longitud/prefijo aún necesaria para reconstruir la palabra literal.

## 6. Endpoints

- Hiperacceso coherente: `CLOSED_CONDITIONAL_COMBINATORIAL`.
- Multifractalidad Koch–UMI: `CLOSED_FOR_DEFINED_MEASURE`.
- Bloqueo biplanar dinámico simple: `CLOSED_MODEL`.
- Incertidumbre: `CONDITIONAL_NONCOMMUTATIVE_MODEL`.
- Operador ramanujiano interno: `CLOSED_DEFINITIONAL_OPERATOR`.
- Realización física: `NOT_CLAIMED`.
