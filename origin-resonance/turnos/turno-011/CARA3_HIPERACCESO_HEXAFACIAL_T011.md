# Cara 3 — Hiperacceso hexafacial anidado

Una cara completa es

\[
f=(\varepsilon,\sigma)\in\{M,m\}\times\{-,0,+\}.
\]

Existen seis caras. La complejidad zero-error es

\[
\boxed{\log_2 6=1+\log_2 3,}
\]

compuesta por un bit de plano y un trit de fase.

Si ambas proyecciones manifiestan la misma fase, sólo hay tres completitudes y la llave cuesta `log2(3)` bits.

Una secuencia libre de profundidad `N` posee `6^N` historias y exige `N log2(6)` bits: eso es superacceso.

Si una sola cara gobierna toda la torre, hay únicamente seis completitudes:

\[
(f,f,\ldots,f).
\]

La llave cuesta `log2(6)` bits y

\[
\boxed{\frac{\log_2 6}{N}\to0.}
\]

Para llaves locales `g_1,...,g_N in D3`, la fase total es

\[
\boxed{G_N=g_N\cdots g_1.}
\]

Si el exterior depende sólo de `G_N`, una llave de seis valores sincroniza la completitud sin reconstruir la historia.

Una máscara de cosimultaneidad es `A subset F_6`; existen `2^6=64` máscaras. Una máscara fija para toda la torre cuesta seis bits y tiene tasa `6/N -> 0`.

\[
\boxed{\text{Hiperacceso} \iff \text{llave global sublineal que completa una torre coherente}.}
\]
