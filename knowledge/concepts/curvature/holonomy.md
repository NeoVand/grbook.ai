---
type: "concept"
schema_version: 2
id: "holonomy"
title: "Holonomy: the turn an arrow picks up around a loop"
domain: "curvature"
tier: "core"
aliases: ["holonomy of parallel transport", "loop holonomy", "holonomy group"]
prerequisites: ["path-dependence-of-parallel-transport", "gaussian-curvature", "angular-excess", "riemann-curvature-tensor"]
leads_to: ["flatness-criterion", "riemann-curvature-operator", "bianchi-identity", "gauge-field-strength", "cosmic-string"]
visuals: ["carry-an-arrow-around-a-loop", "shrink-the-loop-to-find-riemann", "paper-cone-with-a-missing-wedge", "arrow-around-a-circle-of-latitude", "cube-of-small-loops"]
review: {}
---

# Holonomy: the turn an arrow picks up around a loop

`holonomy` · curvature · core

**Needs:** [[path-dependence-of-parallel-transport]] (entry) · [[gaussian-curvature]] (working) · [[angular-excess]] (working) · [[riemann-curvature-tensor]] (working)  
**Opens:** [[flatness-criterion]] · [[riemann-curvature-operator]] · [[bianchi-identity]] · [[gauge-field-strength]] · [[cosmic-string]]  
**Related:** [[parallel-transport]] (the rule that is applied around the loop) · [[intrinsic-versus-extrinsic-curvature]] (holonomy detects only intrinsic curvature, which is why a rolled tube returns no turn) · [[curvature-of-the-two-sphere]] (the sphere is where the area law is easiest to verify) · [[gauge-parallel-transport]] (holonomy of a gauge connection is a phase or an internal rotation) · [[loop-quantum-gravity]] (uses holonomies of a connection along curves as its basic variables)  
**Visuals:** ★ [[carry-an-arrow-around-a-loop]] · [[shrink-the-loop-to-find-riemann]] · [[paper-cone-with-a-missing-wedge]] · [[arrow-around-a-circle-of-latitude]] · [[cube-of-small-loops]]

> Carry an arrow around a closed loop without ever turning it, then compare it with how it started. On a flat sheet it comes back unchanged. On a ball it comes back turned, and that turn is the loop's holonomy: a way to measure curving from the inside.

## Ways in

### 1. Walk a loop and check your arrow · entry

Imagine you are a tiny ant living on the surface of a huge ball. You can never leave the surface or look at the ball from outside. Can you still find out whether your world is flat, like a table, or curved, like a ball?

Here is a test. Hold a small arrow that lies flat along the ground. Walk along a path that ends exactly where it began. Such a path is called a closed loop. While you walk, obey one rule: never turn the arrow. You may turn your body at corners. The arrow keeps pointing the way it pointed a moment before. When you get back to the start, compare the arrow with the direction it had when you set off.

Try it on a flat table first. Walk a triangle, a square, or any shape you like. The arrow always comes back pointing exactly the way it started.

Now try it on the ball. Start at the North Pole, with the arrow pointing straight ahead along your path. Walk straight down to the equator. The arrow still points ahead of you, toward the south. At the equator, turn left and walk a quarter of the way around the ball. You turned, but the arrow did not. So it now points to your right, still toward the south. Turn left again and walk straight back up to the North Pole. The arrow still points south, which is now straight behind you.

Back at the pole, compare. When you left, the arrow pointed down your first path. Now it points back down your last path. Those two paths leave the pole at a right angle. So the arrow has turned by a quarter turn, even though you never turned it.

This turn is called the holonomy of the loop. A flat table never produces one. So if your arrow comes back turned, your world must be curved somewhere inside the loop. You found that out without ever leaving the surface.

The takeaway: an arrow carried around a loop without turning, and coming back turned, reveals curving from the inside.

*Picture:* A globe with a three-sided path from the North Pole down to the equator, a quarter of the way along it, and back up. The ant's arrow is drawn at the start (pointing down the first path) and at the finish (pointing down the last path), a right angle apart.

*What this leaves out:* The precise rule for 'never turn the arrow' is: along a straightest path, keep a fixed angle between the arrow and your direction of travel. The picture uses a two-dimensional surface, where the only possible change is a rotation; in spacetime a loop can also return a velocity-like change (a boost). A loop that cannot be shrunk to a point, for example around a hole, can return a turn even where the surface is flat; the cone in the formal way shows this.

*Builds on:* [[path-dependence-of-parallel-transport]] · *Visuals:* [[carry-an-arrow-around-a-loop]]

### 2. Bent is not the same as curved · entry

Roll a sheet of paper into a tube. From outside, the tube looks curved. Now let the ant repeat the arrow test on the tube.

Draw any loop on the tube and carry the arrow around it, never turning it. The arrow comes back unturned. Even a loop that goes all the way around the tube brings the arrow back unchanged.

Why? Unroll the tube. It becomes a flat sheet again, and nothing on it was stretched or squashed. Every path the ant walked becomes a path on flat paper. On flat paper the arrow never turns. So it did not turn on the tube either.

A ball is different. You cannot flatten a piece of orange peel without tearing or stretching it. That kind of curving can be detected from the inside, and it is called intrinsic curvature. Bending a flat sheet, as with the tube, does not create any.

The takeaway: the arrow test ignores how a surface is bent in the space around it. It responds only to curving that no bending can remove.

*Picture:* A paper tube next to its unrolled flat sheet, with the same loop drawn on both and the arrow returning unchanged on each.

*What this leaves out:* This covers surfaces. In spacetime there is no outside view to compare with, so intrinsic curvature is the only kind that matters.

*Visuals:* [[carry-an-arrow-around-a-loop]]

### 3. The turn equals the curving inside · working

Go back to the walk on the ball. The loop fenced in one eighth of the ball's surface, and the arrow turned by a quarter turn, $\pi/2$ radians. That is not a coincidence. For any loop on a sphere of radius $a$, the turn in radians is the enclosed area divided by $a^2$:
$$\Delta\alpha = \frac{A}{a^2}.$$
Check it: one eighth of the sphere's area $4\pi a^2$ is $\pi a^2/2$, and dividing by $a^2$ gives $\pi/2$.

On a general surface the curving varies from place to place. The amount at each point is the Gaussian curvature $K$: it equals $1/a^2$ everywhere on a sphere, and $0$ on a plane or a cylinder. The turn is the curvature added up over the enclosed region $S$:
$$\Delta\alpha = \iint_S K\,dA \pmod{2\pi}.$$
This holds exactly for loops of any size and any shape (the sides need not be straightest paths). It is the local form of the Gauss–Bonnet theorem. Where $K$ is positive the arrow turns the same way you walk around the loop; where $K$ is negative, as on a saddle, it turns the opposite way. Walking the loop in reverse reverses the turn.

Two special cases are worth knowing. For a triangle whose sides are straightest paths (geodesics), the turn equals its angular excess, the amount by which its three angles add up to more than $\pi$. The octant triangle has three right angles, so its excess is $3\pi/2 - \pi = \pi/2$, as found. For a circle of latitude at colatitude $\theta_0$ (the angle down from the North Pole), the enclosed cap has area $2\pi a^2(1-\cos\theta_0)$, so the turn is $2\pi(1-\cos\theta_0)$.

*Picture:* A sphere with a shaded region and its boundary loop; beside it, a small dial showing the returned arrow turned by an angle equal to the shaded area over the radius squared.

*What this leaves out:* The exact area rule is special to two dimensions, where every turn is a rotation about the same axis (the surface's normal). In higher dimensions rotations do not commute and only small loops obey a simple rule.

*Builds on:* [[gaussian-curvature]], [[angular-excess]] · *Visuals:* [[carry-an-arrow-around-a-loop]], [[arrow-around-a-circle-of-latitude]]

### 4. Shrink the loop and the Riemann tensor appears · working

In four-dimensional spacetime there is no single number like $K$. A small loop can lie in many different planes, and each plane can give a different answer. So shrink the loop to a tiny parallelogram with edge vectors $a^\mu$ and $b^\nu$. Walk $+a$, then $+b$, then $-a$, then $-b$, and ask how a vector $V$ changes. To second order in the loop's size the answer is
$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu,$$
where $R^\rho{}_{\sigma\mu\nu}$ is the Riemann curvature tensor in the course conventions. The derivation is given below. Read the formula feature by feature.

- It is linear in $V$. The loop acts on the vector like a matrix.
- It is linear in each edge. Double one side and the change doubles.
- It is antisymmetric in the edges. Swapping $a$ and $b$ walks the same parallelogram the other way round, and the change flips sign.
- It is proportional to the product of the edges. The change scales with the loop's area, just as $A/a^2$ did on the sphere.

So the Riemann tensor is a machine: feed it a small oriented patch of area (the pair of edges) and it returns a small rotation of vectors. Because transport preserves lengths and angles, that small change is always a rotation on a surface, or a small Lorentz transformation (rotation or boost) in spacetime. On a two-dimensional surface the machine reduces to one number: for a small cell of area $\delta A$ the turn is $K\,\delta A$.

*Picture:* A tiny parallelogram with edges a and b at a point. A vector V goes around it and returns as V plus a small extra arrow ΔV. Reversing the circulation flips ΔV; doubling b doubles it.

*What this leaves out:* Keeps only the leading order in loop size. It assumes the connection is the usual metric-compatible, torsion-free one of general relativity.

*Builds on:* [[riemann-curvature-tensor]], [[parallel-transport]] · *Visuals:* [[shrink-the-loop-to-find-riemann]]

### 5. A loop is a transformation, and loops form a group · formal

Let $M$ carry the Levi-Civita connection $\nabla$ of a metric $g$, and let $\gamma$ be a piecewise smooth loop based at $p$. Parallel transport around $\gamma$ is a linear map $\mathrm{Hol}(\gamma): T_pM \to T_pM$, the holonomy of $\gamma$. Writing the connection as matrices $(\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}$, it is the path-ordered exponential
$$\mathrm{Hol}(\gamma) = \mathcal{P}\exp\Big(-\oint_\gamma \Gamma_\mu\,dx^\mu\Big).$$
Because $\nabla g = 0$, transport preserves inner products, so $\mathrm{Hol}(\gamma)$ lies in the orthogonal group of $g_p$: $SO(2)$ on an oriented surface, and a subgroup of the Lorentz group $SO^+(1,3)$ on a time- and space-oriented spacetime. Holonomies of all loops at $p$ form the holonomy group $\mathrm{Hol}_p$; those of contractible loops form the restricted holonomy group $\mathrm{Hol}^0_p$, a connected Lie subgroup.

Curvature is the infinitesimal version of holonomy. For a small loop that flows a parameter distance $\epsilon$ along vector fields $u$ and then $v$ and back (closed, when $[u,v]\neq 0$, by a short extra leg of order $\epsilon^2$ along the Lie bracket), $\mathrm{Hol} = 1 - \epsilon^2\,\mathcal{R}(u,v) + O(\epsilon^3)$, with curvature operator $\mathcal{R}(u,v) = [\nabla_u,\nabla_v] - \nabla_{[u,v]}$ whose components are $R^\rho{}_{\sigma\mu\nu}u^\mu v^\nu$. The Riemann tensor is therefore a map from oriented 2-planes (bivectors) to generators of metric-preserving transformations. The Ambrose–Singer theorem makes this exact: the Lie algebra of $\mathrm{Hol}_p$ is spanned by curvature operators $P^{-1}\mathcal{R}(u,v)P$ transported back to $p$ along all paths. In particular the restricted holonomy is trivial exactly when $R = 0$ in the connected component considered.

Two consequences shape intuition. In two dimensions $SO(2)$ is abelian, so the holonomy of a loop bounding a region is exactly $\exp$ of the integrated curvature, which is the area law; in higher dimensions path ordering matters and no such law exists beyond leading order. And a non-contractible loop can have nontrivial holonomy in a region where $R = 0$: on a cone with deficit angle $\delta$, every loop around the apex returns vectors rotated by $\delta$, although the cone is flat away from the apex. The spacetime outside an idealized straight cosmic string has exactly this conical structure.

*Picture:* At a point p, the circle of unit tangent directions; each loop through p acts on it as a rotation; small loops give rotations linear in the loop's bivector, with the Riemann tensor as the linear map from bivectors to rotation generators.

*What this leaves out:* Restricted to the Levi-Civita connection; holonomy is defined for any connection on any vector bundle, where it need not preserve a metric.

*Builds on:* [[riemann-curvature-operator]], [[lie-bracket]], [[levi-civita-connection]] · *Visuals:* [[paper-cone-with-a-missing-wedge]], [[cube-of-small-loops]]

## Glossary

| Term | In plain words |
| --- | --- |
| closed loop | A path that ends exactly where it began. |
| holonomy | How much an arrow has turned after being carried once around a closed loop without ever being turned along the way. |
| intrinsic curvature | Curving that someone living on a surface can detect from inside it. Bending a flat sheet, like rolling paper into a tube, does not create it. |

## Key equations

### Area law on a sphere · working

$$
\Delta\alpha = \frac{A}{a^2}
$$

On a sphere, the turn of an arrow carried around a loop is the enclosed area measured in units of the radius squared.

**Symbols:** \Delta\alpha: turn of the returned arrow, in radians; A: area enclosed by the loop; a: radius of the sphere  
**Holds when:** Loop on a sphere; the angle is defined up to whole turns; the enclosed region is the one on the walker's left.  
**Say it:** “The turn, in radians, is the enclosed area divided by the radius squared.”

### Area law on any surface (local Gauss–Bonnet) · working

$$
\Delta\alpha = \iint_S K\,dA \pmod{2\pi}
$$

On any two-dimensional surface, the turn around a loop equals the total Gaussian curvature it encloses.

**Symbols:** S: the region enclosed by the loop; K: Gaussian curvature at each point of S; dA: a small piece of area  
**Holds when:** Two-dimensional surface with its metric (Levi-Civita) connection; the loop bounds a region S; exact for loops of any size.  
**Say it:** “The turn equals the curvature added up over the whole inside of the loop.”

### Angular excess of a geodesic triangle · working

$$
\Delta\alpha = \alpha_1 + \alpha_2 + \alpha_3 - \pi
$$

For a triangle made of straightest paths, the turn equals how much its angles overshoot a straight angle.

**Symbols:** \alpha_1, \alpha_2, \alpha_3: the interior angles of the triangle  
**Holds when:** Sides are geodesics; the triangle bounds a region on the surface.  
**Say it:** “The turn is how far the three angles add up to more than a straight line.”

### Small-loop law · working

$$
\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma\,a^\mu\,b^\nu
$$

The change in a vector carried around a tiny parallelogram is the Riemann tensor acting on the vector and on the two edges.

**Symbols:** V^\sigma: the vector being carried; a^\mu, b^\nu: edge vectors of the parallelogram, walked +a, +b, -a, -b; R^\rho{}_{\sigma\mu\nu}: Riemann tensor, course sign convention  
**Holds when:** Torsion-free connection; coordinate parallelogram; valid to second order in the loop size.  
**Say it:** “The change in the vector is minus the Riemann tensor, acting on the vector and on the two edges of the loop.”

### Holonomy as a path-ordered exponential · formal

$$
\mathrm{Hol}(\gamma) = \mathcal{P}\exp\Big(-\oint_\gamma \Gamma_\mu\,dx^\mu\Big),\qquad (\Gamma_\mu)^\rho{}_\sigma = \Gamma^\rho{}_{\mu\sigma}
$$

Carrying a vector around a finite loop multiplies it by the ordered product of the connection's tiny steps.

**Symbols:** \mathcal{P}: path ordering: later points of the loop act after earlier ones; \Gamma^\rho{}_{\mu\sigma}: Christoffel symbols of the connection  
**Holds when:** Any piecewise smooth loop; the result depends on the base point only by conjugation.  
**Say it:** “The holonomy is the ordered product of all the connection's tiny steps around the loop.”

## Derivations

### The small-loop law from the transport equation · formal

**Goal:** Show that walking a coordinate parallelogram +a, +b, -a, -b changes a vector by minus the Riemann tensor acting on the vector and the edges.

1. Parallel transport along a curve obeys $\frac{dV^\rho}{ds} = -\Gamma^\rho{}_{\mu\sigma}\frac{dx^\mu}{ds}V^\sigma$. In matrix form $dV/ds = -\Gamma_{\dot x}V$, with $(\Gamma_e)^\rho{}_\sigma \equiv \Gamma^\rho{}_{\mu\sigma}e^\mu$.
2. For a short straight step $e$ starting at $x$, write $\Gamma_e(x + s e) = \Gamma_e + s\,\partial_e\Gamma_e$ for $0\le s\le 1$, where $\partial_e\Gamma_e \equiv e^\nu\partial_\nu\Gamma_e$. Solving to second order gives the step matrix $P_e(x) = 1 - \Gamma_e - \tfrac12\partial_e\Gamma_e + \tfrac12\Gamma_e\Gamma_e$.
3. The four steps start at $x$, $x+a$, $x+a+b$ and $x+b$. Expand each $\Gamma$ about $x$; for example $\Gamma_b(x+a) = \Gamma_b + \partial_a\Gamma_b$ and $\Gamma_a(x+a+b) = \Gamma_a + \partial_a\Gamma_a + \partial_b\Gamma_a$.
4. Form the product $P_{-b}(x+b)\,P_{-a}(x+a+b)\,P_b(x+a)\,P_a(x)$ and keep second-order terms. The first-order terms $-\Gamma_a - \Gamma_b + \Gamma_a + \Gamma_b$ cancel. The $\partial_a\Gamma_a$ and $\partial_b\Gamma_b$ terms also cancel between opposite edges.
5. The surviving derivative terms are $\partial_b\Gamma_a - \partial_a\Gamma_b$. Collecting all products of first-order terms with the $\tfrac12\Gamma_e\Gamma_e$ terms leaves $\Gamma_b\Gamma_a - \Gamma_a\Gamma_b$.
6. In components, $\Delta V^\rho = a^\mu b^\nu\big(\partial_\nu\Gamma^\rho{}_{\mu\sigma} - \partial_\mu\Gamma^\rho{}_{\nu\sigma} + \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}\big)V^\sigma$.
7. The course definition is $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$. The bracket in the previous step is exactly its negative.

**Result:** $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ plus terms of third order in the loop size.

## Worked examples

### Why nobody notices on Earth · working

**Problem:** A surveyor carries a gyroscope-free direction marker, without turning it, around a loop enclosing 10,000 square kilometres of Earth's surface. Treat Earth as a sphere of radius 6371 km. By how much does the marker come back turned?

1. Use the sphere's area law, turn = area / radius squared.
2. Radius squared: $(6371\ \text{km})^2 = 4.059\times10^{7}\ \text{km}^2$.
3. Turn: $1.0\times10^{4} / 4.059\times10^{7} = 2.46\times10^{-4}$ radians.
4. Convert: $2.46\times10^{-4}\ \text{rad}\times 57.30^\circ/\text{rad} = 0.0141^\circ$, about 51 arcseconds.

**Answer:** About $2.5\times10^{-4}$ rad, or 51 arcseconds.

**Takeaway:** Curvature is invisible in everyday loops because the enclosed area is tiny compared with the radius squared.

### Around the 45th parallel · working

**Problem:** An arrow is carried once around the circle of latitude 45° north on a sphere. By what angle does it return turned?

1. Latitude 45° north means colatitude $\theta_0 = 45^\circ$.
2. The enclosed polar cap has area $2\pi a^2(1-\cos 45^\circ) = 2\pi a^2(0.2929)$.
3. Divide by $a^2$: turn $= 2\pi(0.2929) = 1.840$ rad.
4. In degrees: $1.840 \times 57.30 = 105.4^\circ$.

**Answer:** 1.840 rad, about 105°.

**Takeaway:** The latitude circle is not a straightest path, but the area law still applies.

### A coordinate cell on the unit sphere · formal

**Problem:** On the unit sphere, $ds^2 = d\theta^2 + \sin^2\theta\,d\phi^2$, carry $V = e_\theta$ around a small cell walked $+\delta\theta$, $+\delta\phi$, $-\delta\theta$, $-\delta\phi$. Find the change and check it against the cell's area.

1. The nonzero Christoffel symbols are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \cot\theta$.
2. With the course definition, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. Lowering gives $R_{\theta\phi\theta\phi} = \sin^2\theta$, and the pair antisymmetries give $R^\phi{}_{\theta\theta\phi} = -1$.
3. Small-loop law with $a^\theta = \delta\theta$, $b^\phi = \delta\phi$, $V^\theta = 1$: $\Delta V^\phi = -R^\phi{}_{\theta\theta\phi}\,\delta\theta\,\delta\phi = +\delta\theta\,\delta\phi$. The component $\Delta V^\theta$ is zero, because $R_{\theta\theta\theta\phi} = 0$.
4. The basis vector $e_\phi$ has length $\sin\theta$, so the unit vector $e_\theta$ tilts toward $e_\phi$ by the angle $\sin\theta\,\delta\theta\,\delta\phi$.
5. The cell's area is $\sin\theta\,\delta\theta\,\delta\phi$. With $K = 1$ the area law predicts the same angle. Seen from outside, the rotation from $e_\theta$ toward $e_\phi$ has the same sense as the circulation.

**Answer:** $\Delta V = \delta\theta\,\delta\phi\;e_\phi$: a rotation by $\sin\theta\,\delta\theta\,\delta\phi$, equal to the enclosed area.

**Takeaway:** The index formula and the area picture agree in size and in sense, which checks the sign convention.

## Teaching arc

1. **Ask the insider question.** How could a creature that can never leave its surface find out the surface is curved? *Why:* It frames holonomy as a measurement made from inside, which is the only kind available in spacetime.
2. **Show one surprise and two controls.** Run the octant walk on a ball (a quarter turn), then the same kind of walk on a flat table and on a rolled tube (no turn). *Why:* The controls rule out the corners, the walking rule, and mere bending as explanations.
3. **Let the learner discover the area law.** Resize, reshape and reverse the loop and change the ball's radius; tabulate turn against area over radius squared before naming angular excess. *Why:* Learners find proportionality, the sign flip and the scale independence themselves.
4. **Shrink the loop to reach Riemann.** Derive the small-loop law on a parallelogram and read off linearity, antisymmetry and area scaling. *Why:* Each feature of the formula explains a slot of the Riemann tensor.
5. **Check it two ways.** A unit-sphere coordinate cell gives a turn equal to its area; polar coordinates on a flat plane give zero despite nonzero Christoffel symbols. *Why:* It fixes the sign convention and separates curved coordinates from curved space.
6. **Mark the limits.** Carry the arrow around the tip of a paper cone, and note that the exact area law is special to two dimensions. *Why:* It prevents 'zero curvature along the loop means no turn' and 'the small-loop law works for big loops'.
7. **Transfer.** Show a charged particle's phase around a loop, and the cube of small loops that gives the Bianchi identity. *Why:* Holonomy becomes the shared language of gravity and gauge fields, and prepares the field equations.

## Analogies

### An ant with an arrow on a ball · entry

The ant cannot see its world from outside, but it can carry an arrow around a loop and compare. A returned turn proves the world is curved inside the loop.

| In the analogy | Stands for |
| --- | --- |
| the ant's surface | space or spacetime |
| not turning the arrow | parallel transport |
| the returned turn | holonomy |

*Limits:* Two-dimensional and without time, so the only possible change is a rotation. Other insider tests exist too, such as triangle angle sums and circle circumferences.

### The Foucault pendulum's slow turn · working

In one sidereal day Earth's rotation carries a pendulum around its circle of latitude, and its swing plane behaves approximately like an arrow carried without turning. Against local north, the swing plane turns by $2\pi\sin(\text{latitude})$ per sidereal day, clockwise in the Northern Hemisphere. The holonomy of that circle is $2\pi(1-\cos\theta_0) = 2\pi(1-\sin(\text{latitude}))$. The two differ by exactly one full turn, because local north itself turns once relative to a carried arrow during each lap.

| In the analogy | Stands for |
| --- | --- |
| the swing plane | the carried arrow |
| one sidereal day | one trip around the loop |
| the latitude circle | the loop |

*Limits:* The pendulum only approximately obeys the transport rule (slow rotation, small swings). The curvature involved is that of Earth's surface, not of spacetime.

### Polarization in a coiled optical fibre · working

Light guided along a helically coiled fibre has a direction of travel that traces a closed loop on the sphere of directions. Its polarization is carried along without turning and returns rotated by the solid angle that loop encloses.

| In the analogy | Stands for |
| --- | --- |
| the sphere of propagation directions | the curved surface |
| polarization direction | the carried arrow |
| enclosed solid angle | enclosed curvature |

*Limits:* The sphere is a space of directions, not physical space; the effect is a geometric phase in optics, not gravity.

### A charged particle's phase around a loop · formal

A charged quantum field carried around a loop gains a phase proportional to the enclosed magnetic flux, even where the magnetic field on the path itself is zero (the Aharonov–Bohm effect). The field strength $F_{\mu\nu}$ plays exactly the role the Riemann tensor plays for vectors.

| In the analogy | Stands for |
| --- | --- |
| the phase of the wavefunction | the direction of the arrow |
| the electromagnetic potential | the connection |
| the field strength | the Riemann tensor |

*Limits:* Phases commute, so their ordering around the loop does not matter; rotations of vectors in three or more dimensions do not commute. The phase lives in an internal space, and no metric or boost is involved.

## Misconceptions

### “If I never turn the arrow, it cannot come back turned.” · entry

- **Why it is tempting:** In everyday flat surroundings, not turning something is a global guarantee.
- **What is true:** 'Never turn' is a local rule, step by step. On a curved surface these no-turn steps add up to a net turn around a loop.
- **Question that exposes it:** Predict: after the walk from the North Pole to the equator, a quarter of the way around, and back, which way does the arrow point?

### “The arrow turned because I turned at the corners.” · entry

- **Why it is tempting:** The walker makes visible turns, and the arrow's final direction is different.
- **What is true:** Your body turns at the corners, but the arrow never does. A square walk on a flat floor has four corners too, and the arrow comes back unchanged.
- **Question that exposes it:** Walk a square on a flat floor, turning left at each corner but never turning the arrow. Does it come back turned?

### “A tube looks curved, so an arrow carried around a loop on it must come back turned.” · entry

- **Why it is tempting:** From outside, the tube is obviously bent.
- **What is true:** A tube unrolls into a flat sheet without stretching, so every loop on it returns the arrow unchanged. Only curving that cannot be removed by bending shows up.
- **Question that exposes it:** An ant walks all the way around a paper tube and back to its start. Does its arrow come back turned?

### “The direction I walk around the loop does not matter.” · entry

- **Why it is tempting:** The enclosed area is the same either way.
- **What is true:** Walking the loop backwards undoes the transport, so the turn reverses. In the small-loop law this is the antisymmetry of the Riemann tensor in its last two slots.
- **Question that exposes it:** Walking a small loop clockwise turns the arrow 2° clockwise. What happens counterclockwise?

### “If the surface is flat everywhere along my loop, the arrow cannot come back turned.” · working

- **Why it is tempting:** The small-loop law makes holonomy look like a local sum of curvature along the path.
- **What is true:** Flatness guarantees no turn only for loops that can be shrunk to a point without leaving the flat region. A loop around the tip of a paper cone crosses only flat paper, yet returns turned by the missing wedge's angle.
- **Question that exposes it:** A cone is made by removing a 60° wedge from paper. An ant walks a wide circle around the tip. Does the arrow come back unchanged?

### “Halfway around, I can see how much the arrow has turned so far.” · working

- **Why it is tempting:** Animations show the arrow's direction in the room changing continuously, inviting a running angle.
- **What is true:** Arrows at different places on a curved surface have no route-independent comparison. The turn is defined only when the loop closes and both arrows sit at the same point.
- **Question that exposes it:** Halfway around the octant loop, a readout claims the arrow has turned 45°. Relative to what?

### “The small-loop formula also works for big loops, using the curvature at one point.” · formal

- **Why it is tempting:** On a sphere the area law looks like the small-loop law applied to a big area.
- **What is true:** The formula is leading order only. Big loops need the full path-ordered transport; the exact area law holds only because rotations in two dimensions commute.
- **Question that exposes it:** Using the Riemann tensor at the North Pole alone, could you predict the turn for a loop in a region where the curvature varies? What would you have to do instead?

### “In spacetime, the holonomy of a small loop depends only on its area.” · formal

- **Why it is tempting:** On a sphere, every plane is the same plane, so area is all that matters.
- **What is true:** It depends on the oriented plane the loop spans. A loop in a plane containing the time direction near a mass returns a tiny boost set by the tidal components of the curvature.
- **Question that exposes it:** Near Earth, would a small loop in a horizontal spatial plane and a same-area loop in a plane containing time give the same holonomy? Which object decides?

## Checks

1. **Entry.** An ant carries an arrow around a small loop on a ball, and it comes back turned a little. The ant walks the same loop again, but in the opposite direction. What happens to the arrow? *(targets: “The direction I walk around the loop does not matter.”)*
   - **Answer:** It comes back turned by the same amount, but the other way. Walking the loop backwards undoes the first trip.
2. **Entry.** An ant walks a loop all the way around a paper tube, never turning its arrow. Does the arrow come back turned? Why? *(targets: “A tube looks curved, so an arrow carried around a loop on it must come back turned.”)*
   - **Answer:** No. Unroll the tube and it is a flat sheet with nothing stretched. On a flat sheet the arrow never turns, so it did not turn on the tube.
3. **Working.** A triangle of great-circle arcs on a sphere of radius 1000 km has angles 100°, 60° and 50°. By how much does an arrow carried around it turn, and what is the triangle's area?
   - **Answer:** The angles sum to 210°, so the excess is 30° = π/6 rad; that is the turn. Area = (π/6)(1000 km)² ≈ 5.24 × 10⁵ km².
4. **Working.** An arrow is carried once around the circle of latitude 30° north on a sphere. By what angle does it return turned?
   - **Answer:** Colatitude is 60°. The cap area is 2πa²(1 − cos 60°) = πa², so the turn is πa²/a² = π, a half turn.
5. **Formal.** In polar coordinates on a flat plane, $\Gamma^r{}_{\phi\phi} = -r$ is not zero. Does a small loop there return vectors turned?
   - **Answer:** No. The turn is set by the Riemann tensor, which vanishes for the flat metric $dr^2 + r^2d\phi^2$. Nonzero Christoffel symbols describe curved coordinate lines, not curved space.
6. **Formal.** A cone is made by removing a 90° wedge from paper. A student says: 'every patch of the cone away from the tip is flat, so every loop gives zero holonomy.' Evaluate the claim. *(targets: “If the surface is flat everywhere along my loop, the arrow cannot come back turned.”)*
   - **Answer:** It is true only for loops that do not go around the tip. A loop around the tip returns vectors turned by 90°: unrolling shows that gluing the wedge's edges imposes that rotation. Vanishing curvature along a loop guarantees trivial holonomy only for loops contractible within the flat region.

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the small-loop law | Walking +a, +b, −a, −b gives ΔV^ρ = −R^ρ_σμν V^σ a^μ b^ν with the course Riemann tensor. | Many texts walk the edges in the other order, or define the Riemann tensor with the opposite overall sign, and write +R. Always state the route and the Riemann convention together. |
| Sign of a gauge phase | This note uses D_μ = ∂_μ + iqA_μ with ħ = 1, giving the phase exp(−iq∮A_μ dx^μ). | D_μ = ∂_μ − iqA_μ flips the sign of the exponent; SI and Gaussian units add factors of ħ and c. |

## Visuals

- ★ [[carry-an-arrow-around-a-loop]] (flagship): The central experience: the octant walk with flat and tube controls, loops to reshape and reverse, and a turn readout that appears when the loop closes.
- [[shrink-the-loop-to-find-riemann]] (core): Connects the area picture to the Riemann tensor. *Sketch:* A coordinate parallelogram on a chosen 2D metric (sphere patch, saddle, polar-coordinate plane). The learner shrinks it with sliders and swaps the edge order. A log-log plot shows the change in the vector against the area with slope one, converging to the Riemann prediction; the polar plane stays at zero.
- [[paper-cone-with-a-missing-wedge]] (core): Shows holonomy without local curvature. *Sketch:* Cut a wedge of adjustable angle from a flat sheet and glue it into a cone. Loops that avoid the tip return the arrow unchanged; loops around the tip return it turned by the wedge angle. The unrolled sheet sits beside the cone, so the learner sees the arrow slide rigidly and the seam add the turn.
- [[arrow-around-a-circle-of-latitude]] (supporting): Area law for a curve that is not a straightest path, and the link to the Foucault pendulum. *Sketch:* Drag the latitude and play one lap. Plot the returned turn against latitude, with a toggle between the turn relative to the starting arrow and relative to local north, overlaid with the Foucault pendulum's daily turn. The two curves differ by exactly one full turn.
- [[cube-of-small-loops]] (supporting): Geometric picture of the Bianchi identity. *Sketch:* A small cube whose six faces are traversed as loops joined along shared edges travelled once each way. The face holonomies are shown as small rotation arrows that sum to nothing.

## Tutor moves

**Open with**

- If you carry an arrow around a closed walk and never turn it, can it come back pointing a different way?
- How could an ant that can never leave the surface of a ball find out that the ball is curved?

**If the learner is stuck**

- *The learner thinks the corners caused the turn.* → Run the same kind of walk on a flat floor: the walker turns at the corners and the arrow still comes back unchanged.
- *The learner insists a tube is curved.* → Unroll the tube in the demo, and ask whether any path on flat paper could turn the arrow.
- *The learner is lost in the index formula.* → Return to the unit-sphere cell: compute a single component, then show that the answer equals the cell's area.
- *The learner wants to read an angle partway round.* → Ask what the moving arrow would be compared with, then show that different routes to the halfway point give different answers.

**Common questions**

- *If I never turn the arrow, where does the turn come from?* From the surface itself. On a curved surface, keeping the arrow straight at every step does not keep it pointing the same way overall. The small no-turn steps add up to a net turn.
- *Why does this matter for gravity?* We live inside spacetime and cannot view it from outside. Tests from inside, like carrying an arrow around a loop or watching nearby falling objects drift apart, are how curvature shows up physically.
- *Does a bigger ball give a bigger turn?* For a triangle with the same angles, no: the area grows exactly as fast as the radius squared, so the turn stays the same. For a loop of fixed size in metres, a bigger ball gives a smaller turn, because it is less curved.

**Demo moments**

- Right after the opening question: have the learner predict, then run the octant walk.
- When the learner says 'but it's curved' about the tube: unroll it.
- Before writing the small-loop law: shrink the loop and let the learner see the turn scale with area.

**Saying it aloud:** Say 'delta alpha' as 'the turn'. Read K dA as 'curvature times a little piece of area, added up over the inside'. Read the small-loop law as 'the change in the vector is minus the Riemann tensor acting on the vector and the two edges'; do not read out index names. Say angles in degrees for beginners and radians once the area law is in play.

**Switching levels:** Stay with the two entry ways and the cone for learners without calculus. When a learner uses the word 'area' quantitatively or asks 'how much does it turn', move to the area law. If the learner is comfortable with tensors or asks for the general formula, go to the small-loop law within a few minutes of the demo. For graduate learners, go to holonomy groups, Ambrose–Singer and the cosmic string.

## History

- **Carl Friedrich Gauss (1827), *Disquisitiones generales circa superficies curvas*.** Showed that a surface's curvature can be measured from inside it, and related the angle sum of a geodesic triangle to the curvature it encloses.
- **Pierre Ossian Bonnet (1848).** Extended Gauss's angle-sum result to regions bounded by arbitrary curves, giving the local Gauss–Bonnet theorem.
- **Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*.** Defined parallel transport on any curved space and used it to give Riemann's curvature a geometric meaning.
- **Élie Cartan (1926), *Les groupes d'holonomie des espaces généralisés*.** Introduced holonomy groups and made them a central tool of differential geometry.
- **Warren Ambrose, Isadore Singer (1953), *A theorem on holonomy*.** Proved that curvature generates the holonomy group's Lie algebra.

## Research horizon

- **Special holonomy.** The possible holonomy groups of Riemannian manifolds were classified. Manifolds with small holonomy groups, such as Calabi–Yau spaces (SU(3)) and G₂ manifolds, are the extra dimensions used in string and M-theory compactifications. *Pointers:* Berger (1955); Candelas, Horowitz, Strominger & Witten (1985), *Vacuum configurations for superstrings*
- **Discrete gravity.** Regge calculus builds spacetime from flat simplices glued together, with all curvature concentrated on hinges and measured by deficit angles, which are holonomies of small loops around the hinges. Causal dynamical triangulations build a quantum theory on this idea. *Pointers:* Regge (1961), *General relativity without coordinates*; Ambjørn, Jurkiewicz & Loll (2004), *Emergence of a 4D world from causal quantum gravity*
- **Loop quantum gravity.** The theory takes holonomies of a connection along curves, rather than the metric, as basic variables; spin networks label their quantum states. *Pointers:* Ashtekar (1986), *New variables for classical and quantum gravity*; Rovelli & Smolin (1990), *Loop space representation of quantum general relativity*
- **Cosmic strings and Wilson loops.** Outside a straight cosmic string of mass per unit length μ, spacetime is locally flat, but loops around it return rotated by the deficit angle 8πGμ/c². In gauge theories, holonomies of the gauge field around loops (Wilson loops) are the basic gauge-invariant observables and a diagnostic of confinement. *Pointers:* Vilenkin (1981), *Gravitational field of vacuum domain walls and strings*; Wilson (1974), *Confinement of quarks*
