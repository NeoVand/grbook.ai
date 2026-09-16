---
type: "concept"
schema_version: 2
id: "einstein-space"
title: "Einstein space"
tagline: "A spacetime with one drift total everywhere, for every falling cabin"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["Einstein manifold", "Einstein metric"]
prerequisites: ["ricci-tensor", "contracted-bianchi-identity"]
leads_to: ["vacuum-einstein-equations", "de-sitter-spacetime", "ricci-flat-spacetime", "weyl-tensor"]
visuals: ["falling-ring-of-crumbs", "six-entry-curvature-table"]
---

# Einstein space

*A spacetime with one drift total everywhere, for every falling cabin*

`einstein-space` · curvature · advanced · physics-reviewed (revision 4)

**Needs:** [[ricci-tensor]] (entry) · [[contracted-bianchi-identity]] (formal)  
**Opens:** [[vacuum-einstein-equations]] · [[de-sitter-spacetime]] · [[ricci-flat-spacetime]] · [[weyl-tensor]]  
**Related:** [[space-of-constant-curvature]] · [[cosmological-constant]] · [[kretschmann-scalar]] · [[sectional-curvature]] · [[einstein-tensor]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[six-entry-curvature-table]]

> Let go of a small ball of crumbs at rest in a freely falling cabin. Near the Sun, tidal drift pulls the ball longer one way and narrower the other two ways. The three drifts add to a drift total. A spacetime is an Einstein space when that total is the same one number at every place, in every freely falling cabin, however the cabin moves. The empty space near the Sun is an Einstein space, with the number zero.

## You will be able to

**Entry**
- Explain what makes a spacetime an Einstein space using the drift total, and tell an example from a non-example. `objectives/explain-the-same-total-test` ← `checks/two-cabins-near-the-sun`, `checks/obeys-the-equation-so-einstein-space`, `problems/sun-and-earth-surface-cabins`
- Distinguish a drift total that is the same everywhere from drifts that are equally strong everywhere. `objectives/distinguish-same-total-from-same-curving` ← `checks/two-cabins-near-the-sun`, `problems/sun-and-earth-surface-cabins`

**Working**
- Compute the Ricci scalar and Einstein tensor of an Einstein space, and identify the constant with the cosmological constant in four dimensions. `objectives/compute-traces-and-identify-lambda` ← `checks/schwarzschild-is-an-einstein-space`
- Use the observer-independence of the tidal trace to decide whether a given spacetime is an Einstein space. `objectives/decide-with-the-observer-test` ← `checks/comoving-observers-agree`, `problems/moving-through-a-dust-universe`

**Formal**
- Prove from the contracted Bianchi identity that the Einstein constant is constant in three or more dimensions, and state what happens in two. `objectives/prove-the-constant-is-constant` ← `checks/every-surface-looks-einstein`, `problems/same-total-for-every-observer-means-einstein`
- Decide whether a given Einstein metric has constant curvature, using the Weyl remainder and product examples. `objectives/separate-einstein-from-constant-curvature` ← `checks/product-of-two-spheres`

**Research**
- State the Hitchin–Thorpe inequality and use it to rule out Einstein metrics on a compact four-manifold. `objectives/use-the-hitchin-thorpe-obstruction` ← `checks/hitchin-thorpe-obstruction`

## Ways in

### 1. One drift total, everywhere and for everyone · entry · picture

*What is special about a spacetime in which a falling ball of crumbs gives the same drift total at every place, in every cabin?*

**Recap:** Let go of a small ball of crumbs at rest in a cabin that falls freely. Tidal drift pulls the ball longer along the line toward a planet's centre and narrower across it. Count a drift away from the centre crumb as plus and a drift toward it as minus. In empty space the drift apart along the line is twice as big as each drift together across it, so the three drifts add to zero. The Ricci tensor holds that total, and the total says whether the room the ball takes up starts to change.

Picture a cabin falling freely, without spinning, through empty space near the Sun. Inside, someone lets go of a small ball of crumbs, at rest. Tidal drift pulls the ball longer along the line toward the Sun, and narrower across it. Pick three directions at right angles to each other: the line toward the Sun and two across it. Take one crumb along each and add their three drifts. Count a drift away from the centre crumb as plus and a drift toward it as minus. The drift apart along the line is twice as big as each drift together across it. So one plus cancels two minuses, the three add to zero, and the room the ball takes up does not start to change. Call this sum the drift total.

Repeat the test at other places near the Sun, and in cabins passing those same places at any speed. The total is zero every time, because only matter among the crumbs could change it, and the Sun's matter is outside the ball.

A spacetime is called an Einstein space when the drift total is the same one number at every place, in every freely falling cabin, however the cabin moves. The empty space near the Sun is an Einstein space with the number zero.

A universe holding nothing but dark energy is an Einstein space with a number above zero. Dark energy is whatever makes distant galaxies rush apart faster and faster. There, a ball of crumbs let go at rest starts to grow at the same tiny rate at every place; drifts apart count as plus, so the number is above zero. Growing by one tenth in the room it takes up takes about four and a half billion years, too slow for any lab to notice.

**Takeaway:** A spacetime is an Einstein space when the drift total of a falling ball of crumbs is the same one number everywhere, in every freely falling cabin, however the cabin moves.

*What this leaves out:* The number zero for the space near the Sun leaves out dark energy's tiny share. Counting it, the number is dark energy's own, the same as far from the Sun.

*Builds on:* [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/two-cabins-near-the-sun`, `observations/measured-cosmological-constant`

### 2. Same total is not same curving · entry · contrast

*If the drift total is the same everywhere, does the space curve the same everywhere?*

In "One drift total, everywhere and for everyone", every cabin near the Sun found a total of zero. Does the space near the Sun therefore curve the same everywhere? No. Move the cabin from Neptune's distance from the Sun to Mercury's. Neptune is about 78 times farther from the Sun than Mercury. Gravity's pull weakens by the square of the distance: twice as far, a quarter of the pull. A drift is the small difference between the pulls on two neighbouring crumbs, and it fades faster, by the cube: twice as far gives drifts eight times weaker. So the drifts grow by 78 times 78 times 78, nearly half a million times. Yet they still cancel: the drift apart along the line is still twice each drift together across it, so the total stays zero.

**Try it:** Try the cube with a calculator. Let the pull at distance 10 be 1 divided by 10 squared, and at distance 11 be 1 divided by 11 squared. Their difference, the drift between two crumbs one unit apart, is about 17 ten-thousandths. Now go twice as far out: 1 divided by 400 minus 1 divided by 441 is a bit over 2 ten-thousandths. Twice the distance made the drift about seven and a half times smaller, close to eight. Put the crumbs a tenth of a unit apart instead and the factor comes out at 7.9, closer still to eight.

**Takeaway:** An Einstein space has one drift total everywhere, but the drifts that add up to it can still be far stronger at one place than at another.

*Continues:* `ways_in/one-total-everywhere-for-everyone`<br>*Builds on:* [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `problems/sun-and-earth-surface-cabins`

### 3. One constant fixes every trace · working · calculation

*What does the Einstein condition fix, and what does its constant mean in four dimensions?*

The drift total of "One drift total, everywhere and for everyone", which counts drifts apart as positive, is $-R_{\mu\nu}u^\mu u^\nu$: minus the Ricci tensor contracted twice with the cabin's four-velocity, because the tidal trace $R_{\mu\nu}u^\mu u^\nu$ counts drifts together as positive. Asking for the same number at every event and for every $u$ is asking for

$$R_{\mu\nu} = \lambda\,g_{\mu\nu},$$

with $\lambda$ a constant; the formal rung shows that in three or more dimensions the constant is forced even if one asks only that the number be the same for every $u$ at each event, allowing it to differ between events. Since $g_{\mu\nu}u^\mu u^\nu = -c^2$, the tidal trace reads $-\lambda c^2$ for every observer, so the entry rung's drift total is $+\lambda c^2$, and the initial volume law of the Ricci tensor gives $d^2\delta V/d\tau^2 = \lambda c^2\,\delta V$ at the moment of release: a ball at rest starts to grow when $\lambda > 0$ and to shrink when $\lambda < 0$. Because $R_{\mu\nu}$ has units of inverse length squared, so does $\lambda$.

Tracing with $g^{\mu\nu}$ gives $R = n\lambda$ in $n$ dimensions, and the Einstein tensor becomes $G_{\mu\nu} = (1 - n/2)\,\lambda\, g_{\mu\nu}$. In four dimensions $G_{\mu\nu} = -\lambda g_{\mu\nu}$. The course field equation with nothing on the right, $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$, says $G_{\mu\nu} = -\Lambda g_{\mu\nu}$. So a four-dimensional Einstein spacetime is exactly a solution of the vacuum field equation with cosmological constant $\Lambda = \lambda$, and its Ricci scalar is $R = 4\Lambda$. With the measured $\Lambda \approx 1.1\times10^{-52}\ \mathrm{m^{-2}}$, $\lambda c^2 \approx 1\times10^{-35}\ \mathrm{s^{-2}}$, which sets the four and a half billion years of the entry rung.

Three examples. Outside a non-rotating star, with $\Lambda$ neglected, $R_{\mu\nu} = 0$: an Einstein space with $\lambda = 0$, although its Kretschmann scalar $48G^2M^2/c^4r^6$ shows that its curvature is nonzero and grows as $r^{-6}$ inward. A space of constant curvature $K$ has $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, so $R_{\mu\nu} = (n-1)K g_{\mu\nu}$: always an Einstein space, with $\lambda = 3K = \Lambda$ for de Sitter spacetime. And a star with a cosmological constant has $\lambda = \Lambda$ outside the star. The first and third show that the converse fails: the Einstein condition fixes the traces of the Riemann tensor and nothing else.

**Takeaway:** Ricci equal to lambda times the metric makes the tidal trace minus lambda c squared for every observer; in four dimensions it is the vacuum field equation with cosmological constant equal to lambda.

*Continues:* `ways_in/one-total-everywhere-for-everyone`<br>*Builds on:* [[ricci-tensor]], [[ricci-scalar]], [[four-velocity]]<br>*Visuals:* [[six-entry-curvature-table]]<br>*See:* `key_equations/einstein-condition`, `derivations/traces-of-the-einstein-condition`, `checks/schwarzschild-is-an-einstein-space`, `space-of-constant-curvature/key_equations/contracted-curvatures`

### 4. The gradiometer test · working · operational

*How could instruments decide whether a region of spacetime is an Einstein space?*

The trace $-\lambda c^2$ of "One constant fixes every trace" is something an instrument reads. A gravity gradiometer in a freely falling, non-spinning cabin measures the tidal matrix $E_{ij} = c^2 R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$, whose trace is $R_{\mu\nu}u^\mu u^\nu$. The test is then: fly gradiometers through the region along many paths and at many speeds, and read the trace each time. The region is an Einstein space exactly when every reading is the same number, and that number is $-\lambda c^2$. One family of cabins agreeing is not enough; the cabins rushing past them must agree too.

Above Earth the test has been run, if not under that name. At $255\ \mathrm{km}$ altitude, $r = 6626\ \mathrm{km}$, the gradient along the radius is $-2GM/r^3 = -2740\ \mathrm{E}$ and each horizontal gradient is $+1370\ \mathrm{E}$, where one eötvös is $10^{-9}\ \mathrm{s^{-2}}$. Once the satellite's own rotation is removed, the three add to zero within the instrument's noise of a few hundredths of an eötvös, on every orbit: $\lambda = 0$ as far as the instrument can tell. Dark energy would add $-\Lambda c^2 \approx -1\times10^{-26}\ \mathrm{E}$, more than twenty powers of ten below that noise, so near Earth the vacuum is an Einstein space with $\lambda$ indistinguishable from zero.

A universe filled with dust fails the test. Every cabin at rest in the dust reads $4\pi G\rho - \Lambda c^2$, but a cabin moving through the dust at speed $v$ reads $4\pi G\rho\,(2\gamma^2 - 1) - \Lambda c^2$, with $\gamma = (1 - v^2/c^2)^{-1/2}$, as worked out in "Moving through a dust universe". At $v = 0.6c$ the matter part is $2.125$ times larger. Readings that depend on the cabin's speed mean $R_{\mu\nu}$ is not a multiple of $g_{\mu\nu}$, and the dust universe is not an Einstein space, although it obeys Einstein's equation.

**Takeaway:** A region is an Einstein space exactly when every freely falling gradiometer, at every place and speed, reads the same tidal trace; near Earth that trace is zero within noise, while a dust universe fails because moving cabins read more.

*Continues:* `ways_in/one-constant-fixes-every-trace`<br>*Builds on:* [[ricci-tensor]]<br>*See:* `observations/goce-trace-reads-zero`, `problems/moving-through-a-dust-universe`, `checks/comoving-observers-agree`

### 5. Definition, constancy, and the Weyl remainder · formal · structure

*What exactly is an Einstein metric, why is its constant constant, and how much curvature does the condition leave free?*

Set $G = c = 1$. Let $(M, g)$ be a connected smooth manifold of dimension $n \geq 2$ with a metric of any signature and its Levi-Civita connection. The metric is *Einstein* when $\mathrm{Ric} = \lambda g$ for a constant $\lambda$, the Einstein constant. Zero is allowed: Ricci-flat metrics are Einstein.

*Constancy.* Suppose only that $R_{\mu\nu} = f g_{\mu\nu}$ for a smooth function $f$. Then $R = nf$, and the contracted Bianchi identity $\nabla^\mu R_{\mu\nu} = \tfrac12\nabla_\nu R$ becomes $\partial_\nu f = \tfrac{n}{2}\partial_\nu f$, so $(n - 2)\,\partial_\nu f = 0$. For $n \geq 3$, $f$ is constant on the connected $M$: the pointwise condition already implies the definition. The proof uses metric compatibility and vanishing torsion, which the contracted identity needs. For $n = 2$ every metric satisfies $R_{\mu\nu} = \tfrac12 R\,g_{\mu\nu}$, because the Riemann tensor has one independent component, so the pointwise condition is empty and the definition must demand a constant: an Einstein surface is one of constant Gaussian curvature $K = \lambda$.

*Vacuum with $\Lambda$ in $n$ dimensions.* Tracing $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$ gives $(1 - n/2)R + n\Lambda = 0$, so $R = 2n\Lambda/(n-2)$ and $\lambda = 2\Lambda/(n-2)$; for $n = 4$, $\lambda = \Lambda$.

*What the condition leaves free.* The Ricci decomposition of the Riemann tensor, with $S_{\mu\nu} = R_{\mu\nu} - (R/n)g_{\mu\nu}$ its traceless Ricci part, reads $R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \tfrac{1}{n-2}(g_{\rho\mu}S_{\sigma\nu} - g_{\rho\nu}S_{\sigma\mu} - g_{\sigma\mu}S_{\rho\nu} + g_{\sigma\nu}S_{\rho\mu}) + \tfrac{R}{n(n-1)}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ for $n \geq 3$. Einstein means $S = 0$, so

$$R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \frac{\lambda}{n-1}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big).$$

An Einstein metric is therefore a constant-curvature part with $K = \lambda/(n-1)$ plus an arbitrary Weyl tensor, and it has constant curvature exactly when $C = 0$. In three dimensions $C \equiv 0$, so Einstein and constant curvature coincide there. In four or more they part: Schwarzschild and Kerr are Ricci-flat with nonzero Weyl tensor; the Nariai spacetime, the product of two-dimensional de Sitter space and a round two-sphere with equal curvature $\Lambda$, has $\lambda = \Lambda$ and mixed sectional curvatures zero; the Riemannian product of two round two-spheres of equal radius is Einstein for the same reason.

*Sectional reading.* For a unit vector $X$ and an orthonormal basis $e_i$ of $X^\perp$ in Riemannian signature, $\mathrm{Ric}(X,X) = \sum_i K(X, e_i)$. Einstein therefore means that the sectional curvatures of the $n - 1$ planes through any direction sum to the same $\lambda$, whatever the direction. In Lorentzian signature the analogous statement is that $\mathrm{Ric}(u,u)$ is the same for every unit timelike $u$, and that condition at a point is equivalent to $\mathrm{Ric} = \lambda g$ there, by the polarization argument of "Same total for every observer means Einstein".

**Takeaway:** An Einstein metric has Ricci equal to a constant times the metric; for n at least 3 the constant is forced, and the Riemann tensor is a constant-curvature part with K equal to lambda over n minus 1 plus a free Weyl tensor.

*Picture:* The Riemann tensor drawn as two boxes: a small fixed box labelled 'lambda over n minus 1 times g wedge g' that the Einstein condition fills, and a large empty box labelled 'Weyl' that it does not touch; in three dimensions the Weyl box is missing.

*What this leaves out:* The Ricci decomposition is quoted, not derived; its derivation belongs to the Weyl tensor.

*Continues:* `ways_in/one-constant-fixes-every-trace`<br>*Builds on:* [[contracted-bianchi-identity]], [[levi-civita-connection]], [[metric-compatibility]], [[riemann-curvature-tensor]], [[gaussian-curvature]]<br>*See:* `derivations/lambda-is-constant`, `derivations/weyl-remainder-of-an-einstein-space`, `checks/every-surface-looks-einstein`, `checks/product-of-two-spheres`, `problems/same-total-for-every-observer-means-einstein`

### 6. Critical points of the total scalar curvature · formal · bridge

*Why do Einstein metrics arise as the critical points of a natural functional, and what flow has them as fixed points?*

Set $G = c = 1$. The Weyl remainder of "Definition, constancy, and the Weyl remainder" says what an Einstein metric looks like; a variational principle says where such metrics come from. For metrics on a compact manifold without boundary, the variation of the total scalar curvature with a cosmological term is, stated here and derived with the Einstein–Hilbert action,

$$\delta\int_M (R - 2\Lambda)\sqrt{|g|}\,d^nx = \int_M \big(G_{\mu\nu} + \Lambda g_{\mu\nu}\big)\,\delta g^{\mu\nu}\sqrt{|g|}\,d^nx.$$

Critical points are the metrics with $G_{\mu\nu} = -\Lambda g_{\mu\nu}$, the Einstein metrics with $\lambda = 2\Lambda/(n-2)$. Read in Riemannian signature, $-2\Lambda$ is a Lagrange multiplier: Einstein metrics are the critical points of the total scalar curvature $\int_M R\,dV$ among metrics of fixed total volume, equivalently of the scale-invariant quotient $\int_M R\,dV / \mathrm{Vol}^{(n-2)/n}$. This is how Einstein metrics enter Riemannian geometry as the best metrics a manifold can carry, and how Hilbert obtained the vacuum field equations in 1915.

A second source is the Ricci flow $\partial_t g = -2\,\mathrm{Ric}(g)$. Because the Ricci tensor is unchanged by a constant rescaling of the metric, an Einstein metric evolves only by scaling, $g(t) = (1 - 2\lambda t)\,g_0$: it shrinks when $\lambda > 0$, is fixed when $\lambda = 0$, and expands when $\lambda < 0$. Einstein metrics are thus the fixed points of the flow modulo scale, and metrics that also move by diffeomorphisms, the Ricci solitons, are the next simplest. That is the sense in which the flow searches for Einstein metrics, and it is the bridge to the research rung.

**Takeaway:** Einstein metrics are the critical points of the total scalar curvature at fixed volume, with the cosmological constant as the Lagrange multiplier, and they are the fixed points of the Ricci flow up to scale.

*Picture:* A landscape whose height is the total scalar curvature over the space of unit-volume metrics; Einstein metrics sit at its critical points, and the Ricci flow is a path that pauses only there.

*What this leaves out:* The variation formula omits boundary terms, which vanish on a compact manifold without boundary; the Ricci flow is presented only through its action on Einstein metrics.

*Continues:* `ways_in/definition-constancy-and-the-weyl-remainder`<br>*Builds on:* [[ricci-scalar]], [[levi-civita-connection]]<br>*See:* `history/hilbert-1915`

### 7. Einstein metrics as a research field · research · structure

*Which manifolds carry Einstein metrics, how many, and which Einstein spacetimes are stable?*

The variational picture of "Critical points of the total scalar curvature" turns the definition into questions of existence, uniqueness and stability. Set $G = c = 1$.

*Obstructions in four dimensions.* On a compact oriented four-manifold the Gauss–Bonnet and signature formulas read $\chi = \tfrac{1}{8\pi^2}\int\big(|W|^2 - \tfrac12|S|^2 + \tfrac{1}{24}R^2\big)dV$ and $\tau = \tfrac{1}{12\pi^2}\int\big(|W^+|^2 - |W^-|^2\big)dV$, with $S$ the traceless Ricci tensor and $W^\pm$ the self-dual and anti-self-dual Weyl parts. An Einstein metric has $S = 0$, so $\chi \geq \tfrac{1}{8\pi^2}\int(|W^+|^2 + |W^-|^2)\,dV \geq \tfrac{3}{2}|\tau|$: the Hitchin–Thorpe inequality. Equality forces $R = 0$ and one of $W^\pm$ to vanish, which Hitchin showed happens only for flat manifolds and quotients of a K3 surface with its Ricci-flat Kähler metric. Whether the four-sphere carries any Einstein metric besides the round one is open.

*Kähler–Einstein metrics.* On a compact Kähler manifold the Ricci form represents $2\pi c_1$, so the sign of $\lambda$ is fixed by the first Chern class. Yau's proof of the Calabi conjecture gives a Ricci-flat Kähler metric in every Kähler class when $c_1 = 0$, the Calabi–Yau metrics, and with Aubin a unique Kähler–Einstein metric with $\lambda < 0$ when $c_1 < 0$. When $c_1 > 0$ obstructions appear, and existence is equivalent to the algebro-geometric condition of K-stability, proved by Chen, Donaldson and Sun and by Tian.

*Flows and solitons.* The Ricci flow deforms a metric toward Einstein metrics in favourable cases, as Hamilton showed for three-manifolds of positive Ricci curvature, and its singularity models are Ricci solitons; Perelman's monotone entropy made the flow the tool that proved geometrization.

*Lorentzian Einstein metrics.* The four-dimensional Einstein spacetimes are the $\Lambda$-vacua. With $\lambda > 0$ the questions are dynamical: de Sitter space is nonlinearly stable, as Friedrich proved, and so is the slowly rotating Kerr–de Sitter family, as Hintz and Vasy proved, so small perturbations of these Einstein spacetimes settle back to them. With $\lambda < 0$, Einstein metrics that are conformally compact with a prescribed conformal infinity, constructed by Graham and Lee near the hyperbolic metric, are the bulk geometries of holography: the boundary conformal structure and the metric's asymptotic expansion encode a conformal field theory's sources and expectation values. Uniqueness of such fillings, and existence for a general boundary, remain open.

**Takeaway:** Einstein metrics are the subject of existence theorems, topological obstructions such as Hitchin–Thorpe, the Kähler–Einstein and K-stability programme, Ricci-flow methods, and the stability and holography of Lambda-vacuum spacetimes.

*Picture:* A map with four regions: obstructions (four-manifolds), existence (Kähler geometry), flows (Ricci flow), and spacetimes (positive and negative Lambda), each with its landmark theorem and an open question at its edge.

*Continues:* `ways_in/critical-points-of-total-scalar-curvature`<br>*Builds on:* [[contracted-bianchi-identity]]<br>*See:* `checks/hitchin-thorpe-obstruction`, `research_horizon/kahler-einstein-metrics-and-k-stability`, `research_horizon/existence-and-obstruction-in-four-dimensions`, `research_horizon/stability-of-lambda-vacuum-spacetimes`, `research_horizon/negative-lambda-and-holography`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | — |
| tidal drift | — | The slow drift of neighbouring freely falling objects apart or together, because gravity pulls them slightly differently. | — |
| drift total | — | The three drifts of a small ball of crumbs let go at rest in a freely falling cabin that does not spin, along three directions at right angles, added up. A drift away from the centre crumb counts as plus and a drift toward it as minus. It says whether the room the ball takes up starts to change. | — |
| Ricci tensor | REE-chee tensor | A table kept at every place of a spacetime. For a small ball of crumbs let go at rest in any freely falling cabin, it gives the drift total. | [[ricci-tensor]] |
| spacetime | — | Space and time taken together, as one whole in which every event has both a place and a moment. | — |
| Einstein space | — | A spacetime in which the drift total is the same one number at every place, in every freely falling cabin, however the cabin moves. The number can be zero. | [[einstein-space]] |
| dark energy | — | Whatever makes distant galaxies rush apart faster and faster. A universe holding nothing else is an Einstein space with a number above zero. | — |
| void | — | A huge region of the universe with almost no galaxies or gas in it. | — |
| Einstein's equation | — | The law of gravity in general relativity. It ties the curving of spacetime at each place to the matter there. | [[einstein-field-equations]] |
| curving | — | The bending of space and time near a place, which shows up as tidal drift in a freely falling cabin. Stronger curving means stronger drifts. | — |

## Key equations

### Einstein condition · working

$$
R_{\mu\nu} = \lambda\,g_{\mu\nu},\qquad \lambda\ \text{constant}
$$

The Ricci tensor is one constant times the metric, in any dimension and signature, with zero allowed.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu}$ | Ricci tensor | the Ricci tensor |
| $\lambda$ | the Einstein constant, in units of inverse length squared | lambda |
| $g_{\mu\nu}$ | metric | the metric |

**Holds when:** Levi-Civita connection; $\lambda$ constant, automatic for $n \geq 3$ on a connected manifold.  
**Say it:** “The Ricci tensor equals lambda times the metric, with lambda a constant.”  
**Justified by:** `stated`

### Ricci scalar and Einstein tensor of an Einstein space · working

$$
R = n\lambda,\qquad G_{\mu\nu} = \Big(1 - \frac{n}{2}\Big)\lambda\,g_{\mu\nu}
$$

One constant fixes the Ricci scalar and the Einstein tensor; in four dimensions $G_{\mu\nu} = -\lambda g_{\mu\nu}$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R$ | Ricci scalar | the Ricci scalar |
| $n$ | dimension of the manifold | the dimension n |
| $G_{\mu\nu}$ | Einstein tensor $R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$ | the Einstein tensor |

**Holds when:** Einstein space of dimension $n$.  
**Say it:** “The Ricci scalar is n times lambda, and the Einstein tensor is one minus n over two, times lambda, times the metric.”  
**Justified by:** `derivations/traces-of-the-einstein-condition`

### Einstein spacetimes are the Lambda-vacua · working

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = 0 \;\Longleftrightarrow\; R_{\mu\nu} = \Lambda\,g_{\mu\nu},\qquad R = 4\Lambda \quad (n = 4)
$$

A four-dimensional spacetime is an Einstein space exactly when it solves the vacuum field equation with $\Lambda = \lambda$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Lambda$ | cosmological constant, about $1.1\times10^{-52}\ \mathrm{m^{-2}}$ | the cosmological constant, capital lambda |
| $G_{\mu\nu}$ | Einstein tensor | the Einstein tensor |

**Holds when:** Four dimensions, Lorentzian signature, no matter; in $n$ dimensions $\lambda = 2\Lambda/(n-2)$.  
**Say it:** “The vacuum field equation with a cosmological constant holds exactly when the Ricci tensor equals capital lambda times the metric, and then the Ricci scalar is four capital lambda.”  
**Justified by:** `derivations/traces-of-the-einstein-condition`

### Tidal trace and initial volume law in an Einstein space · working

$$
R_{\mu\nu}u^\mu u^\nu = -\lambda c^2,\qquad \left.\frac{d^2\,\delta V}{d\tau^2}\right|_{\tau = 0} = \lambda c^2\,\delta V
$$

Every freely falling observer measures the same tidal trace; a ball released at rest starts to grow when $\lambda > 0$ and to shrink when $\lambda < 0$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $u^\mu$ | observer's four-velocity, $u_\mu u^\mu = -c^2$ | the observer's four-velocity |
| $\delta V$ | volume of a small ball of freely falling particles released at rest | the ball's volume |

**Holds when:** Einstein space; the volume law holds at release, to first order in the ball's size.  
**Say it:** “The Ricci tensor contracted twice with any four-velocity is minus lambda c squared, and the second proper-time derivative of a released ball's volume is lambda c squared times the volume.”  
**Justified by:** `derivations/traces-of-the-einstein-condition`

### Constancy of the Einstein constant · formal

$$
R_{\mu\nu} = f\,g_{\mu\nu} \;\Longrightarrow\; (n - 2)\,\partial_\nu f = 0
$$

A Ricci tensor proportional to the metric has a constant factor in three or more dimensions; in two the factor is free.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $f$ | the pointwise proportionality function | the function f |
| $n$ | dimension | the dimension n |

**Holds when:** Levi-Civita connection on a connected manifold; $G = c = 1$.  
**Say it:** “If the Ricci tensor is f times the metric, then n minus two times the gradient of f vanishes.”  
**Justified by:** `derivations/lambda-is-constant`

### Weyl remainder of an Einstein metric · formal

$$
R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \frac{\lambda}{n-1}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big)
$$

An Einstein metric is a constant-curvature part with $K = \lambda/(n-1)$ plus a free Weyl tensor; it has constant curvature exactly when the Weyl tensor vanishes.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C_{\rho\sigma\mu\nu}$ | Weyl tensor, the traceless part of the Riemann tensor | the Weyl tensor |
| $\lambda/(n-1)$ | the sectional curvature the Einstein condition would give if the Weyl tensor vanished | lambda over n minus one |

**Holds when:** Einstein metric in dimension $n \geq 3$; $G = c = 1$.  
**Say it:** “The Riemann tensor equals the Weyl tensor plus lambda over n minus one, times the antisymmetrized product of two metrics.”  
**Justified by:** `derivations/weyl-remainder-of-an-einstein-space`

## Derivations

### Traces, the Einstein tensor, and the cosmological constant · working

**Goal:** From $R_{\mu\nu} = \lambda g_{\mu\nu}$ obtain $R$, $G_{\mu\nu}$, the tidal trace, and $\lambda = \Lambda$ in four dimensions.

1. Contract with the inverse metric: $R = g^{\mu\nu}R_{\mu\nu} = \lambda\,g^{\mu\nu}g_{\mu\nu} = \lambda\,\delta^\mu{}_\mu = n\lambda$.
2. Form the Einstein tensor: $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \lambda g_{\mu\nu} - \tfrac{n}{2}\lambda g_{\mu\nu} = (1 - n/2)\lambda\,g_{\mu\nu}$.
3. Set $n = 4$: $G_{\mu\nu} = -\lambda g_{\mu\nu}$.
4. The course field equation with $T_{\mu\nu} = 0$ is $G_{\mu\nu} = -\Lambda g_{\mu\nu}$. So an Einstein spacetime solves it with $\Lambda = \lambda$; conversely a solution has $R = 4\Lambda$ by tracing, hence $R_{\mu\nu} = G_{\mu\nu} + \tfrac12 R g_{\mu\nu} = \Lambda g_{\mu\nu}$.
5. In $n$ dimensions the comparison gives $(1 - n/2)\lambda = -\Lambda$, so $\lambda = 2\Lambda/(n-2)$.
6. Contract with a four-velocity, $g_{\mu\nu}u^\mu u^\nu = -c^2$: $R_{\mu\nu}u^\mu u^\nu = -\lambda c^2$ for every observer.
7. Insert this into the initial volume law $d^2\delta V/d\tau^2 = -R_{\mu\nu}u^\mu u^\nu\,\delta V$: $d^2\delta V/d\tau^2 = \lambda c^2\,\delta V$.

**Result:** $R = n\lambda$, $G_{\mu\nu} = (1 - n/2)\lambda g_{\mu\nu}$, $\lambda = \Lambda$ when $n = 4$, and every observer finds $R_{\mu\nu}u^\mu u^\nu = -\lambda c^2$, so a released ball obeys $d^2\delta V/d\tau^2 = \lambda c^2\,\delta V$.

### The Einstein constant is constant for n at least 3 · formal

**Goal:** Show that $R_{\mu\nu} = f g_{\mu\nu}$ with a smooth function $f$ forces $f$ to be constant on a connected manifold of dimension $n \geq 3$.

1. Trace the hypothesis: $R = g^{\mu\nu}R_{\mu\nu} = nf$.
2. The contracted Bianchi identity for the Levi-Civita connection reads $\nabla^\mu R_{\mu\nu} = \tfrac12\nabla_\nu R$.
3. Compute the left side with metric compatibility, $\nabla g = 0$: $\nabla^\mu(f g_{\mu\nu}) = g_{\mu\nu}\nabla^\mu f = \partial_\nu f$.
4. Compute the right side: $\tfrac12\nabla_\nu(nf) = \tfrac{n}{2}\partial_\nu f$.
5. Equate: $\partial_\nu f = \tfrac{n}{2}\partial_\nu f$, so $(1 - n/2)\partial_\nu f = 0$, equivalently $(n-2)\partial_\nu f = 0$.
6. For $n \neq 2$ the gradient of $f$ vanishes, so $f$ is constant on the connected $M$. For $n = 2$ the equation is empty, and indeed $f = K$ varies on an ellipsoid.

**Result:** $(n - 2)\,\partial_\nu f = 0$: for $n \geq 3$ a Ricci tensor proportional to the metric has a constant factor, and the pointwise condition already defines an Einstein metric.

### The Weyl remainder of an Einstein metric · formal

**Goal:** Show that an Einstein metric in dimension $n \geq 3$ has $R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \tfrac{\lambda}{n-1}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$.

1. Take as given the Ricci decomposition for $n \geq 3$: $R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \tfrac{1}{n-2}(g_{\rho\mu}S_{\sigma\nu} - g_{\rho\nu}S_{\sigma\mu} - g_{\sigma\mu}S_{\rho\nu} + g_{\sigma\nu}S_{\rho\mu}) + \tfrac{R}{n(n-1)}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, with $S_{\mu\nu} = R_{\mu\nu} - \tfrac{R}{n}g_{\mu\nu}$ traceless and $C$ totally traceless.
2. For an Einstein metric $R = n\lambda$, so $S_{\mu\nu} = 0$ and the middle group vanishes.
3. The last coefficient becomes $\tfrac{R}{n(n-1)} = \tfrac{n\lambda}{n(n-1)} = \tfrac{\lambda}{n-1}$.
4. Check by contracting on $\rho$ and $\mu$: $C$ is traceless and $\tfrac{\lambda}{n-1}(n - 1)g_{\sigma\nu} = \lambda g_{\sigma\nu}$, as required.
5. The second term is the Riemann tensor of constant curvature $K = \lambda/(n-1)$, so the metric has constant curvature exactly when $C = 0$; since $C \equiv 0$ for $n = 3$, every three-dimensional Einstein metric has constant curvature $\lambda/2$.

**Result:** $R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu} + \tfrac{\lambda}{n-1}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$: constant curvature $\lambda/(n-1)$ plus a free Weyl tensor.

## Problems

### `sun-and-earth-surface-cabins` · entry · difficulty 2 · conceptual

Two friends compare the empty space just above the Sun's surface with the empty space just above Earth's surface, pretending Earth has no air. One says both are Einstein spaces with the number zero, so a ball of crumbs behaves the same in both. The other says the drifts must be far stronger at the Sun, because the Sun has 333,000 times Earth's mass. Who is right? Two facts help. The Sun's surface is 109 times farther from the Sun's centre than Earth's surface is from Earth's centre. Drifts weaken by the cube of that distance: twice as far gives drifts 8 times weaker.

**Hints**

1. What is the drift total in each cabin, and why?
2. How much weaker do the drifts become when the distance from the centre grows 109 times? Compare that with 333,000.

**Answer:** Both drift totals are zero, so the first friend is right about the number. But the drifts just above Earth's surface are about four times stronger than just above the Sun's surface. So the ball does not behave the same: near Earth it gets longer and narrower about four times faster.

**Must contain:** Both drift totals are zero because the drift along the line is twice each drift across it; 109 times the distance weakens the drifts about 1,300,000 times, more than the mass strengthens them; Earth's surface has drifts about four times stronger, though both numbers are zero

**Numeric:** drift strength at Earth's surface divided by drift strength at the Sun's surface = 3.9 1 (magnitude, ±15%); drift total in each cabin, divided by the drift along the line to the centre = 0 1 (magnitude, ±0.05)

**Solution**

1. In both cabins the crumbs fall through empty space, so the drift along the line to the centre is twice each drift across it, and the three drifts add to zero. Both places are Einstein spaces with the number zero.
2. A drift grows in step with the mass that pulls, so the Sun's mass makes its drifts 333,000 times stronger than Earth's would be at the same distance from the centre.
3. But the Sun's surface is 109 times farther from its centre. 109 times 109 times 109 is about 1,300,000, so the Sun's drifts are 1,300,000 times weaker for that reason.
4. 1,300,000 divided by 333,000 is about 3.9. So the drifts just above Earth's surface are about four times stronger than just above the Sun's surface. Both totals are still zero.

**Targets:** `same-total-means-same-curving`

### `moving-through-a-dust-universe` · working · difficulty 2 · calculation

Take the trace-reversed field equation as given: $R_{\mu\nu} = \dfrac{8\pi G}{c^4}\Big(T_{\mu\nu} - \tfrac12 T g_{\mu\nu}\Big) + \Lambda g_{\mu\nu}$. Dust of density $\rho$ and four-velocity $u^\mu$ has $T_{\mu\nu} = \rho\,u_\mu u_\nu$. An observer with four-velocity $w^\mu$, moving through the dust at speed $v$, has $u_\mu w^\mu = -\gamma c^2$. Compute the tidal trace $R_{\mu\nu}w^\mu w^\nu$, evaluate the factor multiplying $4\pi G\rho$ for $v = 0.6c$, and say whether a dust-filled universe is an Einstein space.

**Hints**

1. First find $T$ using $u_\mu u^\mu = -c^2$.
2. Contract term by term with $w^\mu w^\nu$, using $w_\mu w^\mu = -c^2$.

**Answer:** $R_{\mu\nu}w^\mu w^\nu = 4\pi G\rho\,(2\gamma^2 - 1) - \Lambda c^2$; at $v = 0.6c$, $\gamma = 1.25$ and the factor is $2.125$. Because the reading depends on the observer's speed, $R_{\mu\nu}$ is not a multiple of $g_{\mu\nu}$ unless $\rho = 0$: a dust-filled universe is not an Einstein space.

**Must contain:** T equals minus rho c squared; The trace is four pi G rho times two gamma squared minus one, minus capital lambda c squared; Gamma is 1.25 at six tenths of c, giving the factor 2.125; A speed-dependent trace means the Ricci tensor is not proportional to the metric

**Numeric:** factor multiplying 4 pi G rho at v = 0.6c = 2.125 1 (signed, ±1%)

**Solution**

1. $T = g^{\mu\nu}\rho\,u_\mu u_\nu = \rho\,u_\mu u^\mu = -\rho c^2$.
2. So $T_{\mu\nu} - \tfrac12 T g_{\mu\nu} = \rho\,u_\mu u_\nu + \tfrac12\rho c^2 g_{\mu\nu}$.
3. Contract with $w^\mu w^\nu$: $\rho(u_\mu w^\mu)^2 + \tfrac12\rho c^2 (w_\mu w^\mu) = \rho\gamma^2c^4 - \tfrac12\rho c^4 = \rho c^4(\gamma^2 - \tfrac12)$.
4. Multiply by $8\pi G/c^4$ and add the $\Lambda$ term, $\Lambda g_{\mu\nu}w^\mu w^\nu = -\Lambda c^2$: $R_{\mu\nu}w^\mu w^\nu = 8\pi G\rho(\gamma^2 - \tfrac12) - \Lambda c^2 = 4\pi G\rho(2\gamma^2 - 1) - \Lambda c^2$.
5. At rest in the dust, $\gamma = 1$ and the trace is $4\pi G\rho - \Lambda c^2$. At $v = 0.6c$, $\gamma = 1/\sqrt{1 - 0.36} = 1.25$, $\gamma^2 = 1.5625$, and $2\gamma^2 - 1 = 2.125$.
6. In an Einstein space the trace is $-\lambda c^2$ for every observer. Here it changes with $v$ whenever $\rho \neq 0$, so the dust universe is not an Einstein space.

**Targets:** `one-family-of-observers-suffices`, `obeys-einsteins-equation`

### `same-total-for-every-observer-means-einstein` · formal · difficulty 2 · proof

Let $(M, g)$ be a connected Lorentzian manifold of dimension $n \geq 3$ with $G = c = 1$. Suppose that at every point the value $\mathrm{Ric}(u,u)$ is the same for every unit timelike vector $u$ at that point. Prove that $g$ is an Einstein metric, and identify its constant.

**Hints**

1. Define $\lambda(p)$ by $\mathrm{Ric}(u,u) = -\lambda(p)$ and consider $S = \mathrm{Ric} - \lambda g$.
2. A quadratic form vanishing on an open set vanishes identically; then polarize.

**Answer:** At each point $S(v,v) = 0$ for all timelike $v$ by scaling, hence for all $v$ because timelike vectors form an open set, hence $S = 0$ by polarization: $\mathrm{Ric} = \lambda(p)g$. The contracted Bianchi identity then makes $\lambda$ constant for $n \geq 3$, so $g$ is Einstein with $\lambda = -\mathrm{Ric}(u,u)$ for any unit timelike $u$.

**Must contain:** The quadratic form of Ricci minus lambda g vanishes on the open set of timelike vectors, hence everywhere; Polarization gives Ricci equal to lambda of p times g; The contracted Bianchi identity makes lambda constant for n at least three

**Solution**

1. Fix a point $p$ and let $-\lambda(p)$ be the common value of $\mathrm{Ric}(u,u)$ over unit timelike $u$ at $p$; with signature $(-,+,+,+)$ a unit timelike vector has $g(u,u) = -1$. Define $S = \mathrm{Ric} - \lambda(p)\,g$, a symmetric bilinear form on $T_pM$ with $S(u,u) = -\lambda + \lambda = 0$ for every unit timelike $u$.
2. Any timelike $v$ is $a u$ with $a > 0$ and $u$ unit timelike, and $S(v,v) = a^2 S(u,u) = 0$. So the quadratic form $q(v) = S(v,v)$ vanishes on the set of timelike vectors, which is open in $T_pM$.
3. $q$ is a polynomial in the components of $v$; a polynomial vanishing on a nonempty open set is the zero polynomial. So $q(v) = 0$ for every $v \in T_pM$.
4. Polarize: $S(v,w) = \tfrac12\big(q(v+w) - q(v) - q(w)\big) = 0$ for all $v, w$. Hence $S = 0$ and $\mathrm{Ric} = \lambda(p)\,g$ at $p$.
5. The function $\lambda = R/n$ is smooth, so the constancy derivation applies: $(n-2)\partial_\nu\lambda = 0$, and $n \geq 3$ on a connected manifold makes $\lambda$ constant.
6. So $g$ is Einstein with $\lambda = -\mathrm{Ric}(u,u)$ for any unit timelike $u$, the common tidal trace with its sign reversed. The converse is immediate: $\mathrm{Ric}(u,u) = \lambda g(u,u) = -\lambda$.

**Targets:** `one-family-of-observers-suffices`

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite's gradiometer** (measured, working). The trace of the tidal matrix read by a freely falling gradiometer is $R_{\mu\nu}u^\mu u^\nu$. Above Earth, with the satellite's rotation removed, the diagonal gradients sum to zero within noise everywhere along the orbit while each varies with altitude: the near-Earth vacuum passes the gradiometer test with $\lambda$ consistent with zero. *Numbers:* At $r = 6626\ \mathrm{km}$: radial gradient $-2GM/r^3 = -2740\ \mathrm{E}$, each horizontal gradient $+1370\ \mathrm{E}$, sum zero within a few hundredths of an eötvös; the dark-energy share $-\Lambda c^2 \approx -1\times10^{-26}\ \mathrm{E}$ is far below detection. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **The cosmological constant inferred from the cosmic microwave background and the expansion history** (measured, working). The far future of a universe whose matter dilutes away while $\Lambda$ stays is an Einstein spacetime with $\lambda = \Lambda$: de Sitter space. The measured value sets the tidal trace $-\Lambda c^2$ every freely falling observer would then read. *Numbers:* $H_0 = 67.4\ \mathrm{km/s/Mpc}$ and $\Omega_\Lambda = 0.685$ give $\Lambda = 3\Omega_\Lambda H_0^2/c^2 = 1.1\times10^{-52}\ \mathrm{m^{-2}}$, so $\Lambda c^2 = 9.8\times10^{-36}\ \mathrm{s^{-2}}$; a ball released at rest grows by one tenth in $\sqrt{0.2/\Lambda c^2} = 1.4\times10^{17}\ \mathrm{s}$, about $4.5$ billion years. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Predict the two cabins** (entry). Ask for a prediction about a ball of crumbs in a cabin at Mercury's distance and one at Neptune's, reveal that both totals are zero while the drifts differ half a million times, then name the property and test the name trap with the friend's claim. *Why:* One prediction separates the total from the strength of the drifts, and the name trap is corrected before it settles. *Predict:* In which cabin does the room the ball takes up start to change, and in which are the drifts stronger? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `checks/two-cabins-near-the-sun`, `ways_in/one-total-everywhere-for-everyone`, `ways_in/same-total-is-not-same-curving`, `checks/obeys-the-equation-so-einstein-space`
2. **From crumbs to lambda** (working). Write the drift total as the double contraction of the Ricci tensor, ask what makes it observer-independent, and derive the traces and lambda equals capital lambda. *Why:* The definition appears as the answer to the entry question, not as an arbitrary equation. *Predict:* If every observer must find the same value of the Ricci tensor on their own four-velocity, what form must the Ricci tensor take? *Uses:* `ways_in/one-constant-fixes-every-trace`, `derivations/traces-of-the-einstein-condition`, `checks/schwarzschild-is-an-einstein-space`
3. **Run the gradiometer test** (working). Present the test and the GOCE numbers, then the dust universe, which obeys Einstein's equation yet fails the test because moving cabins read more. *Why:* It turns the definition into a measurement and shows why every cabin cannot be dropped. *Predict:* Will a cabin rushing through the dust read the same total as a cabin at rest in it? *Uses:* `ways_in/the-gradiometer-test`, `problems/moving-through-a-dust-universe`, `checks/comoving-observers-agree`
4. **Constancy and the Weyl remainder** (formal). Derive the constancy of lambda from the contracted Bianchi identity, examine dimension two, then decompose the Riemann tensor to show what the condition leaves free. *Why:* A graduate reader must own both: why lambda is constant, and why Einstein is weaker than constant curvature. *Predict:* Does a Ricci tensor proportional to the metric force the factor to be constant in every dimension? *Uses:* `ways_in/definition-constancy-and-the-weyl-remainder`, `derivations/lambda-is-constant`, `derivations/weyl-remainder-of-an-einstein-space`, `checks/every-surface-looks-einstein`, `checks/product-of-two-spheres`
5. **Origins and open questions** (research). Show the variational origin and the Ricci flow scaling, then survey the four research fronts, ending with the Hitchin–Thorpe check. *Why:* The research reader needs the map of the field and one obstruction to compute with. *Uses:* `ways_in/critical-points-of-total-scalar-curvature`, `ways_in/einstein-metrics-as-a-research-field`, `checks/hitchin-thorpe-obstruction`

## Misconceptions

### “If the drift total is the same everywhere, the curving must be the same everywhere.” · entry · `same-total-means-same-curving`

- **Why it is tempting:** The total is the only number the definition mentions.
- **What is true:** The total says how the three drifts add up, not how strong they are. Between Mercury's and Neptune's distances the drifts differ half a million times while the total stays zero.
- **Exposed by:** `checks/two-cabins-near-the-sun`

### “Our universe obeys Einstein's equation, so it is an Einstein space.” · entry · `obeys-einsteins-equation`

- **Why it is tempting:** The name sounds like a label for anything Einstein's equation describes.
- **What is true:** The name is about geometry: one drift total everywhere, for every cabin. A universe with gas clouds and voids gives different totals in different places, so it is not one.
- **Exposed by:** `checks/obeys-the-equation-so-einstein-space`

### “A Ricci-flat spacetime is not an Einstein space, because zero times the metric is no proportionality.” · working · `zero-is-not-a-multiple`

- **Why it is tempting:** Proportional suggests a nonzero constant, and Ricci-flat spacetimes are usually discussed separately.
- **What is true:** Zero is a constant, and the definition allows it: Schwarzschild and Kerr are Einstein spaces with lambda equal to zero.
- **Exposed by:** `checks/schwarzschild-is-an-einstein-space`

### “If all the observers at rest in the matter find the same total at a given time, the spacetime is an Einstein space.” · working · `one-family-of-observers-suffices`

- **Why it is tempting:** In a homogeneous universe every comoving observer does find the same total.
- **What is true:** Einstein requires the same total for every observer, including those moving through the matter. Dust gives moving observers a larger reading.
- **Exposed by:** `checks/comoving-observers-agree`

### “Every surface is an Einstein space, because its Ricci tensor is always half the scalar curvature times the metric.” · formal · `pointwise-is-enough-in-two-dimensions`

- **Why it is tempting:** In higher dimensions the pointwise proportionality is the whole definition.
- **What is true:** The constancy argument has the factor n minus two and says nothing for n equal to two. An Einstein surface is one of constant Gaussian curvature, which an ellipsoid is not.
- **Exposed by:** `checks/every-surface-looks-einstein`

### “An Einstein metric in four dimensions has constant curvature, as it does in three.” · formal · `einstein-means-constant-curvature`

- **Why it is tempting:** In three dimensions the two notions coincide, and constant curvature always implies Einstein.
- **What is true:** The Einstein condition fixes only the traces of the Riemann tensor; from four dimensions on the Weyl tensor is free. Schwarzschild and the product of two equal spheres are Einstein without constant curvature.
- **Exposed by:** `checks/product-of-two-spheres`

## Checks

1. **Entry · predict** `checks/two-cabins-near-the-sun`. Two cabins fall freely through the empty space near the Sun. One is at Mercury's distance from the Sun, the other at Neptune's distance, about 78 times farther. In each cabin someone lets go of a small ball of crumbs, at rest. In which cabin does the room the ball takes up start to change? In which cabin are the drifts stronger, and by roughly how much?
   - **Hints:** What does the drift along the line add up with, and to what? / If the distance grows 78 times, by what factor do the drifts weaken?
   - **Answer:** In neither cabin does the room start to change. In both, the drift along the line to the Sun is twice each drift across it, so the three add to zero. The drifts are stronger at Mercury's distance by 78 times 78 times 78, nearly half a million times, because drifts weaken by the cube of the distance. The total is the same, zero, while the drifts are nothing alike.
   - **Must contain:** Neither ball's room starts to change; The drift along the line is twice each drift across it, so the total is zero in both; The drifts at Mercury's distance are nearly half a million times stronger
   - **Numeric:** drift strength at Mercury's distance divided by drift strength at Neptune's distance = 470000 1 (magnitude, ±15%)
   - **Targets:** `same-total-means-same-curving`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · evaluate-claim** `checks/obeys-the-equation-so-einstein-space`. A friend says: our universe obeys Einstein's equation, so it must be an Einstein space. Einstein's equation is the law of gravity in general relativity, which ties the curving of spacetime at each place to the matter there. Is the friend right? Test the claim with a cabin falling freely inside a gas cloud and a cabin falling freely in a void, a huge region with almost no galaxies or gas in it.
   - **Hints:** What decides whether a spacetime is an Einstein space? / What happens to a ball of crumbs let go among gas?
   - **Answer:** The friend is not right. Being an Einstein space is not about obeying Einstein's equation; it is about the drift total being the same one number everywhere, for every cabin. Inside a gas cloud, the gas among the crumbs pulls each crumb toward the middle, so the ball starts to shrink. Drifts toward the centre crumb count as minus, so the total is below zero. In a void almost nothing is among the crumbs, so the total is close to zero. Two places, two totals: our universe is not an Einstein space.
   - **Must contain:** Obeying Einstein's equation is not the test; Inside the gas cloud the ball starts to shrink and the total is below zero; In the void the total is close to zero, so the totals differ and the universe is not an Einstein space
   - **Targets:** `obeys-einsteins-equation`
3. **Working · numeric** `checks/schwarzschild-is-an-einstein-space`. Outside a non-rotating star, with the cosmological constant neglected, the Ricci tensor vanishes: $R_{\mu\nu} = 0$. Is this spacetime an Einstein space? Give $\lambda$, $R$ and $G_{\mu\nu}$, and say whether it has constant curvature.
   - **Hints:** Is zero a constant multiple of the metric?
   - **Answer:** Yes. $R_{\mu\nu} = 0 = 0\cdot g_{\mu\nu}$, so it is an Einstein space with $\lambda = 0$; then $R = 0$ and $G_{\mu\nu} = 0$. It does not have constant curvature: $K = \lambda/3 = 0$ would mean a vanishing Riemann tensor, but the Kretschmann scalar $48G^2M^2/c^4r^6$ is nonzero. All of its curvature is Weyl curvature.
   - **Must contain:** Zero is an allowed constant, so it is an Einstein space with lambda zero; R and the Einstein tensor vanish; Not constant curvature, because the Riemann tensor is nonzero
   - **Numeric:** lambda = 0 m^-2 (signed, ±1e-52)
   - **Targets:** `zero-is-not-a-multiple`
4. **Working · evaluate-claim** `checks/comoving-observers-agree`. Claim: in a homogeneous universe filled with dust, every observer at rest in the dust measures the same tidal trace at a given cosmic time, so the universe is an Einstein space. Evaluate the claim.
   - **Hints:** What does an observer moving relative to the dust read?
   - **Answer:** The claim is false. An Einstein space needs the same trace for every observer at every event. Observers at rest in dust read $4\pi G\rho - \Lambda c^2$, but an observer moving through the dust at speed $v$ reads $4\pi G\rho(2\gamma^2 - 1) - \Lambda c^2$, larger whenever $\rho \neq 0$; the reading also falls as $\rho$ dilutes. So the Ricci tensor is not a multiple of the metric unless $\rho = 0$, the de Sitter case, which is an Einstein space.
   - **Must contain:** Agreement among one family of observers is not enough; Moving observers read a trace larger by the factor two gamma squared minus one on the matter term; Only with zero density does the Ricci tensor become proportional to the metric
   - **Targets:** `one-family-of-observers-suffices`
5. **Formal · explain** `checks/every-surface-looks-einstein`. In two dimensions every metric satisfies $R_{\mu\nu} = \tfrac12 R\,g_{\mu\nu}$. Explain why, explain why the constancy argument says nothing here, and state what an Einstein surface therefore means.
   - **Hints:** Where does the dimension enter the constancy derivation?
   - **Answer:** In two dimensions the Riemann tensor has one independent component, so $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ with $K$ the Gaussian curvature; contracting gives $R_{\sigma\nu} = K g_{\sigma\nu}$ and $R = 2K$. The constancy argument gives $(n - 2)\partial_\nu f = 0$, empty for $n = 2$; on an ellipsoid $f = K$ varies from tips to sides. An Einstein surface must therefore be defined by demanding a constant: a surface of constant Gaussian curvature $K = \lambda$.
   - **Must contain:** One independent Riemann component forces Ricci equal to K times the metric; The factor n minus two vanishes, so the Bianchi argument is empty in two dimensions; An Einstein surface means constant Gaussian curvature
   - **Targets:** `pointwise-is-enough-in-two-dimensions`
6. **Formal · numeric** `checks/product-of-two-spheres`. Take the Riemannian product of two round two-spheres of radii $a$ and $b$. For which radii is the product an Einstein manifold, and what is $\lambda a^2$ then? Does it have constant curvature?
   - **Hints:** What is the sectional curvature of a plane with one direction in each factor?
   - **Answer:** The Ricci tensor of a product is the direct sum of the factors' Ricci tensors, and a two-sphere of radius $a$ has $\mathrm{Ric} = (1/a^2)g$. So $\mathrm{Ric} = (1/a^2)g_1 \oplus (1/b^2)g_2$, a multiple of $g_1 \oplus g_2$ exactly when $a = b$; then $\lambda a^2 = 1$. It never has constant curvature: a plane with one vector from each factor has sectional curvature $0$, a plane inside a factor has $1/a^2$, and constant curvature would need $K = \lambda/3 = 1/(3a^2)$ for every plane. The Weyl tensor is nonzero.
   - **Must contain:** Ricci of a product is the sum of the factors' Ricci tensors; Einstein exactly when the radii are equal, with lambda equal to one over a squared; Mixed planes have zero sectional curvature, so the curvature is not constant
   - **Numeric:** lambda times a squared for equal radii = 1 1 (signed, ±1%)
   - **Targets:** `einstein-means-constant-curvature`
7. **Research · evaluate-claim** `checks/hitchin-thorpe-obstruction`. Claim: every compact oriented four-manifold admits an Einstein metric. Evaluate it with $\chi$ and $\tau$, testing the connected sum of $k$ copies of $\mathbb{CP}^2$ ($\chi = 2 + k$, $\tau = k$) and the K3 surface ($\chi = 24$, $\tau = -16$).
   - **Hints:** Compare the Gauss–Bonnet and signature integrands when the traceless Ricci tensor vanishes.
   - **Answer:** False. For an Einstein metric the traceless Ricci tensor vanishes, and the Gauss–Bonnet and signature integrals give $\chi \geq \tfrac{3}{2}|\tau|$, the Hitchin–Thorpe inequality, with equality only for flat manifolds and quotients of K3 with a Ricci-flat Kähler metric. For $k$ copies of $\mathbb{CP}^2$, $2 + k \geq \tfrac32 k$ requires $k \leq 4$, so five or more copies admit no Einstein metric. K3 gives $24 = \tfrac32\cdot16$: equality, realized by Yau's metric.
   - **Must contain:** Einstein makes the traceless Ricci term drop out of the Gauss–Bonnet integrand; chi is at least three halves the absolute signature; At most four copies of CP2 can be summed; K3 saturates the bound
   - **Numeric:** largest k for which the inequality allows an Einstein metric on k copies of CP2 = 4 1 (signed, ±0.1)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Symbol and normalization of the Einstein constant | $R_{\mu\nu} = \lambda g_{\mu\nu}$ with lower-case $\lambda$; in four-dimensional vacuum $\lambda = \Lambda$; $K$ is reserved for sectional and Gaussian curvature, with $\lambda = (n-1)K$ for constant curvature. | Some texts write the constant as $k$, $K$ or $C$, some write $R_{\mu\nu} = (R/n)g_{\mu\nu}$ with no separate constant, and some use $\Lambda$ directly, which hides the factor $2/(n-2)$ outside four dimensions. |
| Sign of the Einstein constant | With the course Riemann and Ricci conventions a round sphere has $\lambda > 0$ and de Sitter spacetime has $\lambda = \Lambda > 0$; the tidal trace is $-\lambda c^2$ because $u_\mu u^\mu = -c^2$. | Some texts define the Ricci tensor with the opposite sign, so their spheres have negative $\lambda$, and some quote the tidal trace with the opposite sign because their observers have $u_\mu u^\mu = +1$. |
| Scope of the term Einstein space | Any dimension, any signature, any constant including zero: Ricci-flat metrics are Einstein spaces, and Einstein manifold and Einstein metric are synonyms. | Some texts reserve the term for Riemannian metrics, some exclude $\lambda = 0$, and some use Einstein space only for spacetimes; a few use it loosely for any solution of Einstein's equation, which this note does not. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The entry experience: the ball of crumbs released in cabins at different places and speeds, with the drift total read out beside the three drifts, in a chosen spacetime. *Sketch:* This concept adds a spacetime chooser to the ball mode: empty space near a star, a dark-energy-only universe, and a dust universe. The learner drags the cabin to other distances and sets its speed. Readouts show the three drifts, their total, and a flag that lights when the total has matched at every place and speed tried. Near the star the drifts change by thousands while the total stays zero; in the dust universe the total rises with cabin speed. Design rule: drifts and total side by side, so a constant total is never confused with constant drifts.
- [[six-entry-curvature-table]] (supporting): Shows the Einstein condition as a pattern in the Ricci readouts: each Ricci entry equal to lambda times the metric entry. *Sketch:* This concept adds an Einstein toggle beside the Ricci readouts: it divides each diagonal Ricci entry by the metric entry and lights up when the quotients agree and the off-diagonal entries vanish. Presets: Schwarzschild (lit, zero), de Sitter (lit, Lambda), dust universe (unlit).

## Tutor moves

**Open with**

- Picture two cabins falling freely through empty space, one close to the Sun and one far out near Neptune. In each, a ball of crumbs is let go at rest. Will the room the ball takes up start to change in either cabin? Will the crumbs drift more in one cabin than in the other? *(prediction)*

**If the learner is stuck**

- *The learner says the drifts must be equal at two places because both totals are zero.* → Replay the three drifts at Mercury's distance and at Neptune's distance side by side, and have the learner add each set to zero before comparing their sizes. *Uses:* `ways_in/same-total-is-not-same-curving`, `checks/two-cabins-near-the-sun`

**Common questions**

- *Why is it called an Einstein space if it is not about obeying Einstein's equation?* (entry) The name comes from a special case. Take a spacetime with no matter at all, only empty space and perhaps dark energy. There, Einstein's equation says exactly that the drift total is one number everywhere, for every cabin. Mathematicians took that pattern and named it after him. So an Einstein space is what Einstein's equation gives when nothing is in it, and the name is used for that pattern wherever it appears. *Uses:* `ways_in/one-total-everywhere-for-everyone`, `checks/obeys-the-equation-so-einstein-space`
- *Why can the factor in front of the metric not vary from point to point?* (formal) Because of the contracted Bianchi identity. With $R_{\mu\nu} = f g_{\mu\nu}$, the divergence of the left side is $\partial_\nu f$ while half the gradient of $R = nf$ is $\tfrac{n}{2}\partial_\nu f$, so $(n-2)\partial_\nu f = 0$. Only in two dimensions does this say nothing, and there $R$ is free to vary. *Uses:* `derivations/lambda-is-constant`, `checks/every-surface-looks-einstein`

**Switching levels**

- To working when: asks what the number is or how to compute it; mentions the cosmological constant or the Ricci tensor by name. Write the drift total as the double contraction of the Ricci tensor and derive the traces and lambda equals capital lambda. *Uses:* `ways_in/one-constant-fixes-every-trace`, `derivations/traces-of-the-einstein-condition`
- To formal when: asks why lambda must be constant; asks whether Einstein implies constant curvature. Go to the constancy derivation and the Weyl remainder, then the product-of-spheres check. *Uses:* `ways_in/definition-constancy-and-the-weyl-remainder`, `checks/product-of-two-spheres`
- To research when: asks which manifolds admit Einstein metrics; mentions Kähler–Einstein metrics, Ricci flow, or holography. Present the variational origin, then the research way and the Hitchin–Thorpe check. *Uses:* `ways_in/critical-points-of-total-scalar-curvature`, `ways_in/einstein-metrics-as-a-research-field`, `checks/hitchin-thorpe-obstruction`

**Pronunciations:** Weyl → vile; Kähler → KAY-ler; Kottler → KOT-ler; Nariai → nah-ree-EYE; Schur → shoor

**Voice notes:** At entry, say 'drift total', never 'trace' or 'Ricci'. Say 'lambda' for the Einstein constant and 'capital lambda' for the cosmological constant.

## History

- **Friedrich Schur (1886).** Proved that a sectional curvature independent of the plane at each point is constant in three or more dimensions. The modern proof of this theorem uses the contracted Bianchi identity, the same argument that gives the constancy of the Einstein constant. Friedrich Schur (1886), *Ueber den Zusammenhang der Räume constanten Riemann'schen Krümmungsmaasses mit den projectiven Räumen*, Mathematische Annalen 27, 537–567, doi:10.1007/BF01906632
- **David Hilbert (1915).** Derived the gravitational field equations from the total scalar curvature, the variational principle whose vacuum critical points are Einstein metrics. David Hilbert (1915), *Die Grundlagen der Physik (Erste Mitteilung)*, Nachrichten von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-physikalische Klasse, 395–407
- **Albert Einstein (1917).** Introduced the cosmological constant, the term that makes the empty-space field equation the Einstein condition with a nonzero constant. Albert Einstein (1917), *Kosmologische Betrachtungen zur allgemeinen Relativitätstheorie*, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften (Berlin), 142–152
- **Willem de Sitter (1917).** Found the empty solution with a cosmological constant: the first Einstein spacetime in physics with a nonzero constant, and the one of constant curvature. Willem de Sitter (1917), *On Einstein's theory of gravitation and its astronomical consequences. Third paper*, Monthly Notices of the Royal Astronomical Society 78, 3–28, doi:10.1093/mnras/78.1.3
- **Friedrich Kottler (1918).** Found the spherically symmetric solution with a mass and a cosmological constant, an Einstein spacetime with nonzero constant and nonzero Weyl tensor. Friedrich Kottler (1918), *Über die physikalischen Grundlagen der Einsteinschen Gravitationstheorie*, Annalen der Physik 361, 401–462, doi:10.1002/andp.19183611402
- **Alexei Zinovievich Petrov (1961).** Classified Einstein spacetimes by the algebraic type of their Weyl tensor, the Petrov types, and made the term Einstein space standard in relativity. Alexei Zinovievich Petrov (1969), *Einstein Spaces*, Pergamon Press, Oxford (translation of the 1961 Russian edition)

## Research horizon

- **Kähler–Einstein metrics and K-stability.** On a compact Kähler manifold the sign of $\lambda$ is fixed by the first Chern class. Yau's solution of the Calabi conjecture gives Ricci-flat Kähler metrics when $c_1 = 0$ and, with Aubin, Kähler–Einstein metrics with $\lambda < 0$ when $c_1 < 0$. For $c_1 > 0$ existence is equivalent to K-stability, proved by Chen, Donaldson and Sun and by Tian. Shing-Tung Yau (1978), *On the Ricci curvature of a compact Kähler manifold and the complex Monge–Ampère equation, I*, Communications on Pure and Applied Mathematics 31, 339–411, doi:10.1002/cpa.3160310304; Xiuxiong Chen, Simon Donaldson, Song Sun (2015), *Kähler–Einstein metrics on Fano manifolds. I: Approximation of metrics with cone singularities*, Journal of the American Mathematical Society 28, 183–197, doi:10.1090/S0894-0347-2014-00799-2; Gang Tian (2015), *K-stability and Kähler–Einstein metrics*, Communications on Pure and Applied Mathematics 68, 1085–1156, doi:10.1002/cpa.21578
- **Existence, obstruction and Ricci flow in low dimensions.** The Hitchin–Thorpe inequality $\chi \geq \tfrac32|\tau|$ obstructs Einstein metrics on many four-manifolds, and Hitchin characterized the equality case. Hamilton's Ricci flow, whose fixed points up to scale are Einstein metrics, deforms positive-Ricci three-manifolds to constant curvature, and Böhm's cohomogeneity-one constructions gave non-round Einstein metrics on spheres of dimension five to nine. Whether the four-sphere carries an Einstein metric other than the round one is open. Nigel Hitchin (1974), *Compact four-dimensional Einstein manifolds*, Journal of Differential Geometry 9, 435–441, doi:10.4310/jdg/1214432419; Richard S. Hamilton (1982), *Three-manifolds with positive Ricci curvature*, Journal of Differential Geometry 17, 255–306, doi:10.4310/jdg/1214436922; Christoph Böhm (1998), *Inhomogeneous Einstein metrics on low-dimensional spheres and other low-dimensional spaces*, Inventiones Mathematicae 134, 145–176, doi:10.1007/s002220050261; Arthur L. Besse (1987), *Einstein Manifolds*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3) 10, Springer, Berlin, doi:10.1007/978-3-540-74311-8
- **Stability of Einstein spacetimes with positive constant.** The four-dimensional Einstein spacetimes with $\lambda > 0$ are the vacua of a universe with a cosmological constant. Friedrich proved that de Sitter space is nonlinearly stable, and Hintz and Vasy proved the stability of slowly rotating Kerr–de Sitter black holes, so small perturbations of these Einstein spacetimes decay back to them. Stability of the full Kerr–de Sitter family is the frontier, and the measured $\Lambda$ makes these the spacetimes our universe approaches. Helmut Friedrich (1986), *On the existence of n-geodesically complete or future complete solutions of Einstein's field equations with smooth asymptotic structure*, Communications in Mathematical Physics 107, 587–609, doi:10.1007/BF01205488; Peter Hintz, András Vasy (2018), *The global non-linear stability of the Kerr–de Sitter family of black holes*, Acta Mathematica 220, 1–206, doi:10.4310/ACTA.2018.v220.n1.a1; Sean M. Carroll (2001), *The Cosmological Constant*, Living Reviews in Relativity 4, 1, doi:10.12942/lrr-2001-1
- **Einstein metrics with negative constant and holography.** Conformally compact Einstein metrics with $\lambda < 0$, constructed by Graham and Lee for conformal infinities near the round sphere, are the bulk geometries of the AdS/CFT correspondence: the boundary conformal class is the source and the metric's asymptotic expansion encodes the stress tensor of a conformal field theory. Existence for general boundary data and uniqueness of fillings are open. C. Robin Graham, John M. Lee (1991), *Einstein metrics with prescribed conformal infinity on the ball*, Advances in Mathematics 87, 186–225, doi:10.1016/0001-8708(91)90071-E; Juan Maldacena (1998), *The large N limit of superconformal field theories and supergravity*, Advances in Theoretical and Mathematical Physics 2, 231–252, doi:10.4310/ATMP.1998.v2.n2.a1; Ofer Aharony, Steven S. Gubser, Juan Maldacena, Hirosi Ooguri, Yaron Oz (2000), *Large N field theories, string theory and gravity*, Physics Reports 323, 183–386, doi:10.1016/S0370-1573(99)00083-6

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** You let go of a ball of crumbs in a cabin falling near the Sun. It gets pulled longer toward the Sun and squeezed narrower sideways, the stretch is twice each squeeze, so they add to zero and the ball keeps its size. An Einstein space is a spacetime where that added-up number is the same everywhere, in every cabin, however fast it goes. Near the Sun the number is zero. A universe with only dark energy is one too, with a number above zero, and there the ball grows, but incredibly slowly. Same number doesn't mean same pull: near Mercury the crumbs drift half a million times more than near Neptune but still add to zero. Our universe isn't one because gas clouds shrink the ball and voids don't. I don't get why it's called an Einstein space if it isn't about his equation, and I don't get why the stretch is exactly twice the squeeze or why drifts weaken by the cube. Also, wait: shrinking in gas gives a number above zero and growing with dark energy also gives a number above zero?

**Stumbles (14)**

- “The drift along the line is twice each drift across it, and there are two across directions. So the three add to zero”: Step left implicit: nothing says a drift apart and a drift together have opposite signs, so 'twice' plus 'two' does not visibly make zero. The Ricci prerequisite counts a drift away from the centre crumb as plus and a drift toward it as minus.
- “Inside a gas cloud, the gas among the crumbs pulls each crumb toward the middle, so the ball starts to shrink and the total is above zero.”: Sign clash: with drifts apart counted as plus (the prerequisite's rule, and the rule that makes the dark-energy number 'above zero' while the ball grows), a shrinking ball has a total below zero. Shrinking and growing cannot both be 'above zero'.
- “Add up the three drifts: along the line, and along two directions across it.”: Direction without a reference: which two directions across the line? A teenager would pick any two.
- “in cabins rushing past at any speed”: Rushing past what? The comparison is between cabins at the same places moving differently.
- “only matter among the crumbs could change it, and there is none”: First what-if: the Sun is matter and it is right there. Nothing says why it does not count.
- “in every freely falling cabin, however it moves”: Ambiguous 'it': the cabin, the spacetime or the ball.
- “Empty space near the Sun is one, with the number zero.”: 'is one' reads as 'is one number' right after 'one number'; had to reread.
- “a ball of crumbs at rest starts to grow by the same tiny amount everywhere. One tenth takes about four and a half billion years”: 'Amount' sounds like a fixed size but the claim is a rate, and 'one tenth' of what is not said. Also no reason is given for the number being above zero rather than below.
- “Neptune is about 78 times farther out, and drifts weaken by 78 times 78 times 78.”: Surprising claim with no reason: why the cube? School physics gives the square of the distance for the pull, if anything. Also 'farther out' from what.
- “yet they still cancel: the total stays zero”: Step left implicit: why do stronger drifts still cancel?
- “A friend says: our universe obeys Einstein's equation, so it must be an Einstein space.”: Undefined term: no entry way or glossary entry says what Einstein's equation is (the note that defines it is a formal-rung prerequisite here), and 'void' appears only in the glossary; the check is not self-contained.
- “the empty space just above Earth's surface”: First what-if: there is air just above Earth's surface, and air is matter among the crumbs.
- “The Sun's mass makes its drifts 333,000 times stronger than Earth's would be at the same distance from the centre.”: Step left implicit: nothing says a drift grows in step with the pulling mass.
- “The drift total of "One drift total, everywhere and for everyone" is R_{mu nu} u^mu u^nu”: Ladder: the entry drift total counts drifts apart as plus, so it is minus the tidal trace; the working way's first sentence flips the sign without saying so, and its 'total reads minus lambda c squared' then contradicts the entry 'number above zero' for dark energy.

**Fixes**

- Fixed the entry sign convention to match the Ricci prerequisite (drift apart = plus): sign rule restated in the first way's recap, explanation and glossary; the gas-cloud check now says the total is below zero; the dark-energy paragraph says why its number is above zero; the working way's first sentence now bridges with drift total = minus the tidal trace = plus lambda c squared.
- First entry way: named the three directions, made the plus-and-minus cancellation explicit, scoped the Sun's matter as outside the ball, replaced 'rushing past' and 'however it moves', and reworded the dark-energy growth as a rate of the room the ball takes up.
- Second entry way: gave the cube its reason (pull weakens by the square, a drift is a difference of pulls and fades by the cube) with a calculator try-it (factor 7.5 for crumbs one unit apart, 7.9 for a tenth of a unit), and said why stronger drifts still cancel.
- Check obeys-the-equation-so-einstein-space: defined Einstein's equation and void inside the question so it is self-contained. Glossary: added Einstein's equation (concept einstein-field-equations) and curving.
- Problem sun-and-earth-surface-cabins: ignored the air explicitly and added the step that a drift grows in step with the pulling mass.
- Summary: 'is one' became 'is an Einstein space'.
- Split two over-long sentences the validator flagged (glossary drift total; the gas-cloud check answer).

**Concerns**

- Entry explanations now total about 435 words by the validator's count, against the 400-word advanced cap and inside the 10% review allowance; the additions are the sign rule, the three named directions, the cube reason and the Sun's-matter scope, all recorded above. To stay inside the allowance, three lowest-value bits were dropped: the second way's closing restatement of its own takeaway ('The drift total says how the drifts add up, not how strong they are', still the takeaway), the clause 'and there is none' (the Sun's-matter sentence now carries the claim), and a repeated 'from Neptune's distance to Mercury's'.
- Physics reviewer: the problem's numeric 'drift total in each cabin' carries unit s^-1; a drift total counted as relative acceleration per unit separation is s^-2, as the working rung's eötvös figures use. Not changed here because it is a units call.
- Physics reviewer: the entry claim 'only matter among the crumbs could change it' is Einstein's equation in disguise (with dark energy handled by simplifies); confirm the wording is acceptable at entry.
- The calculator try-it treats the pull as 1 over distance squared with crumbs one unit and a tenth of a unit apart; ratios computed as 7.47 and 7.94.
- A spinning cabin is not excluded in the entry text; the Ricci prerequisite's entry glossary does not exclude it either, so this note follows it. The working gradiometer way does say non-spinning.

**Re-read** (2026-09-16, revision 4): 2 stumbles in 8 changed passages

- “pulls the ball longer one way and narrower the other two,”: The physics review dropped 'ways', so 'the other two' has no noun; a beginner asks 'the other two what?'
- “the constant is forced even when it is asked for at each event separately”: Working rung: 'it' has no clear noun, and 'asked for at each event separately' does not say what the weaker request is.
- Fix: Summary: restored 'ways' after 'the other two', and split that sentence in two so the average stays at or under 20 words. No wording dropped.
- Fix: One constant fixes every trace: spelled out the weaker, pointwise request that Schur's result still turns into a constant. No claim changed.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Entry sign rule: the drift total (drifts apart counted as plus) is minus the tidal trace, +lambda c^2 in an Einstein space; dark energy gives a number above zero and a growing ball, a gas cloud a number below zero and a shrinking ball.: Geodesic deviation D^2 xi^i/dtau^2 = -c^2 R^i_0i0 xi^i summed over i gives -R_mn u^m u^n as the relative-volume acceleration, matching the prerequisite's initial volume law d^2 dV/dtau^2 = -R_mn u^m u^n dV; de Sitter Ric(u,u) = -Lambda c^2 < 0 so the total is +Lambda c^2; dust Ric(u,u) = 4 pi G rho - Lambda c^2 > 0 for cloud densities, total below zero. Prerequisite's entry text confirmed to count drift away as positive. → Correct; the novice's sign rewrite is confirmed at every rung (recap, explanation, glossary, gas-cloud check, working bridge sentence).
- Traces: R = n lambda, G_mn = (1 - n/2) lambda g_mn, G_mn = -lambda g_mn in four dimensions, lambda = 2 Lambda/(n-2) from G + Lambda g = 0, R = 4 Lambda, tidal trace -lambda c^2, volume law d^2 dV/dtau^2 = lambda c^2 dV.: Re-derived each step by hand with the course Einstein equation G + Lambda g = 8 pi G T/c^4 and u.u = -c^2; traced the converse (R = 4 Lambda then Ric = G + R g/2 = Lambda g). → All correct, signs and factors as in the conventions.
- Constancy: Ric = f g gives (n-2) d f = 0; two dimensions empty, ellipsoid varies.: Contracted Bianchi identity nabla^m R_mn = (1/2) nabla_n R with nabla g = 0; two-dimensional Riemann tensor has one component, Ric = K g. → Correct.
- Ricci decomposition and Weyl remainder: R = C + lambda/(n-1) (g g - g g); K = lambda/(n-1); n = 3 gives constant curvature lambda/2; product of two equal spheres and Nariai are Einstein without constant curvature.: Traced the decomposition on the first and third slots: middle group gives S, last gives (R/n) g, so Ric is recovered; contracted the remainder to lambda g. Product of two-spheres: Ric = (1/a^2) g_1 + (1/b^2) g_2, mixed sectional curvature 0 versus lambda/3 = 1/(3a^2). Nariai: dS_2 and S^2 each with Ric = Lambda g. → Correct; lambda a^2 = 1 for equal radii.
- Dust problem: R_mn w^m w^n = 4 pi G rho (2 gamma^2 - 1) - Lambda c^2; factor 2.125 at v = 0.6c.: Trace-reversed equation checked from the course field equation (R_mn = kappa (T_mn - T g_mn/2) + Lambda g_mn); T = -rho c^2; contraction with w by hand; gamma = 1.25 by python. → Correct; 2 gamma^2 - 1 = 2.125.
- Numbers: Lambda = 3 Omega_Lambda H0^2/c^2 = 1.1e-52 m^-2, Lambda c^2 = 9.8e-36 s^-2, ten-percent growth in sqrt(0.2/Lambda c^2) = 1.4e17 s = 4.5 Gyr; GOCE 2GM/r^3 = 2740 E and GM/r^3 = 1370 E at r = 6626 km; Lambda c^2 = 1e-26 E, 23 powers of ten below 3 mE; Neptune/Mercury = 77.7, 78^3 = 474552; Earth/Sun surface drift ratio 109^3/333000 = 3.89 (3.92 with exact values); try-it ratios 7.47 and 7.94; Hitchin-Thorpe k <= 4 and K3 equality.: One python3 script (scratchpad es_numbers.py) with H0 = 67.4 km/s/Mpc, Omega_Lambda = 0.685, GM_earth = 3.986e14 m^3/s^2. Exact de Sitter growth cosh^3(Ht) = 1.1 gives 4.4 Gyr, so 'about four and a half billion years' holds beyond the initial law. → Every number in the note reproduced within the stated tolerances.
- Gradiometer sign: E_ij = c^2 R^i_0j0 has trace R_mn u^m u^n, radial entry -2GM/r^3 outside a mass.: Schwarzschild static frame R^r_trt = -2M/r^3 (G = c = 1) gives stretching in the deviation equation; Laplacian of the course Phi = -GM/r vanishes outside the mass. → Consistent with the tidal-trace equation of the Ricci prerequisite.
- Variational formula delta int (R - 2 Lambda) sqrt|g| = int (G_mn + Lambda g_mn) delta g^mn sqrt|g|, Ricci-flow scaling g(t) = (1 - 2 lambda t) g_0, scale invariance of int R dV / Vol^((n-2)/n).: delta sqrt|g| = -(1/2) sqrt|g| g_mn delta g^mn; Ricci tensor invariant under constant rescaling; scaling g -> c g sends int R dV to c^(n/2 - 1) times itself. → Correct.
- Hitchin-Thorpe: chi >= 3|tau|/2 from the Gauss-Bonnet and signature integrands with S = 0; equality iff R = 0 and one of W+- vanishes.: chi - 3 tau/2 = (1/8 pi^2) int (2|W-|^2 - |S|^2/2 + R^2/24) dV with the norms of the quoted formulas. → Correct; connected sums of CP^2 allow k <= 4, K3 saturates.
- History scope: Schur 1886 proved constancy of isotropic sectional curvature; de Sitter 1917 found the first Einstein spacetime with nonzero constant.: Schur's proof predates the published Bianchi identity, so the note no longer implies he used it; Schwarzschild 1916 is an earlier curved Einstein spacetime with lambda = 0 under the note's inclusive definition. → Both contributions reworded.
- References: Rummel-Yi-Stummer 2011, Planck 2018 VI, Schur 1886, Hilbert 1915, Einstein 1917, de Sitter 1917, Kottler 1918, Petrov 1969, Yau 1978, Chen-Donaldson-Sun 2015, Tian 2015, Hitchin 1974, Hamilton 1982, Boehm 1998, Besse 1987, Friedrich 1986, Hintz-Vasy 2018, Carroll 2001, Graham-Lee 1991, Maldacena 1998, Aharony et al. 2000.: One web search each for authors, year, title, venue, doi and arxiv. → All twenty-one confirmed and marked verified; Schur's DOI 10.1007/BF01906632 added. Petrov's 1969 Pergamon edition is confirmed as a translation; the 1961 Russian original is from the reviewer's knowledge.

**Counterexamples tried**

- Ricci-flat spacetimes (Schwarzschild, Kerr, vacuum gravitational waves): Einstein with lambda = 0 under the note's definition; the note says so and the working check tests it.
- Two-dimensional surfaces: every metric has Ric = K g pointwise, so the constancy argument is empty; the note demands a constant and gives the ellipsoid.
- Three dimensions: the Weyl tensor vanishes, so Einstein equals constant curvature; stated.
- Product of two equal spheres and the Nariai spacetime: Einstein without constant curvature; stated with a formal check.
- Dust and radiation universes: homogeneous and isotropic yet not Einstein, because moving observers read a different trace; the working problem and check cover it. The Einstein static universe is a sharper case: comoving observers read a trace of exactly zero (Lambda c^2 = 4 pi G rho) yet moving observers read 8 pi G rho (gamma^2 - 1), so one family of observers agreeing on zero still fails; consistent with the one-family misconception, not added to the text.
- Anti-de Sitter: lambda < 0, a released ball shrinks; covered by the volume law's sign statement.
- Disconnected manifold: lambda could differ between components; the definition says connected.
- Entry summary 'longer one way and narrower the other two ways' failed for the dark-energy universe (grows every way) and a gas cloud (shrinks every way); scoped to 'Near the Sun'.
- Spinning cabin: crumbs released at rest in a spinning cabin drift apart by the spin, so the total would not be zero near the Sun; the entry setup and the drift-total glossary now say the cabin does not spin.
- Cube law inside a uniform sphere: drifts are constant there, but the entry text applies the cube only outside the Sun and Earth, where it holds.
- Entry claim 'only matter among the crumbs could change the total': true for vacuum with Lambda neglected (the stated scope) and, with simplifies, for dark energy; pressure is a property of the matter among the crumbs. Acceptable at entry as the prerequisite's own statement.

**Fixes**

- Summary: scoped the tidal-drift pattern to 'Near the Sun', since a dark-energy universe grows the ball every way and a gas cloud shrinks it every way.
- First entry way and drift-total glossary: the cabin does not spin, because a spinning cabin's crumbs drift apart for a reason that is not curvature.
- Entry problem sun-and-earth-surface-cabins: the numeric 'drift total' had unit s^-1; the validator's unit table has no s^-2, so it is now the dimensionless ratio of the total to the drift along the line, value 0 with abs_tol 0.05.
- Working way one-constant-fixes-every-trace: 'the same number at every event' instead of 'one number at every event'; the constancy remark now says the constant is forced even when asked for pointwise; 'growth rate' (lambda c^2 is not a rate) became 'sets'; the Kretschmann remark no longer says curvature grows without limit toward the centre outside a star.
- Gradiometer way and GOCE observation: the trace noise is quoted as a few hundredths of an eötvös rather than a few milli-eötvös, a safer bound for the in-band gradiometer noise; the twenty-powers-of-ten comparison still holds.
- History: Schur's contribution no longer implies he used the Bianchi identity; de Sitter's solution is the first Einstein spacetime with nonzero constant, since Schwarzschild is an earlier one with lambda = 0. Schur's DOI added.
- All twenty-one references marked verified after one web search each.

**Concerns**

- Course conventions do not fix the symbol for the Einstein constant or the scope of the term Einstein space (Ricci-flat and non-Lorentzian cases); the note's notation traps record lower-case lambda and the registry's inclusive definition, as before.
- The validator's unit table lacks s^-2 (relative acceleration per unit separation, the eötvös); the entry problem was rewritten around it, but any note quoting a tidal quantity numerically will need that unit.
- The GOCE trace noise figure is quoted conservatively from memory of the gradiometer's in-band performance; the cited paper's exact trace residual was not read.
- Learner-visible entry and working text changed in this review (summary, first way, glossary, entry problem numeric, working way, gradiometer way); revision bumped from 2 to 3, so the novice review covers revision 2 and a novice re-read of exactly those sentences is due.

**Diff check** (2026-09-16, revision 4)

- Summary and first entry way: near the Sun the ball gets longer along the line to the Sun and narrower the other two ways; a non-spinning cabin is required for the drift total to read curvature alone.: Vacuum tidal tensor outside a spherical mass: radial +2GM/r^3 (apart), transverse -GM/r^3 (together), trace zero; a spinning cabin adds centrifugal separation that is not curvature. → Correct; the scoping to 'near the Sun' and 'without spinning' is needed and true.
- Glossary drift-total: three drifts at right angles, in a non-spinning freely falling cabin, apart counted plus.: Compared with the entry way and the Ricci prerequisite's sign rule (drift away counts plus). → Consistent.
- Problem numeric: drift total divided by the drift along the line to the centre is 0, unit 1, abs_tol 0.05.: At both surfaces the line drift 2GM/r^3 is nonzero and the total is zero, so the ratio is a well-defined 0. → Correct.
- Working way: same trace for every u at every event gives R_mn = lambda g_mn with lambda constant; for n >= 3 pointwise proportionality already forces constancy.: Polarization on the unit hyperboloid gives R_mn = f g_mn; contracted Bianchi identity gives (1 - n/2) d_n f = 0, so f is constant when n differs from 2. → Correct, including the reworded pointwise sentence.
- lambda c^2 = 1e-35 s^-2 sets about 4.5 Gyr for ten-percent growth.: python3: 1.1e-52 m^-2 times c^2 = 9.89e-36 s^-2; acosh(1.1)/sqrt(9.89e-36) = 1.41e17 s = 4.47 Gyr. → Correct.
- Kretschmann scalar 48 G^2 M^2 / c^4 r^6 outside a non-rotating star is nonzero and grows as r^-6 inward.: Schwarzschild K = 48 M^2/r^6 with M -> GM/c^2; units inverse length to the fourth. → Correct.
- GOCE: radial gradient -2740 E, horizontal +1370 E at r = 6626 km, sum zero within a few hundredths of an eötvös; dark energy -1e-26 E more than twenty powers of ten below.: python3: 2GM/r^3 = 2.740e-6 s^-2 = 2740 E; Lambda c^2 = 9.9e-27 E; ratio to 1e-2 E is 24 powers of ten. GOCE trace noise of order ten milli-eötvös in band, so 'a few hundredths of an eötvös' is a conservative true bound. → Correct.
