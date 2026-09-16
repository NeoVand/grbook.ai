---
type: "concept"
schema_version: 2
id: "circumference-to-radius-test"
title: "Circumference-to-radius test"
tagline: "How a ring's length, compared with the string that draws it, reveals curvature"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["circumference deficit test", "Bertrand–Diguet–Puiseux theorem", "ring test"]
prerequisites: ["curvature", "line-element"]
leads_to: ["sectional-curvature", "ricci-scalar", "curvature-density-parameter"]
visuals: ["paced-ring-on-a-ball-and-a-plain"]
---

# Circumference-to-radius test

*How a ring's length, compared with the string that draws it, reveals curvature*

`circumference-to-radius-test` · curvature · foundation · physics-reviewed (revision 7)

**Needs:** [[curvature]] (entry) · [[line-element]] (working)  
**Opens:** [[sectional-curvature]] · [[ricci-scalar]] · [[curvature-density-parameter]]  
**Related:** [[gaussian-curvature]] · [[intrinsic-geometry]] · [[angular-excess]]  
**Visuals:** ★ [[paced-ring-on-a-ball-and-a-plain]]

> Measure out the same distance along a surface from a centre in every direction, for example with a tight string, and draw a ring through the far ends. On a playground the ring is about 6.28 times that distance. On a ball it comes out shorter; near a swim ring's hole it comes out longer. Away from sharp points, how much a small ring is too short or too long tells someone living on the surface how strongly it curves there. Too short means positive curvature, and too long means negative curvature.

## You will be able to

**Entry**
- Explain how a ring drawn with a tight string and measured along a ball shows that the ball is curved. `objectives/explain-the-ring-test` ← `checks/string-ring-on-a-football`
- Predict from a small ring's length whether the curvature around its centre is positive, zero or negative. `objectives/read-the-sign-from-a-ring` ← `checks/a-ring-that-is-too-long`
- Estimate how a small ring's missing fraction changes when the string is doubled or halved. `objectives/scale-the-shortfall` ← `problems/double-the-string-on-earth`

**Working**
- Compute a surface's curvature and its sign from one measured small ring. `objectives/compute-curvature-from-a-ring` ← `checks/curvature-from-one-ring`
- Compute how far a cosmic ring may differ from the flat length, given the curvature density parameter. `objectives/apply-the-test-to-the-universe` ← `problems/cosmic-ring-excess`

**Formal**
- State the Bertrand–Diguet–Puiseux theorem with its hypotheses, and use its exact integral form. `objectives/state-and-use-the-theorem` ← `checks/rings-outside-a-star`, `problems/disc-area-and-ring-growth`
- Distinguish the curvature a ring test finds in a spatial slice from the curvature of spacetime. `objectives/separate-slice-from-spacetime` ← `checks/milne-slices`

## Ways in

### 1. Draw a ring with a string · entry · operational

*How can a ring drawn with a string show someone living on a ball that the ball is curved?*

On a playground, push a peg into the ground and tie a string to it. Pull the string tight along the ground, and hold a piece of chalk at its far end. Walk once around the peg, keeping the string tight, so that the chalk draws a ring.

The string's length is the ring's radius. School geometry says the ring's length is 2 times pi times its radius, which is about 6.28 times the string. This length is called the ring's playground length.

Now do the same on a football, the round kind used in soccer, about 70 centimetres around its middle. Tape one end of a string to a spot on the ball. Pull the string tight along the ball's surface, never through the air, and draw a ring with a felt-tip pen at its far end. Then lay a soft tape measure along the ring, bending it to follow the line you drew.

Think of the ball as a globe, with the taped spot as its North Pole. A ball measures the same all the way around, whichever way you go, so a line drawn around the ball through both poles is also 70 centimetres long. The North Pole to the South Pole is half of that line, and the equator is halfway between the poles. So the equator is a quarter of the way around the ball from the spot, in every direction.

A quarter of 70 centimetres is 17.5 centimetres. So a string 17.5 centimetres long draws the equator as its ring, and the equator is 70 centimetres long. On a playground, a 17.5-centimetre string draws a ring about 110 centimetres long. The ball's ring is short by more than a third.

Comparing a ring's length, measured along the surface, with its playground length is called the ring test.

On flat ground, every ring drawn this way has its playground length. On the ball, every ring comes out short, even with a string much shorter than 17.5 centimetres. So the ball is not flat, but curved.

Seen from outside, the equator is an ordinary circle whose centre lies deep inside the ball. Someone who lives on the ball can never go there, but needs only a string and a tape laid along the surface to find out that the ball is curved.

**Try it:** Tape one end of a string to a spot on a football about 70 centimetres around. Tie a felt-tip pen to the string 10 centimetres from the tape. Keep the string tight against the ball and draw a ring. Lay a soft tape measure along the ring, bending it to follow the line: it reads about 55 centimetres. The same string on flat paper draws a ring about 63 centimetres long.

**Takeaway:** A ring drawn with a tight string on flat ground is about 6.28 times the string, but on a ball the ring comes out shorter, so the ball is not flat.

*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/string-ring-on-a-football`

### 2. Too short, just right, too long · entry · contrast

*What does the ring test find on surfaces that are not balls?*

**Recap:** The ring test: pull a string tight along a surface from a centre, and draw a ring with its far end. Then compare the ring's length with its playground length, 6.28 times the string. Walking without ever steering left or right is called walking straight. Two straight walkers start parallel when they stand side by side on a straight line, facing the same way at a right angle to it. Where such walkers draw together, the curvature is positive. Where they keep their gap, it is zero. Where they spread apart, it is negative.

On the football in "Draw a ring with a string", the ring came out short. Now try the ring test on two more surfaces.

First, roll a sheet of printer paper into a tube about 30 centimetres around, and tape its edges together. From outside, the tube looks bent. Draw a ring on it with a 5-centimetre string. Keep the string shorter than half the way around the tube, which is 15 centimetres, or the string reaches around the back of the tube.

Now peel off the tape and unroll the sheet. Every point of the ring sat 5 centimetres from the centre, measured along the paper. Paper does not stretch, so unrolling changes no length along the paper. On the flat sheet, every point of the ring still sits 5 centimetres from the centre, so the ring is an ordinary circle, about 31.4 centimetres long. So on the tube, too, the ring was 31.4 centimetres long, its playground length.

Why do other surfaces change a ring's length? A tight string lies along a straight walk. If its path steered anywhere, sliding that bend sideways would shorten the path between its ends, and the string would go slack. So a tight string never steers.

Strings leaving the centre in neighbouring directions are therefore straight walks. Near the centre, they fan apart just as on a playground. A ball draws straight walkers together, so the gap between two neighbouring strings' far ends grows more slowly than on a playground. The ring's length is all those gaps added up, so the ring comes out short.

Second, take a swim ring, the blown-up ring that children float in. Put the centre on its inner circle, the circle that runs all the way around the hole, closest to it. A tight string from the centre, laid along that circle, would lift off and cut across the hole, like a string pulled tight around the inside of a cup. Walk straight from the centre instead, the same distance in every direction. Straight walkers that start parallel spread apart near that circle. So the gaps between the walks' far ends grow faster than on a playground, and a small ring comes out too long.

A small ring therefore tells you the curvature around its centre, as long as that centre is not a sharp point like a cone's tip. A short ring means positive curvature. A ring of its playground length means zero curvature. A ring that is too long means negative curvature.

**Try it:** Press a frilly lettuce leaf flat on a plate with your palm. However you press, its edge folds over itself in several places. The edge is too long to lie flat around the leaf's middle, like a ring that comes out too long. Then press a small piece of orange peel flat. Its edge is too short to lie flat around its middle, like a ring that comes out short, so the edge stretches and splits.

**Takeaway:** A small ring that comes out short means positive curvature around its centre, one of its playground length means zero curvature, and one that comes out too long means negative curvature. All three readings need a centre with no sharp point.

*Continues:* `ways_in/draw-a-ring-with-a-string`<br>*Builds on:* [[curvature]]<br>*Visuals:* [[paced-ring-on-a-ball-and-a-plain]]<br>*See:* `checks/a-ring-that-is-too-long`

### 3. Double the string · entry · calculation

*How fast does a ring's shortfall grow as the string gets longer?*

**Recap:** The ring test: pull a string tight along a surface from a centre, and draw a ring with its far end. Then compare its length with its playground length, 6.28 times the string. On a football about 70 centimetres around, the ring comes out short.

On the football in "Draw a ring with a string", measure the rings for two strings. For each ring, divide the length it is missing by its playground length. The result is called the missing fraction.

A 5-centimetre string draws a ring about 30.4 centimetres long. Its playground length is 31.4 centimetres. So the ring misses about 1 centimetre, and 1 divided by 31.4 is about 3 parts in 100.

A 10-centimetre string draws a ring about 54.7 centimetres long, against a playground length of 62.8 centimetres. That ring misses about 8 centimetres, which is about 13 parts in 100.

Doubling the string made the missing fraction about four times bigger, not twice as big. For small rings this is the rule: double the string, and the missing fraction becomes about 2 times 2, or 4 times, as big. The rule is close for strings much shorter than a quarter of the way around the ball, and it gets better the shorter the string.

Why four times? The ball draws neighbouring strings together only gently at first, and more strongly the farther they reach. So the missing length builds up faster than the string grows.

Halving the string makes the missing fraction about four times smaller.

Earth, treated as a smooth ball, is about 40,000 kilometres around. Pull a string 30 kilometres along the ground and draw a ring. The ring is about 188 kilometres long, and it misses its playground length by only about 70 centimetres. That is less than 4 millimetres in every kilometre of ring, so nobody notices it in daily life.

**Takeaway:** For small rings, doubling the string makes the missing fraction about four times bigger, so a string tiny compared with the ball draws a ring that misses almost nothing.

*Continues:* `ways_in/draw-a-ring-with-a-string`<br>*See:* `problems/double-the-string-on-earth`

### 4. The small-ring law from the gap law · working · calculation

*How exactly does the shortfall of a small ring give the curvature at its centre?*

In "Double the string", doubling the string made a small ring's missing fraction about four times bigger. That rule, and the curvature it measures, follow from the gap law. Near a point $p$ of a smooth surface, label each place by its ground distance $\rho$ from $p$ and the direction $\phi$ of the geodesic that reaches it. Taking on trust that these geodesics cross the rings $\rho = \text{const}$ at right angles, the line element is

$$ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2,$$

and a ring has length $C(\rho) = \int_0^{2\pi} f\,d\phi$. A plane has $f = \rho$. A sphere of radius $a$ has $f = a\sin(\rho/a)$, so $C = 2\pi a\sin(\rho/a)$.

Neighbouring geodesics from $p$ are a distance $D = f\,\delta\phi$ apart. The curvature note states the gap law $\partial_\rho^2 D = -KD$ for geodesics that start parallel; it holds equally for neighbouring geodesics leaving one point, which is taken on trust here. Near $p$ the ground is flat to first order, so $f = 0$ and $\partial_\rho f = 1$ at $\rho = 0$. The derivation "Small rings from the gap law" expands $f$ one move at a time and finds

$$C(\rho) = 2\pi\rho - \frac{\pi}{3}K(p)\,\rho^3 + O(\rho^4),\qquad K(p) = \lim_{\rho\to0}\frac{3\,(2\pi\rho - C)}{\pi\rho^3}.$$

The missing fraction is $K\rho^2/6$: quadratic in $\rho$, and proportional to $1/a^2$ on a sphere. For the football, $a = 70\ \text{cm}/2\pi = 11.14$ cm, and the 10 cm ring has $\rho^2/6a^2 = 13.4\%$, against the exact $12.9\%$; the difference is the next order. The signs match "Too short, just right, too long": $K > 0$ gives short rings, and a surface with $K = -1/a^2$ has $f = a\sinh(\rho/a)$, so every ring is too long.

The law has two hypotheses. The centre must be a smooth point: a paper cone with a wedge of angle $\delta$ removed has $f = (1 - \delta/2\pi)\rho$ around its tip, so $\partial_\rho f \neq 1$ there. And the ring must be small enough that geodesics from $p$ have not met again, which on the paper tube of "Too short, just right, too long" fails for strings longer than half its circumference.

**Takeaway:** A small ring misses the flat length by a fraction equal to the Gaussian curvature at its centre times the radius squared over six, so one measured ring gives the curvature.

*Continues:* `ways_in/double-the-string`, `ways_in/too-short-just-right-too-long`<br>*Builds on:* [[curvature]], [[line-element]]<br>*See:* `derivations/small-rings-from-the-gap-law`, `checks/curvature-from-one-ring`, `worked_examples/rings-at-constant-negative-curvature`

### 5. Rings around us in the universe · working · operational

*How can astronomers run the ring test on space itself?*

The small-ring law of "The small-ring law from the gap law" also holds in three-dimensional space, for rings in any plane through the centre, with $K$ the curvature of that plane. A universe that looks the same everywhere and in every direction has, at one cosmic time $t$, the same $K$ for every plane at every point. In the course FLRW metric, the ring in the plane $\theta = \pi/2$ at coordinate $r$ has length $C = 2\pi a(t)\,r$, where $a(t)$ is now the scale factor, which multiplies every distance between galaxies at cosmic time $t$, not a sphere's radius. A ruler laid out from the centre at fixed $t$ reads, for $k > 0$,

$$\ell = a\int_0^r \frac{dr'}{\sqrt{1 - kr'^2}} = \frac{a}{\sqrt k}\arcsin\big(\sqrt k\,r\big).$$

So $C = 2\pi(a/\sqrt k)\sin(\sqrt k\,\ell/a)$, a sphere's rings with $K = k/a^2$. For $k < 0$ the sine becomes a hyperbolic sine and every ring is too long.

Nobody lays rulers across the universe, but light does the comparing. Light reaches us along radial lines, and angles on the sky are set by the $a^2r^2\,d\Omega^2$ part of the metric. So a pattern whose size, scaled up to today by the expansion, is $L$ spans the angle $\vartheta = 2\pi L/C$, where $C$ is today's length of the ring through it. Where rings are short, the pattern looks larger than in flat space at the same ruler distance.

Two patterns have calculable sizes: the imprint of sound waves in the cosmic microwave background, and its echo in the clustering of galaxies. Their measured angles, with ruler distances computed from the measured expansion history, give the curvature density parameter $\Omega_K = -Kc^2/H_0^2$, where $H_0$ is the Hubble constant, today's expansion rate. $\Omega_K$ is positive for negatively curved space. The combined result is $\Omega_K = 0.001 \pm 0.002$. With $K = -\Omega_K H_0^2/c^2$ the small-ring law becomes

$$\frac{C}{2\pi\ell} \approx 1 + \frac{\Omega_K}{6}\left(\frac{H_0\ell}{c}\right)^2.$$

The ring through the region that emitted the microwave background has $\ell \approx 13.9$ Gpc ($4.3\times10^{26}$ m, about 45 billion light-years). With $H_0 = 67.4$ km/s/Mpc ($2.18\times10^{-18}\ \text{s}^{-1}$), $H_0\ell/c = 3.12$, so that ring matches $2\pi\ell$ to $(0.2 \pm 0.3)\%$.

**Takeaway:** Patterns of known size on the sky test whether rings around us have the flat length, and space on the largest scales passes to within a fraction of a percent.

*What this leaves out:* Treats the universe as exactly uniform, and uses space at one cosmic time; slicing spacetime into space differently gives different ring lengths.

*Continues:* `ways_in/ring-law-from-the-gap-law`<br>*Builds on:* [[line-element]]<br>*See:* `observations/flatness-of-space-from-sound-patterns`, `problems/cosmic-ring-excess`

### 6. Geodesic circles: the theorem and its limits · formal · structure

*Under what hypotheses do geodesic circles determine curvature, and what exactly do they measure?*

The small-ring law of "The small-ring law from the gap law" becomes a theorem once its hypotheses are explicit. Let $(M, g)$ be a smooth Riemannian 2-manifold, $p \in M$, and $0 < r < \mathrm{inj}(p)$. Then the geodesic circle $S_r(p) = \exp_p\{v \in T_pM : |v| = r\}$ is a smooth closed curve, equal to the set of points at distance $r$, bounding the geodesic disc $B_r(p)$. By the Gauss lemma, $g = dr^2 + G(r,\theta)\,d\theta^2$, where $\sqrt G$ is the norm of the Jacobi field along each radial geodesic with $J(0) = 0$ and $J'(0)$ a unit vector perpendicular to that geodesic. So $\partial_r^2\sqrt G = -K\sqrt G$ and $\sqrt G = r - K(p)\,r^3/6 + O(r^4)$.

Theorem (Bertrand–Diguet–Puiseux). Integrating over $\theta$, then over $r$,

$$L(r) = 2\pi r - \tfrac{\pi}{3}K(p)\,r^3 + O(r^4),\qquad A(r) = \pi r^2 - \tfrac{\pi}{12}K(p)\,r^4 + O(r^5).$$

An exact form holds for every $r < \mathrm{inj}(p)$. The geodesic curvature of $S_r$ is $k_g = \partial_r\sqrt G/\sqrt G$, so $\oint k_g\,ds = L'(r)$, and the local Gauss–Bonnet theorem for the disc, taken as known, gives $L'(r) = 2\pi - \iint_{B_r(p)} K\,dA$. A ring's growth rate measures the total curvature it encloses, not the curvature along it.

In $n$ dimensions, the circle swept by geodesics tangent to a 2-plane $\sigma \subset T_pM$ has $L = 2\pi r\,(1 - K(\sigma)\,r^2/6 + O(r^3))$, with $K(\sigma)$ the sectional curvature, and a geodesic sphere has $(n-1)$-volume proportional to $r^{n-1}(1 - \mathcal R(p)\,r^2/6n + O(r^3))$, which reads the Ricci scalar $\mathcal R$.

Three limits. First, beyond $\mathrm{inj}(p)$ distance circles escape the law: on a flat cylinder of circumference $\ell_c$, the points at distance $r > \ell_c/2$ form two loops of total length $2r\,(\pi - 2\arccos(\ell_c/2r)) < 2\pi r$. Second, the centre must be smooth: a cone of deficit angle $\delta$ has $L = (2\pi - \delta)\,r$, so the limit diverges, while the exact form survives with curvature $\delta$ concentrated at the tip. Third, in spacetime, with $G = c = 1$, the test applies to a Riemannian slice, and slices of one spacetime differ. In Minkowski spacetime, the events at proper time $\tau$ after an event, along inertial worldlines through it, form a hyperbolic space with $K = -1/\tau^2$, although the spacetime Riemann tensor vanishes; the Painlevé–Gullstrand slices of Schwarzschild spacetime are exactly flat. A ring test in space measures the slice, whose curvature the Gauss equation ties to spacetime curvature and the slice's extrinsic curvature.

**Takeaway:** Around a smooth centre, and below the injectivity radius, geodesic circles give the Gaussian curvature and their growth rate gives the enclosed total; in spacetime they measure a slice.

*Continues:* `ways_in/ring-law-from-the-gap-law`, `ways_in/rings-around-us-in-the-universe`<br>*Builds on:* [[geodesic]]<br>*See:* `checks/rings-outside-a-star`, `checks/milne-slices`, `problems/disc-area-and-ring-growth`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| ring test | — | Measure out the same distance along a surface from a centre in every direction, for example with a tight string. Then compare the length of the ring through the far ends, measured along the surface, with 6.28 times that distance. | [[circumference-to-radius-test]] |
| playground length | — | The length a ring would have on flat ground: 2 times pi times the distance measured out from the centre, about 6.28 times that distance. | — |
| missing fraction | — | The length by which a ring falls short of its playground length, divided by that playground length. | — |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| start parallel | — | Two straight walkers start parallel when they stand side by side on a straight line, facing the same way at a right angle to it. | [[curvature]] |
| curvature | — | The way a surface makes straight walkers that start parallel draw together, keep their gap, or spread apart. | [[curvature]] |
| positive curvature | — | Curvature that makes straight walkers that start parallel draw together, as on a ball. | [[curvature]] |
| negative curvature | — | Curvature that makes straight walkers that start parallel spread apart, as near a swim ring's hole. | [[curvature]] |
| flat | — | Having zero curvature everywhere, so straight walkers that start parallel keep their gap, as on a playground. | [[curvature]] |

## Key equations

### Small-ring law · working

$$
C(\rho) = 2\pi\rho - \frac{\pi}{3}K(p)\,\rho^3 + O(\rho^4),\qquad K(p) = \lim_{\rho\to0}\frac{3\,(2\pi\rho - C)}{\pi\rho^3}
$$

A small ring misses the flat length by the fraction $K(p)\rho^2/6$, so ever smaller rings give the curvature at their centre.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $C(\rho)$ | length of the ring of ground radius $\rho$ | the ring's length |
| $K(p)$ | Gaussian curvature at the centre $p$ | the curvature at the centre |

**Holds when:** Smooth surface; $p$ a smooth point; $\rho$ smaller than the distance at which geodesics from $p$ meet again.  
**Say it:** “The ring's length is two pi rho, minus pi over three times the curvature at the centre times rho cubed; so the curvature is the limit of three times the shortfall over pi rho cubed.”  
**Justified by:** `derivations/small-rings-from-the-gap-law`

### Ring growth and enclosed curvature · formal

$$
L'(r) = 2\pi - \iint_{B_r(p)} K\,dA
$$

The rate at which geodesic circles lengthen equals $2\pi$ minus the total curvature of the disc they bound.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $L'(r)$ | derivative of the geodesic circle's length with respect to its radius | the ring's growth rate |
| $B_r(p)$ | the geodesic disc of radius $r$ about $p$ | the disc |

**Holds when:** Smooth Riemannian surface, $0 < r < \mathrm{inj}(p)$; follows from the local Gauss–Bonnet theorem.  
**Say it:** “The ring's growth rate is two pi minus the curvature added up over the disc.”  
**Justified by:** `stated`

## Derivations

### Small rings from the gap law · working

**Goal:** Show that a small ring of ground radius $\rho$ around a smooth point $p$ has length $2\pi\rho - \tfrac{\pi}{3}K(p)\rho^3 + O(\rho^4)$.

1. Label places near $p$ by ground distance $\rho$ and direction $\phi$. Taking on trust that geodesics from $p$ cross the rings at right angles, $ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2$, so $C(\rho) = \int_0^{2\pi} f\,d\phi$.
2. Two geodesics from $p$ with directions $\phi$ and $\phi + \delta\phi$ are a distance $D = f\,\delta\phi$ apart at ground distance $\rho$.
3. The gap law $\partial_\rho^2 D = -KD$, stated for geodesics that start parallel, holds equally for neighbouring geodesics leaving one point (taken on trust), so $\partial_\rho^2 f = -Kf$, with $K$ taken along the geodesic.
4. The geodesics start together, so $f(0,\phi) = 0$. Very near $p$ the ground is flat to first order, so the gap grows as $\rho\,\delta\phi$ and $\partial_\rho f(0,\phi) = 1$.
5. At $\rho = 0$ the gap law gives $\partial_\rho^2 f = -K(p)\cdot 0 = 0$.
6. Differentiate the gap law once: $\partial_\rho^3 f = -(\partial_\rho K)f - K\,\partial_\rho f$, which at $\rho = 0$ is $-K(p)$.
7. Taylor's theorem gives $f = \rho - K(p)\,\rho^3/6 + O(\rho^4)$.
8. Integrate over $\phi$: $C(\rho) = 2\pi\rho - \tfrac{\pi}{3}K(p)\,\rho^3 + O(\rho^4)$.
9. Solve for the curvature and let $\rho \to 0$: $K(p) = \lim 3(2\pi\rho - C)/\pi\rho^3$.
10. Check on a sphere of radius $a$: $f = a\sin(\rho/a)$ obeys $\partial_\rho^2 f = -f/a^2$ with $f(0) = 0$ and $\partial_\rho f(0) = 1$, and $a\sin(\rho/a) = \rho - \rho^3/6a^2 + \dots$, so $K = 1/a^2$.

**Result:** $C(\rho) = 2\pi\rho\,\big(1 - K(p)\,\rho^2/6\big) + O(\rho^4)$, and $K(p) = \lim_{\rho\to0} 3(2\pi\rho - C)/\pi\rho^3$.

## Worked examples

### Rings on a surface of constant negative curvature · working

**Problem:** A surface has line element $ds^2 = d\rho^2 + a^2\sinh^2(\rho/a)\,d\phi^2$ with $a = 1$ km. Find its curvature from the gap law, the length of the ring of ground radius 0.5 km, and compare the excess with the small-ring law.

1. Here $f = a\sinh(\rho/a)$, so $\partial_\rho^2 f = f/a^2$. The gap law $\partial_\rho^2 f = -Kf$ gives $K = -1/a^2 = -1\ \text{km}^{-2}$.
2. The centre is smooth: $f(0) = 0$ and $\partial_\rho f(0) = \cosh 0 = 1$.
3. $C = 2\pi a\sinh(\rho/a) = 2\pi(1\ \text{km})\sinh 0.5 = 3.274$ km.
4. The flat length is $2\pi(0.5\ \text{km}) = 3.142$ km, so the ring is too long by $3.274/3.142 - 1 = 4.22\%$.
5. The small-ring law predicts an excess of $-K\rho^2/6 = (0.5)^2/6 = 4.17\%$; the difference, $0.05\%$, is the next order.

**Answer:** $K = -1\ \text{km}^{-2}$; the ring is 3.274 km long, 4.2% longer than $2\pi\rho = 3.142$ km, close to the 4.17% of the small-ring law.

**Takeaway:** Negative curvature makes rings too long, by the same small-ring law with the sign of $K$ reversed.

## Problems

### `double-the-string-on-earth` · entry · difficulty 1 · estimate

Treat Earth as a smooth ball. A ring drawn with a string pulled tight along the ground for 30 kilometres misses its playground length by about 3.7 millimetres in every kilometre of ring. Roughly how much does a ring drawn with a 60-kilometre string miss, in millimetres per kilometre? What about a 15-kilometre string?

**Hints**

1. How many times longer is the 60-kilometre string?
2. For small rings, doubling the string makes the missing fraction about 4 times as big.

**Answer:** About 15 millimetres in every kilometre of ring for the 60-kilometre string, and a little under 1 millimetre in every kilometre for the 15-kilometre string.

**Must contain:** Twice the string gives about four times the missing fraction; About 15 millimetres in every kilometre of ring for 60 kilometres; Half the string gives about a quarter of the fraction, a little under 1 millimetre in every kilometre

**Numeric:** missing fraction for the 60-kilometre string = 1.48e-05 1 (magnitude, ±5%); missing fraction for the 15-kilometre string = 9.2e-07 1 (magnitude, ±5%)

**Solution**

1. Both strings are tiny compared with Earth, so the rule for small rings applies: doubling the string makes the missing fraction about 2 times 2, or 4 times, as big.
2. The 60-kilometre string is 2 times as long, so its fraction is 2 times 2, which is 4 times as big. Four times 3.7 millimetres in every kilometre is about 15 millimetres in every kilometre.
3. The 15-kilometre string is half as long, so its fraction is a half times a half, which is a quarter as big. A quarter of 3.7 millimetres in every kilometre is a little under 1 millimetre in every kilometre.

### `cosmic-ring-excess` · working · difficulty 2 · calculation

Suppose the curvature density parameter were +0.003, with a Hubble constant of 67.4 km/s/Mpc. By what percentage would a ring of ruler radius 13.9 Gpc around us differ from the flat length, and would it be too long or too short?

**Hints**

1. Find $c/H_0$ in megaparsecs.
2. Use $K = -\Omega_K H_0^2/c^2$ in the small-ring law.

**Answer:** About 0.49% too long, because a positive $\Omega_K$ means negatively curved space.

**Must contain:** H nought ell over c is about 3.1; The ring is about 0.49 percent too long; A positive curvature density parameter means negative curvature

**Numeric:** ring length excess over the flat length = 0.49 percent (signed, ±5%)

**Solution**

1. $c/H_0 = (299\,792\ \text{km/s})/(67.4\ \text{km/s/Mpc}) = 4448$ Mpc.
2. With ruler radius $\ell = 13\,900$ Mpc, $H_0\ell/c = 13\,900\ \text{Mpc}/4448\ \text{Mpc} = 3.125$.
3. The curvature of space is $K = -\Omega_K H_0^2/c^2 = -0.003/(4448\ \text{Mpc})^2$, which is negative.
4. The small-ring law gives $C/2\pi\ell - 1 \approx -K\ell^2/6 = (\Omega_K/6)(H_0\ell/c)^2 = 0.0005 \times 9.77 = 0.0049$.
5. The ring would be 0.49% too long. The next term of $\sinh x/x$ is $x^4/120$ with $x^2 = |K|\ell^2 = 0.029$, about $7\times10^{-6}$, which is negligible.

### `disc-area-and-ring-growth` · formal · difficulty 2 · proof

Starting from $\sqrt G = r - K(p)\,r^3/6 + O(r^4)$ in geodesic polar coordinates, derive the area $A(r)$ of a small geodesic disc and an area form of the curvature limit. Then verify both the area expansion and $L'(r) = 2\pi - \iint_{B_r} K\,dA$ exactly on a sphere of radius $a$.

**Hints**

1. The area element is $\sqrt G\,dr\,d\theta$.
2. On the sphere, $\sqrt G = a\sin(r/a)$.

**Answer:** $A(r) = \pi r^2 - \tfrac{\pi}{12}K(p)\,r^4 + O(r^5)$, so $K(p) = \lim_{r\to0} 12(\pi r^2 - A)/\pi r^4$. On the sphere $A = 2\pi a^2(1 - \cos(r/a))$ and $L' = 2\pi\cos(r/a) = 2\pi - A/a^2$.

**Must contain:** The area is the integral of the circle length over the radius; The quartic term of the area is minus pi over twelve times K r to the fourth; On the sphere the growth rate and the enclosed curvature add to two pi for every radius below pi a

**Solution**

1. $L(r) = \int_0^{2\pi}\sqrt G\,d\theta = 2\pi r - \tfrac{\pi}{3}K(p)\,r^3 + O(r^4)$.
2. The area element is $\sqrt G\,dr\,d\theta$, so $A(r) = \int_0^r L(s)\,ds = \pi r^2 - \tfrac{\pi}{12}K(p)\,r^4 + O(r^5)$.
3. Rearranging, $12(\pi r^2 - A)/\pi r^4 = K(p) + O(r)$, which tends to $K(p)$.
4. On the sphere $\sqrt G = a\sin(r/a)$, so $L = 2\pi a\sin(r/a)$ and $A = \int_0^r L = 2\pi a^2(1 - \cos(r/a))$.
5. With $1 - \cos x = x^2/2 - x^4/24 + \dots$, $A = \pi r^2 - \pi r^4/12a^2 + \dots$, which matches the general expansion with $K = 1/a^2$.
6. $L' = 2\pi\cos(r/a)$, and $\iint_{B_r} K\,dA = A/a^2 = 2\pi(1 - \cos(r/a))$, so $L' = 2\pi - \iint_{B_r} K\,dA$ for every $r < \pi a$, the injectivity radius.

## Observations

- **The curvature of space on the largest scales, inferred from sound-wave patterns in the cosmic microwave background and in galaxy clustering** (measured, working). Each pattern has a calculable size, so its measured angle on the sky compares the length of a ring around us with its ruler radius, as "Rings around us in the universe" explains. Within the standard cosmological model, the combined data fix the curvature density parameter $\Omega_K = -Kc^2/H_0^2$, zero for flat space and positive for negatively curved space. *Numbers:* $\Omega_K = 0.001 \pm 0.002$ from the microwave background combined with baryon acoustic oscillations. With $H_0 = 67.4$ km/s/Mpc, the ring of ruler radius 13.9 Gpc matches the flat length, $2\pi$ times that radius, to $(0.2 \pm 0.3)\%$. *Reference:* N. Aghanim, Y. Akrami, M. Ashdown, J. Aumont and others (2020), *Planck 2018 results. VI. Cosmological parameters*, Astronomy & Astrophysics 641, A6, doi:10.1051/0004-6361/201833910

## Teaching arc

1. **Predict a ring on a ball** (entry). Ask for a prediction about a ring drawn with a tight string on a football, then run the equator count. *Why:* The count turns roundness into a shortfall measured along the surface. *Predict:* On a football, will the ring be longer or shorter than six point two eight times the string? *Visual:* [[paced-ring-on-a-ball-and-a-plain]] *Uses:* `ways_in/draw-a-ring-with-a-string`, `checks/string-ring-on-a-football`
2. **Derive the law and test space** (working). Derive the small-ring law, read a curvature from one ring, then run the test on the universe. *Why:* It turns the test into numbers, including a real measurement of space. *Uses:* `derivations/small-rings-from-the-gap-law`, `checks/curvature-from-one-ring`, `ways_in/rings-around-us-in-the-universe`
3. **Mark the limits** (formal). State the theorem, then show that ring growth reads enclosed curvature and that a slice is not spacetime. *Why:* It stops the test being read as local or independent of slicing. *Uses:* `ways_in/geodesic-circles-theorem-and-limits`, `checks/rings-outside-a-star`, `checks/milne-slices`

## Misconceptions

### “The ring's real radius is its distance through the air to the middle of the ball, so the ring still follows the 6.28 rule.” · entry · `radius-through-the-air`

- **Why it is tempting:** Seen from outside, a ring on a ball is an ordinary circle in the room.
- **What is true:** Someone living on the ball can measure only along its surface. Measured that way, the radius is the string, and the ring falls short of 6.28 times it.
- **Exposed by:** `checks/string-ring-on-a-football`

### “Curvature can only make a ring shorter, never longer.” · entry · `curving-only-shortens`

- **Why it is tempting:** The first curved surface anyone meets is a ball, where rings are short.
- **What is true:** Where straight walkers that start parallel spread apart, as near a swim ring's hole, small rings come out too long.
- **Exposed by:** `checks/a-ring-that-is-too-long`

### “If rings grow by less than two pi per unit of radius, the space where the rings lie must be positively curved.” · formal · `ring-reads-local-ground`

- **Why it is tempting:** For small rings the shortfall does read the curvature at the centre.
- **What is true:** A ring's growth rate is two pi minus the total curvature it encloses, wherever that curvature sits. Outside a star the equatorial plane is negatively curved, and the star's interior supplies the positive total.
- **Exposed by:** `checks/rings-outside-a-star`

### “Rings in space that miss two pi times their radius prove that spacetime is curved.” · formal · `space-rings-show-spacetime-curvature`

- **Why it is tempting:** In a static spacetime the natural slices seem to be the only space there is.
- **What is true:** The ring test measures the curvature of a chosen slice. Flat spacetime has slices with hyperbolic geometry, and curved spacetime can have flat slices.
- **Exposed by:** `checks/milne-slices`

## Checks

1. **Entry · predict** `checks/string-ring-on-a-football`. On a football about 70 centimetres around its middle, you tape one end of a string to a spot. The string is 17.5 centimetres long from the tape to a pen tied at its far end. Keeping the string tight along the ball, you draw a ring. How long is the ring, measured along the ball? A friend says the ring is just a circle seen from outside, so its length must be 6.28 times its radius. Which radius is the friend using, and why doesn't it count for someone living on the ball?
   - **Hints:** What fraction of the way around the ball is 17.5 centimetres?
   - **Answer:** The ring is about 70 centimetres long. Think of the ball as a globe with the taped spot as its North Pole. A line around the ball through both poles is 70 centimetres long, and the equator is halfway from one pole to the other. So the equator is a quarter of the way around the ball from the spot, and a quarter of 70 is 17.5 centimetres. In every direction, then, the pen stops on the equator, and the ring is the equator, 70 centimetres long. On a playground, a 17.5-centimetre string would draw about 110 centimetres. The friend's radius runs through the air, from the equator to the middle of the ball. The equator is an ordinary circle in the room, 70 centimetres around, so that radius is 70 divided by 6.28, about 11.1 centimetres. But someone living on the ball can measure only along its surface, and can never reach the middle of the ball. Measured along the surface, the radius is the string, 17.5 centimetres, so the ring is short of its playground length by more than a third.
   - **Must contain:** The ring is the equator, about 70 centimetres long; On a playground it would be about 110 centimetres; The friend's radius runs through the air, which someone living on the ball cannot measure
   - **Numeric:** ring length = 70 cm (magnitude, ±5%)
   - **Targets:** `radius-through-the-air`
   - **Visual:** [[paced-ring-on-a-ball-and-a-plain]]
2. **Entry · choice** `checks/a-ring-that-is-too-long`. An ant living on a surface with no sharp points walks straight 2 centimetres from a centre in every direction, and draws a small ring through the places where it stops. Measured along the surface, the ring is 12.9 centimetres long. Is the surface around the centre like a ball, like a playground, or like a swim ring near its hole? Explain.
   - **Hints:** What is the ring's playground length?
   - **Answer:** Like a swim ring near its hole. The ring's playground length is 6.28 times 2, about 12.6 centimetres. On a playground the ring would have exactly that length, and on a ball it would be shorter. This ring is longer, so the places where neighbouring walks stop are farther apart than on a playground. The walks spread apart that fast only where the surface spreads straight walkers apart. Straight walkers that start parallel spread apart where the curvature is negative, as near a swim ring's hole.
   - **Must contain:** The ring's playground length is about 12.6 centimetres; The ring is too long; Too long means negative curvature, as near a swim ring's hole
   - **Targets:** `curving-only-shortens`
3. **Working · numeric** `checks/curvature-from-one-ring`. Surveyors on a smooth surface measure a ring of ground radius 2.000 km and find its length along the ground to be 12.6503 km. Estimate the Gaussian curvature at the centre, with its sign, and the radius of curvature, one over the square root of the curvature's size.
   - **Hints:** Compare the measured length with $2\pi\rho$ before using the small-ring law.
   - **Answer:** The flat length is $2\pi \times 2.000$ km $= 12.5664$ km, so the shortfall $2\pi\rho - C = -0.0839$ km: the ring is too long. The small-ring law gives $K \approx 3(2\pi\rho - C)/\pi\rho^3 = 3(-0.0839)/(8\pi)\ \text{km}^{-2} = -0.0100\ \text{km}^{-2} = -1.00\times10^{-8}\ \text{m}^{-2}$. The radius of curvature is about 10.0 km. The sign is negative because the ring is too long.
   - **Must contain:** The ring is longer than the flat length, so the curvature is negative; K is about minus 0.0100 per square kilometre; The radius of curvature is about 10 kilometres
   - **Numeric:** Gaussian curvature = -1e-08 m^-2 (signed, ±3%); radius of curvature = 10 km (magnitude, ±3%)
4. **Formal · evaluate-claim** `checks/rings-outside-a-star`. Take the equatorial plane of space outside a static spherical star with a regular interior, using the course Schwarzschild metric at constant time. Rings in this plane grow by less than two pi per unit of ruler distance. A student concludes that the plane is positively curved outside the star. Evaluate the claim.
   - **Hints:** For $ds^2 = d\rho^2 + f^2\,d\phi^2$, $K = -\partial_\rho^2 f/f$. / Which region does $L' = 2\pi - \iint K\,dA$ integrate over?
   - **Answer:** The claim is wrong. With $G = c = 1$ the plane has $ds^2 = dr^2/(1 - 2M/r) + r^2\,d\phi^2$, so $f = r$ and $d\rho = dr/\sqrt{1 - 2M/r}$. Then $\partial_\rho f = \sqrt{1 - 2M/r} < 1$, so rings do grow more slowly than $2\pi$. But $\partial_\rho^2 f = M/r^2$, so $K = -\partial_\rho^2 f/f = -M/r^3 < 0$ outside the star. The growth rate reads the total enclosed curvature: $L' = 2\pi - \iint_B K\,dA$ gives $\iint_B K\,dA = 2\pi(1 - \sqrt{1 - 2M/r}) > 0$. The exterior between the star's radius $R_\star$ and $r$ contributes $-2\pi(\sqrt{1 - 2M/r} - \sqrt{1 - 2M/R_\star})$, so the interior holds the positive total $2\pi(1 - \sqrt{1 - 2M/R_\star})$; a uniform-density interior has $K = 2M/R_\star^3$. For the Sun that total is about $2\pi GM/R_\star c^2 = 1.33\times10^{-5}$ rad.
   - **Must contain:** Outside the star the plane's curvature is minus M over r cubed, negative; Ring growth measures the total curvature enclosed, not the curvature where the ring lies; The star's interior supplies a positive total that outweighs the negative exterior
   - **Targets:** `ring-reads-local-ground`
5. **Formal · explain** `checks/milne-slices`. In flat spacetime, take the events that lie a fixed proper time after one event, measured along inertial worldlines through that event. Rings in this slice of space come out too long. Does this show that spacetime is curved? What does it show?
   - **Hints:** Compute the ring length in the slice, then ask which object it describes.
   - **Answer:** No. With $c = 1$, the slice at proper time $\tau$ has metric $\tau^2(d\chi^2 + \sinh^2\chi\,d\Omega^2)$, while Minkowski spacetime has vanishing Riemann tensor. A ring of ruler radius $\rho = \tau\chi$ in the slice has $L = 2\pi\tau\sinh(\rho/\tau) > 2\pi\rho$, so the slice is a hyperbolic space with $K = -1/\tau^2$: the ring test measures the slice's intrinsic curvature. The slice is a curved hypersurface with extrinsic curvature $\kappa_{ij} = h_{ij}/\tau$ and trace $\kappa = 3/\tau$. For a spacelike slice of flat spacetime the Gauss equation reads ${}^{(3)}\mathcal R = \kappa_{ij}\kappa^{ij} - \kappa^2 = 3/\tau^2 - 9/\tau^2 = -6/\tau^2$, the scalar curvature of that hyperbolic space. The slices $t = \text{const}$ of inertial coordinates in the same spacetime give rings of exactly $2\pi\rho$.
   - **Must contain:** Spacetime is flat, so the long rings do not show spacetime curvature; The ring test measures the intrinsic curvature of the chosen slice, here minus one over tau squared; The Gauss equation links the slice's curvature to its extrinsic curvature
   - **Targets:** `space-rings-show-spacetime-curvature`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Radial coordinates defined by ring length | In the course Schwarzschild and FLRW metrics, rings at coordinate $r$ have length $2\pi r$ or $2\pi a(t)\,r$; ruler radii come from the $dr^2$ term. | Some texts call $r$ the radius outright. In any form, $C = 2\pi r$ alone says nothing about flatness. |

## Visuals

- ★ [[paced-ring-on-a-ball-and-a-plain]] (flagship): Flagship: rings drawn out from a centre on a ball, flat ground, a paper tube and a saddle, with the missing fraction read out. *Sketch:* Adds a saddle and a plot of the missing fraction against string length squared, a line of slope $K/6$ near zero. A string longer than half the tube's circumference splits its ring into two loops. On the ball, flat ground and the tube a tight string draws the ring; on the saddle the ring must be drawn by straight walks of equal length, because a taut string lifts off a surface of negative curvature instead of lying along it.

## Tutor moves

**Open with**

- Picture a football, the round kind used in soccer. You tape a short string to one spot, keep it tight along the ball, and draw a ring with its far end. On a playground, a ring is about six point two eight times its string. On the ball, measured along the ball, will the ring be longer, shorter, or the same? *(prediction)*

**If the learner is stuck**

- *The learner measures the ring's radius through the air or through the ball.* → Put a finger on the string and ask what someone living on the ball could lay a tape along. *Uses:* `checks/string-ring-on-a-football`

**Common questions**

- *Can the ring test be done in space, not just on a surface?* (entry) Yes. Imagine rulers of the same length laid out from a centre in space, pointing every way around inside one thin slab, like the hands of a clock pointing around its face. Then measure the ring through the rulers' far ends. Astronomers run a version of this test on the whole universe, using patterns of known size on the sky. So far those rings match their playground length to within about one percent. *Uses:* `ways_in/rings-around-us-in-the-universe`, `observations/flatness-of-space-from-sound-patterns`

**Switching levels**

- To working when: asks for a formula for the ring's length. Derive the small-ring law, then read a curvature from one measured ring. *Uses:* `derivations/small-rings-from-the-gap-law`, `checks/curvature-from-one-ring`

**Pronunciations:** Bertrand → bair-TRAHN; Diguet → dee-GAY; Puiseux → pwee-ZUH; Painlevé–Gullstrand → pan-luh-VAY GULL-strand; Planck → PLAHNK

## History

- **Carl Friedrich Gauss (1827).** Built coordinates from geodesics leaving one point, proved that they cross the geodesic circles at right angles, and showed that curvature depends only on lengths measured along the surface. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Joseph Bertrand, Charles François Diguet, Victor Puiseux (1848).** Proved, in three short notes in one 1848 journal volume, that the shortfall of small geodesic circles, and of the areas they bound, gives the Gaussian curvature at their centre. Joseph Bertrand, Charles François Diguet, Victor Puiseux (1848), *Démonstration d'un théorème de Gauss*, Journal de mathématiques pures et appliquées 13, 80–90

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** You push a peg into a playground, tie a string to it and swing chalk round: the circle you draw is 6.28 times the string. Do the same on a football with a 17.5-centimetre string and you get the equator, 70 centimetres, where flat ground would give 110, so the ball is curved. That comparison is the ring test, and 6.28 times the string is the playground length. A paper tube looks bent, but its rings come out normal, because you can unroll it without stretching anything. Near a swim ring's hole rings come out too long. Short means positive curvature, normal means zero, too long means negative. Doubling the string makes the missing fraction about four times bigger, and on Earth a 30-kilometre string misses by only 70 centimetres, under 4 millimetres in every kilometre. Three things stopped me. I could not follow why a tight string cannot steer: it said pulling makes the string shorter, and a string's length cannot change. I could not tell which circle on the swim ring the inner circle is; I pictured a loop round the tube. And instead of a tube I rolled the paper into a cone and drew a ring round the tip: it came out short, yet the paper is flat, so 'short means positive curvature' looked wrong to me. I also wondered why the problem says 3.7 parts in a million when the page had just said about 4 millimetres in every kilometre.

**Stumbles (12)**

- “A line drawn around the ball through both poles goes once around its middle, so that line is 70 centimetres long.”: Step taken on trust. The 70 centimetres was given for the ball's middle, and nothing says why a line through the poles is the same length, so I reread to check whether the two lines were the same one.
- “If the string steered anywhere, pulling on it would slide that bend sideways and make the string shorter. A tight string cannot get any shorter, so it never steers.”: 'Shorter' does double duty: a shorter route and a shorter piece of string. A string's length cannot change, so the reason reads as false and the argument is lost.
- “the circle around the swim ring's surface that runs closest to the hole”: I first pictured a loop that goes around the tube, not around the hole. The prerequisite picture names it as the circle that runs all the way around the hole.
- “A small ring therefore tells you the curvature around its centre. A short ring means positive curvature.”: False first what-if. The way has just had me roll paper into a tube; rolling it into a cone instead and drawing a ring round the tip gives a short ring, yet straight walkers that start parallel on that paper keep their gap, so the reader's own curvature test calls the paper flat.
- “Two straight walkers start parallel when they stand side by side, both facing the same way at a right angle to the line between them.”: On a curved surface 'the line between them' is not defined, and it is a second wording for the prerequisite's 'on a straight line, facing the same way at a right angle to it'.
- “An ant living on a smooth surface walks straight 2 centimetres from a centre in every direction”: 'Smooth' is an undefined word at this rung. I read it as 'not rough', which is not the hypothesis the check needs; the hypothesis is that the centre is not a sharp point.
- “This ring is longer, so the gaps between neighbouring points on it are wider than on a playground. The places where the walks stop spread apart that fast only where the surface spreads straight walkers apart.”: Two wordings for one idea in consecutive sentences, and 'neighbouring points on it' sounds like any two points of the drawn ring rather than the places where neighbouring walks stop.
- “The length a ring is missing, compared with its playground length, divided by that playground length.”: Reread: 'compared with its playground length' and 'divided by that playground length' name the same step twice, so I could not tell which number goes on top.
- “The length a ring drawn with a tight string would have on flat ground: 2 times pi times the string, about 6.28 times the string.”: The entry check draws its ring by walking, not with a string, and its answer still uses the playground length. The definition covers only string-drawn rings.
- “misses its playground length by about 3.7 parts in a million”: The way I had just read gives the same Earth ring as 'less than 4 millimetres in every kilometre of ring'. Two units for one number, so I stopped to check whether the problem meant a different ring.
- “Imagine rulers of one length laid out from a centre in space, in many directions all around within one thin slab of space, and measure the ring through their far ends.”: Reread: 'in many directions all around within one thin slab of space' gives nothing to picture, and 'their' could be the directions or the rulers.
- “So far those rings match their flat-space length to within about one percent.”: 'Flat-space length' is a second name for the playground length, the term this note defines and uses everywhere else.

**Fixes**

- Summary: 'Away from sharp points' scopes the general sentence, so a reader who tries a paper cone is not misled. To stay inside the 500-character cap, 'flat playground' became 'playground', the note's own flat reference, and the swim-ring clause was joined with a semicolon; no content was dropped.
- Draw a ring with a string: a ball measures the same all the way around, so the line through both poles is also 70 centimetres.
- Too short, just right, too long: the tight string's reason now says that a bend could be slid sideways to shorten the path, leaving the string slack, instead of saying the string gets shorter; the inner circle is named as the circle that runs all the way around the hole, matching the curvature note; the reading of a small ring is scoped to a centre that is not a sharp point like a cone's tip; the recap's 'start parallel' now matches the prerequisite word for word; the takeaway carries the same scope.
- Double the string: dropped 'Near the centre, neighbouring strings fan apart just as on a playground.', which repeats a sentence of 'Too short, just right, too long' word for word, and gave the next sentence its noun ('The ball draws neighbouring strings together'). This is the cut that pays for the sharp-point scope inside the 1,100-word entry allowance.
- Glossary: playground length now covers a ring drawn by walking as well as by string, because the entry check walks; missing fraction says which length is divided by which; start parallel matches the curvature note word for word.
- Entry check a-ring-that-is-too-long: 'a smooth surface' became 'a surface with no sharp points', the same plain scope the ways now use; the answer keeps one wording for the places where neighbouring walks stop.
- Entry problem double-the-string-on-earth: Earth's shortfall is now in millimetres in every kilometre of ring, the unit the way uses, in the statement, answer, key points and solution. The numeric answers are unchanged fractions, 1.48 in a hundred thousand and 9.2 in ten million.
- Tutor common question: the rulers now point every way around inside one thin slab, like the hands of a clock around its face, and the rings are matched against their playground length, not a second term.
- Budget: entry way explanations went from 1,088 to 1,097 words, inside the 1,100 review allowance, all for the stumbles recorded here; nothing else was dropped or compressed.
- Bumped the revision to 5 and set the status back to novice-reviewed, because the physics stage signed revision 4.

**Concerns**

- This record replaces an earlier novice record of 2026-09-13 at revision 4 (verdict fixed, 22 stumbles, one re-read), which the schema has no room to keep alongside a new one. That note is untracked in git, so the superseded file was copied to knowledge snapshots as circumference-to-radius-test.before-novice2.json in the pipeline's scratchpad before any edit.
- The physics stage signed revision 4. The 18 learner-visible strings changed here are all at the entry rung and change no number, but they need a physics diff check before an editor publishes; the sharp-point scope and the wording that a taut string's path could be shortened are the two that make new claims.
- Three entry parts now sit at their ceilings: entry way explanations at 1,097 of the 1,100 review allowance, the summary at 499 of 500 characters, and the takeaway of 'Too short, just right, too long' at exactly 240 characters. Any later entry addition needs a matching cut.
- The entry rung now names a cone's tip as the exception but does not say what happens there. Saying that every ring around the tip is short although the paper is flat would take about a dozen more entry words, which the budget does not have; a reader who asks is answered by the working way's cone.
- The summary runs to five sentences against the guide's two or three. I did not compress it, because compressing entry sentences is forbidden; an editor who wants it shorter should drop content and say so.
- The glossary's 'flat' ends 'as on a playground' while the curvature note's ends 'as on a can's label'. Both are true and each fits its own note's setting, so I left this note's wording; an editor may want one example across the network. The superseded record's claim that the curvature definitions match word for word was true of the other four entries, not of this one.
- Entry check a-ring-that-is-too-long still fits a small swim ring (a radius of curvature near 5 centimetres), not the 70-centimetre swim ring of the curvature note. The check names no size, so it is not wrong; the physics stage already recorded it.
- Still open from earlier stages: the conventions file fixes no row for the curvature density parameter or for which factor carries length in the cosmological line element, and the flagship visual paced-ring-on-a-ball-and-a-plain has no catalog entry.

**Re-read** (2026-09-13, revision 7): 1 stumbles in 6 changed passages

- “give the curvature density parameter $\Omega_K = -Kc^2/H_0^2$, which is positive for negatively curved space, where $H_0$ is the Hubble constant, today's expansion rate.”: Two new things at once. The sentence introduces $\Omega_K$, then makes a sign claim about it, and only afterwards says what $H_0$ is, so I had to hold an undefined symbol from the formula while working out which way the sign goes, then go back. The sign claim and the symbol gloss are also both attached by commas to the same formula, so on first reading I could not tell which of $\Omega_K$ and $H_0$ the clause 'which is positive' belonged to.
- Fix: Working way rings-around-us-in-the-universe: split the $\Omega_K$ sentence so the gloss of $H_0$ follows the formula directly and the sign claim stands as its own sentence naming $\Omega_K$. Same claim, same sign, same condition; one word added, and working way explanations stay far inside their 1,000-word cap.
- Fix: Read the four name changes (alias Bertrand-Diguet-Puiseux theorem, pronunciation Diguet / dee-GAY, history work title Demonstration d'un theoreme de Gauss) and left them: they are proper names and a citation title, nothing a beginner is asked to follow, and the respelling dee-GAY reads with a hard g in English, which is what the French name needs.
- Fix: No entry prose, takeaway, summary, check or number changed at this stage, so every entry rewrite of the novice review stands untouched.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- Entry football count: a 17.5 cm string on a ball 70 cm around draws the equator, 70 cm; playground length about 110 cm; short by more than a third; a line through both poles is also 70 cm.: python: a = 70/2pi = 11.1408 cm; the equator sits a quarter of the way around, pi a/2 = 17.50 cm; C = 2 pi a sin(rho/a); flat = 2 pi rho. Sphere symmetry gives every great circle the same length. → C = 70.000 cm, flat = 109.956 cm, shortfall 0.3634 of the flat length. Every step correct.
- Entry try_it and 'Double the string': 10 cm string gives about 55 cm (flat about 63 cm, missing about 13 parts in 100); 5 cm gives about 30.4 cm (flat 31.4, about 3 parts in 100); doubling multiplies the missing fraction by about four.: python, exact C = 2 pi a sin(rho/a) with a = 11.1408 cm. → 54.728 and 30.372 cm; missing 8.104 cm (0.1290) and 1.044 cm (0.0332); ratio 3.88. All 'about' statements correct.
- Entry Earth numbers: 40 000 km around, a 30 km string draws a ring about 188 km long that misses its playground length by about 70 cm, less than 4 mm in every kilometre.: python with a = 40000/2pi = 6366.198 km and the exact sine. → C = 188.4949 km, flat = 188.4956 km, shortfall 0.6976 m, fraction 3.701e-6, i.e. 3.70 mm per km. Correct.
- Entry problem double-the-string-on-earth: 3.7 mm per km at 30 km gives about 15 mm per km at 60 km and a little under 1 mm per km at 15 km; numeric fields 1.48e-5 and 9.2e-7 with 5% relative tolerance.: python, exact sine and the small-ring fraction rho^2/6a^2. → 14.804 mm/km (1.4804e-5) and 0.925 mm/km (9.253e-7). Both numeric fields are inside 5%; the four-times rule is exact to better than 0.01% at these sizes. Correct.
- Entry paper tube: 30 cm around, a 5 cm string draws a ring 31.4 cm long, its playground length; keep the string under 15 cm.: Unrolling is an isometry, so the ring is a plane circle of radius 5 cm, length 2 pi (5) = 31.416 cm. Injectivity radius of a flat cylinder is half its circumference. → Correct, and the 15 cm bound is exactly the injectivity radius.
- Novice rewrite, entry: 'If its path steered anywhere, sliding that bend sideways would shorten the path between its ends, and the string would go slack. So a tight string never steers.': First variation of arc length for a curve on a surface under a normal variation phi n: delta L = -integral k_g phi ds with fixed ends. Choosing phi with the sign of k_g makes delta L negative. → Correct, and a genuine improvement: the old wording said the string itself got shorter. A curve with non-zero geodesic curvature can always be shortened by displacing it toward its concave side, so a string held taut on the surface has k_g = 0, a geodesic. The conclusion stays true where a taut string leaves the surface, because the sentence speaks only of a string lying along the surface, and the way handles the lift-off case separately.
- Novice rewrite, entry scope: 'A small ring therefore tells you the curvature around its centre, as long as that centre is not a sharp point like a cone's tip', with the same scope in the takeaway, the summary ('Away from sharp points') and the check ('a surface with no sharp points').: Checked the scope against the cone (f = (1 - delta/2pi) rho, so L = (2pi - delta) r is short for a flat cone), against a smooth centre whose small disc contains a distant cone tip (tips are isolated, so a small enough ring excludes them), against a crease (intrinsically flat, and the test correctly reads zero there, so the scope does not wrongly exclude it), and against the small-ring law itself. → Correct and sufficient at this rung. Around a smooth centre, C = 2 pi rho (1 - K rho^2/6) + O(rho^4), so short, exact and long read K positive, zero and negative for small enough rings; the only entry-reachable failure is the sharp point, which the new clause names. 'Sharp point' is the right exclusion in plain words: a crease is a sharp line, not a point, and the test still works across it.
- Novice rewrite, entry: the swim ring's centre is 'on its inner circle, the circle that runs all the way around the hole, closest to it'.: Torus with tube radius r and centre-circle radius R: K = cos(theta)/(r(R + r cos theta)), so K = -1/(r(R - r)) on the inner circle. python for the curvature note's swim ring, r = 10 cm, R = 25 cm. → K = -1/150 cm^-2 there, negative, so small rings centred on that circle are too long. The named circle is the one the curvature note names, and the geometry is right.
- Working small-ring law C(rho) = 2 pi rho - (pi/3) K(p) rho^3 + O(rho^4), the limit K(p) = lim 3(2 pi rho - C)/(pi rho^3), the missing fraction K rho^2/6, and derivation steps 1-10.: Hand: geodesic polar form ds^2 = d rho^2 + f^2 d phi^2, Jacobi equation f'' = -K f with f(0) = 0 and f'(0) = 1, so f''(0) = 0 and f'''(0) = -K(p); Taylor; integrate over phi. Sphere check f = a sin(rho/a). → Every step correct. Signs match the conventions sectional-curvature row: a sphere has K = +1/a^2 and short rings; f = a sinh(rho/a) gives K = -1/a^2 and long rings at every radius. The stated error O(rho^4) is a valid bound; the phi average of the rho^4 term vanishes, so the true error is O(rho^5).
- Working football numbers: a = 70 cm/2pi = 11.14 cm and the 10 cm ring has rho^2/6a^2 = 13.4% against the exact 12.9%.: python. → 13.43% and 12.90%. Correct, and the gap is the next order.
- Working cone hypothesis: f = (1 - delta/2pi) rho around a paper cone's tip, so the derivative is not 1 there; and the tube fails for strings longer than half its circumference.: Hand: a cone of deficit delta is flat with total angle 2pi - delta at the tip. Injectivity radius of a flat cylinder. → Correct.
- Worked example: ds^2 = d rho^2 + a^2 sinh^2(rho/a) d phi^2 with a = 1 km gives K = -1 km^-2; the ring at rho = 0.5 km is 3.274 km, 4.22% longer than 3.142 km, against 4.17% from the small-ring law.: python: 2 pi sinh(0.5), 2 pi (0.5), and rho^2/6a^2. → 3.27414 km, excess 4.2191%, law 4.1667%, difference 0.052%. Correct, including the sign statement.
- Working check curvature-from-one-ring: a ring of ground radius 2.000 km measuring 12.6503 km gives K = -0.0100 km^-2 = -1.00e-8 m^-2 and a radius of curvature of 10.0 km.: python: 2 pi rho = 12.56637 km, K = 3(2 pi rho - C)/(pi rho^3); checked the data against the exact surface 2 pi (10 km) sinh(0.2). → K = -1.0018e-8 m^-2, radius 9.991 km; the datum is exactly the ring of a K = -1/(10 km)^2 surface, so the 3% tolerances hold and the sign convention is right.
- Entry check a-ring-that-is-too-long: a 2 cm walk in every direction giving a 12.9 cm ring means negative curvature, 'like a swim ring near its hole'; playground length about 12.6 cm.: python: flat 12.5664 cm, excess 2.655%, implied K = -6 (excess)/rho^2 = -0.0398 cm^-2, radius of curvature 5.01 cm; compared with tori of several sizes. → Internally correct and realizable: a torus with r (R - r) = 25 cm^2, for instance a tube 5 cm thick around a hole, gives exactly this. It is not the curvature note's swim ring (r = 10 cm, R = 25 cm), where a 2 cm ring is 12.62 cm. The check names no size, so nothing is wrong; recorded as a concern.
- Formal theorem: for 0 < r < inj(p), S_r(p) is a smooth closed curve equal to the distance circle; Gauss lemma g = dr^2 + G d theta^2; L(r) = 2 pi r - (pi/3) K r^3 + O(r^4); A(r) = pi r^2 - (pi/12) K r^4 + O(r^5).: Hand: Jacobi field norm sqrt G with sqrt G(0) = 0 and derivative 1, d_r^2 sqrt G = -K sqrt G, integrate over theta then over r. Cross-checked against the published statement of the theorem. → Correct, and the published limits, 3(2 pi r - C)/(pi r^3) and 12(pi r^2 - A)/(pi r^4), agree with the note's. One precision gap fixed: J'(0) must also be perpendicular to the radial geodesic, otherwise J(0) = 0 with |J'(0)| = 1 does not pick out the angular Jacobi field.
- Formal: k_g = d_r sqrt G / sqrt G and L'(r) = 2 pi - double integral of K over B_r(p).: Hand: the closed integral of k_g ds over theta is the integral of d_r sqrt G d theta = L'(r); local Gauss-Bonnet for a disc (Euler characteristic 1) with the disc on the walker's left. Plane check k_g = 1/r. → Correct, with the sign convention of the conventions orientation row.
- Formal cylinder limit: beyond inj(p) the points at distance r > l_c/2 on a flat cylinder form two loops of total length 2r (pi - 2 arccos(l_c/2r)) < 2 pi r.: Universal cover: distance from p is the plane distance inside the strip |x| <= l_c/2, so the set is the plane circle cut by |cos theta| <= l_c/2r, giving two arcs of angular width pi - 2 arccos(l_c/2r); each arc closes on the cylinder because x = l_c/2 and x = -l_c/2 are the same. python at l_c = 30 cm, r = 20 cm. → 67.84 cm against a flat 125.66 cm. Formula, count of loops and inequality all correct; this is a flat surface whose large distance circles are short, so the entry inference is rightly restricted to small rings.
- Formal n-dimensional statements: the circle swept by geodesics tangent to a 2-plane sigma has L = 2 pi r (1 - K(sigma) r^2/6 + ...), and a geodesic sphere has (n-1)-volume proportional to r^(n-1)(1 - R(p) r^2/6n + ...).: Hand: d(exp_p)_{r v} (r w) is the Jacobi field with J(0) = 0 and J'(0) = w, so |J|(r) = r - K(v,w) r^3/6 + ...; K(v,w) = K(sigma) for an orthonormal pair spanning sigma. Checked the sphere-volume coefficient on S^n of radius a, where R = n(n-1)/a^2, and at n = 2 against 1 - K r^2/6. → Both correct, including the factor 6n.
- Formal check rings-outside-a-star: K = -M/r^3 in the equatorial plane; growth rate 2 pi sqrt(1 - 2M/r); the exterior annulus contributes a negative total; the interior holds 2 pi (1 - sqrt(1 - 2M/R_star)); a uniform interior has K = 2M/R_star^3; for the Sun the total is about 1.33e-5.: Hand with G = c = 1: f = r, d rho = dr/sqrt(1 - 2M/r), so d_rho f = sqrt(1 - 2M/r), d_rho^2 f = M/r^2 and K = -d_rho^2 f/f. The uniform interior slice is a spherical cap of radius squared R_star^3/2M, whose total curvature out to the surface is 2 pi (1 - cos chi) with sin chi = sqrt(2M/R_star). python for the Sun with GM/c^2 = 1477 m and R = 6.957e8 m. → All correct. The cap's total, 2 pi (1 - sqrt(1 - 2M/R_star)), matches the value forced by the exterior growth rate exactly, which is a real consistency check on the whole argument. Sun: 2 pi GM/(R c^2) = 1.334e-5, matching the quoted 1.33e-5.
- Formal check milne-slices: the slice at proper time tau is hyperbolic with K = -1/tau^2; extrinsic curvature h_ij/tau with trace 3/tau; the Gauss equation gives a scalar curvature -6/tau^2; inertial t = const slices give exactly 2 pi rho.: Hand: the hyperboloid in Minkowski spacetime has induced metric tau^2 (d chi^2 + sinh^2 chi d Omega^2); ring length 2 pi tau sinh(rho/tau) > 2 pi rho; unit normal x^mu/tau gives K_ij = h_ij/tau; the Hamiltonian constraint for a spacelike slice of flat spacetime is 3R = K_ij K^ij - K^2. Hyperbolic 3-space of curvature K has R = 6K. → 3/tau^2 - 9/tau^2 = -6/tau^2 = 6(-1/tau^2). Correct and mutually consistent. Painleve-Gullstrand slices of Schwarzschild are exactly flat Euclidean 3-space: correct.
- Working FLRW ring test: C = 2 pi a r, ruler radius (a/sqrt k) arcsin(sqrt k r), so C = 2 pi (a/sqrt k) sin(sqrt k l/a) with K = k/a^2; the angle is 2 pi L/C; short rings make a pattern look larger; Omega_K = -K c^2/H_0^2 is positive for negatively curved space.: Hand from the course FLRW metric; in geodesic polar form the angle at the centre subtended by an arc of length L on the ring of circumference C is 2 pi L/C. → Correct, and K = k/a^2 holds whichever of a and k is given length units. The sign statement was ambiguous as written ('where H_0 is the Hubble constant, today's expansion rate, which is positive for negatively curved space' reads as a claim about H_0); reordered so the clause sits on Omega_K. The conventions file still fixes no row for Omega_K or for the units of a and k; recorded as a concern.
- Cosmic numbers: l = 13.9 Gpc = 4.3e26 m = about 45 billion light-years; H_0 = 67.4 km/s/Mpc = 2.18e-18 s^-1; H_0 l/c = 3.12; the ring matches 2 pi l to (0.2 +- 0.3)%.: python with 1 Mpc = 3.0857e22 m and 1 ly = 9.4607e15 m. → 4.289e26 m, 45.3 billion ly, 2.184e-18 s^-1, H_0 l/c = 3.125, and (Omega_K/6)(H_0 l/c)^2 = 0.163% +- 0.326%. Correct; the quoted comoving distance to last scattering matches the concordance value.
- Working problem cosmic-ring-excess: Omega_K = +0.003 and H_0 = 67.4 km/s/Mpc give a ring of ruler radius 13.9 Gpc about 0.49% too long, with a next term of about 7e-6.: python: c/H_0 = 4448 Mpc, H_0 l/c = 3.125, (Omega_K/6) x^2; next term of sinh(x)/x is x^4/120 with x^2 = |K| l^2 = Omega_K x^2. → c/H_0 = 4447.96 Mpc, excess 0.4883%, x^2 = 0.02930, x^4/120 = 7.15e-6. Correct, and the sign (too long for positive Omega_K, that is negative K) matches the note's convention.
- Formal problem disc-area-and-ring-growth: A(r) = pi r^2 - (pi/12) K r^4 + O(r^5), K(p) = lim 12(pi r^2 - A)/(pi r^4); on a sphere A = 2 pi a^2 (1 - cos(r/a)), L' = 2 pi cos(r/a) = 2 pi - A/a^2 for r < pi a.: Hand integration and series; checked the sphere identity term by term. → All correct, including the injectivity radius pi a. The area limit agrees with the published form of the theorem.
- Observation: Omega_K = 0.001 +- 0.002 from the microwave background combined with baryon acoustic oscillations, with the Planck 2018 cosmological-parameters paper as reference.: Web check of the published paper: authors, year, journal, article number, DOI and arXiv id. → Confirmed: Aghanim, Akrami, Ashdown, Aumont and others, 2020, Astronomy & Astrophysics 641, A6, doi 10.1051/0004-6361/201833910, arXiv 1807.06209, with Omega_K = 0.001 +- 0.002. Kept verified.
- History: Gauss 1827/1828, Disquisitiones generales circa superficies curvas, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99-146; geodesic polar coordinates, their orthogonality to geodesic circles, and curvature from lengths measured along the surface.: Bibliographic records; the work was presented to the Royal Society of Gottingen on 8 October 1827 and published in 1828. → Confirmed; the split between the history year 1827 and the work year 1828 is right, and the scope of the contribution matches the memoir. No DOI exists. Kept verified.
- History: the 1848 theorem and the spelling of its second author.: Checked the encyclopedia entry for the theorem, the journal's own table of contents for volume 13, and a biographical record of the author. → The name is Diguet, not Diquet: Charles Francois Diguet (1822-1897), whose note giving the area form pi s^2 - pi s^4/(12 R_1 R_2) appears at page 83 of Journal de mathematiques pures et appliquees 13 (1848); Bertrand's note starts at page 80 and the three notes run to page 90. The theorem is conventionally named Bertrand-Diguet-Puiseux. The previous physics record had this backwards. Corrected everywhere in this note, including the alias, the objective, the theorem name in the formal way, the pronunciation and the reference, which now carries all three authors, the title 'Demonstration d'un theoreme de Gauss' and pages 80-90. Diguet's quoted area coefficient is an independent confirmation of the note's A(r) = pi r^2 - (pi/12) K r^4.
- Entry, working and formal sign statements are one consistent set: short means positive curvature, long means negative.: Compared the summary, both entry takeaways, the glossary, the too-long check, the small-ring law, the worked example and the formal theorem against the conventions sectional-curvature row and the curvature note's definitions. → Consistent everywhere, with the sphere at K = +1/a^2 and the swim ring's inner circle negative.
- Structure: prerequisites direct and acyclic; assumes within the prerequisite closure; the formal rung carries two formal checks and one formal problem; every check and problem evidences an objective; visual ids exist or are proposed with a sketch; nothing names a source book.: Read the registry entries for curvature and line-element; checked that 'geodesic' is a prerequisite of curvature; ran the validator. → All hold. The prerequisites curvature and line-element do not lead back to this note; the formal way's assumes 'geodesic' is a prerequisite of curvature; checks rings-outside-a-star and milne-slices are the two formal checks and disc-and-ring-growth the formal problem; the one visual is proposed with a sketch; the validator reports no source overlap.

**Counterexamples tried**

- Cone tip, entry rung: a ring round a paper cone's tip has length (2 pi - delta) r, short although the paper is flat, so 'a short ring means positive curvature' fails there. The novice reviewer's clause 'as long as that centre is not a sharp point like a cone's tip', repeated in the takeaway, the summary and the check, scopes every entry statement correctly. Checked and kept.
- Cone tip enclosed but not at the centre: a smooth centre with the tip inside the disc gives a short ring on a flat surface. Cone tips are isolated, so a small enough ring around a smooth centre excludes them; the entry rung's 'small ring' and the formal L'(r) = 2 pi - enclosed curvature cover this.
- Crease in paper: a sharp line, not a sharp point, and the surface is intrinsically flat there, so the ring test correctly reads zero. The new scope does not wrongly exclude it.
- Bent but flat surface: the paper tube. Rings are exactly their playground length while the string stays under half the circumference, which the entry way states.
- Beyond the injectivity radius: on a flat cylinder the points at distance r > l_c/2 form two loops of total length 2r (pi - 2 arccos(l_c/2r)) < 2 pi r, so a flat surface gives short rings. The entry way caps the string at half the tube's circumference, the working way names the hypothesis and the formal way gives the formula.
- Great circle as the ring: the exact C = 2 pi a sin(rho/a) covers rho = pi a/2, which is the entry count; beyond it rings keep shrinking, so 'short' still reads positive curvature all the way to the far pole.
- Region larger than half a closed surface: on a sphere every ring out to the antipode is short, so no entry sentence breaks.
- Taut string on a negatively curved surface: a string pulled tight from a centre on a swim ring's inner circle lifts off and cuts across the hole, so that ring is drawn by walking straight instead. The entry way says this, and the visual sketch carries the same instruction.
- Mixed curvature inside one ring: a finite ring can have exactly its playground length while enclosing both signs, because L'(r) = 2 pi minus the enclosed total. The entry rung reads only small rings and their centre; check rings-outside-a-star makes the general case explicit, where the plane outside a star is negatively curved although rings grow more slowly than 2 pi.
- Centre where K = 0 on a swim ring (the top of the tube): the third-order shortfall vanishes, matching 'a ring of its playground length means zero curvature' at the centre.
- Different slicing: Milne slices of flat spacetime have long rings and Painleve-Gullstrand slices of Schwarzschild spacetime have flat ones, so the test never reads spacetime curvature by itself. Stated in the working way's simplifies field, the formal way and check milne-slices.
- Negative-curvature limit of the small-ring law: f = a sinh(rho/a) gives rings longer than 2 pi rho at every radius, so the sign statement holds globally there, not only for small rings.

**Fixes**

- Corrected the second author's name from Diquet to Diguet, the conventional and correct spelling: Charles Francois Diguet (1822-1897). Changed in the alias, in the objective state-and-use-the-theorem, in the theorem name in the formal way, in the pronunciation (now dee-GAY, since 'gu' before 'e' is a hard g in French) and in the history entry's id and people.
- Corrected the 1848 reference: it now carries all three authors, the title 'Demonstration d'un theoreme de Gauss' (not 'de M. Gauss') and pages 80-90 of Journal de mathematiques pures et appliquees volume 13, the standard joint citation. The previous record cited Bertrand alone at pages 80-82 and recorded the spelling question the wrong way round.
- Working way rings-around-us-in-the-universe: moved 'which is positive for negatively curved space' next to the curvature density parameter it describes, because after 'today's expansion rate' it read as a claim about the Hubble constant. Same words, no change of length.
- Formal way geodesic-circles-theorem-and-limits: the Jacobi field that defines sqrt G now has J'(0) a unit vector perpendicular to the radial geodesic. With J(0) = 0 and |J'(0)| = 1 alone, a radial component is allowed and the field is not the angular one.
- No number changed anywhere in the note, and no entry sentence was rewritten: every entry rewrite of the novice review was checked and kept.

**Concerns**

- This record replaces the physics record of revision 4, which the schema has no room to keep alongside a new one. The note is untracked in git, so the superseded file was copied to the pipeline scratchpad as circumference-to-radius-test.before-physics.json (the revision-4 record itself is also in circumference-to-radius-test.before-physics.round1.json). Its one diff_check, dated 2026-09-13 at revision 4, is in those snapshots and is not repeated here.
- Entry check a-ring-that-is-too-long still fits a swim ring with a radius of curvature near 5 cm (a torus with tube radius times hole-side radius about 25 cm^2), not the curvature note's swim ring of tube radius 10 cm and centre-circle radius 25 cm, where a 2 cm ring measures 12.62 cm, too close to the 12.57 cm playground length to make the point. The check names no size and its own numbers are realizable, so it is accurate as it stands; an editor who wants the two notes to share one swim ring should use a 5 cm walk and a 32.3 cm ring, which the curvature note's torus gives (computed 32.17 cm by geodesic integration, 32.29 cm by the small-ring law). That is an entry-rung change and would need a novice re-read.
- The conventions file still fixes no row for the curvature density parameter Omega_K = -K c^2/H_0^2, and none for whether the scale factor or the curvature constant carries length units in the cosmological line element. The note's statements hold under either assignment, because K = k/a^2 either way, but a row is needed before more cosmology notes are written. Reported rather than invented, as the conventions file requires.
- The registry entry knowledge/concepts/curvature/_registry.json still carries the misspelling in its alias and summary ('Bertrand-Diquet-Puiseux'), inherited from the source study. The sibling note gaussian-curvature.json already spells it Diguet. The registry is scaffolding and outside this review's scope, so an editor should fix the alias there.
- The flagship visual paced-ring-on-a-ball-and-a-plain has no catalog entry in knowledge/visuals/ and is shared by several curvature notes. Its sketch correctly requires the saddle and swim-ring rings to be drawn by geodesic walks rather than taut strings; that instruction must survive into the catalog entry.
- Three entry parts remain at their ceilings after this review, which changed no entry prose: entry way explanations at 1,097 words of the 1,100 review allowance, the summary at 499 of 500 characters, and the takeaway of 'Too short, just right, too long' at exactly 240 characters. Any later entry addition needs a matching cut.
- The entry rung names a cone's tip as the exception without saying what happens there, as the novice reviewer recorded. That is a deliberate budget choice, not an error: a reader who asks is answered by the working way's cone.

**Diff check** (2026-09-13, revision 7)

- Scope of this diff check: note_diff between the pre-re-read snapshot and revision 7 reports exactly one changed learner-visible string, at the working rung, in ways_in/rings-around-us-in-the-universe/explanation, where one sentence became two.: python3 knowledge/_tools/note_diff.py on the before-reread snapshot against the current note; then read the whole working way and every other field of the note that names the curvature density parameter (objectives, problems/cosmic-ring-excess, observations/flatness-of-space-from-sound-patterns, leads_to) to place the change in context. → One changed string, at the working rung; nothing at entry, formal or research. Old: '... give the curvature density parameter $\Omega_K = -Kc^2/H_0^2$, which is positive for negatively curved space, where $H_0$ is the Hubble constant, today's expansion rate.' New: '... give the curvature density parameter $\Omega_K = -Kc^2/H_0^2$, where $H_0$ is the Hubble constant, today's expansion rate. $\Omega_K$ is positive for negatively curved space.' The re-read moved a clause and added no quantity, number, symbol or condition.
- The relocated sentence claims exactly what the old one claimed: the same parameter, the same defining formula, the same gloss of $H_0$, the same sign statement.: Word-by-word comparison of the two versions. Checked that the split adds only the subject '$\Omega_K$' and a full stop, and that no hypothesis travelled with the clause. Checked that the sign claim, now a separate sentence, still has its defining formula in the sentence before it, so the reader can still verify it where it stands. → Identical claim, and strictly less ambiguous: in the old order the relative clause 'which is positive for negatively curved space' followed 'today's expansion rate' and could be read as a claim about $H_0$, which would have been false as a statement about curvature. The new sentence names its subject, so the sign attaches to $\Omega_K$ only.
- The sign statement '$\Omega_K$ is positive for negatively curved space' is true, and true without further hypotheses, given the definition $\Omega_K = -Kc^2/H_0^2$ stated in the sentence before it.: Algebra: $c^2 > 0$ and $H_0^2 > 0$ for any non-zero $H_0$, so $\operatorname{sign}(\Omega_K) = -\operatorname{sign}(K)$. Checked the three branches numerically in python3 with $H_0 = 67.4$ km/s/Mpc: $K = -10^{-52}\,\text{m}^{-2}$ gives $\Omega_K = +1.884$, $K = 0$ gives $0$, $K = +10^{-52}\,\text{m}^{-2}$ gives $-1.884$. Checked that $\Omega_K$ is dimensionless: $[K][c^2]/[H_0^2] = \text{m}^{-2}\,\text{m}^2\text{s}^{-2}/\text{s}^{-2}$. → True in every branch, and dimensionless as a density parameter must be. The statement needs no scope beyond the definition it follows: it does not say 'all', and it stays true for a contracting universe, because $H_0$ enters squared. It is also unaffected by the one thing the sentence leaves implicit, the cosmic time at which $K$ is read, because $K = k/a^2$ keeps the sign of $k$ at every time.
- The split sentence is consistent with the sentences around it in the same way, and with the note's other statements of the same sign rule.: Checked the working way's own chain: 'For $k < 0$ the sine becomes a hyperbolic sine and every ring is too long', then $K = k/a^2$, then the definition, then '$K = -\Omega_K H_0^2/c^2$' and $C/2\pi\ell \approx 1 + (\Omega_K/6)(H_0\ell/c)^2$. Compared with observations/flatness-of-space-from-sound-patterns ('zero for flat space and positive for negatively curved space') and with problems/cosmic-ring-excess ('a positive $\Omega_K$ means negatively curved space', key point 'A positive curvature density parameter means negative curvature'). → Consistent everywhere, and the wording now matches the observation's wording for the same rule, so the note says one thing one way. The inverse relation $K = -\Omega_K H_0^2/c^2$ is the exact inverse of the definition, and the leading sign of the small-ring law follows: $-K\ell^2/6 = +(\Omega_K/6)(H_0\ell/c)^2$, so positive $\Omega_K$ gives a ring that is too long, as the way's earlier hyperbolic-sine sentence says.
- The numbers the changed sentence leads into still work out, and the sign of the result matches the sign rule as now stated.: python3 with $H_0 = 67.4$ km/s/Mpc $= 2.1843\times10^{-18}\,\text{s}^{-1}$ and $\ell = 13.9$ Gpc $= 4.289\times10^{26}$ m: computed $H_0\ell/c$, the small-ring excess $(\Omega_K/6)(H_0\ell/c)^2$ for $\Omega_K = 0.001 \pm 0.002$, and the exact ratio $\sinh(\sqrt{-K}\ell)/(\sqrt{-K}\ell)$ with $K = -\Omega_K H_0^2/c^2$. → $c/H_0 = 4448$ Mpc, $H_0\ell/c = 3.125$, excess $0.163\%$ with an uncertainty of $0.326\%$, so $(0.2 \pm 0.3)\%$ as the way states; the exact ratio agrees with the approximation to better than $10^{-5}$. $\Omega_K = +0.001$ gives $K = -5.31\times10^{-56}\,\text{m}^{-2}$, negative curvature and a ring that is too long, exactly as the changed sentence requires.
- The sign convention of the quoted measurement matches the convention the changed sentence states.: Checked the definition behind the quoted $\Omega_K = 0.001 \pm 0.002$: the standard cosmological curvature density parameter is $\Omega_K = 1 - \Omega_\text{tot} = -kc^2/(a_0^2H_0^2)$, positive for an open, negatively curved universe. Compared with the note's $\Omega_K = -Kc^2/H_0^2$ and $K = k/a^2$. No reference was added or altered by the re-read, so nothing needed re-verifying against a source. → Same convention and same sign, so the quoted value keeps its meaning under the new wording and no 'different sign convention' note is needed. The reference in observations/flatness-of-space-from-sound-patterns was confirmed at the full physics review and is untouched.
- The re-read stayed inside the length budget, and no other sentence was compressed to make room for the split.: Validator word counts before and after, and the note_diff output as the complete list of changed learner-visible strings. → Working way explanations are 610 words against a 1,000-word cap, so the split used none of the review allowance. note_diff lists no other changed string, so nothing was shortened elsewhere.
