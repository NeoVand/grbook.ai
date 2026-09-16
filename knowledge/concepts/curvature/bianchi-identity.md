---
type: "concept"
schema_version: 2
id: "bianchi-identity"
title: "Bianchi identity"
tagline: "Why curving cannot change from place to place in just any way"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["second Bianchi identity", "differential Bianchi identity"]
prerequisites: ["riemann-curvature-tensor", "riemann-tensor-in-normal-coordinates", "symmetries-of-the-riemann-tensor", "covariant-derivative-of-a-tensor", "holonomy", "torsion-free-connection"]
leads_to: ["contracted-bianchi-identity", "weyl-tensor-field-equation", "bianchi-identity-in-differential-forms"]
visuals: ["cube-of-small-loops", "falling-ring-of-crumbs"]
---

# Bianchi identity

*Why curving cannot change from place to place in just any way*

`bianchi-identity` · curvature · core · physics-reviewed (revision 8)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[riemann-tensor-in-normal-coordinates]] (working) · [[symmetries-of-the-riemann-tensor]] (working) · [[covariant-derivative-of-a-tensor]] (working) · [[holonomy]] (formal) · [[torsion-free-connection]] (formal)  
**Opens:** [[contracted-bianchi-identity]] · [[weyl-tensor-field-equation]] · [[bianchi-identity-in-differential-forms]]  
**Related:** [[cyclic-identity]] · [[ricci-identity]] · [[boundary-of-a-boundary-vanishes]] · [[maxwell-equations-in-differential-forms]] · [[identity-versus-equation]] · [[gauge-field-strength]]  
**Visuals:** ★ [[cube-of-small-loops]] · [[falling-ring-of-crumbs]]

> Carry an arrow around each of the six faces of a tiny box, each counterclockwise seen from outside, and add up how the arrow comes back changed. Every edge is walked once in each direction, so in any smoothly curved space the changes add up to nothing. Opposite faces nearly cancel, and the three amounts they leave over must balance. So curving cannot change from place to place in just any way. This rule is the Bianchi identity.

## You will be able to

**Entry**
- Explain why the changes from carrying an arrow around all six faces of a tiny box add up to nothing. `objectives/explain-the-box-rule` ← `checks/the-sixth-trip`, `problems/tent-and-open-box`
- Use the leftovers of the three pairs of opposite faces to predict one leftover from the other two, and tell whether the curving changes. `objectives/use-the-leftovers` ← `checks/leftover-of-the-third-pair`
- Explain why no experiment can find a tiny box that breaks the rule. `objectives/tell-identity-from-law` ← `checks/an-experiment-to-break-it`

**Working**
- Prove the identity at a point where the connection vanishes, and explain why it then holds in every chart. `objectives/prove-at-a-point` ← `checks/why-special-coordinates-suffice`, `problems/empty-in-two-dimensions`
- Distinguish the Bianchi identity from the cyclic identity by what data each needs. `objectives/distinguish-first-and-second` ← `checks/which-identity-at-one-point`
- Use the static weak-field form of the identity to predict how one tidal reading changes from how another does. `objectives/predict-tidal-gradients` ← `checks/tidal-gradient-at-goce-height`

**Formal**
- State the identity for a general connection, including torsion, and say which steps need a metric. `objectives/state-the-hypotheses` ← `checks/does-it-need-a-metric`
- Count the independent relations the identity and its contraction impose at a point. `objectives/count-its-content` ← `checks/count-the-relations`
- Prove that curvature equal on every plane at every point is constant in three or more dimensions. `objectives/apply-to-constant-curvature` ← `problems/curvature-constant-on-every-plane`

## Ways in

### 1. Six loops around a box · entry · picture

*If you carry an arrow around every face of a tiny box, what do the six changes add up to?*

**Recap:** The arrow test: carry an arrow around a loop, a path that ends where it began, and never let it swing any way at all. Around a tiny loop in a curved space, the arrow usually comes back changed a little. Walking the loop the other way round gives the opposite change. Take two tiny loops that share an edge, walked the same way round. Their changes add up to the change around the path along the outside of both, because their shared edge is walked once each way.

Picture a tiny cardboard box floating in a curved space with three directions. Pick one corner of the box and call it the home corner.

Start at the home corner with an arrow. Carry it around one face that touches the home corner, along the face's four edges, and back home. Never let the arrow swing. Go around the face counterclockwise, seen from outside the box, looking at that face.

Back home, the arrow has usually turned a tiny bit, so its tip has moved a tiny distance. How far the tip moved, and which way, is the face's change.

Do this for all six faces. Each time, start at home with a fresh arrow, pointing the way the first arrow pointed when it set off. Three faces touch the home corner. To reach each of the other three, carry the arrow along one edge, go around the face, and come back along the same edge. The walk out and the walk back along that edge undo each other, so only the trip around the face leaves a change.

Now add the six changes, the way you add small steps: 3 steps ahead and 1 step back leave you 2 steps ahead. What do the six changes add up to?

Look at any edge of the box. It belongs to two faces. Going counterclockwise around each of them, seen from outside, you walk that edge once in each direction.

Join two faces that share an edge. The path along the outside of both faces together is called their outline. Their two changes add up to the change around the outline, because the shared edge is walked once each way.

Keep joining faces one at a time. Five faces joined together make a box with its lid missing. Their outline is the rim: the four edges of the sixth face. Each rim edge also belongs to the sixth face, and you walk it the other way going around that face. So the outline goes around the sixth face the opposite way, and the first five changes add up to the opposite of the sixth change.

That means the six changes of a tiny box add up to nothing.

Adding changes like steps is not quite exact. But as the box shrinks, the error shrinks much faster than the changes do. So for a tiny box, "nothing" means far smaller than any one face's change.

**Try it:** On each face of an empty cereal box, draw a ring of small arrows just inside the edges, going counterclockwise, seen from outside the box. Look closely at any edge: the two rings beside it point opposite ways along it. All 12 edges behave this way.

**Takeaway:** Walk all six faces of a tiny box counterclockwise, seen from outside: every edge is walked once each way, so the six changes add up to nothing.

*What this leaves out:* Changes add like steps only for a tiny box. For a box of any size, carry one arrow on all six trips, one after another, in a suitable order. In that joined walk, every walk along an edge is undone by a walk back along the same edge, so the arrow comes back matching its start exactly.

*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[cube-of-small-loops]]<br>*See:* `checks/the-sixth-trip`

### 2. Leftovers from opposite faces · entry · calculation

*What does the zero total of a tiny box say about how curving changes from place to place?*

**Recap:** Carry a fresh arrow from one corner of a tiny box around each of its six faces, counterclockwise seen from outside. Every edge is walked once each way, so the six changes add up to nothing. A loop's tilt is set by the two directions its edges run along. Walking a loop the other way round gives the opposite change.

In "Six loops around a box", the six changes of a tiny box added up to nothing. Give the box's faces names: top and bottom, front and back, left and right. These are only names, like the faces of a box on a shelf. Now look at the faces in opposite pairs.

The top and bottom faces have the same tilt. Each is walked counterclockwise, as seen from outside the box, so the bottom face is seen from below. Looking at a face from its other side reverses which way round the walk goes. So seen from above, the bottom face is walked clockwise, and the top and bottom faces are walked opposite ways.

If the curving were the same at the top face and at the bottom face, their two changes would be opposite, and they would cancel. What is left after adding them is called the pair's leftover. It shows how the curving for loops tilted like the top face changes from the bottom of the box to the top.

Each pair gives a leftover. The front and back pair shows how the curving for loops tilted like the front face changes from back to front. The left and right pair does the same for loops tilted like the left face, from left to right.

The three leftovers are just the six changes, grouped in pairs. The six changes add up to nothing, so the three leftovers add up to nothing too. Suppose one leftover moves the arrow's tip toward the top of the box by 3 millionths of a millimetre, and another moves it toward the bottom by 1. Then the third must move it toward the bottom by 2.

In most boxes the leftovers are much smaller than the face changes. Where the curving changes from place to place, the error from adding changes like steps is smaller than a tiny box's leftovers. So the leftovers really must balance.

So curving cannot change from place to place in just any way. How the curving for one tilt changes in one direction is tied to how the curving for the other two tilts changes in the other two directions. This rule is called the Bianchi identity.

Take the space around Earth at one moment, as clocks at rest around Earth mark moments. Picture a level loop there, 1 kilometre along each edge, floating in the air. It turns an arrow by only about 2 millionths of a billionth of a degree. An arrow pressed against the ground, carried around a loop drawn there, turns far more, because the ground is the surface of a ball.

Going 1 kilometre higher weakens the floating loop's turn by about 1 part in 2,100. So for a box 1 kilometre along each edge, the top and bottom leftover is only about 1 part in 2,100 of one face's change. Nobody notices leftovers that small.

**Try it:** Draw a ring of small arrows going counterclockwise on a clear plastic sheet, as seen from the side facing you. Flip the sheet over and look at the ring from the other side. Seen from this other side, the same ring now runs clockwise.

**Takeaway:** Opposite faces of a tiny box nearly cancel, and the three leftovers must add up to nothing. So how curving changes in one direction is tied to how it changes in the other two.

*What this leaves out:* Treats Earth as a still, round ball.

*Continues:* `ways_in/six-loops-around-a-box`<br>*Visuals:* [[cube-of-small-loops]]<br>*See:* `checks/leftover-of-the-third-pair`

### 3. True in every curved space · entry · contrast

*Could some curved space break the rule that the six changes of a tiny box add up to nothing?*

**Recap:** Around each face of a tiny box, walked counterclockwise seen from outside, a carried arrow comes back changed. Tiny changes add like steps, and every edge is walked once each way, so the six changes add up to nothing. The rule this gives about how curving changes is called the Bianchi identity.

The reason in "Six loops around a box" used only two facts. The first is that tiny changes add like steps, in any smoothly curved space. The second is that every edge of a closed box belongs to two faces, so it is walked once each way. Neither fact says what the space is made of, or what curves it. So the Bianchi identity holds in every smoothly curved space, even an invented one.

Compare it with the rule that a dropped stone falls toward Earth. Nothing about boxes or edges forces that rule, so only experiments can tell us whether it holds.

No experiment can find a tiny box whose six changes fail to add up to nothing. To find one, an experiment would have to break one of the two facts the reason uses. But tiny changes always add like steps in a smoothly curved space, and no closed box has an edge that belongs to only one face.

A rule that holds whatever the world is like is called an identity. An identity cannot tell us which curved space our world has. It tells us how the curving of any space must fit together.

**Takeaway:** The Bianchi identity holds in every smoothly curved space, because its reason uses only how tiny changes add and how a box's edges are shared. It is an identity, not a law of nature.

*What this leaves out:* "Smoothly curved" rules out sharp points, like the tip of a paper cone, where all the curving is squeezed into one spot.

*Continues:* `ways_in/six-loops-around-a-box`, `ways_in/leftovers-from-opposite-faces`<br>*See:* `checks/an-experiment-to-break-it`

### 4. Proof where the connection vanishes · working · calculation

*What does the identity say in components, and how is it proved?*

The three leftovers of "Leftovers from opposite faces" add to nothing. To write them in components, use the small-loop rule: walking $+a, +b, -a, -b$ changes a vector by $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$. Take coordinates with $\Gamma^\rho{}_{\mu\nu} = 0$ at the home corner, and a coordinate cube of side $\epsilon$ there. The two faces normal to $x^\lambda$, each walked counterclockwise seen from outside, have edges $\mu\nu$ with $(\lambda,\mu,\nu)$ a cyclic order of $(x,y,z)$, and they differ only by a displacement $\epsilon$ along $x^\lambda$. So to leading order their leftover is $-\epsilon^3\,\nabla_\lambda R^\rho{}_{\sigma\mu\nu}V^\sigma$. In a general chart each leftover gains terms $-\epsilon^3(\Gamma^\alpha{}_{\lambda\mu}R^\rho{}_{\sigma\alpha\nu} + \Gamma^\alpha{}_{\lambda\nu}R^\rho{}_{\sigma\mu\alpha})V^\sigma$, because the far face's edges are not parallel copies of the near face's. These extra terms cancel in the sum of the three pairs because $\Gamma$ is symmetric in its lower indices. Adding the three leftovers keeps the arrow slots $\rho\sigma$ fixed and cycles the derivative index together with the loop-edge pair:

$$\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0.$$

With $\lambda\mu\nu = zxy$ this is the leftover picture: $\nabla_z R^\rho{}_{\sigma xy}$ is how the entries for loops tilted like the top face change going up, and the other two terms are the forward and sideways pairs. Because $R^\rho{}_{\sigma\mu\nu} = -R^\rho{}_{\sigma\nu\mu}$, the three-term sum is three times the antisymmetrized derivative, so the identity also reads $\nabla_{[\lambda}R^\rho{}_{|\sigma|\mu\nu]} = 0$.

The derivation "The identity at a point where the connection vanishes" proves it. At any point $P$ choose coordinates with $\Gamma^\rho{}_{\mu\nu}(P) = 0$; they exist for a torsion-free connection, for example Riemann normal coordinates. There the Christoffel corrections inside $\nabla_\lambda$ vanish, and so does the derivative of each product of Christoffel symbols, since every term keeps one undifferentiated $\Gamma$. Six second derivatives of $\Gamma$ remain, and they cancel in pairs because partial derivatives commute. The cyclic sum is a tensor, so components that vanish at $P$ in one chart vanish in every chart, and $P$ was arbitrary.

Consequences:

- Only $\Gamma(P) = 0$ was used, so no metric is needed. The identity is linear and homogeneous in the Riemann tensor, so its overall sign convention does not matter, but which slots are cycled does.
- If two of $\lambda, \mu, \nu$ coincide, the sum vanishes by last-pair antisymmetry alone. So in two dimensions the identity says nothing, and in three, for the Levi-Civita connection, it gives 3 independent equations.
- Contracting $\rho$ with $\lambda$ gives $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$, and a second contraction with the metric gives $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$, as the derivation "Contracting the identity" shows: the Einstein tensor is divergence-free.
- It is not the cyclic identity $R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0$, which has no derivative and constrains the tensor at a single point. The two are often called the first and second Bianchi identities.

**Takeaway:** The covariant derivative of the Riemann tensor, cycled over the derivative index and the loop-edge pair, vanishes; it is proved where the connection vanishes and holds in every chart because it is a tensor equation.

*What this leaves out:* Torsion-free connections; the formal rung adds the torsion terms.

*Continues:* `ways_in/leftovers-from-opposite-faces`<br>*Builds on:* [[riemann-tensor-in-normal-coordinates]], [[symmetries-of-the-riemann-tensor]], [[covariant-derivative-of-a-tensor]]<br>*See:* `derivations/identity-where-connection-vanishes`, `derivations/contracting-the-identity`, `checks/why-special-coordinates-suffice`, `problems/empty-in-two-dimensions`

### 5. Tidal readings that must fit together · working · operational

*What does the identity require of tidal readings taken by a gradiometer at neighbouring places?*

The leftovers of "Leftovers from opposite faces" become measurable through tides. In a freely falling, non-rotating frame with orthonormal axes, hats dropped below, a gravity gradiometer reads the tidal matrix

$$E_{ij} \equiv c^2 R_{i0j0},$$

so that nearby free masses separate as $\ddot\xi^i = -E_{ij}\xi^j$. In a weak static field $E_{ij} = \partial_i\partial_j\Phi$.

Take the identity with the first pair $i0$ fixed and $\lambda\mu\nu = kj0$. To first order in the field, covariant derivatives become partial derivatives. In a static field the time-derivative term drops, and last-pair antisymmetry gives

$$\partial_k E_{ij} = \partial_j E_{ik},$$

as the derivation "Tides from the identity" shows. Since $E_{ij}$ is symmetric, $\partial_k E_{ij}$ is symmetric in all three indices. So readings at neighbouring places must fit together: how one entry changes along one axis fixes how others change along the rest. In Newtonian terms, third derivatives of $\Phi$ commute; conversely, a static tidal field that obeys this is locally the Hessian of a potential.

Above Earth's centre, take $z$ up and $x$ horizontal. On the vertical line $E_{xx} = GM/r^3$, which weakens upward at $\partial_z E_{xx} = -3GM/r^4$. The identity then predicts that the mixed entry $E_{xz}$, zero on that line, changes sideways at the same rate, $\partial_x E_{xz} = -3GM/r^4$. At Earth's surface this is $-7.26\times10^{-10}\ \mathrm{s^{-2}}$ per km, against $E_{xx} = 1.54\times10^{-6}\ \mathrm{s^{-2}}$: one part in 2,124 per km.

When the field changes with time the balance shifts: $\partial_k E_{ij} - \partial_j E_{ik} = -c\,\partial_t R_{i0kj}$, the gravitational counterpart of Faraday's law.

**Takeaway:** In a weak static field the identity makes the gradient of the tidal matrix symmetric in all three indices, so tidal readings at neighbouring places must fit together.

*What this leaves out:* First order in a weak field; the time-dependent term is suppressed by the square of source speeds over $c$.

*Continues:* `ways_in/leftovers-from-opposite-faces`, `ways_in/proof-where-the-connection-vanishes`<br>*Builds on:* [[tidal-force]], [[newtonian-tidal-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/tides-from-the-identity`, `observations/goce-gravity-gradients`, `checks/tidal-gradient-at-goce-height`

### 6. Any connection, any size of box · formal · structure

*What is the identity for a general connection, what exactly does it contain, and what is the finite-box statement?*

The proof in "Proof where the connection vanishes" used a torsion-free connection and special coordinates. Neither is essential. Let $M$ be a smooth manifold with a connection $\nabla$ on $TM$, curvature $\mathcal R(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$ and torsion $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$. Define $\nabla\mathcal R$ by the Leibniz rule, $(\nabla_X\mathcal R)(Y,Z) = [\nabla_X,\mathcal R(Y,Z)] - \mathcal R(\nabla_XY,Z) - \mathcal R(Y,\nabla_XZ)$, with components $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}$ for $X, Y, Z = \partial_\lambda, \partial_\mu, \partial_\nu$.

Theorem (second Bianchi identity). For all vector fields,

$$\mathfrak S_{X,Y,Z}\big[(\nabla_X\mathcal R)(Y,Z) + \mathcal R(T(X,Y),Z)\big] = 0,$$

where $\mathfrak S$ sums the three cyclic permutations. With zero torsion this is the component identity, for any metric or none.

Proof sketch. Commutators obey $\mathfrak S[\nabla_X,[\nabla_Y,\nabla_Z]] = 0$. Substitute $[\nabla_Y,\nabla_Z] = \mathcal R(Y,Z) + \nabla_{[Y,Z]}$, expand with the Leibniz rule, and use the Jacobi identity for vector fields; the remaining terms assemble into the torsion, as the derivation "The identity from the Jacobi identity" shows. For the Levi-Civita connection, lowering gives $\nabla_{[\lambda}R_{|\rho\sigma|\mu\nu]} = 0$, and pair exchange lets the cycle run over the first pair instead. In a local frame with connection one-forms $\omega$ and curvature two-forms $\Omega = d\omega + \omega\wedge\omega$, differentiation gives $d\Omega + \omega\wedge\Omega - \Omega\wedge\omega = 0$ for every connection on every vector bundle, although each $d\Omega^\rho{}_\sigma$ need not vanish. In a coordinate frame, with $\omega^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}dx^\mu$, the components of this equation are the cyclic sum of $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}$ plus terms in the antisymmetric part of $\Gamma$, which is the torsion.

Content. For a Levi-Civita connection in dimension $n$, $\nabla R$ at a point has $n\cdot n^2(n^2-1)/12$ components, and the identity imposes $n^2(n^2-1)(n-2)/24$ independent linear relations: 0, 3 and 20 for $n = 2, 3, 4$, leaving 2, 15 and 60. In four dimensions, 60 matches the third-order Taylor coefficients of the metric that no coordinate change removes, $200 - 140$. In three dimensions the identity is equivalent to $\nabla_\mu G^\mu{}_\nu = 0$; in four, that contraction carries only 4 of the 20 relations.

Finite boxes. Take the coordinate cube $[0,\epsilon]^3$ and lasso each face to one corner along edges, each face traversed with its outward orientation. Some ordering of the six lassos concatenates into a path that retraces itself, so the ordered product of the face holonomies is exactly the identity, for any connection and any $\epsilon$. In normal coordinates at the corner each face holonomy is $1 - \epsilon^2\mathcal R_{\text{face}} + O(\epsilon^3)$; opposite faces cancel at order $\epsilon^2$, cancellation at order $\epsilon^3$ is the identity, and the ordering matters only at order $\epsilon^4$.

Limits.

- With torsion the component identity gains $\mathfrak S\,\mathcal R(T(X,Y),Z)$, while $D\Omega = 0$ is unchanged.
- It needs a connection with two continuous derivatives, so that $\nabla\mathcal R$ exists.
- It is local: it says nothing about loops that cannot be shrunk to a point, whose holonomy it leaves free.
- It constrains how curvature varies; it neither implies nor requires a field equation.

**Takeaway:** For any connection the cyclic sum of the covariant derivative of curvature equals minus a torsion term; exactly, the lassoed holonomies of a closed cube multiply to the identity, and the third-order term of that statement is the identity.

*Picture:* A cube of face loops lassoed to one corner: face holonomies deviate from the identity at second order, opposite faces cancel at second order, and the third-order residues sum to zero.

*What this leaves out:* Connections on the tangent bundle, except where vector bundles are named.

*Continues:* `ways_in/proof-where-the-connection-vanishes`<br>*Builds on:* [[torsion-free-connection]], [[lie-bracket]], [[holonomy]]<br>*See:* `derivations/identity-from-jacobi`, `checks/does-it-need-a-metric`, `checks/count-the-relations`, `problems/curvature-constant-on-every-plane`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To move a carried arrow so that it points a different way, in any direction at all. | — |
| change | — | How far a carried arrow's tip has moved when the arrow gets back to where it started, including which way the tip moved. | [[holonomy]] |
| outline | — | The path along the outside of several joined faces or loops, leaving out the edges they share. The outline of five faces of a box is the rim of the missing sixth face. | — |
| tilt | — | The way a tiny loop is angled at a spot, set by the two directions its edges run along, like the bottom, front or left face of a box. | — |
| leftover | — | What remains after adding the changes from two opposite faces of a tiny box. It shows how the curving for loops of their tilt changes from one face to the other. | — |
| Bianchi identity | bee-AHN-kee | The rule that the three leftovers of any tiny box add up to nothing, so that how curving changes in one direction is tied to how it changes in the other two. | [[bianchi-identity]] |
| identity | — | A rule that holds whatever the world is like, because of how the things it talks about are built. | [[identity-versus-equation]] |

## Key equations

### Bianchi identity · working

$$
\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0
$$

Cycling the derivative index with the loop-edge pair of the Riemann tensor, the covariant derivatives add to zero: the three leftovers of a tiny box balance.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\lambda$ | covariant derivative along $x^\lambda$ | nabla lambda |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course convention; $\rho\sigma$ are the arrow slots, $\mu\nu$ the loop edges | R rho sigma mu nu |

**Holds when:** Torsion-free connection, with or without a metric; every point and every chart.  
**Say it:** “Nabla lambda of R rho sigma mu nu, plus nabla mu of R rho sigma nu lambda, plus nabla nu of R rho sigma lambda mu, equals zero.”  
**Justified by:** `derivations/identity-where-connection-vanishes`

### Once- and twice-contracted identity · working

$$
\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu},\qquad \nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R
$$

The divergence of the Riemann tensor is an antisymmetrized derivative of the Ricci tensor, and the divergence of the Ricci tensor is half the gradient of the Ricci scalar.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\sigma\nu}$ | Ricci tensor, $R^\rho{}_{\sigma\rho\nu}$ | the Ricci tensor |
| $R$ | Ricci scalar, $g^{\mu\nu}R_{\mu\nu}$ | the Ricci scalar |

**Holds when:** Torsion-free connection for the first; the second also needs $\nabla g = 0$, the Levi-Civita connection.  
**Say it:** “The divergence of Riemann equals nabla mu of Ricci sigma nu minus nabla nu of Ricci sigma mu; and the divergence of Ricci is half the gradient of the Ricci scalar.”  
**Justified by:** `derivations/contracting-the-identity`

### Tidal gradients in a weak static field · working

$$
\partial_k E_{ij} = \partial_j E_{ik},\qquad E_{ij} \equiv c^2 R_{\hat i\hat 0\hat j\hat 0}
$$

The gradient of the tidal matrix is symmetric in all three indices, so tidal readings at neighbouring places fit together.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E_{ij}$ | tidal matrix read by a freely falling, non-rotating gradiometer | the tidal matrix |
| $\partial_k$ | rate of change along the spatial axis $k$ | d by d x k |

**Holds when:** First order in a weak field; static field. Otherwise $\partial_kE_{ij} - \partial_jE_{ik} = -c\,\partial_tR_{\hat i\hat 0\hat k\hat j}$.  
**Say it:** “d by d x k of E i j equals d by d x j of E i k.”  
**Justified by:** `derivations/tides-from-the-identity`

### Second Bianchi identity for any connection · formal

$$
\mathfrak S_{X,Y,Z}\big[(\nabla_X\mathcal R)(Y,Z) + \mathcal R(T(X,Y),Z)\big] = 0
$$

For any connection on the tangent bundle, the cyclic sum of the covariant derivative of curvature is balanced by curvature acting on torsion.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathfrak S_{X,Y,Z}$ | sum over the three cyclic permutations of $X, Y, Z$ | the cyclic sum |
| $\mathcal R(X,Y)$ | curvature operator $[\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$ | the curvature of X and Y |
| $T(X,Y)$ | torsion $\nabla_XY - \nabla_YX - [X,Y]$ | the torsion of X and Y |

**Holds when:** Any connection on $TM$ with two continuous derivatives; reduces to the component identity when $T = 0$.  
**Say it:** “The cyclic sum of nabla X of the curvature on Y and Z, plus the curvature of the torsion of X and Y with Z, is zero.”  
**Justified by:** `derivations/identity-from-jacobi`

## Derivations

### The identity at a point where the connection vanishes · working

**Goal:** Prove $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0$ for a torsion-free connection.

1. At a point $P$ choose coordinates with $\Gamma^\rho{}_{\mu\nu}(P) = 0$; they exist because $\Gamma$ is symmetric in its lower indices.
2. Every Christoffel correction in $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}$ contains one $\Gamma$, so at $P$ it equals $\partial_\lambda R^\rho{}_{\sigma\mu\nu}$.
3. In $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\kappa}\Gamma^\kappa{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\kappa}\Gamma^\kappa{}_{\mu\sigma}$, each term of $\partial_\lambda(\Gamma\Gamma)$ keeps one undifferentiated $\Gamma$, so it vanishes at $P$.
4. So at $P$, $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} = \partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma}$.
5. Cycle $(\lambda,\mu,\nu)$ and add: $\partial_\lambda\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\lambda\partial_\nu\Gamma^\rho{}_{\mu\sigma} + \partial_\mu\partial_\nu\Gamma^\rho{}_{\lambda\sigma} - \partial_\mu\partial_\lambda\Gamma^\rho{}_{\nu\sigma} + \partial_\nu\partial_\lambda\Gamma^\rho{}_{\mu\sigma} - \partial_\nu\partial_\mu\Gamma^\rho{}_{\lambda\sigma}$.
6. Partial derivatives commute, so the first and fourth terms cancel, the second and fifth, and the third and sixth.
7. The cyclic sum is a tensor whose components all vanish at $P$ in one chart, so it vanishes at $P$ in every chart; $P$ was arbitrary.

**Result:** $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0$ everywhere, in every chart, with no metric used.

### Contracting the identity · working

**Goal:** Derive $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$ and $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$.

1. Set $\lambda = \rho$ and sum; contraction commutes with $\nabla$: $\nabla_\rho R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\rho} + \nabla_\nu R^\rho{}_{\sigma\rho\mu} = 0$.
2. With $R_{\sigma\nu} = R^\rho{}_{\sigma\rho\nu}$ and last-pair antisymmetry, $R^\rho{}_{\sigma\nu\rho} = -R_{\sigma\nu}$ and $R^\rho{}_{\sigma\rho\mu} = R_{\sigma\mu}$.
3. So $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$.
4. Contract with $g^{\sigma\mu}$, which passes through $\nabla$ because $\nabla g = 0$. First-pair antisymmetry gives $g^{\sigma\mu}R^\rho{}_{\sigma\mu\nu} = -R^\rho{}_\nu$.
5. The result is $-\nabla_\rho R^\rho{}_\nu = \nabla_\mu R^\mu{}_\nu - \nabla_\nu R$, so $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$.

**Result:** $\nabla_\rho R^\rho{}_{\sigma\mu\nu} = \nabla_\mu R_{\sigma\nu} - \nabla_\nu R_{\sigma\mu}$ and $\nabla_\mu\big(R^\mu{}_\nu - \tfrac12\delta^\mu{}_\nu R\big) = 0$.

### Tides from the identity · working

**Goal:** Show $\partial_k E_{ij} = \partial_j E_{ik}$ in a weak static field, with $E_{ij} = c^2R_{\hat i\hat 0\hat j\hat 0}$.

1. Write the identity with $\rho\sigma = \hat i\hat 0$ and $\lambda\mu\nu = \hat k\hat j\hat 0$: $\nabla_k R_{i0j0} + \nabla_j R_{i00k} + \nabla_0 R_{i0kj} = 0$.
2. In a weak field $\Gamma$ and $R$ are both first order, so to first order each $\nabla$ becomes $\partial$.
3. Last-pair antisymmetry gives $R_{i00k} = -R_{i0k0}$, so $\partial_k R_{i0j0} - \partial_j R_{i0k0} = -\partial_0 R_{i0kj}$.
4. Multiply by $c^2$ and use $\partial_0 = c^{-1}\partial_t$: $\partial_k E_{ij} - \partial_j E_{ik} = -c\,\partial_t R_{i0kj}$, which vanishes in a static field.

**Result:** $\partial_k E_{ij} = \partial_j E_{ik}$ for a weak static field; with $E_{ij} = E_{ji}$, $\partial_kE_{ij}$ is symmetric in all three indices.

### The identity from the Jacobi identity · formal

**Goal:** Prove $\mathfrak S[(\nabla_X\mathcal R)(Y,Z) + \mathcal R(T(X,Y),Z)] = 0$ for any connection on $TM$.

1. Commutators of operators on vector fields obey $\mathfrak S\,[\nabla_X,[\nabla_Y,\nabla_Z]] = 0$.
2. Substitute $[\nabla_Y,\nabla_Z] = \mathcal R(Y,Z) + \nabla_{[Y,Z]}$.
3. By the definition of $\nabla\mathcal R$, $[\nabla_X,\mathcal R(Y,Z)] = (\nabla_X\mathcal R)(Y,Z) + \mathcal R(\nabla_XY,Z) + \mathcal R(Y,\nabla_XZ)$.
4. Also $[\nabla_X,\nabla_{[Y,Z]}] = \mathcal R(X,[Y,Z]) + \nabla_{[X,[Y,Z]]}$, and $\mathfrak S\,\nabla_{[X,[Y,Z]]} = 0$ by the Jacobi identity for vector fields.
5. Inside $\mathfrak S$, relabel each remaining curvature term to put $X$ first: $\mathcal R(\nabla_XY,Z) \to -\mathcal R(X,\nabla_YZ)$ and $\mathcal R(Y,\nabla_XZ) \to \mathcal R(X,\nabla_ZY)$.
6. With $\mathcal R(X,[Y,Z])$ they give $\mathcal R(X,\nabla_ZY - \nabla_YZ + [Y,Z]) = -\mathcal R(X,T(Y,Z)) = \mathcal R(T(Y,Z),X)$.
7. So $\mathfrak S[(\nabla_X\mathcal R)(Y,Z) + \mathcal R(T(Y,Z),X)] = 0$, and relabelling the cycle turns the last term into $\mathcal R(T(X,Y),Z)$.

**Result:** $\mathfrak S_{X,Y,Z}[(\nabla_X\mathcal R)(Y,Z) + \mathcal R(T(X,Y),Z)] = 0$; with $T = 0$ this is the component identity, and no metric was used.

## Worked examples

### How curving may change in a round space · working

**Problem:** A spherically symmetric space has $ds^2 = ds_r^2 + f(s_r)^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, with $s_r$ the radial distance. Planes containing the radial direction have sectional curvature $K_r = -f''/f$, and tangential planes $K_t = (1 - f'^2)/f^2$, primes meaning $d/ds_r$. Use the contracted identity to find how $K_t$ must change outward, and test the result on the space around a star at one moment.

1. The orthonormal Ricci components are $R^{s}{}_{s} = 2K_r \equiv A$ and $R^\theta{}_\theta = R^\phi{}_\phi = K_r + K_t \equiv B$, so $R = A + 2B = 4K_r + 2K_t$.
2. The nonzero Christoffel symbols with a radial lower index include $\Gamma^\theta{}_{\theta s} = \Gamma^\phi{}_{\phi s} = f'/f$, so $\nabla_\mu R^\mu{}_s = A' + 2(f'/f)(A - B)$.
3. The contracted identity $2\nabla_\mu R^\mu{}_s = R'$ gives $2A' + 4(f'/f)(A - B) = A' + 2B'$.
4. Substituting $A$ and $B$: $-2K_t' + 4(f'/f)(K_r - K_t) = 0$, so $K_t' = 2(f'/f)(K_r - K_t)$.
5. Direct check: differentiating $K_t = (1 - f'^2)/f^2$ gives $-2f'f''/f^2 - 2f'(1 - f'^2)/f^3$, which is the same.
6. Around a star of mass $M$, at one moment, $f = r$ with $f' = \sqrt{1 - 2GM/rc^2}$, $K_t = 2GM/c^2r^3$ and $K_r = -GM/c^2r^3$. Left side: $f'(-6GM/c^2r^4)$. Right side: $2(f'/r)(-3GM/c^2r^3)$, equal.

**Answer:** $K_t' = 2(f'/f)(K_r - K_t)$. At Earth's surface $K_t = 3.43\times10^{-23}\ \mathrm{m^{-2}}$, falling outward by about $3/r$, one part in 2,124 per km.

**Takeaway:** In a round space the outward change of tangential curvature is fixed by how radial and tangential curvature differ; where they are equal, the tangential curvature cannot change outward.

## Problems

### `tent-and-open-box` · entry · difficulty 1 · conceptual

A tiny closed tent-shaped box has two triangle faces and three rectangle faces. (a) How many edges does it have? Going once around every face, how many edge walks is that in all? (b) Carry a fresh arrow around every face, each counterclockwise seen from outside. Do the five changes add up to nothing? (c) Now take the lid off an ordinary tiny box. What do the changes of the five remaining faces add up to?

**Hints**

1. Count the edges of each face, then count the edges of the whole tent.
2. Does every edge of the tent still belong to exactly two faces?
3. What is the outline of an open box?

**Answer:** (a) 9 edges and 18 edge walks. (b) Yes. (c) The opposite of the change the lid would give.

**Must contain:** Each of the 9 edges is walked twice, once each way; The rule needs only a closed box, not a cube; An open box leaves the rim, which is the lid's loop walked the other way

**Numeric:** edges of the tent = 9 1 (magnitude, ±0.1); edge walks = 18 1 (magnitude, ±0.1)

**Solution**

1. The faces have 3, 3, 4, 4 and 4 edges, which makes 18 edge walks.
2. The tent has 3 edges on each triangle end and 3 long edges joining them, so 9 edges. So 18 walks means each edge is walked twice.
3. Every edge belongs to two faces, and going counterclockwise around both, seen from outside, walks it once each way. So joining all five faces leaves no outline, and the five changes add up to nothing.
4. Without the lid, the rim's edges each belong to only one face. Joining the five faces leaves the rim as the outline.
5. Seen from outside, the rim goes around the missing lid the opposite way, so the five changes add up to the opposite of the lid's change.

### `empty-in-two-dimensions` · working · difficulty 2 · derivation

Show that $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu}$ vanishes by antisymmetry alone whenever two of $\lambda, \mu, \nu$ are equal. Conclude that the identity is empty in two dimensions, and count its independent equations in three dimensions for the Levi-Civita connection.

**Hints**

1. Try $\mu = \nu$ first, using $R^\rho{}_{\sigma\mu\nu} = -R^\rho{}_{\sigma\nu\mu}$.
2. In three dimensions, how many different unordered triples $\lambda\mu\nu$ with no repeats are there?
3. Lower $\rho$ and use first-pair antisymmetry to count the pairs $\rho\sigma$.

**Answer:** Repeated cycled indices give $0$ identically, so two dimensions give no equations; three dimensions give 3 independent equations.

**Must contain:** A repeated index makes the three terms cancel by last-pair antisymmetry; Two dimensions always force a repeat; In three dimensions only the triple 1 2 3 remains, with 3 independent pairs rho sigma

**Numeric:** independent equations in three dimensions = 3 1 (magnitude, ±0.1)

**Solution**

1. If $\mu = \nu$, the first term contains $R^\rho{}_{\sigma\mu\mu} = 0$, and the other two are $\nabla_\mu R^\rho{}_{\sigma\mu\lambda} + \nabla_\mu R^\rho{}_{\sigma\lambda\mu} = 0$.
2. The cases $\lambda = \mu$ and $\lambda = \nu$ are the same after a cyclic relabelling.
3. In two dimensions three indices take only two values, so a repeat is unavoidable and the identity holds trivially.
4. In three dimensions the only non-repeating triple is a permutation of $123$; cyclic permutations give the same equation and odd ones its negative.
5. Lowering $\rho$, $\nabla_{[1}R_{|\rho\sigma|23]} = 0$ is antisymmetric in $\rho\sigma$, leaving the pairs $12, 13, 23$: 3 equations, all independent.

### `curvature-constant-on-every-plane` · formal · difficulty 2 · proof

On a connected Riemannian manifold of dimension $n \geq 3$, suppose $R_{\rho\sigma\mu\nu} = k\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ at every point, for some smooth function $k$. Prove that $k$ is constant. Why does the argument fail for $n = 2$?

**Hints**

1. Compute the Ricci tensor and Ricci scalar from the assumed form.
2. Insert them into $\nabla_\mu R^\mu{}_\nu = \tfrac12\nabla_\nu R$.

**Answer:** $(n-1)(n-2)\,\partial_\nu k = 0$, so $k$ is locally constant, hence constant on a connected manifold, when $n \geq 3$. For $n = 2$ the factor vanishes and the identity gives nothing; an ellipsoid has varying $K$.

**Must contain:** Ricci equals n minus one times k times the metric; The Ricci scalar is n times n minus one times k; The contracted identity gives n minus one times n minus two times the gradient of k equals zero; In two dimensions the factor is zero

**Solution**

1. $R_{\sigma\nu} = g^{\rho\mu}R_{\rho\sigma\mu\nu} = k(n\,g_{\sigma\nu} - g_{\sigma\nu}) = (n-1)k\,g_{\sigma\nu}$, and $R = n(n-1)k$.
2. Since $\nabla g = 0$, $\nabla_\mu R^\mu{}_\nu = (n-1)\partial_\nu k$ and $\tfrac12\nabla_\nu R = \tfrac12 n(n-1)\partial_\nu k$.
3. The contracted identity equates them: $(n-1)(1 - n/2)\,\partial_\nu k = 0$, that is $(n-1)(n-2)\,\partial_\nu k = 0$.
4. For $n \geq 3$ the factor is nonzero, so $dk = 0$, and a connected manifold makes $k$ constant.
5. For $n = 2$ every metric has this form with $k = K$, the identity is empty, and $K$ may vary, as on an ellipsoid.

## Observations

- **Gravity gradients mapped by the gradiometer of ESA's GOCE satellite** (measured, working). From 2009 to 2013 GOCE measured the tidal matrix $E_{ij}$ along its orbit, which ran about 255 km above Earth and lower in its final year. Its gradiometer senses $E_{ij}$ together with the centrifugal and angular-acceleration terms of the satellite's own turn, which is one turn per orbit and keeps the satellite facing Earth. Those extra terms are reconstructed from the star trackers and from the antisymmetric part of the readings, then removed. Earth's field is weak and its sources move slowly, so the time term of the identity is negligible and $\partial_kE_{ij}$ must be symmetric in all three indices. Readings along and across the track must therefore fit together as second derivatives of one potential, which is how gravity-field models are built from them. *Numbers:* At $r = 6626$ km for a spherical Earth: $E_{xx} = GM/r^3 = 1.37\times10^{-6}\ \mathrm{s^{-2}}$ across the radius, $E_{zz} = -2.74\times10^{-6}\ \mathrm{s^{-2}}$ along it, and $\partial_zE_{xx} = \partial_xE_{xz} = -6.20\times10^{-10}\ \mathrm{s^{-2}}$ per km. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0

## Teaching arc

1. **Predict the box total** (entry). Pose the six face trips, ask for a prediction, then count edge walks on a real box. *Why:* Learners reach the rule by counting edges. *Predict:* If you know the changes from five faces of a tiny box, can you tell what the sixth face does? *Visual:* [[cube-of-small-loops]] *Uses:* `ways_in/six-loops-around-a-box`, `checks/the-sixth-trip`
2. **Turn the zero into leftovers** (entry). Pair opposite faces so the zero total becomes three balancing leftovers. *Why:* The rule is about how curving changes. *Visual:* [[cube-of-small-loops]] *Uses:* `ways_in/leftovers-from-opposite-faces`, `checks/leftover-of-the-third-pair`
3. **Separate identity from law** (entry). Contrast the box rule with a law that experiments test. *Why:* It blocks reading the identity as testable physics. *Predict:* Could a precise enough experiment find a tiny box that breaks the rule? *Uses:* `ways_in/true-in-every-curved-world`, `checks/an-experiment-to-break-it`
4. **Prove it at a point** (working). Set the connection to zero at a point, pair the six terms, and promote by tensoriality. *Why:* Shortest rigorous route; no metric needed. *Uses:* `ways_in/proof-where-the-connection-vanishes`, `derivations/identity-where-connection-vanishes`, `checks/why-special-coordinates-suffice`
5. **Read it in tides** (working). Show that tidal gradients above Earth fit together, then work the round space. *Why:* It ties the identity to real measurements. *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tidal-readings-that-must-fit`, `observations/goce-gravity-gradients`, `worked_examples/curving-of-a-round-space`
6. **Mark hypotheses and content** (formal). Add torsion, count relations, and apply the contraction to constant curvature. *Why:* Graduate readers need what it assumes and forces. *Uses:* `ways_in/any-connection-any-size`, `checks/does-it-need-a-metric`, `problems/curvature-constant-on-every-plane`

## Analogies

### Faraday's law and the absence of magnetic charge · working

A charged particle's quantum phase around a small loop is set by the flux of $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ through it. Around a closed box every edge is walked once each way, giving $\partial_\lambda F_{\mu\nu} + \partial_\mu F_{\nu\lambda} + \partial_\nu F_{\lambda\mu} = 0$: with three space indices, $\nabla\cdot\mathbf B = 0$; with one time index, Faraday's law.

| In the analogy | Stands for |
| --- | --- |
| the potential $A_\mu$ | the connection $\Gamma^\rho{}_{\mu\sigma}$ |
| the field strength $F_{\mu\nu}$ | the Riemann tensor $R^\rho{}_{\sigma\mu\nu}$ |
| $\partial_\lambda$ | $\nabla_\lambda$ |

*Limits:* Phases commute, so the electromagnetic rule is an exact sum for any box and needs no covariant derivative; arrow changes are matrices. Where magnetic charge sat, $F$ would have no potential and the rule would fail; curvature always comes from a connection.

## Misconceptions

### “The Bianchi identity is a law of nature, so a precise enough experiment might catch it failing.” · entry · `identity-is-a-law-of-nature`

- **Why it is tempting:** It sits beside Einstein's equation, and its electromagnetic twin is listed among Maxwell's laws.
- **What is true:** Its reason uses only how tiny arrow changes add and the fact that each edge of a closed box is walked once each way, and both hold in any smoothly curved space.
- **Exposed by:** `checks/an-experiment-to-break-it`

### “If the six changes of a box always add up to nothing, the curving must be the same all through the box.” · entry · `zero-total-means-uniform-curving`

- **Why it is tempting:** Opposite faces cancel exactly when the curving is the same at both.
- **What is true:** Each pair may leave a leftover; the zero total only requires the three leftovers to balance.
- **Exposed by:** `checks/leftover-of-the-third-pair`

### “The proof uses coordinates where the connection vanishes, so the identity holds only in those coordinates.” · working · `only-in-special-coordinates`

- **Why it is tempting:** Setting the Christoffel symbols to zero is valid only in special coordinates and only at one point.
- **What is true:** The cyclic sum is a tensor, so if its components vanish at a point in one chart, they vanish there in every chart.
- **Exposed by:** `checks/why-special-coordinates-suffice`

### “The Bianchi identity and the cyclic identity are the same statement.” · working · `same-as-cyclic-identity`

- **Why it is tempting:** Both are three-term cyclic sums and are called the first and second Bianchi identities.
- **What is true:** The cyclic identity is algebraic and constrains the tensor at one point; the Bianchi identity involves derivatives and constrains how the tensor varies.
- **Exposed by:** `checks/which-identity-at-one-point`

### “The Bianchi identity is a property of the Levi-Civita connection and fails for other connections.” · formal · `needs-the-metric`

- **Why it is tempting:** It is usually met right after the metric symmetries of the Riemann tensor.
- **What is true:** It holds for every torsion-free connection, with or without a metric. Torsion adds a definite curvature-torsion term.
- **Exposed by:** `checks/does-it-need-a-metric`

## Checks

1. **Entry · predict** `checks/the-sixth-trip`. A tiny box floats in a curved space. From one corner, you carry a fresh arrow around each face, counterclockwise seen from outside the box. For the three faces that do not touch that corner, you walk out along an edge first and come back along it. Every arrow starts pointing the same way. Five trips move the arrow's tip toward the top of the box by 20, 11 and 9, and toward the bottom by 19 and 12. These are millionths of a millimetre. How does the sixth trip move the tip?
   - **Hints:** What do all six changes add up to?
   - **Answer:** Toward the bottom by 9 millionths of a millimetre. Every edge of the box is walked once each way, so the six changes add up to nothing. The five trips give 20, 11 and 9, which is 40, toward the top, and 19 and 12, which is 31, toward the bottom. That leaves 9 toward the top. So the sixth trip must move the tip 9 toward the bottom.
   - **Must contain:** The six changes add up to nothing; The five trips leave 9 toward the top; The sixth trip moves the tip 9 toward the bottom
   - **Numeric:** sixth trip's tip movement toward the top = -9e-06 mm (signed, ±1e-07)
   - **Visual:** [[cube-of-small-loops]]
2. **Entry · numeric** `checks/leftover-of-the-third-pair`. For a tiny box, the top and bottom trips together move the arrow's tip 7 millionths of a millimetre toward the front of the box. The front and back trips together move it 2 millionths of a millimetre toward the back. Every trip starts at the same corner with a fresh arrow pointing the same way. (a) What do the left and right trips do together? (b) Is the curving the same all through the box?
   - **Hints:** What do the three leftovers add up to? / What would every leftover be if the curving were the same at opposite faces?
   - **Answer:** (a) They move the tip 5 millionths of a millimetre toward the back. The three leftovers are the six changes grouped in pairs. The six changes add up to nothing, so the three leftovers add up to nothing too. The first two leftovers give 7 toward the front and 2 toward the back, which is 5 toward the front. So the third must be 5 toward the back. (b) No. If the curving were the same all through the box, the changes of opposite faces would cancel, and every leftover would be nothing. The top and bottom leftover is 7, not nothing.
   - **Must contain:** The three leftovers add up to nothing; The left and right leftover is 5 toward the back; Leftovers that are not nothing mean the curving changes
   - **Numeric:** left and right leftover toward the front = -5e-06 mm (signed, ±1e-07)
   - **Targets:** `zero-total-means-uniform-curving`
   - **Visual:** [[cube-of-small-loops]]
3. **Entry · evaluate-claim** `checks/an-experiment-to-break-it`. A friend says: one day, a very precise experiment near a heavy star may find a tiny box whose six changes do not add up to nothing. That would prove the Bianchi identity wrong. Is your friend right?
   - **Hints:** What did the reason for the rule use about the space?
   - **Answer:** No. The six changes add up to nothing because every edge of a closed box belongs to two faces. Going around both faces counterclockwise, seen from outside, walks that edge once each way. Tiny changes add like steps, so those two walks cancel. This reason says nothing about stars, gravity or matter, so it holds in every smoothly curved space. To break the rule, an experiment would have to show that one of the two facts this reason uses is false. But neither fact can fail: tiny changes always add like steps in a smoothly curved space, and no closed box has an edge that belongs to only one face.
   - **Must contain:** The friend is wrong; The reason uses only how tiny changes add and that each edge is walked once each way; A rule that holds in every smoothly curved space is an identity, not a law that experiments test
   - **Targets:** `identity-is-a-law-of-nature`
4. **Working · explain** `checks/why-special-coordinates-suffice`. The proof sets the Christoffel symbols to zero at a point, which is possible only in special coordinates. Why does the identity then hold in polar coordinates too, and why would the same step fail for the statement that the Christoffel symbols vanish at that point?
   - **Hints:** How do the components of a tensor change between charts?
   - **Answer:** The cyclic sum $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \text{cyclic}$ is a tensor. Its components in any chart are linear combinations of its components in another, so if all vanish at $P$ in one chart they vanish at $P$ in every chart, and $P$ was arbitrary. The Christoffel symbols are not a tensor: under a change of coordinates they gain a term with second derivatives of the coordinate change, so zero in one chart can be nonzero in another, as polar coordinates on a flat plane show with $\Gamma^r{}_{\phi\phi} = -r$.
   - **Must contain:** The cyclic sum is a tensor; Tensor components vanishing in one chart vanish in all charts at that point; Christoffel symbols transform inhomogeneously, so their vanishing does not carry over
   - **Targets:** `only-in-special-coordinates`
5. **Working · choice** `checks/which-identity-at-one-point`. You are given every component of the Riemann tensor at a single point, and nothing else. Which can you check: (a) the cyclic identity, (b) the Bianchi identity, (c) both, (d) neither?
   - **Hints:** Which of the two contains a derivative?
   - **Answer:** (a). The cyclic identity $R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0$ is a linear relation among components at one point. The Bianchi identity involves $\nabla_\lambda R^\rho{}_{\sigma\mu\nu}$, which needs the tensor at neighbouring points and the connection, so it cannot be tested from one point's values. They are different statements: one about the table at a point, the other about how it varies.
   - **Must contain:** Only the cyclic identity; The cyclic identity is algebraic at one point; The Bianchi identity needs derivatives of the tensor
   - **Targets:** `same-as-cyclic-identity`
6. **Working · numeric** `checks/tidal-gradient-at-goce-height`. Treat Earth as a sphere with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$. At $r = 6626$ km on a vertical line through its centre, with $z$ up and $x$ horizontal, a gradiometer reads $E_{xx} = GM/r^3$. Using the static limit of the identity, not the potential, predict $E_{xz}$ at 1 km horizontally from that line, and the horizontal relative acceleration of the upper of two free masses 1 m apart vertically there.
   - **Hints:** Differentiate $GM/r^3$ with respect to $r$ along the vertical line. / $E_{xz} = 0$ on the line itself.
   - **Answer:** $\partial_xE_{xz} = \partial_zE_{xx} = -3GM/r^4 = -6.20\times10^{-13}\ \mathrm{s^{-2}\,m^{-1}}$, so $E_{xz} = -6.20\times10^{-10}\ \mathrm{s^{-2}}$ at $x = 1$ km. Then $\ddot\xi^x = -E_{xz}\xi^z = +6.20\times10^{-10}\ \mathrm{m\,s^{-2}}$: the upper mass drifts away from the vertical line, because the horizontal pull toward the line is weaker higher up.
   - **Must contain:** d E x z by d x equals d E x x by d z; Both equal minus three G M over r to the fourth; The upper mass drifts away from the line at 6.2 times ten to the minus ten metres per second squared
   - **Numeric:** horizontal relative acceleration, positive away from the vertical line = 6.2e-10 m/s^2 (signed, ±2%)
   - **Visual:** [[falling-ring-of-crumbs]]
7. **Formal · explain** `checks/does-it-need-a-metric`. (a) Does the second Bianchi identity hold for a torsion-free connection that preserves no metric? (b) For a metric connection with torsion, what happens to the component identity, and to the frame identity that the exterior covariant derivative of the curvature two-form vanishes? (c) Which steps toward the divergence-free Einstein tensor need the metric?
   - **Hints:** Where in the Jacobi proof does torsion appear?
   - **Answer:** (a) Yes. The Jacobi-identity proof and the proof at a point with $\Gamma(P) = 0$ use only the connection. (b) The component cyclic sum becomes $\mathfrak S(\nabla_X\mathcal R)(Y,Z) = -\mathfrak S\,\mathcal R(T(X,Y),Z)$, generally nonzero, while $D\Omega = d\Omega + \omega\wedge\Omega - \Omega\wedge\omega = 0$ still holds, since it uses no torsion-free assumption. (c) The first contraction needs no metric. The second needs a metric to contract $\sigma$ with $\mu$, and $\nabla g = 0$ both for first-pair antisymmetry and for passing $g^{\sigma\mu}$ through $\nabla$.
   - **Must contain:** Holds for every torsion-free connection; Torsion adds minus the cyclic sum of curvature acting on torsion; D Omega equals zero holds for every connection; The second contraction needs a metric connection
   - **Targets:** `needs-the-metric`
8. **Formal · numeric** `checks/count-the-relations`. At a point of a four-dimensional pseudo-Riemannian manifold, how many independent linear relations does the Bianchi identity impose on the covariant derivative of the Riemann tensor, and how many of them does the twice-contracted identity carry?
   - **Hints:** Count the components of an object antisymmetric in one pair and in one triple. / Which part of the identity is implied by the cyclic identity?
   - **Answer:** 20 relations, of which the contraction carries 4. The identity $\nabla_{[\lambda}R_{|\rho\sigma|\mu\nu]} = 0$ is antisymmetric in $\rho\sigma$ (6 pairs) and in $\lambda\mu\nu$ (4 triples), so it has 24 components. Antisymmetrizing it over $\rho\sigma\lambda\mu$ gives the derivative of $R_{[\rho\sigma\mu]\nu} = 0$, which already vanishes by the cyclic identity: 4 automatic relations, leaving 20. So the 80 components of $\nabla R$ reduce to 60. The twice-contracted identity has one free index, hence 4 components.
   - **Must contain:** 24 components, antisymmetric in rho sigma and in lambda mu nu; 4 are automatic because of the cyclic identity; 20 relations leave 60 of 80 components; The contraction carries only 4
   - **Numeric:** independent relations = 20 1 (magnitude, ±0.1); relations in the twice-contracted identity = 4 1 (magnitude, ±0.1)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which indices the identity cycles | $\nabla_\lambda R^\rho{}_{\sigma\mu\nu} + \nabla_\mu R^\rho{}_{\sigma\nu\lambda} + \nabla_\nu R^\rho{}_{\sigma\lambda\mu} = 0$: the first pair stays fixed, and the derivative index cycles with the last pair. | Some texts put the derivative after a semicolon, as in $R_{\rho\sigma\mu\nu;\lambda} + R_{\rho\sigma\nu\lambda;\mu} + R_{\rho\sigma\lambda\mu;\nu} = 0$, or antisymmetrize, $R^\rho{}_{\sigma[\mu\nu;\lambda]} = 0$; both agree with the course form. For the Levi-Civita connection, pair exchange allows cycling over the first pair instead. Cycling three slots of the tensor with no derivative gives the different cyclic identity. |
| What the name refers to | "Bianchi identity" means this differential identity; the algebraic one is the "cyclic identity"; "contracted Bianchi identity" means the Ricci or Einstein form. | Some texts call the cyclic identity the first Bianchi identity and this one the second; others call the twice-contracted form the Bianchi identities, or mark identities with $\equiv$. |

## Visuals

- ★ [[cube-of-small-loops]] (flagship): Flagship: six face trips around a tiny box, their leftovers, and a total that stays at zero. *Sketch:* A small cube floats in a chosen curved three-dimensional space: a round three-sphere, the space around a star at one moment, or a smooth bump. The learner picks a home corner and an arrow, then plays the six trips, each face counterclockwise seen from outside, with edge detours to the far faces. Each face's change appears as a tip-shift arrow at home; opposite pairs combine into three leftovers, and a total readout stays at zero. A size slider shows face changes shrinking like the area, leftovers like the volume, and the total faster still. On the three-sphere every leftover is zero. Removing one face leaves a total equal to minus that face's change.
- [[falling-ring-of-crumbs]] (supporting): Tidal readings at neighbouring places that must fit together. *Sketch:* Adds a gradiometer mode above a round planet: the tidal matrix read on a small grid of points, with readouts of how $E_{xx}$ changes going up and how $E_{xz}$ changes going sideways. For a still planet the two always agree.

## Tutor moves

**Open with**

- Picture a tiny cardboard box floating in curved space. You carry an arrow around each of its six faces, going counterclockwise as seen from outside the box, and add up how the arrow comes back changed. Could the total be anything, or must it be something special? *(prediction)*
- Some rules could have been different, like how fast a dropped stone falls. Others could not, like the rule that every edge of a closed box touches two faces. Which kind could a rule about curving be? *(reflection)*

**If the learner is stuck**

- *The learner does not see why every edge is walked once each way.* → Have the learner draw counterclockwise rings on a real box, face by face as seen from outside, then inspect one edge. *Uses:* `ways_in/six-loops-around-a-box`
- *The learner loses track of the six second-derivative terms.* → Expand the three cyclic terms into six and pair each with its swapped-derivative partner. *Uses:* `derivations/identity-where-connection-vanishes`
- *The learner cycles the arrow slots or all four indices.* → Return to the box: the derivative direction and a face's two edges rotate; the arrow slots stay put. *Uses:* `notation_traps/which-slots-are-cycled`, `checks/which-identity-at-one-point`

**Common questions**

- *If the rule holds everywhere anyway, why does it matter for gravity?* (entry) Einstein's equation is the law of gravity in general relativity. One side describes the curving of space and time, and the other side describes the matter and energy there. A form of the Bianchi identity always holds for the curving side. So the equation can hold only if the matter side obeys a matching rule. The rule says that, for someone falling freely at any place, energy and momentum there cannot appear or vanish without flowing in or out. That matching rule is how Einstein's equation fits with the conservation of energy. Even so, over large regions, matter can gain or lose energy by trading it with gravity. *Uses:* `ways_in/true-in-every-curved-world`

**Switching levels**

- To working when: uses index notation; asks how the rule is proved. Go to the proof at a point. *Uses:* `ways_in/proof-where-the-connection-vanishes`, `checks/why-special-coordinates-suffice`
- To formal when: asks about torsion or other connections; asks for the finite version. Give the Jacobi proof and the count of relations. *Uses:* `derivations/identity-from-jacobi`, `ways_in/any-connection-any-size`
- To research when: asks about numerical relativity, higher dimensions or gauge theories. Open the research horizon. *Uses:* `research_horizon/constraint-propagation`, `research_horizon/lovelock-gravity`

**Pronunciations:** Bianchi → bee-AHN-kee; Riemann → REE-mahn; Christoffel → kris-TOFF-el; Levi-Civita → LEH-vee CHEE-vee-tah; Noether → NUR-tuh; Voss → FOSS; Fourès-Bruhat → foo-REZ brew-AH

**Voice notes:** Stress the rotating pattern lambda mu nu, mu nu lambda, nu lambda mu, rather than every index.

## History

- **Aurel Voss (1880).** Derived a contracted form of the identity.
- **Luigi Bianchi (1902).** Published the full differential identity, which carries his name. Levi-Civita later reported that Ricci-Curbastro had found it around 1889 without publishing it. Luigi Bianchi (1902), *Sui simboli a quattro indici e sulla curvatura di Riemann*, Rendiconti della Reale Accademia dei Lincei, serie 5, 11, 3–7
- **Emmy Noether (1918).** Showed that symmetries depending on arbitrary functions force identities among field equations; for general relativity's freedom to relabel events these are the contracted Bianchi identities. Emmy Noether (1918), *Invariante Variationsprobleme*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse 1918, 235–257

## Research horizon

- **Constraint propagation in the initial value problem.** Einstein's equation splits into constraints on one moment and evolution equations. Through the contracted identity, the constraints and gauge conditions such as the harmonic condition obey their own evolution equations, so data that satisfy them keep satisfying them. This underlies existence theorems and numerical relativity. Yvonne Fourès-Bruhat (1952), *Théorème d'existence pour certains systèmes d'équations aux dérivées partielles non linéaires*, Acta Mathematica 88, 141–225, doi:10.1007/BF02392131
- **Lovelock gravity.** In more than four dimensions, symmetric divergence-free tensors built from the metric and its first two derivatives include higher-curvature Lovelock tensors, whose vanishing divergence again rests on the Bianchi identity. In four dimensions only the Einstein tensor and the metric remain. David Lovelock (1971), *The Einstein tensor and its generalizations*, Journal of Mathematical Physics 12, 498–501, doi:10.1063/1.1665613
- **Bianchi identity of gauge fields.** A non-abelian gauge field strength obeys $D_{[\lambda}F_{\mu\nu]} = 0$, the same identity with internal rotations in place of rotations of arrows. It is the half of the Yang–Mills equations that holds for any connection. Chen Ning Yang, Robert L. Mills (1954), *Conservation of isotopic spin and isotopic gauge invariance*, Physical Review 96, 191–195, doi:10.1103/PhysRev.96.191

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** You take a tiny box floating in curved space and carry an arrow around each face, going counterclockwise as seen from outside, and see how far its tip moved. Every edge gets walked both ways, so all six changes add to zero. I think that's because five faces make something whose edge is the sixth face backwards, but I'm not sure what 'outline' means, why the changes add like steps, or whether the detour to the far faces spoils anything. Top and bottom almost cancel, and the bit left over says how the curving changes going up. The three leftovers must add to zero, which somehow ties the directions together, but I couldn't say which change is tied to which. It's called the Bianchi identity, and it isn't a law you can test, because it only uses the edges of a box. Near Earth the numbers are tiny, but I'm confused: the Riemann note said a 1 square kilometre loop on the ground turns an arrow by 1.4 millionths of a degree, and here it's billions of times less. Compared with the takeaways, I got the box rule and the identity-versus-law point, but only half of the leftovers takeaway.

Second novice pass, reading revision 4 whole (2026-09-13). A tiny box floats in a curved space. You start at one corner, carry an arrow around each of the six faces, always counterclockwise seen from outside, and each time note how far the arrow's tip has moved and which way. For the three faces that do not touch your corner you walk out along an edge and back, and that out-and-back leaves no change. Add the six movements and you get nothing, because every edge of the box is walked once each way, so those walks cancel. Then pair up opposite faces: they are walked opposite ways, so if the curving were the same at both they would cancel, and what is left over says how the curving changes across the box. The three leftovers must add up to nothing, so two of them fix the third. That rule is the Bianchi identity, and no experiment can break it, because its reason only uses how a box's edges are shared. Near Earth the leftovers are far too small to notice. Where I stumbled: the first recap told me to take two loops "side by side" sharing a "side", but everywhere else that line is called an edge, and two faces of a box meet at a right angle rather than lying side by side, so I had to reread. "Looking at a face from its other side reverses the direction of turning" made me think the arrow's turn was reversed, because turn has been the arrow's word all along, and "Turn the sheet over" in the try-it made that worse. "The sixth face, which walks it the other way" gave a face legs. In the last way I was told the reason used two facts, then only the edge fact was defended, and I could not tell whether "It would first have to find" meant the experiment or the box. Against the takeaways: I could say all three back, but the third takeaway only in its concrete form (top and bottom, front and back, left and right), not in general.

**Stumbles (26)**

- “Every edge is walked once each way, so the changes add up to nothing, in any curved space. So curving cannot change from place to place in just any way.”: Summary: two jumps. Walking an edge both ways does not obviously make changes cancel, and nothing links a zero total to how curving changes.
- “Back home, the arrow's tip has usually moved a tiny distance. That movement is the face's change.”: The prerequisite taught that the arrow comes back turned. Why a turn is now measured by the tip is left implicit, and 'which way' is missing, although the checks add directions.
- “each time with a fresh arrow pointing the same way”: Unclear starting state: pointing the same way as what?
- “To reach each of the other three, walk along one edge first, go around the face, and come back along the same edge.”: A what-if left open: doesn't the extra walk along the edge change the arrow too?
- “Now add the six changes, the way you add small steps.”: Adding changes is new; one small example is needed.
- “Two tiny loops that share a side give changes that add up to the change around their outline”: 'Outline' is undefined, and the rule is taken on trust from a prerequisite without being restated in the recap. The sentence also adds a new term to the paragraph that makes the edge argument.
- “Five faces joined together have an outline: the four edges of the sixth face. That outline goes around the sixth face the opposite way, seen from outside.”: Hard to picture, and 'the opposite way' has no reason.
- “That means the six changes of a tiny box add up to nothing.”: First what-if: exactly nothing? The recap and the steps rule hold only nearly for tiny loops, and the entry prose must be true without simplifies.
- “For a box of any size, the six trips joined in a suitable order bring the arrow back matching its start exactly.”: 'Joined' trips is not something the reader can do, and the surprise has no reason.
- “Seen from above the box, the top face is walked counterclockwise and the bottom face clockwise.”: The switch in viewpoint for the bottom face (outside means from below) is left implicit, with no test to try.
- “It shows how the curving for level loops changes from the bottom of the box to the top.”: 'Level loops' is a second name for the tilt of the top face; 'level' in a curved space has no reference.
- “The six changes add up to nothing, so the three leftovers add up to nothing too.”: Missing link: why do the leftovers inherit the zero?
- “Suppose one leftover moves the tip up by 3 millionths of a millimetre”: 'Up' in a curved space has no reference; the checks say 'toward the top of the box'.
- “(no sentence: the leftovers are much smaller than the face changes)”: What-if: if adding changes is only nearly exact, how can the much smaller leftovers still be trusted to balance?
- “How it changes going up is tied to how it changes going forward and sideways.”: Loose: 'it' could be any curving, and the sentence hides that each direction pairs with a different tilt.
- “Near Earth, a level loop 1 kilometre on each side turns an arrow by only about 2 millionths of a billionth of a degree.”: This clashes with the prerequisite's number for a loop on the ground, about a billion times larger. 'Space at one moment' has its measurer only in simplifies.
- “Going 1 kilometre higher weakens that turn by about 1 part in 2,100. So nobody notices these leftovers.”: Missing step from a weaker turn to a size for the leftover.
- “The reason in "Six loops around a box" used one fact: every edge of a closed box belongs to two faces”: The reason also used the rule that tiny changes add like steps, so 'one fact' is false. 'Every curved space' fails the cone-tip what-if.
- “That rule could have been different, so experiments test it.”: The 'so' does not follow: a rule that could have been different does not by that alone need testing.
- “An identity cannot tell us which curved spaces exist.”: Mathematically, every invented space 'exists'; the point is which one our world has.
- “Every trip starts with the same fresh arrow.”: Check starting state: the same arrow reused, or a fresh one each time?
- “From one corner, you carry a fresh arrow around each face”: Check: faces that do not touch the corner cannot be walked from it without a detour.
- “You carry an arrow around each of its six faces and add up how it comes back changed. Could the total be anything”: Opening question: without a sense for each face the total really could be anything, so a correct novice answer would be marked wrong.
- “The curving side always obeys the Bianchi identity. So the equation can be true only if the matter side obeys a matching rule”: Entry common question: 'Einstein's equation' and 'the curving side' are undefined for this reader, and 'never made or destroyed at any place' hides how local the rule is.
- “Use the three leftovers of opposite faces to predict one from the other two”: Objective: 'leftovers of opposite faces' and the bare 'one' read ambiguously.
- “wording-trap warnings: counterclockwise with no viewpoint ('as seen by someone outside the box'); 'The same ring now runs clockwise.'; a 36-word recap sentence”: Validator warnings from rewritten text.

**Fixes**

- Summary: added the missing links (edge walks cancel, opposite faces leave amounts that must balance) and scoped it to smoothly curved spaces.
- Six loops way: defined a face's change as the tip's movement with its direction, fixed the fresh arrow's starting state, explained why the edge detour to far faces leaves no change, and added a steps example for adding changes. Also defined 'outline' in its own sentence and restated the two-loop rule in the recap. The lid-missing picture now gives the reason the rim runs the opposite way.
- Six loops way: added a scope paragraph saying adding changes is only nearly exact and its error shrinks faster than the changes, so the entry prose stays true without simplifies. Simplifies now describes a doable joined walk for boxes of any size.
- Leftovers way: explained the viewpoint switch for the bottom face, with a new try-it using a clear plastic sheet. Replaced 'level loops' with 'loops tilted like the top face', 'up' with 'toward the top of the box', and the loose tie sentence with one naming tilts and directions. The way now says the leftovers are the six changes grouped in pairs, and that the error from adding changes is smaller than the leftovers.
- Leftovers way: moved 'space around Earth at one moment' into the explanation with its measurer (clocks at rest around Earth). The floating level loop is now distinguished from a loop on the ground, reconciling it with the prerequisite's number. The 1 part in 2,100 is turned into a leftover size for a 1 kilometre box. Rechecked with python: tangential spatial curvature 3.43e-23 per square metre, 1.97e-15 degrees for 1 square kilometre, 3/r per km = 1 part in 2,124.
- True-in-every-space way: the reason now names both facts it uses, 'smoothly curved' scopes the claim, and simplifies says it rules out sharp points like a cone tip. Also fixed the stone-law 'so' and changed 'which curved spaces exist' to 'which curved space our world has'. The takeaway and the law-of-nature misconception correction now match.
- Entry checks: the-sixth-trip now describes the far-face detours, and leftover-of-the-third-pair fixes its starting state and adds the grouped-in-pairs step to its answer. The entry objective wording is clarified.
- Tutor: the box opening question gives each face's sense, and the entry common question on gravity defines Einstein's equation and its two sides.
- Glossary: added 'outline'; the 'leftover' definition now names the tilt.
- Ladder: the working proof way now bridges from the leftovers to components. It uses the course small-loop rule, orients each pair of cube faces outward with (lambda, mu, nu) in cyclic order, and gives each leftover as minus epsilon cubed times nabla lambda R V. I checked the sign by hand for the z, x and y pairs. It also says 'loops tilted like the top face', and the garbled 'locally inertial coordinates of the Riemann tensor in normal coordinates' became 'Riemann normal coordinates'.
- Budgets: entry explanations went from 697 to 1,052 words and way extras from 600 to 754, both inside the 10% review allowance (1,100 and 880), for the recorded stumble fixes only. Nothing was dropped.
- Bumped the revision to 2.

**Concerns**

- Physics reviewer: please confirm the new entry scope claims. First, adding face changes like steps has an error of order size to the fourth, smaller than the leftovers (size cubed), with lasso detours included when the home corner uses normal coordinates. Second, the edge detour leaves no extra change at the order that matters. Third, the any-size joined walk in simplifies retraces itself edge by edge, matching the formal way's lasso ordering.
- Physics reviewer: please check the new working bridge. With the course small-loop rule and outward-oriented faces, each pair's leftover is minus epsilon cubed times nabla lambda R rho sigma mu nu V sigma, with (lambda, mu, nu) a cyclic order of (x, y, z). The sign was checked by hand only.
- Physics reviewer: the entry common question on gravity says energy and momentum 'cannot appear or vanish at a place without flowing in or out'. Covariant conservation in curved spacetime is local and includes exchange with the gravitational field, so please confirm this spoken wording is acceptable or tighten it.
- Entry explanations now sit at 1,052 words, above the 1,000 cap but inside the review allowance. Any later entry additions need cuts, for example the ground-versus-floating comparison sentence.
- Writer's reports carried forward: the conventions file still needs a row for connection one-forms and curvature two-forms. The prerequisites differ from the registry, for sync_registry.py. Neither visual is in the catalog yet, and the cube-of-small-loops sketch should show the edge detours and the clear-sheet viewpoint switch that the entry ways now use.
- Physics diff check needed for revision 5. Three of the nine changed entry strings carry a claim: "Looking at a face from its other side reverses which way round the walk goes"; "The first is that tiny changes add like steps, in any smoothly curved space"; and "To find one, an experiment would have to break one of the two facts the reason uses. But tiny changes always add like steps in a smoothly curved space, and no closed box has an edge that belongs to only one face." The other six are wording only. Until that check runs, review.physics covers revision 4 and the validator says so.
- Status moved from physics-reviewed back to novice-reviewed because revision 5 has passed only the novice lens. review.physics is untouched and still records the full revision-4 verification, so a physics diff check over the nine changed strings can restore physics-reviewed.
- Left unfixed, and worth an editor's eye rather than more entry words: "change" is a noun for what an arrow's tip does and a verb for how curving varies ("the curving changes from the bottom of the box to the top"). Context separates them everywhere I read, and unpicking it would mean renaming the note's central term.
- Left unfixed: the general sentence "How the curving for one tilt changes in one direction is tied to how the curving for the other two tilts changes in the other two directions" does not say which direction goes with which tilt. The three sentences before it give the pairing concretely for top and bottom, front and back, and left and right, so a reader who has just read them can supply it; saying it in general would cost words the entry rung does not have.
- The summary runs to five sentences, where the guide asks for two or three. Every sentence earns its place after the earlier review added the missing links, so shortening it would mean dropping a link; flagged for an editor rather than cut.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 10 changed passages

- “So the equation can hold only if the matter side obeys a matching rule. For someone falling freely at any place, energy and momentum there cannot appear or vanish without flowing in or out.”: The listener is not told that the second sentence is the matching rule, so the link between the two sentences is left to supply (novice rule 3).
- “Over large regions, matter can still gain or lose energy by trading it with gravity. That matching rule is how Einstein's equation fits with the conservation of energy.”: Hearing that matter can gain or lose energy and then, at once, 'conservation of energy' sounds like a contradiction, and 'That matching rule' now sits far from the rule it names.
- “because the far face's edges are not parallel copies of the near face's; they cancel in the sum of the three pairs because $\Gamma$ is symmetric.”: One long sentence carries two claims joined by a semicolon, 'they' could mean the edges or the terms, and 'symmetric' does not say in which indices.
- Fix: Entry common question why-it-matters-for-gravity: named the second sentence as the matching rule, and moved the large-regions sentence after the conservation sentence with 'Even so'; no claim or scope changed.
- Fix: Working way proof-where-the-connection-vanishes: split the general-chart sentence in two, replaced 'they' with 'These extra terms', and said the symmetry is in the lower indices.
- Fix: Read without stumbles: the sixth-trip question, answer and key points (20+11+9=40, 19+12=31, 9 left); the experiment check's answer and key point; the ground-loop sentence in leftovers-from-opposite-faces; the round-space takeaway.

**Re-read** (2026-09-13, revision 5): 10 stumbles in 18 changed passages

- “Take two tiny loops side by side, walked the same way round. Their changes add up to the change around the path along the outside of both, because their shared side is walked once each way.”: Two words for one idea (rule 5). This recap calls the shared line a "side", while the way's own explanation, try-it and takeaway call it an "edge" a dozen times. "Side by side" also primes a flat picture, but the rule is then used on two faces of a box that meet at a right angle, so I reread to check it still applied.
- “Each rim edge also belongs to the sixth face, which walks it the other way.”: A rule the reader could not follow as written, and a reread: everywhere else the reader is the walker, so a face that walks an edge has no doer. "It" is also two nouns away from the rim edge.
- “Looking at a face from its other side reverses the direction of turning.”: One word for two kinds of turning, the trap the guide names. Up to this sentence "turn" has meant what the arrow does; here it means which way round the walk goes, so I first read it as "the arrow's turn is reversed".
- “Turn the sheet over and look at the ring from the other side.”: A third sense of "turn" in the try-it that is about which way round a ring runs, beside the arrow's turn and the walk's sense.
- “It would first have to find a closed box with an edge that belongs to only one face, and no such box exists.”: Ambiguous "It" (the experiment, or the tiny box of the sentence before), and a missing step: the same way says the reason used two facts, but only the edge fact is defended here, so the first what-if a reader tries is whether a space could break the other fact instead.
- “The first is that tiny changes add like steps, in any curved space.”: A general sentence that fails the cone-tip what-if, and it contradicts the same way's takeaway and simplifies, which scope the rule to a smoothly curved space.
- “The way a tiny loop is angled at a spot, set by the two directions its sides run along, like the bottom, front or side of a box.”: The glossary entry for "tilt" uses "side" twice in one sentence in two senses: first a loop's edges, then a face of a box.
- “Picture a level loop there, 1 kilometre on each side, floating in the air.”: "Side" again for a loop's edge, in the way whose recap defines tilt by the loop's edges. Same in "a box 1 kilometre on each side".
- “A rule that holds in every curved space is an identity, not a law that experiments test”: This key point of the check drops the scope its own answer, takeaway and simplifies all state, so a learner marking themselves keeps the unscoped claim.
- “You carry an arrow around each of its six faces, going counterclockwise as seen from outside the box, and add up how it comes back changed.”: Spoken opener: "it" follows "the box" and could be the box, a face or the arrow.
- Fix: One word per idea for the line where two faces meet: the six-loops recap and the leftovers recap, the tilt glossary entry and the two Earth measurements now all say "edge", matching the explanations, try-its and takeaways. "Side" is now left with one meaning in the entry text, which side of a surface you look from (a face of the box, a face of the plastic sheet). The equation's two sides in the spoken gravity answer are a different setting and were left alone.
- Fix: One word per idea for turning: "reverses the direction of turning" became "reverses which way round the walk goes", and "Turn the sheet over" became "Flip the sheet over", so "turn" belongs to the arrow alone.
- Fix: Six loops around a box: the face no longer walks its own edge; the reader does.
- Fix: True in every curved space: the no-experiment paragraph now names both facts the reason uses instead of one, and "It" became "an experiment". The first fact is now scoped to a smoothly curved space, which removes a contradiction with the same way's takeaway and simplifies and with the cone-tip case.
- Fix: Check an-experiment-to-break-it: key point 3 now carries the same "smoothly curved" scope as the answer, the point the earlier physics diff check left to an editor.
- Fix: Opening question picture-a-box-of-loops: "how it comes back changed" became "how the arrow comes back changed".
- Fix: Budgets: entry explanations went from 1,056 to 1,083 words, inside the review allowance of 1,100, and only for the stumbles above; way extras 754 to 755; tutoring 2,822 to 2,825. Nothing was dropped or compressed.
- Fix: Ladder re-read: each non-entry way's opening sentence still names the way it continues by title, no working sentence uses index notation before its prerequisites, and the three entry ways remain distinct routes (a picture, a calculation with the pairs, and a contrast with a law of nature). No bridge was missing.

**Re-read** (2026-09-13, revision 7): 6 stumbles in 5 changed passages

- “To break the rule, an experiment would have to break one of the two facts this reason uses.”: 'Break' is used in two senses one after the other: breaking the rule means showing it false, while breaking a fact sounds like snapping something (novice rule 5). The reader also has to hold 'the two facts' in mind with no statement of what would count as breaking one.
- “But tiny changes always add like steps in a smoothly curved space, and no closed box has an edge that belongs to only one face.”: After being told an experiment must break one of two facts, the reader is given the two facts but never told the conclusion, that neither can be broken; the last step of the answer is left to supply (novice rule 3).
- “The leftovers are usually much smaller than the face changes.”: 'Usually' is a scope word hidden in the middle of a short sentence, so a reader meets the exception before the rule and cannot tell what the exception is about: a strange box, a strange place, or a strange moment. Putting the scope first and naming what it ranges over settles it without promising a case the entry rung never shows.
- “For a tiny box, though, the error from adding changes like steps is smaller still.”: 'Smaller still' now has two candidates to be smaller than, the face changes and the leftovers, and the scoped sentence in front of it makes the reader pick. The next sentence, 'So the leftovers really must balance', only follows if the comparison is with the leftovers.
- “Its gradiometer senses $E_{ij}$ together with the centrifugal and angular-acceleration terms of the satellite's own turn, one turn per orbit to keep it facing Earth; these are reconstructed from the star trackers and from the antisymmetric part of the readings, then removed.”: One 46-word sentence squeezed across a semicolon carries two new ideas at once: that the instrument reads more than $E_{ij}$ because the satellite turns, and how that extra reading is measured and subtracted. A reader climbing to the working rung has to settle the first before the second means anything. 'One turn per orbit to keep it facing Earth' also hangs loose off 'turn', and 'these' has both the terms and the turn as candidates.
- “From 2009 to 2013 GOCE measured the tidal matrix $E_{ij}$ along its orbit, about 255 km above Earth and lower in its final year.”: 'About 255 km above Earth and lower in its final year' attaches to nothing named: on one reading the measuring was lower, on another the orbit was. Naming the orbit as the thing that ran at that height fixes the attachment without adding a height the sentence does not give.
- Fix: Check an-experiment-to-break-it: 'break one of the two facts' became 'show that one of the two facts this reason uses is false', so 'break' keeps one sense, and the closing sentence now states the conclusion ('But neither fact can fail:') before listing the two facts. Both facts keep their own wording and scope, and the verdict is unchanged.
- Fix: Way leftovers-from-opposite-faces: the physics reviewer's scope word moved to the front of its sentence as 'In most boxes', and 'smaller still' became 'smaller than the leftovers', which is the comparison the next sentence needs. Neither change touches a number, a sign or the size claimed.
- Fix: Observation goce-gravity-gradients: the 46-word semicolon sentence became two sentences, one for what the gradiometer senses and why the satellite turns, one for how the extra terms are recovered and removed; 'it' and 'these' became 'the satellite' and 'Those extra terms'; and the orbit is now named as the thing that ran about 255 km up. Every instrument, correction and scope claim is word for word the same.
- Fix: Budget: entry prose goes from 1,084 to 1,088 words against the 1,000 cap, inside the reviewer's 1,100 allowance, and the four words are the two recorded entry fixes. Nothing was dropped or compressed; the support and tutoring parts stay well under their caps.
- Fix: Read without stumbles: the rest of the experiment check's answer, question, key points and hint, which still read cleanly with the new last two sentences; the leftovers paragraph either side of the changed sentence; and the last two sentences of the GOCE connection with its numbers line.

**Re-read** (2026-09-13, revision 8): 0 stumbles in 2 changed passages


## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Entry: the six face changes of a tiny box sum to nothing; the error of adding like steps is of order size to the fourth, below the leftovers (size cubed), with the entry lasso detours.: Python RK4 parallel transport for a random torsion-free polynomial connection in three dimensions around the six coordinate faces, each outward-oriented, far faces lassoed along one edge from the home corner; eps = 0.04, 0.02, 0.01. Also the argument: the ordered product is exactly the identity, so the sum of (H_i - 1) equals minus products of pairs, O(eps^4); changing a lasso conjugates by a small loop, also O(eps^4). → Face change scales as eps^2 (5.1e-4, 1.2e-4, 3.1e-5), total as eps^4 (2.96e-6, 1.85e-7, 1.15e-8, ratio 16), both with Gamma = 0 at home and in a general chart. Confirmed.
- Entry: the walk out and back along an edge leaves no change of its own.: Lassoed holonomy is P^-1 H P, which is the identity exactly when the face holonomy H is. → True exactly. The conjugation is what turns partial into covariant derivatives in the leftovers, so it is not an error term.
- Entry simplifies and formal way: for any size of box, the six trips joined in a suitable order retrace every edge, so the arrow returns exactly.: Free-group reduction in python of the concatenated edge words for all 720 orderings of the six specific trips (near faces from home, far faces lassoed by one edge, outward orientation). Also checked that each of the 12 edges is walked once each way. → 6 orderings reduce to the empty word, for example x0, y1, z0, x1, y0, z1. Confirmed for exactly the trips the entry describes.
- Working bridge: with (lambda, mu, nu) cyclic and outward faces, each pair leftover is -eps^3 nabla_lambda R^rho_{sigma mu nu} V^sigma.: Hand: far face walks +mu,+nu giving -eps^2 R(far); near face walks +nu,+mu giving +eps^2 R(near). Numerics: same RK4 run compared against nabla R from analytic Gamma, in a chart with Gamma(home) = 0 and in a general chart. → Sign correct. With Gamma(home) = 0 the pair leftovers converge linearly to the prediction (x pair: -2.190, -2.174, -2.166 vs -2.157 times eps^3). In a general chart they do not (x pair -2.007 vs -1.941): each pair gains -eps^3(Gamma^a_{lambda mu} R^rho_{sigma a nu} + Gamma^a_{lambda nu} R^rho_{sigma mu a})V, confirmed numerically (extrapolated -2.056 vs predicted -2.057), and these cancel in the cyclic sum by symmetry of Gamma. Fixed: the bridge now takes Gamma = 0 at the home corner and states the general-chart terms.
- Key equation and proof at a point where the connection vanishes, including the six-term cancellation and tensoriality.: Re-derived by hand in course conventions; python check that the cyclic sum of numerically computed nabla R vanishes for the random connection. → Correct; numerical cyclic sum 2e-12 (Gamma = 0) and 5e-12 (general chart). Cyclic sum equals three times the antisymmetrization, since R is antisymmetric in its last pair.
- Contractions: nabla_rho R^rho_{sigma mu nu} = nabla_mu R_{sigma nu} - nabla_nu R_{sigma mu}; nabla_mu R^mu_nu = (1/2) nabla_nu R; which steps need a metric.: Hand derivation with R_{mu nu} = R^rho_{mu rho nu}; g^{sigma mu} R^rho_{sigma mu nu} = -R^rho_nu from first-pair antisymmetry. → Correct. Formal check (c) wording tightened: contracting sigma with mu needs a metric, first-pair antisymmetry and passing g through nabla need nabla g = 0.
- Two-dimensional emptiness and 3 equations in three dimensions.: Hand; count n^2(n^2-1)(n-2)/24. → Correct for the Levi-Civita connection; a torsion-free connection without a metric has 9. Working way now scopes the 3 to Levi-Civita, as the problem already did.
- Formal counts: nabla R has n^3(n^2-1)/12 components, the identity imposes n^2(n^2-1)(n-2)/24 relations (0, 3, 20), leaving 2, 15, 60; 60 = 200 - 140 Taylor count; 24 - 4 = 20 in four dimensions; contraction carries 4.: python arithmetic; cross-check with n^2(n^2-1)(n+2)/24 for the surviving dimension; 10*20 third derivatives of g minus 4*35 fourth-order coordinate freedoms. → All correct. In three dimensions R is fixed by G, so the identity is equivalent to nabla_mu G^mu_nu = 0: correct.
- Formal theorem with torsion and the Jacobi derivation, including the relabelling inside the cyclic sum; D Omega = d Omega + omega^Omega - Omega^omega = 0.: Re-derived each step by hand; differentiated Omega = d omega + omega^omega; checked omega^rho_sigma = Gamma^rho_{mu sigma} dx^mu against the course covariant derivative. → Correct, including signs of R(T(X,Y),Z); matches the standard statement for connections with torsion.
- Tidal matrix E_ij = c^2 R_{i0j0}, xi-double-dot = -E_ij xi^j, weak static E_ij = d_i d_j Phi, and d_k E_ij - d_j E_ik = -c d_t R_{i0kj}.: Course geodesic deviation with u = c e_0; identity with rho sigma = i0, lambda mu nu = k j 0; d_0 = c^-1 d_t; order-of-magnitude of the time term. → Correct in sign and factors of c; the time term is suppressed by (v/c)^2. Converse (symmetric, curl-free rows gives a local Hessian) correct locally.
- Earth numbers: E_xx = 1.54e-6 s^-2, d_x E_xz = -7.26e-10 s^-2 per km, 1 part in 2,124 per km; GOCE r = 6626 km: 1.37e-6, -2.74e-6, -6.20e-10 per km; check answer +6.20e-10 m/s^2 away from the line.: python with GM = 3.986e14 m^3 s^-2; E_xz = -3GM xz/r^5 from Phi = -GM/r; sense traced from the weaker horizontal pull higher up. → 1.5414e-6, -7.258e-10, 2123.7; 1.3702e-6, -2.7404e-6, -6.204e-10. All correct, sign and tolerance fine.
- Entry Earth numbers: floating level loop of 1 km^2 turns an arrow about 2e-15 degrees; 1 part in 2,100 per km higher; a pressed-against-the-ground loop turns far more.: Spatial Schwarzschild slice: K_t = 2GM/(c^2 r^3) = 3.43e-23 m^-2 (python); ground sphere K = 1/r^2; air density adds 16 pi G rho/c^2 = 4.5e-26 m^-2 to the scalar curvature. → 1.97e-15 degrees; ground loop 1.41e-6 degrees, 7.2e8 times more; 3/r = 1/2124 per km; air changes the level-loop number by about 0.1 percent. Correct. The ground comparison holds for an arrow kept against the ground, as the prerequisite defines it; wording fixed.
- Worked example: Ricci components of the round space, nabla_mu R^mu_s = A' + 2(f'/f)(A - B), K_t' = 2(f'/f)(K_r - K_t), star check with K_t = 2GM/c^2 r^3, K_r = -GM/c^2 r^3.: Hand derivation of each step and direct differentiation; K_r and K_t recomputed from f = r, f' = sqrt(1 - 2GM/rc^2); vacuum check R = 4K_r + 2K_t = 0. → All steps correct. Takeaway overclaimed that curvature cannot change at all where K_r = K_t; only K_t' vanishes there. Fixed.
- Entry checks and problems: sixth trip, third leftover, tent box (9 edges, 18 walks), constant-curvature proof (n-1)(n-2) dk = 0.: Arithmetic and hand proof. → All answers correct. The sixth-trip numbers (4, 2, 1 up; 1, 3 down; 3 down) could not come from a tiny box, whose opposite faces nearly cancel; replaced by 20, 11, 9 up and 19, 12 down, answer 9 down, which pair into leftovers of 1, 1 and 0.
- Entry common question: the identity forces a matching rule on matter, energy and momentum cannot appear or vanish without flowing in or out.: Compared with nabla_mu T^{mu nu} = 0: exact local conservation in a freely falling frame at a point; no global conservation law for matter energy in general spacetimes. → The unscoped wording implied matter energy is conserved everywhere. Rewritten: for someone falling freely at any place; over large regions matter can trade energy with gravity.
- Analogy: dF = 0 gives div B = 0 and Faraday's law; phases commute so the rule is an exact sum; a magnetic charge would break it.: Stokes on a closed surface; component split of the cyclic identity for F. → Correct, signs irrelevant (homogeneous).
- References: Rummel, Yi, Stummer 2011 J. Geod. 85, 777-790; Yang and Mills 1954 Phys. Rev. 96, 191-195; Lovelock 1971 J. Math. Phys. 12, 498-501; Fourès-Bruhat 1952 Acta Math. 88, 141-225; Noether 1918 Nachr. Ges. Wiss. Göttingen 235-257; Bianchi 1902 Rend. Lincei ser. 5, 11, 3-7.: The first three match entries already verified in other vault notes with the same DOIs; Crossref record for 10.1007/BF02392131; arXiv physics/0503066 record of the translation citing Gott. Nachr. 1918, 235-257; Wikipedia pages on Luigi Bianchi and the contracted Bianchi identities. → All confirmed; DOI added for Fourès-Bruhat. History: Voss 1880 published the contracted form in Mathematische Annalen, Levi-Civita reported Ricci found the identities around 1889 and forgot them, Bianchi rediscovered and published by direct calculation in 1902. Contributions as scoped are accurate.
- Second physics pass over revision 5 (all of it, not only the changed strings). Entry leftover picture and the component identity, re-derived from the course conventions rather than from the note: outward faces normal to x^lambda with (lambda, mu, nu) a cyclic order of (x, y, z) give a pair leftover -eps^3 nabla_lambda R^rho_{sigma mu nu} V^sigma.: By hand from the course small-loop rule: the far face (outward normal +lambda) walks +mu then +nu, giving -eps^2 R^rho_{sigma mu nu}V at the far corner; the near face, outward normal -lambda, walks +nu then +mu, giving +eps^2 R^rho_{sigma mu nu}V at the home corner. Independent python3 RK4 parallel transport for a fresh random torsion-free polynomial connection in three dimensions with Gamma(home) = 0, eps = 0.08, 0.04, 0.02, far faces lassoed along one edge. → Confirmed. Leftover divided by prediction 1.0067, 1.0094, 1.0061 (the residual is the finite-difference error in nabla R). The six-face total falls as eps^4 (2.69e-4, 1.75e-5, 1.12e-6; ratios 15.4 and 15.7 against 16) while a face change falls as eps^2, so the entry orders (total far below one face's change, leftovers between them) are right.
- Second pass: the cyclic sum is three times the antisymmetrization, and the cyclic sum of nabla R vanishes for an arbitrary torsion-free connection.: Hand: antisymmetrizing T_{lambda mu nu} = nabla_lambda R^rho_{sigma mu nu}, already antisymmetric in mu nu, over six permutations gives one third of the cyclic sum. Numerically: cyclic sum of the computed nabla R at the home corner of the random connection. → Both confirmed; numerical cyclic sum 3.7e-8 against nabla R components of order 1, which is the finite-difference floor of the test.
- Second pass: in three dimensions the identity is equivalent to nabla_mu G^mu_nu = 0, not merely equal in count.: New linear-algebra check in python3: with the Weyl tensor absent in three dimensions, build nabla_lambda R_{rho sigma mu nu} from an arbitrary symmetric nabla_lambda R_{sigma nu} at a point with g = delta, then compare the largest cyclic-sum residual with the residual of nabla_mu R^mu_nu - (1/2) nabla_nu R. → The two residuals are equal, term for term: 1.112, 0.780, 1.048 for random data, and 6e-15, 9e-15, 9e-15 once the contracted identity is imposed. Equivalence confirmed.
- Second pass: component counts 2, 18, 80 for nabla R; relations 0, 3, 20; survivors 2, 15, 60; and the Taylor cross-check.: python3 arithmetic for n^3(n^2-1)/12 and n^2(n^2-1)(n-2)/24, and for the independent count n(n+1)/2 times C(n+2,3) minus n times C(n+3,4) in every dimension, not only four. → 2 = 12 - 10, 15 = 60 - 45, 60 = 200 - 140. All three dimensions agree with the survivor counts, which is stronger evidence than the four-dimensional case alone.
- Second pass: the finite-box statement, that some ordering of the six lassoed face trips retraces itself exactly.: Fresh free-group reduction in python3 over all 720 orderings of the six specific trips (near faces walked from the home corner, far faces lassoed along one edge, every face outward-oriented), cancelling adjacent inverse edge walks. → 6 orderings reduce to the empty word, for example z0, x1, y0, z1, x0, y1. The six face loops between them walk each of the 12 edges once in each direction, with the three lasso edges walked out and back in addition. The entry simplifies and the formal way are both right.
- Second pass: the Jacobi derivation with torsion, and D Omega = d Omega + omega wedge Omega - Omega wedge omega = 0.: Each step re-derived by hand, including both relabellings inside the cyclic sum (R(nabla_X Y, Z) to -R(X, nabla_Y Z) and R(Y, nabla_X Z) to R(X, nabla_Z Y)) and the final relabelling that turns R(T(Y,Z),X) into R(T(X,Y),Z). D Omega re-derived from Omega = d omega + omega wedge omega with d(omega wedge omega) = d omega wedge omega - omega wedge d omega. → Correct, and the torsion term has the sign and slot order of the standard statement for connections with torsion.
- Second pass: the tidal equations, including the converse and the time term.: Identity with rho sigma = i0 and lambda mu nu = k j 0 written out by hand; geodesic deviation with u = c e_0 in the course convention; converse by the Poincare lemma (each row E_i is a closed one-form, so E_ij = partial_j A_i, and the symmetry of E makes A closed, so E is a Hessian locally); time term estimated as (v/c)^2 times the gradient. → All correct: xi-double-dot^i = -E_ij xi^j with E_ij = c^2 R_{i0j0}, partial_k E_ij - partial_j E_ik = -c partial_t R_{i0kj}, and the weak static signs (E_zz = -2GM/r^3 stretches along the radius, E_xx = +GM/r^3 squeezes across it).
- Second pass: every number in the note recomputed from scratch.: python3 with GM = 3.986e14 m^3 s^-2, c = 2.99792458e8 m/s, Earth radius 6371 km. → Earth surface E_xx = 1.5414e-6 s^-2, partial_z E_xx = -7.258e-10 s^-2 per km, ratio 2123.7; GOCE r = 6626 km (255 km up) E_xx = 1.3702e-6, E_zz = -2.7404e-6, partial_z E_xx = -6.2037e-10 per km, and the check's relative acceleration +6.204e-10 m/s^2 away from the vertical line, inside the 2 percent tolerance. Entry numbers: K_t = 3.4301e-23 m^-2, so a 1 km by 1 km level loop turns an arrow 1.965e-15 degrees (the note says about 2 millionths of a billionth), a loop on the ground 1.4116e-6 degrees (7.2e8 times more), and K_t falls by 3/r = 1 part in 2124 per km. The sixth-trip and third-leftover arithmetic and the tent's 9 edges and 18 walks all check out.
- Second pass: the round-space worked example.: Each step re-derived by hand: Ricci from sectional curvatures, nabla_mu R^mu_s = A' + 2(f'/f)(A - B) from Gamma^theta_{theta s} = Gamma^phi_{phi s} = f'/f, then the contracted identity; direct differentiation of K_t = (1 - f'^2)/f^2 as an independent route; f'' = GM/(c^2 r^2) for the star check. → K_t' = 2(f'/f)(K_r - K_t) by both routes. For f = r, K_t = 2GM/c^2r^3 and K_r = -GM/c^2r^3 give R = 4K_r + 2K_t = 0 exactly, as vacuum requires, and both sides of the star check equal -6GMf'/(c^2r^4).
- Second pass: the nine learner-visible strings the novice re-read changed at revision 5, the three claim-bearing ones first.: Read each against the note's own scope. 'Looking at a face from its other side reverses which way round the walk goes': a circuit seen from the two sides of its face runs opposite ways, which is what the outward orientation of the bottom face needs. 'The first is that tiny changes add like steps, in any smoothly curved space': the eps^4 error above, with smoothness required. 'To find one, an experiment would have to break one of the two facts the reason uses...': both facts named, the first scoped to a smoothly curved space. The other six changes (share an edge, you walk it the other way, flip the sheet, the tilt glossary's left face, 1 kilometre along each edge, and the arrow in the opening question) carry no claim. → All nine accurate; none needed a change. The neighbouring answer of check an-experiment-to-break-it still carried the older one-fact version of the same claim and is fixed in this pass.
- Second pass: every reference and history claim re-confirmed against an independent record.: Rummel, Yi and Stummer 2011 checked against the publisher record (Journal of Geodesy 85, 777-790, DOI 10.1007/s00190-011-0500-0); Lovelock 1971 against the publisher and abstract records; Yang and Mills 1954 against the journal's own DOI page; Bianchi 1902 title, series, volume and pages against two independent accounts; Noether 1918 and Foures-Bruhat 1952 unchanged from the first pass. History: Voss 1880 checked for what exactly was first; the Ricci attribution traced to Levi-Civita's own report. → All six confirmed. DOIs added for Lovelock (10.1063/1.1665613) and Yang and Mills (10.1103/PhysRev.96.191). Voss 1880 did publish a contracted form, in Mathematische Annalen 16, 129-178, so the note's scoped contribution is right; the primary work is still recorded as null, which an editor may fill. Levi-Civita did report that Ricci-Curbastro found the identities about 1889; Ricci himself never published them, although Padova stated them without proof in 1889 on Ricci's spoken communication, so the note's wording is true as it stands.
- Second pass: GOCE's gradiometer is not the non-rotating instrument the note's E_ij is defined for.: Checked the mission's own description of the instrument: each accelerometer pair senses gravitational gradients together with centrifugal terms (squares of angular velocities) and Euler angular accelerations, which are separated using the antisymmetric part of the acceleration differences and the star trackers. Also checked the orbit: 255 km mean altitude held to July 2012, then lowered in stages to 224 km by May 2013. → The observation claimed a measurement of E_ij in a frame the satellite does not have (it turns once per orbit to face Earth). Fixed by naming the rotation terms and their removal, and by saying the orbit was lower in the final year.

**Counterexamples tried**

- Cone tip or cosmic-string line inside the box: face changes are not tiny, adding like steps fails, and the sum of changes is not small, although the ordered product of lassoed holonomies is still exactly the identity. The entry scope "smoothly curved" covers it; the check answer that said "every curved space" now says "every smoothly curved space".
- Round three-sphere (nabla R = 0): every leftover vanishes to order eps^3, so opposite faces cancel; consistent with the leftover check (b).
- General chart with nonzero Christoffel symbols at the corner: individual pair leftovers are not -eps^3 nabla R V; only their sum is covariant. Fixed in the working bridge.
- Two dimensions: identity empty; ellipsoid shows K may vary, consistent with the formal problem.
- Torsion-free connection with no metric in three dimensions: 9 relations, not 3; working sentence scoped to Levi-Civita.
- Connection with torsion: box product still exactly the identity and D Omega = 0, but the component cyclic sum gains the torsion term; matches the formal limits.
- Time-dependent field (moving sources): tidal gradients need not be fully symmetric; the note gives the -c d_t R term and the (v/c)^2 suppression.
- Expanding universe or a falling stone: matter energy over large regions is not conserved, although nabla T = 0 holds locally; the entry answer now says so.
- Point where K_r = K_t in a round space but not in a neighbourhood: K_r may still change outward; takeaway scoped.
- Non-shrinkable loops (a flat torus or cone complement): the identity is local and leaves their holonomy free, as the formal limits state.
- A spot where the curving for one tilt passes through zero while it is still changing: there a face change is itself of order eps^3, so it is not much larger than the leftover. The entry sentence now says the leftovers are usually much smaller than the face changes.
- A cone edge or cosmic string threading one face of the box: the face changes are not tiny, they do not add like steps, and the six changes need not sum to nothing, yet every edge still belongs to two faces. So the entry check's old 'would first have to find a closed box with an edge on only one face' named a way out that is not the only one; the answer now names both facts, as the way does.
- A rotating gradiometer, GOCE itself: its readings are E_ij plus centrifugal and Euler terms of its own one turn per orbit, so 'measured the tidal matrix' needed the frame and the correction named.
- Three dimensions with the Weyl tensor absent: the identity carries exactly the content of nabla_mu G^mu_nu = 0, checked numerically as equal residuals, so the working way's claim is an equivalence and not just a matching count.

**Fixes**

- Working proof way: per-pair leftover -eps^3 nabla_lambda R V now stated in coordinates with Gamma = 0 at the home corner, with the general-chart extra terms and why they cancel in the sum.
- Working proof way: "in three it gives 3 independent equations" scoped to the Levi-Civita connection.
- Worked example takeaway: where K_r = K_t only the tangential curvature cannot change outward.
- Entry leftovers way: the ground-loop comparison now says the arrow is pressed against the ground, matching the prerequisite and making the comparison true.
- Entry check the-sixth-trip: numbers changed to 20, 11, 9 toward the top and 19, 12 toward the bottom (answer 9 toward the bottom, numeric -9e-6 mm), so opposite faces can nearly cancel as the note says.
- Entry check an-experiment-to-break-it: answer now names both facts of the reason and scopes the claim to smoothly curved spaces; key point updated.
- Entry common question why-it-matters-for-gravity: local conservation scoped to someone falling freely at a place, with the added sentence that over large regions matter can trade energy with gravity.
- Formal check does-it-need-a-metric (c): separated what needs a metric from what needs nabla g = 0.
- References: all six verified; DOI added for Fourès-Bruhat 1952.
- Status physics-reviewed; revision bumped from 2 to 3 for the entry and working changes.
- Second physics pass (revision 5 to 6). Entry leftovers way: 'The leftovers are much smaller than the face changes' scoped to 'usually', because where the curving for that tilt passes through zero the face change is the same order as the leftover. One word; no step removed.
- Second pass. Entry check an-experiment-to-break-it: the closing sentences now say an experiment would have to break one of the two facts the reason uses, and name both, instead of claiming it would first have to find a closed box with an edge on only one face. That matches the way's own wording and closes the sharp-point way out.
- Second pass. Observation goce-gravity-gradients: named the frame. The gradiometer senses E_ij together with the centrifugal and angular-acceleration terms of GOCE's one turn per orbit, reconstructed from the star trackers and the antisymmetric part of the readings and then removed; the orbit is also said to be lower in the final year.
- Second pass. References: DOIs added for Lovelock 1971 and for Yang and Mills 1954; all six references and all three history entries re-confirmed against independent records.
- Second pass. Status physics-reviewed; revision bumped from 5 to 6 for the two entry-rung changes and the one working-rung change. reviewed_revision 6.

**Concerns**

- A novice re-read is needed for exactly three changed learner strings: the word 'usually' in the leftovers way, the last two sentences of check an-experiment-to-break-it, and the two new sentences of the GOCE observation. Until it runs, the validator's one warning (review.novice covers revision 5, the note is at 6) is expected.
- Entry way explanations are now 1,084 words against the 1,000 cap, inside the reviewer's 1,100 allowance with 16 words of headroom. Any further entry-rung addition must be paid for by a recorded cut.
- The conventions file still lacks a row for connection one-forms and curvature two-forms (omega^rho_sigma = Gamma^rho_{mu sigma} dx^mu, Omega = d omega + omega wedge omega, D Omega = d Omega + omega wedge Omega - Omega wedge omega); the formal way and the formal check both use this choice. Reported rather than invented here.
- The prerequisites still differ from the registry for covariant-derivative-of-a-tensor, holonomy, riemann-curvature-tensor and torsion-free-connection; sync_registry.py resolves it, but it touches the shared registry. Outside a reviewer's remit.
- Both visuals, cube-of-small-loops (flagship) and falling-ring-of-crumbs (supporting), are still proposals with sketches only. If the cube demo ever prints per-pair leftovers as nabla R, it must use Gamma = 0 at the home corner or show only the sum of the three pairs, since in a general chart a single pair's leftover is not covariant.
- Voss 1880 is confirmed as Mathematische Annalen 16, 129-178, but the history entry's work is still null. An editor may add it; I left it out rather than transcribe a long title I could only read through secondary records.
- Carried forward from the novice pass and still true after this one, all accurate and all matters of taste rather than correctness: 'change' is both the note's central noun and a verb for how curving varies; the general tie sentence does not say which direction pairs with which tilt, relying on the three concrete sentences before it; and the summary runs to five sentences where the guide asks for two or three.

**Diff check** (2026-09-13, revision 4)

- Entry common question why-it-matters-for-gravity: 'The rule says that, for someone falling freely at any place, energy and momentum there cannot appear or vanish without flowing in or out.': Compared with the pre-reread sentence and with the contracted Bianchi identity: the divergence of the Einstein tensor vanishes, so the equation forces the divergence of the stress-energy tensor to vanish; at a point, in a local inertial (freely falling) frame, that reduces to the flat-space continuity equation for energy and momentum. → True and the same claim as before; the added 'The rule says that' only names it as the matching rule of the previous sentence.
- Same answer: 'That matching rule is how Einstein's equation fits with the conservation of energy. Even so, over large regions, matter can gain or lose energy by trading it with gravity.': Checked the new order and the contrast 'Even so' against what local conservation does and does not imply; tried the what-if of an expanding universe (radiation loses energy to redshift) and of a curved spacetime without a time symmetry, where no conserved total matter energy exists. → True. Local conservation holds while no general global conservation of matter energy exists, so 'Even so' marks a real contrast and removing 'still' drops no condition. Scope unchanged.
- Working way proof-where-the-connection-vanishes: in a general chart the extra terms -eps^3(Gamma^a_{lm}R^r_{s a n} + Gamma^a_{ln}R^r_{s m a})V^s cancel in the sum of the three pairs because Gamma is symmetric in its lower indices.: Wrote out the cyclic sum over (l,m,n) by hand: the six terms pair Gamma^a_{lm}R_{s a n} with Gamma^a_{ml}R_{s n a}, and so on, cancelling by lower-index symmetry of Gamma together with last-pair antisymmetry of Riemann. Recomputed in python3 with a random symmetric Gamma and a random last-pair-antisymmetric R in 3 dimensions (sum -5.6e-17), and with a random non-symmetric Gamma (sum 1.06). → True. 'Symmetric in its lower indices' is exactly the torsion-free condition in a coordinate chart, matching the way's simplifies field and course conventions; the split sentence claims what the old one did, and 'These extra terms' refers to the right objects. The Riemann antisymmetry the cancellation also uses is stated later in the same explanation.
- Novice re-read proposal: check an-experiment-to-break-it key_points[2] says 'holds in every curved space' while the answer says 'every smoothly curved space'.: Outside the changed text; read both for accuracy at the entry rung. → Not an error: at the entry rung 'curved space' already means a smoothly curved space, and a key point is a grading cue. Left unedited to keep this check to the changed strings; an editor may align the wording.
- Fix: No fixes: both changed strings are accurate as reworded; no learner-visible text changed.

**Diff check** (2026-09-13, revision 8)

- Check an-experiment-to-break-it, changed sentences: 'To break the rule, an experiment would have to show that one of the two facts this reason uses is false. But neither fact can fail: tiny changes always add like steps in a smoothly curved space, and no closed box has an edge that belongs to only one face.': Read the whole answer as the referee. Checked that the two facts named here are the two the answer's own reason uses (edges shared by two faces; tiny changes adding like steps) and that they are stated with the same scopes as before. Tried the note's own counterexamples: a cone tip or a cosmic string threading a face (not a smoothly curved space, so outside the stated scope), a box with an edge on a boundary (not a closed box), and a connection with torsion (excluded by course conventions, whose Riemann row is torsion-free). → Accurate and the same claim as before. 'But neither fact can fail:' only names the conclusion the previous wording left the reader to draw; the fact list, its order and its scope words are word for word what the physics review signed. The unsaid hypothesis is smoothness, and it is stated inside the sentence.
- Observation goce-gravity-gradients, changed sentences: the orbit 'ran about 255 km above Earth and lower in its final year'; the gradiometer senses the tidal matrix together with the centrifugal and angular-acceleration terms of 'the satellite's own turn, which is one turn per orbit and keeps the satellite facing Earth'; 'Those extra terms are reconstructed from the star trackers and from the antisymmetric part of the readings, then removed.': Checked the altitude against the note's own numbers field with python3: 6371 km + 255 km = 6626 km, the radius the numbers use, and recomputed GM/r^3 = 1.370e-6 s^-2, -2GM/r^3 = -2.740e-6 s^-2 and -3GM/r^4 = -6.20e-10 s^-2 per km, matching the three quoted values. Checked the instrument claim against the measured combination: a gradiometer reads the gravity gradient together with the centrifugal term built from the angular velocity and the angular-acceleration term, whose antisymmetric part is the angular acceleration alone; an Earth-pointing satellite holds its attitude in the local orbital frame, which is one rotation per orbit relative to the stars. Checked that splitting the old semicolon sentence in two moved no claim: 'Those extra terms' has only the centrifugal and angular-acceleration terms as candidates, and the reconstruction and removal stay attached to them. → Accurate. Altitude, instrument model, correction route and the final-year lowering all hold, and every number in the observation is unchanged and reproduced. The rewritten sentences claim exactly what the old ones did; no frame, sense or condition moved. The reference was confirmed at the earlier physics review and is untouched.
- Way leftovers-from-opposite-faces, changed sentence: 'In most boxes the leftovers are much smaller than the face changes.': Compared with the signed wording ('The leftovers are usually much smaller than the face changes') and checked the scaling: for a box of side eps a face change is of order curvature times eps squared and a pair's leftover of order the curvature's rate of change times eps cubed, so the ratio is of order eps divided by the distance over which the curving changes. Checked against the way's own number, a 1 km box near Earth, where 3/6371 gives 1 part in 2,124, close to the quoted 1 part in 2,100. → Accurate, and the same hedge as the signed sentence with the scope moved to the front. 'Most boxes' is honest: the statement fails only for boxes as large as the distance over which the curving changes, which the way never uses.
- Way leftovers-from-opposite-faces, changed sentence as the re-read left it: 'For a tiny box, though, the error from adding changes like steps is smaller than the leftovers.': Re-derived the orders for a box of side eps: adding face changes like steps instead of composing them costs a commutator of two face changes, of order curvature squared times eps to the fourth, while a pair's leftover is of order the curvature's rate of change times eps cubed, so the error falls away one power of eps faster. Then tried the standard limits on the sentence as a universal claim about tiny boxes: flat space, where every face change, every leftover and the error are zero, and a space whose curving is the same everywhere, where the leftovers vanish while the error does not. → The order comparison is right wherever the curving changes from place to place, but the sentence as written is false in exactly those two limits, because it compares a leftover that is zero with an error that is not. The signed wording said 'smaller still', which left the comparison open; making it explicit hardened it into a claim the flat-space limit breaks. Fixed by stating the condition first, in the way's own words.
- Budget after the fix.: Ran the validator word counts before and after the edit. → Entry prose 1,088 -> 1,094 words against the 1,000 cap, inside the reviewer's 1,100 allowance with 6 words of headroom left, and the six words are the recorded accuracy fix. Support 1,774/2,300, tutoring 2,850/3,300, links 562/900, total 8,000/9,500. Nothing was dropped or compressed.
- Fix: ways_in[leftovers-from-opposite-faces].explanation: 'For a tiny box, though, the error from adding changes like steps is smaller than the leftovers.' -> 'Where the curving changes from place to place, the error from adding changes like steps is smaller than a tiny box's leftovers.' The comparison only holds where there is a leftover to compare with: in flat space, and in a space whose curving is the same everywhere, the leftovers are zero while the error of adding like steps is not. The condition now comes first, as the re-read did for the neighbouring sentence, and the tiny box is kept, so both hypotheses are in the sentence. The conclusion it supports, 'So the leftovers really must balance', is unchanged and still holds in the excluded cases, where all three leftovers are zero.
- Fix: No other change: the check answer and the GOCE observation were checked and left exactly as the re-read wrote them.
