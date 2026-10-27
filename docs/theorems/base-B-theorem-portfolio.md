# RGΦ — Portfolio de teoremas base-B v1.0

## 0. Definiciones

Sea un entero:

\[
B\ge2.
\]

Definimos:

\[
T_B(x)=\{Bx\},
\qquad
C(x)=x^{-1}-1,
\qquad
H(x)=\frac1{1+x},
\]


y, en el dominio donde se usa la rama conjugada,

\[
S_B=H\circ T_B\circ C.
\]

Para un racional reducido:

\[
x=\frac ab,
\qquad 0<a<b,
\]

la altura portal es:

\[
q(x)=\frac{b}{b-a}.
\]

---

# Teorema 1 — Conjugación radix–Möbius en base entera

Para todo `B≥2`:

\[
\boxed{S_B=H\circ T_B\circ H^{-1}.}
\]

En una rama con:

\[
d=\left\lfloor B\frac{b-a}{a}\right\rfloor,
\]

se tiene:

\[
\boxed{
S_B\left(\frac ab\right)
=
\frac{a}{Bb-(B-1+d)a}.
}
\]

### Prueba

Como:

\[
C(a/b)=\frac{b-a}{a},
\]

entonces:

\[
T_B(C(a/b))
=
\frac{B(b-a)-da}{a}.
\]

Aplicando `H`:

\[
H\left(\frac{B(b-a)-da}{a}\right)
=
\frac{a}{a+B(b-a)-da}
=
\frac{a}{Bb-(B-1+d)a}.
\]

---

# Teorema 2 — Familia exacta de semillas

Sean:

\[
N\ge2,
\qquad
1\le r<N,
\qquad
x_{N,r}=\frac{N}{N+r}.
\]

Sea:

\[
s\equiv Br\pmod N,
\qquad
0\le s<N.
\]

Entonces:

\[
\boxed{
S_B(x_{N,r})=\frac{N}{N+s}.
}
\]

### Prueba

\[
C(x_{N,r})=\frac rN.
\]

Como:

\[
T_B(r/N)=s/N,
\]

se obtiene:

\[
H(s/N)=\frac{N}{N+s}.
\]

### Corolario RGΦ

Para:

\[
B=10,
\quad N=17,
\quad r=2,
\]

se tiene:

\[
s=20\bmod17=3,
\]

por lo que:

\[
\frac{17}{19}\mapsto\frac{17}{20}.
\]

El ejemplo fundacional es un miembro de una familia aritmética, no un caso aislado.

---

# Teorema 3 — Matrices de rama y determinante

Las ramas enteras están representadas por:

\[
M_{T_B}(d)=
\begin{pmatrix}
B&-d\\
0&1
\end{pmatrix},
\]

\[
M_{S_B}(d)=
\begin{pmatrix}
1&0\\
-(B-1+d)&B
\end{pmatrix}.
\]

En ambos casos:

\[
\boxed{\det M=B.}
\]

Este hecho controla todo el transporte prime-wise posterior.

---

# Teorema 4 — Factores de reducción del estado

Para `x=a/b` reducido:

## Rama T

\[
M_T(a,b)=(Ba-db,b).
\]

Luego:

\[
\boxed{g_T=\gcd(B,b).}
\]

## Rama S

\[
M_S(a,b)=\left(a,Bb-(B-1+d)a\right).
\]

Luego:

\[
\boxed{g_S=\gcd(B,a).}
\]

### Consecuencia

La parte del presupuesto radix asignada al estado está determinada por el numerador o denominador visible, dependiendo de la rama.

---

# Teorema 5 — Transporte exacto del defecto Farey

Sea un estado primitivo `v=(a,b)` y una sombra primitiva `c=(p,q)`. Definimos:

\[
\Delta(v,c)=aq-bp.
\]

Sea `M` una rama de determinante `B`. Supongamos:

\[
Mv=g v',
\qquad
Mc=k c',
\]

con `v',c'` primitivos. Entonces:

\[
\boxed{
\Delta(v',c')
=
\frac{B}{gk}\Delta(v,c).
}
\]

### Prueba

\[
\det(Mv,Mc)=\det(M)\det(v,c)=B\Delta(v,c).
\]

Pero:

\[
\det(gv',kc')=gk\Delta(v',c').
\]

Igualando ambos términos se obtiene la fórmula.

---

# Teorema 6 — Ledger prime-wise general

Sea:

\[
h=|\Delta|,
\qquad
h'=|\Delta'|.
\]

Para cada primo `p|B`, definimos:

\[
e_p=v_p(h),
\quad
\beta_p=v_p(B),
\quad
s_p=v_p(g),
\quad
\kappa_p=v_p(k).
\]

Entonces:

\[
\boxed{
e_p'=e_p+\beta_p-s_p-\kappa_p.
}
\]

### Caso squarefree

Si `B` es squarefree, `β_p=1`. Cada primo ejecuta pasos de tipo:

\[
1-s_p-\kappa_p.
\]

Para `B=10=2\cdot5` se recuperan los dos ledgers RGΦ.

### Caso no squarefree

Si `p^α||B`, los pasos pertenecen a:

\[
\alpha-s_p-\kappa_p,
\]

por lo que la generalización correcta no es siempre Motzkin: es un lattice walk de salto acotado por la multiplicidad de `p` en la base.

---

# Teorema 7 — Umbrales portales parametrizados

Definimos:

\[
P_m(B,\kappa)
=
\left\{
 x:\ q(x)>\kappa B^m
\right\},
\qquad \kappa>0.
\]

Y la profundidad:

\[
d_{B,\kappa}(x)
=
\max\{m:q(x)>\kappa B^m\}.
\]

La elección histórica RGΦ es:

\[
B=10,
\qquad
\kappa=11.
\]

Debe tratarse como calibración experimental, no como constante intrínseca.

---

# Teorema 8 — Robustez piecewise-constant en horizonte finito

Fijemos:

- base `B`;
- semilla;
- horizonte `H`;
- nivel `m`.

El conjunto de estados alcanzables hasta `H` es finito. Por tanto el primer hitting time de:

\[
P_m(B,\kappa)
\]

como función de `κ` sólo puede cambiar en los valores críticos:

\[
\boxed{
\kappa=\frac{q(x)}{B^m}
}
\]

para estados alcanzables `x` hasta `H`.

### Consecuencia

La sensibilidad al umbral puede certificarse exactamente mediante un atlas de intervalos, no mediante barridos flotantes arbitrarios.

---

# Teorema 9 — Criterio de trap finito

Sea `F` un conjunto finito de estados no terminales y `Z` un conjunto terminal ya certificado. Supongamos:

1. para todo `x∈F`, todo hijo admisible pertenece a `F∪Z`;
2. `F∩P_m=∅`;
3. ningún estado de `Z` alcanza `P_m`.

Entonces:

\[
\boxed{
V_m(x)=\infty
\quad\forall x\in F.
}
\]

### Prueba

Por inducción, toda trayectoria desde `F` permanece en `F∪Z`. Ningún elemento de ese conjunto pertenece ni conduce a `P_m`.

### Aplicación

`C8` satisface exactamente estas hipótesis para `m=5`.

---

# Teorema 10 — Corte de primera divergencia

Sea un testigo de longitud `L`:

\[
w=w_1\cdots w_L,
\]

con estados:

\[
x_0,x_1,\ldots,x_L.
\]

Para cada tiempo `t` en el que existe una acción alternativa, sea `y_t` el hijo alternativo de `x_t`.

Toda trayectoria distinta de `w` posee un primer tiempo de divergencia único y pertenece a:

\[
\boxed{
\bigcup_t \operatorname{Desc}(y_t).
}
\]

### Consecuencia

La optimalidad global de un testigo puede verificarse mediante una búsqueda unificada sobre el corte de primeras divergencias, deduplicando descendencias compartidas.

---

# Teorema 11 — Insuficiencia del estado visible

En los sectores no puros, el mismo:

\[
(x,h,\text{acción})
\]

puede tener diferentes defectos sucesores según la fase p-ádica del shadow address.

El contraejemplo mínimo RGΦ usa:

\[
x=17/19,
\quad h=1,
\quad T,
\]

con diferentes valores de `t mod 10`, produciendo:

\[
h'\in\{1,2,5,10\}.
\]

Por tanto:

\[
\boxed{
(x,e_2,e_5)
\text{ no es Markov-completo en general.}
}
\]

---

# Teorema 12 — Markovización por coordenada Farey completa

El estado aumentado:

\[
\boxed{
(x,c)
}
\]

con estado racional y sombra primitiva es suficiente para determinar exactamente todas las ramas futuras, reducciones y defectos.

La representación comprimida puede sustituir `c` por coordenadas canónicas:

\[
(h,t)
\]

respecto de un vecino Farey, siempre que se preserve la precisión p-ádica necesaria para divisiones futuras.

---

# Estado del portfolio

| Teorema | Estado |
|---|---|
| 1–6 | demostrado simbólicamente; auditado computacionalmente en base 2–40 |
| 7 | definición canónica propuesta |
| 8 | demostrado para horizonte finito |
| 9 | demostrado; C8 como instancia |
| 10 | demostrado combinatoriamente |
| 11 | demostrado por contraejemplo exacto |
| 12 | demostrado a nivel de dinámica exacta; compresión mínima todavía abierta |

## Auditoría asociada

`rgphi_base_b_audit.py` produjo:

- 193.050 verificaciones exactas de la familia de semillas;
- 1.638 verificaciones de determinante;
- 77.460 verificaciones aleatorias exactas del transporte de defecto;
- 115.811 verificaciones prime-wise.

Resultado:

\[
\boxed{\texttt{PASS}.}
\]
