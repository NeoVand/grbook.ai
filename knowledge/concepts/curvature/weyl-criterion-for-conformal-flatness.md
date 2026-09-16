---
type: "concept"
schema_version: 2
id: "weyl-criterion-for-conformal-flatness"
title: "Weyl criterion for conformal flatness"
tagline: "When a curved spacetime is a flat one drawn at a scale that changes from place to place"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 3
updated: "2026-09-16"
aliases: ["vanishing Weyl tensor criterion", "conformally flat spacetime", "Weyl–Schouten theorem"]
prerequisites: ["weyl-tensor", "conformally-flat-metric", "conformal-time", "index-notation", "flatness-criterion", "bianchi-identity"]
leads_to: ["petrov-classification", "conformal-compactification", "penrose-diagram-of-flrw-spacetime", "weyl-curvature-hypothesis", "conformal-method-for-initial-data"]
visuals: ["angle-true-map-of-a-globe", "falling-ring-of-crumbs", "expanding-universe-on-a-flat-map"]
---

# Weyl criterion for conformal flatness

*When a curved spacetime is a flat one drawn at a scale that changes from place to place*

`weyl-criterion-for-conformal-flatness` · curvature · advanced · physics-reviewed (revision 3)

**Needs:** [[weyl-tensor]] (entry) · [[conformally-flat-metric]] (working) · [[conformal-time]] (working) · [[index-notation]] (working) · [[flatness-criterion]] (formal) · [[bianchi-identity]] (formal)  
**Opens:** [[petrov-classification]] · [[conformal-compactification]] · [[penrose-diagram-of-flrw-spacetime]] · [[weyl-curvature-hypothesis]] · [[conformal-method-for-initial-data]]  
**Related:** [[conformal-invariance]] · [[de-sitter-spacetime]] · [[space-of-constant-curvature]] · [[ricci-focusing-versus-weyl-shear]]  
**Visuals:** ★ [[angle-true-map-of-a-globe]] · [[falling-ring-of-crumbs]] · [[expanding-universe-on-a-flat-map]]

> A wall map of the world gets every angle right but draws Greenland far too big, because its scale changes from place to place. Every smooth surface has such a scale-only map. A spacetime, with its four directions, has one exactly when its Weyl tensor is zero everywhere in the region. That tensor holds the shape-changing part of the drift of falling crumbs. So a spacetime with a map is a flat spacetime drawn at a scale that changes from place to place.

## You will be able to

**Entry**
- Explain, using a wall map of the world, what a scale-only map is and why its scale must change from place to place. `objectives/explain-a-scale-only-map` ← `checks/africa-or-greenland`, `problems/one-idea-two-facts`
- Predict, from how a ball of freely falling crumbs drifts, whether a spacetime has a scale-only map, and say what a map does not mean. `objectives/decide-from-crumbs` ← `checks/crumbs-in-a-dust-universe`, `checks/scale-only-map-means-flat`

**Working**
- Compute the Gaussian curvature of a surface from the scale of its scale-only map. `objectives/compute-curvature-from-the-scale` ← `problems/stereographic-curvature`
- Distinguish conformally flat spacetimes from others using the Weyl tensor. `objectives/sort-spacetimes` ← `checks/schwarzschild-symmetric-claim`

**Formal**
- State the Weyl criterion with its dimension hypotheses, sketch its proof, and say where it stops. `objectives/state-and-prove` ← `checks/where-three-dimensions-fail`, `checks/slice-versus-spacetime`, `problems/closed-universe-on-a-flat-map`, `problems/conformally-flat-einstein-space`

**Research**
- Use conformal flatness, and its local character, to read cosmological Penrose diagrams and to assess conformally flat initial data. `objectives/place-the-criterion` ← `checks/no-horizons-in-de-sitter`

## Ways in

### 1. Greenland on the wall map · entry · picture

*How can a flat map of a round world get every angle right?*

Look at a wall map of the world, the flat map with straight lines for latitude and longitude. Greenland looks about as big as Africa. Yet Africa is about fourteen times bigger. So the map is wrong about sizes. It is not wrong about angles. Where a road crosses a river at a right angle on the ground, the two lines cross at a right angle on the map. A small round lake is drawn round. So the map keeps every angle and every small shape. It is wrong only about the scale.

A map that keeps every angle and is wrong only about the scale is called a scale-only map. In the middle of Greenland, each kilometre is drawn about three times longer than a kilometre at the equator. On a town map the scale barely changes, so nobody notices.

Why must the scale change? Try to press an orange peel flat: it tears or wrinkles. So no map at one scale can draw a round world. The wall map keeps every angle by letting its scale grow toward the poles instead.

Every smooth surface, however it curves, has a scale-only map of each small patch. A surface is smooth when it has no sharp tips, creases or edges. That is a theorem, first proved in the 1820s, taken on trust here. All of the surface's curving hides in the changing scale.

**Try it:** Find a wall map of the world. Compare Greenland with Africa. Then look at a small island near the top edge and find the same island on a globe, or in a map app zoomed out until the world is round. The shapes match; the map only draws the island bigger.

**Takeaway:** A scale-only map keeps every angle and every small shape and is wrong only about the scale, which changes from place to place. Every smooth surface has one for each small patch.

*Visuals:* [[angle-true-map-of-a-globe]]<br>*See:* `checks/africa-or-greenland`, `problems/one-idea-two-facts`

### 2. A ball of crumbs decides · entry · operational

*Does a spacetime have a scale-only map, and how could someone find out from inside it?*

**Recap:** In a cabin falling freely, let go a small ball of crumbs, all at rest. Their slow change of position is the drift. It is measured against the centre crumb with a ruler fixed to the cabin. With nothing around the cabin, or only dust at rest around it, the Weyl tensor holds the part of the drift that changes the ball's shape.

The scale-only map of 'Greenland on the wall map' has a spacetime version. It is a curved spacetime drawn as a flat one, at a scale that changes from place to place and from moment to moment. A spacetime does not always have one. It has one exactly when the Weyl tensor is zero everywhere in the region. So the ball of crumbs decides.

Beside a planet, in a cabin falling freely through empty space, the ball slowly becomes an egg, longer along the line to the planet and thinner across it. The Weyl tensor holds that shape change, so it is not zero. So spacetime around a planet has no scale-only map.

Now picture a universe filled evenly with dust, and a cabin falling freely, at rest among the dust. From that cabin every direction looks the same, so there is no direction for the ball to lengthen along. The dust pulls the crumbs together evenly, so the ball slowly shrinks, but it stays round. So the Weyl tensor is zero, and this universe is a flat spacetime drawn at a scale that changes with time. The universe itself is not flat, because the shrinking ball is real gravity.

**Takeaway:** A spacetime has a scale-only map exactly when its Weyl tensor is zero everywhere in the region. Beside a planet the ball becomes an egg and there is no map; in an evenly filled dust universe it stays round and there is one.

*What this leaves out:* The ball stays round for a cabin at rest among the dust. A cabin rushing through the dust finds the ball shrinking faster across its motion than along it, so the ball becomes an egg. That egg comes from the dust rushing past, not from the Weyl tensor, which stays zero.

*Continues:* `ways_in/greenland-on-the-wall-map`<br>*Builds on:* [[weyl-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/crumbs-in-a-dust-universe`, `checks/scale-only-map-means-flat`

### 3. The curvature hidden in the scale · working · calculation

*If a surface is a flat map at a varying scale, where does its curvature live?*

The wall map of 'Greenland on the wall map' is the Mercator map. On a sphere of radius $a$ with colatitude $\theta$, the angle from the North Pole, and longitude $\phi$, the map coordinates are $x = a\phi$ and $y = a\,\mathrm{artanh}(\cos\theta)$, which gives $\sin\theta = \mathrm{sech}(y/a)$ and

$$ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2) = \mathrm{sech}^2(y/a)\,(dx^2 + dy^2).$$

The sphere's metric is a positive function $\Omega^2 = \mathrm{sech}^2(y/a)$ times the flat metric of the map: it is conformally flat, and $\Omega$ is the map's scale, the ground length per unit map length. At the equator $\Omega = 1$. At latitude $72^\circ$, the middle of Greenland, $\theta = 18^\circ$ and $\Omega = \sin 18^\circ = 0.31$, so a kilometre of ground is drawn $1/0.31 = 3.2$ times longer than at the equator and areas come out $10.5$ times too large.

Every smooth surface admits such coordinates near each point; this is the existence of isothermal coordinates, a theorem of analysis stated here without proof. So the whole curvature must sit in $\Omega$. The derivation 'Gaussian curvature from the scale' gives

$$K = -\frac{1}{\Omega^2}\left(\frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}\right)\ln\Omega .$$

For the Mercator sphere $\ln\Omega = -\ln\cosh(y/a)$, whose second $y$-derivative is $-\mathrm{sech}^2(y/a)/a^2$, so $K = 1/a^2$, constant, as a sphere must have. A constant scale gives $K = 0$: then the map is exact and the surface is flat. A scale whose logarithm has zero Laplacian, such as $e^{\alpha x}$, gives $K = 0$ as well, so a changing scale is necessary for curvature but not sufficient. The second derivatives of $\ln\Omega$ are what measure it.

**Takeaway:** A surface with a scale-only map has metric Ω squared times the flat map metric, and its Gaussian curvature is minus the flat Laplacian of ln Ω divided by Ω squared; the Mercator sphere gives K equal to one over a squared.

*Continues:* `ways_in/greenland-on-the-wall-map`<br>*Builds on:* [[conformally-flat-metric]]<br>*Visuals:* [[angle-true-map-of-a-globe]]<br>*See:* `derivations/gaussian-curvature-from-the-scale`, `worked_examples/mercator-sphere`, `problems/stereographic-curvature`

### 4. Which spacetimes pass the test · working · contrast

*Which familiar spacetimes are conformally flat, and what does passing the test buy?*

The crumbs of 'A ball of crumbs decides' become a rule. In four or more dimensions a metric is locally conformally flat, $g_{\mu\nu} = \Omega^2\eta_{\mu\nu}$ in some coordinates near each point, exactly when its Weyl tensor vanishes throughout the region. This is the Weyl criterion, stated here and proved at the formal rung. It does not hold in three dimensions, where the Weyl tensor is zero for every metric and a different tensor decides, and it is not needed in two, where every metric passes.

The expanding universe passes. With conformal time $\eta$, defined by $c\,d\eta = c\,dt/a(t)$, the spatially flat FLRW metric becomes

$$ds^2 = a(\eta)^2\left(-c^2d\eta^2 + dx^2 + dy^2 + dz^2\right),$$

flat spacetime at the scale $\Omega = a(\eta)$. The closed and open models pass too, after a less obvious change of coordinates. Their Weyl tensors vanish because comoving observers find the same in every direction. Light rays are null curves, and a positive factor does not change where $ds^2 = 0$, so in conformal time they are the $45^\circ$ lines $dx = \pm c\,d\eta$ of flat spacetime. That is why conformal diagrams of cosmology look like pieces of a flat spacetime diagram.

Schwarzschild spacetime fails. It is a vacuum solution, so its Ricci tensor vanishes and its Weyl tensor is its whole Riemann tensor, with $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 48G^2M^2/c^4r^6 \neq 0$; its tides are the shape change the crumbs feel. No scale-only map draws the spacetime around a star, although space alone at one instant does have one.

Passing is not being flat. De Sitter spacetime, the far future of a universe with only dark energy, is conformally flat and has constant nonzero curvature: free-fall neighbours in it drift apart. Conformal flatness says only that the light cones are those of flat spacetime drawn at a varying scale.

**Takeaway:** In four or more dimensions a metric is locally conformally flat exactly when its Weyl tensor vanishes: FLRW and de Sitter pass, Schwarzschild fails, and passing means flat light cones at a varying scale, not flatness.

*Continues:* `ways_in/crumbs-decide-the-map`<br>*Builds on:* [[conformally-flat-metric]], [[conformal-time]], [[weyl-tensor]]<br>*Visuals:* [[expanding-universe-on-a-flat-map]]<br>*See:* `worked_examples/dust-universe-on-a-flat-map`, `checks/schwarzschild-symmetric-claim`

### 5. Flattening the Schouten tensor · formal · structure

*What exactly does the Weyl criterion assert, and why does a vanishing Weyl tensor let the metric be rescaled to a flat one?*

The rule of 'Which spacetimes pass the test' becomes a theorem once its objects are defined. Set $G = c = 1$. Let $(M, g)$ be a pseudo-Riemannian manifold of dimension $n \ge 3$ with its Levi-Civita connection, Schouten tensor $P_{ab} = \frac{1}{n-2}\big(R_{ab} - \frac{R}{2(n-1)}g_{ab}\big)$ and Ricci decomposition $R_{abcd} = C_{abcd} + (P \owedge g)_{abcd}$, where $(P \owedge g)_{abcd} = P_{ac}g_{bd} + P_{bd}g_{ac} - P_{ad}g_{bc} - P_{bc}g_{ad}$. The metric is *locally conformally flat* if every point has a neighbourhood carrying a positive function $\Omega$ with $\Omega^2 g$ flat.

**Theorem (Weyl, Schouten).** For $n \ge 4$, $g$ is locally conformally flat if and only if $C^a{}_{bcd} = 0$ on $M$. For $n = 3$, $C \equiv 0$ for every metric, and $g$ is locally conformally flat if and only if the Cotton tensor $\mathcal C_{abc} = \nabla_bP_{ac} - \nabla_cP_{ab}$ vanishes. For $n = 2$ every metric is locally conformally flat.

*Necessity.* Under $\tilde g = \Omega^2 g$ the Weyl tensor with one index up is unchanged, and a flat metric has $\tilde C = 0$, so $C = 0$.

*Sufficiency for $n \ge 4$.* Write $\Omega = e^{\sigma}$. The Schouten tensor transforms as

$$\tilde P_{ab} = P_{ab} - \nabla_a\nabla_b\sigma + \nabla_a\sigma\,\nabla_b\sigma - \tfrac12 g_{ab}\,\nabla_c\sigma\nabla^c\sigma,$$

stated here; it follows from the standard transformation of the Ricci tensor. Since $\tilde C = C = 0$, the rescaled Riemann tensor is $\tilde P \owedge \tilde g$, and $h \mapsto h \owedge \tilde g$ is injective for $n \ge 3$, so $\tilde g$ is flat exactly when $\tilde P = 0$. We therefore need a function $\sigma$ with

$$\nabla_a\nabla_b\sigma = \nabla_a\sigma\,\nabla_b\sigma - \tfrac12 g_{ab}\,\nabla_c\sigma\nabla^c\sigma + P_{ab}.$$

Set $W_a = \nabla_a\sigma$; the equation is a closed first-order system $\nabla_bW_a = S_{ab}(W, x)$ with $S$ symmetric. By the Frobenius theorem it has a local solution through any initial value $W_a(p)$ exactly when the second derivatives commute as the Ricci identity demands, $\nabla_c\nabla_bW_a - \nabla_b\nabla_cW_a = -R^d{}_{acb}W_d$. Substituting the system and using $R_{dacb} = (P \owedge g)_{dacb}$, every term quadratic or cubic in $W$ cancels and the terms linear in $W$ on the two sides agree identically; what remains is $\nabla_cP_{ab} - \nabla_bP_{ac} = 0$, the vanishing of the Cotton tensor (derivation 'Integrability of the flattening equation'). Contracting the second Bianchi identity gives $\nabla^dC_{dabc} = (n-3)\,\mathcal C_{abc}$ (derivation 'Divergence of the Weyl tensor'), so for $n \ge 4$ a vanishing Weyl tensor forces a vanishing Cotton tensor, the system is integrable, $W$ is a closed one-form because $S$ is symmetric, and $\sigma$ exists locally. The rescaled metric has $\tilde C = 0$ and $\tilde P = 0$, hence $\tilde R_{abcd} = 0$, and the flatness criterion supplies coordinates in which $\tilde g$ is constant.

*Three dimensions.* $C \equiv 0$ because the space of algebraic curvature tensors has dimension six, the same as the symmetric two-tensors, so $h \mapsto h \owedge g$ is onto. The divergence identity then reads $0 = 0$; the integrability condition $\mathcal C_{abc} = 0$ must be imposed on its own, and generic three-metrics violate it.

*Freedom.* The solution depends on $W_a(p)$ and $\sigma(p)$, $n + 1$ constants, and the flat metric is then fixed up to its own isometries; together this matches the $(n+1)(n+2)/2$-dimensional conformal group of flat space for $n \ge 3$.

**Takeaway:** For n at least four, a vanishing Weyl tensor is exactly conformal flatness: the flattening equation for ln Ω is integrable when the Cotton tensor vanishes, and the divergence identity makes that automatic.

*Picture:* The Ricci decomposition as two boxes, Weyl and Schouten; a conformal rescaling leaves the Weyl box untouched and moves the Schouten box by a second-derivative term, so an empty Weyl box is the only obstruction to emptying both.

*What this leaves out:* Smoothness of the metric is assumed throughout; the argument is local, and the pseudo-Riemannian signature is arbitrary.

*Continues:* `ways_in/which-spacetimes-pass`<br>*Builds on:* [[weyl-tensor]], [[flatness-criterion]], [[bianchi-identity]]<br>*See:* `derivations/divergence-of-the-weyl-tensor`, `derivations/integrability-of-the-flattening-equation`, `checks/where-three-dimensions-fail`, `problems/conformally-flat-einstein-space`

### 6. Where the criterion stops · formal · contrast

*What does the criterion not say: about two and three dimensions, about points and slices, and about the whole manifold?*

The Frobenius argument of 'Flattening the Schouten tensor' has edges, and each is a common error. Set $G = c = 1$.

*Two dimensions.* The Schouten tensor is undefined and the argument does not apply, yet the result is stronger. For a Riemannian surface, isothermal coordinates exist near every point, real-analytic metrics by Gauss and smooth ones by later work in analysis. For a Lorentzian surface, take the two families of null curves as coordinate lines $u$, $v$: then $ds^2 = -e^{2\sigma}\,du\,dv$, and $t = (u+v)/2$, $x = (v-u)/2$ give $e^{2\sigma}(-dt^2 + dx^2)$. The $(t, r)$ plane of Schwarzschild is conformally flat for this reason alone.

*Points versus regions.* The criterion is a statement about an open set. A Weyl tensor that vanishes at one event, or on one hypersurface, yields no conformally flat neighbourhood. The Schwarzschild slice $t = \mathrm{const}$ has three-metric $dr^2/(1 - 2M/r) + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, which $r = \rho(1 + M/2\rho)^2$ turns into $(1 + M/2\rho)^4\big(d\rho^2 + \rho^2(d\theta^2 + \sin^2\theta\,d\phi^2)\big)$: the slice is conformally flat and its Cotton tensor vanishes, while the spacetime's Weyl tensor, of size $M/r^3$, never does. Conformal flatness of a slice and of the spacetime are statements about different metrics.

*Vacuum.* If $R_{ab} = 0$ and $C_{abcd} = 0$ on an open set, then $R_{abcd} = 0$ there: conformally flat vacuum regions are flat, so no black hole exterior is conformally flat. More generally a conformally flat Einstein space, $R_{ab} = \Lambda g_{ab}$, has constant curvature $K = \Lambda/(n-1)$; in Lorentzian signature, de Sitter and anti-de Sitter are locally the only curved cases.

*Local versus global.* The word 'locally' cannot be dropped. The round sphere $S^2$ is locally conformally flat, but no conformal map takes all of it onto a region of the plane, because $S^2$ is compact and the plane is not; remove one point and stereographic projection does the job. For $n \ge 3$ a compact simply connected conformally flat manifold is conformally equivalent to the round sphere $S^n$ (Kuiper), and the conformal maps of flat space are the Möbius transformations (Liouville), a finite-dimensional group, unlike the holomorphic maps of the plane.

**Takeaway:** The criterion is local and needs an open set and four or more dimensions: surfaces always pass, three dimensions need the Cotton tensor, a conformally flat slice says nothing about the spacetime, and conformally flat vacuum is flat.

*Picture:* Four panels: a surface with its isothermal grid; a Schwarzschild slice drawn as flat space at a varying scale beside the spacetime whose light cones refuse; an empty vacuum region collapsing to Minkowski; and a sphere whose scale-only map needs one point removed.

*Continues:* `ways_in/flatten-the-schouten-tensor`<br>*Builds on:* [[flatness-criterion]], [[weyl-tensor]]<br>*See:* `checks/slice-versus-spacetime`, `problems/conformally-flat-einstein-space`, `problems/closed-universe-on-a-flat-map`

### 7. Where conformal flatness works today · research · bridge

*Where do the criterion, and the Cotton tensor behind it, appear in current research?*

The cosmological maps of 'Which spacetimes pass the test' and the limits in 'Where the criterion stops' both lead into current work. Set $G = c = 1$.

*Conformal infinity.* Penrose's compactification rescales a spacetime by a factor $\Omega$ that vanishes at infinity, so that infinity becomes a finite boundary of the rescaled metric and the causal structure can be drawn. For the FLRW models the rescaled metric is a piece of the Einstein static universe, or of Minkowski space, exactly because they are conformally flat; their Penrose diagrams are cut-outs of those. For asymptotically flat radiating spacetimes the rescaled metric is not flat, and whether it is smooth at null infinity, rather than differentiable a few times, depends on the fall-off of the Weyl tensor and is still studied.

*Weyl curvature hypothesis.* Penrose proposed that the initial singularity had vanishing Weyl curvature, so that the early universe was conformally flat and close to FLRW, while singularities inside black holes have divergent Weyl curvature. This ties the low gravitational entropy of the beginning to conformal flatness and offers the second law a geometric origin. Conformal cyclic cosmology goes further and identifies the conformally rescaled remote future of one aeon with the big bang of the next.

*Initial data.* The conformal method writes the spatial metric of a Cauchy slice as $\psi^4$ times a chosen conformal metric and solves the constraints for $\psi$; taking the conformal metric flat gives the Bowen–York and puncture data used for binary black holes. But Kerr admits no conformally flat slice compatible with its asymptotics, so conformally flat data for spinning holes are not slices of Kerr and shed spurious 'junk' radiation as they relax. Nonexistence was proved by Garat and Price and sharpened by Valiente Kroon; conformally curved data address it.

*Cotton, Bach and beyond.* In three dimensions the Cotton–York tensor, $Y^{ab} = \epsilon^{acd}\nabla_cP_d{}^b$ up to normalization, is the variation of the gravitational Chern–Simons term, and topologically massive gravity adds it to the Einstein tensor. In four dimensions the analogue is the Bach tensor $B_{ab} = \nabla^c\nabla^dC_{acbd} + \tfrac12R^{cd}C_{acbd}$: conformally invariant, trace-free, divergence-free, the field equation of Weyl-squared conformal gravity, and zero for every metric conformal to an Einstein metric. The ambient construction of Fefferman and Graham produces the obstruction tensor, its analogue in every even dimension, and their expansions underlie holographic renormalization in the AdS/CFT correspondence.

*Global questions.* Kuiper's theorem, that a compact simply connected conformally flat manifold is conformally the round sphere, and Liouville's theorem, that conformal maps of flat space in three or more dimensions are Möbius transformations, make conformal flatness rigid in a way surfaces are not; conformally flat Lorentzian manifolds and their developing maps remain an active corner of geometry.

**Takeaway:** Conformal flatness underlies cosmological Penrose diagrams, the Weyl curvature hypothesis and conformally flat initial data, while the Cotton, Bach and obstruction tensors carry the criterion into conformal gravity and holography.

*Picture:* A Penrose diagram of a dust universe cut from the Einstein static cylinder, beside a Bowen–York puncture slice radiating junk, beside the ladder Cotton, Bach, obstruction indexed by dimension.

*Continues:* `ways_in/which-spacetimes-pass`, `ways_in/where-the-criterion-stops`<br>*Builds on:* [[weyl-tensor]]<br>*See:* `checks/no-horizons-in-de-sitter`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| wall map | — | The usual flat map of the whole world, with straight lines for latitude and longitude, on which Greenland looks as big as Africa. Mapmakers call it the Mercator map. | — |
| scale | — | How much ground one centimetre of map stands for. On a scale-only map it is different at different places. | — |
| scale-only map | — | A flat drawing of a curved surface or spacetime that keeps every angle and every small shape and is wrong only about the scale. Physicists say the surface or spacetime is conformally flat. | [[conformally-flat-metric]] |
| patch | — | A small piece of a surface with no holes. | — |
| region | — | A piece of spacetime with room around every point in it, rather than a single point or moment. | — |
| spacetime | — | Space and time taken together as one world with four directions, three of space and one of time. In a flat spacetime, a ball of crumbs let go at rest keeps its size and its shape for ever. | — |
| Weyl tensor | VILE tensor | The table, kept at every place, that holds the part of the drift that matter at the spot does not set. In empty space, or among dust at rest, that is the part that changes the ball's shape. | [[weyl-tensor]] |
| smooth | — | A surface is smooth when it has no sharp tips, creases or edges, so every small patch of it looks like a gently bent sheet. | — |
| shape-changing part | — | What is left of the drift once the part that is the same in every direction is taken away. It stretches a ball of crumbs into an egg. | [[weyl-tensor]] |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | — |
| drift | — | The slow change of position of crumbs let go at rest in a freely falling cabin, measured against the centre crumb with a ruler fixed to the cabin. | — |
| dust | — | Matter spread out as separate grains that do not push on one another, the physicist's model for galaxies. | — |

## Key equations

### Weyl criterion · working

$$
C^{\rho}{}_{\sigma\mu\nu} = 0 \ \text{on } U \iff g \ \text{is locally conformally flat on } U \qquad (n \ge 4)
$$

In four or more dimensions, the Weyl tensor vanishes on a region exactly when the metric there is flat at a varying scale.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C^{\rho}{}_{\sigma\mu\nu}$ | Weyl tensor | the Weyl tensor |
| $U$ | open region of the manifold | the region |

**Holds when:** Dimension $n \ge 4$, smooth metric of any signature, Levi-Civita connection; in $n = 3$ the Cotton tensor decides, in $n = 2$ every metric qualifies.  
**Say it:** “In four or more dimensions, the Weyl tensor vanishes on a region if and only if the metric is locally conformally flat there.”  
**Justified by:** `stated`

### Gaussian curvature from the scale · working

$$
ds^2 = \Omega^2(dx^2 + dy^2) \ \Rightarrow\ K = -\frac{1}{\Omega^2}\left(\partial_x^2 + \partial_y^2\right)\ln\Omega
$$

For a surface drawn as a flat map at scale $\Omega$, the Gaussian curvature is minus the flat Laplacian of $\ln\Omega$ divided by $\Omega^2$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature of the surface | the Gaussian curvature |
| $\Omega$ | scale of the map, ground length per unit map length | omega |

**Holds when:** Two dimensions, isothermal coordinates $x, y$, flat Laplacian; $K$ is the course sectional curvature of the only plane.  
**Say it:** “K equals minus one over omega squared times the flat Laplacian of the logarithm of omega.”  
**Justified by:** `derivations/gaussian-curvature-from-the-scale`

### Spatially flat FLRW metric in conformal time · working

$$
ds^2 = a(\eta)^2\left(-c^2d\eta^2 + dx^2 + dy^2 + dz^2\right),\qquad c\,d\eta = \frac{c\,dt}{a(t)}
$$

The spatially flat expanding universe is flat spacetime drawn at the scale $a(\eta)$; light rays are the lines $dx = \pm c\,d\eta$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $a(\eta)$ | scale factor as a function of conformal time | a of eta |
| $\eta$ | conformal time | eta |

**Holds when:** Spatially flat FLRW model, $k = 0$; the closed and open models are conformally flat too but need a further change of coordinates.  
**Say it:** “d s squared equals a of eta squared times minus c squared d eta squared plus d x squared plus d y squared plus d z squared, with c d eta equal to c d t over a of t.”  
**Justified by:** `conformal-time`

### Schouten tensor under a conformal rescaling · formal

$$
\tilde g_{ab} = e^{2\sigma}g_{ab}\ \Rightarrow\ \tilde P_{ab} = P_{ab} - \nabla_a\nabla_b\sigma + \nabla_a\sigma\,\nabla_b\sigma - \tfrac12 g_{ab}\,\nabla_c\sigma\nabla^c\sigma
$$

Rescaling by $e^{2\sigma}$ shifts the Schouten tensor by derivatives of $\sigma$; the flattening equation asks this shift to cancel $P_{ab}$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $P_{ab}$ | Schouten tensor | the Schouten tensor |
| $\sigma$ | logarithm of the conformal factor, $\Omega = e^{\sigma}$ | sigma |

**Holds when:** $G = c = 1$, $n \ge 3$, Levi-Civita connections of $g$ and $\tilde g$; derivatives and the contraction on the right use $g$.  
**Say it:** “The rescaled Schouten tensor is the Schouten tensor, minus the second derivative of sigma, plus the product of its first derivatives, minus half the metric times its squared gradient.”  
**Justified by:** `stated`

### Divergence of the Weyl tensor · formal

$$
\nabla^dC_{dabc} = (n-3)\,\mathcal C_{abc},\qquad \mathcal C_{abc} = \nabla_bP_{ac} - \nabla_cP_{ab}
$$

The divergence of the Weyl tensor is $n - 3$ times the Cotton tensor, so for $n \ge 4$ a vanishing Weyl tensor forces a vanishing Cotton tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal C_{abc}$ | Cotton tensor, antisymmetric in its last two indices | the Cotton tensor |
| $C_{dabc}$ | Weyl tensor, all indices down | the Weyl tensor |

**Holds when:** $G = c = 1$, $n \ge 3$, Levi-Civita connection.  
**Say it:** “The divergence of the Weyl tensor on its first index equals n minus three times the Cotton tensor.”  
**Justified by:** `derivations/divergence-of-the-weyl-tensor`

## Derivations

### Gaussian curvature from the scale · working

**Goal:** For $ds^2 = e^{2\sigma}(dx^2 + dy^2)$, show that $K = -e^{-2\sigma}(\sigma_{xx} + \sigma_{yy})$, subscripts denoting partial derivatives.

1. The metric components are $g_{xx} = g_{yy} = e^{2\sigma}$ and $g_{xy} = 0$, with inverse $g^{xx} = g^{yy} = e^{-2\sigma}$.
2. The course formula $\Gamma^\lambda{}_{\mu\nu} = \tfrac12 g^{\lambda\kappa}(\partial_\mu g_{\kappa\nu} + \partial_\nu g_{\kappa\mu} - \partial_\kappa g_{\mu\nu})$ gives $\Gamma^x{}_{xx} = \sigma_x$, $\Gamma^x{}_{xy} = \sigma_y$, $\Gamma^x{}_{yy} = -\sigma_x$, $\Gamma^y{}_{yy} = \sigma_y$, $\Gamma^y{}_{xy} = \sigma_x$ and $\Gamma^y{}_{xx} = -\sigma_y$.
3. The course Riemann tensor gives $R^x{}_{yxy} = \partial_x\Gamma^x{}_{yy} - \partial_y\Gamma^x{}_{xy} + \Gamma^x{}_{x\lambda}\Gamma^\lambda{}_{yy} - \Gamma^x{}_{y\lambda}\Gamma^\lambda{}_{xy}$.
4. The derivative terms are $-\sigma_{xx} - \sigma_{yy}$.
5. The product terms are $\Gamma^x{}_{xx}\Gamma^x{}_{yy} + \Gamma^x{}_{xy}\Gamma^y{}_{yy} - \Gamma^x{}_{yx}\Gamma^x{}_{xy} - \Gamma^x{}_{yy}\Gamma^y{}_{xy} = -\sigma_x^2 + \sigma_y^2 - \sigma_y^2 + \sigma_x^2 = 0$.
6. Lowering the index, $R_{xyxy} = g_{xx}R^x{}_{yxy} = -e^{2\sigma}(\sigma_{xx} + \sigma_{yy})$.
7. The course sectional curvature of the only plane is $K = R_{xyxy}/(g_{xx}g_{yy} - g_{xy}^2) = -e^{2\sigma}(\sigma_{xx} + \sigma_{yy})/e^{4\sigma}$.

**Result:** $K = -e^{-2\sigma}(\sigma_{xx} + \sigma_{yy}) = -\Omega^{-2}(\partial_x^2 + \partial_y^2)\ln\Omega$ with $\Omega = e^{\sigma}$.

### Divergence of the Weyl tensor · formal

**Goal:** Show that $\nabla^aC_{abcd} = (n-3)(\nabla_cP_{bd} - \nabla_dP_{bc})$ for $n \ge 3$, with $G = c = 1$.

1. The second Bianchi identity $\nabla_eR_{abcd} + \nabla_cR_{abde} + \nabla_dR_{abec} = 0$, contracted with $g^{ae}$ and using $R^a{}_{bda} = -R_{bd}$ and $R^a{}_{bac} = R_{bc}$, gives $\nabla^aR_{abcd} = \nabla_cR_{bd} - \nabla_dR_{bc}$.
2. Contracting once more gives $\nabla^aR_{ab} = \tfrac12\nabla_bR$, hence $\nabla^aP_{ab} = \nabla_bP$ with $P = g^{ab}P_{ab} = R/(2(n-1))$.
3. Substitute $R_{abcd} = C_{abcd} + (P \owedge g)_{abcd}$. The divergence of the second term is $\nabla^a(P \owedge g)_{abcd} = \nabla_cP\,g_{bd} + \nabla_cP_{bd} - \nabla_dP\,g_{bc} - \nabla_dP_{bc}$.
4. Since $R_{bd} = (n-2)P_{bd} + P\,g_{bd}$, the right side of step 1 equals $(n-2)(\nabla_cP_{bd} - \nabla_dP_{bc}) + \nabla_cP\,g_{bd} - \nabla_dP\,g_{bc}$.
5. Subtracting step 3 from step 4, the trace terms cancel and $\nabla^aC_{abcd} = (n-3)(\nabla_cP_{bd} - \nabla_dP_{bc})$.

**Result:** $\nabla^aC_{abcd} = (n-3)\,\mathcal C_{bcd}$ with $\mathcal C_{bcd} = \nabla_cP_{bd} - \nabla_dP_{bc}$; for $n = 3$ both sides vanish identically.

### Integrability of the flattening equation · formal

**Goal:** Given $C_{abcd} = 0$, show that the system $\nabla_bW_a = W_aW_b - \tfrac12 g_{ab}W^2 + P_{ab}$ is locally solvable exactly when the Cotton tensor vanishes, with $G = c = 1$.

1. Write $S_{ab} = W_aW_b - \tfrac12 g_{ab}W^2 + P_{ab}$ with $W^2 = W_cW^c$, so the system reads $\nabla_bW_a = S_{ab}$ with $S$ symmetric.
2. Differentiate and substitute the system for every derivative of $W$: $\nabla_c\nabla_bW_a = S_{ac}W_b + W_aS_{bc} - W^dS_{dc}\,g_{ab} + \nabla_cP_{ab}$.
3. Antisymmetrize in $b$ and $c$. The terms with $W^2$ are $-\tfrac12W^2(g_{ac}W_b - g_{ab}W_c) - \tfrac12W^2(W_cg_{ab} - W_bg_{ac}) = 0$, and the cubic terms $W_aW_cW_b - W_aW_bW_c$ cancel.
4. The terms linear in $W$ are $P_{ac}W_b - P_{ab}W_c - P_{cd}W^dg_{ab} + P_{bd}W^dg_{ac}$.
5. The Ricci identity for a covector requires $\nabla_c\nabla_bW_a - \nabla_b\nabla_cW_a = -R^d{}_{acb}W_d$. With $C = 0$, $R_{dacb} = (P \owedge g)_{dacb}$, and the right side becomes $P_{ac}W_b - P_{ab}W_c - P_{cd}W^dg_{ab} + P_{bd}W^dg_{ac}$, identical to step 4.
6. What survives is $\nabla_cP_{ab} - \nabla_bP_{ac} = 0$: the Cotton tensor must vanish. Conversely, when it does, the Frobenius theorem gives a local solution $W$ through any initial value, $W$ is closed because $S$ is symmetric, and $\sigma$ with $d\sigma = W$ exists locally.

**Result:** Given $C_{abcd} = 0$, the flattening equation is locally solvable if and only if $\mathcal C_{abc} = 0$.

## Worked examples

### The Mercator sphere · working

**Problem:** Show that the Mercator map of a sphere of radius $a$ is a scale-only map, find its scale, and check that the curvature hidden in the scale is $1/a^2$.

1. On the sphere, $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$ with colatitude $\theta$ and longitude $\phi$.
2. Set $x = a\phi$ and $y = a\,\mathrm{artanh}(\cos\theta)$. Then $dy = -a\,d\theta/\sin\theta$ and $\tanh(y/a) = \cos\theta$, so $\mathrm{sech}(y/a) = \sin\theta$.
3. Hence $ds^2 = \sin^2\theta\,(dx^2 + dy^2) = \mathrm{sech}^2(y/a)(dx^2 + dy^2)$: the flat map metric times $\Omega^2$ with $\Omega = \sin\theta$.
4. $\ln\Omega = -\ln\cosh(y/a)$, so $\partial_y^2\ln\Omega = -\mathrm{sech}^2(y/a)/a^2$ and $\partial_x^2\ln\Omega = 0$.
5. $K = -\Omega^{-2}(\partial_x^2 + \partial_y^2)\ln\Omega = \cosh^2(y/a)\,\mathrm{sech}^2(y/a)/a^2 = 1/a^2$.

**Answer:** $\Omega = \sin\theta$, the cosine of the latitude, and $K = 1/a^2$ everywhere; at latitude $72^\circ$, $\Omega = 0.31$.

**Takeaway:** The map keeps angles, its scale carries the whole curvature, and the formula returns the constant value a sphere must have.

### A dust universe on a flat map · working

**Problem:** A spatially flat universe of dust has $a(t) = (t/t_0)^{2/3}$, with $a = 1$ today at $t = t_0$. Write its metric as flat spacetime at a varying scale, and find how far light has travelled since $t = 0$.

1. Conformal time: $\eta = \int_0^t dt'/a(t') = 3t_0^{2/3}t^{1/3}$, so $\eta_0 = 3t_0$ today and $a = (\eta/\eta_0)^2$.
2. With $c\,dt = a\,c\,d\eta$, $ds^2 = a(\eta)^2(-c^2d\eta^2 + dx^2 + dy^2 + dz^2)$: flat spacetime at the scale $\Omega = a(\eta) = (\eta/3t_0)^2$.
3. A radial light ray obeys $dx = c\,d\eta$ on the map, so since $\eta = 0$ it has covered the map distance $c\eta_0 = 3ct_0$.
4. Today $a = 1$, so map distance equals present proper distance: for $t_0 = 13.8$ billion years, taken for illustration, $3ct_0 = 41$ billion light-years.

**Answer:** $ds^2 = (\eta/3t_0)^4(-c^2d\eta^2 + dx^2 + dy^2 + dz^2)$; light from $t = 0$ has reached the map distance $3ct_0$, about $41$ billion light-years.

**Takeaway:** The scale factor is the map's scale, and light's 45-degree lines on the map make horizon distances a one-line calculation.

## Problems

### `one-idea-two-facts` · entry · difficulty 1 · conceptual

On a wall map of the world, Greenland looks about as big as Africa, yet Africa is about fourteen times bigger. A small round lake in Greenland still looks round on the map. In the middle of Greenland the map draws each kilometre about three times longer than at the equator. Explain both facts with one idea, and estimate how many times too big Greenland's area comes out.

**Hints**

1. What happens to the area of a small square when every side is drawn three times longer?

**Answer:** The map keeps every angle, so small shapes like the lake stay round. It is wrong only about the scale, and at Greenland the scale is about three times the equator's, so Greenland's area comes out about three times three, roughly ten times too big.

**Must contain:** The map keeps every angle and every small shape; Only the scale is wrong, growing toward the poles; Three times longer each way makes about ten times the area

**Numeric:** factor by which Greenland's area is drawn too big = 10 1 (magnitude, ±2)

**Solution**

1. The lake stays round because the map keeps every angle, and a small round shape is made of angles between its tiny pieces.
2. Greenland is drawn too big because the scale there is about three times the scale at the equator. So every stretch of Greenland is drawn about three times longer than the same stretch at the equator.
3. Three times longer across and three times longer up and down makes about nine times the area, roughly ten. Africa lies near the equator, where the scale is smallest, so a fourteen-fold real difference almost vanishes on the map.

**Targets:** `map-has-one-wrong-scale`

### `stereographic-curvature` · working · difficulty 2 · calculation

Projecting a sphere of radius $a$ from its north pole onto the plane through its equator gives the map metric $ds^2 = \dfrac{4a^4\,(dx^2 + dy^2)}{(a^2 + x^2 + y^2)^2}$. Find the scale $\Omega$ at the south pole, show that $K = 1/a^2$, and give $K$ for Earth, $a = 6371$ km.

**Hints**

1. Write $\ln\Omega$ with $r^2 = x^2 + y^2$; for a function $f(r)$ the flat Laplacian is $f'' + f'/r$.

**Answer:** The south pole is $x = y = 0$, where $\Omega^2 = 4$, so $\Omega = 2$. $K = 1/a^2$ everywhere; for Earth $K = 2.46\times10^{-14}\ \mathrm{m^{-2}}$.

**Must contain:** Omega is 2 at the south pole; The Laplacian of ln(a squared plus r squared) is 4 a squared over (a squared plus r squared) squared; K equals 1 over a squared everywhere

**Numeric:** scale Omega at the south pole = 2 1 (magnitude, ±0.05); Gaussian curvature of Earth's surface = 2.464e-14 m^-2 (magnitude, ±2%)

**Solution**

1. $\Omega = 2a^2/(a^2 + r^2)$, so $\ln\Omega = \ln(2a^2) - \ln(a^2 + r^2)$, and at $r = 0$, the image of the south pole, $\Omega = 2$.
2. With $f = \ln(a^2 + r^2)$: $f' = 2r/(a^2 + r^2)$ and $f'' = 2(a^2 - r^2)/(a^2 + r^2)^2$, so $f'' + f'/r = 4a^2/(a^2 + r^2)^2$.
3. $K = -\Omega^{-2}(\partial_x^2 + \partial_y^2)\ln\Omega = \dfrac{(a^2 + r^2)^2}{4a^4}\cdot\dfrac{4a^2}{(a^2 + r^2)^2} = \dfrac{1}{a^2}$; for $a = 6.371\times10^6\ \mathrm{m}$ this is $2.46\times10^{-14}\ \mathrm{m^{-2}}$.

### `closed-universe-on-a-flat-map` · formal · difficulty 3 · calculation

Set $G = c = 1$. The closed FLRW metric is $ds^2 = a(\eta)^2\big(-d\eta^2 + d\chi^2 + \sin^2\chi\,(d\theta^2 + \sin^2\theta\,d\phi^2)\big)$. Using $t - r = \tan\tfrac{\eta - \chi}{2}$ and $t + r = \tan\tfrac{\eta + \chi}{2}$, show that the bracket equals $(\cos\eta + \cos\chi)^{2}\big(-dt^2 + dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)\big)$, conclude that the closed universe is conformally flat, and evaluate the factor multiplying the Minkowski metric at $\eta = \chi = 0$ for $a = 1$.

**Hints**

1. Write $p = (\eta - \chi)/2$ and $q = (\eta + \chi)/2$; then $dt^2 - dr^2 = d(t - r)\,d(t + r)$.
2. $r = (\tan q - \tan p)/2 = \sin\chi/(2\cos p\cos q)$, and $2\cos p\cos q = \cos\eta + \cos\chi$.

**Answer:** $-d\eta^2 + d\chi^2 + \sin^2\chi\,d\Sigma^2 = (\cos\eta + \cos\chi)^2(-dt^2 + dr^2 + r^2d\Sigma^2)$ with $d\Sigma^2$ the round two-sphere metric, so the closed universe is $[a(\eta)(\cos\eta + \cos\chi)]^2$ times Minkowski space wherever $|\eta| + \chi < \pi$; at $\eta = \chi = 0$ with $a = 1$ the factor is $4$.

**Must contain:** The null coordinates map to the null coordinates of Minkowski space; Sine squared chi equals (cos eta plus cos chi) squared times r squared; The conformal factor is a of eta times (cos eta plus cos chi), positive on each patch

**Numeric:** factor multiplying the Minkowski metric at eta = chi = 0, a = 1 = 4 1 (magnitude, ±0.01)

**Solution**

1. With $p = (\eta - \chi)/2$ and $q = (\eta + \chi)/2$, $t - r = \tan p$ and $t + r = \tan q$, so $d(t - r)\,d(t + r) = \sec^2p\,\sec^2q\,dp\,dq = \sec^2p\,\sec^2q\,(d\eta^2 - d\chi^2)/4$.
2. Since $-dt^2 + dr^2 = -d(t - r)\,d(t + r)$, this gives $-d\eta^2 + d\chi^2 = 4\cos^2p\cos^2q\,(-dt^2 + dr^2)$.
3. $r = (\tan q - \tan p)/2 = \sin(q - p)/(2\cos p\cos q) = \sin\chi/(2\cos p\cos q)$, so $\sin^2\chi = 4\cos^2p\cos^2q\,r^2$: the angular parts match with the same factor.
4. $2\cos p\cos q = \cos(q - p) + \cos(q + p) = \cos\chi + \cos\eta$, so the closed FLRW metric is $[a(\eta)(\cos\eta + \cos\chi)]^2$ times Minkowski space: conformally flat, with $\Omega = a(\eta)(\cos\eta + \cos\chi)$.
5. The map covers one patch $|\eta \pm \chi| < \pi$ at a time, where $\Omega > 0$. At $\eta = \chi = 0$ and $a = 1$, $\Omega^2 = 4$.

### `conformally-flat-einstein-space` · formal · difficulty 2 · proof

Set $G = c = 1$ and $n \ge 3$. Show that a conformally flat Einstein space, $R_{ab} = \Lambda g_{ab}$, has constant curvature, find $K$ in terms of $\Lambda$ and $n$, and deduce that a conformally flat vacuum region is flat.

**Hints**

1. With $C = 0$, the Riemann tensor is $P \owedge g$, and $P$ is a multiple of the metric.

**Answer:** $R_{abcd} = \dfrac{\Lambda}{n-1}(g_{ac}g_{bd} - g_{ad}g_{bc})$, so $K = \Lambda/(n-1)$, which is $\Lambda/3$ in four dimensions; $\Lambda = 0$ gives $R_{abcd} = 0$, and the flatness criterion makes the region flat.

**Must contain:** The Schouten tensor of an Einstein space is lambda over 2(n minus 1) times the metric; K equals lambda over (n minus 1); vacuum gives zero Riemann tensor

**Numeric:** K divided by Lambda for n = 4 = 0.3333 1 (signed, ±0.001)

**Solution**

1. $R = n\Lambda$, so $P_{ab} = \dfrac{1}{n-2}\Big(\Lambda - \dfrac{n\Lambda}{2(n-1)}\Big)g_{ab} = \dfrac{\Lambda}{2(n-1)}\,g_{ab}$.
2. Conformal flatness gives $C_{abcd} = 0$, so $R_{abcd} = (P \owedge g)_{abcd} = \dfrac{\Lambda}{2(n-1)}\big(2g_{ac}g_{bd} - 2g_{ad}g_{bc}\big) = \dfrac{\Lambda}{n-1}(g_{ac}g_{bd} - g_{ad}g_{bc})$.
3. The course sectional curvature of any plane is then $K = \Lambda/(n-1)$: constant, and $\Lambda/3$ for $n = 4$, matching $\Lambda = 3K$ for spaces of constant curvature.
4. Vacuum is $\Lambda = 0$, so $R_{abcd} = 0$ on the open set, and the flatness criterion gives coordinates near each point in which the metric is constant.

## Observations

- **Two high tides a day at most coasts, raised by the Moon and the Sun.** (measured, entry). The Moon stretches Earth along the line toward it and squeezes it across: the shape-changing drift the Weyl tensor holds. So the Weyl tensor near Earth is not zero, and spacetime around Earth has no scale-only map. *Numbers:* At most coasts one high tide follows the last by about twelve and a half hours. At many coasts the sea rises by a metre or more between low and high tide.
- **Cosmic shear: coherent stretching of distant galaxy images by the lumpy matter along the line of sight.** (measured, working). In an exactly conformally flat universe the Weyl tensor vanishes, so light bundles are magnified or shrunk but never sheared. The measured shear is Weyl curvature along the line of sight: the departure from the smooth conformally flat model that lumpy matter produces. *Numbers:* Root-mean-square shear of order $10^{-2}$ on scales of a few arcminutes. *Reference:* David J. Bacon, Alexandre R. Refregier, Richard S. Ellis (2000), *Detection of weak gravitational lensing by large-scale structure*, Monthly Notices of the Royal Astronomical Society 318, 625–640, doi:10.1046/j.1365-8711.2000.03851.x

## Teaching arc

1. **Open with the wall map** (entry). Ask which is really bigger, Greenland or Africa, have the learner say what the map gets right before what it gets wrong, then name the scale-only map and give it to every smooth surface. *Why:* Sizes wrong, angles right is the whole idea, met on an object every learner has seen. *Predict:* Which is really bigger, Greenland or Africa, and by about how much? *Visual:* [[angle-true-map-of-a-globe]] *Uses:* `ways_in/greenland-on-the-wall-map`, `checks/africa-or-greenland`, `problems/one-idea-two-facts`
2. **Let the crumbs decide** (entry). Run the planet and the dust universe after a prediction, state the criterion, then hit the belief that a map means flatness. *Why:* The criterion becomes a test the learner can picture, with real gravity inside the map. *Predict:* In the dust universe, does the ball of crumbs keep its size, and does it keep its round shape? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/crumbs-decide-the-map`, `checks/crumbs-in-a-dust-universe`, `checks/scale-only-map-means-flat`
3. **Compute the scale and sort the spacetimes** (working). Derive the Mercator metric and the curvature-from-scale formula, then write FLRW in conformal time and show why Schwarzschild fails. *Why:* The scale carries curvature in a case the learner can compute, then the same structure appears in spacetime. *Predict:* In conformal time, what do light rays look like on the diagram? *Visual:* [[expanding-universe-on-a-flat-map]] *Uses:* `ways_in/curvature-hidden-in-the-scale`, `worked_examples/mercator-sphere`, `ways_in/which-spacetimes-pass`, `checks/schwarzschild-symmetric-claim`
4. **State the theorem and walk the proof** (formal). State the theorem with its dimensions, walk the Frobenius argument and the divergence identity, then tour the edges. *Why:* The dimension hypotheses and the local character are where graduate students go wrong. *Uses:* `ways_in/flatten-the-schouten-tensor`, `derivations/divergence-of-the-weyl-tensor`, `ways_in/where-the-criterion-stops`, `checks/where-three-dimensions-fail`, `checks/slice-versus-spacetime`
5. **Place the criterion in current work** (research). Connect conformal flatness to Penrose diagrams, the Weyl curvature hypothesis and initial data, then test local against global on de Sitter. *Why:* Research use is where 'local' stops being a footnote. *Uses:* `ways_in/conformal-flatness-in-research`, `checks/no-horizons-in-de-sitter`

## Misconceptions

### “The wall map is just drawn at the wrong scale; a better single scale would fix Greenland.” · entry · `map-has-one-wrong-scale`

- **Why it is tempting:** Every map in daily life has one scale printed in its corner.
- **What is true:** A round world cannot be drawn flat at one scale at all, just as an orange peel cannot be pressed flat without tearing. The wall map keeps every angle by letting its scale change from place to place, and that change makes Greenland huge.
- **Exposed by:** `checks/africa-or-greenland`

### “A spacetime with a scale-only map is flat, so there is no gravity in it.” · entry · `conformally-flat-means-flat`

- **Why it is tempting:** A bigger or smaller copy of flat spacetime seems to change nothing.
- **What is true:** The scale changes from place to place, and that change is curving. In the dust universe a ball of crumbs shrinks, which never happens in flat spacetime.
- **Exposed by:** `checks/scale-only-map-means-flat`

### “If the Weyl tensor is zero, the crumbs do not drift at all.” · entry · `zero-weyl-means-no-drift`

- **Why it is tempting:** The Weyl tensor is introduced as what makes the ball drift into an egg.
- **What is true:** The Weyl tensor holds only the shape-changing part. Matter at the spot still shrinks or grows the ball, and in the dust universe it shrinks.
- **Exposed by:** `checks/crumbs-in-a-dust-universe`

### “A spherically symmetric static spacetime like Schwarzschild is conformally flat.” · working · `symmetry-makes-conformally-flat`

- **Why it is tempting:** Isotropy kills the Weyl tensor in cosmology, and Schwarzschild is also symmetric about a centre.
- **What is true:** Isotropy about every point kills the Weyl tensor; symmetry about one centre does not. Schwarzschild's Weyl tensor is its whole Riemann tensor, which is not zero.
- **Exposed by:** `checks/schwarzschild-symmetric-claim`

### “A vanishing Weyl tensor means conformally flat in every dimension.” · formal · `criterion-in-every-dimension`

- **Why it is tempting:** The theorem is often quoted without its dimension hypothesis.
- **What is true:** In three dimensions the Weyl tensor vanishes for every metric, so it decides nothing; the Cotton tensor decides, and generic three-metrics fail.
- **Exposed by:** `checks/where-three-dimensions-fail`

### “If a spacelike slice of a spacetime is conformally flat, so is the spacetime.” · formal · `conformally-flat-slice-means-spacetime`

- **Why it is tempting:** Conformally flat initial data are standard in numerical relativity.
- **What is true:** A slice's conformal flatness concerns its own three-metric. Schwarzschild's slices are conformally flat while its Weyl tensor never vanishes.
- **Exposed by:** `checks/slice-versus-spacetime`

### “A conformally flat spacetime has the global causal structure of Minkowski space, so it has no horizons.” · research · `conformally-flat-means-minkowski-causality`

- **Why it is tempting:** Conformal rescaling preserves light cones, which seem to be all that causal structure is.
- **What is true:** The criterion is local, and the map may cover only part of Minkowski space. De Sitter is conformally flat and has cosmological horizons.
- **Exposed by:** `checks/no-horizons-in-de-sitter`

## Checks

1. **Entry · predict** `checks/africa-or-greenland`. You stand in front of a wall map of the world, the flat map with straight lines of latitude and longitude. Greenland and Africa look about the same size on it. Which is really bigger, and by about how much? And will a small round lake in Greenland look round on this map, or squashed?
   - **Hints:** What does the map do to angles at a road crossing?
   - **Answer:** Africa is bigger, about fourteen times. The map gets every angle right, so it can be wrong only about sizes. And it is. On the globe the lines of longitude come together at the poles, but the map draws them side by side all the way to its top and bottom edges. So near the poles the map stretches the ground across, and to keep angles it stretches the ground by the same amount from bottom to top. Its scale therefore grows toward the poles. In the middle of Greenland each kilometre is drawn about three times longer than at the equator. So Greenland's area is drawn about ten times too big and looks like Africa. The lake is small, so across it the scale hardly changes. Every angle is right, so its round shape stays round.
   - **Must contain:** Africa is about fourteen times bigger; The map keeps angles and small shapes and is wrong only about the scale; The scale grows toward the poles, so the lake stays round but Greenland swells
   - **Numeric:** how many times bigger Africa really is = 14 1 (magnitude, ±4)
   - **Targets:** `map-has-one-wrong-scale`
   - **Visual:** [[angle-true-map-of-a-globe]]
2. **Entry · predict** `checks/crumbs-in-a-dust-universe`. Picture a universe filled evenly with dust in every direction, and a cabin falling freely, at rest among the dust. Inside, someone lets go a small ball of crumbs, all at rest. Over the next minutes the crumbs drift, measured against the centre crumb with a ruler fixed to the cabin. Predict: does the ball keep its size? Does it keep its round shape? And does this spacetime have a scale-only map?
   - **Hints:** If the ball lengthened, along which direction would it have to lengthen?
   - **Answer:** The ball does not keep its size. The dust pulls the crumbs together, so the ball slowly shrinks. It keeps its round shape. From a cabin at rest among the dust every direction looks the same, so there is no direction for the ball to lengthen along. A shape change with no direction is impossible. So the shape-changing part of the drift, the Weyl tensor, is zero. That holds at every place in the dust universe. So the spacetime has a scale-only map: a flat spacetime drawn at a scale that changes with time.
   - **Must contain:** The ball shrinks; It stays round because no direction is singled out; The Weyl tensor is zero everywhere, so a scale-only map exists
   - **Targets:** `zero-weyl-means-no-drift`
   - **Visual:** [[falling-ring-of-crumbs]]
3. **Entry · evaluate-claim** `checks/scale-only-map-means-flat`. Evaluate the claim: 'The expanding dust universe has a scale-only map, so it is really a flat spacetime, and there is no gravity in it.'
   - **Hints:** What does the ball of crumbs do in flat spacetime, and what does it do in the dust universe?
   - **Answer:** False. A scale-only map keeps angles and small shapes, but its scale changes from place to place, here from moment to moment. In a flat spacetime a ball of crumbs let go at rest keeps its size for ever. In the dust universe the ball shrinks, and that shrinking is gravity, set by the dust at the spot. So the universe is curved. The map says only that its curving has no shape-changing part.
   - **Must contain:** False: the scale changes, and that change is curving; The ball shrinks in the dust universe, never in flat spacetime; The map says only that the shape-changing part is zero
   - **Targets:** `conformally-flat-means-flat`
4. **Working · evaluate-claim** `checks/schwarzschild-symmetric-claim`. Evaluate the claim: 'Schwarzschild spacetime is spherically symmetric and static, so its light cones are those of flat spacetime at a varying scale: it is conformally flat.'
   - **Hints:** What is the Ricci tensor of a vacuum solution, and what does that leave of the Riemann tensor?
   - **Answer:** False. Schwarzschild is a vacuum solution, so $R_{\mu\nu} = 0$ and its Weyl tensor equals its full Riemann tensor, whose invariant $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 48G^2M^2/c^4r^6$ is not zero. A freely falling ball of crumbs beside the mass becomes an egg, the shape change the Weyl tensor records. Symmetry about one centre does not help; isotropy about every point is what kills the Weyl tensor in cosmology. Only the $(t, r)$ plane and the constant-time slices are conformally flat, not the spacetime.
   - **Must contain:** False: in vacuum the Weyl tensor is the Riemann tensor, which is nonzero; The Kretschmann invariant is 48 G squared M squared over c to the fourth r to the sixth; Symmetry about one centre is not isotropy about every point
   - **Targets:** `symmetry-makes-conformally-flat`
   - **Visual:** [[falling-ring-of-crumbs]]
5. **Formal · explain** `checks/where-three-dimensions-fail`. Which step of the sufficiency proof breaks down in three dimensions, and what replaces the Weyl tensor as the criterion? Give a count showing that conformal flatness is not automatic there, and name one three-metric that fails.
   - **Hints:** Where does the proof get the Cotton tensor from the Weyl tensor?
   - **Answer:** The proof needs the Cotton tensor to vanish and gets it from $\nabla^dC_{dabc} = (n-3)\,\mathcal C_{abc}$. In three dimensions the factor $n - 3$ is zero and $C \equiv 0$ anyway, so the identity says nothing. The Cotton tensor must vanish on its own, and that is the three-dimensional criterion. Count: a three-metric has $6$ components, coordinate freedom removes $3$ and a conformal factor $1$, leaving $2$ free functions per point that a conformally flat metric cannot carry; in two dimensions $3 - 2 - 1 = 0$. The Nil metric $dx^2 + dy^2 + (dz - x\,dy)^2$ has a nonzero Cotton tensor and is a concrete failure.
   - **Must contain:** The divergence identity carries the factor n minus 3 and is empty in three dimensions; The Cotton tensor is the criterion for n = 3; 6 minus 3 minus 1 leaves 2 free functions; the Nil metric fails
   - **Numeric:** free functions per point in a three-dimensional conformal class = 2 1 (magnitude, ±0)
   - **Targets:** `criterion-in-every-dimension`
6. **Formal · explain** `checks/slice-versus-spacetime`. Set $G = c = 1$. The slice $t = \mathrm{const}$ of Schwarzschild has three-metric $dr^2/(1 - 2M/r) + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$. Show that it is conformally flat, and explain why this does not contradict the spacetime's nonzero Weyl tensor.
   - **Hints:** Try $r = \rho(1 + M/2\rho)^2$ and compute $r - 2M$ first.
   - **Answer:** Substitute $r = \rho(1 + M/2\rho)^2$. Then $dr/d\rho = (1 - M/2\rho)(1 + M/2\rho)$ and $r - 2M = \rho(1 - M/2\rho)^2$, so $dr^2/(1 - 2M/r) = (1 + M/2\rho)^4d\rho^2$, while $r^2 = \rho^2(1 + M/2\rho)^4$. The slice metric is $(1 + M/2\rho)^4$ times flat space in spherical coordinates: conformally flat, with vanishing Cotton tensor. The spacetime's Weyl tensor is a different object, built from the four-dimensional metric, whose time-time coefficient $-(1 - M/2\rho)^2/(1 + M/2\rho)^2$ does not share the factor $(1 + M/2\rho)^4$; it is nonzero because the vacuum Riemann tensor is. Conformal flatness of a slice constrains only its intrinsic three-geometry.
   - **Must contain:** Isotropic coordinates display the slice as (1 + M over 2 rho) to the fourth times flat space; The four-metric's time coefficient breaks the common factor; A conformally flat slice says nothing about the spacetime's Weyl tensor
   - **Numeric:** conformal factor squared of the slice at rho equal to two M = 2.4414 1 (magnitude, ±0.001)
   - **Targets:** `conformally-flat-slice-means-spacetime`
7. **Research · evaluate-claim** `checks/no-horizons-in-de-sitter`. Evaluate the claim: 'De Sitter spacetime is conformally flat, so its causal structure is that of Minkowski space and it has no horizons.'
   - **Hints:** Write the flat slicing of de Sitter in conformal time; what is the range of $\eta$?
   - **Answer:** False. Conformal flatness is local. With $G = c = 1$ and Hubble rate $H$, the flat slicing of de Sitter is $ds^2 = (H\eta)^{-2}(-d\eta^2 + dx^2 + dy^2 + dz^2)$ with $\eta < 0$: conformal to the half of Minkowski space with $\eta < 0$, not to all of it. An observer at rest at the origin therefore receives, by $\eta \to 0$, only light emitted from comoving radius less than $-\eta_{\rm e}$ at emission time $\eta_{\rm e}$: a cosmological event horizon. A conformal map onto part of Minkowski space fixes the light cones inside the patch, not how the patch ends. Penrose diagrams record this: de Sitter's is a square, Minkowski's a half-diamond.
   - **Must contain:** False: the map covers only half of Minkowski space; The flat slicing ends at eta = 0, giving an event horizon at comoving radius minus eta; Local conformal flatness fixes light cones inside the patch, not global structure
   - **Targets:** `conformally-flat-means-minkowski-causality`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Symbol and sign of the Cotton tensor | This note writes $\mathcal C_{abc} = \nabla_bP_{ac} - \nabla_cP_{ab}$ with the Schouten tensor $P_{ab}$, so that $\nabla^dC_{dabc} = (n-3)\,\mathcal C_{abc}$; the course conventions do not yet fix a symbol for it. | Some texts use the opposite sign, some build it from the Ricci tensor so that a factor $n - 2$ appears, many use the same letter $C$ as for the Weyl tensor, and in three dimensions the dual Cotton–York tensor $Y^{ab}$ often replaces it. |
| Power of the conformal factor | $\tilde g_{\mu\nu} = \Omega^2 g_{\mu\nu}$ with $\Omega > 0$, and $\sigma = \ln\Omega$ in the flattening equation. | Some texts write $\tilde g = \Omega\,g$, $\tilde g = e^{2\sigma}g$ with another letter, or $\tilde g = \Omega^{-2}g$ when the factor vanishes at infinity; in initial data the spatial factor is $\psi^4$. |

## Visuals

- ★ [[angle-true-map-of-a-globe]] (flagship): The entry experience: a globe beside its Mercator map, with a small circle that stays a circle wherever it is dragged and a readout of how many times too large it is drawn. *Sketch:* A globe and its Mercator map side by side, linked. Dragging a small circle on the globe shows its image on the map, always a circle, with a readout of the scale factor at that latitude. A Greenland/Africa toggle compares true areas with map areas. A stereographic mode swaps the map. Design rule: the circle never squashes, against the belief that the map is simply wrong at one scale.
- [[falling-ring-of-crumbs]] (core): The ball of crumbs beside a planet and in a dust universe, with a lamp that says whether a scale-only map exists. *Sketch:* This concept adds a spacetime chooser: empty space beside a planet, and an evenly filled dust universe with the cabin at rest among the dust. Beside the readout of the shape-changing part, a lamp labelled 'scale-only map?' lights only when that readout stays zero for every cabin direction the chooser offers.
- [[expanding-universe-on-a-flat-map]] (supporting): The dust universe drawn in cosmic time and in conformal time, where light rays become 45-degree lines and the scale factor is the map's scale. *Sketch:* A dust universe drawn twice: in cosmic time, where light rays curve, and in conformal time, where they are 45-degree lines and a readout of $a(\eta)$ grows up the vertical axis. A slider moves the present moment and shows the map distance light has covered, three times c times the age for dust.

## Tutor moves

**Open with**

- Picture the wall map of the world in a classroom, the one with straight lines for latitude and longitude. On it Greenland looks about as big as Africa. Which do you think is really bigger, and by about how much? *(prediction)*

**If the learner is stuck**

- *The learner says the map is simply wrong and cannot say what it gets right.* → Ask whether a small round lake and a right-angled road crossing are drawn round and right-angled. Then contrast a big region, across which the scale changes. *Uses:* `ways_in/greenland-on-the-wall-map`, `checks/africa-or-greenland`
- *The learner thinks a shrinking ball proves the dust universe has no scale-only map.* → Separate size from shape: ask which of the two the Weyl tensor holds, then replay the every-direction-looks-the-same argument. *Uses:* `ways_in/crumbs-decide-the-map`, `checks/crumbs-in-a-dust-universe`

**Common questions**

- *Every surface has a scale-only map. Why not every spacetime?* (entry) On a surface, once the angles are right, the only thing left for a map to get wrong is the scale. One scale at each spot turns out to be enough to draw any small patch. Spacetime has more to get wrong. A ball of crumbs can be stretched one way and squeezed another, while a scale, one number at each spot, can only make the whole ball bigger or smaller. So no scale undoes a stretched ball, and there is no map. *Uses:* `ways_in/crumbs-decide-the-map`, `checks/where-three-dimensions-fail`
- *The expanding universe has a scale-only map. So is space flat after all?* (entry) Not because of the map. The map says the light paths are those of flat spacetime drawn at a scale that changes with time, and from place to place as well when space is curved. It says nothing about whether space at one moment is flat, curved like a ball, or curved like a saddle: all three kinds of expanding universe have such a map. Whether space is flat is a separate measurement, made with a distant ruler. *Uses:* `ways_in/which-spacetimes-pass`, `checks/scale-only-map-means-flat`

**Switching levels**

- To working when: asks how the scale is computed; uses coordinates or the metric. Bring in the Mercator metric and the curvature-from-scale formula, then conformal time. *Uses:* `ways_in/curvature-hidden-in-the-scale`, `worked_examples/mercator-sphere`, `ways_in/which-spacetimes-pass`
- To formal when: asks why the Weyl tensor is enough; asks about three dimensions or the Cotton tensor. State the theorem with its dimensions and walk the Frobenius argument, then the edges. *Uses:* `ways_in/flatten-the-schouten-tensor`, `ways_in/where-the-criterion-stops`
- To research when: asks about Penrose diagrams, initial data or the Weyl curvature hypothesis. Move to the research way and test local against global on de Sitter. *Uses:* `ways_in/conformal-flatness-in-research`, `checks/no-horizons-in-de-sitter`

**Pronunciations:** Weyl → VILE; Schouten → SKHOW-ten; Mercator → mer-KAY-tor; Frobenius → fro-BAY-nee-us; Kuiper → KY-per

**Voice notes:** At entry say 'scale-only map' every time and hold 'conformal' until the working rung. When the learner says the map is wrong, ask 'wrong about what?'.

## History

- **Gerardus Mercator (1569).** Published the angle-true world map on which courses of constant compass bearing are straight lines: a scale-only map of the globe whose scale grows toward the poles.
- **Carl Friedrich Gauss (1825).** Prize essay of 1822 proving that every real-analytic surface can be mapped onto the plane with small shapes preserved: the two-dimensional case of conformal flatness. Carl Friedrich Gauss (1825), *Allgemeine Auflösung der Aufgabe: die Theile einer gegebnen Fläche auf einer andern gegebnen Fläche so abzubilden, dass die Abbildung dem Abgebildeten in den kleinsten Theilen ähnlich wird*, Astronomische Abhandlungen 3, 1–30
- **Émile Cotton (1899).** Found the tensor that decides conformal flatness in three dimensions. Émile Cotton (1899), *Sur les variétés à trois dimensions*, Annales de la Faculté des sciences de Toulouse, 2e série, 1, 385–438, doi:10.5802/afst.160
- **Hermann Weyl (1921).** Having introduced the conformally invariant curvature tensor in 1918, showed that its vanishing characterizes conformally flat metrics in four or more dimensions. Hermann Weyl (1921), *Zur Infinitesimalgeometrie: Einordnung der projektiven und der konformen Auffassung*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-Physikalische Klasse 1921, 99–112
- **Jan Arnoldus Schouten (1921).** Gave the theorem its full form in every dimension, with the Cotton tensor deciding the three-dimensional case. Jan Arnoldus Schouten (1921), *Über die konforme Abbildung n-dimensionaler Mannigfaltigkeiten mit quadratischer Maßbestimmung auf eine Mannigfaltigkeit mit euklidischer Maßbestimmung*, Mathematische Zeitschrift 11, 58–88, doi:10.1007/BF01203193

## Research horizon

- **Conformal infinity and the smoothness of the conformal boundary.** Penrose's compactification rescales the metric by a factor vanishing at infinity; for conformally flat cosmologies the rescaled metric is flat throughout, so their Penrose diagrams are cut-outs of the Einstein static universe. For radiating spacetimes the smoothness of the rescaled metric at null infinity is still studied. Jörg Frauendiener (2004), *Conformal Infinity*, Living Reviews in Relativity 7, 1, doi:10.12942/lrr-2004-1
- **Weyl curvature hypothesis.** Penrose's proposal that the initial singularity had vanishing Weyl curvature makes the early universe conformally flat and assigns it low gravitational entropy, in contrast with the divergent Weyl curvature of black hole singularities. Roger Penrose (1979), *Singularities and time-asymmetry*, In S. W. Hawking and W. Israel (eds), General Relativity: An Einstein Centenary Survey, Cambridge University Press, 581–638
- **Conformally flat initial data and junk radiation.** Bowen–York and puncture data take the spatial metric conformally flat; since Kerr admits no conformally flat slices with its asymptotics, such data for spinning black holes carry spurious radiation, and conformally curved data are used to reduce it. Jeffrey M. Bowen, James W. York (1980), *Time-asymmetric initial data for black holes and black-hole collisions*, Physical Review D 21, 2047–2056, doi:10.1103/PhysRevD.21.2047; Alcides Garat, Richard H. Price (2000), *Nonexistence of conformally flat slices of the Kerr spacetime*, Physical Review D 61, 124011, doi:10.1103/PhysRevD.61.124011; Gregory B. Cook (2000), *Initial Data for Numerical Relativity*, Living Reviews in Relativity 3, 5, doi:10.12942/lrr-2000-5
- **Cotton, Bach and obstruction tensors.** The Cotton tensor in three dimensions and the Bach tensor in four are the conformally natural tensors built from derivatives of the Schouten tensor; the Fefferman–Graham ambient metric produces their analogue, the obstruction tensor, in every even dimension. Rudolf Bach (1921), *Zur Weylschen Relativitätstheorie und der Weylschen Erweiterung des Krümmungstensorbegriffs*, Mathematische Zeitschrift 9, 110–135, doi:10.1007/BF01378338; Charles Fefferman, C. Robin Graham (2012), *The Ambient Metric*, Annals of Mathematics Studies 178, Princeton University Press, arXiv:0710.0919

## Review: novice

**Verdict:** fixed (2026-09-16, revision 3)

**Retell attempt:** There's a wall map where Greenland looks as big as Africa even though Africa is really 14 times bigger. The map gets angles right and is only wrong about the scale, which is different in different places; that's a scale-only map. Every smooth surface has one for small patches, but I don't know why. A spacetime can have one too, but only if the Weyl tensor is zero, and that is the table of the shape-changing part of the crumbs' drift. Next to a planet the crumbs make an egg so there's no map; in a universe full of dust the ball stays round but shrinks, so there is a map and the universe is a flat spacetime drawn at a changing scale. Things I didn't get: 'in four dimensions' (isn't spacetime always four?), 'the map is not free' (free of what?), 'no matter at the spot sets' (no matter what?), why the scale has to change, and if the ball shrinks how it can be flat.

**Stumbles (18)**

- “In four dimensions a spacetime has one exactly when its Weyl tensor is zero everywhere.”: A beginner has just learned that spacetime has four directions, so 'in four dimensions' reads as if other spacetimes existed; and 'everywhere' names no region.
- “the shape-changing drift that no matter at the spot sets”: 'no matter' reads as the idiom 'no matter what'; the sentence needed two readings. Same phrase in the Weyl tensor glossary entry.
- “drawn at a place-dependent scale”: Second wording for one idea; the ways say 'changes from place to place'.
- “Look at a wall map of the world.”: Classroom wall maps come in several shapes; only the check names the one with straight lines, so a reader could pick a map that does squash the lake.
- “In the middle of Greenland, each kilometre is drawn about three times longer than a kilometre at the equator.”: The objective asks why the scale must change, but the way never says; the first what-if is 'why not print one correct scale?'.
- “Every smooth surface, however it curves, has a scale-only map of each small patch.”: 'smooth' is undefined, and a universal claim arrives with no reason or trust marker.
- “In four dimensions the map is not free.”: 'not free' is ambiguous (free of charge?) and had to be reread.
- “That shape change is the Weyl tensor.”: The glossary says the Weyl tensor is the table that holds the change, so 'is' clashes with it, and the step to 'not zero' is implicit.
- “The ball slowly shrinks, but it stays round, and the Weyl tensor is zero.”: The shrinking has no cause, and 'and the Weyl tensor is zero' hides the step from 'stays round' to 'zero'.
- “So this universe is a flat spacetime drawn at a scale that changes with time.”: The ball has just shrunk, so 'flat spacetime' is a surprise with no backing within two sentences.
- “A cabin rushing through the dust finds the ball stretched along its motion, by the dust itself and not by the Weyl tensor.”: 'stretched' sounds like growing, but the ball shrinks in every direction, only less along the motion.
- “The scale-only map of 'Greenland on the wall map' has a spacetime version: a curved spacetime drawn as a flat one at a changing scale.”: After the fix the sentence ran to 35 words; and 'changing scale' does not say the scale also changes in time.
- “In a flat spacetime, balls let go at rest keep their distances for ever.”: 'balls' is a second word for the single ball of crumbs used everywhere else.
- “its scale grows toward the poles, because it stretches the lines of longitude apart to keep them side by side”: The lines are not stretched apart: on the globe they come together and the map keeps them side by side; the step from that to a growing scale was implicit.
- “No single scale can flatten a round world without breaking angles.”: Suggests one scale could flatten a round world if angles were given up; no flat drawing at one scale exists at all.
- “One scale at each spot turns out to be enough to fix any small patch.”: 'fix' has two senses, repair and settle.
- “Two high tides a day at most coasts, raised by the Moon and the Sun.”: The entry observation carried no everyday number.
- “its shape matches the shape on a globe, only drawn bigger”: The try-it needs a globe and names none a teenager has to hand.

**Fixes**

- Summary and tagline: replaced 'in four dimensions' with 'with its four directions', added 'in the region', removed the 'no matter at the spot sets' phrase and 'place-dependent', and split the last sentence so the average stays at or below 20 words.
- Way greenland-on-the-wall-map: named the straight-line map, added the orange-peel paragraph answering why the scale must change, defined 'smooth' in its own sentence with a trust tag for the 1820s theorem, and gave the try-it a globe or map app. To stay within the 10% review allowance (entry cap 400), dropped the longitude-stretching mechanism from the way; it lives in the check africa-or-greenland's answer.
- Way crumbs-decide-the-map: split the opener, replaced 'the map is not free', made the Weyl tensor hold rather than be the shape change, gave the shrinking its cause, made the step to 'Weyl tensor is zero' explicit, backed 'flat spacetime' with 'the universe itself is not flat', and rewrote simplifies so the moving cabin's ball shrinks faster across its motion than along it instead of being 'stretched'.
- Glossary: added 'smooth'; spacetime entry now uses the single ball of crumbs; Weyl tensor entry avoids the 'no matter' idiom.
- Check africa-or-greenland: replaced the longitude sentence with the globe/map contrast and the across-then-bottom-to-top stretching chain.
- Misconception map-has-one-wrong-scale: correction now says a round world cannot be drawn flat at one scale at all, with the orange peel.
- Observation two-high-tides: added everyday numbers. Common question why-not-every-spacetime: 'fix' became 'draw'.
- Ladder: added the prerequisite index-notation at working, because both working ways write indexed tensors; the registry needs a sync.

**Concerns**

- Entry explanations now total about 437 words, above the advanced cap of 400 and inside the 10% review allowance; the physics reviewer has no room to add entry text without dropping something.
- Physics reviewer: please confirm the rewritten simplifies of crumbs-decide-the-map. My check from the Ricci decomposition with vanishing Weyl tensor gives, for dust of density rho and a cabin moving at Lorentz factor gamma, tidal coefficients 4 pi G rho / 3 along the motion and 4 pi G rho (gamma squared minus two thirds) across it, so the ball shrinks in every direction and faster across the motion.
- The glossary calls the usual classroom wall map the Mercator map; many classroom maps are not, which is why the way now names the map with straight lines of latitude and longitude.
- The entry common question why-not-every-spacetime cites the formal check where-three-dimensions-fail in its uses; harmless for the tutor but odd.
- Prerequisites conformally-flat-metric and conformal-time still have no notes, so the working rung's assumes cannot be checked against digests.
- The three visuals remain proposals; the flagship angle-true-map-of-a-globe should name the straight-line map and let the learner toggle Greenland against Africa, as the sketch says.

**Re-read** (2026-09-16, revision 3): 0 stumbles in 4 changed passages


## Review: physics

**Verdict:** fixed (2026-09-16, revision 3)

**Verification**

- Ricci decomposition $R = C + P \owedge g$ with $P_{ab} = \frac{1}{n-2}(R_{ab} - \frac{R}{2(n-1)}g_{ab})$ and the stated Kulkarni–Nomizu product: Hand trace: $g^{ac}(P \owedge g)_{abcd} = (n-2)P_{bd} + P g_{bd}$ with $P = R/(2(n-1))$, which equals $R_{bd}$ with the course $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$; $h \mapsto h \owedge g$ injective for $n \ge 3$ since its trace forces $\mathrm{tr}\,h = 0$ then $h = 0$ → Correct, including the three-dimensional count 6 = 6 that makes it onto
- Derivation 'Gaussian curvature from the scale': Christoffel symbols, $R^x{}_{yxy}$ and $K = -e^{-2\sigma}\Delta\sigma$ in course conventions: Re-derived every symbol from the course Christoffel formula and the course Riemann sign; product terms cancel; sign checked against the sphere; numeric central-difference Riemann tensor for the Mercator, stereographic and $e^{\alpha x}$ scales → Correct: $K = 0.25000$ for $a = 2$ in both maps, $K = 0$ for $e^{\alpha x}$, Ricci scalar $2/a^2$ as the conventions require
- Mercator map $x = a\phi$, $y = a\,\mathrm{artanh}\cos\theta$, scale $\Omega = \sin\theta$; latitude 72 gives $\Omega = 0.31$, lengths 3.2 times, areas 10.5 times; Africa/Greenland ratio 14: python3: $\sin 18^\circ = 0.3090$, $1/\Omega = 3.236$, $\sec^2 72^\circ = 10.47$; $30.37/2.166 = 14.0$ million square kilometres → All entry and working numbers correct; numeric tolerances (14 ± 4, 10 ± 2) contain the true values
- Stereographic problem: $\Omega = 2$ at the south pole, Laplacian of $\ln(a^2 + r^2)$ equals $4a^2/(a^2 + r^2)^2$, $K = 1/a^2$, Earth $2.46\times10^{-14}\,\mathrm{m^{-2}}$: Hand algebra of $f'' + f'/r$; python3 $1/(6.371\times10^6)^2 = 2.4637\times10^{-14}$; numeric Riemann check of the map metric → Correct; numeric answer within the 2% tolerance
- Dust universe: $\eta = 3t_0^{2/3}t^{1/3}$, $\eta_0 = 3t_0$, $a = (\eta/\eta_0)^2$, horizon map distance $3ct_0 = 41$ billion light-years for $t_0 = 13.8$ billion years: Integration by hand, python3 for the numbers; noted that a pure dust universe with $H_0 = 70$ has $t_0 = 9.3$ billion years, which the example flags with 'taken for illustration' → Correct
- Entry and simplifies claim: a cabin at rest among dust sees the ball shrink and stay round; a cabin moving at Lorentz factor $\gamma$ sees tidal coefficients $4\pi G\rho/3$ along its motion and $4\pi G\rho(\gamma^2 - 2/3)$ across, so the ball shrinks in every direction and faster across the motion: python3: built $R_{abcd} = (P \owedge g)_{abcd}$ from the dust Ricci tensor with $C = 0$, formed $E_{ab} = R_{acbd}u^cu^d$ for $v = 0, 0.6, 0.9$ and projected on the along and across directions; course deviation equation gives acceleration $-E\xi$ → Confirmed exactly: 0.3333 along for every $v$, and 0.8958, 4.5965 across for $v = 0.6, 0.9$, matching $\gamma^2 - 2/3$; trace equals $R_{ab}u^au^b = 4\pi G\rho(2\gamma^2 - 1)$
- Schouten transformation law and the flattening equation; Ricci identity sign for a covector; integrability computation (derivation 'Integrability of the flattening equation'): Re-expanded steps 2 to 5 by hand: cubic and $W^2$ terms cancel on antisymmetrization, linear terms equal $-R_{dacb}W^d$ with $R = P \owedge g$, leaving $\nabla_cP_{ab} - \nabla_bP_{ac}$; covector Ricci identity $[\nabla_c, \nabla_b]W_a = -R^d{}_{acb}W_d$ follows from the course vector identity → Correct; the surviving condition is minus the note's Cotton tensor, so 'Cotton tensor vanishes' is the right conclusion
- Derivation 'Divergence of the Weyl tensor': $\nabla^aC_{abcd} = (n-3)(\nabla_cP_{bd} - \nabla_dP_{bc})$: Re-derived from the second Bianchi identity with course index placements: $R^a{}_{bac} = R_{bc}$, $R^a{}_{bda} = -R_{bd}$, $\nabla^aR_{ab} = \frac12\nabla_bR$, $\nabla^aP_{ab} = \nabla_bP$; trace terms cancel between steps 3 and 4 → Correct, and consistent with the key equation after renaming indices
- Freedom count $n + 1 + n(n+1)/2 = (n+1)(n+2)/2$; algebraic curvature tensors in three dimensions number $n^2(n^2-1)/12 = 6$: Hand arithmetic → Correct
- Lorentzian surfaces: $-e^{2\sigma}du\,dv = e^{2\sigma}(-dt^2 + dx^2)$ with $t = (u+v)/2$, $x = (v-u)/2$: Hand expansion: $dt^2 - dx^2 = du\,dv$ → Correct
- Schwarzschild slice in isotropic radius: $dr/d\rho = (1 - M/2\rho)(1 + M/2\rho)$, $r - 2M = \rho(1 - M/2\rho)^2$, factor $(1 + M/2\rho)^4$, value 2.4414 at $\rho = 2M$; Cotton tensor of the slice vanishes; time coefficient $-(1 - M/2\rho)^2/(1 + M/2\rho)^2$: Hand algebra; python3 $(1.25)^4 = 2.44140625$; numeric Cotton tensor of the slice metric at $r = 5M$ is $7\times10^{-7}$ (finite-difference noise) and its Ricci scalar $10^{-8}$ → Correct
- Schwarzschild fails: Kretschmann scalar $48G^2M^2/c^4r^6$, Ricci zero; Weyl components of size $M/r^3$: Numeric Riemann tensor at $r = 5M$: $R_{abcd}R^{abcd} = 0.0030720$ against $48/5^6 = 0.003072$, Ricci at the $10^{-7}$ level; SI factors checked dimensionally ($GM/c^2$ a length) → Correct
- Closed FLRW problem: bracket equals $(\cos\eta + \cos\chi)^2$ times Minkowski, factor 4 at the origin, domain $|\eta| + \chi < \pi$: Hand algebra of the solution steps; python3 finite-difference Jacobian of $(\eta, \chi) \mapsto (t, r)$ at three points confirms $F^2(-dt^2 + dr^2) = -d\eta^2 + d\chi^2$ and $\sin\chi = F r$ with $F = \cos\eta + \cos\chi$; numeric Weyl tensor of a closed FLRW metric with $a = 1 + 0.3\sin\eta$ is $10^{-6}$ → Solution and answer correct; the problem statement and its spoken form asked for the factor with exponent $-2$, contradicting the answer and the numeric value 4: fixed to exponent $+2$
- Conformally flat Einstein space: $P_{ab} = \frac{\Lambda}{2(n-1)}g_{ab}$, $K = \Lambda/(n-1)$, $\Lambda/3$ in four dimensions; vacuum gives $R_{abcd} = 0$: Hand algebra with the course sectional curvature; numeric de Sitter check in the flat slicing $(H\eta)^{-2}\eta_{\mu\nu}$: $R = 12H^2$, Weyl exactly zero, sectional curvature of the $(t, x)$ plane $H^2 = \Lambda/3$ → Correct, including the sign for a timelike plane under the course convention
- Three dimensions: Nil metric $dx^2 + dy^2 + (dz - x\,dy)^2$ is not conformally flat; the count $6 - 3 - 1 = 2$: Numeric Cotton tensor of the Nil metric: largest component 1.00 with Ricci scalar $-1/2$, while its Weyl tensor is $10^{-13}$; count by hand → Correct
- De Sitter flat slicing $\eta < 0$, horizon at comoving radius $-\eta_{\rm e}$, Penrose diagram shapes: $\eta = -1/(aH)$ for $a = e^{Ht}$; radial null line covers comoving distance $-\eta_{\rm e}$ by $\eta = 0$ → Correct
- Entry tides observation: interval about twelve and a half hours, rise of a metre or more: Lunar semidiurnal period 12 h 25 min; typical open-coast ranges 1 to 3 m, but enclosed seas have far less → Interval correct; the rise was scoped to 'at many coasts'
- Cosmic shear observation: root-mean-square shear of order $10^{-2}$ on arcminute scales; Weyl curvature shears light bundles, Ricci curvature focuses them: WebSearch: Bacon, Refregier and Ellis 2000 report an rms shear of 1.6 percent on 8 arcminute cells; Sachs optical equations → Correct
- History: Gauss 1822 prize essay (real-analytic surfaces), Cotton 1899, Weyl 1918 tensor and 1921 theorem, Schouten 1921, Mercator 1569: WebSearch for each work; scope of Gauss's result checked (real-analytic case; smooth case is later analysis, as the formal way says) → Confirmed; the entry sentence 'a theorem from the 1820s' was scoped to 'first proved in the 1820s' because the smooth case dates from the 1910s
- References: Bacon–Refregier–Ellis 2000 (MNRAS 318, 625), Gauss 1825 (Astronomische Abhandlungen 3, 1–30), Cotton 1899 (AFST 2e s. 1, 385–438), Weyl 1921 (Nachr. Göttingen 1921, 99–112), Schouten 1921 (Math. Z. 11, 58–88), Frauendiener 2004 (LRR 7, 1), Penrose 1979 (Einstein Centenary Survey, 581–638), Bowen–York 1980 (PRD 21, 2047), Garat–Price 2000 (PRD 61, 124011), Cook 2000 (LRR 3, 5), Bach 1921 (Math. Z. 9, 110–135), Fefferman–Graham 2012 (AMS 178, arXiv 0710.0919): One WebSearch each; publisher, EUDML, ADS, arXiv and NUMDAM listings → All twelve confirmed and marked verified; DOIs added for Cotton (10.5802/afst.160), Schouten (10.1007/BF01203193) and Bach (10.1007/BF01378338)
- Structure: prerequisites direct and acyclic, assumes within prerequisites, two formal checks and two formal problems, visual ids: Digests of weyl-tensor, flatness-criterion and bianchi-identity (none lists this note); grep of registries for every linked id; visual_ids.py → Sound. All leads_to and related ids exist in registries; conformally-flat-metric, conformal-time and index-notation have registry entries but no notes yet; the three visuals are proposals with sketches, falling-ring-of-crumbs shared with 22 other notes

**Counterexamples tried**

- Three dimensions: the Weyl tensor vanishes for every metric, yet the Nil metric has Cotton tensor of order one; the note scopes the criterion to n at least four and gives this example.
- Two dimensions: every metric is locally conformally flat, Riemannian or Lorentzian; the note states this and gives the null-coordinate construction.
- Round sphere: locally conformally flat but not globally conformal to a region of the plane; covered under 'Local versus global'.
- Schwarzschild: spherically symmetric, static, with conformally flat slices and a conformally flat (t, r) plane, yet not conformally flat; covered by the working check and the formal slice check.
- De Sitter: conformally flat, curved, and with horizons; covered at working, formal and research rungs.
- Moving observer in a dust universe: the ball becomes an egg although the Weyl tensor is zero; the simplifies scopes the entry sentence and the tidal coefficients were recomputed.
- Weyl tensor zero at one event or on one hypersurface only: no conformally flat neighbourhood follows; covered under 'Points versus regions'.
- Non-Mercator wall maps (plate carrée, Gall–Peters) have straight latitude and longitude lines but squash small shapes; the glossary now pins the map by Greenland looking as big as Africa.

**Fixes**

- Problem closed-universe-on-a-flat-map: the statement and its spoken form asked for the factor (cos eta + cos chi) to the power minus two; the solution, answer and numeric value 4 give the power plus two. Statement corrected to plus two.
- Way greenland-on-the-wall-map: 'a theorem from the 1820s' became 'a theorem, first proved in the 1820s', since Gauss proved the real-analytic case and the smooth case came in the 1910s.
- Glossary wall-map: added 'on which Greenland looks as big as Africa', because straight latitude and longitude lines alone also describe maps that squash shapes.
- Observation two-high-tides: the metre-or-more rise now holds 'at many coasts' rather than at most coasts.
- Common question is-space-flat-then: the map's scale changes with time 'and from place to place as well when space is curved', since the closed and open models have Omega depending on position.
- Way where-the-criterion-stops: 'de Sitter and anti-de Sitter are the only curved cases' scoped to Lorentzian signature and to local equivalence.
- Research horizon conformally-flat-initial-data: Kerr admits no conformally flat slices 'with its asymptotics', matching the theorems cited.
- References: all twelve verified after one search each; three DOIs added.

**Concerns**

- Course conventions do not fix a symbol or sign for the Cotton tensor, the Schouten tensor or the Kulkarni–Nomizu product, nor the exponent of the conformal factor; the note's choices ($\mathcal C_{abc} = \nabla_bP_{ac} - \nabla_cP_{ab}$, $P_{ab}$, $\owedge$, $\tilde g = \Omega^2 g$) are self-consistent and recorded as notation traps, and should be added to course-conventions.md before other notes use them.
- Entry ways total 438 words against the advanced cap of 400, inside the 10% review allowance only because of recorded fixes; the next revision should shorten the Greenland way rather than add to it.
- The registry lists only weyl-tensor and conformally-flat-metric as prerequisites; the note adds conformal-time, index-notation, flatness-criterion and bianchi-identity, so sync_registry.py must run. Prerequisites conformally-flat-metric, conformal-time and index-notation have no notes yet.
- The summary sentence 'That tensor holds the shape-changing part of the drift of falling crumbs' is exact only in empty space or for a cabin at rest among dust; the crumbs way's recap and simplifies give that scope, and the summary is left simple.
- Valiente Kroon's sharpening of the Garat–Price result is named in the research way without a reference entry; add one if the research rung is expanded.

**Diff check** (2026-09-16, revision 3)

- Glossary wall-map: the flat world map with straight latitude and longitude lines on which Greenland looks as big as Africa is the Mercator map.: Checked the pin against the other straight-grid maps (plate carrée, Gall–Peters): only the conformal Mercator map stretches Greenland to Africa's apparent size, since its scale grows as the secant of latitude, about three at Greenland's middle. → Accurate; the extra clause singles out the Mercator map and agrees with the way's Greenland-to-Africa comparison.
- Observation two-high-tides: successive high tides about twelve and a half hours apart at most coasts; a rise of a metre or more between low and high tide at many coasts.: Semidiurnal lunar period is half the lunar day, 24 h 50 min / 2 = 12 h 25 min; open-ocean range is a few tenths of a metre to a metre and many coasts amplify it to a metre or more. → Accurate within its scope; splitting the sentence and scoping the rise to 'many coasts' keeps both claims true.
- Common question is-space-flat-then: a scale-only map of an expanding universe has a scale that changes with time, and from place to place as well when space is curved.: Hand check: with $r = \tan(\chi/2)$, $d\chi^2 + \sin^2\chi\,d\Omega^2 = (2/(1+r^2))^2 (dr^2 + r^2 d\Omega^2)$, so the closed model's conformal factor depends on position as well as conformal time; the flat model's factor is $a(\eta)$ alone. → Accurate; agrees with the note's problem closed-universe-on-a-flat-map, whose factor $(\cos\eta + \cos\chi)^{-2}$ depends on both.
- Way greenland-on-the-wall-map: the existence of a scale-only map of each small patch of a smooth surface is a theorem first proved in the 1820s.: Compared with the note's history: Gauss's 1822 prize essay proved the real-analytic case; the smooth case followed in the 1910s. 'First proved' credits the 1820s without claiming the full smooth statement was settled then. → Accurate at entry rung as scoped; no change.
