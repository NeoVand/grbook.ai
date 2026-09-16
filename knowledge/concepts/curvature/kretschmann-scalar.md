---
type: "concept"
schema_version: 2
id: "kretschmann-scalar"
title: "Kretschmann scalar"
tagline: "One number from the whole curvature table that everyone agrees on"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 6
updated: "2026-09-13"
aliases: ["Kretschmann invariant", "Riemann-squared scalar"]
prerequisites: ["riemann-curvature-tensor", "scalar-invariant"]
leads_to: ["curvature-singularity", "schwarzschild-singularity", "weyl-tensor", "cartan-karlhede-algorithm"]
visuals: ["three-gauges-on-a-falling-probe", "pencil-on-turning-squared-paper", "falling-ring-of-crumbs", "six-entry-curvature-table"]
---

# Kretschmann scalar

*One number from the whole curvature table that everyone agrees on*

`kretschmann-scalar` · curvature · core · physics-reviewed (revision 6)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[scalar-invariant]] (working)  
**Opens:** [[curvature-singularity]] · [[schwarzschild-singularity]] · [[weyl-tensor]] · [[cartan-karlhede-algorithm]]  
**Related:** [[ricci-scalar]] · [[coordinate-singularity]] · [[relativistic-tidal-tensor]]  
**Visuals:** ★ [[three-gauges-on-a-falling-probe]] · [[pencil-on-turning-squared-paper]] · [[falling-ring-of-crumbs]] · [[six-entry-curvature-table]]

> The curving of space and time at a place is described by a whole table of numbers. Those numbers change when you choose your directions differently. Squaring the entries and adding them gives one number everyone agrees on: the Kretschmann scalar. When time is one of the directions, some squares are subtracted instead. For a black hole that does not spin, this number has an ordinary value at the horizon and grows without limit only as the centre is approached.

## You will be able to

**Entry**
- Predict how the Kretschmann scalar changes when every entry of the curvature table grows. `objectives/explain-the-agreed-number` ← `problems/ball-half-as-wide`
- Predict how the Kretschmann scalar outside a round body changes with distance and with the body's mass. `objectives/predict-scaling` ← `checks/halve-the-distance`, `checks/bigger-black-hole`
- Distinguish a number that blows up on one map of a place from curving that grows without limit. `objectives/distinguish-map-from-place` ← `checks/crushed-at-the-horizon`

**Working**
- Compute the Kretschmann scalar from orthonormal components or tidal readings, with the sign each time index brings. `objectives/compute-from-components` ← `checks/horizon-curvature-length`, `problems/expanding-universe-scalars`
- Use the Kretschmann scalar to judge whether a diverging tensor component signals curvature or a failing basis. `objectives/judge-a-diverging-component` ← `checks/component-blows-up-at-horizon`
- Explain why the Ricci scalar cannot measure curvature outside a star or in a radiation-filled universe. `objectives/explain-where-ricci-fails` ← `checks/ricci-zero-outside-a-star`

**Formal**
- State what an unbounded scalar invariant proves about extending a spacetime, and why bounded invariants do not prove regularity. `objectives/state-what-invariants-certify` ← `checks/finite-is-not-regular`
- Distinguish the positive-definite case, where a zero Kretschmann scalar forces flatness at a point, from the Lorentzian case, where it does not. `objectives/distinguish-signatures` ← `checks/zero-is-not-flat`
- Prove that every polynomial invariant of the Riemann tensor vanishes for a plane gravitational wave. `objectives/prove-plane-wave-invariants-vanish` ← `problems/plane-wave-invisible-to-invariants`

## Ways in

### 1. Square and add · entry · picture

*How can people who choose their directions differently agree on how strongly a place is curved?*

**Recap:** The Riemann curvature tensor is a table kept at every place. Pick a tilt for a tiny loop: the way the loop is angled, like the bottom, front or side of a box. Pick a starting direction for an arrow, and carry the arrow around the loop without letting it swing to point a different way. The table lists how the arrow comes back changed, divided by the loop's area.

Lay a pencil stub on squared paper whose squares are 1 centimetre wide. Put the pencil's ends on two corners of squares, 3 squares apart across the paper and 4 squares apart along it. By Pythagoras, the pencil is 5 centimetres long.

Now keep one end of the pencil on its corner and turn the paper under it, until the pencil lies on one of the lines running along the paper. The pencil now spans 5 squares along and 0 across. The two counts changed, because they depend on how the paper is turned.

Square the counts and add them. Before the turn, 3 times 3 plus 4 times 4 is 25. After the turn, 5 times 5 plus 0 times 0 is also 25. This sum is the pencil's length squared, and turning the paper cannot change the pencil's length. So no turn of the paper can change the sum.

The lines of the paper are your chosen directions. A number that stays the same however you choose your directions is called an invariant.

The curvature table works like the counts. To fill it in, you choose directions at right angles, like the lines of the paper. You test tiny loops whose tilts are pairs of those directions, with arrows that start along those directions.

Set the arrow that comes back beside a copy of the starting arrow, tail to tail. The short arrow from the starting arrow's tip to the returned arrow's tip is the change. Its parts along your chosen directions, divided by the loop's area, are the table's entries. Choose the directions differently, and the entries change, but the place is just as curved as before.

For a curved surface, or for space on its own, square every entry and add them all up. Walking a loop the other way round gives the opposite change, which has the same squares, and the recipe counts both ways round. This total is called the Kretschmann scalar. *Scalar* is a mathematician's word for a single number.

Like the pencil's squared counts, this total comes out the same for every choice of directions. We take the full reason on trust here.

**Try it:** On the edge of a paper strip, mark two dots exactly 5 squares apart, using a line of squared paper. Lay the strip on the paper at a slant, with one dot on a corner of a square. Turn the strip around that dot until the other dot lands on a corner. It can land 3 squares across and 4 along, or 4 across and 3 along, because 9 plus 16 is 25.

**Takeaway:** The curvature table's entries depend on the directions you choose, but their squares, combined by a fixed recipe, give one number everyone agrees on: the Kretschmann scalar.

*What this leaves out:* The plain recipe needs directions at right angles, marked off in equal steps like the squares of the paper. Other choices need a longer recipe that gives the same total. Space and time together need one more change: the table also has entries for tilts that include time, and the squares of some of those are subtracted instead of added.

*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[pencil-on-turning-squared-paper]]<br>*See:* `problems/ball-half-as-wide`

### 2. Read it from the stretch · entry · operational

*How could a crew falling toward a planet measure the Kretschmann scalar there?*

**Recap:** Things falling freely near a round planet drift apart along the line toward its centre and draw together across it. This is called tidal drift. The curvature table is the Riemann curvature tensor. The Kretschmann scalar is one number made by squaring its entries and adding the squares, with some squares subtracted when time is one of the directions.

A crew rides in a cabin falling freely, directly toward the centre of a round planet that does not spin and has no air. The crew lets go of two crumbs on the line toward the centre, one a little nearer the centre than the other.

Gravity pulls the nearer crumb a little harder, so the gap between the crumbs slowly grows. By timing how fast the gap grows, the crew works out how much harder gravity pulls the nearer crumb. This reading, the extra pull for each metre of gap, is called the stretch.

For this crew, outside a round body that does not spin, the laws of gravity for empty space fix every entry of the curvature table once the stretch is known. We take that on trust here.

Each entry, in the crew's directions, is a fixed multiple of the stretch. Doubling the stretch doubles every entry, and that makes every square 4 times bigger. So the Kretschmann scalar is 4 times bigger too, whether each square is added or subtracted.

Now compare two distances from the centre, both outside the planet. A crumb 1 metre nearer the centre is nearer by one part in the whole distance. Gravity's pull weakens with the square of the distance, so the pull on that crumb is stronger by about two such parts. Squaring doubles a tiny excess, as 1.001 times 1.001 is about 1.002.

Twice as far out, the pull is a quarter as strong. One metre is also half as big a part of the whole distance, so the extra pull is half as big a share of that weaker pull. The stretch is therefore a quarter of a half: one eighth as big. Each entry is one eighth as big, each square is one sixty-fourth as big, and so the scalar is 64 times smaller.

At Earth's surface, the pull on a crumb 2 metres nearer the centre is stronger by less than one millionth of its weight. That is why nobody notices the stretch.

**Takeaway:** Outside a round body that does not spin, a crew falling directly toward the centre can find the Kretschmann scalar from its stretch reading. The scalar grows 64 times when the crew's distance from the centre halves.

*What this leaves out:* A crew moving sideways past the planet, rather than falling directly in, gets different stretch readings but works out the same Kretschmann scalar. Near a spinning body, or inside a planet, the stretch alone does not fix the table.

*Continues:* `ways_in/square-and-add`<br>*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/halve-the-distance`

### 3. A map can blow up where the ground does not · entry · contrast

*When a formula for a black hole gives an infinite number, is something infinite really there?*

**Recap:** The Kretschmann scalar is one number built from the whole curvature table at a place. Everyone who describes the place gets the same value, however they choose their directions. Outside a round body that does not spin, a crew falling directly toward its centre can work the scalar out from its stretch reading. The stretch is the extra pull on the one of two crumbs nearer that centre, for each metre of gap.

Some rectangular world maps draw the globe's lines of latitude and longitude as an even grid of squares. The North Pole is a single point on the ground, but such a map spreads it along the whole top edge. A walk of a few steps around the pole crosses the map from one side to the other.

So near the top edge, the map makes distances around the pole look larger and larger, without limit. Nothing strange happens to the ice at the North Pole, though. The blow-up belongs to the map, not to the ground. So a number that blows up on a map does not prove that the place itself is extreme.

A black hole is a place where gravity is so strong that nothing falling far enough in can get back out. Its surface of no return is called the horizon.

A formula for the space and time around a black hole works like a map: it gives every moment at every place a set of labels. The usual formula for a black hole that does not spin contains a number that becomes infinite at the horizon. That formula's labels suit people who hover at fixed distances, holding themselves up with rockets. At the horizon nobody can hover, however strong the rocket, so these labels fail there, like the map at its top edge.

The Kretschmann scalar gives a fair test, because every map gives the same value for it at a place. A crew falling directly toward the black hole's centre works out the scalar at the horizon from its stretch reading and gets an ordinary value, not an infinite one. For a black hole about 58 million times as heavy as the Sun, the scalar at the horizon matches the scalar at the ground under your feet.

So the test finds no infinite curving there. A better map, drawn for a crew falling in, has no infinite number at the horizon at all; we take its details on trust here. The infinite number was a fault of the usual map.

The scalar keeps growing as the crew falls deeper in, and it grows without limit as the crew nears the centre. Every map gives the same scalar, so no better map can remove this blow-up.

**Takeaway:** An infinite number in a black hole's formula can be the map's fault. The Kretschmann scalar, the same for every map, has an ordinary value at the horizon and grows without limit only as the centre is approached.

*Continues:* `ways_in/square-and-add`, `ways_in/read-it-from-the-stretch`<br>*Visuals:* [[three-gauges-on-a-falling-probe]]<br>*See:* `checks/crushed-at-the-horizon`

### 4. Contract every index · working · calculation

*How is the Kretschmann scalar computed from components, and why can a component diverge where the scalar does not?*

The squared-paper recipe of "Square and add" is, in index notation, the full contraction of the Riemann tensor with itself:

$$\mathcal K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}.$$

No index is left free. Under a change of coordinates each lower index brings a Jacobian factor and each upper index its inverse, and the factors cancel in pairs, so $\mathcal K$ is a scalar, with units of inverse length to the fourth power.

In an orthonormal frame, raising a spatial index changes nothing and raising $\hat 0$ flips the sign. The derivation "Expanding the contraction in an orthonormal frame" groups the squares by how many time indices they carry:

$$\mathcal K = 4\sum_{i,j}\big(R_{\hat 0\hat i\hat 0\hat j}\big)^2 - 4\sum_{i,j,k}\big(R_{\hat 0\hat i\hat j\hat k}\big)^2 + \sum_{i,j,k,l}\big(R_{\hat i\hat j\hat k\hat l}\big)^2.$$

The middle sum is the subtraction in the entry recipe. A positive-definite geometry has no such sum, so there $\mathcal K$ is a plain sum of squares. A two-dimensional sphere of radius $a$ has one independent component, $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = 1/a^2$, in four index orders, so $\mathcal K = 4/a^4$.

Why not use the simpler Ricci scalar, the trace $R = g^{\mu\nu}R^\rho{}_{\mu\rho\nu}$? Outside a star or a black hole, the vacuum Einstein equation with no cosmological constant sets $R_{\mu\nu} = 0$, so $R = 0$ at every radius and cannot tell one radius from another. The Riemann tensor is not zero there. With $m = GM/c^2$, its components in the static orthonormal frame of the Schwarzschild metric, taken on trust here, lead to

$$\mathcal K = \frac{48\,G^2M^2}{c^4r^6},$$

as the derivation "Schwarzschild from six components" shows. At the horizon, $r_s = 2m$, this is $12/r_s^4$: finite.

A single coordinate component can still diverge there. With $g_{rr} = (1 - 2m/r)^{-1}$, $R_{r\theta r\theta} = g_{rr}\,r^2R_{\hat r\hat\theta\hat r\hat\theta} = -m/(r - 2m)$. The basis vector $\partial_r$ has squared length $g_{rr}$, which diverges at $r = 2m$, and the component inherits that divergence. $\mathcal K$ has no free index to inherit it. As $r \to 0$, however, $\mathcal K$ grows without bound, and because it is a scalar no change of coordinates can tame it.

**Takeaway:** The Kretschmann scalar is the full contraction of the Riemann tensor; outside a spherical mass it falls as the inverse sixth power of the radius and stays finite at the horizon, even where a coordinate component diverges.

*What this leaves out:* Leaves the Schwarzschild components themselves to the Schwarzschild metric; ignores the cosmological constant.

*Continues:* `ways_in/square-and-add`<br>*Builds on:* [[scalar-invariant]]<br>*See:* `derivations/orthonormal-expansion`, `derivations/schwarzschild-from-six-components`, `checks/component-blows-up-at-horizon`

### 5. Tidal readings fix the scalar · working · operational

*How do an observer's tidal measurements determine the Kretschmann scalar in empty space?*

The falling crew in "Read it from the stretch" was measuring Riemann components. Neighbouring freely falling worldlines, separated by $\xi^{\hat i}$ in a frame carried by one of them, obey $\ddot\xi^{\hat i} = -c^2R_{\hat 0\hat i\hat 0\hat j}\,\xi^{\hat j}$, the geodesic deviation equation taken on trust here. So minus $c^2$ times the symmetric matrix of tidal components $R_{\hat 0\hat i\hat 0\hat j}$ is the matrix of relative accelerations per unit separation, in $\mathrm{s^{-2}}$. In a weak field those accelerations are $-\partial_i\partial_j\Phi$, built from the Newtonian potential $\Phi$, and they are what a gravity gradiometer reads, up to the instrument's sign convention.

In vacuum the Ricci tensor vanishes, and that ties the purely spatial components to the tidal ones: $\sum(R_{\hat i\hat j\hat k\hat l})^2 = 4\sum(R_{\hat 0\hat i\hat 0\hat j})^2$, as the derivation "In vacuum, space follows the tides" shows. The orthonormal expansion becomes

$$\mathcal K = 8\sum_{i,j}\big(R_{\hat 0\hat i\hat 0\hat j}\big)^2 - 4\sum_{i,j,k}\big(R_{\hat 0\hat i\hat j\hat k}\big)^2.$$

For an observer at rest in a static field, reversing time is a symmetry. It flips the sign of every component with one time index, so those components vanish, and $\mathcal K$ is eight times the sum of the squared tidal components. Outside a spherical mass the tidal matrix is $\mathrm{diag}(-2, 1, 1)\,GM/(c^2r^3)$, radial entry first, so $\mathcal K = 8 \times 6\,G^2M^2/(c^4r^6)$, the Schwarzschild value again. A radially falling observer's frame is a radial boost of the static one, and it reads the same tidal matrix, so the entry crew's single stretch reading, $2GM/r^3$, fixes $\mathcal K = 12(2GM/r^3)^2/c^4$.

An observer moving tangentially reads more. For a tangential boost of rapidity 0.9, a speed of $0.72c$ relative to the static observer, the squared tidal components sum to about 45 in units of $(GM/c^2r^3)^2$ instead of 6, but the one-time components switch on and $\mathcal K$ stays 48 in the same units. Only the combination is invariant.

Near Earth the radial gradient $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$ matches the measured decrease of gravity with height. The worked example "Earth against a black hole's horizon" turns it into $\mathcal K$.

**Takeaway:** In vacuum, the Kretschmann scalar is eight times the summed squares of the tidal components minus four times those with one time index; for static observers only the tides remain.

*What this leaves out:* Vacuum with no cosmological constant; tidal readings over separations small compared with $r$.

*Continues:* `ways_in/read-it-from-the-stretch`, `ways_in/contract-every-index`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/space-follows-the-tides`, `worked_examples/earth-against-a-horizon`, `checks/horizon-curvature-length`

### 6. What scalar invariants can and cannot certify · formal · structure

*What does an unbounded curvature invariant prove, and what does a bounded one fail to prove?*

The scalar of "Contract every index" belongs to a family; set $G = c = 1$ throughout. On a Lorentzian manifold $(M, g)$ with its Levi-Civita connection, a scalar polynomial curvature invariant is a complete contraction, formed with $g$, $g^{-1}$ and possibly $\epsilon$, of a polynomial in the Riemann tensor and finitely many of its covariant derivatives: $R$, $R_{\mu\nu}R^{\mu\nu}$, $\mathcal K$ and $\nabla_\lambda R_{\mu\nu\rho\sigma}\nabla^\lambda R^{\mu\nu\rho\sigma}$ are examples.

*Decomposition.* For $n \ge 3$ the Riemann tensor splits orthogonally into the Weyl tensor and parts built from $R_{\mu\nu}$ and $R$, so squared norms add; in four dimensions $\mathcal K = C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + 2R_{\mu\nu}R^{\mu\nu} - \tfrac13R^2$. In vacuum with $\Lambda = 0$, $\mathcal K$ is the squared norm of the Weyl tensor.

*Sign.* If $g$ is positive definite, $\mathcal K = \sum(R_{abcd})^2$ in an orthonormal frame, so $\mathcal K \ge 0$, with equality at $p$ exactly when the Riemann tensor vanishes at $p$. In Lorentzian signature the frame expansion has a negative term and $\mathcal K$ is indefinite: for Kerr, in Boyer–Lindquist coordinates, $\mathcal K = 48M^2(r^2 - a^2\cos^2\theta)(r^4 - 14a^2r^2\cos^2\theta + a^4\cos^4\theta)/(r^2 + a^2\cos^2\theta)^6$, negative on the axis just outside the horizon whenever $a > M/2$.

*Counting.* At a point the 20 Riemann components, modulo the six-dimensional Lorentz group, leave at most 14 algebraically independent invariants; the 10 Weyl components of a vacuum field leave 4.

*Theorem.* Let $\gamma$ be an inextendible causal geodesic of finite affine length along which some scalar polynomial invariant built from the Riemann tensor alone is unbounded. Then no extension $(M', g')$ with $g'$ of class $C^2$ continues $\gamma$ to a point $p$. Sketch: in such an extension the frame components of the Riemann tensor are continuous near $p$, hence bounded on a compact neighbourhood, and so is every polynomial built from them with the constant frame metric. Invariants with $k$ derivatives need $g' \in C^{k+2}$. Schwarzschild's $r \to 0$, reached by radial infall at finite proper time with $\mathcal K = 48M^2/r^6$, is such a scalar polynomial curvature singularity.

*Limits.* The converse is false. Bounded invariants do not make a spacetime extendible: the regularity of $r = 2M$ is proven by the ingoing Eddington–Finkelstein chart, in which $g$ is analytic and nondegenerate across the horizon, not by $\mathcal K = 3/(4M^4)$ there. Geodesics can end with every invariant bounded, at a conical defect or at the singularities of the plane waves in "Every invariant vanishes, yet the wave is curved". Nor do invariants fix the local geometry in general; that equivalence problem needs frame components and their derivatives.

**Takeaway:** An unbounded scalar invariant along a geodesic of finite affine length rules out any extension with a twice continuously differentiable metric; bounded or vanishing invariants prove neither regularity nor flatness in Lorentzian signature.

*What this leaves out:* Four dimensions and the Levi-Civita connection; singularities defined through inextendible geodesics of finite affine length.

*Continues:* `ways_in/contract-every-index`<br>*See:* `checks/finite-is-not-regular`, `checks/zero-is-not-flat`

### 7. Every invariant vanishes, yet the wave is curved · formal · contrast

*Can a curved spacetime have every curvature invariant equal to zero?*

The positivity found in "What scalar invariants can and cannot certify" for positive-definite metrics fails completely in Lorentzian signature. Set $G = c = 1$ and take the vacuum plane wave in Brinkmann coordinates,

$$ds^2 = -2\,du\,dv + dx^2 + dy^2 + A(u)\,(x^2 - y^2)\,du^2,$$

with $u$, $v$ null coordinates and $A$ any smooth function. Up to index symmetries the only nonzero Riemann components are $R_{uxux} = -A$ and $R_{uyuy} = A$, so $R_{uu} = 0$ and the metric is vacuum. The wave is curved: in a parallel-propagated transverse frame, geodesics with $du/d\lambda = k$ separate as $d^2\xi^x/d\lambda^2 = Ak^2\xi^x$ and $d^2\xi^y/d\lambda^2 = -Ak^2\xi^y$.

Yet every complete contraction of products of Riemann tensors vanishes. The inverse metric has $g^{uu} = 0$, so in a contraction a $u$ slot can pair only with a $v$ slot. Every nonzero component has $u$ slots and no $v$ slot, so every term of every complete contraction contains a zero factor. In particular $\mathcal K = 0$. A boost-weight count extends the result to contractions with $\epsilon$ and with covariant derivatives: these waves have vanishing scalar invariants of every order.

The blindness matters for singularities. Take $A = \alpha/u^2$ for $u < 0$. Because $\partial_v$ is a Killing vector, $du/d\lambda$ is constant along geodesics, so geodesics with $k \ne 0$ reach $u = 0$ at finite affine parameter. In a parallel-propagated frame the tidal components along them are $\mp\alpha k^2/u^2$, which grow without bound, while every scalar invariant stays exactly zero. Only frame components along curves can detect such parallel-propagated curvature singularities.

**Takeaway:** A plane gravitational wave is curved, with real tides, yet every scalar curvature invariant vanishes; its singular versions are invisible to all of them.

*What this leaves out:* Exact plane waves; the same vanishing holds for the wider family of spacetimes with vanishing scalar invariants.

*Continues:* `ways_in/what-invariants-certify`<br>*See:* `problems/plane-wave-invisible-to-invariants`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To move the arrow so that it points a different way. The arrow test never lets it swing. | — |
| tilt | — | The way a tiny loop is angled at a spot, set by the two directions its sides run along, like the bottom, front or side of a box. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every place. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed. The arrow goes around the loop without swinging, and each change is divided by the loop's area. | [[riemann-curvature-tensor]] |
| invariant | — | A number that comes out the same however you choose your directions, like the squared length of a pencil lying on squared paper that you turn. | [[scalar-invariant]] |
| Kretschmann scalar | KRETCH-mahn SKAY-ler | One number made from the whole curvature table at a place, by squaring every entry and adding the squares. When time is one of the directions, some squares are subtracted instead. Everyone who describes the place gets the same value. Scalar means a single number. | [[kretschmann-scalar]] |
| fall freely | — | To move with nothing but gravity acting: no engine, no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tidal drift | — | The way gravity makes neighbouring falling objects outside a round planet spread apart along the line toward its centre and draw together across it. | [[tidal-force]] |
| stretch | — | For two crumbs falling freely, one nearer a round body's centre than the other, the extra pull on the nearer crumb for each metre of gap. It measures how strong the tidal drift is along the line toward the centre. | — |
| black hole | — | A place where gravity is so strong that nothing falling far enough in can get back out, not even light. | [[black-hole]] |
| horizon | — | The surface of no return around a black hole. Anything that falls through it can never get back out, not even light. | [[event-horizon]] |

## Key equations

### Kretschmann scalar · working

$$
\mathcal{K} = R_{\mu\nu\rho\sigma}\,R^{\mu\nu\rho\sigma}
$$

The Riemann tensor contracted with itself on every index: one number per event, the same in every coordinate system.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal{K}$ | the Kretschmann scalar, in $\mathrm{m^{-4}}$ | the Kretschmann scalar |
| $R_{\mu\nu\rho\sigma}$ | the Riemann tensor with all indices lowered | the Riemann tensor |

**Holds when:** Any metric with its Levi-Civita connection; every index summed. Unchanged by the overall sign convention of the Riemann tensor and by $g \to -g$.  
**Say it:** “The Kretschmann scalar is the Riemann tensor with all indices down times the Riemann tensor with all indices up, summed over every index.”  
**Justified by:** `stated`

### Kretschmann scalar in an orthonormal frame · working

$$
\mathcal{K} = 4\sum_{i,j}\big(R_{\hat 0\hat i\hat 0\hat j}\big)^2 - 4\sum_{i,j,k}\big(R_{\hat 0\hat i\hat j\hat k}\big)^2 + \sum_{i,j,k,l}\big(R_{\hat i\hat j\hat k\hat l}\big)^2
$$

Squares of components with two time indices and with none add; squares of components with one time index subtract.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\hat 0\hat i\hat 0\hat j}$ | tidal components in an orthonormal frame | the tidal components |
| $R_{\hat 0\hat i\hat j\hat k}$ | components with exactly one time index | the components with one time index |
| $R_{\hat i\hat j\hat k\hat l}$ | purely spatial components | the spatial components |

**Holds when:** Orthonormal frame, signature $(-,+,+,+)$, four dimensions; spatial indices summed from 1 to 3.  
**Say it:** “The Kretschmann scalar is four times the squared tidal components, minus four times the squared components with one time index, plus the squared spatial components.”  
**Justified by:** `derivations/orthonormal-expansion`

### Kretschmann scalar outside a spherical mass · working

$$
\mathcal{K} = \frac{48\,G^2M^2}{c^4\,r^6}
$$

Outside a spherical, non-rotating mass the scalar falls as the sixth power of $r$; at the horizon it is finite, and it diverges only as $r \to 0$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $M$ | the mass | the mass |
| $r$ | the Schwarzschild radial coordinate, circumference divided by $2\pi$ | r |

**Holds when:** Vacuum Schwarzschild region, no cosmological constant. At $r_s = 2GM/c^2$ it equals $12/r_s^4$.  
**Say it:** “The Kretschmann scalar is forty-eight G squared M squared over c to the fourth r to the sixth.”  
**Justified by:** `derivations/schwarzschild-from-six-components`

### Vacuum form from tidal readings · working

$$
\mathcal{K} = 8\sum_{i,j}\big(R_{\hat 0\hat i\hat 0\hat j}\big)^2 - 4\sum_{i,j,k}\big(R_{\hat 0\hat i\hat j\hat k}\big)^2
$$

In empty space the spatial components follow from the tidal ones, so an observer's tidal readings and one-time components give the scalar.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\hat 0\hat i\hat 0\hat j}$ | tidal components; minus $c^2$ times them are the relative accelerations per unit separation | the tidal components |
| $R_{\hat 0\hat i\hat j\hat k}$ | components with exactly one time index, zero for static observers in a static field | the components with one time index |

**Holds when:** Vacuum, $R_{\mu\nu} = 0$, four dimensions, orthonormal frame of any observer.  
**Say it:** “In vacuum, the Kretschmann scalar is eight times the squared tidal components minus four times the squared components with one time index.”  
**Justified by:** `derivations/space-follows-the-tides`

## Derivations

### Expanding the contraction in an orthonormal frame · working

**Goal:** Show that $\mathcal K = 4\sum(R_{\hat 0\hat i\hat 0\hat j})^2 - 4\sum(R_{\hat 0\hat i\hat j\hat k})^2 + \sum(R_{\hat i\hat j\hat k\hat l})^2$ in an orthonormal frame.

1. In an orthonormal frame $\eta^{\hat a\hat b} = \mathrm{diag}(-1, 1, 1, 1)$, so raising a spatial index leaves a component unchanged and raising $\hat 0$ flips its sign.
2. Hence $\mathcal K = \sum_{a,b,c,d}(-1)^N(R_{\hat a\hat b\hat c\hat d})^2$, where $N$ counts the $\hat 0$ indices among $a, b, c, d$.
3. Antisymmetry in each index pair removes every component with $\hat 0$ twice in one pair, so $N = 3$ and $N = 4$ contribute nothing, and $N = 2$ needs one $\hat 0$ in each pair.
4. $N = 2$: the orders $\hat 0\hat i\hat 0\hat j$, $\hat i\hat 0\hat 0\hat j$, $\hat 0\hat i\hat j\hat 0$ and $\hat i\hat 0\hat j\hat 0$ have equal squares, giving $+4\sum_{i,j}(R_{\hat 0\hat i\hat 0\hat j})^2$.
5. $N = 1$: the $\hat 0$ can sit in any of four slots, and pair antisymmetry and pair exchange make each square equal to some $(R_{\hat 0\hat i\hat j\hat k})^2$, giving $-4\sum_{i,j,k}(R_{\hat 0\hat i\hat j\hat k})^2$.
6. $N = 0$ gives $+\sum_{i,j,k,l}(R_{\hat i\hat j\hat k\hat l})^2$.

**Result:** $\mathcal K = 4\sum_{i,j}(R_{\hat 0\hat i\hat 0\hat j})^2 - 4\sum_{i,j,k}(R_{\hat 0\hat i\hat j\hat k})^2 + \sum_{i,j,k,l}(R_{\hat i\hat j\hat k\hat l})^2$.

### In vacuum, space follows the tides · working

**Goal:** Show that in vacuum $\sum(R_{\hat i\hat j\hat k\hat l})^2 = 4\sum(R_{\hat 0\hat i\hat 0\hat j})^2$.

1. Write $\mathcal E_{ij} = R_{\hat 0\hat i\hat 0\hat j}$, symmetric by pair exchange. Spatial components are antisymmetric in $ij$ and in $kl$, so in three dimensions $R_{\hat i\hat j\hat k\hat l} = \epsilon_{ijm}\epsilon_{kln}S_{mn}$ with $S_{mn}$ symmetric by pair exchange.
2. Contract one index of each pair: $\sum_i R_{\hat i\hat j\hat i\hat l} = \sum_i\epsilon_{ijm}\epsilon_{iln}S_{mn} = \delta_{jl}\,\mathrm{tr}\,S - S_{jl}$.
3. The Ricci components are $R_{\hat 0\hat 0} = \sum_i R_{\hat i\hat 0\hat i\hat 0} = \mathrm{tr}\,\mathcal E$ and $R_{\hat j\hat l} = -\mathcal E_{jl} + \delta_{jl}\,\mathrm{tr}\,S - S_{jl}$.
4. Vacuum sets both to zero. The first gives $\mathrm{tr}\,\mathcal E = 0$; the trace of the second then gives $2\,\mathrm{tr}\,S = 0$, and the second itself gives $S = -\mathcal E$.
5. So $\sum(R_{\hat i\hat j\hat k\hat l})^2 = \sum\epsilon_{ijm}\epsilon_{kln}\epsilon_{ijp}\epsilon_{klq}S_{mn}S_{pq} = 4\sum S_{mn}^2 = 4\sum\mathcal E_{mn}^2$.
6. Insert this into the orthonormal expansion: the tidal and spatial terms together give $8\sum\mathcal E_{ij}^2$.

**Result:** In vacuum, $\mathcal K = 8\sum_{i,j}(R_{\hat 0\hat i\hat 0\hat j})^2 - 4\sum_{i,j,k}(R_{\hat 0\hat i\hat j\hat k})^2$.

### Schwarzschild from six components · working

**Goal:** Find $\mathcal K$ outside a spherical mass from the orthonormal Riemann components of the Schwarzschild metric.

1. In the static orthonormal frame, with $q = GM/(c^2r^3)$, the components are taken on trust here. The tidal ones are $-2q$ for $R_{\hat t\hat r\hat t\hat r}$ and $q$ for both $R_{\hat t\hat\theta\hat t\hat\theta}$ and $R_{\hat t\hat\phi\hat t\hat\phi}$. The spatial ones are $2q$ for $R_{\hat\theta\hat\phi\hat\theta\hat\phi}$ and $-q$ for each pair of $\hat r$ with an angle. Components not related to these by index symmetries vanish.
2. No component has one time index, and the tidal matrix is $\mathrm{diag}(-2q, q, q)$, whose squares sum to $6q^2$.
3. The orthonormal expansion gives $4 \times 6q^2$ from the tidal terms and $4\,(4 + 1 + 1)\,q^2 = 24q^2$ from the spatial terms, each spatial pair appearing in four index orders.
4. The total is $48q^2$, matching the vacuum form $8 \times 6q^2$.

**Result:** $\mathcal K = 48G^2M^2/(c^4r^6)$, which equals $12/r_s^4$ at $r_s = 2GM/c^2$.

## Worked examples

### Earth against a black hole's horizon · working

**Problem:** Treat Earth as a static sphere with $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ and radius 6371 km. Find $\mathcal K$ at its surface and the length $\mathcal K^{-1/4}$. Then find the mass of a non-rotating black hole whose horizon has the same $\mathcal K$.

1. $GM/r^3 = 3.986\times10^{14}/(6.371\times10^{6})^3 = 1.541\times10^{-6}\ \mathrm{s^{-2}}$.
2. $\mathcal K = 48\,(GM/r^3)^2/c^4 = 48\times(1.541\times10^{-6})^2/(2.998\times10^{8})^4 = 1.41\times10^{-44}\ \mathrm{m^{-4}}$.
3. $\mathcal K^{-1/4} = 9.2\times10^{10}$ m, about 0.61 au, with $1\ \mathrm{au} = 1.496\times10^{11}$ m.
4. At a horizon $\mathcal K = 12/r_s^4$, so equal values need $r_s = (12/\mathcal K)^{1/4} = 1.71\times10^{11}$ m.
5. $M = r_sc^2/2G = 1.15\times10^{38}$ kg, about $5.8\times10^{7}$ solar masses.

**Answer:** $\mathcal K \approx 1.4\times10^{-44}\ \mathrm{m^{-4}}$ at Earth's surface, the same as at the horizon of a black hole of about 58 million solar masses.

**Takeaway:** Because $\mathcal K$ at a horizon falls as $M^{-4}$, the horizon of a very massive black hole can be no more strongly curved than the ground under your feet.

## Problems

### `ball-half-as-wide` · entry · difficulty 1 · conceptual

On a smooth ball, carry an arrow around a tiny loop without letting it swing. The arrow's turn is proportional to the loop's area divided by the ball's whole surface area. A second ball is half as wide. On it you walk a tiny loop with exactly the same area. How many times bigger is the turn? How many times bigger is the Kretschmann scalar?

**Hints**

1. When a ball is half as wide, every length on it halves. What happens to its whole surface?
2. For small turns, the change in the arrow grows in step with the turn, and so does each entry of the curvature table. What happens to the square of a number that becomes 4 times bigger?

**Answer:** The turn is 4 times bigger, and the Kretschmann scalar is 16 times bigger.

**Must contain:** The smaller ball has a quarter of the surface; The same loop area is 4 times the fraction, so the turn is 4 times bigger; Every entry is 4 times bigger, so every square and the scalar are 16 times bigger

**Numeric:** ratio of turns = 4 1 (magnitude, ±1%); ratio of Kretschmann scalars = 16 1 (magnitude, ±1%)

**Solution**

1. Halving every length makes every area a quarter as big, so the smaller ball has a quarter of the surface.
2. The loop's area is therefore 4 times as big a fraction of the smaller ball's surface, so the arrow turns 4 times as much.
3. For such small turns, the change in the arrow grows in step with the turn. The loop's area is unchanged, so every entry of the table, a change divided by the area, is 4 times bigger.
4. Squaring each entry makes it 16 times bigger, so the sum of the squares, the Kretschmann scalar, is 16 times bigger.

### `expanding-universe-scalars` · working · difficulty 2 · calculation

A spatially flat universe has scale factor $a(t)$. In the orthonormal frame of comoving observers the nonzero components, up to index symmetries, are $R_{\hat t\hat i\hat t\hat i} = -\ddot a/(c^2a)$ for each $i$ and $R_{\hat i\hat j\hat i\hat j} = \dot a^2/(c^2a^2)$ for each pair $i \ne j$. (a) Show that $\mathcal K = 12[(\ddot a/a)^2 + (\dot a/a)^4]/c^4$ and $R = 6(\ddot a/a + \dot a^2/a^2)/c^2$. (b) Evaluate both for dust, $a \propto t^{2/3}$, and radiation, $a \propto t^{1/2}$. (c) What happens as $t \to 0$?

**Hints**

1. There are no components with one time index. Use the orthonormal expansion, counting how many tidal and spatial components there are.
2. For $a \propto t^p$, $\dot a/a = p/t$ and $\ddot a/a = p(p-1)/t^2$.

**Answer:** (b) Dust: $\mathcal K = 80/(27c^4t^4)$ and $R = 4/(3c^2t^2)$. Radiation: $\mathcal K = 3/(2c^4t^4)$ and $R = 0$. (c) In both cases $\mathcal K$ grows as $t^{-4}$, a curvature singularity at $t = 0$, although the radiation universe has $R = 0$ at every time.

**Must contain:** Three tidal components and three spatial pairs, each squared term counted four times; The Kretschmann scalar times c to the fourth times t to the fourth is 80/27 for dust and 3/2 for radiation; The radiation universe has zero Ricci scalar but nonzero Kretschmann scalar; The Kretschmann scalar diverges as t goes to zero

**Numeric:** dust: Kretschmann scalar times c to the fourth times t to the fourth = 2.963 1 (magnitude, ±1%); radiation: Kretschmann scalar times c to the fourth times t to the fourth = 1.5 1 (magnitude, ±1%); radiation: Ricci scalar times c squared times t squared = 0 1 (magnitude, ±0.01)

**Solution**

1. The tidal matrix is $-(\ddot a/a)/c^2$ times the identity, so $4\sum(R_{\hat t\hat i\hat t\hat j})^2 = 12(\ddot a/a)^2/c^4$.
2. Each of the three spatial pairs appears in four index orders, so $\sum(R_{\hat i\hat j\hat k\hat l})^2 = 12(\dot a/a)^4/c^4$. Isotropy leaves no component with one time index.
3. Adding gives $\mathcal K = 12[(\ddot a/a)^2 + (\dot a/a)^4]/c^4$.
4. $R_{\hat t\hat t} = \sum_i R_{\hat i\hat t\hat i\hat t} = -3\ddot a/(c^2a)$ and $R_{\hat i\hat i} = -R_{\hat t\hat i\hat t\hat i} + \sum_{j \ne i}R_{\hat j\hat i\hat j\hat i} = (\ddot a/a + 2\dot a^2/a^2)/c^2$, so $R = -R_{\hat t\hat t} + \sum_i R_{\hat i\hat i} = 6(\ddot a/a + \dot a^2/a^2)/c^2$.
5. Dust, $p = 2/3$: $\dot a/a = 2/(3t)$ and $\ddot a/a = -2/(9t^2)$, so $\mathcal K = 12(4/81 + 16/81)/(c^4t^4) = 80/(27c^4t^4)$ and $R = 6(-2/9 + 4/9)/(c^2t^2) = 4/(3c^2t^2)$.
6. Radiation, $p = 1/2$: $\dot a/a = 1/(2t)$ and $\ddot a/a = -1/(4t^2)$, so $\mathcal K = 12(1/16 + 1/16)/(c^4t^4) = 3/(2c^4t^4)$ and $R = 6(-1/4 + 1/4)/(c^2t^2) = 0$.
7. As $t \to 0$ both values of $\mathcal K$ grow without bound, so no coordinate change can remove the big bang singularity.

**Targets:** `ricci-zero-means-no-curvature`

### `plane-wave-invisible-to-invariants` · formal · difficulty 3 · proof

Set $G = c = 1$ and take $ds^2 = -2\,du\,dv + dx^2 + dy^2 + A(u)(x^2 - y^2)\,du^2$. (a) Show that, up to index symmetries, the only nonzero Riemann components are $R_{uxux} = -A$ and $R_{uyuy} = A$, and that the metric is vacuum. (b) Prove that every complete contraction of products of Riemann tensors formed with $g^{\mu\nu}$ vanishes.

**Hints**

1. Only $g_{uu}$ depends on position. Compute $\Gamma_{\sigma\mu\nu}$ with every index down, then raise with $g^{uu} = 0$, $g^{uv} = -1$, $g^{vv} = -A(x^2 - y^2)$.
2. Through $g^{-1}$, which slot can a $u$ slot be paired with?

**Answer:** (a) $R^x{}_{uxu} = \partial_x\Gamma^x{}_{uu} = -A$ and $R^y{}_{uyu} = A$, so $R_{uu} = 0$ and all other Ricci components vanish. (b) Since $g^{uu} = 0$, a $u$ slot pairs only with a $v$ slot, and no nonzero component has one, so every term has a zero factor.

**Must contain:** No Christoffel symbol has an upper u index; The inverse metric has no u-u entry, so contractions pair u slots only with v slots, and no nonzero component has a v slot

**Solution**

1. With every index down, the nonzero symbols are $\Gamma_{uuu} = \tfrac12\partial_uH$, $\Gamma_{uux} = \Gamma_{uxu} = Ax$, $\Gamma_{uuy} = \Gamma_{uyu} = -Ay$, $\Gamma_{xuu} = -Ax$ and $\Gamma_{yuu} = Ay$, with $H = A(x^2 - y^2)$.
2. Raising the first index gives $\Gamma^x{}_{uu} = -Ax$, $\Gamma^y{}_{uu} = Ay$ and $\Gamma^v{}_{\mu\nu} = -\Gamma_{u\mu\nu}$; every $\Gamma^u{}_{\mu\nu}$ vanishes.
3. $R^x{}_{uxu} = \partial_x\Gamma^x{}_{uu} - \partial_u\Gamma^x{}_{xu} + \Gamma^x{}_{x\lambda}\Gamma^\lambda{}_{uu} - \Gamma^x{}_{u\lambda}\Gamma^\lambda{}_{xu} = -A$, since the product terms need $\Gamma^x{}_{x\lambda}$ or $\Gamma^u{}_{xu}$, which vanish. Likewise $R^y{}_{uyu} = A$, and lowering with $g_{xx} = g_{yy} = 1$ gives $R_{uxux} = -A$, $R_{uyuy} = A$.
4. $R_{uu} = R^x{}_{uxu} + R^y{}_{uyu} = 0$, and every other Ricci component contains a vanishing Riemann component, so the metric is vacuum for every $A(u)$.
5. Write every factor with its indices down; a complete contraction pairs slots through $g^{\mu\nu}$. Since $g^{uu} = 0$, a $u$ slot pairs only with a $v$ slot. Every nonzero component has $u$ slots and no $v$ slot, so every term of the contraction contains a vanishing factor.

**Targets:** `zero-kretschmann-means-flat`

## Observations

- **Flares from stars torn apart by the tides of supermassive black holes, found in time-domain sky surveys** (measured, working). A star is torn apart roughly where the black hole's tidal stretch across it beats its own gravity, near $r_t \approx R_*(M/m_*)^{1/3}$. At a horizon $\mathcal K = 12/r_s^4$ falls as $M^{-4}$ and the tidal stretch as $M^{-2}$, so above a limiting mass a star crosses the horizon of a non-rotating hole before it is disrupted, and no flare escapes. *Numbers:* Setting $r_t = r_s$ for a Sun-like star gives about $1\times10^{8}$ solar masses; black-hole spin and the star's structure shift this by factors of order one. Observed flares come mainly from black holes below this mass. *Reference:* Suvi Gezari (2021), *Tidal Disruption Events*, Annual Review of Astronomy and Astrophysics 59, 21–58, doi:10.1146/annurev-astro-111720-030029

## Teaching arc

1. **Ask how different descriptions can agree** (entry). Ask how two people who choose different directions can agree on how curved a place is, then turn the squared paper under the pencil. *Why:* The invariant idea is easiest to own with a pencil before it meets a curvature table. *Predict:* If you turn the paper under the pencil, will the sum of the squared counts change? *Visual:* [[pencil-on-turning-squared-paper]] *Uses:* `ways_in/square-and-add`, `problems/ball-half-as-wide`
2. **Measure it with falling crumbs** (entry). Let a falling crew read the stretch, then halve the distance and ask for the new scalar. *Why:* It turns the scalar into something a crew could measure, and exposes the linear-scaling guess. *Predict:* If the crew gets twice as close to the centre, how many times bigger is the Kretschmann scalar? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/read-it-from-the-stretch`, `checks/halve-the-distance`
3. **Separate the map from the place** (entry). Show the rectangular world map near the pole, then the black-hole formula's infinite number beside the finite scalar at the horizon. *Why:* It prevents the belief that a horizon is a place of infinite curving. *Predict:* Where the usual formula gives an infinite number, at the horizon, is the Kretschmann scalar infinite too? *Visual:* [[three-gauges-on-a-falling-probe]] *Uses:* `ways_in/a-map-can-blow-up`, `checks/crushed-at-the-horizon`, `checks/bigger-black-hole`
4. **Contract and compute** (working). Build the orthonormal expansion, then the Schwarzschild value, and compare a diverging coordinate component with the scalar. *Why:* Signs from time indices and basis-vector divergences are where calculations go wrong. *Uses:* `ways_in/contract-every-index`, `derivations/schwarzschild-from-six-components`, `checks/component-blows-up-at-horizon`, `checks/ricci-zero-outside-a-star`
5. **Mark the limits** (formal). State what an unbounded invariant certifies, then show the plane wave whose invariants all vanish. *Why:* It stops finite or zero invariants being read as proofs of regularity or flatness. *Uses:* `ways_in/what-invariants-certify`, `ways_in/invariants-that-all-vanish`, `checks/finite-is-not-regular`

## Misconceptions

### “Twice as close to a planet's centre, while still outside it, the curving is twice as strong.” · entry · `twice-as-close-twice-as-curved`

- **Why it is tempting:** Getting closer feels like it should make things stronger in the same proportion.
- **What is true:** Outside the planet the stretch grows eight times when the distance halves, and the Kretschmann scalar, built from squares, grows sixty-four times.
- **Exposed by:** `checks/halve-the-distance`

### “At a black hole's horizon something becomes infinite and crushes you.” · entry · `horizon-is-infinite`

- **Why it is tempting:** The usual formula for a black hole really does give an infinite number there, and films show the edge as violent.
- **What is true:** The infinite number belongs to the formula's map, and the Kretschmann scalar has an ordinary value at the horizon. Near a small black hole that ordinary value can still pull a body apart, but nothing there is infinite.
- **Exposed by:** `checks/crushed-at-the-horizon`

### “A bigger black hole has a more violent horizon.” · entry · `bigger-hole-harsher-edge`

- **Why it is tempting:** Heavier sounds stronger in every way.
- **What is true:** The stretch at a horizon is in step with the mass divided by the cube of the horizon's size, and that size grows in step with the mass. So ten times the mass gives one hundredth of the stretch, and a Kretschmann scalar ten thousand times smaller.
- **Exposed by:** `checks/bigger-black-hole`

### “If a component of the Riemann tensor diverges somewhere, spacetime is singular there.” · working · `diverging-component-means-singular`

- **Why it is tempting:** Components are the numbers we actually compute, and an infinity in them looks physical.
- **What is true:** A component in a coordinate basis inherits any divergence of the basis vectors, as the radial-angular component does at the Schwarzschild horizon. The Kretschmann scalar, which has no basis, stays finite there.
- **Exposed by:** `checks/component-blows-up-at-horizon`

### “Outside a star the Ricci scalar is zero, so there is no curvature to measure.” · working · `ricci-zero-means-no-curvature`

- **Why it is tempting:** The Ricci scalar is the first curvature scalar most learners meet, and in vacuum it is zero.
- **What is true:** The vacuum equation sets only the Ricci contraction to zero; the rest of the Riemann tensor carries the tides. The Kretschmann scalar sees that curvature.
- **Exposed by:** `checks/ricci-zero-outside-a-star`

### “If the Kretschmann scalar vanishes at a point, spacetime is flat there.” · formal · `zero-kretschmann-means-flat`

- **Why it is tempting:** For a positive-definite metric it is a sum of squares, and zero does force flatness.
- **What is true:** In Lorentzian signature some squares subtract and null structure can cancel everything. A plane gravitational wave has every scalar invariant zero yet real tides.
- **Exposed by:** `checks/zero-is-not-flat`

### “If every curvature invariant stays finite, spacetime has no singularity.” · formal · `finite-invariants-mean-regular`

- **Why it is tempting:** Divergent invariants certify singularities, so finite ones seem to certify regularity.
- **What is true:** Only the forward direction is a theorem; regularity needs an explicit extension. Singular plane waves and conical defects keep every invariant bounded.
- **Exposed by:** `checks/finite-is-not-regular`

## Checks

1. **Entry · numeric** `checks/halve-the-distance`. A crew falls freely, directly toward the centre of a round planet that does not spin. At 20,000 kilometres from the centre they work out the Kretschmann scalar from their stretch reading. Later they are 10,000 kilometres from the centre, still outside the planet. How many times bigger is the scalar now?
   - **Hints:** First find how much bigger the stretch is.
   - **Answer:** 64 times bigger. At half the distance, the pull is 4 times as strong, because the pull weakens with the square of the distance. One metre is also twice as big a part of the whole distance. So the extra pull on a crumb 1 metre nearer is twice as big a share of that stronger pull. So the stretch, the extra pull for each metre of gap, is 4 times 2, which is 8 times bigger. Every entry of the curvature table is a fixed multiple of the stretch, so every entry is 8 times bigger. Every square is then 64 times bigger, whether it is added or subtracted, so the scalar is 64 times bigger.
   - **Must contain:** The pull is 4 times as strong; The stretch is 8 times bigger; The scalar, built from squares, is 64 times bigger
   - **Numeric:** ratio of Kretschmann scalars = 64 1 (magnitude, ±2%)
   - **Targets:** `twice-as-close-twice-as-curved`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · evaluate-claim** `checks/crushed-at-the-horizon`. A friend says: "The usual formula for a black hole that does not spin gives an infinite number at the horizon. So anyone who falls in is crushed by infinite curving right there." Is your friend right?
   - **Answer:** No. Everyone gets the same Kretschmann scalar at a place, whatever map of space and time they use. A crew falling directly toward the black hole's centre works out the scalar at the horizon from its stretch reading and gets an ordinary value, not an infinite one. So this test finds no infinite curving at the horizon. The usual formula's labels suit people who hover with rockets, and nobody can hover at the horizon, so those labels fail there. A better map, drawn for a crew falling in, has no infinite number there at all. An ordinary value is not always a gentle one: at the horizon of a black hole a few times as heavy as the Sun, the stretch would still pull a person apart. The scalar grows without limit only as the crew nears the centre.
   - **Must contain:** The Kretschmann scalar is the same for every map; It is finite at the horizon; A better map has no infinite number at the horizon
   - **Targets:** `horizon-is-infinite`
   - **Visual:** [[three-gauges-on-a-falling-probe]]
3. **Entry · numeric** `checks/bigger-black-hole`. Black hole B has 10 times the mass of black hole A, and neither spins. A circle drawn around B's horizon is 10 times as long as one around A's. Outside a round body that does not spin, the stretch at a place follows a rule. It is a fixed number times the body's mass, divided by the cube of the length of a circle drawn around the centre through that place. How do the stretch and the Kretschmann scalar at B's horizon compare with those at A's horizon?
   - **Answer:** At B's horizon the stretch is one hundredth as strong and the Kretschmann scalar is one ten-thousandth as big. The mass is 10 times bigger, which on its own makes the stretch 10 times stronger. The circle is 10 times as long, and 10 cubed is 1,000, which on its own makes the stretch 1,000 times weaker. Together the stretch is 10 divided by 1,000, one hundredth as strong. Every entry of the table is a fixed multiple of the stretch, so every square, and the scalar, is one hundredth times one hundredth: one ten-thousandth as big.
   - **Must contain:** Ten times the mass makes the stretch 10 times stronger; Ten times the circle's length makes it 1,000 times weaker; The stretch is one hundredth and the scalar one ten-thousandth
   - **Numeric:** stretch at B divided by stretch at A = 0.01 1 (magnitude, ±2%); Kretschmann scalar at B divided by that at A = 0.0001 1 (magnitude, ±2%)
   - **Targets:** `bigger-hole-harsher-edge`
4. **Working · numeric** `checks/horizon-curvature-length`. A crew falls radially into a non-rotating black hole of 10 solar masses. Crossing the horizon, it measures a radial relative acceleration of 103 million metres per second squared for each metre of separation, transverse squeezes of half that, and no curvature components with one time index. Find the Kretschmann scalar there and the length equal to its inverse fourth root. Check the result against twelve divided by the fourth power of the Schwarzschild radius.
   - **Hints:** Use the vacuum form with no one-time components.
   - **Answer:** The tidal matrix is $R_{\hat 0\hat i\hat 0\hat j} = \mathrm{diag}(-2q, q, q)$ with $2q = 1.03\times10^{8}/c^2 = 1.146\times10^{-9}\ \mathrm{m^{-2}}$. The vacuum form gives $\mathcal K = 8 \times 6q^2 = 12(2q)^2 = 1.58\times10^{-17}\ \mathrm{m^{-4}}$, so $\mathcal K^{-1/4} = 15.9$ km. With $r_s = 2GM/c^2 = 29.5$ km, $12/r_s^4 = 1.58\times10^{-17}\ \mathrm{m^{-4}}$ as well.
   - **Must contain:** Divide the measured accelerations by c squared to get the tidal components; The Kretschmann scalar is eight times the summed squares, which is twelve times the radial component squared; Its inverse fourth root is about 15.9 kilometres, matching twelve over the fourth power of the Schwarzschild radius
   - **Numeric:** length equal to the inverse fourth root of the Kretschmann scalar = 15.9 km (magnitude, ±2%)
5. **Working · evaluate-claim** `checks/component-blows-up-at-horizon`. In Schwarzschild coordinates, $R_{r\theta r\theta} = -m/(r - 2m)$ with $m = GM/c^2$. A student concludes that $r = 2m$ is a curvature singularity. Evaluate the claim.
   - **Answer:** The claim is wrong. $R_{r\theta r\theta} = g_{rr}\,r^2R_{\hat r\hat\theta\hat r\hat\theta}$, and the orthonormal component $-m/r^3$ is finite at $r = 2m$. The divergence comes from $g_{rr} = (1 - 2m/r)^{-1}$, the squared length of the basis vector $\partial_r$, which fails at the horizon. A scalar has no basis to inherit that failure, and $\mathcal K = 48m^2/r^6 = 3/(4m^4)$ there. What proves the horizon regular is a chart, such as ingoing Eddington–Finkelstein coordinates, in which every metric component is finite and the metric nondegenerate at $r = 2m$.
   - **Must contain:** The coordinate component is the radial metric coefficient times r squared times a finite orthonormal component; The Kretschmann scalar is 3 divided by 4 m to the fourth at the horizon; Regularity is shown by a chart that covers the horizon
   - **Targets:** `diverging-component-means-singular`
6. **Working · explain** `checks/ricci-zero-outside-a-star`. Neglecting the cosmological constant, the Ricci scalar outside the Sun is exactly zero at every radius. Can it tell you how strongly spacetime is curved 1 au from the Sun? What can?
   - **Answer:** No. The vacuum Einstein equation sets $R_{\mu\nu} = 0$, so $R = 0$ at every radius, near and far. The Riemann tensor is not zero: its tidal components $\mathrm{diag}(-2, 1, 1)\,GM/(c^2r^3)$ produce measurable tides. The Kretschmann scalar sees them: $\mathcal K = 48G^2M^2/(c^4r^6) = 9.3\times10^{-60}\ \mathrm{m^{-4}}$ at 1 au. A radiation-filled universe shows the same failure, with $R = 0$ but $\mathcal K \neq 0$.
   - **Must contain:** Vacuum sets the Ricci tensor and scalar to zero at every radius; The tidal part of the Riemann tensor survives; The Kretschmann scalar is about 9.3e-60 per metre to the fourth at 1 au
   - **Targets:** `ricci-zero-means-no-curvature`
   - **Visual:** [[six-entry-curvature-table]]
7. **Formal · evaluate-claim** `checks/zero-is-not-flat`. Evaluate the claim: "If the Kretschmann scalar vanishes at a point, the Riemann tensor vanishes there." Treat positive-definite and Lorentzian metrics separately, and give a Lorentzian counterexample.
   - **Hints:** Write $\mathcal K$ in an orthonormal frame for each signature.
   - **Answer:** For a positive-definite metric, $\mathcal K = \sum(R_{abcd})^2$ in an orthonormal frame, so $\mathcal K = 0$ forces every component to vanish, and the claim holds. For a Lorentzian metric the frame expansion subtracts $4\sum(R_{\hat 0\hat i\hat j\hat k})^2$, so terms can cancel, and null structure can kill every contraction at once. The plane wave $ds^2 = -2\,du\,dv + dx^2 + dy^2 + A(u)(x^2 - y^2)\,du^2$ has $R_{uxux} = -A \neq 0$ and real tides, yet $g^{uu} = 0$ forces every complete contraction, $\mathcal K$ included, to vanish. The claim fails. $\mathcal K$ is not even sign-definite: on the axis of a Kerr black hole with $a > M/2$ it is negative just outside the horizon.
   - **Must contain:** Positive-definite: K is a sum of squares, so the claim holds; Lorentzian: squares with one time index subtract; Plane wave: curved, with every scalar invariant zero; K can be negative, as near the axis of a rapidly spinning Kerr black hole
   - **Targets:** `zero-kretschmann-means-flat`
8. **Formal · explain** `checks/finite-is-not-regular`. Along an infalling geodesic of finite affine length in the Schwarzschild spacetime, the Kretschmann scalar grows without bound as the radial coordinate goes to zero. Explain what that proves, why the finite value at the horizon does not by itself prove the horizon regular, and what does prove it.
   - **Hints:** What does continuity of the metric's second derivatives imply for frame components near a boundary point?
   - **Answer:** If the metric extended as a $C^2$ metric through an endpoint $p$ of the geodesic, the Riemann components in a continuous frame would be continuous and hence bounded near $p$, and so would $\mathcal K$. Since $\mathcal K = 48M^2/r^6$ is unbounded as the geodesic reaches $r \to 0$ at finite proper time, no such extension exists. The converse is not a theorem: bounded invariants are compatible with singular behaviour, as in the plane waves with $A = \alpha/u^2$, whose invariants all vanish while parallel-frame tidal components diverge, and at conical defects, where nearby curvature vanishes. Regularity at $r = 2M$, where $\mathcal K = 3/(4M^4)$, is proven by exhibiting a chart, such as ingoing Eddington–Finkelstein coordinates, in which the metric is smooth and nondegenerate across the horizon.
   - **Must contain:** A C2 extension would make every polynomial invariant bounded near the endpoint; r to 0 is reached at finite proper time with K unbounded, so no such extension exists; Bounded invariants do not imply extendibility: singular plane waves and conical defects; The horizon is shown regular by an explicit chart
   - **Targets:** `finite-invariants-mean-regular`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Symbol for the Kretschmann scalar | This course writes $\mathcal K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ and keeps $K$ for Gaussian and sectional curvature, scoping the symbol as the conventions require. | Some texts write $K$, $I$ or just $R_{abcd}R^{abcd}$, and $K$ may name Gaussian curvature in the same text. |
| Mass or Schwarzschild radius in the Schwarzschild value | $\mathcal K = 48G^2M^2/(c^4r^6)$, which is $48M^2/r^6$ with $G = c = 1$ and $12r_s^2/r^6$ with $r_s = 2GM/c^2$. | Reading $M$ as the Schwarzschild radius, or $r_s$ as $GM/c^2$, changes the coefficient by a factor of 4; check which length a symbol stands for. |

## Visuals

- ★ [[three-gauges-on-a-falling-probe]] (flagship): The horizon test: metric numbers that blow up at the horizon beside a Kretschmann gauge that stays finite there. *Sketch:* A probe falls radially into a non-spinning black hole. Three gauges track it: the usual radial metric coefficient, rising without bound at the horizon; $\mathcal K$ on a log scale, smooth through the horizon and diverging only as $r \to 0$; and the head-to-feet stretch on a cartoon body. A map switch redraws the first gauge in coordinates for a falling crew, where it stays finite, while the $\mathcal K$ gauge is unchanged.
- [[pencil-on-turning-squared-paper]] (core): The entry picture of an invariant. *Sketch:* A pencil on squared paper that the learner turns. Readouts give the across and along counts and the sum of their squares: the counts change, the sum does not. A second panel turns the directions under a small symmetric table of numbers and shows its entries changing while the sum of their squares stays fixed.
- [[falling-ring-of-crumbs]] (supporting): Stretch readings that fix the Kretschmann scalar outside a round body. *Sketch:* A ring of freely falling crumbs near a round mass stretches along the line to the centre and squeezes across it. Sliders set mass and distance; readouts show the stretch and the Kretschmann scalar relative to a starting value, reading 8 and 64 when the distance halves.
- [[six-entry-curvature-table]] (supporting): A sandbox for the orthonormal expansion and for curvature the Ricci tensor misses. *Sketch:* Six sliders set the orthonormal components $R_{\hat a\hat b\hat a\hat b}$ for the six index pairs. Readouts show the Ricci components, $R$ and $\mathcal K$. A Schwarzschild preset, $q(-2, 1, 1, -1, -1, 2)$ in the order $tr, t\theta, t\phi, r\theta, r\phi, \theta\phi$, gives zero Ricci tensor and $\mathcal K = 48q^2$.

## Tutor moves

**Open with**

- Imagine falling into a black hole millions of times heavier than the Sun. At the moment you cross its horizon, would something dramatic happen to your body? *(prediction)*

**If the learner is stuck**

- *The learner mixes up how the pull, the stretch and the scalar change with distance.* → Build the chain one factor at a time: the pull a quarter, the fraction per metre a half, the stretch an eighth, every square a sixty-fourth. *Uses:* `ways_in/read-it-from-the-stretch`, `checks/halve-the-distance`

**Common questions**

- *Is the centre of a black hole a place I could steer around?* (entry) Not for a black hole that does not spin. Inside its horizon, every path, even one steered with the strongest rocket, ends at the centre, where the Kretschmann scalar grows without limit. In the same way, every path through time reaches tomorrow. So the centre is better pictured as a last moment than as a place. *Uses:* `ways_in/a-map-can-blow-up`

**Switching levels**

- To working when: asks how to compute it from components; uses index notation. Go to the full contraction, the orthonormal expansion and the Schwarzschild value. *Uses:* `ways_in/contract-every-index`, `derivations/schwarzschild-from-six-components`
- To formal when: asks whether a finite scalar proves a spacetime regular; asks whether zero means flat. Open the certification theorem and the plane-wave counterexample. *Uses:* `ways_in/what-invariants-certify`, `ways_in/invariants-that-all-vanish`
- To research when: asks how singularities are classified, or about quantum corrections to gravity. Open the research horizon. *Uses:* `research_horizon/classifying-singularities`, `research_horizon/curvature-squared-in-quantum-gravity`

**Pronunciations:** Kretschmann → KRETCH-mahn; Riemann → REE-mahn; Schwarzschild → SHVARTS-shilt; Eddington–Finkelstein → EDD-ing-tun FINK-el-stine; Brinkmann → BRINK-mahn; Lemaître → luh-MET-ruh; Weyl → VILE

## History

- **Erich Kretschmann (1917).** Argued that requiring physical laws to take the same form in every coordinate system restricts a theory far less than it seems. The curvature scalar in this note carries his name.
- **Georges Lemaître (1933).** Showed, with coordinates attached to freely falling observers, that the Schwarzschild solution is regular at $r = 2GM/c^2$, so the singularity there belongs to the coordinates. Georges Lemaître (1933), *L'univers en expansion*, Annales de la Société Scientifique de Bruxelles A 53, 51–85
- **Martin Kruskal, George Szekeres (1960).** Independently built coordinates covering the whole vacuum Schwarzschild geometry, in which the horizon is a regular null surface and only $r = 0$ remains singular. Martin D. Kruskal (1960), *Maximal extension of Schwarzschild metric*, Physical Review 119, 1743–1745, doi:10.1103/PhysRev.119.1743

## Research horizon

- **Classifying spacetime singularities.** A diverging scalar invariant marks only one class of singularity. Ellis and Schmidt separated these scalar polynomial curvature singularities from parallel-propagated ones, seen only in frame components along a curve, and from quasi-regular ones such as conical defects, all defined through incomplete curves. George F. R. Ellis, Bernd G. Schmidt (1977), *Singular space-times*, General Relativity and Gravitation 8, 915–953, doi:10.1007/BF00759240
- **Spacetimes that invariants cannot tell apart.** Every scalar polynomial invariant vanishes for a family of Kundt spacetimes that includes the pp-waves, and distinct metrics can share all their invariants. Deciding local equivalence then needs the Cartan–Karlhede procedure, which compares frame components of the Riemann tensor and finitely many of its derivatives. Vojtěch Pravda, Alena Pravdová, Alan Coley, Robert Milson (2002), *All spacetimes with vanishing curvature invariants*, Classical and Quantum Gravity 19, 6213–6236, doi:10.1088/0264-9381/19/23/318; Anders Karlhede (1980), *A review of the geometrical equivalence of metrics in general relativity*, General Relativity and Gravitation 12, 693–707, doi:10.1007/BF00771861
- **Curvature invariants that locate horizons.** With the course signature, $\nabla_\lambda R_{\mu\nu\rho\sigma}\nabla^\lambda R^{\mu\nu\rho\sigma} = 720M^2(r - 2M)/r^9$ in Schwarzschild, which vanishes exactly on the horizon. Invariants built from curvature and its derivatives give local markers for stationary horizons, including Kerr, whose event horizons are otherwise defined by the whole future of spacetime. Anders Karlhede, Ulf Lindström, Jan E. Åman (1982), *A note on a local effect at the Schwarzschild sphere*, General Relativity and Gravitation 14, 569–571, doi:10.1007/BF00756219; Majd Abdelqader, Kayll Lake (2015), *Invariant characterization of the Kerr spacetime: Locating the horizon and measuring the mass and spin of rotating black holes using curvature invariants*, Physical Review D 91, 084017, doi:10.1103/PhysRevD.91.084017
- **Squared curvature in quantum gravity.** Quantum corrections add curvature-squared terms to the action. In four dimensions $\mathcal K - 4R_{\mu\nu}R^{\mu\nu} + R^2$ integrates to $32\pi^2$ times the Euler characteristic of a compact Riemannian manifold, so it leaves the field equations unchanged. Pure gravity is finite on shell at one loop, diverges at two loops through a term cubic in the Riemann tensor, and adding $R^2$ and Weyl-squared terms makes it renormalizable at the price of a ghost. Gerard 't Hooft, Martinus J. G. Veltman (1974), *One-loop divergencies in the theory of gravitation*, Annales de l'Institut Henri Poincaré A 20, 69–94; Kellogg S. Stelle (1977), *Renormalization of higher-derivative quantum gravity*, Physical Review D 16, 953–969, doi:10.1103/PhysRevD.16.953; Marc H. Goroff, Augusto Sagnotti (1986), *The ultraviolet behavior of Einstein gravity*, Nuclear Physics B 266, 709–736, doi:10.1016/0550-3213(86)90193-8

## Review: novice

**Verdict:** fixed (2026-09-13, revision 6)

**Retell attempt:** FIRST READING (of the revision-1 draft). If you put a pencil on squared paper, the counts across and along change when you turn the paper, but 3 squared plus 4 squared stays 25 because that is the length squared. The curvature table is like that: its numbers change with your directions, but square them all and add them and you get the Kretschmann scalar, which everybody agrees on. I didn't get how a change 'is a small arrow' with parts, why each tilt counts twice, why the total really can't change, or what 'scalar' means. A falling crew measures the stretch between two crumbs, and halving the distance makes the scalar 64 times bigger, though I lost the 'one metre is half as big a part' step. A black hole formula blows up at the horizon like a world map at the pole, but the scalar is finite there, so it's the map's fault, and it only blows up at the centre. I don't know why the formula blows up in the first place, or whether that means falling in is safe.

INDEPENDENT RE-READ OF THE WHOLE ENTRY SURFACE (revision 5, same persona, no memory of the earlier read assumed). You put a short pencil on squared paper so its ends sit on corners, 3 across and 4 along, and it is 5 centimetres long. Turn the paper under it and the counts become 5 and 0, but 9 plus 16 and 25 plus 0 are both 25, because that is the length squared and turning the paper cannot change the length. The lines of the paper are your directions, and a number that survives changing them is an invariant. The curvature table is the same story: you pick directions at right angles, walk tiny loops tilted along pairs of them, carry an arrow round without letting it swing, and the short arrow from the starting tip to the returned tip is the change. Square every entry, add them up, and you get the Kretschmann scalar, which everyone agrees on; the full reason is taken on trust. With time in the picture some squares are subtracted instead. A crew falling straight down toward a planet drops two crumbs on the line to the centre, times how fast the gap opens, and calls the extra pull per metre the stretch; the stretch fixes the whole table, so it fixes the scalar. Twice as far out the pull is a quarter and the stretch an eighth, so the scalar is 64 times smaller. I had to read 'nearer by one part in the whole distance' twice before I saw it meant one metre out of the millions of metres to the centre. A flat world map spreads the North Pole along its whole top edge, so distances around the pole look endless there even though the ice is ordinary; the usual black-hole formula does the same thing at the horizon, because its labels are made for people hovering on rockets and nobody can hover there. The Kretschmann scalar is the fair test, and for a crew falling in it comes out ordinary at the horizon, the same as at the ground under my feet if the hole is 58 million suns. It only grows without limit as the crew nears the centre. What I could still not do: turn the paper to a slant that does not land on corners and say what the counts are then.

**Stumbles (34)**

- “with one change to the recipe when time is involved”: The summary names a change without saying what it is, and the entry ways never mention it again.
- “it is finite at the horizon and grows without limit only deeper in”: 'It' could be the black hole; and 'grows without limit only deeper in' reads as if it is infinite everywhere inside the horizon.
- “Pick a tilt for a tiny loop and a starting direction for an arrow. ... without swinging”: 'Tilt' and 'swinging' come from the prerequisite and are not restated or in this note's glossary.
- “Lay a pencil on squared paper whose squares are 1 centimetre wide.”: A real pencil is far longer than 5 centimetres, so the picture fails when tried.
- “Now turn the paper under the pencil until the pencil lies along a line of the paper.”: A rule the reader cannot follow: turning the paper freely moves the pencil's ends off the corners, and 'along a line' clashes with the count word 'along'.
- “This sum is the pencil's length squared, so no turn of the paper can change it.”: A step left implicit: why the length cannot change.
- “A number that stays the same however you choose your directions is called an invariant.”: 'Your directions' has not been linked to anything on the paper.
- “The curvature table has the same problem as the counts.”: 'Problem' is vague; nothing so far was a problem.
- “Each change in the table is a small arrow, and its parts along your chosen directions are the table's entries.”: Reread three times: how is a change an arrow, and where do the loop's tilts and the starting arrows come from?
- “Include each tilt twice, once for each way round the loop.”: The Riemann note says one way round is enough, so counting twice looks like an error with no reason.
- “This total is called the Kretschmann scalar.”: 'Scalar' is an unfamiliar word never explained.
- “Every change is an arrow whose squared parts add up to its length squared, so the total comes out the same for every choice of directions.”: A missing step: new directions also change which arrows and loops are tested, so the pencil rule alone does not give the conclusion the 'so' claims.
- “For a curved surface, or for space on its own, square every entry”: A teenager's first what-if is 'and for space and time?', and the way is silent; ways 2 and 3 then use the scalar in space and time.
- “Cut a paper strip exactly 5 squares long ... one end sits on a corner and the other end sits on the corner 3 squares across and 4 squares along.”: Not doable as written: a strip has width, so 'an end' is not a point, and the reader is not told how to find the slanted position.
- “The Kretschmann scalar comes from squaring the entries of the curvature table and adding them up.”: The recap for a way set in space and time repeats the plain recipe that the previous way limited to space alone, and never names tidal drift, the prerequisite's word for the pattern.
- “falling freely, straight toward the centre”: 'Straight' is a wording trap; here it means 'directly'.
- “The crew measures the extra pull on the nearer crumb for each metre of gap.”: A measurement without its method: the crew cannot read a pull off a crumb.
- “fix every entry of the curvature table from this one reading, which we take on trust here.”: Ambiguous 'which': the reading, or the fixing?
- “So the Kretschmann scalar depends only on the stretch. Each entry is a fixed multiple of the stretch.”: The 'so' comes before its reason, and the reader has just been told some squares may be subtracted, so 'every square 4 times bigger' does not obviously make the total 4 times bigger.
- “One metre is also half as big a part of the whole distance, so it changes the pull by half as big a fraction.”: Reread; the reader cannot see why a smaller share of the distance means a smaller share of the pull, nor how the quarter and the half combine into an eighth.
- “which grows 64 times when the distance halves.”: 'The distance' has no reference.
- “Look at a rectangular world map drawn as a grid of straight lines.”: Most classroom maps do not show the pole as an edge; the reader cannot tell which map is meant.
- “Near the top edge, the map enlarges the ground more and more, without limit.”: False for the first what-if: such a map does not enlarge distances toward the pole, only distances around it.
- “So a number that blows up in a description does not prove”: Two words for one idea: 'description', 'formula' and 'map' are used for the same thing without being tied together.
- “contains a number that becomes infinite at the horizon.”: A surprising claim with no reason: why would a formula blow up at a place where nothing happens?
- “gets an ordinary, finite value.”: No everyday number shows how ordinary the value is.
- “A better map, drawn for a crew falling in, has no infinite number at the horizon at all.”: A claim given without saying it is taken on trust.
- “The scalar grows without limit where the formula's distance to the centre shrinks to zero.”: 'The formula's distance' is unfamiliar and reread.
- “So anyone who falls in is crushed by infinite curving right there. (answer: No. ... gets an ordinary, finite value.)”: A false what-if: a reader who knows small black holes tear things apart would take 'No' to mean the horizon is always safe.
- “Halfway to the centre of a planet, the curving is twice as strong.”: Starting from the surface, halfway to the centre is inside the planet, where the stretch rule of the way does not apply.
- “B's horizon is 10 times as big around as A's. Just outside a round body, the stretch is proportional to the mass and weakens with the cube of the size around the centre at that place.”: 'Weakens with the cube' is ambiguous for a beginner, and 'size around' is a new measure not tied to anything.
- “a tiny loop turns a carried arrow in step with the fraction of the ball's whole surface that lies in the loop's small piece ... a tiny loop of exactly the same size”: 'The loop's small piece' is unclear, 'size' could mean width or area, and the carrying rule is missing.
- “every entry of the table, a turn divided by the area, is 4 times bigger”: An entry is a change divided by the area, not a turn; the link from turn to change is skipped.
- “Inside its horizon, every path that falls in reaches the spot”: First what-if: 'what if I fire a rocket outward?' The answer seems to allow escape for paths that do not fall in.

**Fixes**

- Summary split into short sentences, naming the space-and-time subtraction and scoping where the scalar grows without limit.
- Square and add: pencil stub; a doable turning rule; the change arrow built tail to tail; tilts and starting arrows tied to the chosen directions; why both ways round count; 'scalar' explained; the invariance claim now says the full reason is taken on trust instead of implying the pencil rule proves it (the old sentence skipped the change of tested arrows and loops). New try-it with marked dots.
- Judgement on the writer's question about the entry sign gap: the plain recipe stays scoped to surfaces and space in 'Square and add', and the subtraction is stated in words, with no rule, in its simplifies, in both later entry recaps, the summary and the glossary. 'Read it from the stretch' says the scaling holds whether a square is added or subtracted, so every entry check is answerable without the exact sign rule. This keeps one idea per way.
- Read it from the stretch: says how the crew measures the stretch, restates tidal drift, and spells out the quarter-times-a-half step with the 1.001 example used by the Riemann note.
- A map can blow up: named the kind of map, corrected 'enlarges the ground' to distances around the pole, tied 'formula' to 'map', gave the reason the usual labels fail (nobody can hover at the horizon), added the 58-million-solar-mass everyday comparison from the worked example, and marked the falling map as taken on trust.
- Checks: halve-the-distance and bigger-black-hole rewritten to match the ways and split over-long sentences; crushed-at-the-horizon now warns that an ordinary value can still be violent for a small black hole (10 solar masses gives about 100 million metres per second squared per metre, checked in python).
- Problem ball-half-as-wide restated with area and the carrying rule; its solution links turn to change. Entry common question and two entry misconceptions reworded for their what-ifs.
- Glossary: added loop, swing, tilt and tidal drift, copied or trimmed from the Riemann note so the two notes match; 'stretch' is now defined as the strength of tidal drift along the line toward the centre.
- Ladder: the working way 'Contract every index' defines the Ricci scalar as a trace before using it; 'Tidal readings fix the scalar' says 'gravity gradiometer' and gives rapidity 0.9 as a speed of 0.72c (tanh 0.9 = 0.716); the formal way 'What scalar invariants can and cannot certify' now opens by naming the way it continues.
- Budget: entry explanations would have reached about 1,280 words. To stay within the 10% review allowance I dropped, rather than squeezed: the flat-floor zero example, the explicit space-and-time paragraph in 'Square and add' (moved to its simplifies), the map's 6,400-times enlargement numbers, the across/along definition sentence, and the partial invariance argument. Two redundant linking sentences were also removed. In 'Read it from the stretch' the sentence about dividing by the gap was also dropped, since the definition of the stretch that follows says 'for each metre of gap'.
- Bumped the revision to 2 and set status novice-reviewed.

**Concerns**

- Entry explanations now sit at about 1,100 words, the review ceiling for core notes. Later reviews cannot add entry prose without cutting.
- The physics reviewer should confirm the new entry claims: the usual Schwarzschild labels suit hovering observers and fail because nobody can hover at the horizon; the 'longer version' of invariance for the choice of starting arrows and tilts; and that a 10-solar-mass horizon stretch would pull a person apart.
- 'Read it from the stretch' still carries two linked steps, the stretch fixing the scalar and the 64-times scaling. I judged the scaling an application of the first step, not a second idea, because the checks need both together.
- The Riemann note calls the effect 'tidal drift'; this note keeps 'stretch' for the reading of its strength along the line. The proposed visual falling-ring-of-crumbs should use both words in those two senses.
- Missing conventions reported by the writer still stand: the symbol for the Kretschmann scalar and the electric and magnetic Weyl parts.
- Independent re-read at revision 5 found seven stumbles, all recorded in the last rereads entry with ready rewrites and none applied. Two need entry-budget headroom that does not exist; four are word-for-word-neutral rule-5 consistency fixes; one is a judgement call left as is.
- The entry budget is the root cause of the two unfixable stumbles. Entry way explanations are at 1,099 words against a 1,000 cap, so the stage that is meant to add explicit steps for beginners has no room to add any. If the vault wants this note publishable and complete, an editor should decide which entry sentence to drop before the next edit pass, not the reviewer under a 1-word ceiling.
- The working rung still cannot be aligned with its prerequisite's glossary: scalar-invariant (needed_for working) has no note anywhere under knowledge/concepts/. The entry rung is unaffected, because it defines 'invariant' itself with the pencil picture.
- Ladder pass found no jump: 'Contract every index' opens by naming the squared-paper recipe of 'Square and add'; 'Tidal readings fix the scalar' opens with the falling crew of 'Read it from the stretch'; 'What scalar invariants can and cannot certify' opens with the scalar of 'Contract every index'; 'Every invariant vanishes, yet the wave is curved' opens with the positivity found in 'What scalar invariants can and cannot certify'. Index notation first appears at the working rung, which is allowed because index-notation reaches this note through the riemann-curvature-tensor prerequisite.
- The four entry routes are genuinely different: a pencil on turning paper (picture), a falling crew's stretch reading (operational), and a map that blows up where the ground does not (contrast).

**Re-read** (2026-09-13, revision 4): 4 stumbles in 7 changed passages

- “A crew falling directly toward the centre can work it out from its stretch reading, the extra pull on the nearer of two crumbs for each metre of gap.”: The recap has to stand alone, but it names no body, so 'the centre' has no reference. 'Nearer' does not say nearer to what, 'it' could mean the value rather than the scalar, and the sentence is 33 words, over the 32-word limit.
- “A crew falling directly toward the centre works out the scalar at the horizon from its stretch reading”: 'The centre' comes one paragraph after the black hole is named, so the reader has to look back to find what it is the centre of.
- “A crew falling directly toward the centre works out the scalar at the horizon (crushed-at-the-horizon answer)”: The same missing reference as in the way. The answer should match the way word for word.
- “the stretch there follows the mass divided by the cube of that size, so it is gentler.”: 'Follows' is vague. 'It' could be the horizon or the stretch. The step from ten times the mass to a smaller stretch is skipped, so the jump to ten thousand times smaller is taken on trust.
- Fix: A map can blow up, recap: split into two sentences; named the round body; 'it' became 'the scalar'; the stretch is now the pull on the crumb nearer that centre. The claim is unchanged.
- Fix: A map can blow up, explanation, and the crushed-at-the-horizon answer: 'the centre' became 'the black hole's centre'.
- Fix: bigger-hole-harsher-edge correction: replaced 'follows' with 'is in step with', removed the unclear 'it', and wrote out the one-hundredth step that the bigger-black-hole check uses. 'Gentler' is now carried by 'one hundredth of the stretch'. The scaling claim is unchanged.
- Fix: Read it from the stretch: the changed explanation sentence ('For this crew, ...') and the two-sentence takeaway read cleanly; no change.
- Fix: Bumped the revision to 4. Nothing was dropped for budget.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 5): 7 stumbles in 13 changed passages

- “A crumb 1 metre nearer the centre is nearer by one part in the whole distance.”: Reread, and the only one in the note that cost me the argument. 'One part in' normally takes a count: one part in six million. Here it takes a quantity, 'the whole distance', so the reader has to silently turn that distance into a number of metres before the fraction means anything. The prerequisite note does the same step with the number in it ('nearer the centre by one part in 6,371,000'), which is why it reads easily there and not here. Everything after it, including 'two such parts' and the quarter-of-a-half step, rests on this sentence.
- “Square the counts and add them. ... This sum is the pencil's length squared, and turning the paper cannot change the pencil's length. So no turn of the paper can change the sum.”: A step left implicit, and the first what-if a teenager tries. Turn the paper to any other angle and the pencil's ends land between corners, so there are no whole squares to count and 'the counts' cannot be read off at all. The claim that no turn changes the sum then looks untestable. The try-it does not close the gap, because it only ever lands on corners.
- “Its parts along your chosen directions, divided by the loop's area, are the table's entries.”: One word in two senses (rule 5). Here 'part' is a piece of the change arrow measured along a direction. In 'Read it from the stretch' and in the halve-the-distance answer, 'part' is a fraction: 'one part in the whole distance', 'two such parts', 'twice as big a part of the whole distance'.
- “this number is an ordinary size at the horizon (summary); The Kretschmann scalar, the same for every map, is an ordinary size at the horizon (takeaway of 'A map can blow up'); the Kretschmann scalar is an ordinary size at the horizon (correction of 'horizon-is-infinite')”: Two words for one idea, and one word for two ideas (rule 5). The explanation of 'A map can blow up' and the crushed-at-the-horizon answer both say the crew 'gets an ordinary value'; these three strings say 'an ordinary size' for the same thing. At the same time 'size' means a length in the bigger-hole-harsher-edge correction, 'the cube of the horizon's size, and that size grows in step with the mass'.
- “The arrow's turn is proportional to the loop's area divided by the ball's whole surface area.”: Two phrasings for one relation inside one problem (rule 5). The same problem's second hint and third solution step say 'the change in the arrow grows in step with the turn', and the bigger-hole-harsher-edge correction also says 'in step with'. 'Proportional to' appears nowhere else in the note's entry text.
- “The stretch is the extra pull on the one of two crumbs nearer that centre, for each metre of gap.”: Reread. 'The one of two crumbs nearer that centre' is a compressed relative clause, and on a first pass 'the one of two crumbs' reads as a noun phrase that has lost a word. The glossary says the same thing more plainly: 'one nearer a round body's centre than the other'.
- “Lay the strip on the paper at a slant, with one dot on a corner of a square. Turn the strip around that dot until the other dot lands on a corner.”: The explanation holds the pencil still and turns the paper, because the whole point is that the directions change while the thing measured does not. The try-it turns the strip instead, so the reader does the experiment the other way round from the story.
- Fix: No learner-visible text changed, so the revision stays at 5 and the status stays physics-reviewed. This was a re-run of the novice stage on a note whose novice review, two rereads and physics review (with a diff check) already all cover revision 5. Editing here would bump the note to revision 6, drop the status to novice-reviewed, and leave the validator warning that review.physics covers revision 5, blocking publication until a physics stage re-runs.
- Fix: The two stumbles that actually cost me comprehension, 'one part in the whole distance' and the missing non-corner-turn step, both need words added to the entry way explanations, which sit at 1,099 against a 1,000-word cap and the 1,100-word review ceiling. The guide forbids paying for them by compressing other entry sentences, so neither can be fixed inside this stage's allowance.
- Fix: The other four, 'parts' in two senses, 'ordinary size' against 'ordinary value' with 'size' also meaning a length, 'proportional to' against 'in step with', and 'the one of two crumbs nearer that centre', are word-for-word-neutral consistency breaches of rule 5 and of the reread rule. Each rewrite above is ready to paste. I judged that shipping them is a smaller harm than regressing a fully signed-off note, because none of them made me misread anything: I understood every sentence they appear in on the first pass.
- Fix: Recommended: an editor applies all six rewrites, plus the two items the earlier stages queued (tightening 'Up to sign and a factor $c^2$' to 'Exactly $c^2$ times' in 'Tidal readings fix the scalar', and adding the Kretschmann symbol row to the conventions file), in one pass, dropping one lower-value entry sentence to pay for the two entry-budget items. That is one revision bump and one physics diff check instead of several.

**Re-read** (2026-09-13, revision 6): 2 stumbles in 10 changed passages

- “So near the top edge, the map makes distances around the pole look larger and larger, without limit.”: Reread once. 'Look larger' gives no reference: larger than what? The comparison that carries the whole way is the real distance walked on the ground, and this sentence leaves the reader to supply it. The two sentences after it do supply it ('Nothing strange happens to the ice at the North Pole, though. The blow-up belongs to the map, not to the ground.'), so the hesitation cost me a second, not the argument. The new wording is still a clear gain on the old 'the map shows distances around the pole larger and larger', which read as a claim about the ground.
- “the map makes distances around the pole look larger and larger”: Rule 5, no synonyms. This is the only 'larger' in the whole entry surface; the note says 'bigger' for the same idea in sixteen places, including 'Doubling the stretch ... makes every square 4 times bigger', '64 times bigger' and 'How many times bigger is the turn?'. It did not make me misread anything, because 'makes it look larger' is the ordinary English for a picture that exaggerates, and the sentence is about how the map draws a distance rather than about a number growing.
- Fix: No learner-visible text changed, so the note stays at revision 6 with status physics-reviewed, and this re-read signs revision 6. Both stages now cover the current revision.
- Fix: Entry, the three 'ordinary size' -> 'has an ordinary value' swaps (summary, the 'A map can blow up' takeaway, the horizon-is-infinite correction): these are exactly the rewrite the last re-read queued, and they read clean. 'Value' is now the note's single word for what the scalar comes out to, matching 'gets an ordinary value, not an infinite one' in the same way and in the crushed-at-the-horizon answer, and 'size' is left meaning only a length, as in 'the cube of the horizon's size'. The spoken correction stays plain words with no math. 'This number has an ordinary value' is mildly circular, but 'this number' is the note's own back-reference to 'one number everyone agrees on: the Kretschmann scalar' and no other number is in play, so I left it rather than churn a signed sentence.
- Fix: Entry, 'A map can blow up': the map sentence still answers the way's one question with one picture, so no rule-17 stumble was introduced. Its first what-ifs still hold: walk right at the pole and the exaggeration is endless, which is what 'without limit' says, and north-south distances are drawn honestly on the even grid, which is why the sentence is scoped to distances around the pole.
- Fix: Working, 'Tidal readings fix the scalar': the two new sentences follow the geodesic deviation equation directly, and the minus sign is carried in words rather than left to the reader. 'Those accelerations' has one candidate, the relative accelerations per unit separation named in the sentence before. The second sentence carries three things at once (the weak-field form, what Phi is, and the gradiometer hedge) and runs to 37 words, which is fine at the working rung but is the densest sentence in the way. The units 's^-2' now attach to accelerations per unit separation rather than to 'gravity gradients', and the later paragraph's 'the radial gradient' still lands, because 'gravity gradiometer' is kept in the same paragraph.
- Fix: Working, the vacuum-tidal-form symbol gloss now matches the way word for word ('minus c^2 times them are the relative accelerations per unit separation'), so a reader meeting the equation on its own reads the same sign as the reader coming through the way.
- Fix: Working, 'Contract every index': 'A two-dimensional sphere of radius a' removes the dimension guess in a paragraph whose other examples are four-dimensional, and it reads naturally after 'A positive-definite geometry has no such sum'.
- Fix: Working, expanding-universe-scalars answer (c): 'In both cases K grows as t^-4' no longer reads as a claim about K and R together, which was the wrong reading available while 'both scalars' sat after parts that give both K and R. The clause 'although the radiation universe has R = 0 at every time' now clearly contrasts with it.
- Fix: Nothing was dropped or shortened for budget, because nothing was added: entry way explanations stay at 1,100 words, the hard ceiling, and the total stays at 8,329 of 9,500.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 6)

**Verification**

- Definition $\mathcal K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$, and the condition that it is unchanged by the Riemann sign convention and by $g \to -g$.: The contraction raises four indices, so a flip of the overall metric sign gives $(-1)^4$, and the Riemann tensor enters quadratically. Checked against the orthonormal expansion, where only the count of hatted-zero indices sets a sign. → Accurate. Both flips leave every term of the expansion unchanged.
- Orthonormal expansion $\mathcal K = 4\sum(R_{\hat 0\hat i\hat 0\hat j})^2 - 4\sum(R_{\hat 0\hat i\hat j\hat k})^2 + \sum(R_{\hat i\hat j\hat k\hat l})^2$.: Re-derived by grouping index quadruples by the number $N$ of hatted-zero indices with $\eta = \mathrm{diag}(-1,1,1,1)$: pair antisymmetry kills $N = 3, 4$; $N = 2$ has four orders per $(i,j)$; $N = 1$ has four slots for the zero. Then built the full Schwarzschild vacuum Riemann array in python3 from $\mathcal E = \mathrm{diag}(-2,1,1)q$, $S = -\mathcal E$ and evaluated both sides. → Accurate. Both sides give $48q^2$; the array satisfies pair symmetry, both antisymmetries and the first Bianchi identity exactly, and its Ricci tensor is exactly zero.
- Derivation 'In vacuum, space follows the tides': $\sum(R_{\hat i\hat j\hat k\hat l})^2 = 4\sum(R_{\hat 0\hat i\hat 0\hat j})^2$, with $\mathrm{tr}\,S = 0$ and $S = -\mathcal E$.: Re-derived each step: $R_{\hat i\hat j\hat k\hat l} = \epsilon_{ijm}\epsilon_{kln}S_{mn}$ in three dimensions; $\sum_i\epsilon_{ijm}\epsilon_{iln} = \delta_{jl}\delta_{mn} - \delta_{jn}\delta_{ml}$ gives $\delta_{jl}\mathrm{tr}S - S_{jl}$; vacuum $R_{\hat 0\hat 0} = \mathrm{tr}\,\mathcal E = 0$ then makes the trace of $R_{\hat j\hat l} = 0$ read $2\,\mathrm{tr}\,S = 0$; $\sum_{ij}\epsilon_{ijm}\epsilon_{ijp} = 2\delta_{mp}$ gives the factor 4. → Accurate. Checked on Schwarzschild: spatial squares sum to $24q^2 = 4 \times 6q^2$.
- Schwarzschild static orthonormal components $-2q, q, q$ (tidal) and $-q, -q, 2q$ (spatial) with $q = GM/(c^2r^3)$, and the visual sketch's preset $q(-2,1,1,-1,-1,2)$.: Reconstructed them from $S = -\mathcal E$ with $\mathcal E = \mathrm{diag}(-2,1,1)q$ in the order $(\hat r, \hat\theta, \hat\phi)$, so $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = S_{rr} = 2q$ and $R_{\hat r\hat\theta\hat r\hat\theta} = S_{\phi\phi} = -q$. Cross-checked the Ricci tensor numerically. → Accurate, and the six-entry-curvature-table preset is consistent: zero Ricci tensor and $\mathcal K = 48q^2$.
- $\mathcal K = 48G^2M^2/(c^4r^6)$ outside a spherical mass, equal to $12/r_s^4$ at $r_s = 2GM/c^2$, and $12r_s^2/r^6$ in the notation trap.: $8 \times 6q^2 = 48q^2$ with $q = GM/(c^2r^3)$; $G^2M^2/c^4 = r_s^2/4$ gives $12r_s^2/r^6$ and $12/r_s^4$ at $r = r_s$. Checked the trap's claimed factor of 4 both ways. → Accurate, including the factor of 4 from misreading $M$ as $r_s$ or $r_s$ as $GM/c^2$.
- The relation between the tidal components and what an observer measures: the note's own $\ddot\xi^{\hat i} = -c^2R_{\hat 0\hat i\hat 0\hat j}\xi^{\hat j}$ versus the key-equation gloss '$c^2$ times them are relative accelerations per unit separation'.: Took the Newtonian limit of the course geodesic-deviation equation with $u^0 \approx c$: $c^2R_{\hat 0\hat i\hat 0\hat j} = \partial_i\partial_j\Phi$ with a plus sign, so the relative acceleration per unit separation is $-c^2R_{\hat 0\hat i\hat 0\hat j}$. Checked against Schwarzschild: $\Phi = -GM/r$ gives $\partial_i\partial_j\Phi = \mathrm{diag}(-2,1,1)GM/r^3$, matching $c^2\mathcal E$, while two radially separated crumbs really do draw apart. → Error found. The gloss had the sign backwards: $R_{\hat 0\hat r\hat 0\hat r} = -2q$ while the radial relative acceleration per unit separation is $+2GM/r^3$. Fixed, and the way's vague 'Up to sign and a factor $c^2$' replaced with the exact statement.
- 'A radially falling observer's frame is a radial boost of the static one, and it reads the same tidal matrix.': Applied Lorentz boosts of rapidity 0.3, 0.9 and 1.5 along the radial direction to the full Schwarzschild Riemann array in python3. → Accurate. The tidal matrix stays $\mathrm{diag}(-2,1,1)q$ to machine precision and the one-time components stay zero at every rapidity.
- 'For a tangential boost of rapidity 0.9, a speed of $0.72c$, the squared tidal components sum to about 45 instead of 6, but $\mathcal K$ stays 48.': Boosted the same array tangentially in python3 and summed each group of squares. → Accurate. $\tanh 0.9 = 0.716$; $\sum(\mathcal E')^2 = 44.954$, $\sum(R_{\hat 0\hat i\hat j\hat k})^2 = 77.908$, spatial squares $179.815$, and $\mathcal K = 48.000$ from both the full expansion and $8\sum\mathcal E'^2 - 4\sum(\cdot)^2$.
- 'For an observer at rest in a static field, reversing time is a symmetry, so the components with one time index vanish.': Components with an odd number of time indices change sign under $t \to -t$, which is an isometry of a static (not merely stationary) spacetime. Checked against the numeric static Schwarzschild array. → Accurate, and correctly scoped to static fields, not to stationary ones such as Kerr.
- Worked example 'Earth against a black hole's horizon': every step and the final masses.: python3 with $GM = 3.986004418\times10^{14}$, $r = 6.371\times10^{6}$ m, $c = 2.99792458\times10^{8}$ m/s. → Accurate. $GM/r^3 = 1.5414\times10^{-6}$; $\mathcal K = 1.4118\times10^{-44}\ \mathrm{m^{-4}}$; $\mathcal K^{-1/4} = 9.17\times10^{10}$ m $= 0.613$ au; $r_s = 1.707\times10^{11}$ m; $M = 1.150\times10^{38}$ kg $= 5.78\times10^{7}$ solar masses, so 'about 58 million' holds.
- Entry claim: 'For a black hole about 58 million times as heavy as the Sun, the scalar at the horizon matches the scalar at the ground under your feet.': Same computation, run from the horizon side: $12/r_s^4 = \mathcal K_\oplus$. → Accurate to two significant figures.
- Check 'horizon-curvature-length': 103 million per second squared per metre, $\mathcal K = 1.58\times10^{-17}\ \mathrm{m^{-4}}$, 15.9 km, $r_s = 29.5$ km.: python3 for 10 solar masses: $r_s = 2GM/c^2$, radial gradient $2GM/r_s^3$, $\mathcal K = 12(2q)^2$ and $12/r_s^4$. → Accurate. $r_s = 29.53$ km; $2GM/r_s^3 = 1.0303\times10^{8}\ \mathrm{s^{-2}}$; $2q = 1.146\times10^{-9}\ \mathrm{m^{-2}}$; $\mathcal K = 1.576\times10^{-17}$ from both routes; $\mathcal K^{-1/4} = 15.87$ km, inside the numeric field's 2 per cent tolerance.
- Check 'ricci-zero-outside-a-star': $\mathcal K = 9.3\times10^{-60}\ \mathrm{m^{-4}}$ at 1 au from the Sun.: python3 with $GM_\odot = 1.32712440018\times10^{20}$ and $1\ \mathrm{au} = 1.495978707\times10^{11}$ m. → Accurate: $9.34\times10^{-60}\ \mathrm{m^{-4}}$.
- Check 'component-blows-up-at-horizon': $R_{r\theta r\theta} = g_{rr}r^2R_{\hat r\hat\theta\hat r\hat\theta} = -m/(r - 2m)$, with $\mathcal K = 3/(4m^4)$ at $r = 2m$.: Substituted $g_{rr} = (1 - 2m/r)^{-1}$ and the orthonormal value $-m/r^3$; evaluated $48m^2/r^6$ at $r = 2m$. → Accurate on both counts.
- Entry chain in 'Read it from the stretch' and check 'halve-the-distance': pull as $r^{-2}$, stretch as $r^{-3}$, scalar as $r^{-6}$; the quoted factors 4, 8 and 64, and one eighth and one sixty-fourth going outward.: Checked each factor against $2GM/r^3$ and $\mathcal K = 12(2GM/r^3)^2/c^4$, and checked the 'two such parts' step against $(1+\varepsilon)^{-2} \approx 1 - 2\varepsilon$ with the note's own $1.001 \times 1.001 \approx 1.002$. → Accurate, and the factor chain in the check's answer (4 times 2 gives 8) is the same statement.
- Entry claim: 'At Earth's surface, the pull on a crumb 2 metres nearer the centre is stronger by less than one millionth of its weight.': $2\Delta r/r = 2 \times 2/6.371\times10^{6}$. → Accurate: $6.3\times10^{-7}$, which is less than one millionth.
- Check 'bigger-black-hole': the circumference rule, and the ratios 1/100 and 1/10,000.: The stretch $2GM/r^3$ equals $2GM(2\pi)^3/C^3$ with $C$ the circumference, so at a horizon it scales as $M/M^3 = M^{-2}$ and $\mathcal K = 12(\text{stretch})^2/c^4$ as $M^{-4}$. → Accurate; matches both numeric fields and the bigger-hole-harsher-edge correction.
- Problem 'ball-half-as-wide': turn 4 times bigger, scalar 16 times bigger, and the statement that the turn is proportional to loop area over the ball's whole surface.: Small-loop holonomy on a sphere is $A/a^2$, and $A/(4\pi a^2)$ is the area fraction, so the two differ by the fixed factor $4\pi$. Halving $a$ multiplies $1/a^2$ by 4 and $\mathcal K = 4/a^4$ by 16. → Accurate.
- Problem 'expanding-universe-scalars' part (a): the stated components, $\mathcal K = 12[(\ddot a/a)^2 + (\dot a/a)^4]/c^4$ and $R = 6(\ddot a/a + \dot a^2/a^2)/c^2$.: Re-derived the flat FLRW components from $\Gamma^0{}_{ij} = a\dot a\delta_{ij}$, $\Gamma^i{}_{0j} = (\dot a/a)\delta^i{}_j$ with the course Riemann convention, giving $R_{\hat 0\hat i\hat 0\hat j} = -(\ddot a/a)\delta_{ij}$ and $R_{\hat i\hat j\hat k\hat l} = (\dot a/a)^2(\delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk})$. Counted 3 tidal terms (times 4) and 12 nonzero spatial quadruples. → Accurate, including the solution's Ricci steps $R_{\hat t\hat t} = -3\ddot a/(c^2a)$ and $R_{\hat i\hat i} = (\ddot a/a + 2\dot a^2/a^2)/c^2$.
- Problem 'expanding-universe-scalars' part (b) and its numeric fields 2.963, 1.5 and 0.: For $a \propto t^p$: dust $p = 2/3$ gives $\dot a/a = 2/3t$, $\ddot a/a = -2/9t^2$; radiation $p = 1/2$ gives $1/2t$, $-1/4t^2$. Evaluated both expressions. → Accurate. Dust $\mathcal K c^4t^4 = 12(4/81 + 16/81) = 80/27 = 2.963$, $Rc^2t^2 = 4/3$; radiation $12(1/16 + 1/16) = 3/2$ and $R = 0$ exactly.
- Cross-check of the formal identity $\mathcal K = C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + 2R_{\mu\nu}R^{\mu\nu} - \tfrac13R^2$.: Flat FLRW is conformally flat, so the identity must reduce to $\mathcal K = 2R_{\mu\nu}R^{\mu\nu} - R^2/3$. Computed $R_{\mu\nu}R^{\mu\nu}$ from the orthonormal Ricci components for dust and radiation. → Accurate, and it confirms the problem's answers independently: dust $2(16/9) - (16/9)/3 = 80/27$; radiation $2(3/4) - 0 = 3/2$.
- Problem 'plane-wave-invisible-to-invariants' part (a): the Christoffel symbols, $R_{uxux} = -A$, $R_{uyuy} = A$, and vacuum.: Computed $\Gamma_{\sigma\mu\nu}$ by hand from $H = A(u)(x^2 - y^2)$; inverted the metric to $g^{uu} = 0$, $g^{uv} = -1$, $g^{vv} = -H$; confirmed $\Gamma^u{}_{\mu\nu} = 0$ and evaluated $R^x{}_{uxu} = \partial_x\Gamma^x{}_{uu}$ in the course convention. → Accurate. $R_{uu} = -A + A = 0$, and $H$ is harmonic in $x, y$, so the metric is vacuum for every smooth $A(u)$.
- Problem part (b) and the formal way's argument that every complete contraction vanishes.: $g^{uu} = g^{ux} = g^{uy} = 0$, so a $u$ slot can pair only with a $v$ slot; the only nonzero components carry $u$ slots and no $v$ slot. → Valid as stated, and it covers $\mathcal K$, contractions with $\epsilon$ and, by boost weight, covariant derivatives of every order.
- Plane-wave tides: $d^2\xi^x/d\lambda^2 = Ak^2\xi^x$, $d^2\xi^y/d\lambda^2 = -Ak^2\xi^y$, and frame components $\mp\alpha k^2/u^2$ for $A = \alpha/u^2$.: Applied the course geodesic-deviation equation with $u^\mu = k\,\delta^\mu{}_u$; $\partial_v$ Killing keeps $du/d\lambda = k$ constant, so $u = k\lambda$ reaches zero at finite affine parameter. → Signs, branch and the finite affine parameter all check out.
- Kerr: $\mathcal K = 48M^2(r^2 - a^2\cos^2\theta)(r^4 - 14a^2r^2\cos^2\theta + a^4\cos^4\theta)/(r^2 + a^2\cos^2\theta)^6$, negative on the axis just outside the horizon whenever $a > M/2$.: Rewrote the second factor as $(r^2 + a^2\cos^2\theta)^2 - 16r^2a^2\cos^2\theta$; on the axis solved $r^4 - 14a^2r^2 + a^4 < 0$, that is $r/a < 2 + \sqrt3$, at $r_+ = M + \sqrt{M^2 - a^2}$. → Accurate, and the threshold is exact: at $a = M/2$ both sides equal $1.8660254\,M$, so the strict inequality $a > M/2$ is the right condition. The first factor $r_+^2 - a^2 = 2(Mr_+ - a^2)$ stays positive, so the sign comes from the second factor alone.
- Research horizon: $\nabla_\lambda R_{\mu\nu\rho\sigma}\nabla^\lambda R^{\mu\nu\rho\sigma} = 720M^2(r - 2M)/r^9$ in Schwarzschild with the course signature, vanishing on the horizon.: Computed it numerically in python3 straight from the Schwarzschild metric: fourth-order central differences for $\partial g$, $\partial\Gamma$ and $\partial R$, then the full covariant derivative and the contraction with $(-,+,+,+)$, at $M = 1$, $\theta = 60^\circ$ and $r = 1.5, 3, 5, 10$. → Confirmed. The ratio to $M^2(r-2M)/r^9$ came out 720.000, 719.9999, 719.9996 and 720.04, and the value is negative inside the horizon. The same run reproduced $\mathcal K = 48M^2/r^6$.
- Research horizon: $\mathcal K - 4R_{\mu\nu}R^{\mu\nu} + R^2$ integrates to $32\pi^2$ times the Euler characteristic in four dimensions.: Checked against the four-dimensional Gauss-Bonnet normalization $\chi = (1/32\pi^2)\int(\mathcal K - 4R_{\mu\nu}R^{\mu\nu} + R^2)\sqrt{g}\,d^4x$. → Accurate, as is the statement that the combination leaves the field equations unchanged in four dimensions.
- Observation 'tidal-disruption-flares': $r_t = r_s$ for a Sun-like star gives about $1\times10^{8}$ solar masses, with $\mathcal K$ at a horizon falling as $M^{-4}$ and the stretch as $M^{-2}$.: Solved $R_*(M/m_*)^{1/3} = 2GM/c^2$ in python3 with $R_* = 6.957\times10^{8}$ m and $m_* = 1$ solar mass; checked the scalings from $12/r_s^4$ and $2GM/r_s^3$. → Accurate: $1.14\times10^{8}$ solar masses, and the 'factors of order one' caveat covers spin and stellar structure.
- 'Near Earth the radial gradient $2GM/r^3 = 3.08\times10^{-6}\ \mathrm{s^{-2}}$ matches the measured decrease of gravity with height.': $2 \times 1.5414\times10^{-6}$, compared with the measured free-air gradient of about $3.086\times10^{-6}\ \mathrm{s^{-2}}$. → Accurate: $3.083\times10^{-6}\ \mathrm{s^{-2}}$.
- Related-concept claim: for static vacuum fields the squared tidal components add to one eighth of $\mathcal K$.: The vacuum form with no one-time components gives $\mathcal K = 8\sum(R_{\hat 0\hat i\hat 0\hat j})^2$. → Accurate; Schwarzschild gives $6q^2 = 48q^2/8$.
- Ambiguity in 'A sphere of radius $a$ has one independent component ... so $\mathcal K = 4/a^4$.': Counted the nonzero quadruples for a two-sphere (4 orders of one pair, $\mathcal K = 4/a^4$) and for a three-sphere (3 pairs in 4 orders, $\mathcal K = 12/a^4$). → The sentence sits in a four-dimensional discussion, so the dimension had to be named. Fixed to 'a two-dimensional sphere'.
- Entry analogy: 'near the top edge, the map shows distances around the pole larger and larger, without limit.': Checked the quantities the analogy relates. On an even latitude-longitude grid a full circle of latitude is drawn at the constant map width while its ground length $2\pi R\cos\phi$ shrinks to zero, so what grows without limit is the exaggeration, not any drawn length. → As written the sentence could be read as a claim about drawn lengths, which are bounded. Fixed to 'makes distances around the pole look larger and larger', which is the ratio that does blow up, and is the right parallel to the metric coefficient.
- References re-verified directly this pass: Gezari 2021; Ellis and Schmidt 1977; Pravda, Pravdova, Coley and Milson 2002; Karlhede, Lindstrom and Aman 1982; Goroff and Sagnotti 1986.: WebSearch against publisher and abstract-service records for authors, year, title, venue, page range, DOI and arXiv id. → All five confirmed exactly as recorded, including page ranges 21-58, 915-953, 6213-6236, 569-571 and 709-736. They stay verified: true.
- The remaining six references (Lemaitre 1933, Kruskal 1960, Karlhede 1980, Abdelqader and Lake 2015, 't Hooft and Veltman 1974, Stelle 1977).: Checked their internal consistency (venue, volume, first page, DOI pattern) against the records seen while verifying the others; each was confirmed in the earlier physics pass. → No discrepancy found; left verified: true.
- History scope: Kretschmann 1917, with work left null.: WebSearch for the paper. It appears as 'Uber den physikalischen Sinn der Relativitatspostulate...', Annalen der Physik 53, 575-614, cited as 1917 in the literature while the publisher's record dates that issue to 1918. → The contribution as worded is accurate and, correctly, does not say he introduced the scalar that carries his name. Left work null because of the year discrepancy; recorded as a concern.
- Structure: prerequisites direct and acyclic, assumes consistent, formal rung complete, visuals declared.: Read the registry entries for riemann-curvature-tensor and scalar-invariant; checked each way's assumes against the prerequisite rungs; counted formal checks and problems; ran visual_ids.py. → No cycle; assumes are legal at each way's rung; two formal checks and one formal problem, as the core tier needs. All four visuals are proposals with sketches, and the prerequisite scalar-invariant still has no note.

**Counterexamples tried**

- Cone tip: curvature vanishes off the tip, so every invariant is bounded while geodesics still end. Tried against the formal theorem, which the note states in one direction only, and against the check finite-is-not-regular, which names conical defects. Consistent.
- Bent but flat surface (a rolled paper tube): the arrow test returns every arrow unturned, so the entry table is all zeros and the entry recipe gives zero. Tried against 'square every entry and add them all up'. No entry sentence claims a visibly bent surface must give a nonzero total.
- A region bigger than half a closed surface, and a figure-eight loop: tried against the entry problem's 'the turn is proportional to the loop's area divided by the ball's whole surface area'. The problem says 'tiny loop' and uses a single tilt, so neither case is in scope.
- Non-relativistic limit: $c^2R_{\hat 0\hat i\hat 0\hat j} \to \partial_i\partial_j\Phi$. Tried against the entry stretch chain. Exact for the static Schwarzschild frame, where $c^2\mathcal E = \mathrm{diag}(-2,1,1)GM/r^3$, so the entry scalings are the Newtonian ones with no hidden relativistic factor.
- Massless, null case: an exact vacuum plane wave is curved with real tides and every scalar invariant zero. Tried against every sentence that could read as 'a bounded or zero scalar means nothing is there'. The note makes this its formal contrast way, and no entry or working sentence claims the converse.
- Non-static case (flat FLRW): tried against 'in vacuum the scalar is eight times the summed squared tides' and against 'for static observers only the tides remain'. FLRW is not vacuum, so the vacuum form is out of scope and the problem uses the general expansion; comoving observers are not static, yet isotropy still kills the one-time components, which the solution says explicitly.
- Strong field (Kerr): $\mathcal K$ is negative on the axis just outside the horizon for $a > M/2$. Tried against any reading of $\mathcal K$ as a sum of squares. The formal way states the indefiniteness, and every entry and working claim about a round body is scoped to bodies that do not spin.
- A different observer: a tangentially boosted observer near a spherical mass reads $\sum\mathcal E^2 = 45$ and nonzero one-time components instead of 6 and none. Tried against 'the crew's stretch reading fixes the scalar'. The entry way and its simplifies both scope this to a crew falling directly toward the centre, and say a sideways crew reads a different stretch and the same scalar.
- Inside matter: a radiation universe has $R = 0$ with $\mathcal K \neq 0$, and a dust universe has both nonzero. Tried against 'outside a star the Ricci scalar is zero, so it cannot tell one radius from another'. The claim is about vacuum, and the note offers the radiation universe as the second example of $R = 0$ without flatness.
- A different chart at the same place: ingoing Eddington-Finkelstein against Schwarzschild coordinates at $r = 2M$. $\mathcal K = 3/(4M^4)$ in both, while $R_{r\theta r\theta}$ diverges only in the second. Confirms 'a component inherits a failing basis; a scalar has none'.
- Signature and dimension: a two-sphere gives $\mathcal K = 4/a^4$, a three-sphere $12/a^4$, and a positive-definite metric makes $\mathcal K$ a plain sum of squares. Tried against the sphere sentence in 'Contract every index', which needed its dimension named; now fixed.
- Nonzero cosmological constant: $R_{\mu\nu} = \Lambda g_{\mu\nu}$ gives $\mathcal K = C^2 + 8\Lambda^2/3$, so the vacuum tidal form fails. Every statement that uses it carries 'vacuum with no cosmological constant' in its conditions or simplifies. Consistent.
- Reversing a loop: walking the other way round flips the sign of every table entry, because the tensor is antisymmetric in the pair that names the loop. Tried against the entry sentence that the recipe 'counts both ways round'. Squares are unchanged and both orders appear in the sum, so the sentence holds.

**Fixes**

- key_equations/vacuum-tidal-form, symbol $R_{\hat 0\hat i\hat 0\hat j}$: '$c^2$ times them are relative accelerations per unit separation' had the sign backwards against the note's own geodesic-deviation equation and against radially separating crumbs. Now 'minus $c^2$ times them are the relative accelerations per unit separation'.
- ways_in/tidal-readings-fix-it: 'Up to sign and a factor $c^2$, the symmetric matrix of tidal components ... is the matrix of gravity gradients a gravity gradiometer reads' was too vague to check. Replaced with the exact chain: minus $c^2$ times the tidal matrix is the matrix of relative accelerations per unit separation, and in a weak field those accelerations are $-\partial_i\partial_j\Phi$, which is what a gradiometer reads up to the instrument's sign convention. Working explanations rise from 557 to 584 words, well inside the 1,000 cap.
- ways_in/contract-every-index: 'A sphere of radius $a$' became 'A two-dimensional sphere of radius $a$', because the sentence sits in a four-dimensional discussion and a three-sphere gives $12/a^4$, not $4/a^4$.
- ways_in/a-map-can-blow-up: 'the map shows distances around the pole larger and larger, without limit' became 'the map makes distances around the pole look larger and larger, without limit'. On an even grid the drawn length of a circle of latitude is the constant map width; what grows without limit is the exaggeration, which is the quantity that parallels the diverging metric coefficient. This cost one word, the whole remaining entry headroom, taking entry way explanations from 1,099 to 1,100 words, exactly the review ceiling. Nothing was dropped.
- problems/expanding-universe-scalars, answer (c): 'Both scalars $\mathcal K$ grow as $t^{-4}$' became 'In both cases $\mathcal K$ grows as $t^{-4}$'. After parts (a) and (b), which give both $\mathcal K$ and $R$, 'both scalars' reads as $\mathcal K$ and $R$, and $R$ does not grow as $t^{-4}$: it is $4/(3c^2t^2)$ for dust and exactly zero for radiation.
- 'an ordinary size at the horizon' became 'has an ordinary value at the horizon' in the summary, in the takeaway of 'A map can blow up' and in the horizon-is-infinite correction. $\mathcal K$ has units of inverse length to the fourth power, and 'size' names a length elsewhere in the note ('the cube of the horizon's size'), so 'size' invited reading the scalar as a length. Word-for-word neutral, and it matches 'an ordinary value' already used in the explanation and in the crushed-at-the-horizon answer.
- Nothing was dropped or shortened to pay for these fixes; the only budgeted part that moved to its ceiling is the entry rung, at exactly 1,100 words.

**Concerns**

- EDITOR DECISION NEEDED, the note's one unresolved convention gap: knowledge/notation/course-conventions.md still fixes no symbol for the Kretschmann scalar. Its Practices section only flags the collision ('$K$ for Gaussian curvature versus the Kretschmann scalar') without deciding, so notation_traps/symbol-for-the-scalar states a course choice the conventions file does not make. Reported rather than invented, as that file requires. Recommend adding a row adopting $\mathcal K$, which this note, its renders and its sibling notes already use.
- EDITOR DECISION NEEDED, carried from both earlier stages and now worse: entry way explanations sit at exactly 1,100 words, the review ceiling for the 1,000-word core cap, with zero headroom. The novice reviewer's two real comprehension fixes (the 'one part in the whole distance' step, +5 words, and the untestable 'no turn of the paper can change the sum' what-if, +27 words) still cannot be made. An editor should drop or shorten an entry sentence before the next pass, rather than leave a reviewer working under a zero-word ceiling. Other parts have room: extras 769/800, support 1,852/2,300, tutoring 2,875/3,300, total 8,329/9,500.
- Four word-sense items the novice reviewer listed remain unapplied, deliberately: they are novice-lens wording with no accuracy content, and each would add to the next re-read. They are 'Its parts along your chosen directions' against 'part' as a fraction; 'is proportional to' in the ball-half-as-wide statement against 'grows in step with' in its own hint and solution; and 'the one of two crumbs nearer that centre' in the recap of 'A map can blow up'. The fourth, 'ordinary size', I did apply, because it also confuses a magnitude with a length.
- The prerequisite scalar-invariant (needed_for working) still has no note anywhere under knowledge/concepts/, so this note's working rung cannot be aligned with its glossary.
- All four linked visuals are proposals with sketches, not catalog entries, and visual_ids.py returns no catalog entry to reuse for any of them.
- History: Kretschmann's 1917 paper is dated 1918 by the publisher's own record for that issue of Annalen der Physik, while the literature cites it as 1917. The note keeps year 1917 and work null, which avoids asserting either.
- Sign convention outside the course: the research-horizon value $720M^2(r - 2M)/r^9$, now confirmed numerically, is positive outside the horizon only with the course signature $(-,+,+,+)$; a reader checking $(+,-,-,-)$ literature will meet the opposite sign. A notation trap could record this if the research rung grows.
- The next stage is a novice re-read of exactly the eight changed strings: four at entry (the summary, the map sentence and takeaway in 'A map can blow up', and the horizon-is-infinite correction) and four at working (the vacuum-tidal-form symbol gloss, the gradiometer sentence in 'Tidal readings fix the scalar', the two-dimensional sphere sentence, and answer (c) of the expanding-universe problem).

**Diff check** (2026-09-13, revision 5)

- Recap, 'A map can blow up': a crew falling directly toward the centre of a round body can work the scalar out from its stretch reading.: Tried the standard counterexamples against the widened scope: a spinning black hole (Kerr), where the scalar also depends on the twisting (gravitomagnetic) part of the curvature, and a crew inside matter, where the Ricci part adds to the scalar. Checked against the note's own scope wording in 'Read it from the stretch'. → Too broad. The old sentence took its black-hole scope from context, but 'a round body' extends it to spinning bodies and to places inside matter. Fixed by limiting it to outside a round body that does not spin, the note's wording elsewhere.
- Recap: the stretch is the extra pull on the one of two crumbs nearer that centre, for each metre of gap.: Compared with the old wording and the glossary's plain definition of stretch (relative tidal acceleration per unit separation along the radial line). → Same claim as before and as the glossary. Accurate.
- Explanation and crushed-at-the-horizon answer: a crew falling directly toward the black hole's centre gets an ordinary scalar value at the horizon.: Only 'the centre' became 'the black hole's centre'. Schwarzschild K = 48 M^2/r^6 (G=c=1) gives 3/(4M^4) at r = 2M. This is finite, and the radial tidal eigenvalue 2M/r^3 is boost-invariant for radial infall, so K = 12 (2M/r^3)^2 holds for the falling crew. → Accurate. The antecedent is clearer and the claim is unchanged.
- Misconception correction: the stretch at a horizon is in step with mass over the cube of the horizon size, which grows with the mass, so ten times the mass gives one hundredth of the stretch and a scalar ten thousand times smaller.: The radial stretch is 2M/r^3 with r_h = 2M, so it is 1/(4M^2) and scales as M^-2. K = 12 (stretch)^2 scales as M^-4. Computed in python3: M=1 gives stretch 0.25 and K 0.75; M=10 gives stretch 0.0025 and K 7.5e-5, ratios 0.01 and 1e-4. Compared with the bigger-black-hole check's numeric fields (0.01 and 0.0001, rel_tol 0.02). → Accurate and consistent with the check.
- Fix: Recap, 'A map can blow up': 'A crew falling directly toward the centre of a round body can work the scalar out from its stretch reading.' became 'Outside a round body that does not spin, a crew falling directly toward its centre can work the scalar out from its stretch reading.' This narrows the claim to where a single stretch reading fixes the scalar.
