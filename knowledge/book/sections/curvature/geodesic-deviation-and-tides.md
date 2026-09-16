# Geodesic deviation and tides

`curvature/geodesic-deviation-and-tides` · main track · working depth · physics-reviewed · revision 4 · 2026-09-16

Teaches: `deviation-vector`, `newtonian-deviation-equation`, `geodesic-deviation-equation`, `relativistic-tidal-tensor`, `volume-preserving-tidal-deformation`

Builds on: `curved-surfaces`, `holonomy-and-the-riemann-tensor`, `symmetries-and-identities`, `ricci-bianchi-and-einstein-tensors`, `newtonian-gravity-as-a-field`, `the-lift-and-the-equivalence-principles`, `the-newtonian-limit`, `the-geodesic-equation`, `lie-derivatives`, `the-levi-civita-connection`, `transport-along-worldlines`, `constant-curvature-weyl-and-invariants`

**Two things that fall freely side by side feel no gravity, yet the gap between them changes. In Newton's theory the second derivatives of the potential act on the separation; in Einstein's theory the Riemann tensor fed the four-velocity twice, the tidal tensor, does the same job, and the two agree in weak fields. The trace of the tidal tensor is a Ricci component, so a small ball of free particles starts to change shape but not its volume unless matter lies inside it.**

A capsule is dropped inside a tower 110 metres tall from which the air has been pumped out. An accelerometer bolted to the capsule reads zero for the whole 4.7 seconds of the fall: nothing acts on the capsule but gravity, and gravity is not felt. Inside, two steel balls were released at the moment of the drop, 1 metre apart, side by side at the same height. A laser between them reads their gap. By the time the capsule reaches the bottom the gap has closed by about 17 millionths of a metre, and it was closing faster and faster. Nothing pushed either ball. *The lift and the equivalence principles* named this the tidal force, and *Newtonian gravity as a field* introduced the Newtonian tidal tensor behind it. This section derives the rule for the gap, first from Newton's law and then from the Riemann tensor, and finds that the second rule contains the first.

## Two falls, subtracted

Let a reference particle fall freely along $\mathbf x(t)$ in a Newtonian potential $\Phi$, and let a neighbour fall along $\mathbf x(t) + \boldsymbol\xi(t)$, both positions taken at the same Newtonian time $t$. Each obeys $\ddot{\mathbf x} = -\nabla\Phi$ at its own position. Subtract the two equations of motion:

$$\ddot{\boldsymbol\xi} = -\nabla\Phi(\mathbf x + \boldsymbol\xi) + \nabla\Phi(\mathbf x).$$

Expand the first term to first order in $\boldsymbol\xi$ as a Taylor series in three variables: $\partial_i\Phi(\mathbf x + \boldsymbol\xi) = \partial_i\Phi(\mathbf x) + \xi^j\,\partial_j\partial_i\Phi(\mathbf x) + \dots$ The zeroth-order terms cancel, and what is left is the Newtonian deviation equation

$$\ddot\xi^i = -\big(\partial_i\partial_j\Phi\big)\,\xi^j .$$

The matrix $\partial_i\partial_j\Phi$, evaluated on the reference path, is the Newtonian tidal tensor of *Newtonian gravity as a field*. It is symmetric, because the order of two partial derivatives of a smooth $\Phi$ does not matter, and it is sampled where the pair is now, so it changes as the pair moves.

Three features will carry over to relativity. The field $-\nabla\Phi$ itself has cancelled: a uniform field, however strong, produces no relative acceleration. That is why the gap can close while the capsule's accelerometer reads zero: the accelerometer feels only the field at its own spot, which free fall cancels, and the gap feels the difference of the field between two spots, which it does not. The relative acceleration is linear in $\boldsymbol\xi$: twice the gap gives twice the effect. And only the change of the field from place to place remains.

Outside a spherical mass, $\Phi = -GM/r$. Differentiating twice, with $\partial_i r = x_i/r$, gives

$$\partial_i\partial_j\Phi = \frac{GM}{r^3}\big(\delta_{ij} - 3\hat x_i\hat x_j\big),$$

where $\hat{\mathbf x}$ is the unit vector from the mass to the pair. Acting on $\hat{\mathbf x}$, the bracket gives $\hat{\mathbf x} - 3\hat{\mathbf x} = -2\hat{\mathbf x}$, so the eigenvalue along the radius is $-2GM/r^3$; acting on any vector perpendicular to $\hat{\mathbf x}$, the bracket gives that vector back, so the transverse eigenvalue is $+GM/r^3$. A radial separation therefore obeys $\ddot\xi = +(2GM/r^3)\,\xi$ and grows, while a transverse one obeys $\ddot\xi = -(GM/r^3)\,\xi$ and is pulled back like a mass on a spring. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$. A transverse pair released at rest 1 m apart closes by $\tfrac12(GM/r^3)\,t^2\times 1\ \mathrm m$ while $t\sqrt{GM/r^3}$ stays small, the first term of the spring solution $\cos(t\sqrt{GM/r^3})$: 17 millionths of a metre in the capsule's 4.7 s, and 0.077 mm in 10 s. A radial pair separates by twice as much.

*Subtracting two nearby free falls and expanding to first order gives a relative acceleration equal to minus the second derivatives of the potential acting on the separation; the field itself cancels, only its change from place to place remains.*

## A vector between neighbours

Relativity has no shared instant $t$. Replace the pair of paths with a family of geodesics and compare members at equal proper time. Take a smooth one-parameter family of timelike geodesics $x^\mu(\tau, s)$: the label $s$ picks a member, and $\tau$ is proper time along that member, so that $u^\mu = \partial x^\mu/\partial\tau$ obeys $u_\mu u^\mu = -c^2$ on every member. The deviation vector is the derivative across the family,

$$\xi^\mu = \frac{\partial x^\mu}{\partial s}.$$

To first order in $\delta s$, the member $s + \delta s$ passes through $x^\mu + \xi^\mu\,\delta s$ at the same proper time $\tau$. Equal proper time replaces the equal $t$ of Newton's equation, and it plays the part of the matching step count for the two walkers of *Curved surfaces*.

Two things follow from the definition alone. First, $\partial u^\mu/\partial s = \partial\xi^\mu/\partial\tau$, because mixed partial derivatives commute. The left side needs $\Gamma^\mu{}_{\alpha\beta}\xi^\alpha u^\beta$ added to become $Du^\mu/ds$, the covariant derivative of $u$ along $\xi$; the right side needs $\Gamma^\mu{}_{\alpha\beta}u^\alpha\xi^\beta$ added to become $D\xi^\mu/d\tau$, the covariant derivative of $\xi$ along $u$. The Christoffel symbols of *The Levi-Civita connection* are symmetric in their lower indices, so these two terms are the same term. Add it to both sides, and each side is now a covariant derivative along one set of grid lines:

$$\frac{D\xi^\mu}{d\tau} = \frac{Du^\mu}{ds} = \xi^\nu\nabla_\nu u^\mu .$$

In the language of *Lie derivatives*, $[u, \xi] = 0$: the deviation vector is Lie dragged along the flow, always joining the same two members. Dragged does not mean constant. Its rate of change is the gradient of the family's four-velocity across the family, so if the members move apart, $\xi$ grows.

Second, $u_\mu\xi^\mu$ is constant along each member. Along a geodesic $Du^\mu/d\tau = 0$, so $d(u_\mu\xi^\mu)/d\tau = u_\mu\,D\xi^\mu/d\tau = u_\mu\,Du^\mu/ds = \tfrac12\,\partial(u_\mu u^\mu)/\partial s$, and that is zero because $u_\mu u^\mu = -c^2$ on every member. The constant records only how the members' clocks were set. Relabelling the family as $x^\mu(\tau + f(s), s)$, which resets each member's clock by $f(s)$, adds $f'(s)\,u^\mu$ to $\xi^\mu$ and changes nothing else. So the part of $\xi$ along $u$ is a clock offset, not a distance. The part that an observer riding the reference geodesic measures as the separation, by radar say, is the orthogonal part,

$$\xi_\perp^\mu = h^\mu{}_\nu\,\xi^\nu,\qquad h^\mu{}_\nu = \delta^\mu{}_\nu + \frac{u^\mu u_\nu}{c^2},$$

which obeys $u_\mu\xi_\perp^\mu = u_\nu\xi^\nu - c^2\,u_\nu\xi^\nu/c^2 = 0$ with signature $(-,+,+,+)$.

*The deviation vector is the derivative of a family of geodesics across the family; its covariant rate of change is the velocity gradient acting on it, its part along the four-velocity is a fixed clock offset, and its orthogonal part is the separation an observer measures.*

## Swap the order: the geodesic deviation equation

Now differentiate once more along the reference geodesic. Start from $D\xi^\mu/d\tau = Du^\mu/ds$ and apply $D/d\tau$:

$$\frac{D^2\xi^\mu}{d\tau^2} = \frac{D}{d\tau}\frac{Du^\mu}{ds}.$$

If the two covariant derivatives could be swapped, the right side would be $D/ds$ of $Du^\mu/d\tau$, which is zero because every member is a geodesic (*The geodesic equation*). They cannot be swapped for free; the cost is exactly what curvature measures. For a vector field $V^\mu$ on the two-dimensional sheet swept out by the family, the Ricci identity of *Holonomy and the Riemann tensor*, contracted with the sheet's two tangent vectors $u$ and $\xi$, gives

$$\frac{D}{d\tau}\frac{DV^\mu}{ds} - \frac{D}{ds}\frac{DV^\mu}{d\tau} = R^\mu{}_{\nu\alpha\beta}\,V^\nu u^\alpha\xi^\beta,$$

with no Lie-bracket term, the term the curvature operator of that section subtracts, because $[u, \xi] = 0$ for a Lie-dragged deviation vector. Put $V = u$ and use $Du^\mu/d\tau = 0$:

$$\frac{D^2\xi^\mu}{d\tau^2} = R^\mu{}_{\nu\alpha\beta}\,u^\nu u^\alpha\xi^\beta = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma,$$

where the last step swaps the antisymmetric last pair of indices. This is the geodesic deviation equation, in the course's sign.

Read it slot by slot. The right side is linear in $\xi$: twice the separation, twice the relative acceleration, as in Newton's equation. It contains $\xi$ and $u$ at the event but not $D\xi/d\tau$, so to this order neighbours released at rest and neighbours already drifting feel the same relative acceleration. A part of $\xi$ along $u$ drops out, because the last index pair is antisymmetric while $u^\rho u^\sigma$ is symmetric; the clock offset never enters, and only $\xi_\perp$ is accelerated. In flat spacetime the right side vanishes and $\xi$ changes linearly with $\tau$: free particles that start with no relative velocity keep their separation, which is the parallel postulate of *Curved surfaces* in spacetime form.

Check the sign on a sphere of radius $a$. Arc length, written $\ell$ here because $s$ is already the family label, takes the place of $\tau$, and the tangent $u$ has unit length. On a surface the Riemann tensor has one independent component (*Symmetries and identities*), so $R_{\mu\nu\rho\sigma} = K(g_{\mu\rho}g_{\nu\sigma} - g_{\mu\sigma}g_{\nu\rho})$, and on the sphere $K = 1/a^2$ (*Constant curvature, the Weyl tensor and invariants*). For $\xi$ orthogonal to $u$ the right side is $-\xi^\mu (u_\nu u^\nu)/a^2 = -\xi^\mu/a^2$. Write $\xi = f\,e$ with $e$ a parallel unit vector orthogonal to the geodesic: $f'' = -f/a^2$. Walkers who leave the equator side by side, with $f'(0) = 0$, have $f = f_0\cos(\ell/a)$, which reaches zero at $\ell = \pi a/2$, the pole, as *Curved surfaces* found with a globe.

*Swapping covariant derivatives along and across a family of geodesics costs a Riemann term, so the relative acceleration of neighbouring geodesics is minus the Riemann tensor fed the four-velocity, the separation and the four-velocity again; it is linear in the separation, ignores the clock offset, and vanishes in flat spacetime.*

## The tidal tensor and its matrix

Group the two four-velocity slots together:

$$\frac{D^2\xi^\mu}{d\tau^2} = -\big(R^\mu{}_{\alpha\nu\beta}\,u^\alpha u^\beta\big)\,\xi^\nu .$$

The bracket is the relativistic tidal tensor of the observer with four-velocity $u$. A second observer passing through the same event with a different four-velocity feeds the same Riemann tensor a different $u$ and in general gets a different tidal tensor: tides are an observer's reading of the curvature, not a property of the event alone. Its components have units of $\mathrm{s^{-2}}$, relative acceleration per unit separation. Fed the same unit direction in both free slots, a positive result means neighbours in that direction are pulled back together and a negative one means they are pushed apart. The Riemann symmetries of *Symmetries and identities* fix its shape. Antisymmetry in the last pair kills any $\xi$ along $u$. Antisymmetry in the first pair makes $u_\mu R^\mu{}_{\alpha\nu\beta}u^\alpha u^\beta = 0$, so every relative acceleration is orthogonal to $u$. Pair exchange makes the lowered tensor symmetric in $\mu$ and $\nu$.

To turn it into numbers, give the observer three gyroscopes. In free fall nothing twists them, so their axes are parallel transported (*Transport along worldlines*), and with $\hat e_{\hat 0} = u/c$ they form a parallel-propagated orthonormal frame. Components in a parallel frame change by ordinary derivatives, so $D^2\xi^\mu/d\tau^2$ has frame components $d^2\xi^{\hat a}/d\tau^2$, and $u^{\hat a} = (c, 0, 0, 0)$. The $\hat 0$ component of the equation is zero on both sides: on the left because $\xi^{\hat 0} = -u_\mu\xi^\mu/c$ is the constant clock offset, on the right because every relative acceleration is orthogonal to $u$. The space components read

$$\frac{d^2\xi^{\hat\imath}}{d\tau^2} = -E_{ij}\,\xi^{\hat\jmath},\qquad E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0},$$

the tidal matrix that *Ricci, Bianchi and Einstein* took on trust. It is a real symmetric $3\times3$ matrix, so it has three orthogonal eigenvectors, the main directions, with real eigenvalues $\lambda_k$. Along an eigenvector, $d^2\xi/d\tau^2 = -\lambda_k\xi$. While $\lambda_k$ stays constant, a positive eigenvalue makes the separation oscillate like a mass on a spring, and a negative one makes neighbours released at rest separate as $\cosh(\sqrt{|\lambda_k|}\,\tau)$. Either way, a cloud released at rest has its axis along that direction change as $L \approx L_0(1 - \tfrac12\lambda_k\tau^2)$ at first.

Now take the weak, static field of *The Newtonian limit and the weak-field metric*, $g_{00} = -(1 + 2\Phi/c^2)$ with $x^0 = ct$. There $\Gamma^i{}_{00} = -\tfrac12\partial_i g_{00} = \partial_i\Phi/c^2$, and in the Riemann formula of *Holonomy and the Riemann tensor* only $\partial_j\Gamma^i{}_{00}$ survives to first order in $\Phi$ for a static field. For a slow observer, one moving at a speed much less than $c$ relative to the mass, whose frame is the coordinate basis to this order,

$$E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \partial_i\partial_j\Phi .$$

The frame equation becomes $\ddot\xi^i = -\partial_i\partial_j\Phi\,\xi^j$: Newton's deviation equation, with Newton's tidal tensor revealed as the weak-field face of six Riemann components. Outside a spherical mass, in the radial and two transverse main directions, $E = (GM/r^3)\,\mathrm{diag}(-2, 1, 1)$. Outside a non-rotating spherical mass this pattern holds exactly, not only in weak fields, for observers at rest and for observers falling radially; take that on trust until *The Schwarzschild solution*.

*Contracting the Riemann tensor twice with an observer's four-velocity gives a symmetric tidal tensor, a three-by-three matrix in the observer's gyroscope frame whose eigenvectors are the main directions; in a weak static field it is the matrix of second derivatives of the Newtonian potential.*

## Shape first, volume later

Release crumbs at rest on a small sphere of radius $L_0$ around the observer. The crumbs are test particles: they pull on nothing, and whatever matter sits inside the sphere passes through them freely. Each main direction is an axis of the cloud, and that half-axis changes as $L_k \approx L_0(1 - \tfrac12\lambda_k\tau^2)$. The cloud becomes an ellipsoid, whose volume is proportional to the product of its three half-axes, so for small changes the fractional change of the volume is the sum of the fractional changes of the three half-axes:

$$\frac{\delta V}{\delta V_0} \approx 1 - \tfrac12\tau^2\sum_k\lambda_k,\qquad \left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau=0} = -\sum_k\lambda_k = -E_{ii} .$$

The trace of the tidal matrix is $c^2R^{\hat\imath}{}_{\hat 0\hat\imath\hat 0}$. Adding the $\hat 0\hat 0$ term, which vanishes, makes it $R^\mu{}_{\alpha\mu\beta}u^\alpha u^\beta$, and by the definition of the Ricci tensor in *Ricci, Bianchi and Einstein* that is $R_{\alpha\beta}u^\alpha u^\beta$:

$$\left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau=0} = -R_{\mu\nu}u^\mu u^\nu .$$

The shape of the cloud is set by all six components of $E_{ij}$; its volume, at first, by the one Ricci component along $u$.

Newton's version of the same statement is Poisson's equation. The trace of $\partial_i\partial_j\Phi$ is $\nabla^2\Phi = 4\pi G\rho$ (*Newtonian gravity as a field*), with $\rho$ the mass density at the cloud. Outside matter the trace is zero, and indeed $-2 + 1 + 1 = 0$. In general relativity the trace $R_{\mu\nu}u^\mu u^\nu$ also vanishes outside matter when there is no cosmological constant; that is a consequence of Einstein's equation, taken on trust here until *Finding the field equations*. Beside Earth a ball of radius 1 m becomes, in 10 s, an egg: its 1 m half-axis along the radius grows by 0.154 mm and each 1 m transverse half-axis shrinks by 0.077 mm; the fractions $+154$, $-77$ and $-77$ parts in a million add to zero. A change of shape by tides that keeps the volume is called a volume-preserving tidal deformation. Inside a uniform ball of density $\rho$, by contrast, $\Phi$ is quadratic in $r$ and all three eigenvalues equal $4\pi G\rho/3$, so a released cloud shrinks in every direction. The words at first matter: the sum rule holds only while the fractional changes stay small.

*A small ball of free particles released at rest starts changing volume at a rate set by the trace of the tidal matrix, which is the Ricci component along the observer's four-velocity; outside matter that trace is zero, so tides reshape the ball into an egg of the same volume, and matter inside makes it shrink.*

## Key equations

**Newtonian deviation equation** (derived-here)

$$\ddot\xi^i = -\big(\partial_i\partial_j\Phi\big)\,\xi^j$$

The relative acceleration of two nearby freely falling particles is minus the matrix of second derivatives of the Newtonian potential, evaluated on the reference path, acting on their separation. First order in the separation, both positions at the same time $t$.

- $\xi^i$: separation of the neighbour from the reference particle at the same time
- $\partial_i\partial_j\Phi$: second partial derivatives of the Newtonian potential, the Newtonian tidal tensor

Say: The second time derivative of the separation equals minus the second derivatives of the potential acting on the separation.

**Deviation vector and its rate of change** (derived-here)

$$\xi^\mu = \frac{\partial x^\mu}{\partial s},\qquad \frac{D\xi^\mu}{d\tau} = \frac{Du^\mu}{ds} = \xi^\nu\nabla_\nu u^\mu$$

In a family of geodesics $x^\mu(\tau, s)$ the deviation vector is the derivative across the family. Because mixed partials commute and the connection is torsion-free, its covariant rate along a member equals the gradient of the four-velocity across the family.

- $s$: label of the member of the family
- $\tau$: proper time along each member
- $u^\mu$: four-velocity, the derivative of position with respect to proper time

Say: The deviation vector is the derivative of position with respect to the family label, and its covariant derivative along proper time equals the covariant derivative of the four-velocity across the family.

**Geodesic deviation equation** (derived-here)

$$\frac{D^2\xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\,u^\nu\xi^\rho u^\sigma$$

The relative acceleration of neighbouring geodesics is the Riemann tensor fed the four-velocity, the deviation vector and the four-velocity again, with a minus sign in the course's conventions. Linear in $\xi$, independent of the relative velocity to this order, and blind to the part of $\xi$ along $u$.

- $\frac{D^2\xi^\mu}{d\tau^2}$: second covariant derivative of the deviation vector along the reference geodesic
- $R^\mu{}_{\nu\rho\sigma}$: Riemann curvature tensor in the course's sign

Say: The second covariant derivative of the deviation vector with respect to proper time equals minus the Riemann tensor fed the four-velocity, the deviation vector, and the four-velocity again.

**Tidal matrix in a parallel-propagated frame** (derived-here)

$$\frac{d^2\xi^{\hat\imath}}{d\tau^2} = -E_{ij}\,\xi^{\hat\jmath},\qquad E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0}$$

In the orthonormal frame carried by a freely falling observer's gyroscopes, the geodesic deviation equation is an ordinary second-order equation with a real symmetric three-by-three matrix of Riemann components. Its eigenvectors are the main directions and its eigenvalues are relative accelerations per unit separation.

- $\xi^{\hat\imath}$: space components of the deviation vector in the observer's parallel-propagated orthonormal frame
- $E_{ij}$: tidal matrix, c squared times the Riemann components with the frame time direction in the second and fourth slots

Say: The second derivative of the frame components of the separation equals minus the tidal matrix acting on the separation, where the tidal matrix is c squared times the Riemann components i zero j zero in the observer's frame.

**Tidal matrix in a weak static field** (derived-here)

$$E_{ij} = c^2R^{\hat\imath}{}_{\hat 0\hat\jmath\hat 0} \approx \partial_i\partial_j\Phi$$

For a slow observer in the weak static metric $g_{00} = -(1 + 2\Phi/c^2)$, the tidal matrix reduces to the Newtonian tidal tensor, so the geodesic deviation equation reduces to the Newtonian deviation equation.

- $\Phi$: Newtonian potential, zero far from every mass

Say: In a weak static field the tidal matrix is approximately the matrix of second derivatives of the Newtonian potential.

**Volume law for a small released ball** (derived-here)

$$\left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau = 0} = -E_{ii} = -R_{\mu\nu}u^\mu u^\nu$$

A small ball of free particles released at rest starts changing its volume at a fractional rate equal to minus the trace of the tidal matrix, which is the Ricci tensor fed the observer's four-velocity twice. Zero outside matter with no cosmological constant.

- $\delta V$: volume of the small ball
- $R_{\mu\nu}u^\mu u^\nu$: Ricci tensor contracted twice with the observer's four-velocity

Say: The initial fractional volume acceleration of a small released ball equals minus the trace of the tidal matrix, which is minus the Ricci tensor fed the four-velocity twice.

## Checks

**zero-christoffels-nonzero-drift** (numeric): A friend argues: in a freely falling frame the Christoffel symbols vanish along the observer's worldline, so the geodesic equation of a neighbour reduces to $\ddot x^\mu = 0$ and neighbours cannot accelerate relative to the observer. Two test masses are released at rest 2 m apart, side by side at the same height, at Earth's surface. What does the friend predict for their gap after 5 s, what actually happens, and by how much?

Answer: The friend predicts the gap stays 2 m. In fact it closes by $\tfrac12(GM/r^3)t^2\times 2\ \mathrm m = \tfrac12(1.54\times10^{-6})(25)(2) = 3.9\times10^{-5}\ \mathrm m$, about 0.04 mm. Coordinates can remove the Christoffel symbols on one worldline, but not their first derivatives, and the Riemann tensor is built from those derivatives. A neighbour 2 m away sits where the Christoffel symbols are no longer zero, at first order in the separation, and the geodesic deviation equation collects exactly that first-order term. The transverse tidal entry $+GM/r^3$ pulls the pair together.

Key points: Christoffel symbols vanish on the worldline, their derivatives do not, and the Riemann tensor survives; The gap closes by about 0.04 mm, from half of GM over r cubed times t squared times 2 metres

Numeric: closing of the gap after 5 s = 3.85e-05 m

**dragged-but-growing** (predict): Galaxies in a uniform expansion move with velocity $\mathbf v = H\mathbf x$ relative to a reference galaxy, with $H = 70$ km per second per megaparsec (one megaparsec is $3.086\times10^{22}$ m). A friend says: the deviation vector between two galaxies is Lie dragged along the flow, so their separation never changes. Use the rate equation for the deviation vector to find how fast the separation of two galaxies 1 megaparsec apart changes, and say what Lie dragged does mean.

Answer: In this slow-motion setting the rate equation reads $d\xi^i/dt = \xi^j\partial_j v^i = H\xi^i$. For $\xi = 1$ megaparsec the separation grows at 70 km per second, and it keeps growing as long as the flow does. Lie dragged means the vector always joins the same two members of the family; it says nothing about its length, which is set by the velocity gradient of the flow. Dragged is not constant.

Key points: The rate of change of the deviation vector is the velocity gradient acting on it, here H times the separation, so the separation grows at 70 kilometres per second per megaparsec; Lie dragged means the vector follows the same two members, not that its length is fixed

**ball-at-the-centre-of-a-planet** (numeric): Two small balls of free test particles, each 1 m in radius, are released at rest for 10 s: one beside Earth in a falling cabin, one at the centre of a uniform planet of density $\rho = 5500\ \mathrm{kg\,m^{-3}}$ through which particles pass freely. A friend says gravity pulls everything together, so both balls must shrink. For each ball, find the three eigenvalues of the tidal matrix, the fractional change of each axis, and the fractional change of volume after 10 s.

Answer: Beside Earth the eigenvalues are $(GM/r^3)(-2, 1, 1) = (-3.08, 1.54, 1.54)\times10^{-6}\ \mathrm{s^{-2}}$. Each axis changes by $-\tfrac12\lambda t^2$: $+154$, $-77$ and $-77$ parts in a million. Their sum, the fractional volume change, is zero: the ball becomes an egg of the same volume. At the planet's centre $\Phi$ is quadratic and all three eigenvalues equal $4\pi G\rho/3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$, so each axis shrinks by 77 parts in a million and the volume by $3\times77 = 231$ parts in a million, which is $\tfrac12(4\pi G\rho)t^2$. Only mass inside the ball makes its volume start to change; mass outside reshapes it.

Key points: Beside Earth: eigenvalues minus 2, 1, 1 times GM over r cubed, axes plus 154 and minus 77 twice, volume change zero; At the centre: three equal eigenvalues 4 pi G rho over 3, every axis shrinks by 77 parts in a million, volume by 231 parts in a million

Numeric: fractional volume change of the ball at the planet's centre after 10 s = -0.00023 1; fractional volume change of the ball beside Earth after 10 s = 0 1

## Misconceptions

- **free-fall-removes-relative-acceleration**: "In a freely falling frame the Christoffel symbols vanish, so neighbouring free particles cannot accelerate relative to each other." — Coordinates remove the Christoffel symbols on one worldline, not their first derivatives, and the Riemann tensor is built from those. Neighbours a small distance away feel the first-order term, which is the geodesic deviation equation. (diagnosed by zero-christoffels-nonzero-drift)
- **lie-dragged-means-constant**: "The deviation vector is Lie dragged along the family, so the separation between neighbouring free particles never changes." — Lie dragged means the vector always joins the same two members. Its covariant rate of change is the velocity gradient acting on it, which is nonzero whenever the members move apart or together. (diagnosed by dragged-but-growing)
- **tides-squash-the-ball**: "Gravity pulls everything together, so tides squash a freely falling ball of particles and make it smaller." — The initial volume change is set by the trace of the tidal matrix, a Ricci component, which vanishes outside matter. Beside a planet the ball becomes an egg of the same volume; only mass inside the ball makes it shrink. (diagnosed by ball-at-the-centre-of-a-planet)

## Glossary

- **deviation vector**: In a family of geodesics, the derivative of position with respect to the family label: the vector from a point on one geodesic to the point at the same proper time on its neighbour. (`deviation-vector`)
- **orthogonal part**: The part of the deviation vector at right angles to the four-velocity, which is the separation an observer on the reference geodesic measures by radar. The part along the four-velocity is only a clock offset. (`deviation-vector`)
- **Newtonian deviation equation**: The rule that the relative acceleration of two nearby freely falling particles is minus the matrix of second derivatives of the potential acting on their separation. (`newtonian-deviation-equation`)
- **geodesic deviation equation**: The rule that the covariant relative acceleration of neighbouring geodesics is minus the Riemann tensor fed the four-velocity, the deviation vector and the four-velocity again. (`geodesic-deviation-equation`)
- **relativistic tidal tensor**: The Riemann tensor contracted twice with an observer's four-velocity: the symmetric tensor that turns a separation into a relative acceleration for that observer. (`relativistic-tidal-tensor`)
- **tidal matrix**: The three-by-three matrix of the tidal tensor in a freely falling observer's gyroscope frame: c squared times the Riemann components with the frame time direction in the second and fourth slots. (`relativistic-tidal-tensor`)
- **main directions**: The three perpendicular eigenvectors of the tidal matrix, along which a neighbour accelerates directly toward the observer, directly away, or not at all when the eigenvalue is zero. (`relativistic-tidal-tensor`)
- **volume-preserving tidal deformation**: A change of shape by tides that keeps the volume: a small ball of free particles released at rest outside matter becomes an egg of the same volume, because the trace of the tidal matrix is zero there. (`volume-preserving-tidal-deformation`)

## Visuals

- `falling-ring-of-crumbs` (flagship): The flagship: a ball of free test particles released at rest in a falling cabin, with the tidal matrix, its main directions and a volume meter read live. Sketch: A cabin falling near a spherical mass, holding a ball of crumbs around a centre crumb, with the line to the centre of the mass marked. After release the ball becomes an egg; readouts show the three eigenvalues of the tidal matrix in the observer's gyroscope frame, the fractional change of each axis, their sum, and the volume. Presets: Earth's surface (eigenvalues minus 2, 1, 1 times 1.54 times ten to the minus 6 per second squared), inside a uniform planet (three equal eigenvalues, volume meter falls) and the surface of a neutron star. Design rule: the volume meter sits beside the shape so that a reader cannot take the egg for a shrinking ball.
- `two-walkers-set-off-side-by-side` (supporting): Two straight walkers on a ball with a string at matching counts: the deviation vector and its along-path piece, and the printed readings at equal stretches whose extra per stretch is the geodesic deviation equation in finite steps.

## Tutor

Opening question: Picture two steel balls released one metre apart, side by side, inside a capsule falling down an airless tower. The capsule's accelerometer reads zero the whole way down. Does the gap between the balls stay one metre, grow, or shrink, and what decides how fast?

- Q: Why does the Moon raise bigger tides than the Sun when the Sun pulls harder? A: Because tides come from the difference in pull across Earth, not from the pull itself. The pull weakens with the square of the distance, but the difference across a fixed gap weakens with the cube. The Sun is about three hundred and ninety times farther away than the Moon and pulls about a hundred and eighty times harder, so its tide is a hundred and eighty over three hundred and ninety of the Moon's, a little under half.
- Q: Does a ball of free particles falling near a planet get squashed by gravity? A: It gets reshaped, not squashed. Along the line to the planet's centre the particles drift apart, and across that line they drift together by half as much in each of the two directions. The three fractional changes add to zero, so at first the ball becomes an egg of the same volume. That zero is the trace of the tidal matrix, which is a Ricci component, and it vanishes outside matter. Only mass inside the ball makes its volume start to shrink.

## Review: novice

Verdict fixed (2026-09-16, revision 4)

Retell attempt: Two things falling freely side by side feel nothing, but their gap changes because the field differs between the two places. In Newton's theory you subtract the two equations of motion and Taylor-expand: the relative acceleration is minus the second-derivative matrix of the potential times the separation. The field itself cancels, only its change from place to place matters, and outside a spherical mass the matrix has eigenvalues minus 2, 1, 1 times GM over r cubed, so radial gaps grow and transverse gaps shrink; at Earth's surface GM over r cubed is about 1.5 millionths per second squared, which closes a 1 metre transverse gap by 17 microns in a 4.7 second drop. In relativity there is no common time, so you take a family of geodesics labelled by s with proper time along each, and the deviation vector is the s-derivative of position. Because mixed partials commute and the Christoffel symbols are symmetric, the covariant rate of the deviation vector along the geodesic equals the velocity gradient across the family; that is Lie dragging, which does not mean constant. The part of the deviation vector along u is a clock offset; the orthogonal part is the separation. Differentiate again and try to swap the two covariant derivatives: you cannot for free, the cost is a Riemann term, and since the members are geodesics you get the geodesic deviation equation, minus Riemann fed u, xi, u. It is linear in xi, ignores the clock offset, vanishes in flat spacetime, and on a sphere gives f double prime equals minus f over a squared, so walkers from the equator meet at the pole. Grouping the two u slots gives the tidal tensor; in the observer's gyroscope frame it is a real symmetric 3 by 3 matrix, c squared times R i 0 j 0, whose eigenvectors are the main directions, and in a weak static field it becomes the second-derivative matrix of the potential, so Newton is the weak-field limit. Its trace is the Ricci component along u, and that sets the initial fractional volume acceleration of a small released ball; Newton's trace is 4 pi G rho, zero outside matter, so outside a planet the ball becomes an egg of the same volume and only matter inside the ball makes it shrink. I could not have reproduced why u dot xi is constant without looking back, and I was unsure whether s in the sphere check was still the family label.

17 stumbles

- “The trace of that tidal matrix is a Ricci component”: 'that tidal matrix' points back to something the summary never called a matrix; the ambiguous 'that'.
- “which is why the capsule's accelerometer reads zero while the gap closes”: The cancellation of the field in the gap equation is presented as the reason the accelerometer reads zero; the accelerometer reads zero because it is in free fall. The step linking the two was implicit.
- “Acting on x-hat the matrix gives x-hat minus 3 x-hat”: The matrix gives GM over r cubed times that; 'the matrix' and 'the bracket' were being used for one another.
- “while t times the square root of GM over r cubed stays small”: No reason given why the closing follows one half k t squared only then.
- “Relativity has no shared instant t. Replace it with a family.”: Replace what with a family? An instant cannot be replaced by a family of paths; the step was implicit.
- “Add Gamma u xi to both sides ... so the same term has been added on each side”: Adding one term to both sides is trivially the same term; the point that the two sides need Gamma xi u and Gamma u xi, which symmetry makes equal, was left implicit, so the role of symmetry was lost.
- “d(u xi)/d tau = u D u/ds”: One step skipped: u dot D xi/d tau equals u dot Du/ds by the rate equation.
- “with no extra term because the two grid directions commute”: Which extra term? The reader knows the curvature operator subtracts a derivative along the Lie bracket, but the sentence does not say that is the term meant, nor that [u, xi] = 0 was just derived.
- “where arc length s takes the place of tau”: s was the family label two paragraphs earlier; one symbol for two ideas, and f = f0 cos(s/a) then reads as a function of the family label.
- “the one independent component of Symmetries and identities makes R = (g g - g g)/a^2”: The step from 'one component' to this formula with 1/a^2 was implicit; the reader knows K = 1/a^2 from the constant-curvature section but was not told K is that component.
- “A positive entry along a direction pulls neighbours back together”: 'entry along a direction' is undefined before eigenvectors are introduced; a matrix entry has two indices.
- “The 0-hat component of the equation is zero on both sides”: A surprising claim with no reason: why is the second derivative of xi^0 zero?
- “For a slow observer”: Slow relative to what was not said.
- “Release crumbs at rest on a small sphere ... with nothing among them”: Ambiguous: no matter between the crumbs, or the crumbs do not attract each other? The same part then puts the cloud inside a planet, so 'nothing among them' cannot be a blanket assumption.
- “the fractional change of a volume is the sum of the fractional changes of three perpendicular lengths”: Stated without its reason; the reader needs the ellipsoid whose volume is the product of its half-axes.
- “an egg 0.154 mm longer along the radius”: Longer measured how: the whole axis or the 1 m radius? The fractions quoted match the 1 m half-axis, but the sentence does not say so.
- “orthogonal part ... measures by radar (glossary)”: Radar appears only in the glossary; the part text names the measurer but no instrument.

Fixes:
- Summary: named the tidal tensor before referring to its trace.
- Part 1: explained why the gap closes while the accelerometer reads zero; said 'the bracket' consistently in the eigenvalue reading; gave the cosine reason for the half k t squared closing.
- Part 2: said what the family replaces; spelled out the two Christoffel terms that symmetry makes equal; added the skipped step in the constancy of u dot xi; named radar as the instrument.
- Part 3: named the Lie-bracket term of the curvature operator and why it vanishes; renamed the sphere's arc length to ell to free s for the family label; made the sphere's Riemann tensor follow from K = 1/a^2.
- Part 4: replaced 'entry along a direction' by feeding the tensor one direction twice; gave both reasons for the vanishing 0-hat component; said what slow means; renamed cloud half-axes from ell to L for consistency with part 3.
- Part 5: replaced 'with nothing among them' by the test-particle statement; added the ellipsoid volume reason; quoted the egg's changes per 1 m half-axis.

Concerns:
- The validator counts 4 469 words after the fixes (4 255 before) against the 5 000 cap; the fixes added about 210 words within the review allowance, and nothing was dropped. Any further addition should drop an item.
- The writer's report is right that observer dependence of the tidal tensor is absent; a reader who asks 'tides for whom?' has only the phrase 'of the observer with four-velocity u' to go on.
- The section relies on The lift and the equivalence principles, Newtonian gravity as a field, The Newtonian limit, The geodesic equation, Lie derivatives, The Levi-Civita connection and Transport along worldlines, all earlier in the outline but not yet written; the exact names of the Newtonian tidal tensor, Lie dragging and parallel-propagated frames must be checked against those sections when they exist.
- The trace's vanishing outside matter in general relativity rests on the earlier Ricci section; the section itself proves only the Newtonian trace. A reader may not notice the gap, which is fine at this depth but the physics reviewer should confirm the earlier section carries it.
- The course conventions still lack a row for the tidal matrix symbol E_ij, as the writer reported.

## Review: physics

Verdict fixed (2026-09-16, revision 4)

19 verification items, 7 counterexamples

- Newtonian deviation equation: subtracting two free falls and Taylor expanding gives xi-ddot^i = -(d_i d_j Phi) xi^j, symmetric tidal tensor: correct
- Hessian of -GM/r is (GM/r^3)(delta_ij - 3 xhat_i xhat_j) with eigenvalues -2GM/r^3 radial and +GM/r^3 transverse: correct; radial pairs separate, transverse pairs close, consistent with course sign (positive tidal entry pulls together)
- GM/r^3 at Earth's surface is 1.54e-6 s^-2; a 110 m airless drop lasts 4.7 s; a 1 m transverse pair closes by 17 microns in 4.7 s and 0.077 mm in 10 s; radial pairs move twice as much: correct; Earth's rotation changes the 4.7 s closing by under 0.4 percent, within the quoted precision
- Rate equation D xi/d tau = D u/ds = xi^nu nabla_nu u^mu and [u, xi] = 0: correct
- u . xi is constant along each geodesic; reparametrising tau -> tau + f(s) adds f'(s) u to xi; the projector h = delta + u u/c^2 gives u . xi_perp = 0: correct
- Geodesic deviation equation D^2 xi/d tau^2 = R^mu_nu alpha beta u^nu u^alpha xi^beta = -R^mu_nu rho sigma u^nu xi^rho u^sigma: correct, matches the course conventions row for geodesic deviation
- Sphere check: R = K(gg - gg) with K = 1/a^2 gives f'' = -f/a^2, f = f0 cos(l/a), zero at l = pi a/2: correct; agrees with the quarter-way meeting of Curved surfaces
- Tidal tensor R^mu_alpha nu beta u^alpha u^beta: kills xi along u, gives accelerations orthogonal to u, and is symmetric when lowered: correct
- In a parallel-propagated orthonormal frame with e_0 = u/c the equation reads xi-ddot^i = -E_ij xi^j with E_ij = c^2 R^i_0j0, and xi^0 = -u.xi/c is constant: correct; E_ij has units s^-2; agrees with the form the Ricci section took on trust
- Weak static field: Gamma^i_00 = d_i Phi/c^2 and c^2 R^i_0j0 = d_i d_j Phi to first order in Phi: correct; sign matches the Newtonian deviation equation
- Outside a non-rotating spherical mass E = (GM/r^3) diag(-2,1,1) exactly for static observers and for radially falling observers: correct; stated as taken on trust in the prose
- Volume law: delta V-ddot/delta V at tau = 0 equals -sum of eigenvalues = -E_ii = -R_mu nu u^mu u^nu: correct
- Newtonian trace: nabla^2 Phi = 4 pi G rho, so -2 + 1 + 1 = 0 outside matter; egg numbers +154, -77, -77 parts in a million after 10 s; inside a uniform ball all eigenvalues equal 4 pi G rho/3: correct
- Check 1: 2 m pair after 5 s closes by 3.85e-5 m: correct
- Check 2: separation of two galaxies 1 Mpc apart grows at 70 km/s under d xi/dt = H xi: correct
- Check 3: rho = 5500 kg/m^3 gives 4 pi G rho/3 = 1.54e-6 s^-2, each axis -77 ppm, volume -231 ppm = (1/2)(4 pi G rho) t^2; beside Earth the volume change is zero: correct; Earth's mean density 5513 kg/m^3 makes the two sets of eigenvalues equal in magnitude, as the check's numbers show
- Tutor: the Sun is about 390 times farther than the Moon, pulls about 180 times harder, and raises a little under half the Moon's tide: correct
- Key equations: all six are derived in the parts and marked derived-here; the exact Schwarzschild pattern and the general-relativistic vanishing of the trace outside matter are taken on trust and the prose now says so: correct after adding the on-trust sentence for the trace
- Section names cited in the text match the outline and the written sections: three names corrected; constant-curvature section added to builds_on since the sphere check cites it

Fixes:
- Part 4: added one sentence on the observer dependence of the tidal tensor (the concern both earlier reports raised).
- Part 5: said that the general-relativistic vanishing of the trace outside matter, with no cosmological constant, is a consequence of Einstein's equation taken on trust here, instead of leaving only the Newtonian argument.
- Part 3 and 4 and 5: cited section names corrected to the outline titles (The Newtonian limit and the weak-field metric; Constant curvature, the Weyl tensor and invariants; the Ricci section's title), and the constant-curvature section added to builds_on.
- Glossary: main directions now include the zero-eigenvalue case.

Concerns:
- The course conventions have no row for the tidal matrix symbol E_ij = c^2 R^i_0j0; this section and the Ricci section both use it, so a row should be added rather than a section-local choice.
- Seven builds_on sections are not yet written; the borrowed names (Newtonian tidal tensor, tidal force, Lie dragged, parallel-propagated frame, weak-field metric) match those sections' outline concept lists but must be re-checked when the sections exist.
- No further references: the section is working depth and cites nothing, so nothing needed web verification.
