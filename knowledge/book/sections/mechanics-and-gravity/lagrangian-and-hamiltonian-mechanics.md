# Lagrangian and Hamiltonian mechanics

`mechanics-and-gravity/lagrangian-and-hamiltonian-mechanics` · main track · working depth · physics-reviewed · revision 2 · 2026-09-22

Teaches: `generalized-coordinates`, `calculus-of-variations`, `fundamental-lemma-calculus-of-variations`, `euler-lagrange-equation`, `lagrangian`, `hamiltons-principle`, `canonical-momentum`, `cyclic-coordinate`, `constant-of-the-motion`, `hamiltonian`, `hamiltons-equations`, `hamilton-jacobi-equation`

Builds on: `units-and-dimensions`, `newtons-laws-and-inertial-frames`, `rotating-frames`, `calculus-refresher`

**Instead of tracking every force, write one function of the coordinates and their rates of change, and add it up along the path. The path the system takes is the one where nudging it, with its two ends held fixed, leaves that total unchanged at first order. One equation per coordinate follows, in whatever coordinates suit the problem, and every coordinate the function leaves out hands back a quantity that never changes. Trading velocities for momenta turns the law into a flow through the states.**

A brass bob hangs on a light rigid rod half a metre long and swings in one vertical plane. Written Newton's way, the bob has two coordinates, $x$ and $y$ measured from the pivot, and three unknowns: $x$, $y$ and the tension $T$ the rod exerts along its length. Two component equations plus the constraint $x^2 + y^2 = \ell^2$ close the system, and $T$ has to be carried through every line and discarded at the end.

Nobody wanted the tension. The rod's only job was to hold the length fixed. This section rebuilds mechanics so that the rod's job is done once, by the choice of coordinate, and the tension never appears. The same rebuilding turns symmetries into conserved quantities, puts a flow on the space of states, and compresses the whole motion into one partial differential equation. Each of those returns in general relativity, where free fall is itself a stationary-action law.

## Coordinates that fit the system

Start by counting. A system's configuration is the list of where all its parts are at one instant, and the number of independent numbers needed to fix that list is its number of degrees of freedom, $n$. The swinging bob needs one, the angle $\theta$ measured from the downward vertical in the plane of the swing. A bead threaded on a fixed wire needs one, the distance along the wire. Two particles held apart by a rigid rod need five. This counting works when every constraint can be written as an equation among the positions, as the rod's can; a constraint that restricts velocities without restricting positions, such as a ball rolling on a table without slipping, needs machinery beyond this section.

Any $n$ independent quantities $q^1, \dots, q^n$ that fix the configuration are called generalized coordinates, written $q^a$ with a Latin index $a$ running from $1$ to $n$. They need not be lengths. An angle, an area, or the charge that has passed a point all serve. Their time derivatives $\dot q^a = dq^a/dt$ are the generalized velocities, and the set of all configurations is the configuration space, in which a motion is a curve $q^a(t)$.

Choosing coordinates that already obey the constraints is the first saving. The rod fixes $x^2 + y^2 = \ell^2$; writing $x = \ell\sin\theta$ and $y = -\ell\cos\theta$ builds that in, so no equation ever needs the tension. When the forces come from a potential energy $V(q)$, as *Newton's laws and inertial frames* defines it, the quantity $Q_a = -\partial V/\partial q^a$ is the generalized force conjugate to $q^a$. Its units are whatever makes the product $Q_a\,\delta q^a$ an energy, so the generalized force conjugate to an angle is a torque, measured in newton metres.

*A system with n degrees of freedom can be described by any n independent generalized coordinates, and choosing ones that already obey the constraints removes the constraint forces before the calculation begins.*

## Wiggling a path with its ends pinned

A rule that swallows a whole function and returns one number is a functional. The length of a curve $y(x)$ between two fixed points, $I[y] = \int_{x_1}^{x_2}\sqrt{1 + y'^2}\,dx$, is one. Finding the function that makes a functional stationary is the calculus of variations.

Take any functional $I[y] = \int_{x_1}^{x_2} F(y, y', x)\,dx$ with the end values $y(x_1)$ and $y(x_2)$ held fixed. Compare a candidate $y$ with the neighbour $y + \epsilon\eta$, where $\epsilon$ is a number and $\eta(x)$ is any bump with a continuous derivative that vanishes at both ends, so the neighbour keeps the same end values. Feeding the neighbour into the functional gives one number for each $\epsilon$; write it $I(\epsilon) = I[y + \epsilon\eta]$, an ordinary function of one variable. The candidate is called stationary when $dI/d\epsilon = 0$ at $\epsilon = 0$ for every such $\eta$. Write $\delta y = \epsilon\eta$ and call it the variation. It is the gap between two rival curves at the same $x$, not anything the system does as $x$ advances, so pinning it at the ends restricts which curves compete and says nothing about slopes there. The first-order change is

$$\delta I = \int_{x_1}^{x_2}\left(\frac{\partial F}{\partial y}\,\delta y + \frac{\partial F}{\partial y'}\,\delta y'\right) dx .$$

The second term still carries a derivative of the variation, so integrate it by parts:

$$\int_{x_1}^{x_2}\frac{\partial F}{\partial y'}\,\delta y'\,dx = \left[\frac{\partial F}{\partial y'}\,\delta y\right]_{x_1}^{x_2} - \int_{x_1}^{x_2}\frac{d}{dx}\!\left(\frac{\partial F}{\partial y'}\right)\delta y\,dx .$$

The bracket vanishes because $\delta y$ vanishes at both ends. That is the entire reason the ends were pinned.

What survives is $\int_{x_1}^{x_2}\phi(x)\,\delta y(x)\,dx = 0$ for every admissible variation, with $\phi = \partial F/\partial y - (d/dx)(\partial F/\partial y')$. The fundamental lemma of the calculus of variations says a continuous $\phi$ with that property is zero everywhere. Its proof traps the function: if $\phi(\xi) > 0$ then, by continuity, $\phi > 0$ on some interval $(\xi_1, \xi_2)$ around $\xi$, and $\delta y = (x - \xi_1)^4(x - \xi_2)^4$ inside that interval, zero outside, has a continuous derivative everywhere and vanishes at both ends, so it is one of the admissible variations, and it makes the integral strictly positive. That contradiction, with signs reversed too, leaves $\phi = 0$ everywhere.

*Pinning the ends lets integration by parts move every derivative off the variation, and the fundamental lemma then converts one vanishing integral into a condition that must hold at every point of the path.*

## The Euler-Lagrange equation

Setting $\phi = 0$ gives the Euler-Lagrange equation,

$$\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right) = \frac{\partial F}{\partial y} ,$$

a second-order ordinary differential equation for $y(x)$, with two constants of integration for the two end values to fix. Fixing them is not the same as starting from a position and a velocity: for some pairs of ends there is more than one stationary curve, and for some there is none. When several functions $y^1(x), \dots, y^n(x)$ are varied, each variation $\delta y^a$ can be chosen independently with the others set to zero, so the lemma applies once per function: there is one Euler-Lagrange equation for each.

Test it on the shortest curve in a plane, $F = \sqrt{1 + y'^2}$. Here $F$ contains no $y$, so the right-hand side is zero and $\partial F/\partial y' = y'/\sqrt{1 + y'^2}$ is constant along the curve. That function of $y'$ is strictly increasing, so $y'$ itself is constant and the curve is a straight line. Whenever $F$ lacks one of the functions $y^a$, the matching derivative $\partial F/\partial y'^a$ keeps the same value all along the solution.

One warning belongs here. Only the first-order change was used, so a solution is stationary; whether it is a minimum, a maximum or a saddle of $I$ is settled by the second-order change, and all three cases occur.

*Requiring an integral to be stationary between fixed ends gives one second-order Euler-Lagrange equation for each function varied, and it finds stationary curves only, not necessarily shortest or smallest ones.*

## The action and Hamilton's principle

Now the physics. For a system whose forces come from a potential energy, define the Lagrangian as kinetic minus potential energy,

$$L(q^a, \dot q^a, t) = T - V ,$$

and define the action of a path as $S[q] = \int_{t_1}^{t_2} L\,dt$. Hamilton's principle states that, among all paths joining a fixed starting configuration at $t_1$ to a fixed finishing configuration at $t_2$, the motion the system actually follows makes $S$ stationary. The time $t$ plays the role of $x$ and the coordinates $q^a$ the role of the $y^a$, so the Euler-Lagrange equations follow without new work.

That this reproduces mechanics is a check, not a definition. For one particle on a line with $L = \tfrac12 m\dot x^2 - V(x)$, the Lagrangian gives $\partial L/\partial \dot x = m\dot x$ and $\partial L/\partial x = -dV/dx$, so the Euler-Lagrange equation reads $m\ddot x = -dV/dx$: Newton's second law with a conservative force. A dimension check in the style of *Units and dimensions*: $L$ is an energy, so $S$ is an energy times a time, measured in joule seconds, the units of angular momentum.

The Lagrangian is not unique. Replace $L$ by $\alpha L + df(q, t)/dt$ with $\alpha$ a nonzero constant and $f$ any function of the coordinates and time. The action becomes $\alpha S + f(q_2, t_2) - f(q_1, t_1)$, and those two extra terms are fixed by the end configurations, which every competing path shares. The change under any pinned variation is therefore $\alpha\,\delta S$, and the stationary paths are exactly the same. So a Lagrangian is a chosen bookkeeping device, not a measurable energy budget.

The traditional name, the principle of least action, overpromises. Stationary is all that is required. For a system that can swing back and forth, a motion lasting long enough makes the true path a saddle of $S$ rather than a minimum; a free particle is the easy case the other way, its straight path having the least action over any duration at all.

*Hamilton's principle says the motion between fixed end configurations makes the action stationary; with kinetic minus potential energy as the Lagrangian it reproduces Newton's second law, and stationary does not mean least.*

## Momenta, missing coordinates and constants

The combination that kept appearing deserves a name. The canonical momentum conjugate to $q^a$ is

$$p_a = \frac{\partial L}{\partial \dot q^a} ,$$

and with it the Euler-Lagrange equation becomes $\dot p_a = \partial L/\partial q^a$. When the kinetic energy does not contain $q^a$ itself, the right-hand side is the generalized force $Q_a = -\partial V/\partial q^a$, so the rate of change of a momentum equals the matching force. When the kinetic energy does contain $q^a$, as $T = \tfrac12 m(\dot r^2 + r^2\dot\varphi^2)$ contains $r$, the right-hand side carries a further term coming from $T$, and that term is not a force.

Canonical momentum need not be mass times velocity. For a particle in a plane in polar coordinates, $L = \tfrac12 m(\dot r^2 + r^2\dot\varphi^2) - V(r)$, so $p_r = m\dot r$ but $p_\varphi = mr^2\dot\varphi$, which is the angular momentum about the centre and is measured in kilogram metre squared per second.

A coordinate that is absent from $L$, although its velocity is present, is called cyclic, or ignorable. Its Euler-Lagrange equation reads $\dot p_a = 0$, so its conjugate momentum keeps the same value along every motion. A quantity with that property is a constant of the motion. The name covers more than this one mechanism: a constant of the motion is any function of the coordinates, the momenta and the time whose total time derivative vanishes along every motion the system can make, and a cyclic coordinate is the cheapest way to find one rather than the only way. In the polar Lagrangian, $\varphi$ is cyclic for any $V(r)$, so $mr^2\dot\varphi$ is constant: the line from the centre to the particle sweeps equal areas in equal times, whatever the central force law. Each constant of the motion is one integration already performed, which is why symmetric problems can be solved at all, and this is the mechanism that reappears for symmetric spacetimes.

*The momentum conjugate to a coordinate is the derivative of the Lagrangian with respect to that coordinate's rate of change, and a coordinate missing from the Lagrangian makes its conjugate momentum a constant of the motion.*

## From velocities to momenta

Momenta turned out to be the quantities that are conserved, so make them the variables. Solve $p_a = \partial L/\partial \dot q^a$ for the velocities, which can be done whenever the matrix $\partial^2 L/\partial\dot q^a\partial\dot q^b$ is invertible, as it is for a kinetic energy $\tfrac12 m_{ab}\dot q^a\dot q^b$ with $m_{ab}$ positive definite. Then define the Hamiltonian by the Legendre transform

$$H(q^a, p_a, t) = p_a\dot q^a - L ,$$

with the velocities everywhere replaced by their expressions in $q$ and $p$. Take the differential of both sides: $dH = \dot q^a dp_a + p_a d\dot q^a - (\partial L/\partial q^a)dq^a - (\partial L/\partial \dot q^a)d\dot q^a - (\partial L/\partial t)dt$. The definition of $p_a$ cancels the two terms in $d\dot q^a$, which is the point of the transform, and the Euler-Lagrange equation replaces $\partial L/\partial q^a$ by $\dot p_a$. Reading off the coefficients gives Hamilton's equations,

$$\dot q^a = \frac{\partial H}{\partial p_a}, \qquad \dot p_a = -\frac{\partial H}{\partial q^a}, \qquad \frac{\partial H}{\partial t} = -\frac{\partial L}{\partial t} .$$

Along a motion, $dH/dt = (\partial H/\partial q^a)\dot q^a + (\partial H/\partial p_a)\dot p_a + \partial H/\partial t$, and the first two terms cancel, leaving $dH/dt = \partial H/\partial t$. So a Lagrangian with no explicit $t$ has a conserved $H$.

Is $H$ the energy? Only under a stated condition. If the recipe giving the positions of the parts in terms of the $q^a$ contains no explicit $t$, so that no constraint is being moved or driven, the kinetic energy takes the form $T = \tfrac12 m_{ab}(q)\dot q^a\dot q^b$, and if $V$ depends on the coordinates alone then $p_a\dot q^a = 2T$, so $H = 2T - (T - V) = T + V$. When a motor or a moving constraint puts $t$ into that recipe, that step fails and $H$, though still conserved, is not $T + V$.

The payoff is structural. Instead of $n$ second-order equations there are $2n$ first-order ones, so a complete state is a single point $(q^a, p_a)$ of the $2n$-dimensional phase space, and one instant fixes the whole future. Hamilton's equations hand each point of phase space one rate of change $(\dot q^a, \dot p_a)$. When $H$ carries no explicit $t$, that rate is the same at every instant, so exactly one trajectory passes through each point and no two trajectories ever cross; a conserved $H$ then confines each of them to one surface of constant $H$.

*Swapping velocities for conjugate momenta turns n second-order equations into 2n first-order ones, so a state is one point of phase space whose motion the Hamiltonian generates; the Hamiltonian equals the energy only when the coordinates carry no explicit time.*

## One function for the whole motion

One boundary term was thrown away along the way, and it pays to pick it up. Fix the starting configuration and the starting time, and let the finishing configuration and the finishing time vary. Define Hamilton's principal function $S(q^a, t)$ as the action along the actual motion that leaves that start and arrives at configuration $q^a$ at time $t$, for those ends that exactly one motion reaches. Repeat the variation with the far end free. The integral vanishes because the motion satisfies the Euler-Lagrange equations, and only the bracket survives, which gives $\partial S/\partial q^a = p_a$. The time derivative takes one more line. Let the finish travel along the motion itself, so that $q^a$ and $t$ advance together; then $S$ grows at the rate $dS/dt = L$, because that is what the action integral is accumulating. The chain rule writes the same rate as $\partial S/\partial t + (\partial S/\partial q^a)\dot q^a = \partial S/\partial t + p_a\dot q^a$, so $\partial S/\partial t = L - p_a\dot q^a = -H$.

Substituting the first into the second removes the momenta and leaves one equation for one function,

$$\frac{\partial S}{\partial t} + H\!\left(q^a, \frac{\partial S}{\partial q^a}, t\right) = 0 ,$$

the Hamilton-Jacobi equation. It is a first-order partial differential equation, and it carries the whole of mechanics: a solution $S(q^a, t; \alpha_1, \dots, \alpha_n)$ carrying $n$ independent constants, over and above the additive constant every solution allows, yields every trajectory by differentiation. Setting each $\partial S/\partial\alpha_b$ equal to a constant gives $n$ equations tying the $q^a$ to $t$, with no equation of motion integrated.

A single free particle shows the machinery. With $H = p^2/2m$, the function $S = m(q - q_0)^2/2(t - t_0)$ gives $\partial S/\partial q = m(q - q_0)/(t - t_0) = p$ and $\partial S/\partial t = -m(q - q_0)^2/2(t - t_0)^2 = -p^2/2m$, so the equation is satisfied. That $S$ is indeed the action of the straight path covering $q - q_0$ in time $t - t_0$.

The shape of the equation is why it matters later. Surfaces of constant $S$ sweep through configuration space like wavefronts, with the momentum as the gradient of $S$, so trajectories cross them the way rays cross wavefronts. The same equation, with the Hamiltonian of a free particle in a curved spacetime, joins a wave picture of motion to a particle picture.

*Letting the action depend on where and when the motion ends turns mechanics into a single first-order partial differential equation whose level surfaces advance like wavefronts and whose gradient is the momentum.*

## Key equations

**The action of a path** (stated)

$$S[q] = \int_{t_1}^{t_2} L(q^a, \dot q^a, t)\, dt, \qquad L = T - V$$

Every path between two fixed configurations gets a number, the action, in joule seconds.

- $S$: action of the path
- $L$: Lagrangian, kinetic minus potential energy

Say: The action of a path is the integral of the Lagrangian with respect to time, from the start time to the finish time, and the Lagrangian is kinetic energy minus potential energy.

**Euler-Lagrange equation** (derived-here)

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q^a}\right) = \frac{\partial L}{\partial q^a}$$

One second-order equation per coordinate, holding for any independent choice of coordinates. For $L = \tfrac12 m\dot x^2 - V(x)$ it is Newton's second law.

- $\partial L/\partial \dot q^a$: derivative of the Lagrangian with respect to a velocity, at fixed coordinates

Say: The time derivative of the partial derivative of L with respect to the velocity equals the partial derivative of L with respect to the coordinate.

**Canonical momentum** (stated)

$$p_a = \frac{\partial L}{\partial \dot q^a}$$

Mass times velocity for a free particle in Cartesian coordinates, and the angular momentum $mr^2\dot\varphi$ for a polar angle.

- $p_a$: canonical momentum conjugate to the coordinate

Say: The canonical momentum is the partial derivative of the Lagrangian with respect to the matching velocity.

**The Hamiltonian and Hamilton's equations** (derived-here)

$$H = p_a\dot q^a - L, \qquad \dot q^a = \frac{\partial H}{\partial p_a}, \qquad \dot p_a = -\frac{\partial H}{\partial q^a}$$

The Legendre transform trades velocities for momenta, replacing $n$ second-order equations by $2n$ first-order ones. $H$ is conserved when $L$ has no explicit time dependence, and equals $T + V$ when the coordinates also carry no explicit time.

- $H$: Hamiltonian, a function of coordinates, momenta and time
- $p_a\dot q^a$: sum over all coordinates of momentum times velocity

Say: H equals the sum of momentum times velocity, minus the Lagrangian. Each velocity is the partial derivative of H with respect to the matching momentum, and the rate of change of each momentum is minus the partial derivative of H with respect to the matching coordinate.

**Hamilton-Jacobi equation** (derived-here)

$$\frac{\partial S}{\partial t} + H\!\left(q^a, \frac{\partial S}{\partial q^a}, t\right) = 0$$

One first-order partial differential equation for $S(q^a, t)$, the action of the actual motion reaching $q^a$ at time $t$, whose momenta are $p_a = \partial S/\partial q^a$.

- $S(q^a, t)$: Hamilton's principal function, the action as a function of the finishing configuration and time

Say: The partial derivative of S with respect to time, plus the Hamiltonian with the momenta replaced by the partial derivatives of S with respect to the coordinates, equals zero.

## Worked examples

**the-pendulum-in-one-coordinate.** A bob of mass $m$ hangs on a light rigid rod of length $\ell = 0.50\ \text{m}$ and swings in a vertical plane. Using the angle $\theta$ from the downward vertical, find the equation of motion, the canonical momentum, the Hamiltonian, and the period of small swings with $g = 9.81\ \text{m}\,\text{s}^{-2}$.

1. The bob's position is $x = \ell\sin\theta$, $y = -\ell\cos\theta$ with $y$ measured upward from the pivot, so its speed is $\ell|\dot\theta|$ and $T = \tfrac12 m\ell^2\dot\theta^2$.
2. Taking the potential energy as zero at the pivot, $V = mgy = -mg\ell\cos\theta$, so $L = \tfrac12 m\ell^2\dot\theta^2 + mg\ell\cos\theta$.
3. Differentiate: $\partial L/\partial\dot\theta = m\ell^2\dot\theta$, which is the canonical momentum $p_\theta$, and $\partial L/\partial\theta = -mg\ell\sin\theta$.
4. The Euler-Lagrange equation is $m\ell^2\ddot\theta = -mg\ell\sin\theta$, that is $\ddot\theta = -(g/\ell)\sin\theta$. The mass cancels and the rod tension never appeared.
5. The kinetic energy is a homogeneous quadratic in $\dot\theta$ and the coordinate carries no explicit time, so $H = p_\theta^2/2m\ell^2 - mg\ell\cos\theta = T + V$; and $L$ has no explicit $t$, so $H$ is conserved.
6. For small swings $\sin\theta \approx \theta$, giving $\ddot\theta = -\omega^2\theta$ with $\omega = \sqrt{g/\ell} = \sqrt{9.81/0.50} = 4.429\ \text{rad}\,\text{s}^{-1}$, so the period is $2\pi/\omega = 1.4185\ \text{s}$.

Answer: $\ddot\theta = -(g/\ell)\sin\theta$, with $p_\theta = m\ell^2\dot\theta$ and $H = p_\theta^2/2m\ell^2 - mg\ell\cos\theta$ conserved and equal to $T + V$. Small swings have $\omega = 4.429\ \text{rad}\,\text{s}^{-1}$ and a period of $1.4185\ \text{s}$.

*One coordinate chosen to obey the constraint gives the whole motion in four lines, and the constraint force is never computed.*

## Checks

**free-particle-in-polar-coordinates** (derive): A free particle moves in a plane with no forces. Write its Lagrangian in polar coordinates $(r, \varphi)$, obtain both Euler-Lagrange equations, and show that they describe the same straight-line motion as $\ddot x = \ddot y = 0$. Why does this work when the polar equations look nothing like Newton's?

Answer: With $x = r\cos\varphi$ and $y = r\sin\varphi$ the speed squared is $\dot r^2 + r^2\dot\varphi^2$, so $L = \tfrac12 m(\dot r^2 + r^2\dot\varphi^2)$ and $V = 0$. For $r$: $\partial L/\partial\dot r = m\dot r$ and $\partial L/\partial r = mr\dot\varphi^2$, giving $\ddot r = r\dot\varphi^2$. For $\varphi$: the coordinate is absent from $L$, so $p_\varphi = mr^2\dot\varphi$ is constant. Writing $p_\varphi = mh$ and eliminating $\dot\varphi$ gives $\ddot r = h^2/r^3$, solved by $r(t)^2 = b^2 + h^2t^2/b^2$ for a constant $b$, which is the polar description of a straight line passing at distance $b$ from the origin. It works because the derivation assumed nothing about the coordinates except that they are independent. The $r\dot\varphi^2$ term is not a new force; it is what the second derivative of position becomes in these coordinates.

Key points: The Lagrangian is one half m times r dot squared plus r squared phi dot squared, with no potential; The angle is absent, so its conjugate momentum m r squared phi dot is constant; The radial equation gives straight-line motion written in polar form; The derivation assumed only independent coordinates, so its form holds in every coordinate system

**angular-momentum-of-the-earths-orbit** (numeric): Earth moves on a near-circular orbit of radius $r = 1.496\times 10^{11}\ \text{m}$ about the Sun, of mass $M = 1.989\times 10^{30}\ \text{kg}$, with $G = 6.674\times 10^{-11}\ \text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}$. Take $L = \tfrac12 m(\dot r^2 + r^2\dot\varphi^2) + GMm/r$. Which coordinate is cyclic, and what does its conjugate momentum equal? Using the radial equation for a circular orbit, find the orbital speed in kilometres per second and the period in years.

Answer: The angle $\varphi$ is cyclic, so $p_\varphi = mr^2\dot\varphi$ is a constant of the motion: the orbital angular momentum, not mass times speed. The radial equation is $m\ddot r = mr\dot\varphi^2 - GMm/r^2$; a circular orbit has $\ddot r = 0$, so $r\dot\varphi^2 = GM/r^2$ and the speed $v = r\dot\varphi$ satisfies $v^2 = GM/r$. Then $v = 2.979\times 10^{4}\ \text{m}\,\text{s}^{-1}$, that is $29.79\ \text{km}\,\text{s}^{-1}$, and the period $2\pi r/v$ is $3.155\times 10^{7}\ \text{s}$, which is $1.000$ year.

Key points: The angle is cyclic, so its conjugate momentum is the angular momentum m r squared phi dot; Setting the radial acceleration to zero gives v squared equals G M over r; The speed is about 29.8 kilometres per second and the period 1.00 year

Numeric: orbital speed = 29.79 km/s; orbital period = 1.0 yr

**when-the-action-stops-being-least** (derive): For small swings the pendulum of length $\ell = 0.50\ \text{m}$ has $L = \tfrac12 m\ell^2(\dot\theta^2 - \omega^2\theta^2)$ with $\omega = \sqrt{g/\ell}$. For a motion lasting a time $\tau$, add the pinned variation $\delta\theta = \varepsilon\sin(\pi t/\tau)$ and compute the change in the action. For which $\tau$ is the true path a minimum, and for which a saddle? Give the changeover time in seconds.

Answer: Because $L$ is quadratic in $\theta$ and $\dot\theta$, the change in the action has only a piece linear in the variation and a piece quadratic in it; the linear piece vanishes because the true path obeys the Euler-Lagrange equation, so the exact change is $\Delta S = \tfrac12 m\ell^2\int_0^\tau(\delta\dot\theta^2 - \omega^2\delta\theta^2)\,dt$. With $\delta\theta = \varepsilon\sin(\pi t/\tau)$ each integral contributes $\varepsilon^2\tau/2$ times its coefficient, so $\Delta S = \tfrac14 m\ell^2\varepsilon^2\tau\,[(\pi/\tau)^2 - \omega^2]$, positive for $\tau < \pi/\omega$ and negative for $\tau > \pi/\omega$. Any pinned variation is a sum of terms $\sin(n\pi t/\tau)$, each contributing $(n\pi/\tau)^2 - \omega^2$, so below the changeover every term raises the action and the true path is a genuine minimum, while above it the first term lowers the action and higher ones raise it, making the path a saddle. With $\omega = 4.429\ \text{rad}\,\text{s}^{-1}$ the changeover is $\tau = \pi/\omega = 0.7093\ \text{s}$, half the period of the swing.

Key points: The change in the action is one quarter m ell squared epsilon squared tau, times pi over tau all squared minus omega squared; The sign flips when the duration passes pi over omega, which is half the period; Below the changeover every sine variation raises the action; above it one lowers it, making a saddle; The changeover time is 0.709 seconds for a pendulum half a metre long

Numeric: changeover duration = 0.7093 s

**hoop-turned-by-a-motor** (derive): A motor turns a hoop of radius $a = 0.20\ \text{m}$ about its vertical diameter at a fixed $\omega = 12\ \text{rad}\,\text{s}^{-1}$, and a bead of mass $m = 0.010\ \text{kg}$ slides on it without friction. With $\theta$ measured from the lowest point, write $L$, find $p_\theta$ and $H$, say which of $H$ and $T + V$ is conserved and which is the bead's energy, and give $H - (T + V)$ at $\theta = 60^\circ$.

Answer: The bead moves along the hoop at speed $a|\dot\theta|$ and is carried around the axis on a circle of radius $a\sin\theta$ at speed $a\omega\sin\theta$; these are perpendicular, so $T = \tfrac12 m a^2(\dot\theta^2 + \omega^2\sin^2\theta)$ and $V = -mga\cos\theta$. Then $p_\theta = \partial L/\partial\dot\theta = m a^2\dot\theta$ and $H = p_\theta\dot\theta - L = \tfrac12 m a^2\dot\theta^2 - \tfrac12 m a^2\omega^2\sin^2\theta - mga\cos\theta$: the $\omega$ term carries no $\dot\theta$, so the transform treats it like a potential energy and flips its sign. $L$ has no explicit $t$, so $dH/dt = \partial H/\partial t = 0$ and $H$ is conserved. $T + V$ is the bead's energy and is not conserved, because the motor supplies or absorbs work through the constraint to hold the rate fixed. The difference is $H - (T + V) = -m a^2\omega^2\sin^2\theta$, which at $\theta = 60^\circ$ is $-0.0432\ \text{J}$. Seen from the frame turning with the hoop, $-\tfrac12 m a^2\omega^2\sin^2\theta$ is the potential energy of the centrifugal force of *Rotating frames*, so $H$ is the energy a rider turning with the hoop writes down.

Key points: H is conserved because the Lagrangian has no explicit time dependence; T plus V is the energy and is not conserved, because the motor works through the constraint; The difference is minus m a squared omega squared sine squared theta, which is minus 0.0432 joules at sixty degrees; H is the energy written down in the frame turning with the hoop, with the centrifugal potential energy included

Numeric: H minus the total energy = -0.0432 J

## Misconceptions

- **stationary-means-least**: "The true path always gives the least action, as the name principle of least action says." — Hamilton's principle requires only that the first-order change vanish. A pendulum path minimises the action only over durations shorter than half a swing period. (diagnosed by when-the-action-stops-being-least)
- **canonical-momentum-is-mass-times-velocity**: "Canonical momentum is just another name for mass times velocity." — Canonical momentum is the derivative of the chosen Lagrangian with respect to a generalized velocity. Conjugate to a polar angle it is an angular momentum. (diagnosed by angular-momentum-of-the-earths-orbit)
- **the-hamiltonian-is-always-the-energy**: "The Hamiltonian is the total energy, so whenever it is conserved the energy is conserved." — The Hamiltonian equals kinetic plus potential energy only when the coordinates carry no explicit time and the potential does not depend on velocities. A bead on a hoop turned by a motor has a conserved Hamiltonian and a changing energy. (diagnosed by hoop-turned-by-a-motor)
- **only-cartesian-coordinates-work**: "Because Newton's second law is written in Cartesian components, equations of motion must be derived there and then converted." — The derivation assumes only that the coordinates are independent, so the equations keep their form in any of them. Terms that look like extra forces are what the acceleration becomes there. (diagnosed by free-particle-in-polar-coordinates)

## Glossary

- **generalized coordinates**: Any independent set of quantities, one per degree of freedom, that fixes a configuration. They need not be lengths. (`generalized-coordinates`)
- **degrees of freedom**: The number of independent quantities needed to fix where every part of a system is at one instant. (`generalized-coordinates`)
- **generalized velocity**: The time derivative of a generalized coordinate. (`generalized-coordinates`)
- **configuration space**: The space whose points are all the configurations the system can take; a motion is a curve in it. (`generalized-coordinates`)
- **generalized force**: The quantity conjugate to a coordinate whose product with a small change of that coordinate is an energy. For forces from a potential energy it is minus the derivative of that energy with respect to the coordinate. (`generalized-coordinates`)
- **functional**: A rule that takes a whole function and returns one number. (`calculus-of-variations`)
- **stationary**: Said of a path at which the first-order change of a functional vanishes for every allowed variation. It may be a minimum, a maximum or a saddle. (`calculus-of-variations`)
- **variation**: The gap, at each instant, between a competing path and the path being tested. Not a change the system undergoes in time. (`calculus-of-variations`)
- **fundamental lemma of the calculus of variations**: A continuous function that integrates to zero against every smooth bump vanishing at the ends is zero everywhere. (`fundamental-lemma-calculus-of-variations`)
- **Euler-Lagrange equation**: The equation a path must satisfy to make an integral stationary, one per function varied. (`euler-lagrange-equation`)
- **Lagrangian**: The function of coordinates, velocities and time whose time integral is the action; kinetic minus potential energy. (`lagrangian`)
- **action**: The integral of the Lagrangian along a path, measured in joule seconds. (`hamiltons-principle`)
- **Hamilton's principle**: The law that the motion between fixed start and finish configurations makes the action stationary. (`hamiltons-principle`)
- **canonical momentum**: The derivative of the Lagrangian with respect to a generalized velocity. (`canonical-momentum`)
- **cyclic coordinate**: A coordinate absent from the Lagrangian although its velocity is present. Also called ignorable. (`cyclic-coordinate`)
- **constant of the motion**: A quantity that keeps the same value all along every motion of the system. (`constant-of-the-motion`)
- **Hamiltonian**: The Legendre transform of the Lagrangian, in coordinates and momenta: momentum times velocity summed over coordinates, minus the Lagrangian. (`hamiltonian`)
- **phase space**: The space whose points are all coordinates paired with all conjugate momenta. One point fixes the entire future. (`hamiltons-equations`)
- **Hamilton's principal function**: The action of the actual motion reaching a given configuration at a given time, as a function of both. (`hamilton-jacobi-equation`)

## Visuals

- `wiggle-a-path-with-pinned-ends` (flagship): The central picture: trial paths between two pinned events, each carrying its action, and the parabola of action against variation size that flips over when the motion lasts too long. Sketch: A position-against-time panel with the start and finish pinned as dots, the true path solid, and a competing path the learner shapes by dragging a bump. A slider sets the variation size and a side plot shows the action against it, a parabola with its vertex at zero. Presets: free particle, opening upward; harmonic oscillator with a duration slider, opening upward below half a period and downward above, the changeover marked at 0.709 seconds for a pendulum half a metre long; and a two-bump saddle mode. Competing paths drag only between the pinned ends, so a path with moved ends never appears as a test.
- `phase-portrait-of-a-pendulum` (core): Phase space made an instrument: the pendulum's state as one point, its flow generated by the Hamiltonian, and the curves of constant Hamiltonian it must stay on. Sketch: The plane with the angle across and the conjugate momentum up, carrying the arrow field of Hamilton's equations and the level curves of $H$. A dropped state point runs along one level curve while a second panel shows the bob in step. Presets: small swings as nested ovals, the separatrix through the upside-down position, and going over the top as open curves. A test: two state points never meet, because one point fixes the whole motion.

## Tutor

Opening question: Picture a bob on a light rigid rod, swinging in one plane. Written Newton's way you carry three unknowns: two position components and the tension in the rod, which you never wanted. If you instead describe the bob by the single angle it makes with the downward vertical, what happens to the tension, and what would you then need in order to predict the motion?

- Q: Where does kinetic minus potential energy come from? It looks invented. A: It is invented, in the sense that it is a postulate rather than a derivation. What justifies it is that its Euler-Lagrange equation is Newton's second law with a conservative force, for every system where we already know the answer. The reason to prefer it is what it buys: the same equation in any coordinates, a conserved quantity for every missing coordinate, and a form that carries over to fields and to curved spacetime.
- Q: Is the action really least along the true path? A: Only sometimes. For a swinging pendulum half a metre long, the true path really is the least action path if the journey lasts less than about seven tenths of a second, which is half the swing period. Longer than that and you can find a wiggle that lowers the action, so the true path is a saddle. Stationary is the honest statement.
- Q: How do I know which generalized coordinates to choose? A: Count first. Work out how many independent numbers it takes to say where every part of the system is, and that is how many coordinates you need. Then pick quantities that already respect whatever holds the system together, like the angle of a pendulum rather than its two position components, because every constraint you build into the coordinates is a constraint force you never have to compute. After that, look for a coordinate that the Lagrangian does not contain at all, because each one of those hands you a conserved momentum for free.
- Q: Why does the principle fix where the motion ends? Nature does not know where it will end up. A: The principle is not a rule the system follows as it goes. It is a way of picking one curve out of a family of curves that all join the same two configurations, and the ends are held fixed so that the comparison is a fair one and so that the boundary term from the integration by parts drops out. What comes out of it is an ordinary equation of motion: give it a position and a velocity now, and it marches forward one instant at a time, with no knowledge of where it will end up.

## Review: novice

Verdict fixed (2026-09-22, revision 2)

Retell attempt: Instead of writing out F = ma for every piece and dragging the constraint forces along, you count the degrees of freedom, pick that many independent coordinates, and pick them so the constraints are already built in; then the rod's tension never appears. You form L = T - V, integrate it over time to get the action, and demand that the action be stationary among paths that join the same two configurations. Wiggle the path, the first-order change has a dF/dy piece and a dF/dy' piece, integrate the second by parts, the boundary term dies because the wiggle is pinned at the ends, and the fundamental lemma turns the one vanishing integral into an equation at every point: one Euler-Lagrange equation per coordinate. For L = half m x-dot squared minus V it is Newton's second law, which is the check that the postulate was worth making. The derivative of L with respect to a velocity is the canonical momentum; for a polar angle it is m r squared phi-dot, an angular momentum, not mass times velocity. A coordinate missing from L is cyclic and its momentum never changes, which is where equal areas in equal times comes from. Then trade velocities for momenta: H = p q-dot minus L, and n second-order equations become 2n first-order ones, so a state is one point of phase space. H is conserved whenever L has no explicit time in it, but H is the energy only when nothing is driving the system: the bead on the motor-driven hoop has a conserved H and a changing energy. Finally let the finishing end of the action vary, so dS/dq = p and dS/dt = -H, and those combine into the Hamilton-Jacobi equation, one first-order partial differential equation whose level surfaces move like wavefronts. What I could not say back after one reading: why the changeover from minimum to saddle sits at half a period rather than anywhere else; whether a constant of the motion can be anything besides a cyclic coordinate's momentum; how a Hamilton-Jacobi solution actually hands me a trajectory; why the momentum index is written downstairs; and what class of wiggles the fundamental lemma is quantified over. The takeaways cover all of the first list except the last two, which is where most of the fixes went.

20 stumbles

- “Instead of tracking every force, write one function of the coordinates and their rates of change, and demand that its integral along the path be stationary.”: The summary is the first thing the tutor speaks, and it leans on the word stationary with no hint of what it means, and without the one condition that gives it content, that the two ends of the path are held fixed. Nudged how, and holding what?
- “the bob has two coordinates, $x$ and $y$, and three unknowns”: A measurement without its reference. The constraint $x^2 + y^2 = \ell^2$ in the next sentence is only true if $x$ and $y$ are measured from the pivot, and nothing says so.
- “the quantity $F_a = -\partial V/\partial q^a$ is the generalized force conjugate to $q^a$”: One symbol with two meanings: the very next part writes every functional as $\int F(y, y', x)\,dx$, so $F$ is the generalized force and the integrand at once.
- “Two particles held apart by a rigid rod need five.”: The counting rule is stated as if it always worked; nothing says which kinds of constraint it covers, and a reader who thinks of a rolling ball gets the wrong number.
- “The number $I(\epsilon)$ is then an ordinary function of one variable”: $I$ was introduced with square brackets as a rule that eats a function. $I(\epsilon)$ with round brackets is a different object that is never defined; I had to reread to see it meant the functional evaluated on the neighbour.
- “where $\eta(x)$ is any smooth bump that vanishes at both ends ... $\delta y = (x - \xi_1)^4(x - \xi_2)^4$ inside that interval, zero outside, is smooth”: A rule I could not follow, and it is also false. Extended by zero, that quartic product has three continuous derivatives, not infinitely many, so it is not smooth in the sense a reader who has met the word will take. The class of competing variations is never actually stated, so I could not tell whether the bump qualified.
- “whose two free constants are fixed by the two end values”: A general sentence that fails the section's own what-if. Three parts later the same section shows the pendulum's ends failing to pick out one curve once the motion lasts half a period.
- “Whenever $F$ lacks one of the functions, the matching derivative $\partial F/\partial y'$ is a constant of integration.”: The paragraph has just introduced several functions $y^a$, and this sentence drops back to an unindexed $y'$, so I could not tell which derivative is meant. 'Constant of integration' also names the thing by where it came from rather than by what it does.
- “over long enough stretches of time the true path is a saddle of $S$ rather than a minimum”: The first what-if breaks it. A free particle's straight path has the least action over any duration whatever, so the sentence is not true of every system.
- “$\dot p_a = \partial L/\partial q^a$: the rate of change of a momentum equals the matching generalized force”: One word for two ideas, and it contradicts two other places in the section. Part one defined the generalized force as $-\partial V/\partial q^a$, and the polar check warns that the $mr\dot\varphi^2$ in $\partial L/\partial r$ is not a force at all.
- “the radius sweeps equal areas in equal times”: A radius is a length; a length does not sweep an area. The thing that sweeps is the line joining the centre to the particle.
- “A quantity with that property is a constant of the motion.”: A term defined by one example only. After this I could not say whether anything other than a cyclic coordinate's momentum counts, and the section never tells me.
- “Solve $p_a = \partial L/\partial \dot q^a$ for the velocities”: An instruction I cannot always carry out, with nothing said about when it can be carried out. The whole of Hamiltonian mechanics is built on this one step.
- “If the coordinates carry no explicit time”: Coordinates are numbers; they cannot carry a time. The condition is about the recipe tying them to actual positions, and until the motor appeared two sentences later I read this as a condition on $L$, which it is not.
- “Exactly one trajectory passes through each point”: A universal sentence in a paragraph that has just allowed $H(q^a, p_a, t)$. With an explicit $t$ in $H$, two motions can pass through the same phase point at different times and go different ways, so phase-space paths do cross.
- “Fix the starting event and let the finishing point vary.”: An undefined word and an ambiguous one in the same sentence. No earlier section on this track gives me 'event', and 'finishing point' could be a point of the path, of configuration space, or of time.
- “only the bracket survives, giving $\partial S/\partial q^a = p_a$ and $\partial S/\partial t = -H$”: A step left implicit. The bracket from the integration by parts contains $p_a\,\delta q^a$ and nothing else, so it can give the first result but cannot give the second, and I could not see where the $-H$ came from.
- “a solution containing $n$ free constants yields every trajectory by differentiation, without integrating any equation of motion”: A surprising claim with no test I could try. Which constants, and differentiate with respect to what? Every solution also carries an additive constant, which is free and yields nothing.
- “Because $L$ is quadratic, the exact change is $\Delta S = \tfrac12 m\ell^2\int_0^\tau(\delta\dot\theta^2 - \omega^2\delta\theta^2)\,dt$.”: A step left implicit in a check I am meant to be graded on. Quadratic $L$ gives a linear piece as well as this quadratic one, and nothing says why the linear piece is absent.
- “degrees of freedom, generalized velocity, configuration space, generalized force, functional, stationary”: Six technical terms introduced in the prose and used through the whole section, none of them in the glossary, so the tutor has nowhere to look them up when a learner asks.

Fixes:
- Summary rewritten so the word stationary arrives with its condition, that both ends of the path are held fixed, and with what unchanged means.
- Opening: $x$ and $y$ given their origin at the pivot, so the constraint quoted in the same sentence is true.
- Generalized force renamed $Q_a$ throughout, freeing $F$ for the integrand of a general functional.
- Admissible variations defined once, as bumps with a continuous derivative vanishing at both ends, and the lemma's test bump described by what it actually is.
- Euler-Lagrange paragraph: the two end values no longer promised to fix a unique curve; the first-integral sentence given its index.
- 'The matching generalized force' replaced by the two cases that $\partial L/\partial q^a$ really splits into.
- Constant of the motion given its general definition, so the term is not left equal to the one mechanism that produced it.
- Legendre transform and the $H = T + V$ condition given the hypotheses a reader has to be able to test.
- Hamilton-Jacobi part: 'event' replaced, and the missing line that produces $\partial S/\partial t = -H$ written out.
- Six glossary entries restored (degrees of freedom, generalized velocity, configuration space, generalized force, functional, stationary) and two tutor questions added, on choosing coordinates and on why the ends are pinned.
- The 10% review allowance was used for these additions: total went from 4388 to about 5250 words against a 5500 cap. Nothing was compressed and nothing was dropped.

Concerns:
- hamilton-jacobi-equation gets one part, one equation and no check, while every other concept gets a check or a worked example. A learner who is asked about it after one reading can quote the equation and not use it.
- builds_on names 'calculus-refresher', which the outline has but the book does not yet contain. The section leans on partial derivatives, integration by parts and second-order linear ODEs from it.

## Review: physics

Verdict fixed (2026-09-22, revision 2)

16 verification items, 8 counterexamples

- Pendulum small-swing rate and period, $\ell = 0.50$ m, $g = 9.81$ m/s^2.: $\omega = 4.42945$ rad/s and $T = 1.41850$ s; the section's 4.429 and 1.4185 are right.
- Pendulum Lagrangian, momentum and Hamiltonian in the worked example.: $L = \tfrac12 m\ell^2\dot\theta^2 + mg\ell\cos\theta$, $p_\theta = m\ell^2\dot\theta$, $H = p_\theta^2/2m\ell^2 - mg\ell\cos\theta$, $\ddot\theta = -(g/\ell)\sin\theta$. All as written, signs included.
- Earth's orbital speed and period from the radial equation.: $v = 29.788$ km/s and $P = 3.1555\times10^{7}$ s = 0.99991 yr. The stated 29.79 km/s and 1.000 yr are inside the 1% tolerances.
- Radial Euler-Lagrange equation for $L = \tfrac12 m(\dot r^2 + r^2\dot\varphi^2) + GMm/r$.: $m\ddot r = mr\dot\varphi^2 - GMm/r^2$, matching the check; the circular case gives $v^2 = GM/r$.
- The free-particle polar solution $r(t)^2 = b^2 + h^2t^2/b^2$ solves $\ddot r = h^2/r^3$.: Equals $h^2/r^3$ exactly, and $h = bv$ identifies $b$ as the perpendicular distance from the origin. Correct.
- Second variation of the harmonic action with $\delta\theta = \varepsilon\sin(\pi t/\tau)$.: $\Delta S = \tfrac14 m\ell^2\varepsilon^2\tau[(\pi/\tau)^2 - \omega^2]$, as written. The Fourier argument is sound: the modes $\sin(n\pi t/\tau)$ are orthogonal on $[0,\tau]$ with orthogonal derivatives, so there are no cross terms.
- Changeover duration is half the swing period.: Both 0.709252 s; the stated 0.7093 s and 'half the period' are right.
- Bead on the motor-driven hoop: $T$, $V$, $p_\theta$, $H$ and $H - (T+V)$.: $H = \tfrac12 ma^2\dot\theta^2 - \tfrac12 ma^2\omega^2\sin^2\theta - mga\cos\theta$ and $H - (T+V) = -ma^2\omega^2\sin^2\theta$, which at $60^\circ$ is $-0.04320$ J. Sign and magnitude as stated.
- That same $H$ is the energy in the frame turning with the hoop.: Exactly $H$. Added to the check, which also gives *Rotating frames* the use its place in builds_on promises.
- Hamilton's equations and their signs against the Legendre transform.: $\dot q^a = \partial H/\partial p_a$, $\dot p_a = -\partial H/\partial q^a$, $\partial H/\partial t = -\partial L/\partial t$; and $(\partial H/\partial q^a)\dot q^a + (\partial H/\partial p_a)\dot p_a = -\dot p_a\dot q^a + \dot q^a\dot p_a = 0$, so $dH/dt = \partial H/\partial t$. All correct as printed.
- $p_a\dot q^a = 2T$ for $T = \tfrac12 m_{ab}(q)\dot q^a\dot q^b$.: Holds, so $H = T + V$ under the two stated hypotheses. Both hypotheses are now printed.
- Free-particle solution of the Hamilton-Jacobi equation.: $\partial S/\partial q = m(q-q_0)/(t-t_0)$, $\partial S/\partial t = -m(q-q_0)^2/2(t-t_0)^2 = -p^2/2m$, so $\partial S/\partial t + H = 0$; and $\int\tfrac12 mv^2dt = \tfrac12 m(q-q_0)^2/(t-t_0)$, the same $S$. Correct.
- Action carries the units of angular momentum.: Correct as stated; joule seconds and kilogram metre squared per second are the same kind.
- Every concept in the outline's list is introduced by name in some part.: All twelve appear by name. hamilton-jacobi-equation gets one part only, which is noted as a concern rather than an error.
- Checks and misconceptions link both ways.: Four checks, four misconceptions, each pair linked in both directions.
- Nothing in the section names, cites or quotes a source book.: Nothing does. provenance.source_units is internal.

Fixes:
- Scoped the degrees-of-freedom count to constraints expressible among the positions.
- Renamed the generalized force $Q_a$ to end the collision with the functional integrand $F$.
- Stated the class of admissible variations and corrected the description of the lemma's test bump, which is three times continuously differentiable and not smooth.
- Scoped the claim that two end values fix the two constants of the Euler-Lagrange equation.
- Scoped the saddle claim to systems that can swing, and named the free particle as the standing counterexample.
- Replaced 'the rate of change of a momentum equals the matching generalized force' by the two cases $\partial L/\partial q^a$ actually splits into, which also removes a contradiction with the polar check.
- Added the general definition of a constant of the motion.
- Printed the invertibility condition on $\partial^2 L/\partial\dot q^a\partial\dot q^b$ that the Legendre transform needs.
- Restated the $H = T + V$ hypothesis as a condition on the recipe relating the $q^a$ to the positions, which is what it is.
- Scoped the no-crossing claim in phase space to a Hamiltonian without explicit time.
- Supplied the missing line that yields $\partial S/\partial t = -H$, and made the complete-solution statement precise ($n$ independent constants beyond the additive one, trajectories from $\partial S/\partial\alpha_b$).
- Said why the linear piece of the action change vanishes in the least-action check.
- Added to the hoop check that $H$ is the energy in the frame turning with the hoop, with $-\tfrac12 ma^2\omega^2\sin^2\theta$ the centrifugal potential energy of *Rotating frames*.
- No numeric answer, tolerance or sign needed changing: every one of them recomputed correctly.

Concerns:
- MISSING CONVENTION, unchanged from the writer's report: notation/course-conventions.md fixes nothing for analytical mechanics. This section had to choose generalized coordinates $q^a$ with $a = 1..n$ (which collides with the file's 'Latin $i, j = 1,2,3$ for space'), overdot for $d/dt$, $L = T - V$, $S = \int L\,dt$, $p_a = \partial L/\partial\dot q^a$ with a lower index, $H = p_a\dot q^a - L$, and Hamilton's principal function written $S$, the same letter as the action. This review added one more: $Q_a$ for the generalized force, forced by the clash with the integrand $F$ of a general functional. A mechanics block should be added to course conventions before kepler-orbits, geodesics-as-extremals or the action-principles chapter is written.
- MISSING UNIT, unchanged from the writer's report: UNITS in knowledge/_tools/validate.py has no kg m^2/s, J s or m^2/s, so the Earth-orbit check cannot carry a numeric answer for the conserved momentum it is really about and has to report speed and period instead. Adding those three units would fix it.
- CONCEPT FIT: hamilton-jacobi-equation is the only advanced-tier concept in a section otherwise built from prerequisite-tier ones, and it is taught as a preview. Correct and self-contained as written, but if the outline wants it taught it belongs with the action-principles chapter or an advanced-track section.
- Both visuals are proposals with sketches and neither exists in the catalog. visual_ids.py offered nothing that fits either role.
- The section stays silent on Noether's theorem, which is the general statement behind 'a missing coordinate gives a conserved momentum'. That is the right call at this depth, but a later section should say so explicitly rather than leave the cyclic-coordinate mechanism looking like the whole story.
