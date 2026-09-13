---
type: "concept"
schema_version: 2
id: "riemann-curvature-tensor"
title: "Riemann curvature tensor"
tagline: "The full table of how space and time curve at each place"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 2
updated: "2026-09-13"
aliases: ["Riemann tensor", "curvature tensor", "Riemann-Christoffel tensor"]
prerequisites: ["parallel-transport", "path-dependence-of-parallel-transport", "tidal-force", "christoffel-symbols", "covariant-derivative", "tensor", "newtonian-tidal-tensor", "lie-bracket", "levi-civita-connection"]
leads_to: ["symmetries-of-the-riemann-tensor", "number-of-independent-riemann-components", "ricci-tensor", "geodesic-deviation-equation", "flatness-criterion", "ricci-identity", "riemann-tensor-in-normal-coordinates", "weyl-tensor", "kretschmann-scalar", "linearized-riemann-tensor", "curvature-sign-conventions", "bianchi-identity"]
visuals: ["tilt-a-tiny-loop-at-one-point", "falling-ring-of-crumbs", "shrink-the-loop-to-find-riemann", "four-terms-that-cancel", "twenty-of-256-slots"]
---

# Riemann curvature tensor

*The full table of how space and time curve at each place*

`riemann-curvature-tensor` · curvature · core · physics-reviewed (revision 2)

**Needs:** [[parallel-transport]] (entry) · [[path-dependence-of-parallel-transport]] (entry) · [[tidal-force]] (entry) · [[christoffel-symbols]] (working) · [[covariant-derivative]] (working) · [[tensor]] (working) · [[newtonian-tidal-tensor]] (working) · [[lie-bracket]] (formal) · [[levi-civita-connection]] (formal)  
**Opens:** [[symmetries-of-the-riemann-tensor]] · [[number-of-independent-riemann-components]] · [[ricci-tensor]] · [[geodesic-deviation-equation]] · [[flatness-criterion]] · [[ricci-identity]] · [[riemann-tensor-in-normal-coordinates]] · [[weyl-tensor]] · [[kretschmann-scalar]] · [[linearized-riemann-tensor]] · [[curvature-sign-conventions]] · [[bianchi-identity]]  
**Related:** [[holonomy]] · [[nonzero-christoffel-symbols-in-flat-space]] · [[gaussian-curvature]] · [[local-flatness-theorem]] · [[gauge-field-strength]] · [[curvature-2-form]]  
**Visuals:** ★ [[tilt-a-tiny-loop-at-one-point]] · [[falling-ring-of-crumbs]] · [[shrink-the-loop-to-find-riemann]] · [[four-terms-that-cancel]] · [[twenty-of-256-slots]]

> Carry an arrow around a tiny loop without letting it swing. The Riemann curvature tensor records how the arrow comes back changed, for every tilt of the loop and every starting direction. In a space with three or more directions, one number is not always enough, so it is a table kept at every place. The same table sets how neighbouring falling objects drift together or apart.

## You will be able to

**Entry**
- Explain why the curving at a spot of a space with three or more directions can need a whole table of numbers rather than one. `objectives/explain-why-a-table` ← `checks/two-tilts-in-the-building`, `checks/count-the-tilts`
- Predict whether neighbouring falling objects drift together or apart, and estimate how much near Earth. `objectives/predict-falling-drift` ← `checks/side-by-side-drop`, `problems/tower-drop`

**Working**
- Compute Riemann components from Christoffel symbols for a two-dimensional metric, including a flat control. `objectives/compute-components` ← `checks/polar-plane-zero`, `problems/hyperbolic-plane`
- Use the small-loop law and the component formula to predict antisymmetry and linearity, and to judge what the tensor is built from. `objectives/read-the-slots` ← `checks/swap-the-edges`, `checks/second-derivatives-claim`
- Compute tidal components and relative accelerations from the weak-field form of the tensor. `objectives/compute-tidal-components` ← `checks/vacuum-tides`, `problems/astronaut-stretch`

**Formal**
- Prove that the curvature operator is linear over functions and therefore a tensor. `objectives/prove-tensor-property` ← `problems/prove-function-linearity`
- Count the independent components in n dimensions and state what they do and do not represent. `objectives/count-and-interpret-components` ← `checks/count-and-meaning`
- State the flatness criterion with its hypotheses and translate signs across signature conventions. `objectives/state-flatness-and-signs` ← `checks/flatness-hypotheses`, `checks/sign-under-metric-flip`

## Ways in

### 1. A table of turns for tiny loops · entry · picture

*Why does the curving at one spot need a whole table of numbers, not just one?*

**Recap:** The arrow test: press a cardboard arrow against the ground and walk a loop, a path that ends where it began. Never let the arrow swing left or right. On a flat floor it comes back matching its start. On a ball, most loops bring it back turned.

Draw a tiny square loop on a smooth ball, one centimetre along each side. Carry a cardboard arrow around it, pressed against the surface, and never let it swing. The arrow comes back turned by a small amount. Two such squares side by side give twice the turn, because their shared side is walked once each way, and those two trips cancel.

So at that spot, one number describes how curved the ball is: the turn divided by the area of the loop. One number is enough because the surface offers only two directions to move in, ahead and sideways.

The space around you has three directions: ahead, sideways and up. At one spot, a tiny square loop could lie level like the bottom of a box, or stand upright like its front or its side. These are three tilts of the loop. The arrow test works here too, if the arrow never swings any way at all, not even up or down.

A curved space with three directions can give different answers for different tilts. Picture a made-up building whose floors are not flat slabs. Each floor is the whole surface of a huge ball, and every floor is an exact copy of the same ball. The floors are close together. A lift joins each spot to the matching spot on the next floor.

Start at one spot with a fresh arrow pressed against the floor. A tiny loop along the floor brings the arrow back turned, because the floor is a ball's surface. Now walk an upright loop: ride the lift up one floor, walk a short way ahead without steering, ride down, and walk the same distance back.

Every floor is an exact copy, so after each lift ride the arrow points toward the copy of whatever it pointed toward before. The walk ahead and the walk back are the same stretch on identical floors, in opposite directions. So the arrow comes back matching its start.

Same spot, two tilts, two answers. The starting direction matters too: an arrow pointing along the lift shaft comes back from the floor loop matching its start, because every spot's lift shaft is alike. So one number cannot describe the curving at a spot here. You need a table.

For each tilt of a tiny loop and each starting direction of the arrow, the table lists how the arrow comes back changed, divided by the loop's area. Walking the other way round gives the opposite change, so one way round is enough. This table is called the Riemann curvature tensor.

Each tilt is a pair of directions, like two edges of the box, so three directions give three tilts. To meet a friend you name a place and a time, so time counts as a fourth direction, and four directions give six pairs. Nobody can walk a loop backward in time, but falling objects measure entries for tilts that include time.

Earth's ground is nearly a ball. A loop around one square kilometre of it turns an arrow by about 1.4 millionths of a degree, the angle across a hair's width from 3 kilometres away. The curving of space and time near Earth is roughly a billion times weaker still.

**Try it:** Write ahead, sideways, up and time on four slips of paper. List every pair of slips you can pick up together. You should find six pairs, so a tiny loop in space and time can be tilted in six basic ways.

**Takeaway:** At one spot, a curved space can turn an arrow differently for loops at different tilts, so describing its curving can take a whole table: the Riemann curvature tensor.

*What this leaves out:* The building world is made up to isolate one idea. In spacetime the change the table records can go beyond a turn. Many entries repeat others or follow from them, so fewer different numbers are needed: twenty in spacetime.

*Builds on:* [[parallel-transport]], [[path-dependence-of-parallel-transport]]<br>*Visuals:* [[tilt-a-tiny-loop-at-one-point]]<br>*See:* `worked_examples/multi-storey-ball-world`

### 2. Falling side by side · entry · operational

*What can two falling balls tell us about the curving of space and time?*

**Recap:** The Riemann curvature tensor is a table kept at every place. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed after being carried around the loop without swinging. Tilts are pairs of directions, and time counts as a direction.

Hang two steel balls side by side, one metre apart, at the top of a tall tube with the air pumped out. A single catch lets both go at once. They fall freely: nothing but gravity acts on them.

Each ball falls toward the centre of Earth. Like two spokes of a wheel, their paths lead to the same point, so the balls drift slightly toward each other.

How much? Between two spokes, the gap is in proportion to the distance from the centre, here 6,371 kilometres. A 100-metre fall shrinks that distance by 100 parts in 6,371,000, and the one-metre gap by the same fraction. That is 16 thousandths of a millimetre, about a fifth of a hair's width. So nobody notices it.

Now hang the balls one under the other, a metre apart. The lower ball is nearer the centre by one part in 6,371,000. Gravity weakens with the square of distance, so its pull is stronger by about two parts: squaring doubles a tiny excess, as 1.001 times 1.001 is about 1.002. The side-by-side pulls only lean together by one part. So this gap grows twice as fast, by 31 thousandths of a millimetre over the same fall.

This pattern is called tidal drift: falling objects spread apart along the line toward Earth's centre and draw together across it. Inside a freely falling lift you would float, yet two crumbs floating beside you would still drift. Falling removes the feeling of weight, not this drift.

Why is this drift curving? On a flat floor, two people who set off side by side, facing the same way, and walk without steering stay the same distance apart. On a ball, two such walkers leaving the equator toward the North Pole draw together and meet there. On a saddle, which curves the opposite way, they spread apart.

Each moment of a falling ball's trip has a place and a time, so its path runs through a world with four directions. This world of space and time together is called spacetime. Nothing pushes or steers a falling ball, so its path through spacetime is a walk without steering.

Both balls start at rest, so their paths set off side by side, like the walkers. The side-by-side pair then draws together, as on the ball, and the other pair spreads apart, as on the saddle. The Riemann curvature tensor records both, in entries for two tilts: time with sideways, and time with the line toward Earth's centre.

**Takeaway:** Near Earth, balls falling side by side drift together, and balls falling one under the other drift apart; this tidal drift shows spacetime's curving, and the Riemann tensor records it.

*What this leaves out:* We treated Earth as a perfect ball that does not spin, and ignored the pull of the two balls on each other. The drift numbers come from Newton's gravity, which is extremely accurate near Earth.

*Continues:* `ways_in/a-table-of-turns`<br>*Builds on:* [[tidal-force]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `problems/tower-drop`

### 3. Four slots and the component formula · working · calculation

*How are the components computed from the connection, and what job does each index do?*

The table of turns in "A table of turns for tiny loops" becomes an array of numbers once coordinates are chosen. Carry a vector $V$ around a tiny coordinate parallelogram, walking $+a$, then $+b$, then $-a$, then $-b$. To second order in the loop's size, in the course sign conventions,

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu.$$

The product $a^\mu b^\nu$ carries the loop's area, so the components are the entry picture's change per unit area, and the index pair $\mu\nu$ is its tilt. This small-loop law is taken on trust here; the note on holonomy builds it step by step from the transport equation.

Each index has a job. The slot $\sigma$ takes the carried vector, $\mu$ and $\nu$ take the two edges, and $\rho$ picks the component of the change you read. The change $\Delta V$ is a vector at the starting point, linear in $V$, $a$ and $b$ in every coordinate system, so the quotient theorem makes $R^\rho{}_{\sigma\mu\nu}$ a $(1,3)$ tensor. Swapping $a$ and $b$ walks the same parallelogram the other way round, so $R^\rho{}_{\sigma\mu\nu} = -R^\rho{}_{\sigma\nu\mu}$.

In a coordinate basis the components are

$$R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.$$

To remember it, treat $(\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}$ as one matrix for each $\mu$. The formula becomes $\partial_\mu\Gamma_\nu - \partial_\nu\Gamma_\mu + [\Gamma_\mu, \Gamma_\nu]$: how the connection changes across the loop, plus how its steps along the two edges fail to commute.

The same tensor answers a second question. For a torsion-free connection, differentiating covariantly in two orders and subtracting leaves no derivatives of $V$:

$$[\nabla_\mu, \nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma,$$

as the derivation "Covariant derivatives in two orders" shows. Since the left side is a tensor for every $V$, this proves the tensor property a second way.

In an orthonormal frame every component has units of inverse length squared, a turn per unit area, as the loop test suggests. On a sphere of radius $a$ the one independent orthonormal component is $1/a^2$.

**Takeaway:** The Riemann tensor has four slots, the carried vector, two loop edges and the output component, and its components come from the Christoffel symbols and their first derivatives.

*What this leaves out:* Leading order in the loop size, for a torsion-free connection; the component formula holds only in a coordinate basis.

*Continues:* `ways_in/a-table-of-turns`<br>*Builds on:* [[christoffel-symbols]], [[covariant-derivative]], [[tensor]]<br>*Visuals:* [[shrink-the-loop-to-find-riemann]]<br>*See:* `holonomy/derivations/small-loop-law-from-transport`, `derivations/ricci-identity-in-coordinates`, `checks/swap-the-edges`

### 4. Coordinates cannot fake it · working · contrast

*Can curved coordinate lines make a flat plane look curved to the Riemann tensor?*

The component formula of "Four slots and the component formula" is built from Christoffel symbols, which are not tensor components and can be nonzero on a perfectly flat plane. In polar coordinates, $ds^2 = dr^2 + r^2 d\phi^2$, the nonzero symbols are $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$. They record how the coordinate basis vectors change from point to point, not any curving of the plane.

Put them into the formula for $R^r{}_{\phi r\phi}$. The derivative term gives $\partial_r(-r) = -1$. The last product term gives $-\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = +1$. Every other term vanishes, so the component is $0$, and the remaining components vanish the same way. On a sphere the same bookkeeping does not cancel: the worked example "The multi-storey ball world" finds $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$.

The cancellation on the plane is guaranteed. The Riemann tensor's components in one coordinate system are linear combinations of its components in any other. In Cartesian coordinates every Christoffel symbol vanishes everywhere, so every Riemann component vanishes there, and therefore in polar or any other coordinates. The useful direction is the converse: compute the Riemann tensor in whatever coordinates the metric arrives in, and a nonzero component can never be removed by relabelling points.

Flat spacetime described by observers at rest in a uniformly accelerating rocket is the spacetime version. Their coordinates have nonzero Christoffel symbols, their clocks at different heights tick at different rates, and the Riemann tensor is exactly zero.

**Takeaway:** Nonzero Christoffel symbols can come from curved coordinate lines alone; the Riemann tensor is zero in every coordinate system exactly when it is zero in one.

*Continues:* `ways_in/slots-of-the-table`<br>*Builds on:* [[christoffel-symbols]], [[tensor]]<br>*Visuals:* [[four-terms-that-cancel]]<br>*See:* `checks/polar-plane-zero`, `worked_examples/multi-storey-ball-world`

### 5. Tidal accelerations measure it · working · operational

*How does an instrument in free fall read off components of the Riemann tensor?*

The balls in "Falling side by side" drift together or apart, and that drift reads the Riemann tensor directly. Two neighbouring freely falling worldlines, with four-velocity $u^\mu$ and small separation $\xi^\mu$, obey the geodesic deviation equation, taken on trust here:

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma.$$

In a freely falling frame riding with one ball, $u^\mu = (c, 0, 0, 0)$ and the separation is spatial, so $\ddot\xi^i = -c^2R^i{}_{0j0}\,\xi^j$. An accelerometer on either ball reads zero. Only the relative acceleration, measured for instance by timing light sent between the balls, carries the curvature.

For a static weak field with Newtonian potential $\Phi$, the derivation "Weak static field gives Newtonian tides" finds $R^i{}_{0j0} = \partial_i\partial_j\Phi/c^2$. Geodesic deviation then becomes Newton's tidal equation, $\ddot\xi^i = -\partial_i\partial_j\Phi\,\xi^j$.

Outside a spherical mass, $\Phi = -GM/r$. The second derivative along the radial direction is $-2GM/r^3$, and along each transverse direction it is $+GM/r^3$. So radial pairs separate at $2GM/r^3$ per unit separation, and transverse pairs approach at $GM/r^3$. At Earth's surface, $r = 6371$ km and $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$, so for $z$ along the local vertical $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. A 100 m drop lasts 4.51 s, and $\tfrac12(GM/r^3)(1\ \mathrm{m})(4.51\ \mathrm{s})^2 = 1.57\times10^{-5}$ m is the sideways drift of the falling balls.

The three diagonal entries are proportional to $-2$, $1$ and $1$, which sum to zero because $\nabla^2\Phi = 0$ in empty space. Empty space still has tides. Einstein's vacuum equation, without a cosmological constant, sets only a contraction of the Riemann tensor to zero; in four dimensions the rest of the tensor can be nonzero. The tidal measurements of one freely falling observer give only the six components $R^i{}_{0j0}$ in that observer's frame.

**Takeaway:** The relative acceleration of neighbouring free-fall worldlines is minus the Riemann tensor fed the velocity, the separation and the velocity; in weak fields it is the Hessian of the Newtonian potential.

*What this leaves out:* Weak static field and slow test masses for the Newtonian form; separations small compared with the distance over which the curvature changes.

*Continues:* `ways_in/falling-side-by-side`, `ways_in/slots-of-the-table`<br>*Builds on:* [[newtonian-tidal-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/weak-field-tides`, `observations/atom-gravity-gradiometer`, `observations/gw150914-arm-response`

### 6. The curvature operator and its symmetries · formal · structure

*What is the Riemann tensor without coordinates, and which identities and theorems constrain it?*

The four slots of "Four slots and the component formula" and its commutator $[\nabla_\mu, \nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$ have a coordinate-free form. For a connection $\nabla$ on a manifold $M$ and vector fields $X, Y, Z$, define

$$\mathcal{R}(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z.$$

The bracket term makes $\mathcal{R}$ linear over functions: $\mathcal{R}(fX,Y)Z = \mathcal{R}(X,Y)(fZ) = f\,\mathcal{R}(X,Y)Z$ for every smooth $f$, and antisymmetry handles the $Y$ slot. A map linear over functions acts pointwise, so $\mathcal{R}$ is a $(1,3)$ tensor field with components $R^\rho{}_{\sigma\mu\nu} = dx^\rho\big(\mathcal{R}(\partial_\mu,\partial_\nu)\partial_\sigma\big)$. In a coordinate basis $[\partial_\mu,\partial_\nu] = 0$, and $\nabla_{\partial_\mu}\partial_\sigma = \Gamma^\lambda{}_{\mu\sigma}\partial_\lambda$ reproduces the component formula. In a non-coordinate frame the bracket term contributes the frame's commutation coefficients. On a covector, $[\nabla_\mu,\nabla_\nu]\omega_\sigma = -R^\lambda{}_{\sigma\mu\nu}\omega_\lambda$, with one such term per index on higher tensors, for a torsion-free connection.

For the Levi-Civita connection of $g$, lower the first index:

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma},\qquad R_{\rho[\sigma\mu\nu]} = 0.$$

Antisymmetry in the first pair expresses $\nabla g = 0$: small-loop holonomy is an infinitesimal rotation or boost. The cyclic identity needs zero torsion, and pair exchange follows from the other three. So at each point $\mathcal{R}$ is a symmetric map of bivectors, a symmetric $6\times6$ array in four dimensions subject to one cyclic condition, leaving $20$ independent components. In two dimensions one function remains, $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ with $K$ the Gaussian curvature. In three dimensions the Ricci contraction determines $\mathcal{R}$; in four or more, the trace-free Weyl part is independent of it. The second Bianchi identity, $\nabla_{[\lambda}R_{\rho\sigma]\mu\nu} = 0$, constrains derivatives.

Flatness criterion: for the Levi-Civita connection, $\mathcal{R} = 0$ on an open set exactly when every point has a neighbourhood with coordinates in which $g_{\mu\nu}$ is constant. Transport is then unchanged under deformations of a path with fixed ends. The statement is local: a flat cone with its tip removed, or a flat torus, has $\mathcal{R} = 0$ without being globally Euclidean.

Signs: $\Gamma^\lambda{}_{\mu\nu}$ and $R^\rho{}_{\sigma\mu\nu}$ are unchanged under $g \to -g$, while $R_{\rho\sigma\mu\nu}$ and the Ricci scalar change sign. The course fixes the overall sign so that a sphere of radius $a$ has Ricci scalar $+2/a^2$.

**Takeaway:** Curvature is covariant derivatives along two fields in both orders minus the derivative along their bracket; it is function-linear, and for Levi-Civita a symmetric map of bivectors that vanishes exactly where space is locally flat.

*Picture:* At a point, a machine that takes an oriented 2-plane and returns an infinitesimal rotation or boost of the tangent space, symmetric under exchanging the plane it is fed with the plane of the rotation it returns.

*What this leaves out:* Assumes a torsion-free connection for the covector rule and the cyclic identity; the operator definition holds for any connection on any vector bundle.

*Continues:* `ways_in/slots-of-the-table`, `ways_in/coordinates-cannot-fake-it`<br>*Builds on:* [[lie-bracket]], [[levi-civita-connection]]<br>*See:* `problems/prove-function-linearity`, `checks/flatness-hypotheses`, `checks/sign-under-metric-flip`

### 7. Twenty numbers coordinates cannot remove · formal · calculation

*Why does spacetime curvature carry exactly twenty independent numbers at each event?*

"Coordinates cannot fake it" showed that no change of coordinates removes a nonzero Riemann component. Counting coordinate freedom at one event $p$ shows how many such numbers exist, before any symmetry is proved. Expand the metric and a general coordinate change in Taylor series about $p$, and compare at each order the numbers to be fixed with the numbers available. The derivation "Count what coordinates cannot remove" finds, in four dimensions, that $g_{\mu\nu}(p)$ can be set to $\eta_{\mu\nu}$ with 6 Lorentz transformations to spare, all 40 first derivatives can be set to zero, and 20 of the 100 second derivatives survive every choice.

In such coordinates $\Gamma^\lambda{}_{\mu\nu}(p) = 0$, the component formula keeps only its derivative terms, and $R_{\rho\sigma\mu\nu}(p)$ is a combination of second derivatives of $g$ that no remaining coordinate change alters. Its independent components number $n^2(n^2-1)/12$: 0, 1, 6 and 20 for $n = 1, 2, 3, 4$, matching the leftover count in every dimension. A curve has no intrinsic curvature, and a surface has one number, its Gaussian curvature.

This sharpens the equivalence principle. A freely falling observer can make the metric Minkowskian, with vanishing first derivatives, at an event, but no choice of observer or coordinates removes the 20 second-order numbers. That is why tidal measurements are coordinate-independent evidence of gravity. The 20 are values at one event, not twenty kinds of gravitational wave: vacuum radiation has two polarizations, and Einstein's equations tie the 10 Ricci components to the local matter.

**Takeaway:** At an event coordinates can fix the metric and its first derivatives, but 20 combinations of second derivatives always survive, and they are the independent Riemann components.

*What this leaves out:* Local statement at one event, for a smooth metric in four dimensions; the general count is for any dimension.

*Continues:* `ways_in/coordinates-cannot-fake-it`<br>*Visuals:* [[twenty-of-256-slots]]<br>*See:* `derivations/count-what-coordinates-cannot-remove`, `checks/count-and-meaning`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To move the arrow so that it points a different way. Along the ground that means left or right; with more directions to move in, it means any way at all, even up or down. The arrow test never lets it swing. | — |
| tilt | — | The way a tiny loop is angled at a spot, set by the two directions its sides run along, like the bottom, front or side of a box. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every place. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed, divided by the loop's area. The arrow goes around the loop without swinging. | [[riemann-curvature-tensor]] |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tidal drift | — | The way gravity makes neighbouring falling objects outside a round planet spread apart along the line toward its centre and draw together across it. | [[tidal-force]] |
| spacetime | — | Space and time taken together as one world with four directions: three of space and one of time. | [[spacetime]] |

## Key equations

### Riemann tensor from the connection · working

$$
R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}
$$

The components in a coordinate basis: how the connection changes across the $\mu\nu$ plane, plus connection matrices multiplied in two orders.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor: $\sigma$ the carried vector, $\mu\nu$ the loop plane, $\rho$ the output component | the Riemann tensor |
| $\Gamma^\rho{}_{\mu\sigma}$ | Christoffel symbols, derivative index first | the Christoffel symbols |

**Holds when:** Coordinate basis; course index order. In a non-coordinate frame, commutation coefficients add terms.  
**Say it:** “The Riemann tensor is the derivative along mu of the connection in the nu direction, minus the same with mu and nu swapped, plus the connection matrices multiplied in one order, minus the other order.”  
**Justified by:** `stated`

### Small-loop law · working

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu
$$

A vector carried around a tiny parallelogram changes by minus the tensor fed the vector and the two edges.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta V^\rho$ | change after one trip | the change in the vector |
| $a^\mu,\ b^\nu$ | edges, walked $+a, +b, -a, -b$ | the two edges |

**Holds when:** Torsion-free connection; second order in the loop size.  
**Say it:** “The change in the vector is minus the Riemann tensor acting on the vector and the two edges.”  
**Justified by:** `stated`

### Commutator of covariant derivatives · working

$$
[\nabla_\mu, \nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma
$$

Covariant derivatives taken in two orders differ by the tensor acting on the field, with no derivatives of the field.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\mu$ | covariant derivative | nabla mu |

**Holds when:** Torsion-free connection; one term with a minus sign for each lower index.  
**Say it:** “Nabla mu nabla nu minus nabla nu nabla mu, acting on V, equals the Riemann tensor acting on V.”  
**Justified by:** `derivations/ricci-identity-in-coordinates`

### Geodesic deviation · working

$$
\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma
$$

Neighbouring free-fall worldlines accelerate apart by minus the tensor fed velocity, separation and velocity.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^\mu$ | separation vector | the separation |
| $u^\mu$ | four-velocity, $u_\mu u^\mu = -c^2$ | the four-velocity |

**Holds when:** Geodesics; separation small compared with the curvature scale.  
**Say it:** “The relative acceleration equals minus the Riemann tensor fed the velocity, the separation and the velocity.”  
**Justified by:** `stated`

### Tidal components of a weak static field · working

$$
R^i{}_{0j0} = \frac{1}{c^2}\,\frac{\partial^2\Phi}{\partial x^i\,\partial x^j}
$$

In a weak static field, the space-time-space-time components are the Hessian of the Newtonian potential.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Phi$ | Newtonian potential, $g_{00} = -(1 + 2\Phi/c^2)$ | the potential |

**Holds when:** Static, first order in $\Phi/c^2$, $x^0 = ct$.  
**Say it:** “R upper i, lower zero j zero, equals the second derivative of the potential along i and j, divided by c squared.”  
**Justified by:** `derivations/weak-field-tides`

### Curvature operator · formal

$$
\mathcal{R}(X,Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X,Y]}Z
$$

The coordinate-free definition, linear over functions in all three slots.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $[X,Y]$ | Lie bracket | the bracket of X and Y |

**Holds when:** Any connection; components $R^\rho{}_{\sigma\mu\nu} = dx^\rho(\mathcal{R}(\partial_\mu,\partial_\nu)\partial_\sigma)$.  
**Say it:** “The curvature of X and Y acting on Z is nabla X nabla Y minus nabla Y nabla X minus nabla along the bracket of X and Y.”  
**Justified by:** `stated`

### Algebraic symmetries · formal

$$
R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma},\qquad R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0
$$

Pair antisymmetries, pair exchange and the cyclic identity.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\rho\sigma\mu\nu}$ | first index lowered with $g$ | the all-lower Riemann tensor |

**Holds when:** Levi-Civita connection.  
**Say it:** “The all-lower Riemann tensor flips sign within either pair, is unchanged when the pairs swap, and its cyclic sum over the last three indices vanishes.”  
**Justified by:** `stated`

### Number of independent components · formal

$$
N(n) = \frac{n^2(n^2-1)}{12}
$$

1, 6 and 20 in two, three and four dimensions.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $n$ | dimension | n |

**Holds when:** Levi-Civita connection; counts components at one point.  
**Say it:** “n squared times n squared minus one, over twelve.”  
**Justified by:** `derivations/count-what-coordinates-cannot-remove`

## Derivations

### Covariant derivatives in two orders · working

**Goal:** Show that $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$ for a torsion-free connection.

1. $\nabla_\nu V^\rho$ is a $(1,1)$ tensor, so $\nabla_\mu\nabla_\nu V^\rho = \partial_\mu(\nabla_\nu V^\rho) + \Gamma^\rho{}_{\mu\lambda}\nabla_\nu V^\lambda - \Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$.
2. Antisymmetrize in $\mu\nu$. The last term drops out because $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$ without torsion.
3. Expand the rest: $\partial_\mu\partial_\nu V^\rho + (\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma + \Gamma^\rho{}_{\nu\sigma}\partial_\mu V^\sigma + \Gamma^\rho{}_{\mu\lambda}\partial_\nu V^\lambda + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}V^\sigma$.
4. $\partial_\mu\partial_\nu V^\rho$ and the pair $\Gamma^\rho{}_{\nu\sigma}\partial_\mu V^\sigma + \Gamma^\rho{}_{\mu\lambda}\partial_\nu V^\lambda$ are symmetric in $\mu\nu$, so they cancel.
5. What remains is $\big(\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}\big)V^\sigma$, the course $R^\rho{}_{\sigma\mu\nu}V^\sigma$.

**Result:** $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$; the left side is a tensor for every $V$, so by the quotient theorem $R^\rho{}_{\sigma\mu\nu}$ is a tensor.

### Weak static field gives Newtonian tides · working

**Goal:** Find $R^i{}_{0j0}$ for $g_{00} = -(1 + 2\Phi/c^2)$, $g_{ij} = (1 - 2\Phi/c^2)\delta_{ij}$ to first order, and recover Newton's tidal equation.

1. With $x^0 = ct$ and no time dependence, $\Gamma^i{}_{00} = -\tfrac12\partial_i g_{00} = \partial_i\Phi/c^2$ to first order, while $\Gamma^i{}_{j0} = 0$.
2. The component formula gives $R^i{}_{0j0} = \partial_j\Gamma^i{}_{00} - \partial_0\Gamma^i{}_{j0} + \Gamma^i{}_{j\lambda}\Gamma^\lambda{}_{00} - \Gamma^i{}_{0\lambda}\Gamma^\lambda{}_{j0}$.
3. The time derivative vanishes, and each product of Christoffel symbols is second order in $\Phi/c^2$, so $R^i{}_{0j0} = \partial_i\partial_j\Phi/c^2$.
4. For slow test masses, $u^\mu \approx (c,0,0,0)$ and $\tau \approx t$, so geodesic deviation gives $\ddot\xi^i = -c^2R^i{}_{0j0}\xi^j = -\partial_i\partial_j\Phi\,\xi^j$.

**Result:** $R^i{}_{0j0} = \partial_i\partial_j\Phi/c^2$, and geodesic deviation becomes $\ddot\xi^i = -\partial_i\partial_j\Phi\,\xi^j$.

### Count what coordinates cannot remove · formal

**Goal:** Count the second derivatives of the metric at an event that no coordinate change can alter.

1. Put the event $p$ at the origin and expand $x^\mu = A^\mu{}_\nu x'^\nu + \tfrac12 B^\mu{}_{\nu\lambda}x'^\nu x'^\lambda + \tfrac16 C^\mu{}_{\nu\lambda\kappa}x'^\nu x'^\lambda x'^\kappa + \dots$, with $B$ and $C$ symmetric in their lower indices.
2. Order zero: $g_{\mu\nu}(p)$ has 10 values and $A$ has 16 entries, so $g'_{\mu\nu}(p) = \eta_{\mu\nu}$ is reachable with 6 to spare, the Lorentz transformations.
3. Order one: $\partial_\lambda g_{\mu\nu}(p)$ has 40 values and $B$ has 40 entries. The map from $B$ has no kernel, since a tensor antisymmetric in one index pair and symmetric in an overlapping pair vanishes, so every $\partial g(p)$ can be set to zero.
4. Order two: $\partial_\kappa\partial_\lambda g_{\mu\nu}(p)$ has $10\times10 = 100$ values and $C$ has $4\times20 = 80$ entries. The map from $C$ again has no kernel, so exactly 20 combinations are untouched.
5. In $n$ dimensions: $\big(\tfrac{n(n+1)}{2}\big)^2 - n\,\tfrac{n(n+1)(n+2)}{6} = \tfrac{n^2(n^2-1)}{12}$.

**Result:** At an event, 20 combinations of second metric derivatives survive every coordinate change in four dimensions, and $n^2(n^2-1)/12$ in $n$, the number of independent components of $R_{\rho\sigma\mu\nu}$.

## Worked examples

### The multi-storey ball world · working

**Problem:** The metric $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2) + dz^2$ stacks copies of a sphere of radius $a$ along $z$. Find its nonzero Riemann components, and use the small-loop law to compare loops in the $\theta\phi$ and $\theta z$ planes.

1. Only $g_{\phi\phi} = a^2\sin^2\theta$ varies. The nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$; none carries a $z$ index or depends on $a$.
2. $R^\theta{}_{\phi\theta\phi} = \partial_\theta\Gamma^\theta{}_{\phi\phi} - \Gamma^\theta{}_{\phi\phi}\Gamma^\phi{}_{\theta\phi} = (\sin^2\theta - \cos^2\theta) + \cos^2\theta = \sin^2\theta$.
3. $R^\phi{}_{\theta\phi\theta} = -\partial_\theta\cot\theta - \cot^2\theta = 1$. Every component with a $z$ index vanishes, since no Christoffel symbol has one.
4. Loop in the $\theta z$ plane, $a^\theta = \delta\theta$, $b^z = \delta z$: $\Delta V^\rho = -R^\rho{}_{\sigma\theta z}V^\sigma\delta\theta\,\delta z = 0$ for every $V$.
5. Loop in the $\theta\phi$ plane: $\Delta V^\theta = -\sin^2\theta\,V^\phi\,\delta\theta\,\delta\phi$, nonzero for $V^\phi \neq 0$.
6. Orthonormal component: $R_{\theta\phi\theta\phi}/(g_{\theta\theta}g_{\phi\phi}) = a^2\sin^2\theta/(a^4\sin^2\theta) = 1/a^2$.

**Answer:** $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and $R^\phi{}_{\theta\phi\theta} = 1$, with their sign-flipped partners; all components with a $z$ index vanish. Loops in planes containing $z$ return vectors unchanged, and the orthonormal component in the $\theta\phi$ plane is $1/a^2$.

**Takeaway:** One point, two planes, two answers: the tensor depends on the loop plane, and each sphere contributes its Gaussian curvature $1/a^2$.

## Problems

### `tower-drop` · entry · difficulty 1 · estimate

Two steel balls hang side by side, 3 metres apart, in a tall tube with the air pumped out. A single catch lets both go at once, and they fall 50 metres. The centre of Earth is 6,371 kilometres away. Does the gap grow or shrink, and by how much?

**Hints**

1. Where does each ball's path lead?
2. Over the fall, what fraction of the way to the centre do the balls travel?

**Answer:** It shrinks, by about 24 thousandths of a millimetre.

**Must contain:** Both balls fall toward Earth's centre, so their paths meet there; The gap shrinks by the same fraction as the distance to the centre: 50 parts in 6,371,000; About 24 thousandths of a millimetre

**Numeric:** shrinking of the gap = 2.35e-05 m (magnitude, ±5%)

**Solution**

1. Each ball falls toward the centre of Earth, so the two paths close in like spokes of a wheel that meet at the centre.
2. Between two spokes, the gap is in proportion to the distance from the centre. A 50-metre fall shrinks that distance by 50 parts in 6,371,000, so the gap shrinks by the same fraction.
3. So the gap shrinks by 3 metres times 50, divided by 6,371,000, which is 0.0000235 metres, about 24 thousandths of a millimetre.

**Targets:** `free-fall-removes-all-gravity`

### `hyperbolic-plane` · working · difficulty 2 · calculation

The metric $ds^2 = dr^2 + \sinh^2 r\,d\phi^2$ has nonzero Christoffel symbols $\Gamma^r{}_{\phi\phi} = -\sinh r\cosh r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = \coth r$. Compute $R^r{}_{\phi r\phi}$ and the orthonormal component. Does a small loop return a vector rotated toward the walker's left or right?

**Hints**

1. The derivative term is $\partial_r\Gamma^r{}_{\phi\phi}$.
2. Only one product term survives.
3. Divide by $g_{\phi\phi}$ for the orthonormal component.

**Answer:** $R^r{}_{\phi r\phi} = -\sinh^2 r$; the orthonormal component is $-1$. Small loops rotate vectors toward the walker's right, as on a saddle.

**Must contain:** Derivative term minus cosh squared minus sinh squared; Product term plus cosh squared; Orthonormal component minus one, negative curvature, rotation to the right

**Numeric:** orthonormal component = -1 1 (signed, ±0.01)

**Solution**

1. $\partial_r\Gamma^r{}_{\phi\phi} = -(\cosh^2 r + \sinh^2 r)$; $\partial_\phi\Gamma^r{}_{r\phi} = 0$.
2. $\Gamma^r{}_{r\lambda} = 0$, and $-\Gamma^r{}_{\phi\lambda}\Gamma^\lambda{}_{r\phi} = -\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = +\cosh^2 r$.
3. Sum: $R^r{}_{\phi r\phi} = -\sinh^2 r$, so $R_{r\phi r\phi} = -\sinh^2 r$ and $R_{r\phi r\phi}/(g_{rr}g_{\phi\phi}) = -1$.
4. The Gaussian curvature is $-1$, so by the small-loop law a loop enclosing area $\delta A$ on the walker's left rotates vectors by $-\delta A$: toward the right.

### `astronaut-stretch` · working · difficulty 2 · estimate

An astronaut 1.8 m tall falls feet first. Find $R^r{}_{0r0}$ and the difference between the accelerations of head and feet (a) just above Earth's surface, $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$, $r = 6371$ km; (b) at $r = 1000$ km from a black hole of 10 solar masses, $GM = 1.327\times10^{21}\ \mathrm{m^3\,s^{-2}}$.

**Hints**

1. Use $R^r{}_{0r0} = \partial_r^2\Phi/c^2$ with $\Phi = -GM/r$.
2. The stretching acceleration is $2GM/r^3$ times the height.

**Answer:** (a) $R^r{}_{0r0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$, difference $5.5\times10^{-6}\ \mathrm{m/s^2}$. (b) $R^r{}_{0r0} = -2.95\times10^{-14}\ \mathrm{m^{-2}}$, difference $4.8\times10^{3}\ \mathrm{m/s^2}$, about 490 times Earth's surface gravity.

**Must contain:** Radial second derivative of the potential is minus two GM over r cubed; Negative component means stretching; Earth: about five millionths of a metre per second squared; black hole: about 4800

**Numeric:** head-feet acceleration difference near Earth = 5.55e-06 m/s^2 (magnitude, ±3%); head-feet acceleration difference near the black hole = 4778 m/s^2 (magnitude, ±3%)

**Solution**

1. $\partial_r^2(-GM/r) = -2GM/r^3$, so $R^r{}_{0r0} = -2GM/(r^3c^2)$ and $\ddot\xi^r = +2GM\xi^r/r^3$: stretching.
2. (a) $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$; dividing by $c^2$ gives $3.43\times10^{-23}\ \mathrm{m^{-2}}$; times 1.8 m gives $5.55\times10^{-6}\ \mathrm{m/s^2}$.
3. (b) $2GM/r^3 = 2654\ \mathrm{s^{-2}}$; dividing by $c^2$ gives $2.95\times10^{-14}\ \mathrm{m^{-2}}$; times 1.8 m gives $4.78\times10^{3}\ \mathrm{m/s^2}$.
4. At 1000 km the black hole's Schwarzschild radius, 29.5 km, is small compared with $r$; for radial fall the exact Schwarzschild tidal component has the same form, $-2GM/(r^3c^2)$.

### `prove-function-linearity` · formal · difficulty 2 · proof

Show that $\mathcal{R}(fX,Y)Z = f\,\mathcal{R}(X,Y)Z$ and $\mathcal{R}(X,Y)(fZ) = f\,\mathcal{R}(X,Y)Z$ for every smooth $f$. Show that $\nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z$ alone fails the first property, and explain why function-linearity makes $\mathcal{R}$ a tensor.

**Hints**

1. Use $[fX,Y] = f[X,Y] - (Yf)X$.
2. Expand $\nabla_X(fW) = (Xf)W + f\nabla_X W$ twice for the third slot.

**Answer:** The derivatives of $f$ cancel between the three terms, but only with the bracket term; a map linear over functions depends only on the values of its arguments at each point, so it is a tensor.

**Must contain:** The bracket term cancels the (Yf) nabla X Z term; In the third slot the second derivatives of f cancel through XYf minus YXf minus [X,Y]f; Function-linearity means the output at a point depends only on values at that point

**Solution**

1. $\nabla_{fX}\nabla_Y Z = f\nabla_X\nabla_Y Z$ and $\nabla_Y\nabla_{fX}Z = (Yf)\nabla_X Z + f\nabla_Y\nabla_X Z$.
2. $\nabla_{[fX,Y]}Z = f\nabla_{[X,Y]}Z - (Yf)\nabla_X Z$. Subtracting, the $(Yf)\nabla_X Z$ terms cancel, giving $f\,\mathcal{R}(X,Y)Z$; without the bracket term, $-(Yf)\nabla_X Z$ is left.
3. $\nabla_X\nabla_Y(fZ) = (XYf)Z + (Yf)\nabla_X Z + (Xf)\nabla_Y Z + f\nabla_X\nabla_Y Z$; subtract the same with $X \leftrightarrow Y$ and $\nabla_{[X,Y]}(fZ) = ([X,Y]f)Z + f\nabla_{[X,Y]}Z$.
4. First derivatives of $f$ cancel in pairs, and $(XYf - YXf - [X,Y]f)Z = 0$, leaving $f\,\mathcal{R}(X,Y)Z$.
5. If a map is linear over functions, writing each argument in a local basis shows its value at $p$ depends only on the components at $p$, so it defines a $(1,3)$ tensor at each point.

## Observations

- **The vertical gradient of Earth's gravity, measured with falling atoms** (measured, working). An atom-interferometer gradiometer compares the free-fall accelerations of two clouds of laser-cooled atoms at different heights. Their relative acceleration per unit separation is $-c^2R^z{}_{0z0}$ for the local vertical, the radial tidal entry of the Riemann tensor near Earth; Earth's rotation and shape change it slightly. *Numbers:* Spherical Earth: $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$, so $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$. The standard free-air gradient is $3.086\times10^{-6}\ \mathrm{s^{-2}}$. *Reference:* M. J. Snadden, J. M. McGuirk, P. Bouyer, K. G. Haritos, M. A. Kasevich (1998), *Measurement of the Earth's Gravity Gradient with an Atom Interferometer-Based Gravity Gradiometer*, Physical Review Letters 81, 971–974, doi:10.1103/PhysRevLett.81.971
- **The arms of the LIGO detectors responding to the gravitational wave GW150914** (measured, working). A passing gravitational wave is oscillating curvature. The freely suspended mirrors at the ends of each arm obey $\ddot\xi^i = -c^2R^i{}_{0j0}\xi^j$, with $R^i{}_{0j0} = -\ddot h_{ij}/2c^2$ for the wave's strain $h_{ij}$ in its transverse-traceless description. *Numbers:* Peak strain $1.0\times10^{-21}$ over 4 km arms changed the arm length by about $\tfrac12 hL = 2\times10^{-18}$ m. At 150 Hz, within the observed sweep from 35 to 250 Hz, the curvature component is about $5\times10^{-33}\ \mathrm{m^{-2}}$, some $7\times10^{9}$ times smaller than Earth's static tidal entry but oscillating where the detectors are quiet. *Reference:* B. P. Abbott and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Ask whether one number is enough** (entry). Recall the ball, then walk the two loops of the multi-storey ball world after a prediction. *Why:* The tilt dependence is what makes a table necessary. *Predict:* At the same spot, will a loop on the floor and a loop that rides the lift turn the arrow by the same amount? *Visual:* [[tilt-a-tiny-loop-at-one-point]] *Uses:* `ways_in/a-table-of-turns`, `checks/two-tilts-in-the-building`
2. **Drop two pairs of balls** (entry). Predict the side-by-side drift and the drift of balls lined up toward Earth's centre, then compare with walkers on a ball and a crisp. *Why:* It shows the table as something measured, and that free fall does not remove it. *Predict:* Two balls dropped side by side in a tube with no air: does the gap stay the same? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/falling-side-by-side`, `checks/side-by-side-drop`
3. **Give each index a job** (working). Read the small-loop law slot by slot, then write the component formula and its matrix form. *Why:* Slots make the antisymmetry and the tensor property visible before the algebra. *Predict:* If you swap the two edges of the tiny loop, what happens to the change? *Visual:* [[shrink-the-loop-to-find-riemann]] *Uses:* `ways_in/slots-of-the-table`, `checks/swap-the-edges`
4. **Run the flat control** (working). Compute the polar plane, then the multi-storey ball world. *Why:* Watching derivative and product terms cancel defeats the belief that Christoffel symbols signal curvature. *Predict:* Polar coordinates have nonzero Christoffel symbols. Will the plane's Riemann tensor be zero? *Visual:* [[four-terms-that-cancel]] *Uses:* `checks/polar-plane-zero`, `worked_examples/multi-storey-ball-world`
5. **Measure it with tides** (working). Derive the weak-field components and connect them to gradiometers and gravitational-wave detectors. *Why:* It turns the tensor into instrument readings with units. *Uses:* `ways_in/tides-measure-it`, `checks/vacuum-tides`, `observations/gw150914-arm-response`
6. **Define it without coordinates and count it** (formal). Present the curvature operator, its symmetries and the coordinate-freedom count. *Why:* Graduate work needs a frame-independent definition and the meaning of the twenty components. *Uses:* `ways_in/curvature-operator`, `ways_in/twenty-numbers-coordinates-cannot-remove`, `checks/count-and-meaning`

## Analogies

### Stress across a cut in a loaded beam · working

Imagine slicing a loaded steel beam with a thin cut. The force per area across the cut depends on the cut's tilt: $t_i = \sigma_{ij}n_j$ for a cut with unit normal $n$. The stress tensor is a table that turns an oriented patch into a response, linear in the patch, as the Riemann tensor turns an oriented small loop into a change of a vector.

| In the analogy | Stands for |
| --- | --- |
| the tilt and area of the cut | the plane and area of the small loop |
| reversing the normal flips the traction | reversing the loop flips $\Delta V$ |
| the stress tensor $\sigma_{ij}$ | the Riemann tensor $R^\rho{}_{\sigma\mu\nu}$ |

*Limits:* Stress describes a cut by its normal, and a loop's plane has a single normal only in three dimensions; stress also has no slot for a carried vector. Riemann takes an ordered pair of edges in any dimension plus the vector being carried, and returns a change of that vector rather than a force.

### The field strength of a gauge field · formal

With the course gauge derivative $D_\mu = \partial_\mu - i(q/\hbar)A_\mu$, $[D_\mu,D_\nu]\psi = -i(q/\hbar)F_{\mu\nu}\psi$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. On vector components $\nabla_\mu = \partial_\mu + \Gamma_\mu$ with $(\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}$, and the commutator is $\partial_\mu\Gamma_\nu - \partial_\nu\Gamma_\mu + [\Gamma_\mu,\Gamma_\nu]$, the Riemann tensor as a matrix. A non-abelian gauge field has the same commutator term.

| In the analogy | Stands for |
| --- | --- |
| $-i(q/\hbar)A_\mu$ | the connection matrix $\Gamma_\mu$ |
| $-i(q/\hbar)F_{\mu\nu}$ | $R^\rho{}_{\sigma\mu\nu}$ as a matrix in $\rho\sigma$ |

*Limits:* Gauge phases act on an internal space, so the field strength has no pair-exchange or cyclic symmetry. For gravity the transformed space is the tangent space itself, which ties the matrix indices to the loop-plane indices and gives the Riemann tensor its extra symmetries.

## Misconceptions

### “Curvature at a spot is just one number saying how curved it is.” · entry · `curvature-is-one-number`

- **Why it is tempting:** On a ball, one number really is enough.
- **What is true:** One number works on a surface because every tiny loop there lies in the same surface. With more directions, loops at different tilts can turn an arrow by different amounts.
- **Exposed by:** `checks/two-tilts-in-the-building`

### “When you fall freely, gravity is completely gone.” · entry · `free-fall-removes-all-gravity`

- **Why it is tempting:** People in a freely falling lift float as if they had no weight.
- **What is true:** Falling removes the feeling of weight, but not the difference in gravity's pull between nearby places. Neighbouring falling objects still drift together or apart.
- **Exposed by:** `checks/side-by-side-drop`

### “Nonzero Christoffel symbols mean the space is curved.” · working · `christoffels-mean-curvature`

- **Why it is tempting:** They are the first gravity-like objects in the geodesic equation.
- **What is true:** Christoffel symbols also describe coordinate lines that bend or spread on a flat plane. Only the Riemann tensor decides, and in polar coordinates it vanishes.
- **Exposed by:** `checks/polar-plane-zero`

### “Where there is no matter, spacetime is flat.” · working · `empty-space-is-flat`

- **Why it is tempting:** Matter sources curvature, and the vacuum field equation sets a curvature tensor to zero.
- **What is true:** Vacuum sets only a contraction to zero. Outside Earth the tidal entries are nonzero and merely sum to zero.
- **Exposed by:** `checks/vacuum-tides`

### “The Riemann tensor is just the second derivatives of the metric.” · working · `riemann-is-just-second-derivatives`

- **Why it is tempting:** In coordinates adapted to a point that is exactly its form.
- **What is true:** In general coordinates the products of Christoffel symbols matter. Only where every Christoffel symbol vanishes does the tensor reduce to second derivatives.
- **Exposed by:** `checks/second-derivatives-claim`

### “The 20 Riemann components are 20 independent gravitational fields or wave polarizations.” · formal · `twenty-components-are-twenty-freedoms`

- **Why it is tempting:** Independent components sound like independent physical freedoms.
- **What is true:** They are values at one event. Matter fixes the 10 Ricci components through Einstein's equations, and vacuum radiation has two polarizations.
- **Exposed by:** `checks/count-and-meaning`

### “A Riemann component or Ricci scalar means the same thing in every text.” · formal · `one-universal-sign`

- **Why it is tempting:** Each text presents its own convention as the only one.
- **What is true:** Texts differ in overall sign, index order and signature, and lowered components flip with the signature. Calibrate with the sphere before borrowing a sign.
- **Exposed by:** `checks/sign-under-metric-flip`

## Checks

1. **Entry · predict** `checks/two-tilts-in-the-building`. Picture a made-up building whose floors are not flat slabs: each floor is the whole surface of the same huge ball, copied exactly, with the floors close together. A lift joins each spot to the matching spot on the next floor. At one spot, a fresh cardboard arrow is pressed against the floor. You carry it, never letting it swing, around two tiny loops. Loop A runs along the floor. Loop B rides the lift up one floor, walks a short way ahead without steering, rides the lift down, and walks the same distance back to the start. Which loop brings the arrow back turned?
   - **Hints:** What kind of surface is each floor? / What does the walk back do to whatever the walk out did?
   - **Answer:** Loop A. The floor is a ball's surface, so a tiny loop along it brings the arrow back turned. On loop B, every floor is an exact copy, so after each lift ride the arrow points toward the copy of whatever it pointed toward before. The walk ahead and the walk back are the same stretch on identical floors, in opposite directions, so the walk back undoes the walk ahead. So loop B brings the arrow back matching its start. Two tilts at one spot give two answers, so one number cannot describe the curving there.
   - **Must contain:** Loop A turns the arrow; Loop B brings it back matching its start; One spot needs different answers for different tilts
   - **Targets:** `curvature-is-one-number`
   - **Visual:** [[tilt-a-tiny-loop-at-one-point]]
2. **Entry · numeric** `checks/count-the-tilts`. The tilt of a tiny loop is set by choosing two directions for its sides. Space has three directions: ahead, sideways and up. How many different pairs can you choose, counting ahead with up and up with ahead as the same pair? How many if time is added as a fourth direction?
   - **Hints:** List the pairs that include ahead first.
   - **Answer:** Three, then six. With three directions the pairs are ahead with sideways, ahead with up, and sideways with up. Adding time gives three more pairs: time with each of the three space directions. So there are six.
   - **Must contain:** Three pairs in space; Six pairs in space and time
   - **Numeric:** pairs in space = 3 1 (magnitude, ±0.1); pairs in space and time = 6 1 (magnitude, ±0.1)
3. **Entry · evaluate-claim** `checks/side-by-side-drop`. You ride a lift that falls freely down a very deep shaft with the air pumped out of it. You float, and so do two crumbs you let go of, side by side. A friend says: in free fall gravity has gone completely, so the crumbs will stay exactly the same distance apart. Is your friend right?
   - **Hints:** Where does each crumb's path lead?
   - **Answer:** No. Each crumb falls toward the centre of Earth, so their paths are not parallel: like spokes of a wheel, they lead to the same point, the centre. So the crumbs drift slowly toward each other. You float because you, the lift and the crumbs all fall together. Falling cannot remove the slight difference in the direction of the pull at two places. That leftover drift is the part of gravity the Riemann curvature tensor describes.
   - **Must contain:** The crumbs drift toward each other; Their paths lead to Earth's centre and meet there; Falling removes the feeling of weight, not the drift
   - **Targets:** `free-fall-removes-all-gravity`
   - **Visual:** [[falling-ring-of-crumbs]]
4. **Working · numeric** `checks/polar-plane-zero`. Polar coordinates on the flat plane, $ds^2 = dr^2 + r^2d\phi^2$, have $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$. A classmate concludes that the plane is curved. Compute $R^r{}_{\phi r\phi}$ and evaluate the conclusion.
   - **Hints:** Only one product term survives.
   - **Answer:** $R^r{}_{\phi r\phi} = \partial_r\Gamma^r{}_{\phi\phi} - \partial_\phi\Gamma^r{}_{r\phi} + \Gamma^r{}_{r\lambda}\Gamma^\lambda{}_{\phi\phi} - \Gamma^r{}_{\phi\lambda}\Gamma^\lambda{}_{r\phi}$. The first term is $-1$, the second $0$, the third $0$ because $\Gamma^r{}_{rr} = \Gamma^r{}_{r\phi} = 0$, and the fourth $-(-r)(1/r) = +1$. So the component is $0$, and the classmate is wrong: the symbols come from the coordinate lines, and a tensor that vanishes in one coordinate system vanishes in all.
   - **Must contain:** Derivative term minus one; Product term plus one; Riemann is zero, so the plane is flat; Christoffel symbols do not decide
   - **Numeric:** R upper r lower phi r phi = 0 1 (signed, ±1e-06)
   - **Targets:** `christoffels-mean-curvature`
   - **Visual:** [[four-terms-that-cancel]]
5. **Working · predict** `checks/swap-the-edges`. A tiny parallelogram has edges $a^\mu$ and $b^\nu$, and $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$. Predict the change when (i) the edges are swapped, (ii) $b = 2a$, (iii) the edge $a$ is doubled.
   - **Hints:** What is the area of a parallelogram with parallel edges?
   - **Answer:** (i) It flips sign: swapping the edges walks the loop the other way, and $R^\rho{}_{\sigma\mu\nu} = -R^\rho{}_{\sigma\nu\mu}$. (ii) It is zero: $a^\mu a^\nu$ is symmetric while the tensor is antisymmetric in $\mu\nu$, and the parallelogram has no area. (iii) It doubles, by linearity in each edge.
   - **Must contain:** Swapping flips the sign; Parallel edges give zero; Doubling an edge doubles the change
   - **Visual:** [[shrink-the-loop-to-find-riemann]]
6. **Working · evaluate-claim** `checks/second-derivatives-claim`. Evaluate the claim: "The Riemann tensor is just the second derivatives of the metric." Use the sphere component $R^\theta{}_{\phi\theta\phi}$ as evidence.
   - **Hints:** What does each product term contain in terms of $g$?
   - **Answer:** Only partly true. The derivative terms $\partial\Gamma$ contain second derivatives of $g$, but the product terms contain squares of first derivatives. On the sphere, $\partial_\theta\Gamma^\theta{}_{\phi\phi} = \sin^2\theta - \cos^2\theta$, and the product term supplies $+\cos^2\theta$ to make $\sin^2\theta$. Only at a point in coordinates where every Christoffel symbol vanishes do the products drop out.
   - **Must contain:** Product terms carry squares of first metric derivatives; On the sphere the product term contributes cos squared theta; Pure second derivatives only where the Christoffel symbols vanish
   - **Targets:** `riemann-is-just-second-derivatives`
7. **Working · numeric** `checks/vacuum-tides`. Outside Earth there is no matter and $\nabla^2\Phi = 0$. Does that make $R^i{}_{0j0}$ zero there? Give $R^z{}_{0z0}$ for the local vertical and $R^x{}_{0x0}$ for a horizontal direction at Earth's surface, $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$, $r = 6371$ km.
   - **Hints:** Take the second derivatives of $-GM/r$ along and across the radial direction.
   - **Answer:** No. With $\Phi = -GM/r$, $R^z{}_{0z0} = -2GM/(r^3c^2) = -3.43\times10^{-23}\ \mathrm{m^{-2}}$ and $R^x{}_{0x0} = +GM/(r^3c^2) = +1.71\times10^{-23}\ \mathrm{m^{-2}}$. The three diagonal entries sum to zero, which is all that $\nabla^2\Phi = 0$ requires. The entries themselves are nonzero, so vertical pairs separate and horizontal pairs approach: spacetime there is curved.
   - **Must contain:** Vertical component minus 3.43 times ten to the minus 23 per metre squared; Horizontal components plus half that size; Only the sum vanishes in vacuum
   - **Numeric:** R upper z lower 0 z 0 = -3.43e-23 m^-2 (signed, ±3%); R upper x lower 0 x 0 = 1.71e-23 m^-2 (signed, ±3%)
   - **Targets:** `empty-space-is-flat`
8. **Formal · explain** `checks/count-and-meaning`. How many independent components does the Riemann tensor of a metric have at a point in $n = 2$, $3$ and $4$ dimensions? A student says the 20 in four dimensions are 20 independent gravitational waves that empty space can carry. Evaluate.
   - **Hints:** Which part of the curvature do Einstein's equations fix locally?
   - **Answer:** $n^2(n^2-1)/12$ gives 1, 6 and 20. The student is wrong. The components are values of curvature at one event, left over after coordinates fix the metric and its first derivatives. Einstein's equations tie the 10 Ricci components to the local stress-energy, and only the 10 Weyl components are free there. Radiation, a question about evolution in time, carries just two polarizations.
   - **Must contain:** 1, 6 and 20; Components are pointwise data, not propagating freedoms; Ricci part fixed by matter; waves have two polarizations
   - **Numeric:** independent components in four dimensions = 20 1 (magnitude, ±0.1)
   - **Targets:** `twenty-components-are-twenty-freedoms`
   - **Visual:** [[twenty-of-256-slots]]
9. **Formal · evaluate-claim** `checks/flatness-hypotheses`. Evaluate the claim: "If the Levi-Civita curvature vanishes everywhere on a connected manifold, the manifold is Euclidean or Minkowski space, and transport around every loop returns every vector unchanged."
   - **Hints:** Try a paper cone with its tip cut off.
   - **Answer:** The local part is true: vanishing curvature gives coordinates with constant metric near every point, and loops that can be shrunk within the manifold return vectors unchanged. The global part fails. A flat cone with its tip removed has zero curvature, yet a loop around the missing tip rotates vectors by the wedge angle. A flat torus returns every vector unchanged but is compact, so it is not Euclidean space. Globally Euclidean or Minkowskian structure needs further hypotheses, such as simple connectedness and completeness.
   - **Must contain:** Locally flat coordinates exist; Loops that cannot be shrunk can rotate vectors, as around a removed cone tip; Global conclusions need topology and completeness hypotheses
10. **Formal · derive** `checks/sign-under-metric-flip`. Show that $\Gamma^\lambda{}_{\mu\nu}$ and $R^\rho{}_{\sigma\mu\nu}$ are unchanged under $g \to -g$, while $R_{\rho\sigma\mu\nu}$ and the Ricci scalar $g^{\mu\nu}R^\rho{}_{\mu\rho\nu}$ change sign. What must you check before using a Ricci scalar from a text with signature $(+,-,-,-)$?
   - **Hints:** How many factors of the metric or its inverse does each object contain?
   - **Answer:** $\Gamma$ is $\tfrac12 g^{-1}\partial g$, and both factors flip, so $\Gamma$ is unchanged; $R^\rho{}_{\sigma\mu\nu}$ is built from $\Gamma$ alone, so it is unchanged. Lowering with $g$ flips $R_{\rho\sigma\mu\nu}$, and raising with $g^{\mu\nu}$ flips the Ricci scalar. So the same sphere has Ricci scalar $+2/a^2$ in the course and $-2/a^2$ in a text using the same Riemann and Ricci definitions with the opposite signature. Check the signature, the overall sign of the Riemann tensor, and which indices are contracted, and calibrate with the sphere.
   - **Must contain:** Christoffel symbols and the one-up Riemann tensor do not change; Lowered components and the Ricci scalar change sign; Calibrate conventions with the sphere
   - **Targets:** `one-universal-sign`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Overall sign and index order of the Riemann tensor | $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, loop plane in the last two slots, $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$, and a sphere has Ricci scalar $+2/a^2$. | Some texts reverse the overall sign, put the loop-plane indices first, or write the commutator with antisymmetrizing brackets that carry a factor one half. Compare definitions and calibrate with the sphere before borrowing a sign. |
| Which lower index of a Christoffel symbol is the derivative index | Derivative index first: $\nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\lambda}V^\lambda$. | Some texts put the derivative index last, so their component formula looks reordered. For the torsion-free Levi-Civita connection the two agree. |
| Lowered components under the opposite signature | Signature $(-,+,+,+)$. | With $(+,-,-,-)$, $R^\rho{}_{\sigma\mu\nu}$ is unchanged, but $R_{\rho\sigma\mu\nu}$ and the Ricci scalar flip sign for the same geometry. |

## Visuals

- ★ [[tilt-a-tiny-loop-at-one-point]] (flagship): Shows that at one point the returned change depends on the loop's tilt and the arrow's direction, filling a table. *Sketch:* A point in the multi-storey ball world: a stack of identical sphere surfaces, with a lift at every point joining it to the matching point on the next floor. The learner turns a handle to tilt a tiny square loop and picks the arrow's starting direction; the arrow is carried around and the change appears in a growing table. Tilts containing the lift direction give zero for every arrow; the tilt along the floor turns floor arrows by an amount proportional to area and leaves an arrow along the lift shaft unchanged. It proves that one number cannot describe curvature with three directions.
- [[falling-ring-of-crumbs]] (core): Tidal drift of freely falling particles as a reading of the tensor. *Sketch:* A ring or ball of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it. Sliders for mass and distance, presets for Earth, a neutron star and a black hole; readouts of the entries $(-2, 1, 1)GM/r^3c^2$ and their zero sum. It proves that free fall leaves tides.
- [[shrink-the-loop-to-find-riemann]] (core): Connects the small-loop law to the index slots. *Sketch:* A coordinate parallelogram on a sphere patch, a saddle, or a polar-coordinate plane. The learner shrinks it and swaps the edge order; a log-log plot shows the change against area with slope one, converging to the small-loop law, while the polar-coordinate plane stays at zero.
- [[four-terms-that-cancel]] (supporting): Shows derivative and product terms cancelling for flat metrics. *Sketch:* Pick a metric (polar plane, sphere, hyperbolic plane, accelerating-rocket coordinates) and a point. Each Riemann component expands into its four terms with numerical values; nonzero Christoffel symbols light up while flat metrics sum to zero.
- [[twenty-of-256-slots]] (supporting): Counts independent components. *Sketch:* A grid of all index combinations. Applying pair antisymmetry, pair exchange and the cyclic identity in turn greys out dependent slots and links partners with signs, ending at 1, 6 or 20 for dimension 2, 3 or 4.

## Tutor moves

**Open with**

- Picture two steel balls dropped side by side, one metre apart, in a tall tube with no air. As they fall toward Earth, will the gap between them stay the same, shrink, or grow? *(prediction)*
- On a ball, one number tells how curved it is at a spot. In a world with more directions to move in, would one number still be enough? *(reflection)*

**If the learner is stuck**

- *The learner cannot keep track of which index does what.* → Name the slots aloud: carried vector, two edges, output component. Then ask what swapping the edges must do. *Uses:* `ways_in/slots-of-the-table`, `checks/swap-the-edges`
- *The learner's polar-plane calculation does not come out zero.* → Check the last product term with $\lambda = \phi$: $-\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = +1$. *Uses:* `checks/polar-plane-zero`
- *The learner cannot picture loops at different tilts.* → Use the bottom, front and side of a cardboard box, then the multi-storey ball world. *Uses:* `ways_in/a-table-of-turns`, `worked_examples/multi-storey-ball-world`

**Common questions**

- *Is the Riemann tensor the same thing as gravity?* (entry) It is the part of gravity that falling freely cannot remove. Inside a falling lift you float, but two floating crumbs slowly drift together or apart, and the Riemann tensor sets that drift. The weight you feel standing on the ground is not in this table: it comes from the floor pushing you and stopping you from falling freely. *Uses:* `ways_in/falling-side-by-side`
- *Why is it called a tensor?* (entry) A tensor is a table of numbers describing something real, in a way that does not depend on how you label directions. Relabel the directions and the numbers change together by fixed rules, but a table of zeros stays all zeros. That is why a zero Riemann tensor means no tiny loop turns an arrow, whatever labels you use. *Uses:* `ways_in/coordinates-cannot-fake-it`
- *Why do different texts get different signs?* (working) They choose a different overall sign, a different index for the loop plane, or a different signature. Calibrate with the sphere: in the course convention $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and the Ricci scalar is $+2/a^2$. *Uses:* `notation_traps/riemann-sign-and-slots`, `checks/sign-under-metric-flip`

**Switching levels**

- To working when: asks how to calculate it; uses coordinates or Christoffel symbols. Go to the slots, the component formula and the polar-plane control. *Uses:* `ways_in/slots-of-the-table`, `checks/polar-plane-zero`
- To formal when: asks why it is a tensor; wants a definition without coordinates. Present the curvature operator and the function-linearity proof. *Uses:* `ways_in/curvature-operator`, `problems/prove-function-linearity`
- To research when: asks whether curvature determines the geometry; asks about theories beyond Einstein's. Open the research horizon. *Uses:* `research_horizon/equivalence-problem`, `research_horizon/higher-curvature-gravity`

**Pronunciations:** Riemann → REE-mahn; Christoffel → kris-TOFF-el; Ricci → REE-chee; Levi-Civita → LEH-vee CHEE-vee-tah; Weyl → VILE

**Voice notes:** Say Riemann tensor, Ricci tensor and Ricci scalar in full, never a bare R. Read index positions aloud only while the learner is computing components.

## History

- **Bernhard Riemann (1854).** In his 1854 habilitation lecture, published in 1868, founded the geometry of spaces of any dimension built on a metric, with curvature measured on two-dimensional sections through each point. Bernhard Riemann (1868), *Ueber die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150
- **Elwin Bruno Christoffel (1869).** Introduced the symbols now named after him and published the four-index curvature quantity while deciding when two quadratic differential forms are related by a change of variables; Riemann's 1861 prize essay, printed only in 1876, had reached similar expressions. Elwin Bruno Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46–70, doi:10.1515/crll.1869.70.46
- **Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900).** Systematized the absolute differential calculus, now called tensor calculus, the language in which general relativity was later formulated. Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900), *Méthodes de calcul différentiel absolu et leurs applications*, Mathematische Annalen 54, 125–201, doi:10.1007/BF01454201

## Research horizon

- **When curvature decides the geometry.** The Riemann tensor at one point does not determine a geometry. The Cartan–Karlhede method compares the tensor and its covariant derivatives, up to a finite order, in frames fixed by the curvature itself, to decide whether two metrics differ only by coordinates. Scalar invariants are weaker: some curved spacetimes, including plane gravitational waves, have every polynomial curvature invariant equal to zero. Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861; Vojtěch Pravda, Alena Pravdová, Alan Coley, Robert Milson (2002), *All spacetimes with vanishing curvature invariants*, Classical and Quantum Gravity 19, 6213, doi:10.1088/0264-9381/19/23/318
- **Gravity beyond linear curvature.** In four dimensions, the only symmetric, divergence-free two-index tensors built from the metric and its first two derivatives are combinations of the Einstein tensor and the metric. In higher dimensions, and in effective field theories of gravity, invariants quadratic and higher in the Riemann tensor, such as the Gauss–Bonnet combination, enter the action. David Lovelock (1971), *The Einstein tensor and its generalizations*, Journal of Mathematical Physics 12, 498–501, doi:10.1063/1.1665613

## Review: novice

**Verdict:** fixed (2026-09-13, revision 2)

**Retell attempt:** If you carry an arrow around a tiny loop on a ball without letting it swing, it comes back turned, and bigger loops turn it more, so one number tells how curved the ball is. Our space has three directions, so a loop can be tilted like the bottom or sides of a box. Then there is a building where every floor is a ball, which I could not really picture, and a loop on the floor turns the arrow but a loop that uses the lift does not, so you need a table, the Riemann tensor. I don't get how time is a direction, or how you walk a loop in time. Earth's ground turns an arrow a millionth of a degree or so per square kilometre, which I think is why we don't notice gravity? Separately, two balls dropped side by side get closer, and balls one above the other get further apart, twice as much, but I'm not sure why twice. Floating in a falling lift doesn't stop crumbs drifting. Somehow falling is a walk through spacetime and that drift is the curving, but I'd have to take that on trust.

**Stumbles (30)**

- “With three or more directions one number is not enough, so it is a table kept at every place.”: Directions of what is unstated, and the claim is too general: a space could be curved the same way at every tilt.
- “Carry a cardboard arrow around it, lying flat on the surface ... a fresh arrow lying flat on the floor ... brings a flat arrow back turned”: 'Flat' describes surfaces in this note (flat floor, flat slabs); here it describes how the arrow lies, one word in two senses.
- “A square with twice the area gives twice the turn.”: A surprising claim with no reason, and a square with twice the area is not two of the first squares.
- “the turn for each square centimetre the loop fences off ... for each unit of area fenced off ... a loop fencing off one square kilometre”: 'Fence off' names no region on a closed ball, and it is a second phrase for the loop's area.
- “a ball's surface offers only two directions to move in”: Which two directions? The reader cannot match them with the three named next.
- “you could hold a tiny square loop flat like a tabletop, upright facing you, or upright beside you”: A loop is a path, so it cannot be held, and 'flat' is again a position.
- “In a curved space, loops at different tilts can give different answers.”: The reader does not know what 'curved' means for a space with three directions; the arrow rule for three directions sat only in simplifies, so the test was not doable from the prose.
- “Picture a tall building in which every floor is a copy of the same huge ball's surface.”: Reread several times: a floor that is a ball does not fit in a building, and the reader tries to stack balls on top of each other.
- “Ride the lift one floor, walk a short stretch without steering, ride back, and walk the matching stretch back to the start.”: Up or down is not said, 'back' is used twice for different moves, and 'the matching stretch' is unclear.
- “Riding the lift changes nothing about the arrow, because every floor is an exact copy of the others.”: The reader cannot check 'changes nothing' across two different floors; there is no visible reference to compare with.
- “For each tilt of a tiny loop and each starting direction of the arrow, it lists how the arrow comes back changed”: Why the starting direction matters is never shown; on the ball every arrow turned alike.
- “For each tilt of a tiny loop ... it lists how the arrow comes back changed”: First what-if: walking the loop the other way round. The table seemed to need that too.
- “Space and time together have four directions, with time as the fourth, and four directions give six pairs.”: A surprising claim with no reason, and the reader asks how anyone walks a loop in time.
- “On Earth's surface, treated as a ball, a loop fencing off one square kilometre turns an arrow by about one and a half millionths of a degree. That is why nobody notices the curving in daily life.”: 'The curving' reads as the curving of space and time, but the number is the ground's shape; and the number has no everyday feel.
- “With three or more directions, the arrow rule means the arrow never swings in any direction. (simplifies)”: A simple, precise rule hidden in simplifies; the entry prose did not tell the reader how to carry the arrow in three directions.
- “Many entries are copies of others, so fewer numbers are independent.”: 'Independent' is undefined, and many entries are not copies but follow from others.
- “Over a 100-metre fall, the gap shrinks by 100 parts in 6,371,000 of its one metre.”: Step left implicit: why the gap shrinks by the same fraction as the fall.
- “Now hang one ball a metre nearer to Earth's centre than the other”: Reread: the reader works out that this means one ball under the other.
- “That is twice the sideways drift, because gravity weakens with the square of distance. Squaring doubles a tiny excess: 1.001 squared is about 1.002.”: Compressed chain: the reader cannot see what the doubled excess is compared with.
- “This pattern is called tidal stretching ... this tidal drift ... this drift”: Two names for one pattern, and 'stretching' names only the half that spreads apart.
- “Why is this curving?”: 'This' has several candidates: the drift, the pattern, falling.
- “On a saddle-shaped crisp, such walkers spread apart.”: 'Crisp' is regional, and the claim has no link to the ball case.
- “Falling freely is the no-steering walk through space and time taken together, a world with four directions called spacetime.”: A leap: why a falling ball walks through time is not said, and a new term arrives inside the claim.
- “Falling balls that draw together or spread apart are feeling spacetime's curving.”: Why the balls count as walkers that set off side by side is implicit, and which tilts of the table are meant is not said.
- “At one spot, a fresh cardboard arrow lies flat on the floor. ... Loop B rides the lift one floor, walks a short stretch without steering, rides back, and walks the matching stretch back.”: Check: the same 'flat' and 'back' ambiguities, and a floor that is a ball is not explained within the check.
- “How many different pairs can you choose?”: Ambiguous: a reader may count ahead-with-up and up-with-ahead separately and get six and twelve.
- “with the air pumped out of the shaft and the lift”: What-if: nobody can ride in a lift with no air.
- “The gap shrinks in step with the distance fallen: 50 metres is 50 parts in 6,371,000 of the way to the centre.”: Problem solution skips why the gap follows the distance.
- “The weight you feel standing on the ground is not curving; it is the floor pushing you away from falling freely.”: Confusing for a reader told that gravity is curving: 'is not curving' sounds like a denial of that.
- “this tidal drift is spacetime's curving, read from the Riemann tensor”: Takeaway: 'read from' suggests the drift is computed from a table the reader never sees.

**Fixes**

- Compared the retell with the takeaways. The table-of-turns takeaway came through, but the building, time as a direction and the Earth number were muddled. The falling-balls retell missed why drift counts as curving and why the stretching is twice the squeezing. Rewrote both entry explanations to close those gaps, and kept them within the core cap of 1,000 entry words.
- Table-of-turns way: moved the three-direction arrow rule from simplifies into the explanation, backed the doubling of the turn with the two-squares argument, and rebuilt the building as floors that are whole ball surfaces with a lift at every spot. Loop B is now a doable sequence (up, ahead, down, back), and the lift ride compares the arrow with the copy of a landmark.
- Added the lift-shaft arrow, which comes back matching its start from the floor loop, to show why the table needs starting directions. Added that the reversed loop gives the opposite change.
- Justified time as a fourth direction (meeting a friend needs a place and a time), said honestly that loops in time cannot be walked and that falling objects measure those entries, and separated the ground's curving (1.41 millionths of a degree per square kilometre, a hair's width at 3 kilometres) from the far weaker curving of space and time.
- Falling way: spokes proportion stated as the reason for the 16 thousandths of a millimetre, the 'why twice' chain spelled out with the one-part and two-part comparisons, one term 'tidal drift' throughout (glossary id renamed from tidal-stretching to tidal-drift; the note was never published), 'spacetime' introduced after the reader sees that a falling ball's path has places and times, and the balls starting at rest tied to walkers setting off side by side, with the two tilts named.
- Removed 'flat' for how the arrow lies and 'fence off' everywhere at entry; summary scoped to 'not always enough'; glossary definitions for swing, tilt and the Riemann tensor rewritten in short sentences.
- Entry checks and problem: the building check restates its world and loop B's route, count-the-tilts says unordered pairs, the lift in side-by-side-drop keeps its air, and the tower-drop solution states the spokes proportion.
- Entry common question is-it-gravity no longer says standing weight 'is not curving'.
- Ladder: all non-entry ways already name the way they continue in their first sentence. Added a bridge to 'Four slots and the component formula' saying that $a^\mu b^\nu$ carries the loop's area, so components are the entry picture's change per unit area and the index pair is its tilt. Index notation at working is allowed: index-notation is reached through the tensor prerequisite. The seven ways use five kinds and are distinct routes.
- Recomputed every new or changed entry number with python: 1 square km over Earth's radius squared is 1.41 millionths of a degree; a 0.08 mm hair subtends that at 3.2 km; spokes estimate 1.57e-5 m and 3.14e-5 m agree with the tidal-acceleration calculation over a 4.52 s fall; tower drop 2.35e-5 m; Earth's ground curvature over the spacetime tidal entries is 0.7 to 1.4 billion.
- Updated the flagship visual's sketch so the lift joins every point and the floor loop leaves a lift-shaft arrow unchanged. Bumped the revision to 2.

**Concerns**

- The physics reviewer should confirm three new entry claims: the two-squares additivity argument (leading order for tiny loops); that an arrow along the lift direction returns unchanged from a floor loop in the sphere-times-line world (the lift direction is a parallel field of the product metric); and the comparison 'roughly a billion times weaker', which sets the Gaussian curvature of Earth's ground, 2.46e-14 per square metre, against the tidal entries of 1.7e-23 to 3.4e-23 per square metre.
- The 'why twice' paragraph uses 1.001 squared for the inverse-square excess, which is 1/(1-x)^2 ≈ 1 + 2x; the physics reviewer should confirm that this simplification is acceptable.
- The entry explanations are close to the core cap of 1,000 words, so any further entry additions will need cuts elsewhere.
- The prerequisite notes parallel-transport and tidal-force do not exist yet, and path-dependence-of-parallel-transport is still in the old schema, so their entry glossaries could not be aligned with this note.
- The writer's reported open items are unchanged by this review: five proposed visuals, references unverified with DOIs to add, the transverse-traceless form of the gravitational-wave curvature, and the GW150914 and black-hole tidal numbers.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 2)

**Verification**

- Component formula, small-loop law and commutator agree with course conventions.: Compared each with the conventions rows; expanded R(∂μ,∂ν)∂σ from the operator definition; checked the matrix form (Γ_μΓ_ν)^ρ_σ = Γ^ρ_μλ Γ^λ_νσ. → Correct: operator components reproduce the course formula exactly, loop plane in the last two slots, sign of the small-loop law matches the conventions.
- Derivation ricci-identity-in-coordinates.: Re-expanded every step by hand, including the dropped −Γ^λ_μν ∇_λ V^ρ term (torsion-free) and the symmetric cancellations. → Correct, each step.
- Polar plane: R^r_φrφ = 0 with Γ^r_φφ = −r, Γ^φ_rφ = 1/r.: Hand computation of all four terms. → −1 + 0 + 0 + 1 = 0. Correct.
- Sphere and S²×R worked example: R^θ_φθφ = sin²θ, R^φ_θφθ = 1, z-components zero, orthonormal 1/a², ΔV^θ = −sin²θ V^φ δθ δφ.: Hand computation from the Christoffel symbols; small-loop law with a = δθ ∂θ, b = δφ ∂φ; lowered with g_θθ = a². → All correct; −∂θ cot θ − cot²θ = csc²θ − cot²θ = 1.
- Hyperbolic plane problem: R^r_φrφ = −sinh²r, orthonormal −1, rotation toward the walker's right.: Hand computation; sense from the conventions orientation row (positive = toward the walker's left). → Correct in value and sense.
- Weak static field: Γ^i_00 = ∂_iΦ/c², R^i_0j0 = ∂_i∂_jΦ/c², geodesic deviation gives ξ̈^i = −∂_i∂_jΦ ξ^j.: Hand derivation with x^0 = ct, g_00 = −(1+2Φ/c²); dropped quadratic Γ products as O(Φ²/c⁴). → Correct, including the sign: positive entry means approach.
- Earth tidal numbers: GM/r³ = 1.54e-6 s⁻², R^z_0z0 = −3.43e-23 m⁻², R^x_0x0 = +1.71e-23 m⁻², 100 m fall 4.51 s, side drift 1.57e-5 m.: python3 with GM = 3.986e14, r = 6.371e6 m, c = 299792458 m/s. → 1.5414e-6; −3.4301e-23; +1.7150e-23; 4.513 s; 1.5696e-5 m. Correct.
- Entry spokes estimate: 1 m gap shrinks by 16 thousandths of a mm over 100 m; vertical pair grows 31 thousandths; tower-drop 3 m over 50 m gives 24 thousandths.: python3. Radial fall from rest keeps both balls on radial lines, so gap ∝ r exactly for a spherical non-rotating Earth; compared with ½(GM/r³)d t². → 1.5696e-5 m (identical to the tidal formula, since ½ g t²/r = h/r); 3.139e-5 m; 2.354e-5 m. Correct.
- Novice claim: 1.001 squared illustrates the inverse-square excess (pull stronger by about two parts for one part nearer).: python3: exact (1/(1−x))² − 1 with x = 1/6,371,000 versus 2x. → 3.1392253e-7 versus 3.1392246e-7; the leading-order doubling is correct and the (1+x)² illustration gives the same first-order excess. Acceptable.
- Novice claim: two squares side by side give twice the turn.: On a surface the holonomy is a rotation in SO(2), which is abelian, and the shared edge is traversed once each way; the angle equals the integral of Gaussian curvature, which is additive over regions. → Correct on a surface (exactly, modulo a whole turn; tiny loops never reach that). Correct.
- Novice claim: in the stacked-ball world a floor loop returns an arrow along the lift direction unchanged, and loop B (up, ahead, down, back) returns every arrow unchanged.: Product metric a²(dθ²+sin²θ dφ²)+dz²: no Christoffel symbol carries a z index, so ∂_z is parallel; transport along z copies components, and the ahead and back legs are a transport T and the copy of its inverse. → Correct, and exact for any size of rectangle, not only to leading order. Added that floors are close together so loop B is also a tiny loop, matching the table's definition.
- Novice claim: spacetime curving near Earth is roughly a billion times weaker than the ground's curving.: python3: ground Gaussian curvature 1/R² = 2.464e-14 m⁻² against the tidal entries 1.715e-23 and 3.430e-23 m⁻²; all orthonormal Schwarzschild components at r are of order GM/r³c². → Ratios 1.44e9 and 0.72e9. "Roughly a billion" is correct.
- Entry Earth number: 1 km² loop turns an arrow by one and a half millionths of a degree; hair's width at 3 km.: python3: 1e6/R² rad in degrees; 0.08 mm hair over 3 km. → 1.412e-6 degrees, so "one and a half" was 6% high; changed to "about 1.4 millionths". Hair: 1.53e-6 degrees at 3 km (1.41e-6 at 3.2 km); acceptable for "about".
- Six pairs from four directions; tilt counts three and six.: python3 combinations. → C(4,2) = 6, C(3,2) = 3. Correct.
- Entry ball and saddle analogy with falling pairs: side-by-side pairs draw together "as on the ball", vertical pairs spread "as on the saddle".: Signs: ξ̈ = −c²R^i_0i0 ξ with R^x_0x0 > 0 (approach) and R^z_0z0 < 0 (separate); geodesics on K > 0 converge, on K < 0 diverge. → Behavioural mapping correct. Note: the Lorentzian sectional curvature of a timelike plane, R(ξ,u,ξ,u)/(g(ξ,ξ)g(u,u)), has the opposite sign because g(u,u) < 0; the entry prose compares behaviour only and states no sign, so it stays true.
- Astronaut problem: (a) 3.43e-23 m⁻², 5.55e-6 m/s²; (b) 2.95e-14 m⁻², 4.78e3 m/s² ≈ 490 g; Schwarzschild radius 29.5 km; exact radial Schwarzschild tidal component −2GM/r³c².: python3; the radial-radial frame component is invariant under radial boosts, so the static and radially infalling values agree. → 5.549e-6; 2654 s⁻²; 2.953e-14; 4777 m/s² = 487 g; 29.53 km. All correct, tolerances cover them.
- GW150914: R^i_0j0 = −ḧ_ij/2c² in TT gauge; ½hL = 2e-18 m; 5e-33 m⁻² at 150 Hz; 7e9 times below Earth's radial entry; sweep 35 to 250 Hz, peak strain 1.0e-21.: Linearized R_αβμν = ½(∂β∂μh_αν + ∂α∂νh_βμ − ∂α∂μh_βν − ∂β∂νh_αμ) with h_0μ = 0, ∂_0 = c⁻¹∂_t; python3; numbers checked against the PRL abstract. → R_i0j0 = −½∂_0²h_ij, so the formula and ξ̈ = ½ḧξ are correct; 2.0e-18 m; 4.94e-33 m⁻²; 6.9e9. Correct.
- Coordinate count: 10 − 16 leaves 6 Lorentz; 40 = 40; 100 − 80 = 20; general (n(n+1)/2)² − n·n(n+1)(n+2)/6 = n²(n²−1)/12.: Algebra and python3 for n = 1..4; kernel argument for B and C (symmetric in one pair and antisymmetric in an overlapping pair implies zero). → 0, 1, 6, 20 both ways. Correct.
- Formal statements: function-linearity proof, covector commutator sign, algebraic symmetries, 21 − 1 = 20 bivector count, 2D form K(g g − g g), second Bianchi identity, flatness criterion, sign behaviour under g → −g.: Hand checks: proof steps of prove-function-linearity; sphere check of the 2D form gives R_θφθφ = a² sin²θ; Γ ∝ g⁻¹∂g invariant, lowering and tracing flip. → All correct.
- Gauge analogy: [D_μ, D_ν]ψ = −i(q/ħ)F_μν ψ with D = ∂ − i(q/ħ)A.: Hand expansion in course gauge convention. → Correct sign and mapping.
- References: Snadden et al. PRL 81, 971 (1998); Abbott et al. PRL 116, 061102 (2016); Karlhede GRG 12, 693 (1980); Pravda et al. CQG 19, 6213 (2002); Lovelock JMP 12, 498 (1971); Riemann Abh. Göttingen 13, 133 (1868); Christoffel J. reine angew. Math. 70, 46 (1869); Ricci and Levi-Civita Math. Ann. 54, 125 (1900).: WebSearch against APS, Springer, IOP, AIP/ADS, De Gruyter, Deutsches Textarchiv and EUDML records. → All confirmed; DOIs added (and arXiv ids for GW150914 and Pravda et al.); Snadden page range 971–974 added. Riemann pages 133–150 per the Deutsches Textarchiv record (some catalogues give 133–152). Lovelock's abstract confirms the four-dimensional uniqueness statement.
- History scope: Christoffel "introduced" the four-index curvature quantity.: Checked against the historical record: Riemann's 1861 Paris prize essay contained equivalent expressions but was printed only in 1876. → Rescoped to "published", with the Riemann 1861 essay named.
- Structure: prerequisites acyclic, leads_to and related ids in the registry, assumes within prerequisites at or below each way's rung.: python3 transitive walk over the registry prerequisites. → No cycles; all ids exist; assumes consistent.

**Counterexamples tried**

- Uniform-density planet interior (a tunnel through the centre): vertical pairs draw together, breaking the unscoped glossary "spread apart along the line toward a planet's centre". Glossary scoped to objects outside a round planet; the falling takeaway scoped to "Near Earth" (for the real Earth vertical pairs still separate down to the core, since g grows with depth in the mantle; python: 4πGρ_crust − 2g/r = −8.4e-7 s⁻²).
- Deep shaft in side-by-side-drop: horizontal pairs converge at any depth because both pulls point to the centre. Check survives.
- Loop B of the building with widely separated floors: not a tiny loop, so it would not directly test the table. The transport result is exact for any size, but floors are now stated to be close together.
- Arrow along the lift direction on a floor loop: returns unchanged (parallel ∂_z). Confirms the starting-direction claim.
- Reversed loop: leading-order change flips sign by antisymmetry in μν. "Walking the other way round gives the opposite change" holds for tiny loops.
- Two squares on a ball: SO(2) holonomy is abelian on a surface, so turns add. Survives.
- Three-dimensional vacuum (2+1 gravity): Ricci = 0 forces Riemann = 0, which broke "sets a contraction to zero, never the whole tensor" read as a general claim. Rescoped to four dimensions.
- Flat cone minus tip, flat torus: break global readings of the flatness criterion; the note already scopes it as local and uses both. Survives.
- Rindler (uniformly accelerating) observers: nonzero Christoffel symbols and clock-rate differences with zero Riemann. Used correctly in coordinates-cannot-fake-it.
- Plane gravitational waves: curved with all polynomial invariants zero. Correctly stated in the research horizon.
- Different observer (boosted) for "one observer measures six components R^i_0j0": correct as frame-dependent; all components follow from deviation for all timelike u. Entry sentence changed from "the table's entries" to "entries" so it does not suggest falling objects can only reach time tilts or that one experiment reads the whole table.
- Strong field (10 solar-mass black hole at 1000 km): Newtonian tidal form equals the exact radial Schwarzschild value. Problem survives.
- Signature flip: R^ρ_σμν invariant, lowered components and Ricci scalar flip. Notation trap and check correct.

**Fixes**

- Entry table-of-turns: Earth ground number 1.41 millionths of a degree now "about 1.4 millionths" (was "one and a half"); floors of the building stated to be close together so loop B is a tiny loop; "measure the table's entries for tilts that include time" changed to "measure entries for tilts that include time". Entry explanations stay at 979 words.
- Entry check two-tilts-in-the-building: floors close together, matching the way.
- Falling-side-by-side takeaway scoped with "Near Earth"; glossary tidal-drift scoped to objects outside a round planet.
- Tides way: vacuum sentence scoped to four dimensions ("sets only a contraction ... in four dimensions the rest of the tensor can be nonzero").
- Formal curvature-operator takeaway rewritten without Unicode math, since takeaway is plain text.
- Stress analogy limits: a loop plane has a single normal only in three dimensions (stress itself exists in any dimension).
- Christoffel history rescoped: he published the four-index quantity; Riemann's 1861 essay, printed 1876, had similar expressions.
- All eight references verified; DOIs and arXiv ids added; verified set true.

**Concerns**

- The physics fixes change learner-visible entry text slightly (Earth number, floors close together, tidal-drift glossary, falling takeaway). Revision kept at 2 so both reviews cover the same text; an editor may bump the revision and ask for a quick novice re-read of those sentences.
- The prerequisite notes parallel-transport and tidal-force do not exist, and path-dependence-of-parallel-transport is in the old schema; entry vocabulary (arrow test, swing, tidal drift) should be aligned when they are written.
- Five visuals remain proposals with sketches only.
- The entry "falling side by side" relates converging falling pairs to the ball. In Lorentzian geometry the sectional curvature of the corresponding timelike plane has the opposite sign; working or formal ways that introduce sectional curvature should flag this, so learners do not carry "converge means positive" into spacetime.
- Entry explanations are 979 of 1,000 words.
