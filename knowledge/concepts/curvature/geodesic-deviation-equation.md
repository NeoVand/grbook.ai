---
type: "concept"
schema_version: 2
id: "geodesic-deviation-equation"
title: "Geodesic deviation equation"
tagline: "The rule linking curving to how neighbouring straight paths draw together or spread apart"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["geodesic deviation", "Jacobi equation", "equation of geodesic deviation"]
prerequisites: ["deviation-vector", "riemann-curvature-tensor", "ricci-identity", "geodesic-equation", "ricci-tensor"]
leads_to: ["relativistic-tidal-tensor", "schwarzschild-tidal-field", "geodesic-deviation-in-gravitational-wave", "tidal-derivation-of-vacuum-field-equations", "ricci-focusing-versus-weyl-shear", "conjugate-point"]
visuals: ["two-walkers-set-off-side-by-side", "falling-ring-of-crumbs"]
---

# Geodesic deviation equation

*The rule linking curving to how neighbouring straight paths draw together or spread apart*

`geodesic-deviation-equation` · curvature · core · physics-reviewed (revision 5)

**Needs:** [[deviation-vector]] (entry) · [[riemann-curvature-tensor]] (entry) · [[ricci-identity]] (working) · [[geodesic-equation]] (working) · [[ricci-tensor]] (formal)  
**Opens:** [[relativistic-tidal-tensor]] · [[schwarzschild-tidal-field]] · [[geodesic-deviation-in-gravitational-wave]] · [[tidal-derivation-of-vacuum-field-equations]] · [[ricci-focusing-versus-weyl-shear]] · [[conjugate-point]]  
**Related:** [[newtonian-deviation-equation]] · [[tidal-force]] · [[holonomy]] · [[raychaudhuri-equation]]  
**Visuals:** ★ [[two-walkers-set-off-side-by-side]] · [[falling-ring-of-crumbs]]

> Two close neighbours who walk straight, or fall freely, can draw together or spread apart. On a ball, walkers who set off side by side draw together slowly at first, then faster and faster, until they meet. The geodesic deviation equation is the rule for how that drawing together, or spreading apart, speeds up or slows down. That speeding up, or slowing down, is in proportion to the distance between the neighbours. The curving of the ground, or of spacetime, sets the proportion.

## You will be able to

**Entry**
- Predict the next length of the string between straight walkers on a ball, using the rule for the extra shrinking. `objectives/predict-the-next-stretch` ← `checks/next-stretch-on-the-ball`, `problems/past-the-pole`
- Predict how the shrinking between two falling crumbs changes when they start farther apart. `objectives/scale-with-distance` ← `checks/three-metres-apart`
- Explain why one freely falling object cannot show the curving of spacetime, but two can. `objectives/explain-two-objects-needed` ← `checks/scales-cannot-tell`

**Working**
- Explain why Christoffel symbols vanishing along one worldline do not remove a neighbour's relative acceleration. `objectives/explain-free-fall-keeps-relative-acceleration` ← `checks/christoffels-vanish-along-one-worldline`
- Compute relative accelerations of free test masses from frame components of the Riemann tensor. `objectives/compute-with-frame-form` ← `checks/free-mirrors-in-a-wave`
- Solve the equation on a sphere and derive the exact rule for equal finite steps. `objectives/solve-on-a-sphere` ← `problems/stretch-rule-is-exact`

**Formal**
- Relate the sign of relative acceleration to the sectional curvature of the plane of four-velocity and separation. `objectives/relate-sign-to-sectional-curvature` ← `checks/timelike-plane-sign`
- State when the equation is exact and when it fails for two real neighbours. `objectives/state-exactness-and-limits` ← `checks/exact-or-first-order`
- Compute how free neighbours separate at constant curvature, and relate it to a cosmological constant. `objectives/compute-constant-curvature-spreading` ← `problems/de-sitter-spreading`

## Ways in

### 1. Walkers on a ball draw together faster and faster · entry · picture

*When two straight walkers set off side by side on a ball, how does the string between them change, stretch by stretch?*

**Recap:** Walking straight means walking without ever steering left or right. Two friends walk straight, taking equal steps and counting them. An elastic string joins them at matching counts. If they start side by side, neither ahead, the string's length is the distance between their paths. On a ball, take friends who leave the equator side by side, facing the North Pole. At matching counts they stand on the same circle around the ball, one of the circles printed on a globe parallel to the equator. The string always covers the same fraction of that circle as it did of the equator. Those circles get shorter toward the North Pole, so the friends draw together.

Two friends stand on the equator of a huge smooth ball the size of Earth, 100 metres apart. They face the North Pole, side by side, and both walk straight. An elastic string joins them at matching step counts.

Split the walk to the North Pole into six equal stretches, each about 1,670 kilometres long. At matching counts the friends stand on the same circle around the ball, one of the circles printed on a globe parallel to the equator. The string always covers the same fraction of that circle as it did of the equator. Those circles get shorter toward the North Pole, so the string does too.

At the ends of the first three stretches the string is 96.6 metres, then 86.6, then 70.7. You can check the third length with a thread on a globe: halfway to the North Pole, the circle is about 7 tenths as long as the equator.

Now subtract. The first stretch shrinks the string by 3.4 metres. The second shrinks it by 10.0 metres, and the third by 15.9 metres. So the shrinking speeds up: each stretch shrinks the string more than the stretch before.

How much more? The second stretch shrinks it 6.6 metres more than the first. At the end of the first stretch, the string is 96.6 metres long, and 6.6 is about 7 hundredths of 96.6. The third stretch shrinks it 5.9 metres more than the second. At the end of the second stretch, the string is 86.6 metres long, and 5.9 is again about 7 hundredths of 86.6.

This amount, how much more one stretch shrinks the string than the stretch before, is called the extra shrinking. On this walk, the extra shrinking is always the same share of the string's length at the end of the earlier stretch. A string twice as long, between friends 200 metres apart, therefore shrinks twice as much in every stretch.

At the moment the friends set off side by side, the string is not shrinking at all. By the end of the first stretch it is shrinking at about one full extra per stretch. So across that first stretch the shrinking averages half of one extra: half of 7 hundredths of 100 metres is about 3.4 metres. After that, each stretch adds a full extra.

The share, 7 hundredths here, is set by how curved the ground is and by how long the stretches are. Cut the same walk into twelve stretches, half as long, and the share drops to about a quarter, near 1.7 hundredths. On a smaller ball, with stretches of the same length, the share is bigger. On flat ground the share is zero, so friends who start side by side keep their distance. On a saddle, which curves the opposite way, the string grows instead, faster and faster.

This rule, for close neighbours, is called the geodesic deviation equation. In words: the extra shrinking, or extra growing, is in proportion to the string's length, and the curving sets the proportion.

You never notice this drawing together on Earth's ground. Two friends 100 metres apart who set off side by side and walk straight for one kilometre draw together by only about one thousandth of a millimetre.

**Try it:** Take an orange about 25 centimetres around. Put two rubber bands around it so that they cross at two opposite points, like the two poles of a globe. Around the orange's middle, halfway between the crossings, the bands should be 2 centimetres apart. A tight band takes the shortest way over the peel, like a straight walk. Mark one band at the middle, then at three more points toward one crossing, each 1.5 centimetres farther along the band. At each mark, lay a strip of paper over the peel to the other band, at a right angle to the marked band, and mark the gap on the strip. The gaps come out near 20, 19, 15 and 9 millimetres. So the gap shrinks by only about 1 millimetre between the first two marks, and by more between each later pair.

**Takeaway:** On a ball, the string between straight walkers who start side by side shrinks faster and faster until they meet, and each extra shrinking is in proportion to the string's length.

*What this leaves out:* Treats the ball as perfectly smooth, keeps the friends close together compared with its size, and rounds the lengths to a tenth of a metre.

*Builds on:* [[deviation-vector]], [[curvature]]<br>*Visuals:* [[two-walkers-set-off-side-by-side]]<br>*See:* `checks/next-stretch-on-the-ball`

### 2. Two crumbs read the curving of spacetime · entry · operational

*How can someone inside a freely falling cabin measure the curving of spacetime?*

**Recap:** Moving with nothing but gravity acting is called falling freely. Space and time taken together form spacetime, a world with four directions: three of space and one of time. The path of a freely falling object through spacetime counts as a straight walk, which we take on trust here. The Riemann curvature tensor is a table of numbers, kept at every place, that describes the curving there. Each entry belongs to a pair of directions, and falling objects can measure the entries whose pair includes time. On a ball, straight walkers who start side by side draw together faster and faster. Each stretch's extra shrinking, over the stretch before, is in proportion to the string's length.

The walkers in "Walkers on a ball draw together faster and faster" needed a ball. This way needs only a cabin.

Picture a cabin falling freely inside a tall hollow tower on Earth, with the air pumped out of the tower. You float inside the cabin, with your feet touching bathroom scales. Gravity makes you and the scales fall alike, so nothing presses you onto them, and the scales read zero. Far out in space, away from every star and planet, they would read zero too. So the scales cannot tell you whether Earth is nearby.

Now hold two crumbs one metre apart, both the same distance from Earth's centre. The line between them then runs at a right angle across the line toward Earth's centre. Let go of both at once, with no push. Imagine an elastic string between them.

Seen from the tower's wall, each crumb falls toward Earth's centre, as the cabin does. The two paths point at that one centre, like two spokes of a wheel, so they lean slightly toward each other. Inside the cabin, the crumbs draw together, and the string shrinks.

Time the shrinking with a clock on the cabin wall, and measure it with a ruler fixed to the cabin. In the first second the string shrinks by 0.77 thousandths of a millimetre. In the next second it shrinks by 2.31 thousandths, and in the third by 3.85 thousandths. So each second shrinks the string by the same extra, 1.54 thousandths of a millimetre, more than the second before.

This is the walkers' rule again, with seconds in place of stretches. The first second gets half of the extra, just as the first stretch did, because the crumbs start with no drawing together.

Start the crumbs 2 metres apart instead. Their two spokes then lean toward each other twice as much, so the extra doubles to 3.08 thousandths of a millimetre. The extra shrinking is in proportion to the string's length, as the geodesic deviation equation says.

So divide the extra by the string's length. For any short string placed this way near Earth's surface, you get the same number: an extra of 1.54 thousandths of a millimetre each second, for each metre of string. That number gives one entry of the Riemann curvature tensor, the entry for time paired with that sideways direction. You measured that entry without looking outside.

Other directions give other entries. Two crumbs placed along the line toward Earth's centre spread apart instead, because the crumb nearer the centre is pulled a little harder. Their extra growing is twice as big.

In daily life this is far too small to see. After three seconds, a one-metre string has shrunk by only about 7 thousandths of a millimetre, a tenth of a hair's width.

**Takeaway:** In a falling cabin near Earth, crumbs let go side by side draw together faster and faster, with an extra shrinking each second in proportion to their distance apart. That extra, divided by the distance, gives a Riemann tensor entry.

*What this leaves out:* Treats Earth as a perfect ball that does not spin, and ignores the pull of the tower, of nearby hills, and of the crumbs on each other. The fall lasts only a few seconds, so the numbers do not change during it.

*Continues:* `ways_in/faster-and-faster-on-a-ball`<br>*Builds on:* [[riemann-curvature-tensor]], [[free-fall]], [[spacetime]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/scales-cannot-tell`, `checks/three-metres-apart`

### 3. Swap the order along the family · working · calculation

*What equation does the deviation vector of a family of geodesics obey, and why does curvature appear in it?*

The string between walkers on a ball, in "Walkers on a ball draw together faster and faster", shrank faster and faster, with an extra in proportion to its length. Calculus turns that rule into a second-order equation: the extra per stretch, divided by the stretch length squared, becomes a second derivative as the stretches shrink. Take a smooth family of timelike geodesics $x^\mu(\tau, s)$, with proper time $\tau$ along each member and a label $s$ across them. Write $u^\mu = \partial x^\mu/\partial\tau$ for the four-velocity, $\xi^\mu = \partial x^\mu/\partial s$ for the deviation vector, and $D/d\tau$ and $D/ds$ for covariant derivatives along the two sets of grid lines.

Three facts combine, as the derivation "Deviation from swapping the order" shows step by step.

- Mixed partial derivatives commute and the Christoffel symbols are symmetric, so $D\xi^\mu/d\tau = Du^\mu/ds$.
- Each member is a geodesic, so $Du^\mu/d\tau = 0$.
- By the Ricci identity, swapping $D/d\tau$ and $D/ds$ on a vector along the family costs a curvature term.

Together they give the geodesic deviation equation

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma.$$

Read its features one at a time.

- The right side is linear in $\xi$: twice the separation gives twice the relative acceleration. That is the entry rule.
- Only $\xi$ and $u$ at the event enter, not $D\xi/d\tau$. To this order, neighbours released at rest and neighbours already separating feel the same relative acceleration.
- A part of $\xi$ along $u$ drops out, because $R^\mu{}_{\nu\rho\sigma}$ is antisymmetric in $\rho\sigma$. Only the part orthogonal to $u$ is accelerated.
- In flat spacetime the right side vanishes, and the components of $\xi$ in a parallel frame change linearly in $\tau$.

Now test it on a sphere of radius $a$, where $R_{abcd} = (g_{ac}g_{bd} - g_{ad}g_{bc})/a^2$ and arc length $s$ replaces $\tau$. For a unit-speed geodesic and $\xi = f\,e$, with $e$ a parallel unit vector orthogonal to it, the equation becomes $f'' = -f/a^2$. Walkers leaving the equator side by side have $f = f_0\cos(s/a)$. For stretches of length $h$, every solution obeys exactly

$$f(s + h) - 2f(s) + f(s - h) = -2\big(1 - \cos(h/a)\big)f(s).$$

Six equal stretches to the pole have $h/a = \pi/12$, and the factor is $0.068$: the entry rung's 7 hundredths. On a surface of constant $K = -1/b^2$ the sign flips, and walkers that start side by side separate as $\cosh(s/b)$.

**Takeaway:** Swapping covariant derivatives along and across a family of geodesics gives a relative acceleration equal to minus the Riemann tensor fed the four-velocity, the separation and the four-velocity again.

*What this leaves out:* First order in the separation and in the relative velocity, for test particles with no forces but gravity.

*Continues:* `ways_in/faster-and-faster-on-a-ball`, `ways_in/crumbs-in-a-falling-cabin`<br>*Builds on:* [[ricci-identity]], [[geodesic-equation]], [[deviation-vector]], [[covariant-derivative-along-a-curve]]<br>*See:* `derivations/deviation-from-swapping-order`, `problems/stretch-rule-is-exact`

### 4. Gyroscope axes turn it into a matrix · working · operational

*What does a freely falling observer with gyroscopes measure, and what matrix does the equation give them?*

The two crumbs in "Two crumbs read the curving of spacetime" were timed by one freely falling observer. Give that observer three gyroscopes. Nothing twists them in free fall, so their spin axes are parallel transported along the worldline. Together with $\hat e_{\hat 0} = u/c$ they form an orthonormal frame that stays parallel. Components in a parallel frame change by ordinary derivatives, so the derivation "Components in a parallel frame" turns the geodesic deviation equation into

$$\frac{d^2\xi^{\hat\imath}}{d\tau^2} = -c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}\,\xi^{\hat\jmath}.$$

The time component of $\xi$ has zero second derivative and never feeds the spatial equation. So the observer needs one $3\times3$ matrix, $-c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$: relative acceleration per unit separation. Pair exchange, $R_{\hat\imath\hat 0\hat\jmath\hat 0} = R_{\hat\jmath\hat 0\hat\imath\hat 0}$, makes it symmetric, so its eigenvectors are orthogonal directions along which neighbours accelerate directly apart or directly together. Radar timing to test masses gives $\xi^{\hat\imath}$, so pairs of test masses measure the matrix. Its six entries depend on the observer's four-velocity: a boosted observer measures other combinations of the same Riemann tensor.

For a static weak field with potential $\Phi$ and slow motion, the weak-field form of the tensor, $R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \partial_i\partial_j\Phi/c^2$, gives Newton's tidal equation $\ddot\xi^i = -\partial_i\partial_j\Phi\,\xi^j$. Outside a spherical mass the matrix is $(GM/r^3)\,\mathrm{diag}(2, -1, -1)$ in the radial and two transverse directions. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$. A steady relative acceleration $a$ makes consecutive one-second shrinks differ by $a\,(1\ \mathrm s)^2$, so this is the entry rung's extra of 1.54 thousandths of a millimetre each second, per metre of string.

In Schwarzschild spacetime the pattern holds exactly, for observers at rest and for observers falling radially: $R^{\hat r}{}_{\hat 0\hat r\hat 0} = -2GM/r^3c^2$, and each transverse entry is $+GM/r^3c^2$. This is stated here without derivation. The worked example "Tides at two horizons" puts numbers in.

Instruments read these entries. The GOCE satellite compared accelerometers 0.5 m apart, and the free mirrors of gravitational-wave detectors respond to the oscillating entries of a passing wave.

**Takeaway:** In the frame of a freely falling observer's gyroscopes, relative accelerations of neighbours form a symmetric matrix of Riemann components, which becomes the Newtonian tidal matrix in weak fields.

*What this leaves out:* Separations small compared with the distance over which the matrix changes; a static weak field and slow motion for the Newtonian form.

*Continues:* `ways_in/crumbs-in-a-falling-cabin`, `ways_in/swap-the-order-along-the-family`<br>*Builds on:* [[proper-time]], [[freely-falling-frame]], [[newtonian-tidal-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/components-in-a-parallel-frame`, `worked_examples/tides-at-two-horizons`, `observations/goce-gradiometer`, `observations/gw150914-free-mirrors`

### 5. Jacobi fields: the exact statement and its limits · formal · structure

*In what precise sense does the equation hold, what structure does it carry, and where does it stop describing real neighbours?*

The swap of derivatives in "Swap the order along the family" becomes a theorem once the family is a smooth map. Set $G = c = 1$ and give $(M, g)$ its Levi-Civita connection. A geodesic variation is a smooth map $x: I\times(-\epsilon, \epsilon) \to M$ whose curves $x(\cdot, s)$ are affinely parametrized geodesics. Write $u = x_*\partial_\lambda$ and $J = x_*\partial_s$.

*Theorem (Jacobi equation).* Along $x(\cdot, 0)$, $D_\lambda^2 J = -\mathcal{R}(J, u)u$, with $\mathcal{R}(X, Y) = [\nabla_X, \nabla_Y] - \nabla_{[X,Y]}$. *Sketch:* zero torsion gives $D_\lambda J = D_s u$; since $[\partial_\lambda, \partial_s] = 0$, $D_\lambda D_s u - D_s D_\lambda u = \mathcal{R}(u, J)u$; and $D_\lambda u = 0$. The equation is linear, second order and exact for variation fields. Its solutions, the Jacobi fields, are exactly the variation fields of geodesic variations, and they form a $2n$-dimensional space. It is the linearization of the geodesic flow, not an approximation to it.

*Structure.* The Jacobi operator $X \mapsto \mathcal{R}(X, u)u$ annihilates $u$ and is self-adjoint by pair exchange. The derivation "The sign from sectional curvature" gives

$$g\big(J, D_\lambda^2J\big) = -K(u,J)\,\big[g(u,u)\,g(J,J) - g(u,J)^2\big].$$

On a Riemannian manifold, with unit $u$ and $J \perp u$, convergence means $K > 0$. For unit timelike $u$ the bracket is negative, so free neighbours accelerating toward each other have $K < 0$, the opposite of a sphere. In a parallel orthonormal frame with $\hat e_{\hat 0} = u$, the matrix $R_{\hat\imath\hat 0\hat\jmath\hat 0}$ has trace $R_{\mu\nu}u^\mu u^\nu$. A small cloud released with zero relative velocity therefore starts with $\ddot V/V = -R_{\mu\nu}u^\mu u^\nu$: zero in vacuum, where only the shape changes at first, and $-4\pi\rho$ for dust when $\Lambda = 0$.

*Conjugate points.* A point $q$ on the geodesic is conjugate to $p$ if a nonzero Jacobi field vanishes at both. On a round sphere of radius $a$ this first happens at distance $\pi a$, where meridians from a pole meet again. A timelike geodesic from $p$ to $q$ with a point conjugate to $p$ strictly between them is not a local maximum of proper time. Focusing arguments, and through them the singularity theorems, work by forcing such points.

*Limits of validity.* A Jacobi field is first-order information about real neighbours.

- Two particular geodesics a proper distance $\ell$ apart obey the equation only up to higher-order terms, built from $\nabla R$ and products of curvature. So $\ell$ must be small compared with the curvature radius $|R|^{-1/2}$ and with the scale on which curvature changes.
- Terms involving the relative velocity enter at the next order, so fast relative motion needs a generalized deviation equation.
- Separations are compared at equal affine parameter. Only the part orthogonal to $u$ is physical, and for null geodesics only the two-dimensional screen part.
- The bodies must be test bodies with no forces but gravity. Other forces add the difference of their accelerations.
- Curvature may change quickly along the geodesic, as in a gravitational wave, provided $\ell$ is small compared with its wavelength.

**Takeaway:** The equation is exact for Jacobi fields, the linearized geodesic flow; for real neighbours it is first order in separation and relative velocity, and on timelike planes its sign is opposite to a sphere's.

*What this leaves out:* Levi-Civita connection and smooth geodesics; torsion or non-gravitational forces add terms.

*Continues:* `ways_in/swap-the-order-along-the-family`, `ways_in/gyroscope-axes-and-a-tidal-matrix`<br>*Builds on:* [[lie-bracket]], [[levi-civita-connection]], [[ricci-tensor]]<br>*See:* `derivations/jacobi-sign`, `checks/timelike-plane-sign`, `checks/exact-or-first-order`, `problems/de-sitter-spreading`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| walk straight | — | To walk without ever steering left or right, even where the path bends over a curved surface. | [[geodesic]] |
| string | — | An imagined elastic string joining two close neighbours at matching step counts, or at the same reading of a clock that falls with them. If they start side by side, its length is the distance between their paths. | [[deviation-vector]] |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| spacetime | — | Space and time taken together as one world with four directions: three of space and one of time. | [[spacetime]] |
| Riemann curvature tensor | REE-mahn | A table of numbers, kept at every place, that describes the curving there. Each entry belongs to a pair of directions. Neighbours drawing together or spreading apart give some of its entries. | [[riemann-curvature-tensor]] |
| stretch | — | One of the equal pieces a walk is split into, such as one sixth of the walk from the equator to the North Pole. | — |
| extra shrinking | — | How much more one stretch of a walk, or one second of a fall, shrinks the string than the stretch or second before. When the string grows faster and faster instead, it is called the extra growing. | — |
| geodesic deviation equation | jee-oh-DESS-ik | The rule for how the drawing together or spreading apart of two close neighbours, who walk straight or fall freely, speeds up or slows down. The extra shrinking or growing of the string between them is in proportion to its length, and the curving sets the proportion. | [[geodesic-deviation-equation]] |

## Key equations

### Geodesic deviation equation · working

$$
\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\,\xi^\rho\,u^\sigma
$$

The relative acceleration of neighbouring geodesics is the Riemann tensor acting on four-velocity, separation and four-velocity, with a minus sign.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^\mu$ | deviation vector joining neighbours at equal proper time | xi |
| $u^\mu$ | four-velocity of the reference geodesic, with $u_\mu u^\mu = -c^2$ | u |
| $\frac{D}{d\tau}$ | covariant derivative along the geodesic, with respect to proper time | capital D by d tau |
| $R^\mu{}_{\nu\rho\sigma}$ | Riemann tensor in the course convention | the Riemann tensor |

**Holds when:** Smooth family of timelike geodesics; torsion-free connection. Exact for the family's deviation vector; for two particular neighbours, first order in separation and relative velocity.  
**Say it:** “The second covariant derivative of the deviation vector is minus the Riemann tensor contracted with the four-velocity, the deviation vector and the four-velocity.”  
**Justified by:** `derivations/deviation-from-swapping-order`

### Deviation in a freely falling frame · working

$$
\frac{d^2\xi^{\hat\imath}}{d\tau^2} = -c^2\,R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}\,\xi^{\hat\jmath}
$$

In a freely falling observer's parallel frame, relative acceleration is a symmetric matrix of Riemann components acting on the separation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^{\hat\imath}$ | spatial frame components of the separation | xi i hat |
| $R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$ | frame components of the Riemann tensor, observer's time direction in slots two and four | the Riemann components i zero j zero |

**Holds when:** Parallel orthonormal frame with $\hat e_{\hat 0} = u/c$, such as gyroscope axes; $x^0 = ct$; limits as for the covariant form.  
**Say it:** “Each separation component accelerates as minus c squared times the Riemann components i zero j zero acting on the separation.”  
**Justified by:** `derivations/components-in-a-parallel-frame`

### Weak-field frame components · working

$$
R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \frac{1}{c^2}\,\frac{\partial^2\Phi}{\partial x^i\,\partial x^j}
$$

In a weak static field the frame components are second derivatives of the Newtonian potential, giving Newton's tidal equation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Phi$ | Newtonian potential, $-GM/r$ outside a spherical mass | phi |

**Holds when:** Static weak field, slow motion, first order in $\Phi/c^2$.  
**Say it:** “The Riemann components i zero j zero are about the second derivatives of the potential over c squared.”  
**Justified by:** `riemann-curvature-tensor`

### Sign of the relative acceleration · formal

$$
g\big(J, D_\lambda^2 J\big) = -K(u,J)\,\big[g(u,u)\,g(J,J) - g(u,J)^2\big]
$$

Relative acceleration along the separation is set by the sectional curvature of the plane of four-velocity and separation, with a sign that flips for timelike planes.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $J$ | Jacobi field along the geodesic | J |
| $K(u,J)$ | sectional curvature of the plane of $u$ and $J$, course sign | the sectional curvature of u and J |

**Holds when:** Levi-Civita connection; affinely parametrized geodesic; the plane of $u$ and $J$ not null; $G = c = 1$.  
**Say it:** “J dotted with its second derivative is minus the sectional curvature times the squared area element of the plane of u and J.”  
**Justified by:** `derivations/jacobi-sign`

## Derivations

### Deviation from swapping the order · working

**Goal:** Show that the deviation vector of a family of geodesics obeys $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

1. Write the family as $x^\mu(\tau, s)$, with $u^\mu = \partial x^\mu/\partial\tau$ and $\xi^\mu = \partial x^\mu/\partial s$. Each curve of fixed $s$ is a geodesic with proper time $\tau$.
2. Mixed partial derivatives commute and $\Gamma^\mu{}_{\alpha\beta} = \Gamma^\mu{}_{\beta\alpha}$, so $D\xi^\mu/d\tau = Du^\mu/ds$.
3. Apply $D/d\tau$ to both sides: $D^2\xi^\mu/d\tau^2 = \dfrac{D}{d\tau}\dfrac{Du^\mu}{ds}$.
4. For any vector $Z^\mu$ along the family, expand both orders with $D/d\tau = u^\alpha\nabla_\alpha$ and $D/ds = \xi^\beta\nabla_\beta$. The terms with first derivatives of $Z$ cancel by step 2, and the Ricci identity turns the rest into $\dfrac{D}{d\tau}\dfrac{DZ^\mu}{ds} - \dfrac{D}{ds}\dfrac{DZ^\mu}{d\tau} = R^\mu{}_{\sigma\alpha\beta}Z^\sigma u^\alpha\xi^\beta$.
5. Put $Z = u$. Every member is a geodesic, so $Du^\mu/d\tau = 0$ for all $s$ and its derivative $D/ds$ vanishes. This leaves $D^2\xi^\mu/d\tau^2 = R^\mu{}_{\sigma\alpha\beta}u^\sigma u^\alpha\xi^\beta$.
6. Antisymmetry in the last pair, $R^\mu{}_{\sigma\alpha\beta} = -R^\mu{}_{\sigma\beta\alpha}$, and renaming dummy indices give $-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$.

**Result:** $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma$ for the deviation vector of any smooth family of geodesics, with a torsion-free connection.

### Components in a parallel frame · working

**Goal:** Write the geodesic deviation equation in the orthonormal frame carried by a freely falling observer's gyroscopes.

1. Along the geodesic take an orthonormal frame $\hat e_{\hat a}{}^\mu$ with $\hat e_{\hat 0}{}^\mu = u^\mu/c$, parallel transported, and its dual frame $\hat e^{\hat a}{}_\mu$, also parallel.
2. Define $\xi^{\hat a} = \hat e^{\hat a}{}_\mu\xi^\mu$. The dual frame is parallel, so $d^2\xi^{\hat a}/d\tau^2 = \hat e^{\hat a}{}_\mu D^2\xi^\mu/d\tau^2$.
3. Insert the equation with $u^\nu = c\,\hat e_{\hat 0}{}^\nu$ and $\xi^\rho = \xi^{\hat b}\hat e_{\hat b}{}^\rho$: $d^2\xi^{\hat a}/d\tau^2 = -c^2R^{\hat a}{}_{\hat 0\hat b\hat 0}\,\xi^{\hat b}$.
4. For $\hat b = \hat 0$, $R^{\hat a}{}_{\hat 0\hat 0\hat 0} = 0$ by antisymmetry in the last pair, so the time component of $\xi$ never enters.
5. For $\hat a = \hat 0$, lowering with $\eta_{\hat 0\hat 0} = -1$ gives $R_{\hat 0\hat 0\hat b\hat 0} = 0$ by antisymmetry in the first pair, so $d^2\xi^{\hat 0}/d\tau^2 = 0$.
6. Pair exchange gives $R_{\hat\imath\hat 0\hat\jmath\hat 0} = R_{\hat\jmath\hat 0\hat\imath\hat 0}$, and spatial indices are raised with $\delta_{ij}$, so the spatial matrix is symmetric.

**Result:** $d^2\xi^{\hat\imath}/d\tau^2 = -c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}\xi^{\hat\jmath}$, with a symmetric matrix, and $d^2\xi^{\hat 0}/d\tau^2 = 0$.

### The sign from sectional curvature · formal

**Goal:** Relate $g(J, D_\lambda^2 J)$ to the sectional curvature of the plane of $u$ and $J$.

1. Contract $D_\lambda^2 J^\mu = -R^\mu{}_{\nu\rho\sigma}u^\nu J^\rho u^\sigma$ with $J_\mu$: $g(J, D_\lambda^2 J) = -R_{\mu\nu\rho\sigma}J^\mu u^\nu J^\rho u^\sigma$.
2. The course definition $K(X,Y) = R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma/\big(g(X,X)g(Y,Y) - g(X,Y)^2\big)$ with $X = J$ and $Y = u$ writes that contraction as $K(J,u)\big[g(J,J)g(u,u) - g(J,u)^2\big]$.
3. Swapping $X$ and $Y$ flips both antisymmetric pairs of the numerator and leaves the denominator unchanged, so $K(J,u) = K(u,J)$.

**Result:** $g(J, D_\lambda^2 J) = -K(u,J)\big[g(u,u)g(J,J) - g(u,J)^2\big]$.

## Worked examples

### Tides at two horizons · working

**Problem:** An astronaut 2.0 m tall falls feet first, radially, into a non-rotating black hole. Using the frame component $R^{\hat r}{}_{\hat 0\hat r\hat 0} = -2GM/r^3c^2$ for a radially falling observer, find the difference between the free-fall accelerations of her head and feet as she crosses the horizon $r = 2GM/c^2$, for (a) 10 solar masses and (b) $4.3\times10^6$ solar masses. Take $GM_\odot = 1.327\times10^{20}\ \mathrm{m^3\,s^{-2}}$.

1. Radially, the frame form gives $\ddot\xi^{\hat r} = -c^2R^{\hat r}{}_{\hat 0\hat r\hat 0}\,\xi^{\hat r} = (2GM/r^3)\,\xi^{\hat r}$: head and feet are pushed apart.
2. At $r = 2GM/c^2$ the coefficient is $2GM\,c^6/(2GM)^3 = c^6/4G^2M^2$, falling as $1/M^2$.
3. (a) $GM = 1.327\times10^{21}\ \mathrm{m^3\,s^{-2}}$: $r = 29.5$ km and $2GM/r^3 = 1.03\times10^{8}\ \mathrm{s^{-2}}$, so $2.1\times10^{8}\ \mathrm{m/s^2}$ across 2.0 m, about 21 million times Earth's surface gravity.
4. (b) The mass is $4.3\times10^5$ times larger, so the coefficient is $(4.3\times10^5)^2 = 1.85\times10^{11}$ times smaller, $5.6\times10^{-4}\ \mathrm{s^{-2}}$: $1.1\times10^{-3}\ \mathrm{m/s^2}$ across 2.0 m, at $r = 1.27\times10^{7}$ km.

**Answer:** (a) $2.1\times10^{8}\ \mathrm{m/s^2}$; (b) $1.1\times10^{-3}\ \mathrm{m/s^2}$, about one ten-thousandth of Earth's surface gravity.

**Takeaway:** Tides at a horizon scale as $1/M^2$: overwhelming at a stellar black hole, gentle at a supermassive one, and finite at both.

## Problems

### `past-the-pole` · entry · difficulty 3 · calculation

Two friends leave the equator of a huge smooth ball side by side, 100 metres apart, facing the North Pole, and walk straight. The walk to the North Pole is split into six equal stretches. After four stretches the string between them is 50.0 metres long, and the fourth stretch shrank it by 20.7 metres. Each stretch shrinks the string more than the stretch before, by about 7 hundredths of the string's length at the end of the earlier stretch. How long is the string after five stretches, and after six? What happens in a seventh stretch, if the friends keep walking straight?

**Hints**

1. Find 7 hundredths of 50.0 metres and add it to 20.7 metres.
2. After six stretches the string is about zero long. What is 7 hundredths of zero?

**Answer:** After five stretches about 25.9 metres, and after six about zero: the friends meet at the North Pole. In a seventh stretch they walk on past each other, and they end up about 25.9 metres apart on the far side of the North Pole.

**Must contain:** After five stretches about 25.9 metres; After six, about zero: the friends meet at the North Pole; The seventh stretch has no extra, so the friends walk past each other and end up about 26 metres apart

**Numeric:** string after five stretches = 25.9 m (magnitude, ±0.6); string after six stretches = 0 m (magnitude, ±0.6); distance apart after seven stretches = 25.9 m (magnitude, ±0.8)

**Solution**

1. Seven hundredths of 50.0 metres is 3.5 metres, so the fifth stretch shrinks the string by about 20.7 plus 3.5, which is 24.2 metres. That leaves about 25.8 metres; the exact value is 25.9.
2. Seven hundredths of 25.9 metres is 1.8 metres, so the sixth stretch shrinks the string by about 24.2 plus 1.8, which is 26 metres. That brings it to about zero: the friends meet at the North Pole.
3. At the end of the sixth stretch the string is zero long, and seven hundredths of zero is zero. So the seventh stretch has no extra, and it changes the friends' distance by the same 26 metres as the sixth stretch.
4. A string cannot be shorter than zero. Changing by another 26 metres means the friends walk on past each other at the North Pole. The friend who was on the other's right is now on the other's left, and they end up about 26 metres apart.

**Targets:** `shrinks-at-a-steady-rate`

### `stretch-rule-is-exact` · working · difficulty 2 · derivation

On a sphere of radius $a$, the deviation equation for a separation $\xi = f(s)\,e$ orthogonal to a unit-speed geodesic reduces to $f'' = -f/a^2$. (a) Show that every solution obeys $f(s+h) - 2f(s) + f(s-h) = -2\big(1 - \cos(h/a)\big)f(s)$ exactly. (b) Show that dividing by $h^2$ and letting $h \to 0$ recovers the equation. (c) Evaluate the factor for six equal stretches from equator to pole, and for 100 km stretches on a sphere of radius 6371 km.

**Hints**

1. Write the general solution as $A\cos(s/a) + B\sin(s/a)$.

**Answer:** (a) Every solution has $f(s+h) + f(s-h) = 2\cos(h/a)\,f(s)$. (b) The factor is $(h/a)^2 + O(h^4)$, so the rule tends to $f'' = -f/a^2$. (c) $0.0681$ and $2.46\times10^{-4}$.

**Must contain:** Every solution is a combination of cosine and sine of s over a; The sum identities give the exact finite-step rule; 0.0681 for six stretches, 2.46 times ten to the minus four for 100 kilometres

**Numeric:** factor for six stretches to the pole = 0.0681 1 (magnitude, ±0.0005); factor for 100 km stretches = 0.000246 1 (magnitude, ±2%)

**Solution**

1. The equation $f'' = -f/a^2$ has general solution $f = A\cos(s/a) + B\sin(s/a)$.
2. With $x = s/a$ and $y = h/a$, $\cos(x+y) + \cos(x-y) = 2\cos x\cos y$ and $\sin(x+y) + \sin(x-y) = 2\sin x\cos y$, so $f(s+h) + f(s-h) = 2\cos(h/a)\,f(s)$.
3. Subtracting $2f(s)$ gives $f(s+h) - 2f(s) + f(s-h) = -2\big(1 - \cos(h/a)\big)f(s)$, for any $A$ and $B$: the rule does not care how the walkers started.
4. The left side is $h^2f''(s) + O(h^4)$, and the right side is $-(h/a)^2 f(s) + O(h^4)$. Dividing by $h^2$ and letting $h \to 0$ gives $f'' = -f/a^2$.
5. For $h/a = \pi/12$: $2(1 - \cos 15^\circ) = 0.0681$. For $h/a = 100/6371 = 0.01570$: $2(1 - \cos 0.01570) = 2.46\times10^{-4}$, almost exactly $(h/a)^2$.

### `de-sitter-spreading` · formal · difficulty 3 · derivation

A spacetime of constant curvature has $R_{\mu\nu\rho\sigma} = k\,(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$ with constant $k$; set $G = c = 1$. (a) Show that the part $\xi_\perp$ of a deviation vector orthogonal to a unit timelike geodesic obeys $D^2\xi_\perp/d\tau^2 = k\,\xi_\perp$, for a family whose members share one normalization. (b) Use Einstein's equation with a cosmological constant $\Lambda$ and no matter to find $k$. (c) For $\Lambda = 1.1\times10^{-52}\ \mathrm{m^{-2}}$, restore SI units and find the late-time e-folding time of the separation of free test masses, in gigayears. (d) Compare the sign with neighbouring geodesics on a sphere.

**Hints**

1. Contract the given Riemann tensor with $u^\nu\xi^\rho u^\sigma$ and use $g(u,u) = -1$.
2. Contract twice to get $R_{\nu\sigma}$ and $R$, then form $G_{\mu\nu}$.

**Answer:** (a) $D^2\xi_\perp/d\tau^2 = k\,\xi_\perp$. (b) $k = \Lambda/3$. (c) $c\sqrt{\Lambda/3} = 1.8\times10^{-18}\ \mathrm{s^{-1}}$, an e-folding time of about 17.5 Gyr. (d) Positive $k$ makes sphere geodesics converge but timelike neighbours spread.

**Must contain:** The contraction gives k times the orthogonal separation; k equals Lambda over three; An e-folding time of about 17.5 gigayears, with the sign opposite to a sphere's

**Numeric:** late-time e-folding time = 17.5 Gyr (magnitude, ±3%)

**Solution**

1. $-R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma = -k\big(\delta^\mu{}_\rho g_{\nu\sigma} - \delta^\mu{}_\sigma g_{\nu\rho}\big)u^\nu\xi^\rho u^\sigma = -k\big[g(u,u)\,\xi^\mu - g(u,\xi)\,u^\mu\big]$.
2. With $g(u,u) = -1$ this is $k\big[\xi^\mu + g(u,\xi)\,u^\mu\big] = k\,\xi_\perp^\mu$.
3. With a shared normalization $g(u,\xi)$ is constant and $Du/d\tau = 0$, so $D^2\xi_\perp/d\tau^2 = D^2\xi/d\tau^2 = k\,\xi_\perp$.
4. Contracting, $R_{\nu\sigma} = 3k\,g_{\nu\sigma}$ and $R = 12k$, so $G_{\nu\sigma} = -3k\,g_{\nu\sigma}$, and $G_{\mu\nu} + \Lambda g_{\mu\nu} = 0$ gives $k = \Lambda/3$.
5. In SI, $u\cdot u = -c^2$ gives $D^2\xi_\perp/d\tau^2 = kc^2\xi_\perp$. Masses released at rest separate as $\cosh(c\sqrt{k}\,\tau)$, which grows at late times as $e^{c\sqrt{k}\,\tau}$.
6. $c\sqrt{\Lambda/3} = 1.82\times10^{-18}\ \mathrm{s^{-1}}$, whose inverse is $5.5\times10^{17}$ s, or 17.5 Gyr.
7. On a sphere, $k > 0$ with a unit spacelike tangent gives $f'' = -kf$ and convergence; here $g(u,u) = -1$ flips the sign.

**Targets:** `converging-means-positive-curvature`

## Observations

- **Gravity gradients measured by the GOCE satellite, 2009 to 2013** (measured, working). GOCE flew about 255 km up with its air drag compensated, carrying accelerometer pairs 0.5 m apart along three perpendicular arms. After the satellite's rotation is removed, the measured differences of acceleration are entries of $-c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$, here the Newtonian gradient matrix. *Numbers:* Spherical Earth at 255 km: radial entry $2GM/r^3 = 2.74\times10^{-6}\ \mathrm{s^{-2}}$, or $1.4\times10^{-6}\ \mathrm{m/s^2}$ across 0.5 m. Gravity maps come from the far smaller departures. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **The free mirrors of the LIGO detectors responding to the gravitational wave GW150914** (measured, working). At the signal's frequencies each end mirror, hung as a pendulum, moves along its arm like a free mass, so the frame form with the wave's oscillating curvature gives the change in each 4 km arm. *Numbers:* Peak strain $1.0\times10^{-21}$: arm changes of about $\tfrac12 hL = 2\times10^{-18}$ m. At 150 Hz the relative acceleration amplitude $\tfrac12 h(2\pi f)^2L$ is about $1.8\times10^{-12}\ \mathrm{m/s^2}$, and the wavelength, 2000 km, dwarfs the arms. *Reference:* B. P. Abbott and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Predict the next stretch** (entry). Show the first three string lengths for walkers leaving the equator side by side, and ask for the fourth before stating the rule. *Why:* Learners expect a steady shrink; their own subtraction breaks that. *Predict:* Will the fourth stretch shrink the string by the same amount as the third? *Visual:* [[two-walkers-set-off-side-by-side]] *Uses:* `ways_in/faster-and-faster-on-a-ball`, `checks/next-stretch-on-the-ball`
2. **Measure without looking outside** (entry). In the falling cabin, show scales reading zero, then release two crumbs and read the extra per metre as a table entry. *Why:* It makes curvature something an insider measures. *Predict:* If the crumbs start three times as far apart, how does the shrinking in each second change? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/crumbs-in-a-falling-cabin`, `checks/scales-cannot-tell`, `checks/three-metres-apart`
3. **Derive the equation** (working). Swap covariant derivatives along and across the family, then solve on a sphere to recover the 7 hundredths. *Why:* It shows why curvature appears and closes the loop with the entry table. *Uses:* `ways_in/swap-the-order-along-the-family`, `derivations/deviation-from-swapping-order`, `problems/stretch-rule-is-exact`
4. **Read the matrix an observer measures** (working). Put the equation on gyroscope axes, recover Newtonian tides, and test the claim that free fall removes relative acceleration. *Why:* It ties the tensor to instruments. *Predict:* With the Christoffel symbols zero along your worldline, can a neighbour still accelerate relative to you? *Uses:* `ways_in/gyroscope-axes-and-a-tidal-matrix`, `checks/christoffels-vanish-along-one-worldline`, `worked_examples/tides-at-two-horizons`, `observations/gw150914-free-mirrors`
5. **Mark exactness and signs** (formal). State the Jacobi theorem, the timelike sign flip and the limits, then apply them to a cosmological constant. *Why:* Graduate readers need what is exact, which sign bites, and where the first-order description ends. *Uses:* `ways_in/jacobi-fields-exact-statement-and-limits`, `checks/timelike-plane-sign`, `problems/de-sitter-spreading`

## Misconceptions

### “Curving makes the string between two walkers shrink by the same amount in every stretch.” · entry · `shrinks-at-a-steady-rate`

- **Why it is tempting:** The friends walk at a steady pace, so a steady change seems natural.
- **What is true:** Friends who start side by side are not heading toward each other at first, so the string starts shrinking slowly. The curving makes that shrinking speed up.
- **Exposed by:** `checks/next-stretch-on-the-ball`

### “Two falling crumbs draw together by the same amount however far apart they start.” · entry · `distance-apart-does-not-matter`

- **Why it is tempting:** Gravity feels the same everywhere in a room.
- **What is true:** Each crumb's path points at Earth's centre, like two spokes of a wheel, so crumbs twice as far apart have paths that lean toward each other twice as much. So the shrinking is in proportion to their distance apart.
- **Exposed by:** `checks/three-metres-apart`

### “One thing on its own, like bathroom scales in a falling cabin, can show whether Earth is nearby.” · entry · `one-object-can-tell`

- **Why it is tempting:** On the ground, scales show your weight, so they seem to measure gravity.
- **What is true:** In free fall the scales fall with you and read zero, near Earth or far from every planet. Comparing two falling objects, through the string between them, is what shows the curving.
- **Exposed by:** `checks/scales-cannot-tell`

### “In a freely falling frame the Christoffel symbols vanish, so neighbouring free particles cannot accelerate relative to each other.” · working · `free-fall-removes-relative-acceleration`

- **Why it is tempting:** The equivalence principle says gravity disappears in free fall.
- **What is true:** Coordinates remove the Christoffel symbols along one worldline, not their first derivatives across a separation. Those derivatives form the Riemann tensor.
- **Exposed by:** `checks/christoffels-vanish-along-one-worldline`

### “Free-fall neighbours that accelerate toward each other mean positive sectional curvature, as on a sphere.” · formal · `converging-means-positive-curvature`

- **Why it is tempting:** On surfaces, converging geodesics are the standard sign of positive curvature.
- **What is true:** For a timelike four-velocity the normalization is negative, which reverses the relation: converging free-fall neighbours have negative sectional curvature.
- **Exposed by:** `checks/timelike-plane-sign`

### “The geodesic deviation equation holds exactly for any two free-fall worldlines, whatever their separation and relative speed.” · formal · `exact-for-any-separation`

- **Why it is tempting:** Its derivation uses no approximation.
- **What is true:** It is exact for the variation field of a smooth family, which describes two real neighbours only to first order in separation and relative velocity.
- **Exposed by:** `checks/exact-or-first-order`

## Checks

1. **Entry · predict** `checks/next-stretch-on-the-ball`. Two friends leave the equator of a huge smooth ball side by side, 100 metres apart, facing the North Pole, and walk straight. The walk to the North Pole is split into six equal stretches. After three stretches the string between them is 70.7 metres long. The three stretches, in order, shrank it by 3.4, 10.0 and 15.9 metres. A classmate says the fourth stretch will also shrink it by 15.9 metres. How long is the string after four stretches?
   - **Hints:** Did the second stretch shrink the string by the same amount as the first?
   - **Answer:** About 50 metres, not 54.8. Each stretch shrinks the string more than the stretch before, because the curving makes the shrinking speed up. The extra shrinking is about 7 hundredths of the string's length at the end of the earlier stretch, here the third, where it is 70.7 metres. Seven hundredths of 70.7 is about 4.9 metres. So the fourth stretch shrinks the string by about 15.9 plus 4.9, which is 20.8 metres. That leaves about 49.9 metres, and the exact value is 50.0. Four stretches out of six take the friends two thirds of the way to the North Pole. There the circle they stand on is half as long as the equator, so the string is half its starting length, which agrees.
   - **Must contain:** The fourth stretch shrinks the string more than the third; The extra is about 4.9 metres, 7 hundredths of 70.7; About 50 metres
   - **Numeric:** string after four stretches = 50 m (magnitude, ±0.6)
   - **Targets:** `shrinks-at-a-steady-rate`
   - **Visual:** [[two-walkers-set-off-side-by-side]]
2. **Entry · numeric** `checks/three-metres-apart`. A cabin falls freely inside a tall hollow tower on Earth, with the air pumped out of the tower. Inside it, you hold two crumbs 3 metres apart, both the same distance from Earth's centre, and let go of both at once with no push. You time the string between them with a clock on the cabin wall. How much does the string shrink in the first second, the second second and the third second? How much does it shrink in all?
   - **Hints:** What does a one-metre string do in each second?
   - **Answer:** About 2.3, 6.9 and 11.6 thousandths of a millimetre, about 21 thousandths in all. For a one-metre string placed this way, the three seconds give 0.77, 2.31 and 3.85 thousandths of a millimetre. The extra shrinking is in proportion to the string's length. So a string three times as long has three times the extra in every second. Both strings start with no shrinking, and each second's shrink is built only from those extras: half an extra in the first second, then one more extra each second. Tripling every extra therefore triples every second's shrink: 2.31, 6.93 and 11.55 thousandths. Together they make about 20.8 thousandths of a millimetre, about a third of a hair's width.
   - **Must contain:** Three times the string, three times the shrinking each second; About 2.3, 6.9 and 11.6 thousandths of a millimetre; About 21 thousandths in all
   - **Numeric:** total shrink after three seconds = 0.0208 mm (magnitude, ±5%)
   - **Targets:** `distance-apart-does-not-matter`
   - **Visual:** [[falling-ring-of-crumbs]]
3. **Entry · explain** `checks/scales-cannot-tell`. An astronaut floats inside a windowless cabin with her feet touching bathroom scales, and the scales read zero. She knows the cabin is in one of two places. Either it falls freely inside a tall hollow tower on Earth, with the air pumped out of the tower, or it drifts far out in space, away from every star and planet. Can the scales tell her which? If not, what could she do instead, without looking outside?
   - **Hints:** Why do the scales read zero in the falling cabin?
   - **Answer:** The scales cannot tell her. In both places nothing but gravity acts on her or on the scales, and gravity makes everything fall alike. So she and the scales move together, nothing presses her onto them, and they read zero. Instead she can let go of two crumbs with no push, one metre apart, and watch the string between them. Near Earth the crumbs start to drift relative to each other, faster and faster, whichever way she places them. If they happen to lie across the line toward Earth's centre, the string shrinks by about 7 thousandths of a millimetre in three seconds. Far from every star and planet the crumbs stay put, and the string keeps its length. So comparing two falling objects shows the curving of spacetime, and a single reading on the scales does not.
   - **Must contain:** The scales read zero in both places; One small thing falling freely cannot show the curving; Two crumbs drift relative to each other near Earth, but stay put far from every planet
   - **Targets:** `one-object-can-tell`
4. **Working · evaluate-claim** `checks/christoffels-vanish-along-one-worldline`. A student argues: "In a freely falling frame the Christoffel symbols vanish, so both neighbouring particles have zero coordinate acceleration and their relative acceleration is zero. Geodesic deviation is a coordinate effect." Evaluate the argument.
   - **Hints:** Where exactly do the Christoffel symbols vanish?
   - **Answer:** The argument fails. Coordinates adapted to a freely falling observer with gyroscope axes make every $\Gamma^\lambda{}_{\mu\nu}$ vanish all along that observer's worldline, but not at a neighbour a separation $\xi^\sigma$ away. There, with $x^0 = c\tau$ and the neighbour nearly at rest, the geodesic equation gives a coordinate acceleration $-c^2\,\Gamma^\mu{}_{00} \approx -c^2\,\xi^\sigma\partial_\sigma\Gamma^\mu{}_{00}$. On the worldline $\Gamma$ and its time derivative vanish, so the course definition reduces to $R^\mu{}_{0\sigma 0} = \partial_\sigma\Gamma^\mu{}_{00}$. The relative acceleration is therefore $-c^2R^\mu{}_{0\sigma 0}\xi^\sigma$, the frame form. It is built from a tensor, so no coordinate change removes it where the Riemann tensor is nonzero, and radar between the particles measures it.
   - **Must contain:** The Christoffel symbols vanish only along one worldline; Their first derivatives survive at the neighbour; Those derivatives form the Riemann tensor
   - **Targets:** `free-fall-removes-relative-acceleration`
5. **Working · numeric** `checks/free-mirrors-in-a-wave`. A gravitational wave with strain $h_+(t) = h_0\cos(2\pi f t)$, $h_0 = 5.0\times10^{-22}$ and $f = 100$ Hz, travels along $z$. In the frame of a freely falling mirror, $R^{\hat x}{}_{\hat 0\hat x\hat 0} = -\ddot h_+/2c^2$. A second free mirror sits 3.0 km away along $x$. Find the amplitudes of the relative acceleration and of the change in separation.
   - **Hints:** Differentiate $h_0\cos(2\pi ft)$ twice.
   - **Answer:** The frame form gives $\ddot\xi^{\hat x} = -c^2R^{\hat x}{}_{\hat 0\hat x\hat 0}\,\xi^{\hat x} = \tfrac12\ddot h_+L$. The amplitude of $\ddot h_+$ is $h_0(2\pi f)^2 = 1.97\times10^{-16}\ \mathrm{s^{-2}}$, so the relative acceleration amplitude is $\tfrac12(1.97\times10^{-16})(3000\ \mathrm m) = 3.0\times10^{-13}\ \mathrm{m/s^2}$. Integrating twice with no drift gives $\delta\xi = \tfrac12h_+L$, of amplitude $7.5\times10^{-19}$ m. The wavelength, 3000 km, is far longer than the arm, so the first-order equation holds.
   - **Must contain:** Relative acceleration is half the strain's second derivative times the separation; About 3.0 times ten to the minus thirteen metres per second squared; About 7.5 times ten to the minus nineteen metres
   - **Numeric:** relative acceleration amplitude = 2.96e-13 m/s^2 (magnitude, ±3%); separation change amplitude = 7.5e-19 m (magnitude, ±3%)
6. **Formal · evaluate-claim** `checks/timelike-plane-sign`. Claim: near Earth two freely falling test masses side by side accelerate toward each other, just as neighbouring meridians on a sphere converge, so the sectional curvature of the plane of their four-velocity and separation is positive. Evaluate the claim in the course convention, and give that sectional curvature at Earth's surface.
   - **Hints:** Evaluate the bracket $g(u,u)g(\xi,\xi) - g(u,\xi)^2$ for a timelike $u$.
   - **Answer:** The claim is false. For $\xi \perp u$ the Jacobi relation gives $g(\xi, D^2\xi/d\tau^2) = -K\,[g(u,u)\,g(\xi,\xi)]$. On a sphere, with unit spacelike $u$, this is $-K|\xi|^2$, so convergence means $K > 0$. For a timelike four-velocity $g(u,u) = -c^2$, so it is $+Kc^2|\xi|^2$, and masses accelerating toward each other have $K < 0$. At Earth's surface the transverse relative acceleration is $-(GM/r^3)\,\xi$, so $Kc^2 = -GM/r^3$ and $K = -GM/r^3c^2 = -1.7\times10^{-23}\ \mathrm{m^{-2}}$. The plane containing the radial direction has $K = +2GM/r^3c^2 = +3.4\times10^{-23}\ \mathrm{m^{-2}}$, and there the masses separate.
   - **Must contain:** The timelike normalization reverses the sign relation; Converging free-fall neighbours have negative sectional curvature; About minus 1.7 times ten to the minus twenty-three per square metre
   - **Numeric:** sectional curvature of the transverse timelike plane = -1.715e-23 m^-2 (signed, ±3%)
   - **Targets:** `converging-means-positive-curvature`
7. **Formal · evaluate-claim** `checks/exact-or-first-order`. Claim: the geodesic deviation equation is exact, so the proper distance between any two free-fall worldlines, however far apart and however fast they separate, obeys it. Evaluate the claim, and illustrate with two meridians leaving the North Pole of a unit sphere at a small but finite angle.
   - **Hints:** What exactly does the variation field describe?
   - **Answer:** The claim confuses two objects. The Jacobi equation is exact for the variation field $J = \partial_s x$ of a smooth family of geodesics: it is the linearized geodesic flow. The distance between two particular geodesics equals $|J_\perp|\,\delta s$ only to first order in $\delta s$. Beyond that come terms built from $\nabla R$ and products of curvature, which matter unless the separation is small compared with the curvature radius and the scale on which curvature changes, and terms in the relative velocity, which matter unless it is small. For meridians leaving the pole an angle $\delta\phi$ apart, the Jacobi field gives $\sin\theta\,\delta\phi$ at colatitude $\theta$, exactly for the family. The great-circle distance between the two meridians is $\sin\theta\,\delta\phi\,[1 - \cos^2\theta\,\delta\phi^2/24 + \dots]$, so the equation misses a relative correction of order $\delta\phi^2$.
   - **Must contain:** Exact for the variation field of a family; First order in separation and relative velocity for two particular geodesics; Meridians: a relative correction of order delta phi squared
   - **Targets:** `exact-for-any-separation`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Slot order and sign in the deviation equation | $D^2\xi^\mu/d\tau^2 = -R^\mu{}_{\nu\rho\sigma}u^\nu\xi^\rho u^\sigma = +R^\mu{}_{\nu\rho\sigma}u^\nu u^\rho\xi^\sigma$, with the course Riemann tensor. | Some texts put the separation in the last slot with a plus sign; that is the same equation. Real disagreements come only from an opposite Riemann or signature convention: compare index order first, then check that a radial pair near a mass separates. |
| Name, sign and factors of c of the tidal matrix | Relative acceleration per unit separation is $-c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$, with no separate symbol. | Some texts call $R_{\hat\imath\hat 0\hat\jmath\hat 0}$ the tidal tensor or, in vacuum only, the electric part of the Weyl tensor; others set $c = 1$ or flip its sign so that positive entries pull neighbours apart. |

## Visuals

- ★ [[two-walkers-set-off-side-by-side]] (flagship): Entry picture: the string between walkers who start side by side, stretch by stretch, with the extra shrinking in proportion to its length. *Sketch:* This concept adds a stretch mode. The walk from the equator to the North Pole is split into equal stretches, and a table fills with the string's length at each stretch end, each stretch's shrink, and the extra over the stretch before. A readout divides each extra by the string's length where the stretches meet: 0.068 for six stretches on the ball, zero on flat ground, and negative, meaning extra growing, on a saddle. A slider tilts the walkers slightly toward each other at the start, and the readout does not change.
- [[falling-ring-of-crumbs]] (core): Two crumbs in a falling cabin: the per-second extra, its proportion to distance, and the Riemann entries it gives. *Sketch:* This concept adds a two-crumb mode with a cabin clock and bathroom scales that always read zero. The learner sets the crumbs' distance and direction and releases them at rest. A bar chart shows each second's shrink or growth and the constant extra, and a readout divides the extra by the distance, labelled as an entry of the table. A second panel compares the frame-form prediction with exact free-fall paths as the distance grows, showing where the first-order rule fails.

## Tutor moves

**Open with**

- Two friends start side by side on the equator of a huge smooth ball, 100 metres apart, facing the North Pole, and walk straight. Does the distance between them shrink by the same amount every thousand kilometres? *(prediction)*
- If you floated in a windowless cabin, how could you tell whether it was falling freely toward Earth or drifting far out in space? *(reflection)*

**If the learner is stuck**

- *The learner cannot see why each stretch shrinks the string more than the last.* → Have the learner subtract neighbouring lengths, then neighbouring shrinks, and compare each extra with the string's length. *Uses:* `ways_in/faster-and-faster-on-a-ball`
- *The learner treats the equation as setting the relative velocity.* → Stress that the equation fixes the second derivative, not the first; compare neighbours released at rest with neighbours already separating. *Uses:* `ways_in/swap-the-order-along-the-family`

**Common questions**

- *Why does the string start by shrinking so slowly?* (entry) The friends set off side by side, facing the same way, so at first neither is heading toward the other. The curving does not set how fast the string shrinks. It sets how fast that shrinking speeds up. So the shrinking starts from nothing and builds, stretch after stretch. *Uses:* `ways_in/faster-and-faster-on-a-ball`
- *Is something pulling the two crumbs toward each other?* (entry) Their pull on each other is far too weak to matter. Each crumb falls freely toward Earth's centre, and the two paths lean slightly toward each other, like two spokes of a wheel. In Einstein's picture each crumb follows a straight path through spacetime, and the shrinking string is the curving of spacetime showing itself. *Uses:* `ways_in/crumbs-in-a-falling-cabin`

**Switching levels**

- To working when: asks for the equation; uses derivatives or vectors. Derive the equation by swapping covariant derivatives, then solve it on a sphere. *Uses:* `ways_in/swap-the-order-along-the-family`, `derivations/deviation-from-swapping-order`
- To formal when: asks when the equation is exact; asks about sign conventions or conjugate points. Go to Jacobi fields, the timelike sign flip and the limits of validity. *Uses:* `ways_in/jacobi-fields-exact-statement-and-limits`, `checks/timelike-plane-sign`
- To research when: asks about singularity theorems, measuring curvature with test masses, or gravitational-wave memory. Open the research horizon. *Uses:* `research_horizon/focusing-and-singularity-theorems`, `research_horizon/gravitational-wave-memory`

**Pronunciations:** Riemann → REE-mahn; Jacobi → yah-KOH-bee; Levi-Civita → LEH-vee CHEE-vee-tah; Christoffel → KRIS-toff-el; Raychaudhuri → ray-CHOW-dhoo-ree; Szekeres → SEK-er-esh; GOCE → GOH-chay

## History

- **Carl Gustav Jacob Jacobi (1837).** In the calculus of variations, studied the linear equation obeyed by the difference between neighbouring extremals, and the conjugate points at which it vanishes again; the geodesic version carries his name. C. G. J. Jacobi (1837), *Zur Theorie der Variations-Rechnung und der Differential-Gleichungen*, Journal für die reine und angewandte Mathematik 17, 68–82, doi:10.1515/crll.1837.17.68
- **Tullio Levi-Civita (1927).** Derived the equation of geodesic deviation for Riemannian manifolds of any dimension, with the Riemann tensor as the coefficient. Tullio Levi-Civita (1927), *Sur l'écart géodésique*, Mathematische Annalen 97, 291–320, doi:10.1007/BF01447869
- **Felix Pirani (1956).** Made the equation the physical meaning of curvature in general relativity: an observer in a parallel-propagated frame measures Riemann components through the relative accelerations of neighbouring free particles. F. A. E. Pirani (1956), *On the physical significance of the Riemann tensor*, Acta Physica Polonica 15, 389–405

## Research horizon

- **Focusing, conjugate points and singularity theorems.** The trace of the Jacobi operator along a family of geodesics drives the Raychaudhuri equation for its expansion. When that trace is non-negative, as energy conditions imply through Einstein's equation, a rotation-free family that starts converging must develop conjugate or focal points within finite affine parameter, if the geodesics extend that far. Penrose used the null version of this focusing, for light rays leaving a trapped surface, to prove his singularity theorem. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123; Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57
- **Measuring curvature with test masses.** Pirani used geodesic deviation to give an observer-based, invariant characterization of gravitational radiation. Szekeres designed an idealized gravitational compass, test masses joined by springs whose strains read frame components of the curvature, and related its readings to the algebraic type of the Weyl tensor. These ideas shape how exact radiative spacetimes are interpreted and how detectors are modelled. F. A. E. Pirani (1957), *Invariant formulation of gravitational radiation theory*, Physical Review 105, 1089–1099, doi:10.1103/PhysRev.105.1089; Peter Szekeres (1965), *The gravitational compass*, Journal of Mathematical Physics 6, 1387–1391, doi:10.1063/1.1704788
- **Gravitational-wave memory.** Integrating the deviation equation through a burst of waves can leave free test masses permanently displaced: the memory effect. Linear memory comes from matter or radiation that escapes the source, and Christodoulou showed that the gravitational waves' own energy adds a nonlinear part. Memory is a target of searches in detector data. V. B. Braginsky, K. S. Thorne (1987), *Gravitational-wave bursts with memory and experimental prospects*, Nature 327, 123–125, doi:10.1038/327123a0; Demetrios Christodoulou (1991), *Nonlinear nature of gravitation and gravitational-wave experiments*, Physical Review Letters 67, 1486–1489, doi:10.1103/PhysRevLett.67.1486

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** Two friends 100 metres apart on the equator of a ball the size of Earth both face the North Pole and walk straight. The walk is cut into six equal stretches, and the string between them goes 100, then 96.6, 86.6, 70.7 metres, so each stretch shrinks it more than the one before: 3.4, then 10.0, then 15.9. The jump from one shrink to the next is about 7 hundredths of the string, and that jump is the extra shrinking. Twice the string, twice the shrinking. Flat ground does nothing; a saddle makes the string grow. I could not see why the first stretch gets exactly half of the extra rather than some other part of it, and when the note said the extra is the same share of the string's length I was not sure which length, because the string keeps changing. Then a cabin falls inside an airless tower, and two crumbs one metre apart drift together by 0.77, 2.31 and 3.85 thousandths of a millimetre in the first three seconds, each second 1.54 thousandths more than the second before; divide that 1.54 by the one metre and you have one entry of the table that describes the curving. I reread 'You float inside', because I first pictured myself floating in the tower, and the summary's 'How much it changes' sent me back to work out what 'it' was. Both entry takeaways did land: the string on the ball shrinks faster and faster until the friends meet, and the crumbs' extra divided by their distance is a Riemann curvature tensor entry.

**Stumbles (10)**

- “How much it changes is in proportion to the distance between the neighbours.”: 'It' has three candidates in the sentence before: the rule, the drawing together, the spreading apart. The reader has to guess which one changes, and the sentence is the fourth of five in the note's most-read field.
- “At matching counts they stand on the same one of the circles a globe draws around the ball, parallel to the equator.”: A globe does not draw anything, and 'the same one of the circles ... parallel to the equator' has to be reread to find what is parallel to what. The prerequisite the reader has just met calls these the circles printed on a globe.
- “On this walk, the extra shrinking is always the same share of the string's length.”: The string's length changes every stretch, so the sentence does not say which length the share is taken of. The check 'next-stretch-on-the-ball' needs the length at the end of the earlier stretch, so an entry reader cannot answer it from this sentence alone.
- “At the very start, side by side, the string is not shrinking at all. So the first stretch gets only half of the extra.”: A step left implicit: starting from no shrinking explains why the first stretch shrinks the string less, but not why it gets exactly half. The reader has no way to check the half, and the same half is used again in the falling-cabin way and in a check.
- “Two friends 100 metres apart who walk side by side for one kilometre draw together by only about one thousandth of a millimetre.”: 'Walk side by side for one kilometre' describes keeping the formation, which is steering. Friends who really stay side by side never draw together, so the sentence undercuts the note's own rule.
- “You float inside, with your feet touching bathroom scales.”: The nearest place named is the tower, so 'inside' first reads as inside the tower rather than inside the cabin, and the sentence is reread.
- “The line between them then runs across the line toward Earth's centre.”: 'Across' can mean simply crossing at any angle, and every later sentence ('placed this way', 'lie across the line') leans on this one for the right angle that makes the numbers true.
- “You measured it without looking outside.”: 'It' could be the number, the entry or the sideways direction named in the sentence before.
- “That extra, divided by the distance, gives a Riemann tensor entry.”: Two names for one thing: the glossary and every other sentence say 'Riemann curvature tensor', and a beginner cannot tell whether the shorter name is the same table.
- “The friend who was on the other's right is now on the left, and they end up about 26 metres apart.”: A direction without its reference: the first half says whose right, the second half leaves whose left to be guessed, just where the two friends have swapped sides.

**Fixes**

- Second independent novice read, of revision 4. The retelling brought back both entry takeaways and every number, so the ways work; what tripped it was three missing links (why half, which length, which container) and four pronouns or directions without a reference. All ten are now said outright.
- Summary: 'How much it changes' became 'That speeding up, or slowing down', so the sentence names what is in proportion to the distance instead of leaving a pronoun. No claim changed.
- 'Walkers on a ball draw together faster and faster': the latitude circles are now 'printed on a globe' in both the recap and the explanation, the wording the deviation-vector note already uses; the share is now pinned to 'the string's length at the end of the earlier stretch', which is what the check next-stretch-on-the-ball asks the reader to use; and the half is now derived rather than asserted, through the shrinking building from nothing to about one full extra across the first stretch.
- Checked the new half sentence with python3: the string is 100 cos(s/a) metres, so the first stretch shrinks it by 100(1 - cos 15 degrees) = 3.407 metres, and one full extra is 2(1 - cos 15 degrees) x 100 = 6.815 metres, exactly twice that. At the end of the first stretch the shrinking per stretch is 100 sin(15 degrees) x (15 degrees in turns of the ball) = 6.776 metres, which is the 'about one full extra' the sentence claims, 0.6 per cent below it.
- 'Walkers on a ball': the daily-life number now belongs to friends who 'set off side by side and walk straight', not to friends who 'walk side by side', which would mean steering. The number, about one thousandth of a millimetre over one kilometre, is unchanged and rechecked: 100 m x (1 - cos(1 km / 6,371 km)) = 0.00123 mm.
- 'Two crumbs read the curving of spacetime': 'You float inside the cabin'; the crumbs' line now runs 'at a right angle across' the line toward Earth's centre, which is the placement all the numbers assume; and 'You measured that entry'. The takeaway keeps its wording, because it already fills the 240-character limit; instead 'Riemann tensor' became a form of the glossary term 'Riemann curvature tensor', so the short name the takeaway and the working ways use resolves to the same table.
- Problem 'past-the-pole': the swapped sides are now 'on the other's left', matching 'on the other's right' in the same sentence.
- Ladder read as a stronger student: each non-entry way still opens by naming a way it continues, by that way's title; nothing changed outside entry text, so no symbol or notation moved down a rung; the five ways stay five routes of four kinds (picture, operational, calculation, operational, structure), with no kind on more than half.
- Nothing was dropped and no sentence was compressed. Entry way explanations go from 1,004 to 1,042 words against the 1,000-word cap, inside the 10 per cent review allowance and only for the stumble fixes listed here; every other part is unchanged apart from one glossary form and one word in a problem's solution.
- This pass rewrote the top-level novice record, which covered revision 2 with its own retelling and thirty stumbles. That record is kept in the snapshot geodesic-deviation-equation.before-novice2.json, and the two entries in rereads are untouched.
- Bumped the revision to 5.

**Concerns**

- review.physics covers revision 4, so the five changed learner-visible strings need a physics diff check and the status is back at novice-reviewed. None of them changes a claim, a number or a sign; the only new quantitative sentence, 'By the end of the first stretch it is shrinking at about one full extra per stretch', is checked in the fixes above.
- Entry way explanations now sit at 1,042 words against a cap of 1,000, inside the review allowance but with little room left. A later re-read that must add a step will have to shorten something in these two ways; the likeliest candidate is the twelve-stretch aside in 'Walkers on a ball draw together faster and faster'.
- The question of 'Walkers on a ball draw together faster and faster' says 'stretch by stretch' before the explanation introduces what a stretch is. The glossary carries the term and the explanation's second paragraph defines it, so I left the question alone rather than spend words on it.
- The falling-cabin recap says each Riemann entry 'belongs to a pair of directions', while the prerequisite riemann-curvature-tensor calls a pair of directions a tilt and indexes its table by a tilt and a starting direction. The two are consistent, but this note could reuse 'tilt' and save the reader a translation.
- This note calls the deviation vector an elastic string, because 'stretch' is already the name of a piece of the walk; the deviation-vector note calls it a stretchy string. An editor may want one word across both notes.
- The analogies list is still empty, and the schema allows that, but tutoring sits at 2,835 of 3,300 words, so there is room for one analogy from a setting no way uses.
- The visuals two-walkers-set-off-side-by-side and falling-ring-of-crumbs are still proposals with sketches only; three entry items point at them, so a reader has no picture yet.
- The registry's prerequisite list for this concept still lacks ricci-tensor, which the note names as a formal-rung prerequisite; the validator reports it as a note for sync_registry.py.
- The takeaway of 'Two crumbs read the curving of spacetime' is 232 of its 240 allowed characters, so a later reviewer who wants to spell out 'Riemann curvature tensor' there must shorten its first sentence.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 5 changed passages

- “Picture a cabin falling freely down a tall tower on Earth, with the air pumped out of the tower.”: 'Down a tall tower' can be pictured as falling along the outside of the tower; only the later 'air pumped out of the tower' hints that the cabin is inside it, so the sentence is reread.
- “She knows the cabin is either falling freely down a tall tower on Earth with the air pumped out, or drifting far out in space, away from every star and planet.”: 'With the air pumped out' has no stated container, so it reads as the cabin's air, and an astronaut breathing in an airless cabin is confusing. 'Down a tall tower' has the same outside-or-inside ambiguity, and a fuller sentence would pass 32 words.
- “A cabin falls freely down a tall tower on Earth, with the air pumped out of the tower.”: Same outside-or-inside ambiguity as the cabin way, and the check should match the way's wording.
- Fix: Cabin way explanation, scales-cannot-tell question and three-metres-apart question: 'down a tall tower' became 'inside a tall hollow tower'; the scales question names the tower as the place the air is pumped from and splits into two sentences. No claim changed.
- Fix: Read without stumbles: the cabin way's simplifies (pull of the tower, hills and crumbs ignored) and the orange try_it gaps (20, 19, 15, 9 mm; first shrink about 1 mm, later shrinks 4 and 6 mm, so 'by more between each later pair' holds).
- Fix: Entry way explanations were at 1,003 words before this re-read (cap 1,000); the fix adds one word, within the 10% review allowance. Nothing dropped.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Covariant equation D^2 xi^mu/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma, derivation deviation-from-swapping-order.: Re-derived by hand: D xi/dtau = D u/ds from torsion-free symmetric Gamma; commutator of D/dtau and D/ds on Z equals R^mu_{sigma alpha beta} Z^sigma u^alpha xi^beta with the course [nabla_mu, nabla_nu] V^rho = R^rho_{sigma mu nu} V^sigma, the first-derivative terms cancelling because [u, xi] = 0; set Z = u, use Du/dtau = 0, then antisymmetry in the last pair and renamed dummies. → Correct; matches the conventions geodesic-deviation row. Sign check on a sphere with R_abcd = (g_ac g_bd - g_ad g_bc)/a^2 (course sign, R = +2/a^2) gives -xi/a^2 for unit u orthogonal to xi: convergence.
- Frame form d^2 xi^i/dtau^2 = -c^2 R^i_{0j0} xi^j, time component decoupled, symmetric matrix.: Contracted with a parallel dual frame, u = c e_0; checked R^a_{000} = 0 (last pair) and R_{00b0} = 0 (first pair), pair exchange for symmetry. → Correct, including the factor c^2 with x^0 = ct.
- Weak field R^i_{0j0} ~ d_i d_j Phi / c^2 and Newton's tidal equation; outside a sphere the relative-acceleration matrix is (GM/r^3) diag(2,-1,-1); Schwarzschild R^r_{0r0} = -2GM/r^3c^2, transverse +GM/r^3c^2, for static and radially falling observers.: Gamma^i_00 = d_i Phi/c^2 from g_00 = -(1+2Phi/c^2); R^i_{0j0} = d_j Gamma^i_00 for a static field; d_i d_j(-GM/r) = GM(delta_ij - 3 n_i n_j)/r^3; radial boost invariance of the Schwarzschild frame components from the known result. → Correct in sign and factor.
- Orthogonal-part, flat-space and velocity-independence remarks; sphere f'' = -f/a^2 and exact finite-step rule f(s+h) - 2f(s) + f(s-h) = -2(1 - cos(h/a)) f(s); saddle cosh(s/b).: Sum identities for A cos + B sin; python for factors. → Correct. Factor 0.068148 for h/a = pi/12; 2.4636e-4 for 100 km on 6371 km, vs (h/a)^2 = 2.4637e-4.
- Entry walker numbers: lengths 96.6, 86.6, 70.7, 50.0, 25.9, 0; shrinks 3.4, 10.0, 15.9, 20.7; extras 6.6 and 5.9 as 7 hundredths of 96.6 and 86.6; stretches about 1,670 km; globe halfway 0.707.: python with L_k = 100 cos(15k degrees). → Correct: 96.59, 86.60, 70.71, 50.00, 25.88; shrinks 3.41, 9.99, 15.89, 20.71, 24.12, 25.88; extras equal 0.06815 L exactly; 1,668 km.
- Novice claim: with a side-by-side start the first stretch gets exactly half the extra (3.41 vs 6.81 m), and the first second of the fall half the extra (0.77 vs 1.54).: On the sphere f is even about the start, so f(h) - f(0) = -(1 - cos(h/a)) f(0), half the factor; for constant relative acceleration the first-second shrink is a/2 and later differences are a. → Confirmed exact in both settings, to the idealizations stated.
- Novice claim: twelve stretches give a share of 0.0171, about a quarter of 0.068.: python 2(1 - cos 7.5 degrees). → 0.017110; ratio 0.2511. Confirmed.
- Entry: friends 100 m apart walking side by side 1 km on Earth-sized ground draw together about one thousandth of a millimetre.: python 100 m (1 - cos(1/6371)). → 1.23 thousandths of a millimetre. Correct as 'about'.
- Novice orange try_it: gaps 20.0, 18.6, 14.6, 8.5 mm for a 25 cm orange, bands 2 cm apart at the middle, marks every 1.5 cm, gap measured with a strip at a right angle to the marked band.: python on a sphere of radius 3.979 cm, band angle 0.5027 rad: perpendicular geodesic from the marked band to the other band, tan(d/a) = cos(lat) tan(dphi), compared with the latitude-arc value a cos(lat) dphi. → The novice numbers are the latitude-arc (Jacobi) values; the procedure as written gives 20.0, 18.8, 15.2, 9.2 mm, because 29 degrees between bands is not small. Corrected to 'near 20, 19, 15 and 9' and a first shrink of about 1 mm (1.2), later 3.6 and 6.0: still faster and faster.
- Cabin numbers: GM/r^3 = 1.54e-6 s^-2; per-second shrinks 0.77, 2.31, 3.85 thousandths of a mm; 6.9 thousandths after 3 s; 3 m gives 2.31, 6.93, 11.56 and 20.8 total; radial extra twice as big; mutual pull negligible.: python with GM = 3.986e14, r = 6.371e6; x = a t^2/2; Gm/d^2 for a milligram crumb. → All correct above ground: 1.5414e-6; 0.771, 2.312, 3.853; 6.94; 20.81. Mutual pull 6.7e-17 m/s^2. A 3 s drop covers 44 m, so the field does not change during the fall.
- Entry setting 'a very deep shaft near Earth' with those numbers.: Newtonian tidal field inside rock: d_rr Phi = 4 pi G rho - 2GM/r^3, transverse GM/r^3; a long thin vacuum shaft adds the field of a negative-density cylinder, -2 pi G rho on each horizontal entry. rho = 2670 kg/m^3. → Error found. In a deep shaft the horizontal squeezing is about 0.42e-6 s^-2, not 1.54e-6, and the vertical spreading about 0.84e-6, not 3.08e-6 (this matches the borehole gravity-gradient relation). The numbers hold only outside Earth's mass. Moved the cabin to a tall tower with the air pumped out (way, scales check, three-metre check); the walls of a long hollow tube add no field inside.
- Novice claim: near Earth two crumbs released at rest drift relative to each other whichever way she places them.: Relative acceleration (GM/r^3) diag(2,-1,-1) n has no zero eigenvalue, so it is nonzero for every direction n; in the rock-shaft field diag(-0.84, 0.42, 0.42) it is also invertible. → Confirmed. At about 54.7 degrees from the vertical the string's length does not change at leading order while the crumbs drift sideways; the answer says 'drift relative to each other', which stays true.
- Check next-stretch-on-the-ball and problem past-the-pole: 50 m after four; 25.9, 0, and 25.9 m apart after a seventh stretch, with left and right swapped.: python L_7 = 100 cos 105 degrees = -25.88; signed finite-step rule; meridians cross exactly at the pole. → Correct; tolerances adequate.
- Check christoffels-vanish-along-one-worldline: relative acceleration -c^2 R^mu_{0 sigma 0} xi^sigma from Gamma vanishing on the worldline.: Course Riemann definition with Gamma and its time derivative zero on the worldline gives R^mu_{0 sigma 0} = d_sigma Gamma^mu_00; geodesic equation with dx^0/dtau = c. → Correct.
- Check free-mirrors-in-a-wave: R^x_{0x0} = -hddot_+/2c^2; 2.96e-13 m/s^2 and 7.5e-19 m for 5e-22, 100 Hz, 3 km; wavelength 3000 km.: TT-gauge R_{x0x0} = -(1/2) d_0^2 h_xx; python. → 2.961e-13; 7.5e-19; 2998 km. Correct.
- Check timelike-plane-sign: K = -GM/r^3c^2 = -1.7e-23 m^-2 transverse, +3.4e-23 radial.: Course sectional-curvature definition with g(u,u) = -c^2; python. → -1.715e-23 and +3.430e-23. Correct and consistent with the conventions row.
- Check exact-or-first-order: meridian distance sin(theta) dphi [1 - cos^2(theta) dphi^2/24].: Series of d = 2 asin(sin theta sin(dphi/2)); python at theta = 1, dphi = 0.1. → 0.0841368563 exact vs 0.0841368632 series. Correct.
- Formal way: Jacobi theorem D^2 J = -R(J,u)u with R(X,Y) = [nabla_X, nabla_Y] - nabla_[X,Y]; Jacobi fields are variation fields and form a 2n-dimensional space; trace of R_{i0j0} = R_{mu nu}u^mu u^nu; Vddot/V = -R_uu, -4 pi rho for dust; conjugate points at pi a; no local maximum past a conjugate point.: Mapped R(X,Y)Z = R^rho_{sigma mu nu} Z^sigma X^mu Y^nu; R_00 = sum R_{i0i0}; R_uu = 8 pi (T_uu + T/2) = 4 pi rho for dust with G = c = 1. → Correct with the stated hypotheses.
- Derivation jacobi-sign and key equation jacobi-sign.: Contraction with J and the course K definition; symmetry K(J,u) = K(u,J). → Correct; the non-null-plane condition is needed and stated.
- Worked example tides-at-two-horizons: 29.5 km, 2.1e8 m/s^2 (21 million g); 1.27e7 km, 1.1e-3 m/s^2.: python with GM_sun = 1.327e20. → 29.53 km, 2.06e8 (2.10e7 g); 1.270e7 km, 1.11e-3 (1.14e-4 g). Correct.
- Problem de-sitter-spreading: k = Lambda/3, D^2 xi_perp = k c^2 xi_perp, e-folding 17.5 Gyr for Lambda = 1.1e-52 m^-2.: Contractions R_{nu sigma} = 3k g, R = 12k, G = -3k g; g(u, xi) constant for shared normalization; python. → c sqrt(Lambda/3) = 1.815e-18 s^-1, 5.51e17 s = 17.46 Gyr; 17.5 within rel_tol 0.03. Sign: spreading, opposite to a sphere. Correct.
- Observation GOCE: 255 km altitude, 0.5 m baselines, 2GM/r^3 = 2.74e-6 s^-2, 1.4e-6 m/s^2 over 0.5 m.: python with r = 6626 km; mission facts from the reference. → 2.740e-6 and 1.370e-6. Correct; GOCE flew near 255 km for most of the mission and lower at the end.
- Observation GW150914: peak strain 1.0e-21, 2e-18 m arm change, 1.8e-12 m/s^2 at 150 Hz, wavelength 2000 km.: python; strain from the discovery letter. → 2.0e-18, 1.78e-12, 1999 km. Correct.
- References: Rummel, Yi, Stummer 2011 J. Geod. 85, 777-790; Abbott et al. 2016 PRL 116, 061102; Jacobi 1837 Crelle 17, 68-82; Levi-Civita 1927 Math. Ann. 97, 291-320; Pirani 1956 Acta Phys. Pol. 15, 389; Raychaudhuri 1955 Phys. Rev. 98, 1123; Penrose 1965 PRL 14, 57; Pirani 1957 Phys. Rev. 105, 1089; Szekeres 1965 J. Math. Phys. 6, 1387; Braginsky and Thorne 1987 Nature 327, 123; Christodoulou 1991 PRL 67, 1486.: WebSearch against publisher, ADS and INSPIRE records. → All confirmed and marked verified. Added DOIs 10.1103/PhysRev.105.1089, 10.1063/1.1704788, 10.1038/327123a0, 10.1103/PhysRevLett.67.1486. Pirani 1956 has no DOI (reprinted in GRG 41, 1215, 2009).
- History and horizon scope: Jacobi's accessory equation and conjugate points; Levi-Civita's n-dimensional geodesic deviation (not claimed first); Pirani's operational reading; Penrose's null focusing from trapped surfaces; Szekeres compass and Weyl type; linear and nonlinear memory.: Checked against the confirmed records and abstracts. → Scoped correctly.

**Counterexamples tried**

- Deep shaft through rock: breaks the cabin numbers, because the rock around the shaft changes the tidal field (horizontal 0.42e-6 instead of 1.54e-6 s^-2). Fixed by moving the cabin to an evacuated tower.
- Saddle: 'the string grows faster and faster' holds for a side-by-side start on constant negative curvature (cosh). The 'same share' sentence is scoped to 'this walk'.
- Flat ground with a tilted start: the distance changes, but the sentence is scoped to side-by-side starts. Survives.
- Walkers who start tilted toward each other on the ball: the exact finite-step rule holds for any start, but 'half the extra in the first stretch' needs a side-by-side start, and the text scopes it that way. Survives.
- Walkers side by side away from the equator, or walking along it: they are still two great circles that meet a quarter circle later, so the summary's 'until they meet' holds.
- Past the pole: the string would grow again; takeaway and summary say 'until they meet', and the problem treats the crossing. Survives.
- Very small ball, with stretches longer than a third of its circumference (h/a > pi): 'on a smaller ball the share is bigger' fails, since 2(1 - cos) peaks at h/a = pi. Not a first what-if at the stated sizes; left unscoped, recorded here.
- Crumbs placed at about 54.7 degrees from the vertical: the relative acceleration is nonzero but perpendicular to the string, so the length is unchanged at leading order. The scales check says 'drift relative to each other', which stays true.
- Crumbs along the vertical: they spread, twice as fast; stated in the cabin way. Inside matter the ratio changes, which the tower setting avoids.
- Large separation or fast relative motion: the exact-or-first-order check and the formal limits cover it; meridian example checked numerically.
- Strong field: Schwarzschild frame components are exact for static and radially falling observers; the horizon example stays first order because 2 m is much smaller than 29.5 km.
- Non-static field (gravitational wave): the frame form still holds when the separation is much smaller than the wavelength; the checks use 3 km against 3000 km.
- Massless case: for null geodesics only the two-dimensional screen part is physical; stated in the formal limits.
- Other observer: a boosted observer measures other combinations of Riemann components; stated in the gyroscope way.
- Non-rotating Earth idealization: Earth's spin adds nothing to the free-fall relative acceleration measured in a gyroscope frame over a few seconds at this precision; kept in simplifies.
- (revision 5 diff check) New sentence 'By the end of the first stretch it is shrinking at about one full extra per stretch', read as an average instead of an instantaneous rate: the second stretch shrinks the string by 10.0 m, not 6.8 m, so an average reading would be false. As written the sentence is about the rate at one moment, the end of the first stretch, which is 6.776 m per stretch against a full extra of 6.815 m. True on the intended reading; recorded because the two readings differ by half as much again.
- (revision 5 diff check) The same sentence on a saddle or on flat ground: on flat ground the extra is zero and the rate is zero, so 'half of one extra' is 0 = 0 and survives; on constant negative curvature the string grows as cosh and the same half holds with growing in place of shrinking. The sentence is scoped to the ball walk, so neither case is claimed.
- (revision 5 diff check) 'The extra shrinking is always the same share of the string's length at the end of the earlier stretch', with walkers who start tilted toward each other instead of side by side: the exact finite-step rule f(s+h) - 2f(s) + f(s-h) = -2(1 - cos(h/a))f(s) holds for every solution A cos(s/a) + B sin(s/a), so the sentence survives a tilted start. It fails only after the walkers cross, where the length is the magnitude of a signed f; the past-the-pole problem handles that crossing explicitly.
- (revision 5 diff check) 'The friend who was on the other's right is now on the other's left' past the pole, checked against the walker who keeps going: A on longitude 0 and B on longitude epsilon both walk north, so B is east of A and, facing north, on A's right. Past the pole A is on longitude 180 walking south and B on longitude 180 + epsilon, still east, but facing south east is on A's left. Sides swap, as the solution says.

**Fixes**

- Cabin way, scales check and three-metre check: the cabin now falls down a tall tower on Earth with the air pumped out, not a deep shaft. The rock around a deep shaft would make the sideways squeezing about a quarter of the quoted value. The cabin way's simplifies now also ignores the pull of the tower and nearby hills.
- Ball way try_it: gaps corrected to 'near 20, 19, 15 and 9 millimetres', with the first shrink 'about 1 millimetre', matching the strip laid at a right angle to the marked band. The earlier numbers were for a different measurement.
- References: all eleven confirmed and marked verified; four DOIs added.
- Nothing dropped; the entry word count changes by a few words, within the review allowance.
- Revision 5 diff check of the second novice read's five changed strings: nothing needed fixing, so no learner-visible text changed and the revision stands at 5. Every number in the note was recomputed from scratch rather than taken from the revision 4 record, and five of the eleven references were re-confirmed against publisher and ADS records.

**Concerns**

- Convention gap still open: the conventions file gives no symbol for an observer's tidal matrix, so the note writes -c^2 R^i_{0j0} everywhere.
- The prerequisite ricci-tensor still needs a registry sync (validator note).
- Tutor: in the scales check, a learner may place crumbs at an angle where the string keeps its length while the crumbs drift sideways. 'Drift relative to each other' is the true statement.
- The past-the-pole problem is still ahead of both entry ways, as the novice reviewer noted.
- 'By the end of the first stretch it is shrinking at about one full extra per stretch' is a rate at one moment. A learner who reads it as the next stretch's shrink will expect 6.8 metres and meet 10.0. The sentence is accurate and the next paragraph's arithmetic is unaffected, but a future novice pass may want 'at that moment' in it; that costs words the entry budget does not have.
- Entry way explanations sit at 1,042 words against a 1,000-word cap. Any further accuracy fix in the two entry ways will have to shorten something; the twelve-stretch aside in 'Walkers on a ball draw together faster and faster' is the lowest-value sentence, and dropping it costs no claim the note depends on.
- Cross-note wording, for an editor, not an accuracy fault: this note's falling-cabin recap says each Riemann entry 'belongs to a pair of directions', while the prerequisite riemann-curvature-tensor indexes its table by a tilt (a pair of directions) and a starting direction. Both are true of the entries this note measures, whose two index pairs each contain time, but the shorter phrasing describes fewer slots than the table has.

**Diff check** (2026-09-13, revision 4)

- Cabin way: 'Picture a cabin falling freely inside a tall hollow tower on Earth, with the air pumped out of the tower.' claims the same setting as the old 'down a tall tower' sentence.: Compared old and new sentences in context, including 'Seen from the tower's wall' and the simplifies line that ignores the pull of the tower; tried the tower's own mass as a what-if. → Same physical setting: an evacuated tower above ground, no rock around the cabin, so the horizontal tidal value g/R = 1.54e-6 s^-2 still applies. A hollow tower's walls pull even less on the cabin's inside than a solid one, and simplifies already ignores the tower's pull. Consistent with 'Seen from the tower's wall'. Accurate.
- Scales check: 'She knows the cabin is in one of two places. Either it falls freely inside a tall hollow tower on Earth, with the air pumped out of the tower, or it drifts far out in space, away from every star and planet.': Checked that the split keeps the either-or of the old sentence, that 'air pumped out of the tower' no longer suggests an airless cabin, and that the answer (scales read zero in both; crumbs drift near Earth, stay put far away) still follows. → Same claim as before; both options are free fall, so the zero reading and the crumb test in the answer are unchanged and true. 'Drifts' far in space is free fall with no tidal field. Accurate.
- Three-metres check question now uses the same tower wording; answer 2.31, 6.93, 11.55 thousandths of a millimetre, total 20.8, numeric 0.0208 mm rel_tol 0.05.: python3: k = g/R = 9.81/6.371e6 = 1.54e-6 s^-2; shrink in second n = (1/2) k L (n^2 - (n-1)^2). → L = 1 m: 0.77, 2.31, 3.85 micrometres; L = 3 m: 2.31, 6.93, 11.55, total 20.79 micrometres = 0.0208 mm. Setting unchanged, so answer and numeric field stand.

**Diff check** (2026-09-13, revision 5)

- Summary: 'That speeding up, or slowing down, is in proportion to the distance between the neighbours.' replaces 'How much it changes is in proportion to...'.: Compared the new sentence with the equation it summarizes, D^2 xi/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma: checked that the quantity named is the second derivative, not the first, and that linearity in xi is what 'in proportion to the distance' asserts. Tried the two cases the summary allows, drawing together and spreading apart, and the transverse case where the relative acceleration is perpendicular to the string. → Accurate, and more accurate than the sentence it replaces: the equation fixes the second derivative of the separation, which is exactly 'that speeding up, or slowing down', while the old 'How much it changes' could be read as the first derivative, which the equation does not fix. Linearity in xi is exact. In the perpendicular case both sides are zero, so the proportion survives.
- Recap and explanation of 'Walkers on a ball draw together faster and faster': 'they stand on the same circle around the ball, one of the circles printed on a globe parallel to the equator', and 'The string always covers the same fraction of that circle as it did of the equator.': Two walkers leaving the equator on meridians a longitude delta apart are at the same colatitude after equal arc length, so they share a latitude circle; the arc between them is a sin(theta) delta, a fixed fraction delta/2pi of that circle's length 2 pi a sin(theta). Compared the latitude arc with the geodesic distance for the note's numbers. → Accurate. The fraction claim is exact for the latitude arc. The geodesic between them is shorter by a relative cos^2(theta) delta^2/24; with delta = 100 m / 6,371 km that is about 1e-11, far below the note's tenth-of-a-metre rounding, and the way's simplifies keeps the friends close compared with the ball. Latitude circles are parallel to the equator and are the ones printed on a globe, and the walk's six stretches land on 15, 30, 45, 60 and 75 degrees, which a globe prints.
- 'On this walk, the extra shrinking is always the same share of the string's length at the end of the earlier stretch.': python3 on the exact solution L_k = 100 cos(15k degrees): formed extra_k = (L_{k-1} - L_k) - (L_{k-2} - L_{k-1}) = 2 L_{k-1} - L_k - L_{k-2} and divided by L_{k-1} for k = 2..6. Also checked the identity 2 L_{k-1} - L_k - L_{k-2} = 2(1 - cos(h/a)) L_{k-1} for a general solution A cos + B sin. → Correct, and the pinned length is the right one. Extras 6.583, 5.902, 4.819, 3.407, 1.764 m divided by L_{k-1} = 96.593, 86.603, 70.711, 50.000, 25.882 m give 0.068148 every time, the factor 2(1 - cos 15 degrees). Dividing by any other length in the walk does not give a constant, so the added phrase is not merely helpful but necessary, and it is what check next-stretch-on-the-ball asks the reader to use.
- The new derivation of the half: 'At the moment the friends set off side by side, the string is not shrinking at all. By the end of the first stretch it is shrinking at about one full extra per stretch. So across that first stretch the shrinking averages half of one extra: half of 7 hundredths of 100 metres is about 3.4 metres.': python3 on L(s) = 100 cos(s/a) with h/a = pi/12. Rate of shrinking per stretch = -h dL/ds = 100 sin(s/a) h. Evaluated at s = 0 and at s = h; compared with one full extra, 2(1 - cos(h/a)) x 100 m; and compared the stretch-average rate, which is the actual first shrink, with half of one extra. → Accurate at every step. At s = 0 the rate is exactly zero, because the start is side by side. At the end of the first stretch it is 6.776 m per stretch against one full extra of 6.815 m, 0.6 per cent below, which is what 'about' carries. The average rate across the first stretch is the first shrink, 3.4074 m, and half of one extra is 3.4074 m: equal exactly, not approximately, since 100(1 - cos x) is exactly half of 200(1 - cos x). The chain now gives the reader a reason where revision 4 asserted 'So the first stretch gets only half of the extra', and the reason is the true one.
- 'Two friends 100 metres apart who set off side by side and walk straight for one kilometre draw together by only about one thousandth of a millimetre.': python3: 100 m x (1 - cos(1 km / 6,371 km)). Also checked that the rewritten subject describes the same two walkers the way is about, since 'walk side by side' would describe steering rather than walking straight. → 0.00123 mm, so 'about one thousandth of a millimetre' holds. The rewrite makes the sentence describe the note's own walkers: friends who really keep formation are not on geodesics, and for them the distance would not change at all, so the old wording named a case in which the stated number is wrong. Accuracy improved.
- Crumbs way: 'You float inside the cabin' and 'The line between them then runs at a right angle across the line toward Earth's centre.': Checked the geometry the numbers assume: two crumbs at the same distance r from Earth's centre, 1 m apart, and the tidal matrix (GM/r^3) diag(2, -1, -1) in the radial and two transverse directions. The chord joining two points at equal radius is perpendicular to the radius that bisects them. → Accurate and needed. The quoted per-second shrinks 0.77, 2.31 and 3.85 thousandths of a millimetre come from the transverse eigenvalue -GM/r^3 = -1.541e-6 s^-2, which is the value only for a separation at a right angle to the radial direction; a line merely 'across' the radius at some other angle mixes in the radial eigenvalue +2GM/r^3 and changes every number. 'Inside the cabin' fixes the container without touching the physics.
- 'You measured that entry without looking outside', and 'Riemann tensor' added as a form of the glossary term 'Riemann curvature tensor' so the takeaway's short name resolves.: Read the two sentences before it to see which object 'that entry' names, then checked the claim itself: divide the per-second extra by the string's length and you get 1.54e-6 s^-2, which is -c^2 R^{x}_{0x0} for the sideways direction x. Compared the added glossary form with the prerequisite note riemann-curvature-tensor. → Accurate. The number the reader forms is the relative acceleration per unit separation, which is one entry of -c^2 R^i_{0j0}, exactly what the sentence claims, and it is obtained inside a sealed cabin. The prerequisite note's glossary already lists 'Riemann tensor' as a form of 'Riemann curvature tensor', so the added form matches the vault rather than inventing a synonym.
- Problem past-the-pole, solution step 4: 'The friend who was on the other's right is now on the other's left.': Placed the walkers on meridians of longitude 0 and epsilon walking north, worked out which side each is on before and after the pole, and checked that a walker who keeps walking straight continues on the opposite meridian, longitude 180 + epsilon. → Correct. Facing north, east is on the walker's right, so the friend at longitude epsilon starts on the other's right. Past the pole both face south, east is now on the left, and the friend is still the eastern one, so the sides have swapped. The sentence also now gives its reference on both halves, which the earlier 'is now on the left' did not.
- Every number in the note, recomputed independently of the revision 4 record.: python3 from the definitions: ball lengths 100 cos(15k degrees) and their differences; factor 2(1 - cos(h/a)) for 6 and 12 stretches and for 100 km on 6,371 km; stretch length; the 1 km daily-life number; GM/r^3 at Earth's surface and the per-second shrinks for 1, 2 and 3 m strings; the orange try_it gaps by solving for the geodesic that leaves one band at a right angle and meets the other; the two horizon tides; GOCE; GW150914; the free-mirror check; the sectional curvatures; the de Sitter e-folding time; the meridian series. → All reproduce the note. 96.593, 86.603, 70.711, 50.000, 25.882, 0, -25.882 m; shrinks 3.407, 9.990, 15.892, 20.711, 24.118, 25.882; factor 0.068148, twelve-stretch 0.017110 (0.251 of it), 100 km 2.4636e-4; 1,668 km; 0.00123 mm; GM/r^3 = 1.5414e-6 s^-2 giving 0.771, 2.312, 3.853 micrometres and 6.94 after three seconds, tripled to 2.312, 6.936, 11.560 and 20.81 for 3 m; orange gaps 20.0, 18.8, 15.2, 9.2 mm with first shrink 1.2 mm then 3.6 and 6.0; 29.53 km and 2.06e8 m/s^2 (2.1e7 g), 1.270e7 km and 1.11e-3 m/s^2; GOCE 2.740e-6 s^-2 and 1.37e-6 m/s^2; GW150914 2.0e-18 m, 1.78e-12 m/s^2, 1,999 km; mirrors 2.961e-13 m/s^2, 7.5e-19 m, 2,998 km; K = -1.715e-23 and +3.430e-23 m^-2; 17.46 Gyr; meridian distance 0.08413685628 against the series 0.08413686316. Every rounding in the note is honest and every tolerance covers the value a reader's own chain produces.
- References, re-confirmed rather than trusted: Levi-Civita 1927 Math. Ann. 97, 291-320; Jacobi 1837 Crelle 17, 68-82 with DOI 10.1515/crll.1837.17.68; Pirani 1956 Acta Phys. Polon. 15, 389-405; Szekeres 1965 J. Math. Phys. 6, 1387 with DOI 10.1063/1.1704788; Rummel, Yi and Stummer 2011 J. Geod. 85, 777-790 with DOI 10.1007/s00190-011-0500-0; Braginsky and Thorne 1987 Nature 327, 123-125.: WebSearch against publisher pages, EUDML and ADS records. → All six confirmed exactly as written, including the pages and the DOIs. Pirani 1956 still shows no DOI of its own; the 2009 republication in Gen. Rel. Grav. 41, 1215 is the citable reprint, as the record already says. The remaining five references were confirmed in the revision 4 pass and are standard; nothing in them was touched by this revision.
