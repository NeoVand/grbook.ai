---
type: "concept"
schema_version: 2
id: "normal-curvature"
title: "Normal and geodesic curvature"
tagline: "How a path on a curved surface bends: the ground's part and the steering part"
domain: "curvature"
tier: "advanced"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["normal curvature", "geodesic curvature"]
prerequisites: ["curvature-of-a-curve", "second-fundamental-form", "geodesic", "levi-civita-connection", "connection-one-forms"]
leads_to: ["principal-curvatures", "geodetic-precession", "photon-sphere"]
visuals: ["bend-arrow-split-on-a-surface", "carry-an-arrow-around-a-loop"]
---

# Normal and geodesic curvature

*How a path on a curved surface bends: the ground's part and the steering part*

`normal-curvature` · curvature · advanced · physics-reviewed (revision 8)

**Needs:** [[curvature-of-a-curve]] (entry) · [[second-fundamental-form]] (working) · [[geodesic]] (working) · [[levi-civita-connection]] (formal) · [[connection-one-forms]] (formal)  
**Opens:** [[principal-curvatures]] · [[geodetic-precession]] · [[photon-sphere]]  
**Related:** [[holonomy]] · [[gaussian-curvature]] · [[frenet-serret-equations]] · [[extrinsic-curvature-of-a-hypersurface]] · [[black-hole-shadow]]  
**Visuals:** ★ [[bend-arrow-split-on-a-surface]] · [[carry-an-arrow-around-a-loop]]

> Walk on a smooth, round ball without ever steering, and your path still bends, seen from far away, outside the ball. The part of a path's bend that comes from the ground curving away beneath your feet is called normal curvature. Steer to your left or right, and your direction of travel also turns along the ground. The part that comes from steering is called geodesic curvature, and a walk that never steers has none.

## You will be able to

**Entry**
- Explain why a path on a ball bends, seen from outside, even when the walker never steers. `objectives/explain-the-ground-part` ← `checks/tape-around-a-football`
- Distinguish the part of a path's bend that comes from steering from the part that comes from the ground. `objectives/separate-the-steering-part` ← `checks/small-ring-on-a-ball`, `problems/cycle-path-on-earth`

**Working**
- Compute the normal and geodesic curvature of a curve on a surface, with their signs, and combine them into the curve's curvature. `objectives/compute-the-split` ← `checks/ring-split-on-a-ball`, `problems/skateboard-bowl`
- Use Meusnier's theorem and the geodesic equation to decide which part of a curve's bend is fixed by its direction and which by its steering. `objectives/tell-direction-from-steering` ← `checks/tilted-circle-claim`, `checks/spiral-tape-on-a-can`

**Formal**
- Prove that geodesic curvature is intrinsic, and integrate it along a boundary in the Gauss–Bonnet theorem. `objectives/prove-intrinsic-and-integrate` ← `checks/circle-on-a-rolled-sheet`, `problems/gauss-bonnet-from-the-frame-angle`
- State when directions of zero normal curvature exist, and how a straight line lying in a surface relates to its geodesics. `objectives/state-asymptotic-directions` ← `checks/asymptotic-directions-at-a-saddle`

**Research**
- Locate circular light orbits from null normal curvature and from geodesic curvature in optical geometry. `objectives/locate-light-rings` ← `checks/photon-sphere-from-null-normal-curvature`, `problems/optical-circle-at-three-m`

## Ways in

### 1. A straight walk still bends · entry · picture

*Why does a path on a ball bend, seen from outside, even when the walker never steers?*

**Recap:** The curvature of a path is how many degrees your direction of travel turns for each metre along it.

Picture a huge, smooth ball, and a walker on it who never steers left or right. Walking without ever steering left or right is called walking straight.

She sets off from any point, in any direction. The ball on her left is a mirror image of the ball on her right, so she has no reason to steer to either side. Her path therefore stays on the line where those two equal halves meet. Seen from far away, outside the ball, that line is a circle as big as the ball, going around the ball's middle. Halfway around, she heads the opposite way to the way she set off. So her direction of travel turned, although she never steered.

The ground made that turn. A step aimed exactly along the ground where she stands would carry her foot a little off the ball, because the ground ahead curves away from that direction. Her foot lands on the ground instead, and her direction of travel tips a little toward the ball's centre. This happens at every step.

The part of a path's bend that comes from following the ground is called normal curvature.

Treat Earth as a smooth, round ball about 40,000 kilometres around. A straight walk all the way around brings you back heading the way you set off, after turning steadily through one full turn, 360 degrees. Every stretch of a round ball is alike, so that turn is shared out equally, and 40,000 divided by 360 is about 111. On Earth, then, the ground bends a straight walk by 1 degree for every 111 kilometres. A walk of 1 kilometre turns you by less than one hundredth of a degree, far too little to notice.

**Try it:** Start narrow masking tape anywhere on a round football, a soccer ball about 70 centimetres around. Press it down as you go, letting it run on ahead, and never pull the roll to the left or right of the line the tape already follows. The tape then never steers. After about 70 centimetres, it comes back to its own start, lined up with it. Seen from the side, it bends around the ball the whole way.

**Takeaway:** Even a walker who never steers follows a bent path on a ball, because the ground curves away beneath each step; that part of the bend is normal curvature.

*Visuals:* [[bend-arrow-split-on-a-surface]]<br>*See:* `checks/tape-around-a-football`

### 2. Steering bends the path along the ground · entry · contrast

*Which part of a path's bend on a ball comes from steering?*

**Recap:** Walking without ever steering left or right is called walking straight. On a ball, a straight walk goes around the ball's middle, along a circle as big as the ball. That walk bends, seen from far away, outside the ball, because the ground curves away beneath each step. The part of a path's bend that comes from following the ground is called normal curvature. A smaller circle turns you more for each metre along it.

Draw a small ring around one point on a basketball, and let a ladybird walk along it. A smaller circle turns you more for each metre, so her ring turns her direction of travel more sharply than a straight walk around the ball's middle would. Following the ground alone would take her on that straight walk, off her ring. So she must keep steering toward the point her ring goes around.

Her path therefore bends for two reasons. The ball's surface curves away beneath her, as it does for a straight walk. Her steering also turns her direction of travel to her left or right, along the ball's surface. The part of a path's bend that comes from steering is called geodesic curvature.

A straight walk has no steering, so its geodesic curvature is zero.

**Try it:** Draw a small ring on a football, going around one point, about 10 centimetres all the way round. Press narrow masking tape along the ring. The tape has to steer to follow the ring. The tape's two edges are the same length. But the edge nearer the point the ring goes around must lie along a shorter line than the other edge. So that nearer edge has more tape than its line needs, and that edge crinkles. Tape laid without steering, as in 'A straight walk still bends', lies almost smooth.

**Takeaway:** Steering turns your direction of travel to your left or right along the ground; that part of a path's bend is geodesic curvature, and a straight walk has none.

*What this leaves out:* The two parts do not simply add up to the whole bend. The ground's part tips the ladybird's direction of travel toward the ball's centre. The steering part turns that direction to her left or right, at ninety degrees to the first. So they combine like the two shorter sides of a right-angled triangle, with the whole bend as the longest side.

*Continues:* `ways_in/a-straight-walk-still-bends`<br>*Visuals:* [[bend-arrow-split-on-a-surface]]<br>*See:* `checks/small-ring-on-a-ball`, `problems/cycle-path-on-earth`

### 3. Split the bend into two perpendicular parts · working · calculation

*How is a surface curve's curvature vector split into normal and geodesic parts, and what fixes each part?*

The ladybird's path in 'Steering bends the path along the ground' bent for two reasons, one at right angles to the ball's surface and one along it; resolving a vector into perpendicular parts makes the split exact. Let a unit-speed curve $\mathbf r(s)$ lie on a surface in flat space, with unit tangent $\mathbf T = d\mathbf r/ds$ and a chosen unit normal $\hat{\mathbf n}$. Complete an orthonormal frame with $\hat{\mathbf u} = \hat{\mathbf n}\times\mathbf T$, which points to the walker's left when the walker's head points along $\hat{\mathbf n}$. Since $\mathbf T\cdot\mathbf T = 1$, $d\mathbf T/ds$ is perpendicular to $\mathbf T$, so

$$\frac{d\mathbf T}{ds} = \kappa_n\,\hat{\mathbf n} + \kappa_g\,\hat{\mathbf u},\qquad \kappa^2 = \kappa_n^2 + \kappa_g^2.$$

The normal curvature $\kappa_n$ is positive when the curve bends toward $\hat{\mathbf n}$. The geodesic curvature $\kappa_g$ is positive when it bends toward the walker's left, the course's positive sense. The parts are perpendicular components, so their squares add, not the parts themselves.

The normal part depends only on the direction. Gauss's formula gives $\kappa_n = K_{\mu\nu}t^\mu t^\nu$, with $t^\mu = dx^\mu/ds$ and $K_{\mu\nu}$ the second fundamental form, so every curve through a point in the direction $t^\mu$ has the same $\kappa_n$, however it steers. If the curve's principal normal makes an angle $\varphi$ with $\hat{\mathbf n}$, then $\kappa_n = \kappa\cos\varphi$: this is Meusnier's theorem. A tilted curve needs a larger $\kappa$ to share that $\kappa_n$.

The tangential part is the geodesic equation. The derivation 'Split of the bend' shows

$$\kappa_g\,\hat{\mathbf u} = \Big(\frac{dt^\lambda}{ds} + \Gamma^\lambda{}_{\mu\nu}\,t^\mu t^\nu\Big)\mathbf e_\lambda,$$

which involves only the metric and its derivatives. So $\kappa_g = 0$ all along a curve exactly when it obeys the geodesic equation with arc length as parameter: a geodesic, the path of a straight walk.

On a sphere of radius $a$ with the outward normal, $K_{\mu\nu} = -g_{\mu\nu}/a$, so $\kappa_n = -1/a$ in every direction. For Earth, $|\kappa_n| = 1/(6371\ \text{km})$ in radians per length; one radian is $57.3^\circ$, so this is the entry rung's $1^\circ$ per $111$ km. A circle at colatitude $\theta_0$, walked eastward, has $\kappa = 1/(a\sin\theta_0)$, pointing at the sphere's axis. Then $\kappa_g^2 = \kappa^2 - \kappa_n^2$ gives $\kappa_g = \cot\theta_0/a$, positive in the northern hemisphere, where the circle bends toward the North Pole, on the walker's left. The equator has $\kappa_g = 0$. On a cylinder of radius $a$ with the outward normal, the principal curvatures are $0$ along the axis and $-1/a$ around it, so Euler's formula $\kappa_n = \kappa_1\cos^2\beta + \kappa_2\sin^2\beta$ gives $\kappa_n = -\sin^2\beta/a$ for a direction at angle $\beta$ to the axis.

**Takeaway:** The curvature vector of a surface curve splits into a normal part fixed by its direction alone and a tangential part, the geodesic curvature, that vanishes exactly on geodesics; their squares add.

*What this leaves out:* Assumes a $C^2$ curve on a $C^2$ surface in flat three-dimensional space, with a chosen normal; reversing $\hat{\mathbf n}$ flips both signs.

*Continues:* `ways_in/a-straight-walk-still-bends`, `ways_in/steering-bends-the-path-along-the-ground`<br>*Builds on:* [[second-fundamental-form]], [[christoffel-symbols]], [[geodesic]]<br>*Visuals:* [[bend-arrow-split-on-a-surface]]<br>*See:* `derivations/split-of-the-bend`, `checks/ring-split-on-a-ball`, `checks/tilted-circle-claim`, `checks/spiral-tape-on-a-can`

### 4. Two pushes on a hilltop bend · working · operational

*What does each part of the split do to a vehicle moving along a road surface?*

The two perpendicular parts of 'Split the bend into two perpendicular parts' are felt as two different pushes. A car moves along a curve on a road surface with speed $v = ds/dt$, as its speedometer measures relative to the road. Differentiating $\mathbf v = v\mathbf T$ and splitting $d\mathbf T/ds$ gives, relative to the road and neglecting Earth's rotation,

$$\mathbf a = \frac{dv}{dt}\,\mathbf T + v^2\kappa_n\,\hat{\mathbf n} + v^2\kappa_g\,\hat{\mathbf u}.$$

The road pushes along $\hat{\mathbf n}$; the tyres' grip and gravity's component along the road supply the rest. So $\kappa_n$, set by the road's shape and the car's heading, changes the road's push, and $\kappa_g$, set by the steering, decides the sideways grip needed.

Take a dome-shaped hilltop whose crest has radius of curvature $200$ m in every direction, with $\hat{\mathbf n}$ pointing up. A car crosses the crest at $15$ m/s. There $v^2\kappa_n = -1.13\ \text{m/s}^2$, downward, so the road's push per unit mass drops from $9.81$ to $8.69\ \text{m/s}^2$: an accelerometer's vertical reading falls by 11 percent. If the driver also steers on a bend with $\kappa_g = 1/(50\ \text{m})$, the tyres must supply $4.5\ \text{m/s}^2$ sideways, while the vertical reading stays $8.69\ \text{m/s}^2$, because every heading has the same $\kappa_n$ at this crest. The whole acceleration is $v^2\kappa = 4.64\ \text{m/s}^2$, and the path's radius of curvature in space is $48.5$ m. Below a crest radius of $v^2/g = 23$ m the road would have to pull, so the car leaves the road.

**Takeaway:** Moving along a surface curve, normal curvature changes the surface's push and geodesic curvature sets the sideways grip; each scales with speed squared.

*What this leaves out:* Newtonian motion relative to a road fixed on a non-rotating Earth; at the crest, gravity is along the normal.

*Continues:* `ways_in/split-the-bend-into-perpendicular-parts`<br>*See:* `problems/skateboard-bowl`

### 5. Curves on a hypersurface · formal · structure

*What are normal and geodesic curvature in a Riemannian setting, which of them is intrinsic, and what theorems do they obey?*

The split in 'Split the bend into two perpendicular parts' is the Gauss formula evaluated along a curve, and it holds in any Riemannian space. Let $(M, \bar g)$ be Riemannian with Levi-Civita connection $\bar\nabla$, and $\Sigma \subset M$ a $C^2$ hypersurface with induced metric $g$, its Levi-Civita connection $\nabla$, a unit normal field $N$, and second fundamental form $\mathrm{II}(X,Y) = \bar g(\bar\nabla_XY, N)$. For a unit-speed $C^2$ curve in $\Sigma$ with tangent $T$,

$$\bar\nabla_TT = \nabla_TT + \mathrm{II}(T,T)\,N.$$

*Definitions.* The normal curvature is $\kappa_n = \mathrm{II}(T,T)$. The geodesic curvature vector is $\nabla_TT$, tangent to $\Sigma$ and orthogonal to $T$ because $g(T,T) = 1$. On an oriented surface let $J$ rotate each tangent plane by $+\pi/2$, toward the walker's left; the signed geodesic curvature is $\kappa_g = g(\nabla_TT, JT)$, and $|\bar\nabla_TT|^2 = \kappa_g^2 + \kappa_n^2$.

*Results.*

- Meusnier: $\kappa_n$ depends only on $T$ at the point, because $\mathrm{II}$ is a tensor.
- Geodesic curvature is intrinsic. $\nabla$ is determined by $g$, so a local isometry carries geodesic curvature vectors to geodesic curvature vectors; it preserves $\kappa_g$ if it preserves orientation and flips its sign otherwise. $\kappa_n$ is not intrinsic: rolling a plane into a cylinder of radius $a$ keeps $g$ and changes $\kappa_n$ from $0$ to $-\sin^2\beta/a$ for the outward normal.
- Geodesics: a curve is a geodesic of $\Sigma$ iff $\kappa_g \equiv 0$, iff its acceleration $\bar\nabla_TT$ in $M$ is normal to $\Sigma$. It is also a geodesic of $M$ iff in addition $\kappa_n \equiv 0$. If $\mathrm{II} = 0$, $\Sigma$ is totally geodesic.
- Extremes: on a surface, $\kappa_n$ restricted to unit tangents is the quadratic form of the self-adjoint shape operator, so $\kappa_n = \kappa_1\cos^2\phi + \kappa_2\sin^2\phi$, with $\phi$ measured from a principal direction. Asymptotic directions, where $\kappa_n = 0$, exist iff $\kappa_1\kappa_2 \le 0$.
- Gauss–Bonnet: let $R \subset \Sigma$ be a region homeomorphic to a closed disk, with piecewise-smooth boundary traversed with $R$ on the left and exterior angles $\epsilon_i \in (-\pi, \pi)$. Then

$$\iint_R K\,dA + \oint_{\partial R}\kappa_g\,ds + \sum_i\epsilon_i = 2\pi,$$

where bare $K$ is the Gaussian curvature. *Proof sketch.* With an oriented orthonormal frame $e_1, e_2 = Je_1$ on $R$ and $\omega(X) = g(\nabla_Xe_1, e_2)$, writing $T = \cos\vartheta\,e_1 + \sin\vartheta\,e_2$ gives $\kappa_g = \vartheta' + \omega(T)$. The rotation index theorem gives $\oint d\vartheta + \sum_i\epsilon_i = 2\pi$, and Stokes with $d\omega = -K\,dA$ gives $\oint\omega = -\iint_RK\,dA$.

The same frame shows that a parallel vector's angle to $T$ changes at the rate $-\kappa_g$. So on an oriented surface the holonomy of a closed smooth loop is a rotation by $-\oint\kappa_g\,ds$ modulo $2\pi$, whether or not the loop bounds a disk.

*Limits.* $\kappa_n$ changes sign with $N$, and $\kappa_g$ with the orientation; on a non-orientable surface only $|\nabla_TT|$ is defined globally. A corner has no curvature and enters through its exterior angle. In higher codimension the normal curvature is a vector in the normal bundle. If $\bar g$ is indefinite and $\bar g(N,N) = \epsilon = \pm1$, the Gauss formula carries $\epsilon\,\mathrm{II}(T,T)N$, and a null tangent $k$ has no unit normalization, so only the vanishing of $\mathrm{II}(k,k)$ is independent of scale.

**Takeaway:** Normal curvature is the second fundamental form on the tangent and depends on the embedding; geodesic curvature is intrinsic, vanishes on geodesics, and closes the Gauss–Bonnet theorem.

*What this leaves out:* Surfaces are $C^2$ and, for signed $\kappa_g$, oriented; the Gauss–Bonnet statement is for a region homeomorphic to a disk.

*Continues:* `ways_in/split-the-bend-into-perpendicular-parts`<br>*Builds on:* [[levi-civita-connection]], [[connection-one-forms]]<br>*Visuals:* [[carry-an-arrow-around-a-loop]] (preset `latitude-circle`)<br>*See:* `derivations/geodesic-curvature-from-the-frame-angle`, `checks/circle-on-a-rolled-sheet`, `checks/asymptotic-directions-at-a-saddle`, `problems/gauss-bonnet-from-the-frame-angle`

### 6. Light that skims a sphere · research · bridge

*Where do normal and geodesic curvature of curves appear in black-hole physics?*

The limits of 'Curves on a hypersurface' allowed an indefinite metric and null tangents, and in general relativity that extension locates where light can circle a black hole. Set $G = c = 1$.

*Photon surfaces.* A timelike hypersurface $S$ is a photon surface if every null geodesic that starts tangent to $S$ stays in $S$. By the Lorentzian Gauss formula, a null geodesic of $S$ with tangent $k$ is a geodesic of spacetime iff $\mathrm{II}(k,k) = 0$. Requiring this for every null $k$ tangent to $S$ forces $\mathrm{II} = \lambda h$, with $h$ the induced metric: the surface is totally umbilic. Claudel, Virbhadra and Ellis proved that a timelike hypersurface is a photon surface exactly when it is totally umbilic. In Schwarzschild, the surface $r = r_0$ with outward unit normal has, for $k = (1 - 2M/r_0)^{-1/2}\partial_t + r_0^{-1}\partial_\theta$,

$$\mathrm{II}(k,k) = \frac{3M - r_0}{r_0^2\sqrt{1 - 2M/r_0}},$$

which vanishes only at the photon sphere $r_0 = 3M$. Light near that surface is lensed into the bright ring that outlines a black hole's shadow.

*Optical geometry.* In a static spacetime $g_{tt}\,dt^2 + \gamma_{ij}dx^idx^j$, Fermat's principle makes light rays geodesics of the optical metric $\tilde\gamma_{ij} = \gamma_{ij}/(-g_{tt})$. In the equatorial plane of Schwarzschild, the circle $r = r_0$ has optical geodesic curvature $(r_0 - 3M)/r_0^2$ toward the hole: zero at the photon sphere and of opposite sign inside it. This sign change is what is meant by the statement that centrifugal effects reverse inside $3M$. Gibbons and Werner turned lensing into Gauss–Bonnet: for a region bounded by a ray and a distant circle, the deflection angle is minus the integral of the optical Gaussian curvature, giving $4M/b$ at leading order for impact parameter $b$.

*Gyroscopes.* In a slice of Schwarzschild, the equatorial plane is totally geodesic, and a circle of radius $r$ in it has geodesic curvature $\sqrt{1 - 2M/r}/r$. A spin axis carried once around therefore returns rotated by $2\pi\big[1 - \sqrt{1 - 2M/r}\big] \approx 2\pi M/r$ in the sense of the loop, about two thirds of the geodetic precession of an orbiting gyroscope.

Open directions include uniqueness theorems for photon spheres in static vacuum spacetimes, and rotating black holes, where spherical photon orbits fill a photon region rather than a single photon surface.

**Takeaway:** Vanishing normal curvature in null directions picks out photon surfaces, and geodesic curvature in optical geometry locates light rings and turns lensing into Gauss–Bonnet.

*What this leaves out:* Uses static, spherically symmetric spacetimes; the optical-geometry statements need a static metric.

*Continues:* `ways_in/curves-on-a-hypersurface`<br>*See:* `checks/photon-sphere-from-null-normal-curvature`, `problems/optical-circle-at-three-m`, `observations/gravity-probe-b-geodetic`, `observations/m87-ring`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| curvature | — | How sharply a path bends at a place: the degrees your direction of travel turns for each metre along it. | [[curvature-of-a-curve]] |
| walk straight | — | To walk without ever steering left or right. The name describes what the walker does, not how the path looks from outside: on a ball, a straight walk still bends, because it follows the ground. Its path is called a geodesic. | [[geodesic]] |
| steer | — | To turn your direction of travel to your left or your right along the ground, as a cyclist does with the handlebars. | — |
| normal curvature | — | The part of a path's bend that comes from following the ground as the ground curves away beneath the path. Here normal does not mean ordinary: it means at right angles to the surface. This part tips the direction of travel at right angles to the ground, not to the walker's left or right. | [[normal-curvature]] |
| geodesic | jee-uh-DESS-ik | The path of a straight walk, one that never steers left or right along the ground. | [[geodesic]] |
| geodesic curvature | jee-uh-DESS-ik curvature | The part of a path's bend that comes from steering left or right along the ground. A straight walk, whose path is a geodesic, has none, which is where the name comes from. | [[normal-curvature]] |

## Key equations

### Split of a surface curve's bend · working

$$
\frac{d\mathbf T}{ds} = \kappa_n\,\hat{\mathbf n} + \kappa_g\,\hat{\mathbf u},\qquad \hat{\mathbf u} = \hat{\mathbf n}\times\mathbf T
$$

The rate of change of the unit tangent has a part along the surface normal and a part along the surface, perpendicular to the curve.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\mathbf T$ | unit tangent of the curve, $d\mathbf r/ds$ | T |
| $\hat{\mathbf n}$ | chosen unit normal of the surface | n hat |
| $\hat{\mathbf u}$ | unit vector along the surface to the walker's left, head along $\hat{\mathbf n}$ | u hat |
| $\kappa_n$ | normal curvature, positive toward $\hat{\mathbf n}$ | kappa n |
| $\kappa_g$ | geodesic curvature, positive toward the walker's left | kappa g |

**Holds when:** Unit-speed $C^2$ curve on a $C^2$ surface in flat three-dimensional space; both signs flip when $\hat{\mathbf n}$ is reversed.  
**Say it:** “d T by d s equals kappa n times n hat plus kappa g times u hat, where u hat is n hat cross T.”  
**Justified by:** `derivations/split-of-the-bend`

### Normal curvature from the second fundamental form · working

$$
\kappa_n = K_{\mu\nu}\,t^\mu t^\nu,\qquad g_{\mu\nu}t^\mu t^\nu = 1
$$

The normal part of the bend depends only on the curve's direction at the point.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K_{\mu\nu}$ | second fundamental form, $\hat{\mathbf n}\cdot\partial_\mu\mathbf e_\nu$ | K mu nu |
| $t^\mu$ | components of the unit tangent, $dx^\mu/ds$ | t mu |

**Holds when:** Unit tangent measured with the induced metric.  
**Say it:** “Kappa n equals K mu nu times t mu times t nu.”  
**Justified by:** `second-fundamental-form`

### The parts combine in quadrature; Meusnier's theorem · working

$$
\kappa^2 = \kappa_n^2 + \kappa_g^2,\qquad \kappa_n = \kappa\cos\varphi
$$

The curve's curvature is the length of the split vector, and the normal part is the curvature times the cosine of the tilt between the curve's principal normal and the surface normal.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa$ | curvature of the curve in space | kappa |
| $\varphi$ | angle between the curve's principal normal and $\hat{\mathbf n}$ | phi |

**Holds when:** The angle form needs $\kappa \neq 0$, so that the principal normal is defined.  
**Say it:** “Kappa squared is kappa n squared plus kappa g squared, and kappa n is kappa times cos phi.”  
**Justified by:** `derivations/split-of-the-bend`

### Geodesic part as the geodesic equation · working

$$
\kappa_g\,\hat{\mathbf u} = \Big(\frac{dt^\lambda}{ds} + \Gamma^\lambda{}_{\mu\nu}\,t^\mu t^\nu\Big)\mathbf e_\lambda
$$

The sideways part of the bend is the left side of the geodesic equation, so it vanishes exactly on geodesics.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Gamma^\lambda{}_{\mu\nu}$ | Christoffel symbols of the induced metric | gamma lambda mu nu |
| $\mathbf e_\lambda$ | coordinate basis vector on the surface | e lambda |

**Holds when:** Arc-length parameter; surface in flat three-dimensional space.  
**Say it:** “Kappa g times u hat equals d t lambda by d s plus gamma lambda mu nu t mu t nu, times e lambda.”  
**Justified by:** `derivations/split-of-the-bend`

### Local Gauss–Bonnet theorem · formal

$$
\iint_R K\,dA + \oint_{\partial R}\kappa_g\,ds + \sum_i\epsilon_i = 2\pi
$$

The curvature inside a disk-shaped region, the boundary's geodesic curvature and its corner angles add up to one full turn.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $K$ | Gaussian curvature (bare $K$, unlike $K_{\mu\nu}$) | the Gaussian curvature |
| $\epsilon_i$ | exterior angles at the corners, in $(-\pi, \pi)$ | the corner angles |

**Holds when:** Oriented surface; $R$ homeomorphic to a closed disk, boundary piecewise smooth and traversed with $R$ on the left.  
**Say it:** “The Gaussian curvature integrated over the region, plus the geodesic curvature integrated around its boundary, plus the corner angles, equals two pi.”  
**Justified by:** `derivations/geodesic-curvature-from-the-frame-angle`

## Derivations

### Split of the bend · working

**Goal:** Show that $d\mathbf T/ds = \kappa_n\hat{\mathbf n} + \kappa_g\hat{\mathbf u}$ with $\kappa_n = K_{\mu\nu}t^\mu t^\nu$, that the tangential part is the geodesic equation, and that $\kappa^2 = \kappa_n^2 + \kappa_g^2$.

1. Differentiate $\mathbf T\cdot\mathbf T = 1$: $2\,\mathbf T\cdot d\mathbf T/ds = 0$, so $d\mathbf T/ds$ has no component along $\mathbf T$.
2. $(\mathbf T, \hat{\mathbf u}, \hat{\mathbf n})$ is orthonormal, so $d\mathbf T/ds = \kappa_g\hat{\mathbf u} + \kappa_n\hat{\mathbf n}$ with $\kappa_g = \hat{\mathbf u}\cdot d\mathbf T/ds$ and $\kappa_n = \hat{\mathbf n}\cdot d\mathbf T/ds$.
3. Write $\mathbf T = t^\mu\mathbf e_\mu$ and use the chain rule: $d\mathbf T/ds = (dt^\lambda/ds)\,\mathbf e_\lambda + t^\mu t^\nu\,\partial_\nu\mathbf e_\mu$.
4. Insert Gauss's formula $\partial_\nu\mathbf e_\mu = \Gamma^\lambda{}_{\nu\mu}\mathbf e_\lambda + K_{\nu\mu}\hat{\mathbf n}$: $d\mathbf T/ds = \big(dt^\lambda/ds + \Gamma^\lambda{}_{\mu\nu}t^\mu t^\nu\big)\mathbf e_\lambda + K_{\mu\nu}t^\mu t^\nu\,\hat{\mathbf n}$.
5. Match the normal parts: $\kappa_n = K_{\mu\nu}t^\mu t^\nu$. Match the tangential parts: $\kappa_g\hat{\mathbf u}$ is the bracket times $\mathbf e_\lambda$.
6. Take the squared length of the split: $\kappa^2 = |d\mathbf T/ds|^2 = \kappa_g^2 + \kappa_n^2$.
7. Where $\kappa \neq 0$, $d\mathbf T/ds = \kappa\hat{\mathbf N}$; dotting with $\hat{\mathbf n}$ gives $\kappa_n = \kappa\cos\varphi$.

**Result:** $d\mathbf T/ds = \kappa_n\hat{\mathbf n} + \kappa_g\hat{\mathbf u}$, with $\kappa_n = K_{\mu\nu}t^\mu t^\nu = \kappa\cos\varphi$, $\kappa_g\hat{\mathbf u}$ the geodesic-equation bracket, and $\kappa^2 = \kappa_n^2 + \kappa_g^2$.

### Geodesic curvature from the frame angle · formal

**Goal:** Show that $\kappa_g = \vartheta' + \omega(T)$ and integrate it to the local Gauss–Bonnet theorem.

1. Take an oriented orthonormal frame $e_1$, $e_2 = Je_1$ on $R$ and set $\omega(X) = g(\nabla_Xe_1, e_2)$. Metric compatibility gives $\nabla_Xe_1 = \omega(X)e_2$ and $\nabla_Xe_2 = -\omega(X)e_1$.
2. Write $T = \cos\vartheta\,e_1 + \sin\vartheta\,e_2$, so $JT = -\sin\vartheta\,e_1 + \cos\vartheta\,e_2$.
3. Differentiate: $\nabla_TT = \vartheta'\,JT + \omega(T)\,(\cos\vartheta\,e_2 - \sin\vartheta\,e_1) = (\vartheta' + \omega(T))\,JT$, so $\kappa_g = \vartheta' + \omega(T)$.
4. Use $d\omega = -K\,dA$. Check on the unit sphere with $e_1 = \hat\theta$, $e_2 = \hat\phi$ and the outward normal: $\omega = \cos\theta\,d\phi$, so $d\omega = -\sin\theta\,d\theta\wedge d\phi = -dA$.
5. For a boundary traversed with $R$ on the left, the rotation index theorem in the frame gives $\oint_{\partial R}d\vartheta + \sum_i\epsilon_i = 2\pi$.
6. Integrate $\kappa_g$ and apply Stokes: $\oint\kappa_g\,ds = 2\pi - \sum_i\epsilon_i - \iint_RK\,dA$.

**Result:** $\iint_RK\,dA + \oint_{\partial R}\kappa_g\,ds + \sum_i\epsilon_i = 2\pi$ for a disk-shaped region on an oriented surface.

## Problems

### `cycle-path-on-earth` · entry · difficulty 1 · calculation

On Earth, a cyclist rides once around a circular cycle path 126 metres long, measured along the path. (a) About how many degrees does her direction of travel turn for each metre of path? (b) On Earth, the ground bends a straight walk by 1 degree for every 111 kilometres. How many kilometres of straight walking does it take for the ground to turn a walker's direction of travel as much as one metre of cycle path turns the cyclist's? (c) Does most of her bend come from steering or from the ground?

**Hints**

1. One lap turns her direction of travel by a full turn.
2. How many degrees does one metre of path turn her?

**Answer:** (a) About 2.9 degrees per metre. (b) About 317 kilometres. (c) Almost all of it comes from steering.

**Must contain:** One lap is a full turn of 360 degrees; About 2.9 degrees per metre; About 317 kilometres of straight walking; Almost all of her bend is steering

**Numeric:** turn per metre of cycle path = 2.857 deg (magnitude, ±0.1); straight walk with the same turn = 317 km (magnitude, ±3%)

**Solution**

1. One lap brings her back heading the way she started, so it turns her direction of travel by a full turn, 360 degrees.
2. Every part of a circular path is alike, so each metre turns her by 360 divided by 126, about 2.86 degrees.
3. The ground turns a walker's direction of travel by 1 degree for every 111 kilometres of straight walking. So turning her direction of travel by 2.86 degrees takes 2.86 times 111, about 317 kilometres.
4. One metre of her path turns the cyclist's direction of travel as much as 317 kilometres of straight walking would. So the ground's part of her bend is tiny, and almost all of her bend comes from steering.

### `skateboard-bowl` · working · difficulty 2 · calculation

A skateboarder rides a horizontal circle inside a spherical bowl of radius $a = 3.0$ m, at $60^\circ$ from the bowl's lowest point as seen from the bowl's centre. Take $\hat{\mathbf n}$ pointing into the bowl, toward its centre, and let her ride with the lowest point on her left. (a) Find $\kappa_n$ and $\kappa_g$ of her circle. (b) Ignoring friction, find the speed at which gravity's component along the bowl supplies exactly $v^2\kappa_g$. (c) Find the bowl's push per unit mass at that speed.

**Hints**

1. The circle is a circle of colatitude $60^\circ$ about the downward vertical.
2. Resolve the horizontal acceleration $v^2/\rho$ along $\hat{\mathbf n}$ and along the bowl.

**Answer:** (a) $\kappa_n = +1/a = 0.333$ m$^{-1}$ and $\kappa_g = +\cot60^\circ/a = 0.192$ m$^{-1}$. (b) $v = 6.64$ m/s. (c) $19.6\ \text{m/s}^2$, twice $g$.

**Must contain:** Normal curvature one over the bowl radius, toward the centre; Geodesic curvature cot 60 degrees over the radius, toward the lowest point; Friction-free speed about 6.6 metres per second; The bowl pushes with twice g

**Numeric:** friction-free speed = 6.64 m/s (magnitude, ±2%); bowl's push per unit mass = 19.62 m/s^2 (magnitude, ±2%)

**Solution**

1. The circle has radius $\rho = a\sin60^\circ = 2.60$ m and curvature $1/\rho$, pointing horizontally at the bowl's axis.
2. The bowl is a sphere, so $\kappa_n = 1/a = 0.333$ m$^{-1}$, positive because the circle bends toward $\hat{\mathbf n}$.
3. $\kappa_g^2 = 1/\rho^2 - 1/a^2 = \cos^2 60^\circ/(a^2\sin^2 60^\circ)$, so $|\kappa_g| = \cot60^\circ/a = 0.192$ m$^{-1}$. The in-bowl part of the horizontal pull toward the axis points down the wall, toward the lowest point on her left, so $\kappa_g > 0$.
4. Down the wall, gravity supplies $g\sin60^\circ$. Setting $g\sin60^\circ = v^2\cot60^\circ/a$ gives $v^2 = ga\sin^2 60^\circ/\cos60^\circ = 44.1$ m$^2$/s$^2$, so $v = 6.64$ m/s.
5. Along $\hat{\mathbf n}$, the push $P$ per unit mass minus gravity's component $g\cos60^\circ$ supplies $v^2\kappa_n$: $P = 4.91 + 44.1/3.0 = 19.6\ \text{m/s}^2$.
6. Check: the whole acceleration is $v^2/\rho = 17.0\ \text{m/s}^2$, and $\sqrt{14.7^2 + 8.49^2} = 17.0\ \text{m/s}^2$, so the squares add.

**Targets:** `parts-simply-add`

### `gauss-bonnet-from-the-frame-angle` · formal · difficulty 3 · proof

On an oriented surface, let $e_1, e_2 = Je_1$ be an orthonormal frame on a disk-shaped region $R$, with $\omega(X) = g(\nabla_Xe_1, e_2)$. (a) Show that $\kappa_g = \vartheta' + \omega(T)$, where $\vartheta$ is the angle of $T$ from $e_1$. (b) Using $d\omega = -K\,dA$ and the rotation index theorem, prove the local Gauss–Bonnet theorem. (c) On a sphere of radius $a$, check it for the polar cap bounded by the circle at colatitude $45^\circ$, walked eastward, and show that $-\oint\kappa_g\,ds$ equals the cap's area over $a^2$ modulo $2\pi$.

**Hints**

1. Differentiate $T = \cos\vartheta\,e_1 + \sin\vartheta\,e_2$ with the product rule.
2. For (c), $\kappa_g = \cot\theta_0/a$ and the circle has length $2\pi a\sin\theta_0$.

**Answer:** (a) $\nabla_TT = (\vartheta' + \omega(T))\,JT$. (b) $\oint\kappa_g\,ds = 2\pi - \sum_i\epsilon_i - \iint_RK\,dA$. (c) $\oint\kappa_g\,ds = 2\pi\cos45^\circ = 4.443$ rad and $\iint K\,dA = 2\pi(1 - \cos45^\circ) = 1.840$ rad, summing to $2\pi$; $-4.443$ rad $\equiv +1.840$ rad, a rotation of $105.4^\circ$ toward the walker's left.

**Must contain:** Geodesic curvature is the frame angle's rate plus the connection form; Stokes and the rotation index give Gauss-Bonnet; For the 45 degree cap: 254.6 degrees plus 105.4 degrees make a full turn; The holonomy is minus the integrated geodesic curvature modulo two pi

**Numeric:** integrated geodesic curvature of the 45 degree circle = 4.443 rad (magnitude, ±0.01); holonomy toward the walker's left = 105.44 deg (signed, ±0.2, mod 360)

**Solution**

1. Metric compatibility and $g(e_i, e_j) = \delta_{ij}$ give $\nabla_Xe_1 = \omega(X)e_2$ and $\nabla_Xe_2 = -\omega(X)e_1$.
2. The product rule gives $\nabla_TT = \vartheta'(-\sin\vartheta\,e_1 + \cos\vartheta\,e_2) + \omega(T)(\cos\vartheta\,e_2 - \sin\vartheta\,e_1) = (\vartheta' + \omega(T))\,JT$, so $\kappa_g = \vartheta' + \omega(T)$.
3. Integrate around $\partial R$ with $R$ on the left. The frame is defined on all of $R$, so the rotation index theorem gives $\oint d\vartheta = 2\pi - \sum_i\epsilon_i$.
4. Stokes gives $\oint\omega = \iint_R d\omega = -\iint_RK\,dA$. Adding, $\iint_RK\,dA + \oint\kappa_g\,ds + \sum_i\epsilon_i = 2\pi$.
5. For the cap, $K = 1/a^2$ and the area is $2\pi a^2(1 - \cos45^\circ)$, so $\iint K\,dA = 1.840$ rad. The circle has no corners, $\kappa_g = \cot45^\circ/a = 1/a$ and length $2\pi a\sin45^\circ$, so $\oint\kappa_g\,ds = 2\pi\cos45^\circ = 4.443$ rad. The sum is $6.283$ rad $= 2\pi$.
6. A parallel vector's angle to $T$ changes at rate $-\kappa_g$, and $T$ returns to itself, so the holonomy is $-4.443$ rad $\equiv 1.840$ rad $= 105.4^\circ$ modulo $2\pi$: the area rule for the cap on the walker's left.

### `optical-circle-at-three-m` · research · difficulty 2 · derivation

With $G = c = 1$, the equatorial optical metric of Schwarzschild is $d\tilde s^2 = dr^2/f^2 + r^2d\phi^2/f$ with $f = 1 - 2M/r$. Find the geodesic curvature of the circle $r = r_0$ in this metric, show that it vanishes at $r_0 = 3M$, and check the limit $M \to 0$.

**Hints**

1. Use $\Gamma^r{}_{\phi\phi} = -\tfrac12\tilde g^{rr}\partial_r\tilde g_{\phi\phi}$.
2. The unit tangent is $(\sqrt f/r_0)\,\partial_\phi$, and $\partial_r$ has optical length $1/f$.

**Answer:** $\tilde\kappa_g = (r_0 - 3M)/r_0^2$, toward decreasing $r$: zero at $r_0 = 3M$, reversed inside it, and $1/r_0$ when $M = 0$.

**Must contain:** The derivative of r squared over f is two times r minus three M over f squared; Geodesic curvature r zero minus three M over r zero squared; Zero at the photon sphere, one over r zero in flat space

**Solution**

1. $\partial_r(r^2/f) = 2r/f - 2M/f^2 = 2(r - 3M)/f^2$, so $\Gamma^r{}_{\phi\phi} = -\tfrac12 f^2\cdot 2(r - 3M)/f^2 = -(r - 3M)$.
2. The unit tangent is $T = (\sqrt f/r_0)\,\partial_\phi$, since $\tilde g_{\phi\phi} = r_0^2/f$. Along the circle $\nabla_TT = (f/r_0^2)\,\Gamma^r{}_{\phi\phi}\,\partial_r = -\big(f(r_0 - 3M)/r_0^2\big)\,\partial_r$.
3. $\partial_r$ has optical length $1/f$, so $|\nabla_TT| = |r_0 - 3M|/r_0^2$, pointing toward decreasing $r$ when $r_0 > 3M$ and away from the hole when $r_0 < 3M$.
4. At $r_0 = 3M$ the circle is an optical geodesic, a circular light orbit. With $M = 0$ the result is $1/r_0$, a circle in the flat plane.

## Observations

- **Geodetic precession of gyroscopes orbiting Earth, measured by Gravity Probe B** (measured, working). In a slice of the spacetime around a static spherical Earth, a plane through Earth's centre is totally geodesic, and a circular orbit of radius $r$ in it has geodesic curvature $\sqrt{1 - 2GM/rc^2}/r$, slightly less than $1/r$. Carrying the spin axis once around returns it rotated by $2\pi\big[1 - \sqrt{1 - 2GM/rc^2}\big]$ in the sense of the orbit, about two thirds of the geodetic precession; the rest comes from the orbital motion. *Numbers:* For $r = 7013$ km the spatial part is $0.82$ milliarcseconds per orbit, about $4.4$ arcseconds per year of the $6.6$ total for a spherical Earth. Measured: $6601.8 \pm 18.3$ milliarcseconds per year, against a prediction of $6606.1$. *Reference:* C. W. F. Everitt, D. B. DeBra, B. W. Parkinson, J. P. Turneaure and others (2011), *Gravity Probe B: Final Results of a Space Experiment to Test General Relativity*, Physical Review Letters 106, 221101, doi:10.1103/PhysRevLett.106.221101
- **The bright ring around the black hole at the centre of the galaxy M87** (measured, research). Light that skims the photon sphere, the surface of vanishing null normal curvature, is lensed into a ring around the shadow. For a non-spinning hole the shadow's edge has impact parameter $\sqrt{27}\,GM/c^2$. *Numbers:* Ring diameter $42 \pm 3$ microarcseconds. Calibrated with simulations, it gives a mass of $(6.5 \pm 0.7)\times10^{9}$ solar masses at 16.8 Mpc, consistent with the mass from stellar motions; for that mass $2\sqrt{27}\,GM/(c^2D) = 39.7$ microarcseconds. *Reference:* Kazunori Akiyama and others (2019), *First M87 Event Horizon Telescope Results. I. The Shadow of the Supermassive Black Hole*, The Astrophysical Journal Letters 875, L1, doi:10.3847/2041-8213/ab0ec7

## Teaching arc

1. **Ask whether a straight walk bends** (entry). Ask the opening prediction, then lay tape around a ball without ever pulling it to the left or right. *Why:* It separates never steering from following a straight line in space. *Predict:* If you walk all the way around a giant ball without ever steering, does your path bend, seen from far away outside the ball? *Visual:* [[bend-arrow-split-on-a-surface]] *Uses:* `ways_in/a-straight-walk-still-bends`, `checks/tape-around-a-football`
2. **Add steering** (entry). Put the ladybird on a small ring, then compare a cycle path's steering with the bend Earth's ground gives. *Why:* The second part of the bend appears only when the walker steers. *Predict:* Must a ladybird on a small ring around one point of a ball steer to stay on it? *Visual:* [[bend-arrow-split-on-a-surface]] *Uses:* `ways_in/steering-bends-the-path-along-the-ground`, `checks/small-ring-on-a-ball`, `problems/cycle-path-on-earth`
3. **Resolve the curvature vector** (working). Derive the split, then test the adding claim and the tilted circle. *Why:* Learners see that the normal part belongs to the direction and the parts add in quadrature. *Predict:* A small circle on a ball bends more sharply than a great circle in the same direction. Is its normal curvature bigger? *Uses:* `ways_in/split-the-bend-into-perpendicular-parts`, `derivations/split-of-the-bend`, `checks/ring-split-on-a-ball`, `checks/tilted-circle-claim`
4. **Unroll a spiral** (working). Wind tape slantwise on a can, then unroll the can. *Why:* It shows a curve bent in space with zero geodesic curvature. *Predict:* Does a spiral of tape around a can steer? *Visual:* [[bend-arrow-split-on-a-surface]] *Uses:* `checks/spiral-tape-on-a-can`
5. **Prove what is intrinsic, then integrate** (formal). Roll a sheet with a drawn circle, then derive Gauss–Bonnet from the frame angle. *Why:* It ties geodesic curvature to the metric and to holonomy. *Visual:* [[carry-an-arrow-around-a-loop]] (preset `latitude-circle`) *Uses:* `ways_in/curves-on-a-hypersurface`, `checks/circle-on-a-rolled-sheet`, `problems/gauss-bonnet-from-the-frame-angle`
6. **Skim a black hole** (research). Compute null normal curvature on spheres around a black hole, then the optical circle. *Why:* Both methods locate the photon sphere. *Uses:* `ways_in/light-that-skims-a-sphere`, `checks/photon-sphere-from-null-normal-curvature`, `problems/optical-circle-at-three-m`

## Misconceptions

### “If a walker never steers, her path cannot bend.” · entry · `never-steered-so-not-bent`

- **Why it is tempting:** On a flat floor, a walk without steering is a straight line.
- **What is true:** On a ball, the ground curves away beneath each step, so even a walk without steering follows a bent path. Only the steering part of its bend is zero.
- **Exposed by:** `checks/tape-around-a-football`

### “On a ball every path bends anyway, so walking a small ring needs no steering.” · entry · `ball-does-all-the-bending`

- **Why it is tempting:** The ball bends in every direction, so it seems to do all the bending.
- **What is true:** Following the ground alone bends a path only as sharply as a straight walk around the ball's middle. A small ring bends more sharply than that, so the walker must steer to stay on it.
- **Exposed by:** `checks/small-ring-on-a-ball`

### “A surface curve's curvature is its normal curvature plus its geodesic curvature.” · working · `parts-simply-add`

- **Why it is tempting:** The bend is described as having two parts.
- **What is true:** The parts are perpendicular components of one vector, so their squares add. The curvature is the square root of the sum of their squares.
- **Exposed by:** `checks/ring-split-on-a-ball`

### “A curve that bends more sharply in space has a larger normal curvature.” · working · `normal-curvature-belongs-to-the-curve`

- **Why it is tempting:** Normal curvature is part of the curve's bend, so a sharper bend seems to give more of it.
- **What is true:** Normal curvature depends only on the curve's direction at the point. A sharper curve in the same direction is tilted away from the normal, and its normal component is the same.
- **Exposed by:** `checks/tilted-circle-claim`

### “A spiral winding around a can bends in space, so it cannot be a geodesic of the can.” · working · `spiral-must-steer`

- **Why it is tempting:** Geodesics are pictured as straight lines in space.
- **What is true:** Unrolling the can without stretching turns the spiral into a straight line, so its geodesic curvature is zero. All of its bend is normal curvature.
- **Exposed by:** `checks/spiral-tape-on-a-can`

### “Rolling a sheet changes the geodesic curvature of a circle drawn on it, because the circle's shape in space changes.” · formal · `rolling-changes-steering`

- **Why it is tempting:** The curve's curvature in space does change when the sheet is rolled.
- **What is true:** Geodesic curvature is fixed by the metric, which rolling keeps. Only the normal curvature, and with it the curvature in space, changes.
- **Exposed by:** `checks/circle-on-a-rolled-sheet`

### “If the normal curvature vanishes in some direction at a point, the surface is flat there.” · formal · `zero-normal-curvature-means-flat`

- **Why it is tempting:** Zero bending along one line looks like no bending.
- **What is true:** At the centre of a saddle the normal curvature vanishes in two directions while the Gaussian curvature is negative. Asymptotic directions exist wherever the Gaussian curvature is zero or negative.
- **Exposed by:** `checks/asymptotic-directions-at-a-saddle`

## Checks

1. **Entry · predict** `checks/tape-around-a-football`. A round football, a soccer ball, is about 70 centimetres around its middle. You press narrow masking tape onto it, starting anywhere and never pulling the roll to the left or right, so the tape never steers. Seen from the side, does the tape's path bend? Over the whole trip, until the tape gets back to its start, by how many degrees in total has its direction of travel turned?
   - **Hints:** Which way is the tape heading when it is halfway around the ball? / Which way is it heading back at its start, and did its direction jump there or turn steadily?
   - **Answer:** The path bends, and all of that bend comes from the ball. The tape never steers, so it follows a straight walk, which goes around the ball's middle. Seen from the side, it follows the ball around, so its path bends. That bend comes from the ball's surface curving away beneath the tape, so all of it is normal curvature. Halfway around, the tape heads the opposite way to its start, so its direction has turned half a turn. Back at its start it heads the way it set off, after turning steadily through one full turn, 360 degrees, over the 70 centimetres.
   - **Must contain:** The path bends; The tape does not steer, so the bend comes from the ball; Half a turn by halfway around; One full turn, 360 degrees, in total
   - **Numeric:** turn of the tape's direction around the ball = 360 deg (magnitude, ±5)
   - **Targets:** `never-steered-so-not-bent`
   - **Visual:** [[bend-arrow-split-on-a-surface]]
2. **Entry · predict** `checks/small-ring-on-a-ball`. A basketball is about 75 centimetres around its middle. One ladybird walks once around a ring drawn around the ball's middle, cutting the ball into two equal halves. A second ladybird walks once around a small ring, 10 centimetres around, drawn around one point of the ball. Which ladybird must keep steering to stay on her ring? Why?
   - **Hints:** Which ring has the same ball on both sides? / Each lap is one full turn. Over how many centimetres is it shared on each ring?
   - **Answer:** Only the second. The ball on one side of the ring around the middle is a mirror image of the ball on the other side, so the first ladybird has no reason to steer. That ring is a straight walk, and following the ground alone keeps her on it. Each lap of either ring turns its ladybird one full turn. The small ring shares that turn over 10 centimetres instead of 75, so it turns the second ladybird about seven and a half times as sharply. Following the ground alone would take her on a straight walk around the ball's middle instead. So she must keep steering toward the point her ring goes around.
   - **Must contain:** Only the ladybird on the small ring steers; The ring around the middle is a straight walk, by mirror symmetry; The small ring turns her about seven and a half times as sharply as the ground alone
   - **Targets:** `ball-does-all-the-bending`
   - **Visual:** [[bend-arrow-split-on-a-surface]]
3. **Working · numeric** `checks/ring-split-on-a-ball`. On a ball of radius 5 cm, a ring lies in a plane 4 cm from the ball's centre, so the ring's radius is 3 cm. With the outward normal, and walking with the smaller cap on your left, find the ring's curvature, normal curvature and geodesic curvature. A student adds the sizes of the two parts to get the ring's curvature. Evaluate that.
   - **Hints:** Find the ring's colatitude from the 3-4-5 triangle. / Which combination of the two parts gives the whole curvature vector's length?
   - **Answer:** The ring is a circle of radius 3 cm, so $\kappa = 1/3$ cm$^{-1}$, pointing at the ball's axis. The ball is a sphere, so $\kappa_n = -1/5$ cm$^{-1}$ with the outward normal. The colatitude has $\sin\theta_0 = 3/5$ and $\cos\theta_0 = 4/5$, so $\kappa_g = \cot\theta_0/a = (4/3)/5 = 4/15$ cm$^{-1}$, positive because the ring bends toward the cap on the left. Check: $(1/5)^2 + (4/15)^2 = 25/225 = (1/3)^2$. The sizes add to $7/15$ cm$^{-1}$, not $5/15$, so the student is wrong: the parts are perpendicular, and only their squares add. The radii are $3$ cm in space, $5$ cm for the normal part and $3.75$ cm for the geodesic part.
   - **Must contain:** Curvature one third per centimetre; Normal curvature minus one fifth per centimetre; Geodesic curvature four fifteenths per centimetre; Squares add, not the parts
   - **Numeric:** radius of curvature of the ring in space = 3 cm (magnitude, ±0.05); reciprocal of the geodesic curvature = 3.75 cm (magnitude, ±0.05)
   - **Targets:** `parts-simply-add`
   - **Visual:** [[bend-arrow-split-on-a-surface]]
4. **Working · evaluate-claim** `checks/tilted-circle-claim`. On a sphere of radius 10 cm, a circle of radius 6 cm and a great circle touch at a point, heading the same way there. Claim: the small circle has normal curvature of size 1/6 cm$^{-1}$, because it bends more sharply than the great circle. Evaluate the claim.
   - **Hints:** Draw the right triangle formed by the sphere's centre, the circle's centre and the point.
   - **Answer:** False. The small circle's curvature is $1/6$ cm$^{-1}$, but its principal normal points at its own centre, tilted from the sphere's normal. The perpendicular from the sphere's centre to the circle's plane meets that plane at the circle's centre, so the sphere's centre, the circle's centre and the touching point form a right triangle with legs $8$ cm and $6$ cm and hypotenuse $10$ cm. Its angle at the touching point, between the ray to the circle's centre and the ray to the sphere's centre, has cosine $6/10$. The small circle's principal normal runs along the first ray, and the sphere's normal runs along the second ray or against it, because the question fixes no side, so only the size is settled: $|\cos\varphi| = 6/10$. Meusnier's theorem gives $|\kappa_n| = (1/6)(0.6) = 0.1$ cm$^{-1}$, the same as the great circle. The rest of the bend is geodesic: $|\kappa_g| = (1/6)(0.8) = 0.133$ cm$^{-1}$.
   - **Must contain:** The claim is false; The cosine of the tilt between the small circle's principal normal and the sphere's normal has size six tenths; Normal curvature one tenth per centimetre, the same as the great circle
   - **Numeric:** radius for the normal curvature = 10 cm (magnitude, ±0.1)
   - **Targets:** `normal-curvature-belongs-to-the-curve`
5. **Working · numeric** `checks/spiral-tape-on-a-can`. Narrow tape is wound around a can of radius 3.3 cm, crossing the can's length at 30° everywhere, and never bent sideways. Is its geodesic curvature zero? Find the radius of curvature of the tape's path in space.
   - **Hints:** What does the spiral become when the can is unrolled? / Around the can the principal curvature has size one over the radius; along it, zero.
   - **Answer:** Yes. Unroll the can: nothing stretches, and the tape becomes a straight line, so $\kappa_g = 0$ on the flat sheet and, because geodesic curvature depends only on the metric, on the can too. The whole bend is normal: with the outward normal, Euler's formula gives $\kappa_n = -\sin^2 30^\circ/(3.3\ \text{cm}) = -0.0758$ cm$^{-1}$, so $\kappa = 0.0758$ cm$^{-1}$ and the radius is $13.2$ cm. The helix formula agrees: pitch parameter $b = a/\tan30^\circ = 5.72$ cm gives $a/(a^2 + b^2) = 1/(4a) = 0.0758$ cm$^{-1}$.
   - **Must contain:** Unrolled, the spiral is a straight line; Geodesic curvature zero; Radius of curvature 13.2 centimetres, all from the can
   - **Numeric:** radius of curvature of the spiral in space = 13.2 cm (magnitude, ±2%)
   - **Targets:** `spiral-must-steer`
   - **Visual:** [[bend-arrow-split-on-a-surface]]
6. **Formal · explain** `checks/circle-on-a-rolled-sheet`. A circle of radius 5 cm is drawn on a flat sheet and walked counterclockwise as seen from the side the chosen normal points to. The sheet is rolled, without stretching, into a tube of radius 2 cm with that normal pointing out of the tube. Find $\kappa_g$, $\kappa_n$ and the curvature in space where the circle heads around the tube and where it heads along the tube. Which quantity is intrinsic, and why?
   - **Hints:** Which of the two quantities can be computed from the metric alone?
   - **Answer:** Rolling is an orientation-preserving local isometry, and $\kappa_g = g(\nabla_TT, JT)$ uses only $g$ and the orientation, so $\kappa_g = +0.2$ cm$^{-1}$ everywhere on the circle, before and after. $\kappa_n = -\sin^2\beta/(2\ \text{cm})$ depends on the angle $\beta$ to the tube's axis. Heading around, $\kappa_n = -0.5$ cm$^{-1}$ and $\kappa = \sqrt{0.2^2 + 0.5^2} = 0.539$ cm$^{-1}$, a radius of $1.86$ cm. Heading along, $\kappa_n = 0$ and $\kappa = 0.2$ cm$^{-1}$, a radius of $5$ cm. Only $\kappa_g$ is intrinsic.
   - **Must contain:** Geodesic curvature stays 0.2 per centimetre; Normal curvature minus 0.5 heading around, zero heading along; Curvature in space 0.539 and 0.2 per centimetre; Geodesic curvature uses only the metric and orientation
   - **Numeric:** radius of curvature in space heading around the tube = 1.857 cm (magnitude, ±2%)
   - **Targets:** `rolling-changes-steering`
7. **Formal · derive** `checks/asymptotic-directions-at-a-saddle`. For the saddle $z = (x^2 - y^2)/(2a)$ at the origin, with the normal along $+z$, find the directions with $\kappa_n = 0$. Show that such directions exist at a point iff $\kappa_1\kappa_2 \le 0$, and that a straight line lying in a surface is both a geodesic and an asymptotic curve.
   - **Hints:** Use Euler's formula and ask when a weighted average of the principal curvatures can vanish.
   - **Answer:** Here $\kappa_1 = 1/a$ along $x$ and $\kappa_2 = -1/a$ along $y$, so Euler's formula gives $\kappa_n = \cos2\phi/a$, zero at $\phi = \pm45^\circ$, while $\kappa_1\kappa_2 = -1/a^2 < 0$. In general $\kappa_1\cos^2\phi + \kappa_2\sin^2\phi = 0$ has a solution iff $\kappa_1$ and $\kappa_2$ do not share a strict sign, that is iff $\kappa_1\kappa_2 \le 0$. A straight line has constant $\mathbf T$, so $d\mathbf T/ds = 0$ and both $\kappa_n$ and $\kappa_g$ vanish; the rulings of a hyperboloid of one sheet are examples, on a surface with negative Gaussian curvature.
   - **Must contain:** Zero normal curvature at 45 degrees on the saddle; Solutions exist iff the principal curvatures do not share a strict sign; A straight line has zero curvature vector, so both parts vanish
   - **Targets:** `zero-normal-curvature-means-flat`
8. **Research · derive** `checks/photon-sphere-from-null-normal-curvature`. In Schwarzschild with $G = c = 1$ and $f = 1 - 2M/r$, take the timelike hypersurface $r = r_0$ with outward unit normal $N = \sqrt f\,\partial_r$ and $\mathrm{II}(X,Y) = g(\nabla_XY, N)$, with $g$ the spacetime metric and $h$ the induced metric on the surface. Compute $\mathrm{II}(k,k)$ for the null tangent $k = f^{-1/2}\partial_t + r_0^{-1}\partial_\theta$, find where it vanishes, and show that there $\mathrm{II} = \lambda h$.
   - **Hints:** Use $\Gamma^r{}_{ab} = -\tfrac12 g^{rr}\partial_r g_{ab}$ for $a, b \neq r$.
   - **Answer:** For tangent coordinate fields, $\mathrm{II}_{ab} = g_{rr}\Gamma^r{}_{ab}N^r = -\tfrac12\partial_rg_{ab}\sqrt f$. So $\mathrm{II}_{tt} = \tfrac12f'\sqrt f = (M/r_0^2)\sqrt f$ and $\mathrm{II}_{\theta\theta} = -r_0\sqrt f$. Then $\mathrm{II}(k,k) = (M/r_0^2)/\sqrt f - \sqrt f/r_0 = (3M - r_0)/(r_0^2\sqrt f)$, zero only at $r_0 = 3M$. There $\mathrm{II}_{tt}/h_{tt} = -(M/r_0^2)/\sqrt f$ and $\mathrm{II}_{\theta\theta}/h_{\theta\theta} = -\sqrt f/r_0$ are both $-1/(3\sqrt3\,M)$, and the $\phi$ component matches by symmetry, so $\mathrm{II} = -h/(3\sqrt3\,M)$.
   - **Must contain:** Second fundamental form components M over r squared times root f and minus r root f; Null normal curvature three M minus r over r squared root f; Totally umbilic at r equals three M with lambda minus one over three root three M

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Signs of normal and geodesic curvature | $\kappa_n = K_{\mu\nu}t^\mu t^\nu$ with $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\mathbf e_\nu$, positive toward the chosen normal; $\kappa_g$ positive toward the walker's left with the head along $\hat{\mathbf n}$, as in the course orientation convention. | Some texts define the second fundamental form with the opposite sign, or quote $\kappa_g$ as an unsigned magnitude; $\kappa^2 = \kappa_n^2 + \kappa_g^2$ holds in every convention. |
| Letters for the two parts and for Gaussian curvature | $\kappa_n$ and $\kappa_g$; $K_{\mu\nu}$ always carries indices, and a bare $K$ in the Gauss–Bonnet theorem is the Gaussian curvature. | Others write $k_n$, $k_g$, or $\kappa_\nu$ for the normal part, and some write the geodesic curvature as the tangential curvature. |

## Visuals

- ★ [[bend-arrow-split-on-a-surface]] (flagship): The central picture: a path's bend arrow split into a part toward the surface and a steering part along it. *Sketch:* A ball, a drinks can, a saddle or a flat floor with a walker on a path. Presets: a straight walk around the ball's middle, a small ring, a spiral on the can, a line through the saddle at $45^\circ$. The bend arrow splits into an arrow along the normal and an arrow along the ground to the walker's left, with dials for both and for the whole bend, and a right-triangle inset. At a fixed point, a heading dial changes only the normal arrow, following Euler's formula; a steering slider changes only the sideways arrow. An unroll button flattens the can, and the spiral's sideways arrow stays zero. It proves that the normal part belongs to the heading and the steering part to the metric.
- [[carry-an-arrow-around-a-loop]] (supporting): Integrated geodesic curvature of a latitude circle and the returned rotation add up with the enclosed curvature to a full turn. *Sketch:* Drag the latitude and play one lap. Show the arrow's returned rotation, the integrated steering $2\pi\cos\theta_0$, and the cap's curvature $2\pi(1-\cos\theta_0)$ as two arcs that close a full circle.

## Tutor moves

**Open with**

- Picture yourself setting off across a giant smooth ball and walking all the way around it, never steering left or right. Seen from far away, outside the ball, does your path bend? *(prediction)*

**If the learner is stuck**

- *The learner cannot tell which part of a bend is steering.* → Ask whether a narrow strip of tape laid along the path would crinkle: it crinkles only where the path steers. *Uses:* `ways_in/steering-bends-the-path-along-the-ground`
- *The learner gets the wrong sign for the geodesic curvature.* → Stand with the head along $\hat{\mathbf n}$, face along $\mathbf T$, and ask whether the curve bends toward the left. *Uses:* `key_equations/curvature-vector-split`, `checks/ring-split-on-a-ball`

**Common questions**

- *Is a straight walk on a ball really straight?* (entry) It is straight in a sense a walker on the ball can check: she never steers left or right. Seen from far away, outside the ball, her path bends around the ball. That bend comes entirely from the ground. So a straight walk has no steering part, but it still has a ground part. *Uses:* `ways_in/a-straight-walk-still-bends`
- *Why is it called geodesic curvature?* (working) It measures how far a curve is from being a geodesic of the surface: it is the left side of the geodesic equation, so it vanishes exactly along geodesics. *Uses:* `key_equations/geodesic-part`

**Switching levels**

- To working when: asks how big each part is; asks whether the parts add. Go to the split of the curvature vector and the ring check. *Uses:* `ways_in/split-the-bend-into-perpendicular-parts`, `checks/ring-split-on-a-ball`
- To formal when: asks which part someone living on the surface can measure. Give the Riemannian definitions, then the rolled sheet and Gauss–Bonnet. *Uses:* `ways_in/curves-on-a-hypersurface`, `checks/circle-on-a-rolled-sheet`
- To research when: asks how light can circle a black hole. Open photon surfaces and optical geometry. *Uses:* `ways_in/light-that-skims-a-sphere`, `research_horizon/photon-surfaces`

**Pronunciations:** Meusnier → muh-NYAY; Gauss–Bonnet → GOWSS bon-AY; Euler → OY-ler; geodesic → jee-uh-DESS-ik; Christoffel → kris-TOFF-el; Virbhadra → veer-BAH-drah; umbilic → um-BIL-ik

**Voice notes:** Say "kappa n" and "kappa g"; at entry, say "the ground's part" and "the steering part" before the names.

## History

- **Leonhard Euler (1767).** Studied the curvatures of the slices of a surface by planes through its normal, and showed that they take two extreme values in perpendicular directions. Leonhard Euler (1767), *Recherches sur la courbure des surfaces*, Mémoires de l'académie des sciences de Berlin 16, 119–143
- **Jean Baptiste Meusnier (1776).** Related the curvature of an oblique slice to that of the normal slice in the same direction, the theorem now written $\kappa_n = \kappa\cos\varphi$. Presented in 1776 and published in 1785. Jean Baptiste Meusnier (1785), *Mémoire sur la courbure des surfaces*, Mémoires de mathématique et de physique présentés à l'Académie royale des sciences, par divers savans 10, 477–510
- **Pierre Ossian Bonnet (1848).** Used the integrated geodesic curvature of a boundary to extend Gauss's angle-sum result to regions bounded by arbitrary curves, the local Gauss–Bonnet theorem. Pierre Ossian Bonnet (1848), *Mémoire sur la théorie générale des surfaces*, Journal de l'École polytechnique 19 (cahier 32), 1–146

## Research horizon

- **Photon surfaces and light rings.** A timelike hypersurface that traps every null geodesic starting tangent to it is totally umbilic, the statement that its normal curvature vanishes in every null direction. Uniqueness theorems for photon spheres in static vacuum spacetimes build on this, while in rotating black holes spherical photon orbits fill a photon region instead of a single surface. Light near these orbits sets the size of black-hole shadows. Clarissa-Marie Claudel, K. S. Virbhadra, G. F. R. Ellis (2001), *The geometry of photon surfaces*, Journal of Mathematical Physics 42, 818–838, doi:10.1063/1.1308507; Volker Perlick (2004), *Gravitational lensing from a spacetime perspective*, Living Reviews in Relativity 7, 9, doi:10.12942/lrr-2004-9
- **Lensing from the Gauss–Bonnet theorem.** In the optical geometry of a static spacetime, light rays are geodesics, so a region bounded by a ray and a distant circle obeys Gauss–Bonnet with zero geodesic curvature along the ray. The deflection angle then comes from integrating the optical Gaussian curvature, and later work extends the method to rotating black holes. Marek A. Abramowicz, Brandon Carter, Jean-Pierre Lasota (1988), *Optical reference geometry for stationary and static dynamics*, General Relativity and Gravitation 20, 1173–1183, doi:10.1007/BF00758937; G. W. Gibbons, M. C. Werner (2008), *Applications of the Gauss–Bonnet theorem to gravitational lensing*, Classical and Quantum Gravity 25, 235009, doi:10.1088/0264-9381/25/23/235009

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** If you walk on a giant smooth ball and never steer left or right, your path still curves round the ball when someone watches from far away outside it, because the ground keeps dropping away under your feet, so every step tips you a little toward the ball's centre. That bit of the bending is called normal curvature, and normal here means at right angles to the ground, not ordinary. Go all the way round and your direction of travel turns a whole 360 degrees; on Earth that is 1 degree every 111 kilometres, so a kilometre turns you less than a hundredth of a degree and you never notice. A ladybird on a little ring around one point has to keep steering toward that point, because her ring turns her much more sharply per centimetre than the ground alone would, and the steering part is called geodesic curvature, which is zero if you never steer. The two parts do not just add: they are at right angles, like the two short sides of a right-angled triangle.

What I could not say back. Why never steering puts me on the biggest circle rather than some smaller one: the mirror sentence tells me she has no reason to turn either way, and then the next sentence simply says her walk goes around the ball's middle, so I took that on trust. In the summary I stopped at 'That part of a path's bend' because no parts had been mentioned yet. For the second try-it I did not know whether the ring should be 10 centimetres all the way round or 10 centimetres out from the point, so I could not draw it. And 'steering bends a path sideways' - sideways compared with what? The way itself had said left or right, so I was not sure the two sentences meant the same thing.

**Stumbles (34)**

- “Walking without ever steering left or right is called walking straight.”: A teenager objects at once that a path around a ball is not straight; nothing says the name is about the walker, not the path's shape.
- “Let her walk straight around the middle of the ball.”: A ball has no middle until a circle is chosen, and nothing says why this walk needs no steering; the claim is taken on trust.
- “Seen from far out in space, her path is a circle as big as the ball.”: The huge ball was never put in space, so 'space' mixes the imagined ball with Earth; the viewpoint needs a plain reference.
- “At every step, the ground bends away beneath her, and her next step follows the ground.”: 'Bends away' gives no mechanism and no direction: the reader cannot see how following the ground turns her, or which way.
- “The part of a path's bend that comes from following the ground is called normal curvature.”: 'Normal' reads as 'ordinary'; the name is left unexplained.
- “A straight walk all the way around turns your direction of travel by one full turn, 360 degrees. Every stretch of a round ball is alike. So on Earth, the ground bends a straight walk by 1 degree for every 111 kilometres.”: Two steps left implicit: why a lap is a full turn (you come back heading the same way) and the division 40,000 by 360. Earth is also treated as a smooth ball without saying so.
- “That is far too gentle to notice on a walk.”: Rule 12: 'why don't I notice?' is answered without a number.
- “Press narrow masking tape onto a football, around its middle. Keep the tape flat against the ball, and never bend it sideways as you lay it.”: 'Football' can mean a non-round American football; 'around its middle' needs a chosen start; 'bend it sideways' is a second phrase for steering and not an action the reader can check; what to see at the end is vague.
- “The ring is much smaller than the circle around the ball's middle. So it turns her direction of travel more sharply than a straight walk would.”: A step taken on trust: that a smaller circle turns you more per metre is a prerequisite fact not restated, and the circle around the middle is not linked to a straight walk in this way.
- “Following the ground alone cannot keep her on the ring.”: Missing link: the reader is not told what following the ground alone would do instead.
- “Her steering also bends her path sideways, along the ball's surface.”: 'Sideways' has no reference, and 'bends' is used a third way beside the path's bend and the ground bending away.
- “The part of a path's bend that comes from steering is called geodesic curvature.”: 'Geodesic' is a strange word with no reason given for the name.
- “Lay narrow masking tape around a ball in a small ring. The tape's inner edge crinkles, because the tape has to bend sideways to follow the ring. Tape laid around the middle of the ball, never bent sideways, lies almost smooth.”: No ring size, 'inner edge' has no reference, the reason for crinkling is incomplete (why that edge), and 'bend sideways' again stands in for steering.
- “One bends the path toward the ground, and the other bends it sideways, at right angles to the first. So they combine like the two short sides of a right triangle, whose long side is the whole bend.”: Reread: 'toward the ground' does not match the ball's-centre direction of the explanation, 'sideways' has no reference, and 'combine like the short sides' leaves the reader unsure what is the whole bend.
- “Seen from outside, by how many degrees has the tape's direction turned when it gets back to where it started?”: Rule 10: back at its start the tape heads the way it set off, so a careful reader answers 0 degrees, which the check marks wrong; 'Does the tape steer?' is also answered by the question itself.
- “The ring around the middle is a straight walk, so following the ground alone keeps the first ladybird on it. The small ring is much smaller than the ring around the middle.”: Check answer rests on two steps the entry ways did not prepare (why the middle ring is straight, why smaller means sharper) and uses no specific number although the question gives 10 centimetres.
- “How far must a straight walk go for the ground to turn it as much as one metre of the cycle path turns her? (c) Is her bend mostly steering?”: Reread: 'it' and 'her' switch between the walk and the cyclist, and (c) does not name the alternative.
- “then compare a running track's steering with Earth's ground”: The running-track paragraph was dropped from the way; the tutor move points at content the note no longer has.
- “Ask whether a narrow strip of tape would crease along the path”: 'Crease' is a second word for the try-it's 'crinkle'.
- “That part of a path's bend is its normal curvature.”: Rule 11: 'that part' points at no noun. The summary has not yet said that a bend has parts, so the reader meets the word 'part' for the first time as a back-reference.
- “Steer left or right, and your path also bends sideways along the ground.”: Rules 5 and 6: 'sideways' has no reference, and 'bends' is used for the steering turn, which both entry ways carefully call turning the direction of travel to the walker's left or right.
- “The ball on her left is a mirror image of the ball on her right, so she has no reason to steer to either side. Seen from far away, outside the ball, her straight walk goes around the ball's middle, along a circle as big as the ball.”: Rule 3: the step from 'no reason to steer to either side' to 'a circle as big as the ball' is left for the reader to supply, with no connective between the two sentences. The first what-if a teenager tries is 'why not a smaller circle?', and the note does not answer it.
- “It bends, seen from outside, because the ground curves away beneath each step.”: Rule 6: 'seen from outside' gives no reference (outside what?), and it breaks the note's own fixed phrase 'seen from far away, outside the ball'. 'It' also has the ball as a rival antecedent.
- “That part of a path's bend is called normal curvature.”: Same back-reference as in the summary, inside the recap, where a reader arriving straight at this way meets it first.
- “Draw a ring about 10 centimetres around one point on a football, and press narrow masking tape along it.”: A rule the reader cannot follow: '10 centimetres around one point' reads equally well as 10 centimetres out from the point, which is a ring almost as big as the ball. 'Along it' also has the football and the point as rival antecedents.
- “Steering bends a path sideways along the ground; that part of the bend is geodesic curvature, and a straight walk has none.”: The takeaway keeps the wording the explanation was rewritten to avoid: 'sideways' with no reference, and 'bends' for steering. A reader who says this sentence back has not said what the way taught.
- “The part of a path's bend that comes from following the ground as the ground curves away beneath it. Here normal does not mean ordinary: it means at right angles to the surface, the way this part tips the path.”: 'Beneath it' can be the path or the bend (rule 11), and the trailing clause 'the way this part tips the path' has to be read twice to see that it explains 'at right angles'.
- “The ground turns a straight walk 1 degree every 111 kilometres. So turning it 2.86 degrees takes 2.86 times 111, about 317 kilometres.”: 'Turning it' can be the straight walk, the ground or the direction of travel, and a walk is not the thing that turns (rule 11).
- “One metre of her path turns her as much as 317 kilometres of ground would.”: '317 kilometres of ground' is not a thing the reader can picture, and 'turns her' hides what turns: her direction of travel, not the cyclist herself.
- “Picture walking all the way around the middle of a giant smooth ball, never steering left or right.”: The opener is spoken before any way, and a ball has no middle until a circle is chosen, so the reader is asked to picture a place the note has not yet given her. It also hands over the setting that the way is about to derive.
- “Following the ground alone bends a path only as sharply as the ball bends.”: 'The ball bends' is a third sense of bend beside a path bending and a walker steering, and it gives the reader nothing to picture to compare the ring with.
- “That bend comes from the ball's surface curving away beneath the tape, which is normal curvature.”: 'Which' sits next to 'the tape', so the sentence can be read as saying the tape is normal curvature.
- “The ladybird in 'Steering bends the path along the ground' bent for two reasons, one toward the ground and one sideways; resolving a vector makes the split exact.”: Ladder read: the ladybird did not bend, her path did; 'toward the ground' is not what the entry way says (it says her direction tips toward the ball's centre); and 'sideways' is the word the entry text was cleared of, so the bridge back does not match the way it names.
- “The ground's part tips her direction toward the ball's centre, and the steering part turns it to her left or right, at right angles to the first.”: Read in place, this sentence follows a takeaway that speaks to 'your direction of travel', so 'her direction' arrives with no owner in sight (rule 11). The same sentence also runs to 32 words and puts 'her right' next to 'right angles', two senses of right in one breath (rule 5).

**Fixes**

- Straight-walk way: backed the claim that a straight walk needs no steering with the mirror reason, defined 'the ball's middle' as a circle as big as the ball, gave the step-by-step reason the ground tips her direction toward the ball's centre, spelled out the full-turn and 40,000-divided-by-360 steps, and added the 1-kilometre number for why nobody notices.
- Steering way: recap now restates that a straight walk goes around the middle and that a smaller circle turns you more per metre; the explanation says what following the ground alone would do and gives 'left or right' as the reference for steering; try-it and simplifies reworded as recorded.
- Word discipline: the ground 'curves away' (summary, takeaway, recap, misconception correction), the path 'bends', and the walker or tape 'steers'; 'bend sideways', 'crease' and 'far out in space' are gone from entry text.
- Entry checks: tape check asks for the total turn, removing the 0-versus-360 ambiguity, and drops the self-answering steering question; ring check gives 75 and 10 centimetres, the mirror reason and the seven-and-a-half-times comparison. Hints and key points follow. Cycle-path problem (b) and (c) reworded; numbers unchanged (360/126 = 2.857 degrees per metre, times 111 = 317 km; 75/10 = 7.5).
- Glossary: added 'geodesic'; 'walk straight', 'normal curvature' and 'geodesic curvature' now carry the reasons for their names.
- Budget: entry explanations reached 491 words after the fixes, over the 440 allowance. Moved three name explanations out of the explanations into the glossary rather than compressing anything: why 'walking straight' names the walker's action, what 'normal' means, and where 'geodesic' comes from. Entry is now 419 of 400 (within the 10% review allowance, used only for the recorded fixes); tutoring 3004 of 3500; extras 616 of 800.
- Ladder: working way 'Split the bend' now bridges the entry unit (one radian is 57.3 degrees, so 1/(6371 km) is the entry 1 degree per 111 km) and states the cylinder's principal curvatures before using Euler's formula, which otherwise first appears at the formal rung. Every non-entry way's first sentence already names the way it continues; the six ways use six different kinds.
- Tutor-facing: teaching-arc move no longer points at the dropped running-track paragraph; if-stuck move uses 'crinkle'.
- Bumped the revision to 2.
- SECOND FULL NOVICE READ (revision 4 read, revision 5 written). Stumbles 20 to 34 above and the fixes in this block come from this read; stumbles 1 to 19 and the fixes above them are the first read (revision 1 to 2), kept so nothing is lost.
- Summary rewritten so no sentence points back at a 'part' that has not been named, and so the steering sentence uses the ways' own words: the direction of travel turns to your left or right along the ground. Four sentences, average 19 words.
- Straight-walk way: added the missing step between the mirror reason and the circle. Her path stays on the line where the two equal halves meet, and that line, seen from far away outside the ball, is a circle as big as the ball. This is the only entry-explanation change; entry is 431 words of the 400 cap, inside the 10 percent review allowance and used only for this recorded fix.
- Steering way: recap now says 'seen from far away, outside the ball' and names the part by what it comes from; the try-it says the ring is about 10 centimetres all the way round, going around one point, and presses the tape 'along the ring'; the takeaway drops 'sideways' for 'to your left or right along the ground'.
- Glossary 'normal curvature': 'beneath it' is now 'beneath the path', and the at-right-angles explanation is its own sentence, contrasted with the walker's left or right.
- Entry check and problem: the tape answer no longer lets 'which' attach to the tape; the cycle-path solution names the cyclist's direction of travel and compares against kilometres of straight walking, not 'kilometres of ground'.
- Tutor-facing entry text: the opening question lets the reader set off in any direction instead of naming the ball's middle before the way defines it; the 'ball does all the bending' correction compares the ring with a straight walk around the ball's middle instead of saying 'the ball bends'.
- Ladder: the working way's bridge sentence now says the ladybird's path bent, at right angles to the ball's surface and along it, matching the entry wording it continues. The other non-entry ways each still name the way they continue in their first sentence, no rung uses notation from above it, and the six ways keep six different kinds.
- Budgets after the fixes: entry 431 of 400 (review allowance 440), extras 668 of 800, tutoring 3029 of 3500, support 1969 of 2500, links 617 of 1000, total 7979 of 10500. Nothing was dropped or compressed.
- Bumped the revision to 5 and set the status back to novice-reviewed.
- Steering way, what-this-leaves-out: named the ladybird's direction of travel instead of 'her direction', split the 32-word sentence in two, and said 'at ninety degrees to the first' so that 'right' is not used for a direction and for an angle in the same sentence.

**Concerns**

- This read changed 12 learner-visible strings (11 entry, 1 working), so review.physics, which covers revision 4, now needs a diff check of exactly those strings. The one that carries a physical claim is the new entry sentence 'Her path therefore stays on the line where those two equal halves meet': the mirror plane through her position, her heading and the ball's centre cuts the ball in a circle as big as the ball, which the physics record already verified for revision 2, but the sentence itself is new.
- review.novice now holds two reads. Its retell_attempt is this read's; the first read's retell is only in the snapshot scratchpad/snapshots/notes-curvature/normal-curvature.before-novice.json, because the note is still untracked in git. Committing the curvature notes would make these records recoverable.
- Still open from the earlier reads: course-conventions.md fixes no sign for the second fundamental form, for normal curvature or for geodesic curvature of a curve in a surface, and does not say that a bare K in Gauss-Bonnet is the Gaussian curvature. The note sets these in notation_traps, consistently with second-fundamental-form.json, but they should be promoted into the conventions file rather than living note-locally.
- The registry lists only second-fundamental-form and curvature-of-a-curve as prerequisites, while the note also needs geodesic, levi-civita-connection and connection-one-forms; sync_registry.py should apply it. There is still no geodesic concept note, so the glossary entries 'walk straight' and 'geodesic' have nothing to align with yet.
- Both visuals are still proposals. bend-arrow-split-on-a-surface is this note's flagship and is cited by both entry ways, both entry checks and two teaching-arc steps, so the entry rung currently teaches without a picture. When it is built it must use this note's words: steer, the ground curves away, seen from far away outside the ball.
- analogies and worked_examples are both empty. An advanced note is not required to have either, but the entry rung then rests on two ways, two checks and one problem. An analogy from a setting no way uses, for example a car's tyre grip against the load the road carries, would fit inside the tutoring budget if a writer wants one; I did not add content that would need a fresh physics check.

**Re-read** (2026-09-13, revision 4): 3 stumbles in 5 changed passages

- “Both edges of the tape are the same length, but the line its edge nearer that point must follow is shorter than the line for its other edge.”: The phrase 'the line its edge nearer that point must follow' has to be read twice to parse, and the sentence packs two facts (equal edges, unequal lines) into 25 words.
- “the line its edge nearer that point must follow”: 'That point' refers to 'one point' two sentences back, with the ring in between as another candidate (rule 11).
- “So that nearer edge has too much tape, and it crinkles.”: 'It' could be the edge or the tape, and 'too much tape' does not say too much for what.
- Fix: Steering try-it: split the equal-edges sentence into two, named 'the point the ring goes around' instead of 'that point', said the extra tape is more than the edge's line needs, and replaced 'it' with 'that edge'. The claim (equal edges, shorter line for the nearer edge, nearer edge crinkles) is unchanged.
- Fix: Common answer 'a sense a walker can check' and the two French history titles read without stumbles; titles are exact reference metadata and were left as they are.

**Re-read** (2026-09-13, revision 7): 2 stumbles in 3 changed passages

- “The foot of the perpendicular from the sphere's centre to the circle's plane is the circle's centre, so $|\cos\varphi| = 6/10$.”: The 'so' hides three steps: that the three points make a right triangle with legs 8 cm and 6 cm and hypotenuse 10 cm, that the angle at the touching point is the one whose cosine is 6/10, and why only the size of the cosine follows. The hint tells the reader to draw the triangle, but the answer is meant to be a chain of because-steps, and I had to build the triangle myself to see where 6/10 came from.
- “The tilt's cosine has size six tenths”: Read on its own in the key-point list, 'the tilt' has no referent: tilt of what away from what. The list item also has to carry the reason for 'size', which the answer now gives, so the noun has to be exact.
- Fix: Check tilted-circle-claim, answer: replaced the one-clause jump to the cosine with the three steps a reader has to supply - the right triangle (legs 8 cm and 6 cm, hypotenuse 10 cm), its angle at the touching point, and the free choice of surface normal that leaves only the size fixed. Every number and the conclusion $|\cos\varphi| = 6/10$ are unchanged; the Meusnier line, $|\kappa_n| = 0.1$ and $|\kappa_g| = 0.133$ per centimetre were not touched.
- Fix: Check tilted-circle-claim, key_points[1]: named what is tilted from what instead of the bare noun 'the tilt'. Same claim, same size.
- Fix: Nothing dropped: the support bucket for checks and tutoring text had room, so the added steps cost no other item.

**Re-read** (2026-09-13, revision 8): 0 stumbles in 3 changed passages

- Fix: Sign-off, no edit to learner-visible text. Both changed strings swap one noun phrase, from the curve to the small circle. The check puts two curves in play, the small circle and the great circle, so the new noun points at exactly one of them, and it is the name the question and the rest of the answer already use.
- Fix: Answer sentence: The small circle's principal normal runs along the first ray. The first ray and the second ray are named in the sentence before, as the ray to the circle's centre and the ray to the sphere's centre, in that order, so the chain from the right triangle to the size of the cosine still holds together with nothing to supply.
- Fix: key_points[1] read standalone: it now says whose principal normal is tilted from what, so a grader reading only the list cannot match it to the great circle, whose principal normal lies along the sphere's radius.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Entry: a walker who never steers on a ball is mirror-symmetric about the plane through her position, her heading and the centre, so she has no reason to steer and follows a circle as big as the ball.: Reflection in that plane is an isometry fixing the starting point and heading; by uniqueness of geodesics the path lies in the plane, a great circle. → Correct for any start and any heading on a round ball.
- Entry mechanism: a step along the ground where she stands would leave the ball, so her direction tips toward the ball's centre.: The tangent line lies outside the sphere except at the touching point; the curvature vector of a great circle points at the centre. → Correct, with the right direction.
- Entry numbers: 40,000 km / 360 = 111 km per degree; under one hundredth of a degree per km; working bridge 6371 km x pi/180 = 111.19 km.: python → 111.1 km; 1/111 = 0.0090 degree per km; 111.19 km. Correct.
- Entry: a straight walk all the way around turns the direction of travel through one full turn and comes back heading the way it set off; halfway round it heads the opposite way.: The unit tangent of a planar circle rotates once in its plane. → Correct.
- Try-it: tape laid on a 68-70 cm soccer ball without in-plane bending returns to its start lined up with it.: A narrow inextensible strip pressed onto a surface without in-plane bending has a centreline of zero geodesic curvature, a geodesic; on a sphere every geodesic is a closed great circle of length equal to the circumference (size-5 ball 68-70 cm). → Correct in the ideal; a real ball is slightly faceted, which the entry wording tolerates.
- Try-it: tape along a ring 10 cm around on a football crinkles on its edge nearer the ring's centre point.: Ball radius 70/2pi = 11.1 cm, ring radius 1.59 cm; kappa = 0.628 /cm, |kappa_n| = 0.090 /cm, kappa_g = 0.622 /cm toward the centre point. The line for the nearer edge is shorter by about the tape width times kappa_g per unit length. → The claim is true, but the rev-2 reason said the tape's nearer edge 'is shorter', which would make it stretch, not crinkle. Fixed: both tape edges are equally long, the line for the nearer edge is shorter, so that edge has too much tape.
- Entry check: basketball 75 cm around; ring 10 cm around turns the ladybird 7.5 times as sharply; she must steer toward the ring's centre point.: Size-7 basketball circumference 29.5 in = 74.9 cm; 75/10 = 7.5; kappa > |kappa_n| = 1/a forces kappa_g != 0, pointing into the smaller cap. → Correct.
- Entry check: tape turns 360 degrees in total over the 70 cm, half a turn by halfway.: As for the full-turn claim. → Correct; tolerance 5 degrees fine.
- Problem cycle-path-on-earth: 360/126 = 2.857 degrees per metre; times 111 km = 317 km; almost all steering.: python → 2.857 deg/m; 317.5 km (using 111.1). Tolerances 0.1 deg and 3 percent cover it. Correct.
- Working split dT/ds = kappa_n n + kappa_g u with u = n x T to the walker's left, kappa^2 = kappa_n^2 + kappa_g^2, Meusnier kappa_n = kappa cos(phi).: Re-derived from T.T = 1 and the orthonormal frame (T, u, n); checked n = z, T = x gives u = y, the walker's left with head along n; conventions orientation row. → Correct; both signs flip with n, as stated.
- Derivation split-of-the-bend: chain rule and Gauss formula give kappa_n = K_{mu nu} t^mu t^nu and kappa_g u = (dt^lambda/ds + Gamma t t) e_lambda.: Hand derivation using the Gauss formula row of the second-fundamental-form note, K_{mu nu} = n . d_mu e_nu. → Correct; sign convention matches that note (sphere, outward normal, K_{mu nu} = -g_{mu nu}/a).
- Sphere: kappa_n = -1/a outward; circle at colatitude theta0 walked eastward has kappa_g = cot(theta0)/a, positive toward the North Pole on the walker's left; cylinder kappa_n = -sin^2(beta)/a.: kappa_g^2 = 1/(a sin)^2 - 1/a^2; direction from resolving the axis-pointing curvature vector; Euler's formula with principal curvatures 0 and -1/a. → Correct.
- Hilltop: R = 200 m, v = 15 m/s: v^2 kappa_n = -1.13 m/s^2, push 8.69 m/s^2 (11 percent drop); kappa_g = 1/50 m gives 4.5 m/s^2; total 4.64 m/s^2, radius 48.5 m; lift-off below v^2/g = 23 m.: python → 1.125, 8.685, 11.5 percent, 4.5, 4.638, 48.51 m, 22.9 m. Correct.
- Problem skateboard-bowl: kappa_n = +1/3 m^-1, kappa_g = +0.192 m^-1 toward the lowest point, v = 6.64 m/s, push 19.62 m/s^2 = 2g; squares check 17.0 m/s^2.: python with explicit vectors: n = (-sin60, cos60), horizontal inward curvature vector resolved along n and down the wall; Newton's law along n and along the wall. → 0.3333, 0.19245 (down the wall, so positive with the lowest point on the left), v^2 = 44.145, v = 6.644, P = g/cos60 = 19.62, v^2/rho = 16.99 = hypot(14.72, 8.50). Correct.
- Check ring-split-on-a-ball: kappa = 1/3, kappa_n = -1/5, kappa_g = 4/15 cm^-1; squares add; sizes add to 7/15; radii 3, 5, 3.75 cm.: python → 1/25 + 16/225 = 1/9. Correct.
- Check tilted-circle-claim: cos(phi) = 6/10, |kappa_n| = 0.1, |kappa_g| = 0.133 cm^-1.: Right triangle with sides 6, 8, 10; python. → Correct; 0.1^2 + 0.1333^2 = (1/6)^2.
- Check spiral-tape-on-a-can: kappa_g = 0, kappa_n = -0.0758 cm^-1, radius 13.2 cm; helix b = 5.72 cm gives a/(a^2+b^2) = 1/(4a).: python; isometric unrolling of the cylinder. → 0.07576 /cm, 13.20 cm, b = 5.716 cm. Correct.
- Formal Gauss formula, kappa_g = g(nabla_T T, JT), intrinsic up to orientation, geodesic iff kappa_g = 0, geodesic of M iff also kappa_n = 0, asymptotic directions iff kappa1 kappa2 <= 0, indefinite case epsilon II(T,T) N.: Hand derivation; normal component of a vector is g(V,N)/g(N,N) N. → Correct.
- Derivation geodesic-curvature-from-the-frame-angle: kappa_g = theta' + omega(T), d omega = -K dA, local Gauss-Bonnet.: Product rule with nabla e1 = omega e2, nabla e2 = -omega e1; unit sphere with e1 = theta-hat, e2 = phi-hat, theta-hat x phi-hat = outward r-hat, nabla_phi theta-hat = cos(theta) phi-hat, so omega = cos(theta) d phi and d omega = -dA. → Correct; signs consistent with the course orientation row.
- Holonomy of a closed smooth loop is -oint kappa_g ds mod 2 pi.: Parallel V has frame angle rate -omega(T); T has rate kappa_g - omega(T); relative angle rate -kappa_g. Compared with the holonomy note: 2 pi - oint kappa_g - sum epsilon. → Correct on an oriented surface; an orientation-reversing loop on a Mobius band returns a reflection. Scope added to the formal sentence and to the related entry for holonomy.
- Problem gauss-bonnet-from-the-frame-angle (c): oint kappa_g = 2 pi cos45 = 4.443 rad, iint K = 1.840 rad, holonomy 105.44 degrees toward the left.: python → 4.4429, 1.8403, 105.4416 degrees; matches the holonomy note's RK4 value. Correct.
- Check circle-on-a-rolled-sheet: kappa_g = +0.2 /cm, heading around kappa_n = -0.5, kappa = 0.539, radius 1.857 cm; heading along kappa = 0.2, radius 5 cm.: python; circle diameter 10 cm is less than the tube circumference 12.57 cm, so it does not overlap. → Correct.
- Check asymptotic-directions-at-a-saddle: kappa_n = cos(2 phi)/a, zero at 45 degrees; straight lines are geodesic and asymptotic.: Second derivatives of z = (x^2 - y^2)/2a at the origin; the lines x = +-y, z = 0 lie in the saddle. → Correct.
- Research: II_ab = -(1/2) sqrt(f) d_r g_ab, II(k,k) = (3M - r0)/(r0^2 sqrt f), totally umbilic at 3M with lambda = -1/(3 sqrt3 M).: Hand derivation with Gamma^r_ab = -(1/2) f d_r g_ab; python check at r0 = 5M (component sum -0.10328 equals formula) and at 3M (both ratios -0.19245/M). → Correct; sign agrees with the course convention (outward normal on a sphere gives negative II).
- Research: symmetric form vanishing on all null vectors of a Lorentzian h is proportional to h; photon surface iff totally umbilic (Claudel, Virbhadra, Ellis).: Checked in 2D by hand (Q_tx = 0, Q_tt = -Q_xx); theorem statement confirmed from the arXiv abstract record. → Correct.
- Problem optical-circle-at-three-m: Gamma^r_phiphi = -(r - 3M), optical kappa_g = (r0 - 3M)/r0^2 toward the hole, 1/r0 at M = 0.: Hand derivation: d_r(r^2/f) = 2(r - 3M)/f^2; unit tangent sqrt(f)/r0 d_phi; |d_r| = 1/f. → Correct.
- Gyroscope: spatial circle kappa_g = sqrt(1 - 2M/r)/r, holonomy 2 pi [1 - sqrt(1 - 2M/r)] ~ 2 pi M/r in the loop's sense, two thirds of 2 pi [1 - sqrt(1 - 3M/r)].: Spatial metric dr^2/f + r^2 d phi^2: Gamma^r_phiphi = -r f, |d_r| = 1/sqrt f; python ratio at r = 7013 km. → Correct; ratio 0.66667.
- Observation GP-B: 0.82 mas per orbit spatial, 4.4 of 6.6 arcsec per year; measured -6601.8 +- 18.3 against -6606.1 mas/yr.: python with GM = 3.986e14, r = 7013 km (period 97.4 min); WebSearch of the PRL abstract. → 0.820 mas/orbit, 4.43 and 6.64 arcsec/yr; published values confirmed (quoted as magnitudes, the paper gives negative drift rates).
- Observation M87: ring 42 +- 3 microarcseconds, M = (6.5 +- 0.7) x 10^9 solar masses at 16.8 Mpc; 2 sqrt27 GM/(c^2 D) = 39.7 microarcseconds.: WebSearch of the EHT paper I abstract; python. → Confirmed; 39.70 microarcseconds. Correct.
- References: Everitt et al. 2011 PRL 106 221101 (arXiv 1105.3456); EHT Collaboration (Akiyama et al.) 2019 ApJL 875 L1; Claudel, Virbhadra, Ellis 2001 JMP 42 818; Perlick 2004 LRR 7 9; Abramowicz, Carter, Lasota 1988 GRG 20 1173; Gibbons and Werner 2008 CQG 25 235009; Euler 1767 Mem. Acad. Berlin 16, 119-143.: WebSearch of publisher, arXiv, ADS and Euler Archive records. → All confirmed; added DOIs 10.3847/2041-8213/ab0ec7, 10.1063/1.1308507, 10.12942/lrr-2004-9, 10.1007/BF00758937, 10.1088/0264-9381/25/23/235009 and arXiv 1906.11238, 1010.3416; set verified.
- History: Meusnier presented 1776, published 1785; Bonnet 1848 introduced integrated geodesic curvature into the local Gauss-Bonnet theorem.: WebSearch: Meusnier, Mem. div. savans 10 (1785) 477-510; Bonnet, J. Ec. Polytech. 19 (1848) 1-146. → Confirmed; added both primary works as verified references. Bonnet also proved bending invariance of geodesic curvature (independently of Minding), which the history entry does not need to claim.
- SECOND FULL PHYSICS READ, revision 5 to 6. Entries below this marker belong to this read; entries above it are the first read (revision 2 to 3), and diff_checks holds the revision 3 to 4 check.: Every equation and derivation step re-derived from scratch, every number recomputed with python3, every reference re-confirmed, and a diff check of the 13 learner-visible strings the second novice read changed (note_diff.py against the revision-5 snapshot). → No error found in the changed strings. Two scope fixes made elsewhere, listed in fixes.
- Changed entry sentences: 'Her path therefore stays on the line where those two equal halves meet. Seen from far away, outside the ball, that line is a circle as big as the ball, going around the ball's middle.': Reflection in the plane through the walker's position, her heading and the ball's centre is an isometry of the round ball that fixes her starting point and her starting direction. A non-steering path from a given point and direction is unique, so the reflection maps it to itself and it lies in the fixed set. On the surface that fixed set is the intersection of the plane with the sphere: a great circle, of the ball's own radius, whose plane passes through the centre. → True for any starting point and any starting direction on a round ball. 'A circle as big as the ball' is exact, since a great circle has the ball's radius. The only looseness is that the two solid halves meet along a flat disk whose boundary is the line meant; the following sentence names that line, so the reader is not left with the disk.
- Changed summary, opening question, and the reworded recap, takeaway, simplifies and try-it of the two entry ways.: Each sentence tested against the first what-ifs: a flat floor, a bigger ball, walking the other way round a ring, walking backwards, a ring past the ball's middle, and a bent but flat surface. → All true within their stated setting. 'A walk that never steers has none' is the definition of geodesic curvature and holds on any smooth surface. 'Steer to your left or right, and your direction of travel also turns along the ground' is the statement that steering makes kappa_g non-zero, correct. Every claim of a bend is tied to a round ball, so the floor and the rolled sheet are not counterexamples.
- Changed glossary entry: normal curvature 'tips the direction of travel at right angles to the ground, not to the walker's left or right'.: The normal part of d T by d s is kappa_n times n-hat, along the unit normal, which is at right angles to the tangent plane; the left-right part is kappa_g times u-hat, with u-hat = n-hat cross T lying in the tangent plane. → Correct, and it separates the two directions exactly as the split does.
- Changed misconception correction: 'Following the ground alone bends a path only as sharply as a straight walk around the ball's middle.': On a sphere of radius a, with either normal, the size of kappa_n is 1/a in every direction, which is exactly a great circle's curvature. Counterexample tried: on an egg or a saddle kappa_n varies with direction, so the sentence would be false there. → True on a round ball, and both the belief and its correction are stated for a ball, so the scope holds.
- Changed check answer: 'That bend comes from the ball's surface curving away beneath the tape, so all of it is normal curvature.': Tape laid without steering has kappa_g = 0, so kappa equals the size of kappa_n. → Correct; 'all of it' is exact, not an approximation.
- Changed problem solution steps in cycle-path-on-earth (steps 3 and 4); the numbers 2.86 degrees per metre, 111 km per degree and 317 km are unchanged.: python3: 360/126 = 2.857 degrees per metre; 2.857 times 111 = 317.1 km, and 317.7 km with 111.19 km per degree. Compared kappa = 2 pi/126 m = 0.0499 per metre with the size of kappa_n = 1/6371 km = 1.57e-7 per metre. → Correct. 'Almost all of her bend comes from steering' is right by a factor of about 3 times 10 to the fifth. The stated tolerances, 0.1 degree and 3 percent, cover both roundings.
- Changed working sentence: the ladybird's path 'bent for two reasons, one at right angles to the ball's surface and one along it; resolving a vector into perpendicular parts makes the split exact'.: Since T dotted with T is 1, d T by d s is orthogonal to T, so it lies in the plane spanned by n-hat and u-hat = n-hat cross T, which are orthogonal to each other. → Correct. The new wording names the two directions accurately, and 'exact' is justified because the frame is orthonormal.
- Working split and Meusnier: d T by d s = kappa_n n-hat + kappa_g u-hat with u-hat = n-hat cross T to the walker's left; kappa squared = kappa_n squared + kappa_g squared; kappa_n = kappa cos(phi); kappa_n = K_{mu nu} t^mu t^nu.: Re-derived from T dotted with T = 1 and the Gauss formula d_nu e_mu = Gamma^lambda_{nu mu} e_lambda + K_{nu mu} n-hat. Checked the frame with n-hat = z-hat and T = x-hat, which gives u-hat = y-hat, the walker's left. Checked K_{mu nu} = n-hat dotted with d_mu e_nu on a sphere of radius a with the outward normal: d_theta e_theta = -a r-hat gives K_{theta theta} = -a = -g_{theta theta}/a. → Correct, and identical to the sign row of the second-fundamental-form note. Both kappa_n and kappa_g flip when n-hat is reversed, as the conditions say.
- Sphere and cylinder values: kappa_n = -1/a with the outward normal; a latitude circle walked eastward has kappa_g = cot(theta0)/a, positive in the northern hemisphere; a cylinder has kappa_n = -sin squared(beta)/a; Earth's 1/6371 km is 1 degree per 111 km.: python3: kappa_g squared = 1/(a sin theta0) squared minus 1/a squared; 6371 km times pi/180 = 111.19 km per degree; 40000/360 = 111.11 km per degree; Euler's formula with principal curvatures 0 and -1/a. → Correct, and the entry and working figures agree to three significant figures. Walking east with the outward normal puts north on the walker's left, so cot(theta0) greater than zero has the right sense, and the equator gives zero.
- Working hilltop numbers: v squared kappa_n = -1.13 m/s^2, road push 8.69 m/s^2 (11 percent below 9.81), v squared kappa_g = 4.5 m/s^2, whole acceleration 4.64 m/s^2, radius of curvature 48.5 m, and lift-off below v squared over g = 23 m.: python3 with v = 15 m/s, crest radius 200 m in every direction, kappa_g = 1/50 m and g = 9.81 m/s^2. → 1.125, 8.685, 11.47 percent (quoted as 11 to two figures), 4.500, 4.6385, 48.51 m and 22.94 m. Correct. The vertical reading is independent of the steering because the crest is umbilic, which is the reason the text gives.
- Problem skateboard-bowl: kappa_n = +1/3 per m, kappa_g = +0.192 per m toward the lowest point, v = 6.64 m/s, bowl push 19.6 m/s^2 equal to twice g, and the quadrature check 17.0 m/s^2.: python3 with explicit vectors: bowl centre at the origin, rider at a times (sin 60, 0, -cos 60), n-hat toward the centre, and the horizontal curvature vector of size 1/rho pointing at the vertical axis, resolved along n-hat and down the wall; then Newton's law in both directions. → rho = 2.598 m, kappa_n = 0.3333, kappa_g = 0.19245 with the lowest point on the left, v squared = 44.145 m^2/s^2, v = 6.644 m/s, P = g over cos 60 = 19.62 m/s^2 exactly twice g, and v squared over rho = 16.99 = hypot(14.72, 8.50). Correct.
- Checks ring-split-on-a-ball, tilted-circle-claim, spiral-tape-on-a-can, circle-on-a-rolled-sheet and asymptotic-directions-at-a-saddle.: python3 and hand algebra: the 3-4-5 triangle on a 5 cm ball; the 6-8-10 triangle on a 10 cm sphere; a helix of radius 3.3 cm at 30 degrees to the axis; a 5 cm circle rolled onto a 2 cm tube; second derivatives of z = (x squared minus y squared) over 2a at the origin. → kappa = 1/3, kappa_n = -1/5, kappa_g = 4/15 with (1/5) squared plus (4/15) squared = (1/3) squared, radii 3, 5 and 3.75 cm. Sizes 0.1 and 0.1333 per cm with 0.1 squared plus 0.1333 squared = (1/6) squared. Helix b = a over tan 30 = 5.716 cm, a over (a squared plus b squared) = 1 over 4a = 0.07576 per cm, radius 13.20 cm, matching Euler's minus sin squared 30 over a. Rolled circle 0.539 per cm and radius 1.857 cm heading around, 0.2 per cm and 5 cm heading along, with its 10 cm width fitting the tube's 12.57 cm circumference. Saddle kappa_n = cos(2 phi)/a, zero at 45 degrees, Gaussian curvature minus 1 over a squared. All correct.
- Formal way: Gauss formula, kappa_g = g(nabla_T T, JT), intrinsic-ness, geodesic iff kappa_g vanishes, asymptotic directions iff kappa1 kappa2 is zero or negative, local Gauss-Bonnet, and holonomy equal to minus the integrated geodesic curvature modulo two pi.: Re-derived kappa_g = theta-prime plus omega(T) from nabla e1 = omega e2 and nabla e2 = minus omega e1. Checked d omega = -K dA on the unit sphere with e1 = theta-hat, e2 = phi-hat and the outward normal, where nabla_phi theta-hat = cos(theta) phi-hat gives omega = cos(theta) d phi. Checked local Gauss-Bonnet on a polar cap, where two pi (1 minus cos theta0) plus two pi cos theta0 equals two pi with no corners. Checked the holonomy statement directly, without a frame: a parallel vector's angle to T changes at rate minus kappa_g, and T returns to itself on a smooth closed loop. → All correct, and the holonomy sign matches the course orientation row, where positive is toward the walker's left: minus the integral of kappa_g equals two pi minus the integral of K dA, which is congruent to the integral of K dA modulo two pi. The degenerate flat point, where both principal curvatures vanish, satisfies the non-strict inequality and has every direction asymptotic, so the stated criterion holds there too.
- Problem gauss-bonnet-from-the-frame-angle (c): the integrated geodesic curvature is two pi cos 45 = 4.443 rad, the integrated Gaussian curvature is 1.840 rad, and the holonomy is 105.44 degrees toward the walker's left.: python3. Note that at 45 degrees two pi cos(theta0) and two pi sin(theta0) coincide numerically, so the general form two pi cos(theta0) was re-derived and checked at other colatitudes as well. → 4.4429 and 1.8403 rad, summing to 6.2832 = two pi; 254.56 plus 105.44 equals 360 degrees; the holonomy minus 4.4429 rad is congruent to plus 1.8403 rad, that is 105.44 degrees, inside the stated modulo of 360. Correct.
- Research: a timelike hypersurface is a photon surface exactly when it is totally umbilic; in Schwarzschild the second fundamental form on the null tangent built from the t and theta directions is (3M minus r0) over (r0 squared root f); at r0 = 3M the form is minus h over three root three M.: Hand derivation with N = root f times d_r, II_ab = minus one half root f times d_r g_ab, Gamma^r_tt = f M over r squared and Gamma^r_theta theta = minus r f; checked that k is null and tangent to the surface; python3 for the two ratios at r0 = 3M. → II(k,k) = M over r0 squared root f, minus root f over r0, which is (3M minus r0) over (r0 squared root f), zero only at r0 = 3M for r0 greater than 2M. Both II_tt over h_tt and II_theta theta over h_theta theta equal minus 0.19245 over M, that is minus one over three root three M. Correct.
- Research: optical geodesic curvature (r0 minus 3M) over r0 squared toward the hole; gyroscope circle kappa_g = root(1 minus 2M over r) over r with holonomy two pi times one minus that root, about two thirds of geodetic precession; Gibbons-Werner deflection 4M over b.: Hand derivation in both metrics, the optical d r squared over f squared plus r squared d phi squared over f and the spatial d r squared over f plus r squared d phi squared, using Gamma^r_phi phi = minus one half g^rr d_r g_phi phi; python3 for the ratio; and an explicit integral of the leading optical Gaussian curvature minus 2M over r cubed over the region outside the straight-line ray r = b over sin(phi). → Optical kappa_g = (r0 minus 3M) over r0 squared, inward for r0 greater than 3M, zero at 3M, reversed inside it, and 1 over r0 when M is zero. Spatial kappa_g = root f over r gives holonomy two pi (1 minus root f), positive, hence in the traversal sense; its ratio to two pi times one minus root(1 minus 3M over r) tends to 0.66667. The lensing integral gives exactly 4M over b at leading order. Correct.
- Observations: the Gravity Probe B geodetic result and the M87 ring.: python3 with GM = 3.986004418e14 m^3/s^2 and r = 7013 km; then G = 6.6743e-11, one solar mass 1.98892e30 kg and D = 16.8 Mpc. → Spatial holonomy 3.973e-9 rad per orbit, that is 0.820 milliarcseconds; period 5845 s (97.4 min), so 5399 orbits per year and 4.43 arcseconds per year against 6.64 for the full geodetic rate, a ratio of two thirds at this order. Shadow diameter two root 27 GM over c squared D = 39.70 microarcseconds against the measured ring of 42 plus or minus 3. The published Gravity Probe B numbers, minus 6601.8 plus or minus 18.3 against minus 6606.1 milliarcseconds per year, are confirmed; the note quotes magnitudes and claims no sign.
- References: Everitt and colleagues 2011; the Event Horizon Telescope Collaboration 2019; Claudel, Virbhadra and Ellis 2001; Perlick 2004; Abramowicz, Carter and Lasota 1988; Gibbons and Werner 2008; Euler 1767; Meusnier 1785, presented 1776; Bonnet 1848.: WebSearch of publisher, ADS, arXiv, Euler Archive and history-of-mathematics records, re-checking authors, year, title, venue, pages, doi and arXiv id. → All nine confirmed unchanged, including General Relativity and Gravitation 20, 1173-1183 with doi 10.1007/BF00758937; Journal de l'Ecole polytechnique 19 (cahier 32), 1-146, the source both of the term geodesic curvature and of the extension to a non-geodesic boundary; Euler E333, Memoires de l'academie des sciences de Berlin 16 (1767), 119-143; and Meusnier, Memoires presentes par divers savans 10 (1785), 477-510, presented in 1776. The verified flag stays true for all.
- Structure: prerequisites direct and acyclic, assumes consistent with them, and the advanced tier's rungs present.: Walked the registry ancestry of every prerequisite, and checked that christoffel-symbols, named in the working way's assumes, is a prerequisite of second-fundamental-form and of connection-one-forms. → All five prerequisites are direct: levi-civita-connection is not an ancestor of geodesic, which reaches parallel-transport and christoffel-symbols but not levi-civita-connection, and none of the five has normal-curvature in its ancestry, so there is no cycle and no redundancy. Two formal checks, one formal problem, a research way and two research-horizon topics with one review: the advanced tier is met.

**Counterexamples tried**

- Great circle (equator, ring around the middle): kappa_g = 0, all bend normal; entry ways and checks agree.
- Flat floor: normal curvature zero and a straight walk has no bend; every entry claim of a bend is scoped to a ball.
- Bigger ball: smaller ground bend per metre (1 degree per 111 km on Earth); nothing claims otherwise.
- Walking backwards or the other way round a ring: kappa_g changes sign with direction, kappa_n does not; entry says 'left or right' without a fixed sign, working rung states the sense.
- Bent but flat surface (cylinder, rolled sheet): kappa_n changes, kappa_g unchanged; spiral on the can and rolled-sheet checks confirm.
- Mobius band: signed kappa_g and a rotation holonomy fail for an orientation-reversing loop; added 'on an oriented surface' to the formal holonomy sentence and the related holonomy entry, and 'globally' to the non-orientable limit.
- Corner (cone tip or polygon vertex): curvature concentrated in exterior angles; Gauss-Bonnet carries sum epsilon_i and the formal limits say so.
- Region bigger than half the sphere, or loop not bounding a disk: holonomy -oint kappa_g mod 2 pi still holds for smooth loops on oriented surfaces; Gauss-Bonnet itself is scoped to a disk.
- Saddle: zero normal curvature in two directions with negative Gaussian curvature; misconception zero-normal-curvature-means-flat covers it.
- Geodesic that is not locally shortest in a unique way, and 'straight' as shortest: the entry common answer claimed never steering is 'the only sense' a walker can check straightness, but local shortness is also checkable with a tape; changed to 'a sense'.
- Indefinite ambient metric and null tangents: epsilon factor and scale-free vanishing of II(k,k) stated; photon-surface result holds.
- Rotating black hole: no single photon surface (photon region); research way says so.
- Different slicing for the gyroscope split: the two-thirds spatial part depends on the static slicing; the observation says 'in a slice of the spacetime around a static spherical Earth'.
- Second read, flat floor against the reworded summary: on a floor kappa_n is zero and a non-steering walk is a straight line, but every claim of a bend is tied to a round ball, so the floor is not a counterexample.
- Second read, egg or saddle against 'following the ground alone bends a path only as sharply as a straight walk around the ball's middle': false on any surface that is not umbilic, true on a round ball, and both the belief and its correction name a ball.
- Second read, a ring past the ball's middle against 'she must keep steering toward the point her ring goes around': a ring at a colatitude beyond 90 degrees steers toward the far point instead, but the way and the check both say 'small ring', which keeps the colatitude below 90 degrees.
- Second read, degenerate right triangle against 'they combine like the two shorter sides of a right-angled triangle': a straight walk has kappa_g zero and the triangle collapses, but that sentence is attached to the ladybird's ring, where both parts are non-zero.
- Second read, flat point with both principal curvatures zero against 'asymptotic directions exist iff the product of the principal curvatures is zero or negative': every direction is asymptotic there and the product is zero, so the non-strict inequality is the right one.
- Second read, choice of normal against 'cos phi = 6/10' in the tilted-circle check: with the sphere's outward normal the cosine is minus 6/10, so the question fixes only its size; the sentence now reads size 6/10.
- Second read, symbol collision: g is the induced metric in the formal way and the spacetime metric in the research check, so the check now scopes both g and h.

**Fixes**

- Steering way try-it: the reason for crinkling said the tape's nearer edge 'is shorter', which would make it stretch; now both edges of the tape are the same length but the line for the nearer edge is shorter, so that edge has too much tape and crinkles.
- Formal way: 'on an oriented surface' added to the holonomy-equals-minus-integrated-geodesic-curvature sentence; 'defined globally' in the non-orientable limit.
- Related holonomy entry scoped to an oriented surface.
- Entry common question: 'the only sense a walker on the ball can check' became 'a sense', since local shortness is also checkable.
- References: all seven confirmed and set verified, with DOIs and arXiv ids added; Meusnier 1785 and Bonnet 1848 primary works added to history as verified references.
- Revision bumped to 3 for the learner-visible changes; status physics-reviewed.
- SECOND FULL PHYSICS READ (revision 5 to 6). The 13 learner-visible strings the second novice read changed were all diff-checked and needed no correction.
- Check tilted-circle-claim: 'so cos phi = 6/10' became 'so |cos phi| = 6/10', because the question fixes no surface normal and the sphere's outward normal gives minus 6/10; the key point became 'The tilt's cosine has size six tenths'. The rest of that answer already worked in sizes.
- Check photon-sphere-from-null-normal-curvature: the question now says 'with g the spacetime metric and h the induced metric on the surface', because the formal way writes g for the induced metric and the check needed both letters scoped; h was also used in the question without being named.
- Revision bumped to 6 for those two learner-visible changes, both outside the entry rung; status physics-reviewed.

**Concerns**

- A novice re-read is due for exactly two changed strings, both outside the entry rung: the working check tilted-circle-claim (its answer and one key point) and the research check photon-sphere-from-null-normal-curvature (its question). This read left the entry rung untouched.
- No entry headroom: entry way explanations are 431 words against the advanced cap of 400, inside the 10 percent review allowance of 440. Any entry addition must first drop or shorten something else.
- course-conventions.md still fixes no sign for the second fundamental form, for normal curvature or for geodesic curvature of a curve in a surface, and does not say that a bare K in the Gauss-Bonnet theorem is the Gaussian curvature. The note sets all three in notation_traps, consistently with second-fundamental-form.json and with the orientation row, which itself writes a bare K. They belong in the conventions file.
- Entry wording for a novice eye, not a physics error: 'the line where those two equal halves meet' names a seam that, for two solid halves, is a flat disk; the next sentence identifies the line as a circle as big as the ball, which repairs it for a reader who reads on.
- The try-it ring of about 10 centimetres all the way round has a radius of about 1.6 cm on a 70 cm football, so masking tape 19 mm wide reaches to within 6 mm of the point the ring goes around. The demonstration still works, and works strongly (the nearer edge's line is about 4 cm for 10 cm of tape), but 'narrow' is doing real work in the instruction.
- Registry drift, informational rather than a warning: the registry lists only second-fundamental-form and curvature-of-a-curve, while the note also needs geodesic, levi-civita-connection and connection-one-forms. All five were checked this read and are direct and acyclic, so sync_registry.py should apply them.
- Both visuals are still proposals. bend-arrow-split-on-a-surface is cited by both entry ways, both entry checks and two teaching-arc steps, so the entry rung currently teaches with no picture; arrow-around-a-circle-of-latitude is also cited by holonomy.json and should be built once with a tour per concept.
- No geodesic concept note exists yet for the glossary entries 'walk straight' and 'geodesic' to align with.
- The history year for Meusnier stays 1776, the presentation, while the work's year is 1785, the publication; the contribution text states both.
- analogies and worked_examples are empty. An advanced note requires neither, and adding one now would need a fresh physics check rather than a diff check.
- The note and its neighbours in this domain are untracked in git. No commit was made from this stage, to avoid racing other agents in this workflow.

**Diff check** (2026-09-13, revision 4)

- Steering try-it: the tape's two edges are the same length.: Checked against the physical setup: narrow masking tape is laid without stretching, so both edges carry equal tape length; same claim as revision 3. → True; unchanged in substance.
- Steering try-it: the edge nearer the point the ring goes around must lie along a shorter line than the other edge.: On a ball of radius R, a circle at geodesic distance r from the centre point has length 2 pi R sin(r/R), which grows with r while r < pi R/2. Football of circumference about 70 cm gives R about 11.1 cm and pi R/2 about 17.5 cm. Computed with python3 for tape width 1.9 cm: ring radius 10 cm gives inner edge line 50.8 cm and outer 58.2 cm; ring radius 5 cm gives 24.9 cm and 35.6 cm. Whether '10 centimetres around' means radius or diameter, the ring is far smaller than the ball's middle, so the nearer edge's line is shorter. Counterexample tried: a ring past the ball's middle would reverse which edge is shorter, but 'the point the ring goes around' names the point the ring was drawn around, and the stated 10 cm ring is well inside the limit. → True within the stated setup; same claim as revision 3.
- Steering try-it: so that nearer edge has more tape than its line needs, and that edge crinkles.: Equal tape length laid along a shorter line leaves excess on that edge, which buckles out of the surface; the outer edge's line is longer, so it is pulled taut rather than crinkled. Checked the sense: the old wording 'too much tape, and it crinkles' made the same claim. → True; sense and edge match revision 3 and the note's explanation that steering is toward the point.

**Diff check** (2026-09-13, revision 8)

- Geometry of the new triangle sentence: the perpendicular from the sphere's centre to the circle's plane meets that plane at the circle's centre, and the sphere's centre, the circle's centre and the touching point form a right triangle with legs 8 cm and 6 cm and hypotenuse 10 cm.: Every point of the circle is at distance 10 cm from the sphere's centre, so the foot of the perpendicular is equidistant from them within the plane and is the circle's centre; the perpendicular meets the plane at a right angle, so the right angle sits at the circle's centre. Checked with python3 using O = (0,0,0), C = (0,0,8), P = (6,0,8): |OC| = 8, |CP| = 6, |OP| = 10, and 8 squared plus 6 squared is 100. → True. The 8 cm leg is fixed by the two given radii, not assumed.
- New sentence: the triangle's angle at the touching point, between the ray to the circle's centre and the ray to the sphere's centre, has cosine 6/10.: At the touching point the leg of length 6 cm is adjacent and the hypotenuse of length 10 cm subtends the right angle, so the cosine is 6/10; confirmed numerically by dotting the two unit rays from P. → 0.6 exactly. Correct, and the sine is 8/10, which the unchanged geodesic-curvature line uses.
- New sentence: the small circle's principal normal runs along the ray to the circle's centre, the sphere's normal runs along the ray to the sphere's centre or against it because the question fixes no side, so only the size is settled and $|\cos\varphi| = 6/10$.: A circle is a plane curve whose principal normal points at its own centre. The unit normal of the sphere at the touching point is the outward or the inward radial direction, and the question names neither. Computed both: the principal normal has cosine +0.6 with the inward normal and -0.6 with the outward one. → True, and consistent with key_equations/squares-add-and-meusnier, where $\varphi$ is the angle between the curve's principal normal and the chosen surface normal. Taking the size is the only claim the question supports.
- Unchanged conclusions still follow from the reworded steps: $|\kappa_n| = (1/6)(0.6) = 0.1$ per centimetre, the same as the great circle, and $|\kappa_g| = (1/6)(0.8) = 0.133$ per centimetre.: python3 with both normal choices: $\kappa = 1/6$ per cm, $\kappa_n = \pm 0.1$, $|\kappa_g| = 0.13333$, and $\kappa_n^2 + \kappa_g^2 = 1/36$ to machine precision. A great circle on the 10 cm sphere has $\kappa = 1/10$ with its principal normal along the radius, so $|\kappa_n| = 0.1$; Meusnier's theorem also forces the two curves to share $\kappa_n$, since they touch and head the same way. → Correct. The numeric field, 10 cm as the radius for the normal curvature, matches $1/0.1$.
- The reworded key point states the same fact as the sentence it summarises.: Compared word by word with the answer: both say the cosine of the angle between the small circle's principal normal and the sphere's normal has size six tenths, with no side chosen. → Same claim, and true.
- Fix: Check tilted-circle-claim, key point 'The cosine of the tilt between the curve's principal normal and the sphere's normal has size six tenths': 'the curve's' became 'the small circle's'. Read on its own in the grading list, 'the curve' had two candidates in this check, and for the great circle the statement is false, since its principal normal lies along the sphere's radius and the size of the cosine is one. Same claim, same number.
- Fix: Check tilted-circle-claim, answer sentence 'The curve's principal normal runs along the first ray...': 'The curve's' became 'The small circle's', for the same two candidates and because the note names this curve the small circle everywhere else. No other word changed, and nothing was shortened to make room.
- Fix: Revision bumped to 8 for those two learner-visible changes, both at the working rung inside one check; status stays physics-reviewed, so a novice sign-off of exactly these two strings is owed.
