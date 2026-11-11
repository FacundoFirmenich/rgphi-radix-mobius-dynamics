# RGΦ Round 022-C — descomposición finita en tipos diofánticos

## Tipo abstracto

Un tipo RGΦ de cardinalidad \(n\) consiste en un conjunto \(V=\{1,\ldots,n\}\), dos endomapas \(\tau,\sigma:V\to V\) y factores de defecto \(g_i,h_i\ge1\).

Una realización en base \(B\) añade estados primitivos \(v_i=(p_i,q_i)\) y dígitos de rama \(a_i,b_i\), sujetos a
\[
q_i=g_iq_{\tau(i)},\qquad Bp_i-a_iq_i=g_ip_{\tau(i)},
\]
\[
p_i=h_ip_{\sigma(i)},\qquad B(q_i-p_i)-b_ip_i=h_i(q_{\sigma(i)}-p_{\sigma(i)}),
\]
junto con highness, primitividad, distinción, exactitud de gcd y fuerte conexidad. Estas condiciones definen un conjunto diofántico cuasi-afín explícito.

## Presupuesto de ciclo

Para un ciclo high \(C\), con \(m_T,m_S\) aristas de cada letra y producto total de defectos \(R_C\), multiplicar las razones de numeradores alrededor del ciclo da
\[
R_C=\prod_{T\text{-edges}}\frac{x_{i+1}}{x_i}<2^{m_T}.
\]
El argumento dual con denominadores da \(R_C<2^{m_S}\). Por tanto
\[
\boxed{R_C<2^{\min(m_T,m_S)}.}
\]

## Teorema de finitud de tipos

Toda arista de una SCC de \(n\) estados pertenece a un ciclo simple de longitud a lo sumo \(n\). En consecuencia, cada factor estricto satisface
\[
\boxed{d<2^{\lfloor n/2\rfloor}.}
\]

Como existen finitos pares de endomapas de un conjunto finito y finitas etiquetas de defecto admisibles,
\[
\boxed{\text{para cada }n\text{ existen sólo finitos tipos RGΦ abstractos, independientemente de }B.}
\]

## Fibra de bases

Para una tupla primitiva fija, las ecuaciones locales son congruencias lineales en \(B\). El CRT generalizado implica que la fibra de bases es vacía o una única progresión aritmética completa.

## Arquitectura del programa

La clasificación de cardinalidad fija se separa canónicamente en:

1. combinatoria finita de tipos;
2. aritmética diofántica de sus espacios de realización.
