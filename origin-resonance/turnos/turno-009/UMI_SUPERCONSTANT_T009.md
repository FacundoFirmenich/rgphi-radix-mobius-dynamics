# Teorema-marco T009-D — Superconstante de acoplamiento jerárquico

## 1. Operador antes que número

La UMI no debe recibir inicialmente una constante escalar. El objeto primario es el operador interplano

\[
J_u:T_uX_m\to T_uX_M.
\]

Su forma adimensional es

\[
\widehat J_u=g_M^{-1/2}J_ug_m^{-1/2}.
\]

## 2. Invariancia

Bajo cambios de frames ortonormales \(Q_M,Q_m\),

\[
\widehat J_u'=Q_M\widehat J_uQ_m^T.
\]

Por tanto, sus valores singulares son invariantes. Definimos la superconstante completa como

\[
\boxed{\boldsymbol\kappa_{\mathcal U}(u)=\operatorname{sv}(\widehat J_u).}
\]

Sólo en rango uno se reduce legítimamente a un escalar \(\kappa_{\mathcal U}(u)\).

## 3. Latencia y efectivización

Introducimos un selector correlacional

\[
\chi_{\mathcal O}(u)\in\{0,1\}.
\]

El acoplamiento efectivo es

\[
\boxed{\boldsymbol\kappa_{\mathrm{eff}}=\chi_{\mathcal O}(u)\boldsymbol\kappa_{\mathcal U}(u).}
\]

- \(\chi=0\): la UMI existe, pero permanece latente para ese observador;
- \(\chi=1\): la correlación se efectiviza.

La diferencia entre observadores no modifica la UMI; modifica qué correlación se vuelve observable.

## 4. Transición de fase

La actualización es una transición de fase en sentido algebraico:

\[
\operatorname{rank}G_{\mathrm{mixed}}:0\longrightarrow\operatorname{rank}J_u.
\]

Para convertirla en transición física o termodinámica habría que aportar parámetro de control, límite, no-analyticidad y observable experimental. Eso permanece abierto.

## 5. Jerarquía

Para una torre \(X_0\hookrightarrow\cdots\hookrightarrow X_n\), la UMI generalizada porta operadores \(J_{i+1,i}\). La superconstante jerárquica es el sistema compatible

\[
\boxed{\boldsymbol\kappa_{\mathrm{hier}}=\{\operatorname{sv}(\widehat J_{i+1,i})\}_{i=0}^{n-1},}
\]

no necesariamente un único número universal.
