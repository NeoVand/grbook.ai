---
type: "concept"
schema_version: 2
id: "curvature-of-the-two-sphere"
title: "Curvature of the 2-sphere"
tagline: "A round ball curves equally everywhere, and more gently the bigger it is"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 3
updated: "2026-09-16"
aliases: ["curvature of a sphere", "curvature of the round sphere"]
prerequisites: ["riemann-curvature-tensor", "holonomy", "gaussian-curvature", "two-sphere-metric", "ricci-scalar", "isometry"]
leads_to: ["space-of-constant-curvature", "three-sphere", "areal-radius"]
visuals: ["carry-an-arrow-around-a-loop", "paced-ring-on-a-ball-and-a-plain"]
---

# Curvature of the 2-sphere

*A round ball curves equally everywhere, and more gently the bigger it is*

`curvature-of-the-two-sphere` · curvature · core · physics-reviewed (revision 3)

**Needs:** [[riemann-curvature-tensor]] (working) · [[holonomy]] (entry) · [[gaussian-curvature]] (entry) · [[two-sphere-metric]] (working) · [[ricci-scalar]] (working) · [[isometry]] (formal)  
**Opens:** [[space-of-constant-curvature]] · [[three-sphere]] · [[areal-radius]]  
**Related:** [[curvature-sign-conventions]] · [[angular-excess]] · [[circumference-to-radius-test]] · [[cartan-method-for-curvature]]  
**Visuals:** ★ [[carry-an-arrow-around-a-loop]] · [[paced-ring-on-a-ball-and-a-plain]]

> A smooth, round ball curves equally strongly at every spot, because it looks the same after any roll. Its curving is 1 divided by the radius times itself, so a ball twice as wide curves a quarter as strongly. So someone who never leaves the ball can find its radius from a small loop's area and its arrow's turn.

## You will be able to

**Entry**
- Explain why a smooth, round ball curves equally strongly at every spot, whatever lines are painted on it. `objectives/explain-every-spot-alike` ← `checks/same-loop-anywhere`
- Predict how the turn around a loop of fixed area changes when the ball's radius changes. `objectives/predict-size-scaling` ← `checks/double-the-ball`
- Estimate a ball's radius from the turn of a loop and the area on the walker's left. `objectives/find-radius-from-a-turn` ← `problems/radius-of-a-small-moon`

**Working**
- Compute the Christoffel symbols, Riemann component, Gaussian curvature, Ricci tensor and Ricci scalar of a sphere from a metric. `objectives/compute-sphere-curvature` ← `problems/hat-box-coordinates`, `checks/soap-bubble-numbers`
- Distinguish coordinate artefacts, such as a varying component or an infinite Christoffel symbol, from the sphere's constant curvature. `objectives/separate-components-from-curvature` ← `checks/sin-squared-varies`, `checks/christoffels-at-the-pole`
- Use the sphere to diagnose the sign conventions of a curvature formula. `objectives/calibrate-signs-on-the-sphere` ← `checks/stranger-gets-a-minus-sign`

**Formal**
- Prove from rotational symmetry and Gauss–Bonnet that the sphere has constant curvature 1 over a squared. `objectives/prove-constancy-from-symmetry` ← `checks/symmetry-fixes-the-curvature`
- State which surfaces have constant positive curvature, and which hypotheses make the round sphere the only one. `objectives/state-rigidity-hypotheses` ← `checks/closed-surfaces-with-constant-curvature`, `problems/spindle-with-two-tips`

## Ways in

### 1. Every spot of a round ball is alike · entry · picture

*Does a round ball curve more strongly at some spots than at others?*

**Recap:** The arrow test: press a cardboard arrow against the ground and walk a loop, a path that ends where it began. Never let the arrow swing left or right. Back at the start, compare its direction with its starting direction. On a ball, most loops bring it back turned.

Picture a huge globe, a smooth, round ball with lines painted on it. The lines that run from pole to pole crowd together near the North Pole. Does the ball curve more strongly there?

Use the arrow test to find out. Push a peg into the ground near the North Pole and tie a string to it. Carry a cardboard arrow that never swings. Walk once around the peg, keeping the string tight and the peg on your left. Say the arrow comes back turned 3 degrees toward your left.

Now move the peg to a spot near the equator. Walk around it the same way, with the same string. The arrow comes back turned 3 degrees toward your left again.

Here is why. Stand still and imagine rolling the whole globe until the second peg sits right in front of you, exactly where the first peg sat when you began. A smooth, round ball looks and feels exactly the same after any roll. Only the painted lines have moved, and the arrow test never uses them. So the second walk is the first walk over again, with the same result. The same holds for any two spots.

So a round ball curves equally strongly at every spot. The crowded lines near the North Pole are only labels.

An egg is different. Its pointed end curves more strongly than its middle, so rolling an egg changes what lies under the peg. The same walk around a peg then gives different turns at different spots.

Earth is close to a round ball, but it is slightly flattened. Its curving is about 1.3 percent weaker at the poles than at the equator. Walking around a peg on a string 1 kilometre long turns the arrow by only about 4 millionths of a degree anywhere on Earth. So nobody notices the turn, let alone the difference.

**Try it:** Hold a smooth ball with no seams, such as a plastic ball. Close your eyes while a friend rolls it in your hands, then feel it all over. You cannot tell how it was rolled. Try again with a hard-boiled egg: you feel at once where its pointed end has gone, so you can tell it was rolled.

**Takeaway:** A round ball looks the same after any roll, so a walk around a peg gives the same turn at every spot: the ball curves equally strongly everywhere.

*Builds on:* [[holonomy]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]]<br>*See:* `checks/same-loop-anywhere`

### 2. A ball twice as wide curves a quarter as strongly · entry · calculation

*How does the strength of a ball's curving depend on its size?*

**Recap:** The arrow test: walk a loop, a path that ends where it began. Carry a cardboard arrow that never swings left or right. On a smooth, round ball, keep a small piece of the ball on your left as you walk. Then the arrow comes back turned toward your left. Measure the turn in full turns, so a quarter turn counts as one quarter. The turn is twice the fraction of the ball's whole surface area that lies in the piece on your left.

A round ball curves equally strongly at every spot. But how strongly? Take two smooth, round balls. One has a radius of 10 centimetres. The other is twice as wide, with a radius of 20 centimetres. Imagine you are small enough to walk on them.

On each ball, walk a small loop that keeps 14 square centimetres on your left, about the size of a large postage stamp. Carry a cardboard arrow that never swings. On the smaller ball, the arrow comes back turned 8 degrees toward your left. What happens on the bigger ball?

The turn depends on the fraction of the ball's surface area on your left, so compare the two whole surface areas. A ball's surface area is about 12.57 times its radius times itself. That 12.57 is 4 times pi. Doubling the radius makes the radius times itself four times as big. So the bigger ball has four times as much surface area.

The same 14 square centimetres is therefore a quarter of the fraction it was on the smaller ball. The turn is twice that fraction, so the turn is a quarter as big too: 2 degrees.

Divide a small loop's turn by the area it keeps on your left, and you get a measure of how strongly the ball curves. On the bigger ball this measure is a quarter as big. Double the radius again, and it drops to a quarter again. Now try 1 divided by the radius times itself. Double the radius, and that drops to a quarter too, every time. So the strength of a ball's curving matches 1 divided by the radius times itself.

That number, 1 divided by the radius times itself, is called the ball's Gaussian curvature. Halve the radius instead, and the curving is four times as strong.

Earth's radius is about 6,371 kilometres, so its Gaussian curvature is tiny. A loop that keeps 1 square kilometre on your left turns the arrow by only about 1.4 millionths of a degree. That is why nobody notices Earth's curving on a walk.

**Takeaway:** On a ball twice as wide, the same small loop turns the arrow a quarter as much, so a ball's Gaussian curvature is 1 divided by the radius times itself.

*Continues:* `ways_in/every-spot-alike`<br>*Builds on:* [[holonomy]], [[gaussian-curvature]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]]<br>*See:* `checks/double-the-ball`

### 3. Find the radius without leaving the ball · entry · operational

*How can someone who never leaves a ball find out how big it is?*

**Recap:** The arrow test: walk a loop, a path that ends where it began. Carry a cardboard arrow that never swings left or right. On a smooth, round ball, keep a small piece of the ball on your left as you walk. Then the arrow comes back turned toward your left. Measure the turn in full turns, so a quarter turn counts as one quarter. The turn is twice the fraction of the ball's whole surface area that lies in the piece on your left.

The two balls showed that a loop's turn depends on the ball's size. So a turn can reveal the size. Imagine an explorer on a small, smooth, round planet. She cannot fly, and she has never seen the planet from outside. Can she find its radius?

She walks a loop, carrying a cardboard arrow that never swings. It comes back turned 1 degree toward her left. She also measures the piece of ground her loop fences off, the piece that stayed on her left as she walked. She marks it out in squares 1 kilometre on each side and counts them. It covers 1,000 square kilometres.

Step one: find the fraction. A full turn is 360 degrees, so her turn is one 360th of a full turn. The turn, in full turns, is twice the fraction of the planet on her left. So that fraction is one 720th.

Step two: find the whole surface area. Her 1,000 square kilometres is one 720th of it. So the whole surface area is 720 times 1,000, which is 720,000 square kilometres.

Step three: find the radius. A ball's surface area is about 12.57 times its radius times itself. Dividing 720,000 by 12.57 gives about 57,300. So the radius times itself is about 57,300 square kilometres. The radius is the number that gives 57,300 when multiplied by itself, which is about 239 kilometres.

The same steps work on Earth. Take a loop that keeps 51,000 square kilometres on your left, about the size of Costa Rica. It turns the arrow by 72 thousandths of a degree, about the angle across a thin pencil lead held at arm's length. Running the three steps on that turn gives Earth's radius, about 6,370 kilometres. A turn that small needs very careful instruments, which is why nobody notices it.

**Takeaway:** Measure a loop's turn and the area on your left: the turn gives the fraction of the ball, the fraction gives the whole surface area, and the surface area gives the radius.

*Continues:* `ways_in/double-the-ball`<br>*Builds on:* [[holonomy]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]]<br>*See:* `problems/radius-of-a-small-moon`

### 4. One number from the distance rule · working · calculation

*How do the Christoffel symbols, Riemann tensor, Ricci tensor and Ricci scalar of a sphere follow from its metric?*

In "A ball twice as wide curves a quarter as strongly", doubling a ball's radius cut its curving to a quarter. The metric turns that scaling into exact components. On a sphere of radius $a$, with colatitude $\theta$, the angle from the North Pole measured at the centre, and longitude $\phi$,

$$ds^2 = a^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right).$$

Only $g_{\phi\phi} = a^2\sin^2\theta$ varies, and only with $\theta$. So the Christoffel formula leaves two nonzero symbols, $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$. Neither contains $a$, because each term has one metric factor and one inverse-metric factor.

The derivation "The sphere's curvature from its metric" feeds these into the course Riemann formula. The derivative term gives $\sin^2\theta - \cos^2\theta$, one product term adds $\cos^2\theta$, and

$$R^\theta{}_{\phi\theta\phi} = \sin^2\theta.$$

In two dimensions each antisymmetric index pair has a single independent value, $\theta\phi$, so this is the only independent component. Lowering gives $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$, and every other component is plus or minus this, or zero.

The factor $\sin^2\theta$ does not mean the curving varies. The basis vector $\partial_\phi$ has length $a\sin\theta$, so divide by the squared area of the basis cell. The Gaussian curvature is

$$K = \frac{R_{\theta\phi\theta\phi}}{g_{\theta\theta}\,g_{\phi\phi}} = \frac{1}{a^2},$$

the same at every point and equal to the orthonormal component $R_{\hat\theta\hat\phi\hat\theta\hat\phi}$. Its units, inverse length squared, are the quarter-for-double scaling.

Every contraction follows. The whole tensor is $R_{\mu\nu\rho\sigma} = (g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})/a^2$, so $R_{\mu\nu} = g_{\mu\nu}/a^2$, which in components is $R_{\theta\theta} = 1$ and $R_{\phi\phi} = \sin^2\theta$. Tracing with the inverse metric gives $R = 2/a^2$, twice $K$, as on every surface. For Earth, $a = 6371$ km gives $K = 2.46\times10^{-14}$ m$^{-2}$.

Two features make this the standard calibration. The same formula applied to the flat plane in polar coordinates, $dr^2 + r^2d\phi^2$, must give zero, although its Christoffel symbols are not zero. And the sign is known in advance: a small loop keeping a region on the walker's left returns vectors rotated toward the left, by $K$ times the area. So the course conventions must give $R^\theta{}_{\phi\theta\phi} > 0$, $K > 0$ and $R = +2/a^2$.

**Takeaway:** On a sphere of radius a, the single independent Riemann component gives a Gaussian curvature of 1 over a squared everywhere, a Ricci tensor equal to the metric over a squared, and a Ricci scalar of 2 over a squared.

*What this leaves out:* Uses the chart $(\theta, \phi)$, which fails at the poles; the invariant results hold there too.

*Continues:* `ways_in/double-the-ball`<br>*Builds on:* [[two-sphere-metric]], [[christoffel-symbols]], [[riemann-curvature-tensor]], [[ricci-scalar]]<br>*See:* `derivations/sphere-curvature-from-metric`, `checks/sin-squared-varies`, `checks/stranger-gets-a-minus-sign`

### 5. Three insider measurements, one number · working · operational

*Which measurements made on a sphere read off its curvature, and why do they all agree?*

The explorer in "Find the radius without leaving the ball" read her planet's radius from one turn and one area. With $K = 1/a^2$ from "One number from the distance rule", three instruments used on the surface give the same radius.

- *A carried arrow.* A simple loop bounding a region of area $A$ on the walker's left returns a vector rotated toward the left by $\Delta\alpha = KA = A/a^2$, modulo $2\pi$. This is the local Gauss–Bonnet theorem with constant $K$, taken on trust here. The explorer used it in full turns, $A/2\pi a^2$.
- *A theodolite*, the surveyor's telescope for measuring angles. A triangle of great-circle arcs has angles summing to more than $\pi$ by the same amount, $\alpha_1 + \alpha_2 + \alpha_3 - \pi = A/a^2$.
- *A tape measure.* Put the centre of a ring at the North Pole. The points at distance $\rho$ from it, measured along the surface, lie at colatitude $\theta = \rho/a$, so the metric gives the ring length $C = 2\pi a\sin(\rho/a)$. For a small ring the fraction missing from $2\pi\rho$ is $\rho^2/6a^2 = K\rho^2/6$.

The worked example "Earth, read three ways" puts in numbers. A geodesic triangle of 10,000 km² on Earth has an excess of 50.8 arcseconds, where one arcsecond is $1/3600$ of a degree, and a ring of radius 100 km is 25.8 m short.

Why must they agree? Each reading is $K$ times a geometric size: an area for the first two, $\rho^2/6$ for the third. On a general surface a small ring reads $K$ at its centre, while a loop adds $K$ up over its region, so readings taken on different patches disagree. On the sphere $K$ is the same everywhere, so they agree for every size and position. The tape measure even works for large rings: solving $C = 2\pi a\sin(\rho/a)$ for $a$ uses one ring, and the ring shrinks back to a point at $\rho = \pi a$, the far pole.

Real Earth is close to this model. It is flattened by about one part in 298, and its $K$ is 1.35% larger at the equator than at the poles, so precise surveys use an ellipsoid. The observation "Earth's size and curvature from geodesy" gives the numbers.

**Takeaway:** Arrow rotation, angle excess and ring shortfall on a sphere are each K times a geometric size, and because K is the same everywhere they all return the same radius.

*What this leaves out:* Treats Earth as a perfect sphere with smooth ground.

*Continues:* `ways_in/find-the-radius-without-leaving`, `ways_in/curvature-from-the-metric`<br>*Builds on:* [[holonomy]], [[angular-excess]], [[two-sphere-metric]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `worked_examples/earth-read-three-ways`, `observations/earth-from-geodesy`

### 6. The round sphere as a space form · formal · structure

*What fixes the sphere's curvature without coordinates, and which theorems single the sphere out?*

The components of "One number from the distance rule" came from one chart. Here the same number is found without coordinates and placed among the theorems that use it. Only lengths enter, so setting $G = c = 1$ changes nothing. Let $S^2_a = \{x \in \mathbb{R}^3 : |x| = a\}$ carry the metric $g$ induced from the Euclidean one. The chart $(\theta, \phi)$ covers $S^2_a$ minus a closed half great circle joining the poles; the vanishing of $g_{\phi\phi}$ at $\theta = 0, \pi$ is a failure of the chart, not of the metric.

*Cartan's computation.* On the chart take the orthonormal coframe $e^1 = a\,d\theta$, $e^2 = a\sin\theta\,d\phi$, oriented by the outward normal. The derivation "The sphere by Cartan's method" solves the torsion-free structure equation for $\omega^1{}_2 = -\cos\theta\,d\phi$ and finds

$$\Omega^1{}_2 = d\omega^1{}_2 = \frac{1}{a^2}\,e^1\wedge e^2,$$

so $R^1{}_{212} = 1/a^2$. Under a change of oriented orthonormal frame $\Omega^1{}_2$ is invariant, because $SO(2)$ is abelian. So $\Omega^1{}_2 = K\,dA$ is a smooth global two-form, even where the chart fails.

*Symmetry does it without computation.* $SO(3)$ acts on $S^2_a$ by isometries, transitively on points and, through the stabilizer $SO(2)$, on unit tangent vectors. Isometries preserve $K$, so $K$ is constant. On any surface $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$. Hence $R_{\mu\nu} = Kg_{\mu\nu}$, $R = 2K$, the Einstein tensor vanishes identically, and the Kretschmann scalar is $4K^2$. The three Killing fields spanning $\mathfrak{so}(3)$ reach the maximum $n(n+1)/2$ for $n = 2$, so the sphere is maximally symmetric. The value follows from the Gauss–Bonnet theorem, $\int K\,dA = 2\pi\chi(S^2) = 4\pi$, over the area $4\pi a^2$.

*Rigidity.* These standard results, stated without proof, each need their hypotheses.

- Minding: surfaces with the same constant $K$ are locally isometric, so every small patch with $K = 1/a^2$ is isometric to a piece of $S^2_a$.
- Killing–Hopf: a complete connected surface with $K \equiv 1/a^2$ is isometric to $S^2_a$ or to the real projective plane $S^2_a/\{\pm1\}$.
- Liebmann: a compact connected smooth surface in $\mathbb{R}^3$ with constant $K$ is a round sphere.
- Bonnet–Myers: a complete surface with $K \ge 1/a^2$ has diameter at most $\pi a$, and by Cheng's theorem equality forces an isometry with $S^2_a$.

*Limits.* Drop smoothness and constant $K$ survives with cone points: the spindle $d\rho^2 + b^2\sin^2(\rho/a)\,d\phi^2$ with $0 < b < a$ has $K = 1/a^2$ away from two tips, which carry the rest of the $4\pi$. Drop compactness and $K$ no longer fixes the shape in $\mathbb{R}^3$: surfaces of revolution with profile radius $b\cos(s/a)$, $b \neq a$, have $K = 1/a^2$ and are locally isometric to $S^2_a$, yet they are not pieces of round spheres. In spacetime, the orbits of a spherically symmetric metric are round spheres $r^2\,d\Omega^2$ with $K = 1/r^2$, whatever the curvature of the spacetime around them; that is what defines the areal radius $r$.

**Takeaway:** Rotational symmetry makes the sphere's curvature constant and Gauss–Bonnet fixes it at 1 over a squared; with smoothness and completeness, that curvature allows only the round sphere and its projective quotient.

*Continues:* `ways_in/curvature-from-the-metric`<br>*Builds on:* [[isometry]], [[levi-civita-connection]]<br>*See:* `derivations/sphere-by-cartan`, `checks/symmetry-fixes-the-curvature`, `checks/closed-surfaces-with-constant-curvature`, `problems/spindle-with-two-tips`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| arrow test | — | Carry a cardboard arrow around a loop, never letting it swing, and compare its direction at the end with its direction at the start. The difference is the loop's turn. | [[holonomy]] |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way the arrow points, left or right, while it lies against the ground. In the arrow test the arrow never swings. | — |
| Gaussian curvature | GOW-see-un | A number that says how strongly a surface curves at a spot. For a round ball it is the same at every spot: multiply the radius by itself and divide 1 by the result. | [[gaussian-curvature]] |

## Key equations

### Line element of a sphere · working

$$
ds^2 = a^2\left(d\theta^2 + \sin^2\theta\,d\phi^2\right)
$$

Distances on a sphere of radius $a$, in colatitude and longitude.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $a$ | radius of the sphere | a, the radius |
| $\theta$ | colatitude, the angle from the North Pole measured at the centre | theta, the colatitude |
| $\phi$ | longitude | phi, the longitude |

**Holds when:** $0 < \theta < \pi$; the chart fails at the poles, the geometry does not.  
**Say it:** “d s squared equals a squared times, d theta squared plus sine squared theta d phi squared.”  
**Justified by:** `two-sphere-metric`

### The one independent component and the Gaussian curvature · working

$$
R^\theta{}_{\phi\theta\phi} = \sin^2\theta,\qquad K = \frac{R_{\theta\phi\theta\phi}}{g_{\theta\theta}\,g_{\phi\phi}} = \frac{1}{a^2}
$$

The coordinate component varies with $\theta$, but the Gaussian curvature it gives is the same at every point.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R^\theta{}_{\phi\theta\phi}$ | Riemann component in the course convention and the coordinate basis | R theta phi theta phi |
| $K$ | Gaussian curvature | K |

**Holds when:** Course Riemann convention; coordinate basis of the line element.  
**Say it:** “R theta phi theta phi equals sine squared theta, and the Gaussian curvature is one over a squared.”  
**Justified by:** `derivations/sphere-curvature-from-metric`

### Riemann, Ricci and scalar curvature of a sphere · working

$$
R_{\mu\nu\rho\sigma} = \frac{1}{a^2}\left(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}\right),\qquad R_{\mu\nu} = \frac{g_{\mu\nu}}{a^2},\qquad R = \frac{2}{a^2}
$$

Every curvature tensor of the sphere is the metric times one number.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu\rho\sigma}$ | lowered Riemann tensor | the Riemann tensor |
| $R_{\mu\nu}$ | Ricci tensor, $R^\rho{}_{\mu\rho\nu}$ | the Ricci tensor |
| $R$ | Ricci scalar | the Ricci scalar |

**Holds when:** Course conventions; holds in every basis.  
**Say it:** “The Riemann tensor is one over a squared times g g minus g g, the Ricci tensor is the metric over a squared, and the Ricci scalar is two over a squared.”  
**Justified by:** `derivations/sphere-curvature-from-metric`

### Turn around a loop on a sphere · working

$$
\Delta\alpha = K A = \frac{A}{a^2} \pmod{2\pi}
$$

A loop bounding area $A$ on the walker's left returns vectors rotated by $A/a^2$; for a geodesic triangle this equals the angle excess.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta\alpha$ | rotation of the returned vector, positive toward the walker's left | the turn |
| $A$ | area of the region on the walker's left | the area |

**Holds when:** Simple loop on a sphere of radius $a$; modulo $2\pi$.  
**Say it:** “The turn is the area on the walker's left divided by a squared.”  
**Justified by:** `holonomy`

### Length of a ring on a sphere · working

$$
C(\rho) = 2\pi a\sin\frac{\rho}{a} = 2\pi\rho\left(1 - \frac{K\rho^2}{6} + \dots\right)
$$

A ring whose points lie at distance $\rho$ from a centre, measured along the sphere, is shorter than $2\pi\rho$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\rho$ | distance from the centre, measured along the surface | rho |
| $C$ | length of the ring | C |

**Holds when:** $0 \le \rho \le \pi a$; the series is for $\rho \ll a$.  
**Say it:** “C of rho equals two pi a sine of rho over a, which is two pi rho times one minus K rho squared over six, plus smaller terms.”  
**Justified by:** `two-sphere-metric`

### Curvature two-form of a sphere · formal

$$
\Omega^1{}_2 = d\omega^1{}_2 = \frac{1}{a^2}\,e^1\wedge e^2,\qquad e^1 = a\,d\theta,\quad e^2 = a\sin\theta\,d\phi
$$

In an oriented orthonormal coframe the whole curvature of the sphere is one two-form, $K$ times the area form.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Omega^1{}_2$ | curvature two-form, $\tfrac12 R^1{}_{2cd}\,e^c\wedge e^d$ | omega one two, the curvature form |
| $\omega^1{}_2$ | connection one-form of the Levi-Civita connection | little omega one two |
| $e^1, e^2$ | orthonormal coframe | e one and e two |

**Holds when:** Levi-Civita connection; the same two-form in every oriented orthonormal frame.  
**Say it:** “Capital omega one two equals d of little omega one two, which is one over a squared times e one wedge e two.”  
**Justified by:** `derivations/sphere-by-cartan`

## Derivations

### The sphere's curvature from its metric · working

**Goal:** Starting from $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, find $R^\theta{}_{\phi\theta\phi}$, $K$, $R_{\mu\nu}$ and $R$ with the course conventions.

1. Read off $g_{\theta\theta} = a^2$, $g_{\phi\phi} = a^2\sin^2\theta$ and $g_{\theta\phi} = 0$, so $g^{\theta\theta} = 1/a^2$ and $g^{\phi\phi} = 1/(a^2\sin^2\theta)$.
2. The only nonzero metric derivative is $\partial_\theta g_{\phi\phi} = 2a^2\sin\theta\cos\theta$.
3. $\Gamma^\theta{}_{\phi\phi} = -\tfrac12 g^{\theta\theta}\partial_\theta g_{\phi\phi} = -\sin\theta\cos\theta$.
4. $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \tfrac12 g^{\phi\phi}\partial_\theta g_{\phi\phi} = \cot\theta$. Every other symbol contains a vanishing derivative, so it is zero.
5. Write the course formula: $R^\theta{}_{\phi\theta\phi} = \partial_\theta\Gamma^\theta{}_{\phi\phi} - \partial_\phi\Gamma^\theta{}_{\theta\phi} + \Gamma^\theta{}_{\theta\lambda}\Gamma^\lambda{}_{\phi\phi} - \Gamma^\theta{}_{\phi\lambda}\Gamma^\lambda{}_{\theta\phi}$.
6. First term: $\partial_\theta(-\sin\theta\cos\theta) = \sin^2\theta - \cos^2\theta$. Second term: $\Gamma^\theta{}_{\theta\phi} = 0$, so it vanishes.
7. Third term: $\Gamma^\theta{}_{\theta\theta} = \Gamma^\theta{}_{\theta\phi} = 0$, so it vanishes. Fourth term: only $\lambda = \phi$ survives, giving $-\Gamma^\theta{}_{\phi\phi}\Gamma^\phi{}_{\theta\phi} = \sin\theta\cos\theta\cot\theta = \cos^2\theta$.
8. Add: $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. Lower with $g_{\theta\theta}$: $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$.
9. In two dimensions the pair antisymmetries leave one independent component: $R_{\phi\theta\phi\theta} = R_{\theta\phi\theta\phi}$ and $R_{\theta\phi\phi\theta} = R_{\phi\theta\theta\phi} = -R_{\theta\phi\theta\phi}$.
10. Divide by $g_{\theta\theta}g_{\phi\phi} = a^4\sin^2\theta$: $K = 1/a^2$. The tensor $g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}$ has the same symmetries and equals $a^4\sin^2\theta$ for $\theta\phi\theta\phi$, so $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$.
11. Contract: $R_{\mu\nu} = g^{\rho\sigma}R_{\rho\mu\sigma\nu} = K(2g_{\mu\nu} - g_{\mu\nu}) = g_{\mu\nu}/a^2$, so $R_{\theta\theta} = 1$, $R_{\phi\phi} = \sin^2\theta$ and $R_{\theta\phi} = 0$.
12. Trace: $R = g^{\mu\nu}R_{\mu\nu} = 2K = 2/a^2$.

**Result:** $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, $K = 1/a^2$, $R_{\mu\nu} = g_{\mu\nu}/a^2$ and $R = 2/a^2$, all positive in the course conventions.

### The sphere by Cartan's method · formal

**Goal:** Find the curvature two-form of $S^2_a$ in the coframe $e^1 = a\,d\theta$, $e^2 = a\sin\theta\,d\phi$, with $\nabla e_b = \omega^a{}_b\otimes e_a$ and $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c\wedge\omega^c{}_b = \tfrac12R^a{}_{bcd}\,e^c\wedge e^d$.

1. Exterior derivatives: $de^1 = 0$ and $de^2 = a\cos\theta\,d\theta\wedge d\phi$.
2. Metric compatibility in an orthonormal frame makes $\omega_{ab} = -\omega_{ba}$, and torsion-freeness gives $de^a = -\omega^a{}_b\wedge e^b$.
3. Try $\omega^2{}_1 = \cos\theta\,d\phi$: then $-\omega^2{}_1\wedge e^1 = a\cos\theta\,d\theta\wedge d\phi = de^2$ and $-\omega^1{}_2\wedge e^2 = a\sin\theta\cos\theta\,d\phi\wedge d\phi = 0 = de^1$. The solution is unique, so $\omega^1{}_2 = -\cos\theta\,d\phi$.
4. The quadratic term $\omega^1{}_c\wedge\omega^c{}_2$ contains $\omega^1{}_1$ or $\omega^2{}_2$, both zero, so $\Omega^1{}_2 = d\omega^1{}_2 = \sin\theta\,d\theta\wedge d\phi$.
5. Since $e^1\wedge e^2 = a^2\sin\theta\,d\theta\wedge d\phi$, $\Omega^1{}_2 = a^{-2}\,e^1\wedge e^2$, which is $R^1{}_{212}\,e^1\wedge e^2$.

**Result:** $R^1{}_{212} = K = 1/a^2$, the orthonormal component found from the Christoffel symbols.

## Worked examples

### Earth, read three ways · working

**Problem:** Treat Earth as a sphere of radius 6371 km. Find $K$ and $R$ in SI units. Then predict (a) the angle excess of a geodesic triangle of area 10,000 km², (b) the shortfall of a ring of radius 100 km measured along the ground, and (c) the radius a surveyor would infer from an excess of 50.8 arcseconds on that triangle.

1. $K = 1/a^2 = 1/(6.371\times10^{6}\ \text{m})^2 = 2.464\times10^{-14}$ m$^{-2}$, and $R = 2K = 4.93\times10^{-14}$ m$^{-2}$.
2. (a) The excess is $KA = 2.464\times10^{-14}\ \text{m}^{-2}\times10^{10}\ \text{m}^2 = 2.464\times10^{-4}$ rad. One radian is 206,265 arcseconds, so the excess is 50.8 arcseconds.
3. (b) $\rho/a = 0.015696$, and $2\pi\rho - 2\pi a\sin(\rho/a) = 25.8$ m, which matches $\pi\rho^3/3a^2 = 25.8$ m: a fraction $4.1\times10^{-5} = K\rho^2/6$.
4. (c) $a = \sqrt{A/\Delta\alpha} = \sqrt{10^{10}\ \text{m}^2/2.463\times10^{-4}} = 6.37\times10^{6}$ m.

**Answer:** $K = 2.46\times10^{-14}$ m$^{-2}$ and $R = 4.93\times10^{-14}$ m$^{-2}$; (a) 50.8 arcseconds; (b) 25.8 m; (c) about 6370 km.

**Takeaway:** One number, $1/a^2$, predicts every insider measurement on a sphere, and any one of them gives back $a$.

## Problems

### `radius-of-a-small-moon` · entry · difficulty 2 · estimate

An explorer on a smooth, round moon walks a loop that keeps 2,000 square kilometres on her left. Her cardboard arrow never swings, and it comes back turned 3 degrees toward her left. A ball's surface area is about 12.57 times its radius times itself. How big is the moon's radius?

**Hints**

1. What fraction of a full turn is 3 degrees? The fraction of the moon on her left is half of that.
2. Her 2,000 square kilometres is that fraction of the whole surface.

**Answer:** About 195 kilometres.

**Must contain:** The fraction of the moon on her left is one 240th; The whole surface area is 480,000 square kilometres; The radius is about 195 kilometres

**Numeric:** radius of the moon = 195.4 km (magnitude, ±2%)

**Solution**

1. A full turn is 360 degrees, so 3 degrees is one 120th of a full turn.
2. The turn in full turns is twice the fraction of the moon on her left. So that fraction is one 240th.
3. The whole surface area is 240 times 2,000 square kilometres, which is 480,000 square kilometres.
4. Dividing 480,000 by 12.57 gives about 38,200. So the radius times itself is about 38,200 square kilometres.
5. The number that gives 38,200 when multiplied by itself is about 195. So the radius is about 195 kilometres.

### `hat-box-coordinates` · working · difficulty 2 · calculation

Label points of a sphere of radius $a$ by their height $z = a\cos\theta$ above the equatorial plane and their longitude $\phi$, so that $ds^2 = \dfrac{a^2\,dz^2}{a^2 - z^2} + (a^2 - z^2)\,d\phi^2$ for $|z| < a$. Find the nonzero Christoffel symbols and $R^z{}_{\phi z\phi}$, then $K$ and $R$. Show that bands of equal height have equal area, as Archimedes found.

**Hints**

1. Only $g_{zz}$ and $g_{\phi\phi}$ are nonzero, and both depend only on $z$.
2. In the Riemann component, check which of the two product terms survive.

**Answer:** $\Gamma^z{}_{zz} = z/(a^2 - z^2)$, $\Gamma^z{}_{\phi\phi} = z(a^2 - z^2)/a^2$, $\Gamma^\phi{}_{z\phi} = -z/(a^2 - z^2)$; $R^z{}_{\phi z\phi} = (a^2 - z^2)/a^2$, so $K = 1/a^2$ and $R = 2/a^2$. The area element is $a\,dz\,d\phi$.

**Must contain:** The component varies with z but K is one over a squared; Both product terms contribute z squared over a squared; The area element a dz dphi does not depend on z

**Solution**

1. $\Gamma^z{}_{zz} = \tfrac12 g^{zz}\partial_z g_{zz} = \tfrac12\,\dfrac{a^2 - z^2}{a^2}\cdot\dfrac{2a^2z}{(a^2 - z^2)^2} = \dfrac{z}{a^2 - z^2}$.
2. $\Gamma^z{}_{\phi\phi} = -\tfrac12 g^{zz}\partial_z g_{\phi\phi} = z(a^2 - z^2)/a^2$ and $\Gamma^\phi{}_{z\phi} = \tfrac12 g^{\phi\phi}\partial_z g_{\phi\phi} = -z/(a^2 - z^2)$.
3. $R^z{}_{\phi z\phi} = \partial_z\Gamma^z{}_{\phi\phi} + \Gamma^z{}_{zz}\Gamma^z{}_{\phi\phi} - \Gamma^z{}_{\phi\phi}\Gamma^\phi{}_{z\phi} = \dfrac{a^2 - 3z^2}{a^2} + \dfrac{z^2}{a^2} + \dfrac{z^2}{a^2} = \dfrac{a^2 - z^2}{a^2}$.
4. $K = g_{zz}R^z{}_{\phi z\phi}/(g_{zz}g_{\phi\phi}) = R^z{}_{\phi z\phi}/g_{\phi\phi} = 1/a^2$, and $R = 2K = 2/a^2$, as in $(\theta, \phi)$.
5. $\sqrt{g_{zz}g_{\phi\phi}} = a$, so the band between heights $z_1$ and $z_2$ has area $2\pi a(z_2 - z_1)$, the area of the matching band of the cylinder of radius $a$.

**Targets:** `varying-component-means-varying-curvature`

### `spindle-with-two-tips` · formal · difficulty 3 · proof

For $0 < b < a$, the metric $ds^2 = d\rho^2 + b^2\sin^2(\rho/a)\,d\phi^2$, with $0 < \rho < \pi a$ and $\phi$ of period $2\pi$, describes a spindle. (a) Show that $K = 1/a^2$ away from the tips. (b) Show that each tip is a cone point and find its deficit angle. (c) Verify the Gauss–Bonnet balance $\int K\,dA + \sum\delta = 4\pi$, and explain why the spindle does not contradict the rigidity of the round sphere.

**Hints**

1. With $e^1 = d\rho$ and $e^2 = f\,d\phi$, show that $\Omega^1{}_2 = -(f''/f)\,e^1\wedge e^2$.
2. Compare the circumference of a small circle $\rho = \epsilon$ with $2\pi\epsilon$.

**Answer:** $K = -f''/f = 1/a^2$; each tip has total angle $2\pi b/a$ and deficit $2\pi(1 - b/a)$; $\int K\,dA = 4\pi b/a$ and the two deficits add $4\pi - 4\pi b/a$. The rigidity theorems assume a smooth complete metric, which the tips violate.

**Must contain:** Gaussian curvature one over a squared away from the tips; Deficit two pi times one minus b over a at each tip; The tips supply the curvature missing from four pi; Rigidity needs smoothness at every point

**Solution**

1. With $f = b\sin(\rho/a)$, $e^1 = d\rho$ and $e^2 = f\,d\phi$, the structure equation gives $\omega^1{}_2 = -f'\,d\phi$, so $\Omega^1{}_2 = -f''\,d\rho\wedge d\phi = -(f''/f)\,e^1\wedge e^2$ and $K = -f''/f = 1/a^2$.
2. A circle $\rho = \epsilon$ has length $2\pi b\sin(\epsilon/a) = 2\pi(b/a)\epsilon + O(\epsilon^3)$, as on a flat cone of total angle $2\pi b/a$, so the tip is a cone point with deficit $\delta = 2\pi(1 - b/a)$. The tip $\rho = \pi a$ is the same by the symmetry $\rho \to \pi a - \rho$.
3. $\int K\,dA = a^{-2}\int_0^{2\pi}\!\int_0^{\pi a} b\sin(\rho/a)\,d\rho\,d\phi = a^{-2}\cdot 2\pi\cdot 2ab = 4\pi b/a$.
4. Adding $2\delta = 4\pi - 4\pi b/a$ gives $4\pi = 2\pi\chi(S^2)$. For $b = a/2$: $2\pi$ from the smooth part and $\pi$ from each tip.
5. Killing–Hopf and Liebmann assume a smooth metric at every point. At the tips the metric is not smooth, so the spindle is a sphere topologically with constant $K$ only on an incomplete smooth part, and no theorem is contradicted. For $b = a$ the deficits vanish and the round sphere returns.

**Targets:** `constant-k-means-round-sphere`

## Observations

- **Earth's size and curvature from geodesy, as summarized by the GRS80 reference ellipsoid** (measured, working). Treated as a sphere of the ellipsoid's mean radius, Earth's surface has $K = 1/a^2$ and $R = 2/a^2$. The ellipsoid's flattening makes $K$ vary with latitude, which is why the sphere is a first model rather than a survey standard. *Numbers:* Equatorial radius 6378.137 km and flattening $1/298.257$ give a mean radius of 6371.0 km, so $K = 2.464\times10^{-14}$ m$^{-2}$ and $R = 4.927\times10^{-14}$ m$^{-2}$. On the ellipsoid $K$ runs from $2.442\times10^{-14}$ m$^{-2}$ at the poles to $2.475\times10^{-14}$ m$^{-2}$ at the equator. *Reference:* Helmut Moritz (1980), *Geodetic Reference System 1980*, Bulletin Géodésique 54, 395–405, doi:10.1007/BF02521480
- **The daily turning of a Foucault pendulum's swing plane** (measured, working). For slow rotation and small swings, Earth's rotation carries the swing plane around its circle of latitude $\lambda$ without swinging, so it returns rotated by $K$ times the area of the polar cap on the walker's left. With $K = 1/a^2$ and cap area $2\pi a^2(1 - \sin\lambda)$, the radius cancels: a counterclockwise rotation by $2\pi(1 - \sin\lambda)$, seen from above the North Pole, which is the observed clockwise turn by $2\pi\sin\lambda$ per sidereal day in the northern hemisphere. *Numbers:* Paris, latitude $48.85^\circ$: $360^\circ\sin\lambda = 271^\circ$ per sidereal day, about $11.3^\circ$ per hour. *Reference:* Léon Foucault (1851), *Démonstration physique du mouvement de rotation de la Terre au moyen du pendule*, Comptes rendus hebdomadaires des séances de l'Académie des sciences 32, 135–138

## Teaching arc

1. **Predict at a new spot** (entry). Run the peg walk near the North Pole, ask for a prediction near the equator, then explain the answer by rolling the ball. *Why:* It separates the ball from the labels painted on it. *Predict:* If you walk around the same peg with the same string near the equator, will the arrow come back turned more, less, or the same? *Visual:* [[carry-an-arrow-around-a-loop]] *Uses:* `ways_in/every-spot-alike`, `checks/same-loop-anywhere`
2. **Double the ball** (entry). Ask for the turn on a ball twice as wide, then count surface to reach a quarter. *Why:* The quarter, not a half, is the heart of 1 over the radius squared. *Predict:* If the ball is twice as wide, how does the turn around the same small loop change? *Visual:* [[carry-an-arrow-around-a-loop]] *Uses:* `ways_in/double-the-ball`, `checks/double-the-ball`
3. **Measure the radius from inside** (entry). Work the explorer's three steps, then set the moon problem. *Why:* It turns the curving number into a measurement of size. *Uses:* `ways_in/find-the-radius-without-leaving`, `problems/radius-of-a-small-moon`
4. **Compute from the metric** (working). Derive the Riemann component, then confront the sine-squared and pole traps. *Why:* The sphere is where students first meet coordinate artefacts in curvature. *Predict:* Does sine squared theta mean the sphere curves less near its poles? *Uses:* `derivations/sphere-curvature-from-metric`, `checks/sin-squared-varies`, `checks/christoffels-at-the-pole`
5. **Check against measurements** (working). Compare the arrow, the triangle and the ring on Earth, then diagnose a stranger's sign. *Why:* Independent readings that agree are what make the sphere the calibration geometry. *Visual:* [[paced-ring-on-a-ball-and-a-plain]] *Uses:* `ways_in/three-measurements-one-number`, `worked_examples/earth-read-three-ways`, `checks/stranger-gets-a-minus-sign`
6. **Prove it without coordinates** (formal). Derive constancy from symmetry, then test the rigidity theorems on the projective plane and the spindle. *Why:* It shows which hypotheses make the sphere unique. *Uses:* `ways_in/round-sphere-as-a-space-form`, `checks/closed-surfaces-with-constant-curvature`, `problems/spindle-with-two-tips`

## Misconceptions

### “A globe curves more strongly near its North Pole, where the painted lines crowd together.” · entry · `poles-curve-more`

- **Why it is tempting:** On a globe the lines bunch up at the poles, as if something special happens there.
- **What is true:** The painted lines are only labels. A round ball looks the same after any roll, so the same walk gives the same turn at every spot.
- **Exposed by:** `checks/same-loop-anywhere`

### “A ball twice as wide curves half as strongly.” · entry · `twice-as-wide-half-as-curved`

- **Why it is tempting:** A circle twice as wide bends half as sharply.
- **What is true:** The turn follows the fraction of the ball's surface area, and the surface area grows with the radius times itself. So a ball twice as wide curves a quarter as strongly.
- **Exposed by:** `checks/double-the-ball`

### “The Riemann component in theta and phi is sine squared theta, so the sphere curves most at its equator and not at all at its poles.” · working · `varying-component-means-varying-curvature`

- **Why it is tempting:** Components are the numbers students compute, and this one visibly changes with latitude.
- **What is true:** A coordinate component carries the lengths of its basis vectors, and the longitude basis vector shrinks toward the poles. Dividing that out gives one over a squared everywhere.
- **Exposed by:** `checks/sin-squared-varies`

### “The sphere's geometry breaks down at the poles, because a Christoffel symbol there is infinite.” · working · `pole-is-singular`

- **Why it is tempting:** Infinite coefficients usually signal something physical.
- **What is true:** The coordinates fail at the poles, not the sphere. The curvature invariants stay constant there, and rotated coordinates make every Christoffel symbol finite.
- **Exposed by:** `checks/christoffels-at-the-pole`

### “The Ricci scalar of a sphere is its curvature, one over the radius squared.” · working · `ricci-scalar-equals-k`

- **Why it is tempting:** Both are single numbers called curvature.
- **What is true:** On a surface the Ricci scalar is twice the Gaussian curvature, two over the radius squared. The rotation around a small loop is set by the Gaussian curvature.
- **Exposed by:** `checks/soap-bubble-numbers`

### “Any formula that gives a sphere a negative Riemann component or Ricci scalar is wrong.” · working · `negative-sphere-means-mistake`

- **Why it is tempting:** The course gives a sphere positive values, and a sphere obviously curves one way.
- **What is true:** The printed sign depends on the Riemann sign, the Ricci contraction and the metric's overall sign. Only after matching those conventions does a negative value signal an error.
- **Exposed by:** `checks/stranger-gets-a-minus-sign`

### “Any closed surface with curvature one over a squared at every point is a round sphere of radius a.” · formal · `constant-k-means-round-sphere`

- **Why it is tempting:** Constant curvature seems to fix the shape completely.
- **What is true:** It holds for smooth, compact, orientable surfaces without boundary. The projective plane is another compact case, and cone points allow spindles.
- **Exposed by:** `checks/closed-surfaces-with-constant-curvature`

## Checks

1. **Entry · predict** `checks/same-loop-anywhere`. On a huge, smooth, round globe, you push a peg into the ground near the North Pole and tie a 5-metre string to it. You walk once around the peg, keeping the string tight and the peg on your left. Your cardboard arrow never swings, and it comes back turned 3 degrees toward your left. Then you move the peg to a spot near the equator and walk around it the same way, with the same string. How far, and toward which side, does the arrow come back turned?
   - **Hints:** Could you roll the globe so the new peg lands where the old peg was? / Does the arrow test use the painted lines?
   - **Answer:** Turned 3 degrees toward your left again. Imagine rolling the whole globe until the new peg sits where the old peg was. A smooth, round ball looks and feels the same after any roll. Only the painted lines move, and the arrow test never uses them. So the second walk is the first walk over again, with the same turn. The lines crowding near the North Pole do not make the ball curve more strongly there.
   - **Must contain:** It comes back turned 3 degrees toward your left; Rolling the ball brings the new peg onto the old spot; A round ball looks the same after any roll, and the painted lines do not matter
   - **Numeric:** turn toward the walker's left = 3 deg (signed, ±0.5, mod 360)
   - **Targets:** `poles-curve-more`
   - **Visual:** [[carry-an-arrow-around-a-loop]]
2. **Entry · numeric** `checks/double-the-ball`. On a smooth, round ball with a radius of 10 centimetres, you walk a small loop that keeps 14 square centimetres on your left. Your cardboard arrow never swings, and it comes back turned 8 degrees toward your left. Now you walk a loop that keeps the same 14 square centimetres on your left, on a ball with a radius of 20 centimetres. How far does the arrow come back turned?
   - **Hints:** How much more surface does a ball twice as wide have?
   - **Answer:** About 2 degrees toward your left. The turn, in full turns, is twice the fraction of the ball on your left. A ball's surface area is about 12.57 times its radius times itself. Doubling the radius makes the radius times itself four times as big, so the bigger ball has four times the surface area. So the same 14 square centimetres is a quarter of the fraction it was, and the turn is a quarter of 8 degrees. It is not 4 degrees, because the surface area grows with the radius times itself, not with the radius.
   - **Must contain:** About 2 degrees toward your left; The bigger ball has four times the surface area; The same area is a quarter of the fraction, so a quarter of the turn
   - **Numeric:** turn toward the walker's left = 2 deg (signed, ±0.3, mod 360)
   - **Targets:** `twice-as-wide-half-as-curved`
   - **Visual:** [[carry-an-arrow-around-a-loop]]
3. **Working · evaluate-claim** `checks/sin-squared-varies`. On a sphere of radius $a$, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. A student says: this is largest on the equator and zero at the poles, so the sphere curves most strongly at its equator and not at all at its poles. Evaluate the claim.
   - **Hints:** How long is the basis vector along $\phi$ at colatitude $\theta$?
   - **Answer:** The claim is wrong. A coordinate component carries the lengths of the basis vectors it is taken on, and $\partial_\phi$ has length $a\sin\theta$, which shrinks to zero at the poles. The Gaussian curvature divides this out: $K = R_{\theta\phi\theta\phi}/(g_{\theta\theta}g_{\phi\phi}) = a^2\sin^2\theta/(a^4\sin^2\theta) = 1/a^2$ at every $\theta$, equal to the orthonormal component. Rotations carry any point of the sphere to any other and preserve the metric, so no point can curve more strongly than another. A small coordinate cell confirms it: its turn, $K$ times its area $a^2\sin\theta\,\delta\theta\,\delta\phi$, shrinks near the poles only because the cell does.
   - **Must contain:** Coordinate components carry basis-vector lengths; K equals one over a squared at every point; Rotational symmetry rules out a special point
   - **Targets:** `varying-component-means-varying-curvature`
4. **Working · evaluate-claim** `checks/christoffels-at-the-pole`. On the sphere, $\Gamma^\phi{}_{\theta\phi} = \cot\theta$ grows without bound as $\theta \to 0$. A classmate concludes that the sphere's geometry is singular at the North Pole. Evaluate the conclusion.
   - **Hints:** What does the flat plane in polar coordinates do at its origin?
   - **Answer:** The conclusion is wrong: the chart fails there, not the geometry. At $\theta = 0$ every value of $\phi$ names the same point and $g_{\phi\phi} = a^2\sin^2\theta$ vanishes, just as polar coordinates on a flat plane give $\Gamma^\phi{}_{r\phi} = 1/r$ at the origin. Christoffel symbols are not tensors, so their growth alone says nothing about the geometry. The invariants stay finite and constant as $\theta \to 0$: $K = 1/a^2$ and $R = 2/a^2$. Rotating the sphere so that the old North Pole lies on the new equator makes every Christoffel symbol finite there.
   - **Must contain:** The coordinates fail at the pole; Christoffel symbols are not tensors; K and R stay constant at the pole
   - **Targets:** `pole-is-singular`
5. **Working · numeric** `checks/soap-bubble-numbers`. A soap bubble has radius 4.0 cm. Treating its film as a sphere, find its Gaussian curvature and Ricci scalar in SI units, and the angle by which a vector carried around a small loop enclosing 1.0 cm² returns rotated.
   - **Hints:** Convert the radius and the area to metres first.
   - **Answer:** $K = 1/a^2 = 1/(0.040\ \text{m})^2 = 625$ m$^{-2}$, and $R = 2K = 1250$ m$^{-2}$. For a small loop the rotation is $KA = 625\ \text{m}^{-2}\times1.0\times10^{-4}\ \text{m}^2 = 0.0625$ rad, about $3.6^\circ$ toward the walker's left. Using $R$ in place of $K$ would double the rotation, because on a surface the Ricci scalar is twice the Gaussian curvature.
   - **Must contain:** K is 625 per square metre; R is twice K, 1250 per square metre; The rotation is K times the area, 0.0625 radians
   - **Numeric:** Gaussian curvature = 625 m^-2 (magnitude, ±2%); Ricci scalar = 1250 m^-2 (magnitude, ±2%); rotation = 0.0625 rad (magnitude, ±3%)
   - **Targets:** `ricci-scalar-equals-k`
6. **Working · evaluate-claim** `checks/stranger-gets-a-minus-sign`. A formula sheet reports that a sphere of radius $a$ has $R^\theta{}_{\phi\theta\phi} = -\sin^2\theta$ and $R = -2/a^2$. A student decides the sheet is wrong. Evaluate the decision, and say what to check.
   - **Hints:** Which convention change flips the Riemann component itself?
   - **Answer:** The sheet is not necessarily wrong. What happens on the sphere is fixed: a small loop with its region on the walker's left returns vectors rotated toward the left, and rings come out short. How that is written depends on conventions. A Riemann tensor defined with the opposite overall sign flips $R^\theta{}_{\phi\theta\phi}$ and $R$ together, which matches this sheet. Contracting a different pair of slots, or writing the metric with an overall minus sign, flips $R$ but leaves $R^\theta{}_{\phi\theta\phi}$ unchanged. So read the sheet's definitions of the Riemann tensor, the Ricci contraction and the metric, and run the flat plane in polar coordinates, which must give zero in every convention. Only if the definitions match the course's is the sign an error.
   - **Must contain:** The observed rotation fixes the geometry, not the printed sign; An opposite Riemann sign flips both printed values; Check the definitions and the flat-plane control before calling it an error
   - **Targets:** `negative-sphere-means-mistake`
7. **Formal · derive** `checks/symmetry-fixes-the-curvature`. Without computing any connection, show that the round sphere $S^2_a \subset \mathbb{R}^3$ has constant Gaussian curvature, that $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$, and that $K = 1/a^2$. Which step fails for a round 3-sphere, and what replaces it?
   - **Hints:** Does an isometry change the Gaussian curvature? / How many 2-planes does a tangent space of dimension 2 contain?
   - **Answer:** Rotations in $SO(3)$ restrict to isometries of the induced metric and act transitively on $S^2_a$. The Gaussian curvature is determined by the metric, so isometries preserve it, and $K$ is constant. In two dimensions the space of 2-planes at a point is a single plane, so the Riemann tensor is fixed by one number; $K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ has the Riemann symmetries and the right sectional curvature, so it equals $R_{\mu\nu\rho\sigma}$. Gauss–Bonnet gives $K\cdot4\pi a^2 = 2\pi\chi(S^2) = 4\pi$, so $K = 1/a^2$. On a round 3-sphere transitivity on points makes only scalar invariants constant. Each point has a family of 2-planes, so one needs the isotropy group $SO(3)$ acting transitively on those planes to make every sectional curvature equal. The value then comes from a great 2-sphere, which is totally geodesic with $K = 1/a^2$, giving $R = 6/a^2$.
   - **Must contain:** Isometries act transitively and preserve K; In two dimensions one number fixes the Riemann tensor; Gauss–Bonnet fixes K at one over a squared; In three dimensions isotropy on 2-planes is also needed
8. **Formal · evaluate-claim** `checks/closed-surfaces-with-constant-curvature`. Evaluate the claim: "A compact surface whose Gaussian curvature is $1/a^2$ at every point is a round sphere of radius $a$." Give hypotheses under which it holds, and the other possibilities.
   - **Hints:** What does Gauss–Bonnet say about the Euler characteristic?
   - **Answer:** As stated it is false. For a compact smooth surface without boundary, Gauss–Bonnet gives $2\pi\chi = \int K\,dA = A/a^2 > 0$, so $\chi = 2$ or $\chi = 1$. A compact surface is complete, so by Killing–Hopf it is $S^2_a$, with area $4\pi a^2$, or the real projective plane $S^2_a/\{\pm1\}$, with area $2\pi a^2$, which is non-orientable. So the claim holds for compact orientable smooth surfaces without boundary; for surfaces in $\mathbb{R}^3$, where the projective plane cannot occur, it is Liebmann's theorem. A compact surface with boundary, such as a hemisphere, fails at once. Smoothness is also needed: a spindle $d\rho^2 + b^2\sin^2(\rho/a)\,d\phi^2$ with $b < a$ has $K = 1/a^2$ except at two cone points.
   - **Must contain:** Gauss–Bonnet allows Euler characteristic 2 or 1; The projective plane is the other compact case; Orientability, no boundary and smoothness make the claim true
   - **Targets:** `constant-k-means-round-sphere`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which angle is theta and which is phi on a sphere | $\theta$ is colatitude, measured from the North Pole with $0 \le \theta \le \pi$, and $\phi$ is longitude, so $d\Omega^2 = d\theta^2 + \sin^2\theta\,d\phi^2$ and $a$ names the sphere's radius, not a scale factor. | Some texts, especially in mathematics, swap the letters and use $\phi$ for colatitude; geography uses latitude $\lambda = \pi/2 - \theta$, so $\cos\lambda$ replaces $\sin\theta$. |
| Printed sign of the sphere's curvature | $R^\theta{}_{\phi\theta\phi} = +\sin^2\theta$, $K = +1/a^2$ and $R = +2/a^2$. | Texts with the opposite overall Riemann sign print $-\sin^2\theta$ and $R = -2/a^2$; texts that contract another pair of slots keep the component but print $R = -2/a^2$. |

## Visuals

- ★ [[carry-an-arrow-around-a-loop]] (flagship): The entry picture: one loop of fixed area on balls of different sizes and at different spots, showing equal turns everywhere and a quarter of the turn on a ball twice as wide. *Sketch:* Two smooth balls side by side with radius sliders, each carrying a loop of the same area in square centimetres. Play carries an arrow around both loops; on completion readouts give each turn, the turn divided by the area, and 1 over the radius squared. A roll control moves one loop to any spot and heading while its readouts stay fixed, and an egg toggle breaks that. A plot of turn per area against radius on logarithmic axes shows a line of slope $-2$.
- [[paced-ring-on-a-ball-and-a-plain]] (supporting): The tape-measure reading of the sphere's curvature. *Sketch:* This concept adds a readout of the radius recovered from one ring by solving $C = 2\pi a\sin(\rho/a)$, which matches the ball's radius for every string length up to the far pole, where the ring shrinks to a point.

## Tutor moves

**Open with**

- Picture a tennis ball and a beach ball ten times as wide, both smooth and round. On each one, you walk the same small loop, about the size of a fingernail, carrying a cardboard arrow that never swings. On which ball does the arrow come back turned more, and about how many times more? *(prediction)*
- If you lived on a huge round ball and could never leave it or see it from outside, how could you find out how big it is? *(reflection)*

**If the learner is stuck**

- *The learner cannot turn a measured turn into a radius.* → Split the task into the explorer's three steps, fraction, whole surface, radius, and do one step per exchange. *Uses:* `ways_in/find-the-radius-without-leaving`
- *The learner loses track of the four terms of the Riemann component.* → Write the four terms in a column, cross out those containing a zero Christoffel symbol, and evaluate the two that remain. *Uses:* `derivations/sphere-curvature-from-metric`
- *The learner expects the North Pole to curve differently.* → Have the learner imagine rolling the ball until the second peg lands on the first. *Uses:* `checks/same-loop-anywhere`

**Common questions**

- *Is Earth's curving really the same everywhere?* (entry) Nearly. Earth spins, so it bulges slightly at the equator and is flattened at the poles. That makes its curving about one and a third percent stronger at the equator than at the poles. Hills and valleys add bumps of their own, but on the scale of whole countries Earth is very close to a round ball. *Uses:* `observations/earth-from-geodesy`
- *Why does a ball twice as wide curve a quarter as strongly, and not half as strongly?* (entry) Because the turn follows area, and area grows with the radius times itself. A ball twice as wide has four times the surface area. So a loop of fixed size keeps a quarter of the fraction of that ball on your left, and the arrow turns a quarter as much. A single curved line is different: a circle twice as wide bends half as sharply, because its length grows only with the radius. *Uses:* `ways_in/double-the-ball`, `checks/double-the-ball`
- *Why is the sphere the standard test for curvature formulas?* (working) Its answer is known before any calculation: symmetry makes $K$ constant, the area rule or Gauss–Bonnet fixes $K = 1/a^2$, and the direction arrows rotate fixes the sign. It also has a nonzero product term and a coordinate singularity at the poles, so it exercises every part of the formula. Pair it with the flat plane in polar coordinates, which must give zero. *Uses:* `ways_in/curvature-from-the-metric`, `checks/stranger-gets-a-minus-sign`

**Switching levels**

- To working when: asks for the formula behind the quarter; mentions a metric or Christoffel symbols. Go to the metric calculation and the soap-bubble check. *Uses:* `ways_in/curvature-from-the-metric`, `checks/soap-bubble-numbers`
- To formal when: asks why the answer must be constant without computing; asks which closed surfaces have constant curvature. Use the symmetry argument, then the rigidity theorems and the spindle. *Uses:* `ways_in/round-sphere-as-a-space-form`, `problems/spindle-with-two-tips`
- To research when: asks about black-hole horizons, Ricci flow or quasi-local energy. Open the research horizon. *Uses:* `research_horizon/horizon-geometry`, `research_horizon/ricci-flow-on-the-sphere`

**Pronunciations:** Riemann → REE-mahn; Ricci → REE-chee; Christoffel → kris-TOFF-ul; Gauss–Bonnet → GOWSS bon-AY; Liebmann → LEEB-mahn

**Voice notes:** At entry say "the radius times itself", not "radius squared". Read colatitude as "the angle from the North Pole".

## History

- **Carl Friedrich Gauss (1827).** Measured a surface's curvature by the area its normals sweep, which gives $1/a^2$ for a sphere, and proved that this number depends only on lengths along the surface. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Ferdinand Minding (1839).** Showed that surfaces with the same constant curvature are locally isometric, so every patch with curvature $1/a^2$ matches a piece of a sphere of radius $a$.
- **Bernhard Riemann (1854).** In his 1854 lecture, published in 1868, extended curvature to spaces of any dimension and described spaces of constant positive curvature, of which the sphere is the two-dimensional case. Bernhard Riemann (1868), *Ueber die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150
- **Heinrich Liebmann (1899).** Proved that a closed surface in ordinary space with constant Gaussian curvature is a round sphere.

## Research horizon

- **Ricci flow on the two-sphere.** Ricci flow evolves a metric by $\partial_t g_{\mu\nu} = -2R_{\mu\nu}$, which on a surface is $-2Kg_{\mu\nu}$. Hamilton showed that, with the area held fixed, a metric of positive curvature on the sphere flows to the round metric of constant $K$, and Chow removed the positivity assumption. Hamilton's programme in three dimensions led to Perelman's proof of the Poincaré conjecture. Richard S. Hamilton (1988), *The Ricci flow on surfaces*, Mathematics and General Relativity, Contemporary Mathematics 71, 237–262, American Mathematical Society; Bennett Chow (1991), *The Ricci flow on the 2-sphere*, Journal of Differential Geometry 33, 325–334, doi:10.4310/jdg/1214446319
- **Intrinsic geometry of black-hole horizons.** Hawking showed that cross-sections of the event horizon of a stationary black hole are two-spheres, under the dominant energy condition. For Schwarzschild the cross-section is round, with $K = 1/4M^2$ in $G = c = 1$ units. Smarr found that the Kerr horizon is not round: its Gaussian curvature turns negative near the poles once $J/M^2 > \sqrt3/2$, while its total stays $4\pi$, as Gauss–Bonnet requires. Stephen W. Hawking (1972), *Black holes in general relativity*, Communications in Mathematical Physics 25, 152–166, doi:10.1007/BF01877517; Larry Smarr (1973), *Surface geometry of charged rotating black holes*, Physical Review D 7, 289–295, doi:10.1103/PhysRevD.7.289
- **Embedding spheres and quasi-local energy.** Weyl asked whether every metric on the sphere with $K > 0$ is realized by a convex surface in $\mathbb{R}^3$, and Nirenberg proved it. Brown and York use such embeddings as the reference for the quasi-local energy inside a closed two-surface. For a round sphere of areal radius $r$ in Schwarzschild, with $G = c = 1$, their energy is $r\,(1 - \sqrt{1 - 2M/r})$. Louis Nirenberg (1953), *The Weyl and Minkowski problems in differential geometry in the large*, Communications on Pure and Applied Mathematics 6, 337–394, doi:10.1002/cpa.3160060303; J. David Brown, James W. York (1993), *Quasilocal energy and conserved charges derived from the gravitational action*, Physical Review D 47, 1407–1419, doi:10.1103/PhysRevD.47.1407

## Review: novice

**Verdict:** fixed (2026-09-16, revision 3)

**Retell attempt:** A round ball curves the same amount everywhere, because you can roll it and it looks exactly the same, so the lines crowding at the top of a globe don't mean it curves more there. If you walk around a peg on a string, the arrow comes back turned the same 3 degrees at the pole and at the equator; an egg would give different turns. A ball twice as wide has four times the skin, so the same little loop is only a quarter of the fraction, so the arrow turns a quarter as much, 2 degrees instead of 8. So the curving 'goes with' 1 over the radius times itself, and that's called Gaussian curvature; I'm not sure what 'goes with' means exactly, or where 12.57 comes from. An explorer can find her planet's radius from the turn and the area: turn to fraction (half of the turn in full turns), fraction to whole surface, surface to radius, about 239 km. On Earth the turn is millionths of a degree so nobody notices. I was unsure which 'piece of ground on her left' she measures, and I read 'the whole surface' as the skin, not a number.

**Stumbles (15)**

- “a ball twice as wide curves a quarter as strongly, since its curving goes with 1 divided by the radius times itself”: 'Goes with' is vague to a novice (goes along with? grows with?), and the summary's sentences average 24 words.
- “The lines crowd together near the North Pole.”: Only the pole-to-pole lines crowd at the pole; the circles around it shrink instead. A teen picturing a globe sees both kinds of line.
- “Say your arrow comes back turned 3 degrees toward your left.”: The explanation never says the walker is carrying an arrow; the recap is hidden for readers arriving in sequence.
- “Imagine rolling the whole globe until the new peg sits where the old peg was.”: 'Where the old peg was' has no reference: the old spot rolls along with the globe, so the reader cannot picture what stays fixed.
- “Try again with a hard-boiled egg: the pointed end tells you at once.”: Tells you what? The try-it does not say what to notice.
- “In full turns, the turn is twice the fraction of the ball in that piece.”: Two ideas squeezed into one 21-word sentence: measuring a turn in full turns, and the fraction rule. 'Fraction of the ball' does not say fraction of what.
- “Take two smooth, round balls. One has a radius of 10 centimetres.”: A person cannot walk a loop on a 10-centimetre ball; the rule is not physically followable as written, and the way does not refer back to the way it continues.
- “A ball's surface is about 12.57 times its radius times itself.”: 'Surface' is used for two ideas, the skin of the ball and its area as a number, and 12.57 appears with no reason.
- “So the strength of a ball's curving goes with 1 divided by the radius times itself.”: A step is left implicit: the reader has seen the turn-per-area drop to a quarter, but not that 1 over radius squared does the same.
- “That number, 1 divided by the radius times itself, is called the ball's Gaussian curvature.”: The first what-if a teen tries is a smaller ball; the way never says which direction the rule runs for that.
- “She also measures the piece of ground on her left.”: Ambiguous piece: the ground beside her, or the region the loop fences off?
- “Dividing 720,000 by 12.57 gives about 57,300. The radius is the number that gives 57,300 when multiplied by itself”: Implicit step: 57,300 is never named as the radius times itself.
- “Take a loop whose piece on the left covers 51,000 square kilometres”: 'Whose piece on the left' is squeezed wording; the rest of the note says 'keeps ... on your left'.
- “How does the arrow come back?”: The check question does not say what kind of answer it wants (a size and a side).
- “Use the arrow test to find out.”: 'Arrow test' is used as a name throughout the entry rung but is not in the glossary.

**Fixes**

- Summary rewritten as three sentences averaging 19 words, replacing 'goes with' by the plain statement that the curving is 1 divided by the radius times itself.
- Every spot alike: pole-to-pole lines named; the walker now carries the arrow in the explanation itself; the rolling argument is referenced to a walker who stands still; the egg try-it says what to feel.
- Recaps of the two rule-using entry ways split into short sentences, with 'in full turns' explained by an example and 'fraction' tied to the ball's whole surface area.
- Double the ball: opening bridge to the first way; 'imagine you are small enough to walk on them'; 12.57 explained as 4 times pi; the missing step that 1 over radius squared also drops to a quarter; the half-radius what-if; takeaway says 'Gaussian curvature is' instead of 'goes with'.
- Find the radius: opening bridge to the two balls; the measured piece is the one the loop fences off; radius squared named at 57,300 square kilometres; 'keeps ... on your left' wording matched to the rest of the note.
- 'Surface' replaced by 'surface area' wherever a number is meant (entry ways, check double-the-ball, misconception twice-as-wide-half-as-curved, problem radius-of-a-small-moon, common question why-a-quarter-not-a-half).
- Glossary: added 'arrow test'. Check same-loop-anywhere asks for size and side. Working way: theodolite named as the surveyor's angle-measuring telescope. Prerequisite riemann-curvature-tensor moved from entry to working, since the entry ways use only the arrow test and the working way needs the component formula.
- Nothing dropped; the additions used the review allowance.

**Concerns**

- Entry way words are now 987 of the 1000 core cap (recaps included); any further entry addition must drop something.
- The working way uses index notation through riemann-curvature-tensor (working) and two-sphere-metric; there is no direct index-notation prerequisite. Fine if transitive coverage is accepted.
- Physics reviewer: the 5-metre string giving 3 degrees implies a globe of radius about 39 m, consistent but unstated; '1.3 percent weaker at the poles' (way 1) versus '1.35% larger at the equator' (working way) are the same fact rounded differently; 'thin pencil lead at arm's length' for 0.072 degrees fits a 0.7 mm lead at about 60 cm.
- The flagship visual one-loop-on-two-balls and paced-ring-on-a-ball-and-a-plain are still proposals, not catalog entries.

**Re-read** (2026-09-16, revision 3): 0 stumbles in 1 changed passages


## Review: physics

**Verdict:** fixed (2026-09-16, revision 3)

**Verification**

- Christoffel symbols Γ^θ_φφ = -sinθcosθ, Γ^φ_θφ = cotθ and R^θ_φθφ = sin²θ with the course Riemann formula.: Re-derived by hand from the course definitions, term by term as in the derivation (derivative term sin²θ - cos²θ, one surviving product term cos²θ); central finite difference of Γ^θ_φφ at θ = 1 in python. → Correct: 0.70807 vs sin²(1) = 0.70807. Index placement and the order of the four terms match the conventions row.
- K = R_θφθφ/(g_θθ g_φφ) = 1/a², R_μν = g_μν/a² (R_θθ = 1, R_φφ = sin²θ), R = 2/a², G_μν = 0, Kretschmann 4K², and the orthonormal component equals K.: Contraction of K(g g - g g) by hand; frame conversion factor a·(1/a sinθ)·(1/a)·(1/a sinθ) applied to sin²θ. → All correct and positive, agreeing with the conventions row 'a sphere of radius a has R = +2/a²'.
- Cartan derivation: ω^1_2 = -cosθ dφ, Ω^1_2 = sinθ dθ∧dφ = a^{-2} e^1∧e^2, R^1_212 = 1/a²; spindle hint Ω^1_2 = -(f''/f) e^1∧e².: Solved de^a = -ω^a_b∧e^b by hand for general e^2 = f dφ, then set f = a sinθ and f = b sin(ρ/a). → Correct; the sphere is the f = a sinθ case of the spindle formula, and both give K = 1/a².
- Hat-box problem: the three Christoffel symbols, R^z_φzφ = (a² - z²)/a², both product terms +z²/a², K = 1/a², area element a dz dφ.: Hand derivation from g_zz = a²/(a² - z²), g_φφ = a² - z²; python evaluation at z = 0.3a. → R^z_φzφ = 0.91 = (a² - z²)/a², K = 1.000. Correct, including the Archimedes band area 2πa(z₂ - z₁).
- Spindle problem: K = 1/a², cone angle 2πb/a, deficit 2π(1 - b/a), ∫K dA = 4πb/a, balance 4π; b = a/2 gives 2π + π + π.: Integral (1/a²)·2π·b·2a by hand and python. → Correct; Gauss–Bonnet balance holds exactly.
- Earth worked example: K = 2.464e-14 m^-2, R = 4.927e-14 m^-2, excess 50.8 arcsec for 10,000 km², ring of 100 km short by 25.8 m (fraction 4.1e-5 = Kρ²/6), radius 6.37e6 m recovered.: python3 with a = 6.371e6 m; exact 2πρ - 2πa sin(ρ/a) against πρ³/3a². → 50.82 arcsec, 25.80 m exact vs 25.80 m series, 6.372e6 m. All within the stated rounding.
- Entry numbers: 5 m string and 3° imply a globe of radius 38.7 m (exact cap formula gives 3.00°); 1 km string on Earth 4.4 millionths of a degree; 14 cm² on 10 cm and 20 cm balls gives 8.02° and 2.01°; 1 km² on Earth 1.4 millionths of a degree; explorer 1/720, 720,000 km², 57,300 km², 239 km; Costa Rica 51,000 km² gives 0.0720° and 6371 km back; pencil lead 0.75 mm at 60 cm.: python3, using Δα = A/a² and the exact cap turn 2π(1 - cos(ρ/a)). → All reproduce. Sense: the peg on the walker's left puts the fenced-off disc on the left, so the turn is toward the left, as stated.
- Moon problem 195.4 km (rel_tol 0.02) and soap-bubble check K = 625 m^-2, R = 1250 m^-2, rotation 0.0625 rad = 3.6°.: python3; the moon both by the three entry steps with 12.57 and exactly with a² = A/Δα. → 195.41 km by the steps, 195.44 km exact; bubble values exact. Tolerances adequate.
- GRS80 numbers: mean radius 6371.0 km, K = 2.464e-14 and R = 4.927e-14 m^-2; K from 2.442e-14 (poles) to 2.475e-14 m^-2 (equator); 1.35% larger at the equator, 1.3 percent weaker at the poles, 'one and a third percent'.: python3 with a = 6378137 m, f = 1/298.257222101: K_pole = b²/a⁴, K_eq = 1/b², mean radius (2a + b)/3. → 6371.009 km, 2.4417e-14, 2.4747e-14, ratio 1.01352 (1.35% larger at the equator; poles 1.33% weaker). All three phrasings are one fact.
- Foucault: parallel transport eastward around latitude λ keeps the polar cap, area 2πa²(1 - sinλ), on the walker's left; holonomy 2π(1 - sinλ) counterclockwise ≡ clockwise 2π sinλ; Paris 271° per sidereal day, 11.3° per hour.: Sense checked against the conventions row (region on the left gives a positive, counterclockwise-from-outside turn); python for 360 sin 48.85° and division by 23.934 h. → 271.1° and 11.33° per hour. Sense and branch correct; the statement is scoped to the northern hemisphere, where 'seen from above the North Pole' agrees with 'seen from outside at the pendulum'.
- Formal way: chart covers the sphere minus a closed half meridian; Ω^1_2 frame-invariant because SO(2) is abelian; three Killing fields = n(n+1)/2; Gauss–Bonnet 4π; Minding, Killing–Hopf (S² or RP²), Liebmann, Bonnet–Myers with Cheng's equality case; b cos(s/a) profiles; areal radius.: Checked each statement's hypotheses against the standard theorems; K = -f''/f for f = b cos(s/a). → Accurate. Every theorem carries its hypotheses (complete, compact, smooth, in R³), and the counterexamples (RP², spindle, hemisphere) are placed correctly.
- Sign-diagnosis check: an opposite Riemann sign flips R^θ_φθφ and R together; another Ricci contraction or g → -g flips R only; the flat plane in polar coordinates gives zero with nonzero Christoffel symbols.: Γ is invariant under g → -g; R^r_φrφ = ∂_r(-r) + r·(1/r) = 0 by hand. → Correct.
- Research horizon: Hamilton 1988 (positive curvature on S² flows to round), Chow 1991 (no positivity needed); Hawking 1972 horizon topology under the dominant energy condition; Schwarzschild horizon K = 1/4M²; Kerr horizon K < 0 near the poles for J/M² > √3/2 (Smarr 1973); Weyl problem solved by Nirenberg 1953; Brown–York energy r(1 - √(1 - 2M/r)).: Checked against the papers' abstracts found in the reference searches and the standard results. → Accurate and current for a core note.
- References: Gauss 1828 (Comm. Soc. Reg. Sci. Gott. Rec. 6, 99–146), Riemann 1868 (Abh. Kgl. Ges. Wiss. Göttingen 13, 133–150), Moritz 1980 (Bull. Géod. 54, 395–405, doi 10.1007/BF02521480), Foucault 1851 (C. R. 32, 135–138), Hamilton 1988 (Contemp. Math. 71, 237–262), Chow 1991 (JDG 33, 325–334), Hawking 1972 (CMP 25, 152–166), Smarr 1973 (PRD 7, 289), Nirenberg 1953 (CPAM 6, 337–394), Brown and York 1993 (PRD 47, 1407–1419, gr-qc/9209012).: One web search each against publisher, ADS, Project Euclid, Wiley, Deutsches Textarchiv or arXiv records. → All ten confirmed and marked verified; dois added for Chow, Hawking, Smarr, Nirenberg and Brown–York. Minding 1839 and Liebmann 1899 have no work entry; their year and claim match the standard attributions.

**Counterexamples tried**

- Region larger than half the sphere: the summary's 'find its radius from a loop's area and its arrow's turn' fails, because the turn is known only modulo a full turn; a 1° turn with 1,000 km² on the left also fits a moon of radius 12.6 km whose loop fences off just over half the surface. Fixed by scoping the summary to a small loop; the entry recaps already say 'a small piece of the ball on your left'.
- Great circle (equator): turn 2π ≡ 0, consistent with 'most loops bring it back turned' and with the modulo in the area rule.
- Cone tip and spindle: constant K with cone points; the note uses the spindle as the smoothness counterexample and balances Gauss–Bonnet exactly.
- Real projective plane: compact, K = 1/a², not a sphere; handled by the orientability hypothesis in the check and the misconception.
- Hemisphere (surface with boundary): named in the check as failing the rigidity claim.
- Egg: a smooth closed surface that is not homogeneous; used at entry as the contrast to 'the same after any roll'.
- Flat plane in polar coordinates: nonzero Christoffel symbols with zero curvature; used as the control for the sign diagnosis, and R^r_φrφ = 0 was checked by hand.
- Southern hemisphere for Foucault: eastward transport keeps the large northern cap on the left, and 2π(1 - sinλ) with λ < 0 still reduces to a clockwise turn seen from above the North Pole, i.e. counterclockwise locally; the note's statement is correctly scoped to the northern hemisphere.

**Fixes**

- Summary: 'from a loop's area and its arrow's turn' became 'from a small loop's area and its arrow's turn', because the inversion from turn to radius needs the branch of the turn, which only a small region fixes.
- All ten references marked verified after one web search each; dois added for Chow 1991, Hawking 1972, Smarr 1973, Nirenberg 1953 and Brown–York 1993.

**Concerns**

- The summary change is one learner-visible word at the entry rung; revision bumped to 3 and the novice lens should re-read that sentence.
- The way 'A ball twice as wide curves a quarter as strongly' says the strength of the curving 'matches' 1 divided by the radius times itself; the turn per area equals 1/a² exactly only when the turn is in radians, so at entry 'matches' means 'scales the same way'. True as written, but the tutor should not let a learner divide degrees by square centimetres and expect 1/a².
- The check 'same-loop-anywhere' with a 5 m string and a 3° turn implies a globe of radius about 39 m; consistent, and 'huge' relative to a walker, but it is not stated.
- Visuals one-loop-on-two-balls and paced-ring-on-a-ball-and-a-plain remain proposals with sketches; the note reuses the catalog id carry-an-arrow-around-a-loop without a preset, which the catalog allows.

**Diff check** (2026-09-16, revision 3)

- Summary: someone who never leaves the ball can find its radius from a small loop's area and its arrow's turn (the physics review's added word 'small').: Turn = A/a^2 modulo 2 pi for a simple loop with the region on the walker's left. python3: A = 1000 km^2 with a 1 degree turn gives a = 239.4 km on the principal branch but also 12.6 km on the next branch, where the loop fences off 50.1 percent of that ball. Tried the domain counterexamples: region larger than half the ball (excluded by 'small'), reversed loop (turn changes sign, radius unchanged), great circle (turn is a whole turn, not small). → True as scoped: 'small' removes the branch ambiguity, and area and turn are both measurable from within (tiling, carried arrow). Read once more as the novice: 'its' can only be the loop's, and the arrow is known from the holonomy prerequisite at entry. No change.
