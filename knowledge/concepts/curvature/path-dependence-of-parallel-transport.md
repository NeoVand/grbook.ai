---
type: "concept"
id: "path-dependence-of-parallel-transport"
title: "Path dependence of parallel transport"
domain: "curvature"
tier: "core"
aliases: ["no global parallelism", "no global Cartesian grid", "non-integrability of parallel transport", "route dependence of transported vectors"]
prerequisites: ["parallel-transport", "curvature"]
leads_to: ["holonomy", "riemann-curvature-tensor", "flatness-criterion", "integrability-condition-for-parallel-fields", "global-energy-momentum-conservation"]
sources: ["dinverno:ch06", "gifted-amateur:ch12", "gifted-amateur:ch35", "legacy:lesson-carry-a-direction-without-turning-it", "legacy:scene-3d-parallel-transport-two-routes", "schutz:ch06", "schutz:ch07"]
review: "fixed"
---

# Path dependence of parallel transport

> On a curved space, carrying an arrow from one place to another without ever turning it gives an answer that depends on the road you took. Two arrows that start together and travel by different routes can disagree when they meet, so 'pointing the same way' only makes sense at a single point. This is why curved spacetime has no global grid of parallel axes and no invariant way to add up vectors that live at different events.

## Explanations by level

### Intuition

Imagine walking on a huge ball holding a pointer, with one rule: never twist it relative to the ground under your feet, so each step it points as nearly as possible where it pointed a moment ago. Start on the equator with the pointer aimed east. Walk due north to the pole, then walk south down a different line of longitude a quarter of the way around, then walk west along the equator back to your start. You never turned the pointer, yet it now aims due south: a quarter turn. Or send two friends from the same spot with identical pointers, one straight to a meeting place and one via a detour: they arrive disagreeing. Do the same on a flat floor, or on a sheet of paper rolled into a tube, and the pointers always agree. The ball is different because its surface is curved from the inside, not merely bent in space. What this picture simplifies: the ball is a two-dimensional surface we view from outside, while in spacetime there is no outside; and in spacetime the mismatch between two routes can be a change of velocity (a boost) rather than only a rotation.

**Picture to hold:** Two walkers leave the same equator point on a globe with arrows pointing east; one walks along the equator, the other goes over the pole; at the meeting point their arrows are at right angles.

**Assumes:** [[parallel-transport]], [[curvature]]

### Working

Parallel transport along a curve $x^\mu(s)$ solves $\dfrac{dV^\mu}{ds} + \Gamma^\mu{}_{\nu\sigma}\dfrac{dx^\nu}{ds}V^\sigma = 0$. Given the starting vector and the route, the answer at the far end is unique, but a different route to the same endpoint solves a different equation and in general gives a different vector. You can see the size of the effect for two nearby routes: go first along a small displacement $\delta x$ and then $\Delta x$, or take the other order. The arrival by the $\delta x$-first route minus the arrival by the $\Delta x$-first route is $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma\,\delta x^\mu \Delta x^\nu$. This is second order in the displacements, and its coefficient is the Riemann tensor, which gets its own note next; here it is enough to know it is built from the Christoffel symbols and their derivatives. No curvature, no mismatch; curvature, mismatch. On a sphere of radius $a$, any two routes that together bound a region of area $A$ deliver arrows rotated relative to each other by $A/a^2$. The routes do not have to be geodesics, and the octant gives $\pi/2$. Two consequences follow. First, a field that is parallel everywhere, $\nabla_\mu V^\rho = 0$, cannot exist unless $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$, so you cannot fill a curved region with a Cartesian grid of transported axes. Second, four-momenta at different events live in different tangent spaces; to add them you must first transport them to one point, and the total depends on the routes, so 'total four-momentum' is not the simple sum it is in special relativity. Be careful not to confuse this with changing components: in polar coordinates on a flat plane a transported arrow has changing components, yet every route delivers the same arrow.

**Picture to hold:** A small coordinate parallelogram: one arrow goes along the bottom then up the right side, a twin goes up the left side then along the top; at the far corner a tiny gap arrow between them scales with the parallelogram's area.

**Assumes:** [[parallel-transport]], [[christoffel-symbols]]

### Formal

Let $M$ carry a torsion-free connection $\nabla$ (in GR the Levi-Civita connection of $g$). For a piecewise smooth curve $\gamma$ from $p$ to $q$, parallel transport defines a linear isomorphism $P_\gamma: T_pM \to T_qM$; if $\nabla g = 0$ it is an isometry, so on a Lorentzian manifold it preserves norms and the mismatch between routes is a Lorentz transformation (rotation, boost or a combination). Transport is path dependent when $P_{\gamma_1} \neq P_{\gamma_2}$ for two curves with the same endpoints, which is the same as saying the closed loop $\gamma_2^{-1}\circ\gamma_1$ has nontrivial holonomy. For infinitesimally separated routes the difference is $-R^\rho{}_{\sigma\mu\nu}V^\sigma\delta x^\mu\Delta x^\nu + O(3)$. Theorem (integrability): on a simply connected region, transport is independent of path for every pair of curves if and only if $R^\rho{}_{\sigma\mu\nu} = 0$ there. Necessity follows because a parallel field through every vector at a point requires the mixed partials of $\partial_\mu V^\rho = -\Gamma^\rho{}_{\mu\sigma}V^\sigma$ to commute, which gives $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$ for all $V$; sufficiency follows by deforming one curve into the other through a sequence of thin loops, each contributing nothing. Without simple connectedness, vanishing curvature only guarantees independence within a homotopy class: on a cone with its apex removed the geometry is flat, yet transport around the apex rotates vectors by the deficit angle. With torsion the story changes: zero curvature still gives path independence, but no coordinates make the connection vanish. Physical corollaries: there is no canonical identification of tangent spaces at separated events, hence no invariant sum of four-momenta and no global energy-momentum conservation law for matter unless a Killing symmetry or asymptotic flatness supplies one.

**Picture to hold:** The space of all curves from p to q, each labelled by the linear map it induces; in a flat simply connected region every label is the same map, in a curved region the labels vary continuously as the curve is deformed across curvature.

**Assumes:** [[parallel-transport]], [[riemann-curvature-tensor]], [[simply-connected-space]], [[torsion-tensor]]

## Prerequisites

- [[parallel-transport]] — The phenomenon is a property of the transport rule itself; the learner must know how a vector is carried along one curve before comparing two curves.
- [[curvature]] — Path dependence is presented as the inside-the-space signature of curvature, so the learner needs the idea that a space can fail to be flat.

## Leads to

- [[holonomy]] — Closing two routes into a loop turns the mismatch into the return change of a vector, which makes it quantitative (area times curvature).
- [[riemann-curvature-tensor]] — The infinitesimal two-route mismatch is the Riemann tensor contracted with the vector and the two displacements; Schutz and Gifted Amateur define Riemann this way.
- [[flatness-criterion]] — Path independence on a simply connected region is equivalent to vanishing Riemann tensor, the working test for flatness.
- [[integrability-condition-for-parallel-fields]] — The failure of globally parallel fields is made precise by the integrability condition R V = 0.
- [[global-energy-momentum-conservation]] — Because vectors at separated events cannot be added invariantly, a global conservation law for matter energy needs a Killing symmetry.

## Related

- [[angular-excess]] — On a surface the rotation between two geodesic routes equals the angular excess of the triangle they bound.
- [[intrinsic-versus-extrinsic-curvature]] — The rolled-paper cylinder is bent but transport on it is path independent, isolating intrinsic curvature as the cause.
- [[nonzero-christoffel-symbols-in-flat-space]] — Changing components along a route in curvilinear coordinates must not be mistaken for path dependence.
- [[lie-bracket]] — Non-commuting flows give an endpoint mismatch even in flat space; path dependence is a direction mismatch at a shared endpoint, a different effect.
- [[gauge-parallel-transport]] — A charged field's phase transported along two routes differs by the enclosed field-strength flux, the gauge-theory version of the same idea.
- [[conservation-of-four-momentum]] — Special relativity sums four-momenta freely; path dependence is why that sum loses invariant meaning in curved spacetime.

## Key equations

### Parallel transport along a curve

$$
\frac{dV^\mu}{ds} + \Gamma^\mu{}_{\nu\sigma}\,\frac{dx^\nu}{ds}\,V^\sigma = 0
$$

A first-order ODE: given the route x(s) and the starting vector it fixes the transported vector uniquely along that route. A different route means a different ODE, hence possibly a different result. *(SCH ch06 §6.4 p.154; DIV ch06 §6.7 p.97; GA ch11 §11.3 p.124)*

**Convention:** Course convention puts the derivative index first on Gamma; Schutz and d'Inverno put it last. For the torsion-free Levi-Civita connection the two readings agree.

### Mismatch between two infinitesimal routes

$$
\Delta V^\rho \equiv V^\rho_{(\delta x\ \text{first})} - V^\rho_{(\Delta x\ \text{first})} = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma\,\delta x^\mu\,\Delta x^\nu + O(3)
$$

Carry V to the far corner of a tiny parallelogram by its two edge orders; the arrivals differ by a term linear in V and in each edge, antisymmetric in the edge order, with the Riemann tensor as coefficient. It vanishes for every V and every plane only if R = 0. *(DIV ch06 §6.7 p.98; DIV ch06 Fig. 6.9 p.97; legacy:manuscript-section-8-1-8-3-riemann-commutator-and-loop)*

**Convention:** d'Inverno writes the same result with index names a b c d and the connection's derivative index last; the sign agrees with the course because both use the MTW Riemann convention.

### Integrability condition for a globally parallel field

$$
\nabla_\mu V^\rho = 0 \ \text{everywhere} \;\Longrightarrow\; R^\rho{}_{\sigma\mu\nu}\,V^\sigma = 0
$$

Requiring a vector field to be parallel along every direction forces its mixed second partial derivatives to agree, which only happens where the Riemann tensor annihilates it. A full grid of parallel axes therefore needs R = 0. *(SCH ch06 Ex 6.11; DIV ch06 §6.7 p.96; GA ch35 §35.3 p.369)*

### Route mismatch on a sphere

$$
\Delta\alpha = \frac{A}{a^2}\quad(\text{octant: } A = \tfrac{1}{8}\,4\pi a^2 \Rightarrow \Delta\alpha = \tfrac{\pi}{2})
$$

On a sphere of radius a, two geodesic routes between the same points deliver arrows rotated relative to each other by the area they enclose divided by a squared. It depends on angular size, not on the sphere's radius, for a triangle of fixed angles. *(SCH ch06 Fig. 6.3 p.153; SCH ch06 Ex 6.10; legacy:scene-3d-parallel-transport-two-routes)*

**Convention:** Radius written a (course practice) so that R stays reserved for curvature. The sense of rotation follows the orientation of the loop formed by the two routes.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Index order on the connection in the transport equation | Derivative (direction) index last: dV^alpha/dlambda + Gamma^alpha_{mu beta} V^mu U^beta = 0 (SCH ch06 §6.3). | Derivative index first: dV^alpha/dx^1 = -Gamma^alpha_{1 beta} V^beta in the loop calculation (GA ch11 §11.3); ch35 states nabla_mu e_nu = Gamma^alpha_{mu nu} e_alpha. | Derivative index last: the transported change is -Gamma^a_{bc} X^b delta x^c (DIV ch06 §6.7), matching nabla_c X^a = d_c X^a + Gamma^a_{bc} X^b. | Derivative index first, nabla_mu V^nu = d_mu V^nu + Gamma^nu_{mu lambda} V^lambda. Identical results for the symmetric (torsion-free) connection used in GR; flag the order only if torsion is discussed. |
| Which connection the theorem is stated for | Metric (Levi-Civita) connection only; states that transport around a loop in curved space changes a vector and that no globally parallel field exists. | Metric connection; ch35 phrases the consequence as the impossibility of a global Cartesian grid. | General affine connection, possibly with torsion; defines an integrable connection as one with path-independent transport and proves integrable iff Riemann vanishes, assuming a simply connected manifold; affine flatness additionally needs a symmetric connection. | Torsion-free metric connection. State the simple-connectedness condition explicitly at formal level, and mention that with torsion, zero curvature does not give coordinates with vanishing Gamma. |
| Terminology | No special term; speaks of parallelism failing and of no globally parallel vector field. The word holonomy is not used. | 'Being parallel is path dependent'; ch35 'no Cartesian grid'. | 'Integrable connection' for path-independent transport. | 'Path-dependent transport' for two routes, 'holonomy' for the closed-loop version, 'integrable' only at formal level. |
| Metric signature | (-,+,+,+) | (-,+,+,+) | (+,-,-,-) (signature -2) | (-,+,+,+). Christoffel symbols, the transport equation and the route mismatch are unchanged by an overall sign flip of g, so d'Inverno's results transfer directly. |

## How the sources teach it

### schutz

**Route:** After developing Christoffel symbols and parallel transport, §6.4 runs a flat control (an arbitrary loop in the plane, arrows redrawn parallel, no change) and then the sphere octant loop with two corners on the equator and one at the pole, where the arrow returns turned by a quarter. The conclusion is drawn at once: parallelism is not global on curved manifolds. §6.5 reuses the loop to define the Riemann tensor, Exercise 6.10 generalizes the octant to the angular-excess law and Exercise 6.11 derives the condition for a globally parallel field. Chapter 7 §7.3 returns to the idea to explain why total four-momentum cannot be a simple sum over particles.

**Representation:** Hand-drawn arrows along a loop seen by a two-dimensional ant; words rather than equations for the octant; component integrals for the small loop later.

**Strengths:** The flat-control-then-sphere pairing is clean and memorable, and the physics payoff (no invariant sum of momenta) is stated explicitly. Exercises turn one picture into a general law and into the integrability condition.

**Weaknesses:** Framed as a loop rather than as two routes to one point, so 'comparison at a distance' is implicit. The octant is a large loop, and the book itself warns the later small-loop formula does not apply to it, leaving the quantitative link to exercises. The chapter 7 remark is a single paragraph. *(SCH ch06 Fig. 6.2 p.153; SCH ch06 Fig. 6.3 p.153; SCH ch06 §6.4 p.154; SCH ch06 Ex 6.10; SCH ch06 Ex 6.11; SCH ch07 §7.3 p.177)*

### gifted-amateur

**Route:** The sphere loop appears in chapter 11 as a curvature test and is turned into the Riemann tensor. Path dependence proper is used later for its consequences: chapter 12 §12.4 asks how to define the energy of a distant object, which in flat spacetime relies on a family of parallel observers (Fig. 12.4); Example 12.11 shows that in curved spacetime the needed condition becomes Killing's equation, which generic spacetimes violate. Chapter 35 §35.3, after recomputing loop transport with covariant derivatives, poses the tempting plan of laying out a Cartesian grid by transporting a pair of orthogonal vectors and shows it fails because the resulting field is multivalued.

**Representation:** Physical thought experiments (distant energy, grid building), slot-machine tensors, a margin note on summing momenta over a closed surface.

**Strengths:** Ties the geometry directly to physics the learner cares about: why energy conservation in GR is subtle. The grid framing gives a crisp alternative definition of curvature.

**Weaknesses:** Never isolates a two-route experiment; relies on the chapter 11 sphere picture. The Lorentzian feature that the mismatch can be a boost is not discussed. *(GA ch12 Fig. 12.4 p.138; GA ch12 §12.4 p.139; GA ch12 Example 12.11; GA ch35 §35.3 p.369)*

### dinverno

**Route:** In §6.7, after defining the Riemann tensor algebraically from the commutator of covariant derivatives, the book looks for its geometric meaning. It observes that transport from one point to another along two curves generally gives two vectors (Fig. 6.8), defines an integrable connection, and proves a lemma: integrable iff Riemann vanishes. Necessity comes from commuting mixed partials of the transport equation; sufficiency from a second-order Taylor expansion of transport around an infinitesimal loop (Fig. 6.9) followed by deforming one curve into another through thin loops on a simply connected manifold (Fig. 6.10). A second lemma links integrability plus symmetry to affine flatness, and §6.11 gives the metric flatness theorem.

**Representation:** Abstract affine manifold, Taylor expansions, lemma-and-proof structure, schematic figures.

**Strengths:** Precise if-and-only-if statements with the hypotheses (symmetric connection, simple connectedness) spelled out; the two-route framing is explicit and the infinitesimal computation is clean.

**Weaknesses:** No concrete surface, no numbers, no rotation angle; a learner without prior intuition may not see that the 'two different vectors' are physically meaningful. Physical consequences are not drawn here. *(DIV ch06 Fig. 6.8 p.96; DIV ch06 §6.7 p.97; DIV ch06 Fig. 6.9 p.97; DIV ch06 Fig. 6.10 p.98)*

### legacy

**Route:** Chapter 8 opens with a completed demonstration: two arrows leave A, one goes directly to C and one via B, both with the no-twist rule; on a sphere they meet 90 degrees apart, on a plane and a rolled sheet they agree. The lab then notes that one route out and the other back form a loop, so the meeting mismatch equals the loop's return rotation. The guided lesson 'carry a direction home' checks the transport rule on each great-circle arc and warns that a single projection at the end is not transport.

**Representation:** Interactive three.js scene with surface selector (plane, rolled sheet, sphere), triangle-size and radius sliders, angle arc at C drawn in a shared tangent plane; exact rotations verified by scripts.

**Strengths:** Makes the two-route comparison explicit and visual, includes intrinsic-flat controls, and shows the angle depends on angular size rather than radius. Directions are only compared where the arrows share a tangent plane.

**Weaknesses:** Riemannian surfaces only, with no bridge to Lorentzian transport; route shapes are fixed; the physics consequences (adding momenta, global grids) are not connected to the lab. *(legacy:scene-3d-parallel-transport-two-routes; legacy:lesson-carry-a-direction-without-turning-it; legacy:manuscript-chapter-08-curvature-holonomy)*

## Recommended teaching path

1. **Pose the question** — Ask: two arrows are drawn in different cities; what would it mean to say they point the same way, and how would you check? Let the learner propose sliding one arrow to the other. *Why:* The learner's own proposal (slide it over) is exactly parallel transport, so the surprise that follows lands on their idea rather than on a definition. *(SCH ch06 §6.4 p.154; GA ch12 §12.4 p.138)*
2. **Run the flat controls** — Transport an arrow along two different routes on a plane and on a rolled paper cylinder; the arrivals agree every time. *Why:* Establishes that the rule is sound and that bending in space is not the cause, before anything surprising happens. *(SCH ch06 Fig. 6.2 p.153; legacy:scene-3d-parallel-transport-two-routes)*
3. **Show two routes on a sphere** — Send twin arrows from an equator point to a second equator point a quarter-turn away, one along the equator and one over the pole; they meet at right angles. Then join the routes into a loop and show the loop's return rotation is the same 90 degrees. *Why:* Two routes to one point is the cleanest statement of the phenomenon; closing the loop hands off to holonomy. *(DIV ch06 Fig. 6.8 p.96; SCH ch06 Fig. 6.3 p.153; legacy:scene-3d-parallel-transport-two-routes)*
4. **Rule out cheating** — Pause mid-route and verify the arrow is not turning relative to the surface at any step; compare vectors only at a shared point. *Why:* Learners suspect a hidden twist or a numerical artefact; checking the local rule shows the mismatch is geometry. *(legacy:lesson-carry-a-direction-without-turning-it)*
5. **Quantify** — Write the transport equation, then the infinitesimal two-route mismatch as minus Riemann times V and both displacements; on the sphere, state that the mismatch equals enclosed area over radius squared, which for a geodesic triangle is its angular excess. *Why:* Connects the picture to the tensor the learner will compute and gives a number to check against the demo. *(DIV ch06 §6.7 p.97; SCH ch06 Ex 6.10; SCH ch06 §6.5 p.157)*
6. **Check against a trap** — Transport an arrow on the flat plane using polar coordinates: components change along the way, yet two routes deliver identical arrows. *Why:* Separates changing components (a coordinate effect) from genuine path dependence before the learner generalizes wrongly. *(GA ch11 Example 11.7; legacy:manuscript-section-7-5-five-polar-plane-experiments)*
7. **Draw the physics consequences** — Try to build a grid of parallel axes and watch it fail to close; then ask how to add the four-momenta of two particles far apart, and connect to why energy conservation in GR needs a symmetry. *Why:* Shows the idea is not a curiosity of spheres but the reason global conservation laws and global inertial frames are lost. *(GA ch35 §35.3 p.369; SCH ch07 §7.3 p.177; GA ch12 Example 12.11)*

## Analogies

- **Carrying a pointer on a globe without twisting it** (intuition): A walker keeps a pointer fixed relative to the ground at every step. On a globe, different walks to the same place leave the pointer aimed differently; on a floor they never do. *Limits:* The globe is a positive-curvature Riemannian surface seen from outside; spacetime has no outside, can curve differently in different planes, and its mismatch can be a boost. The walker's sense of 'not twisting' must be the intrinsic rule, not a 3D gyroscope held rigid in space (a rigid gyroscope would point at a fixed star, which is not tangent to the surface). *(SCH ch06 §6.4 p.153; legacy:scene-3d-parallel-transport-two-routes)*
- **Laying floor tiles with a carpenter's square** (intuition): You try to tile a region by copying a right-angled frame from tile to tile. On a flat floor the tiles close up; on a curved surface, copying the frame around a block of tiles brings it back turned, so the pattern cannot close consistently. *Limits:* Real tiles are rigid 2D objects that also fail to fit on curved surfaces for metric reasons (distances), not only for transport reasons; the analogy blends the two. In spacetime the frames include a time axis and the misfit can be a boost. *(GA ch35 §35.3 p.369)*
- **Currency exchange by different routes** (working): Convert money from one currency to another directly, or via a third currency. If rates are consistent the result is the same by every route; if not, going around a loop of exchanges changes your holdings. Consistent rates play the role of a flat connection, and the gain around a loop plays the role of curvature. *Limits:* Exchange rates are single numbers that multiply and commute, whereas transport maps are rotation or Lorentz matrices that need not commute. Rates are not tied to any metric or geometry, and there is no notion of an infinitesimal loop whose effect scales with area.
- **Adding arrows drawn on different parts of a globe** (working): To add an arrow drawn in one city to an arrow drawn in another you must first carry one to the other; on a globe the sum depends on how you carry it, just as summing four-momenta at separated events does in curved spacetime. *Limits:* For isolated systems in nearly flat surroundings the ambiguity is tiny and a total energy-momentum can be defined from the far field; the analogy overstates the problem in weak-field situations. *(SCH ch07 §7.3 p.177; GA ch12 §12.4 p.139)*

## Misconceptions

- **You can always say whether an arrow here is parallel to an arrow over there.** — Parallelism is only defined at a single point. Comparing distant arrows requires transporting one to the other, and on a curved space the verdict depends on the route. *Why tempting:* On a table, a map or in everyday space, directions at different places are compared without any thought about routes. *Diagnostic:* Two arrows sit at different points on a sphere. Your friend says 'they are parallel'. What extra information must you ask for before you can agree or disagree? *(SCH ch06 §6.4 p.154)*
- **If the components of a transported vector change along the route, transport must be path dependent (and the space curved).** — Components change whenever the basis changes, as in polar coordinates on a flat plane. Path dependence is about the arrow itself: two routes to the same point giving different arrows. In polar coordinates every route gives the same arrow. *Why tempting:* The transport equation shows Gamma terms changing the components, and Gammas look like 'gravity' or 'curvature'. *Diagnostic:* In polar coordinates on a flat sheet you carry an arrow once around a circle centred on the origin. Its r and theta components change along the way. When you return, is it a different arrow? *(GA ch11 §11.3 p.124; legacy:manuscript-section-7-5-five-polar-plane-experiments)*
- **Any bent surface, such as a cylinder, shows path-dependent transport.** — A cylinder is extrinsically bent but intrinsically flat: unroll it and transport becomes ordinary sliding on a plane, so every route between two points agrees, even routes that wrap around the tube a different number of times (on the unrolled sheet those are just translated copies). *Why tempting:* The arrow visibly changes direction in the room as it moves around the cylinder. *Diagnostic:* An arrow is carried around a paper tube along one route and along another route to the same point. Before you look: will they agree? What would you do to the paper to convince yourself? *(SCH ch06 Ex 6.30; legacy:scene-3d-parallel-transport-loop)*
- **Parallel transporting a pair of perpendicular axes everywhere builds a consistent Cartesian grid.** — Transport keeps the axes perpendicular along each curve, but different routes to the same point deliver differently oriented axes, so the 'grid' is multivalued in a curved region. *Why tempting:* Orthogonality is preserved at every step, which seems to be all a grid needs. *Diagnostic:* You transport an orthonormal pair from P along meridians and then along latitude lines to fill a patch of a globe. A friend fills the same patch going along latitude lines first. Will your two grids agree at the far corner? *(GA ch35 §35.3 p.369)*
- **The total four-momentum of a system in curved spacetime is the sum of its particles' four-momenta.** — Each four-momentum lives in the tangent space at its own event. Adding them needs transport to a common point, and the result depends on the routes, so there is no invariant sum; conserved totals exist only with a symmetry or for isolated systems in asymptotically flat spacetime. *Why tempting:* It is exactly how total momentum works in Newtonian mechanics and special relativity. *Diagnostic:* Two stars orbit a black hole on opposite sides. Describe step by step how you would compute their 'total momentum', and point to the step where a choice sneaks in. *(SCH ch07 §7.3 p.177; GA ch12 §12.4 p.139)*
- **The arrows disagree because the rule quietly turns the arrow, or because of numerical error.** — At every step the arrow is kept as parallel as the surface allows; checking the local rule anywhere along the route finds no turning. The disagreement is produced by the geometry enclosed between the routes and grows with its area. *Why tempting:* A global rotation seems to need a local cause, so learners look for a hidden twist. *Diagnostic:* If the mismatch were numerical error, how would it change when you halve the step size? If it is geometry, how should it change when you halve the area between the routes? *(legacy:lesson-carry-a-direction-without-turning-it)*
- **When two flows applied in different orders end at different points, that is curvature.** — An endpoint mismatch between flows is measured by the Lie bracket and happens in flat space. Path dependence compares directions of arrows at the same endpoint. *Why tempting:* Both involve 'doing A then B versus B then A' and a small second-order gap. *Diagnostic:* On a flat sheet, following field X then field Y lands you at a different point than Y then X. Does this show the sheet is curved? What would you need to measure instead? *(legacy:lab-flow-order-lie-bracket)*

## Thought experiments

- **Two walkers, one meeting point**: Two walkers with identical pointers leave the same equator point on a globe; one follows the equator a quarter of the way around, the other goes via the north pole to the same destination. Both obey the no-twist rule. *Lesson:* At the meeting point the pointers are at right angles. The enclosed octant has area one eighth of the sphere, and the mismatch equals that area over the radius squared. *(SCH ch06 Fig. 6.3 p.153; DIV ch06 Fig. 6.8 p.96)*
- **The energy of a faraway star**: An astronomer wants the energy of a distant star, but energy is only defined relative to an observer at the star. She imagines a stand-in observer there moving 'with the same velocity' as herself. *Lesson:* In flat spacetime 'same velocity' is unambiguous; in curved spacetime it depends on the transport route, so distant energies and global energy conservation need extra structure (a Killing symmetry). *(GA ch12 §12.4 p.138; GA ch12 Example 12.11)*
- **Building a grid by transport**: Start with two perpendicular unit vectors at a point and try to extend them to a grid of axes covering a region by transporting them everywhere. *Lesson:* The construction is multivalued in curved space; its failure is another definition of curvature. *(GA ch35 §35.3 p.369)*

## Visualizations

### Two routes, one meeting point · interactive-3d · high priority

Twin arrows start together and are transported along two learner-drawn routes to a common endpoint on a chosen surface; the angle between them at arrival is compared with the enclosed area times the Gaussian curvature.

**Interaction:** Choose plane, rolled cylinder, sphere or saddle. Drag the endpoint and a waypoint on each route; scrub a progress slider. Readouts show the arrival mismatch angle, enclosed area, K times area, and (for geodesic routes) the angle excess. A button swaps which route is 'first' to flip the sign; a radius slider shows the angle depends on angular size only.

**Model:** Intrinsic transport integrated with RK4 from dV/ds = -Gamma V dx/ds in surface coordinates (sphere: theta, phi; saddle: a hyperbolic-plane patch); great-circle segments use exact rotations as a check. Mismatch computed in the shared tangent plane at the endpoint; enclosed area from the metric area element.

**Inspired by:** DIV ch06 Fig. 6.8 p.96; SCH ch06 Fig. 6.3 p.153; SCH ch06 Fig. 6.2 p.153

**Legacy assets:** scene-3d-parallel-transport-two-routes, scene-3d-parallel-transport-loop

### Try to build a grid · interactive-3d · medium priority

The learner places an orthonormal frame at a corner of a patch and fills the patch with frames by transport along two different sweeping orders; wherever the two fillings disagree the frames are drawn doubled with a coloured misfit wedge.

**Interaction:** Pick sweep order (meridians first or parallels first), patch size and latitude on a globe; toggle a flat sheet. The misfit angle at the far corner is plotted against patch area to show linear growth.

**Model:** Levi-Civita transport on the unit sphere in (theta, phi); along latitude lines the frame angle obeys d(psi) = -cos(theta) d(phi); along meridians it is constant. Misfit equals the integral of sin(theta) dtheta dphi over the patch.

**Inspired by:** GA ch35 §35.3 p.369

**Legacy assets:** figure-cartan-comparison

### Adding momenta that live apart · interactive-2d · medium priority

A spatial analogue of summing four-momenta: arrows attached to several points on a curved surface are each transported to a base point along routes the learner picks, and their vector sum is displayed. Changing a route changes the total; on a flat sheet it never does.

**Interaction:** Drag the base point, redraw any route, toggle curvature strength (sphere radius) and flat mode; the total arrow and its spread over a set of random routes update live.

**Model:** Same intrinsic transport integrator; sum formed in the base-point tangent plane. Caption states that this is a Riemannian surface standing in for spacetime.

**Inspired by:** SCH ch07 §7.3 p.177; GA ch12 Fig. 12.4 p.138

### Components change, the arrow does not · interactive-2d · medium priority

On a flat plane drawn with a polar grid, an arrow is transported along two routes; its polar components are plotted along each route and differ in between, but coincide on arrival. A second tab repeats the experiment on a sphere patch where arrivals differ.

**Interaction:** Drag start, end and route waypoints; toggle Cartesian versus polar component readouts; switch plane or sphere.

**Model:** Polar-plane Christoffel symbols Gamma^r_{theta theta} = -r, Gamma^theta_{r theta} = 1/r in the transport ODE, with Cartesian components shown constant as an independent check.

**Inspired by:** GA ch11 Example 11.7

**Legacy assets:** manuscript-section-7-5-five-polar-plane-experiments

## Worked examples

- **Octant triangle on the sphere** (intuition): Step-by-step reasoning that an arrow kept perpendicular, then tangent, then perpendicular to three quarter-great-circles returns rotated by 90 degrees. *(SCH ch06 §6.4 p.153)*
- **Exact octant transport with tangent projection** (working): Verifies the transport rule on each great-circle arc with explicit unit vectors and shows the right-angle return equals area over radius squared; warns that one projection at the end is not transport. *(legacy:lesson-carry-a-direction-without-turning-it)*
- **Two infinitesimal routes and the integrability lemma** (formal): Second-order Taylor expansion of transport along both edge orders of a tiny parallelogram gives a difference equal to minus Riemann times the vector and both edges; deforming curves through thin loops extends this to finite paths on simply connected manifolds. *(DIV ch06 §6.7 p.97)*
- **Energy conservation needs parallel observers** (formal): Repeating the flat-space energy-current argument with covariant derivatives turns the requirement on the observer field into Killing's equation, which generic spacetimes do not satisfy. *(GA ch12 Example 12.11)*
- **The grid illusion** (working): Argues from loop holonomy that a field obtained by transporting a vector everywhere is multivalued, so no global Cartesian grid exists. *(GA ch35 §35.3 p.369)*

## Exercises

- (standard) Show that the rotation of a vector transported around any great-circle triangle equals the triangle's angular excess. *Skill:* Linking route mismatch to spherical geometry *(SCH ch06 Ex 6.10)*
- (standard) Derive the condition for a vector field to be parallel everywhere from equality of mixed partial derivatives and rewrite it in terms of the Riemann tensor. *Skill:* Integrability conditions *(SCH ch06 Ex 6.11)*
- (intro) Compute the Riemann tensor of a cylinder and confirm it vanishes. *Skill:* Separating extrinsic bending from intrinsic curvature *(SCH ch06 Ex 6.30)*
- (standard) Prove that an affine-flat manifold has a connection that is both integrable and symmetric. *Skill:* Formal link between flatness and path independence *(DIV ch06 Ex 6.12)*
- (standard) Show that the metric of a rotating reference frame is flat, despite its fictitious-force Christoffel symbols. *Skill:* Distinguishing coordinate effects from curvature *(GA ch11 Ex 11.4)*
- (intro) Track a constant Cartesian vector in polar components and show that the Christoffel terms exactly cancel the basis change. *Skill:* Components versus arrows *(legacy:practice-set-appendix-a-thirty-exercises)*

## Checks for understanding

- **Q (intuition):** On a paper tube (a cylinder), you carry an arrow from point P to point Q along two different routes that do not wrap around the tube. Do the arrows agree at Q? Explain without equations.
  - **A:** Yes. Cut the tube along a line and unroll it flat without stretching; the no-twist rule becomes ordinary sliding on a flat sheet, where every route gives the same arrow. The tube is bent in space but not curved from the inside. *(targets: Any bent surface, such as a cylinder, shows path-dependent transport.)*
- **Q (working):** On a sphere of radius a, point A is on the equator at longitude 0 and C is on the equator at longitude 90 degrees east. Arrow 1 goes from A to C along the equator; arrow 2 goes from A up to the north pole and down the 90-degree meridian to C. Both start pointing east. How do they differ at C, and how does this match the area rule?
  - **A:** Arrow 1 slides along the equator staying tangent to it, so it arrives pointing east. Arrow 2 stays perpendicular to the first meridian (pointing east, which is tangent to the second meridian at the pole), then stays tangent to the second meridian and arrives pointing south. They differ by 90 degrees. The two routes enclose one octant, area 4 pi a^2 / 8 = pi a^2 / 2; divided by a^2 this is pi/2, a right angle, as observed.
- **Q (working):** In polar coordinates on a flat plane, an arrow carried along a circle about the origin has components V^r and V^theta that change continuously. A classmate concludes the plane is curved. What do you tell them, and what test would settle it?
  - **A:** Changing components reflect the rotating polar basis, not a change in the arrow; in Cartesian components the transported arrow is constant. The decisive test compares arrows (not components) delivered by two routes to the same point, or computes the Riemann tensor, which for the polar plane is zero because the derivative and product terms cancel. *(targets: If the components of a transported vector change along the route, transport must be path dependent (and the space curved).)*
- **Q (formal):** A cone made by removing a wedge from paper and gluing the edges is flat everywhere except at its tip. Is parallel transport on the cone (with the tip removed) path independent?
  - **A:** Only for routes that can be deformed into each other without crossing the tip. Two routes passing on opposite sides of the tip deliver arrows rotated relative to each other by the deficit angle (the angle of the removed wedge). Zero curvature guarantees path independence only on a simply connected region; the tip is where the missing curvature is concentrated.
- **Q (formal):** Why can you not define the total four-momentum of a galaxy in curved spacetime by adding the four-momenta of its stars, and when does an approximate total still make sense?
  - **A:** Each star's four-momentum is a vector in the tangent space at its own event; adding requires transporting them to one point, and in curved spacetime the result depends on the routes, so there is no invariant sum. A useful total exists when the spacetime has a symmetry (a Killing vector gives a conserved quantity) or for an isolated system viewed from the nearly flat region far away, where route ambiguities become negligible. *(targets: The total four-momentum of a system in curved spacetime is the sum of its particles' four-momenta.)*

## Applications

- **Energy and momentum conservation in GR**: Because vectors at separated events have no canonical comparison, local conservation of stress-energy does not integrate to a global conservation law for matter unless the spacetime has a Killing symmetry; this underlies the subtleties of energy in cosmology and of gravitational energy. *(GA ch12 Example 12.11; SCH ch07 §7.3 p.177)*
- **No global inertial frames**: A global inertial frame would need a grid of parallel axes; path dependence forbids it in a curved region, which is why GR works with local inertial frames only. *(GA ch35 §35.3 p.369)*

## Tutor guidance

**Opening questions**

- If I draw an arrow in London and another in Tokyo, what would it mean to say they point the same way?
- How would an ant living on a surface, unable to see outside it, carry a direction from one place to another?
- Do you expect carrying an arrow along two different roads to the same place to matter? Why or why not?

**Common questions**

- *Isn't the arrow just turning because the surface curves away underneath it?* — On a cylinder the surface curves away too, yet routes agree. What matters is curvature you can detect from inside the surface. At each step the arrow is kept as parallel as possible; the disagreement only appears when you compare two whole routes.
- *Which route gives the 'right' answer?* — Neither. Each route gives a perfectly good transported vector; there is simply no route-independent meaning of 'the same vector' at a distant point when curvature is present.
- *Does this mean physics in curved spacetime is ambiguous?* — Local physics is not: all measurements compare quantities at one event. The ambiguity affects only comparisons or sums across separated events, which is why GR phrases laws locally.
- *How big is this effect on Earth's surface for everyday routes?* — The mismatch equals enclosed area divided by Earth's radius squared. Two routes enclosing a 1 km by 1 km square give about 1 divided by 6371 squared, roughly 2.5 times ten to the minus eight radians: utterly negligible, which is why we never notice.
- *In spacetime, is the mismatch always a rotation?* — No. Transport preserves the spacetime inner product, so the mismatch is a Lorentz transformation: it can rotate spatial directions, boost (mix time and space), or both, depending on the plane the routes enclose.

**Pitfalls when explaining**

- Do not compare vectors at different points while explaining path dependence; always bring both arrows to a shared point first.
- Do not use a rigid 3D gyroscope as the 'no twist' rule on a surface; it would leave the tangent plane.
- Do not let changing components stand in for path dependence; use the arrow or an orthonormal frame.
- Avoid saying the loop formula applies to the octant; the octant result comes from the exact area law on a sphere, not from the small-loop expansion.
- Say 'curved from the inside' (intrinsic) explicitly, so the cylinder does not become a counterexample in the learner's mind.
- When a demo carries arrows on a surface drawn in 3D, the exact rule is to remove only the part of the change along the normal, dV/ds = -(V . dn/ds) n. Snapping the arrow back into the tangent plane and rescaling it at each step only approximates this, so do not present that shortcut as transport (legacy pitfall 16).

**When to show a demo**

- Before revealing the sphere result, ask the learner to predict the mismatch for the rolled cylinder, then run it.
- After the 90-degree sphere result, halve the triangle's angular size and ask for a prediction (a quarter of the area, so a quarter of the angle for similar shapes), then show it.
- Change the sphere's radius with the angular triangle fixed and ask whether the angle changes; it does not.
- In the grid demo, let the learner choose both sweep orders and discover the misfit wedge themselves.

**Saying it aloud:** Say the transport equation as: the rate of change of the vector's components along the curve, plus the connection times the curve's direction times the vector, equals zero. Say the two-route mismatch as: the difference between the two arrivals is minus the Riemann tensor fed the vector and the two small steps. Say 'delta alpha equals A over a squared' as: the mismatch angle is the enclosed area divided by the square of the sphere's radius. Never read index letters aloud; name their roles instead.

## Sources

- schutz ch06 (core): p.153 §6.4, p.154 §6.4
- schutz ch07 (revisited): p.177 §7.3
- gifted-amateur ch12 (revisited): p.138 §12.4, p.139 §12.4
- gifted-amateur ch35 (introduced): p.369 §35.3
- dinverno ch06 (developed): p.96 §6.7, p.97 §6.7, p.98 §6.7
- legacy scene-3d-parallel-transport-two-routes (core)
- legacy lesson-carry-a-direction-without-turning-it (developed)

## Review

**Verdict:** fixed

**Fixes**

- Working level now says which arrival is subtracted from which in the two-route formula. The sign was checked against d'Inverno's §6.7 derivation, which takes the delta-x-first route minus the Delta-x-first route, and confirmed independently with normal coordinates and Stokes' theorem.
- Removed the claim that the sphere area law needs geodesic routes. Any two routes that bound a region of area A give a rotation of A/a^2; only the angular-excess form needs geodesic sides.
- Removed riemann-curvature-tensor from the working level's 'assumes' list, since the Riemann note lists this concept as a prerequisite. The text now introduces Riemann as the coefficient that is developed next, so the dependency order stays acyclic.
- Added an explaining pitfall based on legacy pitfall 16: the exact rule for transport on an embedded surface, and a warning that projecting and renormalizing at each step only approximates it.

**Concerns**

- Registry entry still omits DIV ch06 and the two legacy assets that the note cites; sync the registry.
- The currency-exchange analogy and the everyday numbers have no book source; they are standard, and the arithmetic has been checked (1 km^2 over Earth's radius squared is 2.5e-8 rad).
