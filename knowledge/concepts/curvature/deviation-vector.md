---
type: "concept"
schema_version: 2
id: "deviation-vector"
title: "Deviation vector"
tagline: "A stretchy string joining two neighbours who walk without steering, at the same step count"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["connecting vector", "separation vector", "geodesic deviation vector"]
prerequisites: ["geodesic", "affine-parameter", "congruence-of-curves", "lie-dragging", "lie-bracket", "riemann-curvature-tensor", "killing-vector"]
leads_to: ["geodesic-deviation-equation", "expansion-shear-and-rotation", "conjugate-point", "geodesic-deviation-in-gravitational-wave"]
visuals: ["two-walkers-set-off-side-by-side", "elastic-arrow-between-two-beads", "falling-ring-of-crumbs"]
---

# Deviation vector

*A stretchy string joining two neighbours who walk without steering, at the same step count*

`deviation-vector` · curvature · core · physics-reviewed (revision 7)

**Needs:** [[geodesic]] (entry) · [[affine-parameter]] (entry) · [[congruence-of-curves]] (working) · [[lie-dragging]] (working) · [[lie-bracket]] (formal) · [[riemann-curvature-tensor]] (formal) · [[killing-vector]] (formal)  
**Opens:** [[geodesic-deviation-equation]] · [[expansion-shear-and-rotation]] · [[conjugate-point]] · [[geodesic-deviation-in-gravitational-wave]]  
**Related:** [[newtonian-deviation-equation]] · [[parallel-postulate]] · [[tidal-force]] · [[hubble-parameter]]  
**Visuals:** ★ [[two-walkers-set-off-side-by-side]] · [[elastic-arrow-between-two-beads]] · [[falling-ring-of-crumbs]]

> Two friends walk side by side without ever steering, taking equal steps and counting them. A stretchy string from where one friend stands to where the other stands at the same step count is called the deviation vector. It grows or shrinks as their paths spread apart or draw together. Only its part running across the paths measures how far apart the paths are; any part lying along the paths comes from one friend starting to count further back.

## You will be able to

**Entry**
- Explain what the deviation vector joins, and why it can shrink on a ball while a carried arrow keeps its length. `objectives/explain-string-at-same-count` ← `checks/shrinking-string-on-a-ball`
- Predict the sideways and along-path parts of the string when two walkers start counting from different spots. `objectives/split-sideways-and-along-path` ← `checks/late-start-string`, `problems/string-at-the-pole`
- Explain why a string of steady length between two straight walkers does not show that the ground is flat. `objectives/explain-steady-string` ← `checks/one-behind-the-other`

**Working**
- Compute the deviation vector of a labelled family of geodesics and remove its part along the four-velocity. `objectives/compute-and-project` ← `checks/desynchronized-clocks`
- Use the rule that the velocity gradient sets the rate of change of the deviation vector to find how fast a separation grows. `objectives/use-first-derivative-rule` ← `problems/hubble-neighbours`
- Distinguish a Lie-dragged deviation vector from one of constant length. `objectives/distinguish-dragged-from-constant` ← `checks/lie-dragged-claim`

**Formal**
- Prove that the two covariant derivatives on a family of curves agree for every family exactly when the torsion vanishes. `objectives/prove-grid-closes` ← `checks/torsion-and-symmetry`
- State which vector fields along a geodesic are deviation vectors, and count the physical ones. `objectives/classify-deviation-fields` ← `checks/counting-deviation-fields`
- Prove that a Killing field along a geodesic is a deviation vector, and use it to find a separation that never changes. `objectives/use-killing-fields` ← `problems/killing-field-along-an-orbit`

## Ways in

### 1. A string between two walkers · entry · picture

*How can you keep track of the gap between two neighbours who walk without steering?*

**Recap:** Walking straight means walking without ever steering left or right. On a ball, the equator is a straight walk. So is each line printed on a globe from the equator to the North Pole. The ball on one side of such a line is a mirror image of the ball on the other side. So a walker following the line has no reason to steer either way.

Two friends, Asha and Ben, stand on a flat playground, one metre apart and facing the same way. Ben is on Asha's right, and neither is ahead of the other. Each takes steps exactly one metre long and counts them. Both walk straight, never steering left or right.

Now picture a stretchy string running from Asha to Ben. At count 10, one end is where Asha stands after her tenth step, and the other end is where Ben stands after his tenth step. The count matters, not the clock. If Ben walks faster, the string at count 10 still joins the spots each friend reaches after ten steps.

Neither friend started ahead, and both take equal steps, so the string runs across their paths at a right angle. On flat ground, their straight paths keep the same gap. So the string stays one metre long at every count.

Put an arrowhead on the string at Ben's end, so that it points from Asha to Ben. An arrow with a length and a direction like this is called a vector.

This string is called the deviation vector, because it shows which way and how far Ben stands from Asha at the same count.

The string is tied to both friends. If their paths draw together or spread apart, the string shrinks or grows with them.

Compare a stiff cardboard arrow, one metre long, that Asha holds against the ground. It points at Ben at the start, and she never lets it swing left or right in her hands. The arrow is tied only to Asha, and cardboard cannot stretch, so it always keeps its length.

Now take the friends to a huge smooth ball the size of Earth. They start on the equator, one metre apart, both facing the North Pole. Walking straight, each follows a line from the equator to the North Pole, like the lines printed on a globe but only one metre apart at the equator.

Those lines draw together and meet at the North Pole, so the string shrinks. To find by how much, look at the other circles printed on a globe. Each runs all the way around the ball like the equator, but closer to the North Pole.

Both friends have taken the same number of steps from the equator, so at matching counts they stand on the same one of these circles. The lines from the equator to the North Pole cut every such circle into equal pieces, like the cuts between the segments of an orange. So the string always covers the same fraction of the friends' circle as it did of the equator.

Two thirds of the way to the North Pole, that circle is half as long as the equator. You can check this on a globe with a piece of thread. So there, after about 6,700 kilometres, the string is 50 centimetres long. At the North Pole, where the lines meet, the string has shrunk to nothing.

On Earth, this shrinking is far too slow to notice on a walk. After one kilometre, the one-metre string is shorter by only about 12 millionths of a millimetre. That is less than a thousandth of a hair's width.

**Try it:** Find a globe with lines printed from the equator to the North Pole and a circle marked 60 degrees. The circles are marked from 0 degrees at the equator to 90 degrees at the North Pole, so the 60-degree circle is two thirds of the way up. Lay a thread along the equator between two neighbouring lines and cut it to that length. Lay a second thread between the same two lines along the 60-degree circle and cut it. Fold the first thread in half: it matches the second.

**Takeaway:** The deviation vector is a short, stretchy string from one walker to a neighbour at the same count. It is tied to both walkers, so it grows or shrinks as their straight paths spread apart or draw together.

*What this leaves out:* Treats Earth as a smooth ball and keeps the friends close together, a few metres apart at most.

*Builds on:* [[geodesic]], [[affine-parameter]]<br>*Visuals:* [[two-walkers-set-off-side-by-side]]<br>*See:* `checks/shrinking-string-on-a-ball`

### 2. Three steps behind the line · entry · contrast

*Does it matter where each walker starts counting?*

**Recap:** Two friends walk straight, never steering, taking one-metre steps and counting them. The deviation vector is a stretchy string running from one friend to the other at the same count, pointing from the first to the second. On a huge smooth ball, friends who start on the equator one metre apart, facing the North Pole, draw together. Two thirds of the way to the North Pole, the string between them is half as long.

In "A string between two walkers", Asha and Ben started side by side, with neither ahead. This time, Ben stands one metre to Asha's right but three metres behind her. Both face the same way on a flat playground. Each counts one-metre steps from their own starting spot and walks straight.

At every count, Ben is three metres behind Asha and one metre to her right, because each count moves both friends one metre ahead. So the string from Asha to Ben at the same count slants backward. By Pythagoras's rule, its length times itself is 3 times 3 plus 1 times 1, which is 10. So the string is about 3.2 metres long.

Yet their paths are only one metre apart. To see why, split the string into two pieces. Start where Asha stands, go three metres back along her path, then go one metre across to Ben, at a right angle to her path. These two pieces, joined end to end, reach the same spot as the string.

The piece that runs across Asha's path at a right angle is called the sideways part. Its length is the distance between the two paths, here one metre.

The piece that points ahead or behind along Asha's path is called the along-path part. Here it is three metres long, pointing behind her.

The along-path part comes only from where the friends started counting. It stays three metres for the whole walk, because both friends add one metre with every count. If Ben had started side by side with Asha, it would be zero.

Now try the same start on the ball. Asha stands on the equator, facing the North Pole. Ben faces the same way, one metre to her right and three metres behind her, on the side of the equator away from the North Pole. When Asha is two thirds of the way there, the sideways part has halved to 50 centimetres, as in the side-by-side walk. The along-path part is three metres, the same as at the start. So the whole string has gone from about 3.2 metres to about 3.0 metres. It has not halved, because its along-path part did not shrink.

Moving where Ben starts counting changes the string's along-path part, but not its sideways part. Only the sideways part tells you how far apart the paths are.

**Takeaway:** With equal steps, where the walkers start counting adds a fixed along-path part to the string; only the sideways part measures how far apart the paths are.

*What this leaves out:* Keeps the friends a few metres apart. For paths one metre apart on an Earth-sized ball, as in this walk, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.

*Continues:* `ways_in/string-between-two-walkers`<br>*Builds on:* [[affine-parameter]]<br>*Visuals:* [[two-walkers-set-off-side-by-side]]<br>*See:* `checks/late-start-string`, `problems/string-at-the-pole`

### 3. Label the family and differentiate · working · calculation

*How do you compute a deviation vector from a family of geodesics, and what fixes how fast it changes?*

The string between two walkers at the same count, in "A string between two walkers", becomes a derivative once the counts are a parameter. Take a smooth family of timelike geodesics $x^\mu(\tau, s)$. The label $s$ picks a member, and $\tau$ is proper time along it, so $u^\mu = \partial x^\mu/\partial\tau$ with $u_\mu u^\mu = -c^2$ for every member. Define the deviation vector

$$\xi^\mu = \frac{\partial x^\mu}{\partial s}.$$

The neighbour with label $s + \delta s$ at the same proper time sits at $x^\mu + \xi^\mu\,\delta s$, to first order in $\delta s$. Equal proper time plays the part of the matching count.

Mixed partial derivatives commute, so $\partial u^\mu/\partial s = \partial\xi^\mu/\partial\tau$. The two grid directions close, $[u, \xi] = 0$: the deviation vector is Lie dragged along the family, always joining the same two members. Adding $\Gamma^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$ to both sides and using the symmetry of the Christoffel symbols gives, as the derivation "Commuting derivatives along and across the family" shows step by step,

$$\frac{D\xi^\mu}{d\tau} = \xi^\nu\nabla_\nu u^\mu.$$

The separation changes at a rate set by how the family's four-velocity varies across it. Dragged does not mean constant: if neighbours move apart, $\xi$ grows.

The same derivation shows that $u_\mu\xi^\mu$ never changes along a member, because every member has $u_\mu u^\mu = -c^2$. That is the along-path part of "Three steps behind the line". Its value depends only on how the members' clocks were set: relabelling so that $x^\mu(\tau, s)$ becomes $x^\mu(\tau + f(s), s)$ adds $f'(s)\,u^\mu$ to $\xi^\mu$. The part that an observer riding on the geodesic calls the separation is the orthogonal part

$$\xi_\perp^\mu = \Big(\delta^\mu{}_\nu + \frac{u^\mu u_\nu}{c^2}\Big)\xi^\nu.$$

The sign suits signature $(-,+,+,+)$: $u_\mu\xi_\perp^\mu = u_\nu\xi^\nu + (-c^2)\,u_\nu\xi^\nu/c^2 = 0$.

The first derivative can vanish at an event, for masses released at rest relative to each other. The second derivative cannot be removed that way. Taken on trust here, it obeys the geodesic deviation equation $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$, and the along-path part, a constant times $u^\mu$, drops out of it. The worked example "Meridians with a head start" runs all of this on a sphere.

**Takeaway:** The deviation vector is the label derivative of a family of geodesics; its covariant rate of change is the velocity gradient acting on it, and its part along the four-velocity stays fixed.

*What this leaves out:* Assumes every member is timelike and normalized to $u_\mu u^\mu = -c^2$; "Variation fields and Jacobi fields" treats other normalizations and light rays.

*Continues:* `ways_in/string-between-two-walkers`, `ways_in/three-steps-behind-the-line`<br>*Builds on:* [[congruence-of-curves]], [[lie-dragging]], [[covariant-derivative-along-a-curve]]<br>*Visuals:* [[elastic-arrow-between-two-beads]]<br>*See:* `derivations/commuting-derivatives`, `worked_examples/meridians-with-a-head-start`, `problems/hubble-neighbours`

### 4. Radar from a falling mass · working · operational

*What does an instrument riding on one freely falling mass measure of the deviation vector?*

The family labelled in "Label the family and differentiate" is a mathematical grid. An observer riding on one freely falling mass has only a clock, gyroscopes, an accelerometer and a lamp. Call that observer A, and a neighbouring mass B. A's accelerometer reads zero, so the separation cannot be felt on A alone; it has to be measured between the two.

A sends a light pulse at proper time $\tau_1$ on A's clock, B reflects it, and it returns at $\tau_2$. The deviation vector keeps only first order in the separation, and to that order A's freely falling frame is inertial near A. In that frame the reflection happens at A's time $\tau_{\rm m} = (\tau_1 + \tau_2)/2$, at distance

$$L = \frac{c\,(\tau_2 - \tau_1)}{2}.$$

The direction of the returning pulse, read against A's gyroscopes, gives the direction. Together they measure $\xi_\perp^\mu\,\delta s$, the orthogonal part of the deviation vector: the separation in A's rest frame.

The along-path part is invisible to radar. It records which tick of B's clock the family pairs with each tick of A's. If B's clock reads $\tau_{\rm B}$ at the reflection, then $u_\mu\xi^\mu\,\delta s = c^2(\tau_{\rm B} - \tau_{\rm m})$, a clock offset rather than a distance. Resetting B's clock changes it and nothing else. B's relative speed is itself first order in the separation, so it changes clock rates only at second order.

Gravitational-wave detectors work this way. At the signal's frequencies, each LIGO mirror hangs as a pendulum and moves along its arm like a free mass, so each 4 km arm is $|\xi_\perp|\,\delta s$ for a pair of mirrors. As GW150914, the first gravitational wave detected, passed, laser light comparing the two arms found their lengths changing relative to each other by about $4\times10^{-18}$ m. The wave's wavelength was more than a thousand kilometres, so the first-order description holds across a 4 km arm.

**Takeaway:** Radar timing and gyroscopes on one freely falling mass measure the orthogonal part of the deviation vector; its along-path part is only a clock offset.

*What this leaves out:* Keeps first order in the separation and ignores the mirrors' residual forces from their suspensions.

*Continues:* `ways_in/label-the-family-and-differentiate`<br>*Builds on:* [[proper-time]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `observations/gw150914-mirror-separation`

### 5. Variation fields and Jacobi fields · formal · structure

*What exactly is a deviation vector, which fields along a geodesic can be one, and where does the idea stop working?*

The label grid of "Label the family and differentiate" becomes a definition once the family is a smooth map. Set $G = c = 1$, and let $(M, g)$ carry its Levi-Civita connection. A geodesic variation is a smooth map $x: I \times (-\epsilon, \epsilon) \to M$ such that each curve $\gamma_s = x(\cdot, s)$ is an affinely parametrized geodesic. Write $u = x_*\partial_\lambda$ and $\xi = x_*\partial_s$ for the vector fields along the map. The deviation vector, or variation field, is $\xi$ along $\gamma_0$. It belongs to the family, not to $\gamma_0$ and one neighbour alone.

Three facts follow, with $D_\lambda$ and $D_s$ the covariant derivatives along the two sets of grid lines.

- In components $D_\lambda\xi^\mu - D_s u^\mu = T^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$, since the mixed partials of $x^\mu$ cancel. Zero torsion gives $D_\lambda\xi = D_s u$, whether or not $x$ is an immersion.

- Because $D_\lambda u = 0$ and $\nabla g = 0$, $\partial_\lambda g(u, \xi) = g(u, D_s u) = \tfrac12\partial_s g(u, u)$. Each $g(u, u)$ is constant along its geodesic, so $g(u, \xi) = \alpha + \beta\lambda$ along $\gamma_0$, with $\beta = 0$ when all members share one normalization.

- The derivation "The Jacobi equation from a geodesic variation" commutes $D_\lambda$ past $D_s$ at the cost of curvature and finds $D_\lambda^2\xi = -\mathcal{R}(\xi, u)u$, with $\mathcal{R}(X, Y) = [\nabla_X, \nabla_Y] - \nabla_{[X,Y]}$. Its components are the course geodesic deviation equation.

A vector field $J$ along a geodesic that solves this equation is a Jacobi field. Conversely, every Jacobi field is a variation field. Sketch: pick a curve $c(s)$ with $c'(0) = J(0)$ and a field $W(s)$ along $c$ with $W(0) = u(0)$ and $D_sW(0) = D_\lambda J(0)$, and set $x(\lambda, s) = \exp_{c(s)}(\lambda W(s))$ where defined. Its variation field solves the same linear second-order equation with the same initial data, so it equals $J$.

So deviation vectors along a geodesic in $n$ dimensions form a $2n$-dimensional space, fixed by $\xi$ and $D_\lambda\xi$ at one point. The fields $(a + b\lambda)u$ come from reparametrizing the members, replacing $x(\lambda, s)$ by $x(\lambda + as, s)$ or by $x((1 + bs)\lambda, s)$; on a unit-speed timelike geodesic such a field has $g(u, \xi) = -(a + b\lambda)$, so $\alpha = -a$ and $\beta = -b$. For a unit-speed timelike geodesic, $\xi_\perp = \xi + g(u, \xi)u$ obeys the same equation, and the physically distinct separations form a $(2n - 2)$-dimensional space: six in spacetime.

If $K$ is a Killing field, its flow $\phi_s$ acts by isometries, which carry affinely parametrized geodesics to affinely parametrized geodesics. So $x(\lambda, s) = \phi_s(\gamma(\lambda))$ is a geodesic variation, and $K$ restricted to any geodesic is a Jacobi field. A point $q$ is conjugate to $p$ along $\gamma$ when a nonzero Jacobi field vanishes at both.

Limits of validity. A deviation vector is first-order information: $x(\lambda, \delta s)$ and $\exp_{x(\lambda, 0)}(\delta s\,\xi)$ agree only to first order in $\delta s$, and the second-order terms depend on the family, not on curvature alone. The vector vanishes where neighbouring members reach the same event at the same parameter. For null geodesics $g(u, u) = 0$ for every member, so $g(u, \xi)$ is constant, but $u$ lies in its own orthogonal space; in spacetime the physical transverse separations form the two-dimensional quotient $u^\perp/\mathrm{span}(u)$.

**Takeaway:** A deviation vector is the variation field of a family of geodesics; such fields are exactly the Jacobi fields, and up to reparametrization they carry 2n minus 2 physical degrees of freedom.

*Picture:* A two-parameter sheet of geodesics mapped into spacetime, its grid lines $\lambda$ and $s$ closing into small parallelograms, with $u$ and $\xi$ drawn at one corner and the tangential directions $(a + b\lambda)u$ shaded as the part that relabelling removes.

*What this leaves out:* Uses the Levi-Civita connection; with torsion the first identity gains a torsion term and the Jacobi equation gains terms in the torsion and its derivative.

*Continues:* `ways_in/label-the-family-and-differentiate`<br>*Builds on:* [[lie-bracket]], [[riemann-curvature-tensor]], [[killing-vector]]<br>*See:* `derivations/jacobi-equation-from-a-variation`, `checks/counting-deviation-fields`, `problems/killing-field-along-an-orbit`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| walk straight | — | Walking without ever steering left or right. On a ball, the equator is a straight walk, and so is each line from the equator to the North Pole. The ball on one side of such a line mirrors the ball on the other side, so nothing makes the walker steer. | [[geodesic]] |
| same count | — | Two walkers are at the same count when each has taken the same number of equal steps from their own starting spot. | [[affine-parameter]] |
| vector | — | An arrow with a length and a direction. | — |
| deviation vector | — | A stretchy string from one walker to a neighbouring walker at the same count, with an arrowhead pointing from the first to the second. It is tied to both walkers, so it grows or shrinks as their paths spread apart or draw together. | [[deviation-vector]] |
| sideways part | — | The piece of the deviation vector that runs across a walker's path at a right angle. Its length is the distance between the two paths. | — |
| along-path part | — | The piece of the deviation vector that points ahead or behind along a walker's path. It comes only from where the walkers started counting. | — |
| swing | — | To change which way a carried arrow points, left or right, while it lies against the ground. | — |

## Key equations

### Deviation vector of a family · working

$$
\xi^\mu = \frac{\partial x^\mu}{\partial s}
$$

The deviation vector is how a point of the family moves as the label changes at fixed proper time; the neighbour with label $s + \delta s$ sits at $x^\mu + \xi^\mu\delta s$ to first order.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^\mu$ | the deviation vector | xi |
| $x^\mu(\tau, s)$ | the event at proper time $\tau$ on the member with label $s$ | the position on the family |
| $s$ | the label that picks a member of the family | the label |

**Holds when:** Smooth one-parameter family of geodesics, each with proper time or another affine parameter $\tau$, held fixed in the derivative; first order in $\delta s$.  
**Say it:** “Xi is the rate of change of position with the family label, at fixed proper time.”  
**Justified by:** `stated`

### Rate of change of the deviation vector · working

$$
\frac{D\xi^\mu}{d\tau} = \xi^\nu\nabla_\nu u^\mu
$$

The covariant rate of change of the separation is the family's velocity gradient acting on the separation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $D/d\tau$ | covariant derivative along the geodesic | the covariant rate of change |
| $u^\mu$ | four-velocity of the family | u |
| $\nabla_\nu u^\mu$ | velocity gradient of the family | the velocity gradient |

**Holds when:** Torsion-free connection; the family fills a region so that $u^\mu$ is a field (otherwise read the right side as $Du^\mu/ds$).  
**Say it:** “The covariant rate of change of xi equals xi dotted into the gradient of the four-velocity.”  
**Justified by:** `derivations/commuting-derivatives`

### Orthogonal part of the deviation vector · working

$$
\xi_\perp^\mu = h^\mu{}_\nu\,\xi^\nu,\qquad h^\mu{}_\nu = \delta^\mu{}_\nu + \frac{u^\mu u_\nu}{c^2}
$$

Projecting out the four-velocity leaves the separation measured in the rest frame of an observer riding on the geodesic.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi_\perp^\mu$ | orthogonal part of the deviation vector | xi perp |
| $h^\mu{}_\nu$ | projector onto the observer's rest space | the projector h |

**Holds when:** Timelike geodesic with $u_\mu u^\mu = -c^2$ and signature $(-,+,+,+)$.  
**Say it:** “Xi perp is the projector h acting on xi, where h is the identity plus u u over c squared.”  
**Justified by:** `stated`

### Jacobi equation · formal

$$
D_\lambda^2\,\xi = -\mathcal{R}(\xi, u)\,u
$$

Deviation vectors of geodesic variations are exactly the solutions of this linear second-order equation; in components it is $D^2\xi^\mu/d\lambda^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $D_\lambda$ | covariant derivative along the geodesic | D lambda |
| $\mathcal{R}(X, Y)$ | curvature operator $[\nabla_X, \nabla_Y] - \nabla_{[X,Y]}$ | the curvature operator |

**Holds when:** Levi-Civita connection; affinely parametrized geodesic; $G = c = 1$.  
**Say it:** “D lambda squared of xi equals minus the curvature operator of xi and u, acting on u.”  
**Justified by:** `derivations/jacobi-equation-from-a-variation`

## Derivations

### Commuting derivatives along and across the family · working

**Goal:** Show that $D\xi^\mu/d\tau = \xi^\nu\nabla_\nu u^\mu$ and that $u_\mu\xi^\mu$ is constant along each member.

1. Write the family as $x^\mu(\tau, s)$, with $u^\mu = \partial x^\mu/\partial\tau$ and $\xi^\mu = \partial x^\mu/\partial s$.
2. Mixed partial derivatives of $x^\mu$ commute: $\partial u^\mu/\partial s = \partial\xi^\mu/\partial\tau$.
3. Add $\Gamma^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$ to both sides. On the left, $\partial\xi^\mu/\partial\tau + \Gamma^\mu{}_{\alpha\beta}u^\alpha\xi^\beta = D\xi^\mu/d\tau$.
4. On the right, $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$ turns the added term into $\Gamma^\mu{}_{\beta\alpha}\xi^\beta u^\alpha$, so the right side is $Du^\mu/ds$.
5. Where the family fills a region, $u^\mu$ is a field and $Du^\mu/ds = \xi^\nu\nabla_\nu u^\mu$. This proves the first result.
6. Metric compatibility gives $\dfrac{d}{d\tau}(g_{\mu\nu}u^\mu\xi^\nu) = g_{\mu\nu}\dfrac{Du^\mu}{d\tau}\xi^\nu + g_{\mu\nu}u^\mu\dfrac{D\xi^\nu}{d\tau}$.
7. The first term vanishes because each member is a geodesic, $Du^\mu/d\tau = 0$.
8. By the first result, the second term is $g_{\mu\nu}u^\mu Du^\nu/ds = \tfrac12\,\partial(g_{\mu\nu}u^\mu u^\nu)/\partial s$.
9. Every member has $g_{\mu\nu}u^\mu u^\nu = -c^2$, which does not depend on $s$, so the derivative is zero.

**Result:** $D\xi^\mu/d\tau = \xi^\nu\nabla_\nu u^\mu$, and $u_\mu\xi^\mu$ is constant along each member.

### The Jacobi equation from a geodesic variation · formal

**Goal:** Show that the variation field of a geodesic variation obeys $D_\lambda^2\xi = -\mathcal{R}(\xi, u)u$.

1. For the Levi-Civita connection, $D_\lambda\xi = D_s u$, so $D_\lambda^2\xi = D_\lambda D_s u$.
2. For any field $Z$ along the map, $D_\lambda D_s Z - D_s D_\lambda Z = \mathcal{R}(u, \xi)Z$; the bracket term of $\mathcal{R}$ is absent because $[\partial_\lambda, \partial_s] = 0$.
3. Take $Z = u$. Each member is a geodesic, so $D_\lambda u = 0$ and $D_\lambda^2\xi = \mathcal{R}(u, \xi)u$.
4. Antisymmetry in the two slots gives $\mathcal{R}(u, \xi)u = -\mathcal{R}(\xi, u)u$.
5. With $(\mathcal{R}(X, Y)Z)^\rho = R^\rho{}_{\sigma\mu\nu}Z^\sigma X^\mu Y^\nu$, the components are $D_\lambda^2\xi^\mu = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

**Result:** $D_\lambda^2\xi = -\mathcal{R}(\xi, u)u$, the course geodesic deviation equation when $\lambda$ is proper time.

## Worked examples

### Meridians with a head start · working

**Problem:** On a sphere of radius $a$, with colatitude $\theta$ and longitude $\phi$, walkers leave the equator toward the North Pole along meridians. The label $s$ is arc length along the equator, and walker $s$ starts a distance $ks$ behind the equator. Find the deviation vector along the walker $s = 0$, split it into along-path and sideways parts, and evaluate both on Earth at latitude $45^\circ$ for $\delta s = 1$ m and $k\,\delta s = 3$ m.

1. Walker $s$, after arc length $\sigma$ from its own start, is at $\theta = \pi/2 - (\sigma - ks)/a$ and $\phi = s/a$. Each member is a meridian with arc-length parameter $\sigma$.
2. So $u = \partial_\sigma$ has $u^\theta = -1/a$, and $\xi = \partial_s$ has $\xi^\theta = k/a$ and $\xi^\phi = 1/a$.
3. With $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, $u\cdot\xi = a^2(-1/a)(k/a) = -k$. Since $u$ points forward, this is a part of length $k$ pointing backward, and it never changes.
4. On a surface $u\cdot u = +1$, so the sideways part is $\xi - (u\cdot\xi)u = \xi + ku$, with components $(0, 1/a)$. Its length is $a\sin\theta\cdot(1/a) = \sin\theta$, and on walker $s = 0$, $\sin\theta = \cos(\sigma/a)$, the cosine of the latitude.
5. Check with the first-derivative rule: $D\xi^\phi/d\sigma = \Gamma^\phi{}_{\theta\phi}u^\theta\xi^\phi = -\cot\theta/a^2$. Its length along the unit vector $\hat\phi$ is $a\sin\theta \times (-\cot\theta/a^2) = -\cos\theta/a$, which equals $d(\sin\theta)/d\sigma$.
6. At latitude $45^\circ$ on Earth, $\sigma = (\pi/4)(6371\ \text{km}) = 5004$ km. Multiplying by $\delta s$: 3 m backward along the path and $\cos 45^\circ \times 1\ \text{m} = 0.707$ m sideways, a total length $\sqrt{9 + 0.5} = 3.08$ m.

**Answer:** Per unit label, $\xi$ is $k$ backward along the path plus $\cos(\text{latitude})$ sideways. On Earth at $45^\circ$: 3 m backward and 0.707 m sideways, 3.08 m in all.

**Takeaway:** The along-path part records only where each walker started counting and never changes; the sideways part carries the geometry.

## Problems

### `string-at-the-pole` · entry · difficulty 2 · conceptual

On a huge smooth ball, Asha stands on the equator facing the North Pole. Ben stands one metre to her right, but four metres behind the equator, on the side away from the North Pole, also facing the North Pole. Both take one-metre steps, count them from their own starting spot, and walk straight. When Asha reaches the North Pole, how long is the string from Asha to Ben at the same count, and which way does it point? Are their paths four metres apart there?

**Hints**

1. Which part of the string never changes on the walk?

**Answer:** The string is four metres long and points back along Asha's path. The paths are not four metres apart: they meet at the North Pole, so the sideways part is zero.

**Must contain:** The along-path part stays four metres; The sideways part shrinks to nothing at the North Pole; The string is four metres long but the paths meet

**Numeric:** string length = 4 m (magnitude, ±0.2); sideways part = 0 m (magnitude, ±0.05)

**Solution**

1. At the start, the string from Asha to Ben has an along-path part of four metres, pointing behind Asha, and a sideways part of one metre.
2. Both friends add one metre with every count, so the along-path part stays four metres for the whole walk.
3. Both walk along lines from the equator to the North Pole, and those lines meet at the North Pole. So the sideways part shrinks to nothing there.
4. When Asha stands at the North Pole, the string is only its along-path part: four metres, pointing back along her path, toward Ben.
5. The distance between the paths is the sideways part, which is zero. The four metres come only from where Ben started counting.

**Targets:** `any-moments-will-do`

### `hubble-neighbours` · working · difficulty 2 · calculation

In a spatially flat expanding universe, $ds^2 = -c^2dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$, galaxies at fixed $(x, y, z)$ follow geodesics with proper time $t$. For two neighbouring galaxies separated by $\Delta x$ along $x$, use $D\xi^\mu/d\tau = \xi^\nu\nabla_\nu u^\mu$ to find how fast their proper separation $L$ grows. With $H_0 = 67.4$ km/s/Mpc, how much does a separation of 1 Mpc grow in one million years at today's rate?

**Hints**

1. With $x^0 = ct$, the nonzero Christoffel symbols are $\Gamma^i{}_{0j} = \Gamma^i{}_{j0} = \dot a\,\delta^i_j/(ca)$ and $\Gamma^0{}_{ij} = a\dot a\,\delta_{ij}/c$.
2. Use $u^\mu = (c, 0, 0, 0)$ and $\xi^\mu = (0, \Delta x, 0, 0)$, then $L^2 = g_{\mu\nu}\xi^\mu\xi^\nu$.

**Answer:** $dL/dt = HL$ with $H = \dot a/a$: about 69 pc, a fractional growth of $6.9\times10^{-5}$.

**Must contain:** The velocity gradient of comoving galaxies is H times the identity on space; Proper separation grows at the fractional rate H; About 69 parsecs per million years for 1 megaparsec

**Numeric:** growth of the separation = 68.9 pc (magnitude, ±3%)

**Solution**

1. $\xi^\nu\nabla_\nu u^i = \xi^j(\partial_j u^i + \Gamma^i{}_{j0}u^0) = \xi^j\,\frac{\dot a}{ca}\,\delta^i_j\,c = \frac{\dot a}{a}\xi^i$, and $\xi^\nu\nabla_\nu u^0 = \xi^j\Gamma^0{}_{j0}c = 0$.
2. So $D\xi^\mu/d\tau = H\xi^\mu$ with $H = \dot a/a$.
3. $u_\mu\xi^\mu = 0$, so $L^2 = g_{\mu\nu}\xi^\mu\xi^\nu$ and $d(L^2)/dt = 2g_{\mu\nu}\xi^\mu D\xi^\nu/dt = 2HL^2$, giving $dL/dt = HL$.
4. $H_0 = 67.4\ \text{km/s} / (3.0857\times10^{19}\ \text{km}) = 2.184\times10^{-18}\ \text{s}^{-1}$.
5. One million years is $3.156\times10^{13}$ s, so $\Delta L/L = H_0\Delta t = 6.89\times10^{-5}$.
6. For $L = 1$ Mpc $= 10^6$ pc, $\Delta L = 68.9$ pc. $H$ changes by far less than 1% in a million years, so today's rate is enough.

**Targets:** `lie-dragged-means-constant`

### `killing-field-along-an-orbit` · formal · difficulty 3 · proof

(a) Show that the restriction of a Killing vector field $K$ to any affinely parametrized geodesic is a deviation vector. (b) In Schwarzschild spacetime with $G = c = 1$, a satellite follows the circular geodesic $r = r_0 > 3M$ in the equatorial plane, with $u_\phi = L$ and $L^2 = Mr_0^2/(r_0 - 3M)$. A second satellite follows the same orbit a small angle $\delta\phi$ ahead. Using $K = \partial_\phi$, find the length of the orthogonal part of their separation, show that it never changes, and interpret the factor multiplying $r_0\,\delta\phi$.

**Hints**

1. Isometries map geodesics to geodesics and preserve affine parameters.
2. For unit-speed $u$, $|\xi_\perp|^2 = g(\xi, \xi) + g(u, \xi)^2$.
3. A static observer at $r_0$ measures the orbital speed $v$ with $v^2 = M/(r_0 - 2M)$.

**Answer:** $|\xi_\perp|\,\delta\phi = r_0\,\delta\phi\sqrt{(r_0 - 2M)/(r_0 - 3M)}$, constant along the orbit. The square root is the Lorentz factor of the orbit relative to static observers.

**Must contain:** The flow of a Killing field maps the geodesic to a family of geodesics with the same affine parameter; g of xi with itself and g of u with xi are both constant on the circular orbit; The orthogonal length is the Lorentz factor times r zero times the angle

**Solution**

1. The flow $\phi_s$ of $K$ consists of isometries. An isometry maps a geodesic with affine parameter $\lambda$ to a geodesic with the same affine parameter, so $x(\lambda, s) = \phi_s(\gamma(\lambda))$ is a geodesic variation.
2. Its variation field at $s = 0$ is $\partial_s\phi_s(\gamma(\lambda))|_{s=0} = K(\gamma(\lambda))$, which proves (a).
3. For $K = \partial_\phi$, $\phi_s$ rotates by angle $s$, carrying the circular orbit into the same orbit shifted in phase; the second satellite is $s = \delta\phi$ and $\xi = \partial_\phi$.
4. On the orbit, $g(\xi, \xi) = r_0^2$ and $g(u, \xi) = u_\phi = L$, both constant.
5. With $g(u, u) = -1$, $\xi_\perp = \xi + g(u, \xi)u$ has $g(\xi_\perp, \xi_\perp) = r_0^2 + L^2 = r_0^2\,(r_0 - 2M)/(r_0 - 3M)$, constant along the orbit.
6. Relative to static observers, $\gamma^2 = 1/(1 - v^2) = (r_0 - 2M)/(r_0 - 3M)$. Static observers measure the gap $r_0\,\delta\phi$ at fixed $t$; the satellites move along the gap, so in their rest frame it is longer by $\gamma$.

**Targets:** `steady-string-means-flat`

## Observations

- **The separation between LIGO's suspended mirrors changing as the gravitational wave GW150914 passed** (measured, working). In the signal's band, each mirror hangs from a pendulum and moves along its arm like a free mass. So each 4 km arm is a deviation vector between two freely falling mirrors, and laser light timing round trips measures its orthogonal part. *Numbers:* The signal swept from 35 to 250 Hz, wavelengths of 8600 to 1200 km, far longer than the arms. Peak strain $1.0\times10^{-21}$ over 4 km arms: the two arm lengths changed relative to each other by $hL = 4\times10^{-18}$ m, about $2\times10^{-18}$ m in each arm when the changes are equal and opposite. *Reference:* B. P. Abbott and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102
- **The growth of distances between galaxies moving with the cosmic expansion, summarized by the Hubble constant** (measured, working). Galaxies moving with the expansion follow geodesics whose proper time is cosmic time. For neighbours, the first-derivative rule gives $D\xi^\mu/dt = H\xi^\mu$, so every small separation grows at the fractional rate $H$. Distant galaxies need the full metric, because their redshifts and distances are no longer small. *Numbers:* From the cosmic microwave background, assuming the standard cosmological model: $H_0 = 67.4 \pm 0.5$ km/s/Mpc, a fractional growth of $6.9\times10^{-11}$ per year. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Pair walkers at matching counts** (entry). Set up the two walkers with a string at the same count, first on a playground and then on the ball, and ask for a prediction at the North Pole. *Why:* It names the deviation vector as something tied to both walkers before any symbol appears. *Predict:* When the friends reach the North Pole, how long will the string between them be? *Visual:* [[two-walkers-set-off-side-by-side]] *Uses:* `ways_in/string-between-two-walkers`, `checks/shrinking-string-on-a-ball`
2. **Move one starting spot** (entry). Put one walker three steps behind the line and split the string into its sideways and along-path parts. *Why:* It separates the bookkeeping part of the arrow from the part that carries geometry. *Predict:* If Ben starts three metres behind, will the string still halve two thirds of the way up? *Visual:* [[two-walkers-set-off-side-by-side]] *Uses:* `ways_in/three-steps-behind-the-line`, `checks/late-start-string`, `checks/one-behind-the-other`
3. **Differentiate the labelled family** (working). Define the deviation vector as a label derivative, commute the derivatives, and run the sphere example. *Why:* Two facts every calculus student knows give Lie dragging, the first-derivative rule and the fixed along-path part. *Visual:* [[elastic-arrow-between-two-beads]] *Uses:* `ways_in/label-the-family-and-differentiate`, `derivations/commuting-derivatives`, `worked_examples/meridians-with-a-head-start`, `checks/lie-dragged-claim`
4. **Measure it from free fall** (working). Show what radar and gyroscopes on one falling mass read, and connect it to a gravitational-wave detector arm. *Why:* It ties the orthogonal part to a measurement and exposes the along-path part as a clock setting. *Predict:* If one mass resets its clock, what changes in the radar reading? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/radar-from-a-falling-mass`, `checks/desynchronized-clocks`, `observations/gw150914-mirror-separation`
5. **Identify deviation vectors with Jacobi fields** (formal). Define geodesic variations, derive the Jacobi equation, count the solutions, and use a Killing field. *Why:* It gives graduate readers the exact object behind the pictures and its limits. *Uses:* `ways_in/variation-fields-and-jacobi-fields`, `checks/counting-deviation-fields`, `problems/killing-field-along-an-orbit`

## Misconceptions

### “The string between the walkers is just an arrow carried along without swinging, so it keeps its length.” · entry · `string-is-a-carried-arrow`

- **Why it is tempting:** Both are arrows that travel with the walkers.
- **What is true:** The string is tied to both walkers, so it follows the gap between their paths. A stiff carried arrow is tied only to one walker and keeps its length, while the string on a ball shrinks to nothing at the North Pole.
- **Exposed by:** `checks/shrinking-string-on-a-ball`

### “It does not matter which points of the two walks the string joins; its length is always how far apart the paths are.” · entry · `any-moments-will-do`

- **Why it is tempting:** When both walkers start level, every string at the same count runs across the paths at a right angle.
- **What is true:** A string between walkers who started counting at different spots gains a part along the path. Only the sideways part measures how far apart the paths are.
- **Exposed by:** `checks/late-start-string`

### “If the string between two straight walkers keeps its length, the ground must be flat.” · entry · `steady-string-means-flat`

- **Why it is tempting:** On a ball, side-by-side walkers draw together, so a steady string seems to rule out a ball.
- **What is true:** A string that lies along one straight path, between walkers taking equal steps, keeps its length on any ground. Whether the ground curves shows only in a sideways part.
- **Exposed by:** `checks/one-behind-the-other`

### “The deviation vector is Lie dragged, so the separation between neighbouring freely falling particles never changes.” · working · `lie-dragged-means-constant`

- **Why it is tempting:** A vanishing derivative usually means a constant quantity.
- **What is true:** Lie dragging only says the vector keeps joining the same two neighbours. Its covariant rate of change is the velocity gradient acting on it, which is usually not zero.
- **Exposed by:** `checks/lie-dragged-claim`

### “The deviation vector is always a spatial separation between the two particles.” · working · `deviation-vector-is-spatial`

- **Why it is tempting:** It is introduced as the gap between neighbours.
- **What is true:** Its part along the four-velocity comes from how the clocks are set and can even make it timelike. Only the orthogonal part is the separation an observer measures.
- **Exposed by:** `checks/desynchronized-clocks`

### “Any smooth vector field along a geodesic is the deviation vector of some family of geodesics.” · formal · `any-field-along-a-geodesic`

- **Why it is tempting:** The definition seems to allow any choice of neighbours.
- **What is true:** The neighbours must themselves be geodesics, which forces the Jacobi equation. A deviation vector is fixed by its value and first derivative at one point.
- **Exposed by:** `checks/counting-deviation-fields`

## Checks

1. **Entry · predict** `checks/shrinking-string-on-a-ball`. On a huge smooth ball, Asha and Ben start on the equator side by side, one metre apart, both facing the North Pole. Each takes one-metre steps, counts them, and walks straight. Asha also holds a one-metre cardboard arrow against the ground. It points at Ben at the start, and she never lets it swing. How long is the string from Asha to Ben at the same count two thirds of the way to the North Pole? How long is it at the North Pole? How long is the cardboard arrow at those two places?
   - **Hints:** Where do all the lines from the equator to the North Pole meet? / What does a carried arrow keep, whatever the ground does?
   - **Answer:** Half a metre, then nothing, while the cardboard arrow stays one metre long. Both friends walk along lines from the equator to the North Pole. At matching counts they have walked the same distance from the equator, so they stand on the same circle around the ball. The lines cut each such circle into equal pieces, so the string always covers the same fraction of the friends' circle as it did of the equator. Two thirds of the way up, that circle is half as long as the equator, so the string is 50 centimetres. All the lines meet at the North Pole, so there the string has shrunk to nothing. The cardboard arrow keeps its one-metre length the whole way, because it is stiff and tied only to Asha, not to Ben.
   - **Must contain:** 50 centimetres two thirds of the way up; Nothing at the North Pole; The carried arrow keeps its length, unlike the string
   - **Numeric:** string two thirds of the way = 50 cm (magnitude, ±3); string at the North Pole = 0 cm (magnitude, ±2); cardboard arrow at both places = 100 cm (magnitude, ±3)
   - **Targets:** `string-is-a-carried-arrow`
   - **Visual:** [[two-walkers-set-off-side-by-side]]
2. **Entry · numeric** `checks/late-start-string`. On a flat playground, Ben stands one metre to Asha's right and three metres behind her, both facing the same way. Each counts one-metre steps from their own starting spot and walks straight. At count 200, how long is the string from Asha to Ben at the same count? How far apart are their paths?
   - **Hints:** Where is Ben compared with Asha after each count?
   - **Answer:** About 3.2 metres, but the paths are one metre apart. Each count moves both friends one metre ahead, so at every count Ben is three metres behind Asha and one metre to her right. So the string has an along-path part of three metres and a sideways part of one metre. By Pythagoras's rule its length times itself is 9 plus 1, which is 10, so it is about 3.2 metres. Only the sideways part measures how far apart the paths are: one metre.
   - **Must contain:** Along-path part three metres, sideways part one metre; String about 3.2 metres long; The paths are one metre apart
   - **Numeric:** string length = 3.16 m (magnitude, ±3%); distance between the paths = 1 m (magnitude, ±0.05)
   - **Targets:** `any-moments-will-do`
   - **Visual:** [[two-walkers-set-off-side-by-side]]
3. **Entry · explain** `checks/one-behind-the-other`. On a huge smooth ball, Asha and Ben stand on the equator, both facing the same way along it, with Ben three metres behind Asha. Both take one-metre steps, count from their own starting spot, and walk straight, so both follow the equator. When Asha has walked a quarter of the way around the equator, how long is the string from Asha to Ben at the same count? Suppose the friends did not know they were on a ball. Would this steady string tell them that the ground is flat?
   - **Hints:** Is any part of this string sideways?
   - **Answer:** Three metres, and no. Ben walks the same path as Asha, three metres behind, so the string lies along the path: it is all along-path part. That part stays three metres, because both friends add one metre with every count. The string has no sideways part, and only a sideways part can show paths drawing together or spreading apart. On the same ball, friends who start side by side on the equator, one metre apart and facing the North Pole, do draw together.
   - **Must contain:** Three metres; The string is all along-path part, which never changes; Curving shows only in a sideways part
   - **Numeric:** string length = 3 m (magnitude, ±0.1)
   - **Targets:** `steady-string-means-flat`
4. **Working · numeric** `checks/desynchronized-clocks`. In flat spacetime, observers at rest sit at $x = s$ along a line, one for each $s$ in metres. Observer $s$ has a clock that reads $\tau = t - ks$, with $k = 10$ ns per metre. With $x^0 = ct$, find the deviation vector $\xi^\mu = \partial x^\mu/\partial s$, its squared length, and its part orthogonal to $u^\mu$.
   - **Hints:** At what coordinate time does observer $s$ read $\tau$? / Project with $\delta^\mu{}_\nu + u^\mu u_\nu/c^2$.
   - **Answer:** Observer $s$ reaches proper time $\tau$ at $t = \tau + ks$, so $x^\mu(\tau, s) = (c(\tau + ks), s, 0, 0)$ and $\xi^\mu = (ck, 1, 0, 0) = (3.00, 1, 0, 0)$. Its squared length is $1 - (ck)^2 = -7.99$, so it is timelike. With $u^\mu = (c, 0, 0, 0)$, $u_\mu\xi^\mu = -c^2k$, and $\xi_\perp^\mu = \xi^\mu + (u_\nu\xi^\nu)u^\mu/c^2 = (0, 1, 0, 0)$: neighbours one metre of label apart are one metre apart. The timelike part came only from the clock settings.
   - **Must contain:** The deviation vector is (ck, 1, 0, 0); Its squared length is about minus 8, so it is timelike; The orthogonal part is a unit spatial vector
   - **Numeric:** squared length per unit label squared = -7.99 1 (signed, ±0.05); length of the orthogonal part per unit label = 1 1 (magnitude, ±0.01)
   - **Targets:** `deviation-vector-is-spatial`
5. **Working · evaluate-claim** `checks/lie-dragged-claim`. A student writes: "The deviation vector is Lie dragged along the geodesics, $\mathcal{L}_u\xi = 0$, so the separation between neighbouring freely falling particles never changes." Evaluate the claim.
   - **Hints:** What are the components of $\xi$ in the labels $(\tau, s)$, and what is its length?
   - **Answer:** The premise is right and the conclusion wrong. $\mathcal{L}_u\xi = [u, \xi] = 0$ says only that $\xi$ keeps joining the same two members: in the labels $(\tau, s)$ its components stay $(0, 1)$. A separation changes at the covariant rate $D\xi^\mu/d\tau = \xi^\nu\nabla_\nu u^\mu$, which is not zero when the velocities vary across the family. For galaxies moving with the cosmic expansion it is $H\xi^\mu$, so their separation grows.
   - **Must contain:** Lie dragging means the vector keeps joining the same neighbours; The covariant rate of change is the velocity gradient acting on xi; Comoving galaxies separate at the rate H
   - **Targets:** `lie-dragged-means-constant`
   - **Visual:** [[elastic-arrow-between-two-beads]]
6. **Formal · derive** `checks/torsion-and-symmetry`. For a smooth two-parameter family of curves $x(\lambda, s)$, not necessarily geodesics, show that $D_\lambda\xi - D_s u$ is set by the torsion. What does this give for the Levi-Civita connection, and does the geodesic condition enter?
   - **Hints:** Write both covariant derivatives in components along the map.
   - **Answer:** In components $D_\lambda\xi^\mu = \partial_\lambda\partial_s x^\mu + \Gamma^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$ and $D_s u^\mu = \partial_s\partial_\lambda x^\mu + \Gamma^\mu{}_{\alpha\beta}\xi^\alpha u^\beta$. The partials cancel, leaving $(\Gamma^\mu{}_{\alpha\beta} - \Gamma^\mu{}_{\beta\alpha})u^\alpha\xi^\beta = T^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$. The Levi-Civita connection is torsion-free, so $D_\lambda\xi = D_s u$. The geodesic condition never enters; it matters only for the second derivative.
   - **Must contain:** Mixed partials of the map cancel; The difference is the torsion acting on u and xi; No geodesic condition is used
7. **Formal · explain** `checks/counting-deviation-fields`. Along a timelike geodesic in four-dimensional spacetime, how many linearly independent deviation vector fields are there? Which describe no physical separation, and why is a generic smooth vector field along the geodesic not the deviation vector of any family?
   - **Hints:** What initial data fix a solution of a linear second-order equation?
   - **Answer:** Eight. Deviation vectors are exactly the Jacobi fields, solutions of a linear second-order equation, so they are fixed by $\xi$ and $D_\lambda\xi$ at one event: $4 + 4 = 8$. The fields $(a + b\lambda)u$ solve it, because $D_\lambda^2 u = 0$ and $\mathcal{R}(u, u)u = 0$, and they come from reparametrizing the members, so two carry no separation. That leaves six physical ones, the Jacobi fields orthogonal to $u$ with orthogonal first derivative. A generic field fails the Jacobi equation, and only its solutions are variation fields.
   - **Must contain:** Eight, from four initial values and four initial rates; Two tangential fields come from reparametrizing; Six physical fields; Only solutions of the Jacobi equation are deviation vectors
   - **Numeric:** independent deviation fields = 8 1 (magnitude, ±0.1); physical deviation fields = 6 1 (magnitude, ±0.1)
   - **Targets:** `any-field-along-a-geodesic`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the projector onto an observer's rest space | With signature $(-,+,+,+)$ and $u_\mu u^\mu = -c^2$: $h^\mu{}_\nu = \delta^\mu{}_\nu + u^\mu u_\nu/c^2$. | With signature $(+,-,-,-)$ and $c = 1$ the same projector is $\delta^\mu{}_\nu - u^\mu u_\nu$. Keep one index up and one down on the $uu$ term. |
| Names and symbols for the deviation vector | $\xi^\mu = \partial x^\mu/\partial s$, the deviation vector; its orthogonal part is $\xi_\perp^\mu$. | Some texts write $\eta$, $n$, $Z$, $J$ or $s$, and call it a connecting, separation or Jacobi vector; some reserve a symbol for the orthogonal part. The letter $n$ may also be the family label or the dimension. |
| Slot order and sign in the deviation equation | $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma = +R^\mu{}_{\nu\rho\sigma}u^\nu u^\rho\xi^\sigma$. | Texts with the opposite overall sign of the Riemann tensor, or with the separation in another slot, print a different sign. Check on a sphere, where neighbouring geodesics that start parallel converge. |

## Visuals

- ★ [[two-walkers-set-off-side-by-side]] (flagship): Flagship entry picture: a string at matching counts between two straight walkers on a playground or a ball, with a head start that splits it into sideways and along-path parts. *Sketch:* This concept adds step counters, a string drawn between the walkers at the same count, a 'start behind the line' slider, and readouts of the string's length, sideways part and along-path part. A toggle shows a carried cardboard arrow beside the string: it keeps its length while the string shrinks toward the North Pole.
- [[elastic-arrow-between-two-beads]] (core): Lie dragging and the first-derivative rule. *Sketch:* Two beads ride neighbouring members of a family: galaxies in a uniform expansion, a shearing flow, or meridians on a sphere. An elastic arrow joins them at equal parameter and stretches and turns. Toggles add a copy with frozen components, which drifts off the second member, and a parallel-carried copy. A readout compares the arrow's rate of change with the velocity gradient acting on it.
- [[falling-ring-of-crumbs]] (supporting): Radar between freely falling crumbs reads the orthogonal part of each deviation vector. *Sketch:* A ring of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it. One crumb times light echoes from its neighbours to find each separation; resetting a neighbour's clock changes only the along-path part, never the echo time.

## Tutor moves

**Open with**

- Two friends stand one metre apart on the equator of a huge smooth ball, both facing the North Pole. They walk without steering, taking equal steps. When they have walked two thirds of the way to the North Pole, how far apart will they be? *(prediction)*
- Picture a stretchy string tied between two people who walk side by side at the same pace, neither of them ever steering. On flat ground the string keeps its length. What kind of ground could make it go slack or pull tight? *(reflection)*

**If the learner is stuck**

- *The learner stretches the string to the nearest point of the other path instead of the same count.* → Have the learner number each step on both paths and join equal numbers, then compare with the nearest-point string. *Uses:* `ways_in/three-steps-behind-the-line`, `checks/late-start-string`
- *The learner treats the along-path part as a real distance.* → Reset one clock in the desynchronized-clocks setup and ask what radar would read before and after. *Uses:* `checks/desynchronized-clocks`, `ways_in/radar-from-a-falling-mass`

**Common questions**

- *Does a bigger ball make the string shrink differently?* (entry) Two thirds of the way to the North Pole, the string is half its starting length on a ball of any size. On a bigger ball the friends need more steps to get there, so the string shrinks more slowly with each kilometre walked. *Uses:* `ways_in/string-between-two-walkers`
- *Why pair the walkers by their counts instead of by a clock?* (entry) Counting equal steps pairs the spots where the two friends have walked the same distance, and that keeps the along-path part fixed. If both walk at the same steady pace, a clock gives the same pairing. If one walks faster, pairing by the clock would join spots at different distances walked, so the along-path part would keep growing. For things falling freely through space, each one's own wristwatch plays the part of the count. *Uses:* `ways_in/three-steps-behind-the-line`

**Switching levels**

- To working when: asks how to compute the arrow; uses derivatives or components. Define the deviation vector as a label derivative and work the sphere example. *Uses:* `ways_in/label-the-family-and-differentiate`, `worked_examples/meridians-with-a-head-start`
- To formal when: asks which fields can be deviation vectors; mentions Jacobi fields or conjugate points. Go to geodesic variations, the Jacobi equation and the counting check. *Uses:* `ways_in/variation-fields-and-jacobi-fields`, `checks/counting-deviation-fields`
- To research when: asks about focusing, singularity theorems or gravitational lensing. Open the research horizon. *Uses:* `research_horizon/focusing-and-singularity-theorems`, `research_horizon/null-deviation-and-lensing`

**Pronunciations:** ξ (xi) → ksai; Jacobi → yah-KOH-bee; Levi-Civita → LEH-vee CHEE-vee-tah; Pirani → pih-RAH-nee; Raychaudhuri → ray-CHOW-dhuh-ree

**Voice notes:** With beginners, say 'the string' until the deviation vector is named, call it stretchy, and always say which friend it points from. Say xi as 'ksai'.

## History

- **Carl Gustav Jacob Jacobi (1837).** In the calculus of variations, introduced the linear equation for the difference between neighbouring extremal curves and the conjugate points where such a difference vanishes again. C. G. J. Jacobi (1837), *Zur Theorie der Variations-Rechnung und der Differential-Gleichungen*, Journal für die reine und angewandte Mathematik 17, 68–82, doi:10.1515/crll.1837.17.68
- **Tullio Levi-Civita (1927).** Derived, for Riemannian manifolds of any dimension, how the Riemann tensor governs the deviation between neighbouring geodesics. Tullio Levi-Civita (1927), *Sur l'écart géodésique*, Mathematische Annalen 97, 291–320, doi:10.1007/BF01447869
- **Felix Pirani (1956).** Showed how an observer measures the Riemann tensor in general relativity by tracking deviation vectors to neighbouring freely falling particles in a parallel-propagated frame. F. A. E. Pirani (1956), *On the physical significance of the Riemann tensor*, Acta Physica Polonica 15, 389–405

## Research horizon

- **Focusing and singularity theorems.** The deviation vectors of a congruence evolve by the velocity gradient, whose trace, trace-free symmetric and antisymmetric parts are the expansion, shear and rotation. The Raychaudhuri equation drives the expansion; for a rotation-free congruence that is converging somewhere, an energy condition forces focusing within finite affine parameter, where deviation vectors vanish at conjugate or focal points, provided the geodesics extend that far. That focusing step underlies Penrose's singularity theorem. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123; Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57
- **Null deviation and gravitational lensing.** For light rays, deviation vectors live in a two-dimensional screen space. Their evolution, described by optical scalars, gives the Jacobi map from angles at the observer to sizes at the source, and with it angular-diameter distances, magnification and the shear that weak lensing measures. R. K. Sachs (1961), *Gravitational waves in general relativity. VI. The outgoing radiation condition*, Proceedings of the Royal Society of London A 264, 309–338, doi:10.1098/rspa.1961.0202; Volker Perlick (2004), *Gravitational lensing from a spacetime perspective*, Living Reviews in Relativity 7, 9, doi:10.12942/lrr-2004-9
- **Geodesic deviation beyond first order.** When neighbours are not close compared with the curvature scale, the first-order deviation vector is not enough. Expanding a family of geodesics to higher order in the label reproduces, for example, nearby eccentric orbits as epicycles about a circular one. R. Kerner, J. W. van Holten, R. Colistete Jr. (2001), *Relativistic epicycles: another approach to geodesic deviations*, Classical and Quantum Gravity 18, 4725–4742, doi:10.1088/0264-9381/18/22/302

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** Two friends, Asha and Ben, walk without ever steering and count their one-metre steps. Between them you imagine a stretchy string joining the spots they reach at the same count, and that string is the deviation vector, with an arrowhead at Ben's end. On flat ground it stays one metre long. On a ball the size of Earth, starting on the equator and facing the North Pole, their two lines close up: two thirds of the way the string is 50 centimetres, and at the pole it is nothing. A stiff cardboard arrow that Asha carries does not shrink, because it is tied only to her. I was told the two friends each follow one of the lines printed on a globe, and that puzzled me, because the lines on my globe are hundreds of kilometres apart and these two friends are one metre apart. If Ben starts three metres behind, the string is about 3.2 metres long but the paths are still one metre apart: three metres of the string lies along the path and one metre runs across it, and only the across part says how far apart the paths are. When they tried that start on the ball I could not picture where Ben stood, because 'three metres behind the equator' does not say which side of it. And the small-print line said 'for friends one metre apart', when the two friends in that walk are 3.2 metres apart, so I did not know which distance the tiny number belonged to.

**Stumbles (8)**

- “A stretchy string from one straight walker to a neighbour at the same step count”: 'Straight walker' makes 'straight' describe the person. The note's own words are 'walks straight', and 'straight walker' is not one of the glossary's forms, so I read it twice. The neighbour is never said to walk straight either, although the whole idea needs both of them to.
- “Only its part running across the paths measures how far apart the paths are; any part lying along the paths comes from where each friend started counting.”: The friends in this summary walk side by side, so there is no part lying along the paths. I cannot picture the part the sentence warns me about, or what would ever make one.
- “Now picture a stretchy string running from Asha to Ben, with its ends at matching counts.”: An end cannot be at a count, because a count is a number and not a place, so I had to reread the sentence. The sentence after it already gives the concrete version.
- “Walking straight, each follows one of the lines printed on a globe from the equator to the North Pole.”: The try-it asks me to pick up a globe, and the lines printed on it are hundreds of kilometres apart at the equator, while Asha and Ben are one metre apart. So they cannot each be standing on a printed line, and the first thing I check contradicts the sentence.
- “Compare a stiff cardboard arrow that Asha holds against the ground.”: The string is given a length, the arrow is not, yet the check 'shrinking-string-on-a-ball' asks how long the arrow is and this way is where I am meant to learn it.
- “The deviation vector is a short string from one walker to a neighbour at the same count.”: Everywhere else the string is stretchy, and being stretchy is what lets it shrink. The sentence I am meant to say back drops that word and puts a different adjective on the same object.
- “Asha stands on the equator, and Ben stands one metre to her right and three metres behind the equator. Both face the North Pole.”: 'Behind the equator' gives no reference, because a line has no behind, and the sentence that says which way they face only comes afterwards. So I could not place Ben. The note's own problem 'string-at-the-pole' says 'on the side away from the North Pole', which is what is missing here.
- “Keeps the friends a few metres apart. For friends one metre apart on an Earth-sized ball, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.”: In this walk the friends are about 3.2 metres apart and their paths are one metre apart, so 'friends one metre apart' clashes with the way and with 'a few metres apart' in the sentence before it. I could not tell which distance the tiny number belongs to. The revision-5 sign-off recorded this and left the rewrite for an editor.

**Fixes**

- Retell compared with the entry takeaways: the reader came back with the shrinking string (50 centimetres, then nothing), the carried arrow that keeps its length, and the 3.2-metre string across one-metre paths, so both entry takeaways landed. What tripped the retelling was placing things, not the physics: where Ben stands on the ball, which lines the friends follow, and which distance the small-print number is about. All three are now said outright.
- Tagline and summary: 'one straight walker' becomes 'two neighbours who walk without steering', the note's own wording. The summary now names one friend's later start as what makes a part lying along the paths, instead of warning about a part its own side-by-side picture cannot show. Average summary sentence length is 19 words.
- 'A string between two walkers': dropped 'with its ends at matching counts', because the next sentence gives the same thing concretely; gave the cardboard arrow the one-metre length its check asks for; and the friends' two lines are now 'like the lines printed on a globe but only one metre apart at the equator', so a reader holding a globe is not told something the globe contradicts. The takeaway now says 'short, stretchy string', the word the rest of the note uses.
- 'Three steps behind the line': the ball start now fixes the facing first and places Ben three metres behind Asha, on the side of the equator away from the North Pole, matching the wording the problem 'string-at-the-pole' already uses.
- 'Three steps behind the line' simplifies: applied the rewrite the revision-5 sign-off proposed and left for an editor, so 'For friends one metre apart' reads 'For paths one metre apart ... as in this walk'. The bound is unchanged and still holds: recomputed the change in the sideways part over the whole walk for paths one metre apart on a ball of radius 6,371 kilometres, and its largest value is 0.0005 millimetres, under a thousandth of a millimetre.
- Ladder read: every non-entry way still opens by naming the way it continues, no changed sentence touches a working, formal or research field, and no symbol or notation moved to a lower rung. The five ways remain five different kinds: picture, contrast, calculation, operational and structure.
- Nothing was dropped and no sentence was compressed. Entry way explanations go from 932 to 948 words, inside the 1,000-word cap.
- This pass rewrote the top-level novice record, which had covered revision 2. The earlier retelling and its twenty-three stumbles are kept in the snapshot deviation-vector.before-novice2.json and in git history, and the two re-reads are kept in rereads.
- Bumped the revision to 6.

**Concerns**

- review.physics covers revision 5, so the six changed entry strings need a physics diff check. None of them changes a claim, a number or a sign; the only number-bearing sentence is the simplifies bound, which was recomputed here.
- The note still has no analogy at any rung, because the drafting stage cut the only entry one for budget. Entry explanations sit at 948 of 1,000 words and tutoring at 2,771 of 3,300, so there is room for one.
- The prerequisite notes geodesic, affine-parameter, congruence-of-curves, lie-dragging, lie-bracket and killing-vector do not exist yet, and two ways also assume covariant-derivative-along-a-curve and proper-time. The entry recap's mirror-image reason for straight globe lines came from parallel-postulate, and geodesic should use the same reason when it is written.
- All three visuals are still proposals. two-walkers-set-off-side-by-side should call the string stretchy, put its arrowhead at the neighbour's end, pair spots by step count even when one walker is faster, and draw the two walkers' lines one metre apart rather than as the printed lines of a globe.
- The registry's prerequisite list for this concept still lacks lie-bracket, riemann-curvature-tensor and killing-vector, and course-conventions.md still fixes no symbol for the orthogonal part of the deviation vector and no torsion convention, both of which this note uses.

**Re-read** (2026-09-13, revision 4): 2 stumbles in 5 changed passages

- “On an Earth-sized ball, moving Ben's start three metres back then changes the sideways part by less than a thousandth of a millimetre.”: 'Then' can read as 'afterwards, later in the walk' rather than 'with the friends kept this close', so the reader cannot tell which condition the tiny change depends on.
- “The wave was more than a thousand kilometres long, so the first-order description holds across an arm.”: For a wave, 'long' can mean how long the signal lasted or how far the wave train reached; the argument needs the wavelength, and the comparison with the 4 km arm is left for the reader to supply.
- Fix: 'Three steps behind the line' simplifies: replaced the ambiguous 'then' with 'For friends this close'; the bound, scope and numbers are unchanged.
- Fix: 'Radar from a falling mass': 'the wave was more than a thousand kilometres long' now names the wavelength and compares it with the 4 km arm stated in the same paragraph; the claim is unchanged.
- Fix: Read without stumbles: the new deviation-vector naming sentence ('how far Ben stands from Asha at the same count'), the explicit relabelling $x^\mu(\tau + f(s), s)$, the accelerometer in the observer's kit, and the Sachs title punctuation (research reference).

**Re-read** (2026-09-13, revision 5): 1 stumbles in 1 changed passages

- “Keeps the friends a few metres apart. For friends one metre apart on an Earth-sized ball, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.”: The way says the string between the friends is about 3.2 metres while their paths are one metre apart, so 'friends one metre apart' clashes both with that and with 'a few metres apart' just before; the reader cannot tell whether the bound is about the paths' distance, the friends' distance, or a different, closer pair.

**Re-read** (2026-09-16, revision 7): 0 stumbles in 9 changed passages

- Fix: No wording changed. Read each changed sentence inside its paragraph as the novice: the globe-lines sentence now says the friends' lines are only one metre apart, Ben's ball start names the side of the equator he stands on, and the simplifies bound names the paths' one-metre distance, so the three stumbles of the earlier retell no longer occur. The formal renaming of the reparametrization constants to a and b, read as a second-year undergraduate, keeps them apart from the alpha and beta of g(u, xi).

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Entry, 'A string between two walkers': two thirds of the way to the North Pole the string halves, after about 6,700 kilometres, and it is nothing at the pole.: python3: latitude 60 degrees is two thirds of the way from the equator, cos 60 = 1/2; meridian arc (pi/3) x 6371 km. → 0.500 and 6,672 km; all meridians meet at the pole. Correct.
- Entry: after one kilometre the one-metre string is shorter by about 12 millionths of a millimetre, less than a thousandth of a hair's width.: python3: 1 m x (1 - cos(1 km / 6371 km)); hair widths 17 to 180 micrometres. → 1.232e-8 m = 12.3 millionths of a millimetre; a thousandth of even a thin 17-micrometre hair is 1.7e-8 m. Correct.
- Novice rewrite, 'Three steps behind the line' simplifies: for paths one metre apart on an Earth-sized ball, as in this walk, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.: python3 on a sphere of radius 6371 km: Asha on a meridian, Ben one metre of equatorial arc to her right, his start at the equator or three metres behind it; compared at equal counts over the whole walk, both as the component of the Asha-to-Ben chord perpendicular to Asha's heading and as the great-circle distance from Ben to Asha's meridian. Repeated for paths 3 m and 5 m apart. → Largest change 0.00047 mm, with Asha at the pole, under the stated bound and the same under both readings of 'sideways part'. At 3 m it is 0.0014 mm and at 5 m 0.0024 mm, so scoping the sentence to one-metre paths is exactly what the bound needs. Accurate.
- Novice rewrite, summary: any part lying along the paths comes from one friend starting to count further back.: g(u, xi) is constant along each member (derivation 'Commuting derivatives along and across the family'), and zero when the two set off level with equal step lengths. Tried the what-ifs: walking the equator, a bigger ball, and a neighbour whose straight path is a tilted great circle rather than a meridian. → True in every case inside the way's equal-step scope, and symmetric: a part pointing ahead means the other friend started counting further back. Accurate.
- Novice rewrite, 'A string between two walkers': each follows a line from the equator to the North Pole, like the lines printed on a globe but only one metre apart at the equator.: Meridians are geodesics, by the mirror symmetry of the sphere across the meridian plane; their separation is a sin(colatitude) times the longitude difference, so it is one metre at the equator. → Correct, and now consistent with the try_it, which uses the globe's own printed meridians rather than the friends' paths. Accurate.
- Novice rewrite, 'Three steps behind the line': Asha on the equator facing the North Pole; Ben facing the same way, one metre to her right and three metres behind her, on the side of the equator away from the North Pole. Sideways part halves to 50 cm, along-path part stays three metres, whole string about 3.2 m to about 3.0 m.: Placed both on a 6371 km sphere: facing the North Pole, Asha's right runs along the equator, so Ben's meridian is one metre of equatorial arc away and his start is three metres of meridian arc on the far side. python3 for the sideways and along-path parts at equal counts. → Placement consistent; sideways 1.000 m at the start and 0.500 m at latitude 60, along-path 3.000 m throughout, string 3.162 m then 3.041 m. 'About 3.2' and 'about 3.0' are right, and it has not halved. Accurate.
- Novice rewrites, remaining three: the cardboard arrow is one metre long; the takeaway says 'short, stretchy string'; the tagline says 'two neighbours who walk without steering'.: Parallel transport preserves length, and the east direction is parallel-transported along a meridian, so the carried arrow keeps both its length and its bearing. Compared the added length with check 'shrinking-string-on-a-ball', whose numeric field answers 100 cm. → The arrow's new length agrees with the check, nothing else in the note gives it another length, and neither the takeaway nor the tagline changes a claim. Accurate.
- Entry: 'Neither friend started ahead, and both take equal steps, so the string runs across their paths at a right angle', carried over to the ball.: python3: along-path component of the Asha-to-Ben chord for one-metre friends at latitudes 0, 45, 60 and 89.99 degrees. → At most 4e-8 m out of one metre, 4e-6 degrees from perpendicular. Correct at entry precision.
- Entry checks and problem: shrinking-string-on-a-ball (50 cm, nothing, 100 cm), late-start-string (3.16 m, paths 1 m), one-behind-the-other (3 m), string-at-the-pole (4 m, sideways 0).: python3: sqrt(10); cos 60; pole case by the 3D chord with Ben four metres from the pole at longitude 1 m / a. → 3.1623 m; 0.5 m, 0 m, 1 m; 3 m; pole chord 4.00000000 m with a lateral offset of 6.3e-7 m. Every numeric field and tolerance holds.
- Derivation 'Commuting derivatives along and across the family': D xi^mu / d tau = xi^nu nabla_nu u^mu, and u.xi is constant along each member.: Re-derived in the course conventions, with the derivative index first on the Christoffel symbols and their lower pair symmetric; metric compatibility for step 6, and u.u = -c^2 for every member in step 9. Checked the factor of one half in step 8. → Correct at every step, including index placement and the factor of one half.
- Working and notation trap: h^mu_nu = delta^mu_nu + u^mu u_nu / c^2 gives u.xi_perp = 0 in signature (-,+,+,+), and the variant delta^mu_nu - u^mu u_nu holds in (+,-,-,-) with c = 1.: Contracted the projector with u_mu in both signatures. → Both correct; the sign follows from u.u = -c^2 and +1 respectively.
- Working: relabelling x^mu(tau, s) to x^mu(tau + f(s), s) adds f'(s) u^mu to xi^mu, and the along-path part drops out of the deviation equation.: Differentiated the relabelled family with respect to s; contracted -R^mu_{nu rho sigma} u^nu u^rho u^sigma using the antisymmetry of the Riemann tensor's last index pair, and checked D^2(alpha u)/d tau^2 = 0. → +f'(s) u^mu confirmed; the tangential piece gives zero on both sides of the deviation equation. Correct.
- Worked example 'Meridians with a head start': u^theta = -1/a, xi = (k/a, 1/a), u.xi = -k, sideways length sin theta = cos(latitude), D xi^phi / d sigma = -cot theta / a^2 = d(sin theta)/d sigma, and the numbers at latitude 45 degrees.: Hand computation with Gamma^phi_{theta phi} = cot theta and Gamma^theta_{phi phi} = -sin theta cos theta; checked that xi_perp has the same phi component as xi because Du/d sigma = 0; python3 for 5003.8 km, cos 45 and sqrt(9.5). → Every step correct; the covariant rate equals the derivative of the sideways length, and the totals are 3 m backward, 0.707 m sideways, 3.082 m in all.
- Problem 'hubble-neighbours': Gamma^i_{0j} = a-dot delta^i_j / (c a), Gamma^0_{ij} = a a-dot delta_{ij} / c, D xi^mu / dt = H xi^mu, dL/dt = H L, and 68.9 pc per million years for 1 Mpc at today's rate.: Hand Christoffel symbols for ds^2 = -(dx^0)^2 + a^2 dx.dx with x^0 = ct, including Gamma^0_{j0} = 0 which the solution's second half needs; python3 with 1 Mpc = 3.0857e19 km and the Julian year; drift of H from H-dot = -H^2 (1 + q) with q about -0.53. → H_0 = 2.1843e-18 per second, 6.893e-5 per million years, 68.93 pc, inside the 3% tolerance; H itself drifts by about 3e-5 per million years, so 'far less than 1%' holds.
- Check 'desynchronized-clocks': xi^mu = (ck, 1, 0, 0) = (3.00, 1, 0, 0), squared length 1 - (ck)^2 = -7.99, xi_perp^mu = (0, 1, 0, 0).: python3 with c = 299792458 m/s and k = 1e-8 s per metre; projected with delta^mu_nu + u^mu u_nu / c^2. → ck = 2.9979, squared length -7.9876, orthogonal part a unit spatial vector. Inside the stated tolerance of 0.05, and dimensionless as the unit field says.
- Working 'Radar from a falling mass': tau_m = (tau_1 + tau_2)/2, L = c(tau_2 - tau_1)/2 measures the orthogonal part, and u_mu xi^mu delta s = c^2 (tau_B - tau_m).: Applied both to the desynchronized-clocks family, where u.xi = -c^2 k and B's clock reads tau_m - k delta s at the reflection event in A's rest space. → Sign and magnitude agree, so the clock-offset reading is right; the relative-speed correction to clock rates is second order in the separation, as the way says.
- Observation and working way, GW150914: 35 to 250 Hz, wavelengths 8600 to 1200 km, peak strain 1.0e-21, arm lengths changing relative to each other by 4e-18 m over 4 km arms, about 2e-18 m per arm.: python3: wavelength c/f across the sweep; differential arm change h L with h the differential strain. → 8565 km and 1199 km, so 'more than a thousand kilometres' holds across the whole sweep and a 4 km arm is under half a percent of it; 4.0e-18 m differential and 2.0e-18 m per arm for equal and opposite changes. Correct.
- Formal way and its derivation: D_lambda xi^mu - D_s u^mu = T^mu_{alpha beta} u^alpha xi^beta; g(u, xi) = alpha + beta lambda with beta = 0 for a shared normalization; D_lambda^2 xi = -R(xi, u) u with components -R^mu_{nu rho sigma} u^nu xi^rho u^sigma; every Jacobi field is a variation field; 2n fields and 2n - 2 physical ones.: Components with the course Christoffel index order and T(X, Y) = nabla_X Y - nabla_Y X - [X, Y]; partial_lambda g(u, xi) = (1/2) partial_s g(u, u); the pulled-back identity D_lambda D_s Z - D_s D_lambda Z = R(u, xi) Z with R(X, Y) = [nabla_X, nabla_Y] - nabla_{[X, Y]} and (R(X, Y)Z)^rho = R^rho_{sigma mu nu} Z^sigma X^mu Y^nu, which is the course commutator; initial-data count for a linear second-order system; the exponential-map construction's initial data; sphere test with converging meridians. → All correct and in the course conventions: the components match the conventions geodesic-deviation row, the sphere gives D^2|xi| = -K|xi| and converging meridians, and the counting gives 8 and 6 as the check answers say.
- Formal way: the tangential fields written (alpha + beta lambda) u, with the same two letters used for g(u, xi) = alpha + beta lambda.: Reparametrized a family with g(u, xi) = 0 by x(lambda + a s, s) and by x((1 + b s) lambda, s), then computed g(u, xi) of each result on a unit-speed timelike geodesic, and cross-checked beta = (1/2) partial_s g(u, u) for the rescaled family. → Error found: the field (a + b lambda) u has g(u, xi) = -(a + b lambda), so the two uses of alpha and beta differ by a sign, and a reader combining the two sentences gets the wrong sign. Fixed by giving the tangential fields their own letters and stating alpha = -a and beta = -b.
- Problem 'killing-field-along-an-orbit': |xi_perp|^2 = r0^2 + L^2 = r0^2 (r0 - 2M)/(r0 - 3M) with L^2 = M r0^2/(r0 - 3M), equal to the square of the Lorentz factor of the orbit relative to static observers, and constant along the orbit.: Hand algebra with g(u, u) = -1, g(xi, xi) = r0^2 and g(u, xi) = L, using xi_perp = xi + g(u, xi) u; python3 at M = 1, r0 = 10; v^2 = M/(r0 - 2M) for the circular geodesic. → 114.2857 both ways and gamma^2 = 1.142857 both ways. Correct, and the length-contraction reading holds because the static observers' simultaneity surfaces are t = constant.
- All ten references: Abbott et al. 2016, Planck 2018 VI, Jacobi 1837, Levi-Civita 1927, Pirani 1956, Raychaudhuri 1955, Penrose 1965, Sachs 1961, Perlick 2004, Kerner, van Holten and Colistete 2001.: WebSearch plus publisher and archive records: De Gruyter for Crelle 17, Springer and EUDML for Mathematische Annalen 97, ADS for Acta Physica Polonica 15, IOPscience for Classical and Quantum Gravity 18. → All confirmed, authors, years, titles, venues and page ranges; the Classical and Quantum Gravity DOI 10.1088/0264-9381/18/22/302, which the previous pass could not confirm, is confirmed on the publisher's record and added.
- History scope: Jacobi introduced the equation for the difference between neighbouring extremals and its conjugate points; Levi-Civita derived n-dimensional geodesic deviation; Pirani gave the observer's reading in a parallel-propagated frame.: Publisher abstracts and the republication record of Pirani's paper. → Each scoped to its own setting, with no priority claim beyond it. Unchanged from the previous pass and still correct.

**Counterexamples tried**

- A neighbour whose straight path is a tilted great circle rather than a meridian: they set off level, so the along-path part stays zero and the summary's rule survives.
- Two friends walking the equator, one behind the other: a steady string on curved ground, which is exactly check one-behind-the-other against 'a steady string means flat'.
- A head start on the ball: the string goes from 3.162 m to 3.041 m rather than halving, as 'Three steps behind the line' says.
- The pole as a conjugate point: the side-by-side string vanishes there while a string with a head start keeps its four metres, which is problem string-at-the-pole.
- Paths three and five metres apart: the simplifies bound fails there, 0.0014 mm and 0.0024 mm, which is why the sentence now names one-metre paths.
- Unequal step lengths, that is members with different normalizations: g(u, xi) then grows linearly in the parameter; the entry rung fixes equal steps and the formal rung records the linear term.
- Desynchronized clocks in flat spacetime: the deviation vector is timelike although every separation is spatial; check desynchronized-clocks.
- Galaxies moving with the cosmic expansion: Lie dragged and still growing, against 'dragged means constant'.
- Null geodesics: u lies in its own orthogonal space, so the projector fails and the formal rung uses the two-dimensional quotient screen space.
- A connection with torsion: D_lambda xi and D_s u differ by T(u, xi); the formal simplifies says so and check torsion-and-symmetry derives it.
- Finite separation: the second-order terms depend on the family and not on curvature alone; stated in the formal limits of validity.
- A rotating congruence: focusing fails without the rotation-free hypothesis, which the research horizon states.

**Fixes**

- Formal way 'Variation fields and Jacobi fields' and check counting-deviation-fields: the tangential fields are now (a + b lambda) u, and the way says outright that such a field has g(u, xi) = -(a + b lambda), so alpha = -a and beta = -b. Before, the same two letters stood for quantities of opposite sign on a timelike geodesic, and a reader who joined the two sentences got the wrong sign. The formal picture uses the new letters too.
- Added the confirmed Classical and Quantum Gravity DOI 10.1088/0264-9381/18/22/302 to the relativistic-epicycles reference, which the previous pass left null.
- The six entry strings the novice stage changed at revision 6 were each re-derived or recomputed. None needed a change: no claim, number or sign moved, and the recomputed simplifies bound is 0.00047 mm against the stated thousandth of a millimetre.
- This pass replaced the previous top-level physics record, which covered revision 5, because the schema allows only one. Its verification, counterexamples and concerns survive in git history and in the snapshot deviation-vector.before-physics.json; its diff check is kept in diff_checks.
- Nothing dropped and no sentence compressed. The formal way explanation grows by 18 words against a 900-word cap; the note's total is unchanged to within those words.
- Revision bumped from 6 to 7.

**Concerns**

- This pass changed learner-visible text only at the formal rung, so the entry and working diff is empty: note_diff.py with --rungs entry,working lists no change, and a novice re-read has nothing in its own fields to read. The expected validator warning is that review.novice covers revision 6.
- course-conventions.md still fixes no symbol for the orthogonal part of the deviation vector, which this note writes xi_perp with h^mu_nu = delta^mu_nu + u^mu u_nu / c^2, and no torsion component convention, which the formal way and check torsion-and-symmetry take as T^mu_{alpha beta} = Gamma^mu_{alpha beta} - Gamma^mu_{beta alpha}. Both should be added there rather than left note-local.
- The registry's prerequisite list for this concept still lacks lie-bracket, riemann-curvature-tensor and killing-vector, so sync_registry.py needs to run.
- The working way assumes covariant-derivative-along-a-curve and the radar way assumes proper-time, neither of them a direct prerequisite of this note.
- None of geodesic, affine-parameter, congruence-of-curves, lie-dragging, lie-bracket, killing-vector, covariant-derivative-along-a-curve or proper-time exists as a note yet, so the entry recap carries the mirror-image reason for straight globe lines on its own.
- All three visuals are proposals and the visual catalog is empty vault-wide.
- The note still has no analogy at any rung, and tutoring sits at 2,771 words of 3,300, so there is room for one.
- Check torsion-and-symmetry targets no misconception, which the schema allows but leaves it outside the diagnosis graph.

**Diff check** (2026-09-13, revision 5)

- Entry, 'Three steps behind the line' simplifies: for friends this close on an Earth-sized ball, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.: python3: sphere of radius 6371 km, Asha on a meridian and Ben one metre of longitude-arc to her right, Ben's start at the equator or three metres behind it; component of the chord from Asha to Ben perpendicular to Asha's heading, compared at equal counts over the whole walk to the North Pole. Also repeated with 3 m and 5 m side separations as the 'a few metres apart' what-if. Checked that dropping 'then' and adding 'For friends this close' only scopes the old claim. → Largest change for the way's 1 m separation is 0.00085 mm (Asha at the pole), under the stated bound, and zero to first order in the separation. But 'this close' refers back to 'a few metres apart', and there the bound fails: 0.0016 mm at 3 m and 0.0025 mm at 5 m apart. Fixed by scoping the sentence to friends one metre apart.
- Working, 'Radar from a falling mass': the wave's wavelength was more than a thousand kilometres, so the first-order description holds across a 4 km arm.: python3: wavelength c/f over the GW150914 frequency sweep of about 35 to 250 Hz; compared with the 4 km LIGO arm length already stated in the same paragraph. → Wavelength runs from about 8,600 km down to about 1,200 km, so 'more than a thousand kilometres' holds throughout, and 4 km is less than half a percent of it. Same claim as the old sentence, now unambiguous. Accurate.
- Fix: Entry, 'Three steps behind the line' simplifies: 'For friends this close on an Earth-sized ball, ...' now reads 'For friends one metre apart on an Earth-sized ball, ...'. The bound of a thousandth of a millimetre holds for the way's one-metre friends but not for the 'few metres apart' that 'this close' pointed back to.

**Diff check** (2026-09-16, revision 7)

- Entry, 'Three steps behind the line' simplifies: for paths one metre apart on an Earth-sized ball, moving Ben's start three metres back changes the sideways part by less than a thousandth of a millimetre.: python3: radius 6371 km, meridian paths one metre apart at the equator, Ben three metres behind; change of the across-path arc 1 m (cos(lat - 3/R) - cos lat) at Asha's latitude, at 60 degrees and at the pole. → 0.00041 mm at 60 degrees and 0.00047 mm at the pole, both under the stated bound; the rescoping to 'paths one metre apart' matches the quantity the earlier check bounded. Accurate.
- Entry, 'A string between two walkers': walking straight from the equator facing the North Pole, each friend follows a line from the equator to the North Pole, like the lines printed on a globe but only one metre apart at the equator; Ben's ball start is one metre to Asha's right and three metres behind her on the side of the equator away from the North Pole.: Meridians are great circles, hence geodesics of the sphere; a walker facing the pole on the equator has the meridian as her straight path. Checked that 'right' is referenced to facing the North Pole and that 'behind' is fixed by naming the side of the equator. → Accurate; same claims as before, with the one-metre spacing and the side of the equator made explicit.
- Formal: the fields (a + b lambda) u come from x(lambda + a s, s) and x((1 + b s) lambda, s); on a unit-speed timelike geodesic g(u, xi) = -(a + b lambda), so alpha = -a and beta = -b; they solve the Jacobi equation because D_lambda^2 u = 0 and R(u, u) u = 0.: Hand algebra: d/ds of x(lambda + a s, s) at s = 0 gives a u, and of x((1 + b s) lambda, s) gives b lambda u, both affine reparametrizations so the members stay affinely parametrized geodesics; g(u, (a + b lambda) u) = (a + b lambda) g(u, u) = -(a + b lambda) with signature (-,+,+,+); D_lambda of a linear multiple of the parallel u is constant, so its second derivative vanishes, and R(u, u) = 0 by antisymmetry. → Accurate. The renaming to a, b removes the clash with the alpha, beta of g(u, xi) = alpha + beta lambda in the same way, and the summary 'starting to count further back' matches the a-term within the equal-steps scope stated earlier in the summary.
