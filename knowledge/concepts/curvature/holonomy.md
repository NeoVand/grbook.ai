---
type: "concept"
schema_version: 2
id: "holonomy"
title: "Holonomy"
tagline: "How an arrow carried around a loop can come back turned"
domain: "curvature"
tier: "core"
status: "draft"
revision: 1
updated: "2026-09-13"
aliases: ["holonomy of parallel transport", "loop holonomy"]
prerequisites: ["path-dependence-of-parallel-transport", "gaussian-curvature", "angular-excess", "riemann-curvature-tensor", "levi-civita-connection", "lie-bracket"]
leads_to: ["flatness-criterion", "riemann-curvature-operator", "bianchi-identity", "gauge-field-strength", "cosmic-string", "geodetic-precession"]
visuals: ["carry-an-arrow-around-a-loop", "shrink-the-loop-to-find-riemann", "paper-cone-with-a-missing-wedge", "arrow-around-a-circle-of-latitude", "cube-of-small-loops"]
---

# Holonomy

*How an arrow carried around a loop can come back turned*

`holonomy` · curvature · core · draft (revision 1)

**Needs:** [[path-dependence-of-parallel-transport]] (entry) · [[gaussian-curvature]] (working) · [[angular-excess]] (working) · [[riemann-curvature-tensor]] (working) · [[levi-civita-connection]] (formal) · [[lie-bracket]] (formal)  
**Opens:** [[flatness-criterion]] · [[riemann-curvature-operator]] · [[bianchi-identity]] · [[gauge-field-strength]] · [[cosmic-string]] · [[geodetic-precession]]  
**Related:** [[parallel-transport]] · [[intrinsic-versus-extrinsic-curvature]] · [[curvature-of-the-two-sphere]] · [[gauge-parallel-transport]] · [[loop-quantum-gravity]]  
**Visuals:** ★ [[carry-an-arrow-around-a-loop]] · [[shrink-the-loop-to-find-riemann]] · [[paper-cone-with-a-missing-wedge]] · [[arrow-around-a-circle-of-latitude]] · [[cube-of-small-loops]]

> Carry an arrow around a loop without ever letting it swing left or right, then compare it with the way it pointed at the start. On a flat table it always comes back pointing the same way. On a ball, most loops bring it back pointing a new way. That turn is the loop's holonomy, and it lets someone who lives on a surface discover that the surface is curved without ever leaving it.

## You will be able to

**Entry**
- Explain how carrying an arrow around a loop, never letting it swing, shows that a ball is curved while a flat table and a paper tube are not. `objectives/explain-the-arrow-test`
- Predict how the returned turn changes when the same loop is walked the other way. `objectives/predict-reversal`

**Working**
- Compute the turn for loops on a sphere or a saddle from the enclosed area, the angle excess of a triangle, or the latitude of a circle. `objectives/compute-turn-from-area`
- Explain why the turn is defined only when the loop closes, and not partway around. `objectives/explain-when-turn-is-defined`
- Use the small-loop law to find the change of a vector around a small cell, with the correct sign. `objectives/use-small-loop-law`

**Formal**
- Distinguish holonomy from curvature: state when zero curvature guarantees trivial holonomy, and give counterexamples. `objectives/distinguish-curvature-and-holonomy`
- Prove that small-loop holonomy is an infinitesimal rotation or boost, and compute a finite holonomy as a matrix exponential. `objectives/prove-holonomy-preserves-the-metric`

## Ways in

### 1. Walk a loop on a ball · entry · picture

*How can someone who never leaves a ball find out that it is curved?*

**Recap:** Carrying an arrow without letting it swing can bring it to the same spot pointing in different directions, depending on the route. A loop is two routes joined end to end.

Imagine a huge, smooth ball with no hills, and imagine you live on its surface. You can never leave the surface or look at the ball from above. Can you still find out that your world is curved?

Here is a test. Take a flat arrow, like a cardboard pointer, and lay it on the ground. Then walk along a path that ends exactly where it began. Such a path is called a loop.

As you walk, follow one rule about the arrow. Keep it lying flat on the ground, and never let it swing to the left or to the right. On a straight stretch, this means the arrow keeps the same angle to your path the whole way. At a corner, you turn your body, but you leave the arrow as it was. So after a corner, the arrow makes a new angle with your new path.

First, try it on a flat table. Walk a triangle, a square, or any loop you like. Because the arrow never swings, it keeps pointing at the same wall of the room the whole time. So it comes back pointing exactly the way it started.

Now try it on the ball. Mark one point on top and call it the North Pole, as on a globe. The equator is the circle around the middle, halfway between the North Pole and the bottom point. Walking straight on a ball means never steering left or right. On a globe, a straight walk from the North Pole follows one of the lines drawn from top to bottom.

Start at the North Pole with the arrow pointing straight ahead of you. Walk straight until you reach the equator, which you meet at a right angle. The arrow still points straight ahead. Turn left by a quarter turn, so that you walk along the equator. The arrow did not swing, so now it points to your right. Walk a quarter of the way around the equator, with the arrow pointing to your right the whole way. Then turn left by a quarter turn again, and walk straight back to the North Pole. The arrow did not swing at this corner either, so now it points straight behind you.

Back at the North Pole, compare. When you set off, the arrow pointed along your first path. Now it points back along your last path. How far apart are those two directions? Your last path starts a quarter of the way around the equator from your first path. A quarter of a full circle is a right angle. Seen from above the North Pole, the two paths meet like the corner of a book. So the arrow has come back turned by a quarter turn, even though it never swung. It turned the same way you turned at the corners: to the left.

This turn is called the holonomy of the loop. A flat table never produces one. So the patch of ground your loop fenced off, the smaller piece on your left as you walked, cannot be flat like a table. You learned that without ever leaving the surface.

Two more facts are worth knowing. Walk the same loop the other way, turning right at each corner, and the arrow comes back turned the other way, to the right. That has to happen, because the backwards trip undoes the forwards trip. Also, for loops that fence off less than half of the ball, a bigger patch gives a bigger turn. On Earth, a loop around an area of 10,000 square kilometres, about the size of a small country, turns the arrow by only about one seventieth of a degree. That is why nobody notices it in daily life.

**Try it:** Draw the three-stretch walk on an orange with a pen. Lay a matchstick at the top, along your first stretch, and mark that direction. Move the matchstick along the path in small steps, never letting it swing. Back at the top, compare it with your mark.

**Takeaway:** An arrow carried around a loop without swinging comes back turned on a ball but never on a flat table, so the turn reveals curving.

*Picture:* A globe with a three-stretch loop: from the North Pole straight to the equator, a quarter of the way along the equator, and straight back up. The arrow is drawn at the start, pointing along the first path, and at the finish, pointing back along the last path, a right angle apart.

*What this leaves out:* We used a smooth ball. A loop that fences off exactly half the ball, like the equator itself, turns the arrow by a full circle, so it looks unturned. On a surface with a sharp tip or a hole, a loop around the tip or the hole can turn the arrow. That can happen even where the ground is flat, as the paper cone shows. In the space and time we live in, a loop can change an arrow in more ways than a turn.

*Gist:* Walk a big triangle on a ball, keeping an arrow flat and never letting it swing. Back at the start, the arrow points a quarter turn away from where it began. On a flat table, that never happens.<br>*Retell:* If you walk a loop on a ball holding an arrow that never swings, the arrow comes back turned. On a flat table it never does. So the turn tells you the ball is curved.<br>*Builds on:* [[path-dependence-of-parallel-transport]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `octant`)

### 2. Bent is not the same as curved · entry · contrast

*Does a rolled-up paper tube count as curved for the arrow test?*

Roll a sheet of paper into a tube. From outside, the tube looks curved. Now do the arrow test on the tube.

Walk any loop on the tube, keeping the arrow flat and never letting it swing. The arrow comes back pointing exactly the way it started. Even a loop that wraps once around the tube, like a bracelet around a wrist, brings the arrow back unchanged.

Why? Unroll the tube. It becomes a flat sheet again, and nothing was stretched or squashed. Rolling and unrolling do not change any angle drawn on the paper. On the flat sheet, the arrow slides without swinging, so it points the same way everywhere. A loop drawn on the tube becomes a path on the flat sheet. The bracelet loop becomes a straight line from one edge of the sheet to the opposite edge, and those two edges were glued together in the tube. The arrow points the same way at both ends of that line. So when you roll the paper up again, the arrow comes back matching its start.

A ball is different. You cannot flatten a piece of orange peel without tearing or stretching it. Curving that cannot be flattened away is built into the surface itself. Someone living on the surface can detect it without looking from outside. This is called intrinsic curvature. Rolling a flat sheet into a tube does not create any.

**Try it:** Draw a small loop with an arrow on a sheet of paper, then roll the sheet into a tube. The drawing keeps every angle it had, because the paper did not stretch.

**Takeaway:** The arrow test cannot tell a flat sheet from a rolled-up one; it only notices curving that cannot be unrolled flat, like a ball's.

*Picture:* A paper tube beside its unrolled sheet. A bracelet loop on the tube becomes a straight line across the sheet, with the arrow pointing the same way at both ends.

*What this leaves out:* This contrast is about surfaces. The universe as a whole has no outside view, so its own curving is the built-in kind. Surfaces drawn inside it can still bend, and that other kind of bending matters in later topics.

*Gist:* A rolled-up paper tube looks curved, but an arrow carried around any loop on it comes back unturned, because the tube unrolls into flat paper without stretching.<br>*Retell:* A tube is rolled-up flat paper, so the arrow comes back unturned on it. Only curving you cannot flatten out, like a ball's, turns the arrow.<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `tube-unrolled`)

### 3. The turn equals the curving fenced off · working · calculation

*How big is the turn, and what decides it?*

In the walk from the North Pole, the loop fenced off one eighth of the ball's surface, and the arrow came back turned by a quarter turn, $\pi/2$ radians. The two numbers are linked. For a loop on a sphere of radius $a$, the turn in radians equals the fenced-off area divided by $a^2$:

$$\Delta\alpha = \frac{A}{a^2} \pmod{2\pi}.$$

Check it: the whole sphere has area $4\pi a^2$, one eighth of it is $\pi a^2/2$, and dividing by $a^2$ gives $\pi/2$. The sign rule is to take the region on the walker's left; the arrow then turns in the same sense as the walk. The equator fences off $2\pi a^2$, so its turn is $2\pi$, a full turn, which is why the arrow looks unturned there.

On a general surface the curving varies from place to place. Its strength at each point is the Gaussian curvature $K$: it is $1/a^2$ everywhere on a sphere, $0$ on a plane or a cylinder, and negative on a saddle. For a simple loop, one that does not cross itself, fencing off a smooth region $S$ on the walker's left, the turn is the curvature added up over $S$:

$$\Delta\alpha = \iint_S K\,dA \pmod{2\pi}.$$

This is the local Gauss–Bonnet theorem. It holds for loops of any size, and the sides need not be straight. Where $K<0$, the arrow turns against the sense of the walk.

Two special cases are worth owning. For a triangle whose sides are geodesics, the straight walks of a surface, the turn equals the angular excess: the amount by which the three angles add up to more than $\pi$. The North Pole walk has three right angles, so its excess is $3\pi/2 - \pi = \pi/2$. For a circle at colatitude $\theta_0$, the angle measured down from the North Pole, walked eastward, the polar cap on the walker's left has area $2\pi a^2(1-\cos\theta_0)$, so the turn is $2\pi(1-\cos\theta_0)$.

**Try it:** In the demo, halve the fenced-off area on the ball and watch the turn halve; then switch to the saddle and watch it reverse.

**Takeaway:** The turn is the total curvature fenced off by the loop, so on a sphere it is the enclosed area divided by the radius squared.

*Picture:* A sphere with a shaded patch and its boundary loop; beside it, a dial showing the returned arrow turned by the patch's area divided by the radius squared.

*What this leaves out:* In more than two dimensions, turns about different axes do not commute, so this simple area rule holds only for small loops.

*Gist:* On a sphere the turn, in radians, is the fenced-off area divided by the radius squared. On any surface it is the Gaussian curvature added up over the fenced-off region.<br>*Continues:* `ways_in/walk-a-loop-on-a-ball`<br>*Builds on:* [[gaussian-curvature]], [[angular-excess]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `octant-half-area`), [[arrow-around-a-circle-of-latitude]]<br>*See:* `worked_examples/forty-fifth-parallel`

### 4. Shrink the loop and the Riemann tensor appears · working · calculation

*What replaces the area rule when a small loop can lie in many different planes?*

On a surface, one number $K$ at each point was enough, because every small loop lies in the same plane. In four-dimensional spacetime a small loop can lie in many different planes, and each plane can give a different turn. So shrink the loop to a tiny parallelogram with edge vectors $a^\mu$ and $b^\nu$. Walk $+a$, then $+b$, then $-a$, then $-b$, and ask how a carried vector $V$ changes. To second order in the size of the loop, and with the course sign conventions,

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu,$$

where $R^\rho{}_{\sigma\mu\nu}$ is the Riemann curvature tensor. The derivation "The small-loop law from the transport equation" builds this one move at a time.

Read the formula one feature at a time.

- It is linear in $V$: the loop acts on vectors like a matrix.
- It is linear in each edge: doubling one side doubles the change.
- It is antisymmetric in the edges: swapping $a$ and $b$ walks the same parallelogram the other way round, and the change flips sign.
- It is proportional to the product of the edges: the change scales with the loop's area, as $A/a^2$ did on the sphere.

So the Riemann tensor is a machine. Feed it a small oriented patch, the two edges in order, and it returns a small change of vectors. Because carrying a vector this way preserves lengths and angles, $V_\rho\,\Delta V^\rho = 0$ to this order. The change is a small rotation on a surface, or a small Lorentz transformation, a rotation or a boost, in spacetime. On a two-dimensional surface the machine holds a single number: for a small cell of area $\delta A$ the turn is $K\,\delta A$.

**Takeaway:** The Riemann tensor turns a small oriented patch into a small rotation of vectors; that is what curvature measures.

*Picture:* A tiny parallelogram with edges a and b. A vector V goes around it and returns as V plus a small extra arrow at right angles to V. Reversing the walk flips the extra arrow; doubling b doubles it.

*What this leaves out:* Keeps only the leading order in the loop's size, for the torsion-free, metric-compatible connection of general relativity.

*Gist:* Shrink the loop to a tiny parallelogram. The change in the carried vector is minus the Riemann tensor acting on the vector and the two edges, so the Riemann tensor turns a small patch of area into a small rotation.<br>*Continues:* `ways_in/turn-equals-enclosed-curving`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[shrink-the-loop-to-find-riemann]]<br>*See:* `derivations/small-loop-law-from-transport`, `worked_examples/unit-sphere-cell`

### 5. Whole loops as transformations · formal · calculation

*What is the holonomy of a finite loop, and what kind of transformation can it be?*

The parallelogram derivation multiplies four step matrices. Chop a finite loop $\gamma$ into many short steps and multiply all their matrices in order. The limit is the holonomy of $\gamma$, a linear map $\mathrm{Hol}(\gamma): T_pM \to T_pM$ of the tangent space at the base point $p$. With connection matrices $(\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}$ it is the path-ordered exponential

$$\mathrm{Hol}(\gamma) = \mathcal{P}\exp\Big(-\oint_\gamma \Gamma_\mu\,dx^\mu\Big),$$

where later points of the loop act after earlier ones, for a loop inside one coordinate chart. Changing the basis at $p$, or moving the base point along the loop, conjugates this matrix and leaves its invariants, such as a rotation angle, unchanged.

The Levi-Civita connection satisfies $\nabla g = 0$, so transport preserves inner products and $\mathrm{Hol}(\gamma)$ lies in the orthogonal group of $g_p$. On an oriented surface that group is $SO(2)$: every holonomy is a rotation by an angle defined modulo $2\pi$. On an oriented, time-oriented spacetime it is a proper orthochronous Lorentz transformation in $SO^+(1,3)$.

In two dimensions all rotations commute, so the ordering in $\mathcal{P}$ drops out, and the holonomy of a simple loop bounding a smooth region is exactly the rotation by $\iint K\,dA$. In three or more dimensions the ordering matters. The exact finite-loop statement, the non-abelian Stokes theorem, is a surface-ordered exponential of curvature transported back to $p$; the plain exponential of the integrated curvature is only its leading-order approximation.

For a small loop that flows a parameter distance $\epsilon$ along vector fields $u$ and then $v$ and back, $\mathrm{Hol} = 1 - \epsilon^2\,\mathcal{R}(u,v) + O(\epsilon^3)$. Here $\mathcal{R}(u,v) = [\nabla_u,\nabla_v] - \nabla_{[u,v]}$ has components $R^\rho{}_{\sigma\mu\nu}u^\mu v^\nu$. When $[u,v] \neq 0$ the loop needs a short extra closing leg, whose effect is the $\nabla_{[u,v]}$ term. The Riemann tensor is thus a linear map from oriented 2-planes to generators of metric-preserving transformations.

**Takeaway:** Holonomy is the path-ordered product of transport steps; for the Levi-Civita connection it is a rotation or Lorentz transformation, and curvature is its infinitesimal form.

*Picture:* At a point p, the circle of unit tangent directions; each loop through p acts on it as a rotation, and small loops give rotations linear in the loop's oriented area element.

*What this leaves out:* Restricted to the Levi-Civita connection; holonomy is defined for any connection on any vector bundle, where it need not preserve a metric.

*Gist:* The holonomy of a finite loop is the ordered product of all the small transport steps around it, a path-ordered exponential of the connection. Because lengths and angles are preserved, it is a rotation, or a Lorentz transformation in spacetime.<br>*Continues:* `ways_in/shrink-the-loop-to-find-riemann`<br>*Builds on:* [[levi-civita-connection]], [[lie-bracket]]<br>*See:* `worked_examples/latitude-circle-as-matrix-exponential`, `problems/small-loop-change-is-a-rotation`

### 6. Loops around tips and holes · formal · contrast

*Can a loop return a vector turned where there is no curvature at all?*

Make a cone by cutting a wedge of angle $\delta$ out of a flat sheet and gluing the cut edges together. Away from the tip the cone is flat: its Gaussian curvature is zero, and a small loop there returns vectors unchanged. Now carry a vector once around the tip. Unroll the cone. The loop becomes a path from one cut edge to the other, the vector slides rigidly along it, and gluing the edges back rotates it by $\delta$, in the same sense as the circulation. A loop that winds $n$ times around the tip returns a rotation by $n\delta$.

This separates two ideas that the small-loop law ties together. The restricted holonomy group $\mathrm{Hol}^0_p$, built from loops that can be shrunk to a point, is trivial on a connected region exactly when $R = 0$ there. The full holonomy group $\mathrm{Hol}_p$ also contains loops that cannot be shrunk, and those can transform vectors in a flat region: around the cone's missing tip, or along a flat Möbius band, where a loop along the band returns a reflection. The cone's tip carries a concentrated curvature: a disk around it contributes $\delta$ to the local Gauss–Bonnet sum, in the limit of rounding off the tip.

The same structure appears in gravity. Outside an idealized, infinitely thin, straight cosmic string of mass per unit length $\mu$, spacetime is locally flat, yet vectors carried around the string return rotated, in the plane perpendicular to it, by the deficit angle $8\pi G\mu/c^2$. Regge calculus builds curved spacetimes from flat pieces on the same principle, with all curvature carried by deficit angles.

**Try it:** Make a cone from paper with a quarter-circle wedge removed, draw a loop around the tip, and slide a matchstick along it; then unroll the paper to see where the turn comes from.

**Takeaway:** Zero curvature guarantees an unturned return only for loops that can be shrunk to a point; loops around tips or holes can still turn vectors.

*Picture:* A paper cone beside its unrolled sheet with the wedge missing. A loop around the tip becomes a path between the two cut edges; the vector slides unchanged, and the glued seam adds the wedge angle.

*What this leaves out:* Idealizes the tip as a point and the string as infinitely thin.

*Gist:* Yes, when the loop cannot be shrunk to a point without crossing a tip or a hole. On a paper cone, a loop winding once around the tip returns vectors turned by the missing wedge's angle, although the paper is flat.<br>*Continues:* `ways_in/whole-loops-as-transformations`<br>*Visuals:* [[paper-cone-with-a-missing-wedge]]<br>*See:* `checks/cone-with-a-missing-wedge`

## Glossary

| Term | Say | In plain words |
| --- | --- | --- |
| loop | — | A path that ends exactly where it began. |
| swing | — | To turn the arrow to the left or right along the ground. The rule of the arrow test is that the arrow never swings. |
| walk straight | — | On a ball, walking without ever steering left or right, like following a line drawn from top to bottom on a globe. |
| holonomy | ho-LON-uh-mee | The turn between an arrow's starting direction and its direction after being carried once around a loop, never swinging. |
| intrinsic curvature | in-TRIN-zik | Curving built into a surface, which someone living on it can detect without looking from outside. A ball has it. A rolled-up paper tube does not. |

## Key equations

### Area rule on a sphere · working

$$
\Delta\alpha = \frac{A}{a^2} \pmod{2\pi}
$$

On a sphere, the turn of an arrow carried around a loop is the enclosed area measured in units of the radius squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta\alpha$ | turn of the returned arrow, in radians, positive in the sense of the walk | the turn |
| $A$ | area of the region on the walker's left | the fenced-off area |
| $a$ | radius of the sphere | the radius |

**Holds when:** Simple loop on a sphere of radius $a$; region on the walker's left; the turn is defined modulo $2\pi$.  
**Say it:** “The turn, in radians, is the fenced-off area divided by the radius squared.”  
**Justified by:** `stated`

### Area rule on any surface (local Gauss–Bonnet) · working

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

On any two-dimensional surface, the turn around a loop equals the total Gaussian curvature it encloses.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S$ | the region on the walker's left | the fenced-off region |
| $K$ | Gaussian curvature at each point of $S$ | the Gaussian curvature |
| $dA$ | an element of area | a small piece of area |

**Holds when:** Oriented smooth surface with its Levi-Civita connection; a simple, piecewise-smooth loop bounding a region $S$ that contains no cone points or holes; positive turn in the sense of the walk; exact for any size; modulo $2\pi$.  
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
| $\Gamma_\mu$ | connection matrices built from the Christoffel symbols | the connection matrices |

**Holds when:** Piecewise-smooth loop inside one coordinate chart (otherwise include transition matrices); the matrix depends on the basis at the base point, and on the base point along the loop, only by conjugation.  
**Say it:** “The holonomy is the path-ordered exponential of minus the connection, taken around the loop.”  
**Justified by:** `stated`

## Derivations

### The small-loop law from the transport equation · working

**Goal:** Show that walking a coordinate parallelogram $+a, +b, -a, -b$ changes a vector by $-R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$.

1. Carrying a vector without swinging it obeys $\frac{dV^\rho}{ds} = -\Gamma^\rho{}_{\mu\sigma}\frac{dx^\mu}{ds}V^\sigma$. In matrix form, $\frac{dV}{ds} = -\Gamma_{\dot x}V$, with $(\Gamma_e)^\rho{}_\sigma \equiv \Gamma^\rho{}_{\mu\sigma}e^\mu$.
2. For one short straight step $e$ from a point $x$, with $s$ running from 0 to 1, expand to first order along the step: $\Gamma_e(x + se) = \Gamma_e + s\,\partial_e\Gamma_e$, where $\partial_e\Gamma_e \equiv e^\nu\partial_\nu\Gamma_e$ and everything on the right is evaluated at $x$.
3. Integrate the matrix equation, keeping terms of second order in $e$. The step multiplies $V$ by $P_e(x) = 1 - \Gamma_e - \tfrac12\partial_e\Gamma_e + \tfrac12\Gamma_e\Gamma_e$.
4. The four steps start at $x$, $x+a$, $x+a+b$ and $x+b$. Expand each connection matrix about $x$: $\Gamma_b(x+a) = \Gamma_b + \partial_a\Gamma_b$, $\Gamma_{-a}(x+a+b) = -(\Gamma_a + \partial_a\Gamma_a + \partial_b\Gamma_a)$, and $\Gamma_{-b}(x+b) = -(\Gamma_b + \partial_b\Gamma_b)$.
5. Write the four step matrices to second order: $P_1 = 1 - \Gamma_a - \tfrac12\partial_a\Gamma_a + \tfrac12\Gamma_a^2$, $P_2 = 1 - \Gamma_b - \partial_a\Gamma_b - \tfrac12\partial_b\Gamma_b + \tfrac12\Gamma_b^2$, $P_3 = 1 + \Gamma_a + \tfrac12\partial_a\Gamma_a + \partial_b\Gamma_a + \tfrac12\Gamma_a^2$, and $P_4 = 1 + \Gamma_b + \tfrac12\partial_b\Gamma_b + \tfrac12\Gamma_b^2$.
6. Multiply $P_4P_3P_2P_1$. The first-order terms cancel: $-\Gamma_a - \Gamma_b + \Gamma_a + \Gamma_b = 0$.
7. Collect the derivative terms. $\partial_a\Gamma_a$ appears as $-\tfrac12 + \tfrac12$ and $\partial_b\Gamma_b$ as $-\tfrac12 + \tfrac12$, so both cancel. What survives is $\partial_b\Gamma_a - \partial_a\Gamma_b$.
8. Collect the products of first-order terms, with each later factor on the left: $\Gamma_b\Gamma_a - \Gamma_a^2 - \Gamma_a\Gamma_b - \Gamma_b\Gamma_a - \Gamma_b^2 + \Gamma_b\Gamma_a$. Adding the four $\tfrac12\Gamma^2$ terms, which total $\Gamma_a^2 + \Gamma_b^2$, leaves $\Gamma_b\Gamma_a - \Gamma_a\Gamma_b$.
9. Second derivatives of $\Gamma$ and triple products enter only at third order. So to second order, $\Delta V^\rho = a^\mu b^\nu\big(\partial_\nu\Gamma^\rho{}_{\mu\sigma} - \partial_\mu\Gamma^\rho{}_{\nu\sigma} + \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}\big)V^\sigma$.
10. The course definition is $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. The bracket in the previous step is exactly its negative.

**Result:** $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, with corrections of third order in the loop size.

## Worked examples

### Around the 45th parallel · working

**Problem:** An arrow is carried once eastward around the circle of latitude 45° north on a sphere. By what angle does it return turned?

1. Latitude 45° north means colatitude $\theta_0 = 45^\circ$, measured down from the North Pole.
2. Walking east, the polar cap is on the walker's left. Its area is $2\pi a^2(1-\cos 45^\circ) = 2\pi a^2 \times 0.2929$.
3. Divide by $a^2$: the turn is $2\pi \times 0.2929 = 1.840$ rad.
4. In degrees, $1.840 \times 57.30 = 105.4^\circ$, in the same sense as the walk.

**Answer:** $1.840$ rad, about $105^\circ$.

**Takeaway:** A circle of latitude is not a geodesic, yet the area rule still gives its turn exactly.

### A small cell on the unit sphere · working

**Problem:** On the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, carry $V = e_\theta$ around a small cell walked $+\delta\theta$, $+\delta\phi$, $-\delta\theta$, $-\delta\phi$. Find the change and compare it with the cell's area.

1. The nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$.
2. With the course definition, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, so $R_{\theta\phi\theta\phi} = \sin^2\theta$.
3. Antisymmetry in the first pair gives $R_{\phi\theta\theta\phi} = -\sin^2\theta$. Raising with $g^{\phi\phi} = 1/\sin^2\theta$ gives $R^\phi{}_{\theta\theta\phi} = -1$.
4. Apply the small-loop law with $a^\theta = \delta\theta$, $b^\phi = \delta\phi$ and $V^\theta = 1$: $\Delta V^\phi = -R^\phi{}_{\theta\theta\phi}\,\delta\theta\,\delta\phi = +\delta\theta\,\delta\phi$. $\Delta V^\theta = 0$, because $R_{\theta\theta\theta\phi} = 0$.
5. The basis vector $e_\phi$ has length $\sin\theta$, so the unit vector $e_\theta$ tilts toward $e_\phi$ by the angle $\sin\theta\,\delta\theta\,\delta\phi$.
6. The cell's area is $\sin\theta\,\delta\theta\,\delta\phi$, and $K = 1$, so the area rule predicts the same angle. Seen from outside the sphere, the rotation from $e_\theta$ toward $e_\phi$ has the same sense as the walk around the cell.

**Answer:** $\Delta V = \delta\theta\,\delta\phi\;e_\phi$: a rotation by $\sin\theta\,\delta\theta\,\delta\phi$, equal to the enclosed area, in the sense of the walk.

**Takeaway:** The index formula and the area picture agree in size and in sense, which checks the sign convention.

### A latitude circle as a matrix exponential · formal

**Problem:** Compute the holonomy of the circle at colatitude $\theta_0$ on the unit sphere, walked eastward, directly from the path-ordered exponential.

1. Parametrize the circle by $\phi \in [0, 2\pi]$. Only $dx^\phi/d\phi = 1$ is nonzero.
2. The transport equation gives $\frac{dV^\theta}{d\phi} = -\Gamma^\theta{}_{\phi\phi}V^\phi = \sin\theta_0\cos\theta_0\,V^\phi$ and $\frac{dV^\phi}{d\phi} = -\Gamma^\phi{}_{\phi\theta}V^\theta = -\cot\theta_0\,V^\theta$.
3. Use orthonormal components $x = V^{\hat\theta} = V^\theta$ and $y = V^{\hat\phi} = \sin\theta_0\,V^\phi$. Then $\frac{dx}{d\phi} = \cos\theta_0\,y$ and $\frac{dy}{d\phi} = -\cos\theta_0\,x$, so the connection matrix is constant along the loop.
4. A constant matrix commutes with itself, so path ordering is irrelevant and the holonomy is an ordinary matrix exponential. Starting from $(x, y) = (1, 0)$, the solution is $(\cos(\phi\cos\theta_0), -\sin(\phi\cos\theta_0))$. After one lap this is a rotation by $-2\pi\cos\theta_0$ in the $(\hat\theta, \hat\phi)$ basis.
5. Seen from outside the sphere, turning from $\hat\theta$ (south) toward $\hat\phi$ (east) is counterclockwise. So the holonomy is a clockwise rotation by $2\pi\cos\theta_0$.
6. Modulo $2\pi$, a clockwise rotation by $2\pi\cos\theta_0$ is the same rotation as a counterclockwise one by $2\pi(1 - \cos\theta_0)$. That is the area rule for the polar cap on the walker's left, with the counterclockwise sense matching the walk.

**Answer:** A clockwise rotation by $2\pi\cos\theta_0$, the same rotation as a counterclockwise turn by $2\pi(1-\cos\theta_0)$. At $\theta_0 = 45^\circ$ that is $254.6^\circ$ clockwise, or $105.4^\circ$ counterclockwise.

**Takeaway:** Both forms describe one rotation. The clockwise form, $2\pi\sin(\text{latitude})$, is exactly the Foucault pendulum's daily turn against local north.

## Problems

### `equator-walk` · entry · difficulty 1 · conceptual

You walk once all the way around the equator of a smooth ball, keeping an arrow flat and pointing straight ahead the whole time, never letting it swing. When you are back at the start, does the arrow point the way it did when you set off? Does this mean the ball is not curved after all?

**Hints**

1. Where does the arrow point at every moment of this walk?
2. Does the walk from the North Pole still bring its arrow back turned?

**Answer:** The arrow comes back pointing the same way. This does not mean the ball is flat: some loops happen to bring the arrow back matching, but the walk from the North Pole still returns it a quarter turn away.

**Solution**

1. On the equator you walk straight the whole time, with no corners.
2. The arrow points straight ahead at the start, and because it never swings on a straight walk, it points straight ahead the whole way.
3. Back at the start you are walking the same way as when you set off, so the arrow points the same way too.
4. One matching loop does not make the ball flat. The walk from the North Pole to the equator and back still brings its arrow back turned by a quarter turn, which never happens on a flat table.

### `earth-loop-size` · working · difficulty 1 · estimate

Treat Earth as a sphere of radius 6371 km. A loop on its surface returns a carried arrow turned by 1°. How large an area does the loop enclose, and how does that compare with France, about 550,000 km²?

**Hints**

1. Convert 1° to radians.
2. Use the area rule on a sphere and solve for the area.

**Answer:** About $7.1\times10^{5}$ km², roughly 1.3 times the area of France.

**Solution**

1. $1^\circ = \pi/180 = 0.017453$ rad.
2. The area rule $\Delta\alpha = A/a^2$ gives $A = \Delta\alpha\,a^2$.
3. $a^2 = (6371\ \text{km})^2 = 4.0590\times10^{7}$ km².
4. $A = 0.017453 \times 4.0590\times10^{7} = 7.08\times10^{5}$ km², and $7.08\times10^{5}/5.5\times10^{5} \approx 1.3$.

### `saddle-sign` · working · difficulty 2 · calculation

Near its centre, a saddle-shaped surface has Gaussian curvature $K \approx -1/R^2$. A small simple loop there encloses area $A \ll R^2$ and is walked counterclockwise as seen from above, with the region on the walker's left. Find the turn and its sense.

**Hints**

1. Use the local Gauss–Bonnet rule with a nearly constant $K$.

**Answer:** $\Delta\alpha \approx -A/R^2$: a turn of size $A/R^2$, clockwise, against the sense of the walk.

**Solution**

1. For a small region, $K$ is nearly constant, so $\iint_S K\,dA \approx K A$.
2. With $K \approx -1/R^2$, $\Delta\alpha \approx -A/R^2$.
3. A negative turn means opposite to the sense of the walk, so the arrow turns clockwise as seen from above.

### `small-loop-change-is-a-rotation` · formal · difficulty 2 · proof

Using the small-loop law for the Levi-Civita connection, show that $V_\rho\,\Delta V^\rho = 0$ for every vector $V$. Explain why this makes the holonomy of a small loop an infinitesimal rotation or boost.

**Hints**

1. Lower the first index of the Riemann tensor.
2. Which symmetry does $R_{\rho\sigma\mu\nu}$ have in its first two indices?

**Answer:** $V_\rho\,\Delta V^\rho = -R_{\rho\sigma\mu\nu}V^\rho V^\sigma a^\mu b^\nu = 0$, because $R_{\rho\sigma\mu\nu}$ is antisymmetric in $\rho\sigma$. The generator $-R_{\rho\sigma\mu\nu}a^\mu b^\nu$ is therefore an antisymmetric bilinear form, an element of the Lie algebra of the metric's orthogonal or Lorentz group.

**Solution**

1. Contract the small-loop law with $V_\rho$: $V_\rho\,\Delta V^\rho = -R_{\rho\sigma\mu\nu}V^\rho V^\sigma a^\mu b^\nu$.
2. For a metric-compatible connection, $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$, while $V^\rho V^\sigma$ is symmetric, so the contraction vanishes.
3. Write the holonomy as $1 + \Omega$ with $\Omega^\rho{}_\sigma = -R^\rho{}_{\sigma\mu\nu}a^\mu b^\nu$. The lowered form $\Omega_{\rho\sigma}$ is antisymmetric.
4. A linear map $1 + \Omega$ preserves $g$ to first order exactly when $\Omega_{\rho\sigma} + \Omega_{\sigma\rho} = 0$. So $\Omega$ lies in the Lie algebra of $SO(n)$ on a Riemannian manifold or $SO(1,3)$ in spacetime: an infinitesimal rotation or boost.

## Observations

- **Geodetic precession of gyroscopes orbiting Earth, measured by Gravity Probe B** (measured, working). A gyroscope in free fall carries its spin axis without swinging it: the spacetime version of the arrow rule. After each polar orbit, about 642 km above Earth, the spin axis comes back turned by a tiny angle. In the standard post-Newtonian description, two thirds of that turn is the holonomy of curved space around the orbit, and one third comes from the gyroscope's motion through Earth's gravitational field. *Numbers:* Predicted $6606.1$ milliarcseconds per year; measured $6601.8 \pm 18.3$ milliarcseconds per year. *Reference:* C. W. F. Everitt, et al. (2011), *Gravity Probe B: Final Results of a Space Experiment to Test General Relativity*, Physical Review Letters 106, 221101, doi:10.1103/PhysRevLett.106.221101 _(unverified)_
- **The slow turning of a Foucault pendulum's swing plane** (analogue, working). Earth turns eastward, so seen from above the North Pole the pendulum is carried counterclockwise around its circle of latitude once per sidereal day. For slow rotation and small swings, the swing plane obeys the arrow rule on Earth's surface. The holonomy of that circle is a counterclockwise turn by $2\pi(1-\cos\theta_0) = 2\pi(1-\sin\lambda)$, where $\lambda$ is the latitude. Modulo $2\pi$ this is the same rotation as a clockwise turn by $2\pi\sin\lambda$, which is exactly the pendulum's observed turn against local north per sidereal day. The physical cause is Earth's rotation; the sphere enters as the set of directions the local vertical takes around the lap, and spacetime curvature plays no role. *Numbers:* At latitude $48.85^\circ$ north (Paris), $360^\circ\sin\lambda = 271^\circ$ per sidereal day, about $11.3^\circ$ per hour.

## Teaching arc

1. **Ask the insider question** (entry). Ask how someone who can never leave a ball, or look at it from above, could find out that it is curved. *Why:* It frames holonomy as a measurement made from inside, the only kind available for the universe.
2. **Show one surprise and two controls** (entry). Run the North Pole walk after the learner predicts, then a square walk on a flat floor, then a bracelet loop on a tube that unrolls. *Why:* The controls rule out the corners and mere bending as explanations. *Predict:* When the arrow gets back to the North Pole, will it point the way it did when you set off? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `octant`)
3. **Discover the area rule** (working). Resize and reverse the loop and change the ball's radius; tabulate the turn against area over radius squared before naming angular excess. *Why:* Learners find proportionality, the sign flip, and the role of the radius themselves. *Predict:* If the loop fences off half as much of the ball, what happens to the turn? *Visual:* [[carry-an-arrow-around-a-loop]] (preset `octant-half-area`)
4. **Shrink the loop to reach the Riemann tensor** (working). Derive the small-loop law and read off linearity, antisymmetry, and area scaling. *Why:* Each feature of the formula explains a slot of the Riemann tensor. *Predict:* If you swap the order of the two edges, what happens to the change in the vector? *Visual:* [[shrink-the-loop-to-find-riemann]]
5. **Check the sign two ways** (working). Work the unit-sphere cell, then ask about polar coordinates on a flat plane. *Why:* It fixes the sign convention and separates curved coordinates from curved space.
6. **Mark the limits** (formal). Carry a vector around the tip of a paper cone, then state what zero curvature does and does not guarantee. *Why:* It prevents the belief that flatness along a loop always means no turn. *Predict:* Every patch of this cone away from the tip is flat. Will a loop around the tip bring the arrow back unturned? *Visual:* [[paper-cone-with-a-missing-wedge]]
7. **Transfer to physics** (formal). Connect to the orbiting gyroscope and to the charged-particle phase around a loop. *Why:* Holonomy becomes the shared language of gravity and gauge fields.

## Analogies

### Polarization in a coiled optical fibre · working

Light guided through a gently coiled single-mode fibre, whose exit direction matches its entry direction, has a direction of travel that traces a closed loop on the sphere of directions. Its polarization is carried along without swinging and comes back rotated by the solid angle that loop encloses, defined modulo $2\pi$. This holds when stress-induced birefringence in the fibre is negligible.

| In the analogy | Stands for |
| --- | --- |
| the sphere of propagation directions | the curved surface |
| the polarization direction | the carried arrow |
| the enclosed solid angle | the enclosed curvature, $\iint K\,dA$ on the unit sphere |

*Limits:* The sphere is a space of directions, not physical space; the effect is a geometric phase in optics, and gravity plays no role.

### A charged particle's phase around a loop · formal

A charged quantum field carried around a loop is multiplied by $\exp\big(+i(q/\hbar)\oint A_\mu dx^\mu\big)$ in the course convention, a phase set by the enclosed magnetic flux $\Phi$: $q\Phi/\hbar$. For a small loop the phase is governed by the field strength $F_{\mu\nu}$, which plays the role the Riemann tensor plays for vectors. The Aharonov–Bohm setup, with no field on the path itself, is the gauge-field twin of the cone: holonomy without local field strength.

| In the analogy | Stands for |
| --- | --- |
| the phase of the wavefunction | the direction of the carried arrow |
| the electromagnetic potential $A_\mu$ | the connection |
| the field strength $F_{\mu\nu}$ | the Riemann tensor |

*Limits:* Phases commute, so their ordering around the loop never matters; rotations of vectors in three or more dimensions do not commute. The phase lives in an internal space, with no metric and no boosts.

## Misconceptions

### “If I never let the arrow swing, it cannot come back turned.” · entry · `never-swung-so-never-turned`

- **Why it is tempting:** On a flat floor, an arrow that never swings keeps pointing at the same wall forever.
- **What is true:** The rule tells you what to do at each small step. It does not promise where the arrow points after a long trip. On the North Pole walk, follow every step: straight ahead, then to your right, then behind you. Back at the pole, behind you along the last path is a quarter turn away from ahead along the first path.
- **Exposed by:** `checks/octant-walk-prediction`

### “The arrow turned because I turned at the corners.” · entry · `corners-caused-the-turn`

- **Why it is tempting:** The walker makes visible turns, and the arrow ends up pointing a new way.
- **What is true:** Your body turned at the corners, but the arrow never did. A square walk on a flat floor also has four corners, and there the arrow comes back unchanged. So the corners alone cannot turn the arrow.
- **Exposed by:** `checks/square-on-a-floor`

### “A tube looks curved, so an arrow carried around a loop on it must come back turned.” · entry · `tube-must-turn`

- **Why it is tempting:** From outside, the tube looks bent.
- **What is true:** A tube unrolls into a flat sheet without stretching, and unrolling changes no angle drawn on it. So every loop on the tube brings the arrow back unchanged. The arrow test only notices curving that cannot be unrolled flat, like a ball's.
- **Exposed by:** `checks/loop-around-a-tube`

### “It does not matter which way I walk around the loop.” · entry · `direction-does-not-matter`

- **Why it is tempting:** The patch fenced off is the same either way.
- **What is true:** Walking the loop the other way is the first trip played backwards. The forwards trip followed by the backwards trip must bring the arrow back exactly to its start. So if one direction turns the arrow to the left, the other direction turns it to the right by the same amount.
- **Exposed by:** `checks/reverse-the-loop`

### “If the surface is flat everywhere along my loop, the arrow cannot come back turned.” · working · `flat-along-loop-means-no-turn`

- **Why it is tempting:** The small-loop law makes holonomy look like a local sum of curvature along the path.
- **What is true:** Flatness guarantees no turn only for loops that can be shrunk to a point without leaving the flat region. A loop around the tip of a paper cone crosses only flat paper, yet it returns turned by the missing wedge's angle.
- **Exposed by:** `checks/cone-with-a-missing-wedge`

### “Halfway around, I can see how much the arrow has turned so far.” · working · `running-angle-halfway`

- **Why it is tempting:** Animations show the arrow's direction in the room changing continuously, which invites a running angle.
- **What is true:** Arrows at different places on a curved surface can be compared only by carrying one to the other, and different routes give different answers. The turn is defined only when the loop closes and both arrows sit at the same point.
- **Exposed by:** `checks/halfway-readout`

## Checks

1. **Entry · predict** `checks/octant-walk-prediction`. Picture a giant smooth ball. Start at the North Pole and walk straight to the equator. Turn left and walk a quarter of the way around the equator. Then turn left and walk straight back to the North Pole. You carry a flat arrow that points straight ahead at the start and never swings. Back at the North Pole, does the arrow point the same way it did when you set off? If not, how far apart are the two directions?
   - **Hints:** Where does the arrow point just after the first left turn? / Where does it point after the second left turn?
   - **Answer:** No. On the first stretch the arrow points ahead. At the equator you turn left but the arrow does not swing, so it points to your right. At the next corner you turn left again, so it points behind you. Behind you along the last path is a right angle away from ahead along the first path. That is because the two paths start a quarter of the way around the equator from each other. So the arrow comes back a quarter turn away from its start.
   - **Must contain:** The arrow does not come back pointing the same way; It points ahead, then right, then behind; The first and last paths meet at the North Pole at a right angle; The difference is a quarter turn
   - **Numeric:** turn = 90 deg (±5%)
   - **Targets:** `never-swung-so-never-turned`
2. **Entry · predict** `checks/square-on-a-floor`. On a flat floor, you walk a square, turning left by a quarter turn at each of its four corners. You carry a flat arrow that points straight ahead at the start and never swings. Back at the start, which way does the arrow point?
   - **Hints:** Pick the wall the arrow points at when you start.
   - **Answer:** The same way it pointed at the start. Because the arrow never swings, it keeps pointing at the same wall of the room the whole time. Your body turned four times, but the arrow did not. So turning at corners cannot by itself turn the arrow.
   - **Must contain:** It points the same way as at the start; The arrow keeps pointing at the same wall; Corners turn the walker, not the arrow
   - **Targets:** `corners-caused-the-turn`
3. **Entry · explain** `checks/loop-around-a-tube`. Roll a sheet of paper into a tube. You walk once around the tube, like a bracelet around a wrist, carrying a flat arrow that never swings. Back at the start, does the arrow point the same way it did when you set off? Why?
   - **Hints:** What does the tube become when you unroll it?
   - **Answer:** Yes. Unroll the tube and it becomes a flat sheet with nothing stretched. Your loop becomes a straight line across the sheet, and on flat paper the arrow never changes direction. The two ends of that line were glued together in the tube, so the arrow comes back matching its start.
   - **Must contain:** Yes, it points the same way; The tube unrolls flat without stretching; On the flat sheet the arrow never changes direction
   - **Targets:** `tube-must-turn`
4. **Entry · predict** `checks/reverse-the-loop`. On a ball, you walk a small loop, turning left at each corner, with an arrow that never swings. The arrow comes back turned 5 degrees to the left. You set the arrow back to its starting direction, then walk the same loop the other way, turning right at each corner. How does the arrow come back?
   - **Hints:** What happens if you do the first trip and then the second trip, one after the other?
   - **Answer:** Turned 5 degrees to the right. The second trip is the first trip played backwards. Doing the first trip and then the backwards trip would bring the arrow exactly back to its start. The first trip turned it 5 degrees left, so the backwards trip must turn it 5 degrees right.
   - **Must contain:** Turned by the same amount; In the opposite direction, to the right; The backwards trip undoes the forwards trip
   - **Numeric:** turn to the right = 5 deg (±5%)
   - **Targets:** `direction-does-not-matter`
5. **Working · numeric** `checks/triangle-on-a-big-sphere`. A triangle of great-circle arcs on a sphere of radius 1000 km has angles of 100°, 60° and 50°. By how much does an arrow carried around it turn, and what is the triangle's area?
   - **Hints:** Compare the angle sum with 180°. / Convert the excess to radians before using the area rule.
   - **Answer:** The angles sum to 210°, so the angular excess is 30°, or $\pi/6$ rad, and that is the turn. By the area rule, the area is $(\pi/6)(1000\ \text{km})^2 \approx 5.24\times10^{5}$ km².
   - **Must contain:** Angle sum 210 degrees; Turn equals the excess, 30 degrees; Area equals the turn in radians times the radius squared
   - **Numeric:** turn = 0.5236 rad (±1%); area = 523600 km^2 (±1%)
6. **Working · numeric** `checks/latitude-30-north`. An arrow is carried once eastward around the circle of latitude 30° north on a sphere. By what angle does it return turned?
   - **Hints:** Measure the angle down from the North Pole.
   - **Answer:** The colatitude is 60°. The polar cap on the walker's left has area $2\pi a^2(1-\cos 60^\circ) = \pi a^2$, so the turn is $\pi a^2/a^2 = \pi$: a half turn.
   - **Must contain:** Colatitude 60 degrees; Cap area is pi times the radius squared; The turn is a half turn
   - **Numeric:** turn = 3.1416 rad (±1%)
7. **Working · evaluate-claim** `checks/halfway-readout`. A demo shows the arrow halfway around the North Pole loop, with a readout saying 'turned 45° so far'. Evaluate the readout.
   - **Hints:** Relative to what would the 45° be measured?
   - **Answer:** The readout has no meaning as a holonomy. On a curved surface, arrows at different points can be compared only by carrying one to the other, and different routes give different answers. The turn is defined when the loop closes, where the starting arrow and the returned arrow sit at the same point. An angle measured against a local reference, such as the path or a compass direction, is a different, reference-dependent quantity.
   - **Must contain:** Arrows at different points have no route-independent comparison; The turn is defined only when the loop closes; A running angle depends on an arbitrary local reference
   - **Targets:** `running-angle-halfway`
8. **Formal · explain** `checks/polar-coordinates-plane`. In polar coordinates on a flat plane, $\Gamma^r{}_{\phi\phi} = -r$ is not zero. Does a small loop there return vectors turned?
   - **Hints:** Which object appears in the small-loop law?
   - **Answer:** No. The small-loop law sets the change by the Riemann tensor, which vanishes for the flat metric $dr^2 + r^2 d\phi^2$. Nonzero Christoffel symbols describe curved coordinate lines, not curved space.
   - **Must contain:** No turn; Holonomy is governed by the Riemann tensor, not the Christoffel symbols; The plane's Riemann tensor is zero
9. **Formal · evaluate-claim** `checks/cone-with-a-missing-wedge`. A cone is made by removing a 90° wedge from paper. A student says: 'every patch of the cone away from the tip is flat, so every loop gives zero holonomy.' Evaluate the claim.
   - **Hints:** Unroll the cone and follow the loop across the seam.
   - **Answer:** It is true only for loops that do not go around the tip. A loop winding once around the tip returns vectors turned by 90°, in the sense of the circulation. Unrolling shows why: the vector slides unchanged on the flat sheet, and gluing the wedge's edges imposes the rotation. Vanishing curvature along a loop guarantees trivial holonomy only for loops that can be shrunk to a point within the flat region.
   - **Must contain:** The claim fails for loops around the tip; The turn equals the wedge angle, 90 degrees; Only contractible loops in a flat region are guaranteed trivial holonomy
   - **Numeric:** turn = 90 deg (±1%)
   - **Targets:** `flat-along-loop-means-no-turn`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the small-loop law | Walking $+a, +b, -a, -b$ gives $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ with the course Riemann tensor. | Some texts walk the edges in the other order, or define the Riemann tensor with the opposite overall sign, and write $+R$. State the route and the Riemann convention together. |
| Sense and branch of the holonomy angle | Positive in the sense of circulation, with the enclosed region on the walker's left, modulo $2\pi$. | A clockwise rotation by $2\pi\cos\theta_0$ and a counterclockwise rotation by $2\pi(1-\cos\theta_0)$ are the same rotation, and the literature quotes either form. |
| Sign of a gauge phase | $D_\mu = \partial_\mu - i(q/\hbar)A_\mu$, so transport multiplies a charged field by $\exp\big(+i(q/\hbar)\oint A_\mu dx^\mu\big)$. | Texts that write $D_\mu = \partial_\mu + iqA_\mu$ flip the sign of the phase; some set $\hbar = 1$ or use Gaussian units. |

## Visuals

- ★ [[carry-an-arrow-around-a-loop]] (flagship): The central experience: the North Pole walk with flat-floor and tube controls, loops to resize and reverse, and a turn readout that appears only when the loop closes.
- [[shrink-the-loop-to-find-riemann]] (core): Connects the area picture to the Riemann tensor. *Sketch:* A coordinate parallelogram on a chosen 2D metric: a sphere patch, a saddle, or a polar-coordinate plane. The learner shrinks it with sliders and swaps the edge order. A log-log plot of the vector's change against the area shows slope one and converges to the small-loop law; the polar-coordinate plane stays at zero.
- [[paper-cone-with-a-missing-wedge]] (core): Shows holonomy without local curvature. *Sketch:* Cut a wedge of adjustable angle from a flat sheet and glue it into a cone. Loops that avoid the tip return the arrow unchanged; loops winding n times around the tip return it turned by n times the wedge angle. The unrolled sheet sits beside the cone, so the learner sees the arrow slide rigidly and the seam add the turn.
- [[arrow-around-a-circle-of-latitude]] (supporting): The area rule for a curve that is not a geodesic, and the link to the Foucault pendulum. *Sketch:* Drag the latitude and play one lap. Plot the returned turn against latitude in two equivalent forms, counterclockwise $2\pi(1-\sin\lambda)$ and clockwise $2\pi\sin\lambda$, and show that they are the same rotation. Overlay the Foucault pendulum's daily clockwise turn on the second form.
- [[cube-of-small-loops]] (supporting): Geometric picture of the second Bianchi identity. *Sketch:* A small cube whose six faces are walked as loops. Each face's rotation is carried to a common corner along the cube's edges. The sum cancels at third order in the cube's size, shown as a readout that shrinks faster than the cube.

## Tutor moves

**Open with**

- Picture a giant smooth ball. You walk a big triangle on it, holding an arrow flat on the ground and never letting it swing left or right. When you get back to where you started, will the arrow point the same way it did at the start? *(prediction)*
- If you could never leave the surface of a ball, or look at it from above, how could you find out that it is curved? *(reflection)*

**If the learner is stuck**

- *The learner loses track of where the arrow points during the walk.* → Replay the walk one stretch at a time, and have the learner say the arrow's direction relative to the path: ahead, right, behind.
- *The learner cannot find the area of a patch on a sphere.* → Use fractions of the whole sphere first: the North Pole triangle is one eighth of $4\pi a^2$. Postpone the cap formula.
- *The learner is lost in the index formula.* → Go to the unit-sphere cell, compute only $\Delta V^\phi$, and show that the angle equals the cell's area.
- *The learner asks for the angle partway around.* → Ask what the moving arrow would be compared with, then show that two routes to the halfway point give different answers.

**Common questions**

- *If I never let the arrow swing, where does the turn come from?* (entry) Follow the walk step by step: ahead, then to your right after the first corner, then behind you after the second. Each step obeys the rule. But on a ball, the three straight stretches meet at right angles at all three corners. On a flat table, a triangle's three corners always add up to half a turn, never three quarters. That extra quarter turn at the corners is where the arrow's turn comes from.
- *Why does this matter for gravity?* (entry) We live inside space and time, and nobody can look at them from outside. Tests from inside are how curving shows up. A spinning gyroscope carried around Earth in orbit comes back turned by a tiny angle, about five millionths of a full turn each year. A space experiment called Gravity Probe B measured it.
- *Does a bigger ball give a bigger turn?* (entry) It depends on what you keep the same. For a triangle with the same corner angles, no: on a bigger ball the triangle is bigger, and the turn stays the same. For a loop of the same size in kilometres, a bigger ball gives a smaller turn, because a bigger ball curves more gently.

**Switching levels**

- To working when: asks how big the turn is; starts using areas or angles as numbers. Go to the area rule and the North Pole triangle check.
- To formal when: is comfortable with index notation; asks whether the turn is always a rotation. Derive the small-loop law, then the path-ordered exponential and the cone.
- To research when: asks about groups of loops, discrete gravity, or quantum gravity. Open the research horizon: special holonomy, Regge calculus, and loop quantum gravity.

**Pronunciations:** Levi-Civita → LEH-vee CHEE-vee-tah; Gauss–Bonnet → GOWSS bon-AY; Riemann → REE-mahn; Aharonov–Bohm → ah-HAR-uh-nov BOHM; Regge → REJ-eh

**Voice notes:** Use degrees and fractions of a turn with beginners; switch to radians only once the area rule is on the table.

## History

- **Carl Friedrich Gauss (1827).** Showed that a surface's curvature can be measured from inside it, and related the angle sum of a geodesic triangle to the curvature it encloses. Presented in 1827 and published in 1828. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas* _(unverified)_
- **Pierre Ossian Bonnet (1848).** Extended Gauss's angle-sum result to regions bounded by arbitrary curves, giving the local Gauss–Bonnet theorem.
- **Tullio Levi-Civita (1917).** Defined parallel transport on Riemannian manifolds, first through an embedding in flat space, and used it to give Riemann's curvature a geometric meaning. Weyl and Schouten soon gave intrinsic formulations. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173–205 _(unverified)_
- **Élie Cartan (1926).** Introduced holonomy groups and made them a central tool of differential geometry. Élie Cartan (1926), *Les groupes d'holonomie des espaces généralisés*, Acta Mathematica 48, 1–42 _(unverified)_
- **Warren Ambrose, Isadore Singer (1953).** Proved that the Lie algebra of the holonomy group is spanned by curvature operators transported back to the base point. Warren Ambrose, Isadore M. Singer (1953), *A theorem on holonomy*, Transactions of the American Mathematical Society 75, 428–443 _(unverified)_

## Research horizon

- **Special holonomy.** Berger classified the possible holonomy groups of irreducible Riemannian manifolds that are not locally symmetric. Manifolds whose holonomy is a proper subgroup of $SO(n)$, such as Calabi–Yau threefolds with holonomy $SU(3)$ and $G_2$ manifolds, supply the extra dimensions of string and M-theory compactifications, because reduced holonomy is what leaves some supersymmetry unbroken. Marcel Berger (1955), *Sur les groupes d'holonomie homogène des variétés à connexion affine et des variétés riemanniennes*, Bulletin de la Société Mathématique de France 83, 279–330 _(unverified)_; Philip Candelas, Gary T. Horowitz, Andrew Strominger, Edward Witten (1985), *Vacuum configurations for superstrings*, Nuclear Physics B 258, 46–74 _(unverified)_
- **Discrete gravity.** Regge calculus builds spacetime from flat simplices glued together. All curvature sits on codimension-two hinges and is measured by deficit angles, which are the holonomies of small loops around the hinges. Causal dynamical triangulations use this construction to define a path integral for quantum gravity. Tullio Regge (1961), *General relativity without coordinates*, Il Nuovo Cimento 19, 558–571 _(unverified)_; Jan Ambjørn, Jerzy Jurkiewicz, Renate Loll (2004), *Emergence of a 4D world from causal quantum gravity*, Physical Review Letters 93, 131301, arXiv:hep-th/0404156 _(unverified)_
- **Loop quantum gravity.** Loop quantum gravity takes the holonomies of a connection along curves, rather than the metric, as its basic variables. Spin networks, graphs labelled by representations, give a basis of its quantum states. Abhay Ashtekar (1986), *New variables for classical and quantum gravity*, Physical Review Letters 57, 2244 _(unverified)_; Carlo Rovelli, Lee Smolin (1990), *Loop space representation of quantum general relativity*, Nuclear Physics B 331, 80–152 _(unverified)_; Carlo Rovelli (1998), *Loop quantum gravity*, Living Reviews in Relativity 1, 1, arXiv:gr-qc/9710008 _(unverified)_
- **Wilson loops.** In a non-abelian gauge theory, the holonomy of the gauge field around a loop changes by conjugation under gauge transformations, so its trace in a chosen representation, the Wilson loop, is gauge invariant. Wilson loops are basic observables of gauge theories, and an area-law fall-off of their expectation values diagnoses confinement. Kenneth G. Wilson (1974), *Confinement of quarks*, Physical Review D 10, 2445 _(unverified)_
