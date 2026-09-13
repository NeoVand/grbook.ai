---
type: "concept"
id: "ricci-scalar"
title: "Ricci scalar"
domain: "curvature"
tier: "core"
aliases: ["scalar curvature", "curvature scalar", "R"]
prerequisites: ["ricci-tensor", "inverse-metric"]
leads_to: ["einstein-tensor", "einstein-hilbert-action", "curvature-of-the-two-sphere", "curvature-of-the-flrw-metric", "trace-reversed-einstein-equations", "weyl-tensor"]
sources: ["dinverno:ch06", "gifted-amateur:ch11", "gifted-amateur:ch13", "gifted-amateur:ch36", "legacy:design-doc-misconception-diagnostics", "legacy:lesson-a-curved-universe-capstone", "legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature", "schutz:ch06", "schutz:ch07"]
review: "fixed"
---

# Ricci scalar

> The Ricci scalar is the single number left after tracing the Ricci tensor with the inverse metric, so every observer and every coordinate system agrees on its value at a point. For a sphere of radius a it equals 2 over a squared, twice the Gaussian curvature, and in four-dimensional spacetime Einstein's equation fixes it locally by the trace of the matter's energy-momentum. It is a handy but very incomplete curvature detector: it vanishes outside every black hole and throughout a radiation-filled universe, both of which are curved.

## Explanations by level

### Intuition

Picture an ant on a surface that marks out a small circle by walking the same short distance from a centre point in every direction, then measures the circle's circumference. On a flat table the circumference is exactly two pi times the radius. On a globe it comes out a little short, and on a saddle or a potato-crisp shape it comes out a little long. The Ricci scalar packages that shortfall or excess into one number for each point: positive on the globe, negative on the saddle, zero on the table. Because it is built only from distances measured on the surface, the ant needs no map and no outside view, and any two ants using different maps get the same number. A smaller globe bends more sharply, so its number is larger. For a two-dimensional surface this one number tells the whole story of curvature at a point. For three-dimensional space and four-dimensional spacetime it is only a grand total over many directions, and very different curvatures can total zero: the space around a black hole has a Ricci scalar of zero even though its tides can tear things apart. Its sign is also partly a naming convention in spacetime.

**Picture to hold:** Small circles drawn on a globe, a table and a saddle, each with its measured circumference compared against two pi times the radius, and a colour showing positive, zero or negative scalar curvature.

**Assumes:** [[curvature]], [[intrinsic-geometry]], [[circumference-to-radius-test]]

### Working

Contract the Ricci tensor with the inverse metric: R = g^{mu nu} R_{mu nu}, which amounts to tracing the Riemann tensor twice. The inverse metric is essential; summing diagonal components of R_{mu nu} is wrong except in an orthonormal frame with a Euclidean metric. For a sphere of radius a, R_{theta theta} = 1 and R_{phi phi} = sin^2 theta, and with g^{theta theta} = 1/a^2 and g^{phi phi} = 1/(a^2 sin^2 theta) you get R = 1/a^2 + 1/a^2 = 2/a^2, the same everywhere on the sphere. In two dimensions R = 2K, where K is the Gaussian curvature, and a small geodesic circle of radius s has circumference 2 pi s (1 - R s^2/12 + ...). A space of constant curvature K in n dimensions has R = n(n-1)K: 6/a^2 for a 3-sphere of radius a, 12K in four dimensions. Because R is a scalar, its value does not change between coordinate and orthonormal frames, even though Ricci components do. In spacetime, tracing Einstein's equation G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu} with g^{mu nu} (using g^{mu nu} g_{mu nu} = 4) gives R = 4 Lambda - 8 pi G T. For a perfect fluid T = -rho + 3p, so R = 8 pi G (rho - 3p) + 4 Lambda: positive for dust, zero for radiation, 4 Lambda for pure vacuum energy. For the FLRW universe R = 6(a''/a + (a'/a)^2 + k/a^2). Outside a star or black hole R = 0, yet the Kretschmann scalar is 48 M^2/r^6, so R = 0 does not mean flat.

**Picture to hold:** A trace machine: feed in the Ricci tensor and the inverse metric, get out one invariant number per event, with calibration cards (sphere 2/a^2, dust 8 pi G rho, radiation 0, Schwarzschild 0).

**Assumes:** [[ricci-tensor]], [[inverse-metric]], [[gaussian-curvature]], [[scalar-invariant]], [[einstein-field-equations]]

### Formal

The Ricci scalar of a (pseudo-)Riemannian manifold (M, g) with its Levi-Civita connection is the smooth function R = g^{mu nu} R_{mu nu}, with R_{mu nu} = R^rho_{mu rho nu} in the course convention and signature (-,+,+,+). It is a (0,0) tensor, hence invariant under diffeomorphisms, and in any chart it depends on g, its first derivatives and linearly on its second derivatives. Under g -> -g it changes sign; under a constant rescaling g -> c^2 g it scales as R -> R/c^2, so it carries units of inverse length squared. Geometric meaning on a Riemannian manifold: the volume of a small geodesic ball of radius r obeys Vol = omega_n r^n [1 - R r^2/(6(n+2)) + O(r^4)], so R measures the leading-order deficit of volume relative to flat space. Dimension dependence: for n = 2, R_{mu nu rho sigma} = (R/2)(g_{mu rho} g_{nu sigma} - g_{mu sigma} g_{nu rho}) and the Einstein tensor vanishes identically; for n = 3 the trace of the Einstein tensor is -R/2; for n = 4 it is -R. A space of constant curvature, R_{mu nu rho sigma} = K(g_{mu rho} g_{nu sigma} - g_{mu sigma} g_{nu rho}), has R = n(n-1)K; an Einstein space R_{mu nu} = lambda g_{mu nu} with n > 2 has constant R = n lambda by the contracted Bianchi identity nabla_mu R^mu_nu = (1/2) nabla_nu R. Constant R is necessary but not sufficient for maximal symmetry. Under a conformal change of a 3-metric gamma = psi^4 hat-gamma, R = psi^{-4} hat-R - 8 psi^{-5} hat-D^2 psi, which makes the Hamiltonian constraint an elliptic equation for psi. R is the Lagrangian density of the Einstein-Hilbert action S = (1/16 pi G) integral (R - 2 Lambda) sqrt(-g) d^4x, whose metric variation yields G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu}. Linearized about flat space, g = eta + h, it reads R = d_mu d_nu h^{mu nu} - Box h. As a curvature detector R is weak: it vanishes for all Ricci-flat spacetimes, and even the full set of polynomial curvature invariants vanishes for plane gravitational waves.

**Picture to hold:** One invariant function on spacetime sitting at the bottom of a ladder Riemann -> Ricci -> R, where each step keeps less information, and feeding upward into the Einstein-Hilbert action.

**Assumes:** [[ricci-tensor]], [[inverse-metric]], [[contracted-bianchi-identity]], [[space-of-constant-curvature]], [[einstein-hilbert-action]], [[conformally-related-metrics]]

## Prerequisites

- [[ricci-tensor]] — The Ricci scalar is the metric trace of the Ricci tensor.
- [[inverse-metric]] — Tracing a two-index covariant tensor requires g^{mu nu}.

## Leads to

- [[einstein-tensor]] — The Einstein tensor subtracts half the Ricci scalar times the metric from Ricci.
- [[einstein-hilbert-action]] — The gravitational Lagrangian density is sqrt(-g) R.
- [[curvature-of-the-two-sphere]] — The sphere's R = 2/a^2 is the standard worked value and calibration.
- [[curvature-of-the-flrw-metric]] — R = 6(a''/a + H^2 + k/a^2) summarises spacetime curvature of the expanding universe.
- [[trace-reversed-einstein-equations]] — Tracing the field equation gives R = 4 Lambda - 8 pi G T, the step used to trace-reverse.
- [[weyl-tensor]] — The scalar appears in the terms removed from Riemann to leave the Weyl tensor.

## Related

- [[gaussian-curvature]] — In two dimensions R = 2K.
- [[kretschmann-scalar]] — A different curvature invariant that stays non-zero where R vanishes, used to locate genuine singularities.
- [[scalar-invariant]] — R is the simplest curvature scalar and the prototype of a coordinate-independent diagnostic.
- [[space-of-constant-curvature]] — Constant curvature K gives R = n(n-1)K.
- [[contracted-bianchi-identity]] — Relates the divergence of Ricci to the gradient of R.
- [[circumference-to-radius-test]] — The circle circumference deficit measures R/12 in two dimensions.
- [[coordinate-singularity]] — Invariants like R distinguish coordinate artefacts from curvature, with limits.
- [[trace-of-stress-energy-tensor]] — In four dimensions R is fixed locally by T.
- [[de-sitter-spacetime]] — Pure vacuum energy gives constant R = 4 Lambda = 12 H^2.
- [[hamiltonian-constraint]] — The scalar curvature of a spatial slice enters the constraint on initial data.
- [[curvature-sign-conventions]] — The sign of R flips with the metric signature and with the Riemann or Ricci sign choice.

## Key equations

### Definition

$$
R = g^{\mu\nu}R_{\mu\nu} = g^{\mu\nu}g^{\alpha\beta}R_{\alpha\mu\beta\nu}
$$

Trace the Ricci tensor with the inverse metric; equivalently a double contraction of Riemann. The result is a scalar field. *(SCH ch06 §6.6 Eq. 6.92 p.162; GA ch11 §11.5 eqn 11.27 p.127; DIV ch06 §6.12 (6.85) p.106)*

**Convention:** Signature (-,+,+,+) and Ricci on the first and third Riemann slots; in (+,-,-,-) the same spacetime has the opposite sign of R.

### Sphere of radius a

$$
R = g^{\theta\theta}R_{\theta\theta} + g^{\phi\phi}R_{\phi\phi} = \frac{1}{a^2} + \frac{\sin^2\theta}{a^2\sin^2\theta} = \frac{2}{a^2}
$$

Constant over the sphere and larger for smaller spheres; the same value in orthonormal and coordinate frames. *(GA ch11 Example 11.8 eqn 11.36 p.128; GA ch36 Example 36.4 p.381; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*

**Convention:** A positive-definite metric: the value is +2/a^2 in all three books.

### Two dimensions: scalar curvature and Gaussian curvature

$$
R = 2K,\qquad R_{\mu\nu\rho\sigma} = \frac{R}{2}\left(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}\right),\qquad C(s) = 2\pi s\left(1 - \frac{R\,s^2}{12} + \dots\right)
$$

On a surface one number fixes the whole curvature tensor; the circumference of a small geodesic circle falls short of 2 pi s by an amount set by R. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; GA ch36 Example 36.4 p.381)*

**Convention:** K here is Gaussian curvature, not the Kretschmann scalar or a tidal matrix.

### Constant curvature in n dimensions

$$
R_{\mu\nu} = (n-1)K\,g_{\mu\nu},\qquad R = n(n-1)K\quad(\;{}^{(3)}R = 6K,\ \ R_{4D} = 12K\;)
$$

A maximally symmetric space is summarised by one constant; the factor grows with dimension. *(GA ch16 §16.1 eqn 16.4 p.170; DIV ch25 §25.9 (25.57) p.527; GA ch49 §49.7 eqn 49.48 p.540)*

**Convention:** d'Inverno writes K = R/12 in four dimensions with signature (+,-,-,-), so its de Sitter K and R are negative; in the course de Sitter has K = H^2 > 0.

### Trace of Einstein's equation

$$
R = 4\Lambda - 8\pi G\,T,\qquad T = g^{\mu\nu}T_{\mu\nu} = -\rho + 3p\ \text{(perfect fluid)}
$$

In four dimensions the scalar curvature at an event is set algebraically by the local trace of energy-momentum: 8 pi G rho for dust, zero for radiation, 4 Lambda for vacuum energy. *(GA ch13 Example 13.5 p.148; GA ch13 §13.4 p.148; legacy:lesson-a-curved-universe-capstone)*

**Convention:** Gifted Amateur writes R = -8 pi G T with Lambda = 0. Restore c^4 in 8 pi G/c^4.

### FLRW scalar curvature

$$
R = 6\left(\frac{\ddot a}{a} + \frac{\dot a^2}{a^2} + \frac{k}{a^2}\right)
$$

Spacetime curvature of the expanding universe; non-zero even when k = 0, so a spatially flat universe is not flat spacetime. *(GA ch15 Example 15.3 eqn 15.27 p.165; GA ch16 §16.1 p.171; GA ch16 §16.2 p.174; GA ch36 Example 36.5 p.383)*

**Convention:** Gifted Amateur's margin prints 2k/a in the spatial Ricci component; the correct 2k/a^2 is needed for this trace.

### Contracted Bianchi identity

$$
\nabla_\mu R^\mu{}_\nu = \tfrac12\,\nabla_\nu R
$$

Twice the divergence of Ricci is the gradient of the scalar curvature; this is what makes R_{mu nu} - (1/2) R g_{mu nu} divergence-free. *(GA ch13 §13.3 eqn 13.29 p.146; SCH ch06 §6.6 Eq. 6.97 p.163)*

### Einstein-Hilbert action

$$
S = \frac{1}{16\pi G}\int (R - 2\Lambda)\sqrt{-g}\,d^4x + S_{\mathrm{matter}}
$$

The scalar curvature, weighted by the invariant volume element, is the simplest gravitational Lagrangian; varying the metric gives Einstein's equation. *(GA ch40 §40.4 eqn 40.36 p.434; DIV ch13 §13.3 (13.7) p.220; legacy:manuscript-chapter-14-einstein-hilbert-action)*

**Convention:** d'Inverno, in (+,-,-,-), writes the density (R + 2 Lambda) sqrt(-g) + 2 kappa L_M; the flipped sign of R is matched by its matter Lagrangian convention. In SI with x^0 = ct the prefactor is c^3/(16 pi G).

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Sign of R for Lorentzian spacetimes (signature dependence) | (-,+,+,+) with MTW Riemann and Ricci (ch06 §6.6 p.162); a sphere has positive R. | (-,+,+,+); de Sitter has K = +1/alpha^2 and R > 0 (ch49 §49.7 p.540). | (+,-,-,-). Same Riemann and Ricci conventions, so R = g^ab R_ab has the opposite sign for the same spacetime (dust gives R < 0); ch25 relates K = R/12 but labels the positive-K case de Sitter, inconsistent with its own signature (p.527). | (-,+,+,+): dust R = +8 pi G rho, de Sitter R = +4 Lambda. Quote the signature whenever a sign of R is stated. |
| Name and symbol clashes | 'Ricci scalar' R (Eq. 6.92); in cosmology R(t) is the scale factor (ch13 §13.2 p.423). | 'Ricci scalar' R; scale factor a(t); in ch21 R also names an areal-radius function and a stellar radius. | 'curvature scalar or Ricci scalar' R (6.85); R(t) is the scale factor in ch24-26, overloaded with the Ricci scalar in §25.9. | R is reserved for the Ricci scalar; the scale factor is a(t); spatial scalar curvature is written ^(3)R. |
| Trace relation between R and matter | Not written out in the cited Schutz units; its (-,+,+,+) signature and MTW curvature conventions give the course relation and dust R > 0. | R = -8 pi G T with signature (-,+,+,+), so dust (T = -rho) has R = +8 pi G rho (ch13 §13.4 p.148). | Field equations G_ab = 8 pi T_ab with (+,-,-,-): the same trace relation holds, but dust has T = +rho, giving R = -8 pi rho (G = 1). | R = 4 Lambda - 8 pi G T with T = -rho + 3p for a perfect fluid. |
| Sign of the Lambda term in the Lagrangian density | No action principle in the Schutz units cited for this concept. | S_EH = integral d^4x sqrt(-g) R (eqn 40.36 p.434), without a Lambda term in that equation. | L = (R + 2 Lambda) sqrt(-g) + 2 kappa L_M (13.7 p.220), matching its G_ab - Lambda g_ab = 8 pi T_ab. | (1/16 pi G)(R - 2 Lambda) sqrt(-g), matching G + Lambda g = 8 pi G T. |
| Sign of the induced spatial metric used for the scalar curvature of a slice | Uses a positive-definite 3-metric and the trace of the 3D Einstein tensor, G = -R/2, to impose constant curvature (ch13 §13.2 p.424). | Positive-definite spatial metric gamma: ^(3)R = 6K for a constant-curvature 3-space (ch16 eqn 16.4 p.170). | The induced metric h_ab inherits the negative spatial signs of (+,-,-,-); switching to gamma = -h flips ^(3)R, and the dossier flags a resulting sign inconsistency in the Hamiltonian constraint (ch14 §14.4 p.244, §14.11 p.254). | Always compute ^(3)R with the positive-definite induced metric gamma_ij: a 3-sphere of radius a has ^(3)R = 6/a^2, and the Hamiltonian constraint reads ^(3)R + (K^i_i)^2 - K_ij K^ij = 16 pi G rho. |
| Which trace formula is displayed | Trace of Ricci with the inverse metric, also displayed as a double contraction of the all-lower Riemann tensor (Eq. 6.92). | R = g^{mu nu} R_{mu nu} in ch11 (eqn 11.27) and R = g_{mu nu} R^{mu nu} in ch13 (eqn 13.7); equivalent. | R = g^ab R_ab (6.85). | R = g^{mu nu} R_{mu nu}; any placement works provided one index is up and one down in each contracted pair. |

## How the sources teach it

### schutz

**Route:** Defines the scalar in one line right after the Ricci tensor, also as a double contraction of Riemann, and uses it immediately when contracting the Bianchi identities twice to reach the Einstein tensor. In ch07 the scalar reappears as the ingredient of a rival conservation law that agrees with special relativity yet would let curvature create particles, illustrating why the equivalence principle needs care. Later (ch13) a constant curvature scalar is imposed on a spherically symmetric 3-metric to derive the homogeneous cosmological spatial metric.

**Representation:** Component definitions and index manipulation in ch06; physical arguments in ch07; a derivation reusing stellar-structure formulas in ch13.

**Strengths:** Shows R as a working part of the divergence-free Einstein tensor, and the ch13 derivation is an elegant use of a single scalar condition.

**Weaknesses:** No geometric meaning or worked value appears where R is defined (the sphere value is left to the reader), and the ch13 claim that a constant scalar suffices for homogeneity is not proven. *(SCH ch06 §6.6 Eq. 6.92 p.162; SCH ch06 §6.6 p.163; SCH ch07 §7.1 p.173; SCH ch13 §13.2 p.424)*

### gifted-amateur

**Route:** Introduces the scalar in ch11 as a further contraction of Ricci, reminding readers that the metric must be used for a trace, and computes the sphere's value 2/a^2. Ch13 recaps it, shows that the rejected Ricci-equals-matter guess would force R to be constant, and traces the correct field equation to get R = -8 pi G T. Ch15 and ch36 compute R for the expanding universe and stress that it is the same in orthonormal and coordinate frames. Ch26 uses invariants to show a horizon is not a curvature singularity, and ch40 makes R the Lagrangian of the Einstein-Hilbert action.

**Representation:** Worked component calculations, orthonormal frames and Cartan forms, trace manipulations, and margin reference tables.

**Strengths:** Concrete values early, explicit frame independence, and the trace trick that makes vacuum and radiation cases immediate.

**Weaknesses:** Does not connect 2/a^2 to Gaussian curvature, angle excess or circle deficits; the printed Robertson-Walker Ricci component carries a 2k/a typo; the warning that R = 0 does not mean flat is left implicit. *(GA ch11 §11.5 p.127; GA ch11 Example 11.8 p.128; GA ch13 §13.3 p.146; GA ch13 Example 13.5 p.148; GA ch15 Example 15.3 p.164; GA ch36 Example 36.4 p.381; GA ch26 §26.1 p.273; GA ch40 §40.4 p.434)*

### dinverno

**Route:** Ch06 names it 'curvature scalar or Ricci scalar' in one line as the final contraction before defining the Einstein tensor. The scalar then serves many later purposes: the Lagrangian with cosmological term in ch13, the conformal transformation of a slice's scalar curvature in the ch14 initial-data method, a coordinate-independent test of singularities in ch17, and the constant-curvature relation K = R/12 in ch25.

**Representation:** Terse boxed definitions, variational formulae, and invariant-based arguments.

**Strengths:** Shows the breadth of roles one scalar plays, from actions to numerical-relativity initial data and singularity diagnosis.

**Weaknesses:** No geometric meaning or example value in ch06; the (+,-,-,-) signature gives signs of R opposite to most modern texts; R collides with the scale factor R(t); sign slips appear for the de Sitter constant and for ^(3)R with the flipped induced metric. *(DIV ch06 §6.12 p.106; DIV ch13 §13.3 p.220; DIV ch14 §14.12 p.258; DIV ch17 §17.2 p.323; DIV ch25 §25.9 p.527)*

### legacy

**Route:** The earlier course computes the sphere's Ricci tensor and scalar, uses R = 2/a^2 to fix the sign convention, and shows the circumference deficit of geodesic circles. Its Ricci/Weyl chapter states the one-way implication chain Riemann = 0 implies Ricci = 0 implies R = 0. A diagnostic task contrasts N(z) = 1 + az/c^2 (flat) with N = e^{kz} (R = -2k^2), and the cosmology capstone gives R = 4/(3t^2) for dust while the radiation model has R = 0 yet is curved. A calculation checklist uses calibration geometries with known R.

**Representation:** Worked derivations, calibration tables, predict-then-check diagnostics and a multi-stage capstone project.

**Strengths:** Treats R as a tool with explicit limits, supplies memorable counterexamples, and ties values to checkable numbers.

**Weaknesses:** The geodesic-ball interpretation in higher dimensions is not given; the invariants discussion is split across chapters. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; legacy:manuscript-chapter-09-ricci-weyl-einstein; legacy:design-doc-misconception-diagnostics; legacy:lesson-a-curved-universe-capstone; legacy:manuscript-section-24-3-calculation-checklist; legacy:manuscript-section-10-curvature-invariants-and-summary-table)*

## Recommended teaching path

1. **1. Motivating question** — Ask: can a surface-bound ant, with only a tape measure, find one number telling how curved its world is at a point? Let the learner predict what happens to the circumference of a small circle on a globe and on a saddle. *Why:* An operational, coordinate-free test gives the scalar a meaning before its formula, and it fills the gap left by books that never link R to measurements. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature; GA ch11 §11.6 p.128)*
2. **2. Picture** — Use the surface explorer to draw geodesic circles on a sphere, paraboloid, saddle and cylinder, reading the circumference deficit and the colour-coded R = 2K. Close by tying the deficit to the loop picture: on a surface a vector carried around a small loop turns by the enclosed area times R/2. *Why:* Seeing that the cylinder reads zero and the saddle reads negative fixes intrinsic meaning and sign in one session. *(GA ch36 Ex 36.4 p.385; legacy:scene-3d-parallel-transport-loop; legacy:manuscript-chapter-08-curvature-holonomy)*
3. **3. Formalism: trace with the inverse metric** — Define R = g^{mu nu} R_{mu nu}, compute the sphere value 2/a^2 from the Ricci components, and redo it in an orthonormal frame to show the scalar does not change while components do. *Why:* Combines the calculation learners must be able to do with the idea of invariance, and pre-empts the error of summing diagonal components. *(GA ch11 Example 11.8 p.128; GA ch36 Example 36.4 p.381; SCH ch06 §6.6 p.162)*
4. **4. Check: dimension and constant curvature** — Derive R = 2K in two dimensions, then R = n(n-1)K for constant curvature (6/a^2 for a 3-sphere, 12K in four dimensions). Have the learner compute R at the tip of a paraboloid. *Why:* Prevents the belief that R equals Gaussian curvature in general and builds a stock of reference values. *(GA ch16 §16.1 p.170; DIV ch25 §25.9 p.527; GA ch36 Ex 36.4 p.385)*
5. **5. Spacetime: matter fixes R** — Trace Einstein's equation to R = 4 Lambda - 8 pi G T. Tabulate dust, radiation, vacuum energy; compute R(t) for a matter-dominated universe and confirm R = 8 pi G rho. *Why:* Shows R's physical content in four dimensions and gives immediate, checkable numbers. *(GA ch13 Example 13.5 p.148; GA ch15 Example 15.3 p.164; legacy:lesson-a-curved-universe-capstone)*
6. **6. Limits of a single number** — Show three curved spacetimes with R = 0 (Schwarzschild exterior, radiation FLRW, a plane wave) and one position-dependent clock rate that is flat (N = 1 + az) versus one that is curved (N = e^{kz}, R = -2k^2). Introduce the Kretschmann scalar as a complementary invariant. *Why:* Blocks the 'R = 0 means flat' slogan and teaches that invariants, not metric components, decide curvature, while no single invariant decides everything. *(legacy:design-doc-misconception-diagnostics; GA ch26 §26.1 p.273; DIV ch17 §17.2 p.323; legacy:manuscript-section-10-curvature-invariants-and-summary-table)*
7. **7. Application: the action** — Present the Einstein-Hilbert action as the spacetime integral of R, and note the contracted Bianchi identity that makes R_{mu nu} - (1/2) R g_{mu nu} conserved. *Why:* Connects the scalar to the field equations from a second direction and motivates why the trace term in the Einstein tensor has the coefficient one half. *(GA ch40 §40.4 p.434; DIV ch13 §13.3 p.220; SCH ch06 §6.6 p.163)*

## Analogies

- **Flattening a paper disc onto a curved surface** (intuition): Press a flat paper disc onto a ball and its rim has too much paper, so it crumples; press it onto a saddle and its rim has too little, so it tears. The Ricci scalar measures that mismatch between the surface's small circles and flat ones. *Limits:* The paper picture uses an outside, extrinsic view of what is an intrinsic quantity; in four-dimensional spacetime there are no such circles to press, and there R also has a convention-dependent sign. *(legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature)*
- **A thermometer reading versus the full weather map** (intuition): The Ricci scalar is like the temperature at a point: one number everyone agrees on. The Riemann tensor is the whole weather map with winds and pressures in every direction. Very different weather can share the same temperature. *Limits:* Unlike temperature, R can be negative, is not an average of anything physical in general, and a zero reading says nothing about how violent the 'weather' (tides) is. *(legacy:manuscript-chapter-09-ricci-weyl-einstein)*
- **The bottom line of a set of accounts** (working): Riemann lists every curvature entry, Ricci subtotals them by row, and R is the final bottom line. A bottom line of zero can hide large, cancelling entries, as in the Schwarzschild curvature table. *Limits:* The entries are combined with metric signs that depend on the signature, and some information (the Weyl part) is lost already at the Ricci stage, not only at the last step. *(legacy:lesson-contract-curvature-by-hand)*

## Misconceptions

- **If the Ricci scalar is zero, spacetime is flat.** — Riemann = 0 implies Ricci = 0 implies R = 0, with no converse. The Schwarzschild exterior, a radiation-dominated universe and gravitational plane waves all have R = 0 but non-zero Riemann curvature. *Why tempting:* A single invariant called 'the curvature scalar' sounds like it should capture curvature, and on two-dimensional surfaces it does. *Diagnostic:* A radiation-dominated universe has a(t) proportional to t^(1/2). Compute R. Is this spacetime flat? *(legacy:manuscript-chapter-09-ricci-weyl-einstein; legacy:lesson-a-curved-universe-capstone; legacy:practice-set-misconception-checks)*
- **Because Ricci components change between orthonormal and coordinate frames, the Ricci scalar changes too.** — Components change by frame factors (on a sphere, 1/a^2 in an orthonormal frame versus 1 and sin^2 theta in coordinates), but the full trace R is a scalar and is identical in every frame. *Why tempting:* After watching many curvature numbers change with the frame, learners generalise to all of them. *Diagnostic:* On a sphere, R_{theta-hat theta-hat} = 1/a^2 in the orthonormal frame and R_{theta theta} = 1 in coordinates. What is R in each frame? *(GA ch36 §36.4 p.382)*
- **You can get R by adding the diagonal components of R_{mu nu}.** — The trace needs the inverse metric: R = g^{mu nu} R_{mu nu}. Only in an orthonormal frame of a positive-definite metric does it reduce to a plain sum; in spacetime the time component enters with a minus sign. *Why tempting:* In linear algebra a trace is the sum of diagonal entries. *Diagnostic:* For the sphere, adding R_{theta theta} + R_{phi phi} gives 1 + sin^2 theta. Why is that not the scalar curvature, and what is? *(GA ch11 §11.5 p.127; GA ch11 Example 11.8 p.128)*
- **A space with the same Ricci scalar everywhere must be homogeneous or maximally symmetric.** — Constant R is necessary for maximal symmetry but not sufficient. Schwarzschild has R = 0 everywhere and is not homogeneous; Einstein spaces with R_{mu nu} = lambda g_{mu nu} need not have constant curvature. *Why tempting:* Deriving the FLRW spatial metric by imposing a constant curvature scalar suggests the condition is enough by itself. *Diagnostic:* Schwarzschild spacetime has R = 0 at every point. Does it look the same at every point? *(SCH ch13 §13.2 p.424)*
- **The Ricci scalar equals the Gaussian curvature, or R = 2K in every dimension.** — R = 2K only in two dimensions. A space of constant sectional curvature K has R = n(n-1)K: 6K in three dimensions and 12K in four. *Why tempting:* The sphere example is two-dimensional and the factor 2 looks universal. *Diagnostic:* A 3-sphere of radius a has sectional curvature 1/a^2 in every plane. What is its Ricci scalar? *(GA ch16 §16.1 eqn 16.4 p.170; DIV ch25 §25.9 p.527)*
- **Position-dependent clock rates, or metric components that vary or blow up, prove the spacetime is curved or singular.** — Only invariants decide. The metric -(1 + az)^2 dt^2 + dz^2 has varying clock rates but R = 0 and is flat (Rindler); -e^{2kz} dt^2 + dz^2 has R = -2k^2. Schwarzschild components blow up at r = 2M while invariants stay finite there. *Why tempting:* Gravitational time dilation is often introduced as the signature of gravity. *Diagnostic:* For ds^2 = -N(z)^2 dt^2 + dz^2 one finds R = -2N''/N. Which of N = 1 + az and N = e^{kz} is curved? *(legacy:design-doc-misconception-diagnostics; DIV ch17 §17.2 p.323; GA ch26 §26.1 p.273)*
- **Reaching a constant Ricci scalar is by itself what rules out the Ricci-equals-matter field equation.** — A constant R is not unphysical. The problem is that the guess ties R to the trace of T, so the trace of T would have to be the same everywhere, which real matter distributions violate. *Why tempting:* The derivation arrives at 'R is constant' first, which looks like the punchline. *Diagnostic:* Under the guess R_{mu nu} = kappa T_{mu nu}, what would a constant R imply about the matter density inside and outside a star? *(GA ch13 §13.3 p.146)*

## Thought experiments

- **A rival law in which curvature creates particles**: Replace ordinary conservation of particle number by a law whose divergence equals a constant times the square of the Ricci scalar. In flat spacetime R = 0, so the law agrees with every special-relativistic experiment. *Lesson:* Laws that differ only by curvature terms cannot be told apart by flat-spacetime physics; choosing the minimal coupling is an extra physical assumption, and R is the simplest curvature scalar such terms could use. *(SCH ch07 §7.1 p.173)*

## Visualizations

### Scalar curvature surface explorer · interactive-3d · high priority

A gallery of surfaces (sphere, paraboloid, saddle, torus, pseudosphere, cylinder) coloured by R = 2K. The learner drops a small geodesic circle anywhere and compares its measured circumference and area with flat values.

**Interaction:** Learner picks a surface, adjusts its parameters (sphere radius, paraboloid steepness, torus radii), and drags a circle centre and radius. Readouts: exact R at the centre, circumference deficit 1 - C/(2 pi s), and the estimate R_est = 12(1 - C/(2 pi s))/s^2 converging to R as s shrinks.

**Model:** Gaussian curvature from each surface's metric (sphere 1/a^2; paraboloid z = a r^2/2 gives K = a^2/(1 + a^2 r^2)^2; torus K = cos v/(r(R0 + r cos v)); pseudosphere -1/c^2); geodesic circles by integrating geodesics from the centre; C(s) = 2 pi s(1 - K s^2/6 + ...).

**Inspired by:** GA ch36 Ex 36.4 p.385; GA ch11 Example 11.8 p.128; legacy:manuscript-section-8-4-8-6-flatness-count-sphere-curvature

**Legacy assets:** scene-3d-parallel-transport-loop, manuscript-section-8-4-8-6-flatness-count-sphere-curvature

### Invariants versus coordinate artefacts · interactive-plot · medium priority

Metric cards (polar plane, Rindler, N = e^{kz}, Schwarzschild in Schwarzschild and ingoing coordinates, a plane wave) with plots of metric components and of R and the Kretschmann scalar along a line.

**Interaction:** Learner switches card and chart. Metric components spike or vary between charts while R and Kretschmann curves stay identical; the Schwarzschild card shows R = 0 everywhere while Kretschmann rises as 48 M^2/r^6; the plane-wave card shows both invariants at zero despite non-zero curvature components.

**Model:** Closed-form or finite-difference curvature from each metric: R = -2N''/N for the 2D lapse metrics; Schwarzschild R = 0, Kretschmann 48 M^2/r^6; plane wave all polynomial invariants zero.

**Inspired by:** GA ch26 §26.1 p.273; DIV ch17 §17.2 p.323; legacy:design-doc-misconception-diagnostics

**Legacy assets:** engine-independent-curvature-checker, manuscript-section-10-curvature-invariants-and-summary-table

### What sets R? A source picker · interactive-2d · medium priority

Choose a mix of dust, radiation, stiff matter and vacuum energy; the panel shows T, its trace, R = 4 Lambda - 8 pi G T, and a plot of R(t) for the corresponding flat FLRW history.

**Interaction:** Learner adjusts component densities or picks a single fluid. Radiation drives R to zero while the expansion curve stays curved (a'' non-zero); vacuum energy pins R at 4 Lambda; dust gives R = 4/(3t^2).

**Model:** Perfect fluids with p = w rho, T = -rho + 3p; flat Friedmann evolution; R = 6(a''/a + H^2) compared with 4 Lambda - 8 pi G T at every time.

**Inspired by:** GA ch13 §13.4 p.148; GA ch15 Example 15.3 p.164; legacy:lesson-a-curved-universe-capstone

**Legacy assets:** lesson-a-curved-universe-capstone

## Worked examples

- **Scalar curvature of the sphere** (working): From Christoffel symbols to Riemann to Ricci, then the trace with g^{theta theta} = 1/a^2 and g^{phi phi} = 1/(a^2 sin^2 theta) gives R = 2/a^2, constant and growing as the sphere shrinks. *(GA ch11 Example 11.8 p.128)*
- **Same sphere, two frames** (working): Cartan's method in an orthonormal coframe gives Ricci components 1/a^2; converted to coordinates they become 1 and sin^2 theta, but the scalar is 2/a^2 either way. *(GA ch36 Example 36.4 p.381)*
- **Tracing the field equation** (working): Contracting with g^{mu nu} and using g^{mu nu} g_{mu nu} = 4 gives R = -8 pi G T, which lets the equation be rewritten with Ricci alone. *(GA ch13 Example 13.5 p.148)*
- **Scalar curvature of the flat expanding universe** (formal): Orthonormal-frame Ricci components combine to R = 6(a''/a + a'^2/a^2): flat spatial slices, curved spacetime. *(GA ch15 Example 15.3 p.164; GA ch36 Example 36.5 p.382)*
- **Homogeneous 3-spaces from a constant curvature scalar** (working): Setting the trace of the 3D Einstein tensor of a spherical 3-metric to a constant and requiring regularity at the centre yields the k = +1, 0, -1 spatial metrics. *(SCH ch13 §13.2 p.424)*
- **Constant-curvature spacetime** (working): Contracting R_abcd = K(g_ac g_bd - g_ad g_bc) gives R_bd = 3K g_bd and R = 12K, so maximal symmetry makes the spacetime a vacuum with a cosmological constant. *(DIV ch25 §25.9 p.527)*
- **A matter-dominated universe, end to end** (working): For a proportional to t^(2/3): R = 4/(3t^2), matching 8 pi G rho with rho = 1/(6 pi G t^2); the radiation model a proportional to t^(1/2) has R = 0 but is curved. *(legacy:lesson-a-curved-universe-capstone)*
- **Clock rates without curvature** (working): For ds^2 = -N(z)^2 dt^2 + dz^2 the scalar curvature is -2N''/N, so a linear N is flat and an exponential N is curved. *(legacy:design-doc-misconception-diagnostics)*
- **Kaluza-Klein reduction of the scalar curvature** (formal): The five-dimensional scalar curvature of a block metric splits into the four-dimensional one minus a quarter of the Maxwell invariant, so one action contains gravity and electromagnetism. *(GA ch48 Example 48.1 p.523)*

## Exercises

- (intro) Show that contracting the Einstein tensor with the metric gives minus the Ricci scalar. *Skill:* Tracing with the metric in four dimensions. *(GA ch13 Ex 13.3 p.150)*
- (standard) Find the metric of a sphere and its inverse, compute its Riemann tensor from the single 2D component, then contract to the scalar curvature. *Skill:* The full sphere calculation including the inverse metric. *(SCH ch06 Ex 6.28 p.167; SCH ch06 Ex 6.29 p.167)*
- (standard) Compute Riemann, Ricci and scalar curvature for a paraboloid-shaped surface and see where curvature is largest. *Skill:* Position-dependent scalar curvature on a surface. *(GA ch36 Ex 36.4 p.385)*
- (challenging) For a 2D metric whose coordinate lines meet at a variable angle, compute the curvature and show that constant scalar curvature leads to the sine-Gordon equation. *Skill:* Scalar curvature as a differential condition on a metric function. *(GA ch15 Ex 15.4)*
- (standard) From the Robertson-Walker metric, compute the scalar curvature of a constant-time slice and show it is 6k divided by the square of the scale factor. *Skill:* Spatial scalar curvature and the sign of k. *(DIV ch25 Ex 25.10)*
- (challenging) For the closed Robertson-Walker universe, find the curvature 2-forms, the Ricci scalar and the orthonormal Einstein components. *Skill:* Four-dimensional Cartan computation ending in R. *(GA ch36 Ex 36.7 p.385)*

## Checks for understanding

- **Q (intuition):** An ant walks out a small circle of radius 10 cm on a curved surface and finds its circumference slightly larger than 2 pi times 10 cm. Is the scalar curvature at the centre positive, negative or zero? What kind of surface might it be on?
  - **A:** Negative. A circumference larger than the flat value means small circles have 'extra room', which happens on saddle-shaped surfaces; on a globe it would be smaller (positive R), and on a flat sheet or a cylinder it would be exactly 2 pi s (R = 0).
- **Q (working):** Compute the Ricci scalar of a sphere of radius 2 m and of a sphere of radius 1 m. Why does the smaller sphere have the larger value?
  - **A:** R = 2/a^2 gives 0.5 m^-2 for a = 2 m and 2 m^-2 for a = 1 m. A smaller sphere turns more sharply over a given distance, so small circles fall shorter of 2 pi s; curvature scales as one over length squared.
- **Q (working):** A radiation-dominated flat universe has a(t) proportional to t^(1/2). Compute its Ricci scalar and decide whether spacetime is flat.
  - **A:** a'/a = 1/(2t) and a''/a = -1/(4t^2), so R = 6(a''/a + a'^2/a^2) = 6(-1/4 + 1/4)/t^2 = 0, consistent with T = -rho + 3p = 0 for radiation. Spacetime is not flat: a'' is non-zero, the Riemann components such as R^t-hat_{i-hat t-hat i-hat} proportional to a''/a do not vanish, and freely falling comoving observers decelerate apart. *(targets: If the Ricci scalar is zero, spacetime is flat.)*
- **Q (working):** For a matter-dominated flat universe a proportional to t^(2/3), find R(t) and check it against the trace of Einstein's equation with Lambda = 0.
  - **A:** a'/a = 2/(3t), a''/a = -2/(9t^2), so R = 6(-2/9 + 4/9)/t^2 = 4/(3t^2). The Friedmann equation H^2 = 8 pi G rho/3 gives rho = 1/(6 pi G t^2), and R = -8 pi G T = 8 pi G rho = 8/(6 t^2) = 4/(3t^2), in agreement.
- **Q (formal):** For the two-dimensional spacetime ds^2 = -N(z)^2 dt^2 + dz^2, the scalar curvature is R = -2N''/N. Which of N = 1 + az and N = e^{kz} describes a curved spacetime, and what does this say about using clock rates to detect curvature?
  - **A:** N = 1 + az has N'' = 0, so R = 0; in two dimensions that means the full curvature vanishes and the spacetime is flat (it is Rindler's accelerated frame). N = e^{kz} gives R = -2k^2, a genuinely curved spacetime. Both have position-dependent clock rates, so varying clock rates alone do not prove curvature; an invariant must be checked. *(targets: Position-dependent clock rates, or metric components that vary or blow up, prove the spacetime is curved or singular.)*
- **Q (formal):** Show that replacing g_{mu nu} by -g_{mu nu} changes the sign of R, and explain why d'Inverno's dust has R < 0 while the course's dust has R > 0.
  - **A:** Christoffel symbols, the mixed Riemann tensor and R_{mu nu} are unchanged by g -> -g, but R = g^{mu nu} R_{mu nu} contains one inverse metric, which flips. Physically the same trace relation R = -8 pi G T holds in both, but in (+,-,-,-) dust has T = +rho, giving R = -8 pi G rho, whereas in (-,+,+,+) T = -rho and R = +8 pi G rho.

## Applications

- **Einstein-Hilbert action and modified gravity**: sqrt(-g) R is the gravitational Lagrangian of general relativity; many alternative theories replace R by a function of R or add curvature-squared terms. Key numbers: Prefactor 1/(16 pi G) with c = 1, or c^3/(16 pi G) with x^0 = ct in SI *(GA ch40 §40.4 p.434; legacy:manuscript-chapter-14-einstein-hilbert-action)*
- **Telling coordinate from physical singularities**: Curvature invariants are the same in every chart. Where metric components blow up but invariants stay finite, the problem is the coordinates; R alone is insufficient in vacuum (it is zero), so the Kretschmann scalar is used. Key numbers: Schwarzschild: R = 0 everywhere; Kretschmann 48 M^2/r^6, equal to 3/(4 M^4) (finite) at r = 2M and divergent at r = 0 *(DIV ch17 §17.2 p.323; GA ch26 §26.1 p.273)*
- **Cosmology**: R(t) tracks how far the universe is from being a vacuum or radiation era; it vanishes in the radiation era and approaches 4 Lambda at late times, and a constant spatial scalar curvature characterises the homogeneous spatial slices. Key numbers: Dust: R = 4/(3t^2); de Sitter: R = 12 H^2 *(GA ch15 Example 15.3 p.164; SCH ch13 §13.2 p.424; legacy:lesson-a-curved-universe-capstone)*
- **Initial data for numerical relativity**: The scalar curvature of a spatial slice enters the Hamiltonian constraint; writing the slice metric as psi^4 times a background turns the constraint into an elliptic equation for psi. *(DIV ch14 §14.12 p.258; legacy:manuscript-section-20-2-constraints-and-dof)*

## Tutor guidance

**Opening questions**

- If you could measure only distances along a surface, how might you tell whether it is curved at a point?
- What would you expect the circumference of a small circle on a globe to be, compared with two pi times its radius?
- If one number summarised curvature at a point, what kinds of curvature might it miss?

**Common questions**

- *Why do I need the inverse metric? Isn't a trace just the sum of the diagonal?* — A trace pairs an upper index with a lower one. R_{mu nu} has two lower indices, so one must be raised with g^{mu nu} first. In an orthonormal Euclidean frame that reduces to adding diagonal entries; in coordinates or in spacetime it does not.
- *If R is invariant, why not use it to find black-hole singularities?* — Outside and inside a Schwarzschild black hole R is exactly zero, because the spacetime is Ricci-flat. It cannot see that curvature. The Kretschmann scalar R_{mu nu rho sigma} R^{mu nu rho sigma} = 48 M^2/r^6 does, staying finite at the horizon and diverging at r = 0.
- *What are the units of the Ricci scalar?* — Inverse length squared, like the 2/a^2 of a sphere. In SI with x^0 = ct, the trace equation reads R = 4 Lambda - (8 pi G/c^4) T, with T an energy density.
- *What does a negative Ricci scalar mean?* — On a surface or in space, small circles and balls have more circumference or volume than flat ones, as on a saddle or in hyperbolic space. In spacetime the sign depends on the signature convention and on the matter content, for example R = 8 pi G(rho - 3p) with Lambda = 0, which is negative for matter with p > rho/3.
- *Why is R a good Lagrangian for gravity?* — It is the simplest scalar built from the metric that contains second derivatives, and the second-derivative terms combine into a total divergence, so its variation gives second-order field equations: Einstein's equation.

**Pitfalls when explaining**

- Do not call R 'the curvature' of spacetime; call it one scalar summary and always pair 'R = 0' with 'not necessarily flat'.
- Do not state R = 2K outside two dimensions.
- State the signature when quoting a sign of R for a spacetime; d'Inverno's values have the opposite sign.
- Do not let the symbol R double as the scale factor in a lesson; use a(t).
- When computing, do not skip the inverse metric even when the Ricci tensor looks diagonal.

**When to show a demo**

- Open the surface explorer when introducing the concept: drop a circle on the sphere, then the saddle, then the cylinder to show R positive, negative and zero.
- After computing 2/a^2, use the explorer's radius slider to show R growing as the sphere shrinks.
- When discussing R = 0 versus flat, switch the source picker to pure radiation and show R(t) at zero while the expansion still decelerates.
- When discussing singularities, open the invariants demo on the Schwarzschild card to contrast R = 0 with the rising Kretschmann curve.

**Saying it aloud:** Say R = g^{mu nu} R_{mu nu} as 'R equals g upper mu nu times R lower mu nu: the Ricci tensor traced with the inverse metric'. Say the sphere value as 'two over a squared'. Say the trace equation as 'R equals four Lambda minus eight pi G times the trace of T'. Say the FLRW result as 'six times, a double-dot over a, plus a-dot over a squared, plus k over a squared'. Never read 'R' alone without saying 'Ricci scalar' the first time in a lesson.

## Sources

- schutz ch06 (developed): p.162 §6.6
- schutz ch07 (mention): p.173 §7.1
- gifted-amateur ch11 (developed): p.127 §11.5, p.128 §11.6
- gifted-amateur ch13 (revisited): p.142 §13.1, p.146 §13.3, p.148 §13.4
- gifted-amateur ch36 (revisited): p.382 §36.4, p.383 §36.4
- dinverno ch06 (core): p.106 §6.12
- legacy manuscript-section-8-4-8-6-flatness-count-sphere-curvature (developed)
- legacy lesson-a-curved-universe-capstone (revisited)
- legacy design-doc-misconception-diagnostics (mention)

## Review

**Verdict:** fixed

**Fixes**

- Filled two null Schutz convention entries (trace relation; Lambda term in the Lagrangian) with checked statements: derived from Schutz's confirmed conventions, and noting the absence of an action principle in the cited units.
- Removed a GA ch35 ref that did not support the 'constant R implies maximal symmetry' misconception.
- Teaching step 2 now links the circle deficit to loop holonomy (turning angle = area times R/2 in 2D), closing the gap flagged in the GA ch11 dossier, with the legacy holonomy chapter cited.
- Added the linearized scalar curvature to the formal level (d'Inverno ch21 evidence) and the GA ch16 'flat space is not flat spacetime' ref to the FLRW equation.

**Concerns**

- Worked and verified: sphere 2/a^2, C(s) = 2 pi s(1 - R s^2/12), geodesic-ball volume coefficient R/(6(n+2)), R = n(n-1)K, trace R = 4 Lambda - 8 pi G T, FLRW R and the dust (4/(3t^2)) and radiation (0) checks, R = -2N''/N for the lapse metric, Kretschmann 3/(4M^4) at r = 2M, conformal 3-metric formula, paraboloid and torus Gaussian curvatures.
- The statement that d'Inverno's flipped sign of R is compensated by its matter-Lagrangian convention is an inference from (13.7) and (13.5), not a quoted remark.
- Exercise refs GA Ex 15.4 and DIV Ex 25.10 still lack page numbers.
