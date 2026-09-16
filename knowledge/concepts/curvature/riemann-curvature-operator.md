---
type: "concept"
schema_version: 2
id: "riemann-curvature-operator"
title: "Riemann curvature operator"
tagline: "Curvature as a recipe: two walking instructions and an arrow in, the arrow's change out"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["curvature operator", "curvature endomorphism"]
prerequisites: ["riemann-curvature-tensor", "covariant-derivative", "lie-bracket", "holonomy", "levi-civita-connection"]
leads_to: ["curvature-2-form", "geodesic-deviation-equation", "sectional-curvature", "bundle-curvature", "integrability-condition-for-parallel-fields"]
visuals: ["four-legs-that-do-not-close", "falling-ring-of-crumbs"]
---

# Riemann curvature operator

*Curvature as a recipe: two walking instructions and an arrow in, the arrow's change out*

`riemann-curvature-operator` · curvature · advanced · physics-reviewed (revision 7)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[covariant-derivative]] (working) · [[lie-bracket]] (working) · [[holonomy]] (working) · [[levi-civita-connection]] (formal)  
**Opens:** [[curvature-2-form]] · [[geodesic-deviation-equation]] · [[sectional-curvature]] · [[bundle-curvature]] · [[integrability-condition-for-parallel-fields]]  
**Related:** [[ricci-identity]] · [[torsion-tensor]] · [[gauge-field-strength]] · [[second-exterior-covariant-derivative]]  
**Visuals:** ★ [[four-legs-that-do-not-close]] · [[falling-ring-of-crumbs]]

> Follow two walking instructions, then each one in reverse, and you can miss your starting spot even on flat ground. The curvature operator takes a tiny fraction of each instruction and adds a short closing walk, so the path ends where it began. Then it reports how an arrow carried around that loop, never swinging, comes back changed. On flat ground the arrow always comes back matching its start, so any change comes from curving.

## You will be able to

**Entry**
- Explain why two walking instructions and their reverses may need a closing walk to make a loop, and why the gap they leave says nothing about curving. `objectives/explain-the-closing-walk` ← `checks/playground-gap`, `checks/friend-on-a-flat-floor`, `problems/bigger-steps`
- Predict how swapping the order of the two instructions changes the arrow's change around the finished loop. `objectives/predict-swapped-order` ← `checks/swap-the-instructions`

**Working**
- Compute the curvature operator for non-commuting fields, including the bracket term, and check it on a flat plane. `objectives/compute-with-the-bracket` ← `checks/polar-unit-frame`, `problems/sphere-unit-frame`
- Explain why the operator's output at a point depends only on the values of the three vectors there. `objectives/explain-pointwise-action` ← `problems/same-value-at-a-point`
- Use the operator form of geodesic deviation to find tidal accelerations, with the correct slot order and sign. `objectives/read-tides-from-the-operator` ← `checks/tidal-map-at-earth`

**Formal**
- Derive the operator's components in a non-coordinate frame, and relate the operator to the square of the exterior covariant derivative. `objectives/derive-frame-components` ← `problems/frame-components`, `checks/exterior-derivative-twice`
- State which properties of the operator need metric compatibility, which need zero torsion, and which need neither. `objectives/sort-properties-by-hypothesis` ← `checks/torsion-and-the-operator`, `problems/skew-and-cyclic`

**Research**
- Distinguish the endomorphism-valued curvature operator from the operator on bivectors, and evaluate claims linking their signs to topology. `objectives/distinguish-curvature-operators` ← `checks/positive-sectional-not-enough`

## Ways in

### 1. Instructions that miss the start · entry · picture

*How can the arrow test work for a loop built from any two walking instructions?*

**Recap:** The arrow test: carry a cardboard arrow around a loop, a path that ends where it began. Keep it pressed against the ground and never let it swing left or right. On a flat floor it comes back matching its start. On a ball, a small loop brings it back turned a little. Two small loops side by side give twice the turn of one, so a loop's turn divided by its area measures the curving at that spot. Walking a loop the other way turns the arrow by the same amount the other way.

Stand in a flat playground, 10 metres from a pole. Here are two walking instructions. Each is a rule you can follow from wherever you stand. Instruction A: walk 1 metre directly away from the pole. Instruction B: walk 1 metre around the pole, keeping it on your left and staying the same distance from it.

Following an instruction in reverse means walking the other way. For A, that is 1 metre directly toward the pole. For B, it is 1 metre around the pole with the pole on your right.

Do A, then B, then A in reverse, then B in reverse. You might expect to end where you began. Instead, your last walk carries you about 9 centimetres past your starting spot.

Here is why. Picture two spokes running out from the pole, one through each end of your B walk. You did B 11 metres from the pole. A in reverse took you along the second spoke, in to 10 metres. Between the two spokes, the circle 10 metres out is only 10 elevenths as long as the circle 11 metres out. So B in reverse needs only 10 elevenths of a metre to reach your starting spot. Walking a full metre carries you one eleventh of a metre further, about 9 centimetres.

The four walks leave a gap. Walk the last 9 centimetres back to your starting spot, and the path becomes a loop. This extra piece is called the closing walk.

Now carry a cardboard arrow around the finished loop, pressed against the ground, never letting it swing. It comes back matching its start, as on every loop on flat ground. So the gap comes from the instructions, not from the ground.

On a ball, a small finished loop brings the arrow back turned a little. The curvature operator is a recipe built on this test. You hand it two instructions and an arrow. It takes a tiny fraction of each instruction, adds the closing walk, and carries the arrow around. For two 1-metre instructions at right angles, like A and B, it reports how the arrow comes back changed, divided by the loop's area. By custom, the report puts a minus sign in front of that change, which flips the change's direction but keeps its size.

Earth's ground is gently curved. A finished loop around one square metre of it turns an arrow by about 1.4 trillionths of a degree. That is the angle across a hair's width seen from 3 million kilometres away, more than seven times as far as the Moon. So nobody notices it.

**Try it:** On a big sheet of paper, draw two circles around a dot, 20 and 30 centimetres from it. Use a pin, a pencil and a piece of string held at each of those lengths. Mark a spot on the smaller circle. Move the pencil 10 centimetres directly away from the dot, to the bigger circle. Move it 10 centimetres along the bigger circle, measured with a piece of string. Move it 10 centimetres directly toward the dot. Move it 10 centimetres along the smaller circle, the opposite way round from your move along the bigger circle. You should end about 3 centimetres past your mark.

**Takeaway:** Two walking instructions and their reverses can leave a gap even on flat ground. The curvature operator adds a closing walk first, so the arrow's change around the finished loop comes only from curving.

*What this leaves out:* For instructions of other lengths, or not at right angles, the recipe's answer also grows with the instructions' lengths and with how close to a right angle they are.

*Builds on:* [[parallel-transport]]<br>*Visuals:* [[four-legs-that-do-not-close]]<br>*See:* `checks/playground-gap`, `problems/bigger-steps`

### 2. Two orders, minus the gap · working · calculation

*How is the curvature operator computed from covariant derivatives, and why does it subtract a derivative along the Lie bracket?*

The playground instructions in "Instructions that miss the start" left a gap of about 9 centimetres, so the curvature operator adds a closing walk before it compares arrows. In derivatives, the instructions become vector fields $u$ and $v$, the arrow becomes a vector field $w$, and $\nabla_u w = u^\mu\nabla_\mu w$ is the covariant derivative along $u$. Define

$$\mathcal{R}(u,v)w = \nabla_u\nabla_v w - \nabla_v\nabla_u w - \nabla_{[u,v]}w,$$

where $[u,v]^\mu = u^\nu\partial_\nu v^\mu - v^\nu\partial_\nu u^\mu$ is the Lie bracket. Flowing a parameter distance $\epsilon$ along $u$, then $v$, then back along $u$ and back along $v$ misses the start by $\epsilon^2[u,v]$ plus higher orders. The bracket is the gap per $\epsilon^2$. For the playground's unit fields at $r = 10$ m, $[u,v] = -\hat e_\theta/r$, so 1-metre steps predict a gap of 10 cm along $-\hat e_\theta$, the direction of B in reverse; the 9 centimetres found there differ only at higher order.

For coordinate fields $u = \partial_\mu$ and $v = \partial_\nu$ the bracket vanishes, and the derivation "Coordinate fields give the components" finds $\mathcal{R}(\partial_\mu,\partial_\nu)\partial_\sigma = R^\rho{}_{\sigma\mu\nu}\partial_\rho$. For any fields,

$$\big(\mathcal{R}(u,v)w\big)^\rho = R^\rho{}_{\sigma\mu\nu}\,w^\sigma u^\mu v^\nu.$$

The right side contains no derivatives of $u$, $v$ or $w$, so the output at a point depends only on the three vectors there. Without the bracket term this fails.

Test it where nothing is curved. On the flat plane in polar coordinates, take the playground's unit fields $u = \hat e_r = \partial_r$ and $v = \hat e_\theta = r^{-1}\partial_\theta$, and $w = \hat e_r$. With $\Gamma^\theta{}_{r\theta} = 1/r$ and $\Gamma^r{}_{\theta\theta} = -r$, one finds $\nabla_v\hat e_r = \hat e_\theta/r$ and $\nabla_u\hat e_r = 0$, so $\nabla_u\nabla_v\hat e_r - \nabla_v\nabla_u\hat e_r = -\hat e_\theta/r^2$. The bare commutator is not zero. But $[u,v] = -\hat e_\theta/r$ and $\nabla_{[u,v]}\hat e_r = -\hat e_\theta/r^2$, so $\mathcal{R}(u,v)\hat e_r = 0$, as flatness demands. At $r = 10$ m the bare commutator would report $0.01\ \mathrm{m^{-2}}$, about $4\times10^{11}$ times the curvature $1/R_\oplus^2$ of Earth's ground.

A loop built from the flows of $u$ and $v$ needs its closing walk. Carrying $w$ around the closed loop then gives

$$\Delta w = -\epsilon^2\,\mathcal{R}(u,v)w + O(\epsilon^3).$$

Take this on trust from the small-loop law of holonomy: the loop's oriented area is $\epsilon^2$ times the parallelogram of $u$ and $v$, and the closing walk, of length of order $\epsilon^2$, adds no area at that order. Swapping $u$ and $v$ walks the loop the other way and flips the sign. For orthonormal $u$ and $v$ the flow loop has area $\epsilon^2$, so the arrow's change divided by the loop's area is $-\mathcal{R}(u,v)w$: the entry recipe's report carries the opposite sign of the change.

**Takeaway:** The curvature operator takes covariant derivatives along two fields in both orders and subtracts the derivative along their bracket; the result acts pointwise, with the Riemann tensor as its components.

*What this leaves out:* Keeps the leading order in the loop size; the definition and its pointwise character hold for any connection.

*Continues:* `ways_in/instructions-that-miss-the-start`<br>*Builds on:* [[covariant-derivative]], [[lie-bracket]], [[holonomy]]<br>*Visuals:* [[four-legs-that-do-not-close]]<br>*See:* `derivations/coordinate-fields-give-components`, `checks/polar-unit-frame`, `problems/sphere-unit-frame`

### 3. Falling test masses read the operator · working · operational

*What part of the curvature operator does a family of freely falling test masses measure?*

The operator of "Two orders, minus the gap" is easiest to use when the two fields commute, because then the bracket term drops out. A family of freely falling test masses gives exactly that. Label neighbouring worldlines by a number $s$ and each by its proper time $\tau$, with four-velocity $u = \partial_\tau$ and separation $\xi = \partial_s$. Coordinate fields commute, so $[u,\xi] = 0$, and each worldline is a geodesic, $\nabla_u u = 0$. For a torsion-free connection, the derivation "Geodesic deviation from the operator" then finds

$$\frac{D^2\xi}{d\tau^2} = -\mathcal{R}(\xi,u)u,$$

the course geodesic deviation equation written without indices. The slot order matters: $\mathcal{R}(u,\xi)u = -\mathcal{R}(\xi,u)u$, so swapping the first two slots turns stretching into squeezing.

Read it as an instrument. Hold $u$ fixed as the observer's four-velocity and feed in separations $\xi$ orthogonal to it. The map $\xi \mapsto \mathcal{R}(\xi,u)u$ is linear on the observer's three-dimensional rest space. It is symmetric, because $R_{\mu\nu\rho\sigma} = R_{\rho\sigma\mu\nu}$, and its trace is $R_{\nu\sigma}u^\nu u^\sigma$. Freely falling test masses whose separations are tracked with light measure its six independent entries; an accelerometer riding on any one of them reads zero.

In a freely falling frame in a weak static field, $u^\mu = (c,0,0,0)$ and the map's matrix is $c^2R^i{}_{0j0} = \partial_i\partial_j\Phi$. Outside a spherical mass it has eigenvalue $-2GM/r^3$ along the local vertical and $+GM/r^3$ for each horizontal direction. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$. Two masses 1 m apart vertically therefore accelerate apart at $3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$, and a horizontal pair together at half that. The trace vanishes, as the vacuum field equation without a cosmological constant requires, but the map does not.

**Takeaway:** Freely falling test masses read the curvature operator with the four-velocity in its second and third slots: a symmetric map from separations to relative accelerations, whose trace is a Ricci component.

*What this leaves out:* Separations small compared with the distance over which the curvature changes; the weak-field matrix assumes a static field and slow test masses.

*Continues:* `ways_in/two-orders-minus-the-gap`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/deviation-from-the-operator`, `checks/tidal-map-at-earth`, `observations/atom-gravity-gradiometer`

### 4. An endomorphism-valued two-form · formal · structure

*What exactly is the curvature operator in any frame, and which of its properties need which hypotheses?*

The pointwise character found in "Two orders, minus the gap" is the heart of the definition. Let $\nabla$ be a connection on a vector bundle $E \to M$, for instance $TM$, and set $\mathcal{R}(X,Y)s = \nabla_X\nabla_Y s - \nabla_Y\nabla_X s - \nabla_{[X,Y]}s$ for vector fields $X, Y$ and a section $s$. Using $[fX,Y] = f[X,Y] - (Yf)X$ and the Leibniz rule, $\mathcal{R}(fX,Y)s = \mathcal{R}(X,fY)s = \mathcal{R}(X,Y)(fs) = f\,\mathcal{R}(X,Y)s$ for every smooth $f$; the derivatives of $f$ cancel only because of the bracket term. A map linear over functions acts pointwise, so $\mathcal{R}$ is a section of $\Lambda^2T^*M\otimes\mathrm{End}(E)$, an endomorphism-valued 2-form. No metric and no torsion condition enter.

In a local frame $e_a$ of $TM$ with dual coframe $\theta^a$, write $\nabla_{e_c}e_b = \Gamma^a{}_{cb}e_a$, derivative index first, and $[e_c,e_d] = C^e{}_{cd}\,e_e$. The derivation "Components in any frame" gives

$$R^a{}_{bcd} = e_c(\Gamma^a{}_{db}) - e_d(\Gamma^a{}_{cb}) + \Gamma^a{}_{cf}\Gamma^f{}_{db} - \Gamma^a{}_{df}\Gamma^f{}_{cb} - C^e{}_{cd}\Gamma^a{}_{eb},$$

which reduces to the coordinate formula when $C = 0$. With connection 1-forms $\omega^a{}_b(X) = \theta^a(\nabla_X e_b)$ the same computation reads $\mathcal{R}(X,Y)e_b = \Omega^a{}_b(X,Y)\,e_a$, where $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b$. The bracket term is the one in $d\alpha(X,Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X,Y])$. Equivalently, the exterior covariant derivative of $E$-valued forms squares to $d_\nabla^2 s = \mathcal{R}\,s$; the square vanishes for scalar-valued forms and for flat connections, not in general.

The hypotheses sort the properties.

- Antisymmetry, $\mathcal{R}(X,Y) = -\mathcal{R}(Y,X)$: always.
- Skew-adjointness, $g(\mathcal{R}(X,Y)Z,W) = -g(Z,\mathcal{R}(X,Y)W)$: needs $\nabla g = 0$. Apply $XY - YX - [X,Y]$, which annihilates functions, to $g(Z,W)$.
- First Bianchi identity, $\mathcal{R}(X,Y)Z + \mathcal{R}(Y,Z)X + \mathcal{R}(Z,X)Y = 0$: needs zero torsion, $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y] = 0$, and then follows from the Jacobi identity. With torsion the cyclic sum picks up torsion terms.
- Second Bianchi identity, $(\nabla_X\mathcal{R})(Y,Z) + (\nabla_Y\mathcal{R})(Z,X) + (\nabla_Z\mathcal{R})(X,Y) = 0$: stated this way for zero torsion; in frame form, $d\Omega + \omega\wedge\Omega - \Omega\wedge\omega = 0$ holds for any connection.

The component commutator shows torsion explicitly: $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma - T^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$ with $T^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu}$. The extra term appears because the tensor $\nabla_\mu\nabla_\nu V$ differs from $\nabla_{\partial_\mu}\nabla_{\partial_\nu}V$ by $\Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V$; the operator itself is unchanged.

Holonomy ties these together. For a loop that flows a parameter distance $\epsilon$ along $X$, then $Y$, back along both, and closes, $\mathrm{Hol} = 1 - \epsilon^2\mathcal{R}(X,Y) + O(\epsilon^3)$. For the Levi-Civita connection, skew-adjointness puts the generator in the orthogonal algebra of the metric: an infinitesimal rotation in Riemannian signature, an infinitesimal Lorentz transformation in Lorentzian signature. The Ambrose–Singer theorem goes further: the Lie algebra of the holonomy group at $p$ is spanned by the curvature operators at all points, conjugated back to $p$ by transport along paths.

**Takeaway:** The curvature operator is an endomorphism-valued 2-form, defined for any connection; skew-adjointness needs metric compatibility, and the first Bianchi identity needs zero torsion.

*What this leaves out:* Smooth connections on finite-rank vector bundles; sign conventions as in the course conventions.

*Continues:* `ways_in/two-orders-minus-the-gap`<br>*Builds on:* [[lie-bracket]], [[levi-civita-connection]]<br>*See:* `derivations/components-in-any-frame`, `problems/frame-components`, `checks/torsion-and-the-operator`, `problems/skew-and-cyclic`

### 5. The field strength of any connection · formal · bridge

*How is the curvature operator related to the field strength of a gauge field?*

The endomorphism-valued two-form of "An endomorphism-valued two-form" is defined for a connection on any vector bundle, so the same construction gives the field strength of a gauge field. Keep $\hbar$ explicit. A field $\psi$ of charge $q$ has the course gauge covariant derivative $D_\mu = \partial_\mu - i(q/\hbar)A_\mu$, and for coordinate fields

$$[D_\mu, D_\nu]\psi = -\frac{iq}{\hbar}F_{\mu\nu}\psi,\qquad F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu.$$

For non-coordinate fields the bracket term is needed exactly as for vectors. Here the endomorphism is multiplication by a number, so curvature operators at different points commute, and the holonomy of a loop is the phase $\exp(+iq\Phi/\hbar)$ set by the flux through it. For a non-abelian connection $D = d + \mathcal{A}$ with matrix-valued $\mathcal{A}$, the operator is $d\mathcal{A} + \mathcal{A}\wedge\mathcal{A}$, and it transforms as $g(\,\cdot\,)g^{-1}$ under a change of frame $g$, with no derivative of $g$.

Gravity differs in one structural way. For the Levi-Civita connection the bundle is $TM$ itself, so the endomorphism indices and the 2-form indices live in the same space. That identification makes the first Bianchi identity, pair exchange and contractions such as the Ricci tensor possible. A gauge field strength on an internal bundle has none of these three, although it obeys its own second Bianchi identity.

**Takeaway:** A gauge field strength is the curvature operator of a connection on an internal bundle; gravity's version acts on tangent vectors, which gives it extra symmetries and contractions.

*What this leaves out:* Treats the gauge group as a matrix group acting on a trivialized bundle over one chart.

*Continues:* `ways_in/endomorphism-valued-two-form`<br>*See:* `checks/exterior-derivative-twice`

### 6. Two objects called the curvature operator · research · contrast

*Which objects share the name curvature operator, and what do their signs control?*

The endomorphism-valued two-form $\mathcal{R}(X,Y)$ of "An endomorphism-valued two-form" is not the only object researchers call the curvature operator. For a Riemannian metric, pair exchange lets the same tensor define a symmetric map $\mathfrak{R}: \Lambda^2T_pM \to \Lambda^2T_pM$ by $\langle\mathfrak{R}(X\wedge Y), Z\wedge W\rangle = g(\mathcal{R}(Z,W)Y, X)$. Here the bivector inner product makes $e_i\wedge e_j$, $i<j$, orthonormal for an orthonormal frame $e_i$. The quadratic form of $\mathfrak{R}$ on a unit simple bivector is the sectional curvature in the course sign, so a round sphere of radius $a$ has $\mathfrak{R} = a^{-2}\,\mathrm{Id}$. The endomorphism acts on vectors, one plane at a time; $\mathfrak{R}$ acts on planes.

Their positivity conditions form a strict hierarchy. Positive $\mathfrak{R}$ implies positive sectional curvature, which implies positive Ricci curvature. In dimension four and higher neither converse holds; in dimension three every bivector is simple, so the first two conditions coincide. Hamilton used Ricci flow to show that a compact 4-manifold with positive curvature operator is diffeomorphic to $S^4$ or $\mathbb{RP}^4$. Böhm and Wilking extended this to every dimension: a compact manifold with positive curvature operator is diffeomorphic to a spherical space form. Brendle and Schoen reached the same conclusion from pointwise strictly quarter-pinched sectional curvature, proving the differentiable sphere theorem. In each proof the evolution of $\mathfrak{R}$ under Ricci flow, whose reaction term is quadratic in $\mathfrak{R}$, drives the argument, and cones of curvature operators preserved by that evolution organize it.

These theorems also separate the conditions. Complex projective space $\mathbb{CP}^2$ with the Fubini–Study metric, normalized to holomorphic sectional curvature 4, has sectional curvatures from 1 to 4, all positive. It is simply connected with Euler characteristic 3, while $S^4$ has 2 and $\mathbb{RP}^4$ has 1, so by Hamilton's theorem its curvature operator is not positive.

The endomorphism form drives other programmes. The Bochner technique writes a geometric Laplacian as a rough Laplacian plus a term built from $\mathcal{R}$, so a sign on curvature forces harmonic objects to vanish; on spinors the term is a quarter of the scalar curvature. Through the Ambrose–Singer theorem, restrictions on the values of $\mathcal{R}$ become restrictions on holonomy, as in manifolds of special holonomy. In four-dimensional gauge theory, self-duality of the field strength defines instantons.

Lorentzian signature changes the picture. The bivector inner product is indefinite, so sign conditions on $\mathfrak{R}$ behave differently, and spacetime classifications use the algebraic type of the Weyl part instead, as in the Petrov classification.

**Takeaway:** One tensor gives both the endomorphism of each plane and a symmetric operator on bivectors; positivity of the bivector operator is stronger than positive sectional curvature and forces a sphere quotient.

*What this leaves out:* Riemannian signature and compact manifolds for the positivity theorems.

*Continues:* `ways_in/endomorphism-valued-two-form`<br>*See:* `checks/positive-sectional-not-enough`, `research_horizon/positive-curvature-operators`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way the arrow points, left or right, while it lies against the ground. The arrow test never lets it swing. | — |
| closing walk | — | The short extra walk that takes you back to your starting spot after two instructions and their reverses, so that the path becomes a loop. | — |
| in reverse | — | Following a walking instruction the other way, from wherever you stand. For walking away from a pole, that means walking toward it. For walking around a pole with it on your left, it means walking around with it on your right. | — |
| curvature operator | REE-mahn | A recipe that takes two walking instructions and an arrow. It takes a tiny fraction of each instruction, adds a closing walk so the path becomes a tiny loop, and reports how the arrow comes back changed. For two 1-metre instructions at right angles, it reports the change divided by that loop's area, with a minus sign in front. | [[riemann-curvature-operator]] |
| Riemann curvature tensor | REE-mahn | A table kept at every place. For each way a tiny loop can be angled, and each starting direction of an arrow, it lists how the arrow comes back changed, divided by the loop's area. The arrow goes around the loop without swinging. By the same custom the curvature operator uses, the table puts a minus sign in front of the change it lists. | [[riemann-curvature-tensor]] |

## Key equations

### Curvature operator · working

$$
\mathcal{R}(u,v)w = \nabla_u\nabla_v w - \nabla_v\nabla_u w - \nabla_{[u,v]}w
$$

Covariant derivatives along two fields in both orders, minus the derivative along their Lie bracket.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal{R}(u,v)$ | the curvature operator for the fields $u$ and $v$ | the curvature operator of u and v |
| $\nabla_u$ | covariant derivative along $u$, $u^\mu\nabla_\mu$ | nabla along u |
| $[u,v]$ | Lie bracket, $u^\nu\partial_\nu v^\mu - v^\nu\partial_\nu u^\mu$ | the bracket of u and v |

**Holds when:** Any connection; smooth vector fields.  
**Say it:** “The curvature operator of u and v acting on w is nabla u nabla v w, minus nabla v nabla u w, minus nabla along the bracket of u and v acting on w.”  
**Justified by:** `stated`

### Components of the operator · working

$$
\big(\mathcal{R}(u,v)w\big)^\rho = R^\rho{}_{\sigma\mu\nu}\,w^\sigma u^\mu v^\nu
$$

The operator contains no derivatives of $u$, $v$ or $w$: it is the Riemann tensor fed the three vectors at a point.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course convention | the Riemann tensor |

**Holds when:** Coordinate components; the loop plane sits in the last two slots.  
**Say it:** “The rho component of the operator acting on w equals the Riemann tensor fed w, u and v.”  
**Justified by:** `derivations/coordinate-fields-give-components`

### Change around a closed loop of flows · working

$$
\Delta w = -\epsilon^2\,\mathcal{R}(u,v)w + O(\epsilon^3)
$$

Flow $\epsilon$ along $u$, then $v$, back along both, and finish with the closing walk: a carried vector changes by minus the operator times $\epsilon^2$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\epsilon$ | flow parameter of each of the four legs | epsilon |
| $\Delta w$ | change of the carried vector after the closed loop | the change in w |

**Holds when:** Leading order in $\epsilon$; the closing walk has length of order $\epsilon^2$.  
**Say it:** “The change in w is minus epsilon squared times the curvature operator of u and v acting on w.”  
**Justified by:** `stated`

### Geodesic deviation in operator form · working

$$
\frac{D^2\xi}{d\tau^2} = -\mathcal{R}(\xi,u)u
$$

Relative acceleration of neighbouring free-fall worldlines is minus the operator of separation and velocity acting on the velocity.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi$ | separation vector, $\partial_s$ | the separation |
| $u$ | four-velocity, $\partial_\tau$ | the four-velocity |

**Holds when:** Family of geodesics with $[u,\xi] = 0$; torsion-free connection; small separation.  
**Say it:** “The relative acceleration equals minus the curvature operator of the separation and the velocity, acting on the velocity.”  
**Justified by:** `derivations/deviation-from-the-operator`

### Components in any frame · formal

$$
R^a{}_{bcd} = e_c(\Gamma^a{}_{db}) - e_d(\Gamma^a{}_{cb}) + \Gamma^a{}_{cf}\Gamma^f{}_{db} - \Gamma^a{}_{df}\Gamma^f{}_{cb} - C^e{}_{cd}\Gamma^a{}_{eb}
$$

In a non-coordinate frame the bracket term contributes the commutation coefficients.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Gamma^a{}_{cb}$ | frame connection coefficients, $\nabla_{e_c}e_b = \Gamma^a{}_{cb}e_a$ | the connection coefficients |
| $C^e{}_{cd}$ | commutation coefficients, $[e_c,e_d] = C^e{}_{cd}e_e$ | the commutation coefficients |

**Holds when:** Any local frame; reduces to the coordinate formula when $C = 0$.  
**Say it:** “The frame components are two derivatives of connection coefficients, two products of them, and minus the commutation coefficients times a connection coefficient.”  
**Justified by:** `derivations/components-in-any-frame`

### Operator as curvature 2-form · formal

$$
\mathcal{R}(X,Y)e_b = \Omega^a{}_b(X,Y)\,e_a,\qquad \Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b
$$

In a frame the operator is a matrix of 2-forms built from the connection 1-forms.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\omega^a{}_b$ | connection 1-forms, $\omega^a{}_b(X) = \theta^a(\nabla_Xe_b)$ | the connection one-forms |
| $\Omega^a{}_b$ | curvature 2-forms | the curvature two-forms |

**Holds when:** Any connection; wedge and exterior derivative with $d\alpha(X,Y) = X\alpha(Y) - Y\alpha(X) - \alpha([X,Y])$.  
**Say it:** “The operator acting on a frame vector is the curvature two-form times the frame, where the curvature two-form is d omega plus omega wedge omega.”  
**Justified by:** `stated`

## Derivations

### Coordinate fields give the components · working

**Goal:** Show that $\mathcal{R}(\partial_\mu,\partial_\nu)\partial_\sigma = R^\rho{}_{\sigma\mu\nu}\partial_\rho$, and hence $(\mathcal{R}(u,v)w)^\rho = R^\rho{}_{\sigma\mu\nu}w^\sigma u^\mu v^\nu$.

1. Coordinate fields commute, $[\partial_\mu,\partial_\nu] = 0$, so the bracket term drops out.
2. With the derivative index first, $\nabla_\nu\partial_\sigma = \Gamma^\lambda{}_{\nu\sigma}\partial_\lambda$.
3. The Leibniz rule gives $\nabla_\mu(\Gamma^\lambda{}_{\nu\sigma}\partial_\lambda) = (\partial_\mu\Gamma^\rho{}_{\nu\sigma})\partial_\rho + \Gamma^\lambda{}_{\nu\sigma}\Gamma^\rho{}_{\mu\lambda}\partial_\rho$.
4. Subtracting the same with $\mu$ and $\nu$ swapped leaves the coefficient $\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, the course $R^\rho{}_{\sigma\mu\nu}$.
5. For general fields write $u = u^\mu\partial_\mu$, $v = v^\nu\partial_\nu$, $w = w^\sigma\partial_\sigma$ and expand with the Leibniz rule. Terms with derivatives of $u^\mu$ and $v^\nu$ are removed by $\nabla_{[u,v]}w$, and terms with derivatives of $w^\sigma$ cancel between the two orders and the bracket term, as the problem on two fields that agree at a point shows.

**Result:** $(\mathcal{R}(u,v)w)^\rho = R^\rho{}_{\sigma\mu\nu}w^\sigma u^\mu v^\nu$.

### Geodesic deviation from the operator · working

**Goal:** Show that $D^2\xi/d\tau^2 = -\mathcal{R}(\xi,u)u$ for a family of geodesics with $[u,\xi] = 0$.

1. Along each worldline $D/d\tau = \nabla_u$, so $D^2\xi/d\tau^2 = \nabla_u\nabla_u\xi$.
2. Zero torsion gives $\nabla_u\xi - \nabla_\xi u = [u,\xi] = 0$, so $\nabla_u\nabla_u\xi = \nabla_u\nabla_\xi u$.
3. The definition with $[u,\xi] = 0$ gives $\nabla_u\nabla_\xi u = \nabla_\xi\nabla_u u + \mathcal{R}(u,\xi)u$.
4. Every worldline of the family is a geodesic, so $\nabla_u u = 0$ everywhere on it, and $\nabla_\xi\nabla_u u = 0$.
5. Antisymmetry in the operator's first two slots gives $\mathcal{R}(u,\xi)u = -\mathcal{R}(\xi,u)u$, and $\mathcal{R}(\xi,u)u$ has components $R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

**Result:** $D^2\xi/d\tau^2 = -\mathcal{R}(\xi,u)u$, that is $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$, the course geodesic deviation equation.

### Components in any frame · formal

**Goal:** Find $R^a{}_{bcd} = \theta^a(\mathcal{R}(e_c,e_d)e_b)$ in a frame with $\nabla_{e_c}e_b = \Gamma^a{}_{cb}e_a$ and $[e_c,e_d] = C^e{}_{cd}e_e$.

1. $\nabla_{e_c}\nabla_{e_d}e_b = \nabla_{e_c}(\Gamma^f{}_{db}e_f) = e_c(\Gamma^a{}_{db})e_a + \Gamma^f{}_{db}\Gamma^a{}_{cf}e_a$.
2. Swapping $c$ and $d$: $\nabla_{e_d}\nabla_{e_c}e_b = e_d(\Gamma^a{}_{cb})e_a + \Gamma^f{}_{cb}\Gamma^a{}_{df}e_a$.
3. The bracket term is $\nabla_{[e_c,e_d]}e_b = C^e{}_{cd}\nabla_{e_e}e_b = C^e{}_{cd}\Gamma^a{}_{eb}e_a$.
4. Subtract the second and third lines from the first and read off the coefficient of $e_a$.
5. Check on a sphere of radius $a$ with $e_1 = a^{-1}\partial_\theta$, $e_2 = (a\sin\theta)^{-1}\partial_\phi$: $\Gamma^2{}_{21} = \cot\theta/a$, $\Gamma^a{}_{1b} = 0$, $C^2{}_{12} = -\cot\theta/a$, so $R^2{}_{112} = -1/(a^2\sin^2\theta) + \cot^2\theta/a^2 = -1/a^2$.

**Result:** $R^a{}_{bcd} = e_c(\Gamma^a{}_{db}) - e_d(\Gamma^a{}_{cb}) + \Gamma^a{}_{cf}\Gamma^f{}_{db} - \Gamma^a{}_{df}\Gamma^f{}_{cb} - C^e{}_{cd}\Gamma^a{}_{eb}$.

## Problems

### `bigger-steps` · entry · difficulty 1 · estimate

Stand in the flat playground again, 10 metres from the pole. This time each instruction uses 2 metres. A: walk 2 metres directly away from the pole. B: walk 2 metres around the pole, keeping it on your left and staying the same distance from it. Do A, then B, then A in reverse, then B in reverse. How far past your starting spot does your last walk carry you? How does that compare with the 9 centimetres for 1-metre instructions?

**Hints**

1. How far from the pole are you while you do B?
2. Picture two spokes from the pole, one through each end of your B walk. How much shorter is the circle 10 metres out between them?

**Answer:** About 33 centimetres past your starting spot, nearly four times the 9 centimetres.

**Must contain:** B happens 12 metres from the pole; Between the two spokes, B in reverse needs only 1 and two thirds metres; The gap is one third of a metre, nearly four times bigger

**Numeric:** distance past the starting spot = 33.3 cm (magnitude, ±5%)

**Solution**

1. After A you are 12 metres from the pole, so you do B on the circle 12 metres out.
2. A in reverse takes you in to 10 metres along the spoke through the end of B. Between the two spokes, the circle 10 metres out is 10 twelfths as long as the circle 12 metres out. So B in reverse needs only 10 twelfths of 2 metres, 1 and two thirds metres, to reach your starting spot.
3. Walking 2 full metres carries you one third of a metre further, about 33 centimetres.
4. 33 centimetres is nearly four times 9 centimetres. Both instructions doubled, so the gap grew by about two times two. It falls a little short of four because you did B 12 metres from the pole, not 11.

### `sphere-unit-frame` · working · difficulty 2 · calculation

On a sphere of radius $a$ with coordinates $(\theta,\phi)$, take the orthonormal fields $u = \hat e_\theta = a^{-1}\partial_\theta$ and $v = \hat e_\phi = (a\sin\theta)^{-1}\partial_\phi$. Use $\nabla_{\hat e_\phi}\hat e_\theta = (\cot\theta/a)\,\hat e_\phi$ and $\nabla_{\hat e_\theta}\hat e_\theta = \nabla_{\hat e_\theta}\hat e_\phi = 0$. Compute the bare commutator $\nabla_u\nabla_v\hat e_\theta - \nabla_v\nabla_u\hat e_\theta$ and $\mathcal{R}(u,v)\hat e_\theta$, and evaluate both for Earth, $a = 6371$ km, at colatitude $30^\circ$.

**Hints**

1. Compute $[u,v]$ first: only the coefficient of $v$ depends on $\theta$.
2. $\partial_\theta\cot\theta = -1/\sin^2\theta$.

**Answer:** Bare commutator $-\hat e_\phi/(a^2\sin^2\theta)$; operator $-\hat e_\phi/a^2$. For Earth at colatitude $30^\circ$ their $\hat e_\phi$ components are $-9.85\times10^{-14}\ \mathrm{m^{-2}}$ and $-2.46\times10^{-14}\ \mathrm{m^{-2}}$: the bare commutator overstates the curvature fourfold.

**Must contain:** The bare commutator is minus e phi hat over a squared sine squared theta; The bracket term removes the cotangent squared part, leaving minus e phi hat over a squared; At colatitude 30 degrees the bare commutator is four times too large

**Numeric:** e phi hat component of the operator acting on e theta hat = -2.46e-14 m^-2 (signed, ±2%); e phi hat component of the bare commutator = -9.85e-14 m^-2 (signed, ±2%)

**Solution**

1. $\nabla_u\hat e_\theta = 0$, so $\nabla_v\nabla_u\hat e_\theta = 0$.
2. $\nabla_u\nabla_v\hat e_\theta = \nabla_u\big((\cot\theta/a)\hat e_\phi\big) = a^{-1}\partial_\theta(\cot\theta/a)\,\hat e_\phi + 0 = -\hat e_\phi/(a^2\sin^2\theta)$.
3. $[u,v] = a^{-1}\partial_\theta\big((a\sin\theta)^{-1}\big)\partial_\phi = -(\cot\theta/a)\,\hat e_\phi$, so $\nabla_{[u,v]}\hat e_\theta = -(\cot^2\theta/a^2)\,\hat e_\phi$.
4. $\mathcal{R}(u,v)\hat e_\theta = -\hat e_\phi(1 - \cos^2\theta)/(a^2\sin^2\theta) = -\hat e_\phi/a^2$, which matches $K\big(g(v,w)u - g(u,w)v\big)$ with $K = 1/a^2$ and $w = \hat e_\theta$.
5. With $a = 6.371\times10^6$ m, $1/a^2 = 2.46\times10^{-14}\ \mathrm{m^{-2}}$. At $\theta = 30^\circ$, $\sin^2\theta = 1/4$, so the bare commutator is four times larger, $9.85\times10^{-14}\ \mathrm{m^{-2}}$ in size.

**Targets:** `bare-commutator-is-curvature`

### `same-value-at-a-point` · working · difficulty 2 · derivation

The fields $w$ and $fw$ agree at a point $p$, where $f(p) = 1$ but the function $f$ varies nearby. Show that $\mathcal{R}(u,v)(fw) = \mathcal{R}(u,v)w$ at $p$, although $\nabla_u\nabla_v(fw) \neq \nabla_u\nabla_v w$ there in general.

**Hints**

1. Expand with the Leibniz rule twice.
2. $uvf - vuf$ is the bracket of $u$ and $v$ acting on $f$.

**Answer:** $\mathcal{R}(u,v)(fw) = f\,\mathcal{R}(u,v)w$, which equals $\mathcal{R}(u,v)w$ at $p$, while $\nabla_u\nabla_v(fw)$ keeps terms in $uf$, $vf$ and $uvf$. The operator sees only the value of $w$ at $p$.

**Must contain:** Second covariant derivatives of f w contain derivatives of f; First-derivative terms cancel between the two orders; The bracket term cancels the remaining bracket of u and v acting on f

**Solution**

1. $\nabla_v(fw) = (vf)w + f\nabla_vw$, so $\nabla_u\nabla_v(fw) = (uvf)w + (vf)\nabla_uw + (uf)\nabla_vw + f\nabla_u\nabla_vw$, which contains derivatives of $f$.
2. In $\nabla_u\nabla_v(fw) - \nabla_v\nabla_u(fw)$ the first-derivative terms cancel in pairs, leaving $f(\nabla_u\nabla_v - \nabla_v\nabla_u)w + (uvf - vuf)w$.
3. $uvf - vuf = [u,v]f$, and the bracket term is $\nabla_{[u,v]}(fw) = ([u,v]f)w + f\nabla_{[u,v]}w$.
4. Subtracting removes the leftover, so $\mathcal{R}(u,v)(fw) = f\,\mathcal{R}(u,v)w$, which equals $\mathcal{R}(u,v)w$ where $f = 1$.

### `skew-and-cyclic` · formal · difficulty 2 · proof

For a connection $\nabla$ on $TM$: (a) show that $\nabla g = 0$ implies $g(\mathcal{R}(X,Y)Z,W) = -g(Z,\mathcal{R}(X,Y)W)$; (b) show that zero torsion implies $\mathcal{R}(X,Y)Z + \mathcal{R}(Y,Z)X + \mathcal{R}(Z,X)Y = 0$. For each, say which hypothesis the proof uses and which it does not.

**Hints**

1. For (a), $XY - YX - [X,Y]$ annihilates every function; apply it to $g(Z,W)$.
2. For (b), group the cyclic sum by the outer derivative and use $\nabla_XY - \nabla_YX = [X,Y]$.
3. The Jacobi identity finishes (b).

**Answer:** (a) Expanding $(XY - YX - [X,Y])\,g(Z,W) = 0$ with $\nabla g = 0$ leaves $g(\mathcal{R}(X,Y)Z,W) + g(Z,\mathcal{R}(X,Y)W) = 0$; torsion is not used. (b) The cyclic sum reduces to $[X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0$; the metric is not used.

**Must contain:** Metric compatibility alone gives skew-adjointness; Zero torsion turns the cyclic sum into the Jacobi identity; Neither proof needs the other hypothesis

**Solution**

1. (a) $\nabla g = 0$ means $X\,g(Z,W) = g(\nabla_XZ,W) + g(Z,\nabla_XW)$.
2. Applying it twice, $XY\,g(Z,W) = g(\nabla_X\nabla_YZ,W) + g(\nabla_YZ,\nabla_XW) + g(\nabla_XZ,\nabla_YW) + g(Z,\nabla_X\nabla_YW)$.
3. In $XY - YX$ the two mixed terms cancel against their swapped partners, and $[X,Y]\,g(Z,W) = g(\nabla_{[X,Y]}Z,W) + g(Z,\nabla_{[X,Y]}W)$.
4. So $0 = (XY - YX - [X,Y])\,g(Z,W) = g(\mathcal{R}(X,Y)Z,W) + g(Z,\mathcal{R}(X,Y)W)$, using only $\nabla g = 0$.
5. (b) Group the second-derivative terms of the cyclic sum by the outer derivative: $\nabla_X(\nabla_YZ - \nabla_ZY) + \nabla_Y(\nabla_ZX - \nabla_XZ) + \nabla_Z(\nabla_XY - \nabla_YX)$.
6. Zero torsion turns each difference into a bracket; the remaining terms are $-\nabla_{[Y,Z]}X - \nabla_{[Z,X]}Y - \nabla_{[X,Y]}Z$.
7. Pair them: $\nabla_X[Y,Z] - \nabla_{[Y,Z]}X = [X,[Y,Z]]$ by zero torsion, and likewise for the other two pairs.
8. The sum is the Jacobi identity, which vanishes; the metric was never used.

### `frame-components` · formal · difficulty 2 · derivation

In a frame with $\nabla_{e_c}e_b = \Gamma^a{}_{cb}e_a$ and $[e_c,e_d] = C^e{}_{cd}e_e$, derive $R^a{}_{bcd}$. Check it on the flat plane with $e_1 = \hat e_r$ and $e_2 = \hat e_\theta$, where $\Gamma^2{}_{21} = 1/r$, $\Gamma^1{}_{22} = -1/r$, every $\Gamma^a{}_{1b} = 0$, and $C^2{}_{12} = -1/r$, by computing $R^2{}_{112}$.

**Hints**

1. Expand $\nabla_{e_c}(\Gamma^f{}_{db}e_f)$ with the Leibniz rule.
2. In the check, one derivative term and the commutation term survive.

**Answer:** $R^a{}_{bcd} = e_c(\Gamma^a{}_{db}) - e_d(\Gamma^a{}_{cb}) + \Gamma^a{}_{cf}\Gamma^f{}_{db} - \Gamma^a{}_{df}\Gamma^f{}_{cb} - C^e{}_{cd}\Gamma^a{}_{eb}$, and on the flat plane $R^2{}_{112} = -1/r^2 + 1/r^2 = 0$.

**Must contain:** The bracket term contributes minus C times Gamma; The derivative term gives minus one over r squared; The commutation term cancels it, giving zero

**Numeric:** R two one one two for the polar unit frame = 0 m^-2 (signed, ±1e-06)

**Solution**

1. Expand both second derivatives with the Leibniz rule and subtract the bracket term $C^e{}_{cd}\Gamma^a{}_{eb}e_a$, as in the derivation \"Components in any frame\".
2. For the check, $e_1(\Gamma^2{}_{21}) = \partial_r(1/r) = -1/r^2$ and $e_2(\Gamma^2{}_{11}) = 0$.
3. Both products vanish because every $\Gamma^a{}_{1b} = 0$.
4. $-C^2{}_{12}\Gamma^2{}_{21} = +1/r^2$, so $R^2{}_{112} = 0$, as it must be on a flat plane. Dropping the commutation term would leave $-1/r^2$, a fake curvature.

## Observations

- **The vertical gradient of Earth's gravity, measured with two clouds of falling atoms** (measured, working). An atom-interferometer gradiometer drops two clouds of laser-cooled atoms at different heights and compares their free-fall accelerations. The difference per unit vertical separation is the vertical eigenvalue of the map $\xi \mapsto -\mathcal{R}(\xi,u)u$; Earth's rotation, shape and nearby masses change it slightly. *Numbers:* Spherical Earth: $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$, with the clouds accelerating apart. The standard free-air gradient is $3.086\times10^{-6}\ \mathrm{s^{-2}}$. *Reference:* M. J. Snadden, J. M. McGuirk, P. Bouyer, K. G. Haritos, M. A. Kasevich (1998), *Measurement of the Earth's Gravity Gradient with an Atom Interferometer-Based Gravity Gradiometer*, Physical Review Letters 81, 971–974, doi:10.1103/PhysRevLett.81.971

## Teaching arc

1. **Walk instructions that miss the start** (entry). Ask for a prediction about the playground walk, then explain the overshoot with two spokes from the pole. *Why:* The gap is the surprise that motivates the closing walk. *Predict:* If you walk away from the pole, around it, toward it, and back around it the other way, do you end where you began? *Visual:* [[four-legs-that-do-not-close]] *Uses:* `ways_in/instructions-that-miss-the-start`, `checks/playground-gap`
2. **Close the loop and test the ground** (entry). Finish the loop with the closing walk, run the arrow test on flat ground, then swap the instructions on a ball. *Why:* It separates what the instructions do from what the ground does. *Predict:* On flat ground, after the closing walk, will the arrow come back matching its start? *Visual:* [[four-legs-that-do-not-close]] *Uses:* `checks/friend-on-a-flat-floor`, `checks/swap-the-instructions`
3. **Compute the fake and the fix** (working). Compute the bare commutator for the polar unit fields, then the bracket term, then repeat on a sphere. *Why:* A nonzero commutator on a flat plane cures the habit of dropping the bracket. *Predict:* On a flat plane, can two covariant derivatives taken in two orders disagree? *Visual:* [[four-legs-that-do-not-close]] *Uses:* `ways_in/two-orders-minus-the-gap`, `checks/polar-unit-frame`, `problems/sphere-unit-frame`
4. **Read tides from the operator** (working). Derive geodesic deviation in operator form and evaluate the tidal map at Earth's surface. *Why:* It shows why commuting fields make the operator the natural language for measurements. *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tides-read-one-slot`, `derivations/deviation-from-the-operator`, `checks/tidal-map-at-earth`
5. **Sort properties by hypothesis** (formal). Present the operator as an endomorphism-valued 2-form and sort its properties by the hypotheses they need. *Why:* Torsion, frames and gauge bundles each remove a different hypothesis. *Uses:* `ways_in/endomorphism-valued-two-form`, `checks/torsion-and-the-operator`, `problems/skew-and-cyclic`
6. **Separate the two curvature operators** (research). Contrast the endomorphism with the operator on bivectors and test the complex projective plane. *Why:* The shared name hides a strict hierarchy of sign conditions. *Uses:* `ways_in/which-curvature-operator`, `checks/positive-sectional-not-enough`

## Misconceptions

### “If two instructions and their reverses leave me away from my start, the ground must be curved.” · entry · `gap-means-curving`

- **Why it is tempting:** On a flat floor, walking a square with a tape measure brings you back to the start.
- **What is true:** Instructions like walking around a pole leave a gap on perfectly flat ground. Only the arrow's change around the finished loop reveals curving.
- **Exposed by:** `checks/friend-on-a-flat-floor`

### “Doing the two instructions in the other order gives the arrow the same change.” · entry · `order-does-not-matter`

- **Why it is tempting:** Swapping two steps of a cooking recipe often changes nothing.
- **What is true:** Swapping the order walks nearly the same small loop the other way. So the arrow comes back turned the other way.
- **Exposed by:** `checks/swap-the-instructions`

### “Curvature is simply the commutator of covariant derivatives along any two vector fields.” · working · `bare-commutator-is-curvature`

- **Why it is tempting:** In a coordinate basis, where most calculations happen, the bracket term vanishes.
- **What is true:** For fields that do not commute, the bare commutator includes the derivative along their bracket, which is nonzero even on a flat plane. Subtracting it leaves the curvature.
- **Exposed by:** `checks/polar-unit-frame`

### “Applying the exterior covariant derivative twice always gives zero, because d squared is zero.” · formal · `covariant-d-squared-vanishes`

- **Why it is tempting:** The same letter d is used for the ordinary and the covariant exterior derivative.
- **What is true:** The square vanishes for scalar-valued forms. On vector-valued forms the covariant version squares to the curvature operator.
- **Exposed by:** `checks/exterior-derivative-twice`

### “With torsion the curvature operator stops being a tensor.” · formal · `torsion-breaks-the-operator`

- **Why it is tempting:** The component commutator of covariant derivatives gains a derivative term when torsion is present.
- **What is true:** Linearity over functions never uses torsion, so the operator is always a tensor. Torsion changes the component commutator and the first Bianchi identity instead.
- **Exposed by:** `checks/torsion-and-the-operator`

### “Positive sectional curvature means the curvature operator on bivectors is positive.” · research · `positive-sectional-means-positive-operator`

- **Why it is tempting:** Sectional curvature is the operator's value on planes, so positivity on planes looks like positivity everywhere.
- **What is true:** Sectional curvature tests the operator only on simple bivectors. The complex projective plane has positive sectional curvature but not a positive curvature operator.
- **Exposed by:** `checks/positive-sectional-not-enough`

## Checks

1. **Entry · numeric** `checks/playground-gap`. Stand in a flat playground, 5 metres from a pole. Instruction A: walk 1 metre directly away from the pole. Instruction B: walk 1 metre around the pole, keeping it on your left and staying the same distance from it. Do A, then B, then A in reverse, then B in reverse. Do you end at your starting spot? If not, about how far past it does your last walk carry you?
   - **Hints:** How far from the pole are you while you do B? / Picture two spokes from the pole, one through each end of your B walk.
   - **Answer:** No. Your last walk carries you about 17 centimetres past your starting spot. After A you are 6 metres from the pole, so you do B on the circle 6 metres out. A in reverse takes you in to 5 metres, along the spoke through the end of B. Between that spoke and the one through your start, the circle 5 metres out is 5 sixths as long as the circle 6 metres out. So B in reverse needs only 5 sixths of a metre to reach your starting spot. Walking a full metre overshoots by one sixth of a metre, about 17 centimetres.
   - **Must contain:** You do not end at the start; B is walked 6 metres out, but B in reverse only 5 metres out; The overshoot is one sixth of a metre, about 17 centimetres
   - **Numeric:** distance past the starting spot = 16.7 cm (magnitude, ±10%)
   - **Visual:** [[four-legs-that-do-not-close]]
2. **Entry · evaluate-claim** `checks/friend-on-a-flat-floor`. On a flat playground, Maya follows two walking instructions, A then B. Then she follows A in reverse and B in reverse, and ends 3 centimetres from her starting spot. She says this proves the ground is curved. Is she right? What test would settle it?
   - **Hints:** What happened in the playground with the pole, where the ground was flat?
   - **Answer:** No. In the playground with the pole, instructions A and B and their reverses leave a 9-centimetre gap, although the ground is flat. The gap comes from the instructions: 1 metre around the pole takes you further around it when you are closer to it. To test the ground, Maya walks the last 3 centimetres to finish the loop. Then she carries a cardboard arrow around the finished loop, never letting it swing. On curved ground, a small finished loop would bring the arrow back turned. On this flat playground it comes back matching its start, so her gap was never a sign of curving.
   - **Must contain:** No, the gap does not show curving; Instructions alone can leave a gap on flat ground; Finish the loop with a closing walk and run the arrow test
   - **Targets:** `gap-means-curving`
   - **Visual:** [[four-legs-that-do-not-close]]
3. **Entry · predict** `checks/swap-the-instructions`. On a smooth ball, you follow two short instructions: A, then B, then A in reverse, then B in reverse, and you finish with the closing walk. A fresh cardboard arrow, carried without swinging, comes back turned 2 degrees toward your left. You set the arrow back to its starting direction. Now, from the same spot, you do B first: B, then A, then B in reverse, then A in reverse, and the closing walk. How does the arrow come back this time?
   - **Hints:** List the corners of each trip in order.
   - **Answer:** Turned about 2 degrees toward your right. Call the spots where you stop one instruction and start the next your corners. On the first trip the corners in order are: after A; after A and B; and after A, B and A in reverse. On the second trip they are: after B; after B and A; and after B, A and B in reverse. Two facts let you match the corners up, and both hold because the instructions are short. First, swapping two of the walks moves where you end by only a small gap, like the 9 centimetres in the playground. Second, a walk followed by its own reverse brings you back to where that walk began. Now match them. The first trip's third corner is after A, B and A in reverse. Swapping its first two walks makes it after B, A and A in reverse. That is just after B, the second trip's first corner. The first trip's second corner is after A and B. Swapping those two walks makes it after B and A, the second trip's second corner. The second trip's third corner is after B, A and B in reverse. Swapping its first two walks makes it after A, B and B in reverse. That is just after A, the first trip's first corner. So the second trip visits nearly the same three corners as the first, in the opposite order. It walks nearly the same small loop the other way, and walking a loop the other way turns the arrow by the same amount the other way.
   - **Must contain:** About 2 degrees toward the right; B first visits nearly the same corners in the opposite order; Walking a loop the other way reverses the turn
   - **Numeric:** turn toward the walker's left = -2 deg (signed, ±0.3, mod 360)
   - **Targets:** `order-does-not-matter`
4. **Working · numeric** `checks/polar-unit-frame`. On the flat plane in polar coordinates, take $u = \hat e_r = \partial_r$, $v = \hat e_\theta = r^{-1}\partial_\theta$ and $w = \hat e_r$ at $r = 2$ m. A classmate computes $\nabla_u\nabla_v w - \nabla_v\nabla_u w = -\hat e_\theta/(4\ \mathrm{m^2})$ and concludes the plane is curved. Find $[u,v]$, $\nabla_{[u,v]}w$ and $\mathcal{R}(u,v)w$, and evaluate the conclusion.
   - **Hints:** Only the coefficient $r^{-1}$ of $v$ varies along $u$. / Use $\nabla_{\hat e_\theta}\hat e_r = \hat e_\theta/r$.
   - **Answer:** $[u,v] = \partial_r(r^{-1})\,\partial_\theta = -\hat e_\theta/r$. Because $\nabla_{\hat e_\theta}\hat e_r = \hat e_\theta/r$, $\nabla_{[u,v]}w = -\hat e_\theta/r^2 = -\hat e_\theta/(4\ \mathrm{m^2})$. So $\mathcal{R}(u,v)w = -\hat e_\theta/(4\ \mathrm{m^2}) + \hat e_\theta/(4\ \mathrm{m^2}) = 0$. The classmate's result is the bracket term, not curvature: the unit fields do not commute, and the plane is flat.
   - **Must contain:** The bracket is minus e theta hat over r; The bracket term equals the bare commutator; The curvature operator is zero, so the plane is flat
   - **Numeric:** e theta hat component of the bracket term = -0.25 m^-2 (signed, ±0.01); e theta hat component of the curvature operator acting on w = 0 m^-2 (signed, ±1e-06)
   - **Targets:** `bare-commutator-is-curvature`
   - **Visual:** [[four-legs-that-do-not-close]]
5. **Working · numeric** `checks/tidal-map-at-earth`. Two freely falling test masses at Earth's surface are 1 m apart along the local vertical, with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and $r = 6371$ km. Use $D^2\xi/d\tau^2 = -\mathcal{R}(\xi,u)u$, whose map $\xi \mapsto \mathcal{R}(\xi,u)u$ has matrix $\partial_i\partial_j\Phi$ in the weak field. Find their relative acceleration and the trace of the map. A student writes $-\mathcal{R}(u,\xi)u$ instead: what does the student predict?
   - **Hints:** The second derivative of $-GM/r$ along the radial direction is $-2GM/r^3$.
   - **Answer:** Along the vertical, $\partial_z^2(-GM/r) = -2GM/r^3 = -3.08\times10^{-6}\ \mathrm{s^{-2}}$, so $D^2\xi/d\tau^2 = +3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$ for $\xi = 1$ m: the masses accelerate apart. Each horizontal eigenvalue is $+GM/r^3 = +1.54\times10^{-6}\ \mathrm{s^{-2}}$, so the trace is $-2 + 1 + 1 = 0$ in units of $GM/r^3$, as vacuum requires. Because $\mathcal{R}(u,\xi)u = -\mathcal{R}(\xi,u)u$, the student predicts the vertical pair accelerating together at the same rate, the wrong sign.
   - **Must contain:** Vertical relative acceleration 3.08 millionths of a metre per second squared, apart; The trace is zero outside the mass; Swapping the first two slots flips the sign
   - **Numeric:** relative acceleration of the vertical pair, positive apart = 3.08e-06 m/s^2 (signed, ±3%)
   - **Visual:** [[falling-ring-of-crumbs]]
6. **Formal · evaluate-claim** `checks/exterior-derivative-twice`. Evaluate the claim: \"The exterior derivative squares to zero, so applying the exterior covariant derivative $d_\nabla$ twice to a vector field $w$ must give zero.\"
   - **Hints:** Evaluate $d_\nabla(\nabla w)$ on a pair of vector fields.
   - **Answer:** False for vector-valued forms. $d_\nabla w = \nabla w$ is a vector-valued 1-form, and for such a form $S$, $d_\nabla S(X,Y) = \nabla_X(S(Y)) - \nabla_Y(S(X)) - S([X,Y])$. With $S = \nabla w$ this is $\nabla_X\nabla_Yw - \nabla_Y\nabla_Xw - \nabla_{[X,Y]}w = \mathcal{R}(X,Y)w$. So $d_\nabla^2 w = \mathcal{R}\,w$, which vanishes for every $w$ only where the connection is flat. What vanishes for any connection is the covariant derivative of the curvature itself, $d\Omega + \omega\wedge\Omega - \Omega\wedge\omega = 0$, the analogue of $dF = 0$.
   - **Must contain:** The claim holds only for scalar-valued forms; Twice the exterior covariant derivative gives the curvature operator; The second Bianchi identity is the statement that does vanish
   - **Targets:** `covariant-d-squared-vanishes`
7. **Formal · evaluate-claim** `checks/torsion-and-the-operator`. Evaluate the claim: \"For a connection with torsion, $\mathcal{R}(X,Y)Z$ is no longer a tensor, but the first Bianchi identity and $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$ hold unchanged.\"
   - **Hints:** Which step of the tensor proof uses torsion?
   - **Answer:** Both parts fail. Linearity of $\mathcal{R}$ over functions uses only the Leibniz rule and $[fX,Y] = f[X,Y] - (Yf)X$, so $\mathcal{R}$ is a tensor for every connection. Torsion changes the identities instead. The cyclic sum $\mathcal{R}(X,Y)Z + \mathcal{R}(Y,Z)X + \mathcal{R}(Z,X)Y$ picks up terms in the torsion and its derivative, because its proof needs $\nabla_XY - \nabla_YX = [X,Y]$. The component commutator becomes $R^\rho{}_{\sigma\mu\nu}V^\sigma - T^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$, because the tensor $\nabla_\mu\nabla_\nu V$ differs from $\nabla_{\partial_\mu}\nabla_{\partial_\nu}V$ by $\Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V$. Even a function then has $[\nabla_\mu,\nabla_\nu]f = -T^\lambda{}_{\mu\nu}\partial_\lambda f$.
   - **Must contain:** The operator is a tensor for any connection; The first Bianchi identity gains torsion terms; The component commutator gains minus torsion times the covariant derivative
   - **Targets:** `torsion-breaks-the-operator`
8. **Research · evaluate-claim** `checks/positive-sectional-not-enough`. Evaluate the claim: \"Complex projective space $\mathbb{CP}^2$ with the Fubini–Study metric has positive sectional curvature everywhere, so its curvature operator on bivectors is positive.\"
   - **Hints:** Compare Euler characteristics with the conclusion of the four-dimensional theorem.
   - **Answer:** The premise is true: normalized to holomorphic sectional curvature 4, its sectional curvatures lie between 1 and 4. The conclusion is false. By Hamilton's theorem a compact 4-manifold with positive curvature operator on bivectors is diffeomorphic to $S^4$ or $\mathbb{RP}^4$, whose Euler characteristics are 2 and 1. $\mathbb{CP}^2$ has Euler characteristic 3, so its curvature operator cannot be positive. Sectional curvature samples $\mathfrak{R}$ only on simple bivectors, and positivity on all bivectors is stronger.
   - **Must contain:** Its sectional curvatures lie between 1 and 4; In dimension four a positive curvature operator forces the sphere or real projective space; Euler characteristic 3 rules that out
   - **Targets:** `positive-sectional-means-positive-operator`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Overall sign of the curvature operator | $\mathcal{R}(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$, so for orthonormal $X, Y$ the sectional curvature is $g(\mathcal{R}(X,Y)Y,X)$, positive on a sphere. | Some texts define the operator with the opposite overall sign and then write sectional curvature as $g(\mathcal{R}(X,Y)X,Y)$. Check a sphere before borrowing a formula. |
| Which slots of the Riemann tensor hold the plane and the vector acted on | $(\mathcal{R}(u,v)w)^\rho = R^\rho{}_{\sigma\mu\nu}w^\sigma u^\mu v^\nu$: the plane in the last two slots, the vector acted on in the second. | Some texts store the plane in the first two lower slots and the vector acted on in the last, so the same operator has rearranged components. |
| The name curvature operator | The curvature operator is the endomorphism-valued 2-form $\mathcal{R}(X,Y)$; the symmetric map on bivectors is written $\mathfrak{R}$ and named in full. | Comparison geometry often gives the name to the map on bivectors, whose eigenvalues some texts rescale by a factor of two. |

## Visuals

- ★ [[four-legs-that-do-not-close]] (flagship): Shows the gap left by two instruction fields, the closing walk, and the arrow's change around the closed loop. *Sketch:* A flat plane with a pole, a sphere, or a saddle. The learner picks two instruction fields (a coordinate pair, the unit polar pair, or unit fields on the sphere) and a step size. The walker follows the first field, the second, and both back; the gap appears and the closing walk is drawn. A carried arrow shows its change only once the loop closes. Readouts compare gap over step squared with the bracket, and arrow change over step squared with minus the operator, beside the bare commutator. It proves the gap belongs to the fields, while the change around the closed loop belongs to the curvature: zero on the plane for every pair of fields.
- [[falling-ring-of-crumbs]] (supporting): Shows the map from separations to relative accelerations that falling test masses read. *Sketch:* A ring of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it. Sliders for mass and distance; readouts of the eigenvalues in units of GM over r cubed, minus two, one and one, and their zero sum.

## Tutor moves

**Open with**

- Picture a flat playground with a pole. You walk one metre directly away from the pole, then one metre around it with the pole on your left. Then you walk one metre directly toward it, and one metre around it with the pole on your right. Do you end exactly where you started? *(prediction)*
- You follow two walking instructions on a playground, then each one in reverse, and you miss your starting spot by a few centimetres. Is that by itself a sign that the ground is curved? *(reflection)*

**If the learner is stuck**

- *The learner cannot see why the playground walk misses the start.* → Draw two circles around the pole and two spokes through the ends of the walk around it, and show that the inner circle is shorter between the spokes. *Uses:* `ways_in/instructions-that-miss-the-start`
- *The learner finds a nonzero curvature operator on the flat plane.* → Recompute $[u,v]$ from $u^\nu\partial_\nu v^\mu - v^\nu\partial_\nu u^\mu$ and check that the bracket term equals the bare commutator. *Uses:* `checks/polar-unit-frame`

**Common questions**

- *Why not just use instructions that always bring you back to your starting spot?* (entry) Sometimes you can. In a rectangular hall, take 1 metre toward one wall and 1 metre toward the wall next to it. Those two instructions and their reverses always bring you back to your starting spot. But many natural instructions, like walking around a pole, do not. The closing walk lets the recipe accept any pair of instructions and still measure only the ground. *Uses:* `ways_in/instructions-that-miss-the-start`
- *Is the curvature operator different from the Riemann curvature tensor?* (entry) They carry the same information. The tensor is a table of numbers kept at every place. The operator is that table used as a recipe: hand it two instructions and an arrow, and it reports how the arrow comes back changed around the tiny finished loop. *Uses:* `ways_in/instructions-that-miss-the-start`, `ways_in/two-orders-minus-the-gap`

**Switching levels**

- To working when: asks how to compute it; uses covariant derivatives or Christoffel symbols. Go to the definition and the polar unit-field control. *Uses:* `ways_in/two-orders-minus-the-gap`, `checks/polar-unit-frame`
- To formal when: asks why it is a tensor; works with frames or differential forms. Present the operator as an endomorphism-valued 2-form and derive its frame components. *Uses:* `ways_in/endomorphism-valued-two-form`, `derivations/components-in-any-frame`
- To research when: asks about sphere theorems, holonomy groups or gauge theory. Contrast the two curvature operators and open the research horizon. *Uses:* `ways_in/which-curvature-operator`, `research_horizon/positive-curvature-operators`

**Pronunciations:** Riemann → REE-mahn; Levi-Civita → LEH-vee CHEE-vee-tah; Cartan → kar-TAHN; Böhm → BURM; Wilking → VIL-king; Fubini → foo-BEE-nee; Bochner → BOKH-ner; Petrov → peh-TROFF

**Voice notes:** Say 'the curvature operator of u and v acting on w' for the calligraphic R. Keep 'closing walk' at every rung.

## History

- **Tullio Levi-Civita (1917).** Defined parallel transport on Riemannian manifolds and used it to give Riemann's curvature a geometric meaning. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–205, doi:10.1007/BF03014898
- **Élie Cartan (1923).** Described a connection by what it does to frames carried around small closed curves, with curvature as the rotation and torsion as the displacement such a curve produces. Élie Cartan (1923), *Sur les variétés à connexion affine et la théorie de la relativité généralisée (première partie)*, Annales scientifiques de l'École Normale Supérieure 40, 325–412, doi:10.24033/asens.751
- **Chen Ning Yang, Robert L. Mills (1954).** Built a gauge field for isotopic spin whose field strength contains a commutator of the potentials; it was later recognized as the curvature of a connection. Chen Ning Yang, Robert L. Mills (1954), *Conservation of isotopic spin and isotopic gauge invariance*, Physical Review 96, 191–195, doi:10.1103/PhysRev.96.191

## Research horizon

- **Holonomy algebras from curvature operators.** The Ambrose–Singer theorem says the Lie algebra of the holonomy group at a point is spanned by curvature operators at all points, carried back by transport. Combined with the Bianchi identities, this restricts which holonomy groups can occur, the basis of Berger's classification for irreducible manifolds that are not locally symmetric. Warren Ambrose, Isadore M. Singer (1953), *A theorem on holonomy*, Transactions of the American Mathematical Society 75, 428–443, doi:10.1090/S0002-9947-1953-0063739-1; Marcel Berger (1955), *Sur les groupes d'holonomie homogènes de variétés à connexion affine et des variétés riemanniennes*, Bulletin de la Société Mathématique de France 83, 279–330, doi:10.24033/bsmf.1464
- **Positive curvature operators and Ricci flow.** Under Ricci flow the curvature operator on bivectors obeys a reaction-diffusion equation whose reaction term is quadratic in the operator. Cones of curvature operators preserved by this flow turn sign conditions into topology: positive curvature operator in dimension four, then in every dimension, and pointwise strict quarter-pinching each force a spherical space form. Richard S. Hamilton (1986), *Four-manifolds with positive curvature operator*, Journal of Differential Geometry 24, 153–179, doi:10.4310/jdg/1214440433; Christoph Böhm, Burkhard Wilking (2008), *Manifolds with positive curvature operators are space forms*, Annals of Mathematics 167, 1079–1097, doi:10.4007/annals.2008.167.1079; Simon Brendle, Richard Schoen (2009), *Manifolds with 1/4-pinched curvature are space forms*, Journal of the American Mathematical Society 22, 287–307, doi:10.1090/S0894-0347-08-00613-9
- **Curvature in gauge theory and gravity with torsion.** Gauge field strengths are curvature operators of connections on internal bundles, and the phase factor of a loop is their holonomy. Gauge formulations of gravity treat Lorentz curvature and torsion as field strengths of rotations and translations; in Einstein–Cartan theory, spin density sources torsion. Tai Tsun Wu, Chen Ning Yang (1975), *Concept of nonintegrable phase factors and global formulation of gauge fields*, Physical Review D 12, 3845–3857, doi:10.1103/PhysRevD.12.3845; Tohru Eguchi, Peter B. Gilkey, Andrew J. Hanson (1980), *Gravitation, gauge theories and differential geometry*, Physics Reports 66, 213–393, doi:10.1016/0370-1573(80)90130-1; Friedrich W. Hehl, Paul von der Heyde, G. David Kerlick, James M. Nester (1976), *General relativity with spin and torsion: Foundations and prospects*, Reviews of Modern Physics 48, 393–416, doi:10.1103/RevModPhys.48.393

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** You stand 10 metres from a pole on a flat playground. Walk 1 metre straight out, 1 metre round with the pole on your left, 1 metre back in, then 1 metre round with the pole on your right, and you overshoot your starting spot by about 9 centimetres, because between two spokes the inner circle is shorter than the outer one. The 9 centimetres is not the ground curving: you walk those 9 centimetres back to close the loop, carry a cardboard arrow round it without letting it swing, and it comes back matching. On a ball a small closed loop would bring it back turned a little. The curvature operator is a recipe: hand it two instructions and an arrow, and it makes the steps tiny, closes the loop and reports the arrow's change divided by the loop's area, with a minus sign in front. I got stuck where it says the recipe shrinks both instructions to tiny steps and then talks about two 1-metre instructions: if they are shrunk, how are they still 1 metre? On Earth a loop round one square metre turns the arrow by 1.4 trillionths of a degree, which is nothing. The swapping question I could only half answer. I believe that doing B first walks the same loop backwards, so the arrow turns the other way, but the list of corners went past me: I could not see why standing after B is nearly the first trip's third corner.

**Stumbles (8)**

- “It shrinks both instructions to tiny steps, adds the closing walk, and carries the arrow around. For two 1-metre instructions at right angles, like A and B, it reports how the arrow comes back changed, divided by the loop's area.”: Reread twice. If the recipe shrinks the instructions to tiny steps, calling them 1-metre instructions one sentence later sounds like a contradiction. Nothing tells the reader that the size of an instruction and the size of the step taken along it are two different things.
- “It shrinks the instructions to make a tiny loop, finishes the loop with a closing walk, and reports how the arrow comes back changed.”: The glossary says a loop is a path that ends exactly where it began, so a loop that still has to be finished contradicts it. This is the same trap the note's opening sentence was already rewritten to avoid.
- “Two small loops side by side give twice the turn, so the turn divided by the loop's area measures the curving at that spot.”: Ambiguous 'the turn' and 'the loop's area' straight after two loops are named. I reread to work out whether it meant one loop or the pair.
- “draw two circles around a dot, 20 and 30 centimetres from it, using a pin, a loop of string and a pencil”: A rule I could not physically follow: one loop of string draws circles of only one size, so the second circle cannot be drawn.
- “For short instructions, swapping two steps moves where you end only by a small gap. A step followed by its reverse nearly cancels. So after B is nearly the first trip's third corner. After B and A is nearly its second. The last corner is nearly its first.”: I could not follow this at all. Each 'nearly' needs both facts applied in turn to a three-part walk, and not one of the three is worked out for me. 'Corner' is used as a technical word with no definition, and 'step' means a part of the trip here but a tiny move in the entry way.
- “If a walk on flat ground that should bring you home misses by a few centimetres, is that a sign that the ground is curved?”: The question answers itself: it tells me the ground is flat, so 'no' costs no thought and the opener invites nothing.
- “In a rectangular hall, one metre toward the front wall and one metre toward a side wall always meet up.”: A direction with no reference: a rectangular hall has no front wall unless someone says which one it is. 'Meet up' is also a third phrase for ending where you began, next to 'bring you back to your starting spot' and 'end where you began'.
- “Swapping two steps of a recipe often changes nothing.”: One word in two senses: the note calls the curvature operator a recipe, so a learner hearing this thinks the tutor means the curvature operator.

**Fixes**

- Entry way instructions-that-miss-the-start: the recipe now 'takes a tiny fraction of each instruction' instead of shrinking the instructions to tiny steps, so the 1-metre scoping in the next sentence no longer reads as a contradiction. The claim, its scope and its minus sign are unchanged. The summary and the curvature-operator glossary entry were changed the same way, so one action keeps one name.
- Curvature-operator glossary entry: the tiny path is now called a loop only after the closing walk is added, which restores agreement with the glossary entry for loop.
- Recap: 'twice the turn of one' and 'a loop's turn divided by its area' remove the ambiguous 'the turn' and 'the loop'.
- Try-it: a piece of string held at each length replaces the loop of string, so both circles can actually be drawn, and the opening sentence was split in two to stay short. Nothing else in the try-it changed, and its answer of about 3 centimetres is untouched.
- Check swap-the-instructions: the answer now defines a corner, states the two facts it uses, and works all three corner matchings one at a time instead of asserting them. A part of a trip is called a walk, as the entry way calls it, so 'step' is no longer used for both a part of a trip and a tiny move. The hint now says 'each trip'. The prediction, the 2 degrees, the numeric answer and the key points are unchanged.
- Opening question gap-or-curving: the setting is still named (a playground, two instructions and their reverses) but the word flat is gone, so the question no longer hands over its answer.
- Common question why-not-steps-that-meet: the hall's walls are now named relative to each other, the four walks are spelled out, and 'meet up' is replaced by the note's own phrase.
- Misconception order-does-not-matter: 'a cooking recipe', so the tutor's spoken line cannot be heard as the curvature operator.
- Budgets: the entry explanation grew by one word, to 439 against a 400 cap and a 440 review allowance; the way's other fields grew by seven words and the tutoring part by about ninety, both well inside their caps. Nothing was dropped or compressed.

**Concerns**

- This note was already at revision 4 with both reviews recorded when this novice review was scheduled as the first review. Its findings replace the earlier novice record, whose one open item (the minus sign in front of the change) was read again here and still reads cleanly. The earlier re-read entry is kept below as history; it is dated to revision 4, before this review.
- Learner-visible text changed after the physics sign-off, so review.physics now covers revision 4 while the note is at revision 5. The validator says so. The physics reviewer should diff-check exactly these changes: the fraction-of-an-instruction wording in the summary, the entry way and the glossary, and the rebuilt answer of check swap-the-instructions.
- The entry explanation sits at 439 words against a 400 cap, one word inside the review allowance. A later reviewer has no room left and must cut before adding.
- The glossary entry for the Riemann curvature tensor says the tensor lists how the arrow comes back changed divided by the loop's area, with no minus sign, while the curvature-operator entry says the report carries a minus sign, and the common question operator-or-tensor says the two carry the same information. A sharp reader will ask whether the tensor is the operator with the sign dropped. The same sentence appears in riemann-curvature-tensor.json, so an editor should align both notes rather than only this one.
- The swap check still rests on 'swapping two of the walks moves where you end by only a small gap', which the entry way shows only through the 9-centimetre and the 33-centimetre cases. The physics reviewer should confirm that the new corner chain is right to leading order and that the turn is unchanged by the small gaps.
- The note has one entry way, so 'walking a loop the other way turns the arrow by the same amount the other way' still reaches the reader only through the recap.
- The proposed visual four-legs-that-do-not-close should say 'a tiny fraction of each instruction' rather than shrinking, and should keep 'in reverse', 'closing walk' and 'corner' as the note now uses them.

**Re-read** (2026-09-13, revision 4): 1 stumbles in 4 changed passages

- “By custom, the report puts a minus sign in front of that change.”: Step taken on trust: a beginner knows minus signs on numbers, but not what a minus sign in front of an arrow's change means for the report.
- Fix: Spelled out what the minus sign does in the entry explanation of instructions-that-miss-the-start (claim unchanged). Entry explanation now 438 words against a 400 cap, inside the 440 review allowance; nothing dropped. The glossary sentence with the minus sign and the shortened simplifies read cleanly and are unchanged.

**Re-read** (2026-09-13, revision 7): 2 stumbles in 3 changed passages

- “The table puts a minus sign in front of that change, by the same custom the curvature operator uses. The arrow goes around the loop without swinging.”: Reread once. The new sign sentence was dropped between the sentence that says what the table lists and the rule that says how the arrow is carried, so the arrow rule arrives as an afterthought and I looked back to check which arrow it meant. The trailing qualifier also ends the sentence on a cross-reference rather than on the sign itself, and 'that change' is now two nouns away from the change it names.
- “Antisymmetry gives $\mathcal{R}(u,\xi)u = -\mathcal{R}(\xi,u)u$, and $\mathcal{R}(\xi,u)u$ has components $R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.”: Working rung, climbing reader. The step says 'antisymmetry' without saying in which pair, and this note's own notation trap puts the loop plane in the tensor's last two slots, so a reader who has just read that trap has two antisymmetries to choose from before seeing which swap is meant.
- Fix: Reordered the last two sentences of the Riemann-curvature-tensor glossary entry and replaced 'that change' with 'the change it lists'; the sign, the custom and the no-swinging rule are unchanged.
- Fix: Named the antisymmetry in step five of deviation-from-the-operator as the operator's first two slots; no equation, sign or index changed.
- Fix: Nothing dropped or compressed. Tutoring part gains 3 words (3089 of 3500) and the derivation gains 5 (support part 1771 of 2500); the 439-word entry way was outside this re-read's two strings and was not touched.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Entry playground walk: at 10 m from the pole, 1-metre instructions A, B, A in reverse, B in reverse leave you about 9 cm past the start, one eleventh of a metre; the spoke argument (the circle 10 m out is 10 elevenths as long as the circle 11 m out between the two spokes).: Re-derived from scratch. A puts you at r = 11 m; B turns you through 1/11 rad; A in reverse returns you to r = 10 m on the spoke through the end of B; B in reverse needs r*(1/11) = 10/11 m. Closed form gap = eps^2/(r+eps). python3 for every instance. → Correct. r=10, eps=1: 0.0909 m = 9.09 cm. Check playground-gap r=5, eps=1: 1/6 m = 16.67 cm (numeric field 16.7 cm, rel_tol 0.10). Problem bigger-steps r=10, eps=2: 1/3 m = 33.33 cm (numeric field 33.3 cm, rel_tol 0.05), ratio to the 9 cm case 3.667, so 'nearly four times', and the solution's reason (B walked 12 m out, not 11) is the right one: the ratio is 4 x 11/12. Try-it with 20 cm and 30 cm circles and 10 cm moves: 100/30 cm = 3.33 cm, so 'about 3 centimetres'. Every numeric field, unit and tolerance agrees.
- Working bridge: the flow gap is eps^2 [u,v]; for the playground unit fields [u,v] = -e_theta_hat/r, so 1-metre steps predict a 10 cm gap along -e_theta_hat, the direction of B in reverse, against the exact 9 cm.: [d_r, r^-1 d_theta] = -r^-2 d_theta = -e_theta_hat/r. Flowed the four legs explicitly in polar coordinates and read the displacement: end angle -1/110 rad at r = 10 m, i.e. -1/11 m along e_theta_hat. Expanded eps^2/(r+eps) = eps^2/r - eps^3/r^2 + ... Orientation: with the pole at the origin and the walker at angle zero facing +theta, the pole lies to the walker's left, so B is +e_theta_hat and B in reverse is -e_theta_hat. → Correct in size, sign, direction and order: leading order 0.100 m, exact 0.0909 m, difference third order.
- Entry recipe and its minus sign: for two 1-metre instructions at right angles the recipe reports the arrow's change divided by the loop's area, with a minus sign in front, which flips the change's direction but keeps its size.: Conventions small-loop row: walking +a, +b, -a, -b gives Delta V^rho = -R^rho_{sigma mu nu} V^sigma a^mu b^nu, so for orthonormal unit fields Delta w = -eps^2 R(u,v)w and the report R(u,v)w = -Delta w / area. python3 on a unit sphere at colatitude 1 rad with eps = 0.2: parallel transport around the flow loop plus the closing walk rotates w = e_theta_hat toward +e_phi_hat by psi = +0.03818 rad, i.e. Delta w = +eps^2 K e_phi_hat, while R(e_theta_hat, e_phi_hat) e_theta_hat = -e_phi_hat/a^2 computed independently. Negating a vector reverses its direction and preserves its length. → Correct, sign included. The claim is exactly true for unit orthogonal instructions, and the simplifies sentence (the answer grows with the instructions' lengths and with closeness to a right angle) matches the bilinearity and antisymmetry of R, whose magnitude goes as |u||v| sin(angle).
- Entry recap: two small loops side by side give twice the turn of one, so a loop's turn divided by its area measures the curving; walking a loop the other way turns the arrow by the same amount the other way.: Turn = integral of K over the region, so equal-area adjacent small loops at nearly constant K add. Reversal gives the inverse holonomy, hence minus the angle. Checked numerically on the sphere (both loop senses). → Correct for small loops at a smooth point with the two loops of equal area and the same sense, which 'side by side' and 'twice the turn of one' supply.
- Entry Earth numbers: a finished loop around one square metre of Earth's ground turns an arrow by about 1.4 trillionths of a degree; that is a hair's width seen from 3 million kilometres, more than seven times the Moon's distance.: python3 with R = 6371 km: K = 1/R^2 = 2.4637e-14 per m^2; in degrees 1.4116e-12. Subtended size at 3e9 m: 2.4637e-14 x 3e9 = 7.39e-5 m = 74 micrometres. 3e6 km / 384 400 km = 7.80. → Correct. 74 micrometres is a human hair's width, and 7.80 is 'more than seven times'.
- Check swap-the-instructions: if the A-first trip turns a fresh arrow 2 degrees toward the walker's left, the B-first trip turns it about 2 degrees toward the right, because the B-first trip visits nearly the same three corners in the opposite order.: Verified the rebuilt corner chain symbolically: the first trip's corners are A(p), BA(p), A^-1 B A(p) and the second trip's are B(p), AB(p), B^-1 A B(p). Swapping the first two walks of A^-1 B A gives A^-1 A B = B, of BA gives AB, and of B^-1 A B gives B^-1 B A = A, so d1 ~ c3, d2 ~ c2, d3 ~ c1, in reverse order, each swap costing only the O(eps^2) commutator gap. python3 on a unit sphere with e_theta_hat and e_phi_hat instruction fields, latitude closing walks, eps = 0.2 at colatitude 1 rad: corner separations |d1-c3| = 0.019, |d2-c2| = |d3-c1| = 0.022 against leg length 0.20 and the predicted gap scale eps^2 cot(theta)/a = 0.026; holonomy angles psi1 = +2.1878 deg and psi2 = -2.1878 deg, summing to zero to machine precision, and psi1 equals K times the signed area. Repeated at eps = 0.1 and 0.05. → Correct. Every step of the new chain holds, the corner gaps are second order as the answer claims, and the two turns are equal and opposite, well inside the 0.3 degree tolerance on the signed numeric field of -2 deg (positive toward the walker's left, modulo 360). The question fixes the starting state ('a fresh cardboard arrow', then 'you set the arrow back to its starting direction'), so the sign is relative and needs no absolute orientation convention.
- Working: on the flat plane with polar unit fields the bare commutator acting on e_r_hat is -e_theta_hat/r^2, the bracket term cancels it exactly, and at r = 10 m the bare commutator would report 0.01 per m^2, about 4e11 times Earth's ground curvature. Check polar-unit-frame at r = 2 m gives -0.25 per m^2 and zero.: Recomputed from Gamma^theta_{r theta} = 1/r and Gamma^r_{theta theta} = -r: grad_{e_theta_hat} e_r_hat = e_theta_hat/r, grad_{e_r_hat} e_r_hat = 0, grad_{e_r_hat} e_theta_hat = 0, so grad_u grad_v e_r_hat = -e_theta_hat/r^2 and grad_v grad_u e_r_hat = 0; [u,v] = -e_theta_hat/r gives the bracket term -e_theta_hat/r^2. python3: 0.01/2.4637e-14 = 4.06e11. → Correct, including both numeric fields of the check (-0.25 per m^2 with abs_tol 0.01, and 0 with abs_tol 1e-6) and their units.
- Problem sphere-unit-frame: bare commutator -e_phi_hat/(a^2 sin^2 theta), operator -e_phi_hat/a^2; at Earth's radius and colatitude 30 degrees, -9.85e-14 and -2.46e-14 per m^2, the bare commutator four times too large.: Derived the given frame derivatives from the sphere metric (grad_{e_phi_hat} e_theta_hat = (cot theta / a) e_phi_hat, grad_{e_theta_hat} e_theta_hat = grad_{e_theta_hat} e_phi_hat = 0), then [u,v] = -(cot theta/a) e_phi_hat and the bracket term -(cot^2 theta/a^2) e_phi_hat. Cross-checked against the constant-curvature form R(u,v)w = K(g(v,w)u - g(u,w)v) with K = +1/a^2, which the course sectional-curvature row fixes. python3: 1/a^2 = 2.4637e-14, 1/sin^2(30 deg) = 4. → Correct; both signed numeric fields and their 2 percent tolerances agree, and the cross-check with K reproduces -K e_phi_hat.
- Components: R(d_mu, d_nu) d_sigma = R^rho_{sigma mu nu} d_rho and (R(u,v)w)^rho = R^rho_{sigma mu nu} w^sigma u^mu v^nu, with the plane in the last two slots.: Re-derived the four-term coefficient from the Leibniz rule with the derivative index first and compared it letter by letter with the conventions Riemann row and with [grad_mu, grad_nu]V^rho = R^rho_{sigma mu nu}V^sigma. → Correct, and the notation traps operator-overall-sign and operator-slot-order state exactly this choice.
- Geodesic deviation in operator form: D^2 xi/dtau^2 = -R(xi,u)u for a family of geodesics with [u,xi] = 0 and zero torsion, matching the conventions row D^2 xi^mu/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma.: Walked the derivation: D^2 xi/dtau^2 = grad_u grad_u xi; zero torsion and [u,xi] = 0 give grad_u xi = grad_xi u; the definition with vanishing bracket gives grad_u grad_xi u = grad_xi grad_u u + R(u,xi)u; grad_u u = 0 along every worldline kills the first term; antisymmetry flips the slots. Then expanded (R(xi,u)u)^mu with the component rule and compared index by index with the conventions row. → Correct. One defect found: step five read 'R(u,xi)u = -R(xi,u)u, with components R^mu_{nu rho sigma}u^nu xi^rho u^sigma', whose antecedent is ambiguous; those components belong to R(xi,u)u, and attaching them to the left-hand side would flip the sign of the result line. Rewritten to name R(xi,u)u explicitly.
- Tidal map: xi -> R(xi,u)u is linear and symmetric on the observer's rest space with trace R_{nu sigma}u^nu u^sigma; in a weak static field its matrix is c^2 R^i_{0j0} = d_i d_j Phi, with eigenvalues -2GM/r^3 vertically and +GM/r^3 horizontally; a vertical 1 m pair at Earth's surface accelerates apart at 3.08e-6 m/s^2 and the trace vanishes.: Symmetry from M_{rho mu} = R_{rho sigma mu nu}u^sigma u^nu with pair exchange; trace from R_{mu nu} = R^rho_{mu rho nu}. Weak field: g_00 = -(1 + 2Phi/c^2) gives Gamma^i_{00} = d_i Phi/c^2 and R^i_{0j0} = d_i d_j Phi / c^2, and u^0 = c supplies the two factors of c. python3 with GM = 3.986e14 and r = 6371 km: d_z^2(-GM/r) = -2GM/r^3 = -3.083e-6 per s^2, d_x^2(-GM/r) = +GM/r^3 = +1.541e-6 per s^2, trace -2+1+1 = 0. → Correct. Check tidal-map-at-earth: +3.08e-6 m/s^2 apart (signed numeric field, rel_tol 0.03), trace zero as vacuum without a cosmological constant requires, and the student's slot swap flips the sign, as the answer says. The way's 'six independent entries' is right for a symmetric three-by-three map.
- Observation atom-gravity-gradiometer: the vertical eigenvalue of xi -> -R(xi,u)u is 2GM/r^3 = 3.08e-6 per s^2, against the standard free-air gradient 3.086e-6 per s^2.: python3: 2GM/r^3 = 3.0828e-6 per s^2; free-air gradient 0.3086 mGal/m with 1 mGal = 1e-5 m/s^2 gives 3.086e-6 per s^2. Sign: the map's vertical eigenvalue is -2GM/r^3, so minus it is positive and the clouds separate, as the entry stated. → Correct, and the two numbers agree to 0.1 percent, which is the right size for the difference between a spherical Earth and the real one.
- Formal way: tensoriality for any connection; frame components R^a_{bcd} with the -C^e_{cd} Gamma^a_{eb} term; Omega = d omega + omega wedge omega; skew-adjointness needs metric compatibility; first Bianchi needs zero torsion; second Bianchi in frame form holds for any connection; component commutator picks up -T^lambda_{mu nu} grad_lambda V^rho.: Re-derived each. Tensoriality from [fX,Y] = f[X,Y] - (Yf)X and the Leibniz rule, with no metric and no torsion used. Frame formula derived from the three terms and checked twice: on a sphere with e_1 = a^-1 d_theta, e_2 = (a sin theta)^-1 d_phi, where Gamma^2_{21} = cot theta/a, every Gamma^a_{1b} = 0 and C^2_{12} = -cot theta/a give R^2_{112} = -1/(a^2 sin^2 theta) + cot^2 theta/a^2 = -1/a^2, matching theta^2(R(e_1,e_2)e_1) = -K; and on the flat polar frame, where -1/r^2 + 1/r^2 = 0 (problem frame-components, numeric field 0 with abs_tol 1e-6). Second Bianchi in frame form from d Omega = Omega wedge omega - omega wedge Omega, which uses only Omega = d omega + omega wedge omega. Component commutator from grad_mu grad_nu V = grad_{d_mu} grad_{d_nu} V - Gamma^lambda_{mu nu} grad_lambda V, whose antisymmetric part is -T^lambda_{mu nu} grad_lambda V with T^lambda_{mu nu} = Gamma^lambda_{mu nu} - Gamma^lambda_{nu mu}; the same argument gives [grad_mu, grad_nu]f = -T^lambda_{mu nu} d_lambda f. → Correct throughout, and consistent with checks torsion-and-the-operator and exterior-derivative-twice and problem skew-and-cyclic, both of whose proofs I worked. One defect found: 'skew-adjointness makes this an infinitesimal rotation or boost' is not an exhaustive classification in Lorentzian signature, where a null rotation is neither. Rewritten as the orthogonal algebra of the metric, with the two signatures named.
- Gauge bridge: with D_mu = d_mu - i(q/hbar)A_mu, [D_mu, D_nu]psi = -(i q/hbar)F_{mu nu} psi with F_{mu nu} = d_mu A_nu - d_nu A_mu; loop holonomy exp(+i q Phi/hbar); non-abelian curvature d A + A wedge A transforming by conjugation; gravity alone has the first Bianchi identity, pair exchange and contractions.: Expanded the commutator term by term against the conventions gauge-covariant-derivative row. Consistency check: Hol = 1 - eps^2 R = 1 + i(q/hbar)F_{mu nu} eps^2 = 1 + i q Phi/hbar for the flux Phi through the loop, matching the conventions Aharonov-Bohm row (+q Phi/hbar). The three extra structures follow from the endomorphism indices and the form indices lying in the same bundle for TM. → Correct, signs and hbar factors included.
- Research way: the bivector operator defined by <R(X wedge Y), Z wedge W> = g(R(Z,W)Y,X) with e_i wedge e_j orthonormal reproduces the course sectional curvature and equals a^-2 times the identity on a round sphere of radius a; the positivity hierarchy and its failures; CP^2 with Fubini-Study normalized to holomorphic sectional curvature 4 has sectional curvatures in [1,4] and Euler characteristic 3, while S^4 has 2 and RP^4 has 1; the spinor Bochner term is a quarter of the scalar curvature.: Evaluated the quadratic form on a unit simple bivector: <R(X wedge Y), X wedge Y> = g(R(X,Y)Y,X), which the notation trap already fixes as the course sectional curvature, positive on a sphere. Constant curvature K gives R = K Id on all of Lambda^2. Tried the dimension counterexamples: in dimension three Lambda^2 is three-dimensional and every bivector is simple, so positive sectional curvature and a positive curvature operator coincide there; in dimension four and higher CP^2 breaks the first converse and S^2 x S^2 (positive Ricci, zero sectional curvature on mixed planes) breaks the second. Euler characteristics checked (chi(CP^2) = 3, chi(S^4) = 2, chi(RP^{2k}) = 1). Lichnerowicz: D^2 = nabla* nabla + R/4. → Correct, including the dimension-three rescoping already in the note and the logic of check positive-sectional-not-enough, which I worked: Hamilton's four-dimensional theorem plus chi = 3 does rule out a positive curvature operator on CP^2.
- Glossary sign consistency: the operator entry says the report carries a minus sign, the tensor entry said the table lists the change divided by the area with no sign, and the common question operator-or-tensor says the two carry the same information.: In the course convention R^rho_{sigma mu nu} = -Delta w^rho/(a^mu b^nu), so a table listing the change divided by the area lists minus the Riemann components, not the Riemann components. Read all three items together as a learner would. → Fixed. The tensor entry now carries the same minus sign in the same words, so the two glossary entries and the common question no longer disagree. The sentence was split so no sentence exceeds 32 words.
- Notation traps agree with the conventions file: operator overall sign, slot order, and the name 'curvature operator'.: Compared each course_choice with the Riemann, small-loop-holonomy and sectional-curvature rows of course-conventions.md. → Consistent. The operator's own index-free definition and the bivector operator's normalization are still absent from the conventions file; recorded as a concern, not invented here.
- All twelve references: Levi-Civita 1917; Cartan 1923; Yang and Mills 1954; Ambrose and Singer 1953; Berger 1955; Hamilton 1986; Boehm and Wilking 2008; Brendle and Schoen 2009; Wu and Yang 1975; Eguchi, Gilkey and Hanson 1980; Hehl, von der Heyde, Kerlick and Nester 1976; Snadden, McGuirk, Bouyer, Haritos and Kasevich 1998.: Web searches against publisher and archive records: Springer (BF03014898), Numdam and the ENS DOI 10.24033/asens.751, APS (PhysRev.96.191, PhysRevD.12.3845, RevModPhys.48.393, PhysRevLett.81.971), AMS (S0002-9947-1953-0063739-1 and S0894-0347-08-00613-9), EUDML for Berger (Bull. SMF 83, 279-330), Project Euclid for Hamilton (10.4310/jdg/1214440433, vol. 24, 153-179), arXiv math/0606187 and Annals 167 for Boehm-Wilking, ScienceDirect for Physics Reports 66, 213-393. → All twelve confirmed in authors, year, title, venue, volume, pages and identifier; verified stays true for all. The only loose end is the Levi-Civita end page, which different catalogues give as 204 or 205; 173-205 is the commonly cited range and is kept.
- History scope: Levi-Civita defined parallel transport and gave Riemann's curvature a geometric meaning; Cartan read curvature as the rotation and torsion as the displacement a small closed curve produces; Yang and Mills built a field strength later recognized as a curvature.: Compared each contribution with the confirmed title and subject of the work; checked that no 'first' claim is made beyond what the work supports. → Accurately scoped. The Yang-Mills entry correctly says 'later recognized', not that they knew it.
- Structure: prerequisites direct and acyclic, assumes consistent, tier requirements met, objectives evidenced, visuals declared.: Read the prerequisite notes' own prerequisite lists: riemann-curvature-tensor, covariant-derivative, lie-bracket, holonomy and levi-civita-connection do not list this concept, so there is no cycle, and parallel-transport (the entry way's only 'assumes') is an entry prerequisite of riemann-curvature-tensor. Counted evidence: all eight checks and five problems evidence an objective at its own rung; the advanced tier's formal rung has two formal checks and two formal problems; three research_horizon topics carry two reviews. Both visuals are proposals with sketches. → Correct; the validator's only remaining warning is the expected one about review.novice covering an older revision.

**Counterexamples tried**

- Flat cone with a loop around its tip: nonzero holonomy on an intrinsically flat surface. The entry's 'flat ground' is a playground, a plane, and the recipe uses tiny loops at a smooth point, so the claim 'as on every loop on flat ground' survives.
- Flat Moebius band: a loop along it returns the arrow reflected, not rotated. Not a plane, and tiny loops sit in an orientable patch. Survives.
- Flat annulus, and a flat torus: non-simply-connected but with trivial holonomy, so they do not threaten the entry claim either way.
- Great circle on a ball: a large loop can bring the arrow back matching. The entry says only that a small finished loop brings it back turned a little. Survives.
- Figure-eight loop: its two lobes are walked in opposite senses, so their turns subtract. The recap says 'two small loops side by side', each walked the same way round, so it survives; a figure-eight is not that case.
- Rectangular hall with commuting instructions: no gap, no closing walk needed. The common question why-not-steps-that-meet says exactly this.
- Flat plane with the non-commuting polar unit fields: bare commutator nonzero, operator zero. The note's control case; survives and is the point of check polar-unit-frame.
- Bent but intrinsically flat surface (a rolled paper tube): operator zero. The note never calls bending curvature.
- Instructions of unequal length or not at right angles: the entry claim is scoped to 1-metre instructions at right angles, and simplifies gives the bilinear dependence, which I checked against |u||v| sin(angle).
- Instructions swapped: the two loops are nearly the same loop walked the other way, so the turns are equal and opposite; verified numerically to machine precision for e_theta_hat and e_phi_hat on a sphere.
- Connection with torsion: tensoriality survives untouched, while the first Bianchi identity and the component commutator both change, as the note and check torsion-and-the-operator state.
- Flat connection on a vector bundle: d_nabla squared is zero there, which is why the note says the square vanishes for scalar-valued forms and for flat connections, not in general. Survives.
- Null rotation in Lorentzian signature: neither a rotation nor a boost, which broke 'skew-adjointness makes this an infinitesimal rotation or boost'. Rescoped to the orthogonal algebra of the metric.
- Dimension three: every bivector is simple, so positive sectional curvature and a positive curvature operator coincide; the note already scopes 'neither converse holds' to dimension four and higher. Survives.
- S^2 x S^2: positive Ricci curvature but zero sectional curvature on mixed planes, confirming the second converse fails in dimension four and higher.
- CP^2 with the Fubini-Study metric: positive sectional curvature, non-positive curvature operator. The note's own separating example; confirmed by Euler characteristic.
- Non-static or strong field for the tidal matrix: the weak-field eigenvalues -2, +1, +1 in units of GM/r^3 are scoped by the way's simplifies to a static field and slow test masses.
- Slots swapped in geodesic deviation: the sign flips, which check tidal-map-at-earth makes the point of its last part.

**Fixes**

- Glossary riemann-curvature-tensor: the entry said the table 'lists how the arrow comes back changed, divided by the loop's area' with no sign, while the curvature-operator entry says the report carries a minus sign and the common question operator-or-tensor says the two carry the same information. In the course convention the Riemann components are minus the change per area, so the sign-free sentence was wrong and the three items disagreed. Added one short sentence, 'The table puts a minus sign in front of that change, by the same custom the curvature operator uses.', in the entry way's own words. Nothing else in the entry rung changed.
- Derivation deviation-from-the-operator, step five: 'R(u,xi)u = -R(xi,u)u, with components R^mu_{nu rho sigma} u^nu xi^rho u^sigma' left the antecedent of 'with components' ambiguous, and reading it as the left-hand side would flip the sign of the result line. Now names R(xi,u)u explicitly. The result line is unchanged.
- Formal way endomorphism-valued-two-form: 'skew-adjointness makes this an infinitesimal rotation or boost' is not exhaustive in Lorentzian signature, where a null rotation is neither. Now: skew-adjointness puts the generator in the orthogonal algebra of the metric, an infinitesimal rotation in Riemannian signature and an infinitesimal Lorentz transformation in Lorentzian signature.
- Nothing was dropped or compressed. The glossary grew by 19 words and the formal ways by 14, both far inside their caps; the entry way explanation was not touched and stays at 439 words.
- Revision bumped 5 to 6 for the two entry- and working-rung changes.

**Concerns**

- Stage history: this physics review is the second on this note. The first covered revision 4 and its diff check is kept below as history. The novice review then re-ran as a scheduled first review, edited eleven entry strings and took the note to revision 5. I diff-checked all eleven of those strings against the snapshot of revision 4 and found no accuracy defect: the 'takes a tiny fraction of each instruction' wording in the summary, the entry way and the operator glossary states the same claim as the wording it replaced, and the rebuilt corner chain in check swap-the-instructions is correct step by step, which I verified symbolically and numerically on a sphere. None of them needed a fix.
- Cross-note: the same sign-free sentence about the Riemann tensor that I fixed here still stands in knowledge/concepts/curvature/riemann-curvature-tensor.json, which owns the term and is physics-reviewed at revision 3. That note is outside this task, so I did not edit it; an editor should carry the same minus-sign sentence there, or decide the other way and change both. Until then the two notes describe the tensor's sign differently, and this note is the one that agrees with the conventions file.
- Conventions gap, still open from the writer and the first physics review: course-conventions.md has no row for the index-free operator R(X,Y)Z, and none for the sign and normalization of the operator on bivectors. The note's choices (R(X,Y)Z = grad_X grad_Y Z - grad_Y grad_X Z - grad_{[X,Y]}Z, and <R(X wedge Y), Z wedge W> = g(R(Z,W)Y,X) with e_i wedge e_j orthonormal) follow from the Riemann and sectional-curvature rows and are stated in the notation traps, but the rows should be added rather than left implicit.
- Budget: the entry way explanation sits at 439 words against a 400 cap and a 440 review allowance. I added nothing to it, but a later stage has one word of room and must cut before adding.
- Prerequisites still differ from the registry for covariant-derivative, holonomy and levi-civita-connection; run sync_registry.py. Both visuals, four-legs-that-do-not-close and falling-ring-of-crumbs, are still proposals rather than catalog entries.
- A novice re-read now owes exactly two strings: the added sentence in the Riemann-tensor glossary entry (entry rung) and the reworded components clause in derivation deviation-from-the-operator (working rung). The formal way's change is above both re-read rungs.

**Diff check** (2026-09-13, revision 4)

- Entry explanation of instructions-that-miss-the-start, changed sentence: 'By custom, the report puts a minus sign in front of that change, which flips the change's direction but keeps its size.': Read in context: 'that change' is the arrow's change around the finished loop, and the report is that change divided by the loop's area. In course conventions the change around a small loop is Delta w = -eps^2 R(u,v)w, so the report for unit orthonormal instructions is R(u,v)w = -Delta w/eps^2. Negating a vector reverses its direction and keeps its length, and the 'which' clause is about the minus sign alone, before the division by area. python3 check: transport of w = e_theta on a unit sphere at colatitude 1 rad around a small loop with eps = 0.01 gives Delta w = (-3.0e-9, 1.003e-4) in (theta, phi-hat), so -Delta w/eps^2 = (3e-5, -1.003), against R(u,v)u = K(<v,u>u - <u,u>v) = (0, -1). Also read as a turn: an arrow that came back turned toward the left has a report pointing the other way with the same size. → Correct, and the reworded sentence claims exactly what the revision 3 sentence did, plus a true gloss of what the minus sign does. It is consistent with the glossary entry for curvature operator ('with a minus sign in front'), the recap, the takeaway and simplifies. No fix needed.
- Fix: None. The diff check changed no learner-visible text; revision stays 4.

**Diff check** (2026-09-13, revision 7)

- Scope of this diff check: note_diff.py against riemann-curvature-operator.before-reread.json reports exactly two changed learner-visible strings, $.glossary[riemann-curvature-tensor].plain_definition (entry) and $.derivations[deviation-from-the-operator].steps[4] (working). No other learner-visible string differs.: python3 knowledge/_tools/note_diff.py on the before-reread snapshot against the current note; both changed strings then read inside their whole field (the full glossary definition, and the step list with the goal and result). → Confirmed: two strings, one entry, one working. Both are rewordings; neither adds or removes a number, sign, index, condition or scope.
- Entry glossary, reordered sentences: the Riemann curvature tensor lists, for each tilt of a tiny loop and each starting direction, how the arrow comes back changed divided by the loop's area, with a minus sign in front of that listed change, by the same custom the curvature operator uses; the arrow is carried without swinging.: Compared claim by claim with the revision 6 sentence pair: the same three claims (what is listed, the minus sign with its shared custom, the no-swinging rule) in a new order, with 'that change' replaced by 'the change it lists', which names the same quantity as the preceding sentence. Checked the sign against the conventions small-loop holonomy row, Delta V^rho = -R^rho_{sigma mu nu} V^sigma a^mu b^nu, and against the note's own key equation flow-loop-holonomy, Delta w = -eps^2 R(u,v)w. Independent numerical check with python3: parallel transport of V with (theta, phi) components (0.4, 0.7) around the coordinate rectangle +a, +b, -a, -b at colatitude 1.0 rad on the unit sphere with eps = 0.02, by RK2 integration of the transport equation with 20000 steps per leg. → Correct and unchanged in content. Measured Delta V = (-1.9954e-4, +1.6098e-4) against the predicted -R(a,b)V = (-1.9826e-4, +1.6000e-4): agreement to 0.6 percent at eps = 0.02, the expected third-order residual. So the tensor's entries are minus the change per unit area, and the entry sentence states the sign the course convention requires. The custom is the same one the curvature operator uses, since the operator enters the same holonomy formula with the same minus sign. Rewording only; no fix needed.
- Working derivation step five, reworded: antisymmetry in the operator's first two slots gives R(u,xi)u = -R(xi,u)u, and R(xi,u)u has components R^mu_{nu rho sigma} u^nu xi^rho u^sigma.: Re-derived the antisymmetry from the note's own definition: R(X,Y)Z = grad_X grad_Y Z - grad_Y grad_X Z - grad_{[X,Y]}Z, and swapping X and Y flips the first two terms and, through [Y,X] = -[X,Y], the third, so R(X,Y) = -R(Y,X) for any connection, with or without torsion; the operator's first two slots are its two vector arguments X and Y. Checked the naming against the note's key equation operator-components, (R(u,v)w)^rho = R^rho_{sigma mu nu} w^sigma u^mu v^nu, and against notation trap operator-slot-order: the operator's first two slots are the tensor's last two, which are the antisymmetric pair of the coordinate formula, so the qualifier picks out exactly one antisymmetry and it is the right one. Re-derived the component line by substituting w = u, first argument xi, second argument u, then renaming indices, and compared it with the conventions geodesic deviation row. → Correct on both counts, and the reworded step claims exactly what the bare 'Antisymmetry gives' claimed, with the pair named. The component line gives R^mu_{nu rho sigma} u^nu xi^rho u^sigma, so the derivation's result D^2 xi/d tau^2 = -R(xi,u)u is the conventions row D^2 xi^mu/d tau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma exactly. The new phrase also matches the wording of check tidal-map-at-earth ('swaps the first two slots of the operator', 'Swapping the first two slots flips the sign'), so operator slots are named the same way throughout the note. No fix needed.
- The two rewordings leave the rest of the derivation and the surrounding numbers intact.: Reworked the unchanged steps of deviation-from-the-operator in course conventions: D^2 xi/d tau^2 = grad_u grad_u xi; zero torsion with [u,xi] = 0 gives grad_u xi = grad_xi u, hence grad_u grad_u xi = grad_u grad_xi u; the definition with vanishing bracket gives grad_u grad_xi u = grad_xi grad_u u + R(u,xi)u; every worldline being a geodesic gives grad_u u = 0 and so grad_xi grad_u u = 0. Recomputed the numbers of check tidal-map-at-earth with python3 for GM = 3.986e14 m^3 s^-2 and r = 6371 km. → The chain closes on the conventions row, and GM/r^3 = 1.5414e-6 s^-2 with 2GM/r^3 = 3.0828e-6 s^-2, so the check's 3.08e-6 m s^-2 for a 1 m vertical pair and its zero trace (-2 + 1 + 1) stand unchanged.
- Fix: None. Both reworded strings are true, are consistent with course conventions and with the rest of the note, and claim exactly what the revision 6 strings claimed. This diff check changed no learner-visible text, so the revision stays 7 and review.physics.reviewed_revision is set to 7.
- Fix: Reported, not fixed here, because it lies outside this diff check's two strings and outside this note: the owning note knowledge/concepts/curvature/riemann-curvature-tensor.json (revision 3) defines the same term in its entry glossary and summary as listing 'how the arrow comes back changed, divided by the loop's area' with no minus sign, which is off by a sign from the conventions small-loop holonomy row. This note's glossary entry states the sign. An editor should carry the sign sentence into the owning note.
- Fix: Reported, not fixed here: course-conventions.md still has no row for the index-free operator R(X,Y)Z = grad_X grad_Y Z - grad_Y grad_X Z - grad_{[X,Y]}Z, nor for the sign and normalization of the symmetric curvature operator on bivectors. Both choices are stated only in this note's notation traps operator-overall-sign and name-curvature-operator, and both agree with the tensor rows that do exist.
