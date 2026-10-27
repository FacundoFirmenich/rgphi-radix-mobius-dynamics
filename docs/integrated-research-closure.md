# RGΦ — Superdocumento Integrado de Cierre v1.0

**Fecha de canonización:** 27 de octubre de 2026  
**Estado:** cierre integral de fase; benchmark global \(\tau_5\) aún abierto  
**Decisión estratégica:** se congela la serialización de gates padre-a-padre.  
**Último resultado incorporado:** RGΦ-070τ, trap finito no terminal \(C_8\) y \(V_5(7/260)=\infty\).

---

## 0. Tesis ejecutiva

RGΦ ya no debe entenderse como una larga búsqueda para decidir un único tiempo de portal. Es un programa matemático-computacional sobre una dinámica racional no conmutativa en la que confluyen cinco estructuras:

1. **radix decimal y modularidad:** multiplicación por 10 sobre residuos racionales;
2. **conjugación Möbius/Fibonacci:** el operador complementario \(S\) es conjugado de \(T\) por una carta cuya matriz satisface la ecuación áurea;
3. **geometría de Farey:** vecinos unimodulares, defectos y sombras racionales;
4. **control 10-ádico y presupuestos 2/5-ádicos:** la fase oculta decide controles localmente indistinguibles desde el estado visible;
5. **extremos Bellman y traps finitos:** portales cercanos a uno, precursores latentes, componentes recurrentes y basins de no escape.

La observación inicial

\[
\frac{17}{19}\longrightarrow\frac{17}{20}
\]

no conduce a una correlación de dígitos con \(\phi\). Conduce a una **conjugación operatorial exacta** entre una transición decimal escondida

\[
\frac{2}{17}\xrightarrow{T_{10}}\frac{3}{17}
\]

y una transformación Möbius gobernada espectralmente por la matriz Fibonacci.

El benchmark de portales reveló después que:

- los extremos óptimos no forman una cadena anidada;
- la altura instantánea no es una función de valor;
- el control depende de coordenadas ocultas Farey/10-ádicas;
- los contextos de reducción son ortomodulares y 2/5-ádicos;
- existen tanto geodésicas transitorias de gran complejidad como traps finitos exactos.

El resultado \(C_8\) reconfigura la fase final porque muestra que algunas ramas no requieren una búsqueda hasta un horizonte: pueden cerrarse **para siempre** mediante una clasificación modular de traps. El programa correcto de cierre ya no es retroceder un padre por gate, sino construir simultáneamente:

\[
\boxed{
\text{atlas de traps y basins}
\;+
\text{corte global de primera divergencia}
\;+
\text{búsqueda compartida de los residuos bulk}
}
\]

sobre el testigo actual de 212 acciones.

---

# PARTE I — CENTRUM MATEMÁTICO

## 1. La identidad fundacional

Definimos

\[
C(x)=\frac1x-1,
\qquad
H(x)=C^{-1}(x)=\frac1{1+x},
\]

y el desplazamiento decimal

\[
T(x)=\{10x\}.
\]

Entonces

\[
C\!\left(\frac{17}{19}\right)=\frac2{17},
\qquad
C\!\left(\frac{17}{20}\right)=\frac3{17},
\]

y

\[
T\!\left(\frac2{17}\right)
=\left\{\frac{20}{17}\right\}
=\frac3{17}.
\]

Por tanto:

\[
\boxed{
C(17/20)=T(C(17/19)).
}
\]

Aplicando \(H\):

\[
\boxed{
S:=H\circ T\circ C,
\qquad
S(17/19)=17/20.
}
\]

Éste es el puente exacto original. No es una semejanza visual entre expansiones; es una identidad de conjugación.

## 2. La componente áurea legítima

La carta

\[
H(x)=\frac1{1+x}
\]

está representada proyectivamente por

\[
Q=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}.
\]

Cumple

\[
\boxed{Q^2=Q+I},
\]

con autovalores

\[
\phi=\frac{1+\sqrt5}{2},
\qquad
-\phi^{-1}.
\]

La relación con el número áureo es, por tanto:

\[
\boxed{
\text{espectral, Möbius, Fibonacci y de control};
}
\]

no una afirmación de correlación entre los dígitos de \(\phi\) y los de \(1/17\).

## 3. El semigrupo no conmutativo

El segundo generador es

\[
S=H\circ T\circ H^{-1}.
\]

En una rama con dígito \(d\), las matrices enteras son

\[
M_T(d)=
\begin{pmatrix}
10&-d\\
0&1
\end{pmatrix},
\qquad
M_S(d)=
\begin{pmatrix}
1&0\\
-(9+d)&10
\end{pmatrix},
\]

y ambas tienen determinante 10.

En el seed:

\[
T(S(17/19))=\frac12,
\qquad
S(T(17/19))=\frac9{14},
\]

de modo que

\[
\boxed{TS\neq ST.}
\]

El objeto rector del proyecto es el semigrupo

\[
\boxed{
\mathcal S_{10}=\langle T,S\rangle
}
\]

sobre racionales primitivos, enriquecido con coordenadas Farey, fases 10-ádicas y presupuestos 2/5-ádicos.

## 4. Resolución complementaria en base cinco

En el denominador 17:

\[
\operatorname{ord}_{17}(5)=16,
\qquad
\operatorname{ord}_{17}(2)=8,
\]

y

\[
10\equiv5^7\pmod{17}.
\]

Por ello, sobre esa órbita:

\[
\boxed{T_{10}=T_5^7.}
\]

Además:

\[
\boxed{
T_{10}(2/17)
=\frac{1-2/17}{5}
=T_5^7(2/17)
=\frac3{17}.
}
\]

Esto une la transición decimal, la complementariedad por cinco y la fase modular. La línea 2/5-ádica posterior no es una capa añadida artificialmente: ya está codificada en el seed.

---

# PARTE II — LÍNEA ARITMÉTICA Y MODULAR

## 5. Órbitas, períodos y línea Artin/Kummer

La línea inicial identificó denominadores y pares primos para los que la multiplicación por 10 posee órdenes máximos o casi máximos. En el canon histórico consta:

- un censo exacto de **869.982** puentes bimáximos hasta \(10^9\);
- una densidad observada cercana a \(0,2540461\);
- una constante conjectural cercana a \(0,2538860\);
- una formulación producto de tipo Artin/Kummer.

Estado correcto:

\[
\boxed{
\text{PASS computacional; OPEN analítico-asintótico.}
}
\]

Esta rama no debe supeditarse a \(\tau_5\). Constituye un programa aritmético propio.

## 6. Por qué la línea modular vuelve al centrum con \(C_8\)

El último resultado muestra que la multiplicación modular no sólo describe el origen de la investigación: describe también traps finitos de la dinámica completa.

El trap no terminal

\[
C_8=
\left\{
\frac1{13},\frac3{13},\frac4{13},
\frac5{11},\frac6{11},
\frac9{13},\frac{10}{13},\frac{12}{13}
\right\}
\]

contiene dos órbitas exactas de \(T\):

### Ciclo módulo 13

Como

\[
\operatorname{ord}_{13}(10)=6,
\]

obtenemos

\[
\frac1{13}
\xrightarrow{T}
\frac{10}{13}
\xrightarrow{T}
\frac9{13}
\xrightarrow{T}
\frac{12}{13}
\xrightarrow{T}
\frac3{13}
\xrightarrow{T}
\frac4{13}
\xrightarrow{T}
\frac1{13}.
\]

### Ciclo módulo 11

Como

\[
10\equiv-1\pmod{11},
\]

se tiene

\[
\frac5{11}\xleftrightarrow{T}\frac6{11}.
\]

### Acoplamiento por \(S\)

La rama conjugada añade:

\[
S(9/13)=9/13,
\qquad
S(12/13)=6/11,
\]

y las demás ramas \(S\) son inadmisibles o desembocan en componentes terminales previamente certificados:

\[
S(10/13)=1,
\qquad
S(6/11)=3/4.
\]

Así, \(C_8\) es un **kernel de trap no terminal**: todo sucesor no terminal permanece en \(C_8\); cualquier otro sucesor cae en el conjunto terminal cerrado.

Éste es el nuevo punto de unión:

\[
\boxed{
\text{órdenes multiplicativos}
\to
\text{ciclos }T
\to
\text{acoplamientos }S
\to
\text{traps Bellman finitos}.
}
\]

---

# PARTE III — PORTALES Y BELLMAN

## 7. Definición de altura y portales

Para

\[
x=\frac ab<1,
\]

definimos

\[
q(x)=\frac1{1-x}=\frac{b}{b-a}.
\]

Los portales binarios son

\[
\boxed{
P_m=\{x:q(x)>11\cdot10^m\}.
}
\]

El tiempo global de primera entrada es

\[
\tau_m=\min\{n:\exists w, |w|=n,\;w(17/19)\in P_m\}.
\]

## 8. Primeros tiempos exactos

Los tiempos globales cerrados son:

\[
\boxed{
\tau_1=45,
\quad
\tau_2=85,
\quad
\tau_3=120,
\quad
\tau_4=162.
}
\]

Los primeros estados incluyen:

- \(m=1\): \(128/129\);
- \(m=2\): \(1202/1203\);
- \(m=3\): \(11156/11157,11532/11533,11642/11643\);
- \(m=4\): dos óptimos globales, uno puro y otro con excursiones 2-ádicas.

## 9. Teorema de no anidación

Los portales globalmente más tempranos no forman una cadena de continuaciones óptimas.

Ejemplos exactos:

\[
128/129@45
\xrightarrow{\text{mejor continuación}}
P_2@87,
\qquad
\tau_2=85;
\]

\[
1202/1203@85
\xrightarrow{\text{mejor continuación}}
P_3@139,
\qquad
\tau_3=120;
\]

\[
11156/11157@120
\xrightarrow{\text{mejor continuación}}
P_4@168,
\qquad
\tau_4=162.
\]

Por tanto:

\[
\boxed{
\text{la optimalidad portal no tiene subestructura escalar anidada}.
}
\]

## 10. Inversión por precursores latentes

A igual tiempo, un estado con altura diminuta puede poseer valor futuro muy superior a un portal visible.

Se observaron contrastes exactos donde:

- una altura \(27,57\) veces menor gana el siguiente portal;
- una altura aproximadamente \(472\) veces menor gana el siguiente nivel;
- una altura más de \(5.400\) veces menor llega antes al portal profundo.

Así:

\[
\boxed{q(x)\text{ no es una función de valor Bellman}.}
\]

Tampoco basta maximizar la mejor altura a uno, ocho o diez pasos: el ganador local conocido puede quedar casi al final del ranking de lookahead.

## 11. Estado Bellman correcto

El estado dinámico visible \(a/b\) es Markoviano para la evolución racional, pero el valor futuro contextual exige información adicional:

\[
\boxed{
\left(
\frac ab,
\text{fase radix},
\text{sombra Farey},
 e_2,e_5,
\text{contexto ortomodular}
\right).
}
\]

No siempre se necesita materializar todo ese vector. La arquitectura final distingue:

- estado racional base;
- ideal inferior de presupuestos \((e_2,e_5)\);
- antichain de máximos;
- excepciones dispersas de fase.

---

# PARTE IV — LA GEOMETRÍA LOCAL HACIA \(P_5\)

## 12. El viejo testigo 217: válido localmente, supersedido globalmente

El primer testigo profundo conocido llegaba en 217 acciones a

\[
\frac{1257793}{1257794}.
\]

Quedaron demostrados localmente:

- el valor exacto de 55 acciones desde \(124852/124853@162\);
- un prefijo de cone-renewal único `TSSTS`;
- un bulk de 50 acciones;
- una geodésica local completa única;
- un reset final por la cúspide \(10/13\).

Estos resultados siguen siendo correctos como teoremas locales. Lo que quedó refutado fue su interpretación como óptimo global.

## 13. Destrucción y recreación de profundidad

Desde el portal \(m=4\), la geodésica mínima antigua comienza con ramas que multiplican el defecto

\[
\delta=b-a
\]

por diez:

\[
1\to10\to100\to1000\to10000,
\]

mientras la profundidad cae:

\[
4\to3\to2\to1\to0.
\]

Luego la órbita viaja por el bulk y, desde un vecino de Farey de \(10/13\), una última acción produce

\[
\frac{a}{a+1},
\]

restaurando defecto uno y cruzando todos los umbrales a la vez.

La forma estructural es:

\[
\boxed{
\text{desenrollado radix}
\to
\text{transporte bulk}
\to
\text{reset Farey}.
}
\]

## 14. Cone transducer

En el cono \(q>11\), las ramas activas satisfacen

\[
q(Tx)=\frac{q(x)}{10},
\qquad
q(Sx)=\frac{q(x)+9}{10}.
\]

Por tanto ninguna ruta puede profundizar un portal mientras permanece dentro del cono: toda renovación profunda exige salir al bulk.

Para los portales \(m=4\) estudiados, la salida ocurre exactamente después de cinco acciones, generando 32 estados bulk. En el viejo testigo, el único código minimizador fue `TSSTS`.

---

# PARTE V — SOMBRAS FAREY Y CONTROL 10-ÁDICO

## 15. Sombra como coordenada de control

Sea \(v=(a,b)\) el estado y \(c=(p,q)\) una sombra con defecto

\[
\Delta=aq-bp.
\]

Cada matriz de rama tiene determinante 10. Si la reducción del estado es \(g\) y la de la sombra es \(k\), entonces

\[
\boxed{
\Delta'=\frac{10}{gk}\Delta.
}
\]

Para el testigo antiguo puro de 217 acciones, cada paso tenía

\[
(g,k)=(1,10),
\qquad
\Delta=-1.
\]

La palabra completa podía reconstruirse desde la sombra inicial sin BFS, eligiendo la rama con cancelación cuspidal máxima.

## 16. Compilador Farey–Bellman general

El testigo mejorado de 212 acciones introdujo una ley más general:

\[
\boxed{
\text{maximizar primero }gk,
\quad
\text{después maximizar }k.
}
\]

Este compilador reconstruye exactamente tanto el testigo de 212 como el de 217.

En el testigo 212:

- 210 pasos usan \((1,10)\);
- uno usa \((1,5)\);
- uno usa \((2,10)\);
- esos dos pasos forman una excursión 2-ádica \(1\to2\to1\) en el defecto.

## 17. Un solo dígito oculto cambia 217 por 212

Los parámetros 10-ádicos de los testigos 212 y 217 coinciden módulo

\[
10^{146},
\]

pero no módulo

\[
10^{147}.
\]

Sus cifras 147 son:

\[
\boxed{
 d_{147}(t_{212})=9,
\qquad
 d_{147}(t_{217})=8.
}
\]

Ambos llegan al mismo estado visible tras 146 controles, pero el dígito oculto cambia la acción siguiente y reduce el tiempo total en cinco pasos.

Conclusión:

\[
\boxed{
\text{el control no es función del racional visible solamente}.
}
\]

---

# PARTE VI — ORTOMODULARIDAD Y COMPLEMENTARIEDAD 2/5

## 18. La diada complementaria exacta

Para cada primo \(p\in\{2,5\}\), sean

\[
e_p=v_p(h),
\quad
s_p=v_p(g),
\quad
\kappa_p=v_p(k).
\]

La actualización es

\[
\boxed{
e_p'=e_p+1-s_p-\kappa_p.
}
\]

Cada presupuesto realiza un paso de Motzkin:

\[
\sigma_p\in\{-1,0,+1\}.
\]

El ortocomplemento

\[
(s_p,\kappa_p)^\perp=(1-s_p,1-\kappa_p)
\]

invierte el flujo:

\[
\sigma_p^\perp=-\sigma_p.
\]

Los cuatro modos globales balanceados básicos son

\[
(1,10),(2,5),(5,2),(10,1),
\]

con

\[
(g,k)^\perp=(10/g,10/k).
\]

## 19. Por qué \((a/b,e_2,e_5)\) no basta

En el mismo estado \(17/19\), con el mismo defecto inicial y la misma acción \(T\), distintas fases de \(t\bmod10\) producen defectos siguientes

\[
1,2,5,10.
\]

Luego el estado no puro necesita también fase bi-ádica lazy:

\[
\boxed{
(a/b,e_2,e_5,\mathcal C_2,\mathcal C_5).
}
\]

## 20. Compresión por ideales y antichains

Expandir todos los contextos no reduce el grafo racional: su proyección recupera exactamente todas las trayectorias \(T/S\).

En profundidad 40 se observaron:

- 894 estados racionales;
- 1.556.255 contextos explícitos;
- 1.489.218 pares estado-presupuesto;
- ideales inferiores en \(\mathbb N^2\) para todos los estados;
- anchura máxima de antichain 2;
- 929 puntos maximales totales;
- sólo 1,8024% de pares con excepciones de fase.

La representación correcta es:

\[
\boxed{
\text{racional}
+
\text{antichain presupuestaria}
+
\text{excepciones dispersas de fase}.
}
\]

La ortomodularidad no es una poda mágica: es la semántica que impide eliminar complementos incompatibles mediante un ranking distributivo falso.

---

# PARTE VII — EL TESTIGO 212 Y EL ESTADO GLOBAL

## 21. Corrección del objetivo

El objetivo histórico \(\tau_5=217\) quedó refutado cuando apareció un word exacto de longitud 212 que alcanza

\[
\boxed{
\frac{1350416}{1350417}
}
\]

con altura

\[
1.350.417.
\]

El intervalo global vigente es

\[
\boxed{
179\le\tau_5\le212.
}
\]

## 22. Escalera Bellman exacta actual

Tras RGΦ-070τ se ha demostrado

\[
\boxed{
V_5(x_t)=212-t,
\qquad
89\le t\le212.
}
\]

Son 124 estados consecutivos con valor exacto.

En términos de primera divergencia:

\[
\boxed{
\text{todo testigo }<212
\text{ debe separarse de la trayectoria actual en la acción 89 o antes}.
}
\]

## 23. Por qué la serialización se congela

Retroceder un estado por vez ha producido certificados válidos, pero no ha movido el intervalo global. Varias búsquedas procesaron miles de millones de estados cada una para desplazar un solo corte Bellman.

Continuar hasta la semilla podría exigir decenas de gates adicionales y recomputar repetidamente regiones descendientes solapadas.

Decisión canónica:

\[
\boxed{
\text{no se ejecuta RGΦ-071τ como siguiente padre serial}.
}
\]

---

# PARTE VIII — RGΦ-070τ Y LA RECONFIGURACIÓN POR \(C_8\)

## 24. Resultado exacto

La rama competidora

\[
\frac{1307}{2600}
\xrightarrow{T_5}
\frac7{260}@90
\]

entra, a tiempo global 97, en el trap finito \(C_8\).

Como todo sucesor no terminal permanece en \(C_8\), todo otro sucesor entra en componentes terminales ya cerrados y

\[
\max_{x\in C_8}q(x)=13,
\]

se concluye:

\[
\boxed{
V_5(7/260)=\infty.
}
\]

No es un `NO_HIT` de horizonte finito. Es un no-hit para todo tiempo.

Por Bellman:

\[
\boxed{
V_5(1307/2600)=123.
}
\]

## 25. Por qué es mucho más fuerte de lo que parecía

### 25.1 Sustituye cómputo temporal por estructura

Las ramas anteriores se cerraban explorando hasta 211. Aquí el horizonte desaparece: la invariancia del trap cierra el futuro completo.

### 25.2 Reintegra la línea modular

El trap está construido por órbitas de multiplicación por 10 módulo 13 y módulo 11. La línea de órdenes multiplicativos vuelve a ser central para clasificar la dinámica global.

### 25.3 Introduce un nuevo tipo de objeto canónico

Hasta ahora distinguíamos:

- terminales;
- rutas bulk;
- portales;
- sombras geodésicas.

Ahora debemos añadir:

\[
\boxed{
\text{trap finito no terminal con basín alcanzable}.
}
\]

### 25.4 Sugiere un teorema de clasificación

Los traps finitos parecen ser uniones de:

1. ciclos \(T\) dados por órdenes multiplicativos de 10;
2. enlaces \(S\) entre dichos ciclos;
3. salidas únicamente hacia componentes terminales ya certificados.

Esto abre una vía estructural para cerrar muchas primeras divergencias sin BFS masiva.

---

# PARTE IX — REGISTRO CANÓNICO DE RESULTADOS

## 26. Resultados cerrados

### Exactos simbólicos

1. Puente \(C(17/20)=T(C(17/19))\).
2. Conjugación \(S=HTH^{-1}\).
3. Ecuación áurea \(Q^2=Q+I\).
4. No conmutatividad \(TS\neq ST\).
5. Resolución base cinco \(T_{10}=T_5^7\) en el denominador 17.
6. Fórmula Farey \(\Delta'=10\Delta/(gk)\).
7. Ley de presupuesto \(e_p'=e_p+1-s_p-\kappa_p\).
8. Trap finito \(C_8\) y no-hit infinito de \(7/260\).

### Exactos computacionales

1. \(\tau_1=45,\tau_2=85,\tau_3=120,\tau_4=162\).
2. No anidación de los portales óptimos.
3. Fallo exacto del greedy por altura.
4. Geodésica local antigua de 55 acciones y word único en su contexto.
5. Compiladores Farey de 217 y 212 acciones.
6. Upper bound global \(\tau_5\le212\).
7. Lower bound global \(\tau_5\ge179\).
8. Escalera Bellman exacta \(89\le t\le212\).
9. Clausuras de ramas alternativas RGΦ-041–070.
10. Compresión ortomodular a antichains en profundidad 40.

## 27. Problemas abiertos legítimos

1. Determinar exactamente \(\tau_5\):
   \[
   179\le\tau_5\le212.
   \]
2. Clasificar todos los traps finitos y sus basins.
3. Probar o refutar que la anchura ortomodular de antichain permanece acotada.
4. Completar la teoría analítica de la densidad Artin/Kummer.
5. Determinar leyes asintóticas de \(\tau_m\) y de los denominadores extremos.
6. Caracterizar cuándo una sombra 10-ádica compila una geodésica global.

## 28. Hipótesis refutadas o supersedidas

| Afirmación | Estado |
|---|---|
| Hay correlación directa de dígitos entre \(\phi\) y \(1/17\) | No sustentada; reemplazada por relación operatorial/espectral |
| El hub \(39/59\) es obligatorio | Refutada por bypasses exactos |
| Todos los portales tienen defecto \(h=1\) | Refutada por familia superficial \(h=2\) |
| Los óptimos portal forman una cadena | Refutada exactamente |
| Maximizar \(q\) es Bellman-óptimo | Refutada exactamente |
| \(\tau_5=217\) | Refutada por testigo 212 |
| El control depende sólo del racional visible | Refutada por flip 10-ádico |
| \((a/b,e_2,e_5)\) es Markov-completo | Refutada; falta fase bi-ádica |
| Expandir todos los contextos ortomodulares reduce el grafo | Refutada; proyecta al grafo racional completo |
| Un gate serial por padre es la ruta de cierre adecuada | Refutada operacionalmente |

---

# PARTE X — NUEVO CENTRUM UNIFICADO

## 29. Arquitectura en seis capas

### Capa A — Esqueleto modular

\[
T:a/b\mapsto (10a\bmod b)/b.
\]

Los órdenes multiplicativos determinan ciclos y períodos.

### Capa B — Acoplamiento Möbius-áureo

\[
S=HTH^{-1},
\qquad
Q^2=Q+I.
\]

Conecta órbitas, introduce ramas conjugadas y genera puentes entre denominadores.

### Capa C — Geometría Farey

Vecinos unimodulares, defectos \(\Delta\), reducciones \(g,k\) y cusps de reset.

### Capa D — Dirección 10-ádica y presupuestos 2/5

La fase oculta selecciona controles y administra creación/aniquilación de defectos.

### Capa E — Valor Bellman y portales

Los portales son extremos observables; los precursores latentes almacenan valor futuro no visible en \(q\).

### Capa F — Traps, basins y escape

La dinámica global se divide entre:

- basins de traps finitos;
- componentes terminales;
- transientes bulk;
- rutas geodésicas hacia portales.

Éste es el centrum final de RGΦ.

---

# PARTE XI — PROGRAMA DE CIERRE Y COMPLETITUD

## 30. Decisión: congelar la cinta de gates

Se mantienen como evidencia todos los certificados RGΦ-041–070, pero dejan de ser la unidad de diseño científico.

Los nuevos identificadores deben ser teoremas y datasets, no números de gate.

## 31. Macro-gate I — Atlas de traps y basins

Objetivo:

1. enumerar ciclos \(T\) por denominador y orden multiplicativo;
2. añadir todos los enlaces \(S\) admisibles;
3. calcular SCCs y traps forward-invariant;
4. probar cota de altura de cada trap;
5. construir basins exactos para fuentes de primera divergencia.

Salida:

\[
\boxed{
\text{Trap Atlas RGΦ}
}
\]

con \(C_8\) como primer teorema no trivial.

## 32. Macro-gate II — Corte global de primera divergencia

Sea \(w_{212}\) el testigo actual. Para cada tiempo \(t\le88\) con acción alternativa admisible, se define la fuente de primera divergencia \(y_t\).

Toda ruta más rápida tiene una primera divergencia única, luego pertenece a

\[
\bigcup_{t=0}^{88}\operatorname{Desc}(y_t).
\]

En vez de 89 BFS independientes:

1. se inyectan todas las fuentes en su tiempo global;
2. se propaga la unión;
3. se deduplican estados compartidos por capa;
4. se separan inmediatamente los basins de traps;
5. se conserva provenance sólo para auditoría;
6. se testea \(P_5\) antes de podar;
7. se detiene en 211.

Resultado binario:

- `NO_HIT`: \(\boxed{\tau_5=212}\);
- `HIT`: nuevo testigo exacto \(<212\).

## 33. Macro-gate III — Búsqueda inversa desde el portal

Complementariamente:

1. caracterizar preimágenes racionales de estados de defecto pequeño;
2. construir conos inversos de cusps de reset;
3. realizar meet-in-the-middle con el corte de primera divergencia;
4. usar la fase 10-ádica para comprimir familias de preimágenes.

## 34. Criterio de cierre de \(\tau_5\)

La línea de benchmark se considera cerrada cuando ocurra una de dos cosas:

\[
\boxed{
\tau_5=212
}
\]

mediante ausencia global de hit hasta 211, o aparece un nuevo testigo y se repite **una sola vez** el corte global respecto del nuevo campeón.

No se vuelve a una serialización padre-a-padre.

## 35. Cierre científico aunque \(\tau_5\) permanezca abierto

El programa RGΦ ya posee suficiente contenido para una publicación modular incluso si el intervalo \([179,212]\) no se reduce inmediatamente.

El cierre científico exige:

1. canonizar teoremas y fronteras de evidencia;
2. etiquetar legacy/superseded;
3. publicar códigos y hashes;
4. separar con precisión resultados simbólicos, computacionales y conjecturales;
5. formular el benchmark abierto como problema delimitado, no como déficit de toda la teoría.

---

# PARTE XII — PAQUETE DE PUBLICACIÓN

## 36. Paper I — Radix–Möbius–Golden Bridge

Contenido:

- identidad \(2/17\to3/17\);
- carta \(H\) y matriz Fibonacci;
- no conmutatividad;
- resolución base cinco;
- órbitas modulares;
- demarcación frente a correlaciones de dígitos.

## 37. Paper II — Nonnested Portal Dynamics

Contenido:

- definición de \(P_m\);
- \(\tau_1,\ldots,\tau_4\);
- no anidación;
- precursores latentes;
- fallo de la altura y de lookaheads cortos;
- estructura Bellman correcta;
- estado abierto de \(\tau_5\).

## 38. Paper III — Farey Shadows and 10-adic Control

Contenido:

- compiladores 217 y 212;
- flip de una cifra 10-ádica;
- geodésicas locales;
- cone/bulk/reset;
- cusps de reset.

## 39. Paper IV — Orthomodular 2/5-adic Context Semantics

Contenido:

- diadas complementarias;
- ley Motzkin;
- fases lazy;
- ideales inferiores;
- antichain compression;
- condiciones válidas de poda.

## 40. Paper V — Finite Traps and Portal Escape

El nuevo paper habilitado por RGΦ-070:

- ciclos multiplicativos de \(T\);
- enlaces conjugados de \(S\);
- clasificación de traps;
- basins;
- \(C_8\) como caso exacto;
- aplicación al cierre global de primera divergencia.

## 41. Monografía integrada

Título provisional:

> **Radix–Möbius–Farey Dynamics: Golden Conjugacy, Hidden 10-adic Control, Orthomodular Budgets and Extremal Rational Portals**

---

# PARTE XIII — REGISTRO DE EVIDENCIA

## 42. Fuentes canónicas mínimas

- `rgphi019_report.md`: no anidación, splice y bypass.
- `rgphi020_report.md`: inversión por precursores latentes y estado Bellman.
- `rgphi026_report.md`: sombra Farey y decimación 10-ádica del testigo 217.
- `rgphi029_report.md`: ley bi-ádica/Motzkin.
- `rgphi030_report.md`: ideales inferiores y antichain compression.
- `rgphi033_report.md`: compilador 212 y flip de una cifra.
- `rgphi039_report.md`: resolución exacta en base cinco.
- `rgphi041_tau212_report.md`: corrección 217→212 y cota global.
- `rgphi069_report.md`: escalera Bellman hasta tiempo 90.
- `rgphi070_report.md`: trap \(C_8\), no-hit infinito y escalera hasta tiempo 89.

## 43. Convenciones de evidencia

- **SYMBOLIC EXACT:** derivación algebraica verificable a mano.
- **COMPUTATIONAL EXACT:** enumeración finita exacta, aritmética entera, hashes y cross-checks.
- **CONJECTURAL:** evidencia finita o heurística sin teorema global.
- **LEGACY VALID:** resultado correcto localmente, supersedido como frontera global.
- **REFUTED:** existe contraejemplo exacto.

---

# PARTE XIV — DICTAMEN DE CIERRE DE FASE

## 44. Qué está cerrado

Está cerrado el núcleo teórico que conecta:

\[
\boxed{
\text{radix}
\leftrightarrow
\text{Möbius áureo}
\leftrightarrow
\text{Farey}
\leftrightarrow
\text{10-ádico}
\leftrightarrow
\text{ortomodular}
\leftrightarrow
\text{Bellman}
}
\]

con ejemplos exactos, teoremas locales y certificados computacionales de gran escala.

Está cerrado que:

- la correlación legítima no es digitológica;
- la dinámica es no conmutativa;
- los portales no son anidados;
- la altura no es Bellman;
- el control puede depender de una fase oculta;
- los contextos complementarios son 2/5-ádicos;
- existen traps finitos exactos;
- el testigo 212 domina al de 217;
- la trayectoria 212 es localmente exacta desde tiempo 89.

## 45. Qué no está cerrado

No está probado todavía:

\[
\tau_5=212.
\]

Tampoco están cerradas:

- la clasificación completa de traps;
- la densidad analítica Artin/Kummer;
- la asintótica de \(\tau_m\);
- la completitud global del compilador Farey–Bellman.

## 46. Conclusión sustantiva

El último resultado no es un pequeño paso adicional. Devuelve la investigación a su origen modular, pero a un nivel superior:

- empezamos con períodos de \(1/17\);
- pasamos por Möbius, Farey y portales;
- descubrimos control 10-ádico y ortomodular;
- y regresamos a ciclos modulares como constituyentes de traps finitos que deciden valores Bellman infinitos.

La línea describe ahora dos geometrías complementarias:

\[
\boxed{
\text{geodésicas de escape a extremos}
\quad\text{versus}\quad
\text{basins de traps modulares finitos}.
}
\]

Ése es el nuevo centrum.

El cierre legítimo del benchmark no será una sucesión indefinida de gates, sino una clasificación conjunta de todas las primeras divergencias en:

\[
\boxed{
\text{trap}
\;\cup\;
\text{terminal}
\;\cup\;
\text{bulk residual compartido}.
}
\]

Y el cierre científico global de RGΦ ya puede organizarse, escribirse y publicarse con independencia de que el último intervalo \([179,212]\) tarde más en resolverse.

---

## 47. Estado canónico final de esta fase

\[
\boxed{
\begin{aligned}
&\tau_1=45,\quad \tau_2=85,\quad \tau_3=120,\quad \tau_4=162,\\
&179\le\tau_5\le212,\\
&x_{212}=1350416/1350417,\\
&V_5(x_t)=212-t\quad(89\le t\le212),\\
&V_5(7/260)=\infty,\\
&C_8=\{1/13,3/13,4/13,5/11,6/11,9/13,10/13,12/13\}.
\end{aligned}
}
\]

**Próxima acción autorizable, pero no ejecutada en esta fase:** `RGΦ–GLOBAL–TRAP–CUT–088`, macro-gate conjunto de atlas de traps + corte global de primera divergencia.

