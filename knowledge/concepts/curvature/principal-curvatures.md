---
type: "concept"
schema_version: 2
id: "principal-curvatures"
title: "Principal curvatures"
tagline: "The largest and smallest bending of a surface at a point, and their directions"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["principal curvature"]
prerequisites: ["normal-curvature", "eigenvalues-and-eigenvectors"]
leads_to: ["sectional-curvature", "extrinsic-curvature-of-a-hypersurface", "kasner-solution", "apparent-horizon", "quasi-local-mass"]
visuals: ["card-touching-a-curved-patch", "plumb-lines-along-a-walk", "lines-of-curvature-on-an-ellipsoid"]
---

# Principal curvatures

*The largest and smallest bending of a surface at a point, and their directions*

`principal-curvatures` · curvature · advanced · physics-reviewed (revision 8)

**Needs:** [[normal-curvature]] (entry) · [[eigenvalues-and-eigenvectors]] (working)  
**Opens:** [[sectional-curvature]] · [[extrinsic-curvature-of-a-hypersurface]] · [[kasner-solution]] · [[apparent-horizon]] · [[quasi-local-mass]]  
**Related:** [[second-fundamental-form]] · [[gaussian-curvature]] · [[theorema-egregium]] · [[photon-sphere]]  
**Visuals:** ★ [[card-touching-a-curved-patch]] · [[plumb-lines-along-a-walk]] · [[lines-of-curvature-on-an-ellipsoid]]

> At one point of a smooth surface, the bending often depends on direction. An egg's shell at its widest circle, for example, bends more sharply around the egg than along it. Count bending toward one side of the surface as positive and toward the other side as negative. The largest and smallest values at a point are then its principal curvatures. Unless every direction bends alike there, as on a ball, their directions are a quarter turn apart.

## You will be able to

**Entry**
- Predict the direction of gentlest bending at a point of a surface like an egg's shell, given the direction of sharpest bending. `objectives/predict-the-gentlest-direction` ← `checks/helmet-top`
- Explain how a saddle-shaped point has one positive and one negative principal curvature. `objectives/explain-opposite-signs` ← `checks/mountain-pass`

**Working**
- Compute principal curvatures and directions by raising an index of the second fundamental form. `objectives/compute-from-the-shape-operator` ← `checks/helical-lines-on-a-can`, `problems/satellite-dish`
- Distinguish a surface with zero mean curvature from a flat one. `objectives/distinguish-zero-mean-from-flat` ← `checks/soap-film-flat-claim`

**Formal**
- Analyse principal curvatures near an umbilic, and use the index sum to decide whether a closed surface must have umbilics. `objectives/analyse-umbilics` ← `problems/star-umbilic`, `checks/no-umbilic-free-egg`
- State when the principal curvatures of a hypersurface are real, and give a timelike counterexample. `objectives/state-when-principal-curvatures-are-real` ← `checks/timelike-surface-claim`

**Research**
- Compute the Hawking mass of round spheres from their principal curvatures. `objectives/compute-hawking-mass` ← `checks/hawking-mass-of-schwarzschild-spheres`
- Derive the constraint on the Kasner exponents from the principal curvatures of the slices. `objectives/constrain-kasner-exponents` ← `problems/kasner-exponents`

## Ways in

### 1. Turn a ruler on an egg · entry · picture

*At one point on an egg's shell, in which directions does the shell bend most and least sharply?*

Hold a hen's egg still on its side on a folded towel. Lay a ruler on top, touching the shell at one point on the widest circle around the egg. Keep that point still and turn the ruler slowly around it.

Under the ruler there is a gap, which grows as you look further from the touching point. The more quickly the gap grows, the more sharply the shell bends in the direction the ruler points. That is why, at the same distance from the touching point, a tennis ball leaves a bigger gap under a ruler than a basketball does.

On a typical egg, look at the gap 2 centimetres along the ruler from the touching point. It is biggest, about 1 and a quarter centimetres, when the ruler lies around the egg. It is smallest, about 6 millimetres, when the ruler lies along the egg, from end to end. So the shell bends most sharply around the egg and least sharply along it. Around and along are a quarter turn apart.

The shell stays on one side of the ruler, whichever way the ruler points. On a surface like that, the sharpest and the gentlest bending at a point are called the principal curvatures.

At every point of such a smooth surface, their directions are a quarter turn apart, unless all directions bend alike, as on a ball. You can test this on a tin can.

**Try it:** Hold a tin can still on its side on a folded towel. Lay a ruler on top, touching the can at one point, and turn the ruler slowly around that point. Watch the light under the ruler. The gap grows most quickly when the ruler lies around the can. When the ruler lies along the can, a quarter turn away, the gap does not grow at all, because the can does not bend in that direction.

**Takeaway:** On a surface like an egg's shell, the sharpest and gentlest bending at a point are its principal curvatures. Unless every direction bends alike, their directions are a quarter turn apart.

*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `checks/helmet-top`

### 2. A saddle bends both ways · entry · contrast

*Can a surface bend toward one side in one direction and toward the other side in another?*

**Recap:** A ruler touches a surface at one point. The more quickly the gap under the ruler grows away from that point, the more sharply the surface bends in the ruler's direction. An egg's shell stays on one side of the ruler, whichever way it points. On a surface like that, the sharpest and gentlest bending at a point are called the principal curvatures. Their directions are a quarter turn apart, unless every direction bends alike.

Look at the middle of a horse's saddle. Along the horse's back, the seat rises toward the front and toward the back. Across the horse, the seat drops away over the horse's sides.

Where a surface is level, sloping in no direction, say that a line on it bends up at a point when it rises on both sides of that point, like a valley. It bends down when it drops on both sides, like a hill. The middle of the seat is level, so there the seat bends up along the horse and down across it.

To compare these, give bending a sign. Upward bending counts as positive and downward bending as negative, and a sharper bend gets a bigger number before its sign. The principal curvatures are then the largest and the smallest of these signed values.

On a saddle like this, which is shaped the same on both sides of the horse, the directions of the principal curvatures are along the horse and across it. The principal curvature along the horse is positive, and the one across it is negative.

**Try it:** Lay a saddle-shaped crisp on a table, so that it rests on its two low sides. Slide a fingertip across its middle from one raised side to the other. The path goes down to the middle and back up, like a valley, so the crisp bends up that way. Now slide from one low side to the other. The path goes up over the middle and back down, like a hill, so the crisp bends down that way.

**Takeaway:** At a saddle-shaped point, one principal curvature is positive and the other negative. Counting signs, they are the largest and smallest bending, and their directions are still a quarter turn apart.

*Continues:* `ways_in/turn-a-ruler-on-an-egg`<br>*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `checks/mountain-pass`

### 3. The extremes are eigenvalues · working · calculation

*How do you find the principal curvatures and their directions from the second fundamental form in any coordinates?*

The ruler turning on the egg in 'Turn a ruler on an egg' reads the normal curvature direction by direction, and 'A saddle bends both ways' gave it a sign. On a surface $\mathbf X(x^1, x^2)$ in flat space, with induced metric $g_{\mu\nu}$, a chosen unit normal $\hat{\mathbf n}$ and second fundamental form $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$, the normal curvature in a unit direction $t^\mu$ is $\kappa_n = K_{\mu\nu}t^\mu t^\nu$, positive when the surface bends toward $\hat{\mathbf n}$. The principal curvatures $\kappa_1 \ge \kappa_2$ are its largest and smallest values over directions with $g_{\mu\nu}t^\mu t^\nu = 1$.

A Lagrange multiplier turns this constrained problem into an eigenvalue problem. The derivation 'Extremes by a Lagrange multiplier' gives

$$K^\mu{}_\nu\,t^\nu = \kappa\,t^\mu,\qquad K^\mu{}_\nu = g^{\mu\lambda}K_{\lambda\nu},$$

and shows that each eigenvalue equals $\kappa_n$ in its own eigendirection. The mixed tensor $K^\mu{}_\nu$ is the shape operator. Its eigenvalues do not depend on the coordinates. The eigenvalues of the component matrix $K_{\mu\nu}$ do, and they are guaranteed to be the principal curvatures only in a basis that is orthonormal at the point. With the mean curvature $H = \tfrac12K^\mu{}_\mu$,

$$\kappa_{1,2} = H \pm \sqrt{H^2 - \det K^\mu{}_\nu},$$

and the Gaussian curvature is the product $\kappa_1\kappa_2 = \det K^\mu{}_\nu$. In an orthonormal basis at the point, $K^\mu{}_\nu$ is a symmetric matrix and $H^2 - \det K^\mu{}_\nu = \tfrac14(K_{11} - K_{22})^2 + K_{12}^2 \ge 0$. So the principal curvatures are always real, and they coincide only where $K_{\mu\nu} = \kappa\,g_{\mu\nu}$, at an umbilic point. Where they differ, the symmetry of $K_{\mu\nu}$ gives $(\kappa_1 - \kappa_2)\,g_{\mu\nu}t_1^\mu t_2^\nu = 0$: the principal directions are perpendicular, which is the egg's quarter turn.

Measure the angle $\phi$ of a unit direction from the $\kappa_1$ direction. Then Euler's formula gives every normal curvature at the point:

$$\kappa_n(\phi) = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi = H + \tfrac12(\kappa_1 - \kappa_2)\cos 2\phi.$$

Two consequences follow at once. The normal curvatures of any two perpendicular directions add to $2H$, so $H$ is also the average of $\kappa_n$ over all directions. At a saddle point, where $\kappa_1 > 0 > \kappa_2$, $\kappa_n$ vanishes where $\tan^2\phi = -\kappa_1/\kappa_2$.

Reversing $\hat{\mathbf n}$ negates $K_{\mu\nu}$, $H$ and both principal curvatures, and swaps which one is called $\kappa_1$; the directions and the product do not change. A sphere of radius $a$ with the outward normal has $\kappa_1 = \kappa_2 = -1/a$ at every point, so every point is umbilic. A can of radius $a$ has $0$ along its length and $-1/a$ around it.

**Takeaway:** The principal curvatures and directions are the eigenvalues and eigenvectors of the second fundamental form with one index raised by the inverse metric, and Euler's formula gives every other normal curvature from them.

*What this leaves out:* Assumes a $C^2$ surface in flat three-dimensional space and a chosen normal.

*Continues:* `ways_in/turn-a-ruler-on-an-egg`, `ways_in/a-saddle-bends-both-ways`<br>*Builds on:* [[normal-curvature]], [[second-fundamental-form]], [[eigenvalues-and-eigenvectors]]<br>*Visuals:* [[card-touching-a-curved-patch]]<br>*See:* `derivations/extremes-by-a-lagrange-multiplier`, `checks/helical-lines-on-a-can`, `checks/soap-film-flat-claim`

### 4. Earth's two bendings, surveyed · working · operational

*How do surveyors measure the principal curvatures of Earth's surface, and what do they find?*

The egg in 'Turn a ruler on an egg' bent more sharply around its widest part than along it. Sea level on Earth also bends by different amounts in two directions, on a far larger scale but the other way round: at the equator, a walk that never steers turns slightly more quickly heading toward a pole than along the equator. 'The extremes are eigenvalues' says where to look for the extremes. Geodesists treat sea level as an ellipsoid of revolution with equatorial radius $a$ and flattening $f$, with $e^2 = f(2 - f)$. At any point, the plane through the axis and that point is a mirror symmetry that fixes the point, so the principal directions are along the meridian and at right angles to it. Their principal radii of curvature at geodetic latitude $\varphi$, stated here without derivation, are

$$M = \frac{a(1 - e^2)}{(1 - e^2\sin^2\varphi)^{3/2}},\qquad N = \frac{a}{(1 - e^2\sin^2\varphi)^{1/2}}.$$

$N$ is the length of the normal from the surface to the axis, as Meusnier's theorem requires for the circle of latitude.

A surveyor reads $1/M$ as the change of astronomical latitude, the tilt of the plumb line measured against the stars, per unit distance along a meridian. Along a unit direction $t^\mu$ the normal changes as $d\hat{\mathbf n}/ds = -K^\lambda{}_\mu t^\mu\,\partial_\lambda\mathbf X$, Weingarten's equation, which follows from differentiating $\hat{\mathbf n}\cdot\partial_\nu\mathbf X = 0$. This change is parallel to the path exactly when $t^\mu$ is principal. So heading at right angles to the meridian, the plumb line tilts along the path at the rate $1/N$, with no sideways lean. For the GRS80 reference ellipsoid used in geodesy, with $a = 6378.137$ km and $f = 1/298.257$:

- at the equator, $M = 6335.4$ km and $N = 6378.1$ km, so a degree of tilt takes $110.574$ km along the meridian and $111.319$ km along the equator;

- at latitude $45^\circ$, $M = 6367.4$ km and $N = 6388.8$ km;

- at either pole, $M = N = 6399.6$ km, so every direction bends alike and the poles are umbilic points.

Away from the poles $M < N$, so the meridian carries the larger principal curvature in size. Heading at $45^\circ$ to the meridian at the equator, Euler's formula gives a radius of $6356.7$ km. The product $1/(MN)$ ranges only from $2.442\times10^{-8}$ km$^{-2}$ at the poles to $2.475\times10^{-8}$ km$^{-2}$ at the equator.

**Takeaway:** On Earth's reference ellipsoid the principal directions run along the meridian and at right angles to it, with radii from about 6335 to 6400 kilometres, and the poles are umbilic points.

*What this leaves out:* Uses the reference ellipsoid. The real sea-level surface departs from it by up to about 100 metres, and plumb lines deviate slightly from its normal.

*Continues:* `ways_in/turn-a-ruler-on-an-egg`, `ways_in/extremes-are-eigenvalues`<br>*Visuals:* [[plumb-lines-along-a-walk]]<br>*See:* `observations/earth-ellipsoid-radii`

### 5. The shape operator, umbilics and topology · formal · structure

*What theorems govern the principal curvatures of a hypersurface, where do they stop being smooth, and what does topology force?*

The eigenvalue problem of 'The extremes are eigenvalues' is the spectral theorem for one self-adjoint map. Let $(M^{n+1}, \bar g)$ be Riemannian with Levi-Civita connection $\bar\nabla$, and $\Sigma^n \subset M$ a $C^k$ hypersurface, $k \ge 2$, with induced metric $g$ and unit normal field $N$. The shape operator $S: T_p\Sigma \to T_p\Sigma$ is defined by $\bar\nabla_XN = -S(X)$, so that $g(S(X), Y) = \mathrm{II}(X,Y)$, the second fundamental form; in components $S^\mu{}_\nu = K^\mu{}_\nu$.

*Definitions.* $\mathrm{II}$ is symmetric, so $S$ is self-adjoint on $(T_p\Sigma, g_p)$. Its eigenvalues $\kappa_1 \ge \dots \ge \kappa_n$ are the principal curvatures, and a $g$-orthonormal eigenbasis gives principal directions. The mean curvature is $H = \tfrac1n\,\mathrm{tr}\,S$, and $\det S$ is the Gauss–Kronecker curvature; for $n = 2$ the Gauss equation makes it the Gaussian curvature of $\Sigma$ minus the ambient sectional curvature of the tangent plane, so the two agree when the ambient space is flat. A point is umbilic when $S = \kappa\,\mathrm{id}$. A curve whose tangent is principal at every point is a line of curvature.

*Results.*

- Extremal characterization. For unit $X$, $\mathrm{II}(X,X)$ is the Rayleigh quotient of $S$. So $\kappa_1$ and $\kappa_n$ are its maximum and minimum, and by the min–max theorem $\kappa_k = \max_{\dim V = k}\,\min_{X\in V,\,|X| = 1}\mathrm{II}(X,X)$. For $n = 2$ this is Euler's formula.

- Regularity. $S$ is $C^{k-2}$. For $n = 2$, $\kappa_{1,2} = H \pm \sqrt{H^2 - \det S}$ are continuous everywhere, and they and the two principal line fields are $C^{k-2}$ away from umbilics, where the square root vanishes. At an umbilic they can fail to be differentiable.

- Rodrigues' formula. Along a unit-speed curve the Weingarten equation gives $dN/ds = -S(T)$, so the curve is a line of curvature exactly when $dN/ds = -\kappa\,T$, with $\kappa$ its principal curvature. The derivation 'Rodrigues' formula from Weingarten' writes this out.

- Umbilic surfaces. A connected $C^3$ surface in $\mathbb R^3$ made entirely of umbilics lies in a plane or a sphere. Isolated umbilics are common: the vertex of a paraboloid of revolution, the poles of a spheroid, four points of a triaxial ellipsoid.

- Index. Around an isolated umbilic of a surface, a principal line field turns by $2\pi j$, with $j \in \tfrac12\mathbb Z$. On a closed surface whose umbilics are isolated, the Poincaré–Hopf theorem for line fields, taken on trust here, gives $\sum j = \chi(\Sigma)$. So every closed surface of genus zero has umbilics, while a torus of revolution, with $\chi = 0$, has none. The four umbilics of a triaxial ellipsoid each have $j = +\tfrac12$.

- Constant mean curvature. On a surface in $\mathbb R^3$ with constant $H$, the umbilics are the zeros of a holomorphic quadratic differential, the Hopf differential. A sphere carries no nonzero holomorphic quadratic differential, so an immersed sphere of constant mean curvature is round, as Hopf showed.

*Proof sketch of the extremal characterization.* On the unit sphere of $(T_p\Sigma, g_p)$, a critical point of $f(X) = \mathrm{II}(X,X)$ satisfies $\mathrm{II}(X,\cdot) = \lambda\,g(X,\cdot)$, that is $S(X) = \lambda X$, and then $f(X) = \lambda$. Eigenvectors with $\lambda \ne \mu$ obey $\lambda\,g(X,Y) = g(SX, Y) = g(X, SY) = \mu\,g(X,Y)$, so they are orthogonal. In an orthonormal eigenbasis of a surface, $f(\cos\phi\,e_1 + \sin\phi\,e_2) = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$.

*Limits of validity.* Reversing $N$ negates $S$ and every $\kappa_i$ and reverses their order; $\det S$ is unchanged when $n$ is even. At a crease or a cone tip, $S$ is undefined. In higher codimension each normal $\nu$ has its own shape operator $S_\nu$, and the principal curvatures depend on $\nu$. If $\bar g$ is Lorentzian and $\Sigma$ is spacelike, $g$ is positive definite, and the extremal characterization, the regularity and Rodrigues' formula hold unchanged, with $\bar g(N,N) = -1$ entering the Gauss formula. If $\Sigma$ is timelike, $g$ is indefinite, and a $g$-self-adjoint $S$ need not be diagonalizable: its principal curvatures can be complex, or a repeated eigenvalue can have a one-dimensional eigenspace.

**Takeaway:** Principal curvatures are the eigenvalues of a self-adjoint shape operator, smooth away from umbilics; topology forces umbilics on closed surfaces of genus zero, and reality fails for timelike hypersurfaces.

*What this leaves out:* Takes $\Sigma$ to be a $C^2$ or smoother hypersurface with a chosen unit normal; the index statements are for surfaces with isolated umbilics.

*Continues:* `ways_in/extremes-are-eigenvalues`<br>*Builds on:* [[second-fundamental-form]], [[tangent-space]]<br>*Visuals:* [[lines-of-curvature-on-an-ellipsoid]]<br>*See:* `derivations/rodrigues-from-weingarten`, `problems/star-umbilic`, `checks/no-umbilic-free-egg`, `checks/timelike-surface-claim`

### 6. Slices, horizons and mass · research · bridge

*Where do principal curvatures and mean curvature do work in general relativity?*

The limits of 'The shape operator, umbilics and topology' allowed spacelike hypersurfaces in a Lorentzian spacetime, and two kinds of such surfaces carry much of general relativity. Set $G = c = 1$.

*Slices of spacetime.* On a spacelike slice with future unit normal $n$ and induced metric $h_{ij}$, the second fundamental form is the extrinsic curvature $K_{ij}$, and its eigenvalues with respect to $h_{ij}$ are the principal curvatures of the slice. Their overall sign follows a convention that differs between texts, but expressions of even degree in them do not. The vacuum Hamiltonian constraint reads ${}^{(3)}\!R + (h^{ij}K_{ij})^2 - K_{ij}K^{ij} = 0$, and in a principal frame $(h^{ij}K_{ij})^2 - K_{ij}K^{ij} = 2\sum_{i<j}\kappa_i\kappa_j$.

The Kasner solution $ds^2 = -dt^2 + \sum_i t^{2p_i}(dx^i)^2$ makes this concrete. Its slices $t = \text{const}$ are flat, and their principal curvatures are $p_i/t$ along the coordinate axes, up to that overall sign. The constraint forces $\sum_{i<j}p_ip_j = 0$, and with $\sum_ip_i = 1$ from the evolution equations, $\sum_ip_i^2 = 1$. Unless one exponent is $1$ and the others $0$, a case that is flat spacetime, exactly one exponent is negative. So toward $t = 0$ the principal curvatures diverge with mixed signs, one direction stretching while two contract. Belinski, Khalatnikov and Lifshitz argued that in vacuum a generic spacelike singularity is approached through a sequence of such Kasner epochs.

*Minimal surfaces as horizons.* A closed two-surface in a slice with $H = 0$, so $\kappa_1 = -\kappa_2$ at every point, is a minimal surface. In time-symmetric data, $K_{ij} = 0$, the outermost minimal surface is the apparent horizon. On the sphere $r = r_0$ of the time-symmetric Schwarzschild slice both principal curvatures have size $\sqrt{1 - 2M/r_0}/r_0$, which vanishes at the horizon $r_0 = 2M$.

*Quasi-local mass.* In time-symmetric data, the Hawking mass of a closed two-surface $\Sigma$ of area $A$ is

$$m_{\rm H} = \sqrt{\frac{A}{16\pi}}\left(1 - \frac{1}{16\pi}\oint_\Sigma(\kappa_1 + \kappa_2)^2\,dA\right).$$

It equals $M$ on every Schwarzschild sphere. In flat space it is never positive, by Willmore's inequality $\oint(\kappa_1 + \kappa_2)^2\,dA \ge 16\pi$, with equality only for round spheres. Geroch observed, and Huisken and Ilmanen proved in a weak formulation, that $m_{\rm H}$ does not decrease along inverse mean curvature flow, in which the surface moves outward with speed $1/|\kappa_1 + \kappa_2|$, when the slice has nonnegative scalar curvature. On the outermost minimal surface $m_{\rm H} = \sqrt{A/16\pi}$, and far out it is bounded by the ADM mass, which proves the Riemannian Penrose inequality $M_{\rm ADM} \ge \sqrt{A/16\pi}$ for a connected horizon.

**Takeaway:** Principal curvatures of spacetime slices enter the Hamiltonian constraint, which fixes the Kasner exponents, and the mean curvature of closed surfaces locates horizons and defines the Hawking mass.

*What this leaves out:* Uses time-symmetric data for the horizon and Hawking-mass statements, and leaves the overall sign of $K_{ij}$ unfixed.

*Continues:* `ways_in/shape-operator-and-umbilics`<br>*See:* `checks/hawking-mass-of-schwarzschild-spheres`, `problems/kasner-exponents`, `research_horizon/penrose-inequality`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| principal curvatures | — | The largest and smallest bending of a surface at a point, comparing every direction a ruler touching it there could point. Bending toward one side counts as positive, and toward the other side as negative. | [[principal-curvatures]] |
| bend up | — | Where a surface is level, sloping in no direction, a line on it bends up at a point when it rises on both sides of that point, like a valley. It bends down when it drops on both sides, like a hill. | — |
| steer | — | To turn your direction of travel to your left or your right along the ground, as a cyclist does with the handlebars. | — |
| saddle | — | A horse's riding seat, which rises toward the front and back and drops over the horse's sides. A surface bending like that at a point is called saddle-shaped there. | — |
| equator | — | The circle around Earth's middle, the same distance from both poles. | — |

## Key equations

### Principal curvatures as eigenvalues · working

$$
K^\mu{}_\nu\,t^\nu = \kappa\,t^\mu,\qquad K^\mu{}_\nu = g^{\mu\lambda}K_{\lambda\nu}
$$

The principal directions are the eigenvectors of the shape operator, and the principal curvatures are its eigenvalues.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K^\mu{}_\nu$ | shape operator: the second fundamental form with its first index raised | K upper mu lower nu |
| $g^{\mu\lambda}$ | inverse induced metric | g upper mu lambda |
| $t^\mu$ | a principal direction | t mu |
| $\kappa$ | the principal curvature in that direction, positive toward the chosen normal | kappa |

**Holds when:** $C^2$ surface in flat three-dimensional space; signs set by the chosen normal $\hat{\mathbf n}$.  
**Say it:** “K upper mu lower nu times t nu equals kappa times t mu, where K upper mu lower nu is the second fundamental form with an index raised by the inverse metric.”  
**Justified by:** `derivations/extremes-by-a-lagrange-multiplier`

### Principal curvatures from the mean curvature and the determinant · working

$$
\kappa_{1,2} = H \pm \sqrt{H^2 - \det K^\mu{}_\nu},\qquad H = \tfrac12 K^\mu{}_\mu
$$

The two principal curvatures sit symmetrically about the mean curvature, separated by a square root that vanishes only at umbilic points.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $H$ | mean curvature, half the trace of $K^\mu{}_\nu$ | H |
| $\det K^\mu{}_\nu$ | determinant of the shape operator, the Gaussian curvature $\kappa_1\kappa_2$ | the determinant of the shape operator |

**Holds when:** Surface in flat three-dimensional space; the square root is real and is zero exactly at umbilic points.  
**Say it:** “Kappa one and kappa two are H plus or minus the square root of H squared minus the determinant of the shape operator.”  
**Justified by:** `derivations/extremes-by-a-lagrange-multiplier`

### Euler's curvature formula · working

$$
\kappa_n(\phi) = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi
$$

Every normal curvature at a point is a weighted mix of the two principal curvatures.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa_n(\phi)$ | normal curvature in a unit direction | kappa n of phi |
| $\phi$ | angle of that direction from the $\kappa_1$ direction, measured with the metric | phi |

**Holds when:** At an umbilic every direction gives the same value; $\phi$ is defined modulo $\pi$.  
**Say it:** “Kappa n of phi equals kappa one times cos squared phi plus kappa two times sine squared phi.”  
**Justified by:** `derivations/extremes-by-a-lagrange-multiplier`

### Rodrigues' formula · formal

$$
\frac{dN}{ds} = -\kappa\,T
$$

Along a line of curvature the unit normal turns in the direction of travel, at the rate of the principal curvature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $N$ | unit normal field | N |
| $T$ | unit tangent of the curve | T |
| $\kappa$ | principal curvature in the direction of the curve | kappa |

**Holds when:** Unit-speed curve on a $C^2$ hypersurface; holds exactly when $T$ is principal at every point; $d/ds$ is $\bar\nabla_T$ in a curved ambient space.  
**Say it:** “The derivative of the normal along the curve is minus kappa times the tangent.”  
**Justified by:** `derivations/rodrigues-from-weingarten`

### Index sum of umbilics · formal

$$
\sum_{p\ \text{umbilic}} j_p = \chi(\Sigma)
$$

The half-integer turning numbers of a principal line field around the umbilics of a closed surface add up to its Euler characteristic.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $j_p$ | index of the umbilic $p$: the turn of a principal line field around it, in units of $2\pi$ | j p |
| $\chi(\Sigma)$ | Euler characteristic of the surface | chi of sigma |

**Holds when:** Closed $C^2$ surface whose umbilics are isolated.  
**Say it:** “The indices of the umbilics add up to the Euler characteristic.”  
**Justified by:** `stated`

### Hawking mass in time-symmetric data · research

$$
m_{\rm H} = \sqrt{\frac{A}{16\pi}}\left(1 - \frac{1}{16\pi}\oint_\Sigma(\kappa_1 + \kappa_2)^2\,dA\right)
$$

A mass assigned to a closed surface from its area and the squared sum of its principal curvatures.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $m_{\rm H}$ | Hawking mass | the Hawking mass |
| $A$ | area of the surface | A |
| $\kappa_1 + \kappa_2$ | twice the mean curvature of the surface within the slice | kappa one plus kappa two |

**Holds when:** $G = c = 1$; closed two-surface in initial data with zero extrinsic curvature. In SI the mass is $c^2 m_{\rm H}/G$ with $m_{\rm H}$ a length.  
**Say it:** “The Hawking mass is the square root of A over sixteen pi, times one minus one over sixteen pi times the integral of kappa one plus kappa two, squared, over the surface.”  
**Justified by:** `stated`

## Derivations

### Extremes by a Lagrange multiplier · working

**Goal:** Show that the extremes of $\kappa_n = K_{\mu\nu}t^\mu t^\nu$ over unit directions are the eigenvalues of $K^\mu{}_\nu$, in perpendicular directions, and derive Euler's formula.

1. The unit directions form a closed curve, so the maximum and minimum of $K_{\mu\nu}t^\mu t^\nu$ on it exist. At each, $L = K_{\mu\nu}t^\mu t^\nu - \kappa\,(g_{\mu\nu}t^\mu t^\nu - 1)$ is stationary for some multiplier $\kappa$.
2. Differentiate with respect to $t^\lambda$, using the symmetry of $K_{\mu\nu}$ and $g_{\mu\nu}$: $2K_{\lambda\nu}t^\nu - 2\kappa\,g_{\lambda\nu}t^\nu = 0$.
3. Multiply by $g^{\mu\lambda}$: $K^\mu{}_\nu t^\nu = \kappa\,t^\mu$, an eigenvalue problem for the shape operator.
4. Contract $K_{\lambda\nu}t^\nu = \kappa\,g_{\lambda\nu}t^\nu$ with $t^\lambda$ and use $g_{\lambda\nu}t^\lambda t^\nu = 1$: $K_{\lambda\nu}t^\lambda t^\nu = \kappa$. Each eigenvalue is the normal curvature in its own direction.
5. For eigenvectors $t_1$ and $t_2$, $K_{\mu\nu}t_1^\mu t_2^\nu$ equals $\kappa_2\,g_{\mu\nu}t_1^\mu t_2^\nu$ from the eigen-equation for $t_2$, and $\kappa_1\,g_{\mu\nu}t_1^\mu t_2^\nu$ from the one for $t_1$ and the symmetry of $K_{\mu\nu}$.
6. Subtract: $(\kappa_1 - \kappa_2)\,g_{\mu\nu}t_1^\mu t_2^\nu = 0$. Where $\kappa_1 \ne \kappa_2$ the principal directions are perpendicular, and then $K_{\mu\nu}t_1^\mu t_2^\nu = 0$ too.
7. Write a unit direction as $t = \cos\phi\,t_1 + \sin\phi\,t_2$ with $t_1, t_2$ unit. Expanding, the cross terms vanish and $K_{\mu\nu}t^\mu t^\nu = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$.
8. The characteristic polynomial of $K^\mu{}_\nu$ is $\kappa^2 - K^\mu{}_\mu\,\kappa + \det K^\mu{}_\nu$. Its roots are $\kappa_{1,2} = H \pm \sqrt{H^2 - \det K^\mu{}_\nu}$ with $H = \tfrac12K^\mu{}_\mu$.

**Result:** $K^\mu{}_\nu t^\nu = \kappa\,t^\mu$ with $\kappa$ the normal curvature of $t$; perpendicular principal directions where $\kappa_1 \ne \kappa_2$; $\kappa_n(\phi) = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$; and $\kappa_{1,2} = H \pm \sqrt{H^2 - \det K^\mu{}_\nu}$.

### Rodrigues' formula from Weingarten · formal

**Goal:** Show that a unit-speed curve on a hypersurface is a line of curvature exactly when $dN/ds = -\kappa\,T$.

1. Along the curve, $dN/ds = \bar\nabla_TN = -S(T)$ by the Weingarten equation.
2. If $T$ is principal at every point with principal curvature $\kappa$, then $S(T) = \kappa\,T$ and $dN/ds = -\kappa\,T$.
3. Conversely, if $dN/ds = -\lambda\,T$ for some function $\lambda$, then $S(T) = \lambda\,T$, so $T$ is principal and $\lambda$ is its principal curvature.
4. On a surface of revolution the plane through the axis and the point is a mirror symmetry, so meridians and circles of latitude are lines of curvature; on a sphere every point is umbilic and every curve is one.

**Result:** A curve is a line of curvature iff $dN/ds = -\kappa\,T$, with $\kappa$ the principal curvature along it.

## Problems

### `satellite-dish` · working · difficulty 2 · calculation

A satellite dish is the paraboloid $z = r^2/(4F)$ with focal length $F = 1.0$ m and rim radius $1.2$ m. With the normal pointing into the dish, find the principal curvatures at the vertex and at the rim, and find every umbilic point of the dish.

**Hints**

1. Which directions does the mirror symmetry through the axis make principal?
2. Use Meusnier's theorem for the circle around the dish.

**Answer:** At the vertex both are $1/(2F) = 0.50$ m$^{-1}$. At the rim, $0.315$ m$^{-1}$ along the profile (radius $3.17$ m) and $0.429$ m$^{-1}$ around the dish (radius $2.33$ m). The vertex is the only umbilic.

**Must contain:** Both principal curvatures one half per metre at the vertex; At the rim, 0.315 along the profile and 0.429 around, per metre; The vertex is the only umbilic

**Numeric:** radius of curvature along the profile at the rim = 3.17 m (magnitude, ±1%); radius of curvature around the dish at the rim = 2.33 m (magnitude, ±1%)

**Solution**

1. The plane through the axis and any point is a mirror symmetry of the dish, so the principal directions are along the profile and around the dish.
2. The profile has slope $z' = r/(2F)$ and $z'' = 1/(2F)$. Its curvature, bending toward the inward normal, is $\kappa_{\rm p} = z''/(1 + z'^2)^{3/2}$.
3. The circle around the dish has radius $r$ and curvature $1/r$, pointing at the axis. The inward normal makes an angle with that direction whose cosine is $z'/\sqrt{1 + z'^2}$, so Meusnier's theorem gives $\kappa_{\rm c} = z'/(r\sqrt{1 + z'^2}) = (1/2F)/\sqrt{1 + z'^2}$.
4. At $r = 0$, $z' = 0$, so $\kappa_{\rm p} = \kappa_{\rm c} = 1/(2F) = 0.50$ m$^{-1}$.
5. At $r = 1.2$ m, $z' = 0.6$ and $1 + z'^2 = 1.36$. So $\kappa_{\rm p} = 0.5/1.586 = 0.315$ m$^{-1}$ and $\kappa_{\rm c} = 0.5/1.166 = 0.429$ m$^{-1}$, radii $3.17$ m and $2.33$ m.
6. $\kappa_{\rm c}/\kappa_{\rm p} = 1 + z'^2 > 1$ for every $r > 0$, so no point other than the vertex is umbilic, although the dish is not part of a sphere.

**Targets:** `umbilics-only-on-spheres`

### `star-umbilic` · formal · difficulty 3 · derivation

Near the origin, a surface is the graph $z = \tfrac12(x^2 + y^2) + \tfrac16(x^3 - 3xy^2)$ in units of a fixed length, with the normal along $+z$ at the origin. (a) Show that the origin is umbilic with $\kappa = 1$. (b) Show that $\kappa_1 - \kappa_2 = 2r + O(r^2)$ at distance $r$ from the origin, so neither principal curvature is differentiable there. (c) As the point goes once around the origin, counterclockwise seen from $+z$, how does the $\kappa_1$ direction turn? Give the index.

**Hints**

1. The metric and the normal's length factor differ from their values at the origin only at order $r^2$.
2. Write the traceless part of the shape operator as $r$ times a reflection matrix.

**Answer:** (a) $K^\mu{}_\nu = \delta^\mu{}_\nu$ at the origin. (b) $K^\mu{}_\nu = \delta^\mu{}_\nu + \begin{pmatrix}x & -y\\ -y & -x\end{pmatrix} + O(r^2)$, whose traceless part has eigenvalues $\pm r$. (c) At polar angle $\theta$ the $\kappa_1$ direction is at angle $-\theta/2$, so it turns by half a turn clockwise over one counterclockwise loop: index $-\tfrac12$.

**Must contain:** The shape operator at the origin is the identity; The traceless part is r times a reflection matrix, with eigenvalues plus and minus r; Principal curvatures are one plus or minus r, continuous but not differentiable at the origin; The principal direction turns by minus half a turn, index minus one half

**Numeric:** index of the umbilic = -0.5 1 (signed, ±0.01)

**Solution**

1. The gradient $(z_x, z_y) = \big(x + \tfrac12(x^2 - y^2),\ y - xy\big)$ is $O(r)$, so $g_{\mu\nu} = \delta_{\mu\nu} + O(r^2)$ and the unit normal's normalization factor is $1 + O(r^2)$.
2. So $K_{\mu\nu}$ is the Hessian up to $O(r^2)$: $z_{xx} = 1 + x$, $z_{yy} = 1 - x$ and $z_{xy} = -y$. Raising an index changes nothing at this order: $K^\mu{}_\nu = \delta^\mu{}_\nu + \begin{pmatrix}x & -y\\ -y & -x\end{pmatrix} + O(r^2)$.
3. At the origin $K^\mu{}_\nu = \delta^\mu{}_\nu$, so every direction has $\kappa_n = 1$: an umbilic.
4. With $x = r\cos\theta$, $y = r\sin\theta$ the traceless part is $r\begin{pmatrix}\cos\theta & -\sin\theta\\ -\sin\theta & -\cos\theta\end{pmatrix}$, $r$ times a reflection matrix, with eigenvalues $\pm r$. So $\kappa_{1,2} = 1 \pm r + O(r^2)$ and $\kappa_1 - \kappa_2 = 2r + O(r^2)$.
5. $r = \sqrt{x^2 + y^2}$ has no derivative at the origin, so neither $\kappa_1$ nor $\kappa_2$ is differentiable there, although both are continuous.
6. The eigenvector of that reflection matrix for $+1$ is $(\cos\tfrac\theta2, -\sin\tfrac\theta2)$: check $\cos\theta\cos\tfrac\theta2 + \sin\theta\sin\tfrac\theta2 = \cos\tfrac\theta2$ and $-\sin\theta\cos\tfrac\theta2 + \cos\theta\sin\tfrac\theta2 = -\sin\tfrac\theta2$. So the $\kappa_1$ direction is at angle $-\theta/2$.
7. As $\theta$ runs from $0$ to $2\pi$, the direction turns by $-\pi$, against the loop, so the index is $-\tfrac12$: a star umbilic.

### `kasner-exponents` · research · difficulty 2 · derivation

With $G = c = 1$, the Kasner metric is $ds^2 = -dt^2 + \sum_{i=1}^3 t^{2p_i}(dx^i)^2$ for $t > 0$. (a) Taking $K_{ij} = \tfrac12\partial_th_{ij}$ for the slices $t = \text{const}$, find their principal curvatures. (b) Use the vacuum Hamiltonian constraint to relate the exponents. (c) Given $\sum_ip_i = 1$ from the evolution equations, show that unless one exponent is $1$ and the others $0$, exactly one exponent is negative, and check $p = (-\tfrac13, \tfrac23, \tfrac23)$.

**Hints**

1. Raise an index of $K_{ij}$ with $h^{ij} = \mathrm{diag}(t^{-2p_i})$.
2. The slices are flat, so ${}^{(3)}\!R = 0$.

**Answer:** (a) $p_i/t$ along the coordinate axes. (b) $\sum_{i<j}p_ip_j = 0$. (c) Then $\sum_ip_i^2 = 1$; two negative exponents would push the third above $1$, and no negative exponent forces two zeros. $(-\tfrac13, \tfrac23, \tfrac23)$ has sum $1$ and squares summing to $1$.

**Must contain:** Extrinsic curvature with an index raised is p i over t on the diagonal; The constraint gives the sum of pairwise products equal to zero; With the sum equal to one, the squares also sum to one; Exactly one exponent is negative except in the flat cases

**Solution**

1. The unit normal is $n = \partial_t$ and $h_{ij} = \mathrm{diag}(t^{2p_1}, t^{2p_2}, t^{2p_3})$, so $K_{ij} = \tfrac12\partial_th_{ij} = \mathrm{diag}(p_it^{2p_i - 1})$.
2. Raising an index, $K^i{}_j = \mathrm{diag}(p_1, p_2, p_3)/t$: the principal curvatures are $p_i/t$ along the axes. The opposite sign convention negates all three.
3. Rescaling each $x^i$ by the constant $t^{p_i}$ makes $h_{ij} = \delta_{ij}$ on a slice, so the slices are flat and ${}^{(3)}\!R = 0$.
4. The vacuum constraint becomes $(h^{ij}K_{ij})^2 - K_{ij}K^{ij} = 0$, that is $(\sum_ip_i)^2 - \sum_ip_i^2 = 2\sum_{i<j}p_ip_j = 0$, in either sign convention.
5. With $\sum_ip_i = 1$, $\sum_ip_i^2 = 1 - 2\sum_{i<j}p_ip_j = 1$.
6. If $p_1, p_2 < 0$, then $p_3 = 1 - p_1 - p_2 > 1$ and $\sum_ip_i^2 > 1$, a contradiction. If no exponent is negative, $\sum_{i<j}p_ip_j = 0$ makes every pairwise product zero, so two exponents vanish and the third is $1$.
7. For $(-\tfrac13, \tfrac23, \tfrac23)$: $-\tfrac13 + \tfrac23 + \tfrac23 = 1$ and $\tfrac19 + \tfrac49 + \tfrac49 = 1$. The principal curvatures are $-1/(3t)$, and $2/(3t)$ twice.

## Observations

- **Earth's two principal radii of curvature, which differ between the meridian and the direction at right angles to it everywhere except at the poles** (measured, working). Geodetic surveys measure how plumb lines tilt per kilometre along meridians and across them. Fitted to the reference ellipsoid, these give the principal radii $M$ and $N$, and the poles are umbilic points. *Numbers:* GRS80, $a = 6378.137$ km and $f = 1/298.257222101$: $M = 6335.4$ km and $N = 6378.1$ km at the equator, a degree of tilt taking $110.574$ km and $111.319$ km; $M = N = 6399.6$ km at the poles. *Reference:* Helmut Moritz (1980), *Geodetic Reference System 1980*, Bulletin Géodésique 54, 395–405, doi:10.1007/BF02521480
- **Soap films with equal air pressure on both sides have equal and opposite principal curvatures, so they are saddle-shaped wherever they are not flat** (measured, working). A liquid surface with tension $\gamma$ holds a pressure jump of size $\gamma(\kappa_1 + \kappa_2)$, higher on the side it bends toward. A film has two surfaces and holds twice that jump, so with no pressure difference it has $\kappa_1 = -\kappa_2$ at every point, as on a catenoid between two rings. *Numbers:* A soap bubble of radius $1.0$ cm with $\gamma \approx 0.025$ N/m holds $4\gamma/R \approx 10$ Pa. *Reference:* Thomas Young (1805), *An essay on the cohesion of fluids*, Philosophical Transactions of the Royal Society of London 95, 65–87, doi:10.1098/rstl.1805.0005

## Teaching arc

1. **Turn a ruler on an egg** (entry). Ask where the gentlest bending lies, then turn the ruler and name the principal curvatures. *Why:* The quarter turn is the surprise that makes the two extremes worth naming. *Predict:* If the shell bends most sharply when the ruler lies around the egg, in which direction does it bend least sharply? *Visual:* [[card-touching-a-curved-patch]] *Uses:* `ways_in/turn-a-ruler-on-an-egg`, `checks/helmet-top`, `common_questions/earths-two-bendings`
2. **Give bending a sign** (entry). Move to a saddle and a mountain pass, and count upward bending as positive. *Why:* With signs, one rule, largest and smallest, covers eggs and saddles alike. *Predict:* At the middle of a horse's saddle, does the seat bend the same way along the horse and across it? *Uses:* `ways_in/a-saddle-bends-both-ways`, `checks/mountain-pass`
3. **Raise the index** (working). Derive the eigenvalue problem, then test it on helical coordinates on a can. *Why:* It shows why the inverse metric enters. *Predict:* In slanted coordinates on a can, are the coordinate directions still the principal directions? *Uses:* `ways_in/extremes-are-eigenvalues`, `derivations/extremes-by-a-lagrange-multiplier`, `checks/helical-lines-on-a-can`
4. **Survey Earth** (working). Read Earth's principal radii from plumb-line tilts, and find the umbilic poles. *Why:* It attaches the concept to a measured surface. *Predict:* Where on Earth does the ground bend alike in every direction? *Visual:* [[plumb-lines-along-a-walk]] *Uses:* `ways_in/earths-two-bendings-surveyed`, `observations/earth-ellipsoid-radii`
5. **Find the umbilics** (formal). Prove the extremal characterization, analyse the star umbilic, and count indices on closed surfaces. *Why:* Umbilics are where principal directions break down, and topology can force them. *Visual:* [[lines-of-curvature-on-an-ellipsoid]] *Uses:* `ways_in/shape-operator-and-umbilics`, `problems/star-umbilic`, `checks/no-umbilic-free-egg`
6. **Weigh with bending** (research). Compute the Hawking mass of Schwarzschild spheres, then fix the Kasner exponents from the constraint. *Why:* Both show principal curvatures doing physical work in general relativity. *Uses:* `ways_in/slices-horizons-and-mass`, `checks/hawking-mass-of-schwarzschild-spheres`, `problems/kasner-exponents`

## Misconceptions

### “The sharpest and gentlest directions on a curved surface could be at any angle to each other.” · entry · `extremes-at-any-angle`

- **Why it is tempting:** Lumpy surfaces look too irregular for a neat angle.
- **What is true:** On an egg or a helmet, which stays on one side of a ruler, the sharpest and gentlest directions are a quarter turn apart, unless every direction bends alike. At a saddle, where the surface bends both ways, it is the largest and the smallest bending, counted with signs, whose directions are a quarter turn apart.
- **Exposed by:** `checks/helmet-top`

### “At any point, a curved surface bends toward the same side in every direction.” · entry · `bends-to-one-side`

- **Why it is tempting:** Balls, eggs and cans, the most familiar curved objects, all do.
- **What is true:** A saddle or a mountain pass bends up in one direction and down in another, so one principal curvature is positive and the other negative.
- **Exposed by:** `checks/mountain-pass`

### “The principal curvatures and directions are the eigenvalues and eigenvectors of the component matrix of the second fundamental form.” · working · `component-matrix-eigenvectors`

- **Why it is tempting:** In orthonormal tangent-plane coordinates they are, and first examples use those coordinates.
- **What is true:** They belong to the form with one index raised by the inverse metric. In a basis that is not orthonormal, the component matrix gives wrong values and directions.
- **Exposed by:** `checks/helical-lines-on-a-can`

### “A surface whose principal curvatures add up to zero is flat.” · working · `zero-mean-curvature-means-flat`

- **Why it is tempting:** Zero average bending sounds like no bending.
- **What is true:** Only the sum vanishes. The principal curvatures can be equal and opposite and large, as at the neck of a soap-film catenoid.
- **Exposed by:** `checks/soap-film-flat-claim`

### “Only spheres and planes have points where every direction bends alike, so a lumpy closed surface has none.” · formal · `umbilics-only-on-spheres`

- **Why it is tempting:** A connected surface made entirely of such points must be a piece of a sphere or a plane.
- **What is true:** That theorem is about surfaces made entirely of umbilics. Isolated umbilics are common, and topology forces them on every closed surface of genus zero.
- **Exposed by:** `checks/no-umbilic-free-egg`

### “The principal curvatures of any hypersurface are real, because the shape operator is self-adjoint.” · formal · `self-adjoint-means-real`

- **Why it is tempting:** For surfaces in Euclidean space the spectral theorem always applies.
- **What is true:** Self-adjointness gives real eigenvalues only for a positive-definite metric. On a timelike hypersurface in spacetime the principal curvatures can be complex.
- **Exposed by:** `checks/timelike-surface-claim`

## Checks

1. **Entry · predict** `checks/helmet-top`. A bike helmet has a smooth shell that stays on one side of a ruler laid on it, whichever way the ruler points. At the very top of the helmet, the shell bends most sharply in the direction from ear to ear. In which direction does it bend least sharply there?
   - **Hints:** How far apart were the sharpest and gentlest directions on the egg?
   - **Answer:** From front to back. The shell stays on one side of the ruler in every direction, so its sharpest and gentlest bending at a point are its principal curvatures. At a point of a smooth surface like that, the directions of the principal curvatures are a quarter turn apart, unless every direction bends alike. Here one direction bends most sharply, so they do not all bend alike. The sharpest direction runs from ear to ear, so the gentlest runs a quarter turn away from it, from front to back.
   - **Must contain:** From front to back; The sharpest and gentlest directions are a quarter turn apart; Front to back is a quarter turn from ear to ear
   - **Numeric:** angle between the sharpest and gentlest directions = 90 deg (magnitude, ±5)
   - **Targets:** `extremes-at-any-angle`
   - **Visual:** [[card-touching-a-curved-patch]]
2. **Entry · predict** `checks/mountain-pass`. A road crosses a mountain pass. At the road's highest point, the ground drops away ahead of a driver and behind, and it rises on both sides of the road. There the ground is level, and the directions of the principal curvatures are along the road and across it. Count upward bending as positive and downward bending as negative. Which principal curvature is positive, and which is negative?
   - **Hints:** Does the ground bend up or down along the road? And across it?
   - **Answer:** The one across the road is positive, and the one along the road is negative. Across the road, the ground rises on both sides of the highest point, like a valley. So it bends up there, which gives a positive value. Along the road, the ground drops ahead and behind, like a hill. So it bends down there, which gives a negative value. The principal curvatures are the largest and smallest signed values. So the positive one, across the road, is the largest, and the negative one, along the road, is the smallest.
   - **Must contain:** Positive across the road, because the ground rises on both sides like a valley; Negative along the road, because the ground drops ahead and behind like a hill; One principal curvature positive and one negative, as at a saddle
   - **Targets:** `bends-to-one-side`
3. **Working · evaluate-claim** `checks/helical-lines-on-a-can`. A can of radius 3 cm is parametrized by $\mathbf X(u,v) = (3\cos u,\ 3\sin u,\ v + 4u)$ in centimetres, so its lines of constant $v$ are helices. With the outward normal, a student finds $K_{uu} = -3$ cm and $K_{uv} = K_{vv} = 0$, and claims that $\mathbf e_u$ and $\mathbf e_v$ are the principal directions, with principal curvatures $-3$ cm and $0$. Evaluate the claim.
   - **Hints:** What units must a curvature have? / Compute $g^{\mu\nu}$ before taking eigenvalues.
   - **Answer:** The components are right; the claim is wrong. $\mathbf e_u = (-3\sin u, 3\cos u, 4)$ and $\mathbf e_v = (0, 0, 1)$ give $g_{uu} = 25$ cm$^2$, $g_{uv} = 4$ cm and $g_{vv} = 1$, with $\det g = 9$ cm$^2$. Raising an index gives $K^u{}_u = -1/3$ cm$^{-1}$ and $K^v{}_u = 4/3$, with the other two entries zero. So the eigenvalues are $-1/3$ cm$^{-1}$, a radius of $3$ cm, and $0$. The eigenvector for $-1/3$ cm$^{-1}$ is $\mathbf e_u - 4\mathbf e_v = (-3\sin u, 3\cos u, 0)$, around the can, and the one for $0$ is $\mathbf e_v$, along it. $\mathbf e_u$ climbs the helix at $53.1^\circ$ to the horizontal, where $\kappa_n = K_{uu}/g_{uu} = -0.12$ cm$^{-1}$, as Euler's formula confirms: $-\tfrac13\cos^2 53.1^\circ = -0.12$ cm$^{-1}$. The eigenvectors of the component matrix are principal only where the basis is orthonormal, and a curvature cannot have units of length.
   - **Must contain:** A curvature must have units of inverse length; Raise an index with the inverse metric first; Principal curvatures minus one third per centimetre and zero, around and along the can; The helix direction e u has normal curvature minus 0.12 per centimetre
   - **Numeric:** radius of the nonzero principal curvature = 3 cm (magnitude, ±0.05); radius of curvature of the normal slice along e u = 8.33 cm (magnitude, ±1%)
   - **Targets:** `component-matrix-eigenvectors`
4. **Working · evaluate-claim** `checks/soap-film-flat-claim`. A soap film spans two rings on a common axis, with equal air pressure on both sides, and forms the catenoid $r = c\cosh(z/c)$ with neck radius $c = 3$ cm. Claim: because $\kappa_1 + \kappa_2 = 0$ at every point, the film is flat at every point. Evaluate the claim at the neck.
   - **Hints:** Find the normal curvature of the neck circle and of the profile curve separately.
   - **Answer:** False. Equal pressures make $\kappa_1 + \kappa_2 = 0$, but that fixes only the sum. At the neck take the normal pointing away from the axis. The plane through the axis is a mirror symmetry, so the principal directions are around the neck and along the profile. The neck circle has radius $3$ cm and bends toward the axis, so its normal curvature is $-1/3$ cm$^{-1}$. The profile $r = 3\cosh(z/3)$ has $r' = 0$ and $r'' = 1/3$ cm$^{-1}$ there, so it bends away from the axis with $\kappa_n = +1/3$ cm$^{-1}$. The principal curvatures are $\pm 1/3$ cm$^{-1}$, their sum is zero, and their product is $-1/9$ cm$^{-2}$: the neck is saddle-shaped, not flat. Only the directions at $45^\circ$ to the axis have zero normal curvature.
   - **Must contain:** Zero mean curvature fixes only the sum; Principal curvatures plus and minus one third per centimetre at the neck; The product is negative, so the film is saddle-shaped
   - **Numeric:** radius of curvature of each principal slice at the neck = 3 cm (magnitude, ±0.05)
   - **Targets:** `zero-mean-curvature-means-flat`
5. **Formal · evaluate-claim** `checks/no-umbilic-free-egg`. Claim: a smooth, closed, egg-shaped surface in $\mathbb R^3$ with no symmetry at all can be made so that $\kappa_1 > \kappa_2$ at every point. Evaluate the claim, and contrast it with a torus of revolution.
   - **Hints:** What would the $\kappa_1$ directions define on the whole surface?
   - **Answer:** False. If $\kappa_1 > \kappa_2$ everywhere, the $\kappa_1$ eigenspaces of the shape operator form a continuous line field with no singular points, because the eigenvector of a simple eigenvalue of a continuous symmetric matrix field depends continuously on the point. An egg-shaped surface is a topological sphere, and the Poincaré–Hopf theorem for line fields says that the indices of the singular points of a line field on a closed surface add up to $\chi = 2$. A line field with no singular points has index sum $0 \ne 2$, so at least one umbilic exists. A torus of revolution with tube radius $a$ and centre-circle radius $b > a$ has principal curvatures $-1/a$ and $-\cos v/(b + a\cos v)$ with the outward normal; they are equal only if $b = 0$, so it has no umbilics, consistent with $\chi = 0$.
   - **Must contain:** Away from umbilics the principal directions form a continuous line field; The index sum of a line field equals the Euler characteristic, 2 for a sphere; So umbilics must exist; A torus of revolution has Euler characteristic 0 and no umbilics
   - **Targets:** `umbilics-only-on-spheres`
   - **Visual:** [[lines-of-curvature-on-an-ellipsoid]]
6. **Formal · evaluate-claim** `checks/timelike-surface-claim`. In Minkowski space with $ds^2 = -dt^2 + dx^2 + dy^2$, consider the timelike surface $y = tx/L$ near the origin, where its unit normal is $\partial_y$. Claim: like every hypersurface, it has two real principal curvatures in orthogonal directions at the origin. Evaluate the claim.
   - **Hints:** Write $S = g^{-1}\mathrm{II}$ with $g = \mathrm{diag}(-1, 1)$.
   - **Answer:** False. At the origin the tangent basis $\partial_t, \partial_x$ has $g = \mathrm{diag}(-1, 1)$, which is indefinite. The normal is $\partial_y$ and the surface is the height $y = tx/L$, so $\mathrm{II}_{ab} = \bar g(\partial_a\partial_b\mathbf X, \partial_y)$ is the Hessian of $tx/L$: $\mathrm{II}_{tt} = \mathrm{II}_{xx} = 0$ and $\mathrm{II}_{tx} = 1/L$. The shape operator $S = g^{-1}\mathrm{II}$ has $S^t{}_x = -1/L$ and $S^x{}_t = 1/L$, and zero diagonal. Its characteristic equation is $\kappa^2 + 1/L^2 = 0$, so $\kappa = \pm i/L$. $S$ is self-adjoint with respect to $g$, but that guarantees real eigenvalues and an orthonormal eigenbasis only when $g$ is positive definite, as it is on a spacelike hypersurface.
   - **Must contain:** The induced metric on a timelike surface is indefinite; The second fundamental form has off-diagonal entry one over L; The principal curvatures are plus and minus i over L; Real eigenvalues need a positive-definite metric
   - **Targets:** `self-adjoint-means-real`
7. **Research · derive** `checks/hawking-mass-of-schwarzschild-spheres`. With $G = c = 1$, the time-symmetric slice of Schwarzschild has metric $dr^2/(1 - 2M/r) + r^2d\Omega^2$. Find the principal curvatures of the sphere $r = r_0$ with the outward normal, and its Hawking mass. What is the Hawking mass of a round sphere in flat space?
   - **Hints:** Use $\Gamma^r{}_{ab} = -\tfrac12g^{rr}\partial_rg_{ab}$ for angular $a$ and $b$.
   - **Answer:** The outward unit normal is $N = \sqrt{1 - 2M/r}\,\partial_r$. For angular coordinate fields, $\mathrm{II}_{ab} = g_{rr}\Gamma^r{}_{ab}N^r = -\tfrac12\sqrt{1 - 2M/r_0}\,\partial_rg_{ab}$, so $\mathrm{II}_{\theta\theta} = -r_0\sqrt{1 - 2M/r_0}$ and $\mathrm{II}_{\phi\phi} = \sin^2\theta\,\mathrm{II}_{\theta\theta}$. Dividing by $g_{\theta\theta} = r_0^2$ gives $\kappa_1 = \kappa_2 = -\sqrt{1 - 2M/r_0}/r_0$: every point is umbilic. Then $(\kappa_1 + \kappa_2)^2 = 4(1 - 2M/r_0)/r_0^2$ and $A = 4\pi r_0^2$, so $\oint(\kappa_1 + \kappa_2)^2dA = 16\pi(1 - 2M/r_0)$ and $m_{\rm H} = (r_0/2)(2M/r_0) = M$ at every radius. At $r_0 = 2M$ the principal curvatures vanish, a minimal surface with $m_{\rm H} = \sqrt{A/16\pi} = M$. In flat space, $M = 0$ gives $\kappa = -1/r_0$ and $m_{\rm H} = 0$.
   - **Must contain:** Both principal curvatures are minus the square root of one minus 2M over r zero, divided by r zero; The integral of the squared sum is 16 pi times one minus 2M over r zero; The Hawking mass is M at every radius; It is zero for a round sphere in flat space

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Mean curvature: average or sum | $H = \tfrac12(\kappa_1 + \kappa_2) = \tfrac12K^\mu{}_\mu$ for a surface, and $\tfrac1n\,\mathrm{tr}\,S$ in dimension $n$. | Many relativity texts and analysis papers call the trace $\kappa_1 + \kappa_2$ the mean curvature and write it $H$ or $K$, so inequalities such as Willmore's differ by a factor of $4$. |
| Sign and order of the principal curvatures | $\kappa_1 \ge \kappa_2$ are the eigenvalues of $K^\mu{}_\nu$, with $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$ positive toward the chosen normal; a sphere of radius $a$ with the outward normal has $\kappa_1 = \kappa_2 = -1/a$. | Some texts give the second fundamental form the opposite sign, so a sphere has $+1/a$ with the outward normal. The product $\kappa_1\kappa_2$ and the principal directions agree in every convention. |

## Visuals

- ★ [[card-touching-a-curved-patch]] (flagship): The entry picture made measurable: a ruler turning about a touching point, the bending in each direction, and the principal directions a quarter turn apart. *Sketch:* Adds a turning mode to the second-fundamental-form sketch. On an egg, a spoon bowl, a can, a saddle or a crisp turned by $45^\circ$, a ruler pivots about the touching point (on the saddle and the crisp, where no ruler can rest on one side, a line drawn in the tangent plane pivots instead) while a polar plot traces $\kappa_n(\phi)$, with its maximum and minimum marked on the patch. A thin-slice slider cuts the patch parallel to the card: the outline is an ellipse on the egg and a hyperbola on the saddle, with axes along the principal directions. A flip-normal button negates every $\kappa$. It proves that the extremes are a quarter turn apart and that Euler's formula fills in the rest.
- [[plumb-lines-along-a-walk]] (supporting): Earth's two principal radii read as plumb-line tilt per kilometre, with umbilic poles. *Sketch:* On the flattened-ellipsoid preset scaled to Earth, readouts give kilometres per degree of tilt along the meridian and across it: 110.6 and 111.3 at the equator, both 111.7 at the poles. A heading dial follows Euler's formula between them, and the sideways lean vanishes only along the two principal directions.
- [[lines-of-curvature-on-an-ellipsoid]] (core): Principal line fields, their umbilics, and the index sum on closed surfaces. *Sketch:* A triaxial ellipsoid with both families of lines of curvature, meeting at four umbilics labelled $+\tfrac12$, and a counter showing their sum, 2. Sliders morph it to a spheroid, where the umbilics merge in pairs at the poles, and to a torus of revolution, with none and a counter of 0. A bump preset adds $\tfrac16(x^3 - 3xy^2)$ to a round cap and shows a star umbilic, around which the line field turns half a turn backwards. It proves that umbilics are forced by topology, not special to spheres.

## Tutor moves

**Open with**

- Picture a ruler lying on a hen's egg at its widest part, touching the shell at one point. If the shell bends most sharply when the ruler lies around the egg, in which direction do you predict it bends least sharply? *(prediction)*

**If the learner is stuck**

- *The learner cannot decide which principal curvature is the larger on a saddle.* → Fix which side counts as positive first, then compare signed values; the sign of the product does not depend on that choice. *Uses:* `ways_in/a-saddle-bends-both-ways`, `checks/mountain-pass`
- *The learner's principal curvatures have units of length, or their directions are not perpendicular in space.* → Raise an index with $g^{\mu\nu}$ before taking eigenvalues, and work the helical-coordinates check. *Uses:* `checks/helical-lines-on-a-can`

**Common questions**

- *Why are the sharpest and gentlest directions a quarter turn apart?* (entry) Take the egg, and imagine slicing a very thin piece off its shell, parallel to the ruler and just under it. Where the shell bends gently, it drops away slowly, so the cut reaches further out in that direction. Close to the touching point, the cut edge is shaped like a stretched circle. It is longest in the direction of gentlest bending and shortest in the direction of sharpest bending. A stretched circle is longest along the stretch and shortest at right angles to it, a quarter turn away. On a saddle, the cut edge is a pair of curves bowing away from each other. They too are shaped the same on each side of two lines a quarter turn apart. This holds at every point of a smooth surface where the directions do not all bend alike. *Uses:* `ways_in/turn-a-ruler-on-an-egg`, `ways_in/extremes-are-eigenvalues`
- *With signs, which principal curvature of an egg is the largest?* (entry) Picture an egg lying on a table, and look at the top of its shell. There the shell bends down in every direction, like a hill, so both principal curvatures are negative. A sharper bend gives a bigger number before the minus sign, so the sharper bend has the more negative value. The sharpest bending is then the smallest value, and the gentlest bending is the largest. *Uses:* `ways_in/a-saddle-bends-both-ways`, `ways_in/turn-a-ruler-on-an-egg`
- *Does the ground under my feet have principal curvatures?* (entry) Yes. Picture sea level as smooth ground. Even a walk that never steers turns, seen from far away, outside Earth, because the ground bends away beneath each step. The walk turns more quickly where the ground bends more sharply ahead. At the equator, such a walk turns by 1 degree every 110.6 kilometres heading toward a pole, but every 111.3 kilometres along the equator, a quarter turn away. Fewer kilometres for each degree means sharper bending. The reason is that Earth is slightly squashed. Seen from far out in space, directly out from the equator, Earth's outline is an oval through both poles. So a walk from the equator toward a pole follows an oval of that same shape. Now draw a circle around the oval, with the same centre and as wide as the equator. The oval fits inside that circle and touches it at the two ends of its longest width. A curve that stays inside a circle and touches it cannot cross to the outside, so the curve must bend more sharply than the circle there. Those ends lie on the equator, and a walk along the equator bends like that circle. The two numbers differ by less than 1 part in 100, so nobody notices. *Uses:* `ways_in/turn-a-ruler-on-an-egg`, `ways_in/earths-two-bendings-surveyed`, `observations/earth-ellipsoid-radii`
- *Why does this matter for gravity?* (entry) General relativity describes gravity as the curving of space and time, and it studies surfaces inside curved space. Picture an idealized black hole that does not spin and never changes. Take a snapshot of the space around it, at one moment by the clocks of people far away. Near the black hole, that space is shaped a little like the waist of an hourglass. The black hole's edge is the narrowest sphere, where both principal curvatures drop to zero, just as a walker around the narrowest ring of an hourglass never has to steer. Bending can also weigh what a sphere encloses. In empty, flat space, a perfectly round sphere's bending is fixed by its area. Around a round mass at rest, a round sphere centred on it bends less than a sphere of the same area in flat space, and the shortfall tells you the mass inside. *Uses:* `ways_in/slices-horizons-and-mass`, `checks/hawking-mass-of-schwarzschild-spheres`

**Switching levels**

- To working when: asks how to compute the two bendings; mentions matrices or eigenvalues. Go to the eigenvalue problem and the helical-coordinates check. *Uses:* `ways_in/extremes-are-eigenvalues`, `checks/helical-lines-on-a-can`
- To formal when: asks whether the directions are always defined; asks about closed surfaces or topology. Open the shape operator, the star umbilic and the index sum. *Uses:* `ways_in/shape-operator-and-umbilics`, `problems/star-umbilic`
- To research when: asks about black-hole horizons, quasi-local mass or singularities. Open slices, minimal surfaces and the Hawking mass. *Uses:* `ways_in/slices-horizons-and-mass`, `research_horizon/penrose-inequality`

**Pronunciations:** Euler → OY-ler; Meusnier → muh-NYAY; Dupin → dew-PAN; Rodrigues → roh-DREE-gez; umbilic → um-BIL-ik; catenoid → KAT-uh-noyd; Poincaré → pwan-kah-RAY; Khalatnikov → khah-LAHT-nee-kov; Huisken → HOYS-ken

**Voice notes:** Say "kappa one" and "kappa two". At entry, say "the sharpest and gentlest bending" before the name, and "a quarter turn" rather than "perpendicular".

## History

- **Leonhard Euler (1767).** Showed that the curvatures of the normal slices at a point take a largest and a smallest value in perpendicular directions, and expressed all the others through them. Leonhard Euler (1767), *Recherches sur la courbure des surfaces*, Mémoires de l'académie des sciences de Berlin 16, 119–143
- **Jean Baptiste Meusnier (1776).** Showed that the catenoid and the helicoid satisfy Lagrange's equation for surfaces of least area, and that on such surfaces the two principal radii at each point are equal and opposite. Presented in 1776, published in 1785. Jean Baptiste Meusnier (1785), *Mémoire sur la courbure des surfaces*, Mémoires de mathématique et de physique présentés à l'Académie royale des sciences, par divers savans 10, 477–510
- **Charles Dupin (1813).** Introduced the indicatrix, the conic whose axes lie along the principal directions, and proved that the surfaces of a triply orthogonal family meet along lines of curvature. Charles Dupin (1813), *Développements de géométrie*, Courcier, Paris
- **Olinde Rodrigues (1815).** Showed that along a line of curvature the normal changes along the direction of travel at the rate of the principal curvature.
- **Carl Friedrich Gauss (1827).** Showed that the curvature defined by the spreading of normals equals the product of the principal curvatures, and that this product survives bending without stretching. Carl Friedrich Gauss (1828), *Disquisitiones generales circa superficies curvas*, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6, 99–146

## Research horizon

- **Quasi-local mass and the Penrose inequality.** The Hawking mass uses only the area of a closed surface and the squared sum of its principal curvatures. Its monotonicity under inverse mean curvature flow proved the Riemannian Penrose inequality for a connected horizon, and a conformal flow proved it for horizons with several components. The inequality for general initial data remains open. Stephen W. Hawking (1968), *Gravitational radiation in an expanding universe*, Journal of Mathematical Physics 9, 598–604, doi:10.1063/1.1664615; Gerhard Huisken, Tom Ilmanen (2001), *The inverse mean curvature flow and the Riemannian Penrose inequality*, Journal of Differential Geometry 59, 353–437, doi:10.4310/jdg/1090349447; Hubert L. Bray (2001), *Proof of the Riemannian Penrose inequality using the positive mass theorem*, Journal of Differential Geometry 59, 177–267, doi:10.4310/jdg/1090349428; Marc Mars (2009), *Present status of the Penrose inequality*, Classical and Quantum Gravity 26, 193001, doi:10.1088/0264-9381/26/19/193001
- **Anisotropic approach to spacelike singularities.** Near a generic spacelike singularity in vacuum, the principal curvatures of slices are expected to behave locally like those of a Kasner solution, with the exponents jumping between Kasner epochs. Controlling this oscillatory regime mathematically, and deciding when it gives way to steady Kasner-like behaviour, is active research. Edward Kasner (1921), *Geometrical theorems on Einstein's cosmological equations*, American Journal of Mathematics 43, 217–221, doi:10.2307/2370192; V. A. Belinskii, I. M. Khalatnikov, E. M. Lifshitz (1970), *Oscillatory approach to a singular point in the relativistic cosmology*, Advances in Physics 19, 525–573, doi:10.1080/00018737000101171
- **Willmore energy.** The integral of the squared mean curvature over a closed surface is unchanged by inversions in spheres centred off the surface, and it is smallest for round spheres. Marques and Neves proved Willmore's conjecture that every torus has at least $2\pi^2$, with $H = \tfrac12(\kappa_1 + \kappa_2)$; the same integral enters the Hawking mass. T. J. Willmore (1965), *Note on embedded surfaces*, Analele Ştiinţifice ale Universităţii Al. I. Cuza din Iaşi, Secţiunea I a Matematică 11B, 493–496; Fernando C. Marques, André Neves (2014), *Min-max theory and the Willmore conjecture*, Annals of Mathematics 179, 683–782, doi:10.4007/annals.2014.179.2.6

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** If you put a ruler on an egg and turn it, the gap under it is bigger going around the egg than along it, so the egg bends more around it. The most and least bending are the principal curvatures, and they are a quarter turn apart, except on a ball. I didn't get why the gap tells you the bending, since that was only in the reminder box, or why it has to be exactly a quarter turn on every surface. Earth does it too, something about 110.6 and 111.3 kilometres, but I couldn't tell which one was sharper or why flattening makes a difference. A saddle bends up one way and down the other, so one is positive and one negative. But if the egg bends down everywhere, aren't both of the egg's negative? Then is the largest one the gentle one? And on the crisp, 'the path dips, so it bends up' confused me.

Second entry read, of revision 5, before fixes: A ruler laid on an egg leaves a gap, and the faster the gap grows the more sharply the shell bends that way. Around the egg the gap is about a centimetre and a quarter two centimetres out; along the egg it is about 6 millimetres. So the shell bends most sharply around and least sharply along, and those two directions are a quarter turn apart. Those two bendings are the principal curvatures. On a saddle the seat bends up one way and down the other, so one is positive and one negative, and they are still a quarter turn apart. Two sentences stopped me. 'On a saddle like this, whose left and right halves are mirror images' - left and right seen by whom, the rider or someone facing the horse? Then 'The one along the horse is positive' - the one what? The sentence before it is about directions, and a direction cannot be positive. I also tried the spoon test, and the ruler kept catching on the handle exactly when I turned it to lie along the spoon, which is the direction the test cares about. In the Earth answer I read 'A walk that never steers still turns' twice before I saw that 'still' meant 'even so' and not 'standing still'. And I took on trust that an oval fitting inside a circle and touching it must bend more sharply there.

**Stumbles (17)**

- “Turn a ruler that touches a smooth surface at one point, and on most surfaces the bending changes with the ruler's direction.”: The summary opens with a rule, not a scene. 'Turn' does not say around what point, and 'the bending' does not say of what.
- “Unless every direction bends alike, as on a ball, they lie in directions a quarter turn apart.”: 'They' are numbers, and numbers do not lie in directions.
- “Rest a ruler on a surface so that it touches at one point. The more quickly the gap under the ruler grows away from that point, the more sharply the surface bends in the ruler's direction.”: The gap test, which the whole egg picture depends on, appears only in the recap. The recap is hidden for a reader arriving from normal curvature, and that note never meets a ruler, so the explanation's 'So the shell bends most sharply around the egg' has no stated reason.
- “Lay a ruler on a hen's egg at its widest part, so that it touches the shell at one point. Keep that point still and turn the ruler slowly around it.”: Not doable as written: an egg rolls, and it is unclear where the ruler rests.
- “It is biggest, just over 1 centimetre, when the ruler lies around the egg. It is smallest, about half a centimetre,”: The numbers are loose. A typical egg 4.4 centimetres wide gives 1.28 centimetres around it, and 0.61 to 0.63 centimetres along it.
- “So the shell bends most sharply around the egg and least sharply along it.”: Step left implicit: the takeaway is 'a quarter turn apart', but the way never says that around and along are a quarter turn apart.
- “The same is true at every point of such a smooth surface, unless all directions bend alike, as on a ball.”: A surprising general claim with no test nearby. The spoon try-it exists, but the explanation does not point to it.
- “Earth's ground has principal curvatures too, and they differ because Earth is slightly flattened. At the equator, a walk that never steers turns by 1 degree every 110.6 kilometres heading toward a pole, but every 111.3 kilometres along the equator.”: Rule 17: this paragraph adds a second measure of bending, turning per kilometre, to a way about gaps under a ruler. It also skips the link between fewer kilometres per degree and sharper bending. And 'flattened' leaves the teenager's first what-if unanswered: if Earth is flattened at the poles, why is the bending toward a pole the sharper one?
- “Along the horse's back, the seat curves up toward the front and the back. Across the horse, it curves down over the horse's sides. So at one point, the seat bends up in one direction and down in another.”: Two words for one idea, 'curves' and 'bends'. 'Bends up' is never defined, and a reader could take it to mean the seat is raised.
- “To compare, count upward bending as positive and downward bending as negative. The principal curvatures are then the largest and the smallest of these values, on a saddle and on an egg alike.”: The first what-if fails. At the top of an egg on a table both values are negative, so the 'largest' is the gentlest bending, which contradicts 'sharpest and gentlest' in 'Turn a ruler on an egg'. Nothing says how size and sign combine.
- “On the saddle, the one along the horse is positive and the one across it is negative. Their directions are still a quarter turn apart.”: An ambiguous 'the one'. Also, no reason is given for the directions being along and across the horse.
- “Slide a fingertip across its middle from one raised edge to the other: the path dips, so it bends up.”: Reread: 'dips, so it bends up' sounds contradictory. 'Edge' also appears twice with no picture of which edges are raised.
- “A road crosses a mountain pass, which is shaped the same on both sides of the road. ... in which directions do they lie?”: The check is not prepared by the entry ways. Its answer uses a mirror-symmetry rule for where principal directions lie that no entry way teaches, and 'ahead and behind' has no named traveller.
- “Imagine slicing a very thin piece off its shell, level with the ruler. Close to the touching point, the cut edge is shaped like a stretched circle, longest where the shell bends most gently.”: Two steps are left implicit. Why does gentle bending make the cut longer in that direction? And 'on a saddle the rule behind it is the same' names no rule. 'Level with' is also ambiguous.
- “The sphere where both bendings drop to zero is the black hole's edge. How much round surfaces bend also gives a way to weigh what they enclose.”: 'Bendings' is a new synonym for principal curvatures. Two surprising claims have no reason: a sphere with zero bending, and weighing by bending.
- “Rest a ruler on a surface so that it touches at one point. ... On Earth, a walk that never steers left or right turns by about 1 degree every 111 kilometres. That turn comes from the ground bending.”: The egg recap restated a rule the explanation should carry, plus an Earth fact the way no longer uses.
- “Unless every direction bends alike, they lie a quarter turn apart.”: The takeaway says the principal curvatures, which are amounts of bending, 'lie' somewhere. It is their directions that are a quarter turn apart, the same slip as in the summary.

**Fixes**

- Summary: now opens with the egg scene in three short sentences, and the principal curvatures' directions, not the numbers, are said to be a quarter turn apart.
- Egg way: the gap test moved from the recap into the explanation, with the tennis-ball-versus-basketball reason. The towel makes the setup doable. Gap numbers were recomputed with python for an egg 4.4 centimetres wide and about 5.7 to 5.8 centimetres long (1.28 cm around, 0.61 to 0.63 cm along). The way now says around and along are a quarter turn apart and points to the spoon test. The recap is null because the way uses nothing from elsewhere.
- Rule 17: Earth's two bendings left the egg way and became the entry common question 'earths-two-bendings'. It adds the step that fewer kilometres per degree means sharper bending, and the squashed-oval reason (an ellipse bends most sharply at the ends of its long axis, on the equator). GRS80 values were rechecked: 110.574 and 111.319 km per degree, a 0.67 per cent difference. The teaching arc's first step uses it.
- Saddle way: 'curves' was replaced by 'rises' and 'drops'. Bends up and bends down are defined (valley and hill) in their own paragraph and added to the glossary. The way adds that a sharper bend gets a bigger number before its sign, and scopes the along-and-across directions to a saddle whose halves are mirror images.
- The signed egg case moved to a new entry common question, 'egg-with-signs', so the explanation stays within budget. The crisp try-it now says which sides the crisp rests on, and uses valley and hill instead of 'dips, so it bends up'. The saddle recap uses shorter sentences.
- Mountain-pass check: the question now gives the principal directions, because no entry way teaches the symmetry rule that the old answer relied on. The answer is a valley-and-hill because-chain, and the key points were rewritten to match. The objective explain-opposite-signs is unchanged.
- Common questions: the quarter-turn answer now spells out why gentle bending makes the slice longer, and gives the saddle case as mirror lines. The gravity answer uses the hourglass waist, a geodesic ring, for the horizon sphere of the time-symmetric Schwarzschild slice. It explains weighing by comparing the bending of a sphere of the same area with flat space, which matches the research way's formula sqrt(1 - 2M/r)/r against 1/r.
- Ladder: the working way 'earths-two-bendings-surveyed' now opens by referring to the egg in 'Turn a ruler on an egg' instead of a walk that the egg way no longer contains. It also explains Weingarten's equation in one line, d n-hat/ds = -K^lambda_mu t^mu d_lambda X, derived from differentiating n-hat . d_nu X = 0 (sign checked against K_mu nu = n-hat . d_mu d_nu X), instead of naming it before the formal rung defines it. It names GRS80 as the geodetic reference ellipsoid.
- Budget: entry explanations were 582 words after the first rewrite. To fit the 440 review allowance, the Earth paragraph and the signed-egg paragraph moved into entry common questions rather than being compressed, and the sentence 'A ruler could not rest on that middle point from one side of the seat in every direction' was dropped. Entry explanations now total 402 words.
- Bumped the revision to 2 and set status novice-reviewed.

**Concerns**

- The entry explanations remain above the 80% draft share and within the review allowance. The advanced entry cap of 400 is tight for two ideas that each need a new test (the gap test, and signed bending). Any further entry addition needs a cut, or a third entry way with the cap reconsidered.
- The mountain-pass check no longer asks for the directions. If authors want the entry reader to reason from mirror symmetry, the saddle way needs a sentence explaining why a mirror-symmetric point has its principal directions along and across the mirror line, and that sentence costs budget.
- The physics reviewer should confirm four new entry claims: the egg gap numbers for a typical egg; the oval reason for sharper meridian bending at the equator; the hourglass-waist picture of the horizon sphere (time-symmetric slice only); and 'a sphere of the same area bends less' around a mass.
- The working way extremes-are-eigenvalues writes the second fundamental form as K_mu nu, and the conventions use K for Gaussian and sectional curvature. The note writes Gaussian curvature as kappa1 kappa2, but the conventions file should scope the K symbol. The writer also reported that the mean-curvature normalization and shape-operator sign rows are missing.
- The first entry way has no Earth number and no answer to 'why don't I notice' in its own text. Its everyday numbers are the gap sizes on an egg, and the Earth comparison lives in the entry common question 'earths-two-bendings'. If a book editor wants Earth inside the way, the entry cap must grow or the saddle way must shrink.
- The proposed visual card-touching-a-curved-patch shows a 'ruler turning' on a saddle, but a ruler cannot physically rest on a saddle point from one side. Its sketch should say that on a saddle the line through the touching point is drawn, not rested.
- Second novice review: the try-it in 'Turn a ruler on an egg' now uses a tin can instead of a spoon's back, so the physics diff check should confirm the new claims - a right circular cylinder bends most sharply around it and not at all along it, the two directions are a quarter turn apart, and the can stays on one side of the ruler, so it is 'a surface like that' in the way's sense.
- Second novice review: entry explanations now stand at about 425 words against the advanced entry cap of 400, inside the 440 review allowance but with almost no room left. Any further entry sentence needs an entry sentence dropped.
- Second novice review: book readers meet only the ways and the glossary, not the tutor's common questions. So the tension between 'the sharpest and the gentlest bending' in 'Turn a ruler on an egg' and 'the largest and the smallest of these signed values' in 'A saddle bends both ways' is resolved only for the tutor, in 'egg-with-signs'. If the book ships the ways alone, the saddle way needs one sentence for the all-negative case, and that costs entry budget the way does not have.
- Second novice review: the entry rung never connects the word 'bending' used here to 'normal curvature', the entry prerequisite the reader arrives from, which teaches bending by walking and turning rather than by gaps under a ruler. The only bridge is the tutor's common question 'earths-two-bendings'. A one-line recap in the egg way would join them, at the cost of the way's self-sufficiency and of entry budget.
- Second novice review: the conventions file still has no row for the sign of the second fundamental form or the extrinsic curvature of a slice, and none for whether mean curvature means the average or the trace. Both notation traps in this note therefore state choices the file does not record. Reported, not invented, as the first review also reported.

**Re-read** (2026-09-13, revision 4): 7 stumbles in 8 changed passages

- “Where a surface is level, say that a line on it bends up at a point”: 'Level' makes the reader picture a flat floor, and then a line on it cannot bend. The reader rereads to see that 'level' means level at one point of a curved surface.
- “So at the middle of the seat, the seat bends up along the horse and down across it.”: The up-or-down rule now applies only where a surface is level, but the way never says the middle of the seat is level. The step is taken on trust.
- “There, the directions of the principal curvatures are along the road and across it.”: The check relies on the up-or-down rule, which holds only where the ground is level, and does not say the ground at the pass is level.
- “its outline is an oval, and the equator itself is a circle as wide as that oval. The oval fits inside that circle”: Seen from beside the equator, the equator is edge-on, a line across the oval, so the equator cannot hold the oval inside it. The reader also is not told why the oval's bending is the bending heading toward a pole, or which bending the circle stands for.
- “a round sphere centred on it with the same area bends less”: 'The same area' as what? The comparison sphere sits in the previous sentence, so the reader rereads.
- “at one moment by the clocks of people far away”: The reader is not told why a snapshot of space needs clocks far away; how distant clocks set 'one moment' is a second new idea taken on trust. Explaining it needs a new claim, so it is left for a physics decision.
- “The egg in 'Turn a ruler on an egg' bent by different amounts around it and along it. Sea level on Earth does too, on a far larger scale but the other way round”: 'The other way round' has nothing to be the other way round from, because the first sentence no longer says which direction of the egg bends more sharply.
- Fix: Applied the rewrites for stumbles 1-5 and 7 without changing any claim; the egg's sharper-around bending at its widest part restates the entry way 'Turn a ruler on an egg'.
- Fix: Stumble 6 is not applied, because it would add a claim; it is reported for the physics diff check.
- Fix: Bumped revision 3 to 4. Entry explanations rise from 409 to 414 words, within the 440 review allowance; nothing dropped.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 6): 12 stumbles in 12 changed passages

- “On a saddle like this, whose left and right halves are mirror images, the directions of the principal curvatures are along the horse and across it.”: A direction with no reference (rule 6): whose left? The rider's left and a bystander's left are opposite, and a reader facing the horse's head sees them swapped again.
- “The one along the horse is positive, and the one across it is negative.”: Ambiguous 'the one' (rule 11), and a category error. The only plural noun in the sentence before is 'the directions of the principal curvatures', and a direction is neither positive nor negative. This is a regression: the first novice review's rewrite said 'the principal curvatures lie along the horse and across it', so 'the one' had a noun; the physics review then corrected 'lie along' to 'the directions of ... are along', which left 'the one' stranded.
- “Lay a ruler on the back of a large spoon, touching it at one point in the middle of the bowl. Turn the ruler around that point. ... It grows least quickly when the ruler lies along the spoon, a quarter turn away.”: Not doable as written (rule 8). A spoon laid face down rests on the back of its bowl with the handle raised clear of the table, and the raised handle stands higher than the top of the bowl. A ruler turned to lie along the spoon therefore rests on the handle instead of touching the bowl at one point, and that is exactly the direction the try-it asks the reader to look at. 'touching it' is also an ambiguous pronoun.
- “A walk that never steers still turns, because the ground bends away beneath each step, and it turns more quickly where the ground bends more sharply ahead of it.”: A reread, and a word doing double duty (rule 5): 'never steers still turns' reads first as 'stands still', because 'still' sits next to a verb of motion. The sentence also gives the turning no reference: turns as seen by whom, from where? The prerequisite is careful to say 'seen from far away, outside the ball', and this answer drops that. Two 'it's in the tail add to the load.
- “The oval fits inside that circle and touches it at the two ends of its longest width, so there the oval bends more sharply than the circle.”: A step left implicit (rule 3) behind a 'so'. Nothing says why fitting inside and touching forces sharper bending, and this is the one step that carries the whole squashed-Earth answer.
- “A horse's riding seat, which curves up toward the front and back and down over the horse's sides.”: Two words for one idea (rule 5). The saddle way was rewritten to say 'rises' and 'drops' precisely so that 'curves' would not compete with 'bends', but the glossary entry still says 'curves'.
- “On a saddle, the cut edge is a pair of curves bowing away from each other, and they too have two mirror lines a quarter turn apart.”: 'Mirror lines' is an undefined term at this point, and it is the only place in the entry rung that names symmetry. The saddle way's own phrase for the same idea is 'shaped the same on both sides'.
- “A sharper bend gives a bigger number before the minus sign, so it is the more negative value.”: Ambiguous 'it' (rule 11): the candidates in the sentence are the bend, the number and the minus sign.
- “Lay a ruler on top, across the egg's widest part, so that the ruler touches the shell at one point.”: 'Across' reads as an instruction about which way the ruler points, which the next sentence then tells the reader to change; and 'the egg's widest part' can be read as the egg's fat end rather than the circle where it is widest. The gap numbers are computed on that widest circle, so the ambiguity changes the answer.
- “On a typical egg, look at the gap 2 centimetres from the touching point.”: A measurement without its measurer (rule 7): 2 centimetres measured along the ruler, or around the shell? The two differ, and the quoted gap of about 1 and a quarter centimetres is the one measured along the ruler.
- “That is why a tennis ball leaves a bigger gap under a ruler than a basketball does.”: The comparison has no fixed distance, so a reader can picture the two gaps measured at different places and the reason stops working. It is the sentence that backs the surprise (rule 9), so it has to be airtight.
- “Seen from far out in space, beside the equator, Earth's outline is an oval through both poles.”: 'Beside the equator' reads as 'close to the equator', which fights 'far out in space' in the same sentence.
- Fix: Saddle way: 'whose left and right halves are mirror images' became 'which is shaped the same on both sides of the horse', which names the mirror without a left or a right; and 'The one along the horse' became 'The principal curvature along the horse', restoring the noun the physics fix had removed. The claim is unchanged.
- Fix: Entry way 'Turn a ruler on an egg': the try-it moved from the back of a spoon to a tin can on its side, because a face-down spoon's raised handle blocks the ruler in the along direction. The can keeps the quarter turn and adds a direction with no gap at all, which is easier to see than a slowly growing gap. The way's closing pointer became 'You can test this on a tin can.'
- Fix: Entry way 'Turn a ruler on an egg': the setup now names the touching point ('at one point on the widest circle around the egg') instead of 'across the egg's widest part'; the gap is measured '2 centimetres along the ruler'; and the tennis-ball comparison is now 'at the same distance from the touching point'. No number changed: the widest circle of a 4.4 cm egg gives 1.283 cm at 2 cm out, the profile gives 0.607 to 0.633 cm, and at 2 cm out a tennis ball gives 0.66 cm against a basketball's 0.17 cm.
- Fix: Common question 'earths-two-bendings': 'A walk that never steers still turns' became 'Even a walk that never steers turns, seen from far away, outside Earth', which removes the garden path and restores the viewpoint the prerequisite uses; the tail became its own sentence with a named subject. The missing reason for the circle step was added: a curve that stays inside a circle and touches it cannot cross to the outside, so it bends more sharply there. 'Beside the equator' became 'directly out from the equator'.
- Fix: Common question 'why-always-a-quarter-turn': 'two mirror lines' became 'shaped the same on each side of two lines', matching the saddle way's phrase. Common question 'egg-with-signs': the ambiguous 'it' became 'the sharper bend'.
- Fix: Glossary 'saddle': 'curves up ... and down' became 'rises ... and drops', matching the saddle way.
- Fix: Budget: entry explanations rose from 415 to about 425 words, inside the 440 review allowance for the advanced entry cap of 400; tutoring rose by about 28 words to about 3300 against a cap of 3500; other way fields rose by about 8. Nothing was dropped or compressed.
- Fix: Bumped revision 5 to 6 and set status novice-reviewed, so that the physics stage diff-checks the changed text; review.physics was not touched.
- Fix: Cleared two validator warnings raised by these rewrites: the saddle sentence in 'why-always-a-quarter-turn' was split into two so that no sentence runs past 32 words, and the circle reason in 'earths-two-bendings' avoids the wording trap 'from the inside' by saying 'stays inside a circle and touches it', with 'the curve' repeated so that the two 'it's do not point at different things.

**Re-read** (2026-09-13, revision 8): 3 stumbles in 4 changed passages

- “An egg's shell at its widest part, for example, bends more sharply around the egg than along it.”: 'Its widest part' reads as the egg's fat end, the rounder of its two ends, rather than the circle where the egg is widest. An earlier reading caught the same phrase in the entry way and replaced it with 'the widest circle around the egg'. Read as the fat end, the sentence points the reader at the wrong place, and near the tip the shell bends almost alike in every direction.
- “it is the largest and smallest signed bending whose directions are a quarter turn apart”: 'Signed bending' is a term the reader has never met, and the tutor says this out loud. The note everywhere else says that bending toward one side counts as positive and toward the other as negative, and asks 'with signs, which principal curvature is the largest'. Two words for one idea, and the newer one sounds like mathematics. The compression comes from the two-sentence limit on a correction: the sentence has to carry the saddle case and the sign rule at once.
- “The gap stops growing when the ruler lies along the can, a quarter turn away, because the can does not bend in that direction.”: 'Stops growing' says the gap grew first and then stopped, so the reader looks for the distance along the ruler where the growing stops. Along the can the gap never grows at all. The reader with a can in hand finds nothing to see and rereads.
- Fix: Applied all three rewrites. No claim, number, condition, sign or scope changed: the summary still scopes the egg to where the entry way puts the ruler, and 'widest circle' is the entry way's own phrase for that place; the correction still gives the convex case and the signed rule; and 'does not grow at all' is the same statement as 'stops growing' for an ideal cylinder and for a seamed tin, whose rims hold the ruler a constant sliver clear of the body.
- Fix: Budget: +3 words in tutoring (the correction) and +3 in the other-way-fields bucket (the try-it); the summary is unchanged in length. Nothing was compressed or dropped, and every part stays inside its cap or its review allowance.
- Fix: Not fixed, reported instead: the correction still asks a learner to take in the convex case and the signed rule in one spoken turn (rule 17). Splitting it needs a third sentence or a new tutor move, which is a content change, so it is left for an editor.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Normal curvature kappa_n = K_{mu nu} t^mu t^nu with K_{mu nu} = n-hat . d_mu d_nu X, positive toward n-hat; sphere of radius a with outward normal has -1/a; can has 0 and -1/a.: Differentiated a unit-speed curve on the surface: n-hat . X'' = K_{mu nu} t^mu t^nu. For a sphere X'' points inward, so the value is -1/a with the outward normal. → Correct. The sign is consistent with S(X) = -nabla_X N, g(S X, Y) = II(X, Y) in the formal way and with the notation trap.
- Lagrange-multiplier derivation: K^mu_nu t^nu = kappa t^mu, each eigenvalue equals kappa_n in its direction, (kappa_1 - kappa_2) g t_1 t_2 = 0, Euler's formula, kappa_{1,2} = H +- sqrt(H^2 - det K^mu_nu).: Re-derived each of the eight steps by hand, including the characteristic polynomial kappa^2 - tr kappa + det. → Correct at every step.
- In an orthonormal basis H^2 - det = (K11 - K22)^2/4 + K12^2 >= 0; Euler's formula equals H + (kappa_1 - kappa_2)cos(2 phi)/2; perpendicular normal curvatures add to 2H; at a saddle kappa_n = 0 where tan^2 phi = -kappa_1/kappa_2.: Hand algebra. → Correct.
- Weingarten: d n-hat/ds = -K^lambda_mu t^mu d_lambda X, parallel to the path exactly when t is principal; Rodrigues' formula and its converse.: Differentiated n-hat . d_nu X = 0 to get d_mu n-hat . d_nu X = -K_{mu nu}, then raised the index with g^{nu lambda}. → Correct, and consistent in sign with the formal definition S(X) = -nabla-bar_X N.
- GRS80 radii: M = 6335.4 km, N = 6378.1 km at the equator (110.574 and 111.319 km per degree); 6367.4 and 6388.8 km at 45 degrees; 6399.6 km at the poles; radius 6356.7 km heading at 45 degrees at the equator; 1/(MN) from 2.442e-8 to 2.475e-8 km^-2.: python3 with a = 6378.137 km and f = 1/298.257222101, M = a(1-e^2)/(1-e^2 sin^2)^(3/2), N = a/(1-e^2 sin^2)^(1/2); Euler radius 2MN/(M+N). Checked M/N = (1-e^2)/(1-e^2 sin^2) < 1 away from the poles, and N as the normal to the axis via Meusnier (cos phi/(N cos phi)). → All values reproduce: 6335.439, 6378.137, 110.5743, 111.3195; 6367.38, 6388.84; 6399.594 (111.694 km per degree, matching the plumb-lines sketch's 111.7); 6356.72; 2.4417e-8 and 2.4747e-8. The difference is 0.674 per cent, under 1 part in 100.
- Working way opening: the egg 'does the same' as Earth.: Compared directions: on the egg (prolate) the around direction is sharper; at Earth's equator (oblate) the meridian, heading toward a pole, is sharper than the equator circle. → Wrong: the two bend the opposite way round. Fixed.
- Entry egg gap numbers: 2 cm from the touching point, about 1 and a quarter cm around and about 6 mm along, for an egg 4.4 cm wide and 5.7 to 5.8 cm long.: python3: around, the widest circle of radius 2.2 cm gives 2.2 - sqrt(2.2^2 - 2^2) = 1.283 cm; along, an ellipse profile with half-axes 2.2 and 2.85 to 2.9 cm gives 0.607 to 0.633 cm (profile radius of curvature 3.7 to 3.8 cm). → Correct to the stated roundings. The egg is modelled as symmetric; a real egg's asymmetry changes the along gap slightly, which 'about' and 'typical' cover.
- Tennis ball leaves a bigger gap under a ruler than a basketball, at the same distance from the touching point.: Gap r - sqrt(r^2 - x^2) decreases with radius r at fixed x. → Correct.
- Spoon try-it: gap grows fastest across the bowl and slowest along it.: The back of a spoon bowl is an elongated convex cap, narrower across than along, so its across section has the smaller radius. → Correct for a typical spoon.
- Entry sign rule and 'bends up' definition (valley or hill); crisp try-it; mountain-pass check answer; egg-with-signs common question.: Checked against kappa_n with an upward normal at a level point: height along a normal section is kappa_n s^2/2. Crisp (hyperbolic paraboloid resting on its low sides): raised-to-raised path is a valley (positive), low-to-low a hill (negative). Egg top on a table: both negative, and the sharper bend is more negative, so it is kappa_2. → Correct where the surface is level. At a tilted point a line along the slope rises on one side and drops on the other while still bending, so the definition gives no answer. Scoped to level points in the explanation and glossary. Every use in the note (saddle middle, pass top, egg top) is at a level point.
- Mirror symmetry of a saddle's left and right halves puts the principal directions along and across the horse.: A reflection fixing the point commutes with the shape operator, so it preserves the reflection's +1 and -1 eigenlines, which are then eigenvectors; one mirror suffices. → Correct. The phrase 'the principal curvatures lie along' (numbers placed in directions) was reworded in the saddle way and the mountain-pass check, matching the novice fix to the summary.
- Quarter-turn common question: a thin slice parallel to the tangent plane gives a stretched circle on the egg, longest along the gentlest bending, and a pair of curves bowing apart on a saddle, with mirror lines a quarter turn apart.: Dupin indicatrix: at depth h the cut reaches sqrt(2h/kappa_n(phi)) in direction phi, an ellipse with axes along the principal directions; on a saddle, a hyperbola. → Correct.
- Earth common question: fewer km per degree means sharper bending; the oval reason.: Meridian ellipse with half-axes a > b: radius b^2/a = 6335.4 km at the ends of the long axis, against radius a = 6378.1 km for the equator circle. The old sentence said only that an oval bends most sharply at those ends. That compares the meridian with itself, not with the equator. → The numbers and step are correct, but the reason had a gap. The ellipse lies inside the circle of radius a and touches it at those ends, so it bends more sharply there. That sentence was added.
- Gravity common question: space near a black hole shaped like an hourglass waist; the edge is the narrowest sphere with both principal curvatures zero; a waist ring needs no steering; around a mass a sphere of the same area bends less.: Time-symmetric Schwarzschild slice dr^2/(1-2M/r) + r^2 dOmega^2: the r = const spheres have principal curvatures of size sqrt(1-2M/r)/r, zero at r = 2M, the minimal throat of the Einstein-Rosen bridge. The hourglass waist ring is a geodesic by mirror symmetry. A sphere of area 4 pi r^2 bends by sqrt(1-2M/r)/r < 1/r, and M = (r/2)(1 - r^2 kappa^2). → Correct only for the eternal static black hole on the static slice. A black hole formed by collapse has no hourglass throat, and 'at one moment' needed a clock. The mass statement holds for round spheres around a round mass at rest (time-symmetric data), not in general. Scoped in equally simple words.
- Satellite dish: 0.50 m^-1 at the vertex; at the rim 0.315 m^-1 (radius 3.17 m) along the profile and 0.429 m^-1 (radius 2.33 m) around; only the vertex is umbilic.: python3 with z' = 0.6: 0.5/1.36^1.5 = 0.31525, 0.6/(1.2 sqrt 1.36) = 0.42875, radii 3.172 and 2.332. Meusnier's cosine z'/sqrt(1+z'^2) checked against the inward normal (-z' r-hat + z-hat)/sqrt(1+z'^2). → Correct; numeric tolerances of 1 per cent contain the values.
- Helical can check: g_uu = 25 cm^2, g_uv = 4 cm, g_vv = 1, det 9 cm^2; K^u_u = -1/3 cm^-1, K^v_u = 4/3; eigenvectors e_u - 4e_v (around) and e_v (along); e_u at 53.1 degrees with kappa_n = -0.12 cm^-1, radius 8.33 cm.: Hand computation of the inverse metric (1/9)[[1,-4],[-4,25]] and mixed tensor; python3 for atan(4/3) = 53.13 degrees, -(1/3)cos^2 = -0.12, 25/3 = 8.333. → Correct, including units.
- Soap-film check: catenoid neck c = 3 cm, principal curvatures -1/3 (around) and +1/3 (profile) cm^-1 with the normal away from the axis, product -1/9 cm^-2, zero normal curvature at 45 degrees.: r'' = 1/c at the neck; tan^2 phi = -kappa_1/kappa_2 = 1. → Correct.
- Soap-film observation: Young-Laplace jump gamma(kappa_1 + kappa_2), higher on the side the surface bends toward; a film holds twice that; bubble of 1.0 cm with gamma 0.025 N/m holds 10 Pa.: Laplace pressure 2 gamma H per surface; python3 4(0.025)/0.01 = 10.0 Pa. → The physics and number are correct. The heading 'form saddle-shaped surfaces' failed for a flat film in a flat wire ring (both curvatures zero), so it was scoped to 'saddle-shaped wherever they are not flat'.
- Star umbilic: K^mu_nu = delta + [[x,-y],[-y,-x]] + O(r^2), kappa_{1,2} = 1 +- r, kappa_1 direction at -theta/2, index -1/2.: Hand derivation of the Hessian and eigenvector (cos theta/2, -sin theta/2); python3 full shape operator with exact metric and normal at r = 0.001, tracking the kappa_1 line field over 3600 steps. → Numerical index -0.5000 and kappa_1 - kappa_2 = 0.0019990 against 2r = 0.002. Correct.
- No-umbilic-free egg: a line field with no singularities on a sphere contradicts index sum chi = 2; torus principal curvatures -1/a and -cos v/(b + a cos v) coincide only if b = 0.: Continuity of simple eigenvectors of a continuous symmetric field; Poincare-Hopf for line fields; torus algebra. → Correct.
- Timelike surface y = tx/L: II_tx = 1/L, S = [[0,-1/L],[1/L,0]], kappa = +-i/L.: Hand computation of g^{-1} II with g = diag(-1,1); python3 discriminant tr^2/4 - det = -1/L^2. → Correct. 'Only when g is positive definite' is right for hypersurfaces of a Lorentzian spacetime, whose induced metrics are never negative definite in dimension 2 or more.
- Formal results: regularity C^{k-2}; min-max characterization; umbilic surfaces of class C^3 lie in planes or spheres; index in half-integers; triaxial ellipsoid four umbilics of index +1/2; Hopf's theorem on immersed CMC spheres; sign reversal with N; timelike non-diagonalizability.: Checked against standard results: kappa_k = max over k-dimensional V of min of II; S has one derivative fewer than N; index sum 4 x 1/2 = 2; Hopf differential argument. → Correct with the hypotheses stated.
- Hawking mass check: II_thetatheta = -r_0 sqrt(1-2M/r_0), kappa = -sqrt(1-2M/r_0)/r_0, integral 16 pi(1-2M/r_0), m_H = M at every radius, M at r_0 = 2M, 0 in flat space.: Hand computation with Gamma^r_thetatheta = -r(1-2M/r) and N^r = sqrt(1-2M/r). → Correct.
- Research way: Hamiltonian constraint in a principal frame gives 2 sum kappa_i kappa_j; Kasner principal curvatures p_i/t; sum p_i p_j = 0 and sum p_i^2 = 1; exactly one exponent negative except (1,0,0), which is flat; the negative-exponent direction stretches toward t = 0; Willmore inequality >= 16 pi with the summed H; IMCF speed 1/(kappa_1 + kappa_2); Riemannian Penrose inequality for a connected horizon.: Hand algebra for each step. Case analysis of the exponents: two negatives force p_3 > 1 and sum of squares > 1. Checked (-1/3, 2/3, 2/3) with python3. Checked the Willmore factor: the integral of the averaged H squared is at least 4 pi, so the summed form is at least 16 pi. → Correct. The Kasner problem is sign-convention independent where it says so.
- SI restoration for the Hawking mass: mass = c^2 m_H / G with m_H a length.: Dimensional check: G M / c^2 is a length. → Correct.
- References: Moritz 1980 Bull. Geod. 54, 395-405; Young 1805 Phil. Trans. 95, 65-87; Euler 1767 Mem. Acad. Berlin 16, 119-143 (E333); Meusnier 1785 Savans etrangers 10, 477-510, read 1776; Dupin 1813 Developpements de geometrie, Courcier; Gauss 1828 Comment. Gotting. Recent. 6, 99-146; Hawking 1968 J. Math. Phys. 9, 598-604; Huisken and Ilmanen 2001 J. Diff. Geom. 59, 353-437; Bray 2001 J. Diff. Geom. 59, 177-267; Mars 2009 Class. Quantum Grav. 26, 193001; Kasner 1921 Am. J. Math. 43, 217-221; Belinskii, Khalatnikov and Lifshitz 1970 Adv. Phys. 19, 525-573; Willmore 1965 An. Sti. Univ. Al. I. Cuza Iasi 11B, 493-496; Marques and Neves 2014 Ann. Math. 179, 683-782.: WebSearch against publisher pages, ADS, Project Euclid, JSTOR, arXiv and the Euler Archive. → All confirmed. Added DOIs for Huisken-Ilmanen, Bray (plus arXiv math/9911173), Mars, Kasner, BKL and Marques-Neves. Hawking's DOI was not shown by a reliable record, so it was left null. History scope checked: Meusnier's minimal-surface reading of Lagrange's equation, Dupin's indicatrix and his theorem on triply orthogonal families, and Gauss's definition of curvature through the spreading of normals are correctly attributed.
- Second physics review, diff check of the second novice read: the entry try-it now uses a tin can on its side. A right circular cylinder bends most sharply around it and not at all along it, the two directions are a quarter turn apart, and the can stays on one side of the ruler, so it is 'a surface like that' in the way's sense.: Shape operator of a cylinder of radius a with the outward normal: K^mu_nu has eigenvalues -1/a around and 0 along, computed from K_{mu nu} = n-hat . d_mu d_nu X in the check's own helical parametrization and in the plain one. Convexity: every normal section has kappa_n of one sign or zero, so the surface never crosses the tangent plane. Gap under a ruler across a can of body radius 3.7 cm at 2 cm from the touching point: 0.587 cm. → Correct on every count. The eigenvalues are -1/a and 0, their eigendirections are orthogonal, and a can is convex, so the way's scope ('the shell stays on one side of the ruler') covers it. One wording change was needed: a real food tin is seamed, so its end rims stand about a millimetre proud of the body and a ruler laid along the can rests on them. 'The gap disappears' became 'The gap stops growing', which is exactly true for an ideal cylinder and for a seamed tin alike, and which is the way's own measure of bending.
- Second physics review: the egg way's revised setup and numbers. The touching point is 'at one point on the widest circle around the egg'; the gap is read '2 centimetres along the ruler'; the tennis ball beats the basketball 'at the same distance from the touching point'.: The widest circle of a prolate egg is a normal section, so the around-gap is exact: 2.2 - sqrt(2.2^2 - 2^2). The along-gap is the exact meridian ellipse, 2.2(1 - sqrt(1 - 4/c^2)) with half-length c. python3 for all four numbers. → Correct. Around 1.2835 cm ('about 1 and a quarter centimetres'); along 0.6327 cm at c = 2.85 and 0.6069 cm at c = 2.90 ('about 6 millimetres'); tennis ball of radius 3.35 cm gives 0.663 cm against a basketball's 0.169 cm at radius 11.94 cm. Naming the widest circle also makes the setup exact, because the ruler laid on an egg lying on its side touches at the top of that circle.
- Second physics review: the saddle way's revised sentences, 'which is shaped the same on both sides of the horse' and 'The principal curvature along the horse is positive, and the one across it is negative.': A reflection of the surface that fixes the point commutes with the shape operator, so it maps eigenspaces to eigenspaces; its own +1 and -1 eigenlines in the tangent plane are then principal whenever kappa_1 differs from kappa_2, which holds at a saddle. Signs from kappa_n s^2/2 at a level point with an upward normal. → Correct, and the restored noun fixes the earlier regression: it is a curvature, not a direction, that is positive. One mirror plane suffices; the saddle need not be symmetric front to back.
- Second physics review: the Earth common question's added step, 'A curve that stays inside a circle and touches it cannot cross to the outside, so the curve must bend more sharply than the circle there', and 'directly out from the equator'.: Comparison of curvatures at a point of tangency: if a curve stays inside a circle of radius a and touches it, its curvature there is at least 1/a. Checked against the numbers: the meridian ellipse has radius b^2/a = 6335.4 km at the ends of its long axis, against a = 6378.1 km for the equator. The silhouette seen from a distant point in the equatorial plane is the ellipse with half-axes a and b. → Correct. The viewpoint 'directly out from the equator' is the one that shows the meridian ellipse edge on, and the equator projects to the ellipse's long axis, so the two ends named are on the equator.
- Second physics review: independent re-derivation of the whole sign chain, K_{mu nu} = n-hat . d_mu d_nu X, kappa_n = K_{mu nu} t^mu t^nu, d_mu n-hat = -K^lambda_mu d_lambda X, S(X) = -nabla-bar_X N, g(SX,Y) = II(X,Y), S^mu_nu = K^mu_nu.: Differentiated n-hat . d_nu X = 0 and raised the index; checked on the sphere (outward normal gives -1/a both ways) and on the cylinder (0 and -1/a). → Self-consistent throughout the note, and consistent with the notation trap 'sign-and-order'. It is the opposite of the sign most differential-geometry texts use, which the trap records.
- Formal way: 'for n = 2 the Gaussian curvature is det S', stated for a hypersurface of a general Riemannian ambient.: Gauss equation: for orthonormal principal directions, K_Sigma = K-bar(T_p Sigma) + det S. Counterexample inside this same note: the sphere r = r_0 of the time-symmetric Schwarzschild slice has det S = (1 - 2M/r_0)/r_0^2 while its Gaussian curvature is 1/r_0^2; the difference 2M/r_0^3 is exactly the slice's sectional curvature in the sphere's tangent plane. → Wrong as written; det S is the Gauss-Kronecker curvature and equals the Gaussian curvature only when the ambient space is flat. Fixed by stating the Gauss equation. The working way's identical claim is already scoped to flat three-dimensional space and stands.
- Entry misconception 'extremes-at-any-angle': 'At a point of a smooth surface, the sharpest and gentlest directions are always a quarter turn apart, unless every direction bends alike.': Tried the note's own saddle. With kappa_1 = +2 and kappa_2 = -1 per unit length, Euler's formula gives kappa_n = 0 where tan^2 phi = 2, that is 54.7 degrees from the sharpest direction. → False at a saddle point: read without signs, the gentlest bending is no bending at all, in two directions that are not a quarter turn from the sharpest. The claim is true where the surface stays on one side of the ruler, and true at every point once bending carries a sign. Rewritten to say both, in the same everyday words.
- Summary: 'An egg's shell, for example, bends more sharply around the egg than along it.': Prolate spheroid with half-axes 2.2 and 2.85 cm: ratio of the meridian to the parallel normal curvature is a^2/(a^2 cos^2 u + c^2 sin^2 u), computed with python3 at several points. → True everywhere except at the two tips, where the ratio is 1 and the point is umbilic, as the note itself says of a spheroid's poles. Scoped to 'at its widest part', which also matches where the entry way puts the ruler.
- Every number in the note, recomputed from scratch.: python3 throughout: GRS80 M and N at 0, 45 and 90 degrees and the kilometres per degree; the Euler radius at a 45 degree heading; 1/(MN) at pole and equator; the egg and ball gaps; the satellite dish at vertex and rim; the helical can's metric, inverse metric, mixed tensor, eigenvalues, eigenvectors and Euler check; the catenoid neck; the star umbilic's line-field index tracked over 4000 steps at three radii; the Schwarzschild sphere and its Hawking mass; the Kasner exponents. → Every value reproduces: 6335.4393, 6378.1370, 110.5743, 111.3195, 6367.38, 6388.84, 6399.5936 (111.694 per degree), 6356.72, 2.4417e-8 and 2.4747e-8; 1.2835, 0.6069 to 0.6327, 0.663, 0.169 cm; 0.31525 and 0.42875 per metre with radii 3.172 and 2.332 m; eigenvalues -1/3 and 0 per cm with radius 8.333 cm for the helix direction; +-1/3 per cm at the catenoid neck; index -0.500000 and kappa_1 - kappa_2 within O(r^2) of 2r; m_H = M at every radius and 0 in flat space; (-1/3, 2/3, 2/3) satisfies both Kasner constraints. Choosing f = 1/298.257 or 1/298.257222101 changes nothing at the quoted precision.
- Related concept: the photon sphere 'is a totally umbilic timelike surface, with all principal curvatures equal'.: For r = const in Schwarzschild the ratios II_tt/g_tt = f'/(2 sqrt f) and II_angular/g_angular = sqrt f / r agree when r f' = 2f, that is r = 3M. → Correct, and it is the only such radius outside the horizon.
- References, re-verified independently.: WebSearch against ADS, JSTOR, Project Euclid, Springer, the Annals of Mathematics, MathSciNet records and the Euler Archive. → All fourteen confirmed as recorded. Hawking 1968, J. Math. Phys. 9, 598-604, now confirmed with doi 10.1063/1.1664615 by ADS and the publisher record, so the DOI was added and the earlier concern is closed. Euler's memoir is E333, written 1760 and published 1767, which matches the history entry's year. Meusnier was read in 1776 and printed in 1785, as the contribution says.

**Counterexamples tried**

- Sphere and plane (every point umbilic): 'directions a quarter turn apart unless every direction bends alike' survives through its exception clause.
- Can (parabolic point, one principal curvature zero): the quarter turn still holds, and the thin-slice picture degenerates to two parallel lines. No sentence breaks.
- Cone tip and crease: excluded by 'smooth' at entry and by the formal limits of validity.
- Tilted point on a surface, such as the side of an egg lying down: broke the definition 'bends up when it rises on both sides'. Scoped to level points.
- Flat soap film in a flat wire ring: broke 'films with equal pressure form saddle-shaped surfaces'. Scoped.
- Prolate egg versus oblate Earth: broke 'sea level does the same as the egg'. Fixed to 'the other way round'.
- Black hole formed by collapse, and a different slicing: the hourglass throat and 'at one moment' fail. Scoped to an idealized unchanging black hole and the clocks of people far away.
- Non-round sphere, or data with motion: the Hawking mass is not the enclosed mass in general. Scoped to round spheres around a round mass at rest.
- Torus of revolution: no umbilics, consistent with chi = 0, as the note says.
- Timelike surface in Minkowski space: principal curvatures complex, as the formal check says.
- Kasner (1,0,0): flat spacetime with no negative exponent, correctly excluded.
- Second physics review. Tip of a prolate egg (umbilic): broke the summary's unscoped 'bends more sharply around the egg than along it'. Scoped to the widest part.
- Second physics review. Saddle with kappa_1 = +2 and kappa_2 = -1: broke 'the sharpest and gentlest directions are always a quarter turn apart', because the gentlest bending is zero, 54.7 degrees from the sharpest. The misconception's correction now gives both the convex case and the signed rule.
- Second physics review. Sphere in the time-symmetric Schwarzschild slice: broke 'for n = 2 the Gaussian curvature is det S' in a curved ambient space, since det S = (1 - 2M/r_0)/r_0^2 against a Gaussian curvature of 1/r_0^2. Fixed with the Gauss equation.
- Second physics review. A real seamed tin can: its end rims stand proud of the body, so 'The gap disappears' along the can fails by about a millimetre. 'The gap stops growing' holds for an ideal cylinder and a seamed tin alike.
- Second physics review. Parabolic point, again: on the can the thin slice of 'why-always-a-quarter-turn' degenerates from a stretched circle to a pair of straight lines. The answer's conclusion, stated for every smooth surface where the directions do not all bend alike, stays true, so nothing was rewritten; recorded as a concern because the entry try-it is now a can.
- Second physics review. Reversed normal, cone tip, crease, torus of revolution, timelike surface in Minkowski space and Kasner (1, 0, 0): all still handled by the sentences that scope them.

**Fixes**

- Working way earths-two-bendings-surveyed: 'bent more sharply around than along, and sea level on Earth does the same' was false, since the egg is sharper around and Earth's equator is sharper toward a pole. Rewritten as two sentences, 'bent by different amounts around it and along it. Sea level on Earth does too, on a far larger scale but the other way round'.
- Saddle way and glossary bend-up: the valley and hill definition was scoped with 'Where a surface is level'. 'The principal curvatures lie along the horse and across it' became 'the directions of the principal curvatures are along the horse and across it'.
- Check mountain-pass question: the same 'directions of' fix.
- Common question earths-two-bendings: added the missing comparison. The equator is a circle as wide as the oval, and the oval sits inside it, touching at the ends of its longest width, so it bends more sharply there. Those ends are on the equator, and the oval's bending there is the bending heading toward a pole.
- Common question why-it-matters-for-gravity: scoped the hourglass to an idealized black hole that does not spin and never changes, snapshotted by the clocks of people far away. The mass comparison is now 'a perfectly round sphere' in flat space and 'a round sphere centred on a round mass at rest'. 'Its edge' became 'The black hole's edge' so the pronoun is unambiguous.
- Observation soap-film-saddles: the heading now says the principal curvatures are equal and opposite, so the films are saddle-shaped wherever they are not flat.
- Visual card-touching-a-curved-patch sketch (author field): on the saddle and the crisp, a line drawn in the tangent plane pivots instead of a resting ruler.
- References: all 14 set verified, with DOIs and arXiv ids added where confirmed. Nothing was dropped for budget: entry explanations rise by 6 words to about 408, within the 440 review allowance, and tutoring by about 50 words, under its cap.
- Second physics review. Formal way 'The shape operator, umbilics and topology': 'for n = 2 the Gaussian curvature is det S' was false for a hypersurface of a curved ambient space, and the note's own Schwarzschild sphere is the counterexample. It now reads that det S is the Gauss-Kronecker curvature and that the Gauss equation makes it the Gaussian curvature minus the ambient sectional curvature of the tangent plane, so the two agree when the ambient space is flat.
- Second physics review. Misconception 'extremes-at-any-angle': the correction was a false universal at a saddle point. It now names the convex case ('an egg or a helmet, which stays on one side of a ruler') and adds the signed rule that holds everywhere. Still two sentences, still everyday words.
- Second physics review. Summary: 'An egg's shell, for example' became 'An egg's shell at its widest part, for example', because the two tips of an egg are umbilic, where the shell does not bend more sharply around than along.
- Second physics review. Entry try-it: 'The gap disappears when the ruler lies along the can' became 'The gap stops growing', because a seamed tin's end rims lift the ruler about a millimetre off the body. The new wording is exact for any cylinder and uses the way's own measure, how quickly the gap grows.
- Second physics review. Reference: Hawking 1968 gained doi 10.1063/1.1664615, confirmed this pass. Nothing was dropped or compressed for budget; the three entry-rung edits add 4 words to the summary, 1 to the try-it and 33 to a tutor field, all far inside their caps.

**Concerns**

- Conventions gaps, reported and not invented: the conventions file has no row for the second fundamental form's symbol and sign. The note uses K_{mu nu} = n-hat . d_mu d_nu X, and S(X) = -nabla_X N. The same letter K is the conventions symbol for Gaussian and sectional curvature, although inside this note K never means Gaussian curvature. The file also has no rows for the normalization of mean curvature (the note uses H = tr S / n) or the sign of the extrinsic curvature of a spacetime slice (the note leaves it unfixed and uses only even-degree expressions, except the Kasner problem, which states its choice). Both notation traps name course choices that the file does not yet record.
- The entry egg numbers model the egg as symmetric about its widest circle. A real egg's asymmetry changes the along gap by a few tenths of a millimetre.
- The formal umbilic-surface theorem is stated for C^3; C^2 versions exist but were not needed.
- The Hawking mass reference lacks a DOI because no reliable record confirmed it.
- Common question why-it-matters-for-gravity: the novice re-read found that 'at one moment by the clocks of people far away' leaves the reader to trust why far-away clocks are needed. The proposed sentence 'Near a black hole, clocks do not all tick alike, so a moment must say whose clocks set it.' is true, but it adds a second new idea, so the diff check did not apply it. An editor may cut the snapshot framing or keep it as it is.
- Second physics review, conventions still missing and reported again, not invented: the conventions file has no row for the symbol and sign of the second fundamental form or the extrinsic curvature of a slice, and none for whether mean curvature is the average or the trace. This note uses K_{mu nu} = n-hat . d_mu d_nu X with S(X) = -nabla-bar_X N, and H = tr S / n, agreeing with the sibling note normal-curvature. Rows should be added before more surface notes drift.
- Second physics review: the Kasner problem states 'Taking K_ij = (1/2) d_t h_ij', which is the opposite of what this note's own surface convention gives for a slice, namely II_ij = -(1/2) d_t h_ij. The problem declares the choice and says the opposite convention negates all three, and the research way says the same, so nothing is wrong; but until the conventions file fixes a slice sign, a reader who carries the note's surface convention into the problem will find the signs flipped. The choice made is the one that keeps the Kasner exponents equal to the principal curvatures times the time, which the leads_to entry also uses.
- Second physics review: the entry common question 'why-always-a-quarter-turn' explains the quarter turn through a thin slice that is a stretched circle on an egg and a pair of curves on a saddle. Neither picture fits a can, where the slice is a pair of straight lines, and the entry try-it is now a can. The answer's conclusion is true as stated, so this is a teaching gap rather than an error; one sentence for the can would close it, within the tutoring budget.
- Second physics review: the working way 'Earth's two bendings, surveyed' opens 'bent more sharply around its widest part than along it', where 'it' can be read as the widest part rather than the egg. The claim is right either way; an editor may prefer 'than along the egg'.
- Second physics review: the Hawking mass key equation is justified_by 'stated', but the research way presents the formula without saying it is taken on trust, unlike the Earth way's 'stated here without derivation'. Left for an editor, since it changes no claim.

**Diff check** (2026-09-13, revision 5)

- Saddle way and bend-up glossary: 'level' glossed as 'sloping in no direction'; 'The middle of the seat is level, so there the seat bends up along the horse and down across it.': The explanation has the seat rising toward front and back and dropping over the sides, so the middle is a stationary point of the seat's height, where the tangent plane is horizontal. At a level point the height along a normal section is kappa_n s^2/2, so rising on both sides means kappa_n > 0 with an upward normal. → Correct. The gloss matches a horizontal tangent plane, and the up-or-down rule is now used only where it holds.
- Mountain-pass check question: 'There the ground is level' at the road's highest point.: The ground drops ahead and behind and rises on both sides, so the point is a saddle point of the terrain height, with a horizontal tangent plane. Reworked the check: across the road kappa_n > 0, along the road kappa_n < 0; the answer is unchanged. → Correct, and consistent with the answer.
- Earth common question: from far out beside the equator, the outline is an oval through both poles; a walk from the equator toward a pole follows that oval; a circle with the same centre, as wide as the equator, encloses the oval and touches it at the ends of its longest width, which lie on the equator; the oval bends more sharply there; a walk along the equator bends like that circle.: python3 with GRS80 (a = 6378.137 km, f = 1/298.257222101). A distant viewer in the equatorial plane sees the meridian ellipse (half-axes a and b = a(1-f)) as the outline, through both poles. The ellipse lies inside its major circle of radius a and touches it at the major-axis ends, on the equator. Curvature there a/b^2 = 1.5784e-4 per km = 1/M, versus 1/a = 1.5679e-4 per km for the circle. The equator is a circle of radius a whose curvature vector points at the centre, along the surface normal, so its normal curvature is 1/a = 1/N, equal to the drawn circle's. → Circle, tangency, equator location and both bendings correct. Error: 'follows that oval' names the outline seen from one viewpoint, but a walk from most equator points follows a different meridian, which the viewer sees edge-on across the middle. Every meridian is an oval of the same shape, so the sentence was reworded to 'follows an oval of that same shape'.
- Gravity common question: 'a round sphere centred on it bends less than a sphere of the same area in flat space, and the shortfall tells you the mass inside.': python3 on the time-symmetric Schwarzschild slice with M = 1: at r = 3, 5, 10 each principal curvature has size sqrt(1 - 2M/r)/r, below the flat value 1/r for the same area 4 pi r^2, and the Hawking mass comes out 1.000 each time. Tried spheres near the horizon (bending goes to zero, still less) and spheres far out (the shortfall goes to zero as the mass's effect fades). → Correct for spheres outside the mass, which 'around' implies; the flat-space comparison is now named explicitly.
- Working way opening: the egg bent more sharply around its widest part than along it; sea level bends differently in two directions the other way round, with the toward-a-pole direction sharper at the equator.: Egg at its widest part: around radius 2.2 cm, along profile radius b^2/a = 3.69 to 3.82 cm for half-length 2.85 to 2.9 cm, so around is sharper. Earth at the equator: M = 6335.4 km < N = 6378.1 km, so the meridian is sharper and the along-the-equator direction, the analogue of the egg's around direction, is gentler. → Correct: the sharper direction on the egg is around its axis, and on Earth it is along the meridian, so the order really is reversed.
- Novice proposal, not applied by the re-read: add 'Near a black hole, clocks do not all tick alike, so a moment must say whose clocks set it.' to the gravity common question.: Checked against the static slicing. Clocks staying still at different heights tick at different rates by far-away clocks, so equal readings on such clocks do not pick out the t = const snapshot. The sentence is true in that sense, but it offers a second new idea, not a reason the reader can check, in a spoken answer about bending. → Not applied. The existing sentence names the measurer as rule 7 requires and is correct. Left for the editor as a concern, not changed here.
- Fix: Common question earths-two-bendings: 'So a walk from the equator toward a pole follows that oval.' became 'So a walk from the equator toward a pole follows an oval of that same shape.', because the outline seen from one viewpoint is only one meridian. Four words added to tutoring; nothing dropped.

**Diff check** (2026-09-13, revision 7)

- The twelve entry and working strings the second novice read changed at revision 6: the tin-can try-it and the way's closing pointer, the egg setup and gap wording, the tennis-ball comparison, the saddle way's mirror-symmetry and sign sentences, the glossary entry for saddle, and the common questions 'earths-two-bendings', 'why-always-a-quarter-turn' and 'egg-with-signs'.: Re-derived or recomputed each claim: cylinder eigenvalues and convexity; exact around and along gaps on a prolate egg; gap against ball radius; reflection symmetry and the shape operator; signs from kappa_n s^2/2 at a level point; the inside-a-circle comparison of curvatures at a point of tangency; the Dupin indicatrix on an egg and a saddle; and the all-negative egg top. → Every claim holds, and no number changed. One wording fix was needed, 'The gap disappears' to 'The gap stops growing', for a seamed tin can.
- The novice's proposed but unapplied sentence for 'why-it-matters-for-gravity': 'Near a black hole, clocks do not all tick alike, so a moment must say whose clocks set it.': Checked for truth and for whether it adds a claim the entry rung must then support. → True for a static black hole, and it is the reason the snapshot names distant clocks. It still introduces gravitational time running at different rates, a second new idea in an answer that already carries the hourglass throat and the weighing of a sphere. Left unapplied, as the first diff check did, and left in the concerns for an editor.
- Fix: Applied the three entry-rung and one formal-rung fixes listed in this review's fixes, then bumped revision 6 to 7 and set status physics-reviewed. A novice re-read of exactly the three changed entry strings follows.

**Diff check** (2026-09-13, revision 8)

- Summary, changed at revision 8: 'An egg's shell at its widest circle, for example, bends more sharply around the egg than along it.' The re-read narrowed 'widest part' to 'widest circle'.: Modelled a hen's egg as a prolate spheroid 5.7 cm long and 4.4 cm wide, half-axes 2.85 cm along the axis and 2.20 cm across it, and took a point on the circle of greatest distance from the axis. python3: the around direction is that circle, of radius 2.20 cm, so its normal curvature is 1 over 2.20, which is 0.4545 per cm; the along direction is the profile ellipse, whose radius of curvature at the end of its short half-axis is 2.85 squared over 2.20, which is 3.692 cm, so its normal curvature is 0.2709 per cm. Checked that these two really are the extremes: on any surface of revolution the meridians and the circles around the axis are the lines of curvature, so these are the principal directions, and Euler's formula puts every other direction between them. → Correct. Around bends 1.68 times as sharply as along at the widest circle, and the two are the principal directions there. The narrower scope is also true: every point of the widest circle is equivalent by the symmetry about the axis, and the tip counterexample that forced the scoping stays excluded. The wording matches where the entry way puts the ruler, 'one point on the widest circle around the egg', and the entry way's gap numbers follow from the same two radii: 1.283 cm around and 0.589 cm along, 2 cm from the touching point.
- Misconception extremes-at-any-angle, second sentence, changed at revision 8: 'At a saddle, where the surface bends both ways, it is the largest and the smallest bending, counted with signs, whose directions are a quarter turn apart.' The re-read replaced 'the largest and smallest signed bending'.: Compared the two wordings claim by claim: both say the extremes of the signed normal curvature, and neither adds a condition. Re-derived the geometric claim from Euler's formula, normal curvature equals kappa one times cosine squared of the angle plus kappa two times sine squared. At a saddle kappa one is positive and kappa two negative, so they differ, so their directions are orthogonal, with no exception needed. python3 with kappa one equal to plus 1 and kappa two equal to minus 5: the largest is at 0 degrees and the smallest at 90 degrees, while the two directions of zero bending are at plus and minus 24.1 degrees, only 48.2 degrees apart. → Correct, and the sentence still does the work it was written for. Read without signs, the sharpest bending at that saddle is the one of size 5 and the gentlest is zero, and those are not a quarter turn apart; counted with signs the quarter turn is exact. 'Counted with signs' is the note's own phrasing for the rule the saddle entry way states, upward bending positive and downward negative at a level point, so no new term enters a line the tutor speaks.
- Entry try-it of turn-a-ruler-on-an-egg, changed at revision 8: 'When the ruler lies along the can, a quarter turn away, the gap does not grow at all, because the can does not bend in that direction.' The re-read replaced 'The gap stops growing when the ruler lies along the can'.: A tin can is a right circular cylinder. Its principal curvatures are 1 over the radius around the can and zero along it, a quarter turn apart, and the line along the top is straight in space, so the reason clause is exact rather than merely zero to leading order. Retried the seamed-tin counterexample that forced the earlier wording: proud end rims hold the ruler about a millimetre clear of the body, so along the can the gap is a roughly constant sliver that shrinks to nothing at the rims. Checked the other half of the try-it against the way's measure with python3: on a can 7.4 cm across, 2 cm from the touching point the gap around the can is 0.587 cm. → Correct, and strictly better than the sentence it replaced. 'Stops growing' asserted growth and then an end to it, which is false in that direction for an ideal cylinder and for a seamed tin alike; 'does not grow at all' is true for both. The claim is unchanged in every other respect, and it stays consistent with the way's rule that the more quickly the gap grows, the more sharply the surface bends.
- Fix: None. All three changed sentences are accurate within their stated scope, claim exactly what they replaced or something equally true, and agree with the rest of the note. Revision stays 8 and no learner-visible text changed, so no novice sign-off is owed for this check.
