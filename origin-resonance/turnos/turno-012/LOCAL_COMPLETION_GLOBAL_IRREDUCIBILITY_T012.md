# Teorema T012‑E — Exactitud local y complejidad global

Para toda etiqueta admisible \(h\), la fibra

\[
\mathcal F_h=\{8^tC(K_0\,343^j):j,t\ge0\}
\]

satisface simultáneamente:

1. pertenencia decidible determinísticamente en tiempo polinómico y espacio \(O(|w|)\);
2. no es un lenguaje libre de contexto;
3. su serie generatriz canónica tiene \(|z|=1\) como frontera natural;
4. no es racional, algebraica ni \(D\)-finita;
5. a longitud fija, su inverso exacto requiere únicamente una llave de \(O(\log\ell)\) bits.

Por tanto

\[
\boxed{
\text{inversión condicional pequeña}
\not\Rightarrow
\text{lenguaje global simple}.
}
\]

La UMI‑FST tiene dos escalas de complejidad:

- **global**: frontera natural y no libertad de contexto;
- **local/condicionada**: rango finito y llave logarítmica.

El hiperacceso no comprime toda la palabra ni trivializa la fibra. Completa una observación que ya contiene la etiqueta primitiva, la longitud y el dominio admitido.