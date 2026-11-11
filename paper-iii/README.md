# RGΦ Paper III — estado canónico v1.13 (Object Freeze)

Objeto exclusivo: dinámica racional radix–Möbius, subautómatas finitos, SCC, cuencas universales y realizabilidad aritmética.

## Definición canónica

RGΦ es el **sistema proyectivo de reducción de contenido radix–Möbius**:

- estados: rayos primitivos \((p,q)\) con \(0<p<q\);
- generadores: dos familias conjugadas de matrices enteras de determinante \(B\);
- dinámica: matriz de rama seguida de normalización primitiva;
- defecto: contenido gcd eliminado en cada arista;
- objetos finitos: subautómatas invariantes y fuertemente conexos en el cono high.

La formulación proyectivo-entera es exactamente conjugada a \(T_B(x)=\{Bx\}\) y \(S_B=\Phi T_B\Phi^{-1}\).

## Resultados estructurales Round 022

- cociclo matricial/contenido para toda palabra admisible;
- teorema espectral de ciclos;
- discriminante cuadrado obligatorio para todo ciclo racional;
- descomposición finita en tipos abstractos para cada cardinalidad;
- espacios de realización diofánticos explícitos;
- forma elíptica de frontera en coordenadas \((A,C,D)\);
- reducción coprima por pendiente a una ecuación de discriminante cuadrado.

## Status conceptual

`RGPHI_MATHEMATICAL_OBJECT = FROZEN_CANONICAL`.

No hace falta terminar la clasificación para definir el objeto. Lo abierto es la clasificación de sus subobjetos finitos y de sus puntos enteros.

## Canon Round 022

- [Object definition](object/RGPHI_OBJECT_DEFINITION_022.md)
- [Content cocycle](theorems/PROJECTIVE_CONTENT_COCYCLE_022.md)
- [Cycle spectral theorem](theorems/CYCLE_SPECTRAL_THEOREM_022.md)
- [Finite moduli decomposition](theorems/FINITE_MODULI_DECOMPOSITION_022.md)
- [Elliptic boundary normal form](theorems/ELLIPTIC_BOUNDARY_NORMAL_FORM_022.md)
- [Coprime slope reduction](theorems/COPRIME_SLOPE_REDUCTION_022.md)
- [Theorem stack v1.13](PAPER_III_THEOREM_STACK_v1_13.md)
- [Round 022](round-022/)
- [Gate 023](gates/RGPHI_MODULI_CLASSIFICATION_023.md)

## Estado abierto

- enumeración efectiva de puntos relativos-integrales;
- clasificación aritmética completa en cardinalidad cinco;
- unicidad global del countergraph;
- catálogo completo de tipos en cardinalidad seis.
