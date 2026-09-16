---
type: "concept"
schema_version: 2
id: "symmetries-of-the-riemann-tensor"
title: "Symmetries of the Riemann tensor"
tagline: "Three rules that make most entries of the curvature table zeros or repeats"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 4
updated: "2026-09-13"
aliases: ["algebraic symmetries of the Riemann tensor", "index symmetries of the Riemann tensor"]
prerequisites: ["riemann-curvature-tensor", "riemann-tensor-in-normal-coordinates", "symmetric-and-antisymmetric-tensors", "raising-and-lowering-indices", "covariance-of-tensor-equations"]
leads_to: ["cyclic-identity", "number-of-independent-riemann-components", "ricci-tensor", "bianchi-identity", "weyl-tensor", "sectional-curvature"]
visuals: ["tips-of-a-turning-cross", "falling-ring-of-crumbs", "twenty-of-256-slots"]
---

# Symmetries of the Riemann tensor

*Three rules that make most entries of the curvature table zeros or repeats*

`symmetries-of-the-riemann-tensor` · curvature · core · physics-reviewed (revision 4)

**Needs:** [[riemann-curvature-tensor]] (entry) · [[riemann-tensor-in-normal-coordinates]] (entry) · [[symmetric-and-antisymmetric-tensors]] (working) · [[raising-and-lowering-indices]] (working) · [[covariance-of-tensor-equations]] (working)  
**Opens:** [[cyclic-identity]] · [[number-of-independent-riemann-components]] · [[ricci-tensor]] · [[bianchi-identity]] · [[weyl-tensor]] · [[sectional-curvature]]  
**Related:** [[riemann-curvature-operator]] · [[ricci-identity]] · [[bivector]] · [[torsion-tensor]]  
**Visuals:** ★ [[tips-of-a-turning-cross]] · [[falling-ring-of-crumbs]] · [[twenty-of-256-slots]]

> Carry arrows around tiny loops without letting them swing, and the curvature table records how they come back changed. Three rules tie its entries together. Walking a loop the other way flips the change. Of two equal arrows at right angles, one leans toward the other as far as the other leans away. And swapping a loop's tilt with the arrow's tilt leaves an entry unchanged. So a surface needs one number at each spot, and space needs six.

## You will be able to

**Entry**
- Explain why, of two equal arrows at right angles carried around a tiny loop, one leans toward the other as far as the other leans away. `objectives/explain-the-lean-rule` ← `checks/lean-of-the-second-arrow`
- Explain why tidal drift near a planet whose gravity does not change with time forms no whirlpool, and what that forces on two sideways drifts. `objectives/explain-fair-tides` ← `checks/four-crumbs-and-a-whirlpool`
- Use the three rules to count the different numbers the curvature table needs on a surface, in space, and in space and time. `objectives/count-with-the-rules` ← `checks/count-on-a-surface-and-in-space`, `problems/count-in-space-and-time`

**Working**
- Derive the pair antisymmetries and pair exchange from the metric, and explain why they hold in every basis. `objectives/derive-the-rules` ← `checks/proved-where-connection-vanishes`
- Use the rules to find vanishing and partner components, keeping track of which indices are lowered. `objectives/generate-partner-components` ← `checks/mixed-index-partner`, `problems/whole-two-dimensional-table`
- Compute a gradiometer's angular acceleration from the antisymmetric part of its readings. `objectives/separate-spin-from-gravity` ← `checks/gradiometer-spin`

**Formal**
- State which property of a connection each symmetry needs, and decide which survive without a metric or with torsion. `objectives/state-the-assumption-ladder` ← `checks/connection-without-a-metric`, `checks/ricci-with-torsion`
- Prove pair exchange from the two antisymmetries and the cyclic identity, and show that the converse fails. `objectives/prove-pair-exchange` ← `problems/pair-exchange-from-the-others`

## Ways in

### 1. Two arrows at right angles · entry · picture

*When a loop changes two arrows that sit at right angles, how must their changes compare?*

**Recap:** The arrow test: carry an arrow around a tiny loop, a path that ends where it began, and never let it swing. On the ground that means never turning it left or right. In space it means never turning it any way at all. A loop's tilt is set by the two directions its sides run along, like the bottom, front or side of a box. For each tilt of a tiny loop and each starting direction of the arrow, the curvature table lists how the arrow comes back changed, divided by the loop's area. This table is called the Riemann curvature tensor.

Cut two cardboard arrows, each 10 centimetres long, and tape their tails together at a right angle. Stand at a spot on a huge, smooth ball. Lay the pair on the ground, with one arrow pointing ahead of you and the other to your left. Call them the ahead arrow and the left arrow.

Carry the pair around a loop, never letting either arrow swing. Cardboard does not stretch, and the tape keeps the right angle between the arrows. So if the pair comes back turned, it comes back turned as one piece.

Back at the start, face the way you faced when you set off. Say the ahead arrow's tip has moved 2 millimetres toward your left, toward the left arrow. Then the left arrow's tip has moved 2 millimetres backward, away from the ahead arrow.

The distance a tip has moved toward the other arrow is called its lean. A tip that has moved away from the other arrow leans away.

Why the same 2 millimetres? If the left arrow leaned away less than the ahead arrow leaned toward it, the angle between the arrows would shrink. If it leaned away more, the angle would grow. The tape keeps a right angle, so on the ground one arrow leans toward the other exactly as far as the other leans away. This is called the lean rule.

In space, a tiny loop can turn the pair about any line at all. Then the two leans can differ, but only by far less than the tips move. For the tiny loops the curvature table records, that difference is too small to count, so the lean rule holds there too.

**Try it:** Tape two equal pencils into a plus sign, crossing at their middles at a right angle, with their sharpened tips next to each other. Push a drawing pin through the crossing into a piece of cardboard, so the cross can turn. Mark on the cardboard where the two tips sit. Turn the cross until the first tip is 2 millimetres from its mark, toward the second pencil. You should see the second tip about 2 millimetres from its mark, away from the first pencil.

**Takeaway:** Carried around a tiny loop, two equal arrows at right angles turn as one piece, so one leans toward the other as far as the other leans away.

*What this leaves out:* In spacetime, where time is one of the four directions, the change need not be a turn. The lean rule then holds only if a lean along time is counted with the opposite sign, which this way does not explain.

*Builds on:* [[riemann-curvature-tensor]]<br>*Visuals:* [[tips-of-a-turning-cross]]<br>*See:* `checks/lean-of-the-second-arrow`

### 2. Tides without a whirlpool · entry · operational

*Can tidal drift in a freely falling room ever carry a ring of crumbs around in a whirlpool?*

**Recap:** In a room falling freely near a planet, loose crumbs float beside you, because everything falls together. Crumbs away from the room's centre slowly drift: apart along the line toward the planet's centre, and together across it. This is tidal drift. The curvature table, the Riemann curvature tensor, lists how arrows carried around tiny loops come back changed. With time counted as a fourth direction, it also records tidal drift.

A room falls freely toward a round planet. The planet's gravity at each place stays the same from moment to moment, and the room does not spin. Pick any two directions in the room at right angles, and call them A and B. Let go of four crumbs, each at rest in the room and 1 metre from its centre. One sits out along A, one out along B, and one on the far side of the centre from each of those.

Gravity at a crumb differs slightly, in strength and in direction, from gravity at the room's centre. That small difference is an extra pull, and it makes the crumb drift in the room. A crumb on the far side of the centre gets the opposite extra pull, so it drifts the opposite way.

Go around the ring of crumbs, starting from the crumb out along A toward the crumb out along B. Call the way you travel forward. At the crumb out along A, forward points toward B, so its drift toward B is a forward drift. At the crumb out along B, forward points away from A, so its drift toward A is a backward drift. At each far-side crumb, the drift and forward both point the opposite way, so it adds the same forward or backward drift again. If the forward drifts added up to more than the backward drifts, the ring would start to circle as a whole, like a whirlpool.

Can that happen? A roller-coaster car with no friction comes back to where it started with its starting speed, whatever the track's shape. In the same way, near a planet whose gravity stays the same from moment to moment, gravity gives back all the energy it takes on every route that ends where it began.

An extra pull is gravity at the crumb minus gravity at the room's centre. Gravity at the room's centre is one pull, the same all around the ring. A pull that is the same everywhere also gives back all it takes, because a loop goes as far against it as along it. So the extra pulls give back all they take too.

A whirlpool would push a crumb, carried once around the ring before the room falls far, forward more than backward. The crumb would gain energy from nothing. So there is no whirlpool: the crumb out along A drifts toward B just as far as the crumb out along B drifts toward A.

Near Earth, a crumb 1 metre out drifts less than 2 tenths of a millimetre in 10 seconds, too little to notice.

**Takeaway:** Near a planet whose gravity does not change with time, tidal drift forms no whirlpool, so of two crumbs out along directions at right angles, each drifts toward the other's direction equally.

*What this leaves out:* The drifts balance even where gravity changes with time, as around two circling stars; there the reason comes from how the curvature table is built, not from energy.

*Continues:* `ways_in/two-arrows-at-right-angles`<br>*Builds on:* [[riemann-tensor-in-normal-coordinates]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/four-crumbs-and-a-whirlpool`

### 3. Counting what the table holds · entry · calculation

*How many different numbers does the curvature table really need at one spot?*

**Recap:** Walking a tiny loop the other way gives the opposite change. A loop's tilt is set by the two directions its sides run along, like the bottom, front or side of a box. The lean rule: of two equal arrows at right angles carried around a tiny loop, one leans toward the other as far as the other leans away. Near a planet whose gravity does not change with time, tidal drift forms no whirlpool. Falling crumbs out along directions at right angles drift toward each other's directions equally.

In space you can pick three directions at right angles: ahead, left and up. Filling one entry of the curvature table takes four choices of direction. The first two give the loop's sides, in the order you walk them. The third gives the arrow's starting direction, and the fourth gives the direction its lean is read in. Each choice can be any of the three directions, so 3 times 3 times 3 times 3 gives 81 entries.

Start with the loop. If its first two sides run along the same direction, you walk out and back along one line. That loop encloses nothing, so its entries are zero. Walking two different directions in the other order goes around the same loop the other way, so it gives the opposite change. So only the loop's tilt matters, and space has three tilts: ahead with left, ahead with up, and left with up.

The arrow works the same way. Its starting direction and the direction its lean is read in make a tilt too. This is called the arrow's tilt. A lean read along the arrow's own direction is far too small to count for a tiny loop, because the tip moves along a circle around the tail. So it counts as zero. By the lean rule, swapping the two directions flips the sign. So only the arrow's tilt matters, which leaves 3 times 3, or 9, numbers.

The equal drifts of falling crumbs make two entries of the table equal. We take on trust that the loop's tilt of each entry is the arrow's tilt of the other. Every entry obeys a rule of this kind, also taken on trust here. It is called the mirror rule: swapping a loop's tilt with the arrow's tilt leaves the entry unchanged.

In 3 of the 9 numbers, the two tilts match. The other 6 form pairs with the tilts swapped, and the mirror rule makes each pair equal, which gives 3 more. So 3 plus 3, or 6, numbers describe the curving at a spot in space.

A surface has only two directions, ahead and left, so loops and arrows each have one tilt, and one number remains.

**Takeaway:** The rules shrink the curvature table from 81 entries to 6 different numbers in space and to one number on a surface, which is why one number describes a ball's curving.

*What this leaves out:* In space and time, with four directions and six tilts, the three rules leave 21 numbers; one more rule, for entries whose four directions all differ, leaves 20.

*Continues:* `ways_in/two-arrows-at-right-angles`, `ways_in/tides-without-a-whirlpool`<br>*Visuals:* [[twenty-of-256-slots]]<br>*See:* `checks/count-on-a-surface-and-in-space`, `problems/count-in-space-and-time`

### 4. The rules in components · working · calculation

*What do the three rules say about components, and why do they hold in every basis?*

The count in "Counting what the table holds" used three rules about the table. In components they concern the Riemann tensor with its first index lowered by the metric, $R_{\rho\sigma\mu\nu} \equiv g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$, and read

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}.$$

The last pair $\mu\nu$ takes the loop's edges, so swapping it walks the loop backwards. The first pair holds the output slot $\rho$ and the carried vector's slot $\sigma$. So the first pair is the arrow's tilt of the count, and the last pair is the loop's tilt. Lowered, a small loop changes a vector by $\Delta V_\rho = -R_{\rho\sigma\mu\nu}V^\sigma a^\mu b^\nu$, and antisymmetry in $\rho\sigma$ makes this change an infinitesimal rotation or boost: the lean rule. Pair exchange is the mirror rule.

The derivation "Reading the rules off the metric" proves all three at a point $P$ where $\partial_\lambda g_{\mu\nu}(P) = 0$. There the lowered tensor is half a signed sum of four second derivatives of $g$. Each swap either reverses every term or permutes the terms, because $g$ is symmetric and partial derivatives commute. A difference such as $R_{\rho\sigma\mu\nu} + R_{\sigma\rho\mu\nu}$ is a tensor, and a tensor whose components vanish in one basis vanishes in every basis, so the rules hold in all coordinates. First-pair antisymmetry also follows in any coordinates from $\nabla g = 0$, as the derivation "Metric compatibility forces first-pair antisymmetry" shows.

Consequences:

- A repeated index inside a pair gives zero: $R_{00\mu\nu} = R_{\rho\sigma 33} = 0$.
- Moving a single index across the pairs is not a symmetry: $R_{0011} = 0$, while $R_{0101}$ need not vanish.
- In two dimensions every component is $0$ or $\pm R_{1212}$, and $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ with $K = R_{1212}/\det g$ the Gaussian curvature, as the problem "The whole two-dimensional table" proves.
- The Ricci tensor $R_{\mu\nu} = R^\lambda{}_{\mu\lambda\nu}$ is symmetric, by pair exchange.

The rules need both first-pair indices at the same level. On a sphere of radius $a$, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, but its first-pair partner with $\phi$ raised is not $-\sin^2\theta$, because lowering $\theta$ and raising $\phi$ bring different metric factors.

**Takeaway:** With its first index lowered, the Riemann tensor flips sign within either index pair and is unchanged when the pairs trade places, in every basis.

*What this leaves out:* Levi-Civita connection only; "Which rule needs which assumption" separates what each rule needs.

*Continues:* `ways_in/counting-what-the-table-holds`<br>*Builds on:* [[riemann-tensor-in-normal-coordinates]], [[raising-and-lowering-indices]], [[symmetric-and-antisymmetric-tensors]], [[covariance-of-tensor-equations]]<br>*See:* `derivations/rules-from-the-four-term-formula`, `derivations/metric-compatibility-forces-first-pair-antisymmetry`, `worked_examples/sphere-table-from-one-component`, `checks/mixed-index-partner`

### 5. A gradiometer splits spin from gravity · working · operational

*How does a gravity gradiometer use pair exchange to tell its own rotation from gravity?*

The crumbs in "Tides without a whirlpool" drifted toward each other's directions equally, with no whirlpool. In a freely falling, non-rotating frame with orthonormal axes, neighbouring free-fall worldlines obey the geodesic deviation equation, taken on trust here:

$$\ddot\xi^{\hat i} = -E_{ij}\,\xi^{\hat j},\qquad E_{ij} \equiv c^2R_{\hat i\hat 0\hat j\hat 0}.$$

The two antisymmetries give $R_{\hat i\hat 0\hat j\hat 0} = R_{\hat 0\hat i\hat 0\hat j}$, and pair exchange swaps $\hat i$ with $\hat j$, so the tidal matrix is symmetric, $E_{ij} = E_{ji}$. In a weak static field $E_{ij} = \partial_i\partial_j\Phi$, symmetric because partial derivatives commute: the energy argument of "Tides without a whirlpool" in calculus form.

A gradiometer holds proof masses at fixed places in a spacecraft and measures the force per unit mass needed to hold each one. If the spacecraft turns with angular velocity $\boldsymbol\Omega$ relative to the non-rotating frame, a mass held at $\boldsymbol\xi$ needs $f_i = M_{ij}\xi^j$, with

$$M = E + \boldsymbol\Omega\boldsymbol\Omega^{\mathsf T} - \Omega^2\,\mathbb 1 + [\dot{\boldsymbol\Omega}\times],$$

the standard rotating-frame result, taken on trust here, where $[\dot{\boldsymbol\Omega}\times]\boldsymbol\xi = \dot{\boldsymbol\Omega}\times\boldsymbol\xi$. The first three terms are symmetric and the last is antisymmetric. So the antisymmetric part of $M$ is the angular acceleration alone, with $M_{xy} - M_{yx} = -2\dot\Omega_z$ and its cyclic partners. The symmetric part is gravity plus the centrifugal term.

The split matters. Take a satellite 255 km up, $r = 6626$ km, where $GM/r^3 = 1.37\times10^{-6}\ \mathrm{s^{-2}}$. With $x$ along the track, $y$ across it and $z$ radial, $E = (GM/r^3)\,\mathrm{diag}(1, 1, -2)$. Keeping one face toward Earth, the satellite turns once per orbit, every 89.5 min, about $y$, with $\Omega^2 = GM/r^3$. The centrifugal term is as large as the gravity gradients, and the diagonal of $M$ becomes $(0, 1, -3)\,GM/r^3$.

**Takeaway:** Pair exchange makes the tidal matrix symmetric, so a gradiometer reads its angular acceleration from the antisymmetric part of its readings.

*What this leaves out:* Treats the satellite's centre as falling freely and Earth as a Newtonian sphere.

*Continues:* `ways_in/tides-without-a-whirlpool`, `ways_in/rules-from-the-metric`<br>*Builds on:* [[tidal-force]], [[newtonian-tidal-tensor]]<br>*See:* `observations/goce-gravity-gradients`, `checks/gradiometer-spin`

### 6. Which rule needs which assumption · formal · structure

*Which property of a connection does each symmetry require, and what structure do the symmetries give curvature at a point?*

The rules in "The rules in components" were read off the Levi-Civita connection all at once. Separating them shows what each needs. Let $\nabla$ be a connection on the tangent bundle of an $n$-manifold $M$, with curvature $\mathcal R(X,Y)Z = \nabla_X\nabla_YZ - \nabla_Y\nabla_XZ - \nabla_{[X,Y]}Z$ and components $R^\lambda{}_{\sigma\mu\nu} = dx^\lambda\big(\mathcal R(\partial_\mu,\partial_\nu)\partial_\sigma\big)$. Given a metric $g$, set $\mathrm{Rm}(W,Z,X,Y) = g\big(W, \mathcal R(X,Y)Z\big)$, with components $R_{\rho\sigma\mu\nu}$.

Proposition.

- (a) For every connection, $\mathcal R(X,Y) = -\mathcal R(Y,X)$.
- (b) If the torsion vanishes, $\mathcal R(X,Y)Z + \mathcal R(Y,Z)X + \mathcal R(Z,X)Y = 0$; in components this is the cyclic identity $R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0$.
- (c) If $\nabla g = 0$, with or without torsion, $\mathrm{Rm}(W,Z,X,Y) = -\mathrm{Rm}(Z,W,X,Y)$: each $\mathcal R(X,Y)$ is skew-adjoint, an element of $\mathfrak{so}(g_p)$.
- (d) Together, (a), (b) and (c) imply pair exchange, $\mathrm{Rm}(W,Z,X,Y) = \mathrm{Rm}(X,Y,W,Z)$.

Proof sketch. (a) is built into the definition. For (b), a torsion-free connection admits coordinates with $\Gamma(p) = 0$; there $R^\lambda{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\lambda{}_{\nu\sigma} - \partial_\nu\Gamma^\lambda{}_{\mu\sigma}$, and the cyclic sum cancels because $\Gamma^\lambda{}_{\nu\sigma} = \Gamma^\lambda{}_{\sigma\nu}$. For (c), the operator $\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]}$ annihilates every function, in particular $g(Z,W)$, and expanding with $\nabla g = 0$ leaves $g(\mathcal R(X,Y)Z, W) + g(Z, \mathcal R(X,Y)W) = 0$. For (d), let $S_{\rho\sigma\mu\nu}$ be the cyclic sum in (b). Using only (a) and (c), $S_{\rho\sigma\mu\nu} - S_{\sigma\mu\nu\rho} - S_{\mu\nu\rho\sigma} + S_{\nu\rho\sigma\mu} = 2(R_{\rho\sigma\mu\nu} - R_{\mu\nu\rho\sigma})$. The converse of (d) fails: in four dimensions $\epsilon_{\rho\sigma\mu\nu}$ obeys (a), (c) and pair exchange but not (b).

Structure. For the Levi-Civita connection, $\mathrm{Rm}_p$ is a symmetric bilinear form on bivectors, $\Lambda^2T_pM$, of dimension $n(n-1)/2$, obeying (b). In four dimensions that form has 21 entries, and (b) adds one independent condition, leaving the 20 counted in the note on the number of independent components. Equivalently, the curvature operator on $\Lambda^2T_pM$ is self-adjoint for the induced metric. In Riemannian signature it has real eigenvalues and an orthonormal eigenbasis. In Lorentzian signature the induced metric on bivectors has signature $(3,3)$, a self-adjoint operator need not be diagonalizable, and the Petrov classification sorts the Weyl tensor by the algebraic form of this operator.

The sectional curvature $K(u,v) = \mathrm{Rm}(u,v,u,v)/\big(g(u,u)g(v,v) - g(u,v)^2\big)$ depends only on the plane of $u$ and $v$, by (a) and (c). With (b) and (d), its values on nondegenerate planes fix $\mathrm{Rm}$. So if $K$ takes one value $k$ on every plane at $p$, then $R_{\rho\sigma\mu\nu} = k(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ at $p$, because the right side has all four symmetries and the same sectional curvatures.

Limits.

- A torsion-free connection that preserves no metric keeps only (a) and (b). Its trace $R^\lambda{}_{\lambda\mu\nu} = \partial_\mu\Gamma^\lambda{}_{\nu\lambda} - \partial_\nu\Gamma^\lambda{}_{\mu\lambda}$ can be nonzero, which (c) forbids, and then $R_{\mu\nu} - R_{\nu\mu} = R^\lambda{}_{\lambda\mu\nu} \neq 0$.
- A metric connection with torsion, as in Einstein–Cartan theory, keeps (a) and (c). The cyclic sum becomes a combination of the torsion and its covariant derivative, and pair exchange and the symmetry of the Ricci tensor fail in general.
- Under $g \to -g$, $R^\lambda{}_{\sigma\mu\nu}$ is unchanged and every $R_{\rho\sigma\mu\nu}$ flips sign, so all four relations survive. In a Lorentzian orthonormal frame the antisymmetry needs both indices down: $R^{\hat 0}{}_{\hat i\mu\nu} = +R^{\hat i}{}_{\hat 0\mu\nu}$.

**Takeaway:** Last-pair antisymmetry holds for any connection, the cyclic identity needs zero torsion, first-pair antisymmetry needs a metric connection, and together they give pair exchange.

*What this leaves out:* Connections on the tangent bundle; on other vector bundles only (a) holds, and (c) given a bundle metric.

*Continues:* `ways_in/rules-from-the-metric`<br>*Builds on:* [[levi-civita-connection]], [[metric-compatibility]], [[torsion-free-connection]], [[lie-bracket]]<br>*See:* `problems/pair-exchange-from-the-others`, `checks/connection-without-a-metric`, `checks/ricci-with-torsion`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| loop | — | A path that ends exactly where it began. | — |
| swing | — | To move a carried arrow so that it points a different way. Along the ground that means left or right; with more directions to move in, it means any way at all, even up or down. The arrow test never lets it swing. | — |
| tilt | — | A pair of directions at a spot, like the bottom, front or side of a box. A loop's tilt is set by the two directions its sides run along. An arrow's tilt is set by its starting direction and the direction its lean is read in. | — |
| Riemann curvature tensor | REE-mahn | A table kept at every spot. For each tilt of a tiny loop and each starting direction of an arrow, it lists how the arrow comes back changed, divided by the loop's area. | [[riemann-curvature-tensor]] |
| lean | — | The distance an arrow's tip has moved toward a second direction. A tip that has moved away from that direction leans away. | — |
| lean rule | — | Of two equal arrows at right angles carried around a tiny loop, one leans toward the other as far as the other leans away. | [[symmetries-of-the-riemann-tensor]] |
| mirror rule | — | Swapping a loop's tilt with the arrow's tilt leaves an entry of the curvature table unchanged. | [[symmetries-of-the-riemann-tensor]] |
| tidal drift | — | The slow drift of neighbouring objects falling freely near a planet: apart along the line toward the planet's centre, and together across it. | [[tidal-force]] |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| spacetime | — | Space and time taken together as one world with four directions: three of space and one of time. | [[spacetime]] |

## Key equations

### Riemann tensor with its first index lowered · working

$$
R_{\rho\sigma\mu\nu} = g_{\rho\lambda}\,R^\lambda{}_{\sigma\mu\nu}
$$

The symmetries are statements about this form, with the output index lowered by the metric.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\rho\sigma\mu\nu}$ | the all-lower Riemann tensor | R rho sigma mu nu |
| $g_{\rho\lambda}$ | the metric | the metric |
| $R^\lambda{}_{\sigma\mu\nu}$ | the Riemann tensor in the course convention, loop edges in the last two slots | the Riemann tensor |

**Holds when:** Any metric; the only upper index is the one lowered.  
**Say it:** “R rho sigma mu nu is the metric contracted with the first index of the Riemann tensor.”  
**Justified by:** `raising-and-lowering-indices`

### Pair antisymmetries and pair exchange · working

$$
R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}
$$

Swapping the indices within either pair flips the sign; trading the two pairs leaves the value unchanged.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\rho\sigma$ | first pair: output slot and carried-vector slot | the first pair |
| $\mu\nu$ | last pair: the edges of the small loop | the last pair |

**Holds when:** Levi-Civita connection; all four indices lowered; any basis.  
**Say it:** “R rho sigma mu nu equals minus R sigma rho mu nu, equals minus R rho sigma nu mu, equals R mu nu rho sigma.”  
**Justified by:** `derivations/rules-from-the-four-term-formula`

### The whole tensor in two dimensions · working

$$
R_{\rho\sigma\mu\nu} = K\,\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big),\qquad K = \frac{R_{1212}}{\det g}
$$

In two dimensions the rules leave a single component, so the Gaussian curvature fixes the whole tensor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature; $+1/a^2$ on a sphere of radius $a$ | K |
| $\det g$ | determinant of the metric components | the determinant of the metric |

**Holds when:** Two dimensions; Levi-Civita connection. Taken on trust in the working way and proved in the problem "The whole two-dimensional table".  
**Say it:** “R rho sigma mu nu equals K times g rho mu g sigma nu minus g rho nu g sigma mu, with K equal to R one two one two over the determinant of the metric.”  
**Justified by:** `stated`

### What a turning gradiometer reads · working

$$
f_i = M_{ij}\,\xi^j,\qquad M = E + \boldsymbol\Omega\boldsymbol\Omega^{\mathsf T} - \Omega^2\,\mathbb 1 + [\dot{\boldsymbol\Omega}\times]
$$

The force per unit mass that holds a proof mass in a turning, freely falling spacecraft: symmetric tidal and centrifugal parts, plus an antisymmetric angular-acceleration part.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E$ | tidal matrix $c^2R_{\hat i\hat 0\hat j\hat 0}$, symmetric by pair exchange | the tidal matrix |
| $\boldsymbol\Omega$ | angular velocity of the spacecraft relative to a non-rotating frame | omega |
| $[\dot{\boldsymbol\Omega}\times]$ | the antisymmetric matrix with $[\dot{\boldsymbol\Omega}\times]\boldsymbol\xi = \dot{\boldsymbol\Omega}\times\boldsymbol\xi$ | the angular-acceleration matrix |

**Holds when:** Spacecraft centre in free fall; separations small compared with the distance over which the tidal field changes; components along the spacecraft's axes.  
**Say it:** “The holding force per unit mass is M times the offset, where M is the tidal matrix plus the centrifugal matrix plus the angular-acceleration matrix.”  
**Justified by:** `stated`

### Curvature of a metric connection is skew-adjoint · formal

$$
g\big(\mathcal R(X,Y)Z,\,W\big) = -\,g\big(Z,\,\mathcal R(X,Y)W\big)
$$

For a metric connection each curvature operator is an infinitesimal rotation or boost: first-pair antisymmetry without coordinates.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathcal R(X,Y)$ | curvature operator for the vector fields $X$ and $Y$ | the curvature of X and Y |

**Holds when:** $\nabla g = 0$; torsion is allowed.  
**Say it:** “g of the curvature of X and Y acting on Z, with W, equals minus g of Z with the curvature of X and Y acting on W.”  
**Justified by:** `derivations/metric-compatibility-forces-first-pair-antisymmetry`

## Derivations

### Reading the rules off the metric · working

**Goal:** Show that $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$ in every basis.

1. At a point $P$ choose coordinates with $\partial_\lambda g_{\mu\nu}(P) = 0$. There $R_{\rho\sigma\mu\nu} = \tfrac12\big(\partial_\sigma\partial_\mu g_{\rho\nu} - \partial_\sigma\partial_\nu g_{\rho\mu} + \partial_\rho\partial_\nu g_{\sigma\mu} - \partial_\rho\partial_\mu g_{\sigma\nu}\big)$, the four-term formula of the Riemann tensor in normal coordinates.
2. Swap $\rho$ and $\sigma$. The new first term is minus the old fourth, the new fourth is minus the old first, and the second and third trade places the same way, so the sum flips sign.
3. Swap $\mu$ and $\nu$. The new first term is minus the old second, the new third is minus the old fourth, and so on, so the sum flips sign again.
4. Trade the pairs, $\rho\sigma \leftrightarrow \mu\nu$: $\tfrac12\big(\partial_\nu\partial_\rho g_{\mu\sigma} - \partial_\nu\partial_\sigma g_{\mu\rho} + \partial_\mu\partial_\sigma g_{\nu\rho} - \partial_\mu\partial_\rho g_{\nu\sigma}\big)$.
5. With $g_{\mu\sigma} = g_{\sigma\mu}$ and commuting partial derivatives, these are the old third, second, first and fourth terms with their old signs, so the value is unchanged.
6. Each difference, such as $D_{\rho\sigma\mu\nu} = R_{\rho\sigma\mu\nu} - R_{\mu\nu\rho\sigma}$, is a tensor at $P$ whose components all vanish in these coordinates, so they vanish in every basis.
7. $P$ was arbitrary, so the three relations hold everywhere.

**Result:** $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$ for the Levi-Civita connection, in every basis.

### Metric compatibility forces first-pair antisymmetry · working

**Goal:** Show $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$ in any coordinates from $\nabla g = 0$.

1. For a torsion-free connection, the commutator of covariant derivatives on a tensor with two lower indices has one Riemann term per index, each with a minus sign: $[\nabla_\mu,\nabla_\nu]T_{\rho\sigma} = -R^\lambda{}_{\rho\mu\nu}T_{\lambda\sigma} - R^\lambda{}_{\sigma\mu\nu}T_{\rho\lambda}$.
2. Take $T = g$. Metric compatibility makes $\nabla g = 0$, so the left side vanishes.
3. Lowering gives $R^\lambda{}_{\rho\mu\nu}g_{\lambda\sigma} = R_{\sigma\rho\mu\nu}$ and $R^\lambda{}_{\sigma\mu\nu}g_{\rho\lambda} = R_{\rho\sigma\mu\nu}$.
4. So $0 = -R_{\sigma\rho\mu\nu} - R_{\rho\sigma\mu\nu}$.

**Result:** $R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu}$ wherever $\nabla g = 0$, with no special coordinates.

## Worked examples

### A sphere's whole table from one component · working

**Problem:** On a sphere of radius $a$, $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, one computation gives $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. Use the rules to find all sixteen lowered components, and check the two-dimensional form.

1. Lower with $g_{\theta\theta} = a^2$: $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$.
2. A repeated index inside a pair gives zero, which removes the 12 slots with $\theta\theta$ or $\phi\phi$ in either pair.
3. The antisymmetries give the other three: $R_{\phi\theta\phi\theta} = a^2\sin^2\theta$ and $R_{\theta\phi\phi\theta} = R_{\phi\theta\theta\phi} = -a^2\sin^2\theta$. Pair exchange is then automatic.
4. $\det g = a^4\sin^2\theta$, so $K = R_{\theta\phi\theta\phi}/\det g = 1/a^2$, and $K\,(g_{\theta\theta}g_{\phi\phi} - g_{\theta\phi}g_{\phi\theta}) = a^2\sin^2\theta$ matches.

**Answer:** Four nonzero components, $\pm a^2\sin^2\theta$, and $K = 1/a^2$.

**Takeaway:** In two dimensions one computed component fixes all sixteen, and the sphere comes out with positive curvature, as the course conventions require.

## Problems

### `count-in-space-and-time` · entry · difficulty 2 · calculation

Space and time together have four directions: ahead, left, up and time. How many entries does the curvature table have before any rule is used? How many tilts are there, and how many different numbers are left after the rule for walking a loop the other way and the lean rule? How many after the mirror rule?

**Hints**

1. Each entry needs four choices of direction.
2. List the tilts that include time, then the tilts that do not.
3. How many of those numbers have matching tilts?

**Answer:** 256 entries, 6 tilts, 36 numbers after the first two rules, and 21 after the mirror rule.

**Must contain:** Four choices among four directions give 256 entries; Four directions give six tilts; Six tilts by six tilts give 36 numbers; Six matching numbers plus fifteen pairs give 21

**Numeric:** entries before any rule = 256 1 (magnitude, ±0.1); numbers after the mirror rule = 21 1 (magnitude, ±0.1)

**Solution**

1. Each entry takes four choices among four directions, and 4 times 4 times 4 times 4 is 256.
2. The tilts are time with each of ahead, left and up, plus ahead with left, ahead with up, and left with up: six in all.
3. The rule for walking a loop the other way and the lean rule leave one number for each loop's tilt and each arrow's tilt, so 6 times 6 gives 36 numbers.
4. The mirror rule keeps the 6 numbers with matching tilts and pairs up the other 30 into 15, so 6 plus 15 gives 21.

**Targets:** `every-slot-is-new`

### `whole-two-dimensional-table` · working · difficulty 2 · derivation

In two dimensions, show that the pair antisymmetries leave one independent component, $R_{1212}$, and that $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ with $K = R_{1212}/\det g$. Then find $K$ for $ds^2 = dr^2 + \sinh^2 r\,d\phi^2$, given $R_{r\phi r\phi} = -\sinh^2 r$.

**Hints**

1. Which values can a pair take without the component vanishing?
2. Check that the right side obeys both antisymmetries, then compare the $1212$ components.

**Answer:** Every component is $0$ or $\pm R_{1212}$, the right side has the same pattern with $1212$ component $K\det g$, and the given metric has $K = -1$.

**Must contain:** A nonzero component needs 12 or 21 in each pair; The right side is antisymmetric within each pair; Its 1 2 1 2 component is K times the determinant of the metric; The given metric has K equal to minus one

**Numeric:** K for the given metric = -1 1 (signed, ±0.01)

**Solution**

1. Antisymmetry within a pair kills $11$ and $22$, so each pair is $12$ or $21 = -12$. Every component is therefore $0$ or $\pm R_{1212}$.
2. $T_{\rho\sigma\mu\nu} = g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}$ changes sign under $\rho \leftrightarrow \sigma$ and under $\mu \leftrightarrow \nu$, so it has the same pattern.
3. $T_{1212} = g_{11}g_{22} - g_{12}g_{21} = \det g$.
4. Two tensors with the same one-component pattern agree when their $1212$ components agree, so $R_{\rho\sigma\mu\nu} = (R_{1212}/\det g)\,T_{\rho\sigma\mu\nu}$.
5. For $dr^2 + \sinh^2 r\,d\phi^2$, $\det g = \sinh^2 r$, so $K = -\sinh^2 r/\sinh^2 r = -1$.

### `pair-exchange-from-the-others` · formal · difficulty 3 · proof

Let $R_{\rho\sigma\mu\nu}$ be antisymmetric in $\rho\sigma$ and in $\mu\nu$, and let $S_{\rho\sigma\mu\nu} \equiv R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu}$. Show that $S_{\rho\sigma\mu\nu} - S_{\sigma\mu\nu\rho} - S_{\mu\nu\rho\sigma} + S_{\nu\rho\sigma\mu} = 2(R_{\rho\sigma\mu\nu} - R_{\mu\nu\rho\sigma})$, and conclude that the cyclic identity implies pair exchange. Does pair exchange, with the antisymmetries, imply the cyclic identity?

**Hints**

1. Write out all twelve terms and use the antisymmetries to match them.
2. For the converse, try a totally antisymmetric tensor in four dimensions.

**Answer:** Eight of the twelve terms cancel in pairs and four combine into $2R_{\rho\sigma\mu\nu} - 2R_{\mu\nu\rho\sigma}$, so $S = 0$ gives pair exchange. The converse fails: $\epsilon_{\rho\sigma\mu\nu}$ obeys both antisymmetries and pair exchange, but its cyclic sum is $3\epsilon_{\rho\sigma\mu\nu} \neq 0$.

**Must contain:** Only the pair antisymmetries are used to cancel eight terms; The four survivors give twice R rho sigma mu nu minus R mu nu rho sigma; A vanishing cyclic sum therefore gives pair exchange; The totally antisymmetric symbol obeys pair exchange but not the cyclic identity

**Solution**

1. The twelve terms are $R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu}$, $-R_{\sigma\mu\nu\rho} - R_{\sigma\nu\rho\mu} - R_{\sigma\rho\mu\nu}$, $-R_{\mu\nu\rho\sigma} - R_{\mu\rho\sigma\nu} - R_{\mu\sigma\nu\rho}$ and $R_{\nu\rho\sigma\mu} + R_{\nu\sigma\mu\rho} + R_{\nu\mu\rho\sigma}$.
2. By the antisymmetries, $-R_{\sigma\rho\mu\nu} = R_{\rho\sigma\mu\nu}$ and $R_{\nu\mu\rho\sigma} = -R_{\mu\nu\rho\sigma}$, which gives $2R_{\rho\sigma\mu\nu} - 2R_{\mu\nu\rho\sigma}$ from four terms.
3. The rest cancel in pairs: $R_{\mu\rho\sigma\nu} = R_{\rho\mu\nu\sigma}$, $R_{\nu\rho\sigma\mu} = -R_{\rho\nu\sigma\mu}$, $R_{\nu\sigma\mu\rho} = R_{\sigma\nu\rho\mu}$ and $R_{\mu\sigma\nu\rho} = -R_{\sigma\mu\nu\rho}$.
4. If the cyclic identity holds, every $S$ vanishes, so $R_{\rho\sigma\mu\nu} = R_{\mu\nu\rho\sigma}$.
5. For the converse, $\epsilon_{\rho\sigma\mu\nu}$ changes sign within each pair, and moving one pair past the other is an even permutation, so pair exchange holds. Cyclic permutations of three indices are even, so its cyclic sum is $3\epsilon_{\rho\sigma\mu\nu}$.

## Observations

- **Gravity gradients measured by the gradiometer of ESA's GOCE satellite** (measured, working). From 2009 to 2013 GOCE carried three orthogonal pairs of accelerometers about 255 km above Earth. Differences of their readings form the matrix $M$ of "A gradiometer splits spin from gravity". Its antisymmetric part is taken as the satellite's angular acceleration, because tidal and centrifugal terms are symmetric; the symmetric part, corrected for the measured rotation, gives the gravity gradients used to map Earth's gravity field. *Numbers:* At $r = 6626$ km for a spherical Earth: the second derivative of the potential along the radius is $-2GM/r^3 = -2.74\times10^{-6}\ \mathrm{s^{-2}}$ and across it $+1.37\times10^{-6}\ \mathrm{s^{-2}}$; the once-per-orbit rotation adds $-1.37\times10^{-6}\ \mathrm{s^{-2}}$ to the along-track and radial diagonal entries. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0

## Teaching arc

1. **Turn a taped cross** (entry). Ask for a prediction about the second tip, then turn a pinned pencil cross and measure both tips. *Why:* The lean rule becomes a measurement before it becomes an index swap. *Predict:* If the first arrow's tip moves two millimetres toward the second arrow, where does the second arrow's tip go? *Visual:* [[tips-of-a-turning-cross]] *Uses:* `ways_in/two-arrows-at-right-angles`, `checks/lean-of-the-second-arrow`
2. **Hunt for a whirlpool** (entry). Release four crumbs in a falling room, add their drifts around the ring, and run the energy argument. *Why:* It gives the mirror rule a physical reason and a measurable face. *Predict:* Could tidal drift near a planet carry a ring of falling crumbs around in a whirlpool? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/tides-without-a-whirlpool`, `checks/four-crumbs-and-a-whirlpool`
3. **Count what is left** (entry). Shrink 81 entries to 6 numbers together, then let the learner count a surface, and space and time. *Why:* The count shows why the rules matter, and why a ball needs only one number. *Predict:* How many different numbers does the table need at a spot on a surface? *Visual:* [[twenty-of-256-slots]] *Uses:* `ways_in/counting-what-the-table-holds`, `checks/count-on-a-surface-and-in-space`, `problems/count-in-space-and-time`
4. **Read the rules and guard index positions** (working). Read the rules off the four-term formula, promote them to every basis, then test a mixed component on the sphere. *Why:* Proof and pitfall together fix the rules and their condition on index positions. *Predict:* On a sphere, is the mixed partner of sine squared theta simply minus sine squared theta? *Uses:* `ways_in/rules-from-the-metric`, `derivations/rules-from-the-four-term-formula`, `checks/mixed-index-partner`
5. **Climb the assumption ladder** (formal). Separate what each rule needs, then break the rules with a connection that preserves no metric. *Why:* Graduate readers meet connections with torsion or non-metricity and must know which identities still hold. *Uses:* `ways_in/assumption-ladder`, `checks/connection-without-a-metric`, `problems/pair-exchange-from-the-others`

## Misconceptions

### “If a loop makes one arrow lean toward a second arrow, it makes the second arrow lean toward the first too.” · entry · `both-arrows-lean-together`

- **Why it is tempting:** Squashing a cardboard frame out of square does move two of its sides toward each other.
- **What is true:** Carried arrows keep their right angle and their length, so the pair turns as one piece. For a tiny loop, one then leans toward the other as far as the other leans away.
- **Exposed by:** `checks/lean-of-the-second-arrow`

### “The curvature table in space needs all 81 of its numbers.” · entry · `every-slot-is-new`

- **Why it is tempting:** Each entry seems to come from its own test, with its own loop and arrow.
- **What is true:** The three rules make most entries zeros or repeats of others. Six different numbers remain in space, and one on a surface.
- **Exposed by:** `checks/count-on-a-surface-and-in-space`

### “Tidal drift could carry a ring of falling crumbs around in a whirlpool.” · entry · `tides-can-whirl`

- **Why it is tempting:** Tidal drift pushes crumbs sideways as well as in and out.
- **What is true:** A whirlpool would give a crumb carried around the ring energy from nothing. Near a planet whose gravity does not change with time, gravity gives back all the energy it takes around any loop, so the sideways drifts balance.
- **Exposed by:** `checks/four-crumbs-and-a-whirlpool`

### “The Riemann tensor with its first index still up is also antisymmetric in its first two indices.” · working · `mixed-tensor-antisymmetric`

- **Why it is tempting:** The rules are quoted compactly, and the mixed tensor is what a calculation produces first.
- **What is true:** Antisymmetry holds only with both indices at the same level, and raising or lowering brings in metric factors. On a sphere the mixed partner of sine squared theta is minus one.
- **Exposed by:** `checks/mixed-index-partner`

### “Rules proved in coordinates where the metric has zero first derivatives hold only in those coordinates.” · working · `only-in-special-coordinates`

- **Why it is tempting:** The proof visibly relies on those special coordinates.
- **What is true:** Each rule says that a tensor built from the Riemann tensor vanishes, and a tensor that vanishes in one basis vanishes in all. Only the four-term formula itself is tied to those coordinates.
- **Exposed by:** `checks/proved-where-connection-vanishes`

### “All the Riemann symmetries hold for any connection.” · formal · `symmetries-for-any-connection`

- **Why it is tempting:** General relativity always uses the Levi-Civita connection, so the assumptions are rarely stated.
- **What is true:** Only last-pair antisymmetry is universal. The cyclic identity needs zero torsion, first-pair antisymmetry needs a metric connection, and pair exchange needs both.
- **Exposed by:** `checks/connection-without-a-metric`, `checks/ricci-with-torsion`

## Checks

1. **Entry · predict** `checks/lean-of-the-second-arrow`. You stand on a huge, smooth ball. You tape two cardboard arrows, each 10 centimetres long, tail to tail at a right angle, and lay the pair flat on the ground. One arrow points ahead of you and one points to your left. You carry the pair around a loop, never letting either arrow swing. Back at the start, you face the way you faced when you set off, and the ahead arrow's tip has moved 2 millimetres toward your left. Where has the left arrow's tip moved, and how far?
   - **Hints:** What does the tape do to the angle between the arrows?
   - **Answer:** About 2 millimetres backward, away from the ahead arrow. The tape keeps the arrows at a right angle, and cardboard does not stretch, so the pair can only turn as one piece. The ahead arrow's tip has moved 2 millimetres toward the left arrow. If the left arrow's tip moved backward by less, the angle between the arrows would shrink, and if by more, it would grow. The right angle stays, so the left arrow's tip moves backward by the same 2 millimetres.
   - **Must contain:** It moves backward, away from the ahead arrow; It moves the same 2 millimetres; The right angle is kept, so the pair turns as one piece
   - **Numeric:** lean of the left arrow's tip toward ahead = -2 mm (signed, ±0.3)
   - **Targets:** `both-arrows-lean-together`
   - **Visual:** [[tips-of-a-turning-cross]]
2. **Entry · numeric** `checks/count-on-a-surface-and-in-space`. A surface has two directions, ahead and left. Space has three: ahead, left and up. Use three rules: walking a loop the other way flips the change, the lean rule, and the mirror rule. How many different numbers does the curvature table need at a spot on a surface? How many at a spot in space?
   - **Hints:** List the tilts first.
   - **Answer:** One on a surface, and six in space. On a surface the only tilt is ahead with left. Every entry that is not zero has that tilt for its loop and for its arrow, so 1 number remains. In space there are three tilts: ahead with left, ahead with up, and left with up. Walking a loop the other way and the lean rule leave one number for each loop's tilt and each arrow's tilt, so 3 times 3 gives 9 numbers. In 3 of them the two tilts match. The mirror rule makes the other 6 equal in pairs, which gives 3 more, so 6 numbers remain.
   - **Must contain:** One number on a surface; Nine numbers in space before the mirror rule; The mirror rule leaves six
   - **Numeric:** numbers on a surface = 1 1 (magnitude, ±0.1); numbers in space = 6 1 (magnitude, ±0.1)
   - **Targets:** `every-slot-is-new`
   - **Visual:** [[twenty-of-256-slots]]
3. **Entry · evaluate-claim** `checks/four-crumbs-and-a-whirlpool`. A room falls freely toward a round planet whose gravity at each place stays the same from moment to moment, and the room does not spin. A crew picks two directions at right angles, A and B. They let go of four crumbs, each at rest in the room and 1 metre from its centre. One is out along A, one out along B, and one on the far side of the centre from each of those. After 10 seconds they report two sideways drifts. The crumb out along A drifted 5 hundredths of a millimetre toward B. The crumb out along B drifted only 2 hundredths of a millimetre toward A. Could the report be right?
   - **Hints:** Which way around the ring does each crumb drift? / What would a crumb carried once around the ring gain?
   - **Answer:** No. Go around the ring from the crumb out along A toward the crumb out along B, and call that way forward. At the crumb out along A, forward points toward B, so its 5 hundredths of a millimetre count forward. At the crumb out along B, forward points away from A, so its 2 hundredths count backward. At each far-side crumb, the drift and forward both point the opposite way, so the far-side crumbs add the same again. So the forward drifts total 10 hundredths and the backward drifts 4 hundredths: 6 hundredths of a millimetre more forward, a whirlpool. The drifts come from extra pulls, so those pulls would push a crumb carried once around the ring forward more than backward, and it would gain energy from nothing. Near such a planet gravity gives back all the energy it takes around any loop, so the two sideways drifts must be equal.
   - **Must contain:** The report cannot be right; The drifts would form a whirlpool; A whirlpool would make energy from nothing
   - **Numeric:** net forward drift around the ring in the report, going from A toward B = 0.06 mm (signed, ±0.005)
   - **Targets:** `tides-can-whirl`
   - **Visual:** [[falling-ring-of-crumbs]]
4. **Working · evaluate-claim** `checks/mixed-index-partner`. On a sphere of radius $a$, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. A classmate writes $R^\phi{}_{\theta\theta\phi} = -\sin^2\theta$, citing antisymmetry in the first pair. Find $R^\phi{}_{\theta\theta\phi}$ and evaluate the step.
   - **Hints:** Which metric component lowers $\theta$, and which raises $\phi$?
   - **Answer:** Lower first: $R_{\theta\phi\theta\phi} = g_{\theta\theta}\sin^2\theta = a^2\sin^2\theta$. Antisymmetry in the first pair gives $R_{\phi\theta\theta\phi} = -a^2\sin^2\theta$. Raise with $g^{\phi\phi} = 1/(a^2\sin^2\theta)$: $R^\phi{}_{\theta\theta\phi} = -1$. The classmate is wrong, because antisymmetry holds only with both first-pair indices lowered, and $g_{\theta\theta}$ and $g^{\phi\phi}$ bring different factors.
   - **Must contain:** It equals minus one; Lower, swap, then raise; The rule needs both first-pair indices lowered
   - **Numeric:** R upper phi lower theta theta phi = -1 1 (signed, ±0.01)
   - **Targets:** `mixed-tensor-antisymmetric`
5. **Working · evaluate-claim** `checks/proved-where-connection-vanishes`. The rules were read off the four-term formula at a point where $\partial_\lambda g_{\mu\nu} = 0$. A classmate says they may fail for Schwarzschild components in Schwarzschild coordinates, where the Christoffel symbols do not vanish. Evaluate the claim. What from that derivation does not carry over?
   - **Hints:** Is each rule a tensor equation?
   - **Answer:** The rules carry over. Each says that a tensor, such as $R_{\rho\sigma\mu\nu} - R_{\mu\nu\rho\sigma}$, has zero components at the point. Components transform linearly under a change of coordinates, so zero components stay zero. What does not carry over is the four-term formula itself: in Schwarzschild coordinates the lowered tensor also contains products of Christoffel symbols.
   - **Must contain:** The rules hold in Schwarzschild coordinates; A tensor that vanishes in one basis vanishes in every basis; The four-term formula does not carry over
   - **Targets:** `only-in-special-coordinates`
6. **Working · numeric** `checks/gradiometer-spin`. A gradiometer in a freely falling satellite reads $M_{xy} = 3.0\times10^{-8}\ \mathrm{s^{-2}}$ and $M_{yx} = -1.0\times10^{-8}\ \mathrm{s^{-2}}$, where $M = E + \boldsymbol\Omega\boldsymbol\Omega^{\mathsf T} - \Omega^2\mathbb 1 + [\dot{\boldsymbol\Omega}\times]$. Find $\dot\Omega_z$ and the value of $E_{xy} + \Omega_x\Omega_y$.
   - **Hints:** Split $M$ into its symmetric and antisymmetric parts. / Write out $\dot{\boldsymbol\Omega}\times\boldsymbol\xi$ for $\boldsymbol\xi$ along $y$.
   - **Answer:** The tidal and centrifugal terms are symmetric, so the antisymmetric part $\tfrac12(M_{xy} - M_{yx}) = 2.0\times10^{-8}\ \mathrm{s^{-2}}$ comes from $[\dot{\boldsymbol\Omega}\times]$ alone. Its $xy$ entry is $-\dot\Omega_z$, so $\dot\Omega_z = -2.0\times10^{-8}\ \mathrm{rad\,s^{-2}}$. The symmetric part is $\tfrac12(M_{xy} + M_{yx}) = 1.0\times10^{-8}\ \mathrm{s^{-2}} = E_{xy} + \Omega_x\Omega_y$.
   - **Must contain:** Split M into symmetric and antisymmetric parts; Angular acceleration minus two times ten to the minus eight; Symmetric part one times ten to the minus eight
   - **Numeric:** angular acceleration about z, in units of ten to the minus eight radians per second squared = -2 1 (signed, ±0.05); E x y plus omega x omega y, in units of ten to the minus eight per second squared = 1 1 (signed, ±0.05)
7. **Formal · derive** `checks/connection-without-a-metric`. On the plane with coordinates $(x, y)$, take the torsion-free connection whose only nonzero symbols are $\Gamma^x{}_{xy} = \Gamma^x{}_{yx} = x$ and $\Gamma^y{}_{yy} = 2x$. Compute $R^\lambda{}_{\lambda xy}$ and the Ricci components $R_{xy}$ and $R_{yx}$. Which of the four algebraic symmetries survive, and can this be the Levi-Civita connection of any metric?
   - **Hints:** Use $R^\lambda{}_{\lambda\mu\nu} = \partial_\mu\Gamma^\lambda{}_{\nu\lambda} - \partial_\nu\Gamma^\lambda{}_{\mu\lambda}$. / What would first-pair antisymmetry say about the trace?
   - **Answer:** $\Gamma^\lambda{}_{y\lambda} = 3x$ and $\Gamma^\lambda{}_{x\lambda} = 0$, and the product terms form the trace of a commutator, so $R^\lambda{}_{\lambda xy} = \partial_x(3x) = 3$. Directly, $R^x{}_{xxy} = 1$, $R^y{}_{yxy} = 2$, $R^x{}_{yxy} = x^2$ and $R^y{}_{xxy} = 0$. So $R_{xy} = R^x{}_{xxy} + R^y{}_{xyy} = 1$ and $R_{yx} = R^x{}_{yxx} + R^y{}_{yyx} = -2$, consistent with $R_{\mu\nu} - R_{\nu\mu} = R^\lambda{}_{\lambda\mu\nu}$. Last-pair antisymmetry holds for every connection, and the cyclic identity holds because the torsion vanishes. First-pair antisymmetry fails for every metric used to lower the index, since it would force $R^\lambda{}_{\lambda\mu\nu} = g^{\lambda\kappa}R_{\kappa\lambda\mu\nu} = 0$. Pair exchange with last-pair antisymmetry would imply first-pair antisymmetry, so it fails too. No metric has this Levi-Civita connection.
   - **Must contain:** The trace is three; R x y is one and R y x is minus two; Last-pair antisymmetry and the cyclic identity survive; First-pair antisymmetry fails, so no metric gives it
   - **Numeric:** R lambda lambda x y = 3 1 (signed, ±0.01)
   - **Targets:** `symmetries-for-any-connection`
8. **Formal · explain** `checks/ricci-with-torsion`. For the Levi-Civita connection, show that the Ricci tensor $R_{\mu\nu} = R^\lambda{}_{\mu\lambda\nu}$ is symmetric. Does the argument survive for a metric connection with torsion, as in Einstein–Cartan theory?
   - **Hints:** Which rule moves the contracted indices from one pair to the other?
   - **Answer:** $R_{\mu\nu} = g^{\lambda\kappa}R_{\kappa\mu\lambda\nu}$. Pair exchange gives $R_{\kappa\mu\lambda\nu} = R_{\lambda\nu\kappa\mu}$, and $g^{\lambda\kappa}R_{\lambda\nu\kappa\mu} = R^\kappa{}_{\nu\kappa\mu} = R_{\nu\mu}$. With torsion both pair antisymmetries survive, but the cyclic sum picks up torsion terms. Pair exchange rested on the cyclic identity, so it fails in general, and with it the symmetry of the Ricci tensor.
   - **Must contain:** Pair exchange gives a symmetric Ricci tensor; Torsion spoils the cyclic identity; Pair exchange and Ricci symmetry then fail
   - **Targets:** `symmetries-for-any-connection`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| How the cyclic identity is written | $R_{\rho\sigma\mu\nu} + R_{\rho\mu\nu\sigma} + R_{\rho\nu\sigma\mu} = 0$, cycling the last three indices with the first fixed. | Some texts cycle the other way or write $R_{\rho[\sigma\mu\nu]} = 0$ with antisymmetrizing brackets; given the pair antisymmetries, all these forms are equivalent. |
| Signs of lowered components | Signature $(-,+,+,+)$; a sphere of radius $a$ has $R_{\theta\phi\theta\phi} = +a^2\sin^2\theta$. | With the opposite overall sign of the metric, as in signature $(+,-,-,-)$, every $R_{\rho\sigma\mu\nu}$ flips sign for the same geometry while $R^\lambda{}_{\sigma\mu\nu}$ does not; the symmetry relations are unchanged. |

## Visuals

- ★ [[tips-of-a-turning-cross]] (flagship): The lean rule made visible: two equal arrows at right angles turn as one piece, with equal and opposite leans. *Sketch:* Two equal arrows taped at a right angle, on a ball's surface or in space. The learner carries them around a tiny loop or tips the pair by a small angle about any axis. A large tip about an axis in the arrows' own plane makes both tips lean toward each other, so the readouts must show that the leans differ only at second order in the angle. Readouts show each tip's lean toward the other arrow and its much smaller slip along itself. A squash control, marked as not allowed for carried arrows, bends the right angle and breaks the equality.
- [[falling-ring-of-crumbs]] (core): Tidal drift with no whirlpool: the mirror rule seen in falling crumbs. *Sketch:* Adds two chosen directions, a table of the sideways drifts, and a readout of net forward drift around the ring, which stays zero. A switch shows an invented whirlpool table, where a crumb carried around the ring gains energy every lap.
- [[twenty-of-256-slots]] (core): Counts what the rules leave: 1, 6 or 20. *Sketch:* A grid of all index combinations with a dimension selector for 2, 3 and 4. Applying last-pair antisymmetry, first-pair antisymmetry, pair exchange and the cyclic identity in turn greys out zero slots, links partners with signs, and ends at 1, 6 or 20.

## Tutor moves

**Open with**

- Tape two equal cardboard arrows together at their tails, at a right angle, and lay them on a table. Turn the pair a little. If one arrow's tip moves two millimetres toward the other arrow, where does the other arrow's tip go? *(prediction)*

**If the learner is stuck**

- *The learner cannot see why the four crumbs' drifts add up around the ring.* → Draw the ring with its four crumbs, mark the forward direction at each crumb, and add the sideways drifts one crumb at a time. *Uses:* `checks/four-crumbs-and-a-whirlpool`

**Common questions**

- *Why do these rules matter?* (entry) They save work and explain a puzzle. Whoever computes curvature finds one entry and gets its partners for free. They also explain why one number describes a ball's curving at a spot, while space needs six. *Uses:* `ways_in/counting-what-the-table-holds`

**Switching levels**

- To working when: asks how the rules look in components; uses index notation. Read the rules off the four-term formula, then run the mixed-index check. *Uses:* `ways_in/rules-from-the-metric`, `checks/mixed-index-partner`
- To formal when: asks which assumptions the rules need; mentions torsion or other connections. Climb the assumption ladder and try the connection that preserves no metric. *Uses:* `ways_in/assumption-ladder`, `checks/connection-without-a-metric`
- To research when: asks how curvature is classified; asks what curvature says about topology. Open the research horizon. *Uses:* `research_horizon/petrov-types`, `research_horizon/positive-curvature-operator`

**Pronunciations:** Riemann → REE-mahn; Ricci → REE-chee; Levi-Civita → LEH-vee CHEE-vee-tah; Christoffel → kris-TOFF-el; Einstein–Cartan → EYEN-shtine kar-TAHN; Petrov → pyot-ROFF

## History

- **Elwin Bruno Christoffel (1869).** Wrote down the fully lowered four-index curvature quantity in terms of a metric's derivatives, the object whose index symmetries this note describes. Elwin Bruno Christoffel (1869), *Ueber die Transformation der homogenen Differentialausdrücke zweiten Grades*, Journal für die reine und angewandte Mathematik 70, 46–70, doi:10.1515/crll.1869.70.46

## Research horizon

- **Algebraic classification of spacetime curvature.** The pair rules make the Weyl part of four-dimensional curvature a self-adjoint operator on bivectors. Sorting it by algebraic form, or by how its principal null directions coincide, gives the Petrov types used to classify exact solutions; the Kerr black hole is type D. Roger Penrose (1960), *A spinor approach to general relativity*, Annals of Physics 10, 171–201, doi:10.1016/0003-4916(60)90021-X
- **Curvature operators and topology.** For a Riemannian metric the pair rules make the curvature operator self-adjoint, with real eigenvalues. Hamilton used the Ricci flow to show that a compact four-manifold with positive curvature operator is diffeomorphic to a quotient of the round sphere, and Böhm and Wilking extended this to every dimension. Richard S. Hamilton (1986), *Four-manifolds with positive curvature operator*, Journal of Differential Geometry 24, 153–179, doi:10.4310/jdg/1214440433; Christoph Böhm, Burkhard Wilking (2008), *Manifolds with positive curvature operators are space forms*, Annals of Mathematics 167, 1079–1097, doi:10.4007/annals.2008.167.1079
- **Curvature with torsion or non-metricity.** Theories in which spin sources torsion, or in which the connection is freed from the metric, keep only some of the rules. For a metric connection with torsion the curvature keeps both pair antisymmetries but loses pair exchange, so it has 36 independent components in four dimensions instead of 20, and the Ricci tensor need not be symmetric. Friedrich W. Hehl, Paul von der Heyde, G. David Kerlick, James M. Nester (1976), *General relativity with spin and torsion: Foundations and prospects*, Reviews of Modern Physics 48, 393–416, doi:10.1103/RevModPhys.48.393; Friedrich W. Hehl, J. Dermott McCrea, Eckehard W. Mielke, Yuval Ne'eman (1995), *Metric-affine gauge theory of gravity: field equations, Noether identities, world spinors, and breaking of dilation invariance*, Physics Reports 258, 1–171, doi:10.1016/0370-1573(94)00111-F

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** You tape two cardboard arrows at a right angle on a ball and carry them around a loop, and they come back turned together, so if one tip moves 2 millimetres toward the other arrow, the other tip moves 2 millimetres away, because the tape keeps the right angle. That's the lean rule. I don't get 'slips back along its own arrow', or whose left it is at the end. Then there's a falling room with four crumbs and something about going forward and backward around the ring; if it whirled you'd get free energy, so the sideways drifts are equal. I lost track of what 'forward' was, what the extra pull is extra to, and how that becomes the mirror rule, because I don't know what 'the tilt the arrows lean in' means. Then you count: 81 entries, down to 9, down to 6 in space and 1 on a surface. I followed the 81 but not 'three choices, four times over', and I'm not sure why the arrows only need a tilt. Compared with the takeaways: the lean-rule takeaway I could say back; the whirlpool takeaway I could say but not justify; the counting takeaway I could repeat without seeing where 9 came from.

**Stumbles (38)**

- “Carry arrows around tiny loops, and the curvature table records how they come back changed.”: The summary drops the arrow test's rule, so a reader could turn the arrows by hand and still expect a table.
- “And swapping the loop's tilt with the tilt the arrows lean in leaves an entry unchanged.”: 'The tilt the arrows lean in' is never defined anywhere in the entry ways; I reread it three times.
- “So at a spot on a surface the table holds one number, and in space six.”: The table holds 81 entries in space; what shrinks is the number of different numbers, so 'holds' contradicts the count.
- “Of two equal arrows at right angles, one leans toward the other exactly as far as the other leans away.”: Fails the first what-if in space: for a finite turn about a slanted line the two leans differ slightly, and the summary says neither 'carried' nor 'tiny loop'.
- “For each way of tilting the loop and each starting direction of the arrow, the curvature table lists how the arrow comes back changed.”: The recap uses 'tilting' without saying what a tilt is, and does not say what 'swing' means in space.
- “Lay the pair on the ground at a spot of a smooth ball, with one arrow pointing ahead of you”: Which ball: a football cannot be walked on. The scale of the scene is unclear.
- “The pair comes back turned a little, as one piece. Cardboard does not stretch, and the tape keeps the right angle.”: The claim comes before its reason and the link is left implicit.
- “Say the ahead arrow's tip has moved 2 millimetres toward your left, toward the left arrow.”: Whose left, facing which way? After a loop the walker may face any direction.
- “If the ahead arrow leaned toward the left arrow further than the left arrow leaned away, the angle between them would shrink.”: 'Lean' is used as a measured distance before it is introduced, and the other what-if (the left arrow leaning away more) is not answered.
- “Each tip also slips back a little along its own arrow, but far less.”: A surprise with no reason, and a side issue inside the lean-rule way; 'along its own arrow' is ambiguous once the arrow has turned.
- “In space, a tiny loop can tip the pair any way at all, and the same reason holds for any two equal arrows at right angles.”: 'Tip' is a fifth turning word beside swing, turn, lean and tilt, and the sentence is not exact: turned about a slanted line, the two leans differ by a small amount.
- “So the curvature table's entries come in opposite pairs, and knowing one entry tells you its partner.”: Which entries are partners is left implicit.
- “Tape two equal pencils into a cross at their middles and pin the crossing to card. Mark where two neighbouring tips sit.”: A pencil has one tip; the right angle and how the cross turns are not said.
- “With time as a direction, a change need not be a turn, and the lean rule holds only if parts along time count with the opposite sign.”: 'Parts along time' is unclear, and the sentence does not say the sign is left unexplained.
- “A room falls freely toward a round planet whose gravity never changes”: Gravity does change from place to place, which is the whole point of tidal drift; the sentence means 'not with time'.
- “one out along A, one out along B, and one opposite each of those.”: 'Opposite each' could mean at right angles, or facing; I had to reread.
- “Each drift comes from a small extra pull, and a bigger pull gives a bigger drift.”: Extra compared with what? The term is undefined.
- “The crumb out along A drifts forward by its sideways drift toward B.”: 'Forward' is never defined, so this sentence had to be reread several times.
- “The two opposite crumbs repeat the pattern.”: The step is implicit: why do the far-side crumbs add the same, not cancel?
- “If the forward drifts were bigger, the crumbs would form a whirlpool.”: Bigger than what, and what does a whirlpool of crumbs mean?
- “Near such a planet, gravity gives back all the energy it takes, whatever route a stone follows.”: A surprising claim with no everyday backing, and it holds only for routes that end where they began.
- “The extra pulls are differences of gravity between nearby spots, so they give back all they take too.”: Why a difference of two such pulls also gives back all it takes is left implicit.
- “This fairness is one case of a rule that every entry of the curvature table obeys, and we take the general rule on trust here. It is called the mirror rule”: A second new idea in the tides way (rule 17), using an undefined 'tilt its arrows lean in', and 'fairness' is a new word for the balance; nothing says which entries the drifts are.
- “Near a steady planet tidal drift forms no whirlpool”: 'Steady' could mean not spinning or not wobbling.
- “An arrow's lean along its own direction is too small to count.”: A rule in the recap with no reason anywhere in the entry ways.
- “Three choices, four times over, make 81 entries.”: Reread: three choices four times would be twelve.
- “A loop whose two sides run along the same direction encloses nothing, so it changes nothing.”: A square loop has four sides; 'two sides along the same direction' is hard to picture.
- “Walking the two sides in the other order gives the opposite change. So a loop needs only its tilt, and space has three tilts.”: The link to walking the loop the other way, and the step from nine orders to three tilts, are implicit.
- “The lean rule does the same for the arrows. ... swapping the two arrow directions flips the sign. So the arrows also need only a tilt”: The arrows' tilt is undefined, and the link to the lean rule is implicit.
- “Three have matching tilts, and the other six form three pairs.”: Three what? The subject is lost.
- “Back at the start, the ahead arrow's tip has moved 2 millimetres toward your left.”: Check starting state: facing which way at the end of the loop, and on what size of ball?
- “If the left arrow leaned away by less, the angle between them would shrink.”: The answer covers only one of the two alternatives.
- “so every entry is labelled by that one tilt twice, which gives 1 number.”: Reread: 'labelled twice' is unclear, and the zero entries are forgotten.
- “The two opposite crumbs drift the opposite way, and add the same again. So the crumbs drifted 6 hundredths of a millimetre more forward than backward”: Check answer skips why the far-side crumbs add rather than cancel, and the 6 is not shown as a sum.
- “They let go of four crumbs at rest, each 1 metre from the room's centre: out along A, out along B, and opposite each.”: A 39-word sentence with an ambiguous 'opposite each', and 'at rest' without saying relative to what.
- “To change which way an arrow points while you carry it.”: Contradicts the note: a carried arrow does come back pointing a different way without ever swinging.
- “Tape two equal arrows together at a right angle and turn the pair a little.”: Opening question does not say where the tape goes or where the pair lies, so the setting is unclear.
- “How many tilts are there, and how many numbers are left after the rule for walking a loop the other way and the lean rule?”: 'Numbers' here means different numbers; entries are numbers too.

**Fixes**

- Applied every rewrite recorded in the stumbles. Revision 1 to 2.
- Rule 17: the tides way held two ideas (no whirlpool, and the mirror rule with which entries record the drifts). The mirror rule and the on-trust statement that the two drift entries have each other's loop's and arrow's tilts now sit in the counting way, where the rule is used; the tides way ends at equal drifts and its Earth number, and its simplifies now speaks of the drifts balancing.
- Accuracy while simplifying: the lean rule is exact for a pair turning on a surface, but in space a finite turn about a slanted line makes the two leans differ at second order (rotation matrix R_BA + R_AB = 2(1 - cos theta) n_A n_B, checked by hand). The entry text now says 'exactly' only on the ground, and scopes the space case to the tiny loops the table records; 'exactly' was removed from the summary, takeaway, objective, glossary and misconception correction.
- Checked numbers with python3: a 2-millimetre lean on a 10-centimetre arrow slips back 0.020 millimetres; the check's ring sum is 10 minus 4 = 6 hundredths; near Earth GM/R^3 = 1.54e-6 per second squared gives at most 0.154 millimetres of drift in 10 seconds for a crumb 1 metre out, consistent with 'less than 2 tenths'.
- Glossary: swing now matches the prerequisite note's definition; tilt covers both the loop's tilt and the arrow's tilt; lean, lean rule, mirror rule and tidal drift reworded to match; added spacetime, which the first way's simplifies uses.
- Ladder: the working way 'The rules in components' now says its first pair is the arrow's tilt of the count and its last pair the loop's tilt; the gradiometer way names 'Tides without a whirlpool' instead of 'the entry way's energy argument'. Every non-entry way's first sentence already refers back to the way it continues, and the six ways use four kinds.
- Budget drops, to stay within 1,100 entry-explanation words: removed an Earth-area sentence I had added to the lean-rule way (810,000 square kilometres for a 1.15-degree turn); removed the lean-rule way's closing 'partners' paragraph, whose content the counting way now states; removed my added paragraph on why a slanted crumb's drift has a sideways part, keeping only 'differs in strength and in direction' as the reason; merged the counting way's surface sentences, since its takeaway and the surface check carry 'why one number describes a ball'. No sentence was compressed.
- Final re-read: split 'which is one pull' so the pronoun cannot point at the room's centre instead of its gravity.

**Concerns**

- The counting way now states two things on trust: which entries the crumb drifts sit in, and the general mirror rule. The physics reviewer should confirm the mapping (drift of the crumb along A toward B is -E_BA = -c^2 R_{B0A0}, first pair (B,0) = arrow's tilt time with B, last pair (A,0) = loop's tilt time with A) and judge whether stating it at entry is honest enough.
- Why a crumb's drift has a sideways part at all is backed only by 'gravity at a crumb differs in strength and in direction'. A tutor may need the slanted-crumb picture: out along a direction halfway between the planet line and level, apart-along plus together-across gives a slanted drift.
- The energy argument treats the extra pull as gravity at the crumb minus gravity at the room's centre, with the centre's pull the same all around the ring. This is right for the tidal (linear) approximation in a non-spinning room; the physics reviewer should confirm the wording 'gives back all it takes' for the uniform part.
- The lean-rule way's simplifies names spacetime and a sign flip along time that no entry way explains; it is scoped honestly but may prompt questions the entry rung cannot answer.
- Entry explanations are at the edge of the review allowance, so any further entry fix will need a drop elsewhere.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Retell after one reading: two cardboard arrows taped at a right angle, carried round a loop on a giant ball without letting them swing, come back turned as one piece, so a tip that moves two millimetres toward the other arrow is matched by the other tip moving two millimetres away; that is the lean rule, and the pinned pencil cross shows it. Then a room falling near a planet, four crumbs on a ring: going round the ring the A crumb's sideways drift counts forward and the B crumb's counts backward, the far-side crumbs repeat both, and if forward won the ring would whirl and a crumb would gain energy from nothing, which gravity near a planet whose gravity does not change with time never gives; so the two sideways drifts are equal, and near Earth the drift is under two tenths of a millimetre in ten seconds. Then the count: four choices among three directions give 81 entries, out-and-back loops give zero and the reversed loop gives the opposite change, so only the loop's tilt counts and there are three; the arrow works the same way, leaving nine; the mirror rule pairs six of them and three stand alone, leaving six numbers in space and one on a surface. Every entry takeaway came back. The one wobble was why an entry takes four choices rather than three.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Stumble, not fixed, for an editor. Quote: 'lay the pair flat on the ground' (checks/lean-of-the-second-arrow). Problem: the re-read deliberately dropped 'flat' from the same instruction in 'Two arrows at right angles' because 'flat' does double duty for a surface and for how an arrow lies, and beside 'a huge, smooth ball' it can read as 'a flat patch of ground'. The check kept it, so the two now differ. Rewrite: 'lay the pair on the ground'. Not applied because it is learner-visible and would push the note past the revision the physics stage signed, for one word; the identical change to the way's sentence was already accepted by the physics diff check, and tutoring words sit at 2773 of 3300, so the drop costs nothing.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Stumble, not fixed, for an editor. Quote: 'Filling one entry of the curvature table takes four choices of direction.' (ways_in/counting-what-the-table-holds). Problem: the table as defined in the first way's recap and in the glossary takes a loop's tilt and the arrow's starting direction, which is three directions; the fourth choice, the direction the lean is read in, is asserted with no step. This is the one place the retell wobbled. Rewrite: before 'The first two give the loop's sides', add 'The change is itself a direction the tip has moved in, so to get one number from it you read the lean toward one chosen direction.' Not applied because entry explanations already sit at 1100 words, the review ceiling, so it needs a drop elsewhere, and an editor should choose what goes.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Stumble, not fixed, for an editor. Quote: the recap of 'Counting what the table holds'. Problem: it restates the reversed loop, the loop's tilt, the lean rule and the equal drifts, but never what the curvature table is or what a lean is, although the way uses 'entry' and 'the direction its lean is read in'. Ways are retrieved one at a time, so a reader who meets this way first falls back on the glossary. Rewrite: add to the recap 'The curvature table, the Riemann curvature tensor, lists for each tilt of a tiny loop and each starting direction how a carried arrow comes back changed. A lean is how far a tip has moved toward a chosen direction.' Other way fields sit at 757 of 800, so about forty words fit without a drop.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Wording, minor. At entry this note says 'at each spot' for where the table sits and 'gravity at each place' for the same kind of location, and the prerequisite note riemann-curvature-tensor's glossary says 'A table kept at every place'. One word per idea would pick 'spot' or 'place' and use it in both notes.
- Second novice read, 2026-09-13 (the novice stage was re-run on the finished note; no learner-visible text changed, so the revision stays 4 and both stages still cover it). Ladder re-checked with no finding: each non-entry way's first sentence names the way it continues ('Counting what the table holds', 'Tides without a whirlpool', 'The rules in components'); index notation appears only at working, which the prerequisites reach through tensor components; the six ways use four kinds and no kind more than twice; and the three entry ways are genuinely different routes, a taped pair of arrows, a falling room of crumbs, and a count.

**Re-read** (2026-09-13, revision 4): 1 stumbles in 3 changed passages

- “A whirlpool would push a crumb, carried quickly once around the ring, forward more than backward.”: Step on trust: nothing in the way says why the lap must be quick. The reader was told gravity at each place stays the same, so speed seems not to matter; the real condition, that the room must not fall far during the lap, is never named.
- Fix: Tides way: replaced 'quickly' with the condition it stands for, 'before the room falls far', so the reader sees what the lap must beat (+4 words).
- Fix: Budget: entry explanations sat at 1098 of the 1100 review ceiling. To pay for the fix, dropped the connective 'Now' at the start of the tides way's ring paragraph, and dropped 'flat' from 'Lay the pair flat on the ground' in the lean way, which also removes 'flat' used for how an arrow lies (novice contract rule 5). Entry explanations stay at 1100.
- Fix: Read without stumble: the lean way's 'only by far less than the tips move' and 'that difference is too small to count' (reads once, and matches the counting way's 'too small to count'), and the misconception correction's 'For a tiny loop'.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 4)

**Verification**

- Four-term formula at a point with vanishing first metric derivatives: R_{ρσμν} = ½(∂σ∂μ g_ρν − ∂σ∂ν g_ρμ + ∂ρ∂ν g_σμ − ∂ρ∂μ g_σν), course sign.: python: random 4D Lorentzian metric η + ½A x x; Christoffels and Riemann by finite differences from the conventions row, lowered with η, compared term by term. → Agrees to 6e-8 on components of size 0.3. Correct sign and factor.
- Derivation steps 2–5: each swap flips the sign or permutes terms as described; step 4's rewritten terms are the old third, second, first, fourth terms with old signs.: Hand check of each term mapping. → Correct.
- Pair antisymmetries, pair exchange and cyclic identity hold for the Levi-Civita Riemann tensor.: Same random 4D metric, python. → All four relations hold to 1e-16.
- Metric-compatibility derivation: [∇μ,∇ν]T_ρσ = −R^λ_ρμν T_λσ − R^λ_σμν T_ρλ, giving first-pair antisymmetry.: Derived the covector commutator from [∇μ,∇ν]V^ρ = R^ρ_σμν V^σ. → Correct signs and index placement.
- Lowered small-loop change ΔV_ρ = −R_ρσμν V^σ a^μ b^ν; first pair = arrow's tilt (output ρ, carried σ), last pair = loop's tilt.: Lowered the conventions small-loop row; matched slot meanings. → Correct to leading order; the mapping in the working bridge sentence is right.
- Novice mapping: drift of the crumb out along A toward B is −c²R_{B0A0} ξ; its arrow's tilt is (B, time) and loop's tilt (A, time), and the partner entry swaps them.: Conventions geodesic deviation with u = c e_0 in an orthonormal free-fall frame: ξ̈^i = −c²R^i_{0j0}ξ^j. → Confirmed. The two entries R_{B0A0} and R_{A0B0} are mirror partners, so stating the mapping on trust at entry is honest.
- Lean rule: for a finite rotation R_BA + R_AB = 2(1−cosθ) n_A n_B; exact on the ground (axis normal to the pair's plane).: python: rotation matrices for axes (0,0,1), (1,1,1), (1,1,0) and angles 0.02, 1, π. → Formula confirmed. Counterexample to the entry sentence 'differ only by amounts far smaller than the leans themselves': axis (1,1,0), 0.02 rad gives both leans +0.0001 (both toward each other) with difference 0.0002, larger than the leans. The difference is always far smaller than the tips' movement (0.014). Fixed.
- Lean-way numbers: a 2 mm lean on a 10 cm arrow is a 1.15° turn; slip along the arrow 0.020 mm.: python → 1.146°, 0.0200 mm. Correct.
- Try it: a pinned plus-sign cross turned so one tip moves 2 mm toward the other pencil shows the other tip about 2 mm away.: Planar rigid rotation: both tips move L sinθ perpendicular to their pencils. → Correct, exactly.
- Tides way energy argument: a whirlpool of drifts means the extra-pull field has circulation; near a static planet the tidal field at one moment is a gradient ∂i(½Φ_jk ξ^j ξ^k).: Hand check; E_ij = ∂i∂jΦ symmetric. Checked the time dependence of the tidal field seen in the falling room. → Conclusion correct. 'Carried slowly once around the ring' was inaccurate: the room moves through the planet's field during a slow lap, so the extra pulls change and a slow lap need not close relative to the planet. Changed to 'quickly'.
- Ring circulation in the check: 2(d_BA − d_AB) = 2(0.05 − 0.02) = 0.06 mm forward.: python and sign trace around the four crumbs. → 0.060 mm. Correct; the reported 0.05 mm drift corresponds to an off-diagonal tidal entry 1e-6 per second squared, below Earth's maximum 2.3e-6, so the scenario is physically sized.
- Near Earth a crumb 1 m out drifts less than 2 tenths of a millimetre in 10 s.: python: ½(2GM/R³)(10 s)²(1 m), GM = 3.986e14, R = 6371 km. → 0.154 mm. Correct.
- Counts: 81 → 9 → 6 in space, 16 → 1 on a surface, 256 → 36 → 21 → 20 in spacetime; the cyclic identity adds one condition in four dimensions.: python: d⁴, m², m(m+1)/2, d²(d²−1)/12 with m = d(d−1)/2. → 2: 16,1,1,1; 3: 81,9,6,6; 4: 256,36,21,20. Correct.
- Sphere: R^θ_φθφ = sin²θ, R_θφθφ = a² sin²θ, K = 1/a², mixed partner R^φ_θθφ = −1.: python finite differences, a = 2, θ = 1. → 0.70807 vs sin²1 = 0.70807; 2.83229; K = 0.25000; R^φ_θθφ = −1.0000. Correct; worked example and mixed-index check confirmed.
- Problem whole-two-dimensional-table: dr² + sinh²r dφ² has R_rφrφ = −sinh²r and K = −1.: python at r = 0.7. → −0.57545 vs −0.57545; K = −1.0000. Correct.
- Check connection-without-a-metric: trace 3, R^x_xxy = 1, R^y_yxy = 2, R^x_yxy = x², R^y_xxy = 0, R_xy = 1, R_yx = −2, cyclic identity holds.: python finite differences at x = 0.37. → All values confirmed; R^x_yxy = 0.1369 = x². Reasoning that pair exchange with last-pair antisymmetry implies first-pair antisymmetry checked by hand.
- Problem pair-exchange-from-the-others: S_ρσμν − S_σμνρ − S_μνρσ + S_νρσμ = 2(R_ρσμν − R_μνρσ) using only the pair antisymmetries; ε has cyclic sum 3ε and obeys pair exchange.: python on a random tensor with both antisymmetries; hand check of each cancellation in step 3; permutation signs of ε. → Identity holds to 2e-15; cyclic ratio 3; ε pair exchange exact. Correct.
- Formal proposition (a)–(d), proof sketches, Ricci antisymmetry R_μν − R_νμ = R^λ_λμν for torsion-free non-metric connections, torsion spoils (b).: Hand derivation: cyclic sum of ∂Γ terms with symmetric Γ; derivation property on g(Z,W); contraction of the cyclic identity; first Bianchi identity with torsion. → Correct. (c) does not need zero torsion, as stated.
- Under g → −g, R^λ_σμν unchanged and R_ρσμν flips; in a Lorentzian orthonormal frame R^0̂_îμν = +R^î_0̂μν.: Γ invariant under g → −g; python on the random metric. → R^0_1 01 = R^1_0 01 = 0.04240. Correct.
- Structure: Rm a symmetric form on Λ² (dimension 6 in 4D, 21 entries), cyclic identity one more condition; bivector metric signature (3,3) in Lorentzian signature; constant sectional curvature gives k(gg − gg).: Standard linear algebra; sectional-curvature formula compared with the conventions row (sphere K = +1/a²). → Correct.
- Ricci symmetry from pair exchange (check ricci-with-torsion).: Hand contraction. → Correct.
- Gradiometer: holding force per unit mass f = Eξ + Ω×(Ω×ξ) + Ω̇×ξ, so M = E + ΩΩᵀ − Ω²1 + [Ω̇×], and M_xy − M_yx = −2Ω̇_z.: Rotating-frame equation of motion with the mass at rest; python with random Ω, Ω̇, ξ. → Formula agrees to 1e-16; antisymmetric entry −Ω̇_z confirmed.
- Check gradiometer-spin: Ω̇_z = −2.0e-8 rad s⁻², E_xy + Ω_xΩ_y = 1.0e-8 s⁻².: Hand arithmetic. → Correct, tolerances fine.
- Satellite at r = 6626 km: GM/r³ = 1.37e-6 s⁻², period 89.5 min, E = (GM/r³)diag(1,1,−2), diagonal of M = (0,1,−3)GM/r³; observation numbers −2.74e-6, +1.37e-6, −1.37e-6.: python with GM = 3.986004e14 m³ s⁻². → 1.3702e-6, 89.46 min, 2.740e-6. Correct; 6626 − 6371 = 255 km.
- GOCE flew 2009–2013 about 255 km up with three orthogonal accelerometer pairs; angular accelerations come from the antisymmetric part of the differential readings.: WebSearch record of Rummel, Yi and Stummer (2011) and mission facts. → Consistent: launched March 2009, science orbit near 255 km before later lowering, mission ended late 2013.
- Reference: E. B. Christoffel (1869), J. reine angew. Math. 70, 46–70, doi:10.1515/crll.1869.70.46.: WebSearch: De Gruyter and EUDML records. → Confirmed; verified. History claim is scoped to writing down the lowered four-index quantity, not a priority claim.
- Reference: R. Penrose (1960), A spinor approach to general relativity, Annals of Physics 10, 171–201.: WebSearch: ScienceDirect record. → Confirmed; added doi:10.1016/0003-4916(60)90021-X; verified.
- Reference: R. S. Hamilton (1986), Four-manifolds with positive curvature operator, J. Differential Geom. 24, 153–179.: WebSearch: Project Euclid record. → Confirmed; added doi:10.4310/jdg/1214440433; verified.
- Reference: C. Böhm, B. Wilking (2008), Manifolds with positive curvature operators are space forms, Ann. of Math. 167, 1079–1097.: WebSearch: arXiv and journal citation. → Confirmed; added arXiv:math/0606187 and doi:10.4007/annals.2008.167.1079; verified.
- Reference: Hehl, von der Heyde, Kerlick, Nester (1976), Rev. Mod. Phys. 48, 393–416, doi:10.1103/RevModPhys.48.393.: WebSearch: APS record. → Confirmed; verified.
- Reference: Hehl, McCrea, Mielke, Ne'eman (1995), Physics Reports 258, 1–171, arXiv:gr-qc/9402012.: WebSearch: arXiv and citation records. → Confirmed; added doi:10.1016/0370-1573(94)00111-F; verified.
- Reference: Rummel, Yi, Stummer (2011), GOCE gravitational gradiometry, J. Geodesy 85, 777–790.: WebSearch: Springer record. → Confirmed; added doi:10.1007/s00190-011-0500-0; verified.
- Research claims: Kerr is Petrov type D; Hamilton's 4D and Böhm–Wilking's all-dimension theorems; metric connection with torsion has 36 algebraically independent curvature components in 4D.: Standard results; 6×6 count of a form antisymmetric in each pair with no pair exchange. → Correct; 'with torsion alone' reworded to 'for a metric connection with torsion' so non-metricity is excluded.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Four-term formula at a point where the metric's first derivatives vanish: R_rho,sigma,mu,nu = 1/2 (d_sigma d_mu g_rho,nu - d_sigma d_nu g_rho,mu + d_rho d_nu g_sigma,mu - d_rho d_mu g_sigma,nu).: Re-derived from scratch from the conventions' Christoffel and Riemann rows: differentiated Gamma at the point (the g-inverse factor contributes nothing because dg = 0 there), then lowered with g_rho,kappa, and matched term by term against the note. → Identical term by term after commuting partial derivatives. Correct, and consistent with the course Riemann sign.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Derivation 'Reading the rules off the metric', steps 2-5: each swap either reverses every term or permutes the terms; step 5's 'old third, second, first and fourth terms with their old signs'.: Independent hand mapping of all four terms under rho<->sigma, mu<->nu and the pair trade. → All three mappings reproduce exactly what the steps say, including the third/second/first/fourth order in step 5.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Derivation 'Metric compatibility forces first-pair antisymmetry': [nabla_mu, nabla_nu] T_rho,sigma = -R^lambda_rho,mu,nu T_lambda,sigma - R^lambda_sigma,mu,nu T_rho,lambda, giving R_rho,sigma,mu,nu = -R_sigma,rho,mu,nu.: Derived the covector commutator from the conventions' [nabla_mu, nabla_nu] V^rho = R^rho_sigma,mu,nu V^sigma, then set T = g. → Signs and index placement correct. Noted that step 1 assumes zero torsion while the result line and the formal-rung key equation allow torsion; see concerns.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Lowered small-loop change Delta V_rho = -R_rho,sigma,mu,nu V^sigma a^mu b^nu, first pair = arrow's tilt, last pair = loop's tilt.: Lowered the conventions' small-loop holonomy row and matched each slot to the entry-rung words. → Matches the conventions exactly; the slot-to-word map in the working way is right.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Lean rule on the ground is exact; in space the departure is second order in the turn angle. Entry sentence 'the two leans can differ, but only by far less than the tips move'.: python: Rodrigues rotation matrices for axes normal to the pair, along one arrow, at 45 degrees in the pair's plane, and slanted (1,2,3), at angles 0.02, 0.1 and 0.5 rad, on 10 cm arrows. Compared lean1 = L(Re1).e2, lean2 = L(Re2).e1 and the tip displacement 2L sin(theta/2). → Normal axis: lean1 + lean2 = 0 to machine precision at every angle, so 'exactly' on the ground is right. Other axes: lean1 + lean2 = 2L(1-cos theta) n_A n_B, i.e. 0.020 mm against a 2.00 mm tip move at 0.02 rad (1 percent), 0.14 mm against 10.0 mm at 0.1 rad. Second order, so 'far less than the tips move' holds for every small turn.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Try it: a pinned plus-sign pencil cross turned until one tip is 2 mm from its mark toward the other pencil shows the other tip about 2 mm from its mark, away.: python: planar rigid rotation, 9 cm tip radius, theta = 0.0222 rad. → Second tip lean 1.9998 mm, displacement 2.0000 mm. 'About 2 millimetres' correct.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Tides way: near Earth a crumb 1 m out drifts less than 2 tenths of a millimetre in 10 s.: python: 1/2 (2GM/R^3)(1 m)(10 s)^2 with GM = 3.986004418e14 m^3/s^2, R = 6371 km; also checked the transverse direction and a low orbit. → 0.154 mm radial (largest case), 0.077 mm transverse, 0.137 mm at 6626 km. The bound holds everywhere outside Earth, so the 'less than' sentence is safe.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). No-whirlpool argument: zero circulation of the extra-pull field round the ring forces the two sideways drifts to be equal, and that is exactly the symmetry of the tidal matrix.: Hand computation of the circulation of a_i = -E_ij xi^j round a circle of radius r: it equals -pi r^2 (E_12 - E_21), and the four-crumb sum equals 2r(E_AB - E_BA). Checked that subtracting the uniform field g(centre) leaves a gradient field, so the roller-coaster step is sound. → Both vanish precisely when E is symmetric. The entry conclusion 'the crumb out along A drifts toward B just as far as the crumb out along B drifts toward A' is the correct consequence.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Check four-crumbs-and-a-whirlpool: the reported drifts give 0.06 mm net forward round the ring.: Sign trace at all four crumbs: forward drifts 5 + 5 hundredths, backward 2 + 2 hundredths. → 0.06 mm. Correct, and the signed direction (from A toward B) matches the numeric field.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Counts: 81 -> 9 -> 6 in space, 16 -> 1 on a surface, 256 -> 36 -> 21 -> 20 in spacetime; n^2(n^2-1)/12 in the leads_to reason.: python: d^4, m = d(d-1)/2, m^2, m(m+1)/2, and d^2(d^2-1)/12 for d = 2, 3, 4. → 1, 6, 20 from the closed formula; 21 before the cyclic identity in four dimensions and 6 in three, so the identity removes nothing below four dimensions. All counts in the note, its checks and its problem are right.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Sphere of radius a: R^theta_phi,theta,phi = sin^2 theta, R_theta,phi,theta,phi = a^2 sin^2 theta, det g = a^4 sin^2 theta, K = 1/a^2, and the mixed partner R^phi_theta,theta,phi = -1.: Hand algebra from R_rho,sigma,mu,nu = K(g_rho,mu g_sigma,nu - g_rho,nu g_sigma,mu) with K = 1/a^2, then lowering and raising with g_theta,theta = a^2 and g^phi,phi = 1/(a^2 sin^2 theta). → All four values confirmed, including the worked example's 'four nonzero components, plus or minus a^2 sin^2 theta' and the 12 vanishing slots. The sphere comes out with positive K, as the conventions require.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Problem 'The whole two-dimensional table': dr^2 + sinh^2 r dphi^2 with R_r,phi,r,phi = -sinh^2 r has K = -1.: det g = sinh^2 r, K = R_1212/det g; cross-checked with K = -f''/f for dr^2 + f(r)^2 dphi^2, f = sinh r. → K = -1 both ways. The hyperbolic plane, so the sign convention carries to negative curvature.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Check 'connection-without-a-metric': trace 3, R^x_x,x,y = 1, R^y_y,x,y = 2, R^x_y,x,y = x^2, R^y_x,x,y = 0, R_xy = 1, R_yx = -2, cyclic identity holds, torsion vanishes.: python: exact polynomial-in-x evaluation of the full four-term Riemann formula (derivative and Gamma-Gamma terms) for every index quadruple, plus the traces and the cyclic sum over all 16 quadruples. → Every value in the answer confirmed exactly; cyclic sum zero for all quadruples; R_xy - R_yx = 3 = R^lambda_lambda,x,y. The 'trace of a commutator' step is right: the Gamma-Gamma terms contract to tr(Gamma_mu Gamma_nu) - tr(Gamma_nu Gamma_mu) = 0, so the trace formula is exact and not only valid at a point.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Problem 'Pair exchange from the others': S_rho,sigma,mu,nu - S_sigma,mu,nu,rho - S_mu,nu,rho,sigma + S_nu,rho,sigma,mu = 2(R_rho,sigma,mu,nu - R_mu,nu,rho,sigma) using only the two pair antisymmetries.: python: random 4D tensor built with both pair antisymmetries and no cyclic identity imposed; identity tested on all 256 index quadruples. Also checked the solution's twelve-term list and each of its four stated cancellations by hand. → Zero mismatches. All four cancellation identities in the solution are correct, and the four survivors give exactly 2R_rho,sigma,mu,nu - 2R_mu,nu,rho,sigma.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). The converse fails: the totally antisymmetric symbol in four dimensions obeys both pair antisymmetries and pair exchange but has cyclic sum 3 epsilon.: python over all 256 quadruples. → Pair exchange holds for every quadruple; the cyclic sum equals 3 epsilon for every quadruple. Correct counterexample.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Formal way's limits: for a torsion-free connection with no metric, R^lambda_lambda,mu,nu = d_mu Gamma^lambda_nu,lambda - d_nu Gamma^lambda_mu,lambda and R_mu,nu - R_nu,mu = R^lambda_lambda,mu,nu.: Contracted the four-term Riemann formula (the Gamma-Gamma terms cancel identically) and derived the Ricci antisymmetry from the cyclic identity; cross-checked numerically on the plane connection above. → Both exact, with the sign as written (+R^lambda_lambda,mu,nu, not minus).
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Lorentzian orthonormal frame: R^0hat_ihat,mu,nu = +R^ihat_0hat,mu,nu; and under g -> -g, R^lambda_sigma,mu,nu is unchanged while every R_rho,sigma,mu,nu flips.: Raised with eta^00 = -1 and eta^ii = +1; and checked that Gamma is invariant under an overall metric rescaling by -1. → Both correct, and the notation trap 'lowered-components-under-sign-flip' follows.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Structure: Rm is a symmetric form on bivectors of dimension n(n-1)/2, 21 entries in four dimensions, one more condition from the cyclic identity; the induced bivector metric has Lorentzian signature (3,3).: Computed G(e_a ^ e_b, e_c ^ e_d) = g_ac g_bd - g_ad g_bc on the six basis bivectors of Minkowski space: the three e_0 ^ e_i give -1 and the three e_i ^ e_j give +1. → (3,3) confirmed; the rest is standard linear algebra and correct. The sectional-curvature formula matches the conventions' row, including the sphere's K = +1/a^2.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Gradiometer matrix M = E + Omega Omega^T - Omega^2 I + [Omega-dot x], with M_xy - M_yx = -2 Omega-dot_z.: Re-derived the holding force per unit mass in a freely falling frame turning at Omega: f = E xi + Omega x (Omega x xi) + Omega-dot x xi, expanded the double cross product, and read the xy and yx entries of epsilon_i,j,k Omega-dot_j. → Matrix and the -2 Omega-dot_z sign both confirmed. E_ij = c^2 R_ihat,0hat,jhat,0hat follows from the conventions' geodesic-deviation row with u = c e_0hat, and E_ij = d_i d_j Phi in a weak static field, with the sign that matches xi-double-dot = -E xi.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Satellite numbers: r = 6626 km, GM/r^3 = 1.37e-6 s^-2, period 89.5 min, Omega^2 = GM/r^3, E = (GM/r^3) diag(1,1,-2), diagonal of M = (0,1,-3) GM/r^3; observation values -2.74e-6, +1.37e-6 and -1.37e-6 s^-2.: python with GM = 3.986004418e14 m^3/s^2; Kepler period 2 pi sqrt(r^3/GM). → 1.3702e-6 s^-2, 5367.7 s = 89.46 min, Omega^2 = 1.3702e-6 s^-2 exactly equal to GM/r^3, diagonal (0, 1, -3). Every number correct to the quoted precision, including 6371 + 255 = 6626 km.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Check 'gradiometer-spin': Omega-dot_z = -2.0e-8 rad/s^2 and E_xy + Omega_x Omega_y = 1.0e-8 s^-2.: python: symmetric and antisymmetric parts of the two readings. → Both confirmed; the sign of Omega-dot_z follows from the xy entry being -Omega-dot_z. Tolerances of 0.05 on values of 2.0 and 1.0 are appropriate.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). All seven references: Christoffel 1869, Penrose 1960, Hamilton 1986, Boehm-Wilking 2008, Hehl et al. 1976, Hehl et al. 1995, Rummel et al. 2011.: WebSearch again this round against publisher records (De Gruyter, EUDML, ScienceDirect, Project Euclid, arXiv, APS, Springer). → All authors, years, titles, venues, volumes, page ranges, DOIs and arXiv ids confirmed unchanged; verified stays true for all seven. GOCE mission facts (launched March 2009, re-entered November 2013, about 255 km, three orthogonal accelerometer pairs) also confirmed.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Research-horizon claims: Kerr is Petrov type D; Hamilton's four-dimensional and Boehm-Wilking's all-dimension space-form theorems; a metric connection with torsion has 36 independent curvature components in four dimensions.: Standard results, plus the 6x6 count for a form antisymmetric in each pair with no pair exchange and no cyclic identity. → All correct. 'Quotient of the round sphere' is the right scope for Hamilton's 1986 conclusion (S^4 or RP^4).
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Symbol E for the tidal matrix, with xi-double-dot = -E xi, agrees with the rest of the vault.: Grep across knowledge/concepts/curvature for the tidal matrix definition. → Sibling notes use E_ij = c^2 R_ihat,0hat,jhat,0hat with hats dropped on E, the same as this note. Consistent, though the conventions file still fixes no symbol; see concerns.

**Counterexamples tried**

- Rotation about an axis in the pair's own plane (in space): both arrows lean toward each other by (1−cosθ)/2 each, so a finite loop in space can produce exactly the 'both lean together' pattern. Broke 'differ only by amounts far smaller than the leans themselves'. Rewritten as 'only by far less than the tips move', which holds for every small turn; the table's first-order record is unaffected.
- Large loop in space, same axis: leans can be of full arrow length and equal in sign. The summary, takeaway, objective and glossary all say 'tiny loop', so they survive; the misconception correction lacked that scope and now says 'For a tiny loop'.
- Turn on the ground (axis along the surface normal): leans are exactly equal and opposite for any loop size. Statement 'exactly' on the ground survives.
- Spacetime (boost-like change): lean along time counts with the opposite sign, R^0_i = +R^i_0. Covered by the lean way's simplifies.
- Non-static field (binary stars): energy argument fails, but E_ij stays symmetric by pair exchange. Covered by the tides way's simplifies.
- Slow lap in the falling room: the tidal field seen in the room changes as the room falls, so the no-circulation argument needs a lap that is quick compared with that change. Fixed 'slowly' to 'quickly'.
- Spinning room: centrifugal and Coriolis effects would add apparent drifts; the tides way and its check both require that the room does not spin. Survives.
- Mixed-index tensor on the sphere: R^φ_θθφ = −1, not −sin²θ. Working way and misconception state it correctly.
- Connection with no metric (check connection-without-a-metric) and metric connection with torsion: first-pair antisymmetry, respectively pair exchange, fail. Formal way scopes every rule by its assumption.
- Totally antisymmetric ε in 4D: obeys both antisymmetries and pair exchange but not the cyclic identity, so pair exchange does not imply it. Stated in the formal way and problem.
- Two dimensions and three dimensions: the cyclic identity adds nothing (counts 1 and 6); only in four dimensions does it remove one number. Entry counts are for surface and space, so 'three rules' suffice there; the spacetime count names the fourth rule.
- Hyperbolic plane (dr² + sinh²r dφ²): K = −1 with the two-dimensional form, confirming the sign convention works for negative curvature.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Turn about an axis lying in the pair's own plane at 45 degrees (in space): both tips lean TOWARD each other by L(1-cos theta)/2, so their magnitudes are identical and only the toward/away pattern of the lean rule breaks. Checked whether the entry sentence 'the two leans can differ' misdescribes this. It does not: the paragraph defines the rule as one arrow leaning toward as far as the other leans away, so 'the two leans' are the lean-toward and the lean-away, and their difference is lean1 + lean2 = 2L(1-cos theta) n_A n_B. At 0.02 rad that is 0.020 mm against a 2.00 mm tip move. The sentence survives, but see concerns.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Turn about an axis along one of the arrows: both leans are exactly zero at every angle, so the lean rule holds trivially and no sentence is stressed.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Turn about the surface normal (the on-the-ground case), at angles up to 2 radians: the off-diagonal entries are exactly sin theta and -sin theta, so the word 'exactly' in 'on the ground one arrow leans toward the other exactly as far as the other leans away' is right for loops of any size, not only tiny ones.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Spinning room, and a room falling far during the lap: both are excluded in words by the tides way ('the room does not spin', 'before the room falls far'). Without them the sideways drifts need not balance.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Non-static source (two circling stars): the energy argument fails, but the tidal matrix stays symmetric by pair exchange. Covered by that way's simplifies.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Spacetime with a boost-like change: the lean along time counts with the opposite sign. Covered by the lean way's simplifies.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Two and three dimensions: the cyclic identity is vacuous (counts 1 and 6 come out of the three pair rules alone), so the entry ways' 'three rules' is exactly right and only the spacetime simplifies needs a fourth.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Torsion-free connection preserving no metric (the plane connection in the formal check): Ricci is not symmetric, R_xy = 1 and R_yx = -2, and no metric can have it as Levi-Civita connection. Isolates first-pair antisymmetry as the rule that needs a metric.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Metric connection with torsion: keeps both pair antisymmetries, loses pair exchange and Ricci symmetry, 36 components in four dimensions. Isolates the cyclic identity as the rule that needs zero torsion.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Totally antisymmetric symbol in four dimensions: both antisymmetries and pair exchange without the cyclic identity, so pair exchange is strictly weaker. Confirmed over all 256 components.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Hyperbolic plane dr^2 + sinh^2 r dphi^2: K = -1 from the same two-dimensional form, so the sign convention is not tuned to positive curvature.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Overall metric sign flip g -> -g: every lowered component flips while the mixed tensor does not, and all four relations survive. Matches the notation trap.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Null (degenerate) two-planes in Lorentzian signature: sectional curvature is undefined there. The formal way says its values 'on nondegenerate planes' fix Rm before the constant-curvature sentence, so the scope is carried.

**Fixes**

- Lean-rule way (entry): 'only by amounts far smaller than the leans themselves ... those amounts are too small to count' became 'only by far less than the tips move ... that difference is too small to count'. Net one word fewer, so entry explanations stay within the review allowance.
- Tides way (entry): 'carried slowly once around the ring' became 'carried quickly once around the ring', because the tidal field in a falling room changes during a slow lap.
- Misconception both-arrows-lean-together: correction scoped with 'For a tiny loop'.
- Research horizon torsion-and-nonmetricity: 'With torsion alone' became 'For a metric connection with torsion'.
- Visual sketch tips-of-a-turning-cross: tipping control limited to small angles, with a note that a large tip about an in-plane axis makes both tips lean toward each other, so the demo must present the second-order difference honestly.
- References: all seven confirmed and set verified; added DOIs for Penrose, Hamilton, Böhm–Wilking, Hehl et al. 1995 and Rummel et al., and arXiv:math/0606187 for Böhm–Wilking.
- Revision 2 to 3; status physics-reviewed.
- Second physics review, 2026-09-13: no fixes. Every equation, derivation step, number, count, check answer, problem answer, analogy relation and reference was re-derived or recomputed independently and came out as written. note_diff.py reports 0 learner-visible strings changed, so the note stays at revision 4 and both review stages still cover the current revision.

**Concerns**

- Changed entry text for the novice re-read: the lean-rule way's space paragraph and the tides way's 'quickly'. A reader may ask why the lap must be quick; the entry prose gives no reason, and the entry budget (about 1,098 of 1,100) leaves no room for one. A tutor can say the room falls to where gravity differs, so the extra pulls change during a slow lap.
- The counting way states on trust both which entries hold the crumb drifts and the general mirror rule. This is accurate (the drifts are E_BA = c²R_{B0A0} and E_AB = c²R_{A0B0}), but it is a second thing taken on trust in one way.
- Registry prerequisites differ from the note for riemann-curvature-tensor and covariance-of-tensor-equations; sync_registry.py should apply them.
- Proposed visuals tips-of-a-turning-cross, falling-ring-of-crumbs and twenty-of-256-slots are not yet in the catalog.
- The Christoffel entry does not mention Riemann's 1861 Paris essay, which contains the same quantity but was published only in 1876; the history claim does not assert priority, so it is not wrong.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). STAGE RE-RUN, NOT A FIRST REVIEW. The note was already at status 'physics-reviewed', revision 4, with review.novice and review.physics both covering revision 4, and with a physics diff check that changed nothing. The writer stage and the novice stage before me were both blocked for the same reason. I re-read the whole note and redid the physics independently rather than trusting the earlier record; this entry and the verification and counterexample items tagged with this date are that second pass. Verdict for this pass alone is 'accurate' (0 errors found, 0 learner-visible strings changed); the stage-level verdict stays 'fixed' because the first pass did fix things.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). For an editor, the one sentence worth a future word-neutral tightening: 'Then the two leans can differ, but only by far less than the tips move' (ways_in/two-arrows-at-right-angles). It is accurate on the reading the paragraph forces, where 'the two leans' are the lean-toward of one arrow and the lean-away of the other. Read instead as two lean-toward magnitudes it would understate the worst case, a turn about an axis at 45 degrees in the pair's plane, where the magnitudes are identical (L(1-cos theta)/2 each) yet the rule fails by their sum. Not changed, for two reasons: the context settles the reading, and entry explanations sit at 1100 words, exactly the review ceiling, so any added word needs a drop elsewhere. A word-neutral option an editor could take is 'Then the lean rule can miss, but only by far less than the tips move', with 'that difference' becoming 'that miss' in the next sentence.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). The novice stage's three unapplied rewrites were checked for accuracy and all three are physically sound: dropping 'flat' from 'lay the pair flat on the ground' in checks/lean-of-the-second-arrow changes no claim (the physics diff check already accepted the identical change to the way's sentence); the proposed bridge 'the change is itself a direction the tip has moved in, so to get one number from it you read the lean toward one chosen direction' correctly states why an entry takes a fourth choice of direction; and a recap that restates the curvature table and the lean would repeat the glossary, not add a claim.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Conventions gap, reportable: knowledge/notation/course-conventions.md still fixes no symbol or sign for the tidal matrix. This note uses E_ij = c^2 R_ihat,0hat,jhat,0hat with xi-double-dot = -E xi, which follows from the conventions' geodesic-deviation row and matches the sibling curvature notes; the hats are dropped on E, as elsewhere in the vault, although the frame indices it is built from carry them.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). key_equations/skew-curvature states conditions 'nabla g = 0; torsion is allowed', but its justified_by points at derivations/metric-compatibility-forces-first-pair-antisymmetry, whose first step assumes a torsion-free connection. The claim itself is right, and the formal way's part (c) gives the torsion-allowed coordinate-free proof; only the pointer is narrower than the claim. Left alone because fixing it means either re-scoping a working-rung derivation or pointing justified_by at a way.
- Second physics review, 2026-09-13 (stage re-run on the finished note; independent re-derivation of every equation and recomputation of every number). Inherited and unchanged: the three cited visuals (tips-of-a-turning-cross, falling-ring-of-crumbs, twenty-of-256-slots) are still proposals rather than catalog entries; registry prerequisites differ from the note for covariance-of-tensor-equations and riemann-curvature-tensor, which sync_registry.py should apply; and the note is eligible for status 'published' on an editor's call.

**Diff check** (2026-09-13, revision 4)

- Tides way: 'carried once around the ring before the room falls far' claims the same condition as 'carried quickly once around the ring': the lap must end before the room has moved to where the planet's gravity, and so the extra pulls, differ appreciably.: Newtonian tidal field in a freely falling, non-rotating room: extra pull a_i = -(d_i d_j Phi) x^j is a gradient at each instant, so its work around a closed loop vanishes only while the field is effectively constant during the lap. Estimated how far and how long the room must fall for a 1% change (tidal field goes as 1/r^3) near Earth with python, and tried a radially falling room, an orbiting room, a slow lap and a spinning room as what-ifs. → Equivalent and true. A 1% change needs a fall of about 21 km (about 65 s from rest, about 3 s at orbital speed); after the way's 10 s from rest the change is about 2e-4, so a lap finished before the room falls far keeps the extra pulls fixed. 'Falls' covers any free-fall path, including an orbit, since the way sets the room falling freely. A slow lap during which the room falls far is exactly the case excluded, as before. Spinning is still excluded by 'the room does not spin'. Consistent with the earlier sentence that gravity at each place stays the same, which is what makes position, not time, the thing that matters.
- Lean way: 'Lay the pair on the ground' (was 'Lay the pair flat on the ground') still places both arrows along the surface.: Read in context: 'lay ... on the ground' means lying along the surface; later sentences 'on the ground one arrow leans toward the other exactly as far as the other leans away' and 'In space, a tiny loop can turn the pair about any line' rely on the pair lying in the surface. → Same claim; the exact lean rule on the ground (turn about the surface normal) is unaffected.
- Dropping 'Now' at the start of the tides way's ring paragraph.: Read in context. → No change in meaning.
- Fix: None; both changed entry strings are accurate. No learner-visible text changed, revision stays 4.
