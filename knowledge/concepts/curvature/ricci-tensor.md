---
type: "concept"
schema_version: 2
id: "ricci-tensor"
title: "Ricci tensor"
tagline: "The total of the tidal drifts in a small falling ball of crumbs"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 4
updated: "2026-09-13"
aliases: ["Ricci curvature", "Ricci curvature tensor"]
prerequisites: ["riemann-curvature-tensor", "tensor-contraction", "symmetries-of-the-riemann-tensor", "poisson-equation-for-gravity", "riemann-curvature-operator"]
leads_to: ["ricci-scalar", "einstein-tensor", "contracted-bianchi-identity", "weyl-tensor", "ricci-flat-spacetime", "volume-preserving-tidal-deformation", "raychaudhuri-equation", "relativistic-tidal-tensor"]
visuals: ["falling-ring-of-crumbs", "six-entry-curvature-table"]
---

# Ricci tensor

*The total of the tidal drifts in a small falling ball of crumbs*

`ricci-tensor` · curvature · core · physics-reviewed (revision 4)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[tensor-contraction]] (working) · [[symmetries-of-the-riemann-tensor]] (working) · [[poisson-equation-for-gravity]] (working) · [[riemann-curvature-operator]] (formal)  
**Opens:** [[ricci-scalar]] · [[einstein-tensor]] · [[contracted-bianchi-identity]] · [[weyl-tensor]] · [[ricci-flat-spacetime]] · [[volume-preserving-tidal-deformation]] · [[raychaudhuri-equation]] · [[relativistic-tidal-tensor]]  
**Related:** [[kretschmann-scalar]] · [[curvature-sign-conventions]] · [[vacuum-einstein-equations]] · [[ricci-focusing-versus-weyl-shear]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[six-entry-curvature-table]]

> Let go of a small ball of crumbs, at rest in a cabin that falls freely near a planet, with nothing among them. Tidal drift pulls the ball longer along the line toward the planet's centre and narrower across it. Add the drifts along those three directions and they add to zero, so at first the room the ball takes up does not change. Where dust fills the space among the crumbs, the drifts no longer add to zero, and the ball starts to shrink. The Ricci tensor is the table that holds this total.

## You will be able to

**Entry**
- Explain why the three tidal drifts in a falling ball of crumbs add up to zero near a planet, with nothing among the crumbs. Say what that zero total means for the room the ball takes up. `objectives/explain-the-total-of-the-drifts` ← `checks/egg-keeps-its-volume`, `checks/zero-total-is-not-flat`, `problems/missing-drift-near-the-moon`
- Predict how a small ball of crumbs among evenly spread dust starts to shrink, and how that changes with the dust. `objectives/predict-shrinking-among-matter` ← `checks/denser-dust-faster`

**Working**
- Compute Ricci components from Riemann components, including a table whose Ricci components vanish while its Riemann components do not. `objectives/compute-ricci-components` ← `checks/vacuum-table-with-zero-ricci`
- Use the initial volume law to estimate how fast a ball of free particles released at rest loses volume. `objectives/use-the-initial-volume-law` ← `problems/water-density-dust-ball`
- Find the Ricci contraction along an observer's four-velocity from density, pressure and the cosmological constant. `objectives/relate-ricci-to-matter` ← `checks/tunnel-through-the-earth`, `problems/accelerating-universe-focusing`

**Formal**
- Prove that the Ricci tensor of the Levi-Civita connection is symmetric and is its only independent single contraction. `objectives/prove-symmetry-and-uniqueness` ← `checks/every-trace-is-ricci`
- State the hypotheses of the initial volume law, and show how shear changes volume where Ricci vanishes. `objectives/state-limits-of-the-volume-law` ← `checks/sheared-ball-loses-volume`
- Prove that the tidal traces measured by all freely falling observers at an event fix the Ricci tensor there. `objectives/prove-observer-traces-fix-ricci` ← `problems/all-observers-zero-trace`

## Ways in

### 1. Add up the three drifts · entry · picture

*A small falling ball of crumbs is pulled longer one way and narrower the other two. What single number says whether the room it takes up starts to change?*

**Recap:** A cabin falls freely when nothing but gravity acts on it: no air pushing, no floor or rope holding it. Let go of crumbs inside such a cabin near a round planet, each at rest relative to the cabin. Compared with a crumb at their centre, they slowly drift. Along the line toward the planet's centre they drift apart. Across that line they drift together, half as far. This is called tidal drift. The Riemann curvature tensor, or curvature table for short, is a table kept at every place that describes the curving there. Some of its entries give these drifts.

Picture a cabin falling freely down a tall tower on Earth, with the air pumped out. You float inside and let go of seven crumbs at once, each at rest relative to the cabin. One sits at the centre. Two sit 1 metre from that centre crumb along the line toward Earth's centre, one on each side of it. Four more sit 1 metre from the centre crumb across that line, two in each of two directions at right angles to each other. The six outer crumbs mark a small ball around the centre crumb. You time them with the cabin's clock and measure them with a ruler fixed to the cabin.

Now watch the six outer crumbs, each compared with the centre crumb. In the first 10 seconds, each crumb along the line drifts away from the centre crumb by about 15 hundredths of a millimetre. Each crumb across the line drifts toward the centre crumb by half as far, 7 and a half hundredths. Both distances are about the width of a hair or two, so nobody notices them.

Why those two sizes? Gravity weakens with the square of the distance, and squaring doubles a small share: 1.0001 times 1.0001 is just over 1.0002. Earth's centre is 6371 kilometres away, so a step of 1 metre toward it strengthens the pull by 2 parts in 6 371 000. The crumb nearer Earth's centre is pulled that much harder than the centre crumb, and the one farther away that much less. So both of them drift away from the centre crumb. A crumb across the line stays the same distance from Earth's centre, so it is pulled just as hard. But it is pulled toward Earth's centre, not toward the centre crumb. Sitting 1 metre to the side tilts that pull by 1 metre in 6371 kilometres. So 1 part in 6 371 000 of the pull aims toward the centre crumb. That is half the share the crumbs along the line feel, so the drift across the line is half as far.

Now take one crumb in each of three directions at right angles and add their drifts. Count a drift away from the centre crumb as positive, and a drift toward it as negative. The drift along the line is plus 15 hundredths of a millimetre, and the two drifts across that line are minus 7 and a half hundredths each. So the total is zero.

Why add them? The ball of crumbs grows longer along the line and narrower across it, so it turns into an egg shape. The room a shape takes up is called its volume. For small changes, write each change of length as a fraction of the length it belongs to. Do that for the ball's length and for its two widths. The change in the room the ball takes up is the sum of those three fractions. Every crumb started 1 metre from the centre crumb, so each drift divided by that metre is one of the three fractions. The three fractions add to zero, so at first the room the ball takes up does not change.

The words "at first" matter. Let go of fresh crumbs at any later moment, and their drifts still add to zero. But the crumbs you let go at the start are now moving. They keep stretching the ball along the line toward Earth's centre, and keep narrowing it across that line. Take on trust that this ongoing motion, by itself, slowly shrinks the room the ball takes up. A satellite flying above Earth measured these drifts for four years and found their total zero within its accuracy.

Adding up entries of the curvature table in this way gives a smaller table. It is called the Ricci tensor, and it holds enough numbers to give that total for a cabin moving in any way.

**Try it:** Shape a block of modelling clay 10 centimetres long, 2 centimetres wide and 2 centimetres deep. Press gently along its top and its sides with a flat ruler, pushing clay toward the ends, until it is 11 centimetres long with square sides. Measure its width and depth with a ruler marked in millimetres: each is now about 1.9 centimetres. The length grew by a tenth, and each width shrank by about a twentieth. A tenth minus a twentieth minus a twentieth is zero, and the room the clay takes up never changed.

**Takeaway:** Add the tidal drifts of a small falling ball of crumbs along three directions at right angles. That total says whether the room the ball takes up starts to change, and the Ricci tensor is the table that holds that total.

*Builds on:* [[riemann-curvature-tensor]], [[tidal-force]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/egg-keeps-its-volume`

### 2. Among dust, the ball starts to shrink · entry · contrast

*What makes the three drifts in a small falling ball of crumbs add up to something other than zero?*

**Recap:** Let go of crumbs in a cabin that falls freely, each at rest relative to the cabin, so that they mark a small ball around a centre crumb. Near a round planet, with nothing among the crumbs, they drift away from the centre crumb along the line toward the planet's centre. Across that line they drift toward the centre crumb, half as far. Take one crumb in each of three directions at right angles and add those drifts, counting a drift away from the centre crumb as positive. The total is zero, so at first the room the ball takes up does not change. The Ricci tensor is the table that holds that total.

Far from any planet, picture a huge round cloud of fine dust, spread evenly. A small ball of crumbs, 4 metres across, sits at the middle of the cloud, with one crumb at its centre. Dust fills the space among the crumbs. Let go of everything at once, every grain and every crumb at rest relative to each other, so all of it falls freely.

The dust pulls on the crumbs. Two facts about an evenly spread round cloud help here, both taken on trust. All the dust farther from the middle than a crumb pulls that crumb from every side, and those pulls cancel. The dust nearer the middle than a crumb pulls that crumb as if all of that dust sat at the middle.

So compare a crumb 1 metre from the middle with a crumb 2 metres out. The farther crumb has 8 times as much dust nearer the middle than it, because a ball twice as wide holds 2 times 2 times 2 times as much. That dust pulls from twice as far away, and gravity weakens with the square of distance, so each bit of it pulls 4 times less. Since 8 divided by 4 is 2, the farther crumb is pulled twice as hard.

The same counting works in every direction. Each crumb is pulled toward the middle in proportion to how far out it sits, so the ball stays round while it starts to shrink. All three drifts now point toward the centre crumb, so their total is not zero.

Denser dust pulls harder. Put twice as much dust in each cubic metre and every drift doubles. Making the cloud wider changes nothing: the extra dust lies farther out than the crumbs, and its pulls cancel. So the total counts only what is there among the crumbs, and nothing farther out. Einstein's theory of gravity ties the Ricci tensor at each place to the matter at that same place.

Suppose the dust is as dense as water. In the first 10 seconds, a crumb 1 metre from the middle drifts toward the middle by 14 thousandths of a millimetre, far too little to see. Yet nothing holds the dust apart, so the whole cloud falls in to its middle in about 35 minutes, however wide it is. A wider cloud pulls its dust harder, but that dust also has farther to fall, and the two changes balance exactly.

**Takeaway:** Dust, water or rock among the crumbs gives each crumb an extra drift toward the centre crumb. So the total is no longer zero, and a falling ball of crumbs starts to shrink. The denser that matter, the bigger the total.

*What this leaves out:* Einstein's theory also gives empty space itself a tiny total of its own, one that spreads the crumbs apart rather than drawing them together. It beats the matter's total only where each cubic metre holds less mass than about 7 hydrogen atoms.

*Continues:* `ways_in/add-up-the-three-drifts`<br>*Builds on:* [[tidal-force]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/denser-dust-faster`

### 3. The total is a trace of the Riemann tensor · working · calculation

*Which contraction of the Riemann tensor gives the total of the drifts, and how does that total set the volume of a small ball?*

The drifts added up in "Add up the three drifts" are Riemann components, and their total has a name in index notation. First turn a drift into an acceleration: a particle released at rest that drifts a distance $d$ in a short time $t$ has relative acceleration $2d/t^2$. So 0.154 mm in 10 s, at 1 m from the centre crumb, is $3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$ per metre of separation.

Give a freely falling observer with four-velocity $u^\mu$ an orthonormal frame whose spatial axes are held fixed by gyroscopes. Taken on trust here, the geodesic deviation equation gives the separation $\xi$ of a neighbouring free particle:

$$\ddot\xi^{\hat\imath} = -E_{ij}\,\xi^{\hat\jmath},\qquad E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}.$$

Exchanging the index pairs of the lowered Riemann tensor leaves it unchanged, so $E$ is symmetric, with three orthogonal eigen-directions and eigenvalues $\lambda_i$. A positive $\lambda_i$ draws that direction inward. The total of the drifts, counted as relative accelerations per unit separation, is therefore $-\sum_i\lambda_i$. Since $R^{\hat 0}{}_{\hat 0\hat 0\hat 0} = 0$, the eigenvalue sum runs over all four frame indices, which turns it into a contraction of the upper index with the third slot:

$$\sum_i\lambda_i = c^2R^\rho{}_{\hat 0\rho\hat 0} = R_{\mu\nu}u^\mu u^\nu,\qquad R_{\mu\nu} \equiv R^\rho{}_{\mu\rho\nu}.$$

That last definition fixes the Ricci tensor in every basis. Pair exchange makes it symmetric, so in four dimensions it holds 10 independent components. No other single trace is new: the first two lowered slots are antisymmetric, so tracing them gives zero, and tracing the upper index against the fourth slot gives $-R_{\mu\nu}$.

Now the volume. Lay the edges of a small box of particles along the eigen-directions, every particle at rest relative to the centre at $\tau = 0$. Each edge obeys $\ddot L_i = -\lambda_iL_i$, so $L_i \approx L_i(0)\big(1 - \tfrac12\lambda_i\tau^2\big)$. The volume is the product of the edges, and small fractional changes add:

$$\delta V(\tau) = \delta V(0)\Big(1 - \tfrac12R_{\mu\nu}u^\mu u^\nu\,\tau^2\Big) + O(\tau^3).$$

A positive $R_{\mu\nu}u^\mu u^\nu$ therefore makes the ball start to shrink.

Outside a spherical mass $M$ the eigenvalues are $(GM/r^3)(-2, 1, 1)$, which sum to zero. At Earth's surface that means particles 1 m apart accelerate apart at $3.08\times10^{-6}\ \mathrm{m\,s^{-2}}$ along the radius and together at $1.54\times10^{-6}\ \mathrm{m\,s^{-2}}$ across it, so the volume holds to order $\tau^2$. The Riemann tensor there is not zero, so a vanishing Ricci tensor does not mean flat spacetime.

**Takeaway:** Tracing the Riemann tensor's upper index against its third slot gives the symmetric Ricci tensor; contracted twice with an observer's four-velocity it is the trace of the tides, which sets a small ball's initial volume change.

*What this leaves out:* Keeps the volume change to second order in proper time, for particles released at rest relative to each other.

*Continues:* `ways_in/add-up-the-three-drifts`<br>*Builds on:* [[riemann-curvature-tensor]], [[tensor-contraction]], [[symmetries-of-the-riemann-tensor]]<br>*See:* `derivations/volume-law-from-deviation`, `worked_examples/ricci-tensor-of-a-sphere`, `checks/vacuum-table-with-zero-ricci`

### 4. A gradiometer reads the trace · working · operational

*What does a gravity gradiometer measure of the Ricci tensor, and what sets the value it reads?*

The trace in "The total is a trace of the Riemann tensor" can be read by an instrument. A gravity gradiometer carries pairs of accelerometers a short distance apart along three orthogonal axes. Each pair's difference in readings, divided by its separation, gives one entry of the tidal matrix. In a static weak field with Newtonian potential $\Phi$ that matrix is $c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \partial_i\partial_j\Phi$, so for an observer at rest, with $x^0 = ct$, its trace and Poisson's equation give

$$c^2R_{00} \approx \nabla^2\Phi = 4\pi G\rho.$$

The sum of the three diagonal gravity gradients therefore measures the mass density at the instrument. In "Among dust, the ball starts to shrink" each direction contributes $\tfrac{4\pi}{3}G\rho$, and three of them make this sum. Outside matter the sum is zero, which is Laplace's equation.

One satellite carried such an instrument for four years, about 255 km above Earth and lower near the end. For a spherical Earth at $r = 6626$ km the gradient along the radius is $-2GM/r^3 = -2.74\times10^{-6}\ \mathrm{s^{-2}}$ and each horizontal gradient is $+1.37\times10^{-6}\ \mathrm{s^{-2}}$. The satellite turns once per orbit, at rate $\Omega$, and that rotation adds $-2\Omega^2$ to the raw diagonal sum, which is $-2.74\times10^{-6}\ \mathrm{s^{-2}}$ again because $\Omega^2 = GM/r^3$ on a circular orbit. With the rotation removed, the measured gradients sum to zero within the instrument's noise, as Laplace's equation requires.

In full general relativity, Einstein's equation, taken on trust here, ties the Ricci tensor to the matter at the same event. For an observer at rest in a perfect fluid of mass density $\rho$ and pressure $p$, with cosmological constant $\Lambda$,

$$R_{\mu\nu}u^\mu u^\nu = 4\pi G\Big(\rho + \frac{3p}{c^2}\Big) - \Lambda c^2.$$

Pressure focuses as well, entering three times over, and a positive $\Lambda$ defocuses. Today $\Lambda c^2 \approx 1\times10^{-35}\ \mathrm{s^{-2}}$, smaller than the tidal gradients near Earth by about 30 orders of magnitude and far below any gradiometer's reach.

**Takeaway:** The diagonal sum of gravity gradients reads the Ricci contraction: four pi G times the local density in a weak field, zero outside matter, with pressure and the cosmological constant added in general relativity.

*What this leaves out:* Uses a static weak field for the gradiometer relation and a perfect fluid for the matter relation.

*Continues:* `ways_in/the-total-is-a-trace`, `ways_in/crumbs-among-dust-draw-together`<br>*Builds on:* [[newtonian-tidal-tensor]], [[poisson-equation-for-gravity]]<br>*See:* `observations/goce-zero-trace`, `checks/tunnel-through-the-earth`, `problems/accelerating-universe-focusing`

### 5. Ricci as a trace, and what it controls · formal · structure

*What is the Ricci tensor without coordinates, what determines it, and exactly what does it say about volumes?*

The trace in "The total is a trace of the Riemann tensor" has a coordinate-free form. Set $G = c = 1$. For a connection $\nabla$ with curvature operator $\mathcal R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$, define

$$\mathrm{Ric}(Y,Z) = \operatorname{tr}\big(X \mapsto \mathcal R(X,Z)Y\big),$$

with components $R_{\sigma\nu} = R^\rho{}_{\sigma\rho\nu}$. A trace of a linear map needs no metric, so $\mathrm{Ric}$ exists for any affine connection. Its symmetry does not come free. Pair exchange $R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$ follows from first-pair antisymmetry, which needs $\nabla g = 0$, together with the cyclic identity, which needs zero torsion. For the Levi-Civita connection $\mathrm{Ric}$ is symmetric; for a general affine connection it need not be.

*Uniqueness.* For Levi-Civita, every contraction of one pair of Riemann indices is $0$ or $\pm\mathrm{Ric}$. The first lowered pair is antisymmetric, so $g^{\rho\sigma}R_{\rho\sigma\mu\nu} = 0$; the last pair is antisymmetric, so tracing the upper index against the fourth slot gives $-R_{\sigma\mu}$; pair exchange carries the remaining traces onto these.

*Sectional sums.* On a Riemannian manifold with orthonormal basis $\{e_1, \dots, e_n\}$, $\mathrm{Ric}(e_1,e_1) = \sum_{i\ge2}K(e_1,e_i)$. In spacetime a unit timelike $u$ with orthonormal spatial $e_i$ has $\mathrm{Ric}(u,u) = -\sum_iK(u,e_i)$, because the denominator in the course definition of $K$ is negative on timelike planes. The behaviour matches in both cases: positive $\mathrm{Ric}$ along a geodesic's tangent makes neighbouring geodesics converge on average.

*What fixes it.* A symmetric tensor is determined by its values on the open cone of timelike vectors, by a short polarization argument. So $\mathrm{Ric} = 0$ at an event exactly when every freely falling observer there measures tides of zero trace.

*Volumes.* In Riemannian normal coordinates at $p$, $\sqrt{\det g} = 1 - \tfrac16R_{ij}x^ix^j + O(x^3)$, so positive Ricci curvature in a direction thins the volume element along it. For a timelike geodesic congruence with $B_{\mu\nu} = \nabla_\nu u_\mu$, expansion $\theta = B^\mu{}_\mu$, shear $\sigma_{\alpha\beta}$ and rotation $\omega_{\alpha\beta}$, commuting covariant derivatives gives $u^\lambda\nabla_\lambda B_{\mu\nu} = -B_{\mu\lambda}B^\lambda{}_\nu - R_{\sigma\mu\lambda\nu}u^\sigma u^\lambda$. Its trace is the Raychaudhuri equation,

$$\frac{d\theta}{d\tau} = -\frac{\theta^2}{3} - \sigma_{\alpha\beta}\sigma^{\alpha\beta} + \omega_{\alpha\beta}\omega^{\alpha\beta} - R_{\mu\nu}u^\mu u^\nu,$$

where $\theta = d\ln\delta V/d\tau$. With expansion, shear and rotation all zero at release it returns $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$, the initial volume law.

*Limits.* That law speaks about one instant. A trace-free tide builds shear, and shear then drives $\theta$ negative, so even where $\mathrm{Ric} = 0$ a ball holds its volume only through order $\tau^3$. The sign of $R_{\mu\nu}u^\mu u^\nu$ is pure geometry until Einstein's equation sets it to $4\pi(\rho + 3p) - \Lambda$ for an observer at rest in a perfect fluid. With $\Lambda = 0$ it is non-negative for every observer exactly when the matter obeys the strong energy condition, the input of the timelike focusing theorems.

*Dimension.* In two dimensions $R_{\mu\nu} = \tfrac12Rg_{\mu\nu}$, so $\mathrm{Ric}$ carries the whole Riemann tensor. In three dimensions $\mathrm{Ric}$ and $g$ still determine it. In four, Riemann's 20 independent components split into the 10 of $\mathrm{Ric}$ and the 10 of the trace-free Weyl tensor, which $\mathrm{Ric}$ cannot see.

**Takeaway:** Ricci is the trace of the curvature operator, symmetric for the Levi-Civita connection and fixed by every observer's tidal trace; it sets initial volume change through the Raychaudhuri equation, while shear and Weyl lie beyond it.

*What this leaves out:* Takes the commutator step of the Raychaudhuri equation from the Ricci identity without writing it out.

*Continues:* `ways_in/the-total-is-a-trace`<br>*Builds on:* [[riemann-curvature-operator]], [[levi-civita-connection]]<br>*See:* `checks/every-trace-is-ricci`, `checks/sheared-ball-loses-volume`, `problems/all-observers-zero-trace`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tidal drift | — | The slow drift of neighbouring freely falling objects apart or together, because gravity pulls them slightly differently. Outside a round planet they drift apart along the line toward its centre and together across it. | [[tidal-force]] |
| volume | — | The amount of room something takes up. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every place that describes the curving there. Some of its entries give how crumbs let go in a freely falling cabin drift. | [[riemann-curvature-tensor]] |
| Ricci tensor | REE-chee | A smaller table made from the Riemann curvature tensor by adding up entries. For a cabin moving in any way, it gives the total of the drifts of a small ball of crumbs let go at rest there. That total says whether the room the ball takes up starts to change. | [[ricci-tensor]] |

## Key equations

### Ricci tensor as a contraction · working

$$
R_{\mu\nu} = R^\rho{}_{\mu\rho\nu},\qquad R_{\mu\nu} = R_{\nu\mu}
$$

The Ricci tensor is the Riemann tensor with its upper index traced against its third slot; pair exchange makes it symmetric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu}$ | Ricci tensor | the Ricci tensor |
| $R^\rho{}_{\mu\rho\nu}$ | Riemann tensor in the course convention, traced on its first and third indices | the Riemann tensor, traced |

**Holds when:** Definition for any connection; symmetry holds for the torsion-free, metric-compatible connection of general relativity.  
**Say it:** “R mu nu is the Riemann tensor with its upper index traced against its third slot, and it is symmetric.”  
**Justified by:** `symmetries-of-the-riemann-tensor`

### Ricci as the trace of the tides · working

$$
R_{\mu\nu}u^\mu u^\nu = c^2\sum_i R^{\hat\imath}{}_{\hat 0\hat\imath\hat 0}
$$

Contracted twice with an observer's four-velocity, the Ricci tensor is the diagonal sum of that observer's tidal matrix.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $u^\mu$ | four-velocity of the freely falling observer, with $u_\mu u^\mu = -c^2$ | the four-velocity |
| $R^{\hat\imath}{}_{\hat 0\hat\imath\hat 0}$ | Riemann components in the observer's orthonormal frame | the tidal entries |

**Holds when:** Orthonormal frame with its time leg along $u/c$; any spacetime.  
**Say it:** “The Ricci tensor contracted twice with the four-velocity equals c squared times the sum of the diagonal tidal entries.”  
**Justified by:** `derivations/volume-law-from-deviation`

### Initial volume law · working

$$
\left.\frac{d^2\,\delta V}{d\tau^2}\right|_{\tau=0} = -R_{\mu\nu}u^\mu u^\nu\,\delta V
$$

A small ball of free particles released at rest starts to lose volume at a rate set by the Ricci tensor along its motion.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\delta V$ | volume of the small ball | the small volume |
| $\tau$ | proper time of the central particle | proper time |

**Holds when:** Ball small compared with the curvature scale; every particle at rest relative to the centre at $\tau = 0$; valid at that instant only.  
**Say it:** “The second proper-time derivative of a small volume, at release, is minus the Ricci tensor contracted twice with the four-velocity, times the volume.”  
**Justified by:** `derivations/volume-law-from-deviation`

### Weak-field time-time component · working

$$
R_{00} \approx \frac{1}{c^2}\nabla^2\Phi = \frac{4\pi G\rho}{c^2}
$$

In a weak static field the time-time Ricci component is the Laplacian of the Newtonian potential, which Poisson's equation sets by the mass density.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Phi$ | Newtonian potential | the potential |
| $\rho$ | mass density at the point | the density |

**Holds when:** Static weak field, slow sources, $x^0 = ct$, pressure negligible.  
**Say it:** “R zero zero is about the Laplacian of the potential over c squared, which is four pi G rho over c squared.”  
**Justified by:** `poisson-equation-for-gravity`

### Focusing by a perfect fluid · working

$$
R_{\mu\nu}u^\mu u^\nu = 4\pi G\left(\rho + \frac{3p}{c^2}\right) - \Lambda c^2
$$

Einstein's equation sets the Ricci contraction for an observer at rest in a perfect fluid: density and pressure focus, a positive cosmological constant defocuses.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $p$ | pressure | the pressure |
| $\Lambda$ | cosmological constant | Lambda |

**Holds when:** Einstein's equation in the course convention, taken on trust; observer at rest in the fluid.  
**Say it:** “The Ricci tensor contracted twice with the fluid four-velocity is four pi G times density plus three pressure over c squared, minus Lambda c squared.”  
**Justified by:** `stated`

### Ricci tensor without coordinates · formal

$$
\mathrm{Ric}(Y,Z) = \operatorname{tr}\big(X \mapsto \mathcal R(X,Z)Y\big)
$$

The Ricci tensor is the trace of the linear map that the curvature operator makes from one vector slot.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal R(X,Z)$ | curvature operator, $\nabla_X\nabla_Z - \nabla_Z\nabla_X - \nabla_{[X,Z]}$ | the curvature operator |
| $\mathrm{Ric}$ | Ricci tensor | Ric |

**Holds when:** Any affine connection; symmetric in $Y, Z$ for the Levi-Civita connection.  
**Say it:** “Ric of Y and Z is the trace of the map sending X to the curvature operator of X and Z acting on Y.”  
**Justified by:** `stated`

## Derivations

### Volume of a small ball from the deviation equation · working

**Goal:** Show that a small ball of free particles released at rest has $\delta V(\tau) = \delta V(0)\big(1 - \tfrac12R_{\mu\nu}u^\mu u^\nu\tau^2\big) + O(\tau^3)$.

1. Work in the orthonormal frame of the central particle, with spatial axes held fixed by gyroscopes. The geodesic deviation equation gives $\ddot\xi^{\hat\imath} = -E_{ij}\xi^{\hat\jmath}$ with $E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$.
2. Pair exchange gives $R_{\hat\imath\hat 0\hat\jmath\hat 0} = R_{\hat\jmath\hat 0\hat\imath\hat 0}$, and raising a spatial index in an orthonormal frame changes no sign, so $E$ is symmetric with orthogonal eigenvectors and eigenvalues $\lambda_1, \lambda_2, \lambda_3$.
3. Take a small box with edges $L_i(0)$ along those eigenvectors, every particle at rest relative to the centre at $\tau = 0$. Along an eigenvector $\ddot L_i = -\lambda_iL_i$ with $\dot L_i(0) = 0$, so $L_i(\tau) = L_i(0)\big(1 - \tfrac12\lambda_i\tau^2\big) + O(\tau^3)$.
4. Multiply the three edges. Products of two $\tau^2$ terms are of order $\tau^4$, so $\delta V(\tau) = \delta V(0)\big(1 - \tfrac12(\lambda_1 + \lambda_2 + \lambda_3)\tau^2\big) + O(\tau^3)$.
5. The eigenvalue sum is the trace, $\sum_i\lambda_i = c^2\sum_iR^{\hat\imath}{}_{\hat 0\hat\imath\hat 0} = c^2R^\rho{}_{\hat 0\rho\hat 0}$, because $R^{\hat 0}{}_{\hat 0\hat 0\hat 0} = 0$ by antisymmetry in the last two slots.
6. With $u^\mu = c\,\delta^\mu{}_{\hat 0}$ in this frame, $c^2R^\rho{}_{\hat 0\rho\hat 0} = R_{\mu\nu}u^\mu u^\nu$. Differentiating the volume twice at $\tau = 0$ then gives $\ddot{\delta V}(0) = -R_{\mu\nu}u^\mu u^\nu\,\delta V(0)$.

**Result:** $\delta V(\tau) = \delta V(0)\big(1 - \tfrac12R_{\mu\nu}u^\mu u^\nu\tau^2\big) + O(\tau^3)$ for a small box released at rest; any small ball follows by filling it with such boxes.

## Worked examples

### Ricci tensor of a sphere · working

**Problem:** A sphere of radius $a$ has metric $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$ and, in the course convention, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. Find every component of $R_{\mu\nu}$ and the Ricci scalar.

1. Lower the index and exchange pairs: $R_{\theta\phi\theta\phi} = g_{\theta\theta}R^\theta{}_{\phi\theta\phi} = a^2\sin^2\theta$, so $R_{\phi\theta\phi\theta} = a^2\sin^2\theta$.
2. Raise with $g^{\phi\phi} = 1/(a^2\sin^2\theta)$: $R^\phi{}_{\theta\phi\theta} = 1$.
3. $R_{\theta\theta} = R^\theta{}_{\theta\theta\theta} + R^\phi{}_{\theta\phi\theta} = 0 + 1 = 1$, since a component with matching last two slots vanishes.
4. $R_{\phi\phi} = R^\theta{}_{\phi\theta\phi} + R^\phi{}_{\phi\phi\phi} = \sin^2\theta$.
5. $R_{\theta\phi} = R^\theta{}_{\theta\theta\phi} + R^\phi{}_{\theta\phi\phi} = 0$: the first term vanishes by antisymmetry in the first lowered pair, the second by antisymmetry in the last pair.
6. Compare with the metric: $R_{\mu\nu} = g_{\mu\nu}/a^2$, and $R = g^{\mu\nu}R_{\mu\nu} = 2/a^2$.

**Answer:** $R_{\theta\theta} = 1$, $R_{\phi\phi} = \sin^2\theta$, $R_{\theta\phi} = 0$, so $R_{\mu\nu} = g_{\mu\nu}/a^2$ and $R = +2/a^2$.

**Takeaway:** The components do not depend on $a$, but their ratio to the metric does; the positive Ricci scalar confirms the slot and sign conventions.

## Problems

### `missing-drift-near-the-moon` · entry · difficulty 1 · calculation

A cabin falls freely just above the Moon's surface, where there is no air. Crumbs are let go around a centre crumb, each at rest relative to the cabin, and no matter sits among them. In the first 10 seconds, each crumb 1 metre from the centre crumb across the line toward the Moon's centre drifts toward the centre crumb by 47 thousandths of a millimetre. That holds in both directions across that line. How far does a crumb 1 metre out along the line drift in those 10 seconds, and which way?

**Hints**

1. What do the three drifts add up to when no matter sits among the crumbs?

**Answer:** About 94 thousandths of a millimetre, away from the centre crumb.

**Must contain:** With no matter among the crumbs the three drifts add up to zero; The two drifts across the line add to 94 thousandths toward the centre crumb; The drift along the line is 94 thousandths outward

**Numeric:** drift along the line, positive outward = 0.094 mm (signed, ±5%)

**Solution**

1. No matter sits among the crumbs, so the three drifts along directions at right angles add up to zero.
2. The two directions across the line give 47 thousandths of a millimetre toward the centre crumb each, which is 94 thousandths toward it in all.
3. So the drift along the line is 94 thousandths of a millimetre outward, twice each drift across, the same pattern as near Earth.

### `water-density-dust-ball` · working · difficulty 2 · estimate

A pressureless ball of dust with the density of water, $\rho = 1000\ \mathrm{kg\,m^{-3}}$, is released at rest far from other matter. Find $R_{\mu\nu}u^\mu u^\nu$ for a grain at its centre, and use the initial volume law to estimate the fraction of a small central ball's volume lost after 60 s.

**Hints**

1. For dust at rest with no cosmological constant, the focusing term is $4\pi G\rho$.

**Answer:** $R_{\mu\nu}u^\mu u^\nu = 8.39\times10^{-7}\ \mathrm{s^{-2}}$, and the volume falls by about $1.5\times10^{-3}$, or 0.15 per cent, in 60 s.

**Must contain:** R contracted with u twice is 4 pi G rho, 8.39e-7 per second squared; The volume falls by half of that times t squared, 1.5e-3 after 60 s

**Numeric:** fraction of volume lost after 60 s = 0.00151 1 (magnitude, ±3%)

**Solution**

1. For dust at rest with $\Lambda = 0$, $R_{\mu\nu}u^\mu u^\nu = 4\pi G\rho = 4\pi(6.674\times10^{-11})(1000) = 8.39\times10^{-7}\ \mathrm{s^{-2}}$.
2. The volume law gives $\delta V/\delta V_0 = 1 - \tfrac12(8.39\times10^{-7}\ \mathrm{s^{-2}})(60\ \mathrm s)^2 = 1 - 1.51\times10^{-3}$.
3. Newtonian check: a grain at radius $r$ starts with $\ddot r = -\tfrac{4\pi}{3}G\rho\,r$, so $r \approx r_0(1 - \tfrac{2\pi}{3}G\rho t^2)$ and $V \approx V_0(1 - 2\pi G\rho t^2)$, the same answer.
4. The law gives only the first term at release; the full collapse, in about 35 minutes, needs the nonlinear evolution.

### `accelerating-universe-focusing` · working · difficulty 2 · calculation

For the spatially flat expanding universe $ds^2 = -c^2dt^2 + a(t)^2(dx^2 + dy^2 + dz^2)$, show that a comoving observer has $R_{\mu\nu}u^\mu u^\nu = -3\ddot a/a$. Today the Hubble rate is $H_0 = 67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ and the deceleration parameter is $q_0 = -\ddot aa/\dot a^2 \approx -0.53$. Find $R_{\mu\nu}u^\mu u^\nu$ and say what its sign means for free particles momentarily at rest relative to each other.

**Hints**

1. With $x^0 = ct$, the nonzero Christoffel symbols are $\Gamma^0{}_{ij} = a\dot a\,\delta_{ij}/c$ and $\Gamma^i{}_{0j} = (\dot a/ac)\,\delta^i{}_j$.
2. Write $-3\ddot a/a$ as $3q_0H_0^2$.

**Answer:** $R_{\mu\nu}u^\mu u^\nu = -3\ddot a/a = 3q_0H_0^2 \approx -1.6H_0^2 \approx -7.6\times10^{-36}\ \mathrm{s^{-2}}$. It is negative, so such particles accelerate apart: the Ricci term defocuses.

**Must contain:** R zero zero equals minus three a double dot over a c squared; The contraction is 3 q0 H0 squared, about minus 7.6e-36 per second squared; Negative means defocusing, which ordinary matter alone cannot give

**Numeric:** Ricci contraction divided by H0 squared = -1.58 1 (signed, ±5%)

**Solution**

1. With $x^0 = ct$ and $\dot a = da/dt$, the nonzero Christoffel symbols are $\Gamma^0{}_{ij} = a\dot a\,\delta_{ij}/c$ and $\Gamma^i{}_{0j} = \Gamma^i{}_{j0} = (\dot a/ac)\,\delta^i{}_j$.
2. $R_{00} = R^i{}_{0i0}$, since $R^0{}_{000} = 0$. With $\Gamma^\lambda{}_{00} = 0$, the course formula leaves $R^i{}_{0i0} = -\partial_0\Gamma^i{}_{i0} - \Gamma^i{}_{0j}\Gamma^j{}_{i0}$.
3. $\partial_0\Gamma^i{}_{i0} = \tfrac1c\tfrac{d}{dt}\big(3\dot a/ac\big) = \tfrac{3}{c^2}\big(\ddot a/a - \dot a^2/a^2\big)$ and $\Gamma^i{}_{0j}\Gamma^j{}_{i0} = 3\dot a^2/a^2c^2$, so $R_{00} = -3\ddot a/ac^2$.
4. The comoving four-velocity is $u^\mu = (c, 0, 0, 0)$, so $R_{\mu\nu}u^\mu u^\nu = c^2R_{00} = -3\ddot a/a = 3q_0H_0^2$.
5. $H_0 = 67.4\ \mathrm{km\,s^{-1}}/(3.0857\times10^{19}\ \mathrm{km}) = 2.18\times10^{-18}\ \mathrm{s^{-1}}$, so $3q_0H_0^2 \approx -7.6\times10^{-36}\ \mathrm{s^{-2}}$.
6. The comoving tidal matrix is $c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} = -(\ddot a/a)\,\delta_{ij}$, so with $\ddot a > 0$ particles at rest relative to each other accelerate apart. Dust alone would give a positive contraction.

### `all-observers-zero-trace` · formal · difficulty 2 · proof

Let $S_{\mu\nu}$ be a symmetric tensor at a point of a Lorentzian manifold with $S_{\mu\nu}u^\mu u^\nu = 0$ for every timelike $u$. Prove $S_{\mu\nu} = 0$. Conclude that the tides measured by every freely falling observer at an event have zero trace exactly when $R_{\mu\nu} = 0$ there.

**Hints**

1. Perturb a timelike vector by a small multiple of an arbitrary vector.
2. A symmetric bilinear form is fixed by its quadratic form.

**Answer:** $S_{\mu\nu} = 0$, so Ricci-flatness at an event is the same as every freely falling observer there measuring tides of zero trace.

**Must contain:** Timelike vectors form an open set; Vanishing of a polynomial in epsilon on an interval kills each coefficient; Polarization recovers the bilinear form from the quadratic form

**Solution**

1. Fix a timelike $u$ and any vector $v$. Timelike vectors form an open set, so $u + \epsilon v$ is timelike for small $|\epsilon|$.
2. Then $0 = S(u + \epsilon v, u + \epsilon v) = 2\epsilon\,S(u,v) + \epsilon^2S(v,v)$ for all small $\epsilon$, using $S(u,u) = 0$ and symmetry.
3. A polynomial in $\epsilon$ that vanishes on an interval has zero coefficients, so $S(u,v) = 0$ and $S(v,v) = 0$ for every $v$.
4. Polarization, $S(v,w) = \tfrac14\big[S(v+w,v+w) - S(v-w,v-w)\big]$, then gives $S(v,w) = 0$ for all $v, w$.
5. An observer with four-velocity $u$ measures tides whose trace is $R_{\mu\nu}u^\mu u^\nu$, by the trace formula of "The total is a trace of the Riemann tensor". Those traces all vanish exactly when $R_{\mu\nu} = 0$.

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite** (measured, working). From 2009 to 2013 GOCE carried three orthogonal pairs of accelerometers and measured the tidal matrix $\partial_i\partial_j\Phi$ directly, from about 255 km above Earth and lower near the end. Its diagonal sum is $c^2R_{00}$ for an observer at rest in a weak field, and that vanishes outside matter. With the satellite's once-per-orbit rotation removed, the three measured diagonal gradients sum to zero within the instrument's noise, as Laplace's equation requires, for gradients varying with periods of about 10 to 200 s. *Numbers:* At $r = 6626$ km for a spherical Earth: $-2.74\times10^{-6}\ \mathrm{s^{-2}}$ along the radius and $+1.37\times10^{-6}\ \mathrm{s^{-2}}$ along each horizontal axis, summing to zero; the rotation adds $-2.74\times10^{-6}\ \mathrm{s^{-2}}$ to the raw sum. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **The accelerating expansion of the universe** (measured, working). For comoving observers in a spatially flat expanding universe, $R_{\mu\nu}u^\mu u^\nu = -3\ddot a/a$. Supernova distances and the cosmic microwave background give $\ddot a > 0$ today, so on the largest scales the Ricci term defocuses: free particles momentarily at rest relative to each other accelerate apart. In Einstein's equation that needs a positive cosmological constant, or a component with $\rho + 3p/c^2 < 0$. *Numbers:* With $H_0 = 67.4\ \mathrm{km\,s^{-1}\,Mpc^{-1}}$ and density fractions $\Omega_{\rm m} = 0.315$ and $\Omega_\Lambda = 0.685$: $q_0 = \Omega_{\rm m}/2 - \Omega_\Lambda = -0.53$ and $R_{\mu\nu}u^\mu u^\nu = 3q_0H_0^2 \approx -7.6\times10^{-36}\ \mathrm{s^{-2}}$. *Reference:* Nabila Aghanim, Yashar Akrami, Mark Ashdown, Jonathan Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Predict the volume** (entry). Take a prediction, then add the three drifts and test the box on a calculator. *Why:* The shape changes visibly, so an unchanged volume surprises. *Predict:* Tidal drift pulls the ball longer one way and narrower the other two ways. Does the room it takes up grow, shrink, or stay the same? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/add-up-the-three-drifts`, `checks/egg-keeps-its-volume`
2. **Fill the ball with dust** (entry). Put the same ball at the middle of an even dust cloud, and compare crumbs at two distances. *Why:* It isolates matter among the crumbs as what makes the total nonzero. *Predict:* If dust fills the space among the crumbs, what happens to the ball? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/crumbs-among-dust-draw-together`, `checks/denser-dust-faster`
3. **Name the trace** (working). Take the trace of the tidal matrix and recognize the contraction, then derive the volume law and calibrate the sign on a sphere. *Why:* Defining Ricci as the trace of something measured makes the choice of slots feel forced. *Uses:* `ways_in/the-total-is-a-trace`, `derivations/volume-law-from-deviation`, `worked_examples/ricci-tensor-of-a-sphere`
4. **Zero Ricci, real tides** (working). Contract the six-entry table with the Schwarzschild pattern, then work the tunnel through a uniform Earth. *Why:* Both show a vanishing trace beside real tides, blocking the flatness slogan. *Predict:* If every Ricci component is zero, must every curvature entry be zero? *Visual:* [[six-entry-curvature-table]] *Uses:* `checks/vacuum-table-with-zero-ricci`, `checks/tunnel-through-the-earth`
5. **Mark the limits** (formal). Give the coordinate-free trace, its uniqueness and Raychaudhuri, then run the sheared ball. *Why:* It blocks the slogan that zero Ricci means constant volume for good. *Predict:* Where the Ricci tensor is zero, does a small ball keep its volume for good? *Uses:* `ways_in/the-trace-of-the-curvature-operator`, `checks/every-trace-is-ricci`, `checks/sheared-ball-loses-volume`

## Misconceptions

### “If the drifts in a falling ball of crumbs add up to zero, space and time there are flat.” · entry · `zero-total-means-flat`

- **Why it is tempting:** A total of zero sounds as though nothing is happening.
- **What is true:** Every drift can be real while the drifts cancel in the total. Tidal drift near Earth shows that the curvature table is not zero there.
- **Exposed by:** `checks/zero-total-is-not-flat`, `checks/vacuum-table-with-zero-ricci`

### “If tidal drift pulls a ball of crumbs into an egg shape, the room it takes up must change too.” · entry · `shape-change-means-volume-change`

- **Why it is tempting:** Stretching something looks like making it bigger.
- **What is true:** Written as fractions, the changes in a length and two widths add up. Growing one way and shrinking the other two by half as much leaves the volume the same at first.
- **Exposed by:** `checks/egg-keeps-its-volume`

### “Inside a planet, even in an empty tunnel, the Ricci tensor cannot be zero: matter surrounds you.” · working · `matter-nearby-counts`

- **Why it is tempting:** The dust picture ties shrinking to matter, and a tunnel lies deep inside it.
- **What is true:** Through Einstein's equation the Ricci tensor answers only to the matter at that event, and to the cosmological constant. Surrounding rock changes the shape of the tides, not their trace.
- **Exposed by:** `checks/tunnel-through-the-earth`

### “Tracing a different pair of Riemann slots gives another independent curvature tensor.” · formal · `other-traces-give-new-tensors`

- **Why it is tempting:** A four-index tensor offers six pairs of slots to trace.
- **What is true:** For the Levi-Civita connection the Riemann symmetries make every other single trace zero, or plus or minus Ricci.
- **Exposed by:** `checks/every-trace-is-ricci`

### “Where the Ricci tensor vanishes, a small ball of free particles keeps its volume for good.” · formal · `volume-law-holds-forever`

- **Why it is tempting:** The slogan that Ricci changes volume and the rest changes shape is usually stated bare.
- **What is true:** The law fixes only the initial volume acceleration of a ball released with no expansion, shear or rotation. Shear built up by a trace-free tide reduces the volume later.
- **Exposed by:** `checks/sheared-ball-loses-volume`

## Checks

1. **Entry · predict** `checks/egg-keeps-its-volume`. In a cabin falling freely near Earth, crumbs are let go at the corners of a box with 1-metre edges, each crumb at rest relative to the cabin. The box is set square: four of its edges run along the line toward Earth's centre, and the other eight run across that line. After a while, each edge along that line has grown by 2 tenths of a millimetre. Each edge across it has shrunk by 1 tenth of a millimetre. Has the room the box takes up grown, shrunk, or stayed about the same?
   - **Hints:** Write each change as a fraction of 1 metre. / Add the three fractions, counting a shrinking edge as negative.
   - **Answer:** About the same. For small changes, write each edge's change as a fraction of that edge. The change in the room the box takes up is the sum of the three fractions, one for the length and one for each of the two widths. The edge along the line grew by 2 parts in 10,000, and each edge across it shrank by 1 part in 10,000. So the sum is 2 minus 1 minus 1, which is zero. A calculator agrees: 1.0002 times 0.9999 times 0.9999 is 0.99999997. The box changed shape, but the room it takes up changed by only 3 parts in 100 million.
   - **Must contain:** The room it takes up stays about the same; Written as fractions of the edges, the three changes add up; Plus 2, minus 1, minus 1 gives 0
   - **Numeric:** change in volume = 0 percent (signed, ±0.005)
   - **Targets:** `shape-change-means-volume-change`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · evaluate-claim** `checks/zero-total-is-not-flat`. In a cabin falling freely near Earth, a friend lets go of a small ball of crumbs at rest. She says: "The drifts add up to zero, so space and time here are not curved." Is she right?
   - **Hints:** Is each drift zero, or only their total?
   - **Answer:** No. The drifts add up to zero, but not one of them is zero. Crumbs along the line toward Earth's centre drift apart, and crumbs across that line drift together. That is tidal drift, and entries of the curvature table give it. Those entries are not zero, so space and time there are curved. The zero total says only this: at first the room the ball takes up does not change, while its shape does.
   - **Must contain:** She is wrong; Each drift is real; only the total is zero; Tidal drift means the curvature table is not zero
   - **Targets:** `zero-total-means-flat`
3. **Entry · numeric** `checks/denser-dust-faster`. A small ball of crumbs sits at the middle of a huge round cloud of dust as dense as water, far from any planet, and dust fills the space among the crumbs. Everything is let go at once, every grain and every crumb at rest relative to each other. In the first 10 seconds, a crumb 1 metre from the middle drifts toward the middle by 14 thousandths of a millimetre. How far does a crumb 2 metres out drift in those 10 seconds? How far would the 1-metre crumb drift in dust twice as dense?
   - **Hints:** How much more dust sits nearer the middle for the crumb twice as far out?
   - **Answer:** 28 thousandths of a millimetre in both cases. The crumb 2 metres out has 8 times as much dust nearer the middle, because a ball twice as wide holds 2 times 2 times 2 times as much. That dust pulls as if it sat at the middle, twice as far away, so each bit pulls 4 times less. Since 8 divided by 4 is 2, the pull doubles, and the drift with it. Dust twice as dense puts twice as much dust within 1 metre of the middle, so that drift doubles too.
   - **Must contain:** Both drifts are 28 thousandths of a millimetre; Twice as far out means 8 times the dust, each bit pulling 4 times less; Twice the density doubles it
   - **Numeric:** drift of the crumb 2 metres out = 0.028 mm (magnitude, ±5%); drift of the 1-metre crumb in dust twice as dense = 0.028 mm (magnitude, ±5%)
4. **Working · numeric** `checks/tunnel-through-the-earth`. Model Earth as a uniform ball of density $\rho = 5510\ \mathrm{kg\,m^{-3}}$ with a narrow empty tunnel through its centre. Near the centre, free particles are released at rest in the tunnel. Find $R_{\mu\nu}u^\mu u^\nu$ there, and the relative acceleration of two particles 1 m apart along the tunnel and across it.
   - **Hints:** Where is the density that enters Poisson's equation? / Treat the tunnel as a full ball minus a long cylinder.
   - **Answer:** $R_{\mu\nu}u^\mu u^\nu = 0$, because $\nabla^2\Phi = 4\pi G\rho = 0$ where the particles sit: the tunnel is empty. The tides are not zero. Superpose a full ball with a cylinder of the same density removed: the ball gives $\partial_i\partial_j\Phi = \tfrac{4\pi}{3}G\rho\,\delta_{ij}$ inside it, and a long cylinder gives $2\pi G\rho$ across its axis and $0$ along it. So along the tunnel the entry is $\tfrac{4\pi}{3}G\rho = 1.54\times10^{-6}\ \mathrm{s^{-2}}$ and the particles accelerate together at $1.54\times10^{-6}\ \mathrm{m\,s^{-2}}$; across it the entry is $-\tfrac{2\pi}{3}G\rho$ and they accelerate apart at $0.77\times10^{-6}\ \mathrm{m\,s^{-2}}$ in each of the two directions. The three add to zero: the surrounding rock changes the shape of the tides, not their trace.
   - **Must contain:** Zero, because no matter sits where the particles are; Along the tunnel: together at 1.54e-6 metres per second squared; Across: apart at half that
   - **Numeric:** relative acceleration along the tunnel, positive apart = -1.54e-06 m/s^2 (signed, ±3%); relative acceleration across the tunnel, positive apart = 7.7e-07 m/s^2 (signed, ±3%)
   - **Targets:** `matter-nearby-counts`
5. **Working · numeric** `checks/vacuum-table-with-zero-ricci`. In an orthonormal frame $(\hat t, \hat r, \hat\theta, \hat\phi)$, the only independent nonzero Riemann components are $R_{\hat a\hat b\hat a\hat b}$ for the pairs $tr, t\theta, t\phi, r\theta, r\phi, \theta\phi$, with values $q(-2, 1, 1, -1, -1, 2)$. Find the diagonal Ricci components and the Kretschmann scalar $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ in units of $q^2$.
   - **Hints:** Which Riemann components feed $R_{\hat t\hat t}$?
   - **Answer:** $R_{\hat b\hat d} = \eta^{\hat a\hat c}R_{\hat a\hat b\hat c\hat d}$, so the time index brings a minus sign. $R_{\hat t\hat t} = q(-2 + 1 + 1) = 0$. $R_{\hat r\hat r} = -R_{\hat t\hat r\hat t\hat r} + R_{\hat\theta\hat r\hat\theta\hat r} + R_{\hat\phi\hat r\hat\phi\hat r} = q(2 - 1 - 1) = 0$. Likewise $R_{\hat\theta\hat\theta} = q(-1 - 1 + 2) = 0$ and $R_{\hat\phi\hat\phi} = q(-1 - 1 + 2) = 0$; off-diagonal components vanish because no mixed pairs appear. Each pair appears in four index orders, and raising squares the signs, so the Kretschmann scalar is $4q^2(4 + 1 + 1 + 1 + 1 + 4) = 48q^2$: the Ricci tensor vanishes while the Riemann tensor does not. This is the Schwarzschild pattern with $q = GM/c^2r^3$.
   - **Must contain:** Every Ricci component is zero; The time index brings a minus sign into the contraction; The Kretschmann scalar is 48 q squared, so curvature remains
   - **Numeric:** Kretschmann scalar in units of q squared = 48 1 (magnitude, ±0.5); each diagonal Ricci component in units of q = 0 1 (signed, ±0.01)
   - **Targets:** `zero-total-means-flat`
   - **Visual:** [[six-entry-curvature-table]]
6. **Formal · derive** `checks/every-trace-is-ricci`. For the Levi-Civita connection, show that every contraction of one pair of indices of the Riemann tensor is zero or $\pm R_{\mu\nu}$, and that $R_{\mu\nu}$ is symmetric. Which steps fail for a connection with torsion, or one that does not preserve the metric?
   - **Hints:** List the antisymmetric index pairs, and the symmetry that swaps the pairs.
   - **Answer:** Use $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$. Tracing either antisymmetric pair gives $0$. The upper index with the third slot gives $R_{\sigma\nu}$ by definition, and with the fourth gives $R^\rho{}_{\sigma\nu\rho} = -R_{\sigma\nu}$. The second slot against the third gives $-R_{\rho\nu}$, and against the fourth $+R_{\rho\mu}$. Symmetry: $R_{\sigma\nu} = g^{\rho\lambda}R_{\lambda\sigma\rho\nu} = g^{\rho\lambda}R_{\rho\nu\lambda\sigma} = R_{\nu\sigma}$. Only last-pair antisymmetry holds for every connection: first-pair antisymmetry needs $\nabla g = 0$, and pair exchange needs the cyclic identity as well, which needs zero torsion. Without them the other traces are new tensors and Ric can have an antisymmetric part.
   - **Must contain:** Traces over an antisymmetric pair vanish; The remaining traces equal plus or minus Ricci; Symmetry uses pair exchange, which needs metric compatibility and zero torsion
   - **Targets:** `other-traces-give-new-tensors`
7. **Formal · evaluate-claim** `checks/sheared-ball-loses-volume`. Claim: "Where $R_{\mu\nu} = 0$, a small ball of free particles released at rest keeps its volume while it stays small." Test it where the tidal matrix $c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$ along the central worldline is constant, with eigenvalues $(-2, 1, 1)/\tau_0^2$.
   - **Hints:** Solve each axis separately, with zero initial rate. / Expand the product of the three lengths to fourth order.
   - **Answer:** The claim is false. With $s = \tau/\tau_0$, the first axis obeys $L'' = 2L$, so $L = L_0\cosh(\sqrt2\,s)$; the other two obey $L'' = -L$, so $L = L_0\cos s$. Hence $\delta V/\delta V_0 = \cosh(\sqrt2\,s)\cos^2s$, which expands to $1 - \tfrac12s^4 + O(s^6)$ and equals $0.971$ at $s = 0.5$ and $0.636$ at $s = 1$. The zero trace removes only the $s^2$ term. The tide builds shear, whose $-\sigma_{\mu\nu}\sigma^{\mu\nu}$ term in the Raychaudhuri equation drives the expansion negative. Ricci fixes only the volume acceleration at release, with $\theta = \sigma_{\mu\nu} = \omega_{\mu\nu} = 0$.
   - **Must contain:** The claim is false; Volume ratio is cosh of root two s times cos squared s, or 1 minus s to the fourth over 2; Shear drives the later loss of volume
   - **Numeric:** volume ratio at s = 1 = 0.636 1 (magnitude, ±1%)
   - **Targets:** `volume-law-holds-forever`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which Riemann slots are traced to form the Ricci tensor | $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, the upper index against the third slot, so a sphere of radius $a$ has $R_{\mu\nu} = g_{\mu\nu}/a^2$ and $R = +2/a^2$. | Some texts trace the upper index against the fourth slot, or use a Riemann tensor of opposite overall sign; either flips the sign of the Ricci tensor, and the two together cancel. Calibrate on the sphere. |
| Subtracting a quarter or a half of the trace | The Einstein tensor is $G_{\mu\nu} = R_{\mu\nu} - \tfrac12Rg_{\mu\nu}$, with trace $-R$ in four dimensions. The trace-free part $R_{\mu\nu} - \tfrac14Rg_{\mu\nu}$ is written out in full. | Some texts call the quarter version trace-reversed, or give it the Einstein tensor's letter. For a null vector $k$ both reduce to $R_{\mu\nu}k^\mu k^\nu$, which hides the difference in lensing. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The central picture: a small ball of freely falling crumbs whose drifts change its shape near a planet and its volume among dust. *Sketch:* This concept adds a ball mode: crumbs on a small sphere around a centre crumb, a translucent reference sphere, readouts of the three principal drifts, their total and the volume ratio, and a dust switch that fills the ball with matter of adjustable density. A time slider past the first seconds shows a trace-free tide slowly reducing the volume.
- [[six-entry-curvature-table]] (core): Shows nonzero curvature entries whose Ricci components all vanish. *Sketch:* This concept adds Ricci readouts that light up, with signs, the entries feeding each diagonal component, and a challenge to find a table with every Ricci component zero and some entry nonzero; the Schwarzschild preset is one answer.

## Tutor moves

**Open with**

- Picture a small ball of crumbs floating in a cabin that falls freely near Earth, with nothing but empty space among the crumbs. Tidal drift pulls it longer along the line toward Earth's centre and narrower across that line. Does the room the ball takes up grow, shrink, or stay the same? *(prediction)*

**If the learner is stuck**

- *The learner does not see why small changes of the edges add up to the volume change.* → Multiply out boxes with edges 1.001, 0.9995, 0.9995 and 1.01, 0.995, 0.995, then compare with the summed fractions. *Uses:* `ways_in/add-up-the-three-drifts`
- *The learner insists that matter around the particles must make the trace nonzero.* → Work the tunnel through a uniform Earth: a full ball minus a cylinder, then add the entries. *Uses:* `checks/tunnel-through-the-earth`

**Common questions**

- *If the drifts add up to zero near Earth, why is there any gravity there?* (entry) Each crumb still falls toward Earth, pulled by gravity. The zero total is about the drifts between neighbouring crumbs, not about the fall itself. Falling freely takes away the feeling of weight, but not those drifts. Near Earth every drift is real: crumbs along the line toward Earth's centre drift apart, and crumbs across that line drift together. Only their total is zero, so the room the ball takes up does not start to change. Other entries of the curvature table still give how the ball changes shape. *Uses:* `ways_in/add-up-the-three-drifts`, `checks/zero-total-is-not-flat`

**Switching levels**

- To working when: asks which curvature entries are added; uses indices. Go to the trace of the tidal matrix, then the table with zero Ricci. *Uses:* `ways_in/the-total-is-a-trace`, `checks/vacuum-table-with-zero-ricci`
- To formal when: asks whether the volume holds for good; asks for a definition without coordinates. Give the operator trace and the Raychaudhuri equation, then run the sheared ball. *Uses:* `ways_in/the-trace-of-the-curvature-operator`, `checks/sheared-ball-loses-volume`
- To research when: asks about Ricci flow, singularity theorems, or curvature bounds. Open the research horizon. *Uses:* `research_horizon/ricci-flow`, `research_horizon/focusing-and-singularities`

**Pronunciations:** Ricci → REE-chee; Riemann → REE-mahn; Ricci-Curbastro → REE-chee koor-BAHS-troh; Levi-Civita → LEH-vee CHEE-vee-tah; Raychaudhuri → ray-CHOWD-hoo-ree

**Voice notes:** At the entry rung say "the drifts add up to zero", not "Ricci vanishes".

## History

- **Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900).** Set out the absolute differential calculus, the index methods used for the Riemann tensor and its contractions; the contracted curvature tensor carries Ricci's name. Gregorio Ricci-Curbastro, Tullio Levi-Civita (1900), *Méthodes de calcul différentiel absolu et leurs applications*, Mathematische Annalen 54, 125–201, doi:10.1007/BF01454201
- **Albert Einstein (1915).** Earlier in November 1915 Einstein set a Ricci-type tensor proportional to the energy-momentum tensor, which forced the trace of that tensor to vanish. This paper of 25 November added the trace term and gave the final field equations. Albert Einstein (1915), *Die Feldgleichungen der Gravitation*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 844–847
- **Amal Kumar Raychaudhuri (1955).** Derived the evolution equation for the expansion of a family of free-fall worldlines, in which the Ricci tensor along the flow drives focusing. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123

## Research horizon

- **Ricci flow.** Hamilton's Ricci flow evolves a Riemannian metric by $\partial_tg_{ij} = -2R_{ij}$, contracting positively curved directions and smoothing curvature somewhat as heat flow smooths temperature. Perelman's control of its singularities completed the proofs of the Poincaré and geometrization conjectures. Richard S. Hamilton (1982), *Three-manifolds with positive Ricci curvature*, Journal of Differential Geometry 17, 255–306, doi:10.4310/jdg/1214436922; Grisha Perelman (2002), *The entropy formula for the Ricci flow and its geometric applications*, arXiv:math/0211159
- **Ricci curvature bounds without smoothness.** A lower bound on Ricci curvature controls how fast the volume of balls grows, and it can be restated through optimal transport as convexity of an entropy along transport paths. That restatement defines Ricci bounds on non-smooth metric measure spaces, and a Lorentzian version characterizes the strong energy condition. John Lott, Cédric Villani (2009), *Ricci curvature for metric-measure spaces via optimal transport*, Annals of Mathematics 169, 903–991, doi:10.4007/annals.2009.169.903; Karl-Theodor Sturm (2006), *On the geometry of metric measure spaces. I*, Acta Mathematica 196, 65–131, doi:10.1007/s11511-006-0002-8; Robert J. McCann (2020), *Displacement convexity of Boltzmann's entropy characterizes the strong energy condition from general relativity*, Cambridge Journal of Mathematics 8(3), 609–681, doi:10.4310/CJM.2020.v8.n3.a4
- **Focusing and singularity theorems.** Where $R_{\mu\nu}k^\mu k^\nu \ge 0$ for null $k$, as Einstein's equation gives for matter obeying the null energy condition, the Raychaudhuri equation forces converging light rays leaving a closed trapped surface to focus within a finite affine parameter. Penrose used this to show that a spacetime with a non-compact Cauchy surface and a closed trapped surface is null geodesically incomplete. Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** Let go of crumbs in a cabin falling freely near Earth and they drift: the ones along the line to Earth's centre spread apart, the ones across it come together by half as much, so the ball turns into an egg. Add the three drifts, plus 15 hundredths and two minus 7 and a halves of a millimetre, and you get zero, so the room the ball takes up does not change at first even though its shape does. That total is what the Ricci tensor keeps. I could not say why the sideways drift is exactly half; I was just handed the two numbers. If dust fills the space among the crumbs the ball shrinks instead, and denser dust shrinks it faster, because a crumb twice as far out has 8 times as much dust pulling from twice as far, and 8 divided by 4 is 2. I got lost where the ball is 2 metres across and then there is a crumb 2 metres out from the middle. And 'at rest' compared with what, the cabin? I also did not know whether 'the room it takes up' and the glossary's 'volume' were the same thing, and in 'Where dust fills the space among the crumbs, they no longer cancel' I first read 'they' as the crumbs.

**Stumbles (22)**

- “Let go of a small ball of crumbs at rest in a cabin falling freely near a planet”: At rest compared with what? The reader has no measurer for 'at rest', and the whole picture depends on the crumbs starting still in the cabin.
- “Tidal drift pulls the ball longer one way and narrower the other two.”: A direction with no reference: which way is 'one way'? The summary is read before any way, so nothing names it.
- “Where dust fills the space among the crumbs, they no longer cancel, and the ball starts to shrink.”: 'They' reads first as the crumbs, the nearest plural noun. 'Cancel' is also used later for the dust's pulls cancelling, so one word carries two ideas.
- “The Ricci tensor is the table that holds these totals.”: 'These totals' is plural, but the reader has met exactly one total, so they hunt for the others.
- “Crumbs let go at rest inside such a cabin near a round planet slowly drift.”: Drift compared with what, and measured by whom? Rule 7 asks for the measurer, and the sibling picture in the vault names the cabin's clock and ruler.
- “Two sit 1 metre from it along the line toward Earth's centre. Four more sit 1 metre from it across that line, in two directions at right angles to each other.”: A rule the reader cannot follow: where exactly do the two go, and how do four crumbs fill two directions? 'It' also has the centre crumb and the centre as candidates.
- “Why add them? The ball of crumbs grows longer along the line and narrower across it”: The reader was given seven crumbs, never a ball, so 'the ball of crumbs' arrives from nowhere.
- “Why those two sizes? The crumb nearer Earth's centre is pulled harder than the centre crumb, and the one farther away is pulled less, so both move away from it.”: The paragraph promises the two sizes and then explains only the two directions. The factor of two, on which the zero total rests, is a surprise with no reason and no test.
- “For small changes, the change in the room a shape takes up is the sum of the changes in its length and its two widths, each counted as a fraction of itself.”: Had to reread: 'each counted as a fraction of itself' packs the whole rule into a trailing clause.
- “volume: The amount of room something takes up.”: The glossary defines a word the entry prose never uses, while the prose says 'the room it takes up' and the check answers and misconception say 'volume'. The reader cannot tell whether they are the same idea.
- “Now watch each crumb against the centre crumb. ... each crumb along the line moves away from the centre crumb”: 'Watch against' is not English a beginner can act on, and 'moves away' is a second word for the drift the glossary already names.
- “over much longer times the new shape itself starts to shrink the ball”: A surprising claim, and the wording lets the reader conclude that the drifts stop adding to zero, which is not what happens.
- “A small ball of crumbs sits at the middle of the cloud, 2 metres across, and dust fills the space among the crumbs. ... So compare a crumb 1 metre from the middle with a crumb 2 metres out.”: The first what-if a teenager tries: a ball 2 metres across has no crumb 2 metres from its middle, so the comparison is impossible. '2 metres across' also reads at first as the cloud's size.
- “Let go of everything at once, every grain and every crumb at rest, so all of it falls freely.”: 'At rest' again with no reference, in the way where the whole cloud is falling.
- “The dust nearer the middle pulls it as if it all sat at the middle.”: Two 'it's in one sentence, and the nearest noun to the first is 'the middle', not the crumb.
- “the whole cloud falls in to its middle in about 35 minutes, however wide it is”: A surprise with no reason: a teenager objects at once that a wider cloud has farther to fall.
- “Einstein's theory also gives empty space itself a tiny outward total, away from the middle.”: 'Outward total' is a phrase the reader has not met; the note's total is a number, and an outward number means nothing yet.
- “all three drifts point inward, so their total is not zero and the ball starts to shrink”: 'Inward' has no reference here, and the sentence promises shrinking for rock, where nothing is falling freely.
- “crumbs are let go at rest at the corners of a box with 1-metre edges. After a while, each edge along the line toward Earth's centre has grown by 2 tenths of a millimetre.”: The starting state is ambiguous: nothing says the box is lined up with the line toward Earth's centre, and 'at rest' has no reference.
- “each crumb 1 metre from the centre crumb across the line toward the Moon's centre moves inward by 47 thousandths of a millimetre”: 'Inward' in a sentence that has just named the Moon's centre reads as 'toward the Moon', which is the wrong direction to picture.
- “Picture a small ball of crumbs floating in a cabin that falls freely near Earth.”: An opening question must name its setting fully; without 'nothing among the crumbs' a reader who pictures dusty air is marked wrong for a good answer.
- “crumbs along the line toward Earth's centre spread apart, and crumbs across that line draw together”: Two fresh verbs for the drift the note names everywhere else, in the answer the tutor speaks.

**Fixes**

- Gave every 'at rest' its reference (relative to the cabin, or relative to each other) in the summary, both entry ways, both entry checks that need it, and the entry problem, and named the measurer once: the cabin's clock and a ruler fixed to the cabin.
- Backed the factor of two in 'Add up the three drifts' with a count the reader can check: squaring doubles a small share (1.0001 times 1.0001 is 1.0002), 1 metre out of 6371 kilometres gives 2 parts in 6 371 000 along the line and 1 part in 6 371 000 across it. Checked against the note's own numbers: 0.154 mm and 0.077 mm in 10 seconds.
- Introduced the small ball explicitly ('The six outer crumbs mark a small ball around the centre crumb'), said where the six crumbs sit, and named 'volume' once as the name for the room a shape takes up, so the glossary entry and the check answers match the prose.
- Rewrote the volume rule as three short steps instead of one clause ending 'as a fraction of itself', in the way, the egg check answer and the matching misconception correction.
- Made the 'Among dust' ball 4 metres across, so the crumb 2 metres from the middle exists, and put its size beside the ball rather than beside the cloud. Added 'dust fills the space among the crumbs' to the dust check, which had dropped it.
- Gave the reasons two surprises were missing: why a wider dust cloud still falls in about 35 minutes, and what 'at first' hides (the drifts keep adding to zero; the egg shape itself shrinks the ball later).
- Settled the vocabulary: 'drift' for every tidal drift (no more 'moves away', 'spread apart', 'draw together'), 'add to zero' for the total and 'cancel' only for the pulls of the outer dust, and 'toward the centre crumb' in place of every bare 'inward'.
- Made the egg check's starting state unambiguous by lining the box up with the line toward Earth's centre, and named the setting in the opening question ('with nothing but empty space among the crumbs').
- Cleared the ambiguous pronouns: 'they no longer cancel' in the summary, 'these totals', 'pulls it as if it all sat at the middle', and 'the Ricci tensor records it'.
- Rewrote the dust way's simplifies so the cosmological-constant limit is stated in words the entry reader has met, keeping the 7 hydrogen atoms per cubic metre number.
- Ladder: no change was needed. Each non-entry way's first sentence already names the way it continues by title, the working way bridges back to the entry count of three drifts, and no index notation appears below the working rung. The gradiometer way's link back to 'Among dust, the ball starts to shrink' still reads correctly after the 4-metre change, because it quotes only the per-direction share.
- Nothing was dropped. Entry way explanations grew from 795 to 1,044 words, 44 past the 1,000 core cap and inside the 10% review allowance; every added word is one of the fixes recorded here, and the largest single addition is the factor-of-two count.

**Concerns**

- Entry way explanations sit at 1,044 words against a 1,000 cap. If an editor wants them under the cap, the lowest-value sentence is 'Near a planet, with nothing among the crumbs, the total comes out zero as closely as anyone can measure', which the satellite sentence right after it already carries.
- For the physics reviewer, three new entry claims: that squaring doubles a small share so the radial share is 2 parts in 6 371 000 and the transverse share 1 part in 6 371 000 at 1 metre from a crumb near Earth's surface; that a uniform ball's free-fall time does not depend on its width, so 'a wider cloud pulls harder but has farther to fall, and the two changes balance exactly'; and that where the drifts add to zero the egg shape built up later shrinks the ball on its own, while the drifts still add to zero.
- The dust way now uses a ball 4 metres across. The proposed visual falling-ring-of-crumbs should show the same size, and its sketch should place one crumb on each side of the centre crumb along the line and two in each direction across it, matching the seven-crumb setup.
- The entry-rung overlap with volume-preserving-tidal-deformation that the writer reported is untouched: both notes now teach the egg-keeps-its-volume picture, and this one also names 'volume'. An editor should decide which note owns the picture.
- My snapshot command overwrote the scratchpad file snapshots/notes-curvature/ricci-tensor.before-novice.json, which held the pre-novice state of the build that the writer discarded. My own pre-review copy is snapshots/notes-curvature/ricci-tensor.before-novice-rev1.json, and the discarded build itself survives in ricci-tensor.before-writer-rerun.json and ricci-tensor.before-rebuild.json.

**Re-read** (2026-09-13, revision 4): 4 stumbles in 4 changed passages

- “But the crumbs already let go are now moving.”: Had to reread the sentence to parse it. 'the crumbs already let go' reads at first as a subject followed by a verb ('the crumbs already let go of something'), and only the word 'are' forces a second pass.
- “They are stretching the ball along the line toward Earth's centre and narrowing it across that line, and that motion by itself slowly shrinks the room the ball takes up.”: Thirty words carrying two things at once: what the moving crumbs are doing, and a claim that this shrinks the room the ball takes up. The shrinking is a surprise with no reason, no count and no test behind it, and it appears to contradict the clay in this way's try_it, where a tenth minus a twentieth minus a twentieth is zero and the room never changed. Nothing tells the reader that the shrinking is a step taken on trust (rule 17: the way's own idea is the total of the three drifts, and this arrives as a second idea).
- “So the total counts only what is right among the crumbs, and nothing farther out.”: 'right' is doing double duty. This note uses 'right' as a direction word throughout ('three directions at right angles'), and the sentence sits between 'farther out', 'toward the middle' and 'farther from the middle', so 'right among the crumbs' first reads as a direction rather than as 'exactly among'.
- “Dust, water or rock filling the space among the crumbs adds a drift toward the centre crumb in every direction.”: Two readings, and the wrong one comes first: 'a drift toward the centre crumb in every direction' sounds like one drift pointing every way at once, rather than every crumb drifting inward whichever way it sits from the centre. Ten words of subject also arrive before the verb, which is a lot for the sentence a reader is meant to say back.
- Fix: Entry way 'Add up the three drifts': split the 30-word sentence about the crumbs already moving into three short ones, fixed the 'crumbs already let go' parse, and said that the later shrinking is taken on trust, the phrase this note already uses for the two dust facts. The claim is unchanged: the ongoing stretching and narrowing, by itself, slowly shrinks the room the ball takes up.
- Fix: Entry way 'Crumbs among dust draw together': 'what is right among the crumbs' became 'what is there among the crumbs', so 'right' is left as a direction word only. Scope unchanged: the total counts what is there among the crumbs and nothing farther out.
- Fix: Entry way 'Crumbs among dust draw together' takeaway: recast so 'in every direction' cannot be read as one drift pointing every way ('gives each crumb an extra drift toward the centre crumb'); saying it of each crumb covers every direction in fewer words and keeps the takeaway inside its 240-character limit. The claim is the physics review's: the matter adds an inward drift for every crumb, whatever else is going on.
- Fix: Left unchanged: 'just over 1.0002' (a novice can check 1.0001 times 1.0001 by hand and see why 'just over' is there), and 'Let go of fresh crumbs at any later moment' (letting go of a crumb you are holding is already letting it go at rest relative to the cabin).
- Fix: Budget: entry way explanations went 1,058 to 1,066 words against the 1,000 cap, inside the 10 per cent review allowance, and the other way fields fell from 710 to 707 words; nothing was dropped.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 4)

**Verification**

- Ricci slot convention R_munu = R^rho_{mu rho nu}, symmetry, and uniqueness of the single trace.: Re-derived from the conventions Riemann row: g^{rho sigma}R_{rho sigma mu nu}=0 by first-pair antisymmetry; upper index against the fourth slot gives R^rho_{sigma nu rho} = -R_{sigma nu}; second slot against third gives -R_{rho nu}, against fourth +R_{rho mu}; symmetry R_{sigma nu}=g^{rho lambda}R_{lambda sigma rho nu}=g^{rho lambda}R_{rho nu lambda sigma}=R_{nu sigma}. → Correct as written in key_equations/ricci-as-contraction, ways_in/the-total-is-a-trace and checks/every-trace-is-ricci. The dependence of pair exchange on metric compatibility plus zero torsion is stated correctly.
- Coordinate-free Ric(Y,Z) = tr(X -> R(X,Z)Y) has components R_{sigma nu} = R^rho_{sigma rho nu}.: Wrote [R(X,Z)Y]^rho = R^rho_{sigma mu nu} Y^sigma X^mu Z^nu from the conventions commutator row, then contracted rho with mu. → Correct; the slot assignment in ways_in/the-trace-of-the-curvature-operator reproduces the course Ricci exactly, with no sign flip.
- Tidal matrix E_ij = c^2 R^{i-hat}_{0-hat j-hat 0-hat} and the trace identity sum_i lambda_i = R_{mu nu}u^mu u^nu.: Substituted u^mu = c delta^mu_{0-hat} into the conventions geodesic-deviation row D^2 xi^mu/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma; added the vanishing rho = 0-hat term. → Correct, including the sign that a positive eigenvalue draws that direction inward, and the total of the drifts being -sum lambda_i.
- Initial volume law d^2 deltaV/dtau^2 = -R_{mu nu}u^mu u^nu deltaV at release.: Re-worked derivations/volume-law-from-deviation step by step, then re-derived it independently from the Raychaudhuri trace with theta = sigma = omega = 0 at release. → Both routes agree. The O(tau^3) remainder and the 'at that instant only' condition are correct.
- Raychaudhuri equation and the transport equation for B_{mu nu} = nabla_nu u_mu.: Derived u^lambda nabla_lambda B_{mu nu} = -B_{mu lambda}B^lambda_nu - R_{sigma mu lambda nu}u^sigma u^lambda using the course commutator on a covector, then traced with g^{mu nu}, checking g^{mu nu}R_{sigma mu lambda nu} = R_{sigma lambda} by pair exchange. → Correct, including the signs -theta^2/3 - sigma.sigma + omega.omega - R_{mu nu}u^mu u^nu and theta = d ln deltaV/dtau.
- Perfect-fluid focusing R_{mu nu}u^mu u^nu = 4 pi G (rho + 3p/c^2) - Lambda c^2.: Inverted G_{mu nu} + Lambda g_{mu nu} = 8 pi G T_{mu nu}/c^4 to R_{mu nu} = kappa(T_{mu nu} - T g_{mu nu}/2) + Lambda g_{mu nu}, then used the conventions perfect-fluid row with u.u = -c^2: T_{mu nu}u^mu u^nu = rho c^4 and T = -rho c^2 + 3p. → Correct, factor for factor, including the sign that positive Lambda defocuses.
- Weak-field R_00 = nabla^2 Phi / c^2 = 4 pi G rho / c^2 with x^0 = ct.: Computed Gamma^i_{00} = (1/c^2) partial_i Phi from g_00 = -(1 + 2Phi/c^2) in the conventions weak-field row, then R_00 = partial_i Gamma^i_{00}. → Correct and positive; consistent with the perfect-fluid formula at p = 0, Lambda = 0.
- Entry drifts near Earth: 0.154 mm out along the line and 0.077 mm in across it, per metre, in 10 s.: python: 2GM/R^3 = 3.0828e-6 s^-2 and GM/R^3 = 1.5414e-6 s^-2 with GM = 3.986004418e14 m^3 s^-2, R = 6371 km; d = a t^2 / 2. → 0.15414 mm and 0.07707 mm. Matches 'about 15 hundredths' and '7 and a half hundredths', and their signed total is zero.
- The novice reviewer's factor-of-two count: squaring doubles a small share, so 2 parts in 6 371 000 along the line and 1 part in 6 371 000 across it.: python: exact (R/(R-1))^2 - 1 = 3.1392e-7 against 2/6.371e6 = 3.1392e-7; transverse tilt sin(1 m / R) = 1.5696e-7 against 1/6.371e6. Cross-checked g x 2/R = 3.0828e-6 s^-2 against 2GM/R^3. → Correct in size and sense. One literal slip fixed: 1.0001 x 1.0001 = 1.00020001, so 'is 1.0002' became 'is just over 1.0002'.
- Working-rung conversion: a drift of 0.154 mm in 10 s at 1 m is 3.08e-6 m s^-2 per metre, and 2d/t^2 is the right rule for release from rest.: python: 2 x 1.54e-4 / 100 = 3.08e-6. → Correct.
- Try-it clay block: 10 x 2 x 2 cm pressed to 11 cm long with square sides gives about 1.9 cm.: python: sqrt(40/11) = 1.9069 cm; fractional changes +0.100, -0.0465, -0.0465. → Correct, and the volume is exactly conserved, so the tenth-minus-two-twentieths arithmetic lands where the text says.
- Entry problem missing-drift-near-the-moon: 47 thousandths of a mm across implies 94 thousandths outward along the line.: python with GM_Moon = 4.90487e12 m^3 s^-2, R = 1737.4 km: transverse 0.04676 mm, radial 0.09353 mm in 10 s. → Both quoted values correct; the signed numeric answer 0.094 mm at 5 per cent is comfortable.
- Dust way: drift 14 thousandths of a mm at 1 m in 10 s at water density, and collapse in about 35 minutes however wide the cloud.: python: (4 pi/3) G rho r = 2.7957e-7 m s^-2 gives 0.013979 mm; free-fall time sqrt(3 pi / 32 G rho) = 2100.7 s = 35.01 min, independent of radius. → Both correct. The added sentence 'a wider cloud pulls its dust harder, but that dust also has farther to fall, and the two changes balance exactly' is exact: g scales as r and the distance as r, so the time scales as sqrt(r/g), a constant.
- Novice rewrite: '8 times as much dust, each bit pulling 4 times less, so twice the pull', and 'twice as dense doubles the drift'.: Checked against g(r) = (4 pi/3) G rho r: linear in r and in rho. → Correct, and it matches the numbers in checks/denser-dust-faster (0.028 mm in both cases).
- Cosmological-constant bound: empty space wins only below about 7 hydrogen atoms per cubic metre.: python: Lambda c^2 = 3 Omega_Lambda H_0^2 = 9.80e-36 s^-2 with H_0 = 67.4 km/s/Mpc; rho = Lambda c^2 / (4 pi G) = 1.169e-26 kg m^-3, divided by 1.6735e-27 kg. → 6.99 atoms per cubic metre. Correct, and Lambda c^2 is about 1e-35 s^-2 as the gradiometer way says.
- GOCE numbers: -2.74e-6 s^-2 radial and +1.37e-6 s^-2 horizontal at r = 6626 km, with the rotation adding -2 Omega^2 = -2.74e-6 s^-2 to the raw diagonal sum.: python for the gradients. Derived the rotating-frame term: for a rigid gradiometer the measured tensor is V + Omega^2 + Omega-dot, with (Omega^2)_ij = omega_i omega_j - omega^2 delta_ij, whose trace is -2 omega^2 and Omega-dot traceless; Omega^2 = GM/r^3 on a circular orbit. → Both gradients and the -2 Omega^2 trace term are correct, and the two happen to be equal in size, as the text says. This answers the writer's open item on the rotation term.
- Lambda c^2 is about 30 orders of magnitude below near-Earth tidal gradients.: python: 3.08e-6 / 9.80e-36 = 3.1e29. → Correct.
- Worked example: Ricci tensor and scalar of a sphere of radius a.: Recomputed R^theta_{phi theta phi} from Gamma^theta_{phi phi} = -sin theta cos theta and Gamma^phi_{theta phi} = cot theta with the course Riemann formula, then repeated every raise, lower and contraction of the example. → R^theta_{phi theta phi} = sin^2 theta, R_{theta theta} = 1, R_{phi phi} = sin^2 theta, R_{mu nu} = g_{mu nu}/a^2 and R = +2/a^2, matching the conventions sphere row. Sign calibration of the slot choice confirmed.
- checks/egg-keeps-its-volume: +2, -1, -1 parts in ten thousand leave the volume unchanged to 3 parts in 100 million.: python: 1.0002 x 0.9999 x 0.9999 = 0.99999997, a change of -3.00e-8. → Correct. A cube has four edges in each direction, so 'four along, eight across' is right.
- checks/tunnel-through-the-earth: zero trace, 1.54e-6 m s^-2 together along the tunnel and 0.77e-6 m s^-2 apart across it.: Superposed a uniform ball (Hessian (4 pi/3) G rho delta_ij) with a removed long cylinder (2 pi G rho across the axis, 0 along it); python with rho = 5510 kg m^-3. → (4 pi/3) G rho = 1.5404e-6 s^-2 and (2 pi/3) G rho = 7.702e-7 s^-2; the three entries are (+4 pi/3, -2 pi/3, -2 pi/3) G rho and sum to zero. Signs of both numeric answers correct.
- checks/vacuum-table-with-zero-ricci: the six-entry table q(-2,1,1,-1,-1,2) has zero Ricci and Kretschmann 48 q^2.: Contracted with eta^{a c} by hand for each diagonal component; counted four index orders per pair for the Kretschmann sum, checking that raising a pair of hatted indices squares each sign. → All four diagonal components vanish, Kretschmann = 4 q^2 (4+1+1+1+1+4) = 48 q^2, and this is the Schwarzschild pattern with q = GM/c^2 r^3, whose known Kretschmann is 48 G^2 M^2 / c^4 r^6. Correct.
- checks/sheared-ball-loses-volume: volume ratio cosh(sqrt2 s) cos^2 s = 1 - s^4/2 + O(s^6), 0.971 at s = 0.5 and 0.636 at s = 1.: Solved each axis from L'' = -lambda L with zero initial rate; series-expanded the product by hand; python for the two values. → 0.970846 and 0.635870. Series correct: the s^2 term cancels because the trace is zero, leaving -s^4/2.
- problems/water-density-dust-ball: 4 pi G rho = 8.39e-7 s^-2 and 0.15 per cent of the volume lost in 60 s.: python: 4 pi G rho = 8.3872e-7 s^-2; half of that times 3600 s^2 = 1.5097e-3; Newtonian cross-check V = V_0(1 - 2 pi G rho t^2) gives the identical number. → Correct, and the two routes agree exactly as the solution claims.
- problems/accelerating-universe-focusing: R_00 = -3 a-double-dot/(a c^2), contraction 3 q_0 H_0^2 = -7.6e-36 s^-2.: Recomputed Gamma^0_{ij} and Gamma^i_{0j} for the flat FLRW metric with x^0 = ct, then R^i_{0i0} from the course formula; python for H_0 = 67.4 km/s/Mpc and q_0 = Omega_m/2 - Omega_Lambda. → H_0 = 2.184e-18 s^-1, q_0 = -0.5275, 3 q_0 H_0^2 = -7.550e-36 s^-2, ratio to H_0^2 = -1.5825. Every quoted value correct, and the comoving tidal matrix -(a-double-dot/a) delta_ij has the right sign for particles accelerating apart.
- problems/all-observers-zero-trace: the polarization proof.: Worked each step: openness of the timelike cone, the quadratic in epsilon, vanishing coefficients, polarization identity. → Valid. Symmetry of S is used and is available, since Ricci is symmetric for the Levi-Civita connection.
- Sectional-curvature sums: Ric(e1,e1) = sum_{i>=2} K(e1,e_i) in Riemannian signature, and Ric(u,u) = -sum_i K(u,e_i) for unit timelike u.: Expanded both in an orthonormal basis using the conventions sectional-curvature row, tracking the negative denominator g(u,u)g(e_i,e_i) on timelike planes. → Both correct, including the minus sign in the Lorentzian case and the note's remark that the behaviour, not the sign of K, is what matches.
- Normal-coordinate volume element sqrt(det g) = 1 - R_{ij}x^i x^j / 6 + O(x^3).: From g_ij = delta_ij - R_{ikjl}x^k x^l / 3, took the trace and the square root. → Correct, and it is stated for Riemannian normal coordinates, as it must be.
- Trace-reversal notation trap: for a null k, R_{mu nu}k^mu k^nu is common to the half- and quarter-trace versions.: Contracted R_{mu nu} - c R g_{mu nu} with a null vector for c = 1/2 and c = 1/4. → Correct: g_{mu nu}k^mu k^nu = 0 kills the trace term either way. G_{mu nu} trace -R in four dimensions is also correct.
- Prerequisite graph is direct and acyclic.: Built the whole vault graph from note prerequisites (registry entries where no note exists) and ran a depth-first cycle scan. → Six cycles found, every one of them through the single edge ricci-tensor -> relativistic-tidal-tensor, because that note (physics-reviewed, revision 4) lists ricci-tensor as a working prerequisite. Dropping that one edge here makes the entire vault graph acyclic.
- Reference: Rummel, Yi, Stummer (2011), GOCE gravitational gradiometry, Journal of Geodesy 85, 777-790.: Publisher record for doi:10.1007/s00190-011-0500-0. → Confirmed; verified set true.
- Reference: Aghanim, Akrami, Ashdown, Aumont and others (2020), Planck 2018 results. VI. Cosmological parameters, A&A 641, A6.: Publisher record for doi:10.1051/0004-6361/201833910 and arXiv:1807.06209; checked the four expanded given names against the author list and the quoted H_0 = 67.4, Omega_m = 0.315, Omega_Lambda = 0.685. → Confirmed, including the parameter values; verified set true.
- Reference: Ricci-Curbastro and Levi-Civita (1900), Methodes de calcul differentiel absolu et leurs applications, Mathematische Annalen 54, 125-201.: Publisher record for doi:10.1007/BF01454201 and the EuDML record. → Confirmed, volume and pages exact. The publisher dates volume 54 to 1900 while some indexes give 1901; kept 1900. The history line credits the memoir with the calculus and says only that the contracted tensor carries Ricci's name, which is the correct scope.
- Reference: Einstein (1915), Die Feldgleichungen der Gravitation, Sitzungsberichte (Berlin), 844-847, and the claim about the earlier November 1915 trace condition.: Bibliographic record (1915SPAW.......844E) and the session date of 25 November 1915; checked the scope of the earlier November papers, which set a Ricci-type tensor proportional to the energy-momentum tensor under the hypothesis that its trace vanishes. → Confirmed in venue, pages, date and scope; verified set true.
- Reference: Raychaudhuri (1955), Relativistic cosmology. I, Physical Review 98, 1123-1126.: Publisher record for doi:10.1103/PhysRev.98.1123. → Confirmed; verified set true.
- References: Hamilton (1982) JDG 17, 255-306; Perelman (2002) arXiv:math/0211159; Lott and Villani (2009) Ann. Math. 169, 903-991; Sturm (2006) Acta Math. 196, 65-131; McCann (2020) Camb. J. Math. 8(3), 609-681; Penrose (1965) PRL 14, 57-59.: Publisher or repository record for each doi or arXiv id, checking authors, year, title, venue and pages. → All six confirmed; verified set true. Added the confirmed arXiv ids math/0412127 (Lott and Villani) and 1808.01536 (McCann). Penrose's stated hypotheses (non-compact Cauchy surface, closed trapped surface, null convergence) are the theorem's actual hypotheses.
- Observation scope: GOCE measured from about 255 km, lower near the end, over 2009-2013, for gradients with periods of about 10 to 200 s.: Checked the altitude, mission dates and the measurement bandwidth of 5 to 100 mHz against the reference. → Consistent; the period range is the reciprocal of that bandwidth, and the three accurate diagonal components are the ones the trace statement uses.

**Counterexamples tried**

- Crumbs let go inside a tank of water at Earth's surface: the matter term (4 pi/3) G rho_water = 2.8e-7 s^-2 is swamped by Earth's radial tide 3.08e-6 s^-2, so the crumbs along the line toward Earth's centre still drift apart. This falsified the entry takeaway 'all three drifts point toward the centre crumb' wherever water or rock fills the space; the takeaway now says the matter adds an inward drift in every direction, which is true in every such setting. The trace, and so the shrinking, is unaffected.
- A trace-free tide held on for a long time (eigenvalues (-2,1,1)/tau_0^2): the accumulated fractional length changes are cosh(sqrt2 s) - 1 and cos s - 1 twice, which sum to +0.259 at s = 1, not zero, while the volume ratio is 0.636. This falsified 'over much longer times the drifts still add to zero' read as accumulated drifts, and also the claim that the built-up egg shape shrinks the ball: a shape at rest shrinks nothing, the shear rate does. Both sentences were rewritten.
- Empty space with a cosmological constant and no matter: R_{mu nu}u^mu u^nu = -Lambda c^2, not zero. This falsified 'the total counts only the matter right among the crumbs, and nothing else' as entry prose that must stand without the simplifies note; it now says 'only what is right among the crumbs, and nothing farther out', which keeps the locality point and stays true.
- Schwarzschild vacuum, a strong field: Ricci vanishes while Kretschmann is 48 q^2, so 'zero total' never means flat. Held by checks/vacuum-table-with-zero-ricci and by the entry misconception.
- A tunnel through a uniform Earth, matter all around but none at the event: trace zero, tides (+4 pi/3, -2 pi/3, -2 pi/3) G rho. Held; this is the intended counterexample to 'matter nearby counts'.
- The non-relativistic limit: R_00 -> nabla^2 Phi / c^2 = 4 pi G rho / c^2, and the perfect-fluid formula with p = 0, Lambda = 0 gives the same 4 pi G rho. Consistent.
- A non-static case, the accelerating universe: R_{mu nu}u^mu u^nu = -3 a-double-dot/a < 0 today, so the contraction can be negative and ordinary matter alone cannot produce it. Held by the problem and the observation.
- A massless case, null vectors: the Lambda term and the trace term both drop out of R_{mu nu}k^mu k^nu. Held, and it is what the trace-reversal notation trap says.
- A different observer at the same event: the polarization argument shows the tidal traces of all freely falling observers fix Ric, so no observer can see a zero trace where another sees a nonzero one. Held by the formal problem.
- A connection with torsion or with nabla g nonzero: pair exchange fails, other traces become new tensors and Ric acquires an antisymmetric part. Held; the formal check asks for exactly this and answers it correctly.
- Low dimensions: in two dimensions Ric = R g / 2 carries all of Riemann and in three dimensions Ric and g determine it, so 'Ricci cannot see everything' is a four-dimensional statement. The formal way scopes it correctly.
- A ball released with shear or expansion already present: the volume law fails at once, which is why its conditions name theta = sigma = omega = 0 at release. Held.
- An infinitely wide dust cloud, the first what-if against 'however wide it is': the free-fall time sqrt(3 pi / 32 G rho) does not contain the radius at all, so the claim survives every width. Held.

**Fixes**

- Entry way 'Add up the three drifts': replaced 'Over much longer times the drifts still add to zero, but the egg shape that has built up starts to shrink the ball on its own.' Read as accumulated drifts the first half is false (they sum to +0.259 of a length at s = 1 for a trace-free tide), and a built-up shape shrinks nothing by itself; it is the ongoing stretching and narrowing that does. The text now says fresh crumbs let go at any later moment still have drifts that add to zero, and that the crumbs already moving are what slowly shrinks the room.
- Entry way 'Add up the three drifts': '1.0001 times 1.0001 is 1.0002' became 'is just over 1.0002'. The product is 1.00020001, and the doubling point the sentence makes survives the one extra word.
- Entry way 'Add up the three drifts': dropped 'Near a planet, with nothing among the crumbs, the total comes out zero as closely as anyone can measure.' This is the sentence the novice reviewer nominated as lowest value, and the satellite sentence right after it carries the same claim with a measurement. It pays for most of the words the two accuracy fixes above needed; entry way explanations go from 1,044 to 1,058 words against the 1,000 cap, inside the 10 per cent review allowance.
- Entry way 'Among dust, the ball starts to shrink', takeaway: 'all three drifts point toward the centre crumb' was false wherever another body's tide dominates, for instance crumbs in water at Earth's surface. It now reads 'Dust, water or rock filling the space among the crumbs adds a drift toward the centre crumb in every direction', which is true in every setting and keeps the same one-line picture within the 240-character takeaway limit. The body of the way, which is explicitly set at the middle of a dust cloud far from any planet, needed no change.
- Entry way 'Among dust, the ball starts to shrink': 'the total counts only the matter right among the crumbs, and nothing else' became 'only what is right among the crumbs, and nothing farther out', because the cosmological constant also enters the total and entry prose has to stand without the simplifies note.
- Structure: removed relativistic-tidal-tensor from prerequisites and from the assumes of 'The total is a trace of the Riemann tensor'. That note lists ricci-tensor as its own working prerequisite, and a cycle scan showed this single edge produced every cycle in the vault's prerequisite graph. The working way already takes the geodesic deviation equation on trust and builds the tidal matrix in place, so nothing in the prose depends on the removed prerequisite. Added relativistic-tidal-tensor to leads_to instead.
- References: verified all ten and set verified true on each; added the confirmed arXiv ids math/0412127 and 1808.01536. No reference needed correcting or removing.

**Concerns**

- The registry still lags the note for poisson-equation-for-gravity and riemann-curvature-operator, and now also needs relativistic-tidal-tensor dropped; sync_registry.py should be run once this note is published. Registry prerequisites for ricci-tensor currently list only riemann-curvature-tensor, tensor-contraction and symmetries-of-the-riemann-tensor.
- The cycle I broke on this side is really a disagreement between two notes. relativistic-tidal-tensor (physics-reviewed, revision 4) lists ricci-tensor as a working prerequisite for 'the trace of the tidal tensor is the Ricci tensor'. That direction is the defensible one, so I removed the reverse edge here rather than edit a reviewed note, but an editor should confirm the ordering rather than have a later writer restore it.
- Both visuals are still proposals with no component contract. falling-ring-of-crumbs needs the seven-crumb setup and the 4-metre dust ball the entry ways now use, and six-entry-curvature-table needs the q(-2,1,1,-1,-1,2) preset that checks/vacuum-table-with-zero-ricci calls the Schwarzschild pattern.
- Course conventions still fix no symbol for the tidal matrix. The note uses E_ij, consistently with the rest of the curvature domain, but the conventions file should adopt it.
- The entry-rung overlap with volume-preserving-tidal-deformation that both earlier stages reported is unchanged; nothing I fixed touches it, and an editor still has to decide which note owns the egg-keeps-its-volume picture.
- Entry way explanations sit at 1,058 words against the 1,000 cap after these fixes, inside the review allowance. If an editor wants them under the cap, the next lowest-value sentence is the clay try-it's closing 'A tenth minus a twentieth minus a twentieth is zero, and the room the clay takes up never changed', whose arithmetic the way already stated.

**Diff check** (2026-09-13, revision 4)

- ways_in/add-up-the-three-drifts explanation: 'But the crumbs you let go at the start are now moving.' (was 'But the crumbs already let go are now moving.'): Compared the two sentences against the way's own setup, where the seven crumbs are released simultaneously, each at rest relative to the cabin, and their separations then evolve by geodesic deviation. Checked that 'at the start' names the same release moment the paragraph contrasts with 'any later moment'. → True and identical in content. Crumbs released at rest relative to the cabin acquire non-zero velocity relative to it as soon as the tide acts, so 'are now moving' is right, and the rewrite only removes the parse ambiguity of 'already let go'.
- ways_in/add-up-the-three-drifts explanation: 'They keep stretching the ball along the line toward Earth's centre, and keep narrowing it across that line.': Integrated the linear deviation equation for the way's scenario with A = GM/r^3 = 1.5414e-6 s^-2 at Earth's surface: radial separation x(t) = 1 + A t^2, transverse y(t) = z(t) = 1 - A t^2/2, both monotone while the cabin falls. Checked the sense against the note's stated convention that a drift away from the centre crumb is positive. → True throughout the fall the way describes, and the same claim as the old clause. The radial stretch and transverse narrowing keep their signs (and grow, since r decreases), so 'keep' is right. The pattern is the local tidal one, diag(+2A, -A, -A) in a freely falling non-rotating frame, consistent with the satellite sentence that follows.
- ways_in/add-up-the-three-drifts explanation, new sentence: 'Take on trust that this ongoing motion, by itself, slowly shrinks the room the ball takes up.': Raychaudhuri in vacuum with no rotation: dtheta/dtau = -theta^2/3 - sigma.sigma, and theta = sigma = 0 at release, so the first non-zero effect is the shear term alone. Cross-checked by direct integration, including the fall of the centre crumb: x = 1 + u + (5/12)u^2, y = z = 1 - u/2 - u^2/12 with u = A t^2 gives ln(xyz) = -u^2/2, hence theta = -2 A^2 t^3, matching -sigma.sigma = -6 A^2 t^2 integrated. Python: after 10 s at Earth's surface the volume is down by 1.188e-8, i.e. about one part in a hundred million. → True. The shrink is real, second order in time, and driven by the shear alone in vacuum, so 'by itself' and 'slowly' are both correct. 'Take on trust' is the right label: the volume law in this note fixes only the initial volume acceleration, so a novice cannot check the later shrink at entry. Consistent with misconceptions/volume-law-holds-forever ('Shear built up by a trace-free tide reduces the volume later') and with checks/egg-keeps-its-volume, whose answer already records the tiny product 1.0002 x 0.9999 x 0.9999 = 0.99999997.
- ways_in/crumbs-among-dust-draw-together explanation: 'So the total counts only what is there among the crumbs, and nothing farther out.' (was 'only what is right among the crumbs'): Checked the wider claim against Einstein's equation, which makes R_{mu nu} algebraic in T_{mu nu} at the same event, so the total R_{mu nu}u^mu u^nu = 4 pi G(rho + 3p/c^2) - Lambda c^2 depends on no distant source. Tried the standard counterexamples: a shell of dust farther out (its Newtonian pull cancels, and it adds no Ricci at the crumbs); a passing gravitational wave (Weyl, not Ricci); radiation rather than dust among the crumbs (rho + 3p/c^2 = 2 rho_rad, still local). → True, and the rewrite widens nothing it should not: 'what is there' covers pressure and radiation as well as rest mass, while the vacuum-energy piece stays in this way's simplifies. Consistent with misconceptions/matter-nearby-counts.
- ways_in/crumbs-among-dust-draw-together takeaway: 'Dust, water or rock among the crumbs gives each crumb an extra drift toward the centre crumb.' (was 'adds a drift toward the centre crumb in every direction'): Split the potential of the region into the uniform-density part and an external harmonic part: the local uniform density rho adds exactly -(4 pi G rho/3) xi_i to the deviation of a crumb at separation xi, which is inward and isotropic. Checked the relativistic version for a comoving perfect fluid, where the deviation is xi-double-dot = -(4 pi G/3)(rho + 3p/c^2) xi in every direction. Counterexamples tried: negative pressure (excluded by naming dust, water or rock, and covered by this way's simplifies), strong field and non-static matter (rho + 3p/c^2 stays positive), matter only farther out (adds nothing). → Equally true and the same physics. Saying it of each crumb carries the isotropy the old 'in every direction' carried, because this way's recap has the crumbs marking a small ball around the centre crumb. The extra drift is proportional to how far out a crumb sits, as the way's own sentence 'Each crumb is pulled toward the middle in proportion to how far out it sits' states, so the centre crumb's zero is the degenerate case of the same rule, not an exception to it.
- Numbers standing next to the changed sentences, rechecked because the changed text leans on them: the 15 and 7.5 hundredths of a millimetre drifts, the 14 thousandths of a millimetre in dust as dense as water, the 35-minute collapse, and the 7 hydrogen atoms per cubic metre.: Python with G = 6.674e-11: A = GM/r^3 = 1.5414e-6 s^-2 gives 0.1541 mm and 0.0771 mm in 10 s; (4 pi G rho/3) with rho = 1000 kg/m^3 gives 0.01398 mm in 10 s and a free-fall time sqrt(3 pi/(32 G rho)) = 35.01 min; the crossover density 2 rho_Lambda = 1.186e-26 kg/m^3 is 7.09 hydrogen masses per cubic metre. → All unchanged numbers confirmed, so the reworded sentences sit on correct arithmetic.
- The re-read's open worry that the unchanged try_it now contradicts the new shrinking sentence, because 1.1 x 0.95 x 0.95 = 0.9927.: Modelling clay is incompressible, so the honest comparison is the volume-preserving width: 11 w^2 = 40 gives w = 1.9069 cm, which reads as 1.9 cm on the millimetre ruler the try_it specifies, and 11 x 1.9069^2 = 40.00 exactly. The 0.7 per cent comes from treating a rounded ruler reading as exact. → No error, and no contradiction with the new sentence. The clay really does keep its volume, and the first-order sum rule gets that right to the ruler's precision; the second-order shrink the new sentence names is a property of the falling crumbs, not of the clay. Left unchanged, since editing it would only restate what the ruler already scopes.
- Fix: No errors found in the three changed entry strings, so nothing was edited and the revision stays at 4. No novice sign-off is needed.
- Fix: review.physics.reviewed_revision raised from 3 to 4, which clears the expected validator warning.
- Fix: Left for an editor, unchanged from the physics review: the registry lag for poisson-equation-for-gravity and riemann-curvature-operator (run sync_registry.py); both visuals still proposals without component contracts; no course-conventions symbol for the tidal matrix; and the entry-rung overlap with volume-preserving-tidal-deformation.
