---
type: "concept"
id: "riemann-curvature-tensor"
title: "Riemann curvature tensor"
domain: "curvature"
tier: "core"
aliases: ["Riemann tensor", "curvature tensor", "Riemann-Christoffel tensor", "R^a_bcd", "Riemann tensor component formula", "Riemann in terms of Christoffel symbols"]
prerequisites: ["christoffel-symbols", "covariant-derivative", "parallel-transport", "tensor", "path-dependence-of-parallel-transport"]
leads_to: ["symmetries-of-the-riemann-tensor", "number-of-independent-riemann-components", "ricci-tensor", "geodesic-deviation-equation", "flatness-criterion", "ricci-identity", "riemann-tensor-in-normal-coordinates", "weyl-tensor", "kretschmann-scalar", "linearized-riemann-tensor", "curvature-sign-conventions", "riemann-curvature-operator"]
sources: ["dinverno:ch06", "dinverno:ch09", "dinverno:ch10", "gifted-amateur:ch06", "gifted-amateur:ch11", "gifted-amateur:ch13", "gifted-amateur:ch30", "gifted-amateur:ch34", "gifted-amateur:ch35", "gifted-amateur:ch36", "legacy:manuscript-chapter-08-curvature-holonomy", "legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop", "legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature", "schutz:ch05", "schutz:ch06"]
review: "accurate"
---

# Riemann curvature tensor

> The Riemann tensor is the complete local measure of intrinsic curvature: a four-index tensor built from the Christoffel symbols and their first derivatives, and therefore from the metric and its first and second derivatives. It says how much a vector changes when carried around a tiny loop, how much two covariant derivatives fail to commute, and how nearby freely falling paths accelerate apart. It vanishes everywhere exactly when the geometry is flat, whatever coordinates you use.

## Explanations by level

### Intuition

Picture a curvature meter you can use at any point, from inside the space. You choose a tiny patch through the point, a small square lying in some plane, carry an arrow around its edge without twisting it, and note how the arrow comes back changed. Different planes and different arrows can give different answers, and the Riemann tensor is the complete table of all those answers at that point. The same table also tells you how two nearby objects falling freely side by side drift apart or together, which is what we feel as tides. Its great virtue is honesty: clever or awkward coordinates can make almost any quantity look strange, but they cannot fake or hide this table. If the table reads zero at every point, the space is flat, even if its maps look distorted. What the picture simplifies: the 'tiny patch' is really a limit; in four-dimensional spacetime the table has 20 independent entries rather than one number, and a plane can include the time direction, so 'arrow comes back changed' includes changes of velocity; and the table is local, so it can miss global features such as the tip of a cone.

**Picture to hold:** A small square card placed in different orientations at one point of a curved surface or space; for each orientation a pointer carried round the card's edge returns turned by a different amount; the list of those turns, for all orientations and pointers, is the Riemann tensor.

**Assumes:** [[parallel-transport]], [[path-dependence-of-parallel-transport]]

### Working

In a coordinate basis the components are $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. Give each index a job: $\sigma$ is the vector being carried, $\mu$ and $\nu$ span the plane of the loop, and $\rho$ picks which component of the change you read. The first two terms are how the connection varies across the loop; the last two are the connection acting on itself (as matrices, a commutator). Three equivalent readings: (1) loop: carrying $V$ around a small loop along $a$ then $b$ changes it by $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$; (2) commutator: $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$; (3) tides: nearby geodesics with separation $\xi$ obey $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$. Unlike the Christoffel symbols, $R$ is a genuine tensor, so if it vanishes in one coordinate system it vanishes in all. In locally inertial coordinates at a point the Christoffel symbols vanish and $R$ is a combination of second derivatives of the metric; those are exactly the 20 second-derivative combinations no coordinate change can remove. Symmetries with all indices down: antisymmetric in the first pair, antisymmetric in the second pair, symmetric under swapping pairs, plus the cyclic identity, leaving 1 component in two dimensions, 6 in three and 20 in four. Checks: the flat plane in polar coordinates has nonzero Christoffel symbols but $R^r{}_{\theta r\theta} = -1 + 1 = 0$; a sphere of radius $a$ has $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, Gaussian curvature $1/a^2$ and Ricci scalar $2/a^2$. In the Newtonian limit $R^i{}_{0j0} \approx \partial_i\partial_j\Phi$, the tidal tensor. Units: inverse length squared (with $c = 1$), or inverse time squared after multiplying by $c^2$.

**Picture to hold:** A four-slot machine: drop in the vector to be carried and two edge vectors of a tiny loop, pick an output component, and it returns the change; swap the two edge slots and the output flips sign.

**Assumes:** [[christoffel-symbols]], [[covariant-derivative]], [[tensor]], [[path-dependence-of-parallel-transport]]

### Formal

Let $\nabla$ be a torsion-free connection on a manifold $M$ (in GR the Levi-Civita connection of $g$, with $\nabla g = 0$). The curvature is the map $\mathcal{R}(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z$. It is $C^\infty$-linear in $X$, $Y$ and $Z$ (all derivatives of $Z$ cancel), hence a $(1,3)$ tensor field with components $R^\rho{}_{\sigma\mu\nu} = \langle dx^\rho, \mathcal{R}(\partial_\mu,\partial_\nu)\partial_\sigma\rangle$, which in a coordinate basis gives the component formula above; in a non-coordinate frame the commutation coefficients of the frame add terms. Ricci identities: $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$ and $[\nabla_\mu,\nabla_\nu]\omega_\sigma = -R^\lambda{}_{\sigma\mu\nu}\omega_\lambda$, one term per index for higher tensors (with torsion, an extra $-T^\lambda{}_{\mu\nu}\nabla_\lambda$ term appears). Algebraic identities for Levi-Civita: $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$ and $R_{\rho[\sigma\mu\nu]} = 0$ (the cyclic identity needs zero torsion); differential identity $\nabla_{[\lambda}R_{\rho\sigma]\mu\nu} = 0$. Independent components: $n^2(n^2-1)/12$. Flatness theorem: $R^\rho{}_{\sigma\mu\nu} = 0$ on an open set iff locally there are coordinates in which $g_{\mu\nu}$ is constant (diagonal with entries $\pm 1$); on a simply connected region this is equivalent to path-independent transport. Geometric content: $R$ is the holonomy per unit oriented area, a linear map from bivectors to infinitesimal isometries ($R_{\rho\sigma\mu\nu}$ antisymmetric in $\rho\sigma$). In two dimensions $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$; in three dimensions Riemann is determined by Ricci; in four or more it splits into Ricci parts plus the trace-free Weyl tensor. Sign behaviour: $R^\rho{}_{\sigma\mu\nu}$ depends only on the connection, so it is unchanged if $g \to -g$ (a signature flip), while $R_{\rho\sigma\mu\nu}$ and the Ricci scalar change sign. Course convention (MTW): the formula as written, $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, so a sphere of radius $a$ has $R = +2/a^2$.

**Picture to hold:** At each point, a linear machine from oriented 2-planes to infinitesimal rotations/boosts of the tangent space, with the pair symmetries making it a symmetric map on the space of bivectors (a symmetric 6 by 6 matrix in four dimensions, minus one cyclic constraint).

**Assumes:** [[tensor]], [[covariant-derivative]], [[lie-bracket]], [[torsion-free-connection]], [[metric-compatibility]]

## Prerequisites

- [[christoffel-symbols]] — The component formula is built from Christoffel symbols and their first derivatives.
- [[covariant-derivative]] — Riemann measures the failure of covariant derivatives to commute, so the covariant derivative must be fluent first.
- [[parallel-transport]] — The geometric definition carries a vector around a small loop by parallel transport.
- [[tensor]] — The key claim is that this combination, unlike Gamma, is a tensor, argued from its linearity in all four slots.
- [[path-dependence-of-parallel-transport]] — The motivating phenomenon: Riemann quantifies how transport depends on route, which is how Schutz and Gifted Amateur introduce it.

## Leads to

- [[symmetries-of-the-riemann-tensor]] — Pair antisymmetries and pair exchange cut the component count and are used in every calculation.
- [[number-of-independent-riemann-components]] — Counting the 20 components in four dimensions connects Riemann to the second metric derivatives coordinates cannot remove.
- [[ricci-tensor]] — The only independent contraction of Riemann; it enters the Einstein equation.
- [[geodesic-deviation-equation]] — Riemann is the coefficient in the relative acceleration of neighbouring geodesics, its physical reading as tides.
- [[flatness-criterion]] — Vanishing Riemann everywhere is the coordinate-independent test for flatness.
- [[ricci-identity]] — The commutator of covariant derivatives on any tensor is expressed through Riemann.
- [[riemann-tensor-in-normal-coordinates]] — At a point with vanishing Christoffel symbols Riemann reduces to second metric derivatives, the quickest route to its symmetries.
- [[weyl-tensor]] — The trace-free part of Riemann, the curvature not fixed locally by matter.
- [[kretschmann-scalar]] — Contracting Riemann with itself gives an invariant used to diagnose true singularities.
- [[linearized-riemann-tensor]] — Dropping the quadratic Gamma terms gives the gauge-invariant curvature of weak fields and gravitational waves.
- [[curvature-sign-conventions]] — Books differ in the sign and index placement of Riemann and Ricci; translating requires knowing this definition precisely.
- [[riemann-curvature-operator]] — The index-free operator with the Lie-bracket term defines Riemann in any frame.

## Related

- [[holonomy]] — Riemann is holonomy per unit oriented area; the two are equivalent local descriptions of curvature.
- [[newtonian-tidal-tensor]] — In the Newtonian limit the space-time-space-time components of Riemann reduce to the Hessian of the potential.
- [[nonzero-christoffel-symbols-in-flat-space]] — The standard trap Riemann resolves: nonzero Gamma in curvilinear coordinates with zero curvature.
- [[gaussian-curvature]] — In two dimensions Riemann has one component, equal to Gaussian curvature times the metric determinant.
- [[theorema-egregium]] — Gauss's intrinsic curvature is the two-dimensional ancestor of Riemann's tensor.
- [[local-flatness-theorem]] — Coordinates can remove the metric's first derivatives at a point but not the curvature carried by second derivatives.
- [[curvature-2-form]] — Cartan's curvature 2-forms carry exactly the Riemann components in an orthonormal frame.
- [[gauge-field-strength]] — The commutator form of Riemann mirrors the field strength of a gauge theory.
- [[minimal-coupling]] — Terms containing Riemann vanish in flat spacetime, so flat-space laws do not fix curvature couplings; minimal coupling excludes them.
- [[curvature-of-the-two-sphere]] — The canonical first explicit Riemann calculation.

## Key equations

### Riemann tensor from the connection (coordinate basis)

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}
$$

The working formula: derivative terms measure how the connection changes across a small loop in the mu-nu plane, product terms are the connection acting on itself. Antisymmetric in mu and nu by construction. *(SCH ch06 §6.5 p.157; GA ch11 §11.3 p.125; DIV ch06 §6.5 p.94)*

**Convention:** Course (MTW) convention. Schutz (6.63), Gifted Amateur (11.19) and d'Inverno (6.40) define the same tensor; Schutz and d'Inverno write Gamma with the derivative index last, which is invisible for the symmetric connection.

### Matrix (commutator) form

$$
\mathbf{R}_{\mu\nu} = \partial_\mu\boldsymbol{\Gamma}_\nu - \partial_\nu\boldsymbol{\Gamma}_\mu + [\boldsymbol{\Gamma}_\mu, \boldsymbol{\Gamma}_\nu],\qquad (\boldsymbol{\Gamma}_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}
$$

A memory aid and a computational shortcut: treat each Gamma_mu as a matrix (row index up, column index down); Riemann for the mu-nu plane is a curl plus a commutator, exactly like a non-abelian field strength. *(GA ch11 §11.3 p.125)*

**Convention:** Gifted Amateur margin note 11 writes the same with bullets for the matrix indices.

### Ricci identity (commutator of covariant derivatives)

$$
[\nabla_\mu, \nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma,\qquad [\nabla_\mu, \nabla_\nu]\omega_\sigma = -R^\lambda{}_{\sigma\mu\nu}\,\omega_\lambda
$$

Second covariant derivatives do not commute in curved space; the failure involves no derivatives of the field, only the Riemann tensor acting on it (plus sign for upper indices, minus for lower). *(SCH ch06 §6.5 p.160; DIV ch06 §6.5 p.95; GA ch35 §35.2 p.366)*

**Convention:** Torsion-free connection. d'Inverno (6.39) keeps a torsion term and writes the antisymmetrized derivative with a factor one half; Gifted Amateur writes c^alpha_{;nu mu} - c^alpha_{;mu nu}, where the later semicolon index is the outer derivative.

### Curvature operator

$$
\mathcal{R}(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z,\qquad R^\rho{}_{\sigma\mu\nu}X^\mu Y^\nu Z^\sigma = \big(\mathcal{R}(X,Y)Z\big)^\rho
$$

The index-free definition, valid in any basis; the Lie-bracket term corrects for loops of flow lines that do not close, and makes the result linear in X, Y and Z. *(GA ch35 §35.2 p.367; DIV ch06 Ex 6.11; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*

**Convention:** Gifted Amateur writes R( , c, a, b) = R-hat(a,b)c, matching this slot order.

### Small-loop holonomy

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu\qquad(\text{route } +a,\ +b,\ -a,\ -b)
$$

The geometric meaning: the change in a vector carried around a tiny loop, linear in the vector and in both edges. *(SCH ch06 §6.5 p.157; GA ch11 Example 11.3; DIV ch06 §6.7 p.98)*

**Convention:** Schutz and Gifted Amateur state it for the nu edge first, with a plus sign; equivalent.

### Riemann in locally inertial coordinates

$$
R_{\alpha\beta\mu\nu}\big|_p = \tfrac12\left(g_{\alpha\nu,\beta\mu} - g_{\alpha\mu,\beta\nu} + g_{\beta\mu,\alpha\nu} - g_{\beta\nu,\alpha\mu}\right)\quad(\Gamma|_p = 0)
$$

Where the connection vanishes at a point, curvature is a combination of second derivatives of the metric; the symmetries can be read off directly from this form. Not a tensor equation: valid only in such coordinates and only at p. *(SCH ch06 §6.5 p.158; GA ch11 Example 11.5)*

### Algebraic symmetries and component count

$$
R_{\alpha\beta\mu\nu} = -R_{\beta\alpha\mu\nu} = -R_{\alpha\beta\nu\mu} = R_{\mu\nu\alpha\beta},\quad R_{\alpha\beta\mu\nu} + R_{\alpha\nu\beta\mu} + R_{\alpha\mu\nu\beta} = 0,\quad N = \frac{n^2(n^2-1)}{12}
$$

Pair antisymmetries and pair exchange, plus the cyclic identity, reduce n^4 components to 1, 6 and 20 in two, three and four dimensions. *(SCH ch06 §6.5 p.159; GA ch35 Example 35.6; DIV ch06 §6.12 p.106)*

**Convention:** The lowered form depends on the metric's overall sign; with d'Inverno's (+,-,-,-) signature every lowered component flips sign relative to the course.

### Geodesic deviation

$$
\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\,\xi^\rho\,u^\sigma
$$

Relative acceleration of neighbouring free-fall worldlines with four-velocity u and separation xi: the physical, measurable face of Riemann (tides). *(SCH ch06 §6.5 p.160; GA ch11 §11.2 p.123; DIV ch10 §10.3 p.174)*

**Convention:** Schutz (6.87) writes +R^alpha_{mu nu beta} V^mu V^nu xi^beta and d'Inverno puts xi in the last slot with a minus on the other side; swapping the last two indices flips the sign, so all agree with the course.

### Newtonian limit

$$
R^i{}_{0j0} \approx \frac{\partial^2\Phi}{\partial x^i\,\partial x^j}
$$

For a static weak field the curvature components with two time slots are the Hessian of the Newtonian potential, so geodesic deviation reproduces Newtonian tides. *(GA ch11 Example 11.4; SCH ch07 Ex 7.9)*

**Convention:** Geometrized units (c = 1); restore 1/c^2 on the right in SI.

### Two dimensions and the sphere

$$
R_{\rho\sigma\mu\nu} = K\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}),\qquad \text{sphere of radius } a:\ R^\theta{}_{\phi\theta\phi} = \sin^2\theta,\ K = \frac{1}{a^2},\ R = \frac{2}{a^2}
$$

A surface has one independent component, the Gaussian curvature; the sphere is the calibration case that fixes the sign convention (positive Ricci scalar). *(SCH ch06 Ex 6.29; GA ch30 §30.6 p.319; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** Gifted Amateur ch30 writes K = R_1212 / g with g the metric determinant.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Overall sign and index order of R^rho_{sigma mu nu} | Eq. (6.63), same as MTW: R^alpha_{beta mu nu} = Gamma^alpha_{beta nu,mu} - Gamma^alpha_{beta mu,nu} + Gamma^alpha_{sigma mu} Gamma^sigma_{beta nu} - Gamma^alpha_{sigma nu} Gamma^sigma_{beta mu}; a footnote warns other books differ. | Eq. (11.19), MTW convention: first lower index is the transported vector, last two the loop plane. | Eq. (6.40): R^a_{bcd} = d_c Gamma^a_{bd} - d_d Gamma^a_{bc} + Gamma^e_{bd} Gamma^a_{ec} - Gamma^e_{bc} Gamma^a_{ed}, stated to match MTW. | MTW, as in the key equation. All three books define the same tensor; check against other texts (e.g. Weinberg) before borrowing signs. |
| Order of the lower indices on Gamma | Derivative index last: in the covariant derivative of a vector the vector is contracted with the first lower index of Gamma and the differentiation direction sits in the second. | Derivative index first: nabla_mu e_nu = Gamma^alpha_{mu nu} e_alpha (ch35); ch11 loop uses Gamma^alpha_{1 beta}. | Derivative index last: nabla_c X^a = d_c X^a + Gamma^a_{bc} X^b, which is why (6.40) reads d_c Gamma^a_{bd}. | Derivative index first: nabla_mu V^nu = d_mu V^nu + Gamma^nu_{mu lambda} V^lambda. Indistinguishable for the torsion-free Levi-Civita connection; matters only if torsion is introduced. |
| Metric signature and lowered components | (-,+,+,+). | (-,+,+,+). | (+,-,-,-). R^a_{bcd} and R_{ab} are unchanged by the overall sign flip, but R_{abcd}, the Ricci scalar and constant-curvature K flip sign relative to the course. | (-,+,+,+). When importing d'Inverno's lowered Riemann components, Ricci scalar or K, reverse their sign. |
| Commutator notation, factor one half and torsion | [nabla_alpha, nabla_beta] V^mu = R^mu_{nu alpha beta} V^nu (6.77), torsion-free; the lower-index version is left to an exercise that probes its sign. | [nabla_mu, nabla_nu] c^alpha = c^alpha_{;nu mu} - c^alpha_{;mu nu} = R^alpha_{beta mu nu} c^beta (35.13), where c_{;nu mu} means nabla_mu nabla_nu c. | (6.39) keeps a torsion term, proportional to the antisymmetric part of Gamma times the first derivative of the vector, alongside the Riemann term; for a symmetric connection (6.41) then writes the antisymmetrized second derivative, with normalized square brackets, as one half of Riemann acting on the vector. | Explicit commutator without the one half, torsion-free: [nabla_mu, nabla_nu] V^rho = R^rho_{sigma mu nu} V^sigma and a minus sign for each lower index. |
| Coordinate versus general frames | Component formula derived in coordinates; notes that equations with partial derivatives hold only in the frame where derived. | Curvature operator R-hat(a,b) = [nabla_a, nabla_b] - nabla_[a,b]; component formula valid in a coordinate basis where the bracket term drops; ch36 gets components from curvature 2-forms in orthonormal frames. | Index-free form with the Lie bracket appears as Exercise 6.11 and in ch10 (10.18). | Quote the component formula only in coordinate bases; in orthonormal frames use the operator or Cartan's structure equations. |
| Index order in geodesic deviation | (6.87): nabla_V nabla_V xi^alpha = R^alpha_{mu nu beta} V^mu V^nu xi^beta. | (11.6), (11.39): D^2 xi / dtau^2 = -R( , u, xi, u); a ch13 margin note drops the minus sign. | D^2 xi^a / Dtau^2 - R^a_{bcd} V^b V^c xi^d = 0 (ch10). | D^2 xi^mu / dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma. Compare index order before comparing signs; check with the Newtonian limit (radial stretching near a mass). |
| Ricci contraction (needed for sign checks) | R_{alpha beta} = R^mu_{alpha mu beta}. | R_{nu beta} = R^mu_{nu mu beta}. | R_{ab} = R^c_{acb}. | R_{mu nu} = R^rho_{mu rho nu}; a sphere of radius a has R = +2/a^2 in the course signature. |

## How the sources teach it

### schutz

**Route:** Chapter 5 closes by naming a tensor that will measure the failure of parallelism. Chapter 6 first counts what coordinate freedom can do to a metric's Taylor expansion at a point and finds 20 second-derivative combinations left over, before Riemann is defined. Section 6.4 shows the sphere octant loop. Section 6.5 defines Riemann by transporting a vector around a tiny loop of coordinate lines (Fig. 6.5), argues tensor character from linearity in the vector and both edges, rewrites it in locally inertial coordinates as second metric derivatives, derives the symmetries and the count of 20 (matching the earlier count), shows the commutator of covariant derivatives equals Riemann, and derives geodesic deviation. Section 6.6 adds Bianchi identities, Ricci and Einstein tensors.

**Representation:** Components and comma-semicolon notation; tensors as machines with slots; local inertial frame arguments ('true in one frame, tensor equation, true in all').

**Strengths:** The early count makes 20 a prediction rather than a fact; the loop definition gives each index a role; the local-inertial-frame trick makes symmetries short; three readings (loop, commutator, deviation) appear in one section.

**Weaknesses:** Much algebra is left to exercises (loop details, symmetries, the sphere and polar-plane checks); the loop formula's small-loop restriction is stated but not visualized; conventions are only flagged in a footnote. *(SCH ch05 §5.6 p.138; SCH ch06 §6.2 p.149; SCH ch06 Fig. 6.5 p.156; SCH ch06 §6.5 p.157; SCH ch06 §6.5 p.158; SCH ch06 §6.5 p.160)*

### gifted-amateur

**Route:** Chapter 6 gives the slogan that first metric derivatives make the connection and first plus second derivatives make curvature. Chapter 11 opens with Newtonian tidal accelerations and the Hessian of the potential, states geodesic deviation as their relativistic version with Riemann as coefficient, then defines Riemann by transport around an infinitesimal parallelogram (Example 11.3), offers the matrix-commutator mnemonic, checks the weak-field limit against Newtonian tides (Example 11.4), derives symmetries in a local inertial frame (Example 11.5), contracts to Ricci, and shows the polar plane has zero curvature despite nonzero Gammas (Example 11.7). Chapter 13 calls Riemann the best candidate for 'the gravitational field'. Chapter 35 rebuilds it abstractly as the curvature operator reached from geodesic deviation and shows its components match (Example 35.3); chapter 36 recovers the same components from curvature 2-forms.

**Representation:** Physics-first motivation (tides), slot-machine tensors, parallelogram bookkeeping, matrix mnemonic, later operator and differential-form versions.

**Strengths:** Learners meet Riemann as the answer to a physical question (tides) and see the flat-coordinates trap defused early; the matrix mnemonic makes the formula memorable; the same object is shown to arise from three formalisms.

**Weaknesses:** In chapter 11 geodesic deviation is asserted rather than derived; the operator definition that justifies everything arrives 24 chapters later; a margin sign slip in chapter 13; the relation between the two definitions can feel disconnected. *(GA ch06 §6.3 p.75; GA ch11 §11.2 p.123; GA ch11 Example 11.3; GA ch11 Example 11.4; GA ch11 Example 11.7; GA ch13 §13.1 p.142; GA ch35 Example 35.3; GA ch36 Example 36.2)*

### dinverno

**Route:** Section 6.5 computes the commutator of two covariant derivatives on a vector for a general affine connection, finds a torsion term plus a term linear in the vector, and defines the Riemann tensor from the latter, proving tensor character by the quotient argument. Section 6.7 supplies the geometric meaning through the lemma that a connection is integrable iff Riemann vanishes, using an infinitesimal loop. Section 6.11 proves a metric is flat iff Riemann vanishes, and §6.12 lists symmetries, the cyclic identity, Ricci and Einstein tensors. Chapter 10 reads Riemann physically as the coefficient in geodesic deviation and linearizes it in the Newtonian limit, stressing that vacuum means vanishing Ricci, not Riemann.

**Representation:** Algebra-first, abstract index notation, identities marked with a triple bar, lemma-and-proof structure; physical interpretation deferred.

**Strengths:** Logically tight: definition, tensor proof, geometric meaning and flatness theorem with hypotheses (symmetric connection, simple connectedness) all explicit; keeps torsion visible so the learner sees where symmetry is used.

**Weaknesses:** Little motivation or imagery when the tensor first appears; no worked component example on a familiar surface in the chapter; physical meaning arrives chapters later. *(DIV ch06 §6.5 p.94; DIV ch06 §6.5 p.95; DIV ch06 §6.7 p.97; DIV ch06 §6.11 p.105; DIV ch06 §6.12 p.106; DIV ch10 §10.3 p.174; DIV ch10 §10.4 p.176)*

### legacy

**Route:** Chapter 8 opens with transport around loops (two-route and loop labs), then defines Riemann from the commutator of covariant derivatives with the key cancellations stated, gives the operator form with the bracket term and the covector sign, states the small-loop law with orientation conventions, shows the polar plane gives zero (a derivative term of -1 cancelling a product term of +1), proves the symmetries in explicitly constructed coordinates with vanishing Gamma, counts 21 minus 1 = 20 components (and warns they are not wave polarizations), and computes the sphere's components, Gaussian curvature and Ricci scalar to fix the sign convention.

**Representation:** Manuscript with visual labs, a component-counting lab, an independent finite-difference curvature checker, and a calibration table of test metrics.

**Strengths:** Flat control and curved case use the identical formula; sign convention is fixed operationally by the sphere; symmetries are proved in a constructed frame, not assumed; numerical verification backs every quoted result.

**Weaknesses:** The commutator cancellations are stated rather than shown; the learner never computes a new metric; the component-count lab has interaction rough edges. *(legacy:manuscript-chapter-08-curvature-holonomy; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; legacy:lab-riemann-independent-components)*

## Recommended teaching path

1. **Ask what coordinates cannot remove** — Pose Gifted Amateur's puzzle: a free particle seems to accelerate; is it gravity or perverse coordinates? Then do Schutz's count: coordinate freedom at a point can set the metric to Minkowski and kill its first derivatives, but 20 combinations of second derivatives remain. *Why:* Creates the need for a coordinate-proof object and predicts the number 20 before any formula. *(GA ch13 §13.1 p.141; SCH ch06 §6.2 p.149; GA ch06 §6.3 p.75)*
2. **Picture it as loop holonomy** — Recall a vector carried around a small loop returns changed in proportion to area; define Riemann as that change per unit area, a machine with slots for the vector, the two loop edges and the output component. *Why:* Gives every index a physical job before the learner sees 16 Christoffel terms. *(SCH ch06 §6.5 p.158; GA ch11 Fig. 11.5 p.124; legacy:manuscript-chapter-08-curvature-holonomy)*
3. **Derive the component formula** — Either expand transport around a coordinate parallelogram or expand the commutator of covariant derivatives; show derivative-of-V terms cancel, leaving the curl of Gamma plus the Gamma commutator. Offer the matrix mnemonic. *Why:* Two short derivations of the same formula build trust that it is not arbitrary; the mnemonic makes it recallable. *(GA ch11 Example 11.3; DIV ch06 §6.5 p.94; SCH ch06 §6.5 p.160; GA ch11 §11.3 p.125)*
4. **Establish tensor character and structure** — Argue tensor character from linearity; go to locally inertial coordinates to write Riemann as second metric derivatives, read off the symmetries, and count 20 components in four dimensions (1 in two). *Why:* Connects the formula back to the opening count and makes the symmetries a consequence rather than a list. *(GA ch11 Example 11.5; SCH ch06 §6.5 p.159; legacy:lab-riemann-independent-components)*
5. **Calibrate on known geometries** — Compute the polar-coordinate plane (zero, with the -1 and +1 cancelling), the sphere of radius a (sin squared theta, K = 1/a^2, R = 2/a^2) and, optionally, Rindler coordinates (zero). *Why:* The flat controls defeat the belief that Christoffel symbols signal curvature; the sphere fixes the sign convention with a number the learner can remember. *(GA ch11 Example 11.7; SCH ch06 Ex 6.29; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; legacy:manuscript-section-24-2-rindler-full-check)*
6. **Give it physical meaning: tides** — Show geodesic deviation with Riemann as coefficient and take the weak static limit: the time-time components are the Hessian of the Newtonian potential, stretching radially and squeezing sideways near a mass. *Why:* Links the abstract tensor to something felt and measured, and shows GR contains Newtonian tides. *(GA ch11 Example 11.4; SCH ch06 §6.5 p.160; DIV ch10 §10.3 p.174; legacy:lab-tidal-cloud-geodesic-deviation)*
7. **Guard against common slips** — Contrast Riemann with Ricci (vacuum outside a star has zero Ricci but tides) and with the Ricci scalar; state the course sign convention and the sphere check for translating other books. *Why:* The most damaging later errors (vacuum means flat; sign mismatches across texts) are prevented here. *(GA ch11 Ex 11.3; DIV ch10 §10.4 p.176; SCH ch06 §6.5 p.158)*
8. **Unify the definitions (formal track)** — Present the curvature operator with the Lie-bracket term, show its coordinate components reproduce the formula, and mention the curvature 2-form route. *Why:* Learners going further need a frame-independent definition and assurance the different routes give one object. *(GA ch35 Example 35.3; GA ch36 Example 36.2; DIV ch06 Ex 6.11)*

## Analogies

- **A curvature meter with a card you can tilt** (intuition): At a point, hold a tiny card in some orientation, carry an arrow around its edge, and record the change; the Riemann tensor is the full set of readings for every card orientation and every arrow. *Limits:* Real measurements use finite loops; spacetime cards can include the time direction, so 'change' includes boosts; and the meter is local, blind to global features like conical tips. *(SCH ch06 §6.5 p.158)*
- **Tilting a sheet of graph paper against a curved dome** (intuition): Laying a flat sheet on a dome at one point, you can match the position and slope exactly, but not how the dome bends away; coordinate choice likewise matches the metric and its first derivatives at a point, while the leftover second derivatives are curvature. *Limits:* The dome is an extrinsic picture of a surface in 3D; Riemann is intrinsic and needs no embedding. The counting in four dimensions (20 irreducible combinations) has no simple dome analogue. *(SCH ch06 §6.2 p.149; GA ch06 §6.4 p.76)*
- **A tensor slot machine that returns a relative acceleration** (working): Feed the four-velocity into two slots and the separation into one; out comes (minus) the relative acceleration of the neighbouring free-fall path. *Limits:* Hides which slot is which; learners must remember the velocity occupies the second and fourth slots and the sign convention. *(GA ch35 §35.1 p.363; GA ch11 §11.2 p.123)*
- **Connection matrices and a commutator** (working): Treat each Christoffel symbol with fixed derivative index as a matrix; Riemann is then 'derivative minus derivative plus commutator', the same shape as a Yang-Mills field strength. *Limits:* The matrix picture hides index positions; mixing up which lower index is the derivative index gives sign errors when torsion or unconventional orderings appear. *(GA ch11 §11.3 p.125)*
- **Riemann as 'the gravitational field'** (working): What remains of gravity after you choose a freely falling frame is the part no frame can remove, and that is Riemann: the tidal field. *Limits:* It corresponds to second derivatives of the Newtonian potential (tides), not to the Newtonian g-vector, which is frame dependent in GR; and matter fixes only its Ricci part locally. *(GA ch13 §13.1 p.142)*

## Misconceptions

- **Nonzero Christoffel symbols mean the space is curved.** — Christoffel symbols describe how the coordinate basis changes and are nonzero for curvilinear coordinates in flat space. Only the Riemann tensor, a true tensor, decides curvature; for the polar plane it vanishes. *Why tempting:* Christoffel symbols are the first gravity-like objects learners meet and appear as 'forces' in the geodesic equation. *Diagnostic:* The flat plane in polar coordinates has Gamma^r_{theta theta} = -r. Is the plane curved? What would you compute to decide, and what do you expect? *(SCH ch05 §5.3 p.127; GA ch11 §11.3 p.124; legacy:manuscript-section-24-2-rindler-full-check)*
- **A vanishing Ricci tensor (or Ricci scalar) means spacetime is flat.** — Riemann = 0 implies Ricci = 0 implies R = 0, but not conversely. Outside a star Ricci vanishes while Riemann does not, so tides persist; gravitational waves are Ricci-flat but curved; a radiation-filled universe has zero Ricci scalar yet is curved. *Why tempting:* All three are called curvature and share the letter R; the vacuum field equation sets Ricci to zero. *Diagnostic:* The vacuum Einstein equation says R_{mu nu} = 0 outside the Sun. Does that mean no tides act on the Earth-Moon system? Which object would you compute to check? *(GA ch11 Ex 11.3; DIV ch10 §10.4 p.176; GA ch13 §13.4 p.148)*
- **The Riemann tensor has 256 independent components in spacetime (or its 20 components are 20 independent wave polarizations).** — Symmetries leave 20 independent components in four dimensions. They describe curvature at a point, not propagating degrees of freedom: gravitational waves have two polarizations, and ten of the 20 (the Ricci part) are fixed locally by matter. *Why tempting:* A four-index object in four dimensions naively has 4^4 = 256 entries, and 'independent components' sounds like 'independent physical freedoms'. *Diagnostic:* How many independent Riemann components does a two-dimensional surface have, and what familiar quantity is it? Why does that not mean a surface has one 'degree of freedom' that propagates? *(GA ch11 §11.4 p.126; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **The Riemann tensor has one universal sign and index layout.** — Books differ in the overall sign, in which index pair is the loop plane, in Ricci contraction and in signature. Always translate using a calibration: a sphere should have positive Ricci scalar in MTW-type conventions. *Why tempting:* Each textbook presents its own convention as if it were the only one. *Diagnostic:* A formula from another book gives the unit sphere a Ricci scalar of -2. List the three convention differences that could produce this before you conclude anything is wrong. *(SCH ch06 §6.5 p.158)*
- **With clever enough coordinates you can make spacetime flat around a point to all orders.** — Coordinates can make the metric Minkowskian with vanishing first derivatives at a point, but 20 combinations of second derivatives cannot be removed; they are the Riemann tensor. *Why tempting:* The equivalence principle is often paraphrased as 'gravity can always be transformed away'. *Diagnostic:* In a freely falling lab, which gravitational effects disappear and which remain? Where in the metric's Taylor expansion does the remaining effect live? *(GA ch06 §6.4 p.76; SCH ch06 §6.2 p.149)*
- **The full Riemann tensor should vanish in vacuum, or appear itself on the left side of the field equation.** — Vanishing Riemann would forbid tides and is the flatness condition of special relativity. Riemann has four indices while stress-energy has two, so only a contraction (Ricci, via the Einstein tensor) is set by matter; the rest (Weyl) is determined by field equations and boundary conditions. *Why tempting:* If curvature is gravity and matter sources gravity, 'no matter, no curvature' seems natural. *Diagnostic:* If R^rho_{sigma mu nu} had to vanish wherever there is no matter, what would happen to the tidal stretching of an astronaut falling toward a black hole? *(DIV ch10 §10.8 p.184; GA ch13 §13.1 p.142)*
- **A single component of Riemann blowing up in some frame proves a curvature singularity.** — Components can diverge because the frame or coordinates are bad. Evidence for a physical singularity comes from invariants (such as the Kretschmann scalar) or from components measured in a frame carried by an actual observer. *Why tempting:* Divergent numbers look like physical infinities. *Diagnostic:* At the Schwarzschild horizon some coordinate components misbehave. What quantity would you compute to decide whether the horizon is a real singularity, and what is its value there? *(GA ch26 §26.1 p.273; legacy:manuscript-section-10-curvature-invariants-and-summary-table)*
- **Curvature (times c squared) is an acceleration, so a large Riemann tensor means a large gravitational pull.** — Riemann has units of inverse length squared (inverse time squared after multiplying by c^2). A tidal acceleration needs a separation, and curvature says nothing about the weight felt by a supported observer, which is set by the first derivative of the potential. *Why tempting:* Curvature is loosely called 'gravity'. *Diagnostic:* Near Earth's surface the tidal components are about 1.5e-6 per second squared. What acceleration difference does that give between your head and feet, and why is it not 9.8 m/s^2? *(GA ch11 Example 11.4)*

## Thought experiments

- **Gravity or perverse coordinates?**: A single free particle appears to accelerate in some coordinate system. Is a gravitational field present, or only odd coordinates? *Lesson:* A single worldline cannot tell; the relative acceleration of neighbouring free particles, governed by Riemann, is the coordinate-independent test. *(GA ch13 §13.1 p.141)*
- **Resizing and reversing the tiny loop**: Double one side of the infinitesimal loop, or traverse it in the opposite sense. *Lesson:* The change doubles or flips sign, so it is linear in each edge and antisymmetric in their order: a tensor antisymmetric in its last two indices. *(SCH ch06 §6.5 p.157)*
- **Counting what coordinates can do**: Expand a metric in a Taylor series about a point and count the free coefficients of a coordinate transformation at each order against the metric coefficients to be cancelled. *Lesson:* Everything can be matched at zeroth and first order (leaving the 6 Lorentz freedoms), but 20 second-order combinations survive: the Riemann components. *(SCH ch06 §6.2 p.149)*

## Visualizations

### Riemann slot machine · interactive-3d · high priority

On a curved space the learner drops a vector and two small edge vectors into slots at a point; the output arrow Delta V (the loop change) appears, computed from Riemann and confirmed by numerically transporting around the actual loop. Swapping edges flips the output; scaling an edge scales it; tilting the plane changes it.

**Interaction:** Choose sphere, saddle, polar plane, or the 3D product space sphere-times-line; drag V, a and b in the tangent space; a panel shows the contracted formula with live numbers. In the product space, planes containing the line direction give zero output, showing plane dependence.

**Model:** Symbolic Christoffels and Riemann for each metric (sphere a^2(dtheta^2 + sin^2 theta dphi^2), product with + dz^2, hyperbolic plane); numerical RK4 transport around the parallelogram as an independent check of -R V a b to leading order.

**Inspired by:** SCH ch06 §6.5 p.158; GA ch11 Fig. 11.5 p.124; SCH ch06 Fig. 6.5 p.156

**Legacy assets:** scene-3d-parallel-transport-loop, engine-independent-curvature-checker

### Christoffels say yes, Riemann says no · interactive-2d · high priority

A calculation board: pick a metric and a point; the nonzero Christoffel symbols light up, and each Riemann component is shown as its four terms (two derivative terms and two product terms) with numerical values, so the learner watches the cancellation for flat metrics and its failure for curved ones.

**Interaction:** Metrics: polar plane, rotating frame, Rindler, weak-field static potential, unit sphere, Schwarzschild exterior. Drag the evaluation point; click a component to expand its terms; a 'flat?' verdict updates.

**Model:** Symbolic or finite-difference Christoffels and Riemann (course conventions), cross-checked against closed forms (polar R^r_{theta r theta} = 0; sphere R^theta_{phi theta phi} = sin^2 theta; Rindler R^z_{tzt} proportional to q'' = 0).

**Inspired by:** GA ch11 Example 11.7; SCH ch06 Ex 6.19; GA ch11 Ex 11.4

**Legacy assets:** manuscript-section-8-4-8-6-flatness-count-sphere-curvature, manuscript-section-24-2-rindler-full-check, engine-independent-curvature-checker

### From Riemann to tides · interactive-3d · medium priority

A small freely falling cloud of particles near a mass deforms according to geodesic deviation driven by R^i_{0j0}; the tidal matrix with eigenvalues proportional to (-2, 1, 1) GM/r^3 is displayed beside the stretching ellipsoid.

**Interaction:** Sliders for mass and distance with Earth, neutron star and black hole presets in SI units; toggle a Newtonian Hessian overlay to show agreement in the weak field.

**Model:** xi'' = -R^i_{0j0} xi^j with R^i_{0j0} = d_i d_j Phi for Phi = -GM/r (weak field), exact exponential and trigonometric solutions along eigen-axes; orthonormal-frame Schwarzschild components for the strong-field preset.

**Inspired by:** GA ch11 Example 11.4; SCH ch06 §6.5 p.160

**Legacy assets:** lab-tidal-cloud-geodesic-deviation, scene-3d-tidal-cloud

### From 256 to 20 · interactive-2d · medium priority

A grid of all index combinations; applying each symmetry in turn greys out dependent entries and links partners with signs, ending at the independent components.

**Interaction:** Dimension selector 2, 3, 4 (showing 1, 6, 20 against the formula n^2(n^2-1)/12); click an entry to see its symmetry partners; step through pair antisymmetry, pair exchange and the cyclic identity; commit on click, not hover.

**Model:** Combinatorial canonicalization of index tuples under the Riemann symmetries, verified exhaustively.

**Inspired by:** SCH ch06 §6.2 p.149; GA ch35 Example 35.6

**Legacy assets:** lab-riemann-independent-components, figure-curvature-count

## Worked examples

- **Riemann from an infinitesimal loop** (working): Transport along four coordinate edges, pairing of opposite edges, first-order expansion and elimination of derivatives of V yield the component formula and its tensor character. *(SCH ch06 §6.5 p.156; GA ch11 Example 11.3)*
- **Commutator of covariant derivatives** (working): In a local inertial frame only derivatives of Gamma survive the antisymmetrized second derivative, reproducing the Riemann terms; the general computation shows a torsion term when the connection is not symmetric. *(SCH ch06 §6.5 p.159; DIV ch06 §6.5 p.94)*
- **Weak static field gives Newtonian tides** (working): With only Gamma^i_{tt} = d_i Phi and products dropped, the time-time Riemann components equal the Hessian of the potential. *(GA ch11 Example 11.4)*
- **Symmetries in a local inertial frame** (formal): Where Gamma vanishes, Riemann is four second metric derivatives whose symmetries follow from symmetry of g and of mixed partials; tensor equations then hold everywhere. *(GA ch11 Example 11.5; SCH ch06 §6.5 p.158)*
- **Polar plane is flat** (working): The two nonzero polar Christoffel symbols generate a derivative term and a product term that cancel exactly. *(GA ch11 Example 11.7; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **Sphere curvature and the sign check** (working): Christoffels of the sphere, R^theta_{phi theta phi} = sin^2 theta, Gaussian curvature 1/a^2, Ricci tensor and scalar 2/a^2 fixing the convention. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **Counting independent components** (working): Pairs of antisymmetric indices, a symmetric matrix of pairs, minus cyclic constraints give n^2(n^2-1)/12. *(GA ch35 Example 35.6)*
- **Operator components equal the component formula** (formal): Evaluating the curvature operator on coordinate basis vectors with the Leibniz rule recovers the Christoffel expression, uniting the geometric and component definitions. *(GA ch35 Example 35.3; GA ch36 Example 36.2)*
- **Flat iff Riemann vanishes** (formal): Necessity from a constant metric; sufficiency via coordinates with vanishing connection and metric compatibility forcing constant components. *(DIV ch06 §6.11 p.105)*
- **Rindler observers: connection without curvature** (working): Accelerated coordinates have nonzero Christoffels, height-dependent proper acceleration and clock rates, yet the Riemann component vanishes. *(legacy:manuscript-section-24-2-rindler-full-check)*

## Exercises

- (intro) Show the Riemann tensor of the Euclidean plane in polar coordinates vanishes. *Skill:* Component formula on a flat control *(SCH ch06 Ex 6.19)*
- (standard) Compute the Riemann tensor of a unit sphere using the single independent component in two dimensions. *Skill:* First curved calculation *(SCH ch06 Ex 6.29)*
- (standard) Reduce the independent components from 256 to 21 by pair symmetries and then to 20 with the cyclic identity. *Skill:* Symmetry counting *(SCH ch06 Ex 6.18)*
- (standard) Compute the first-order Riemann tensor of the weak-field metric and show geodesic deviation gives the Hessian of the potential. *Skill:* Newtonian limit of curvature *(SCH ch07 Ex 7.9)*
- (standard) Show the Ricci tensor vanishes outside a star using given Schwarzschild Riemann components, and explain why. *Skill:* Ricci versus Riemann *(GA ch11 Ex 11.3)*
- (standard) Prove a rotating-frame metric is flat. *Skill:* Coordinate effects versus curvature *(GA ch11 Ex 11.4)*
- (standard) Prove the component commutator identity and contract it to swap a divergence and a gradient. *Skill:* Second covariant derivatives *(GA ch35 Ex 35.2)*
- (challenging) Show the covariant-derivative commutator corrected by the Lie bracket equals Riemann contracted with three vectors. *Skill:* Index-free definition *(DIV ch06 Ex 6.11)*
- (challenging) Compute Schwarzschild Christoffels and Riemann components, transform to an orthonormal frame, show they stay finite at 2M and that an invariant diverges at r = 0. *Skill:* Full curvature computation and singularity diagnosis *(SCH ch11 Ex 11.21)*

## Checks for understanding

- **Q (intuition):** In polar coordinates the flat plane has nonzero Christoffel symbols. A friend says this proves polar coordinates 'see' curvature. What is wrong, and what single object settles the question?
  - **A:** Christoffel symbols encode how the coordinate basis vectors change from point to point, which happens in curvilinear coordinates even on a flat plane; they are not tensor components and can be made zero by switching to Cartesian coordinates. The Riemann tensor is a tensor: computed in polar coordinates it is zero, so it is zero in every coordinate system and the plane is flat. *(targets: Nonzero Christoffel symbols mean the space is curved.)*
- **Q (working):** For the polar plane, Gamma^r_{theta theta} = -r and Gamma^theta_{r theta} = Gamma^theta_{theta r} = 1/r. Compute R^r_{theta r theta} with the course formula.
  - **A:** R^r_{theta r theta} = d_r Gamma^r_{theta theta} - d_theta Gamma^r_{r theta} + Gamma^r_{r lambda} Gamma^lambda_{theta theta} - Gamma^r_{theta lambda} Gamma^lambda_{r theta}. First term: -1. Second: 0. Third: Gamma^r_{rr} Gamma^r_{theta theta} + Gamma^r_{r theta} Gamma^theta_{theta theta} = 0. Fourth: Gamma^r_{theta r} Gamma^r_{r theta} + Gamma^r_{theta theta} Gamma^theta_{r theta} = 0 + (-r)(1/r) = -1, entering with a minus sign as +1. Total: -1 + 1 = 0.
- **Q (working):** A sphere of radius a has metric a^2(dtheta^2 + sin^2 theta dphi^2), with Gamma^theta_{phi phi} = -sin theta cos theta and Gamma^phi_{theta phi} = cot theta. Find R^theta_{phi theta phi}, the Gaussian curvature and the Ricci scalar.
  - **A:** R^theta_{phi theta phi} = d_theta Gamma^theta_{phi phi} - Gamma^theta_{phi phi} Gamma^phi_{theta phi} = -(cos^2 theta - sin^2 theta) + sin theta cos theta cot theta = sin^2 theta. Lowering: R_{theta phi theta phi} = a^2 sin^2 theta; dividing by det g = a^4 sin^2 theta gives K = 1/a^2. Ricci: contracting the first and third indices gives 1 for the theta-theta component and sin^2 theta for the phi-phi component. Raising with the inverse metric, (1/a^2)(1) plus (1/(a^2 sin^2 theta))(sin^2 theta) gives a Ricci scalar of 2/a^2, positive as the course convention requires. *(targets: The Riemann tensor has one universal sign and index layout.)*
- **Q (working):** Outside the Sun the vacuum field equation gives R_{mu nu} = 0. Does this mean spacetime there is flat? Use the Newtonian limit to support your answer.
  - **A:** No. Ricci is only a trace of Riemann. In the Newtonian limit R^i_{0j0} = d_i d_j Phi, the Hessian of the potential, and Ricci-flatness corresponds to its trace, the Laplacian of Phi, vanishing in empty space. The Hessian itself is nonzero: for Phi = -GM/r its radial eigenvalue is -2GM/r^3 and transverse ones +GM/r^3 (trace zero), giving radial stretching and sideways squeezing: tides. So Riemann is nonzero and spacetime is curved. *(targets: A vanishing Ricci tensor (or Ricci scalar) means spacetime is flat.)*
- **Q (formal):** How many independent Riemann components are there in 2, 3 and 4 dimensions, and why does the three-dimensional count explain why Ricci-flat 3D space is flat?
  - **A:** n^2(n^2-1)/12 gives 1, 6 and 20. In three dimensions the symmetric Ricci tensor also has 6 components, and Riemann can be written entirely in terms of Ricci and the metric, so Ricci = 0 forces Riemann = 0. In four dimensions Ricci has 10 components and the remaining 10 (Weyl) can be nonzero in vacuum. *(targets: The Riemann tensor has 256 independent components in spacetime (or its 20 components are 20 independent wave polarizations).)*
- **Q (formal):** Show that the Riemann tensor is unchanged by g -> -g but R_{rho sigma mu nu} changes sign. Why does this matter when reading d'Inverno?
  - **A:** The Christoffel symbols are built from g^{-1} times derivatives of g, so the two sign flips cancel and Gamma, hence R^rho_{sigma mu nu}, is unchanged; Ricci R_{mu nu} is a contraction of it and is also unchanged. Lowering the first index uses g, so R_{rho sigma mu nu} flips, and the Ricci scalar g^{mu nu} R_{mu nu} flips. d'Inverno uses signature (+,-,-,-), so his lowered components, Ricci scalar and constant-curvature K have the opposite sign to the course's for the same geometry.

## Applications

- **Tides**: Geodesic deviation with Riemann as coefficient gives tidal stretching and squeezing; in the weak field it reproduces the Newtonian tidal tensor. Key numbers: Near Earth's surface GM/r^3 = g/R_Earth = 1.5e-6 s^-2; at the horizon of a 10 solar-mass black hole 2GM/r^3 is about 1e8 s^-2. *(GA ch11 Example 11.4; SCH ch07 Ex 7.9)*
- **Gravitational-wave detection**: A detector responds to the curvature of the passing wave; in transverse-traceless gauge R_{i0j0} = -(1/2) d_t^2 h_{ij}, which drives the relative motion of test masses; Riemann is gauge invariant while h is not. Key numbers: Strain h = 1e-21 over a 4 km arm changes the arm length by about 2e-18 m. *(legacy:manuscript-section-18-1-linearized-gravity-detector)*
- **Singularities versus coordinate artefacts**: The Kretschmann invariant R_{abcd}R^{abcd} = 48 M^2 / r^6 for Schwarzschild is finite at the horizon (3/(4M^4) at r = 2M) and diverges at r = 0. Key numbers: K = 48 G^2 M^2 / (c^4 r^6) *(SCH ch11 Ex 11.21; legacy:manuscript-section-10-curvature-invariants-and-summary-table)*
- **Choosing laws of physics in curved spacetime**: Because curvature terms vanish in flat spacetime, a flat-space law can be generalized with or without explicit Riemann couplings; minimal coupling excludes them, and the choice is ultimately experimental. *(DIV ch09 §9.6 p.166)*

## History

- **Bernhard Riemann (1854):** Habilitation lecture on the hypotheses underlying geometry introduced curvature of higher-dimensional spaces measured on two-dimensional sections; his 1861 Paris prize essay contains the curvature expression. *(GA ch30 §30.6 p.319)*
- **Elwin Bruno Christoffel (1869):** Introduced the connection symbols and the four-index curvature quantity while studying when two quadratic differential forms are equivalent.
- **Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900):** Systematized tensor calculus (absolute differential calculus), the language Einstein and Grossmann adopted for gravitation in 1913.

## Tutor guidance

**Opening questions**

- If someone hands you a strange-looking metric, how could you tell whether the space is truly curved or just described with awkward coordinates?
- When you ride in a freely falling elevator, gravity seems to vanish. What gravitational effect could you still detect inside, given a large enough elevator?
- What happened when we carried an arrow around a loop on a sphere, and how might we turn that into a number at each point?

**Common questions**

- *Why does Riemann have four indices?* — One index for the vector you carry, two for the plane of the tiny loop (two edge directions), and one for the component of the change you read off.
- *Do I have to memorize the component formula?* — It helps to remember its shape: derivative of Gamma minus the same with the loop indices swapped, plus Gamma times Gamma minus the swap. The matrix form, curl plus commutator, is the easiest way to store it.
- *Why can't I just use the Christoffel symbols to measure curvature?* — They are not tensor components; they change under coordinate transformations and can be zero at a point in any spacetime, or nonzero in flat space. Riemann combines their derivatives and products so that coordinate artefacts cancel.
- *Is the Riemann tensor the gravitational field?* — It is the part of gravity that no choice of freely falling frame can remove: the tidal field. The 'pull' you feel standing on Earth is not curvature; it is the floor accelerating you away from free fall.
- *Why do other books have different signs?* — They choose a different overall sign, a different index for the loop plane, a different Ricci contraction or signature. Check with the sphere: in the course convention its Ricci scalar is +2 over the radius squared.

**Pitfalls when explaining**

- Do not introduce Riemann as 'the second derivative of the metric' without the locally-inertial-frame qualifier; in general coordinates it has product terms too.
- Do not let 'R' float without its indices in speech; say Riemann, Ricci tensor or Ricci scalar explicitly.
- Do not state 'vacuum means no curvature'; say 'vacuum means zero Ricci curvature'.
- State the course convention whenever a sign matters, and use the sphere as the check.
- Do not quote the component formula in an orthonormal frame without the extra commutation terms.
- Avoid calling the 20 components degrees of freedom or polarizations.

**When to show a demo**

- In the Christoffel-versus-Riemann board, have the learner predict the polar-plane result before expanding the four terms.
- In the slot machine, ask what happens when the two edge vectors are made parallel (output zero) before trying it.
- In the tidal cloud, ask for the direction of stretching near a mass before pressing play, then compare with the sign of the Hessian.
- In the component counter, let the learner switch to two dimensions and name the single surviving component.

**Saying it aloud:** Say the component formula as: the Riemann tensor for a loop in the mu-nu plane is the derivative along mu of the connection in the nu direction, minus the same with mu and nu swapped, plus the connection matrices multiplied in one order, minus the other order. Say the Ricci identity as: taking covariant derivatives in two orders and subtracting gives the Riemann tensor acting on the field. Say geodesic deviation as: the relative acceleration equals minus Riemann fed the velocity, the separation, and the velocity again. Say 'R upper theta, lower phi theta phi equals sine squared theta' as: on the sphere, the curvature component that carries the phi direction around the theta-phi plane and reads the theta change equals sine squared of the colatitude. Read indices aloud only when the learner is computing components.

## Sources

- schutz ch05 (mention): p.138 §5.6
- schutz ch06 (core): p.156 §6.5, p.157 §6.5, p.158 §6.5, p.160 §6.5
- gifted-amateur ch06 (mention): p.67, p.75 §6.3
- gifted-amateur ch11 (core): p.120, p.123 §11.2, p.125 §11.3, p.126 §11.4, p.128 §11.6, p.130
- gifted-amateur ch13 (revisited): p.142 §13.1
- gifted-amateur ch30 (revisited): p.319 §30.6
- gifted-amateur ch34 (mention): p.352 §34.1, p.358 §34.4
- gifted-amateur ch35 (revisited): p.363 §35.1, p.366 §35.2, p.367 §35.2
- gifted-amateur ch36 (revisited): p.374 §36.1, p.376 §36.1, p.377 §36.1, p.380 §36.4
- dinverno ch06 (core): p.94 §6.5, p.95 §6.5, p.98 §6.7, p.105 §6.12
- dinverno ch09 (mention): p.166 §9.6
- dinverno ch10 (revisited): p.174 §10.3, p.181 §10.6, p.183 §10.7
- legacy manuscript-chapter-08-curvature-holonomy (core)
- legacy manuscript-section-8-1-8-3-riemann-commutator-and-loop (developed)
- legacy manuscript-section-8-4-8-6-flatness-count-sphere-curvature (developed)

## Review

**Verdict:** accurate

**Fixes**

- Changed the working level's 'assumes' entry from holonomy to path-dependence-of-parallel-transport. The holonomy note lists Riemann as a prerequisite, so the old entry created a cycle.
- Checked every sign and convention entry against the reading copies. The component formulas (SCH 6.63, GA 11.19, DIV 6.40 after reordering Gamma's lower indices) define the same tensor as the course. The commutators (SCH 6.77, GA 35.13, DIV 6.39/6.41) agree, and so do the geodesic-deviation forms (SCH 6.87, GA 11.6/11.39, DIV ch10). The GA ch13 margin sign slip and Schutz's p.158 convention footnote are both real.
- Worked all checks: polar-plane R^r_{theta r theta} = -1 + 1 = 0; sphere R^theta_{phi theta phi} = sin^2 theta, K = 1/a^2, R = 2/a^2; tidal eigenvalues (-2, 1, 1) GM/r^3; Earth g/R_E = 1.5e-6 s^-2; horizon tide of a 10 solar-mass black hole about 1e8 s^-2; Kretschmann 3/(4M^4) at r = 2M; GW arm change 2e-18 m. All are correct.

**Concerns**

- The note is very long (about 70 KB). Tutors may need to retrieve it section by section.
- Prerequisites add path-dependence-of-parallel-transport beyond the registry; sync the registry.
