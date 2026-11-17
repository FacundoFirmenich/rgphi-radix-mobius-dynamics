# Teorema T009-B — FST-11 como prototipo exacto de UMI escalonada

## 1. Torre de cocientes

Sea \(\Sigma=\{0,\ldots,9\}\) y

\[
\mathcal K(w)=8\,10^{|w|}-9\operatorname{val}(w).
\]

FST-11 demuestra la torre exacta

\[
\boxed{\Sigma^*\xrightarrow{\mathcal K}8+9\mathbb Z\xrightarrow{\Pi_7}\mathcal H}
\]

con

\[
\mathcal H=\{h\in\mathbb Z:7\nmid h,\ h\bmod9\in\{2,5,8\}\}.
\]

Cada palabra posee coordenadas únicas

\[
\boxed{w=8^t C\!\left(7^{a_0(h)+3j}h\right),\qquad(h,j,t)\in\mathcal H\times\mathbb N_0^2.}
\]

## 2. UMI aritmético-literal

Definimos \(\mathcal U_{\mathrm{FST}}=\mathcal H\times\mathbb N_0^2\). Un punto \(u=(h,j,t)\) tiene las proyecciones

\[
\pi_{\mathrm{norm}}(u)=h,
\quad
\pi_{\mathrm{ent}}(u)=K=7^{a_0(h)+3j}h,
\quad
\pi_{\mathrm{lit}}(u)=w=8^tC(K).
\]

El mismo nodo conecta el plano normalizado, el plano entero y el plano literal.

## 3. Dos direcciones latentes independientes

Para \(h\) fijo, la fibra es \(\mathbb N_0^2\), con:

- \(j\): profundidad multiplicativa invisible para \(\Pi_7\);
- \(t\): cantidad de prefijos 8, invisible incluso para \(\mathcal K\).

La longitud literal activa su acoplamiento:

\[
\boxed{|w|=t+\ell_*\!\left(7^{a_0(h)+3j}h\right).}
\]

Ésta es una realización exacta de ejes latentes independientes que se correlacionan al incorporar una observación de frontera.

## 4. Reclasificación superacceso / hiperacceso

### Superacceso

\[
(\Pi_7(K),\Pi_2(K))\longmapsto K
\]

mediante

\[
K=\operatorname{sgn}(K)\operatorname{mcm}(|\Pi_7(K)|,|\Pi_2(K)|).
\]

Recupera información aritmética interna eliminada por cada normalizador individual.

### Hiperacceso

Con \(K\) conocido, persiste la fibra \(\{8^tC(K):t\ge0\}\). La coordenada cualitativa de frontera es \(t\), o equivalentemente la longitud literal.

En la familia acotada por longitud máxima \(L\), la fibra contiene

\[
m_L=L-\ell_*(K)+1
\]

representantes y la llave zero-error óptima cuesta

\[
\boxed{c_L=\lceil\log_2m_L\rceil.}
\]

Como \(c_L/L\to0\), la llave de longitud/prefijo es un hiperacceso subextensivo: no reconstruye por sí sola \(K\), pero sincroniza el entero ya recuperado con su escritura literal completa.

## 5. Conclusión

\[
\boxed{\text{superacceso recupera }K;\qquad\text{hiperacceso selecciona }t.}
\]

La reclasificación no altera los teoremas de FST-11; corrige su ubicación conceptual dentro de Origin–Resonance.
