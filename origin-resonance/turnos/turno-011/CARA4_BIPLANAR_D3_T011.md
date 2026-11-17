# Cara 4 — Biplanaridad y cosimultaneidad \(D_3\)

## 1. Hexafacialidad

Como conjunto,

\[
\mathcal F_6=\{M,m\}\times\mathbb Z_3.
\]

Como simetría, no es el producto directo abeliano. La ley correcta es

\[
\boxed{
D_3\cong\mathbb Z_3\rtimes_{-1}\mathbb Z_2
=
\langle r,s\mid r^3=s^2=e,\ srs=r^{-1}\rangle.
}
\]

Representamos una cara por \((\varepsilon,k)=r^ks^\varepsilon\), con
\(\varepsilon\in\mathbb Z_2\) y \(k\in\mathbb Z_3\). Entonces

\[
\boxed{
(\varepsilon,k)(\eta,\ell)
=
(\varepsilon+\eta,\ k+(-1)^\varepsilon\ell).
}
\]

## 2. Cambio de plano e inversión polar

La operación de cambio de plano actúa como

\[
\boxed{
S(P,k)=(\bar P,-k).
}
\]

Por tanto:

\[
(M,+)\leftrightarrow(m,-),
\qquad
(M,-)\leftrightarrow(m,+),
\qquad
(M,0)\leftrightarrow(m,0).
\]

En los valores normalizados

\[
\left(\frac{14}{15},1,\frac{16}{15}\right),
\]

el cambio de plano es la involución

\[
\boxed{x\mapsto2-x.}
\]

## 3. Fases discretas

Sean

\[
k_M,k_m\in\mathbb Z_3.
\]

Para un desfase \(\delta\in\mathbb Z_3\), definimos

\[
\boxed{
E_{\kappa,\delta}
=
\kappa\left[1-\cos\left(\frac{2\pi}{3}(k_M-k_m-\delta)\right)\right].
}
\]

Si \(\kappa>0\), los mínimos satisfacen

\[
\boxed{k_M-k_m=\delta\pmod3.}
\]

Hay tres pares bloqueados, uno por fase global.

## 4. Fases continuas

\[
E_{\kappa,\Delta}
=
\kappa[1-\cos(\theta_M-\theta_m-\Delta)].
\]

Bajo flujo gradiente, con \(\phi=\theta_M-\theta_m-\Delta\):

\[
\dot\phi=-2\kappa\sin\phi.
\]

Para \(\kappa>0\), \(\phi=0\) es estable y \(\phi=\pi\) inestable.

## 5. Cosimultaneidad

El estado bloqueado es

\[
\boxed{|M,k+\delta\rangle\oplus|m,k\rangle.}
\]

Una fase global y un desfase determinan las dos manifestaciones cosimultáneas.

## 6. Resultado

La expresión trifásica está gobernada por \(\mathbb Z_3\); el intercambio de planos está gobernado por \(\mathbb Z_2\); y la inversión de fase convierte su combinación en \(D_3\), no en \(C_6\).
