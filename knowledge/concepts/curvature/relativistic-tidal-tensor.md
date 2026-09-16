---
type: "concept"
schema_version: 2
id: "relativistic-tidal-tensor"
title: "Relativistic tidal tensor"
tagline: "How the curving of space and time makes freely falling crumbs drift apart or together"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["tidal tensor", "tidal matrix", "tidal field tensor"]
prerequisites: ["geodesic-deviation-equation", "orthonormal-frame", "newtonian-tidal-tensor", "ricci-tensor", "lorentz-transformation", "einstein-field-equations", "weyl-tensor"]
leads_to: ["schwarzschild-tidal-field", "volume-preserving-tidal-deformation", "tidal-derivation-of-vacuum-field-equations", "ricci-focusing-versus-weyl-shear", "geodesic-deviation-in-gravitational-wave", "tidal-deformability"]
visuals: ["falling-ring-of-crumbs"]
---

# Relativistic tidal tensor

*How the curving of space and time makes freely falling crumbs drift apart or together*

`relativistic-tidal-tensor` · curvature · core · physics-reviewed (revision 7)

**Needs:** [[geodesic-deviation-equation]] (entry) · [[orthonormal-frame]] (working) · [[newtonian-tidal-tensor]] (working) · [[ricci-tensor]] (working) · [[lorentz-transformation]] (working) · [[einstein-field-equations]] (working) · [[weyl-tensor]] (formal)  
**Opens:** [[schwarzschild-tidal-field]] · [[volume-preserving-tidal-deformation]] · [[tidal-derivation-of-vacuum-field-equations]] · [[ricci-focusing-versus-weyl-shear]] · [[geodesic-deviation-in-gravitational-wave]] · [[tidal-deformability]]  
**Related:** [[tidal-force]] · [[sectional-curvature]] · [[riemann-curvature-operator]] · [[kretschmann-scalar]] · [[gravitoelectromagnetism]] · [[strong-energy-condition]]  
**Visuals:** ★ [[falling-ring-of-crumbs]]

> In a cabin falling freely near Earth, hold a ring of crumbs around a middle crumb. Set the ring so that the line toward Earth's centre runs through two of its crumbs. Let them all go with no push. The ring turns into an oval. Crumbs on that line drift away from the middle crumb, and crumbs across it drift in toward the line. The tidal tensor is the table of numbers that gives the drift of a crumb let go anywhere nearby. In Einstein's theory that table comes from the curving of space and time.

## You will be able to

**Entry**
- Predict how crumbs let go in a cabin falling near Earth drift, for crumbs on the line toward Earth's centre. `objectives/predict-the-ring-shape` ← `checks/crumbs-nearer-and-farther`
- Compute the drift of a crumb placed anywhere nearby by splitting its place along the main directions and adding the drifts. `objectives/combine-main-direction-drifts` ← `checks/crumb-three-along-four-across`, `problems/ring-for-a-millimetre-difference`

**Working**
- Compute the tidal tensor's eigenvectors, eigenvalues and trace from Riemann components or a potential, and read their signs. `objectives/read-the-matrix` ← `problems/tides-inside-and-outside-a-planet`
- Use the trace to relate the tides a falling observer measures to the density and pressure around them. `objectives/relate-trace-to-matter` ← `checks/pressure-adds-to-the-squeeze`
- Compute how the tidal tensor changes for an observer moving through the same event at a different velocity. `objectives/compute-for-a-moving-observer` ← `checks/polar-entry-ten-times`

**Formal**
- Decompose the tidal operator into the electric part of the Weyl tensor and Ricci terms, and apply it with a cosmological constant. `objectives/decompose-the-operator` ← `checks/where-lambda-wins`
- State which curvature components one observer's tidal operator fixes, and what the operators of all observers fix. `objectives/state-what-one-observer-reads` ← `checks/one-observer-six-numbers`
- Derive the tidal potential of a freely falling frame from Fermi normal coordinates, and state where it applies. `objectives/derive-the-tidal-potential` ← `problems/tides-in-fermi-coordinates`

## Ways in

### 1. A ring of crumbs turns into an oval · entry · picture

*What happens to a whole ring of crumbs let go around one crumb in a cabin falling freely near Earth?*

**Recap:** Moving with nothing but gravity acting is called falling freely. In a cabin falling freely near Earth, two crumbs are let go with no push. They drift relative to each other, slowly at first, then faster and faster. In a given time, the drift is in proportion to the distance between them. The Riemann curvature tensor is a table of numbers, kept at every place, that describes the curving of space and time there. Drifting crumbs measure some of its numbers.

Picture a cabin falling freely inside a tall hollow tower on Earth, with the air pumped out of the tower. Dropped from rest, the cabin falls about 490 metres in ten seconds, about one and a half times the height of the Eiffel Tower.

Inside, thirteen crumbs are held still, relative to the cabin. One is in the middle. The other twelve sit on a circle 1 metre from the middle crumb, placed like the hours on a clock face. The clock face is turned so that the line toward Earth's centre runs through the 6, the middle crumb and the 12, with the 6 nearer Earth's centre.

All thirteen crumbs are let go together, with no push. Watch for ten seconds by the cabin's clock. With a ruler fixed to the cabin, measure where each crumb is compared with the middle crumb. How each crumb moves compared with the middle crumb is called its drift.

Above the ground, Earth's pull gets weaker the farther a crumb is from Earth's centre. One metre farther out, the pull is weaker by about 3 parts in 10 million. The crumb at the 6 is nearer Earth's centre than the middle crumb, so Earth pulls it a little harder. It falls ahead of the middle crumb, toward Earth's centre. The crumb at the 12 is pulled a little less, so it falls behind. Both drift away from the middle crumb, each by 0.154 millimetres in the ten seconds.

The crumbs at the 3 and the 9 lie across that line. Seen from the tower's wall, their paths and the middle crumb's path all point at Earth's centre, like spokes of a wheel. So the three paths lean toward each other. Back inside the cabin, the crumbs at the 3 and the 9 each drift in toward the middle crumb.

How far? Earth's pull on the crumb at the 3 points at Earth's centre, 6371 kilometres away, while that crumb sits only 1 metre across the line. By similar triangles, the part of that pull aimed sideways at the line is the same small fraction of the whole pull as 1 metre is of 6371 kilometres. That fraction is about 1.6 parts in 10 million. The middle crumb feels no sideways pull at all, so that sideways part is the whole difference between the two crumbs. For the crumbs on the line the difference in pull was 3 parts in 10 million, about twice as big. Over the same ten seconds, a drift is in proportion to the difference in pull that makes it. So the crumbs at the 3 and the 9 drift half as far: 0.077 millimetres.

Each of the other eight crumbs sits partly along the line and partly across it. So part of its drift is away along the line, and part is in toward the line. The way "Three numbers give every drift" shows how the two parts combine. The twelve crumbs end up on an oval, longer along the line toward Earth's centre and shorter across it.

The tidal tensor is a small table of numbers that gives this whole pattern: how a crumb let go anywhere near the middle crumb drifts.

The word tidal comes from the tides of the sea, which come from the same kind of difference in pull, mostly the Moon's. The Moon pulls the side of Earth facing it harder than Earth's centre, and the centre harder than the side facing away. So the sea bulges out on both sides, like the oval of crumbs. As Earth turns under the two bulges, most coasts get two high tides a day.

In Einstein's theory of gravity, the tidal tensor is one part of the Riemann curvature tensor. That part holds the numbers that crumbs drifting around a falling crumb can measure.

The pattern is tiny. A crumb 1 metre out drifts less than two tenths of a millimetre in ten seconds, about the width of two hairs. That is why you never notice the drift.

**Takeaway:** Near Earth, crumbs let go in a falling cabin drift away from the middle crumb along the line toward Earth's centre, and in toward that line from either side of it. So a ring set with that line through two of its crumbs becomes an oval.

*What this leaves out:* Treats Earth as a perfect ball that does not spin. Ignores the pull of the tower and of the crumbs on each other, and keeps the crumbs close together compared with Earth's size.

*Builds on:* [[geodesic-deviation-equation]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/crumbs-nearer-and-farther`

### 2. Three numbers give every drift · entry · calculation

*How can a few numbers give the drift of a crumb placed anywhere around the middle crumb?*

**Recap:** In a cabin falling freely near Earth, crumbs are let go with no push around a middle crumb. Each of them then drifts. Time them with the cabin's clock and measure them with a ruler fixed to the cabin. In ten seconds, a crumb 1 metre out on the line toward Earth's centre drifts away by 0.154 millimetres. A crumb 1 metre out across that line drifts in by 0.077 millimetres. Drifts are in proportion to the distance from the middle crumb. The table of numbers that gives the whole pattern is called the tidal tensor.

In "A ring of crumbs turns into an oval", eight of the twelve crumbs sit partly along the line toward Earth's centre and partly across it. This way shows how to find the drift of such a crumb.

Near a round planet like Earth, three directions at right angles to each other are special. One is the line toward Earth's centre. The other two are any two directions across that line, at right angles to each other. Any two will do, because a round planet looks the same all the way round that line. These three are called the main directions.

A crumb placed along a main direction drifts along that same direction. On the line toward Earth's centre, it drifts directly away from the middle crumb. Across the line, it drifts directly in toward the middle crumb.

Give each main direction its own number: how far a crumb 1 metre out drifts in ten seconds. Near Earth's surface, along the line it drifts away by 0.154 millimetres. Across the line, in either main direction, it drifts in by 0.077 millimetres.

Now take a crumb 5 metres from the middle crumb. It is 3 metres along the line toward Earth's centre, on the side farther from Earth, and 4 metres across that line. A right triangle with short sides of 3 and 4 metres has a long side of 5 metres. Only the along part changes how hard Earth pulls the crumb, compared with the middle crumb. Only the across part makes the crumb's path and the middle crumb's path lean toward each other, like spokes. So each part gives its own drift, and the crumb makes both of them at once.

The along part gives 3 times 0.154, which is 0.462 millimetres away from the middle crumb, along the line. The across part gives 4 times 0.077, which is 0.308 millimetres in toward the line. Making both drifts at once, the crumb does not drift directly away from the middle crumb, or directly toward it. Its drift slants in toward the line.

So three main directions, each with its own number, give the drift of a crumb let go anywhere nearby. Even this crumb, 5 metres out, drifts only about half a millimetre in ten seconds.

**Try it:** On squared paper, mark a middle dot and draw a line through it for the line toward Earth's centre. Mark a second dot 6 squares along the line and 8 squares across it. Near Earth, for each square of distance, the drift along the line is twice the drift across it. Keep that two-to-one, but make both drifts much bigger, so that you can draw them. Move the dot out along the line by 2 tenths of 6 squares, and in toward the line by 1 tenth of 8 squares. It lands 7.2 squares along and 7.2 squares across. Draw an arrow from the old dot to the new one: it slants toward the line instead of pointing directly away from the middle dot.

**Takeaway:** Near Earth, split a crumb's distance from the middle crumb into a part along the line toward Earth's centre and a part across that line. Each part gives its own drift, and the crumb makes both at once, so it can drift on a slant.

*What this leaves out:* Keeps crumbs close together compared with Earth's size, and treats Earth as a perfect ball that does not spin.

*Continues:* `ways_in/ring-of-crumbs-becomes-an-oval`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/crumb-three-along-four-across`

### 3. Feed the four-velocity in twice · working · calculation

*Which tensor turns a falling observer's separations into relative accelerations, and what structure does it inherit from the Riemann tensor?*

The rule of "Three numbers give every drift", split a separation along the main directions and give each part its own drift, is a symmetric matrix acting on the separation. The geodesic deviation equation supplies that matrix once its two four-velocity slots are grouped together:

$$\frac{D^2\xi^\mu}{d\tau^2} = -\big(R^\mu{}_{\alpha\nu\beta}\,u^\alpha u^\beta\big)\,\xi^\nu.$$

The bracket is the relativistic tidal tensor of the observer whose four-velocity is $u$. With $u_\mu u^\mu = -c^2$ its components have units of $\mathrm{s^{-2}}$: relative acceleration per unit separation. A positive value pulls neighbours back together, and a negative one pushes them apart.

The Riemann symmetries give its structure.

- Antisymmetry in the last pair makes $R^\mu{}_{\alpha\nu\beta}u^\alpha u^\beta u^\nu = 0$, and antisymmetry in the first pair makes $u_\mu R^\mu{}_{\alpha\nu\beta}u^\alpha u^\beta = 0$. Separations along $u$ feel nothing, and every relative acceleration is orthogonal to $u$.
- Pair exchange makes $R_{\mu\alpha\nu\beta}u^\alpha u^\beta$ symmetric in $\mu$ and $\nu$.
- In the observer's orthonormal frame, with $\hat e_{\hat 0} = u/c$, the tensor is therefore one real symmetric $3\times3$ matrix, $c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$. It has three orthogonal eigenvectors, the main directions, with real eigenvalues $\lambda_k$.

Along an eigenvector, $d^2\xi/d\tau^2 = -\lambda_k\xi$. While $\lambda_k$ stays constant, a positive eigenvalue makes the separation oscillate at frequency $\sqrt{\lambda_k}/2\pi$, like a mass on a spring, and a negative one makes neighbours released at rest separate as $\cosh(\sqrt{|\lambda_k|}\,\tau)$. The eigenvalues are not the lengths of the oval's axes. The eigenvectors fix the axes' directions, and each eigenvalue sets how fast its axis changes: $\ell \approx \ell_0\big(1 - \tfrac12\lambda_k\tau^2\big)$ for a cloud released at rest.

For a static weak field the tensor reduces to the Hessian of the Newtonian potential, $c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \partial_i\partial_j\Phi$. Outside a spherical mass, in the radial and two transverse directions, $\Phi = -GM/r$ gives $(GM/r^3)\,\mathrm{diag}(-2, 1, 1)$. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$, so a transverse neighbour released at rest 1 m away closes by $\tfrac12\lambda\tau^2\times(1\ \mathrm m) = 0.077$ mm in 10 s, the entry number.

By the course definition of the Ricci tensor, the trace is $R_{\alpha\beta}u^\alpha u^\beta$. The derivation "The trace from Einstein's equation" turns it into

$$R_{\alpha\beta}u^\alpha u^\beta = 4\pi G\Big(\rho + \frac{3p}{c^2}\Big) - \Lambda c^2$$

for a perfect fluid at rest relative to the observer. Outside matter, with $\Lambda = 0$, the trace vanishes, and indeed $-2 + 1 + 1 = 0$. Inside a uniform ball of density $\rho$, $\Phi$ is quadratic in $r$, and all three eigenvalues equal $4\pi G\rho/3$: every direction draws in.

**Takeaway:** Contracting the Riemann tensor twice with an observer's four-velocity gives a symmetric tensor of relative acceleration per separation, whose eigenvectors are the main directions and whose trace is a Ricci component.

*What this leaves out:* First order in the separation, for test particles released with small relative velocity; the Newtonian form needs a static weak field and slow motion.

*Continues:* `ways_in/three-numbers-give-every-drift`<br>*Builds on:* [[geodesic-deviation-equation]], [[orthonormal-frame]], [[newtonian-tidal-tensor]], [[ricci-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/trace-from-einstein-equation`, `problems/tides-inside-and-outside-a-planet`, `checks/pressure-adds-to-the-squeeze`

### 4. A passing observer reads other tides · working · operational

*Do two observers passing through the same event at different velocities measure the same tides?*

The tidal tensor of "Feed the four-velocity in twice" carries the observer's four-velocity in two slots. So two observers passing through one event with different four-velocities read different components of one Riemann tensor. Each measures her own with free test masses, radar timing and gyroscope axes carried along.

Take the spacetime outside a non-rotating spherical mass $M$, and a static observer with orthonormal frame $(\hat t, \hat r, \hat\theta, \hat\phi)$ at radius $r$. Write $q = GM/r^3$. Taken on trust here, the nonzero frame components, up to the Riemann symmetries, are $R_{\hat t\hat r\hat t\hat r} = -2q/c^2$, $R_{\hat t\hat\theta\hat t\hat\theta} = R_{\hat t\hat\phi\hat t\hat\phi} = q/c^2$, $R_{\hat\theta\hat\phi\hat\theta\hat\phi} = 2q/c^2$ and $R_{\hat r\hat\theta\hat r\hat\theta} = R_{\hat r\hat\phi\hat r\hat\phi} = -q/c^2$. The static observer's tidal tensor is $q\,\mathrm{diag}(-2, 1, 1)$, the Newtonian pattern, here exact.

A second, freely falling observer passes the same event moving along $\hat e_{\hat\phi}$ at speed $v = \beta c$ relative to the static one, so $u' = \gamma c\,(\hat e_{\hat t} + \beta\,\hat e_{\hat\phi})$. The derivation "Tides for a sideways passer" gives her tidal tensor, diagonal in the radial, polar and motion directions:

$$q\,\mathrm{diag}\big({-\gamma^2(2 + \beta^2)},\ \gamma^2(1 + 2\beta^2),\ 1\big).$$

The trace stays zero, as it must for every observer in vacuum. The radial and polar entries grow roughly as $\gamma^2$, while the entry along her motion is unchanged. An observer falling radially through the event instead measures exactly the static pattern, as the worked example "A radial faller agrees" shows.

At everyday speeds the difference is far too small to measure. In low Earth orbit $\beta^2\gamma^2 \approx 7\times10^{-10}$, so one Newtonian matrix serves every slow observer. Just outside a neutron star, orbits reach about half the speed of light relative to static observers, and at that speed a sideways passer's polar entry is twice the static one and her radial entry one and a half times it.

Around a mass there is no single tidal field that all observers share. What they share is the Riemann tensor, from which each reads her own tidal tensor.

**Takeaway:** The tidal tensor depends on who measures: moving sideways past a mass strengthens the radial and polar tides, though every observer reads one Riemann tensor.

*What this leaves out:* Non-rotating spherical mass in vacuum; both observers are compared at a single event.

*Continues:* `ways_in/feed-the-four-velocity-in-twice`<br>*Builds on:* [[lorentz-transformation]], [[orthonormal-frame]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `derivations/tides-for-a-sideways-passer`, `worked_examples/a-radial-faller-agrees`, `checks/polar-entry-ten-times`

### 5. The tidal operator: structure, split and reach · formal · structure

*What exactly is an observer's tidal operator, what does it determine, and where does it describe real bodies?*

The symmetric matrix of "Feed the four-velocity in twice" is the restriction of a linear map whose properties follow from the Riemann symmetries alone. Set $G = c = 1$. At a point $p$ of a spacetime $(M, g)$ with its Levi-Civita connection, let $u$ be a unit timelike vector with rest space $u^\perp$. With $\mathcal{R}(X,Y) = [\nabla_X,\nabla_Y] - \nabla_{[X,Y]}$, the tidal operator of $u$ is $X \mapsto \mathcal{R}(X,u)u$, with components $R^\mu{}_{\alpha\nu\beta}u^\alpha u^\beta X^\nu$, and the Jacobi equation reads $D_\tau^2J = -\mathcal{R}(J,u)u$.

*Proposition.* (i) $\mathcal{R}(u,u)u = 0$ and $g(u, \mathcal{R}(X,u)u) = 0$, so the operator maps $u^\perp$ into itself. (ii) $g(Y, \mathcal{R}(X,u)u) = g(X, \mathcal{R}(Y,u)u)$. (iii) On the Euclidean space $u^\perp$ it has an orthonormal eigenbasis $e_k$ with real eigenvalues $\lambda_k = -K(u, e_k)$, where $K$ is the sectional curvature in the course convention. *Sketch:* (i) antisymmetry in each pair; (ii) pair exchange; (iii) the spectral theorem, with $R(e,u,e,u) = K(e,u)\,[g(e,e)g(u,u) - g(e,u)^2] = -K(e,u)$ for a unit $e \perp u$.

*Trace.* The trace is $R_{\alpha\beta}u^\alpha u^\beta = 8\pi\big(T_{\alpha\beta}u^\alpha u^\beta + \tfrac12 T^\alpha{}_\alpha\big) - \Lambda$. With $\Lambda = 0$, the strong energy condition is exactly the statement that this trace is non-negative for every observer: net focusing.

*Split.* In four dimensions, with $h_{\mu\nu} = g_{\mu\nu} + u_\mu u_\nu$ and $R_{uu} = R_{\alpha\beta}u^\alpha u^\beta$, the Weyl decomposition contracted twice with $u$ gives

$$R_{\mu\alpha\nu\beta}u^\alpha u^\beta = C_{\mu\alpha\nu\beta}u^\alpha u^\beta + \tfrac12\big(R_{uu}\,h_{\mu\nu} - h_\mu{}^\rho h_\nu{}^\sigma R_{\rho\sigma}\big) + \tfrac16 R\,h_{\mu\nu}.$$

The first term, the electric part of the Weyl tensor, is symmetric, orthogonal to $u$ and trace-free. With $R_{\mu\nu} = 0$ it is the whole operator. With $R_{\mu\nu} = \Lambda g_{\mu\nu}$ the operator is that electric part minus $(\Lambda/3)h_{\mu\nu}$.

*Reach of one observer.* The operator on $u^\perp$ carries 6 of the 20 independent Riemann components at $p$; in general the frame components $R_{\hat 0\hat\imath\hat\jmath\hat k}$ and $R_{\hat\imath\hat\jmath\hat k\hat l}$ are not fixed by it. The operators of all observers at $p$ do fix the whole tensor. They give $F(X,Y) = R(X,Y,X,Y)$ for every timelike $Y$, an open set, so the polynomial $F$ is known everywhere, and an algebraic curvature tensor is recovered from $F$ by polarization with the first Bianchi identity. In vacuum the electric part holds 5 components, and the magnetic part of the Weyl tensor, built from $C_{\hat 0\hat\imath\hat\jmath\hat k}$, holds the other 5; it governs the differential precession of neighbouring gyroscopes.

*Local frame.* In Fermi normal coordinates along the observer's geodesic, built on gyroscope axes, $g_{00} = -1 - R_{\hat 0\hat\imath\hat 0\hat\jmath}x^ix^j + O(x^3)$. Slow free particles move in the tidal potential $\tfrac12R_{\hat 0\hat\imath\hat 0\hat\jmath}x^ix^j$, which in a weak static field is the quadratic Taylor term of $\Phi$ about the worldline.

*Limits.* The operator describes test bodies whose separation $\ell$ is small compared with the curvature radius $|R|^{-1/2}$ and with the scale on which curvature varies. Relative velocities enter only at the next order, and a rotating frame adds centrifugal and Coriolis terms. A body with its own gravity also deforms, which its tidal deformability measures.

**Takeaway:** An observer's tidal operator is a self-adjoint map of her rest space whose eigenvalues are minus sectional curvatures; it is Weyl-electric plus Ricci terms, carries 6 of 20 components, and all observers together fix the Riemann tensor.

*Picture:* In one observer's rest space, a small sphere of directions deformed into an ellipsoid along the operator's eigenvectors; tilting her time axis changes the ellipsoid, while the Riemann tensor behind it stays fixed.

*What this leaves out:* Levi-Civita connection in four dimensions; test bodies and a nonrotating frame.

*Continues:* `ways_in/feed-the-four-velocity-in-twice`, `ways_in/a-passing-observer-reads-other-tides`<br>*Builds on:* [[weyl-tensor]], [[einstein-field-equations]]<br>*See:* `checks/one-observer-six-numbers`, `checks/where-lambda-wins`, `problems/tides-in-fermi-coordinates`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| drift | — | How a crumb moves compared with a middle crumb after both are let go with no push, measured with a ruler fixed to the falling cabin. | — |
| tidal tensor | TIE-dul TEN-ser | A small table of numbers, for someone falling freely, that gives the drift of a crumb let go anywhere near them, in any direction. | [[relativistic-tidal-tensor]] |
| main directions | — | Three directions at right angles to each other along which a crumb drifts directly away from the middle crumb, or directly toward it. | — |
| Riemann curvature tensor | REE-mahn | A table of numbers, kept at every place, that describes the curving of space and time there. Crumbs drifting around a falling crumb measure some of its numbers. | [[riemann-curvature-tensor]] |

## Key equations

### Tidal tensor in the deviation equation · working

$$
\frac{D^2\xi^\mu}{d\tau^2} = -\big(R^\mu{}_{\alpha\nu\beta}\,u^\alpha u^\beta\big)\,\xi^\nu
$$

The relative acceleration of a neighbour is minus the tidal tensor, the Riemann tensor fed the observer's four-velocity twice, acting on the separation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\xi^\nu$ | separation vector to the neighbour | xi |
| $u^\alpha$ | four-velocity of the freely falling observer, $u_\mu u^\mu = -c^2$ | u |
| $R^\mu{}_{\alpha\nu\beta}\,u^\alpha u^\beta$ | the relativistic tidal tensor, in $\mathrm{s^{-2}}$; positive eigenvalues pull neighbours together | the tidal tensor |

**Holds when:** Freely falling observer; test particles; first order in separation and relative velocity; course Riemann convention.  
**Say it:** “The relative acceleration is minus the Riemann tensor, fed the four-velocity twice, acting on the separation.”  
**Justified by:** `geodesic-deviation-equation`

### Weak-field tidal tensor · working

$$
c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \frac{\partial^2\Phi}{\partial x^i\,\partial x^j}
$$

In a static weak field, an observer's tidal tensor is the Hessian of the Newtonian potential.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Phi$ | Newtonian potential, $-GM/r$ outside a spherical mass | phi |
| $R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$ | frame components with the observer's time direction in slots two and four | the Riemann components i zero j zero |

**Holds when:** Static weak field, slow observer, first order in $\Phi/c^2$.  
**Say it:** “c squared times the Riemann components i zero j zero is about the second derivatives of the potential.”  
**Justified by:** `geodesic-deviation-equation`

### Trace of the tidal tensor · working

$$
R^\mu{}_{\alpha\mu\beta}u^\alpha u^\beta = R_{\alpha\beta}u^\alpha u^\beta = 4\pi G\Big(\rho + \frac{3p}{c^2}\Big) - \Lambda c^2
$$

The sum of the eigenvalues is a Ricci component, set by the local density, pressure and cosmological constant.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\rho$ | mass density of the fluid in its rest frame | rho |
| $p$ | pressure | p |
| $\Lambda$ | cosmological constant | lambda |

**Holds when:** Einstein's equation; perfect fluid at rest relative to the observer; $u_\mu u^\mu = -c^2$.  
**Say it:** “The trace of the tidal tensor is four pi G times the density plus three times the pressure over c squared, minus lambda c squared.”  
**Justified by:** `derivations/trace-from-einstein-equation`

### Tides for an observer moving sideways past a mass · working

$$
\frac{GM}{r^3}\,\mathrm{diag}\big({-\gamma^2(2+\beta^2)},\ \gamma^2(1+2\beta^2),\ 1\big)
$$

Tidal tensor, in the radial, polar and motion directions, of an observer moving at $\beta c$ along $\hat e_{\hat\phi}$ past a static observer outside a spherical mass.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\beta$ | speed relative to the static observer, in units of $c$ | beta |
| $\gamma$ | Lorentz factor $(1 - \beta^2)^{-1/2}$ | gamma |

**Holds when:** Vacuum outside a non-rotating spherical mass; motion along $\hat e_{\hat\phi}$ at the event; Schwarzschild frame components taken on trust.  
**Say it:** “G M over r cubed times a diagonal matrix: minus gamma squared times two plus beta squared, gamma squared times one plus two beta squared, and one.”  
**Justified by:** `derivations/tides-for-a-sideways-passer`

## Derivations

### The trace from Einstein's equation · working

**Goal:** Show that $R_{\alpha\beta}u^\alpha u^\beta = 4\pi G(\rho + 3p/c^2) - \Lambda c^2$ for a perfect fluid at rest relative to the observer.

1. The course Ricci tensor is $R_{\alpha\beta} = R^\mu{}_{\alpha\mu\beta}$, so the trace of the tidal tensor is $R_{\alpha\beta}u^\alpha u^\beta$.
2. Take the trace of $G_{\mu\nu} + \Lambda g_{\mu\nu} = \kappa T_{\mu\nu}$, with $\kappa = 8\pi G/c^4$: $-R + 4\Lambda = \kappa T$, where $T = T^\mu{}_\mu$.
3. Substitute $R = 4\Lambda - \kappa T$ back: $R_{\mu\nu} = \kappa\big(T_{\mu\nu} - \tfrac12 T g_{\mu\nu}\big) + \Lambda g_{\mu\nu}$.
4. For $T^{\mu\nu} = (\rho + p/c^2)u^\mu u^\nu + p g^{\mu\nu}$ with the observer's own $u$: $T_{\mu\nu}u^\mu u^\nu = (\rho + p/c^2)c^4 - pc^2 = \rho c^4$, and $T = -\rho c^2 + 3p$.
5. With $g_{\mu\nu}u^\mu u^\nu = -c^2$: $-\tfrac12 T g_{\mu\nu}u^\mu u^\nu = -\tfrac12\rho c^4 + \tfrac32 pc^2$.
6. Add: $R_{\mu\nu}u^\mu u^\nu = \kappa\big(\tfrac12\rho c^4 + \tfrac32 pc^2\big) - \Lambda c^2 = 4\pi G(\rho + 3p/c^2) - \Lambda c^2$.

**Result:** $R_{\alpha\beta}u^\alpha u^\beta = 4\pi G(\rho + 3p/c^2) - \Lambda c^2$; for dust with $\Lambda = 0$ it is $4\pi G\rho = \nabla^2\Phi$.

### Tides for a sideways passer · working

**Goal:** Find the tidal tensor of an observer moving at $\beta c$ along $\hat e_{\hat\phi}$ past a static observer outside a spherical mass.

1. The boosted orthonormal frame is $\hat e_{\hat 0'} = \gamma(\hat e_{\hat t} + \beta\hat e_{\hat\phi})$, $\hat e_{\hat\phi'} = \gamma(\beta\hat e_{\hat t} + \hat e_{\hat\phi})$, $\hat e_{\hat r'} = \hat e_{\hat r}$ and $\hat e_{\hat\theta'} = \hat e_{\hat\theta}$; the tidal tensor is $c^2R_{\hat\imath'\hat 0'\hat\jmath'\hat 0'}$.
2. Radial: $R_{\hat r\hat 0'\hat r\hat 0'} = \gamma^2\big(R_{\hat r\hat t\hat r\hat t} + \beta^2R_{\hat r\hat\phi\hat r\hat\phi}\big)$; the cross term $R_{\hat r\hat t\hat r\hat\phi}$ vanishes. Antisymmetry within each index pair flips the sign twice, so $R_{\hat r\hat t\hat r\hat t} = R_{\hat t\hat r\hat t\hat r} = -2q/c^2$; multiplying by $c^2$ gives the entry $-\gamma^2(2 + \beta^2)q$.
3. Polar: $\gamma^2\big(R_{\hat\theta\hat t\hat\theta\hat t} + \beta^2R_{\hat\theta\hat\phi\hat\theta\hat\phi}\big) = \gamma^2(1 + 2\beta^2)q/c^2$.
4. Along the motion: $\hat e_{\hat\phi'}\wedge\hat e_{\hat 0'} = \gamma^2(1 - \beta^2)\,\hat e_{\hat\phi}\wedge\hat e_{\hat t} = \hat e_{\hat\phi}\wedge\hat e_{\hat t}$, and the Riemann tensor depends on each pair only through this wedge, so the entry stays $q/c^2$.
5. Every off-diagonal entry involves a static-frame component such as $R_{\hat r\hat t\hat\theta\hat t}$ or $R_{\hat r\hat t\hat\phi\hat t}$, which vanish, so the matrix stays diagonal.
6. Check the trace: $-\gamma^2(2 + \beta^2) + \gamma^2(1 + 2\beta^2) + 1 = -\gamma^2(1 - \beta^2) + 1 = 0$.

**Result:** $q\,\mathrm{diag}\big(-\gamma^2(2+\beta^2),\ \gamma^2(1+2\beta^2),\ 1\big)$ with $q = GM/r^3$, trace-free as vacuum requires.

## Worked examples

### A radial faller agrees · working

**Problem:** Outside a spherical mass, a static observer measures the tidal tensor $q\,\mathrm{diag}(-2, 1, 1)$ with $q = GM/r^3$. A freely falling observer passes the same event moving radially inward at $0.6c$ relative to her. Using the static frame components of "A passing observer reads other tides", find the falling observer's tidal tensor.

1. For a radial boost, $\beta = 0.6$ and $\gamma^2 = 1/(1 - 0.36) = 1.5625$. The new time and radial axes are combinations of $\hat e_{\hat t}$ and $\hat e_{\hat r}$, so $\hat e_{\hat r'}\wedge\hat e_{\hat 0'} = \hat e_{\hat r}\wedge\hat e_{\hat t}$ and the radial entry stays $-2q$.
2. Polar: $\hat e_{\hat 0'} = \gamma(\hat e_{\hat t} - \beta\hat e_{\hat r})$ for inward motion, so the entry is $\gamma^2\big(R_{\hat\theta\hat t\hat\theta\hat t} + \beta^2R_{\hat\theta\hat r\hat\theta\hat r}\big)c^2 = \gamma^2(1 - \beta^2)q$; the cross term $R_{\hat\theta\hat t\hat\theta\hat r}$ vanishes.
3. Numerically $1.5625 \times 0.64 = 1$, so the polar entry is $q$, and the azimuthal entry is $q$ by the same steps.
4. The sign of $\beta$ enters only through $\beta^2$, so an outward faller agrees too.

**Answer:** $q\,\mathrm{diag}(-2, 1, 1)$: exactly the static observer's tidal tensor, at any radial speed.

**Takeaway:** Boosts along the radial line leave these tides unchanged; only motion across that line changes what an observer measures.

## Problems

### `ring-for-a-millimetre-difference` · entry · difficulty 2 · calculation

In a cabin falling freely near Earth, a ring of crumbs is held around a middle crumb, set so that the line toward Earth's centre passes through two of its crumbs. All the crumbs are let go with no push. After ten seconds by the cabin's clock, you want the oval's width along that line to be 1 millimetre more than its width across that line. In ten seconds, a crumb 1 metre out along the line drifts away from the middle crumb by 0.154 millimetres. A crumb 1 metre out across it drifts in by 0.077 millimetres. How wide must the ring be at the start, measured right across through the middle crumb?

**Hints**

1. How much longer does the ring get along the line, for each metre of its width?
2. How much shorter does it get across the line, for each metre of its width?

**Answer:** About 4.3 metres across. Each metre of width makes the ring 0.154 millimetres longer along the line. It also makes the ring 0.077 millimetres shorter across it. So for each metre of starting width, the difference between the two widths grows by 0.231 millimetres. One millimetre divided by 0.231 millimetres is about 4.3.

**Must contain:** Width along the line grows by 0.154 millimetres per metre of width; Width across shrinks by 0.077 millimetres per metre of width; The difference, 0.231 millimetres per metre of starting width, needs a ring about 4.3 metres wide

**Numeric:** starting width of the ring = 4.33 m (magnitude, ±3%)

**Solution**

1. A ring 1 metre wide has an end crumb half a metre out on each side of the middle crumb, along the line. Each drifts away by half of 0.154 millimetres, so that width grows by 0.154 millimetres.
2. Across the line, the same reasoning makes a ring 1 metre wide 0.077 millimetres narrower.
3. Drifts are in proportion to the distance from the middle crumb, so a wider ring changes by that many times more. For each metre of starting width, the difference between the two widths grows by 0.154 plus 0.077, which is 0.231 millimetres.
4. One millimetre divided by 0.231 millimetres is about 4.33, so the ring must start about 4.3 metres wide.

### `tides-inside-and-outside-a-planet` · working · difficulty 2 · calculation

Treat a planet as a uniform ball of radius $R$ and density $\rho$, with $\Phi = -GM/r$ outside and $\Phi = (2\pi G\rho/3)(r^2 - 3R^2)$ inside. (a) Find the eigenvalues of the weak-field tidal tensor $\partial_i\partial_j\Phi$ for a slow freely falling observer just outside the surface and just inside it, in units of $GM/R^3$. (b) Check both traces against $4\pi G(\rho + 3p/c^2)$ with $p \approx 0$. (c) Which eigenvalue jumps at the surface, and by how much for $\rho = 5510\ \mathrm{kg\,m^{-3}}$?

**Hints**

1. For a function of $r$ alone, the radial eigenvalue is $\Phi''(r)$ and each transverse eigenvalue is $\Phi'(r)/r$.
2. Use $GM/R^3 = 4\pi G\rho/3$.

**Answer:** (a) Outside: $(-2, 1, 1)$; inside: $(1, 1, 1)$. (b) The outside trace is 0; the inside trace is $3 \times 4\pi G\rho/3 = 4\pi G\rho$. (c) The radial eigenvalue jumps by $3\,GM/R^3 = 4\pi G\rho = 4.62\times10^{-6}\ \mathrm{s^{-2}}$; the transverse ones are continuous.

**Must contain:** Outside eigenvalues minus two, one, one; inside all equal to one, in units of G M over R cubed; Traces zero outside and four pi G rho inside; Only the radial eigenvalue jumps, by four pi G rho

**Numeric:** radial eigenvalue just outside, in units of G M over R cubed = -2 1 (signed, ±0.01); radial eigenvalue just inside, in units of G M over R cubed = 1 1 (signed, ±0.01)

**Solution**

1. For $\Phi(r)$, $\partial_i\partial_j\Phi = \Phi''\,\hat r_i\hat r_j + (\Phi'/r)(\delta_{ij} - \hat r_i\hat r_j)$, so the radial eigenvalue is $\Phi''$ and the two transverse ones are $\Phi'/r$.
2. Outside, $\Phi' = GM/r^2$ and $\Phi'' = -2GM/r^3$: at $r = R$ the eigenvalues are $(-2, 1, 1)\,GM/R^3$.
3. Inside, $\Phi' = 4\pi G\rho r/3$ and $\Phi'' = 4\pi G\rho/3$. With $M = 4\pi R^3\rho/3$ this is $GM/R^3$, so all three eigenvalues are $(1, 1, 1)\,GM/R^3$.
4. The traces are $0$ and $4\pi G\rho$, matching $4\pi G(\rho + 3p/c^2)$ with $\rho = 0$ outside and $p$ negligible inside.
5. The transverse eigenvalue is $GM/R^3$ on both sides. The radial one goes from $-2$ to $+1$ in units of $GM/R^3$, a jump of $3GM/R^3 = 4\pi G\rho = 4\pi(6.674\times10^{-11})(5510) = 4.62\times10^{-6}\ \mathrm{s^{-2}}$, the trace jump required by the density.

### `tides-in-fermi-coordinates` · formal · difficulty 3 · derivation

Set $G = c = 1$. Fermi normal coordinates along a freely falling observer's geodesic, built on gyroscope axes, have $g_{00} = -1 - R_{\hat 0\hat\imath\hat 0\hat\jmath}x^ix^j + O(x^3)$, $g_{0i} = O(x^2)$ and $g_{ij} = \delta_{ij} + O(x^2)$, with the curvature evaluated on the worldline. (a) Show that a particle momentarily at rest at small $x^i$ has $d^2x^i/dt^2 = -R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}x^j$ to first order in $x$. (b) Show that this is motion in the potential $\tfrac12R_{\hat 0\hat\imath\hat 0\hat\jmath}x^ix^j$, and relate it to $\Phi$ in a weak static field.

**Hints**

1. Only $\Gamma^i{}_{00}$ matters at first order for a particle at rest.
2. Time derivatives of $g_{0i}$ are second order in $x$.

**Answer:** (a) $\Gamma^i{}_{00} = R_{\hat 0\hat\imath\hat 0\hat\jmath}x^j + O(x^2)$, so $d^2x^i/dt^2 = -R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}x^j$. (b) Minus the gradient of $\tfrac12R_{\hat 0\hat\imath\hat 0\hat\jmath}x^ix^j$ gives that acceleration; in a weak static field it is $\tfrac12\partial_i\partial_j\Phi\,x^ix^j$, the quadratic Taylor term of $\Phi$.

**Must contain:** Gamma i zero zero equals the Riemann components zero i zero j times x j; The tidal potential is one half R zero i zero j x i x j, the quadratic Taylor term of phi

**Solution**

1. The geodesic equation gives $d^2x^i/d\tau^2 = -\Gamma^i{}_{\alpha\beta}u^\alpha u^\beta$. At rest $u^j = 0$ and $u^0 = 1 + O(x^2)$, and $dt = d\tau\,(1 + O(x^2))$, so $d^2x^i/dt^2 = -\Gamma^i{}_{00} + O(x^2)$.
2. $\Gamma^i{}_{00} = \tfrac12 g^{ik}\big(2\partial_0 g_{k0} - \partial_k g_{00}\big)$. The first term is $O(x^2)$ and $g^{ik} = \delta^{ik} + O(x^2)$.
3. $\partial_k g_{00} = -2R_{\hat 0\hat k\hat 0\hat\jmath}x^j$, using the symmetry of $R_{\hat 0\hat k\hat 0\hat\jmath}$ in $k$ and $j$ from pair exchange. So $\Gamma^i{}_{00} = R_{\hat 0\hat\imath\hat 0\hat\jmath}x^j$.
4. Two sign flips give $R_{\hat 0\hat\imath\hat 0\hat\jmath} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$, and spatial indices are raised with $\delta$, so $d^2x^i/dt^2 = -R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}x^j$.
5. $-\partial_i\big(\tfrac12R_{\hat 0\hat k\hat 0\hat\jmath}x^kx^j\big) = -R_{\hat 0\hat\imath\hat 0\hat\jmath}x^j$, the same acceleration, and $g_{00} = -(1 + 2\Phi_{\rm tid})$ matches the course weak-field form. In a weak static field $R_{\hat 0\hat\imath\hat 0\hat\jmath} \approx \partial_i\partial_j\Phi$: the tidal potential is the quadratic Taylor term of $\Phi$, and free fall has removed the constant and linear terms.

## Observations

- **Gravity gradients measured by the GOCE satellite, 2009 to 2013** (measured, working). GOCE carried pairs of accelerometers 0.5 m apart along three perpendicular arms, about 255 km above Earth. Once the satellite's own rotation is removed, the acceleration differences per metre are entries of a slow freely falling observer's tidal tensor, in its Newtonian form $\partial_i\partial_j\Phi$. Outside Earth's mass the three diagonal entries in any orthonormal frame must add to zero, the vacuum statement that the trace vanishes. *Numbers:* For a spherical Earth at 255 km, the course sign gives a radial entry of $-2GM/r^3 = -2.74\times10^{-6}\ \mathrm{s^{-2}}$ and transverse entries of $+1.37\times10^{-6}\ \mathrm{s^{-2}}$. Geodesists write gradients of a potential of the opposite sign, so they quote the radial value as about $+2740$ eötvös, where one eötvös is $10^{-9}\ \mathrm{s^{-2}}$. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **The oscillating tidal tensor of the gravitational wave GW150914 at the LIGO detectors** (measured, working). At the signal's frequencies each suspended end mirror moves along its arm like a free test mass. The wave's tidal tensor there is trace-free and transverse to its direction of travel, with entries $-\tfrac12\ddot h$ built from the strain; the mirrors hang in vacuum, where the Ricci tensor vanishes, so these tides are pure electric Weyl curvature. *Numbers:* Peak strain $1.0\times10^{-21}$ at about 150 Hz gives tidal entries of amplitude $\tfrac12h(2\pi f)^2 = 4.4\times10^{-16}\ \mathrm{s^{-2}}$, about 3.5 billion times smaller than Earth's transverse entry at its surface. It was detectable because it oscillates at a frequency where the detector's noise was low. *Reference:* B. P. Abbott and others (2016), *Observation of Gravitational Waves from a Binary Black Hole Merger*, Physical Review Letters 116, 061102, doi:10.1103/PhysRevLett.116.061102

## Teaching arc

1. **Predict the ring** (entry). Set up the clock-face ring in the falling cabin, ask what the nearer and farther crumbs do, then reveal the oval. *Why:* Most learners expect the farther crumb to close in. *Predict:* Does the crumb farther from Earth's centre drift toward the middle crumb or away from it? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/ring-of-crumbs-becomes-an-oval`, `checks/crumbs-nearer-and-farther`
2. **Split a crumb's place** (entry). Have the learner split the crumb 3 metres along and 4 metres across into parts and add the two drifts. *Why:* The slanted drift shows why one number per direction is not enough. *Uses:* `ways_in/three-numbers-give-every-drift`, `checks/crumb-three-along-four-across`
3. **Build the tensor and change the observer** (working). Group the four-velocity slots, read the structure and the trace, then boost the observer radially and sideways. *Why:* Every property comes from a Riemann symmetry, and the boost shows that tides depend on who measures. *Predict:* At equal mass density, does a gas of light focus a released cloud more or less than dust? *Uses:* `ways_in/feed-the-four-velocity-in-twice`, `checks/pressure-adds-to-the-squeeze`, `ways_in/a-passing-observer-reads-other-tides`, `checks/polar-entry-ten-times`
4. **Mark structure and reach** (formal). State the operator's spectrum and split, show what one observer cannot see, and derive the tidal potential of a falling laboratory. *Why:* Graduate readers need what the operator determines and where the test-body picture ends. *Uses:* `ways_in/the-tidal-operator-and-its-reach`, `checks/one-observer-six-numbers`, `checks/where-lambda-wins`, `problems/tides-in-fermi-coordinates`

## Misconceptions

### “Earth pulls everything toward it, so the crumb farther from Earth should drift toward the middle crumb.” · entry · `far-crumb-closes-in`

- **Why it is tempting:** Everything in the cabin falls toward Earth.
- **What is true:** Inside the falling cabin only differences in pull show. The farther crumb is pulled a little less than the middle crumb, so it falls behind and drifts away from it.
- **Exposed by:** `checks/crumbs-nearer-and-farther`

### “Every crumb drifts directly toward the middle crumb or directly away from it.” · entry · `drift-straight-out-or-in`

- **Why it is tempting:** The crumbs on the line toward Earth's centre, and those across it, do exactly that.
- **What is true:** A crumb that sits partly along the line and partly across it gets one drift for each part, and together they point on a slant.
- **Exposed by:** `checks/crumb-three-along-four-across`

### “Pressure pushes outward, so at equal density a hot gas focuses a released cloud less than cold dust does.” · working · `pressure-cannot-pull`

- **Why it is tempting:** In a container, pressure is the push that holds things apart.
- **What is true:** The trace of the tidal tensor is set by the density plus three times the pressure over c squared, so positive pressure adds to the focusing. A gas of light focuses twice as strongly as dust of the same mass density.
- **Exposed by:** `checks/pressure-adds-to-the-squeeze`

### “Tides belong to a place, so everyone passing through an event measures the same tidal tensor.” · working · `same-tides-for-every-observer`

- **Why it is tempting:** In Newtonian gravity the tidal matrix is the Hessian of a potential that depends only on position.
- **What is true:** The tidal tensor contains the observer's four-velocity twice, so observers moving differently read different Riemann components. Sideways motion past a mass strengthens the radial and polar tides.
- **Exposed by:** `checks/polar-entry-ten-times`

### “With enough test masses, one freely falling observer can measure every component of the Riemann tensor at an event.” · formal · `one-observer-reads-all-curvature`

- **Why it is tempting:** Relative accelerations of released particles are presented as the operational meaning of curvature.
- **What is true:** One observer's released test masses fix only the 6 components of her tidal operator, and a curved spacetime can give her a zero operator. The operators of all observers at the event together fix the Riemann tensor.
- **Exposed by:** `checks/one-observer-six-numbers`

## Checks

1. **Entry · predict** `checks/crumbs-nearer-and-farther`. A cabin falls freely inside a tall hollow tower on Earth, with the air pumped out. Inside, three crumbs are held still, relative to the cabin, in a row on the line toward Earth's centre. One is the middle crumb, one is 1 metre nearer Earth's centre, and one is 1 metre farther. All three are let go together with no push. A friend says the farther crumb will drift toward the middle crumb, because Earth pulls everything toward Earth's centre. Using the cabin's clock and a ruler fixed to the cabin, what does each outer crumb do in ten seconds?
   - **Hints:** Which of the three crumbs does Earth pull hardest?
   - **Answer:** Both outer crumbs drift away from the middle crumb, each by about 0.154 millimetres. Above the ground, Earth's pull gets weaker the farther a crumb is from Earth's centre. The nearer crumb is pulled a little harder than the middle crumb, so it falls ahead of the middle crumb, toward Earth's centre. Earth does pull the farther crumb toward Earth's centre, as the friend says. But Earth pulls the middle crumb a little harder, so the farther crumb falls behind. Inside the cabin, falling ahead and falling behind both mean drifting away from the middle crumb. So the friend is wrong, and the row of crumbs gets longer by about 0.31 millimetres.
   - **Must contain:** Both outer crumbs drift away from the middle crumb; The nearer crumb is pulled harder and falls ahead; the farther one is pulled less and falls behind; About 0.154 millimetres each in ten seconds
   - **Numeric:** drift of each outer crumb away from the middle crumb = 0.154 mm (magnitude, ±5%)
   - **Targets:** `far-crumb-closes-in`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · numeric** `checks/crumb-three-along-four-across`. In a cabin falling freely near Earth, a crumb is held still, relative to the cabin, 5 metres from a middle crumb. It is 3 metres along the line toward Earth's centre, on the side farther from Earth, and 4 metres across that line. Both are let go with no push. In ten seconds by the cabin's clock, a crumb 1 metre out along the line drifts away by 0.154 millimetres. A crumb 1 metre out across it drifts in by 0.077 millimetres. How far does the 5-metre crumb drift along the line, and how far across? Does it drift directly away from the middle crumb?
   - **Hints:** Treat the 3 metres along and the 4 metres across as two separate crumbs, then add their drifts.
   - **Answer:** About 0.462 millimetres away from the middle crumb along the line, and 0.308 millimetres in toward the line. Only the along part of its place changes how hard Earth pulls it, compared with the middle crumb. That part is 3 metres, so its drift along the line is 3 times 0.154 millimetres. Only the across part makes the two paths lean like spokes. That part is 4 metres, so its drift across is 4 times 0.077 millimetres, inward. The crumb makes both drifts together. Moving out along the line while moving in across it is a slant, so the crumb does not drift directly away from the middle crumb.
   - **Must contain:** Split the place into 3 metres along and 4 metres across; About 0.462 millimetres out along the line and 0.308 millimetres in across it; The drift slants toward the line instead of pointing directly away
   - **Numeric:** drift along the line = 0.462 mm (magnitude, ±5%); drift across the line = 0.308 mm (magnitude, ±5%)
   - **Targets:** `drift-straight-out-or-in`
3. **Working · evaluate-claim** `checks/pressure-adds-to-the-squeeze`. A student says: pressure pushes outward, so a hot gas of light with pressure $p = \rho c^2/3$ must focus a small cloud of released test particles less than cold dust of the same mass density $\rho$. Using the trace of the tidal tensor for an observer at rest in each fluid, with $\Lambda = 0$, evaluate the claim and give the ratio of the two traces.
   - **Hints:** Substitute $p = \rho c^2/3$ into $\rho + 3p/c^2$.
   - **Answer:** The claim is wrong. The trace is $4\pi G(\rho + 3p/c^2)$. For dust $p = 0$, giving $4\pi G\rho$. For the gas of light $3p/c^2 = \rho$, giving $8\pi G\rho$. The trace sets the net pulling together of released neighbours, so the gas of light focuses twice as strongly. In Einstein's equation pressure is a source of gravity like energy density; the outward push acts between the fluid's own parts, not on free test particles passing through.
   - **Must contain:** The trace is four pi G times rho plus three p over c squared; A gas of light gives eight pi G rho, dust gives four pi G rho; The ratio is two: pressure adds to the focusing
   - **Numeric:** trace for light divided by trace for dust = 2 1 (magnitude, ±0.01)
   - **Targets:** `pressure-cannot-pull`
4. **Working · numeric** `checks/polar-entry-ten-times`. Outside a spherical mass, a static observer's tidal tensor is $q\,\mathrm{diag}(-2, 1, 1)$ in the radial and two transverse directions, with $q = GM/r^3$. A freely falling observer passes the same event moving along $\hat e_{\hat\phi}$. Her tidal tensor is $q\,\mathrm{diag}\big({-\gamma^2(2+\beta^2)},\ \gamma^2(1+2\beta^2),\ 1\big)$ in the radial, polar and motion directions. At what speed relative to the static observer is her polar entry ten times the static value? What is her radial entry then, and does her trace still vanish?
   - **Hints:** Replace $\gamma^2$ by $1/(1-\beta^2)$ and solve for $\beta^2$.
   - **Answer:** Set $\gamma^2(1 + 2\beta^2) = 10$ with $\gamma^2 = 1/(1 - \beta^2)$: $1 + 2\beta^2 = 10 - 10\beta^2$, so $\beta^2 = 3/4$ and $v = 0.866c$. Then $\gamma^2 = 4$, and the radial entry is $-4(2 + 0.75)q = -11q$, against $-2q$ for the static observer. The trace is $-11 + 10 + 1 = 0$, as vacuum requires for every observer. Two observers at one event thus disagree by more than a factor of five on radial tides, while the entry along her motion is the same for both.
   - **Must contain:** Beta squared equals three quarters, so the speed is about 0.866 c; The radial entry becomes minus eleven q; The trace still vanishes
   - **Numeric:** speed as a fraction of c = 0.866 1 (magnitude, ±0.005); radial entry in units of G M over r cubed = -11 1 (signed, ±0.05)
   - **Targets:** `same-tides-for-every-observer`
5. **Formal · evaluate-claim** `checks/one-observer-six-numbers`. Claim: a single freely falling observer at an event, using enough released test masses, measures every component of the Riemann tensor there. Evaluate the claim, using the comoving observers of the Einstein static universe, $ds^2 = -dt^2 + a^2\big(d\chi^2 + \sin^2\chi\,d\Omega^2\big)$ with constant $a$, as a test case ($G = c = 1$).
   - **Hints:** Which components of the Riemann tensor of a product of a time line with a 3-sphere carry a time index?
   - **Answer:** The claim is false. Released test masses measure $R_{\hat\imath\hat 0\hat\jmath\hat 0}$, a symmetric $3\times3$ block: 6 of the 20 independent components. In the Einstein static universe the metric is a product of time with a round 3-sphere of radius $a$, so every component with a $t$ index vanishes, and comoving observers, who are geodesic, measure a zero tidal operator. Yet $R_{\hat\imath\hat\jmath\hat k\hat l} = (\delta_{ik}\delta_{jl} - \delta_{il}\delta_{jk})/a^2$ and $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 12/a^4 \neq 0$. An observer moving at speed $\beta$ relative to them, along $\hat e_{\hat 1}$, reads $\gamma^2\beta^2/a^2$ for the two directions across her motion and 0 along it. The tidal operators of all observers at the event determine the Riemann tensor, because they fix $R(X,Y,X,Y)$ on an open set of pairs.
   - **Must contain:** One observer's tidal operator holds 6 of 20 components; Comoving observers in the Einstein static universe measure zero tides in a curved spacetime; All observers' operators together determine the Riemann tensor
   - **Targets:** `one-observer-reads-all-curvature`
6. **Formal · numeric** `checks/where-lambda-wins`. Outside a spherical mass $M$ with $\Lambda > 0$ ($G = c = 1$), the electric Weyl part for a static or radially moving observer is $(M/r^3)\,\mathrm{diag}(-2, 1, 1)$. Use the split of the tidal operator to find its eigenvalues, and the radius beyond which neighbours released across the radial line spread. Evaluate that radius in megaparsecs for $M = 10^{12}$ solar masses, $GM_\odot/c^2 = 1477$ m and $\Lambda = 1.1\times10^{-52}\ \mathrm{m^{-2}}$.
   - **Hints:** Contract $R_{\mu\nu} = \Lambda g_{\mu\nu}$ with $u^\mu u^\nu$ and project it with $h$.
   - **Answer:** In vacuum with $\Lambda$, $R_{\mu\nu} = \Lambda g_{\mu\nu}$ and $R = 4\Lambda$. Then $R_{uu} = -\Lambda$ and the projected Ricci tensor is $\Lambda h_{\mu\nu}$, so the Ricci terms of the split are $\tfrac12(-\Lambda - \Lambda)h_{\mu\nu} + \tfrac23\Lambda h_{\mu\nu} = -\tfrac13\Lambda h_{\mu\nu}$. The eigenvalues are $-2M/r^3 - \Lambda/3$ radially and $M/r^3 - \Lambda/3$ twice. The transverse ones change sign at $r_\Lambda = (3M/\Lambda)^{1/3}$. In SI, $M = 10^{12}\times1477$ m, so $r_\Lambda = (3\times1.477\times10^{15}/1.1\times10^{-52})^{1/3}\ \mathrm m = 3.43\times10^{22}$ m, about 1.11 Mpc. The trace is $-\Lambda$ at every radius. At $r_\Lambda$ the static observer is itself in free fall, since the mass's pull and the cosmological spreading balance there.
   - **Must contain:** The Ricci terms give minus lambda over three times the rest-space projector; Transverse eigenvalue M over r cubed minus lambda over three changes sign at the cube root of three M over lambda; About 1.1 megaparsecs for ten to the twelve solar masses
   - **Numeric:** radius where transverse tides change sign = 1.11 Mpc (magnitude, ±3%)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign, symbol and factors of c of the tidal tensor | The tidal tensor is $R^\mu{}_{\alpha\nu\beta}u^\alpha u^\beta$, with $u_\mu u^\mu = -c^2$, in $\mathrm{s^{-2}}$, written out without a symbol of its own; positive eigenvalues pull neighbours together. | Some texts flip its sign, so that positive entries push neighbours apart, name it with a letter such as $K$ or $E$, or set $c = 1$. Calibrate with a pair released at rest on the radial line just outside a spherical mass, which separates. |
| Tidal tensor versus electric part of the Weyl tensor | The electric part of the Weyl tensor is $C_{\mu\alpha\nu\beta}u^\alpha u^\beta$. It equals the tidal operator only in vacuum with $\Lambda = 0$; otherwise Ricci terms are added. | Some texts call $R_{\hat 0\hat\imath\hat 0\hat\jmath}$ itself the electric part of the curvature, with or without a trace removed, and some define the magnetic part with a different sign or factor. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): Flagship for this concept: a clock-face ring of crumbs in a falling cabin turns into an oval, the main directions carry their numbers, and slanted drifts come from adding parts. *Sketch:* This concept adds a clock-face ring of twelve crumbs around a middle crumb, standing along the line toward the planet's centre or laid across it, with magnified drift arrows and a ten-second clock. Three main-direction axes carry their drift per metre, beside the 3 by 3 table with eigenvalues and trace. Dragging a probe crumb splits its place along the axes and adds the two part-drifts into a slanted drift. A switch puts the cabin inside a uniform ball of rock, where a ring shrinks and stays round. Another gives the cabin a sideways or radial speed past a compact star: sideways, the radial and polar entries grow; radially, nothing changes.

## Tutor moves

**Open with**

- Picture a ring of crumbs held around one crumb inside a cabin that falls freely toward Earth. The ring is set so that the line toward Earth's centre passes through two of its crumbs. When all the crumbs are let go with no push, does the ring stay a circle? *(prediction)*

**If the learner is stuck**

- *The learner insists the farther crumb must close in because Earth pulls everything toward it.* → Ask which crumb falls fastest, then which falls slowest, and have the learner describe both from inside the cabin. *Uses:* `checks/crumbs-nearer-and-farther`
- *The learner cannot tell whether a positive entry means spreading or closing in.* → Calibrate with a pair released at rest on the radial line just outside a spherical mass. That pair separates, so its entry is negative in the course convention; then read the transverse entries. *Uses:* `ways_in/feed-the-four-velocity-in-twice`, `notation_traps/tidal-tensor-sign-and-symbol`

**Common questions**

- *Why does the drifting away along the line balance the drifting in across it?* (entry) Outside a round planet, a crumb on the line toward the centre drifts away twice as far as a crumb the same distance across the line drifts in. There is one direction along the line and two directions across it, so the one double drift balances the two single drifts. So a small ball of crumbs, at first, grows longer and thinner without changing its volume. Inside a planet's rock, say in a tunnel, the balance fails. The drifting in wins, so a small ball of crumbs shrinks. In a planet whose rock is equally tightly packed all the way through, the crumbs even close in from every direction. The next level shows that this balance in empty space is part of Einstein's equation. *Uses:* `ways_in/three-numbers-give-every-drift`, `problems/tides-inside-and-outside-a-planet`
- *Would crumbs near the Moon drift in the same pattern?* (entry) Yes, the same shape of pattern: away along the line toward the Moon's centre, and in across it. At the surface of a round body, these drifts depend only on how tightly packed its rock is on average. They do not depend on its size. The Moon's rock is less tightly packed than Earth's, so the drifts at its surface are about six tenths as big. *Uses:* `ways_in/ring-of-crumbs-becomes-an-oval`

**Switching levels**

- To working when: asks for the matrix or its eigenvalues; uses vectors or index notation. Group the four-velocity slots of the deviation equation, then work the planet problem. *Uses:* `ways_in/feed-the-four-velocity-in-twice`, `problems/tides-inside-and-outside-a-planet`
- To formal when: asks what one observer can measure of the curvature; asks about the Weyl tensor or Fermi coordinates. State the operator's structure and split, then the Einstein static universe check. *Uses:* `ways_in/the-tidal-operator-and-its-reach`, `checks/one-observer-six-numbers`
- To research when: asks about visualizing black-hole mergers, neutron-star tides, or covariant cosmology. Open the research horizon. *Uses:* `research_horizon/tendexes-and-vortexes`, `research_horizon/tidal-deformability-in-inspirals`

**Pronunciations:** Riemann → REE-mahn; Weyl → VILE; Ricci → REE-chee; Pirani → pih-RAH-nee; Szekeres → SEK-er-esh; GOCE → GOH-chay

**Voice notes:** At entry, say 'drifts away' and 'drifts in'; never 'up' or 'down' inside the falling cabin.

## History

- **Isaac Newton (1687).** Explained the ocean tides by the way the Moon's pull, and more weakly the Sun's, differs across Earth, the Newtonian root of the tidal tensor. Isaac Newton (1687), *Philosophiæ Naturalis Principia Mathematica*, Joseph Streater for the Royal Society, London
- **Felix Pirani (1956).** Showed that an observer in a parallel-propagated frame measures the components $R_{\hat\imath\hat 0\hat\jmath\hat 0}$ through relative accelerations of free test particles, making the tidal tensor the operational content of curvature. F. A. E. Pirani (1956), *On the physical significance of the Riemann tensor*, Acta Physica Polonica 15, 389–405
- **Peter Szekeres (1965).** Designed an idealized instrument of test masses joined by springs whose strains read the frame components of curvature, and related its readings to the algebraic type of the Weyl tensor. Peter Szekeres (1965), *The gravitational compass*, Journal of Mathematical Physics 6, 1387–1391, doi:10.1063/1.1704788

## Research horizon

- **Tidal tendexes and frame-drag vortexes.** In vacuum, the eigenvectors of the tidal operator integrate to tendex lines, and those of the magnetic part to vortex lines, with the eigenvalues as line strengths. Numerical-relativity simulations of merging black holes drawn this way show where tides stretch and where neighbouring gyroscopes precess, and how the patterns peel off as gravitational waves. Robert Owen, Jeandrew Brink, Yanbei Chen, Jeffrey D. Kaplan and others (2011), *Frame-dragging vortexes and tidal tendexes attached to colliding black holes: visualizing the curvature of spacetime*, Physical Review Letters 106, 151101, doi:10.1103/PhysRevLett.106.151101; David A. Nichols, Robert Owen, Fan Zhang, Aaron Zimmerman and others (2011), *Visualizing spacetime curvature via frame-drag vortexes and tidal tendexes: general theory and weak-gravity applications*, Physical Review D 84, 124014, doi:10.1103/PhysRevD.84.124014
- **Tidal deformability of neutron stars in binaries.** In a binary inspiral each neutron star sits in its companion's tidal field and develops a quadrupole in proportion to it; the constant of proportionality, the tidal deformability, depends on the equation of state of dense matter. The induced quadrupole shifts the gravitational-wave phase late in the inspiral, so detectors bound the deformability, as they did for GW170817. Éanna É. Flanagan, Tanja Hinderer (2008), *Constraining neutron-star tidal Love numbers with gravitational-wave detectors*, Physical Review D 77, 021502(R), doi:10.1103/PhysRevD.77.021502; B. P. Abbott and others (2017), *GW170817: Observation of Gravitational Waves from a Binary Neutron Star Inspiral*, Physical Review Letters 119, 161101, doi:10.1103/PhysRevLett.119.161101
- **Electric and magnetic Weyl parts in covariant cosmology.** Splitting the Weyl tensor with a family of observers' four-velocity gives electric and magnetic parts whose evolution, from the Bianchi identities, resembles Maxwell's equations with matter as source. This observer-based formulation is used to study gravitational waves, structure formation and silent universes without choosing coordinates. Roy Maartens, Bruce A. Bassett (1998), *Gravito-electromagnetism*, Classical and Quantum Gravity 15, 705–717, doi:10.1088/0264-9381/15/3/018

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** You are in a cabin falling down a tall empty tower, with thirteen crumbs floating in it, and someone lets them all go at once. The ones on the line to Earth's centre move away from the middle one, and the ones at the sides move in, so the ring stretches into an oval. I followed why the top and bottom ones spread: Earth pulls the lower one harder and the upper one less. I could not follow why the side ones move in exactly half as much. The note says to take that on trust, and it was the one place where I had to stop and just believe something. I reread two sentences that start with a list and only get their verb at the end, like "two crumbs let go with no push drift relative to each other". I reread "so it drifts partly outward and partly inward" too, because outward and inward were new words after a page of away and in. The tidal tensor is "a table of numbers", but then it "holds entries", and I was not sure whether an entry is one of the numbers or something else. For a crumb 3 metres along and 4 across you get 0.462 out and 0.308 in, so it goes on a slant. In the squared-paper bit I read the sentence about exaggerating the drifts three times before I saw that it only meant two-to-one. A crumb a metre out moves about the width of two hairs in ten seconds, which is why nobody ever notices it.

**Stumbles (25)**

- “How curving makes crumbs falling freely around you drift apart or together”: The tagline is the first line the reader meets, and "curving" stands alone with no object. Curving of what? The answer only arrives in the last sentence of the summary.
- “Set it so that the line toward Earth's centre passes through two of the ring's crumbs.”: "It" has two candidates in the sentence before: the ring and the middle crumb. A reader who picks the crumb cannot act on the instruction.
- “Crumbs on that line drift away from the middle crumb, and crumbs across it drift in.”: "Drift in" is a direction with no reference. In toward what: the middle crumb, the line, or Earth?
- “In Einstein's theory it comes from the curving of space and time.”: "It" could be the tidal tensor, the table, or the crumb, all in the sentence before. The one sentence that connects the whole note to Einstein must not turn on a guess.
- “In a cabin falling freely near Earth, two crumbs let go with no push drift relative to each other, slowly at first, then faster and faster.”: A garden path. I read "two crumbs let go" as the main clause, then hit "drift" and had to start the sentence again.
- “the cabin falls about 490 metres in ten seconds, more than half the height of the tallest building on Earth”: The comparison is measured against whatever building is tallest at the time of reading. A building taller than 980 metres would make the sentence false without anyone touching the note.
- “The other twelve sit on a circle 1 metre from it, placed like the hours on a clock face.”: "It" reads back to "the middle" rather than to the middle crumb, and "the cabin" is also in the paragraph. The whole picture depends on getting this distance right.
- “Above the ground, Earth's pull gets weaker the farther you are from its centre: 1 metre farther out, it is weaker by about 3 parts in 10 million.”: "You" are not in the cabin, the crumbs are, and "it" sits two nouns away from the pull it names. The sentence also carries a rule and a number across a colon in one breath.
- “Near a round planet, working this out carefully shows that they drift half as far as the crumbs on the line, 0.077 millimetres; take that on trust here.”: The half is the most surprising number in the way, it is the whole reason the ring becomes an oval rather than a bigger circle, and the note asks me to believe it. The picture I was just given, paths leaning like spokes, already contains the reason, so nothing new has to be imported to say it: a pull aimed at a centre 6371 kilometres away, on a crumb 1 metre off the line, has a sideways part in that same ratio by similar triangles, and that is half the 3 parts in 10 million already quoted for the line.
- “so it drifts partly outward and partly inward”: Two new words for ideas that already have words. Everywhere else a crumb drifts "away from the middle crumb" or "in toward" something, so outward and inward made me check whether they meant something else.
- “That part holds the entries that crumbs falling around you can measure.”: "Entries" is a second word for the numbers in the table, and it is never defined. The sentence also switches to "you" as the falling observer, when every other sentence in the way uses the middle crumb.
- “The Moon pulls the near side of Earth harder than Earth's centre, and the centre harder than the far side.”: Near and far to what? The Moon has just been mentioned, but so has Earth's centre, and the reader has been working with crumbs nearer and farther from Earth's centre for three paragraphs.
- “That is why you never notice it.”: "It" could be the drift, the pattern, or the hair-width. The closing line of the way should not need a decision.
- “So a ring set along that line becomes an oval”: "Set along that line" is not a rule I can follow. A ring cannot lie along a line; the setting I was actually given is that the line runs through two of its crumbs. A ring set face-on to the line, which also sounds like "along", stays a circle and shrinks, so the takeaway would be false for it.
- “In a cabin falling freely near Earth, crumbs let go with no push around a middle crumb drift.”: The same garden path as the other recap, and worse: the sentence ends on the bare verb "drift", which I first read as a noun.
- “Drifts are in proportion to distance.”: Distance from what? Every other distance in the note is measured from the middle crumb, but Earth's centre is also in play, and the drift would shrink, not grow, with distance from that.
- “One 1 metre out across that line drifts in by 0.077 millimetres.”: "One 1" made me stop. The noun that "one" stands for is a crumb, two sentences back.
- “The oval in "A ring of crumbs turns into an oval" came from crumbs that sit partly along the line toward Earth's centre and partly across it.”: False for the first what-if I tried: the crumbs at the 6, 12, 3 and 9 are part of the oval too, and none of them sits partly along and partly across. Eight of the twelve do.
- “Any two will do, because a round planet looks the same from every side of that line.”: "From every side" asks me to look from somewhere without saying where. What is meant is that the planet looks the same all the way round the line, which is a turn, not a side.
- “Only the across part makes the two paths lean like spokes. So each part drifts on its own, and the crumb makes both drifts at once.”: "The two paths" have not been named in this way; I had to go back to the other way to find that they are the crumb's path and the middle crumb's path. And a part of a distance cannot drift, only the crumb can.
- “Now exaggerate the drifts, keeping the drift along the line twice as big, for each square, as the drift across it, as near Earth.”: I read this three times. Two comparisons and a condition are stacked inside one instruction, and the trailing "as near Earth" reads at first as another comparison.
- “Near Earth, find a crumb's drift by splitting its place along the main directions, giving each part its own drift, and making both drifts at once.”: "Splitting its place" is not something I can picture or do; a place is not a thing with parts. What I actually did in the way was split the crumb's distance from the middle crumb into an along piece and an across piece.
- “A friend says the farther crumb will drift toward the middle crumb, because Earth pulls everything toward it.”: "Toward it" can be read as toward the middle crumb, which would make the friend's claim circular instead of wrong for a stateable reason.
- “You want the ring to become an oval 1 millimetre longer along that line than across it, after ten seconds by the cabin's clock. ... How wide must the ring be at the start?”: Two ambiguities in one problem. "1 millimetre longer along that line than across it" can be read as the growth along the line being 1 millimetre, and "how wide" can be read as a radius. I got 2.2 metres on my first try.
- “A small table of numbers, for someone falling freely, that gives how crumbs let go around them drift apart or together, for a crumb placed in any direction.”: The definition starts with several crumbs and ends with one, and "drift apart or together" is not what the note showed: a crumb let go on a slant drifts neither apart nor together.

**Fixes**

- Backed the half factor. "Take that on trust here" is gone: the crumbs at the 3 and the 9 now get an entry-rung reason built only from school similar triangles and numbers already in the way, namely 1 metre across the line against Earth's centre 6371 kilometres away, giving a sideways part of about 1.6 parts in 10 million, half the 3 parts in 10 million by which the pull weakens over 1 metre. This is the only substantial addition and it costs about 125 words.
- Cleared eight unreferenced pronouns and directions: "Set it", "crumbs across it drift in", "In Einstein's theory it comes", "a circle 1 metre from it", "the farther you are from its centre", "Earth pulls everything toward it", "That is why you never notice it", and "Drifts are in proportion to distance".
- Removed the synonyms. "Outward" and "inward" became "away along the line" and "in toward the line"; "entries" of the Riemann table became "numbers" in the recap, the explanation and the glossary, so the note uses one word for one idea.
- Unpicked two garden-path recap sentences ("two crumbs let go with no push drift", "crumbs let go with no push around a middle crumb drift") and "One 1 metre out".
- Rewrote both entry takeaways. "A ring set along that line" was a rule the reader could not follow and was false for a ring set face-on to the line; it is now "a ring set with that line through two of its crumbs". "Splitting its place along the main directions" became splitting the crumb's distance from the middle crumb. Both stay under the 240-character limit.
- Fixed a false general sentence: the oval did not come only from crumbs that sit partly along and partly across; it is eight of the twelve.
- Replaced the tallest-building comparison, which would go stale on its own, with the Eiffel Tower, and named the Moon-facing side of Earth instead of "the near side".
- Made the entry problem unambiguous: the target is now the oval's width along the line minus its width across, and the asked-for width is measured right across through the middle crumb. The answer, key point and solution step were reworded to match; the numbers 0.154, 0.077, 0.231 and 4.3 metres are unchanged.
- Rewrote the try-it instruction that stacked two comparisons and a condition into one sentence; the drawing, the 6 and 8 squares and the 7.2 by 7.2 landing point are unchanged.
- Tagline and summary rewritten for the same reasons; the summary is 497 of its 500 characters, so "Let them all go with no push, and the ring turns into an oval" was split into two sentences to make room.
- Budget: entry way explanations now stand at 1080 words against a cap of 1000, inside the 10 per cent review allowance, and every word of the overshoot is the half-factor argument above. Nothing was compressed to fit. If a later stage needs room, the two lowest-value items to drop first are the Eiffel Tower comparison (9 words) and "mostly the Moon's" (3 words), which the next sentence already says.

**Concerns**

- This is a second novice pass over a note that was already novice-reviewed and physics-reviewed at revision 4. The earlier novice record (19 stumbles, 9 fixes) has been replaced by this one; its rereads entry is kept below. If the orchestrator wanted only a sign-off rather than a fresh review, the earlier record is in the snapshot at snapshots/notes-curvature/relativistic-tidal-tensor.before-novice2.json.
- A physics diff check is owed. This pass changed 17 learner-visible strings, all at entry, after the physics review signed revision 4, so the status is back to novice-reviewed. The new claims to check are: the similar-triangles argument for the transverse drift; the sideways fraction of about 1.6 parts in 10 million from 1 metre in 6371 kilometres; that this is half the 3 parts in 10 million already quoted; that drift is in proportion to the difference in pull over a fixed ten seconds; and that 490 metres is about one and a half times the Eiffel Tower.
- checks/crumb-three-along-four-across repeats the worked example of ways_in/three-numbers-give-every-drift with the same 3 metres, 4 metres, 0.154 and 0.077, and restates both per-metre drifts in the question. A learner who has just read the way can answer it from memory, so it evidences recall rather than the objective combine-main-direction-drifts. I left it alone because its id would have to change with the numbers. An editor should change it before publication, for example to 5 metres along and 12 metres across, giving 0.770 millimetres away along the line and 0.924 millimetres in toward it, and rename the id.
- The summary is six sentences where the guide asks for two or three. The ring's setting, the drift pattern, the definition and the link to Einstein each need their own sentence, and the field's 500-character limit leaves no room to merge them. It now sits at 497 characters.
- The working ways use index notation throughout, but index-notation is not a prerequisite of this note, directly or through any of the seven listed ones. The exemplar holonomy note is in the same position, so this looks like a house-wide question rather than something to change here.
- analogies is still empty, so the teaching arc has no transfer setting outside the falling cabin. The tutoring part has about 520 words of headroom, enough for one bridge analogy from a different setting.
- The flagship visual falling-ring-of-crumbs is still a proposal. When it is built it should draw the ring with the line toward the planet's centre running through the 6 and the 12, use only the words drift, away and in, and never up or down inside the cabin.
- Five prerequisites are still unwritten (orthonormal-frame, newtonian-tidal-tensor, lorentz-transformation, einstein-field-equations, weyl-tensor), so the entry vocabulary of this note could not be matched against theirs. Only geodesic-deviation-equation is needed at entry, and it exists.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 7 changed passages

- “The drifting in wins, so a small ball of crumbs shrinks. In a planet whose rock is equally tightly packed all the way through, crumbs close in from every direction.”: Nothing marks the last sentence as a stronger, special case. A listener cannot tell whether a shrinking ball in a tunnel already means crumbs close in from every direction, or whether the equally packed planet is something more.
- “a pair released at rest on the radial line just outside a spherical mass, which separates, so its entry is negative”: The nearest noun to 'which separates' is 'a spherical mass', so the relative clause seems to say the mass separates.
- “Flipping the order within each pair, two sign flips, gives $R_{\hat r\hat t\hat r\hat t} = R_{\hat t\hat r\hat t\hat r} = -2q/c^2$, so the entry is ... after multiplying by $c^2$.”: The appositive 'two sign flips' is squeezed. The student has to work out that antisymmetry in each index pair gives one sign flip each, and the conversion by $c^2$ comes last, after the result it produces.
- Fix: Added 'the' and 'even' to the equally packed planet sentence in common question why-do-they-balance, so it reads as a stronger special case. The claim is unchanged.
- Fix: Split if_stuck sign-confusion so 'That pair separates' names its subject. The scope (at rest, radial line, just outside a spherical mass) is unchanged.
- Fix: Reworded step 2 of derivation tides-for-a-sideways-passer so antisymmetry in each index pair is named as the reason for the two sign flips, with the multiplication by c squared stated in order. Same equations and values.
- Fix: No stumbles in the 'Above the ground' and 'Dropped from rest' sentences of ring-of-crumbs-becomes-an-oval, the check answer crumbs-nearer-and-farther, or the vacuum wording of observation gw150914-oscillating-tides. A novice reads 'Above the ground' as the cabin's setting inside the tower.

**Re-read** (2026-09-13, revision 7): 1 stumbles in 2 changed passages

- “Around a mass there is no one tidal field that all observers share.”: "no one" is a garden path. Read aloud, and in the tutor's voice, it first lands as "no-one" (nobody), and the reader has to restart the sentence to find that "one" counts tidal fields. This is the closing claim of the way, the sentence the reader carries away, so it must not need a second pass. The rest of the paragraph is clear: "What they share is the Riemann tensor, from which each reads her own tidal tensor" names its subject and needs no reread.
- Fix: Changed "no one tidal field" to "no single tidal field" in the closing paragraph of way a-passing-observer-reads-other-tides. Wording only: the scope (around a mass), the quantifier over observers, and the claim are all unchanged, and the word count is unchanged, so no budget is touched.
- Fix: No other stumble in scope. The physics review's second change, "With $R_{\mu\nu} = 0$ it is the whole operator", is formal-rung text and note_diff lists nothing at entry or working besides the sentence above, so no entry text was reread.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- New entry argument for the half factor: Earth's pull on a crumb 1 metre across the line has a sideways part equal, by similar triangles, to the fraction 1 metre in 6371 kilometres of the whole pull, about 1.6 parts in 10 million.: python3: 1/6.371e6 = 1.5696e-7, i.e. 1.570 parts in 10 million; exact sin and tan of the angle agree to seven figures (1.569612e-7 each), so the similar-triangles step loses nothing at entry. → Correct. The sideways component is g sin(theta) with tan(theta) = 1 m / r, and the small-angle and similar-triangle forms agree.
- New entry argument: the middle crumb feels no sideways pull, so the sideways part is the whole difference in pull between the two crumbs.: python3: the transverse crumb's distance to Earth's centre exceeds the middle crumb's by 1/(2r) of a metre, so its pull magnitude differs fractionally by 2.5e-14, seven orders of magnitude below the sideways part 1.57e-7. → Correct to first order in the separation, which is the note's stated scope.
- New entry claim: that sideways fraction is half the 3 parts in 10 million by which the pull weakens over 1 metre, so the transverse drift is half the radial one.: python3: 2/6.371e6 = 3.139e-7 against 1/6.371e6 = 1.5696e-7; ratio exactly 2.000000 for any radius, since the two fractions are 2/r and 1/r. → Correct, and the exact factor 2 does not depend on the value used for Earth's radius. The rounded quotation ('about 3' against 'about 1.6') is scoped with 'about twice as big'.
- New entry claim: over a fixed ten seconds a drift is in proportion to the difference in pull that makes it.: Relative displacement from a constant relative acceleration a is a t^2/2, so at fixed t it is proportional to a; the tidal matrix diag(-2q, q, q) makes the relative acceleration exactly the difference in pull per unit mass to first order in the separation. → Correct. Both drifts are quoted at the same t = 10 s, so the proportionality is used only where it holds.
- New entry scale comparison: 490 metres is about one and a half times the height of the Eiffel Tower.: python3: 0.5 x 9.81 x 100 = 490.5 m; 490.5/330 = 1.49 (tower with its antennas), 490.5/324 = 1.51 (earlier antenna height). → Correct on either figure, and the landmark cannot go stale the way 'the tallest building' could.
- Entry numbers: a 1 m radial neighbour drifts away 0.154 mm and a 1 m transverse neighbour drifts in 0.077 mm in 10 s at Earth's surface.: python3 with GM = 3.986004418e14 m^3 s^-2 and R = 6.371e6 m: q = GM/R^3 = 1.5414e-6 s^-2; radial (2q)t^2/2 = 0.1541 mm, transverse q t^2/2 = 0.0771 mm. → Correct outside a spherical mass, the way's stated setting.
- Entry closing claim: a crumb 1 metre out drifts less than two tenths of a millimetre in ten seconds.: For a unit separation n, the drift is |diag(0.154, -0.077, -0.077) n| mm, maximised at 0.154 mm along the radial line; checked the whole direction sphere algebraically. → Correct for every direction, so the universal form of the sentence is safe.
- The twelve clock-face crumbs end on an oval longer along the line and shorter across it.: Map (cos t, sin t) -> ((1 + 2e)cos t, (1 - e)sin t) with e = q t^2/2 = 7.7e-5; an ellipse to first order, semi-axes in ratio (1+2e):(1-e). → Correct for a ring set with the line through two of its crumbs. A ring set face-on to the line shrinks and stays round; the wording excludes it.
- Entry check crumbs-nearer-and-farther: each outer crumb drifts away 0.154 mm and the row lengthens by about 0.31 mm.: python3: 2 x 0.154 = 0.308 mm. → Correct; numeric field and 5 per cent tolerance fine.
- Entry way and check: a crumb 3 m along the line and 4 m across drifts 0.462 mm away along the line and 0.308 mm in toward it, about half a millimetre in all, on a slant.: python3: 3 x 0.154 = 0.462, 4 x 0.077 = 0.308, magnitude 0.5553 mm; the drift (0.462, -0.308) is not parallel to the separation (3, 4). → Correct, and linear superposition is exact for the eigen-directions of a symmetric matrix.
- Entry try-it: 6 squares along and 8 across, exaggerated by 2 tenths and 1 tenth per square, lands at 7.2 and 7.2.: python3: 6 + 0.2 x 6 = 7.2, 8 - 0.1 x 8 = 7.2; displacement (+1.2, -0.8) against the outward direction (0.6, 0.8). → Correct, and the exaggeration keeps the true two-to-one ratio of the drifts.
- Entry problem ring-for-a-millimetre-difference: the ring must start about 4.3 m wide.: python3: the along width grows by 0.154 D mm and the across width shrinks by 0.077 D mm for a starting width D in metres, so 0.231 D = 1 gives D = 4.329 m. → Correct; the reworded statement (oval's width along minus width across, measured right across through the middle crumb) is the quantity computed.
- Common question near-the-moon: surface drifts depend only on mean density, and the Moon's are about six tenths of Earth's.: GM/R^3 = (4 pi/3) G rho_mean; python3 3344/5514 = 0.606. → Correct.
- Common question why-do-they-balance: one double drift away balances two single drifts in outside a planet; inside rock the drifting in wins; in a uniformly packed planet crumbs close in from every direction.: Trace of diag(-2, 1, 1) is zero and the volume factor (1+2e)(1-e)^2 = 1 + O(e^2); inside matter the trace is 4 pi G rho > 0; for a uniform ball all three eigenvalues equal 4 pi G rho/3. → Correct with the note's scopes ('at first', 'equally tightly packed all the way through'). A real crustal tunnel still spreads radially, which is why the stronger claim is confined to the uniform planet.
- Key equation tidal-tensor-in-deviation: D^2 xi^mu/dtau^2 = -(R^mu_{alpha nu beta} u^alpha u^beta) xi^nu.: Compared slot by slot with the conventions row D^2 xi^mu/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma: slot 2 and slot 4 carry u, slot 3 carries xi in both. → Matches the course convention exactly; units m^-2 x m^2 s^-2 = s^-2 as claimed.
- Key equation weak-field-hessian: c^2 R^i_{0j0} = d_i d_j Phi, giving (GM/r^3) diag(-2, 1, 1) outside a spherical mass, with positive eigenvalues pulling neighbours together.: Derived from the course Riemann convention: with g_00 = -(1 + 2Phi/c^2), Gamma^i_{00} = d_i Phi/c^2 and R^i_{0j0} = d_j Gamma^i_{00} = d_i d_j Phi/c^2; Hessian of -GM/r has Phi'' = -2GM/r^3 and Phi'/r = GM/r^3. → Correct sign, index placement and factors; a radial pair separates, as it must.
- Structure claims: separations along u feel nothing, relative accelerations are orthogonal to u, the matrix is symmetric, oscillation frequency sqrt(lambda)/2 pi, cosh growth for negative lambda, l = l0 (1 - lambda tau^2/2).: Antisymmetry of the first and last index pairs, pair exchange, and the solutions of xi'' = -lambda xi; frequency in hertz from angular frequency sqrt(lambda). → Correct.
- Derivation trace-from-einstein-equation: R_{alpha beta} u^alpha u^beta = 4 pi G (rho + 3p/c^2) - Lambda c^2.: Re-derived each step in the course conventions: -R + 4 Lambda = kappa T with kappa = 8 pi G/c^4; R_{mu nu} = kappa(T_{mu nu} - T g_{mu nu}/2) + Lambda g_{mu nu}; for the perfect fluid T_uu = rho c^4 and T = -rho c^2 + 3p; -T g_uu/2 = -rho c^4/2 + 3 p c^2/2; kappa(rho c^4/2 + 3 p c^2/2) = 4 pi G(rho + 3p/c^2). → Correct, including the sign of the -Lambda c^2 term with u.u = -c^2, and the dust limit 4 pi G rho = Laplacian of Phi.
- Check pressure-adds-to-the-squeeze: a gas of light focuses twice as strongly as dust of the same mass density.: rho + 3(rho c^2/3)/c^2 = 2 rho against rho. → Correct; ratio exactly 2, with the observer at rest in each fluid as the formula requires.
- Working problem tides-inside-and-outside-a-planet: eigenvalues (-2, 1, 1) outside and (1, 1, 1) inside in units of GM/R^3; radial jump 4 pi G rho = 4.62e-6 s^-2 for rho = 5510 kg m^-3.: For Phi(r), the radial eigenvalue is Phi'' and each transverse one Phi'/r; checked that the quoted interior potential (2 pi G rho/3)(r^2 - 3R^2) matches -GM/R at r = R; python3 4 pi x 6.674e-11 x 5510 = 4.621e-6. → Correct, and both traces match 4 pi G(rho + 3p/c^2) with p about zero.
- Schwarzschild static-frame components: R_trtr = -2q/c^2, R_tthtth = R_tphtph = q/c^2, R_thphthph = 2q/c^2, R_rthrth = R_rphrph = -q/c^2 with q = GM/r^3.: Took the two time-time entries from the Newtonian limit, then solved R_rr = 0 and R_thth = 0 for the purely spatial ones: R_rthrth = R_trtr/2 = -q/c^2 and R_thphthph = R_tthtth - R_rthrth = 2q/c^2. R_tt = 0 then follows. → Correct and uniquely fixed by Ricci-flatness and spherical symmetry in the course conventions.
- Derivation tides-for-a-sideways-passer: q diag(-gamma^2(2 + beta^2), gamma^2(1 + 2beta^2), 1), diagonal and trace-free.: Contracted the static-frame components with u' = gamma c(e_t + beta e_ph) and the boosted axes; the motion entry is unchanged because the bivector e_ph' wedge e_0' equals e_ph wedge e_t; every off-diagonal entry needs a vanishing static component such as R_rtthT. python3 at beta = 0, 0.5, 0.6, 0.866 gives traces zero to rounding. → Correct.
- Check polar-entry-ten-times: beta^2 = 3/4, v = 0.866c, radial entry -11q, trace zero, more than a factor five between the two observers.: python3: gamma^2(1 + 2beta^2) = 10 gives beta^2 = 0.75 and gamma^2 = 4; radial -4(2.75) = -11; -11 + 10 + 1 = 0; 11/2 = 5.5. → Correct; both numeric fields and tolerances fine.
- Worked example a-radial-faller-agrees: a radial boost at 0.6c leaves q diag(-2, 1, 1).: The radial boost preserves e_r wedge e_t, so the radial entry is unchanged; the transverse entry is gamma^2(R_tthtth + beta^2 R_rthrth)c^2 = gamma^2(1 - beta^2)q = q; python3 1.5625 x 0.64 = 1. → Correct, and the sign of beta enters only through beta^2, so an outward faller agrees too.
- Working way numbers: low Earth orbit beta^2 gamma^2 about 7e-10; just outside a neutron star beta about 0.5 gives a polar entry twice and a radial entry one and a half times the static values.: python3 with v = 7.7 km/s: 6.6e-10. Circular geodesic speed relative to static observers sqrt(M/(r - 2M)) is 0.5 at r = 6M, close to a neutron-star surface at r about 5 to 6 M; gamma^2(1 + 2beta^2) = 2.0 and gamma^2(2 + beta^2)/2 = 1.5. → Correct.
- Formal proposition: the tidal operator X -> R(X, u)u is self-adjoint on u-perp with eigenvalues lambda_k = -K(u, e_k).: Components R^mu_{alpha nu beta} u^alpha u^beta X^nu agree with R(X, u)u read from [nabla_mu, nabla_nu]V^rho = R^rho_{sigma mu nu} V^sigma; the quadratic form is R(e, u, e, u), and the conventions row for sectional curvature has denominator g(e,e)g(u,u) - g(e,u)^2 = -1 for a unit e orthogonal to a unit timelike u. → Correct, and consistent with the conventions note that free-fall pairs drawing together have K < 0: the Schwarzschild radial eigenvalue -2M/r^3 corresponds to K = +2M/r^3 for a spreading pair.
- Formal split: R_{mu alpha nu beta}u^alpha u^beta = C_{mu alpha nu beta}u^alpha u^beta + (R_uu h_{mu nu} - h_mu^rho h_nu^sigma R_{rho sigma})/2 + R h_{mu nu}/6.: Contracted the four-dimensional Weyl decomposition R_{abcd} = C_{abcd} + (g_{a[c}R_{d]b} - g_{b[c}R_{d]a}) - (R/3) g_{a[c}g_{d]b} twice with u by hand: the Ricci block gives g_{ac}R_uu/2 - u_a R_{cu}/2 - u_c R_{ua}/2 - R_{ca}/2, and expanding the note's projected form h_mu^rho h_nu^sigma R_{rho sigma} reproduces it term by term; the R term gives (R/6)h_{ac}. → Correct, with the stated 1/2 and 1/6 coefficients and the trace-free, u-orthogonal electric part.
- Formal trace and the strong energy condition: R_uu = 8 pi (T_uu + T/2) - Lambda, non-negative for every observer exactly when the strong energy condition holds with Lambda = 0.: Contracted R_{mu nu} = 8 pi(T_{mu nu} - T g_{mu nu}/2) + Lambda g_{mu nu} with u^mu u^nu at u.u = -1. → Correct.
- Check where-lambda-wins: eigenvalues -2M/r^3 - Lambda/3 and M/r^3 - Lambda/3; sign change at r = (3M/Lambda)^(1/3) = 1.11 Mpc for 1e12 solar masses; trace -Lambda at every radius; the static observer is in free fall at that radius.: With R_{mu nu} = Lambda g_{mu nu} the Ricci terms are (-Lambda - Lambda)h/2 + (4 Lambda/6)h = -(Lambda/3)h; python3 with M = 1e12 x 1477 m and Lambda = 1.1e-52 m^-2 gives r = 3.428e22 m = 1.111 Mpc; the Schwarzschild-de Sitter static acceleration is proportional to M/r^2 - Lambda r/3, zero at the same radius. → Correct; the 3 per cent tolerance is comfortable.
- Check one-observer-six-numbers: one observer fixes 6 of 20 components; comoving observers in the Einstein static universe read a zero operator while the Kretschmann scalar is 12/a^4; a boosted observer reads gamma^2 beta^2/a^2 across her motion and 0 along it.: Counted 20 = 6 (R_0i0j) + 8 (R_0ijk after the first Bianchi identity) + 6 (R_ijkl); for a product of a time line with a round 3-sphere every component with a time index vanishes and R_ijkl = (delta delta - delta delta)/a^2, whose Kretschmann is 2n(n-1)K^2 = 12/a^4 with n = 3; contracted with u' = gamma(e_0 + beta e_1), giving gamma^2 beta^2 R_{i1j1} and zero along the motion because the bivector e_1' wedge e_0' equals e_1 wedge e_0. → Correct, and the recovery argument (R(X,Y,X,Y) known on an open set of timelike Y, then polarization with the first Bianchi identity) is sound; 5 + 5 for the electric and magnetic Weyl parts in vacuum.
- Formal problem tides-in-fermi-coordinates: Gamma^i_{00} = R_{0i0j}x^j, d^2x^i/dt^2 = -R^i_{0j0}x^j, tidal potential R_{0i0j}x^i x^j/2 equal to the quadratic Taylor term of Phi.: Worked every step: Gamma^i_{00} = (2 d_0 g_{k0} - d_k g_{00})g^{ik}/2 with the first term O(x^2); d_k g_{00} = -2R_{0k0j}x^j using the pair symmetry of R_{0k0j} in k and j; two sign flips give R_{0i0j} = R_{i0j0}; g_00 = -(1 + 2 Phi_tid) matches the course weak-field row. → Correct and consistent with the working-rung deviation sign.
- Observation goce-gravity-gradients: 0.5 m baselines at about 255 km, radial -2.74e-6 s^-2, transverse +1.37e-6 s^-2, quoted by geodesists as about +2740 eotvos, with the three diagonal entries adding to zero outside Earth's mass.: python3 with r = 6626 km: GM/r^3 = 1.370e-6 s^-2. The trace of d_i d_j Phi is the Laplacian, zero in vacuum. Geodesists use V = +GM/r, which flips the sign; 1 eotvos = 1e-9 s^-2. → Correct, including the mission dates 2009 to 2013 and the differential-accelerometer baseline.
- Observation gw150914-oscillating-tides: strain 1.0e-21 at about 150 Hz gives tidal entries of amplitude 4.4e-16 s^-2, about 3.5 billion times smaller than Earth's transverse entry; entries -h-double-dot/2; Ricci vanishes at the mirrors.: python3: 0.5 x 1e-21 x (2 pi x 150)^2 = 4.44e-16; 1.5414e-6/4.44e-16 = 3.47e9. In transverse-traceless gauge xi'' = h-double-dot xi/2, so the tidal tensor, defined with the opposite sign, is -h-double-dot/2. → Correct, and 'Earth's transverse entry' is the right comparison (the radial entry is twice as large).
- References: Rummel, Yi and Stummer 2011, J. Geodesy 85, 777-790; Maartens and Bassett 1998, CQG 15, 705-717; Szekeres 1965, J. Math. Phys. 6, 1387-1391; Pirani 1956, Acta Physica Polonica 15, 389-405; Flanagan and Hinderer 2008, Phys. Rev. D 77, 021502(R); Owen et al. 2011, Phys. Rev. Lett. 106, 151101; Nichols et al. 2011, Phys. Rev. D 84, 124014; Abbott et al. 2016, Phys. Rev. Lett. 116, 061102; Abbott et al. 2017, Phys. Rev. Lett. 119, 161101; Newton 1687, Principia.: Web search against publisher records (Springer, IOPscience, AIP, APS), ADS and arXiv abstract pages for authors, year, title, volume, page range, DOI and arXiv id. → All confirmed unchanged from the previous pass; every reference keeps verified true. Pirani's paper has no DOI of its own (the 2009 republication in Gen. Rel. Grav. 41, 1215 does), so arxiv and doi stay null.
- History scope: Newton 1687 explained the ocean tides by the differential lunar and solar pull; Pirani 1956 tied R_i0j0 to relative accelerations in a parallel-propagated frame; Szekeres 1965 built a spring compass whose strains read frame components and related them to the Weyl algebraic type.: Checked each contribution sentence against the confirmed paper and its abstract; checked that each claim says what was first and in what setting. → Accurate and correctly scoped.
- Fix made this pass: 'There is no tidal field that all observers share' rescoped to 'Around a mass there is no one tidal field that all observers share'.: Contracted a maximally symmetric curvature R_{mu alpha nu beta} = K(g_{mu nu}g_{alpha beta} - g_{mu beta}g_{alpha nu}) twice with u: the operator is -K c^2 h_{mu nu}, the same isotropic matrix for every observer; flat spacetime is the case K = 0. → The old sentence was a false universal (de Sitter, anti-de Sitter and flat spacetime are shared-tide cases); the rescoped sentence is true in the way's stated setting, the vacuum outside a non-rotating spherical mass, where boosting along e_phi changes the matrix.
- Fix made this pass: 'In vacuum it is the whole operator' tightened to 'With R_{mu nu} = 0 it is the whole operator'.: The Ricci terms of the split vanish only when R_{mu nu} = 0; with R_{mu nu} = Lambda g_{mu nu} they contribute -(Lambda/3)h, which the next sentence and the check where-lambda-wins both use. → Removes an ambiguity, since vacuum with a cosmological constant is also called vacuum; matches the note's own notation trap, which already says 'only in vacuum with Lambda = 0'.

**Counterexamples tried**

- Maximally symmetric spacetime (de Sitter, anti-de Sitter, and flat spacetime as K = 0): every observer's tidal operator is -K c^2 times the projector on her own rest space, so all observers do share one tidal field. This broke the universal 'There is no tidal field that all observers share', which is now scoped to the neighbourhood of a mass.
- Vacuum with a positive cosmological constant: the trace is -Lambda, not zero, and the transverse eigenvalues change sign at (3M/Lambda)^(1/3). The note's trace-zero statements are scoped to vacuum with Lambda = 0, and 'In vacuum it is the whole operator' was tightened to R_{mu nu} = 0 for the same reason.
- Below the ground (a tunnel in the real Earth): g grows with depth through the crust, and the crustal radial eigenvalue 4 pi G(rho_local - 2 rho_mean/3) is still negative, so a radial pair spreads. The entry rule is scoped with 'Above the ground' and the strong every-direction claim is confined to a uniformly packed planet. Rechecked this pass.
- Ring set face-on to the line (the line through its hole): it shrinks and stays round, so the takeaway's 'a ring set with that line through two of its crumbs' is doing real work. Confirmed again against the first-order ellipse map.
- A crumb on a slant: it drifts neither directly away nor directly toward the middle crumb, which is what the second entry way and the check exist to show; the pair still separates or closes as a pair, since the rate goes as 3a^2 - 1 for a radial direction cosine a, so the tagline's 'drift apart or together' survives.
- Cabin already moving when the ten seconds start: breaks 'falls about 490 metres in ten seconds', which is scoped with 'Dropped from rest'. The drift numbers themselves are unchanged by the cabin's radial speed, as the radial-boost worked example shows exactly.
- Longer time or a bigger ring: the cosh and cos corrections are of relative size lambda t^2/12, about 1e-6 at ten seconds, and metre-sized rings are tiny compared with Earth's radius, so the first-order entry statements hold.
- Non-relativistic limit: the sideways-passer matrix tends to diag(-2, 1, 1) as beta -> 0, and a radial boost changes nothing at any speed, so the Newtonian matrix is recovered exactly where it should be.
- Different observer in a curved spacetime: comoving observers in the Einstein static universe read a zero tidal operator while the Kretschmann scalar is 12/a^4, and boosted observers there read gamma^2 beta^2/a^2. This backs the formal claim that one observer sees only 6 of 20 components.
- Inside matter: a uniform ball gives all three eigenvalues 4 pi G rho/3, so a released ring shrinks and stays round; the calibration rule for the sign convention is therefore scoped to a pair released at rest just outside a spherical mass.
- Massless source, and pressure as a source: a gas of light with p = rho c^2/3 doubles the trace rather than reducing it, which is the working misconception and check.
- Strong field: at the innermost stable circular orbit of a compact star, beta = 0.5 relative to static observers changes the polar entry by a factor of two, so the 'one matrix for every observer' shortcut fails there while holding to 1e-9 in low Earth orbit.

**Fixes**

- Rescoped one working sentence in ways_in/a-passing-observer-reads-other-tides: 'There is no tidal field that all observers share' became 'Around a mass there is no one tidal field that all observers share'. The old sentence was false in maximally symmetric spacetimes, flat spacetime included, where every observer reads the same isotropic operator. The following sentence, which names what observers do share, is unchanged.
- Tightened one formal sentence in ways_in/the-tidal-operator-and-its-reach: 'In vacuum it is the whole operator' became 'With $R_{\mu\nu} = 0$ it is the whole operator', so it cannot be read as covering vacuum with a cosmological constant, the case the very next sentence and the check where-lambda-wins treat.
- Nothing else changed. Every entry claim added by the second novice pass, including the similar-triangles argument for the half factor, was verified and left exactly as written; no number, tolerance, equation, reference or id was touched.
- Revision 5 -> 6. note_diff.py over entry and working rungs lists one changed string (working); the formal change is listed only when formal rungs are included. Budgets are unaffected: the working way explanations move from 642 to 646 words against a cap of 1000, and the entry explanations stay at 1080, inside the review allowance of 1100.

**Concerns**

- Entry way explanations sit at 1080 words against the 1000-word core cap, 8 per cent over and inside the guide's 10 per cent review allowance. The whole overshoot is the novice reviewer's half-factor argument, which is correct and which I would not drop: it replaces the only 'take this on trust' step at entry. If an editor needs room, the two items the novice named (the Eiffel Tower comparison and 'mostly the Moon's') are still the cheapest to lose.
- The ladder question the novice raised is resolved: index-notation is a transitive prerequisite through orthonormal-frame (orthonormal-frame -> orthonormal-basis -> basis-vectors -> four-vector -> index-notation), so the working ways may use index notation under the guide's rule. No prerequisite change is needed here.
- course-conventions.md still fixes no symbol for the relativistic tidal tensor and no symbol or normalization for the electric and magnetic parts of the Weyl tensor. This note avoids the gap by writing both out in full, and its notation traps say so, but the gap should be filled before ricci-focusing-versus-weyl-shear, geodesic-deviation-in-gravitational-wave and tidal-deformability are written, since they cannot avoid it.
- checks/crumb-three-along-four-across still repeats the worked example of ways_in/three-numbers-give-every-drift verbatim and restates both per-metre drifts in its question, so it evidences recall rather than the objective it is attached to. I confirmed the novice reviewer's replacement numbers: 5 metres along and 12 metres across give 0.770 mm away along the line and 0.924 mm in toward it, with a 13-metre separation. An editor changing it must also change the id.
- Registry prerequisites still differ from the note for einstein-field-equations, lorentz-transformation, newtonian-tidal-tensor, ricci-tensor and weyl-tensor; sync_registry.py should apply the note's list. I walked the registry graph: nothing in the transitive closure of the note's seven prerequisites is this concept, so there is no cycle. Only schwarzschild-tidal-field and volume-preserving-tidal-deformation list this concept as a prerequisite, and neither is a prerequisite of it.
- Five prerequisites are still unwritten (orthonormal-frame, newtonian-tidal-tensor, lorentz-transformation, einstein-field-equations, weyl-tensor), so their conventions and glossaries could not be matched against this note's. Only geodesic-deviation-equation is needed at entry, and it exists.
- The flagship visual falling-ring-of-crumbs is still a proposal, so all four {id, preset, tour} references cite no preset or tour. The sketch is physically sound: a ring in a uniform ball stays round, a radial boost changes nothing, and a sideways boost grows the radial and polar entries, all of which this review checked.
- analogies is still empty, as the previous two passes recorded. Nothing in the physics blocks adding one.
- The earlier physics record, covering revision 4 with its own verification list, is preserved at snapshots/notes-curvature/relativistic-tidal-tensor.before-physics.json; its diff_checks entry is kept in this record.

**Diff check** (2026-09-13, revision 4)

- Derivation tides-for-a-sideways-passer step 2 (reworded): antisymmetry within each index pair flips the sign twice, so R_rtrt = R_trtr = -2q/c^2; multiplying by c^2 gives -gamma^2(2+beta^2)q.: Hand algebra: R_rtrt = -R_trrt = +R_trtr; static orthonormal Schwarzschild components R_trtr = -2GM/(c^2 r^3), R_rphirphi = -GM/(c^2 r^3) with (-,+,+,+) and deviation acceleration = -E xi; boosted entry gamma^2(R_rtrt + beta^2 R_rphirphi)c^2. Python trace check of the full diagonal at beta = 0, 0.3, 0.9. → Correct and same claim as before; negative radial entry means separation, matching the note's sign convention; trace zero to rounding.
- Common question why-do-they-balance (reworded): in a planet whose rock is equally tightly packed all the way through, the crumbs even close in from every direction.: Newtonian interior tidal eigenvalues: radial -2GM(r)/r^3 + 4 pi G rho = 4 pi G(rho - 2 rho_bar/3), transverse GM(r)/r^3 = 4 pi G rho_bar/3; uniform ball gives all three equal to 4 pi G rho/3 > 0. Checked that 'even' marks a stronger special case without claiming exclusivity. → True within scope; claims exactly what the old sentence did. Consistent with the working problem and with the preceding tunnel sentence (ball shrinks).
- If-stuck sign-confusion (split into two sentences): a pair released at rest on the radial line just outside a spherical mass separates, so its entry is negative in the course convention.: Compared with the static-frame radial entry -2q and the deviation equation sign used elsewhere in the note; confirmed 'That pair' refers to the released pair. → Correct; identical claim and scope to revision 3.
- Fix: None; no learner-visible text changed in the diff check.

**Diff check** (2026-09-13, revision 7)

- Scope of the diff: note_diff.py against the revision-6 before-reread snapshot lists exactly one learner-visible change, at the working rung: ways_in/a-passing-observer-reads-other-tides explanation, 'no one tidal field' -> 'no single tidal field'.: python3 knowledge/_tools/note_diff.py snapshots/notes-curvature/relativistic-tidal-tensor.before-reread.json (revision 6) against the working file (revision 7); grepped the whole note for 'single', 'no one', 'one tidal' and 'share' to confirm no other occurrence of the claim changed. → One changed sentence, one paragraph, one way. Nothing else learner-visible moved, so the diff check covers that sentence in its paragraph and its way.
- The reworded sentence claims exactly what the old one did: a universal negative over observers ('there is no X that all observers share'), scoped to the neighbourhood of a mass. 'no single' and 'no one' are the same quantifier over tidal fields.: Compared the two readings word by word: scope phrase ('Around a mass'), the counted noun ('tidal field'), the quantifier over observers ('all observers share'), and the following sentence naming what is shared. Checked that 'single' is not used in a second sense in the note: its only other learner-visible uses are 'a single event' (the way's simplifies) and 'a single freely falling observer' (formal check one-observer-six-numbers), both the same numeral sense. → Same claim, same scope, no new word sense. The scoping that the revision-5 physics review added is untouched.
- The claim is true in the way's stated setting: outside a non-rotating spherical mass in vacuum, two observers through one event with different four-velocities read different tidal tensors, so no tidal field is common to all of them.: python3: built the full static orthonormal Riemann tensor from the note's components with q = GM/r^3 and c = 1 (R_trtr = -2q, R_ttheta_ttheta = R_tphi_tphi = q, R_rtheta_rtheta = R_rphi_rphi = -q, R_thetaphi_thetaphi = 2q), imposed all index symmetries, then contracted E_ij = R(e_i, u, e_j, u) for u = gamma(e_t + beta e_phi) at beta = 0, 0.5, 0.9 in the basis (radial, polar, direction of motion). → beta = 0 gives q diag(-2, 1, 1); beta = 0.5 gives q diag(-3, 2, 1); beta = 0.9 gives q diag(-14.789, 13.789, 1), matching q diag(-gamma^2(2 + beta^2), gamma^2(1 + 2 beta^2), 1) exactly. Two observers at one event therefore read different tidal tensors, so the closing claim holds. Ricci and the first Bianchi sum are zero to machine precision, and every trace is zero, confirming the vacuum setting the sentence assumes.
- Counterexamples that would break the sentence still lie outside its scope after the rewording.: Re-ran the standard counterexamples on the reworded general sentence: maximally symmetric curvature R_{mu alpha nu beta} = K(g_{mu nu} g_{alpha beta} - g_{mu beta} g_{alpha nu}), for which every observer's tidal operator is -K c^2 times the projector on her own rest space (K = 0 flat space included); the non-relativistic limit beta -> 0, where all slow observers read one Newtonian matrix; and the radial faller, who reads the static pattern exactly. → The maximally symmetric cases are shared-tide cases, and all of them are excluded by the scope 'Around a mass', which the rewording preserves. The slow-observer and radial-faller cases agree with a subset of observers only, which is compatible with a universal negative over all observers; the note states both in the same way. No counterexample inside the stated scope.
- The sentence is consistent with the numbers it closes over, so it is not a stronger claim than its paragraph supports.: python3 recomputation of the way's quoted figures: low Earth orbit beta = 7.67 km/s over c gives beta^2 gamma^2; at beta = 0.5, gamma^2(1 + 2 beta^2) against the static polar entry 1 and gamma^2(2 + beta^2) against the static radial entry 2. → beta^2 gamma^2 = 6.55e-10, quoted as about 7e-10; polar ratio exactly 2 ('twice the static one'), radial ratio exactly 1.5 ('one and a half times it'). All three support the closing sentence.
- Fix: None; no learner-visible text changed in this diff check. The reworded sentence is accurate, correctly scoped and identical in claim to the sentence it replaces.
