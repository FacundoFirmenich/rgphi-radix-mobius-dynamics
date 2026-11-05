# HDH-034 — fully specified P1 modewise consistency theorem

## Authority

`EXPERIMENTAL_ISOLATED`. This theorem strengthens Paper A. It does not modify RGΦ mainline and does not imply a physical spacetime, gravity, or Einstein-equation claim.

## 1. Reference elliptic model

Let

\[
\Omega=(0,L)\times\mathbb T,\qquad \mathbb T=\mathbb R/(2\pi\mathbb Z),
\]

with retained boundary \(\Gamma_0=\{0\}\times\mathbb T\) and fixed boundary \(\Gamma_L=\{L\}\times\mathbb T\). Let \(\kappa>0\). For a periodic deformation field

\[
V\in W^{2,\infty}(\Omega;\mathbb R^2),
\]

vanishing near \(\Gamma_L\), define \(F_\varepsilon=I+\varepsilon V\). Pulling the deformed problem back to \(\Omega\) gives

\[
a_\varepsilon(u,v)=\int_\Omega G_\varepsilon\nabla u\cdot\nabla v+c_\varepsilon uv,
\]

where

\[
G_\varepsilon=J_\varepsilon DF_\varepsilon^{-1}DF_\varepsilon^{-T},\qquad c_\varepsilon=\kappa J_\varepsilon.
\]

At \(\varepsilon=0\),

\[
G'_0=(\nabla\!\cdot V)I-DV-DV^T,\qquad c'_0=\kappa\nabla\!\cdot V.
\]

Hence

\[
B_V(u,v)=\int_\Omega\left(((\nabla\!\cdot V)I-DV-DV^T)\nabla u\cdot\nabla v+\kappa(\nabla\!\cdot V)uv\right).
\]

## 2. Exact-lift P1 scheme

Let \(\psi_j(y)=\pi^{-1/2}\sin(jy)\), so \(\|\psi_j\|_{H^{3/2}(\mathbb T)}=(1+j^2)^{3/4}\). Let \(u_j\) solve \(-\Delta u_j+\kappa u_j=0\), with trace \(\psi_j\) on \(\Gamma_0\), zero trace on \(\Gamma_L\), and periodicity in \(y\). Define \(D_{jk}=B_V(u_j,u_k)\).

On quasiuniform, shape-regular fitted meshes, let \(X_h^0\subset H_0^1(\Omega)\) be the conforming P1 space. Choose a bounded trace right-inverse \(L:H^{3/2}(\Gamma_0)\to H^2(\Omega)\), write \(u_j=L\psi_j+w_j\), solve the P1 correction \(w_{j,h}\), set \(u_{j,h}=L\psi_j+w_{j,h}\), and define \(D^h_{jk}=B_V(u_{j,h},u_{k,h})\).

## 3. Theorem

Primal elliptic regularity, Céa/interpolation, the dual output problem

\[
a_0(v,z_g)=B_V(v,g),
\]

and Galerkin orthogonality yield

\[
\boxed{|D_{jk}-D^h_{jk}|\le Ch^2(1+j^2)^{3/4}(1+k^2)^{3/4}.}
\]

Indeed, with \(e_j=u_j-u_{j,h}\),

\[
D_{jk}-D^h_{jk}=B_V(e_j,u_k)+B_V(u_j,e_k)-B_V(e_j,e_k),
\]

and each term is bounded by \(Ch^2\|u_j\|_{H^2}\|u_k\|_{H^2}\) using primal and dual P1 errors.

Consequently,

\[
\|E_{h,J}\|_2=O(h^2J^4),
\]

and, under order-one trace-energy equivalence,

\[
\|S_J^{-1/2}E_{h,J}S_J^{-1/2}\|_2=O(h^2J^3).
\]

## 4. Exact boundary

Closed for the periodic-strip, exact-lift P1 model. Still open: nodal/discrete lifting at the same order, curved discrete interfaces and geometric variational crimes, nonsmooth domains, topology changes, external specialist review, and second-team blind execution.