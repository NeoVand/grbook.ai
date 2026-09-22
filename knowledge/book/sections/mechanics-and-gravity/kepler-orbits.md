# Kepler orbits

`mechanics-and-gravity/kepler-orbits` · main track · working depth · physics-reviewed · revision 2 · 2026-09-22

Teaches: `central-force`, `conservation-of-angular-momentum`, `keplers-second-law`, `two-body-problem`, `kepler-problem`, `newtonian-effective-potential`, `binet-equation`, `conic-section-orbit`, `eccentricity`, `elliptical-orbit-geometry`, `keplers-first-law`, `keplers-third-law`, `bound-and-unbound-orbits`, `orbital-energy`, `negative-specific-heat`, `laplace-runge-lenz-vector`, `bertrands-theorem`

Builds on: `newtons-laws-and-inertial-frames`, `rotating-frames`, `lagrangian-and-hamiltonian-mechanics`, `newtonian-gravity-as-a-field`, `coordinates-curves-and-surfaces`

**A force that always points at one centre exerts no torque, so the motion keeps to a plane and sweeps equal areas in equal times. Eliminating the angle leaves a one-dimensional problem in an effective potential, and for an inverse-square attraction the orbit is always a conic with the centre of force at a focus. Energy fixes the size and the period, energy with angular momentum fixes the shape, and a third conserved vector pins the direction of closest approach, so that the orbit closes.**

Before the telescope, Tycho Brahe measured the place of Mars on the sky a few thousand times, to a couple of arcminutes. Kepler fitted those positions for years and ended with an ellipse of eccentricity $e = 0.0934$, with the Sun at a focus.

That number hides a surprise. Half the ellipse's longest diameter, called its semi-major axis and written $a$, is $1.5237$ astronomical units, and one astronomical unit is $1.496\times10^{11}$ metres. The ellipse is almost round: its shortest diameter falls short of its longest by a fraction $1 - \sqrt{1 - e^2} = 0.0044$, which is $0.44$ per cent, and no naked eye could catch that. What the data caught was an offset instead. The Sun sits a distance $ea = 0.1423$ astronomical units, about 21 million kilometres, from the centre of the ellipse, so Mars runs between $1.381$ and $1.666$ astronomical units from the Sun.

Kepler had three laws and no reason for any of them. This section gets all three out of the inverse-square law of *Newtonian gravity as a field*, and finds that gravity is one of only two force laws whose bound orbits close.

## Two bodies, one fictitious body

Kepler's laws speak of a planet going around the Sun, but the Sun is not nailed down: by Newton's third law the planet pulls back just as hard. Two bodies that pull on each other and on nothing else are the two-body problem, and the first move in solving it is to show that it is really a one-body problem.

Write the positions as $\mathbf r_1$ and $\mathbf r_2$, the masses as $m_1$ and $m_2$, and let $\mathbf r = \mathbf r_1 - \mathbf r_2$, with $r = |\mathbf r|$ and $\hat{\mathbf r} = \mathbf r/r$. Newton's second law, applied twice, gives

$$m_1\ddot{\mathbf r}_1 = -\frac{Gm_1m_2}{r^2}\hat{\mathbf r},\qquad m_2\ddot{\mathbf r}_2 = +\frac{Gm_1m_2}{r^2}\hat{\mathbf r}.$$

Adding these, the right-hand sides cancel, so the centre of mass $\mathbf R = (m_1\mathbf r_1 + m_2\mathbf r_2)/(m_1+m_2)$ has zero acceleration and carries no information about the orbit. Dividing each equation by its own mass and subtracting instead gives $\ddot{\mathbf r} = -G(m_1+m_2)\hat{\mathbf r}/r^2$. Write $M = m_1+m_2$ for the total mass and $\mu = m_1m_2/M$ for the reduced mass, and multiply by $\mu$:

$$\mu\ddot{\mathbf r} = -\frac{GM\mu}{r^2}\hat{\mathbf r}.$$

That is Newton's second law for one body of mass $\mu$ at $\mathbf r$, pulled by a fixed mass $M$ at the origin. Its energy is $\tfrac12\mu|\dot{\mathbf r}|^2 - GM\mu/r$, and because $GM\mu = Gm_1m_2$ that is exactly the energy of the real pair, measured in the frame in which the centre of mass is at rest. (From the next part onward $\dot r$ means the rate of change of the distance $r$ alone, which is why the whole relative velocity is written $\dot{\mathbf r}$ and its size $|\dot{\mathbf r}|$.)

Subtracting $\mathbf R$ from each position gives $\mathbf r_1 - \mathbf R = (m_2/M)\,\mathbf r$ and $\mathbf r_2 - \mathbf R = -(m_1/M)\,\mathbf r$. So each body runs on a scaled copy of the curve $\mathbf r$ traces, drawn about the centre of mass; the lighter body gets the larger copy, and the minus sign keeps the two bodies on opposite sides of the centre of mass at every instant.

*Two attracting bodies split into a centre of mass that never accelerates and one fictitious body, of the reduced mass, in the fixed field of their total mass.*

## What a central force cannot change

A central force on a body at $\mathbf r$ from a fixed centre is $\mathbf F = F(r)\,\hat{\mathbf r}$: along the line to the centre, with a size set by the distance alone. Gravity is the case $F(r) = -GM\mu/r^2$, the minus sign meaning inward.

The angular momentum about the centre is $\mathbf L = \mathbf r\times\mathbf p$, with $\mathbf p = \mu\dot{\mathbf r}$. Differentiating, $\dot{\mathbf L} = \dot{\mathbf r}\times\mathbf p + \mathbf r\times\dot{\mathbf p} = \mathbf r\times\mathbf F$, since $\dot{\mathbf r}$ and $\mathbf p$ are parallel. For a central force $\mathbf F$ is parallel to $\mathbf r$ as well, so that term vanishes too: $\mathbf L$ is constant in size and in direction.

Then $\mathbf r\cdot\mathbf L = 0$ at every instant, and the motion stays in the plane through the centre perpendicular to $\mathbf L$. (If $\mathbf L = \mathbf 0$ the body moves on a fixed line through the centre; that case is set aside from here on.) In polar coordinates $(r,\phi)$ in that plane, with $\phi$ increasing in the direction of travel, the transverse velocity is $r\dot\phi$, so

$$L = \mu r^2\dot\phi = \text{constant},\qquad h \equiv \frac{L}{\mu} = r^2\dot\phi.$$

*Lagrangian and Hamiltonian mechanics* gets the same constant in one line: $\mathcal L = \tfrac12\mu(\dot r^2 + r^2\dot\phi^2) - U(r)$ has no $\phi$ in it, so $\phi$ is cyclic, and its conjugate momentum $\partial\mathcal L/\partial\dot\phi = \mu r^2\dot\phi$ is a constant of the motion, which is $L$ again. (The Lagrangian is written $\mathcal L$ here, because $L$ is the angular momentum throughout this section.)

In a time $dt$ the line from the centre sweeps a triangle of base $r$ and height $r\,d\phi$, so $dA = \tfrac12 r^2 d\phi$ and $dA/dt = L/2\mu$. That is Kepler's second law, and only the direction of the force went into it: it holds for a puck on a spring pinned to a table too.

*A central force exerts no torque, so the motion lies in one plane and the line to the centre sweeps equal areas in equal times, whatever the force's dependence on distance.*

## The radial problem and its landscape

Two coordinates are left, and one is already solved. Substituting $\dot\phi = L/\mu r^2$ into $E = \tfrac12\mu(\dot r^2 + r^2\dot\phi^2) - GM\mu/r$ removes $\phi$ completely:

$$E = \tfrac12\mu\dot r^2 + U_{\text{eff}}(r),\qquad U_{\text{eff}}(r) = \frac{L^2}{2\mu r^2} - \frac{GM\mu}{r}.$$

This is the Kepler problem in one dimension: a particle of mass $\mu$ on the half-line $r>0$, whose radial story the graph of $U_{\text{eff}}$ tells in full. As $r\to0$ the first term diverges like $r^{-2}$ and beats the second's $r^{-1}$, so $U_{\text{eff}}\to+\infty$: a wall, called the centrifugal barrier, and the reason a body with $L\neq0$ never reaches the centre. As $r\to\infty$ both terms vanish, but the attraction, falling only as $r^{-1}$, is the last to die, so $U_{\text{eff}}\to0$ from below. Between them lies exactly one minimum, where $dU_{\text{eff}}/dr = -L^2/\mu r^3 + GM\mu/r^2$ vanishes:

$$r_c = \frac{L^2}{GM\mu^2} = \frac{h^2}{GM},\qquad U_{\text{eff}}(r_c) = -\frac{G^2M^2\mu^3}{2L^2},$$

and there $d^2U_{\text{eff}}/dr^2 = GM\mu/r_c^3 > 0$. So the minimum is a stable circular orbit: a body placed there with $\dot r = 0$ keeps $r = r_c$, and one nudged off it oscillates about $r_c$.

Wherever $E = U_{\text{eff}}(r)$ the radial speed vanishes: a turning point. The body is not at rest there: it is still moving at right angles to the line to the centre, at the transverse speed $r\dot\phi = h/r$. Only $r$ stops changing, and then reverses.

The barrier is bookkeeping, not a push. The term $L^2/2\mu r^2$ is the transverse kinetic energy $\tfrac12\mu r^2\dot\phi^2$ with $\dot\phi$ traded for the constant $L$, then filed under potential energy. In the inertial frame the only force is gravity, inward everywhere. Minus the derivative of that term, $L^2/\mu r^3 = \mu r\dot\phi^2$, is the centrifugal force of *Rotating frames*, which is what a rider turning with the line to the centre must add.

*Trading the angle for the constant angular momentum gives one-dimensional motion in an effective potential: a centrifugal wall, a well whose minimum is the stable circular orbit, and turning points where the energy meets the curve.*

## One substitution straightens the orbit

The effective potential gives $r(t)$ only as an integral that is not elementary, but the shape of the orbit, $r$ as a function of $\phi$, comes out far more simply. Two changes do it: make $\phi$ the independent variable, using $d/dt = (h/r^2)\,d/d\phi$, and make $u = 1/r$ the unknown. Then

$$\dot r = hu^2\left(-\frac{1}{u^2}\frac{du}{d\phi}\right) = -h\frac{du}{d\phi},\qquad \ddot r = -h^2u^2\frac{d^2u}{d\phi^2}.$$

The radial component of $\mu\ddot{\mathbf r} = F(r)\hat{\mathbf r}$ in polar coordinates is $\mu(\ddot r - r\dot\phi^2) = F(r)$, and $r\dot\phi^2 = h^2u^3$. With $F = -GM\mu u^2$ this reads $\mu(-h^2u^2u'' - h^2u^3) = -GM\mu u^2$. The reduced mass cancels from both sides, and dividing what is left by $-h^2u^2$ leaves

$$\frac{d^2u}{d\phi^2} + u = \frac{GM}{h^2}.$$

This is the Binet equation for gravity. Its right-hand side is a constant, so it is a harmonic oscillator displaced from zero, with $\phi$ playing the part time usually plays. Its solution is that constant plus a free oscillation of period exactly $2\pi$ in $\phi$, $u = (GM/h^2)\,[1 + e\cos(\phi-\phi_0)]$, with constants of integration $e\ge0$ and $\phi_0$. Inverting,

$$r = \frac{l}{1 + e\cos(\phi-\phi_0)},\qquad l = \frac{h^2}{GM}.$$

That is the polar equation of a conic section with a focus at the origin, met in *Coordinates, curves and surfaces*: $l$ is the semi-latus rectum, $e$ the eccentricity, $\phi_0$ the direction of closest approach. Every Kepler orbit is that one formula.

The inverse-square law entered once, and did one thing: it made the right-hand side a constant. Any other force law leaves a function of $u$ there, and in general the orbit is then not a conic with the centre of force at a focus. One other law is an exception: the linear spring $F = -kr$ traces an ellipse *centred* on the force instead of focused on it.

*Writing the inverse distance as a function of the angle turns inverse-square motion into a displaced harmonic oscillator, whose solution is a conic with the centre of force at a focus.*

## Energy and angular momentum fix size and shape

Two constants, $E$ and $L$, fix the orbit up to its orientation, and $L$ is already in $l = h^2/GM$. For $e$, evaluate the energy at a turning point, where $\dot r = 0$ and $E = U_{\text{eff}}(r)$; multiplying through by $r^2$,

$$Er^2 + GM\mu\,r - \frac{L^2}{2\mu} = 0.$$

For $E<0$ this has two positive roots, the least and greatest distances $r_-$ and $r_+$. Their sum is the major axis, which defines the semi-major axis $a$ through $r_+ + r_- = 2a$; the quadratic makes that sum $-GM\mu/E$, so $E = -GM\mu/2a$: the energy of a bound orbit depends on its size alone, not its shape. The conic formula gives those same two distances at $\phi-\phi_0 = 0$ and $\pi$, namely $r_- = l/(1+e)$ and $r_+ = l/(1-e)$. Their sum is $2l/(1-e^2)$, so $a = l/(1-e^2)$ and therefore $r_\pm = a(1\pm e)$. The product of the roots is $-L^2/2\mu E$ from the quadratic and $a^2(1-e^2)$ from these; eliminating $a$,

$$e^2 = 1 + \frac{2EL^2}{G^2M^2\mu^3}.$$

So the sign of $E$ is the sign of $e^2-1$, and the three conics are three ranges of the energy. An orbit with $E<0$ is bound: it never gets farther from the centre than a fixed distance. An orbit with $E\ge0$ is unbound: it reaches arbitrarily large $r$ and never comes back.

- $E<0$ gives $e<1$: a bound ellipse, retraced between $r_-$ and $r_+$ forever. The lowest energy allowed, $E = -G^2M^2\mu^3/2L^2$, is the bottom of the effective-potential well, and there $e = 0$: the circular orbit.
- $E=0$ gives $e=1$: a parabola, reaching arbitrarily large $r$ with its speed tending to zero. This is the case in which the relative speed is exactly the escape speed $\sqrt{2GM/r}$ of *Newtonian gravity as a field*, with $M$ the pair's total mass.
- $E>0$ gives $e>1$: a hyperbola. The denominator vanishes where $\cos(\phi-\phi_0) = -1/e$, so only angles with $|\phi-\phi_0| < \arccos(-1/e)$ lie on the orbit; the body comes in along one asymptote, passes one turning point, and leaves along the other.

Putting $E = -GM\mu/2a$ with $E = \tfrac12\mu v^2 - GM\mu/r$ gives the relative speed at any distance on any of these orbits, $v^2 = GM(2/r - 1/a)$, with $a = -GM\mu/2E$ negative for a hyperbola.

*Energy alone fixes the semi-major axis and the period; energy with angular momentum fixes the eccentricity, which decides between a bound ellipse, a parabola and a hyperbolic fly-by.*

## The ellipse, and the harmonic law

For $0\le e<1$ the conic is an ellipse with the centre of force at one focus. That is Kepler's first law, now a theorem rather than a fit. Its geometry is fixed by $a$ and $e$:

- semi-major axis $a = l/(1-e^2)$, semi-minor axis $b = a\sqrt{1-e^2} = \sqrt{al}$;
- the two foci lie on the major axis, each a distance $ea$ from the centre;
- the apsides, where the distance is stationary, are perihelion at $r_- = a(1-e)$ and aphelion at $r_+ = a(1+e)$, called periapsis and apoapsis about a centre other than the Sun, and perigee and apogee about the Earth;
- area $\pi ab$.

Those relations are where the opening's numbers came from. The flattening $1 - \sqrt{1-e^2}$ is second order in $e$, so for Mars it is $0.44$ per cent and invisible, while the offset $ea$ and the swing in distance are first order, $9.34$ per cent of $a$. Eccentricity shows itself in where the Sun sits, not in the shape of the curve.

Kepler's third law now costs two lines. Equal areas sweeps the whole area at the steady rate $h/2$, so $T = \pi ab/(h/2)$. With $b = a\sqrt{1-e^2}$ and $h^2 = GMl = GMa(1-e^2)$,

$$T = \frac{2\pi a^2\sqrt{1-e^2}}{\sqrt{GMa(1-e^2)}} = 2\pi\sqrt{\frac{a^3}{GM}},\qquad T^2 = \frac{4\pi^2a^3}{G(m_1+m_2)}.$$

The eccentricity cancels: a needle-thin ellipse and a circle with the same $a$ have the same period. And the mass is the pair's total. For a planet the Sun's partner is negligible, Jupiter being 0.095 per cent of the Sun-plus-Jupiter total, which is why Kepler's fit worked with one constant; for a binary star that total is the whole content of the law.

*A bound orbit is an ellipse with the attracting centre at a focus, and its period is set by the semi-major axis and the total mass alone, never by the eccentricity.*

## Why Newtonian orbits close

A bound orbit in a general central field need not close: the angle swept from one closest approach to the next has no reason to be $2\pi$, and unless it is a rational multiple of $2\pi$ the orbit eventually fills the ring between $r_-$ and $r_+$. The Kepler orbit does close, since its Binet solution has period exactly $2\pi$ in $\phi$, and that means one more conserved quantity, fixing the direction of closest approach for all time:

$$\mathbf A = \mathbf p\times\mathbf L - GM\mu^2\,\hat{\mathbf r},$$

the Laplace-Runge-Lenz vector. To check it, differentiate: only $\mathbf p$ and $\hat{\mathbf r}$ change, so $\dot{\mathbf A} = \mathbf F\times\mathbf L - GM\mu^2\,d\hat{\mathbf r}/dt$. With $\mathbf F = -(GM\mu/r^2)\hat{\mathbf r}$, $\mathbf L = \mu\,\mathbf r\times\dot{\mathbf r}$ and $\hat{\mathbf r}\times(\mathbf r\times\dot{\mathbf r}) = \mathbf r\,\dot r - r\dot{\mathbf r}$,

$$\mathbf F\times\mathbf L = -\frac{GM\mu^2}{r^2}\big(\mathbf r\,\dot r - r\dot{\mathbf r}\big) = GM\mu^2\frac{d}{dt}\Big(\frac{\mathbf r}{r}\Big),$$

so the two terms cancel and $\dot{\mathbf A} = \mathbf 0$. Dotting $\mathbf A$ with $\mathbf r$, and using $\mathbf r\cdot(\mathbf p\times\mathbf L) = L^2$, gives $Ar\cos\psi = L^2 - GM\mu^2 r$ with $\psi$ the angle from $\mathbf A$ to $\mathbf r$. That rearranges into the conic equation, with $e = A/GM\mu^2$ and $\psi$ in place of $\phi-\phi_0$: $\mathbf A$ lies in the orbital plane, points from the focus toward the closest approach, and has length $A = GM\mu^2e$. Its constancy is exactly the statement that the direction of closest approach never moves.

Is the inverse-square law special in this, or would most attractions do? Bertrand's theorem answers that among central attractions with a stable circular orbit exactly two close every bounded orbit: the inverse-square attraction $F = -k/r^2$ and the linear spring $F = -kr$, each with $k>0$. Those are the same two laws whose orbits are conics. The theorem is stated here without proof, because no proof short enough for this section exists; take it on trust.

Under any other law bound orbits precess, turning their closest approach a little each time round. So for a pair of bodies alone in space, a measured drift of the closest approach is evidence that the force between them is not exactly inverse-square, or that Newtonian gravity is not the last word. Real planets are not alone: they pull on one another, and those pulls move each perihelion by an amount that can be worked out. Mercury's perihelion drifts by more than that amount.

*For the inverse-square law a third constant, the Laplace-Runge-Lenz vector, points from the focus to the closest approach and pins it there, and only two force laws close every bound orbit at all.*

## A bound system that heats as it cools

One consequence of $E = -GM\mu/2a$ deserves a name of its own. On a circular orbit of radius $a$, balancing $\mu v^2/a$ against $GM\mu/a^2$ gives $\mu v^2 = GM\mu/a$, so the kinetic energy is $GM\mu/2a$ and the potential energy is $-GM\mu/a$. Comparing with $E$,

$$E_{\text{kin}} = -E = \frac{GM\mu}{2a}.$$

The same relation holds between the time averages on any bound Kepler orbit; we take that on trust. Remove energy from the system, by drag, by tides or by gravitational radiation, and $E$ becomes more negative, so $a$ shrinks and $E_{\text{kin}}$ rises: the system loses energy and speeds up.

Take a 1 kilogram satellite on a circular orbit 300 kilometres up, where $r = 6671$ kilometres and $v = \sqrt{GM/r} = 7.730$ kilometres per second. Drag removes $2.256\times10^5$ joules, and it arrives on a circular orbit at 250 kilometres altitude moving at $7.759$ kilometres per second, 29 metres per second faster, with its period cut from 90.4 to 89.4 minutes. The potential energy fell by $4.512\times10^5$ joules, twice what the kinetic energy gained, and the difference is what drag carried away.

If a temperature is read off the mean kinetic energy, such a system therefore has a negative specific heat, or equally a negative heat capacity: take energy out, and the temperature goes up. It cannot sit in stable equilibrium with an ordinary heat bath, because any small transfer of energy runs away. It is also why a star whose core is held up by ordinary gas pressure does not simply cool when its fuel runs out: the core loses energy, contracts, and grows hotter until the next fuel ignites. Once something other than gas pressure holds the core up, the argument no longer applies and the star does cool.

*Because a bound orbit's kinetic energy equals minus its total energy, a self-gravitating system that loses energy contracts and speeds up, as though its heat capacity were negative.*

## Key equations

**Angular momentum and equal areas** (derived-here)

$$L = \mu r^{2}\dot\phi = \text{constant},\qquad \frac{dA}{dt} = \tfrac12 r^{2}\dot\phi = \frac{L}{2\mu}$$

For any central force the motion is planar and area is swept at a steady rate: Kepler's second law.

- $L$: angular momentum about the centre
- $\mu$: reduced mass of the pair

Say: The angular momentum is the reduced mass times the distance squared times the rate of change of the angle, and it is constant; the area swept per unit time is the angular momentum over twice the reduced mass.

**Radial energy and the effective potential** (derived-here)

$$E = \tfrac12\mu\dot r^{2} + U_{\text{eff}}(r),\qquad U_{\text{eff}}(r) = \frac{L^{2}}{2\mu r^{2}} - \frac{GM\mu}{r}$$

Eliminating $\dot\phi$ with the constant $L$ reduces the orbit to one-dimensional motion in $r$. The first term is transverse kinetic energy in disguise, not a force.

- $E$: total energy of the relative motion
- $M$: total mass of the pair

Say: The energy is one half the reduced mass times the radial speed squared, plus the effective potential: the angular momentum squared over twice the reduced mass times the distance squared, minus big G times the total mass times the reduced mass over the distance.

**Binet equation for gravity** (derived-here)

$$\frac{d^{2}u}{d\phi^{2}} + u = \frac{GM}{h^{2}},\qquad u = \frac{1}{r},\qquad h = \frac{L}{\mu} = r^{2}\dot\phi$$

The orbit equation for an inverse-square attraction: a harmonic oscillator in $\phi$, displaced from zero, whose period in $\phi$ is exactly $2\pi$.

- $u$: inverse of the distance from the centre
- $h$: angular momentum per unit reduced mass

Say: The second derivative of the inverse distance with respect to the angle, plus the inverse distance, equals big G times the total mass over the specific angular momentum squared.

**Conic-section orbit** (derived-here)

$$r = \frac{l}{1 + e\cos(\phi - \phi_0)},\qquad l = \frac{h^{2}}{GM} = a\,(1 - e^{2})$$

Every inverse-square trajectory is a conic with the centre of force at a focus: $l$ sets the scale, $e$ the shape, $\phi_0$ the direction of closest approach.

- $l$: semi-latus rectum
- $e$: eccentricity of the orbit

Say: The distance equals the semi latus rectum over one plus the eccentricity times the cosine of the angle from the direction of closest approach.

**Energy, eccentricity and speed** (derived-here)

$$E = -\frac{GM\mu}{2a},\qquad e^{2} = 1 + \frac{2EL^{2}}{G^{2}M^{2}\mu^{3}},\qquad v^{2} = GM\left(\frac{2}{r} - \frac{1}{a}\right)$$

Energy fixes $a$; energy with angular momentum fixes $e$; the two give the relative speed at any distance. The last is the vis-viva equation, and it holds for a hyperbola with $a$ negative.

- $a$: semi-major axis, negative for a hyperbola
- $v$: relative speed of the two bodies

Say: The energy is minus big G times the total mass times the reduced mass over twice the semi major axis. The eccentricity squared is one plus twice the energy times the angular momentum squared, over big G squared times the total mass squared times the reduced mass cubed. The speed squared is big G times the total mass, times two over the distance minus one over the semi major axis.

**Kepler's third law** (derived-here)

$$T^{2} = \frac{4\pi^{2}a^{3}}{G\,(m_1 + m_2)}$$

The period is set by the semi-major axis and the total mass alone; the eccentricity cancels, so measuring $a$ and $T$ measures $m_1 + m_2$ and nothing else.

- $T$: orbital period
- $a$: semi-major axis of the relative orbit

Say: The period squared equals four pi squared times the semi major axis cubed, over big G times the sum of the two masses.

## Worked examples

**a-long-period-comet.** A comet is watched through its closest approach to the Sun, $0.900$ astronomical units out, and its period is found to be $125$ years. Treat the Sun as the whole of the total mass, with $GM = 1.327\times10^{20}$ m$^3$ s$^{-2}$, and take one astronomical unit as $1.496\times10^{11}$ m. Find the semi-major axis, the eccentricity and the greatest distance, then the relative speed at each apsis, and check the two speeds against the constancy of $L$.

1. Kepler's third law, measured in astronomical units, years and solar masses, reads $M = a^3/T^2$, because the Earth's orbit has $a = 1$, $T = 1$ and a total mass of one solar mass to better than a part in a hundred thousand. With $M = 1$ and $T = 125$ this gives $a^3 = 125^2$, so $a = 125^{2/3} = 25.0$ astronomical units, which is $3.740\times10^{12}$ m.
2. The closest approach is $r_- = a(1-e)$, so $e = 1 - r_-/a = 1 - 0.900/25.0 = 0.964$.
3. The greatest distance is $r_+ = a(1+e) = 25.0\times1.964 = 49.1$ astronomical units, which is $7.345\times10^{12}$ m. Check: $r_- + r_+ = 0.900 + 49.1 = 50.0 = 2a$.
4. Vis-viva at closest approach, with $r_- = 1.346\times10^{11}$ m: $v_-^2 = GM(2/r_- - 1/a) = 1.327\times10^{20}\times(1.48544\times10^{-11} - 2.67380\times10^{-13}) = 1.936\times10^{9}$ m$^2$ s$^{-2}$, so $v_- = 44.0$ km s$^{-1}$.
5. The same at the greatest distance, with $r_+ = 7.345\times10^{12}$ m: $v_+^2 = 1.327\times10^{20}\times(2.72280\times10^{-13} - 2.67380\times10^{-13}) = 6.50\times10^{5}$ m$^2$ s$^{-2}$, so $v_+ = 0.806$ km s$^{-1}$.
6. At an apsis $\dot r = 0$, so the velocity there is entirely transverse and $h = rv$. Then $r_-v_- = 1.346\times10^{11}\times4.400\times10^{4} = 5.92\times10^{15}$ m$^2$ s$^{-1}$ and $r_+v_+ = 7.345\times10^{12}\times8.064\times10^{2} = 5.92\times10^{15}$ m$^2$ s$^{-1}$: equal, as the constancy of $L$ demands.

Answer: $a = 25.0$ astronomical units, $e = 0.964$, $r_+ = 49.1$ astronomical units, $v_- = 44.0$ km s$^{-1}$ and $v_+ = 0.806$ km s$^{-1}$. The comet passes the Sun at about fifty-five times the speed it has when it turns around. Its $44.0$ km s$^{-1}$ sits just under the escape speed $\sqrt{2GM/r_-} = 44.4$ km s$^{-1}$ at that distance, which it has to for a bound orbit.

*The third law turns a measured period into a size, the closest approach turns that size into a shape, and the speed relation turns both into a speed at any distance on the orbit.*

## Checks

**total-mass-of-sirius** (numeric): Sirius A and Sirius B orbit each other. Their relative orbit has semi-major axis 19.8 astronomical units and period 50.13 years. (a) What mass does Kepler's third law give? (b) A student says that is the mass of Sirius A, since B is the faint companion. Correct that, and say what further measurement would separate the two masses.

Answer: (a) In astronomical units, years and solar masses the law reads $M = a^3/T^2$, because the Earth's orbit has $a = 1$, $T = 1$ and $M = 1$. So $M = 19.8^3/50.13^2 = 7762/2513 = 3.09$ solar masses. (b) That is the total mass $m_1+m_2$; the derivation used the sum and nothing else, so no re-reading of the orbit's size or period can split it. What splits it is each star's own ellipse about the centre of mass, whose semi-major axes satisfy $m_1a_1 = m_2a_2$. For Sirius that gives roughly $2.1$ and $1.0$ solar masses.

Key points: The third law gives the total mass of the pair, about 3.09 solar masses; Separating the masses needs the ratio of their own ellipses about the centre of mass

Numeric: total mass of the pair = 3.09 M_sun

**what-the-barrier-is** (explain): A probe is on a bound orbit around the Earth. At its closest approach, the periapsis, its distance from the Earth's centre stops falling and starts to rise. (a) In the inertial frame in which the Earth's centre is at rest, name every force on the probe at that instant, with its direction. (b) Say what the angular momentum term in the effective potential actually is. (c) Why can a probe with non-zero angular momentum never reach the centre, however much energy it has?

Answer: (a) One force: gravity, of size $GM\mu/r^2$, pointing inward, at the closest approach exactly as everywhere else on the orbit. Nothing pushes outward. (b) It is the transverse kinetic energy $\tfrac12\mu r^2\dot\phi^2$ with $\dot\phi$ replaced by $L/\mu r^2$: kinetic energy, written as a function of $r$ and filed under potential energy so the radial motion reads as one-dimensional. At the closest approach $\dot r = 0$, but the probe is still moving at right angles to the line to the Earth, at the transverse speed $h/r$, and the inward force bends that motion around. (c) Because $L^2/2\mu r^2$ grows like $r^{-2}$ while $-GM\mu/r$ only falls like $r^{-1}$, so $U_{\text{eff}}\to+\infty$ as $r\to0$: reaching the centre would take infinite energy.

Key points: The only force is gravity, inward at every point, including the closest approach; The barrier term is transverse kinetic energy rewritten with the constant angular momentum, and it diverges at the centre

**drag-speeds-a-satellite-up** (numeric): A $1.0$ kilogram satellite on a circular orbit 300 kilometres above the ground is dragged slowly down to a circular orbit at 250 kilometres. Take the Earth's radius as 6371 kilometres and $GM = 3.986\times10^{14}$ m$^3$ s$^{-2}$. (a) Find its speed on each orbit. (b) Find the energy drag removed. (c) Compare (b) with the change in kinetic energy, and explain the sign of each.

Answer: (a) $v = \sqrt{GM/r}$ with $r = 6671$ and $6621$ kilometres gives $7.730$ and $7.759$ kilometres per second, so the satellite ends up $29$ metres per second faster. (b) $E = -GM\mu/2r$ gives $-2.988\times10^7$ and $-3.010\times10^7$ joules, so drag removed $2.256\times10^5$ joules. (c) The kinetic energy rose by exactly that same $2.256\times10^5$ joules, while the potential energy fell by twice as much, $4.512\times10^5$ joules. The potential energy pays for both the heat carried off and the extra speed. The period falls from $90.4$ to $89.4$ minutes.

Key points: The satellite speeds up by about 29 metres per second while losing energy; The energy removed equals the gain in kinetic energy; the potential energy falls by twice as much

Numeric: gain in orbital speed = 29.0 m/s; energy removed by drag = 225600.0 J

**a-slightly-wrong-force-law** (predict): Suppose the attraction fell off as the distance to the power 2.1 instead of as the distance squared, everything else unchanged. (a) Is angular momentum still conserved, and does equal areas still hold? (b) Is a bound orbit still trapped between an inner and an outer turning point? (c) Is a nearly circular bound orbit still a closed ellipse? Name the theorem that settles (c), and say what an observer would see over many orbits.

Answer: (a) Yes. The force still points along the line to the centre, so $\mathbf r\times\mathbf F = \mathbf 0$ and $dA/dt = L/2\mu$; equal areas never used the distance dependence. (b) Yes. The effective potential still has an $r^{-2}$ centrifugal wall and an attractive well tending to zero far away, so any orbit with $E<0$ is trapped between two turning points. (c) No. Bertrand's theorem allows only the inverse-square attraction and the linear spring. For an attraction $F = -k/r^n$ the Binet equation linearises about a circular orbit to $\delta'' + (3-n)\delta = 0$, where $\delta$ is a small departure of $u = 1/r$ from its circular value. So for a nearly circular orbit the angle from one closest approach to the next is $2\pi/\sqrt{3-n}$, here $2\pi/\sqrt{0.9} = 379.5$ degrees: an advance of $19.5$ degrees each time round. A more eccentric orbit advances by a different amount, but still not by zero. The observer sees the closest approach creep steadily around and the orbit slowly fill the ring between its two turning circles.

Key points: Equal areas and the two turning points survive any central force; Bertrand's theorem allows only the inverse-square attraction and the linear spring to close every bound orbit, so here a nearly circular orbit's closest approach advances about 19.5 degrees each time round

Numeric: advance of the closest approach per orbit, for a nearly circular orbit = 19.5 deg

## Misconceptions

- **equal-areas-comes-from-inverse-square**: "Kepler's second law is a property of the inverse-square law of gravity." — Equal areas follows from the force pointing along the line to the centre and nothing else. Any central force sweeps equal areas, whatever its dependence on distance. (diagnosed by a-slightly-wrong-force-law)
- **centrifugal-barrier-is-a-real-force**: "The centrifugal barrier is an outward force that holds an orbiting body off the centre." — In the inertial frame the only force is gravity, inward everywhere. The barrier term is transverse kinetic energy rewritten with the constant angular momentum. (diagnosed by what-the-barrier-is)
- **third-law-gives-the-central-mass**: "Kepler's third law applied to an orbit gives the mass of the central body." — It gives the total mass of the pair; splitting it needs the ratio of the two bodies' own ellipses about their centre of mass. (diagnosed by total-mass-of-sirius)
- **losing-energy-slows-an-orbit**: "A satellite that loses energy to drag must slow down." — It speeds up: less total energy means a smaller semi-major axis, and a bound orbit's kinetic energy is minus its total energy. (diagnosed by drag-speeds-a-satellite-up)
- **every-attraction-gives-closed-ellipses**: "Any central attraction that falls off with distance gives closed elliptical orbits." — Bertrand's theorem allows exactly two: the inverse-square attraction and the linear spring. Under any other central attraction bound orbits precess. (diagnosed by a-slightly-wrong-force-law)

## Glossary

- **central force**: A force pointing along the line to a fixed centre, whose size depends only on the distance from it. (`central-force`)
- **reduced mass**: The product of two masses divided by their sum; the fictitious body of this mass moves in the field of their total mass. (`two-body-problem`)
- **effective potential**: The potential energy plus the angular momentum term, whose graph against distance governs the radial motion alone. (`newtonian-effective-potential`)
- **centrifugal barrier**: The steep rise of the effective potential at small distance that keeps a body with angular momentum away from the centre. (`newtonian-effective-potential`)
- **turning point**: A distance where the radial speed vanishes because the energy equals the effective potential; the body there is still moving sideways. (`newtonian-effective-potential`)
- **eccentricity**: The shape number of a conic: zero for a circle, under one for an ellipse, one for a parabola, above one for a hyperbola. (`eccentricity`)
- **semi-major axis**: Half the longest diameter of an ellipse; for a bound orbit it alone fixes the energy and the period. (`elliptical-orbit-geometry`)
- **apsides**: The closest and farthest points of an orbit: perihelion and aphelion about the Sun, periapsis and apoapsis in general. (`elliptical-orbit-geometry`)
- **Bertrand's theorem**: The result that only the inverse-square law and the linear spring close every bounded orbit in a central field. (`bertrands-theorem`)
- **two-body problem**: The motion of two bodies that pull only on each other; it splits into a centre of mass that never accelerates and one fictitious body. (`two-body-problem`)
- **bound and unbound orbits**: An orbit is bound when its energy is negative and it never passes a greatest distance, and unbound when its energy is zero or more and it escapes. (`bound-and-unbound-orbits`)
- **Binet equation**: The orbit equation got by taking the angle as the variable and the inverse distance as the unknown; for an inverse-square attraction it is a displaced harmonic oscillator. (`binet-equation`)
- **semi-latus rectum**: The distance from the focus to the orbit measured at right angles to the major axis; it sets the scale of the conic. (`elliptical-orbit-geometry`)
- **vis-viva equation**: The relation that gives the relative speed at any distance from the semi-major axis and the total mass alone. (`orbital-energy`)
- **Laplace-Runge-Lenz vector**: A vector conserved only for an inverse-square attraction, pointing from the focus toward the closest approach, with length proportional to the eccentricity. (`laplace-runge-lenz-vector`)
- **negative specific heat**: The property of a bound self-gravitating system that taking energy out raises its mean kinetic energy, and so the temperature read from it. (`negative-specific-heat`)

## Visuals

- `effective-potential-with-a-sliding-energy-line` (flagship): The one-dimensional reading of an orbit: the effective potential curve with the energy as a line the learner drags, beside the orbit that energy produces. Sketch: Left panel: $U_{\text{eff}}(r)$ against $r$ for a chosen angular momentum, with the centrifugal and gravitational terms drawable separately, the minimum marked at $r_c = h^2/GM$, and a horizontal energy line the learner drags. Turning points light up where the line meets the curve, and the line cannot go below the minimum, so the impossible case never appears. Right panel: the orbit drawn in the plane as it is traced, with the body's current radius shown as a bead running along the energy line. A slider for $L$ lifts the barrier and moves the minimum outward. Readouts give $E$, $L$, $a$, $e$ and the period. Presets: circular, Mercury, a long-period comet, escape at $E = 0$, and a hyperbolic fly-by. Design rule: the barrier is labelled as kinetic energy in the potential column, never as a force, because learners read the wall as an outward push.
- `one-launch-point-many-conics` (core): One launch point with a speed dial and a direction dial, sweeping the family from circle to hyperbola so that the sign of the energy and the value of the eccentricity are seen to move together. Sketch: A fixed mass at the origin and a launch point at a chosen distance. Two dials set the launch speed and the angle between the velocity and the radial direction. The conic is drawn at once, with readouts of $E$, $L$, $e$, $a$ and, where it applies, the period. The circular speed and the escape speed are marked on the speed dial, and the name of the conic changes as the speed crosses the escape value. A ghost trace keeps the previous curve so the family can be compared. Launching straight at the centre is refused, with a note that zero angular momentum is the degenerate radial case.

## Tutor

Opening question: Here is a fact about Mars that took Kepler years to trust. Its orbit is an ellipse, but that ellipse is less than half a per cent away from a perfect circle. Yet the distance from Mars to the Sun changes by about a fifth over one Martian year. How can both of those be true at once?

- Q: Is the centrifugal barrier a real force? A: No. In a frame where the Sun is at rest, the only force on the planet is gravity, and it points inward everywhere on the orbit, including at closest approach. The barrier is the energy of the sideways motion, written as a function of distance and filed under potential energy so that the in and out motion can be read off one graph. It is honest bookkeeping, not a push.
- Q: Why does an orbit that loses energy end up faster? A: Because the energy of a bound orbit is negative and depends only on the size of the orbit. Take energy away and the orbit shrinks, and a smaller orbit is a faster one. For a circular orbit the kinetic energy is exactly minus the total energy, so whatever the total loses, the kinetic energy gains. A satellite dragged from three hundred kilometres altitude down to two hundred and fifty gains about twenty nine metres per second.

## Review: novice

Verdict fixed (2026-09-22, revision 2)

Retell attempt: Two bodies pulling only on each other come down to one body of the reduced mass moving around a fixed total mass. Gravity always points at the centre, so it exerts no torque; the angular momentum is a constant vector, the orbit is flat, and the line to the centre sweeps area at a steady rate. That is Kepler's second law, and nothing about the inverse square went into it. Using the constant angular momentum to remove the angle leaves a particle sliding in an effective potential: a wall at small distance, a well whose bottom is the circular orbit, and turning points where the energy line meets the curve. For the shape rather than the timing you take the angle as the variable and the inverse distance as the unknown, and the inverse-square law makes the equation a harmonic oscillator with a constant on the right, so the answer is a cosine and r = l/(1 + e cos), a conic with the centre of force at a focus. The energy alone fixes the semi-major axis, energy with angular momentum fixes the eccentricity, and the sign of the energy picks ellipse, parabola or hyperbola. Dividing the ellipse's area by the steady areal rate gives the period, the eccentricity cancels, and the mass that appears is the sum of the two. A third constant vector points at the closest approach and holds it still, which is why Kepler orbits close, and Bertrand's theorem says only two laws do that. Finally, a bound orbit's kinetic energy is minus its total energy, so a satellite that loses energy speeds up. What I could not say back: the text told me no other power of the distance gives a conic and then told me the spring also closes its orbits, and I could not hold both. I could not tell whether the dot on r in the first part meant the same thing as the dot on r later. And I could not reconstruct where r plus or minus equals a times one plus or minus e came from.

15 stumbles

- “The Sun sits $ea = 0.1423$ astronomical units”: The symbol $a$ is used in the opening but defined nowhere until the fifth part, and Mars's value for it is never given, so I cannot check any of the opening's numbers.
- “its minor axis falls short of its major axis by $1 - \sqrt{1 - e^2} = 0.44$ per cent”: The equation says the number is 0.44 while the words say 0.44 per cent; they cannot both be right, and I had to reread to decide which.
- “with energy $\tfrac12\mu\dot r^2 - GM\mu/r$”: Here $\dot r$ has to be the whole relative speed, but from the next part on $\dot r$ is the rate of change of the distance alone. One symbol, two meanings. Whose energy it is, and in which frame, is also not said.
- “Both real orbits are copies of the curve $\mathbf r$ traces, scaled by $m_2/M$ and $m_1/M$ about the centre of mass.”: A scaling 'about the centre of mass' does not tell me which side each body is on, and the second body's copy is in fact reflected. I could not draw the picture from this sentence.
- “Two bodies, one fictitious body”: This is the part that teaches the two-body problem, but the phrase 'two-body problem' never appears, so I would not recognise the name later.
- “gets the same constant in one line: ... so $\phi$ is cyclic.”: The promised line is not written. I had to supply the conjugate momentum myself to see where the constant came from.
- “As $r\to\infty$ both vanish, the attraction last, so $U_{\text{eff}}\to0$ from below.”: 'the attraction last' is three words doing the work of a clause; I read the sentence twice.
- “since it still crosses the line to the centre at $h/r$”: 'crosses the line to the centre' sounds like passing through the line, and $h/r$ is a speed with no noun attached. A measurement without its quantity.
- “With $F = -GM\mu u^2$ this reads $-h^2u^2u'' - h^2u^3 = -GMu^2$”: The reduced mass is on the previous line and gone on this one, with no word about it. A step left implicit.
- “Any other power of $r$ leaves a function of $u$ there, and the solution is no longer a conic.”: The first what-if I tried was the spring, which the last part says also closes its orbits, and a spring orbit is an ellipse, which is a conic. The general sentence failed on the section's own example.
- “with $r_\pm = a(1\pm e)$ it is $a^2(1-e^2)$”: This relation is used before anything gives it; the ellipse's geometry only arrives in the next part.
- “This is launch at exactly the escape speed $\sqrt{2GM/r}$”: Whose speed, relative to what, and which mass is $M$? Neither has been said at this point in the part.
- “the angle swept from one perihelion to the next”: The previous part told me perihelion means about the Sun and periapsis is the general word, and this sentence is about a general central field.
- “At perihelion its distance stops falling and starts to rise.”: The check is about a probe orbiting the Earth, so by the section's own rule this should not be called perihelion.
- “such a system therefore has a negative heat capacity”: The section is supposed to teach negative specific heat, but that phrase never appears and neither phrase is in the glossary.

Fixes:
- Opening: named the semi-major axis and gave Mars's value; wrote the flattening as a fraction and then as a percentage.
- Part one: named the two-body problem; wrote the relative energy with $|\dot{\mathbf r}|$, named the frame it is measured in, and scoped $\dot r$ for the rest of the section; gave both bodies' displacements from the centre of mass and said the two stay on opposite sides.
- Part two: wrote the conjugate momentum that the cited earlier section produces.
- Part three: unpacked 'the attraction last'; replaced 'crosses the line to the centre at $h/r$' with the transverse speed named as such.
- Part four: kept $\mu$ in the displayed line and said it cancels; fixed 'in the part time usually plays'.
- Part five: derived $r_\pm = a(1\pm e)$ and $a = l/(1-e^2)$ from the conic formula before using them; named the bound and unbound cases; said the escape-speed comparison is about the relative speed and the total mass.
- Part six: added perigee and apogee; replaced 'the arithmetic of the opening'.
- Parts six and seven and the checks: 'perihelion' now only where the Sun is the centre; 'closest approach' elsewhere.
- Part eight: used 'negative specific heat'.
- Glossary: added two-body problem, bound and unbound orbits, Binet equation, semi-latus rectum, vis-viva equation, Laplace-Runge-Lenz vector and negative specific heat.
- Restored a worked example, a long-period comet, which the writer had dropped for space.

Concerns:
- Part seven still carries two ideas, the Laplace-Runge-Lenz vector and Bertrand's theorem. A joining question now links them, but a future split into two parts would read better.
- Part eight, negative specific heat, is the one part that does not follow from the part before it. It reads well where it is, but it would sit more naturally in a stellar-structure or binary-inspiral section.
- The section says Mercury's perihelion drifts by more than the other planets account for, with no forward pointer, because no perihelion-precession section file exists yet. Add the pointer when it does.

## Review: physics

Verdict fixed (2026-09-22, revision 2)

23 verification items, 9 counterexamples

- Relative equation of motion and the reduced-mass form: Correct: $\ddot{\mathbf r} = -GM\hat{\mathbf r}/r^2$ with $M = m_1+m_2$, and $\mu\ddot{\mathbf r} = -GM\mu\hat{\mathbf r}/r^2$
- The energy written in part one is the energy of the real pair: Equal. But the draft wrote the kinetic term as $\tfrac12\mu\dot r^2$, using $\dot r$ for the full relative speed while every later part uses it for the radial rate. Fixed to $|\dot{\mathbf r}|$, with the frame named.
- Each body's orbit is a scaled copy of the relative orbit: $(m_2/M)\mathbf r$ and $-(m_1/M)\mathbf r$. The draft gave the two scale factors but not the sign, so the second body's copy was left unreflected. Fixed.
- $\dot{\mathbf L} = \mathbf r\times\mathbf F$ and $dA/dt = L/2\mu$: Correct, and correctly attributed to the direction of the force alone
- $U_{\text{eff}}$, its minimum $r_c = h^2/GM$, its value there, and its second derivative: $U_{\text{eff}}(r_c) = -G^2M^2\mu^3/2L^2$ and $U''(r_c) = +GM\mu/r_c^3$, both as written; the minimum is unique and stable
- The barrier term's negative gradient is the centrifugal force of the earlier section: Matches the earlier section's $mv^2/d$ with $v$ transverse; the frame is named
- Binet substitution and the orbit equation: $u'' + u = GM/h^2$ confirmed. The draft dropped $\mu$ silently between two lines; restored and stated.
- 'Any other power of $r$ ... the solution is no longer a conic': FALSE as written: $F = -kr$ gives an ellipse centred on the force, which is a conic. Restated as 'not a conic with the centre of force at a focus', with the spring named as the exception.
- Turning-point quadratic, $E = -GM\mu/2a$, $e^2 = 1 + 2EL^2/G^2M^2\mu^3$, vis-viva: All correct; both roots positive exactly when $E<0$, and the discriminant is non-negative exactly when $e^2\ge0$. The step $r_\pm = a(1\pm e)$ was asserted; now derived from the conic formula.
- Kepler's third law from equal areas: $T = 2\pi\sqrt{a^3/GM}$, eccentricity cancels, $4\pi^2$ and the total mass both correct
- Laplace-Runge-Lenz vector is conserved and gives the conic: $\dot{\mathbf A} = \mathbf 0$; dotting with $\mathbf r$ gives $r = (L^2/GM\mu^2)/(1 + e\cos\psi)$ with $e = A/GM\mu^2$, and $L^2/GM\mu^2 = h^2/GM = l$. Added the explicit length $A = GM\mu^2e$.
- Bertrand's theorem as stated: The draft wrote $F\propto r^{-2}$ and $F\propto r$, which under the section's own convention read as repulsions, and omitted the stable-circular-orbit hypothesis. Rewritten as $F = -k/r^2$ and $F = -kr$ with $k>0$, among central attractions with a stable circular orbit.
- 'a measured drift of perihelion is evidence that the force law is not exactly inverse-square': FALSE without a condition: planetary perturbations move every perihelion under an exact inverse-square law. Scoped to a pair of bodies alone, with the planetary contribution named as calculable.
- $E_{\text{kin}} = -E$ on a circular orbit, and its time-averaged form: Correct; the averaged version is the virial theorem for an inverse-square force and is correctly flagged as taken on trust
- 'a star does not simply cool when its fuel runs out': FALSE without a condition: a core held up by degeneracy has a positive heat capacity and does cool. Scoped to a core held up by ordinary gas pressure.
- Satellite numbers: 7.730 and 7.759 km/s, 29 m/s, 2.256e5 J removed, 4.512e5 J of potential energy, 90.4 to 89.4 minutes: 7729.9 and 7759.0 m/s, $\Delta v = 29.13$ m/s, $\Delta E = 2.2561\times10^5$ J, $\Delta U = -4.5122\times10^5$ J, $T = 90.37$ and $89.36$ min. All as printed.
- Mars numbers in the opening: 0.44 per cent, $ea = 0.1423$ au, 21 million km, 1.381 and 1.666 au: 0.4371 per cent, 0.14231 au, 21.29 million km, 1.3814 and 1.6660 au. All as printed.
- Jupiter is 0.095 per cent of the Sun-plus-Jupiter total: 0.09537 per cent; as printed
- Sirius check: $M = 19.8^3/50.13^2 = 3.09$ solar masses: 3.0889; the stated 3.09 and the 2 per cent tolerance both hold, and 2.1 plus 1.0 recovers it
- Power-2.1 check: apsidal angle $2\pi/\sqrt{3-n}$, 379.5 degrees, 19.5 degrees per orbit: 379.473 degrees, advance 19.473 degrees. Correct, but valid only for a nearly circular orbit; that condition was missing from the answer and is now stated.
- Worked example: comet with $T = 125$ yr and $r_- = 0.900$ au: $a = 25.00$ au, $e = 0.9640$, $r_+ = 49.10$ au, $v_- = 43999$ m/s, $v_+ = 806.5$ m/s; $r_-v_-$ and $r_+v_+$ agree to fifteen digits; $e$ from $1 + 2\varepsilon h^2/(GM)^2$ returns 0.96400; escape speed at $r_-$ is 44400 m/s
- Structure: teaches matches the outline, every concept named, builds_on real, checks and misconceptions link both ways: teaches matches exactly. 'two-body problem', 'unbound' and 'specific heat' were absent from the prose and are now present. All five misconceptions are diagnosed and all four checks' targets exist. builds_on names five real outline sections, four earlier on this track and one reference section.
- No reference needs verifying: Empty, as working depth requires; nothing to search

Fixes:
- 'no longer a conic' corrected to 'not a conic with the centre of force at a focus', with the linear spring named as the exception.
- Bertrand's theorem restated with attractive signs, $k>0$, and the stable-circular-orbit hypothesis.
- The perihelion-drift inference scoped to an isolated pair, with planetary perturbations named.
- The stellar-cooling sentence scoped to a core held up by ordinary gas pressure.
- $\dot r$ disambiguated in part one and scoped for the rest of the section.
- The second body's reflected copy about the centre of mass made explicit.
- $\mu$ kept in the Binet line and its cancellation stated; $r_\pm = a(1\pm e)$ derived rather than asserted.
- The power-2.1 check restricted to a nearly circular orbit, with $\delta$ defined.
- Escape-speed comparison labelled as the relative speed with $M$ the total mass; $A = GM\mu^2e$ stated.
- Added a worked example, a long-period comet, with every number recomputed in python3.

Concerns:
- MISSING CONVENTIONS, unchanged from the writer and still not in notation/course-conventions.md: the orbital symbol set ($\mu$, $M$, $a$, $e$, $l$, $h$, $\phi_0$, $T$, $U_{\text{eff}}$, $\mathbf A$), including a per-section scoping note for $a$ against the scale factor; the clash between $L$ for the Lagrangian and $L$ for angular momentum, scoped inside this section as $\mathcal L$; and the astronomical working form of Kepler's third law, $M/M_\odot = a^3/T^2$ with $a$ in astronomical units and $T$ in years, which two items here rely on. These should be adopted before the next orbit section.
- NO SOURCE NOTES: none of the seventeen concepts has a concept note, so provenance.notes_used is empty. Every derivation, number and check is original and was recomputed here.
- BUDGET: the section now stands at the reviewed cap. To pay for the fixes and the restored worked example I dropped the supporting visual 'equal-areas-and-a-creeping-perihelion', which overlapped 'orbit-with-creeping-perihelion-markers' already proposed in the perihelion-precession note, and did not add a key_equations entry for the Laplace-Runge-Lenz vector, which is still stated, derived and interpreted in part seven.
- The two remaining visuals are proposals, not catalog entries; both carry sketches.
- The writer's suggestion of a fifth check on Mercury's eccentricity was not restored: there is no room, and the existing four already diagnose all five misconceptions.
