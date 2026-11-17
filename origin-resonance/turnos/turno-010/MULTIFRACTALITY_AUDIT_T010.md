# Auditoría T010-F — ¿La ley dada ya es multifractal?

La ley

\[
\varepsilon_n=\frac{3}{40}10^{-n}
\]

posee una única razón de escala:

\[
\frac{\varepsilon_{n+1}}{\varepsilon_n}=\frac1{10}.
\]

Por sí sola define una jerarquía monoescalar —y, con una medida compatible, monofractal—, no un espectro multifractal no trivial. La tripolaridad añade tres fases, pero no crea automáticamente varios exponentes locales.

Una multifractalización efectiva requiere, por ejemplo, contracciones y pesos dependientes de rama:

\[
r_\sigma,\quad p_\sigma,\qquad\sigma\in\{-1,0,+1\},
\]

con función de masa definida por

\[
\sum_\sigma p_\sigma^q r_\sigma^{-\tau(q)}=1.
\]

Un endpoint positivo exige \(\tau(q)\) no lineal. La ley actual corresponde al caso degenerado

\[
r_-=r_0=r_+=1/10.
\]

Estado:

```text
TRIPOLAR_MICRORANGE = CLOSED
MULTIFRACTALITY = NOT_YET_ESTABLISHED
MULTIFRACTAL_EXTENSION = PREREGISTERED
```
