# Curves and surfaces in space

`curvature/curves-and-surfaces-in-space` · main track · working depth · physics-reviewed · revision 3 · 2026-09-16

Teaches: `curvature-of-a-curve`, `frenet-serret-equations`, `second-fundamental-form`, `normal-curvature`, `principal-curvatures`, `gaussian-curvature`, `theorema-egregium`

Builds on: `curved-surfaces`, `coordinates-curves-and-surfaces`, `linear-algebra`, `vector-calculus`, `the-metric`, `hypersurfaces-and-embeddings`, `the-levi-civita-connection`, `the-geodesic-equation`

**Seen from outside, a path bends at some angle per metre, and a surface bends by an amount that can change with direction, coded in the second fundamental form. The largest and smallest bends multiply to one number, the Gaussian curvature, and Gauss proved that this product depends only on lengths measured along the surface: it is the number the ring test reads.**

Rest a flat ruler on top of a basketball about 75 centimetres around and look from the side, with your eye level with the ruler. Light shows under it on both sides of the touching point: about 1.7 millimetres of gap two centimetres out, about 7 millimetres four centimetres out, four times as much for twice the distance. Now lay the ruler on a drinks can lying on its side. Along the can it touches the whole way; across the can the gap opens as on the ball. *Curved surfaces* showed with rings and triangles that the can is flat for an ant and the ball is not, with no view from outside. This section takes the outside view and turns the gap under the ruler into numbers: the bend of a curve, the bends of a surface in every direction, and the largest and smallest of them. It ends with Gauss's theorem that one product of those outside bends is the number the ant's rings read.

## Turn per metre as a derivative

Describe a smooth curve in space by its position $\mathbf r(s)$, with $s$ the arc length along it, as in *Coordinates, curves and surfaces*. A step $ds$ along the curve moves the position by $|d\mathbf r| = ds$, so $\hat{\mathbf T} = d\mathbf r/ds$ is a unit vector along the direction of travel. The curvature of the curve is the rate at which this unit tangent turns per unit length,

$$\kappa = \left|\frac{d\hat{\mathbf T}}{ds}\right|, \qquad R = \frac{1}{\kappa},$$

in radians per metre. Differentiating $\hat{\mathbf T}\cdot\hat{\mathbf T} = 1$ gives $\hat{\mathbf T}\cdot d\hat{\mathbf T}/ds = 0$. So where $\kappa \neq 0$, $d\hat{\mathbf T}/ds = \kappa\hat{\mathbf N}$, with $\hat{\mathbf N}$, the principal normal, a unit vector at right angles to the curve, pointing to the side the curve turns toward. The circle of radius $R$ through the point, tangent to the curve and centred at $\mathbf r + R\hat{\mathbf N}$, is the osculating circle: it shares the curve's position, direction and turning rate there, and $R$ is the radius of curvature. On a circle of radius $a$ the same calculation gives $\kappa = 1/a$ everywhere, with $\hat{\mathbf N}$ pointing at the centre.

Curves rarely come parametrized by arc length, but $ds = |d\mathbf r|$ converts any parameter. For a graph $y(x)$ in a plane, walked toward increasing $x$, the tangent makes the angle $\theta$ with the $x$ axis, where $\tan\theta = y'$ and $ds = \sqrt{1 + y'^2}\,dx$. Differentiating $\tan\theta = y'$ gives $d\theta/dx = y''/(1 + y'^2)$, so the signed curvature is $k = d\theta/ds = y''/(1 + y'^2)^{3/2}$ and $\kappa = |k|$; $k > 0$ where the graph is concave up, turning toward $+y$; on the usual plot, $x$ to the right and $y$ up, that is the walker's left when the walker's head points at the viewer. The curvature equals the second derivative only where the graph is level.

A curve has no intrinsic curvature. Bending a wire without stretching keeps every length along it, so a creature that measures only along the wire never learns of its bends; everything in this part is extrinsic, in the sense of *Curved surfaces*.

*The curvature of a curve is how fast its unit tangent turns per unit arc length; its reciprocal is the radius of the osculating circle.*

## The frame that rides a space curve

A curve in space can also climb out of the plane of its osculating circle, like the coils of a spring. Where $\kappa > 0$, complete $\hat{\mathbf T}$ and the principal normal $\hat{\mathbf N}$ with the binormal $\hat{\mathbf B} = \hat{\mathbf T}\times\hat{\mathbf N}$, so that the three form a right-handed orthonormal triad, the Frenet frame. Its derivative along the curve is fixed by two facts. Write the derivative of each frame vector in the frame itself, $\hat{\mathbf e}_i' = M_{ij}\hat{\mathbf e}_j$, so that $M_{ij} = \hat{\mathbf e}_i'\cdot\hat{\mathbf e}_j$. Differentiating $\hat{\mathbf e}_i\cdot\hat{\mathbf e}_j = \delta_{ij}$ for any two frame vectors gives $\hat{\mathbf e}_i'\cdot\hat{\mathbf e}_j = -\hat{\mathbf e}_i\cdot\hat{\mathbf e}_j'$, that is $M_{ij} = -M_{ji}$: the matrix is antisymmetric, with zeros on its diagonal. And $\hat{\mathbf T}' = \kappa\hat{\mathbf N}$ has no $\hat{\mathbf B}$ part, because $\hat{\mathbf N}$ was defined as the direction $\hat{\mathbf T}$ turns toward. That leaves one free entry, the torsion $\tau$, defined by $\hat{\mathbf B}' = -\tau\hat{\mathbf N}$:

$$\frac{d}{ds}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix} = \begin{pmatrix}0&\kappa&0\\-\kappa&0&\tau\\0&-\tau&0\end{pmatrix}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix}.$$

These are the Frenet–Serret equations. The torsion is the rate, in radians per metre, at which the osculating plane tips about the tangent; it vanishes along a curve that stays in one plane, because $\hat{\mathbf B}$ is then constant. The sign is chosen so that a right-handed helix, coiled like an ordinary screw thread, has $\tau > 0$; a mirror image keeps $\kappa$ and reverses $\tau$. Given $\kappa(s) > 0$ and $\tau(s)$, the equations can be integrated from a starting point and starting frame, so curvature and torsion fix a space curve up to a rigid motion. This is the pattern the rest of the section repeats for a surface: carry a frame along, split its derivative, and read the geometry from the coefficients.

*Along a space curve the Frenet frame turns about the binormal at the curvature and tips about the tangent at the torsion; the two rates fix the curve up to a rigid motion.*

## The gap under a card, in formulas

Now the surface. Parametrize a smooth surface in flat three-dimensional space by $\mathbf X(x^1, x^2)$, as in *Coordinates, curves and surfaces*. The basis vectors $\mathbf e_\mu = \partial_\mu\mathbf X$ span the tangent plane at each point, and the induced metric of *Hypersurfaces and embeddings*, $g_{\mu\nu} = \mathbf e_\mu\cdot\mathbf e_\nu$, gives every length along the surface. The surface has two unit normals; take $\hat{\mathbf n} = \mathbf e_1\times\mathbf e_2/|\mathbf e_1\times\mathbf e_2|$, the one the order of the coordinates picks out, and keep that choice.

Replace the opening's ruler by a flat card touching the surface at one point: the card is the tangent plane, and the ruler was one line across it. The second derivatives of $\mathbf X$ say how the surface leaves the card. Split the change of each basis vector into a part in the tangent plane and a part along the normal:

$$\partial_\mu\mathbf e_\nu = \Gamma^\lambda{}_{\mu\nu}\,\mathbf e_\lambda + K_{\mu\nu}\,\hat{\mathbf n}.$$

This is Gauss's formula, and its tangential coefficients are the Christoffel symbols of $g_{\mu\nu}$, as in *The Levi-Civita connection*. To see this, dot the formula with $\mathbf e_\sigma$: the normal part drops out, leaving $A_{\sigma\mu\nu} = \mathbf e_\sigma\cdot\partial_\mu\mathbf e_\nu = g_{\sigma\lambda}\Gamma^\lambda{}_{\mu\nu}$, symmetric in its last two indices because $\partial_\mu\mathbf e_\nu = \partial_\mu\partial_\nu\mathbf X$. Differentiating $g_{\sigma\nu} = \mathbf e_\sigma\cdot\mathbf e_\nu$ gives $\partial_\mu g_{\sigma\nu} = A_{\sigma\mu\nu} + A_{\nu\mu\sigma}$. So $\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu}$ equals $2A_{\sigma\mu\nu}$, because the four other terms cancel in pairs by that symmetry. Multiplying by $\tfrac12 g^{\rho\sigma}$ gives $\Gamma^\rho{}_{\mu\nu} = \tfrac12 g^{\rho\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$, the Christoffel symbols.

The normal coefficients $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$ are the second fundamental form. They are symmetric because partial derivatives commute, positive where the surface bends toward $\hat{\mathbf n}$, and they change sign with the choice of normal. In coordinates that are Cartesian on the tangent plane at a point, with the height $z$ measured along $\hat{\mathbf n}$, the Taylor series of $z$ starts at second order, $z = \tfrac12 K_{\mu\nu}x^\mu x^\nu$ plus terms of third order in the distance from the point: the gap under the card grows as the square of the distance, at a rate that depends on direction.

The normal tilts as the basis vectors bend. Differentiating $\hat{\mathbf n}\cdot\mathbf e_\nu = 0$ gives $\partial_\mu\hat{\mathbf n}\cdot\mathbf e_\nu = -K_{\mu\nu}$, and $\hat{\mathbf n}\cdot\hat{\mathbf n} = 1$ makes $\partial_\mu\hat{\mathbf n}$ tangential, so

$$\partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda, \qquad K^\lambda{}_\mu = g^{\lambda\nu}K_{\nu\mu},$$

Weingarten's equation. On a sphere of radius $a$ with the outward normal, $\mathbf X = a\hat{\mathbf n}$ gives $K^\lambda{}_\mu = -\delta^\lambda{}_\mu/a$: the normal tilts by $1/a$ radians per unit distance in every direction, for Earth $1^\circ$ every $111$ km, the rate at which a plumb line tilts against the stars as a surveyor walks. On a can of radius $a$, with arc length $u$ around it and distance $v$ along it, the outward normal gives $K_{uu} = -1/a$ and $K_{vv} = K_{uv} = 0$: the ruler's zero gap along the can and open gap across it.

*A surface basis vector's derivative splits into Christoffel symbols along the surface and the second fundamental form along the normal, the rate at which the gap under a touching card grows in each direction.*

## Split the bend of a surface curve

Walk along any unit-speed curve lying in the surface, with unit tangent $\mathbf T = t^\mu\mathbf e_\mu$. Its curvature vector $d\mathbf T/ds$ is perpendicular to $\mathbf T$, so it has a part along $\hat{\mathbf n}$ and a part along $\hat{\mathbf u} = \hat{\mathbf n}\times\mathbf T$, the unit vector in the tangent plane that points to the walker's left when the walker's head is along $\hat{\mathbf n}$:

$$\frac{d\mathbf T}{ds} = \kappa_n\,\hat{\mathbf n} + \kappa_g\,\hat{\mathbf u}, \qquad \kappa^2 = \kappa_n^2 + \kappa_g^2.$$

The normal curvature $\kappa_n$ is the bend that comes from following the surface as it curves away beneath the walker; the geodesic curvature $\kappa_g$ is the bend that comes from steering along the surface, positive when the walker steers toward the left just defined. They are perpendicular components, so their squares add, not the parts themselves.

Gauss's formula computes both at once. Since $d\mathbf e_\mu/ds = t^\nu\partial_\nu\mathbf e_\mu$,

$$\frac{d\mathbf T}{ds} = \Big(\frac{dt^\lambda}{ds} + \Gamma^\lambda{}_{\mu\nu}\,t^\mu t^\nu\Big)\mathbf e_\lambda + K_{\mu\nu}\,t^\mu t^\nu\,\hat{\mathbf n}.$$

So $\kappa_n = K_{\mu\nu}t^\mu t^\nu$, fixed by the direction of travel alone: every curve through a point in the same direction has the same normal curvature, however it steers. The tangential bracket is the left side of the geodesic equation of *The geodesic equation*, with arc length as the parameter. So $\kappa_g$ vanishes all along a curve exactly when the curve is a geodesic, the straight walk of *Curved surfaces*. The bracket contains only the metric and its derivatives, so an ant can measure $\kappa_g$, while $\kappa_n$ stays out of her reach.

On a sphere of radius $a$ with the outward normal, $K_{\mu\nu} = -g_{\mu\nu}/a$, so $\kappa_n = -1/a$ for every direction, negative because the surface bends away from the outward normal: the equator, with $\kappa = 1/a$, bends toward the centre and never steers. A circle of latitude at colatitude $\theta_0$, the angle from the North Pole seen from the centre, walked eastward, has radius $a\sin\theta_0$ in space, so $\kappa = 1/(a\sin\theta_0)$, and $\kappa_g^2 = \kappa^2 - \kappa_n^2$ gives $\kappa_g = \cot\theta_0/a$, positive north of the equator, where the circle bends toward the pole on the walker's left.

*A surface curve's curvature vector splits into normal curvature, fixed by the direction alone, and geodesic curvature, which uses only the metric and vanishes exactly on geodesics; their squares add.*

## Sharpest and gentlest bends

At a point, turn the direction of travel through every angle and watch $\kappa_n = K_{\mu\nu}t^\mu t^\nu$, with $g_{\mu\nu}t^\mu t^\nu = 1$. Its largest and smallest values are the principal curvatures $\kappa_1 \ge \kappa_2$, and the directions where they occur are the principal directions. A Lagrange multiplier, as in *Vector calculus*, finds the extremes: setting the derivative of $K_{\mu\nu}t^\mu t^\nu - \lambda(g_{\mu\nu}t^\mu t^\nu - 1)$ with respect to $t^\mu$ to zero gives $K_{\mu\nu}t^\nu = \lambda g_{\mu\nu}t^\nu$, and contracting with $t^\mu$ shows $\lambda = \kappa_n$ in that direction. Raising the index,

$$K^\mu{}_\nu\,t^\nu = \lambda\,t^\mu, \qquad K^\mu{}_\nu = g^{\mu\sigma}K_{\sigma\nu}.$$

So each extreme direction is an eigenvector of the mixed tensor $K^\mu{}_\nu$, the shape operator, with its normal curvature $\lambda$ as the eigenvalue: the principal curvatures are the eigenvalues of the shape operator, and the principal directions are its eigenvectors. Its eigenvalues do not depend on the coordinates, because the eigenvalue equation is a tensor equation and holds in every coordinate system; those of the component matrix $K_{\mu\nu}$ do, and agree with the principal curvatures only in a basis that is orthonormal at the point. In such a basis $K^\mu{}_\nu$ is a real symmetric matrix, so by *Linear algebra* its eigenvalues are real and, when they differ, its eigenvectors are perpendicular: the sharpest and gentlest bends are a quarter turn apart, unless every direction bends alike, as at every point of a sphere.

Measure the angle $\psi$ of a unit direction from the $\kappa_1$ direction, in an orthonormal basis along the principal directions. Then $t = (\cos\psi, \sin\psi)$ and $K_{\mu\nu} = \mathrm{diag}(\kappa_1, \kappa_2)$ give Euler's formula,

$$\kappa_n(\psi) = \kappa_1\cos^2\psi + \kappa_2\sin^2\psi,$$

so every normal curvature at the point follows from two numbers. Reversing $\hat{\mathbf n}$ negates $K_{\mu\nu}$ and both principal curvatures, and swaps which is called $\kappa_1$; the directions and the product $\kappa_1\kappa_2$ do not change.

A sphere with the outward normal has $\kappa_1 = \kappa_2 = -1/a$ everywhere. The can has $0$ along its length and $-1/a$ around it. The saddle $z = (x^2 - y^2)/(2a)$ has $K_{xx} = 1/a$ and $K_{yy} = -1/a$ at the origin with $\hat{\mathbf n}$ along $+z$, so $\kappa_n = \cos 2\psi/a$: it bends toward $\hat{\mathbf n}$ along $x$ and away from it along $y$.

*The principal curvatures are the eigenvalues of the shape operator, the second fundamental form with one index raised; their directions are perpendicular, and Euler's formula gives every other normal curvature from them.*

## One number for a spot

Multiply the two principal curvatures. The product of the eigenvalues of $K^\mu{}_\nu = g^{\mu\sigma}K_{\sigma\nu}$ is its determinant, and the determinant of a product is the product of the determinants, so

$$K = \kappa_1\kappa_2 = \frac{\det K_{\mu\nu}}{\det g_{\mu\nu}},$$

the Gaussian curvature of the point. It is the same for either choice of normal, and it has units of inverse length squared, so enlarging a surface to twice its size divides $K$ by four. The symbol $K$ without indices means this number throughout the book, never a component of $K_{\mu\nu}$.

The sign sorts surfaces into the three kinds that *Curved surfaces* met. A sphere of radius $a$ has $K = (-1/a)(-1/a) = 1/a^2$. A can has $K = 0\times(-1/a) = 0$, although it is bent: one unbent direction is enough for zero. A saddle bends toward opposite faces, so $\kappa_1 > 0 > \kappa_2$ and $K < 0$; for $z = (x^2 - y^2)/(2a)$ at the origin, $K = -1/a^2$. Equal bends toward opposite faces do not cancel; they multiply to a negative number.

Weingarten's equation adds a picture. Along each principal direction the normal tilts by the principal curvature times the distance walked, so a small rectangle with sides $dx$ and $dy$ along the two principal directions sends its normals onto a rectangle of directions with sides $|\kappa_1|\,dx$ and $|\kappa_2|\,dy$: the normals of a patch of area $dA$ sweep a solid angle $|K|\,dA$ on the unit sphere, $A/a^2$ for a patch of area $A$ on a sphere and a curve of directions with no area for a can.

So far $K$ is an outsider's number, built from $\hat{\mathbf n}$ and the second derivatives of $\mathbf X$, neither of which an ant on the surface can reach. The last part removes the outsider.

*The Gaussian curvature is the product of the principal curvatures, the determinant of the second fundamental form over that of the metric: positive on a ball, zero on a can, negative on a saddle, whichever normal is chosen.*

## The ant and the outsider agree

The ant's number comes from the line element of *The metric*. Around any point of a smooth surface, let $\rho$ be the distance walked along a straight walk from the point and $\phi$ the direction the walk set off in; the line element then takes the form $ds^2 = d\rho^2 + f(\rho, \phi)^2\,d\phi^2$, with no $d\rho\,d\phi$ term because each ring of end marks crosses the straight walks at right angles. For every line element of this form, whatever the function $f$, the curvature is

$$K = -\frac{1}{f}\,\frac{\partial^2 f}{\partial\rho^2}.$$

Both the form of the line element and this formula are taken on trust here; the section *Holonomy and the Riemann tensor* reaches the same combination of the metric and its derivatives from inside the surface. The plane has $f = \rho$, so $K = 0$. A sphere of radius $a$ has $f = a\sin(\rho/a)$, the length of the ring test's ring in *Curved surfaces* divided by $2\pi$, so $\partial_\rho^2 f = -f/a^2$ and $K = 1/a^2$, the outsider's product. Near the starting point $f(0) = 0$ and $\partial_\rho f(0) = 1$, because a tiny ring has its playground length to first order, and differentiating $\partial_\rho^2 f = -Kf$ once gives $\partial_\rho^3 f(0) = -K$, so the ring of straight walks of length $\rho$ has length $2\pi f = 2\pi\rho\,(1 - K\rho^2/6 + \dots)$. The ring test reads $K$: the missing fraction of a small ring is $K\rho^2/6$, and on Earth the ring of $1$-kilometre straight walks is short by $0.026$ millimetres.

Now the theorem. Gauss proved in 1827 that for every smooth surface in flat space, $\det K_{\mu\nu}/\det g_{\mu\nu}$ can be written in terms of $g_{\mu\nu}$ and its first two derivatives alone, and equals the $K$ of the line element. He called it the theorema egregium, the remarkable theorem, because each factor $\kappa_1$, $\kappa_2$ needs the outside view, yet the product does not. The mechanism is short. Mixed partial derivatives commute, so $\partial_\mu\partial_\nu\mathbf e_\sigma = \partial_\nu\partial_\mu\mathbf e_\sigma$. Expanding both sides with Gauss's and Weingarten's formulas and comparing the tangential parts forces $K_{\alpha\mu}K_{\beta\nu} - K_{\alpha\nu}K_{\beta\mu}$ to equal a combination of Christoffel symbols and their derivatives, hence of the metric and its first two derivatives. On a surface that antisymmetric combination has one independent component, $K_{11}K_{22} - K_{12}K_{21} = \det K_{\mu\nu}$.

A surface of revolution shows the two routes meeting. Let $\rho$ be arc length along a profile curve at distance $r(\rho)$ from the axis and height $z(\rho)$, with $r'^2 + z'^2 = 1$, and $\phi$ the angle around the axis. Then $ds^2 = d\rho^2 + r^2\,d\phi^2$, the trusted form with $r$ as the ring function, so the ant finds $K = -r''/r$. The outsider places $\mathbf X = (r\cos\phi, r\sin\phi, z)$ with $\hat{\mathbf n} = (-z'\cos\phi, -z'\sin\phi, r')$ and finds $K_{\rho\phi} = 0$, so the profile and the circles are principal directions, with normal curvature $\kappa_{\rm m} = \hat{\mathbf n}\cdot\partial_\rho^2\mathbf X = r'z'' - z'r''$ along the profile (the meridian) and $\kappa_{\rm p} = \hat{\mathbf n}\cdot\partial_\phi^2\mathbf X/r^2 = z'/r$ around the circle (the parallel), the division by $r^2 = g_{\phi\phi}$ because the unit tangent around the circle has $t^\phi = 1/r$. Differentiating $r'^2 + z'^2 = 1$ gives $z'z'' = -r'r''$, so $z'\kappa_{\rm m} = -r'^2r'' - z'^2r'' = -r''$, and

$$\kappa_{\rm m}\kappa_{\rm p} = -\frac{r''}{r} = K.$$

The line element fixes the product, not the factors. The family $r = b\sin(\rho/a)$ with $0 < b \le a$ all have $r'' = -r/a^2$, hence $K = 1/a^2$: each is a sphere of radius $a$ for the ant away from its two tips, which for $b < a$ are sharp points like a cone's, since near them $r \approx b\rho/a$ rather than $\rho$; yet at its middle the bends are $1/b$ around the axis and $b/a^2$ along the profile. Bending without stretching keeps $g_{\mu\nu}$, so it keeps $K$ while trading one bend against the other. For general relativity the theorem is the licence to speak of curvature with no outside at all. The number the ant measures is the whole story, and the sections that follow build it from the metric alone.

*The Gaussian curvature can be computed from the line element alone, so bending without stretching never changes it: the outsider's product of two bends is the number the ant's rings read.*

## Key equations

**Frenet–Serret equations** (derived-here)

$$\frac{d}{ds}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix} = \begin{pmatrix}0&\kappa&0\\-\kappa&0&\tau\\0&-\tau&0\end{pmatrix}\begin{pmatrix}\hat{\mathbf T}\\ \hat{\mathbf N}\\ \hat{\mathbf B}\end{pmatrix}$$

The Frenet frame stays orthonormal, so its derivative matrix is antisymmetric: the tangent turns toward the normal at the curvature, and the binormal tips at the torsion, positive for a right-handed helix.

- $\hat{\mathbf B}$: binormal, tangent crossed with principal normal
- $\tau$: torsion, in radians per unit length

Say: The derivative of the tangent is kappa times the normal; the derivative of the normal is minus kappa times the tangent plus tau times the binormal; the derivative of the binormal is minus tau times the normal.

**Gauss's formula and Weingarten's equation** (derived-here)

$$\partial_\mu\mathbf e_\nu = \Gamma^\lambda{}_{\mu\nu}\,\mathbf e_\lambda + K_{\mu\nu}\,\hat{\mathbf n},\qquad \partial_\mu\hat{\mathbf n} = -K^\lambda{}_\mu\,\mathbf e_\lambda$$

A basis vector's change splits into Christoffel symbols along the surface and the second fundamental form $K_{\mu\nu} = \hat{\mathbf n}\cdot\partial_\mu\partial_\nu\mathbf X$ along the normal, positive toward the chosen normal; the normal tilts back by the same form with an index raised.

- $K_{\mu\nu}$: second fundamental form, symmetric, changes sign with the normal

Say: The derivative of a basis vector is the Christoffel symbol times a basis vector plus the second fundamental form times the normal, and the derivative of the normal is minus the second fundamental form with one index raised, times a basis vector.

**Normal and geodesic curvature of a surface curve** (derived-here)

$$\frac{d\mathbf T}{ds} = \kappa_n\,\hat{\mathbf n} + \kappa_g\,\hat{\mathbf u},\qquad \kappa_n = K_{\mu\nu}t^\mu t^\nu,\qquad \kappa_g\,\hat{\mathbf u} = \Big(\frac{dt^\lambda}{ds} + \Gamma^\lambda{}_{\mu\nu}t^\mu t^\nu\Big)\mathbf e_\lambda$$

The curvature vector of a unit-speed surface curve splits into a normal part fixed by its direction alone and a tangential part, the geodesic equation's left side, positive toward the walker's left with the head along the normal.

- $\kappa_n$: normal curvature, positive when the curve bends toward the chosen normal
- $\kappa_g$: geodesic curvature, positive when the curve bends toward the walker's left

Say: The derivative of the tangent is the normal curvature times the normal plus the geodesic curvature times the leftward unit vector; the normal curvature is the second fundamental form contracted twice with the tangent, and the geodesic part is the geodesic equation's left side.

**Gaussian curvature as a product of bends** (derived-here)

$$K = \kappa_1\kappa_2 = \frac{\det K_{\mu\nu}}{\det g_{\mu\nu}}$$

The product of the principal curvatures is the determinant of the shape operator, independent of the normal and of the coordinates, in units of inverse length squared.

- $K$: Gaussian curvature, one number per point

Say: The Gaussian curvature is kappa one times kappa two, which equals the determinant of the second fundamental form divided by the determinant of the metric.

**Gaussian curvature from the line element** (stated)

$$ds^2 = d\rho^2 + f(\rho,\phi)^2\,d\phi^2,\qquad K = -\frac{1}{f}\frac{\partial^2 f}{\partial\rho^2},\qquad 2\pi f = 2\pi\rho\Big(1 - \frac{K\rho^2}{6} + \dots\Big)$$

For any line element of this form, for example with distance and direction from a point as coordinates, the Gaussian curvature is minus the second distance-derivative of the ring function over the ring function, so a small ring is short by the fraction $K\rho^2/6$; taken on trust here.

- $f$: ring function: the ring at distance rho has length two pi f

Say: With the line element d rho squared plus f squared d phi squared, the Gaussian curvature is minus the second rho-derivative of f divided by f, and a small ring is short by K rho squared over six.

## Checks

**curvature-of-a-cubic-graph** (numeric): A path in a level plane follows the graph of y equals x cubed over three, with x and y in metres. A friend says the curvature at x equals 1 is the second derivative, 2 per metre, so the osculating circle there has radius 0.5 metres. Find the actual radius of curvature at x equals 1, and say where the friend's rule does hold.

Answer: At $x = 1$, $y' = 1$ and $y'' = 2$, so $k = y''/(1 + y'^2)^{3/2} = 2/2^{3/2} = 0.707$ per metre and $R = 1.41$ m, nearly three times the friend's radius. Curvature is the turning rate per unit arc length: where the graph slopes, a step $dx$ covers arc length $\sqrt{1 + y'^2}\,dx$ while the tangent turns by $y''\,dx/(1 + y'^2)$. The friend's rule holds only where $y' = 0$, here at $x = 0$, where the curvature is zero.

Key points: Curvature is y double prime over one plus y prime squared to the three halves: 0.707 per metre, radius 1.41 m; It equals the second derivative only where the graph is level

Numeric: radius of curvature at x = 1 = 1.414 m

**ring-on-a-smooth-planet** (numeric): Surveyors on a smooth planet walk straight out 50 kilometres from a centre in many directions and measure the ring of end marks along the ground at 314.028 kilometres. Find the Gaussian curvature there and the radius of the ball with that curvature. A geologist says the crust under the survey was later bent by a slow uplift, without stretching or tearing. Could a repeat survey read a different curvature?

Answer: The flat ring would be $2\pi\times50 = 314.16$ km, so the ring is short by $0.131$ km, a missing fraction of $4.18\times10^{-4} = K\rho^2/6$. So $K = 6\times4.18\times10^{-4}/(50\ \text{km})^2 = 1.0\times10^{-6}$ km$^{-2}$, which is $1.0\times10^{-12}$ m$^{-2}$, and the matching ball has radius $1/\sqrt K = 1000$ km. Bending without stretching keeps every length along the ground, hence the metric, and the theorema egregium then keeps $K$: the repeat survey reads the same ring.

Key points: The missing fraction K rho squared over six gives one millionth per square kilometre, a matching ball of radius 1000 km; Bending without stretching keeps the metric, so the theorem keeps K

Numeric: Gaussian curvature = 1e-12 m^-2; radius of the matching ball = 1000 km

**steering-around-a-circle-on-a-ball** (numeric): A circle of radius 3 metres in space is drawn on a ball of radius 5 metres, and a walker follows it. A friend says the walker's geodesic curvature is the circle's curvature minus the ball's normal curvature, one third minus one fifth per metre. Find the true geodesic curvature, give it as the radius of the steering circle, one over the geodesic curvature, and say which way the walker steers.

Answer: In space the circle has $\kappa = 1/3$ per metre, and every direction on the ball has $\kappa_n = -1/5$ per metre with the outward normal. The parts are perpendicular, so $\kappa_g^2 = 1/9 - 1/25 = 16/225$ and $\kappa_g = 4/15$ per metre: a steering circle of radius $3.75$ m, not the friend's $7.5$ m. The walker steers toward the smaller of the two caps the circle cuts from the ball; with that cap on the walker's left, head along the outward normal, $\kappa_g$ is positive.

Key points: Squares add: kappa g is the square root of one ninth minus one twenty-fifth, four fifteenths per metre, a steering radius of 3.75 m; The walker steers toward the smaller cap, positive with that cap on the left

Numeric: radius of the steering circle, one over the geodesic curvature = 3.75 m

## Misconceptions

- **curvature-is-the-second-derivative**: "The curvature of a graph is its second derivative." — Curvature is the turning rate per unit arc length, the second derivative over one plus the slope squared to the three halves; the two agree only where the graph is level. (diagnosed by curvature-of-a-cubic-graph)
- **bending-changes-the-number**: "Bending a surface more sharply raises its Gaussian curvature." — Bending without stretching keeps the metric, and the theorema egregium then keeps the Gaussian curvature, trading one bend against the other. (diagnosed by ring-on-a-smooth-planet)
- **parts-simply-add**: "A surface curve's curvature is its normal curvature plus its geodesic curvature." — The two parts are perpendicular components of the curvature vector, so their squares add. (diagnosed by steering-around-a-circle-on-a-ball)

## Glossary

- **curvature of a curve**: How fast a curve's unit tangent turns per unit arc length, in radians per metre; an extrinsic property. (`curvature-of-a-curve`)
- **osculating circle**: The circle sharing a curve's position, direction and turning rate at a point; its radius is the radius of curvature. (`curvature-of-a-curve`)
- **principal normal**: The unit vector at right angles to a curve that points to the side the tangent turns toward; the curvature vector is the curvature times it. (`curvature-of-a-curve`)
- **binormal**: The unit tangent crossed with the principal normal; it is perpendicular to the osculating plane and constant along a plane curve. (`frenet-serret-equations`)
- **Frenet frame**: The right-handed triad of unit tangent, principal normal and binormal carried along a space curve. (`frenet-serret-equations`)
- **torsion**: The rate at which a space curve's osculating plane tips about the tangent; positive for a right-handed helix, zero for a plane curve. (`frenet-serret-equations`)
- **second fundamental form**: The normal components of a surface's second derivatives, positive where the surface bends toward the chosen normal. (`second-fundamental-form`)
- **shape operator**: The second fundamental form with one index raised by the inverse metric; its eigenvalues are the principal curvatures. (`principal-curvatures`)
- **normal curvature**: The part of a surface curve's curvature vector along the surface normal, fixed by the direction of travel alone. (`normal-curvature`)
- **geodesic curvature**: The part of a surface curve's curvature vector in the tangent plane, positive toward the walker's left; zero exactly on geodesics. (`normal-curvature`)
- **principal curvatures**: The largest and smallest normal curvatures at a point, signed relative to the chosen normal; their directions, the principal directions, are perpendicular when the two curvatures differ. (`principal-curvatures`)
- **Gaussian curvature**: The product of the principal curvatures: positive on a ball, zero on a can, negative on a saddle, whichever normal is chosen. (`gaussian-curvature`)
- **theorema egregium**: Gauss's theorem that the Gaussian curvature follows from the metric and its first two derivatives alone, so bending without stretching never changes it. (`theorema-egregium`)

## Visuals

- `card-touching-a-curved-patch` (core): The second fundamental form and the principal curvatures made visible: a card on a patch, the gap read direction by direction, and the product of the two extreme bends beside the ring-test value at the same spot. Sketch: A patch $z = \tfrac12(K_{xx}x^2 + 2K_{xy}xy + K_{yy}y^2)$ touching a translucent card, with presets for a ball, a drinks can, a spoon bowl, a saddle and a crisp turned by $45^\circ$. A ruler pivots about the touching point and plots the gap at a set distance against direction, showing Euler's formula with the principal directions marked a quarter turn apart. A readout gives the product of the two extreme bends, signed by faces, beside the shortfall of a small ring paced out on the same patch, so the two numbers are seen to agree on every preset.
- `bend-arrow-split-on-a-surface` (supporting): A surface curve's curvature vector split live into its normal part and its steering part, on a ball, a can, a saddle and a flat floor. Sketch: A walker moves along a path on a chosen surface; the curvature vector is drawn as an arrow and split into a part along the normal and a part in the tangent plane, with readouts of $\kappa$, $\kappa_n$ and $\kappa_g$ and a check that the squares add. Presets: the equator and a circle of latitude on a ball, a small ring on a ball, a helix around a can, and a straight line on the floor; the geodesic-curvature readout drops to zero exactly on straight walks.

## Tutor

Opening question: Picture a drinks can lying on its side with a ruler resting on top of it, and imagine turning the ruler slowly about the touching point. In which direction does the gap under the ruler grow fastest, in which does it stay zero, and what single number would you give the can for how curved it is? Predict before we compute.

- Q: How can a can have zero Gaussian curvature when it obviously bends? A: The Gaussian curvature is the product of the two extreme bends at a point, and along the can's length there is no bend at all, so the product is zero. The bend you see lives in the second fundamental form, but only the product is something an ant on the can could measure, and her rings come out as on flat paper.
- Q: Spacetime has no outside, so why learn about bends seen from outside? A: Because the theorem says we do not need the outside. The one number built from the outside bends is fixed by lengths measured within the surface, and general relativity keeps only that intrinsic kind of curvature, computed from the metric, which the sections that follow build in any number of dimensions.

## Further

- **Gauss's original memoir on curved surfaces.** The memoir that defines the Gaussian curvature through the sphere of normals, proves that it depends on the line element alone, and relates it to the angle excess of geodesic triangles. Carl Friedrich Gauss (1827), Disquisitiones generales circa superficies curvas

## Review: novice

Verdict fixed (2026-09-16, revision 3)

Retell attempt: A curve's curvature is how fast its unit tangent turns per unit arc length, kappa equals the size of dT/ds, and one over kappa is the radius of the circle that fits the curve there; for a graph it is y double prime over one plus y prime squared to the three halves, so it is the second derivative only where the graph is level. A curve has no intrinsic curvature because bending a wire keeps its lengths. In space a curve carries a frame T, N, B whose derivative matrix is antisymmetric: kappa turns T into N and the torsion tau tips B, and the two functions fix the curve up to a rigid motion. For a surface X of two coordinates with basis vectors e_mu and a unit normal n, the derivative of a basis vector splits into Christoffel symbols along the surface plus K_mu nu along the normal, where K_mu nu = n dot d_mu d_nu X is the second fundamental form, the rate at which the gap under a touching card grows, positive toward the normal; the normal tilts back by minus K with an index raised. A curve drawn on the surface has its curvature vector split into a normal part kappa_n = K t t, fixed by the direction alone, and a geodesic part kappa_g, which the ant can measure and which is zero exactly on geodesics; the squares add. The biggest and smallest normal curvatures are the eigenvalues of K with an index raised, in perpendicular directions, and every other one is kappa_1 cos squared phi plus kappa_2 sin squared phi. Their product is the Gaussian curvature K = det K over det g: one over a squared on a sphere, zero on a can, negative on a saddle, the same for either normal. Gauss's theorem: K can be computed from the metric alone, K = minus f double prime over f for ds squared = d rho squared plus f squared d phi squared, so a small ring is short by K rho squared over six, and bending without stretching keeps K; on a surface of revolution both routes give minus r double prime over r. Things I could not say back: why the line element around a point has no cross term; what 'the course's sense' of left is; why the eigenvalue equation used kappa, the curve's symbol; how tilt rates become a solid angle; what colatitude and the subscripts m and p mean; why a formula stated for distance-and-direction coordinates may be used on a surface of revolution; and why the numbers in the planet check do not come out of the ring length as posed.

25 stumbles

- “a path bends by a turn per metre”: Reads as one full turn per metre; the summary is the first thing spoken.
- “with N a unit vector at right angles to the curve, pointing to the side the curve turns toward”: The next part calls the same vector 'the principal normal' as if the name had been given: two words for one idea.
- “k > 0 where the graph turns toward the walker's left, seen from the side of the plane the walker's head points to”: Direction without its reference: nothing says which side of the plane the head points to, and the sign of k depends on it.
- “so the matrix of derivative components is antisymmetric”: Step left implicit: no matrix was defined, so I could not see what the dot-product identity says about it.
- “Choose one of the two unit normals, n = e1 x e2 / |e1 x e2|, and keep that choice.”: Reread: it says choose, then a formula makes the choice.
- “The gap under a card, in formulas ... the gap under the card grows as the square of the distance”: The opening used a ruler; the card is never introduced, so I did not know whether it was the same object.
- “z = 1/2 K_mu nu x^mu x^nu + O(r^3)”: r is undefined here and later means the distance from an axis.
- “and A_sigma mu nu = g_sigma lambda Gamma^lambda_mu nu follows”: Step left implicit: how A relates to the tangential coefficients of Gauss's formula, and why that makes them the Christoffel symbols, was never said.
- “positive toward the walker's left in the course's sense”: 'The course's sense' is undefined for a reader; the left was defined one sentence earlier.
- “kappa_n = -1/a for every direction: the equator bends toward the centre and never steers”: A negative number sits next to 'bends toward' with no word on why the sign is negative.
- “A circle of latitude at colatitude theta_0”: Undefined word.
- “K^mu_nu t^nu = kappa t^mu”: kappa was the curvature of a curve; here it is an eigenvalue: one symbol for two ideas.
- “Its eigenvalues do not depend on the coordinates”: Surprising claim with no reason, right after being told the component matrix's eigenvalues do depend on them.
- “enlarging a surface by a factor lambda divides K by lambda^2”: lambda was the Lagrange multiplier and an index in the same part.
- “a picture surveyors use ... so the normals of a small patch of area dA sweep a solid angle |K| dA”: Step from two tilt rates to a solid angle left implicit, and 'surveyors use' is a claim with nothing behind it.
- “the line element then takes the form ds^2 = d rho^2 + f(rho, phi)^2 d phi^2”: Surprising claim (no d rho d phi term) with no reason and not marked as taken on trust.
- “The curvature of such a line element is K = -(1/f) d^2 f/d rho^2 ... Then ds^2 = d rho^2 + r^2 d phi^2, so the ant finds K = -r''/r”: The formula was stated for distance-and-direction coordinates around a point, then used on a surface of revolution where phi is the angle round the axis: a general sentence used outside its stated scope.
- “the ring of the ring test in Curved surfaces divided by 2 pi”: A ring is a curve; its length is what is divided.
- “Near the starting point f(0) = 0 and d f/d rho (0) = 1”: Two facts with no reason.
- “The mechanism fits in one sentence: second derivatives of X commute, so ... which is det K_mu nu.”: Sixty words and three steps in one sentence; also the commuting derivatives shown are third derivatives of X.
- “kappa_m = n . d^2_rho X ... and kappa_p = n . d^2_phi X / r^2”: Subscripts m and p undefined, and the division by r^2 unexplained.
- “each is a sphere of radius a for the ant”: Fails the first what-if: for b < a a ring near a tip has length 2 pi (b/a) rho, short by a fixed fraction, the sharp point that Curved surfaces excluded from the ring test.
- “measure the ring of end marks along the ground at 314.03 kilometres”: From 314.03 the shortfall is 0.129 km and the fraction 4.12 x 10^-4, not the answer's 0.131 km and 4.17 x 10^-4; the numbers in the answer cannot be reproduced from the question as posed.
- “with that cap on the left, kappa_g is positive”: Direction without its reference: whose left, with the head along which normal.
- “complete T and the principal normal N with the binormal B”: Neither principal normal nor binormal is in the glossary, although both are used in the Frenet part and its takeaway.

Fixes:
- Summary: 'bends by a turn per metre' became 'bends at some angle per metre'.
- Part turn-per-metre-as-a-derivative: named N the principal normal where it is defined; gave the sign of k for a graph its reference (concave up, +y, walker's head toward the viewer of the usual plot).
- Part the-frame-that-rides-a-space-curve: defined the matrix M_ij = e_i' . e_j before calling it antisymmetric.
- Part the-gap-under-a-card-in-formulas: normal choice reworded; the card introduced as the tangent plane in place of the opening's ruler; the Christoffel argument now closes with the definition of Gamma from The Levi-Civita connection; O(r^3) replaced by words.
- Part split-the-bend-of-a-surface-curve: 'the course's sense' replaced by the left defined in the part; the sign of kappa_n on the sphere explained; colatitude defined.
- Part sharpest-and-gentlest-bends: eigenvalue written as lambda, not kappa; the reason the shape operator's eigenvalues are coordinate-free added.
- Part one-number-for-a-spot: scaling stated with a concrete factor instead of lambda; the solid-angle sentence now shows the rectangle step and no longer claims surveyors use it.
- Part the-ant-and-the-outsider-agree: no-cross-term fact given its reason and marked as trust together with the formula; the formula scoped to every line element of the form d rho^2 + f^2 d phi^2 so the surface of revolution is inside its scope; ring length wording; reason for f(0) = 0, f'(0) = 1; mechanism split into three sentences; kappa_m and kappa_p named and the division by r^2 explained; the lemon family scoped away from its tips.
- Key equation gaussian-curvature-from-the-line-element: meaning now says the formula holds for any line element of that form.
- Check ring-on-a-smooth-planet: ring length given as 314.028 km so the answer's shortfall 0.131 km and fraction 4.18 x 10^-4 follow from the question; recomputed with python3: K = 1.003 x 10^-6 km^-2, matching ball radius 998.6 km, within the stated tolerances.
- Check steering-around-a-circle-on-a-ball: 'on the left' given its reference (walker's left, head along the outward normal).
- Glossary: added principal normal and binormal.
- Nothing dropped; the review used its allowance for the fixes above, all recorded here. If a later edit must trim, the lowest-value items are the second tutor question, the solid-angle paragraph and the lemon-family sentence.

Concerns:
- Seven of the eight builds_on sections (Coordinates, curves and surfaces; Linear algebra; Vector calculus; The metric; Hypersurfaces and embeddings; The Levi-Civita connection; The geodesic equation) are not written; the persona knew them only by outline title. Re-check once they exist that they give: arc-length parametrization, the Lagrange multiplier, the induced metric, the Christoffel formula, and the geodesic equation with arc length as parameter.
- The forward reference by title to Holonomy and the Riemann tensor is acceptable to this reader because the sentence says what is on trust and where it is paid off; the writer asked the reviewer to decide.
- For the physics reviewer: the new wording 'no d rho d phi term because each ring of end marks crosses the straight walks at right angles' (Gauss's lemma) and 'comparing the tangential parts' in the mechanism paragraph; the tips of the lemon family r = b sin(rho/a) with b < a being cone points of ring ratio b/a; the sign statement for a concave-up graph.
- The writer's missing-convention reports stand: sign of the second fundamental form, sign of torsion and default normal, and K without indices versus K_mu nu.
- Numeric grading uses radii in metres and m^-2 because the unit table has no inverse-length unit; question_spoken is null on all checks.

## Review: physics

Verdict fixed (2026-09-16, revision 3)

19 verification items, 10 counterexamples

- Opening: gap under a ruler on a 75 cm basketball is about 1.7 mm at 2 cm and about 7 mm at 4 cm, four times as much for twice the distance: 1.69 mm and 6.90 mm, ratio 4.09; correct within 'about'
- Signed curvature of a graph k = y''/(1 + y'^2)^{3/2}, positive where concave up, the walker's left with head toward the viewer of the usual plot: correct, including the sign reference
- Frenet-Serret matrix antisymmetric with B' = -tau N, right-handed helix tau > 0, mirror image reverses tau: correct; the convention B' = -tau N is the one that makes a right-handed helix positive (some texts use B' = +tau N, reported as a missing convention)
- Christoffel symbols from Gauss's formula: the four other terms cancel in pairs: leaves 2 A_sigma mu nu; correct, matches the course Christoffel formula
- Weingarten's equation d_mu n = -K^lambda_mu e_lambda; sphere with outward normal has K^lambda_mu = -delta/a, K_mu nu = -g_mu nu/a; can has K_uu = -1/a: correct; sign negative for the outward normal, consistent with K_mu nu = n . d d X
- Earth's normal tilts 1 degree every 111 km; a ring of 1 km straight walks on Earth is short by 0.026 mm: correct
- Split dT/ds = kappa_n n + kappa_g u with u = n cross T the walker's left; kappa_n = K t t; tangential bracket is the geodesic equation's left side with arc length: correct; arc length is an affine parameter so the bracket is the geodesic equation's left side
- Circle of latitude at colatitude theta_0 walked eastward: kappa_g = cot(theta_0)/a, positive north of the equator with left = north: correct, sign included
- Lagrange multiplier gives K^mu_nu t^nu = lambda t^mu with lambda = kappa_n; Euler's formula; saddle z = (x^2 - y^2)/(2a) has kappa_n = cos(2 psi)/a: correct
- K = kappa_1 kappa_2 = det K_mu nu / det g_mu nu, same for either normal, scales as inverse length squared; solid angle |K| dA: correct
- K = -(1/f) d^2 f/d rho^2 for ds^2 = d rho^2 + f^2 d phi^2; f(0) = 0, f'(0) = 1, f'''(0) = -K; ring length 2 pi rho (1 - K rho^2/6): correct; Gauss's lemma (no cross term) correctly marked as trust
- Gauss equation mechanism: commuting third derivatives force K_alpha mu K_beta nu - K_alpha nu K_beta mu to equal metric terms; one independent component det K on a surface: correct; the prose does not state the sign and needs none
- Surface of revolution: n = (-z' cos phi, -z' sin phi, r'), K_rho phi = 0, kappa_m = r' z'' - z' r'', kappa_p = z'/r, product -r''/r: correct; the normal's direction depends on the sense of the profile parametrization, and the text claims neither, which is fine because only the product is used
- Family r = b sin(rho/a): K = 1/a^2, middle bends 1/b around and b/a^2 along the profile, tips are cone points for b < a: correct
- Check curvature-of-a-cubic-graph: R = 1.414 m at x = 1, friend's rule holds only at x = 0: correct
- Check ring-on-a-smooth-planet: 314.028 km at rho = 50 km gives K = 1.0e-6 km^-2 = 1.0e-12 m^-2 and radius 1000 km: correct within the stated tolerances (5% and 3%)
- Check steering-around-a-circle-on-a-ball: kappa_g = 4/15 per m, steering radius 3.75 m, toward the smaller cap: correct
- Reference Gauss 1827, Commentationes Societatis Regiae Scientiarum Gottingensis Recentiores 6 (1828), 99-146: confirmed; verified set to true
- Structure: teaches equals the outline list, every concept named in a part, builds_on precede this section in the outline, checks and misconceptions link both ways, forward reference to Holonomy and the Riemann tensor names a real outline section: all hold; seven builds_on sections are unwritten (concern)

Fixes:
- Summary: 'a surface bends by a different amount in each direction' failed the ball, which bends alike in every direction; now 'by an amount that can change with direction'.
- Part sharpest-and-gentlest-bends: the display line used lambda both as the eigenvalue and as the dummy index in g^{mu lambda} K_{lambda nu}; the dummy is now sigma (also in part one-number-for-a-spot for consistency). Euler's angle renamed psi so that phi keeps its later meaning, the direction coordinate and the angle round the axis.
- Part the-ant-and-the-outsider-agree: the Gauss-equation combination used rho as an index in the part where rho is the walked distance; indices now alpha, beta. 'a ring of 1 kilometre' made unambiguous: 'the ring of 1-kilometre straight walks'.
- Glossary principal curvatures: 'are perpendicular' scoped to 'when the two curvatures differ' (umbilic points).
- Further: Gauss 1827 reference confirmed and marked verified.

Concerns:
- Seven builds_on sections are unwritten (Coordinates, curves and surfaces; Linear algebra; Vector calculus; The metric; Hypersurfaces and embeddings; The Levi-Civita connection; The geodesic equation). This section assumes they give arc-length parametrization, the Lagrange multiplier, the induced metric g = e . e, the course Christoffel formula, and the geodesic equation with an affine parameter; re-check when they exist.
- Missing conventions to add to course-conventions.md: sign of the second fundamental form (this section uses K_mu nu = n . d_mu d_nu X, positive toward the chosen normal, with n = e_1 cross e_2 normalized); sign of torsion (B' = -tau N, right-handed helix positive); K without indices is the Gaussian curvature, K_mu nu the second fundamental form. The section states each choice in prose, as the card allows.
- The index rho is still used in part the-gap-under-a-card-in-formulas (Gamma^rho) four parts before rho names the walked distance; both are unambiguous in place, so it was left.
- The Gauss equation's sign is not stated in the mechanism paragraph; when Holonomy and the Riemann tensor is written, it should give R_alpha beta mu nu = K_alpha mu K_beta nu - K_alpha nu K_beta mu in the course Riemann sign, which makes the sphere positive.
