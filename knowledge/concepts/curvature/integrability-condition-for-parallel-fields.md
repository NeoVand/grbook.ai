---
type: "concept"
schema_version: 2
id: "integrability-condition-for-parallel-fields"
title: "Integrability condition for parallel fields"
tagline: "When arrows can be painted so that every carried copy lands on a matching arrow"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 4
updated: "2026-09-13"
aliases: ["condition for a globally parallel vector field", "integrable connection condition"]
prerequisites: ["ricci-identity", "partial-derivative", "geodesic-deviation-equation", "holonomy", "lie-bracket", "simply-connected-space"]
leads_to: ["flatness-criterion", "brinkmann-coordinates", "exact-plane-gravitational-wave"]
visuals: ["painted-arrows-that-must-match", "falling-ring-of-crumbs", "paper-cone-with-a-missing-wedge"]
---

# Integrability condition for parallel fields

*When arrows can be painted so that every carried copy lands on a matching arrow*

`integrability-condition-for-parallel-fields` · curvature · advanced · physics-reviewed (revision 4)

**Needs:** [[ricci-identity]] (entry) · [[partial-derivative]] (working) · [[geodesic-deviation-equation]] (working) · [[holonomy]] (formal) · [[lie-bracket]] (formal) · [[simply-connected-space]] (formal)  
**Opens:** [[flatness-criterion]] · [[brinkmann-coordinates]] · [[exact-plane-gravitational-wave]]  
**Related:** [[poincare-lemma]] · [[killing-vector-ricci-identity]] · [[torsion-tensor]] · [[gauge-parallel-transport]] · [[local-geometry-versus-global-topology]]  
**Visuals:** ★ [[painted-arrows-that-must-match]] · [[falling-ring-of-crumbs]] · [[paper-cone-with-a-missing-wedge]]

> Picture an arrow painted on every spot of the ground. Lay a cardboard copy on top of one of them, pointing the same way, and carry it anywhere, never letting it swing to your left or right. The painting is perfect if the copy always lands on the arrow painted where it stops. Flat ground allows a perfect painting. A ball allows none, even on a tiny patch, because a small loop there turns a carried copy. Every small loop must bring copies back matching: that is the integrability condition.

## You will be able to

**Entry**
- Explain why a perfect painting of arrows exists on flat ground but on no patch of a ball, and test a proposed painting with a loop. `objectives/explain-why-a-ball-cannot-be-painted` ← `checks/compass-painting`, `checks/equator-loop-matches`, `checks/tiny-patch-on-earth`, `problems/two-routes-to-one-spot`

**Working**
- Derive the integrability condition from the equality of mixed partial derivatives, and apply it to a surface. `objectives/derive-the-condition` ← `problems/surface-of-revolution`, `checks/cap-has-no-parallel-field`, `checks/polar-plane-field`
- Use a measured tidal gradient to decide whether a four-velocity extends to a parallel field. `objectives/read-tides-as-a-failed-condition` ← `problems/gradiometer-verdict`

**Formal**
- State when curvature conditions guarantee parallel sections, and give a counterexample for each missing hypothesis. `objectives/state-when-the-condition-suffices` ← `checks/flat-at-one-point`, `checks/mobius-and-cylinder`
- Show that a plane-fronted wave carries a parallel null field, and test other candidates with the condition. `objectives/test-fields-on-a-plane-wave` ← `problems/brinkmann-wave-fields`

**Research**
- Use the holonomy principle to decide which parallel fields and forms a manifold carries. `objectives/use-the-holonomy-principle` ← `checks/reducible-without-parallel-vector`

## Ways in

### 1. Paint an arrow on every spot · entry · picture

*Can arrows be painted on a patch of a ball so that every carried copy matches the arrow painted where it stops?*

**Recap:** The arrow test: press a cardboard arrow against the ground and carry it along a path. Never let the arrow swing to your left or right. On flat ground, such as a floor or a car park, a carried arrow keeps pointing the same way the whole time. A loop is a path that ends where it began. On flat ground an arrow comes back from any loop matching its start. On a ball, walk a small loop keeping a piece of the ball on your left. Then the arrow comes back turned a little toward your left. One trip turns every arrow by the same amount, whichever way the arrow pointed.

A groundskeeper paints an arrow on every spot of a huge, flat car park. She calls her painting perfect if it passes one test. Take a cardboard arrow and lay it on any painted arrow, so that it lies on top and points the same way. A cardboard arrow used like this is called a copy.

Now carry the copy along any path, never letting it swing to your left or right. Wherever you stop, the copy should lie on top of the arrow painted there, pointing the same way. That is what matching means. Her painting is perfect if every carried copy matches in this way, wherever it stops.

On the car park the job is easy. She paints every arrow parallel to one straight edge of the car park, all pointing the same way. On flat ground a carried copy keeps pointing the same way, so it keeps its angle to that edge and matches every arrow it reaches. A perfect painting is also called a parallel field. The name comes from the carrying test, not from the arrows looking parallel: a ball has no edge to line all its arrows up with.

Now give her a patch of a huge round ball to paint, and suppose for a moment that she has succeeded. Draw a small loop in the patch, and walk it keeping a piece of the ball on your left. Lay a copy on the arrow painted where the loop starts, and carry the copy once around. Her painting is perfect, so the copy matches a painted arrow at every step. Back at the start it must therefore match the arrow it set out on. But on a ball that loop brings every carried arrow back turned a little toward your left. The two answers disagree, so she cannot have succeeded.

Shrinking the patch does not save her. However small a patch is, it holds a smaller loop, and that loop turns a carried copy too. The smaller loop turns it less, because the turn shrinks in proportion to the area of the piece of ball on your left. It never shrinks to nothing.

So a perfect painting needs every small loop to bring carried copies back matching. That demand is called the integrability condition. Flat ground meets it, and a ball fails it on every patch.

On Earth, ignoring hills, a loop around one square kilometre of ground turns a carried copy by about 1.4 millionths of a degree. That is the angle a hair's width makes at 3 kilometres, far too small to notice.

**Takeaway:** On flat ground, arrows can be painted so that every carried copy matches the arrow painted where it stops. On a patch of a ball no such painting exists, because small loops there bring carried copies back turned.

*Tutor opener:* Picture painting an arrow at every spot of a flat car park. Lay a copy on one of them and carry it anywhere, never letting it swing to your left or right. A perfect painting leaves the copy on the arrow painted where you stop, pointing the same way. Could you do that on a huge round ball?<br>*Visuals:* [[painted-arrows-that-must-match]]<br>*See:* `checks/tiny-patch-on-earth`, `problems/two-routes-to-one-spot`

### 2. Mixed partials pin the curvature to the field · working · calculation

*What equation must the curvature satisfy wherever a parallel vector field exists?*

The perfect painting of "Paint an arrow on every spot" is a vector field $V^\rho(x)$ whose carried copies match it everywhere. Matching every carried copy means $V$ is parallel along every curve, so $\dot x^\nu\nabla_\nu V^\rho = 0$ for every tangent $\dot x^\nu$, which is

$$\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma = 0.$$

In $n$ dimensions these are $n^2$ equations, one for each pair $\nu\rho$, for the $n$ unknown functions $V^\rho$, so the system is overdetermined. It fixes every first derivative, $\partial_\nu V^\rho = -\Gamma^\rho{}_{\nu\sigma}V^\sigma$, and the second derivatives it then implies must agree with each other.

That agreement is the loop test in components. Walking a tiny coordinate rectangle, first along $x^\mu$ and then along $x^\nu$ or the other way round, compares two orders of differentiation, so the loop test asks whether the mixed partial derivatives of $V$ agree.

The derivation "Mixed partials give curvature" differentiates the first-derivative rule once more and substitutes it into itself:

$$\partial_\mu\partial_\nu V^\rho - \partial_\nu\partial_\mu V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma.$$

A connection with continuous first derivatives makes a solution twice continuously differentiable, so its mixed partial derivatives agree and the left side vanishes. A parallel field must therefore satisfy the integrability condition

$$R^\rho{}_{\sigma\mu\nu}\,V^\sigma = 0.$$

The Ricci identity reaches the same place in one line, because $\nabla V = 0$ kills $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$. The route through partial derivatives uses no symmetry of $\Gamma$, so the condition holds for any affine connection.

Read it as linear algebra at each point: for each pair $\mu\nu$, the matrix $R^\rho{}_{\sigma\mu\nu}$ must annihilate $V$.

- A parallel frame, meaning $n$ independent parallel fields, needs every such matrix to vanish, so $R^\rho{}_{\sigma\mu\nu} = 0$.
- On a surface, taking on trust $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, the condition reads $K(\delta^\rho{}_\mu V_\nu - \delta^\rho{}_\nu V_\mu) = 0$ in any basis. Choosing $\rho = \mu = 1$, $\nu = 2$ gives $KV_2 = 0$, and $\rho = \nu = 2$, $\mu = 1$ gives $KV_1 = 0$. For the Levi-Civita connection $\nabla V = 0$ also keeps $g(V,V)$ constant, so on a connected region a field that is nonzero anywhere is nonzero everywhere, and then $K = 0$ throughout. A round sphere of radius $a$, with $K = 1/a^2$, has no nonzero parallel field on any open set.
- In four dimensions a single field can survive nonzero curvature, provided the curvature annihilates it. The parallel null field of a plane-fronted gravitational wave does exactly that.

The condition is necessary; the converse needs more. If $R^\rho{}_{\sigma\mu\nu} = 0$ throughout a simply connected region, one in which every loop can be shrunk to a point, then a parallel field passes through every vector at a point. That is taken on trust here and sketched in "When flatness is enough".

**Takeaway:** Requiring the mixed partial derivatives of a parallel field to agree forces the curvature to annihilate it; a full parallel frame needs zero curvature, and on a surface even one field needs zero Gaussian curvature.

*What this leaves out:* One coordinate chart, and a connection whose coefficients have continuous first derivatives.

*Continues:* `ways_in/paint-an-arrow-on-every-spot`<br>*Builds on:* [[ricci-identity]], [[partial-derivative]]<br>*Visuals:* [[painted-arrows-that-must-match]]<br>*See:* `derivations/mixed-partials-give-curvature`, `checks/polar-plane-field`, `problems/surface-of-revolution`, `worked_examples/parallel-field-on-a-cone`

### 3. Tides rule out a parallel four-velocity · working · operational

*How does a measurement near Earth show that freely falling observers carry no parallel four-velocity field?*

"Mixed partials pin the curvature to the field" left a condition on the curvature. It becomes a laboratory reading when the field is a family of observers' four-velocity $u^\mu$. Suppose $\nabla_\nu u^\mu = 0$. Then $u^\nu\nabla_\nu u^\mu = 0$, so every observer in the family falls freely, and the integrability condition gives $R^\mu{}_{\nu\rho\sigma}u^\nu = 0$. The geodesic deviation equation, taken on trust here,

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,$$

then returns zero relative acceleration for every separation $\xi$. A parallel four-velocity field means no tides.

Flat spacetime has one. The observers at rest in an inertial frame have $u^\mu = (c,0,0,0)$ in its Cartesian coordinates, where every $\Gamma$ vanishes, so $u$ is parallel.

Near Earth the condition fails, and a measurement says so. In the rest frame of a freely falling laboratory, $u^\mu = (c,0,0,0)$, and for a static spherical Earth the vertical tidal entry is $-c^2R^z{}_{0z0} = 2GM/r^3$. At the surface, with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and $r = 6.371\times10^6$ m, that is $3.08\times10^{-6}\ \mathrm{s^{-2}}$: two test masses 1 m apart along the vertical separate with a relative acceleration of 3.1 micrometres per second squared. An atom-interferometer gradiometer reads this by comparing two freely falling clouds of atoms. A nonzero reading means $R^z{}_{0z0} \neq 0$, hence $R^\mu{}_{\nu\rho\sigma}u^\nu \neq 0$, so the laboratory's four-velocity at that event is the value of no parallel field, on however small a neighbourhood.

One accelerometer riding with the laboratory cannot make this test, because it reads zero in free fall. The condition involves curvature, and curvature shows itself only when neighbouring free-fall paths are compared.

**Takeaway:** A parallel four-velocity field would leave neighbouring freely falling observers with no tides, so a measured gravity gradient shows that the measuring laboratory's four-velocity extends to no parallel field.

*What this leaves out:* Earth is treated as a static sphere; its rotation, its shape and nearby masses change the measured gradient slightly.

*Continues:* `ways_in/mixed-partials-pin-the-curvature-to-the-field`<br>*Builds on:* [[geodesic-deviation-equation]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `observations/atom-gradiometer`, `problems/gradiometer-verdict`

### 4. When flatness is enough · formal · structure

*Exactly when do curvature conditions guarantee parallel sections, through every vector or through one chosen vector?*

The condition of "Mixed partials pin the curvature to the field" is necessary. Frobenius's theorem decides when a curvature condition is also sufficient.

Let $\nabla$ be a connection on a smooth vector bundle $E \to M$, for instance $TM$, with curvature $\mathcal R(X,Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]}$, whose components on $TM$ are $R^\rho{}_{\sigma\mu\nu}$. A section $s$ is parallel on an open set $U$ when $\nabla s = 0$ there.

*Necessity, to all orders.* If $\nabla s = 0$ on $U$, then $\mathcal R(X,Y)s = 0$; differentiating and using $\nabla s = 0$ again gives $(\nabla^m\mathcal R)(Z_1,\dots,Z_m;X,Y)\,s = 0$ for every $m \ge 0$. The algebraic condition at a point is only the first of an infinite family.

*Full integrability.* For connected $U$ the following are equivalent: (a) $\mathcal R = 0$ on $U$; (b) through every $v \in E_p$, $p \in U$, passes a parallel section defined near $p$; (c) the restricted holonomy group $\mathrm{Hol}^0_p(U)$ is trivial. Sketch of (a) implies (b): in a local trivialization with fibre coordinates $v^\rho$, the horizontal lifts $H_\mu = \partial_\mu - \Gamma^\rho{}_{\mu\sigma}v^\sigma\,\partial/\partial v^\rho$ span a distribution whose integral curves are the transported vectors, and "Horizontal lifts and their bracket" gives $[H_\mu,H_\nu] = -R^\rho{}_{\sigma\mu\nu}v^\sigma\,\partial/\partial v^\rho$. That field is vertical, so the distribution is involutive exactly when $\mathcal R = 0$; Frobenius then supplies integral manifolds through each $(p,v)$, transverse to the fibres and horizontal, hence local graphs of parallel sections. For (b) implies (a), apply necessity to a local frame of parallel sections; (a) is equivalent to (c) by the Ambrose–Singer theorem. If $U$ is simply connected, $\mathrm{Hol}_p(U) = \mathrm{Hol}^0_p(U)$, transport is path-independent, and parallel sections trivialize $E|_U$.

*One chosen vector.* On connected $U$, a vector $v \in E_p$ extends to a parallel section on $U$ exactly when $\mathrm{Hol}_p(U)$ fixes $v$; the extension is $s(q) = P_\gamma v$ along any path $\gamma$ from $p$ to $q$. On simply connected $U$ this says that the holonomy algebra annihilates $v$, and Ambrose-Singer spans that algebra by curvature endomorphisms at all points of $U$, carried back to $p$.

*Analytic against smooth.* For real-analytic data the algebra is spanned by the values at $p$ of $\nabla^m\mathcal R$ for all $m$, so the necessary conditions at one point become sufficient. For smooth data they do not. The surface $dx^2 + G(x)^2dy^2$ with $G = 1$ for $x \le 0$ and $G = 1 + e^{-1/x}$ for $x > 0$ has $\nabla^m\mathcal R = 0$ at every point with $x \le 0$, yet $K = -G''/G$ is nonzero for small $x > 0$, and a parallel field forces $K = 0$ wherever it lives, so none exists on a strip reaching into $x > 0$.

*Limits.* Everything here is local, or else needs simple connectivity. "What topology and torsion each add" pins each remaining hypothesis to its job.

**Takeaway:** Zero curvature makes the horizontal distribution involutive, so Frobenius gives parallel sections through every vector, globally on simply connected sets; one chosen vector extends exactly when holonomy fixes it.

*Picture:* A bundle drawn as fibres over a base, with horizontal planes that stack into sheets exactly when their brackets vanish; each sheet is the graph of a parallel section.

*What this leaves out:* Smooth connections on finite-rank vector bundles.

*Continues:* `ways_in/mixed-partials-pin-the-curvature-to-the-field`<br>*Builds on:* [[lie-bracket]], [[holonomy]], [[simply-connected-space]]<br>*See:* `derivations/horizontal-lifts-bracket`, `checks/flat-at-one-point`

### 5. What topology and torsion each add · formal · contrast

*What do simple connectivity and zero torsion each contribute to a connection with zero curvature?*

"When flatness is enough" settled flat connections on simply connected sets, where parallel sections trivialize the bundle. Two contrasts show what each remaining hypothesis does.

*Topology.* Keep $\mathcal R = 0$ and drop simple connectivity. Parallel fields still exist near every point, but a global one through $v$ needs $\mathrm{Hol}_p v = v$, and now the loops that cannot be shrunk contribute.

- A flat cylinder has trivial holonomy, so every vector extends. Simple connectivity is sufficient, not necessary.
- A flat Möbius band has holonomy $\{1,\sigma\}$, with $\sigma$ the reflection reversing the direction across the band. Vectors along the band extend; vectors across it do not.
- A flat cone with its tip removed, made by cutting a wedge of angle $\delta$ with $0 < \delta < 2\pi$ from a sheet, has holonomy generated by the rotation through $\delta$, which fixes no nonzero vector. No global parallel field exists, although one does on the cone slit along a ray from the tip.

*Torsion.* Frobenius never used a symmetric connection. Let $\mathcal R = 0$ on a simply connected $U$, and take a parallel frame $e_a$ with dual coframe $\theta^a$. The torsion $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$ gives $T(e_a,e_b) = -[e_a,e_b]$, and since $\theta^a(e_b)$ is constant, $d\theta^a(e_b,e_c) = -\theta^a([e_b,e_c]) = \theta^a(T(e_b,e_c))$.

- If $T = 0$, every $\theta^a$ is closed, hence locally $dx^a$ by the Poincaré lemma. In those coordinates the coordinate fields are the parallel $e_a$, so every connection coefficient vanishes.
- If $T \neq 0$, the parallel frame still exists, but its fields do not commute and no coordinates make $\Gamma = 0$. Declaring a non-commuting frame parallel defines such a connection, the Weitzenböck connection of teleparallel formulations of gravity.

For the Levi-Civita connection, $T = 0$ and $\nabla g = 0$ keep $g(e_a,e_b)$ constant, so in those coordinates the metric components are constant. That is the flatness criterion.

**Takeaway:** Without simple connectivity a flat connection has parallel fields only through holonomy-fixed vectors; with torsion it has a parallel frame but no coordinates in which it vanishes.

*What this leaves out:* Surfaces idealized as exactly flat, with the cone's tip removed.

*Continues:* `ways_in/when-flatness-is-enough`<br>*Builds on:* [[holonomy]], [[simply-connected-space]]<br>*Visuals:* [[paper-cone-with-a-missing-wedge]]<br>*See:* `checks/mobius-and-cylinder`, `worked_examples/parallel-field-on-a-cone`

### 6. Parallel tensors and special holonomy · research · structure

*Which parallel objects can a manifold or a spacetime carry, and what do they force on its geometry?*

"When flatness is enough" showed that a vector extends to a parallel section exactly when holonomy fixes it. The same argument runs on every bundle built from $TM$, which gives the holonomy principle: on a connected manifold, parallel tensor fields correspond one to one with tensors at $p$ fixed by $\mathrm{Hol}_p$. Through Ambrose-Singer, integrability conditions become statements about which subgroups of $O(g_p)$ can occur.

- *Splitting.* On a Riemannian manifold a subspace invariant under $\mathrm{Hol}_p$ spreads into a parallel distribution, and so does its orthogonal complement. De Rham's theorem then makes a complete, simply connected Riemannian manifold with reducible holonomy an isometric product. For such a manifold a nonzero parallel vector field is the case of a fixed vector, and it splits off a line, $M \cong \mathbb R \times N$; without completeness the splitting is only local.
- *Special holonomy.* Berger's list of the holonomy groups of irreducible, non-locally-symmetric Riemannian manifolds is a list of parallel objects: a Kähler form for $U(m)$, and parallel spinors for $SU(m)$, $Sp(m)$, $G_2$ and $\mathrm{Spin}(7)$. The integrability condition of a parallel spinor forces a Riemannian metric to be Ricci-flat, which is why these geometries serve as supersymmetric compactifications in string and M-theory.
- *Lorentzian signature.* De Rham splitting needs nondegenerate invariant subspaces, and Lorentzian holonomy can be reducible without being decomposable. A parallel null vector $k$ spans a degenerate invariant line; the four-dimensional vacuum spacetimes carrying one are the pp-waves, $ds^2 = H(u,x,y)\,du^2 + 2\,du\,dv + dx^2 + dy^2$ with $k = \partial_v$ and $(\partial_x^2 + \partial_y^2)H = 0$. A parallel timelike vector instead splits spacetime locally as $ds^2 = -dt^2 + h$, with no tidal field along $\partial_t$.
- *Teleparallelism.* On a parallelizable spacetime, declaring a global orthonormal frame parallel gives a curvature-free metric connection, with torsion unless the frame fields commute. It underlies distant parallelism and the teleparallel equivalent of general relativity.

Open questions remain. Whether every compact, simply connected Ricci-flat Riemannian manifold has holonomy smaller than $SO(n)$, and so carries a parallel spinor or form, is unknown; every known example does.

**Takeaway:** Parallel tensors and spinors are exactly the holonomy-invariant ones; they split Riemannian products, define the special geometries and the pp-waves, and their integrability conditions constrain curvature.

*Continues:* `ways_in/when-flatness-is-enough`<br>*Builds on:* [[holonomy]]<br>*See:* `research_horizon/special-holonomy-and-parallel-spinors`, `research_horizon/parallel-null-vectors-and-pp-waves`, `checks/reducible-without-parallel-vector`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way an arrow points, left or right, while it lies against the ground. A carried arrow never swings. | — |
| match | — | A carried copy matches a painted arrow when it lies on top of that arrow, pointing the same way. | — |
| copy | — | A cardboard arrow laid on top of a painted arrow, pointing the same way, and then carried without swinging. | — |
| perfect painting | — | A painting of an arrow on every spot that passes the carrying test: a copy carried anywhere, without swinging, matches the arrow painted where it stops. | [[integrability-condition-for-parallel-fields]] |
| patch | — | A piece of ground all in one piece, with nothing cut out of it, such as a coin-shaped piece. | — |
| parallel field | — | The other name for a perfect painting of arrows. A copy of any painted arrow, carried anywhere without swinging, matches the arrow painted where it stops. | [[integrability-condition-for-parallel-fields]] |
| integrability condition | IN-teh-gruh-BIL-ih-tee | What the ground must allow before a perfect painting of arrows can exist: every small loop must bring a carried copy back matching the arrow it started on. | [[integrability-condition-for-parallel-fields]] |

## Key equations

### Parallel-field equations · working

$$
\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma = 0
$$

A field is parallel when its covariant derivative vanishes in every direction, so the field fixes its own partial derivatives.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $V^\rho$ | the candidate vector field | V upper rho |
| $\Gamma^\rho{}_{\nu\sigma}$ | connection coefficients, derivative index first | the Christoffel symbols |

**Holds when:** All directions $\nu$ at once; any affine connection, with the course index order.  
**Say it:** “The covariant derivative of V vanishes in every direction.”  
**Justified by:** `stated`

### Integrability condition for a parallel field · working

$$
R^\rho{}_{\sigma\mu\nu}\,V^\sigma = 0
$$

Wherever a parallel field exists, the curvature matrix of every coordinate plane annihilates it.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R^\rho{}_{\sigma\mu\nu}$ | Riemann tensor in the course convention | the Riemann tensor |
| $V^\sigma$ | the parallel field | the field |

**Holds when:** Necessary wherever $\nabla V = 0$ on an open set, for any affine connection with continuously differentiable coefficients; not sufficient on its own.  
**Say it:** “The Riemann tensor, contracted with the parallel field in its second slot, vanishes.”  
**Justified by:** `derivations/mixed-partials-give-curvature`

### Bracket of horizontal lifts · formal

$$
[H_\mu, H_\nu] = -R^\rho{}_{\sigma\mu\nu}\,v^\sigma\,\frac{\partial}{\partial v^\rho},\qquad H_\mu = \partial_\mu - \Gamma^\rho{}_{\mu\sigma}v^\sigma\frac{\partial}{\partial v^\rho}
$$

The horizontal distribution closes up to a vertical field given by the curvature, so it is integrable exactly when curvature vanishes.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $H_\mu$ | horizontal lift of the coordinate field $\partial_\mu$ to the total space | H mu |
| $v^\rho$ | fibre coordinates | v upper rho |

**Holds when:** A local trivialization of the bundle; the course sign of the Riemann tensor.  
**Say it:** “The bracket of two horizontal lifts is minus the curvature acting on the fibre point, pointing along the fibre.”  
**Justified by:** `derivations/horizontal-lifts-bracket`

## Derivations

### Mixed partials give curvature · working

**Goal:** Show that a solution of $\partial_\nu V^\rho = -\Gamma^\rho{}_{\nu\sigma}V^\sigma$ satisfies $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$.

1. A parallel field has $\nabla_\nu V^\rho = 0$ for every $\nu$, so $\partial_\nu V^\rho = -\Gamma^\rho{}_{\nu\sigma}V^\sigma$.
2. Differentiate with respect to $x^\mu$ by the product rule: $\partial_\mu\partial_\nu V^\rho = -(\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma - \Gamma^\rho{}_{\nu\lambda}\,\partial_\mu V^\lambda$.
3. Replace $\partial_\mu V^\lambda$ using the first step: $\partial_\mu\partial_\nu V^\rho = -(\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma + \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}V^\sigma$.
4. Swap the names $\mu$ and $\nu$: $\partial_\nu\partial_\mu V^\rho = -(\partial_\nu\Gamma^\rho{}_{\mu\sigma})V^\sigma + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}V^\sigma$.
5. Subtract: $\partial_\mu\partial_\nu V^\rho - \partial_\nu\partial_\mu V^\rho = -\big(\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}\big)V^\sigma$.
6. The bracket is the course $R^\rho{}_{\sigma\mu\nu}$, so the difference is $-R^\rho{}_{\sigma\mu\nu}V^\sigma$. No symmetry of $\Gamma$ was used.
7. If $\Gamma$ is continuously differentiable, the first step makes $V$ twice continuously differentiable, so its mixed partial derivatives agree and the difference vanishes.

**Result:** $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$ wherever $\nabla V = 0$, for any affine connection.

### Horizontal lifts and their bracket · formal

**Goal:** With base coordinates $x^\mu$ and fibre coordinates $v^\rho$, show $[H_\mu,H_\nu] = -R^\rho{}_{\sigma\mu\nu}v^\sigma\,\partial_{v^\rho}$ for $H_\mu = \partial_\mu - \Gamma^\rho{}_{\mu\sigma}v^\sigma\,\partial_{v^\rho}$.

1. A curve $(x(t),v(t))$ is tangent to the span of the $H_\mu$ exactly when $\dot v^\rho = -\Gamma^\rho{}_{\mu\sigma}\dot x^\mu v^\sigma$, the transport equation, so the $H_\mu$ span the horizontal distribution.
2. Write $A_\mu = \Gamma^\rho{}_{\mu\sigma}v^\sigma\,\partial_{v^\rho}$. Coordinate fields commute, so $[H_\mu,H_\nu] = -[\partial_\mu, A_\nu] + [\partial_\nu, A_\mu] + [A_\mu, A_\nu]$.
3. The first two brackets differentiate only the coefficients: $\big(-\partial_\mu\Gamma^\rho{}_{\nu\sigma} + \partial_\nu\Gamma^\rho{}_{\mu\sigma}\big)v^\sigma\,\partial_{v^\rho}$.
4. In $[A_\mu,A_\nu]$ each field differentiates the factor $v$ in the other: $[A_\mu,A_\nu] = \big(\Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} - \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}\big)v^\sigma\,\partial_{v^\rho}$.
5. The total coefficient is minus the course Riemann bracket, so $[H_\mu,H_\nu] = -R^\rho{}_{\sigma\mu\nu}v^\sigma\,\partial_{v^\rho}$, a vertical field.
6. A vertical field lies in the horizontal distribution only if it vanishes, so the distribution is involutive exactly when $R = 0$.

**Result:** $[H_\mu,H_\nu] = -R^\rho{}_{\sigma\mu\nu}v^\sigma\,\partial/\partial v^\rho$; the horizontal distribution is integrable exactly when the curvature vanishes.

## Worked examples

### Solving for a parallel field on a cone · working

**Problem:** Cut a wedge of angle $\delta = 30^\circ$ from a flat sheet and glue the edges into a cone, whose metric off the tip is $ds^2 = dr^2 + c^2r^2d\phi^2$ with $c = 1 - \delta/2\pi$ and $0 \le \phi < 2\pi$. Solve the parallel-field equations, and find what one lap around the tip does.

1. Here $G = cr$, so $G'' = 0$: the cone is flat away from the tip, and $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$ holds for every $V$.
2. With $\Gamma^r{}_{\phi\phi} = -GG'$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = G'/G$, the four equations read $\partial_rV^r = 0$, $\partial_\phi V^r = c^2rV^\phi$, $\partial_rV^\phi = -V^\phi/r$ and $\partial_\phi V^\phi = -V^r/r$.
3. The two $r$ equations integrate at once, giving $V^r = f(\phi)$ and $V^\phi = h(\phi)/r$.
4. The two $\phi$ equations become $f' = c^2h$ and $h' = -f$, so $f'' = -c^2f$ and $f = A\cos(c\phi + \phi_0)$.
5. Then $h = f'/c^2 = -(A/c)\sin(c\phi + \phi_0)$, and the orthonormal components are $V^{\hat r} = A\cos(c\phi+\phi_0)$ and $V^{\hat\phi} = GV^\phi = -A\sin(c\phi+\phi_0)$.
6. So the angle of $V$ from $\hat e_r$, positive toward $\hat e_\phi$, is $\alpha(\phi) = -(c\phi + \phi_0)$, of fixed length $|A|$.
7. One lap takes $\phi$ from $0$ to $2\pi$ and returns $\hat e_r$ to itself, while $\alpha$ falls by $2\pi c = 2\pi - \delta$. Modulo a full turn, a fall of $2\pi - \delta$ is a rise of $\delta$, so the field comes back turned by $\delta$ in the sense from $\hat e_r$ toward $\hat e_\phi$.
8. A walker going once round in the direction of increasing $\phi$ keeps the tip on the left, so that turn is toward the walker's left.

**Answer:** $V^{\hat r} = A\cos(c\phi+\phi_0)$ and $V^{\hat\phi} = -A\sin(c\phi+\phi_0)$: a parallel field on any slit cone, single-valued around the tip only if $\delta$ is a multiple of $2\pi$. For $\delta = 30^\circ$, one lap around the tip turns the field by $30^\circ$ toward the left of a walker going round in the direction of increasing $\phi$.

**Takeaway:** Zero curvature lets the equations be integrated, but the solution closes up around a hole only if the loop around it has trivial holonomy.

## Problems

### `two-routes-to-one-spot` · entry · difficulty 1 · conceptual

On a huge round ball you carry a cardboard arrow from one spot to a second spot along one path. At every step you paint an arrow on the ground matching the one you carry, leaving a row of painted arrows behind you. A friend sets off from the first spot with an arrow matching yours, carries it to the second spot along a different path, and paints a row too. The two paths meet only at their ends, so together they make a small loop. Call a row perfect along its own path if a copy carried along that path matches every painted arrow it reaches. Is each row perfect along its own path? Do the two arrows painted at the second spot match?

**Hints**

1. Along one path, how was each painted arrow made?
2. Carry a copy of your arrow at the second spot back to the start along your own path, then out along your friend's. What have you walked?

**Answer:** Each row is perfect along its own path, but the two arrows at the second spot do not match. They differ by the turn that the loop gives a carried arrow.

**Must contain:** Each row is perfect along its own path; The two arrows painted at the second spot do not match; They differ by the turn of the loop that the two paths make

**Solution**

1. Along one path, each painted arrow matches the carried arrow as it passed that spot. Two arrows that start matching and are carried along the same path without swinging stay matching all the way. So a copy carried along that path matches each painted arrow it reaches. Each row is therefore perfect along its own path.
2. Now lay a copy on your arrow painted at the second spot. Carry that copy back to the start along your own path. The rule never to let the arrow swing works the same way in both directions. So walking your path backwards plays your carrying backwards, step by step. The copy arrives matching the arrow you both started with.
3. Again, two arrows that start matching and follow the same path without swinging stay matching all the way. So when you carry the copy out along your friend's path, it arrives at the second spot matching your friend's painted arrow.
4. Altogether the copy went once around the loop, starting on your arrow at the second spot. On a ball a small loop brings a carried arrow back turned a little. The copy now matches your friend's arrow, so your friend's arrow and yours differ by that turn.

### `surface-of-revolution` · working · difficulty 2 · derivation

A surface has metric $ds^2 = dr^2 + G(r)^2\,d\phi^2$ with $G > 0$, so $\Gamma^r{}_{\phi\phi} = -GG'$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = G'/G$. Write the four parallel-field equations, require the mixed partial derivatives of $V^r$ and of $V^\phi$ to agree, and show that a nonzero parallel field needs $G'' = 0$. Which of $G = r$, $G = (1 - \delta/2\pi)\,r$ and $G = a\sin(r/a)$ allow one?

**Hints**

1. The equations are $\partial_rV^r = 0$, $\partial_\phi V^r = GG'V^\phi$, $\partial_rV^\phi = -(G'/G)V^\phi$ and $\partial_\phi V^\phi = -(G'/G)V^r$.
2. Compute $\partial_r(\partial_\phi V^r)$ and replace every first derivative using the equations.

**Answer:** Agreement of the mixed partials of $V^r$ gives $GG''V^\phi = 0$, and of $V^\phi$ gives $(G''/G)V^r = 0$, so $G'' = 0$ wherever $V \neq 0$. The plane $G = r$ and the cone $G = (1-\delta/2\pi)r$ pass; the sphere $G = a\sin(r/a)$ fails.

**Must contain:** Mixed partials of V r give G times G double prime times V phi equals zero; Mixed partials of V phi give G double prime over G times V r equals zero; Plane and cone pass; the sphere does not

**Solution**

1. With $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma$: $\partial_rV^r = 0$, $\partial_\phi V^r = GG'V^\phi$, $\partial_rV^\phi = -(G'/G)V^\phi$ and $\partial_\phi V^\phi = -(G'/G)V^r$.
2. $\partial_\phi(\partial_rV^r) = 0$, while $\partial_r(\partial_\phi V^r) = (G'^2 + GG'')V^\phi + GG'\,\partial_rV^\phi = (G'^2 + GG'')V^\phi - G'^2V^\phi = GG''V^\phi$.
3. $\partial_\phi(\partial_rV^\phi) = -(G'/G)\,\partial_\phi V^\phi = (G'/G)^2V^r$, while $\partial_r(\partial_\phi V^\phi) = -(G'/G)'V^r - (G'/G)\,\partial_rV^r = -\big(G''/G - G'^2/G^2\big)V^r$.
4. Equating each pair gives $GG''V^\phi = 0$ and $(G''/G)V^r = 0$. These are $R^\rho{}_{\sigma r\phi}V^\sigma = 0$ with $R^r{}_{\phi r\phi} = -GG''$ and $R^\phi{}_{rr\phi} = G''/G$, and $K = -G''/G$.
5. $G = r$ and $G = (1-\delta/2\pi)r$ have $G'' = 0$, so parallel fields exist on simply connected pieces. $G = a\sin(r/a)$ has $G'' = -\sin(r/a)/a \neq 0$ for $0 < r < \pi a$, so it allows none.

### `gradiometer-verdict` · working · difficulty 2 · estimate

A laboratory falls freely 400 km above Earth's surface. Two test masses inside are 2.0 m apart along the local vertical. Treat Earth as a static sphere with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and radius 6371 km. (a) Find their relative acceleration and $R^z{}_{0z0}$. (b) Can the laboratory's four-velocity extend to a parallel field nearby?

**Hints**

1. Use $-c^2R^z{}_{0z0} = 2GM/r^3$, with $r$ measured from Earth's centre.
2. What would a parallel four-velocity do to geodesic deviation?

**Answer:** (a) $5.1\times10^{-6}\ \mathrm{m\,s^{-2}}$, with $R^z{}_{0z0} = -2.86\times10^{-23}\ \mathrm{m^{-2}}$. (b) No: a parallel extension would need $R^\mu{}_{\nu\rho\sigma}u^\nu = 0$, which forces $R^z{}_{0z0} = 0$.

**Must contain:** Two G M over r cubed at 6771 kilometres is about 2.57 times ten to the minus six per second squared; The masses separate at about 5.1 micrometres per second squared; A parallel four-velocity would give zero tides, so no extension exists

**Numeric:** relative acceleration = 5.14e-06 m/s^2 (magnitude, ±3%); vertical tidal Riemann component = -2.86e-23 m^-2 (signed, ±3%)

**Solution**

1. $r = 6371 + 400 = 6771$ km, so $2GM/r^3 = 2 \times 3.986\times10^{14}/(6.771\times10^6)^3 = 2.57\times10^{-6}\ \mathrm{s^{-2}}$.
2. $R^z{}_{0z0} = -2.57\times10^{-6}/(2.998\times10^8)^2 = -2.86\times10^{-23}\ \mathrm{m^{-2}}$.
3. With $u^\mu = (c,0,0,0)$, geodesic deviation gives $\ddot\xi^z = -c^2R^z{}_{0z0}\,\xi^z = 2.57\times10^{-6} \times 2.0 = 5.1\times10^{-6}\ \mathrm{m\,s^{-2}}$, outward along the vertical.
4. If $u$ extended to a parallel field, the condition would give $R^\mu{}_{\nu\rho\sigma}u^\nu = cR^\mu{}_{0\rho\sigma} = 0$, including $R^z{}_{0z0} = 0$. The nonzero value rules that out.

### `brinkmann-wave-fields` · formal · difficulty 3 · derivation

Take the plane-fronted wave $ds^2 = H(u,x,y)\,du^2 + 2\,du\,dv + dx^2 + dy^2$ in coordinates $(u,v,x,y)$. Its only independent nonzero Riemann components are $R_{uiuj} = -\tfrac12\partial_i\partial_jH$ for $i,j \in \{x,y\}$. (a) Show that $k = \partial_v$ is null and parallel. (b) Check that $k$ satisfies the integrability condition. (c) For $H = A(u)(x^2 - y^2)$ with $A \neq 0$, decide whether $\partial_x$ is parallel, and confirm the answer with the condition.

**Hints**

1. Lower the index: $k_\mu = g_{\mu v}$, and use $\nabla_\mu k_\nu = \partial_\mu k_\nu - \Gamma^\lambda{}_{\mu\nu}k_\lambda$.
2. Nothing in the metric depends on $v$, and $g_{v\mu}$ is constant.
3. For $\partial_x$, $\nabla_\mu(\partial_x)_\nu = \tfrac12\partial_xg_{\mu\nu}$.

**Answer:** (a) $g_{vv} = 0$, and $\nabla_\mu k_\nu = -\Gamma_{v\mu\nu} = 0$ because $g_{v\mu}$ is constant and $\partial_vg_{\mu\nu} = 0$. (b) $R^\rho{}_{v\mu\nu} = 0$, since no nonzero component carries a $v$ slot. (c) $\nabla_u(\partial_x)_u = \tfrac12\partial_xH = A(u)\,x \neq 0$, so $\partial_x$ is not parallel, matching $R_{uxux} = -A \neq 0$.

**Must contain:** k is null because g v v vanishes; k is parallel because the Christoffel symbols with lowered index v vanish; No Riemann component carries a v slot, so the condition holds although R is nonzero; d by d x fails both tests when A is nonzero

**Solution**

1. $k^\mu = \delta^\mu{}_v$, so $g(k,k) = g_{vv} = 0$: $k$ is null. Its lowered form $k_\mu = g_{\mu v}$ is constant, with only a $u$ entry.
2. Since $k_\nu$ is constant, $\nabla_\mu k_\nu = -\Gamma^\lambda{}_{\mu\nu}k_\lambda = -g_{\lambda v}\Gamma^\lambda{}_{\mu\nu} = -\Gamma_{v\mu\nu}$, writing $\Gamma_{\lambda\mu\nu} = g_{\lambda\sigma}\Gamma^\sigma{}_{\mu\nu}$.
3. $\Gamma_{v\mu\nu} = \tfrac12(\partial_\mu g_{v\nu} + \partial_\nu g_{v\mu} - \partial_v g_{\mu\nu}) = 0$, since $g_{v\nu}$ is constant and nothing depends on $v$. So $\nabla k = 0$.
4. Raising and lowering preserve which components vanish, and every nonzero component is a symmetry image of $R_{uiuj}$, with no $v$ slot. So $R_{\rho v\mu\nu} = 0$ and $R^\rho{}_{\sigma\mu\nu}k^\sigma = 0$: the condition holds although $R \neq 0$.
5. For $X = \partial_x$, $X_\nu = g_{\nu x}$ is constant and $\nabla_\mu X_\nu = -\Gamma_{x\mu\nu} = \tfrac12\partial_xg_{\mu\nu}$, whose only nonzero entry is $\nabla_uX_u = \tfrac12\partial_xH = A(u)\,x$. It is nonzero away from $x = 0$, so $\partial_x$ is not parallel.
6. The condition agrees: $R_{uxux} = -\tfrac12\partial_x^2H = -A \neq 0$, so $R_{\rho x\mu\nu}X^x \neq 0$ for $\rho\mu\nu = uux$, and no parallel field takes the value $\partial_x$ anywhere.

## Observations

- **The vertical gradient of Earth's gravity, measured by comparing two freely falling clouds of atoms** (measured, working). An atom-interferometer gradiometer drops two laser-cooled clouds of atoms at different heights and compares their free-fall accelerations. The difference per unit separation is the tidal entry $-c^2R^z{}_{0z0}$ in the laboratory's frame. Because it is nonzero, the laboratory's four-velocity is the value of no parallel field. *Numbers:* Static spherical Earth at the surface: $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$, so $R^z{}_{0z0} = -3.43\times10^{-23}\ \mathrm{m^{-2}}$; the free-air gradient is $3.086\times10^{-6}\ \mathrm{s^{-2}}$. *Reference:* M. J. Snadden, J. M. McGuirk, P. Bouyer, K. G. Haritos, M. A. Kasevich (1998), *Measurement of the Earth's Gravity Gradient with an Atom Interferometer-Based Gravity Gradiometer*, Physical Review Letters 81, 971-974, doi:10.1103/PhysRevLett.81.971
- **Electron interference fringes shifted by a magnetic flux the electrons never touch** (measured, working). The gauge covariant derivative transports a charged field, and a field with $D_\mu\psi = 0$ exists locally exactly when $F_{\mu\nu} = 0$. Outside a shielded solenoid $F$ vanishes, yet the region is not simply connected, so no single-valued parallel phase exists and the two beams arrive with a phase difference $q\Phi/\hbar$: the same failure as on a cone. *Numbers:* An electron has $q = -e$, so the phase difference here has magnitude $e\Phi/\hbar$, whichever sense the loop is taken in. One superconducting flux quantum, $\Phi = h/2e = 2.07\times10^{-15}$ Wb, gives $e\Phi/\hbar = \pi$: a shift of half a fringe spacing. *Reference:* Akira Tonomura, Nobuyuki Osakabe, Tsuyoshi Matsuda, Takeshi Kawasaki, Junji Endo and others (1986), *Evidence for Aharonov-Bohm effect with magnetic field completely shielded from electron wave*, Physical Review Letters 56, 792-795, doi:10.1103/PhysRevLett.56.792

## Teaching arc

1. **Ask the painter's question** (entry). Set up the perfect painting on flat ground, then ask about a patch of a ball. *Why:* It turns an existence theorem into a job someone could try. *Predict:* Could a painter cover a small patch of a giant ball so that every carried copy matches the arrow painted where it stops? *Visual:* [[painted-arrows-that-must-match]] *Uses:* `ways_in/paint-an-arrow-on-every-spot`
2. **Break it with a loop, then size it** (entry). Carry one copy around a small loop, meet the equator objection, and put a number on the turn. *Why:* The equator shows that one good loop is not enough; the number shows why painted ground looks perfect. *Predict:* The equator brings a carried arrow back matching. Can the whole ball be painted perfectly? *Uses:* `checks/equator-loop-matches`, `checks/tiny-patch-on-earth`
3. **Differentiate twice** (working). Derive the condition from mixed partials, then solve the flat plane in polar coordinates as a control. *Why:* The control separates curved coordinate lines from curved space. *Predict:* Polar coordinates on a flat plane have nonzero Christoffel symbols. Can a parallel field live there? *Uses:* `ways_in/mixed-partials-pin-the-curvature-to-the-field`, `derivations/mixed-partials-give-curvature`, `checks/polar-plane-field`
4. **Measure the failure** (working). Show that a parallel four-velocity means no tides, then read a gravity gradient as a failed condition. *Why:* It connects an existence theorem to a laboratory reading. *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tides-rule-out-a-parallel-four-velocity`, `observations/atom-gradiometer`, `problems/gradiometer-verdict`
5. **Mark every hypothesis** (formal). State the Frobenius result, then break it at one point, around a missing tip, and with torsion. *Why:* Each counterexample pins one hypothesis to its job. *Predict:* Every piece of a flat Möbius band is flat. Does every vector at a point extend over the whole band? *Visual:* [[paper-cone-with-a-missing-wedge]] *Uses:* `ways_in/when-flatness-is-enough`, `ways_in/topology-and-torsion`, `checks/flat-at-one-point`, `checks/mobius-and-cylinder`
6. **Generalize to parallel tensors** (research). Present the holonomy principle, then test it on a product of two spheres and on a plane wave. *Why:* Parallel objects organize the special geometries. *Uses:* `ways_in/parallel-tensors-and-special-holonomy`, `checks/reducible-without-parallel-vector`, `problems/brinkmann-wave-fields`

## Misconceptions

### “If I paint every arrow pointing east, the painting is perfect, because they all point the same way.” · entry · `same-direction-means-matching`

- **Why it is tempting:** On flat ground, arrows all pointing the same way do make a perfect painting.
- **What is true:** Matching means a carried copy lies on the painted arrow, pointing the same way. On a ball a small loop brings every carried copy back turned, whichever way the painted arrows point.
- **Exposed by:** `checks/compass-painting`

### “The equator brings a carried arrow back matching, so the whole ball could be painted perfectly.” · entry · `one-good-loop-is-enough`

- **Why it is tempting:** Flat ground is exactly where every loop brings a carried arrow back matching.
- **What is true:** A perfect painting needs every loop in the painted region to return copies matching. On a ball, small loops do not.
- **Exposed by:** `checks/equator-loop-matches`

### “A small enough patch of a ball is flat, so it can be painted perfectly.” · entry · `tiny-patch-is-flat-enough`

- **Why it is tempting:** Painted lines on a car park look perfectly matched.
- **What is true:** However small the patch, it holds a smaller loop, and on a ball that loop turns a carried arrow. Shrinking the patch shrinks the turn in proportion to its area, but never to nothing.
- **Exposed by:** `checks/tiny-patch-on-earth`

### “Where the Christoffel symbols are nonzero, no parallel vector field can exist.” · working · `christoffels-rule-out-a-field`

- **Why it is tempting:** Nonzero Christoffel symbols make a parallel field's components vary.
- **What is true:** Only the curvature enters the condition. The flat plane in polar coordinates has nonzero Christoffel symbols and a parallel field through every vector.
- **Exposed by:** `checks/polar-plane-field`

### “A sphere has no parallel vector field because the hairy ball theorem forbids a nonvanishing field.” · working · `hairy-ball-is-the-reason`

- **Why it is tempting:** Both results deny a sphere some kind of vector field.
- **What is true:** The hairy ball theorem is global, but curvature forbids a parallel field on every open set, even a small cap that does carry nonvanishing fields.
- **Exposed by:** `checks/cap-has-no-parallel-field`

### “If the curvature annihilates a vector at a point, that vector extends to a parallel field near the point.” · formal · `condition-at-a-point-suffices`

- **Why it is tempting:** The condition is algebraic, checkable at a single point.
- **What is true:** A parallel field must satisfy the condition at every point it reaches, with all its covariant derivatives. Curvature that vanishes only at the point stops the extension.
- **Exposed by:** `checks/flat-at-one-point`

### “Zero curvature everywhere guarantees a global parallel field through every vector.” · formal · `zero-curvature-gives-global-fields`

- **Why it is tempting:** Zero curvature does give local parallel fields near every point.
- **What is true:** A global field also needs the holonomy of loops that cannot be shrunk to fix the vector. On a flat Möbius band only vectors along the band extend.
- **Exposed by:** `checks/mobius-and-cylinder`

### “If the holonomy group is reducible, the manifold carries a nonzero parallel vector field.” · research · `reducible-means-parallel-vector`

- **Why it is tempting:** A nonzero parallel field does make holonomy reducible.
- **What is true:** Reducible holonomy gives an invariant subspace, while a parallel field needs a vector fixed by holonomy. A product of two round spheres is reducible and carries no parallel vector field.
- **Exposed by:** `checks/reducible-without-parallel-vector`

## Checks

1. **Entry · evaluate-claim** `checks/compass-painting`. A friend paints arrows over a large region of Earth's ground, far from both poles, ignoring hills. Every arrow points due east. She says her painting is perfect: a copy of any arrow, carried anywhere in the region without swinging, matches the arrow painted where it stops. Is she right?
   - **Hints:** Carry a copy around a small loop inside her region.
   - **Answer:** No. Her region is a patch of a ball. Draw a small loop inside her region, and walk it keeping a piece of the ball on your left. If her painting were perfect, a copy carried around that loop would match a painted arrow at every step. Back at the start it would therefore match the arrow it started on. On a ball, however, such a loop brings every carried arrow back turned a little. So the painting cannot be perfect. Pointing every arrow the same way by the compass does not help, because this reasoning never used which way the arrows point.
   - **Must contain:** She is not right; A perfect painting must bring a copy back matching from every loop in the region; On a ball a small loop returns a carried copy turned; The reasoning never uses which way the arrows point
   - **Targets:** `same-direction-means-matching`
2. **Entry · evaluate-claim** `checks/equator-loop-matches`. On a huge round ball you carry a cardboard arrow once around the equator, never letting it swing, and it comes back matching its start. A friend says this proves the whole ball could be painted so that every carried copy matches the arrow painted where it stops. Is the friend right?
   - **Hints:** Which loops must a perfect painting pass?
   - **Answer:** No. A perfect painting needs every loop in the painted region to bring a carried copy back matching, not just one loop. Pick a small loop beside the equator, and walk it keeping a piece of the ball on your left. If the painting were perfect, a copy of the arrow painted where this loop starts would match a painted arrow at every step, so it would come back matching that arrow. On a ball, however, this small loop brings a carried arrow back turned a little. So no perfect painting exists, not even on a small patch beside the equator.
   - **Must contain:** The friend is not right; One good loop is not enough; A small loop beside the equator returns a carried copy turned
   - **Targets:** `one-good-loop-is-enough`
3. **Entry · numeric** `checks/tiny-patch-on-earth`. A painter wants a perfect painting of arrows on a square patch of Earth's ground, 100 metres on each side, ignoring hills. She lays a cardboard arrow flat at one corner and carries it once around the edge of the patch, back to that corner, never letting it swing. Is a perfect painting possible? About how big is the turn the arrow comes back with?
   - **Hints:** What fraction of a square kilometre is the patch?
   - **Answer:** No perfect painting is possible, but the turn is tiny. Earth is a ball, and the patch's edge is a small loop, so a carried arrow comes back turned. The patch covers 100 times 100, which is 10,000 square metres. A square kilometre is 1,000,000 square metres, so the patch is one hundredth of a square kilometre. A loop around one square kilometre turns a carried arrow by about 1.4 millionths of a degree. The turn shrinks in proportion to the area, so this turn is one hundredth of that, about 14 billionths of a degree.
   - **Must contain:** No perfect painting is possible; The patch is one hundredth of a square kilometre; The turn shrinks in proportion to the area; The turn is about 14 billionths of a degree
   - **Numeric:** turn of a copy carried around the edge = 1.41e-08 deg (magnitude, ±5%)
   - **Targets:** `tiny-patch-is-flat-enough`
4. **Working · numeric** `checks/polar-plane-field`. On the flat plane, $ds^2 = dr^2 + r^2d\phi^2$, with $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$. Show that $V = \sin\phi\,\partial_r + (\cos\phi/r)\,\partial_\phi$ is parallel. At $r = 2$, $\phi = 120^\circ$, what angle does $V$ make with $\hat e_r$, counted positive toward $\hat e_\phi$?
   - **Hints:** Use $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma$ four times. / The orthonormal component along $\hat e_\phi$ is $rV^\phi$.
   - **Answer:** All four components of $\nabla V$ vanish: $\nabla_rV^r = 0$; $\nabla_\phi V^r = \cos\phi - r\cdot\cos\phi/r = 0$; $\nabla_rV^\phi = -\cos\phi/r^2 + (1/r)(\cos\phi/r) = 0$; $\nabla_\phi V^\phi = -\sin\phi/r + (1/r)\sin\phi = 0$. So a parallel field exists although the Christoffel symbols do not vanish; in Cartesian coordinates it is $\partial_y$. At the point, $V^{\hat r} = \sin 120^\circ = 0.866$ and $V^{\hat\phi} = rV^\phi = \cos 120^\circ = -0.5$, so the angle is $-30^\circ$.
   - **Must contain:** Every component of the covariant derivative vanishes; Nonzero Christoffel symbols do not forbid a parallel field; The angle is minus 30 degrees
   - **Numeric:** angle from the radial direction toward the phi direction = -30 deg (signed, ±0.5, mod 360)
   - **Targets:** `christoffels-rule-out-a-field`
5. **Working · evaluate-claim** `checks/cap-has-no-parallel-field`. A classmate says: "The unit sphere has no parallel vector field, because the hairy ball theorem forbids a continuous nonvanishing tangent field." Evaluate the claim, using the cap $\theta < 30^\circ$.
   - **Hints:** Does the cap carry some smooth nonvanishing field?
   - **Answer:** The conclusion is right, but for curvature rather than topology. The hairy ball theorem is about the whole sphere; the cap is a disc, and it carries smooth nonvanishing fields, such as a coordinate field of a stereographic chart. Yet no parallel field lives there either. A parallel field satisfies $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$, which on a surface forces $KV = 0$; with $K = 1$ this gives $V = 0$, and $\nabla V = 0$ keeps $g(V,V)$ constant, so $V$ vanishes on the whole cap. The obstruction is local. A torus of revolution shows the difference: it carries nonvanishing fields, but $K \neq 0$ on open sets, so no parallel one.
   - **Must contain:** The hairy ball theorem is global, and the cap does carry nonvanishing fields; The condition gives K times V equals zero, so V vanishes there; Curvature forbids parallel fields on every open set
   - **Targets:** `hairy-ball-is-the-reason`
6. **Formal · evaluate-claim** `checks/flat-at-one-point`. The surface metric $dx^2 + (1+x^3)^2dy^2$, for $x > -1$, has $K = -6x/(1+x^3)$, which vanishes on $x = 0$. At $p = (0,0)$ the curvature endomorphisms vanish, so every $v \in T_pM$ satisfies $\mathcal R_p(X,Y)v = 0$. Claim: every such $v$ extends to a parallel field on a neighbourhood of $p$. Evaluate.
   - **Hints:** What does the condition say near $p$, rather than at $p$?
   - **Answer:** False for every $v \neq 0$. A parallel field on a connected neighbourhood keeps $g(V,V)$ constant, so it vanishes nowhere, and the condition then forces $K = 0$ throughout that neighbourhood. But $K \neq 0$ at every nearby point with $x \neq 0$. The necessary hierarchy already fails at first order: $(\nabla_{\partial_x}\mathcal R)_p$ has components $(\partial_xK)(\delta^\rho{}_\mu g_{\sigma\nu} - \delta^\rho{}_\nu g_{\sigma\mu})$ with $\partial_xK = -6$ at $p$, and it annihilates no nonzero $v$.
   - **Must contain:** A parallel field would force K to vanish on a whole neighbourhood; K is nonzero at every nearby point off x equals zero; The first covariant derivative of the curvature annihilates no nonzero vector
   - **Targets:** `condition-at-a-point-suffices`
7. **Formal · explain** `checks/mobius-and-cylinder`. A flat cylinder and a flat Möbius band both have $\mathcal R = 0$, and neither is simply connected. At a point $p$ on each core circle, which vectors in $T_pM$ extend to parallel fields on the whole surface?
   - **Hints:** Unroll each surface and look at how the ends are glued.
   - **Answer:** On the cylinder, all of them: unrolled, the strip is glued by a translation, so the holonomy group is trivial and $s(q) = P_\gamma v$ is path-independent. On the Möbius band the strip is glued with a flip across the band, so the holonomy group is $\{1,\sigma\}$ with $\sigma$ the reflection that reverses the direction across the band. Only vectors fixed by $\sigma$, those along the core, extend. So zero curvature gives local parallel fields everywhere, while global ones depend on the holonomy of loops that cannot be shrunk.
   - **Must contain:** Cylinder: trivial holonomy, so every vector extends; Möbius band: the holonomy contains the flip across the band; Only vectors along the band extend there
   - **Targets:** `zero-curvature-gives-global-fields`
8. **Research · evaluate-claim** `checks/reducible-without-parallel-vector`. Claim: "$S^2 \times S^2$ with the product of round metrics has reducible holonomy, so it carries a nonzero parallel vector field." Evaluate, and say which parallel forms it does carry.
   - **Hints:** A parallel field needs a fixed vector, not an invariant subspace.
   - **Answer:** False. The holonomy group is $SO(2)\times SO(2)$ acting on $T_pM = \mathbb R^2 \oplus \mathbb R^2$ by independent rotations. It preserves both planes, so it is reducible, but it fixes no nonzero vector, and by the holonomy principle there is no parallel vector field. The integrability condition agrees: it would need $K_1$ times the first component and $K_2$ times the second to vanish, with both curvatures positive. The invariant $2$-forms at $p$ are the constant combinations $a\,\omega_1 + b\,\omega_2$ of the two area forms; the remaining parallel forms are the constants and the volume form $\omega_1\wedge\omega_2$, and no nonzero $1$-form or $3$-form is fixed.
   - **Must contain:** Holonomy is S O 2 times S O 2: reducible, but fixing no vector; No parallel vector field exists; The parallel forms are the constants, constant combinations of the two area forms, and the volume form
   - **Targets:** `reducible-means-parallel-vector`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which slot of the Riemann tensor takes the parallel vector | $R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$: the vector goes in the second slot, the plane in the last two. The sign convention of the Riemann tensor does not affect this homogeneous condition. | Some texts contract the vector into another slot, for example $R_{\mu\nu\rho\sigma}V^\sigma = 0$. For the Levi-Civita connection its symmetries make these equivalent; for a general affine connection they are not. |
| Order of the lower indices on the connection in the parallel-field equations | $\partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma = 0$, derivative index first. | Some texts put the derivative index last, $\Gamma^\rho{}_{\sigma\nu}$. The two agree for a symmetric connection; with torsion they transport differently. |

## Visuals

- ★ [[painted-arrows-that-must-match]] (flagship): Flagship: a perfect painting succeeds on flat ground and fails on a ball, with the failure located on loops. *Sketch:* A patch of flat ground, a tube, a round ball, a saddle or a paper cone. The learner drops one arrow and spreads carried copies along chosen paths, painting as they go. Where two painted rows meet, a marker gives the angle between them, and a shaded map gives each small loop's turn. Floor and tube stay at zero; on the ball every small loop turns the copy toward the walker's left, growing with the area of the piece on that side; on the cone only paths passing on opposite sides of the tip disagree.
- [[falling-ring-of-crumbs]] (supporting): Tides as the measured failure of a parallel four-velocity. *Sketch:* A ring of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it, with sliders for mass and distance and a readout of relative acceleration per unit separation; a switch to flat spacetime leaves the ring unchanged.
- [[paper-cone-with-a-missing-wedge]] (supporting): Flat but not simply connected: parallel fields on slit pieces, none all the way around the tip. *Sketch:* Cut a wedge of adjustable angle from a flat sheet and glue it into a cone, with the unrolled sheet beside it. Loops that avoid the tip return the arrow unchanged; a loop winding n times around it returns the arrow rotated by n times the wedge angle.

## Tutor moves

**Open with**

- Picture painting an arrow at every spot of a big flat car park. Lay a cardboard copy on one of those arrows and carry it anywhere, never letting it swing to your left or right. Where you stop, the copy should lie on the arrow painted there, pointing the same way. Easy on flat ground. Could you do it on a small patch of a huge round ball? *(prediction)*

**If the learner is stuck**

- *The learner does not see why a perfect painting forces a carried copy to come back matching around a loop.* → Walk the loop one step at a time, asking which painted arrow the copy matches, until it is back at the start. *Uses:* `ways_in/paint-an-arrow-on-every-spot`, `problems/two-routes-to-one-spot`
- *The learner loses track of indices when substituting the equations into their derivatives.* → Work the two-dimensional surface first, component by component, then return to the index proof. *Uses:* `problems/surface-of-revolution`, `derivations/mixed-partials-give-curvature`

**Common questions**

- *Why does this matter for gravity?* (entry) Gravity asks the painter's question too. Drop two small objects together near Earth, one a metre above the other, with no air in the way. Their gap slowly grows: ten seconds of dropping adds about 0.15 millimetres. Now picture an arrow for each dropped object that shows how it is moving, which way and how fast. If those arrows could make a perfect painting, as on flat ground, then neighbours dropped together would keep moving alike and would never drift apart. So the measured drift shows that near Earth no perfect painting of dropping motions exists. *Uses:* `ways_in/tides-rule-out-a-parallel-four-velocity`
- *If every small loop brings a carried copy back matching, can the painter always succeed?* (entry) Not always, and a paper cone shows why. Cut a wedge out of a flat sheet of paper and tape the two cut edges together, so the paper becomes a cone. Ask her to paint only the part more than a hand's width from the tip, which is a ring of paper. The paper was never stretched, so every small loop in that ring brings a carried copy back matching. But carry a copy once around the ring, all the way round the tip, keeping the tip on your left. The copy comes back turned toward your left, by the angle of the wedge you cut out. So she can paint any piece of the ring that does not close up around the tip, and no more. Small loops decide what she can do near each spot. A loop that goes all the way round the tip can still stop her. *Uses:* `ways_in/topology-and-torsion`

**Switching levels**

- To working when: asks how to write the painting with derivatives; uses components or Christoffel symbols. Derive the condition from mixed partials, then solve the polar-plane control. *Uses:* `ways_in/mixed-partials-pin-the-curvature-to-the-field`, `checks/polar-plane-field`
- To formal when: asks whether the condition is sufficient; asks about holes, topology or torsion. State the Frobenius result, then its counterexamples. *Uses:* `ways_in/when-flatness-is-enough`, `ways_in/topology-and-torsion`
- To research when: asks about special holonomy, parallel spinors, pp-waves or teleparallel gravity. Present the holonomy principle and its research horizon. *Uses:* `ways_in/parallel-tensors-and-special-holonomy`, `research_horizon/special-holonomy-and-parallel-spinors`

**Pronunciations:** Frobenius → froh-BAY-nee-us; de Rham → duh RAHM; Brinkmann → BRINK-mahn; Weitzenböck → VYE-tsen-burk; Christoffel → kris-TOFF-el; Levi-Civita → LEH-vee CHEE-vee-tah; Berger → ber-ZHAY; Möbius → MUR-bee-us; Ambrose-Singer → AM-brohz SING-er

## History

- **Elwin Bruno Christoffel (1869).** Asked when one quadratic differential form can be transformed into another, and found a four-index combination of the metric's derivatives, the curvature tensor, among the integrability conditions of the transformation equations. E. B. Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46-70, doi:10.1515/crll.1869.70.46
- **Georg Frobenius (1877).** Treated systematically when systems of first-order total differential equations can be integrated, the result now called Frobenius's theorem; work by Deahna and Clebsch had anticipated it. Georg Frobenius (1877), *Ueber das Pfaffsche Problem*, Journal für die reine und angewandte Mathematik 82, 230-315, doi:10.1515/crll.1877.82.230
- **Tullio Levi-Civita (1917).** Defined parallel transport on Riemannian manifolds, which made it possible to ask when a vector field is parallel and to read curvature as the obstruction. Tullio Levi-Civita (1917), *Nozione di parallelismo in una varietà qualunque e conseguente specificazione geometrica della curvatura riemanniana*, Rendiconti del Circolo Matematico di Palermo 42, 173-205, doi:10.1007/BF03014898
- **Hans Brinkmann (1925).** Found the metrics that admit a covariantly constant null vector field, later recognized as plane-fronted gravitational waves. H. W. Brinkmann (1925), *Einstein spaces which are mapped conformally on each other*, Mathematische Annalen 94, 119-145, doi:10.1007/BF01208647
- **Albert Einstein (1928).** Proposed a geometry with distant parallelism, a global parallel frame given by a curvature-free connection with torsion, as the basis of a unified field theory. Albert Einstein (1928), *Riemann-Geometrie mit Aufrechterhaltung des Begriffes des Fernparallelismus*, Sitzungsberichte der Preußischen Akademie der Wissenschaften, Physikalisch-mathematische Klasse (1928), 217-221

## Research horizon

- **Special holonomy and parallel spinors.** Parallel tensors and spinors are the holonomy-invariant ones, so Berger's classification lists the geometries that carry them. Wang identified the simply connected irreducible Riemannian holonomy groups admitting parallel spinors, all Ricci-flat by the spinor integrability condition. De Rham's theorem splits off a flat factor for every parallel vector field on a complete, simply connected manifold. Marcel Berger (1955), *Sur les groupes d'holonomie homogènes de variétés à connexion affine et des variétés riemanniennes*, Bulletin de la Société Mathématique de France 83, 279-330, doi:10.24033/bsmf.1464; Georges de Rham (1952), *Sur la réductibilité d'un espace de Riemann*, Commentarii Mathematici Helvetici 26, 328-344, doi:10.1007/BF02564308; McKenzie Y. Wang (1989), *Parallel spinors and parallel forms*, Annals of Global Analysis and Geometry 7, 59-68, doi:10.1007/BF00137402; Robert L. Bryant (2000), *Recent advances in the theory of holonomy*, Séminaire Bourbaki 1998/99, exposé 861, Astérisque 266, 351-374, arXiv:math/9910059
- **Parallel null vectors and pp-waves.** A Lorentzian manifold can carry a parallel null vector without splitting as a product, because the invariant line it spans is degenerate. In four-dimensional vacuum those spacetimes are the pp-waves, exact gravitational waves whose integrability condition holds although the curvature does not vanish. They serve as test cases for exact wave solutions and as backgrounds in which quantum fields and strings can be solved. H. W. Brinkmann (1925), *Einstein spaces which are mapped conformally on each other*, Mathematische Annalen 94, 119-145, doi:10.1007/BF01208647; Jürgen Ehlers, Wolfgang Kundt (1962), *Exact solutions of the gravitational field equations*, In L. Witten (ed.), Gravitation: An Introduction to Current Research, Wiley, New York, 49-101
- **Teleparallel gravity.** A curvature-free metric connection with torsion carries a global parallel frame on a parallelizable spacetime, so parallel fields exist through every vector while no coordinates make the connection vanish. The teleparallel equivalent of general relativity rewrites Einstein's theory with this connection, and its modifications are studied as alternatives to general relativity. Albert Einstein (1928), *Riemann-Geometrie mit Aufrechterhaltung des Begriffes des Fernparallelismus*, Sitzungsberichte der Preußischen Akademie der Wissenschaften, Physikalisch-mathematische Klasse (1928), 217-221; Ruben Aldrovandi, José Geraldo Pereira (2013), *Teleparallel Gravity: An Introduction*, Springer, Dordrecht (Fundamental Theories of Physics 173), doi:10.1007/978-94-007-5143-9

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** A groundskeeper paints an arrow on every spot of a car park, and her painting counts as perfect if you can put a cardboard arrow on top of any painted one, carry it around without swinging it, and always find it lying on the arrow painted where you stop. On the flat car park she just lines them all up with one edge and it works. On a ball it cannot work: if it did, a copy carried around a small loop would come back on the arrow it started on, but a loop on a ball always brings an arrow back turned a bit. Making the patch smaller does not help, because there is always a smaller loop inside it. The rule that small loops must bring copies back matching is called the integrability condition, and on Earth the turn is about a millionth of a degree for a square kilometre, so painted car parks look fine. Things I was unsure about: it says the perfect painting is called a parallel field right after saying she paints the arrows parallel to one edge, so I thought a parallel field just means arrows that are parallel, which is exactly what the check says is wrong. The summary says flat ground allows one, and I read that as exactly one painting. I did not know what a copy was the first time the summary used the word. In the 100-metre patch check I was asked how big the turn is, but nothing I had read told me the turn goes with the area. And in the two-paths problem I had to take on trust that walking a path backwards undoes the carrying.

**Stumbles (24)**

- “A perfect painting would let you lay a copy on any painted arrow, carry the copy anywhere without letting it swing, and find it matching the arrow painted where you stop.”: The summary's first use of "a copy" never says a copy of what, and it is 29 words holding the whole test; "swing" also arrives without its left-or-right reference.
- “Flat ground allows one.”: "one" has no clear noun, and it reads as "exactly one perfect painting", which is false: flat ground allows one through every starting direction.
- “When arrows can be painted so that every carried copy matches them”: "them" is ambiguous in the tagline, the one line a reader meets with no context at all.
- “Lay a cardboard copy on any painted arrow, so that the copy lies on top of it, pointing the same way. That is what matching means.”: Two new terms, copy and matching, land in one paragraph, and "it" has to be the painted arrow two clauses back.
- “She paints every arrow parallel to one straight edge of the car park, all pointing the same way. ... A perfect painting like this is called a parallel field.”: "Parallel" is used in two senses one sentence apart, so the name teaches the misconception same-direction-means-matching: that a parallel field just means arrows that look parallel.
- “A carried copy never swings, so it keeps its angle to that edge and matches every arrow it reaches.”: A step left implicit. Why does not swinging keep the angle to a fixed edge? The entry prerequisite is the Ricci identity, not holonomy, so the reader has never been told that a carried arrow keeps pointing the same way on flat ground.
- “Now give her a patch of a huge round ball, and suppose she has succeeded. Draw a small loop in the patch, with a piece of the ball on your left as you walk. ... so her painting cannot be perfect.”: The person switches from her to you with no handover, and the argument by contradiction is never flagged, so the ending reads as a flat contradiction of the opening supposition.
- “However small a patch is, it holds a smaller loop, and that loop turns a carried arrow too.”: A missing everyday rule, and the check tiny-patch-on-earth cannot be answered without it: nothing in the entry ways says how the turn changes when the loop shrinks.
- “So a perfect painting needs small loops to bring carried copies back matching.”: A universal claim missing its quantifier: one small loop passing is not the demand, as the equator check shows.
- “That is a hair's width seen from 3 kilometres away, far too little to notice.”: A turn is being called a width, one word doing two jobs in the sentence that is supposed to make the number feel real.
- “Arrows can be painted so that every carried copy matches on flat ground, but not on any patch of a ball, because small loops there bring carried copies back turned. / Can arrows be painted on a patch of a ball so that every carried copy matches where it stops?”: "matches" with nothing to match, in the takeaway the reader should be able to say back and in the way's own question; the takeaway also squeezes the whole result into one 29-word sentence.
- “Picture painting an arrow at every spot of a big flat car park, so that any arrow you carry matches the arrow painted where you stop.”: The opening question and the tutor's gist both leave out the no-swinging rule, so a learner can answer yes by simply turning the arrow to match; a rule the reader cannot follow is no rule at all.
- “Draw a small loop inside it, with a piece of the ball on your left as you walk.”: "it" sits one sentence after "a patch of a ball", so it can be read as the ball rather than her region.
- “A copy of the arrow painted at one corner is carried once around the patch's edge, without swinging.”: The check's starting state assumes the painting it is asking about already exists, and "around the patch's edge" never says the walk returns to the corner.
- “Is each row of painted arrows perfect along its own path?”: "perfect along its own path" is a new phrase: perfect was defined for a whole painting, and the reader is left to guess what it means for one path.
- “Walking a path backwards plays the carrying backwards, step by step, so the copy arrives matching the arrow you both started with.”: A surprising claim with no reason, and the entry reader has met no rule that says carrying can be undone.
- “Think of each dropped object's motion as an arrow.”: The spoken answer jumps from arrows lying on the ground to motion with no bridge, and never says what the arrow would show.
- “On a ball a small loop brings every copy back turned, whatever chose the directions.”: "whatever chose the directions" is not a phrase a reader can parse; it also hides what the sentence is scoping.
- “So a perfect painting needs every small loop to bring carried copies back matching.”: The first what-if a teenager tries is the converse: if every small loop passes, is she finished? Nothing at the entry rung answers it, and the honest answer is no.
- “These are $n^2$ equations for $n$ unknown functions, so the system is overdetermined.”: Climbing the ladder: $n$ appears at the working rung with no introduction, and the reader has to guess it is the number of dimensions.
- “On a flat floor it comes back matching its start. / Flat ground allows one. / as on a flat floor”: Two words for one setting, flat floor and flat ground, in the recap, the summary, two misconceptions and the spoken gravity answer; a reader cannot tell whether they are the same place.
- “At every step you paint a copy of the carried arrow on the ground.”: "copy" has just been defined as the cardboard arrow you carry, so a painted copy makes the word do two jobs in one problem.
- “A perfect painting returns a copy matching from every loop in the region.”: A check's key point the reader has to reread: "returns a copy matching" has the copy arriving and matching in one verb with no object.
- “A copy of the arrow painted at one corner is carried once around the patch's edge.”: Passive, so the reader does not know who is doing it, in a check whose whole point is a job someone performs.

**Fixes**

- Summary and tagline rebuilt: the copy is introduced before it is used, the no-swinging rule keeps its left-or-right reference, "Flat ground allows one" becomes "Flat ground allows a perfect painting", and the condition is quantified over every small loop.
- Entry way: split the test into two paragraphs so copy and matching each get their own; added the flat-ground reason that a carried copy keeps pointing the same way (also restated in the recap); separated the name parallel field from the everyday word parallel, which was teaching the note's own first misconception; flagged the argument by contradiction and kept one person walking the loop.
- Added the rule that the turn shrinks in proportion to the area of the piece of ball on your left and never to nothing. The check tiny-patch-on-earth needed it to be answerable from the entry ways, and the misconception tiny-patch-is-flat-enough already assumed it.
- Entry checks: fixed the ambiguous "inside it", removed the compass wording from the answer of compass-painting, made the loop in tiny-patch-on-earth start from a fresh cardboard arrow and say that it returns to its corner, and named what a carried copy matches in equator-loop-matches.
- Entry problem: defined "perfect along its own path" in the statement, gave the reversal step its reason, and made the second hint say which copy to carry back.
- Glossary: added copy and perfect painting, tied parallel field to perfect painting as the same thing under two names, quantified the integrability condition over every small loop, and made patch say what it excludes in plain words.
- Settled on flat ground as the note's one name for uncurved ground, in the recap, the summary, both entry misconceptions, the spoken gravity answer and the flagship visual's sketch; the recap says once that flat ground means a floor or a car park.
- Restored an entry common question on whether passing every small loop is enough, answered with the ring of a paper cone, which the writer had dropped for budget. It answers the reader's first what-if and keeps the entry rung honest about necessity against sufficiency.
- Ladder: introduced $n$ as the number of dimensions where the working way first counts equations. Every non-entry way already names the way it continues in its first sentence.
- Budgets after the fixes: entry way explanations 433 words, inside the 440 the review allowance gives (the 400 cap plus 10%), used only for the stumble fixes listed here; every other part is inside its cap. Nothing was dropped; two clauses were said in fewer words to keep headroom, without losing a step.
- Bumped the revision to 2 and set status novice-reviewed.

**Concerns**

- For the physics reviewer: three new entry claims need checking. The turn of a small loop shrinks in proportion to the area of the piece of ball on your left. The paper-cone ring, which passes every small loop yet carries no painting all the way round the tip, with the turn equal to the wedge angle. And the paraphrase in the gravity answer that arrows showing how each dropped object moves would, if they made a perfect painting, keep neighbours moving alike.
- The claim that a copy carried on flat ground keeps pointing the same way is now stated in the entry recap and used in the car-park paragraph. It is the flat case of parallel transport, taken on trust at this rung; holonomy is only a formal prerequisite here, so nothing below can be cited for it.
- The note's entry rung leans on the arrow test, which arrives through the entry rung of ricci-identity. If that note's entry recap ever drops the test, this note's recap is the only place a reader meets it.
- The writer's open question about the overwrite stands: this file was rebuilt as a fresh draft over a previously physics-reviewed revision 4, and the earlier reviews are gone from the record. The snapshots are in the session scratchpad. This review signs revision 2 of the rebuilt note only.
- All three visuals are still proposals. The catalog visual carry-an-arrow-around-a-loop matches this note's entry way, but its serves list does not include this concept, so the entry way cannot cite it.
- References are all verified:false, and the Aharonov-Bohm reference carries no DOI. The physics reviewer confirms them.

**Re-read** (2026-09-13, revision 4): 4 stumbles in 5 changed passages

- “But walk once around the ring, all the way round the tip, keeping the tip on your left. The copy comes back turned toward your left, by the angle of the wedge you cut out.”: Splitting the old sentence in two, to keep every sentence under 32 words, dropped the carrying: the walking sentence no longer says anything is taken round, so "The copy" arrives with its noun two sentences back and a reader who follows the instruction walks the ring empty-handed. Everywhere else in the note the reader is told to carry the copy before being told what it does.
- “An electron has $q = -e$, so one superconducting flux quantum, $\Phi = h/2e = 2.07\times10^{-15}$ Wb, gives a phase difference of magnitude $e\Phi/\hbar = \pi$: a shift of half a fringe spacing, whichever sense the loop is taken in.”: One 41-word sentence holds three separate things at once: the electron's charge, the flux-quantum number, and the sense-independence of the magnitude. Its "so" does not follow from $q = -e$ alone, because the rule $q\Phi/\hbar$ sits in the connection field, so the reader has to reach into another field mid-sentence to see why the magnitude is $e\Phi/\hbar$.
- “Modulo a full turn that is a rise of $\delta$, so the field comes back turned by $\delta$ in the sense from $\hat e_r$ toward $\hat e_\phi$.”: "that" has no noun to point at; the reader must supply "a fall of $2\pi - \delta$" from the clause before it, and the branch step reads as an aside rather than a move. The step also now carries three moves, against one move per step.
- “For $\delta = 30^\circ$, one lap turns it by $30^\circ$ toward the walker's left.”: In the answer, read on its own, "it" has three candidates in the sentence before it (the parallel field, the tip, $\delta$), and "the walker" is definite although no walker appears anywhere in the answer. The reader cannot tell which way that walker goes, which is what fixes the sense.
- Fix: Entry common question is-passing-every-small-loop-enough: "But walk once around the ring" becomes "But carry a copy once around the ring", so the copy is in the reader's hands before the next sentence says what happened to it. Nothing else in the answer changed, and the two short sentences the physics review made stay short.
- Fix: Observation aharonov-bohm-ring numbers: split into two sentences, the charge and the magnitude first, then the flux quantum and the number. Every claim is kept word for word, including $q = -e$, the magnitude $e\Phi/\hbar$, the value $\pi$, the half-fringe shift and the sense-independence.
- Fix: Worked example parallel-field-on-a-cone, last step: "Modulo a full turn that is a rise of $\delta$" becomes "Modulo a full turn, a fall of $2\pi - \delta$ is a rise of $\delta$", and the walker's-left sentence is moved into a step of its own, so each step carries one move. The branch, the sense from $\hat e_r$ toward $\hat e_\phi$, and the walker's direction are unchanged.
- Fix: Worked example answer: "one lap turns it by $30^\circ$ toward the walker's left" names the field and the walker, as "one lap around the tip turns the field by $30^\circ$ toward the left of a walker going round in the direction of increasing $\phi$". The angle, the sense and the single-valuedness condition are unchanged.
- Fix: No claim, number, condition, sign or sense was altered, and nothing was dropped or compressed. The fixes add about 25 words to examples and observations (about 2160 of 2500) and about 2 words to the tutoring part (about 3096 of 3500); entry way explanations are untouched at 433 words and the total stays near 8525 of 10500.
- Fix: Rule 17 was checked on the one entry string in the diff: the common question still answers one question with one picture, the paper cone, and adds no second new idea, so no way had to be split.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 4)

**Verification**

- Parallel-field equations: nabla_nu V^rho = partial_nu V^rho + Gamma^rho_{nu sigma} V^sigma = 0, derivative index first.: Compared with the conventions row for the covariant derivative and the Christoffel index order; checked the notation trap derivative-index-on-the-connection against it. → Matches the course conventions exactly.
- Derivation mixed-partials-give-curvature: the commutator of partial derivatives equals -R^rho_{sigma mu nu} V^sigma with the course Riemann sign.: Re-derived all seven steps by hand from partial_nu V^rho = -Gamma^rho_{nu sigma}V^sigma, then compared the resulting bracket term by term with the conventions row R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} + Gamma Gamma - Gamma Gamma. → Every step correct and the bracket is exactly the course Riemann tensor, so the difference is -R^rho_{sigma mu nu}V^sigma. The claim that no symmetry of Gamma was used is right: with torsion the Ricci-identity route would carry an extra torsion term, which nabla V = 0 kills, so the condition still holds for any affine connection. The C^1 smoothness argument for equality of mixed partials is correct (V is C^1 from the equation, hence C^2).
- Surface form R_{rho sigma mu nu} = K(g_{rho mu}g_{sigma nu} - g_{rho nu}g_{sigma mu}) and the component extractions K V_2 = 0, K V_1 = 0.: Contracted to Ricci and to the scalar by hand (R_{mu nu} = K g_{mu nu}, R = 2K) and checked against the conventions row that a sphere of radius a has K = +1/a^2 and R = +2/a^2; then worked both index choices. → Correct. rho = nu = 2, mu = 1 gives -K V_1 = 0, which is the same condition; the note's wording is fine. Sign of K on a sphere agrees with the conventions.
- Entry claim: a small loop on a ball turns a carried copy toward the walker's left, by an amount proportional to the area of the piece of ball on that side.: python parallel transport (Euler, 40,000 steps per side) of two different start vectors around a coordinate loop at theta = 1.0 with sides 0.05 on the unit sphere, with the enclosed piece on the walker's left; angle measured from theta-hat toward phi-hat, which the conventions row makes the walker's-left sense. → Turn 2.069041e-3 rad against area 2.069039e-3: ratio 1.0000, positive, and the second start vector turned by the same angle to six figures. Confirms both the sense and the recap's 'one trip turns every arrow by the same amount'. The proportionality is exact on a sphere (turn = A/a^2), so 'shrinks in proportion to the area' is true as stated for shrinking loops.
- Entry number: a loop around one square kilometre of Earth's ground turns a carried copy by about 1.4 millionths of a degree, the angle a hair's width makes at 3 kilometres.: python: K = 1/R_E^2 with R_E = 6.371e6 m; angle = K x 1e6 m^2; transverse size at 3 km. → 2.4637e-8 rad = 1.4116e-6 deg, so 'about 1.4 millionths of a degree' is right; the width at 3 km is 0.074 mm, a typical human hair. Both correct.
- Check tiny-patch-on-earth: a 100 m square patch gives about 14 billionths of a degree, numeric 1.41e-8 deg.: python: area 1e4 m^2 times K, in degrees; also checked that the patch is one hundredth of a square kilometre. → 1.4116e-8 deg. Numeric field and 5% tolerance correct, and the fraction statement is right.
- Check equator-loop-matches: a loop around the equator brings a carried arrow back matching, yet no perfect painting exists.: Area of a hemisphere is 2 pi a^2, so the turn is 2 pi, which is zero modulo a full turn; compared with the small-loop result beside the equator. → Correct: the equator is exactly the standard zero-holonomy loop on a curved surface, and the answer's small loop beside it still turns. Good counterexample handling.
- Tidal entry: -c^2 R^z_{0z0} = 2GM/r^3 for a static spherical Earth, with R^z_{0z0} negative.: Took the conventions geodesic-deviation row with u = (c,0,0,0), so xi-double-dot^z = -c^2 R^z_{0z0} xi^z, and compared with the Newtonian tidal result d_z d_z Phi = -2GM/r^3 for Phi = -GM/r on the axis; cross-checked against the known Schwarzschild orthonormal value R^{r-hat}_{t-hat r-hat t-hat} = -2GM/c^2 r^3. → Sign and factor correct: R^z_{0z0} = -2GM/(r^3 c^2) < 0, radial separation grows.
- Surface numbers: 2GM/r^3 = 3.08e-6 s^-2, relative acceleration 3.1 micrometres per second squared at 1 m, R^z_{0z0} = -3.43e-23 m^-2, free-air gradient 3.086e-6 s^-2.: python with GM = 3.986e14 m^3 s^-2, r = 6.371e6 m, c = 2.998e8 m/s; compared the free-air value with 2g/R_E. → 3.0828e-6 s^-2, -3.4299e-23 m^-2, and 2g/R_E = 3.083e-6 s^-2 against the quoted free-air 3.086e-6 s^-2. All correct.
- Problem gradiometer-verdict: at 400 km altitude the relative acceleration of masses 2.0 m apart is 5.14e-6 m/s^2 and R^z_{0z0} = -2.86e-23 m^-2.: python with r = 6.771e6 m. → 2GM/r^3 = 2.5681e-6 s^-2, relative acceleration 5.1362e-6 m/s^2, R^z_{0z0} = -2.8572e-23 m^-2. Both numeric fields and the 3% tolerances are right, and the signed field is correctly negative.
- Entry common question: two objects dropped a metre apart vertically drift about 0.15 mm apart in ten seconds.: python: half times 2GM/r^3 times 1 m times (10 s)^2, with the linearized deviation solution cosh(omega t) checked for the size of the correction. → 0.154 mm; the change of r during the fall alters the gradient by 2 parts in 10^4, negligible. Correct, and the surrounding claim is sound: a parallel velocity field gives zero relative acceleration, so neighbours released with no relative velocity never drift.
- Worked example parallel-field-on-a-cone: the solution, the orthonormal components, and the turn after one lap.: Re-solved the four equations by hand, then integrated the transport equation numerically once around the tip at r = 2 on the 30-degree cone (400,000 steps) and measured the angle from e_r toward e_phi. → Solution correct; numeric lap turn 30.0000 deg in the e_r-toward-e_phi sense. The step said alpha 'falls by 2 pi - delta' and then that the field comes back turned by delta without naming the branch, and glossed e_phi itself as the walker's left, which is the direction of travel. Fixed: stated the modulo, and said that a walker going round in the direction of increasing phi keeps the tip on the left, so the turn is toward the walker's left.
- Problem surface-of-revolution: mixed partials give G G'' V^phi = 0 and (G''/G)V^r = 0, with R^r_{phi r phi} = -G G'', R^phi_{r r phi} = G''/G and K = -G''/G.: Re-derived both mixed-partial pairs by hand; computed the Riemann components and the Ricci scalar numerically from the metric for G = a sin(r/a), a = 1.7, at r = 0.9. → R^r_{phi r phi} = 0.255051 against -G G'' = 0.255051; R^phi_{r r phi} = -0.346021 against G''/G; K = 0.346021 = 1/a^2; Ricci scalar 0.692043 = 2K, positive as the conventions require. Plane and cone pass (G'' = 0), sphere fails for 0 < r < pi a. All correct.
- Check polar-plane-field: the field is parallel, and its angle at r = 2, phi = 120 degrees is -30 degrees.: Evaluated all four covariant-derivative components by hand; converted to orthonormal components and to Cartesian; python atan2. → All four vanish; in Cartesian the field is exactly the unit field along y, as claimed; the angle is -30.000 deg, inside the 0.5 deg tolerance, and the signed sense (positive toward e_phi) is stated.
- Check cap-has-no-parallel-field: the cap carries nonvanishing fields but no parallel one, and a torus of revolution makes the same point.: Checked the algebra K V = 0 with K = 1, the constancy of g(V,V) under a metric connection, and the curvature of a torus of revolution. → Correct. The torus does carry nonvanishing fields and has K nonzero on open sets (positive outside, negative inside, zero only on the top and bottom circles), so it is a valid second example.
- Check flat-at-one-point: K = -6x/(1+x^3) for dx^2 + (1+x^3)^2 dy^2, d_x K = -6 at the origin, and the first covariant derivative of the curvature annihilates no nonzero vector.: Hand computation of K = -G''/G with G = 1 + x^3, numeric Riemann from the metric at x = 0, 0.2, -0.3, and the component form of nabla R from R = K(delta g - delta g) with nabla g = 0. → Numeric K matches -6x/(1+x^3) at all three points, d_x K = -6 at the origin, and (d_x K)(delta^rho_mu V_nu - delta^rho_nu V_mu) = 0 forces V = 0. The claim is right, including the constant-norm argument.
- Check mobius-and-cylinder: the flat cylinder has trivial holonomy, the flat Mobius band has holonomy {1, sigma} with sigma the reflection across the band.: Unrolled each as a quotient of a flat strip: the cylinder by a translation, the band by a glide reflection (x,y) -> (x+1,-y), and read off the linear part. → Correct, including that the fixed vectors are exactly those along the core, and that a flat non-orientable surface has holonomy in O(2) rather than SO(2).
- Derivation horizontal-lifts-bracket: [H_mu, H_nu] = -R^rho_{sigma mu nu} v^sigma d/dv^rho.: Recomputed each bracket: the two mixed brackets give (-d_mu Gamma + d_nu Gamma)v, and [A_mu, A_nu] gives (Gamma^rho_{nu lambda}Gamma^lambda_{mu sigma} - Gamma^rho_{mu lambda}Gamma^lambda_{nu sigma})v; compared the total with the conventions Riemann. → Exactly minus the course Riemann, so the sign in the key equation and the involutivity statement are right. The horizontal-lift definition also reproduces the transport equation, as step 1 claims.
- Formal way: the (a)-(b)-(c) equivalence, Ambrose-Singer, the one-vector criterion, and the smooth counterexample dx^2 + G^2 dy^2 with G = 1 + exp(-1/x) for x > 0.: Checked each implication against the standard statements (restricted holonomy trivial iff curvature vanishes; Hol = Hol^0 on simply connected sets; a vector extends iff holonomy fixes it; Ozeki's analytic result for the span of the nabla^m R), and differentiated the counterexample: G'' = exp(-1/x)(1-2x)/x^4. → All correct. G'' is nonzero for 0 < x < 1/2 while every nabla^m R vanishes on x <= 0, so the example does what the way says. The infinite necessity hierarchy (nabla^m R)s = 0 follows by induction from nabla s = 0.
- Problem brinkmann-wave-fields: k = d/dv is null and parallel, R^rho_{v mu nu} = 0, and d/dx fails both tests for H = A(u)(x^2 - y^2).: Built the metric numerically in coordinates (u,v,x,y) with A(u) = 0.7 + 0.3 sin u, computed Christoffels and the full Riemann tensor by central differences at a generic point, and compared with the quoted R_{uiuj} = -(1/2) d_i d_j H. → R_{uxux} = -0.816826 against -A = -0.816826, R_{uyuy} = +A, R_{uxuy} = 0; every lowered component carrying a v index vanishes; every Gamma^rho_{mu v} vanishes, so k is parallel; and nabla_u X_u = 0.653460 against A x = 0.653460. All parts of the problem, including the answer and key points, are correct.
- Check reducible-without-parallel-vector: S^2 x S^2 has holonomy SO(2) x SO(2), no parallel vector field, and its parallel forms are the constants, the constant combinations of the two area forms, and the volume form.: Decomposed the exterior algebra of R^2 + R^2 into weight spaces of the two independent rotations and looked for invariants in each degree. → Correct: degree 1 and 3 have no invariants, degree 2 has exactly the span of the two area forms (the mixed part carries weights (+-1,+-1)), degree 0 and 4 the constants and the volume form.
- Observation aharonov-bohm-ring: the loop phase is q Phi / hbar, and one superconducting flux quantum gives half a fringe.: Compared with the conventions gauge row (phase +q Phi/hbar around a loop, flux oriented by the right-hand rule); python for Phi = h/2e and e Phi / hbar. → Phi = 2.0678e-15 Wb and e Phi / hbar = pi exactly. The numbers line wrote e Phi / hbar for a phase that the convention gives as q Phi / hbar with q = -e for an electron; the observable half-fringe shift is the same either way, but the sign was unstated. Fixed by naming q = -e and quoting the magnitude.
- Notation trap slot-for-the-vector: contracting the second slot and contracting the last slot agree for the Levi-Civita connection but not for a general affine connection.: Checked with the pair symmetry R_{rho sigma mu nu} = R_{mu nu rho sigma}, which holds for a metric torsion-free connection and fails in general. → Correct, as is the remark that the homogeneous condition is insensitive to the overall Riemann sign convention.
- All thirteen references: authors, year, title, venue, and identifiers.: Web search against publisher and repository records (APS, Springer, De Gruyter, Numdam, EUDML, arXiv). → All confirmed: Snadden et al. 1998 PRL 81, 971-974 (doi 10.1103/PhysRevLett.81.971); Tonomura et al. 1986 PRL 56, 792-795 (doi added, 10.1103/PhysRevLett.56.792); Christoffel 1869 Crelle 70, 46-70; Frobenius 1877 Crelle 82, 230-315; Levi-Civita 1917 Rend. Circ. Mat. Palermo 42, 173-205; Brinkmann 1925 Math. Ann. 94, 119-145; Einstein 1928 Sitzungsberichte 217-221; Berger 1955 Bull. SMF 83, 279-330; de Rham 1952 Comment. Math. Helv. 26, 328-344; Wang 1989 Ann. Global Anal. Geom. 7, 59-68; Bryant, Seminaire Bourbaki expose 861, Asterisque 266, 351-374, arXiv math/9910059; Ehlers and Kundt 1962 in Witten's Gravitation, 49-101; Aldrovandi and Pereira 2013, Springer FTP 173. Every reference set to verified.
- History entries are correctly scoped.: Checked each contribution sentence against the content of the cited work. → Sound. Christoffel's four-index symbol did arise among the integrability conditions of the transformation problem; Frobenius's paper is the systematic treatment, and the note already credits Deahna and Clebsch for anticipating it; Levi-Civita 1917 is the parallelism paper; Brinkmann 1925 found the metrics with a covariantly constant null vector while studying conformally related Einstein spaces; Einstein 1928 is the Fernparallelismus paper. No claim of priority is overstated.
- Structure: prerequisites direct and acyclic, assumes consistent with them, formal rung staffed, tier requirements met.: Read the registry entries of all six prerequisites and searched for any concept listing this note as a prerequisite; matched every way's assumes against needed_for; counted formal checks and problems. → No cycles (nothing downstream lists this note, and no prerequisite reaches it). Every assumes id is a prerequisite at or below the way's rung. Two formal checks and one formal problem, a research way and three research-horizon topics with one review each: the advanced tier is satisfied.

**Counterexamples tried**

- Cone tip: the flat cone with the tip removed carries local parallel fields but none around the tip, holonomy being the rotation by the wedge angle. Verified numerically (30.0000 deg for a 30 deg wedge) and used in the worked example, the contrast way, and the entry common question.
- Hole with no curvature: the flat cylinder has trivial holonomy, so every vector extends. Tried against 'a global parallel field needs simple connectivity' and the note already says simple connectivity is sufficient, not necessary.
- Mobius band: holonomy is a reflection, not a rotation, so only vectors along the band extend. Tried against 'zero curvature gives global parallel fields'; the note's check and misconception cover it.
- Great circle: the equator bounds a hemisphere of area 2 pi a^2, so its holonomy is a whole turn and a carried arrow comes back matching. Tried against 'every loop on a ball turns a carried arrow'; the note never makes that claim and its entry sentences are scoped to small loops with a piece of the ball on the walker's left.
- Figure-eight loop: two equal lobes on opposite sides of a sphere give zero net turn. Tried against 'a perfect painting needs every small loop to bring copies back matching', which stays true (it is a necessary condition, not a test that any single loop passes).
- Region bigger than half a closed surface: a loop whose left-hand piece is most of a sphere turns by more than a full turn, so 'in proportion to the area' would need a modulo. The entry sentence is used only for shrinking loops and reads correctly there; no change made, but it must not be extended to large loops.
- Flat at one point only: dx^2 + (1+x^3)^2 dy^2 satisfies the algebraic condition at the origin for every vector and still admits no parallel field near it. Covered by the formal check.
- Smooth but not analytic: G = 1 + exp(-1/x) for x > 0 kills every nabla^m R on x <= 0 while K is nonzero just beyond. Verified by differentiating; covered in the formal way.
- Bent but intrinsically flat: a rolled paper tube returns every arrow unturned, so 'bent' is not 'curved'. The note keeps this distinction (cylinder check, flagship visual sketch).
- Nonzero curvature with a parallel field: the plane-fronted wave carries a parallel null vector, so the condition is not the same as flatness once the dimension exceeds two. Verified numerically for the Brinkmann metric.
- Reducible without a fixed vector: S^2 x S^2 has reducible holonomy and no parallel vector field. Tried against the holonomy principle bullet; the note's research check states it correctly.
- Nonvanishing but not parallel: a torus of revolution and a cap of a sphere both carry nonvanishing fields with no parallel one, separating curvature from the hairy-ball obstruction.
- Non-relativistic limit and a different observer: the tidal way's conclusion (a measured gradient rules out a parallel four-velocity at that event) uses only the value of R^mu_{nu rho sigma} u^nu at the event, so it survives a change of falling observer; no claim is made that a different u would pass.
- Coordinate effects: the flat plane in polar coordinates has nonzero connection coefficients and a parallel field through every vector, which is the note's control against reading Christoffel symbols as curvature.

**Fixes**

- Worked example parallel-field-on-a-cone, last step and answer: the lap was said to turn the field by delta after alpha fell by 2 pi - delta, with no branch named, and e_phi was glossed as 'the walker's left' although it is the direction of travel. Now states that a fall of 2 pi - delta is a rise of delta modulo a full turn, gives the sense as from e_r toward e_phi, and says that a walker going round in the direction of increasing phi keeps the tip on the left, so the turn is toward the walker's left. Verified numerically.
- Entry common question is-passing-every-small-loop-enough: the turn around the cone's tip was given as a size with no sense, unlike every other turn in the note. Now a separate short sentence says to keep the tip on your left, and that the copy comes back turned toward your left by the angle of the wedge, in the same words the entry way uses for the ball.
- Observation aharonov-bohm-ring: the numbers line quoted e Phi / hbar for a phase that the conventions give as q Phi / hbar, without saying that an electron has q = -e. Now names the charge and quotes the magnitude, and notes that the half-fringe shift is the same whichever sense the loop is taken in.
- Research way parallel-tensors-and-special-holonomy: the sentence splitting off a line from a parallel vector field carried no hypotheses of its own. Now says 'for such a manifold', keeping de Rham's completeness and simple connectivity, and adds that without completeness the splitting is only local.
- All thirteen references confirmed against publisher records and set to verified; added the missing DOI 10.1103/PhysRevLett.56.792 to the Aharonov-Bohm reference. No reference had to be corrected or removed.
- No entry-rung prose was changed, so the entry way explanations stay at 433 words, inside the review allowance the novice review used. The fixes added about 60 words to the examples and observations part (2082 of 2500) and about 10 to the tutoring part (3086 of 3500); both stay inside their caps.

**Concerns**

- The three novice rewrites flagged for this review all check out. The turn of a small loop on a ball is exactly proportional to the area of the piece on the walker's left and is toward that left (numeric transport confirms both); the paper-cone ring passes every small loop yet turns a copy by the wedge angle once around the tip (numeric lap 30.0000 deg for a 30 deg wedge); and the gravity answer's paraphrase is sound, since a parallel velocity field gives zero relative acceleration, so neighbours released with no relative velocity never drift.
- The entry claim that a carried copy on flat ground keeps pointing the same way is taken on trust at this rung, as the novice review noted. It is correct, and no lower rung in this note can carry it, so it must stay in the recap unless the entry rung of ricci-identity supplies it.
- The writer's overwrite question is still unresolved and this review does not settle it: the file was rebuilt as a fresh draft over a previously physics-reviewed revision 4, so the earlier physics record is gone. This review signs revision 3 of the rebuilt note. Snapshots are in the session scratchpad, including the pre-review state of this stage.
- All three visuals remain proposals with sketches only. The built catalog visual carry-an-arrow-around-a-loop fits the entry way, but its serves list omits this concept, so it still cannot be cited; that is an editor's or visual author's change, not one this note can make.
- The validator reports that the note's prerequisites differ from the registry entry for geodesic-deviation-equation, holonomy, lie-bracket and simply-connected-space. The note's list is the right one for its content, and sync_registry.py is meant to apply reviewed notes; an editor should run it.
- The entry rung says 'flat ground' while the prerequisite notes curvature/holonomy and curvature/ricci-identity say 'flat floor' for the same idea. Physically identical, so I made no change, but one phrase across the vault is an editor's call.

**Diff check** (2026-09-13, revision 4)

- Entry common question is-passing-every-small-loop-enough, changed sentence: 'But carry a copy once around the ring, all the way round the tip, keeping the tip on your left.' It must still set up the next sentence's claim that the copy comes back turned toward your left by the wedge angle.: Read the whole answer as one paragraph. Checked the verb against the note's fixed vocabulary (carry a copy, never let it swing, keeping a piece on your left, as the entry way and recap use them). Checked that the instruction is doable on the paper ring: the tip is outside the painted ring, so one sense of travel keeps it on the walker's left the whole way. Checked the orientation dependence by flipping the side of the paper the walker stands on. → Accurate and unchanged in claim. The re-read only restored the carrying, which the picture needs; the geometry is untouched. Keeping the tip on the walker's left puts the curvature-carrying region (the tip) on the left, so the conventions row makes the holonomy positive, that is toward the walker's left, and equal to the deficit angle, which is the wedge angle cut out. The statement is orientation-independent: standing on the other side of the paper swaps left and right in both the instruction and the outcome, so the pair stays true. No change.
- Observation aharonov-bohm-ring, changed numbers line, now two sentences: an electron has q = -e, so the phase difference has magnitude e Phi / hbar whichever sense the loop is taken in; and one superconducting flux quantum Phi = h/2e = 2.07e-15 Wb gives e Phi / hbar = pi, half a fringe spacing.: Re-derived from the connection sentence's q Phi / hbar with q = -e, so the magnitude is e Phi / hbar and only the sign follows the sense of traversal. Recomputed both numbers with python3 from the 2019 SI values h = 6.62607015e-34 J s and e = 1.602176634e-19 C, and checked the exact identity e (h/2e) / hbar = h / (2 hbar) = pi. Checked that a phase difference of pi is half of the 2 pi that separates neighbouring fringes. → Correct, and the split changed no claim: Phi = 2.0678e-15 Wb rounds to 2.07e-15, and e Phi / hbar = pi exactly, giving half a fringe. The 'so' still follows, since q = -e gives |q| = e. The sense-independence clause now sits on the magnitude sentence, which is where it belongs. No change.
- Worked example parallel-field-on-a-cone, changed step: 'Modulo a full turn, a fall of 2 pi - delta is a rise of delta, so the field comes back turned by delta in the sense from e_r toward e_phi.': Re-derived the whole example in course conventions: G = cr, Gamma^r_{phiphi} = -GG' = -c^2 r and Gamma^phi_{r phi} = G'/G = 1/r, giving V^r = A cos(c phi + phi_0), V^phi = -(A/c) sin(c phi + phi_0)/r, orthonormal V^rhat = A cos, V^phihat = -A sin, so alpha(phi) = -(c phi + phi_0) and alpha falls by 2 pi c = 2 pi - delta over one lap. Checked the branch arithmetic in python3 and integrated the transport equation numerically once round the tip at r = 2 for delta = 30 degrees with Runge-Kutta, 2,000,000 steps. → Correct. -(2 pi - delta) = delta - 2 pi is congruent to +delta modulo 2 pi, so 'a fall of 2 pi - delta is a rise of delta' is exact, and it now names the branch that the bare 'that is a rise of delta' left to the reader. Numeric lap: final orthonormal components (0.8660254, 0.5000000) from a start along e_r, norm 1.0000000, angle +30.000000 degrees from e_r toward e_phi. Same claim as before, with the pronoun repaired. No change.
- Worked example parallel-field-on-a-cone, new step: 'A walker going once round in the direction of increasing phi keeps the tip on the left, so that turn is toward the walker's left.': Checked against the conventions row on orientation and rotation sense. With (e_r, e_phi) positively oriented, a walker facing e_phi has e_phi rotated by +90 degrees in the e_r-toward-e_phi sense on the left, and that rotation carries e_phi to -e_r, which points at the tip. Checked the converse orientation as a counterexample: flipping the normal swaps both the side the tip is on and the meaning of a positive angle, so the two halves of the sentence flip together. → Correct and consistent with the same example's earlier step, which fixes the positive sense as from e_r toward e_phi. Splitting this off into its own step changed no claim; it separates the branch arithmetic from the statement about the walker. No change.
- Worked example parallel-field-on-a-cone, changed answer: 'For delta = 30 degrees, one lap around the tip turns the field by 30 degrees toward the left of a walker going round in the direction of increasing phi.': Compared with the steps it summarizes and with the numeric lap above. Tested the ambiguity the re-read was fixing: the old 'turns it by 30 degrees toward the walker's left' had a pronoun with two candidates and a walker who appeared nowhere in the answer. Also checked the unchanged first half of the answer by requiring cos and sin at phi = 2 pi to match their values at phi = 0, which needs 2 pi c in 2 pi Z, that is delta a multiple of 2 pi. → Accurate. The turn is +30 degrees for delta = 30 degrees, numerically confirmed, and naming the direction of travel is strictly more information than the old wording, not less. In the polar orientation the example already uses, that walker has the tip on the left, which the preceding step states, so the direction reference resolves. The single-valuedness condition is right as stated. No change.
- Consistency of the five changed strings with the rest of the note and with course conventions.: Searched every learner-visible field for 'left', 'wedge', 'cone', 'flux', 'fringe' and 'phase' and compared. Checked the entry answer's wedge-angle turn against the proposed visual paper-cone-with-a-missing-wedge (n laps give n times the wedge angle) and against the contrast way's cone treatment; checked the AB magnitude against the same observation's connection sentence; checked the 'carry a copy' and 'keeping the tip on your left' phrasings against the summary, the first entry way and the two entry checks. → Consistent everywhere. One turn word, one sense convention, one word per idea. The cone appears with the same wedge-angle holonomy in the worked example, the contrast way, the visual sketch and the entry common question, all with the turn toward the left of a walker who has the tip on the left.
- No new reference, equation, check, problem or numeric field was introduced by the re-read.: Compared the two revisions with note_diff.py over all rungs and inspected the diff by field address. → Confirmed: five strings, in one entry tutor answer, one observation numbers line and one worked example. Nothing in key_equations, derivations, checks, problems, numeric fields or references changed, so no tolerance or reference needed rechecking.
- Fix: No fixes. All five changed strings are accurate at their rung and claim exactly what they replaced, so no learner-visible text was touched and the revision stays at 4. Budgets are unchanged: 8519 words total of 10500, entry ways 433, examples and observations 2154 of 2500, tutoring 3096 of 3500.
- Fix: Set review.physics.reviewed_revision to 4, which clears the only validator warning.
