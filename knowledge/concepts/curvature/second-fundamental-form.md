---
type: "concept"
schema_version: 2
id: "second-fundamental-form"
title: "Second fundamental form"
tagline: "How sharply a surface bends away from a flat card touching it, in every direction"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 4
updated: "2026-09-13"
aliases: ["second fundamental form of a surface"]
prerequisites: ["parametrized-surface", "induced-metric", "christoffel-symbols", "eigenvalues-and-eigenvectors", "intrinsic-versus-extrinsic-curvature", "riemann-curvature-tensor"]
leads_to: ["normal-curvature", "principal-curvatures", "extrinsic-curvature-of-a-hypersurface", "gauss-codazzi-equations", "junction-conditions", "trapped-surface", "gibbons-hawking-york-boundary-term"]
visuals: ["card-touching-a-curved-patch", "plumb-lines-along-a-walk", "paper-rolled-into-a-tube-and-a-cone"]
---

# Second fundamental form

*How sharply a surface bends away from a flat card touching it, in every direction*

`second-fundamental-form` · curvature · advanced · physics-reviewed (revision 4)

**Needs:** [[parametrized-surface]] (working) · [[induced-metric]] (working) · [[christoffel-symbols]] (working) · [[eigenvalues-and-eigenvectors]] (working) · [[intrinsic-versus-extrinsic-curvature]] (working) · [[riemann-curvature-tensor]] (formal)  
**Opens:** [[normal-curvature]] · [[principal-curvatures]] · [[extrinsic-curvature-of-a-hypersurface]] · [[gauss-codazzi-equations]] · [[junction-conditions]] · [[trapped-surface]] · [[gibbons-hawking-york-boundary-term]]  
**Related:** [[gaussian-curvature]] · [[theorema-egregium]] · [[curvature-of-a-curve]] · [[holonomy]]  
**Visuals:** ★ [[card-touching-a-curved-patch]] · [[plumb-lines-along-a-walk]] · [[paper-rolled-into-a-tube-and-a-cone]]

> Rest a flat card on top of a ball. The gap under the card grows more and more quickly as you move away from the touching point. On a drinks can lying on its side, the gap grows across the can but stays zero along its length. The second fundamental form is the rule that says how sharply a surface bends at a point, in every direction.

## You will be able to

**Entry**
- Explain how the gap under a flat card shows how sharply a surface bends at a point. `objectives/read-bending-from-a-card` ← `checks/double-the-distance`
- Explain why a surface can bend by different amounts in different directions at one point. `objectives/compare-bending-by-direction` ← `checks/card-on-a-can`
- Estimate how far someone must walk on a smooth, round ball for a plumb line to tilt by a given angle. `objectives/estimate-tilt-of-plumb-lines` ← `checks/moon-plumb-line`, `problems/bridge-towers`

**Working**
- Compute principal and normal curvatures from a surface's height over its tangent plane. `objectives/compute-principal-curvatures-from-height` ← `checks/spoon-bowl-directions`
- Compute both fundamental forms of a parametrized surface, and raise an index to find its principal curvatures. `objectives/compute-forms-from-a-parametrization` ← `checks/cone-principal-curvature`, `problems/inner-tube-torus`
- Distinguish what bending without stretching changes from what the metric alone fixes. `objectives/separate-what-bending-keeps` ← `checks/rolled-sheet-claim`

**Formal**
- Prove that the second fundamental form is a symmetric tensor tied to the derivative of the normal, and use it to classify surfaces. `objectives/prove-symmetry-and-weingarten` ← `checks/why-symmetric`, `problems/all-umbilic-surfaces`
- Decide whether a metric and a symmetric tensor can be the fundamental forms of a surface, locally and globally. `objectives/test-a-pair-of-forms` ← `checks/flat-metric-round-bending`, `checks/flat-torus-in-space`

**Research**
- Explain how extrinsic curvature enters the constraints on initial data, and why it depends on the slice. `objectives/explain-slices-and-constraints` ← `checks/curved-slice-of-flat-spacetime`

## Ways in

### 1. The gap under a flat card · entry · picture

*How can a flat card show how sharply a surface bends at a point?*

Rest a stiff, flat card on top of a basketball, so it touches the ball at one point. At 2 centimetres from the touching point, the gap is just under 2 millimetres.

Twice as far out, at 4 centimetres, the gap is about 7 millimetres. Close to the touching point, doubling the distance makes the gap about four times bigger.

On a tennis ball, the gap at 2 centimetres from the touching point is already about 7 millimetres. The gap grows more quickly on the smaller ball, and the smaller ball bends more sharply. So how quickly the gap grows as you move away from the touching point shows how sharply the surface bends.

**Try it:** Lay a ruler across the top of a football and look from the side, with your eye level with the ruler. Light shows under the ruler on both sides of the touching point, and the gap widens more and more quickly toward the ruler's ends.

**Takeaway:** The more quickly the gap under a flat card grows as you move away from the touching point, the more sharply the surface bends there.

*What this leaves out:* The gap is measured at right angles to the card. The fourfold rule holds only close to the touching point. At 8 centimetres out on a basketball, the gap is already about four and a half times the gap at 4 centimetres.

*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `checks/double-the-distance`

### 2. Along a can and across it · entry · contrast

*Can a surface bend by different amounts in different directions at one point?*

**Recap:** Rest a flat card on a surface, touching it at one point. The more quickly the gap under the card grows as you move away from that point, the more sharply the surface bends.

Lay a drinks can on its side and rest a flat card on top. The card touches the can along a line that runs the whole length of the can.

From a point on that line, move along the can's length, and the card lies on the can the whole way, so the gap stays zero. Move across the can instead, around its round side, and the gap grows.

So at one point, a surface can bend by different amounts in different directions.

The rule that says how sharply a surface bends at a point, in every direction, is called the second fundamental form.

**Try it:** Lay a ruler on top of a drinks can lying on its side, along the can's length: it touches the can the whole way. Turn the ruler to lie across the can: it touches at only one point, with light showing under both ends.

**Takeaway:** At one point, a surface can bend by different amounts in different directions: a drinks can bends across its round side but not along its length.

*What this leaves out:* In a slanting direction, the gap on the can grows too, but more slowly than directly across. Hold a card against the middle of a saddle, and the surface drops away below the card in some directions and rises above it in others. So the full rule also says to which side the surface bends.

*Continues:* `ways_in/gap-under-a-card`<br>*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `checks/card-on-a-can`

### 3. The tilting plumb line · entry · operational

*How does a plumb line carried across Earth show how sharply its surface bends?*

**Recap:** A surface bends more sharply where the gap under a flat card touching it grows more quickly as you move away, as on a small ball compared with a big one. On a drinks can, the bending differs between directions. The rule that says how sharply a surface bends at a point, in every direction, is the second fundamental form.

A plumb line is a small weight hanging on a string. It hangs at right angles to the surface of calm water nearby.

Treat Earth as a smooth, round ball. A line at right angles to a ball's surface passes through the ball's centre, just as a wheel's spokes meet its rim at right angles. So a plumb line, followed downward, points at Earth's centre.

Imagine walking halfway around Earth along the equator, about 20,000 kilometres. You end on the opposite side of Earth's centre. So, seen from far out in space, your plumb line now hangs the opposite way to a second plumb line left hanging where you started. It has tilted by half a turn, 180 degrees. Every stretch of a round ball is alike, so each degree of tilt took about 111 kilometres, which is 20,000 divided by 180.

Halfway around a smaller ball is a shorter walk, so each degree of tilt takes fewer kilometres. A smaller ball also bends more sharply, as the gap under a card shows. So on a round ball, the tilt per kilometre measures how sharply the ball bends.

Walking 1 kilometre tilts a plumb line by less than one hundredth of a degree. That is why you do not notice the bending.

**Takeaway:** On a round ball, how much a plumb line tilts for each kilometre you walk measures how sharply the ball bends: on Earth, 1 degree every 111 kilometres.

*What this leaves out:* Earth is slightly flattened. So 1 degree of tilt takes between about 110.6 and 111.7 kilometres, depending on where you are and which way you walk.

A walker can measure the tilt without seeing Earth from space. From the northern half of Earth, measure the angle between your plumb line and the pole star at night. Walk 111 kilometres toward the pole star and measure again: the angle has changed by about 1 degree. The pole star is not quite still, so measure it at the same hour by your watch each night.

On a drinks can, use a pin standing at right angles to the surface instead of a plumb line. Its tilt per centimetre matches the bending when you walk along the can or directly across it. Walk on a slant, and the pin also leans to one side of your path, so it tilts more than the can bends that way.

*Continues:* `ways_in/gap-under-a-card`, `ways_in/along-and-across-a-can`<br>*Visuals:* [[plumb-lines-along-a-walk]]<br>*See:* `checks/moon-plumb-line`, `problems/bridge-towers`

### 4. The height over the touching plane · working · calculation

*How do the bendings in all directions at a point fit into one symmetric matrix?*

In 'The gap under a flat card', doubling the distance from the touching point made the gap about four times bigger, and 'Along a can and across it' found that the answer can depend on direction. A Taylor expansion shows both at once. At a point $P$ of a smooth surface in flat space, pick one of the two unit normals $\hat{\mathbf n}$. Put Cartesian coordinates $(x, y)$ on the tangent plane, the card, with origin $P$, and measure the surface's height $z$ along $\hat{\mathbf n}$. The plane touches the surface at $P$, so the Taylor series of $z$ has no constant or linear term:

$$z = \tfrac12\left(K_{xx}x^2 + 2K_{xy}\,xy + K_{yy}\,y^2\right) + O(r^3),$$

with $r$ the distance from $P$. The symmetric matrix $K_{ij}$ is the second fundamental form at $P$ in these orthonormal coordinates.

Walk out from $P$ along the unit direction $t = (\cos\phi, \sin\phi)$. Over that line the height is $\tfrac12\kappa_n s^2$ at distance $s$, with $\kappa_n = K_{ij}t^it^j$. A circle of radius $\rho$ has height $s^2/(2\rho)$ near its lowest point, so $\kappa_n$ is the curvature of the slice through $\hat{\mathbf n}$ and $t$, positive when it bends toward $\hat{\mathbf n}$. It is the normal curvature in that direction.

A rotation of the axes diagonalizes the symmetric matrix, giving $z = \tfrac12(\kappa_1\xi^2 + \kappa_2\eta^2)$. So Euler's formula $\kappa_n = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$ holds with $\phi$ measured from the $\xi$ axis. The eigenvalues $\kappa_1 \ge \kappa_2$ are the principal curvatures, the largest and smallest normal curvatures, and their directions are perpendicular; at a point where $\kappa_1 = \kappa_2$, every direction is principal.

With $\hat{\mathbf n}$ pointing out of a ball of radius $a$, $\kappa_1 = \kappa_2 = -1/a$; out of a can of radius $a$, the values are $0$ along it and $-1/a$ across it. The saddle $z = (x^2 - y^2)/(2a)$ has $\pm 1/a$, and $\kappa_n = \cos 2\phi/a$ vanishes at $45^\circ$. Reversing $\hat{\mathbf n}$ reverses $z$ and every $\kappa$, but not the product $\kappa_1\kappa_2$. For the basketball, $a = 12$ cm gives a gap $d^2/(2a) = 0.17$ cm at $d = 2$ cm.

**Takeaway:** Near a point, the height over the tangent plane is half a symmetric quadratic form; its eigenvalues are the principal curvatures, in perpendicular directions.

*What this leaves out:* Keeps terms to second order in the distance from the point; the cubic terms describe how the bending changes from point to point.

*Continues:* `ways_in/gap-under-a-card`, `ways_in/along-and-across-a-can`<br>*Builds on:* [[eigenvalues-and-eigenvectors]]<br>*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `derivations/height-from-a-taylor-expansion`, `worked_examples/crisp-with-a-twist`, `checks/spoon-bowl-directions`

### 5. How the basis vectors change · working · calculation

*How do you compute the second fundamental form from any parametrization of a surface?*

The height over the touching plane needs special coordinates at each point. A parametrization $\mathbf X(x^1, x^2)$ of a surface in $\mathbb R^3$ works everywhere at once. Its basis vectors $\mathbf e_\mu = \partial_\mu\mathbf X$ span the tangent plane, $g_{\mu\nu} = \mathbf e_\mu\cdot\mathbf e_\nu$ is the induced metric, classically called the first fundamental form, and $\hat{\mathbf n} = \mathbf e_1\times\mathbf e_2/|\mathbf e_1\times\mathbf e_2|$ is a unit normal.

Split the change of each basis vector into tangential and normal parts:

$$\partial_\mu\mathbf e_\nu = \Gamma^\lambda{}_{\mu\nu}\,\mathbf e_\lambda + K_{\mu\nu}\,\hat{\mathbf n}.$$

This is Gauss's formula. Dotting it with $\mathbf e_\sigma$ and differentiating $g_{\sigma\nu} = \mathbf e_\sigma\cdot\mathbf e_\nu$ shows that the tangential coefficients are the Christoffel symbols of $g_{\mu\nu}$. The normal coefficients, $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$, are the second fundamental form. They are symmetric because partial derivatives commute, and they change sign with $\hat{\mathbf n}$. Where the $\mathbf e_\mu$ are orthonormal at $P$, the $K_{\mu\nu}$ at $P$ are the height matrix $K_{ij}$, because $\hat{\mathbf n}\cdot(\mathbf X - \mathbf X_P) = \tfrac12K_{\mu\nu}x^\mu x^\nu + O(x^3)$.

The normal tilts as well. Differentiating $\hat{\mathbf n}\cdot\mathbf e_\nu = 0$ and $\hat{\mathbf n}\cdot\hat{\mathbf n} = 1$ gives Weingarten's equation, $\partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda$ with $K^\lambda{}_\mu = g^{\lambda\nu}K_{\nu\mu}$. This is the plumb line of 'The tilting plumb line' in formulas. On a sphere of radius $a$ with the outward normal, $K^\lambda{}_\mu = -\delta^\lambda{}_\mu/a$, so the normal tilts by $1/a$ radians per unit distance in every direction: for Earth, $1/6371$ rad per km, or $1^\circ$ per $111$ km.

Along a unit-speed curve with unit tangent $t^\mu$, the normal part of $d\mathbf t/ds$ is $K_{\mu\nu}t^\mu t^\nu$, the normal curvature $\kappa_n$. By Weingarten's equation the normal tilts at the rate $d\hat{\mathbf n}/ds = -K^\lambda{}_\mu t^\mu\,\mathbf e_\lambda$, whose component along $\mathbf t$ is $-\kappa_n$; its part perpendicular to $\mathbf t$ vanishes only along principal directions. The extremes of $\kappa_n$ over directions with $g_{\mu\nu}t^\mu t^\nu = 1$ are the eigenvalues of $K^\mu{}_\nu$, which in general differ from those of the component matrix $K_{\mu\nu}$ unless $g_{\mu\nu} = \delta_{\mu\nu}$ there. So the invariant summaries are

$$\kappa_1\kappa_2 = \frac{\det K_{\mu\nu}}{\det g_{\mu\nu}},\qquad \kappa_1 + \kappa_2 = g^{\mu\nu}K_{\mu\nu}.$$

The product is the Gaussian curvature, and half the sum is the mean curvature.

**Takeaway:** Split each basis vector's change into a tangential part, the Christoffel symbols, and a normal part, the second fundamental form; the normal's own change is that form with an index raised.

*What this leaves out:* Assumes a $C^2$ surface in flat three-dimensional space; at a crease or a cone tip the second derivatives, and so $K_{\mu\nu}$, do not exist.

*Continues:* `ways_in/height-over-the-touching-plane`, `ways_in/tilting-plumb-line`<br>*Builds on:* [[parametrized-surface]], [[induced-metric]], [[christoffel-symbols]]<br>*Visuals:* [[plumb-lines-along-a-walk]]<br>*See:* `key_equations/gauss-formula`, `derivations/weingarten-from-orthogonality`, `derivations/normal-curvature-along-a-curve`, `checks/cone-principal-curvature`

### 6. Bending without stretching · working · contrast

*How much of the second fundamental form could someone living on the surface measure?*

The normal $\hat{\mathbf n}$ used in 'How the basis vectors change' points out of the surface, where someone living on the surface cannot look. How much of $K_{\mu\nu}$ can such an insider recover? Roll a flat sheet into a can of radius $a$, with arc length $u$ around it and $v$ along it as coordinates. Lengths drawn on the paper do not change, so $g_{\mu\nu} = \delta_{\mu\nu}$ before and after. But $K_{\mu\nu}$ goes from zero to $K_{uu} = -1/a$ with the outward normal, and the mean curvature goes from $0$ to $-1/(2a)$. So the metric does not determine the second fundamental form, or even the mean curvature.

The product $\kappa_1\kappa_2$ is zero before and after. That is no accident: Gauss's theorema egregium, taken on trust here, says the product depends only on $g_{\mu\nu}$ and its first two derivatives. So bending without stretching can reshape the principal curvatures only in ways that keep their product.

Two consequences can be felt. Curve a flat slice of pizza across its width, so one principal curvature is nonzero: the other must vanish, so the slice stays straight along its length instead of drooping, as long as it does not stretch. A piece of orange peel has $\kappa_1\kappa_2 > 0$, so it cannot be pressed flat without stretching.

**Takeaway:** Bending without stretching keeps the metric but changes the second fundamental form; only the product of the principal curvatures is fixed by the metric.

*Continues:* `ways_in/how-basis-vectors-change`<br>*Builds on:* [[intrinsic-versus-extrinsic-curvature]]<br>*Visuals:* [[paper-rolled-into-a-tube-and-a-cone]]<br>*See:* `checks/rolled-sheet-claim`

### 7. Gauss, Weingarten and Bonnet without coordinates · formal · structure

*What is the second fundamental form as a geometric object, which equations does it obey, and when do a metric and a symmetric tensor make a surface?*

The split of $\partial_\mu\mathbf e_\nu$ into Christoffel symbols and the second fundamental form, in 'How the basis vectors change', has a coordinate-free form for any hypersurface. Let $\Sigma$ be a hypersurface of a Riemannian manifold $(M, \bar g)$ with Levi-Civita connection $\bar\nabla$, induced metric $g$, and unit normal field $N$. $N$ exists locally, and globally when $\Sigma$ is two-sided. For vector fields $X, Y$ tangent to $\Sigma$,

$$\bar\nabla_XY = \nabla_XY + \mathrm{II}(X,Y)\,N,\qquad \bar\nabla_XN = -S(X).$$

The first is the Gauss formula. Its tangential part $\nabla$ is torsion-free and compatible with $g$, so it is the Levi-Civita connection of $g$, and its normal part defines $\mathrm{II}(X,Y) = \bar g(\bar\nabla_XY, N)$. The second is the Weingarten equation: $\bar g(N,N) = 1$ makes $\bar\nabla_XN$ tangent, and differentiating $\bar g(Y,N) = 0$ gives $g(S(X), Y) = \mathrm{II}(X,Y)$. The shape operator $S$ is $\mathrm{II}$ with an index raised; in components $S^\mu{}_\nu = K^\mu{}_\nu$.

Three properties follow. $\mathrm{II}$ is a tensor: it is $C^\infty$-linear in $Y$ because $\bar g(Y,N) = 0$ absorbs the derivative of a coefficient. It is symmetric: $\mathrm{II}(X,Y) - \mathrm{II}(Y,X) = \bar g([X,Y], N) = 0$, because $\bar\nabla$ is torsion-free and the bracket of tangent fields is tangent. So $S$ is self-adjoint, with real eigenvalues, the principal curvatures, and a $g$-orthonormal eigenbasis, the principal directions.

Expanding $\bar R(X,Y)Z$ with both formulas and taking tangential and normal parts gives, with all indices tangent and the course Riemann convention,

$$R_{\rho\sigma\mu\nu} = \bar R_{\rho\sigma\mu\nu} + K_{\rho\mu}K_{\sigma\nu} - K_{\rho\nu}K_{\sigma\mu},\qquad \nabla_\mu K_{\nu\sigma} - \nabla_\nu K_{\mu\sigma} = \bar R_{\rho\sigma\mu\nu}N^\rho.$$

These are the Gauss and Codazzi equations. For a surface in $\mathbb R^3$, $\bar R = 0$ and $R_{1212} = \det K_{\mu\nu}$, so $\kappa_1\kappa_2 = R_{1212}/\det g_{\mu\nu}$ is fixed by $g$: the theorema egregium. The sum $\kappa_1 + \kappa_2$ is not fixed by $g$: a flat sheet and a rolled tube share a metric.

The Gauss and Codazzi equations are necessary conditions on a pair of forms. For surfaces in $\mathbb R^3$ they are also locally sufficient. Bonnet's theorem: let $U \subset \mathbb R^2$ be open and simply connected, $g_{\mu\nu}$ a smooth metric and $K_{\mu\nu}$ a smooth symmetric tensor on $U$ satisfying $\det K_{\mu\nu} = R_{1212}[g]$ and $\nabla_\mu K_{\nu\sigma} = \nabla_\nu K_{\mu\sigma}$. Then there is an immersion $\mathbf X: U \to \mathbb R^3$ with these first and second fundamental forms, for the normal $\mathbf e_1\times\mathbf e_2/|\mathbf e_1\times\mathbf e_2|$, unique up to a rotation and a translation.

Proof sketch. The Gauss and Weingarten formulas form a linear system $\partial_\mu F = F A_\mu$ for the frame $F = (\mathbf e_1, \mathbf e_2, \hat{\mathbf n})$, with $3\times3$ matrices $A_\mu$ built from $\Gamma$ and $K$. Its integrability condition, $\partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu] = 0$, has the Gauss and Codazzi equations as its components. By the Frobenius theorem, on a simply connected domain the system has a unique solution for each initial frame. Choose an initial frame with $\mathbf e_\mu\cdot\mathbf e_\nu = g_{\mu\nu}$, $\hat{\mathbf n}$ a positively oriented unit normal; the system preserves these inner products because its $\Gamma$ are those of $g$. Finally $\partial_\mu\mathbf e_\nu$ is symmetric, so $\mathbf e_\mu\,dx^\mu$ is closed and integrates to $\mathbf X$. Two admissible initial frames differ by a rotation, and the integration constant is a translation.

The theorem is local, and global conditions add more. At a point of a compact $C^2$ surface in $\mathbb R^3$ farthest from the origin, the surface lies inside a sphere touching it there, so $\kappa_1\kappa_2 > 0$ at that point. Hence the flat torus has no $C^2$ isometric embedding in $\mathbb R^3$, although $C^1$ ones exist by the Nash–Kuiper theorem. One metric can also carry many second fundamental forms: a flat sheet rolls into tubes and cones, and small pieces of a sphere can be bent, while a whole round sphere is rigid among $C^2$ surfaces, by Liebmann's theorem.

Limits of validity. $\mathrm{II}$, $S$ and every $\kappa_i$ flip sign with $N$; the Gauss equation, quadratic in $K$, does not. In higher codimension $\mathrm{II}$ takes values in the normal bundle. If $\bar g$ is indefinite and $\bar g(N,N) = \epsilon = \pm1$, the Gauss formula carries $\epsilon\,\mathrm{II}(X,Y)N$ and the quadratic terms carry a factor $\epsilon$. A null hypersurface has no unit normal, and the construction must be modified. At a crease or a cone tip, $\mathrm{II}$ is undefined as a function.

**Takeaway:** The second fundamental form is a symmetric tensor, the normal part of the ambient derivative; in flat space a metric and such a tensor form a surface, locally and up to rigid motion, exactly when Gauss and Codazzi hold.

*What this leaves out:* Takes $\Sigma$ to be a $C^3$ hypersurface with a chosen unit normal, and uses the course Riemann convention throughout.

*Continues:* `ways_in/how-basis-vectors-change`, `ways_in/bending-without-stretching`<br>*Builds on:* [[riemann-curvature-tensor]], [[levi-civita-connection]], [[lie-bracket]]<br>*See:* `derivations/gauss-and-codazzi-from-third-derivatives`, `checks/why-symmetric`, `problems/all-umbilic-surfaces`, `checks/flat-metric-round-bending`, `checks/flat-torus-in-space`

### 8. Slices of spacetime · research · bridge

*What does the second fundamental form do in general relativity?*

The Gauss and Codazzi equations of 'Gauss, Weingarten and Bonnet without coordinates' carry over to spacetime with one sign change. Set $G = c = 1$. Let $\Sigma$ be a spacelike slice with future unit normal $n$, $n\cdot n = -1$, induced metric $h_{ij}$, and extrinsic curvature $K_{ij}$, its second fundamental form. Up to a sign that differs between conventions, $K_{ij}$ is half the rate at which $h_{ij}$ changes when each point of $\Sigma$ moves along $n$ by unit proper time: the velocity of the spatial geometry.

With $\epsilon = -1$, contracting the Gauss equation twice and using Einstein's equation with $\Lambda = 0$ gives the Hamiltonian constraint

$${}^{(3)}\!R + \left(h^{ij}K_{ij}\right)^2 - K_{ij}K^{ij} = 16\pi\rho,$$

where $\rho = T_{\mu\nu}n^\mu n^\nu$ is the energy density measured by observers moving along $n$. The Codazzi equation gives three momentum constraints, which relate $D_jK^j{}_i - D_i(h^{jk}K_{jk})$ to the momentum density those observers measure. As Bonnet's conditions decide which pairs of forms make a surface, these four equations decide which pairs $(h_{ij}, K_{ij})$ can be initial data; the remaining Einstein equations evolve them. The Hamiltonian 3+1 formulation of general relativity, and numerical simulations of merging black holes, start here.

The same object does three other jobs.

- Across a thin shell of matter, $h_{ij}$ is continuous but $K_{ij}$ jumps, and Israel's junction conditions set the jump by the shell's surface stress-energy.
- A closed spacelike two-surface has two future null normal directions. The traces of its second fundamental forms along them give, up to a conventional sign, the expansions of the light rays leaving it. If both expansions are negative the surface is trapped, the key hypothesis of Penrose's singularity theorem; horizon finders locate apparent horizons as marginally outer trapped surfaces.
- The Einstein–Hilbert action needs a boundary term built from the trace of the boundary's extrinsic curvature for its variational principle to be well posed. The trace of a closed two-surface's extrinsic curvature within a slice, compared with the same two-surface embedded in flat space, defines the Brown–York quasi-local energy.

A slice's $K_{ij}$ describes the slice, not spacetime alone: flat spacetime contains slices with $K_{ij} \neq 0$.

**Takeaway:** On a slice of spacetime the second fundamental form is the extrinsic curvature, and its Gauss and Codazzi equations become the constraints on initial data.

*What this leaves out:* Takes the slice to be spacelike and smooth; null surfaces need a null normal whose scale is not fixed, and the sign of $K_{ij}$ is left unfixed.

*Continues:* `ways_in/gauss-and-weingarten-without-coordinates`<br>*See:* `checks/curved-slice-of-flat-spacetime`, `research_horizon/initial-data-and-the-3-plus-1-split`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| second fundamental form | — | The rule that says how sharply a surface bends away from a flat card touching it, in every direction at a point, and to which side. The first fundamental form is the rule for measuring lengths along the surface. | [[second-fundamental-form]] |
| plumb line | PLUM line | A small weight hanging on a string. It hangs at right angles to the surface of calm water nearby, so it shows which way is up. | — |
| equator | — | The circle around Earth's middle, the same distance from both poles. | — |
| pole star | — | A star seen almost exactly overhead from Earth's North Pole. Through the night it stays almost still in the sky while the other stars circle around it. | — |

## Key equations

### Height over the tangent plane · working

$$
z = \tfrac12 K_{ij}\,x^i x^j + O(r^3)
$$

Near a point, the height along the chosen normal over orthonormal tangent-plane coordinates is half the second fundamental form applied twice to the position.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $z$ | height along $\hat{\mathbf n}$ above the tangent plane | the height |
| $K_{ij}$ | second fundamental form in orthonormal tangent-plane coordinates | K i j |
| $x^i$ | tangent-plane coordinates centred on the point, at distance $r$ | the position |

**Holds when:** $C^3$ surface in flat space; orthonormal coordinates at the point; sign set by $\hat{\mathbf n}$.  
**Say it:** “The height is one half of K i j times x i times x j, plus third-order terms.”  
**Justified by:** `derivations/height-from-a-taylor-expansion`

### Gauss's formula · working

$$
\partial_\mu\mathbf e_\nu = \Gamma^\lambda{}_{\mu\nu}\,\mathbf e_\lambda + K_{\mu\nu}\,\hat{\mathbf n}
$$

The change of a basis vector splits into a part along the surface, given by the Christoffel symbols, and a part along the normal, given by the second fundamental form.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathbf e_\mu$ | coordinate basis vector $\partial_\mu\mathbf X$ | e mu |
| $\Gamma^\lambda{}_{\mu\nu}$ | Christoffel symbols of the induced metric | gamma lambda mu nu |
| $K_{\mu\nu}$ | second fundamental form, $\hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$ | K mu nu |
| $\hat{\mathbf n}$ | chosen unit normal | n hat |

**Holds when:** $C^2$ surface in flat three-dimensional space; $K_{\mu\nu}$ changes sign with $\hat{\mathbf n}$.  
**Say it:** “The derivative of e nu along mu is gamma lambda mu nu times e lambda, plus K mu nu times the unit normal.”  
**Justified by:** `christoffel-symbols`

### Weingarten's equation · working

$$
\partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda,\qquad K^\lambda{}_\mu = g^{\lambda\nu}K_{\nu\mu}
$$

The unit normal tilts along the surface by the second fundamental form with one index raised.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\partial_\mu\hat{\mathbf n}$ | change of the unit normal along $x^\mu$ | the derivative of the normal |
| $K^\lambda{}_\mu$ | second fundamental form with an index raised by the inverse metric, the shape operator | K lambda mu |
| $g^{\lambda\nu}$ | inverse induced metric | g upper lambda nu |

**Holds when:** $C^2$ surface in flat three-dimensional space.  
**Say it:** “The derivative of the normal along mu is minus K lambda mu times e lambda.”  
**Justified by:** `derivations/weingarten-from-orthogonality`

### Normal curvature · working

$$
\kappa_n = K_{\mu\nu}\,t^\mu t^\nu,\qquad g_{\mu\nu}t^\mu t^\nu = 1
$$

The bending of the surface toward the normal in a unit direction is the second fundamental form applied twice to that direction.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa_n$ | normal curvature, positive when the surface bends toward $\hat{\mathbf n}$ | kappa n |
| $t^\mu$ | components of a unit tangent direction | t mu |

**Holds when:** Unit direction measured with the induced metric.  
**Say it:** “The normal curvature is K mu nu times t mu times t nu, for a unit direction t.”  
**Justified by:** `derivations/normal-curvature-along-a-curve`

### Product and sum of the principal curvatures · working

$$
\kappa_1\kappa_2 = \frac{\det K_{\mu\nu}}{\det g_{\mu\nu}},\qquad \kappa_1 + \kappa_2 = g^{\mu\nu}K_{\mu\nu}
$$

The principal curvatures are the eigenvalues of $K^\mu{}_\nu$; their product is the Gaussian curvature and their sum is twice the mean curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa_1, \kappa_2$ | principal curvatures, the extreme normal curvatures | kappa one and kappa two |
| $\det K_{\mu\nu}$ | determinant of the component matrix of the second fundamental form | the determinant of K |
| $\det g_{\mu\nu}$ | determinant of the metric components | the determinant of g |

**Holds when:** Surface in flat three-dimensional space. The sum changes sign with $\hat{\mathbf n}$; the product does not.  
**Say it:** “Kappa one times kappa two is det K over det g; kappa one plus kappa two is the trace of K.”  
**Justified by:** `eigenvalues-and-eigenvectors`

### Gauss equation · formal

$$
R_{\rho\sigma\mu\nu} = \bar R_{\rho\sigma\mu\nu} + K_{\rho\mu}K_{\sigma\nu} - K_{\rho\nu}K_{\sigma\mu}
$$

A hypersurface's own Riemann tensor is the tangential part of the ambient Riemann tensor plus a term quadratic in the second fundamental form.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R_{\rho\sigma\mu\nu}$ | Riemann tensor of the induced metric, course convention | R rho sigma mu nu |
| $\bar R_{\rho\sigma\mu\nu}$ | ambient Riemann tensor with all slots tangent | R bar rho sigma mu nu |

**Holds when:** Hypersurface with $\bar g(N,N) = +1$; for $-1$ the quadratic terms change sign. $\bar R = 0$ in flat space.  
**Say it:** “R rho sigma mu nu equals R bar rho sigma mu nu, plus K rho mu K sigma nu, minus K rho nu K sigma mu.”  
**Justified by:** `derivations/gauss-and-codazzi-from-third-derivatives`

### Codazzi equation · formal

$$
\nabla_\mu K_{\nu\sigma} - \nabla_\nu K_{\mu\sigma} = \bar R_{\rho\sigma\mu\nu}N^\rho
$$

The antisymmetrized derivative of the second fundamental form is the ambient curvature with one slot along the normal; in flat space it vanishes.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\nabla_\mu$ | covariant derivative of the induced metric | nabla mu |
| $N^\rho$ | unit normal | N rho |

**Holds when:** Hypersurface with unit normal $N$, $\bar g(N,N) = \pm1$; lower indices tangent.  
**Say it:** “Nabla mu of K nu sigma minus nabla nu of K mu sigma equals the ambient Riemann tensor with its first slot along the normal.”  
**Justified by:** `derivations/gauss-and-codazzi-from-third-derivatives`

## Derivations

### The height from a Taylor expansion · working

**Goal:** Show that the height of a surface over its tangent plane at $P$ is $\tfrac12K_{ij}x^ix^j$ to second order, with $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$.

1. Choose coordinates with $\mathbf X(0) = \mathbf X_P$ and expand: $\mathbf X(x) = \mathbf X_P + \mathbf e_\mu x^\mu + \tfrac12\partial_\mu\partial_\nu\mathbf X\,x^\mu x^\nu + O(x^3)$, with derivatives at $P$.
2. The height along the normal is $z = \hat{\mathbf n}\cdot(\mathbf X - \mathbf X_P)$. The linear term drops because $\hat{\mathbf n}\cdot\mathbf e_\mu = 0$, leaving $z = \tfrac12K_{\mu\nu}x^\mu x^\nu + O(x^3)$.
3. If the $\mathbf e_\mu$ are orthonormal at $P$, the tangent-plane coordinates $\mathbf e_\mu\cdot(\mathbf X - \mathbf X_P)$ equal $x^\mu + O(x^2)$. Using them instead of $x^\mu$ changes $z$ only at third order.

**Result:** $z = \tfrac12K_{ij}x^ix^j + O(r^3)$ in orthonormal tangent-plane coordinates.

### Weingarten's equation from orthogonality · working

**Goal:** Show that $\partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda$.

1. $\hat{\mathbf n}\cdot\hat{\mathbf n} = 1$, so $2\,\hat{\mathbf n}\cdot\partial_\mu\hat{\mathbf n} = 0$: the derivative of the normal is tangent, $\partial_\mu\hat{\mathbf n} = c^\lambda{}_\mu\,\mathbf e_\lambda$ for some coefficients $c^\lambda{}_\mu$.
2. $\hat{\mathbf n}\cdot\mathbf e_\nu = 0$ everywhere, so $\partial_\mu\hat{\mathbf n}\cdot\mathbf e_\nu = -\hat{\mathbf n}\cdot\partial_\mu\mathbf e_\nu = -K_{\mu\nu}$ by Gauss's formula.
3. Insert the tangent expansion: $c^\lambda{}_\mu\,g_{\lambda\nu} = -K_{\mu\nu}$.
4. Multiply by $g^{\nu\sigma}$ and use the symmetry of $K_{\mu\nu}$: $c^\sigma{}_\mu = -g^{\sigma\nu}K_{\nu\mu} = -K^\sigma{}_\mu$.

**Result:** $\partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda$.

### Normal curvature along a curve · working

**Goal:** Show that every unit-speed curve with unit tangent $t^\mu$ has normal curvature $K_{\mu\nu}t^\mu t^\nu$.

1. Write the curve as $x^\mu(s)$ with arc length $s$. Its unit tangent is $\mathbf t = t^\mu\mathbf e_\mu$ with $t^\mu = dx^\mu/ds$.
2. Differentiate with the chain rule: $d\mathbf t/ds = (dt^\mu/ds)\,\mathbf e_\mu + t^\mu t^\nu\,\partial_\nu\mathbf e_\mu$.
3. Dot with $\hat{\mathbf n}$. The first term is tangent and drops, and Gauss's formula gives $\hat{\mathbf n}\cdot\partial_\nu\mathbf e_\mu = K_{\nu\mu}$.

**Result:** $\kappa_n \equiv \hat{\mathbf n}\cdot d\mathbf t/ds = K_{\mu\nu}t^\mu t^\nu$, the same for every curve through the point in the direction $t^\mu$.

### Gauss and Codazzi from third derivatives · formal

**Goal:** Derive the Gauss and Codazzi equations for a surface in $\mathbb R^3$, in the course convention for the Riemann tensor.

1. Third partial derivatives of a $C^3$ map commute, so $\partial_\mu(\partial_\nu\mathbf e_\sigma) = \partial_\nu(\partial_\mu\mathbf e_\sigma)$.
2. Differentiate Gauss's formula, then use it again together with Weingarten's equation: $\partial_\mu\partial_\nu\mathbf e_\sigma = \big(\partial_\mu\Gamma^\rho{}_{\nu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - K_{\nu\sigma}K^\rho{}_\mu\big)\,\mathbf e_\rho + \big(\partial_\mu K_{\nu\sigma} + \Gamma^\lambda{}_{\nu\sigma}K_{\mu\lambda}\big)\,\hat{\mathbf n}$.
3. Subtract the same expression with $\mu$ and $\nu$ exchanged, and set the tangential part to zero: $\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma} = K^\rho{}_\mu K_{\nu\sigma} - K^\rho{}_\nu K_{\mu\sigma}$.
4. The left side is the course $R^\rho{}_{\sigma\mu\nu}$. Lowering $\rho$ with $g_{\rho\lambda}$ gives $R_{\rho\sigma\mu\nu} = K_{\rho\mu}K_{\sigma\nu} - K_{\rho\nu}K_{\sigma\mu}$.
5. Set the normal part to zero: $\partial_\mu K_{\nu\sigma} - \partial_\nu K_{\mu\sigma} + \Gamma^\lambda{}_{\nu\sigma}K_{\mu\lambda} - \Gamma^\lambda{}_{\mu\sigma}K_{\nu\lambda} = 0$.
6. Add and subtract $\Gamma^\lambda{}_{\mu\nu}K_{\lambda\sigma}$, which is symmetric in $\mu\nu$. The left side becomes $\nabla_\mu K_{\nu\sigma} - \nabla_\nu K_{\mu\sigma}$.
7. Check on a sphere of radius $a$ with the outward normal: $K_{\theta\theta}K_{\phi\phi} - K_{\theta\phi}^2 = (-a)(-a\sin^2\theta) = a^2\sin^2\theta$, the positive $R_{\theta\phi\theta\phi}$ of the course convention.

**Result:** $R_{\rho\sigma\mu\nu} = K_{\rho\mu}K_{\sigma\nu} - K_{\rho\nu}K_{\sigma\mu}$ and $\nabla_\mu K_{\nu\sigma} = \nabla_\nu K_{\mu\sigma}$ for a $C^3$ surface in flat three-dimensional space.

## Worked examples

### A crisp with a twist · working

**Problem:** The middle of a crisp has height $z = xy/a$ over its tangent plane, with $a = 4$ cm and $\hat{\mathbf n}$ along $+z$. Find the principal curvatures and directions, and the product and mean curvature there.

1. Match $z = \tfrac12(K_{xx}x^2 + 2K_{xy}xy + K_{yy}y^2)$: $K_{xx} = K_{yy} = 0$ and $K_{xy} = 1/a$.
2. The eigenvalues of $\begin{pmatrix}0 & 1/a\\ 1/a & 0\end{pmatrix}$ solve $\kappa^2 = 1/a^2$, so $\kappa_{1,2} = \pm1/a = \pm0.25$ cm$^{-1}$, radii of curvature $4$ cm.
3. The eigenvectors are $(1,1)/\sqrt2$ for $+1/a$ and $(1,-1)/\sqrt2$ for $-1/a$: along $y = x$ the crisp bends toward $\hat{\mathbf n}$, and along $y = -x$ away from it.
4. Along the $x$ and $y$ axes $z = 0$ exactly, and $K_{ij}t^it^j = \sin2\phi/a$ vanishes at $\phi = 0$ and $90^\circ$.
5. The product is $-1/a^2 = -0.0625$ cm$^{-2}$, and the mean curvature $\tfrac12(\kappa_1 + \kappa_2)$ is $0$.

**Answer:** $\kappa = \pm0.25$ cm$^{-1}$ along the diagonals $y = \pm x$; product $-0.0625$ cm$^{-2}$; mean curvature $0$ at the middle.

**Takeaway:** An off-diagonal term rotates the principal directions away from the axes; this is the saddle $z = (x^2 - y^2)/(2a)$ turned by $45^\circ$.

## Problems

### `bridge-towers` · entry · difficulty 2 · estimate

The two towers of a long bridge stand 1,410 metres apart. Each tower is 155 metres tall and is built along its own plumb line. Treat Earth as a smooth, round ball whose centre is 6,371 kilometres below the bases. How much farther apart are the tops of the towers than their bases?

**Hints**

1. If you follow the two plumb lines down, where do they meet?
2. The two plumb lines are the long sides of a very thin triangle with its tip at Earth's centre.

**Answer:** About 3.4 centimetres farther apart at the top.

**Must contain:** Both plumb lines point at Earth's centre; The gap grows in step with the distance from the centre; About 3.4 centimetres

**Numeric:** extra separation of the tops = 3.43 cm (magnitude, ±0.2)

**Solution**

1. On a round ball, each plumb line points at the centre. So the towers lean apart like the long sides of a thin triangle with its tip at Earth's centre.
2. In such a triangle the gap between the sides grows in step with the distance from the tip. That is because a triangle cut off closer to the tip has the same shape, only smaller. At the bases, 6,371,000 metres from the tip, the gap is 1,410 metres.
3. So each extra metre out from the centre adds 1,410 divided by 6,371,000 metres of gap.
4. The tops are 155 metres farther out, so the extra gap is 155 times that: about 0.034 metres, or 3.4 centimetres.

### `inner-tube-torus` · working · difficulty 2 · calculation

A bicycle inner tube is roughly the torus $\mathbf X(u,v) = \big((b + a\cos v)\cos u,\ (b + a\cos v)\sin u,\ a\sin v\big)$ with $b = 30$ cm and $a = 2.5$ cm. Using the outward normal, find $g_{\mu\nu}$, $K_{\mu\nu}$, the principal curvatures, and $\kappa_1\kappa_2$ on the outer equator $v = 0$, the inner equator $v = \pi$, and the top circle $v = \pi/2$.

**Hints**

1. Try $\hat{\mathbf n} = (\cos v\cos u, \cos v\sin u, \sin v)$ and check that it is perpendicular to $\mathbf e_u$ and $\mathbf e_v$.
2. The metric is diagonal, so raising an index divides each diagonal component of the second fundamental form by the matching metric component.

**Answer:** $g = \mathrm{diag}\big((b + a\cos v)^2, a^2\big)$, $K = \mathrm{diag}\big(-(b + a\cos v)\cos v,\ -a\big)$, principal curvatures $-\cos v/(b + a\cos v)$ and $-1/a$, product $\cos v/\big(a(b + a\cos v)\big)$: $+123$ m$^{-2}$ on the outer equator, $-145$ m$^{-2}$ on the inner equator, $0$ on the top circle.

**Must contain:** Diagonal metric and diagonal second fundamental form; Raise the index before reading principal curvatures; Product positive outside, negative inside, zero on top

**Numeric:** product of principal curvatures on the outer equator = 123.1 m^-2 (signed, ±1%); product of principal curvatures on the inner equator = -145.5 m^-2 (signed, ±1%)

**Solution**

1. $\mathbf e_u = (b + a\cos v)(-\sin u, \cos u, 0)$ and $\mathbf e_v = a(-\sin v\cos u, -\sin v\sin u, \cos v)$, so $g_{uu} = (b + a\cos v)^2$, $g_{vv} = a^2$ and $g_{uv} = 0$.
2. $\hat{\mathbf n} = (\cos v\cos u, \cos v\sin u, \sin v)$ is a unit vector perpendicular to both, pointing away from the centre circle of the tube, and it equals $\mathbf e_u\times\mathbf e_v/|\mathbf e_u\times\mathbf e_v|$.
3. $\partial_u\mathbf e_u = -(b + a\cos v)(\cos u, \sin u, 0)$ gives $K_{uu} = -(b + a\cos v)\cos v$. $\partial_v\mathbf e_v = -a(\cos v\cos u, \cos v\sin u, \sin v)$ gives $K_{vv} = -a$. $\partial_u\mathbf e_v = a\sin v(\sin u, -\cos u, 0)$ gives $K_{uv} = 0$.
4. Raising an index: $\kappa_u = -\cos v/(b + a\cos v)$ and $\kappa_v = -1/a$, so $\kappa_u\kappa_v = \cos v/\big(a(b + a\cos v)\big)$.
5. At $v = 0$: $1/(0.025\ \mathrm{m}\times0.325\ \mathrm{m}) = 123$ m$^{-2}$, bending to one side in every direction. At $v = \pi$: $\kappa_u = +3.6$ m$^{-1}$ and $\kappa_v = -40$ m$^{-1}$, product $-1/(0.025\ \mathrm{m}\times0.275\ \mathrm{m}) = -145$ m$^{-2}$, a saddle. At $v = \pi/2$: $\kappa_u = 0$ and the product is $0$.

**Targets:** `eigenvalues-of-lower-k`

### `all-umbilic-surfaces` · formal · difficulty 3 · proof

A connected $C^3$ surface in $\mathbb R^3$ has $K_{\mu\nu} = c\,g_{\mu\nu}$ at every point, for some function $c$. Prove that $c$ is constant, and that the surface is part of a plane or of a sphere of radius $1/|c|$.

**Hints**

1. Weingarten's equation becomes $\partial_\mu\hat{\mathbf n} = -c\,\mathbf e_\mu$.
2. Differentiate once more and use $\partial_\mu\mathbf e_\nu = \partial_\nu\mathbf e_\mu$.

**Answer:** Commuting second derivatives of $\hat{\mathbf n}$ force $\partial_\mu c = 0$. If $c = 0$ the normal is constant and the surface is planar; if $c \neq 0$ then $\mathbf X + \hat{\mathbf n}/c$ is a fixed point at distance $1/|c|$.

**Must contain:** Weingarten gives the derivative of the normal as minus c times e mu; Commuting derivatives force c constant; c zero gives a plane; c nonzero gives a sphere

**Solution**

1. With $K_{\mu\nu} = c\,g_{\mu\nu}$, $K^\sigma{}_\mu = c\,\delta^\sigma{}_\mu$, and Weingarten's equation reads $\partial_\mu\hat{\mathbf n} = -c\,\mathbf e_\mu$.
2. Differentiate: $\partial_\nu\partial_\mu\hat{\mathbf n} = -(\partial_\nu c)\,\mathbf e_\mu - c\,\partial_\nu\mathbf e_\mu$. The left side and the last term are symmetric in $\mu\nu$, so $(\partial_\nu c)\,\mathbf e_\mu = (\partial_\mu c)\,\mathbf e_\nu$.
3. Take $\mu = 1$ and $\nu = 2$. Since $\mathbf e_1$ and $\mathbf e_2$ are linearly independent, $\partial_1c = \partial_2c = 0$, and on a connected surface $c$ is constant.
4. If $c = 0$, $\hat{\mathbf n}$ is constant, so $\partial_\mu(\hat{\mathbf n}\cdot\mathbf X) = \hat{\mathbf n}\cdot\mathbf e_\mu = 0$ and the surface lies in a plane.
5. If $c \neq 0$, $\partial_\mu(\mathbf X + \hat{\mathbf n}/c) = \mathbf e_\mu - \mathbf e_\mu = 0$, so $\mathbf X + \hat{\mathbf n}/c = \mathbf C$ is fixed and $|\mathbf X - \mathbf C| = 1/|c|$. With the outward normal of a sphere of radius $a$, $c = -1/a$, matching $K_{\mu\nu} = -g_{\mu\nu}/a$.

## Observations

- **The length of one degree of latitude grows from the equator to the poles** (measured, working). A degree of latitude is the distance along a meridian over which the normal to Earth's reference ellipsoid, which plumb lines follow closely, tilts by $1^\circ$. It is $\pi/180$ times the meridian's radius of curvature $M$, the inverse of a principal curvature. Eighteenth-century surveys found it longer near the poles, showing that Earth is flattened. *Numbers:* With equatorial radius $6378.137$ km and flattening $1/298.257$: $M = 6335.4$ km at the equator, so a degree is $110.574$ km; $M = 6399.6$ km at the poles, so a degree is $111.694$ km. *Reference:* Helmut Moritz (1980), *Geodetic Reference System 1980*, Bulletin Géodésique 54, 395–405, doi:10.1007/BF02521480
- **Pressure differences across curved soap films and bubbles** (measured, working). A liquid surface with tension $\gamma$ holds a pressure jump $\gamma(\kappa_1 + \kappa_2)$, higher on the side it bends toward: the Young–Laplace law. A soap film has two surfaces, doubling the jump. A film on a wire frame with equal pressure on both sides has $\kappa_1 + \kappa_2 = 0$: a minimal surface, saddle-shaped wherever it bends. *Numbers:* A bubble of radius $2$ cm with $\gamma \approx 0.025$ N/m holds $4\gamma/a \approx 5$ Pa, about one twenty-thousandth of atmospheric pressure. *Reference:* Thomas Young (1805), *An essay on the cohesion of fluids*, Philosophical Transactions of the Royal Society of London 95, 65–87, doi:10.1098/rstl.1805.0005

## Teaching arc

1. **Predict the gap, then change direction** (entry). Ask for the gap at twice the distance on a basketball, then move the card to a drinks can. *Why:* Bending becomes how quickly the surface pulls away, direction by direction. *Predict:* If the gap is two millimetres at two centimetres, how big is it at four? *Visual:* [[card-touching-a-curved-patch]] *Uses:* `ways_in/gap-under-a-card`, `ways_in/along-and-across-a-can`, `checks/double-the-distance`, `checks/card-on-a-can`
2. **Walk with a plumb line** (entry). Turn the bending into plumb-line tilt per kilometre, then scale to the Moon. *Why:* A walker can measure the same bending. *Visual:* [[plumb-lines-along-a-walk]] *Uses:* `ways_in/tilting-plumb-line`, `checks/moon-plumb-line`
3. **Build the matrix two ways** (working). Diagonalize the height over the tangent plane, then compute the form from a parametrization. *Why:* It shows where the inverse metric enters. *Predict:* If you turn the crisp by forty-five degrees, what happens to its off-diagonal term? *Uses:* `ways_in/height-over-the-touching-plane`, `ways_in/how-basis-vectors-change`, `checks/cone-principal-curvature`
4. **Roll a sheet** (working). Roll paper into a tube: the metric stays, the form changes. *Why:* It separates the form from the metric. *Predict:* Rolling keeps every length drawn on the sheet. Does it change the second fundamental form? *Visual:* [[paper-rolled-into-a-tube-and-a-cone]] *Uses:* `ways_in/bending-without-stretching`, `checks/rolled-sheet-claim`
5. **Test compatibility** (formal). Derive Gauss and Codazzi, then reject a flat metric with round bending. *Why:* These equations are the whole local story. *Uses:* `derivations/gauss-and-codazzi-from-third-derivatives`, `checks/flat-metric-round-bending`
6. **Slice spacetime** (research). Read the constraints on a spacelike slice, then bend a slice of flat spacetime. *Why:* This is where relativity uses the form. *Uses:* `ways_in/slices-of-spacetime`, `checks/curved-slice-of-flat-spacetime`

## Misconceptions

### “A curved surface bends by the same amount whichever way you go from a spot.” · entry · `same-bending-every-direction`

- **Why it is tempting:** Balls, the most familiar curved surfaces, do bend the same way in every direction.
- **What is true:** A drinks can bends across its round side but not along its length. At one point, a surface can bend by different amounts in different directions.
- **Exposed by:** `checks/card-on-a-can`

### “Right where the card touches, the surface matches the card, so it is not bending there.” · entry · `gap-zero-so-no-bending`

- **Why it is tempting:** The gap there is zero, and the ground under your feet looks level.
- **What is true:** Bending shows in how quickly the gap grows as you move away, not in the gap at the point itself.
- **Exposed by:** `checks/double-the-distance`

### “The principal curvatures are the eigenvalues of the component matrix of the second fundamental form.” · working · `eigenvalues-of-lower-k`

- **Why it is tempting:** In orthonormal tangent-plane coordinates they are, and first examples use those coordinates.
- **What is true:** They are the eigenvalues of the form with one index raised by the inverse metric. The component matrix gives them where the basis is orthonormal, but in general not elsewhere.
- **Exposed by:** `checks/cone-principal-curvature`

### “A tube is flat for anyone living on it, so its second fundamental form must be zero.” · working · `tube-has-no-bending`

- **Why it is tempting:** Tubes are the standard example of a surface that only looks curved.
- **What is true:** Rolling keeps the metric and a zero product of principal curvatures, but the normal still tilts around the tube. The second fundamental form records how the surface sits in space, which the metric does not fix.
- **Exposed by:** `checks/rolled-sheet-claim`

### “Any metric together with any symmetric tensor can be the two fundamental forms of some surface.” · formal · `any-pair-makes-a-surface`

- **Why it is tempting:** In one coordinate patch they look like independent data.
- **What is true:** They must satisfy the Gauss and Codazzi equations, and global conditions can forbid more.
- **Exposed by:** `checks/flat-metric-round-bending`, `checks/flat-torus-in-space`

### “A slice of spacetime with nonzero extrinsic curvature shows that spacetime is curved.” · research · `slice-bending-means-curved-spacetime`

- **Why it is tempting:** For surfaces in space, a nonzero second fundamental form goes with visible curving.
- **What is true:** Extrinsic curvature depends on how the slice is drawn. Flat spacetime contains slices with nonzero extrinsic curvature.
- **Exposed by:** `checks/curved-slice-of-flat-spacetime`

## Checks

1. **Entry · predict** `checks/double-the-distance`. A flat card rests on top of a round football, touching it at one point. At 2 centimetres from that point along the card, the gap under the card is 2 millimetres. About how big is the gap at 4 centimetres? Right at the touching point, where the gap is zero, is the ball bending?
   - **Hints:** What happens to the gap when the distance doubles?
   - **Answer:** About 8 millimetres. Close to the touching point, doubling the distance makes the gap about four times bigger, and four times 2 millimetres is 8 millimetres. Yes, the ball bends at the touching point too. Bending shows in how quickly the gap grows as you move away, not in the gap at the point itself.
   - **Must contain:** About 8 millimetres; Doubling the distance makes the gap about four times bigger; Bending is how quickly the gap grows
   - **Numeric:** gap at 4 centimetres = 8 mm (magnitude, ±1)
   - **Targets:** `gap-zero-so-no-bending`
   - **Visual:** [[card-touching-a-curved-patch]]
2. **Entry · predict** `checks/card-on-a-can`. A drinks can lies on its side with a flat card resting on top. The card touches the can along a line that runs the length of the can. Start at a point near the middle of that line. Is the gap under the card bigger 2 centimetres along the can's length, or 2 centimetres across the can, around its round side? Does the can bend by the same amount in every direction?
   - **Hints:** Where does the card touch the can?
   - **Answer:** Across the can. Along the can's length the card lies on the can the whole way, so the gap stays zero. Across the can the surface bends away below the card, so the gap grows. So the can bends across its round side but not along its length: at one point, a surface can bend by different amounts in different directions.
   - **Must contain:** The gap is bigger across the can; Along the length the gap stays zero; Bending can differ between directions
   - **Targets:** `same-bending-every-direction`
   - **Visual:** [[card-touching-a-curved-patch]]
3. **Entry · numeric** `checks/moon-plumb-line`. Treat the Moon as a smooth, round ball about 10,900 kilometres around its middle. An astronaut walks halfway around it along that middle circle. About how far does she walk for each degree her plumb line tilts? On Earth a degree takes about 111 kilometres. Does the Moon's surface bend more or less sharply than Earth's?
   - **Hints:** How far has the plumb line tilted when she is halfway around?
   - **Answer:** About 30 kilometres. Halfway around is about 5,450 kilometres. There she is on the opposite side of the Moon's centre. So, seen from far out in space, her plumb line hangs the opposite way to a second plumb line left hanging where she started. It has tilted 180 degrees. Every stretch of a round ball is alike, so each degree took 5,450 divided by 180, about 30 kilometres. That is fewer kilometres per degree than on Earth, so the Moon's surface bends more sharply.
   - **Must contain:** Halfway around gives 180 degrees of tilt; About 30 kilometres per degree; The Moon bends more sharply than Earth
   - **Numeric:** walking distance per degree of tilt = 30.3 km (magnitude, ±5%)
   - **Visual:** [[plumb-lines-along-a-walk]]
4. **Working · numeric** `checks/spoon-bowl-directions`. Near its lowest point, a spoon bowl has height $z = x^2/(10\ \mathrm{cm}) + y^2/(4\ \mathrm{cm})$ over its tangent plane, with $\hat{\mathbf n}$ along $+z$. Find the principal curvatures and directions, and the radius of curvature of the slice at $60^\circ$ from the $x$ axis.
   - **Hints:** Watch the factor of one half in the height formula.
   - **Answer:** Matching $z = \tfrac12K_{ij}x^ix^j$ gives $K_{ij} = \mathrm{diag}(0.2, 0.5)$ cm$^{-1}$: principal curvatures $0.2$ cm$^{-1}$ along $x$, radius $5$ cm, and $0.5$ cm$^{-1}$ along $y$, radius $2$ cm, both bending toward $\hat{\mathbf n}$. Euler's formula gives $\kappa_n = 0.2\cos^2 60^\circ + 0.5\sin^2 60^\circ = 0.425$ cm$^{-1}$, a radius of $2.35$ cm, between the principal radii.
   - **Must contain:** 0.2 and 0.5 per centimetre along x and y; Euler's formula gives 0.425 per centimetre; Radius about 2.35 centimetres
   - **Numeric:** radius of curvature at 60 degrees = 2.35 cm (magnitude, ±2%)
   - **Visual:** [[card-touching-a-curved-patch]]
5. **Working · evaluate-claim** `checks/cone-principal-curvature`. An ice-cream cone of half-angle $30^\circ$ is $\mathbf X(r,\phi) = (r\sin30^\circ\cos\phi,\ r\sin30^\circ\sin\phi,\ r\cos30^\circ)$, with $r$ the distance from the tip. At $r = 10$ cm, with the outward normal, a student finds $K_{\phi\phi} = -4.33$ cm and $K_{rr} = K_{r\phi} = 0$, and claims the principal curvatures are $-4.33$ cm and $0$. Evaluate the claim.
   - **Hints:** What units does a curvature have?
   - **Answer:** The components are right; the claim is wrong. A curvature has units of inverse length, so $-4.33$ cm signals an index still to raise. With $g_{rr} = 1$ and $g_{\phi\phi} = r^2\sin^2 30^\circ = 25$ cm$^2$, $K^\phi{}_\phi = -4.33/25 = -0.173$ cm$^{-1}$: a radius of $5.77$ cm around the cone, and $0$ along the lines through the tip. Check: the circle there has radius $5$ cm and bends at $30^\circ$ to the normal, so its normal curvature has size $\cos30^\circ/(5\ \mathrm{cm}) = 0.173$ cm$^{-1}$.
   - **Must contain:** The components have units of length; Raise the index: divide by 25 square centimetres; Principal curvatures minus 0.173 per centimetre and zero
   - **Numeric:** radius of curvature around the cone = 5.77 cm (magnitude, ±1%)
   - **Targets:** `eigenvalues-of-lower-k`
6. **Working · evaluate-claim** `checks/rolled-sheet-claim`. Claim: 'A sheet of paper rolled into a tube of radius 3 cm is still flat for anyone living on it, so its second fundamental form is zero.' Evaluate the claim.
   - **Hints:** Does the normal keep its direction as you move around the tube?
   - **Answer:** The premise is right; the conclusion is wrong. Rolling does not stretch the paper, so the metric is unchanged and an insider finds $\kappa_1\kappa_2 = 0$. But the normal tilts around the tube: with arc-length coordinates and the outward normal, $K_{uu} = -1/3$ cm$^{-1}$, a principal curvature of $-1/3$ cm$^{-1}$ around the tube and $0$ along it. The metric does not determine how a surface sits in space.
   - **Must contain:** The metric and the product are unchanged; The normal tilts, so the form is not zero; Principal curvatures minus one third per centimetre and zero
   - **Targets:** `tube-has-no-bending`
   - **Visual:** [[paper-rolled-into-a-tube-and-a-cone]]
7. **Formal · derive** `checks/why-symmetric`. Let $\Sigma$ be a hypersurface of a Riemannian manifold with Levi-Civita connection $\bar\nabla$ and unit normal $N$. For tangent fields $X, Y$, show that $\mathrm{II}(X,Y) = \bar g(\bar\nabla_XY, N)$ is a symmetric tensor and equals $-\bar g(\bar\nabla_XN, Y)$.
   - **Hints:** Expand the difference of the two orderings and use torsion-freeness.
   - **Answer:** Tensor: $\bar\nabla_XY$ is $C^\infty$-linear in $X$, and $\mathrm{II}(X, fY) = \bar g\big(X(f)\,Y + f\,\bar\nabla_XY,\ N\big) = f\,\mathrm{II}(X,Y)$ because $\bar g(Y,N) = 0$. Symmetry: torsion-freeness gives $\mathrm{II}(X,Y) - \mathrm{II}(Y,X) = \bar g([X,Y], N)$, which vanishes because the bracket of tangent fields is tangent. Weingarten: differentiating $\bar g(Y,N) = 0$ along $X$ with $\bar\nabla\bar g = 0$ gives $\bar g(\bar\nabla_XY, N) + \bar g(Y, \bar\nabla_XN) = 0$.
   - **Must contain:** Linearity in Y uses that Y is orthogonal to N; Symmetry uses torsion-freeness and a tangent bracket; The Weingarten relation uses metric compatibility
8. **Formal · evaluate-claim** `checks/flat-metric-round-bending`. On a region of the plane with $g_{\mu\nu} = \delta_{\mu\nu}$ in Cartesian coordinates, take $K_{\mu\nu} = \delta_{\mu\nu}/a$. Claim: a piece of a sphere of radius $a$ has these as its two fundamental forms. Evaluate the claim, and name the condition that fails.
   - **Hints:** Compute both sides of the Gauss equation.
   - **Answer:** False. The Codazzi equations hold, because $K_{\mu\nu}$ is constant and the Christoffel symbols vanish. The Gauss equation fails: it needs $R_{1212} = \det K_{\mu\nu} = 1/a^2$, but the flat metric has $R_{1212} = 0$. So no surface in $\mathbb R^3$ has this pair. A piece of sphere has principal curvatures of size $1/a$, but its metric is not flat.
   - **Must contain:** Codazzi holds; Gauss fails: one over a squared against zero; No surface has this pair
   - **Targets:** `any-pair-makes-a-surface`
9. **Formal · explain** `checks/flat-torus-in-space`. The flat torus is a square with opposite edges glued, with metric $dx^2 + dy^2$. Can it be a closed $C^2$ surface in $\mathbb R^3$ with this metric? Why is that consistent with rolling a flat sheet into a tube?
   - **Hints:** Look at the point farthest from the origin.
   - **Answer:** No. A closed surface in $\mathbb R^3$ is compact, so some point $p$ is farthest from the origin, at distance $\rho$. The surface lies inside the sphere of radius $\rho$ and touches it at $p$, so with the inward normal both principal curvatures at $p$ are at least $1/\rho$ and $\kappa_1\kappa_2 > 0$. The Gauss equation makes that product a function of the metric, and the flat metric makes it zero everywhere, a contradiction. A tube is not closed, and closing it into a ring would stretch it. $C^1$ isometric embeddings do exist, by the Nash–Kuiper theorem.
   - **Must contain:** A compact surface has a farthest point with positive product; The flat metric forces the product to be zero; A tube is not closed; C1 embeddings exist
   - **Targets:** `any-pair-makes-a-surface`
10. **Research · evaluate-claim** `checks/curved-slice-of-flat-spacetime`. In Minkowski spacetime with $G = c = 1$, take the slice $t^2 - x^2 - y^2 - z^2 = \tau^2$, $t > 0$. Claim: its extrinsic curvature is nonzero, so this spacetime is curved. Evaluate the claim, and check the Hamiltonian constraint on the slice.
   - **Hints:** Use $\tau^2 = -\eta_{\mu\nu}x^\mu x^\nu$ to differentiate $n_\nu = x_\nu/\tau$.
   - **Answer:** False. The future unit normal is $n^\mu = x^\mu/\tau$, and $\partial_\mu n_\nu = (\eta_{\mu\nu} + n_\mu n_\nu)/\tau = h_{\mu\nu}/\tau$, so $K_{ij} = \pm h_{ij}/\tau$ with the sign set by convention, while spacetime stays flat. The slice is hyperbolic space of radius $\tau$, with ${}^{(3)}\!R = -6/\tau^2$, and $(h^{ij}K_{ij})^2 - K_{ij}K^{ij} = 9/\tau^2 - 3/\tau^2 = 6/\tau^2$. Adding the two gives zero, matching $\rho = 0$.
   - **Must contain:** The gradient of the unit normal is h over tau; Spacetime is flat; only the slice bends; The constraint sums to zero in vacuum
   - **Targets:** `slice-bending-means-curved-spacetime`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Overall sign of the second fundamental form | $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\mathbf e_\nu$, positive where the surface bends toward the chosen normal; a sphere of radius $a$ with the outward normal has $K_{\mu\nu} = -g_{\mu\nu}/a$. | Some texts use the opposite sign, and for spacetime slices both signs are common. $\kappa_1\kappa_2$ and the Gauss equation do not depend on the choice. |
| The letter K and the mean curvature | $K_{\mu\nu}$, always with indices, is the second fundamental form; the Gaussian curvature is written $\kappa_1\kappa_2$, and the mean curvature is $\tfrac12(\kappa_1 + \kappa_2)$. | Many texts write the Gaussian curvature as a bare $K$; relativity texts use a bare $K$ for the trace $g^{\mu\nu}K_{\mu\nu}$ and often call that trace the mean curvature. Others write the form as $b_{\mu\nu}$ or $\mathrm{II}$. |

## Visuals

- ★ [[card-touching-a-curved-patch]] (flagship): The entry picture made measurable: a flat card on a curved patch, the gap in each direction, and the principal directions. *Sketch:* A 3D patch $z = \tfrac12(K_{xx}x^2 + 2K_{xy}xy + K_{yy}y^2)$ touching a translucent card, with presets for a ball, a drinks can, a spoon bowl, a saddle and a crisp turned by $45^\circ$. The learner drags a direction around the touching point; a slicing plane through the normal draws the slice and the gap at $d$ and $2d$. Readouts: normal curvature, principal curvatures and directions, product and sum; a flip-normal button reverses every sign except the product. It proves that bending belongs to a direction and that the extremes lie at right angles.
- [[plumb-lines-along-a-walk]] (core): The tilting normal as a measurement made while walking. *Sketch:* A walker crosses a ball, a flattened ellipsoid and a drinks can, planting plumb lines, while an arrow toward a distant star stays fixed. Readouts give the forward-or-back tilt per distance in the current direction, which is the normal curvature, and the sideways tilt, which is zero only along principal directions. On the can the plumb lines stay parallel along it and fan out across it; on the ellipsoid, scaled to Earth, a degree takes 110.6 to 111.7 kilometres.
- [[paper-rolled-into-a-tube-and-a-cone]] (supporting): Separates the metric from the second fundamental form. *Sketch:* A grid sheet rolls into a tube or a cone while grid lengths stay fixed. Panels show the metric, unchanged, and the second fundamental form, changing, with a product that stays zero; a patch of orange peel with positive product tears when pressed flat.

## Tutor moves

**Open with**

- Rest a flat card on top of a basketball. Two centimetres from where it touches, the gap under the card is just under two millimetres. What do you predict the gap is four centimetres out: twice as big, or more? *(prediction)*
- A drinks can lies on its side, and an ant stands on top. Should the ant walk along the can's length or across it, if it wants the can's surface not to bend away beneath its path? *(prediction)*

**If the learner is stuck**

- *The learner gets the opposite sign from a solution for the same surface.* → Fix $\hat{\mathbf n}$ first, then compare products of principal curvatures, which cannot disagree. *Uses:* `key_equations/product-and-sum`
- *The learner gets principal curvatures with units of length.* → Raise an index with $g^{\mu\nu}$ before taking eigenvalues; work the cone check. *Uses:* `checks/cone-principal-curvature`

**Common questions**

- *Why does doubling the distance make the gap under the card four times bigger, not twice as big?* (entry) Near the touching point, the ball's surface slopes away from the card more steeply the farther out you go, in step with the distance. Going twice as far out, you pass over twice the distance, and on average the surface there slopes twice as steeply. Twice the distance at twice the slope gives about four times the gap. *Uses:* `ways_in/gap-under-a-card`, `checks/double-the-distance`
- *Why is it called the second fundamental form?* (entry) Because there is a first one: the rule for measuring lengths along the surface, which someone living on it can measure. The second says how sharply the surface bends away from a flat card touching it. Lengths along the surface cannot tell you all of that. The walker with a plumb line also needs the plumb line, which points out of the surface. *Uses:* `ways_in/gap-under-a-card`, `ways_in/tilting-plumb-line`, `ways_in/bending-without-stretching`
- *Does Earth bend by the same amount in every direction?* (entry) Almost, but not exactly. Earth is slightly flattened: a little wider around the equator than from pole to pole. At the equator, 1 degree of plumb-line tilt takes about 110.6 kilometres walking toward a pole. Walking along the equator, it takes about 111.3 kilometres. So at one place the bending differs a little with direction, by less than one part in a hundred. A flattened ball is also flatter near its poles, so there a degree takes about 111.7 kilometres. *Uses:* `ways_in/tilting-plumb-line`, `observations/degree-of-latitude`

**Switching levels**

- To working when: asks how to compute the bending of a given surface. Go to the height over the touching plane and the spoon check. *Uses:* `ways_in/height-over-the-touching-plane`, `checks/spoon-bowl-directions`
- To formal when: asks why the matrix is symmetric, or whether any bending fits any metric. Give the coordinate-free formulas, then Bonnet's theorem. *Uses:* `ways_in/gauss-and-weingarten-without-coordinates`
- To research when: asks how relativity uses this. Open slices of spacetime. *Uses:* `ways_in/slices-of-spacetime`, `research_horizon/initial-data-and-the-3-plus-1-split`

**Pronunciations:** Weingarten → VINE-gar-ten; Codazzi → ko-DAHT-see; Gauss → GOWSS; Bonnet → bon-AY; Euler → OY-ler; Christoffel → kris-TOFF-el; theorema egregium → tay-oh-RAY-mah eh-GRAY-gee-um; Kuiper → KOY-per

**Voice notes:** Say "K mu nu" for components and "kappa one", "kappa two" for principal curvatures.

## History

- **Leonhard Euler (1767).** Showed that the curvatures of the slices through the normal at a point take two extreme values in perpendicular directions and interpolate between them, the relation now written $\kappa_n = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$. Leonhard Euler (1767), *Recherches sur la courbure des surfaces*, Mémoires de l'académie des sciences de Berlin 16, 119–143
- **Carl Friedrich Gauss (1827).** Built the theory of surfaces on the unit normal and the second fundamental form, and proved the theorema egregium: the product of the principal curvatures depends only on the metric. Presented in 1827, published in 1828. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146
- **Julius Weingarten (1861).** Gave the equations expressing the derivatives of the unit normal through the first and second fundamental forms, now called the Weingarten equations.
- **Pierre Ossian Bonnet (1867).** Proved that a metric and a second fundamental form satisfying the Gauss and Codazzi equations determine a surface in space, locally, up to rigid motion.

## Research horizon

- **Initial data and the 3+1 split.** In the 3+1 formulation the pair $(h_{ij}, K_{ij})$ plays the role of position and velocity, and the Gauss and Codazzi equations become the Hamiltonian and momentum constraints. Initial data for black holes and neutron stars solve these elliptic constraints, usually after a conformal decomposition. Richard Arnowitt, Stanley Deser, Charles W. Misner (1962), *The dynamics of general relativity*, Gravitation: An Introduction to Current Research, ed. L. Witten, Wiley, 227–265; reprinted in General Relativity and Gravitation 40, 1997–2027 (2008), doi:10.1007/s10714-008-0661-1; Gregory B. Cook (2000), *Initial data for numerical relativity*, Living Reviews in Relativity 3, 5, doi:10.12942/lrr-2000-5
- **Trapped surfaces and dynamical horizons.** A closed spacelike two-surface has two future null normals; the traces of its second fundamental forms along them give, up to a conventional sign, the expansions of its light rays. Penrose used surfaces where both are negative, and horizon frameworks and finders track marginally trapped surfaces. Roger Penrose (1965), *Gravitational collapse and space-time singularities*, Physical Review Letters 14, 57–59, doi:10.1103/PhysRevLett.14.57; Abhay Ashtekar, Badri Krishnan (2004), *Isolated and dynamical horizons and their applications*, Living Reviews in Relativity 7, 10, doi:10.12942/lrr-2004-10
- **Boundary terms and quasi-local energy.** The gravitational action needs a boundary integral of the trace of the boundary's extrinsic curvature to have a well-posed variational principle. The trace of a closed two-surface's extrinsic curvature within a slice, compared with a flat-space embedding of the same two-surface, gives the Brown–York quasi-local energy. James W. York (1972), *Role of conformal three-geometry in the dynamics of gravitation*, Physical Review Letters 28, 1082–1085, doi:10.1103/PhysRevLett.28.1082; Gary W. Gibbons, Stephen W. Hawking (1977), *Action integrals and partition functions in quantum gravity*, Physical Review D 15, 2752–2756, doi:10.1103/PhysRevD.15.2752; J. David Brown, James W. York (1993), *Quasilocal energy and conserved charges derived from the gravitational action*, Physical Review D 47, 1407–1419, doi:10.1103/PhysRevD.47.1407
- **Thin shells and junction conditions.** When matter is concentrated on a hypersurface, the induced metric stays continuous while the extrinsic curvature jumps. Israel related the jump to the surface stress-energy, which underlies models of collapsing dust shells and domain walls. Werner Israel (1966), *Singular hypersurfaces and thin shells in general relativity*, Il Nuovo Cimento B 44, 1–14, doi:10.1007/BF02710419

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** If you put a flat card on top of a basketball, the gap under it gets bigger as you go out from where it touches: just under 2 millimetres at 2 centimetres, about 7 at 4, so doubling the distance makes it about four times bigger, though I don't see why four and not two. How fast the gap grows is how much the ball bends. On a can lying down, the card touches along a line, so no gap along it but a gap across it, which I think means around the side, so the bending depends on direction. The name for all that is the second fundamental form. Then a plumb line: it points at Earth's centre, and if you walk halfway round Earth it's upside down compared with a star, so 1 degree for every 111 kilometres. I don't get how you check the same star from the other side of Earth, or why tilting is the same thing as the card gap. You don't notice because it's less than a hundredth of a degree per kilometre.

**Stumbles (28)**

- “the ball curves away beneath it”: Two words for one idea: the ways say 'bends', the summary and the can check say 'curves'.
- “Close to the touching point, doubling the distance makes the gap about four times bigger. [summary]”: A surprising claim with no numbers or reason within two sentences, in a summary of five sentences where the guide asks for two or three.
- “in every direction at a spot”: Two words for one idea: 'spot' in the summary, glossary and recap, 'touching point' and 'point' in the ways.
- “At 2 centimetres along the card, the gap between card and ball is just under 2 millimetres.”: A measurement without its reference: 2 centimetres from where, and the gap measured in which direction?
- “Close to the touching point, doubling the distance makes the gap about four times bigger. [gap way]”: The first question a teenager asks is why four and not two; the numbers back it but no reason is given.
- “How quickly the gap grows shows how sharply the surface bends.”: A step taken on trust: nothing compares two surfaces, so the reader cannot see that faster growth goes with sharper bending, and the first what-if, a smaller ball, is not answered.
- “How quickly the gap under a flat card grows shows how sharply a surface bends, and on a drinks can the answer differs between along and across.”: Rule 17: the way asks the reader to hold two new ideas, that the gap measures bending and that bending differs between directions. Its question and takeaway both have two halves.
- “The card touches the can along a line down its length.”: 'Down' reads as a direction on a can lying on its side.
- “but across the can the gap grows”: 'Across' could mean across the top or around the side; the reader cannot tell which way to move.
- “Lay a sheet of paper on top of a ball: it touches the ball only near one spot.”: Not doable as written: a sheet of paper sags around a ball and touches over a wide patch, so the reader does not see what is promised.
- “On a saddle, the surface drops below the card in some directions and rises above it in others”: A card cannot rest on the middle of a saddle if the surface rises above it; the picture is not physically possible as set up.
- “A line at right angles to a ball's surface points at the ball's centre.”: A surprise with no reason, and a plumb line's string points up at its top, so 'points at the centre' needs a direction.
- “So your plumb line has tilted by half a turn, 180 degrees, measured against a far-off star.”: A rule the reader cannot follow: a star overhead at the start is beneath your feet at the finish, and stars move across the sky as Earth spins.
- “Each degree took about 111 kilometres, which is 20,000 divided by 180.”: A missing step: dividing assumes every stretch of the trip gives the same tilt.
- “Walk halfway around Earth along the equator”: Not doable: most of the equator is ocean.
- “A more sharply bent surface tilts the plumb line faster.”: 'Faster' is a time word for a rate per kilometre, and the link between plumb-line tilt and the bending the card shows is taken on trust.
- “How fast a plumb line tilts as you walk measures how sharply the ground bends in that direction”: 'How fast' is a time word, and 'ground' is a second word for 'surface'.
- “Treat the calm sea as the surface of a smooth, round ball.”: 'Calm sea' and 'calm water' in consecutive paragraphs, and the walker then walks on the sea.
- “A flat card rests on top of a football”: 'Football' is ambiguous: an American football is not round.
- “From a point on that line, is the gap under the card bigger 2 centimetres along the can's length”: Ambiguous starting state: from a point near the can's end, 2 centimetres along the length leaves the can.
- “So the can bends across itself but not along its length”: 'Bends across itself' reads as folding over.
- “An astronaut walks halfway around it along that middle circle, checking her plumb line against a far-off star.”: The same undoable star rule as the plumb-line way.
- “It tilts faster than a plumb line on Earth, so the Moon's surface bends more sharply.”: 'Faster' is a time word, and the step from fewer kilometres per degree to sharper bending is not named.
- “so the extra gap is 1,410 metres times 155 metres divided by 6,371,000 metres”: A missing step: the reader is not told why the gap grows in step with distance from the tip, or where the product comes from.
- “Which way could the ant walk so that the can does not bend away beneath it?”: 'It' could be the ant or the can, and 'bend away' has no card to bend away from.
- “In full, it can be found only from the space around the surface.”: Contradicts the plumb-line way, where a walker on Earth measures the bending; 'in full' is unclear.
- “Almost, because Earth is slightly flattened. Walking from the equator toward a pole, 1 degree of plumb-line tilt takes about 110.6 kilometres at the equator and about 111.7 kilometres near the poles.”: 'Almost' answers the wrong half of the question, the numbers compare places rather than directions, and nothing says why a flattened ball gives longer degrees near the poles.
- “for a plumb line to tilt by a given angle on a round world”: 'Round world' is a third name for the smooth, round ball of the ways.

**Fixes**

- Split the entry way 'The gap under a flat card' (rule 17). It now answers one question with the basketball and tennis-ball gaps. The new entry way 'Along a can and across it' (contrast, id along-and-across-a-can) takes the can, the direction idea, the name of the form, a ruler try-it and the saddle warning. The entry objective read-bending-from-a-card was split to match; compare-bending-by-direction is evidenced by checks/card-on-a-can.
- The schema allows at most 8 ways, so the formal way which-pairs-make-a-surface was folded, unreworded, into the formal way it continued. That way is now titled 'Gauss, Weingarten and Bonnet without coordinates'. The Bonnet text sits before 'Limits of validity', and its opening sentence no longer names the way it now belongs to. That way's question, takeaway (shortened to the 240-character limit), continues (adds bending-without-stretching) and refs (adds the two Bonnet checks) were updated. 'Slices of spacetime' now continues only this way and names the new title, and the formal level switch dropped the removed address. The id was never published, so it is not in retired_ids.
- Plumb-line way: added the spokes reason for 'points at the centre' and the equal-stretches step. The tilt is now seen from far out in space, not against a star. A comparison with a smaller ball ties plumb-line tilt to the bending the card shows. The takeaway uses 'surface' and 'per kilometre'. The question now asks how a carried plumb line shows the bending. A doable pole-star measurement moved to simplifies: 111 kilometres toward the pole star changes the angle by about 1 degree, compared at the same hour by the walker's watch.
- Rewrote the entry checks, the bridge-towers solution, the ant opening question, both existing entry common questions, the can misconception correction, the glossary entries and the objective as the stumbles record. Added the glossary term 'pole star'.
- New entry numbers, checked in python3: a tennis ball of radius 3.35 centimetres has a 6.6-millimetre gap at 2 centimetres (about 7). A basketball of radius 11.9 centimetres has gaps of 1.69, 6.92 and 30.9 millimetres at 2, 4 and 8 centimetres, so the 8-centimetre gap is 4.46 times the 4-centimetre gap. The average slope doubles (ratio 2.05) when the distance doubles, which backs the why-four answer. A degree of latitude is 110.57 kilometres at the equator; an east-west degree there is 111.32 kilometres, and 111.69 near the poles.
- Ladder: 'The height over the touching plane' now continues both entry card ways. Its first sentence names both, replacing 'Here is why', since the entry reason now lives in a common question. The other non-entry ways already open by naming the ways they continue.
- Budget (entry-way explanations may reach 440 words): the why-four paragraph moved to the new entry common question why-four-times. The pole-star measurement and the slanting-direction sentence moved to simplifies, and 'measure at right angles to the card' also moved to simplifies. Dropped from the ways, with no sentence compressed: 'On a flat table, the gap stays zero.', 'A round ball is the special case where every direction bends by the same amount.', 'On a round ball, the tilt per kilometre is the same in every direction.' (the Earth common question covers direction on a round world), 'so it shows which way is up there', and 'Start at a point near the middle of that line.', which the can check keeps.
- Summary: four short sentences, so the sentence average meets the validator. The five-sentence draft had a surprise with no reason.
- Bumped the revision to 2.

**Concerns**

- Carried from the writer: the conventions file has no rows for the sign of the second fundamental form and extrinsic curvature, for the letter K (form versus Gaussian curvature), or for mean curvature as half the trace. The notation traps' course_choice fields name choices the conventions file does not yet make.
- The physics reviewer should check the new entry claims: the tennis-ball gap, the slope reason in why-four-times, 'more slowly than directly across' on a can in a slanting direction, and the pole-star measurement (Polaris sits about 0.7 degrees from the celestial pole; comparing at the same watch hour on nearby nights keeps the error well below the 1-degree change).
- The formal ways were merged only to satisfy the 8-way schema limit. The merged explanation runs about 590 words; the physics reviewer should confirm it reads in order.
- Budgets: entry-way explanations are at the 440-word review ceiling and other way fields are near 880. Further entry additions need cuts. The summary has four sentences where the guide asks for two or three; three sentences failed the validator's 20-word average without compressing.
- The notes for this concept's entry-rung prerequisites (parametrized-surface, induced-metric, christoffel-symbols, eigenvalues-and-eigenvectors, intrinsic-versus-extrinsic-curvature) do not exist yet, so glossaries could not be aligned. The sibling curvature-of-a-curve defines 'curvature' as turn per metre, but this note's entry rung avoids that word.
- The proposed visual card-touching-a-curved-patch now serves both entry card ways; its future tour should have separate beats for gap growth and for direction. Its sketch should show the can's slanting direction too.
- Run sync_registry.py once reviews are done, since the prerequisites and the leads_to placement of extrinsic-curvature-of-a-hypersurface differ from the registry.

**Re-read** (2026-09-13, revision 4): 5 stumbles in 9 changed passages

- “your plumb line now hangs the opposite way to a plumb line left hanging at your start”: 'At your start' can mean a moment or a place; the fix exists to rule out the moment, and a beginner also wonders which plumb line is meant, since there was only one.
- “her plumb line hangs the opposite way to a plumb line left hanging at her start. So it has tilted 180 degrees.”: Same time-or-place ambiguity as in the way; and two sentences in a row now begin with 'So', which reads as a stammer.
- “Walk slantwise, and the plumb line also tilts sideways, so it tilts more per kilometre than the can bends in that direction.”: A real plumb line on a drinks can hangs toward the ground, not at right angles to the can, so the reader cannot picture it tilting with the can; 'per kilometre' makes no sense on a can; and 'sideways' has no reference.
- “its sideways part vanishes only along principal directions. Its extremes over directions with $g_{\mu\nu}t^\mu t^\nu = 1$”: 'Its' now follows a sentence about the normal's tilt rate, so it no longer points unmistakably at the normal curvature; 'sideways' is loose for the tangential component perpendicular to t.
- “In general, the component matrix gives them only where the basis is orthonormal.”: 'In general' followed by 'only where' reads as a contradiction: is the orthonormal condition general or not?
- Fix: Replaced 'a plumb line left hanging at your/her start' with 'a second plumb line left hanging where you/she started' in the tilting-plumb-line explanation and the Moon check answer, and dropped the repeated 'So' in the Moon answer.
- Fix: Rewrote the can sentences in tilting-plumb-line.simplifies with a pin at right angles to the surface in place of a plumb line, per centimetre instead of per kilometre, and a path-relative 'to one side of your path'. The claims (matches along and across; tilts more than the bending on a slant) are unchanged.
- Fix: Budget: other way fields sat at 869 of 880, so to make room dropped the lowest-value sentence 'Hills and dense rock nudge plumb lines very slightly too.' from tilting-plumb-line.simplifies; the explanation already scopes Earth as a smooth, round ball.
- Fix: Working rung: named the referent ('The extremes of kappa_n') after the new Weingarten sentence, replaced 'sideways part' with 'part perpendicular to t', and reordered the eigenvalues-of-lower-k correction so 'in general' no longer clashes with 'only'.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 4)

**Verification**

- Entry gaps: basketball just under 2 mm at 2 cm, about 7 mm at 4 cm, about 4.5 times that at 8 cm; tennis ball about 7 mm at 2 cm; working value d^2/(2a) = 0.17 cm.: python3, exact gap a - sqrt(a^2 - d^2) measured at right angles to the card: a = 12 cm gives 1.68, 6.86, 30.6 mm (ratio 4.45); a = 11.9 cm gives 1.69, 6.92, 30.9 mm (4.46); a = 3.35 cm gives 6.63 mm; 4/24 = 0.167 cm. → Correct.
- Check double-the-distance: 2 mm at 2 cm gives about 8 mm at 4 cm.: Quadratic rule gives 8 mm; exact circle through 2.0 mm at 2 cm (a = 10 cm) gives 8.35 mm; a size-5 football (a = 11 cm) gives 1.83 and 7.53 mm. → Within abs_tol 1 mm. Correct.
- Common question why-four-times: twice the distance at twice the average slope gives four times the gap.: Slope of the circle near the touching point is x/a; gap = integral of slope = d times the average slope d/(2a). → Correct.
- Can: gap zero along the length, grows across; slanting direction grows more slowly; saddle drops below the card in some directions and rises above it in others.: Cylinder height z = (s sin phi)^2/(2a): slanting direction equals the across gap at s sin phi < s. Saddle z = (x^2 - y^2)/(2a) changes sign with direction. → Correct.
- Plumb-line way: halfway around Earth is about 20,000 km and 180 degrees; 111 km per degree; under one hundredth of a degree per km.: python3: 40,075/2/180 = 111.3 km; 20,000/180 = 111.1; 6371 pi/180 = 111.19 km; 1/111 = 0.009 degree. → Correct. Comparison 'the opposite way to how it hung at your start' seen from space is time-dependent because Earth spins during the walk; fixed to compare with a plumb line left hanging at the start.
- Plumb-line takeaway: tilt per kilometre measures how sharply the surface bends in the direction you walk.: Weingarten: dn/ds = -S(t). Its magnitude |S t| equals the normal curvature K(t,t) only along principal directions. Cylinder at 30 degrees from its axis: tilt rate sin(30)/a = 0.5/a, normal curvature sin^2(30)/a = 0.25/a. → False for slanting directions on a can, which the ladder's can way invites. Rescoped to a round ball in the explanation and takeaway, with the can case in simplifies.
- Simplifies: flattened Earth gives 110.6 to 111.7 km per degree, depending on place and direction.: GRS80 a = 6378.137 km, f = 1/298.257222101: meridian radius M from 6335.44 km (equator) to 6399.59 km (pole), prime-vertical N from 6378.14 to 6399.59 km; every normal-curvature radius lies between M and N. Degrees: 110.574, 111.694, and 111.319 km east-west at the equator. → Correct; also matches the Earth common question (110.6, 111.3, 111.7 km, differing by under one percent) and observations/degree-of-latitude.
- Pole-star measurement: walk 111 km toward the pole star and the plumb-line angle changes by about 1 degree; measure at the same watch hour.: The zenith distance of the celestial pole is 90 degrees minus astronomical latitude. Polaris sits about 0.64 degrees from the pole in 2026, so its altitude swings by up to that much with hour angle. Walking due north keeps longitude, so the same watch hour gives nearly the same hour angle; the sidereal drift of about 1 degree of hour angle per day moves the altitude by about 0.01 degree. → Correct.
- Moon check: 10,900 km around, 30.3 km per degree.: python3: 2 pi 1737.4 = 10,916 km; 5,450/180 = 30.28 km. → Correct; rel_tol 0.05 fine.
- Bridge towers: 1,410 m apart, 155 m tall, 6,371 km radius give 3.4 cm.: python3: 1410 x 155/6,371,000 = 0.0343 m. Similar triangles argument checked. → Correct.
- Height over the tangent plane, normal curvature as slice curvature, Euler's formula, sphere, can and saddle values, sign flip with the normal.: Taylor expansion with z'(0) = 0 gives slice curvature z''(0) = K(t,t); diagonalization; saddle kappa_n = (cos^2 - sin^2)/a = cos 2phi/a; outward normal on sphere n = X/a gives negative values. → Correct. Added that at an umbilic every direction is principal, so 'their directions are perpendicular' is not misread.
- Gauss formula, K = n . d^2X, Weingarten dn = -K^lambda_mu e_lambda, sphere K^lambda_mu = -delta/a, product det K/det g and sum g^{mu nu} K_{mu nu}.: Re-derived each step of weingarten-from-orthogonality and normal-curvature-along-a-curve by hand; det(g^-1 K) = det K/det g. → Correct. 'equal those of the component matrix only where g = delta' overstated (a zero form agrees in any basis); rescoped to 'in general differ ... unless'. Added the plumb-line link: the component of dn/ds along t is -kappa_n.
- Gauss and Codazzi in the course Riemann convention, including the epsilon factor for indefinite ambient metrics.: Expanded barR(e_mu,e_nu)e_sigma = [barnabla_mu, barnabla_nu] e_sigma with Gauss and Weingarten, matched R(e_mu,e_nu)e_sigma = R^rho_{sigma mu nu} e_rho, took tangential and normal parts; sphere check R_{theta phi theta phi} = a^2 sin^2 theta. For epsilon = -1, contracted twice with h = g + nn to get 3R + K^2 - K_ij K^ij = 2 G_nn = 16 pi rho. → Correct, signs and index order agree with the conventions file.
- Formal way: tensoriality, symmetry, self-adjoint shape operator; Bonnet's theorem with integrability condition dA - dA + [A,A] = 0 for dF = F A; farthest-point argument; Nash-Kuiper.: Differentiated F A_nu and antisymmetrized; checked that closedness of e_mu dx^mu follows from symmetric Gamma and K; rotation freedom of oriented frames with fixed Gram matrix. → Correct and in logical order after the merge: formulas, properties, Gauss-Codazzi, Bonnet, global statements, limits. 'has no such formula' for the mean curvature replaced by the tube counterexample that backs it; whole-sphere rigidity attributed to Liebmann's theorem.
- Worked example crisp z = xy/a with a = 4 cm.: Eigenvalues of [[0,1/a],[1/a,0]], rotation by 45 degrees gives (xi^2 - eta^2)/(2a). → Correct: +-0.25 cm^-1, product -0.0625 cm^-2, mean 0.
- Check spoon-bowl-directions.: python3: K = diag(0.2, 0.5) cm^-1; 0.2 cos^2 60 + 0.5 sin^2 60 = 0.425; radius 2.353 cm. → Correct.
- Check cone-principal-curvature.: Computed e_r, e_phi, outward normal (cos30 cos phi, cos30 sin phi, -sin30), K_phiphi = -r sin30 cos30 = -4.330 cm, g_phiphi = 25 cm^2, K^phi_phi = -0.1732 cm^-1, radius 5.774 cm; Meusnier check cos30/5 = 0.1732. → Correct. (e_r x e_phi is the inward normal here; the check names the outward normal explicitly.)
- Check rolled-sheet-claim and the tube in bending-without-stretching.: X = (a cos(u/a), a sin(u/a), v): K_uu = -1/a with n = e_u x e_v outward, g = delta, mean -1/(2a). → Correct.
- Problem inner-tube-torus.: Computed e_u, e_v, e_u x e_v = (cos u cos v, sin u cos v, sin v), second derivatives; python3: 1/(0.025 x 0.325) = 123.08 m^-2, -1/(0.025 x 0.275) = -145.45 m^-2, kappa_u(pi) = 3.636 m^-1. → Correct; numeric fields and tolerances agree.
- Problem all-umbilic-surfaces and formal checks why-symmetric, flat-metric-round-bending, flat-torus-in-space.: Worked each proof. → Correct.
- Research way and check curved-slice-of-flat-spacetime: Hamiltonian constraint, K_ij = +-(1/2) L_n h_ij, hyperboloid slice.: n^mu = x^mu/tau, d_mu n_nu = h_mu nu/tau; 3R = -6/tau^2, K^2 = 9/tau^2, K_ij K^ij = 3/tau^2, sum 0. → Correct. Brown-York energy uses the trace of the two-surface's extrinsic curvature within the slice, not the trace of the timelike boundary's; the research way and horizon connection now say so.
- Observation soap-film-pressure: 4 gamma/a = 5 Pa for a = 2 cm, gamma = 0.025 N/m; one twenty-thousandth of an atmosphere.: python3: 0.1/0.02 = 5 Pa; 101325/5 = 20,265. Pressure is higher on the concave side, the side the surface bends toward. → Correct.
- Reference Moritz 1980, Geodetic Reference System 1980, Bulletin Géodésique 54, 395-405.: Web search: ADS 1980BGeod..54..395M and Springer record. → Confirmed; added doi 10.1007/BF02521480.
- Reference Young 1805, An essay on the cohesion of fluids, Phil. Trans. 95, 65-87.: Web search: Royal Society and ADS records. → Confirmed; added doi 10.1098/rstl.1805.0005.
- History Euler 1767 (E333, Mémoires Berlin 16, 119-143) and Gauss 1828 (Commentationes Gottingensis Recentiores 6, 99-146, presented 8 October 1827).: Web search: Euler Archive E333; archive and bibliographic records of the Disquisitiones. → Confirmed. Weingarten 1861 and Bonnet 1867 carry no reference; Bonnet's contribution scoped to 'locally'.
- Research references ADM 1962/2008 (doi 10.1007/s10714-008-0661-1, gr-qc/0405109), Cook 2000 (LRR 3, 5), Penrose 1965 (PRL 14, 57), Ashtekar-Krishnan 2004 (LRR 7, 10, gr-qc/0407042), York 1972 (PRL 28, 1082), Gibbons-Hawking 1977 (PRD 15, 2752), Brown-York 1993 (PRD 47, 1407, gr-qc/9209012), Israel 1966 (Nuovo Cimento B 44, 1-14, doi 10.1007/BF02710419).: Web search of arXiv, APS, Springer, ADS and Living Reviews records. → All confirmed; set verified true.
- Structure: prerequisites and assumes.: Registry prerequisites of each listed prerequisite; reachability search for a cycle; levi-civita-connection and lie-bracket are prerequisites of riemann-curvature-tensor. → Acyclic; assumes consistent. Formal rung has three checks and one problem; four research topics with two reviews.

**Counterexamples tried**

- Slanting walk on a can: breaks 'tilt per kilometre measures how sharply the surface bends in the direction you walk' (tilt rate sin phi/a against normal curvature sin^2 phi/a). Rescoped to a round ball; can case added to simplifies.
- Earth's spin during the walk: 'hangs the opposite way to how it hung at your start', seen from space, compares directions at different times. Now compares with a plumb line left at the start.
- Umbilic point (sphere): principal directions are not unique; the working sentence now says every direction is principal there.
- Zero second fundamental form in a non-orthonormal basis: component and raised eigenvalues agree although g is not delta, so 'only where' was too strong; rescoped.
- Flat sheet versus rolled tube: same metric, different mean curvature; backs the formal statement that the sum is not fixed by g.
- Cone tip and crease: second fundamental form undefined; stated in simplifies and limits of validity.
- Flat torus: no C^2 isometric embedding (farthest-point argument), C^1 embeddings exist; stated correctly.
- Whole round sphere versus a spherical cap: the cap bends, the whole sphere is rigid among C^2 surfaces (Liebmann); now attributed.
- Hyperbolic slice of Minkowski spacetime: nonzero K_ij in flat spacetime; the constraint sums to zero, as the research check says.
- Saddle and card: the card cannot rest on a saddle's middle; the entry text says 'hold a card against', which is correct.
- Region near the ellipsoid's poles and equator: degree lengths 110.57 to 111.69 km cover every direction, since every normal curvature lies between the principal ones.

**Fixes**

- tilting-plumb-line explanation and moon-plumb-line answer: the half-turn is now compared with 'a plumb line left hanging at your start' (Earth and the Moon spin during the walk). The Moon answer sentence was split in two to stay under 32 words.
- tilting-plumb-line explanation and takeaway: rescoped the tilt-per-kilometre claim to a round ball; simplifies gains two sentences on walking along, across and slantwise on a can.
- how-basis-vectors-change: 'equal ... only where g = delta' became 'in general differ ... unless g = delta there'; added one sentence tying Weingarten's equation to the plumb line (component along t is -kappa_n, sideways part zero only along principal directions). Misconception eigenvalues-of-lower-k correction scoped with 'In general'.
- height-over-the-touching-plane: added that every direction is principal where kappa_1 = kappa_2.
- bending-without-stretching: 'kappa_1 != 0' became 'one principal curvature is nonzero' (the ordering kappa_1 >= kappa_2 may put the zero first); orange peel no longer reuses the can's radius a, and 'without tearing or stretching' became 'without stretching'.
- Formal way: mean-curvature nonexistence claim replaced by the tube counterexample; sphere rigidity attributed to Liebmann's theorem.
- Research way and research_horizon boundary-terms: the Brown-York energy uses the trace of a closed two-surface's extrinsic curvature within a slice.
- History bonnet-1867: scoped to 'locally'. Visual sketch plumb-lines-along-a-walk: separate forward-or-back and sideways tilt readouts.
- All references verified; DOIs added for Moritz 1980 and Young 1805. Revision bumped to 3.

**Concerns**

- Carried: course-conventions.md has no rows for the sign of the second fundamental form or extrinsic curvature, for the letter K (form versus Gaussian curvature versus the trace), or for mean curvature as half the trace. The note's choice (K_mu nu = n . d_mu e_nu, positive toward the chosen normal; outward sphere -g/a) is internally consistent, but the notation traps' course_choice fields name choices the conventions file does not yet make. The research way leaves the sign of K_ij unfixed for that reason.
- The merged formal way (about 600 words) reads in order and is correct; its question has three parts, acceptable at the formal rung.
- Budgets after these fixes: other way fields 869 of the 880 review ceiling; entry explanations 437 of 440. Further entry additions need cuts.
- The novice re-read should cover the eight changed strings note_diff.py lists, especially the new can sentences in tilting-plumb-line simplifies ('slantwise').
- The visual sketch plumb-lines-along-a-walk still shows 'an arrow toward a distant star' as a fixed reference; as an outside view it is fine, but its narration should avoid implying the walker sights that star.
- Run sync_registry.py: prerequisites and the leads_to placement of extrinsic-curvature-of-a-hypersurface differ from the registry.

**Diff check** (2026-09-13, revision 4)

- tilting-plumb-line.explanation and checks/moon-plumb-line: seen from space, the plumb line halfway around hangs the opposite way to a second plumb line left hanging where the walker started.: The comparison is now between two places at one instant, so Earth's or the Moon's spin during the walk no longer matters. On a round ball the normals at points half a great circle apart are antiparallel. Moon: 5,450/180 = 30.28 km per degree (10,921/2/180 = 30.34), within rel_tol 0.05 of 30.3. → Correct. It claims the same as before and is more precise. Removing 'So' from 'It has tilted 180 degrees' changes no claim.
- tilting-plumb-line.simplifies: on a drinks can, a pin at right angles to the surface tilts per centimetre as much as the can bends along the can or directly across it; on a slant it also leans to one side of the path, so it tilts more than the can bends that way.: The pin is the unit normal, and its rate is dn/ds = -S t by Weingarten. On a cylinder of radius a (python3, a = 3.3 cm), path at angle phi from the axis: tilt rate sin(phi)/a, normal curvature sin^2(phi)/a, sideways component sin(phi)cos(phi)/a. phi = 0: 0, 0, 0. phi = 90: 0.303, 0.303, 0. phi = 30: 0.152, 0.076, 0.131. phi = 45: 0.214, 0.152, 0.152. phi = 60: 0.262, 0.227, 0.131 per cm. → Correct. Tilt equals bending along and across. For 0 < phi < 90 the sideways part is nonzero and the tilt exceeds the bending. A pin at right angles to the surface is a truer picture than a plumb line on a can, and the claim matches the rescoping from the physics review at revision 3. Dropping the hills-and-rock sentence removes a true side remark and makes no claim false, because the explanation already treats Earth as a smooth, round ball.
- how-basis-vectors-change: the part of dn/ds perpendicular to t vanishes only along principal directions; the extremes of kappa_n over unit directions are the eigenvalues of K^mu_nu.: dn/ds = -S t is tangent to the surface, and it has no part perpendicular to t exactly when S t is parallel to t, that is when t is an eigenvector of S, a principal direction. This includes S t = 0 along a cylinder's axis, and every direction at an umbilic. Lagrange condition K_{mu nu} t^nu = lambda g_{mu nu} t^nu gives the eigenvalues of K^mu_nu. Example g = diag(4,1), K_{mu nu} = diag(1,1): sampled kappa_n over g-unit directions runs from 0.25 to 1.00, which are the eigenvalues of K^mu_nu, while K_{mu nu} has eigenvalues 1 and 1. → Correct. 'part perpendicular to t' and 'The extremes of kappa_n' claim exactly what 'sideways part' and 'Its extremes' did.
- misconceptions/eigenvalues-of-lower-k.correction: the component matrix gives the principal curvatures where the basis is orthonormal, but in general not elsewhere.: Where g = delta, K^mu_nu = K_{mu nu}. Elsewhere, the example g = diag(4,1) above gives different eigenvalues. The hedge 'in general' covers accidental coincidences, such as K proportional to g. → Correct. The claim is the same as before the reorder.
