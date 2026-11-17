# Teorema-marco T009-A — Unidad Multifractal de Interrelación

## 1. Dos planos y un único objeto de correspondencia

Sean dos espacios observacionales métricos \((X_M,g_M)\) y \((X_m,g_m)\), donde \(M\) denota el plano mayor y \(m\) el plano menor subanidado.

Una **Unidad Multifractal de Interrelación** es un span

\[
\boxed{X_M \xleftarrow{\pi_M} \mathcal U \xrightarrow{\pi_m} X_m}
\]

junto con medidas \(\mu_M,\mu_m\) y, cuando existan, dimensiones locales

\[
d_M(u)=\lim_{r\downarrow0}\frac{\log\mu_M(B_M(\pi_Mu,r))}{\log r},
\quad
d_m(u)=\lim_{r\downarrow0}\frac{\log\mu_m(B_m(\pi_mu,r))}{\log r}.
\]

La UMI es multifractal cuando al menos una de estas dimensiones locales no es constante. El mismo \(u\in\mathcal U\) posee dos representaciones observacionales \(u_M=\pi_M(u)\), \(u_m=\pi_m(u)\); no son dos objetos, sino dos caras proyectadas de una única unidad.

## 2. Geometría variable y cosimultánea

Las dos geometrías coexisten sobre \(\mathcal U\) mediante pullback:

\[
g_{\mathcal U}^{M}=\pi_M^*g_M,
\qquad
g_{\mathcal U}^{m}=\pi_m^*g_m.
\]

El observador inmerso en \(X_M\) trata la primera como geometría base y la segunda como fibra latente; el observador inmerso en \(X_m\) invierte esta lectura. La variabilidad es observador-relativa; la cosimultaneidad pertenece al total \(\mathcal U\).

## 3. Latencia ortogonal

Sobre la suma de espacios tangentes se define

\[
G_0=\begin{pmatrix}g_M&0\\0&g_m\end{pmatrix}.
\]

Entonces \(\langle v_M,v_m\rangle_{G_0}=0\). Los planos están yuxtapuestos y ortogonales, pero no correlacionalmente acoplados.

## 4. Actualización correlacional

Sea \(J_u:T_{\pi_m(u)}X_m\to T_{\pi_M(u)}X_M\) un operador de interrelación y \(\chi\in[0,1]\) un parámetro de actualización. Definimos

\[
G_\chi=\begin{pmatrix}g_M&\chi J_u\\\chi J_u^*&g_m\end{pmatrix}.
\]

- \(\chi=0\): UMI latente;
- \(\chi>0\): UMI efectivizada correlacionalmente.

La transición cambia el rango del bloque mixto. Es una transición de fase algebraica del modelo, no una afirmación termodinámica.

## 5. Invariante de acoplamiento

El operador adimensional normalizado es

\[
\widehat J_u=g_M^{-1/2}J_ug_m^{-1/2}.
\]

Su espectro singular

\[
\boxed{\Sigma_{\mathcal U}(u)=\operatorname{sv}(\widehat J_u)}
\]

es invariante bajo cambios ortonormales independientes de marco. Cuando \(\operatorname{rank}J_u=1\), existe un único valor singular \(\kappa_{\mathcal U}(u)\), candidato legítimo a superconstante de acoplamiento jerárquico.

## 6. Positividad

La métrica acoplada permanece definida positiva si

\[
|\chi|\,\|\widehat J_u\|_{\mathrm{op}}<1.
\]

Por tanto, una superconstante no puede introducirse como número libre: debe respetar positividad y covariancia.

## 7. Resultado

\[
\boxed{\text{objeto total}\neq\text{proyección observada}\neq\text{estado de acoplamiento}.}
\]

La UMI es el objeto total; las geometrías mayor y menor son sus proyecciones; latencia y actualización son estados del bloque correlacional.
