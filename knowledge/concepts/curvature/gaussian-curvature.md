---
type: "concept"
schema_version: 2
id: "gaussian-curvature"
title: "Gaussian curvature"
tagline: "One number for how strongly a surface curves at each spot, like a ball or a saddle"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["Gauss curvature"]
prerequisites: ["intrinsic-versus-extrinsic-curvature", "curvature-of-a-curve", "metric-tensor", "riemann-curvature-tensor"]
leads_to: ["theorema-egregium", "sectional-curvature", "angular-excess", "holonomy", "space-of-constant-curvature"]
visuals: ["paced-ring-on-a-ball-and-a-plain", "card-touching-a-curved-patch"]
---

# Gaussian curvature

*One number for how strongly a surface curves at each spot, like a ball or a saddle*

`gaussian-curvature` · curvature · foundation · physics-reviewed (revision 8)

**Needs:** [[intrinsic-versus-extrinsic-curvature]] (entry) · [[curvature-of-a-curve]] (entry) · [[metric-tensor]] (working) · [[riemann-curvature-tensor]] (formal)  
**Opens:** [[theorema-egregium]] · [[sectional-curvature]] · [[angular-excess]] · [[holonomy]] · [[space-of-constant-curvature]]  
**Related:** [[principal-curvatures]] · [[circumference-to-radius-test]] · [[ricci-scalar]]  
**Visuals:** [[paced-ring-on-a-ball-and-a-plain]] · [[card-touching-a-curved-patch]]

> At each spot of a smooth surface, one number, the Gaussian curvature, says how strongly the surface curves. It is positive where the surface curves like a ball, zero on flat paper, and negative on a saddle. An ant can measure it with small rings, and an outsider by multiplying two bends.

## You will be able to

**Entry**
- Compute a spot's Gaussian curvature from its matching ball, and compare balls of different sizes. `objectives/number-a-spot-from-its-matching-ball` ← `checks/marble-and-football`
- Predict the sign and size of the Gaussian curvature from a spot's two bends. `objectives/multiply-bends-with-signs` ← `checks/soap-film-waist`, `problems/swim-ring-two-spots`

**Working**
- Compute the Gaussian curvature from a line element, and predict how enlarging a surface changes it. `objectives/compute-k-from-a-line-element` ← `checks/scale-a-surface-up`

**Formal**
- Prove the Gauss map formula for K, and apply the Gauss–Bonnet total to closed surfaces. `objectives/prove-the-gauss-map-formula` ← `problems/gauss-map-pulls-back-area`, `checks/dented-ball-total`
- Explain why equal Gaussian curvature at corresponding points does not in general make two surfaces isometric. `objectives/decide-when-k-fixes-geometry` ← `checks/same-curvature-different-surfaces`

## Ways in

### 1. A matching ball for each spot · entry · operational

*How can an ant living on a surface give one number for how strongly it curves at one spot?*

**Recap:** Walking without ever steering left or right is called walking straight. The ring test: walk straight out the same distance from a centre in every direction, and mark where each walk ends. Then measure, along the ground, the ring that runs through those marks. On a flat plain the ring is about 6.28 times the distance walked. On a ball it comes out shorter.

Picture a smooth plastic egg, 6 centimetres long and 4 centimetres wide, with both ends the same shape. An ant lives on its shell. She runs the ring test at one tip, walking 2 millimetres out from her centre. Then she runs it on the egg's widest part, halfway between the tips.

Both rings come out shorter than 6.28 times 2 millimetres. To compare them, she divides the length each ring is missing by 6.28 times the distance walked. This is called the ring's missing fraction.

At the tip, the missing fraction is about 0.38 per cent. At the widest part, it is about 0.07 per cent, five times smaller. So the shell curves more strongly at the tip, which looks more pointed.

Balls give a scale to compare with. A football is about 70 centimetres around its middle. On it, a ring drawn 2 centimetres from its centre has a missing fraction of about 0.54 per cent. On a ball twice as wide, the same ring's missing fraction is about 0.13 per cent, a quarter as much. So for rings walked out the same short distance, the smaller the ball, the bigger the missing fraction.

To put a number on each spot, the ant looks for the ball on which a ring drawn 2 millimetres from its centre has the same missing fraction as her ring. This ball is called the matching ball of the spot. Her measurements give a matching ball of radius 1 and a third centimetres at the tip, and 3 centimetres at the widest part.

That second ball is wider than the egg. The reason is that from tip to tip, the shell there curves only gently. So the egg's rings there miss less than rings on a ball 4 centimetres wide.

Now multiply the matching ball's radius by itself, and divide 1 by the result. This number is called the Gaussian curvature of the spot. The radius times itself is in square centimetres, so the Gaussian curvature comes out per square centimetre.

At the widest part, 3 times 3 is 9, so the Gaussian curvature is 1 ninth, about 0.11 per square centimetre. At the tip, 1 and a third is 4 thirds, and 4 thirds times 4 thirds is 16 ninths. So the Gaussian curvature there is 9 sixteenths, about 0.56 per square centimetre, five times as big.

Why multiply the radius by itself? On the ball twice as wide as the football, the radius times itself is four times bigger. So 1 divided by it drops to a quarter, just as the missing fraction does. Dividing 1 by the radius alone would only halve it, and would not follow the rings.

Where small rings come out as on flat paper, the Gaussian curvature is zero. Near the middle of a saddle-shaped potato crisp, small rings come out too long. The crisp's wavy edge hints why. A ring longer than 6.28 times the distance from its centre cannot be laid on flat paper and stay that far from the centre, so the ring ripples. Near the crisp's middle, the ant finds the ball whose missing fraction equals the fraction by which her ring is too long. She works out that ball's number and gives it a minus sign.

Treat Earth as a smooth ball with a radius of 6,371 kilometres. Its Gaussian curvature is 1 divided by about 40.6 million square kilometres. A ring walked 1 kilometre from its centre is short by only about 0.026 millimetres, less than half the width of a hair. So nobody notices the curving on a walk.

**Try it:** Hold one end of a thread on a rubber ball about 7 centimetres across, and tie a pen 2 centimetres along the thread. Keep the thread tight along the ball, so that it never steers, and draw a ring. Lay the thread along the ring to measure it. You should find about 11.9 centimetres, some 7 millimetres short of 6.28 times 2, which is 12.6. On a basketball, the same ring is short by just over half a millimetre.

**Takeaway:** To get a spot's Gaussian curvature, multiply its matching ball's radius by itself and divide 1 by the result. It is zero where small rings come out as on flat paper, and negative where they come out too long.

*Builds on:* [[intrinsic-geometry]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/marble-and-football`

### 2. Multiply the two bends · entry · calculation

*How can someone looking at a surface from outside find the same number?*

**Recap:** A ring's missing fraction is the length it is missing, divided by 6.28 times the distance walked. The matching ball of a spot is the ball whose short rings have the same missing fraction as the spot's rings. To get the Gaussian curvature, multiply that ball's radius by itself and divide 1 by the result. Where a line bends, one circle matches the bend best, and the smaller that circle, the sharper the bend. A shell or a sheet has two faces, such as the inside and the outside of an eggshell.

Stand outside the plastic egg of "A matching ball for each spot", and pick a spot on its widest part. Picture ants walking straight out from that spot in every direction, like the spokes of a wheel. Seen from outside, each ant's short path bends, and its best-fit circle measures how sharply.

The path going around the egg, across its width, follows the egg's middle circle, whose radius is 2 centimetres. The path going along the egg, toward a tip, bends with a best-fit circle of radius 4.5 centimetres, as a careful drawing of the egg's outline shows. These two paths cross at a right angle. Every other path through the spot bends with a radius between 2 and 4.5 centimetres. So these two are the sharpest and the gentlest bends.

The outsider's rule is this: multiply the radii of the sharpest and the gentlest bends, and divide 1 by the result. At the widest part, 2 times 4.5 is 9, and 1 divided by 9 is 1 ninth. The ant's matching ball there had radius 3, and 3 times 3 is also 9. So the outsider gets the ant's number.

At the tip, every path bends alike, with a radius of 1 and a third centimetres. So the sharpest and the gentlest bends are the same, and the rule gives 9 sixteenths, the ant's number there too.

On the egg, every path bends toward the inside face of the shell. On a saddle-shaped potato crisp, some paths bend toward one face, and others toward the other face. There the rule changes in two ways: use the sharpest bend toward each face, and give the number a minus sign. That fits the ant, whose small rings on a crisp come out too long.

A rolled-up poster tests the rule. Through each spot, every path bends toward the same face, except the path along the tube, which does not bend at all. So the gentlest bend has no best-fit circle. The gentler a bend, the bigger its circle, so the bigger the two radii multiplied, and the closer 1 divided by that result gets to zero. So the number is zero, and the ant's rings on the poster agree: they come out as on flat paper.

Rolling a poster changes its bends. Yet it changes no length along the paper, so it never changes the rings. That is why the agreement is surprising: bends can change while rings cannot. Gauss proved in 1827 that the outsider's number depends only on lengths along the surface, just as the ant's rings do. So rolling a poster, or any change that keeps lengths along the surface, never breaks the agreement. The agreement holds at every spot of every smooth surface in ordinary space.

**Takeaway:** Multiply the radii of a spot's sharpest and gentlest bends, and divide 1 by the result. That is the ant's Gaussian curvature. On a saddle, use the sharpest bend toward each face instead, and give the number a minus sign.

*Continues:* `ways_in/a-matching-ball-for-each-spot`<br>*Builds on:* [[curvature-of-a-curve]], [[intrinsic-versus-extrinsic-curvature]]<br>*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `checks/soap-film-waist`, `problems/swim-ring-two-spots`

### 3. The number from the distance rule · working · calculation

*How is the Gaussian curvature computed from a surface's line element?*

The matching ball of "A matching ball for each spot" gives a ball of radius $a$ the Gaussian curvature $K = 1/a^2$, and the products in "Multiply the two bends" give the same numbers. Both can be read from the line element. Near any point of a smooth surface, choose coordinates $(\rho, \phi)$ in which the curves of constant $\phi$ are unit-speed geodesics, the paths of straight walks, crossing the curves of constant $\rho$ at right angles; distance and direction from a centre is one such choice. Then

$$ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2.$$

Neighbouring geodesics $\phi$ and $\phi + \delta\phi$ are a distance $D = f\,\delta\phi$ apart, and the gap law $\partial_\rho^2 D = -KD$ gives

$$K = -\frac{\partial_\rho^2 f}{f},$$

built one move at a time in the derivation "The curvature from the gap law".

- *Plane*, $f = \rho$: $K = 0$. A cylinder of radius $b$ has $ds^2 = dz^2 + b^2\,d\phi^2$, constant $f$, and $K = 0$, although it is bent.
- *Sphere* of radius $a$, $f = a\sin(\rho/a)$: $K = 1/a^2$. A ring has length $2\pi a\sin(\rho/a) = 2\pi\rho\,(1 - \rho^2/6a^2 + \dots)$, so short rings have the missing fraction $K\rho^2/6$, which is why the matching ball works.
- *Hyperbolic plane* with length scale $a$, $f = a\sinh(\rho/a)$: $K = -1/a^2$, and short rings are too long by the same fraction.
- *Swim ring*, tube radius $r$ around a centre circle of radius $b$: $ds^2 = r^2d\theta^2 + (b + r\cos\theta)^2d\phi^2$, so $\rho = r\theta$ and $K = \cos\theta/[r(b + r\cos\theta)]$. For $r = 10$ cm and $b = 25$ cm, $K = +1/350$ cm$^{-2}$ on the outer circle, $0$ on the top circle, and $-1/150$ cm$^{-2}$ on the inner circle, where bends of radii 10 cm and 15 cm go toward opposite faces.

$K$ has units of inverse length squared, so enlarging every length by a factor $\lambda$ divides it by $\lambda^2$, the quarter found for a football twice as wide. Because $K$ comes from the line element's coefficients and their derivatives alone, bending without stretching leaves it unchanged.

**Takeaway:** In coordinates where the line element is d rho squared plus f squared d phi squared, the Gaussian curvature is minus the second rho-derivative of f divided by f, with units of inverse length squared.

*Continues:* `ways_in/a-matching-ball-for-each-spot`, `ways_in/multiply-the-two-bends`<br>*Builds on:* [[metric-tensor]], [[curvature]]<br>*See:* `derivations/curvature-from-the-gap-law`, `checks/scale-a-surface-up`, `worked_examples/soap-film-between-two-rings`

### 4. Plumb lines sweep the sky · working · operational

*How can surveyors on Earth read its Gaussian curvature from plumb lines, and how does it vary over the globe?*

The bends multiplied in "Multiply the two bends" can be measured without leaving the ground, by watching which way a plumb line hangs. At each point of a smooth surface in space, let $\hat{\mathbf n}$ be the unit normal. On Earth a plumb line gives it, and sightings of stars fix its direction. Signed relative to $\hat{\mathbf n}$, the sharpest and gentlest bends, or on a saddle the sharpest toward each face, are the principal curvatures $\kappa_1$ and $\kappa_2$; they have opposite signs exactly when the bends go toward opposite faces, and their directions, at right angles, are the principal directions. Walk a distance $ds_1$ along a principal direction with principal curvature $\kappa_1$: the normal tilts by the angle $|\kappa_1|\,ds_1$ within the plane of that direction and the normal, and likewise along the perpendicular principal direction. A small ground rectangle of area $dA = ds_1\,ds_2$ therefore sends its normals over a patch of directions of solid angle $|\kappa_1\kappa_2|\,dA$. Where $\kappa_1\kappa_2 < 0$ the normals trace that patch in the reverse sense, and the solid angle $d\Omega$ counts as negative. So

$$K = \kappa_1\kappa_2 = \frac{d\Omega}{dA},$$

where the first equality, the product rule for intrinsic curvature, is taken on trust here.

- A sphere of radius $a$ sends the normals of a patch of area $A$ over $A/a^2$ steradians.
- A cylinder's normals fan out only around it, sweeping a curve of directions with no area, so $K = 0$.
- A connected closed surface with $K > 0$ everywhere sends its normals over every direction exactly once, so $\iint K\,dA = 4\pi$, as for a sphere; this is also taken on trust.

Earth's sea level is close to an ellipsoid of revolution. Its principal radii of curvature are $M$ along the meridian and $N$ at right angles to it, so $K = 1/MN$. Comparing plumb-line directions, measured against the stars, with distances measured along the ground fixes $M$ and $N$, as the classic arc surveys did. For the GRS80 reference ellipsoid, $M = 6335.4$ km and $N = 6378.1$ km at the equator give $K = 2.475\times10^{-14}$ m$^{-2}$, while $M = N = 6399.6$ km at the poles give $K = 2.442\times10^{-14}$ m$^{-2}$. So $K$ is 1.35% larger at the equator: the flattened poles curve more gently, although they are closer to Earth's centre.

**Takeaway:** The normals of a small patch sweep a solid angle equal to K times its area; on Earth this makes K about 1.35 per cent larger at the equator than at the flattened poles.

*What this leaves out:* Treats the plumb line as normal to the reference ellipsoid; real plumb lines deviate slightly, because Earth's mass is unevenly spread.

*Continues:* `ways_in/multiply-the-two-bends`<br>*Builds on:* [[intrinsic-versus-extrinsic-curvature]]<br>*See:* `observations/earth-curvature-from-surveys`

### 5. One number is the whole curvature of a surface · formal · structure

*In what precise sense is one number the whole curvature of a surface, and what does its integral know?*

The distance rule of "The number from the distance rule" and the normal sweep of "Plumb lines sweep the sky" express one object. Let $(\Sigma, g)$ be a smooth surface with a Riemannian metric, its Levi-Civita connection and the course Riemann tensor. At $p \in \Sigma$ the Gaussian curvature is the sectional curvature of the only 2-plane, $T_p\Sigma$:

$$K(p) = \frac{R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma}{g(X,X)\,g(Y,Y) - g(X,Y)^2}$$

for any basis $X, Y$ of $T_p\Sigma$.

*One component.* In two dimensions an antisymmetric index pair has one independent value, so the derivation "The Riemann tensor of a surface" finds $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$. Hence $R_{\mu\nu} = Kg_{\mu\nu}$, $R = 2K$, and the Einstein tensor vanishes identically. By Minding's theorem, surfaces with the same constant $K$ are locally isometric. Under a conformal change $\tilde g = e^{2u}g$, $\tilde K = e^{-2u}(K - \Delta_g u)$ with $\Delta_g = \nabla^\mu\nabla_\mu$; the half-plane metric $(dx^2 + dy^2)/y^2$, with $u = -\ln y$ over the flat plane, gives $\tilde K = -1$.

*Gauss map.* For an oriented surface immersed in $\mathbb R^3$ with unit normal $\hat{\mathbf n}$ and shape operator $S$, $d\hat{\mathbf n} = -S$, and the Gauss equation gives $K = \det S$. So $\hat{\mathbf n}: \Sigma \to S^2$ pulls the area form of $S^2$ back to $\det(-S)\,dA = K\,dA$, and reversing $\hat{\mathbf n}$ leaves $K$ unchanged, because a $2\times2$ determinant is even in $S$.

*Totals.* For compact oriented $\Sigma$ without boundary, the Gauss–Bonnet theorem, taken on trust here, gives $\iint_\Sigma K\,dA = 2\pi\chi(\Sigma)$: $4\pi$ for every surface shaped like a sphere, however dented, and $0$ for every torus. For $\Sigma \subset \mathbb R^3$ the Gauss map therefore has degree $\chi/2$.

*Limits.* Where $K$ varies, equal values need not mean equal geometry: the helicoid and the surface $z = \ln\sqrt{x^2 + y^2}$ share $K$ at corresponding coordinates, yet $|\nabla K|$ differs, so they are not isometric. $K$ needs a $C^2$ metric; a cone point of deficit $\delta$ carries curvature $\delta$ as a point mass in the Gauss–Bonnet sum. In $n \ge 3$ dimensions each 2-plane has its own sectional curvature, and by Schur's lemma, if these agree at each point of a connected manifold, the common value is constant. On a two-dimensional Lorentzian spacetime the one-component form and $R = 2K$ still hold, with a negative denominator.

**Takeaway:** On a surface the whole Riemann tensor is K times a fixed tensor, K is the signed Jacobian of the Gauss map, and its integral over a closed surface is 2 pi times the Euler characteristic.

*Continues:* `ways_in/the-number-from-the-distance-rule`, `ways_in/plumb-lines-sweep-the-sky`<br>*Builds on:* [[riemann-curvature-tensor]], [[intrinsic-versus-extrinsic-curvature]]<br>*See:* `derivations/riemann-of-a-surface`, `problems/gauss-map-pulls-back-area`, `checks/same-curvature-different-surfaces`, `checks/dented-ball-total`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| Gaussian curvature | GOW-see-un | A number for each spot of a smooth surface. Where small rings come out short, multiply the matching ball's radius by itself and divide 1 by the result. It is zero where small rings come out as on flat paper, and negative where they come out too long. | [[gaussian-curvature]] |
| matching ball | — | For a spot where small rings come out short, the ball on which a ring drawn the same short distance from its centre has the same missing fraction. | — |
| ring test | — | Walk straight out the same distance from a centre in every direction, and mark where each walk ends. Then measure, along the ground, the ring that runs through those marks. On a flat plain that ring is about 6.28 times the distance walked. | [[circumference-to-radius-test]] |
| missing fraction | — | How much shorter a ring is than 6.28 times the distance walked, divided by 6.28 times the distance walked. | [[circumference-to-radius-test]] |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| best-fit circle | — | At a place where a line bends, the circle that matches the bend best. The smaller the circle, the sharper the bend. | [[curvature-of-a-curve]] |
| face | — | One of the two sides of a sheet or a shell, such as the inside and the outside of an eggshell. | — |

## Key equations

### Gaussian curvature from the line element · working

$$
K = -\frac{\partial_\rho^2 f}{f}, \qquad ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2
$$

The Gaussian curvature is minus the second rho-derivative of the spacing $f$, divided by $f$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature | K |
| $\rho$ | distance along the geodesics of constant $\phi$ | rho |
| $f$ | spacing: neighbouring geodesics lie $f\,\delta\phi$ apart | f |

**Holds when:** Curves of constant $\phi$ are unit-speed geodesics orthogonal to curves of constant $\rho$; $f > 0$; exact.  
**Say it:** “K equals minus the second derivative of f with respect to rho, divided by f.”  
**Justified by:** `derivations/curvature-from-the-gap-law`

### Product of bends and sweep of normals · working

$$
K = \kappa_1\kappa_2 = \frac{d\Omega}{dA}
$$

The product of the principal curvatures is the signed solid angle swept by the unit normals per unit area.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa_1, \kappa_2$ | principal curvatures, signed relative to one normal | kappa one and kappa two |
| $d\Omega$ | signed solid angle of the normals | d omega |
| $dA$ | area element | d A |

**Holds when:** Smooth surface in three-dimensional Euclidean space; $d\Omega < 0$ where the normals trace their patch in reverse.  
**Say it:** “K is kappa one times kappa two, the normals' solid angle per unit area.”  
**Justified by:** `intrinsic-versus-extrinsic-curvature`

### Riemann tensor of a surface · formal

$$
R_{\mu\nu\rho\sigma} = K\,(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}), \qquad R_{\mu\nu} = K g_{\mu\nu}, \qquad R = 2K
$$

On a surface, $K$ fixes the Riemann tensor, the Ricci tensor and the Ricci scalar.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu\rho\sigma}$ | Riemann tensor in the course conventions | R mu nu rho sigma |
| $g_{\mu\nu}$ | the metric | g mu nu |
| $R$ | Ricci scalar | R |

**Holds when:** Any two-dimensional metric with its Levi-Civita connection.  
**Say it:** “The Riemann tensor is K times a fixed combination of metrics; the Ricci tensor is K g, and the Ricci scalar is two K.”  
**Justified by:** `derivations/riemann-of-a-surface`

## Derivations

### The curvature from the gap law · working

**Goal:** Show that $ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2$ has Gaussian curvature $K = -\partial_\rho^2 f/f$.

1. The metric has $g_{\rho\rho} = 1$ and $g_{\rho\phi} = 0$, so $\Gamma^\rho{}_{\rho\rho} = \tfrac12\partial_\rho g_{\rho\rho} = 0$ and $\Gamma^\phi{}_{\rho\rho} = \tfrac12 g^{\phi\phi}(2\partial_\rho g_{\phi\rho} - \partial_\phi g_{\rho\rho}) = 0$.
2. So the curve $(\rho, \phi_0)$ solves the geodesic equation with $\rho$ as arc length: every curve of constant $\phi$ is a unit-speed geodesic.
3. The curve of constant $\rho$ crosses these geodesics at right angles, and along it the neighbouring geodesic $\phi_0 + \delta\phi$ lies at distance $D(\rho) = f(\rho,\phi_0)\,\delta\phi$, to first order in $\delta\phi$.
4. The gap law $\partial_\rho^2 D = -KD$ holds to first order in the gap for neighbouring geodesics whose gap is measured at right angles to them, taken on trust here in that generality.
5. With $\delta\phi$ fixed, $\partial_\rho^2 D = \partial_\rho^2 f\,\delta\phi$. Divide by $D = f\,\delta\phi$ and let $\delta\phi \to 0$: $K = -\partial_\rho^2 f/f$.

**Result:** $K = -\partial_\rho^2 f/f$, exact wherever the coordinates are defined and $f > 0$.

### The Riemann tensor of a surface · formal

**Goal:** Show that on any surface $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ and $R = 2K$.

1. For the Levi-Civita connection, $R_{\mu\nu\rho\sigma}$ is antisymmetric in $\mu\nu$ and in $\rho\sigma$.
2. In two dimensions an antisymmetric pair is nonzero only as $12$ or $21$, with opposite signs, so every component is $0$ or $\pm R_{1212}$.
3. $T_{\mu\nu\rho\sigma} = g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho}$ has the same antisymmetries, and $T_{1212} = g_{11}g_{22} - g_{12}^2 = \det g \neq 0$. So $R_{\mu\nu\rho\sigma} = (R_{1212}/\det g)\,T_{\mu\nu\rho\sigma}$.
4. Contracting $T_{\mu\nu\rho\sigma}$ with $X^\mu Y^\nu X^\rho Y^\sigma$ gives $g(X,X)g(Y,Y) - g(X,Y)^2$, so the sectional-curvature definition identifies $R_{1212}/\det g$ as $K$.
5. The course Ricci tensor is $R_{\nu\sigma} = g^{\mu\rho}R_{\mu\nu\rho\sigma} = K(2g_{\nu\sigma} - g_{\nu\sigma}) = Kg_{\nu\sigma}$, so $R = g^{\nu\sigma}R_{\nu\sigma} = 2K$.
6. Check on a sphere of radius $a$: $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$ and $\det g = a^4\sin^2\theta$ give $K = 1/a^2$ and $R = +2/a^2$, as the course conventions require.

**Result:** $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$, $R_{\mu\nu} = Kg_{\mu\nu}$, and $R = 2K$.

## Worked examples

### A soap film between two rings · working

**Problem:** A soap film between two coaxial rings forms a catenoid with waist radius $c$. A profile curve of the film, at distance $\rho$ from the waist measured along the film, lies $\sqrt{c^2 + \rho^2}$ from the axis. Find $K$ along the film, its value at the waist for $c = 2$ cm, and the total curvature of the complete catenoid.

1. The profile curves are unit-speed geodesics crossing the circles around the axis at right angles, so $ds^2 = d\rho^2 + (c^2 + \rho^2)\,d\phi^2$ and $f = \sqrt{c^2 + \rho^2}$.
2. $\partial_\rho f = \rho/\sqrt{c^2 + \rho^2}$ and $\partial_\rho^2 f = c^2/(c^2 + \rho^2)^{3/2}$.
3. $K = -\partial_\rho^2 f/f = -c^2/(c^2 + \rho^2)^2$, negative everywhere, as equal and opposite bends require.
4. At the waist, $\rho = 0$, so $K = -1/c^2 = -0.25$ cm$^{-2}$ for $c = 2$ cm.
5. With $dA = f\,d\rho\,d\phi$, $\iint K\,dA = -2\pi c^2\int_{-\infty}^{\infty}(c^2 + \rho^2)^{-3/2}\,d\rho = -2\pi\big[\rho/\sqrt{c^2 + \rho^2}\big]_{-\infty}^{\infty} = -4\pi$.

**Answer:** $K = -c^2/(c^2 + \rho^2)^2$; $-0.25$ cm$^{-2}$ at the waist for $c = 2$ cm; total curvature $-4\pi$.

**Takeaway:** An infinite soap film has a finite total curvature, $-4\pi$: its normals cover every direction except the two along the axis once, in the reverse sense.

## Problems

### `swim-ring-two-spots` · entry · difficulty 1 · calculation

A swim ring has a tube 10 centimetres in radius, bent around a hole 30 centimetres across. Take a spot on the circle of its surface that runs closest to the hole. Around the tube, the surface there bends with a best-fit radius of 10 centimetres, toward the air sealed inside the tube. Around the hole, it bends with a best-fit radius of 15 centimetres, toward the hole. These are the sharpest bends toward each face. Now take a spot on the circle farthest from the hole. There the sharpest and the gentlest bends have radii of 10 and 35 centimetres, both toward the air inside the tube. Find the Gaussian curvature at each spot. Which spot curves more strongly, ignoring the sign?

**Hints**

1. At each spot, do the two bends go toward the same face?
2. The hole lies outside the tube, so bending toward the hole means bending toward the tube's outer face.

**Answer:** Outer spot: 1 divided by 350, about 0.0029 per square centimetre. Inner spot: minus 1 divided by 150, about minus 0.0067 per square centimetre. The inner spot curves about 2.3 times as strongly.

**Must contain:** Outer spot plus 1 divided by 350, inner spot minus 1 divided by 150, per square centimetre; The inner spot curves about 2.3 times as strongly

**Numeric:** Gaussian curvature at the inner spot = -66.67 m^-2 (signed, ±3%); how many times more strongly the inner spot curves = 2.333 1 (magnitude, ±2%)

**Solution**

1. At the outer spot, both bends go toward the air inside the tube, the same face, so the number is positive.
2. 10 times 35 is 350, so the Gaussian curvature there is 1 divided by 350, about 0.0029 per square centimetre.
3. At the inner spot, the bend around the tube goes toward the air inside, and the bend around the hole goes toward the hole, outside the tube. These are opposite faces, so the number gets a minus sign. 10 times 15 is 150, which gives minus 1 divided by 150.
4. Ignoring signs, 1 divided by 150 is bigger than 1 divided by 350 by 350 divided by 150, about 2.3 times.

### `gauss-map-pulls-back-area` · formal · difficulty 2 · proof

Let $\Sigma \subset \mathbb R^3$ be an oriented smooth surface with unit normal $\hat{\mathbf n}$ and shape operator $S$, defined by $d\hat{\mathbf n}(X) = -SX$. Show that the Gauss map $\hat{\mathbf n}: \Sigma \to S^2$ satisfies $\hat{\mathbf n}^*\omega_{S^2} = K\,dA$, and that $K$ does not depend on the choice of normal. Check the sign on the saddle $z = (x^2 - y^2)/2$ at the origin.

**Hints**

1. At $p$, the planes $T_p\Sigma$ and $T_{\hat{\mathbf n}(p)}S^2$ are both orthogonal to $\hat{\mathbf n}(p)$.

**Answer:** $\hat{\mathbf n}^*\omega_{S^2} = \det(-S)\,dA = \det S\,dA = K\,dA$. Replacing $\hat{\mathbf n}$ by $-\hat{\mathbf n}$ replaces $S$ by $-S$, and $\det(-S) = \det S$ for $2\times2$ matrices. On the saddle, $S = \mathrm{diag}(1, -1)$ at the origin, so the Gauss map reverses orientation and $K = -1$.

**Must contain:** The pull-back is the determinant of minus S, which equals the determinant of S, which is K; A two by two determinant is unchanged when S changes sign

**Solution**

1. At $p$, $\hat{\mathbf n}(p)$ is orthogonal to both $T_p\Sigma$ and $T_{\hat{\mathbf n}(p)}S^2$, so the two planes coincide, and orienting both by $\hat{\mathbf n}(p)$ gives them the same orientation.
2. For an oriented orthonormal basis $e_1, e_2$ of $T_p\Sigma$, $(\hat{\mathbf n}^*\omega_{S^2})(e_1, e_2) = \omega_{S^2}(d\hat{\mathbf n}\,e_1, d\hat{\mathbf n}\,e_2) = \det(d\hat{\mathbf n})$.
3. $d\hat{\mathbf n} = -S$, and $\det(-S) = (-1)^2\det S = \det S$.
4. The Gauss equation in $\mathbb R^3$ gives $\det S = K$, so $\hat{\mathbf n}^*\omega_{S^2} = K\,dA$.
5. Replacing $\hat{\mathbf n}$ by $-\hat{\mathbf n}$ turns $S$ into $-S$, which leaves $\det S$ unchanged, and flips both orientations, so the identity survives.
6. On the saddle, $\hat{\mathbf n} = (-x, y, 1)$ to first order at the origin, so $d\hat{\mathbf n}(\partial_x) = -\partial_x$ and $d\hat{\mathbf n}(\partial_y) = \partial_y$. Then $S = \mathrm{diag}(1, -1)$, $\det(d\hat{\mathbf n}) = -1$, and $K = -1$.

## Observations

- **Earth's Gaussian curvature from geodetic surveys, as summarized by the GRS80 ellipsoid** (measured, working). Surveys that compare plumb-line directions, measured against the stars, with distances along the ground give the principal radii $M$ and $N$, and $K = 1/MN$. *Numbers:* GRS80: $K = 2.475\times10^{-14}$ m$^{-2}$ at the equator, matching radius $6356.8$ km, and $2.442\times10^{-14}$ m$^{-2}$ at the poles, matching radius $6399.6$ km, a difference of $1.35\%$. *Reference:* Helmut Moritz (1980), *Geodetic Reference System 1980*, Bulletin Géodésique 54, 395–405, doi:10.1007/BF02521480

## Teaching arc

1. **Give each spot a number** (entry). Run the ring test at the egg's tip and widest part, then name each spot's matching ball. *Why:* It turns the insider's ring test into one number with units. *Predict:* On the egg, will the ant's small ring fall short by more at the tip or at the widest part? *Visual:* [[paced-ring-on-a-ball-and-a-plain]] *Uses:* `ways_in/a-matching-ball-for-each-spot`, `checks/marble-and-football`
2. **Let an outsider agree** (entry). Multiply the egg's two bends, then test the rule on a soap film's waist. *Why:* Bends and rings agreeing is what makes the number worth having. *Predict:* Will multiplying the two bends at the egg's widest part give the ant's number? *Visual:* [[card-touching-a-curved-patch]] *Uses:* `ways_in/multiply-the-two-bends`, `checks/soap-film-waist`
3. **Read it from the metric and from plumb lines** (working). Derive the spacing formula, apply it to the swim ring, then read Earth's value from plumb lines. *Why:* One number arises from lengths alone and from normals. *Predict:* Are Earth's flattened poles more or less strongly curved than its equator? *Uses:* `ways_in/the-number-from-the-distance-rule`, `derivations/curvature-from-the-gap-law`, `ways_in/plumb-lines-sweep-the-sky`, `observations/earth-curvature-from-surveys`

## Misconceptions

### “A ball eleven times as wide curves eleven times more gently.” · entry · `wider-ball-linearly-gentler`

- **Why it is tempting:** A circle eleven times as wide bends eleven times more gently.
- **What is true:** The Gaussian curvature divides 1 by the radius times itself, so it becomes one hundred and twenty-one times smaller. A short ring's missing fraction shrinks by the same factor.
- **Exposed by:** `checks/marble-and-football`

### “Equal bends toward opposite faces cancel, so the Gaussian curvature there is zero.” · entry · `equal-opposite-bends-cancel`

- **Why it is tempting:** A bend one way plus an equal bend the other way seems to add up to nothing.
- **What is true:** The bends are multiplied, not added, so they give a negative number. Small rings there come out too long.
- **Exposed by:** `checks/soap-film-waist`

### “Enlarging a surface three times divides its Gaussian curvature by three.” · working · `k-scales-like-a-curve`

- **Why it is tempting:** The curvature of a curve scales that way.
- **What is true:** Gaussian curvature has units of inverse length squared, so it is divided by nine.
- **Exposed by:** `checks/scale-a-surface-up`

### “Two surfaces with the same Gaussian curvature at corresponding points are locally isometric.” · formal · `k-fixes-the-surface`

- **Why it is tempting:** In two dimensions the Gaussian curvature fixes the whole Riemann tensor.
- **What is true:** That holds when the curvature is constant, but a varying curvature is only one invariant, and its derivatives can still differ.
- **Exposed by:** `checks/same-curvature-different-surfaces`

### “Denting a ball changes the total of its Gaussian curvature.” · formal · `denting-changes-total`

- **Why it is tempting:** The dent adds saddle-shaped points with negative curvature.
- **What is true:** The negative curvature around the dent is balanced exactly by changes elsewhere, because the total over any closed surface shaped like a sphere is four pi.
- **Exposed by:** `checks/dented-ball-total`

## Checks

1. **Entry · numeric** `checks/marble-and-football`. A marble has a radius of 1 centimetre, and a football has a radius of 11 centimetres. On a ball, every spot's matching ball is that same ball, because its own rings have exactly its own missing fraction. What is the Gaussian curvature of each ball, and how many times bigger is the marble's? A friend guesses 11 times.
   - **Hints:** What is 11 times 11?
   - **Answer:** The marble's Gaussian curvature is 1 divided by 1 times 1, so 1 per square centimetre. The football's is 1 divided by 11 times 11, which is 1 divided by 121, about 0.0083 per square centimetre. So the marble's is 121 times bigger, not 11 times, because the radius is multiplied by itself. A ring drawn 1 millimetre from its centre has a missing fraction about 121 times bigger on the marble.
   - **Must contain:** Marble: 1 per square centimetre; Football: 1 divided by 121 per square centimetre; 121 times, because the radius is multiplied by itself
   - **Numeric:** how many times bigger the marble's Gaussian curvature is = 121 1 (magnitude, ±3%)
   - **Targets:** `wider-ball-linearly-gentler`
   - **Visual:** [[paced-ring-on-a-ball-and-a-plain]]
2. **Entry · evaluate-claim** `checks/soap-film-waist`. A soap film stretched between two parallel wire rings narrows to a waist. Its two faces are the one looking toward the middle line, which joins the rings' centres, and the one looking away. At a spot on the waist, the path around the waist bends toward the middle line, with a best-fit circle of radius 2 centimetres. The path running from ring to ring bends away from the middle line, also with radius 2 centimetres. These are the sharpest bends toward each face. A friend says: "The bends are equal and opposite, so they cancel, and the Gaussian curvature there is zero." Is the friend right?
   - **Hints:** Are the bends added or multiplied?
   - **Answer:** No. The path around the waist bends toward the face looking toward the middle line, and the path from ring to ring bends toward the face looking away. So the bends go toward opposite faces, and the rule uses the sharpest bend toward each face and gives a minus sign. The bends are multiplied, not added. 2 times 2 is 4, so the Gaussian curvature is minus 1 quarter per square centimetre. That is as strong as on a ball of radius 2 centimetres, but negative. So an ant's small rings on the waist come out too long, not as on flat paper.
   - **Must contain:** No: the Gaussian curvature is minus one quarter per square centimetre; Bends toward opposite faces are multiplied and give a minus sign
   - **Numeric:** Gaussian curvature at the waist = -2500 m^-2 (signed, ±3%)
   - **Targets:** `equal-opposite-bends-cancel`
   - **Visual:** [[card-touching-a-curved-patch]]
3. **Working · evaluate-claim** `checks/scale-a-surface-up`. A surface is enlarged so that every length along it is multiplied by 3. A student says that its Gaussian curvature at corresponding points is divided by 3, like the curvature of a curve. Evaluate the claim using the spacing formula of the distance rule.
   - **Hints:** How do $\rho$ and $f$ change when every length triples?
   - **Answer:** The claim is wrong. The enlarged surface has $ds'^2 = 9\,ds^2 = d\rho'^2 + f'^2\,d\phi^2$ with $\rho' = 3\rho$ and $f' = 3f$. Then $\partial_{\rho'}^2 f' = \tfrac13\,\partial_\rho^2 f$, so $K' = -\partial_{\rho'}^2 f'/f' = K/9$. Gaussian curvature has units of inverse length squared, while the curvature of a curve has units of inverse length.
   - **Must contain:** Both rho and f are multiplied by three; K is divided by nine, since it has units of inverse length squared
   - **Numeric:** factor multiplying the Gaussian curvature = 0.1111 1 (magnitude, ±2%)
   - **Targets:** `k-scales-like-a-curve`
4. **Formal · explain** `checks/same-curvature-different-surfaces`. The helicoid $(u\cos v, u\sin v, v)$ and the surface of revolution $(u\cos v, u\sin v, \ln u)$, with $u > 0$, both have $K = -1/(1 + u^2)^2$ at the point with coordinates $(u, v)$. Is the map $(u, v) \mapsto (u, v)$ an isometry? Are the surfaces locally isometric anywhere?
   - **Hints:** Which quantities built from $K$ must an isometry preserve?
   - **Answer:** No and no. The helicoid has $ds^2 = du^2 + (1 + u^2)\,dv^2$, and the other surface $ds^2 = (1 + 1/u^2)\,du^2 + u^2\,dv^2$, so the map is not an isometry. A local isometry must preserve both $K$ and $|\nabla K|^2$. With $\partial_u K = 4u/(1 + u^2)^3$, the helicoid has $|\nabla K|^2 = 16u^2/(1 + u^2)^6$ and the other surface $16u^4/(1 + u^2)^7$. In terms of $w = 1 + u^2 = (-K)^{-1/2}$ these are $16(w - 1)/w^6$ and $16(w - 1)^2/w^7$, which differ for every $w > 1$. So points with equal $K$ always have different $|\nabla K|^2$, and no open sets are isometric. Equal constant $K$ would have sufficed, by Minding's theorem.
   - **Must contain:** The metrics differ, so the identity map is not an isometry; The length of the gradient of K, as a function of K, differs, so no local isometry exists
   - **Targets:** `k-fixes-the-surface`
5. **Formal · numeric** `checks/dented-ball-total`. A rubber ball is pressed in to form a smooth dent, surrounded by a band of saddle-shaped points. What is the total of its Gaussian curvature over the whole surface, before and after? For the swim ring of the distance rule, with a tube of radius 10 cm around a centre circle of radius 25 cm, find the total over its outer half, the half farther from the hole, and over the whole ring.
   - **Hints:** Does a dent change the Euler characteristic?
   - **Answer:** Before and after, $4\pi$. The dented ball is still a compact oriented surface with $\chi = 2$, so Gauss–Bonnet fixes $\iint K\,dA = 2\pi\chi$, and the negative curvature around the dent is balanced by changes elsewhere. On the swim ring $K\,dA = \cos\theta\,d\theta\,d\phi$, so the outer half gives $2\pi\int_{-\pi/2}^{\pi/2}\cos\theta\,d\theta = 4\pi$, the inner half $-4\pi$, and the whole ring $0 = 2\pi\chi$ for a torus.
   - **Must contain:** Four pi before and after denting, fixed by the Euler characteristic; The swim ring's halves give plus and minus four pi, and zero in total
   - **Numeric:** total curvature of the dented ball = 12.566 1 (signed, ±1%); total curvature of the swim ring's outer half = 12.566 1 (signed, ±1%); total curvature of the whole swim ring = 0 1 (signed, ±0.01)
   - **Targets:** `denting-changes-total`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| The letter K names several quantities | Here $K$ is always the Gaussian curvature. | Some texts write $K$ for the Kretschmann scalar or for the trace of a slice's extrinsic curvature, and $k$ or $K$ for the cosmological curvature constant. |
| Sign of the Ricci scalar of a surface | With the course Riemann tensor, $R = 2K$, so a sphere of radius $a$ has $R = +2/a^2$. | Texts with the opposite overall sign of the Riemann or Ricci tensor write $R = -2K$ for a surface. |

## Visuals

- [[paced-ring-on-a-ball-and-a-plain]] (core): Matching balls for spots of an egg. *Sketch:* Adds an egg mode: a short ring at a chosen spot, the ball whose ring falls short by the same fraction, and that ball's radius and Gaussian curvature.
- [[card-touching-a-curved-patch]] (core): Two bends multiplied give the ring test's number. *Sketch:* Adds a product readout: one over the two best-fit radii multiplied, signed by faces, beside the ring-test value, on an egg, a can, a crisp and a soap-film waist.

## Tutor moves

**Open with**

- Picture a smooth plastic egg. An ant on its shell draws a small ring at one tip and another on the widest part, each the same short distance from its centre. Compared with a ring on flat paper, which ring do you think comes out shorter? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why the radius is multiplied by itself.* → Compare a ring drawn 2 centimetres from its centre on a football and on a ball twice as wide: its missing fraction drops to a quarter. *Uses:* `ways_in/a-matching-ball-for-each-spot`

**Common questions**

- *What does this number have to do with gravity?* (entry) Space has more directions than a surface. Through a point in space, picture the directions along one page of a book, then along another page fanned out from the same spine. Walk straight out from the point along one page's directions, and you trace a surface. Its Gaussian curvature at the point measures the curving for that page. General relativity describes gravity as a curving of space and time, and it keeps a whole table of such numbers at every place. Near the Sun, starlight bends twice as much as it would if space there were not curved. *Uses:* `ways_in/a-matching-ball-for-each-spot`, `ways_in/one-number-is-the-whole-curvature`

**Switching levels**

- To working when: asks for a formula; mentions line elements or metrics. Go to the spacing formula and the scaling check. *Uses:* `ways_in/the-number-from-the-distance-rule`, `checks/scale-a-surface-up`
- To formal when: knows the Riemann tensor; asks why one number is enough. Derive the one-component form, then the Gauss–Bonnet totals. *Uses:* `derivations/riemann-of-a-surface`, `checks/dented-ball-total`

**Pronunciations:** Gauss → GOWSS; Gauss–Bonnet → GOWSS bon-AY; Minding → MIN-ding; catenoid → KAT-uh-noyd; helicoid → HEL-ih-koyd; Schur → SHOOR; Riemann → REE-mahn

## History

- **Carl Friedrich Gauss (1827).** Measured a surface's curvature by the area its normals sweep, and proved that this number is fixed by lengths along the surface. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Ferdinand Minding (1839).** Showed that surfaces with equal constant Gaussian curvature are locally isometric.

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** An egg is more curved at its tip than at its side, and an ant can tell by walking out a little way and measuring small rings, which come out shorter than 6.28 times the distance. She finds a ball whose rings fall short the same way and takes 1 over its radius times itself, though I read that as 1 over the radius, times the radius again, which is just 1. I don't know what 'falls short by a fraction' means exactly, and I don't see how the matching ball at the side can be 3 centimetres when the egg is only 4 across. Bigger balls get smaller numbers, by the square. From outside you multiply two bend radii, but I wasn't sure which two lines count, or which lines at all, and 'the rule' came up at the tip before I knew it. Saddles get a minus sign, a rolled poster gives zero, and Gauss proved the two ways agree. Earth's number is tiny. At the end I thought astronomers had found that space isn't curved. Compared with the takeaways: the second takeaway came through; the first came through except the order of operations and why rings can come out too long.

Second entry-persona pass, 2026-09-13, reading revision 5 cold and before any of this pass's fixes: A surface has one number at every spot. An ant on a plastic egg walks 2 millimetres out in every direction and the ring she gets comes out short. She divides the missing length by 6.28 times 2 millimetres, which is the missing fraction: about 0.38 per cent at the tip and 0.07 per cent at the fat part, so the tip curves more strongly. Then she hunts for a ball whose ring at the same 2 millimetres misses by the same fraction: radius 1 and a third centimetres at the tip, 3 centimetres at the fat part. The number is 1 divided by the radius times the radius, so 9 sixteenths and 1 ninth per square centimetre. Multiplying the radius by itself is right because a ball twice as wide misses a quarter as much. Earth's number is 1 over about 40.6 million square kilometres, and a ring walked 1 kilometre out is short by less than half a hair, so nobody notices. From outside you take the sharpest and the gentlest bend through the spot, multiply their radii and divide 1 by that; on the egg's fat part 2 times 4.5 is 9, the same 9 as 3 times 3. A rolled poster gives zero, because one path along it does not bend at all. On a crisp some paths bend toward one face and some toward the other, and then you take the sharpest bend toward each face and put a minus sign. Gauss proved the insider's and the outsider's numbers always agree. Places I stopped: 'the end marks' when nobody had told me to mark anything; 'rings of one short length'; 'its rings miss less than on a ball 4 centimetres wide', where I could not tell whose rings; the crisp sentence about a ring that cannot be laid on flat paper; 'every path curls', because curling sounded like a different thing from bending; and 'the product', because the rule had called it the result. I could not say the second takeaway back at all: 'or on a saddle of the sharpest bend toward each face' has words missing from it. The word list's entry for missing fraction names 6.28 times the distance twice in one sentence and I still could not tell whether I divide once or twice. Against the takeaways: the first came back whole; the second did not come back as a sentence.

**Stumbles (26)**

- “One number for how strongly, and which way, a surface curves at each spot”: 'Which way' reads as a direction, toward one side or the other, but the number does not depend on which side you look from; its sign says ball-like or saddle-like.
- “A ball of radius 10 centimetres gets one hundredth per square centimetre”: The unit 'per square centimetre' is unexplained in the summary, and the sentence pushes the summary past three sentences once the sign is stated plainly.
- “walk straight out the same distance from a centre in every direction ... Walking straight means never steering left or right.”: The recap uses 'walk straight' one sentence before defining it.
- “The ring at the tip falls short by a bigger fraction”: 'Falls short by a fraction' is never defined: a fraction of what? The reader cannot tell whether it compares lengths or something else.
- “about five times bigger”: A surprising count with no numbers the reader can check.
- “She looks for the ball whose ring, drawn 2 millimetres from its centre, falls short by the same fraction.”: A step on trust: the reader has not yet seen that smaller balls miss more, so it is unclear that one missing fraction picks out one ball. The football numbers that show it come three paragraphs later.
- “At the widest part, its radius is 3 centimetres.”: First what-if: the egg is only 4 centimetres wide there, so how can the matching ball be wider than the egg?
- “Now take 1 divided by the matching ball's radius times itself.”: Reread: it can be parsed as (1 divided by the radius) times the radius, which is always 1.
- “about 0.11 per square centimetre”: The unit 'per square centimetre' appears with no reason.
- “At the tip it is 9 sixteenths”: Skipped arithmetic: the reader cannot get 9 sixteenths from 1 and a third centimetres.
- “Where small rings come out exactly 6.28 times the distance”: 'Exactly' clashes with 'about 6.28' in the recap, since 6.28 is rounded.
- “Where they come out too long by some fraction, its size comes from the ball whose rings fall short by that fraction, and it gets a minus sign.”: A surprise with no example or reason: the reader has never met a ring that comes out too long.
- “A ring paced out 1 kilometre from its centre falls short by only about 0.026 millimetres.”: 'Paced out' is a second word for 'walked', and 0.026 millimetres has no everyday comparison.
- “Keep the thread tight along the ball and draw a ring. Lay the thread along the ring to measure it: about 11.9 centimetres, some 7 millimetres short of 12.6.”: The recap's ring test walks straight, but the try-it uses a thread without linking the two, and 12.6 appears with no source. The basketball's 'about half a millimetre' is low: a 75-centimetre ball gives 0.59 millimetres.
- “picture short lines drawn on the shell in every direction, like the spokes of a wheel. Each line bends”: Which lines? A line drawn on a shell can wiggle as much as you like, so its bend says nothing about the shell.
- “This is the sharpest bend through the spot. Along the egg, from tip to tip, the line bends most gently.”: Taken on trust: nothing says why these two paths, and not others, are the extremes.
- “so the rule gives 9 sixteenths again”: 'The rule' is used before the rule is stated, in the next paragraph.
- “Then 1 divided by 9 is the Gaussian curvature that the ant found at that spot with rings, where the matching ball had radius 3.”: Implicit step: the reader must work out that 3 times 3 is also 9 to see the agreement.
- “This agreement is surprising, because bending a sheet without stretching changes its bends but never its rings.”: Reread: the link between 'bends change, rings don't' and 'surprising' is left to the reader.
- “the line around the waist bends toward the line joining the rings' centres ... The line running from ring to ring bends away from that line”: The entry rule is stated in faces, but the check never names the film's faces, so the reader cannot apply it; nor is the reader told these are the sharpest bends toward each face, which the rule needs.
- “Around the hole it bends with a best-fit radius of 15 centimetres, toward the hole.”: The rule needs the sharpest bends and the faces; the problem gives neither, and 'toward the hole' is not obviously a face of the tube's skin.
- “Each ball is its own matching ball at every spot. ... how many times stronger is the marble's?”: A claim with no reason, and 'stronger' is a new word beside 'curves more strongly' and 'bigger'.
- “so it falls one hundred and twenty-one times”: Spoken, 'falls 121 times' can mean it drops by 121 or happens 121 times.
- “Through a point in space, every flat slice has its own curving.”: 'Flat' is used for a slice of a curved space, so the sentence seems to contradict itself; the reader cannot picture the slices.
- “Astronomers have tested the curving of space across the observable universe, and so far none has been detected.”: False first what-if: a teenager concludes that space is not curved at all, just after hearing that gravity is curving. The null result is about the average over the whole universe, not space near masses.
- “which ring do you think falls short by more?”: 'By more' can mean more length or a bigger fraction, and the fraction has not been introduced when the tutor opens.

**Fixes**

- Tagline and summary: the sign is described as ball-like or saddle-like instead of 'which way'; the unexplained ball number left the summary, which stays at three sentences.
- Matching-ball way: introduced 'missing fraction' as a named term (the term the circumference-to-radius-test note uses) and used it in every entry field, the tutor moves and the working way; gave the tip and side missing fractions (0.375 and 0.074 per cent, ratio 5.06, from K rho squared over 6 with rho = 0.2 cm, checked in python3); moved the football comparison (0.536 and 0.134 per cent, ratio 0.250, exact sine formula) ahead of the matching ball; explained why the side's matching ball is wider than the egg; stated the order of operations; explained the unit; wrote out 4 thirds squared; gave the potato crisp as a place where rings come out too long; added the hair comparison.
- Try-it: linked the tight thread to never steering, sourced 12.6, and corrected the basketball shortfall to 'just over half a millimetre' (0.59 mm for a 75-centimetre ball; rubber ball ring 11.89 cm, short by 0.67 cm, rechecked).
- Two-bends way: lines are now the paths of ants walking straight, which is what makes their bends the surface's bends; the rule is stated before it is used; the paths between the extremes are said to bend with radii between 2 and 4.5 cm (Euler's theorem on the spheroid); the 3 times 3 step is explicit; the saddle case and the poster case each have their own paragraph; the surprise of Gauss's result is spelled out.
- Checks and problem: the soap-film check names the film's faces and says the bends given are the sharpest toward each face; the swim-ring problem says which bends are sharpest and gentlest and gains a second hint about which face the hole is on; the marble check gives the reason each ball is its own matching ball and says 'bigger' instead of 'stronger'. Answers and numeric values are unchanged.
- Glossary: added 'missing fraction'; rewrote the Gaussian curvature and matching ball definitions with the explicit order of operations.
- Entry common question on gravity: replaced the self-contradictory 'flat slice' with the fanned pages of a book, and replaced the misleading cosmological null result with the factor of two in starlight bending near the Sun.
- Ladder: the distance-rule way now calls geodesics 'the paths of straight walks', uses 'missing fraction' for K rho squared over 6, and replaces the undefined g with the line element's coefficients; the plumb-line way now bridges from the sharpest and gentlest bends to principal curvatures and principal directions, signed relative to the chosen normal, before using kappa one and kappa two. First sentences of all non-entry ways already name the ways they continue; the five ways are genuinely different routes (rings, bends, line element, normals, structure).
- Budget: entry-way explanations rose from 754 to about 1,030 words, inside the 10 per cent review allowance over the 1,000 cap, used only for the recorded stumble fixes; nothing dropped.
- Bumped the revision to 2.

**Concerns**

- For the physics reviewer: confirm the new entry claims 'every other path through the spot bends with a radius between 2 and 4.5 centimetres' (normal curvatures of the spheroid at its equator), the crisp's wavy edge as a hint for rings that come out too long, and 'starlight bends twice as much as it would if space there were not curved' in the entry common question.
- The entry claim that the matching ball for a too-long ring gives the size of a negative Gaussian curvature holds to leading order for short rings, as the writer reported; the prose now says 'small rings' but does not state the limit.
- Rule 17: the two-bends way carries the egg, the tip, the saddle sign rule and the poster. The saddle rule is part of the same outsider's rule, so it stayed, but it is the densest entry way; a later edit could give 'bends toward opposite faces' its own short entry way if learners stumble.
- Assessment gaps the writer noted remain: no entry check exercises a ring that comes out too long or the Earth number, and the working plumb-line way and the formal one-component form have no check.
- Vocabulary across notes: this note and intrinsic-versus-extrinsic-curvature say 'best-fit circle', while the prerequisite curvature-of-a-curve teaches 'osculating circle' and 'radius of curvature' at entry. An editor should pick one term for the vault.
- Entry-way explanations now sit at about 1,030 of the 1,000-word cap; further entry additions need cuts elsewhere.
- This was a second entry-persona pass over a note that both stages had already signed at revision 5. The eight fixes are wording only, so the loop needs just a physics diff check over the six entry strings note_diff.py lists, and then an editor can publish.
- Vocabulary across notes, still open from the first pass and confirmed by a fresh read of the prerequisites: this note glosses 'best-fit circle', while curvature-of-a-curve names the same circle 'osculating circle' at entry and gives it a say_as. A reader arriving in sequence meets two names for one idea. The fix is a vault-wide editorial choice, so I left both notes alone.
- Rule 17, agreeing with the first pass after an independent read: multiply-the-two-bends carries the product rule, the sharpest-and-gentlest claim, the saddle sign rule, the rolled poster and Gauss's result. They are all cases of its one rule, so I did not split it, but it is the note's densest entry way and the first place to watch if learners stall.
- The takeaway of a-matching-ball-for-each-spot opens with a rule that holds only where rings come out short; its second sentence supplies the zero and negative cases. A learner who quotes the first sentence alone has a rule that fails on a saddle and at a cone's point, which only the summary's 'smooth surface' scopes away.
- Entry-way explanations now stand at 1,090 words against the cap of 1,000, with ten words of the review allowance left. Any further entry addition needs a cut first; the cheapest is the scene-setting sentence 'Balls give a scale to compare with', whose work the football numbers already do.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 3 changed passages

- “a ring with extra length cannot lie flat, so it ripples up and down”: Rule 5: 'flat' describes surfaces everywhere else in the note ('as on flat paper'), but 'lie flat' uses it for a position. 'Up and down' is also a direction with no reference on a crisp.
- “There, the ant finds the ball whose missing fraction equals the fraction by which her ring is too long.”: Rule 11: after the split, the sentence just before is about the crisp's wavy edge, so 'There' now reads as the edge rather than the middle of the crisp where her rings come out too long.
- “Gauss proved in 1827 that the outsider's number depends only on lengths along the surface. So it agrees with the ant's number at every spot of every smooth surface in ordinary space.”: Rule 3: the 'So' is a step taken on trust. Depending only on lengths does not by itself make two numbers equal, so a careful reader asks how the second sentence follows. What does follow is the answer to the poster puzzle just before: rolling cannot break the agreement.
- Fix: a-matching-ball-for-each-spot: 'cannot lie flat, so it ripples up and down' now reads 'cannot be laid on flat paper, so it ripples'. The claim is unchanged.
- Fix: a-matching-ball-for-each-spot: 'There,' now reads 'Near the crisp's middle,' so the place stays unmistakable after the split.
- Fix: multiply-the-two-bends: the Gauss sentence now says the outsider's number depends only on lengths 'just as the ant's rings do', and the 'So' now leads to what follows from that (rolling or any length-keeping change never breaks the agreement). The agreement's scope, every spot of every smooth surface in ordinary space, is restated unchanged in its own sentence. Entry-way explanations grow by about 20 words, inside the 10% review allowance.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 6): 8 stumbles in 3 changed passages

- “walk straight out the same distance from a centre in every direction, then measure the ring through the end marks along the ground”: Rule 3 and rule 11: nobody was told to make marks, so 'the end marks' arrives from nowhere, and 'measure the ring ... along the ground' splits one instruction around a phrase I had to unpick on a second reading.
- “So for rings of one short length, the smaller the ball, the bigger the missing fraction.”: 'Rings of one short length' is not a phrase I have met. I first read it as rings that are one short length long, rather than rings all walked out the same short distance.
- “So its rings miss less than on a ball 4 centimetres wide.”: Rule 11: 'its' could be the shell's, the second ball's or the egg's, and the second 'rings' is left out of the comparison, so I reread the sentence to see that the egg's rings at the widest part are compared with a small ball's rings.
- “The crisp's wavy edge hints why: a ring with extra length cannot be laid on flat paper at the distance walked from its centre, so it ripples.”: 'At the distance walked from its centre' hangs at the end and reads as attached to 'flat paper', and the length the ring has extra over is never named, so the comparison only appears on a second reading.
- “On the egg, every path curls toward the inside face of the shell.”: Rule 5: paths 'bend' everywhere else in the note, thirteen times over, and here one 'curls'. I stopped to ask whether curling was a different thing from bending.
- “The gentler a bend, the bigger its circle, and the closer 1 divided by the product gets to zero.”: Rule 5 and rule 3: 'the product' is a second word for what the rule itself calls 'the result', and what is multiplied is left for me to supply.
- “Multiply the radii of a spot's sharpest and gentlest bends, or on a saddle of the sharpest bend toward each face, and divide 1 by the result. This gives the ant's Gaussian curvature, with a minus sign on a saddle.”: The middle clause has its verb missing, so the takeaway is not a sentence I can say back, and two rules are folded into one instruction. This is the squeezed wording the review guide asks for by name.
- “The length a ring is missing, compared with 6.28 times the distance walked, divided by that 6.28 times the distance.”: One sentence names 6.28 times the distance walked twice, in two different roles, so after three readings I still could not tell whether I divide once or twice.
- Fix: a-matching-ball-for-each-spot recap and the ring-test glossary entry: the walker is now told to mark where each walk ends, and the measuring instruction is its own sentence. The glossary's 'it is about 6.28 times' also became 'that ring is about 6.28 times'.
- Fix: a-matching-ball-for-each-spot explanation: 'rings of one short length' became 'rings walked out the same short distance'; 'its rings miss less than on a ball' became 'the egg's rings there miss less than rings on a ball'; the crisp sentence was split so the length comparison comes first.
- Fix: multiply-the-two-bends explanation: 'curls' became 'bends'; 'the product' became 'the two radii multiplied' and 'that result', with the step made explicit.
- Fix: multiply-the-two-bends takeaway: rewritten as three sentences, the ball rule then the saddle rule, in the explanation's own words. It is 220 characters, inside the 240 cap.
- Fix: Glossary 'missing fraction': rewritten to the one division the explanation actually performs.
- Fix: Nothing was dropped or compressed. Entry-way explanations rose from 1,077 to 1,090 words, inside the 10 per cent review allowance over the foundation cap of 1,000, and used only for these recorded fixes. No number, claim, condition or scope changed; note_diff.py lists six entry strings and no working or formal string.

**Re-read** (2026-09-13, revision 8): 2 stumbles in 2 changed passages

- “A ring longer than 6.28 times the distance from its centre cannot be laid on flat paper and keep that distance, so it ripples.”: Rule 3 and rule 11. 'Keep that distance' asks me to carry 'the distance from its centre' across nine words and then supply, myself, that it is every point of the ring that has to stay that far out. On the first reading I took 'keep that distance' to mean the ring keeps its own length, which is not the point being made. The measurement also loses its reference: the phrase never says distance from what, once the ring has left the crisp and is lying on the paper.
- “cannot be laid on flat paper and keep that distance, so it ripples”: Rule 11. With 'paper' now sitting between the ring and the pronoun, 'it ripples' has two candidates that can both ripple, and I read it once as the paper rippling. The earlier wording had the same 'it', but the added clause pushed the ring further away from it.
- Fix: a-matching-ball-for-each-spot explanation: 'and keep that distance, so it ripples' now reads 'and stay that far from the centre, so the ring ripples'. The condition the physics diff check added is kept word for word in meaning, only named: 'that far from the centre' is the same distance as 'that distance', which is the distance from the ring's centre set one clause earlier. No number, sign, scope or condition changed; the sentence still says only that a ring longer than 6.28 times that distance cannot lie on flat paper at that distance.
- Fix: Nothing was dropped or compressed. Entry-way explanations go from 1,094 to 1,098 words against the foundation cap of 1,000, inside the 10 per cent review allowance and used only for this recorded fix. Two words remain. Any later entry addition needs a cut first, and the cheapest is still 'Balls give a scale to compare with.', whose work the football numbers do.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Conventions: Riemann R^rho_{sigma mu nu}, Ricci R_{mu nu}=R^rho_{mu rho nu}, sectional-curvature sign row, sphere R=+2/a^2, entry/working/formal unit rows.: Read course-conventions.md in full and matched every equation, sign and unit choice in the note against it. → Every choice in the note follows the file; no convention is needed that the file does not make. K is scoped to Gaussian curvature by notation_traps/letter-k, as the 'one symbol, one meaning' practice requires.
- Derivation curvature-from-the-gap-law: Gamma^rho_{rho rho}=0 and Gamma^phi_{rho rho}=0 for ds^2=drho^2+f^2 dphi^2; constant-phi curves are unit-speed geodesics; D=f dphi; D''=-KD gives K=-f''/f.: Re-derived both Christoffel symbols from the conventions formula Gamma^lambda_{mu nu}=1/2 g^{lambda sigma}(d_mu g_{sigma nu}+d_nu g_{sigma mu}-d_sigma g_{mu nu}); checked the geodesic equation term by term; checked that the Jacobi field f dphi d_phi is orthogonal to d_rho so its norm obeys the scalar Jacobi equation. → Every step correct, one move per step. Sign verified against the sphere below: K>0 on a sphere.
- Working examples of the line-element formula: plane f=rho gives 0; cylinder ds^2=dz^2+b^2 dphi^2 gives 0; sphere f=a sin(rho/a) gives 1/a^2 with ring length 2 pi a sin(rho/a)=2 pi rho(1-rho^2/6a^2+...); hyperbolic f=a sinh(rho/a) gives -1/a^2 with the same excess fraction.: Hand differentiation of each f, Taylor expansion of sin and sinh to third order. → All four correct. The missing (or excess) fraction is K rho^2/6 at leading order, which is exactly what makes the entry matching-ball construction well defined.
- Swim ring: ds^2=r^2 dtheta^2+(b+r cos theta)^2 dphi^2, rho=r theta, K=cos theta/[r(b+r cos theta)]; for r=10 cm, b=25 cm, K=+1/350 on the outer circle, 0 on the top circle, -1/150 on the inner circle, with bends of radii 10 cm and 15 cm toward opposite faces.: Applied K=-d_rho^2 f/f to f=b+r cos(rho/r); checked the principal curvatures at both equators against the surface-of-revolution formulas; python3 arithmetic. → Correct. Both equators of a torus are geodesics, so their space curvatures equal the magnitudes of the normal curvatures quoted, and the second principal radius at the inner equator is b-r=15 cm.
- Scaling: multiplying every length by lambda divides K by lambda^2; check scale-a-surface-up answers K/9 for lambda=3, numeric 0.1111.: rho'=3 rho and f'=3f give d_{rho'}^2 f' = (1/3) d_rho^2 f, so K'=-(1/3)f''/(3f)=K/9. → Correct; the numeric value and 2 per cent tolerance are fine. Contrast with the curvature of a curve (inverse length) is right.
- Plumb-line way: the normal tilts by |kappa_1| ds_1 along a principal direction; a patch of area dA sends its normals over |kappa_1 kappa_2| dA of solid angle, signed negative where kappa_1 kappa_2<0; K=kappa_1 kappa_2=dOmega/dA; a cylinder sweeps a curve of directions, so K=0; a connected closed surface in space with K>0 everywhere covers every direction once, giving 4 pi.: Rodrigues' formula dn = -kappa_i e_i ds along a line of curvature; Jacobian of the Gauss map; Hadamard's theorem for the convexity statement. → Correct with the hypotheses as stated (smooth surface in three-dimensional Euclidean space; connected, closed, K>0 everywhere). The sign convention is intrinsic to the chosen normal and the note says so.
- GRS80 numbers: M=6335.4 km and N=6378.1 km at the equator give K=2.475e-14 m^-2 with matching radius 6356.8 km; M=N=6399.6 km at the poles give K=2.442e-14 m^-2; K is 1.35 per cent larger at the equator.: python3 with a=6378137 m and 1/f=298.257222101: M_eq=a(1-e^2)=b^2/a, N_eq=a, pole radius a^2/b; K=1/(MN). → M=6335.4393 km, N=6378.137 km, K_eq=2.47474e-14; pole radius 6399.5936 km, K_pole=2.44172e-14; ratio 1.013524, i.e. 1.35 per cent. Equatorial matching radius sqrt(MN)=a sqrt(1-e^2)=b=6356.752 km, so 6356.8 km is exact. 'The flattened poles curve more gently, although they are closer to Earth's centre' is correct.
- Formal way: sectional-curvature definition; R_{mu nu rho sigma}=K(g_{mu rho}g_{nu sigma}-g_{mu sigma}g_{nu rho}); R_{mu nu}=K g_{mu nu}; R=2K; Einstein tensor vanishes identically in two dimensions.: Counted independent components from the antisymmetries in 2D; contracted with the course Ricci definition R_{mu nu}=R^rho_{mu rho nu}=g^{rho lambda}R_{lambda mu rho nu}; contracted the model tensor with X,Y,X,Y and compared with the sectional-curvature row; computed the sphere directly from the course Riemann tensor (R^theta_{phi theta phi}=sin^2 theta, R_{theta phi theta phi}=a^2 sin^2 theta, det g=a^4 sin^2 theta). → Correct throughout, and K=1/a^2 with R=+2/a^2 for the sphere, as the conventions row requires. G_{mu nu}=K g_{mu nu}-(1/2)(2K)g_{mu nu}=0.
- Conformal change tilde g = e^{2u} g gives tilde K = e^{-2u}(K - Delta_g u), with the half-plane (dx^2+dy^2)/y^2 giving tilde K = -1.: u=-ln y over the flat plane: Delta u = d^2(-ln y)/dy^2 = 1/y^2, e^{-2u}=y^2, so tilde K = y^2 (0 - 1/y^2) = -1. → Correct, and the way defines Delta_g = nabla^mu nabla_mu explicitly, so the sign is unambiguous without a new conventions row.
- Gauss map: d n = -S, K = det S, n^* omega_{S^2} = det(-S) dA = K dA, independent of the choice of normal; saddle z=(x^2-y^2)/2 has S=diag(1,-1) and K=-1 at the origin (problem gauss-map-pulls-back-area).: Computed the unit normal (-x,y,1) to first order, its differential, and det; cross-checked K=(f_xx f_yy - f_xy^2)/(1+f_x^2+f_y^2)^2 = -1 at the origin; checked that a 2x2 determinant is even under S -> -S. → Correct in value, sign and orientation; the Gauss map reverses orientation there, matching det(dn)=-1.
- Gauss-Bonnet totals: 2 pi chi; dented ball 4 pi before and after; torus K dA = cos theta dtheta dphi, outer half +4 pi, inner half -4 pi, whole ring 0; Gauss map degree chi/2.: Hand integration of 2 pi int_{-pi/2}^{pi/2} cos theta dtheta = 4 pi, and of the full theta range giving 0; degree from 4 pi deg = 2 pi chi. → Correct; the numeric fields 12.566, 12.566 and 0 (abs_tol 0.01) are right. Denting keeps the surface compact, orientable and of Euler characteristic 2, so the total cannot change.
- Catenoid worked example: f=sqrt(c^2+rho^2), K=-c^2/(c^2+rho^2)^2, K=-0.25 cm^-2 at the waist for c=2 cm, total curvature -4 pi.: Checked that the catenary r=c cosh(z/c) has arc length s=c sinh(z/c) from the waist, so r=sqrt(c^2+s^2); differentiated twice; integrated with dA=f drho dphi and antiderivative rho/sqrt(c^2+rho^2). → Correct at every step, including the -4 pi total and the statement that the normals cover every direction except the two along the axis once, in the reverse sense.
- Check same-curvature-different-surfaces: helicoid (u cos v, u sin v, v) and surface of revolution (u cos v, u sin v, ln u) both have K=-1/(1+u^2)^2; their metrics are du^2+(1+u^2)dv^2 and (1+1/u^2)du^2+u^2 dv^2; |grad K|^2 is 16u^2/(1+u^2)^6 and 16u^4/(1+u^2)^7.: Computed E, F, G for both; K of the surface of revolution from (f'g'g''-f''g'^2)/(f(f'^2+g'^2)^2) with f=u, g=ln u; d_u K = 4u/(1+u^2)^3; |grad K|^2 = g^{uu}(d_u K)^2; compared as functions of w=1+u^2=(-K)^{-1/2}. → Correct. The ratio of the two gradients is (w-1)/w, never 1 for w>1, so no points with equal K have equal |grad K|, and no open sets are isometric. Minding's theorem for the constant case is correctly cited.
- Formal limits: Minding's theorem; a cone point of deficit delta carrying delta in the Gauss-Bonnet sum; Schur's lemma for n>=3 and connected; two-dimensional Lorentzian metrics keeping the one-component form and R=2K with a negative denominator.: Checked each against its hypotheses; for the Lorentzian case, the whole tangent plane is a timelike plane, so g(X,X)g(Y,Y)-g(X,Y)^2<0, as the sectional-curvature row of the conventions file states. → Correct as scoped; each carries the hypothesis it needs (connected, n>=3; constant K; compact oriented without boundary).
- Entry egg geometry: a 6 cm by 4 cm spheroid has principal radii 2 cm and 4.5 cm at its widest part and 4/3 cm at the tip; K = 1/9 and 9/16 per square centimetre; matching balls 3 cm and 4/3 cm; the tip's number is five times the widest part's.: python3 with the spheroid formulas a^2/c at the pole and (a, c^2/a) at the equator, a=2 cm, c=3 cm; ratio computed exactly. → R_tip=1.3333 cm, K_tip=0.5625; R=2 and 4.5 cm, K_eq=0.11111; ratio 5.0625. All correct, including 'five times as big'. The radii 2 and 4.5 cm are the space curvatures of the two paths because both the equator and the meridian of a spheroid are geodesics.
- Entry missing fractions: tip 0.38 per cent, widest part 0.07 per cent (five times smaller); football 70 cm round its middle gives 0.54 per cent at a 2 cm ring, a ball twice as wide 0.13 per cent (a quarter); a ball 4 cm wide misses more than the egg's widest part does.: python3 with K rho^2/6 at rho=0.2 cm and 2 cm, and the exact 1 - sin(x)/x on spheres. → 0.375, 0.0741 (ratio 5.06); football radius 11.14 cm gives 0.537, twice as wide 0.134 (ratio 0.2500); ball of radius 2 cm gives 0.167 against the egg's 0.074. Every rounded figure in the note is right.
- Entry Earth number: radius 6,371 km, K = 1 divided by about 40.6 million square kilometres, and a ring walked 1 km from its centre is short by about 0.026 mm, less than half the width of a hair.: python3: 6371^2 = 40.59 million km^2; shortfall 2 pi rho^3/(6 R^2). → 0.02580 mm. A human hair is 50 to 100 micrometres, so 'less than half the width of a hair' holds for a typical hair. Correct.
- Try-it: a 7 cm rubber ball gives a 2 cm ring of about 11.9 cm, some 7 mm short of 12.6 cm; a basketball gives just over half a millimetre; a taut thread traces a straight walk.: python3 with the exact 2 pi a sin(rho/a); a taut string on a convex surface follows a geodesic. → 11.894 cm, shortfall 6.73 mm; a 24 cm basketball gives 0.58 mm. Correct and doable as written.
- Entry check marble-and-football: 1 and 1/121 per square centimetre, the marble 121 times bigger, and a 1 mm ring's missing fraction about 121 times bigger.: python3; ratio of exact missing fractions at rho=0.1 cm. → 1 and 0.008264; ratio 121 exactly for K and 120.9 for the exact missing fractions, so 'about 121 times' is right. Numeric 121 with 3 per cent tolerance is fine.
- Entry check soap-film-waist: both bends of radius 2 cm toward opposite faces give K = -1/4 per square centimetre = -2500 m^-2, as strong as a ball of radius 2 cm but negative.: Catenoid with waist radius c=2 cm: the waist circle has radius c toward the axis and the profile catenary has vertex radius of curvature c away from the axis; unit conversion 1 cm^-2 = 10^4 m^-2. → Correct, and consistent with the worked example's -0.25 cm^-2 at a c=2 cm waist. The claim that the bends multiply rather than add is the point, and it is right.
- Entry problem swim-ring-two-spots: a 10 cm tube around a 30 cm hole gives +1/350 and -1/150 per square centimetre, -66.67 m^-2, and the inner spot about 2.3 times as strong.: python3; a 30 cm hole gives an inner radius of 15 cm, so the centre circle has radius 25 cm and the outer principal radius is 35 cm; 350/150 = 2.3333; -(1/150) cm^-2 = -66.67 m^-2. → Correct, including which bends go toward which face and both numeric fields with their tolerances.
- Entry common question: near the Sun starlight bends twice as much as it would if space there were not curved.: Weak-field deflection 2(1+gamma_PPN)GM/(c^2 b) in the conventions' PPN row: the time part alone (gamma_PPN=0) gives half the general-relativistic 1.75 arcseconds at the Sun's limb, the spatial curvature the other half. → Correct in the standard static isotropic-coordinate split, which is the only sense in which the statement is usually made. The fanned-pages picture is the sectional curvature of the surface swept by straight walks from a point, which is what this note's K measures.
- NOVICE REWRITE 1 (glossary/ring-test): 'walk straight out the same distance from a centre in every direction, and mark where each walk ends. Then measure, along the ground, the ring that runs through those marks. On a flat plain that ring is about 6.28 times the distance walked.': Compared with the geodesic-circle definition and with 2 pi = 6.2832; checked that splitting the instruction changes no quantity. → Accurate and unchanged in content. 'About 6.28' is the right hedge for 2 pi. No change.
- NOVICE REWRITE 2 (glossary/missing-fraction): 'How much shorter a ring is than 6.28 times the distance walked, divided by 6.28 times the distance walked.': Compared with (2 pi rho - C)/(2 pi rho) and with every use of the term in the entry ways, the checks and the working way's K rho^2/6. → Accurate: it names exactly one division, and it is the division the explanation performs. No change.
- NOVICE REWRITE 3 (matching-ball way): 'So for rings walked out the same short distance, the smaller the ball, the bigger the missing fraction.': Monotonicity of the exact missing fraction 1 - sin(rho/a)/(rho/a) in a at fixed rho. → True: sin(x)/x decreases on (0, pi), so the missing fraction grows as a shrinks, for every ring short enough to stay inside the antipode. 'Short distance' carries that condition. No change.
- NOVICE REWRITE 4 (matching-ball way): 'So the egg's rings there miss less than rings on a ball 4 centimetres wide.': python3: egg's widest part 0.0741 per cent against 0.167 per cent for a ball of radius 2 cm, at rho=0.2 cm. → True, and naming both sets of rings removes the earlier ambiguity without changing the claim. No change.
- NOVICE REWRITE 5 (matching-ball way): 'The crisp's wavy edge hints why. A ring longer than 6.28 times the distance from its centre cannot be laid on flat paper, so it ripples.': Counterexample from the earlier diff check, retried: a loop of string of any length can be laid on paper by letting it wiggle, so 'cannot be laid on flat paper' is false unless the ring must keep every point at the walked distance from its centre. The earlier physics pass had added that scope; the rewrite dropped it while repairing a dangling phrase. → FIXED. The sentence now reads 'cannot be laid on flat paper and keep that distance, so it ripples'. The scope is restored as a second verb clause, so it no longer hangs off 'flat paper'. The direction of the implication stays the true one (too long, so it ripples), not the corrugated-sheet converse.
- NOVICE REWRITE 6 (two-bends way): 'On the egg, every path bends toward the inside face of the shell.': Checked that a prolate spheroid is convex, so every normal curvature is positive at every spot, and that 'path' in this way means a straight walk, whose space curvature vector is along the normal. → True at every spot of the egg, for the straight walks the way is about. 'Bends' also restores the note's one word for one idea. No change.
- NOVICE REWRITE 7 (two-bends way): 'The gentler a bend, the bigger its circle, so the bigger the two radii multiplied, and the closer 1 divided by that result gets to zero.': Limit check on the rolled poster: the sharpest radius stays at the tube's radius while the gentlest grows without bound, so the product grows without bound and 1 over it tends to 0. → True as a limit statement in the poster's setting, and naming what is multiplied removes the implicit step. No change.
- NOVICE REWRITE 8 (two-bends takeaway): 'Multiply the radii of a spot's sharpest and gentlest bends, and divide 1 by the result. That is the ant's Gaussian curvature. On a saddle, use the sharpest bend toward each face instead, and give the number a minus sign.': Checked the three cases: both bends toward one face (K=kappa_1 kappa_2>0); one bend absent, as on a cylinder (product of radii unbounded, K=0); bends toward opposite faces (K=-|kappa_1 kappa_2|). Compared with Euler's theorem and with the way's own worked numbers. → Accurate in all three cases and now sayable back as a sentence. The umbilic case (the egg's tip) is covered because the sharpest and the gentlest bends coincide. No change.
- Reference Moritz 1980, 'Geodetic Reference System 1980', Bulletin Geodesique 54, 395-405, doi 10.1007/BF02521480.: Fetched the Crossref record for the DOI. → Confirmed: H. Moritz, 1980, Bulletin Geodesique, volume 54, issue 3, pages 395-405. Stays verified.
- Reference Gauss 1828, 'Disquisitiones generales circa superficies curvas', Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99-146, and the history year 1827.: Web search of library and bibliographic records for the work. → Confirmed: read to the Gottingen society on 8 October 1827 and published in volume 6 (1828), pages 99-146. The history entry's year 1827 is the reading, the reference's 1828 the publication, and the contribution is scoped to what Gauss proved. Stays verified.
- History minding-1839: Minding showed that surfaces with equal constant Gaussian curvature are locally isometric.: Web search of the standard attribution; the work field is null, so nothing beyond the year and the scope needed confirming. → Confirmed for 1839. The scope is right: the theorem is local and needs the curvature to be constant, which the formal way and the check both state.
- Structure: prerequisites direct and acyclic; every 'assumes' id is a prerequisite or a prerequisite of one, at or below its way's rung; foundation tier has entry, working and formal ways, objectives and checks, two formal checks and one formal problem; every check and problem evidences an objective; targets and diagnosed_by agree; visuals are catalog proposals with sketches; no source book is named anywhere.: Script walk of the prerequisite graph over notes and registries (151 ancestors, none is gaussian-curvature); script check of every 'assumes' id against the allowed set; read of every field against the schema and the validator. → Consistent. The two visuals are proposals with sketches, as the validator's notes say, and the registry mismatch for curvature-of-a-curve and riemann-curvature-tensor is for sync_registry.py.

**Counterexamples tried**

- Rolled poster (bent but intrinsically flat): the outsider's rule gives zero because the gentlest bend has no circle, and the ring rule gives zero because rolling changes no length along the paper. Both entry statements survive, and the way uses this case on purpose.
- Corrugated roof sheet (wavy but flat): retried against the crisp sentence. The converse reading 'wavy, so extra length' is false here, and the note states only the true direction, that a ring longer than 6.28 times the distance from its centre cannot keep that distance on flat paper.
- A loop of string longer than its circle, laid on a table: this is why 'cannot be laid on flat paper' needs the distance clause, which this review restored.
- Umbilic spot (the egg's tip, any point of a ball): the sharpest and the gentlest bends coincide; the takeaway and the rule both still read correctly, and the numbers 4/3 cm and 9/16 per square centimetre are right.
- Parabolic spot (the swim ring's top circle, a cylinder): one principal curvature is zero, K=0, and the line-element formula agrees; the entry limiting argument reaches the same answer.
- Minimal surface (catenoid waist): equal and opposite bends give -1/c^2, not zero. The soap-film check targets exactly this, and the worked example gives the same value independently from the line element.
- Cone tip: K is not defined as a smooth value; the formal way treats the deficit as a point mass in the Gauss-Bonnet sum, and every entry sentence is scoped to a smooth surface.
- Great circle and a region bigger than half a closed surface: not used by this note, but the Gauss-Bonnet totals are stated for whole compact surfaces, where the 4 pi and 0 results are exact.
- Helicoid against the logarithmic surface of revolution: equal varying K at corresponding coordinates, yet |grad K| differs at every such point, so they are nowhere locally isometric. The formal limits and the check both carry this.
- Scale and size what-ifs: a ball eleven times as wide gives 121 times smaller K; enlarging every length by 3 divides K by 9; a ball twice as wide quarters the missing fraction. All three are stated and all three check out.
- Non-orientable and Lorentzian cases: a Mobius band has no global normal, so the Gauss-map statements are stated for oriented surfaces; in two-dimensional Lorentzian signature the one-component form and R=2K survive, with a negative sectional-curvature denominator, which the formal way says.
- Different observer or description for the light-bending sentence: the half-from-time, half-from-space split is the standard static isotropic-coordinate split, and the entry sentence is true in that standard sense.

**Fixes**

- Matching-ball way, one entry sentence: 'A ring longer than 6.28 times the distance from its centre cannot be laid on flat paper, so it ripples.' now reads '... cannot be laid on flat paper and keep that distance, so it ripples.' A loop of string of any length can be laid on paper by wiggling, so the claim is false without the distance condition; the earlier physics pass had added that condition and the second novice pass dropped it while repairing a dangling phrase. The condition is now a second verb clause, so it neither dangles nor compresses anything. Four words added; entry-way explanations go from 1,090 to 1,094 against the foundation cap of 1,000, inside the 10 per cent review allowance.
- Nothing else changed. The other five strings the second novice pass rewrote were checked claim by claim and are accurate as they stand.
- No number, equation, condition, sense, branch or scope elsewhere in the note was altered. Status set to physics-reviewed, revision bumped to 7, review.physics.reviewed_revision set to 7.
- The earlier physics record's diff_checks entry (revision 5) is preserved rather than discarded; this entry replaces the verification, counterexamples, fixes and concerns of that pass with a full second-pass record.

**Concerns**

- This is a second full physics pass over a note both stages had already signed, prompted by the second novice pass that took it to revision 6. Everything was re-derived and recomputed from scratch, not taken from the earlier record; the earlier pass's diff_checks entry is kept for history.
- A novice re-read of exactly one entry string follows, and until it signs, review.novice covers revision 6 while the note is at 7. That is the only validator warning and it is expected.
- Entry-way explanations now stand at 1,094 words against the foundation cap of 1,000, with six words of the 10 per cent review allowance left. Any further entry addition needs a cut first; the note's own cheapest cut is still the scene-setting sentence 'Balls give a scale to compare with', whose work the football numbers already do.
- The matching-ball construction, and the entry rule that a too-long ring's size comes from a ball's missing fraction, hold to leading order in the ring's radius. At 2 mm on a 4 cm egg the higher-order correction is well under the two figures quoted, so every number in the note is right as printed; the prose says 'small rings' but never states the limit, which is the honest entry-level choice.
- The egg's bend radii assume a spheroid with semi-axes 2, 2 and 3 cm. The phrase 'as a careful drawing of the egg's outline shows' carries that; a real egg, whose ends differ, would change 4.5 cm and 4/3 cm.
- Carried forward for an editor, unchanged by this stage: 'best-fit circle' here against 'osculating circle' in the prerequisite curvature-of-a-curve, a vault-wide vocabulary choice; the two visuals are still proposals, not catalog entries; the registry's prerequisites differ from the note's for curvature-of-a-curve and riemann-curvature-tensor, which sync_registry.py reconciles; and there is still no entry check for a ring that comes out too long or for the Earth number, and no check for the plumb-line way or the one-component Riemann form.
- No missing course conventions. course-conventions.md made every choice this review needed, including the Riemann and Ricci signs, the sectional-curvature sign, the rotation sense for surfaces and the units by rung.

**Diff check** (2026-09-13, revision 5)

- Matching-ball way: 'a ring with extra length cannot be laid on flat paper, so it ripples.': First what-if and counterexample: a necklace longer than a circle of the walked radius, laid on a table; comparison with the ring test's definition (every point of the ring is the distance walked from the centre); geodesic-circle expansion C = 2 pi r (1 - K r^2/6) checked numerically for K = +1/9 and -1/9 per square centimetre at r = 0.2 cm. → As worded, false: any loop of string, however long, can be laid on paper by letting it wiggle. What is true is that a ring longer than 6.28 times the distance walked cannot lie on paper with every point that distance from its centre, so its extra length must ripple. Scoped by adding 'at the distance walked from its centre'. The expansion confirms negative K gives too-long rings (fractional excess 7.4e-4 at r = 0.2 cm, matching -K r^2/6).
- Matching-ball way: 'Near the crisp's middle, the ant finds the ball whose missing fraction equals the fraction by which her ring is too long.': Read in paragraph; compared with the matching-ball definition (2 millimetre rings) and the working rung's leading-order ring formula. → True to leading order for small rings, and the location now correctly names the crisp's middle rather than its edge. Same claim as before. No change.
- Two-bends way: 'Gauss proved in 1827 that the outsider's number depends only on lengths along the surface, just as the ant's rings do.': History check against the note's history entry gauss-1827 and the Theorema Egregium (read 8 October 1827, published 1828): the product of principal curvatures is expressible through the first fundamental form alone. Ring lengths and walked distances are measured along the surface, so they are intrinsic by definition. → True. The added clause does not attribute the ring formula to Gauss (that was Bertrand, Diguet and Puiseux, 1848); it only notes that the rings are also built from lengths. No change.
- Two-bends way: 'So rolling a poster, or any change that keeps lengths along the surface, never breaks the agreement.': Logic check: if both numbers depend only on lengths, a length-preserving bending leaves both unchanged, so an agreement that held before still holds. What-ifs: rolling a poster (K = 0 before and after); bending a spherical cap isometrically (K = 1/R^2 kept, principal bends change); creasing paper (a crease is not smooth, so the outsider's rule is undefined there). → True, and it follows from the previous sentence. The crease case is covered by the next sentence's scope to smooth surfaces. No change.
- Two-bends way: 'The agreement holds at every spot of every smooth surface in ordinary space.': Compared with the pre-reread sentence and the theorem (Theorema Egregium plus the Bertrand-Diguet-Puiseux ring formula) for smooth surfaces embedded in three-dimensional Euclidean space; counterexamples cone tip and crease excluded by 'smooth'. → True, with the same scope as before. No change.
- Fix: Matching-ball way: 'a ring with extra length cannot be laid on flat paper, so it ripples.' now reads 'a ring with extra length cannot be laid on flat paper at the distance walked from its centre, so it ripples.' (a long necklace lies on paper by wiggling, so the unscoped claim was false).
- Fix: Revision bumped to 5; review.physics.reviewed_revision set to 5.

**Diff check** (2026-09-13, revision 8)

- Scope of this diff check: note_diff.py (gaussian-curvature.before-reread.json -> current, entry and working rungs) lists exactly one changed learner-visible string and no working string: the crisp sentence in $.ways_in[a-matching-ball-for-each-spot].explanation, reworded by the novice re-read from 'cannot be laid on flat paper and keep that distance, so it ripples' to 'cannot be laid on flat paper and stay that far from the centre, so the ring ripples'.: Ran note_diff.py against the pre-re-read snapshot; read the changed sentence inside its paragraph and read the way's recap first for the ring test's vocabulary; nothing else read closely. → One sentence in scope. No number, equation, check, problem, worked example, observation or reference was touched, so nothing needed re-deriving or recomputing and no reference needed verifying.
- The reworded sentence claims exactly what the pre-re-read sentence claimed: 'stay that far from the centre' is the same condition as 'keep that distance'.: Compared the two clauses against their antecedent. 'The distance from its centre' is named earlier in the same sentence and 'the centre' is the ring's own centre, so both clauses say every point of the ring stays that one distance from that one point. Checked that the scope condition the earlier diff check added at revision 7, to exclude the loop-of-string counterexample, is what this clause carries. → Identical claim, and the new wording names the reference point explicitly rather than leaving it to 'that distance'. The string-loop counterexample stays excluded. No change.
- The claim itself: a ring longer than 6.28 times the distance from its centre cannot be laid on flat paper and stay that far from the centre.: Plane geometry, checked numerically with python3: on flat paper the set of points at one distance r from a centre point is a single circle of total length 2 pi r, computed as 1.2566 cm at r = 0.2 cm, 12.566 cm at r = 2 cm and 628.32 cm at r = 100 cm, against the note's 6.28 times r (2 pi = 6.28319, so 6.28 is the right two-figure value). A simple ring longer than that, laid once round, has no room on that circle, so part of it must leave the paper. → True, and backed inside the note: the way's recap already states that on a flat plain the ring is about 6.28 times the distance walked. The universal 'cannot' carries its three conditions in the sentence: longer than 6.28 times the distance, on flat paper, and staying that far from the centre.
- The consequent, 'so the ring ripples', names the right thing and follows from the clause before it.: Checked which object the impossibility falls on: the paper is stipulated flat and the centre-distance is stipulated kept, so the only freedom left is the ring leaving the plane. Compared with the sentence before it, which offers the crisp's wavy edge as the picture, and with the pre-re-read 'so it ripples'. → Correct, and the re-read's replacement of the pronoun by 'the ring' names the object that actually ripples rather than the paper. Same physics as before.
- The sentence is consistent with the rest of the note and with course-conventions.md.: Checked the constant 6.28 and the words 'ring', 'centre' and 'distance' against the way's recap, its try_it and its takeaway, and against the neighbouring sentences on zero and negative curvature. Checked course-conventions.md for any binding choice on surface curvature signs or the ring test. → Consistent throughout; the sentence states no angle, sense, branch, frame or observer, so no conventions row applies to it. Length 28 words, under the 32-word ceiling.
- Fix: None. The one changed sentence is accurate within its stated scope, claims exactly what it replaced, and needed no edit. Revision stays 8; review.physics.reviewed_revision set to 8.
- Fix: Counterexamples tried against the changed sentence, all cleared: a loop of string longer than 6.28 r laid flat as a wider circle (excluded by 'stay that far from the centre'); a ring laid twice round the flat circle (its two strands would lie on each other, not on the paper, and the ring test's ring is the single ring through the end marks of equal straight walks); a ring exactly 6.28 times the distance and a ring shorter than that (both outside the sentence's 'longer than' scope, and both covered elsewhere in the way); a centre that is a region rather than a point (the ant's spot is a point).
