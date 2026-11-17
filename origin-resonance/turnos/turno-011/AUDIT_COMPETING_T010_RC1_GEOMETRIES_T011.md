# Turno 011 · Auditoría de compatibilidad T010/RC1 (2026-11-17)

**Estado:** INPUT_CONFLICT_OPEN; DO_NOT_PROMOTE. **Autoridad:** sólo la rama prospectiva Origin–Resonance; nunca Paper III main.

## Dos leyes bajo hipótesis distintas

La ley que debe preservarse literalmente durante esta vigilancia es

\[
\lambda_n=(\pi/6)10^{+n_{\mathrm{scalar}}},\qquad
U^{(A)}_{n,\sigma}=(\pi/24)(40\,10^n+3\sigma).
\]

Su semiamplitud es \(\pi/8\), su sombra es \([40\,10^n-3:40\,10^n:40\,10^n+3]\) y su límite proyectivo para \(n\to\infty\) es \([1:1:1]\).

RC1, introducida posteriormente en la rama, propone en cambio

\[
a_B=(2/30)C_n=(\pi/9)10^n,\qquad
U^{(B)}_{n,\sigma}=(\pi/9)10^n(15+\sigma).
\]

Ésta tiene sombra constante \([14:15:16]\) y satisface \(\mathbf U^{(B)}_{n+1}=10\mathbf U^{(B)}_n\). Ambas comparten el centro \(C_n=(5\pi/3)10^n\), pero **no** la amplitud lateral. Se igualan sólo cuando \(10^n=9/8\), fuera de \(n\in\mathbb Z_{\ge0}\). Ninguna identidad matemática demuestra que una de estas **definiciones diferentes** refute la otra. Por eso la afirmación de RC1 de que el geocolapso de A queda «refutado» es válida **únicamente** si se adopta su nueva cota lateral; no puede aplicarse a A sin cambiar la hipótesis. Se conservan ambos documentos y se requiere reconciliación explícita antes de una promoción terminológica.

## Endpoints T011 auditados

- **Medida multifractal concreta:** las cuatro similitudes activas Koch de razón 1/3 y los pesos \(w=(15,14,16,15)/60\) (construcción T011) definen una medida auto-semejante no uniforme. La función \(\tau(q)=-\log(\sum_j w_j^q)/\log3\) tiene \(\tau''(q)=-\operatorname{Var}_{q}(\log w_j)/\log3<0\). Resultado matemático positivo **para esa medida**; los pesos son una elección del modelo RC1, no observaciones empíricas ni consecuencias de la fórmula A. Mantener NO MULTIFRACTAL para la jerarquía monoescalar A por sí sola.
- **Hiperacceso:** seis completitudes globales requieren idealmente \(\log_2 6\) bits de información, pero **tres bits** en longitud binaria fija. \(N\) caras locales independientes requieren \(\lceil N\log_2 6\rceil\) bits fijos. No confundir llave del cociente terminal con reconstrucción de la historia.
- **Biplanar:** para flujo gradiente \(\dot\phi=-2\kappa\sin\phi\), el bloqueo \(\phi=0\) es localmente estable si \(\kappa>0\), dentro del modelo sin retrasos; otras dinámicas siguen abiertas.
- **Incertidumbre:** el modelo \(\mathbb C^6\) con \(SZS=-Z\) y estado saturante es matemáticamente condicional, sin afirmación de cuantización física.
- **Operador «ramanujiano»:** T011 define una sustitución con extremos preservados y cociclo de escala. La regla elemental conserva la cara \(g\) en los cuatro hijos; una secuencia de caras variables \(g_1,\ldots,g_n\) exige definir la actualización de caras antes de atribuir el cociclo \(g_n\cdots g_1\) a una única dinámica. No se ha demostrado relación con identidades históricas de Ramanujan.
- **FST/RC28:** mantener la reclasificación SUPERACCESS (recuperación interna) / HYPERACCESS (llave cualitativa de error cero), RC28 como post hoc y el control independiente de RC28 abierto. En el snapshot 2026-11-17 de sinus-math sólo está versionado el README, no el motor FST-11 ni sus tests anunciados.

El certificado complementario AUDIT_HYPERACCESS_BRANCH_COMPLEXITY_T011 demuestra la cota exacta de fibra \(\lceil\log_2|\mathcal A_N|\rceil\) para la observación exclusiva de extremos. Este control preserva las correcciones históricas y los resultados negativos; no modifica main ni hace afirmaciones físicas.
