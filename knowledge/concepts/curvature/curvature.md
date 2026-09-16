---
type: "concept"
schema_version: 2
id: "curvature"
title: "Curvature"
tagline: "How straight walkers that start parallel reveal curvature: positive, negative or zero"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["curvature as departure from flatness", "curved space", "curved spacetime"]
prerequisites: ["parallel-postulate", "geodesic", "flat-metric"]
leads_to: ["intrinsic-versus-extrinsic-curvature", "circumference-to-radius-test", "angular-excess", "path-dependence-of-parallel-transport"]
visuals: ["two-walkers-set-off-side-by-side", "falling-ring-of-crumbs"]
---

# Curvature

*How straight walkers that start parallel reveal curvature: positive, negative or zero*

`curvature` · curvature · foundation · physics-reviewed (revision 7)

**Needs:** [[parallel-postulate]] (entry) · [[geodesic]] (working) · [[flat-metric]] (working)  
**Opens:** [[intrinsic-versus-extrinsic-curvature]] · [[circumference-to-radius-test]] · [[angular-excess]] · [[path-dependence-of-parallel-transport]]  
**Related:** [[flatness-criterion]] · [[gravity-as-spacetime-curvature]]  
**Visuals:** ★ [[two-walkers-set-off-side-by-side]] · [[falling-ring-of-crumbs]]

> Two tiny walkers stand side by side, facing the same way at a right angle to the line between them, and walk without ever steering. Where their paths begin to draw together, as on a ball, the surface has positive curvature. Where they begin to spread apart, as around a swim ring's hole, the surface has negative curvature. Where they keep their gap, the surface is flat, even if it looks bent, like a can's label.

## You will be able to

**Entry**
- Predict whether straight walkers that start parallel draw together or spread apart, and name the curvature. `objectives/tell-the-kind-of-curvature` ← `checks/hole-side-is-not-flat`
- Explain why a can's label, which looks bent, has zero curvature. `objectives/explain-why-looks-mislead` ← `checks/can-label`
- Explain, with a number, why a short trip cannot show Earth's curvature. `objectives/explain-why-short-walks-miss-it` ← `checks/ships-notice-nothing`

**Working**
- Compute Gaussian curvature from a line element. `objectives/compute-gaussian-curvature` ← `problems/which-surface-is-flat`
- Distinguish curvature from position-dependent metric coefficients. `objectives/separate-coordinates-from-curvature` ← `checks/polar-grid-claim`
- Compute the drift of falling neighbours, and explain why a uniform pull shows none. `objectives/compute-tidal-drift` ← `checks/rocket-and-tower`

**Formal**
- Prove that zero Gaussian curvature makes a surface locally Euclidean. `objectives/prove-zero-curvature-is-flat` ← `problems/zero-curvature-is-locally-flat`
- Explain by counting why coordinates cannot remove curvature at a point. `objectives/count-what-coordinates-cannot-remove` ← `checks/count-in-three-dimensions`
- Find the sign of the sectional curvature for a converging free-fall pair. `objectives/sign-of-tidal-curvature` ← `checks/timelike-plane-sign`

## Ways in

### 1. Draw together, keep apart, or spread · entry · picture

*Can a surface curve in more than one way, and how can someone living on it tell?*

**Recap:** Walking without ever steering left or right is called walking straight, and the path is called a straight line. Two straight walkers start parallel when they stand side by side on a straight line drawn between them, both facing the same way at a right angle to that line. On flat ground their gap never changes. On a ball their paths draw together.

Picture a swim ring, the blown-up rubber ring that children float in, lying on a table. Its surface is a fat tube bent round into a circle. Imagine two tiny ants that live on this surface and can only walk along it.

Halfway up the tube, two circles run all the way around the hole: the inner circle, closest to the hole, and the outer circle, farthest from it. The ants start side by side on the inner circle, a few millimetres apart. The half of the ring above that circle is a mirror image of the half below it. So an ant walking along the inner circle has no reason to steer either way, and the inner circle counts as a straight line between the two ants.

Both ants face over the top of the tube, at a right angle to the inner circle, so they start parallel. Each ant walks straight along a loop that goes once around the tube, like a rubber band slipped through the hole. Each loop is a straight line too, because the ring on one side of the loop is a mirror image of the ring on the other side.

Now think of a ring-shaped cake, sliced from above by knife cuts through the centre of its hole, the way a round cake is sliced. Each cut is a mirror that splits the ring into matching sides, so each ant's loop runs along one cut. The two loops are therefore the two cuts of one thin slice. A slice is narrow at the hole and wide at the outside. As the ants walk over the top toward the outer circle, their gap grows: they spread apart.

Seen from above, the width of the slice grows in proportion to the distance from the centre of the hole. On a swim ring 70 centimetres across, with a hole 30 centimetres across, the outer circle is 35 centimetres from that centre and the inner circle only 15. So ants 3 millimetres apart on the inner circle are 7 millimetres apart when they reach the outer circle.

Now start two ants side by side on the outer circle instead, facing over the top toward the hole. The outer circle is a straight line for the same mirror reason. These ants walk along a slice from its wide end to its narrow end, so their gap shrinks: they draw together. On one ring, then, straight walkers that start parallel can draw together or spread apart, depending on where they start.

The way a surface makes such walkers draw together, keep their gap, or spread apart is called its curvature.

Where such walkers begin to draw together, as on a ball or on the outer part of the ring, the curvature is called positive.

Where they begin to spread apart, as on the part of the ring around the hole, the curvature is called negative.

Where they keep their gap, as on flat ground, the curvature is zero.

**Try it:** Lay a bagel on a table. Slip two rubber bands through its hole and around its dough, a pencil's width apart at the hole. Seen from above, slide each band until it looks like a spoke of a wheel, pointing at the centre of the hole. Now follow the bands over the top. At the outer side of the bagel, they sit several times farther apart than at the hole.

**Takeaway:** Where straight walkers that start parallel begin to draw together, curvature is positive; where they begin to spread apart, it is negative; where they keep their gap, it is zero.

*Builds on:* [[parallel-postulate]]<br>*Visuals:* [[two-walkers-set-off-side-by-side]]<br>*See:* `checks/hole-side-is-not-flat`

### 2. Why a short walk shows nothing · entry · calculation

*If Earth is curved, why does a short walk never show it?*

**Recap:** Walking without ever steering is called walking straight. Straight walkers start parallel when they stand side by side on a straight line, facing the same way at a right angle to it. On a ball they meet a quarter of the way around.

On a ball, straight walkers that start parallel meet a quarter of the way around. A football, the round kind used in soccer, measures about 70 centimetres around its middle. A quarter of that is about 17 and a half centimetres, so on a football the walkers meet after that much walking. Earth, treated as a smooth ball, measures about 40,000 kilometres around, so there they meet after about 10,000 kilometres.

The drawing together therefore shows much sooner on the small ball. This is what it means for the smaller ball to curve more strongly. A bigger ball curves more gently, and over a short walk a very big ball is hard to tell from flat ground.

Near the start, the gap also closes very slowly. Two friends on Earth start parallel, 100 metres apart, and walk straight for 5 kilometres. That is one two-thousandth of the 10,000 kilometres to their meeting point. If the gap shrank at an even rate, it would lose one two-thousandth of 100 metres, which is 5 centimetres. In fact it shrinks by only about three hundredths of a millimetre, less than the width of a hair.

The gap shrinks so little because the friends set off facing the same way, so at first neither is heading toward the other. Only as they walk on do their paths begin to close in, and the closing grows faster the farther they go. A walk you could take in an hour therefore cannot tell Earth's ground from flat ground.

**Takeaway:** The smaller the ball, the sooner straight walkers that start parallel meet, so it curves more strongly. Over a short walk on Earth, the change in their gap is far too small to notice.

*Continues:* `ways_in/draw-together-or-spread`<br>*See:* `checks/ships-notice-nothing`

### 3. Looks are not the test · entry · contrast

*Does a surface that looks bent from outside have to be curved?*

**Recap:** Walking without ever steering is called walking straight. Straight walkers start parallel when they stand side by side on a straight line, facing the same way at a right angle to it. Curvature is the way a surface makes them draw together, keep their gap, or spread apart.

Picture the paper label wrapped around a tin can. From outside, the label looks bent. Imagine two ants on the label that start parallel, pointing any way you like along the paper, and walk straight.

Peel the label off and unroll it onto a table. Nothing on it stretches or squashes. So every line drawn on it keeps its length, and every angle between two lines keeps its size.

To steer left, an ant's right-side feet must cover more ground than its left-side feet, like a runner in an outer lane on the bend of a running track. An ant that never steers covers equal ground with the feet on both its sides. Unrolling keeps every length along the paper, so those two distances stay equal on the table. A path that never steers on the can therefore never steers on the table either.

On the table, the two paths are straight lines on flat paper that start parallel, so their gap never changes. Rolling the label back onto the can changes no length along the paper. Measured along the paper, their gap on the can never changes either.

The label has zero curvature everywhere, although it looks bent. Curvature is not about how a surface looks from outside. It is about what walkers measure along the surface.

A surface with zero curvature everywhere is called flat. In this sense the can's label is flat, and a ball is not. No piece of a ball's surface can be pressed onto a table without stretching or tearing. Pressing without stretching would keep every gap, as unrolling the label did. But on the ball straight walkers that start parallel draw together, and on the table they never do. Press a piece of orange peel onto a table, and its rim splits.

The walkers' test never needs a view from outside. That means the same test works for the space we live in, which nobody can step outside to look at.

**Try it:** Draw two slanting lines, 2 centimetres apart, across a sheet of paper, then roll the sheet into a tube and tape it. From outside, the lines now look like curving spirals. Yet a paper strip pressed against the tube, reaching across from one line to the other at a right angle to them, measures 2 centimetres wherever you put it.

**Takeaway:** A surface can look bent from outside and still have zero curvature, like a can's label; curvature is judged only by what walkers measure along the surface.

*Continues:* `ways_in/draw-together-or-spread`<br>*See:* `checks/can-label`

### 4. One number for a surface · working · calculation

*How is the strength and sign of a surface's curvature put into one number?*

In "Draw together, keep apart, or spread", straight walkers that start parallel revealed the sign of curvature, and in "Why a short walk shows nothing" a smaller ball curved more strongly. One number carries both. The straight walks are geodesics. For two geodesics leaving a common geodesic at right angles, a small gap $D$ obeys the gap law met with the parallel postulate,

$$\frac{d^2D}{ds^2} = -K\,D,$$

where $s$ is the distance run and $K$ is the Gaussian curvature. A sphere of radius $a$ gives $D = D_0\cos(s/a)$, so $K = 1/a^2$. A plane or a tube gives $D = D_0$ and $K = 0$. The hyperbolic plane, whose small pieces are saddle-shaped, gives $D = D_0\cosh(s/a)$ and $K = -1/a^2$. Near the start $D \approx D_0(1 - Ks^2/2)$, so the radius of curvature $|K|^{-1/2}$ is the distance over which the gap changes by a sizeable fraction. On a swim ring $K$ changes sign, as the worked example "Curvature on a swim ring" computes.

Every other test made along the surface reads the same $K$. A ring of points at distance $\rho$ from a centre has length

$$C = 2\pi\rho\left(1 - \frac{K\rho^2}{6} + \dots\right),$$

and the angles of a small geodesic triangle of area $A$ add up to $\pi + KA$ to leading order; both are stated here. On a sphere the exact ring length $C = 2\pi a\sin(\rho/a)$ expands to the first. For Earth, $K = 1/(6371\ \text{km})^2 = 2.46\times10^{-14}\ \text{m}^{-2}$, so a geodesic triangle covering 10,000 km² has angles exceeding $\pi$ by only $2.5\times10^{-4}$ rad.

**Takeaway:** The Gaussian curvature is the one number that every test along a surface reads: positive on a sphere, zero on a plane or tube, and negative on saddle-like surfaces.

*Continues:* `ways_in/draw-together-or-spread`, `ways_in/how-soon-it-shows`<br>*Builds on:* [[geodesic]], [[parallel-postulate]]<br>*Visuals:* [[two-walkers-set-off-side-by-side]]<br>*See:* `worked_examples/swim-ring-curvature`, `problems/which-surface-is-flat`

### 5. Curved labels on flat ground · working · contrast

*Can a metric that varies from place to place still describe flat space, and does flat mean Euclidean?*

In "Looks are not the test", a can's label had zero curvature although it looked bent. Formulas mislead in the same way. Flat means that some coordinates make the line element constant, with coefficients $\pm1$, throughout a region. In polar coordinates the plane has

$$ds^2 = dr^2 + r^2\,d\phi^2,$$

whose coefficient $r^2$ varies, and whose lines of constant $\phi$ spread apart. Yet $x = r\cos\phi$, $y = r\sin\phi$ turn it into $dx^2 + dy^2$. The spokes spread because they leave one point in different directions; they never start parallel.

A varying coefficient is therefore no evidence either way. The evidence must be a measurement that no relabelling changes. On the sphere $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, the ring at ground distance $\rho$ from the pole has $C = 2\pi a\sin(\rho/a)$, shorter than the $2\pi\rho$ that every small ring in a flat region has. So no coordinates make any piece of the sphere flat.

Flat does not mean Euclidean. Minkowski spacetime, $ds^2 = -c^2dt^2 + dx^2 + dy^2 + dz^2$, is constant in inertial coordinates, so it is flat: free particles at rest relative to one another keep their separation. It is not Euclidean, because of the minus sign: a light ray has $ds^2 = 0$. The same spacetime, described from a rocket whose floor at $x = 0$ has proper acceleration $g$ along $x$, reads

$$ds^2 = -\left(1 + \frac{gx}{c^2}\right)^2c^2dt^2 + dx^2 + dy^2 + dz^2,$$

a gravitational pull with no curvature at all; the substitution $cT = (c^2/g + x)\sinh(gt/c)$, $X = (c^2/g + x)\cosh(gt/c)$ returns the constant form.

**Takeaway:** Position-dependent metric coefficients do not show curvature, and flat does not mean Euclidean: Minkowski spacetime, even seen from a rocket, is flat.

*Continues:* `ways_in/looks-are-not-the-test`<br>*Builds on:* [[flat-metric]]<br>*See:* `checks/polar-grid-claim`

### 6. Falling neighbours show it · working · operational

*How does anyone measure the curvature of spacetime?*

The walkers of "Draw together, keep apart, or spread" tested a surface by letting straight paths that start parallel run side by side. In general relativity, falling freely is the straightest possible motion through spacetime. So the spacetime version of the test releases two small bodies side by side, at rest relative to each other, and follows their separation.

A pull that is the same on both bodies gives them the same acceleration, so their separation never changes. The rocket of "Curved labels on flat ground" produces weight and falling in flat spacetime, and bodies released side by side in it keep their separation. Only a difference in pull across the separation changes it. Near a spherical mass $M$, Newton's law gives, for a small separation $\xi$ across or along the line to the centre,

$$\frac{d^2\xi_\perp}{dt^2} = -\frac{GM}{r^3}\,\xi_\perp,\qquad \frac{d^2\xi_\parallel}{dt^2} = +\frac{2GM}{r^3}\,\xi_\parallel,$$

built in the derivation "Tidal accelerations from Newton's law". At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \text{s}^{-2}$. Two stones 1 m apart side by side, dropped from rest through 100 m in 4.5 s, end $1.6\times10^{-5}$ m closer.

No freely falling frame removes these relative accelerations, and general relativity identifies them with the curvature of spacetime, a claim taken on trust here. Satellite gradiometers measure them directly, as the GOCE observation records. The comparison with walkers on a ball concerns behaviour only: in the course convention, the sectional curvature of the plane spanned by the fall and a converging separation is negative.

**Takeaway:** Spacetime curvature shows as a change in the separation of freely falling neighbours; a uniform pull, as in an accelerating rocket, changes nothing.

*What this leaves out:* Newtonian limit near a static spherical mass, with separations much smaller than $r$ and falls short enough that $r$ barely changes.

*Continues:* `ways_in/draw-together-or-spread`, `ways_in/curved-labels-on-flat-ground`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/tidal-accelerations-from-newton`, `observations/goce-gravity-gradients`, `checks/rocket-and-tower`

### 7. Flat exactly, and what coordinates cannot remove · formal · structure

*What exactly is flatness, why can coordinates not remove curvature, and what does its sign control?*

"Curved labels on flat ground" took flat to mean that some coordinates make the metric constant, and "One number for a surface" read curvature from the gap law. Both become exact; set $G = c = 1$. Let $(\mathcal M, g)$ be a smooth manifold with a metric of any signature and its Levi-Civita connection $\nabla$. The metric is flat on an open set $U$ if every point of $U$ lies in a chart with $g_{\mu\nu} = \eta_{\mu\nu}$, a constant diagonal matrix of entries $\pm1$. Curvature is the Riemann tensor, $R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$, with components as in the course conventions.

Flatness criterion: $g$ is flat on $U$ if and only if $R = 0$ on $U$. If $g_{\mu\nu}$ is constant, every Christoffel symbol vanishes, so $R = 0$. Conversely, $R = 0$ makes parallel transport path independent in a simply connected neighbourhood, so an orthonormal frame at a point extends to a parallel frame $e_a$. Its dual one-forms obey $d\theta^a = -\omega^a{}_b\wedge\theta^b = 0$, since torsion vanishes and $\omega = 0$ in a parallel frame. So locally $\theta^a = dx^a$ and $g = \eta_{ab}\,dx^adx^b$.

What coordinates cannot remove. At a point $p$ in $n$ dimensions, the $n^2(n+1)/2$ second derivatives of a coordinate change match the $n^2(n+1)/2$ first derivatives of $g_{\mu\nu}$, so $\Gamma(p) = 0$ is attainable. The $n^2(n+1)(n+2)/6$ third derivatives face $n^2(n+1)^2/4$ second derivatives of $g_{\mu\nu}$, leaving at least $n^2(n^2-1)/12$ combinations unchanged: 1 for $n = 2$ and 20 for $n = 4$, the independent components of $R$.

Sign. On a surface $R_{1212} = K\det g$, and a normal Jacobi field $fN$ along a unit-speed geodesic obeys $f'' + Kf = 0$. With $f(0) = 1$ and $f'(0) = 0$, Sturm comparison shows that $K \ge k > 0$ forces a zero of $f$ at or before $s = \pi/(2\sqrt{k})$, while $K \le 0$ keeps $f \ge 1$. In higher dimensions the sectional curvature $K(X,Y)$ of each 2-plane plays this role, and its sign can differ between planes at one point. For a timelike plane the course denominator is negative, so converging free-fall pairs have $K < 0$.

Limits. The criterion is local. A flat cylinder, a flat torus and a cone with its tip removed have $R = 0$, yet none is isometric to Euclidean space, and loops around the cone's tip return vectors rotated. Flatness is independent of signature: Minkowski spacetime is flat without being Euclidean.

**Takeaway:** A metric is flat exactly where its Riemann tensor vanishes; coordinates can remove the metric's first derivatives at a point, never its curvature, and flatness is local.

*Continues:* `ways_in/one-number-for-a-surface`, `ways_in/curved-labels-on-flat-ground`<br>*Builds on:* [[flat-metric]], [[geodesic]]<br>*See:* `problems/zero-curvature-is-locally-flat`, `checks/count-in-three-dimensions`, `checks/timelike-plane-sign`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| start parallel | — | Two straight walkers start parallel when they stand side by side on a straight line, facing the same way at a right angle to it. | — |
| curvature | — | The way a surface makes straight walkers that start parallel draw together, keep their gap, or spread apart. | [[curvature]] |
| positive curvature | — | Curvature that makes straight walkers that start parallel draw together, as on a ball. | [[curvature]] |
| negative curvature | — | Curvature that makes straight walkers that start parallel spread apart, as near a swim ring's hole. | [[curvature]] |
| flat | — | Having zero curvature everywhere, so straight walkers that start parallel keep their gap, as on a can's label. | [[flat-metric]] |

## Key equations

### Gap law for geodesics that start parallel · working

$$
\frac{d^2D}{ds^2} = -K\,D
$$

The gap between nearby geodesics that start parallel bends toward zero where $K > 0$ and away from it where $K < 0$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $D$ | gap between the geodesics | the gap |
| $s$ | distance run along each geodesic | the distance run |
| $K$ | Gaussian curvature where the geodesics are | the Gaussian curvature |

**Holds when:** Geodesics leaving a common geodesic at right angles, so $D'(0) = 0$, with $D' = dD/ds$ and $s = 0$ at the common geodesic. Exact for constant $K$ when $D$ is measured along the curve that stays a fixed distance $s$ from the common geodesic; where $K$ varies, valid to first order in the gap. The strip of surface between the two geodesics must be smooth, with no cone tip anywhere in that strip. A cone tip is a single point where curvature is concentrated.  
**Say it:** “The second derivative of the gap equals minus the Gaussian curvature times the gap.”  
**Justified by:** `parallel-postulate`

### Length of a small ring · working

$$
C = 2\pi\rho\left(1 - \frac{K\rho^2}{6} + \dots\right)
$$

A small ring falls short of $2\pi\rho$ where $K > 0$ and exceeds it where $K < 0$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C$ | length of the ring | the ring length |
| $\rho$ | geodesic distance from the centre to the ring | rho |
| $K$ | Gaussian curvature at the centre | the Gaussian curvature |

**Holds when:** Smooth surface, with $\rho$ small compared with $|K|^{-1/2}$.  
**Say it:** “The ring length is two pi rho times one minus K rho squared over six, plus smaller terms.”  
**Justified by:** `stated`

### Relative accelerations of falling neighbours · working

$$
\frac{d^2\xi_\perp}{dt^2} = -\frac{GM}{r^3}\,\xi_\perp,\qquad \frac{d^2\xi_\parallel}{dt^2} = +\frac{2GM}{r^3}\,\xi_\parallel
$$

Near a spherical mass, falling neighbours side by side draw together, and neighbours one above the other drift apart.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi_\perp$ | separation across the line to the centre | the sideways separation |
| $\xi_\parallel$ | separation along the line to the centre | the vertical separation |
| $r$ | distance from the centre of the mass $M$ | r |

**Holds when:** Newtonian field of a static spherical mass; separations much smaller than $r$.  
**Say it:** “Sideways, the separation accelerates inward at G M over r cubed times the separation; vertically, outward at twice that.”  
**Justified by:** `derivations/tidal-accelerations-from-newton`

## Derivations

### Tidal accelerations from Newton's law · working

**Goal:** Find the relative acceleration of two nearby falling bodies near a spherical mass $M$, across and along the line to the centre.

1. Each body accelerates toward the centre with magnitude $g(r) = GM/r^2$, along its own line to the centre.
2. Side by side at the same $r$, the two lines meet at the centre at the small angle $\xi_\perp/r$.
3. Each acceleration has a component $g\,\xi_\perp/2r$ toward the other body, so $d^2\xi_\perp/dt^2 = -g\,\xi_\perp/r = -(GM/r^3)\,\xi_\perp$.
4. One above the other, at $r$ and $r + \xi_\parallel$, the accelerations differ by $g(r) - g(r + \xi_\parallel) \approx (2GM/r^3)\,\xi_\parallel$.
5. The lower body has the larger acceleration, directed away from the upper one, so $d^2\xi_\parallel/dt^2 = +(2GM/r^3)\,\xi_\parallel$.

**Result:** $d^2\xi_\perp/dt^2 = -(GM/r^3)\,\xi_\perp$ and $d^2\xi_\parallel/dt^2 = +(2GM/r^3)\,\xi_\parallel$, to first order in $\xi/r$.

## Worked examples

### Curvature on a swim ring · working

**Problem:** A swim ring is a torus with tube radius $r = 10$ cm and centre-circle radius $R = 25$ cm. Loops around the tube cross its inner and outer circles, the circles of radius $R - r$ and $R + r$ halfway up the tube, at right angles. Use the gap law to find the Gaussian curvature and the radius of curvature on each of these circles.

1. Each loop lies in a plane through the ring's axis, so it is a geodesic by mirror symmetry. At distance $s$ along it from the outer circle, it is $R + r\cos(s/r)$ from the axis.
2. Two loops whose planes differ by the angle $\Delta\phi$ are separated, along the circle about the axis, by $D(s) = \Delta\phi\,(R + r\cos(s/r))$.
3. On the outer circle $D'(0) = 0$ and $D''(0)/D(0) = -1/[r(R + r)]$, so $K = 1/[r(R + r)] = 1/350\ \text{cm}^{-2}$.
4. From the inner circle $D(s) = \Delta\phi\,(R - r\cos(s/r))$, so $D''(0)/D(0) = +1/[r(R - r)]$ and $K = -1/[r(R - r)] = -1/150\ \text{cm}^{-2}$.
5. The radii of curvature $|K|^{-1/2}$ are $\sqrt{350}$ cm $= 18.7$ cm and $\sqrt{150}$ cm $= 12.2$ cm.

**Answer:** $K = +2.86\times10^{-3}\ \text{cm}^{-2}$ on the outer circle (radius of curvature 18.7 cm) and $K = -6.67\times10^{-3}\ \text{cm}^{-2}$ on the inner circle (12.2 cm).

**Takeaway:** One surface can carry both signs of curvature, and the gap law reads each from how loops that start parallel begin to separate.

## Problems

### `which-surface-is-flat` · working · difficulty 2 · calculation

Two surfaces have line elements $ds^2 = d\rho^2 + \rho^2\,d\phi^2$ and $ds^2 = d\rho^2 + a^2\sinh^2(\rho/a)\,d\phi^2$, where $\rho$ is geodesic distance from a centre and $a$ is a constant length. For each, find the ring length at distance $\rho$, the Gaussian curvature at the centre, and the ring length at $\rho = a$ divided by $2\pi a$.

**Hints**

1. On a ring $\rho$ is fixed, and $\sinh x = x + x^3/6 + \dots$.

**Answer:** The first is flat: $C = 2\pi\rho$, $K = 0$, ratio 1. The second has $C = 2\pi a\sinh(\rho/a)$, $K = -1/a^2$, and ratio $\sinh 1 = 1.175$.

**Must contain:** The first ring is exactly two pi rho, so K is zero; The second ring gives K equal to minus one over a squared; Ratio sinh one, about 1.175

**Numeric:** ring length at rho equal to a over 2 pi a, second surface = 1.1752 1 (magnitude, ±1%)

**Solution**

1. On a ring $d\rho = 0$, so the first gives $C = 2\pi\rho$ exactly, and the small-ring formula gives $K = 0$; indeed $x = \rho\cos\phi$, $y = \rho\sin\phi$ make it $dx^2 + dy^2$.
2. The second gives $C = 2\pi a\sinh(\rho/a) = 2\pi\rho\,(1 + \rho^2/6a^2 + \dots)$.
3. Matching $-K\rho^2/6 = +\rho^2/6a^2$ gives $K = -1/a^2$.
4. At $\rho = a$ the ratio is $\sinh 1 = 1.1752$. Both coefficients vary with $\rho$, so only the ring lengths tell the surfaces apart.

**Targets:** `varying-metric-means-curved`

### `zero-curvature-is-locally-flat` · formal · difficulty 3 · proof

In geodesic polar coordinates about a point $p$ of a smooth surface, $ds^2 = dr^2 + h(r,\phi)^2\,d\phi^2$ on a normal neighbourhood, with $h(0,\phi) = 0$, $\partial_rh(0,\phi) = 1$, and $K = -\partial_r^2h/h$ for $r > 0$. Prove that if $K = 0$ there, the metric is Euclidean in suitable coordinates. Then explain why a flat torus is not isometric to the Euclidean plane.

**Hints**

1. Solve $\partial_r^2h = 0$ with the conditions at $r = 0$.
2. Compare the torus and the plane as topological spaces.

**Answer:** $h = r$, so $ds^2 = dr^2 + r^2d\phi^2 = dx^2 + dy^2$ with $x = r\cos\phi$, $y = r\sin\phi$. A flat torus is compact and the plane is not, so no isometry joins them: flatness is local.

**Must contain:** Zero curvature and the conditions at the centre give h equal to r; Cartesian coordinates then make the metric Euclidean; The compact torus cannot be isometric to the plane

**Solution**

1. With $K = 0$ and $h > 0$ for $r > 0$, $\partial_r^2h = 0$, so $h = A(\phi) + B(\phi)\,r$.
2. As $r \to 0$, $h(0,\phi) = 0$ gives $A = 0$ and $\partial_rh(0,\phi) = 1$ gives $B = 1$, so $h = r$.
3. Then $ds^2 = dr^2 + r^2d\phi^2$, and $x = r\cos\phi$, $y = r\sin\phi$ give $dx^2 + dy^2$. These are the normal coordinates of the exponential map, so they are smooth at $p$ too.
4. A flat torus, a square with opposite edges identified by translations, has $K = 0$ everywhere but is compact. An isometry is a homeomorphism and the plane is not compact, so none exists.

## Observations

- **Gravity gradients measured by the GOCE satellite's gradiometer, 2009 to 2013** (measured, working). Pairs of accelerometers 0.5 m apart inside the freely falling satellite measured the relative accelerations of their test masses, the Newtonian face of spacetime curvature read by falling neighbours. *Numbers:* The dominant gradient along the line to Earth's centre, about $2.7\times10^{-6}\ \text{s}^{-2}$, matches $2GM/r^3$ at the orbit; the mapped signal is the much smaller departure from it. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0

## Teaching arc

1. **Predict on a swim ring** (entry). Pose the swim-ring prediction, then show the spreading with a slice of ring-shaped cake. *Why:* It shows that curvature has a sign. *Predict:* Will ants starting on the circle around the hole draw together or spread apart? *Visual:* [[two-walkers-set-off-side-by-side]] *Uses:* `ways_in/draw-together-or-spread`, `checks/hole-side-is-not-flat`
2. **Size and looks** (entry). Compare a football with Earth, then unroll a can's label. *Why:* It blocks "looks flat, so flat" and "looks bent, so curved". *Uses:* `ways_in/how-soon-it-shows`, `ways_in/looks-are-not-the-test`, `checks/can-label`
3. **Labels and falling** (working). Unmask polar coordinates, then compare dropped balls in a rocket and a tower. *Why:* It separates curvature from coordinates and weight. *Predict:* In a rocket far from any mass, do two dropped balls change their separation? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/curved-labels-on-flat-ground`, `checks/polar-grid-claim`, `ways_in/falling-neighbours-show-it`, `checks/rocket-and-tower`
4. **Criterion and count** (formal). State the flatness criterion, the count, and the timelike sign. *Why:* It turns pictures into theorems. *Uses:* `ways_in/flatness-and-the-count`, `checks/count-in-three-dimensions`, `checks/timelike-plane-sign`

## Misconceptions

### “If straight walkers do not draw together, the ground must be flat.” · entry · `only-closing-means-curved`

- **Why it is tempting:** A ball is the curved surface most people picture.
- **What is true:** Walkers can also spread apart, as near a swim ring's hole: negative curvature. Flat means the gap stays the same.
- **Exposed by:** `checks/hole-side-is-not-flat`

### “Anything that looks bent is curved.” · entry · `bent-means-curved`

- **Why it is tempting:** In everyday speech, curved and bent mean the same thing.
- **What is true:** Curvature is judged along the surface; a can's label unrolls without stretching, so walkers on it keep their gap.
- **Exposed by:** `checks/can-label`

### “Nothing changes over the trips I make, so the ground has no curvature.” · entry · `looks-flat-so-flat`

- **Why it is tempting:** On every trip we make, paths that start side by side seem to keep their gap.
- **What is true:** The gap closes very slowly at first, so a small piece of a curved surface is hard to tell from flat. On Earth, walkers that start parallel meet only after about 10,000 kilometres.
- **Exposed by:** `checks/ships-notice-nothing`

### “If metric coefficients vary from place to place, the space is curved.” · working · `varying-metric-means-curved`

- **Why it is tempting:** The sphere's metric coefficients vary.
- **What is true:** Those of polar coordinates on a flat plane vary too. Only a measurement no relabelling changes, like a ring's length, decides.
- **Exposed by:** `checks/polar-grid-claim`

### “Feeling weight and seeing things fall shows that spacetime is curved.” · working · `weight-means-curvature`

- **Why it is tempting:** Everyday gravity comes with weight and falling.
- **What is true:** A rocket far from any mass gives both in flat spacetime. Only a change in the separation of falling neighbours shows curvature.
- **Exposed by:** `checks/rocket-and-tower`

### “Free-fall neighbours that draw together span a positively curved plane.” · formal · `converging-tides-positive-k`

- **Why it is tempting:** Walkers on a ball draw together.
- **What is true:** A timelike plane makes the sectional curvature's denominator negative, so converging pairs give a negative value. The behaviour matches the sphere; the sign does not.
- **Exposed by:** `checks/timelike-plane-sign`

## Checks

1. **Entry · evaluate-claim** `checks/hole-side-is-not-flat`. On a swim ring, two ants start parallel on the inner circle, the circle around the hole halfway up the tube, and walk straight over the top of the tube. A classmate says: "Their paths do not draw together, so that part of the ring must be flat." Is the classmate right?
   - **Hints:** Where is a slice of ring-shaped cake widest?
   - **Answer:** No. Think of a ring-shaped cake sliced from above by knife cuts through the centre of its hole, the way a round cake is sliced. Each cut is a mirror that splits the ring into matching sides, so each ant's loop runs along one cut, and the two loops are the two cuts of one thin slice. A slice is narrow at the hole and wide at the outside, so the ants spread apart as they walk toward the outer circle. Flat would mean that their gap stays the same. Spreading apart means negative curvature, so that part of the ring is curved, in the opposite way from a ball.
   - **Must contain:** No; The ants spread apart as the slice widens; Spreading apart is negative curvature
   - **Targets:** `only-closing-means-curved`
   - **Visual:** [[two-walkers-set-off-side-by-side]]
2. **Entry · evaluate-claim** `checks/can-label`. Two ants start parallel on the paper label of a tin can and walk straight. A friend says: "The label is bent around the can, so the ants must draw together, like ants on a ball." Is the friend right?
   - **Hints:** What happens to the ants' paths when you unroll the label?
   - **Answer:** No. Unroll the label onto a table: nothing stretches or squashes, so every length along the paper stays the same. An ant that never steers covers equal ground with the feet on both its sides, and unrolling keeps those distances equal, so its path never steers on the table either. On the flat paper the two paths are straight lines that start parallel, so their gap never changes. Rolling the label back changes no length along the paper, so on the can their gap never changes either. The label has zero curvature, although it looks bent.
   - **Must contain:** No; The label unrolls without stretching, so paths that never steer stay that way; On flat paper, and so on the can, the gap never changes
   - **Targets:** `bent-means-curved`
3. **Entry · evaluate-claim** `checks/ships-notice-nothing`. Treat Earth as a smooth ball. Two ships start parallel, 10 kilometres apart, and sail without ever steering for 100 kilometres. Their gap shrinks by only about 1.2 metres. A sailor says: "So the sea is flat." Is the sailor right?
   - **Hints:** On flat ground, how much would the gap shrink?
   - **Answer:** No. On a flat surface, straight paths that start parallel keep their gap exactly, so any shrinking at all shows curvature, and shrinking means positive curvature. The shrinking is small for two reasons. First, Earth is huge: ships that start parallel meet only after about 10,000 kilometres, a quarter of the way around. Second, the gap closes very slowly at first, because the ships set off facing the same way, with neither heading toward the other.
   - **Must contain:** No; Any shrinking shows curvature; Earth is huge, and the gap closes slowly at first
   - **Targets:** `looks-flat-so-flat`
4. **Working · evaluate-claim** `checks/polar-grid-claim`. In polar coordinates, the plane's line element has a coefficient, r squared, that changes from place to place, and the spokes of constant angle spread apart. A student concludes that the plane is curved. Evaluate the argument.
   - **Hints:** Substitute $x = r\cos\phi$, $y = r\sin\phi$ into $dx^2 + dy^2$.
   - **Answer:** Both observations are true, and neither shows curvature. With $x = r\cos\phi$ and $y = r\sin\phi$, $dx^2 + dy^2 = dr^2 + r^2d\phi^2$, so other coordinates make the metric constant and the plane is flat. The lines of constant $\phi$ spread because they leave one point in different directions; they never start parallel. A ring at radius $r$ measures exactly $2\pi r$, the flat value, so $K = 0$.
   - **Must contain:** Cartesian coordinates make the metric constant; The spokes never start parallel; A ring at radius r measures two pi r
   - **Targets:** `varying-metric-means-curved`
5. **Working · numeric** `checks/rocket-and-tower`. Two small balls, one 2.0 m above the other, are released from rest and fall 100 m with no air: once in a rocket far from any mass, accelerating at 9.8 m/s², and once near Earth, radius 6371 km. How much does their separation change in each case?
   - **Hints:** In the rocket, does anything act differently on the two balls?
   - **Answer:** In the rocket, both balls move freely from the same velocity, so their separation stays 2.0 m; only the floor accelerates toward them. Near Earth, the lower ball is pulled harder, and the separation obeys $d^2\xi/dt^2 = +(2GM/R^3)\,\xi$ with $GM/R^3 = g/R = 1.54\times10^{-6}\ \text{s}^{-2}$. The fall takes $t = \sqrt{2h/g} = 4.5$ s, so the separation grows by $\tfrac12(2g/R)\,\xi\,t^2 = 2\xi h/R = 6.3\times10^{-5}$ m. Only the tower shows curvature.
   - **Must contain:** No change in the rocket; About 0.063 millimetres of growth near Earth; Only the tower shows curvature
   - **Numeric:** change in separation in the rocket = 0 m (magnitude, ±1e-06); growth in separation near Earth = 6.28e-05 m (magnitude, ±5%)
   - **Targets:** `weight-means-curvature`
   - **Visual:** [[falling-ring-of-crumbs]]
6. **Formal · explain** `checks/timelike-plane-sign`. With $G = c = 1$, neighbours falling near a spherical mass, separated along a horizontal unit vector $e_{\hat x}$, draw together, with $R^{\hat x}{}_{\hat t\hat x\hat t} = M/r^3$. Find the sign of $K(u, e_{\hat x})$ for four-velocity $u$, and compare with a sphere.
   - **Hints:** Evaluate the denominator for a timelike and a spacelike unit vector.
   - **Answer:** The numerator is $R_{\hat t\hat x\hat t\hat x} = R_{\hat x\hat t\hat x\hat t} = M/r^3$, by pair symmetry and $g_{\hat x\hat x} = 1$. The denominator is $g(u,u)\,g(e_{\hat x},e_{\hat x}) - g(u,e_{\hat x})^2 = -1$. So $K = -M/r^3 < 0$. Converging geodesics on a sphere lie in a plane with $K = +1/a^2$. The behaviour, convergence, is the same; the sign is opposite because the plane is timelike.
   - **Must contain:** Numerator M over r cubed; Denominator minus one; Negative, unlike the sphere, though both converge
   - **Targets:** `converging-tides-positive-k`
7. **Formal · numeric** `checks/count-in-three-dimensions`. At a point of a three-dimensional Riemannian manifold, how many combinations of second derivatives of the metric can no coordinate change remove, and what do they count? Why can all first derivatives be removed?
   - **Hints:** A symmetric index pair takes 6 values, a symmetric triple 10.
   - **Answer:** The metric has 6 components and there are 6 symmetric pairs of derivatives, so there are $6\times6 = 36$ second derivatives. A coordinate change has $3\times10 = 30$ third derivatives. At least $36 - 30 = 6$ combinations survive, equal to $n^2(n^2-1)/12 = 6$, the independent Riemann components in three dimensions. The $3\times6 = 18$ first derivatives of the metric are matched by the $3\times6 = 18$ second derivatives of the coordinate change, so $\Gamma(p) = 0$ is attainable.
   - **Must contain:** 36 second derivatives against 30 third derivatives; Six remain: the independent Riemann components; 18 first derivatives match 18 second derivatives
   - **Numeric:** curvature combinations that cannot be removed = 6 1 (magnitude, ±0)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of sectional curvature for timelike planes | $K(X,Y) = R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma/\big(g(X,X)g(Y,Y) - g(X,Y)^2\big)$; a sphere has $K = +1/a^2$, and converging free-fall pairs have $K < 0$. | Some texts use the absolute value of the denominator, or the opposite Riemann sign, and give converging tidal pairs positive curvature. |

## Visuals

- ★ [[two-walkers-set-off-side-by-side]] (flagship): Flagship: walkers that start parallel draw together, keep their gap or spread, including on the inner and outer circles of a swim ring. *Sketch:* Add a swim ring to the proposed walker scene. Walkers leave its inner or outer circle, halfway up the tube, at right angles; the gap plot and a positive, zero or negative badge update as they set off.
- [[falling-ring-of-crumbs]] (supporting): Tidal drift of falling neighbours as the spacetime version of the walker test. *Sketch:* A ring of falling crumbs near a mass stretches along the line to the centre and squeezes across it; a switch swaps the mass for an accelerating rocket, where the ring keeps its shape.

## Tutor moves

**Open with**

- A swim ring lies on a table. Two tiny ants stand side by side on the circle around its hole, halfway up the tube, facing over the top of the tube. Walking without ever steering, will they draw together, keep their gap, or spread apart? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why the gap changes.* → Hand over a bagel with two rubber bands, or sketch one slice of a ring-shaped cake. *Uses:* `ways_in/draw-together-or-spread`

**Common questions**

- *Does curvature have anything to do with gravity?* (entry) Yes. General relativity, today's theory of gravity, describes gravity as curvature of space and time. Drop two stones side by side, a metre apart, from the top of a tower 100 metres tall. Each falls toward the centre of Earth, so their paths aim at the same spot and draw slightly together. By the time they reach the ground they are about a sixtieth of a millimetre closer. A pull exactly the same on both stones, in size and in direction, would never change their gap. So it is the change in the gap, not the falling itself, that shows curvature. *Uses:* `ways_in/falling-neighbours-show-it`

**Switching levels**

- To working when: asks for a number or a formula. Go to the gap law and the swim-ring example. *Uses:* `ways_in/one-number-for-a-surface`, `worked_examples/swim-ring-curvature`
- To formal when: asks whether curvature can be transformed away. State the flatness criterion and the count. *Uses:* `ways_in/flatness-and-the-count`, `checks/count-in-three-dimensions`

**Pronunciations:** Gauss → GOWSS; Riemann → REE-mahn; Minkowski → min-KOF-skee; GOCE → GOH-chay

## History

- **Carl Friedrich Gauss (1827).** Defined the curvature of a surface as one number at each point, now called its Gaussian curvature, and proved that measurements within the surface determine it. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Bernhard Riemann (1854).** Extended curvature to spaces of any dimension in a lecture given in 1854, published in 1868. Bernhard Riemann (1868), *Über die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** On a swim ring, two ants start next to each other on the edge by the hole and walk over the tube without turning. A slice of a ring cake gets wider toward the outside, so they get farther apart, and that is negative curvature. On a ball they get closer, which is positive, and on flat ground they stay the same, zero. I wasn't sure what the 'edge' of a ring is, since it's round all over, or why the ants' path has to follow a cake cut, or how much farther apart they get. A football makes walkers meet after less than 18 centimetres and Earth after 10,000 kilometres, so a smaller ball curves more. On a 5 kilometre walk the gap only shrinks by a hair, but I don't see why it is so much less than a small share of the gap. A can's label looks bent but you can unroll it without stretching, so walkers keep their gap and it is flat. I didn't follow the sentence about steering changing angles to lines on the paper, and 'no piece of a ball can lie flat' mixed up the two meanings of flat.

Second full novice reading, of revision 4, on 2026-09-13, before this pass's fixes: Curvature is about two tiny walkers who set off side by side, facing the same way at a right angle to the line between them, and never steer. On a swim ring there is a circle around the hole and a circle on the outside, both halfway up the tube. Ants who start on the inner one and walk over the top end up farther apart, because their two paths are the two cuts of one cake slice and a slice is wider at the outside: 3 millimetres becomes 7. That is negative curvature. Starting on the outer circle they draw together, which is positive, as on a ball. Keeping the gap is zero, which is called flat. A football is small, so walkers meet after 17 and a half centimetres; Earth is huge, so they meet after 10,000 kilometres, and over a 5 kilometre walk the gap loses three hundredths of a millimetre instead of the 5 centimetres an even rate would take off. A can's label looks bent, but it unrolls without stretching, so ants on it keep their gap and it is flat; a ball's surface cannot be pressed onto a table, like orange peel that splits at its rim. The test uses only what walkers measure along the surface, so it works for the space we live in as well. All three entry takeaways came back. Two things stopped me. The one-line description promised the curvature's 'sign', and I could not tell whether that meant a plus-or-minus sign or a signal that curvature is there, since nothing else I read used the word. And where the cake is 'sliced straight down' I first read 'straight' as the walking word the note had just defined, and had to reread the sentence.

**Stumbles (29)**

- “Two tiny walkers set off side by side, facing the same way, and never steer.”: The summary drops the right angle that makes walkers start parallel, so on a ball 'facing the same way' has no clear meaning.
- “Small pieces of a smooth curved surface pass for flat, which is why a short walk on Earth shows nothing.”: 'Smooth' and 'pass for flat' are undefined idioms, and the summary ran past its character limit once the first sentence was fixed.
- “Two straight walkers start parallel when they stand side by side on a straight line, both facing the same way, at a right angle to it.”: 'On a straight line' does not say which line, and 'it' could be the line or the way they face.
- “The ants start side by side on the inner edge, the circle around the hole”: A swim ring has no edge; its surface is round all over. Many circles run around the hole, so the reader cannot tell which one is meant. 'Edge' also clashes with the later idea of a surface with no sharp points.
- “So an ant walking along the edge has no reason to steer, and the edge is a straight line for the ants.”: A step left implicit: the ants never walk along this circle, so the reader wonders why its straightness matters. It matters because starting parallel needs a straight line between them.
- “Think of a ring-shaped cake, cut into slices by knife cuts through the centre of its hole.”: A cut 'through the centre of its hole' can be pictured as a sideways cut, like halving a bagel.
- “Each ant's loop lies along one such cut”: A claim with no reason: why does a rubber-band loop follow a knife cut?
- “A slice is narrow at the hole and wide at the outside. So as the ants walk over the top toward the outer edge, their gap grows”: A surprising claim with no number; the reader cannot tell whether the spreading is large or tiny.
- “Now start two ants side by side on the outer edge instead, facing over the top toward the hole. The same slice shows their gap shrinking”: A step taken on trust: nothing says the outer circle is a straight line, which starting parallel needs, and 'the same slice shows' hides that they walk it from the wide end.
- “Seen from above, turn each band to line up with the centre of the hole.”: A rule the reader cannot follow: 'line up with' a point does not say how the band should look, and the try-it does not say how big the difference is.
- “So on a football, the walkers meet after less than 18 centimetres of walking. On Earth, treated as a smooth ball, they meet after about 10,000 kilometres.”: Two arithmetic steps left implicit: a quarter of 70 centimetres, and Earth's distance around.
- “Their gap shrinks by only about three hundredths of a millimetre, less than the width of a hair.”: A surprise with no reason: a teenager expects 5 kilometres, one two-thousandth of the way to meeting, to take off one two-thousandth of the gap, 5 centimetres. 'Near the start, the gap also closes very slowly' asserts the answer without saying why.
- “Small pieces of any smooth surface pass for flat in the same way: the gap between straight walkers changes noticeably only over long enough walks.”: 'Smooth', 'pass for flat' and 'long enough' are undefined; the sentence adds a general claim the way's question does not need.
- “Imagine two ants on the label that start parallel and walk straight.”: Starting state ambiguous: around the can or along it? The reader wonders whether the answer depends on the direction.
- “Steering changes the angle between a path and lines drawn on the paper. Unrolling keeps those angles, so an ant path that never steers on the can also never steers on the table.”: Reread twice: which lines drawn on the paper, and why would steering change an angle to them? The link between 'never steers' and something unrolling keeps is left implicit.
- “Rolling the label back onto the can changes no length along the paper, so on the can their gap never changes either.”: The gap on the can could be measured through the air across the can; the sentence does not say it is measured along the paper.
- “No piece of a ball can lie flat without stretching”: 'Flat' used in two senses: zero curvature, defined one sentence earlier, and lying flat on a table. The reason is also partly implicit.
- “So the same test can be asked of space itself”: An awkward phrase ('asked of'), and 'space itself' is vague for this reader.
- “Looks are not the test (no try_it)”: The claim that a bent-looking surface can be flat is the note's biggest surprise and had no household test.
- “Each ant walks along one knife cut through the middle of the ring, like a cut through a ring-shaped cake”: In the check, 'through the middle of the ring' differs from the way's cut and gives no reason the loop follows a cut; 'the edge around the hole' in the question has the same problem as the way.
- “The ants' paths never steer, so on the flat paper they are straight lines that start parallel”: The check answer relied on the way's unclear angle argument.
- “Two ships start parallel, 10 kilometres apart, and sail straight for 100 kilometres.”: Ships steer all the time; 'sail straight' needs the note's meaning spelled out. The answer's 'On flat ground' does not fit the sea, and 'here it is positive' has an unclear 'it'.
- “Curved things we see, like cans and hoses, look bent.”: Circular: it says curved things look bent, which is the belief itself.
- “Short trips seem to keep straight paths' gaps.”: Squeezed wording that is hard to say aloud; 'small pieces pass for flat' in the correction is an idiom.
- “Both head for the centre of Earth, so they end about a sixtieth of a millimetre closer. A pull exactly the same on both stones would never change their gap.”: A step left implicit: heading for one spot means the paths aim together. 'Exactly the same' pulls toward Earth's centre differ in direction, so the sentence fails the first what-if.
- “How straight walkers that start parallel reveal a surface's curvature and its sign”: The tagline is the first line an entry reader meets, and 'sign' appears nowhere else at the entry rung, where the note says 'positive', 'negative' and 'zero'. A 16-year-old reads 'sign' as a signal that curvature is there, not as plus or minus.
- “Where they begin to spread apart, as around a swim ring's hole, it has negative curvature.”: Ambiguous 'it': the nearest noun is the swim ring's hole, and the intended noun, the surface, sits in the previous sentence.
- “Now think of a ring-shaped cake, sliced by knife cuts straight down through the centre of its hole, the way a round cake is sliced.”: 'Straight' in two senses. Four sentences earlier the note defines walking straight as never steering, and the swim-ring way turns on which lines are straight; here 'straight down' means the everyday 'directly'. The same phrase sits in the check 'hole-side-is-not-flat'.
- “Two tiny ants stand side by side on the circle around a swim ring's hole, halfway up the tube, facing over the top of the tube.”: A direction without its reference, in the first sentence a learner hears. The ways fix 'up' by laying the ring on a table, but the tutor speaks this opening question before any way, so nothing says which way is up on a ring that could be standing on its rim.

**Fixes**

- Named the swim ring's inner and outer circles, halfway up the tube, in place of 'edge' everywhere: the entry way, the check, the opening question, the teaching-arc prediction, the visual role and sketch, and the working worked example (which now gives their radii R - r and R + r).
- Swim-ring way: said why the inner circle matters (it is the straight line between the ants), why each loop follows a cake cut (each cut is a mirror), that the outer circle is straight for the same reason, and added a count: 3 millimetres apart at the hole become 7 at the outside on a ring 70 centimetres across with a 30 centimetre hole (35 over 15, checked in python and matching the worked example's R = 25 cm, r = 10 cm).
- Bagel try-it: bands set like wheel spokes seen from above, with the expected result 'several times farther apart'.
- Short-walk way: spelled out a quarter of 70 centimetres and Earth's 40,000 kilometres, and backed 'closes slowly at first' with the even-rate comparison (5 centimetres expected, 0.031 millimetres actual, both checked in python) and a reason (the walkers set off facing the same way).
- Can-label way: replaced the angle argument with an everyday one, that steering makes one side's feet cover more ground, as in an outer running-track lane, which unrolling cannot change. Measured the gap along the paper, removed 'lie flat' (flat in two senses) in favour of pressing onto a table, backed it with orange peel, and added a doable try-it with slanting lines on a paper tube. The physics reviewer should confirm the equal-sides criterion is stated safely (it is exact to first order in the ant's width).
- Checks: can-label and hole-side answers now carry the way's reasons; ships check says 'without ever steering', 'flat surface', and gives both reasons for the small shrinkage.
- Misconceptions: rewrote two why_tempting lines that were circular or squeezed, and the idiom in one correction.
- Common question on gravity: said why the stones draw together, and made 'the same pull' mean the same in size and direction (0.0157 millimetres, about a sixtieth, rechecked).
- Summary: fixed the first sentence to include the right angle, split long sentences, and dropped the short-walk sentence to stay within the 500-character limit; the way 'Why a short walk shows nothing' carries it.
- Dropped, to stay within the 10% entry allowance (1,087 of 1,100): the closing generalization paragraph of 'Why a short walk shows nothing' ('Small pieces of any smooth surface pass for flat...'), the lowest-value item because the way's question is about Earth.
- Ladder: every working and formal way already names the way it continues; no index notation appears at working; entry ideas (sign, smaller ball curves more strongly, gap closes slowly at first, looks mislead) each have a matching working bridge. The seven ways use five kinds. No bridge added.
- Bumped the revision to 2.
- Second full novice reading, of revision 4: tagline 'and its sign' became 'positive, negative or zero', the words the entry rung actually uses; 85 of the 90 characters allowed.
- Summary: the ambiguous 'it has negative curvature' became 'the surface has negative curvature', matching the sentence before it.
- Removed the one use of 'straight' in a second sense: the cake is now 'sliced from above by knife cuts through the centre of its hole' in the entry way 'Draw together, keep apart, or spread' and in the check 'hole-side-is-not-flat', which also gained 'the way a round cake is sliced' so it stands on its own. Same claim, same cut, and the same word count at entry (1,093), so nothing was dropped.
- Opening question 'ants-on-a-swim-ring': added 'A swim ring lies on a table' so 'halfway up the tube' and 'over the top' have a reference before any way has been read.
- Ladder re-checked: each working and formal way still opens by naming the way it continues; no index notation at working; the seven ways still use five kinds. No bridge needed.
- Bumped the revision to 5.

**Concerns**

- Entry way explanations now total 1,087 words, within the 1,100 review allowance but above the 1,000 foundation cap. Tutoring is 1,877 of 2,200. A later re-read has almost no room at entry.
- The summary no longer mentions why a short walk on Earth shows nothing; the objective 'explain-why-short-walks-miss-it' is still taught and checked by the way and check.
- The entry takeaways say 'where they keep their gap, it is zero'. A walker pair starting parallel at the top of a swim ring's tube, where the curvature is zero, keeps its gap only at first. The 'begin to' wording covers draw together and spread; the physics reviewer may want the zero case scoped the same way.
- The physics reviewer should confirm the new can-label reason (a path that never steers has left and right tracks of equal length, to first order in the width) and the 7 millimetre count on the swim ring.
- Glossary headword mismatch across notes remains: parallel-postulate uses 'straight line' with 'walk straight' as a form; this note uses 'walk straight' with 'straight line' as a form. An editor should pick one.
- Four learner-visible strings changed at revision 5 (tagline, summary, one entry-way sentence, one check answer) and one tutor-spoken opening question; a physics diff check of exactly those is due, and the status is back at novice-reviewed until it runs. The validator therefore warns that review.physics covers revision 4.
- Entry way explanations are unchanged at 1,093 words, above the 1,000 foundation cap and inside the 10% review allowance. This pass deliberately chose rewrites that cost no entry words; a further entry addition would have to drop something.
- The registry titles this concept 'Curvature as departure from flatness' and lists the aliases 'non-Euclidean geometry', 'sign of curvature' and 'positive and negative curvature', none of which the note carries. An editor should settle the registry and the note in one direction.

**Re-read** (2026-09-13, revision 4): 2 stumbles in 3 changed passages

- “The slice widens in step with the distance from the centre of the hole, seen from above.”: The switch to a view from outside is announced only at the end, so the reader first pictures the slice from the ant's place on the surface and must reread. 'In step with' is an idiom a 16-year-old may not read as 'in proportion', which the next sentence's numbers (15 to 35, 3 to 7) rely on.
- “Exact for constant $K$ with $D$ measured along the curve at fixed distance $s$ from the common geodesic”: 'The curve' has no antecedent: the only curves in the entry are the geodesics themselves, so an undergraduate cannot tell which curve the gap is measured along. The wording also differs from the parallel-postulate note that justifies the law.
- Fix: Entry, 'Draw together, keep apart, or spread': moved 'Seen from above' to the front of its sentence and replaced 'widens in step with' by 'the width of the slice grows in proportion to'; same claim (the gap is proportional to horizontal distance from the axis). Entry explanations rise to 1,093 words by the validator's count, inside the 1,100 review allowance.
- Fix: Working, gap-law conditions: 'along the curve at fixed distance s' became 'along the curve that stays a fixed distance s', matching the parallel-postulate note; claim unchanged.
- Fix: Working, swim-ring worked example: 'on each of these circles' reads cleanly, since 'these circles' names the inner and outer circles of the previous sentence; no change.

**Re-read** (2026-09-13, revision 7): 2 stumbles in 4 changed passages

- “Geodesics leaving a common geodesic at right angles, so $D'(0) = 0$.”: The item's symbol list defines $D$, $s$ and $K$, and the equation itself is written as $d^2D/ds^2$, so the prime arrives undefined. I had to stop and decide two things at once: that $D'$ means $dD/ds$, and that the $0$ in $D'(0)$ is the value of $s$, not of $D$. That second reading matters, because $D(0)$ is not zero while $D'(0)$ is. The prime is used again in the swim-ring worked example, and this item, where the symbols are defined, is where it should be pinned down.
- “The strip of surface between the two geodesics must be smooth, with no cone tips, single points where curvature is concentrated.”: Reread. The clause already carries a 'no', so 'no cone tips, single points where curvature is concentrated' reads first as two excluded things rather than as a phrase defining the first. The definition is the useful part of the sentence, and it should not have to be recovered on a second pass.
- Fix: Working, gap-law conditions, first sentence: kept the hypothesis and $D'(0) = 0$ exactly as the physics review set them, and appended the notation the sentence assumed, 'with $D' = dD/ds$ and $s = 0$ at the common geodesic'. No change to the hypothesis, the scope or the initial condition; $s = 0$ at the common geodesic is already what the symbol entry for $s$ ('distance run along each geodesic') implies.
- Fix: Working, gap-law conditions, smoothness sentence: split the appositive into its own sentence, 'with no cone tip anywhere in that strip. A cone tip is a single point where curvature is concentrated.' The requirement and the definition of a cone tip are unchanged; only the punctuation that made them read as two requirements is gone.
- Fix: No way asks the reader to hold two new ideas at once (rule 17) in this diff: the single changed string is a working-rung conditions field, and no entry-rung text changed. Nothing was squeezed to fit a budget; the equations part sits at 600 words against a 1,500 cap, so both fixes were made by adding words rather than by compressing anything.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Novice rewrite, entry way and check: 'a ring-shaped cake, sliced from above by knife cuts through the centre of its hole, the way a round cake is sliced', replacing 'by knife cuts straight down through the centre of its hole'.: Checked what the picture must deliver: each cut has to be a plane containing the ring's axis, because only such a plane reflects the torus onto itself and makes the meridian loop a geodesic. Asked whether 'from above ... through the centre of its hole, the way a round cake is sliced' still forces that plane, and whether any tilted plane through the hole's centre survives the next sentence. → Accurate. The next sentence, unchanged, states the operative condition ('Each cut is a mirror that splits the ring into matching sides'), and only an axis-containing vertical plane does that, so a tilted cut is excluded by the text itself. The rewrite drops no hypothesis; it removes the word 'straight' from a second sense, which the glossary reserves for walking straight.
- Novice rewrite, summary: '..., as around a swim ring's hole, the surface has negative curvature' (was 'it has negative curvature').: Compared the two sentences for scope: subject replaced by its noun; the condition (walkers that begin to spread apart) and the claim (negative curvature) are unchanged. → Accurate. No claim, number or scope changed. The trichotomy in the three summary sentences remains pointwise and uses "begin to", so the swim ring, where a pair that starts on the outer circle later crosses into the negatively curved half, is still described correctly.
- Novice rewrite, tagline: 'How straight walkers that start parallel reveal curvature: positive, negative or zero'.: Checked the trichotomy: at a point of a smooth surface the Gaussian curvature is a real number, so positive, negative and zero exhaust the cases; in higher dimensions the walker test reads the sectional curvature of the plane the walkers span, again one real number. Checked that dropping "a surface's" does not overclaim, since the note also applies the test to spacetime. → Accurate and exhaustive; 12 words, matching the tagline length rule.
- Novice rewrite, opening question: 'A swim ring lies on a table. Two tiny ants stand side by side on the circle around its hole, halfway up the tube, facing over the top of the tube.': Checked the setting against the geometry: with the ring lying on a table, 'halfway up the tube' is the mid-height circle, which is the inner equator of the torus, a geodesic; the ants face along the meridian. Recomputed the expected answer from D(s) = dphi (R - r cos(s/r)) with R = 25 cm, r = 10 cm: D''(0)/D(0) = +1/[r(R - r)]. → Accurate. D''/D = +6.667e-3 cm^-2, so the ants spread apart and K = -1/150 cm^-2, the answer the check and the entry way give. Splitting the setting into its own sentence changed no condition.
- Gap law $d^2D/ds^2 = -KD$ and its hypotheses, including the cone-tip hypothesis that the justifying prerequisite states.: Re-derived in geodesic parallel coordinates about the common geodesic, $ds^2 + G\,du^2$ with $G(0,u) = 1$, $(\sqrt G)_s(0,u) = 0$ and $(\sqrt G)_{ss} = -K\sqrt G$; the gap at fixed $s$ is $\int\sqrt G\,du$. Checked constant $K$ (sphere, plane, hyperbolic) numerically with finite differences of $D_0\cos(s/a)$ at $s = 0.3, 1.0, 1.4$ and of $D_0\cosh(s/a)$. Tried the paper cone against the law as stated. → Law and sign correct; $D''/D = -1/a^2$ and $+1/a^2$ to 6 digits. The constant-$K$ statement is exact wherever the curve at fixed distance $s$ exists (on a sphere, up to $s = \pi a/2$, where it degenerates to the pole), so no bound on $s$ is needed. The cone was the one real gap: away from the tip $K = 0$, yet walkers whose paths pass on opposite sides of the tip draw together, because the curvature sits in the tip. Fixed by adding the smoothness and cone-tip hypothesis, the same hypothesis the prerequisite note states for this equation.
- Swim-ring geometry and numbers: a ring 70 cm across with a 30 cm hole has outer and inner circles 35 cm and 15 cm from the centre; ants 3 mm apart on the inner circle are 7 mm apart at the outer circle; the worked example gives $K = +1/350$ and $-1/150$ cm$^{-2}$ and radii of curvature 18.7 cm and 12.2 cm.: python3: $R = 25$ cm, $r = 10$ cm; $3 \times 35/15$; finite-difference $D''(0)/D(0)$ for $D = \Delta\phi(R \pm r\cos(s/r))$ on both circles; compared with the torus formula $K = \cos v/[r(R + r\cos v)]$; $\sqrt{350}$ and $\sqrt{150}$. → 7.0 mm exactly (the gap is measured along the circle about the axis, which is what 'seen from above' names); $D''/D = -2.85715\times10^{-3}$ and $+6.66667\times10^{-3}$ cm$^{-2}$, so $K = +2.857\times10^{-3}$ and $-6.667\times10^{-3}$ cm$^{-2}$; radii 18.708 cm and 12.247 cm. All as quoted.
- Short-walk numbers: football 70 cm around, walkers meet after 17.5 cm; Earth 40,000 km around, walkers meet after 10,000 km; friends 100 m apart after 5 km lose about three hundredths of a millimetre, against 5 cm at an even rate; ships 10 km apart over 100 km lose about 1.2 m.: python3 with $D = D_0\cos(s/a)$, $a = 6371$ km and $a = 40{,}000$ km$/2\pi$; quarter circumferences; $5/10{,}000$ of 100 m. → 0.0308 mm both ways; 5.0 cm at an even rate; 1.232 m for the ships; quarter circumferences 17.5 cm and 10,008 km (quoted as about 10,000 km). Meridians from a common great circle meet at the pole after a quarter turn for any starting gap, so the "meet" claims hold for every ball size and every gap.
- Tidal numbers: $GM/r^3 = 1.54\times10^{-6}$ s$^{-2}$ at Earth's surface; stones 1 m apart dropped 100 m end $1.6\times10^{-5}$ m closer, about a sixtieth of a millimetre; the rocket-and-tower check grows by $6.28\times10^{-5}$ m with the rocket at zero.: python3 with $GM = 3.986\times10^{14}$ m$^3$s$^{-2}$, $R = 6371$ km, $t = \sqrt{2h/g} = 4.52$ s; transverse $\tfrac12(GM/R^3)\xi t^2 = \xi h/R$, radial $2\xi h/R$; checked the rocket case in the inertial frame, where both balls are released at rest and stay inertial. → $GM/R^3 = 1.541\times10^{-6}$ s$^{-2}$ ($g/R = 1.539\times10^{-6}$); $1.573\times10^{-5}$ m $= 1/63.6$ mm; $6.278\times10^{-5}$ m. The rocket separation is exactly constant, since the two balls share one inertial velocity, so the value 0 with an absolute tolerance is right. Tolerances of 5% and $10^{-6}$ m are appropriate.
- Newtonian tidal derivation: transverse $-(GM/r^3)\xi_\perp$, radial $+(2GM/r^3)\xi_\parallel$, and the directions claimed in each step.: Re-derived by hand: two lines to the centre meet at angle $\xi_\perp/r$, each acceleration contributing $g\xi_\perp/2r$ toward the other; $g(r) - g(r + \xi_\parallel) = 2GM\xi_\parallel/r^3$ to first order, with the lower body pulled harder. → Every step and both signs correct to first order in $\xi/r$; consistent with the course geodesic-deviation sign and with the Schwarzschild orthonormal components $R^{\hat x}{}_{\hat t\hat x\hat t} = M/r^3$ and $R^{\hat r}{}_{\hat t\hat r\hat t} = -2M/r^3$.
- Ring length $C = 2\pi\rho(1 - K\rho^2/6 + \dots)$, the triangle excess $\pi + KA$, the sphere ring $2\pi a\sin(\rho/a)$, Earth $K = 2.46\times10^{-14}$ m$^{-2}$ and an excess of $2.5\times10^{-4}$ rad over 10,000 km$^2$.: python3: compared $2\pi a\sin(\rho/a)$ and $2\pi a\sinh(\rho/a)$ with the expansion at $\rho = 0.05a$ and $0.2a$; $K = 1/(6371\ \mathrm{km})^2$ times $10^{10}$ m$^2$. → Expansion agrees to the order shown in both signs; $K = 2.4637\times10^{-14}$ m$^{-2}$ and excess $2.464\times10^{-4}$ rad. Sphere positive, saddle negative, as the course conventions require.
- Rindler way: $ds^2 = -(1 + gx/c^2)^2c^2dt^2 + dx^2 + dy^2 + dz^2$ is flat, and $cT = (c^2/g + x)\sinh(gt/c)$, $X = (c^2/g + x)\cosh(gt/c)$ returns the constant form with the floor at $x = 0$ having proper acceleration $g$.: Hand algebra for $-c^2dT^2 + dX^2 = dx^2 - (1 + gx/c^2)^2c^2dt^2$, plus python3 evaluation of the numerical $g_{tt}$ at $x = 0$, 12 m and $10^6$ m; the floor traces the hyperbola of radius $c^2/g$, whose proper acceleration is $c^2/(c^2/g) = g$. → Numerical and closed forms agree to 15 digits; proper acceleration 9.80 m s$^{-2}$. The way's claim that weight and falling appear with no curvature is correct.
- Formal counting: $\Gamma(p) = 0$ is attainable, and at least $n^2(n^2-1)/12$ second-derivative combinations survive; the three-dimensional check gives $36 - 30 = 6$ and $18 = 18$.: Hand algebra $n^2(n+1)^2/4 - n^2(n+1)(n+2)/6 = n^2(n^2-1)/12$, python3 for $n = 2, 3, 4$ and for the counts in three dimensions. → 1, 6 and 20 for $n = 2, 3, 4$; the check's 36, 30, 6, 18 and 18 all correct, and 6 matches the independent Riemann components in three dimensions.
- Flatness criterion and its proof sketch, the Jacobi equation $f'' + Kf = 0$ with $R_{1212} = K\det g$, and the Sturm comparison bound $s = \pi/(2\sqrt k)$.: Checked $R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$ against the course $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$; the parallel coframe argument $d\theta^a = -\omega^a{}_b\wedge\theta^b = 0$ with vanishing torsion, then the Poincare lemma; comparison of $f$ with $\cos(\sqrt k s)$ for $K \ge k > 0$ and convexity for $K \le 0$. → All correct, with simple connectedness stated where it is needed. The sphere gives $K = +1/a^2$ from $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$ over $\det g = a^4\sin^2\theta$, matching the conventions.
- Timelike sectional curvature: converging free-fall neighbours give $K(u, e_{\hat x}) = -M/r^3 < 0$, opposite in sign to the sphere though the behaviour matches.: Numerator $R_{\hat t\hat x\hat t\hat x} = R_{\hat x\hat t\hat x\hat t} = g_{\hat x\hat x}R^{\hat x}{}_{\hat t\hat x\hat t} = M/r^3$ by pair symmetry; denominator $g(u,u)g(e,e) - g(u,e)^2 = -1$ in signature $(-,+,+,+)$; cross-checked that convergence needs $R^{\hat x}{}_{\hat t\hat x\hat t} > 0$ in the course geodesic-deviation equation, and that the diverging radial pair gives $K = +2M/r^3$. → Correct, and consistent with the conventions row, the notation trap and the misconception it diagnoses. The sign does not depend on which falling observer supplies $u$.
- Problems: which-surface-is-flat gives $C = 2\pi a\sinh(\rho/a)$, $K = -1/a^2$ and ratio $\sinh 1 = 1.1752$; zero-curvature-is-locally-flat gives $h = r$ and a compactness obstruction for the flat torus.: python3 for $\sinh 1$; matched the series $2\pi\rho(1 + \rho^2/6a^2)$ against $2\pi\rho(1 - K\rho^2/6)$; solved $\partial_r^2h = 0$ with $h(0,\phi) = 0$, $\partial_rh(0,\phi) = 1$ by hand. → 1.175201; $K = -1/a^2$; $h = r$ and $dr^2 + r^2d\phi^2 = dx^2 + dy^2$. The torus argument is right: an isometry is a homeomorphism, and a compact space cannot be homeomorphic to the plane. Tolerance of 1% fine.
- Observation: GOCE accelerometer pairs 0.5 m apart, 2009 to 2013, dominant radial gradient about $2.7\times10^{-6}$ s$^{-2}$ equal to $2GM/r^3$ at the orbit.: python3 $2GM/r^3$ for altitudes 224 km and 255 km. → $2.74\times10^{-6}$ to $2.78\times10^{-6}$ s$^{-2}$, about 2700 Eotvos, matching the quoted value over the mission's altitude range.
- Reference: Rummel, Yi, Stummer (2011), GOCE gravitational gradiometry, Journal of Geodesy 85, 777-790, doi 10.1007/s00190-011-0500-0.: WebSearch; publisher article record. → Confirmed, authors, year, title, volume, pages and doi; verified stays true.
- Reference: Gauss (1828), Disquisitiones generales circa superficies curvas, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99-146, presented 8 October 1827.: WebSearch; bibliographic records and digitised copies. → Confirmed, including the 1827 presentation date the history entry uses as its year; verified stays true. The contribution stays scoped to the single curvature number and its intrinsic character, since curvature of surfaces through normal sections predates him.
- Reference: Riemann (1868), Ueber die Hypothesen, welche der Geometrie zu Grunde liegen, Abhandlungen der Koeniglichen Gesellschaft der Wissenschaften zu Goettingen 13, 133-150, lecture 10 June 1854.: WebSearch; bibliographic records of volume 13. → Confirmed with the 133-150 page range and the 1854 lecture; the volume is sometimes dated 1867, which does not affect the claim. Verified stays true.
- Structure: prerequisites direct and acyclic, assumes at or below each way's rung, formal rung present with two formal checks and one formal problem, every check and problem evidencing an objective.: python3 over the concept registries: transitive closure of parallel-postulate, geodesic and flat-metric (106 concepts) does not contain curvature; matched each way's assumes against the prerequisites' needed_for; counted formal items; validator run. → Correct for a foundation note: entry way assumes only parallel-postulate (entry), working and formal ways assume geodesic and flat-metric (working). Two formal checks, one formal problem, two problems spanning working and formal, one measured observation.

**Counterexamples tried**

- Paper cone: tiny walkers whose paths pass on opposite sides of the tip draw together although the paper unrolls flat, because the curvature sits in the tip. The gap law as written invited exactly this misuse, so its conditions now exclude cone tips, as the prerequisite note does. The entry and glossary uses of 'flat' stay pointwise and remain true.
- Top and bottom circles of the swim ring, where $K = 0$: those circles are not geodesics, so walkers cannot start parallel along them; pairs that start parallel on a meridian there keep their gap only to second order. The note claims positive curvature on the outer part and negative around the hole, and never assigns a sign to these circles, so nothing needed rescoping.
- Walkers who start on the outer circle keep drawing together after crossing into the negatively curved half: every sign sentence says 'begin to' or names where the walkers start, including the novice reviewer's rewritten tagline and summary.
- Region bigger than half a closed surface, and walkers past their meeting point: on a sphere the gap $D_0\cos(s/a)$ is exact only up to the pole, where the curve at fixed distance degenerates; the entry text stops at the meeting point and the working text keeps the first-order scope.
- Flat cylinder (a bent but flat surface) and the flat torus: both have $R = 0$ and neither is isometric to the Euclidean plane; the formal way states that the criterion is local and names both.
- Surface with $K = 0$ along one geodesic only, such as $z = x^2y^2$ along the $x$-axis: walkers keep their gap to first order although no neighbourhood is flat. The summary's 'where they keep their gap, the surface is flat' is a pointwise entry statement; acceptable, and unchanged by this pass.
- Polar coordinates on the plane (varying coefficients, spreading spokes) and the Rindler rocket (weight and falling in flat spacetime): both are handled explicitly as non-curvature cases, at the working rung and in two checks.
- Different observer and different slicing: the sign of the timelike sectional curvature is the same for every freely falling observer whose four-velocity spans the plane with a transverse direction; the diverging radial pair gives $K = +2M/r^3$, which the note does not claim otherwise.
- Non-relativistic limit and a massless case: the tidal formulas are quoted as the Newtonian limit near a static spherical mass, and the simplifies field states it; no claim is made about null separations.

**Fixes**

- Gap-law conditions: added that the geodesics start parallel ($D'(0) = 0$) and that the strip between them must be smooth, with no cone tips, points where curvature is concentrated. Without it a reader could apply $K = 0$ across a cone tip and conclude that walkers keep their gap. The hypotheses now agree with the prerequisite note that justifies the equation, so the tutor retrieves one set of conditions.
- Checked the five strings the novice review rewrote (tagline, summary, the entry way's cake sentence, the hole-side-is-not-flat answer, the opening question); all are accurate and none changes a claim, a number or a scope, so none was altered.
- Re-verified the three references; all confirmed, verified stays true.
- Bumped the revision to 6. Entry-rung words are unchanged at 1,093; the added conditions sit in the equations part, which stays far below its cap.

**Concerns**

- One learner-visible string changed, at the working rung (the gap-law conditions); the entry rung is untouched, so the novice re-read has only that sentence to cover.
- Entry way explanations remain 1,093 words against the 1,000 foundation cap, inside the 10% review allowance. Nothing may be added at the entry rung without dropping something first.
- Registry and note still diverge: the registry titles the concept 'Curvature as departure from flatness' and carries the aliases 'non-Euclidean geometry', 'sign of curvature' and 'positive and negative curvature', which the note does not; the note's aliases 'curved space' and 'curved spacetime' name things that have curvature rather than synonyms of it. An editor's call, not an accuracy fault.
- Glossary headword mismatch with the prerequisite persists: parallel-postulate.json heads the entry 'straight line' with 'walk straight' among its forms, and this note does the reverse. The definitions agree, so the tutor will retrieve two headwords for one idea.
- Both visuals are still proposals with sketches, so the entry rung carries the swim-ring argument in prose alone; the flagship 'two-walkers-set-off-side-by-side' needs the swim ring added to its scene before it can carry the sign of curvature.
- The note has no research_horizon entries, which a foundation tier does not require; if it is ever promoted, the horizon and a review reference would have to be written.

**Diff check** (2026-09-13, revision 4)

- Entry, draw-together-or-spread: 'Seen from above, the width of the slice grows in proportion to the distance from the centre of the hole.': Torus with horizontal radius rho = R + r cos(theta); two meridian cuts at angle dphi are a gap rho*dphi apart along the parallel. That gap is horizontal, so its top view has the same length, and rho is the top-view distance from the centre of the hole. Recomputed 3 mm x 35/15 in python3. Compared with the old wording 'widens in step with ..., seen from above'. → True and exactly proportional; 'seen from above' now also fixes which distance from the centre is meant, which is the horizontal one the physics fix required. Outer gap 7.0 mm matches the next sentence. Same claim as before, stated more precisely. No change.
- Working, gap-law conditions: 'Exact for constant K when D is measured along the curve that stays a fixed distance s from the common geodesic; where K varies, valid to first order in the gap.': Geodesic parallel coordinates ds^2 + G(s) du^2 for constant K: sqrt(G)'' = -K sqrt(G), so the length along s = const between two orthogonal geodesics is sqrt(G(s)) du exactly for any du; checked d2D/ds2 = -K D numerically on the unit sphere at s = 0.3, 1.0, 1.4. Tried K < 0 (hypercycles, cosh) and the sphere past s = pi/2. Compared with the old wording and with the parallel-postulate note. → True in the same scope as the old sentence (exact up to the first focal point for K > 0, everywhere for K <= 0); only the phrase naming the curve changed, and it now matches the parallel-postulate note word for word. No change.

**Diff check** (2026-09-13, revision 7)

- Working, gap-law conditions, added notation: "Geodesics leaving a common geodesic at right angles, so $D'(0) = 0$, with $D' = dD/ds$ and $s = 0$ at the common geodesic.": Checked that the appended clause only names what the item already assumed, and that both halves of it are forced by the hypothesis. Re-derived in geodesic parallel coordinates about the common geodesic $\gamma$: $ds^2 = dv^2 + G(v,u)^2du^2$ with $u$ arclength along $\gamma$ and $v$ arclength along the orthogonal geodesics, so the item's $s$ is $v$ and $s = 0$ is exactly the locus $\gamma$; $D(s) = D(0)\,G(s,u)$ to first order in the gap, so the prime can only be $d/ds$, the derivative the equation $d^2D/ds^2 = -KD$ itself takes. Checked $D'(0) = 0$ by the symmetry lemma: $\nabla_s J|_{s=0} = \nabla_u N$ along $\gamma$, and $\langle\nabla_uN, N\rangle = 0$ while $\langle\nabla_uN, T\rangle = -\langle N, \nabla_uT\rangle = 0$ because $\gamma$ is a geodesic, so the initial condition needs $\gamma$ geodesic, which the hypothesis states. Confirmed numerically in python3 with central differences ($h = 10^{-4}$): sphere of radius 2, $D = D_0\cos(s/a)$, and the hyperbolic case $D = D_0\cosh(s/a)$; also both branches of the swim-ring worked example, $D(s) = \Delta\phi(R \pm r\cos(s/r))$, which is where the prime is used again. Compared the wording with the justifying prerequisite parallel-postulate, whose gap-equation carries the same hypothesis and the same prime. → Accurate, and no claim moved. $D'(0) = 0.000\times10^0$ and $D(0) \ne 0$ in every case (sphere $D(0) = 0.01$; torus $D(0) = 35$ cm on the outer circle and $15$ cm on the inner), so the reading the clause pins down, that the $0$ is the value of $s$ and not of $D$, is the right one. $D'' = -KD$ to nine digits at $s = 0, 0.3, 1.0, 1.4$ for $K = +1/a^2$ and at $s = 0, 0.3, 1.0$ for $K = -1/a^2$. The hypothesis, the scope and the initial condition are character-for-character what the physics review set; only notation the item had left implicit was added. No change.
- Working, gap-law conditions, split sentence: "The strip of surface between the two geodesics must be smooth, with no cone tip anywhere in that strip. A cone tip is a single point where curvature is concentrated.": Compared the two sentences with the single appositive sentence they replace, clause by clause, for any change of quantifier, scope or modality. Re-ran the cone counterexample this condition was written for: a paper cone unrolls flat, so $K = 0$ at every point away from the tip, yet two geodesics passing on opposite sides of the tip draw together, because the total curvature $2\pi - \alpha$ of the cone sits at the tip; checked that the new wording still excludes exactly that case and nothing more, by testing a cone tip lying outside the strip, where the law must and does still apply. Checked the definition sentence against the standard angle-defect statement (concentrated Gaussian curvature $2\pi - \alpha$ at the tip) and against the wording of the same hypothesis in the prerequisite parallel-postulate. Checked that the smoothness requirement and the cone-tip requirement are not now readable as two independent restrictions on different regions, since both name 'that strip'. → Accurate, and the claim is unchanged. 'No cone tips' and 'no cone tip anywhere in that strip' exclude the same surfaces, and the definition, now a sentence of its own, states what the appositive stated. Nothing was strengthened: the split adds no assertion that the law fails across a cone tip, only that a cone tip in the strip is outside the hypothesis. The re-read did not touch the smoothness requirement, the strip, or the region it names. No change.
- Both changed sentences against the rest of the note and the swim-ring worked example, which is the only other place the prime appears.: Reworked the worked example end to end in course conventions with the newly pinned notation. Outer circle: $D(s) = \Delta\phi(R + r\cos(s/r))$ with $s = 0$ on that circle, $R = 25$ cm, $r = 10$ cm. Inner circle: $D(s) = \Delta\phi(R - r\cos(s/r))$ with $s = 0$ there. Computed $D'(0)$, $D''(0)/D(0)$, $K$ and $|K|^{-1/2}$ in python3, and cross-checked against the closed form for a torus, $K = \cos\theta/[r(R + r\cos\theta)]$ with $\theta$ from the outer equator. Checked that both circles are geodesics, so the hypothesis 'a common geodesic' holds at both ends of the example, and that the torus is smooth, so the cone-tip sentence excludes nothing the example needs. → Consistent. $D'(0) = 0$ on both circles; $D''(0)/D(0) = -2.857153\times10^{-3}$ and $+6.666667\times10^{-3}$ cm$^{-2}$, so $K = +1/350 = 2.857\times10^{-3}$ cm$^{-2}$ and $K = -1/150 = -6.667\times10^{-3}$ cm$^{-2}$, matching the closed form and the quoted answer; $\sqrt{350} = 18.708$ cm and $\sqrt{150} = 12.247$ cm, matching 18.7 cm and 12.2 cm. The example now reads with the prime defined where the symbols are pinned down.
- Scope of the diff: no equation, number, reference, tolerance or numeric field changed.: note_diff.py over the re-read snapshot and the current note at rungs entry and working, then a full text diff of the two files to confirm that nothing outside $.key_equations[gap-law].conditions and the internal review record differs. → Confirmed. One learner-visible string changed, at the working rung. No latex, no numeric answer, no tolerance and no reference was touched, so nothing needed re-derivation or verification beyond the two sentences above and the worked example that uses their notation.
- Fix: None. Both re-read edits are accurate, and neither altered a claim, a number, a condition, a scope, a sign or a sense, so no learner-visible text was changed by this diff check and the revision stays at 7.
