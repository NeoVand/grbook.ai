---
type: "concept"
schema_version: 2
id: "path-dependence-of-parallel-transport"
title: "Path dependence of parallel transport"
tagline: "Why arrows carried to one spot by different routes can disagree"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 9
updated: "2026-09-13"
aliases: ["route dependence of parallel transport", "non-integrability of parallel transport"]
prerequisites: ["parallel-transport", "curvature", "christoffel-symbols", "four-momentum", "levi-civita-connection", "simply-connected-space"]
leads_to: ["holonomy", "riemann-curvature-tensor", "flatness-criterion", "integrability-condition-for-parallel-fields", "global-energy-momentum-conservation"]
visuals: ["carry-an-arrow-around-a-loop", "light-through-a-coiled-fibre", "painted-arrows-that-must-match", "two-grids-on-one-playground"]
---

# Path dependence of parallel transport

*Why arrows carried to one spot by different routes can disagree*

`path-dependence-of-parallel-transport` · curvature · core · physics-reviewed (revision 9)

**Needs:** [[parallel-transport]] (entry) · [[curvature]] (entry) · [[christoffel-symbols]] (working) · [[four-momentum]] (working) · [[levi-civita-connection]] (formal) · [[simply-connected-space]] (formal)  
**Opens:** [[holonomy]] · [[riemann-curvature-tensor]] · [[flatness-criterion]] · [[integrability-condition-for-parallel-fields]] · [[global-energy-momentum-conservation]]  
**Related:** [[angular-excess]] · [[intrinsic-versus-extrinsic-curvature]] · [[nonzero-christoffel-symbols-in-flat-space]] · [[local-inertial-frame]] · [[torsion-tensor]] · [[gauge-parallel-transport]]  
**Visuals:** ★ [[carry-an-arrow-around-a-loop]] · [[light-through-a-coiled-fibre]] · [[painted-arrows-that-must-match]] · [[two-grids-on-one-playground]]

> Two friends start together with matching arrows and carry them to the same spot by different routes, never letting the arrows swing. On a flat floor the arrows always arrive matching. On a ball they can arrive pointing different ways, a quarter turn apart for one pair of routes. So on a ball, whether two distant arrows point the same way has no single answer: it can depend on the route along which one is carried to the other.

## You will be able to

**Entry**
- Explain why two matching arrows carried to one spot by different routes can arrive pointing different ways on a ball, but not on a flat floor. `objectives/explain-routes-can-disagree` ← `checks/pole-route-prediction`, `checks/equator-the-long-way`, `problems/tube-two-ways`
- Estimate how far apart the arrows arrive from the fraction of the ball between the routes. `objectives/estimate-disagreement-from-the-piece` ← `checks/one-sixteenth-of-the-ball`

**Working**
- Compute, with its sense, the mismatch between two sphere routes made of meridians and circles of latitude. `objectives/compute-mismatch-on-a-sphere` ← `checks/latitude-strip-on-earth`, `problems/small-rectangle-matches-formula`
- Distinguish changing components of a carried vector from genuine path dependence. `objectives/distinguish-components-from-vectors` ← `checks/polar-components-change`
- Explain why four-momenta at separated events in curved spacetime have no invariant sum. `objectives/explain-no-invariant-sum` ← `checks/adding-two-momenta`

**Formal**
- State when zero curvature makes transport route independent, prove the sufficiency half, and break a hypothesis with a counterexample. `objectives/state-integrability-with-hypotheses` ← `checks/cone-opposite-sides`, `problems/homotopy-cells-give-path-independence`
- Explain why a two-route mismatch in spacetime is a Lorentz transformation that can include a boost. `objectives/identify-lorentz-mismatch` ← `checks/boost-between-routes`

## Ways in

### 1. Two routes to one spot · entry · picture

*If two arrows start matching and are carried to the same spot by different routes, will they arrive matching?*

**Recap:** Carrying an arrow means pressing a cardboard arrow against the ground as you walk, and never letting it swing to your left or right. At a corner you turn your body but leave the arrow alone. Walking without ever steering left or right is called walking straight.

Picture a huge, smooth ball. Seen from outside, as on a globe, call its top point the North Pole and the circle around its middle the equator.

Two friends stand together at a spot on the equator. Each presses a cardboard arrow against the ground. The two arrows match: one lies on top of the other, pointing the same way. Both point along the equator, toward a meeting spot a quarter of the way around the ball.

The equator is a straight walk. So is each line in the evenly spaced set a globe draws from the North Pole to the equator. For the equator and these lines, the ball on one side is a mirror image of the ball on the other side. A walker on one of them therefore has no reason to steer either way.

Neither friend ever lets her arrow swing. While a friend walks straight she never steers either, so her arrow keeps the same angle to her route.

The first friend walks along the equator to the meeting spot. Her arrow points ahead of her the whole way. It arrives pointing along the equator, away from the start.

The second friend turns her body to face the North Pole and leaves her arrow alone. Say the meeting spot is then on her right. Her line to the North Pole crosses the equator at a right angle, as any globe shows. The arrow lies along the equator, so it points to her right.

She walks straight to the North Pole, and the arrow stays on her right. The line from the North Pole to the meeting spot stays on her right too, because she never steers.

At the North Pole, the two lines meet at a right angle. Think of an orange cut from top to bottom into four equal segments. Neighbouring cuts are a quarter of the way apart around the middle, and they meet at the top at a right angle. The meeting spot's line is on her right, so she turns right by a quarter turn to face along it.

Her arrow was on her right. She turned her body a quarter turn to the right and left the arrow alone, so now the arrow points ahead of her. It keeps pointing ahead as she walks straight to the meeting spot. It arrives pointing along her route, away from the North Pole.

At the meeting spot, compare the arrows. One points along the equator. The other points along the line from the North Pole, which crosses the equator at a right angle. So the arrows arrive a quarter turn apart, although neither ever swung.

On a flat floor this never happens. An arrow that never swings keeps pointing at the same wall of the room, whatever route it takes. Two arrows that start matching therefore always arrive matching.

Carrying an arrow without letting it swing is called parallel transport.

On a ball, where a carried arrow ends up pointing can depend on the route. This is called path dependence, where path means the same as route.

Path dependence changes what pointing the same way can mean. On a ball, no wall can tell you that two distant arrows point the same way, because arrows carried to one spot by different routes can arrive pointing different ways. To compare two distant arrows, you must carry one to the other, and the answer can depend on the route.

**Try it:** Set an orange on a table. Stretch a rubber band around its middle, level with the table. Stretch two more bands over the top, crossing there at a right angle. Each of these two bands crosses the middle band at two places. Pick one place where the first band crosses it, and call it the start. A quarter of the way around the middle band from the start, the second band crosses it; call that place the meeting spot. At the start, lay two matchsticks together along the middle band, pointing toward the meeting spot. Slide one along the middle band to the meeting spot. Slide the other up the first band to the top, then down the second band to the meeting spot. Keep each matchstick at the same angle to the band it is on, and do not twist it where it changes bands. At the meeting spot the two matchsticks lie at a right angle.

**Takeaway:** Two arrows that start matching and are carried to one spot by different routes always arrive matching on a flat floor, but on a ball they can arrive pointing different ways.

*Builds on:* [[parallel-transport]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `two-routes`)<br>*See:* `checks/pole-route-prediction`

### 2. The disagreement follows the piece between the routes · entry · calculation

*How far apart do the arrows arrive, and why does nobody notice it on Earth?*

**Recap:** Two friends start at one spot on the equator of a ball, the circle around its middle, with matching arrows. They carry them to a meeting spot a quarter of the way around the equator without letting them swing. One walks straight along the equator. The other walks straight to the North Pole, the ball's top point seen from outside, and then straight to the meeting spot. The arrows arrive a quarter turn apart.

In "Two routes to one spot", the friends' routes met only at their two ends. Together they cut the ball into two pieces. The smaller piece has the equator from the start to the meeting spot along one edge, and the two lines from the North Pole along the others. Call it the piece between the routes.

That piece is one eighth of the ball. The equator cuts the ball into two halves, and the piece lies in the half with the North Pole. The two lines from the North Pole reach the equator a quarter of the way apart, so the piece is one quarter of that half. One quarter of one half is one eighth.

The angle between two arrows at one spot is how much they disagree. For the friends it was a quarter turn.

Now a third friend takes a middle route from the same start. She walks straight to the North Pole. From there she walks straight to the equator, halfway between the start and the meeting spot. At the equator she turns and walks along it to the meeting spot.

The middle route splits the one-eighth piece into two halves. The halves are exact copies of each other, one turned around the ball from the other. Suppose the disagreement is set by the piece between two routes. The ball is the same everywhere, so each half gives the same disagreement, toward the same side.

At the meeting spot, the first friend's arrow and the third friend's arrow disagree by some amount. The third friend's arrow and the second friend's arrow disagree by the same amount again, toward the same side. Together these make the quarter turn, so each half of the piece gives an eighth of a turn.

Splitting pieces again and again points to a rule. Take two routes that meet each other only at their ends. Neither route may cross itself, because that would cut the ball into more than two pieces. Of the two pieces between the routes, let the smaller be at most a quarter of the ball. The disagreement, in full turns, is twice that fraction. One eighth of the ball gives two eighths, a quarter turn, as the friends found.

Splitting shows this rule only for pieces cut like orange segments, so for other shapes take it on trust here. The limit of a quarter of the ball keeps the answer at most a half turn, the most two arrows can disagree.

Earth is nearly a smooth ball, with a surface of about 510 million square kilometres. Take two routes that meet only at their ends, neither crossing itself, with one square kilometre between them, about 140 football pitches. That piece is one part in 510 million of Earth's surface. The arrows therefore disagree by two parts in 510 million of a full turn.

A full turn is 360 degrees, so the disagreement is 720 degrees divided by 510 million, about 1.4 millionths of a degree. That is the angle across a hair's width seen from 3 kilometres away. Nobody notices it on a walk.

**Takeaway:** For routes that meet only at their ends, neither crossing itself, with up to a quarter of the ball between them, the arrows disagree by twice that fraction of a turn. On Earth, one square kilometre gives about 1.4 millionths of a degree.

*Continues:* `ways_in/two-routes-to-one-spot`<br>*See:* `checks/one-sixteenth-of-the-ball`

### 3. Two orders around a small cell · working · calculation

*What sets the mismatch between two routes, in components, and how large is it for finite routes on a sphere?*

In "The disagreement follows the piece between the routes", the mismatch between two routes grew with the piece of ball between them: twice the fraction of the ball, in full turns. A sphere of radius $a$ has area $4\pi a^2$ and a full turn is $2\pi$ radians, so a piece of area $A$ gives $2 \cdot (A/4\pi a^2) \cdot 2\pi = A/a^2$ radians. To compute the mismatch anywhere, write parallel transport along a curve $x^\mu(s)$ in components:

$$\frac{dV^\rho}{ds} + \Gamma^\rho{}_{\mu\sigma}\frac{dx^\mu}{ds}V^\sigma = 0.$$

Given the route and the starting vector, this linear differential equation fixes the carried vector uniquely. A different route to the same endpoint is a different equation, so nothing forces the same answer.

Take the smallest pair of routes: the two ways around a coordinate parallelogram with edges $a^\mu$ and $b^\mu$. One route steps along $a$ and then $b$; the other steps along $b$ and then $a$. Both end at $x + a + b$, so their results can be subtracted in the coordinate basis there. The derivation "Two routes around a small cell" expands each step to second order and finds

$$V^\rho_{(a\ \text{first})} - V^\rho_{(b\ \text{first})} = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu,$$

where $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$ is the Riemann curvature tensor, studied in its own right in its own note.

- The first-order terms cancel, so nearby routes disagree only at second order.
- The mismatch is linear in $V$ and in each edge, and swapping $a$ and $b$ flips its sign.
- It scales with the cell's area, like the piece-of-the-ball rule.
- It is a tensor, so it vanishes for a flat metric in any coordinates, however curved the coordinate lines.

Finite routes can be solved exactly. On the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, where the colatitude $\theta$ is the angle from the North Pole, go from colatitude $\theta_1$ to $\theta_2 > \theta_1$ and through $\Delta\phi > 0$ in longitude, along the meridian first or along the circle of latitude first. The derivation "Meridian first or latitude first" shows that the meridian-first vector is the latitude-first vector rotated by $\Delta\phi(\cos\theta_1 - \cos\theta_2)$, counterclockwise seen from outside the sphere. That is the area between the routes, for routes of any size; on a sphere of radius $a$ the rotation is that area divided by $a^2$.

**Takeaway:** Two routes around a small cell disagree by minus the Riemann tensor acting on the vector and the two edges; on a sphere, meridian and latitude routes of any size disagree by the enclosed area over the radius squared.

*What this leaves out:* Coordinates on one chart; the comparison is made at the shared endpoint, never at separate points.

*Continues:* `ways_in/size-follows-the-piece`<br>*Builds on:* [[christoffel-symbols]]<br>*See:* `derivations/two-routes-around-a-cell`, `derivations/meridian-or-latitude-first`, `worked_examples/quarter-sphere-strip`

### 4. Light in a coiled fibre compares two routes · working · operational

*Where can an instrument actually measure a mismatch between two routes on a curved surface?*

The two routes to one spot in "Two routes to one spot" need a curved surface, and every optics lab has one: the sphere of directions. Each direction in space is a point on a unit sphere. Light guided by a single-mode optical fibre travels along the unit tangent $\hat t(s)$, which traces a route on that sphere as the fibre bends.

If stress-induced birefringence is negligible, bending does not twist the light's linear polarization about $\hat t$. The polarization vector $\mathbf e$ stays perpendicular to $\hat t$, so it is a tangent vector to the sphere of directions at $\hat t$, and it changes only as much as staying perpendicular requires:

$$\frac{d\mathbf e}{ds} = -\Big(\mathbf e\cdot\frac{d\hat t}{ds}\Big)\hat t.$$

This keeps $\mathbf e\cdot\hat t = 0$ and $|\mathbf e|$ fixed, and it is parallel transport on the unit sphere; its derivation from Maxwell's equations is taken on trust here.

Now compare two fibres with the same entry and exit directions. In a straight fibre, $\hat t$ stays at one point of the sphere. In a uniform helix whose fibre makes angle $\vartheta$ with the helix axis, $\hat t$ circles that axis at angular radius $\vartheta$ and returns after each winding. Launch the same linear polarization into both. A polarimeter at the exits finds them rotated relative to each other by the solid angle of that circle, the area it encloses on the unit sphere, $2\pi(1 - \cos\vartheta)$ per winding, modulo $2\pi$, with the sense set by the helix's handedness. For $\vartheta = 30^\circ$ that is $48.2^\circ$ per winding, whatever the helix's radius.

**Takeaway:** Polarization carried along a bent fibre is parallel transport on the sphere of directions, so two fibres with the same ends can deliver differently rotated polarization.

*What this leaves out:* Ideal single-mode fibre with no birefringence; the sphere of directions stands in for a curved space and involves no gravity.

*Continues:* `ways_in/two-routes-to-one-spot`<br>*Visuals:* [[light-through-a-coiled-fibre]]<br>*See:* `observations/coiled-fibre-polarization`

### 5. No grid of parallel axes, no total momentum · working · contrast

*What does special relativity take for granted that path dependence takes away?*

On the flat floor of "Two routes to one spot", every route delivered the same arrow. The flat spacetime of special relativity behaves the same way, and the theory quietly relies on this route independence twice. Both uses fail wherever the two-route mismatch of "Two orders around a small cell" is nonzero.

First, a grid. Carry a set of orthonormal axes from one event to every other. In that spacetime the carried axes form a single-valued field of parallel axes: a global inertial frame. In a curved region, different routes deliver differently oriented axes, so the construction is multivalued. Even one parallel vector field requires $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$, and a full parallel frame requires $R^\rho{}_{\sigma\mu\nu} = 0$. Only local inertial frames survive.

Second, sums. In special relativity a system's total four-momentum is $P^\mu = \sum_i p^\mu_{(i)}$, with each $p_{(i)}$ at its own event. The sum makes sense because every vector reaches a common event with no choice of route. In curved spacetime each $p_{(i)}$ lives in the tangent space at its own event. Adding them requires routes to a common event, and the total depends on those routes, by amounts set by the curvature between them. So there is no invariant sum. A total energy and momentum needs extra structure: a symmetry of the spacetime, or an isolated system seen from nearly flat surroundings far away.

Laws stated at a single event survive. Local conservation, $\nabla_\mu T^{\mu\nu} = 0$, uses transport only across infinitesimal distances, where the mismatch vanishes to first order.

**Takeaway:** Path dependence removes the global grid of parallel axes and the invariant sum of vectors at separated events, while leaving laws stated at a single event intact.

*Continues:* `ways_in/two-routes-to-one-spot`, `ways_in/two-orders-around-a-cell`<br>*Builds on:* [[four-momentum]]<br>*Visuals:* [[painted-arrows-that-must-match]]<br>*See:* `checks/adding-two-momenta`

### 6. Path independence exactly when curvature vanishes · formal · structure

*Under which hypotheses does zero curvature make parallel transport independent of the route, and what kind of map is the mismatch?*

The small-cell mismatch of "Two orders around a small cell" is the local face of a global theorem; set $G = c = 1$. Let $M$ carry a connection $\nabla$ on $TM$, and let $\gamma:[0,1] \to M$ be a piecewise-$C^1$ curve from $p$ to $q$. Solving $\nabla_{\dot\gamma}V = 0$ with $V(0) = v$ defines the transport $P_\gamma: T_pM \to T_qM$, a linear isomorphism independent of parametrization, with $P_{\gamma_2 * \gamma_1} = P_{\gamma_2}P_{\gamma_1}$ and $P_{\bar\gamma} = P_\gamma^{-1}$ for the reversed curve.

*Routes and loops.* For curves $\gamma_1, \gamma_2$ from $p$ to $q$, composition gives

$$P_{\gamma_2}^{-1}P_{\gamma_1} = \mathrm{Hol}_p(\bar\gamma_2 * \gamma_1),$$

so two routes disagree exactly when the loop out along $\gamma_1$ and back along $\gamma_2$ has nontrivial holonomy.

*Metric compatibility.* If $\nabla g = 0$, then $g(V,W)$ is constant for parallel $V, W$, so $P_\gamma$ is an isometry and the mismatch lies in $O(g_p)$. For a Lorentzian metric it is a Lorentz transformation, in $SO^+(1,3)$ when the loop can be shrunk to a point. It can be a boost: to second order its generator is $\Omega_{\rho\sigma} = -R_{\rho\sigma\mu\nu}a^\mu b^\nu$, and $\Omega_{\hat t\hat x} \neq 0$ mixes time and space.

*Theorem.* Let $U \subseteq M$ be open and connected. (i) $R = 0$ on $U$ if and only if $P_\gamma$ depends only on the endpoint-fixed homotopy class of $\gamma$ in $U$. (ii) If $U$ is also simply connected, $R = 0$ on $U$ if and only if $P_\gamma$ depends only on the endpoints; a basis at $p$ then spreads to a parallel frame on $U$.

*Necessity.* On a coordinate ball in $U$, fix $v$ at the centre and let $V(x)$ be its transport along any curve in the ball. Homotopy invariance makes $V$ well defined, and $\partial_\nu V^\rho = -\Gamma^\rho{}_{\nu\sigma}V^\sigma$. Differentiating again gives $\partial_\mu\partial_\nu V^\rho - \partial_\nu\partial_\mu V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma$. Mixed partials of this $C^2$ field agree, so $R^\rho{}_{\sigma\mu\nu}v^\sigma = 0$ for every $v$.

*Sufficiency.* Take a homotopy $H(s,t)$ from $\gamma_1$ to $\gamma_2$ with fixed ends, and cut its square into $N^2$ cells of side $1/N$. With $\mathcal R(X,Y)$ the endomorphism with components $R^\rho{}_{\sigma\mu\nu}X^\mu Y^\nu$, and because $[\partial_s, \partial_t] = 0$, each cell's holonomy is $1 - N^{-2}\mathcal R(\partial_sH, \partial_tH) + O(N^{-3})$, with no torsion term. With $R = 0$, sweeping $\gamma_1$ across all cells changes its transport by $(1 + O(N^{-3}))^{N^2} = 1 + O(N^{-1})$, so $P_{\gamma_1} = P_{\gamma_2}$; the problem "Homotopy cells give path independence" fills in the bounds.

*Limits.*

- Topology: a flat cone with its tip removed has $R = 0$, yet routes passing on opposite sides of the tip deliver vectors rotated relative to each other by the removed wedge angle.
- Torsion: no step used a symmetric connection. A flat connection with torsion transports path-independently, but no coordinates make its $\Gamma$ vanish.
- Physics: where curvature lies between separated events, vectors there have no invariant sum. A conserved total comes from a Killing vector $\xi$, since $\nabla_\mu(T^{\mu\nu}\xi_\nu) = 0$ for symmetric conserved $T^{\mu\nu}$, or from asymptotic flatness.

**Takeaway:** Transport is route independent within each homotopy class exactly when curvature vanishes, and for every route on simply connected regions; the mismatch is a holonomy, and in spacetime a Lorentz transformation.

*Picture:* Two curves from p to q, and the family of curves sweeping one into the other; each curve carries the same linear map exactly when the swept region has zero curvature and no hole.

*Continues:* `ways_in/two-orders-around-a-cell`, `ways_in/no-grid-and-no-total`<br>*Builds on:* [[levi-civita-connection]], [[simply-connected-space]]<br>*See:* `checks/cone-opposite-sides`, `checks/boost-between-routes`, `problems/homotopy-cells-give-path-independence`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| swing | — | To change which way an arrow points, left or right, while it lies against the ground. A carried arrow never swings. | — |
| walk straight | — | To walk without ever steering left or right, even where the route bends over a curved surface, as along a ball's equator. | [[geodesic]] |
| match | — | Two arrows at one spot match when one lies on top of the other, pointing the same way. | — |
| parallel transport | — | Carrying an arrow along a route without ever letting it swing. | [[parallel-transport]] |
| path dependence | — | The fact that, on a surface like a ball, where a carried arrow ends up pointing can depend on the route it was carried along. Here path means the same as route. | [[path-dependence-of-parallel-transport]] |

## Key equations

### Parallel transport along a curve · working

$$
\frac{dV^\rho}{ds} + \Gamma^\rho{}_{\mu\sigma}\,\frac{dx^\mu}{ds}\,V^\sigma = 0
$$

Along a given route, the carried vector's components change only to undo the turning of the coordinate basis; the route and starting vector fix the result.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $V^\rho$ | components of the carried vector | the vector |
| $x^\mu(s)$ | the route, with parameter $s$ | the route |
| $\Gamma^\rho{}_{\mu\sigma}$ | Christoffel symbols, derivative index first | the Christoffel symbols |

**Holds when:** Any smooth connection written in one coordinate chart; the Levi-Civita connection in general relativity.  
**Say it:** “The rate of change of the vector along the route, plus the Christoffel symbols times the route's direction times the vector, is zero.”  
**Justified by:** `parallel-transport`

### Mismatch between the two routes around a small cell · working

$$
V^\rho_{(a\ \text{first})} - V^\rho_{(b\ \text{first})} = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu
$$

Carrying a vector to the far corner of a small coordinate parallelogram along its two edge orders gives results that differ at second order, by minus the Riemann tensor acting on the vector and the edges.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $a^\mu,\ b^\nu$ | edge vectors of the parallelogram | the two edges |
| $V^\sigma$ | the vector at the starting corner | the starting vector |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course convention | the Riemann tensor |

**Holds when:** Coordinate parallelogram; both results compared in the coordinate basis at the shared far corner; valid to second order in the edges.  
**Say it:** “The vector that went along a first, minus the vector that went along b first, is minus the Riemann tensor acting on the vector and the two edges.”  
**Justified by:** `derivations/two-routes-around-a-cell`

### Meridian-first against latitude-first on a sphere · working

$$
\Delta\alpha = \Delta\phi\,(\cos\theta_1 - \cos\theta_2)
$$

The meridian-first vector is the latitude-first vector rotated by the area of the strip between the routes, divided by the radius squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta\alpha$ | rotation from the latitude-first vector to the meridian-first vector, positive counterclockwise seen from outside | the mismatch angle |
| $\theta_1,\ \theta_2$ | starting and final colatitudes, $\theta_1 < \theta_2$ | the two colatitudes |
| $\Delta\phi$ | change of longitude, eastward positive | the change in longitude |

**Holds when:** Sphere of any radius; one meridian arc and one arc of a circle of latitude; $\Delta\phi > 0$ eastward; exact, modulo $2\pi$.  
**Say it:** “The mismatch angle is the change in longitude times the cosine of the first colatitude minus the cosine of the second.”  
**Justified by:** `derivations/meridian-or-latitude-first`

### Two routes make one loop · formal

$$
P_{\gamma_2}^{-1}P_{\gamma_1} = \mathrm{Hol}_p(\bar\gamma_2 * \gamma_1)
$$

Undoing one route's transport after the other's is transport around the loop they form.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $P_\gamma$ | parallel transport along the curve $\gamma$ | transport along gamma |
| $\bar\gamma_2 * \gamma_1$ | the loop out along $\gamma_1$ and back along $\gamma_2$ reversed | the loop out along gamma one and back along gamma two |
| $\mathrm{Hol}_p$ | holonomy at the base point $p$ | the holonomy at p |

**Holds when:** Piecewise-$C^1$ curves with common endpoints $p$ and $q$; any connection.  
**Say it:** “Transport along gamma two undone after transport along gamma one is the holonomy of the loop they form.”  
**Justified by:** `stated`

## Derivations

### Two routes around a small cell · working

**Goal:** Show that the two edge orders of a coordinate parallelogram with edges $a$ and $b$ deliver vectors differing by $-R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$.

1. Write the transport equation as a matrix equation, $dV/ds = -\Gamma_{\dot x}V$, with $(\Gamma_e)^\rho{}_\sigma \equiv \Gamma^\rho{}_{\mu\sigma}e^\mu$.
2. For one straight step $e$ from $x$, with $s$ from 0 to 1, expand along the step: $\Gamma_e(x + se) = \Gamma_e + s\,\partial_e\Gamma_e$, where $\partial_e \equiv e^\nu\partial_\nu$ and everything on the right is evaluated at $x$.
3. Integrate to second order in $e$: the step multiplies $V$ by $P_e(x) = 1 - \Gamma_e - \tfrac12\partial_e\Gamma_e + \tfrac12\Gamma_e\Gamma_e$.
4. On the $a$-first route the second step starts at $x + a$, where $\Gamma_b(x+a) = \Gamma_b + \partial_a\Gamma_b$, so $P_b(x+a) = 1 - \Gamma_b - \partial_a\Gamma_b - \tfrac12\partial_b\Gamma_b + \tfrac12\Gamma_b\Gamma_b$.
5. Multiply, later step on the left, keeping second order: $P_b(x+a)P_a(x) = 1 - \Gamma_a - \Gamma_b - \tfrac12\partial_a\Gamma_a - \tfrac12\partial_b\Gamma_b - \partial_a\Gamma_b + \tfrac12\Gamma_a\Gamma_a + \tfrac12\Gamma_b\Gamma_b + \Gamma_b\Gamma_a$.
6. The $b$-first route is the same expression with $a$ and $b$ swapped, so its cross terms are $-\partial_b\Gamma_a$ and $\Gamma_a\Gamma_b$.
7. Subtract. Every term symmetric in $a$ and $b$ cancels, leaving $\partial_b\Gamma_a - \partial_a\Gamma_b + \Gamma_b\Gamma_a - \Gamma_a\Gamma_b$.
8. In components this is $a^\mu b^\nu\big(\partial_\nu\Gamma^\rho{}_{\mu\sigma} - \partial_\mu\Gamma^\rho{}_{\nu\sigma} + \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}\big)V^\sigma$.
9. The course definition is $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, so the bracket is $-R^\rho{}_{\sigma\mu\nu}$.

**Result:** $V^\rho_{(a\ \text{first})} - V^\rho_{(b\ \text{first})} = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, up to third-order corrections; no symmetry of $\Gamma$ was used.

### Meridian first or latitude first · working

**Goal:** On the unit sphere, find the exact mismatch between the meridian-first and latitude-first routes from $(\theta_1, \phi_0)$ to $(\theta_2, \phi_0 + \Delta\phi)$.

1. For $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$ the nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$. Use orthonormal components $x = V^\theta$ and $y = \sin\theta\,V^\phi$.
2. Along a meridian, the transport equation gives $dV^\theta/d\theta = 0$ and $dV^\phi/d\theta = -\cot\theta\,V^\phi$, so $dy/d\theta = \cos\theta\,V^\phi - \cos\theta\,V^\phi = 0$: the orthonormal components do not change.
3. Along the circle at colatitude $\theta_0$, walked eastward, it gives $dx/d\phi = \cos\theta_0\,y$ and $dy/d\phi = -\cos\theta_0\,x$, so $(x, y)$ rotates by $-\Delta\phi\cos\theta_0$, where the positive sense turns $\hat\theta$ toward $\hat\phi$.
4. Meridian first: no change, then the circle at $\theta_2$, a total rotation of $-\Delta\phi\cos\theta_2$. Latitude first: the circle at $\theta_1$, then no change, a total of $-\Delta\phi\cos\theta_1$.
5. Both vectors sit at the same endpoint in the same basis, so the meridian-first vector is the latitude-first vector rotated by $\Delta\phi(\cos\theta_1 - \cos\theta_2)$.
6. Seen from outside, $\hat\theta$ to $\hat\phi$ is counterclockwise. The strip between the routes has area $\int\!\!\int\sin\theta\,d\theta\,d\phi = \Delta\phi(\cos\theta_1 - \cos\theta_2)$. On a sphere of radius $a$ the Christoffel symbols are unchanged and the area is $a^2$ times larger.

**Result:** $\Delta\alpha = \Delta\phi(\cos\theta_1 - \cos\theta_2)$ counterclockwise seen from outside: the strip's area divided by the radius squared, exactly, for routes of any size.

## Worked examples

### A strip reaching the equator · working

**Problem:** On a sphere, a unit vector starts at colatitude $45^\circ$ pointing along the meridian away from the North Pole. Carry it to the equator at $60^\circ$ of longitude farther east, once along the meridian first and once along the circle of latitude first. Find the angle between the results and check it against the area rule.

1. Meridian first: the meridian leg leaves $(x, y) = (1, 0)$ unchanged, and the equator has $\cos 90^\circ = 0$, so the vector arrives as $(1, 0)$, pointing along the meridian away from the North Pole.
2. Latitude first: the circle at $45^\circ$ rotates $(x, y)$ by $-60^\circ \times \cos 45^\circ = -42.43^\circ$, and the meridian leg changes nothing, so it arrives rotated $42.43^\circ$ clockwise seen from outside.
3. So the meridian-first vector is the latitude-first vector rotated $42.43^\circ$ counterclockwise seen from outside.
4. Area rule: $\Delta\phi(\cos 45^\circ - \cos 90^\circ) = (\pi/3)(0.7071) = 0.7405$ rad $= 42.43^\circ$.

**Answer:** The two results differ by $42.4^\circ$; the meridian-first vector is rotated counterclockwise, seen from outside, relative to the latitude-first vector, matching the strip's area over the radius squared.

**Takeaway:** Only the leg along a circle of latitude away from the equator rotates the orthonormal components, and the difference between the two routes is exactly the enclosed area.

## Problems

### `tube-two-ways` · entry · difficulty 1 · conceptual

Roll a sheet of paper into a tube and tape the edges together. Two tiny walkers start at one spot with matching arrows. Hold the tube in front of you. One walker walks along the side of the tube facing you to a second spot. The other walks around the far side of the tube, across the tape, to the same spot. Neither lets the arrow swing. Do the arrows arrive matching?

**Hints**

1. What does the tube become when you untape it and unroll it?

**Answer:** Yes, they arrive matching. The tube unrolls into a flat sheet with nothing stretched, and on a flat sheet an arrow that never swings keeps the same angle to the sheet's edges.

**Must contain:** The arrows arrive matching; The tube unrolls flat without stretching; Both arrows keep the same angle to the sheet's edges

**Numeric:** angle between the arrows = 0 deg (magnitude, ±1)

**Solution**

1. Untape the tube and unroll it. It becomes a flat sheet, and nothing stretches, so every angle drawn on the paper is the same on the sheet as on the tube.
2. On the sheet, each arrow never swings, so each keeps the same angle to the sheet's edges along its whole route.
3. The route around the far side leaves the sheet at one taped edge and comes back in at the other. Those edges lie side by side when the tube is taped, so crossing the tape changes no angle to the edges.
4. Both arrows started matching, so both arrive at the same angle to the edges. So they match, although the tube looks bent.

### `small-rectangle-matches-formula` · working · difficulty 2 · calculation

On the unit sphere, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. Use the two-route formula to find $V_{(\theta\ \text{first})} - V_{(\phi\ \text{first})}$ for $V = e_\theta$ around the cell with edges $a = \delta\theta\,e_\theta$ and $b = \delta\phi\,e_\phi$. Convert it to an angle with its sense, and compare it with the small-cell limit of $\Delta\phi(\cos\theta_1 - \cos\theta_2)$.

**Hints**

1. Lower the first index with $g_{\theta\theta} = 1$, use antisymmetry in the first pair, and raise with $g^{\phi\phi} = 1/\sin^2\theta$.

**Answer:** The difference is $+\delta\theta\,\delta\phi\;e_\phi$: a rotation by $\sin\theta\,\delta\theta\,\delta\phi$ from $\hat\theta$ toward $\hat\phi$, counterclockwise seen from outside, which is the leading term of $\delta\phi(\cos\theta - \cos(\theta + \delta\theta))$.

**Must contain:** R phi theta theta phi equals minus one; The difference is plus delta theta delta phi along e phi; The angle sine theta delta theta delta phi agrees in size and sense with the exact result

**Solution**

1. $R_{\theta\phi\theta\phi} = g_{\theta\theta}R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, so $R_{\phi\theta\theta\phi} = -\sin^2\theta$ and $R^\phi{}_{\theta\theta\phi} = g^{\phi\phi}R_{\phi\theta\theta\phi} = -1$.
2. With $V^\theta = 1$, $a^\theta = \delta\theta$ and $b^\phi = \delta\phi$: the $\phi$ component is $-R^\phi{}_{\theta\theta\phi}\,\delta\theta\,\delta\phi = +\delta\theta\,\delta\phi$, and the $\theta$ component is $-R^\theta{}_{\theta\theta\phi}\,\delta\theta\,\delta\phi = 0$.
3. In orthonormal terms the difference is $\sin\theta\,\delta\theta\,\delta\phi\;\hat\phi$, so the $\theta$-first unit vector is tilted from the $\phi$-first one toward $\hat\phi$ by $\sin\theta\,\delta\theta\,\delta\phi$.
4. The $\theta$-first route is the meridian-first route. The exact result gives $\delta\phi(\cos\theta - \cos(\theta + \delta\theta)) = \sin\theta\,\delta\theta\,\delta\phi + O(\delta^3)$, counterclockwise seen from outside, in agreement.

### `homotopy-cells-give-path-independence` · formal · difficulty 3 · proof

Let $\nabla$ be a smooth connection on $TM$ with $R = 0$ on an open set $U$. Let $H:[0,1]^2 \to U$ be a smooth homotopy with $H(s,0) = \gamma_1(s)$, $H(s,1) = \gamma_2(s)$, $H(0,t) = p$ and $H(1,t) = q$. Prove that $P_{\gamma_1} = P_{\gamma_2}$, and conclude what holds on a simply connected $U$.

**Hints**

1. Cut the square into $N^2$ cells of side $1/N$ and move from $\gamma_1$ to $\gamma_2$ one cell at a time.

**Answer:** Each move across one cell multiplies the transport by $1 + O(N^{-3})$ when $R = 0$, so $P_{\gamma_2} = P_{\gamma_1}(1 + O(N^{-1}))$ for every $N$, hence equality. On a simply connected $U$, transport depends only on the endpoints.

**Must contain:** A cell's holonomy is one plus third-order terms when the curvature vanishes; N squared cells give an error of order one over N; Simple connectivity makes all curves with the same ends homotopic

**Solution**

1. Cut $[0,1]^2$ into $N^2$ cells of side $\epsilon = 1/N$. Moving from $\gamma_1$ to $\gamma_2$ one cell at a time, each move replaces two adjacent edges of one cell's image by the other two edges.
2. Such a move changes the transport to $q$ from $P_c$ to $P_{c'} = P_c\,Y^{-1}\,\mathrm{Hol}(\text{cell})\,Y$, where $Y$ is the transport from $p$ to the cell's corner along $c$.
3. The cell is spanned by $\epsilon\,\partial_sH$ and $\epsilon\,\partial_tH$, and $[\partial_s, \partial_t] = 0$, so $\mathrm{Hol}(\text{cell}) = 1 - \epsilon^2\mathcal R(\partial_sH, \partial_tH) + O(\epsilon^3)$. Torsion never enters, and the constant in $O(\epsilon^3)$ is uniform because $H$ and $\nabla$ are smooth on a compact square.
4. With $\mathcal R = 0$ each cell gives $1 + O(\epsilon^3)$. The transports $Y$ and $Y^{-1}$ are bounded uniformly, so each move multiplies by $1 + O(N^{-3})$.
5. After $N^2$ moves, $P_{\gamma_2} = P_{\gamma_1}\big(1 + O(N^{-3})\big)^{N^2} = P_{\gamma_1}\big(1 + O(N^{-1})\big)$. The two transports do not depend on $N$, so letting $N \to \infty$ gives $P_{\gamma_2} = P_{\gamma_1}$.
6. On a simply connected $U$, any two curves with the same ends are homotopic with fixed ends, so $P_\gamma$ depends only on the endpoints.

**Targets:** `flat-means-routes-agree`

## Observations

- **Rotation of linearly polarized light guided through a helically wound single-mode optical fibre** (measured, working). The fibre's direction of travel traces a loop on the sphere of directions while a straight fibre's stays at one point, and the polarization is carried by parallel transport on that sphere. The light leaves the coiled fibre rotated, relative to light from a straight fibre with the same ends, by the solid angle the loop encloses, with the sense reversed for a helix of opposite handedness. *Numbers:* Predicted rotation per winding $2\pi(1 - \cos\vartheta)$: $48.2^\circ$ for a helix whose fibre makes $30^\circ$ with its axis. The measured rotations followed this solid-angle prediction. *Reference:* Akira Tomita, Raymond Y. Chiao (1986), *Observation of Berry's topological phase by use of an optical fiber*, Physical Review Letters 57, 937–940, doi:10.1103/PhysRevLett.57.937

## Teaching arc

1. **Ask what the same way means far apart** (entry). Ask how to check that arrows in two distant towns point the same way. *Why:* Learners propose carrying one arrow to the other, which is parallel transport. *Uses:* `ways_in/two-routes-to-one-spot`
2. **Run two routes on a ball** (entry). Run the equator route and the North Pole route after a prediction, then the equator walked the long way. *Why:* The long way rules out distance walked as the cause. *Predict:* When the two friends meet, will their arrows match? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `two-routes`) *Uses:* `checks/pole-route-prediction`, `checks/equator-the-long-way`
3. **Find what sets the size** (entry). Split the piece between the routes with a middle route. *Why:* It turns one example into a rule with an everyday number. *Predict:* If one sixteenth of the ball lies between the routes, how far apart do the arrows arrive? *Uses:* `ways_in/size-follows-the-piece`, `checks/one-sixteenth-of-the-ball`
4. **Compute the mismatch** (working). Derive the small-cell mismatch, solve the sphere strip, then separate changing components from a changed vector. *Why:* It ties the picture to the Riemann tensor. *Predict:* If you swap which edge comes first, what happens to the mismatch? *Uses:* `derivations/two-routes-around-a-cell`, `worked_examples/quarter-sphere-strip`, `checks/polar-components-change`
5. **Name what special relativity loses** (working). Try to build a grid of parallel axes, then to add two stars' four-momenta. *Why:* It explains why only local frames and local laws survive. *Visual:* [[painted-arrows-that-must-match]] *Uses:* `ways_in/no-grid-and-no-total`, `checks/adding-two-momenta`
6. **State the theorem and break its hypotheses** (formal). Prove route independence from zero curvature with cells, then remove simple connectivity with the cone. *Why:* Each hypothesis gets a picture of its failure. *Predict:* Every patch of this cone away from the tip is flat. Will routes on opposite sides of the tip agree? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `cone-around-tip`) *Uses:* `ways_in/integrable-exactly-when-flat`, `problems/homotopy-cells-give-path-independence`, `checks/cone-opposite-sides`

## Misconceptions

### “If both arrows start matching and neither ever swings, they must arrive matching.” · entry · `never-swung-so-arrive-matching`

- **Why it is tempting:** On a flat floor, arrows that never swing keep pointing at the same wall forever.
- **What is true:** The rule says what to do at each small step, not where the arrow points after a long route. On a ball, two routes can add those steps up to different directions.
- **Exposed by:** `checks/pole-route-prediction`

### “The longer the detour, the more the arrows disagree.” · entry · `longer-route-bigger-mismatch`

- **Why it is tempting:** More walking seems to let the small steps add up more.
- **What is true:** What matters is the piece of the ball between the routes, not the distance walked. Two routes along the equator, one three times as long, deliver matching arrows.
- **Exposed by:** `checks/equator-the-long-way`

### “If the components of a carried vector change along the route, transport must depend on the route.” · working · `changing-components-mean-path-dependence`

- **Why it is tempting:** The Christoffel terms visibly change the components.
- **What is true:** Components change whenever the basis turns, as in polar coordinates on a flat plane. Path dependence means different vectors delivered to the same point, which never happens on the plane.
- **Exposed by:** `checks/polar-components-change`

### “The total four-momentum of stars in curved spacetime is the sum of their four-momenta.” · working · `vectors-anywhere-can-be-added`

- **Why it is tempting:** It is exactly how totals work in Newtonian mechanics and special relativity.
- **What is true:** Each four-momentum lives at its own event, and bringing them together depends on the route when curvature lies between them. Only scalars, or totals defined through a symmetry or the far-away geometry, add up invariantly.
- **Exposed by:** `checks/adding-two-momenta`

### “If the curvature is zero everywhere the routes pass, the routes must deliver the same vector.” · formal · `flat-means-routes-agree`

- **Why it is tempting:** The small-cell mismatch is built from curvature alone.
- **What is true:** Zero curvature guarantees agreement only for routes that can be deformed into each other within the flat region. Routes on opposite sides of a flat cone's missing tip disagree by the wedge angle.
- **Exposed by:** `checks/cone-opposite-sides`

### “In spacetime, the mismatch between two routes is always a rotation.” · formal · `mismatch-is-always-a-rotation`

- **Why it is tempting:** Surface examples only give rotations.
- **What is true:** Transport preserves the Lorentzian metric, so the mismatch is a Lorentz transformation. Routes around a small cell that spans a time direction and a space direction can differ by a boost.
- **Exposed by:** `checks/boost-between-routes`

## Checks

1. **Entry · predict** `checks/pole-route-prediction`. On a huge smooth ball, call the top point seen from outside the North Pole, and the circle around the middle the equator. Two friends stand at one spot on the equator with matching cardboard arrows. Both arrows point along the equator, toward a meeting spot a quarter of the way around. One friend walks straight along the equator to the meeting spot. The other turns to face the North Pole, which puts the meeting spot on her right. She walks straight to the North Pole, turns right by a quarter turn, and walks straight to the meeting spot. Neither arrow ever swings. When they meet, do the arrows match? If not, how far apart are they?
   - **Hints:** Where does the second friend's arrow point just after she turns at the North Pole?
   - **Answer:** No. The first friend walks the way her arrow points, so the arrow points ahead of her the whole way. It arrives pointing along the equator, away from the start. The second friend turns to face the North Pole without moving her arrow. Her route crosses the equator at a right angle, so the arrow, lying along the equator, points to her right. It stays on her right up to the North Pole, because she walks straight and the arrow never swings. When she turns right by a quarter turn, the arrow ends up pointing ahead of her. It keeps pointing ahead on her way to the meeting spot, so it arrives pointing along her route, away from the North Pole. Her route crosses the equator at a right angle there too. So the arrows arrive a quarter turn apart.
   - **Must contain:** The arrows do not match; They arrive a quarter turn apart
   - **Numeric:** angle between the arrows = 90 deg (magnitude, ±5)
   - **Targets:** `never-swung-so-arrive-matching`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `two-routes`)
2. **Entry · explain** `checks/equator-the-long-way`. On a huge smooth ball, two friends stand at one spot on the equator, the circle around the ball's middle, with matching arrows. Both arrows point along the equator, toward a meeting spot a quarter of the way around. One friend walks straight along the equator, the way the arrows point, to the meeting spot. The other walks straight along the equator the other way, three quarters of the way around, to the same spot. Neither arrow ever swings. Do the arrows match when the friends meet? Why?
   - **Hints:** Where does the second friend's arrow point, compared with her path, as she sets off?
   - **Answer:** Yes. Each friend walks straight, so each arrow keeps the same angle to its walker's route. The first arrow points ahead of its walker, so it arrives pointing the way she was walking. The second friend walks the opposite way to the one the arrows point, so her arrow points behind her the whole way. She arrives walking the opposite way to the first friend, so behind her is the way the first friend was walking. So the arrows match, although one route is three times as long. The distance walked does not decide whether the arrows match.
   - **Must contain:** The arrows match; A longer route does not by itself make the arrows disagree
   - **Numeric:** angle between the arrows = 0 deg (magnitude, ±1)
   - **Targets:** `longer-route-bigger-mismatch`
3. **Entry · numeric** `checks/one-sixteenth-of-the-ball`. On a huge smooth ball, two routes from one spot to another meet only at their ends, and neither route crosses itself. One sixteenth of the ball lies between them. Arrows that start matching are carried along the two routes without ever swinging. How many degrees apart do they arrive?
   - **Hints:** Is one sixteenth of the ball at most a quarter, so that the twice-the-fraction rule applies?
   - **Answer:** 45 degrees. The routes meet only at their ends, neither route crosses itself, and one sixteenth is less than a quarter of the ball. So the disagreement, in full turns, is twice the fraction of the ball between the routes. Twice one sixteenth is one eighth of a turn. A full turn is 360 degrees, so one eighth of a turn is 45 degrees.
   - **Must contain:** Twice one sixteenth is one eighth of a turn; 45 degrees
   - **Numeric:** angle between the arrows = 45 deg (magnitude, ±2)
4. **Working · numeric** `checks/latitude-strip-on-earth`. Treat Earth as a sphere. A vector is carried from latitude 50° N to latitude 40° N at 10° of longitude farther east, once along the meridian first and once along the circle of latitude first. By what angle do the two results differ, and in which sense is the meridian-first vector rotated relative to the latitude-first vector?
   - **Hints:** Convert latitudes to colatitudes measured from the North Pole.
   - **Answer:** The colatitudes are $\theta_1 = 40^\circ$ and $\theta_2 = 50^\circ$, so $\Delta\alpha = \Delta\phi(\cos\theta_1 - \cos\theta_2) = (0.17453\ \text{rad})(0.76604 - 0.64279) = 0.02151$ rad $= 1.23^\circ$. It is positive, so the meridian-first vector is rotated $1.23^\circ$ counterclockwise, seen from outside, relative to the latitude-first vector.
   - **Must contain:** The mismatch is 0.0215 radians, 1.23 degrees; Meridian-first is rotated counterclockwise seen from outside
   - **Numeric:** rotation of the meridian-first vector, counterclockwise seen from outside = 1.2326 deg (signed, ±0.02, mod 360)
5. **Working · evaluate-claim** `checks/polar-components-change`. On a flat plane in polar coordinates, $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$. A vector carried from $(r, \phi) = (1, 0)$ to $(1, \pi/2)$ along the unit circle has changing components $V^r$ and $V^\phi$. A classmate concludes that transport on the plane depends on the route. Evaluate the claim for $V = \partial_x$ at the start.
   - **Hints:** At $(1, \pi/2)$, which Cartesian direction does $\partial_\phi$ point along?
   - **Answer:** The claim is wrong. At the start $\partial_x = \partial_r$, so $(V^r, V^\phi) = (1, 0)$. Along the circle the transport equation gives $dV^r/d\phi = rV^\phi$ and $dV^\phi/d\phi = -V^r/r$, solved at $r = 1$ by $V^r = \cos\phi$ and $V^\phi = -\sin\phi$. At the end that is $(0, -1)$, and there $\partial_\phi = -\partial_x$, so the vector is $\partial_x$ again. In Cartesian coordinates every Christoffel symbol vanishes, so any other route also delivers $\partial_x$. The components changed only because the polar basis turns; the delivered vector is the same for every route.
   - **Must contain:** Components change because the polar basis turns; Every route on the plane delivers the same vector
   - **Targets:** `changing-components-mean-path-dependence`
   - **Visual:** [[two-grids-on-one-playground]]
6. **Working · evaluate-claim** `checks/adding-two-momenta`. Two stars orbit a black hole on opposite sides. A student defines their total four-momentum by adding the components of the two stars' four-momenta in Schwarzschild coordinates. Evaluate this definition.
   - **Hints:** At which event does each four-momentum live?
   - **Answer:** It has no invariant meaning. Each four-momentum lives in the tangent space at its own event. Adding components from two events in one chart gives an answer that changes with the chart, because vector components transform with different matrices at the two events. A geometric sum would first carry one vector to the other's event, but routes passing on different sides of the black hole deliver different vectors, since spacetime between them is curved. What can be added are scalars: for stars light enough not to disturb the geometry, the energies $E_{(i)} = -\xi\cdot p_{(i)}$ built from the static Killing vector $\xi$ are numbers, and their sum is conserved.
   - **Must contain:** The two vectors live at different events, and carrying one to the other depends on the route; Scalars built with a Killing vector can be added
   - **Targets:** `vectors-anywhere-can-be-added`
7. **Formal · explain** `checks/cone-opposite-sides`. Cut a wedge of angle $\delta$, less than a full turn, from a flat sheet, glue the cut edges into a cone, and remove the tip. Two routes between the same two points pass on opposite sides of the tip. Do they deliver the same vector? Which hypothesis of the integrability theorem fails, and what does the theorem still guarantee?
   - **Hints:** Which loops on the punctured cone cannot be shrunk to a point?
   - **Answer:** No. Out along one route and back along the other is a loop winding once around the missing tip. Unrolled, that loop runs from one cut edge to the other, and gluing the edges rotates vectors by $\delta$. So if $\gamma_1$ is the route for which the loop out along $\gamma_1$ and back along $\gamma_2$ keeps the tip on the walker's left, $P_{\gamma_1}v$ is $P_{\gamma_2}v$ rotated by $+\delta$ modulo $2\pi$, counterclockwise seen from the side the normal points to. The punctured cone has $R = 0$ but is not simply connected, so the hypothesis of part (ii) fails. Part (i) still holds: routes in the same endpoint-fixed homotopy class deliver the same vector.
   - **Must contain:** The routes disagree by a rotation through the wedge angle; The punctured cone is flat but not simply connected, yet homotopic routes still agree
   - **Targets:** `flat-means-routes-agree`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `cone-around-tip`)
8. **Formal · explain** `checks/boost-between-routes`. In a curved spacetime, a unit timelike vector $u$ at $p$ is carried to $q$ along two routes, giving $u_1$ and $u_2$. Show that $u_2$ is the image of $u_1$ under a Lorentz transformation, and say whether routes around a small cell can make it a boost.
   - **Hints:** Which components of the change would mix $e_{\hat t}$ with a space direction?
   - **Answer:** Levi-Civita transport preserves $g$, so $P_{\gamma_2}P_{\gamma_1}^{-1}$ is an isometry of $T_qM$ taking $u_1$ to $u_2$: a Lorentz transformation. For a small cell, $u_1 - u_2 = -R^\rho{}_{\sigma\mu\nu}u^\sigma a^\mu b^\nu$ to second order. In an orthonormal frame with $u = e_{\hat t}$, its $\hat x$ component is $-R^{\hat x}{}_{\hat t\mu\nu}a^\mu b^\nu$, a change of the time direction toward $e_{\hat x}$, which is a boost. Outside a spherical mass, with $G = c = 1$, $R^{\hat r}{}_{\hat t\hat t\hat r} = 2M/r^3 \neq 0$, so a cell spanned by a time step and a radial step gives a boost of rapidity about $2M\,\delta t\,\delta r/r^3$, for a proper time step $\delta t$ and a proper radial step $\delta r$.
   - **Must contain:** Metric-preserving transport makes the mismatch a Lorentz transformation; A cell containing a time direction can tilt the time direction, a boost
   - **Targets:** `mismatch-is-always-a-rotation`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Order and sign of the two-route mismatch | $V_{(a\ \text{first})} - V_{(b\ \text{first})} = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ with the course Riemann tensor, the same change as walking the loop $+a, +b, -a, -b$. | Some texts subtract the routes in the other order, or define the Riemann tensor with the opposite overall sign, and write $+R$. State the subtraction order and the Riemann convention together. |
| Which index of the Christoffel symbol carries the direction of travel | The direction index comes first: $\Gamma^\rho{}_{\mu\sigma}\,(dx^\mu/ds)\,V^\sigma$, matching $\nabla_\mu V^\rho = \partial_\mu V^\rho + \Gamma^\rho{}_{\mu\lambda}V^\lambda$. | Some texts put the direction index last. For the symmetric connection of general relativity both readings agree; with torsion they differ. |

## Visuals

- ★ [[carry-an-arrow-around-a-loop]] (flagship): Its two-routes preset shows twin arrows meeting a quarter turn apart on a ball. *Sketch:* A cone glued from a sheet with an adjustable missing wedge, the unrolled sheet beside it. Routes on the same side of the tip deliver matching arrows; routes on opposite sides disagree by the wedge angle.
- [[light-through-a-coiled-fibre]] (core): Connects route dependence to a laboratory measurement of polarization. *Sketch:* A straight and a helical fibre with the same entry and exit directions, beside the sphere of directions where the helix traces a circle. A pitch slider changes the circle; a polarimeter dial at the exits shows the relative rotation beside the enclosed solid angle, and flipping the handedness flips its sense.
- [[painted-arrows-that-must-match]] (supporting): Shows the failed grid of parallel axes as a consequence of two routes disagreeing. *Sketch:* A patch of floor, tube or ball filled with carried copies of one arrow along two sweeping orders. Where the fillings disagree the arrows double with a shaded wedge, which never appears on the floor or tube and grows with area on the ball.
- [[two-grids-on-one-playground]] (supporting): Separates changing components from a changed vector. *Sketch:* A flat plane with a polar grid and two draggable routes. Plots show each arrow's polar components changing and its Cartesian components constant; the arrows coincide at the endpoint. A switch moves the construction onto a sphere patch, where they differ.

## Tutor moves

**Open with**

- Picture a huge smooth ball with no compass, no stars and no landmarks, and an arrow painted on the ground in each of two towns far apart. How could you check whether the two arrows point the same way? *(reflection)*
- Picture a giant smooth ball. Two friends start together with matching arrows and walk to the same meeting spot by different routes, never letting the arrows swing. When they meet, will the arrows match? *(prediction)*

**If the learner is stuck**

- *The learner loses track of where the second friend's arrow points.* → Replay her route one stretch at a time and have the learner name the arrow's direction relative to her path: on her right, then ahead. *Uses:* `ways_in/two-routes-to-one-spot`

**Common questions**

- *Which route gives the right direction?* (entry) Neither. Each route carries its arrow correctly, never letting it swing. On a ball there is no single right answer to whether two distant arrows point the same way. The answer can depend on the route you use to bring them together. *Uses:* `ways_in/two-routes-to-one-spot`
- *Why does this matter for gravity?* (entry) General relativity, Einstein's theory of gravity, describes gravity as a curving of space and time. Wherever there is such curving, arrows carried to one place by different routes can disagree, as on a ball. So near a star or a planet nobody can set up arrows over a large region that all point exactly the same way as each other. Instead, the laws of physics are written as rules about what happens at each place and its close neighbourhood. *Uses:* `ways_in/no-grid-and-no-total`

**Switching levels**

- To working when: asks how to calculate the mismatch; is comfortable with Christoffel symbols. Go to the small-cell derivation, then the sphere strip. *Uses:* `ways_in/two-orders-around-a-cell`, `worked_examples/quarter-sphere-strip`
- To formal when: asks whether zero curvature always makes routes agree; mentions topology or holonomy. State the integrability theorem and test it on the punctured cone. *Uses:* `ways_in/integrable-exactly-when-flat`, `checks/cone-opposite-sides`
- To research when: asks about energy in general relativity or lattice gauge theory. Open the research horizon. *Uses:* `research_horizon/energy-without-a-global-sum`, `research_horizon/links-on-a-lattice`

**Pronunciations:** Riemann → REE-mahn; Christoffel → kris-TOFF-el; Levi-Civita → LEH-vee CHEE-vee-tah; Weyl → VILE; birefringence → by-ree-FRIN-jence

**Voice notes:** Say that arrows match when they agree at one spot. Read the two-route formula as: the vector that went along a first, minus the vector that went along b first.

## History

- **Tullio Levi-Civita (1917).** Defined parallel transport on curved manifolds, first through an embedding in flat space, and read Riemann's curvature as its failure to be route independent. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–205, doi:10.1007/BF03014898
- **Hermann Weyl (1918).** Proposed a geometry in which lengths, not only directions, depend on the route along which they are carried. Einstein objected that the rates of atomic clocks would then depend on their histories, which the sharp spectral lines of atoms rule out. Hermann Weyl (1918), *Gravitation und Elektrizität*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften zu Berlin, 465–480

## Research horizon

- **Energy and momentum without a global sum.** Since vectors at separated events have no invariant sum, general relativity has no general total energy-momentum built from local densities. For asymptotically flat spacetimes the ADM construction defines total energy and momentum at spatial infinity. For finite regions many quasi-local definitions compete, and none is accepted as unique. Richard Arnowitt, Stanley Deser, Charles W. Misner (1962), *The dynamics of general relativity*, in L. Witten (ed.), Gravitation: An Introduction to Current Research, Wiley, New York, 227–265, arXiv:gr-qc/0405109; László B. Szabados (2009), *Quasi-local energy-momentum and angular momentum in general relativity*, Living Reviews in Relativity 12, 4, doi:10.12942/lrr-2009-4
- **Lattice gauge theory.** Lattice gauge theory keeps a connection only through its transports along the links of a spacetime lattice. The product of transports around one elementary square, which compares the two routes across it, approximates the field strength, and the lattice action is built from these products. Kenneth G. Wilson (1974), *Confinement of quarks*, Physical Review D 10, 2445–2459, doi:10.1103/PhysRevD.10.2445

## Review: novice

**Verdict:** fixed (2026-09-13, revision 9)

**Retell attempt:** Second reading of the revision-5 text, 2026-09-13. Two friends on a giant smooth ball stand at one spot on the equator, with two cardboard arrows lying on top of each other, both pointing along the equator toward a meeting spot a quarter of the way round. Neither friend ever lets her arrow swing. The first walks along the equator and her arrow points ahead of her the whole way. The second faces the North Pole, with the meeting spot on her right, so her arrow lies across her and points to her right. She walks to the pole with the arrow still on her right, turns a quarter turn right, and the arrow now points ahead of her, so it arrives pointing away from the pole. At the meeting spot the arrows are a quarter turn apart, although neither swung. On a flat floor that never happens, because an arrow that never swings keeps pointing at the same wall of the room. Carrying an arrow that way is called parallel transport, and the fact that the answer can depend on the route is called path dependence. How far apart the arrows arrive follows the piece of ball between the routes: twice that fraction of a turn, so one eighth of the ball gives a quarter turn. On Earth one square kilometre gives about 1.4 millionths of a degree, a hair's width seen from 3 kilometres away, which is why nobody notices it. What I could not pin down: what counts as a line from the North Pole to the equator, and why every one of them is a straight walk; why a piece of ball staying on her right tells me the other line is on her right when she reaches the pole; and, in the rule, which of the two pieces the routes cut the ball into is the fraction between the routes, since both pieces lie between them (I guessed the smaller one, from the quarter limit). I had to reread the middle friend's line that reaches the equator halfway along. In the paper-tube problem the answer says the back route where the question said the far side, and I had to check they were the same walker.

First reading of the revision-1 text, 2026-09-13. Two friends on a giant ball start with arrows pointing the same way along the equator. One walks along the equator; the other goes over the North Pole and comes back down to the same spot. Neither lets the arrow swing, but when they meet the arrows are a quarter turn apart. On a flat floor that can't happen, because the arrow keeps pointing at the same wall. So on a ball which way is 'the same way' depends on the route; that's path dependence, or parallel transport, I'm not sure which name is which. The bigger the piece of ball between the routes, the bigger the difference, twice the fraction, and on Earth a square kilometre gives about a millionth of a degree, a hair from 3 km. I didn't see why the equator counts as straight, why she turns right at the pole, why the piece is one eighth, which of the two pieces counts, or how to set up the orange.

**Stumbles (28)**

- “whether two distant arrows point the same way depends on the route used to compare them”: Summary: 'compare them' names no method, and 'depends' is false for pairs of routes that agree, such as the two equator routes.
- “Two friends stand together at a spot on the equator of a huge, smooth ball.”: On a plain ball, 'equator' and 'North Pole' have no meaning until something picks a top point.
- “The first friend walks straight along the equator to the meeting spot.”: Surprise with no reason: a teenager objects that the equator bends, so it cannot be a straight walk; the same goes for the lines from the North Pole.
- “While a friend walks straight, the arrow therefore keeps the same angle to the path.”: 'Therefore' hides the step: the angle stays fixed because the walker does not steer and the arrow does not swing.
- “As she sets off, her arrow points to her right, along the equator.”: Step left implicit: she must first turn to face the North Pole, and nothing says which side the meeting spot is on, or why the arrow ends up at a right angle to her.
- “then straight down to the meeting spot”: Wording trap: 'down' has no meaning on a ball (way 1, the recap of way 2, and the pole-route check).
- “The meeting spot was on her right when she set off, so at the North Pole she turns right by a quarter turn to face it.”: Reread: why should a side she had at the equator still be her side at the North Pole?
- “The arrow did not swing, so now it points ahead of her.”: A step left implicit: the reader must work out that on her right plus a quarter turn right means ahead.
- “Carrying an arrow without letting it swing is called parallel transport. On a ball, where the carried arrow ends up pointing depends on the route. This is called path dependence.”: Two new terms in one paragraph (rule 4); 'depends' is false for routes that agree; and the text says both 'path' and 'route' for one idea.
- “It changes what pointing the same way can mean. ... On a ball there is no such wall.”: An ambiguous 'It', and a claim with no reason.
- “Stretch two more over its top, crossing there at a right angle. Where the first of these meets the middle band, lay two matchsticks together along the middle band. Slide one along the middle band, the way both point, to the second band.”: A rule the reader cannot follow: each band over the top crosses the middle band at two places, and the matchsticks' starting direction is unclear.
- “The smaller piece, between the routes, is one eighth of the ball”: Surprising number with no count; also, on a closed ball both pieces lie between the routes.
- “The ball is the same everywhere, so each half makes the arrows disagree by the same amount, in the same direction.”: A step taken on trust: the two comparisons are not copies of each other unless the disagreement is set by the piece alone. 'Direction' is also the arrow's word, used here for the sense of the disagreement.
- “the first friend's arrow and the middle arrow disagree by some amount”: 'Middle arrow' is a new name for the third friend's arrow, and 'disagree by an amount' was never tied to an angle.
- “Splitting pieces again and again points to a rule, which a later level proves.”: Points by position ('a later level') and oversells the argument: halving works only for pieces cut like orange segments. The reader also asks what happens beyond a quarter of the ball.
- “So the arrows disagree by two parts in 510 million of a full turn, which is about 1.4 millionths of a degree.”: The conversion from a fraction of a turn to degrees is skipped, and one square kilometre gives no everyday feel.
- “The more of the ball lies between two routes, the more their arrows disagree”: False first what-if: the two equator routes have half the ball between them and match.
- “The other walks straight to the North Pole, turns right by a quarter turn”: Check start state ambiguous: the question never says the meeting spot is on her right when she faces the North Pole, so the answer's 'starts on its walker's right' is unbacked.
- “The second arrow points behind its walker the whole way. ... The distance walked is not what decides the mismatch.”: Missing because-step for 'behind', and 'mismatch' is a word the entry ways never use.
- “One walks along the front of the tube to a second spot. The other walks around the back of the tube”: 'Front' and 'back' have no viewpoint.
- “How could you check whether they point the same way?”: Opening question: the everyday right answer (use a compass) would be treated as wrong.
- “So nobody can lay out one grid of matching directions across the universe, and the laws are written place by place.”: Spoken answer: 'grid of matching directions' and 'written place by place' are vague, and 'across the universe' is broader than the reason given.
- “The equator is a straight walk, and so is every line from the North Pole to the equator.”: Second reading: 'line' is never given a meaning, so 'every line' can be read as any line at all, including a wandering one, and the claim then looks false to the first what-if a reader tries.
- “The piece of ball between her line and the meeting spot's line also stays on her right, because she never steers.”: Second reading, reread: the sentence builds a piece of ball out of two lines, one of them ('the meeting spot's line') named here for the first time, and 'because she never steers' does not obviously hold a piece of ball on one side. All the next paragraph needs is that the other line is on her right.
- “From there she walks straight along the line that reaches the equator halfway between the start and the meeting spot.”: Second reading, reread: the reader must first build a line from where it lands, then follow it. Saying where she walks to says the same thing in one move.
- “Let at most a quarter of the ball lie between the routes. The disagreement, in full turns, is twice the fraction of the ball between the routes.”: Second reading: two routes cut the ball into two pieces and, on a closed ball, both lie between them, so 'the fraction of the ball between the routes' does not say which piece to use. The reader has to work backwards from the quarter limit to find out.
- “The back route leaves the sheet at one taped edge and comes back in at the other.”: Second reading: the tube problem's question says 'the far side of the tube', so 'the back route' is a second name for one route, and 'back' gives no viewpoint.
- “So near a star or a planet nobody can set up one set of exactly matching arrows that covers a large region.”: Second reading, spoken answer: by the glossary two arrows match when one lies on top of the other at one spot, so 'matching arrows that cover a large region' stretches the word to the very thing the concept says has no single answer.

**Fixes**

- Way 'Two routes to one spot': defined the North Pole and equator, backed the straight walks with the mirror reason, made the second friend's first turn and the side of the meeting spot explicit, replaced 'down', justified why she turns right at the North Pole, spelled out why the arrow ends up ahead, split parallel transport and path dependence into separate paragraphs, scoped 'depends' to 'can depend', said that path means route, and resolved the ambiguous 'It'.
- Try-it: the start and the meeting spot are named, the orange sits on a table, and the matchsticks' starting direction is given.
- Way 'The disagreement follows the piece between the routes': defined the piece between the routes, counted the one eighth, tied 'disagree' to the angle between arrows, and named the third friend's arrow. The splitting argument now states its assumption, says it covers only pieces cut like orange segments with other shapes taken on trust, and explains the quarter-of-the-ball limit. Added the degrees conversion and the 140 football pitches, and scoped the takeaway (split into two sentences).
- Summary and glossary: 'can depend', and 'path means the same as route'.
- Checks: the pole-route question fixes the meeting spot on the second friend's right, and its answer gives every because-step. The long-way answer explains 'behind' and drops 'mismatch'. The tube problem gives a viewpoint.
- Tutor: the opening question rules out a compass, and the gravity common question is scoped and concrete.
- Ladder: 'Two orders around a small cell' now bridges from twice the fraction of the ball in full turns to $A/a^2$ radians and defines colatitude. 'Light in a coiled fibre' says that solid angle is the enclosed area on the unit sphere, which ties it to the area rule.
- Budget: entry explanations are at 1,076 words, within the 10% review allowance over the 1,000 cap, all for recorded stumble fixes. To stay short, dropped way 1's repeated sentence about flat-floor arrows pointing at the same wall. Nothing else was cut; every other part is under its cap.
- Bumped the revision to 2.
- Second reading (revision 6), way 'Two routes to one spot': the straight walks from the pole are named as the lines a globe draws from the North Pole to the equator, and the walk to the pole now tracks the line from the North Pole to the meeting spot instead of the piece of ball between two lines.
- Second reading, way 'The disagreement follows the piece between the routes': the third friend walks straight to the equator halfway along, and the rule names the smaller of the two pieces the routes cut the ball into, so 'twice that fraction' has one meaning.
- Second reading, problem 'tube-two-ways': 'the back route' became 'the route around the far side', matching the viewpoint the question sets.
- Second reading, common question 'why-it-matters-for-gravity': 'one set of exactly matching arrows that covers a large region' became arrows that 'all point exactly the same way as each other', keeping 'exactly' so the approximate grid near a star is not denied.
- Second reading, budget: entry way explanations fall from 1,099 to 1,095 words, inside the 10% review allowance over the 1,000 cap; two fixes shorten and two lengthen, so nothing had to be dropped.
- Bumped the revision to 6.

**Concerns**

- The entry twice-the-fraction rule is backed only for pieces cut like orange segments, and the text now says so. The halving step assumes the disagreement is set by the piece alone. The physics reviewer should confirm that this scoped wording, with 'toward the same side', is accurate.
- The two-routes preset of carry-an-arrow-around-a-loop has no tour for this concept. A tour should narrate relative to the walker ('on my right, then ahead'), put the meeting spot on the second walker's right, and never say 'down'.
- The prose fixes the meeting spot on the second friend's right. The mirror-image choice gives the same quarter turn, so no convention is needed at entry, but the visual should match the prose.
- The previous stage measured budgets against the 80% draft line. The review allowance is 10% past the real caps, so tutoring (2,774 of 3,300) and support (1,845 of 2,300) still have room.
- The fibre's rotation sense is still unset by the conventions file, as the writer reported. This review did not change that.
- Second reading: this pass re-read a note whose first novice review, physics review, novice re-read and physics diff check had already closed at revision 5. The four changed learner-visible fields are listed in the second-reading fixes; a physics diff check should confirm that 'the smaller of the two pieces between the routes' states the same hypothesis as the old 'at most a quarter of the ball ... between the routes', and that 'every line a globe draws from the North Pole to the equator' names exactly the meridian arcs meant.
- Second reading: the note carries one novice stage, so this pass's retell, stumbles and fixes are appended to the first pass's and labelled 'Second reading'; nothing from the first pass was removed.
- Second reading, budget: entry way explanations sit at 1,095 of the 1,100 the review allowance permits, so a later entry-rung fix has to shorten something. The lowest-value candidates are 'One eighth of the ball gives two eighths, a quarter turn, as the friends found.', which the Earth example immediately repeats in numbers, and the second half of 'On a ball, no wall can tell you that two distant arrows point the same way, because ...', whose reason is the whole way.

**Re-read** (2026-09-13, revision 4): 7 stumbles in 8 changed passages

- “Take two routes that never cross themselves and meet each other only at their ends”: 'Never cross themselves' can be read as 'never cross each other', and nothing says why a route may not cross itself, so the new condition is taken on trust.
- “For routes that never cross themselves and meet only at their ends, with up to a quarter of the ball between them, the arrows disagree by twice that fraction of a turn.”: Same 'themselves' ambiguity: a reader can take it as 'never cross each other'.
- “two routes from one spot to another never cross themselves and meet only at their ends, and one sixteenth of the ball lies between them.”: Check question: the same 'themselves' ambiguity, in a long sentence with three facts.
- “The routes never cross themselves and meet only at their ends”: Check answer: the same 'themselves' ambiguity.
- “The flat spacetime of special relativity behaves the same way, and special relativity quietly relies on it twice.”: Working rung: 'special relativity' twice in one sentence, and 'it' could mean the spacetime or the behaviour.
- “In the flat spacetime of special relativity this gives a single-valued field of parallel axes”: Working rung: repeats the phrase from two sentences earlier, and 'this' has two candidates (the carrying, or the axes).
- “Take two routes that meet only at their ends, with one square kilometre between them, about 140 football pitches.”: False-what-if risk: the Earth example leaves out the new 'neither route crosses itself' condition that the rule a paragraph earlier now requires. Not edited, because adding a condition changes the sentence's scope; proposed for the physics diff check.
- Fix: Way 'The disagreement follows the piece between the routes': split the rule sentence, replaced 'never cross themselves' with 'Neither route may cross itself', and gave the reason (it would cut the ball into more than two pieces, tying back to the opening paragraph). The takeaway says 'neither crossing itself' (kept to one sentence by the 240-character takeaway limit).
- Fix: Check 'one-sixteenth-of-the-ball': question and answer say 'neither route crosses itself'; the question is split into two sentences.
- Fix: Working way 'No grid of parallel axes, no total momentum': removed the doubled 'special relativity' and the ambiguous 'it' and 'this'; the claims and the scope to special relativity's flat spacetime are unchanged.
- Fix: Tutor answers 'can depend' and 'exactly matching arrows' read cleanly; no change.
- Fix: Not edited: the Earth example sentence omits the no-self-crossing condition (see stumbles); left for the physics diff check.
- Fix: Budget: entry explanations rise by 14 words, to 1,096, within the 10% review allowance over the 1,000 cap, all for recorded stumble fixes. Nothing dropped.
- Fix: Bumped the revision to 4.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 8): 2 stumbles in 2 changed passages

- “The equator is a straight walk, and so is each of the evenly spaced lines a globe draws from the North Pole to the equator.”: One 25-word sentence carries two separate straight-walk claims, and 'each of the evenly spaced lines' reads as if even spacing were the reason a line is a straight walk. The reason given next is a mirror image, which says nothing about spacing, so the reader is left asking whether an unevenly spaced line would bend, and has no way to check.
- “For each of these lines, the ball on one side is a mirror image of the ball on the other side.”: 'These lines' has two candidates in the sentence before it: the equator alone, or the equator together with the globe's lines from the North Pole. A reader who takes the narrow reading never learns why the equator counts as a straight walk. Not edited, because either fix picks a scope for the mirror reason, and scope is a claim; proposed for the physics diff check.
- Fix: Way 'Two routes to one spot': split the 25-word double claim into two sentences, and moved 'evenly spaced' from the individual line to the set a globe draws, so the phrase picks out which family of lines is meant instead of reading as the reason the walk is straight. The family named is exactly the one the physics review narrowed to, so the scope is unchanged.
- Fix: Not edited: the ambiguous antecedent in 'For each of these lines' (see stumbles); left for the physics diff check, because naming the equator there widens that sentence's scope.
- Fix: Budget: the rewrite is word-for-word even, so entry way explanations stay at 1,099 words, one word under the 1,100-word review ceiling. Nothing dropped or compressed.
- Fix: Bumped the revision to 8.

**Re-read** (2026-09-13, revision 9): 0 stumbles in 2 changed passages


## Review: physics

**Verdict:** fixed (2026-09-13, revision 9)

**Verification**

- Entry way 'Two routes to one spot': the equator arrow and the pole-route arrow meet a quarter turn apart; the meeting spot is on the second friend's right when she faces the North Pole, and she turns right at the pole.: 3D trace on the unit sphere: start (1,0,0), arrow (0,1,0); transport along the xz great circle leaves (0,1,0) fixed; at the pole the heading is (-1,0,0) and her right, heading x outward normal, is (0,1,0); after a right quarter turn she heads (0,1,0) and arrives at (0,1,0) with the arrow along (0,0,-1), while the equator arrow is (-1,0,0). → Correct: 90 degrees, and every 'on her right', 'ahead' and 'away from the North Pole' matches. The mirror-image choice of meeting spot gives the same quarter turn.
- Entry halving: the middle route splits the octant into two halves, each giving the same disagreement 'toward the same side', together a quarter turn.: Traced both loops (equator route vs middle route; middle route vs pole route) with the walker's head along the outward normal: both keep their wedge on the walker's left. Strip formula with theta1 -> 0, theta2 = 90 degrees for longitude spans 0-45, 45-90, 0-90 in python. → +45, +45, +90 degrees: equal, same sense, additive. 'Toward the same side' is accurate, and the stated assumption (disagreement set by the piece alone) plus 'pieces cut like orange segments, other shapes taken on trust' is an honest scope.
- Entry rule: for routes that meet only at their ends with at most a quarter of the ball between them, the disagreement in full turns is twice the fraction; the quarter limit caps it at a half turn.: Local Gauss-Bonnet for a simple loop: holonomy = K times area mod 2 pi; fraction f of 4 pi a^2 gives 2f turns; the complementary piece gives 2 - 2f, equal mod 1 turn; for f <= 1/4 the angle between arrows is 2f <= 1/2 turn. → Correct for simple loops. The rule was ambiguous for a route that crosses itself (the loop is then not simple and 'the fraction between the routes' is undefined), so 'never cross themselves' was added.
- Entry Earth number: one square kilometre on a 510 million km^2 Earth gives 720/510 million degrees, about 1.4 millionths of a degree, a hair's width at 3 km, about 140 football pitches.: python → 1.412e-6 degrees; 2.46e-8 rad times 3000 m = 74 micrometres, a typical hair; 1 km^2 / (105 m x 68 m) = 140. Correct.
- Entry checks: pole route 90 degrees; equator the long way 0 degrees; one sixteenth of the ball 45 degrees; tube problem 0 degrees.: Worked each: pole route by the 3D trace; long way by holonomy of the equator (half the ball, one full turn, matching); 2 x 1/16 = 1/8 turn = 45 degrees; the tube is a flat cylinder whose holonomy around the bracelet loop is the identity. → All correct, tolerances sensible.
- Bridge: a piece of area A on a sphere of radius a gives 2 (A / 4 pi a^2) 2 pi = A/a^2 radians.: Hand algebra. → Correct.
- Transport equation dV^rho/ds + Gamma^rho_{mu sigma} dx^mu/ds V^sigma = 0 with the direction index first.: Compared with the conventions row nabla_mu V^nu = partial_mu V^nu + Gamma^nu_{mu lambda} V^lambda. → Consistent.
- Derivation 'Two routes around a small cell': single-step matrix 1 - Gamma_e - (1/2) d_e Gamma_e + (1/2) Gamma_e^2; the a-first product; the antisymmetric remainder equals -R^rho_{sigma mu nu} a^mu b^nu with the course Riemann tensor.: Re-derived each step by hand: second-order Dyson expansion of dV/ds = -Gamma_e(x+se) V; P_b(x+a) with Gamma_b shifted by d_a Gamma_b; product and the swap; component form compared term by term with the conventions Riemann row; consistency with the conventions small-loop row via loop = P_bfirst^{-1} P_afirst. → Correct at every step, including the claim that no symmetry of Gamma was used.
- Derivation 'Meridian first or latitude first': orthonormal components fixed along a meridian; rotation -Delta phi cos theta0 along a latitude circle; mismatch Delta phi (cos theta1 - cos theta2), counterclockwise seen from outside, equal to the strip's area.: Hand check of dy/dtheta = 0 and dx/dphi = cos theta0 y, dy/dphi = -cos theta0 x; theta-hat x phi-hat = r-hat for the sense; python RK4 transport in coordinate components for theta 40 -> 50 degrees and 10 degrees of longitude. → RK4 gives +1.232568 degrees, matching the formula to 1e-12; the strip lies on the meridian-first walker's left, consistent with the conventions orientation row. Correct.
- Worked example: colatitude 45 degrees to the equator through 60 degrees gives 42.43 degrees, meridian-first counterclockwise from outside.: python → 60 cos 45 = 42.426 degrees; (pi/3)(0.7071) = 0.7405 rad. Correct.
- Check latitude-strip-on-earth: 0.02151 rad = 1.2326 degrees, positive.: python and RK4 as in the derivation check. → 0.0215124 rad, 1.23257 degrees. Correct; tolerance 0.02 degrees fine.
- Problem small-rectangle-matches-formula: R^phi_{theta theta phi} = -1, difference +delta theta delta phi e_phi, rotation sin theta delta theta delta phi counterclockwise.: Index lowering and antisymmetry by hand; expansion of delta phi (cos theta - cos(theta + delta theta)). → Correct in size and sense.
- Check polar-components-change: V^r = cos phi, V^phi = -sin phi solves transport on the unit circle and delivers d/dx at (1, pi/2).: Substituted into dV^r/dphi = r V^phi and dV^phi/dphi = -V^r/r; d/dphi = -r sin phi d/dx + r cos phi d/dy at phi = pi/2. → Correct.
- Check adding-two-momenta: chart sums are not invariant; E = -xi . p are scalars conserved along each test geodesic.: Standard Killing-vector argument; units checked with xi = d/dt and x^0 = ct. → Correct for test stars on geodesics, as scoped.
- Fibre way: de/ds = -(e . dt/ds) t-hat is transport on the unit sphere; the helix gives 2 pi (1 - cos theta) per winding, 48.2 degrees at 30 degrees, independent of radius.: Checked d(e . t)/ds = 0 and d|e|/ds = 0; cap area on the unit sphere; python. → 360 (1 - cos 30 degrees) = 48.23 degrees. Correct; the complementary cap gives the opposite sense modulo 360, consistent with 'sense set by handedness'.
- Formal key equation P_{gamma2}^{-1} P_{gamma1} = Hol_p(gamma2-bar * gamma1).: From P_{gamma2*gamma1} = P_{gamma2} P_{gamma1} and P_{gamma-bar} = P_gamma^{-1}. → Correct.
- Formal theorem: necessity via mixed partials, d_mu d_nu V - d_nu d_mu V = -R^rho_{sigma mu nu} V^sigma; sufficiency via N^2 cells with holonomy 1 - N^{-2} R(d_s H, d_t H) + O(N^{-3}); restricted Lorentz holonomy lies in SO^+(1,3); generator Omega = -R_{rho sigma mu nu} a^mu b^nu.: Differentiated d_nu V^rho = -Gamma^rho_{nu sigma} V^sigma again and antisymmetrized; checked (1 + O(N^-3))^{N^2} = 1 + O(1/N); restricted holonomy is connected; torsion claim checked (coordinate Gamma vanishing forces T = 0). → Correct.
- Cone check: the loop with the tip on the walker's left gives +delta modulo 2 pi.: Total curvature of a cone with deficit delta is +delta at the tip; P_{gamma1} = P_{gamma2} Hol, rotations commute in 2D. → Correct. The question never named delta and the answer said 'part (ii) fails' where the hypothesis of (ii) fails; both fixed.
- Boost check: R^{r-hat}_{t-hat t-hat r-hat} = +2M/r^3 outside a spherical mass.: Course conventions: R_{t-hat r-hat t-hat r-hat} = -2M/r^3 so that geodesic deviation stretches radially (D^2 xi^r/dtau^2 = +2M xi^r/r^3); antisymmetry in the last pair. → Correct. 'A boost of that size' mixed a curvature with a dimensionless rapidity; replaced by rapidity about 2M delta t delta r / r^3.
- Reference: Tomita and Chiao (1986), Physical Review Letters 57, 937-940.: WebSearch (APS/ADS record). → Confirmed; DOI 10.1103/PhysRevLett.57.937 added.
- Reference: Levi-Civita (1917), Rendiconti del Circolo Matematico di Palermo 42, 173-205.: WebSearch (Springer record). → Confirmed; DOI 10.1007/BF03014898 added.
- Reference: Weyl (1918), Gravitation und Elektrizitaet, Sitzungsberichte Berlin, 465-480; Einstein's objection.: WebSearch (ADS records of the paper and of Einstein's appended comment at p. 478). → Confirmed; no DOI for the original printing.
- Reference: Arnowitt, Deser, Misner (1962), The dynamics of general relativity, in Witten (ed.), Wiley, 227-265, arXiv:gr-qc/0405109.: WebSearch (arXiv abstract). → Confirmed.
- Reference: Szabados (2009), Living Reviews in Relativity 12, 4.: WebSearch (EuDML/PubMed). → Confirmed; DOI 10.12942/lrr-2009-4 added.
- Reference: Wilson (1974), Confinement of quarks, Physical Review D 10, 2445-2459.: WebSearch (APS record). → Confirmed; DOI 10.1103/PhysRevD.10.2445 added.
- History scope: Levi-Civita defined parallel transport, first via an embedding, and read curvature through it; Weyl proposed route-dependent lengths and Einstein objected via atomic spectra.: Paper title and ADS record of Einstein's comment. → Accurate as scoped ('defined', not 'first'; Schouten's independent 1918 work is not contradicted).
- Second pass, novice second-reading rewrite (entry): 'The equator is a straight walk, and so is every line a globe draws from the North Pole to the equator.': Tested the universal 'every line a globe draws from the North Pole to the equator' against what globes actually draw. Lines of latitude are excluded (they do not run from the pole to the equator), but the date line does run from pole to pole and jogs around island groups near the equator, and mapped borders need not follow a meridian. Checked the justification that follows ('the ball on one side is a mirror image of the ball on the other side'): reflection in the plane of a meridian fixes that meridian pointwise and maps the sphere to itself, so a meridian arc is a geodesic; the date line has no such symmetry. → The universal was false as stated, and the mirror reason fails for the exception. Narrowed to 'each of the evenly spaced lines a globe draws from the North Pole to the equator', which names exactly the meridian family, keeps the mirror reason true, and adds four words (entry 1,095 to 1,099 words, inside the review ceiling).
- Second pass, novice second-reading rewrite (entry): 'The line from the North Pole to the meeting spot stays on her right too, because she never steers.': Unit-sphere trace in python. Start (1,0,0), meeting spot (0,1,0), pole (0,0,1). Along the meridian p(t) = (cos t, 0, sin t) the heading is T = (-sin t, 0, cos t) and, with her head along the outward normal n = p, her right is T x n = (0,1,0) for every t. The meeting spot's meridian lies in the half-space y > 0 until the two meet at the pole. → Correct at every point of the walk: her right is constant in space and always points to the side the other meridian lies on. The stated reason is the right one at entry: never steering keeps her on her own line, and neither line moves.
- Second pass, novice second-reading rewrite (entry): the third friend 'walks straight to the equator, halfway between the start and the meeting spot', and each half of the piece gives an eighth of a turn.: Exact great-circle transport of the arrow along all three routes in python (decompose into the component along the plane's unit normal, which is constant, and the component along the arc's tangent, which follows the tangent). Areas checked from the octant decomposition: the middle route cuts the one-eighth piece into two sixteenths related by a 45-degree turn about the polar axis. → Arrows delivered: equator route (-1,0,0), middle route (-0.7071, 0, -0.7071), pole route (0,0,-1). Angles 45.00, 45.00 and 90.00 degrees, in that order and toward the same side. Twice one sixteenth is one eighth of a turn, so the halving argument and its numbers are exact, not approximate.
- Second pass, novice second-reading rewrite (entry rule): 'Of the two pieces between the routes, let the smaller be at most a quarter of the ball. The disagreement, in full turns, is twice that fraction.': Local Gauss-Bonnet for a simple loop on a sphere of radius a: the holonomy angle is the integral of K over the region, A/a^2 radians, so a fraction f of the total area 4 pi a^2 gives 4 pi f radians, that is 2f full turns. Checked the complementary piece: 2(1-f) turns differs from -2f turns by a whole turn, so the angle between the arrows is the same, and f <= 1/4 forces 2f <= half a turn, the largest angle two arrows can make. Checked that at most one of the two pieces can be at most a quarter, so 'the smaller' and 'the piece of at most a quarter' pick out the same piece. → Accurate and now unambiguous. The takeaway's older wording ('with up to a quarter of the ball between them') selects the same piece, since the larger piece is always at least a half, so it was left unchanged.
- Second pass, novice second-reading rewrite (entry problem tube-two-ways): 'the route around the far side'.: Checked against the question's viewpoint ('Hold the tube in front of you') and against the physics: a taped paper tube is a flat cylinder, whose holonomy around the bracelet loop is the identity because the developing map differs by a pure translation, with no rotation. → Wording matches the question's viewpoint and the answer stays correct: the arrows arrive matching, angle 0 degrees, tolerance 1 degree.
- Second pass, novice second-reading rewrite (spoken common question): 'near a star or a planet nobody can set up arrows over a large region that all point exactly the same way as each other'.: Translated into the exact statement: a field of arrows that any route compares as matching is a parallel vector field, which needs R^rho_{sigma mu nu} V^sigma = 0. Checked Schwarzschild in an orthonormal frame, where the nonzero components include R^{r-hat}_{t-hat t-hat r-hat} = 2M/r^3 and R^{theta-hat}_{phi-hat theta-hat phi-hat} = 2M/r^3, so no nonzero vector is annihilated by the curvature operator. → True outside a star or planet, and 'exactly' leaves room for the approximately parallel frames that do exist over small regions. Consistent with the working way, which states the condition in components.
- Small-cell mismatch V_(a first) - V_(b first) = -R^rho_{sigma mu nu} V^sigma a^mu b^nu, re-derived and tested numerically.: Re-derived the Dyson expansion step by step (single-step matrix 1 - Gamma_e - (1/2) d_e Gamma_e + (1/2) Gamma_e^2, the shift of Gamma_b to x+a, the ordered product, the subtraction, the component form, the comparison with the course Riemann convention). Then integrated the transport equation with RK4 in (theta, phi) on the unit sphere, both edge orders, at theta = 1.0 rad with delta theta = delta phi = 1e-3, starting from V = e_theta. → Numerical difference (4.5e-10, 9.9968e-07) against the predicted (0, delta theta delta phi) = (0, 1e-06): agreement to the expected third-order error. Sign, index order and the consistency with the conventions row for the loop +a, +b, -a, -b all confirmed.
- Sphere strip formula Delta alpha = Delta phi (cos theta_1 - cos theta_2), exact for finite routes, positive counterclockwise seen from outside.: Re-derived the Christoffel symbols, the vanishing of the orthonormal components along a meridian, and the rotation -Delta phi cos theta_0 along a circle of latitude (positive sense turning theta-hat toward phi-hat, and theta-hat x phi-hat = r-hat, so that sense is counterclockwise seen from outside). Checked by RK4 over the finite legs for theta_1 = 40 deg, theta_2 = 50 deg, Delta phi = 10 deg, and for the worked example theta_1 = 45 deg, theta_2 = 90 deg, Delta phi = 60 deg. → RK4 gives 1.2325683343243812 deg against the formula's 1.2325683343243865 deg, and 42.426406871192135 deg against 42.426406871192846 deg. Exact agreement to 1e-12; the check's value 1.2326 deg with tolerance 0.02 deg and the example's 42.4 deg stand, with the sense as written.
- Entry numbers: one square kilometre on a 510 million square kilometre Earth gives about 1.4 millionths of a degree, a hair's width at 3 kilometres, about 140 football pitches.: python: 2 x (1/510e6) x 360 degrees; the same angle in radians times 3000 m; 1e6 m^2 divided by 105 m x 68 m. → 1.4118e-6 degrees, 2.464e-8 rad, 73.9 micrometres (a typical hair), 140.06 pitches. All three stand.
- Problem small-rectangle-matches-formula: R^phi_{theta theta phi} = -1 and a rotation of sin theta delta theta delta phi from theta-hat toward phi-hat.: Recomputed R^theta_{phi theta phi} from the course Riemann definition on the unit sphere (sin^2 theta - cos^2 theta from the derivative term, plus cos^2 theta from the Gamma Gamma term, giving sin^2 theta), lowered and raised indices, applied the two-route formula, converted to orthonormal components, and expanded delta phi (cos theta - cos(theta + delta theta)). → R^theta_{phi theta phi} = sin^2 theta, R^phi_{theta theta phi} = -1, difference +delta theta delta phi e_phi, orthonormal tilt sin theta delta theta delta phi toward phi-hat. Matches the leading term of the exact result in size and sense, and matches the RK4 test above.
- Formal boost check: R^{r-hat}_{t-hat t-hat r-hat} = +2M/r^3 outside a spherical mass, and a rapidity of about 2M delta t delta r / r^3.: Fixed the sign from the conventions geodesic-deviation row: radial tidal stretching D^2 xi^{r-hat}/d tau^2 = +2M xi^{r-hat}/r^3 forces R^{r-hat}_{t-hat r-hat t-hat} = -2M/r^3, and antisymmetry in the last pair gives +2M/r^3. Applied the small-cell formula with u = e_{t-hat}, a = delta t e_{t-hat}, b = delta r e_{r-hat}, and checked that M delta t delta r / r^3 is dimensionless with G = c = 1. → Sign, magnitude and dimensions correct; the mismatch tilts the time direction toward e_{r-hat}, a boost.
- Fibre way and observation: parallel transport on the sphere of directions, 2 pi (1 - cos vartheta) per winding, 48.2 degrees at 30 degrees, independent of the helix radius.: Checked that de/ds = -(e . d t-hat/ds) t-hat preserves e . t-hat and |e| and is the tangential projection of de/ds on the unit sphere; computed the cap's solid angle in python. → 48.2309 degrees. Correct, and the quoted modulo 2 pi and handedness-set sense are the honest scope.
- References: Levi-Civita (1917), Tomita and Chiao (1986), Wilson (1974), Arnowitt-Deser-Misner (1962), Szabados (2009), Weyl (1918).: WebSearch against publisher, ADS, arXiv and INSPIRE records, including the page ranges. → All confirmed again, page ranges included: Rendiconti del Circolo Matematico di Palermo 42, 173-205 (DOI 10.1007/BF03014898); Physical Review Letters 57, 937-940 (DOI 10.1103/PhysRevLett.57.937); Physical Review D 10, 2445-2459 (DOI 10.1103/PhysRevD.10.2445); Witten (ed.), Wiley 1962, 227-265, arXiv gr-qc/0405109; Living Reviews in Relativity 12, 4 (DOI 10.12942/lrr-2009-4); Sitzungsberichte Berlin 1918, 465-480. No detail changed; all stay verified.

**Counterexamples tried**

- Route that crosses itself (a small circle walked on the way): the loop is not simple, so 'the fraction of the ball between the routes' was undefined in the entry rule; scoped with 'never cross themselves' in the rule, the takeaway and the one-sixteenth check.
- Two routes along the equator in opposite directions (great circle, half the ball between them): full turn, arrows match; consistent with the quarter-of-the-ball limit and with the long-way check.
- Region bigger than a quarter of the ball: the entry rule is limited to at most a quarter, so the angle between arrows stays 2f <= half a turn; no false statement.
- Mirror-image meeting spot (on the second friend's left): same quarter turn in the opposite sense; entry prose fixes one choice and speaks only of the angle between arrows.
- Real Earth with hills: a bump rising from level ground has zero total curvature by Gauss-Bonnet, and the note says 'nearly a smooth ball'; the entry number stands as an idealization.
- Paper tube (bent but flat, not simply connected): routes on opposite sides deliver matching arrows, because cylinder holonomy is trivial; tube problem correct.
- Punctured cone (flat, not simply connected): routes on opposite sides disagree by the deficit; matches the formal limits and the cone check.
- Flat spacetime with nontrivial topology (cosmic-string exterior): 'flat spacetime gives a global inertial frame' failed there; scoped to the flat spacetime of special relativity.
- Polar coordinates on the plane: nonzero Christoffel symbols, same delivered vector for every route; check correct.
- Flat connection with torsion: route independent, yet coordinate Gamma cannot vanish; formal limit correct, and the small-cell derivation indeed uses no symmetry of Gamma.
- Non-commuting case (Lorentzian, boosts and rotations): the formal way speaks of transformations, not angles, and the composition order in the key equation is correct.
- Different observers in the fibre experiment: the rotation is a relative angle between two fibres' outputs, independent of the lab frame; helix radius independence confirmed.
- Second pass. Lines a globe actually draws from the North Pole to the equator: the date line runs from pole to pole and jogs around island groups near the equator, and a mapped border need not follow a meridian. Both are counterexamples to 'every line a globe draws from the North Pole to the equator is a straight walk'; the sentence now names the evenly spaced lines.
- Second pass. Circles of latitude: not a counterexample, because they do not run from the North Pole to the equator and so were never in the scope of that sentence.
- Second pass. Straight but not shortest (the equator walked three quarters of the way round): checked that the narrowed sentence still says nothing about shortest routes, so it does not contradict the long-way check, where a straight walk is far from the shortest one.
- Second pass. Complementary piece (fifteen sixteenths instead of one sixteenth): twice the larger fraction is one turn and one eighth, the same angle between arrows; the rule's 'smaller piece, at most a quarter' picks one piece without ambiguity.
- Second pass. Two pieces of exactly half each (the equator both ways): outside the rule's quarter limit, and the long-way check answers it directly, by the arrows and not by the rule.
- Second pass. Mobius band: transport around the core reverses orientation, so the mismatch is in O(2) and not SO(2). The formal way says the mismatch lies in O(g_p), not SO(g_p), so it survives; the entry rungs speak only of a ball.
- Second pass. Punctured plane (flat, not simply connected, trivial holonomy): confirms that the note nowhere claims a hole by itself makes routes disagree; part (ii) of the theorem states simple connectivity as a hypothesis, not as a necessary condition.
- Second pass. Schwarzschild exterior as a strong-field case for the spoken gravity answer: no nonzero vector is annihilated by the curvature operator, so no parallel arrow field exists over a large region, exactly as the answer says.

**Fixes**

- Entry rule, takeaway and the one-sixteenth check (question and answer): routes must never cross themselves as well as meet only at their ends.
- Working way 'No grid of parallel axes, no total momentum': 'flat spacetime' scoped to the flat spacetime of special relativity, since flat spacetimes with nontrivial topology have no global parallel frame.
- Tutor common questions: 'the answer can depend on the route'; 'exactly matching arrows' near a star or planet, since an approximate grid does exist.
- Formal cone check: the question now names the wedge angle delta, and the answer says the hypothesis of part (ii) fails rather than part (ii). Added question_spoken for it.
- Formal boost check: 'a boost of that size' replaced by a rapidity of about 2M delta t delta r / r^3 for proper time and radial steps.
- Misconception mismatch-is-always-a-rotation: 'routes enclosing a plane' replaced by 'routes around a small cell that spans a time direction and a space direction'.
- References: all six confirmed and marked verified; DOIs added for Tomita-Chiao, Levi-Civita, Szabados and Wilson.
- Novice rewrites confirmed accurate: the halving argument with its stated assumption, 'toward the same side', the right-turn geometry at the North Pole, the mirror reason for straight walks, the 140 pitches and the hair at 3 km.
- Bumped the revision to 3; note_diff lists 7 changed learner-visible strings (6 entry, 1 working) for the novice re-read. Nothing was dropped for budget; the additions are a few words each.
- Second pass (revision 7), entry way 'Two routes to one spot': 'every line a globe draws from the North Pole to the equator' became 'each of the evenly spaced lines a globe draws from the North Pole to the equator', because a globe also draws the date line and borders from the pole to the equator that are not straight walks and have no mirror symmetry. One learner-visible string changed.
- Second pass: the other five novice second-reading changes (the meeting spot's line staying on her right, the third friend's halfway route, the smaller-piece rule, the tube problem's 'route around the far side', and the spoken gravity answer) were re-derived and confirmed accurate, with no edit.
- Second pass budget: entry way explanations rise from 1,095 to 1,099 words, inside the 1,100-word review ceiling; nothing was dropped or compressed.
- Bumped the revision to 7.

**Concerns**

- The conventions file sets no rotation sense for the coiled fibre (which handedness gives which sign); the note says only that the sense is set by the handedness. Add a conventions row before a demo or tour assigns a sign.
- Worked example id 'quarter-sphere-strip' names a quarter sphere, but the example is a 45-degree-to-equator, 60-degree strip. Ids are permanent once published; rename before publication if wanted.
- Key equation 'two routes make one loop' is justified_by 'stated', while the formal way obtains it from the composition and inverse laws, which are themselves stated; consider a one-line derivation.
- The two-routes preset of carry-an-arrow-around-a-loop has no tour for this concept; a tour should put the meeting spot on the second walker's right and narrate relative to the walker.
- Four visuals are only proposed; prerequisites differ from the registry, so run sync_registry.py.
- Entry way explanations remain slightly past the 1,000-word cap (inside the 10% review allowance); this review added about 10 words there.
- Entry way explanations now stand at 1,099 words against the 1,100-word review ceiling. Any further entry-rung fix must first shorten something; the lowest-value candidates remain the orange-segment aside in 'Two routes to one spot' and the football-pitch comparison in the Earth example.
- The takeaway of 'The disagreement follows the piece between the routes' still says 'with up to a quarter of the ball between them', where the explanation now names the smaller of the two pieces. Both pick the same piece, since the larger is always at least a half, so this is accurate as it stands; if the takeaway is ever reworded, keep the smaller-piece wording.
- Still open from earlier stages and not touched here: four proposed visuals are not in knowledge/visuals/, prerequisites differ from the registry (run sync_registry.py), the conventions file fixes no rotation sense for the coiled fibre, and the note is uncommitted in the working tree.

**Diff check** (2026-09-13, revision 5)

- Entry rule, new reason: 'Neither route may cross itself, because that would cut the ball into more than two pieces.': Euler's formula on the sphere for the closed curve formed by the two routes: a curve with k transverse self-crossings is a graph with k vertices of degree 4 and 2k edges, so V - E + F = 2 gives k + 2 pieces; a figure-eight gives 3. Tried a tangential self-touch (also more than two pieces) and a route that doubles back along a spur (excluded by the condition, which is only sufficient, so no false statement). → True at its rung: with a crossing the routes cut the ball into more than two pieces, so 'the piece between the routes' has no single meaning. Consistent with the opening paragraph ('Together they cut the ball into two pieces').
- Entry rule split into three sentences ('meet each other only at their ends'; 'Neither route may cross itself'; 'Let at most a quarter of the ball lie between the routes'); takeaway 'neither crossing itself'.: Compared with the revision-3 wording 'never cross themselves and meet each other only at their ends, with at most a quarter of the ball between them'; re-applied local Gauss-Bonnet for a simple loop (fraction f gives 2f turns, f <= 1/4 caps the angle at a half turn). → Same hypotheses and same conclusion; 'neither crossing itself' removes the reading 'never cross each other', which the separate 'meet only at their ends' already covers. Accurate.
- Check one-sixteenth-of-the-ball: question split, answer 'The routes meet only at their ends, neither route crosses itself, and one sixteenth is less than a quarter of the ball'; 45 degrees.: python: 2 x (1/16) x 360. → 45.0 degrees; the stated conditions match the rule; numeric value, magnitude sign and tolerance 2 degrees unchanged and sensible.
- Working way 'No grid of parallel axes, no total momentum': 'the theory quietly relies on this route independence twice'; 'In that spacetime the carried axes form a single-valued field of parallel axes: a global inertial frame.': Checked antecedents: 'this route independence' is the flat-floor fact that every route delivers the same arrow; 'that spacetime' is the flat spacetime of special relativity named in the previous sentence. What-if: flat spacetime with nontrivial topology (cosmic-string exterior) remains excluded because the scope is still Minkowski spacetime. In Minkowski spacetime an orthonormal frame transported everywhere is a parallel orthonormal field, whose integral coordinates are inertial. → Same claims and scope as revision 3. Accurate.
- Earth example (unchanged by the re-read, checked for consistency with the new rule): two routes meeting only at their ends with one square kilometre between them give 720/510 million degrees, about 1.4 millionths of a degree, a hair's width at 3 km, about 140 pitches.: python: 720/510e6 = 1.41e-6 degrees; angle 2.46e-8 rad times 3000 m = 74 micrometres; 1e6 m^2/(105 m x 68 m) = 140. What-if: a route that crosses itself makes 'one square kilometre between them' undefined. → Numbers correct, but the sentence applied the rule without the no-self-crossing condition the rule now states; added 'neither crossing itself'.
- Fix: Entry way 'The disagreement follows the piece between the routes', Earth example: 'Take two routes that meet only at their ends, with one square kilometre between them, about 140 football pitches.' became 'Take two routes that meet only at their ends, neither crossing itself, with one square kilometre between them, about 140 football pitches.', adopting the re-read's proposal so the example states the rule's conditions.
- Fix: All other re-read changes confirmed accurate without edits.
- Fix: Budget: entry way explanations rise by 3 words, to about 1,099, inside the 10% review allowance; nothing dropped.
- Fix: Bumped the revision to 5.

**Diff check** (2026-09-13, revision 6)

- Novice second reading, change 1 of 4 (entry): the straight walks from the North Pole are named as the lines a globe draws.: Checked the universal against what globes draw, and checked the mirror-symmetry justification that follows it. → False as a universal: the date line and mapped borders run from the pole to the equator without being straight walks. Narrowed to the evenly spaced lines; this is the one edit of the pass.
- Novice second reading, change 2 of 4 (entry): 'The line from the North Pole to the meeting spot stays on her right too, because she never steers.': Unit-sphere trace: her right is T x n = (0,1,0) at every point of the meridian walk, and the other meridian stays in the half-space on that side until they meet at the pole. → Accurate, including the reason; no edit.
- Novice second reading, change 3 of 4 (entry): the third friend walks 'straight to the equator, halfway between the start and the meeting spot'.: Exact great-circle transport along all three routes in python, plus the octant area split. → 45.00, 45.00 and 90.00 degrees, same side, and each half is one sixteenth of the ball; accurate, no edit.
- Novice second reading, change 4 of 4 (entry rule): 'Of the two pieces between the routes, let the smaller be at most a quarter of the ball. The disagreement, in full turns, is twice that fraction.': Local Gauss-Bonnet, the complementary-piece check modulo one turn, and the half-turn ceiling at f = 1/4. → Accurate and unambiguous; no edit. The takeaway's older wording selects the same piece.
- Novice second reading, wording changes outside the entry rungs: the tube problem's 'route around the far side' and the spoken gravity answer's 'arrows over a large region that all point exactly the same way as each other'.: Cylinder holonomy (trivial, a pure translation on unrolling) for the first; the parallel-vector-field condition R^rho_{sigma mu nu} V^sigma = 0 and the Schwarzschild curvature components for the second. → Both accurate; no edit.
- Fix: One of the four learner-visible changes needed an accuracy fix (the globe lines); the other three, and the two changes outside the entry rungs, stand as written.
- Fix: Bumped the revision to 7 and set review.physics.reviewed_revision to 7.

**Diff check** (2026-09-13, revision 9)

- Changed string, sentence 1 of the re-read's split: 'The equator is a straight walk.' (split out of the single 25-word sentence the physics review left at revision 7).: Computed the geodesic curvature of latitude circles on a unit ball in python, as the walker's steering rate to her left: the equator gives 0, and the circles at 15, 30, 45, 60 and 89 degrees of latitude give 0.268, 0.577, 1.000, 1.732 and 57.29 per ball radius. A straight walk in this note means never steering to either side, so only the zero case qualifies. → True and unchanged in claim: the equator is the one latitude circle that is a straight walk. The re-read's split carried no new claim, since the old sentence asserted the same thing about the equator.
- Changed string, sentence 2 of the same split: 'So is each line in the evenly spaced set a globe draws from the North Pole to the equator.': Compared extensions with the revision-7 wording 'each of the evenly spaced lines a globe draws from the North Pole to the equator': both name the meridian family a globe rules from the pole to the equator, so the same lines are claimed straight. Computed the geodesic curvature along meridians at longitudes 0, 10, 15, 37 and 350 degrees, at latitudes 30 and 75 degrees: 0 in every case, to machine precision. → Same scope and same truth value. The move of 'evenly spaced' from the individual line to the set does not weaken or widen the claim, and the computation confirms that even spacing is not what makes a line straight, which is what the re-read set out to stop the sentence from implying.
- What-if on the unchanged phrase 'a globe draws from the North Pole to the equator': could it be read as the evenly spaced circles a globe draws between the North Pole and the equator?: Read the phrase against the two sentences that follow it ('Her line to the North Pole crosses the equator at a right angle') and against the latitude-circle numbers above, which show that every latitude circle except the equator steers. → The reading in which the lines run from the pole to the equator is the one the rest of the way uses, and it is the true one; the circle reading would be false. No edit: the phrase is unchanged from the revision-7 text, and naming meridians outright would cost a term the entry rung does not have.
- Scope decision the re-read referred here: 'For each of these lines, the ball on one side is a mirror image of the ball on the other side', where 'these lines' could mean the globe's pole-to-equator lines alone or those together with the equator.: Checked both scopes as isometries of the ball in python. For the equator, reflection in the plane of the equator fixes every equator point and every walking direction along it exactly, and sends the walker's left to her right exactly. For meridians at longitudes 0, 10, 15, 37.3 and 123 degrees, reflection in the plane through the axis and that meridian fixes the line pointwise and swaps left and right, at every latitude sampled from 0 to 90 degrees. → The mirror reason is true for the equator as well as for each of the globe's lines, so the wide scope is the accurate one, and it is the scope the sentence had before the revision-7 narrowing. Widened the sentence to say so, which also gives the equator the reason it was missing.
- Consequence sentence, reread after the widening: 'A walker on one of them therefore has no reason to steer either way.': Checked that the mirror argument delivers this for the wider antecedent: at each point the reflection fixes the walker's position and heading and exchanges her left with her right, so a steering rate to the left would have to equal its own negative. Matched against the computed geodesic curvatures, which are zero for the equator and for every meridian. → True for every curve now covered by 'them'. No edit.
- Fix: Way 'Two routes to one spot': 'For each of these lines, the ball on one side is a mirror image of the ball on the other side.' became 'For the equator and these lines, the ball on one side is a mirror image of the ball on the other side.' This adopts the re-read's proposal one word more cheaply, fixes the scope to the true and originally intended one, and leaves the reader no straight walk without a reason.
- Fix: The two changed sentences of the re-read confirmed accurate with no edit.
- Fix: Budget: entry way explanations rise by one word, from 1,099 to 1,100, exactly the 1,000-word core cap plus the 10% allowance for recorded fixes. Nothing dropped and nothing compressed.
- Fix: Bumped the revision to 9. A novice sign-off covers the one changed sentence.
