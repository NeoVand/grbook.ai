---
type: "concept"
schema_version: 2
id: "number-of-independent-riemann-components"
title: "Number of independent Riemann components"
tagline: "How many numbers the curving at one spot can need: 0, 1, 6 or 20"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["independent components of the Riemann tensor", "Riemann tensor component count"]
prerequisites: ["symmetries-of-the-riemann-tensor", "cyclic-identity", "gaussian-curvature", "ricci-tensor"]
leads_to: ["weyl-tensor", "equivalence-problem", "sectional-curvature", "gravitational-degrees-of-freedom"]
visuals: ["twenty-of-256-slots", "coordinate-knobs-and-metric-dials", "falling-ring-of-crumbs"]
---

# Number of independent Riemann components

*How many numbers the curving at one spot can need: 0, 1, 6 or 20*

`number-of-independent-riemann-components` · curvature · core · physics-reviewed (revision 7)

**Needs:** [[symmetries-of-the-riemann-tensor]] (entry) · [[cyclic-identity]] (entry) · [[gaussian-curvature]] (working) · [[ricci-tensor]] (working)  
**Opens:** [[weyl-tensor]] · [[equivalence-problem]] · [[sectional-curvature]] · [[gravitational-degrees-of-freedom]]  
**Related:** [[riemann-curvature-tensor]] · [[relativistic-tidal-tensor]] · [[kretschmann-scalar]] · [[gravitational-wave-polarization]]  
**Visuals:** ★ [[twenty-of-256-slots]] · [[coordinate-knobs-and-metric-dials]] · [[falling-ring-of-crumbs]]

> Carry an arrow around tiny loops at one spot, and the curving there fills a table of numbers. Rules make most entries zero, or copies or opposites of other entries. So on a surface one number is enough, in ordinary space six, and in space and time twenty. A line needs none, however it is coiled.

## You will be able to

**Entry**
- Use the times-table recipe to find how many numbers the curving at one spot can need, for any number of directions. `objectives/count-with-the-times-table-recipe` ← `checks/guess-256`, `problems/flatland-with-time`
- Explain why a coiled or knotted line needs no curvature numbers. `objectives/explain-why-a-line-needs-none` ← `checks/ant-in-a-coiled-hose`
- Explain why a tide meter's 9 readings hold 6 separate numbers, and why they are only part of the curvature table. `objectives/explain-what-a-tide-meter-reads` ← `checks/what-the-tide-meter-misses`, `problems/flatland-with-time`

**Working**
- Derive the general component count from index pairs and the cyclic identity, and compute it in any dimension. `objectives/derive-the-general-count` ← `checks/twenty-one-or-twenty`, `problems/five-dimensions-both-ways`
- Compare the metric's Taylor coefficients with coordinate freedom order by order, and find the surviving second derivatives. `objectives/count-coordinate-freedom` ← `problems/five-dimensions-both-ways`
- Use the Riemann, Ricci and Weyl counts to decide what vacuum curvature and wave polarizations can carry. `objectives/use-counts-across-dimensions` ← `checks/empty-space-three-and-four`, `checks/twenty-and-two`
- Compute the single curvature component of a surface and its Gaussian curvature. `objectives/compute-the-surface-component` ← `problems/hyperbolic-plane-component`

**Formal**
- Prove that every algebraic curvature tensor is realized by a metric and that the second-order jet modulo coordinates is exactly the curvature. `objectives/prove-realization-and-exactness` ← `checks/injective-third-order-map`, `problems/every-curvature-tensor-occurs`
- Distinguish frame-dependent components from invariants, and bound the number of independent curvature invariants. `objectives/bound-the-invariants` ← `checks/boosted-observers-disagree`

## Ways in

### 1. Half a times table · entry · calculation

*Why can the curving at one spot need 1 number on a surface, 6 in space and 20 in space and time?*

**Recap:** The curvature table, the Riemann curvature tensor, lists how an arrow carried around a tiny loop comes back changed. A tilt is a pair of different directions, like the bottom, front or side of a box. Walking a loop the other way flips the change, and the lean rule flips it when the arrow's two directions swap. So one number for each pairing of an arrow's tilt with a loop's tilt fixes every entry. The mirror rule: swapping the two tilts gives the same number. The cyclic identity ties together three entries whose four directions all differ.

A times table for the numbers 1 to 6 has 36 answers. But 3 times 4 is the same as 4 times 3. So you only need the 6 answers where a number meets itself, like 3 times 3, and half of the other 30. That makes 6 plus 15, or 21 answers.

The curvature table counts the same way. Space and time have four directions: ahead, left, up and time. Pairing different directions gives six tilts: ahead with left, ahead with up, ahead with time, left with up, left with time, and up with time. You can check the count: ahead pairs with 3 others, left with 2 more, and up with 1 more, and 3 plus 2 plus 1 is 6.

A tilt that uses time cannot be drawn on a box. It is still a pair of different directions, so it counts the same way.

Now make a grid of tilts. Each row is an arrow's tilt, and each column is a loop's tilt. So the grid is 6 by 6, with 36 boxes. By the mirror rule, swapping the row and column tilts gives the same number, just as 3 times 4 equals 4 times 3. So 21 numbers fix all 36 boxes.

The cyclic identity ties together three boxes that use all four directions. They pair ahead-left with up-time, ahead-up with left-time, and ahead-time with left-up. These three boxes belong to three different mirror pairs, so the mirror rule does not tie them to each other. The cyclic identity does: any two of them fix the third. So one of the 21 numbers is not needed.

Space and time have exactly four directions, so there is only one way to choose four different ones. That leaves 20 numbers, and they fix the whole table.

The recipe works for any number of directions. Count the tilts, and make a grid with one row and one column for each tilt. Keep the boxes where a tilt meets itself, and half of the rest. Then take away one number for each group of four different directions.

- A surface has 2 directions and 1 tilt: 1 number.
- Space has 3 directions and 3 tilts: 3 plus half of 6, or 6 numbers.
- Space and time: 21 minus 1, or 20 numbers.

These counts say how many numbers the curving can need. Some of the numbers can be zero at a spot. Where there is no curving at all, as on a flat floor, every one of them is zero.

**Try it:** Draw a 3-by-3 grid. Label its rows, and also its columns, with the tilts of space: ahead-left, ahead-up and left-up. Go through the boxes one row at a time, starting at the top row and taking each row from its first box to its last. Cross out a box if you have already kept the box with the same two tilts swapped. You should keep 6 boxes: the 3 where a tilt meets itself, and 3 more.

**Takeaway:** Make a grid of tilts. Keep the boxes where a tilt meets itself and half the rest, then remove one for each group of four different directions. That gives 1 number on a surface, 6 in space and 20 in space and time.

*Builds on:* [[symmetries-of-the-riemann-tensor]], [[cyclic-identity]]<br>*Visuals:* [[twenty-of-256-slots]]<br>*See:* `checks/guess-256`

### 2. A coiled string has nothing to count · entry · contrast

*Can a line be curved, as far as someone living in it could ever tell?*

**Recap:** A tilt is a pair of different directions, like the bottom, front or side of a box. Each entry of the curvature table pairs an arrow's tilt with a loop's tilt.

Tie a knot in a piece of string with two free ends, then coil it on a table.

Now imagine an ant that lives in the string. It can only crawl along the string, forward or back, and it carries a tape measure.

Mark a dot on the string every centimetre. Then untie the knot and pull the string straight along a ruler. The string does not stretch, so neighbouring dots are 1 centimetre apart before and after. So every distance the ant can measure is the same on the coiled string and the straight one, and nothing it measures can show the coils or the knot.

The curvature table gives the same answer. Its entries need tilts, and a tilt needs two different directions. Along a string there is only one direction, forward, with back as its opposite. So a line has no tilts, and its table has no entries. The recipe of "Half a times table" gives 0 tilts, so 0 numbers.

The bending you see belongs to how the string lies in the room, not to the string itself.

A ball's surface is different. A piece of orange peel cannot be pressed flat without tearing or stretching. That tearing or stretching happens because on a ball the surface's 1 number is not zero. A sheet of paper rolled into a tube unrolls flat again, and its number is zero.

**Try it:** Mark dots 1 centimetre apart along a shoelace. Coil it on a table and measure the gaps along the lace. Then lay it straight beside a ruler. Each gap is 1 centimetre both times.

**Takeaway:** A line has no tilts, so its curvature table is empty: however a string is coiled or knotted, every distance along it matches the same string pulled straight.

*What this leaves out:* On a string tied into a ring, an ant crawling its whole length arrives back at its start. That comes from the joined ends, not from curving.

*Continues:* `ways_in/half-a-times-table`<br>*See:* `checks/ant-in-a-coiled-hose`

### 3. Six readings for the tides · entry · operational

*How many different readings does a tide meter make, and how much of the curvature table do they give?*

**Recap:** In a room falling freely near a planet, crumbs away from the room's centre slowly drift: apart along the line toward the planet's centre, and together across it. This is tidal drift. With time as a fourth direction, the curvature table records it. When the planet's gravity does not change with time, tidal drift forms no whirlpool: of two crumbs out along directions at right angles, each drifts toward the other's direction equally. A tilt is a pair of different directions. The mirror rule: swapping an arrow's tilt with a loop's tilt gives the same number.

Picture a small box falling freely just above Earth's surface, without spinning. Three arms, each 1 metre long, stick out from its centre at right angles. One arm points away from Earth's centre; call it the up arm. The other two point across that line; call them the ahead arm and the left arm. These are only names.

At the end of each arm floats a crumb, let go at rest in the box. Call this a tide meter.

A reading is how far one crumb has drifted along one arm's direction, measured with a ruler in the box. Each crumb can drift along any of the three directions, so the three crumbs give 3 times 3, or 9, readings. Three are drifts along the crumb's own arm, outward or inward. The other six are sideways drifts.

Earth's gravity hardly changes from moment to moment, so tidal drift forms no whirlpool. So the ahead crumb's drift toward the left arm equals the left crumb's drift toward the ahead arm. The same holds for each pair of arms. So the 6 sideways drifts hold 3 numbers. With the 3 drifts along the arms, that makes 6 separate numbers.

With the up arm pointing away from Earth's centre, the sideways drifts happen to be zero. Set the arms at a slant, or fall near a lumpy moon, and they need not be.

Take on trust that each reading is one box of the grid in "Half a times table". Its row is the tilt of time with the crumb's arm. Its column is the tilt of time with the drift's direction. Three tilts use time: time with ahead, with left and with up. So the readings fill a 3-by-3 corner of the 6-by-6 grid, and the no-whirlpool pairs are that corner's mirror pairs. The mirror rule leaves 3 plus 3, or 6.

So the tide meter reads 6 of the 20 numbers. A crumb at rest in the box does not move through space; it moves only through time. So only boxes whose row and column both use time decide its drift. Each of the other 14 numbers has a row or a column without time. So one tide meter cannot read the whole table.

Near Earth these drifts are tiny. In 10 seconds, the up crumb drifts about 15 hundredths of a millimetre away from the box's centre. That is about the thickness of a sheet and a half of paper, which is why you never notice the drift.

**Takeaway:** A tide meter's 9 readings hold 6 separate numbers, the part of the 20-number curvature table that sets how crumbs at rest in the box drift.

*What this leaves out:* Treats the arms as short compared with the distance to Earth's centre.

*Continues:* `ways_in/half-a-times-table`<br>*Builds on:* [[symmetries-of-the-riemann-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/what-the-tide-meter-misses`

### 4. Pairs of pairs, minus one per four indices · working · calculation

*What is the count in n dimensions, and why does each set of four distinct indices remove exactly one number?*

The times-table count of "Half a times table" becomes a formula once each tilt is an index pair: ahead-with-left becomes the unordered pair $\{1,2\}$, and each box of the grid becomes a component. Lower the first index, $R_{\rho\sigma\mu\nu} = g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$, and use the symmetries

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma},\qquad R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0.$$

- *Pairs.* Antisymmetry makes components with $\rho = \sigma$ or $\mu = \nu$ vanish and fixes the rest by their unordered pairs. There are $N = n(n-1)/2$ pairs, so the tensor becomes an $N\times N$ array $R_{AB}$.
- *Pair exchange* makes the array symmetric: $N(N+1)/2$ entries.
- *Cyclic identity.* If two of $\sigma, \mu, \nu$ coincide, last-pair antisymmetry makes the sum vanish; if $\rho$ equals one of them, pair exchange does. So only distinct indices $a<b<c<d$ give a condition, $R_{abcd} + R_{acdb} + R_{adbc} = 0$, linking the entries $(ab,cd)$, $(ac,db)$ and $(ad,bc)$. Fixing $b$, $c$ or $d$ instead gives the same relation up to sign, and different index sets involve different entries. So each set removes exactly one number.

The derivation "Pairs minus fours" simplifies the result to

$$N_R(n) = \frac{N(N+1)}{2} - \binom{n}{4} = \frac{n^2(n^2-1)}{12},$$

with $\binom n4 = 0$ for $n<4$: 0, 1, 6, 20 and 50 for $n = 1$ to 5. Raising an index is invertible, so $R^\rho{}_{\sigma\mu\nu}$ carries the same number.

On a surface every component is $\pm R_{1212}$ or zero, and $R_{1212} = K\det g$ with $K$ the Gaussian curvature. A sphere of radius $a$ has $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$ and $\det g = a^4\sin^2\theta$, so $K = 1/a^2$.

**Takeaway:** Index pairs make a symmetric array, and each set of four distinct indices adds one cyclic relation, leaving n squared times n squared minus one, over twelve, components.

*Continues:* `ways_in/half-a-times-table`<br>*Builds on:* [[symmetries-of-the-riemann-tensor]], [[cyclic-identity]], [[gaussian-curvature]]<br>*Visuals:* [[twenty-of-256-slots]]<br>*See:* `derivations/pairs-minus-fours`, `worked_examples/a-list-of-the-twenty`

### 5. What coordinates cannot remove · working · structure

*How does counting coordinate freedom give the same number without using the Riemann tensor's symmetries?*

The coiled string of "A coiled string has nothing to count" measured like a straight one: on a line, choosing arc length as the coordinate removes every trace of bending. In $n$ dimensions coordinates remove less, and counting how much less gives the tilt count of "Pairs of pairs, minus one per four indices" a second time.

Expand the metric and a coordinate change $x^\mu(x')$ in Taylor series about a point $p$. The metric has $n(n+1)/2$ values, $n\cdot n(n+1)/2$ first derivatives and $[n(n+1)/2]^2$ second derivatives. The coordinate change has $n^2$ first, $n\cdot n(n+1)/2$ second and $n\cdot n(n+1)(n+2)/6$ third derivatives. In four dimensions the orders compare as 10 with 16, 40 with 40, and 100 with 80.

The local flatness theorem uses the first two orders: $g_{\mu\nu}(p) = \eta_{\mu\nu}$ with 6 Lorentz transformations to spare, and $\partial_\lambda g_{\mu\nu}(p) = 0$. At the next order the third derivatives $A_{\mu\alpha\beta\gamma}$, symmetric in their last three indices, shift the second derivatives by $A_{\mu\nu\alpha\beta} + A_{\nu\mu\alpha\beta}$. That map is one-to-one, so all 80 numbers take effect and exactly 20 combinations survive. In general, as the derivation "Counting what coordinates cannot remove" shows,

$$\Big[\frac{n(n+1)}{2}\Big]^2 - \frac{n^2(n+1)(n+2)}{6} = \frac{n^2(n^2-1)}{12}.$$

The survivors are the Riemann components. Where $\Gamma(p) = 0$, $R_{\rho\sigma\mu\nu}(p)$ is half a signed sum of four second derivatives of $g$, unchanged by the third-order shift, and in normal coordinates $g_{\mu\nu} = \eta_{\mu\nu} - \tfrac13R_{\mu\alpha\nu\beta}x^\alpha x^\beta + O(x^3)$ rebuilds those second derivatives from $R$. So the two counts agree because they count the same thing. For $n = 1$ the ledger gives $1 - 1 = 0$, the string; for $n = 2$ it gives $9 - 8 = 1$, the Gaussian curvature.

**Takeaway:** At a point, coordinates can fix the metric and its first derivatives, but as many second-derivative combinations as there are Riemann components survive, and they are those components.

*What this leaves out:* Counts at one point of a smooth metric.

*Continues:* `ways_in/a-coiled-string-has-nothing-to-count`, `ways_in/pairs-of-pairs-minus-fours`<br>*Builds on:* [[local-flatness-theorem]], [[riemann-tensor-in-normal-coordinates]]<br>*Visuals:* [[coordinate-knobs-and-metric-dials]]<br>*See:* `derivations/what-coordinates-cannot-remove`, `problems/five-dimensions-both-ways`

### 6. Empty space in three and four dimensions · working · contrast

*Why must empty space be flat with two space dimensions and time, but not in our world?*

The count of "Pairs of pairs, minus one per four indices", 6 components in three dimensions and 20 in four, decides whether empty space can be curved. The Ricci tensor $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$ is symmetric, with $n(n+1)/2$ components: 6 in three dimensions and 10 in four.

In three dimensions both counts are 6. That makes it possible for Ricci to fix Riemann, and the derivation "Ricci fixes Riemann in three dimensions" proves it, in either signature:

$$R_{\rho\sigma\mu\nu} = g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu} - \frac{R}{2}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big).$$

So $R_{\mu\nu} = 0$ forces $R_{\rho\sigma\mu\nu} = 0$. With two space dimensions and time, the vacuum Einstein equation without a cosmological constant, taken on trust here, gives $R_{\mu\nu} = 0$. Empty space is then locally flat: no tidal drift outside a star and no gravitational waves. A point mass only removes a wedge, as in a paper cone.

In four dimensions the Ricci tensor holds 10 of the 20 numbers and misses the other 10, the Weyl tensor. For $n \ge 3$ the contraction is onto the symmetric tensors, so the Weyl tensor has $n(n+1)(n+2)(n-3)/12$ components: 0, 10 and 35 for $n = 3, 4, 5$. Outside Earth $R_{\mu\nu} = 0$, yet a static observer measures $R_{\hat r\hat 0\hat r\hat 0} = -2GM/c^2r^3$. That negative component is a stretch along the radius, by the geodesic deviation equation in the course conventions. That curvature is pure Weyl.

A surface is the opposite case. Its Ricci tensor has 3 components but carries one number, $R_{\mu\nu} = Kg_{\mu\nu}$, with $R = 2K$.

**Takeaway:** In three dimensions Ricci and Riemann both have 6 components and Ricci fixes Riemann, so vacuum is flat; in four, 10 Weyl components survive zero Ricci and make the tides of empty space.

*What this leaves out:* General relativity with no cosmological constant, for the vacuum statements.

*Continues:* `ways_in/pairs-of-pairs-minus-fours`<br>*Builds on:* [[ricci-tensor]]<br>*See:* `derivations/ricci-fixes-riemann-in-three-dimensions`, `checks/empty-space-three-and-four`

### 7. Algebraic curvature tensors · formal · structure

*What exactly is counted, is every such tensor a real curvature, and what does the count leave out?*

The second derivatives that coordinates cannot remove, found in "What coordinates cannot remove", become exact statements about one tangent space. Let $V$ be a real $n$-dimensional vector space with a nondegenerate metric $g$ of any signature.

*Definition.* An algebraic curvature tensor is $R \in \otimes^4V^*$ with $R_{abcd} = -R_{bacd} = -R_{abdc}$ and $R_{abcd} + R_{acdb} + R_{adbc} = 0$; pair exchange follows. They form $\mathcal K(V)$, and $\mathrm{Sym}^2(\Lambda^2V^*) = \mathcal K(V)\oplus\Lambda^4V^*$ gives $\dim\mathcal K(V) = n^2(n^2-1)/12$.

*Theorem 1 (realization).* Every $R \in \mathcal K(V)$ is the Riemann tensor at the origin of $g_{\mu\nu}(x) = g_{\mu\nu} - \tfrac13R_{\mu\alpha\nu\beta}x^\alpha x^\beta$. *Sketch:* $\partial g(0) = 0$, so the curvature at the origin is the four-term combination of second derivatives, and the cyclic identity turns it back into $R$.

*Theorem 2 (jets).* At a point where $g = \eta$ and $\partial g = 0$, the sequence

$$0 \to S^3V^*\otimes V \xrightarrow{\ \delta\ } S^2V^*\otimes S^2V^* \xrightarrow{\ \mathrm{Riem}\ } \mathcal K(V) \to 0$$

is exact. *Sketch:* $\delta$ is injective, because a tensor antisymmetric in its first two slots and symmetric in its last three vanishes; coordinate changes leave the curvature at $p$ unchanged, so $\mathrm{Riem}\circ\delta = 0$; Theorem 1 gives surjectivity; the dimensions add up. The Riemann tensor at $p$ is exactly the metric's second-order jet modulo coordinates.

*Theorem 3 (decomposition).* For $n\ge3$, under the full orthogonal group $O(g)$, $\mathcal K = \mathbb R\oplus S^2_0V^*\oplus\mathcal W$: scalar curvature, trace-free Ricci and Weyl, of dimensions 1, $n(n+1)/2 - 1$ and $n(n+1)(n+2)(n-3)/12$, so $1 + 9 + 10$ in four dimensions. For a Riemannian metric in four dimensions, $SO(4)$ splits $\mathcal W$ into self-dual and anti-self-dual halves of 5 each. For $n = 2$, $\mathcal K = \mathbb R$. *Sketch:* the map $P(S)$ of the derivation "Ricci fixes Riemann in three dimensions" sends a symmetric tensor to a curvature tensor whose Ricci contraction is $(n-2)S + (\mathrm{tr}\,S)g$, an invertible map for $n\ge3$, so $\mathcal K$ splits into that image and the Weyl kernel; irreducibility of the summands is standard representation theory.

*Invariants.* Scalar invariants are functions on $\mathcal K$ constant on $O(g)$-orbits. For $n\ge3$ the generic stabilizer is discrete, so at most $n^2(n^2-1)/12 - n(n-1)/2 = n(n-1)(n-2)(n+3)/12$ are functionally independent: 3 for $n = 3$, 14 for $n = 4$. For $n = 2$ the group fixes every $R$, and $K$ is itself invariant. For a Riemannian metric the group is compact, so polynomial invariants do separate orbits. In Lorentzian signature orbits need not be closed, so invariants do not separate them: a plane gravitational wave has $R\neq0$ with every polynomial invariant zero.

*Limits.* The count is pointwise and algebraic. Across a region the second Bianchi identity ties the derivatives of $R$, and the field equations' degrees of freedom are a different count: 2 per point for vacuum gravity in four dimensions, 0 in three. Nor does the count say how many components a symmetric geometry keeps: outside a static round star, a static orthonormal frame shows six nonzero pair entries with only two magnitudes, $M/r^3$ and $2M/r^3$ with $G = c = 1$, while inside a star of varying density the same frame shows four. A connection that is not Levi-Civita has more independent curvature components.

**Takeaway:** Algebraic curvature tensors are all realized by metrics and equal second-order jets modulo coordinates; they split into scalar, trace-free Ricci and Weyl parts.

*Continues:* `ways_in/what-coordinates-cannot-remove`, `ways_in/empty-space-in-three-and-four-dimensions`<br>*Builds on:* [[riemann-normal-coordinates]]<br>*See:* `problems/every-curvature-tensor-occurs`, `checks/boosted-observers-disagree`, `checks/injective-third-order-map`, `cyclic-identity/ways_in/first-bianchi-for-any-connection`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| tilt | — | A pair of different directions at a spot, like the bottom, front or side of a box. A tilt can also pair time with a direction of space. A loop's tilt comes from the directions of its sides; an arrow's tilt, from its starting direction and the direction its change is read in. | — |
| curvature table | — | A table kept at every spot, listing how an arrow carried around a tiny loop comes back changed, for each tilt of the loop and each starting direction of the arrow. Its full name is the Riemann curvature tensor. | [[riemann-curvature-tensor]] |
| lean rule | — | A rule of the curvature table. Swapping an arrow's two directions, its starting direction and the direction its change is read in, turns an entry into its opposite. | [[symmetries-of-the-riemann-tensor]] |
| mirror rule | — | Swapping a loop's tilt with the arrow's tilt leaves an entry of the curvature table unchanged. | [[symmetries-of-the-riemann-tensor]] |
| cyclic identity | SIK-lik eye-DEN-tih-tee | The fourth rule of the curvature table. It ties together three entries that use four different directions, so that any two of them fix the third. | [[cyclic-identity]] |
| tidal drift | — | The slow drift of neighbouring objects falling freely near a planet: apart along the line toward the planet's centre, and together across it. | [[tidal-force]] |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tide meter | — | A small box falling freely without turning, with a crumb let go at rest at the end of each of three arms at right angles. | — |

## Key equations

### Independent Riemann components in n dimensions · working

$$
N_R(n) = \frac{n^2(n^2-1)}{12}
$$

The number of algebraically independent components of the Riemann tensor at one point: 0, 1, 6, 20 and 50 for $n = 1$ to 5.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $n$ | the dimension | n, the number of dimensions |
| $N_R(n)$ | the number of independent components of $R_{\rho\sigma\mu\nu}$ | the number of independent Riemann components |

**Holds when:** Levi-Civita connection (torsion-free and metric-compatible), any signature; counts independent components at one point, not nonzero components of a particular metric.  
**Say it:** “The number of independent Riemann components is n squared times n squared minus one, over twelve.”  
**Justified by:** `derivations/pairs-minus-fours`

### Second derivatives coordinates cannot remove · working

$$
\Big[\frac{n(n+1)}{2}\Big]^2 - \frac{n^2(n+1)(n+2)}{6} = \frac{n^2(n^2-1)}{12}
$$

The metric's second derivatives at a point, less the third-order coefficients of a coordinate change, leave exactly the Riemann count: $100 - 80 = 20$ in four dimensions.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Big[\frac{n(n+1)}{2}\Big]^2$ | second derivatives of the metric at a point | the number of second derivatives of the metric |
| $\frac{n^2(n+1)(n+2)}{6}$ | third-order coefficients of a coordinate change | the number of third-order coordinate coefficients |

**Holds when:** One point of a smooth metric, after setting $g = \eta$ and $\partial g = 0$; exact because the third-order map is injective.  
**Say it:** “The metric's second derivatives minus the third-order coordinate freedom leave n squared times n squared minus one, over twelve.”  
**Justified by:** `derivations/what-coordinates-cannot-remove`

### The single component of a surface · working

$$
R_{1212} = K\det g,\qquad R = 2K
$$

On a surface every Riemann component is $\pm R_{1212}$ or zero, and that one number is the Gaussian curvature times the metric determinant.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature, $1/a^2$ on a sphere of radius $a$ | the Gaussian curvature |
| $\det g$ | determinant of the two-dimensional metric components | the determinant of the metric |
| $R$ | Ricci scalar | the Ricci scalar |

**Holds when:** Two dimensions, any coordinates; course sign conventions, in which a sphere has $R = +2/a^2$.  
**Say it:** “R one two one two is the Gaussian curvature times the metric's determinant, and the Ricci scalar is twice the Gaussian curvature.”  
**Justified by:** `gaussian-curvature`

### Ricci fixes Riemann in three dimensions · working

$$
R_{\rho\sigma\mu\nu} = g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu} - \frac{R}{2}\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big)
$$

In three dimensions the whole Riemann tensor is built from the Ricci tensor and the metric, so zero Ricci means zero curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\mu\nu}$ | Ricci tensor, $R^\rho{}_{\mu\rho\nu}$ | the Ricci tensor |
| $R$ | Ricci scalar, $g^{\mu\nu}R_{\mu\nu}$ | the Ricci scalar |

**Holds when:** Three dimensions, either signature; it also holds in the two dimensions of a surface, but is false in four or more, where the Weyl tensor is added.  
**Say it:** “In three dimensions the Riemann tensor is four metric-times-Ricci terms minus half the Ricci scalar times the antisymmetrized product of two metrics.”  
**Justified by:** `derivations/ricci-fixes-riemann-in-three-dimensions`

### Components the Ricci tensor misses · working

$$
N_W(n) = \frac{n^2(n^2-1)}{12} - \frac{n(n+1)}{2} = \frac{n(n+1)(n+2)(n-3)}{12}\quad (n\ge3)
$$

The Weyl tensor's components: 0 in three dimensions, 10 in four and 35 in five.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $N_W(n)$ | number of independent Weyl components | the number of Weyl components |

**Holds when:** $n \ge 3$, where the Ricci contraction is onto the symmetric tensors; for $n = 2$ the Ricci tensor is $Kg_{\mu\nu}$ and carries the one component.  
**Say it:** “The Weyl count is n times n plus one times n plus two times n minus three, over twelve.”  
**Justified by:** `derivations/ricci-fixes-riemann-in-three-dimensions`

## Derivations

### Pairs minus fours · working

**Goal:** Show that $N(N+1)/2 - \binom n4$, with $N = n(n-1)/2$, equals $n^2(n^2-1)/12$.

1. With $N+1 = (n^2-n+2)/2$, the pair count is $\frac{N(N+1)}{2} = \frac{n(n-1)(n^2-n+2)}{8}$.
2. The number of four-index sets is $\binom n4 = \frac{n(n-1)(n-2)(n-3)}{24}$, which is zero for $n < 4$.
3. Over a common denominator the difference is $\frac{n(n-1)}{24}\big[3(n^2-n+2) - (n-2)(n-3)\big]$.
4. The bracket is $3n^2 - 3n + 6 - (n^2 - 5n + 6) = 2n^2 + 2n = 2n(n+1)$.
5. So $N_R = \frac{2n^2(n-1)(n+1)}{24} = \frac{n^2(n^2-1)}{12}$.

**Result:** $N_R(n) = n^2(n^2-1)/12$: 0, 1, 6, 20, 50 for $n = 1$ to 5.

### Counting what coordinates cannot remove · working

**Goal:** Show that third-order coordinate freedom removes exactly $n^2(n+1)(n+2)/6$ of the metric's second derivatives at a point, leaving $n^2(n^2-1)/12$.

1. Arrange $g_{\mu\nu}(p) = \eta_{\mu\nu}$ and $\partial_\lambda g_{\mu\nu}(p) = 0$, then change coordinates by $x^\mu = x'^\mu + \tfrac16A^\mu{}_{\alpha\beta\gamma}x'^\alpha x'^\beta x'^\gamma$, with $A$ symmetric in $\alpha\beta\gamma$.
2. The Jacobian is $\partial x^\rho/\partial x'^\mu = \delta^\rho{}_\mu + \tfrac12A^\rho{}_{\mu\beta\gamma}x'^\beta x'^\gamma$. Meanwhile $g_{\rho\sigma}(x) - g_{\rho\sigma}(x')$ is only of fourth order in $x'$: the shift $x - x'$ is cubic, and it multiplies $\partial g$, which vanishes at $p$ and so is itself at least first order.
3. So $g'_{\mu\nu} = g_{\rho\sigma}\frac{\partial x^\rho}{\partial x'^\mu}\frac{\partial x^\sigma}{\partial x'^\nu}$ gains $\tfrac12(A_{\mu\nu\beta\gamma} + A_{\nu\mu\beta\gamma})x'^\beta x'^\gamma$, with $A$ lowered by $\eta$, and $\delta(\partial_\alpha\partial_\beta g_{\mu\nu}) = A_{\mu\nu\alpha\beta} + A_{\nu\mu\alpha\beta}$.
4. Suppose this shift vanishes, so $A_{\mu\nu\alpha\beta} = -A_{\nu\mu\alpha\beta}$. Alternating the two symmetries gives $A_{\mu\nu\alpha\beta} = -A_{\nu\alpha\mu\beta} = A_{\alpha\nu\mu\beta} = A_{\alpha\mu\nu\beta} = -A_{\mu\alpha\nu\beta} = -A_{\mu\nu\alpha\beta}$, so $A = 0$ and the map is injective.
5. Hence the $n\cdot n(n+1)(n+2)/6$ coefficients shift that many independent combinations of the $[n(n+1)/2]^2$ second derivatives.
6. The rest number $\frac{n^2(n+1)^2}{4} - \frac{n^2(n+1)(n+2)}{6} = \frac{n^2(n+1)}{12}\big[3(n+1) - 2(n+2)\big] = \frac{n^2(n^2-1)}{12}$.
7. For $n = 1, 2, 3, 4$ this is $1 - 1 = 0$, $9 - 8 = 1$, $36 - 30 = 6$ and $100 - 80 = 20$.

**Result:** Exactly $n^2(n^2-1)/12$ combinations of second derivatives survive every coordinate choice at a point, the Riemann count.

### Ricci fixes Riemann in three dimensions · working

**Goal:** Show that the Ricci contraction is onto the symmetric tensors for $n \ge 3$, count the Weyl components, and invert the contraction for $n = 3$.

1. For a symmetric tensor $S$ set $P(S)_{\rho\sigma\mu\nu} = g_{\rho\mu}S_{\sigma\nu} - g_{\rho\nu}S_{\sigma\mu} + g_{\sigma\nu}S_{\rho\mu} - g_{\sigma\mu}S_{\rho\nu}$. It has both pair antisymmetries, pair exchange and the cyclic identity, so it is a possible curvature tensor.
2. Contract with $g^{\rho\mu}$: the four terms give $nS_{\sigma\nu}$, $-S_{\sigma\nu}$, $g_{\sigma\nu}\,\mathrm{tr}\,S$ and $-S_{\sigma\nu}$, so the Ricci tensor of $P(S)$ is $(n-2)S_{\sigma\nu} + (\mathrm{tr}\,S)\,g_{\sigma\nu}$.
3. For $n\ge3$ any symmetric $Q$ is reached with $S = \big(Q - \tfrac{\mathrm{tr}\,Q}{2(n-1)}g\big)/(n-2)$, so the contraction is onto the $n(n+1)/2$ symmetric tensors.
4. Its kernel, the Weyl tensors, therefore has dimension $\frac{n^2(n^2-1)}{12} - \frac{n(n+1)}{2} = \frac{n(n+1)}{12}\big[n(n-1) - 6\big] = \frac{n(n+1)(n+2)(n-3)}{12}$.
5. For $n = 3$ the kernel has dimension 0, so a curvature tensor is fixed by its Ricci tensor, and $R = P(S)$ with $S = R_{\mu\nu} - \tfrac{R}{4}g_{\mu\nu}$.
6. Since $P(g)_{\rho\sigma\mu\nu} = 2(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, this gives $R_{\rho\sigma\mu\nu} = P(\mathrm{Ric})_{\rho\sigma\mu\nu} - \tfrac R2(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$.

**Result:** For $n\ge3$ the Weyl tensor has $n(n+1)(n+2)(n-3)/12$ components, and in three dimensions $R_{\rho\sigma\mu\nu} = g_{\rho\mu}R_{\sigma\nu} - g_{\rho\nu}R_{\sigma\mu} + g_{\sigma\nu}R_{\rho\mu} - g_{\sigma\mu}R_{\rho\nu} - \tfrac R2(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$.

## Worked examples

### A list of twenty components that fixes all 256 · working

**Problem:** In four dimensions with indices 0 to 3, write down 20 components of $R_{\rho\sigma\mu\nu}$ from which every other component follows, and express $R_{1030}$ and $R_{0312}$ through them.

1. The six index pairs are $01, 02, 03, 12, 13, 23$.
2. Diagonal entries of the pair array: $R_{0101}, R_{0202}, R_{0303}, R_{1212}, R_{1313}, R_{2323}$.
3. Off-diagonal entries, one per unordered pair of pairs: 15 of them, from $R_{0102}$ to $R_{1323}$.
4. The only cyclic relation is $R_{0123} + R_{0231} + R_{0312} = 0$. With $R_{0231} = -R_{0213}$ it gives $R_{0312} = R_{0213} - R_{0123}$, so drop $R_{0312}$ from the list.
5. First-pair antisymmetry gives $R_{1030} = -R_{0130}$, and last-pair antisymmetry gives $R_{0130} = -R_{0103}$. So $R_{1030} = R_{0103}$, an entry of the list for the pairs $01$ and $03$.

**Answer:** The 6 diagonal and 14 off-diagonal pair entries other than $R_{0312}$; $R_{1030} = R_{0103}$ and $R_{0312} = R_{0213} - R_{0123}$.

**Takeaway:** Any component reduces to one of 20 by sign flips within pairs, pair exchange, and the single cyclic relation.

## Problems

### `flatland-with-time` · entry · difficulty 2 · calculation

Picture a world with two space directions, ahead and left, plus time. How many separate numbers can its curvature table need at one spot? A tide meter there has two arms at right angles, ahead and left, with a crumb let go at rest at the end of each. How many readings does it make, how many of them are separate numbers, and what share of the table's numbers are they?

**Hints**

1. List the tilts, then keep only those that use time for the tide meter.

**Answer:** 6 numbers. The tide meter makes 4 readings, holding 3 separate numbers, so it reads 3 of the 6.

**Must contain:** Three tilts give 6 numbers; Two crumbs drifting two ways give 4 readings; Equal sideways drifts leave 3 separate numbers, half of the 6

**Numeric:** numbers in the curvature table = 6 1 (magnitude, ±0); tide meter readings = 4 1 (magnitude, ±0); different tide meter readings = 3 1 (magnitude, ±0)

**Solution**

1. Three directions give three tilts: ahead with left, ahead with time, and left with time. The mirror rule keeps the 3 where a tilt meets itself and half of the other 6, so 6 numbers remain. With only three directions there is no group of four, so the cyclic identity removes none.
2. Each of the 2 crumbs can drift ahead or left, so the tide meter makes 4 readings.
3. Tidal drift forms no whirlpool, so the ahead crumb's drift toward the left arm equals the left crumb's drift toward the ahead arm. So the 4 readings hold 3 separate numbers.
4. Two tilts use time: ahead with time, and left with time. Their corner of the grid is 2 by 2, and the mirror rule keeps 2 plus 1, or 3 numbers. That is half of the 6.

**Targets:** `tides-show-all-the-curving`

### `five-dimensions-both-ways` · working · difficulty 1 · calculation

For $n = 5$, find the number of independent Riemann components by the pair count, by the coordinate ledger and by the closed formula. Then split it into Ricci and Weyl parts.

**Hints**

1. Use $N = n(n-1)/2$ and $\binom 54$ for the pairs, and $[n(n+1)/2]^2$ against $n^2(n+1)(n+2)/6$ for the ledger.

**Answer:** 50 components in every way, split as 15 Ricci and 35 Weyl.

**Must contain:** Pair count 55 minus 5 is 50; Ledger 225 minus 175 is 50; Ricci 15 and Weyl 35

**Numeric:** independent Riemann components = 50 1 (magnitude, ±0); Weyl components = 35 1 (magnitude, ±0)

**Solution**

1. Pairs: $N = 5\cdot4/2 = 10$, so $N(N+1)/2 = 55$, and $\binom54 = 5$ sets of four indices remove 5, leaving 50.
2. Ledger: $[5\cdot6/2]^2 = 225$ second derivatives, and $5^2\cdot6\cdot7/6 = 175$ third-order coefficients, leaving 50.
3. Formula: $25\cdot24/12 = 50$.
4. Ricci has $5\cdot6/2 = 15$ components, and the contraction is onto for $n\ge3$, so Weyl has $50 - 15 = 35 = 5\cdot6\cdot7\cdot2/12$.

### `hyperbolic-plane-component` · working · difficulty 2 · calculation

The metric $ds^2 = dr^2 + \sinh^2 r\,d\phi^2$ describes a surface. Using the course definition of the Riemann tensor, find $R_{r\phi r\phi}$, list every nonzero lowered component, and find the Gaussian curvature.

**Hints**

1. The nonzero Christoffel symbols are $\Gamma^r{}_{\phi\phi}$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r}$.
2. A surface has one independent component, so find one and get the rest by symmetry.

**Answer:** $R_{r\phi r\phi} = R_{\phi r\phi r} = -\sinh^2 r$, $R_{r\phi\phi r} = R_{\phi rr\phi} = +\sinh^2 r$, all others zero, and $K = -1$.

**Must contain:** The two nonzero Christoffel symbols; R r phi r phi is minus sinh squared r; K is minus one

**Numeric:** Gaussian curvature = -1 1 (signed, ±0.001)

**Solution**

1. From $g_{\phi\phi} = \sinh^2r$: $\Gamma^r{}_{\phi\phi} = -\sinh r\cosh r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = \coth r$; all others vanish.
2. $R^r{}_{\phi r\phi} = \partial_r\Gamma^r{}_{\phi\phi} - \partial_\phi\Gamma^r{}_{r\phi} + \Gamma^r{}_{r\lambda}\Gamma^\lambda{}_{\phi\phi} - \Gamma^r{}_{\phi\lambda}\Gamma^\lambda{}_{r\phi}$.
3. The first term is $-(\cosh^2r + \sinh^2r)$, the second and third vanish, and the last is $-(-\sinh r\cosh r)(\coth r) = +\cosh^2 r$.
4. So $R^r{}_{\phi r\phi} = -\sinh^2r$, and with $g_{rr} = 1$, $R_{r\phi r\phi} = -\sinh^2 r$.
5. The pair antisymmetries and pair exchange give $R_{\phi r\phi r} = -\sinh^2r$ and $R_{r\phi\phi r} = R_{\phi rr\phi} = +\sinh^2r$.
6. $\det g = \sinh^2r$, so $K = R_{r\phi r\phi}/\det g = -1$, the opposite sign to a unit sphere.

### `every-curvature-tensor-occurs` · formal · difficulty 3 · proof

Let $R_{\rho\sigma\mu\nu}$ be any tensor with the pair antisymmetries, pair exchange and the cyclic identity. Show that the metric $g_{\mu\nu}(x) = \eta_{\mu\nu} - \tfrac13R_{\mu\alpha\nu\beta}x^\alpha x^\beta$ has Riemann tensor $R_{\rho\sigma\mu\nu}$ at the origin.

**Hints**

1. At the origin the first derivatives of $g$ vanish, so the Christoffel symbols do too.
2. Where $\Gamma = 0$, $R_{\rho\sigma\mu\nu} = \tfrac12(\partial_\mu\partial_\sigma g_{\rho\nu} - \partial_\mu\partial_\rho g_{\sigma\nu} - \partial_\nu\partial_\sigma g_{\rho\mu} + \partial_\nu\partial_\rho g_{\sigma\mu})$.

**Answer:** The first derivatives vanish at the origin, so the curvature there is the four-term combination of second derivatives. Its eight terms reduce to $-4R_{\rho\sigma\mu\nu}$ by the pair symmetries and to $-2R_{\rho\sigma\mu\nu}$ by the cyclic identity, and the prefactor $-\tfrac16$ returns $R_{\rho\sigma\mu\nu}$.

**Must contain:** First derivatives vanish at the origin, so only second derivatives enter; Pair symmetries collect four terms into minus four R; The cyclic identity turns the remaining four into minus two R

**Solution**

1. $\partial_\lambda g_{\mu\nu}(0) = 0$, so $\Gamma(0) = 0$, and the course definition leaves only the derivative terms: $R'_{\rho\sigma\mu\nu} = \tfrac12(\partial_\mu\partial_\sigma g_{\rho\nu} - \partial_\mu\partial_\rho g_{\sigma\nu} - \partial_\nu\partial_\sigma g_{\rho\mu} + \partial_\nu\partial_\rho g_{\sigma\mu})$.
2. $\partial_\alpha\partial_\beta g_{\mu\nu}(0) = -\tfrac13(R_{\mu\alpha\nu\beta} + R_{\mu\beta\nu\alpha})$, so $R' = -\tfrac16 S$ with $S = (R_{\rho\mu\nu\sigma} + R_{\rho\sigma\nu\mu}) - (R_{\sigma\mu\nu\rho} + R_{\sigma\rho\nu\mu}) - (R_{\rho\nu\mu\sigma} + R_{\rho\sigma\mu\nu}) + (R_{\sigma\nu\mu\rho} + R_{\sigma\rho\mu\nu})$.
3. Pair terms: $R_{\rho\sigma\nu\mu} = -R_{\rho\sigma\mu\nu}$, $R_{\sigma\rho\nu\mu} = R_{\rho\sigma\mu\nu}$ and $R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\mu\nu}$, so they add to $-4R_{\rho\sigma\mu\nu}$.
4. Other terms: pair exchange and both antisymmetries give $R_{\sigma\mu\nu\rho} = R_{\rho\nu\mu\sigma}$ and $R_{\sigma\nu\mu\rho} = R_{\rho\mu\nu\sigma}$, so they add to $2R_{\rho\mu\nu\sigma} - 2R_{\rho\nu\mu\sigma} = 2(R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu})$.
5. The cyclic identity gives $R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = -R_{\rho\sigma\mu\nu}$, so $S = -6R_{\rho\sigma\mu\nu}$ and $R' = R$.
6. Replacing $\eta$ by any constant nondegenerate metric changes nothing in the argument, so every algebraic curvature tensor of any signature is a Riemann tensor at a point.

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite, 2009 to 2013** (measured, working). A gradiometer is a tide meter. Its readings give the tidal matrix $E_{ij} = c^2R_{\hat i\hat 0\hat j\hat 0}$, equal to $\partial_i\partial_j\Phi$ in a weak static field. Pair exchange makes it symmetric, so its 9 entries hold 6 of the 20 components, and outside matter its trace vanishes, leaving 5. The other 14 components do not enter a non-rotating gradiometer's readings. *Numbers:* At $r = 6626$ km for a spherical Earth with $\Phi = -GM/r$: $\partial_r^2\Phi = -2GM/r^3 = -2.74\times10^{-6}\ \mathrm{s^{-2}}$ along the radius and $+1.37\times10^{-6}\ \mathrm{s^{-2}}$ along each horizontal axis, summing to zero. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **A test of gravitational-wave polarization with the three-detector event GW170814** (measured, working). For a plane wave in a general metric theory, the curvature detectors read, $R_{\hat i\hat 0\hat j\hat 0}$, has at most 6 independent numbers and fixes the wave's Riemann tensor, allowing up to six polarizations; general relativity allows two tensor ones. With both LIGO detectors and Virgo, GW170814 favoured purely tensor polarization over purely vector or purely scalar. So 20 curvature components are not 20 polarizations. *Numbers:* Two polarizations in general relativity; at most 6 in a general metric theory. *Reference:* B. P. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101

## Teaching arc

1. **Ask for a guess** (entry). Ask how many numbers the curving of space and time at one spot needs, and let the learner reach 256. *Why:* A reasonable wrong guess makes the reduction feel like a discovery. *Predict:* How many separate numbers do you think the curving at one spot in space and time needs? *Uses:* `checks/guess-256`
2. **Sieve with the times table** (entry). Count the tilts, halve the grid with the mirror rule, remove the cyclic link, then run the recipe in other dimensions. *Why:* One recipe gives the whole ladder, so 20 stops looking arbitrary. *Visual:* [[twenty-of-256-slots]] *Uses:* `ways_in/half-a-times-table`, `checks/guess-256`
3. **Two controls: a string and a tide meter** (entry). Show that a coiled string has nothing to count, and that a tide meter reads 6 of the 20 numbers. *Why:* The string separates bending from curving; the tide meter shows what one measurement misses. *Predict:* A tide meter makes nine readings. How many separate numbers can they hold? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/a-coiled-string-has-nothing-to-count`, `ways_in/six-readings-for-the-tides`, `checks/what-the-tide-meter-misses`
4. **Two routes to one number** (working). Derive the pair count, then the coordinate ledger, and have the learner check that both give 50 in five dimensions. *Why:* Two independent counts agreeing shows the Riemann tensor is all of curvature at a point. *Visual:* [[coordinate-knobs-and-metric-dials]] *Uses:* `ways_in/pairs-of-pairs-minus-fours`, `ways_in/what-coordinates-cannot-remove`, `problems/five-dimensions-both-ways`
5. **Three dimensions against four** (working). Compare the Ricci and Riemann counts and draw the consequences. *Why:* Tides in empty space exist only because 20 exceeds 10. *Predict:* In a world with only two space directions and time, could empty space around a star make falling crumbs drift apart? *Uses:* `ways_in/empty-space-in-three-and-four-dimensions`, `checks/empty-space-three-and-four`, `checks/twenty-and-two`

## Misconceptions

### “Space and time have four directions and each entry takes four choices, so the curving at a spot needs 256 separate numbers.” · entry · `every-slot-is-a-new-number`

- **Why it is tempting:** Multiplying the choices is the natural way to count table entries.
- **What is true:** The table does have 256 entries, but its rules make most of them zero, copies or opposites of others, and one more number is fixed by a three-way link. Twenty numbers fix all of them.
- **Exposed by:** `checks/guess-256`

### “A coiled or knotted string is curved, so something living in it could tell.” · entry · `bent-line-is-curved`

- **Why it is tempting:** From outside, the string looks bent in many places.
- **What is true:** Pulled straight without stretching, the string keeps every distance along it, so nothing measured along it changes. A line has no tilts, so it needs no curvature numbers.
- **Exposed by:** `checks/ant-in-a-coiled-hose`

### “If I measure every tidal drift at a spot, I know all of the curving there.” · entry · `tides-show-all-the-curving`

- **Why it is tempting:** Tidal drift is the everyday face of curving, and a tide meter measures it in every direction.
- **What is true:** A tide meter's readings hold only 6 of the 20 numbers. A crumb at rest in the box moves only through time, so the other 14 do not change how it drifts.
- **Exposed by:** `checks/what-the-tide-meter-misses`

### “The pair symmetries already give the final count, so the answer in four dimensions is 21.” · working · `cyclic-identity-never-cuts`

- **Why it is tempting:** The cyclic identity is automatic whenever an index repeats, which covers every case in three dimensions.
- **What is true:** For four distinct indices it links three different pair entries that the pair symmetries alone do not tie, so the count is 20.
- **Exposed by:** `checks/twenty-one-or-twenty`

### “In vacuum the Ricci tensor vanishes, so spacetime there has no curvature.” · working · `ricci-zero-means-flat`

- **Why it is tempting:** The vacuum field equation reads Ricci equals zero.
- **What is true:** Ricci holds 10 of the 20 components in four dimensions, and the 10 Weyl components survive in vacuum. Only in three dimensions does zero Ricci force zero curvature.
- **Exposed by:** `checks/empty-space-three-and-four`

### “Curvature has 20 independent components, so gravity has 20 degrees of freedom or gravitational waves 20 polarizations.” · working · `twenty-polarizations`

- **Why it is tempting:** Both counts are described as independent pieces of the gravitational field.
- **What is true:** The 20 are algebraic components at one event. General relativity's field equations and gauge freedom leave 2 polarizations.
- **Exposed by:** `checks/twenty-and-two`

### “The 20 components are numbers every observer at the event agrees on.” · formal · `components-are-invariants`

- **Why it is tempting:** Independent is heard as invariant.
- **What is true:** Components change under rotations and boosts of the frame. At a generic point at most 14 scalar combinations are invariant and independent.
- **Exposed by:** `checks/boosted-observers-disagree`

## Checks

1. **Entry · evaluate-claim** `checks/guess-256`. A friend says: space and time have four directions, and each entry of the curvature table takes four choices of direction. So 4 times 4 times 4 times 4 gives 256 separate numbers to describe the curving at one spot. Is the friend right?
   - **Hints:** How many tilts do four directions make, and which entries does the mirror rule make equal?
   - **Answer:** No. Walking a loop the other way flips the change, and the lean rule flips it when the arrow's two directions swap. So one number for each pairing of an arrow's tilt with a loop's tilt fixes every entry. Four directions give 6 tilts, so there are 6 times 6, or 36, pairings. The mirror rule makes swapped pairings equal, which leaves the 6 where a tilt meets itself and half of the other 30: 6 plus 15, or 21. The cyclic identity links three pairings that use all four directions, so any two fix the third, and one more number goes. So 20 numbers fix all 256 entries.
   - **Must contain:** The 256 entries are not all separate; Six tilts give 36 pairings, and the mirror rule leaves 21; The cyclic identity removes one, leaving 20
   - **Numeric:** separate numbers = 20 1 (magnitude, ±0)
   - **Targets:** `every-slot-is-a-new-number`
   - **Visual:** [[twenty-of-256-slots]]
2. **Entry · explain** `checks/ant-in-a-coiled-hose`. An ant lives inside a garden hose coiled on a lawn. It crawls only along the hose and carries a tape measure. Treating the hose as a line, can the ant find out that it is coiled? How many curvature numbers does the line need?
   - **Hints:** What happens to the distances along the hose if you lay it out straight?
   - **Answer:** No, and none. Lay the hose out straight without stretching it. Every distance along it is the same as before, so nothing the ant measures changes. The curvature table also needs tilts, and a tilt needs two different directions. Along a line there is only one direction, with back as its opposite, so the table has no entries.
   - **Must contain:** Laying the hose straight keeps every distance; A line has no tilts, so no curvature numbers
   - **Numeric:** curvature numbers = 0 1 (magnitude, ±0)
   - **Targets:** `bent-line-is-curved`
3. **Entry · predict** `checks/what-the-tide-meter-misses`. A crew falls freely just above Earth's surface with a tide meter that does not spin. It records all 9 drift readings of the meter's three crumbs. Does the crew now know every number of the curvature table at its spot? How many separate numbers does it have, and how many are missing?
   - **Hints:** Which readings does the no-whirlpool rule make equal?
   - **Answer:** No. Earth's gravity hardly changes from moment to moment, so tidal drift forms no whirlpool. So the sideways readings come in 3 equal pairs, and the 9 readings hold 6 separate numbers. The table needs 20 numbers in space and time, so 14 are missing. A crumb at rest in the box moves only through time, so only boxes whose row and column both use time decide its drift. Each of the other 14 has a row or a column without time, so none of them changes how crumbs at rest drift.
   - **Must contain:** 6 separate numbers; 14 missing; The missing ones do not change how crumbs at rest drift
   - **Numeric:** different numbers read = 6 1 (magnitude, ±0); numbers missing = 14 1 (magnitude, ±0)
   - **Targets:** `tides-show-all-the-curving`
   - **Visual:** [[falling-ring-of-crumbs]]
4. **Working · evaluate-claim** `checks/twenty-one-or-twenty`. A student counts 21 independent components of the lowered Riemann tensor in four dimensions, six times seven over two, and says the cyclic identity follows from the pair symmetries. Evaluate the claim, and say in which dimensions this method gives the right count.
   - **Hints:** Write the cyclic sum for indices 0, 1, 2, 3 and name the pair entries it contains.
   - **Answer:** Wrong in four dimensions. The cyclic sum vanishes automatically when two of its indices coincide, but for distinct indices $R_{0123} + R_{0231} + R_{0312} = 0$ links three different entries of the symmetric pair array, $(01,23)$, $(02,31)$ and $(03,12)$. A tensor whose only nonzero components are $R_{0123}$ and its partners under the pair symmetries has all the pair symmetries but a cyclic sum of $R_{0123} \neq 0$. So the identity is a new condition, and the count is $21 - 1 = 20$. The student's method is right for $n \le 3$, where $\binom n4 = 0$, giving 1 and 6.
   - **Must contain:** Four distinct indices link three distinct pair entries; Pair symmetries alone can violate the cyclic identity; 20 in four dimensions; the method works only up to three
   - **Numeric:** independent components = 20 1 (magnitude, ±0)
   - **Targets:** `cyclic-identity-never-cuts`
5. **Working · explain** `checks/empty-space-three-and-four`. Why does a vanishing Ricci tensor force the whole Riemann tensor to vanish in three dimensions but not in four? Give a measured four-dimensional example of curvature with zero Ricci tensor.
   - **Hints:** Compare $n(n+1)/2$ with the Riemann count, and look for tides outside matter.
   - **Answer:** In three dimensions both tensors have 6 components, and the explicit formula builds $R_{\rho\sigma\mu\nu}$ from $R_{\mu\nu}$ and $g$. So zero Ricci gives zero Riemann. In four dimensions Ricci has 10 components and Riemann 20, and the Ricci contraction is onto, so a 10-dimensional space of Weyl tensors has zero Ricci. Outside Earth $R_{\mu\nu} = 0$, yet a static observer at the surface measures $R_{\hat r\hat 0\hat r\hat 0} = -2GM/c^2r^3 \approx -3.4\times10^{-23}\ \mathrm{m^{-2}}$, and $c^2$ times this component is the vertical gravity gradient that gradiometers read.
   - **Must contain:** Ricci fixes Riemann in three dimensions by an explicit formula; Ten Weyl components survive zero Ricci in four; Earth's vertical gravity gradient
   - **Targets:** `ricci-zero-means-flat`
6. **Working · evaluate-claim** `checks/twenty-and-two`. Evaluate the claim: spacetime curvature has 20 independent components, so gravitational waves can come in up to 20 polarizations.
   - **Hints:** What does the vacuum field equation set to zero? / Which components does a detector's arm respond to?
   - **Answer:** The claim mixes two counts. The 20 are algebraic components at one event. In vacuum, with no cosmological constant, the Einstein equation sets the 10 Ricci components to zero, leaving the 10 Weyl components. A plane wave's components all depend on one phase and are fixed by the 6 components $R_{\hat i\hat 0\hat j\hat 0}$ that detectors read, so even a general metric theory allows at most 6 polarizations. General relativity's field equations leave 2, the plus and cross polarizations.
   - **Must contain:** Twenty is a pointwise algebraic count; Vacuum leaves 10 Weyl components; At most 6 polarizations in a metric theory, 2 in general relativity
   - **Numeric:** polarizations in general relativity = 2 1 (magnitude, ±0)
   - **Targets:** `twenty-polarizations`
7. **Formal · explain** `checks/boosted-observers-disagree`. Two observers at one event use orthonormal frames related by a boost. Do they list the same 20 components? How many independent scalar curvature invariants can there be at a generic point in four dimensions, and why does the same subtraction fail on a surface?
   - **Hints:** What is an orbit's dimension when the stabilizer is discrete?
   - **Answer:** No. The components form a representation of the Lorentz group and mix under a boost. Scalar invariants are functions constant on Lorentz orbits of the space of algebraic curvature tensors. At a generic point the stabilizer is discrete, so orbits have the group's dimension 6, and at most $20 - 6 = 14$ invariants are functionally independent. On a surface $O(2)$ fixes every curvature tensor, so orbits are points and $K$ itself is invariant; $1 - 1 = 0$ would be wrong.
   - **Must contain:** Components mix under boosts; Generic orbits have dimension 6, so at most 14 independent invariants; On a surface the group acts trivially and K is invariant
   - **Numeric:** independent invariants at a generic point = 14 1 (magnitude, ±0)
   - **Targets:** `components-are-invariants`
8. **Formal · derive** `checks/injective-third-order-map`. Show that the third-order coefficients of a coordinate change shift the metric's second derivatives at a point by an injective linear map. Deduce the exact number of surviving combinations, and say why injectivity is needed.
   - **Hints:** Chain the swaps: first pair, last three, first pair, last three.
   - **Answer:** The shift is $\delta(\partial_\alpha\partial_\beta g_{\mu\nu}) = A_{\mu\nu\alpha\beta} + A_{\nu\mu\alpha\beta}$ with $A$ symmetric in its last three indices. If it vanishes, $A$ is antisymmetric in its first two indices, and alternating the two symmetries gives $A_{\mu\nu\alpha\beta} = -A_{\mu\nu\alpha\beta}$, so $A = 0$. The image therefore has dimension $n^2(n+1)(n+2)/6$, and the quotient has dimension $[n(n+1)/2]^2 - n^2(n+1)(n+2)/6 = n^2(n^2-1)/12$. Without injectivity some coefficients would change nothing, and the subtraction would give only a lower bound on the survivors.
   - **Must contain:** The shift symmetrizes A in its first two indices; Three symmetric and two antisymmetric indices force A to vanish; Injectivity makes the subtraction exact

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which form of the Riemann tensor is counted | Count $R_{\rho\sigma\mu\nu} = g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$, with $R^\rho{}_{\sigma\mu\nu}$ as in the course definition; the mixed tensor carries the same $n^2(n^2-1)/12$ numbers because lowering is invertible. | Some texts count only the slots allowed by the mixed tensor's last-pair antisymmetry, 96 in four dimensions, which is not a count of independent numbers. Others quote the number of nonzero components of a particular metric, which is a different question. |
| Naming and sign of a surface's single component | $R_{1212} = K\det g$ and $R = 2K$, so a sphere of radius $a$ has $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$, $K = 1/a^2$ and $R = +2/a^2$. | Some texts call the one number the Ricci scalar without the factor 2, or define the Riemann tensor with the opposite overall sign, which flips $R_{1212}$ and $R$ for the same sphere. The count of one is unchanged. |

## Visuals

- ★ [[twenty-of-256-slots]] (flagship): Flagship: the sieve to 0, 1, 6, 20 or 50.
- [[coordinate-knobs-and-metric-dials]] (core): The coordinate-freedom count, order by order. *Sketch:* Three rows for the metric's values, first and second derivatives at a point, each a bar of metric numbers beside a bar of coordinate-change numbers, with a dimension slider from 1 to 5. In four dimensions the rows read 10 against 16 (6 Lorentz parameters spare), 40 against 40, and 100 against 80 (20 survivors, equal to the Riemann count).
- [[falling-ring-of-crumbs]] (supporting): The tide meter: 9 readings, 6 different numbers, 6 of the 20. *Sketch:* A ring of freely falling crumbs near a mass stretches along the line to the centre and squeezes across it. This concept adds a three-arm tide meter whose 3-by-3 table of readings lights mirror pairs together, with counters for 9 readings, 6 numbers and 6 of 20.

## Tutor moves

**Open with**

- Space and time have four directions. How many separate numbers do you think it takes to describe the curving of space and time at one spot? *(prediction)*
- An ant lives inside a knotted piece of string and can only crawl along it with a tape measure. Could it ever find out that its string is knotted or coiled? *(prediction)*

**If the learner is stuck**

- *The learner cannot list the tilts for a given number of directions.* → Name the directions aloud and pair each with every later one, then count: for four directions that is 3 plus 2 plus 1. *Uses:* `ways_in/half-a-times-table`
- *The learner accepts 21 and cannot see where the last number goes.* → Write the three entries that use all four directions and show that any two fix the third; then check that no such group exists with three directions. *Uses:* `ways_in/half-a-times-table`, `checks/twenty-one-or-twenty`

**Common questions**

- *Are all twenty numbers nonzero in real space and time?* (entry) No. Twenty is how many separate numbers the curving at one spot can need. Many of them can be zero at a particular place. Picture someone hovering at rest outside a round star that does not spin. The numbers this person finds that are not zero come in only two sizes, if you ignore plus and minus signs. So few sizes appear because the star looks the same seen from every side, and because the space around the star is empty. *Uses:* `ways_in/half-a-times-table`
- *Why does it matter how many numbers there are?* (entry) It tells you how much you must measure to know the curving at a spot. A tide meter with crumbs at rest reads only six of the twenty. The count also tells you how much curving empty space can hold. Take Einstein's theory in its simplest form, with no dark energy. With only two space directions and time, that theory would leave empty space with no curving at all. In our world, empty space can still need ten separate numbers, half of the twenty. That is why curving does not stop where matter stops. It is also why falling crumbs drift even far above Earth, in space empty of air and of everything else. *Uses:* `ways_in/six-readings-for-the-tides`, `ways_in/empty-space-in-three-and-four-dimensions`

**Switching levels**

- To working when: asks for a formula in any dimension; uses index notation. Go to the pair count and its derivation, then the coordinate ledger. *Uses:* `ways_in/pairs-of-pairs-minus-fours`, `ways_in/what-coordinates-cannot-remove`
- To formal when: asks whether every such tensor is a real curvature; asks about invariants or group decompositions. Open the algebraic curvature tensors way and the boosted-observers check. *Uses:* `ways_in/algebraic-curvature-tensors`, `checks/boosted-observers-disagree`
- To research when: asks about polarizations in other theories, invariant bases, or gravity in three dimensions. Open the research horizon. *Uses:* `research_horizon/wave-polarizations`, `research_horizon/curvature-invariants`, `research_horizon/gravity-in-three-dimensions`

**Pronunciations:** Riemann → REE-mahn; Ricci → REE-chee; Weyl → VILE; Christoffel → KRIS-toff-el; Carminati → car-mee-NAH-tee; McLenaghan → mak-LEN-uh-han

**Voice notes:** Say the formula as 'n squared times n squared minus one, over twelve', then the ladder 'none, one, six, twenty, fifty'. At entry, name tilts by their directions, never by index letters.

## History

- **Bernhard Riemann (1854).** In his 1854 habilitation lecture, published in 1868, argued that a metric in $n$ dimensions has $n(n+1)/2$ component functions, $n$ of which coordinates can fix, and tied curvature to surface directions at a point: a count of functions, not of curvature components at a point. Bernhard Riemann (1868), *Ueber die Hypothesen, welche der Geometrie zu Grunde liegen*, Abhandlungen der Königlichen Gesellschaft der Wissenschaften zu Göttingen 13, 133–152
- **Elwin Bruno Christoffel (1869).** Introduced the four-index quantities, built from the metric and its first and second derivatives, that two quadratic differential forms must match to be transformable into each other: the components of what is now the Riemann tensor. Elwin Bruno Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46–70, doi:10.1515/crll.1869.70.46
- **Hermann Weyl (1918).** Introduced the conformal curvature tensor, now the Weyl tensor: the part of the curvature, with one index raised, unchanged when the metric is rescaled from point to point. Hermann Weyl (1918), *Reine Infinitesimalgeometrie*, Mathematische Zeitschrift 2, 384–411, doi:10.1007/BF01199420

## Research horizon

- **Bases of curvature invariants.** In four-dimensional Lorentzian geometry at most 14 scalar invariants of the Riemann tensor are functionally independent at a generic point, but practical work uses explicit polynomial sets with their relations, such as the Carminati–McLenaghan invariants. Because Lorentz orbits need not be closed, curved spacetimes with every polynomial invariant zero exist, so classification also uses frame components. J. Carminati, R. G. McLenaghan (1991), *Algebraic invariants of the Riemann tensor in a four-dimensional Lorentzian space*, Journal of Mathematical Physics 32, 3135–3140, doi:10.1063/1.529470
- **Polarizations of gravitational waves beyond general relativity.** For a plane wave in a general metric theory, the Riemann tensor is fixed by the 6 components a detector reads, allowing up to six polarization states classified under the little group of a null direction. General relativity keeps two tensor modes. Networks of three or more detectors can separate tensor, vector and scalar modes. Douglas M. Eardley, David L. Lee, Alan P. Lightman, Robert V. Wagoner, Clifford M. Will (1973), *Gravitational-wave observations as a tool for testing relativistic gravity*, Physical Review Letters 30, 884–886, doi:10.1103/PhysRevLett.30.884; B. P. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101
- **Gravity in two space dimensions and time.** Because Ricci fixes Riemann in three dimensions, vacuum Einstein gravity there is locally flat: point masses make conical deficits, and there are no local degrees of freedom or waves. Global structure remains, and the theory can be written as a Chern–Simons gauge theory, a testing ground for quantum gravity. Stanley Deser, Roman Jackiw, Gerard 't Hooft (1984), *Three-dimensional Einstein gravity: dynamics of flat space*, Annals of Physics 152, 220–235, doi:10.1016/0003-4916(84)90085-X; Edward Witten (1988), *2 + 1 dimensional gravity as an exactly soluble system*, Nuclear Physics B 311, 46–78, doi:10.1016/0550-3213(88)90143-5

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** Second novice read, of revision 4, before fixes. What I would say back: "There is a table of numbers at every spot that says how an arrow comes back changed after you carry it round a tiny loop. To count how many numbers you really need you do it like a times table. A tilt is a pair of two different directions; four directions make six tilts; so the grid is 6 by 6, or 36 boxes. Swapping the row tilt with the column tilt gives the same number, so you keep the 6 boxes where a tilt meets itself and half of the other 30, which is 21. Then the cyclic identity takes one more away, so 20. On a surface it is 1 and in space it is 6. A string has no tilts at all, so it needs no numbers, however knotted it is: an ant inside could never tell, because pulling the string straight keeps every distance along it. Last was a falling box with three arms and a crumb on each, called a tide meter. It makes 9 readings, the sideways ones pair up because there is no whirlpool, and that leaves 6 numbers, which are 6 of the 20." Three things I could not say back. I could not say how 3 equal pairs turn into 6 separate numbers; I just accepted the 6. I could not say which of the three arms was the up arm without going back. And I lost the sentence listing the three boxes the cyclic identity links, because it has three "with"s in a row. Against the takeaways: I matched "Half a times table" and "A coiled string has nothing to count" well, and "Six readings for the tides" only in its numbers, not in its reasons.

**Stumbles (42)**

- “Most entries are copies, opposites or zeros of others.”: 'Zeros of others' means nothing, and the sentence hides the cyclic link, which is neither a copy nor an opposite.
- “On a surface one number is enough, in space six, and in space and time twenty.”: 'Space' alone sits next to 'space and time', so the reader is unsure which world has six.
- “The table's first rules leave one entry for each pairing of an arrow's tilt with a loop's tilt.”: 'First rules' names nothing, and the explanation uses the mirror rule and the cyclic identity without restating them, so the recap does not make the way self-sufficient.
- “So you only need the 6 answers where a number meets itself”: 'A number meets itself' needs an example before the reader can picture it.
- “Pairing different directions gives six tilts”: A count taken on trust; a teenager wants to check that nothing is missing.
- “ahead with time”: The prerequisite pictures a tilt as the bottom, front or side of a box, and no box has a side made of time.
- “Each entry pairs an arrow's tilt, its row, with a loop's tilt, its column. So the table is 6 by 6, with 36 entries.”: One word for two ideas: 'table' and 'entry' mean the 256-entry curvature table in the check and the 36-box grid here, so 256 and 36 seem to contradict each other.
- “The cyclic identity ties together three entries that use all four directions.”: A missing step: the reader cannot tell why the mirror rule had not already tied these three together.
- “Space and time have only one group of four different directions, so one more number goes.”: No reason for 'only one group', and the jump from 'any two fix the third' to 'one number goes' is left implicit.
- “Count the tilts. Keep the entries where a tilt meets itself, and half of the rest.”: The recipe skips the step of making the grid, so 'entries where a tilt meets itself' has no grid to live in.
- “A world with 5 directions has 10 tilts: 10 plus 45 is 55, and 5 groups of four leave 50.”: Two counts taken on trust (10 tilts, 5 groups of four) packed into one line; the reader rereads it twice.
- “Some of them can be zero at a spot, and on a flat floor all are.”: 'Them' is ambiguous, and a flat floor is a surface while the sentence follows the space-and-time count.
- “Cross out each box whose two tilts appear, swapped, in a box you kept.”: The rule depends on the order you visit the boxes, which is not given, so two readers can cross out different boxes.
- “Count the tilts, keep the entries where a tilt meets itself and half the rest, and remove one per group of four directions. That gives 1 number on a surface, 6 in space and 20 in space and time.”: The rewritten takeaway ran to 38 words in one sentence, too long to say back.
- “The curvature table agrees.”: A table cannot agree; the reader stops to work out what is meant.
- “A surface is different. A piece of orange peel cannot be pressed flat without tearing or stretching, and a surface's 1 number shows that.”: False for the first what-if, a rolled paper tube, which is a surface that unrolls flat; and 'shows that' is unclear.
- “When the planet's gravity does not change with time, tidal drift forms no whirlpool.”: The recap names the no-whirlpool rule without saying what it means for the crumbs, and it does not restate the mirror rule or a tilt, which the explanation uses.
- “Three arms, each 1 metre long, stick out from its centre at right angles: ahead, left and up.”: 'Up' has no meaning for someone falling freely, and 'ahead' has no reference for a box.
- “Picture a small box falling freely near Earth, without turning.”: 'Turning' is the prerequisites' word for an arrow coming back changed, and the tides prerequisite says the room 'does not spin'.
- “so the three crumbs give 3 times 3, or 9, readings”: 'Reading' is never defined, and no measurer is named.
- “6 different readings remain”: Two words for one idea: 'different' here and in the check, 'separate' in the summary check and misconception.
- “The other six are sideways drifts.”: A false first what-if: the recap says crumbs drift only along and across the line to the planet's centre, so near Earth the reader finds no sideways drift at all.
- “Each of the 6 is an entry of the curvature table that pairs two tilts using time: time with the crumb's arm, and time with the direction of its drift.”: Reread twice: the link from a drift to a table entry is taken on trust without saying so, and 'this corner' has no grid to sit in.
- “Each of the other 14 uses a tilt without time, and none of them changes how crumbs at rest drift.”: A surprising claim with no reason, in the way and in the check answer.
- “Two crumbs 1 metre apart, one above the other, drift apart by about 15 hundredths of a millimetre in 10 seconds.”: 'Above' has no meaning in free fall, no measurer is named, and the number has no everyday feel.
- “They are the entries of the 2 tilts that use time, whose grid keeps 2 plus 1, or 3: half of the 6.”: Reread: 'whose grid' has two candidates, and 'no group of four' in the first step gives no reason.
- “No. Two rules leave one entry for each pairing of an arrow's tilt with a loop's tilt.”: The check answer's chain starts from unnamed rules, so its first because-step is missing.
- “In our world, half of the twenty can exist in empty space, and they make the tides the Moon raises on Earth.”: 'Exist' is vague for a number, and Earth itself is not empty space.
- “Go through the boxes row by row from the top, left to right in each row.”: Second novice read. The same try_it labels a tilt "ahead-left", so "left" is a named direction here; "left to right" then uses the same word for a direction across the page. That is one word in two senses (rule 5), in the one place the reader is handling direction names.
- “They pair ahead-with-left with up-with-time, ahead-with-up with left-with-time, and ahead-with-time with left-with-up.”: Second novice read. Each item is itself an "A with B", so the sentence nests "with" inside "with" six times. I had to reread it to see where one tilt ended and the next began.
- “Now make a grid of the numbers that fix the table.”: Second novice read. "A grid of the numbers that fix the table" names the grid by something the reader does not have yet, and the way's own takeaway and try_it both call it a grid of tilts. Two names for one thing (rule 5).
- “then remove one per group of four directions”: Second novice read. The explanation says "four different directions"; the takeaway drops "different". A general sentence then fails the first what-if a reader tries: in space you can pick four directions with one repeated, and the takeaway would have them remove a number, giving 5 instead of 6.
- “- Space and time: 21 minus 1, or 20 numbers.”: Second novice read. The other two bullets read "has 2 directions and 1 tilt" and "has 3 directions and 3 tilts"; this one drops the pattern, so a reader checking the recipe on the bullets alone cannot see where 21 came from.
- “On a ball, the surface's 1 number is not zero, and it records exactly that.”: Second novice read. "It" could be the number or the ball's surface, and "that" points at a whole previous clause rather than a noun (rule 11). "Records exactly that" also leaves the reader unsure whether the number says the peel tears, or says how much.
- “One arm points away from Earth's centre, and the other two point across that line. Call them the up arm, the ahead arm and the left arm; these are only names.”: Second novice read. "Call them" names all three arms at once, so which arm is the up arm rests on word order alone. I had to read on to the sideways-drift paragraph to find out.
- “So the sideways drifts come in 3 equal pairs, and 6 separate numbers remain.”: Second novice read. The arithmetic is left to the reader: 3 pairs give 3 numbers, and the 3 drifts along the crumbs' own arms give 3 more. The sentence joins the two halves with "and", so nothing says the 6 is 3 plus 3, and the grid paragraph only confirms it two paragraphs later.
- “That is about the thickness of a sheet and a half of paper, which is why you never notice it.”: Second novice read. "It" should be the drift, but the nearest nouns are the thickness and the paper, so the sentence reads for a moment as though the paper is what goes unnoticed (rule 11).
- “the part of the 20-number curvature table that sets how crumbs at rest drift”: Second novice read. "At rest" has no reference here (rule 7). The explanation says "let go at rest in the box", but the takeaway is the sentence a reader carries away, and at rest relative to Earth's surface would be a different thing.
- “A crumb at rest moves only through time, so only boxes whose row and column both use time decide its drift.”: Second novice read, in the check "what-the-tide-meter-misses" and again in the misconception "tides-show-all-the-curving". Same missing reference for "at rest" (rule 7), and here the reader has no explanation paragraph beside it to supply the box.
- “the lean rule flips it when the arrow's two directions swap”: Second novice read. "The lean rule" is named in the recap of "Half a times table" and again in the check "guess-256", but this note's glossary does not define it, although it defines the mirror rule and the cyclic identity. A reader who has not just come from the prerequisite meets a named rule with no entry to look up.
- “So few sizes appear because the star looks the same in every direction.”: Second novice read, in the common question "are-all-twenty-nonzero". "Looks the same in every direction" gives a direction with no place to look from (rule 6); it can be read as looking out from the star rather than at it.
- “How many numbers the curving at one spot can need: 1, 6 or 20”: Second novice read. The summary and the whole way "A coiled string has nothing to count" say a line needs none, so the tagline's list of three left me looking for the zero.

**Fixes**

- Summary, the three entry ways, the entry glossary, objective, checks, misconceptions, problem, teaching-arc prediction and common question rewritten as the stumbles record.
- Introduced 'grid' and 'box' for the 6-by-6 array of tilt pairings, keeping 'table' and 'entry' for the full curvature table, in the way, the try-it, the tide meter way and the flatland problem.
- Unified 'separate numbers' for independent counts across the entry rung; 'different' now only means distinct directions.
- Glossary 'tilt' now says a tilt can pair time with a direction of space.
- Ladder bridge: 'Pairs of pairs, minus one per four indices' now says a tilt such as ahead-with-left becomes the unordered index pair {1,2} and each box of the grid a component.
- Dropped for budget (entry explanations were 1198 words against the 1100 review allowance): the five-direction bullet in 'Half a times table' (the working way and the flagship visual carry 50), the loop-on-a-string-encloses-nothing sentence in 'A coiled string has nothing to count' (the no-tilts reason already carries it), the sentence 'It looks bent in many places' in the same way (coiling and knotting already show it), and in 'Six readings for the tides' the sentence on crumbs sent moving across the box and the sentence 'the count is about what the readings can be'.
- Revision bumped from 1 to 2; status novice-reviewed.
- Second novice read (revision 4 to 5), 14 stumbles, 13 applied. This record keeps the first novice read's 28 stumbles and 7 fixes and its re-read; only retell_attempt was replaced, because the first one retold text that later revisions no longer contain.
- Way "Half a times table": de-nested the cyclic-identity pairing sentence to the hyphenated tilt names the way's own try_it already uses; renamed the grid "a grid of tilts", matching the takeaway and try_it; rewrote the try_it's traversal so "left" is not used both as a direction name and as a way across the page; added "different" to the takeaway's group of four directions. No count, rule or number changed.
- Way "A coiled string has nothing to count": replaced "it records exactly that" with a named consequence, that the 1 number is why the peel cannot lie flat. The claim is the same one the previous sentence makes about the orange peel.
- Way "Six readings for the tides": named the up arm in its own sentence; made the 3 plus 3 arithmetic explicit where the 6 first appears; replaced "never notice it" with "never notice the drift"; said "at rest in the box" in the takeaway. The readings, the pairs and the 0.154 millimetre drift are unchanged.
- Check "what-the-tide-meter-misses" and misconception "tides-show-all-the-curving": said "at rest in the box", the frame the explanation uses.
- Common question "are-all-twenty-nonzero": "looks the same seen from every side" instead of "in every direction", so the viewpoint is outside the star. The two sizes and the reason are unchanged.
- Glossary: added "lean rule", defined in this note's own words, because the entry reading names it twice without defining it.
- Tagline: added the 0, so it agrees with the summary and with the coiled-string way.
- Not applied, and recorded as a stumble only: the third recipe bullet's missing "4 directions and 6 tilts". The entry rung sits at 1099 words against a cap of 1000 plus the 10% review allowance, and that bullet is the lowest-value fix of the fourteen, because the paragraphs above it derive 36 to 21 to 20 in full. Applying it would cost 6 words and push the rung over. Room for it came only from trims that were themselves fixes; no sentence was compressed to fit.

**Concerns**

- Physics reviewer: confirm the entry simplifications added in 'Six readings for the tides' and its check: a crumb at rest 'moves only through time', so only boxes whose row and column both use time (the components R_{0i0j}) decide its drift, and each of the other 14 has a row or a column without time.
- Physics reviewer: confirm the sideways-drift what-if: with one arm along the radial direction of a spherical Earth the off-diagonal tidal readings are zero, and a slanted frame or a lumpy source makes them nonzero.
- Physics reviewer: confirm the rewritten common answer that the Weyl part in the empty space around the Moon produces the tidal drift that raises tides on Earth.
- This note's glossary says an arrow's tilt uses 'the direction its change is read in', while the prerequisite notes say 'the direction its lean is read in'. The entry ways here never use 'lean', so I kept 'change'; an editor may want to align them across notes.
- The five-direction count, 50, no longer appears at entry; the working problem five-dimensions-both-ways and the flagship visual carry it.
- Second novice read: revision 5 changes 12 learner-visible strings, all at the entry rung, so review.physics still covers revision 4 and the validator warns. A physics diff check is needed on exactly those strings before an editor publishes. The two claims worth checking are the rewording "the star looks the same seen from every side" and "which is why the peel cannot lie flat", both intended to say what the previous wording said.
- Second novice read: the entry rung is now 1099 words against the 1100-word review ceiling, so the next reader has one word. Any further entry fix must drop or shorten something and say which; the third recipe bullet's rewrite is the first candidate for the room.
- Second novice read: "A crumb at rest in the box does not move through space; it moves only through time" is still the one entry claim a reader can only take on trust. The paragraph flags the grid mapping as taken on trust, but not this. Giving it a reason needs room the entry rung does not have; an editor could move it behind the trust flag in one sentence when room appears.

**Re-read** (2026-09-13, revision 4): 6 stumbles in 4 changed passages

- “someone hovering at rest finds only two different sizes among them”: 'Them' could mean the twenty numbers or the many that are zero, and 'sizes' is unexplained: the reader cannot tell whether zero counts as a size, or whether a number and its negative are the same size. A long sentence also hides the 'because' link at its end.
- “It also tells you what empty space can hold.”: 'It' follows a sentence about the tide meter, so the pronoun has two candidates (rule 11), and 'what empty space can hold' is vague.
- “Einstein's theory, in its simplest form with no dark energy, would leave empty space with no curving at all.”: Squeezed: the scope is wedged into the middle of the sentence as a second clause, so the reader holds 'dark energy' and 'two space directions and time' before reaching the verb.
- “In our world, empty space can still need ten separate numbers.”: 'Ten' arrives with no link to the twenty the whole note counts, so the reader takes it on trust as an unrelated number.
- “why falling crumbs drift even far above Earth, where no air is left”: Naming only air suggests the drift has something to do with air, rather than showing that the space is empty of all matter; the two 'why' reasons are also joined in one long sentence.
- “while $g_{\rho\sigma}(x)$ changes only at fourth order, because $\partial g(p) = 0$”: For a second-year student, 'changes' names no comparison, and the step from $\partial g(p) = 0$ to fourth order skips that the cubic shift multiplies $\partial g$, which is first order near $p$.
- Fix: Common question are-all-twenty-nonzero: split the hovering-observer sentence and said the two sizes are of the nonzero numbers with signs ignored, which is the physics review's meaning (magnitudes 2GM/c^2r^3 and GM/c^2r^3 in the static frame); claim unchanged.
- Fix: Common question why-the-count-matters: replaced the ambiguous 'It', moved the no-dark-energy scope into its own sentence, tied ten to half of the twenty, and split the two consequences; scope, numbers and claims unchanged.
- Fix: Derivation what-coordinates-cannot-remove step 2: named what is compared, $g(x) - g(x')$, and gave the reason it is fourth order.
- Fix: Revision bumped from 3 to 4; status kept physics-reviewed. Nothing dropped: tutoring words stay under the cap.

**Re-read** (2026-09-13, revision 7): 5 stumbles in 6 changed passages

- “A piece of orange peel cannot be pressed flat without tearing or stretching. On a ball, the surface's 1 number is not zero, which is why the peel cannot be pressed flat.”: The second sentence repeats the first one's words but drops its condition, so 'the peel cannot be pressed flat' reads as a new and stronger claim, and I went back to check whether the tearing had been withdrawn. The entry way is also exactly at its word allowance, so nothing can be added here.
- “So few sizes appear because the star looks the same seen from every side, and because the space around it is empty.”: Spoken to me, 'around it' can attach to the star or to the side just named, and a listener cannot look back (rule 11). The second reason also arrives with no link I can check: I am told empty space is a reason for few sizes, while the same voice tells me empty space can hold curving.
- “$\approx -3.4\times10^{-23}\ \mathrm{m^{-2}}$, which times $c^2$ is the vertical gravity gradient that gradiometers read”: A clause squeezed in to carry the $c^2$: 'which' points at a number and an equation at once, and the multiplication is over before I know a conversion is happening, so I stopped to work out what is multiplied by what.
- “Three dimensions, either signature; it holds on a surface too, but is false in four or more.”: Every other count in the line is a dimension, and 'a surface' is the only one left as a picture, so I had to translate it to two before I could place it between three and four. 'It' also sits between two nouns.
- “By the geodesic deviation equation in the course conventions, that negative component is a stretch along the radius.”: Two qualifiers come before the subject, so the sentence that reads the sign of the component just displayed starts by pointing somewhere else, and 'that negative component' lands far from the formula it names.
- Fix: Entry way a-coiled-string-has-nothing-to-count: the peel sentence now says the tearing or stretching happens because the surface's 1 number is not zero, instead of repeating 'cannot be pressed flat' without its condition. Same claim in the same direction; 3 words shorter, which was necessary because entry way explanations sat exactly at the cap plus the 10 per cent review allowance (1,100 words) and are now 1,097.
- Fix: Common question are-all-twenty-nonzero: 'the space around it' became 'the space around the star'. Spoken answer, so the noun is repeated rather than pronouned; both reasons and their scope are unchanged.
- Fix: Check empty-space-three-and-four: 'which times $c^2$ is the vertical gravity gradient' became 'and $c^2$ times this component is the vertical gravity gradient'. The value, the factor and the identification are word-for-word the same claim; only the clause is unpacked.
- Fix: Key equation riemann-from-ricci-in-three-dimensions, conditions: 'it holds on a surface too' became 'it also holds in the two dimensions of a surface', so the line reads three, two, four in the same units. Scope unchanged: true in two and three dimensions, false in four or more.
- Fix: Working way empty-space-in-three-and-four-dimensions: the geodesic deviation sentence was reordered so the statement comes first and the rule that licenses it follows. Same words, same claim, and it now sits next to the formula it reads.
- Fix: Nothing dropped. Entry 1,097 of the 1,000 cap plus allowance, working 675, support about 1,903 of 2,300, tutoring about 2,844 of 3,300.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- N_R(n) = n^2(n^2-1)/12 = N(N+1)/2 - C(n,4) = [n(n+1)/2]^2 - n^2(n+1)(n+2)/6: 0, 1, 6, 20, 50.: Exact rational rank computation in python of the linear system (both pair antisymmetries, pair exchange, cyclic identity) on all n^4 components for n = 1 to 4; the three closed forms evaluated for n = 1 to 5; derivation pairs-minus-fours redone by hand. → Brute-force dimensions 0, 1, 6, 20 match all three forms; n = 5 gives 55 - 5 = 225 - 175 = 50. Correct.
- Cyclic identity gives a new condition only for four distinct indices; one relation per index set; fixing b, c or d gives the same relation up to sign.: Hand check of the sums with sigma = mu and rho = sigma; permuted first index reduced with pair exchange and antisymmetries. → Correct; the permuted relation is minus the original.
- Check twenty-one-or-twenty: a tensor with only R_0123 and its pair-symmetry partners violates the cyclic identity.: Direct evaluation: R_0231 and R_0312 belong to other pair entries and vanish, so the sum is R_0123. → Correct.
- Worked example: R_1030 = R_0103 and R_0312 = R_0213 - R_0123.: Checked on a random integer algebraic curvature tensor built from Kulkarni-Nomizu products in python. → Both hold exactly.
- Coordinate ledger: third-order shift delta(d_a d_b g_mn) = A_mnab + A_nmab is injective and leaves the Riemann tensor at p unchanged.: Re-derived the Jacobian and shift by hand, re-chained the six swaps of the injectivity proof, computed the rank of the shift map for n = 3 exactly (30), and applied the four-term second-derivative Riemann formula to a random symmetrized shift in n = 4. → Correct. One slip fixed: with dg(p) = 0 the metric g(x(x')) differs from g(x') at fourth order, not third.
- Four-term formula R_rsmn = 1/2(d_m d_s g_rn - d_m d_r g_sn - d_n d_s g_rm + d_n d_r g_sm) where Gamma = 0, in course conventions.: Derived from the course Riemann row with Gamma_rns = 1/2(d_n g_rs + d_s g_rn - d_r g_ns). → Matches the note's hint and solution.
- Realization: g = eta - (1/3) R_manb x^a x^b has Riemann tensor R at the origin; S = -6R.: Exact rational computation in python for a random algebraic curvature tensor in n = 4, plus the solution steps by hand. → Recovers R exactly; the -4R and -2R split in the solution is correct.
- P(S) has Ricci contraction (n-2)S + (tr S)g; the 3D formula R_rsmn = P(Ric) - (R/2)(g g - g g) in either signature; Weyl count n(n+1)(n+2)(n-3)/12.: Exact python checks with Euclidean and Lorentzian diagonal metrics for random curvature tensors and random S; algebra of the kernel dimension by hand. → All exact; Weyl counts 0, 10, 35 for n = 3, 4, 5; 15 Ricci plus 35 Weyl in five dimensions.
- Hyperbolic plane: R_{r phi r phi} = -sinh^2 r, K = -1.: Christoffel symbols by hand; course Riemann definition evaluated in python at r = 0.7. → -0.57545 = -sinh^2(0.7); K = -1.000. Correct.
- Sphere R_{theta phi theta phi} = a^2 sin^2 theta, det g = a^4 sin^2 theta, K = 1/a^2, R = 2K; normal-coordinate sign.: Hand computation; normal-coordinate metric in 2D gives g_22 = 1 - K x_1^2/3, the shrinking circumference of a sphere. → Correct, matches the conventions row R = +2/a^2.
- R_{r0r0} (hatted, static frame) = -2GM/c^2 r^3 = -3.4e-23 per square metre at Earth's surface; E_ij = c^2 R_{i0j0} = d_i d_j Phi.: Geodesic deviation row with u^0 = c compared with Newtonian deviation; python with GM = 3.986e14, r = 6371 km. → 3.43e-23; sign and factor c^2 correct; exact Schwarzschild static-frame value is also -2M/r^3.
- GOCE numbers at r = 6626 km: -2.74e-6 and +1.37e-6 per second squared, trace zero.: python. → 2.740e-6 and 1.370e-6. Correct.
- Entry tide meter: up crumb drifts about 15 hundredths of a millimetre in 10 seconds on a 1 metre arm; a sheet and a half of paper.: python: (1/2)(2GM/R^3)(1 m)(10 s)^2. → 0.154 mm; paper is about 0.1 mm. Correct.
- Entry: a crumb at rest moves only through time, so only boxes whose row and column both use time (R_{0i0j}) decide its drift; the other 14 have a row or a column without time.: Geodesic deviation for u = e_0 in a non-rotating freely falling frame; listed the 20 as 6 (0i,0j) + 8 (0i,jk) after the one cyclic relation + 6 (ij,kl). → Correct to first order in the tiny drift velocities; the 9 readings give the whole symmetric E_ij.
- Entry: with one arm along the radius of a round Earth the sideways drifts are zero; slanted arms or a lumpy moon make them nonzero.: E_ij for Phi = -GM/r is diagonal in the radial-tangential frame; a rotated frame or a non-spherical potential has off-diagonal entries. → Correct.
- Entry counts: 6 tilts, 36 boxes, 21 after the mirror rule, 20 after the cyclic identity; flatland 6 numbers, 4 readings, 3 separate; try-it keeps 6 of 9 boxes.: Hand enumeration, including the row-by-row crossing order of the try-it. → Correct.
- Entry summary 'Rules make most entries zero, or copies or opposites of other entries'.: Counted in four dimensions: 112 of 256 vanish by antisymmetry, 144 fall into 36 sign-classes, then 21, then 20. → True; the single cyclic link is correctly not called a copy.
- Common answer 'half of the twenty can be nonzero in empty space'.: Vacuum imposes 10 linear conditions; in a generic frame all 6 E_ij entries and the others can be nonzero. → False as worded (numbers nonzero is not numbers independent). Rewritten: empty space can still need ten separate numbers.
- Common answer on a round star: 'only a few different values appear'.: Schwarzschild static orthonormal frame: R_trtr = -2M/r^3, R_tθtθ = R_tφtφ = M/r^3, R_θφθφ = 2M/r^3, R_rθrθ = R_rφrφ = -M/r^3. → True only outside the star and in a named frame; rescoped to someone hovering at rest outside it, two sizes.
- Invariant bound n(n-1)(n-2)(n+3)/12: 3 for n = 3, 14 for n = 4; plane waves have all polynomial invariants zero; compact groups separate orbits by invariants.: Dimension of generic orbits equals dim O(g) when the stabilizer is discrete; standard results on VSI spacetimes and compact group actions. → Correct.
- Plane waves in a metric theory: Riemann fixed by the 6 R_{i0j0}, at most 6 polarizations; GR has 2; GW170814 favoured pure tensor over pure vector and pure scalar.: Known Eardley et al. result; GW170814 paper record. → Correct.
- References: Rummel, Yi, Stummer 2011 (J Geod 85, 777–790, doi 10.1007/s00190-011-0500-0); Christoffel 1869 (J. reine angew. Math. 70, 46–70, doi 10.1515/crll.1869.70.46); Riemann 1868 (Abh. Ges. Wiss. Göttingen 13); Weyl 1918; Carminati and McLenaghan 1991; Eardley et al. 1973; Abbott et al. 2017 GW170814; Deser, Jackiw, 't Hooft 1984; Witten 1988.: Crossref records fetched for Weyl (10.1007/BF01199420, Math. Z. 2, 384–411), Carminati–McLenaghan (10.1063/1.529470, JMP 32, 3135–3140), Witten (10.1016/0550-3213(88)90143-5, NPB 311, 46–78), Eardley et al. (PRL 30, 884–886, five authors), GW170814 (PRL 119, 141101); EuDML record for Riemann; GOCE, Christoffel and Deser–Jackiw–'t Hooft (10.1016/0003-4916(84)90085-X) match physics-verified entries in other vault notes. → All confirmed; Riemann page range corrected to 133–152; DOIs added; verified set true.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). N_R(n) = n^2(n^2-1)/12 equals both N(N+1)/2 - C(n,4) and [n(n+1)/2]^2 - n^2(n+1)(n+2)/6, giving 0, 1, 6, 20, 50.: Exact rational Gaussian elimination in python on the full linear system (both pair antisymmetries, pair exchange, cyclic identity) over all n^4 components for n = 1 to 4, independent of the earlier run; the three closed forms evaluated for n = 1 to 5; the algebra of derivation pairs-minus-fours redone by hand over the denominator 24. → Brute-force dimensions 0, 1, 6, 20. All three forms agree, and n = 5 gives 55 - 5 = 225 - 175 = 50. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). The cyclic identity is a new condition only for four distinct indices, exactly one per index set.: Re-ran the same rank computation with the cyclic rows dropped; checked by hand that the cyclic sum vanishes identically when sigma, mu or nu repeat (last-pair antisymmetry) and when rho equals one of them (pair exchange); re-derived the permuted relation with free index b. → Without the cyclic rows the counts are 0, 1, 6, 21, so it removes exactly one number in four dimensions and none below. The b-relation is minus the a-relation. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Entry arithmetic: 3 + 2 + 1 = 6 tilts, 36 boxes, 21 after the mirror rule, 20 after the cyclic identity; the try-it keeps 6 of 9 boxes read row by row; the recipe gives 0, 1, 6, 20.: Hand enumeration of the 3-by-3 and 6-by-6 grids, following the try-it's stated order (top row first, each row from its first box to its last). → Correct: the kept boxes are the upper triangle with its diagonal, 3 + 3 = 6 of 9.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). The three boxes the cyclic identity ties are ahead-left with up-time, ahead-up with left-time, and ahead-time with left-up, and they lie in three different mirror pairs.: Named ahead, left, up, time as 1, 2, 3, 4 and wrote R_1234 + R_1342 + R_1423 = 0; listed the pair labels (12,34), (13,24), (14,23) and their mirrors. → Correct; the three entries sit in three distinct mirror pairs, so the mirror rule does not relate them and the cyclic identity is what removes the twenty-first number.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Worked example: R_1030 = R_0103 and R_0312 = R_0213 - R_0123; the list is 6 diagonal plus 14 off-diagonal pair entries.: Sign chain by hand through first-pair and last-pair antisymmetry; cyclic sum for rho = 0 solved for R_0312; counted C(6,2) = 15 off-diagonal entries minus the dropped one. → Both identities hold, and 6 + 14 = 20. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Coordinate ledger: 10 against 16, 40 against 40, 100 against 80; the third-order shift A_{mu nu alpha beta} + A_{nu mu alpha beta} is injective; the general identity closes.: Counts recomputed from n(n+1)/2, n*n(n+1)/2, [n(n+1)/2]^2, n^2, n^2(n+1)(n+2)/6; the six-swap injectivity chain re-run index by index; the identity [n(n+1)/2]^2 - n^2(n+1)(n+2)/6 factored by hand to n^2(n+1)(n-1)/12. → All counts correct, 16 - 10 = 6 Lorentz parameters spare, 100 - 80 = 20; the chain ends at A = -A; n = 1 gives 1 - 1 = 0 and n = 2 gives 9 - 8 = 1. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Where Gamma(p) = 0, R_{rho sigma mu nu} = (1/2)(d_mu d_sigma g_{rho nu} - d_mu d_rho g_{sigma nu} - d_nu d_sigma g_{rho mu} + d_nu d_rho g_{sigma mu}) in course conventions, and g = eta - (1/3)R x x realizes any algebraic curvature tensor.: Derived the four-term formula from the course Riemann and Christoffel rows; expanded the realization metric's second derivatives and collected the eight terms of S by hand, using pair exchange, both antisymmetries and the cyclic identity. → Formula matches the problem's hint; the four pair terms give -4R, the other four give -2R, S = -6R and R' = R. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Normal-coordinate sign: g_{mu nu} = eta_{mu nu} - (1/3)R_{mu alpha nu beta}x^alpha x^beta reproduces the sphere.: For a sphere of radius a took R_{1212} = 1/a^2 and compared g_22 = 1 - x^2/(3a^2) with the exact geodesic-polar value (a sin(r/a)/r)^2 expanded to second order. → Both give 1 - r^2/(3a^2). The sign is right in the course conventions.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). P(S) has Ricci contraction (n-2)S + (tr S)g, is inverted by S = (Q - tr Q g/(2(n-1)))/(n-2), and the three-dimensional formula contracts back to the Ricci tensor.: Contracted P(S) with g^{rho mu} term by term; solved the trace condition for the coefficient 1/(2(n-1)); contracted the note's explicit three-dimensional formula with g^{rho mu} and set n = 3; checked P(g) = 2(gg - gg) and the step S = Ric - (R/4)g. → Contraction gives (n-2)S_{sigma nu} + (tr S)g_{sigma nu}; the general contraction is (n-2)R_{bd} + Rg_{bd} - (R/2)(n-1)g_{bd}, which is R_{bd} exactly at n = 3. All steps correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). The three-dimensional formula also holds on a surface, so the key equation's condition 'exactly three dimensions' was too narrow.: Substituted R_{mu nu} = (R/2)g_{mu nu} for n = 2 into the formula: P(Ric) = R(gg - gg) and the -R/2 term leaves (R/2)(gg - gg), the true two-dimensional Riemann tensor. → Identity holds at n = 2. Condition reworded to say it holds on a surface too and fails only from four dimensions up.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Hyperbolic plane problem: R_{r phi r phi} = -sinh^2 r, K = -1, and every nonzero lowered component is plus or minus sinh^2 r.: Christoffel symbols by hand (Gamma^r_{phi phi} = -sinh r cosh r, Gamma^phi_{r phi} = coth r); the course Riemann definition evaluated numerically in python by finite differences at r = 0.7. → R^r_{phi r phi} = -0.5754491 against -sinh^2(0.7) = -0.5754492; det g = sinh^2 r, K = -1.0000. Correct, and opposite in sign to the unit sphere.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Sphere of radius a: R_{theta phi theta phi} = a^2 sin^2 theta, det g = a^4 sin^2 theta, K = 1/a^2, R = 2K = +2/a^2.: Course Riemann definition with Gamma^theta_{phi phi} = -sin theta cos theta and Gamma^phi_{theta phi} = cot theta, by hand. → R^theta_{phi theta phi} = sin^2 theta, so R_{theta phi theta phi} = a^2 sin^2 theta and K = +1/a^2. Matches the conventions row.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Outside a static round star a static orthonormal frame shows six nonzero pair entries with magnitudes M/r^3 and 2M/r^3, with G = c = 1.: Numerical Christoffel and Riemann by finite differences in python for the exterior metric at M = 1, r = 7, theta = 1.1, projected onto the static orthonormal frame over all six index pairs. → R_trtr = -2M/r^3, R_t theta t theta = R_t phi t phi = M/r^3, R_r theta r theta = R_r phi r phi = -M/r^3, R_theta phi theta phi = 2M/r^3: six entries, two magnitudes. Correct. The way had no units statement, so 'with G = c = 1' was added.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). The two magnitudes need empty space as well as the star's symmetry, so the entry answer's single reason was incomplete.: Ran the same numerical frame computation for a static spherically symmetric non-vacuum metric (Phi = 0.1r^2, Lambda = 0.07r^2, r = 1.3) and for the uniform-density interior solution. → The non-vacuum case gives four distinct magnitudes (0.1105, 0.1247, 0.1579, 0.1739); the uniform-density interior happens to give two. The entry answer now names empty space as well, and the formal way says 'inside a star of varying density' to exclude the uniform case.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). R_{hat r hat 0 hat r hat 0} = -2GM/c^2 r^3 is a stretch along the radius, and equals -3.4e-23 per square metre at Earth's surface; E_ij = c^2 R_{hat i hat 0 hat j hat 0} = d_i d_j Phi.: Course geodesic deviation row with u = e_hat 0: D^2 xi^r/dtau^2 = -R^r_{0r0} xi^r, so a negative lowered component is a positive outward relative acceleration; python with GM = 3.986004418e14 and r = 6371 km; dimensions checked (GM/c^2 is a length, so the component is an inverse square length). → -3.430e-23 per square metre, and the negative sign is indeed the radial stretch. The way now names the convention, and the check now says the component times c squared is the gradient, since the two differ by c squared.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Entry tide meter: about 15 hundredths of a millimetre in 10 seconds on a 1 metre arm, about a sheet and a half of paper.: python: (1/2)(2GM/R_E^3)(1 m)(10 s)^2, and the exact cosh solution for comparison. → 0.15414 mm by the quadratic form and 0.15414 mm exactly; office paper is about 0.1 mm a sheet. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). GOCE observation: -2.74e-6 and +1.37e-6 per second squared at r = 6626 km, summing to zero; the gradiometer reads 6 of the 20 components, 5 outside matter.: python with Phi = -GM/r; trace of d_i d_j Phi in vacuum; symmetry of E_ij from pair exchange. → -2.7404e-6 and +1.3702e-6, trace exactly zero. Six symmetric entries, five once the trace is removed. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). A tide meter reads 6 of the 20 numbers, and each of the other 14 has a pair without time.: Listed the 20 as the six (0i,0j) entries, the eight surviving (0i,jk) entries after the single cyclic relation, and the six (ij,kl) entries; checked that the cyclic relation involves only mixed entries, so the six time-time entries stay independent. → 6 + 8 + 6 = 20 and the six E-entries are untouched by the cyclic relation. Correct, to first order in the drift velocities.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Flatland problem: 6 numbers in two space dimensions and time, 4 readings, 3 separate, half the table.: Hand count with n = 3: three tilts, 3 + 3 = 6 numbers, C(3,4) = 0; two arms drifting two ways give 4 readings; the time corner is 2 by 2, leaving 2 + 1 = 3. → Correct, and 3 is half of 6.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Five-dimensions problem: 55 - 5 = 225 - 175 = 50 = 15 Ricci + 35 Weyl.: python arithmetic on N(N+1)/2, C(5,4), [n(n+1)/2]^2, n^2(n+1)(n+2)/6, n^2(n^2-1)/12, n(n+1)/2 and n(n+1)(n+2)(n-3)/12. → All five numbers reproduce; Weyl counts are 0, 10, 35 for n = 3, 4, 5 by both the subtraction and the closed form. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Invariant bound n(n-1)(n-2)(n+3)/12: 3 for n = 3 and 14 for n = 4; on a surface the subtraction would be wrong.: Checked the algebra against n^2(n^2-1)/12 - n(n-1)/2; dim O(1,3) = 6 and dim O(2) = 1; noted that a generic algebraic curvature tensor in four dimensions has discrete isotropy while O(2) acts trivially on the one-dimensional space at n = 2. → 20 - 6 = 14, 6 - 3 = 3, and 1 - 1 = 0 is indeed the wrong answer on a surface, as the check says. Correct.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Polarization claims: at most 6 in a general metric theory, 2 in general relativity, and GW170814 favoured tensor modes.: The six components a detector reads are the symmetric E-matrix, which fixes a null plane wave's Riemann tensor in any metric theory; general relativity's vacuum equations and gauge freedom leave two; GW170814 record checked. → Correct as stated in the check, the misconception and the research horizon.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Entry summary 'Rules make most entries zero, or copies or opposites of other entries'.: python count in four dimensions of index quadruples with a repeated pair index, and of the entries that are plus or minus one of the twenty. → 112 of 256 vanish by antisymmetry; only the eight sign-variants of R_0312 are combinations rather than copies, so 248 of 256 fit the sentence. True.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Every reference: authors, year, title, venue, doi.: Crossref records fetched again for 10.1007/s00190-011-0500-0, 10.1007/BF01199420, 10.1515/crll.1869.70.46, 10.1063/1.529470, 10.1103/PhysRevLett.30.884, 10.1016/0003-4916(84)90085-X, 10.1016/0550-3213(88)90143-5 and 10.1103/PhysRevLett.119.141101; a web record for the Riemann 1868 Abhandlungen volume and pages. → All eight DOI records match the note exactly, including the five authors of Eardley, Lee, Lightman, Wagoner and Will. Riemann 1868, Abhandlungen volume 13, pages 133-152 confirmed. The Christoffel Crossref record carries no author field but the volume, pages and title match. All stay verified.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). Weyl 1918 history line: the conformal curvature tensor is the part of the curvature unchanged under a pointwise rescaling of the metric.: Conformal transformation of the Weyl tensor: the mixed form C^rho_{sigma mu nu} is invariant, while the fully lowered form scales with the conformal factor. → The sentence was true only for the mixed form; 'with one index raised' added.
- Second physics review, 2026-09-13 (full independent re-derivation on revision 5, after the second novice read). The twelve rewrites of the second novice read, checked one by one for accuracy.: note_diff between the pre-novice-2 snapshot and revision 5, then each changed string re-derived: the tagline's added 0, the lean-rule glossary entry against first-pair antisymmetry, 'a grid of tilts', 'ahead-left with up-time', 'one for each group of four different directions', the row-by-row try-it order, 'the 6 sideways drifts hold 3 numbers', 'a crumb at rest in the box', 'seen from every side', and 'the peel cannot lie flat'. → Eleven are accurate. Two needed work: 'seen from every side' as the sole reason for two magnitudes (empty space added), and 'cannot lie flat', which drops the qualifier of the sentence above it (changed to 'cannot be pressed flat', matching that sentence's own verb).

**Counterexamples tried**

- Rolled paper tube against 'a surface's number records that it cannot be pressed flat': the novice rewrite scopes it to a ball and gives the tube zero. Survives.
- String tied into a ring: an ant returns to its start, but that is topology, not curvature; simplifies says so and the count 0 stands.
- Spherical Earth with a radial arm against 'six are sideways drifts': the sideways drifts vanish in that frame; the note says so. Survives.
- Time-dependent tidal field (gravitational wave) against the no-whirlpool reason: pair exchange keeps E_ij symmetric anyway, so the stated static condition is sufficient, not necessary; no false sentence results.
- Vacuum in a generic frame against 'half of the twenty can be nonzero in empty space': all components can be nonzero while only ten are independent. Broke the sentence; fixed.
- Two space dimensions and time with a cosmological constant against 'empty space has no curving': vacuum then has constant curvature. The working way already scopes it; the entry common answer now says 'simplest form with no dark energy'.
- Inside a round star against 'only a few different values': Ricci is nonzero and the count differs; rescoped to outside.
- Lorentzian orbits against 'invariants fix the curvature': plane waves have zero polynomial invariants with R nonzero; the formal way already states it.
- Non-Levi-Civita connection (torsion) against the count: loses pair exchange and the cyclic identity; key-equation conditions and formal limits already name Levi-Civita.
- n = 1, 2, 3 against the minus-C(n,4) step and the Weyl formula: C(n,4) = 0 and the Weyl formula is scoped to n >= 3; surface case handled separately. Survives.
- Second physics review: a passing gravitational wave against the note's static condition for no whirlpool. Pair exchange makes R_{hat i hat 0 hat j hat 0} symmetric in any spacetime, so the condition is sufficient but not necessary. Nothing in the note claims it is necessary, and the prerequisite reaches the same conclusion by an energy argument that does need a static field, so the wording was kept again; the concern stands for an editor.
- Second physics review: a spinning tide meter against 'the 9 readings hold 6 separate numbers'. A rotating frame adds a symmetric centrifugal term at order t squared and an antisymmetric Coriolis term only at order t cubed, so the readings would no longer be the table's entries. The way, the glossary entry for tide meter and the check all say the box does not spin. Survives.
- Second physics review: a uniform-density star against 'inside a star the same frame shows four magnitudes'. The uniform-density interior is isotropic in its tidal part and has a constant-curvature spatial slice, so it gives two magnitudes; checked numerically. The formal way therefore says 'of varying density'.
- Second physics review: a static spherically symmetric non-vacuum metric against 'so few sizes appear because the star looks the same seen from every side'. Four distinct magnitudes appear (checked numerically), so symmetry alone is not the reason. Broke the sentence; fixed by naming empty space as well.
- Second physics review: a surface against the key equation's 'exactly three dimensions'. The formula also holds at n = 2 with R_{mu nu} = (R/2)g_{mu nu}. Broke the condition; reworded.
- Second physics review: a rolled paper tube against 'the peel cannot be pressed flat'. The tube's one number is zero and it does unroll flat; the way says exactly that in the next sentence. Survives.
- Second physics review: a cone tip and a conical deficit against the pointwise count. The count assumes a smooth metric at the point; the coordinate way's simplifies says so, and the three-dimensional point mass is described as a removed wedge, not as curvature at the tip. Survives.
- Second physics review: n = 1, 2, 3 against the minus-C(n,4) step, and n = 2 against the Weyl formula. Brute-force rank gives 0, 1, 6 with and without the cyclic rows, and the Weyl formula is scoped to n >= 3 with the surface handled separately. Survives.
- Second physics review: a boosted observer against '20 independent numbers'. Components mix under the Lorentz group; the formal check and the misconception components-are-invariants say so. Survives.
- Second physics review: a cosmological constant in two space dimensions and time against 'empty space is then locally flat'. With Lambda non-zero the vacuum has constant curvature; the way's simplifies and the entry answer both scope to no cosmological constant. Survives.
- Second physics review: a connection with torsion against the whole count. It loses pair exchange and the cyclic identity, so more components are independent; the key equation's conditions and the formal way's limits both name Levi-Civita. Survives.
- Second physics review: a Lorentzian plane wave against invariants separating orbits. Every polynomial invariant vanishes while R does not; the formal way states it. Survives.

**Fixes**

- Common question why-the-count-matters: 'half of the twenty can be nonzero in empty space' (false; number of independent values, not nonzero components) and the loose Moon sentence replaced by 'empty space can still need ten separate numbers', with the consequence that falling crumbs drift far above Earth; the 2+1 statement scoped to Einstein's theory in its simplest form with no dark energy.
- Common question are-all-twenty-nonzero: 'Around a round star... only a few different values appear' scoped to outside the star and to someone hovering at rest, who finds two sizes (M/r^3 and 2M/r^3).
- Derivation what-coordinates-cannot-remove, step 2: the metric's change under the cubic coordinate shift is fourth order, not third, because dg(p) = 0.
- History: Riemann venue page range corrected to 133–152. DOIs added for Weyl 1918, Carminati–McLenaghan 1991, Deser–Jackiw–'t Hooft 1984 (full first names) and Witten 1988. All references verified.
- Revision bumped from 2 to 3; status physics-reviewed.
- Second physics review, revision 5 to 6. Entry way a-coiled-string-has-nothing-to-count: 'which is why the peel cannot lie flat' became 'which is why the peel cannot be pressed flat'. Without the qualifier of the sentence above it ('cannot be pressed flat without tearing or stretching') the shorter phrase is loose, and it used a second verb for one idea. Entry explanations are now 1,100 words, exactly the review limit.
- Working way empty-space-in-three-and-four-dimensions: 'R_{hat r hat 0 hat r hat 0} = -2GM/c^2r^3, the tidal stretch along the radius' became two sentences, the second naming the course geodesic deviation equation as what turns the negative component into a stretch. A negative number labelled a stretch needs its convention, as the conventions file's sectional-curvature row warns.
- Check empty-space-three-and-four: the component in inverse square metres was called the vertical gravity gradient, which has units of inverse square seconds. Now 'which times c squared is the vertical gravity gradient that gradiometers read', matching the GOCE observation's E_ij = c^2 R_{hat i hat 0 hat j hat 0}.
- Key equation riemann-from-ricci-in-three-dimensions: conditions 'Exactly three dimensions' became 'Three dimensions ... it holds on a surface too, but is false in four or more', because the formula is also an identity at n = 2.
- Tutor common question are-all-twenty-nonzero: 'So few sizes appear because the star looks the same seen from every side' gained 'and because the space around it is empty'. Symmetry alone leaves four magnitudes; a numerical non-vacuum spherically symmetric example confirms it.
- Formal way algebraic-curvature-tensors: the Schwarzschild magnitudes M/r^3 and 2M/r^3 now say 'with G = c = 1', which the rung requires once per way, and the sentence adds that inside a star of varying density the same frame shows four magnitudes, which is what makes the vacuum case the special one.
- History weyl-1918: the conformal curvature tensor is unchanged under a pointwise rescaling only with one index raised; the clause was added.

**Concerns**

- The entry tide way, its check and the flatland problem give 'gravity does not change with time' as the reason for no whirlpool, matching the prerequisite symmetries-of-the-riemann-tensor. That is sufficient but not necessary: the mirror rule keeps tidal drift of crumbs at rest symmetric in any field, including a passing gravitational wave. Nothing stated is false, so the wording was kept for consistency with the prerequisite; an editor may prefer to lean on the mirror rule alone.
- The entry common answers changed; entry explanations were untouched, so the 1,100-word entry allowance is unaffected.
- The glossary's 'the direction its change is read in' versus the prerequisites' 'lean' (raised by the novice reviewer) is physically equivalent; left to an editor.
- Registry prerequisites differ from the note for gaussian-curvature and ricci-tensor; both are direct and acyclic and should be synced with sync_registry.py.
- Proposed visuals twenty-of-256-slots, coordinate-knobs-and-metric-dials and falling-ring-of-crumbs have sketches consistent with the corrected counts; not yet in the catalog.
- Second physics review: entry way explanations now total 1,100 words, exactly the core cap of 1,000 plus the 10 per cent review allowance. The one word I added is an accuracy fix I record above. Nothing further can be added at the entry rung without dropping an item; the lowest-value candidate remains the third recipe bullet the second novice read left unapplied.
- Second physics review: the no-whirlpool condition 'the planet's gravity does not change with time' is kept in the tide way, its check and the flatland solution. It is sufficient, not necessary, and the note nowhere claims otherwise; it matches the energy argument the prerequisite symmetries-of-the-riemann-tensor uses at the entry rung, which does need a static field. Leaning on the mirror rule alone would be more general but would break the shared entry vocabulary across the two notes, so it stays an editor's call.
- Second physics review: review.novice covers revision 5 while the note is at revision 6, which the validator reports. That is expected: a novice re-read of the five learner-visible strings this stage changed is due, four of them one clause long and one of them a tutor answer.
- Second physics review: course-conventions.md still fixes no convention for the Weyl tensor's explicit component definition and normalization, for the Kulkarni-Nomizu product (this note writes its own P(S) instead), or for the duality convention behind the four-dimensional self-dual split the formal way mentions. This note sidesteps all three; a note that must write the Weyl tensor in components cannot.
- Second physics review: the registry still lists different prerequisites from the note for gaussian-curvature and ricci-tensor, and all three visuals remain proposals with sketches. Neither is this stage's to change.

**Diff check** (2026-09-13, revision 4)

- are-all-twenty-nonzero: for someone hovering at rest outside a round star that does not spin, the Riemann components that are not zero come in two magnitudes, and this is due to the symmetry.: Computed Schwarzschild Christoffels and Riemann by finite differences in python at r = 7M, theta = 1.1, then projected onto the static orthonormal frame for all 256 index orders. Compared the rewording with the revision-3 sentence. → The magnitudes are exactly 2M/r^3 and M/r^3, which is 2GM/c^2r^3 and GM/c^2r^3 in SI units. 'Ignoring plus and minus signs' is needed and correct. The claim matches the old one, stated more precisely.
- why-the-count-matters: with Lambda = 0, vacuum in 2+1 dimensions is flat; in 3+1, empty space can carry ten independent numbers, half of the twenty; tidal drift continues in vacuum.: In 3D the Weyl count n(n+1)(n+2)(n-3)/12 is 0, so Riemann is fixed by Ricci, and Ricci is zero in vacuum. In 4D it is 10 = 20 - 10. Checked that the no-dark-energy scope still covers the 2+1 claim after the split, and compared the split with the old sentences. → Correct, and the scope condition is kept. 'In space empty of air and of everything else' makes the vacuum claim sharper and is still true.
- Derivation step 2: with dg(p) = 0 and x - x' cubic, g(x) - g(x') is of fourth order in x'; Jacobian delta + (1/2)A x'x'.: Taylor expansion by hand: dg(x') = O(x') times O(x'^3), and the next term is O(x'^6). Differentiated the symmetric cubic map to get the Jacobian. Ran a 1D python toy with g = 1 + 0.9x^2 + 0.3x^3 and a = 0.7: (g(x) - g(x'))/x'^4 tends to 0.9a/3 = 0.21. → Correct: 0.221, 0.215 and 0.213 at x' = 0.1, 0.05 and 0.025 approach 0.21. The Jacobian is correct. The step says what the revision-3 fix meant.

**Diff check** (2026-09-13, revision 7)

- checks/empty-space-three-and-four answer, reworded tail: outside Earth a static observer at the surface measures R_{r-hat 0-hat r-hat 0-hat} = -2GM/c^2r^3 about -3.4e-23 per square metre, and c^2 times this component is the vertical gravity gradient that gradiometers read.: Recomputed -2GM/c^2r^3 in python with G = 6.674e-11, M = 5.972e24 kg, r = 6371 km, c = 2.998e8 m/s, and multiplied by c^2. Checked the sign against the course geodesic-deviation row with u^0-hat = c: D^2 xi^r/dtau^2 = -R^{r-hat}{}_{0-hat r-hat 0-hat} c^2 xi^r = +2GM/r^3 xi^r, a radial stretch, so c^2 times the component equals the free-air gradient of the downward gravity magnitude with height. Compared old and new clause word by word. → -3.4297e-23 per square metre, rounding to -3.4e-23 as printed; c^2 times it is -3.083e-6 per second squared, which is the standard free-air vertical gradient (about -0.3086 milligal per metre, 3086 eotvos in magnitude). The reworded clause states exactly the old relation, only moving 'times c^2' out of a relative clause; no number, sign or measurer changed. The measurer is still named and placed ('a static observer at the surface'). Accurate.
- key_equations/riemann-from-ricci-in-three-dimensions conditions, reworded: the formula 'also holds in the two dimensions of a surface', and is false in four or more.: Substituted the two-dimensional identities R_{mu nu} = (R/2) g_{mu nu} and R_{rho sigma mu nu} = (R/2)(g_{rho mu}g_{sigma nu} - g_{rho nu}g_{sigma mu}) into the note's right-hand side by hand; then evaluated the right-hand side for a constant-curvature n-space in python, where R_{rho sigma mu nu} = K(gg - gg), R_{sigma nu} = K(n-1)g_{sigma nu} and R = Kn(n-1), giving coefficient 2(n-1) - n(n-1)/2. → The hand substitution returns (R/2)(g_{rho mu}g_{sigma nu} - g_{rho nu}g_{sigma mu}), which is the whole two-dimensional Riemann tensor, so the identity holds for every two-dimensional metric, not only constant curvature. The python coefficients are 1 for n = 2 and n = 3 and 0 and -2 for n = 4 and n = 5, confirming both halves of the condition. The new wording ('the two dimensions of a surface') says the same as the old 'on a surface too' and names the dimension, which is what the condition is about. Accurate.
- tutor_moves/common_questions/are-all-twenty-nonzero, reworded pronoun: 'So few sizes appear because the star looks the same seen from every side, and because the space around the star is empty', following 'The numbers this person finds that are not zero come in only two sizes, if you ignore plus and minus signs.': Recomputed the Schwarzschild Riemann tensor from the metric by finite differences in pure python at r = 10M, theta = pi/2, lowered the first index, and projected onto the static orthonormal frame e_t = f^{-1/2} d_t, e_r = f^{1/2} d_r, e_theta = r^{-1} d_theta, e_phi = (r sin theta)^{-1} d_phi. Listed every nonzero component and its magnitude. → The nonzero components are R_trtr = -2M/r^3, R_tthth = R_tphph = +M/r^3, R_rthrth = R_rphrph = -M/r^3, R_thphthph = +2M/r^3: exactly two magnitudes, 2M/r^3 and M/r^3, so 'two sizes ignoring plus and minus signs' is right, and R_{r-hat 0-hat r-hat 0-hat} = -2M/r^3 agrees with the working rung. Both stated reasons are correct: spherical symmetry plus vacuum with no cosmological constant fixes the exterior to one function of r. The edit replaced 'it' with 'the star' and changed no claim. Accurate.
- ways_in/a-coiled-string-has-nothing-to-count entry explanation, reworded: 'A piece of orange peel cannot be pressed flat without tearing or stretching. That tearing or stretching happens because on a ball the surface's 1 number is not zero.': Checked the causal direction against the intrinsic-curvature theorem: pressing a patch flat with no tearing or stretching would be a distance-preserving map to the plane, which carries the surface's single independent Riemann component to zero. Confirmed the count n^2(n^2-1)/12 = 1 for n = 2 and that a sphere of radius a has that component nonzero (R = +2/a^2 in the conventions), while a rolled sheet of paper has it zero. Compared the new causal order with the old sentence. → Correct in both directions: nonzero component implies no flattening, and the old sentence claimed the same implication with the clauses swapped. The following sentence about a paper tube is the matching zero case and stays true. No hypothesis was lost: the claim is about a piece of a ball's surface, and it holds for every piece of nonzero area. Accurate.
- ways_in/empty-space-in-three-and-four-dimensions working explanation, reordered: 'That negative component is a stretch along the radius, by the geodesic deviation equation in the course conventions.': Applied the course geodesic-deviation row D^2 xi^mu/dtau^2 = -R^mu{}_{nu rho sigma} u^nu xi^rho u^sigma to a static observer with u^0-hat = c and a radial separation, using R^{r-hat}{}_{0-hat r-hat 0-hat} = R_{r-hat 0-hat r-hat 0-hat} = -2GM/c^2r^3 since the frame is orthonormal with eta_{r-hat r-hat} = +1. Compared the two word orders clause by clause. → D^2 xi^{r-hat}/dtau^2 = +2GM/r^3 xi^{r-hat} > 0, a stretch along the radius, so the negative component does mean a radial stretch in the course sign conventions. The reorder moves the justifying phrase to the end and changes no claim, scope or sense. Accurate.
