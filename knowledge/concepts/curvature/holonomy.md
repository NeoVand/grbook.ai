---
type: "concept"
schema_version: 2
id: "holonomy"
title: "Holonomy"
tagline: "How an arrow carried around a loop can come back turned"
domain: "curvature"
tier: "core"
status: "draft"
revision: 2
updated: "2026-09-13"
aliases: ["holonomy of parallel transport", "loop holonomy"]
prerequisites: ["path-dependence-of-parallel-transport", "gaussian-curvature", "angular-excess", "riemann-curvature-tensor", "levi-civita-connection", "lie-bracket"]
leads_to: ["flatness-criterion", "riemann-curvature-operator", "bianchi-identity", "gauge-field-strength", "cosmic-string", "geodetic-precession"]
visuals: ["carry-an-arrow-around-a-loop", "shrink-the-loop-to-find-riemann", "paper-cone-with-a-missing-wedge", "arrow-around-a-circle-of-latitude", "cube-of-small-loops"]
---

# Holonomy

*How an arrow carried around a loop can come back turned*

`holonomy` · curvature · core · draft (revision 2)

**Needs:** [[path-dependence-of-parallel-transport]] (entry) · [[gaussian-curvature]] (working) · [[angular-excess]] (working) · [[riemann-curvature-tensor]] (working) · [[levi-civita-connection]] (formal) · [[lie-bracket]] (formal)  
**Opens:** [[flatness-criterion]] · [[riemann-curvature-operator]] · [[bianchi-identity]] · [[gauge-field-strength]] · [[cosmic-string]] · [[geodetic-precession]]  
**Related:** [[parallel-transport]] · [[intrinsic-versus-extrinsic-curvature]] · [[curvature-of-the-two-sphere]] · [[gauge-parallel-transport]] · [[loop-quantum-gravity]]  
**Visuals:** ★ [[carry-an-arrow-around-a-loop]] · [[shrink-the-loop-to-find-riemann]] · [[paper-cone-with-a-missing-wedge]] · [[arrow-around-a-circle-of-latitude]] · [[cube-of-small-loops]]

> Carry an arrow around a loop without ever letting it swing left or right, then compare it with the way it pointed at the start. On a flat table it always comes back pointing the same way. On a ball, most loops bring it back pointing a new way. That turn is the loop's holonomy, and it lets someone who lives on a surface discover that the surface is curved without ever leaving it.

## You will be able to

**Entry**
- Explain how carrying an arrow around a loop, never letting it swing, shows that a ball is curved while a flat table and a paper tube are not. `objectives/explain-the-arrow-test` ← `checks/octant-walk-prediction`, `checks/square-on-a-floor`, `checks/loop-around-a-tube`, `problems/equator-walk`
- Predict how the returned turn changes when the same loop is walked the other way. `objectives/predict-reversal` ← `checks/reverse-the-loop`

**Working**
- Compute the turn for loops on a sphere or a saddle from the enclosed area, the angle excess, or the latitude. `objectives/compute-turn-from-area` ← `checks/triangle-on-a-big-sphere`, `checks/latitude-30-north`, `problems/earth-loop-size`, `problems/saddle-sign`
- Explain why the turn is defined only when the loop closes. `objectives/explain-when-turn-is-defined` ← `checks/halfway-readout`
- Use the small-loop law to find how a vector changes around a small cell, with the correct sign. `objectives/use-small-loop-law` ← `problems/small-loop-cell-other-vector`, `checks/polar-coordinates-plane`

**Formal**
- Distinguish restricted from full holonomy, and state when zero curvature guarantees trivial holonomy. `objectives/distinguish-curvature-and-holonomy` ← `checks/cone-holonomy-group`
- Explain when the path ordering in the holonomy can be dropped. `objectives/explain-path-ordering` ← `checks/why-ordering-matters`
- Prove that the holonomy of a small loop is an infinitesimal rotation or boost. `objectives/prove-small-loop-generator-antisymmetric` ← `problems/small-loop-change-is-a-rotation`
- Compute a finite holonomy from the transport equation as a matrix exponential. `objectives/compute-holonomy-by-path-ordering` ← `problems/latitude-holonomy-from-path-ordering`

## Ways in

### 1. Walk a loop on a ball · entry · picture

*How can someone who never leaves a ball find out that it is curved?*

**Recap:** A loop is like going out to a place by one route and coming home by another. Carrying an arrow without letting it swing can bring it to the same place pointing different ways, depending on the route.

Imagine a huge, smooth ball with no hills, and imagine you live on its surface. You can never leave the surface or look at the ball from above. Can you still find out that your world is curved?

Here is a test. Take a cardboard arrow and press it against the ground. Then walk along a path that ends exactly where it began. Such a path is called a loop.

As you walk, follow one rule. Keep the arrow pressed against the ground, and never let it swing to the left or to the right. Walking straight means never steering left or right. On a straight stretch, the rule means the arrow keeps the same angle to your path the whole way. At a corner, you turn your body, but you leave the arrow alone. So after a corner, the arrow makes a new angle with your new path.

First, try it on a flat table. Walk a triangle, a square, or any loop you like. Because the arrow never swings, it keeps pointing at the same wall of the room the whole time. So it comes back pointing exactly the way it started.

Now try it on the ball. Seen from outside, as on a globe, mark the top point and call it the North Pole. The equator is the circle around the middle, halfway between the North Pole and the bottom point. On a globe, the lines from top to bottom are straight walks, and so is the equator. A small circle around the North Pole is not, because you would have to keep steering to stay on it.

Start at the North Pole with the arrow pointing straight ahead of you. Walk straight until you reach the equator, which you meet at a right angle. The arrow is pointing straight ahead when you arrive. Turn left by a quarter turn, so that you walk along the equator. The arrow did not swing, so now it points to your right. Walk a quarter of the way around the equator, with the arrow pointing to your right the whole way. Then turn left by a quarter turn again, and walk straight back to the North Pole. The arrow did not swing at this corner either, so now it points straight behind you.

Back at the North Pole, compare. When you set off, the arrow pointed along your first path. Now it points back along your last path. How far apart are those two directions? Your first path met the equator at one point. Your last path left the equator a quarter of the way around from that point. A quarter of a full circle is a right angle, so the two paths leave the North Pole at a right angle. Seen from above the North Pole, they meet like the corner of a book. So, seen from above, the arrow's new direction is a quarter turn counterclockwise from its old one, even though it never swung. That is the same way you went around the loop.

This turn is called the holonomy of the loop. A flat table never produces one. So the ball cannot be flat like a table, and you learned that without ever leaving the surface.

A few more facts are worth knowing. On a surface like this, one trip around a loop turns every arrow by the same amount, whichever way it pointed at the start. Walk the same loop the other way, turning right at each corner, and the arrow comes back turned the other way. That has to happen, because the backwards trip undoes the forwards trip. For loops that fence off less than a quarter of the ball, a bigger patch gives a bigger turn, up to a half turn. So the turn is set by the patch your loop fences off. On Earth, a loop around an area of 10,000 square kilometres, about the size of a small country, gives a turn of only about one seventieth of a degree. That is why nobody notices it in daily life.

**Try it:** Stretch two rubber bands around an orange so that they cross at the top at a right angle, and a third band around its middle. All three are straight walks. Lay a matchstick at the top along one band and mark its direction. Slide the matchstick along the loop, keeping the same angle to the band you are on, and leave it alone at each corner. Back at the top, it lies along the other band, a quarter turn from your mark.

**Takeaway:** An arrow carried around a loop without swinging never comes back turned on a flat table, but on a ball most loops bring it back turned.

*What this leaves out:* We used a smooth ball. A loop that splits the ball into two equal halves, like the equator, brings the arrow back matching its start. That does not make the ball flat, because the North Pole walk still gives a turn. A surface with a sharp tip is different: a paper cone is flat everywhere except at its tip, yet a loop around the tip brings the arrow back turned.

*Builds on:* [[path-dependence-of-parallel-transport]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `octant`, tour `holonomy-first-walk`)

### 2. Bent is not the same as curved · entry · contrast

*Does a rolled-up paper tube count as curved for the arrow test?*

**Recap:** The arrow test: press a cardboard arrow against the ground and walk a loop, a path that ends where it began, never letting the arrow swing left or right. Back at the start, compare its direction with its starting direction. On a flat table it always matches; on a ball, most loops bring it back turned.

Roll a sheet of paper into a tube. From outside, the tube looks curved. Now do the arrow test on the tube.

Walk any loop on the tube, never letting the arrow swing. The arrow comes back pointing exactly the way it started. Even a loop that wraps once around the tube, like a bracelet around a wrist, brings the arrow back unchanged.

Why? Unroll the tube. It becomes a flat sheet again, and nothing was stretched or squashed. So every angle drawn on the paper is the same on the tube and on the sheet. The arrow rule is a rule about angles along the ground, so an arrow that never swings on the tube also never swings on the sheet. On a flat sheet, such an arrow points the same way everywhere. The bracelet loop becomes a straight line from one edge of the sheet to the opposite edge, and those two edges were glued together in the tube. The arrow points the same way at both ends of that line. So when you roll the paper up again, the arrow comes back matching its start.

A ball is different. You cannot flatten a piece of orange peel without tearing or stretching it. Curving that cannot be flattened away is built into the surface itself. Someone living on the surface can detect it without looking from outside. This is called intrinsic curvature. Rolling a flat sheet into a tube does not create any.

**Try it:** Draw a small loop and an arrow on a sheet of paper, then roll the sheet into a tube. Look closely: every angle in the drawing is unchanged, because the paper did not stretch.

**Takeaway:** The arrow test cannot tell a flat sheet from a rolled-up one; it only notices curving that cannot be unrolled flat, like a ball's.

*What this leaves out:* This contrast is about surfaces. Nobody can step outside the universe to look at it. So the curving of space and time we can find is the built-in kind, which the arrow test detects. A surface inside space, like the surface of a star, can also be bent, and that other kind of bending comes up in other topics.

*Continues:* `ways_in/walk-a-loop-on-a-ball`<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `tube-unrolled`)

### 3. The turn equals the curving fenced off · working · calculation

*How big is the turn, and what decides it?*

In the walk from the North Pole, the loop fenced off one eighth of the ball's surface, and the arrow came back turned by a quarter turn, $\pi/2$ radians. The two numbers are linked. For a simple loop on a sphere of radius $a$, the turn in radians equals the area of the region on the walker's left divided by $a^2$:

$$\Delta\alpha = \frac{A}{a^2} \pmod{2\pi}.$$

Check it: the whole sphere has area $4\pi a^2$, one eighth of it is $\pi a^2/2$, and dividing by $a^2$ gives $\pi/2$. A positive turn rotates the arrow toward the walker's left, which is counterclockwise seen from outside the sphere. Walk the same triangle the other way and the region on your left is the other seven eighths, $7\pi a^2/2$. That gives $7\pi/2 \equiv -\pi/2$: a quarter turn to the right, as it should be. The equator fences off $2\pi a^2$, so its turn is $2\pi$, which is why the arrow comes back matching.

On a general surface the curving varies from place to place. Its strength at each point is the Gaussian curvature $K$: $1/a^2$ everywhere on a sphere, $0$ on a plane or a cylinder, and negative on a saddle. For a simple loop bounding a smooth region $S$ on the walker's left,

$$\Delta\alpha = \iint_S K\,dA \pmod{2\pi}.$$

This is the local Gauss–Bonnet theorem. It holds for loops of any size, and the sides need not be geodesics. Around a small loop where $K<0$, the arrow comes back rotated toward the walker's right.

Two special cases are worth owning. For a triangle whose sides are geodesics, the straight walks of a surface, the turn equals the angular excess: the amount by which the three angles add up to more than $\pi$. The North Pole triangle has three right angles, so its excess is $3\pi/2 - \pi = \pi/2$. For a circle at colatitude $\theta_0$ walked eastward, which is not a geodesic, the polar cap on the walker's left has area $2\pi a^2(1-\cos\theta_0)$, so the turn is $2\pi(1-\cos\theta_0)$.

**Takeaway:** The turn is the total curvature on the walker's left, so on a sphere it is the enclosed area divided by the radius squared.

*What this leaves out:* In more than two dimensions, rotations about different axes do not commute, so this simple area rule holds only for small loops.

*Continues:* `ways_in/walk-a-loop-on-a-ball`<br>*Builds on:* [[gaussian-curvature]], [[angular-excess]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `octant-half-area`), [[arrow-around-a-circle-of-latitude]]<br>*See:* `checks/latitude-30-north`

### 4. Shrink the loop and the Riemann tensor appears · working · calculation

*What replaces the area rule when a small loop can lie in many different planes?*

On a surface, the turn around a small loop was set by one number, the curvature $K$, because every small loop lies in the same plane. In four-dimensional spacetime a small loop can lie in many different planes, and each plane can give a different result. So shrink the loop to a tiny parallelogram with edge vectors $a^\mu$ and $b^\nu$. Walk $+a$, then $+b$, then $-a$, then $-b$, and ask how a carried vector $V$ changes. To second order in the size of the loop, and with the course sign conventions,

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu,$$

where $R^\rho{}_{\sigma\mu\nu}$ is the Riemann curvature tensor. The derivation "The small-loop law from the transport equation" builds this one move at a time.

Read the formula one feature at a time.

- It is linear in $V$: the loop acts on vectors like a matrix.
- It is linear in each edge: doubling one side doubles the change.
- It is antisymmetric in the edges: swapping $a$ and $b$ walks the same parallelogram the other way round, and the change flips sign.
- It is proportional to the product of the edges: the change scales with the loop's area, as $A/a^2$ did on the sphere.

So the Riemann tensor is a machine. Feed it a small oriented patch, the two edges in order, and it returns a small change of vectors. Because carrying a vector this way preserves lengths and angles, $V_\rho\,\Delta V^\rho = 0$ to this order. The change is a small rotation on a surface, or a small Lorentz transformation, a rotation or a boost, in spacetime. On a two-dimensional surface the machine holds a single number: for a small cell of area $\delta A$ the turn is $K\,\delta A$.

**Takeaway:** The Riemann tensor turns a small oriented patch into a small rotation of vectors; that is what curvature measures.

*What this leaves out:* Keeps only the leading order in the loop's size, for the torsion-free, metric-compatible connection of general relativity.

*Continues:* `ways_in/turn-equals-enclosed-curving`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[shrink-the-loop-to-find-riemann]]<br>*See:* `derivations/small-loop-law-from-transport`, `worked_examples/unit-sphere-cell`

### 5. A gyroscope measures it in orbit · working · operational

*How could you measure this kind of turn in the space around Earth?*

The area rule for a curved surface has a counterpart in the curved space around Earth. To use it you need an arrow that never swings. A spinning gyroscope in free fall is one: nothing twists it, so its spin axis is carried along its path without swinging, which is the spacetime version of the arrow rule. Its direction is compared with distant stars, which serve as the fixed reference.

Put the gyroscope in a circular orbit around a spherical mass $M$, on a circle of circumference $2\pi r$. After each orbit its spin axis comes back turned, within the orbital plane and in the same sense as the orbit, by the standard result, stated here without derivation,

$$\Delta\phi_{\text{orbit}} = 2\pi\left[1 - \sqrt{1 - \frac{3GM}{rc^2}}\right] \approx \frac{3\pi GM}{rc^2}.$$

Part of this is exactly the area-rule turn. Describe the space around a static mass at one moment. That space is curved, and carrying an arrow once around the circle within it gives $2\pi\big[1 - \sqrt{1 - 2GM/rc^2}\big] \approx 2\pi GM/rc^2$, which is two thirds of the total. The remaining third comes from the gyroscope's motion through Earth's gravitational field. The split into two parts depends on describing spacetime as space at successive moments around a static Earth; the total turn does not.

For Gravity Probe B, orbiting about 642 km above Earth, $r \approx 7013$ km. The total is about $1.2$ milliarcseconds per orbit, adding up to about $6.6$ arcseconds per year.

**Takeaway:** A freely falling gyroscope carries its spin axis like the arrow; in orbit, two thirds of its turn is the area-rule turn of the curved space around Earth.

*What this leaves out:* Treats Earth as static and spherical and the orbit as circular; Earth's rotation adds a much smaller frame-dragging turn.

*Continues:* `ways_in/turn-equals-enclosed-curving`<br>*See:* `observations/gravity-probe-b-geodetic`

### 6. Whole loops as transformations · formal · structure

*What is the holonomy of a finite loop, and what kind of transformation can it be?*

The small-loop law came from multiplying four step matrices around a tiny loop. Chop a finite loop $\gamma$ into many short steps and multiply all their matrices in order. The limit is the holonomy of $\gamma$, a linear map $\mathrm{Hol}(\gamma): T_pM \to T_pM$ of the tangent space at the base point $p$. With coordinate connection matrices $(\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}$, for a loop inside one chart,

$$\mathrm{Hol}(\gamma) = \mathcal{P}\exp\Big(-\oint_\gamma \Gamma_\mu\,dx^\mu\Big),$$

where later points of the loop act after earlier ones. Changing the basis at $p$, or moving the base point along the loop, conjugates this matrix and leaves its invariants unchanged.

The Levi-Civita connection satisfies $\nabla g = 0$, so transport preserves inner products and $\mathrm{Hol}(\gamma)$ lies in the orthogonal group $O(g_p)$. On an oriented surface it lies in $SO(2)$ and is a rotation by an angle defined modulo $2\pi$. On an oriented, time-oriented spacetime it lies in $SO^+(1,3)$.

In two dimensions, work in an orthonormal frame defined on all of a region $S$ bounded by the loop. The connection is then a single $\mathfrak{so}(2)$-valued one-form $\omega$ whose values commute, so the ordering drops out: the holonomy is a rotation by an angle given by $\oint_\gamma \omega$, with its sign fixed by the frame's orientation, and Stokes' theorem turns that integral into $\iint_S K\,dA$. In a coordinate basis the matrices $\Gamma_\mu$ do not commute, and the ordering still matters. In three or more dimensions the ordering matters in every frame; the exact finite-loop statement, the non-abelian Stokes theorem, is a surface-ordered exponential of curvature transported back to $p$.

For a small loop that flows a parameter distance $\epsilon$ along vector fields $u$ and then $v$ and back, $\mathrm{Hol} = 1 - \epsilon^2\,\mathcal{R}(u,v) + O(\epsilon^3)$, where $\mathcal{R}(u,v) = [\nabla_u,\nabla_v] - \nabla_{[u,v]}$ has components $R^\rho{}_{\sigma\mu\nu}u^\mu v^\nu$. When $[u,v] \neq 0$ the loop needs a short extra closing leg, whose effect is the $\nabla_{[u,v]}$ term. The Riemann tensor is thus a linear map from oriented 2-planes to generators of metric-preserving transformations.

**Takeaway:** Holonomy is the path-ordered product of transport steps; for the Levi-Civita connection it is a rotation or Lorentz transformation, and curvature is its infinitesimal form.

*Picture:* At a point p, the circle of unit tangent directions; each loop through p acts on it as a rotation, and small loops give rotations linear in the loop's oriented area element.

*What this leaves out:* Restricted to the Levi-Civita connection; holonomy is defined for any connection on any vector bundle.

*Continues:* `ways_in/shrink-the-loop-to-find-riemann`<br>*Builds on:* [[levi-civita-connection]], [[lie-bracket]]<br>*See:* `problems/latitude-holonomy-from-path-ordering`, `problems/small-loop-change-is-a-rotation`, `checks/why-ordering-matters`

### 7. Loops around tips and holes · formal · contrast

*Can a loop return a vector rotated where there is no curvature at all?*

The paper tube in "Bent is not the same as curved" returned every arrow unturned because it unrolls flat. A paper cone also unrolls flat, yet one kind of loop on it behaves differently. Make the cone by cutting a wedge of angle $\delta$ out of a flat sheet and gluing the cut edges together. Away from the tip the cone is flat: its Gaussian curvature is zero, and a small loop there returns vectors unchanged. Now carry a vector once around the tip. Unroll the cone. The loop becomes a path from one cut edge to the other, the vector slides rigidly along it, and gluing the edges back rotates it by $\delta$ toward the walker's left. A loop that winds $n$ times around the tip returns a rotation by $n\delta$ modulo $2\pi$.

This separates two ideas that the small-loop law ties together. The restricted holonomy group $\mathrm{Hol}^0_p$ consists of the transformations produced by loops that can be shrunk to a point; on a connected region it is trivial exactly when $R = 0$ there. The full holonomy group $\mathrm{Hol}_p$ also contains the transformations produced by loops that cannot be shrunk, and those can be nontrivial in a flat region: around the cone's missing tip, or along a flat Möbius band, where a loop along the band returns a reflection. In the local Gauss–Bonnet sum, a disk around the tip contributes $\delta$, in the limit of rounding off the tip.

The same structure appears in gravity. Outside an idealized, infinitely thin, straight cosmic string whose tension equals its mass per unit length $\mu$ times $c^2$, spacetime is locally flat. Yet vectors carried around the string return rotated, in the plane perpendicular to it, by the deficit angle $8\pi G\mu/c^2$. Regge calculus builds curved spacetimes from flat pieces on the same principle.

**Takeaway:** Zero curvature guarantees an unrotated return only for loops that can be shrunk to a point; loops around tips or holes can still rotate vectors.

*What this leaves out:* Idealizes the tip as a point and the string as infinitely thin.

*Continues:* `ways_in/bent-is-not-curved`, `ways_in/turn-equals-enclosed-curving`<br>*Visuals:* [[paper-cone-with-a-missing-wedge]]<br>*See:* `checks/cone-holonomy-group`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To move the arrow's direction to the left or right along the ground. The rule of the arrow test is that the arrow never swings. | — |
| walk straight | — | On a ball, walking without ever steering left or right. On a globe, the lines from top to bottom and the equator are straight walks. A small circle around the North Pole is not: to stay on it you must keep steering. | [[geodesic]] |
| holonomy | ho-LON-uh-mee | The turn between an arrow's starting direction and its direction after being carried once around a loop, never swinging. | [[holonomy]] |
| intrinsic curvature | in-TRIN-zik | Curving built into a surface, which someone living on it can detect without looking from outside. A ball has it. A rolled-up paper tube does not. | [[intrinsic-versus-extrinsic-curvature]] |
| gyroscope | JY-ruh-scope | A fast-spinning wheel whose spin axis keeps pointing the same way unless something twists it. | — |
| orbit | — | The path of something that keeps falling around a planet without hitting it, as the Moon does around Earth. | — |

## Key equations

### Area rule on a sphere · working

$$
\Delta\alpha = \frac{A}{a^2} \pmod{2\pi}
$$

On a sphere, the turn of an arrow carried around a loop is the area on the walker's left in units of the radius squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta\alpha$ | turn of the returned arrow in radians, positive toward the walker's left | the turn |
| $A$ | area of the region on the walker's left | the fenced-off area |
| $a$ | radius of the sphere | the radius |

**Holds when:** Simple loop on a sphere of radius $a$; sense and branch as in the course conventions.  
**Say it:** “The turn, in radians, is the fenced-off area divided by the radius squared.”  
**Justified by:** `stated`

### Area rule on any surface (local Gauss–Bonnet) · working

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

On any two-dimensional surface, the turn around a loop equals the total Gaussian curvature of the region on the walker's left.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S$ | the region on the walker's left | the fenced-off region |
| $K$ | Gaussian curvature at each point of $S$ | the Gaussian curvature |
| $dA$ | an element of area | a small piece of area |

**Holds when:** Oriented smooth surface with its Levi-Civita connection; simple, piecewise-smooth loop bounding a region $S$ with no cone points or holes; positive toward the walker's left; exact for any size; modulo $2\pi$.  
**Say it:** “The turn equals the Gaussian curvature added up over the fenced-off region.”  
**Justified by:** `stated`

### Turn around a geodesic triangle · working

$$
\Delta\alpha = \alpha_1 + \alpha_2 + \alpha_3 - \pi
$$

For a triangle made of geodesics, the turn equals how much its interior angles overshoot a straight angle.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\alpha_1, \alpha_2, \alpha_3$ | the interior angles of the triangle | the three angles |

**Holds when:** Sides are geodesics; the triangle bounds a smooth region on the walker's left.  
**Say it:** “The turn is how far the three angles add up to more than a straight angle.”  
**Justified by:** `angular-excess`

### Small-loop law · working

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma\,a^\mu\,b^\nu
$$

The change in a vector carried around a tiny parallelogram is minus the Riemann tensor acting on the vector and on the two edges.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta V^\rho$ | change of the carried vector after one trip | the change in the vector |
| $V^\sigma$ | the carried vector | the vector |
| $a^\mu,\ b^\nu$ | edge vectors of the parallelogram, walked $+a, +b, -a, -b$ | the two edges |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course sign convention | the Riemann tensor |

**Holds when:** Torsion-free connection; coordinate parallelogram walked $+a, +b, -a, -b$; valid to second order in the loop size.  
**Say it:** “The change in the vector is minus the Riemann tensor acting on the vector and on the two edges of the loop.”  
**Justified by:** `derivations/small-loop-law-from-transport`

### Holonomy as a path-ordered exponential · formal

$$
\mathrm{Hol}(\gamma) = \mathcal{P}\exp\Big(-\oint_\gamma \Gamma_\mu\,dx^\mu\Big),\qquad (\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}
$$

Carrying a vector around a finite loop multiplies it by the ordered product of the connection's small steps.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathrm{Hol}(\gamma)$ | the holonomy of the loop, a linear map of the tangent space at the base point | the holonomy of the loop |
| $\mathcal{P}$ | path ordering: later points of the loop act after earlier ones | path ordering |
| $\Gamma_\mu$ | coordinate connection matrices built from the Christoffel symbols | the connection matrices |

**Holds when:** Piecewise-smooth loop inside one coordinate chart (otherwise include transition matrices); the ordering cannot be dropped in a coordinate basis; basis and base-point changes conjugate the matrix.  
**Say it:** “The holonomy is the path-ordered exponential of minus the connection, taken around the loop.”  
**Justified by:** `stated`

## Derivations

### The small-loop law from the transport equation · working

**Goal:** Show that walking a coordinate parallelogram $+a, +b, -a, -b$ changes a vector by $-R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$.

1. Carrying a vector without swinging it obeys $\frac{dV^\rho}{ds} = -\Gamma^\rho{}_{\mu\sigma}\frac{dx^\mu}{ds}V^\sigma$. In matrix form, $\frac{dV}{ds} = -\Gamma_{\dot x}V$, with $(\Gamma_e)^\rho{}_\sigma \equiv \Gamma^\rho{}_{\mu\sigma}e^\mu$.
2. For one short straight step $e$ from a point $x$, with $s$ from 0 to 1, expand to first order along the step: $\Gamma_e(x + se) = \Gamma_e + s\,\partial_e\Gamma_e$, where $\partial_e\Gamma_e \equiv e^\nu\partial_\nu\Gamma_e$ and the right side is evaluated at $x$.
3. Integrate the matrix equation, keeping terms of second order in $e$. The step multiplies $V$ by $P_e(x) = 1 - \Gamma_e - \tfrac12\partial_e\Gamma_e + \tfrac12\Gamma_e\Gamma_e$.
4. The four steps start at $x$, $x+a$, $x+a+b$ and $x+b$. Expand each connection matrix about $x$: $\Gamma_b(x+a) = \Gamma_b + \partial_a\Gamma_b$, $\Gamma_{-a}(x+a+b) = -(\Gamma_a + \partial_a\Gamma_a + \partial_b\Gamma_a)$, and $\Gamma_{-b}(x+b) = -(\Gamma_b + \partial_b\Gamma_b)$.
5. The four step matrices to second order are $P_1 = 1 - \Gamma_a - \tfrac12\partial_a\Gamma_a + \tfrac12\Gamma_a^2$, $P_2 = 1 - \Gamma_b - \partial_a\Gamma_b - \tfrac12\partial_b\Gamma_b + \tfrac12\Gamma_b^2$, $P_3 = 1 + \Gamma_a + \tfrac12\partial_a\Gamma_a + \partial_b\Gamma_a + \tfrac12\Gamma_a^2$, and $P_4 = 1 + \Gamma_b + \tfrac12\partial_b\Gamma_b + \tfrac12\Gamma_b^2$.
6. Multiply $P_4P_3P_2P_1$. The first-order terms cancel: $-\Gamma_a - \Gamma_b + \Gamma_a + \Gamma_b = 0$.
7. Collect the derivative terms. $\partial_a\Gamma_a$ appears as $-\tfrac12 + \tfrac12$ and $\partial_b\Gamma_b$ as $-\tfrac12 + \tfrac12$, so both cancel, leaving $\partial_b\Gamma_a - \partial_a\Gamma_b$.
8. Collect the products of first-order terms, with each later factor on the left: $\Gamma_b\Gamma_a - \Gamma_a^2 - \Gamma_a\Gamma_b - \Gamma_b\Gamma_a - \Gamma_b^2 + \Gamma_b\Gamma_a$. Adding the four $\tfrac12\Gamma^2$ terms, which total $\Gamma_a^2 + \Gamma_b^2$, leaves $\Gamma_b\Gamma_a - \Gamma_a\Gamma_b$.
9. Second derivatives of $\Gamma$ and triple products enter only at third order. So $\Delta V^\rho = a^\mu b^\nu\big(\partial_\nu\Gamma^\rho{}_{\mu\sigma} - \partial_\mu\Gamma^\rho{}_{\nu\sigma} + \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}\big)V^\sigma$.
10. The course definition is $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. The bracket in the previous step is exactly its negative.

**Result:** $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, with corrections of third order in the loop size.

## Worked examples

### A small cell on the unit sphere · working

**Problem:** On the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, carry $V = e_\theta$ around a small cell walked $+\delta\theta$, $+\delta\phi$, $-\delta\theta$, $-\delta\phi$. Find the change and compare it with the cell's area.

1. The nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$.
2. The course definition gives $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, so $R_{\theta\phi\theta\phi} = \sin^2\theta$. Antisymmetry in the first pair gives $R_{\phi\theta\theta\phi} = -\sin^2\theta$, and raising with $g^{\phi\phi} = 1/\sin^2\theta$ gives $R^\phi{}_{\theta\theta\phi} = -1$.
3. The small-loop law with $a^\theta = \delta\theta$, $b^\phi = \delta\phi$ and $V^\theta = 1$ gives $\Delta V^\phi = -R^\phi{}_{\theta\theta\phi}\,\delta\theta\,\delta\phi = +\delta\theta\,\delta\phi$, and $\Delta V^\theta = 0$.
4. The basis vector $e_\phi$ has length $\sin\theta$, so the unit vector $e_\theta$ tilts toward $e_\phi$ by the angle $\sin\theta\,\delta\theta\,\delta\phi$.
5. The cell's area is $\sin\theta\,\delta\theta\,\delta\phi$ and $K = 1$, so the area rule predicts the same angle. Seen from outside, turning from $e_\theta$ toward $e_\phi$ is counterclockwise, the positive sense for this walk.

**Answer:** $\Delta V = \delta\theta\,\delta\phi\;e_\phi$: a positive rotation by $\sin\theta\,\delta\theta\,\delta\phi$, the enclosed area.

**Takeaway:** The index formula and the area rule agree in size and in sense, which checks the sign convention.

## Problems

### `equator-walk` · entry · difficulty 1 · conceptual

You walk once all the way around the equator of a smooth ball, carrying a cardboard arrow that points straight ahead at the start and never swings. Back at the start, does the arrow point the way it did when you set off? Does this mean the ball is not curved after all?

**Hints**

1. Where does the arrow point at every moment of this walk?
2. Does the walk from the North Pole still bring its arrow back turned?

**Answer:** It comes back pointing the same way, but the ball is still curved: the walk from the North Pole brings its arrow back a quarter turn away.

**Must contain:** The arrow comes back pointing the same way; The equator is a straight walk with no corners; One matching loop does not make the ball flat

**Numeric:** turn = 0 deg (magnitude, ±1)

**Solution**

1. The equator is a straight walk with no corners, so the arrow keeps the same angle to your path, pointing straight ahead the whole way.
2. Back at the start you face the way you set off, so the arrow matches its start.
3. One matching loop does not make a surface flat; the North Pole walk still gives a turn, which never happens on a flat table.

### `earth-loop-size` · working · difficulty 1 · estimate

Treat Earth as a sphere of radius 6371 km. A loop on its surface returns a carried arrow turned by 1°. How large an area does the loop enclose, and how does that compare with France, about 550,000 km²?

**Hints**

1. Convert 1° to radians.
2. Solve the area rule on a sphere for the area.

**Answer:** About $7.1\times10^{5}$ km², roughly 1.3 times the area of France.

**Must contain:** Turn of 1 degree is 0.01745 radians; Area equals the turn in radians times the radius squared; About 1.3 times the area of France

**Numeric:** area = 708423 km^2 (magnitude, ±3%)

**Solution**

1. $1^\circ = \pi/180 = 0.017453$ rad.
2. The area rule $\Delta\alpha = A/a^2$ gives $A = \Delta\alpha\,a^2$.
3. $a^2 = (6371\ \text{km})^2 = 4.0590\times10^{7}$ km².
4. $A = 0.017453 \times 4.0590\times10^{7} = 7.08\times10^{5}$ km², and $7.08\times10^{5}/5.5\times10^{5} \approx 1.3$.

### `saddle-sign` · working · difficulty 2 · calculation

Near its centre, a saddle-shaped surface has Gaussian curvature $K \approx -1/R^2$. A small simple loop there encloses area $A \ll R^2$ on the walker's left. Find the turn and its sense.

**Hints**

1. Use the local Gauss–Bonnet rule with a nearly constant $K$.

**Answer:** $\Delta\alpha \approx -A/R^2$: a rotation of size $A/R^2$ toward the walker's right.

**Must contain:** The enclosed curvature is about K times A; The turn is about minus A over R squared; Negative means toward the walker's right

**Solution**

1. For a small region $K$ is nearly constant, so $\iint_S K\,dA \approx K A$.
2. With $K \approx -1/R^2$, $\Delta\alpha \approx -A/R^2$.
3. A negative turn rotates the arrow toward the walker's right, against the positive sense.

### `small-loop-cell-other-vector` · working · difficulty 2 · calculation

On the unit sphere, carry the unit vector $V = e_\phi/\sin\theta$ around a small cell walked $+\delta\theta$, $+\delta\phi$, $-\delta\theta$, $-\delta\phi$. Use the small-loop law to find $\Delta V^\theta$, and check the size and sense of the rotation against the area rule.

**Hints**

1. Use $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and $V^\phi = 1/\sin\theta$.
2. Which way does turning $\hat\phi$ toward $-\hat\theta$ go, seen from outside?

**Answer:** $\Delta V^\theta = -\sin\theta\,\delta\theta\,\delta\phi$: a positive rotation by $\sin\theta\,\delta\theta\,\delta\phi$, the same as for $e_\theta$ and equal to the cell's area.

**Must contain:** Delta V theta equals minus sine theta times the cell's coordinate size; The rotation angle equals the cell's area; Every vector is rotated by the same angle in the same sense

**Solution**

1. $\Delta V^\theta = -R^\theta{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ with $V^\phi = 1/\sin\theta$, $a^\theta = \delta\theta$, $b^\phi = \delta\phi$.
2. Only $\sigma = \phi$ contributes: $\Delta V^\theta = -R^\theta{}_{\phi\theta\phi}\,(1/\sin\theta)\,\delta\theta\,\delta\phi = -\sin\theta\,\delta\theta\,\delta\phi$.
3. $e_\theta$ has unit length, so the unit vector $\hat\phi$ tilts toward $-\hat\theta$ by $\sin\theta\,\delta\theta\,\delta\phi$.
4. A counterclockwise rotation seen from outside takes $\hat\theta$ to $\hat\phi$ and $\hat\phi$ to $-\hat\theta$, so this is the same positive rotation found for $e_\theta$, equal to the cell's area.

### `small-loop-change-is-a-rotation` · formal · difficulty 2 · proof

Using the small-loop law for the Levi-Civita connection, show that $V_\rho\,\Delta V^\rho = 0$ for every vector $V$. Explain why this makes the holonomy of a small loop an infinitesimal rotation or boost.

**Hints**

1. Lower the first index of the Riemann tensor.
2. Which symmetry does $R_{\rho\sigma\mu\nu}$ have in its first two indices?

**Answer:** $V_\rho\,\Delta V^\rho = -R_{\rho\sigma\mu\nu}V^\rho V^\sigma a^\mu b^\nu = 0$, because $R_{\rho\sigma\mu\nu}$ is antisymmetric in $\rho\sigma$. The generator $\Omega_{\rho\sigma} = -R_{\rho\sigma\mu\nu}a^\mu b^\nu$ is antisymmetric, so it lies in the Lie algebra of the metric's orthogonal or Lorentz group.

**Must contain:** Antisymmetry of the Riemann tensor in its first pair for a metric connection; A symmetric product contracted with an antisymmetric tensor vanishes; An antisymmetric generator preserves the metric to first order

**Solution**

1. Contract the small-loop law with $V_\rho$: $V_\rho\,\Delta V^\rho = -R_{\rho\sigma\mu\nu}V^\rho V^\sigma a^\mu b^\nu$.
2. For a metric-compatible connection $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$, while $V^\rho V^\sigma$ is symmetric, so the contraction vanishes.
3. Write the holonomy as $1 + \Omega$ with $\Omega^\rho{}_\sigma = -R^\rho{}_{\sigma\mu\nu}a^\mu b^\nu$; the lowered form $\Omega_{\rho\sigma}$ is antisymmetric.
4. $1 + \Omega$ preserves $g$ to first order exactly when $\Omega_{\rho\sigma} + \Omega_{\sigma\rho} = 0$, so $\Omega$ lies in the Lie algebra of $SO(n)$ or $SO(1,3)$: an infinitesimal rotation or boost.

### `latitude-holonomy-from-path-ordering` · formal · difficulty 3 · derivation

On a sphere of radius $a$, compute the holonomy of the circle at colatitude $\theta_0$, walked eastward, directly from the transport equation in the orthonormal frame $(\hat\theta, \hat\phi)$. Show that the result does not depend on $a$, and relate it to the area rule.

**Hints**

1. The Christoffel symbols of $a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$ do not depend on $a$.
2. Show that the connection matrix along the circle is constant.

**Answer:** A clockwise rotation, seen from outside, by $2\pi\cos\theta_0$ for every $a$. Modulo $2\pi$ this is the counterclockwise rotation by $2\pi(1-\cos\theta_0)$ that the area rule gives for the polar cap on the walker's left.

**Must contain:** The connection matrix along the circle is constant, so ordering is irrelevant; Rotation by minus two pi cos theta zero, independent of a; Equal modulo two pi to the area-rule turn two pi times one minus cos theta zero

**Solution**

1. Parametrize the circle by $\phi \in [0, 2\pi]$; only $dx^\phi/d\phi = 1$ is nonzero. The Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\phi\theta} = \cot\theta$, independent of $a$.
2. The transport equation gives $dV^\theta/d\phi = \sin\theta_0\cos\theta_0\,V^\phi$ and $dV^\phi/d\phi = -\cot\theta_0\,V^\theta$.
3. In orthonormal components $x = aV^\theta$ and $y = a\sin\theta_0\,V^\phi$ these become $dx/d\phi = \cos\theta_0\,y$ and $dy/d\phi = -\cos\theta_0\,x$. The matrix is constant, so path ordering is irrelevant and $a$ has dropped out.
4. Starting from $(1, 0)$ the solution is $(\cos(\phi\cos\theta_0), -\sin(\phi\cos\theta_0))$: after one lap, a rotation by $-2\pi\cos\theta_0$ in the $(\hat\theta, \hat\phi)$ basis.
5. Seen from outside, $\hat\theta$ to $\hat\phi$ is counterclockwise, so this is a clockwise rotation by $2\pi\cos\theta_0$.
6. Modulo $2\pi$ it equals a counterclockwise rotation by $2\pi(1-\cos\theta_0)$, the area rule for the cap on the walker's left. At $\theta_0 = 45^\circ$ that is $254.6^\circ$ clockwise, or $105.4^\circ$ counterclockwise.

## Observations

- **Geodetic precession of gyroscopes orbiting Earth, measured by Gravity Probe B** (measured, working). Each gyroscope's spin axis came back turned after every polar orbit about 642 km above Earth, within the orbital plane and in the same sense as the orbit, by about 1.2 milliarcseconds. Describing space around a static Earth at successive moments, two thirds of that turn is the holonomy of the curved space around the orbit; the rest comes from the gyroscope's motion through Earth's field. *Numbers:* Magnitudes: predicted $6606.1$ milliarcseconds per year, measured $6601.8 \pm 18.3$ milliarcseconds per year (the paper reports them as negative drift rates). *Reference:* C. W. F. Everitt, D. B. DeBra, B. W. Parkinson, J. P. Turneaure and others (2011), *Gravity Probe B: Final Results of a Space Experiment to Test General Relativity*, Physical Review Letters 106, 221101, doi:10.1103/PhysRevLett.106.221101 _(unverified)_
- **The slow turning of a Foucault pendulum's swing plane** (measured, working). Earth turns eastward, so seen from above the North Pole a pendulum at latitude $\lambda$ is carried counterclockwise around its circle of latitude once per sidereal day. For slow rotation and small swings, the swing plane obeys the arrow rule on Earth's surface. The holonomy of that circle is a counterclockwise rotation by $2\pi(1-\sin\lambda)$, which modulo $2\pi$ is a clockwise rotation by $2\pi\sin\lambda$: exactly the observed turn against local north per sidereal day. The cause is Earth's rotation; the sphere enters as the set of directions the local vertical takes around the lap. *Numbers:* At Paris, latitude $48.85^\circ$ north: $360^\circ\sin\lambda = 271^\circ$ per sidereal day, about $11.3^\circ$ per hour. *Reference:* Léon Foucault (1851), *Démonstration physique du mouvement de rotation de la Terre au moyen du pendule*, Comptes rendus hebdomadaires des séances de l'Académie des sciences 32 _(unverified)_

## Teaching arc

1. **Ask the insider question** (entry). Ask how someone who can never leave a ball, or look at it from above, could find out that it is curved. *Why:* It frames holonomy as a test made without leaving, the only kind available for the universe. *Uses:* `ways_in/walk-a-loop-on-a-ball`
2. **Show one surprise and two controls** (entry). Run the North Pole walk after a prediction, then the square on a flat floor and the loop around a tube. *Why:* The controls rule out the corners and mere bending as explanations. *Predict:* When the arrow gets back to the North Pole, will it point the way it did when you set off? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `octant`, tour `holonomy-first-walk`) *Uses:* `checks/octant-walk-prediction`, `checks/square-on-a-floor`, `ways_in/bent-is-not-curved`
3. **Discover the area rule** (working). Resize and reverse the loop, and tabulate the turn against area over radius squared. *Why:* Learners find proportionality, the sign flip, and the role of the radius themselves. *Predict:* If the loop fences off half as much of the ball, what happens to the turn? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `octant-half-area`) *Uses:* `ways_in/turn-equals-enclosed-curving`, `checks/triangle-on-a-big-sphere`
4. **Shrink the loop to reach the Riemann tensor** (working). Derive the small-loop law and read off each feature. *Why:* Each feature of the formula explains a slot of the Riemann tensor. *Predict:* If you swap the order of the two edges, what happens to the change in the vector? *Visual:* [[shrink-the-loop-to-find-riemann]] *Uses:* `ways_in/shrink-the-loop-to-find-riemann`, `derivations/small-loop-law-from-transport`, `problems/small-loop-cell-other-vector`
5. **Measure it in orbit** (working). Connect the arrow rule to a freely falling gyroscope and Gravity Probe B. *Why:* It turns a geometric picture into a measurement of the space around Earth. *Uses:* `ways_in/a-gyroscope-measures-it`, `observations/gravity-probe-b-geodetic`
6. **Mark the limits** (formal). Carry a vector around a paper cone's tip, then separate restricted from full holonomy. *Why:* It prevents the belief that flatness along a loop always means no rotation. *Predict:* Every patch of this cone away from the tip is flat. Will a loop around the tip bring the arrow back unturned? *Visual:* [[paper-cone-with-a-missing-wedge]] *Uses:* `ways_in/loops-around-tips-and-holes`, `checks/cone-holonomy-group`

## Analogies

### Polarization in a coiled optical fibre · working

Light guided through a gently coiled single-mode fibre, whose exit direction matches its entry direction, has a direction of travel that traces a closed loop on the sphere of directions. Its polarization is carried along without swinging and comes back rotated by an angle equal to the solid angle that loop encloses, modulo $2\pi$. The sense of the rotation reverses when the loop on the sphere of directions is traced the other way. This holds when stress-induced birefringence in the fibre is negligible.

| In the analogy | Stands for |
| --- | --- |
| the sphere of propagation directions | the curved surface |
| the polarization direction | the carried arrow |
| the enclosed solid angle | the enclosed curvature, $\iint K\,dA$ on the unit sphere |

*Limits:* The sphere is a space of directions, not physical space; the effect is a geometric phase in optics, and gravity plays no role.

### A charged particle's phase around a loop · formal

In the course convention a charged quantum field carried around a loop is multiplied by $\exp\big(+i(q/\hbar)\oint A_\mu dx^\mu\big)$, a phase $q\Phi/\hbar$ set by the magnetic flux $\Phi$ through the loop, oriented by the right-hand rule. For a small loop the phase is governed by the field strength $F_{\mu\nu}$, which plays the role the Riemann tensor plays for vectors. The Aharonov–Bohm setup, with no field on the path itself, is the gauge-field twin of the cone: holonomy without local field strength.

| In the analogy | Stands for |
| --- | --- |
| the phase of the wavefunction | the direction of the carried arrow |
| the electromagnetic potential $A_\mu$ | the connection |
| the field strength $F_{\mu\nu}$ | the Riemann tensor |

*Limits:* Phases commute, so their ordering around the loop never matters; rotations of vectors in three or more dimensions do not commute. The phase lives in an internal space, with no metric and no boosts.

## Misconceptions

### “If I never let the arrow swing, it cannot come back turned.” · entry · `never-swung-so-never-turned`

- **Why it is tempting:** On a flat floor, an arrow that never swings keeps pointing at the same wall forever.
- **What is true:** The rule says what to do at each small step, not where the arrow ends up after a long trip. On a ball those small steps add up to a turn.
- **Exposed by:** `checks/octant-walk-prediction`

### “The arrow turned because I turned at the corners.” · entry · `corners-caused-the-turn`

- **Why it is tempting:** The walker makes visible turns, and the arrow ends up pointing a new way.
- **What is true:** Corners turn the walker, not the arrow. A square on a flat floor has four corners and brings the arrow back unchanged.
- **Exposed by:** `checks/square-on-a-floor`

### “A tube looks curved, so an arrow carried around a loop on it must come back turned.” · entry · `tube-must-turn`

- **Why it is tempting:** From outside, the tube looks bent.
- **What is true:** A tube unrolls into a flat sheet without stretching, so the arrow test treats it as flat. Only curving that cannot be unrolled flat, like a ball's, changes the arrow.
- **Exposed by:** `checks/loop-around-a-tube`

### “It does not matter which way I walk around the loop.” · entry · `direction-does-not-matter`

- **Why it is tempting:** The patch fenced off looks the same either way.
- **What is true:** Walking the loop the other way plays the first trip backwards. So the arrow comes back turned by the same amount the other way.
- **Exposed by:** `checks/reverse-the-loop`

### “If the surface is flat everywhere along my loop, the arrow cannot come back rotated.” · working · `flat-along-loop-means-no-turn`

- **Why it is tempting:** The small-loop law makes holonomy look like a local sum of curvature along the path.
- **What is true:** Flatness guarantees no rotation only for loops that can be shrunk to a point within the flat region. A loop around the tip of a paper cone crosses only flat paper, yet it returns rotated.
- **Exposed by:** `checks/cone-holonomy-group`

### “Halfway around, I can see how much the arrow has turned so far.” · working · `running-angle-halfway`

- **Why it is tempting:** Animations show the arrow's direction in the room changing continuously.
- **What is true:** Arrows at different places on a curved surface can be compared only by carrying one to the other, and different routes give different answers. The turn is defined only when the loop closes.
- **Exposed by:** `checks/halfway-readout`

## Checks

1. **Entry · predict** `checks/octant-walk-prediction`. Picture a giant smooth ball. Start at the North Pole and walk straight to the equator. Turn left and walk a quarter of the way around the equator. Then turn left and walk straight back to the North Pole. You carry a cardboard arrow that points straight ahead at the start and never swings. Back at the North Pole, does the arrow point the same way it did when you set off? If not, how far apart are the two directions?
   - **Hints:** Where does the arrow point just after the first left turn? / Where does it point after the second left turn?
   - **Answer:** No. The arrow points ahead on the first stretch, to your right after the first left turn, and behind you after the second. Behind you along the last path is a right angle away from ahead along the first path, because the two paths leave the North Pole at a right angle. So the arrow comes back a quarter turn away from its start.
   - **Must contain:** The arrow does not come back pointing the same way; It points ahead, then right, then behind; The difference is a quarter turn
   - **Numeric:** turn = 90 deg (magnitude, ±5)
   - **Targets:** `never-swung-so-never-turned`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `octant`, tour `holonomy-first-walk`)
2. **Entry · predict** `checks/square-on-a-floor`. On a flat floor, you walk a square, turning left by a quarter turn at each of its four corners. You carry a cardboard arrow that points straight ahead at the start and never swings. Back at the start, which way does the arrow point?
   - **Hints:** Pick the wall the arrow points at when you start.
   - **Answer:** The same way it pointed at the start. The arrow never swings, so it keeps pointing at the same wall of the room while your body turns at the corners.
   - **Must contain:** It points the same way as at the start; The arrow keeps pointing at the same wall; Corners turn the walker, not the arrow
   - **Numeric:** turn = 0 deg (magnitude, ±1)
   - **Targets:** `corners-caused-the-turn`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `flat-square`)
3. **Entry · explain** `checks/loop-around-a-tube`. Roll a sheet of paper into a tube. You walk once around the tube, like a bracelet around a wrist, carrying a cardboard arrow that never swings. Back at the start, does the arrow point the same way it did when you set off? Why?
   - **Hints:** What does the tube become when you unroll it?
   - **Answer:** Yes. Unroll the tube and it becomes a flat sheet with nothing stretched. Your loop becomes a straight line across the sheet, and on flat paper the arrow never changes direction. The two ends of that line were glued together in the tube, so the arrow comes back matching its start.
   - **Must contain:** Yes, it points the same way; The tube unrolls flat without stretching; On the flat sheet the arrow never changes direction
   - **Numeric:** turn = 0 deg (magnitude, ±1)
   - **Targets:** `tube-must-turn`
   - **Visual:** [[carry-an-arrow-around-a-loop]] (preset `tube-unrolled`)
4. **Entry · predict** `checks/reverse-the-loop`. On a ball, you walk a small loop, turning left at each corner, with a cardboard arrow that never swings. The arrow comes back turned 5 degrees to the left. You set the arrow back to its starting direction, then walk the same loop the other way, turning right at each corner. How does the arrow come back?
   - **Hints:** What happens if you do the first trip and then the second trip, one after the other?
   - **Answer:** Turned 5 degrees to the right. One trip around a loop changes every arrow by the same amount, whichever way it pointed at the start. The second trip is the first trip played backwards, so doing both would bring an arrow exactly back to its start. The first trip moved the arrow 5 degrees left, so the backwards trip must move it 5 degrees right.
   - **Must contain:** Same amount, opposite direction; The backwards trip undoes the forwards trip; A trip changes every arrow by the same amount
   - **Numeric:** turn toward the walker's left = -5 deg (signed, ±0.5, mod 360)
   - **Targets:** `direction-does-not-matter`
5. **Working · numeric** `checks/triangle-on-a-big-sphere`. A triangle of great-circle arcs on a sphere of radius 1000 km has angles of 100°, 60° and 50°. By how much does an arrow carried around it turn, and what is the triangle's area?
   - **Hints:** Compare the angle sum with 180°. / Convert the excess to radians before using the area rule.
   - **Answer:** The angles sum to 210°, so the angular excess is 30°, or $\pi/6$ rad, and that is the turn. By the area rule the area is $(\pi/6)(1000\ \text{km})^2 \approx 5.24\times10^{5}$ km².
   - **Must contain:** Angle sum 210 degrees; Turn equals the excess, 30 degrees; Area equals the turn in radians times the radius squared
   - **Numeric:** turn = 0.5236 rad (magnitude, ±1%); area = 523599 km^2 (magnitude, ±1%)
6. **Working · numeric** `checks/latitude-30-north`. An arrow is carried once eastward around the circle of latitude 30° north on a sphere. By what angle does it return turned?
   - **Hints:** Measure the angle down from the North Pole.
   - **Answer:** The colatitude is 60°. The polar cap on the walker's left has area $2\pi a^2(1-\cos 60^\circ) = \pi a^2$, so the turn is $\pi$: a half turn. The circle is not a geodesic, yet the area rule still gives its turn exactly.
   - **Must contain:** Colatitude 60 degrees; Cap area is pi times the radius squared; The turn is a half turn
   - **Numeric:** turn = 3.1416 rad (magnitude, ±0.03)
   - **Visual:** [[arrow-around-a-circle-of-latitude]]
7. **Working · evaluate-claim** `checks/halfway-readout`. A demo shows the arrow halfway around the North Pole loop, with a readout saying 'turned 45° so far'. Evaluate the readout.
   - **Hints:** Relative to what would the 45° be measured?
   - **Answer:** The readout has no meaning as a holonomy. On a curved surface, arrows at different points can be compared only by carrying one to the other, and different routes give different answers. The turn is defined when the loop closes, where the starting arrow and the returned arrow sit at the same point.
   - **Must contain:** Arrows at different points have no route-independent comparison; The turn is defined only when the loop closes; A running angle depends on an arbitrary local reference
   - **Targets:** `running-angle-halfway`
8. **Working · explain** `checks/polar-coordinates-plane`. In polar coordinates on a flat plane, $\Gamma^r{}_{\phi\phi} = -r$ is not zero. Does a small loop there return vectors rotated?
   - **Hints:** Which object appears in the small-loop law?
   - **Answer:** No. The small-loop law sets the change by the Riemann tensor, which vanishes for the flat metric $dr^2 + r^2 d\phi^2$. Nonzero Christoffel symbols describe curved coordinate lines, not curved space.
   - **Must contain:** No rotation; Holonomy of small loops is governed by the Riemann tensor, not the Christoffel symbols; The plane's Riemann tensor is zero
9. **Formal · explain** `checks/cone-holonomy-group`. A flat cone is made by removing a wedge of angle $\delta$, and its tip is removed. What are its restricted and full holonomy groups at a point? When does vanishing curvature along a loop guarantee trivial holonomy?
   - **Hints:** Which loops cannot be shrunk to a point on the punctured cone?
   - **Answer:** The punctured cone is flat, so every contractible loop has trivial holonomy: the restricted group is trivial. A loop winding $n$ times around the missing tip gives a rotation by $n\delta$, so the full group is the subgroup of $SO(2)$ generated by the rotation by $\delta$, finite and cyclic when $\delta/2\pi$ is rational and dense otherwise. So vanishing curvature guarantees trivial holonomy only for contractible loops within the flat region.
   - **Must contain:** Restricted holonomy is trivial because the cone is flat; Full holonomy is generated by the rotation by delta; Only contractible loops in a flat region are guaranteed trivial holonomy
   - **Targets:** `flat-along-loop-means-no-turn`
   - **Visual:** [[paper-cone-with-a-missing-wedge]]
10. **Formal · explain** `checks/why-ordering-matters`. On the unit sphere, why can you not drop the path ordering $\mathcal{P}$ when computing the holonomy of a coordinate rectangle from the coordinate Christoffel matrices? What makes dropping it legitimate in two dimensions?
   - **Hints:** Write out $\Gamma_\theta$ and $\Gamma_\phi$ as 2 by 2 matrices and compute their commutator.
   - **Answer:** The coordinate matrices $\Gamma_\theta = \mathrm{diag}(0, \cot\theta)$ and $\Gamma_\phi$, with off-diagonal entries $-\sin\theta\cos\theta$ and $\cot\theta$, do not commute. So for the rectangle $\theta \in [0.5, 1.2]$, $\phi \in [0, 1]$ the ordered product gives the enclosed area, $29.52^\circ$, while the plain exponential gives neither that angle nor a length-preserving map. In an orthonormal frame on the whole region the connection is one $\mathfrak{so}(2)$-valued form whose values commute, so the ordering drops out and Stokes' theorem gives the area rule.
   - **Must contain:** Coordinate connection matrices do not commute; The ordered product gives the enclosed area, the unordered exponential does not; In an orthonormal frame in two dimensions the connection values commute
   - **Numeric:** rotation for the rectangle = 29.52 deg (magnitude, ±0.05)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the small-loop law | Walking $+a, +b, -a, -b$ gives $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ with the course Riemann tensor. | Some texts walk the edges in the other order, or define the Riemann tensor with the opposite overall sign, and write $+R$. State the route and the Riemann convention together. |
| Sense and branch of the holonomy angle | Positive toward the walker's left (counterclockwise seen from the side the normal points to), for the region on the walker's left, modulo $2\pi$. | A clockwise rotation by $2\pi\cos\theta_0$ and a counterclockwise rotation by $2\pi(1-\cos\theta_0)$ are the same rotation, and the literature quotes either form; published drift rates may carry the opposite sign. |

## Visuals

- ★ [[carry-an-arrow-around-a-loop]] (flagship): The central experience: the North Pole walk with flat-floor and tube controls, loops to resize and reverse, and a turn readout that appears only when the loop closes.
- [[shrink-the-loop-to-find-riemann]] (core): Connects the area rule to the Riemann tensor. *Sketch:* A coordinate parallelogram on a sphere patch, a saddle, or a polar-coordinate plane. The learner shrinks it and swaps the edge order; a log-log plot shows the vector's change against area with slope one, converging to the small-loop law, while the polar-coordinate plane stays at zero.
- [[paper-cone-with-a-missing-wedge]] (core): Shows holonomy without local curvature. *Sketch:* Cut a wedge of adjustable angle from a flat sheet and glue it into a cone, with the unrolled sheet beside it. Loops that avoid the tip return the arrow unchanged; loops winding n times around it return it rotated by n times the wedge angle.
- [[arrow-around-a-circle-of-latitude]] (supporting): The area rule for a curve that is not a geodesic, and the link to the Foucault pendulum. *Sketch:* Drag the latitude and play one lap. Plot the returned rotation against latitude in its two equivalent forms, counterclockwise $2\pi(1-\sin\lambda)$ and clockwise $2\pi\sin\lambda$, showing they are one rotation, with the Foucault pendulum's turn per sidereal day on the second.
- [[cube-of-small-loops]] (supporting): Geometric picture of the second Bianchi identity. *Sketch:* A small cube whose six faces are walked as loops, each face's rotation carried to a common corner along the edges; the sum shrinks faster than the cube, cancelling at third order in its size.

## Tutor moves

**Open with**

- Picture a giant smooth ball. You walk a big triangle on it, holding a cardboard arrow against the ground and never letting it swing left or right. When you get back to where you started, will the arrow point the same way it did at the start? *(prediction)*
- If you could never leave the surface of a ball, or look at it from above, how could you find out that it is curved? *(reflection)*

**If the learner is stuck**

- *The learner loses track of where the arrow points during the walk.* → Replay the walk one stretch at a time, and have the learner say the arrow's direction relative to the path: ahead, right, behind. *Uses:* `ways_in/walk-a-loop-on-a-ball`
- *The learner cannot find the area of a patch on a sphere.* → Use fractions of the whole sphere first: the North Pole triangle is one eighth of $4\pi a^2$. *Uses:* `ways_in/turn-equals-enclosed-curving`
- *The learner is lost in the index formula.* → Work the unit-sphere cell, computing one component, and show that the angle equals the cell's area. *Uses:* `worked_examples/unit-sphere-cell`
- *The learner asks for the angle partway around.* → Ask what the moving arrow would be compared with, then show that two routes to the halfway point give different answers. *Uses:* `checks/halfway-readout`

**Common questions**

- *If I never let the arrow swing, where does the turn come from?* (entry) Each step obeys the rule; what is different is the ground. A triangle on a flat table has inside angles adding up to half a turn, but the North Pole triangle has three right angles, three quarters of a turn. That extra quarter turn is the ball's curving, and it matches the arrow's change exactly. *Uses:* `ways_in/walk-a-loop-on-a-ball`, `checks/square-on-a-floor`
- *Why does this matter for gravity?* (entry) We live inside space and time, and nobody can look at them from outside. So tests made without leaving are the only way to find their curving. A gyroscope keeps pointing the same way unless something twists it, so it acts like the arrow that never swings. Carried around Earth in orbit, a gyroscope's direction slowly drifts, adding up to about five millionths of a full turn each year. Most of that drift comes from the curving of space around Earth, and a space experiment called Gravity Probe B measured it. *Uses:* `ways_in/a-gyroscope-measures-it`, `observations/gravity-probe-b-geodetic`
- *Does a bigger ball give a bigger turn?* (entry) It depends on what you keep the same. For a triangle with the same corner angles, no: on a bigger ball the triangle is bigger, and the turn stays the same. For a loop of the same size in kilometres, a bigger ball gives a smaller turn, because a bigger ball curves more gently. *Uses:* `checks/triangle-on-a-big-sphere`

**Switching levels**

- To working when: asks how big the turn is; starts using areas or angles as numbers. Go to the area rule and the triangle check. *Uses:* `ways_in/turn-equals-enclosed-curving`, `checks/triangle-on-a-big-sphere`
- To formal when: is comfortable with index notation; asks whether the turn is always a rotation. Derive the small-loop law, then the path-ordered exponential and the cone. *Uses:* `derivations/small-loop-law-from-transport`, `ways_in/whole-loops-as-transformations`
- To research when: asks about groups of loops, discrete gravity, or quantum gravity. Open the research horizon. *Uses:* `research_horizon/special-holonomy`, `research_horizon/discrete-gravity`

**Pronunciations:** Levi-Civita → LEH-vee CHEE-vee-tah; Gauss–Bonnet → GOWSS bon-AY; Riemann → REE-mahn; Aharonov–Bohm → ah-HAR-uh-nov BOHM; Regge → REJ-eh

**Voice notes:** Use degrees and fractions of a turn with beginners; switch to radians once the area rule is on the table.

## History

- **Carl Friedrich Gauss (1827).** Showed that a surface's curvature can be measured from within the surface, and related the angle sum of a geodesic triangle to the curvature it encloses. Presented in 1827 and published in 1828. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas* _(unverified)_
- **Pierre Ossian Bonnet (1848).** Extended Gauss's angle-sum result to regions bounded by arbitrary curves, giving the local Gauss–Bonnet theorem.
- **Tullio Levi-Civita (1917).** Defined parallel transport on Riemannian manifolds, first through an embedding in flat space, and used it to give Riemann's curvature a geometric meaning. Weyl and Schouten soon gave intrinsic formulations. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–205 _(unverified)_
- **Élie Cartan (1926).** Introduced holonomy groups and made them a central tool of differential geometry. Élie Cartan (1926), *Les groupes d'holonomie des espaces généralisés*, Acta Mathematica 48, 1–42 _(unverified)_
- **Warren Ambrose, Isadore Singer (1953).** Proved that the Lie algebra of the holonomy group is spanned by curvature operators transported back to the base point. Warren Ambrose, Isadore M. Singer (1953), *A theorem on holonomy*, Transactions of the American Mathematical Society 75, 428–443 _(unverified)_

## Research horizon

- **Special holonomy.** Berger classified the possible holonomy groups of irreducible Riemannian manifolds that are not locally symmetric. Manifolds whose holonomy lies in $SU(3)$, the Calabi–Yau threefolds, or in $G_2$ admit covariantly constant spinors, which is why they serve as the extra dimensions of string and M-theory compactifications that preserve some supersymmetry. Marcel Berger (1955), *Sur les groupes d'holonomie homogènes de variétés à connexion affine et des variétés riemanniennes*, Bulletin de la Société Mathématique de France 83, 279–330, doi:10.24033/bsmf.1464 _(unverified)_; Philip Candelas, Gary T. Horowitz, Andrew Strominger, Edward Witten (1985), *Vacuum configurations for superstrings*, Nuclear Physics B 258, 46–74 _(unverified)_
- **Discrete gravity.** Regge calculus builds spacetime from flat simplices glued together. All curvature sits on codimension-two hinges and is measured by deficit angles, the holonomies of small loops around the hinges. Causal dynamical triangulations use this construction to define a path integral for quantum gravity. Tullio Regge (1961), *General relativity without coordinates*, Il Nuovo Cimento 19, 558–571 _(unverified)_; Jan Ambjørn, Jerzy Jurkiewicz, Renate Loll (2004), *Emergence of a 4D world from causal quantum gravity*, Physical Review Letters 93, 131301, arXiv:hep-th/0404156 _(unverified)_
- **Loop quantum gravity.** Loop quantum gravity takes the holonomies of a connection along curves, rather than the metric, as its basic variables. Spin networks, graphs labelled by group representations, give a basis of its quantum states. Abhay Ashtekar (1986), *New variables for classical and quantum gravity*, Physical Review Letters 57, 2244 _(unverified)_; Carlo Rovelli (1998), *Loop quantum gravity*, Living Reviews in Relativity 1, 1, arXiv:gr-qc/9710008 _(unverified)_
