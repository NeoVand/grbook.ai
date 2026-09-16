---
type: "concept"
schema_version: 2
id: "weyl-tensor"
title: "Weyl tensor"
tagline: "The shape-changing part of curvature, the part that lives in empty space"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["Weyl curvature tensor", "conformal curvature tensor", "trace-free part of the Riemann tensor"]
prerequisites: ["riemann-curvature-tensor", "ricci-tensor", "ricci-scalar", "number-of-independent-riemann-components", "index-notation"]
leads_to: ["weyl-tensor-field-equation", "weyl-criterion-for-conformal-flatness", "petrov-classification", "ricci-focusing-versus-weyl-shear"]
visuals: ["falling-ring-of-crumbs", "six-entry-curvature-table", "twenty-of-256-slots", "circles-behind-a-see-through-star"]
---

# Weyl tensor

*The shape-changing part of curvature, the part that lives in empty space*

`weyl-tensor` · curvature · core · physics-reviewed (revision 4)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[ricci-tensor]] (entry) · [[ricci-scalar]] (working) · [[number-of-independent-riemann-components]] (working) · [[index-notation]] (working)  
**Opens:** [[weyl-tensor-field-equation]] · [[weyl-criterion-for-conformal-flatness]] · [[petrov-classification]] · [[ricci-focusing-versus-weyl-shear]]  
**Related:** [[relativistic-tidal-tensor]] · [[volume-preserving-tidal-deformation]] · [[kretschmann-scalar]] · [[gravitational-wave]] · [[conformally-flat-metric]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[six-entry-curvature-table]] · [[twenty-of-256-slots]] · [[circles-behind-a-see-through-star]]

> Let go of crumbs on a small ball inside a cabin falling freely near a planet. Part of their drift changes the room the ball takes up, and matter right at the spot sets that part. The rest changes only the ball's shape. With nothing in the cabin, or only dust at rest around it, the Weyl tensor is the table that holds this shape-changing part. Beside a planet, or in a passing gravitational wave, where there is no matter at all, it is all the drift there is.

## You will be able to

**Entry**
- Explain how the drift of crumbs in a falling cabin splits into a room-changing part, set by matter at the spot, and a shape-changing part, which the Weyl tensor holds. `objectives/split-the-drift` ← `checks/ball-above-the-air`, `checks/three-places`, `problems/two-high-tides`
- Predict which part a ball of crumbs shows beside a planet, inside dust at rest, or in a gravitational wave. `objectives/predict-which-part-shows` ← `checks/three-places`

**Working**
- Compute the Weyl tensor from the Riemann tensor, Ricci tensor, Ricci scalar and metric, and count its components in any dimension. `objectives/compute-the-weyl-tensor` ← `checks/vacuum-leftover`
- Use the electric part of the Weyl tensor as the vacuum tidal tensor to compute relative accelerations near a distant mass or in a gravitational wave. `objectives/use-the-electric-part` ← `checks/moon-stretch`, `problems/wave-tide-on-a-detector`

**Formal**
- State the Ricci decomposition, conformal invariance and the Weyl–Schouten theorem with their hypotheses, prove that the Weyl tensor vanishes in three dimensions, and split it for an observer into electric and magnetic parts. `objectives/state-the-decomposition` ← `checks/rescale-the-lowered-weyl`, `checks/conformally-flat-in-three-dimensions`, `problems/isotropy-kills-weyl`

## Ways in

### 1. Take the shrinking out of the drift · entry · picture

*A ball of crumbs let go in a falling cabin changes shape, and among dust it also shrinks. How can the two changes be told apart?*

**Recap:** To fall freely is to move with nothing but gravity acting. In a cabin falling freely near a planet, crumbs let go at rest drift slowly compared with a centre crumb. That is because gravity pulls each of them slightly differently. That slow drift is called tidal drift. With nothing among the crumbs, the drifts along three directions at right angles add up to zero, so at first the room the ball takes up does not change. Dust among the crumbs pulls every crumb in toward the centre crumb, so then the drifts no longer add up to zero and the ball starts to shrink.

Picture a cabin falling freely toward Earth, high above the air. Inside it, hold crumbs at rest on a small imaginary ball around a centre crumb, and let them all go. A ruler fixed to the cabin measures how each crumb moves compared with the centre crumb.

Tidal drift sets in. The two crumbs on the line toward Earth's centre, the top and bottom of the ball, drift away from the centre crumb; the bottom crumb is the one nearer Earth. That is because Earth pulls the bottom crumb harder, and the top crumb less, than it pulls the centre crumb. The crumbs around the ball's middle drift in toward the centre crumb, each by half as much, because with nothing among the crumbs the three drifts add up to zero. So the ball slowly becomes an egg standing along that line.

Now picture the same ball let go far from every planet, inside a huge round cloud of dust, spread evenly and at rest around the cabin. Every crumb drifts in toward the centre crumb by the same amount, whatever direction it lies in. That is because the dust inside the ball pulls each crumb in toward the centre crumb, and that dust is the same on every side. The ball stays round and shrinks.

Any pattern of drift can be split into two parts. The first part is the same drift in every direction, all in or all out. To find its size, measure the drifts along three directions at right angles and take their average. This first part is the room-changing part, because equal drift in every direction is what makes the room a ball takes up grow or shrink. The second part is whatever is left once the first is taken away. It stretches the ball in some directions and squeezes it in others by amounts that add up to zero, so it changes the shape and leaves the room the same at first.

Try the split on the egg near Earth. Count the drifts along three directions at right angles: 2 units out along the line to Earth's centre, and 1 unit in along each of the other two. Added up, 2 minus 1 minus 1 is 0, so the average is 0 too. So there is no room-changing part at all: the drift near Earth is pure shape-changing part. In the dust cloud the drifts are 1 in, 1 in and 1 in, the same in every direction, so that drift is pure room-changing part and nothing is left over.

How big is the drift? Take a ball one metre across in a cabin falling 400 kilometres above Earth. After one minute the top and bottom crumbs are each about two millimetres farther from the centre crumb, and the crumbs around the middle each about one millimetre nearer. Daily life hides this because a floor holds you up and nothing you own falls freely for a minute.

The Ricci tensor is the table that holds the room-changing part, and matter right at the spot sets it. The Weyl tensor is the table that holds the shape-changing part, for every way the cabin can move and for every direction a crumb can lie. That is exact when the cabin holds nothing, or only dust at rest around it. Together, the two tables hold all the curving there is.

**Try it:** Press a blown-up party balloon between your hands around its middle: it bulges into an egg, holding the same air. Let a little air out instead: it stays round and shrinks. One is a shape change with no room change, the other a room change with no shape change.

**Takeaway:** Split the drift of a ball of crumbs into the same drift in every direction, which changes its room, and the leftover, which changes only its shape. The Weyl tensor holds the shape-changing part.

*What this leaves out:* The leftover is exactly the Weyl part when there is no matter at the spot. It is also exact when the matter there is dust at rest around the cabin. Matter rushing past, or pressing harder one way than another, adds a shape change that the Ricci table holds.

*Builds on:* [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/ball-above-the-air`

### 2. The part that lives in empty space · entry · operational

*Beside a planet there is no matter to set the drift. Where does the shape-changing part come from, and how can it be measured without a cabin?*

**Recap:** In a cabin falling freely, crumbs let go on a small ball drift. The drift splits into two parts. The room-changing part is the same in every direction, and matter at the spot sets it. The shape-changing part stretches some directions and squeezes others by balancing amounts. The Weyl tensor holds the shape-changing part.

In 'Take the shrinking out of the drift', the ball beside Earth became an egg although no matter was in the cabin. So the shape-changing part needs no matter at the spot. It comes from matter somewhere else: there, from the whole Earth below the cabin.

Earth itself shows the same thing on a grand scale. Earth, like the cabin, falls freely: nothing holds it up, and the Moon's pull is one of the pulls it falls under. The water of its oceans plays the crumbs. Call the side of Earth facing the Moon the near side, and the side facing away the far side. The Moon's pull weakens with distance, so it pulls the near side a little harder than Earth's centre, and the centre a little harder than the far side. Compared with the centre, then, the near side drifts toward the Moon. The far side is pulled less than the centre, so compared with the centre it lags behind: it drifts away from the Moon. Around the ring of Earth halfway between the near side and the far side, the Moon's pull slants a little in toward the line from Earth's centre to the Moon. It slants because the Moon sits on that line, so from the ring the Moon lies a little inward. So Earth is stretched along the line to the Moon and squeezed across it: the same egg the crumbs made, with the Moon in the planet's place.

Water can flow, so it piles up on the near side and on the far side, and it is drawn down around the ring between them. A tide gauge in a harbour measures the sea level. As Earth turns once, the harbour passes both piles and crosses the low ring twice: two high tides and two low tides in a day. That double pattern is the shape-changing part, read in water.

The Moon's stretch at Earth's surface is about one part in nine million of Earth's own pull, so you never feel it. The oceans show it because they are thousands of kilometres wide, and over that width the tiny slanting pulls add up.

The Sun does the same, a little less than half as strongly, although its pull on Earth as a whole is far stronger than the Moon's. The stretch comes from how much the pull differs across Earth's width, and that difference fades with distance much faster than the pull itself. No matter at the spot is needed for any of this: the Moon and the Sun stretch Earth from across empty space.

**Try it:** Look up a tide table for any ocean harbour. Most show two high tides and two low tides each day, and each day the times slip later by about fifty minutes, because the Moon has moved on around Earth.

**Takeaway:** The shape-changing part needs no matter at the spot. From across empty space the Moon stretches Earth along the line toward it and squeezes it across, and a tide gauge reads that egg as two high tides a day.

*What this leaves out:* Real tides are also shaped by coastlines, ocean depth and the water's own sloshing, so their size and timing differ from harbour to harbour. A few seas, such as the Gulf of Mexico, respond with only one high tide a day. The double pattern in most harbours comes from the stretch.

*Continues:* `ways_in/take-the-shrinking-out-of-the-drift`<br>*Builds on:* [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/three-places`, `observations/ocean-tides`

### 3. Subtract every trace · working · calculation

*How is the Weyl tensor built from the Riemann tensor, and what does being trace-free buy?*

In 'Take the shrinking out of the drift', the drift of a ball of crumbs split into a same-in-every-direction part and a balanced leftover. The Riemann tensor $R_{\rho\sigma\mu\nu}$ splits the same way. Its trace over the first and third slots is the Ricci tensor, $R_{\sigma\nu} = g^{\rho\mu}R_{\rho\sigma\mu\nu}$: ten numbers at each event of spacetime, and by Einstein's equation those ten are fixed by the matter at the event. The Riemann tensor has twenty, so ten numbers escape the Ricci tensor. The Weyl tensor collects them.

To build it, subtract from $R_{\rho\sigma\mu\nu}$ the one combination of the Ricci tensor, the Ricci scalar and the metric that has the Riemann symmetries and the same traces. The derivation 'Kill every trace' fixes the coefficients. In four dimensions,

$$C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu} - \tfrac12\big(g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu}\big) + \tfrac{R}{6}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big).$$

Being trace-free buys three things. First, $C$ keeps every symmetry of the Riemann tensor, so it can be read as a symmetric 6-by-6 matrix on pairs of directions, and every contraction of it vanishes: $C^\rho{}_{\sigma\rho\nu} = 0$, and by the symmetries every other trace too. Second, in a vacuum region with no cosmological constant, $R_{\mu\nu} = 0$, so the subtracted terms vanish and $C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu}$: outside a star, and in a gravitational wave, all the curvature is Weyl curvature. Third, at the other extreme, a space of constant curvature, $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, has $C = 0$: everything is trace and nothing is left. The same is true of the homogeneous, isotropic universe of cosmology, whose curvature is pure Ricci.

The count works in any number of dimensions $n$. The Riemann tensor has $n^2(n^2-1)/12$ independent components and the Ricci tensor $n(n+1)/2$. In three dimensions both are 6, and the map from Riemann to Ricci is then invertible, so the Ricci tensor fixes the whole Riemann tensor and the Weyl tensor vanishes identically. That is why a world with two space dimensions and one time dimension has no tides in empty space. In four dimensions $20 - 10 = 10$ components survive, and they are exactly what lets gravity reach across empty space.

**Takeaway:** The Weyl tensor is the Riemann tensor with every trace subtracted; in vacuum it equals the Riemann tensor, and in three dimensions it is zero.

*Continues:* `ways_in/take-the-shrinking-out-of-the-drift`<br>*Builds on:* [[ricci-tensor]], [[ricci-scalar]], [[number-of-independent-riemann-components]]<br>*Visuals:* [[six-entry-curvature-table]], [[twenty-of-256-slots]]<br>*See:* `derivations/kill-every-trace`, `worked_examples/schwarzschild-is-pure-weyl`, `checks/vacuum-leftover`

### 4. The electric part is the vacuum tide · working · operational

*What does a freely falling observer measure of the Weyl tensor, and what sets its size?*

The egg of 'The part that lives in empty space' is what an observer falling freely with four-velocity $u^\mu$ reads of the Riemann tensor through the drift of nearby free test masses: in her orthonormal frame, $d^2\xi^{\hat\imath}/d\tau^2 = -c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}\,\xi^{\hat\jmath}$. Feed the Weyl tensor of 'Subtract every trace' her four-velocity twice instead, and you get its electric part,

$$E_{ij} = c^2\,C_{\hat\imath\hat 0\hat\jmath\hat 0},$$

a symmetric matrix with zero trace, so five numbers. In vacuum $C = R$ and the drift law becomes $\ddot\xi^i = -E_{ij}\xi^j$: the electric part is the whole tidal tensor of empty space. Its zero trace is the cancelling of the three drifts in 'Take the shrinking out of the drift'.

Three vacuum tides fix the picture. Outside a spherical mass $M$, an observer at rest or falling radially at distance $r$ reads $E = \dfrac{GM}{r^3}\,\mathrm{diag}(-2, 1, 1)$ along the radial and two transverse directions; the minus sign on the radial entry means stretching, because $\ddot\xi = -E\xi$. Doubling $M$ doubles every entry, and doubling $r$ divides them by 8. For the Moon at Earth, $GM/d^3 = 8.6\times10^{-14}\ \mathrm{s^{-2}}$, so a point on Earth's surface facing the Moon, $6371$ km from the centre, is pulled away from the centre by $2GMR_\oplus/d^3 = 1.1\times10^{-6}\ \mathrm{m/s^2}$, one part in nine million of $g$. Second, a gravitational wave travelling along $z$ with plus polarization $h_+(t - z/c)$ gives $E_{xx} = -E_{yy} = -\tfrac12\ddot h_+$ and $E_{zz} = 0$: a stretch along $x$ paired with an equal squeeze along $y$, both across the direction of travel. Third, inside a uniform ball of dust, for an observer at rest in the dust, $E = 0$: the tide there is pure Ricci.

A single observer reads only five of the ten Weyl components. The other five form the magnetic part. She can read it from the drift of test masses moving relative to her, or by asking a differently moving observer, whose electric part mixes in the magnetic one much as a boost mixes electric and magnetic fields.

What sets the size of $E$ is matter elsewhere. The second Bianchi identity, with Einstein's equation substituted, becomes a field equation for $C$ whose source is built from derivatives of the Ricci tensor, so a star's mass sources the Weyl field around it, which then falls off as $1/r^3$. That equation is the subject of its own note; here it is stated, not derived.

**Takeaway:** For a freely falling observer the electric part of the Weyl tensor is the vacuum tidal tensor: five trace-free numbers sourced by matter elsewhere.

*What this leaves out:* The tidal tensor is the electric part only in vacuum; with matter at the spot, Ricci terms add to it.

*Continues:* `ways_in/subtract-every-trace`, `ways_in/the-part-that-lives-in-empty-space`<br>*Builds on:* [[riemann-curvature-tensor]], [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/moon-stretch`, `problems/wave-tide-on-a-detector`

### 5. Trace-free part, conformal class and the observer split · formal · structure

*What exactly is the Weyl tensor, which theorems does it obey, and how does it decompose for an observer?*

The subtraction in 'Subtract every trace' is a projection, and the electric part of 'The electric part is the vacuum tide' is half of an observer's split; this way makes both exact. Set $G = c = 1$. On a pseudo-Riemannian manifold $(M, g)$ of dimension $n \ge 3$ with its Levi-Civita connection, fix a point and let $\mathcal C$ be the space of algebraic curvature tensors there: $(0,4)$ tensors antisymmetric in each pair, symmetric under pair exchange and obeying the cyclic identity, so $\dim\mathcal C = n^2(n^2-1)/12$. For symmetric 2-tensors $h, k$ the Kulkarni–Nomizu product $(h \owedge k)_{abcd} = h_{ac}k_{bd} + h_{bd}k_{ac} - h_{ad}k_{bc} - h_{bc}k_{ad}$ lies in $\mathcal C$. With the Schouten tensor $P_{ab} = \dfrac{1}{n-2}\Big(R_{ab} - \dfrac{R}{2(n-1)}\,g_{ab}\Big)$, the Ricci decomposition of 'Subtract every trace' reads

$$R_{abcd} = C_{abcd} + (P \owedge g)_{abcd},$$

and expanding $P$ gives the $n$-dimensional formula with coefficients $1/(n-2)$ and $1/((n-1)(n-2))$. The map $h \mapsto h \owedge g$ from symmetric tensors into $\mathcal C$ is injective for $n \ge 3$: its Ricci trace is $(n-2)h + (\operatorname{tr}h)\,g$, from which $h$ is recovered. Its image has dimension $n(n+1)/2$ and is orthogonal, in the inner product induced by $g$, to the kernel of the Ricci trace, which is the space of Weyl tensors. So $\mathcal C$ splits into scalar, trace-free Ricci and Weyl parts of dimensions $1$, $n(n+1)/2 - 1$ and $n(n+1)(n+2)(n-3)/12$, each irreducible under the orthogonal group of $g$. For $n = 3$, $\dim\mathcal C = 6 = \dim\mathrm{Sym}^2$, so the injective map is onto and $C \equiv 0$: the Riemann tensor is an algebraic function of the Ricci tensor.

Conformal invariance. Under $\tilde g = \Omega^2 g$ with $W_a = \partial_a\ln\Omega$, the connection changes by $\tilde\Gamma^a{}_{bc} = \Gamma^a{}_{bc} + \delta^a_bW_c + \delta^a_cW_b - g_{bc}W^a$, and a direct computation gives $\tilde R_{abcd} = \Omega^2\big(R_{abcd} + (T \owedge g)_{abcd}\big)$ for a symmetric $T_{ab}$ built from $\nabla_aW_b$ and $W_aW_b$. The correction lies in the image of $h \mapsto h \owedge g$, hence is Weyl-free, and the trace-free projection with respect to $\tilde g$ of $\Omega^2 X$ is $\Omega^2$ times the projection of $X$ with respect to $g$. So $\tilde C_{abcd} = \Omega^2C_{abcd}$, that is $\tilde C^a{}_{bcd} = C^a{}_{bcd}$; lowered or fully raised, the tensor scales by $\Omega^2$ or $\Omega^{-6}$. Thus $C = 0$ is a property of the conformal class. The Weyl–Schouten theorem states the converse for $n \ge 4$: $g$ is locally conformally flat, $g = \Omega^2\eta$ near each point, if and only if $C = 0$. For $n = 3$ the criterion is instead the vanishing of the Cotton tensor $\nabla_cP_{ab} - \nabla_bP_{ac}$, and for $n = 2$ every metric is locally conformally flat. All of these statements are local.

Observer split. For a unit timelike $u$, with the course Levi-Civita tensor $\epsilon_{0123} = +\sqrt{-g}$ and the left dual ${}^*C_{abcd} = \tfrac12\epsilon_{abef}C^{ef}{}_{cd}$, define

$$E_{ab} = C_{acbd}u^cu^d,\qquad B_{ab} = {}^*C_{acbd}u^cu^d.$$

Both are symmetric, trace-free and orthogonal to $u$, so each has five components, and $C$ is recovered from $E$, $B$ and $u$; for the Weyl tensor the left and right duals agree. Under a boost $E$ and $B$ mix. The invariant $C_{abcd}C^{abcd} = 8(E_{ab}E^{ab} - B_{ab}B^{ab})$: for Schwarzschild, static observers read $E = (M/r^3)\,\mathrm{diag}(-2,1,1)$ and $B = 0$, giving the Kretschmann value $48M^2/r^6$. In an isotropic cosmology comoving observers read $E = B = 0$, hence $C = 0$.

**Takeaway:** The Weyl tensor is the Ricci-orthogonal part of curvature: zero for n at most 3, conformally invariant with one index up, and split for an observer into five electric and five magnetic components.

*Picture:* Three orthogonal axes labelled scalar (1), trace-free Ricci (9) and Weyl (10); vacuum lies on the Weyl axis, constant curvature on the scalar axis.

*What this leaves out:* The conformal change of the Riemann tensor is quoted, not derived.

*Continues:* `ways_in/subtract-every-trace`, `ways_in/the-electric-part-is-the-vacuum-tide`<br>*Builds on:* [[riemann-curvature-tensor]], [[number-of-independent-riemann-components]]<br>*See:* `checks/rescale-the-lowered-weyl`, `checks/conformally-flat-in-three-dimensions`, `problems/isotropy-kills-weyl`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | — |
| tidal drift | — | The slow drift of crumbs let go at rest in a freely falling cabin, compared with a centre crumb, because gravity pulls each crumb slightly differently. | [[relativistic-tidal-tensor]] |
| centre crumb | — | The crumb at the centre of the ball. Every other crumb's drift is measured against it, with a ruler fixed to the falling cabin. | — |
| room | — | How much a thing takes up; physicists say volume. | — |
| room-changing part | — | The part of the drift that is the same in every direction, all in or all out. It makes the room a ball takes up start to change, and matter right at the spot sets it. | [[ricci-tensor]] |
| shape-changing part | — | What is left of the drift once the room-changing part is taken away. It stretches a ball of crumbs in some directions and squeezes it in others by balancing amounts, so at first the room stays the same. | [[weyl-tensor]] |
| Weyl tensor | VILE tensor, Weyl rhymes with mile | The table, kept at every place, that holds the part of the drift that no matter at the spot sets, for every way a cabin can move. With nothing in the cabin, or only dust at rest around it, that is exactly the shape-changing part. Beside a planet or in a gravitational wave it is all the curving there is. | [[weyl-tensor]] |
| Ricci tensor | REE-chee tensor | The table that holds the room-changing part of the drift. Matter right at the spot sets it. | [[ricci-tensor]] |
| gravitational wave | — | A pattern of stretch and squeeze that travels through empty space at the speed of light, made by violently moving masses such as two merging black holes. | [[gravitational-wave]] |
| tide gauge | — | An instrument in a harbour that records the height of the sea through the day. | — |

## Key equations

### Weyl tensor in four dimensions · working

$$
C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu} - \tfrac12\big(g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu}\big) + \tfrac{R}{6}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big)
$$

The Riemann tensor with the unique Ricci-and-metric combination removed so that every contraction vanishes; in vacuum with no cosmological constant it equals the Riemann tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C_{\rho\sigma\mu\nu}$ | Weyl tensor with all indices down | the Weyl tensor |
| $R_{\rho\sigma\mu\nu}$ | Riemann tensor with its first index lowered | the Riemann tensor |
| $R_{\sigma\nu}$ | Ricci tensor, the trace of the Riemann tensor over its first and third slots | the Ricci tensor |
| $R$ | Ricci scalar | the Ricci scalar |
| $g_{\rho\mu}$ | metric | the metric |

**Holds when:** Four dimensions, Levi-Civita connection, $R_{\sigma\nu} = g^{\rho\mu}R_{\rho\sigma\mu\nu}$.  
**Say it:** “The Weyl tensor is the Riemann tensor, minus one half of the four metric-times-Ricci terms, plus one sixth of the Ricci scalar times the metric-times-metric pair.”  
**Justified by:** `derivations/kill-every-trace`

### Electric part of the Weyl tensor · working

$$
E_{ij} = c^2\,C_{\hat\imath\hat 0\hat\jmath\hat 0},\qquad \frac{d^2\xi^{\hat\imath}}{d\tau^2} = -E_{ij}\,\xi^{\hat\jmath}\ \ \text{(vacuum)}
$$

The Weyl tensor fed the observer's four-velocity twice: a symmetric trace-free matrix of relative acceleration per unit separation, which in vacuum is the whole tidal tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E_{ij}$ | electric part of the Weyl tensor in the observer's orthonormal frame, in inverse seconds squared | the electric part |
| $C_{\hat\imath\hat 0\hat\jmath\hat 0}$ | Weyl components in the observer's orthonormal frame with the time index in the second and fourth slots | the Weyl tensor with the observer's time direction in its second and fourth slots |
| $\xi^{\hat\imath}$ | separation of a nearby free test mass from the observer, along her proper time $\tau$ | the separation |

**Holds when:** The drift law holds in vacuum with no cosmological constant, to first order in the separation, for test masses at rest relative to the observer.  
**Say it:** “The electric part is c squared times the Weyl tensor with the observer's time direction in its second and fourth slots; in vacuum, a separation accelerates by minus the electric part times the separation.”  
**Justified by:** `riemann-curvature-tensor`

### Conformal invariance · formal

$$
\tilde g_{\mu\nu} = \Omega^2 g_{\mu\nu}\ \Longrightarrow\ \tilde C^{\rho}{}_{\sigma\mu\nu} = C^{\rho}{}_{\sigma\mu\nu}
$$

Rescaling the metric by any positive function leaves the Weyl tensor with one index up unchanged; the all-lowered form picks up the function squared.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Omega$ | positive smooth conformal factor | omega |
| $\tilde C^{\rho}{}_{\sigma\mu\nu}$ | Weyl tensor of the rescaled metric, first index up | the Weyl tensor of the rescaled metric with its first index up |

**Holds when:** Any dimension $n \ge 3$, Levi-Civita connections of $g$ and $\tilde g$.  
**Say it:** “If the rescaled metric is omega squared times the metric, the Weyl tensor with its first index up is the same for both.”  
**Justified by:** `stated`

## Derivations

### Kill every trace · working

**Goal:** Find the coefficients $\alpha, \beta$ for which $C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu} + \alpha\,(g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu}) + \beta\,R\,(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ has every contraction zero in $n$ dimensions.

1. Each bracket is antisymmetric in $\rho\sigma$ and in $\mu\nu$, symmetric under pair exchange, and obeys the cyclic identity; so $C$ has every Riemann symmetry whatever $\alpha$ and $\beta$ are.
2. Contract with $g^{\rho\mu}$: the Riemann term gives $R_{\sigma\nu}$.
3. In the $\alpha$ bracket, $g^{\rho\mu}g_{\rho\mu} = n$ turns the first term into $nR_{\sigma\nu}$; the second term gives $-R_{\sigma\nu}$; the third gives $g_{\sigma\nu}R$; the fourth gives $-R_{\sigma\nu}$. Total: $\alpha\big[(n-2)R_{\sigma\nu} + R\,g_{\sigma\nu}\big]$.
4. In the $\beta$ bracket, $g^{\rho\mu}(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}) = (n-1)g_{\sigma\nu}$, so the term gives $\beta(n-1)R\,g_{\sigma\nu}$.
5. The contraction is $R_{\sigma\nu}\big[1 + \alpha(n-2)\big] + R\,g_{\sigma\nu}\big[\alpha + \beta(n-1)\big]$. For it to vanish for every Ricci tensor, both brackets must be zero.
6. So $\alpha = -\dfrac{1}{n-2}$ and $\beta = -\dfrac{\alpha}{n-1} = \dfrac{1}{(n-1)(n-2)}$. For $n = 4$ these are $-\tfrac12$ and $\tfrac16$.
7. A trace within a pair is zero by antisymmetry, and the other cross traces are $\pm$ the one just computed.
8. Check with constant curvature, $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$: the $\alpha$ bracket becomes $2(n-1)K$ times the metric pair, and the total coefficient $K\big[1 - \tfrac{2(n-1)}{n-2} + \tfrac{n}{n-2}\big]$ vanishes.

**Result:** $\alpha = -\dfrac{1}{n-2}$ and $\beta = \dfrac{1}{(n-1)(n-2)}$ make $C$ trace-free in every slot pair; $n = 4$ gives $-\tfrac12$ and $\tfrac16$.

## Worked examples

### Outside a star the curvature is pure Weyl · working

**Problem:** Outside a nonrotating mass $M$, in the orthonormal frame of a static observer at radius $r$ and with $m = GM/c^2$, the independent Riemann components are $R_{\hat t\hat r\hat t\hat r} = -2m/r^3$, $R_{\hat t\hat\theta\hat t\hat\theta} = R_{\hat t\hat\phi\hat t\hat\phi} = m/r^3$, $R_{\hat r\hat\theta\hat r\hat\theta} = R_{\hat r\hat\phi\hat r\hat\phi} = -m/r^3$ and $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = 2m/r^3$. Show that the Ricci tensor vanishes and read off the electric part.

1. With $R_{\hat a\hat b} = \eta^{\hat c\hat d}R_{\hat c\hat a\hat d\hat b}$ and $\eta^{\hat t\hat t} = -1$: $R_{\hat t\hat t} = R_{\hat r\hat t\hat r\hat t} + R_{\hat\theta\hat t\hat\theta\hat t} + R_{\hat\phi\hat t\hat\phi\hat t} = (-2 + 1 + 1)\,m/r^3 = 0$, using pair exchange to rewrite each term.
2. $R_{\hat r\hat r} = (2 - 1 - 1)\,m/r^3 = 0$ and $R_{\hat\theta\hat\theta} = R_{\hat\phi\hat\phi} = (-1 - 1 + 2)\,m/r^3 = 0$ in the same way, with the time term entering with a minus sign; the off-diagonal components have no nonzero terms.
3. With every Ricci component zero, the subtracted terms vanish and $C_{\hat a\hat b\hat c\hat d} = R_{\hat a\hat b\hat c\hat d}$.
4. The electric part is $E_{ij} = c^2C_{\hat\imath\hat t\hat\jmath\hat t}$, so $E = \dfrac{GM}{r^3}\,\mathrm{diag}(-2, 1, 1)$ on the radial and two transverse directions, with zero trace; the drift law $\ddot\xi = -E\xi$ stretches radially and squeezes transversely.

**Answer:** $R_{\hat a\hat b} = 0$, so $C = R$ outside the star; $E = (GM/r^3)\,\mathrm{diag}(-2,1,1)$ with trace zero.

**Takeaway:** Vacuum curvature is Weyl curvature: a star's whole $1/r^3$ tidal field lives in the ten components the Ricci tensor cannot see.

## Problems

### `two-high-tides` · entry · difficulty 1 · conceptual

A friend says: 'The Moon pulls the sea toward it. So the water should pile up on the side of Earth facing the Moon. A harbour should get one high tide a day.' Using the picture of crumbs let go in a falling cabin, explain why most harbours get two high tides in a day. Explain also why the Moon makes no room-changing part at Earth.

**Hints**

1. Compared with Earth's centre, which way is the far side of Earth pulled?
2. Which part of the drift, room-changing or shape-changing, does a body far away make?

**Answer:** Two high tides: the Moon stretches Earth along the line toward it, on the near side and the far side alike, and squeezes it across that line. That is a shape change with no room change, so the water is only moved about, not added to or taken away.

**Must contain:** Compared with Earth's centre, the far side is pulled away from the Moon and the near side toward it; The Moon stretches Earth along the line to it and squeezes across, making two piles; A body far away makes only the shape-changing part, which leaves the room unchanged

**Numeric:** high tides in one day at most harbours = 2 1 (magnitude, ±0)

**Solution**

1. Like the cabin, Earth falls freely, here under the Moon's pull, so treat Earth's centre as the centre crumb and the oceans as the crumbs.
2. The Moon pulls the near side harder than the centre, so compared with the centre the near side drifts toward the Moon. It pulls the far side less than the centre, so compared with the centre the far side drifts away from the Moon.
3. Around the ring halfway between, the pulls slant in toward Earth's centre, so the water there is drawn down. The result is two piles, one under the Moon and one opposite, and a low ring between: a harbour passes both piles as Earth turns, giving two high tides.
4. No part of the Moon is at Earth, and only matter at the spot makes a room-changing part. So at Earth the Moon makes only the shape-changing part: 2 out along the line, 1 in and 1 in across it, which add to zero. The oceans' total room is unchanged.

### `wave-tide-on-a-detector` · working · difficulty 2 · calculation

A plane gravitational wave with plus polarization $h_+ = h_0\cos[2\pi f(t - z/c)]$, $h_0 = 1.0\times10^{-21}$, $f = 100$ Hz, passes two free mirrors $L = 4.0$ km apart along $x$. Write the electric part of the Weyl tensor for an observer at rest; find the largest relative acceleration of the mirrors and the amplitude of the change in their separation; check that the trace is zero and say what that means for a ring of free mirrors in the $x$-$y$ plane.

**Hints**

1. For a plane wave $R_{\hat\imath\hat 0\hat\jmath\hat 0} = -\tfrac12\ddot h_{ij}/c^2$, and in vacuum $C = R$.

**Answer:** $E = -\tfrac12\ddot h_+\,\mathrm{diag}(1, -1, 0)$; largest relative acceleration $7.9\times10^{-13}\ \mathrm{m/s^2}$, separation amplitude $2.0\times10^{-18}$ m; trace zero, so the ring's area is unchanged to first order.

**Must contain:** E equals minus one half the second time derivative of h plus, times diag of one, minus one, zero; Acceleration about eight times ten to the minus thirteen metres per second squared; separation amplitude two times ten to the minus eighteen metres; Zero trace: the ring stretches along x and squeezes along y equally, keeping its area to first order

**Numeric:** largest relative acceleration of the mirrors = 7.9e-13 m/s^2 (magnitude, ±5%); amplitude of the change in separation = 2e-18 m (magnitude, ±5%)

**Solution**

1. With $h_{xx} = -h_{yy} = h_+$ and $C = R$ in vacuum, $E_{xx} = -\tfrac12\ddot h_+$, $E_{yy} = +\tfrac12\ddot h_+$, $E_{zz} = 0$.
2. The drift law $\ddot\xi^x = -E_{xx}\xi^x = \tfrac12\ddot h_+\,\xi^x$, with $\xi^x = L$ to zeroth order, integrates to $\xi^x = L(1 + \tfrac12h_+)$: the separation oscillates with amplitude $\tfrac12h_0L = 2.0\times10^{-18}$ m.
3. The largest acceleration is $\tfrac12h_0(2\pi f)^2L = 0.5 \times 10^{-21} \times (628)^2 \times 4000 = 7.9\times10^{-13}\ \mathrm{m/s^2}$.
4. $E_{xx} + E_{yy} + E_{zz} = 0$. A ring of mirrors in the $x$-$y$ plane becomes an ellipse stretched along $x$ by $\tfrac12h_+$ and squeezed along $y$ by the same fraction, so its area is unchanged to first order in $h_0$.

**Targets:** `weyl-only-for-light`

### `isotropy-kills-weyl` · formal · difficulty 2 · proof

Suppose that at each event a spacetime admits a unit timelike vector such that the geometry is invariant under every rotation of that vector's rest space. Show that the Weyl tensor vanishes there, and conclude that every homogeneous, isotropic cosmological model is locally conformally flat.

**Answer:** The electric and magnetic parts are rotation-invariant symmetric trace-free tensors on the rest space, hence multiples of the spatial metric, hence zero; they determine $C$, so $C = 0$, and the Weyl–Schouten theorem gives local conformal flatness.

**Must contain:** E and B are rotation-invariant symmetric trace-free tensors on the rest space, hence multiples of the metric, hence zero; Vanishing Weyl in four dimensions is local conformal flatness by the Weyl–Schouten theorem

**Solution**

1. Relative to $u$, define $E_{ab} = C_{acbd}u^cu^d$ and $B_{ab} = \tfrac12\epsilon_{acef}C^{ef}{}_{bd}u^cu^d$. Both are symmetric, trace-free and orthogonal to $u$, so they are tensors on the rest space $u^\perp$, and the Weyl tensor is a linear function of $E$, $B$ and $u$.
2. A rotation of $u^\perp$ fixes $u$ and maps $E$ and $B$ to the parts of the rotated geometry, which by hypothesis equal $E$ and $B$. So both are invariant under the whole rotation group of $u^\perp$.
3. A symmetric tensor on three-dimensional Euclidean space that commutes with every rotation has every direction as an eigenvector with one eigenvalue, so it is $\lambda h_{ab}$ with $h$ the spatial metric; proper rotations act on the pseudotensor $B$ in the same way. Trace-free gives $3\lambda = 0$, so $E = B = 0$ and hence $C_{abcd} = 0$.
4. A homogeneous, isotropic model is isotropic about its comoving observers at every event, so $C = 0$ everywhere, and in four dimensions the Weyl–Schouten theorem makes the metric locally conformally flat.

## Observations

- **Two high tides and two low tides a day in most harbours, following the Moon** (measured, entry). Earth falls freely around the Moon. The Moon's pull differs across Earth's width, stretching Earth along the line to the Moon and squeezing it across. That is the shape-changing part, made from across empty space; the Moon adds no room-changing part at Earth, because no part of the Moon is here. The oceans flow into the two piles. *Numbers:* The Moon's stretch at Earth's surface is about one part in nine million of Earth's own pull. On an Earth covered by deep ocean, it alone would raise the sea by about a third of a metre under the Moon and on the far side. It would lower the sea by about a sixth of a metre around the ring between. The Sun adds a little under half as much. *Reference:* Isaac Newton (1687), *Philosophiae Naturalis Principia Mathematica*, Royal Society, London; Book III
- **GW150914, the first gravitational wave detected, on 14 September 2015** (measured, working). A gravitational wave in vacuum is pure Weyl curvature, $C = R$. For a detector at rest its electric part is $E_{xx} = -E_{yy} = -\tfrac12\ddot h_+$ with zero trace, so one arm is stretched while the perpendicular arm is squeezed by the same fraction; the two LIGO interferometers measured that difference. *Numbers:* Peak strain about $1.0\times10^{-21}$, so each 4 km arm changed by about $2\times10^{-18}$ m at the peak. *Reference:* B. P. Abbott, R. Abbott, T. D. Abbott, M. R. Abernathy and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Predict, then split and name** (entry). Set the cabin falling with only crumbs inside and ask for the ball's shape and room after a minute. Then add the three drifts, fill the ball with dust at rest, and name the two tables. *Why:* The surprise, an egg with no matter in the cabin, is the whole reason the Weyl tensor exists. *Predict:* Will the ball change its shape? Will the room it takes up change? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `checks/ball-above-the-air`, `ways_in/take-the-shrinking-out-of-the-drift`, `checks/three-places`
2. **Read it in the sea** (entry). Turn Earth into the ball and the oceans into the crumbs, then walk through the two piles and the tide gauge. *Why:* The Moon shows that the shape-changing part needs no matter at the spot and comes from matter elsewhere. *Predict:* How many high tides should a harbour get in a day: one, or two? *Uses:* `ways_in/the-part-that-lives-in-empty-space`, `observations/ocean-tides`
3. **Build the tensor, then measure it in vacuum** (working). Fix the coefficients by contraction and count twenty as ten plus ten; then define the electric part and compute the Moon's and the wave's tides. *Why:* The electric part ties the ten components to accelerations a laboratory can read. *Visual:* [[six-entry-curvature-table]] *Uses:* `derivations/kill-every-trace`, `ways_in/subtract-every-trace`, `worked_examples/schwarzschild-is-pure-weyl`, `checks/vacuum-leftover`, `ways_in/the-electric-part-is-the-vacuum-tide`, `checks/moon-stretch`, `problems/wave-tide-on-a-detector`
4. **Structure and the observer split** (formal). Present the Ricci decomposition and the three-dimensional collapse, then conformal invariance with its index caveat, then the observer split and the isotropy proof. *Why:* The decomposition makes the count and the three-dimensional vanishing theorems, not coincidences. *Uses:* `ways_in/trace-free-part-conformal-class-and-observer-split`, `checks/rescale-the-lowered-weyl`, `checks/conformally-flat-in-three-dimensions`, `problems/isotropy-kills-weyl`

## Analogies

### A magnifying glass and an astigmatic lens · working

Send a narrow bundle of light rays through a region. Where the rays cross matter, Ricci curvature focuses the bundle equally in every transverse direction, so a small circular image is magnified and stays round, like a plain converging lens. Where the rays pass beside matter, only Weyl curvature acts: it focuses in one transverse direction and defocuses in the perpendicular one, so a small circle becomes an ellipse of the same area, like an astigmatic lens.

| In the analogy | Stands for |
| --- | --- |
| the plain converging lens | Ricci curvature along the bundle, from matter on its path |
| the astigmatic lens | Weyl curvature along the bundle, from matter beside its path |

*Limits:* Light bundles feel the Ricci and Weyl components along the ray's null direction, not the electric part an observer's test masses feel; a glass lens works by refraction, not curvature.

## Misconceptions

### “Beside a planet there is no matter, so nothing there can make a ball of crumbs change.” · entry · `empty-space-cannot-stretch`

- **Why it is tempting:** Matter curves space and time, so no matter sounds like no curving.
- **What is true:** Matter at the spot sets only the room-changing part. The shape-changing part comes from matter elsewhere, and beside a planet it is all the drift.
- **Exposed by:** `checks/ball-above-the-air`

### “Weyl curvature matters only for light rays, as a distortion of images.” · working · `weyl-only-for-light`

- **Why it is tempting:** The lens picture of circles sheared into ellipses is the usual illustration.
- **What is true:** In vacuum the electric part of the Weyl tensor is the entire tidal tensor on any free test mass; the Moon's ocean tide and a wave's push on mirrors are Weyl curvature.
- **Exposed by:** `checks/moon-stretch`

### “Einstein's vacuum equation says the Ricci tensor is zero, so empty spacetime is flat.” · working · `vacuum-means-flat`

- **Why it is tempting:** The field equation calls the Ricci tensor the curvature, and zero curvature sounds like flat.
- **What is true:** Zero Ricci removes only ten of the twenty Riemann components; the ten Weyl components survive and make the tides of empty space.
- **Exposed by:** `checks/vacuum-leftover`

### “The Weyl tensor is unchanged by a conformal rescaling in any index position.” · formal · `conformal-invariance-any-index`

- **Why it is tempting:** Raising and lowering indices is usually treated as pure notation.
- **What is true:** Only the form with one index up is invariant; each lowering with the rescaled metric multiplies by the conformal factor squared, each raising divides by it.
- **Exposed by:** `checks/rescale-the-lowered-weyl`

### “Since the Weyl tensor vanishes in three dimensions, every three-dimensional metric is conformally flat.” · formal · `three-dimensions-conformally-flat`

- **Why it is tempting:** In four or more dimensions a vanishing Weyl tensor is exactly local conformal flatness.
- **What is true:** The Weyl criterion needs at least four dimensions; in three the Cotton tensor decides, and generic three-metrics fail it.
- **Exposed by:** `checks/conformally-flat-in-three-dimensions`

## Checks

1. **Entry · predict** `checks/ball-above-the-air`. A cabin with no air inside it falls straight down from rest, 400 kilometres above Earth's surface, far above Earth's air. Inside it, crumbs are held at rest on a small imaginary ball one metre across around a centre crumb, then let go. Nothing else is in the cabin. After one minute, does the ball still have its shape? Does it still take up the same room? Where does any change come from, if no matter is in the cabin?
   - **Hints:** Which crumb does Earth pull hardest: the top one, the centre one or the bottom one? / Add up the drifts along three directions at right angles.
   - **Answer:** The ball becomes an egg. The top and bottom crumbs, on the line toward Earth's centre, end up about two millimetres farther from the centre crumb. That is because Earth pulls the lower crumb harder, and the upper crumb less, than it pulls the centre crumb. The crumbs around the middle end up about one millimetre nearer, because Earth's pull on them slants in toward the line from the centre crumb to Earth's centre. Two out, one in and one in add to zero. So at first the room the ball takes up does not change. The drift is pure shape-changing part, and it comes from Earth below, not from anything in the cabin.
   - **Must contain:** The ball becomes an egg: top and bottom crumbs out about two millimetres, side crumbs in about one; The room it takes up does not change at first, because the drifts add to zero; The change comes from Earth below, with no matter in the cabin
   - **Numeric:** extra distance of the top crumb from the centre crumb after one minute = 2.3 mm (magnitude, ±0.5); distance a side crumb moves toward the centre crumb after one minute = 1.2 mm (magnitude, ±0.3)
   - **Targets:** `empty-space-cannot-stretch`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · explain** `checks/three-places`. Crumbs are let go at rest on a small ball inside a freely falling cabin, in each of three places. First, far from any planet, inside a huge round cloud of dust that is spread evenly and at rest around the cabin. Second, beside a planet, with nothing in the cabin. Third, far from everything, as a gravitational wave passes. A gravitational wave is a pattern of stretch and squeeze that travels through empty space, made by distant violently moving masses. For each place, say whether the ball shows a room-changing part, a shape-changing part, both or neither, and what the ball looks like after a while.
   - **Hints:** Is there matter inside the ball of crumbs? / Add the drifts in three directions at right angles.
   - **Answer:** In the dust cloud, only the room-changing part. Every crumb drifts in by the same amount, because the dust inside the ball pulls each crumb toward the centre crumb and is the same on every side. So the ball stays round and shrinks. Beside the planet, only the shape-changing part. There is no matter in the cabin, so there is no room-changing part, and the planet's pull differs from crumb to crumb. So the ball becomes an egg along the line to the planet and keeps its room. In the wave, only the shape-changing part again. There is no matter at the spot, so there is no room-changing part, and any drift the wave makes must be shape-changing. The wave stretches the ball one way and squeezes it across by the same fraction, back and forth. So wherever there is no matter, the shape-changing part is all the drift there is.
   - **Must contain:** Dust at rest: room-changing part only, the ball stays round and shrinks; Beside a planet and in a wave: shape-changing part only, the room unchanged; Where there is no matter, the shape-changing part is all the drift
   - **Visual:** [[falling-ring-of-crumbs]]
3. **Working · numeric** `checks/moon-stretch`. The Moon's mass times the gravitational constant is 4.903 times ten to the twelve cubic metres per second squared, and the Moon is 384 400 kilometres from Earth's centre. Write the electric part of the Weyl tensor the Moon produces at Earth's centre for an observer falling with Earth, give its trace, and compute the acceleration, relative to Earth's centre, of a free particle on Earth's surface at the point facing the Moon, 6371 kilometres from the centre.
   - **Hints:** The radial entry of the electric part outside a spherical mass is minus two GM over d cubed.
   - **Answer:** Outside the Moon the tide is pure Weyl, so $E = (GM/d^3)\,\mathrm{diag}(-2,1,1)$ with the first axis along the line to the Moon: $GM/d^3 = 4.903\times10^{12}/(3.844\times10^8)^3 = 8.63\times10^{-14}\ \mathrm{s^{-2}}$. The trace is $(-2 + 1 + 1)\,GM/d^3 = 0$. The drift law $\ddot\xi = -E\xi$ gives, for a particle at $\xi = 6.371\times10^6$ m along the line, $\ddot\xi = 2 \times 8.63\times10^{-14} \times 6.371\times10^6 = 1.1\times10^{-6}\ \mathrm{m/s^2}$ away from Earth's centre, one part in nine million of $g$. It acts on rock and water alike; this is the lunar tide, not an effect on light.
   - **Must contain:** E is GM over d cubed times diag of minus two, one, one along the Earth-Moon line, with zero trace; Relative acceleration about one point one times ten to the minus six metres per second squared, away from Earth's centre; It acts on any free mass, not only on light
   - **Numeric:** relative acceleration of the surface particle facing the Moon = 1.1e-06 m/s^2 (magnitude, ±5%); trace of the electric part divided by GM over d cubed = 0 1 (magnitude, ±0.01)
   - **Targets:** `weyl-only-for-light`
4. **Working · explain** `checks/vacuum-leftover`. In a vacuum region of four-dimensional spacetime with no cosmological constant, how many independent components can the Riemann tensor have at an event, and why does it equal the Weyl tensor there? What changes in a world with two space dimensions and one time dimension?
   - **Hints:** Count Riemann components minus Ricci components in each dimension.
   - **Answer:** The vacuum equation $R_{\mu\nu} = 0$ sets the ten Ricci components to zero, so of the twenty Riemann components ten survive. Because the Ricci tensor and scalar vanish, every subtracted term in the Weyl formula is zero and $C_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu}$: the surviving ten are the Weyl components, which is why empty space beside a star is curved and has tides. In three dimensions the Riemann tensor has six components and the Ricci tensor six, the Ricci tensor determines the Riemann tensor, and the Weyl tensor vanishes identically; so vacuum there is flat and a planet in that world would raise no tides in the empty space around it.
   - **Must contain:** Ten Riemann components survive the vacuum equation in four dimensions, and with Ricci zero they are the Weyl components; In three dimensions Ricci fixes Riemann and Weyl is identically zero, so vacuum is flat
   - **Numeric:** independent Riemann components in four-dimensional vacuum = 10 1 (magnitude, ±0)
   - **Targets:** `vacuum-means-flat`
   - **Visual:** [[twenty-of-256-slots]]
5. **Formal · derive** `checks/rescale-the-lowered-weyl`. Given that $\tilde C^{\rho}{}_{\sigma\mu\nu} = C^{\rho}{}_{\sigma\mu\nu}$ under $\tilde g_{\mu\nu} = \Omega^2 g_{\mu\nu}$, find how $\tilde C_{\rho\sigma\mu\nu}$, $\tilde C^{\rho\sigma\mu\nu}$ and the invariant $\tilde C_{\rho\sigma\mu\nu}\tilde C^{\rho\sigma\mu\nu}$ are related to their unrescaled values.
   - **Hints:** Count the uses of the rescaled metric and its inverse.
   - **Answer:** Lowering the first index uses $\tilde g_{\rho\lambda} = \Omega^2 g_{\rho\lambda}$, so $\tilde C_{\rho\sigma\mu\nu} = \Omega^2 C_{\rho\sigma\mu\nu}$. Raising the other three uses $\tilde g^{\mu\nu} = \Omega^{-2}g^{\mu\nu}$ three times, so $\tilde C^{\rho\sigma\mu\nu} = \Omega^{-6}C^{\rho\sigma\mu\nu}$. The invariant scales as $\Omega^{2}\Omega^{-6} = \Omega^{-4}$, as a quantity of dimension inverse length to the fourth must. Only the mixed form with one index up is invariant.
   - **Must contain:** All-lowered form scales by omega squared; All-raised form scales by omega to the minus six; The squared invariant scales by omega to the minus four
   - **Numeric:** power of omega multiplying the squared invariant = -4 1 (signed, ±0)
   - **Targets:** `conformal-invariance-any-index`
6. **Formal · evaluate-claim** `checks/conformally-flat-in-three-dimensions`. Evaluate the claim: 'In three dimensions the Weyl tensor vanishes identically, so every three-dimensional Riemannian metric is locally conformally flat.'
   - **Hints:** Count the free functions in a conformally flat metric and in an arbitrary metric modulo coordinates.
   - **Answer:** False. The Weyl–Schouten criterion holds only for $n \ge 4$. In three dimensions the obstruction is the Cotton tensor, built from first derivatives of the Schouten tensor, and generic metrics have it nonzero. A count shows why: a three-dimensional metric has 6 components, local diffeomorphisms remove 3 and a conformal factor removes 1, leaving 2 free functions per point in the conformal class, while a conformally flat metric has none. In two dimensions the same count gives $3 - 2 - 1 = 0$, matching the theorem that every surface is locally conformally flat.
   - **Must contain:** The Weyl criterion needs dimension at least four; in three the Cotton tensor is the obstruction; Counting free functions: six minus three minus one leaves two, so generic three-metrics are not conformally flat; In two dimensions the count gives zero and every metric is locally conformally flat
   - **Numeric:** free functions per point in a three-dimensional conformal class = 2 1 (magnitude, ±0)
   - **Targets:** `three-dimensions-conformally-flat`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign and arrangement of the Ricci terms in the Weyl formula | With $R_{\sigma\nu} = g^{\rho\mu}R_{\rho\sigma\mu\nu}$, the Ricci terms enter with $-\tfrac12$ and the scalar term with $+\tfrac{R}{6}$, as in the four-dimensional key equation. | Some texts contract the first and fourth slots, or use the opposite Riemann sign, which flips the correction terms; many write them with antisymmetrization brackets, which hide factors of two. Check trace-freeness before copying. |
| Sign of the magnetic part | $B_{ab} = \tfrac12\epsilon_{acef}C^{ef}{}_{bd}u^cu^d$ with $\epsilon_{0123} = +\sqrt{-g}$; for the Weyl tensor the left and right duals coincide. | Some texts use $\epsilon_{0123} = -\sqrt{-g}$, or put a minus sign in front of the dual, which flips the sign of $B$; squared invariants are unaffected. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The central picture: a ball of falling crumbs whose drift is split live into the same-in-every-direction part and the balanced leftover, beside a planet, inside dust and in a wave. *Sketch:* This concept adds a two-part readout beside the ball mode: the mean of the three principal drifts drawn as uniform in-or-out arrows, and the leftover drawn as stretch-and-squeeze arrows, with the volume ratio. A source switch chooses a planet below with mass and distance sliders, dust at rest with a density slider, or a passing plane wave. The two arrow sets are never shown summed, so the learner sees that the leftover alone makes the egg.
- [[six-entry-curvature-table]] (core): The subtraction made visible: six orthonormal entries, their Ricci traces, and the Weyl remainder. *Sketch:* This concept adds a Weyl column: the six entries with their trace parts removed, greying to zero for the expanding-universe preset and equal to the Riemann entries for the star-exterior preset.
- [[twenty-of-256-slots]] (supporting): The split of the surviving count into Ricci and Weyl components as the dimension changes.
- [[circles-behind-a-see-through-star]] (supporting): Ricci magnifies, Weyl shears: small circles seen through and beside a transparent star. *Sketch:* A field of small circles behind a transparent star that does not refract. Circles seen through the star are magnified but stay round; circles seen beside it become ellipses pointing around the star, with area unchanged to first order. A cursor readout shows convergence and shear.

## Tutor moves

**Open with**

- Picture a cabin falling freely toward Earth, far above the air, with nothing inside but crumbs let go on a small ball. Will the ball keep its shape? Will it keep the room it takes up? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why two out, one in and one in leaves the room unchanged.* → Have them count edge lengths: a box 10 by 10 by 10 that becomes 12 by 9 by 9 holds 972 instead of 1000, a change far smaller than any edge's; then do the sum 2 minus 1 minus 1. *Uses:* `ways_in/take-the-shrinking-out-of-the-drift`

**Common questions**

- *Why split the curving into two tables at all?* (entry) One big table does hold everything. The split answers two different questions. Matter right at a spot fixes the room-changing part. The shape-changing part is not fixed by anything at the spot; it carries gravity from far away. So the split shows which part of the curving is local and which part travels. *Uses:* `ways_in/take-the-shrinking-out-of-the-drift`, `ways_in/the-part-that-lives-in-empty-space`

**Switching levels**

- To working when: asks for the formula; asks how many numbers the shape-changing part has. Go to the subtraction and the count of twenty as ten plus ten. *Uses:* `ways_in/subtract-every-trace`, `derivations/kill-every-trace`
- To formal when: asks why three dimensions are special; asks about conformal transformations or the magnetic part. Go to the Ricci decomposition and the observer split. *Uses:* `ways_in/trace-free-part-conformal-class-and-observer-split`

**Pronunciations:** Weyl → VILE, rhymes with mile; Schouten → SKHOW-ten; Kulkarni–Nomizu → kool-KAR-nee no-MEE-zoo; Petrov → peh-TROFF

**Voice notes:** Say 'shape-changing part' and 'room-changing part' at entry, and introduce the name Weyl, rhyming with mile, once the split is clear. Say 'the electric part', never the letter E.

## History

- **Hermann Weyl (1918).** Introduced the trace-free conformal curvature tensor while building a geometry in which the metric may be rescaled from point to point, and showed that this tensor is unchanged by such rescalings. Hermann Weyl (1918), *Reine Infinitesimalgeometrie*, Mathematische Zeitschrift 2, 384–411, doi:10.1007/BF01199420

## Research horizon

- **Petrov types and the peeling of radiation.** At a point the Weyl tensor has up to four principal null directions, and their coincidences sort it into the Petrov types I, II, D, III, N and O. Far from an isolated radiating source the types peel apart along outgoing light rays, the type N part falling as $1/r$, and numerical relativity extracts gravitational waveforms from the Weyl scalar that carries that part. A. Z. Petrov (1954), *Classification of spaces defining gravitational fields*, Uchenye Zapiski Kazanskogo Gosudarstvennogo Universiteta 114 (8), 55–69; English translation in General Relativity and Gravitation 32, 1665–1685 (2000), doi:10.1023/A:1001910908054; Ezra Newman, Roger Penrose (1962), *An Approach to Gravitational Radiation by a Method of Spin Coefficients*, Journal of Mathematical Physics 3, 566–578, doi:10.1063/1.1724257
- **The Weyl curvature hypothesis.** Penrose proposed that the Weyl tensor vanishes, or is strongly constrained, at initial singularities such as the big bang but not at final ones, and that a measure of gravitational entropy should grow with Weyl curvature, giving the arrow of time a geometric origin. What that entropy measure is, and whether the hypothesis follows from any dynamics, remain open. Roger Penrose (1979), *Singularities and time-asymmetry*, General Relativity: An Einstein Centenary Survey, eds S. W. Hawking and W. Israel, Cambridge University Press, 581–638
- **Electric and magnetic parts as a Maxwell-like system.** Written in terms of $E_{ab}$ and $B_{ab}$ relative to a family of observers, the Bianchi identities take a form close to Maxwell's equations, with matter gradients as sources. This covariant approach underlies much of relativistic cosmology; whether the magnetic part can consistently be set to zero, as in the proposed silent universes, turned out to be a delicate integrability question. George F. R. Ellis (1971), *Relativistic cosmology*, Proceedings of the International School of Physics Enrico Fermi, Course 47, ed. R. K. Sachs, Academic Press, 104–182; reprinted in General Relativity and Gravitation 41, 581–660 (2009), doi:10.1007/s10714-009-0760-7; Roy Maartens, Bruce A. Bassett (1998), *Gravito-electromagnetism*, Classical and Quantum Gravity 15, 705–717, doi:10.1088/0264-9381/15/3/018

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** You let go of crumbs on a ball inside a falling cabin. Near Earth the ball turns into an egg: the top and bottom crumbs move out, the ones round the middle move in half as much, though I'm not sure why half. Inside a dust cloud every crumb moves in the same amount and the ball just shrinks. You split any drift into a same-in-every-direction bit, which changes how much room the ball takes up, and a leftover, which only changes the shape. I don't know how much of the drift counts as the first bit; you just add three numbers and see if you get zero. The Ricci table holds the first bit and matter at the spot sets it; the Weyl table holds the leftover. Near Earth it's all leftover, and after a minute the crumbs have moved about two millimetres. The Moon does the same to Earth: the near side gets pulled toward the Moon, the far side away, which sounds odd, so the sea piles up on both sides and you get two high tides a day. Earth 'falls around the Moon', which I thought was backwards. The Sun does less than half as much even though it's huge, and I don't see why.

**Stumbles (17)**

- “Part of their drift changes the room the ball takes up, and matter right there sets that part. The rest changes only the ball's shape. The Weyl tensor is the table that holds this shape-changing part.”: 'Right there' has no reference, and the claim is unscoped: with matter streaming past the cabin the Ricci table holds a shape change too, as the way's simplifies says.
- “The crumbs around the ball's middle drift in toward the centre crumb, each by half as much.”: A surprising number with no reason; the reader cannot see where 'half' comes from, yet the 2 minus 1 minus 1 sum later rests on it. The rule it rests on, drifts add to zero with nothing among the crumbs, was borrowed from the Ricci note and not restated.
- “The two crumbs on the line toward Earth's centre, the top and bottom of the ball, drift away from the centre crumb.”: 'Top' and 'bottom' have no reference in a falling cabin, and the drift outward is stated with no reason.
- “Every crumb drifts in toward the centre crumb by the same amount, whatever direction it lies in.”: No reason given for 'same amount in every direction'.
- “The first part is the same drift in every direction, all in or all out. … The second part is whatever is left once the first is taken away.”: Step left implicit: how big is the first part? Without a rule the reader cannot do the split themselves, and 'whatever is left' is ambiguous.
- “by amounts that balance”: 'Balance' is a new word for 'add up to zero', which the way already uses; two words for one idea.
- “Dark energy adds a same-in-every-direction push, far too small to notice in a cabin.”: Undefined term at entry, not in the glossary, and not needed for the way's claim.
- “Earth is a ball falling freely around the Moon, and the water of its oceans plays the crumbs.”: Surprising claim with no reason: a teenager knows the Moon goes around Earth and reads this as backwards.
- “The Moon pulls the near side of Earth a little harder than Earth's centre, and the centre a little harder than the far side. Compared with the centre, then, the near side is pulled toward the Moon and the far side is pulled away from it.”: 'Near side' and 'far side' are used before they are named, the reason (pull weakens with distance) is missing, and 'the far side is pulled away' skips the step that makes it true: it is pulled less than the centre, so it lags behind.
- “Around the ring halfway between, the pulls slant in toward the centre.”: Halfway between what? Slant relative to what, and why?
- “As Earth turns once, the harbour passes both piles and both low rings”: There is one low ring, crossed twice; 'both low rings' contradicts the picture just drawn.
- “The Sun does the same, a little less than half as strongly, because it is far heavier but much farther away.”: A teenager who knows the Sun holds Earth in orbit is surprised that its stretch is smaller than the Moon's; 'heavier but farther' does not say why the stretch loses while the pull wins.
- “A cabin with the air pumped out falls straight down from rest, 400 kilometres above Earth, far above the air.”: 'Air' used in two senses in one sentence: the air inside the cabin and Earth's atmosphere.
- “Crumbs are let go on a small ball in three places. First, inside a huge round cloud of dust, far from any planet, with the dust at rest around the cabin. … Third, far from everything, as a gravitational wave passes.”: Starting state ambiguous: 'in three places' reads as three places on the ball, and 'the cabin' appears before any cabin is mentioned. The wave is not prepared by any entry way, so the check must say what a gravitational wave is and the answer must show the reasoning that gets there.
- “Explain also why the Moon does not change the total room the oceans take up.”: The first what-if a teenager tries: water cannot be squeezed anyway, so the question has an answer that has nothing to do with the split.
- “Will the ball keep its shape? Will it keep its size?”: 'Size' is a second word for 'room', the word every entry way uses.
- “Its zero trace is the cancelling of the three drifts in 'The part that lives in empty space'.”: Ladder: the three drifts were counted in 'Take the shrinking out of the drift', not in the tides way, and the electric-part way's first sentence did not refer back to the way it continues.

**Fixes**

- Summary and the Weyl glossary entry scoped: the Weyl table is the part of the drift that no matter at the spot sets, which is exactly the shape-changing part with nothing in the cabin or with dust at rest around it; the way's closing paragraph says the same in one sentence.
- Way 'Take the shrinking out of the drift': recap now restates the Ricci rule (with nothing among the crumbs the three drifts add to zero; dust makes the ball shrink); every drift direction and the 'half as much' get their reason; the split gets its rule (average the three drifts); 'balance' became 'add up to zero'; top and bottom got their reference; the dark-energy sentence was dropped as the lowest-value item.
- Way 'The part that lives in empty space': Earth's free fall, the near and far sides, the lagging far side, the slanting ring and the Sun's smaller stretch each got a reason; 'both low rings' corrected to crossing one low ring twice; 'under the Moon' became 'on the near side'.
- Checks: 'ball-above-the-air' no longer uses 'air' in two senses and names the line the side crumbs slant toward; 'three-places' states its starting state, defines a gravitational wave, and reasons from 'no matter at the spot' to 'no room-changing part'.
- Problem 'two-high-tides' asks why the Moon makes no room-changing part at Earth instead of why the oceans' room is unchanged; the opening question says 'room' instead of 'size'; glossary 'room' no longer uses 'space' in a second sense.
- Ladder: 'The electric part is the vacuum tide' opens by referring back to the tides way it continues, and points the three-drift cancellation to the way that counted it; added index-notation as a working prerequisite, since the working formula is the first four-index expression a reader meets here.
- Budget: entry explanations are 1013 words, 13 past the core cap of 1000 and within the 10 percent review allowance; extras, support, tutoring, links and total are past their 80 percent draft lines but under every cap. All growth is the recorded fixes; no sentence was compressed to fit.

**Concerns**

- The 'half as much' inward drift is now backed by the adds-to-zero rule rather than by a picture of why Earth's pull slants; a physics reviewer may prefer a slanting-pull reason, which needs the inverse-square fall-off and is beyond an entry reader.
- The gravitational-wave case in 'three-places' is reachable by reasoning (no matter at the spot, so no room-changing part) but is not shown in any entry way; a third entry way on waves was cut for budget by the previous stage and the check now carries a one-sentence definition instead.
- The tide numbers (one part in nine million; a third of a metre up, a sixth down) were checked with python3 in this review and match the working-rung check; the observation still cites Newton's Principia without a doi.
- The prerequisite 'index-notation' added here differs from the registry; sync_registry.py needs to run after review.
- Entry way 'Take the shrinking out of the drift' now runs 557 words with three pictures (egg, dust ball, the split); it stays at one new idea, the split, but a future edit should not add to it.

**Re-read** (2026-09-16, revision 4): 2 stumbles in 3 changed passages

- “inside a huge round cloud of dust spread evenly, far from any planet”: The comma lets 'spread evenly' run into 'far from any planet', so for a moment the dust seems to be spread evenly far from any planet rather than spread evenly around the cabin.
- “Earth falls freely in the Moon's pull”: 'Falls freely' sounds as if Earth were dropping onto the Moon, and the problem no longer links Earth to the cabin picture the statement asks for.
- Fix: three-places question: reordered the first place so 'spread evenly and at rest around the cabin' stays together and 'far from any planet' comes first.
- Fix: two-high-tides solution step 1: 'Like the cabin, Earth falls freely, here under the Moon's pull'. Same claim; the way's dust-cloud sentence read cleanly and was left as it was.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Four-dimensional Weyl formula: coefficients -1/2 on the four metric-times-Ricci terms and +R/6 on the metric pair, with the course contraction $R_{\sigma\nu} = g^{\rho\mu}R_{\rho\sigma\mu\nu}$.: Re-derived the contraction in 'Kill every trace' by hand: alpha bracket gives $(n-2)R_{\sigma\nu} + Rg_{\sigma\nu}$, beta bracket $(n-1)g_{\sigma\nu}$, so $\alpha = -1/(n-2)$, $\beta = 1/((n-1)(n-2))$. Then python3: random algebraic curvature tensors (sums of Kulkarni-Nomizu products) in n = 3, 4, 5 with Lorentzian metric; contracted C over slots 1-3, 1-4 and 1-2. → Every trace vanishes to 1e-15 in each dimension; the constant-curvature check in step 8 gives coefficient $K[1 - 2(n-1)/(n-2) + n/(n-2)] = 0$. Correct.
- In three dimensions the Weyl tensor vanishes identically; component counts 6 + 0, 10 + 10, 15 + 35.: Numeric n = 3 Weyl tensor of a random curvature tensor; formula $n(n+1)(n+2)(n-3)/12$ against $n^2(n^2-1)/12 - n(n+1)/2$. → $|C| = 2\times10^{-15}$ for n = 3; dimensions 0, 10, 35 match the visual sketch and the way.
- Formal way: $R = C + P \owedge g$ with the Schouten tensor, and the Ricci trace of $h \owedge g$ is $(n-2)h + (\mathrm{tr}\,h)g$.: Expanded $P \owedge g$ by hand and matched it term by term with the working formula; numeric check of the trace identity. → Matches exactly; trace residual 0. Injectivity for n >= 3 follows since $2(n-1)\,\mathrm{tr}\,h$ is recovered first.
- Conformal scaling: $\tilde C^a{}_{bcd} = C^a{}_{bcd}$, lowered form $\Omega^2$, raised form $\Omega^{-6}$, squared invariant $\Omega^{-4}$; Weyl-Schouten for n >= 4, Cotton for n = 3, every surface conformally flat.: Hand check of index counting; the connection change $\delta^a_bW_c + \delta^a_cW_b - g_{bc}W^a$ and the Weyl-free correction of Riemann checked against the standard derivation; the argument that the $\tilde g$-trace-free projection of $\Omega^2X$ is $\Omega^2$ times the $g$-projection checked (same kernel, same complement). → Correct; the way says the Riemann change is quoted, and 'simplifies' records it.
- Observer split: E and B symmetric, trace-free, orthogonal to u; left and right duals agree for Weyl; $C_{abcd}C^{abcd} = 8(E_{ab}E^{ab} - B_{ab}B^{ab})$.: python3 with a random four-dimensional Weyl tensor, $u = e_0$, $\epsilon_{0123} = +1$, indices raised with eta. → Symmetry and trace residuals below 1e-15, $E_{0i} = 0$; left minus right dual 1.6e-15 for C (9.4 for the full Riemann tensor, as expected); $C\cdot C$ and $8(E^2 - B^2)$ agree to six decimals.
- Schwarzschild orthonormal components give Ricci = 0, C = R, $E = (GM/r^3)\,\mathrm{diag}(-2,1,1)$ and Kretschmann $48M^2/r^6 = 8E_{ab}E^{ab}$.: python3 with the six listed components and the Riemann symmetries. → All confirmed; the worked example's three Ricci sums (-2+1+1, 2-1-1, -1-1+2) are right with the time term entering through $\eta^{\hat t\hat t} = -1$.
- Signs of the drift law and the electric part: $\ddot\xi^{\hat\imath} = -c^2R^{\hat\imath}{}_{\hat0\hat\jmath\hat0}\xi^{\hat\jmath}$, $E_{ij} = c^2C_{\hat\imath\hat0\hat\jmath\hat0}$, radial entry negative means stretching; wave $E_{xx} = -E_{yy} = -\tfrac12\ddot h_+$.: Course geodesic deviation with $u^{\hat 0} = c$; plane-wave $R_{\hat\imath\hat0\hat\jmath\hat0} = -\tfrac12\ddot h_{ij}/c^2$ with the course Riemann sign; integrated $\ddot\xi^x = \tfrac12\ddot h_+L$. → Consistent throughout the note: $\xi^x = L(1 + \tfrac12h_+)$, stretch along x while y squeezes.
- Scope 'nothing in the cabin, or only dust at rest around it' makes the shape-changing part exactly the Weyl part.: Orthonormal decomposition $R_{\hat\imath\hat0\hat\jmath\hat0} = C_{\hat\imath\hat0\hat\jmath\hat0} + \tfrac12(\delta_{ij}R_{00} - R_{ij}) + \tfrac{R}{6}\delta_{ij}$; for a perfect fluid at rest $R_{ij} = 4\pi G(\rho - p)\delta_{ij}$, isotropic. → The Ricci contribution to the tide is pure trace for any fluid at rest with isotropic pressure (dust included, cosmological constant included); a fluid moving past adds $\gamma^2v_iv_j$ anisotropy. The novice's scope is correct and the 'simplifies' sentence about matter rushing past or pressing unequally is right.
- Dust cloud: every crumb drifts in by the same amount whatever its direction.: Newtonian potential inside a uniform sphere, $\Phi = \tfrac{2\pi G\rho}{3}(r^2 - 3R^2)$, Hessian $\tfrac{4\pi G\rho}{3}\delta_{ij}$ everywhere inside; a non-uniform outer cloud adds a trace-free (Weyl) tide. → True for a round cloud spread evenly, wherever the cabin sits inside it; the way and the check now say 'spread evenly'.
- Entry numbers: a one-metre ball 400 km up, one minute: top and bottom out about 2 mm, sides in about 1 mm.: python3: $GM/r^3 = 1.284\times10^{-6}\,\mathrm{s^{-2}}$ at r = 6771 km, drift $\tfrac12 a t^2$ with a = 2(GM/r^3)(0.5 m) and (GM/r^3)(0.5 m). → 2.31 mm and 1.16 mm, matching the numeric fields 2.3 +/- 0.5 and 1.2 +/- 0.3; $t\sqrt{2GM/r^3} = 0.096$ and the 15.6 km fall in a minute keep the linear estimate good to about one percent.
- Moon numbers: $GM/d^3 = 8.6\times10^{-14}\,\mathrm{s^{-2}}$, surface relative acceleration $1.1\times10^{-6}\,\mathrm{m/s^2}$, one part in nine million of g; equilibrium tide a third of a metre up, a sixth down; Sun a little under half.: python3 with GM = 4.903e12, d = 384 400 km, R = 6371 km, g = 9.81; tide height $GMR^2/(gd^3)$ times $P_2$; solar ratio $(M_\odot/M_{\rm Moon})(d/d_\odot)^3$. → 8.632e-14, 1.100e-6, g/a = 8.9 million, 0.357 m up, 0.179 m down, solar ratio 0.459. All match.
- Wave problem: separation amplitude 2.0e-18 m, largest relative acceleration 7.9e-13 m/s^2; GW150914 peak strain 1.0e-21.: python3: $\tfrac12h_0L$ and $\tfrac12h_0(2\pi f)^2L$; peak strain checked against the discovery paper's abstract. → 2.00e-18 m and 7.896e-13 m/s^2 within the 5 percent tolerances; peak strain 1.0e-21 confirmed.
- Tide-table slip of about fifty minutes a day; box 12 by 9 by 9 holds 972.: Lunar day 360/(360.986 - 13.18) solar days; 12*9*9. → 50.5 minutes; 972.
- Isotropy proof and the three-dimensional conformal count.: Checked Schur-type step (rotation-invariant symmetric tensor on R^3 is a multiple of the metric; proper rotations act on B as on a tensor) and the count 6 - 3 - 1 = 2, 3 - 2 - 1 = 0. → Sound as a proof sketch at formal rung.
- References.: One WebSearch each: Weyl 1918 Math. Z. 2, 384-411, doi 10.1007/BF01199420; Petrov 1954, translation Gen. Rel. Grav. 32, 1665-1685 (2000), doi 10.1023/A:1001910908054; Newman and Penrose 1962, J. Math. Phys. 3, 566-578, doi 10.1063/1.1724257; Penrose 1979 in the Einstein Centenary Survey, 581-638; Ellis 1971, Enrico Fermi Course 47 ed. Sachs, 104-182, reprinted Gen. Rel. Grav. 41, 581 (2009), doi 10.1007/s10714-009-0760-7; Maartens and Bassett 1998, Class. Quantum Grav. 15, 705-717, gr-qc/9704059; Abbott et al. 2016, Phys. Rev. Lett. 116, 061102; Newton 1687 Principia, Book III propositions 24, 36, 37 on the tides. → All eight confirmed and set verified; Ellis venue now names the editor and publisher. History scope confirmed: the conformal curvature tensor and its invariance under rescaling appear in Weyl's 1918 paper.

**Counterexamples tried**

- Cosmological constant: $\Lambda g_{\mu\nu}$ adds an isotropic Ricci term, so the shape-changing part is still all Weyl, but C = R fails; the note scopes C = R to vacuum with no cosmological constant. Passes.
- Matter streaming past the cabin, or anisotropic stress: the Ricci part of the tide acquires a trace-free piece; the summary, glossary and 'simplifies' scope the claim to nothing in the cabin or dust at rest. Passes.
- Lumpy or off-round dust cloud: the outer lumps add a Weyl tide, so the crumbs would not drift in equally; fixed by 'round' and 'spread evenly' in the way and the check.
- Three dimensions: Weyl vanishes yet generic metrics are not conformally flat (Cotton tensor); two dimensions: every metric is; both covered by the formal check.
- Observer moving sideways past the star: reads a different E; the note scopes the diag(-2,1,1) reading to observers at rest or falling radially. Passes.
- Euclidean signature in four dimensions: the Weyl space splits into self-dual and anti-self-dual halves under SO(4); the note says 'orthogonal group', which includes reflections and keeps it irreducible. Passes.
- Plane wave: B is nonzero for the observer at rest, but the note only gives E and says a single observer reads five of ten. Passes.
- Diurnal seas such as the Gulf of Mexico: scoped in the tides way's 'simplifies'. Passes.

**Fixes**

- Scoped the dust cloud as round and spread evenly in 'Take the shrinking out of the drift' and in check 'three-places', since a lumpy cloud adds a shape-changing tide from outside the ball.
- Problem 'two-high-tides' solution: 'Earth falls freely around the Moon' became 'Earth falls freely in the Moon's pull', matching the corrected way.
- All eight references confirmed and marked verified; Ellis 1971 venue now names the editor and publisher.
- Revision bumped to 3 for the learner-visible changes.

**Concerns**

- course-conventions.md does not fix the sign of the magnetic part of the Weyl tensor; the note uses $B_{ab} = {}^*C_{acbd}u^cu^d$ with the course $\epsilon_{0123} = +\sqrt{-g}$ and records the choice in a notation trap. The convention file should adopt or change this before the note is published.
- The working prerequisite 'index-notation' has a registry entry but no note yet, and the registry prerequisites differ; sync_registry.py must run.
- Penrose 1979 is a book chapter carried with kind 'paper' because the schema has no chapter kind.
- The formal way quotes the conformal change of Riemann, the Weyl-Schouten theorem, the Cotton criterion and $C\cdot C = 8(E^2 - B^2)$ without derivation; the identity was checked numerically here, the theorems are standard.

**Diff check** (2026-09-16, revision 4)

- Inside a huge round cloud of dust spread evenly, every crumb drifts in by the same amount whatever its direction, wherever the cabin sits in the cloud (way, check three-places).: python3 finite-difference Hessian of the uniform-sphere gravity field at an off-centre interior point; compared with the Newtonian limit of the Ricci tide for dust at rest, R_00 = 4 pi G rho. → Hessian equals (4 pi G rho/3) times the identity, inward, at every interior point; the cloud outside the ball contributes no tide. Round and evenly spread are both needed: a lumpy or flattened cloud adds a shape-changing part. Correct.
- Earth as a whole falls freely under the Moon's pull, so Earth's centre plays the centre crumb; the Moon's tide at Earth is 2 out along the line and 1 in across it, adding to zero.: python3: Hessian of the Moon's point-mass potential at Earth's distance, 2GM/d^3 along the line and -GM/d^3 across. → 1.73e-13 and -8.66e-14 per second squared, ratio 2 : -1 : -1, trace zero. Earth's centre follows free fall in the combined field; the wording no longer says Earth orbits the Moon, which it does not (both orbit their common centre). Correct.
- Fix: None: the two novice rewrites of revision 4 keep their claims and were re-read as the novice without a stumble.
