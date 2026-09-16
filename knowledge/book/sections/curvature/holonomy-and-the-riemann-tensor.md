# Holonomy and the Riemann tensor

`curvature/holonomy-and-the-riemann-tensor` · main track · working depth · physics-reviewed · revision 4 · 2026-09-16

Teaches: `path-dependence-of-parallel-transport`, `holonomy`, `riemann-curvature-tensor`, `riemann-curvature-operator`, `ricci-identity`, `riemann-tensor-in-normal-coordinates`

Builds on: `curved-surfaces`, `curves-and-surfaces-in-space`, `the-covariant-derivative`, `parallel-transport`, `the-levi-civita-connection`, `tensors-as-machines`, `local-flatness`, `lie-derivatives`

**Carrying a vector between two points by two routes on a curved surface gives two answers, and carrying it once around a loop brings it back rotated by the curvature the loop encloses. Shrinking the loop to a tiny cell turns that rotation into the Riemann curvature tensor, which is also the amount by which second covariant derivatives fail to commute. In coordinates that remove the metric's first derivatives at a point, the Riemann tensor is what survives of its second derivatives.**

Lay two identical arrows on the ground at one spot on the equator of a smooth globe, both pointing east along the equator. Carry the first east along the equator through a quarter of the way around. Carry the second north along its meridian to the pole, turn there, leaving the arrow alone, to face down the meridian 90 degrees of longitude to the east, and carry it to the equator, where the first arrow is waiting. Each arrow is parallel transported by the rule of *Parallel transport*: along a geodesic it keeps its angle to the path, and at a corner it is left alone while the walker turns. The first arrow still points east. The second arrives pointing south, at a right angle to it, although neither ever swung. This section finds what that right angle measures, shrinks the two routes to a tiny cell, and reads off the machine that curvature is: the Riemann tensor.

## Two routes to one spot

Parallel transport along a route $x^\mu(s)$, as in *Parallel transport*, solves the linear equation $dV^\rho/ds + \Gamma^\rho{}_{\mu\sigma}\,(dx^\mu/ds)\,V^\sigma = 0$, whose coefficients are the Christoffel symbols along the route. A different route to the same endpoint is a different equation, so nothing forces the same answer, and on a sphere the two answers can be compared exactly.

Take a sphere of radius $a$ with $ds^2 = a^2(d\theta^2 + \sin^2\theta\,d\phi^2)$, the colatitude $\theta$ measured from the north pole. Its nonzero Christoffel symbols, from the metric as in *The Levi-Civita connection*, are $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$. Describe a carried vector by its angle $\alpha$ from the southward unit vector $\hat e_\theta$ toward the eastward unit vector $\hat e_\phi$. A meridian is a geodesic, so along it $\alpha$ stays fixed. Along a circle of latitude walked east, the transport equation in orthonormal components, $V^{\hat\theta} = a\,V^\theta$ and $V^{\hat\phi} = a\sin\theta\,V^\phi$, reads $dV^{\hat\theta}/d\phi = \cos\theta\,V^{\hat\phi}$ and $dV^{\hat\phi}/d\phi = -\cos\theta\,V^{\hat\theta}$, so $\alpha$ falls at the steady rate $d\alpha/d\phi = -\cos\theta$. The circle is not a geodesic, so its walker steers toward the nearer pole while the arrow does not.

Now go from colatitude $\theta_1$ to $\theta_2 > \theta_1$ and east through $\Delta\phi$ by two routes. Meridian first: $\alpha$ is unchanged on the meridian, then falls by $\cos\theta_2\,\Delta\phi$. Latitude first: $\alpha$ falls by $\cos\theta_1\,\Delta\phi$, then is unchanged. Subtracting the latitude-first angle from the meridian-first angle,

$$\Delta\alpha = \Delta\phi\,(\cos\theta_1 - \cos\theta_2) = \frac{A}{a^2},$$

where $A = a^2\Delta\phi\,(\cos\theta_1 - \cos\theta_2)$ is the area of the strip between the routes. The meridian-first arrow is the latitude-first arrow rotated from $\hat e_\theta$ toward $\hat e_\phi$, counterclockwise seen from outside the sphere, by the strip's area over $a^2$.

This is path dependence. It also rules out a vector field that is parallel everywhere on a sphere, because transporting such a field along any route would return the same answer; in curved spacetime, in the same way, an inertial frame can be carried along one worldline but cannot be spread as one parallel field over a region that is not flat.

*Parallel transport from one point to another depends on the route: on a sphere, meridian-first and latitude-first routes deliver arrows that differ by the area of the strip between them divided by the radius squared.*

## The turn around a loop

Two routes to one spot make one loop, out by one route and home by the other, so carry a single arrow once around a loop and compare it with its start. The rotation it returns with is the holonomy of the loop. Transport preserves lengths and angles, because the connection is metric compatible, so on a surface with a unit normal vector chosen continuously over it the holonomy is a rotation by one angle $\Delta\alpha$, the same for every arrow, and reversing the loop reverses it. A reflection would also preserve lengths and angles, but with the normal chosen, whether a second transported arrow lies to the left or to the right of the first can be followed along the loop and never jumps, so no reflection occurs; on a Möbius band, which has no such normal, a loop along the band does return arrows reflected.

The course fixes the sign this way: $\Delta\alpha$ is positive when the arrow turns toward the walker's left, with the walker's head along the surface's chosen normal, outward on the globe. Seen from the side the normal points to, that is counterclockwise. For a loop that does not cross itself and bounds, on the walker's left, a region $S$ that is a smooth disk with no hole or cone tip inside,

$$\Delta\alpha = \iint_S K\,dA \pmod{2\pi},$$

with $K$ the Gaussian curvature of *Curves and surfaces in space*. This is the local Gauss–Bonnet theorem, stated here without proof. The sides need not be geodesics and the region may be any size. On a sphere it says $\Delta\alpha = A/a^2$, which is what the strip gave.

Test it on the opening's loop: out along the equator, home over the pole, with the triangle on the left. The triangle is one eighth of the sphere, so $A/a^2 = 4\pi/8 = \pi/2$: a quarter turn to the left, the right angle between the opening's two arrivals. Walk the same triangle the other way and the region on the left is the other seven eighths, giving $7\pi/2 \equiv -\pi/2$: a quarter turn to the right, as reversing the loop must give. For a triangle of geodesics whose interior angles are each less than a half turn, as the octant's are, the turn is the angle excess of *Curved surfaces*, and the transport rule shows why: along each side the arrow keeps its angle to the path, and at each corner the walker turns left through the exterior angle while the arrow stays. Over the loop the walker's heading gains, relative to the arrow, the three exterior angles, $3\pi$ minus the interior sum, which is $2\pi$ minus the excess; so when the walker is back facing the start direction, the arrow has turned left by the excess, modulo $2\pi$.

Zero curvature along a loop does not by itself mean zero holonomy. Make a cone by cutting a wedge of angle $\delta$ from a flat sheet and taping the edges. The side is flat, yet a loop around the tip returns the arrow turned by $\delta$, toward the left when the tip is on the left. To see it, unroll the cone: on the flat sheet the arrow keeps one fixed direction, and the two cut edges are glued by a rotation through $\delta$ about the tip, so crossing the tape turns the arrow by $\delta$ relative to the surface. Zero curvature guarantees zero holonomy only for loops that can be shrunk to a point without leaving the flat region.

*An arrow carried once around a simple loop returns rotated toward the walker's left by the total curvature of the region on the left, modulo a full turn; on a sphere that is the enclosed area divided by the radius squared.*

## Shrink the loop: the Riemann tensor

On a surface every small loop at a point lies in one tangent plane, so one number $K$ serves. In more dimensions a small loop can lie in different planes and carry different vectors, so the curving at a point is a table.

Shrink the loop to a coordinate parallelogram at $x$ with edge vectors $a^\mu$ and $b^\nu$, and walk $+a$, $+b$, $-a$, $-b$. To second order in the edges, a carried vector returns changed by

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu,$$

the small-loop law, where $R^\rho{}_{\sigma\mu\nu}$ is the Riemann curvature tensor. We take its derivation on trust here; *Two orders of differentiation* reaches the same tensor from derivatives and reads the loop from it. The change is linear in $V$, so the loop acts on vectors like a matrix; it is linear in each edge; it flips sign when $a$ and $b$ swap, because that walks the cell the other way round; and it scales with the cell's area, as the strip's rotation scaled with the strip's area. The slot $\sigma$ takes the carried vector, $\mu$ and $\nu$ the two edges in order, and $\rho$ is the component read.

Since $\Delta V$ is a vector for every choice of $V$, $a$ and $b$, the quotient theorem of *Tensors as machines* makes $R^\rho{}_{\sigma\mu\nu}$ a $(1,3)$ tensor, so a Riemann tensor that vanishes in one coordinate system vanishes in all. In a coordinate basis its components are

$$R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}.$$

Christoffel symbols alone prove nothing: on the flat plane in polar coordinates they are nonzero, and the derivative and product terms cancel to zero, as the check *Polar plane, two formulas* asks you to verify. On the sphere they do not cancel: the Christoffel symbols of *Two routes to one spot* give $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$ and $R^\phi{}_{\theta\theta\phi} = -1$, and the small-loop law with $V = \partial_\theta$ and the cell $\delta\theta\,\partial_\theta$, $\delta\phi\,\partial_\phi$ gives $\Delta V^\theta = 0$, because every term of $R^\theta{}_{\theta\theta\phi}$ contains a vanishing Christoffel symbol, and $\Delta V^\phi = +\delta\theta\,\delta\phi$. In orthonormal components that is $\Delta V^{\hat\phi} = a\sin\theta\,\delta\theta\,\delta\phi$ against $|V| = a$: a turn from $\hat e_\theta$ toward $\hat e_\phi$ by $\sin\theta\,\delta\theta\,\delta\phi = \delta A/a^2$ with the cell on the walker's left, the area rule with its sense.

*The Riemann tensor is the machine that turns a small cell, two edges in order, and a carried vector into the vector's change around the cell; its components come from the Christoffel symbols and their first derivatives, and it is zero in every coordinate system exactly when it is zero in one.*

## Two orders of differentiation

For a scalar field $f$, $\nabla_\mu\nabla_\nu f = \partial_\mu\partial_\nu f - \Gamma^\lambda{}_{\mu\nu}\partial_\lambda f$ is symmetric in $\mu\nu$, because partial derivatives commute and the Levi-Civita connection is torsion-free: for a scalar the order of differentiation does not matter. For a vector field it does. Write $\nabla_\mu\nabla_\nu V^\rho$ for $\nabla_\mu(\nabla_\nu V^\rho)$, the rightmost derivative acting first, and expand one move at a time.

- $\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\lambda}V^\lambda$ is a $(1,1)$ tensor, so its derivative corrects both indices: $\nabla_\mu\nabla_\nu V^\rho = \partial_\mu(\nabla_\nu V^\rho) + \Gamma^\rho{}_{\mu\lambda}\nabla_\nu V^\lambda - \Gamma^\lambda{}_{\mu\nu}\nabla_\lambda V^\rho$.
- Expanded, the first two terms are $\partial_\mu\partial_\nu V^\rho + (\partial_\mu\Gamma^\rho{}_{\nu\sigma})V^\sigma + \Gamma^\rho{}_{\nu\lambda}\partial_\mu V^\lambda + \Gamma^\rho{}_{\mu\lambda}\partial_\nu V^\lambda + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma}V^\sigma$.
- Swap $\mu$ and $\nu$ and subtract. The second partials cancel because they commute; the pair $\Gamma^\rho{}_{\nu\lambda}\partial_\mu V^\lambda + \Gamma^\rho{}_{\mu\lambda}\partial_\nu V^\lambda$ cancels because it is symmetric in $\mu\nu$; the index correction cancels because $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$.
- What remains is $(\partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma})V^\sigma$.

The expression in parentheses is the component formula of *Shrink the loop*, so

$$[\nabla_\mu,\nabla_\nu]V^\rho \equiv \nabla_\mu\nabla_\nu V^\rho - \nabla_\nu\nabla_\mu V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma,$$

the Ricci identity. Every term with a derivative of $V$ has cancelled. This is the section's derivation of the component formula: the commutator has been computed exactly, and the loop reading that follows shows that it is the small-loop change, so its coefficient is the same $R^\rho{}_{\sigma\mu\nu}$.

The loop is hiding in the two orders. Multiply by $a^\mu b^\nu$ and read each derivative as a comparison across the cell: $b^\nu\nabla_\nu V$ at a point is $V$ one step $b$ away, carried back to the point, minus $V$ at the point, to first order in $b$. Then $a^\mu b^\nu\nabla_\mu\nabla_\nu V$ at $x$ is that comparison made at $x + a$ and carried back to $x$, minus the same comparison made at $x$: four terms, the far corner's vector carried home through $x + a$, minus the vector at $x + a$ carried home, minus the vector at $x + b$ carried home, plus $V(x)$. The other order gives the same four terms except that the far corner's vector comes home through $x + b$. Subtracting, three terms cancel, and $[\nabla_\mu,\nabla_\nu]V^\rho\,a^\mu b^\nu$ is the far corner's vector carried home through $x + a$ minus the same vector carried home through $x + b$. Out through $x + b$ and home through $x + a$ is the cell walked $+b$, $+a$, $-b$, $-a$, the reverse of $+a$, $+b$, $-a$, $-b$; so the commutator is minus the change around $+a$, $+b$, $-a$, $-b$, which is the small-loop law with its sign, once we take on trust that the corrections from carrying the edge vectors themselves are of third order.

Apply the commutator to the scalar $\omega_\rho V^\rho$, on which it gives zero; the product rule then forces $[\nabla_\mu,\nabla_\nu]\omega_\rho = -R^\sigma{}_{\rho\mu\nu}\,\omega_\sigma$ for a covector. A tensor with several indices gets one term per index, plus for each upper index and minus for each lower one.

*Second covariant derivatives of a vector field do not commute: their difference is the Riemann tensor acting on the vector with no derivative of the field left over, and it is the change around a tiny loop read at a point.*

## The operator that needs a closing walk

In the Ricci identity the coordinate basis fields $\partial_\mu$ and $\partial_\nu$ commute, as *Lie derivatives* showed. Replace them by any two vector fields $u$ and $v$, with $\nabla_u w = u^\mu\nabla_\mu w$ the derivative along $u$, and the bare commutator $\nabla_u\nabla_v w - \nabla_v\nabla_u w$ is no longer curvature. Expanding, $\nabla_u\nabla_v w$ has components $u^\mu v^\nu\nabla_\mu\nabla_\nu w^\rho + u^\mu(\nabla_\mu v^\nu)\nabla_\nu w^\rho$. Swap and subtract: the first pieces give $u^\mu v^\nu R^\rho{}_{\sigma\mu\nu}w^\sigma$ by the Ricci identity, and the second pieces give $(\nabla_u v - \nabla_v u)^\nu\nabla_\nu w^\rho$, which for a torsion-free connection is $[u,v]^\nu\nabla_\nu w^\rho$, the derivative of $w$ along the Lie bracket of *Lie derivatives*. That leftover contains a derivative of $w$, so it is not a property of the point. Subtract it and define the curvature operator

$$\mathcal R(u,v)w = \nabla_u\nabla_v w - \nabla_v\nabla_u w - \nabla_{[u,v]}w, \qquad \big(\mathcal R(u,v)w\big)^\rho = R^\rho{}_{\sigma\mu\nu}\,w^\sigma u^\mu v^\nu.$$

The right side has no derivative of $u$, $v$ or $w$: the operator depends only on the three vectors at the point.

Flow a parameter distance $\epsilon$ along $u$, then along $v$, then back along $u$ and back along $v$. Unless the fields commute, the four legs miss the start by $\epsilon^2[u,v]$ plus higher orders, even on flat ground. The bracket is the gap per $\epsilon^2$, and $\epsilon^2\,\nabla_{[u,v]}w$ accounts for the change of $w$ across the closing walk that turns the four legs into a loop. Around the closed loop, $\Delta w = -\epsilon^2\,\mathcal R(u,v)w + O(\epsilon^3)$ by the small-loop law, because the closing walk is of order $\epsilon^2$ and adds no area at that order.

Test it where nothing is curved. On the flat plane take the unit polar fields $u = \hat e_r = \partial_r$ and $v = \hat e_\phi = r^{-1}\partial_\phi$, and $w = \hat e_r$. The Christoffel symbols of the check *Polar plane, two formulas* give $\nabla_{\hat e_\phi}\hat e_r = \hat e_\phi/r$ and $\nabla_{\hat e_r}\hat e_r = \nabla_{\hat e_r}\hat e_\phi = 0$, so $\nabla_u\nabla_v w - \nabla_v\nabla_u w = \nabla_{\hat e_r}(\hat e_\phi/r) = -\hat e_\phi/r^2$, not zero. But $[u,v] = -\hat e_\phi/r$ and $\nabla_{[u,v]}w = -\hat e_\phi/r^2$ too, so $\mathcal R(u,v)w = 0$.

*The curvature operator takes covariant derivatives along two vector fields in both orders and subtracts the derivative along their Lie bracket; what remains depends only on the three vectors at the point and is the Riemann tensor.*

## What a falling frame leaves

*Local flatness* showed that around any event $P$ there are coordinates with $g_{\mu\nu}(P) = \eta_{\mu\nu}$ and $\partial_\lambda g_{\mu\nu}(P) = 0$, locally inertial coordinates at $P$. Every Christoffel symbol is built from first derivatives of the metric, so all of them vanish at $P$, and the products in the component formula drop out there: $R^\rho{}_{\sigma\mu\nu}(P) = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma}$. The derivatives of $\Gamma$ still hold second derivatives of $g$. Lower the first index with $g_{\alpha\rho}$, which at $P$ passes through $\partial$ because $\partial g(P) = 0$, and use $g_{\alpha\rho}\Gamma^\rho{}_{\nu\beta} = \tfrac12(\partial_\nu g_{\alpha\beta} + \partial_\beta g_{\alpha\nu} - \partial_\alpha g_{\nu\beta})$. Differentiating and antisymmetrizing in $\mu\nu$ kills the $\partial_\mu\partial_\nu g_{\alpha\beta}$ pair and leaves

$$R_{\alpha\beta\mu\nu}(P) = \tfrac12\big(\partial_\beta\partial_\mu g_{\alpha\nu} - \partial_\beta\partial_\nu g_{\alpha\mu} + \partial_\alpha\partial_\nu g_{\beta\mu} - \partial_\alpha\partial_\mu g_{\beta\nu}\big).$$

This is the equivalence principle made quantitative: a freely falling frame removes the metric's value and first derivatives at one event, but not all of its second derivatives, and the combinations that survive are the curvature. The four-term formula is not a tensor equation and holds only where $\partial g = 0$; elsewhere products of Christoffel symbols must be added.

The Riemann normal coordinates of *Local flatness* go further: with an orthonormal basis at $P$, they give the event reached by the geodesic leaving $P$ with tangent $v^\mu$ after unit affine parameter the coordinates $x^\mu = v^\mu$. In them, stated here without proof,

$$g_{\mu\nu}(x) = \eta_{\mu\nu} - \tfrac13 R_{\mu\alpha\nu\beta}(P)\,x^\alpha x^\beta + O(x^3).$$

There is no linear term, so $\Gamma(P) = 0$ and the four-term formula applies. The length of the position vector itself, $g_{\mu\nu}x^\mu x^\nu$, keeps its flat value to this order, since $R_{\mu\alpha\nu\beta}\,x^\alpha x^\beta x^\nu = 0$ by the antisymmetry in the last pair that *Shrink the loop* noted. Lengths across the position vector change. On a surface the tensor has one independent orthonormal component at $P$, the Gaussian curvature $K$ (taken on trust here; *Symmetries and identities* counts the components), so a vector perpendicular to $x$, of length one by the flat $\eta_{\mu\nu}$, has squared length $1 - \tfrac13 K|x|^2$, and a circle of radius $r$ has circumference $2\pi r(1 - Kr^2/6)$ to this order. That is the ring test of *Curved surfaces*: on Earth a ring drawn with a 1 km string is short by $\pi r^3/3a^2 = 0.026$ mm, the number that section quoted.

*Where coordinates make the metric's first derivatives vanish, the lowered Riemann tensor is half a signed sum of four second derivatives of the metric; in Riemann normal coordinates the metric departs from flat at second order by minus a third of the Riemann tensor, which is what no coordinates can remove.*

## Key equations

**Holonomy of a simple loop** (stated)

$$\Delta\alpha = \iint_S K\,dA \pmod{2\pi}$$

The holonomy of a simple loop bounding a smooth disk $S$ (no hole or cone tip inside) on the walker's left is the total Gaussian curvature inside, modulo a full turn, positive toward the left. Stated without proof.

- $\Delta\alpha$: holonomy, the rotation the arrow returns with
- $K$: Gaussian curvature

Say: Delta alpha equals the integral of the Gaussian curvature over the region on the walker's left, modulo two pi.

**Small-loop law** (stated)

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu$$

A vector carried around the parallelogram $+a$, $+b$, $-a$, $-b$ returns changed by minus the Riemann tensor fed the vector and the two edges, to second order. Stated; the Ricci identity gives the tensor and the loop reading of the two orders fixes the sign.

- $\Delta V^\rho$: change of the carried vector after one trip around the cell
- $R^\rho{}_{\sigma\mu\nu}$: Riemann curvature tensor
- $a^\mu, b^\nu$: the two edge vectors of the cell, in walking order

Say: Delta V upper rho equals minus R upper rho lower sigma mu nu, times V upper sigma, times a upper mu, times b upper nu.

**Riemann tensor from the Christoffel symbols** (derived-here)

$$R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$$

Coordinate components of the Riemann tensor: the change of the connection across the cell plus the failure of its two edge steps to commute. Derived in *Two orders of differentiation*.

- $\Gamma^\rho{}_{\mu\sigma}$: Christoffel symbols of the Levi-Civita connection
- $\partial_\mu$: partial derivative along the mu coordinate

Say: R upper rho lower sigma mu nu equals d mu of Gamma upper rho lower nu sigma, minus d nu of Gamma upper rho lower mu sigma, plus Gamma upper rho lower mu lambda times Gamma upper lambda lower nu sigma, minus Gamma upper rho lower nu lambda times Gamma upper lambda lower mu sigma.

**Ricci identity** (derived-here)

$$[\nabla_\mu,\nabla_\nu]V^\rho \equiv \nabla_\mu\nabla_\nu V^\rho - \nabla_\nu\nabla_\mu V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$$

Second covariant derivatives of a vector field, the rightmost acting first, fail to commute by the Riemann tensor acting on the vector, with no derivative of the field left over. A covector gets $-R^\sigma{}_{\rho\mu\nu}\,\omega_\sigma$ instead.

- $[\nabla_\mu,\nabla_\nu]$: commutator of the two covariant derivatives, nabla nu acting first in the first term

Say: The commutator of nabla mu and nabla nu, acting on V upper rho, equals R upper rho lower sigma mu nu times V upper sigma.

## Checks

**two-routes-across-a-strip-of-earth** (numeric): Treat Earth as a sphere of radius 6371 kilometres. An arrow starts at latitude 40 degrees north, longitude zero, and is parallel transported to latitude 30 degrees north, longitude 10 degrees east, by two routes: south along the meridian and then east along the circle of latitude, or east first and then south. By what angle do the two arrivals differ, what is the area of the strip between the routes, and which arrival is rotated which way relative to the other, seen from outside Earth?

Answer: The colatitudes are $\theta_1 = 50^\circ$ and $\theta_2 = 60^\circ$, and $\Delta\phi = 10^\circ = 0.1745$ rad. So $\Delta\alpha = \Delta\phi\,(\cos\theta_1 - \cos\theta_2) = 0.1745\times(0.6428 - 0.5000) = 0.0249$ rad, which is $1.43^\circ$, and the strip's area is $a^2\Delta\alpha = 1.0\times10^6\ \mathrm{km^2}$. The meridian-first arrow is the latitude-first arrow rotated by $1.43^\circ$ counterclockwise seen from outside, because the latitude-first route pays its $\cos\theta$ per radian of longitude on the northern circle, where $\cos\theta$ is larger.

Key points: Colatitudes 50 and 60 degrees and a longitude difference of 0.1745 rad give 0.0249 rad, about 1.43 degrees; the strip's area is that times the radius squared, about one million square kilometres; The meridian-first arrival is rotated counterclockwise, seen from outside, relative to the latitude-first arrival

Numeric: angle between the two arrivals, positive counterclockwise seen from outside = 1.43 deg; area of the strip between the routes = 1010000.0 km^2

**polar-plane-two-formulas** (derive): The flat plane in polar coordinates has $ds^2 = dr^2 + r^2d\phi^2$, with nonzero Christoffel symbols $\Gamma^r{}_{\phi\phi} = -r$ and $\Gamma^\phi{}_{r\phi} = \Gamma^\phi{}_{\phi r} = 1/r$. Compute $R^r{}_{\phi r\phi}$ from the component formula, term by term. Then evaluate the four-second-derivative formula for $R_{r\phi r\phi}$ and explain what you find.

Answer: $\partial_r\Gamma^r{}_{\phi\phi} = -1$; $\partial_\phi\Gamma^r{}_{r\phi} = 0$; $\Gamma^r{}_{r\lambda}\Gamma^\lambda{}_{\phi\phi} = 0$ because $\Gamma^r{}_{rr}$ and $\Gamma^r{}_{r\phi}$ vanish; $\Gamma^r{}_{\phi\lambda}\Gamma^\lambda{}_{r\phi} = \Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = -1$. So $R^r{}_{\phi r\phi} = -1 - 0 + 0 - (-1) = 0$: the plane is flat however curved its coordinate lines. The four-term formula gives $\tfrac12(\partial_\phi\partial_r g_{r\phi} - \partial_\phi\partial_\phi g_{rr} + \partial_r\partial_\phi g_{\phi r} - \partial_r\partial_r g_{\phi\phi}) = \tfrac12(0 - 0 + 0 - 2) = -1$, which is wrong because that formula holds only where the metric's first derivatives vanish, and here $\partial_r g_{\phi\phi} = 2r$. The Christoffel product it omits, $-g_{rr}\Gamma^r{}_{\phi\phi}\Gamma^\phi{}_{r\phi} = +1$, restores zero.

Key points: Derivative term minus one, product term plus one, total zero: nonzero Christoffel symbols come from the coordinate lines; The four-second-derivative formula gives minus one because it assumes vanishing first derivatives of the metric; the omitted Christoffel products give plus one

Numeric: the component R upper r lower phi r phi = 0 1

**loop-around-a-cone-tip** (numeric): Cut a wedge of 60 degrees, with its point at the centre, out of a flat sheet, and tape the cut edges together to make a cone. Loop A circles the tip once with the tip on the walker's left. Loop B lies on the cone's side and does not go around the tip. Give the holonomy of each with its sense, and say whether zero curvature along a loop guarantees zero holonomy.

Answer: Away from the tip the cone is the flat sheet bent without stretching, so $K = 0$ there and loop B returns the arrow unchanged. For loop A, unroll the cone: a carried arrow keeps a fixed direction on the sheet, and the two taped edges are identified by a rotation through $60^\circ$ about the tip, so the arrow returns rotated by $60^\circ$ toward the walker's left. Zero curvature along the loop guarantees nothing; zero curvature throughout a region within which the loop can be shrunk to a point does.

Key points: Loop B: zero, because the side is flat; loop A: sixty degrees toward the walker's left, the missing wedge; The guarantee needs zero curvature on a region the loop can be shrunk within, not just along the loop

Numeric: holonomy of loop A, positive toward the walker's left = 60 deg; holonomy of loop B = 0 deg

## Misconceptions

- **never-swung-so-arrive-matching**: "Two arrows that start matching and are never allowed to swing must arrive matching, whatever routes they take." — Transport is a differential equation whose coefficients depend on the route. On a sphere, meridian-first and latitude-first routes deliver arrows that differ by the area of the strip between them divided by the radius squared. (diagnosed by two-routes-across-a-strip-of-earth)
- **christoffels-mean-curvature**: "Nonzero Christoffel symbols show that a space is curved." — Christoffel symbols record how coordinate basis vectors change and are nonzero in polar coordinates on a flat plane, where the Riemann tensor's terms cancel to zero. (diagnosed by polar-plane-two-formulas)
- **flat-along-loop-means-no-turn**: "If the curvature is zero everywhere along a loop, the arrow must come back unturned." — A loop around the tip of a cone runs through flat surface and returns the arrow turned by the missing wedge. Zero curvature guarantees zero holonomy only for loops that can be shrunk to a point inside the flat region. (diagnosed by loop-around-a-cone-tip)

## Glossary

- **path dependence**: The fact that parallel transport between two points can deliver different vectors along different routes on a curved space. (`path-dependence-of-parallel-transport`)
- **holonomy**: The rotation, or in spacetime the Lorentz transformation, that a vector returns with after parallel transport once around a closed loop. (`holonomy`)
- **Riemann curvature tensor**: The tensor with one upper and three lower indices that gives minus the change of a carried vector around a tiny cell, per unit of oriented area. (`riemann-curvature-tensor`)
- **Ricci identity**: The rule that the commutator of two covariant derivatives on a vector field is the Riemann tensor acting on the vector. (`ricci-identity`)
- **curvature operator**: The map that differentiates a vector covariantly along two vector fields in both orders, subtracts the derivative along their Lie bracket, and depends only on the three vectors at the point. (`riemann-curvature-operator`)
- **Riemann normal coordinates**: Coordinates around one event that label each nearby event by the initial tangent of the geodesic reaching it from the origin in unit affine parameter. (`riemann-tensor-in-normal-coordinates`)

## Visuals

- `carry-an-arrow-around-a-loop` (flagship): Flagship: two routes to one spot on a globe, the octant loop walked both ways, and a cone whose tip a loop can enclose or avoid.
- `shrink-the-loop-to-find-riemann` (core): Connects the area rule to the Riemann tensor: a coordinate cell that shrinks while the change per unit area settles to the component. Sketch: A coordinate parallelogram on a sphere patch, a saddle or the polar-coordinate plane, with a carried arrow. A slider shrinks the cell; a log-log plot of the arrow's change against edge length shows slope two, and the change over the cell's area settles to the printed component, zero on the polar plane. A button swaps the edge order and flips the sign.

## Tutor

Opening question: Picture a smooth globe. Two arrows start at one spot on the equator, both pointing east. One is carried east along the equator a quarter of the way round. The other goes north to the pole and comes back down to the same meeting spot, and neither is ever allowed to swing. Do they arrive pointing the same way, and if not, what sets the angle between them?

- Q: The transport rule is the same rule everywhere, so why do two routes give two different arrows? A: The rule is a differential equation whose coefficients are the Christoffel symbols along the route, and those differ from route to route. On a sphere a circle of latitude keeps steering toward the pole while a meridian does not, so an arrow that never steers drops behind the walker's frame on one route and not on the other. The difference is the area between the routes divided by the radius squared.
- Q: If I can make every Christoffel symbol vanish at a point, is spacetime flat there? A: No. You can remove the metric's value and first derivatives at one event, but not all of its second derivatives, and the Riemann tensor at that event is built from those. On a sphere, normal coordinates at any point have vanishing Christoffel symbols there, and the Gaussian curvature is still one over the radius squared.

## Review: novice

Verdict fixed (2026-09-16, revision 4)

Retell attempt: Parallel transport solves a differential equation whose coefficients are the Christoffel symbols along the route, so two routes to the same point can give two arrows. On a sphere, meridian-first and latitude-first arrivals differ by the strip's area over the radius squared, because along a circle of latitude the walker keeps steering toward the pole while the arrow does not, at the rate cos(theta) per radian of longitude. Going round a loop, the arrow comes back rotated: that rotation is the holonomy, and for a simple loop with the region on the walker's left it is the integral of the Gaussian curvature over the region, modulo 2 pi, positive to the left (stated, not proved). The octant gives a quarter turn left, the reversed octant a quarter turn right, and a cone gives the wedge angle even though its side is flat, so zero curvature along the loop is not enough. Shrinking the loop to a tiny parallelogram gives the small-loop law: the change of the vector is minus the Riemann tensor fed the vector and the two edges, antisymmetric in the edges, and R is a tensor by the quotient theorem, with a formula from the Christoffel symbols and their first derivatives. The polar plane has nonzero Christoffels but zero Riemann. Second covariant derivatives of a vector do not commute, and the commutator is exactly R times V with no derivatives of V left (I could follow every bullet); the section then says this commutator is minus the loop change, but I had to read that paragraph three times and still could not say back which four terms cancel or why the loop comes out reversed. For general vector fields the plain commutator picks up a derivative along the Lie bracket, which is the gap in the four flow legs, so the curvature operator subtracts it; on the polar plane the two pieces are both minus e-phi over r squared and cancel, though I could not see where minus e-phi over r squared came from. In locally inertial coordinates the Christoffels vanish and R is half a signed sum of four second derivatives of the metric; in Riemann normal coordinates the metric is flat minus a third of R times x x, which gives the ring shortfall 2 pi r times K r squared over 6 and the 0.026 mm on Earth. Things I could not say back: why the geodesic triangle's turn is its angle excess, why the holonomy has to be a rotation and not a reflection, where the +1 in the polar check answer comes from, and what 'no field of parallel vectors covers a sphere, and only local inertial frames survive' was telling me.

21 stumbles

- “turn there to face down the meridian a quarter turn of longitude to the east”: 'a quarter turn of longitude' is unclear, and the opening does not say that the arrow is left alone while the walker turns until the next sentence.
- “the transport equation in orthonormal components reads”: The step from the coordinate transport equation with the given Christoffel symbols to the orthonormal components is left implicit; I could not reproduce the cos(theta) without knowing the scaling.
- “its walker steers toward the pole while the arrow does not”: Which pole? In the southern hemisphere the walker steers toward the south pole and the sign of cos(theta) flips.
- “Subtracting,”: Subtracting which angle from which? The sign of the result and the sense claimed in the next sentence depend on it.
- “This is path dependence: no field of parallel vectors covers a sphere, and in curved spacetime only local inertial frames survive.”: Two conclusions with the steps left out: why path dependence forbids a parallel field, and what the frames 'survive'.
- “so on a surface the holonomy is a rotation by one angle”: Preserving lengths and angles also allows a reflection; the reason it must be a rotation is missing.
- “For a triangle of geodesics the turn is the angle excess of *Curved surfaces*.”: A surprising claim with no reason; the earlier section gave the excess only for a ball, and the transport rule stated in the opening is enough to see it.
- “because the taped edges are identified by a rotation through delta. The guarantee holds only for loops”: 'identified by a rotation' is not a rule I could physically follow, and 'the guarantee' has no clear referent.
- “and it scales with the cell's area, as A/a^2 did”: In this part a is the edge vector; here a is the sphere's radius. One symbol for two ideas in one paragraph.
- “gives Delta V^theta = 0 and Delta V^phi = + delta theta delta phi: a turn from e_theta toward e_phi by sin(theta) delta theta delta phi”: Two steps left implicit: why the theta component vanishes when R^theta_theta theta phi was never listed, and how delta theta delta phi becomes an angle sin(theta) delta theta delta phi.
- “The bracket is the component formula of *Shrink the loop*”: 'bracket' here means the parentheses, but the same word names the commutator bracket in the next line and the Lie bracket in the next part.
- “so this is the section's proof of the formula”: Which formula, and proof of what? The commutator has been computed; that its coefficient is the loop's tensor still needs the next paragraph.
- “Each order is then a change of a change across the cell, and the difference of the two orders is the far corner's vector brought home along the cell's two sides, once through x + a and once through x + b. Home by one route and back out by the other is the cell walked round”: Read three times and could not say back which terms each order contains, why three of them cancel, or why the loop comes out as the reverse of +a, +b, -a, -b, which is what the minus sign rests on.
- “Apply the commutator to the scalar omega_rho V^rho, which it leaves at zero”: 'leaves at zero' reads as if the scalar were zero; the commutator gives zero on any scalar.
- “In the Ricci identity the fields partial_mu and partial_nu commute.”: 'fields' without saying they are the coordinate basis vector fields, and the fact comes from an earlier section that is not named.
- “nabla_[u,v] w is the change of w along the closing walk”: The closing walk is epsilon squared long, so the change along it is epsilon squared times the derivative; the factor was dropped.
- “One finds nabla_u nabla_v w - nabla_v nabla_u w = - e_phi / r^2, not zero.”: 'One finds' hides every step of the only test of the operator in the section; I could not see where minus e_phi over r squared came from.
- “kills the partial_mu partial_nu g_alpha sigma pair”: The lowered Christoffel symbol was written with sigma but the result uses beta for that index; I had to rename to follow.
- “Riemann normal coordinates go further. Choose an orthonormal basis at P, and give the event reached by the geodesic ...”: Restates a construction that *Local flatness* already gave, without naming that section.
- “Radial lengths are exact to this order ... by antisymmetry in the last pair. Transverse lengths change. On a surface the tensor has one independent orthonormal component at P, the Gaussian curvature K”: 'Radial lengths' does not say what is measured; the antisymmetry was noted in Shrink the loop but not named as the source; the one-component claim is stated without saying it is taken on trust.
- “The products it omits, g_phi phi Gamma^phi_phi r Gamma^phi_r phi = +1, restore zero.”: That product is not a term of the component formula computed in the first half of the answer; the omitted term I can see there is minus Gamma^r_phi phi Gamma^phi_r phi, lowered with g_rr.

Fixes:
- Opening: the pole turn now says the arrow is left alone and the meridian is 90 degrees of longitude east.
- Part 1: orthonormal scaling of the components stated; 'nearer pole'; the subtraction names its order; the closing sentence on parallel fields and inertial frames made explicit.
- Part 2: reason that the holonomy is a rotation and not a reflection; reversed octant tied to loop reversal; two-sentence reason that a geodesic triangle's holonomy is its angle excess; cone holonomy explained by unrolling; 'the guarantee' named.
- Part 3: radius a no longer reused next to the edge vector a; the sphere cell's zero theta component and the conversion to an angle made explicit.
- Part 4: 'bracket' replaced by 'expression in parentheses'; the derivation claim now says what is derived and what the loop reading adds; the loop-reading paragraph rewritten as explicit steps with the reversed loop shown; 'leaves at zero' reworded.
- Part 5: coordinate basis fields named with their source section; epsilon squared restored on the closing-walk change; the polar-plane test shows its two intermediate covariant derivatives.
- Part 6: index letter made consistent; Riemann normal coordinates credited to Local flatness; radial length claim made concrete; the one-component claim marked as taken on trust.
- Check polar-plane-two-formulas: the omitted product written as the term of the component formula, - g_rr Gamma^r_phi phi Gamma^phi_r phi = +1, which equals the value the writer gave.
- Revision 1 to 2; status novice-reviewed.

Concerns:
- The loop-reading paragraph in Part 4 was rewritten as explicit steps; the physics reviewer should confirm the four-term bookkeeping and that out through x + b and home through x + a is the loop +b, +a, -b, -a, the reverse of +a, +b, -a, -b, so that the commutator is minus the small-loop change.
- The added reason for the geodesic-triangle holonomy (walker's heading gains 2 pi minus the excess relative to the arrow) should be checked for sense on a triangle walked with the region on the right.
- The added cone sentence says crossing the tape turns the arrow by delta relative to the surface; the physics reviewer should confirm the sense (toward the walker's left with the tip on the left) matches the check answer.
- The section still has no check for the curvature operator or for the normal-coordinate formula beyond the polar-plane check; the writer's dropped octant-both-ways and bracket checks would fill the gap if a later revision has room.
- The 0.026 mm ring shortfall is attributed to Curved surfaces; that section's text should be confirmed to quote it (a grep found it there).

## Review: physics

Verdict fixed (2026-09-16, revision 4)

17 verification items, 10 counterexamples

- Sphere Christoffel symbols Gamma^theta_phiphi = -sin cos, Gamma^phi_thetaphi = cot; transport east along a circle of latitude gives d alpha/d phi = -cos theta with alpha from e_theta toward e_phi: correct; numerical meridian-first minus latitude-first angle 0.024921 rad equals dphi (cos 50 - cos 60)
- Rotation from e_theta toward e_phi is counterclockwise seen from outside and is a turn toward the left of a walker whose head is along the outward normal: correct; matches the course orientation row
- Opening: equator arrow arrives east, over-the-pole arrow arrives south, at a right angle: correct; the pole arrival is clockwise from the equator arrival seen from outside, consistent with the +pi/2 holonomy of the loop out along the equator and home over the pole
- Octant loop with the triangle on the left has holonomy +pi/2 (left turn); the reversed walk gives 7pi/2 = -pi/2: correct
- Geodesic-triangle holonomy equals the angle excess: correct for interior angles below pi; scoped to that case in the text
- Cone: loop around the tip with the tip on the left returns the arrow turned by the wedge angle delta toward the left; loop B on the side gives zero: correct; agrees with concentrated curvature delta at the tip and with check loop-around-a-cone-tip (60 degrees, left)
- Sphere components R^theta_phithetaphi = sin^2 theta, R^phi_thetathetaphi = -1, R^theta_thetathetaphi = 0: correct
- Small-loop law sign: walking +a (south), +b (east), -a, -b with V = d_theta gives Delta V^phi = +delta theta delta phi, a left turn by delta A / a^2 with the cell on the walker's left: correct; the course sign of the small-loop law agrees with the Gauss-Bonnet sense
- Ricci identity derivation: the four bullets and the surviving terms match the course Riemann formula; covector rule -R^sigma_rhomunu omega_sigma: correct
- Loop reading of the commutator: a.nabla(b.nabla V) is four terms (far corner home through x+a, minus x+a home, minus x+b home, plus V(x)); the difference of orders is T_a W - T_b W = (T_a T_b^-1 - 1) T_b W, and T_a T_b^-1 is the loop x, x+b, x+a+b, x+a, x, the reverse of +a,+b,-a,-b: correct; so [nabla_mu, nabla_nu] V a b = -Delta V around +a,+b,-a,-b, matching both course rows
- Curvature operator: bare commutator of nabla_u and nabla_v leaves [u,v].nabla w; the four flows +eps u, +eps v, -eps u, -eps v end at x + eps^2 [u,v]: correct
- Polar-plane test: nabla_{e_phi} e_r = e_phi / r, nabla_{e_r} e_r = nabla_{e_r} e_phi = 0, commutator -e_phi / r^2, [u,v] = -e_phi / r, nabla_[u,v] w = -e_phi / r^2, operator zero: correct
- Four-second-derivative formula R_abmn = 1/2 (d_b d_m g_an - d_b d_n g_am + d_a d_n g_bm - d_a d_m g_bn) at a point with dg = 0: correct; agrees with the standard form g_an,bm + g_bm,an - g_am,bn - g_bn,am over 2
- Check polar-plane-two-formulas: derivative term -1, product term +1, total 0; the four-term formula gives -1; omitted product -g_rr Gamma^r_phiphi Gamma^phi_rphi = +1: correct
- Riemann normal expansion g = eta - (1/3) R x x: radial length exact at this order, transverse unit vector squared length 1 - K|x|^2/3, circumference 2 pi r (1 - K r^2/6), Earth 1 km ring short by 0.026 mm: correct
- Check two-routes-across-a-strip-of-earth: 1.43 degrees counterclockwise seen from outside, strip 1.01e6 km^2: correct within the stated tolerances
- Structure: teaches equals the outline list; builds_on names main-track sections earlier in the outline (positions 30 to 67 of 68); Symmetries and identities is the next section; checks and misconceptions link both ways; further is empty at working depth: correct; no references to verify

Fixes:
- Part 1: an inertial frame 'cannot be spread over a region' now says it cannot be spread as one parallel field over a region that is not flat
- Part 2: the rotation-not-reflection claim is scoped to a surface with a continuously chosen normal, with the Möbius band as the case that reflects
- Part 2 and key equation local-gauss-bonnet: the region is a smooth disk with no hole or cone tip inside
- Part 2: the geodesic-triangle excess argument is scoped to interior angles below a half turn
- Part 6: 'a unit vector perpendicular to x' now says a vector of flat length one
- Glossary: the Riemann tensor gives minus the change around a tiny cell
- Tutor: 'the curvature' on the sphere named as the Gaussian curvature
- Revision 2 to 3; status physics-reviewed

Concerns:
- The small-loop law and the local Gauss-Bonnet law are stated on trust; the loop reading of the Ricci identity fixes the sign but the third-order corrections from carrying the edge vectors are also taken on trust, as the text says
- Still no check exercises the curvature operator or the normal-coordinate expansion; a later revision could add the octant-both-ways or polar-bracket check the writer dropped
- Conventions gaps reported earlier remain open: a symbol for the curvature operator (the section uses calligraphic R), the component form of the Lie bracket, and 'Riemann normal' versus 'locally inertial' naming
- builds_on names sections that exist in the outline but are not yet written; their concept lists cover everything assumed here (transport rule, Christoffel symbols from the metric and of the first kind, quotient theorem, local flatness and Riemann normal coordinates, Lie bracket and commuting coordinate fields)
