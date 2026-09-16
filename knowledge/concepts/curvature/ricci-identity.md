---
type: "concept"
schema_version: 2
id: "ricci-identity"
title: "Ricci identity"
tagline: "Why the order of two changes matters for arrows on a curved surface"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["commutator of covariant derivatives"]
prerequisites: ["riemann-curvature-tensor", "second-covariant-derivative"]
leads_to: ["geodesic-deviation-equation", "raychaudhuri-equation", "integrability-condition-for-parallel-fields", "killing-vector-ricci-identity", "gauss-codazzi-equations", "cyclic-identity", "bianchi-identity"]
visuals: ["carry-the-far-arrow-home-two-ways", "cross-off-matching-terms", "falling-ring-of-crumbs"]
---

# Ricci identity

*Why the order of two changes matters for arrows on a curved surface*

`ricci-identity` · curvature · core · physics-reviewed (revision 7)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[second-covariant-derivative]] (working)  
**Opens:** [[geodesic-deviation-equation]] · [[raychaudhuri-equation]] · [[integrability-condition-for-parallel-fields]] · [[killing-vector-ricci-identity]] · [[gauss-codazzi-equations]] · [[cyclic-identity]] · [[bianchi-identity]]  
**Related:** [[riemann-curvature-operator]] · [[holonomy]] · [[torsion-tensor]] · [[gauge-field-strength]] · [[minimal-coupling]]  
**Visuals:** ★ [[carry-the-far-arrow-home-two-ways]] · [[cross-off-matching-terms]] · [[falling-ring-of-crumbs]]

> Around a tiny square, you can find how something changes along one side, and how that change differs on the opposite side. You can begin with either pair of opposite sides, and those two choices are the two orders. For heights of the ground, the two orders agree. For arrows painted on a ball, they differ by the turn an arrow comes back with after one trip around the square: that is the Ricci identity.

## You will be able to

**Entry**
- Show with arithmetic that, for numbers at the corners of a square, the change of a change comes out the same in either order. `objectives/explain-order-for-numbers` ← `checks/heights-at-four-corners`
- Predict how the two orders differ for arrows painted on a ball or on a flat floor, and explain why the painting does not matter. `objectives/predict-two-orders-for-arrows` ← `checks/painted-ball-two-orders`, `checks/two-paintings-one-square`, `problems/ten-kilometre-square`

**Working**
- Derive the Ricci identity for a vector field from the second covariant derivative, naming each group of terms that cancels. `objectives/derive-the-identity` ← `checks/inertial-frame-claim`, `problems/fields-that-agree-at-a-point`
- Use the one-term-per-index rule, with its signs, on covectors and on the metric. `objectives/use-one-term-per-index` ← `checks/covector-sign`, `checks/metric-commutator`
- Explain where swapping derivative order enters tidal drift, and estimate the relative acceleration a pair of falling test masses shows. `objectives/explain-tidal-drift` ← `problems/gradiometer-in-orbit`

**Formal**
- Distinguish the curvature term from the bracket and torsion terms in commutators along arbitrary vector fields. `objectives/separate-bracket-and-torsion` ← `checks/polar-frame-bracket`, `problems/operator-from-components`
- Use the identity as an integrability condition to decide whether a parallel vector field can exist. `objectives/apply-integrability` ← `checks/no-parallel-field-on-a-sphere`

## Ways in

### 1. Two orders for heights on a hillside · entry · contrast

*When you compare a change on one side of a square with the change on the opposite side, does it matter which pair of sides you start with?*

Picture a square field on a gentle hillside, 100 metres along each side. Stand at one corner, facing along one side, with the field on your left. Call your corner the start. Call the corner in front of you the corner ahead. The side on your left ends at the corner on your left. The remaining corner is the far corner.

A surveyor measures the height of the ground at each corner, above the foot of the hill. It is 10 metres at the start, 13 metres at the corner ahead, 11 metres at the corner on your left, and 16 metres at the far corner.

Two sides of the field run the way you face, so a change along either is a change going ahead. The other two run to your left, so a change along either is a change going left.

Start with the changes going ahead. From the start to the corner ahead, the height rises by 3 metres. On the opposite side, from the corner on your left to the far corner, it rises by 5 metres. The second change minus the first is 2 metres. This difference is called a change of a change: how much a change going ahead differs between the two sides.

Now use the other order: start with the changes going left. From the start to the corner on your left, the height rises by 1 metre. On the opposite side, from the corner ahead to the far corner, it rises by 3 metres. The second change minus the first is again 2 metres.

This is no accident. Going ahead first, you worked out 16 minus 11, and then took away 13 minus 10. Taking away 13 minus 10 is the same as taking away 13 and adding 10. The answer is therefore 16 plus 10, minus 13, minus 11: the far corner plus the start, minus the other two corners.

Going left first, you worked out 16 minus 13, and then took away 11 minus 10: the same four heights with the same signs. So for any numbers laid out on the ground, like heights or temperatures, the order never matters.

**Try it:** Draw a square and label its corners start, ahead, left and far, as in the field. Write any four whole numbers at the corners. Work out far minus left, then ahead minus start, and subtract the second answer from the first. Next work out far minus ahead, then left minus start, and subtract again. You should get the same number both times, whatever numbers you chose.

**Takeaway:** For numbers at the corners of a square, the change of a change comes out the same in either order. Both orders come to the far corner plus the start, minus the other two corners.

*Picture:* A square field with a height written at each corner. Two chains of subtractions, one starting with the changes going ahead and one with the changes going left, end at the same number.

*See:* `checks/heights-at-four-corners`

### 2. Arrows painted on a ball · entry · picture

*What happens to the two orders when the corners hold arrows on a ball?*

**Recap:** The arrow test: press a cardboard arrow against the ground and carry it around a loop, a path that ends where it began. Never let it swing left or right. On a flat floor it comes back matching its start. On a ball, walk a small loop so that the piece of ball it goes round stays on your left; the arrow comes back turned a little toward your left. The hillside field: stand at one corner, the start, facing along one side with the field on your left. The corner in front of you is the corner ahead. The side on your left ends at the corner on your left. The last is the far corner. For heights at the corners, a change of a change comes out the same in either order.

As in the hillside field, stand at one corner of a tiny square on a huge round ball, facing along one side, with the square on your left. Name the corners the same way.

Paint an arrow on the ground at each corner. Any painting will do, as long as it is smooth: neighbouring arrows point nearly the same way.

How much does the arrow change from one corner to a neighbouring corner? Take them in order, a first and a second. Unlike a flat room, a ball offers no wall to measure arrows against, because the ground faces a different way at every spot. Instead, lay a cardboard copy on the second corner's painted arrow, matching it. Carry the copy along the side to the first corner, never letting it swing. Then measure the angle from the first corner's painted arrow to the copy. That angle is the change from the first corner to the second.

Give that angle a sign. Stand at the first corner, facing along its painted arrow. If you must turn left to face along the copy, the angle counts as positive; if you must turn right, it counts as negative.

Now repeat the hillside steps with these angles. First order: the change from the corner on your left to the far corner, minus the change from the start to the corner ahead. Second order: the change from the corner ahead to the far corner, minus the change from the start to the corner on your left. Each change is an angle, just a number, so you can subtract two of them without carrying anything.

On a flat floor, give every painted arrow a number: its angle from one chosen wall. A carried copy keeps its angle to that wall. Each change is then the second corner's number minus the first corner's number, just like a change in height, so the two orders agree.

On the ball the two orders differ. Walk once around the square, ahead first, turning left at each corner, so the square stays on your left. The first order minus the second equals the turn an arrow comes back with from that trip. That turn is a little toward your left, so the difference is positive.

Here is why. Write out the first order minus the second, and regroup the four changes into one sum minus another, as with the heights. The first sum follows the route through the corner on your left: the change from the start to that corner, plus the change from there to the far corner. The second sum follows the route through the corner ahead in the same way.

Take the route through the corner on your left. At that corner, the second angle of the sum is measured from its painted arrow to a copy of the far arrow. Tape that copy to a copy of the painted arrow, and carry both home to the start. Neither arrow swings, so the angle between them stays the same. The painted arrow's copy arrives at the first angle of the sum from the start's arrow. So the far copy arrives at the two angles added together.

Each sum is therefore the angle from the start's arrow to a copy of the far arrow, carried home by one of two routes. Now take the copy that came home through the corner ahead. Carry it back out along that same route: walking a route backwards plays the carrying backwards, so it matches the far arrow again. Then carry it home through the corner on your left, and it matches the other copy.

Altogether that copy went once around the square, ahead first. So the two copies differ by the loop's turn, and so do the two orders.

No painted arrow matters for this. The start's arrow is the reference for both sums, so it cancels. A loop on a ball turns every arrow by the same amount, whichever way it points, so the far arrow's direction does not matter either. This rule is called the Ricci identity.

On Earth, ignoring hills, a square covering one square kilometre gives a turn of about 1.4 millionths of a degree. That is the angle across a hair's width seen from 3 kilometres away. So the difference caused by Earth's roundness alone is far too small to notice.

**Takeaway:** For arrows on a ball, the two orders differ by exactly the turn of the tiny loop, whatever smooth pattern the arrows are painted in; on a flat floor they agree.

*What this leaves out:* The rule holds exactly whenever neighbouring painted arrows point nearly the same way, so that no angle comes near half a turn. On a ball, a tiny square cannot have both four exact right angles and sides walked without steering. The reasoning works for any four-sided loop, so this does not matter. The Ricci identity itself is the rule's limit as the square shrinks to a point. There the changes become rates of change.

*Continues:* `ways_in/changes-of-changes-for-numbers`<br>*Builds on:* [[riemann-curvature-tensor]], [[path-dependence-of-parallel-transport]]<br>*Visuals:* [[carry-the-far-arrow-home-two-ways]]<br>*See:* `checks/painted-ball-two-orders`, `checks/two-paintings-one-square`

### 3. Both orders in components · working · calculation

*What does the rule of two orders become for a vector field in coordinates, and why does no derivative of the field survive?*

In "Arrows painted on a ball", the two orders of taking changes differed by the turn of a loop around a tiny square, and the painted pattern dropped out. Shrink the square and divide each change by the lengths of its sides, and the changes become rates of change. For a vector field $V$, the change along a coordinate direction is the covariant derivative $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\lambda}V^\lambda$, which compares neighbouring vectors after carrying one to the other. Its change along a second direction is the second covariant derivative, the components of $\nabla(\nabla V)$, with the rightmost derivative acting first. Because $\nabla_\nu V^\rho$ has a lower index, it carries a correction for that index too:

$$\nabla_\mu\nabla_\nu V^\rho = \partial_\mu(\nabla_\nu V^\rho) + \Gamma^\rho{}_{\mu\lambda}\nabla_\nu V^\lambda - \Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho.$$

For a torsion-free connection, swapping the order and subtracting gives the Ricci identity,

$$[\nabla_\mu,\nabla_\nu]V^\rho \equiv \nabla_\mu\nabla_\nu V^\rho - \nabla_\nu\nabla_\mu V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma.$$

The derivation "Expand both orders and cancel" goes one move at a time. Three groups cancel: the second partial derivatives of $V$, which commute; the terms with one $\Gamma$ and one first derivative of $V$, which pair up symmetrically; and the index correction, because $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$. What survives is the course Riemann tensor acting on $V$.

Each slot has a job: $\mu$ and $\nu$ are the two directions, the sides of the tiny square; $\sigma$ takes the vector; $\rho$ is the component of the result. No derivative of $V$ survives, so two fields that agree at a point give the same commutator there, just as the painting dropped out on the ball. This also proves again that $R^\rho{}_{\sigma\mu\nu}$ is a tensor, since the left side is a tensor for every $V$.

The sign agrees with the small-loop law. For a small cell with edges $a$ and $b$, $\nabla_\mu\nabla_\nu V$ uses the far corner's vector carried home along $-b$ and then $-a$, and the other order carries it along $-a$ and then $-b$. The first copy minus the second is minus the change $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ from walking $+a, +b, -a, -b$, so $[\nabla_\mu,\nabla_\nu]V^\rho\,a^\mu b^\nu \approx R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$. The first order in "Arrows painted on a ball" took the changes along $a$ first, so it is $\nabla_\nu\nabla_\mu V$, and its difference from the second order, $[\nabla_\nu,\nabla_\mu]V^\rho a^\mu b^\nu$, is the loop's own change $\Delta V^\rho$.

Contracting $\rho$ with $\mu$ gives $\nabla_\mu\nabla_\nu V^\mu - \nabla_\nu\nabla_\mu V^\mu = R_{\sigma\nu}V^\sigma$, the form that brings the Ricci tensor into the focusing of free-fall paths.

**Takeaway:** Swapping two covariant derivatives on a vector field leaves only the Riemann tensor acting on the vector, because every term with a derivative of the field cancels.

*What this leaves out:* Torsion-free connection, coordinate basis, and a field with continuous second derivatives; the small-loop comparison holds to leading order in the cell size.

*Continues:* `ways_in/arrows-painted-on-a-ball`<br>*Builds on:* [[second-covariant-derivative]], [[riemann-curvature-tensor]], [[christoffel-symbols]]<br>*Visuals:* [[cross-off-matching-terms]]<br>*See:* `derivations/expand-both-orders`, `worked_examples/both-orders-on-the-sphere`, `holonomy/key_equations/small-loop-law`

### 4. One curvature term per index · working · calculation

*How does swapping the order act on scalars, covectors and tensors with several indices?*

The heights in "Two orders for heights on a hillside" did not care about order, and neither does a scalar field $f$. Its second covariant derivative is $\nabla_\mu\nabla_\nu f = \partial_\mu\partial_\nu f - \Gamma^\lambda{}_{\mu\nu}\partial_\lambda f$, which is symmetric in $\mu\nu$ for a torsion-free connection, so $[\nabla_\mu,\nabla_\nu]f = 0$.

That forces a covector to take the opposite sign. Apply the commutator to the scalar $\omega_\rho V^\rho$ with the product rule. The cross terms $(\nabla_\mu\omega_\rho)(\nabla_\nu V^\rho)$ and $(\nabla_\nu\omega_\rho)(\nabla_\mu V^\rho)$ cancel in the swap, leaving $\big([\nabla_\mu,\nabla_\nu]\omega_\rho\big)V^\rho + \omega_\sigma R^\sigma{}_{\rho\mu\nu}V^\rho = 0$ for every $V$. Hence

$$[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\,\omega_\sigma.$$

A tensor with several indices gets one such term per index, with a plus sign for each upper index and a minus sign for each lower one:

$$[\nabla_\mu,\nabla_\nu]S^\alpha{}_\beta = R^\alpha{}_{\lambda\mu\nu}S^\lambda{}_\beta - R^\lambda{}_{\beta\mu\nu}S^\alpha{}_\lambda.$$

The commutator therefore behaves like a product rule with no derivatives left over: it passes through products and contractions one index at a time, and at each point it acts only on the values of the tensor there.

**Takeaway:** Swapping the order does nothing to a scalar, adds a Riemann term for each upper index, and subtracts one for each lower index.

*What this leaves out:* Torsion-free connection.

*Continues:* `ways_in/changes-of-changes-for-numbers`, `ways_in/both-orders-in-components`<br>*Builds on:* [[second-covariant-derivative]], [[covariant-derivative-of-a-one-form]]<br>*See:* `derivations/one-term-per-index`, `checks/covector-sign`

### 5. Tidal drift is a swap of order · working · operational

*How does a pair of freely falling test masses measure the effect of swapping derivative order?*

The commutator of "Both orders in components" is what two neighbouring freely falling masses feel. Label a family of free-fall worldlines $x^\mu(\tau, s)$ by proper time $\tau$ along each one and a label $s$ across them. The four-velocity is $u^\mu = \partial x^\mu/\partial\tau$, the separation vector is $\xi^\mu = \partial x^\mu/\partial s$, and the relative acceleration of two neighbours is $D^2\xi^\mu/d\tau^2$, two covariant derivatives along $u$.

Two facts do the work. Mixed partial derivatives of $x^\mu$ commute and the connection is symmetric, so $u^\alpha\nabla_\alpha\xi^\mu = \xi^\alpha\nabla_\alpha u^\mu$. Free fall means $u^\alpha\nabla_\alpha u^\mu = 0$ on every worldline. The derivation "Tidal drift from swapping order" uses them to turn $D^2\xi^\mu/d\tau^2$ into $u^\alpha\xi^\beta[\nabla_\alpha,\nabla_\beta]u^\mu$, and the Ricci identity turns that into curvature:

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,$$

the geodesic deviation equation in course form.

An accelerometer riding on one mass reads zero in free fall, so one accelerometer alone cannot measure this relative acceleration. A gravity gradiometer therefore measures each of two falling masses against one reference that both share, and subtracts the two readings. A translation of that shared reference, such as vibration of its mounting, enters both readings alike and cancels in the difference. What is left is the relative acceleration of the two masses, quoted per unit separation. A rotation of the reference does not cancel, so its rotation rate has to be controlled, or else measured and removed. For slowly moving masses near a static spherical mass $M$, the vertical entry is $-c^2R^z{}_{0z0} = 2GM/r^3$. At Earth's surface that is $3.08\times10^{-6}\ \mathrm{s^{-2}}$: two masses 1 m apart along the vertical separate with a relative acceleration of 3.1 micrometres per second squared.

**Takeaway:** The relative acceleration of neighbouring free-fall worldlines is a swap of derivative order in disguise, so a gradiometer reads the Riemann tensor through the Ricci identity.

*What this leaves out:* Separations small compared with the distance over which the curvature changes; the numbers treat Earth as a static sphere.

*Continues:* `ways_in/both-orders-in-components`<br>*Builds on:* [[geodesic]], [[tidal-force]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/tidal-drift-from-swapping-order`, `observations/atom-gravity-gradiometer`, `problems/gradiometer-in-orbit`

### 6. Commutators, brackets and torsion · formal · structure

*What is the exact statement for any connection and any vector fields, and what follows from it?*

The component identity of "Both orders in components" and the sign rule of "One curvature term per index" are shadows of one operator statement. Let $\nabla$ be an affine connection on a smooth manifold $M$, with torsion $\mathrm{Tor}(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$ and curvature operator

$$\mathcal{R}(X,Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]},$$

whose coordinate components are the course $R^\rho{}_{\sigma\mu\nu}$. The second covariant derivative of a tensor field $S$ is $\nabla^2_{X,Y}S = \nabla_X\nabla_YS - \nabla_{\nabla_XY}S$; its components are $\nabla_\mu\nabla_\nu S$ for $X = \partial_\mu$, $Y = \partial_\nu$.

*Ricci identity.* For all vector fields $X, Y$ and tensor fields $S$,

$$\nabla^2_{X,Y}S - \nabla^2_{Y,X}S = \mathcal{R}(X,Y)S - \nabla_{\mathrm{Tor}(X,Y)}S.$$

*Proof sketch.* The left side is $[\nabla_X,\nabla_Y]S - \nabla_{\nabla_XY - \nabla_YX}S$, and $\nabla_XY - \nabla_YX = [X,Y] + \mathrm{Tor}(X,Y)$. Each $\nabla_X$ is a derivation of the tensor algebra that commutes with contractions, so $\mathcal{R}(X,Y)$ is one too, and it annihilates functions because $X(Yf) - Y(Xf) = [X,Y]f$. Such a derivation is fixed by its action on vectors. For a covector $\omega$, applying it to the function $\omega(V)$ gives $0 = (\mathcal{R}(X,Y)\omega)(V) + \omega(\mathcal{R}(X,Y)V)$, which forces $-R^\sigma{}_{\rho\mu\nu}$ on each covector index. With $\mathrm{Tor}^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu}$, every component commutator gains $-\mathrm{Tor}^\lambda{}_{\mu\nu}\nabla_\lambda S$, even on scalars. In semicolon notation, torsion-free, $V^\rho{}_{;\nu\mu} - V^\rho{}_{;\mu\nu} = R^\rho{}_{\sigma\mu\nu}V^\sigma$.

*Frames.* For a non-coordinate frame $e_a$, the operator $\nabla_{e_a}\nabla_{e_b} - \nabla_{e_b}\nabla_{e_a}$ exceeds $\mathcal{R}(e_a,e_b)$ by $\nabla_{[e_a,e_b]}$, so a nonzero value does not by itself signal curvature. The frame components of the tensor $\nabla^2S$ obey the identity unchanged.

*Consequences*, for a torsion-free connection:

- All second covariant derivatives of all tensor fields commute on an open set exactly when $R = 0$ there. Conversely, for the Levi-Civita connection, $R = 0$ on a simply connected open set lets every vector at a point extend to a parallel field on it, by the Frobenius theorem, which is the core of the flatness criterion.
- Order matters when partial derivatives are promoted to covariant ones in second-order field equations. For a vector potential, the contracted identity gives $\nabla_\nu\nabla^\mu A^\nu - \nabla^\mu\nabla_\nu A^\nu = R^\mu{}_\sigma A^\sigma$, so two flat-space forms of the wave equation differ in curved spacetime by a Ricci term.
- A parallel field, $\nabla V = 0$, satisfies $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$. On a surface, $R^\rho{}_{\sigma\mu\nu} = K(\delta^\rho{}_\mu g_{\sigma\nu} - \delta^\rho{}_\nu g_{\sigma\mu})$, so a nonzero parallel field on an open set forces $K = 0$ there.
- On a gradient, $[\nabla_\mu,\nabla_\nu]\nabla_\lambda f = -R^\sigma{}_{\lambda\mu\nu}\nabla_\sigma f$. Summing cyclically over $\lambda\mu\nu$, the symmetry of $\nabla_\mu\nabla_\nu f$ cancels the left side, which gives the cyclic identity $R^\sigma{}_{[\lambda\mu\nu]} = 0$.
- The Jacobi identity for the operators $\nabla_X$ gives the second Bianchi identity: the cyclic sum of $(\nabla_X\mathcal{R})(Y,Z)$ over $X, Y, Z$ vanishes.

*Limits.* The identity is pointwise: it needs the field twice differentiable and the connection once. Where curvature is concentrated, as at a cone's tip, it holds away from the tip, and the tip shows up only in holonomy. For spinor and gauge bundles the argument is unchanged, with the bundle's curvature in place of $R$.

**Takeaway:** For any connection, swapping two covariant derivatives gives the curvature operator minus a derivative along the torsion; bracket terms appear only when the directions are fields that do not commute.

*Picture:* An operator diagram: the commutator of two covariant derivatives splits into the curvature acting pointwise, a derivative along the torsion, and, for non-commuting fields, a derivative along their bracket.

*Continues:* `ways_in/both-orders-in-components`, `ways_in/one-term-per-index`<br>*Builds on:* [[lie-bracket]], [[torsion-tensor]], [[levi-civita-connection]]<br>*See:* `checks/polar-frame-bracket`, `checks/no-parallel-field-on-a-sphere`, `problems/operator-from-components`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| change of a change | — | How much a change along one side of a square differs from the change along the opposite side. | — |
| the two orders | — | The two ways of working out a change of a change on a square. One starts with the changes along the two sides that run the way you face. The other starts with the changes along the two sides that run to your left. | — |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way an arrow points, left or right, while it lies against the ground. A carried arrow never swings. | — |
| loop's turn | — | The angle by which an arrow comes back turned after being carried once around a loop without swinging. | [[holonomy]] |
| Ricci identity | REE-chee eye-DEN-tih-tee | The rule that, for arrows painted on a curved surface, a change of a change worked out in the two orders can give two different answers. The arrows sit at the corners of a tiny square. The two answers differ by the turn an arrow comes back with from one trip around that square. In a space with more directions, the difference is read from the Riemann curvature tensor. | [[ricci-identity]] |
| Riemann curvature tensor | REE-mahn | A table kept at every place. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed, divided by the loop's area. | [[riemann-curvature-tensor]] |

## Key equations

### Ricci identity for a vector field · working

$$
[\nabla_\mu,\nabla_\nu]V^\rho \equiv \nabla_\mu\nabla_\nu V^\rho - \nabla_\nu\nabla_\mu V^\rho = R^\rho{}_{\sigma\mu\nu}\,V^\sigma
$$

Swapping the order of two covariant derivatives on a vector field gives the Riemann tensor acting on the vector, with the two derivative directions in its last two slots.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\mu\nabla_\nu V^\rho$ | components of $\nabla(\nabla V)$; the rightmost derivative acts first | nabla mu nabla nu of V upper rho |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course convention | the Riemann tensor |
| $V^\sigma$ | the vector field at the point | the vector |

**Holds when:** Torsion-free connection; coordinate basis or tensor components of $\nabla^2V$; $V$ twice continuously differentiable.  
**Say it:** “Nabla mu nabla nu minus nabla nu nabla mu, acting on V, equals the Riemann tensor acting on V.”  
**Justified by:** `derivations/expand-both-orders`

### Covectors and mixed tensors · working

$$
[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\,\omega_\sigma,\qquad [\nabla_\mu,\nabla_\nu]S^\alpha{}_\beta = R^\alpha{}_{\lambda\mu\nu}S^\lambda{}_\beta - R^\lambda{}_{\beta\mu\nu}S^\alpha{}_\lambda
$$

Each upper index contributes a Riemann term with a plus sign and each lower index one with a minus sign; a scalar contributes nothing.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\omega_\rho$ | a covector field | omega lower rho |
| $S^\alpha{}_\beta$ | a tensor field with one upper and one lower index | S upper alpha lower beta |

**Holds when:** Torsion-free connection.  
**Say it:** “On a covector the commutator gives minus the Riemann tensor acting on it; a mixed tensor gets a plus term for its upper index and a minus term for its lower index.”  
**Justified by:** `derivations/one-term-per-index`

### Contracted Ricci identity · working

$$
\nabla_\mu\nabla_\nu V^\mu - \nabla_\nu\nabla_\mu V^\mu = R_{\sigma\nu}\,V^\sigma
$$

Swapping a divergence and a gradient on a vector field gives the Ricci tensor acting on the vector.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\sigma\nu}$ | Ricci tensor, $R_{\sigma\nu} = R^\mu{}_{\sigma\mu\nu}$ | the Ricci tensor |

**Holds when:** Torsion-free connection.  
**Say it:** “Swapping divergence and gradient gives the Ricci tensor acting on V.”  
**Justified by:** `derivations/expand-both-orders`

### Geodesic deviation from the swapped order · working

$$
\frac{D^2\xi^\mu}{d\tau^2} = u^\alpha\xi^\beta[\nabla_\alpha,\nabla_\beta]u^\mu = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma
$$

The relative acceleration of neighbouring free-fall worldlines is a commutator acting on the four-velocity, hence curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^\mu$ | separation vector to a neighbouring worldline | xi, the separation |
| $u^\mu$ | four-velocity of the free-fall worldlines | u, the four-velocity |
| $\tau$ | proper time along the worldlines | tau, proper time |

**Holds when:** A smooth family of geodesics; torsion-free connection; separation small compared with the curvature scale.  
**Say it:** “The second covariant derivative of the separation along the worldline equals minus the Riemann tensor fed u, xi and u.”  
**Justified by:** `derivations/tidal-drift-from-swapping-order`

### Commutator for a connection with torsion · formal

$$
[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma - \mathrm{Tor}^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho,\qquad \mathrm{Tor}^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu}
$$

For a connection that is not symmetric, a derivative of the field survives the swap, multiplied by the torsion.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathrm{Tor}^\lambda{}_{\mu\nu}$ | components of the torsion $\mathrm{Tor}(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$, with the derivative index first on $\Gamma$ | the torsion |

**Holds when:** Any affine connection, coordinate basis; the same term appears on every tensor, including scalars.  
**Say it:** “The commutator equals the Riemann tensor acting on V, minus the torsion times the derivative of V.”  
**Justified by:** `derivations/expand-both-orders`

## Derivations

### Expand both orders and cancel · working

**Goal:** Show that $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$, keeping any torsion visible until the end.

1. $\nabla_\nu V^\rho$ is a $(1,1)$ tensor, so $\nabla_\mu\nabla_\nu V^\rho = \partial_\mu(\nabla_\nu V^\rho) + \Gamma^\rho{}_{\mu\lambda}\nabla_\nu V^\lambda - \Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$.
2. Insert $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma$ into the first term: $\partial_\mu\partial_\nu V^\rho + (\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma + \Gamma^\rho{}_{\nu\sigma}\partial_\mu V^\sigma$.
3. Insert it into the second term: $\Gamma^\rho{}_{\mu\lambda}\partial_\nu V^\lambda + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}V^\sigma$.
4. Swap $\mu$ and $\nu$ and subtract. $\partial_\mu\partial_\nu V^\rho$ cancels, because partial derivatives of a twice continuously differentiable field commute.
5. $\Gamma^\rho{}_{\nu\sigma}\partial_\mu V^\sigma + \Gamma^\rho{}_{\mu\sigma}\partial_\nu V^\sigma$ is unchanged by the swap, so it cancels too.
6. The index correction leaves $-(\Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu})\nabla_\lambda V^\rho$, the torsion term, which vanishes for a symmetric connection.
7. The rest is $(\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})V^\sigma$, exactly the course $R^\rho{}_{\sigma\mu\nu}V^\sigma$.
8. Set $\rho = \mu$ and sum: $R^\mu{}_{\sigma\mu\nu} = R_{\sigma\nu}$ gives the contracted form.

**Result:** $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma - (\Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu})\nabla_\lambda V^\rho$, which for a torsion-free connection is the Ricci identity; contracted, $\nabla_\mu\nabla_\nu V^\mu - \nabla_\nu\nabla_\mu V^\mu = R_{\sigma\nu}V^\sigma$.

### Signs for covectors from a scalar · working

**Goal:** Find $[\nabla_\mu,\nabla_\nu]\omega_\rho$ and the rule for a mixed tensor, for a torsion-free connection.

1. For a scalar, $\nabla_\mu\nabla_\nu f = \partial_\mu\partial_\nu f - \Gamma^\lambda{}_{\mu\nu}\partial_\lambda f$ is symmetric in $\mu\nu$, so $[\nabla_\mu,\nabla_\nu]f = 0$.
2. For $f = \omega_\rho V^\rho$ the product rule gives $\nabla_\mu\nabla_\nu f = (\nabla_\mu\nabla_\nu\omega_\rho)V^\rho + (\nabla_\nu\omega_\rho)(\nabla_\mu V^\rho) + (\nabla_\mu\omega_\rho)(\nabla_\nu V^\rho) + \omega_\rho\nabla_\mu\nabla_\nu V^\rho$.
3. Swap and subtract. The two middle terms are unchanged by the swap and cancel, leaving $0 = ([\nabla_\mu,\nabla_\nu]\omega_\rho)V^\rho + \omega_\sigma R^\sigma{}_{\rho\mu\nu}V^\rho$ after renaming indices.
4. This holds for every $V$, so $[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\omega_\sigma$. A mixed tensor is locally a sum of products $U^\alpha\omega_\beta$, and the commutator is linear, so it gains $+R^\alpha{}_{\lambda\mu\nu}S^\lambda{}_\beta - R^\lambda{}_{\beta\mu\nu}S^\alpha{}_\lambda$.

**Result:** $[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\omega_\sigma$, with one term per index: plus for upper indices, minus for lower ones.

### Tidal drift from swapping order · working

**Goal:** Derive $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ from the Ricci identity.

1. For free-fall worldlines $x^\mu(\tau,s)$ put $u^\mu = \partial_\tau x^\mu$ and $\xi^\mu = \partial_s x^\mu$. Since $\partial_\tau\partial_s x^\mu = \partial_s\partial_\tau x^\mu$ and $\Gamma$ is symmetric, $u^\alpha\nabla_\alpha\xi^\mu = \xi^\alpha\nabla_\alpha u^\mu$.
2. Extend $u$ smoothly off the family if needed; only derivatives along the family enter. Then $D^2\xi^\mu/d\tau^2 = u^\alpha\nabla_\alpha(\xi^\beta\nabla_\beta u^\mu) = (u^\alpha\nabla_\alpha\xi^\beta)\nabla_\beta u^\mu + u^\alpha\xi^\beta\nabla_\alpha\nabla_\beta u^\mu$.
3. Free fall gives $u^\beta\nabla_\beta u^\mu = 0$ on every worldline, so its derivative across the family vanishes: $0 = (\xi^\alpha\nabla_\alpha u^\beta)\nabla_\beta u^\mu + \xi^\alpha u^\beta\nabla_\alpha\nabla_\beta u^\mu$.
4. Subtract the third line from the second; by the first step their first terms are equal. So $D^2\xi^\mu/d\tau^2 = u^\alpha\xi^\beta(\nabla_\alpha\nabla_\beta u^\mu - \nabla_\beta\nabla_\alpha u^\mu)$.
5. The Ricci identity gives $R^\mu{}_{\sigma\alpha\beta}u^\sigma u^\alpha\xi^\beta$, and antisymmetry in the last pair rewrites it as $-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

**Result:** $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$, the geodesic deviation equation in course form.

## Worked examples

### Both orders on the unit sphere · working

**Problem:** On the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, take $V = \partial_\phi$, with $V^\theta = 0$ and $V^\phi = 1$. Compute $\nabla_\theta\nabla_\phi V^\theta$ and $\nabla_\phi\nabla_\theta V^\theta$, and compare their difference with $R^\theta{}_{\phi\theta\phi}V^\phi$.

1. The nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$.
2. The components of $V$ are constant, so $\nabla_\nu V^\rho = \Gamma^\rho{}_{\nu\lambda}V^\lambda$: $\nabla_\theta V^\theta = 0$, $\nabla_\theta V^\phi = \cot\theta$, $\nabla_\phi V^\theta = -\sin\theta\cos\theta$, $\nabla_\phi V^\phi = 0$.
3. $\nabla_\theta\nabla_\phi V^\theta = \partial_\theta(-\sin\theta\cos\theta) + \Gamma^\theta{}_{\theta\lambda}\nabla_\phi V^\lambda - \Gamma^\phi{}_{\theta\phi}\nabla_\phi V^\theta = -\cos2\theta + 0 + \cos^2\theta = \sin^2\theta$.
4. $\nabla_\phi\nabla_\theta V^\theta = 0 + \Gamma^\theta{}_{\phi\phi}\nabla_\theta V^\phi - \Gamma^\phi{}_{\phi\theta}\nabla_\phi V^\theta = -\cos^2\theta + \cos^2\theta = 0$.
5. The difference is $\sin^2\theta$, and the course component $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ times $V^\phi = 1$ gives the same.
6. Dropping the index corrections, the last terms of the two middle lines, would change the second derivatives to $-\cos2\theta$ and $-\cos^2\theta$ but not their difference: for a torsion-free connection those corrections cancel in the swap.

**Answer:** $[\nabla_\theta,\nabla_\phi]V^\theta = \sin^2\theta = R^\theta{}_{\phi\theta\phi}V^\phi$, although $\nabla_\phi\nabla_\theta V^\theta = 0$.

**Takeaway:** The index correction matters for each second derivative but cancels in the commutator, which lands exactly on the Riemann component.

## Problems

### `ten-kilometre-square` · entry · difficulty 1 · estimate

On Earth, ignoring hills, a loop covering one square kilometre brings a carried arrow back turned by about 1.4 millionths of a degree. The turn grows in proportion to the area the loop covers. You paint arrows at the corners of a square 10 kilometres on each side, so that neighbouring arrows point nearly the same way. Then you work out the change of the change in both orders. By about how much do the two answers differ? Could you notice it with a school protractor?

**Hints**

1. How many square kilometres does the square cover?
2. The two orders differ by the turn of the loop around the field.

**Answer:** By about 140 millionths of a degree, roughly one seven-thousandth of a degree. A school protractor is marked in whole degrees, so nobody could notice it.

**Must contain:** The square covers 100 square kilometres; The two orders differ by the loop's turn; About 140 millionths of a degree, far too small for a protractor

**Numeric:** difference between the two orders = 0.000141 deg (magnitude, ±5%)

**Solution**

1. The square covers 10 times 10, which is 100 square kilometres.
2. The turn grows in proportion to the area, so it is 100 times 1.4 millionths, which is 140 millionths of a degree.
3. The two orders differ by exactly this loop's turn.
4. One degree divided by 140 millionths of a degree is about 7,000, so the difference is about one seven-thousandth of a degree.

### `fields-that-agree-at-a-point` · working · difficulty 2 · calculation

On the unit sphere, compare $V = \partial_\phi$ with $W = (\theta - \theta_0)\,\partial_\theta + \partial_\phi$, which equals $V$ at colatitude $\theta_0$ but has a different covariant derivative there. Compute both components of $[\nabla_\theta,\nabla_\phi]W^\rho$, show that they equal $R^\rho{}_{\sigma\theta\phi}W^\sigma$ everywhere, and compare with the result for $V$ at $\theta_0$.

**Hints**

1. Write $s = \theta - \theta_0$ and list the four components $\nabla_\nu W^\rho$ first.
2. For a torsion-free connection the index corrections cancel, so $[\nabla_\theta,\nabla_\phi]W^\rho = \partial_\theta(\nabla_\phi W^\rho) - \partial_\phi(\nabla_\theta W^\rho) + \Gamma^\rho{}_{\theta\lambda}\nabla_\phi W^\lambda - \Gamma^\rho{}_{\phi\lambda}\nabla_\theta W^\lambda$.

**Answer:** $[\nabla_\theta,\nabla_\phi]W^\theta = \sin^2\theta$ and $[\nabla_\theta,\nabla_\phi]W^\phi = -(\theta - \theta_0)$, equal to $R^\theta{}_{\phi\theta\phi}W^\phi$ and $R^\phi{}_{\theta\theta\phi}W^\theta$. At $\theta_0$ both match the result for $V$, although $\nabla_\theta W^\theta = 1$ there while $\nabla_\theta V^\theta = 0$.

**Must contain:** The theta component is sine squared theta; The phi component is minus theta minus theta zero, which vanishes at theta zero; Same commutator as V at theta zero despite different first derivatives

**Solution**

1. With $s = \theta - \theta_0$: $\nabla_\theta W^\theta = 1$, $\nabla_\theta W^\phi = \cot\theta$, $\nabla_\phi W^\theta = -\sin\theta\cos\theta$, $\nabla_\phi W^\phi = s\cot\theta$.
2. $\theta$ component: $\partial_\theta(-\sin\theta\cos\theta) - \partial_\phi(1) + 0 - \Gamma^\theta{}_{\phi\phi}\nabla_\theta W^\phi = -\cos2\theta + \cos^2\theta = \sin^2\theta$.
3. $\phi$ component: $\partial_\theta(s\cot\theta) - \partial_\phi(\cot\theta) + \Gamma^\phi{}_{\theta\phi}\nabla_\phi W^\phi - \Gamma^\phi{}_{\phi\theta}\nabla_\theta W^\theta = \cot\theta - s\csc^2\theta + s\cot^2\theta - \cot\theta = -s$.
4. With $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and $R^\phi{}_{\theta\theta\phi} = -1$, $R^\rho{}_{\sigma\theta\phi}W^\sigma = (\sin^2\theta,\ -s)$, matching everywhere.
5. At $\theta_0$, $s = 0$ and the commutator is $(\sin^2\theta_0, 0)$, the same as for $V$: only the value of the field at the point enters.

**Targets:** `painting-matters`

### `gradiometer-in-orbit` · working · difficulty 2 · estimate

Two test masses fall freely 255 km above Earth, 0.50 m apart along the local vertical and at rest relative to each other in a non-rotating freely falling frame. (a) At which step of the derivation "Tidal drift from swapping order" does the Ricci identity enter? (b) Treating Earth as a static sphere with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and radius 6371 km, find $R^z{}_{0z0}$ and the relative acceleration of the masses.

**Hints**

1. Once free fall and the symmetric connection have been used, what is left of $D^2\xi^\mu/d\tau^2$?
2. Use $-c^2R^z{}_{0z0} = 2GM/r^3$ with $r$ measured from Earth's centre.

**Answer:** (a) In the last step, where $u^\alpha\xi^\beta[\nabla_\alpha,\nabla_\beta]u^\mu$ becomes curvature. (b) $r = 6626$ km, $R^z{}_{0z0} = -3.05\times10^{-23}\ \mathrm{m^{-2}}$, and the masses separate with relative acceleration $1.37\times10^{-6}\ \mathrm{m\,s^{-2}}$.

**Must contain:** The identity converts the swapped second derivatives of the four-velocity into curvature; R z zero z zero is about minus 3.05 times ten to the minus 23 per square metre; Relative acceleration about 1.37 micrometres per second squared, outward

**Numeric:** relative acceleration = 1.37e-06 m/s^2 (magnitude, ±2%); vertical tidal Riemann component = -3.05e-23 m^-2 (signed, ±2%)

**Solution**

1. (a) The first four steps use only the symmetric connection and free fall to reduce the relative acceleration to $u^\alpha\xi^\beta[\nabla_\alpha,\nabla_\beta]u^\mu$; the last step applies the Ricci identity.
2. $r = 6371 + 255 = 6626$ km, so $GM/r^3 = 3.986\times10^{14}/(6.626\times10^{6})^3 = 1.370\times10^{-6}\ \mathrm{s^{-2}}$.
3. Along the vertical $-c^2R^z{}_{0z0} = 2GM/r^3 = 2.740\times10^{-6}\ \mathrm{s^{-2}}$, so $R^z{}_{0z0} = -2.740\times10^{-6}/(2.998\times10^{8})^2 = -3.05\times10^{-23}\ \mathrm{m^{-2}}$.
4. With $u^\mu = (c,0,0,0)$, geodesic deviation gives $\ddot\xi^z = -c^2R^z{}_{0z0}\,\xi^z = 2.740\times10^{-6} \times 0.50 = 1.37\times10^{-6}\ \mathrm{m\,s^{-2}}$, positive, so the masses separate.

### `operator-from-components` · formal · difficulty 2 · proof

For a torsion-free connection, show that $\mathcal{R}(X,Y)Z = X^\mu Y^\nu[\nabla_\mu,\nabla_\nu]Z$, so that the bracket term removes every derivative of $X$ and $Y$. Then show that $\nabla_X\nabla_YZ - \nabla_Y\nabla_XZ$ alone is not linear over functions in $X$.

**Hints**

1. Write $\nabla_YZ$ as the contraction $Y^\nu\nabla_\nu Z$ and use the product rule.
2. Compute $[fX, Y]$.

**Answer:** $\nabla_X\nabla_YZ - \nabla_Y\nabla_XZ = X^\mu Y^\nu[\nabla_\mu,\nabla_\nu]Z + \nabla_{\nabla_XY - \nabla_YX}Z$, and with zero torsion the last term is $\nabla_{[X,Y]}Z$, which the definition of $\mathcal{R}$ subtracts. Replacing $X$ by $fX$ adds $-(Yf)\nabla_XZ$ to the unbracketed difference, and $\nabla_{[fX,Y]}Z$ contains the same term, so only $\mathcal{R}$ is function-linear.

**Must contain:** The product rule produces derivatives of X and Y only through nabla X Y minus nabla Y X; Zero torsion turns that into the Lie bracket, which the definition subtracts; The extra term minus Y f nabla X Z spoils linearity without the bracket

**Solution**

1. $\nabla_X(\nabla_YZ) = X^\mu\nabla_\mu(Y^\nu\nabla_\nu Z) = (\nabla_XY)^\nu\nabla_\nu Z + X^\mu Y^\nu\nabla_\mu\nabla_\nu Z$.
2. Swapping $X$ and $Y$ and subtracting gives $X^\mu Y^\nu(\nabla_\mu\nabla_\nu - \nabla_\nu\nabla_\mu)Z + \nabla_{\nabla_XY - \nabla_YX}Z$.
3. Zero torsion means $\nabla_XY - \nabla_YX = [X,Y]$, so $\mathcal{R}(X,Y)Z = X^\mu Y^\nu[\nabla_\mu,\nabla_\nu]Z = R^\rho{}_{\sigma\mu\nu}Z^\sigma X^\mu Y^\nu$.
4. For a function $f$, $\nabla_{fX}\nabla_YZ - \nabla_Y\nabla_{fX}Z = f(\nabla_X\nabla_YZ - \nabla_Y\nabla_XZ) - (Yf)\nabla_XZ$.
5. Since $[fX,Y] = f[X,Y] - (Yf)X$, $\nabla_{[fX,Y]}Z = f\nabla_{[X,Y]}Z - (Yf)\nabla_XZ$, which cancels the extra term, so $\mathcal{R}(fX,Y)Z = f\,\mathcal{R}(X,Y)Z$.

**Targets:** `any-fields-commutator-is-curvature`

## Observations

- **The vertical gradient of Earth's gravity, measured by comparing two freely falling atom clouds** (measured, working). An atom-interferometer gradiometer drops two clouds of laser-cooled atoms at different heights and compares their free-fall accelerations. Their relative acceleration per unit separation is the tidal entry $-c^2R^z{}_{0z0}$, which geodesic deviation obtains from the Ricci identity; no single freely falling accelerometer can detect it. *Numbers:* Static spherical Earth: $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$ at the surface, so $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. The standard free-air gradient is $3.086\times10^{-6}\ \mathrm{s^{-2}}$. *Reference:* M. J. Snadden, J. M. McGuirk, P. Bouyer, K. G. Haritos, M. A. Kasevich (1998), *Measurement of the Earth's Gravity Gradient with an Atom Interferometer-Based Gravity Gradiometer*, Physical Review Letters 81, 971–974, doi:10.1103/PhysRevLett.81.971

## Teaching arc

1. **Ask whether order matters for numbers** (entry). Have the learner predict, then work the hillside heights in both orders and find the same number. *Why:* It sets an expectation that arrows will break. *Predict:* If you find how the height changes along your side and how that change differs on the opposite side, then start with the other two sides, will you get the same number? *Uses:* `ways_in/changes-of-changes-for-numbers`, `checks/heights-at-four-corners`
2. **Break the expectation with arrows** (entry). Repeat with painted arrows on a ball after a prediction, then switch to a flat floor and to a second painting. *Why:* The floor and the second painting leave the loop as the only cause. *Predict:* If the corners hold arrows on a ball instead of heights, will the two orders still agree? *Visual:* [[carry-the-far-arrow-home-two-ways]] *Uses:* `ways_in/arrows-painted-on-a-ball`, `checks/painted-ball-two-orders`, `checks/two-paintings-one-square`
3. **Expand and cross off** (working). Expand both orders, let the learner cross off the three cancelling groups, then check against the sphere. *Why:* Every derivative of the field cancelling is why the result is a tensor. *Predict:* After you swap the two derivatives and subtract, will any derivative of the field be left? *Visual:* [[cross-off-matching-terms]] *Uses:* `ways_in/both-orders-in-components`, `derivations/expand-both-orders`, `worked_examples/both-orders-on-the-sphere`
4. **Fix the signs index by index** (working). Derive the covector sign from a scalar, then test it on the sphere and on the metric. *Why:* Sign errors on lower indices are the most common slip in later derivations. *Predict:* Swapping the order does nothing to a number. What sign must a covector term carry? *Uses:* `ways_in/one-term-per-index`, `checks/covector-sign`, `checks/metric-commutator`
5. **Measure it with falling masses** (working). Derive geodesic deviation by swapping order, then connect it to a gradiometer. *Why:* It shows the identity as the engine behind a quantity instruments measure. *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tides-from-swapping-order`, `derivations/tidal-drift-from-swapping-order`, `observations/atom-gravity-gradiometer`
6. **Separate curvature from brackets and torsion** (formal). State the operator identity, then run the polar frame on a flat plane. *Why:* It prevents reading every nonzero commutator as curvature. *Predict:* On a flat plane, can two derivatives along the polar directions fail to commute? *Uses:* `ways_in/curvature-as-a-commutator`, `checks/polar-frame-bracket`

## Misconceptions

### “Taking two changes in either order always gives the same answer, for arrows just as for numbers.” · entry · `arrows-like-numbers`

- **Why it is tempting:** For heights and temperatures the order never matters.
- **What is true:** Arrows at different spots can be compared only by carrying one to the other, and the two orders carry the far arrow home by different routes. On a ball the two copies that arrive differ by the turn of the loop those routes make.
- **Exposed by:** `checks/painted-ball-two-orders`

### “A swirlier pattern of painted arrows makes the two orders differ by more.” · entry · `painting-matters`

- **Why it is tempting:** Both answers are built from how the arrows change, so a wilder pattern seems to change them more.
- **What is true:** No painted arrow survives when the two orders are subtracted. What remains is the turn of the loop, which depends only on the square and the ball.
- **Exposed by:** `checks/two-paintings-one-square`

### “Where all Christoffel symbols vanish, second covariant derivatives are plain second partial derivatives, so they commute there.” · working · `zero-christoffels-means-commute`

- **Why it is tempting:** First covariant derivatives do reduce to partial derivatives at such a point.
- **What is true:** The second derivative still contains the derivatives of the Christoffel symbols, which need not vanish there. Their antisymmetric part is the Riemann tensor.
- **Exposed by:** `checks/inertial-frame-claim`

### “Every index of a tensor gets a plus-sign Riemann term when the derivatives are swapped.” · working · `lower-index-plus-sign`

- **Why it is tempting:** Some texts write every term with a plus sign by moving indices around.
- **What is true:** With the Riemann tensor in standard placement, a lower index needs a minus sign, because the swap does nothing to the number formed by contracting a covector with a vector.
- **Exposed by:** `checks/covector-sign`

### “For any two vector fields, a nonzero difference between the two orders of differentiating along them proves the space is curved.” · formal · `any-fields-commutator-is-curvature`

- **Why it is tempting:** Coordinate basis fields commute, so the bracket term is easy to forget in other frames.
- **What is true:** Along fields whose bracket is nonzero, the derivative along the bracket must be subtracted first. The polar frame on a flat plane gives a nonzero difference with zero curvature.
- **Exposed by:** `checks/polar-frame-bracket`

## Checks

1. **Entry · numeric** `checks/heights-at-four-corners`. A square field on a hillside is 200 metres along each side. You stand at one corner, the start, facing along one side with the field on your left. Above the foot of the hill, the ground is 20 metres high at the start and 26 metres at the corner ahead. It is 23 metres at the corner on your left and 35 metres at the far corner. Work out the change of the change in both orders. Do the two answers agree?
   - **Hints:** Start with the changes going ahead: find the rise along your own side and along the opposite side, then subtract.
   - **Answer:** Yes, both give 6 metres. Start with the changes going ahead. From the start to the corner ahead, the height rises 6 metres. On the opposite side, from the corner on your left to the far corner, it rises 12 metres. So the change of the change is 12 minus 6, which is 6 metres. Now start with the changes going left. From the start to the corner on your left, it rises 3 metres. From the corner ahead to the far corner, it rises 9 metres. So the change of the change is 9 minus 3, again 6 metres. Both orders equal the far corner plus the start, minus the other two corners: 35 plus 20, minus 26, minus 23.
   - **Must contain:** Both orders give 6 metres; Both equal the far corner plus the start minus the other two corners
   - **Numeric:** change of the change = 6 m (magnitude, ±0.1)
2. **Entry · predict** `checks/painted-ball-two-orders`. On a huge round ball, you paint an arrow at each corner of a tiny square, so that neighbouring arrows point nearly the same way. Stand at one corner, the start, facing along one side with the square on your left. You measure the change from one corner to a neighbouring corner like this. Lay a cardboard copy on the second corner's painted arrow. Carry it along the side to the first corner, never letting it swing. Then measure the angle from the first corner's painted arrow to the copy. Now work out the change of the change in both orders. Do the two orders give the same number? What if the square is drawn on a flat floor instead?
   - **Hints:** Which two routes lead from the far corner back to the start?
   - **Answer:** On the ball, no, although they differ only by a tiny angle. When the four changes are regrouped, the difference between the orders compares two copies of the far corner's arrow. They are carried home to the start by two routes: one through the corner ahead and one through the corner on your left. The two routes together make a loop around the square. On a ball, a small loop brings an arrow back turned a little, so the two copies differ by that turn, and so do the two orders. On a flat floor, every carried copy keeps its angle to a chosen wall, so the copies match and the orders agree.
   - **Must contain:** On the ball the two orders differ; They differ by the loop's turn, because the far arrow comes home by two routes; On a flat floor they agree
   - **Targets:** `arrows-like-numbers`
   - **Visual:** [[carry-the-far-arrow-home-two-ways]]
3. **Entry · numeric** `checks/two-paintings-one-square`. Two friends use the same tiny square on a huge round ball, both starting from the same corner with the square on their left. One paints arrows that barely change from corner to corner. The other paints a swirling pattern that changes more, though neighbouring arrows still point nearly the same way. The first friend finds that the two orders differ by 3 millionths of a degree. What does the second friend find, and why?
   - **Hints:** After the subtraction, what is left besides the two routes home?
   - **Answer:** The same, 3 millionths of a degree. When the two orders are subtracted, the difference compares two copies of the far arrow, carried home by two routes. Those copies differ by the turn of the loop around the square. That turn is the same whichever way the far arrow points, and no other painted arrow appears in that turn. The turn depends only on the square and the ball, which are the same for both friends.
   - **Must contain:** The same difference, 3 millionths of a degree; The painted arrows drop out; Only the loop around the square matters
   - **Numeric:** difference between the two orders = 3e-06 deg (magnitude, ±5%)
   - **Targets:** `painting-matters`
   - **Visual:** [[carry-the-far-arrow-home-two-ways]]
4. **Working · evaluate-claim** `checks/inertial-frame-claim`. At a point $p$ a classmate uses coordinates in which every $\Gamma^\lambda{}_{\mu\nu}(p) = 0$. She concludes that $\nabla_\mu\nabla_\nu V^\rho = \partial_\mu\partial_\nu V^\rho$ at $p$, so $[\nabla_\mu,\nabla_\nu]V^\rho = 0$ there. Evaluate the claim.
   - **Hints:** Differentiate $\Gamma^\rho{}_{\nu\sigma}V^\sigma$ before setting $\Gamma = 0$.
   - **Answer:** The claim is wrong. At $p$ the terms with an undifferentiated $\Gamma$ vanish, but $\partial_\mu(\partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma)$ still contains $(\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma$, and derivatives of $\Gamma$ need not vanish at $p$. Swapping and subtracting removes $\partial_\mu\partial_\nu V^\rho$ and leaves $(\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma})V^\sigma$. Because the products of Christoffel symbols vanish at $p$, that is $R^\rho{}_{\sigma\mu\nu}V^\sigma$ there. Both sides are tensors, so the identity then holds in every coordinate system.
   - **Must contain:** Derivatives of the Christoffel symbols survive at p; Their antisymmetric combination is the Riemann tensor at p; The tensor equation then holds in all coordinates
   - **Targets:** `zero-christoffels-means-commute`
5. **Working · numeric** `checks/covector-sign`. On the unit sphere take the covector field $\omega = d\phi$, with $\omega_\theta = 0$ and $\omega_\phi = 1$. A classmate uses $[\nabla_\mu,\nabla_\nu]\omega_\rho = +R^\sigma{}_{\rho\mu\nu}\omega_\sigma$ and predicts $[\nabla_\theta,\nabla_\phi]\omega_\theta = -1$. What is the correct value, and why must the sign differ from the vector rule?
   - **Hints:** Use $R^\phi{}_{\theta\theta\phi} = -1$ on the unit sphere. / What does the swap do to the number $\omega_\rho V^\rho$?
   - **Answer:** It is $+1$. The course rule gives $[\nabla_\theta,\nabla_\phi]\omega_\theta = -R^\sigma{}_{\theta\theta\phi}\omega_\sigma = -R^\phi{}_{\theta\theta\phi} = +1$, using $R^\phi{}_{\theta\theta\phi} = -1$. The sign must flip because the swap does nothing to the scalar $\omega_\rho V^\rho$: in the product rule the cross terms cancel, so the covector term must cancel the vector term $+\omega_\rho R^\rho{}_{\sigma\mu\nu}V^\sigma$. A direct computation agrees: $\nabla_\theta\nabla_\phi\omega_\theta = \csc^2\theta + \cot^2\theta$ and $\nabla_\phi\nabla_\theta\omega_\theta = 2\cot^2\theta$, which differ by 1.
   - **Must contain:** The value is plus one; A lower index takes minus the Riemann tensor; The swap annihilates the scalar formed with any vector
   - **Numeric:** commutator component = 1 1 (signed, ±0.01)
   - **Targets:** `lower-index-plus-sign`
6. **Working · explain** `checks/metric-commutator`. For the Levi-Civita connection, $\nabla_\lambda g_{\rho\sigma} = 0$. Apply the one-term-per-index rule to $[\nabla_\mu,\nabla_\nu]g_{\rho\sigma}$. What symmetry of the Riemann tensor follows?
   - **Hints:** Lower the first index of each Riemann term with the metric.
   - **Answer:** The commutator of a field with zero derivative is zero. The rule gives $-R^\lambda{}_{\rho\mu\nu}g_{\lambda\sigma} - R^\lambda{}_{\sigma\mu\nu}g_{\rho\lambda} = -R_{\sigma\rho\mu\nu} - R_{\rho\sigma\mu\nu}$. So $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$: the curvature of a metric-compatible connection is antisymmetric in its first pair, which is why small-loop changes are rotations or boosts.
   - **Must contain:** The commutator vanishes because the metric is parallel; Two lower-index terms give minus R sigma rho mu nu minus R rho sigma mu nu; Antisymmetry in the first pair of indices
7. **Formal · explain** `checks/polar-frame-bracket`. On the flat plane in polar coordinates, $ds^2 = dr^2 + r^2d\phi^2$, take $X = \partial_r$ and $Y = \hat e_\phi = r^{-1}\partial_\phi$. Compute $\nabla_X\nabla_YX - \nabla_Y\nabla_XX$, then $\mathcal{R}(X,Y)X$. What does the comparison show?
   - **Hints:** Compute $[\partial_r, r^{-1}\partial_\phi]$ first.
   - **Answer:** With $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$: $\nabla_YX = r^{-1}\nabla_\phi\partial_r = r^{-2}\partial_\phi$, and $\nabla_X(r^{-2}\partial_\phi) = -2r^{-3}\partial_\phi + r^{-3}\partial_\phi = -r^{-2}\hat e_\phi$. Since $\nabla_XX = 0$, the difference is $-r^{-2}\hat e_\phi$, not zero. But $[X,Y] = -r^{-2}\partial_\phi$, so $\nabla_{[X,Y]}X = -r^{-3}\partial_\phi = -r^{-2}\hat e_\phi$, and $\mathcal{R}(X,Y)X = 0$, as a flat plane requires. The nonzero difference came from the bracket of the fields, not from curvature.
   - **Must contain:** The unbracketed difference is minus one over r squared along e phi; The bracket term is the same, so the curvature term is zero; Non-commuting fields, not curvature, produced the difference
   - **Targets:** `any-fields-commutator-is-curvature`
8. **Formal · explain** `checks/no-parallel-field-on-a-sphere`. Can a round sphere of radius $a$ carry a nonzero vector field $V$ with $\nabla V = 0$ on some open set? Answer with the Ricci identity.
   - **Hints:** Write the two-dimensional Riemann tensor in terms of $K$.
   - **Answer:** No. If $\nabla V = 0$ on the open set, both second derivatives vanish, so $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$ there. On a surface $R^\rho{}_{\sigma\mu\nu}V^\sigma = K(\delta^\rho{}_\mu V_\nu - \delta^\rho{}_\nu V_\mu)$. In an orthonormal frame at a point, $\rho = \mu = 1$, $\nu = 2$ gives $KV_2 = 0$, and $\rho = \nu = 2$, $\mu = 1$ gives $-KV_1 = 0$. With $K = 1/a^2 \ne 0$, $V = 0$.
   - **Must contain:** A parallel field satisfies R rho sigma mu nu V sigma equals zero; On a surface this forces K times V to vanish; With K nonzero on the sphere, V must be zero

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Order of the indices after a semicolon | Indices after the semicolon apply left to right: $V^\rho{}_{;\nu\mu} = \nabla_\mu\nabla_\nu V^\rho$, so $V^\rho{}_{;\nu\mu} - V^\rho{}_{;\mu\nu} = R^\rho{}_{\sigma\mu\nu}V^\sigma$. | Operator notation puts the outer derivative on the left, the reverse of the semicolon string, and some texts write $\nabla_{[\mu}\nabla_{\nu]}$ with a factor one half. |
| How the lower-index term is written | $[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\omega_\sigma$. | Some texts write it with a plus sign as $R_\rho{}^\sigma{}_{\mu\nu}\omega_\sigma$; for a metric connection the two agree. |
| Overall sign and slot order of the Riemann tensor in the commutator | The course Riemann tensor, derivative index first on $\Gamma$, gives $[\nabla_\mu,\nabla_\nu]V^\rho = +R^\rho{}_{\sigma\mu\nu}V^\sigma$, with $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ on the unit sphere. | Some texts reverse the overall sign, put the derivative index last, or place the loop-plane indices first. Calibrate with the unit sphere before borrowing a sign. |

## Visuals

- ★ [[carry-the-far-arrow-home-two-ways]] (flagship): Makes the entry result visible: two orders, two routes home for the far arrow, and a difference equal to the loop's turn for any painting. *Sketch:* A tiny square on a ball, a flat floor or a saddle, with a painted arrow field chosen from uniform, swirl or drawn by hand. The four side changes appear as angles at their corners, then the two orders and their difference. Copies of the far arrow travel home by both routes and land at the start. Changing the painting leaves the difference fixed; enlarging the square scales it with area; the floor gives zero and the saddle a turn to the right.
- [[cross-off-matching-terms]] (supporting): The ledger of cancelling terms in the component derivation. *Sketch:* Both orders of the second covariant derivative laid out as term tiles. Selecting two tiles that cancel removes them and names the reason: commuting partials, a symmetric pair, or symmetric Christoffel symbols. A torsion switch keeps the last pair alive; the survivors assemble into the Riemann tensor acting on the vector.
- [[falling-ring-of-crumbs]] (supporting): Tidal drift as the measured face of the swapped order. *Sketch:* A ring of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it, with sliders for mass and distance and a readout of relative acceleration per unit separation.

## Tutor moves

**Open with**

- On a hillside you stand at one corner of a square field, facing along one side, with the field on your left. You measure the height of the ground at all four corners. You find how the height changes along the side ahead of you, and how that change differs on the opposite side. Then you start with the two sides that run to your left instead. Will the two answers match? *(prediction)*
- Now picture arrows painted at the corners of a tiny square on a huge round ball. To compare two arrows, you carry a copy of one to the other without letting it swing. Will the two orders still give the same answer? *(prediction)*

**If the learner is stuck**

- *The learner loses track of terms in the expansion.* → Sort the terms into the three cancelling groups before looking at the survivors, then work the sphere example. *Uses:* `derivations/expand-both-orders`, `worked_examples/both-orders-on-the-sphere`

**Common questions**

- *Why do I have to carry the arrow to compare it?* (entry) In a flat room you could measure every arrow against one wall. Two arrows at different spots on a ball have no such wall, because the ground faces a different way at every spot. The fair comparison is to carry a copy of one arrow to the other without letting it swing. Different routes can deliver the copy pointing different ways, and the two orders use different routes. That is where the difference between the orders comes from. *Uses:* `ways_in/arrows-painted-on-a-ball`
- *Does the direction of the arrow at the corner ever matter?* (entry) On a ball, no. Every arrow comes back from a loop turned by the same amount, so only the loop matters. In a space with more directions, the change can depend on which way the arrow points. It can also depend on how the tiny square is tilted. The Riemann curvature tensor is the table of those answers. The Ricci identity reads the difference of the two orders straight from that table. *Uses:* `riemann-curvature-tensor/ways_in/a-table-of-turns`
- *Why does the Earth number say to ignore hills? Would a hill change the answer?* (entry) A hilltop does change the answer, but not every hill does. The turn a loop gives an arrow depends on how sharply the ground curves over the piece the loop goes round. A hilltop curves far more sharply than Earth as a whole. Take a hilltop that curves like a ball of radius 100 metres. A square 10 metres along each side, marked over that top, turns an arrow by about half a degree. You could measure that with care. A long ridge that keeps the same shape all along its length is different. Roll a sheet of paper into a tube, and you can still lay it flat again without stretching it. The ground on such a ridge can be laid flat in the same way. Ground like that adds no turn of its own. So the millionth-of-a-degree number is about Earth's roundness alone, on ground that curves no more sharply than Earth does. *Uses:* `ways_in/arrows-painted-on-a-ball`

**Switching levels**

- To working when: asks how to write it with derivatives; uses indices or Christoffel symbols. Expand both orders and work the sphere example. *Uses:* `ways_in/both-orders-in-components`, `worked_examples/both-orders-on-the-sphere`
- To formal when: asks about frames that are not coordinates; asks what torsion changes. Present the operator identity with bracket and torsion terms, then the polar frame check. *Uses:* `ways_in/curvature-as-a-commutator`, `checks/polar-frame-bracket`
- To research when: asks about focusing, singularities or gauge theories. Open the research horizon. *Uses:* `research_horizon/focusing-and-singularities`, `research_horizon/yang-mills-field-strength`

**Pronunciations:** Ricci → REE-chee; Ricci-Curbastro → REE-chee koor-BAH-stroh; Levi-Civita → LEH-vee CHEE-vee-tah; Riemann → REE-mahn; Raychaudhuri → ray-CHOWD-hoo-ree; Bochner → BOKH-ner

**Voice notes:** Say the identity in words before the symbols, and warn aloud that the rightmost derivative acts first while a semicolon string runs the other way.

## History

- **Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900).** Set out the absolute differential calculus, now called tensor calculus, in its standard form, with covariant differentiation at its centre. The rule for exchanging the order of covariant derivatives carries Ricci's name. Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900), *Méthodes de calcul différentiel absolu et leurs applications*, Mathematische Annalen 54, 125–201, doi:10.1007/BF01454201
- **Tullio Levi-Civita (1917).** Introduced parallel transport on Riemannian manifolds, first through an embedding in a Euclidean space and then showing that it depends only on the metric, and used it to give Riemann's curvature a geometric meaning. That meaning is behind reading the exchange rule as carrying vectors around small loops. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–204, doi:10.1007/BF03014898

## Research horizon

- **Focusing and the singularity theorems.** Contracting the Ricci identity along a congruence of free-fall worldlines gives the Raychaudhuri equation for the rate of change of their expansion, in which $R_{\mu\nu}u^\mu u^\nu$ drives focusing. For a congruence without rotation, an energy condition makes the expansion decrease monotonically, so a bundle of worldlines or light rays that is already converging reaches a caustic within finite proper time or affine parameter, a key step in the singularity theorems. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123; Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57
- **Curvature and the existence of symmetries.** Commuting covariant derivatives on a vector field and integrating over a closed manifold ties the field's derivatives to Ricci curvature. This Bochner technique shows that a closed Riemannian manifold with negative Ricci curvature has no nonzero Killing fields, and one with positive Ricci curvature has no nonzero harmonic one-forms. Salomon Bochner (1946), *Vector fields and Ricci curvature*, Bulletin of the American Mathematical Society 52, 776–797, doi:10.1090/S0002-9904-1946-08647-4
- **Field strength in gauge theories.** In a gauge theory the commutator of gauge-covariant derivatives is the field strength. For a non-abelian group it gains a commutator of potentials, just as the Riemann tensor contains products of Christoffel symbols, and the field strength then transforms like the curvature of a connection. Chen Ning Yang, Robert L. Mills (1954), *Conservation of isotopic spin and isotopic gauge invariance*, Physical Review 96, 191–195, doi:10.1103/PhysRev.96.191

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** A square field sits on a hillside and each corner has a height. You take the rise along the side ahead of you and the rise along the opposite side, and the difference between those two rises is the change of a change. If you start instead with the two sides running to your left you get the same number, because both ways come to the far corner plus the start, minus the other two corners. I could redo that part myself with any four numbers. On a ball you cannot just read off how much an arrow changes, because there is nothing to measure both arrows against, so you copy the neighbouring arrow, carry it along the side without letting it swing, and measure the angle. Then the two orders come out different, and the difference is the turn a trip round the square gives an arrow. On Earth that is about a millionth of a degree for a square kilometre, far too small to see. The painting of the arrows does not matter. What I could not say back: when the change runs between two corners that I am not standing at, I did not know which of them 'your corner' was, so I did not know which arrow the angle is measured from, or which way to face for the plus sign. I did not know where the wall came from. In 'a copy of the far arrow makes the second angle of the sum with that corner's painted arrow' I lost the thread completely; I read it three times and gave up. I did not know which rule the two taped arrows obey, or where 'home' is. And I could not tell what the phrase 'the two orders' means on its own, because nothing ever names them; in the ball question I also did not know which way I was facing, although the answer talked about the corner ahead and the corner on my left.

**Stumbles (25)**

- “Around a tiny square, you can find how a change along one side differs on the opposite side, starting from either pair of opposite sides.”: Reread. 'A change along one side differs on the opposite side' packs two things into one clause, and 'starting from either pair of opposite sides' is a condition hung on the end. The next sentence then says 'the two orders', a phrase the summary never introduces.
- “they differ by the turn an arrow gets from one trip around the square”: Two wordings for one idea: the glossary and both entry ways say an arrow 'comes back turned', while the summary says it 'gets' a turn.
- “Does the order matter when you work out a change of a change?”: The way's question is the first thing after the summary, and it uses 'a change of a change' before the reader has met it. Neither the summary nor anything earlier defines the phrase.
- “Call the corner in front of you the corner ahead, the corner along the side to your left the corner on your left, and the last one the far corner.”: Reread. 'The corner along the side to your left the corner on your left' runs two noun phrases together with no verb or comma, so the sentence has to be parsed twice.
- “For arrows it can, as "Arrows painted on a ball" shows.”: Elliptical: 'it can' leaves the reader to supply 'matter' from the sentence before.
- “On a ball, a small loop with its piece of ball on your left brings the arrow back turned a little toward your left.”: Reread. 'A small loop with its piece of ball on your left' is a noun phrase doing the work of an instruction, and 'its piece of ball' is a phrase a reader has never met.
- “On a huge round ball, mark a tiny square.”: The ball way continues the hillside way, but its first sentence points at nothing earlier; the link only arrives in the third sentence. Dropping the hillside way's closing pointer made the seam weaker still.
- “Then measure the angle from your corner's painted arrow to the copy.”: Ambiguous. The reader was told to stand at the start, but this recipe is later applied to pairs such as the corner on your left and the far corner. With four corners in play, 'your corner' and 'the neighbouring corner' do not say which is which.
- “First order: the change from the corner on your left to the far corner, minus the change from the start to the corner ahead.”: A step left implicit. The way describes how to measure an angle between two corners but never says that this angle is what 'the change from one corner to another' means, so the reader cannot tell which corner is the reference.
- “Carry the copy back along the side between the two corners, never letting it swing.”: 'Back' says you are returning the copy to where you came from, but the reader has not travelled; and 'the side between the two corners' makes them work out which side that is.
- “A ball offers no wall to measure arrows against, because the ground faces a different way at every spot.”: A wall appears from nowhere: nothing has suggested measuring an arrow against a wall, so the reader stops on the word.
- “The first order minus the second equals the turn an arrow comes back with from one trip around the square. Walk that trip ahead first, turning left at each corner, with the square on your left.”: Reread. The trip is used in the claim and only described afterwards, so on first reading 'one trip around the square' has no direction and the sign that follows has nothing to hang on.
- “There, a copy of the far arrow makes the second angle of the sum with that corner's painted arrow.”: The hardest sentence in the note. 'Makes an angle with' buries which two things are being compared and where, and 'there' has to carry the location.
- “Two taped arrows can both obey the rule, so they keep the angle between them.”: 'The rule' has no antecedent in the way; the no-swing instruction is never called a rule. The sentence also asks the reader to accept the key fact on the strength of the word 'can'.
- “Tape the far copy to a copy of that painted arrow, and carry both home without swinging.”: 'Home' is used for the first time here, with no reference: home for the reader could be any corner.
- “On a ball, a tiny square cannot have straight sides and four exact right angles.”: 'Straight' on a curved surface with no definition, which the ways elsewhere avoid by talking about walking without steering.
- “On a huge round ball, you paint an arrow at each corner of a tiny square... You measure each change by carrying a cardboard copy of the neighbouring corner's arrow back along the side, without letting it swing.”: The check's starting state is ambiguous: it never places the reader, yet its answer speaks of the corner ahead and the corner on your left. The measuring recipe is also compressed into one clause and uses the wording the ball way no longer uses.
- “Regrouped, the difference between the orders compares two copies of the far corner's arrow.”: 'Regrouped' dangles: grammatically it attaches to 'the difference', but it is the four changes that are regrouped. The sentence has to be read twice.
- “That turn is the same whichever way the far arrow points, and no other painted arrow appears in it.”: 'In it' can be the turn or the difference of the orders.
- “On a hillside, you measure the height of the ground at the four corners of a square field. You find how the height changes along the side ahead of you...”: A direction with no reference: the opening question never places the reader, so 'the side ahead of you' and 'the two sides that run to your left' have nothing to hang on.
- “Two arrows at different spots on a ball have no shared wall to compare them with... Different routes can deliver it pointing different ways.”: Spoken on its own, the answer springs a wall on the listener, and 'it' is the copy, which the answer never mentions.
- “the two orders”: An undefined term. The phrase carries the summary, both takeaways, three checks, the entry problem, two misconceptions and both opening questions, but the glossary never defines it, so a reader who meets a check on its own cannot tell what the two orders are.
- “On Earth, ignoring hills, a square covering one square kilometre gives a turn of about 1.4 millionths of a degree.”: A first what-if left open, carried over from the previous review cycle: the reader asks at once why hills are excluded and whether a hill would make the difference noticeable, and nothing answers.
- “A gravity gradiometer compares two, and its output is the relative acceleration per unit separation.”: Climbing the ladder, a step taken on trust, also carried over from the previous cycle: the sentence before says a freely falling accelerometer reads zero, so the reader pictures two zeros being compared and cannot see where a nonzero output comes from.
- “Mark a tiny square on a huge round ball. ... Name the corners as in the hillside field.”: Order of steps. The corner names in the hillside field are fixed by where the reader stands and which side the field is on, so naming them before the reader is placed on the ball leaves a step hanging.

**Fixes**

- Summary: split the first sentence in two and named the two orders in it, so the phrase the rest of the note leans on is introduced where the reader first meets it; 'gets' became 'comes back with', matching the glossary and both ways.
- Hillside way: rewrote the corner naming as three short sentences so no sentence runs two noun phrases together, and replaced the opening question, which used 'a change of a change' before the reader could have met it.
- Ball way: the measuring recipe now names a first and a second corner and ends by saying that the measured angle is the change from the first to the second. Every 'your corner' and 'the neighbouring corner' in the way and in the flat-floor paragraph follows that naming, and the sign rule places the reader at the first corner.
- Ball way: 'Unlike a flat room' now sets up the wall before the ball is said to lack one; the walk around the square is described before its turn is used; the taped-arrow step names where the second angle is measured, says the arrows are carried home to the start, and replaces 'can both obey the rule' with 'Neither arrow swings, so the angle between them stays the same'.
- Ball way: it now opens 'As in the hillside field, stand at one corner of a tiny square on a huge round ball...', so the way it continues is named in its first sentence and the reader is placed before the corner names are carried over.
- Simplifies: 'straight sides' became 'sides walked without steering', which is how the prerequisite ways describe a walk on a curved surface.
- Recap: the small-loop sentence became an instruction with the piece of ball named, and the corner naming matches the hillside way's new three sentences.
- Entry checks: painted-ball-two-orders now places the reader and spells the measuring recipe out in the way's own words, and its answer no longer opens with the dangling 'Regrouped'. two-paintings-one-square says 'in that turn' instead of 'in it'.
- Opening question heights-two-orders now places the reader before using 'the side ahead of you'. The common question why-carry-at-all sets the wall up and names the copy.
- Glossary: added 'the two orders'.
- Added the entry common question would-a-hill-change-it, answering why the Earth number says to ignore hills, with the hilltop number the physics review had already worked out (about half a degree for a 10 metre square over a hilltop curving like a ball of radius 100 metres).
- Working tidal way: replaced 'A gravity gradiometer compares two' with two sentences saying that both masses are measured against one shared reference and the readings subtracted, so that whatever the reference does cancels. This is new working-rung text and needs the physics reviewer's check.
- Budget: entry way explanations were already at 1099 of the 1100 review ceiling, so every fix above had to be paid for. Dropped the hillside way's closing pointer 'For arrows it can, as "Arrows painted on a ball" shows', and dropped the ball way's restatement of the four corner names, since the recap and the hillside way both carry them. Wrote the flat-room setup as the three-word 'Unlike a flat room' rather than a full sentence. Tightened two function-word phrases in the hillside way ('either of them' to 'either', 'The other two sides run' to 'The other two run') to pay for the opening seam; no step, reason or number was removed, and no check answer was touched to save words. Entry explanations now stand at 1099.
- Ladder: every non-entry way still opens by naming the way it continues; index notation appears only from the working rung, after second-covariant-derivative, which has index-notation among its ancestors. The six ways use five kinds and remain distinct routes.
- Revision bumped to 5; status set to novice-reviewed.

**Concerns**

- This is a second full novice pass over a note that had already been signed off at revision 4. The review record from that pass, including its re-read, has been replaced by this one; the physics review record is untouched.
- Physics reviewer: fifteen learner-visible strings changed, fourteen at the entry rung and one at the working rung. The working one is the new gradiometer explanation: two falling masses measured against one shared reference, the readings subtracted, so that any motion of the reference cancels. Please confirm that this describes a gravity gradiometer correctly and is consistent with the atom-interferometer observation. Please also confirm the new entry common question's number: a hilltop curving like a ball of radius 100 metres turns an arrow by about half a degree over a square 10 metres on each side. I get 0.573 degrees from area over radius squared, which matches the hill counterexample already recorded in the physics review.
- review.physics still records reviewed_revision 4 while the note is now at revision 5, so the validator warns that the physics stage has not covered this revision. That warning is the expected signal for the physics diff check and clears when that stage runs; nothing in review.physics was edited.
- Entry way explanations sit at exactly 1100 words, the ceiling a review may use. There is no headroom left at the entry rung. If a later stage must add an explicit step there, something in the two entry explanations has to go; the ball way's 'Here is why' chain is the obvious candidate for a split into its own entry way, which would not by itself reduce the word count.
- Rule 17: the ball way still asks the reader to take in two things, how to measure a change between two arrows at all, and what the two orders then do. The measuring recipe is a tool rather than a second result, and it now ends with a sentence that names what it produces, so the chain reads as one. An editor who sees learners stall should give the measuring recipe its own entry way and question.
- The three visuals are still proposals. The flagship carry-the-far-arrow-home-two-ways should use this note's wording when it is built: round ball, neighbouring arrows point nearly the same way, the corner names start, corner ahead, corner on your left and far corner, the first and second corner of a change, and the turn-left sign rule.
- course-conventions.md still has no torsion row, as both earlier stages reported. It affects only the formal way and the torsion key equation, never entry text.

**Re-read** (2026-09-13, revision 7): 6 stumbles in 2 changed passages

- “A hilltop does, but not every hill.”: Elliptical opener. 'A hilltop does' leaves me to carry the verb over from the question ('change the answer'), and 'but not every hill' has no verb at all. Spoken aloud I heard 'a hilltop does' and waited for the rest.
- “A long even ridge is different.”: 'Even' is doing precise work I cannot decode. I read it as 'smooth' or 'gently sloping', and then the unrolling claim made no sense to me, because a gentle slope and a sharp one both looked like hills. The property that matters is that the ridge keeps the same shape all the way along.
- “Its ground can be unrolled flat onto a table without stretching it, the way a rolled sheet of paper can, and ground like that adds no turn of its own.”: Reread, twice. Thirty words carrying a test, a household comparison and a conclusion at once, spoken without punctuation to lean on. 'Its' is the ridge's, 'it' is the ground, and 'the way a rolled sheet of paper can' asks me to supply 'be unrolled flat'. Ground is not rolled up in the first place, so 'unrolled' arrives before the paper that would explain it.
- “So the millionth-of-a-degree figure is about Earth's roundness alone, on ground that curves no more sharply than Earth does.”: Second word for one idea. The question calls it 'the Earth number' and the ball way calls an angle 'just a number', but this sentence calls it a 'figure'. Spoken, 'figure' also sounds like a shape, which is the wrong picture in a question about hills.
- “A translation of that shared reference, such as vibration of its mounting, enters both readings alike and cancels in the difference, which leaves the relative acceleration of the two masses, quoted per unit separation.”: Working rung, but squeezed: thirty-four words with an inserted example and a trailing 'which' clause whose antecedent is the subtraction rather than any noun. The sentence gained the example clause on the last pass without losing anything, and the result has to be parsed twice to see that the surviving quantity is the answer the instrument reports.
- “A rotation of the reference does not cancel, so its rotation rate has to be controlled or measured and removed.”: 'Controlled or measured and removed' can be read two ways: controlled-or-measured and then removed, or controlled, or else measured and removed. Only the second is the practice being described.
- Fix: Entry, common question would-a-hill-change-it: opener made a full sentence ('A hilltop does change the answer, but not every hill does'), 'a long even ridge' spelled out as 'a long ridge that keeps the same shape all along its length', the thirty-word unrolling sentence split into three with the paper tube put first as something the reader has done, and 'figure' changed to 'number' to match 'the Earth number' in the question. No claim changed: the hilltop still changes the answer, the ridge still adds no turn of its own, and the closing scope is still ground that curves no more sharply than Earth does.
- Fix: Working, way tides-from-swapping-order: the gradiometer common-mode sentence split in two, and a comma plus 'or else' added to the rotation sentence to fix its ambiguous reading. The translation-cancels claim, the rotation-does-not-cancel claim, and 'quoted per unit separation' are unchanged.
- Fix: Budget: entry way explanations untouched at 1099 words, so the part that has no headroom paid nothing. The entry fixes cost 24 words in tutoring (3093 to 3117 of 3300) and the working fixes 3 words in working ways (763 to 766 of 1000). Nothing was dropped or compressed.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Course conventions: Riemann sign and slot order, commutator form, contraction to Ricci, semicolon order, small-loop holonomy, geodesic deviation, orientation and rotation sense.: Read the conventions rows and compared each against every equation, derivation, check and trap in the note. → Every statement matches. [nabla_mu, nabla_nu]V^rho = +R^rho_sigma mu nu V^sigma, R_mu nu = R^rho_mu rho nu, V^rho_;nu mu - V^rho_;mu nu = R^rho_sigma mu nu V^sigma, Delta V^rho = -R^rho_sigma mu nu V^sigma a^mu b^nu, D^2 xi/dtau^2 = -R^mu_nu rho sigma u^nu xi^rho u^sigma. No note-local convention is invented.
- Derivation expand-both-orders, step by step, including the torsion term and the contraction.: Re-expanded nabla_mu(nabla_nu V^rho) as a (1,1) tensor from the conventions covariant-derivative row and subtracted the swapped expression term by term. → Correct. Three groups cancel (commuting partials; the symmetric Gamma-times-first-derivative pair; nothing else), the index correction leaves -(Gamma^l_mu nu - Gamma^l_nu mu) nabla_l V^rho, and the survivor is exactly the course R^rho_sigma mu nu V^sigma. Setting rho = mu gives R^mu_sigma mu nu = R_sigma nu, the contracted form.
- Torsion convention: Tor(X,Y) = nabla_X Y - nabla_Y X - [X,Y] gives Tor^l_mu nu = Gamma^l_mu nu - Gamma^l_nu mu with the derivative index first on Gamma, and the commutator gains -Tor^l_mu nu nabla_l on every tensor including scalars.: Evaluated Tor on coordinate fields; computed [nabla_mu, nabla_nu]f for a scalar directly. → Correct and self-consistent across the formal key equation, the derivation and the formal way. course-conventions.md has no torsion row, so this choice is not covered there; reported as a concern rather than changed.
- Derivation one-term-per-index: scalar symmetry, covector sign, mixed-tensor rule.: Product rule on the scalar omega_rho V^rho, then linearity on U^alpha omega_beta. → Correct: [nabla_mu, nabla_nu]omega_rho = -R^sigma_rho mu nu omega_sigma, plus per upper index and minus per lower one.
- Derivation tidal-drift-from-swapping-order and the geodesic-deviation key equation.: Re-derived each line: u^a nabla_a xi = xi^a nabla_a u from commuting mixed partials and a symmetric connection; product rule; the free-fall line differentiated across the family; index renaming with antisymmetry in the last pair. → Correct. The subtraction leaves u^alpha xi^beta [nabla_alpha, nabla_beta]u^mu = R^mu_sigma alpha beta u^sigma u^alpha xi^beta = -R^mu_nu rho sigma u^nu xi^rho u^sigma, the course form.
- Entry sign chain of 'Arrows painted on a ball': first order minus second order equals the turn of one trip around the square walked ahead first, and that turn is toward the walker's left.: Numerical parallel transport on the unit sphere (python, 200000 steps per side) at colatitude 1.0 with sides of arc length 0.05, ahead = +e_theta, left = +e_phi (outward normal, so e_theta x e_phi = outward). Built the four changes exactly as the way prescribes (carry a copy of the second corner's painted arrow along the side to the first corner; signed angle from the first corner's painted arrow, positive leftward) with a smooth arbitrary painting. → Holonomy of the loop S->A->F->L->S = +0.0025390812 rad, enclosed area = 0.0025390809, ratio 1.0000001. First order = +0.0011883950, second order = -0.0013506858, difference = +0.0025390808, matching the holonomy to 4e-10. Positive, toward the walker's left. The entry claim and its sign are correct.
- Entry claim that the painting drops out of the difference.: Repeated the numerical construction with a completely different smooth painting (a large-amplitude sin-cos pattern). → Difference 0.0025390861 against 0.0025390808, agreeing to 2e-6 relative, the size of the integration and higher-order error. Correct; on an oriented surface holonomy is an SO(2) rotation, so it is the same for every arrow.
- Conventions small-loop row reproduces the same number: Delta V^rho = -R^rho_sigma mu nu V^sigma a^mu b^nu for walking +a, +b, -a, -b.: Fed a = d in theta, b = d_phi in phi, V = d_theta, with R^phi_theta theta phi = -1 on the unit sphere, and converted to an orthonormal rotation angle. → Gives +d^2 = 0.0025 rad toward the walker's left, matching the exact 0.0025391 to order d^3. Sign and magnitude confirmed.
- Working way's bridge: nabla_mu nabla_nu V a^mu b^nu carries the far corner's vector home along -b then -a, the two copies differ by minus Delta V, and the entry first order is nabla_nu nabla_mu V.: Expanded the nested finite differences with transports; the non-far-corner terms are symmetric in a and b and cancel between the orders; identified the residual loop as +b, +a, -b, -a. → Correct: Copy1 - Copy2 = -Delta V = +R^rho_sigma mu nu V^sigma a^mu b^nu = [nabla_mu, nabla_nu]V a b, and [nabla_nu, nabla_mu]V a b = +Delta V, which is the entry first order minus the second. Consistent with the numerical result above.
- Entry hillside arithmetic, both ways and the check.: Hand arithmetic: (16,13,11,10) and (35,26,23,20). → Way: 5 - 3 = 2 and 3 - 1 = 2, and 16 + 10 - 13 - 11 = 2. Check: 12 - 6 = 6 and 9 - 3 = 6, and 35 + 20 - 26 - 23 = 6. The regrouping is exact for any four numbers.
- Entry number: 1 square kilometre on Earth turns an arrow by about 1.4 millionths of a degree, a hair's width seen from 3 kilometres.: python with R = 6371 km: A/R^2. → 2.4637e-8 rad = 1.4116e-6 deg, subtending 73.9 micrometres at 3 km, a typical hair. Correct.
- Entry problem ten-kilometre-square: 100 square kilometres, about 140 millionths of a degree, about one seven-thousandth of a degree.: python: 100e6/R^2 in degrees, then its reciprocal. → 1.4116e-4 deg and 1/7084 deg. The stored numeric 0.000141 with rel_tol 0.05 holds. Correct.
- New entry common question: a hilltop curving like a ball of radius 100 metres turns an arrow by about half a degree over a 10 metre square.: python: 100 m^2 / (100 m)^2 = 0.01 rad. → 0.5730 degrees. Correct. But 'A hill changes it a lot' was false for an evenly sloping hillside or a long ridge, which is intrinsically flat; fixed.
- Check two-paintings-one-square: both friends find 3 millionths of a degree.: Checked internal consistency, not an Earth number: the check names a 'huge round ball', not Earth. → Consistent; 3e-6 deg = 5.24e-8 rad, a tiny square on a ball a few thousand kilometres across. Painting-independence confirmed numerically above.
- Worked example both-orders-on-the-sphere: sin^2 theta and 0, and the claim about dropping the index corrections.: Hand computation of all four first derivatives and both second derivatives from Gamma^theta_phi phi = -sin theta cos theta and Gamma^phi_theta phi = cot theta; independent computation of R^theta_phi theta phi from the conventions Riemann row. → nabla_theta nabla_phi V^theta = -cos 2theta + cos^2 theta = sin^2 theta; nabla_phi nabla_theta V^theta = -cos^2 theta + cos^2 theta = 0; R^theta_phi theta phi = sin^2 theta. Dropping the index corrections gives -cos 2theta and -cos^2 theta, whose difference is still sin^2 theta. All correct.
- Problem fields-that-agree-at-a-point: commutator components (sin^2 theta, -(theta - theta_0)).: Hand computation of the four nabla_nu W^rho and both components of the commutator; independent computation of R^phi_theta theta phi from the conventions Riemann row. → theta component -cos 2theta + cos^2 theta = sin^2 theta; phi component cot theta - s csc^2 theta + s cot^2 theta - cot theta = -s, using cot^2 - csc^2 = -1. R^phi_theta theta phi = -csc^2 theta + cot^2 theta = -1, so R^rho_sigma theta phi W^sigma = (sin^2 theta, -s). Correct everywhere, and at theta_0 it matches V despite nabla_theta W^theta = 1.
- Problem gradiometer-in-orbit: r = 6626 km, R^z_0z0 = -3.05e-23 m^-2, relative acceleration 1.37e-6 m/s^2 over 0.50 m, and the sign (the masses separate).: python with GM = 3.986e14, c = 2.99792458e8; sign from the weak static field g_00 = -(1 + 2Phi/c^2), Gamma^i_00 = d_i Phi/c^2, R^i_0j0 = d_i d_j Phi/c^2 with Phi = -GM/r. → GM/r^3 = 1.3702e-6 s^-2, 2GM/r^3 = 2.7404e-6 s^-2, R^z_0z0 = -3.0491e-23 m^-2, relative acceleration 1.3702e-6 m/s^2. Radial separation grows, so the positive sign is right. Both stored numerics hold within rel_tol 0.02, and the signed R^z_0z0 is negative as recorded.
- Observation atom-gravity-gradiometer: 2GM/R^3 = 3.08e-6 s^-2 at the surface, R^z_0z0 = -3.43e-23 m^-2, free-air gradient 3.086e-6 s^-2; and the working way's 3.1 micrometres per second squared per metre.: python with R = 6371 km; compared with the standard free-air correction 0.3086 mGal/m. → 3.0828e-6 s^-2 and -3.4301e-23 m^-2; 0.3086 mGal/m = 3.086e-6 s^-2. All correct, and the idealised and standard values are quoted as separate numbers, not equated.
- Check inertial-frame-claim: at a point where all Christoffel symbols vanish the commutator is still R^rho_sigma mu nu V^sigma.: Expanded nabla_mu nabla_nu V^rho at such a point and antisymmetrised. → Correct: the undifferentiated Gamma terms and the Gamma-Gamma products drop, leaving (d_mu Gamma^rho_nu sigma - d_nu Gamma^rho_mu sigma)V^sigma = R^rho_sigma mu nu V^sigma there, and both sides are tensors.
- Check covector-sign: the value is +1, with the stated direct values csc^2 theta + cot^2 theta and 2 cot^2 theta.: Hand computation of nabla_nu omega_rho and both second derivatives for omega = d phi on the unit sphere. → nabla_theta nabla_phi omega_theta = csc^2 theta + cot^2 theta, nabla_phi nabla_theta omega_theta = 2 cot^2 theta, difference csc^2 - cot^2 = 1. The rule -R^sigma_rho mu nu omega_sigma gives -R^phi_theta theta phi = +1. Correct.
- Check metric-commutator: antisymmetry of the Riemann tensor in its first pair.: Applied the one-term-per-index rule to g_rho sigma and lowered indices. → -R_sigma rho mu nu - R_rho sigma mu nu = 0, so R_rho sigma mu nu = -R_sigma rho mu nu. Correct, and the remark that small-loop changes are rotations or boosts follows.
- Check polar-frame-bracket on the flat plane: unbracketed difference -r^-2 e_phi, bracket term the same, curvature zero.: Hand computation with Gamma^r_phi phi = -r and Gamma^phi_r phi = 1/r; [d_r, r^-1 d_phi] = -r^-2 d_phi. → nabla_Y X = r^-2 d_phi, nabla_X nabla_Y X = -r^-3 d_phi = -r^-2 e_phi, nabla_X X = 0, nabla_[X,Y] X = -r^-3 d_phi. R(X,Y)X = 0, as a flat plane requires. Correct.
- Check no-parallel-field-on-a-sphere and the two-dimensional form R^rho_sigma mu nu = K(delta^rho_mu g_sigma nu - delta^rho_nu g_sigma mu).: Verified the form against the unit sphere components (sin^2 theta and -1), then contracted the parallel-field condition. → Correct; contracting rho with mu gives K V_nu = 0, so a nonzero parallel field forces K = 0. On a sphere of radius a, K = 1/a^2, so V = 0.
- Problem operator-from-components: R(X,Y)Z = X^mu Y^nu [nabla_mu, nabla_nu]Z and the failure of function-linearity without the bracket.: Expanded nabla_X(nabla_Y Z) with the product rule and used [fX,Y] = f[X,Y] - (Yf)X. → Correct: the derivative terms appear only as nabla_{nabla_X Y - nabla_Y X}Z, which zero torsion turns into nabla_[X,Y]Z; replacing X by fX adds -(Yf)nabla_X Z to both the unbracketed difference and nabla_[fX,Y]Z, so only R is function-linear.
- Formal consequences: the flatness criterion, the wave-equation Ricci term, the cyclic identity from a gradient, and the second Bianchi identity from the Jacobi identity.: Raised the contracted identity using the symmetry of the Ricci tensor; took the cyclic sum of [nabla_mu, nabla_nu]nabla_lambda f. → nabla_nu nabla^mu A^nu - nabla^mu nabla_nu A^nu = R^mu_sigma A^sigma is correct. The cyclic sum of the left side vanishes by the symmetry of nabla_mu nabla_nu f, giving R^sigma_[lambda mu nu] = 0. All hypotheses (torsion-free, simply connected for the parallel extension) are stated.
- Notation traps: semicolon order, the plus-sign covector form, and the Riemann sign calibration.: Compared with the conventions comma-and-semicolon row; checked R_rho^sigma_mu nu = -R^sigma_rho mu nu using first-pair antisymmetry. → All three correct, including 'for a metric connection the two agree' and the sphere calibration R^theta_phi theta phi = sin^2 theta.
- References: Snadden et al. 1998 PRL 81, 971-974; Ricci-Curbastro and Levi-Civita 1900 Math. Ann. 54, 125-201; Levi-Civita 1917 Rend. Circ. Mat. Palermo 42, 173-204; Raychaudhuri 1955 Phys. Rev. 98, 1123-1126; Penrose 1965 PRL 14, 57-59; Bochner 1946 Bull. AMS 52, 776-797; Yang and Mills 1954 Phys. Rev. 96, 191-195.: Crossref API lookup of each DOI (title, authors, container, volume, pages, year), plus a web search for the Levi-Civita page range, which is cited as both 173-204 and 173-205 in secondary sources. → All seven confirmed: titles, author lists, journals, volumes, page ranges and years match, and Crossref gives 173-204 for the Levi-Civita paper, as the note has. All remain verified true. Crossref stamps that issue December 1916; the paper is universally cited as 1917 and the note keeps 1917.
- History scope: Ricci and Levi-Civita 1900 set out the absolute differential calculus and the exchange rule carries Ricci's name; Levi-Civita 1917 introduced parallel transport through a Euclidean embedding and then showed it depends only on the metric.: Checked both claims against the standard record of the two papers. → Both correctly scoped. Neither claims priority for the identity itself, and the 1917 entry names the embedding route, which is what the paper actually does.
- Bochner and Raychaudhuri horizon statements.: Checked Bochner's two theorems (closed manifold, definite Ricci sign) and the Raychaudhuri equation with its rotation and shear terms. → Bochner correct as stated. The focusing sentence overstated the conclusion: an energy condition with zero rotation makes the expansion decrease monotonically, and only a bundle already converging reaches a caustic in finite parameter. Fixed.
- Structure: prerequisites direct and acyclic, assumes consistent, justified_by at or below rung, objective and check links, formal-rung count.: Checked every id against the domain registries and every internal address against the target notes; counted formal items. → All ids resolve (including holonomy/key_equations/small-loop-law and riemann-curvature-tensor/ways_in/a-table-of-turns). No assumes id appears in leads_to. Every check and problem evidences an objective, targets and diagnosed_by agree, and the core tier's requirement of two formal checks and one formal problem is met. No field mentions a source book.

**Counterexamples tried**

- Bent but flat surface (a rolled sheet, a long even ridge, an evenly sloping hillside): holonomy around a contractible loop is exactly zero, so the new entry common question's 'A hill changes it a lot' was false for that shape. Rewritten to say a hilltop does but a long even ridge does not, with the unrolling test as the reason.
- Flat floor: both orders agree. Stated in the ball way, its takeaway, the summary and the painted-ball check; confirmed numerically (all transport angles vanish in a Cartesian frame).
- Saddle: K < 0, so the difference is negative, a turn to the walker's right. The entry text speaks only of a ball, and the flagship visual's sketch already shows the saddle turning right. Consistent.
- Reversed walking sense, or starting from a different corner: this swaps the two orders and flips the sign. Both entry ways, both entry checks and both opening questions now fix the corner and the sense ('the start', 'with the square on your left'), so nothing is left ambiguous.
- Non-square quadrilateral, and a square whose sides are not walked without steering: the argument uses only four side paths, never right angles or geodesics, and holonomy equals the integral of K over the region for any simple loop. The simplifies claim stands; checked numerically on a coordinate quadrilateral, which is not geodesic, with ratio 1.0000001.
- Angles near half a turn (a wildly swirling painting on a large square): measured angles can wrap and the difference can be off by a whole turn. Excluded by 'neighbouring arrows point nearly the same way' in the way, the checks and the simplifies.
- Region bigger than half the ball: the turn exceeds half a turn and the quoted branch matters. Excluded by 'tiny square' and 'small loop' everywhere in the entry text.
- Cone tip: the identity is pointwise and holds away from the tip, where the curvature is concentrated; the formal limits paragraph says so and the tip appears only in holonomy.
- Non-coordinate frame (the polar frame on a flat plane): a nonzero unbracketed difference with zero curvature. Covered by the formal frames paragraph, the formal check and the misconception any-fields-commutator-is-curvature.
- Connection with torsion: the commutator gains -Tor^l_mu nu nabla_l even on scalars, so scalars no longer commute. Stated in the formal key equation and the formal way; the torsion-free hypothesis appears in every conditions field that needs it.
- Rotating reference for the gradiometer: a translation of the shared reference is common to both readings and cancels, but a rotation is not, so 'Any motion ... cancels' was false. Fixed, with the rotation caveat added.
- Orbiting rather than static observer for the tidal number: the correction to the radial tidal component is of order GM/(rc^2) ~ 1e-9, far below the quoted two figures.
- Non-relativistic limit and massless case for the tidal statements: the geodesic deviation equation is quoted with proper time and a four-velocity, so it is scoped to timelike worldlines; the null case appears only in the research horizon, where 'affine parameter' is now named alongside proper time.
- Rotating congruence in the Raychaudhuri statement: vorticity opposes focusing, so the horizon sentence keeps 'without rotation' and no longer claims convergence without an initially converging bundle.

**Fixes**

- Tidal way (working): 'Any motion of that shared reference enters both readings alike and cancels in the difference' became 'A translation of that shared reference, such as vibration of its mounting, enters both readings alike and cancels in the difference', with a new sentence saying that a rotation of the reference does not cancel and its rotation rate has to be controlled or measured and removed. The old sentence was a false universal: common-mode rejection covers translation, not rotation.
- Entry common question would-a-hill-change-it: 'A hill changes it a lot' became 'A hilltop does, but not every hill', and a long even ridge was added as the case that can be unrolled flat onto a table and adds no turn of its own; the closing scope became 'on ground that curves no more sharply than Earth does' instead of 'on ground with no hills'. The half-degree hilltop number is unchanged and recomputed as 0.5730 degrees.
- Research horizon focusing-and-singularities: 'an energy condition then forces nearby worldlines or light rays to converge' became 'an energy condition makes the expansion decrease monotonically, so a bundle of worldlines or light rays that is already converging reaches a caustic within finite proper time or affine parameter'.
- No equation, derivation step, number, tolerance or check answer needed correction. Nothing was dropped: the entry way explanations stayed at 1099 words, working grew from 737 to 763, tutoring from 3051 to 3093 and links from 681 to 699, all inside their caps.
- review.physics was rewritten for this pass; the record it replaces covered revision 4 and its diff-check step was superseded by the second novice pass.

**Concerns**

- course-conventions.md still has no torsion row. The note uses Tor^l_mu nu = Gamma^l_mu nu - Gamma^l_nu mu, which is the only choice consistent with the file's derivative-index-first covariant derivative and with Tor(X,Y) = nabla_X Y - nabla_Y X - [X,Y]; an editor should add the row so the formal way and the torsion key equation rest on the file rather than on this note.
- All three visuals (carry-the-far-arrow-home-two-ways, cross-off-matching-terms, falling-ring-of-crumbs) are still proposals with sketches. falling-ring-of-crumbs is proposed by eighteen notes and should be built first; the flagship carry-the-far-arrow-home-two-ways is unique to this note and its sketch already carries the correct saddle sign.
- Entry has no headroom: entry way explanations stand at 1099 words against a 1000 cap plus the 10 per cent review allowance of 1100. Any later stage that must add an explicit step at entry will have to drop something, and the ball way is the only place with a droppable item.
- Rule 17 remains open for an editor, unchanged from the novice pass: the ball way carries both the measuring recipe and the two-orders result. It is now one chain, but if learners stall the recipe should become its own entry way and question.
- The novice pass must re-read exactly two changed strings: the hill common question's answer (entry) and the gradiometer sentences in the tidal way (working).

**Diff check** (2026-09-13, revision 7)

- Scope of the check: the novice re-read changed exactly two learner-visible strings, the entry common question would-a-hill-change-it and the working way tides-from-swapping-order.: note_diff.py between the pre-reread snapshot and the current note, then read both fields whole and compared each new sentence with the sentence it replaces. → Two strings, six changed or added sentences. Every one is a wording change. No number, equation, unit, tolerance, condition, sense, branch, frame or scope word differs from the text the revision 6 physics pass approved.
- 'A hilltop does change the answer, but not every hill does' claims what 'A hilltop does, but not every hill' claimed.: Supplied the elided verbs from the question and compared the two readings; then tested the positive half on a smooth summit whose Hessian is degenerate, z = -x^2 - y^4, with K = (f_xx f_yy - f_xy^2)/(1 + f_x^2 + f_y^2)^2. → Same claim. The positive half holds even in the degenerate case: K = 0 only on the line y = 0 and K > 0 off it (0.222 at (0.1, 0.1), 0.958 at (0, 0.2)), so the integral of K over any small square about a strict local maximum is positive. The negative half stays existential, so the saddle of a mountain pass, which turns an arrow the other way, is not a counterexample.
- 'A long ridge that keeps the same shape all along its length' names the same surface class as the old 'A long even ridge', namely the bent-but-flat class already recorded in this review's counterexamples.: Wrote the class as a graph z = f(x) with no dependence on the length direction and computed K from the graph formula at several points of a sample ridge, z = 5 exp(-x^2/10). → K = 0 at every point (x = 0, 1, 3), because f_yy and f_xy vanish identically. The new wording names the defining property, translation of one cross-section along the length, where 'even' named none, so it is if anything tighter. A ridge whose crest curves is outside the class, and the paper test the answer gives is the discriminator that excludes it.
- The three split sentences 'Roll a sheet of paper into a tube, and you can still lay it flat again without stretching it. The ground on such a ridge can be laid flat in the same way. Ground like that adds no turn of its own' say what the old thirty-word sentence said.: Compared clause by clause with the old sentence and checked that 'in the same way' still carries 'without stretching it'; checked the developability claim by arclength reparametrization of the cross-section. → Same three claims, in the order test, application, conclusion. A generalized cylinder is isometric to a strip of the plane under s = integral of sqrt(1 + f'^2) dx, so laying it flat without stretching is exact, and zero K over the region gives exactly zero turn. The paper tube now arrives before it is applied, which removes the old forward reference without weakening anything.
- 'the millionth-of-a-degree number' (was 'figure') still points at the note's Earth number, and that number is right.: Recomputed the entry way's value: K = 1/a^2 with a = 6371 km, area 1 square kilometre, turn = K times area. → 1.41 millionths of a degree, so 'about 1.4 millionths of a degree' and 'the millionth-of-a-degree number' both stand. The hilltop number in the same answer recomputes to 0.5730 degrees for a 10 metre square on a dome of radius 100 metres, unchanged.
- Splitting the gradiometer sentence into 'cancels in the difference' and 'What is left is the relative acceleration of the two masses, quoted per unit separation' keeps the old claim and its units.: Compared with the old relative clause; checked the units of a difference of two accelerations divided by a separation against the number quoted later in the same way. → Same claim. Common-mode translation of the shared housing enters both readings identically and drops out of the difference; the difference divided by the separation has units of inverse seconds squared, matching 3.08e-6 per second squared and 3.1 micrometres per second squared at 1 metre, both recomputed from 2GM/r^3. 'What is left' is not overstated, because the very next sentence names rotation as the part that does not cancel, exactly as the old 'which leaves' clause did.
- 'its rotation rate has to be controlled, or else measured and removed' is the true reading of the ambiguous 'controlled or measured and removed'.: Parsed both readings, then sized the term that survives: a reference rotating at rate Omega contributes centrifugal and angular-acceleration terms proportional to the separation, of order Omega^2, which therefore live in the gradient rather than in the common mode. → The chosen reading is the physical one: either hold the rotation rate fixed and known, or measure it and subtract its contribution. The term is real and not negligible: Earth's sidereal rate gives Omega^2 = 5.3e-9 per second squared against a signal of 3.08e-6, a fraction of 0.17 per cent, which is thousands of times a gradiometer's resolution.
- Consistency with the rest of the note and with course conventions after the rewording.: Re-read both changed fields whole and against the ways they cite, checked the new words 'roll', 'tube', 'number' and 'laid flat' for a second sense elsewhere in the note, and re-ran the validator. → Consistent. No sense or branch statement is touched, so the conventions rows on rotation sense and small-loop holonomy are unaffected. 'Flat' still describes surfaces only, 'roll' and 'tube' occur nowhere else, and 'number' matches 'the Earth number' in the question the answer serves. No math entered a spoken field.
- Fix: No fix was needed. All six changed sentences are true within their stated scope at their rung and claim exactly what the text they replace claimed, so no learner-visible text was edited and the note stays at revision 7. review.physics.reviewed_revision moves from 6 to 7.
- Fix: Noted for an editor, no change made: the unchanged sentence 'The turn a loop gives an arrow depends on how sharply the ground curves over the piece the loop goes round' uses 'curves' in the intrinsic sense, while the ridge that follows visibly curves and adds no turn. The answer resolves this with the paper test, and the revision 6 pass approved the sentence, so touching it now would restart the review loop for no accuracy gain. If an editor ever splits this answer into two common questions, the ridge half is the place to say that a curve you can see and a curve that turns arrows are different things.
