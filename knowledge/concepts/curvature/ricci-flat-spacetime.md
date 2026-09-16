---
type: "concept"
schema_version: 2
id: "ricci-flat-spacetime"
title: "Ricci-flat versus Riemann-flat"
tagline: "Zero drift total everywhere, yet not flat: the curvature that empty space keeps"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 4
updated: "2026-09-16"
aliases: ["Ricci-flat", "Ricci-flat spacetime", "Weyl tensor equals Riemann tensor in vacuum"]
prerequisites: ["ricci-tensor", "flatness-criterion", "weyl-tensor", "einstein-field-equations", "bianchi-identity"]
leads_to: ["vacuum-einstein-equations", "einstein-space"]
visuals: ["falling-ring-of-crumbs", "six-entry-curvature-table", "three-nested-rings-of-flatness"]
---

# Ricci-flat versus Riemann-flat

*Zero drift total everywhere, yet not flat: the curvature that empty space keeps*

`ricci-flat-spacetime` · curvature · core · physics-reviewed (revision 4)

**Needs:** [[ricci-tensor]] (entry) · [[flatness-criterion]] (entry) · [[weyl-tensor]] (working) · [[einstein-field-equations]] (working) · [[bianchi-identity]] (formal)  
**Opens:** [[vacuum-einstein-equations]] · [[einstein-space]]  
**Related:** [[kretschmann-scalar]] · [[volume-preserving-tidal-deformation]] · [[ricci-scalar]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[six-entry-curvature-table]] · [[three-nested-rings-of-flatness]]

> Beside a planet, crumbs let go on a small ball in a falling cabin drift into an egg that keeps its room, because the three drifts add to zero. A region where every falling cabin, everywhere in it, finds a zero drift total is called Ricci-flat. Flat asks for more: there, nothing drifts at all. So the empty space beside a planet is Ricci-flat and still curved.

## You will be able to

**Entry**
- Explain the difference between no drift at all and drifts that add to zero, and say which test the empty space beside a planet passes. `objectives/tell-the-two-tests-apart` ← `checks/seventh-of-a-millimetre`, `problems/wave-through-empty-space`
- Predict, from what fills a region, whether it is flat, Ricci-flat, both, or neither. `objectives/sort-regions` ← `checks/four-regions-two-tests`

**Working**
- Place a spacetime on the ladder scalar-flat, Ricci-flat, flat from its stress-energy and one invariant, and derive that vacuum without a cosmological constant is exactly Ricci-flat. `objectives/climb-the-ladder` ← `checks/radiation-universe-is-scalar-flat`, `problems/outside-a-charged-ball`
- Distinguish a zero tidal trace for one family of observers from Ricci-flatness, which needs every velocity. `objectives/every-observer-is-needed` ← `checks/crossing-a-string-gas`

**Formal**
- Prove that Ricci-flat implies flat in two and three dimensions, and use the equality of the Riemann and Weyl tensors to derive the vacuum Bianchi constraint and the Kretschmann scalar from tidal components. `objectives/prove-what-ricci-flat-forces-and-frees` ← `checks/three-dimensions-collapse-the-ladder`, `checks/inverse-cube-from-the-vacuum-bianchi-identity`, `problems/kretschmann-from-the-electric-part`

## Ways in

### 1. Egg-shaped, but not shrinking · entry · picture

*Beside a planet, a ball of crumbs let go in a falling cabin becomes an egg that keeps its room. Is spacetime there flat?*

**Recap:** Let go of crumbs at rest on a small imaginary ball, inside a cabin that falls freely beside a planet, above its air. Measured with a ruler fixed to the cabin, the crumbs drift: the ball grows longer along the line toward the planet's centre and narrower across that line. Add the drifts along three directions at right angles, and the sum is the drift total. Beside the planet the total is zero, so at first the egg takes up the same room as the ball. Among dust or rock the total is not zero, and the ball starts to shrink. The Ricci tensor is the table that holds the total.

Picture a cabin falling freely beside a planet, above its air, with a crew inside. The crew lets go of crumbs at rest on a small imaginary ball, with one crumb at its middle. Slowly the ball becomes an egg, its long axis along the line toward the planet's centre. The crew's ruler, fixed to the cabin, shows that the egg takes up the same room as the ball did. That is what a zero drift total means: the drifts along three directions at right angles cancel.

Now picture a second cabin, far from every star and planet. Its crew lets go of the same ball of crumbs. Nothing happens. Each crumb stays where it was let go.

Put two different tests to each cabin. The first test passes when no crumb drifts at all. The second test passes when the drifts along three directions at right angles add up to zero. Far from every star, both tests pass. Beside the planet, the crumbs drift, so the first test fails, but the drifts add to zero, so the second test passes.

A region of spacetime is flat when the first test passes at every spot of it, in cabins moving through it in every direction and at every speed. Far from every star, spacetime is flat.

A region is called Ricci-flat when the second test passes at every spot of it, again in cabins moving in every direction and at every speed. The name says that the Ricci tensor, the table of drift totals, is zero all over the region. The empty space beside the planet, above its air, is Ricci-flat.

So a Ricci-flat region need not be flat. A zero total does not mean zero drifts. Beside the planet, the crumb on the line toward the planet's centre drifts away from the middle crumb by some amount. The two crumbs on the two lines across it, at right angles to it and to each other, each drift in toward the middle crumb by half that amount. One minus a half minus a half is zero, though none of the three drifts is zero.

Going the other way round is safe. Where no crumb drifts at all, the totals are zero too. So every flat region is also Ricci-flat, but only some Ricci-flat regions are flat.

How big are the drifts? In a cabin falling freely near Earth, just above the air, let go of two crumbs one metre apart along the line toward Earth's centre. After ten seconds the crew's ruler shows them about a seventh of a millimetre farther apart. Daily life hides this, because a floor holds you up, and nobody falls freely for ten seconds with a ruler in hand.

**Try it:** Roll a lump of modelling clay into a ball. Drop it into a glass filled to the brim with water, standing on a saucer, and see how much spills. Dry the clay and press it gently into an egg shape between your palms. Refill the glass to the brim and drop the egg in. About the same amount of water spills, because the clay changed its shape without changing its room. That is what the drift beside a planet does to the ball of crumbs: shape, not room.

**Takeaway:** Beside a planet the crumbs drift, so spacetime there is not flat, yet the drifts add to zero at every spot, so it is Ricci-flat. Flat is the stricter of the two.

*What this leaves out:* Far from every star and planet here means a region where nothing is arriving from elsewhere: no wave of any kind is passing through. This way also sets aside the cosmological constant, a faint push apart spread evenly through all of space, which no cabin's ruler could notice anyway.

*Builds on:* [[ricci-tensor]], [[flatness-criterion]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/seventh-of-a-millimetre`

### 2. Which regions pass the zero-total test · entry · operational

*How can crews tell whether a whole region is Ricci-flat, and what does passing tell them?*

**Recap:** The ball test: let go of crumbs at rest on a small ball in a cabin that falls freely. Measure with a ruler fixed to the cabin how far each crumb drifts from the middle crumb. Add the drifts along three directions at right angles to get the drift total. A region is flat when nothing drifts at all. It is Ricci-flat when the total is zero, in every cabin at every spot.

In "Egg-shaped, but not shrinking", one cabin beside a planet found a zero drift total. One reading at one spot cannot name a whole region Ricci-flat. The crews must run the ball test at every spot of the region, in cabins moving through it in every direction and at every speed.

Why every speed? Because the drift total can depend on how the cabin moves. In a universe filled evenly with dust, a cabin at rest among the dust finds one total. A cabin racing through the same dust finds a bigger one. So a zero reading in one cabin could be luck.

There is a shortcut. Einstein's equation of gravity, stated here without proof, ties the drift total a cabin finds at a spot to two things only. One is the matter at that very spot. The other is how the cabin moves. Matter here means anything whose energy sits at a spot: rock, gas, dust and light all count. With no matter at the spot, every cabin finds zero. So a region is Ricci-flat exactly when no matter sits anywhere in it.

Four regions show the pattern. Far from every star, nothing drifts: the region is flat, and so Ricci-flat as well. Beside a planet, above its air, the crumbs drift and the total is zero: Ricci-flat, not flat. Inside a cloud of gas, the crumbs drift and the total is not zero: neither flat nor Ricci-flat.

The fourth region holds a gravitational wave. A gravitational wave is a pattern of stretch and squeeze that travels through empty space at the speed of light, made by violently moving masses such as two merging black holes. Where it passes, crumbs along one line across its path spread apart by a tiny fraction of their gap. Crumbs along the other line across its path, at right angles to the first, draw together by the same fraction. Crumbs along the wave's path do not drift. The total is zero, so the region is Ricci-flat, though the crumbs drift plenty. The wave carries energy, but that energy is spread over the whole wave and sits at no one spot, so it is not matter at the spot. A light meter held at one spot reads how much light energy arrives there. No meter at one spot can read a gravitational wave's energy, which can only be added up over a long stretch of the wave.

So Ricci-flat names what the empty space beside a planet and the space a gravitational wave is passing through share. No matter sits there, no ball of crumbs changes its room, and yet the curving is real, because mass elsewhere made it.

**Takeaway:** A region is Ricci-flat when every cabin at every spot and speed finds a zero drift total. By Einstein's equation that means no matter sits anywhere in it, as beside a planet or where a wave is passing.

*What this leaves out:* This leaves out the cosmological constant, a faint push spread through all of space. With it, an empty region's drift total is not quite zero, but the difference is far too small for any cabin near a planet to notice.

*Continues:* `ways_in/egg-shaped-but-not-shrinking`<br>*Builds on:* [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/four-regions-two-tests`, `problems/wave-through-empty-space`

### 3. Three ways to be flat, and a strict ladder · working · contrast

*Which of scalar-flat, Ricci-flat and flat imply which, and which spacetimes separate them?*

The zero-total test of "Which regions pass the zero-total test" is one of three conditions that all borrow the word flat. Write the Riemann tensor $R^\rho{}_{\sigma\mu\nu}$, its trace the Ricci tensor $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, and the Ricci scalar $R = g^{\mu\nu}R_{\mu\nu}$. A region is *flat* when $R^\rho{}_{\sigma\mu\nu} = 0$ throughout it, *Ricci-flat* when $R_{\mu\nu} = 0$ throughout it, and *scalar-flat* when $R = 0$ throughout it.

Each condition is a trace of the one before, and a trace of zero is zero, so the three form a ladder:

$$R^\rho{}_{\sigma\mu\nu} = 0 \;\Rightarrow\; R_{\mu\nu} = 0 \;\Rightarrow\; R = 0.$$

Neither arrow reverses in four dimensions, and one spacetime for each gap shows why.

Ricci-flat but not flat: the empty space outside a spherical star. There the stress-energy tensor vanishes, and Einstein's equation with no cosmological constant becomes $G_{\mu\nu} = 0$. Its trace gives $R = 0$, and putting that back gives $R_{\mu\nu} = 0$, as the derivation "Vacuum and Ricci-flat coincide" shows. Yet the Kretschmann scalar there is $48G^2M^2/c^4r^6$, quoted from the Kretschmann concept, and not zero. Curvature survives with every Ricci component zero.

Scalar-flat but not Ricci-flat: a universe filled evenly with radiation. Radiation has pressure $p = \rho c^2/3$, so the trace of its stress-energy tensor, $T = -\rho c^2 + 3p$, vanishes. The trace of Einstein's equation, $R = -8\pi GT/c^4$, then gives $R = 0$. But an observer at rest in the radiation measures a tidal trace $R_{\mu\nu}u^\mu u^\nu = 4\pi G(\rho + 3p/c^2) = 8\pi G\rho$, which is positive: a released ball of crumbs shrinks, and the Ricci tensor is not zero.

Two cautions. With a cosmological constant, empty regions obey $R_{\mu\nu} = \Lambda g_{\mu\nu}$ instead: they are Einstein spaces, not Ricci-flat, though their tidal trace $-\Lambda c^2 \approx -1\times10^{-35}\,\mathrm{s^{-2}}$ lies thirty powers of ten below Earth's surface tidal gradient of $3\times10^{-6}\,\mathrm{s^{-2}}$. And "no matter" includes no light and no electric field: an electromagnetic field has $T = 0$, so a region holding one is scalar-flat but not Ricci-flat, as the problem "Outside a charged ball" works out.

**Takeaway:** Flat implies Ricci-flat implies scalar-flat, and neither converse holds in four dimensions: a star's exterior is Ricci-flat but curved, and a radiation universe is scalar-flat but not Ricci-flat.

*Continues:* `ways_in/which-regions-pass-the-zero-total-test`<br>*Builds on:* [[ricci-scalar]], [[einstein-field-equations]]<br>*Visuals:* [[three-nested-rings-of-flatness]]<br>*See:* `derivations/vacuum-and-ricci-flat-coincide`, `checks/radiation-universe-is-scalar-flat`, `worked_examples/four-spacetimes-on-the-ladder`, `problems/outside-a-charged-ball`

### 4. What is left when Ricci is zero · working · calculation

*In a Ricci-flat region, which curvature survives, and what does a freely falling observer measure of it?*

The ladder of "Three ways to be flat" allows a Ricci-flat region to be curved; here is exactly which curvature it keeps. The Weyl concept splits the Riemann tensor into the Weyl tensor plus terms built from the Ricci tensor, the Ricci scalar and the metric. When $R_{\mu\nu} = 0$, every one of those terms vanishes, so

$$R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu}.$$

All the curvature of a Ricci-flat region is Weyl curvature. Of the Riemann tensor's twenty independent components in four dimensions, the ten Ricci components are zero and the ten Weyl components stay free, to be fixed by the sources elsewhere and by the vacuum field equations.

What does an observer feel of these ten? A freely falling observer with four-velocity $u^\mu$ measures the tidal tensor $E_{ij} = c^2R_{\hat\imath\hat 0\hat\jmath\hat 0}$ in her orthonormal frame, and its trace is the Ricci component $R_{\mu\nu}u^\mu u^\nu$. In a Ricci-flat region that trace is zero for every observer. A symmetric three-by-three table with zero trace has five independent entries, so the tides carry five of the ten Weyl numbers. The other five, the magnetic part, appear as velocity-dependent tides that a static observer beside a static star does not measure.

Outside a spherical, non-rotating star of mass $M$, a static observer at radius $r$ measures $E_{ij} = (GM/r^3)\,\mathrm{diag}(-2, 1, 1)$, radial direction first, as the relativistic tidal tensor concept shows. The trace is $-2 + 1 + 1 = 0$, as it must be. At Earth's distance from the Sun, $GM_\odot/r^3 = 4.0\times10^{-14}\,\mathrm{s^{-2}}$: two released crumbs one metre apart along the line to the Sun gain separation at $7.9\times10^{-14}$ metres per second squared, while a pair one metre apart across that line closes at half that rate.

In a plane gravitational wave the tides stretch along one line across the wave's path, squeeze equally along the perpendicular line, and vanish along the path: again a zero trace, in a pattern travelling at $c$.

Ricci-flatness therefore neither makes curvature small nor silences invariants: the Kretschmann scalar equals $C_{\rho\sigma\mu\nu}C^{\rho\sigma\mu\nu}$, and outside the star it is $48G^2M^2/c^4r^6$. What Ricci-flatness fixes is the shape of every tide: stretch balanced by squeeze, with no all-round shrinking anywhere in the region.

**Takeaway:** In a Ricci-flat region the Riemann tensor equals the Weyl tensor: ten free components, felt as trace-free tides, stretch balanced by squeeze, for every observer.

*Continues:* `ways_in/three-ways-to-be-flat`<br>*Builds on:* [[weyl-tensor]], [[number-of-independent-riemann-components]]<br>*Visuals:* [[six-entry-curvature-table]]<br>*See:* `checks/crossing-a-string-gas`, `problems/kretschmann-from-the-electric-part`

### 5. Definition, dimension, and what stays free · formal · structure

*What exactly is a Ricci-flat metric, in which dimensions is it flat, and what does Ricci-flatness constrain and leave free?*

In "What is left when Ricci is zero", Ricci-flatness left the Weyl tensor free; here that freedom is made precise, with $G = c = 1$. Let $(M, g)$ be a smooth manifold with a metric of any signature and its Levi-Civita connection. The metric is *Ricci-flat on an open set* $U$ when $\mathrm{Ric} = 0$ at every point of $U$. Like the flatness criterion, it is a condition on an open set, not on a single point.

*Dimension.* For $n \ge 3$ the Riemann tensor decomposes as

$$R_{abcd} = C_{abcd} + \frac{1}{n-2}\big(g_{ac}R_{bd} - g_{ad}R_{bc} + g_{bd}R_{ac} - g_{bc}R_{ad}\big) - \frac{R}{(n-1)(n-2)}\big(g_{ac}g_{bd} - g_{ad}g_{bc}\big),$$

stated here as the general-dimension form of the Weyl definition; with $n = 4$ it reproduces the formula of the Weyl concept. In two dimensions $R_{abcd} = \tfrac12 R\,(g_{ac}g_{bd} - g_{ad}g_{bc})$ and $R_{ab} = \tfrac12 R\,g_{ab}$, so scalar-flat, Ricci-flat and flat coincide. In three dimensions the Weyl tensor vanishes identically and the decomposition inverts the trace: the Riemann tensor is determined by the Ricci tensor (derivation "Invert the trace in three dimensions"), so Ricci-flat implies flat. Only from $n = 4$ on does the Weyl tensor have components, $n(n+1)(n+2)(n-3)/12$ of them: 10 in four dimensions, 35 in five. Ricci-flatness constrains the $n(n+1)/2$ Ricci components and leaves these free.

*Conformal flatness.* Since $R_{abcd} = C_{abcd}$ in a Ricci-flat region, a Ricci-flat region that is also conformally flat, $C_{abcd} = 0$, is flat. Every Friedmann–Lemaître–Robertson–Walker metric is conformally flat, so the only Ricci-flat ones are flat: with no sources the Friedmann equations give $\dot a^2 = -k$, so either $k = 0$ with constant $a$, which is Minkowski spacetime, or $k = -1$ with $a = t$, the Milne model, which is Minkowski spacetime in expanding coordinates.

*Invariants.* Every scalar built from the Riemann tensor and its derivatives in a Ricci-flat region is a Weyl invariant; in particular $R_{abcd}R^{abcd} = C_{abcd}C^{abcd}$. In Riemannian signature this sum of squares vanishes only if $C = 0$, so a Ricci-flat Riemannian metric with zero Kretschmann scalar is flat. In Lorentzian signature the sum has both signs, and plane-wave spacetimes are Ricci-flat and curved with every polynomial invariant zero.

*The vacuum Bianchi identity.* The contracted second Bianchi identity reads $\nabla^a R_{abcd} = \nabla_c R_{bd} - \nabla_d R_{bc}$ (derivation "The vacuum Bianchi identity"). In a Ricci-flat region the right side vanishes, so

$$\nabla^a C_{abcd} = 0.$$

Relative to a family of observers this splits into constraint and evolution equations for the electric and magnetic parts of the Weyl tensor, formally like Maxwell's equations in empty space. It is what makes Weyl curvature propagate: gravitational waves are its solutions, and in the static weak-field limit it forces the inverse-cube fall-off of spherically symmetric tides.

*Field equations.* In four dimensions $G_{ab} = 0$ and $R_{ab} = 0$ are equivalent by the trace argument, and the same holds in every dimension except two, where $G_{ab}$ vanishes identically. Ricci-flat metrics are the Einstein metrics with constant zero. With a cosmological constant the empty-space equation is $R_{ab} = \Lambda g_{ab}$, an Einstein metric that is not Ricci-flat: Schwarzschild, Kerr and the plane waves are Ricci-flat, de Sitter is not.

*Riemannian Ricci-flat metrics.* Compact Ricci-flat manifolds need not be flat: by Yau's solution of the Calabi conjecture, every compact Kähler manifold with vanishing first Chern class carries a Ricci-flat Kähler metric, and a K3 surface is such a manifold with no flat metric, since its Euler characteristic is 24.

*Limits.* Everything above assumes a torsion-free metric connection. Ricci-flatness on an open set fixes neither the global topology nor any bound on the Weyl tensor, which grows without limit toward the Schwarzschild centre.

**Takeaway:** Ricci-flat on an open set means Ric equals zero there; it forces flatness in dimensions two and three, leaves the Weyl tensor free from dimension four on, and constrains that tensor only through the divergence-free vacuum Bianchi identity.

*Picture:* Three nested classes, flat inside Ricci-flat inside scalar-flat, collapsing to one class in dimensions two and three and opening a gap of ten free Weyl components in dimension four, more in higher dimensions.

*Continues:* `ways_in/what-is-left-when-ricci-is-zero`<br>*Builds on:* [[bianchi-identity]]<br>*See:* `derivations/invert-the-trace-in-three-dimensions`, `derivations/vacuum-bianchi-identity`, `checks/three-dimensions-collapse-the-ladder`, `checks/inverse-cube-from-the-vacuum-bianchi-identity`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | — |
| tidal drift | — | The slow drift of crumbs let go at rest in a freely falling cabin, because gravity pulls each slightly differently. It is measured against a middle crumb with a ruler fixed to the cabin. | — |
| drift total | — | The drifts of a ball of crumbs along three directions at right angles, added up, with drift away from the middle crumb positive and drift toward it negative. | — |
| ball test | — | Let go of crumbs at rest on a small ball in a freely falling cabin, with one crumb at the middle. Then measure with a ruler fixed to the cabin how far each crumb drifts from the middle crumb. | — |
| room | — | How much space a thing takes up; physicists say volume. | — |
| Ricci tensor | REE-chee tensor | The table, kept at every place, of drift totals for cabins moving in every way. | [[ricci-tensor]] |
| Ricci-flat | REE-chee flat | Said of a region where the drift total is zero at every spot, for cabins moving in every way: its Ricci tensor is zero. | [[ricci-flat-spacetime]] |
| flat | — | Said of a region where no crumb drifts at all, whichever way its cabin moves; its Riemann curvature tensor is zero. | [[flatness-criterion]] |
| spacetime | — | Space and time taken together as one world with four directions: three of space and one of time. | — |
| curvature | — | The curving of spacetime that shows up as tidal drift between falling neighbours. | [[curvature]] |
| matter | — | Anything whose energy sits at a spot: rock, gas, dust, light and electric fields all count. A gravitational wave's energy is spread over the whole wave, at no one spot, so it does not count. A light meter held at one spot reads how much light energy arrives there. No meter at one spot can read a gravitational wave's energy, which can only be added up over a long stretch of the wave. | — |
| gravitational wave | — | A pattern of stretch and squeeze that travels through empty space at the speed of light, made by violently moving masses. | [[gravitational-wave]] |
| Einstein's equation | — | The rule of gravity that ties the drift total a cabin finds at a spot to the matter at that spot and to how the cabin moves. With no matter at the spot, every cabin finds zero. | [[einstein-field-equations]] |
| cosmological constant | — | A faint push apart, spread evenly through all of space, that Einstein's equation allows. It is far too weak for any cabin's ruler to notice. | [[cosmological-constant]] |

## Key equations

### Ricci-flat condition · working

$$
R_{\mu\nu} = 0 \quad \text{throughout a region}
$$

The defining condition: the Ricci tensor vanishes at every point of the region, so every observer's tidal trace is zero there.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu}$ | the Ricci tensor | the Ricci tensor |

**Holds when:** A condition on an open region, not on a single point; the Riemann tensor may be nonzero.  
**Say it:** “The Ricci tensor is zero throughout the region.”  
**Justified by:** `stated`

### Vacuum equals Ricci-flat · working

$$
G_{\mu\nu} = 0 \;\Longleftrightarrow\; R_{\mu\nu} = 0 \qquad (\Lambda = 0,\ n = 4)
$$

With no cosmological constant, the empty-space Einstein equation and Ricci-flatness are the same statement, in either direction.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $G_{\mu\nu}$ | the Einstein tensor | the Einstein tensor |
| $\Lambda$ | the cosmological constant | lambda |

**Holds when:** Four dimensions, or any dimension other than two; cosmological constant zero.  
**Say it:** “The Einstein tensor vanishes exactly when the Ricci tensor vanishes, with no cosmological constant.”  
**Justified by:** `derivations/vacuum-and-ricci-flat-coincide`

### Riemann equals Weyl in a Ricci-flat region · working

$$
R_{\mu\nu} = 0 \;\Longrightarrow\; R_{\rho\sigma\mu\nu} = C_{\rho\sigma\mu\nu}
$$

Every Ricci-built term of the Weyl decomposition drops out: all the curvature of a Ricci-flat region is Weyl curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C_{\rho\sigma\mu\nu}$ | the Weyl tensor, the trace-free part of the Riemann tensor | the Weyl tensor |

**Holds when:** Dimension at least three; in three dimensions both sides are then zero.  
**Say it:** “Where the Ricci tensor vanishes, the Riemann tensor equals the Weyl tensor.”  
**Justified by:** `weyl-tensor`

### Riemann from Ricci in three dimensions · formal

$$
R_{abcd} = g_{ac}R_{bd} - g_{ad}R_{bc} + g_{bd}R_{ac} - g_{bc}R_{ad} - \tfrac12 R\,(g_{ac}g_{bd} - g_{ad}g_{bc}) \qquad (n = 3)
$$

In three dimensions the Ricci tensor determines the whole Riemann tensor, so Ricci-flat implies flat.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $g_{ab}$ | the metric | the metric |
| $R$ | the Ricci scalar | the Ricci scalar |

**Holds when:** Three dimensions, any signature, Levi-Civita connection.  
**Say it:** “In three dimensions, the Riemann tensor is built from the metric, the Ricci tensor and the Ricci scalar alone.”  
**Justified by:** `derivations/invert-the-trace-in-three-dimensions`

### Vacuum Bianchi identity · formal

$$
\nabla^a C_{abcd} = 0 \quad \text{where } R_{ab} = 0
$$

In a Ricci-flat region the Weyl tensor is divergence-free: the contracted second Bianchi identity with its Ricci source removed.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla^a$ | the covariant divergence on the first slot | the divergence |

**Holds when:** Ricci-flat open set; dimension at least three.  
**Say it:** “The divergence of the Weyl tensor vanishes wherever the Ricci tensor does.”  
**Justified by:** `derivations/vacuum-bianchi-identity`

## Derivations

### Vacuum and Ricci-flat coincide · working

**Goal:** Show that $G_{\mu\nu} = 0$ and $R_{\mu\nu} = 0$ are equivalent in four dimensions with $\Lambda = 0$.

1. Write the empty-space equation with $\Lambda = 0$ and $T_{\mu\nu} = 0$: $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu} = 0$.
2. Contract with $g^{\mu\nu}$, using $g^{\mu\nu}g_{\mu\nu} = 4$: $R - \tfrac12\cdot 4R = -R = 0$, so $R = 0$.
3. Substitute $R = 0$ back: $R_{\mu\nu} = 0$.
4. Conversely, if $R_{\mu\nu} = 0$ then $R = g^{\mu\nu}R_{\mu\nu} = 0$, so $G_{\mu\nu} = 0 - 0 = 0$.
5. In $n$ dimensions the contraction gives $(1 - n/2)R$, so the argument works whenever $n \neq 2$.

**Result:** $G_{\mu\nu} = 0 \iff R_{\mu\nu} = 0$ for $\Lambda = 0$ and $n \neq 2$. With $\Lambda \neq 0$ the same steps give $R_{\mu\nu} = \Lambda g_{\mu\nu}$ instead.

### Invert the trace in three dimensions · formal

**Goal:** Show that in three dimensions the Riemann tensor is determined by the Ricci tensor, so Ricci-flat implies flat.

1. Start from the decomposition valid for $n \ge 3$, the general-dimension form of the Weyl definition, stated: $R_{abcd} = C_{abcd} + \frac{1}{n-2}(g_{ac}R_{bd} - g_{ad}R_{bc} + g_{bd}R_{ac} - g_{bc}R_{ad}) - \frac{R}{(n-1)(n-2)}(g_{ac}g_{bd} - g_{ad}g_{bc})$.
2. In three dimensions the Weyl tensor vanishes identically, so set $C_{abcd} = 0$ and $n = 3$: the coefficients become $1$ and $\tfrac12$.
3. Check by tracing with $g^{ac}$: $3R_{bd} + R\,g_{bd} - R_{bd} - R_{bd} - \tfrac12 R\,(3g_{bd} - g_{bd}) = R_{bd}$, the correct Ricci trace.
4. If $R_{bd} = 0$ on an open set, then $R = g^{bd}R_{bd} = 0$ there, and every term on the right vanishes: $R_{abcd} = 0$.

**Result:** In three dimensions $R_{abcd}$ is a linear function of $R_{bd}$ and $R$, so $\mathrm{Ric} = 0$ on an open set forces $\mathrm{Riem} = 0$. In two dimensions $R_{abcd} = \tfrac12 R\,(g_{ac}g_{bd} - g_{ad}g_{bc})$ gives the same.

### The vacuum Bianchi identity · formal

**Goal:** Derive $\nabla^a C_{abcd} = 0$ in a Ricci-flat region from the second Bianchi identity.

1. The second Bianchi identity, with the course index order, reads $\nabla_e R_{abcd} + \nabla_c R_{abde} + \nabla_d R_{abec} = 0$.
2. Contract $e$ with $a$ using $g^{ea}$: $\nabla^a R_{abcd} + \nabla_c R^a{}_{bda} + \nabla_d R^a{}_{bac} = 0$.
3. Use $R_{bc} = R^a{}_{bac}$ and antisymmetry in the last pair, $R^a{}_{bda} = -R^a{}_{bad} = -R_{bd}$: $\nabla^a R_{abcd} - \nabla_c R_{bd} + \nabla_d R_{bc} = 0$, so $\nabla^a R_{abcd} = \nabla_c R_{bd} - \nabla_d R_{bc}$.
4. In a Ricci-flat region the right side is zero, and $R_{abcd} = C_{abcd}$ there, so $\nabla^a C_{abcd} = 0$.

**Result:** $\nabla^a R_{abcd} = \nabla_c R_{bd} - \nabla_d R_{bc}$ in general, and $\nabla^a C_{abcd} = 0$ wherever $R_{ab} = 0$.

## Worked examples

### Four spacetimes on the ladder · working

**Problem:** Place Minkowski spacetime, a spherical star's empty exterior, a radiation-filled universe and a dust-filled universe on the ladder scalar-flat, Ricci-flat, flat, with $\Lambda = 0$.

1. Trace Einstein's equation: $R = -8\pi GT/c^4$, with $T = -\rho c^2 + 3p$ for a perfect fluid. The comoving tidal trace is $R_{\mu\nu}u^\mu u^\nu = 4\pi G(\rho + 3p/c^2)$.
2. Minkowski: every Riemann component is zero in inertial coordinates: flat, hence Ricci-flat and scalar-flat.
3. Star exterior: $T_{\mu\nu} = 0$, so $R = 0$ and, by the derivation "Vacuum and Ricci-flat coincide", $R_{\mu\nu} = 0$. The Kretschmann scalar $48G^2M^2/c^4r^6$, quoted from the Kretschmann concept, is not zero. Ricci-flat, not flat.
4. Radiation: $p = \rho c^2/3$ gives $T = 0$ and $R = 0$, but $R_{\mu\nu}u^\mu u^\nu = 8\pi G\rho \neq 0$. Scalar-flat only.
5. Dust: $p = 0$ gives $T = -\rho c^2$ and $R = 8\pi G\rho/c^2 \neq 0$. Not even scalar-flat.

**Answer:** Minkowski: flat. Star exterior: Ricci-flat, not flat. Radiation universe: scalar-flat, not Ricci-flat. Dust universe: none of the three.

**Takeaway:** The stress-energy trace decides scalar-flatness, the whole tensor decides Ricci-flatness, and a nonzero invariant shows a Ricci-flat region is not flat.

## Problems

### `wave-through-empty-space` · entry · difficulty 1 · conceptual

A gravitational wave from two merging black holes passes a cabin floating far from every star, where the crew has let go of crumbs on a small ball. Crumbs along one line across the wave's path spread apart by a tiny fraction. Crumbs along the other line across the wave's path, at right angles to the first, draw together by the same fraction. Crumbs along the wave's path stay put. A friend says the wave carries energy, so the drift total cannot be zero, and that with no matter here nothing can be curved. Is the region flat? Is it Ricci-flat? The first wave found, in 2015, moved detector mirrors four kilometres apart by about a thousandth of the width of a proton. Why did nobody feel it?

**Hints**

1. Add the three drifts: out, in by the same amount, and none.
2. Does the zero-total test need the no-drift test to pass?
3. Compare a thousandth of a proton's width with anything a body can sense.

**Answer:** Ricci-flat but not flat. The drifts add to zero: out, in by the same amount, none. Einstein's equation counts only matter at the spot, and the cabin holds none. But the crumbs drift, so the region is not flat; the far-off black holes made that curving. Nobody felt the wave because a thousandth of a proton's width is far below anything a body can sense.

**Must contain:** Out, in by the same amount, and none: the total is zero, so Ricci-flat; The crumbs drift, so not flat; the curving came from the far-off black holes; The wave's energy is spread over the whole wave, so it is not matter at the spot; A thousandth of a proton's width is far too small to feel

**Numeric:** mirror movement as a fraction of a proton's width = 0.001 1 (magnitude, ±50%)

**Solution**

1. Add the three drifts: a stretch along one line, an equal squeeze along the line at right angles, none along the path. They cancel, so the drift total is zero.
2. Einstein's equation ties the total to matter at the spot, and none sits in the cabin, so the zero total is what it requires: Ricci-flat.
3. The crumbs drift, so the no-drift test fails: not flat. The far-away black holes made this curving, and it travelled through empty space.
4. A proton is about a millionth of a millionth of a millimetre across, and the mirrors moved by a thousandth of that. No body can sense that; a laser comparing two arms can.

**Targets:** `wave-needs-matter`

### `outside-a-charged-ball` · working · difficulty 2 · calculation

Outside a small ball carrying electric charge there is no matter, only its static electric field of strength $E$. The electromagnetic stress-energy tensor is trace-free, $T = 0$, and its energy density is $\tfrac12\varepsilon_0E^2$; take $\Lambda = 0$. (a) Show that the region is scalar-flat. (b) Find the tidal trace $R_{\mu\nu}u^\mu u^\nu$ for an observer at rest beside the ball and decide whether the region is Ricci-flat. (c) Evaluate $R_{\hat 0\hat 0} = R_{\mu\nu}u^\mu u^\nu/c^2$ for $E = 3\times10^6\,\mathrm{V/m}$.

**Hints**

1. The Ricci scalar is minus eight pi G over c to the fourth times the trace of the stress-energy tensor.
2. Trace-reverse Einstein's equation and contract with the four-velocity; with $T = 0$ only $T_{\mu\nu}u^\mu u^\nu$ survives.

**Answer:** (a) $R = -8\pi GT/c^4 = 0$: scalar-flat. (b) $R_{\mu\nu}u^\mu u^\nu = (8\pi G/c^4)\,T_{\mu\nu}u^\mu u^\nu = 4\pi G\varepsilon_0E^2/c^2 > 0$: a released ball shrinks, so not Ricci-flat. (c) $R_{\hat 0\hat 0} = 4\pi G\varepsilon_0E^2/c^4 = 8.3\times10^{-42}\,\mathrm{m^{-2}}$.

**Must contain:** Trace-free stress-energy gives R = 0; The tidal trace is 4 pi G epsilon nought E squared over c squared, positive, so not Ricci-flat; No matter is not the same as no energy: fields source the Ricci tensor

**Numeric:** Ricci scalar = 0 m^-2 (magnitude, ±1e-60); time-time Ricci component for E = 3e6 V/m = 8.3e-42 m^-2 (signed, ±5%)

**Solution**

1. Trace Einstein's equation: $-R = 8\pi GT/c^4$. With $T = 0$, $R = 0$ everywhere outside the ball, so the region is scalar-flat.
2. Trace-reverse: $R_{\mu\nu} = (8\pi G/c^4)(T_{\mu\nu} - \tfrac12Tg_{\mu\nu}) = (8\pi G/c^4)\,T_{\mu\nu}$. Contract with the observer's four-velocity, $u^{\hat 0} = c$ in her own frame: $T_{\mu\nu}u^\mu u^\nu = T_{\hat 0\hat 0}c^2 = \tfrac12\varepsilon_0E^2c^2$.
3. So $R_{\mu\nu}u^\mu u^\nu = 4\pi G\varepsilon_0E^2/c^2$, positive: the field's energy focuses a released ball of crumbs. Scalar-flat but not Ricci-flat.
4. Numerically, $4\pi G\varepsilon_0E^2/c^4 = 4\pi\times6.674\times10^{-11}\times8.854\times10^{-12}\times(3\times10^6)^2/(3.0\times10^8)^4 = 8.3\times10^{-42}\,\mathrm{m^{-2}}$.

**Targets:** `scalar-flat-means-ricci-flat`

### `kretschmann-from-the-electric-part` · formal · difficulty 2 · calculation

Work with $G = c = 1$. For an observer whose orthonormal frame gives magnetic components $R_{\hat 0\hat\imath\hat\jmath\hat k} = 0$ in a Ricci-flat region, the Kretschmann scalar reduces to $\mathcal K = 8\sum_{i,j}(R_{\hat 0\hat\imath\hat 0\hat\jmath})^2$, taken as given from the Kretschmann concept's vacuum form. (a) Explain why $\mathcal K$ equals the Weyl contraction $C_{abcd}C^{abcd}$ here. (b) Write $\mathcal K$ in terms of the electric part $E_{ij} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$. (c) Evaluate it for a static observer outside a spherical mass, where $E_{ij} = (M/r^3)\,\mathrm{diag}(-2,1,1)$, and compare with $\mathcal K = 48M^2/r^6$.

**Hints**

1. Which tensor is contracted with itself when Ricci vanishes?
2. Sum the squares of the three eigenvalues.

**Answer:** (a) Where $R_{ab} = 0$ the Riemann and Weyl tensors are the same tensor, so every self-contraction of one is the same self-contraction of the other. (b) $\mathcal K = 8\,E_{ij}E_{ij}$, or $8E_{ij}E_{ij}/c^4$ in SI. (c) $E_{ij}E_{ij} = (M^2/r^6)(4 + 1 + 1) = 6M^2/r^6$, so $\mathcal K = 48M^2/r^6$, the Schwarzschild value.

**Must contain:** Riemann equals Weyl, so the Kretschmann scalar is the Weyl contraction; The scalar is eight times the sum of the squared electric entries when the magnetic part vanishes; Eigenvalues minus two, one, one give six, and the scalar is forty-eight M squared over r to the sixth

**Numeric:** coefficient of M squared over r to the sixth in the Kretschmann scalar = 48 1 (signed, ±0.5)

**Solution**

1. Where $R_{ab} = 0$ the Riemann and Weyl tensors are one tensor, so every self-contraction of one is the same self-contraction of the other: $\mathcal K = C_{abcd}C^{abcd}$.
2. With the magnetic sum zero, $R_{\hat 0\hat\imath\hat 0\hat\jmath} = R_{\hat\imath\hat 0\hat\jmath\hat 0} = E_{ij}$ by antisymmetry in each pair, so $\mathcal K = 8E_{ij}E_{ij}$.
3. For $E = (M/r^3)\,\mathrm{diag}(-2, 1, 1)$, $E_{ij}E_{ij} = 6M^2/r^6$, so $\mathcal K = 48M^2/r^6$; in SI, $48G^2M^2/c^4r^6$.

## Observations

- **Extra delay of radio signals passing near the Sun between Earth and the Cassini spacecraft in 2002** (measured, working). The signals crossed the Sun's exterior, Ricci-flat to the test's accuracy since the solar wind's energy is negligible. The curvature that delays them is Weyl curvature, and the measured post-Newtonian parameter $\gamma_{\rm PPN}$ matches the value of one predicted by the Ricci-flat Schwarzschild exterior. *Numbers:* $\gamma_{\rm PPN} - 1 = (2.1 \pm 2.3)\times10^{-5}$. *Reference:* Bruno Bertotti, Luciano Iess, Paolo Tortora (2003), *A test of general relativity using radio links with the Cassini spacecraft*, Nature 425, 374–376, doi:10.1038/nature01997
- **The first detected gravitational wave, GW150914, in the two LIGO interferometers on 14 September 2015** (measured, working). The wave reached the detectors through Ricci-flat space, so its tide was trace-free: one arm lengthened while the perpendicular arm shortened by the same fraction, the Weyl curvature that Ricci-flatness allows, with no change of volume. *Numbers:* Peak strain about $1.0\times10^{-21}$: about $2\times10^{-18}$ m per 4 km arm. *Reference:* B. P. Abbott, R. Abbott, T. D. Abbott and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Open with the egg beside a planet** (entry). Run the egg picture, ask whether spacetime there is flat, then separate the two tests. *Why:* The learner owns the gap between zero total and zero drift before the name arrives. *Predict:* The egg keeps the ball's room. Is spacetime there flat? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/egg-shaped-but-not-shrinking`, `checks/seventh-of-a-millimetre`
2. **Tour four regions and name the class** (entry). Walk the four regions, ask for both verdicts on each, then give Einstein's rule tying the total to matter at the spot. *Why:* Sorting concrete regions makes the definition a skill. *Predict:* Where the wave passes, is the total zero? *Uses:* `ways_in/which-regions-pass-the-zero-total-test`, `checks/four-regions-two-tests`, `problems/wave-through-empty-space`
3. **Build the three-rung ladder** (working). Write the three conditions, derive vacuum equals Ricci-flat, then break each converse with the star exterior and the radiation universe. *Why:* The separating examples are the content; the ladder itself is one line. *Predict:* Is a radiation universe's Ricci scalar zero? *Visual:* [[three-nested-rings-of-flatness]] *Uses:* `ways_in/three-ways-to-be-flat`, `derivations/vacuum-and-ricci-flat-coincide`, `checks/radiation-universe-is-scalar-flat`, `worked_examples/four-spacetimes-on-the-ladder`
4. **Show what survives and who must check** (working). Replace Riemann by Weyl, read the trace-free tide off the star exterior, then run the string-gas case. *Why:* Otherwise learners keep zero total in my cabin as the definition. *Visual:* [[six-entry-curvature-table]] *Uses:* `ways_in/what-is-left-when-ricci-is-zero`, `checks/crossing-a-string-gas`, `problems/outside-a-charged-ball`
5. **Dimension and the vacuum Bianchi identity** (formal). Prove the three-dimensional collapse, derive the vacuum Bianchi identity, and let the learner extract the inverse-cube law. *Why:* These theorems make Ricci-flat a four-dimensional phenomenon. *Uses:* `ways_in/definition-dimension-and-what-stays-free`, `derivations/invert-the-trace-in-three-dimensions`, `derivations/vacuum-bianchi-identity`, `checks/three-dimensions-collapse-the-ladder`, `checks/inverse-cube-from-the-vacuum-bianchi-identity`, `problems/kretschmann-from-the-electric-part`

## Analogies

### The source-free electric field outside a charged ball · working

Outside a charged ball the electric field has zero divergence, because Gauss's law ties the divergence to the charge density and there is none there. Yet the field is not zero. Ricci-flatness is the same statement one level up: Einstein's equation ties the Ricci tensor to the stress-energy at the spot, while the Weyl curvature, like the field, reaches out from the source.

| In the analogy | Stands for |
| --- | --- |
| charge density | stress-energy at the spot |
| zero divergence of the field | zero Ricci tensor |
| the nonzero field outside the ball | the Weyl curvature |

*Limits:* The field is a vector under one scalar constraint; curvature is a rank-four tensor under the tensor-valued vacuum Bianchi identity. The analogy ignores gravity's nonlinearity, and a real electric field, unlike the Weyl tensor, carries stress-energy that itself sources Ricci curvature.

## Misconceptions

### “Ricci-flat means the curving there is zero, so the spacetime is flat.” · entry · `ricci-flat-is-flat`

- **Why it is tempting:** The word flat sits inside the name.
- **What is true:** Ricci-flat sets only the drift totals to zero, and one, minus a half and minus a half add to zero without being zero. Beside a planet the crumbs drift.
- **Exposed by:** `checks/seventh-of-a-millimetre`

### “A gravitational wave carries energy, so where it passes the drift total cannot be zero.” · entry · `wave-needs-matter`

- **Why it is tempting:** Energy sounds like matter.
- **What is true:** Einstein's equation counts only matter at the spot, and a wave in empty space has none there: its energy is spread over the whole wave, at no one spot. Its stretch along one line and equal squeeze along the other add to zero.
- **Exposed by:** `checks/four-regions-two-tests`

### “If the Ricci scalar is zero, the Ricci tensor is zero too, since the scalar is just its trace.” · working · `scalar-flat-means-ricci-flat`

- **Why it is tempting:** The implication runs the other way.
- **What is true:** A trace can vanish while its entries do not: a radiation universe has zero Ricci scalar, yet its comoving tidal trace is eight pi G rho.
- **Exposed by:** `checks/radiation-universe-is-scalar-flat`

### “If the observers at rest in the matter all measure a zero tidal trace, the region is Ricci-flat.” · working · `one-family-zero-trace-suffices`

- **Why it is tempting:** Comoving observers are the natural ones to compute with.
- **What is true:** Ricci-flat needs every component zero, which takes observers at every velocity. In a string-gas universe comoving observers read zero while one at six tenths of c reads three pi G rho.
- **Exposed by:** `checks/crossing-a-string-gas`

### “The vacuum equation says nothing about the Weyl tensor, so in a Ricci-flat region it can be any field with the right symmetries.” · formal · `weyl-unconstrained-in-vacuum`

- **Why it is tempting:** The equation mentions only the Ricci part, and the Weyl part is called free.
- **What is true:** The Bianchi identity makes the Weyl tensor divergence-free wherever Ricci vanishes, forcing the inverse-cube fall-off of spherical tides. Free means undetermined locally, not unconstrained.
- **Exposed by:** `checks/inverse-cube-from-the-vacuum-bianchi-identity`

## Checks

1. **Entry · predict** `checks/seventh-of-a-millimetre`. A cabin falls freely near Earth, just above the air. Using a ruler fixed to the cabin, the crew lets go of four crumbs at rest around a middle crumb. The near crumb is one metre from it, toward Earth's centre. The far crumb is one metre from it, away from Earth. The side crumb is one metre from it, across that line. The fourth crumb is one metre from it, across both that line and the side crumb's line. After ten seconds the near crumb is about a seventh of a millimetre farther from the middle crumb. How far, and which way, have the far crumb, the side crumb and the fourth crumb drifted? Add the drifts of the near crumb, the side crumb and the fourth crumb, which lie along three directions at right angles. Is spacetime in the cabin flat? Is it Ricci-flat?
   - **Hints:** Is the far crumb pulled more or less than the middle crumb? / Across the centre line, do crumbs draw together or spread apart?
   - **Answer:** Count drift away from the middle crumb as positive. The far crumb has drifted out by about a seventh of a millimetre, because along the centre line the drift away is the same on both sides. The side crumb has drifted in by half as much, a fourteenth of a millimetre, because across that line the pull draws crumbs together at half the rate. The fourth crumb also lies across the centre line, so it drifts in by another fourteenth of a millimetre. One seventh minus one fourteenth minus one fourteenth is zero: the drift total is zero. Spacetime in the cabin is not flat, because crumbs drift. It is Ricci-flat, because the total is zero, and Einstein's equation says every cabin in empty space finds the same zero.
   - **Must contain:** The far crumb drifts out by a seventh of a millimetre; The side crumb and the fourth crumb each drift in by half as much; The drifts add to zero: not flat, but Ricci-flat
   - **Numeric:** far crumb drift, positive outward = 0.14 mm (signed, ±0.03); side crumb drift, positive outward = -0.07 mm (signed, ±0.02); drift total = 0 mm (magnitude, ±0.01)
   - **Targets:** `ricci-flat-is-flat`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · choice** `checks/four-regions-two-tests`. Four crews run the ball test all through their regions, in cabins moving every way. Crew A is far from every star and planet. Crew B is beside a planet, above its air. Crew C is inside a huge cloud of gas. Crew D floats far from every star while a gravitational wave passes through. For each crew, say whether its region is flat, Ricci-flat, both, or neither.
   - **Hints:** Ask first whether anything drifts at all, then whether matter sits at the spot.
   - **Answer:** Crew A: both. No mass is near enough to pull one crumb differently from another, so no crumb drifts, and drifts of zero add to zero. Crew B: Ricci-flat only. The planet pulls the near crumb harder than the far one, so crumbs drift. But the drift out along the centre line is cancelled by two half-size drifts in across it, as in every cabin where no matter sits. Crew C: neither. Gas sits among the crumbs, so the total is not zero and the ball shrinks; and the crumbs drift, so the region is not flat. Crew D: Ricci-flat only. The wave stretches crumbs along one line across its path and squeezes them by the same fraction along the other line across its path. Nothing drifts along the path, so the total is zero. The crumbs drift, so the region is not flat. The wave carries energy, but that energy is spread over the whole wave and sits at no one spot. Einstein's equation counts only matter at the spot, and there is none.
   - **Must contain:** A is flat, hence Ricci-flat too; B and D are Ricci-flat but not flat; C is neither: gas sits among the crumbs
   - **Targets:** `wave-needs-matter`
3. **Working · explain** `checks/radiation-universe-is-scalar-flat`. A universe is filled evenly with radiation, a perfect fluid whose pressure is one third of rho c squared, with no cosmological constant. Find its Ricci scalar and the tidal trace measured by an observer at rest in the radiation, as a multiple of four pi G rho. Which rungs of the ladder does this universe reach?
   - **Hints:** Take the trace of Einstein's equation with the metric. / Use the tidal-trace formula $4\pi G(\rho + 3p/c^2)$.
   - **Answer:** The stress-energy trace is $T = -\rho c^2 + 3p = 0$. The trace of Einstein's equation is $R = -8\pi GT/c^4$, so $R = 0$: scalar-flat. The comoving tidal trace is $R_{\mu\nu}u^\mu u^\nu = 4\pi G(\rho + 3p/c^2) = 8\pi G\rho$, twice $4\pi G\rho$ and positive, so a released ball of crumbs shrinks and the Ricci tensor is not zero. Scalar-flat, not Ricci-flat, so not flat either.
   - **Must contain:** Zero stress-energy trace, so zero Ricci scalar; Comoving tidal trace eight pi G rho, not zero; Scalar-flat only
   - **Numeric:** Ricci scalar = 0 m^-2 (magnitude, ±1e-60); tidal trace in units of 4 pi G rho = 2 1 (signed, ±1%)
   - **Targets:** `scalar-flat-means-ricci-flat`
4. **Working · numeric** `checks/crossing-a-string-gas`. A model universe is filled evenly with a fluid whose pressure is minus one third of rho c squared, the average pressure of a tangle of cosmic strings, with no cosmological constant. (a) Find the tidal trace for an observer at rest in the fluid. (b) Find it for an observer moving through the fluid at six tenths of the speed of light, using the orthonormal Ricci components in the fluid's rest frame. Is the universe Ricci-flat?
   - **Hints:** For the comoving observer use $4\pi G(\rho + 3p/c^2)$. / Write the Ricci tensor in the fluid frame, then contract with the moving observer's four-velocity.
   - **Answer:** (a) $R_{\mu\nu}u^\mu u^\nu = 4\pi G(\rho + 3p/c^2) = 0$: a ball of crumbs released at rest in the fluid keeps its volume at first. (b) Trace-reversed, $R_{\mu\nu} = (8\pi G/c^4)(T_{\mu\nu} - \tfrac12 T g_{\mu\nu})$ with $T = -\rho c^2 + 3p = -2\rho c^2$. In the fluid's rest frame $T_{\hat 0\hat 0} = \rho c^2$ and $T_{\hat\imath\hat\imath} = p$, so $R_{\hat 0\hat 0} = 0$ and $R_{\hat\imath\hat\imath} = (8\pi G/c^4)(p + \rho c^2) = 16\pi G\rho/3c^2$. An observer moving along $\hat x$ at $\beta = 0.6$ has $u^{\hat 0} = \gamma c$, $u^{\hat x} = \gamma\beta c$ and $\gamma^2 = 1.5625$, so $R_{\mu\nu}u^\mu u^\nu = \gamma^2c^2(R_{\hat 0\hat 0} + \beta^2R_{\hat x\hat x}) = 1.5625\times0.36\times16\pi G\rho/3 = 3\pi G\rho$. Not zero: this observer's ball shrinks. The Ricci tensor has nonzero space components, so the universe is not Ricci-flat, although one family of observers reads zero.
   - **Must contain:** Comoving observers read a zero tidal trace; The space-space Ricci components are not zero; The moving observer reads three pi G rho, so not Ricci-flat
   - **Numeric:** tidal trace for the comoving observer, in units of pi G rho = 0 1 (magnitude, ±0.01); tidal trace for the observer at 0.6c, in units of pi G rho = 3 1 (signed, ±2%)
   - **Targets:** `one-family-zero-trace-suffices`
5. **Formal · derive** `checks/three-dimensions-collapse-the-ladder`. In three dimensions the Weyl tensor vanishes identically. Show that a three-dimensional metric which is Ricci-flat on an open set is flat there, and explain by a component count why no such argument can work in four dimensions.
   - **Hints:** Set $n = 3$ and $C = 0$ in the decomposition. / Compare the component counts of Riemann and Ricci.
   - **Answer:** With $C_{abcd} = 0$ and $n = 3$ the decomposition becomes $R_{abcd} = g_{ac}R_{bd} - g_{ad}R_{bc} + g_{bd}R_{ac} - g_{bc}R_{ad} - \tfrac12 R\,(g_{ac}g_{bd} - g_{ad}g_{bc})$; tracing with $g^{ac}$ returns $R_{bd}$, so it is consistent. If $R_{bd} = 0$ on the open set then $R = 0$ too, every term vanishes, and $R_{abcd} = 0$: flat by the flatness criterion. The count agrees: Riemann has $n^2(n^2-1)/12 = 6$ independent components in three dimensions and the symmetric Ricci tensor has $6$, and the trace map is onto, hence one to one. In four dimensions Riemann has 20 and Ricci 10, so the trace map has a ten-dimensional kernel, the Weyl tensors, which zero Ricci leaves free.
   - **Must contain:** With Weyl zero, Riemann is built from Ricci and the scalar; Ricci zero forces the scalar zero and hence Riemann zero; Six equals six in three dimensions; twenty exceeds ten in four
   - **Numeric:** independent Weyl components in four dimensions = 10 1 (magnitude, ±0)
6. **Formal · derive** `checks/inverse-cube-from-the-vacuum-bianchi-identity`. For static observers in a static, weak-field vacuum region, the vacuum Bianchi identity reduces to the statement that the electric part of the Weyl tensor has zero divergence; take this as given. A spherically symmetric trace-free tidal pattern is a function f of r times the identity minus three times the outer product of the unit radial vector with itself. Show that the constraint forces f to fall as the inverse cube of r, and check against the tides outside a spherical mass.
   - **Hints:** Use $\partial_in_j = (\delta_{ij} - n_in_j)/r$ and collect the coefficient of $n_j$.
   - **Answer:** Use $\partial_in_j = (\delta_{ij} - n_in_j)/r$, so $\partial_in_i = 2/r$ and $n_i\partial_in_j = 0$. Then $\partial_i(\delta_{ij}f) = f'n_j$ and $\partial_i(n_in_jf) = (2/r)fn_j + n_jf'$, so $\partial_iE_{ij} = -n_j\,(2f' + 6f/r)$. This vanishes for all $r$ only when $rf' + 3f = 0$, whose solution is $f = A\,r^{-3}$; for a trial power $r^{-k}$ the coefficient is $(2k - 6)r^{-k-1}$, zero only at $k = 3$. Outside a spherical mass $E_{ij} = (GM/r^3)(\delta_{ij} - 3n_in_j)$: radial entry $-2GM/r^3$, transverse entries $+GM/r^3$, the inverse-cube tide. The Bianchi identity, not an extra assumption, fixes how vacuum tides weaken with distance.
   - **Must contain:** The divergence is proportional to two f prime plus six f over r; Only f proportional to r to the minus three makes it vanish; Matches the minus two, one, one tide outside a spherical mass
   - **Numeric:** power of r in the fall-off of f = -3 1 (signed, ±0)
   - **Targets:** `weyl-unconstrained-in-vacuum`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| What vacuum and Ricci-flat mean when a cosmological constant is present | Ricci-flat means $R_{\mu\nu} = 0$ exactly. With $\Lambda \neq 0$ empty regions obey $R_{\mu\nu} = \Lambda g_{\mu\nu}$ and are called Einstein spaces, never Ricci-flat. | Some texts call any solution of the empty-space equations vacuum whether or not $\Lambda$ is included; check which equation is meant before reading vacuum as Ricci-flat. |
| The word flat by itself, and the cosmologist's flat universe | Flat alone means the Riemann tensor vanishes; Ricci-flat and scalar-flat name the weaker conditions $R_{\mu\nu} = 0$ and $R = 0$. | In cosmology a flat universe means zero spatial curvature constant, $k = 0$, a different statement again: a flat dust universe has $R = 8\pi G\rho/c^2 \neq 0$. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The two tests side by side: the far-from-every-star cabin where nothing drifts, and the planet cabin where the egg keeps its room, with the drift total read out. *Sketch:* This concept adds a two-cabin mode: one cabin far from every mass and one beside a planet, each with the ball of crumbs and a readout of the three drifts and their total. A verdict panel shows two lamps, any drift and zero total, and the learner sorts scenes (planet, gas cloud, wave, empty) before the lamps light; the wave scene shows the trace-free stretch and squeeze travelling across.
- [[six-entry-curvature-table]] (core): Ricci-flat as a pattern in the table: every Ricci readout zero while entries survive. *Sketch:* This concept adds a Ricci-flat toggle that constrains the six entries so that all Ricci readouts vanish, leaving two free sliders, with the Kretschmann readout staying nonzero and a star-exterior preset loading the minus two, one, one pattern.
- [[three-nested-rings-of-flatness]] (supporting): A sorting board for the ladder: three nested rings and spacetimes to drag into the innermost ring they belong to. *Sketch:* Three nested rings labelled scalar-flat, Ricci-flat and flat. Cards for Minkowski, Milne, a star's exterior, a plane wave, a radiation universe, a charged ball's exterior, a dust universe and de Sitter are dragged into place; a wrong placement shows the trace or invariant that rules it out.

## Tutor moves

**Open with**

- Picture a cabin falling freely beside a planet, above its air. The crew lets go of crumbs on a small ball, and it slowly turns into an egg that keeps the same room. A friend says that since the room did not change, spacetime there must be flat. Do you agree? *(prediction)*

**If the learner is stuck**

- *The learner treats no drift and zero total as one thing.* → Return to the far-from-every-star cabin and the planet cabin. For each, have the learner say whether anything drifted and what the three drifts added to. *Uses:* `ways_in/egg-shaped-but-not-shrinking`, `checks/seventh-of-a-millimetre`

**Common questions**

- *If no matter sits beside the planet, what curves spacetime there?* (entry) The planet's mass does, from a distance. Einstein's equation fixes only the drift total at each spot, and beside the planet that is zero. The stretch and squeeze that remain come from mass elsewhere, as the Moon raises tides on Earth from across empty space. *Uses:* `ways_in/egg-shaped-but-not-shrinking`, `ways_in/which-regions-pass-the-zero-total-test`
- *Is Ricci-flat just another name for a vacuum solution?* (working) With no cosmological constant, yes, by the trace argument. With $\Lambda \neq 0$ empty space is an Einstein space, not Ricci-flat, and vacuum must also exclude fields: an electric field sources Ricci curvature too. *Uses:* `derivations/vacuum-and-ricci-flat-coincide`, `problems/outside-a-charged-ball`

**Switching levels**

- To working when: asks for the equation behind the zero total; asks whether light counts as matter. Go to the ladder and the trace of Einstein's equation. *Uses:* `ways_in/three-ways-to-be-flat`, `derivations/vacuum-and-ricci-flat-coincide`
- To formal when: asks about dimension or what constrains the Weyl tensor. Go to the dimension argument and the vacuum Bianchi identity. *Uses:* `ways_in/definition-dimension-and-what-stays-free`, `checks/three-dimensions-collapse-the-ladder`

**Pronunciations:** Ricci → REE-chee; Weyl → VILE; Kretschmann → KRETCH-mahn; Lemaître → luh-MET-ruh

**Voice notes:** Stress Ricci in Ricci-flat and pause before a bare flat when contrasting the two. At entry say drift total, never trace.

## History

- **Albert Einstein (1915).** Proposed field equations whose empty-space form is $R_{\mu\nu} = 0$, and used that form later the same month to compute Mercury's perihelion advance, before the equations with sources reached their final form. Albert Einstein (1915), *Zur allgemeinen Relativitätstheorie*, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften (Berlin), 778–786
- **Karl Schwarzschild (1916).** Found the first exact Ricci-flat solution beyond Minkowski spacetime, the curved empty exterior of a spherical mass: a spacetime with $R_{\mu\nu} = 0$ that is not flat. Karl Schwarzschild (1916), *Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*, Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften (Berlin), 189–196

## Research horizon

- **Uniqueness of stationary Ricci-flat black holes.** Israel proved that a static, asymptotically flat, Ricci-flat spacetime with a regular, non-degenerate horizon is Schwarzschild, and Carter and Robinson extended this to the Kerr family for the stationary axisymmetric case. Globally, with a horizon and asymptotic flatness, the Ricci-flat equations leave only mass and spin free, in sharp contrast to the ten local Weyl components they allow. Werner Israel (1967), *Event Horizons in Static Vacuum Space-Times*, Physical Review 164, 1776–1779, doi:10.1103/PhysRev.164.1776; D. C. Robinson (1975), *Uniqueness of the Kerr Black Hole*, Physical Review Letters 34, 905–906, doi:10.1103/PhysRevLett.34.905
- **Nonlinear stability of Minkowski and the Kerr family.** Christodoulou and Klainerman proved that small perturbations of Minkowski data evolve under the Ricci-flat equations into spacetimes that stay close to Minkowski and radiate their Weyl curvature away as gravitational waves. The linear stability of Schwarzschild was settled by Dafermos, Holzegel and Rodnianski, and the nonlinear stability of slowly rotating Kerr black holes was proved by Klainerman, Szeftel and Giorgi in a series of works from 2021 on; the full subextremal range of spins remains the central active problem of mathematical relativity. Demetrios Christodoulou, Sergiu Klainerman (1993), *The Global Nonlinear Stability of the Minkowski Space*, Princeton Mathematical Series 41, Princeton University Press; Mihalis Dafermos, Gustav Holzegel, Igor Rodnianski (2019), *The linear stability of the Schwarzschild solution to gravitational perturbations*, Acta Mathematica 222, 1–214, doi:10.4310/ACTA.2019.v222.n1.a1; Sergiu Klainerman, Jérémie Szeftel (2023), *Kerr stability for small angular momentum*, Pure and Applied Mathematics Quarterly 19 (2023), arXiv:2104.11857
- **Ricci-flat metrics in Riemannian geometry.** Yau's proof of the Calabi conjecture gives a Ricci-flat Kähler metric on every compact Kähler manifold with vanishing first Chern class, the Calabi–Yau manifolds. None beyond flat tori and their quotients is known in closed form, and their moduli, degenerations and special holonomy remain active, with the string compactifications of the holonomy concept's horizon as one motivation. Shing-Tung Yau (1978), *On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I*, Communications on Pure and Applied Mathematics 31, 339–411, doi:10.1002/cpa.3160310304

## Review: novice

**Verdict:** fixed (2026-09-16, revision 4)

**Retell attempt:** In a cabin falling past a planet you let go of a ball of crumbs and it slowly stretches into an egg, but the egg takes up the same room as the ball, because the crumb toward the planet drifts out and the crumbs across drift in by half each, so the drifts add to zero. Far from all stars nothing drifts at all. Flat means nothing drifts anywhere in the region however the cabin moves. Ricci-flat means the drifts add to zero everywhere, in any cabin. So beside a planet it is Ricci-flat but not flat, and flat is the stricter one. Einstein's equation says the total is zero exactly where there is no matter, so Ricci-flat means empty. Where a gravitational wave passes it is Ricci-flat too, because the stretch and squeeze cancel. Near Earth two crumbs a metre apart drift a seventh of a millimetre in ten seconds. I am not sure what 'cabins moving in every way' means, or which crumb is the 'middle crumb', or which line 'the line at right angles' is for the wave, and 'the inside of a wave' sounds like a room. The 'other direction' sentence made me think of a direction in space. In the check I counted near, far and side and could not find the fourth crumb.

**Stumbles (15)**

- “That is weaker than flat, where nothing drifts at all.”: 'Weaker' reads as weaker curving; the sentence means a looser condition.
- “The crew's ruler, fixed to the cabin, shows that the egg takes up the same room as the ball did.”: A surprise with no reason within two sentences; the reason (three drifts cancel) arrives four paragraphs later, and the recap is hidden for readers arriving in sequence.
- “The two cabins pass two different tests.”: Reads as cabin one passes test one and cabin two passes test two; also 'pass' is never defined for either test.
- “in cabins moving through it in every way”: 'Every way' is vague; the second way says direction and speed.
- “drifts away from the middle crumb by some amount”: 'Middle crumb' is used before any crumb was placed at the middle in the explanation.
- “The two crumbs across that line each drift in by half that amount.”: Which two crumbs is implicit; the three directions at right angles were not tied to crumbs.
- “The other direction does hold.”: 'Direction' has meant a direction in space all through the way; here it means the converse.
- “Flat is the stronger of the two.”: Same double sense as 'weaker'.
- “ties the drift total at a spot to the matter at that very spot, and to nothing else.”: The paragraph before says the total depends on the cabin's speed, so 'nothing else' contradicts it; and the step from 'no matter' to 'every cabin finds zero' is implicit.
- “Inside a cloud of gas, the total is not zero: neither.”: Only one of the two verdicts is given a reason, and 'neither' is left bare.
- “crumbs along the line at right angles to that one draw together by the same fraction”: Two lines are at right angles to the first: the wave's own path and the other line across it; and 'fraction' has no reference.
- “the inside of a gravitational wave”: A wave is a travelling pattern, not a container; 'inside' suggests a room.
- “the crew lets go of four crumbs at rest around a middle crumb. The near crumb ... The far crumb ... The side crumb ... Add the three drifts.”: Four crumbs are announced but only three are named, so the reader cannot find the third direction the answer uses.
- “With no matter beside the planet, what does the curving there?”: 'What does the curving' is hard to parse on first read.
- “run the ball test”: 'Ball test' and 'Einstein's equation' are used across ways, checks and misconceptions without glossary entries.

**Fixes**

- Summary and first-way takeaway: replaced 'weaker' and 'stronger' with 'asks for more' and 'stricter' so the words compare conditions, not curving.
- Egg way: placed a crumb at the middle of the ball, gave the unchanged room its reason at once, defined what passing each test means, spelled out 'every direction and at every speed', named the two crumbs across the centre line, and replaced 'the other direction' by 'going the other way round'.
- Zero-total way: Einstein's equation now names both things the total depends on (matter at the spot, the cabin's motion) in short sentences, with the explicit step that no matter gives zero for every cabin; the gas cloud gets both reasons; the wave's second line is named as the other line across its path with the fraction referred to the crumbs' gap; 'inside a wave' became 'the space a wave is passing through'.
- Seventh-of-a-millimetre check: added the fourth crumb and said which three drifts to add; answer and key points name it.
- Four-regions check answer and wave problem statement: the squeezed line is now the other line across the wave's path.
- Common question reworded; glossary entries ball test and Einstein's equation added. Nothing was dropped.

**Concerns**

- Wave problem: the mirror movement of 'about a thousandth of the width of a proton' with numeric 0.001 (rel_tol 0.5) sits below 4e-18 m divided by a proton width of about 1.7e-15 m (about 0.0024); the physics reviewer should confirm the phrase and the tolerance.
- The note says 'beside a planet' while the ricci-tensor prerequisite says 'near a planet', and this note's Earth number says 'near Earth'. Both are clear to a novice, so not changed; an editor may standardize.
- Entry claim that 'flat' means the first test passes for cabins moving in every direction and at every speed (all observers' tidal drifts vanish exactly when Riemann vanishes) is left for the physics reviewer to confirm.
- Budgets after this review: 7,797 words of the 9,500 total cap; tutoring 2,771 is above the 80 percent draft ceiling of 2,640 but well under the 3,300 cap.

**Re-read** (2026-09-16, revision 4): 5 stumbles in 7 changed passages

- “rock, gas, dust, light and electric fields all count. A gravitational wave's energy is spread over the whole wave, at no one spot, so it does not count.”: Light is spread out over a beam too, so a reader cannot see why light counts and a gravitational wave does not; the surprise has no reason within two sentences (rule 9).
- “The wave carries energy, but that energy is spread over the whole wave and sits at no one spot, so it is not matter at the spot.”: Same missing reason in the zero-total way, where the reader meets the contrast first.
- “sits at no one spot; Einstein's equation counts only matter at the spot, and there is none.”: A 27-word sentence joined by a semicolon at entry; two ideas in one sentence.
- “a region that nothing reaches”: Reads as an unreachable place rather than a place nothing is arriving at.
- “It also leaves out the cosmological constant”: 'It' has no unmistakable noun (the phrase? the region?), and the cosmological constant is a new term with no glossary entry.
- Fix: Glossary 'matter' and the zero-total way now give the reason a light meter can read light's energy at a spot but no meter can read a gravitational wave's energy at one spot.
- Fix: Four-regions check answer: semicolon sentence split in two, claim unchanged.
- Fix: Egg way simplifies reworded (nothing arriving from elsewhere; 'This way also sets aside'); glossary entry 'cosmological constant' added with concept link.

## Review: physics

**Verdict:** fixed (2026-09-16, revision 4)

**Verification**

- Vacuum equals Ricci-flat: G_μν = 0 ⇔ R_μν = 0 for Λ = 0, n ≠ 2; with Λ the empty-space equation gives R_μν = Λ g_μν.: Re-derived by hand: g^μν G_μν = (1 − n/2) R, so R = 0 for n ≠ 2 and R_μν = 0 follows; with Λ, −R + 4Λ = 0 gives R = 4Λ and R_μν = ½R g − Λ g = Λ g (n = 4). → Correct, including the two-dimensional exception, where G_ab vanishes identically.
- General-dimension decomposition R_abcd = C_abcd + (g_ac R_bd − g_ad R_bc + g_bd R_ac − g_bc R_ad)/(n−2) − R(g_ac g_bd − g_ad g_bc)/((n−1)(n−2)); n = 3 coefficients 1 and ½; n = 2 form R_abcd = ½R(g_ac g_bd − g_ad g_bc).: Traced each term with g^ac using the course Ricci convention R_bd = g^ac R_abcd: Ricci terms give R_bd + R g_bd/(n−2), scalar term gives −R g_bd/(n−2), Weyl is trace-free. Checked the n = 3 trace 3R + Rg − R − R − ½R(3g − g) = R_bd and the n = 2 trace ½R(2g − g) = ½R g = R_bd. → Decomposition, three-dimensional key equation and derivation step 3 all correct; with n = 4 it matches the Weyl concept's formula (coefficients ½ and R/6).
- Vacuum Bianchi identity: ∇^a R_abcd = ∇_c R_bd − ∇_d R_bc, so ∇^a C_abcd = 0 where R_ab = 0.: Contracted ∇_e R_abcd + ∇_c R_abde + ∇_d R_abec = 0 with g^ea: g^ea R_abec = R^e_bec = R_bc and g^ea R_abde = R^e_bde = −R_bd by antisymmetry in the last pair. → Signs and index placement correct with the course Ricci convention R_μν = R^ρ_μρν.
- Component counts: Riemann n²(n²−1)/12 (6, 20), Ricci n(n+1)/2 (6, 10), Weyl n(n+1)(n+2)(n−3)/12 (0, 10, 35 for n = 3, 4, 5).: python3. → All counts as stated.
- Tidal signs: E_ij = c²R_î0̂ĵ0̂ has trace R_μν u^μ u^ν, tidal acceleration −E_ij ξ^j, so E = (GM/r³) diag(−2, 1, 1) means radial stretch 2GM/r³ and transverse squeeze GM/r³, and a positive trace shrinks a released ball.: Geodesic deviation D²ξ^μ/dτ² = −R^μ_νρσ u^ν ξ^ρ u^σ in the observer's orthonormal frame; R_t̂r̂t̂r̂ = −2M/r³ for Schwarzschild static observers. → Consistent throughout the note: star-exterior pattern, zero trace, and 'positive trace, ball shrinks' all carry the right sign.
- Perfect-fluid results: T = −ρc² + 3p, R = −8πGT/c⁴, comoving tidal trace 4πG(ρ + 3p/c²); radiation gives R = 0 and 8πGρ; dust gives R = 8πGρ/c².: Hand algebra from T^μν = (ρ + p/c²)u u + p g with u·u = −c² and the trace-reversed equation R_μν = (8πG/c⁴)(T_μν − ½T g_μν). → Correct; check radiation-universe-is-scalar-flat and the worked example agree.
- String gas p = −ρc²/3: R_0̂0̂ = 0, R_îî = 16πGρ/3c², and an observer at β = 0.6 reads γ²β²c²R_x̂x̂ = 3πGρ.: python3: γ² = 1.5625, 1.5625 × 0.36 × 16/3 = 3.0. Also checked the dust claim 'a racing cabin finds a bigger total': γ²(1+β²)·4πGρ = 8.5πGρ > 4πGρ. → Correct, including the space-space components; the numeric tolerances are met.
- Charged ball: R = 0, R_μν u^μ u^ν = 4πGε₀E²/c², R_0̂0̂ = 4πGε₀E²/c⁴ = 8.3 × 10⁻⁴² m⁻² for E = 3 × 10⁶ V/m.: python3 with G = 6.6743e−11, ε₀ = 8.8542e−12, c = 2.9979e8: 8.27e−42 m⁻²; T_0̂0̂ = ½ε₀E² from the course electromagnetic stress-energy row. → Correct; within the 5 percent tolerance.
- Earth crumbs: two crumbs one metre apart along the radial line, released at rest just above the air, separate by about a seventh of a millimetre in ten seconds; side crumbs close by half that.: python3: GM/R³ = 1.54e−6 s⁻², Δ = (GM/R³)·1 m·(10 s)² = 0.154 mm; side −0.077 mm; total zero. Cabin falls 490 m in ten seconds, a negligible change of radius; shear-induced volume change is 5e−8 relative, far below ruler precision. → 0.154 mm against 1/7 = 0.143 mm: 'about a seventh' is fair, and the check tolerances 0.14 ± 0.03 and −0.07 ± 0.02 contain the computed values. 'Earth's surface tidal gradient 3e−6 s⁻²' is 2GM/R³ = 3.08e−6 s⁻².
- Sun at Earth's distance: GM/r³ = 4.0e−14 s⁻², radial separation rate 7.9e−14 m s⁻² per metre.: python3 with GM_sun = 1.327e20 m³ s⁻², r = 1.496e11 m. → 3.96e−14 and 7.93e−14: correct.
- Cosmological constant: tidal trace −Λc² ≈ −1e−35 s⁻², about thirty powers of ten below 3e−6 s⁻².: python3 with Λ = 1.1e−52 m⁻²: −9.9e−36 s⁻²; ratio 3.1e29. → Correct; sign negative (a released ball expands), as R_μν = Λ g_μν with u·u = −c² requires.
- Kretschmann from the electric part: K = 8 E_ij E_ij when B = 0; E = (M/r³) diag(−2, 1, 1) gives 48M²/r⁶.: Vacuum identity R_abcd R^abcd = 8(E_ij E_ij − B_ij B_ij); python3 sum of squares 4 + 1 + 1 = 6, times 8 = 48, the known Schwarzschild value. → Correct, in SI 48G²M²/c⁴r⁶.
- Inverse-cube check: ∂_i[f(δ_ij − 3n_i n_j)] = −n_j(2f′ + 6f/r); zero only for f ∝ r⁻³; trial power r⁻ᵏ gives coefficient (2k − 6).: Hand calculation with ∂_i n_j = (δ_ij − n_i n_j)/r, ∂_i n_i = 2/r, n_i ∂_i n_j = 0; python3 for k = 2, 3, 4: −2, 0, 2. → Correct; the linearized vacuum Bianchi constraint for static observers is indeed ∂_i E_ij = 0.
- Entry: 'flat' as no drift in cabins moving in every direction and at every speed, and 'Ricci-flat' as zero total for all such cabins, match Riemann = 0 and Ricci = 0.: Polarization: R_μνρσ u^ν u^σ = 0 for all timelike u forces R_μ(ν|ρ|σ) = 0; combined with the first Bianchi identity this gives R_μνρσ = −2R_μνρσ, so Riemann vanishes (the electric parts of all observers determine Riemann). For Ricci, a symmetric tensor vanishing on the open cone of timelike vectors vanishes. → Both entry definitions are exactly right, and 'every speed' is necessary: the string-gas check shows one family reading zero without Ricci-flatness.
- Entry shortcut 'Einstein's equation ties the drift total a cabin finds to matter at the spot and how the cabin moves; no matter gives zero for every cabin; Ricci-flat exactly when no matter sits anywhere'.: R_μν u^μ u^ν = (8πG/c⁴)(T_μν − ½T g_μν)u^μ u^ν with Λ = 0; trace reversal is invertible, so T = 0 ⇔ Ric = 0. → Correct with Λ = 0, which the way's simplifies states. The one gap was the word 'matter' defined as 'anything that carries energy' while the wave problem says the wave's energy is not matter at the spot; fixed by defining matter as energy that sits at a spot and saying a wave's energy sits at no one spot.
- GW150914 mirror movement 'about a thousandth of the width of a proton', numeric 0.001 with rel_tol 0.5; observation 'about 2e−18 m per 4 km arm'.: python3: peak strain 1.0e−21 changes each arm by hL/2 = 2.0e−18 m; proton diameter about 1.7e−15 m; ratio 1.2e−3. The novice's 4e−18 m is the differential arm change hL, which is not what one mirror pair moves. → Phrase and tolerance confirmed; no change.
- FLRW: conformally flat, so Ricci-flat FLRW is flat; sourceless Friedmann equation ȧ² = −kc² gives Minkowski (k = 0) or Milne (k = −1, a = ct).: Hand check of both Friedmann equations with ρ = p = Λ = 0. → Correct; k = +1 has no real solution.
- K3 surface: Ricci-flat Kähler metric by Yau, no flat metric since χ = 24.: Gauss–Bonnet–Chern: a compact flat manifold has χ = 0; K3 has χ = 24. → Correct.
- Analogy: source-free electric field outside a charged ball stands for Ricci-flat curvature with nonzero Weyl.: Gauss's law ∇·E = ρ/ε₀ = 0 outside, E ≠ 0; relation holds in sense and sign. The analogy's limits already note that a real field carries stress-energy. → Accurate as stated; the charged-ball problem gives the learner the real case.
- References: Bertotti–Iess–Tortora 2003 (Nature 425, 374–376); Abbott et al. 2016 (PRL 116, 061102); Einstein 1915 (Sitzungsberichte 778–786, 4 November); Schwarzschild 1916 (Sitzungsberichte 189–196); Israel 1967 (Phys. Rev. 164, 1776–1779); Robinson 1975 (PRL 34, 905–906); Christodoulou–Klainerman 1993 (Princeton Mathematical Series 41); Dafermos–Holzegel–Rodnianski 2019 (Acta Math. 222, 1–214, arXiv:1601.06467); Yau 1978 (Comm. Pure Appl. Math. 31, 339–411); Klainerman–Szeftel 2023 (Pure Appl. Math. Q. 19, arXiv:2104.11857).: One web search each against publisher, ADS, arXiv or Project Euclid records. → All ten confirmed and marked verified. Cassini number γ − 1 = (2.1 ± 2.3) × 10⁻⁵ and the peak strain 1.0 × 10⁻²¹ match the papers.
- History scope: Einstein's 4 November 1915 paper gave equations whose empty-space form is R_μν = 0, used for Mercury on 18 November; Schwarzschild's paper of 13 January 1916 gave the first non-trivial exact solution.: Dates checked against the Sitzungsberichte records found in the searches. → Accurate. Schwarzschild's contribution reworded to drop the claim that it 'showed at once' that R_μν = 0 is not flatness, a reading rather than a documented aim.
- Structure: prerequisites direct and acyclic; assumes and justified_by consistent; formal rung has two formal checks and one formal problem; every check and problem evidences an objective at its rung; misconceptions and targets agree; three research topics with references.: Digests of ricci-tensor, flatness-criterion, weyl-tensor, bianchi-identity and the registry entry of einstein-field-equations (no note yet); none lists ricci-flat-spacetime as a prerequisite. Cross-checked every evidenced_by, targets and diagnosed_by id by hand. → Consistent. Prerequisites still differ from the registry (flatness-criterion, einstein-field-equations, bianchi-identity added), which sync_registry.py applies. All three visuals are proposals with sketches; falling-ring-of-crumbs and six-entry-curvature-table are already proposed by neighbouring notes, so the ids are shared, not invented.

**Counterexamples tried**

- Two and three dimensions: Ricci-flat forces flat; the note states this and the three-dimensional check proves it. Confirmed by the trace inversion.
- Plane gravitational wave: Ricci-flat, curved, every polynomial invariant zero. Breaks any claim that a nonzero invariant is needed to show curvature; the note only says a nonzero invariant suffices, and names plane waves as the Lorentzian exception. Survives.
- Cosmological constant: de Sitter is empty but not Ricci-flat. The zero-total way's simplifies scopes it out; the first entry way said 'far from every star, spacetime is flat' with no scope, so a simplifies was added there covering Λ and passing waves.
- Electromagnetic field outside a charged ball: scalar-flat but not Ricci-flat; the note's 'no matter includes no light and no electric field' and the charged-ball problem cover it.
- String gas p = −ρc²/3: comoving observers read a zero tidal trace without Ricci-flatness. Covered by the crossing-a-string-gas check; it is why 'every speed' is in the entry definition.
- Milne universe: an FLRW model that is Ricci-flat and flat. Named in the formal way and on the sorting board.
- Gravitational-wave energy: a wave carries energy yet T_μν = 0 where it passes. The glossary's 'matter is anything that carries energy' contradicted the wave problem; fixed by 'energy that sits at a spot'.
- Strong field: the static-observer tide (GM/r³) diag(−2, 1, 1) is exact for Schwarzschild at every r > 2GM/c², so the star-exterior statements need no weak-field scope. Kerr static observers do measure a magnetic part, which is why the note says 'static star'.
- Other observer: a boosted observer in Schwarzschild sees a different E_ij, still trace-free; consistent with 'for every observer'.
- Shear-induced volume change: a released ball in vacuum does lose volume at fourth order in time. The recap says 'at first'; at ten seconds near Earth the effect is 5e−8 relative, invisible to the crew's ruler, so the entry wording stands.
- Riemannian compact case: flat tori are Ricci-flat and flat, K3 is Ricci-flat and not flat; 'none known in closed form' was too strong and now excludes flat tori and their quotients.

**Fixes**

- Zero-total way, glossary 'matter', wave problem key point, four-regions check answer and the wave-needs-matter correction: matter is now 'anything whose energy sits at a spot', and a gravitational wave's energy is said to be spread over the whole wave, at no one spot, so the entry text no longer contradicts itself about wave energy.
- Egg way: added a simplifies scoping 'far from every star and planet' to a region no wave reaches and leaving out the cosmological constant.
- Cassini observation: the post-Newtonian parameter is written γ_PPN, since γ is the Lorentz factor elsewhere in the note, as the course conventions require.
- Formal way: the vacuum Bianchi identity forces the inverse-cube fall-off of spherically symmetric tides (scope added); picture text now says the gap is ten Weyl components in dimension four and more in higher dimensions; 'tidal-tensor concept' renamed to the relativistic tidal tensor concept, the registry id.
- Research horizon: Israel's theorem now names a non-degenerate horizon; the Kerr-stability entry records the proof for slowly rotating Kerr by Klainerman, Szeftel and Giorgi with the Klainerman–Szeftel 2023 reference added, and leaves the full subextremal range open; Calabi–Yau 'none known in closed form' now excludes flat tori and their quotients.
- History: Schwarzschild's contribution reworded to a factual description of the solution.
- All ten references verified and marked verified.

**Concerns**

- Entry and working text changed (matter definition, wave-energy sentences, egg-way simplifies, Cassini γ_PPN, formal scope words), so the revision is now 3 and review.novice covers revision 2; the post-review novice check should read exactly the diff lines.
- Prerequisites still differ from the registry (flatness-criterion, einstein-field-equations, bianchi-identity); einstein-field-equations has no note yet, so its entry-level claims here rest on the glossary definition and 'stated here without proof'.
- Three cited visuals remain proposals; the catalog entry for falling-ring-of-crumbs will have to reconcile 23 notes' sketches.
- Klainerman–Szeftel 2023 is cited without page numbers (venue confirmed as Pure and Applied Mathematics Quarterly 19, 2023); an editor may add them.

**Diff check** (2026-09-16, revision 4)

- Matter is anything whose energy sits at a spot; light and electric fields count, a gravitational wave's energy does not.: Compared with the stress-energy tensor: the electromagnetic field has a local energy density (SI T^00 = eps0 E^2/2 + B^2/2mu0), while a vacuum gravitational wave has T_mn = 0 exactly and its energy is defined only after averaging over several wavelengths (no local gravitational stress-energy, by the equivalence principle). → Correct within the entry scope; the added light-meter sentences state exactly this operational difference.
- The region a gravitational wave passes is Ricci-flat though the crumbs drift; Einstein's equation counts only matter at the spot, and there is none.: Vacuum plane-wave solutions satisfy R_mn = 0 exactly; the transverse stretch and squeeze are the two polarization-frame components of R_i0j0, trace zero, with nothing along the propagation direction. → Correct.
- Egg way simplifies: no wave is passing far from every star, and the cosmological constant is set aside, a faint push apart that no cabin's ruler could notice.: Lambda = 1.1e-52 m^-2 gives an isotropic tidal acceleration Lambda c^2/3 = 3.3e-36 s^-2; two crumbs one metre apart move about 1.6e-34 m in ten seconds (python3). Positive Lambda drives free crumbs apart in every direction, so 'push apart' has the right sense. → Correct; unnoticeable by thirty-odd powers of ten, consistent with the note's Lambda number.
- Cassini: measured gamma_PPN - 1 = (2.1 +/- 2.3)e-5 matches general relativity's gamma_PPN = 1 from the Ricci-flat Schwarzschild exterior; symbol renamed per course conventions.: Checked the course-conventions post-Newtonian row (gamma_PPN where a Lorentz factor appears) and the Bertotti-Iess-Tortora value. → Correct.
- Reference: Klainerman and Szeftel, 'Kerr stability for small angular momentum', arXiv 2104.11857, Pure and Applied Mathematics Quarterly 19 (2023).: One web search. → Confirmed: authors, title and arXiv id match; the arXiv record cites the 2023 PAMQ publication.
- 'as the relativistic tidal tensor concept shows' for E_ij = (GM/r^3) diag(-2,1,1).: Trace -2+1+1 = 0; matches the Schwarzschild static-observer tidal tensor and the registry concept name. → Correct.
- Fix: None beyond the novice wording fixes; each was re-read as the novice and checked as a claim.
