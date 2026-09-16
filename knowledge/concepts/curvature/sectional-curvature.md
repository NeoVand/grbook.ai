---
type: "concept"
schema_version: 2
id: "sectional-curvature"
title: "Sectional curvature"
tagline: "How strongly space curves in one tilt at a single spot"
domain: "curvature"
tier: "advanced"
status: "novice-reviewed"
revision: 2
updated: "2026-09-13"
aliases: ["curvature of a two-plane", "two-plane curvature"]
prerequisites: ["gaussian-curvature", "riemann-curvature-tensor", "geodesic-deviation-equation"]
leads_to: ["space-of-constant-curvature", "einstein-space", "einstein-tensor", "conjugate-point", "curvature-of-the-flrw-metric"]
visuals: ["ring-in-each-tilt-of-the-ball-building", "falling-ring-of-crumbs", "three-rings-around-a-spot"]
---

# Sectional curvature

*How strongly space curves in one tilt at a single spot*

`sectional-curvature` · curvature · advanced · novice-reviewed (revision 2)

**Needs:** [[gaussian-curvature]] (entry) · [[riemann-curvature-tensor]] (entry) · [[geodesic-deviation-equation]] (working)  
**Opens:** [[space-of-constant-curvature]] · [[einstein-space]] · [[einstein-tensor]] · [[conjugate-point]] · [[curvature-of-the-flrw-metric]]  
**Related:** [[ricci-tensor]] · [[ricci-scalar]] · [[relativistic-tidal-tensor]] · [[riemann-curvature-operator]] · [[holonomy]]  
**Visuals:** ★ [[ring-in-each-tilt-of-the-ball-building]] · [[falling-ring-of-crumbs]] · [[three-rings-around-a-spot]]

> In a space with three or more directions, a small flat piece at one spot can lie at many tilts, like a box's bottom, front or side. Run the ring test using only straight walks that set off in one tilt. The ring gives that tilt its own number for how strongly space curves there. That number is the tilt's sectional curvature, and different tilts at one spot can give different numbers.

## You will be able to

**Entry**
- Explain how a ring of straight walks that set off in one tilt gives that tilt its own sectional curvature. `objectives/explain-a-ring-for-each-tilt` ← `checks/upright-ring-length`
- Explain why one ring of playground length at a spot does not show that space there is flat. `objectives/explain-one-flat-ring-is-not-enough` ← `checks/one-flat-ring`

**Working**
- Compute the sectional curvature of a plane from Riemann components in any basis. `objectives/compute-plane-curvature-from-components` ← `checks/sphere-coordinate-component`
- Find the sign and size of a timelike plane's curvature from measured tidal accelerations. `objectives/read-timelike-planes-from-tides` ← `checks/radial-pair-in-a-falling-cabin`
- Relate single plane curvatures to the energy density an observer measures. `objectives/use-plane-sums` ← `checks/three-planes-in-water`, `problems/plane-curvatures-around-a-neutron-star`
- Predict where neighbouring geodesics refocus from the curvature of their plane. `objectives/predict-refocusing-from-a-plane` ← `problems/refocusing-in-the-ball-building`

**Formal**
- State Schur's lemma and explain why it says nothing in two dimensions. `objectives/apply-schur-and-its-limits` ← `checks/schur-on-a-surface`
- Show that sectional curvature at an event of a curved spacetime is unbounded near degenerate planes. `objectives/explain-unbounded-lorentzian-planes` ← `checks/planes-near-a-light-cone`
- Prove that a four-dimensional metric is Einstein exactly when orthogonal planes have equal curvature. `objectives/prove-einstein-planes-pair` ← `problems/einstein-spaces-pair-orthogonal-planes`

**Research**
- Evaluate claims linking sign conditions on sectional curvature to a manifold's topology. `objectives/evaluate-curvature-topology-claims` ← `checks/hopf-product-claim`

## Ways in

### 1. Two rings at one spot · entry · picture

*At a spot with three directions to move in, does every ring test agree?*

**Recap:** Walking straight means moving without ever steering: not to the left, not to the right, and, where you can rise or sink, not upward or downward.

A tilt is the way a small flat piece is angled at a spot, set by two directions along that piece.

The ring test: walk straight out the same short distance from a spot, in every direction of one tilt, and mark where each walk ends. Then measure the ring through those marks, keeping to the surface the walks sweep out. On flat ground it comes out at its playground length. On a ball it comes out short.

In the ball building every floor is the whole surface of a huge ball, and every floor is an exact copy of the same ball, joined by lift shafts.

There is a floor at every height in the ball building, so you may move any way you like: along a floor, up a shaft, or slanting. Call any such trip a walk; upward means along a shaft.

At one spot, the level tilt is set by two floor directions, an upright tilt by the upward direction and one floor direction.

Every height here is alike, so nothing can make a walk gain more height at one height than at another. A straight walk therefore gains the same height for each metre it covers.

Run the ring test in the level tilt. Each walk sets off gaining no height, so it never gains any. Those walks stay on the floor, which is a ball's surface, so the ring comes out short.

Now run the test in an upright tilt. Each walk rises or sinks steadily while heading along one floor direction, or its opposite. Every floor is an exact copy, so at any height you can say which place on the ball you are at. That place moves as you walk, and it never steers: steering it would mean steering yourself. So every walk keeps to the lift shafts through one straight path around the ball. That path runs through your start along that floor direction.

Those shafts make a tube, which unrolls flat without stretching. On the unrolled sheet every mark still sits the same distance from the centre, so the ring is an ordinary circle of playground length.

**Try it:** Roll a sheet of paper into a tube about 20 centimetres around and tape the seam. The tube stands for the surface that the walks in an upright tilt sweep out. On the far side of the tube from the seam, halfway up, tape one end of a thread. Tie a pen to that thread 2 centimetres along. Keeping the thread tight against the paper, draw a ring. Lay a second thread along the ring to measure it: about 12.6 centimetres, its playground length. On a ball 20 centimetres around, the same ring comes out about 11.8 centimetres.

**Takeaway:** At one spot of the ball building, a ring in the level tilt comes out short, while a ring in an upright tilt comes out at its playground length.

*What this leaves out:* A tilt between level and upright gives a ring whose length falls between those two. For tilts other than level and upright, the ring gives that tilt's number only when the distance walked is very short.

*Builds on:* [[gaussian-curvature]], [[riemann-curvature-tensor]]<br>*Visuals:* [[ring-in-each-tilt-of-the-ball-building]]<br>*See:* `checks/upright-ring-length`

### 2. One ring does not settle a spot · entry · contrast

*If one ring at a spot comes out at its playground length, is space flat there?*

**Recap:** In the ball building, every floor is the whole surface of one huge ball. Every floor is an exact copy of the same ball. Lift shafts join each spot to its copies, and there is a floor at every height. At one spot, a ring in the level tilt comes out short. A ring in an upright tilt comes out at its playground length, about 6.28 times the distance walked.

In "Two rings at one spot" one spot gave two different rings. So a ring test measures a tilt, not a spot.

Turn each tilt's ring into a number, exactly as for a surface: find the matching ball, multiply its radius by itself, and divide 1 by the result. A ring of playground length misses nothing, so its number is zero, and a too-long ring gets a minus sign. This number is called the sectional curvature of that tilt.

So space at a spot is flat exactly when every tilt there has sectional curvature zero. One ring never settles that, because it tests only one tilt.

Real space has tilts too. Take space as people standing on the ground measure it, all at one moment by their clocks. There a level tilt's straight walks do not keep to the ground: a walk that sets off level rises away from it. One kilometre out from a spot just above the ground, that ring falls short by less than a thousandth of an atom's width. An upright ring there comes out too long.

**Takeaway:** Each tilt at a spot has its own sectional curvature, so space at that spot is flat exactly when every tilt there gives zero.

*What this leaves out:* The numbers quoted for real space are what general relativity predicts for a ball-shaped Earth that does not spin.

*Continues:* `ways_in/two-rings-at-one-spot`<br>*Builds on:* [[gaussian-curvature]]<br>*Visuals:* [[ring-in-each-tilt-of-the-ball-building]]<br>*See:* `checks/one-flat-ring`

### 3. One formula for any plane · working · calculation

*How is a plane's curvature computed from the Riemann tensor, and why does it depend only on the plane?*

The two rings at one spot of the ball building gave one number per tilt; the Riemann tensor gives the same number directly. A tilt is now a plane in the tangent space, and the straight walks are geodesics. At a point $p$, let a plane $\Pi$ be spanned by vectors $X$ and $Y$. Its sectional curvature, in the course sign convention, is

$$K(\Pi) = \frac{R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma}{g(X,X)\,g(Y,Y) - g(X,Y)^2}.$$

The denominator is the squared area of the parallelogram on $X$ and $Y$. Replace the pair by $X' = aX + bY$ and $Y' = cX + dY$. Antisymmetry of $R_{\mu\nu\rho\sigma}$ in each index pair multiplies the numerator by $(ad - bc)^2$, and the denominator changes by the same factor, so $K$ depends only on the plane. For an orthonormal pair of a positive-definite metric it is the single component $R_{\hat 1\hat 2\hat 1\hat 2}$. A coordinate component must still be divided by its denominator: on a sphere of radius $a$, $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$, while $K = 1/a^2$.

Two measurements read $K(\Pi)$.

- *Rings.* Geodesics leaving $p$ tangent to $\Pi$ sweep out a small surface whose Gaussian curvature at $p$ is $K(\Pi)$, stated here without proof. A geodesic circle of radius $\ell$ in that surface has length $2\pi\ell\,(1 - K\ell^2/6 + \dots)$, which is the ring test of the ball building.
- *Loops.* Walk a small loop $+\delta e_1$, $+\delta e_2$, $-\delta e_1$, $-\delta e_2$ on orthonormal $e_1, e_2$ spanning $\Pi$. The small-loop law $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, with $a = \delta e_1$ and $b = \delta e_2$, changes the carried $e_1$ by $\Delta V^{\hat 2} = -R^{\hat 2}{}_{\hat 1\hat 1\hat 2}\delta^2 = +K\delta^2$: a rotation from $e_1$ toward $e_2$ by $K$ times the loop's area.

In the ball building the metric is a product: the floor is a sphere of radius $a$, and the lift direction contributes a flat line. A plane tilted by $\alpha$ from level has $K = \cos^2\alpha/a^2$, worked out in "A slanted plane in the ball building". A round 3-sphere of radius $b$ has $K = 1/b^2$ for every plane at every point.

For an orthonormal basis of a positive-definite space, contracting the definition gives $\mathrm{Ric}(e_a,e_a) = \sum_{b\ne a}K(e_a,e_b)$ and $R = 2\sum_{a<b}K(e_a,e_b)$. These sums lose the single planes. The ball building has $R = 2/a^2$, as does a round 3-sphere of radius $\sqrt3\,a$, yet only the 3-sphere has the same curvature on every plane.

**Takeaway:** Sectional curvature is the Riemann tensor fed a plane's two vectors twice, divided by the squared area they span; it is the Gaussian curvature of the geodesic surface tangent to the plane.

*What this leaves out:* The Ricci sums as written hold for positive-definite metrics; the ring and loop readings hold to leading order in size.

*Continues:* `ways_in/two-rings-at-one-spot`, `ways_in/one-ring-does-not-settle-a-spot`<br>*Builds on:* [[riemann-curvature-tensor]], [[gaussian-curvature]]<br>*Visuals:* [[ring-in-each-tilt-of-the-ball-building]]<br>*See:* `worked_examples/slanted-plane-in-the-ball-building`, `checks/sphere-coordinate-component`

### 4. Tides and matter read planes in spacetime · working · operational

*What do falling test masses and local matter tell an observer about the sectional curvatures of spacetime?*

The formula that divides the Riemann tensor by a squared area applies unchanged in spacetime, with signature $(-,+,+,+)$, to every plane whose denominator is not zero. A plane containing a timelike vector has a negative denominator. A null plane, tangent to a light cone, has a zero denominator and no sectional curvature.

*Tides read timelike planes.* Take two neighbouring freely falling test masses with four-velocity $u$, $g(u,u) = -c^2$, and small separation $\xi$ along a parallel-transported unit spatial vector $e \perp u$. Contracting the geodesic deviation equation $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ with $e_\mu$ gives $-R_{\mu\nu\rho\sigma}e^\mu u^\nu e^\rho u^\sigma\,\xi$, and the definition makes that numerator $K(u,e)\,(-c^2)$. So the relative acceleration along $e$ is

$$\ddot\xi = +c^2K(u,e)\,\xi.$$

Positive $K$ means the masses accelerate apart, the opposite of meridians converging on a sphere. Near a spherical mass $M$, masses separated along the radius accelerate apart at $2GM\xi/r^3$, so $K(u,e_r) = +2GM/c^2r^3$. Masses separated across the radius approach at $GM\xi/r^3$, so $K = -GM/c^2r^3$. At Earth's surface these are $+3.43\times10^{-23}$ and $-1.72\times10^{-23}$ m$^{-2}$.

*Space at one moment.* Observers at rest outside a non-rotating star slice spacetime into space at one moment. That slice is not bent within spacetime, because the static metric is unchanged by reversing time, so its extrinsic curvature vanishes. The Gauss equation, taken on trust here, then makes the slice's own plane curvatures equal the spacetime ones. Its level plane has $K = +2GM/c^2r^3$ and each plane containing the radius has $K = -GM/c^2r^3$.

*Matter fixes a sum.* Take an observer's unit four-velocity $\hat u$ and orthonormal spatial vectors $e_1, e_2, e_3$. The derivation "Energy density from three planes" shows that $G_{\mu\nu}\hat u^\mu\hat u^\nu = K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1)$. Einstein's equation, taken on trust here, then gives

$$K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1) = \frac{8\pi G\rho}{c^2} + \Lambda,$$

with $\rho$ the mass density the observer measures. Outside a star the three planes give $2 - 1 - 1 = 0$ in units of $GM/c^2r^3$. In water at rest, $8\pi G\rho/c^2 = 1.87\times10^{-23}$ m$^{-2}$, and $\Lambda = 1.1\times10^{-52}$ m$^{-2}$ adds nothing measurable. Density fixes only this sum; how it is shared among single planes depends on matter elsewhere.

**Takeaway:** Tides read planes containing the four-velocity, where positive curvature means test masses accelerate apart; local energy density fixes only the sum over three perpendicular spatial planes.

*What this leaves out:* The plane values are exact outside a non-rotating spherical mass; the accelerations quoted are the Newtonian reading for slow test masses close together.

*Continues:* `ways_in/one-formula-for-any-plane`<br>*Builds on:* [[geodesic-deviation-equation]]<br>*Visuals:* [[falling-ring-of-crumbs]], [[three-rings-around-a-spot]]<br>*See:* `derivations/energy-density-from-three-planes`, `problems/plane-curvatures-around-a-neutron-star`, `observations/goce-radial-plane`

### 5. Planes fix the curvature tensor · formal · structure

*In what precise sense do sectional curvatures determine the Riemann tensor, and where does that fail?*

The formula for any plane is a function on planes, and it carries the whole curvature tensor. Let $(M,g)$ be a smooth semi-Riemannian manifold of dimension $n \ge 2$ with its Levi-Civita connection, and write $\mathrm{Rm}(X,Y,Z,W) = R_{\mu\nu\rho\sigma}X^\mu Y^\nu Z^\rho W^\sigma$ and $Q(X,Y) = g(X,X)g(Y,Y) - g(X,Y)^2$. A plane $\Pi \subset T_pM$ is nondegenerate when $Q \ne 0$ on a basis of it, and there $K(\Pi) = \mathrm{Rm}(X,Y,X,Y)/Q(X,Y)$. In Riemannian signature every plane is nondegenerate, the planes at $p$ form the compact Grassmannian $\mathrm{Gr}_2(T_pM)$, and $K$ attains a maximum and a minimum on it.

*Determination.* An algebraic curvature tensor has both pair antisymmetries, pair exchange and the cyclic identity. Two such tensors with equal $K$ on every nondegenerate plane at $p$ are equal. Their difference $T$ has $T(X,Y,X,Y) = 0$ on the dense open set of pairs with $Q \ne 0$, hence everywhere, and the derivation "Recover the tensor from its planes" turns this into $T = 0$ through the formula

$$6\,\mathrm{Rm}(X,Y,Z,W) = \frac{\partial^2}{\partial x\,\partial y}\Big[B(X + xZ,\, Y + yW) - B(X + xW,\, Y + yZ)\Big]_{x = y = 0},$$

with $B(X,Y) = \mathrm{Rm}(X,Y,X,Y)$. The cyclic identity is essential: for a metric connection with torsion it fails, and plane values no longer fix the curvature.

*Constant curvature and Schur's lemma.* The tensor $\bar K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ is algebraic with sectional curvature $\bar K$ on every nondegenerate plane. So $K$ takes one value $\bar K(p)$ on all nondegenerate planes at $p$ exactly when $R_{\mu\nu\rho\sigma}$ has this form there. If that holds at every point of a connected manifold with $n \ge 3$, then $\bar K$ is constant: $R_{\mu\nu} = (n-1)\bar Kg_{\mu\nu}$, and the contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ gives $(n-1)(1 - n/2)\,\partial_\nu\bar K = 0$. For $n = 2$ the factor vanishes and the hypothesis is empty.

*Three dimensions.* For Riemannian $n = 3$, with $N$ a unit normal of $\Pi$, $K(\Pi) = -G_{\mu\nu}N^\mu N^\nu$. Every plane curvature is a value of one symmetric tensor, so the Ricci tensor determines the Riemann tensor.

*Indefinite signature.* For $n \ge 3$, nondegenerate planes accumulate at degenerate ones, where $Q \to 0$ while $\mathrm{Rm}(X,Y,X,Y)$ need not. Kulkarni's theorem states that if $K$ is bounded above, or below, on the nondegenerate planes at $p$, then $K$ is constant at $p$. So a one-sided bound on all planes at an event occurs only where the curvature is constant. In four dimensions, in either signature, $R_{\mu\nu} = \lambda g_{\mu\nu}$ exactly when $K(\Pi) = K(\Pi^\perp)$ for every nondegenerate plane.

**Takeaway:** Plane curvatures on nondegenerate planes fix the curvature tensor through the cyclic identity; one value on all planes means constant curvature, and in indefinite signature any one-sided bound forces that.

*Continues:* `ways_in/one-formula-for-any-plane`<br>*Builds on:* [[levi-civita-connection]]<br>*See:* `derivations/recover-the-tensor-from-planes`, `checks/schur-on-a-surface`, `checks/planes-near-a-light-cone`, `problems/einstein-spaces-pair-orthogonal-planes`

### 6. Bounds on planes steer geodesics · formal · calculation

*What do bounds on sectional curvature imply for geodesics and for the shape of a whole manifold?*

The relative acceleration that tides read has a Riemannian twin that turns bounds on planes into global geometry. Let $\gamma$ be a unit-speed geodesic with arc length $\ell$ in a Riemannian manifold, and let $J \perp \dot\gamma$ be a Jacobi field, $D^2J^\mu/d\ell^2 = -R^\mu{}_{\nu\rho\sigma}\dot\gamma^\nu J^\rho\dot\gamma^\sigma$. Contracting with $J$ gives

$$g(J, J'') = -K(\dot\gamma, J)\,|J|^2.$$

Only planes containing $\dot\gamma$ steer the neighbours of $\gamma$. A conjugate point is a zero of a nontrivial Jacobi field with $J(0) = 0$.

*Upper bounds.* Suppose $K \le k$ on every plane containing $\dot\gamma$, and $J(0) = 0$. Let $\mathrm{sn}_k$ solve $f'' + kf = 0$ with $f(0) = 0$ and $f'(0) = 1$: that is $\sin(\sqrt k\,\ell)/\sqrt k$, or $\ell$, or $\sinh(\sqrt{-k}\,\ell)/\sqrt{-k}$. Rauch's comparison theorem gives $|J(\ell)| \ge \mathrm{sn}_k(\ell)\,|J'(0)|$ for $0 < \ell < \pi/\sqrt k$ when $k > 0$, and for all $\ell > 0$ when $k \le 0$. So no conjugate point occurs before $\ell = \pi/\sqrt k$, or none at all when $k \le 0$. On a complete, simply connected manifold with $K \le 0$, $\exp_p$ is then a diffeomorphism from $T_pM$ onto $M$ (Cartan–Hadamard).

*Lower bounds.* Suppose $K \ge k > 0$ on every plane, and take a geodesic of length $L > \pi/\sqrt k$, a parallel unit field $E \perp \dot\gamma$, and $V = \sin(\pi\ell/L)\,E$. The second variation of length is

$$I(V,V) = \int_0^L\Big(|V'|^2 - K(\dot\gamma,E)\,|V|^2\Big)d\ell \le \frac L2\Big(\frac{\pi^2}{L^2} - k\Big) < 0,$$

so $\gamma$ is not minimizing. A complete manifold with $K \ge k > 0$ therefore has diameter at most $\pi/\sqrt k$, is compact, and has finite fundamental group (Bonnet–Myers). Summing over $n - 1$ orthonormal choices of $E$ shows that $\mathrm{Ric} \ge (n-1)k\,g$ already suffices. Synge's theorem adds that a compact, orientable, even-dimensional manifold with $K > 0$ is simply connected.

*The ball building.* A geodesic rising at angle $\beta$ above the floor has $K(\dot\gamma,E) = \cos^2\beta/a^2$ for $E$ level and perpendicular to it, and $0$ for the other perpendicular direction. So $K \ge 0$ holds with no positive lower bound, and the building indeed has infinite diameter along its lifts.

*Indefinite signature.* Along timelike geodesics the sign relation reverses, as the tidal formula shows, and Kulkarni's theorem rules out one-sided bounds on all planes except at constant curvature. Focusing of timelike and null congruences is governed instead by the Ricci term of the Raychaudhuri equation, which energy conditions bound.

**Takeaway:** Only planes containing a geodesic's direction steer its neighbours: upper bounds delay conjugate points, while a positive lower bound ends minimizing geodesics, bounds the diameter and forces compactness.

*What this leaves out:* Riemannian signature; the global statements need completeness.

*Continues:* `ways_in/tides-and-matter-read-planes`, `ways_in/planes-fix-the-curvature-tensor`<br>*Builds on:* [[geodesic-deviation-equation]]<br>*See:* `problems/refocusing-in-the-ball-building`

### 7. What signs on every plane force · research · structure

*Which theorems and open problems turn sign conditions on sectional curvature into topology or into rough-space definitions?*

The comparison theorems by which bounds steer geodesics open a programme that turns sign conditions on sectional curvature into topology.

*Nonpositive curvature.* A complete, simply connected manifold with $K \le 0$ is diffeomorphic to $\mathbb R^n$. A compact manifold with $K \le 0$ therefore has contractible universal cover, and its topology is governed by its fundamental group; when $K < 0$, Preissmann's theorem makes every nontrivial abelian subgroup infinite cyclic.

*Nonnegative curvature.* By the soul theorem of Cheeger and Gromoll, a complete noncompact manifold with $K \ge 0$ is diffeomorphic to the normal bundle of a compact totally geodesic submanifold, its soul. Gromov bounded the sum of the Betti numbers of a compact $n$-manifold with $K \ge 0$ by a constant depending only on $n$.

*Positive curvature.* Compact simply connected examples are scarce. Beyond the compact rank-one symmetric spaces, the known ones lie in dimensions 6, 7, 12, 13 and 24. Two questions of Hopf remain open: whether $S^2\times S^2$ carries a metric with $K > 0$, and whether every compact even-dimensional manifold with $K > 0$ has positive Euler characteristic. Much current work classifies positively curved manifolds with large isometry groups.

*Pinching.* A compact simply connected manifold with $1/4 < K \le 1$ is homeomorphic to a sphere, by work of Rauch, Berger and Klingenberg, and diffeomorphic to one, by Brendle and Schoen through Ricci flow. Complex projective space, with $1/4 \le K \le 1$, shows that the constant is sharp.

*Without smoothness.* A length space has curvature at least $k$ in Alexandrov's sense when its geodesic triangles are no thinner than comparison triangles on the surface of constant curvature $k$; for a Riemannian manifold this is $K \ge k$. With a dimension bound, such spaces are closed under Gromov–Hausdorff limits, and the structure theory of Burago, Gromov and Perelman describes those limits. Upper bounds give the CAT($k$) spaces.

*Indefinite signature.* Kulkarni's theorem makes a one-sided bound on all planes useless as a hypothesis in spacetime. Comparison theory instead bounds the numerator against the denominator, $\mathrm{Rm}(X,Y,X,Y) \ge k\,Q(X,Y)$, which bounds $K$ below on spacelike planes and above on timelike ones. Andersson and Howard proved comparison and rigidity theorems under such bounds. Lorentzian length spaces, introduced by Kunzinger and Sämann, define timelike curvature bounds by triangle comparison for spacetimes too rough to have a Riemann tensor.

**Takeaway:** Sign conditions on every plane constrain topology strongly, positive curvature most of all, and triangle comparison extends such bounds to rough spaces and, in reversed form, to spacetime.

*Continues:* `ways_in/bounds-on-planes-steer-geodesics`<br>*See:* `checks/hopf-product-claim`, `research_horizon/positive-curvature-and-topology`, `research_horizon/comparison-geometry-in-spacetime`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| tilt | — | The way a small flat piece is angled at a spot, set by two directions along that piece, like the bottom, front or side of a box. A tiny loop drawn in that piece has the same tilt. | — |
| playground length | — | The length a ring would have on flat ground: about 6.28 times the distance walked out from its centre. | [[circumference-to-radius-test]] |
| ring test | — | Pick one tilt at a spot. Walk straight out the same short distance from that spot, in every direction of that tilt, and mark where each walk ends. Then measure the ring through the marks, keeping to the surface the walks sweep out. On flat ground the ring comes out at its playground length. | [[circumference-to-radius-test]] |
| walk straight | — | To move without ever steering: not to the left, not to the right, and, where you can also rise or sink, not upward or downward either. | [[geodesic]] |
| matching ball | — | For a spot where small rings come out short, the ball on which a ring walked the same short distance from its centre falls short by the same fraction. | [[gaussian-curvature]] |
| Gaussian curvature | GOW-see-an | A number for each spot of a smooth surface. Where small rings come out short, find the matching ball, multiply its radius by itself and divide 1 by the result. It is zero where small rings come out at their playground length, and negative where they come out too long. | [[gaussian-curvature]] |
| sectional curvature | — | The number for how strongly space curves in one tilt at a spot. Run the ring test in that tilt, then turn the ring into a number exactly as for Gaussian curvature. | [[sectional-curvature]] |

## Key equations

### Sectional curvature of a plane · working

$$
K(\Pi) = \frac{R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma}{g(X,X)\,g(Y,Y) - g(X,Y)^2}
$$

The Riemann tensor fed the pair $X, Y$ twice, divided by the squared area of their parallelogram.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Pi$ | a plane in the tangent space at a point | the plane |
| $X,\ Y$ | any two vectors spanning $\Pi$ | the two spanning vectors |
| $R_{\mu\nu\rho\sigma}$ | Riemann tensor, course sign convention | the Riemann tensor |

**Holds when:** Levi-Civita connection; nonzero denominator; independent of the basis of $\Pi$. A sphere of radius $a$ has $K = +1/a^2$.  
**Say it:** “The sectional curvature is the Riemann tensor fed X, Y, X, Y, over the squared area on X and Y.”  
**Justified by:** `riemann-curvature-tensor`

### Small ring in a plane · working

$$
C(\ell) = 2\pi\ell\left(1 - \frac{K(\Pi)\,\ell^2}{6} + O(\ell^3)\right)
$$

A small geodesic circle in the surface of geodesics tangent to $\Pi$ falls short of the flat length by the fraction $K\ell^2/6$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C$ | length of the circle | the ring's length |
| $\ell$ | geodesic radius of the circle | the distance walked |

**Holds when:** Positive-definite metric; $\ell$ small compared with the curvature scale.  
**Say it:** “The ring's length is two pi ell, times one minus the plane's curvature times ell squared over six.”  
**Justified by:** `stated`

### Tides read a timelike plane · working

$$
\ddot\xi = +c^2K(u,e)\,\xi
$$

Relative acceleration of free-fall neighbours along $e$ is $c^2$ times the curvature of the plane of $u$ and $e$, times the separation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi$ | separation along the parallel-transported unit spatial vector $e \perp u$ | the separation |
| $u$ | four-velocity, $g(u,u) = -c^2$ | the four-velocity |
| $K(u,e)$ | sectional curvature of the timelike plane of $u$ and $e$ | the curvature of their plane |

**Holds when:** Neighbouring geodesics, small separation, $e$ parallel-transported along the worldline; positive $K$ means apart.  
**Say it:** “The separation's acceleration is c squared times the curvature of their plane, times the separation.”  
**Justified by:** `geodesic-deviation-equation`

### Energy density from three planes · working

$$
K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1) = \frac{8\pi G\rho}{c^2} + \Lambda
$$

For any observer, the curvatures of three perpendicular planes in her space add up to the energy density term plus the cosmological constant.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $e_1, e_2, e_3$ | orthonormal spatial vectors perpendicular to the observer's four-velocity | three perpendicular directions |
| $\rho$ | mass density the observer measures, energy density over $c^2$ | the density |
| $\Lambda$ | cosmological constant | lambda |

**Holds when:** Einstein's equation; spacetime sectional curvatures of planes orthogonal to the observer's four-velocity.  
**Say it:** “Three perpendicular spatial planes add up to eight pi G rho over c squared, plus lambda.”  
**Justified by:** `derivations/energy-density-from-three-planes`

### Recovering the tensor from planes · formal

$$
6\,\mathrm{Rm}(X,Y,Z,W) = \frac{\partial^2}{\partial x\,\partial y}\Big[B(X + xZ, Y + yW) - B(X + xW, Y + yZ)\Big]_{x=y=0}
$$

The values $B(X,Y) = \mathrm{Rm}(X,Y,X,Y)$, and hence the plane curvatures, determine the whole curvature tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $B(X,Y)$ | $\mathrm{Rm}(X,Y,X,Y)$, equal to $K\,Q(X,Y)$ on nondegenerate pairs | B of X and Y |
| $x,\ y$ | real parameters | x and y |

**Holds when:** Algebraic curvature tensor: both pair antisymmetries, pair exchange and the cyclic identity.  
**Say it:** “Six times the curvature tensor is a mixed second derivative of two plane values with swapped perturbations.”  
**Justified by:** `derivations/recover-the-tensor-from-planes`

### Planes steer neighbouring geodesics · formal

$$
g(J, J'') = -K(\dot\gamma, J)\,|J|^2
$$

A perpendicular Jacobi field is pulled back where its plane curves positively and pushed out where it curves negatively.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $J$ | Jacobi field perpendicular to $\dot\gamma$ | J |
| $\dot\gamma$ | unit tangent of the geodesic | gamma dot |

**Holds when:** Riemannian signature, unit speed, $J \perp \dot\gamma$.  
**Say it:** “J dotted with its second derivative is minus the curvature of their plane times J squared.”  
**Justified by:** `geodesic-deviation-equation`

## Derivations

### Energy density from three planes · working

**Goal:** Show that for a unit timelike $\hat u$ and orthonormal spatial $e_1, e_2, e_3$ perpendicular to it, $G_{\mu\nu}\hat u^\mu\hat u^\nu = K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1)$.

1. Write $e_0 = \hat u$ and $\epsilon_a = g(e_a,e_a)$, so $\epsilon_0 = -1$ and $\epsilon_i = +1$. For $a \ne b$ the denominator of $K(e_a,e_b)$ is $\epsilon_a\epsilon_b$, so $\mathrm{Rm}(e_a,e_b,e_a,e_b) = \epsilon_a\epsilon_bK(e_a,e_b)$.
2. The inverse metric is $g^{\mu\rho} = \sum_a\epsilon_ae_a^\mu e_a^\rho$, and the course Ricci tensor is $R_{\nu\sigma} = g^{\mu\rho}R_{\mu\nu\rho\sigma}$.
3. So $\mathrm{Ric}(e_b,e_b) = \sum_a\epsilon_a\mathrm{Rm}(e_a,e_b,e_a,e_b) = \epsilon_b\sum_{a\ne b}K(e_a,e_b)$, because $\epsilon_a^2 = 1$ and the $a = b$ term vanishes.
4. For $b = 0$: $\mathrm{Ric}(\hat u,\hat u) = -\big[K(e_0,e_1) + K(e_0,e_2) + K(e_0,e_3)\big]$.
5. The scalar is $R = \sum_b\epsilon_b\mathrm{Ric}(e_b,e_b) = \sum_b\sum_{a\ne b}K(e_a,e_b)$, which counts each of the six planes twice.
6. With $g(\hat u,\hat u) = -1$, $G_{\mu\nu}\hat u^\mu\hat u^\nu = \mathrm{Ric}(\hat u,\hat u) + \tfrac12R$.
7. The three planes containing $e_0$ enter with $-1$ from Ricci and $+1$ from $\tfrac12R$, and cancel; the three spatial planes enter only through $\tfrac12R$, with $+1$.
8. Einstein's equation $G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi GT_{\mu\nu}/c^4$ with $T_{\mu\nu}\hat u^\mu\hat u^\nu = \rho c^2$ gives $G_{\mu\nu}\hat u^\mu\hat u^\nu = 8\pi G\rho/c^2 + \Lambda$.

**Result:** $K(e_1,e_2) + K(e_2,e_3) + K(e_3,e_1) = G_{\mu\nu}\hat u^\mu\hat u^\nu = 8\pi G\rho/c^2 + \Lambda$.

### Recover the tensor from its planes · formal

**Goal:** Show that $B(X,Y) = \mathrm{Rm}(X,Y,X,Y)$ determines an algebraic curvature tensor.

1. Expand $B(X + xZ, Y + yW)$ by multilinearity. The coefficient of $xy$ collects the terms with one $Z$ and one $W$: $\mathrm{Rm}(Z,W,X,Y) + \mathrm{Rm}(Z,Y,X,W) + \mathrm{Rm}(X,W,Z,Y) + \mathrm{Rm}(X,Y,Z,W)$.
2. Pair exchange makes the first term equal the fourth and the second equal the third, so the coefficient is $2\mathrm{Rm}(X,Y,Z,W) + 2\mathrm{Rm}(X,W,Z,Y)$.
3. Swapping $Z$ and $W$, the coefficient of $xy$ in $B(X + xW, Y + yZ)$ is $2\mathrm{Rm}(X,Y,W,Z) + 2\mathrm{Rm}(X,Z,W,Y)$.
4. Subtract and use $\mathrm{Rm}(X,Y,W,Z) = -\mathrm{Rm}(X,Y,Z,W)$: the difference is $4\mathrm{Rm}(X,Y,Z,W) + 2\big[\mathrm{Rm}(X,W,Z,Y) - \mathrm{Rm}(X,Z,W,Y)\big]$.
5. Last-pair antisymmetry gives $\mathrm{Rm}(X,W,Z,Y) = -\mathrm{Rm}(X,W,Y,Z)$, and the cyclic identity $\mathrm{Rm}(X,Y,Z,W) + \mathrm{Rm}(X,Z,W,Y) + \mathrm{Rm}(X,W,Y,Z) = 0$ turns the bracket into $\mathrm{Rm}(X,Y,Z,W)$.
6. So the mixed derivative is $6\,\mathrm{Rm}(X,Y,Z,W)$.
7. On pairs with $Q(X,Y) \ne 0$, $B = K\,Q$ with $Q$ fixed by the metric. Such pairs are dense, so the plane curvatures fix $B$ everywhere by continuity, and with it $\mathrm{Rm}$.

**Result:** $6\,\mathrm{Rm}(X,Y,Z,W) = \partial_x\partial_y\big[B(X + xZ, Y + yW) - B(X + xW, Y + yZ)\big]_{x=y=0}$, so sectional curvatures on nondegenerate planes determine the curvature tensor.

## Worked examples

### A slanted plane in the ball building · working

**Problem:** The ball building has $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2) + dz^2$, with $z$ along the lifts. At a point, let $e_1, e_2$ be orthonormal along the floor and $e_3$ along the lift. Find $K$ for the plane spanned by $e_2$ and $X = \cos\alpha\,e_1 + \sin\alpha\,e_3$, and show that every plane at the point has this form.

1. The metric is a product of the floor sphere and a line, so its Levi-Civita connection is too, and every orthonormal Riemann component carrying an index $\hat 3$ vanishes.
2. The floor sphere contributes $R_{\hat 1\hat 2\hat 1\hat 2} = 1/a^2$, and the components related to it by the pair symmetries.
3. By multilinearity, $\mathrm{Rm}(X,e_2,X,e_2) = \cos^2\alpha\,R_{\hat 1\hat 2\hat 1\hat 2} = \cos^2\alpha/a^2$; the other terms carry an index $\hat 3$.
4. $X$ and $e_2$ are orthonormal, so the denominator is $1$ and $K = \cos^2\alpha/a^2$.
5. Any plane at the point meets the level plane in at least a line; choosing $e_2$ along that line and $e_1$ perpendicular to it in the level plane puts the plane in this form, with $\alpha$ its tilt from level.

**Answer:** $K = \cos^2\alpha/a^2$: $1/a^2$ for the level plane, $0$ for every plane containing the lift direction, and $1/(2a^2)$ at $\alpha = 45^\circ$.

**Takeaway:** At one point of the ball building the plane curvatures run from $0$ to $1/a^2$, set only by the plane's tilt from level.

## Problems

### `plane-curvatures-around-a-neutron-star` · working · difficulty 2 · calculation

Outside a non-rotating star of mass $M$, space at one moment, as observers at rest measure it, has $dl^2 = dr^2/(1 - 2GM/rc^2) + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$. With proper radial distance $s$ and $f = r$, a plane containing the radial direction has $K_{\rm up} = -f''/f$ and the level plane has $K_{\rm level} = (1 - f'^2)/f^2$, primes meaning $d/ds$. (a) Find both. (b) Show that three perpendicular planes add to zero. (c) Evaluate both at the surface of a neutron star of 1.4 solar masses and radius 12 km.

**Hints**

1. $f' = dr/ds = \sqrt{1 - 2GM/rc^2}$.
2. Differentiate $f'$ with respect to $s$ through $r$, using the chain rule.

**Answer:** $K_{\rm level} = +2GM/c^2r^3$ and $K_{\rm up} = -GM/c^2r^3$, which add as $2 - 1 - 1 = 0$. At the neutron star, $K_{\rm level} = +2.39\times10^{-9}$ m$^{-2}$ and $K_{\rm up} = -1.20\times10^{-9}$ m$^{-2}$.

**Must contain:** Level plane plus two G M over c squared r cubed; Planes containing the radius minus G M over c squared r cubed; Three perpendicular planes add to zero outside matter

**Numeric:** level plane curvature = 2.393e-09 m^-2 (signed, ±3%); upright plane curvature = -1.196e-09 m^-2 (signed, ±3%)

**Solution**

1. $f' = \sqrt{1 - 2GM/rc^2}$, so $1 - f'^2 = 2GM/rc^2$ and $K_{\rm level} = (2GM/rc^2)/r^2 = 2GM/c^2r^3$.
2. $f'' = \dfrac{df'}{dr}\dfrac{dr}{ds} = \dfrac{GM/c^2r^2}{\sqrt{1 - 2GM/rc^2}}\sqrt{1 - 2GM/rc^2} = GM/c^2r^2$, so $K_{\rm up} = -GM/c^2r^3$.
3. Three perpendicular planes at a point are the level plane and two planes containing the radius: $(2 - 1 - 1)\,GM/c^2r^3 = 0$. This slice has zero extrinsic curvature, so the energy-density sum applies to it, and it vanishes outside matter.
4. $GM_\odot/c^2 = 1476.6$ m, so $GM/c^2 = 2067$ m and $GM/c^2r^3 = 2067/(1.2\times10^4)^3 = 1.196\times10^{-9}$ m$^{-2}$.
5. So $K_{\rm level} = +2.39\times10^{-9}$ m$^{-2}$, the curvature of a sphere of radius 20.4 km, and $K_{\rm up} = -1.20\times10^{-9}$ m$^{-2}$.

**Targets:** `density-sets-each-plane`

### `refocusing-in-the-ball-building` · working · difficulty 2 · calculation

In the ball building with floor radius $a = 10$ m, two neighbouring geodesics leave a point together, rising at $\beta = 60^\circ$ above the floor, and at first separate along the level direction perpendicular to their motion. Treating the separation as a Jacobi field, where do they meet again? What happens if they separate at first along the other perpendicular direction?

**Hints**

1. Use the worked example on a slanted plane for the plane of the velocity and the separation.
2. Solve $j'' = -Kj$ with $j(0) = 0$.

**Answer:** They meet again after $\pi a/\cos\beta = 62.8$ m along the geodesic, having crossed $\pi a = 31.4$ m of floor to the point opposite the start and risen 54.4 m. Separated along the other perpendicular direction, their plane contains the lift direction, so $K = 0$ and they never meet.

**Must contain:** The plane's curvature is cos squared beta over a squared; They meet after 62.8 metres, halfway around the floor ball; The other direction spans a flat plane, so they never meet

**Numeric:** distance along the geodesic to the meeting point = 62.83 m (magnitude, ±1%)

**Solution**

1. The velocity is $\dot\gamma = \cos\beta\,h + \sin\beta\,e_3$ with $h$ level, and the level separation direction $E$ is perpendicular to both $h$ and $e_3$.
2. The worked example with $e_2 = E$, $e_1 = h$ and $\alpha = \beta$ gives $K(\dot\gamma,E) = \cos^2\beta/a^2 = 0.0025$ m$^{-2}$.
3. In the product, $\dot\gamma$ and $E$ stay parallel along the geodesic, so $J = jE$ obeys $j'' = -K(\dot\gamma,E)\,j$ with $j(0) = 0$.
4. So $j = j'(0)\,(a/\cos\beta)\sin(\ell\cos\beta/a)$, whose first zero is at $\ell = \pi a/\cos\beta = \pi\times10/0.5 = 62.8$ m.
5. The floor distance covered is $\ell\cos\beta = \pi a = 31.4$ m, half way around the floor ball, and the rise is $\ell\sin\beta = 54.4$ m.
6. The other perpendicular direction, $-\sin\beta\,h + \cos\beta\,e_3$, spans with $\dot\gamma$ the plane of $h$ and $e_3$, which contains the lift direction, so $K = 0$ and $j = j'(0)\,\ell$ never returns to zero.

### `einstein-spaces-pair-orthogonal-planes` · formal · difficulty 3 · proof

Let $(M,g)$ be four-dimensional, Riemannian or Lorentzian. Prove that $R_{\mu\nu} = \lambda g_{\mu\nu}$ holds exactly when $K(\Pi) = K(\Pi^\perp)$ for every nondegenerate plane $\Pi$. Check the result on the Schwarzschild values in a static orthonormal frame, with $G = c = 1$: $K(\hat t,\hat r) = K(\hat\theta,\hat\phi) = 2m/r^3$ and $K = -m/r^3$ for the other four coordinate planes.

**Hints**

1. A nondegenerate plane and its orthogonal plane together give an orthonormal basis of four vectors.
2. Use $S_b = \epsilon_b\,\mathrm{Ric}(e_b,e_b) = \sum_{a\ne b}K(e_a,e_b)$ from the derivation of energy density from three planes.

**Answer:** With $K_{ab} = K(e_a,e_b)$, $S_1 + S_2 - S_3 - S_4 = 2(K_{12} - K_{34})$. An Einstein metric has every $S_b = \lambda$, so $K_{12} = K_{34}$. Conversely, equal orthogonal pairs make all four $S_b$ equal in every orthonormal basis, which forces $\mathrm{Ric} = \lambda g$. Schwarzschild pairs $(\hat t\hat r, \hat\theta\hat\phi)$, $(\hat t\hat\theta, \hat r\hat\phi)$ and $(\hat t\hat\phi, \hat r\hat\theta)$ are equal, and each $S_b = 2 - 1 - 1 = 0$.

**Must contain:** S1 plus S2 minus S3 minus S4 equals twice K12 minus K34; Equal S values in every orthonormal basis force Ricci proportional to the metric; Schwarzschild has lambda equal to zero

**Solution**

1. A nondegenerate $\Pi$ has an orthonormal basis $e_1, e_2$; $\Pi^\perp$ is then nondegenerate with an orthonormal basis $e_3, e_4$, and together they form an orthonormal basis with signs $\epsilon_a = g(e_a,e_a)$.
2. The derivation of energy density from three planes gives $\mathrm{Ric}(e_b,e_b) = \epsilon_b\sum_{a\ne b}K_{ab}$ in any signature; write $S_b = \epsilon_b\mathrm{Ric}(e_b,e_b) = \sum_{a\ne b}K_{ab}$.
3. $S_1 + S_2 - S_3 - S_4 = (K_{12}+K_{13}+K_{14}) + (K_{12}+K_{23}+K_{24}) - (K_{13}+K_{23}+K_{34}) - (K_{14}+K_{24}+K_{34}) = 2K_{12} - 2K_{34}$.
4. If $\mathrm{Ric} = \lambda g$, then $S_b = \epsilon_b\lambda\epsilon_b = \lambda$ for every $b$, so $K_{12} = K_{34}$, that is $K(\Pi) = K(\Pi^\perp)$.
5. Conversely, if $K_{12} = K_{34}$, $K_{13} = K_{24}$ and $K_{14} = K_{23}$, each $S_b$ equals $K_{12} + K_{13} + K_{14}$. So $\mathrm{Ric}(e,e) = \lambda\,g(e,e)$ for every vector of every orthonormal basis; two unit vectors can always be joined through bases sharing a vector, so $\lambda$ is one number at the point.
6. Scaling gives $\mathrm{Ric}(v,v) = \lambda\,g(v,v)$ for every non-null $v$, continuity extends it to null $v$, and polarization gives $\mathrm{Ric} = \lambda g$.
7. Schwarzschild: $K(\hat t,\hat r) = K(\hat\theta,\hat\phi) = 2m/r^3$, $K(\hat t,\hat\theta) = K(\hat r,\hat\phi) = -m/r^3$ and $K(\hat t,\hat\phi) = K(\hat r,\hat\theta) = -m/r^3$. Each $S_b$ is $(2 - 1 - 1)\,m/r^3 = 0$, the vacuum case $\lambda = 0$.

## Observations

- **Gravity gradients measured by the GOCE satellite, 2009 to 2013** (measured, working). GOCE's gradiometer measured relative accelerations of test masses inside the freely falling satellite. Its radial entry, for masses separated along the line to Earth's centre, becomes through $\ddot\xi = c^2K(u,e)\,\xi$ the sectional curvature of the plane of the satellite's four-velocity and that line. The masses accelerate apart, so this plane has $K > 0$, the sign a sphere has, although on a sphere neighbours converge. *Numbers:* For a spherical Earth at $r = 6626$ km: $2GM/r^3 = 2.74\times10^{-6}$ s$^{-2}$ apart, so $K(u,e_r) = +3.05\times10^{-23}$ m$^{-2}$. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0 _(unverified)_
- **The curvature of space at one cosmic time, from the Planck satellite's maps combined with galaxy clustering** (measured, working). In the standard cosmological model each slice of constant cosmic time has the same sectional curvature for every plane at every point, $K = -\Omega_KH_0^2/c^2$ today in the slice's own geometry. The measurement bounds that one number. *Numbers:* $\Omega_K = 0.001 \pm 0.002$ at 68% confidence with $H_0 = 67.4$ km s$^{-1}$ Mpc$^{-1}$, so $K$ lies between $-1.6\times10^{-55}$ and $+5\times10^{-56}$ m$^{-2}$, against $2.5\times10^{-14}$ m$^{-2}$ for Earth's ground. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910 _(unverified)_

## Teaching arc

1. **Ask about tilts** (entry). Ask whether one small ring can say how curved space is at a spot where rings lie in many tilts. *Why:* It separates a spot from a tilt before any formula. *Uses:* `ways_in/two-rings-at-one-spot`
2. **Compare two tilts at one spot** (entry). In the ball building, have the learner predict the upright ring, then weigh the claim that it proves flatness. *Why:* Two rings at one spot make plane dependence visible. *Predict:* Will a small ring in an upright tilt come out short, like the ring along the floor? *Visual:* [[ring-in-each-tilt-of-the-ball-building]] *Uses:* `checks/upright-ring-length`, `ways_in/one-ring-does-not-settle-a-spot`, `checks/one-flat-ring`
3. **Compute a plane's curvature** (working). Write the definition, divide a sphere's coordinate component by its denominator, then tilt a plane. *Why:* The denominator is where component work goes wrong. *Uses:* `ways_in/one-formula-for-any-plane`, `checks/sphere-coordinate-component`, `worked_examples/slanted-plane-in-the-ball-building`
4. **Read planes in spacetime** (working). Relate tidal drift to timelike planes, flag the reversed sign, then add three spatial planes. *Why:* It ties the definition to measurement and to Einstein's equation. *Predict:* Test masses one above the other drift apart as they fall. Is the curvature of their plane positive or negative? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tides-and-matter-read-planes`, `checks/radial-pair-in-a-falling-cabin`, `checks/three-planes-in-water`
5. **Recover the tensor, then use bounds** (formal). Recover the tensor from plane values, test Schur's lemma and planes near a light cone, then use bounds. *Why:* It gives the theorem, its limits and its main use. *Uses:* `ways_in/planes-fix-the-curvature-tensor`, `checks/schur-on-a-surface`, `checks/planes-near-a-light-cone`, `ways_in/bounds-on-planes-steer-geodesics`
6. **Open the topology questions** (research). Evaluate the claim about the product of two spheres, then survey open problems. *Why:* Sign conditions on planes lead to unsolved problems. *Uses:* `ways_in/what-signs-on-every-plane-force`, `checks/hopf-product-claim`

## Misconceptions

### “Space at a spot is either curved or flat, so every small ring there comes out the same way.” · entry · `one-ring-settles-the-spot`

- **Why it is tempting:** On a surface one ring settles it, because a surface has one tilt per spot.
- **What is true:** Each tilt at a spot gives its own ring. In the ball building a ring in an upright tilt comes out at its playground length, while a ring in the level tilt comes out short.
- **Exposed by:** `checks/upright-ring-length`, `checks/one-flat-ring`

### “A component like R theta phi theta phi is the sectional curvature of that coordinate plane.” · working · `coordinate-component-is-k`

- **Why it is tempting:** In an orthonormal frame it is.
- **What is true:** In a coordinate basis it must be divided by the squared area of the basis vectors' parallelogram. On a sphere the component is a squared sine squared theta, but the curvature is one over a squared.
- **Exposed by:** `checks/sphere-coordinate-component`

### “Free-fall neighbours that accelerate apart span a negatively curved plane, as on a saddle.” · working · `spreading-means-negative`

- **Why it is tempting:** On surfaces, spreading geodesics mean negative curvature.
- **What is true:** A plane containing a timelike four-velocity has a negative denominator, which reverses the relation. Neighbours that accelerate apart have positive sectional curvature.
- **Exposed by:** `checks/radial-pair-in-a-falling-cabin`

### “Where matter is present, its density sets the curvature of every plane there.” · working · `density-sets-each-plane`

- **Why it is tempting:** Einstein's equation links curvature to density at the same place.
- **What is true:** Density fixes only the sum over three perpendicular planes in an observer's space. How that sum is shared depends on matter elsewhere.
- **Exposed by:** `checks/three-planes-in-water`

### “If every plane at each point has one curvature, it is the same everywhere, on a surface too.” · formal · `schur-holds-on-surfaces`

- **Why it is tempting:** Schur's lemma sounds like a statement about isotropy in any dimension.
- **What is true:** A surface has one plane per point, so the hypothesis says nothing. The contracted Bianchi step carries a factor that vanishes in two dimensions.
- **Exposed by:** `checks/schur-on-a-surface`

### “At one event the sectional curvatures of spacetime planes have a largest and a smallest value.” · formal · `spacetime-planes-are-bounded`

- **Why it is tempting:** In a positive-definite space the planes at a point form a compact set.
- **What is true:** Nondegenerate spacetime planes approach null planes, where the denominator vanishes while the numerator need not. So the values are unbounded unless the curvature is constant there.
- **Exposed by:** `checks/planes-near-a-light-cone`

### “A manifold whose usual metric has zero-curvature planes cannot carry any metric of positive curvature.” · research · `zero-planes-rule-out-positive`

- **Why it is tempting:** The curvature of the familiar metric looks like a property of the manifold.
- **What is true:** Sectional curvature belongs to a metric, not to the manifold. For the product of two 2-spheres the question is still open.
- **Exposed by:** `checks/hopf-product-claim`

## Checks

1. **Entry · predict** `checks/upright-ring-length`. In a made-up building, every floor is an exact copy of the surface of one ball 6 metres across. Lift shafts join each spot to its copies, and there is a floor at every height. At one spot you run the ring test in an upright tilt, walking 2 metres out. That tilt is set by the upward direction and one floor direction. About how long is the ring?
   - **Hints:** Which surface do the walks in an upright tilt keep to?
   - **Answer:** About 12.6 metres, its playground length, which is 6.28 times 2 metres. Every walk in an upright tilt rises or sinks steadily while heading along one floor direction, or its opposite. Every floor is an exact copy of the same ball. So at any height you can say which place on the ball you are at, and that place never steers as you walk. So every walk keeps to the lift shafts through one straight path around the ball. That is the path through your start along that floor direction. Those shafts make a tube, and a tube unrolls flat without stretching. On the unrolled sheet every mark still sits 2 metres from the centre, so the ring is an ordinary circle. A ring walked 2 metres out in the level tilt instead would stay on the floor, which is a ball's surface, so it would come out short, about 11.7 metres.
   - **Must contain:** About 12.6 metres, the playground length; The walks keep to a tube, which unrolls flat without stretching
   - **Numeric:** ring length = 12.57 m (magnitude, ±2%)
   - **Targets:** `one-ring-settles-the-spot`
   - **Visual:** [[ring-in-each-tilt-of-the-ball-building]]
2. **Entry · evaluate-claim** `checks/one-flat-ring`. In the building whose floors are copies of one ball's surface, a friend runs the ring test at a spot in an upright tilt. Her ring is 6.28 times the distance she walked. She says: "So space at this spot is flat." Is she right?
   - **Hints:** What happens to a ring in the level tilt there?
   - **Answer:** No. She tested only one tilt. Every height in the building is alike, so a straight walk gains the same height for each metre it covers. In the level tilt at her spot, every walk sets off gaining no height, so it never gains any. Those walks stay on the floor, and that floor is a ball's surface. So the level ring there comes out short, and the level tilt's sectional curvature is not zero. Space at a spot is flat exactly when every tilt there has sectional curvature zero. So her ring shows only that her upright tilt has sectional curvature zero.
   - **Must contain:** No, she tested only one tilt; The level ring at the same spot comes out short; Flat at a spot needs every tilt to give zero
   - **Targets:** `one-ring-settles-the-spot`
3. **Working · numeric** `checks/sphere-coordinate-component`. On a sphere of radius $a = 2$ m at $\theta = 30^\circ$, $R_{\theta\phi\theta\phi} = a^2\sin^2\theta = 1$ m$^2$. Using $X = \partial_\theta$ and $Y = \partial_\theta + \partial_\phi$, find $K$. Why is reading $K$ straight off the component wrong, and what if $g(X,Y)^2$ is dropped?
   - **Answer:** $\mathrm{Rm}(X,Y,X,Y) = R_{\theta\phi\theta\phi} = 1$ m$^2$, because the extra $\partial_\theta$ in $Y$ only adds terms with a repeated index in an antisymmetric pair. Then $g(X,X) = a^2 = 4$ m$^2$, $g(Y,Y) = a^2 + a^2\sin^2\theta = 5$ m$^2$ and $g(X,Y) = 4$ m$^2$, so the denominator is $20 - 16 = 4$ m$^4$ and $K = 0.25$ m$^{-2} = 1/a^2$. Reading $K$ off the component ignores that coordinate basis vectors are not unit vectors. Dropping $g(X,Y)^2$ gives $0.05$ m$^{-2}$, because it ignores that $X$ and $Y$ are not perpendicular.
   - **Must contain:** The denominator is 20 minus 16; K is 0.25 per square metre, one over a squared; Coordinate vectors are neither unit nor perpendicular
   - **Numeric:** sectional curvature = 0.25 m^-2 (signed, ±2%)
   - **Targets:** `coordinate-component-is-k`
4. **Working · numeric** `checks/radial-pair-in-a-falling-cabin`. Inside a freely falling cabin that does not rotate relative to distant stars, 400 km above a spherical Earth ($r = 6771$ km), two test masses float 10 m apart, one directly above the other. They accelerate apart at $2GM\xi/r^3$. What is the sectional curvature of the plane of their four-velocity and separation, with its sign? Compare with a sphere.
   - **Hints:** Evaluate $g(u,u)g(e,e) - g(u,e)^2$ first.
   - **Answer:** Contracting the deviation equation with the unit separation $e$ gives $\ddot\xi = -R_{\mu\nu\rho\sigma}e^\mu u^\nu e^\rho u^\sigma\,\xi$. With $g(u,u) = -c^2$, $g(e,e) = 1$ and $g(u,e) = 0$, the definition makes that numerator $-c^2K(u,e)$, so $\ddot\xi = c^2K\xi$. Here $\ddot\xi/\xi = 2GM/r^3 = 2.57\times10^{-6}$ s$^{-2}$, positive, so $K = 2GM/c^2r^3 = +2.86\times10^{-23}$ m$^{-2}$. On a sphere, positive $K$ makes geodesics converge; in a timelike plane the negative denominator makes positive $K$ mean the masses accelerate apart.
   - **Must contain:** Relative acceleration is c squared K times the separation; K is plus 2.9 times ten to the minus 23 per square metre; The timelike denominator reverses the sphere's relation
   - **Numeric:** sectional curvature of the plane = 2.857e-23 m^-2 (signed, ±3%)
   - **Targets:** `spreading-means-negative`
   - **Visual:** [[falling-ring-of-crumbs]]
5. **Working · numeric** `checks/three-planes-in-water`. A diver hangs at rest in a still lake of density 1000 kilograms per cubic metre. What is the sum of the sectional curvatures of any three perpendicular planes in the diver's space? Does the density also fix each single plane?
   - **Answer:** For the diver's unit four-velocity and orthonormal spatial directions, the three plane curvatures add up to $G_{\mu\nu}\hat u^\mu\hat u^\nu = 8\pi G\rho/c^2 + \Lambda$. With $\rho = 1000$ kg/m$^3$ this is $1.87\times10^{-23}$ m$^{-2}$, and $\Lambda = 1.1\times10^{-52}$ m$^{-2}$ changes nothing visible. The density does not fix single planes. Just above the lake the sum is essentially zero, yet Earth's mass gives the level plane about $+3.4\times10^{-23}$ m$^{-2}$ and each plane containing the vertical about $-1.7\times10^{-23}$ m$^{-2}$. How the sum is shared among single planes is set by matter elsewhere.
   - **Must contain:** The sum is 8 pi G rho over c squared plus lambda; About 1.9 times ten to the minus 23 per square metre; Matter elsewhere shares the sum among single planes
   - **Numeric:** sum of three plane curvatures = 1.866e-23 m^-2 (signed, ±3%)
   - **Targets:** `density-sets-each-plane`
   - **Visual:** [[three-rings-around-a-spot]]
6. **Formal · explain** `checks/schur-on-a-surface`. Schur's lemma says that a connected manifold of dimension $n \ge 3$ whose sectional curvature at each point is the same for all planes has constant curvature. An egg's surface has one value for all planes at each point, yet its curvature varies. Why is there no contradiction, and which step of the proof fails?
   - **Hints:** Compute the Einstein tensor of a constant-curvature form in dimension n.
   - **Answer:** A surface has one plane at each point, its tangent plane, so the hypothesis holds for every surface and carries no information. The proof writes $R_{\mu\nu\rho\sigma} = \bar K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$, so $R_{\mu\nu} = (n-1)\bar Kg_{\mu\nu}$, $R = n(n-1)\bar K$ and $G_{\mu\nu} = (n-1)(1 - n/2)\bar Kg_{\mu\nu}$. The contracted Bianchi identity $\nabla^\mu G_{\mu\nu} = 0$ then gives $(n-1)(1 - n/2)\,\partial_\nu\bar K = 0$. For $n \ge 3$ the factor is nonzero and $\bar K$ is constant; for $n = 2$ it vanishes, since the Einstein tensor of every surface is zero, and nothing is forced.
   - **Must contain:** A surface has only one plane per point; The contracted Bianchi identity gives a factor one minus n over two, which vanishes at n equal to two
   - **Targets:** `schur-holds-on-surfaces`
7. **Formal · numeric** `checks/planes-near-a-light-cone`. Outside a Schwarzschild mass, with $G = c = 1$, a static orthonormal frame has $K(\hat\phi,\hat t) = -m/r^3$, $K(\hat\phi,\hat\theta) = 2m/r^3$ and $R_{\hat\phi\hat t\hat\phi\hat\theta} = 0$. Find $K$ for the plane spanned by $e_{\hat\phi}$ and $Y = e_{\hat t} + w\,e_{\hat\theta}$, give its value at $w = 0.99$ in units of $m/r^3$, and explain why no one-sided bound on $K$ over all nondegenerate planes holds at this event.
   - **Hints:** What happens to $g(Y,Y)$ as $w \to 1$?
   - **Answer:** The numerator is $R_{\hat\phi\hat t\hat\phi\hat t} + w^2R_{\hat\phi\hat\theta\hat\phi\hat\theta} = m/r^3 + 2w^2m/r^3$, since $R_{\hat\phi\hat t\hat\phi\hat t} = K(\hat\phi,\hat t)\,g_{\hat\phi\hat\phi}g_{\hat t\hat t} = +m/r^3$. The denominator is $g(e_{\hat\phi},e_{\hat\phi})\,g(Y,Y) = w^2 - 1$. So $K = (m/r^3)(1 + 2w^2)/(w^2 - 1)$, which is $-149\,m/r^3$ at $w = 0.99$ and $+151\,m/r^3$ at $w = 1.01$. At $w = 1$ the plane contains the null vector $e_{\hat t} + e_{\hat\theta}$ and is degenerate, while the numerator stays $3m/r^3$, so $K$ runs to minus infinity from one side and plus infinity from the other. Kulkarni's theorem says this is general: a one-sided bound at an event forces constant curvature there, which Schwarzschild does not have.
   - **Must contain:** K is one plus two w squared, over w squared minus one; About minus 149 m over r cubed at w equal to 0.99; The numerator stays finite as the plane becomes null
   - **Numeric:** K in units of m over r cubed at w = 0.99 = -148.75 1 (signed, ±1%)
   - **Targets:** `spacetime-planes-are-bounded`
8. **Research · evaluate-claim** `checks/hopf-product-claim`. Evaluate: "With its product metric, $S^2\times S^2$ has planes of zero sectional curvature, those spanned by one vector tangent to each factor. So no metric on $S^2\times S^2$ has positive sectional curvature."
   - **Hints:** Does a curvature property of one metric pass to every metric on the manifold?
   - **Answer:** The premise is true: for $X$ tangent to one factor and $Y$ to the other, $\mathrm{Rm}(X,Y,X,Y) = 0$ in the product. The conclusion does not follow, because sectional curvature belongs to a metric and a different metric could make every plane positive. Whether one exists is Hopf's open problem. The known obstructions do not decide it: $S^2\times S^2$ is compact, orientable and simply connected, as Synge's theorem requires in even dimension; its fundamental group is finite, as Bonnet–Myers requires; its Euler characteristic is 4, positive; and its Betti numbers are small enough for Gromov's bound.
   - **Must contain:** Curvature belongs to the metric, not the manifold; Whether a positively curved metric exists is open; The known obstructions do not rule it out
   - **Targets:** `zero-planes-rule-out-positive`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign and slot order in the definition of sectional curvature | $K(X,Y) = R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma/\big(g(X,X)g(Y,Y) - g(X,Y)^2\big)$, so a sphere of radius $a$ has $K = +1/a^2$; for a timelike plane the denominator is negative. | Some texts swap the last two vectors in the numerator, because their Riemann tensor has the opposite sign; a sphere calibrates any formula. Some take the absolute value of the denominator, reversing the sign on timelike planes. |
| The letter K | $K$ is Gaussian or sectional curvature; the Kretschmann scalar is $\mathcal K$. | Some texts write $K$ for the Kretschmann scalar, a slice's mean extrinsic curvature, or the cosmological curvature constant. |

## Visuals

- ★ [[ring-in-each-tilt-of-the-ball-building]] (flagship): The entry picture made measurable: one ring per tilt at a single point. *Sketch:* The ball building drawn as a stack of identical ball-shaped floors threaded by lift lines. At one point the learner turns a handle to tilt a plane from level to upright and sets a string length. Straight walks in that plane sweep a small sheet, and the ring through their ends appears with readouts of its length, missing fraction and sectional curvature: $1/a^2$ level, $0$ upright, half at $45^\circ$. An unroll button lays the upright sheet flat.
- [[falling-ring-of-crumbs]] (supporting): Tidal drift read as the curvature of planes containing the four-velocity. *Sketch:* This concept adds a plane selector through the centre crumb: for each separation direction, a readout of the sectional curvature of the plane of fall and that direction, positive where crumbs drift apart and negative where they draw together.
- [[three-rings-around-a-spot]] (supporting): Single planes differ while three perpendicular planes keep a fixed sum. *Sketch:* This concept adds each ring's sectional curvature beside the sum, which stays zero as the cage turns, and a density slider that fills the space with matter and raises the sum to eight pi G rho over c squared.

## Tutor moves

**Open with**

- Picture a made-up building whose floors are all exact copies of one huge ball's surface, joined by lift shafts. At one spot, run the ring test in an upright tilt. That tilt is set by the upward direction and one floor direction. Will the ring come out shorter than its playground length? *(prediction)*

**If the learner is stuck**

- *The learner reads a coordinate component as the plane's curvature.* → Compute the sphere's component and its denominator side by side. *Uses:* `checks/sphere-coordinate-component`
- *The learner cannot decide the sign of a timelike plane.* → Write the denominator for the four-velocity and separation first, then contract the deviation equation. *Uses:* `checks/radial-pair-in-a-falling-cabin`
- *The learner cannot picture floors that copy one ball.* → Start from one globe, then add a copy of it just above, then a copy at every height, joined by lift shafts. *Uses:* `ways_in/two-rings-at-one-spot`

**Common questions**

- *What about a tilt halfway between level and upright?* (entry) Its ring comes out short, but less short than the level ring. In the level tilt the walks spread out over a patch of the ball. A ball draws neighbouring straight walks together, and that is what makes a ring come out short. Tilt the flat piece up from level, and the walks spread over a narrower patch. So they draw together less, and the ring gets closer to its playground length. Tilt all the way to upright, and the walks cover no patch at all. Their places on the ball all run along one straight path. *Uses:* `ways_in/two-rings-at-one-spot`, `worked_examples/slanted-plane-in-the-ball-building`
- *Why do singularity theorems bound Ricci curvature rather than sectional curvature?* (formal) Focusing of a congruence is driven by the Ricci term of the Raychaudhuri equation. In Lorentzian signature a one-sided bound on all sectional curvatures forces constant curvature, so that hypothesis would be useless. *Uses:* `ways_in/bounds-on-planes-steer-geodesics`, `checks/planes-near-a-light-cone`

**Switching levels**

- To working when: asks for a formula; uses Riemann components. Give the definition, then the coordinate-component check. *Uses:* `ways_in/one-formula-for-any-plane`, `checks/sphere-coordinate-component`
- To formal when: asks whether planes determine the tensor; knows the Bianchi identities. Recover the tensor from plane values, then state Schur's lemma and its Lorentzian limits. *Uses:* `ways_in/planes-fix-the-curvature-tensor`, `derivations/recover-the-tensor-from-planes`
- To research when: asks about sphere theorems, positive curvature or rough spacetimes. Open the research way and its horizon topics. *Uses:* `ways_in/what-signs-on-every-plane-force`, `research_horizon/positive-curvature-and-topology`

**Pronunciations:** Riemann → REE-mahn; Schur → SHOOR; Rauch → ROWK; Hadamard → ah-dah-MAR; Synge → SING; Kulkarni → kool-KAR-nee; Preissmann → PRICE-mahn; Alexandrov → al-ex-AHN-drof; Sämann → ZAY-mahn; Grassmannian → grahss-MAH-nee-an; Brendle → BREND-l

**Voice notes:** Say 'tilt' at the entry rung, 'plane' from the working rung on.

## History

- **Bernhard Riemann (1854).** In his 1854 inaugural lecture, published in 1868, described curvature at a point through the Gaussian curvatures of surfaces formed by geodesics leaving it along a surface direction, and counted $n(n-1)/2$ such functions as the metric data coordinates cannot remove. Bernhard Riemann (1868), *Über die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–150 _(unverified)_
- **Friedrich Schur (1886).** Proved that if the curvature at each point of a connected space of three or more dimensions is the same for all surface directions, it is the same at every point.
- **Harry Ernest Rauch (1951).** Compared Jacobi fields under bounds on sectional curvature, and used the comparison for the first pinching theorem: sufficiently pinched compact simply connected manifolds are homeomorphic to spheres. H. E. Rauch (1951), *A contribution to differential geometry in the large*, Annals of Mathematics 54, 38–55 _(unverified)_
- **Ravindra S. Kulkarni (1979).** Showed that for an indefinite metric in three or more dimensions, sectional curvature bounded on one side at a point must be constant there.

## Research horizon

- **Topology under positive or nonnegative sectional curvature.** The soul theorem reduces complete noncompact manifolds with $K \ge 0$ to bundles over compact souls. Compact positively curved examples are so rare that Hopf's questions about $S^2\times S^2$ and about Euler characteristics remain open, and current work classifies positively curved manifolds with large symmetry groups. Jeff Cheeger, Detlef Gromoll (1972), *On the structure of complete manifolds of nonnegative curvature*, Annals of Mathematics 96, 413–443 _(unverified)_; Burkhard Wilking (2007), *Nonnegatively and positively curved manifolds*, Surveys in Differential Geometry 11, 25–62 _(unverified)_
- **Pinched curvature and Ricci flow.** Pinching hypotheses bound the ratio of the largest to the smallest sectional curvature at each point. Ricci flow turned the topological quarter-pinched sphere theorem into a differentiable one, and the same machinery drives current work on weaker pinching and on which curvature conditions the flow preserves. Simon Brendle, Richard Schoen (2009), *Manifolds with 1/4-pinched curvature are space forms*, Journal of the American Mathematical Society 22, 287–307, doi:10.1090/S0894-0347-08-00613-9 _(unverified)_
- **Curvature bounds without smoothness.** Alexandrov spaces define a lower curvature bound by comparing geodesic triangles with triangles on a surface of constant curvature, which for smooth Riemannian manifolds is a lower bound on sectional curvature. Their structure theory describes Gromov–Hausdorff limits and collapse. Yuri Burago, Mikhail Gromov, Grigori Perelman (1992), *A. D. Alexandrov spaces with curvature bounded below*, Russian Mathematical Surveys 47(2), 1–58 _(unverified)_
- **Comparison geometry in spacetime.** Because one-sided bounds on all planes force constant curvature in indefinite signature, spacetime comparison theorems bound $\mathrm{Rm}(X,Y,X,Y)$ against $k\,Q(X,Y)$, a condition whose direction reverses between spacelike and timelike planes. Lorentzian length spaces carry timelike triangle comparison to spacetimes too rough for a Riemann tensor. Lars Andersson, Ralph Howard (1998), *Comparison and rigidity theorems in semi-Riemannian geometry*, Communications in Analysis and Geometry 6, 819–877 _(unverified)_; Michael Kunzinger, Clemens Sämann (2018), *Lorentzian length spaces*, Annals of Global Analysis and Geometry 54, 399–447, arXiv:1711.08990 _(unverified)_

## Review: novice

**Verdict:** fixed (2026-09-13, revision 2)

**Retell attempt:** There is a made-up building where every floor is the surface of the same huge ball, with lifts joining the copies of a spot. At one spot you pick a tilt, level like the bottom of a box or upright like the front, and do the ring test only in that tilt. Level comes out short, because you stay on the ball. Upright comes out normal length, because the walks stay on a tube and a tube unrolls flat. I had to reread the upright part: I cannot see why "that spot never steers", or how unrolling makes the ring exactly 6.28 times the walk. The ring test says walk out in every direction, but with three directions to move in that marks a whole ball of end points, not a ring, so I am not sure which walks count. Walking straight is "never changing how much height you gain with each step", which I could follow in the building but not on a hill. Each tilt gets its own number, the sectional curvature, and space is flat only if every tilt gives zero. Then something about real space: a level ring walked one kilometre out falls short by less than a thousandth of the width of an atom. But I just read that a one-kilometre ring on Earth's ground is short by about half a hair's width, so I do not know which is right, or whether I am walking on the ground or not. And "flat-paper length" is new to me; the earlier note called it the playground length.

**Stumbles (20)**

- “Where you can also rise, it means never changing how much height you gain with each step.”: This is offered as what walking straight means, but it is true only in the ball building. On real ground a straight walk does change its height gain, so the rule fails at this note's own real-space example.
- “The ring test: walk straight out the same short distance from a centre in every direction.”: With three directions to move in, walking out in every direction marks a whole ball of end points, not a ring. Nothing says the walks are limited to the tilt being tested.
- “Then measure the ring through the end marks.”: In three directions many closed lines run through the marks, and one that cuts across the space between them is shorter. No surface is named, so the test has no single answer.
- “On flat paper that ring is about 6.28 times the distance walked.”: The prerequisite notes already call this the playground length. A third name for one idea, and "flat" was already carrying the note's meaning of zero curvature.
- “Picture a building. Every floor is the whole surface of a huge ball, all copies of one ball.”: "All copies of one ball" made me reread: copies of the ball, or of each other? The building is also being built in the same breath as the idea the way is about.
- “A lift shaft joins each spot to its copy on every other floor, and there is a floor at every height.”: With a floor at every height there is nowhere to stand between floors, so I could not see how anyone walks upward at all. It is a rule I cannot follow.
- “Run the ring test in the level tilt. No walk gains height, so every walk stays on the floor, a ball's surface.”: No reason is given for why a walk that sets off level never gains height. I took it on trust.
- “So at each moment you stand at one spot of the ball, and that spot never steers.”: A spot cannot steer, and "spot" is already the note's word for a place in space, so one word does two jobs. I reread this twice.
- “So all the walks stay above the straight path around the ball through your start.”: Many straight paths run through the start, and the sentence never says which one. "Above" also leaves out the walks that sink.
- “That path, copied at every height, makes a tube, which unrolls flat without stretching. So this ring has its flat-paper length.”: The step from "unrolls without stretching" to "6.28 times the walk" is missing. The reader has to supply that the marks keep their distance from the centre, so they lie on an ordinary circle.
- “It stands for the sheet of an upright tilt. Tape a thread halfway around from the taped edge, and tie a pen 2 centimetres along it.”: "Sheet" is never defined, the thread's height on the tube is not given, and "it" could be the tube or the thread. I could not do this as written.
- “Turn each tilt's ring into a number, as for Gaussian curvature.”: The recipe has to be fetched from another note, and nothing says what a ring that comes out too long gives, which the same way needs three sentences later.
- “Just above the ground, a level ring walked one kilometre out falls short by less than a thousandth of the width of an atom.”: It reads as a ring walked on the ground, and the prerequisite says such a ring is short by about half a hair's width, ten orders of magnitude more. The straight walks of a level tilt do not keep to the ground.
- “Take space as people standing still on the ground measure it at one moment.”: "At one moment" never says by whose clocks, and the note is about to quote numbers measured in that space.
- “In such a tilt every walk spends part of each step rising or sinking, so it crosses less of the ball.”: False for the first what-if: a slanted tilt still holds one direction that is purely level, and a walk along it never rises. "Crosses the ball" also has no clear meaning.
- “How strongly space curves along one tilt at a single spot”: The note says "along one tilt" in the tagline, summary, objective and glossary, but "in the level tilt" in the ways. Two words for one idea.
- “A tilt between level and upright gives a ring between those two in length. There the walks do not stay on one sheet, so its ring gives that tilt's number only for very short walks.”: I reread "between those two in length", and "its" could be the tilt's or the sheet's. The reason is also not right: the walks of a slanted tilt do sweep out a surface.
- “Space at a spot is flat only when every tilt there has sectional curvature zero.”: "Only when" leaves open what does make a spot flat, which is exactly what the check asks about.
- “At one spot you run the ring test in an upright tilt, set by the upward direction and one floor direction, walking 2 metres out.”: One 35-word sentence, and the question never says there is a floor at every height, which the answer's own argument uses.
- “Run the ring test in an upright tilt, with walks that head along the floor while rising or sinking.”: "Head along the floor while rising" reads as a contradiction, and this is the tutor's first spoken line.

**Fixes**

- Redefined walking straight as never steering in any direction, and moved the steady height gain into the ball building as a fact with its reason (every height is alike).
- Restated the ring test so its walks are limited to one tilt, its end marks are marked, and its ring is measured on the surface the walks sweep out; the glossary entry now matches.
- Replaced "flat-paper length" with "playground length", the prerequisite's word, throughout the summary, ways, checks, objective, misconception and tutor moves, and added a glossary entry for it.
- Added "matching ball" to the glossary and made the Gaussian-curvature entry cover both the zero case and the negative case, which the second way now needs.
- Moved the ball building into the first way's recap and said in the explanation that a floor sits at every height, that you may move any way you like, and that any such trip counts as a walk.
- Gave the level ring its reason and the upright ring the missing unrolling step, in the way and in the check answer alike; replaced "that spot never steers" and "stay above the straight path" with wording that names the place on the ball and the one straight path.
- Rewrote the real-space paragraph so the level tilt's walks are said to rise away from the ground, which keeps the quoted shortfall from being read as a ring walked on Earth's surface, and named the clocks that fix the moment.
- Rewrote the halfway-tilt common question, whose reason was false for the level direction inside a slanted tilt, in terms of the patch of ball the walks spread over.
- Strengthened "flat only when" to "flat exactly when" in the way, the takeaway and the check, since the formal way's determination result backs the converse.
- Split every over-long sentence in the summary, recaps, entry checks and the opening question; the validator now reports no sentence-length or wording warnings.
- One working-rung clarity fix: "the lift direction is flat" became "the metric is a product: the floor is a sphere of radius $a$, and the lift direction contributes a flat line".
- Dropped nothing. Entry explanations stand at 436 words against the 400 cap, inside the review's 10% allowance, and every added word pays for one of the stumbles above.

**Concerns**

- Budget headroom is gone. Entry is 436 of the 440 allowance, extras 732 of the 800 cap and tutoring 3014 of the 3500 cap, so the validator's 80% draft warnings stand and a later re-read has almost no room at the entry rung. If an editor needs room, the lowest-value entry item is the real-space paragraph of "One ring does not settle a spot" (about 80 words); moving it to a book sidebar would cost the note its answer to "why don't I notice this?", so it should not be cut silently.
- Physics reviewer: I strengthened "space at a spot is flat only when every tilt gives zero" to "exactly when". Confirm the converse at the entry rung (all sectional curvatures zero implies the Riemann tensor vanishes there), which the formal way's determination result supplies.
- Physics reviewer: confirm the new real-space sentences. A spatial geodesic of the static slice that sets off tangent to a sphere of constant radius has that radius as a minimum, so it rises away from the ground; with K = 2GM/c^2r^3 at Earth's surface and a 1 km walk the shortfall is pi K l^3/3 = 3.6e-14 m, under a thousandth of an atom's width, and the upright ring's excess is half that because |K_up| = K_level/2.
- Physics reviewer: every reference still carries verified: false, as the writer left them. Schur 1886 and Kulkarni 1979 deliberately carry work: null.
- The writer's conventions gap is still open: course-conventions.md fixes the index-form Riemann tensor but not the index-free curvature slot order, so the formal way defines Rm(X,Y,Z,W) inside itself. The conventions file should adopt that definition before other notes need it.
- analogies is empty. The writer drafted a formal-rung moment-of-inertia analogy and dropped it for budget; there is now no room to restore it either.
- The registry lists only gaussian-curvature and riemann-curvature-tensor as prerequisites; the note adds geodesic-deviation-equation at the working rung, which sync_registry.py should pick up now that the note is reviewed.
- All three visuals are proposals, not catalog entries. ring-in-each-tilt-of-the-ball-building is new to this note; falling-ring-of-crumbs and three-rings-around-a-spot are proposed by other curvature notes and this note only adds a mode to each.
- A schema v2 note at revision 2, status novice-reviewed, existed before the writer stage was rerun, and its review record was lost in the rebuild. This review reads the rerun draft from scratch. The earlier files are at /private/tmp/claude-501/-Users-neo-repos-general-relativity/bdf94c63-cbec-4edd-ba4c-fe7299d5507b/scratchpad/snapshots/notes-curvature/sectional-curvature.before.json and .before-writer-rerun2.json, and this stage's own starting point at sectional-curvature.before-novice.json.
