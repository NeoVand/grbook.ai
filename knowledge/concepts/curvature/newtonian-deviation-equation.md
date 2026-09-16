---
type: "concept"
schema_version: 2
id: "newtonian-deviation-equation"
title: "Newtonian deviation equation"
tagline: "How the gap between two nearby freely falling objects changes, and why"
domain: "curvature"
tier: "foundation"
status: "physics-reviewed"
revision: 8
updated: "2026-09-13"
aliases: ["Newtonian equation of deviation", "Newtonian tidal equation"]
prerequisites: ["newtonian-tidal-tensor", "taylor-series", "poisson-equation-for-gravity"]
leads_to: ["geodesic-deviation-equation", "tidal-derivation-of-vacuum-field-equations"]
visuals: ["gap-between-two-falling-marbles", "two-tilted-orbits-crossing"]
---

# Newtonian deviation equation

*How the gap between two nearby freely falling objects changes, and why*

`newtonian-deviation-equation` · curvature · foundation · physics-reviewed (revision 8)

**Needs:** [[newtonian-tidal-tensor]] (entry) · [[taylor-series]] (entry) · [[poisson-equation-for-gravity]] (formal)  
**Opens:** [[geodesic-deviation-equation]] · [[tidal-derivation-of-vacuum-field-equations]]  
**Related:** [[tidal-force]]  
**Visuals:** ★ [[gap-between-two-falling-marbles]] · [[two-tilted-orbits-crossing]]

> When two nearby objects fall freely together, their gap changes only if gravity pulls on them differently. For a small gap, that difference in pull is in proportion to the gap. The Newtonian deviation equation turns this into a rule that predicts the gap, and Einstein's theory of gravity uses a rule of the same shape.

## You will be able to

**Entry**
- Explain why two objects falling freely together change their gap only through the difference in pull. `objectives/explain-shared-pull-drops-out` ← `checks/marbles-in-a-falling-capsule`
- Estimate how the difference in pull depends on the gap and on the distance to the pulling body. `objectives/estimate-difference-from-gap` ← `checks/sun-or-moon`, `problems/jupiter-and-the-tides`
- Predict how a sideways gap between neighbours in orbit changes over one lap. `objectives/predict-sideways-swing` ← `checks/when-is-the-gap-widest-again`

**Working**
- Use the deviation equation with the point-mass Hessian to predict how a separation changes. `objectives/use-deviation-equation` ← `problems/drop-tower-pair`
- Judge when the first-order equation is accurate. `objectives/judge-first-order-accuracy` ← `checks/near-side-and-far-side`

**Formal**
- Relate the trace of the Hessian to how a small cloud's volume changes. `objectives/relate-trace-to-volume` ← `checks/trace-free-cloud-volume`, `checks/pass-through-planet`
- Derive the relative-motion equations about a circular orbit in rotating axes. `objectives/derive-rotating-frame-equations` ← `problems/hill-equations`

## Ways in

### 1. Ride along and measure the gap · entry · operational

*When two marbles fall freely together, what makes the gap between them change?*

Picture a capsule falling down a tube about 110 metres tall, with the air pumped out. Nothing but gravity acts on the capsule while it falls. Moving with nothing but gravity acting is called falling freely.

Ride inside the capsule. At the moment it drops, let go of two identical marbles, one a metre above the other. You, the capsule and both marbles fall freely together. That is why the marbles float in front of you. You measure the gap between them with a ruler fixed to the capsule.

Suppose Earth pulled both marbles with exactly the same strength, in exactly the same direction. Then both would gain speed in exactly the same way, second by second. Their gap would never change, however fast they fell. A pull that the two marbles share cannot change the gap.

Only the difference between the two pulls can. Earth pulls more weakly on things farther from its centre: at the Moon's distance, its pull is about 3,600 times weaker than at the ground. The lower marble is a metre nearer Earth's centre, so Earth pulls it a little harder than the upper marble. The lower marble therefore gains speed a little faster, and the gap slowly grows.

Marbles side by side are pulled equally hard, but in slightly different directions. The way "Neighbours in orbit swing through each other" follows that case.

How slowly does the gap grow? The fall lasts almost five seconds, and each marble reaches about 167 kilometres an hour relative to the tube. Yet the gap grows by only about three hundredths of a millimetre, half the width of a hair. That is why nobody notices this growth in daily life.

**Takeaway:** Two marbles that fall freely together keep their gap unless Earth pulls on them differently; only the difference between the two pulls changes the gap.

*Visuals:* [[gap-between-two-falling-marbles]]<br>*See:* `checks/marbles-in-a-falling-capsule`

### 2. Twice the gap, twice the difference · entry · calculation

*How big is the difference in pull across a small gap?*

**Recap:** Two marbles fall freely together, with nothing but gravity acting on them, one a metre above the other. A pull they share cannot change their gap; only the difference between the pulls on them can. Earth pulls harder on the lower marble, because it is nearer Earth's centre.

In "Ride along and measure the gap", only the difference between two pulls changed the gap between the marbles. How big is that difference?

Earth's centre is 6,371 kilometres, or 6,371,000 metres, below the ground. So a marble one metre lower is nearer the centre by one part in 6,371,000.

Above the ground, gravity weakens with the square of the distance from Earth's centre. Twice as far away, the pull is a quarter as strong. Take a marble nearer by one part in a hundred: its distance is 0.99 times as big. The pull on it is multiplied by one over 0.99, which is about 1.01. The squaring means that happens twice, and 1.01 times 1.01 is about 1.02. So being nearer by a tiny fraction makes the pull stronger by twice that fraction.

The lower marble is therefore pulled harder than the upper marble by two parts in 6,371,000, about one part in 3.2 million.

Now double the gap to two metres. The lower marble is nearer by twice as much, so the difference in pull doubles too. For small gaps, the difference in pull is in proportion to the gap.

The difference in pull changes the gap, and the gap sets the difference in pull. A rule that links them this way, and so predicts the gap, is called the Newtonian deviation equation. For marbles one above the other, a wider gap means a bigger difference in pull, so the gap widens faster and faster.

The rule needs a gap much smaller than the distance to Earth's centre. For a gap of half that distance, the rule predicts a pull twice as strong, but the true pull is four times as strong.

The same rule compares the Sun and the Moon. Outside any round body, take two objects a small gap apart on a line to its centre. The body pulls harder on the nearer object, by a fraction: twice the gap divided by the distance to that centre. The Sun is far heavier, so it pulls on Earth about 180 times harder than the Moon does. But take the same gap for both, from Earth's centre to the ocean facing each body. The Sun is about 390 times farther away than the Moon, so the Sun's fraction is 390 times smaller. And 180 divided by 390 is about one half. So the Moon's difference in pull across Earth is about twice the Sun's.

**Takeaway:** For a small gap, the difference in pull on two falling neighbours is in proportion to the gap, so the gap itself sets the difference in pull that widens or narrows it.

*Continues:* `ways_in/ride-along-and-measure-the-gap`<br>*Builds on:* [[newtonian-tidal-tensor]], [[taylor-series]]<br>*Visuals:* [[gap-between-two-falling-marbles]]<br>*See:* `checks/sun-or-moon`, `observations/tides-follow-the-moon`

### 3. Neighbours in orbit swing through each other · entry · picture

*What does a sideways gap between two neighbours in orbit do over one lap?*

**Recap:** Two neighbours falling freely change their gap only through the difference between the pulls on them. For a small gap, that difference is in proportion to the gap. A stretched spring also pulls harder the more it is stretched.

In "Twice the gap, twice the difference", the difference in pull on marbles one above the other grew with their gap and widened it. Now put two neighbours side by side instead.

Two tiny pebbles orbit Earth 400 kilometres up, at the same height. Ignore the very thin air at that height. Then nothing but gravity acts on each pebble, so each pebble falls freely, like the capsule. Earth's pull is equally strong at equal heights, so the same speed keeps each pebble on its circle. Both take about 92 minutes per lap.

Earth's pull on each pebble points at Earth's centre, so each circle is centred on Earth's centre. The two orbits are therefore like two equal hula hoops sharing a centre, one tilted very slightly. Two such hoops cross at two points, half a lap apart.

Start the pebbles side by side, halfway between the crossings, with one a tiny bit ahead. There the hoops are farthest apart. The gap between the pebbles points across their direction of travel.

Earth pulls both pebbles equally hard, but not in quite the same direction. Each pull points along a line to Earth's centre. The two lines meet there, like two neighbouring spokes of a wheel. So each pull points slightly toward the other pebble.

A wider gap spreads the spokes wider apart. So for a small gap, the part of each pull that points toward the other pebble is in proportion to the gap. This difference in direction is a difference in pull, and it draws the pebbles together. The pull toward each other acts like a stretched spring, which pulls harder the more it is stretched.

The pebbles gain speed toward each other as the gap closes, so they do not stop when they meet. One pebble is a tiny bit ahead, so they slip past without bumping, and the gap opens on the other side.

The hoops show how long one swing takes. The pebbles meet at a crossing after a quarter lap, about 23 minutes. After half a lap, the gap is as wide as at the start. Facing the way the pebbles travel, the pebble that started on the left is now on the right. After one full lap, the pebbles are back where they started, side by side.

**Try it:** Stretch two rubber bands around the widest part of an orange so that they cross at a small angle. They cross twice, on opposite sides of the orange. Follow the gap between the bands around the orange: it is widest halfway between the crossings, closes at each crossing, and opens on the other side.

**Takeaway:** Side by side, the difference in pull draws two falling neighbours together like a spring. For neighbours orbiting side by side at the same height, their gap swings back and forth, once per lap.

*Continues:* `ways_in/twice-the-gap-twice-the-difference`<br>*Visuals:* [[two-tilted-orbits-crossing]]<br>*See:* `checks/when-is-the-gap-widest-again`

### 4. Subtract two falls and expand · working · calculation

*What equation does the separation of two nearby freely falling particles obey?*

In "Twice the gap, twice the difference", the difference in pull between two falling neighbours came out in proportion to their gap. Calculus turns that into an equation. Per unit mass, the entry rung's difference in pull becomes a relative acceleration, and its gap becomes the separation vector $\boldsymbol\xi$. Let a reference particle follow $\mathbf x(t)$ in a Newtonian potential $\Phi$, and let its neighbour be at $\mathbf x(t) + \boldsymbol\xi(t)$ at the same time $t$. Subtract their equations of motion and expand $\nabla\Phi$ to first order in the separation, as the derivation "Subtract two equations of motion" does step by step:

$$\ddot{\boldsymbol\xi} = -\big(\nabla\nabla\Phi\big)\,\boldsymbol\xi.$$

Here $\nabla\nabla\Phi$ is the Hessian matrix of $\Phi$ at $\mathbf x(t)$: its entry in row $x$ and column $y$ is $\partial^2\Phi/\partial x\,\partial y$. Three features matter.

- The field $-\nabla\Phi$ has dropped out, so a uniform field gives no relative acceleration.
- The relative acceleration is linear in $\boldsymbol\xi$.
- The matrix is sampled on the reference path, so it changes as the pair moves.

Outside a spherical mass, $\Phi = -GM/r$ gives $\nabla\nabla\Phi = (GM/r^3)(\mathbf 1 - 3\hat{\mathbf r}\hat{\mathbf r}^{\mathsf T})$, with eigenvalue $-2GM/r^3$ along $\hat{\mathbf r}$ and $+GM/r^3$ in both transverse directions. A radial separation therefore obeys $\ddot\xi = +(2GM/r^3)\,\xi$ and grows. That is the entry rung's "twice the fraction" rule: the pull $GM/r^2$ is weaker by the fraction $2\xi/r$ on a neighbour a distance $\xi$ farther out. A transverse one obeys $\ddot\xi = -(GM/r^3)\,\xi$ and oscillates. While the matrix stays nearly constant, a pair released at rest has $\xi = \xi_0\cosh(\sqrt{2GM/r^3}\,t)$ radially and $\xi = \xi_0\cos(\sqrt{GM/r^3}\,t)$ transversely. For two orbits at the same radius the cross-orbit entry stays constant, and $\sqrt{GM/r^3}$ is the orbit's angular velocity: that is why the pebbles in "Neighbours in orbit swing through each other" complete one swing per lap.

Two limits come with the equation. The separation joins the two particles at one instant $t$. And the neglected second-order term, relative to the kept one, is about $\tfrac32|\boldsymbol\xi|/r$ for a point mass, so the separation must be small compared with $r$.

**Takeaway:** Subtracting the motions of two nearby freely falling particles and expanding to first order gives a relative acceleration equal to minus the Hessian of the potential acting on the separation.

*What this leaves out:* Assumes a non-rotating frame, test particles whose own gravity is negligible, and no forces other than gravity.

*Continues:* `ways_in/twice-the-gap-twice-the-difference`, `ways_in/neighbours-in-orbit-swing`<br>*Builds on:* [[newtonian-tidal-tensor]], [[taylor-series]]<br>*Visuals:* [[gap-between-two-falling-marbles]]<br>*See:* `derivations/subtract-two-equations-of-motion`, `worked_examples/swing-period-of-neighbouring-orbits`

### 5. A gradiometer reads the equation backwards · working · operational

*How can an instrument measure the matrix in the deviation equation?*

The equation of "Subtract two falls and expand" can be read backwards. Measure the relative acceleration of two test masses a known separation apart, divide by the separation, and you have entries of $-\nabla\nabla\Phi$. An instrument that does this is a gravity gradiometer. An accelerometer riding on a single freely falling mass reads zero, so it cannot see $\nabla\nabla\Phi$; a pair can.

The GOCE satellite mapped Earth's gravity from 2009 to 2013, orbiting at about 255 km. Its gradiometer held three pairs of accelerometers on perpendicular arms 0.5 m long, and each pair measured the difference of its two proof masses' accelerations. Gradients are quoted in eötvös, $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$. At $r = 6626$ km a spherical Earth gives a radial entry $2GM/r^3 = 2.74\times10^{-6}\ \mathrm{s^{-2}}$, about 2740 E. So the two masses of the radial pair accelerate apart at $1.37\times10^{-6}\ \mathrm{m\,s^{-2}}$. The mission's goal was the much smaller departures from this spherical value, set by Earth's flattening, mountains and uneven interior.

Two cautions come with the instrument. The spacecraft turns once per orbit to keep facing Earth, so its accelerometers also sense centrifugal and angular accelerations, which must be removed using star-camera attitude data and the gradiometer's own readings. And in empty space the three diagonal entries of $\nabla\nabla\Phi$ add up to zero, because $\nabla^2\Phi = 0$ there: stretching along one axis is balanced by squeezing along the other two.

**Takeaway:** Relative accelerations of test masses a known distance apart measure the Hessian of the potential directly; a single accelerometer in free fall cannot.

*Picture:* Three short perpendicular arms, each with a proof mass at either end; arrows show the radial pair drifting apart and the two transverse pairs drawing together.

*What this leaves out:* Treats Earth as spherical for the numbers and ignores atmospheric drag, which the spacecraft compensated.

*Continues:* `ways_in/subtract-two-falls`<br>*See:* `observations/goce-gravity-gradients`

### 6. The linearized flow and its limits · formal · structure

*Under which hypotheses is the deviation equation exact or approximate, and what structure does it carry?*

The subtraction in "Subtract two falls and expand" is the linearization of Newton's equations of motion, and it can be stated with its hypotheses. Work in Galilean spacetime with absolute time $t$, in a non-rotating frame, with $G = 1$. Let $\Phi \in C^3(U)$ on an open set $U \subset \mathbb{R}^3$, and let only gravity act on test particles whose own gravity is neglected.

*Exact form.* Let $\mathbf x(t, s)$ be a family of solutions of $\partial_t^2\mathbf x = -\nabla\Phi(\mathbf x)$, of class $C^2$ in $(t, s)$. Differentiating in $s$ and exchanging the order of the derivatives gives, for $\mathbf J = \partial_s\mathbf x|_{s=0}$, exactly

$$\ddot{\mathbf J} = -\nabla\nabla\Phi\big(\mathbf x(t, 0)\big)\,\mathbf J.$$

Its solutions form a six-dimensional space fixed by $\mathbf J(0)$ and $\dot{\mathbf J}(0)$: the tangent map of the flow on phase space.

*Two particles.* For solutions $\mathbf x$ and $\mathbf x + \boldsymbol\xi$ compared at equal $t$, Taylor's theorem with remainder gives $\ddot{\boldsymbol\xi} = -\nabla\nabla\Phi(\mathbf x)\,\boldsymbol\xi + \mathbf e$ with $|\mathbf e| \le \tfrac12 M_3|\boldsymbol\xi|^2$, where $M_3$ bounds the third derivatives of $\Phi$ on the segment from $\mathbf x$ to $\mathbf x + \boldsymbol\xi$. The linear term dominates while $|\boldsymbol\xi| \ll \ell = \|\nabla\nabla\Phi\|/M_3$; for a point mass $\ell = r/3$. On a fixed time interval the flow is $C^2$ in its initial data, so the linear solution differs from the true separation by terms quadratic in the initial separation and relative velocity. Along stretching directions the separation grows exponentially, which limits that interval.

*Structure.* $H = \nabla\nabla\Phi$ is symmetric, with real eigenvalues and orthogonal principal axes. A spatially uniform field $\mathbf g(t)$, such as the one that describes a freely falling frame, leaves $H$ unchanged. By Poisson's equation $\mathrm{tr}\,H = 4\pi\rho$, so $H$ is trace-free in vacuum. For a cloud $\boldsymbol\xi = D\,\boldsymbol\xi_0$ released at rest, $\theta = \dot DD^{-1}$ obeys $\dot\theta = -H - \theta^2$, so the volume $V$ satisfies $\tfrac{d^2}{dt^2}\ln V = -4\pi\rho - \mathrm{tr}\,\theta^2$. In a frame rotating at constant $\boldsymbol\Omega$ the equation gains $-2\boldsymbol\Omega\times\dot{\boldsymbol\xi} - \boldsymbol\Omega\times(\boldsymbol\Omega\times\boldsymbol\xi)$.

*Template.* Taken on trust here, Newtonian gravity can be rewritten as a torsion-free connection on Galilean spacetime whose only nonzero Christoffel symbols, in non-rotating coordinates, are $\Gamma^i{}_{tt} = \partial_i\Phi$. Free fall is then geodesic, the course Riemann convention gives $R^i{}_{tjt} = \partial_i\partial_j\Phi$, and the course geodesic deviation equation with $u = \partial_t$ reproduces $\ddot{\boldsymbol\xi} = -H\boldsymbol\xi$ exactly. General relativity keeps this form, with $H$ replaced by curvature components in a freely falling frame.

**Takeaway:** Exact as the variational equation of free fall and first-order for two particles, with a quadratic error; its symmetric matrix has a trace set by density, and its curvature form is what relativity copies.

*Picture:* A bundle of neighbouring free-fall paths in space and time, with the equal-time separation drawn between two of them and a small ellipsoid of neighbours around one path, stretched along one principal axis and squeezed along the others.

*What this leaves out:* Stays within Newtonian gravity; the relativistic version replaces the Hessian by spacetime curvature.

*Continues:* `ways_in/subtract-two-falls`<br>*Builds on:* [[taylor-series]], [[poisson-equation-for-gravity]]<br>*See:* `checks/trace-free-cloud-volume`, `checks/pass-through-planet`, `problems/hill-equations`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| Newtonian deviation equation | new-TOE-nee-un dee-vee-AY-shun ih-KWAY-zhun | In Newton's theory of gravity, the rule that predicts how the gap between two nearby freely falling objects changes. | [[newtonian-deviation-equation]] |
| orbit | — | The path of something that keeps falling around a planet without hitting it, as the Moon does around Earth. | — |
| tide | — | The slow rise and fall of the sea along a coast, at most places twice in a little over a day. | [[tidal-force]] |

## Key equations

### Newtonian deviation equation · working

$$
\ddot{\boldsymbol\xi} = -\big(\nabla\nabla\Phi\big)\big|_{\mathbf x(t)}\,\boldsymbol\xi
$$

The relative acceleration of two nearby freely falling particles is minus the Hessian of the potential acting on their separation.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\boldsymbol\xi$ | separation of the neighbour from the reference particle, at the same time $t$ | xi, the separation |
| $\nabla\nabla\Phi$ | Hessian matrix of the potential on the reference path $\mathbf x(t)$ | the Hessian of the potential |

**Holds when:** Non-rotating frame; only gravity acts; test particles; first order in $|\boldsymbol\xi|$.  
**Say it:** “The second time derivative of the separation is minus the Hessian of the potential acting on the separation.”  
**Justified by:** `derivations/subtract-two-equations-of-motion`

### Hessian outside a spherical mass · working

$$
\nabla\nabla\Phi = \frac{GM}{r^3}\left(\mathbf 1 - 3\,\hat{\mathbf r}\,\hat{\mathbf r}^{\mathsf T}\right)
$$

Eigenvalue $-2GM/r^3$ along the radius, where separations grow, and $+GM/r^3$ across it, where they oscillate.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\hat{\mathbf r}$ | unit vector from the centre toward the reference particle | r hat |
| $\mathbf 1$ | the identity matrix | the identity |

**Holds when:** Outside a spherical mass, where $\Phi = -GM/r$.  
**Say it:** “The Hessian is G M over r cubed, times the identity minus three r hat r hat.”  
**Justified by:** `newtonian-tidal-tensor`

## Derivations

### Subtract two equations of motion · working

**Goal:** Show that the equal-time separation $\boldsymbol\xi$ of two nearby freely falling particles obeys $\ddot{\boldsymbol\xi} = -(\nabla\nabla\Phi)\,\boldsymbol\xi$ to first order.

1. Only gravity acts, so the reference particle obeys $\ddot{\mathbf x} = -\nabla\Phi(\mathbf x)$; its mass has cancelled.
2. The neighbour is at $\mathbf x + \boldsymbol\xi$ at the same time $t$, so $\ddot{\mathbf x} + \ddot{\boldsymbol\xi} = -\nabla\Phi(\mathbf x + \boldsymbol\xi)$.
3. Expand to first order about $\mathbf x$: $\nabla\Phi(\mathbf x + \boldsymbol\xi) = \nabla\Phi(\mathbf x) + (\nabla\nabla\Phi)\,\boldsymbol\xi + O(|\boldsymbol\xi|^2)$. Row $x$ of the Hessian is the gradient of $\partial\Phi/\partial x$, so the new term is the change of $\nabla\Phi$ along $\boldsymbol\xi$.
4. Subtract the first equation from the second. The shared $\nabla\Phi(\mathbf x)$ cancels, leaving $\ddot{\boldsymbol\xi} = -(\nabla\nabla\Phi)\,\boldsymbol\xi + O(|\boldsymbol\xi|^2)$.
5. Mixed partial derivatives of a twice continuously differentiable $\Phi$ agree, so the Hessian is symmetric, with real eigenvalues and perpendicular principal directions.

**Result:** $\ddot{\boldsymbol\xi} = -(\nabla\nabla\Phi)\big|_{\mathbf x(t)}\,\boldsymbol\xi$, with corrections of second order in $|\boldsymbol\xi|$.

## Worked examples

### The swing of neighbouring orbits · working

**Problem:** Two satellites move on circular orbits of radius $r = 6771$ km in planes tilted slightly apart. When they are level, their separation $\xi_0$ is perpendicular to the orbital plane and their relative velocity is zero. Find how the separation changes, its period, and when they first meet.

1. The orbit normal $\hat{\mathbf n}$ is fixed in a non-rotating frame and always perpendicular to $\hat{\mathbf r}$, so $(\nabla\nabla\Phi)\,\hat{\mathbf n} = (GM/r^3)\,\hat{\mathbf n}$ and the separation stays along $\hat{\mathbf n}$.
2. With $r$ constant, $\ddot\xi = -\omega^2\xi$ with $\omega^2 = GM/r^3$, and $\xi(0) = \xi_0$, $\dot\xi(0) = 0$ give $\xi = \xi_0\cos\omega t$.
3. A circular orbit has $v^2/r = GM/r^2$, so its angular velocity $v/r$ equals $\omega$: one swing takes one orbital period.
4. $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$ gives $\omega = 1.133\times10^{-3}\ \mathrm{s^{-1}}$ and period $2\pi/\omega = 5545$ s, or 92.4 min. They first meet at $\omega t = \pi/2$, after 23.1 min.

**Answer:** $\xi = \xi_0\cos\omega t$ with period 92.4 min, the orbital period; they first meet after 23.1 min.

**Takeaway:** The cross-orbit entry of the Hessian is the square of the orbit's angular velocity, so the equation reproduces the geometry of tilted orbits.

## Problems

### `jupiter-and-the-tides` · entry · difficulty 1 · estimate

Jupiter's pull on Earth is at most about one ninetieth of the Moon's. Jupiter is always at least about 1,500 times farther away than the Moon. Could Jupiter noticeably change Earth's tides? Compare its difference in pull across Earth with the Moon's.

**Hints**

1. Across the same gap, how does a body's difference in pull depend on its distance?

**Answer:** No. Jupiter's difference in pull is at most about one part in 135,000 of the Moon's.

**Must contain:** Jupiter's fraction is 1,500 times smaller than the Moon's; One ninetieth divided by 1,500 is one part in 135,000

**Numeric:** Jupiter's difference in pull as a fraction of the Moon's = 7.4e-06 1 (magnitude, ±15%)

**Solution**

1. For both bodies the gap runs from Earth's centre to the ocean facing the body. Across that gap, a body's difference in pull is its own pull times a fraction, and that fraction is twice the gap divided by its distance.
2. Jupiter is at least 1,500 times farther away, so its fraction is at most one part in 1,500 of the Moon's.
3. Jupiter's pull is at most one part in 90 of the Moon's. Its difference in pull is therefore smaller than the Moon's by a factor of 90 and again by a factor of 1,500, which is one part in 135,000.

**Targets:** `bigger-pull-bigger-tides`

### `drop-tower-pair` · working · difficulty 2 · calculation

A drop-tower capsule falls freely for 4.70 s near Earth's surface ($r = 6371$ km, $GM = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$). Two marbles are released at rest inside, 2.00 m apart. How much does their gap change if they are (a) one above the other, (b) side by side?

**Hints**

1. Radially $\ddot\xi = +(2GM/r^3)\,\xi$; transversely $\ddot\xi = -(GM/r^3)\,\xi$.

**Answer:** (a) It grows by $6.81\times10^{-5}$ m. (b) It shrinks by $3.40\times10^{-5}$ m.

**Must contain:** The vertical gap grows by 68 micrometres; The horizontal gap shrinks by 34 micrometres

**Numeric:** increase of the vertical gap = 6.81e-05 m (magnitude, ±3%); decrease of the horizontal gap = 3.4e-05 m (magnitude, ±3%)

**Solution**

1. $GM/r^3 = 3.986\times10^{14}/(6.371\times10^{6})^3 = 1.541\times10^{-6}\ \mathrm{s^{-2}}$.
2. (a) $\xi = \xi_0\cosh(\sqrt{2GM/r^3}\,t)$ with $\sqrt{2GM/r^3}\,t = 8.25\times10^{-3}$, so $\cosh - 1 = 3.40\times10^{-5}$ and the gap grows by $6.81\times10^{-5}$ m.
3. (b) $\xi = \xi_0\cos(\sqrt{GM/r^3}\,t)$ with $1 - \cos = 1.70\times10^{-5}$, so the gap shrinks by $3.40\times10^{-5}$ m.
4. The next terms of these series are smaller by about $6\times10^{-6}$, and the 108 m drop changes $GM/r^3$ by only $5\times10^{-5}$ of itself, so both can be neglected.

### `hill-equations` · formal · difficulty 3 · derivation

A reference body moves on a circular orbit about a spherical mass $M$ with angular velocity $n = \sqrt{GM/r^3}$. From the deviation equation, derive the equations for a nearby particle's separation $(x, y, z)$ in axes rotating with the body: $x$ radially outward, $y$ along the motion, $z$ along the orbital angular momentum.

**Hints**

1. A frame rotating at constant $\boldsymbol\Omega$ adds $-2\boldsymbol\Omega\times\dot{\boldsymbol\xi} - \boldsymbol\Omega\times(\boldsymbol\Omega\times\boldsymbol\xi)$.

**Answer:** $\ddot x - 2n\dot y - 3n^2x = 0$, $\ddot y + 2n\dot x = 0$ and $\ddot z + n^2z = 0$.

**Must contain:** The non-rotating relative acceleration is n squared times two x, minus y, minus z; Coriolis and centrifugal terms complete the rotating equations

**Solution**

1. In a non-rotating frame falling with the body, the Hessian in these axes is $n^2\,\mathrm{diag}(-2, 1, 1)$, so $\ddot{\boldsymbol\xi} = n^2(2x, -y, -z)$.
2. In axes rotating at $\boldsymbol\Omega = n\hat{\mathbf z}$, add $-2\boldsymbol\Omega\times\dot{\boldsymbol\xi} = (2n\dot y, -2n\dot x, 0)$ and $-\boldsymbol\Omega\times(\boldsymbol\Omega\times\boldsymbol\xi) = (n^2x, n^2y, 0)$.
3. Adding gives $\ddot x = 3n^2x + 2n\dot y$, $\ddot y = -2n\dot x$ and $\ddot z = -n^2z$.
4. Constant $y$ with $x = z = 0$ is a solution: a particle trailing on the same orbit keeps its distance. The $z$ motion is the cross-orbit swing with period $2\pi/n$.

## Observations

- **Ocean tides keep pace with the Moon** (measured, entry). Earth and its oceans fall freely toward the Moon together, like marbles in a falling capsule. So the part of the Moon's pull that the ocean and the ground share cannot move the ocean compared with the ground. Only the difference in the Moon's pull across Earth can, and that difference raises the tides. At most coasts, high tide comes about 50 minutes later each day, keeping pace with the Moon. The biggest tides come around new and full Moon. Then the Sun, Earth and the Moon lie nearly in a line, so the Sun's difference in pull adds to the Moon's. *Numbers:* The Moon's difference in pull across Earth is about one nine-millionth of Earth's own gravity at the ground; the Sun's is a little under half of it. *Reference:* David Edgar Cartwright (1999), *Tides: A Scientific History*, Cambridge University Press
- **Gravity gradients measured by the GOCE satellite's gradiometer, 2009 to 2013** (measured, working). Accelerometer pairs 0.5 m apart measured relative accelerations, which the deviation equation turns into entries of the Hessian of Earth's potential. *Numbers:* The dominant radial gradient, about $2.7\times10^{-6}\ \mathrm{s^{-2}}$ (2700 eötvös), matches $2GM/r^3$; the mapped signal is the far smaller departures from it. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0

## Teaching arc

1. **Pose the floating marbles question** (entry). Ask whether marbles floating in a falling capsule can drift, then give the shared-pull argument. *Why:* It separates falling together from gravity being switched off. *Predict:* Will the gap between two marbles floating in a falling capsule change? *Visual:* [[gap-between-two-falling-marbles]] *Uses:* `checks/marbles-in-a-falling-capsule`, `ways_in/ride-along-and-measure-the-gap`
2. **Size the difference** (entry). Double the gap, then compare the Sun and the Moon. *Why:* The pull itself turns out not to matter, only its change across the gap. *Predict:* The Sun pulls Earth far harder than the Moon. Which raises the bigger tides? *Uses:* `ways_in/twice-the-gap-twice-the-difference`, `checks/sun-or-moon`
3. **Watch the sideways swing** (entry). Show two tilted orbits and ask when the pebbles meet. *Why:* A swing instead of a collision is the equation at work. *Visual:* [[two-tilted-orbits-crossing]] *Uses:* `ways_in/neighbours-in-orbit-swing`, `checks/when-is-the-gap-widest-again`
4. **Derive, solve and bound** (working). Derive the equation by subtraction, solve it for a point mass, and find where first order fails. *Why:* The subtraction shows why only the Hessian survives. *Uses:* `derivations/subtract-two-equations-of-motion`, `worked_examples/swing-period-of-neighbouring-orbits`, `checks/near-side-and-far-side`
5. **Read it backwards** (working). Treat the equation as an instrument that measures the Hessian. *Why:* It turns the equation into a measurement. *Uses:* `ways_in/gradiometer-reads-the-hessian`, `observations/goce-gravity-gradients`

## Misconceptions

### “Things floating in a falling capsule feel no gravity, so their gap cannot change.” · entry · `floating-means-no-gravity`

- **Why it is tempting:** Everything floats, as it would far out in space.
- **What is true:** They float because they fall together while Earth keeps pulling. The lower one is pulled slightly harder, so the gap slowly grows.
- **Exposed by:** `checks/marbles-in-a-falling-capsule`

### “The Sun pulls Earth harder than the Moon does, so the Sun must raise the bigger tides.” · entry · `bigger-pull-bigger-tides`

- **Why it is tempting:** A stronger pull sounds like a stronger effect.
- **What is true:** Only the difference in pull across Earth matters. The Sun is so far away that its difference in pull across Earth is about half the Moon's.
- **Exposed by:** `checks/sun-or-moon`

### “If gravity draws two orbiting neighbours together, they meet and stay together.” · entry · `neighbours-meet-and-stay`

- **Why it is tempting:** A pull toward each other sounds as if it must end in contact.
- **What is true:** They gain speed toward each other as the gap closes, so two tiny pebbles that just miss each other do not stop but slip past. The gap swings back and forth like a mass on a spring.
- **Exposed by:** `checks/when-is-the-gap-widest-again`

### “The deviation equation is linear, so it holds for any separation.” · working · `rule-works-for-any-gap`

- **Why it is tempting:** A linear equation looks exact.
- **What is true:** It keeps only the first-order term, which needs a separation much smaller than the distance over which the Hessian changes. Across Earth's radius the Moon's pull already departs from it by about 2.5 percent.
- **Exposed by:** `checks/near-side-and-far-side`

### “In empty space the Hessian has zero trace, so a falling cloud keeps its volume exactly.” · formal · `trace-free-keeps-volume`

- **Why it is tempting:** Zero trace does keep the volume steady at first.
- **What is true:** Zero trace fixes only the early time derivatives of the volume. The shearing feeds back, and the volume shrinks at fourth order in time.
- **Exposed by:** `checks/trace-free-cloud-volume`

## Checks

1. **Entry · predict** `checks/marbles-in-a-falling-capsule`. A capsule falls freely down a tall tube with the air pumped out. As it drops, two identical marbles inside are let go, one a metre above the other. A friend says gravity is switched off inside, so the gap cannot change. Measured with a ruler fixed to the capsule, does the gap stay exactly one metre?
   - **Hints:** Which marble is nearer Earth's centre?
   - **Answer:** No, it grows very slightly. The marbles float because they fall together with the capsule, not because gravity is switched off. Earth keeps pulling on both. The lower marble is nearer Earth's centre, so Earth pulls it a little harder. The lower marble therefore gains speed a little faster than the upper marble, and the gap slowly grows.
   - **Must contain:** The gap grows very slightly; Floating means falling together, and the lower marble is pulled a little harder
   - **Targets:** `floating-means-no-gravity`
   - **Visual:** [[gap-between-two-falling-marbles]]
2. **Entry · numeric** `checks/sun-or-moon`. The Sun pulls on Earth about 180 times harder than the Moon does, but it is about 390 times farther away. Take the gap from Earth's centre to the ocean facing each body. Whose difference in pull across that gap is bigger, and roughly how many times bigger?
   - **Hints:** Across the same gap, how does a body's difference in pull depend on its distance?
   - **Answer:** The Moon's, about twice as big. Take two objects a small gap apart on the line to a body. The body pulls harder on the nearer object, by a fraction: twice the gap divided by the body's distance. Here that gap runs from Earth's centre to the ocean, and it is the same for both bodies. So the Sun's fraction is 390 times smaller, and the Sun's pull is 180 times bigger. The Sun's difference in pull is therefore about 180 divided by 390, one half, of the Moon's.
   - **Must contain:** The Moon's difference in pull is about twice the Sun's; The difference is the body's pull times a fraction: twice the gap divided by its distance
   - **Numeric:** Moon's difference in pull divided by the Sun's = 2.2 1 (magnitude, ±15%)
   - **Targets:** `bigger-pull-bigger-tides`
3. **Entry · predict** `checks/when-is-the-gap-widest-again`. Two tiny pebbles orbit Earth at the same height, in orbits tilted very slightly apart, taking 100 minutes per lap. They start side by side, 5 metres apart, halfway between the two points where their orbits cross. One pebble is a tiny bit ahead, so they cannot bump. Do they meet and stay together? Where are they after 25 minutes, and after 50 minutes?
   - **Hints:** Picture the orbits as two tilted hoops sharing a centre.
   - **Answer:** They do not stay together. The orbits are like two equal tilted hoops sharing a centre, crossing at two points half a lap apart. The pebbles start halfway between the crossings, so they are a quarter lap from the next crossing. After 25 minutes, a quarter lap, they both reach it. One pebble started a tiny bit ahead, so they just miss each other and slip past. Their speed toward each other carries them on, and the gap opens on the other side. After 50 minutes, half a lap, they are 5 metres apart again. Facing the way they travel, the pebble that started on the left is now on the right.
   - **Must contain:** They meet after 25 minutes and slip past; After 50 minutes they are 5 metres apart again, on swapped sides
   - **Numeric:** time until they first meet = 25 min (magnitude, ±5%)
   - **Targets:** `neighbours-meet-and-stay`
   - **Visual:** [[two-tilted-orbits-crossing]]
4. **Working · evaluate-claim** `checks/near-side-and-far-side`. Using the deviation equation, a student claims that the Moon's relative acceleration of the ocean, measured from Earth's centre, is exactly equal in size on the near and far sides. Evaluate the claim for $R/d = 6371/384400$.
   - **Hints:** Expand the exact differences to second order in $R/d$.
   - **Answer:** False as stated: the two sizes agree only to first order in $x = R/d = 0.01657$. The equation gives $2GM_{\rm m}R/d^3$ on both sides. The exact values, $GM_{\rm m}[(d-R)^{-2} - d^{-2}]$ on the near side and $GM_{\rm m}[d^{-2} - (d+R)^{-2}]$ on the far side, are $1.0254$ and $0.9757$ times that, so the near side's is 5.1 per cent larger. The neglected term is about $\tfrac32x = 2.5$ per cent of the kept one.
   - **Must contain:** Equal only to first order in R over d; The near side exceeds the far side by about 5 percent
   - **Numeric:** near-side over far-side relative acceleration = 1.051 1 (magnitude, ±0.003)
   - **Targets:** `rule-works-for-any-gap`
5. **Formal · evaluate-claim** `checks/trace-free-cloud-volume`. Claim: outside a spherical mass $\nabla^2\Phi = 0$, so a small cloud of test particles released at rest keeps its volume exactly. Evaluate the claim.
   - **Hints:** Use Jacobi's formula for the derivative of a determinant.
   - **Answer:** False beyond early times. Write $\boldsymbol\xi = D\,\boldsymbol\xi_0$ with $\ddot D = -HD$, $D(0) = \mathbf 1$, $\dot D(0) = 0$ and $H = \nabla\nabla\Phi$. Jacobi's formula gives $\tfrac{d}{dt}\ln V = \mathrm{tr}\,\theta$ with $\theta = \dot DD^{-1}$, and $\dot\theta = -H - \theta^2$, so $\tfrac{d^2}{dt^2}\ln V = -\mathrm{tr}\,H - \mathrm{tr}\,\theta^2$. In vacuum the first term vanishes, but $\theta \approx -Ht$ gives $\ln V \approx -\mathrm{tr}(H^2)\,t^4/12$. For eigenvalues $(GM/r^3)(-2, 1, 1)$ this is $V/V_0 \approx 1 - \tfrac12(GM/r^3)^2t^4$.
   - **Must contain:** In vacuum the second derivative of log volume is minus the trace of theta squared; The volume shrinks at fourth order in time
   - **Targets:** `trace-free-keeps-volume`
6. **Formal · numeric** `checks/pass-through-planet`. Treat Earth as a uniform ball of density $5510\ \mathrm{kg\,m^{-3}}$ that test particles pass through freely. Show that inside it every small separation swings with one period, whatever its direction, and find that period.
   - **Hints:** Find the field inside the ball from the mass enclosed.
   - **Answer:** The mass within radius $r$ gives a field $\tfrac43\pi G\rho\,r$ toward the centre, so $\Phi = \tfrac23\pi G\rho\,r^2 + \text{const}$ and $\nabla\nabla\Phi = \tfrac43\pi G\rho\,\mathbf 1$, whose trace $4\pi G\rho$ agrees with Poisson's equation. Every separation obeys $\ddot{\boldsymbol\xi} = -\omega^2\boldsymbol\xi$ with $\omega^2 = 1.540\times10^{-6}\ \mathrm{s^{-2}}$, so the period is $2\pi/\omega = 5063$ s, or 84.4 min.
   - **Must contain:** The Hessian is four thirds pi G rho times the identity; The period is 84.4 minutes in every direction
   - **Numeric:** swing period = 84.4 min (magnitude, ±1%)

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Sign of the potential and of the tidal matrix | $\Phi = -GM/r$ and $\ddot{\boldsymbol\xi} = -(\nabla\nabla\Phi)\,\boldsymbol\xi$, the slow-motion, weak-field limit of the course geodesic deviation equation. | Geodesy often uses $V = GM/r$ and writes $+(\nabla\nabla V)\,\boldsymbol\xi$; some texts call $-\nabla\nabla\Phi$ the tidal tensor and others $+\nabla\nabla\Phi$. |

## Visuals

- ★ [[gap-between-two-falling-marbles]] (flagship): The central experience: two falling neighbours, their exact gap, and the prediction. *Sketch:* Two marbles near a planet, one above the other or side by side, with sliders for gap, height and time. The exact gap is plotted beside the deviation-equation prediction; enlarging the gap shows where they part.
- [[two-tilted-orbits-crossing]] (core): The sideways swing as two tilted orbits. *Sketch:* Two equal circles around a planet, one tilted by a small adjustable angle, a pebble on each. One lap shows the gap closing at a crossing and reopening on the other side, beside a cosine plot.

## Tutor moves

**Open with**

- Picture a capsule falling freely down a tall tube, with two marbles floating inside, one a metre above the other. While the capsule falls, will the gap between the marbles stay exactly the same? *(prediction)*

**If the learner is stuck**

- *The learner mixes up the pull on each object with the difference between the pulls.* → Make both pulls exactly equal first and show that the gap stays fixed, then add a tiny extra pull on one marble. *Uses:* `ways_in/ride-along-and-measure-the-gap`

**Common questions**

- *Does the Moon stretch my body the way it stretches the oceans?* (entry) Yes, but far too little to feel. The difference in pull is in proportion to the gap, and you are tiny compared with Earth. Earth's own pull differs between your head and feet about 18 million times more than the Moon's does, and nobody feels even that. *Uses:* `ways_in/twice-the-gap-twice-the-difference`

**Switching levels**

- To working when: asks for the equation; starts using derivatives or vectors. Derive the equation by subtraction, then solve it for a point mass. *Uses:* `derivations/subtract-two-equations-of-motion`, `worked_examples/swing-period-of-neighbouring-orbits`
- To formal when: asks when the approximation fails; asks how the equation becomes geometry. State the exact variational equation and the error bound, then the trace and volume results. *Uses:* `ways_in/linearized-flow-and-its-limits`, `checks/trace-free-cloud-volume`

**Pronunciations:** Newtonian → new-TOE-nee-un; Hessian → HESH-un; Poisson → pwah-SOHN; eötvös → UHT-vuhsh; GOCE → GO-chay

**Voice notes:** Say 'gap' at the entry rung and 'separation' above it.

## History

- **Isaac Newton (1687).** Explained the tides by how the pulls of the Moon and of the Sun differ between Earth's centre and its oceans. Isaac Newton (1687), *Philosophiae Naturalis Principia Mathematica*, Royal Society, London
- **George William Hill (1878).** Treated the Moon's motion about Earth in rotating axes, keeping the difference between the Sun's pulls on the Moon and on Earth to first order in their separation. George William Hill (1878), *Researches in the lunar theory*, American Journal of Mathematics 1, 5–26, doi:10.2307/2369430

## Review: novice

**Verdict:** fixed (2026-09-13, revision 8)

**Retell attempt:** Second full novice read, of the revision 5 text; the first read's retelling is kept at the end of this field.

If you ride a capsule down a tall tube with the air pumped out, you and two marbles all fall together, so the marbles float in front of you. Gravity is not switched off: Earth still pulls, and it pulls a little harder on the lower marble, because that marble is nearer Earth's centre. So the lower marble gains speed a little faster and the gap grows, but only by about three hundredths of a millimetre in a five-second drop, half the width of a hair, which is why nobody notices. A pull the two marbles share does nothing; only the difference between the pulls matters.

How big is that difference? Earth's centre is 6,371,000 metres below the ground, so a marble one metre lower is nearer by one part in 6,371,000, and because gravity goes with the square of the distance the pull is stronger by twice that, about one part in 3.2 million. I had to reread the 0.99 sentences: 'the pull grows by one over 0.99' sounded like adding 1.01 to the pull rather than multiplying by it, and in 'it does so twice' I could not say what 'it' and 'so' stood for. Double the gap and the difference doubles, so a wider gap widens faster and faster, and the rule that links gap and difference is the Newtonian deviation equation. The rule only works for small gaps, but I could not follow 'Being nearer by one half,' because it reads as if the rule is the thing that is nearer, and it never says one half of what. Then comes a rule for any round body, and I reread 'being a small gap nearer its centre makes its pull stronger', because a gap is the space between two things, so nothing in the sentence is doing the being, and each 'its' could be the body or the object. With that rule the Moon beats the Sun: the Sun pulls about 180 times harder but is about 390 times farther away, and 180 divided by 390 is about one half, so the Moon's difference in pull across Earth is about twice the Sun's.

Then two pebbles orbiting side by side at the same height. Both pulls point at Earth's centre, like two neighbouring spokes of a wheel, so each pull points slightly toward the other pebble and the two are drawn together, harder the wider the gap, like a stretched spring. Their orbits are two equal hoops sharing a centre, one tilted slightly, crossing at two points half a lap apart. The pebbles reach a crossing after a quarter lap, about 23 minutes, and slip past because one started a tiny bit ahead; after half a lap the gap is as wide as at the start, with the pebble that started on the left now on the right, facing the way they travel; after a full lap they are back where they started.

Against the takeaways: the first comes back whole. The second comes back as 'twice the gap, twice the difference, and the gap sets the difference in pull', though the fraction rule cost me two rereads. The third comes back whole, spring and once-per-lap swing included. In the Sun-and-Moon check I met the same rule in a third wording, 'across a small gap pointing at a body, the body's pull changes by a fraction of itself', and could not tell at first whether a pull that 'changes' is the same thing as the 'difference in pull' of the summary; the sentence 'Its pull is 180 times bigger' also left me guessing whose pull.

First read, of the revision 1 text: Inside a capsule falling down a tube with no air, marbles float because everything falls together, not because gravity is gone. The lower marble is a bit closer to Earth, so it gets pulled harder and the gap grows, but only by half a hair's width. Then something about the pull getting stronger by twice a tiny fraction because of squaring; I did not see how 1.01 times 1.01 comes from being nearer, since nearer makes the distance smaller, not bigger. Doubling the gap doubles the difference, and a bigger gap widens faster, though I first thought 'pulled apart harder' meant the marbles push each other. The Moon's difference is twice the Sun's even though the Sun pulls harder, because the Sun is far away; I am not sure why the fraction is 390 times smaller, or why a difference in pull makes tides at all. Two pebbles side by side in orbit get drawn together because both pulls point at Earth's centre, and they swing past each other like tilted hoops, meeting after a quarter lap. I did not know what 'the lean' was, whose centre 'its centre' is, or which side 'the other side' is. Compared with the takeaways: the first takeaway comes back whole; the second comes back as 'twice the gap, twice the difference' but without seeing the gap set its own widening; the third comes back, but the reason for the pull toward each other is fuzzy.

**Stumbles (32)**

- “Two objects let go together and falling freely keep their gap unless gravity pulls on them differently.”: A sentence I had to reread: 'let go together and falling freely' reads as a broken list, and the summary runs to four sentences, more than the two or three allowed.
- “So the gap itself sets how hard the pair is pulled apart or together.”: 'The pair is pulled apart' sounds as if the objects push or pull on each other; the step 'bigger gap, bigger difference, faster change' is left implicit. The same wording is in the second way's takeaway.
- “and general relativity keeps its pattern.”: 'General relativity' is undefined for this reader, and 'keeps its pattern' is vague.
- “Picture a capsule falling down a tall tube with the air pumped out.”: A missing everyday number: how tall is a tube that gives a fall of almost five seconds?
- “The lower marble is a metre nearer Earth's centre, and Earth pulls harder on things nearer its centre.”: The claim that gravity changes with distance is given without a number or reason, and 'its' could be the marble's centre.
- “So the lower marble gains speed a little faster than the upper one, and the gap slowly grows.”: First what-if: marbles side by side are pulled equally hard, so a reader concludes their gap never changes, which is false.
- “A marble one metre lower is nearer the centre by one part in 6,371,000.”: A step left implicit: the distance was given in kilometres, and the fraction needs metres.
- “Gravity weakens with the square of the distance. Because of that squaring, being nearer by a tiny fraction makes the pull stronger by twice that fraction: 1.01 times 1.01 is about 1.02.”: 'Weakens with the square' is not unpacked, and the backing skips the step from being nearer (a smaller distance) to one over the distance growing, so 1.01 appears from nowhere.
- “This rule is the heart of the Newtonian deviation equation. The difference in pull changes the gap, and the gap sets the difference in pull.”: The new term arrives before the thing it names is described, and not in its own naming sentence.
- “a wider gap means a harder pull apart, so the gap widens faster and faster.”: 'A harder pull apart' suggests a force between the marbles; the thing that grows is the difference in pull.
- “The rule needs a gap much smaller than the distance to Earth's centre.”: A limit with no reason; the first what-if is a gap of thousands of kilometres.
- “The Sun is about 390 times farther away than the Moon, so that fraction is 390 times smaller.”: A step left implicit: the marble fraction was worked out for Earth's distance only, and nothing says the fraction is the gap divided by the body's distance. The sun-or-moon check and the Jupiter problem depend on this step.
- “The Sun pulls on Earth about 180 times harder than the Moon does.”: A surprising claim with no reason, since the Sun is so much farther away.
- “The Moon's difference in pull across Earth is therefore about twice the Sun's.”: The way ends without saying why a difference in pull has anything to do with tides, yet the Sun-and-Moon check, the Jupiter problem and the tides observation all assume it.
- “Like the capsule, each pebble falls freely.”: A surprising claim with no reason: there is some air at 400 kilometres, and orbiting does not look like falling.
- “Start the pebbles level with each other, halfway between the crossings, where the hoops are farthest apart.”: 'Level' is ambiguous here, since the pebbles are already at the same height; it is meant as 'neither ahead'. The same word is in the swing check.
- “Earth pulls each pebble toward its centre. Those two pulls meet at the centre, like two spokes of a wheel, so they lean toward each other. The lean grows in proportion to the gap.”: 'Its centre' could be the pebble's; pulls do not 'meet'; 'the lean' is an unfamiliar name for an unexplained thing; why it grows with the gap is not said; and 'difference in pull' now silently means a difference in direction, not strength.
- “The difference in pull draws the pebbles together, like a stretched spring.”: The spring comparison is left unexplained: what about a spring is alike?
- “Their gap is widest on the other side after half a lap. After one full lap it is back where it started.”: 'The other side' has no reference, 'widest' is not compared with the start, and 'it' could be the gap or a pebble.
- “Stretch two rubber bands around an orange so that they cross at a small angle.”: Bands off the orange's widest part do not model two equal orbits sharing a centre, and they slip.
- “so their gap swings back and forth, once per lap for neighbours in orbit.”: First what-if: two marbles side by side in the drop capsule are drawn together but hit the ground long before any swing, so the general sentence needs a scope.
- “so Earth pulls it a little harder. It gains speed a little faster than the upper marble”: Ambiguous 'it': Earth and the lower marble are both candidates.
- “Across a small gap, a body's pull changes by a fraction of itself. That fraction is in proportion to the gap divided by the body's distance.”: The entry ways never stated the fraction for a body other than Earth, and the gap must point at the body.
- “After 50 minutes, half a lap, they are 5 metres apart on the other side.”: 'The other side' has no reference, and the step from starting halfway between crossings to a quarter lap is skipped.
- “The biggest tides come around new and full Moon, when the Sun's difference in pull adds to the Moon's.”: A surprise with no reason: why do the two add at new and full Moon but not at half Moon?
- “The pull grows by one over 0.99, which is about 1.01, and it does so twice, because of the squaring.”: Second novice read. 'Grows by one over 0.99' reads as adding 1.01 to the pull, not multiplying by it, and in 'it does so twice' neither 'it' nor 'so' has a clear referent. I reread the paragraph to see that the pull is multiplied, and that the squaring is what makes it happen twice.
- “Be nearer by one part in a hundred, so your distance is 0.99 times as big.”: Second novice read. The imperative turns the reader into the falling object with no warning, in a way that is otherwise about marbles, and 'your distance' does not say from what.
- “Being nearer by one half, the rule predicts a pull twice as strong, but the true pull is four times as strong.”: Second novice read. The opening phrase attaches to 'the rule', so the sentence reads as if the rule is the thing that is nearer, and 'by one half' never says half of what. I reread it twice.
- “Outside any round body, being a small gap nearer its centre makes its pull stronger by a fraction: twice the gap divided by the distance to that centre.”: Second novice read. A gap is the space between two things, so nothing in the sentence is doing the being, and there is no partner to be nearer than; the two 'its' can each be read as the body or as the object being pulled. The Sun-and-Moon sentences that follow need the two objects named, because there the pair is Earth's centre and the ocean.
- “Across a small gap pointing at a body, the body's pull changes by a fraction of itself. ... Its pull is 180 times bigger.”: Second novice read. Two words for one idea: the summary, the ways, the Jupiter problem and the tides observation all say 'difference in pull', while this check says the pull 'changes', so I could not tell it was the same quantity. It is also a third wording of the round-body rule. And after 'the Sun's fraction', 'Its pull' left me guessing whose pull.
- “Its pull is at most one part in 90 of the Moon's, so its difference is at most one part in 90 times 1,500: one part in 135,000.”: Second novice read. 'One part in 90 times 1,500' can be read as one part in 90, multiplied by 1,500, or as one part in 135,000; I had to do the arithmetic to find out which was meant. The sentence also opens with 'Its' rather than naming Jupiter.
- “While it falls, will the gap between the marbles stay exactly the same?”: Second novice read. 'It' can be the capsule or a marble, and the nearest noun is the marbles.

**Fixes**

- Summary: three short sentences, removed the suggestion that the pair pulls on itself, and replaced 'general relativity keeps its pattern' with 'Einstein's theory of gravity uses a rule of the same shape'.
- Ride-along way: gave the tube a height (about 110 metres, checked: a 4.7 second fall from rest covers 108 metres), backed 'weaker farther away' with the Moon-distance number (Earth's pull there is about 3,600 times weaker, from 60.3 squared), repeated the noun for the lower marble, and added a one-line pointer for the side-by-side what-if to the orbit way.
- Twice-the-gap way: unpacked the inverse square with 'twice as far, a quarter as strong', and spelled out the nearer-by-a-fraction step (one over 0.99 is about 1.01, twice over gives about 1.02); converted kilometres to metres; moved the term to its own naming sentence after the idea; replaced 'harder pull apart' with 'bigger difference in pull'; backed the small-gap limit with the half-distance case (rule gives twice, true pull four times); stated the general fraction 'twice the gap divided by the distance', which the sun-or-moon check and Jupiter problem need; and gave the Sun's bigger pull a reason. The link from difference in pull to tides, through the capsule picture, went into the tides observation rather than the way, so the way keeps one idea and the entry explanations stay within the review allowance. Recap now restates why the lower marble is pulled harder.
- Orbit way: stated the thin-air idealization, replaced the 'lean' of the pulls with equal strength but different directions along two spokes, gave the reason the sideways part grows with the gap, said explicitly that a difference in direction is a difference in pull, explained the spring comparison, replaced 'level' with 'side by side, neither ahead', and gave 'the other side' a reference (facing the way the pebbles travel). Recap adds the spring fact. The try-it puts the bands on the orange's widest part. The takeaway is scoped to 'as long as they keep falling'.
- Checks: the capsule answer repeats the noun instead of 'it'; the Sun-and-Moon answer now uses 'twice the gap divided by the distance', matching the way; the swing check says 'side by side, neither ahead', makes the quarter-lap step explicit and gives sides a reference, with key points updated.
- Tides observation: now opens with why a difference in pull raises tides (Earth and ocean fall freely toward the Moon together), and gives the reason spring tides come at new and full Moon (Sun, Earth and Moon nearly in a line).
- Ladder: the working way 'Subtract two falls and expand' now bridges entry words to symbols (difference in pull per unit mass becomes the relative acceleration, the gap becomes the separation vector) and ties the radial eigenvalue back to the entry 'twice the fraction' rule ($GM/r^2$ grows by $2\xi/r$). The gradiometer and formal ways already name the way they continue; index notation appears only at the formal rung. The six ways use four kinds and answer different questions.
- Budget: entry explanations were held within the 1,100-word review allowance by placing the tides link in the observation and not adding a building comparison or a 'small example' lead-in; no existing item was dropped.
- Bumped the revision to 2.
- Second full novice read, 2026-09-13, on revision 5: seven entry stumbles recorded and fixed. The rest of the entry reading (the ride-along way, the orbit way, the capsule and swing checks, the tides observation, the glossary, the objectives, the misconceptions and the common question) came back without a reread.
- Twice-the-gap way: the 0.99 paragraph now says the pull is multiplied by one over 0.99 and that the squaring makes that happen twice; the hypothetical object is a marble instead of the reader; the small-gap limit reads 'For a gap of half that distance' instead of the dangling 'Being nearer by one half'; and the round-body rule now names two objects a small gap apart and says which one is pulled harder. The claims are unchanged.
- Sun-and-Moon check: question, answer, hints, key points and the numeric label now say 'difference in pull' throughout, matching the summary and the ways, and the answer states the round-body rule in the way's own words. 'Its pull is 180 times bigger' became 'the Sun's pull is 180 times bigger'. The numbers and the answer 'about twice' are unchanged.
- Misconception bigger-pull-bigger-tides: 'change in pull' became 'difference in pull', the note's one word for this idea.
- Jupiter problem: the hint and the first solution step use 'difference in pull' and the fraction 'twice the gap divided by the distance', matching the way; the last step names Jupiter and spells out the two factors instead of 'one part in 90 times 1,500'.
- Opening question: 'While it falls' became 'While the capsule falls'.
- Budget: entry way explanations were 1,089 words before and are 1,100 after, exactly the 1,000-word foundation cap plus the 10% review allowance. To pay for the four entry rewrites, 'so your distance' became ': its distance' and 'is then multiplied' became 'is multiplied'; no entry sentence was compressed and no item was dropped. The check, misconception and problem rewrites are longer than the text they replace and leave support at 1,219 of 1,500 and tutoring at 1,807 of 2,200.
- Bumped the revision to 6.

**Concerns**

- All twelve learner-visible strings changed by this read are entry text, and the physics review last covered revision 5, so the revision needs a physics diff check before the status returns to physics-reviewed. Two rewritten statements carry the physics: 'Outside any round body, take two objects a small gap apart, one nearer the centre. The body pulls harder on the nearer object, by a fraction: twice the gap divided by the distance to that centre.' and 'For a gap of half that distance, the rule predicts a pull twice as strong, but the true pull is four times as strong.' Both were meant to restate, not change, the revision 5 claims. The rewritten sun-or-moon answer and Jupiter solution keep every number.
- The entry way explanations now sit at 1,100 words, exactly the review allowance over the 1,000-word foundation cap, so any further entry addition must be paid for by a cut. As earlier reviews noted, the orbit way carries both the spoke picture and the tilted-hoops timing; splitting the timing into its own entry way is the cleanest place to make room if a later read finds the way heavy. On this read the two pictures were one scene answering one question, so the way was left whole.
- The prerequisite notes newtonian-tidal-tensor and taylor-series still do not exist anywhere under knowledge/concepts, so the entry glossary and the phrases 'difference in pull' and 'gap' could not be checked against them. When they are written, align their entry rungs with this note, and make newtonian-tidal-tensor derive the point-mass Hessian in the same sign convention, since key_equations/point-mass-hessian is justified by it.
- Registry drift: the note lists poisson-equation-for-gravity as a formal prerequisite and the registry does not. Run knowledge/_tools/sync_registry.py.
- The course conventions still fix no symbol or sign for the Newtonian tidal matrix, so newtonian-tidal-tensor and relativistic-tidal-tensor can drift from this note's H = grad grad Phi with xi-double-dot = -H xi. Still open at the conventions file; not a novice-review matter.
- Both visuals are proposals with sketches only. Their tours should say 'side by side' with 'one a tiny bit ahead', name sides as 'facing the way the pebbles travel', and use 'difference in pull' rather than 'change in pull'.

**Re-read** (2026-09-13, revision 4): 8 stumbles in 9 changed passages

- “Start the pebbles side by side, neither ahead of the other, halfway between the crossings. ... With one pebble a hair ahead, they slip past each other, and the gap opens on the other side.”: Contradiction inside one way: the start paragraph says neither pebble is ahead, and three paragraphs on one pebble is suddenly a hair ahead. The reader rereads to find when that happened.
- “a hair ahead”: Rule 5, one word in two senses: the ride-along way uses 'the width of a hair' as a real measurement (half the width of a hair), while 'a hair ahead' is an idiom for an unstated tiny amount.
- “They start side by side, 5 metres apart, with one only a hair ahead so they cannot bump, halfway between the two points where their orbits cross.”: One sentence carries the start position, the offset and its purpose, with the place split off after the 'so' clause; the reader rereads to learn where they start.
- “After 25 minutes, a quarter lap, they reach it together, just miss each other, and slip past.”: Step taken on trust in a check answer: why do they just miss rather than bump? The link to the tiny head start is missing, and 'together' clashes with one being ahead.
- “They gain speed toward each other as the gap closes, so tiny pebbles that just miss each other slip past.”: The 'so' links gaining speed to slipping past, but the inserted 'that just miss each other' reads as the reason; the missing step is that they do not stop.
- “So the Moon's pull can move the ocean compared with the ground only through the difference in pull across Earth, and that difference raises the tides.”: A 26-word sentence with 'can ... only through' that must be reread; it does not reuse the ride-along way's words 'a pull they share cannot change the gap'.
- “Outside any round body, a small gap pointing at its centre changes the strength of its pull by a fraction: twice the gap divided by the distance to that centre.”: 'A gap pointing at its centre' is an unfamiliar picture, and 'changes the strength' does not say from where to where; the paragraph on 1.01 times 1.01 phrased the same rule as being nearer making the pull stronger.
- “the pull $GM/r^2$ is weaker by the fraction $2\xi/r$ on a neighbour $\xi$ farther out.”: Working rung: 'a neighbour $\xi$ farther out' reads as naming the neighbour $\xi$ rather than giving its distance.
- Fix: Orbit way: the start now places one pebble a tiny bit ahead, replacing 'neither ahead of the other', and the pass-through sentence gives the head start as the reason they slip past without bumping.
- Fix: Replaced the idiom 'a hair ahead' with 'a tiny bit ahead' in the orbit way and the swing check, because 'hair' is a real width in the ride-along way.
- Fix: Swing check: split the question's start sentence in two, and the answer now says why the pebbles just miss each other.
- Fix: Misconception correction: made the 'do not stop' step explicit.
- Fix: Tides observation: split the scoped sentence into two, reusing 'a pull they share' wording from the ride-along way; claim and scope unchanged.
- Fix: Twice-the-gap way: the round-body rule now says being a small gap nearer the centre makes the pull stronger by the fraction, in the words of the 1.01 paragraph. Still outside any round body, with the same fraction.
- Fix: Working way: 'a neighbour a distance $\xi$ farther out'.
- Fix: Budget: these fixes added 5 entry-explanation words to a note already at 1,098 of the 1,100 allowance. To make room, dropped the lowest-value sentence 'For a huge gap, "twice the fraction" is far off.', since the next sentence's half-distance example shows the same point with numbers.
- Fix: Takeaway 'For neighbours in orbit, their gap swings back and forth, once per lap.' read without a wording stumble; its scope is raised in the summary rather than edited.
- Fix: Bumped the revision to 4.

**Re-read** (2026-09-13, revision 5): 0 stumbles in 2 changed passages


**Re-read** (2026-09-13, revision 8): 5 stumbles in 3 changed passages

- “That is why the marbles float.”: Wording squeezed to fit the entry budget, and the measurer went with the words. Floating is a comparison, and the tube has just had its air pumped out, so the first question is 'float in what?'. The sentence names nothing the marbles float in front of, and the whole point of the way is that they hold still for you while both of you rush down the tube.
- “The fall lasts almost five seconds, and each marble reaches about 167 kilometres an hour past the tube.”: Reread. 'past the tube' arrives after the unit, so on the first pass it reads as part of the speed, as if 167 kilometres an hour were being measured past something that is itself moving. The measurer is the right one; it is standing where the arithmetic ends.
- “But take the same gap for both, from Earth's centre to the ocean facing each body.”: Wording squeezed to fit the entry budget: 'the ocean on the side facing each body' lost 'on the side', so the reader has to supply which part of the ocean is meant, in the one sentence that sets up the whole Sun-and-Moon comparison.
- “Outside any round body, take two objects a small gap apart on a line to its centre.”: Read twice. The sentence hands over two conditions at once, that the gap is small and that both objects sit on a line to the centre, and 'its' comes four nouns after 'body'.
- “The same rule compares the Sun and the Moon. Outside any round body, take two objects a small gap apart on a line to its centre. ... So the Moon's difference in pull across Earth is about twice the Sun's.”: Rule 17, a way asking the reader to hold two new ideas at once. The way's question, how big the difference in pull is across a small gap, is already answered with the marbles. This closing paragraph then adds a second new idea in a second scene: a general rule for any round body, and a comparison of two bodies with three fresh numbers, 180, 390 and one half, whose subject is tides rather than marbles. Both changed sentences sit in that paragraph, which is why it was read as a whole.
- Fix: Ride-along way, the float sentence: restored the measurer as 'That is why the marbles float in front of you', and paid for it by dropping the same phrase from the release sentence, which now reads 'let go of two identical marbles, one a metre above the other'. Net zero words, the repetition the phrase used to cause is gone, and the reference now stands in the sentence that needs it. Nothing about the scene changed.
- Fix: Ride-along way, the speed sentence: 'about 167 kilometres an hour past the tube' became 'about 167 kilometres an hour relative to the tube'. Same frame, same number, same claim; the phrase now reads as a frame instead of trailing the unit. One word.
- Fix: Read and left as written: 'Above the ground, gravity weakens with the square of the distance from Earth's centre', where the new scope reads plainly and the next sentence unpacks the square; and 'Outside any round body, take two objects a small gap apart on a line to its centre', where the restored direction condition is exactly what the fraction needs.
- Fix: Nothing was dropped and no sentence was compressed. Entry way explanations now stand at 1,100 words, the 1,000-word foundation cap plus the whole 10 per cent review allowance. The two rewrites left unapplied, 'on the side facing each body' and 'on a line to the body's centre', need a cut before they can be made; splitting the Sun-and-Moon paragraph into its own entry way is still the cleanest one.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 8)

**Verification**

- Deviation equation: subtracting x'' = -grad Phi(x) from the neighbour's equation at equal t and expanding to first order gives xi'' = -(grad grad Phi) xi.: Re-derived the five derivation steps by hand; checked that the shared field cancels and that the Hessian is symmetric for a C^2 potential. → Correct, with O(|xi|^2) remainder.
- Point-mass Hessian (GM/r^3)(1 - 3 r-hat r-hat^T), eigenvalues -2GM/r^3 radial and +GM/r^3 transverse.: Hand differentiation of -GM/r: d_i d_j(-1/r) = delta_ij/r^3 - 3 x_i x_j/r^5. → Correct; radial xi'' = +2GM xi/r^3 grows (cosh), transverse xi'' = -GM xi/r^3 oscillates (cos).
- Working bridge: radial eigenvalue is the entry 'twice the fraction' rule.: GM/r^2 - GM/(r+xi)^2 = (GM/r^2)(2xi/r) to first order. → The old wording 'the pull grows by the fraction 2xi/r' had the wrong sign for a neighbour farther out; fixed to 'is weaker by the fraction 2xi/r on a neighbour xi farther out'.
- Second-order term is about (3/2)|xi|/r of the kept term; formal ell = ||H||/M3 = r/3 for a point mass.: Series 2x - 3x^2; python3 maximum of |9c - 15c^3| on [-1,1] is 6, so M3 = 6GM/r^4 and ||H|| = 2GM/r^3. → Consistent: (1/2)M3 xi^2 over 2GM xi/r^3 = (3/2) xi/r; ell = r/3.
- Formal template: Gamma^i_tt = d_i Phi gives R^i_tjt = d_i d_j Phi in the course Riemann convention, and the course geodesic deviation equation with u = d_t gives xi'' = -H xi.: Evaluated R^rho_sigma mu nu = d_mu Gamma^rho_nu sigma - ... with rho=i, sigma=t, mu=j, nu=t; quadratic terms vanish since only Gamma^i_tt is nonzero; D/dt reduces to d/dt because Gamma^i_tj = 0 and xi^t = 0. → Correct, sign included.
- theta = D' D^-1 obeys theta' = -H - theta^2; (ln V)'' = -4 pi rho - tr theta^2 (G = 1); vacuum release at rest gives V/V0 = 1 - (1/2)(GM/r^3)^2 t^4.: Differentiated theta; Jacobi's formula; showed D^T D' is conserved and zero, so theta is symmetric and tr theta^2 >= 0; python3 compared cosh(sqrt2 x)cos^2 x with 1 - x^4/2 at x = 0.1, 0.3. → Correct (0.99995013 vs 0.99995; 0.99605 vs 0.99595). Leading t^4 term unaffected by H varying along the path.
- Hill equations x'' - 2n y' - 3n^2 x = 0, y'' + 2n x' = 0, z'' + n^2 z = 0.: Hand computation of -2 Omega x xi' = (2n y', -2n x', 0) and -Omega x (Omega x xi) = (n^2 x, n^2 y, 0) added to n^2(2x, -y, -z). → Correct; matches the standard Clohessy-Wiltshire/Hill form.
- Drop tower: 110 m tube, fall almost five seconds, about 166 km/h, 1 m gap grows by about three hundredths of a millimetre (half a hair).: python3: 0.5 g (4.7 s)^2 = 108 m; g t = 166 km/h; (cosh(sqrt(2GM/R^3) 4.7) - 1) x 1 m = 0.034 mm. → Correct.
- Drop-tower problem: GM/r^3 = 1.541e-6 s^-2; growth 6.81e-5 m, shrink 3.40e-5 m; next terms ~6e-6; 108 m drop changes GM/r^3 by 5e-5.: python3. → All values reproduce (6.810e-5, 3.405e-5, 5.7e-6, 5.1e-5). Earth rotation affects the Hessian by Omega^2/(GM/R^3) = 0.3 percent, inside the 3 percent tolerance.
- Earth's pull at the Moon's distance about 3,600 times weaker; one metre nearer is one part in 6,371,000; pull stronger by two parts, about one in 3.2 million; 1/0.99 ~ 1.01, squared ~ 1.02; nearer by one half gives rule 2x vs true 4x.: python3: (d/R)^2 = 3640; 3,185,500; 1.0101, 1.0203; 1/(0.5)^2 = 4. → Correct.
- New entry sentence: outside any round body, a small gap pointing at its centre changes the strength of its pull by a fraction, twice the gap divided by the distance to that centre.: First-order expansion of GM/r^2 for a spherically symmetric body, radial gap. Counterexamples: inside a uniform ball the pull grows outward; a sideways gap changes direction, not strength. → The novice wording 'changes its pull by twice the gap divided by the distance' read as a change equal to a pure number and had no 'outside' condition. Fixed; true within the stated scope.
- Sun pulls Earth about 180 times harder than the Moon, is about 390 times farther, so the Moon's difference in pull is about twice the Sun's (check value 2.2, rel_tol 0.15).: python3 with GM_sun = 1.32712e20, GM_moon = 4.9028e12, d = 3.844e8 m, D = 1.496e11 m. → Force ratio 178.7, distance ratio 389.2, Moon/Sun tidal 2.18. Correct.
- Tides observation: Moon's difference in pull across Earth about one nine-millionth of g; Sun's a little under half; high tide about 50 minutes later each day; spring tides near new and full Moon.: python3: 2 GM_moon R/d^3 = 1.10e-6 m s^-2, g/that = 8.93 million; Sun/Moon 0.459; lunar day 24 h 50 min. → Correct. The sentence 'only the difference in pull across Earth can move the ocean' was unscoped (winds and the Sun also move the ocean); now scoped to the Moon's pull.
- Jupiter problem: pull at most about 1/90 of the Moon's, at least about 1,500 times farther, so difference at most 1 part in 135,000 (7.4e-6, rel_tol 0.15).: python3 with GM_J = 1.26687e17 and minimum distance (4.950 - 1.017) AU = 588 million km. → Force ratio 1/90.7, distance ratio 1531, tidal ratio 7.2e-6; within tolerance. Correct.
- Orbit way and worked example: 400 km orbit takes about 92 minutes, quarter lap about 23 minutes; r = 6771 km gives omega = 1.133e-3 s^-1, 5545 s = 92.4 min, meet at 23.1 min; cross-orbit entry GM/r^3 equals the orbital angular velocity squared.: python3; circular orbit v^2/r = GM/r^2. → Correct.
- Spoke picture: each pull has a part toward the other pebble in proportion to the gap, producing a spring-like relative acceleration.: Each radial line makes angle xi/(2r) with the midline, so each pull has a component GM xi/(2r^3) toward the other; relative acceleration GM xi/r^3, matching the transverse Hessian eigenvalue. → Correct in sign and size.
- After half a lap, facing the way the pebbles travel, the pebble that started on the left is on the right.: With head away from Earth, left of travel is r-hat x v-hat = the fixed orbit normal n; xi = xi0 cos(omega t) n changes sign at half a lap. With head toward Earth both lefts flip, so the swap still holds. → Correct and independent of the observer's head direction.
- Swing check: 100-minute laps, meet after 25 minutes, 5 metres apart again after 50 minutes (numeric 25 min, rel_tol 0.05).: Quarter and half of 100 minutes; cos(omega t) zero at pi/2. → Correct.
- Near-side/far-side check: x = 0.01657; exact/first-order 1.0254 and 0.9757; ratio 1.051; neglected term about 2.5 percent.: python3. → 1.02542, 0.97568, 1.05098, 1.5x = 0.0249. Correct, within abs_tol 0.003.
- Pass-through planet: Hessian (4/3) pi G rho times identity; omega^2 = 1.540e-6 s^-2; period 5063 s = 84.4 min.: Enclosed mass gives field (4/3) pi G rho r; python3 with rho = 5510 kg m^-3. → omega^2 = 1.5404e-6, 5062.5 s = 84.38 min. Correct; trace 4 pi G rho matches Poisson.
- GOCE: 2009-2013, about 255 km, three orthogonal 0.5 m arms of accelerometer pairs; radial 2GM/r^3 at r = 6626 km is 2.74e-6 s^-2 (2740 E), relative acceleration 1.37e-6 m s^-2 across 0.5 m.: python3; ESA mission pages (launched 11 March 2009, re-entered 11 November 2013; six accelerometers on three 0.5 m baselines; about 250-255 km altitude). → Correct. Sign consistent with entries of -grad grad Phi, and with geodesy's +V_zz.
- Common question: Earth's head-to-feet difference in pull is about 18 million times the Moon's.: python3: (M_E/M_moon)(d/R)^3 = 1.79e7 using d; 1.70e7 using d - R. → Correct to 'about'.
- Notation trap: geodesy's V = GM/r with +(grad grad V) xi; course -(grad grad Phi) xi with Phi = -GM/r.: V = -Phi. → Consistent. The course conventions still fix no symbol for the Newtonian tidal matrix (concern).
- Reference: R. Rummel, W. Yi, C. Stummer, 'GOCE gravitational gradiometry', Journal of Geodesy 85, 777-790 (2011).: Web search, Springer record. → Confirmed; added doi 10.1007/s00190-011-0500-0; verified.
- Reference: G. W. Hill, 'Researches in the lunar theory', American Journal of Mathematics 1, 5-26 (1878).: Web search, JSTOR record 2369430. → Confirmed (first of three parts, continued at 129-147 and 245-260); added doi 10.2307/2369430; verified.
- Reference: D. E. Cartwright, Tides: A Scientific History, Cambridge University Press, 1999.: Web search: publisher pages and 1999 reviews (ISBN 0-521-62145-3). → Confirmed; no book DOI found; verified.
- Reference: I. Newton, Philosophiae Naturalis Principia Mathematica, London, 1687, under the imprimatur of the Royal Society.: Standard bibliographic record. → Confirmed; verified.
- History scope: Newton explained tides by the difference in the Moon's and Sun's pulls across Earth; Hill treated the lunar motion in rotating axes with the solar perturbation kept to lowest order in the Earth-Moon separation.: Checked against the content of the Principia tidal propositions and Hill's 1878 formulation (Hill's problem). → Newton's wording 'the difference between the Moon's and the Sun's pulls' misread as Moon minus Sun and Hill's 'keeping the Sun's pull to first order' was imprecise; both rescoped.
- Second physics review, revision 6, of the twelve entry strings the second novice read changed. Round-body rule as rewritten: 'Outside any round body, take two objects a small gap apart, one nearer the centre. The body pulls harder on the nearer object, by a fraction: twice the gap divided by the distance to that centre.': The fraction 2d/r is the first-order change of GM/r^2 along the radius. For a gap of the same size d laid across the radius instead, both objects sit at the same distance from the centre to first order, so the strengths differ only at order (d/r)^2 and the stated fraction is wrong by 100 per cent. python3 at R = 6.371e6 m, d = 1 m: radial (R/(R-d))^2 - 1 = 3.13923e-7 against 2d/R = 3.13922e-7; sideways (R/sqrt(R^2 - d^2))^2 - 1 = 2.5e-14, not 3.1e-7. → The revision 5 wording carried the condition ('a small gap pointing at its centre'); the novice rewrite dropped it, so as written the sentence was false for a sideways gap, which is the very case the orbit way treats. Fixed to 'take two objects a small gap apart on a line to its centre', which also matches the wording already in checks/sun-or-moon ('on the line to a body').
- Entry inverse-square sentence: 'Gravity weakens with the square of the distance from Earth's centre.': True outside a spherically symmetric body. Counterexample from this note's own formal rung, checks/pass-through-planet: inside a uniform ball the pull is (4/3) pi G rho r, so it grows with the distance from the centre and vanishes at the centre, while the sentence as written predicts it growing without limit. A teenager's first what-if here is a hole dug toward the centre. → Scoped to 'Above the ground, gravity weakens with the square of the distance from Earth's centre.' The two sentences that follow (twice as far, a quarter as strong; the marble at 0.99 of the distance) are unaffected and stay correct.
- Drop tower: a tube about 110 metres tall, a fall of almost five seconds, and 'about 166 kilometres an hour'.: python3 with g = GM/R^2 = 9.820 m s^-2: a 110 m fall from rest takes 4.733 s and ends at 46.48 m s^-1 = 167.3 km/h. The 166 km/h of the first physics review came from t = 4.70 s, which is the 108 m of problems/drop-tower-pair, not the 110 m tube the way states. → Corrected to 'about 167 kilometres an hour', so the entry numbers all follow from the stated 110 metres. The gap growth is unchanged: cosh(sqrt(2GM/R^3) t) - 1 times 1 m is 0.0345 mm at 4.733 s and 0.0340 mm at 4.70 s, both 'about three hundredths of a millimetre'. The earlier verification entry that recorded 166 km/h as correct is superseded by this one.
- Same sentence, measurer: 'each marble speeds up to about 167 kilometres an hour' did not say relative to what.: Relative to the capsule each marble stays within 0.035 mm of its starting place over the whole fall, so the speed only means anything against something outside the capsule. This is the distinction the whole note rests on. → Named the reference: 'each marble reaches about 167 kilometres an hour past the tube'. To pay for the words at an entry rung already at its review allowance, the repeated 'in front of you' was dropped from 'That is why the marbles float in front of you' (the phrase appears two sentences earlier) and 'on the side facing each body' became 'facing each body', matching checks/sun-or-moon. Entry explanations went from 1,100 to 1,099 words.
- Sun and Moon: pull ratio about 180, distance ratio about 390, so the Moon's difference in pull across Earth is about twice the Sun's (checks/sun-or-moon numeric 2.2).: python3 with M_sun 1.989e30 kg at 1.496e11 m and M_moon 7.342e22 kg at 3.844e8 m: force ratio 178.9, distance ratio 389.2, tidal ratio (M/d^3) 2.176. 180/390 = 0.462. → Correct; 2.176 sits inside the 15 per cent tolerance on 2.2, and 'about one half' and 'about twice' are both right.
- Jupiter problem: pull at most about one ninetieth of the Moon's, at least about 1,500 times farther, answer 7.4e-6 of the Moon's difference in pull.: python3 with M_J 1.898e27 kg at 4.2 au and the Moon at apogee 4.055e8 m: force ratio 0.01077 = 1/92.9, distance ratio 1549. (1/90)/1500 = 7.41e-6. The true mean-distance ratio of M/d^3 is 5.9e-6, below the bound, as an 'at most' answer requires. → Correct, and the stated bounds are genuine bounds rather than mean values.
- Orbit way, worked example and swing check: 400 km orbit about 92 minutes, quarter lap about 23 minutes, r = 6771 km gives omega = 1.133e-3 s^-1 and 5545 s; 100-minute laps give 25 and 50 minutes.: python3: T = 2 pi sqrt(r^3/GM) = 5544.9 s = 92.41 min, quarter 23.10 min. Cross-track motion: two equal circular orbits inclined by i have separation r i sin(theta) from the node, so starting at maximum gives r i cos(omega t), zero at a quarter lap and reversed at half a lap. The out-of-plane Hill equation z'' = -n^2 z has exactly the orbital frequency. → Correct, including 'one swing per lap' and the reversal at half a lap.
- 'Facing the way the pebbles travel, the pebble that started on the left is now on the right.': Orbit 1 in the xy-plane, orbit 2 inclined by i about the x-axis; separation (0, 0, r i sin theta) to first order in i. Taking left = up x forward with up the radial direction away from Earth: at theta = 90 degrees, r-hat x v-hat = +z-hat, so pebble 2 is on the left; at theta = 270 degrees the velocity has reversed but r-hat x v-hat is again +z-hat while the separation is -z-hat, so pebble 2 is on the right. → Correct. The sides do swap. The sentence fixes the facing but not the walker's up; the claim is well defined only with up taken away from Earth, and it is then true. Left as written, because the alternatives ('with Earth below you') hit the guide's wording trap about up and down for someone in free fall.
- Deviation equation, point-mass Hessian and the working bridge, re-derived from scratch.: Subtracting x'' = -grad Phi(x) from (x + xi)'' = -grad Phi(x + xi) and expanding gives xi'' = -(grad grad Phi) xi + O(|xi|^2). d_i d_j(-GM/r) = (GM/r^3)(delta_ij - 3 r-hat_i r-hat_j), eigenvalues -2GM/r^3 radial and +GM/r^3 transverse, so xi'' = +(2GM/r^3) xi radially and -(GM/r^3) xi transversely. Second-order term relative to first: f = -GM/r^2 has f' = 2GM/r^3 and f'' = -6GM/r^4, ratio (1/2)|f''| xi / |f'| = (3/2) xi/r. → All correct and in the course sign convention; the entry 'twice the fraction' rule is the radial eigenvalue.
- Formal way: exact variational equation, error length ell = r/3, theta equation and volume, rotating-frame terms, Newton-Cartan template.: ||grad grad Phi|| = 2GM/r^3 and M_3 = 6GM/r^4 give ell = r/3. D'' = -HD with theta = D'D^-1 gives theta' = -H - theta^2, and Jacobi's formula gives (ln V)'' = -tr H - tr theta^2 = -4 pi rho - tr theta^2 with G = 1. Rotating frame: -2 Omega x xi' and -Omega x (Omega x xi) are the standard Coriolis and centrifugal terms, both linear in xi. Newton-Cartan: with Gamma^i_tt = d_i Phi the only nonzero symbols, the course Riemann formula gives R^i_tjt = d_j Gamma^i_tt = d_i d_j Phi (the quadratic terms vanish), and the course geodesic deviation D^2 xi^mu/dtau^2 = -R^mu_{nu rho sigma} u^nu xi^rho u^sigma with u = d_t returns xi'' = -H xi. → All correct, signs included.
- Symbol clash at the formal rung: the Taylor remainder was written $\mathbf r$ while $\hat{\mathbf r}$ is the radial unit vector and $r$ is the radius in the same paragraph ('for a point mass $\ell = r/3$').: Course conventions, one symbol one meaning within a note. → Renamed the remainder to $\mathbf e$. No claim changed.
- Remaining numeric fields recomputed: drop-tower problem, near-side/far-side check, trace-free cloud volume, pass-through planet, GOCE, and the head-to-feet common question.: python3. GM/r^3 = 1.5414e-6 s^-2; growth 6.810e-5 m and shrink 3.405e-5 m for a 2.00 m gap in 4.70 s, next series term 5.7e-6 of the kept one, 3 dr/r = 5.1e-5 for a 108 m drop. x = R/d = 0.016574 gives 1.02542 and 0.97568, ratio 1.05098, and (3/2)x = 2.49 per cent. theta = -Ht gives ln V = -tr(H^2) t^4/12 = -(1/2)(GM/r^3)^2 t^4 for eigenvalues (-2, 1, 1). (4/3) pi G rho = 1.5404e-6 s^-2 and 2 pi/omega = 5063 s = 84.38 min. 2GM/r^3 at 6626 km = 2.740e-6 s^-2 = 2740 E, times 0.5 m = 1.370e-6 m s^-2. (2GM/R^3)/(2GM_moon/d^3) = 1.79e7. → Every value and tolerance confirmed.
- References re-confirmed for revision 7.: Web records: Hill, 'Researches in the Lunar Theory', American Journal of Mathematics 1(1), 5-26 (1878), JSTOR 2369430, doi 10.2307/2369430. Rummel, Yi and Stummer, 'GOCE gravitational gradiometry', Journal of Geodesy 85, 777-790 (2011), doi 10.1007/s00190-011-0500-0. Cartwright, 'Tides: A Scientific History', Cambridge University Press 1999, ISBN 0-521-62145-3. Newton, Philosophiae Naturalis Principia Mathematica, London 1687, printed by order of the Royal Society. → All four confirmed; verified stays true for each. History scope unchanged and accurate.

**Counterexamples tried**

- Tiny pebbles exactly side by side at the crossing: two finite pebbles arriving at the same point at the same moment bump, so 'they slip past each other' was false for the setup as stated. Fixed by putting one pebble a hair ahead in the orbit way and in the swing check; the tutor correction now says pebbles that just miss each other slip past.
- Radial fall from rest outside a point mass (marbles side by side in the drop capsule, if it kept falling): the transverse gap shrinks in proportion to the distance to the centre and never swings back. It broke the takeaway 'as long as they keep falling, their gap swings back and forth'; rescoped to neighbours in orbit.
- Inside a uniform ball (pass-through planet): the pull grows outward, so 'a small gap pointing at a body changes its pull by twice the gap over the distance' fails; the entry sentence now says 'outside any round body'.
- Sideways gap: changes the direction of the pull, not its strength; the entry fraction rule is scoped to a gap pointing at the centre, and the orbit way handles the sideways case separately. Survives.
- Huge gap (half the distance): the rule gives twice, the truth four times; the entry way already states it. Survives.
- Uniform field / free-falling frame: H unchanged, relative acceleration zero; matches 'a pull the two marbles share cannot change the gap'. Survives.
- Non-rotating vs rotating frame: Earth-fixed drop tower adds Omega^2 terms of 0.3 percent; GOCE's Earth-pointing rotation is named in the gradiometer way. Survives.
- Non-static release (cloud with initial vorticity): tr theta^2 could change sign; the formal claim and the check both specify release at rest. Survives.
- Elliptical tilted orbits: the cross-orbit gap still closes at the two crossings once per lap, so 'once per lap' survives; the working 'cos' solution is scoped to circular orbits.
- Other forces moving the ocean (winds, the Sun): 'only the difference in pull across Earth can move the ocean' was too broad; rescoped to the Moon's pull.
- Strong field / relativistic limit: the note says Newtonian throughout and defers to the geodesic deviation equation; formal template correct in the course sign convention. Survives.
- Second physics review. Sideways gap against the rewritten round-body rule: two objects a gap apart across the radius sit at the same distance from the centre to first order, so their pulls differ in strength only at second order. The rewritten sentence had lost the 'pointing at the centre' condition and was false for exactly this case; restored as 'on a line to its centre'.
- Second physics review. A hole dug toward Earth's centre against 'gravity weakens with the square of the distance from Earth's centre': inside a uniform ball the pull is proportional to the distance from the centre, as this note's own checks/pass-through-planet shows. Scoped to 'above the ground'.
- Second physics review. Two freely falling objects pushed apart against the summary's 'their gap changes only if gravity pulls on them differently': with a relative velocity the gap changes in a uniform field too. The word 'together' and every setup in the note (the marbles are let go, the pebbles start on circles) fix the relative velocity, and it is the relative acceleration the sentence is about. Survives; recorded because the sentence is the one a reader repeats.
- Second physics review. Earth's flattening against 'two equal hula hoops sharing a centre': the J2 field makes the orbital planes regress at rates that differ with inclination, so two tilted orbits drift apart over many laps. The way claims only one lap, over which the drift is negligible. Survives.
- Second physics review. Elliptical or unequal orbits against 'Both take about 92 minutes per lap': equal periods need equal semi-major axes, which the stated equal circular radius gives. Survives within the stated setup.
- Second physics review. A finite-size accelerometer against 'a single freely falling mass reads zero': a real instrument has extent and so senses gradients across itself. The sentence is about an idealized point mass, which is what the gradiometer's proof masses approximate. Survives.

**Fixes**

- Twice-the-gap way: 'For any round body, a small gap pointing at it changes its pull by twice the gap divided by the distance to its centre' became 'Outside any round body, a small gap pointing at its centre changes the strength of its pull by a fraction: twice the gap divided by the distance to that centre' (missing 'outside' condition; the old wording equated a change in pull to a pure number).
- Budget: dropped the sentence 'Triple the gap, and the difference triples.' from the twice-the-gap way, which repeats the doubling example, to keep entry explanations within the 1,100-word review allowance (now 1,098).
- Orbit way: 'They slip past each other' became 'With one pebble a hair ahead, they slip past each other', since exactly aligned pebbles would bump. Swing check question now starts the pebbles 'with one only a hair ahead so they cannot bump', and its answer says they 'just miss each other, and slip past'. Tutor correction for neighbours-meet-and-stay matches.
- Orbit way takeaway: removed the false general condition 'as long as they keep falling'; now 'For neighbours in orbit, their gap swings back and forth, once per lap.'
- Tides observation: scoped 'only the difference in pull across Earth can move the ocean' to the Moon's pull.
- Working way 'Subtract two falls and expand': corrected the sign of the bridge sentence to 'the pull GM/r^2 is weaker by the fraction 2xi/r on a neighbour xi farther out'.
- History: rescoped Newton's and Hill's contributions; all four references confirmed and set verified, with DOIs added for Hill and Rummel et al.
- Bumped the revision to 3 for the learner-visible changes; a novice re-read of exactly these changes is due.
- Second full physics review, 2026-09-13, on revision 6 (after the second novice read). Three entry corrections, one entry wording payment and one formal symbol fix; every equation re-derived and every number recomputed from scratch.
- Twice-the-gap way: restored the condition the novice rewrite dropped from the round-body rule, 'take two objects a small gap apart on a line to its centre'. Without it the stated fraction, twice the gap divided by the distance, is false for a sideways gap, which is the case the orbit way treats.
- Twice-the-gap way: scoped the inverse-square sentence to 'Above the ground', because inside Earth the pull grows with the distance from the centre, as checks/pass-through-planet states.
- Ride-along way: 'about 166 kilometres an hour' became 'about 167', which is what a 110 metre fall gives; 166 belongs to the 4.70 second, 108 metre fall of problems/drop-tower-pair. Named the reference for that speed, 'past the tube', since relative to the capsule each marble barely moves at all.
- Budget: entry explanations were at 1,100 words, the whole review allowance, so the added words were paid for by dropping the repeated 'in front of you' from 'That is why the marbles float in front of you' and by shortening 'the ocean on the side facing each body' to 'the ocean facing each body', which also matches checks/sun-or-moon. No sentence was compressed and no item was dropped; entry explanations are now 1,099 words.
- Formal way: the Taylor remainder $\mathbf r$ became $\mathbf e$, because $\hat{\mathbf r}$ and $r$ already mean the radial unit vector and the radius in this note.
- Bumped the revision to 7 for the two entry strings changed; a novice re-read of exactly these changes is due.

**Concerns**

- Entry way explanations are 1,098 words, just inside the 1,100-word review allowance, over the 1,000 foundation cap. Any further entry addition needs a cut; the orbit way (spoke picture plus hoop timing) is the natural candidate to split, as the novice reviewer noted.
- The course conventions fix no symbol or sign name for the Newtonian tidal matrix; the note uses H = grad grad Phi with xi'' = -H xi, consistent with the geodesic deviation row. Report to the conventions owner.
- Prerequisite notes newtonian-tidal-tensor and taylor-series do not exist yet; the point-mass Hessian is justified_by newtonian-tidal-tensor, which must derive it in the same sign convention when written. poisson-equation-for-gravity is in the registry but not yet a registry prerequisite of this concept; run sync_registry.py.
- The proposed visuals should start the orbiting pebbles a hair apart along track, matching the fixed swing check, and keep the tidal matrix sign of this note.
- Second physics review. Entry way explanations are 1,099 of the 1,100-word review allowance over the 1,000-word foundation cap, so the entry rung still has no room. Splitting the tilted-hoop timing out of 'Neighbours in orbit swing through each other' into its own entry way remains the cleanest way to make room, as both earlier stages said.
- Second physics review. 'Facing the way the pebbles travel, the pebble that started on the left is now on the right' fixes the facing but not the walker's up. It is true with up taken away from Earth, and no other choice makes it meaningful, but naming that up would use 'below' for someone in free fall, which the guide lists as a wording trap. Left as written; a visual tour can settle it by showing the view.
- Second physics review. The course conventions still fix no symbol or sign for the Newtonian tidal matrix. This note uses H = grad grad Phi with xi'' = -H xi, matching the course geodesic-deviation row; newtonian-tidal-tensor and relativistic-tidal-tensor can drift from it until the conventions file settles the choice. Reported, not invented, by every stage so far.
- Second physics review. newtonian-tidal-tensor and taylor-series still have no note under knowledge/concepts, so key_equations/point-mass-hessian is justified_by a note that does not exist. When newtonian-tidal-tensor is written it must give the point-mass Hessian as (GM/r^3)(1 - 3 r-hat r-hat) in this sign convention, and its entry rung must use 'gap' and 'difference in pull'.
- Second physics review. Registry drift is unchanged: the note lists poisson-equation-for-gravity as a formal prerequisite and knowledge/concepts/curvature/_registry.json does not. Run knowledge/_tools/sync_registry.py.
- Second physics review. Both visuals are still proposals with sketches only. A tour of two-tilted-orbits-crossing must start the pebbles 'side by side' with 'one a tiny bit ahead', name sides as 'facing the way the pebbles travel', use 'difference in pull', and keep this note's tidal sign.

**Diff check** (2026-09-13, revision 5)

- Round-body rule: outside any round body, being a small gap nearer its centre makes its pull stronger by a fraction, twice the gap divided by the distance to that centre.: First-order expansion of GM/r^2 at r - d; python3 at R = 6.371e6 m, d = 1 m gives (R/(R-d))^2 - 1 = 3.13923e-7 vs 2d/R = 3.13922e-7. Counterexamples: inside a uniform ball (excluded by 'outside'); a sideways gap (excluded by 'nearer its centre'); a large gap (the next sentence's half-distance example). → True within scope; the added sign (stronger at the nearer point) is correct. Dropping 'For a huge gap, twice the fraction is far off' removes no claim the note relies on, since the half-distance example makes the same point.
- Working bridge: the pull GM/r^2 is weaker by the fraction 2 xi/r on a neighbour a distance xi farther out.: GM/(r+xi)^2 = (GM/r^2)(1 - 2xi/r + O(xi^2/r^2)). → Correct; same claim as before, reworded only.
- Orbit way and swing check: equal circular tilted orbits, one pebble a tiny bit ahead, reach the crossing after a quarter lap, just miss and slip past; 5 metres apart again after half a lap on swapped sides; 25 min for a 100 min lap.: Hill equations: an along-track offset y with x = 0 is constant (both orbits have the same angular speed), and the cross-track z'' = -n^2 z gives z = z0 cos(nt), zero at a quarter period and -z0 at half. 100/4 = 25 min, numeric tolerance rel 0.05 unchanged. → Correct. The along-track head start persists, so the pebbles pass the crossing separated by it and do not bump. The opening 'side by side ... with one a tiny bit ahead' no longer contradicts the pass-through sentence.
- Misconception correction: two tiny pebbles that just miss each other do not stop but slip past.: Energy of the z oscillator: speed toward each other is maximal (n z0) at z = 0, so they cannot stop there. → Correct and consistent with the way and the check.
- Tides observation: the part of the Moon's pull that the ocean and the ground share cannot move the ocean compared with the ground; only the difference in the Moon's pull across Earth can, and it raises the tides.: Compared with the revision-3 wording: split into two sentences, still scoped to the Moon's pull. Counterexamples: winds and the Sun also move the ocean, but the sentence is about the Moon's pull only; the solid-Earth body tide is also a difference across Earth, so 'across Earth' covers it. → Same claim as before, equally true.
- Orbit takeaway (raised by the re-read as a scope question): 'For neighbours in orbit, their gap swings back and forth, once per lap.': Hill equations with a radial offset x0 at matched circular speed: along-track drift -(3/2) n x0 t, python3 gives 9.4 m per lap per metre of height difference at 400 km; a pure along-track offset stays constant and does not swing. → False as a general sentence. Scoped to neighbours orbiting side by side at the same height, which is the way's question and setup; there the cross-track gap swings once per lap (also for elliptical orbits, which still cross twice per lap).
- Fix: Orbit way takeaway: 'For neighbours in orbit, their gap swings back and forth, once per lap.' became 'For neighbours orbiting side by side at the same height, their gap swings back and forth, once per lap.' Neighbours at different heights drift apart, and neighbours one behind the other keep a fixed gap, so the unscoped sentence was false.

**Diff check** (2026-09-13, revision 8)

- Changed sentence: 'That is why the marbles float in front of you.' The reason offered is the preceding sentence, 'You, the capsule and both marbles fall freely together.': Checked the claim's scope against the way's own numbers. In the capsule frame the marbles have no relative acceleration to leading order, since free fall removes the shared pull; the residual is the tidal term 2GM d/R^3 = 3.08e-6 m/s^2 for a one-metre gap (python3, GM = 3.986e14 m^3/s^2, R = 6.371e6 m), which over the 4.74 s drop moves each marble by at most 0.017 mm relative to the capsule. Counterexamples tried: air drag (the tube's air is pumped out, and relative speeds are micrometres per second, so drag is irrelevant either way); marbles of different mass (they are identical, and free fall is mass-independent); the exactness of 'float' (the same way ends by quantifying the growth as three hundredths of a millimetre, so the entry prose never claims the gap is fixed). → True within its stated scope, and unchanged in claim. The added 'in front of you' names where the marbles are and whose view they float in, which is the rider's; it adds a measurer and no physics. The check 'marbles-in-a-falling-capsule' gives the same reason ('The marbles float because they fall together with the capsule'), so the note stays consistent.
- Changed sentence: 'At the moment it drops, let go of two identical marbles, one a metre above the other.' (the phrase 'in front of you' was moved out of it).: Checked that the geometry the rest of the way needs survives the cut. The way's next paragraphs need the pair to be separated along the line to Earth's centre, which 'one a metre above the other' in a vertical tube gives; the paragraph then says 'The lower marble is a metre nearer Earth's centre'. The check's statement uses the identical wording. → Correct and unchanged in claim. The radial separation that the tidal argument needs is still stated, and no direction lost its reference: 'above' is set by the tube the capsule falls down, and the sideways case is sent to the orbit way in the same explanation.
- Changed sentence: 'The fall lasts almost five seconds, and each marble reaches about 167 kilometres an hour relative to the tube.': Recomputed with python3 for the way's 110 m tube: t = sqrt(2h/g) = 4.74 s and v = g t = 46.46 m/s = 167.2 km/h with g = 9.81 m/s^2; with the inverse-square field integrated over the drop, v = 46.48 m/s = 167.3 km/h, so the rounding to 167 holds either way. The two marbles differ in final speed by 1.5e-5 m/s, far inside 'about'. Checked the named frame: the tube stands on the ground, so 167 km/h is the speed relative to it; relative to the capsule each marble is nearly at rest. → Correct, and the same claim as 'past the tube' with the reference stated in the guide's idiom. No number, condition, scope, sign or sense changed.
- Fix: None. The re-read's three changed sentences are accurate as written, and no learner-visible text was edited by this diff check, so the revision stays 8 and no novice sign-off is owed for it.
- Fix: Reported, not fixed here, because they are unchanged from earlier stages: course-conventions.md still fixes no symbol or sign for the Newtonian tidal matrix (this note uses H = grad grad Phi with xi'' = -H xi); the prerequisites newtonian-tidal-tensor and taylor-series have no note under knowledge/concepts, so key_equations/point-mass-hessian is justified_by a note that does not yet exist; and the registry does not list poisson-equation-for-gravity as a prerequisite.
