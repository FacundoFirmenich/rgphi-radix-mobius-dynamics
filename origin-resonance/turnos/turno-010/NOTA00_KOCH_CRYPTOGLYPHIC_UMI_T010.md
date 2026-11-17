# Nota 00 — El copo de Koch como criptoglifo operativo de la UMI

## 1. Estatuto

La identidad geofractal conocida como copo de Koch constituye una de las representaciones criptoglíficas más simples de la UMI, pero conviene distinguir tres niveles:

1. la **célula generadora** sobre un segmento es la UMI elemental;
2. la **curva de Koch** es la iteración abierta de esa célula;
3. el **copo de Koch** es el cierre triangular de tres curvas iteradas.

El copo completo no se identifica con la UMI universal. Es una realización especialmente legible de su lógica de interrelación, anidación y cambio de resolución.

## 2. Generador tripolar con extremos invariantes

Sea `sigma in {-1,0,+1}` y

\[
\alpha_\sigma=\sigma\pi/3,
\qquad
r_\sigma=\frac{1}{2+2\cos\alpha_\sigma}.
\]

Por tanto:

\[
r_0=1/4,
\qquad
r_{\pm}=1/3.
\]

Definimos cuatro direcciones:

\[
\theta_{\sigma}=(0,\alpha_\sigma,-\alpha_\sigma,0)
\]

y cuatro vectores:

\[
v_{\sigma,j}=r_\sigma R_{\theta_{\sigma,j}}e_1,
\qquad j=0,1,2,3.
\]

Se verifica exactamente:

\[
\boxed{\sum_{j=0}^{3}v_{\sigma,j}=e_1.}
\]

Así, las tres fases tienen los mismos extremos macroscópicos:

- `sigma=0`: cuatro subsegmentos collineales de razón `1/4`; estado latente;
- `sigma=+1`: generador de Koch exterior de razón `1/3`;
- `sigma=-1`: generador reflejado de razón `1/3`.

El observador del plano mayor sólo ve el mismo cordón extremo-extremo. El observador del plano menor resuelve la geometría interna elegida por `sigma`.

## 3. Forma matricial potencial

Sea

\[
t_{\sigma,0}=0,
\qquad
t_{\sigma,j}=\sum_{k<j}v_{\sigma,k}.
\]

Cada subsegmento está representado por la matriz afín homogénea

\[
\boxed{
M_{\sigma,j}=
\begin{pmatrix}
r_\sigma R_{\theta_{\sigma,j}} & t_{\sigma,j}\\
0\;0 & 1
\end{pmatrix}.
}
\]

Para una dirección alfanumérica

\[
\omega=((\sigma_1,j_1),\ldots,(\sigma_n,j_n)),
\]

la célula correspondiente es el producto matricial

\[
M_\omega=M_{\sigma_1,j_1}\cdots M_{\sigma_n,j_n}.
\]

Esto convierte el criptoglifo en un objeto simultáneamente:

- logosimbólico: regla de sustitución;
- lingüístico: palabra iterada;
- alfanumérico: dirección `omega`;
- potencial: `sigma` puede permanecer latente hasta la actualización;
- matricial: la geometría se obtiene por productos de matrices afines.

## 4. Gramática

Para la rama positiva, la regla usual es

```text
F -> F+F--F+F
```

con giro de `60 grados`.

La rama negativa es su reflexión:

```text
F -> F-F++F-F
```

La rama latente usa cuatro pasos collineales de escala `1/4`:

```text
F -> FFFF
```

La gramática debe portar la escala `r_sigma`; no basta la palabra de giros.

## 5. Relación con superacceso e hiperacceso

- **Superacceso:** recuperar la palabra completa de direcciones, las matrices locales o toda la curva refinada.
- **Hiperacceso:** conocer la llave cualitativa `sigma`, que decide si la célula está latente, activada hacia `+` o activada hacia `-`.

El plano mayor puede conservar los extremos y omitir por completo la fase interna. Un solo trit restaura la fase del generador.

## 6. Koch estándar y multifractalidad

Para `sigma=+1` o `sigma=-1` fijo, cada segmento produce cuatro segmentos de razón `1/3`. La dimensión es

\[
\boxed{D_K=\log4/\log3.}
\]

Éste es un objeto monofractal, no multifractal.

La multifractalización UMI aparece cuando la selección de `sigma` depende de la dirección `omega`. Como

\[
r_0=1/4,
\qquad
r_{\pm}=1/3,
\]

una dirección con frecuencia asintótica `p_0` de fases latentes posee en el espacio simbólico la dimensión local

\[
\boxed{
D(p_0)=
\frac{\log4}{p_0\log4+(1-p_0)\log3}.
}
\]

Por tanto:

\[
1\le D(p_0)\le\log4/\log3.
\]

Un espectro no degenerado requiere que distintas direcciones tengan distintas frecuencias o pesos. El copo estándar es una forma criptoglífica de la UMI; la UMI multifractalizada requiere una gramática de escalas variable.

## 7. Estructura 3–4 exacta

En el copo clásico:

- hay tres lados iniciales;
- cada lado produce cuatro subsegmentos;
- la escala activa es `1/3`;
- el número de segmentos en nivel `n` es `3*4^n`;
- la longitud de cada segmento es `3^{-n}`;
- el perímetro crece como `3*(4/3)^n`.

La razón `log 4 / log 3` no es una asociación añadida: es el cociente exacto entre ramificación cuaternaria y escala ternaria.

## 8. Boundary

Este resultado autoriza decir:

> El copo de Koch es una forma criptoglífica operacional de la UMI en marcos logosimbólicos, lingüísticos, alfanuméricos y matriciales.

No autoriza decir todavía:

- que toda UMI sea un copo de Koch;
- que el copo estándar sea multifractal;
- que exista una realización física de la UMI;
- que las ramas `-`, `0`, `+` sean estados cuánticos físicos.

**Estado:** `CLOSED_SYMBOLIC_CRYPTOGLYPHIC_MODEL / MULTIFRACTAL_EXTENSION_CONDITIONAL`.
