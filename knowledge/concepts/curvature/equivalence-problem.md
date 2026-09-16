---
type: "concept"
schema_version: 2
id: "equivalence-problem"
title: "Equivalence problem for metrics"
tagline: "Telling whether two different-looking distance rules describe the same surface"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["invariant classification of metrics", "invariant classification of exact solutions"]
prerequisites: ["riemann-curvature-tensor", "diffeomorphism", "gaussian-curvature", "kretschmann-scalar", "isometry", "orthonormal-frame"]
leads_to: ["cartan-karlhede-algorithm", "petrov-classification"]
visuals: ["two-grids-on-one-playground", "curvature-fingerprint-curves"]
---

# Equivalence problem for metrics

*Telling whether two different-looking distance rules describe the same surface*

`equivalence-problem` · curvature · advanced · physics-reviewed (revision 7)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[diffeomorphism]] (working) · [[gaussian-curvature]] (working) · [[kretschmann-scalar]] (working) · [[isometry]] (formal) · [[orthonormal-frame]] (formal)  
**Opens:** [[cartan-karlhede-algorithm]] · [[petrov-classification]]  
**Related:** [[flatness-criterion]] · [[hole-argument]] · [[space-of-constant-curvature]] · [[isotropic-coordinates]] · [[exact-solution]]  
**Visuals:** ★ [[two-grids-on-one-playground]] · [[curvature-fingerprint-curves]]

> Two friends can paint different grids on the same flat playground and write down distance rules that look nothing alike. Deciding whether two written distance rules describe the same surface, when you cannot go and look, is called the equivalence problem. A walker's measurements on a surface, like carrying an arrow around a loop without letting it swing, do not depend on the painted grid. So they can show that two rules describe different surfaces.

## You will be able to

**Entry**
- Explain why two distance rules that look different can describe the same surface. `objectives/explain-labels-versus-ground` ← `checks/same-ground-different-rules`, `problems/one-degree-steps`
- Use a measurement made on a surface, such as the arrow test, to show that two distance rules describe different surfaces. `objectives/use-ground-measurements` ← `checks/turned-arrow-settles-it`, `checks/egg-and-ball`

**Working**
- Write the equivalence of two metrics as equations for a coordinate change, and count equations against unknown functions. `objectives/set-up-the-equations` ← `checks/count-the-equations`
- Use curvature invariants and relations between them to rule out an equivalence or to identify corresponding points. `objectives/separate-metrics-with-invariants` ← `checks/same-curvature-values`, `problems/harmonic-radius-disguise`
- Construct an explicit coordinate change between two metrics of the same constant curvature. `objectives/construct-an-equivalence` ← `problems/two-hyperbolic-planes`

**Formal**
- State Cartan's local equivalence theorem with its hypotheses, and distinguish local from global equivalence. `objectives/state-cartan-theorem` ← `checks/torus-and-plane`, `problems/minding-by-geodesic-polar-coordinates`
- Explain why scalar polynomial invariants determine frame components up to rotation in Riemannian signature but can miss curvature in Lorentzian signature. `objectives/explain-lorentzian-failure` ← `checks/plane-wave-scalars`

**Research**
- Evaluate claims about which spacetimes are characterized locally by their scalar curvature invariants. `objectives/evaluate-scalar-characterization` ← `checks/kundt-claim`

## Ways in

### 1. Two grids on one playground · entry · picture

*How can two descriptions that look completely different describe the same surface?*

Two friends map the same flat playground. Ana paints a square grid of rows and columns, one metre apart. Ben paints rings around a flagpole, one ring every metre, and spokes out from the pole, one spoke every degree.

A spot is any place on a surface. Where two painted lines cross, the grid gives that spot a label: Ana's by row and column, Ben's by ring and spoke.

Each friend writes down how far apart neighbouring spots on their grid are. This is called a distance rule.

Ana's rule is the same everywhere: one step along a row or a column covers one metre. Ben's step along a spoke covers one metre, but his step along a ring does not. The ring 5 metres from the pole is about 31 metres long and is split into 360 steps, so each step covers about 9 centimetres. Rings farther out are longer, so their steps cover more.

So the two rules look nothing alike. Yet a tape laid between two spots on the playground gives one reading, whichever grid is painted. The difference lies in the painted grids, not the playground.

Deciding from two written distance rules alone whether they describe the same surface is called the equivalence problem.

**Try it:** Mark two dots about 3 centimetres apart on a sheet of paper. On tracing paper, draw rings around a centre and spokes out from it, and number the rings and the spokes. Lay the tracing paper over the sheet and write down the nearest ring and spoke for each dot. Slide the tracing paper a few centimetres to a new position and write down the nearest ring and spoke for each dot again. You should find new labels for the dots, while a ruler between them still reads 3 centimetres, because the dots never moved.

**Takeaway:** Two distance rules that look nothing alike can describe the same surface, because the difference can lie in the painted grid, not in the surface.

*Visuals:* [[two-grids-on-one-playground]]<br>*See:* `problems/one-degree-steps`

### 2. Measurements the labels cannot change · entry · operational

*How can someone holding only two distance rules show that they describe different surfaces?*

**Recap:** Ana and Ben painted different grids on one flat playground, and each wrote down a distance rule. A distance rule says how far apart neighbouring spots on a painted grid are, and a label is the name the grid gives a spot where two of its lines cross. The arrow test: press a cardboard arrow against a surface and carry it around a loop, a path that ends where it began. Never let the arrow swing left or right. On a flat playground it comes back matching its start. On a ball, a small loop marks off a small piece of the ball. A walker who keeps that piece on her left finds the arrow comes back turned. The larger the fraction of the ball in that piece, the bigger the turn.

Now a third friend, Carl, hands you a distance rule for a surface you cannot visit. Does it describe the same surface as Ana's rule for her flat playground?

Imagine a measurement that ignores the labels. A walker with a real tape and a real arrow never reads the paint. So repainting the grid cannot change what she finds.

The arrow test is such a measurement, and a distance rule settles its result. Adding up small steps, the rule gives the length of every path. Three side lengths fix a small triangle's angles, so the rule gives angles too. Keeping the arrow from swinging needs only lengths and angles, which we take on trust here. So Carl's rule decides what the arrow does around every loop.

Suppose one small loop on Carl's surface brings the arrow back turned, while every loop on Ana's playground brings it back matching its start. No repainting changes either result, so the two rules describe different surfaces.

One matching spot is not enough, though. An egg's pointed end is curved like a smaller ball, and the smaller the ball, the larger the fraction a small loop marks off. So that loop turns the arrow more there than at the egg's middle. Look for a result that one surface gives somewhere and the other gives nowhere.

**Takeaway:** A distance rule fixes what the arrow test finds, whatever grid is painted, so a result that one rule gives and the other gives nowhere shows two different surfaces.

*What this leaves out:* Working out the arrow's turn from a distance rule takes calculus; this way claims only that the rule settles the result.

*Continues:* `ways_in/two-grids-one-playground`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[two-grids-on-one-playground]]<br>*See:* `checks/turned-arrow-settles-it`, `checks/egg-and-ball`

### 3. The map as equations · working · calculation

*What equations define the equivalence of two metrics, and how do curvature invariants test them?*

The painted labels of "Measurements the labels cannot change" are coordinates, and a distance rule is a metric. Ana's and Ben's rules, $dx^2 + dy^2$ and $dr^2 + r^2d\phi^2$, describe one plane because $x = r\cos\phi$, $y = r\sin\phi$ turns one into the other. In general, metrics $g_{\mu\nu}(x)$ and $\bar g_{\alpha\beta}(\bar x)$ on $n$-dimensional regions are equivalent when smooth functions $\bar x^\alpha(x)$ with a smooth inverse satisfy

$$g_{\mu\nu}(x) = \frac{\partial\bar x^\alpha}{\partial x^\mu}\frac{\partial\bar x^\beta}{\partial x^\nu}\,\bar g_{\alpha\beta}\big(\bar x(x)\big).$$

Read this as equations for the unknown functions. Both sides are symmetric in $\mu\nu$, so there are $n(n+1)/2$ equations for $n$ functions: 3 for 2 on a surface, 10 for 4 in spacetime. An overdetermined system has solutions only when integrability conditions hold, so guessing a map is unreliable, and a failed guess proves nothing.

Invariants turn the question around. A scalar $I$ built from the metric alone, such as the Gaussian curvature $K$ of a surface or the Kretschmann scalar $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$, must agree at corresponding points:

$$I(x) = \bar I\big(\bar x(x)\big).$$

This condition is necessary, and it contains no derivatives of the unknown map. If one metric takes a value of $I$ that the other never takes, they are inequivalent. Matching values tell you which points may correspond.

Surfaces show both uses. In the arrow test, $K$ is the arrow's turn per unit area around a small loop, counted positive toward the walker's left when the small region lies on that side. For $ds^2 = dr^2 + f(r)^2d\phi^2$ the derivation "Curvature of a spun metric" gives $K = -f''/f$. So $f = \sin r$ gives $K = +1$, a unit sphere, while $f = \sinh r$ and $f = e^r$ both give $K = -1$. The sphere and the hyperbolic plane are inequivalent even near a single point. The two $K = -1$ metrics look different, yet by Minding's theorem, taken on trust here, they are locally equivalent: two Riemannian surfaces with the same constant $K$ are, near any points.

Constant $K$ cannot say which point matches which, because every point looks alike. When $K$ varies, $|\nabla K|^2 = g^{ab}\,\partial_aK\,\partial_bK$ is a second scalar, and its relation to $K$ is invariant. For $f = r^2$, $K = -2/r^2$ and $|\nabla K|^2 = -2K^3$. A metric whose curvature takes the same values but obeys a different relation cannot be equivalent to it near any point where the two relations disagree.

**Takeaway:** Equivalence means solving an overdetermined system for a coordinate change; curvature invariants and their relations must match at corresponding points, which can rule an equivalence out and shows which points correspond.

*What this leaves out:* Treats smooth Riemannian surfaces and generic points where the invariants are regular.

*Continues:* `ways_in/measurements-labels-cannot-change`<br>*Builds on:* [[diffeomorphism]], [[gaussian-curvature]]<br>*Visuals:* [[curvature-fingerprint-curves]]<br>*See:* `derivations/curvature-of-a-spun-metric`, `checks/count-the-equations`, `checks/same-curvature-values`, `problems/two-hyperbolic-planes`

### 4. Schwarzschild in disguise · working · historical-puzzle

*How can invariants unmask a known spacetime written in unfamiliar coordinates?*

The invariants of "The map as equations" matter in practice. Exact solutions of Einstein's equation arrive in whatever coordinates made them solvable, and known solutions have been rediscovered and published as new. Here is one disguise, in isotropic coordinates, with $m = GM/c^2$:

$$ds^2 = -\left(\frac{1 - m/2\rho}{1 + m/2\rho}\right)^2c^2dt^2 + \left(1 + \frac{m}{2\rho}\right)^4\big(d\rho^2 + \rho^2d\Omega^2\big).$$

It looks nothing like the course form with $1 - 2m/r$. Two invariants settle it without guessing. First, the round spheres of symmetry have area $4\pi r^2$ in the course form, so $r$ is the areal radius; in the isotropic form the areal radius is $\rho(1 + m/2\rho)^2$. Second, the Kretschmann scalar is $48m^2/r^6$ in the course form, taken here on trust. If the two metrics describe one spacetime, both invariants must match, and both demand

$$r = \rho\left(1 + \frac{m}{2\rho}\right)^2.$$

Now check that this map works. It gives $1 - 2m/r = \big[(1 - m/2\rho)/(1 + m/2\rho)\big]^2$ and $dr = (1 + m/2\rho)(1 - m/2\rho)\,d\rho$, so $dr^2/(1 - 2m/r) = (1 + m/2\rho)^4d\rho^2$, and every term of the course form becomes the isotropic one. The invariants did more than allow an equivalence: they pointed to the map.

At the Sun's surface, $r = 6.957\times10^8$ m and $m = 1.477$ km. The two labels of one event differ by $r - \rho = 1.477$ km, while the Kretschmann scalar, $9.2\times10^{-46}\ \mathrm{m^{-4}}$, is the same number in both.

**Takeaway:** Matching the areal radius and the Kretschmann scalar shows that the isotropic metric is the Schwarzschild spacetime and yields the coordinate change between them.

*What this leaves out:* Uses spherical symmetry to single out the areal radius; the region $r > 2m$, $\rho > m/2$.

*Continues:* `ways_in/the-map-as-equations`<br>*Builds on:* [[kretschmann-scalar]]<br>*See:* `key_equations/schwarzschild-kretschmann`, `problems/harmonic-radius-disguise`

### 5. Frames, invariants and Cartan's theorem · formal · structure

*Exactly when are two metrics locally equivalent, and which data decide it?*

The invariants that located corresponding events in "Schwarzschild in disguise" were scalars. Cartan's solution compares components in frames instead. Set $G = c = 1$.

*Definitions.* Let $(M, g)$ and $(\bar M, \bar g)$ be smooth pseudo-Riemannian manifolds of dimension $n$ and equal signature, with points $p$ and $\bar p$. They are locally equivalent at $(p, \bar p)$ if a diffeomorphism $\phi$ between neighbourhoods has $\phi(p) = \bar p$ and $\phi^*\bar g = g$. The orthonormal frame bundle $F \to M$ has dimension $N = n(n+1)/2$, which is 10 for spacetime. Its tautological forms $\theta^a$ and Levi-Civita connection forms $\omega^a{}_b$ form a global coframe on $F$ and obey

$$d\theta^a = -\omega^a{}_b\wedge\theta^b,\qquad d\omega^a{}_b = -\omega^a{}_c\wedge\omega^c{}_b + \tfrac12R^a{}_{bcd}\,\theta^c\wedge\theta^d.$$

The frame components of $\nabla^kR$ are functions on $F$. Write $\mathcal I^{(q)}$ for all of them with $k \le q$, and $t_q$ for the number of functionally independent functions among them.

*Necessity.* An isometry lifts to $\Phi: F \to \bar F$ with $\Phi^*\bar\theta = \theta$ and $\Phi^*\bar\omega = \omega$, so $\mathcal I^{(q)} = \bar{\mathcal I}^{(q)}\circ\Phi$ for every $q$. Scalar invariants are the special case with the frame dependence contracted away.

*Stopping.* The ranks obey $t_0 \le t_1 \le \dots \le N$. Let $q$ be the first order with $t_{q+1} = t_q$. Every order-$(q+1)$ component is then a function of $t_q$ independent ones, and so is every higher order, because the differential of an invariant expands in the coframe with next-order components as coefficients. The ranks rise strictly until they stall, and $t_0 \ge 1$ unless the curvature has constant components on $F$, which means constant curvature. So components of order at most $N$ suffice: 10 in four dimensions.

*Theorem (Cartan).* Suppose each $t_k$ is constant near $p$ and near $\bar p$. Then $g$ and $\bar g$ are locally equivalent at $(p, \bar p)$ exactly when both stall at the same $q$ with the same $t_q$, all components up to order $q+1$ are the same functions of corresponding independent invariants, and some frames $u$ over $p$ and $\bar u$ over $\bar p$ give equal components up to order $q+1$.

*Proof sketch of sufficiency.* In $F\times\bar F$, the set $S$ where $\mathcal I^{(q)} = \bar{\mathcal I}^{(q)}$ is a submanifold of dimension $2N - t_q$ through $(u, \bar u)$. Restrict the Pfaffian system $\theta - \bar\theta = 0$, $\omega - \bar\omega = 0$ to $S$. Differentials of matching invariants agree along $S$, and their coefficients are matching order-$(q+1)$ components, so $t_q$ combinations of the system vanish there, leaving rank $N - t_q$. The structure equations, whose curvature coefficients agree on $S$, put the exterior derivatives of the system in the ideal it generates. Frobenius then gives an integral manifold of dimension $N$ through $(u, \bar u)$: the graph of a local diffeomorphism preserving $\theta$ and $\omega$, which descends to the isometry $\phi$. The regularity details are taken on trust here.

*Limits.* The theorem is local and needs constant ranks. Local equivalence says nothing global: a flat torus and the plane share every invariant. Deciding whether two functional relations coincide is not algorithmic in full generality. Finally, frame components cannot always be traded for scalars. The group $O(n)$ is compact, so invariant polynomials separate its orbits, and in Riemannian signature scalar invariants of $R, \nabla R, \dots$ determine the components at a point up to rotation. The Lorentz group is not compact. The vacuum plane wave

$$ds^2 = -2\,du\,dv + (x^2 - y^2)\,a(u)\,du^2 + dx^2 + dy^2$$

has $R_{uxux} = -a(u)$, yet boosts shrink its curvature components toward zero, so every scalar polynomial invariant takes its Minkowski value, zero.

**Takeaway:** Metrics are locally equivalent exactly when frame components of curvature and its derivatives, up to the order where no new invariants appear, obey the same relations and agree at some frames; scalars can fail.

*What this leaves out:* Smooth metrics at points where the numbers of independent invariants are locally constant.

*Continues:* `ways_in/the-map-as-equations`, `ways_in/schwarzschild-in-disguise`<br>*Builds on:* [[isometry]], [[orthonormal-frame]]<br>*See:* `key_equations/cartan-equivalence-condition`, `checks/plane-wave-scalars`, `checks/torus-and-plane`, `problems/minding-by-geodesic-polar-coordinates`

### 6. Where scalars fail, and what replaced them · research · contrast

*Which spacetimes do scalar invariants fail to characterize, and how is Cartan's method used in practice?*

The plane wave of "Frames, invariants and Cartan's theorem" shares every scalar polynomial invariant with Minkowski spacetime, yet it is curved. Research since then has mapped exactly where scalars fail and turned Cartan's theorem into a working procedure.

*The practical procedure.* Brans adapted Cartan's method to spacetime, and Karlhede recast it so that the frame is fixed as far as possible at each order. The algebraic types of the Weyl and Ricci tensors, the Petrov and Segre types, fix it first, then covariant derivatives fix more. Each order records the number $t_q$ of functionally independent invariants and the dimension $s_q$ of the remaining isotropy group. The procedure stops when neither changes, and the isometry group then has dimension $4 - t_q + s_q$. Karlhede showed that no derivative beyond the seventh is needed in four dimensions, and Milson and Pelavas showed that bound is sharp, with type N null radiation on an anti-de Sitter background. In practice classifications rarely need more than a few derivatives, and computer algebra made them routine, so a claimed new solution can be compared with known ones. The final comparison of functional relations remains undecidable in a formal sense, so some cases need insight.

*When scalars suffice.* Pravda, Pravdová, Coley and Milson found all four-dimensional spacetimes whose scalar curvature invariants all vanish. They form a subclass of the Kundt spacetimes, which carry a null geodesic congruence without expansion, shear or twist, and they include the pp-waves. Coley, Hervik and Pelavas then proved that a four-dimensional Lorentzian metric not locally characterized by its scalar polynomial invariants must belong to the degenerate Kundt class. Outside that class, which excludes the Schwarzschild and Kerr spacetimes, scalars determine the metric locally. The dichotomy explains the plane wave: its curvature is aligned with its null congruence, where boosts rescale it.

*Invariants as detectors.* Scalar invariants also locate features without coordinates, which numerical relativity needs because its coordinates are arbitrary. Page and Shoom built scalars, from wedge products of gradients of curvature invariants, that vanish on the horizon of any stationary black hole. Mars characterized the Kerr metric among stationary, asymptotically flat vacuum spacetimes by the vanishing, together with mild further conditions, of a spacetime version of the Simon tensor built from the curvature and the stationary Killing vector.

**Takeaway:** Karlhede's frame fixing needs at most seven derivatives in four dimensions; scalar invariants fail only for degenerate Kundt spacetimes, and invariant constructions now locate horizons and recognize Kerr.

*What this leaves out:* Four-dimensional spacetimes; bounds and theorems as proved in the cited work.

*Continues:* `ways_in/frames-invariants-and-cartan`<br>*See:* `checks/kundt-claim`, `research_horizon/practical-invariant-classification`, `research_horizon/when-scalar-invariants-suffice`, `research_horizon/invariant-horizon-detection`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| spot | — | Any place on a surface. A painted grid gives a label to each spot where two of its lines cross. | — |
| distance rule | — | A statement of how far apart neighbouring spots on a painted grid are, for every part of the grid. | [[metric-tensor]] |
| label | — | The name a painted grid gives a spot where two of its lines cross, such as a row and column number, or a ring and spoke number. | — |
| equivalence problem | — | The question of whether two distance rules, written for different grids, describe the same surface or space. | [[equivalence-problem]] |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To change which way the arrow points, left or right, while it lies against the surface. The arrow test never lets it swing. | — |
| arrow test | — | Carry a cardboard arrow around a loop, pressed against the surface, never letting it swing, then compare its direction with its starting direction. | [[holonomy]] |

## Key equations

### Equivalence as a coordinate change · working

$$
g_{\mu\nu}(x) = \frac{\partial\bar x^\alpha}{\partial x^\mu}\frac{\partial\bar x^\beta}{\partial x^\nu}\,\bar g_{\alpha\beta}\big(\bar x(x)\big)
$$

Two metrics are equivalent when some coordinate change carries one onto the other; read as equations, these are $n(n+1)/2$ conditions on $n$ unknown functions.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $g_{\mu\nu}(x)$ | components of the first metric in coordinates $x$ | the first metric |
| $\bar g_{\alpha\beta}(\bar x)$ | components of the second metric in coordinates $\bar x$ | the second metric |
| $\bar x^\alpha(x)$ | the unknown coordinate change, smooth with a smooth inverse | x bar as a function of x |

**Holds when:** Both metrics on $n$-dimensional regions; the map is a diffeomorphism between those regions.  
**Say it:** “The first metric equals the second metric, evaluated at the image point, contracted with two derivatives of the coordinate change.”  
**Justified by:** `diffeomorphism`

### Invariants agree at corresponding points · working

$$
I(x) = \bar I\big(\bar x(x)\big)
$$

Any scalar built from the metric alone, such as $K$ or the Kretschmann scalar, takes the same value at points an equivalence matches.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $I$ | a curvature invariant of the first metric | the invariant |
| $\bar I$ | the same invariant computed from the second metric | the invariant of the second metric |

**Holds when:** A necessary condition only; it contains no derivatives of the map.  
**Say it:** “The invariant at a point equals the other metric's invariant at the matching point.”  
**Justified by:** `stated`

### Curvature of a spun metric · working

$$
ds^2 = dr^2 + f(r)^2\,d\phi^2 \;\Rightarrow\; K = -\frac{f''}{f}
$$

A surface metric of this form has Gaussian curvature minus the second derivative of $f$ over $f$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $f(r)$ | length of the curve at fixed $r$ per unit change of $\phi$ (its circumference divided by $2\pi$ when $\phi$ has period $2\pi$) | f of r |
| $K$ | Gaussian curvature | K |

**Holds when:** Riemannian surface, $f > 0$ on the region considered.  
**Say it:** “K equals minus f double prime over f.”  
**Justified by:** `derivations/curvature-of-a-spun-metric`

### Kretschmann scalar of Schwarzschild · working

$$
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = \frac{48\,G^2M^2}{c^4r^6}
$$

The Schwarzschild curvature invariant depends only on the areal radius, so it can identify corresponding events.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $r$ | areal radius, the sphere of symmetry through the event having area $4\pi r^2$ | r |
| $M$ | mass | M |

**Holds when:** Schwarzschild spacetime; independent of the overall sign convention of the Riemann tensor.  
**Say it:** “The Kretschmann scalar is forty-eight G squared M squared over c to the fourth r to the sixth.”  
**Justified by:** `stated`

### Cartan's equivalence condition · formal

$$
\mathcal I^{(k)} = \bar{\mathcal I}^{(k)}\circ\Phi,\qquad k = 0, 1, \dots, q+1,\qquad t_{q+1} = t_q
$$

Frame components of curvature and its covariant derivatives up to the stalling order must correspond under a frame-bundle map; with equal ranks and relations, this is also sufficient for local equivalence.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal I^{(k)}$ | frame components of $R, \nabla R, \dots, \nabla^kR$, as functions on the orthonormal frame bundle | the invariants up to order k |
| $\Phi$ | a map of frame bundles preserving the coframe and connection forms | the frame bundle map |
| $t_q$ | number of functionally independent invariants up to order $q$ | t sub q |

**Holds when:** Smooth metrics of equal dimension and signature; ranks $t_k$ locally constant; local statement only; order $q+1 \le n(n+1)/2$.  
**Say it:** “The invariants up to one order past the stalling order must agree under a frame bundle map, and the number of independent invariants must have stopped growing.”  
**Justified by:** `stated`

## Derivations

### Curvature of a spun metric · working

**Goal:** Show that $ds^2 = dr^2 + f(r)^2d\phi^2$ has Gaussian curvature $K = -f''/f$.

1. The metric has $g_{rr} = 1$ and $g_{\phi\phi} = f^2$, so the only nonzero Christoffel symbols are $\Gamma^r{}_{\phi\phi} = -ff'$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = f'/f$.
2. The course definition gives $R^r{}_{\phi r\phi} = \partial_r\Gamma^r{}_{\phi\phi} - \partial_\phi\Gamma^r{}_{r\phi} + \Gamma^r{}_{r\lambda}\Gamma^\lambda{}_{\phi\phi} - \Gamma^r{}_{\phi\lambda}\Gamma^\lambda{}_{r\phi}$.
3. The second term vanishes because nothing depends on $\phi$, and the third because every $\Gamma^r{}_{r\lambda} = 0$. The first term is $-f'^2 - ff''$.
4. In the last term only $\lambda = \phi$ contributes: $-\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = +f'^2$. So $R^r{}_{\phi r\phi} = -ff''$.
5. Lower the index with $g_{rr} = 1$ and divide by $g_{rr}g_{\phi\phi} = f^2$: $K = R_{r\phi r\phi}/(g_{rr}g_{\phi\phi}) = -f''/f$.

**Result:** $K = -f''/f$. Checks: $f = r$ gives $0$, $f = \sin r$ gives $+1$, and $f = \sinh r$ and $f = e^r$ give $-1$.

## Problems

### `one-degree-steps` · entry · difficulty 1 · estimate

Ben's grid on the flat playground has rings around a flagpole and spokes one degree apart. How much ground does one step along the ring 10 metres from the pole cover? How many such steps make the whole ring? Why does Ben's rule change from ring to ring when the playground is flat everywhere?

**Hints**

1. How long is a ring 10 metres from the pole? It is about 6.28 times 10 metres.
2. The spokes are one degree apart, so every ring is split into 360 steps.

**Answer:** About 17 centimetres per step, and 360 steps make the ring. The rule changes because rings farther out are longer, while every ring gets the same 360 steps.

**Must contain:** The ring is about 63 metres long; One step covers about 17 centimetres; The rule changes because of the painted grid, not the playground

**Numeric:** ground covered by one step along the ring 10 metres from the pole = 17.45 cm (magnitude, ±5%)

**Solution**

1. The ring 10 metres from the pole is about 6.28 times 10 metres long, about 63 metres.
2. Ben's spokes split every ring into 360 steps, so one step covers 63 metres divided by 360, about 17 centimetres.
3. A ring 20 metres out is twice as long but still has 360 steps, so each step covers twice as much ground. The steps differ because of how the grid was painted, while the playground is the same flat playground.

### `two-hyperbolic-planes` · working · difficulty 2 · derivation

Find an explicit coordinate change that turns the upper half-plane metric $d\bar s^2 = (dX^2 + dY^2)/Y^2$, $Y > 0$, into $ds^2 = dx^2 + e^{2x}dy^2$. Use it to find the Gaussian curvature of the half-plane without computing any Christoffel symbols of the half-plane metric. Is the equivalence local or global?

**Hints**

1. Try $X$ depending only on $y$, and $Y$ only on $x$.
2. You need $dY^2/Y^2 = dx^2$.
3. For the second metric, use $K = -f''/f$ with $f = e^x$.

**Answer:** $X = y$, $Y = e^{-x}$. Then $(dX^2 + dY^2)/Y^2 = dx^2 + e^{2x}dy^2$, so the half-plane has $K = -1$. The map is a bijection from the whole $(x, y)$ plane onto $Y > 0$, so the equivalence is global.

**Must contain:** X equals y and Y equals e to the minus x; The pulled-back metric is d x squared plus e to the two x d y squared; Both metrics have curvature minus one; The map is a bijection, so the equivalence is global

**Solution**

1. With $Y = e^{-x}$, $dY = -e^{-x}dx$, so $dY^2/Y^2 = dx^2$.
2. With $X = y$, $dX^2/Y^2 = e^{2x}dy^2$.
3. Adding gives $(dX^2 + dY^2)/Y^2 = dx^2 + e^{2x}dy^2$.
4. The second metric is a spun metric with $f = e^x$, so $K = -f''/f = -1$. An isometry preserves $K$, so the half-plane also has $K = -1$ everywhere.
5. As $x$ runs over all reals, $Y = e^{-x}$ runs over all $Y > 0$ exactly once, and $X = y$ over all reals, so the map is a global bijection with smooth inverse $x = -\ln Y$, $y = X$.

### `harmonic-radius-disguise` · working · difficulty 2 · calculation

A paper presents a new static vacuum metric, with $m = GM/c^2$ and $x > m$: $$ds^2 = -\frac{x - m}{x + m}\,c^2dt^2 + \frac{x + m}{x - m}\,dx^2 + (x + m)^2\,d\Omega^2.$$ Its Kretschmann scalar is $48m^2/(x + m)^6$. Use invariants to decide whether it is the Schwarzschild spacetime, find the correspondence of radial labels, and verify it. For Earth, with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$, how much do the labels $r$ and $x$ of one event differ?

**Hints**

1. What is the area of the round sphere at fixed $t$ and $x$?
2. Compare the Kretschmann scalar with $48m^2/r^6$.
3. Substitute your guess into $1 - 2m/r$.

**Answer:** It is the Schwarzschild spacetime, with $r = x + m$. The labels differ by $m = GM/c^2 = 4.4$ mm for Earth.

**Must contain:** The areal radius is x plus m; The Kretschmann scalars agree when r equals x plus m; Substituting r equals x plus m reproduces every term; For Earth the labels differ by about 4.4 millimetres

**Numeric:** difference between r and x for Earth = 4.435 mm (magnitude, ±2%)

**Solution**

1. The sphere at fixed $t$ and $x$ has area $4\pi(x + m)^2$, so its areal radius is $x + m$. For Schwarzschild the areal radius is $r$.
2. The Schwarzschild Kretschmann scalar is $48m^2/r^6$. With $r = x + m$ it equals the given $48m^2/(x + m)^6$, so both invariants point to $r = x + m$.
3. Substitute: $1 - 2m/r = (x + m - 2m)/(x + m) = (x - m)/(x + m)$, $dr = dx$, and $r^2d\Omega^2 = (x + m)^2d\Omega^2$. The course form becomes the given metric term by term, and $x > m$ is the region $r > 2m$.
4. $m = 3.986\times10^{14}/(2.998\times10^8)^2 = 4.435\times10^{-3}$ m, so the two labels of every event differ by about 4.4 mm.

**Targets:** `same-scalar-values-same-geometry`

### `minding-by-geodesic-polar-coordinates` · formal · difficulty 3 · proof

Let a Riemannian surface have constant Gaussian curvature $K$. In geodesic polar coordinates about a point $p$, $g = dr^2 + G(r,\phi)^2d\phi^2$ with $G(0,\phi) = 0$ and $\partial_rG(0,\phi) = 1$, taken on trust. Using $K = -\partial_r^2G/G$, show that $G$ is determined by $K$ alone, and deduce that two surfaces with the same constant $K$ are locally isometric. Explain what breaks when $K$ varies.

**Hints**

1. For each fixed $\phi$, the condition is a linear ordinary differential equation in $r$ with two initial conditions.
2. Map points with equal $(r, \phi)$ using the exponential maps and a linear isometry of the tangent planes.
3. If $K$ varies, on which surface's coordinates does it depend?

**Answer:** $\partial_r^2G = -KG$ with $G(0) = 0$, $\partial_rG(0) = 1$ has the unique solution $G = \sin(\sqrt K\,r)/\sqrt K$ for $K > 0$, $G = r$ for $K = 0$, and $G = \sinh(\sqrt{-K}\,r)/\sqrt{-K}$ for $K < 0$, independent of $\phi$. Identifying geodesic polar coordinates of the two surfaces pulls one metric back to the other on normal neighbourhoods, a local isometry. When $K$ varies, $K(r,\phi)$ differs between the surfaces unless matching points are known in advance, so the equations for $G$ differ and the invariant analysis is needed.

**Must contain:** The Jacobi-type equation for G with its initial conditions has a unique solution; The solution depends only on K, not on phi or the surface; Equal geodesic polar coordinates define a local isometry; Varying K makes the equation depend on the unknown correspondence

**Solution**

1. From $K = -\partial_r^2G/G$, for each fixed $\phi$ the function $G(\cdot,\phi)$ solves $\partial_r^2G + KG = 0$ with $G(0) = 0$ and $\partial_rG(0) = 1$.
2. With $K$ constant this linear equation has constant coefficients, and uniqueness for initial value problems gives $G = \sin(\sqrt K\,r)/\sqrt K$, $r$, or $\sinh(\sqrt{-K}\,r)/\sqrt{-K}$ as $K$ is positive, zero or negative.
3. So in geodesic polar coordinates both surfaces have the identical metric $dr^2 + G(r)^2d\phi^2$ for $r$ less than the radius of a normal neighbourhood (and $r < \pi/\sqrt K$ when $K > 0$).
4. Choose a linear isometry of $T_pM$ onto $T_{\bar p}\bar M$; with the exponential maps it sends the point with coordinates $(r, \phi)$ to the point with the same coordinates. The pulled-back metric equals $g$, so the map is a local isometry. The polar singularity at $r = 0$ is harmless because both metrics are smooth there and agree on a punctured neighbourhood.
5. If $K$ varies, $K$ is a given function of $(r, \phi)$ on each surface, and these functions agree only if the correspondence of points is already the right one. Finding it is exactly what the invariants $K$ and $|\nabla K|^2$ are for.

## Teaching arc

1. **Paint two grids on one playground** (entry). Ask whether two very different distance rules could describe the same flat playground, then reveal the square grid and the rings and spokes. *Why:* The surprise separates the labels from the playground before any formula appears. *Predict:* Could a square grid and a grid of rings and spokes give two different distance rules for the very same flat playground? *Visual:* [[two-grids-on-one-playground]] *Uses:* `ways_in/two-grids-one-playground`, `checks/same-ground-different-rules`
2. **Measure what paint cannot change** (entry). Use the arrow test to tell a flat surface from a curved one, then show with the egg why one matching spot is not enough. *Why:* It gives the beginner a test that works from the rules alone. *Predict:* If one spot on an egg and one spot on a ball turn the arrow by the same amount, are they the same surface? *Uses:* `ways_in/measurements-labels-cannot-change`, `checks/turned-arrow-settles-it`, `checks/egg-and-ball`
3. **Count the equations, then use invariants** (working). Write the transformation law, count its equations, then compare $K$ and the relation between $K$ and $|\nabla K|^2$ for spun metrics. *Why:* Learners see why guessing fails and why invariants are the efficient test. *Predict:* Two surfaces have curvatures that take exactly the same values. Must they be the same surface? *Visual:* [[curvature-fingerprint-curves]] *Uses:* `ways_in/the-map-as-equations`, `checks/count-the-equations`, `checks/same-curvature-values`
4. **Unmask a disguised Schwarzschild metric** (working). Match the areal radius and Kretschmann scalar of the isotropic form, then let the learner repeat it for another radial label. *Why:* It shows invariants finding the map, not only allowing it. *Uses:* `ways_in/schwarzschild-in-disguise`, `problems/harmonic-radius-disguise`
5. **State Cartan's theorem and its limits** (formal). Present frame invariants, the stopping rule and the Frobenius sketch, then test the flat torus and the plane wave. *Why:* The two tests separate local from global equivalence and frame components from scalars. *Uses:* `ways_in/frames-invariants-and-cartan`, `checks/torus-and-plane`, `checks/plane-wave-scalars`
6. **Map where scalars fail** (research). Discuss the degenerate Kundt theorem, Karlhede's bound, and invariant horizon detectors. *Why:* It turns a counterexample into a precise research-level classification. *Uses:* `ways_in/beyond-scalar-invariants`, `checks/kundt-claim`

## Misconceptions

### “If two distance rules look different, they must describe different surfaces.” · entry · `different-rules-different-surfaces`

- **Why it is tempting:** The rule is the only description you hold, so a different rule looks like a different place.
- **What is true:** The same surface can carry many painted grids, and each grid gives its own rule. Measurements a walker makes on the surface ignore the labels, so only they can show that two surfaces differ.
- **Exposed by:** `checks/same-ground-different-rules`

### “If both surfaces turn the arrow by the same amount at one spot, they are the same surface.” · entry · `one-spot-is-enough`

- **Why it is tempting:** One matching measurement feels like a match.
- **What is true:** The turn can change from spot to spot, as on an egg, so one match proves nothing. For loops of one size, a turn that one surface gives somewhere and the other gives nowhere shows that they differ.
- **Exposed by:** `checks/egg-and-ball`

### “Two metrics whose curvature scalars take the same values describe the same geometry.” · working · `same-scalar-values-same-geometry`

- **Why it is tempting:** Scalars do not depend on coordinates, so matching them seems to settle everything.
- **What is true:** Values must match at corresponding points, so relations between invariants, such as the gradient of the curvature against the curvature, must match too. Surfaces whose curvature takes the same values can obey different relations.
- **Exposed by:** `checks/same-curvature-values`

### “If every scalar curvature invariant vanishes, spacetime is flat.” · formal · `zero-scalars-means-flat`

- **Why it is tempting:** In Riemannian geometry, vanishing scalar invariants do force zero curvature.
- **What is true:** The Lorentz group is not compact, so boosts can shrink a null curvature tensor toward zero without changing any polynomial invariant. Vacuum plane waves are curved yet have every scalar polynomial invariant zero.
- **Exposed by:** `checks/plane-wave-scalars`

### “Two spaces with identical invariants everywhere are the same space.” · formal · `local-means-global`

- **Why it is tempting:** Cartan's theorem sounds like a complete answer.
- **What is true:** Cartan's theorem gives local isometries only. A flat torus and the plane share every invariant, yet one has finite area and closed geodesics.
- **Exposed by:** `checks/torus-and-plane`

### “Because plane waves fool scalar invariants, scalar invariants cannot characterize any Lorentzian spacetime.” · research · `scalars-useless-in-lorentzian`

- **Why it is tempting:** One striking counterexample suggests a general failure.
- **What is true:** Scalar invariants fail only for degenerate Kundt spacetimes. Schwarzschild and Kerr lie outside that class and are characterized locally by their scalars.
- **Exposed by:** `checks/kundt-claim`

## Checks

1. **Entry · predict** `checks/same-ground-different-rules`. On a flat playground, Ana paints rows and columns one metre apart. Ben paints rings around a flagpole, one every metre, and spokes one degree apart. Ana's rule says one step covers one metre everywhere. Ben's rule says one step along a ring covers more ground far from the pole than near it. Does that difference mean Ana and Ben describe different surfaces?
   - **Hints:** What would a tape measure laid on the playground read for each friend?
   - **Answer:** No. Both grids are painted on the same flat playground, so a tape laid between any two spots reads the same whichever grid is painted. Ben's rule changes because his rings are longer farther from the pole, while each ring is split into the same 360 steps. So each step on an outer ring covers more ground. The difference is in the grids, not in the playground.
   - **Must contain:** No, they describe the same surface; A tape between two spots reads the same whichever grid is painted; Ben's steps grow because outer rings are longer
   - **Targets:** `different-rules-different-surfaces`
   - **Visual:** [[two-grids-on-one-playground]]
2. **Entry · explain** `checks/turned-arrow-settles-it`. Dana's distance rule describes a surface where every loop brings a cardboard arrow back matching its start. Eli's rule describes a surface where one small loop brings the arrow back turned by one degree. If Eli repaints his surface with some new grid, could his new rule describe the same surface as Dana's? Why?
   - **Hints:** Does the walker doing the arrow test ever read the paint?
   - **Answer:** No. The arrow test is done with a real arrow on the surface, so the painted labels play no part in it. Repainting changes only the labels, not the surface. So on Eli's surface that loop still brings the arrow back turned by one degree, whatever grid is painted. On Dana's surface no loop ever does that. So the two rules describe different surfaces.
   - **Must contain:** No, they describe different surfaces; The arrow test does not use the painted labels; Eli's surface has a loop that Dana's surface never matches
3. **Entry · explain** `checks/egg-and-ball`. On a smooth egg and on a smooth ball, you do the arrow test around small loops of the same size. You find one spot on each where the arrow comes back turned by the same amount. Does that show that the egg and the ball are the same surface?
   - **Hints:** Does an egg turn the arrow the same way at its pointed end and at its middle?
   - **Answer:** No. Every spot on a ball is curved alike, so loops of the same size turn the arrow by the same amount at every spot. An egg's pointed end is curved like a smaller ball, and the smaller the ball, the larger the fraction a loop of one size marks off. So a loop at the pointed end turns the arrow more than the same-size loop at the egg's middle. So the egg has spots whose turn the ball gives nowhere. That difference shows they are different surfaces, although one spot on each matched.
   - **Must contain:** No, one matching spot is not enough; A ball gives the same turn at every spot; An egg gives different turns at different spots
   - **Targets:** `one-spot-is-enough`
4. **Working · numeric** `checks/count-the-equations`. Two metrics are given on four-dimensional regions. Written as equations for an unknown coordinate change, how many independent equations does the transformation law impose, and how many unknown functions must satisfy them? What are the two numbers for a surface, and what does the mismatch imply?
   - **Hints:** How many independent components does a symmetric 4 by 4 matrix have?
   - **Answer:** The metric is symmetric, so the law gives one equation per independent component: $4\cdot5/2 = 10$ equations for the 4 functions $\bar x^\alpha(x)$. On a surface it gives 3 equations for 2 functions. With more equations than unknowns, solutions exist only when integrability conditions hold, so a map usually does not exist, and failing to guess one proves nothing either way.
   - **Must contain:** Ten equations for four unknown functions in four dimensions; Three equations for two functions on a surface; The system is overdetermined, so solutions need integrability conditions
   - **Numeric:** equations in four dimensions = 10 1 (magnitude, ±0); unknown functions in four dimensions = 4 1 (magnitude, ±0)
5. **Working · numeric** `checks/same-curvature-values`. Take $ds^2 = dr^2 + r^4d\phi^2$ and $ds^2 = dr^2 + r^6d\phi^2$ for $r > 0$, with lengths in units of a fixed length. On both, the Gaussian curvature takes every negative value. At a point where $K = -1$, find $|\nabla K|^2$ for each. Are the surfaces locally equivalent anywhere?
   - **Hints:** Use $K = -f''/f$. / With $g_{rr} = 1$ and $K$ depending only on $r$, $|\nabla K|^2 = (dK/dr)^2$.
   - **Answer:** No. For $f = r^2$, $K = -f''/f = -2/r^2$, so $K = -1$ at $r^2 = 2$, and $|\nabla K|^2 = (dK/dr)^2 = 16/r^6 = 2$. For $f = r^3$, $K = -6/r^2$, so $K = -1$ at $r^2 = 6$, and $|\nabla K|^2 = 144/r^6 = 2/3$. An equivalence would send points with $K = -1$ to points with $K = -1$ and preserve the scalar $|\nabla K|^2$. Every point with $K = -1$ gives 2 on the first surface and $2/3$ on the second, and the same mismatch occurs at every value of $K$, since the relations are $|\nabla K|^2 = -2K^3$ and $-\tfrac23K^3$.
   - **Must contain:** Squared gradient 2 on the first surface at K equal to minus one; Squared gradient two thirds on the second; The relation between the two invariants differs, so no local equivalence exists
   - **Numeric:** squared gradient of K for r to the fourth = 2 1 (magnitude, ±2%); squared gradient of K for r to the sixth = 0.6667 1 (magnitude, ±2%)
   - **Targets:** `same-scalar-values-same-geometry`
   - **Visual:** [[curvature-fingerprint-curves]]
6. **Formal · explain** `checks/plane-wave-scalars`. The vacuum plane wave $ds^2 = -2\,du\,dv + (x^2 - y^2)a(u)\,du^2 + dx^2 + dy^2$ has $R_{uxux} = -a(u)$, yet its Kretschmann scalar and every other scalar polynomial curvature invariant vanish. Is it locally equivalent to Minkowski spacetime where $a \neq 0$? Why do scalar invariants miss the difference, when for a Riemannian metric they would not?
   - **Hints:** What does a boost along the wave's null direction do to its curvature components? / Is the zero tensor in the closure of that orbit?
   - **Answer:** No. A nonzero component means the Riemann tensor is nonzero, and an isometry would carry it to the zero tensor of Minkowski spacetime. The curvature is null, aligned with $\partial_v$: a boost along that direction multiplies every frame component of the curvature and of its covariant derivatives by a positive power of one factor, which can be made as small as desired. A polynomial invariant is constant on the boost orbit and continuous, so it equals its value at the zero tensors, zero. For a Riemannian metric the frame group $O(n)$ is compact, its orbits are closed, and invariant polynomials separate them, so vanishing invariants would force vanishing curvature.
   - **Must contain:** Not equivalent, because the Riemann tensor is nonzero; Boosts shrink the null curvature toward zero along its orbit; Invariants are continuous and constant on orbits, so they vanish; Compact orthogonal groups have closed orbits separated by invariants
   - **Targets:** `zero-scalars-means-flat`
7. **Formal · explain** `checks/torus-and-plane`. A flat torus, made by identifying opposite sides of a square of side $L$, and the Euclidean plane have identical Cartan invariants at every point. Are they equivalent? State precisely what Cartan's theorem gives here and what it does not.
   - **Hints:** Compare total areas and closed geodesics.
   - **Answer:** Locally, yes: all curvature components vanish on both, the ranks are constant (all zero), and Cartan's theorem gives a local isometry from a neighbourhood of any torus point onto a disk in the plane. Globally, no: the torus has finite area $L^2$ and closed geodesics of length $L$, while the plane has infinite area and no closed geodesics. Cartan's theorem is local; global equivalence also needs topological data, such as the fundamental group and its action by isometries.
   - **Must contain:** Locally isometric by Cartan's theorem; Not globally isometric: finite area and closed geodesics; Global equivalence needs topology beyond local invariants
   - **Targets:** `local-means-global`
8. **Research · evaluate-claim** `checks/kundt-claim`. A student claims: since some vacuum plane waves share all scalar polynomial curvature invariants with Minkowski spacetime, scalar invariants cannot tell the Schwarzschild spacetime from other spacetimes either. Evaluate the claim.
   - **Hints:** Which class of metrics does the characterization theorem single out?
   - **Answer:** Overstated. Scalar invariants fail only when boosts can shrink the curvature and its derivatives toward a different tensor, and in four dimensions this happens only for degenerate Kundt metrics, by the theorem of Coley, Hervik and Pelavas. A Kundt metric needs a null geodesic congruence free of shear, expansion and twist. In Schwarzschild, the shear-free null geodesic congruences are the principal null ones, which expand, so Schwarzschild is not Kundt, and its scalar invariants characterize it locally.
   - **Must contain:** Failure is confined to degenerate Kundt metrics; Schwarzschild has no expansion-free shear-free null geodesic congruence; Schwarzschild is characterized locally by its scalar invariants
   - **Targets:** `scalars-useless-in-lorentzian`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Comparing invariants of metrics written in opposite signatures | Signature $(-,+,+,+)$. Convert both metrics to it before comparing invariants. | Some texts use $(+,-,-,-)$. Replacing $g$ by $-g$ leaves the Christoffel symbols and $R^\rho{}_{\sigma\mu\nu}$ unchanged, flips the sign of the Ricci scalar, and leaves the Kretschmann scalar unchanged, so linear invariants can seem to disagree for one geometry. |
| Sign of frame components in published classifications | The course Riemann tensor $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \dots$, with a sphere of radius $a$ having $R = +2/a^2$. | Some texts define the Riemann tensor with the opposite overall sign. Frame components and the Ricci scalar then change sign while quadratic invariants do not; translate a published table of invariants before matching it against a course computation. |

## Visuals

- ★ [[two-grids-on-one-playground]] (flagship): Separates painted labels from the surface: two grids, two distance rules, one set of ruler readings. *Sketch:* A flat playground seen from above with two switchable overlays: a square grid and rings with spokes around a flagpole. The learner drags two nearby spots; each overlay shows its own label differences and its distance rule, while a tape readout on the playground stays fixed. A slider moves the pair outward to show one step along a ring covering more ground on outer rings. A toggle replaces the playground with a ball patch, where an arrow-test readout for a small loop differs from the playground's zero whatever overlay is shown.
- [[curvature-fingerprint-curves]] (core): Shows invariants as fingerprints: equivalent surfaces share a curve of squared curvature gradient against curvature. *Sketch:* Left: a spun surface $dr^2 + f(r)^2d\phi^2$ chosen from presets ($r$, $\sin r$, $\sinh r$, $e^r$, $r^2$, $r^3$). Right: a plot of $|\nabla K|^2$ against $K$, with the current surface's curve or point highlighted. Constant-curvature surfaces collapse to points on the horizontal axis ($\sinh r$ and $e^r$ land on the same point), while $r^2$ and $r^3$ trace different curves over the same range of $K$, proving they are inequivalent. A marker dragged along the surface moves along its curve.

## Tutor moves

**Open with**

- Two friends draw maps of the same town. One uses a square grid, and the other uses rings around the town hall with spokes going out. Their tables of distances between grid spots look nothing alike. Could both maps describe the same town correctly? *(prediction)*
- Suppose all you had were two tables of distances between neighbouring grid spots, and no pictures. How could you check whether the two tables describe the same surface? *(reflection)*

**If the learner is stuck**

- *The learner treats grid labels or step sizes as features of the surface.* → Do the tracing-paper try-it of "Two grids on one playground": the ruler reading stays fixed while the labels change. *Uses:* `ways_in/two-grids-one-playground`, `checks/same-ground-different-rules`
- *The learner tries to guess a coordinate change and gives up.* → Compute an invariant for both metrics first, such as the areal radius or the Kretschmann scalar, and let matching values suggest the map. *Uses:* `ways_in/schwarzschild-in-disguise`, `problems/harmonic-radius-disguise`

**Common questions**

- *If Earth is a ball, why does a flat map of my town work?* (entry) Because the ball's curving is tiny over a town. Take a loop around a town of 100 square kilometres. Carrying an arrow around it without letting it swing turns the arrow by only about one seven-thousandth of a degree. So a flat distance rule and a ball's distance rule agree over the town far better than any map can show. Over a whole continent the difference becomes easy to find. *Uses:* `ways_in/measurements-labels-cannot-change`
- *Isn't comparing the Kretschmann scalar enough to decide equivalence?* (working) It is only a necessary test. Values must agree at corresponding points, relations between invariants such as $|\nabla K|^2$ against $K$ must agree too, and in Lorentzian signature curved plane waves have every scalar polynomial invariant equal to zero. *Uses:* `checks/same-curvature-values`, `checks/plane-wave-scalars`

**Switching levels**

- To working when: asks how to check equivalence with formulas; uses coordinates and partial derivatives comfortably. Write the transformation law, count its equations, and compare the curvature of spun metrics. *Uses:* `ways_in/the-map-as-equations`, `derivations/curvature-of-a-spun-metric`
- To formal when: asks whether matching invariants guarantee a map; is comfortable with frames and differential forms. State Cartan's theorem with the stopping rule, then prove Minding's theorem in geodesic polar coordinates. *Uses:* `ways_in/frames-invariants-and-cartan`, `problems/minding-by-geodesic-polar-coordinates`
- To research when: asks about classifying exact solutions, plane waves, or finding horizons with invariants. Open the degenerate Kundt theorem and the practical procedure. *Uses:* `ways_in/beyond-scalar-invariants`, `research_horizon/when-scalar-invariants-suffice`

**Pronunciations:** Minding → MIN-ding; Christoffel → kris-TOFF-el; Cartan → kar-TAHN; Kretschmann → KRETCH-mahn; Schwarzschild → SHVARTS-shilt; Kundt → KOONT; Riemann → REE-mahn

**Voice notes:** Say "distance rule" and "painted grid" at entry; switch to "metric" and "coordinates" at the working rung and say once that they name the same things.

## History

- **Ferdinand Minding (1839).** Asked how to decide whether two curved surfaces can be bent onto each other without stretching, and showed that surfaces of the same constant curvature can be, locally. Ferdinand Minding (1839), *Wie sich entscheiden lässt, ob zwei gegebene krumme Flächen auf einander abwickelbar sind oder nicht; nebst Bemerkungen über die Flächen von unveränderlichem Krümmungsmaaße*, Journal für die reine und angewandte Mathematik 19, 370–387, doi:10.1515/crll.1839.19.370
- **Elwin Bruno Christoffel (1869).** Treated the equivalence problem for quadratic differential forms in any number of variables, introducing the symbols now named after him and a differentiation process, later developed into covariant differentiation, that builds the curvature conditions. Elwin Bruno Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46–70, doi:10.1515/crll.1869.70.46
- **Carl H. Brans (1965).** Adapted Cartan's method of equivalence to the metrics of general relativity, giving an invariant description of spacetime geometries. Carl H. Brans (1965), *Invariant approach to the geometry of spaces in general relativity*, Journal of Mathematical Physics 6, 94–102, doi:10.1063/1.1704268
- **Anders Karlhede (1980).** Turned the solution into a practical procedure that fixes frames step by step, bounds the derivative order needed, and yields the dimensions of the isometry and isotropy groups along the way. Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861

## Research horizon

- **Practical invariant classification.** Karlhede's frame-fixing procedure, implemented in computer algebra, classifies exact solutions and detects duplicates. Its bound of seven covariant derivatives in four dimensions is sharp, attained by type N null radiation on an anti-de Sitter background. Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861; Robert Milson, Nicos Pelavas (2008), *The type N Karlhede bound is sharp*, Classical and Quantum Gravity 25, 012001, doi:10.1088/0264-9381/25/1/012001; Malcolm A. H. MacCallum (2018), *Computer algebra in gravity research*, Living Reviews in Relativity 21, 6, doi:10.1007/s41114-018-0015-6
- **When scalar invariants suffice.** All four-dimensional spacetimes with vanishing scalar curvature invariants are Kundt, including the pp-waves. More generally, a four-dimensional Lorentzian metric not characterized locally by its scalar polynomial invariants must be degenerate Kundt, so scalar invariants suffice outside that class. Vojtěch Pravda, Alena Pravdová, Alan Coley, Robert Milson (2002), *All spacetimes with vanishing curvature invariants*, Classical and Quantum Gravity 19, 6213–6236, doi:10.1088/0264-9381/19/23/318; Alan Coley, Sigbjørn Hervik, Nicos Pelavas (2009), *Spacetimes characterized by their scalar curvature invariants*, Classical and Quantum Gravity 26, 025013, doi:10.1088/0264-9381/26/2/025013
- **Invariant detection of horizons and of Kerr.** Coordinate-free constructions locate geometric features in spacetimes computed with arbitrary coordinates. Scalars built from gradients of curvature invariants vanish on stationary horizons, and the vanishing of a spacetime version of the Simon tensor, with mild further conditions, characterizes the Kerr metric among stationary, asymptotically flat vacuum spacetimes. Don N. Page, Andrey A. Shoom (2015), *Local Invariants Vanishing on Stationary Horizons: A Diagnostic for Locating Black Holes*, Physical Review Letters 114, 141102, doi:10.1103/PhysRevLett.114.141102; Marc Mars (1999), *A spacetime characterization of the Kerr metric*, Classical and Quantum Gravity 16, 2507–2523, doi:10.1088/0264-9381/16/7/323

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** Two kids paint different grids on the same playground: one is squares, the other is rings around a flagpole with spokes. They each write down how far apart the spots are, and the rules look totally different, because Ben's steps get bigger far from the pole. But it's the same playground, so the difference is only in the paint. Deciding if two rules are the same surface is the equivalence problem, though I don't see why it's a problem when you can just look at the playground. Then there's the arrow test: carry an arrow around a loop without letting it swing. On flat ground it comes back the same, on a ball it comes back turned, so if Ana's rule never turns it and Carl's does, they're different surfaces. But who walks, if all I have is Carl's written rule? What are the 'labels' the walker never reads? And why does an egg turn the arrow more at its pointy end? Also one matching spot isn't enough, but I'm not sure what counts as enough.

Second independent reading, of revision 4, before any fix: Ana and Ben paint different grids on one flat playground, squares for Ana and rings with spokes round a flagpole for Ben. Each writes down how far apart neighbouring crossings are, and the two rules look nothing alike, because a step along one of Ben's rings covers more the farther out the ring is. It is still one playground, so the difference is only paint. Deciding whether two rules describe the same surface is the equivalence problem, although the summary makes that sound like something I could settle by walking over and looking. Then Carl hands me a rule for a surface I cannot visit, and I imagine a walker pressing a cardboard arrow to the surface and carrying it round a loop without letting it swing. On the flat playground it comes back matching its start; on a ball it comes back turned. If one rule gives a turn somewhere and the other gives that turn nowhere, the surfaces differ. One matching spot is not enough, because an egg turns the arrow more at its pointed end than at its middle. What I snagged on: 'spot' meant a crossing of painted lines in the first way but any place on the egg in the second; 'marks', 'ground' and 'shape' turn up as extra words for things that already have words; when the second way opens I am told about 'a third friend' and 'Ana' although its recap never introduces Ana or Ben; and 'A step along a spoke' never says it is Ben's.

**Stumbles (34)**

- “Each friend writes down how far apart neighbouring spots on their grid are.”: 'Spot' is never defined, and 'labels', used throughout the second way, the summary and the takeaway, is never introduced at all.
- “On the ring 5 metres from the pole, one degree covers about 9 centimetres.”: A step left implicit: the reader cannot see where 9 centimetres comes from, and 'one degree' switches from an angle between spokes to a length along a ring.
- “Ana's rule is the same everywhere: one step along a row covers one metre.”: Only rows are mentioned, and Ben's steps along spokes are never given, so the reader wonders whether columns and spokes behave differently.
- “Yet they describe the same flat ground.”: A claim with no reason given at the point it is made.
- “Deciding whether two distance rules describe the same surface is called the equivalence problem.”: A step left implicit: with the playground in view there is no problem to solve. The reader needs to hear that the problem is to decide from the written rules alone.
- “the same flat ground ... not in the ground ... describe the same surface ... describe the same shape”: Three words for one idea: 'ground', 'surface' and, in the tagline, 'shape'. 'Ground' also names the playground itself.
- “Draw rings and spokes on tracing paper, lay it over the sheet, and slide it to a new spot. The dots now sit on different rings and spokes, but the ruler reads the same distance.”: The try-it never has the reader write down any labels, so nothing visibly changes, and 'spot' is used for a position of the tracing paper as well as a grid crossing.
- “Ana's rule and Carl's rule look different. Do they describe the same surface?”: Carl appears with no introduction, and the reader does not know that his surface cannot be visited, which is the whole point of the way.
- “A walker measures with a real tape and a real arrow and never reads the paint.”: Who is the walker, when all you hold is a written rule? The link between the imagined walker and the written rule arrives only two paragraphs later.
- “A distance rule gives every length along the ground, and angles follow from the lengths of small triangles.”: Two surprising steps in one sentence with no reasons: how a rule for neighbouring spots gives every length, and how lengths give angles.
- “The arrow rule uses only lengths and angles along the ground.”: A claim the reader cannot check, presented as obvious.
- “An egg turns the arrow more at its pointed end than at its middle.”: A surprising claim with no reason.
- “So compare the results all over both surfaces.”: A rule the reader cannot follow ('compare all over' how?), and it hints that results matching everywhere would prove the surfaces the same, which the note never claims.
- “carry a cardboard arrow around a loop, a path that ends where it began, pressed against the ground, and never let it swing left or right.”: A sentence reread: the definition of loop and the 'pressed against' phrase interrupt the instruction.
- “Measurements on the ground, like the arrow test, ignore painted labels; so if one rule gives a result that the other rule gives nowhere, the two describe different surfaces.”: A 36-word takeaway that a reader cannot say back, and it leaves out the key link that the rule fixes the result.
- “Measurements made on the ground, like carrying an arrow around a loop, ignore the painted labels, so they can show that two rules describe different surfaces.”: Carrying an arrow around a loop measures nothing unless the arrow is kept from swinging, and the sentence runs past 32 words once that is added.
- “Could some new painted grid make the two rules describe the same surface?”: Ambiguous starting state: a new grid painted on which surface, and which rule changes?
- “while each ring has the same 360 steps. So each step there covers more ground.”: 'There' has no clear place to point to.
- “On a ball, loops of the same size turn the arrow by the same amount at every spot. On an egg, the pointed end turns the arrow more than the middle does.”: Both claims in the check answer are given without reasons, so the answer is not a chain of because-steps.
- “The results must match all over, spot for matching spot.”: 'Matching spot' is undefined, and the sentence suggests that matching everywhere would be enough.
- “Carrying an arrow around it turns the arrow by only about one seven-thousandth of a degree.”: The spoken answer drops the no-swing rule, so the number has no measurement behind it.
- “Deciding whether two distance rules describe the same surface is called the equivalence problem.”: Second reading, in the summary. The summary is the first thing the reader meets, and here the term is defined without the condition that makes it a problem. Standing next to a sentence about a playground you can walk on, it invites the answer 'just go and look'. The entry way was fixed for this at revision 2 and the summary was not.
- “Each place where two painted lines cross is a spot. ... One matching spot is not enough, though. ... Every spot on a ball is curved alike”: Second reading. One word in two senses. In 'Two grids on one playground' a spot is a crossing of two painted lines; in 'Measurements the labels cannot change', in the egg-and-ball check and in the misconception a spot is any place on a surface, where no grid need be painted at all. The first sense made me look for painted lines on the egg, which is the opposite of the point being made.
- “Ana's rule is the same everywhere: one step along a row or a column covers one metre. A step along a spoke covers one metre, but a step along a ring does not.”: Second reading. A step left implicit: the sentence switches from Ana's rule to Ben's with no signal, so I read the spoke sentence as Ana's and had to go back.
- “Yet a tape laid between two marks on the playground gives one reading, whichever grid labels the marks.”: Second reading. 'Mark' is a third word for a place, never introduced, and a label is defined as the name a grid gives a crossing of its lines, so marks in general cannot be labelled at all. With a spot now being any place, the sentence needs no new word.
- “Now a third friend, Carl, hands you a distance rule for a surface you cannot visit. Does it describe the same surface as Ana's rule for her flat playground?”: Second reading. The way is not self-sufficient: its recap never introduces Ana and Ben, so a reader who arrives here first meets 'a third friend' after no friends and 'Ana' with no Ana.
- “Use a measurement that ignores the labels. A walker with a real tape and a real arrow never reads the paint.”: Second reading. A rule the reader cannot follow: Carl's surface is one you cannot visit, so no measurement can be used on it, and the instruction contradicts the sentence two lines above it. The walker is imagined, and the text should say so.
- “Say one small loop on Carl's surface brings the arrow back turned”: Second reading. 'Say' does double duty. In a note whose entry rung is read aloud, and whose glossary explains what to say for terms, I first read it as an instruction to speak.
- “On tracing paper, draw rings around a centre and spokes out from it. Lay the tracing paper over the sheet and write down the nearest ring and spoke for each dot.”: Second reading. A rule I could not physically follow: unnumbered rings and spokes have no names, so there is nothing to write down, and the try-it turns on seeing the written labels change.
- “On a smooth egg and on a smooth ball, you find one spot each where small loops of the same size turn a cardboard arrow by the same amount.”: Second reading, in the egg-and-ball check. The starting state is incomplete: a loop turns nothing by itself, and the no-swing rule that makes the arrow test a measurement is dropped, exactly as it had been in the flat-town-map answer at revision 2.
- “What would a tape measure laid on the ground read for each friend?”: Second reading, in the hint of same-ground-different-rules. 'Ground' is the word revision 2 replaced everywhere with 'playground' and 'surface'; it survives here, and in the teaching arc, as an extra word for the same thing.
- “How could you check whether the two tables describe the same shape?”: Second reading, in the opening question the tutor speaks. 'Shape' is a fourth word for the surface, and revision 2 removed it everywhere else.
- “How much ground does one degree cover along the ring 10 metres from the pole? ... About 17 centimetres per degree, and 360 steps make the ring.”: Second reading, in the entry problem. 'Degree' and 'step' name one idea, and the problem uses both in one breath, while the entry way now says only that each step covers about 9 centimetres. A degree is also still the angle between two spokes, so the same word carries two meanings in the same sentence.
- “Deciding from two written distance rules alone whether they describe the same surface is called the equivalence problem.”: Second reading. A sentence I reread: 'from two written distance rules alone' sits between 'Deciding' and 'whether', so on the first pass 'Deciding from' looked like the verb phrase and I had to start again.

**Fixes**

- Introduced 'spot' and 'label' in the first way, with a glossary entry for label, so the second way, the summary and the takeaways use only defined words.
- Made the equivalence problem a real problem: the term is now defined as deciding from the written rules alone, and Carl's surface is one the reader cannot visit.
- Standardized 'surface' for the general idea and 'playground' for the flat scene, removing 'ground' and 'shape' across the tagline, summary, objectives, glossary, checks, misconceptions and the entry problem.
- Gave the 9-centimetre step its arithmetic (a 31-metre ring split into 360 steps, checked with python: 8.7 cm) and said that spoke steps cover one metre.
- Second way: built the chain that a distance rule settles the arrow test (lengths by adding steps, angles from three side lengths, the no-swing rule taken on trust), reasoned the egg claim through a smaller ball, and replaced 'compare all over' with the one-sided test the note actually supports. The recap now restates labels and the more-on-your-left rule the egg reasoning uses.
- Moved 'working it out takes more maths than school algebra' to simplifies as 'takes calculus', and dropped the 20-metre ring example and the sentence 'Ben's rule changes from place to place' to stay within the review allowance; the entry problem still works the 10-metre and 20-metre rings.
- Rewrote the tracing-paper try-it so the reader writes down labels and sees them change while the ruler reading stays 3 centimetres.
- Split the long summary sentence and shortened the second way's takeaway to one sayable sentence.
- Checks: fixed the starting state of turned-arrow-settles-it (Eli repaints his own surface), the dangling 'there' in same-ground-different-rules, and gave egg-and-ball because-steps.
- Ladder: the working way now links the Gaussian curvature to the arrow's turn per unit area around a small loop, and says Minding's theorem is taken on trust there.
- Bumped the revision to 2.
- Second reading, revision 5. Made 'spot' one word for one idea: it is now any place on a surface, and the grid gives a label to each spot where two of its lines cross. Added a glossary entry for spot. This also matches how neighbouring notes use the word.
- Second reading. Removed 'mark', 'ground' and 'shape' as further words for a place or a surface: the tape in the first entry way is now laid between two spots, the hint of same-ground-different-rules says playground, the opening question same-shape-from-tables says surface, and the teaching arc's first step says playground, and the if-stuck symptom 'features of the ground' now says 'features of the surface'.
- Second reading. Gave the summary the condition that makes the equivalence problem a problem: deciding 'when you cannot go and look'.
- Second reading. Named Ben as the owner of the spoke and ring steps, at no cost in words, and opened the second entry way's recap with the sentence that introduces Ana and Ben, so the way stands on its own.
- Second reading. Changed 'Use a measurement' to 'Imagine a measurement', because Carl's surface cannot be visited, and 'Say one small loop' to 'Suppose one small loop'.
- Second reading. Made the tracing-paper try-it doable by numbering the rings and the spokes before the labels are written down.
- Second reading. Restored the arrow test's no-swing rule in the egg-and-ball check by starting the question with the test itself.
- Second reading. Made the entry problem speak of steps rather than degrees throughout its statement, hint, answer, key points and the name of its numeric answer; the numbers are unchanged (a 63-metre ring split into 360 steps, about 17 centimetres each).
- Second reading. Budget: entry way explanations went from 438 to 439 words against the 440 review ceiling. To pay for the new sentence 'A spot is any place on a surface' I dropped the word 'single' from it and the second 'in' from 'not in the playground'; no sentence lost content, and nothing was cut. One recorded stumble, the garden path in the first way's closing sentence, was therefore left unfixed.
- Second reading. Bumped the revision to 5 and set the status back to novice-reviewed, because learner-visible text changed after the physics sign-off and a physics diff check over exactly those sentences is now owed.

**Concerns**

- Revision 5 changed learner-visible text after the physics review signed revision 4, so a physics diff check is owed over exactly the changed sentences: the summary, the first entry way's explanation and try_it, the second entry way's recap and explanation, the new glossary entry for spot, the checks same-ground-different-rules and egg-and-ball, the entry problem one-degree-steps, the opening question same-shape-from-tables, the first teaching-arc step and the sketch of two-grids-on-one-playground. None of them touches a number or an equation.
- Entry way explanations sit at 439 words against the advanced cap of 400 and the 440 review ceiling. There is room for one word. Any real addition to an entry way now needs something dropped, and the note should say which.
- The summary is four sentences; section 8 asks for two or three. Merging the last two would make a 33-word sentence, past the 32-word limit of the novice contract, so it was left at four.
- The entry problem keeps the idiom 'covers more ground' for distance covered, in the problem, the check and the visual sketch. That is not the surface sense of the word, which is now gone from learner text, but a later editor standardizing vocabulary should know the idiom was kept on purpose.
- The working way writes the surface invariant as $|\nabla K|^2 = g^{ab}\partial_aK\partial_bK$ and the formal way uses $a,b,c,d$ for orthonormal-frame indices. The conventions file fixes Greek $\mu,\nu$ for spacetime and Latin $i,j$ for space, and says nothing about indices on a two-dimensional surface or on a frame. Someone should add that row rather than leave each note to choose.
- Both visuals, two-grids-on-one-playground and curvature-fingerprint-curves, are still proposals with sketches only. The first sketch now says 'one step along a ring'; whoever builds it should also use spot, label, playground and surface exactly as this note does.
- The prerequisites still differ from the registry for gaussian-curvature, isometry, kretschmann-scalar and orthonormal-frame, and sync_registry.py has not been run.
- Four concepts this note leans on or opens onto have no note yet: diffeomorphism, isometry, orthonormal-frame and petrov-classification.

**Re-read** (2026-09-13, revision 4): 5 stumbles in 7 changed passages

- “An egg's pointed end is curved like a smaller ball, so a small loop there marks off a larger fraction of that ball. So it turns the arrow more than the same-size loop at the egg's middle.”: A step left implicit: 'a larger fraction' has no comparison, so the reader must supply that a smaller ball gives a larger fraction for the same loop. 'It' could be the loop or the pointed end, and two connectives ('so', 'So') chain back to back.
- “An egg's pointed end is curved like a smaller ball, so the same-size loop there marks off a larger fraction of that ball. So it turns the arrow more than at the egg's middle.”: The check answer has the same missing comparison for 'a larger fraction' and the same unclear 'it', so the because-chain has a gap.
- “A turn for loops of one size that one surface gives somewhere and the other gives nowhere shows that they differ.”: Sentence reread: 'for loops of one size' separates 'A turn' from its clause 'that one surface gives', so 'that' first seems to point at the loops.
- “such as the Gaussian curvature $K$ of a surface (the arrow's turn per unit area around a small loop in the arrow test, counted positive toward the walker's left when the small region lies on that side) or the Kretschmann scalar”: Sentence reread (working rung): a 28-word parenthetical with its own sign rule sits between two examples and the colon that leads to the equation, so the reader loses the main sentence.
- “its circumference divided by $2\pi$ when $\phi$ closes after $2\pi$”: 'Closes' is said of curves, not of a coordinate; a second-year reader pauses over what a coordinate closing means.
- Fix: Entry egg sentence: stated the rule that a smaller ball gives a larger fraction for a small loop, replaced 'it' with 'that loop', and removed the back-to-back connective. Same claim; entry explanation words unchanged at 439.
- Fix: Check egg-and-ball: same fix, so the answer's because-chain is complete.
- Fix: Misconception one-spot-is-enough: moved 'for loops of one size' to the front of the sentence so it no longer interrupts the relative clause.
- Fix: Working way 'The map as equations': moved the physics review's turn-per-area reading of $K$, with its sign rule word for word, out of the long scalar sentence into its own sentence at the start of the surfaces paragraph.
- Fix: Key equation spun-metric-curvature: 'when $\phi$ closes after $2\pi$' became 'when $\phi$ has period $2\pi$'.
- Fix: Read and left unchanged: the recap's small piece, walker's left and fraction rule (clear at entry, and it matches the egg reasoning), and the Schwarzschild rediscovery sentence.
- Fix: Bumped the revision to 4.

**Re-read** (2026-09-13, revision 7): 1 stumbles in 3 changed passages

- “Slide the tracing paper a few centimetres to a new position and do it again.”: Sentence reread: 'it' stands for an action, not a noun, and the sentence before it holds two actions (lay the tracing paper over the sheet, and write down the nearest ring and spoke for each dot). The slide already repeats the laying, so a reader doing the try-it has to guess which part to repeat. The added words 'a few centimetres' push the instruction further from what it points back to.
- Fix: Entry try-it of 'Two grids on one playground': replaced 'do it again' with the action it stands for, 'write down the nearest ring and spoke for each dot again', in the words the sentence before already uses. Same instruction, same slide of a few centimetres, same predicted result; nine words added, inside the way-fields budget (extras 544 of the 800 cap).
- Fix: Read and left unchanged: the numeric quantity of problem one-degree-steps, 'ground covered by one step along the ring 10 metres from the pole'. It repeats the phrase the problem statement already uses for that ring, so the reader meets no new wording, and it is the ring the solution works.
- Fix: No rule 17 stumble in this pass: neither changed string adds a second idea to its way, and neither was squeezed to fit a budget.
- Fix: Bumped the revision to 7, so a physics diff check of the one changed string is now owed.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Entry: the ring 5 m from the pole is about 31 m long, and one of 360 steps is about 9 cm; problem one-degree-steps gives 17.45 cm on the 10 m ring.: python: 2*pi*r/360. → 8.73 cm and 17.45 cm. Correct, and the tolerance is fine.
- Entry chain (novice rewrite): a distance rule gives lengths by adding small steps, angles from three side lengths, and the no-swing rule needs only lengths and angles.: Levi-Civita connection is fixed by the metric (Koszul formula); the angle at a point follows from the law of cosines for infinitesimal triangles. → Accepted as trust-worthy wording. Scoped 'a triangle' to 'a small triangle', since on a curved surface only small triangles give angles through school trigonometry.
- Entry egg claim: an egg's pointed end is curved like a smaller ball, so a same-size loop there turns the arrow more than at the middle.: python: Gaussian curvature of a revolved egg profile y = (B/2)sqrt((L^2-4x^2)/(L^2+8wx+4w^2)), L = 57 mm, B = 42 mm, w = 3 mm; also the prolate-ellipsoid limit K_tip = a^2/b^4 against K_equator = 1/a^2. → Pointed tip K = 6.1e-3 per mm^2, middle 1.18e-3, blunt tip 2.7e-3. The pointed end (an umbilic point) has about five times the middle's curvature. Correct for ordinary eggs. The reasoning now goes through the fraction of the smaller ball, matching the recap rule.
- Entry recap: 'the more of the ball lies on the walker's left, the bigger the turn'.: Area rule on a sphere: turn = A_left/a^2 modulo 2 pi; a small loop walked the other way has almost all the ball on the left and turns by 4 pi - A/a^2, which is a small turn to the right. → False for the walk-backwards what-if. Rewritten: a small loop marks off a small piece, the walker keeps that piece on her left, and the larger the fraction of the ball in that piece, the bigger the turn.
- Check egg-and-ball: a ball gives the same turn for same-size loops at every spot, so an egg whose turn varies has spots whose turn the ball gives nowhere.: Gauss-Bonnet on a sphere: the turn depends only on the enclosed area. Logic: if the egg's turn for one size takes more than one value, at least one value differs from the ball's single value. → Correct. Added the fraction step so the answer is a complete because-chain.
- Check turned-arrow-settles-it and entry way 2: a surface with a turning loop is not the same surface as one where every loop returns matching.: Holonomy is preserved by isometries. → Correct.
- Entry common question: a 100 square kilometre town on Earth turns the arrow about one seven-thousandth of a degree, and flat and ball distance rules agree better than a map shows.: python: A/R^2 with R = 6371 km; relative circumference defect rho^2/(6R^2) for an equal-area disc. → 1.41e-4 degrees = 1/7084 degree; defect 1.3e-7, about 1.3 mm over 10 km. Correct.
- Transformation law g_{mu nu} = (d xbar^a/d x^mu)(d xbar^b/d x^nu) gbar_{ab}, with n(n+1)/2 equations for n functions (3 for 2, 10 for 4).: Pullback of a symmetric tensor; counting. → Correct.
- Derivation curvature-of-a-spun-metric: Gamma^r_{phi phi} = -f f', Gamma^phi_{r phi} = f'/f, R^r_{phi r phi} = -f f'', K = -f''/f.: Re-derived by hand with the course Riemann definition (rho=r, sigma=phi, mu=r, nu=phi) and the course sectional curvature K = R_{r phi r phi}/(g_rr g_phiphi). → Correct in sign: f = sin r gives +1, f = r gives 0, and sinh r and e^r give -1.
- Symbol f(r) meaning 'circumference over 2 pi'.: The e^r (horocyclic) chart has phi not periodic. → Only true when phi closes after 2 pi. Reworded to length per unit phi, with the circumference as the periodic case.
- Gaussian curvature as the arrow's turn per unit area around a small loop.: Local Gauss-Bonnet with the conventions orientation row. → Correct only with a sense. Added 'counted positive toward the walker's left when the small region lies on that side'.
- Minding's theorem as stated in the working way: surfaces with the same constant K are locally isometric near any points.: Formal problem solution (Jacobi equation in geodesic polar coordinates). → Correct for smooth Riemannian surfaces.
- f = r^2: K = -2/r^2, |grad K|^2 = 16/r^6 = -2K^3; check same-curvature-values: at K = -1, 2 for r^4 and 2/3 for r^6, and the relation -(2/3)K^3.: Hand algebra and python. → Correct. Numeric values and 2 percent tolerances fine. The conclusion of no local equivalence is valid because dK is nonzero everywhere on both surfaces.
- Isotropic Schwarzschild form, areal radius rho(1+m/2rho)^2, map r = rho(1+m/2rho)^2, 1-2m/r = [(1-m/2rho)/(1+m/2rho)]^2, dr = (1+m/2rho)(1-m/2rho)drho, dr^2/(1-2m/r) = (1+m/2rho)^4 drho^2.: Hand algebra: r = rho + m + m^2/(4 rho); expanded (rho+m/2)^2 - 2 m rho = (rho - m/2)^2. → Correct term by term; rho > m/2 maps to r > 2m.
- Sun numbers: m = 1.477 km, r - rho = 1.477 km, Kretschmann 9.2e-46 per m^4 at r = 6.957e8 m.: python: GM_sun = 1.32712440018e20, c = 299792458; solved the quadratic for rho. → m = 1476.6 m; r - rho = m + m^2/(4 rho) = 1476.6 m; K = 9.23e-46. Correct.
- Kretschmann scalar 48 G^2 M^2/(c^4 r^6) is unchanged by the overall sign of the Riemann tensor and by g -> -g.: Counting metric factors: one lowered and three raised indices. → Correct. The notation trap's claims (Christoffels and R^rho_{sigma mu nu} unchanged, Ricci scalar flips) are also correct.
- Problem harmonic-radius-disguise: r = x + m reproduces the metric; Earth m = 4.435 mm.: Substitution; python with GM = 3.986e14. → Correct; x > m is r > 2m; the tolerance is fine.
- Problem two-hyperbolic-planes: X = y, Y = e^{-x} pulls back (dX^2+dY^2)/Y^2 to dx^2 + e^{2x}dy^2, a global bijection onto Y > 0, K = -1.: Hand computation. → Correct.
- Orthonormal frame bundle dimension N = n(n+1)/2 = 10; structure equations d theta = -omega^theta, d omega = -omega^omega + (1/2) R theta^theta.: With omega^a_b(X) = theta^a(nabla_X e_b) and the course convention [nabla_mu, nabla_nu]V = R V, Omega^a_b(X,Y) = theta^a(R(X,Y)e_b) = R^a_{bcd}X^cY^d. → Consistent with the course Riemann sign. The connection-form convention itself is still not fixed in the conventions file.
- Stopping argument and bound: ranks strictly increase from t_0 >= 1 until they stall, so order at most N suffices.: t_q >= q+1 before stalling and t_q <= N give q+1 <= N; t_0 = 0 means frame-independent components, which means constant curvature. → Correct.
- Cartan's theorem statement: only the order-(q+1) components were required to be the same functions of the independent invariants.: Compared with the classifying-manifold formulation. The set S has dimension 2N - t_q only if the classifying manifolds of order q+1 coincide near the common point, and those include the dependent components of lower order. → Incomplete. Changed to 'all components up to order q+1 are the same functions'. The Frobenius sketch (rank N - t_q, integral manifold of dimension N) is then correct.
- Plane wave -2du dv + (x^2-y^2)a(u)du^2 + dx^2 + dy^2 is vacuum with R_uxux = -a(u), and its scalar invariants vanish.: Hand Christoffels: Gamma^x_uu = -(1/2) d_x H, Gamma^x_xu = Gamma^u_xu = 0, so R^x_{uxu} = -(1/2) d_x^2 H = -a; the flat Laplacian of H vanishes, so R_uu = 0. The boost-weight argument uses the negative boost weights of all nabla^k R (VSI). → Correct.
- Compactness argument: O(n) orbits are closed and separated by invariant polynomials; for a noncompact Lorentz group zero is in the closure of the null orbit.: Standard invariant theory for compact groups on real representations. → Correct.
- Torus and plane: locally isometric, globally not (area L^2, closed geodesics of length L).: Direct. → Correct.
- Kundt claim check: in vacuum Schwarzschild every shear-free null geodesic congruence is a repeated principal null direction and expands, so it is not Kundt.: Goldberg-Sachs theorem; radial null expansion 2/r. → Correct.
- Research way: Karlhede stops when t and s both stall; isometry group dimension 4 - t_q + s_q; bound of seven derivatives first established by Karlhede, shown sharp by Milson and Pelavas with type N null radiation on an anti-de Sitter background.: Abstract of Milson-Pelavas (arXiv 0710.0688). → Confirmed by that abstract.
- Research way: all spacetimes with vanishing scalar invariants are Kundt (including pp-waves); a metric not locally characterized by scalar invariants is degenerate Kundt; Page-Shoom wedge-product invariants vanish on stationary horizons; Mars characterizes Kerr by the spacetime Simon tensor.: Abstracts on arXiv, ADS and IOP. → Confirmed. Page-Shoom use n gradients with n the local cohomogeneity; Mars's result is local isometry to Kerr for stationary asymptotically flat vacuum spacetimes.
- Reference Minding 1839, Crelle 19, 370-387, doi 10.1515/crll.1839.19.370.: De Gruyter record and EUDML. → Confirmed; verified.
- Reference Christoffel 1869, Crelle 70, 46-70, doi 10.1515/crll.1869.70.46.: De Gruyter record. → Confirmed; verified. Contribution rescoped: he introduced the differentiation process that was later developed into covariant differentiation, not covariant differentiation itself.
- Reference Brans 1965, J. Math. Phys. 6, 94.: Crossref and the journal's 1965 table of contents. → Confirmed, pages 94-102; added doi 10.1063/1.1704268; verified.
- Reference Karlhede 1980, GRG 12, 693-707, doi 10.1007/BF00771861.: Springer record. → Confirmed; verified.
- Reference Milson and Pelavas, CQG 25, 012001, arXiv 0710.0688.: Wikidata and arXiv. → Confirmed; published online December 2007 in the 2008 volume; added doi 10.1088/0264-9381/25/1/012001; verified.
- Reference MacCallum 2018, Living Rev. Relativ. 21, 6, doi 10.1007/s41114-018-0015-6.: PubMed and Springer listings. → Confirmed; verified.
- Reference Pravda, Pravdova, Coley, Milson 2002, CQG 19, 6213-6236, doi 10.1088/0264-9381/19/23/318, gr-qc/0209024.: arXiv abstract page and IOP. → Confirmed; verified.
- Reference Coley, Hervik, Pelavas 2009, CQG 26, 025013, doi 10.1088/0264-9381/26/2/025013, arXiv 0901.0791.: Crossref and arXiv. → Confirmed; verified.
- Reference Page and Shoom 2015, PRL 114, 141102, doi 10.1103/PhysRevLett.114.141102, arXiv 1501.03510.: ADS and APS. → Confirmed; verified.
- Reference Mars 1999, CQG 16, 2507-2523, doi 10.1088/0264-9381/16/7/323, gr-qc/9904070.: arXiv abstract page and IOP. → Confirmed; verified.
- History claim: 'the Schwarzschild spacetime has been published as new more than once'.: No specific primary record located to scope it. → Replaced with the general, well-documented statement that known solutions have been rediscovered and published as new.
- Second pass (revision 5 to 6), entry ring arithmetic after the novice rewording from 'degree' to 'step': a ring 5 m from the pole is about 31 m and one of its 360 steps about 9 cm; the entry problem's ring 10 m from the pole is about 63 m with steps of 17.45 cm.: python, recomputed from scratch: 2 pi r and 2 pi r/360 for r = 5, 10 and 20 m. → 31.42 m and 8.73 cm; 62.83 m and 17.45 cm; the 20 m ring gives 34.91 cm. Every number survives the rewording, and the 5 per cent tolerance on 17.45 cm holds.
- Second pass: the novice rewrite 'Ben's step along a spoke covers one metre, but his step along a ring does not' attributes the spoke step correctly and keeps it true.: Polar distance rule dr^2 + r^2 dphi^2 with rings 1 m apart and spokes 1 degree apart: a spoke step is exactly 1 m at every ring, a ring step is r pi/180. → Correct. Ana's rows and columns are the pair that both give one metre, and the sentence no longer lets a reader read the spoke step as hers.
- Second pass: entry try-it prediction 'You should find new labels for the dots' after sliding the tracing paper.: Polar labels of a fixed dot under a translation of the grid centre by s: the ring label changes only if the distance to the centre moves by more than the ring gap, and the spoke label only if the angle moves by more than one degree, which for a dot 5 cm out means a sideways shift above about 0.9 mm. → False as written for an arbitrarily small slide. Fixed by giving the slide a size: 'a few centimetres'. At that size a generic slide changes both labels, and any slide direction changes at least one.
- Second pass: the numeric answer of problem one-degree-steps, 17.45 cm with 5 per cent tolerance, is attached to an unambiguous quantity.: Read the numeric field against the problem's own solution, which also works the ring 20 m from the pole. → The quantity named only 'one step along the ring', while the solution's 20 m ring gives 34.91 cm. The quantity now names the ring 10 metres from the pole. Value and tolerance unchanged and correct.
- Second pass, re-derivation of the spun-metric curvature independently of the first pass: Gamma^r_{phiphi} = -f f', Gamma^phi_{rphi} = f'/f, R^r_{phi r phi} = -f f'', K = -f''/f.: Hand computation from the course Christoffel and Riemann definitions, then the course sectional-curvature row K = R_{r phi r phi}/(g_rr g_phiphi - g_rphi^2). → Same result and sign: f = r gives 0, f = sin r gives +1 (a sphere, matching the course R = +2/a^2), f = sinh r and f = e^r give -1.
- Second pass: check same-curvature-values, |grad K|^2 at K = -1 for f = r^2 and f = r^3, and the invariant relations.: python: K = -f''/f gives -2/r^2 and -6/r^2; |grad K|^2 = (dK/dr)^2 with g^rr = 1. → 2.000 and 0.6667 at K = -1, with relations |grad K|^2 = -2K^3 and -(2/3)K^3. Matches the note; the 2 per cent tolerances are fine.
- Second pass: the isotropic Schwarzschild map r = rho(1 + m/2rho)^2 and the Sun numbers m = 1.477 km, r - rho = 1.477 km, Kretschmann 9.2e-46 per m^4 at r = 6.957e8 m.: Hand algebra for (rho + m/2)^2 - 2 m rho = (rho - m/2)^2 and dr/drho = 1 - m^2/4rho^2; python with GM_sun = 1.32712440018e20 and c = 299792458, solving the quadratic for rho. → m = 1476.63 m, r - rho = 1476.63 m, Kretschmann = 9.23e-46 per m^4. Correct to the quoted figures.
- Second pass: problem harmonic-radius-disguise, r = x + m and the Earth value 4.435 mm.: Substitution term by term; python with GM = 3.986e14 and c = 299792458. → 1 - 2m/r = (x - m)/(x + m), dr = dx, areal radius x + m; m = 4.435 mm. Correct, and x > m is r > 2m.
- Second pass: the vacuum plane wave -2 du dv + (x^2 - y^2) a(u) du^2 + dx^2 + dy^2 has R_uxux = -a(u) and is Ricci-flat.: Christoffels recomputed by hand from the course definition (Gamma^x_uu = -(1/2) d_x H, Gamma^v_ux = -(1/2) d_x H, Gamma^x_xu = Gamma^u_xu = 0), then R^x_{uxu} = d_x Gamma^x_uu = -(1/2) d_x^2 H. → R_{xuxu} = -a(u) and the flat Laplacian of H vanishes, so R_uu = 0. Confirms the formal way, the check plane-wave-scalars and the research way.
- Second pass: entry common question, a 100 square kilometre town on Earth turns the arrow about one seven-thousandth of a degree.: python: A/R^2 in radians with R = 6371 km. → 2.46e-6 rad = 1.41e-4 degrees = 1/7084 of a degree. Correct.
- Second pass: the entry egg claim, that a same-size loop turns the arrow more at the pointed end than at the middle.: python: prolate spheroid of half-length 28.5 mm and half-width 21 mm, K at the tip a^2/b^4 against 1/a^2 at the middle; turn = 2 pi (1 - cos theta) for a geodesic circle on a ball, at fixed geodesic radius and at fixed circumference. → Tip 4.18e-3 per mm^2 against 1.23e-3 at the middle, a factor 3.4, and the tip behaves like a ball of radius 15 mm against 28 mm. The fraction and the turn both grow as the ball shrinks under both readings of 'same size'. Correct.
- Second pass, references re-confirmed independently: Milson and Pelavas, CQG 25, 012001 (2008), arXiv 0710.0688; Coley, Hervik and Pelavas, CQG 26, 025013 (2009), arXiv 0901.0791; Mars, CQG 16, 2507-2523 (1999), doi 10.1088/0264-9381/16/7/323, gr-qc/9904070; Brans, J. Math. Phys. 6, 94 (1965).: Web search of the publisher, arXiv and Wikidata records. → All four confirmed with the authors, years, titles, venues and identifiers as written, including the type N null radiation on an anti-de Sitter background that makes the Karlhede bound of seven sharp. The remaining references were confirmed in the first pass and nothing about them changed.

**Counterexamples tried**

- Walk the loop backwards on a ball: broke the entry recap 'the more of the ball on the walker's left, the bigger the turn', since almost the whole ball on the left gives a small turn to the right. The recap is now scoped to the small piece kept on the walker's left.
- Paper cone as Carl's surface: a loop around the tip returns turned while Ana's playground never does, so the one-sided test correctly calls them different. Statements hold.
- Rolled paper tube (bent but flat): every loop returns matching, as on the playground. No entry sentence claims the arrow test tells them apart, and the working and formal rungs say local equivalence is not global (torus-and-plane). Holds.
- Flat Mobius band: a loop can return the arrow flipped, not 'matching'. Dana's surface in turned-arrow-settles-it has every loop matching by hypothesis, so the check is unaffected.
- Saddle surface: the arrow returns turned to the right; entry way 2 says only 'turned', so it holds.
- Egg whose ends are equally curved (a prolate ellipsoid): both tips still exceed the middle, so the egg claim survives; a nearly spherical egg makes the difference small but nonzero.
- Figure-eight loop with equal lobes: zero net turn even on a ball. Entry sentences speak of a small loop marking off a piece, which excludes self-crossing loops.
- Constant curvature (sinh r against e^r): matching invariants cannot fix corresponding points, and the note says so; Minding supplies the equivalence.
- Metrics whose K takes the same values (r^4 against r^6): values match but the relation between |grad K|^2 and K differs, so they are inequivalent. Confirms the relation test.
- Non-constant-rank points (for example where dK = 0 on a spun metric with a curvature extremum): Cartan's theorem needs constant ranks, stated in conditions and simplifies.
- Lorentzian vacuum plane wave: every scalar polynomial invariant vanishes yet it is curved. The formal and research rungs state the failure and its scope (degenerate Kundt).
- Different slicing or signature: g -> -g flips the Ricci scalar but not the Kretschmann scalar; covered by the notation trap.
- Second pass, tiny slide of the tracing paper: the try-it's predicted new labels fail when the slide is smaller than the gap between rings and than about one degree of angle. The slide now has a size, 'a few centimetres'.
- Second pass, slide straight sideways: a dot's distance from the centre then barely changes, so its ring label can survive, but its spoke label swings by many degrees. At a few centimetres every direction changes at least one label of each dot, so the try-it holds.
- Second pass, the ring 20 metres from the pole: the entry problem's own solution gives 34.9 cm per step there, which is why the numeric answer now names the ring 10 metres from the pole.
- Second pass, the egg's blunt end: both ends of an ovoid are more curved than its middle (blunt tip about 2.7e-3 against 1.18e-3 per mm^2), so a reader who tries the other end still finds a bigger turn than at the middle, and the entry claim, which names the pointed end, holds.
- Second pass, Ana's square grid slid instead of Ben's: a translated square grid also relabels every spot while the tape reading holds, so the try-it's conclusion does not depend on the grid being rings and spokes.

**Fixes**

- Entry recap of 'Measurements the labels cannot change': replaced 'the more of the ball lies on the walker's left, the bigger the turn' (false for a small loop walked the other way) with a small piece kept on the walker's left and 'the larger the fraction of the ball in that piece, the bigger the turn'.
- Entry explanation of the same way: 'a triangle's angles' became 'a small triangle's angles', and the egg sentence now says a small loop at the pointed end marks off a larger fraction of that smaller ball, matching the recap. The entry explanation word count is unchanged (439 of the 440 ceiling).
- Check egg-and-ball: added the fraction step between 'curved like a smaller ball' and 'turns the arrow more'.
- Misconception one-spot-is-enough: the test is now for loops of one size.
- Working way 'The map as equations': gave the Gaussian curvature's turn-per-area reading its sense (positive toward the walker's left with the small region on that side).
- Key equation spun-metric-curvature: f(r) is the length per unit phi, and equals the circumference over 2 pi only when phi closes after 2 pi (not true for the e^r chart).
- Working way 'Schwarzschild in disguise': replaced an unscoped history claim about the Schwarzschild spacetime with the general statement that known solutions have been rediscovered and published as new.
- Formal way: Cartan's theorem now requires all components up to order q+1 to be the same functions of the independent invariants, not only the order-(q+1) ones.
- History: Christoffel's contribution rescoped; Brans venue pages completed and doi added; Milson-Pelavas doi added; all references set verified after confirmation.
- Visual two-grids-on-one-playground (author fields): 'ground' replaced by 'surface' and 'playground', as the novice reviewer asked.
- Revision bumped to 3 because note_diff lists 7 changed learner-visible strings at the entry and working rungs.
- Second pass, revision 6. Entry try-it of 'Two grids on one playground': 'Slide the tracing paper to a new position' became 'Slide the tracing paper a few centimetres to a new position', because the promised new labels can fail for a slide smaller than the ring gap or than one degree of angle. Three words, in the way-fields budget, which has room.
- Second pass, revision 6. Problem one-degree-steps: the numeric answer's quantity now reads 'ground covered by one step along the ring 10 metres from the pole', because the problem's own solution works a 20-metre ring where one step covers 34.9 cm. The value 17.45 cm and its tolerance are unchanged.
- Second pass: every equation was re-derived and every number recomputed from scratch, and the references were re-confirmed. Nothing else needed changing; the 21 strings the novice re-read changed at revision 5 are entry wording only.

**Concerns**

- Conventions gaps still open: the connection one-form and structure-equation sign convention (the note's form is consistent with the course Riemann tensor, with omega^a_b(X) = theta^a(nabla_X e_b)), and null coordinates and boost weight, which the plane-wave and Kundt text uses informally.
- Registry prerequisites for gaussian-curvature, isometry, kretschmann-scalar and orthonormal-frame are not yet synced; notes for diffeomorphism, gaussian-curvature, isometry and orthonormal-frame do not exist yet.
- The entry explanations sit at 439 of the 440-word review ceiling, so any further entry change needs a cut.
- Observations remain empty; no honest measured connection was found, which is acceptable for this concept.
- The teaching arc move 'two-grids' still says 'flat ground' (tutor field), and the proposed visual's tour narration should use 'playground' and 'surface' when it is written.
- A novice re-read of the 7 changed strings is due; the recap now uses 'marks off' and 'fraction', which the reader should check.
- Second pass: the only accuracy changes are the two above, both entry strings, so a novice re-read of exactly those two is owed and review.novice will cover revision 5 until then.
- Conventions gap to fill in course-conventions.md, not invented here: the working way writes the surface invariant as |grad K|^2 = g^{ab} d_a K d_b K and the formal way uses a, b, c, d for orthonormal-frame indices, while the conventions file fixes only Greek mu, nu for spacetime and Latin i, j for space. Indices on a two-dimensional surface and on a frame need a row of their own.
- Entry way explanations still sit at 439 words against the advanced cap of 400 and the 440 review ceiling, so both fixes of this pass were placed outside the entry explanations.

**Diff check** (2026-09-13, revision 4)

- Entry way measurements-labels-cannot-change (re-read rewording): 'the smaller the ball, the larger the fraction a small loop marks off. So that loop turns the arrow more there than at the egg's middle.': The comparative holds one loop fixed while the ball varies, and 'that loop ... than at the egg's middle' carries the same-size condition the old 'same-size loop' stated. python: fixed-area loop, fraction A/(4 pi rho^2); fixed-circumference geodesic circle, area 2 pi rho^2 (1 - cos theta) with sin theta = C/(2 pi rho). Turn = 720 degrees times the fraction when the small piece is on the walker's left. The earlier egg curvature result was reused: pointed tip about five times the middle. → Fraction and turn grow as the ball shrinks under both readings of 'one size' (fixed area: 2.29, 14.3, 57.3 degrees for rho = 5, 2, 1; fixed circumference: 0.18, 1.14, 4.59 degrees). The claim matches the old one. What-if 'bigger loop at the middle' is excluded by 'that loop'. Accurate.
- Check egg-and-ball answer (re-read rewording): 'the smaller the ball, the larger the fraction a loop of one size marks off. So a loop at the pointed end turns the arrow more than the same-size loop at the egg's middle.': Same computation. The question fixes small loops of the same size, so the 'curved like a smaller ball' comparison applies. Logic chain rechecked: two turns on the egg mean at least one differs from the ball's single turn. → Accurate, and the because-chain is complete.
- Misconception one-spot-is-enough correction, reordered: 'For loops of one size, a turn that one surface gives somewhere and the other gives nowhere shows that they differ.': Holonomy is preserved by isometries, and an isometry maps a loop to a loop of the same length and area. The turn with the small piece on the walker's left does not depend on orientation, so a reflection gives no way out. Compared with the old ordering. → Same claim as before, with the same scope. Accurate.
- Working way the-map-as-equations: the turn-per-area reading of K, now its own sentence: 'In the arrow test, K is the arrow's turn per unit area around a small loop, counted positive toward the walker's left when the small region lies on that side.': Conventions orientation row (holonomy = integral of K dA for a region on the walker's left). python: geodesic circles on the unit sphere (turn/area = +1.000) and the hyperbolic plane (turn/area = -1.000) as the radius goes to 0. Consistency with the next sentences (f = sin r gives K = +1). → The wording, sign rule and small-loop scope are identical to the reviewed parenthetical. The sign agrees with the conventions and with K = -f''/f. Accurate.
- Key equation spun-metric-curvature, symbol f(r): 'its circumference divided by 2 pi when phi has period 2 pi'.: Length of the fixed-r curve over one period is the integral of f d phi = 2 pi f. Tried a cone (f = alpha r, period 2 pi) and the non-periodic e^r chart. → Same condition as 'closes after 2 pi'. Accurate.

**Diff check** (2026-09-13, revision 6)

- Revision 5 changed 21 learner-visible strings, all at the entry rung. Do any of them move a number, an equation or a physical claim?: note_diff.py between the revision 4 snapshot and revision 5, read string by string against the first pass's verification list. → None does. The changes are: one word per idea ('spot' for any place, 'playground' and 'surface' in place of 'ground', 'mark' and 'shape'), 'step' in place of 'degree' in the entry problem, 'Imagine' and 'Suppose' in place of 'Use' and 'Say', Ben named as the owner of the spoke and ring steps, the recap opened with Ana and Ben, the arrow test restored in the egg-and-ball question, numbered rings and spokes in the try-it, and 'when you cannot go and look' added to the summary.
- Glossary 'spot': 'Any place on a surface. A painted grid gives a label to each spot where two of its lines cross.': Checked the new sense against every use of the word: the two entry ways, the summary, the distance-rule and label glossary entries, the checks same-ground-different-rules and egg-and-ball, and the misconception one-spot-is-enough. → Consistent everywhere, and it is the sense the egg and ball need, where no grid is painted. The distance rule is still stated for neighbouring spots on a painted grid, which are its crossings, so nothing claims a rule for unlabelled places.
- Entry problem one-degree-steps, reworded from 'one degree' to 'one step': statement, hint, answer, key point and numeric quantity.: python: 2 pi times 10 m is 62.83 m, split into 360 steps by spokes one degree apart. → 17.45 cm per step, 360 steps to the ring. The rewording removes the double duty of 'degree' (an angle between spokes and a length along a ring) without touching a number. The hint 'The spokes are one degree apart, so every ring is split into 360 steps' is correct.
- Summary: 'Deciding whether two written distance rules describe the same surface, when you cannot go and look, is called the equivalence problem.': Compared with the standard statement of the equivalence problem for metrics and with the first entry way's definition. → Accurate and better scoped than the old sentence: the problem is exactly to decide from the written rules, and the added condition does not narrow the term wrongly, since a reader who can go and look is doing something else.
- Check egg-and-ball question: 'you do the arrow test around small loops of the same size. You find one spot on each where the arrow comes back turned by the same amount.': Read against the glossary's arrow test (no swinging) and against the answer's because-chain; python for the turn of a geodesic circle at fixed area and at fixed circumference on balls of different radius. → Accurate. The no-swing rule is back, so the turn is a real measurement, and the posited matching spot is possible whenever the ball's curvature lies in the egg's range. The answer's conclusion, that the egg then has spots whose turn the ball gives nowhere, needs only that the egg's turn is not constant, which is true for an egg.
- Entry way 2 recap, now opened with 'Ana and Ben painted different grids on one flat playground, and each wrote down a distance rule', and entry way 2's 'Imagine a measurement' and 'Suppose one small loop'.: Checked that the recap states only what the first way establishes, and that the hedged verbs still support the argument that follows. → Accurate. The argument never needs a measurement actually performed on Carl's surface: the distance rule alone settles the arrow test, which is what the next paragraph says and what the metric determining the Levi-Civita connection guarantees.
- Entry way 1: 'Yet a tape laid between two spots on the playground gives one reading, whichever grid is painted', and 'The difference lies in the painted grids, not the playground.': Both grids chart one flat surface; the tape measures the induced distance, which is grid-independent. → Accurate, and the same claim in the check same-ground-different-rules and its key point now uses the same words.
- Teaching arc step two-grids, the if-stuck symptom labels-look-physical and the opening question same-shape-from-tables, reworded to 'playground' and 'surface'.: Read as tutor text against the note's vocabulary. → Accurate; the opening question now asks about the same object the note answers for.
- Fix: Entry try-it of 'Two grids on one playground': gave the slide a size, 'a few centimetres', so the promised new labels really appear.
- Fix: Problem one-degree-steps: the numeric answer's quantity now names the ring 10 metres from the pole, since the solution also works the 20-metre ring.
- Fix: Revision bumped to 6 and status set to physics-reviewed; a novice re-read of these two strings is owed.

**Diff check** (2026-09-13, revision 7)

- Scope: revision 7 changed exactly one learner-visible string, the entry try-it of 'Two grids on one playground': 'Slide the tracing paper a few centimetres to a new position and write down the nearest ring and spoke for each dot again.': note_diff.py between the pre-re-read snapshot and the current note, then the whole try-it read as one instruction sequence. → One entry string, an instruction. No number, unit, equation, condition, sense or frame moved.
- The rewrite claims exactly what 'do it again' claimed: the reader slides the tracing paper by the same few centimetres and reads off the nearest ring and spoke for each dot.: Compared the two sentences word by word against the sentence they point back to ('Lay the tracing paper over the sheet and write down the nearest ring and spoke for each dot'), and checked that the sliding keeps the paper over the sheet, so no step of the earlier instruction is lost. → Same action, same slide size, same predicted result. Accurate, and the instruction is doable as written.
- A slide of a few centimetres really does give new labels, as the next sentence promises, for dots 3 centimetres apart.: python: for ring spacings 0.5, 1, 1.5 and 2 cm and 8, 12 or 36 spokes, 41424 random centre positions with random slides of 2 to 5 cm; recorded how often both dots kept both their ring label and their spoke label. → 64 of 41424 cases, 0.15 per cent, and only for the coarsest spokes with the centre far from both dots. The promised new labels appear for essentially every slide a reader would make. The remaining cases are self-correcting, since a reader who sees the same labels slides again; no clause was added for them.
- The try-it supports the way's point that the difference lies in the painted grid, not the surface.: A slide of the tracing paper is a translation, which is an isometry of the flat sheet, so it relabels the dots without changing any distance between them. → Correct: the ruler reading between the dots is unchanged at 3 centimetres, exactly as the try-it says.
- Numbers in the way and in the problem the way refers to are unchanged and still right.: python: 2*pi*5 = 31.42 m, one of 360 steps 8.73 cm; 2*pi*10 = 62.83 m, one step 17.45 cm. → 'about 31 metres' and 'about 9 centimetres' hold, and problem one-degree-steps keeps 17.45 cm with a 5 per cent tolerance on a 62.83 m ring. Nothing to fix.
