---
type: "concept"
schema_version: 2
id: "volume-preserving-tidal-deformation"
title: "Volume-preserving tidal deformation"
tagline: "How tidal drift reshapes a small falling ball of crumbs but, at first, keeps its volume"
domain: "curvature"
tier: "core"
status: "physics-reviewed"
revision: 3
updated: "2026-09-13"
aliases: ["tidal ellipsoid", "shape change without volume change"]
prerequisites: ["relativistic-tidal-tensor", "ricci-tensor", "poisson-equation-for-gravity"]
leads_to: ["raychaudhuri-equation", "geodesic-deviation-in-gravitational-wave", "gravitational-wave-polarization", "tidal-derivation-of-vacuum-field-equations", "ricci-focusing-versus-weyl-shear"]
visuals: ["falling-ring-of-crumbs", "two-stars-and-a-distant-ring"]
---

# Volume-preserving tidal deformation

*How tidal drift reshapes a small falling ball of crumbs but, at first, keeps its volume*

`volume-preserving-tidal-deformation` · curvature · core · physics-reviewed (revision 3)

**Needs:** [[relativistic-tidal-tensor]] (entry) · [[ricci-tensor]] (working) · [[poisson-equation-for-gravity]] (working)  
**Opens:** [[raychaudhuri-equation]] · [[geodesic-deviation-in-gravitational-wave]] · [[gravitational-wave-polarization]] · [[tidal-derivation-of-vacuum-field-equations]] · [[ricci-focusing-versus-weyl-shear]]  
**Related:** [[tidal-force]] · [[spaghettification]] · [[weyl-tensor]] · [[strong-energy-condition]]  
**Visuals:** ★ [[falling-ring-of-crumbs]] · [[two-stars-and-a-distant-ring]]

> Let go of crumbs at rest on a small imaginary ball inside a cabin that falls freely near a round planet without turning, with nothing among the crumbs. Tidal drift stretches the ball along the line toward the planet's centre. It squeezes the ball half as much in each of two directions across that line. So the ball becomes an egg that, at first, keeps the ball's volume. By Newton's law of gravity, only mass inside a ball of crumbs let go at rest makes its volume start to change.

## You will be able to

**Entry**
- Explain why tidal drift near a round planet turns a small falling ball of crumbs into an egg without, at first, changing its volume. `objectives/explain-the-egg-keeps-its-volume` ← `checks/squashed-or-stretched`
- Predict whether a ball of crumbs let go at rest starts to shrink, from whether mass sits inside it. `objectives/predict-which-balls-shrink` ← `checks/which-balls-shrink`, `problems/ball-around-earth-higher-up`

**Working**
- Compute the initial volume acceleration of a released cloud of any size from the mass it encloses. `objectives/compute-from-enclosed-mass` ← `checks/big-cloud-beside-earth`, `problems/cube-around-earth`
- Use the zero trace of vacuum tides to find a gravitational wave's squeeze from its stretch and the change in a ring's area. `objectives/use-the-budget-for-a-wave` ← `checks/mirror-arms-in-a-wave`

**Formal**
- State the hypotheses under which a small freely falling ball keeps its volume at first, and give a counterexample when each fails. `objectives/state-the-hypotheses` ← `checks/released-with-a-shear`
- Use the fourth-order vacuum volume law to compare how soon balls released by different observers at one event lose volume. `objectives/compare-when-the-balance-fails` ← `checks/passer-loses-volume-sooner`
- Prove that every freely falling observer at an event finds a zero initial volume acceleration exactly when the stress-energy tensor vanishes there. `objectives/prove-the-matter-equivalence` ← `problems/every-observer-keeps-volume`

## Ways in

### 1. An egg with the ball's volume · entry · picture

*When tidal drift stretches a small falling ball of crumbs into an egg, does the egg take up more room, less, or the same?*

**Recap:** A cabin can fall freely, with nothing but gravity acting on it. Crumbs let go at rest inside it slowly drift compared with a centre crumb, because Earth's pull is slightly different at each crumb's place. They are timed with the cabin's clock and measured with a ruler fixed to the cabin. Near a round planet they drift away from the centre crumb along the line toward the planet's centre, and in across that line. This is called tidal drift.

Picture a cabin falling freely inside a tall tower on Earth, with the air pumped out. The cabin does not turn as it falls. Inside, hundreds of crumbs are held still in the cabin, spread over the surface of an imaginary ball 2 metres across. One more crumb, the centre crumb, sits at the ball's centre. Then all of them are let go together, at rest in the cabin.

Watch for ten seconds by the cabin's clock. Two crumbs sit 1 metre out on the line toward Earth's centre, one on each side of the centre crumb. Each drifts away from the centre crumb by 0.154 millimetres. A crumb 1 metre out across that line drifts in by half as far, 0.077 millimetres. The ball becomes egg-shaped: longer along the line, narrower across it, and with both ends alike.

Does the egg take up more room than the ball, or less? Measure each change as a fraction of the 1 metre from the centre crumb. A metre is 1,000 millimetres, so 0.154 millimetres is 154 millionths of a metre. So along the line, the egg is longer by 154 parts in a million. Across the line there are two directions at right angles to each other. In each of them, the egg is narrower by 77 parts in a million.

For small changes, a volume changes by the sum of these fractions. You can check this with a box. A box 1 metre on each side holds 1 cubic metre. Make it 2 thousandths longer and 1 thousandth narrower each way, so the fractions add to zero. Multiplying 1.002 by 0.999 by 0.999 gives 0.999997 cubic metres, only 3 millionths less than before. That tiny leftover comes from multiplying two small fractions together.

An egg's volume is also set by its length and its two widths multiplied together, so the same rule works for the egg. For the egg, the sum is 154 minus 77 minus 77, which is zero. So the stretch along the line pays for the two half-size squeezes across it, and at first the volume stays the same.

Preserving means keeping, and a deformation is a change of shape. So a change of shape by tidal drift that keeps the volume the same is called a volume-preserving tidal deformation.

The words "at first" matter. Adding fractions works only for small changes: 1.2 times 0.9 times 0.9 is 0.972, not 1. So once the egg is noticeably longer and thinner, the sum no longer gives its volume. Over a much longer fall, the egg's volume does start to shrink slowly; take on trust here that it shrinks rather than grows. After a whole minute, it has lost only about 15 parts in a million.

This balance is not a lucky feature of Earth. Einstein's theory of gravity, taken on trust here, makes it hold wherever nothing sits among the crumbs: near the Moon, the Sun, or a black hole. It holds as closely as anyone could ever measure.

You never notice any of this in daily life. In ten seconds the egg grows longer than the ball by only 0.3 millimetres, about the width of four hairs.

**Try it:** On a calculator, multiply 1.02 by 0.99 by 0.99. You should see 0.999702. So a box 2 parts in 100 longer and 1 part in 100 narrower each way has lost only 3 parts in 10,000 of its volume. That is far less than any of its changes in size. Then multiply 1.2 by 0.9 by 0.9. You should see 0.972. Here the fractions are plus 20, minus 10 and minus 10 hundredths, which still add to zero. Yet the box has lost almost 3 parts in 100 of its volume. For big changes, the sum no longer gives the volume.

**Takeaway:** Near a round planet, tidal drift stretches a small ball of crumbs let go at rest along the line to the planet's centre. It squeezes the ball half as much in two directions across. With nothing among the crumbs, it keeps its volume at first.

*What this leaves out:* Keeps the ball small compared with the planet, and treats the planet as a perfect ball that does not spin.

*Builds on:* [[relativistic-tidal-tensor]]<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/squashed-or-stretched`

### 2. A ball around the whole Earth shrinks · entry · contrast

*What makes a ball of falling crumbs start to shrink instead of keeping its volume?*

**Recap:** In a cabin that falls freely near Earth, crumbs let go at rest drift compared with a centre crumb. Along the line toward Earth's centre, a small ball of crumbs grows longer by some fraction. In each of two directions across that line, it grows narrower by half that fraction. For small changes, a volume changes by the sum of such fractions. That sum is one fraction minus two halves of it, which is zero, so at first the ball keeps its volume.

Now make the ball enormous. Picture crumbs spread over an imaginary ball around the whole Earth, 400 kilometres above the ground, where the space station flies, above almost all of the air. Earth sits at the ball's centre. Each crumb is held still relative to Earth's centre, and then all are let go together.

Every crumb falls toward Earth's centre. Measured with rulers that stay still relative to Earth, each falls about 435 metres in ten seconds. All the crumbs are the same distance from Earth's centre, so none falls ahead of the others. Earth's centre is also the ball's centre, so every crumb moves inward by the same amount. So the ball stays round and shrinks.

How much? Earth's radius is 6,371 kilometres, so the ball's radius is 6,771 kilometres, and 435 metres is 64 parts in a million of that. The ball is narrower by that fraction in every direction, so pick three directions at right angles. Adding the three fractions, its volume shrinks by about 193 parts in a million.

Compare the small ball of crumbs in the falling cabin beside Earth. Its crumbs fall toward the same Earth, yet at first it keeps its volume. Rulers in the cabin and rulers still relative to Earth agree on a ball's size far more closely than these changes, so the comparison is fair. The difference is what sits inside each ball. The huge ball holds the whole Earth. The small ball holds only empty space among its crumbs.

That difference changes how the crumbs move. With Earth inside, every crumb is pulled inward, toward the ball's centre. With Earth outside, crumbs on the side nearer Earth fall ahead and crumbs on the far side lag, so some move away from the centre and some move in, and these balance.

Newton's law of gravity shows that mass inside is what matters, for a ball of any size, which we take on trust here. A ball of crumbs let go at rest starts to change its volume only if mass sits inside it. More mass inside makes it shrink faster. Mass outside the ball, however close or heavy, changes only the ball's shape at first.

The rule covers the small ball in the cabin too. The cabin's walls pull on the crumbs very slightly, but the walls sit outside the small ball, so they do not start to change its volume either. The centre crumb does sit inside. But a crumb is so light that, in ten seconds, its pull moves the other crumbs far less than the width of an atom.

**Takeaway:** By Newton's law of gravity, a ball of crumbs let go at rest starts to shrink only when mass sits inside it. Mass outside, like a planet beside a small ball, changes only its shape at first.

*What this leaves out:* Treats Earth as a perfect ball that does not spin, and uses Newton's law of gravity, which describes gravity near Earth extremely well.

*Continues:* `ways_in/egg-with-the-same-volume`<br>*Visuals:* [[falling-ring-of-crumbs]]<br>*See:* `checks/which-balls-shrink`, `problems/ball-around-earth-higher-up`

### 3. Gauss's law counts the mass inside · working · calculation

*How does the enclosed mass set a released cloud's initial volume change, for a cloud of any size, and what replaces it in general relativity?*

The huge ball in "A ball around the whole Earth shrinks" lost volume, while the small egg beside Earth kept it. Newtonian gravity makes that contrast exact. Take free particles on a closed surface $S$ enclosing volume $V$, all at rest at $t = 0$. The derivation "Volume acceleration from Gauss's law" shows

$$\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}.$$

It holds for any size and shape of cloud, at the instant of release. A cloud beside Earth, however large, encloses no mass and starts with $\ddot V = 0$, although it is distorted into no simple shape. For a sphere of radius $r$ centred on a spherical mass, $\ddot V/V = -3GM/r^3$. At 400 km above Earth, $r = 6771$ km gives $-3.85\times10^{-6}\ \mathrm{s^{-2}}$, so in 10 s the volume falls by $\tfrac12(3.85\times10^{-6})(10)^2 = 1.93\times10^{-4}$, the 193 parts in a million of "A ball around the whole Earth shrinks".

For a small cloud around a point, $M_{\rm enc} = \rho\,\delta V$, and

$$\frac{\ddot{\delta V}}{\delta V} = -4\pi G\rho = -\nabla^2\Phi = -\operatorname{tr}\,\partial_i\partial_j\Phi.$$

The tidal matrix $\partial_i\partial_j\Phi$ fixes the shape as well. An axis along an eigenvector with eigenvalue $\lambda_i$ changes as $\ell_i \approx \ell_0(1 - \tfrac12\lambda_it^2)$. Just outside a spherical mass the eigenvalues are $(GM/r^3)(-2, 1, 1)$. At Earth's surface $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$, so in 10 s a 1 m semi-axis along the radius grows by 0.154 mm and each transverse one shrinks by 0.077 mm. The fractional changes sum to $-\tfrac12t^2\sum_i\lambda_i = 0$. Since $\delta V/V \approx \sum_i \delta\ell_i/\ell_i$ for small changes, this is the entry rule that the fractions add, now with the zero sum traced to $\nabla^2\Phi = 0$.

In general relativity the trace of an observer's tidal tensor is $R_{\mu\nu}u^\mu u^\nu$, and the small-ball law becomes $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$ for a ball released at rest. For a perfect fluid at rest relative to the observer this is $-4\pi G(\rho + 3p/c^2) + \Lambda c^2$. Outside matter, with $\Lambda = 0$, Einstein's equation gives $R_{\mu\nu} = 0$, so the trace vanishes for every observer at any velocity. An observer passing a spherical mass sideways at $0.6c$ measures the tidal tensor $(GM/r^3)\,\mathrm{diag}(-3.69, 2.69, 1)$: a different egg with the same zero sum.

The exact finite-cloud law is Newtonian. In general relativity the volume of a finite cloud depends on which events count as simultaneous, so only the small-ball law is local and exact.

**Takeaway:** A cloud released at rest starts with volume acceleration minus four pi G times its enclosed mass; for a small ball that is minus the tidal trace, which vanishes in vacuum for every observer.

*What this leaves out:* The finite-cloud law assumes Newtonian gravity; the general-relativistic law keeps only the leading order in the ball's size and in time.

*Continues:* `ways_in/ball-around-the-whole-earth`, `ways_in/egg-with-the-same-volume`<br>*Builds on:* [[ricci-tensor]], [[poisson-equation-for-gravity]]<br>*See:* `derivations/volume-acceleration-from-gauss`, `checks/big-cloud-beside-earth`, `problems/cube-around-earth`

### 4. A ring of mirrors in a gravitational wave · working · operational

*How does the zero trace of vacuum tides show up in a gravitational wave, and what can a detector measure of it?*

The zero trace in "Gauss's law counts the mass inside" holds for every tide in vacuum, including one that travels. Far from its source, a gravitational wave is such a tide. Take on trust here that a plane wave of plus polarization moving along $z$ gives a freely falling observer the tidal tensor $-\tfrac12\ddot h_+\,\mathrm{diag}(1, -1, 0)$ in her $x, y, z$ axes. Free masses at separation $L$, at rest before the wave arrives, then move to first order in $h_+$ as

$$\frac{\delta L_x}{L} = +\frac{h_+}{2},\qquad \frac{\delta L_y}{L} = -\frac{h_+}{2},\qquad \frac{\delta L_z}{L} = 0.$$

The budget is now one stretch for one equal squeeze, in the plane across the wave, instead of one stretch for two half-size squeezes. The fractional changes sum to zero at every moment, not only at release. So a ring of free masses in the $xy$ plane keeps its area, and a small ball its volume, to first order in $h_+$; the area factor is $1 - h_+^2/4$. The cross polarization does the same along axes turned by $45^\circ$.

A laser interferometer uses the mirrors at the ends of two perpendicular arms as free masses. At the signal's frequencies each suspended mirror moves freely along its arm, and the instrument measures $\delta L_x - \delta L_y$, which is $h_+L$ for a plus wave arriving along $z$. For GW150914 the peak strain was $1.0\times10^{-21}$. Each 4 km arm of LIGO therefore changed by about $2\times10^{-18}$ m, and the difference was about $4\times10^{-18}$ m, some 400 times smaller than a proton's width.

A single detector measures only this difference. By itself it cannot tell an area-preserving wave from a breathing wave, which stretches both directions together and changes a ring's area, as some alternatives to general relativity predict. Detectors with different orientations respond to each pattern differently, so a network can test which patterns the signal contains.

**Takeaway:** A gravitational wave stretches one direction across its path and squeezes the perpendicular one equally, so rings and small balls of free masses keep their area and volume to first order.

*What this leaves out:* Keeps first order in the strain, for masses much closer together than a wavelength and a wave arriving along one axis.

*Continues:* `ways_in/gauss-law-counts-the-mass-inside`<br>*Builds on:* [[relativistic-tidal-tensor]]<br>*Visuals:* [[two-stars-and-a-distant-ring]]<br>*See:* `checks/mirror-arms-in-a-wave`, `observations/gw170814-polarization-test`

### 5. Volume and shear of a released ball · formal · structure

*Under exactly which hypotheses does a small freely falling ball keep its volume, and for how long?*

The small-ball law in "Gauss's law counts the mass inside" is the first term of an exact evolution equation. Set $G = c = 1$. Let $u$ be a timelike geodesic congruence near an event $p$, with $B_{\mu\nu} = \nabla_\nu u_\mu$ split into expansion $\theta$, shear $\sigma_{\mu\nu}$ and rotation $\omega_{\mu\nu}$. For a small ball of its geodesics $\theta = d\ln\delta V/d\tau$, and the Raychaudhuri equation reads

$$\frac{d\theta}{d\tau} = -\frac{\theta^2}{3} - \sigma_{\alpha\beta}\sigma^{\alpha\beta} + \omega_{\alpha\beta}\omega^{\alpha\beta} - R_{\mu\nu}u^\mu u^\nu.$$

*Proposition.* Suppose (i) the ball is released at rest, $B_{\mu\nu}(0) = 0$; (ii) $R_{\mu\nu} = 0$ along its worldlines, which Einstein's equation gives in vacuum with $\Lambda = 0$; (iii) its size $\ell$ is small compared with the curvature radius and with the length over which curvature varies. Then

$$\ln\frac{\delta V}{\delta V_0} = -\tfrac{1}{12}E_{ij}E_{ij}\,\tau^4 + O(\tau^5),$$

where $E_{ij} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$ at $p$ in a parallel-propagated orthonormal frame, here the electric part of the Weyl tensor. *Sketch:* $\dot B = -B^2 - E$ with $B(0) = 0$ gives $B \approx -E\tau$; the zero trace removes the $\tau^2$ and $\tau^3$ terms of $\ln\delta V$, and the growing shear drives $\dot\theta \approx -E_{ij}E_{ij}\tau^2$. The derivation "Fourth-order volume loss in vacuum" gives the steps.

Each hypothesis is needed.

- *Release at rest.* A ball released with pure shear has $\ddot{\delta V}/\delta V = -\sigma_{\alpha\beta}\sigma^{\alpha\beta}$ at once, even in flat spacetime. An initial expansion changes the volume at first order, and rotation opposes focusing.
- *Vacuum with $\Lambda = 0$.* With $R_{\mu\nu} = \Lambda g_{\mu\nu}$, $R_{\mu\nu}u^\mu u^\nu = -\Lambda$, so a released ball starts to grow at $\ddot{\delta V}/\delta V = +\Lambda$, about $1\times10^{-35}\ \mathrm{s^{-2}}$ in SI today.
- *Smallness.* The deviation equation is first order in $\ell$; where the tidal field varies over a length $L$, corrections of relative order $\ell/L$ appear. Newtonian gravity alone gives the exact finite law $\ddot V(0) = -4\pi M_{\rm enc}$.

*Observers.* With $\Lambda = 0$, $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \tfrac12Tg_{\mu\nu})$, and this trace reversal is invertible in four dimensions. A symmetric tensor that vanishes on every timelike vector vanishes. So every freely falling observer at $p$ finds a zero initial volume acceleration exactly when $T_{\mu\nu}(p) = 0$. The fourth-order coefficient is not shared: $E_{ij}E_{ij}$ changes under boosts, so observers at one event who agree that the volume starts unchanged disagree on how long it stays nearly so. In vacuum the Kretschmann scalar is $R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta} = 8(E_{ij}E_{ij} - B_{ij}B_{ij})$, with $B_{ij}$ the magnetic part of the Weyl tensor. So only that difference is invariant: a static observer outside a spherical mass has $B = 0$ and $E_{ij}E_{ij} = 6M^2/r^6$, and a boosted observer's larger $E_{ij}E_{ij}$ comes with a nonzero $B_{ij}$.

*Light.* The same argument applies to a thin bundle of null geodesics with vanishing initial expansion and shear. In vacuum there is no Ricci term, so its cross-sectional area is constant through third order in the affine parameter; the Weyl tensor acts only by building shear, which then focuses the beam.

**Takeaway:** In vacuum with no cosmological constant, a small ball released at rest keeps its volume through third order in proper time; shear from the Weyl tensor removes volume at fourth order.

*Picture:* A small sphere of geodesics released at rest: its principal axes follow the eigenvectors of the electric Weyl tensor, its volume curve is flat through third order, and it bends down at fourth order as shear builds.

*What this leaves out:* Uses the Levi-Civita connection in four dimensions and a nonrotating, parallel-propagated frame.

*Continues:* `ways_in/gauss-law-counts-the-mass-inside`<br>*Builds on:* [[ricci-tensor]]<br>*See:* `derivations/fourth-order-loss-in-vacuum`, `checks/released-with-a-shear`, `checks/passer-loses-volume-sooner`, `problems/every-observer-keeps-volume`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| fall freely | — | To move with nothing but gravity acting: no air pushing, and no floor or rope holding you. | [[free-fall]] |
| tidal drift | — | The slow drift of neighbouring freely falling objects apart or together, because gravity pulls them slightly differently. Near a round planet they drift apart along the line toward its centre and together across it. | [[tidal-force]] |
| volume | — | The amount of room something takes up. | — |
| volume-preserving tidal deformation | VOL-yoom pri-ZUR-ving TIE-dul dee-for-MAY-shun | A change of shape caused by tidal drift that keeps the volume the same, like a small ball of crumbs becoming an egg that takes up the same room. Preserving means keeping; a deformation is a change of shape. | [[volume-preserving-tidal-deformation]] |

## Key equations

### Volume acceleration of a released cloud · working

$$
\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}
$$

A cloud of free particles released at rest starts to change its volume at a rate set only by the mass it encloses.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $V$ | volume enclosed by the surface of free particles | the volume |
| $\mathbf g$ | gravitational field at the particles | g |
| $M_{\rm enc}$ | mass inside the surface | the enclosed mass |

**Holds when:** Newtonian gravity; every particle on the surface at rest at $t = 0$; any size and shape; valid at that instant.  
**Say it:** “At release, the second time derivative of the volume is minus four pi G times the enclosed mass.”  
**Justified by:** `derivations/volume-acceleration-from-gauss`

### Initial volume law for a small ball · working

$$
\left.\frac{\ddot{\delta V}}{\delta V}\right|_{\tau = 0} = -R_{\mu\nu}u^\mu u^\nu
$$

A small ball released at rest starts to lose volume at a rate set by the trace of the tides, which is zero in vacuum.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\delta V$ | volume of the small ball | the small volume |
| $u^\mu$ | four-velocity of the central particle, $u_\mu u^\mu = -c^2$ | the four-velocity |
| $R_{\mu\nu}$ | Ricci tensor in the course convention | the Ricci tensor |

**Holds when:** Small ball released at rest; that instant only. Weak static field: $R_{\mu\nu}u^\mu u^\nu \approx 4\pi G\rho$.  
**Say it:** “At release, the small volume's second derivative over the volume is minus the Ricci tensor contracted twice with the four-velocity.”  
**Justified by:** `ricci-tensor`

### Free masses in a plus-polarized wave · working

$$
\frac{\delta L_x}{L} = +\frac{h_+}{2},\qquad \frac{\delta L_y}{L} = -\frac{h_+}{2},\qquad \frac{\delta L_z}{L} = 0
$$

A wave moving along $z$ stretches one transverse direction by as much as it squeezes the other, and does nothing along its path.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $h_+$ | plus-polarization strain of the wave | h plus |
| $L$ | separation of two free masses before the wave arrives | L |

**Holds when:** Plane wave along $z$; free masses at rest before it arrives and much closer than a wavelength; first order in $h_+$; course polarization convention.  
**Say it:** “The fractional change along x is plus h plus over two, along y minus h plus over two, and along z zero.”  
**Justified by:** `stated`

### Fourth-order volume loss in vacuum · formal

$$
\ln\frac{\delta V}{\delta V_0} = -\tfrac{1}{12}E_{ij}E_{ij}\,\tau^4 + O(\tau^5)
$$

In vacuum a small ball released at rest loses volume first at fourth order in proper time, at a rate set by the square of the tides.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $E_{ij}$ | tidal tensor $R_{\hat\imath\hat 0\hat\jmath\hat 0}$ at release, the electric Weyl tensor in vacuum ($G = c = 1$) | E i j |
| $\tau$ | proper time of the central particle | tau |

**Holds when:** Released at rest; $R_{\mu\nu} = 0$ along the worldlines; ball small; parallel-propagated orthonormal frame.  
**Say it:** “The log of the volume ratio is minus one twelfth of E i j E i j times tau to the fourth.”  
**Justified by:** `derivations/fourth-order-loss-in-vacuum`

## Derivations

### Volume acceleration from Gauss's law · working

**Goal:** Show that a Newtonian cloud of free particles released at rest has $\ddot V(0) = -4\pi G M_{\rm enc}$, and $\ddot{\delta V}/\delta V = -4\pi G\rho$ when it is small.

1. The particles on the closed surface $S$ move with velocity $\mathbf v$, so the enclosed volume changes as $\dot V = \oint_S \mathbf v\cdot d\mathbf A$.
2. Differentiate, following the particles: $\ddot V = \oint_S \dot{\mathbf v}\cdot d\mathbf A + \oint_S \mathbf v\cdot\frac{d}{dt}(d\mathbf A)$.
3. At $t = 0$ every particle is at rest, so the second integral vanishes, and $\dot{\mathbf v} = \mathbf g$: $\ddot V(0) = \oint_S \mathbf g\cdot d\mathbf A$.
4. Gauss's law for gravity, $\nabla\cdot\mathbf g = -4\pi G\rho$, with the divergence theorem gives $\oint_S \mathbf g\cdot d\mathbf A = -4\pi G M_{\rm enc}$.
5. For a small cloud around a point, $M_{\rm enc} = \rho\,\delta V$, so $\ddot{\delta V}/\delta V = -4\pi G\rho = -\nabla^2\Phi$, minus the trace of the tidal matrix $\partial_i\partial_j\Phi$.

**Result:** $\ddot V(0) = -4\pi G M_{\rm enc}$ for any released cloud, and $\ddot{\delta V}/\delta V = -4\pi G\rho$ for a small one; both vanish where the cloud encloses no mass.

### Fourth-order volume loss in vacuum · formal

**Goal:** With $G = c = 1$, show that a small ball released at rest where $R_{\mu\nu} = 0$ has $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$.

1. In a parallel-propagated orthonormal frame along the central geodesic, $B_{ij} = \nabla_j u_i$ obeys $\dot B_{ij} = -B_{ik}B_{kj} - E_{ij}$, with $E_{ij} = R_{\hat\imath\hat 0\hat\jmath\hat 0}$.
2. Released at rest, $B(0) = 0$. Since $B^2 = O(\tau^2)$, integrating once gives $B = -E(0)\tau + O(\tau^2)$. $B$ stays symmetric, so the rotation stays zero.
3. Take the trace. $\operatorname{tr}E = R_{\hat 0\hat 0} = 0$ along the worldline, so $\dot\theta = -B_{ik}B_{ki} = -E_{ij}(0)E_{ij}(0)\,\tau^2 + O(\tau^3)$.
4. Integrate with $\theta(0) = 0$: $\theta = -\tfrac13E_{ij}E_{ij}\tau^3 + O(\tau^4)$.
5. With $\theta = d\ln\delta V/d\tau$, integrate again: $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$.
6. Check with a constant tide $E = \mathrm{diag}(-2, 1, 1)/\tau_0^2$: the axes are $\cosh(\sqrt2\,s)$ and $\cos s$ with $s = \tau/\tau_0$, and $\cosh(\sqrt2\,s)\cos^2s = 1 - \tfrac12s^4 + O(s^6)$, while $\tfrac1{12}E_{ij}E_{ij} = \tfrac{6}{12}$.

**Result:** $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4 + O(\tau^5)$: no change through third order, then a loss set by the square of the trace-free tide.

## Worked examples

### A one-minute fall near Earth · working

**Problem:** A nonrotating cabin is dropped from rest high above Earth, in vacuum, and a small ball of free particles is released at rest inside it. Treat the tidal eigenvalues as constant at $(GM/r^3)(-2, 1, 1)$ with $GM/r^3 = 1.54\times10^{-6}\ \mathrm{s^{-2}}$. Find the fractional changes of the ball's axes and of its volume after 60 s.

1. Along an eigen-direction with eigenvalue $\lambda$, a separation released at rest obeys $\ddot\ell = -\lambda\ell$. With $q = GM/r^3$, the radial axis grows as $\cosh(\sqrt{2q}\,t)$ and each transverse axis shrinks as $\cos(\sqrt q\,t)$.
2. $\sqrt q\,t = (1.2415\times10^{-3}\ \mathrm{s^{-1}})(60\ \mathrm s) = 0.07449$, so $\cosh(\sqrt2 \times 0.07449) = \cosh(0.10535) = 1.005554$ and $\cos(0.07449) = 0.997227$.
3. The radial axis is longer by 0.555 per cent and each transverse axis shorter by 0.277 per cent, an axis ratio of 1.0084.
4. The volume ratio is $1.005554 \times 0.997227^2 = 0.9999846$, a loss of $1.54\times10^{-5}$.
5. At order $t^2$ the fractional axis changes, $+qt^2$ and $-\tfrac12qt^2$ twice, sum to zero. The whole loss comes from order $t^4$: $\tfrac12q^2t^4 = 1.54\times10^{-5}$.
6. In 60 s the cabin falls about 17.7 km, which changes $GM/r^3$ by less than 1 per cent, so constant eigenvalues are adequate at this precision.

**Answer:** Radial axis $+0.555$ per cent, each transverse axis $-0.277$ per cent; volume $-1.54\times10^{-5}$, about 15 parts in a million.

**Takeaway:** The zero trace cancels the volume change at order $t^2$, so the shape changes several hundred times more than the volume in the first minute.

## Problems

### `ball-around-earth-higher-up` · entry · difficulty 1 · calculation

Crumbs are spread over a huge imaginary ball around the whole Earth, 1,000 kilometres above the ground, so the ball's radius is 7,371 kilometres. All are let go at rest. In ten seconds each crumb falls 367 metres toward Earth's centre, measured with rulers that stay still relative to Earth. By about how many parts in a million does the ball's volume shrink? Why does a small ball of crumbs beside Earth not shrink at first?

**Hints**

1. What fraction of the ball's radius is 367 metres?
2. The ball stays round. In how many directions at right angles does it shrink by that fraction?

**Answer:** About 150 parts in a million, or 0.015 per cent. The huge ball holds all of Earth's mass, while a small ball beside Earth holds none.

**Must contain:** The radius shrinks by about 50 parts in a million; Three directions add to about 150 parts in a million; Only the huge ball has mass inside

**Numeric:** fraction of the ball's volume lost in ten seconds = 0.0149 percent (magnitude, ±5%)

**Solution**

1. The radius shrinks by 367 metres out of 7,371,000 metres. That is 367 divided by 7,371,000, about 50 parts in a million.
2. Every crumb falls the same distance toward Earth's centre, so the ball stays round. It is narrower by 50 parts in a million in each of three directions at right angles.
3. For small changes, the volume changes by the sum of the three fractions: about 150 parts in a million. That is 15 parts in 100,000, or 0.015 per cent.
4. A small ball beside Earth holds none of Earth's mass. Its stretch along the line toward Earth's centre balances its two squeezes across that line, so at first it keeps its volume.

**Targets:** `mass-nearby-shrinks-the-ball`

### `cube-around-earth` · working · difficulty 2 · calculation

A cube of free particles 100,000 km on each side, centred on Earth, is released at rest; the Moon lies outside it. Using Gauss's law with $GM_\oplus = 3.986\times10^{14}\ \mathrm{m^3\,s^{-2}}$, find $\ddot V/V$ at release and the fraction of the cube's volume lost in the first 60 s. Would a sphere of the same volume centred on Earth start any differently?

**Hints**

1. At release, the volume acceleration depends only on the enclosed mass.

**Answer:** $\ddot V/V = -5.01\times10^{-9}\ \mathrm{s^{-2}}$, and the cube loses $9.0\times10^{-6}$ of its volume in 60 s. A sphere of the same volume around Earth starts identically; only the two shapes distort differently.

**Must contain:** The volume acceleration is minus four pi G M, about minus 5.01e-9 per second squared per volume; About 9.0e-6 of the volume is lost in 60 seconds; Any shape of the same volume starts the same

**Numeric:** fraction of the cube's volume lost in 60 s = 9e-06 1 (magnitude, ±3%)

**Solution**

1. The cube's corners are $\sqrt3 \times 50{,}000 \approx 86{,}600$ km from Earth's centre, well inside the Moon's orbit of about 384,000 km, so the enclosed mass is Earth's alone.
2. Released at rest, $\ddot V(0) = -4\pi GM_\oplus = -4\pi(3.986\times10^{14}) = -5.009\times10^{15}\ \mathrm{m^3\,s^{-2}}$.
3. $V = (1.0\times10^{8}\ \mathrm m)^3 = 1.0\times10^{24}\ \mathrm{m^3}$, so $\ddot V/V = -5.01\times10^{-9}\ \mathrm{s^{-2}}$.
4. For a short time $\Delta V/V \approx \tfrac12(\ddot V/V)t^2 = -\tfrac12(5.01\times10^{-9})(3600) = -9.0\times10^{-6}$. The particles fall at most about 300 m in that time, at the face centres, less than a hundred-thousandth of the cube's half-width, so the short-time form is accurate.
5. The law depends only on the enclosed mass, so a sphere of equal volume centred on Earth has the same $\ddot V(0)$ and loses the same fraction at first.

### `every-observer-keeps-volume` · formal · difficulty 2 · proof

Set $G = c = 1$ and $\Lambda = 0$. Prove that at an event $x$, every freely falling observer's small ball released at rest has $\ddot{\delta V}(0) = 0$ if and only if $T_{\mu\nu}(x) = 0$. Then show that one observer's zero is not enough, using a perfect fluid with pressure $P = -\rho/3$.

**Hints**

1. Use the initial volume law, then the trace-reversed Einstein equation.
2. A symmetric bilinear form that vanishes on every timelike vector vanishes.

**Answer:** Every observer finds zero exactly when $R_{\mu\nu}(x) = 0$, which with $\Lambda = 0$ holds exactly when $T_{\mu\nu}(x) = 0$. For the fluid, the comoving observer finds $R_{\mu\nu}u^\mu u^\nu = 4\pi(\rho + 3P) = 0$, while an observer moving relative to it with Lorentz factor $\gamma$ finds $\tfrac{16\pi}{3}\rho(\gamma^2 - 1) > 0$.

**Must contain:** Zero for every timelike vector forces the Ricci tensor to vanish; Trace reversal is invertible, so zero Ricci means zero stress-energy; The fluid gives zero only for its own observer

**Solution**

1. For a ball released at rest the initial volume law gives $\ddot{\delta V}/\delta V = -R_{\mu\nu}u^\mu u^\nu$ for the observer with unit four-velocity $u$.
2. If $T_{\mu\nu}(x) = 0$, Einstein's equation $R_{\mu\nu} = 8\pi(T_{\mu\nu} - \tfrac12Tg_{\mu\nu})$ gives $R_{\mu\nu}(x) = 0$, so every observer finds zero.
3. Conversely, suppose $R_{\mu\nu}u^\mu u^\nu = 0$ for every unit timelike $u$, hence by scaling for every timelike vector. For timelike $u$ and any $v$, $u + \epsilon v$ is timelike for small $|\epsilon|$, so $2\epsilon R(u,v) + \epsilon^2R(v,v) = 0$ on an interval, and $R(v,v) = 0$ for every $v$. Polarization gives $R_{\mu\nu}(x) = 0$.
4. Tracing, $R = -8\pi T$, so $T = 0$, and then $T_{\mu\nu} = R_{\mu\nu}/8\pi + \tfrac12Tg_{\mu\nu} = 0$.
5. For the fluid, $T_{\mu\nu}u'^\mu u'^\nu = (\rho + P)\gamma^2 - P$ and $T = -\rho + 3P$, so $R_{\mu\nu}u'^\mu u'^\nu = 8\pi\big[(\rho + P)\gamma^2 - \tfrac12\rho + \tfrac12P\big]$.
6. With $P = -\rho/3$ this is $8\pi\cdot\tfrac23\rho(\gamma^2 - 1) = \tfrac{16\pi}{3}\rho(\gamma^2 - 1)$: zero for the comoving observer, $\gamma = 1$, and positive for every other, although $T_{\mu\nu} \neq 0$.

## Observations

- **Gravity gradients above Earth measured by the GOCE satellite, 2009 to 2013** (measured, working). GOCE carried three perpendicular pairs of accelerometers whose differences give the Newtonian tidal matrix of a freely falling instrument. Once the satellite's own rotation is removed, the three diagonal gradients add to zero within the instrument's noise, for gradients varying with periods of about 10 to 200 s. That zero sum is the volume budget of a small released ball, measured in orbit outside Earth's mass. *Numbers:* About 255 km up, for a spherical Earth: $-2.74\times10^{-6}\ \mathrm{s^{-2}}$ along the radius and $+1.37\times10^{-6}\ \mathrm{s^{-2}}$ along each horizontal axis in the course sign. A 1 m semi-axis released at rest there would grow by 0.137 mm radially and shrink by 0.069 mm horizontally in 10 s. *Reference:* Reiner Rummel, Weiyong Yi, Claudia Stummer (2011), *GOCE gravitational gradiometry*, Journal of Geodesy 85, 777–790, doi:10.1007/s00190-011-0500-0
- **A polarization test with GW170814, the first gravitational-wave signal recorded by three detectors** (measured, working). The two LIGO detectors and Virgo point their arms in different directions, so they respond differently to general relativity's area-preserving tensor waves and to breathing scalar waves that would change a ring's area. Comparing the three responses, the analysis favoured a purely tensor polarization over purely vector and purely scalar alternatives. *Numbers:* Reported Bayes factors of about 200 for purely tensor against purely vector polarization, and about 1000 against purely scalar. *Reference:* B. P. Abbott, R. Abbott, T. D. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101

## Teaching arc

1. **Predict the egg's volume** (entry). Ask for a prediction, then add the three fractional changes and test the adding rule on a calculator. *Why:* The visible stretch makes an unchanged volume a real surprise. *Predict:* When tidal drift stretches the ball into an egg, does the egg take up more room, less room, or the same? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/egg-with-the-same-volume`, `checks/squashed-or-stretched`
2. **Put the planet inside the ball** (entry). Swap the small ball for a huge ball around the whole Earth, then sort the three balls of the choice check. *Why:* It isolates mass inside the ball as the only thing that starts to change its volume. *Predict:* A huge ball of crumbs around the whole Earth is let go. Does it keep its volume at first, like the small one? *Visual:* [[falling-ring-of-crumbs]] *Uses:* `ways_in/ball-around-the-whole-earth`, `checks/which-balls-shrink`
3. **Count the mass inside, then ride a wave** (working). Derive the release law from Gauss's law, test it on a large cloud beside Earth, then read a wave's equal stretch and squeeze. *Why:* One flux argument covers every size, and the wave balances one squeeze instead of two. *Predict:* As a gravitational wave squeezes a ring of free masses into an oval, does the area inside the ring change? *Visual:* [[two-stars-and-a-distant-ring]] *Uses:* `derivations/volume-acceleration-from-gauss`, `checks/big-cloud-beside-earth`, `ways_in/ring-of-mirrors-in-a-gravitational-wave`, `checks/mirror-arms-in-a-wave`
4. **Break each hypothesis** (formal). Run the Raychaudhuri argument to fourth order, break two hypotheses, then compare two observers at one event. *Why:* Graduate readers need what the statement assumes and how long it lasts. *Predict:* In empty flat spacetime, does a small ball released with a gentle shear keep its volume at first? *Uses:* `ways_in/volume-and-shear-of-a-released-ball`, `checks/released-with-a-shear`, `checks/passer-loses-volume-sooner`

## Misconceptions

### “Gravity pulls everything together, so tidal drift squashes a falling ball of crumbs and makes it smaller.” · entry · `tides-squash-the-ball`

- **Why it is tempting:** Gravity attracts, so any change it causes seems to pull things in.
- **What is true:** Near a round planet, the stretch along the line toward the planet's centre equals the two squeezes across that line added together. So a small ball let go at rest at first changes shape without changing volume.
- **Exposed by:** `checks/squashed-or-stretched`

### “A heavy planet right beside a ball of crumbs squeezes it harder, so the ball must lose volume.” · entry · `mass-nearby-shrinks-the-ball`

- **Why it is tempting:** Bigger drifts look like a stronger squeeze.
- **What is true:** A heavier planet makes the stretch and both squeezes bigger together, so they still balance. Only mass inside the ball makes its volume start to change.
- **Exposed by:** `checks/which-balls-shrink`

### “Only a tiny cloud keeps its volume; a big cloud beside Earth must start to shrink because its near side is pulled much harder.” · working · `big-cloud-must-shrink`

- **Why it is tempting:** The volume budget is usually derived only for small balls.
- **What is true:** In Newtonian gravity a cloud of any size released at rest starts with volume acceleration minus four pi G times the mass it encloses. With no mass inside, only its shape starts to change.
- **Exposed by:** `checks/big-cloud-beside-earth`

### “A gravitational wave squeezes a ring of free masses into an oval, so the area inside the ring shrinks and grows as the wave passes.” · working · `wave-changes-area`

- **Why it is tempting:** Pictures of the wave show the ring squashed.
- **What is true:** The ring stretches along one direction by exactly as much as it squeezes along the perpendicular one, so its area stays the same to first order in the strain. Changing the area would need a breathing polarization, which general relativity does not have.
- **Exposed by:** `checks/mirror-arms-in-a-wave`

### “In any vacuum region, a small ball of free particles keeps its volume at first, however it is released.” · formal · `vacuum-always-keeps-volume`

- **Why it is tempting:** Vacuum tides are trace-free, and the slogan usually drops the conditions on the release and on the cosmological constant.
- **What is true:** A ball released with shear loses volume at once, even in flat spacetime. A positive cosmological constant makes a ball released at rest grow.
- **Exposed by:** `checks/released-with-a-shear`

### “Observers at one event who agree that a released ball keeps its volume at first also agree on how long it stays nearly unchanged.” · formal · `balance-lasts-equally-for-all`

- **Why it is tempting:** The zero trace holds for every observer, so the whole volume history seems observer-independent.
- **What is true:** The fourth-order loss is set by the square of the electric Weyl tensor, which changes under boosts. A ball released by an observer moving sideways past a mass loses volume sooner.
- **Exposed by:** `checks/passer-loses-volume-sooner`

## Checks

1. **Entry · predict** `checks/squashed-or-stretched`. In a cabin falling freely near Earth without turning, crumbs are spread over an imaginary ball 2 metres across, with a centre crumb at its centre and nothing else among them. All are let go at rest. A friend says gravity pulls everything together, so tidal drift will squash the ball and make it smaller. In ten seconds by the cabin's clock, a crumb 1 metre out along the line toward Earth's centre drifts away from the centre crumb by 0.154 millimetres. A crumb 1 metre out across that line drifts in by 0.077 millimetres. What happens to the ball's volume in those ten seconds?
   - **Hints:** Write each drift as a fraction of 1 metre. / Add the three fractions, counting narrower as negative.
   - **Answer:** The volume stays the same. The leftover from multiplying small fractions is less than 2 parts in 100 million. The friend is right that Earth pulls every crumb. But inside the falling cabin only differences in pull show, and they stretch the ball as well as squeeze it. Along the line toward Earth's centre, the ball grows longer by 154 parts in a million, because 0.154 millimetres is that fraction of 1 metre, which is 1,000 millimetres. Across the line, it grows narrower by 77 parts in a million in each of two directions at right angles. For small changes, the volume changes by the sum of these fractions. So the change is 154 minus 77 minus 77, which is zero. The ball becomes egg-shaped, but in these ten seconds it keeps its volume.
   - **Must contain:** The volume stays the same; Plus 154, minus 77, minus 77 parts in a million; Small fractional changes add
   - **Numeric:** change in the ball's volume after ten seconds = 0 percent (signed, ±0.001)
   - **Targets:** `tides-squash-the-ball`
   - **Visual:** [[falling-ring-of-crumbs]]
2. **Entry · choice** `checks/which-balls-shrink`. Three balls of crumbs are each let go at rest, with no air among or around the crumbs. Ball A is 2 metres across, beside a planet 8 times as heavy as Earth. It sits where every drift is 8 times as big as near Earth's surface. Ball B is 2 metres across, just above the Moon's surface. Ball C is a huge ball around the whole Moon, 100 kilometres above its surface. Which balls start to shrink?
   - **Hints:** Which of the three balls has any mass inside it?
   - **Answer:** Only ball C. A ball of crumbs let go at rest starts to change its volume only if mass sits inside it. Ball A holds nothing but empty space. Its planet makes the stretch along the line 8 times as big, but it makes both squeezes across the line 8 times as big too, so they still add up to zero. Ball B is the same, with smaller drifts from the Moon. Ball C holds the whole Moon. Every one of its crumbs falls toward the Moon's centre, so the ball stays round and shrinks.
   - **Must contain:** Only ball C shrinks; Only mass inside a ball changes its volume; Bigger drifts still add up to zero
   - **Targets:** `mass-nearby-shrinks-the-ball`
3. **Working · evaluate-claim** `checks/big-cloud-beside-earth`. A spherical cloud of free particles 20,000 km across is centred 20,000 km from Earth's centre, so Earth lies outside it. All its particles are released at rest. Claim: the side nearer Earth is pulled much harder than the far side, so the cloud must start to lose volume. Treat Earth as a point mass and use Newtonian gravity. Evaluate the claim, and say what does start to change.
   - **Hints:** At release, what does Gauss's law say about the flux of g through the cloud's surface?
   - **Answer:** The claim is false. At release every particle is at rest, so the second derivative of the enclosed volume is the flux of the gravitational field through the cloud's surface, $\ddot V(0) = \oint \mathbf g\cdot d\mathbf A$. Gauss's law makes that flux $-4\pi G M_{\rm enc}$, and the cloud encloses no mass, so $\ddot V(0) = 0$ exactly, whatever the cloud's size. The near side does accelerate toward Earth faster than the centre, but the far side lags behind it and the sides converge toward Earth, and these cancel in the flux. The cloud's shape starts to change: it lengthens toward Earth and narrows across, and because the tidal field varies strongly across a cloud this large, it does not become a simple ellipsoid.
   - **Must contain:** At release the volume acceleration is the flux of g; Gauss's law makes that flux zero with no mass inside; Only the shape starts to change
   - **Targets:** `big-cloud-must-shrink`
4. **Working · numeric** `checks/mirror-arms-in-a-wave`. A plus-polarized gravitational wave arrives along the $z$ axis of a freely falling observer. At one instant it has lengthened a 4 km row of free masses along $x$ by $2.0\times10^{-18}$ m. By how much has it changed rows of the same length along $y$ and along $z$? By what fraction has the area of a ring of free masses in the $xy$ plane changed, to first order in the strain?
   - **Hints:** Find the strain from the change along x. / Multiply the fractional changes along x and y to get the area factor.
   - **Answer:** Along $x$, $\delta L_x/L = h_+/2 = 2.0\times10^{-18}/4000 = 5\times10^{-22}$, so $h_+ = 1.0\times10^{-21}$. Along $y$ the wave gives $\delta L_y/L = -h_+/2$, so the row shortens by $2.0\times10^{-18}$ m. Along $z$, the direction of travel, nothing changes. The ring's area scales as $(1 + h_+/2)(1 - h_+/2) = 1 - h_+^2/4$, so to first order its area is unchanged; the second-order change, $2.5\times10^{-43}$, is far beyond any measurement. The tidal tensor of the wave is trace-free, the vacuum budget with one stretch balanced by one equal squeeze.
   - **Must contain:** The y row shortens by 2.0e-18 metres; The z row does not change; The ring's area is unchanged to first order
   - **Numeric:** change in the row along y = -2e-18 m (signed, ±2%); change in the row along z = 0 m (signed, ±1e-20); first-order fractional change in the ring's area = 0 1 (signed, ±1e-30)
   - **Targets:** `wave-changes-area`
   - **Visual:** [[two-stars-and-a-distant-ring]]
5. **Formal · evaluate-claim** `checks/released-with-a-shear`. Claim: in any vacuum region, a small ball of free particles keeps its volume at first. Test it with two cases. (a) In flat spacetime, a ball is released with velocity field $v_i = S_{ij}x_j$, where $S = \mathrm{diag}(s, -s, 0)$ and $s = 1.0\times10^{-3}\ \mathrm{s^{-1}}$; find its volume ratio after 60 s. (b) In de Sitter spacetime, $R_{\mu\nu} = \Lambda g_{\mu\nu}$, a ball is released at rest. Which hypotheses of the volume statement fail?
   - **Hints:** With no forces, write each particle's position at time t and take the determinant. / Contract $R_{\mu\nu} = \Lambda g_{\mu\nu}$ twice with a unit timelike vector.
   - **Answer:** The claim is false in both cases. (a) No forces act, so each particle moves as $x(t) = (1 + St)x_0$ and $V/V_0 = \det(1 + St) = (1 + st)(1 - st) = 1 - s^2t^2$. After 60 s this is $1 - 0.0036 = 0.9964$, and $\ddot V/V = -2s^2 = -2\times10^{-6}\ \mathrm{s^{-2}}$ from the start, comparable to Earth's tidal entries. The Raychaudhuri equation agrees: $\theta = 0$, $\omega = 0$, $R_{\mu\nu} = 0$, and $\sigma_{\alpha\beta}\sigma^{\alpha\beta} = 2s^2$, so $\dot\theta = -2s^2$. The failed hypothesis is release at rest, $B_{\mu\nu}(0) = 0$. (b) Here $R_{\mu\nu}u^\mu u^\nu = \Lambda g_{\mu\nu}u^\mu u^\nu = -\Lambda c^2$, so $\ddot{\delta V}/\delta V = +\Lambda c^2$: the ball starts to grow, at about $1\times10^{-35}\ \mathrm{s^{-2}}$ for today's value. The failed hypothesis is $R_{\mu\nu} = 0$, which vacuum gives only when $\Lambda = 0$.
   - **Must contain:** The sheared ball's volume ratio is 0.9964 after 60 seconds; Shear removes volume at once, even with zero curvature; A positive cosmological constant makes a released ball grow
   - **Numeric:** volume ratio of the sheared ball after 60 s = 0.9964 1 (magnitude, ±0.05%)
   - **Targets:** `vacuum-always-keeps-volume`
6. **Formal · numeric** `checks/passer-loses-volume-sooner`. Set $G = c = 1$. Just outside a spherical mass, a freely falling observer momentarily at rest relative to it measures the tidal tensor $q\,\mathrm{diag}(-2, 1, 1)$, and one passing sideways at $\beta = 0.6$ measures $q\,\mathrm{diag}(-3.6875, 2.6875, 1)$. Each releases a small ball at rest. Find $E_{ij}E_{ij}$ for each, and the ratio of the passer's time to the other's for the same small volume loss.
   - **Hints:** Square and add the diagonal entries. / Hold the loss fixed and solve the fourth-order law for the time.
   - **Answer:** Both traces vanish, $-2 + 1 + 1 = 0$ and $-3.6875 + 2.6875 + 1 = 0$, so both balls keep their volume through third order in proper time. The fourth-order law $\ln(\delta V/\delta V_0) = -\tfrac1{12}E_{ij}E_{ij}\tau^4$ then separates them. For the observer at rest, $E_{ij}E_{ij} = (4 + 1 + 1)q^2 = 6q^2$. For the passer, $E_{ij}E_{ij} = (13.598 + 7.223 + 1)q^2 = 21.82q^2$. A given small loss needs $\tau^4 \propto 1/E_{ij}E_{ij}$, so the passer's time is $(6/21.82)^{1/4} = 0.724$ of the other's. The passer's ball loses volume sooner, because $E_{ij}E_{ij}$ is not invariant under boosts, although the zero trace is.
   - **Must contain:** Both traces vanish; E i j E i j is 6 and 21.82 in units of q squared; The time ratio is 0.724
   - **Numeric:** E i j E i j for the passer in units of q squared = 21.82 1 (magnitude, ±1%); ratio of the passer's time to the resting observer's time = 0.724 1 (magnitude, ±1%)
   - **Targets:** `balance-lasts-equally-for-all`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| What the strain of a gravitational wave measures | With $h^{\rm TT}_{ij} = h_+e^+_{ij} + h_\times e^\times_{ij}$, free masses along $\mathbf p$ change separation by $\delta L/L = h_+/2$, and arms along $\mathbf p$ and $\mathbf q$ read $(\delta L_x - \delta L_y)/L = h_+$ for a wave along $\mathbf n$. | Detector papers call $(\delta L_x - \delta L_y)/L$ the strain $h(t)$ and sometimes describe one arm as changing by $hL$, twice the single-arm change for an optimally oriented plus wave. |

## Visuals

- ★ [[falling-ring-of-crumbs]] (flagship): The central picture: a small ball of falling crumbs becomes an egg whose volume meter stays flat at first, beside a ball around the whole planet that shrinks. *Sketch:* This concept adds a volume meter and a size switch. Presets: a small ball beside the planet, a large cloud beside it that does not contain it, and a ball around the whole planet. Readouts give the fractional stretch along the line, each squeeze across it, their sum, and the volume ratio. A time slider runs past the first minute so the slow fourth-order loss shows. For formal readers, a shear-at-release toggle and a cosmological-constant slider break the balance.
- [[two-stars-and-a-distant-ring]] (supporting): The zero trace in a wave: a distant ring of free masses stretches one way and squeezes the other equally, keeping its area. *Sketch:* This concept adds an area readout for the distant ring, fractional stretch readouts along two perpendicular axes with their sum, and a switch to an invented breathing wave that grows and shrinks the ring evenly, the only case in which the area readout moves.

## Tutor moves

**Open with**

- Picture a small ball of crumbs let go at rest inside a cabin that falls freely near Earth, with nothing among the crumbs. Tidal drift stretches it into an egg shape. Does the egg take up more room than the ball, less room, or the same? *(prediction)*
- Now picture crumbs spread over a huge ball around the whole Earth, high above the air, all let go at rest. Does this ball keep its volume at first, like the small one? *(prediction)*

**If the learner is stuck**

- *The learner does not believe that small fractional changes of length and widths add up to the change in volume.* → Multiply out 1.002 by 0.999 by 0.999, then 1.2 by 0.9 by 0.9, and compare each with the sum of the fractions. *Uses:* `ways_in/egg-with-the-same-volume`

**Common questions**

- *Does the egg keep its volume forever?* (entry) No, only at first. As the egg keeps growing longer and thinner, the balance slowly fails, and its volume starts to shrink. Near Earth this is very slow. After a whole minute of falling freely near Earth, in a cabin that does not turn, the egg is longer than the ball by about half of one per cent. Yet its volume has shrunk by only about 15 parts in a million. *Uses:* `ways_in/egg-with-the-same-volume`, `worked_examples/one-minute-fall-near-earth`

**Switching levels**

- To working when: asks for a formula for the volume change; asks whether gravitational waves do the same. Derive the release law from Gauss's law, then read the stretch and squeeze of a wave. *Uses:* `ways_in/gauss-law-counts-the-mass-inside`, `ways_in/ring-of-mirrors-in-a-gravitational-wave`
- To formal when: asks how long the volume stays constant; asks what exactly released at rest means. Give the Raychaudhuri argument to fourth order, then break each hypothesis with the sheared ball. *Uses:* `ways_in/volume-and-shear-of-a-released-ball`, `checks/released-with-a-shear`
- To research when: asks about visualizing black-hole mergers, weak lensing, or testing general relativity with wave polarizations. Open the research horizon. *Uses:* `research_horizon/tidal-tendex-lines`, `research_horizon/lensing-convergence-and-shear`, `research_horizon/polarization-tests`

**Pronunciations:** Ricci → REE-chee; Weyl → VILE; Raychaudhuri → ray-CHOWD-hoo-ree; Poisson → pwah-SOHN; GOCE → GOH-chay; LIGO → LIE-go

**Voice notes:** At entry, say 'at first' whenever the balance is stated.

## History

- **Siméon Denis Poisson (1813).** Extended Laplace's equation for the gravitational potential to points inside matter, in modern notation $\nabla^2\Phi = 4\pi G\rho$: the Newtonian statement that the trace of the tides is set by the local density.
- **Albert Einstein (1915).** Gave the final field equations, whose vacuum form $R_{\mu\nu} = 0$ makes the tidal trace vanish for every freely falling observer outside matter. Albert Einstein (1915), *Die Feldgleichungen der Gravitation*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 844–847
- **Amal Kumar Raychaudhuri (1955).** Derived, for the freely falling dust of a cosmological model, the evolution equation for the expansion of its worldlines, with separate terms for shear, rotation and the Ricci tensor. Amal Kumar Raychaudhuri (1955), *Relativistic cosmology. I*, Physical Review 98, 1123–1126, doi:10.1103/PhysRev.98.1123

## Research horizon

- **Tidal tendex lines.** In vacuum the tidal tensor is trace-free at every event, so along its three eigen-directions a stretch is always balanced by squeezes. Drawing the eigenvector fields as tendex lines, labelled by their eigenvalues, maps where merging black holes stretch and squeeze nearby matter, and how those patterns leave as gravitational waves. Robert Owen, Jeandrew Brink, Yanbei Chen, Jeffrey D. Kaplan and others (2011), *Frame-dragging vortexes and tidal tendexes attached to colliding black holes: visualizing the curvature of spacetime*, Physical Review Letters 106, 151101, doi:10.1103/PhysRevLett.106.151101
- **Convergence and shear of light beams.** For a narrow bundle of light rays, matter inside the beam focuses it directly through the Ricci term, while mass beside the beam enters only through the Weyl term, which shears the beam's cross-section: the light-ray version of the egg. Weak-lensing surveys measure that shear in the images of background galaxies to map mass, including dark matter, lying beside the lines of sight. Matthias Bartelmann, Peter Schneider (2001), *Weak gravitational lensing*, Physics Reports 340, 291–472, doi:10.1016/S0370-1573(00)00082-X
- **Testing the polarizations of gravitational waves.** General relativity allows only two polarizations, both transverse and trace-free, so a ring of free masses keeps its area. General metric theories allow up to six, including a breathing mode that changes the area. Networks of differently oriented detectors compare each signal with these patterns, beginning with GW170814. Clifford M. Will (2014), *The Confrontation between General Relativity and Experiment*, Living Reviews in Relativity 17, 4, doi:10.12942/lrr-2014-4; B. P. Abbott, R. Abbott, T. D. Abbott and others (2017), *GW170814: A Three-Detector Observation of Gravitational Waves from a Binary Black Hole Coalescence*, Physical Review Letters 119, 141101, doi:10.1103/PhysRevLett.119.141101

## Review: novice

**Verdict:** fixed (2026-09-13, revision 2)

**Retell attempt:** In a cabin falling freely down a tower, you let go of crumbs on a ball 2 metres across. In ten seconds the ones along the line to Earth's centre drift out 0.154 millimetres and the ones across drift in half as far, so the ball turns into an egg. You turn those into parts in a million and add: 154 minus 77 minus 77 is zero, so the egg takes up the same room at first, which you can check by multiplying on a calculator. A giant ball around the whole Earth does shrink, because Earth is inside it; mass outside only changes the shape. I wasn't sure whether the crumbs fill the ball or sit on its outside, how millimetres became parts in a million, why adding fractions works for an egg when the check used a box, why the egg later shrinks instead of growing, and whether the centre crumb counts as mass inside.

**Stumbles (30)**

- “How tides reshape a small falling ball of crumbs”: Two words for one idea: the tagline says 'tides' while every entry field says 'tidal drift', and 'tides' makes a reader think of the sea.
- “Let go of a small ball of crumbs ... so the ball becomes an egg with, at first, the same volume.”: 'A ball of crumbs' reads as a clump of crumbs, and the comma-wrapped 'at first' made the sentence a reread.
- “Only mass inside a ball of falling crumbs makes its volume start to change.”: Fails the first what-if: crumbs thrown outward change volume with no mass inside, and Einstein's theory adds a tiny growth in empty space. The rule is Newton's, for a release at rest.
- “Crumbs let go at rest inside it slowly drift compared with a centre crumb”: A step left implicit: nothing says why they drift, yet the first check's answer relies on 'only differences in pull show'.
- “Near a round planet they drift away along the line toward the planet's centre”: 'Away' from what?
- “hundreds of crumbs are held still on an imaginary ball 2 metres across, around one centre crumb”: Unclear whether the crumbs fill the ball or sit on its surface, held still relative to what, and where the centre crumb is.
- “A crumb 1 metre out on the line toward Earth's centre drifts away from the centre crumb by 0.154 millimetres.”: There are two such crumbs, one nearer Earth and one farther; the reader wonders whether the far one drifts too.
- “The ball becomes egg-shaped, longer along the line and narrower across it.”: First what-if: a real egg is fatter at one end, but this shape is the same at both ends.
- “Measure each change as a fraction of 1 metre. Along the line, the egg is longer by 154 parts in a million.”: A missing step: how 0.154 millimetres becomes 154 parts in a million.
- “You can check this with a box: 1.002 metres long and 0.999 metres wide and deep, it holds 0.999997 cubic metres.”: The reader must supply the comparison with 1 cubic metre and the zero sum of the box's fractions, and gets no reason for the tiny leftover.
- “For the egg, the sum is 154 minus 77 minus 77, which is zero.”: The check used a box, and an egg is not a box; the link is left implicit.
- “is called a volume-preserving tidal deformation”: 'Preserving' and 'deformation' are unfamiliar words.
- “Over a much longer fall, the egg's volume does start to shrink slowly.”: A surprise with no reason or number: why shrink rather than grow, and how slowly?
- “a block 2 parts in 100 longer ... for big changes, the fractions no longer add up.”: 'Block' and 'box' name one object, and 'the fractions no longer add up' is ambiguous: they still add to zero, but the sum stops giving the volume.
- “tidal drift stretches a small falling ball of crumbs along one line and squeezes it half as much in two directions across”: The takeaway names no line and drops 'let go at rest', so it fails for crumbs thrown apart.
- “Crumbs let go at rest in a cabin that falls freely near Earth drift.”: A reread: the verb arrives after a long subject. The recap also leaves out why the sum is zero.
- “400 kilometres above the ground, beyond the air. ... Each crumb is held still”: Not quite true (a thin trace of air remains at 400 kilometres), no everyday anchor for the height, and held still relative to what?
- “All the crumbs are the same distance from Earth's centre, so none falls ahead of the others. The ball stays round and shrinks.”: A step left implicit: falling toward Earth's centre is moving inward because Earth's centre is the ball's centre.
- “The ball's radius is 6,771 kilometres”: Where 6,771 comes from is not shown.
- “The ball is narrower by that fraction in each of three directions at right angles.”: Which three directions? A round ball shrinks in every direction.
- “Compare the small ball beside Earth.”: Which small ball, and is it fair to compare a ball measured with cabin rulers against one measured with rulers still relative to Earth?
- “The difference is what sits inside each ball. ... Newton's law of gravity turns this into a rule, which we take on trust here.”: A surprising claim with no reason: why should mass inside matter and mass outside not? 'Turns this into a rule' is vague.
- “Its walls pull on the crumbs very slightly, but they sit outside the small ball, so they cannot start to change its volume either.”: 'Its' and 'they' have two candidates each, and the first what-if is unanswered: the centre crumb is itself mass inside the ball.
- “A ball of crumbs let go at rest starts to shrink only when mass sits inside it.”: The takeaway is unscoped, while the way takes Newton's law on trust and Einstein's theory adds a tiny growth in empty space.
- “a ball of crumbs 2 metres across is let go at rest, with nothing among the crumbs ... drifts away from the centre crumb”: The check uses 'the centre crumb' without introducing it, and the starting arrangement is ambiguous.
- “The volume stays the same, to within 2 parts in 100 million.”: The entry ways gave no way to reach this figure.
- “with no air around them”: Air among the crumbs is what would matter, not only around them.
- “the ball stretches along the line toward the planet's centre by as much as it squeezes across that line in total”: A reread: 'in total' arrives at the end, after the reader has pictured one squeeze.
- “about 150 parts in a million, which is 0.015 per cent”: A missing step from parts in a million to per cent.
- “After a whole minute of falling,”: No setting: falling where? The numbers hold only near Earth.

**Fixes**

- Rewrote the tagline and summary to use 'tidal drift', spread the crumbs over the surface of an imaginary ball, and scoped the only-mass-inside rule to Newton's law and a release at rest.
- Egg way: said why crumbs drift, named both crumbs on the line, placed the centre crumb, converted millimetres to parts in a million, walked the box check step by step, and gave the reason for the tiny leftover. Added the sentence linking the box to the egg, defined 'preserving' and 'deformation' in the sentence before the term and in the glossary, added the one-minute number, and marked 'shrinks rather than grows' as taken on trust.
- Egg way try_it: one word ('box') for the object, and it now says the fractions still add to zero while the volume has changed.
- Whole-Earth way: gave Earth's radius, the space station as a height anchor, 'above almost all of the air', and the step that falling toward Earth's centre is moving inward. Said why cabin and ground rulers can be compared, and gave the reason mass inside and mass outside differ (all inward, against ahead-and-lag balancing). Answered the centre-crumb what-if with a size, and scoped the takeaway to Newton's law.
- Checks, problem, misconception and common question: introduced the centre crumb in the first check, said where its 2-parts-in-100-million leftover comes from, put the air among the crumbs, spelled out the per cent step, and gave the common question its setting.
- Checked numbers with python3: 1.002 x 0.999 x 0.999 = 0.999997; (1 + 154e-6)(1 - 77e-6)^2 = 1 - 1.8e-8, under 2 parts in 100 million; one crumb of 1 milligram 1 metre away moves a crumb about 3e-15 metres in ten seconds, far smaller than an atom; 435 m / 6,771 km = 64 parts in a million.
- Ladder: the working way 'Gauss's law counts the mass inside' now names the 193 parts in a million of 'A ball around the whole Earth shrinks' instead of 'the entry figure', and bridges from the entry rule that small fractions add to $\delta V/V \approx \sum_i \delta\ell_i/\ell_i$. Every non-entry way's first sentence already names the way it continues, index notation at working is covered through ricci-tensor, and the five ways use five different kinds.
- Budget: entry explanations grew from 646 to about 990 words, still under the 1,000 cap; extras 700 of 800; nothing was dropped or compressed.
- Bumped the revision to 2.

**Concerns**

- Physics reviewer: confirm the new entry claims: that the volume loss over a longer fall is a shrink (the entry prose takes this on trust), that a centre crumb's own pull is negligible (about 3e-15 metres in ten seconds for 1 milligram), and that cabin and ground rulers agree on the ball's size far more closely than 193 parts in a million.
- The entry prose attributes the only-mass-inside rule to Newton's law. It says nothing about the cosmological constant making a ball grow in empty space, beyond 'as closely as anyone could ever measure' in the egg way; the ricci-tensor entry way covers that exception.
- Entry explanations now sit near the 1,000-word core cap, so later entry additions will need cuts elsewhere.
- The 'egg' shape is a symmetric oval (both ends alike); the proposed visual falling-ring-of-crumbs should draw it that way, not as a real egg with one pointed end.
- Carried over from drafting: the conventions file has no symbols for an observer's tidal tensor or the electric and magnetic Weyl parts, and the GW170814 Bayes factors and the Bartelmann and Schneider reference still need checking.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 3)

**Verification**

- Entry drifts: a 1 m semi-axis released at rest near Earth's surface moves +0.154 mm along the line to the centre and -0.077 mm across it in 10 s; the 2 m ball grows 0.3 mm longer.: python: q = GM/R^3 with GM = 3.986e14, R = 6.371e6 gives 1.5414e-6 s^-2; radial q t^2, transverse q t^2/2, from eigenvalues (-2,1,1)q of the Newtonian tidal matrix. → 0.1541 mm and 0.0771 mm; length gain 0.308 mm, about four 77-micrometre hairs. Correct.
- Box arithmetic: 1.002 x 0.999 x 0.999 = 0.999997; 1.02 x 0.99 x 0.99 = 0.999702; 1.2 x 0.9 x 0.9 = 0.972.: python → Correct.
- Check squashed-or-stretched: leftover under 2 parts in 100 million.: python: (1+154e-6)(1-77e-6)^2 - 1; also the exact constant-tide volume cosh(sqrt(2q) t) cos^2(sqrt(q) t) at t = 10 s. → Product of rounded fractions -1.78e-8; true fourth-order tidal loss -1.19e-8 (= q^2 t^4 / 2). Both under 2e-8, so the statement is true either way. Numeric 0 percent with tolerance 0.001 percent is fine.
- Entry: over a longer fall the volume shrinks rather than grows.: Raychaudhuri in vacuum with theta(0) = 0, omega = 0: d theta/d tau = -theta^2/3 - sigma^2 <= 0, so theta <= 0 for all later times; fourth-order term -E_ij E_ij tau^4/12 < 0. → Correct for every later time before a caustic, for a nonrotating release. A release in a cabin turning with Earth adds growth 2 Omega^2 in the volume acceleration (+0.53 ppm in 10 s, +19 ppm in 60 s), which would reverse the one-minute figure; fixed by saying the cabin does not turn.
- Entry and worked example: after one minute the egg has lost about 15 parts in a million; radial axis +0.555 per cent, transverse -0.277 per cent, axis ratio 1.0084.: python with q = 1.54e-6 and q = 1.5414e-6: cosh(sqrt2 x), cos x, x = sqrt(q) 60; compared with q^2 t^4 / 2. → Volume ratio 0.9999846 (loss 1.54e-5); axes 1.005554, 0.997227; ratio 1.0084; fourth-order estimate 1.54e-5. Fall 17.7 km changes GM/r^3 by 0.83 per cent. Correct.
- Centre crumb: its pull moves the other crumbs far less than an atom's width in 10 s.: python: G m t^2 / (2 r^2) with m = 1 mg, r = 1 m; Newtonian volume effect -4 pi G m over V = 4.19 m^3. → Displacement 3.3e-15 m (atoms ~1e-10 m); fractional volume change ~1e-14 in 10 s. Correct.
- Rulers in the cabin and rulers still relative to Earth agree on the ball's size far more closely than 193 ppm.: Order of magnitude of relativistic ruler differences: GM/rc^2 ~ 7e-10, v^2/c^2 for a 98 m/s fall ~ 1e-13. → Correct; the Newtonian comparison is fair.
- Whole-Earth ball at 400 km: each crumb falls 435 m in 10 s, 64 ppm of 6,771 km, volume -193 ppm; working form -3GM/r^3 = -3.85e-6 s^-2.: python: g = GM/r^2, g t^2/2; 1-(1-f)^3; -4 pi G M / (4 pi r^3 / 3). → 434.7 m; 64.2 ppm; 192.6 ppm; 3.852e-6 s^-2 and 1.93e-4 in 10 s. Correct.
- Problem ball-around-earth-higher-up: 367 m fall at 7,371 km radius, about 150 ppm, 0.0149 percent.: python → 366.8 m; 49.8 ppm; 149.3 ppm = 0.01493 percent. Numeric within tolerance. Correct.
- Summary and ways: by Newton's law, only mass inside a ball let go at rest starts to change its volume; mass outside changes only its shape at first; more mass inside shrinks it faster.: Material-surface derivation: dV/dt = flux of v, second derivative at rest = flux of g = -4 pi G M_enc (divergence theorem); third derivative also vanishes at release for a static field since v and its gradients vanish. → Correct for any size and shape, Newtonian, release at rest in a nonrotating frame. Einstein-theory exception (Lambda) is outside the Newtonian scope; the egg way's "as closely as anyone could ever measure" covers Lambda c^2 ~ 1e-35 s^-2 (5e-34 fractional in 10 s). Accepted.
- Derivation volume-acceleration-from-gauss, steps 1-5.: Re-derived by hand; Poisson nabla^2 Phi = 4 pi G rho, g = -grad Phi. → Correct signs; small cloud gives -4 pi G rho = -tr d_i d_j Phi.
- Tidal eigenvalues (GM/r^3)(-2,1,1) and axis law l = l0(1 - lambda t^2 / 2).: Second derivatives of -GM/r; l'' = -lambda l. → Correct.
- GR trace: E^mu_mu = R_{nu sigma} u^nu u^sigma with the course geodesic-deviation sign; perfect fluid at rest gives 4 pi G(rho + 3p/c^2) - Lambda c^2.: Contracted the conventions deviation equation; trace-reversed Einstein equation with Lambda: R_mn = kappa(T_mn - T g_mn/2) + Lambda g_mn, T_mn u u = rho c^4, T = -rho c^2 + 3p, g_mn u u = -c^2. → Correct: volume law -R u u = -4 pi G(rho + 3p/c^2) + Lambda c^2, as the note states.
- Boosted observer at beta = 0.6 sideways past a spherical mass measures q diag(-3.6875, 2.6875, 1); E_ij E_ij = 21.82 q^2; time ratio 0.724.: Orthonormal Schwarzschild Riemann (R_trtr = -2q, R_tthetattheta = R_tphitphi = q, R_thetaphithetaphi = 2q, R_rthetartheta = R_rphirphi = -q; checked Ricci-flat). Boost u = gamma(e_t + beta e_phi): E'_rr = gamma^2(-2q - beta^2 q), E'_thetatheta = gamma^2(q + 2 beta^2 q), E'_phiphi = q; python. → -3.6875 q, 2.6875 q, 1 q (the unit entry is along the motion); sum of squares 21.8203; (6/21.82)^(1/4) = 0.7241. Correct.
- Kretschmann in vacuum 8(E.E - B.B); static observer E.E = 6M^2/r^6.: 48 M^2/r^6 / 8 = 6. → Correct.
- Derivation fourth-order-loss-in-vacuum, including the constant-tide check cosh(sqrt2 s) cos^2 s = 1 - s^4/2.: Hand series: B-dot = -B^2 - E from xi-dot = B xi; trace; tr E-dot = 0 removes tau^3; series of cosh and cos^2. → (1 + s^2 + s^4/6)(1 - s^2 + s^4/3) = 1 - s^4/2; E.E/12 = 1/2. Correct.
- Formal: sheared release in flat spacetime gives V/V0 = 1 - s^2 t^2 = 0.9964 at 60 s, V''/V = -2 s^2, sigma.sigma = 2 s^2.: Straight-line motion and determinant; python. → Correct.
- Formal: Lambda gives +Lambda c^2 about 1e-35 s^-2.: python: 3 H0^2 Omega_Lambda with H0 = 67.4 km/s/Mpc, Omega_Lambda = 0.685. → 9.8e-36 s^-2. Correct.
- Problem every-observer-keeps-volume: polarization argument and fluid with P = -rho/3 giving (16 pi/3) rho (gamma^2 - 1).: Hand algebra: T_mn u'u' = (rho + P) gamma^2 - P, T = -rho + 3P, g(u',u') = -1. → Correct, including the interval argument for R(v,v) = 0.
- Light bundle: area constant through third order in affine parameter in vacuum.: Sachs equations: sigma ~ C lambda, theta-dot ~ -|C|^2 lambda^2, ln A ~ -|C|^2 lambda^4/12. → Correct.
- Problem cube-around-earth: V''/V = -5.01e-9 s^-2, loss 9.0e-6 in 60 s; corners inside the Moon's orbit; short-time form accurate.: python: 4 pi GM / 1e24; half of that times 3600; free-fall distances at 50,000 km and 86,600 km from Earth's centre. → Rates correct. The solution said the corner particles fall about 0.1 m; they fall 96 m, and face-centre particles 287 m. Fixed; the short-time form remains accurate (287 m is 6e-6 of the half-width).
- Gravitational wave: tidal tensor -h+-double-dot diag(1,-1,0)/2, delta L_x / L = +h+/2; check mirror-arms-in-a-wave h+ = 1.0e-21, y row -2.0e-18 m, area factor 1 - h+^2/4 = 1 - 2.5e-43.: Linearized course Riemann R_i0j0 = -h_ij,00 / 2 in TT gauge; deviation equation; python. → Signs and numbers correct.
- GW150914: peak strain 1.0e-21; 4 km arms change by about 2e-18 m, difference 4e-18 m, about 400 times smaller than a proton.: python with proton diameter 1.68e-15 m; strain as (dLx - dLy)/L per the notation trap. → Ratio 420. Correct as stated.
- GOCE: 255 km altitude, radial -2.74e-6 s^-2, horizontal +1.37e-6 s^-2, 0.137 mm and 0.069 mm in 10 s; measurement band periods 10 to 200 s.: python: GM/r^3 at r = 6,626 km; band 5 to 100 mHz. → 1.370e-6 s^-2; 0.137 mm, 0.0685 mm. Correct. The band scoping also excludes the static self-gravity of the spacecraft.
- References: Rummel, Yi, Stummer 2011 J. Geod. 85, 777-790; Abbott et al. 2017 PRL 119, 141101; Owen, Brink, Chen, Kaplan et al. 2011 PRL 106, 151101; Bartelmann and Schneider 2001 Phys. Rep. 340, 291-472; Raychaudhuri 1955 Phys. Rev. 98, 1123-1126; Will 2014 Living Rev. Relativ. 17, 4.: Crossref API records for each DOI (web search budget was exhausted in this session). → All authors, years, titles, venues and pages confirmed; Bartelmann and Schneider DOI 10.1016/S0370-1573(00)00082-X and arXiv astro-ph/9912508 added. Set verified.
- Einstein 1915, Die Feldgleichungen der Gravitation, Sitzungsberichte (Berlin) 844-847.: Standard bibliographic record (25 November 1915 session), same record as elsewhere in the vault. → Confirmed; no DOI. Set verified.
- GW170814 Bayes factors about 200 (tensor vs vector) and 1000 (tensor vs scalar).: Compared with the published abstract as recalled and the internal study dossier. → Consistent: 200 and 1000. Accepted.

**Counterexamples tried**

- Cabin turning with Earth (once a day): crumbs at rest in the cabin share its rotation, and the vorticity term adds 2 Omega^2 = 1.06e-8 s^-2 of volume growth, +19 ppm in a minute, larger than the 15 ppm tidal loss. Broke the entry one-minute claim; fixed by a non-turning cabin in the egg way, summary, first check, common question and worked example.
- Lumpy, non-round planet or moon: the stretch is not along the line to the centre and the squeezes are not half as big, although the volume is still kept. Broke the summary, objective, egg takeaway and misconception wording "near a planet"; now "near a round planet".
- Crumbs thrown outward (initial expansion) or released with shear in flat spacetime: volume changes at once; entry text scoped to "let go at rest", formal way and check released-with-a-shear cover it.
- Positive cosmological constant: a ball released at rest in empty space grows at Lambda c^2 ~ 1e-35 s^-2. Entry statements are scoped to Newton's law, and the egg way's "as closely as anyone could ever measure" is true (5e-34 in 10 s).
- Large cloud beside Earth (not small): Newtonian volume acceleration still zero at release; in GR the finite-cloud volume is slicing dependent, as the working way says.
- Strong field, near a black hole: small-ball trace still zero in vacuum; ball must be small compared with the curvature radius, as the formal proposition states.
- Different observer at the same event (boost at 0.6c): the trace stays zero, E_ij E_ij changes from 6 to 21.82 q^2; handled by check passer-loses-volume-sooner.
- Non-static vacuum (gravitational wave): trace-free at all times; area kept to first order only, second order 1 - h^2/4, as stated.
- Massless case (light bundle): no Ricci focusing in vacuum, shear focusing at fourth order; stated.
- Non-vacuum fluid with rho + 3P = 0: comoving observer finds zero, others do not; problem every-observer-keeps-volume.
- Centre crumb and cabin walls as mass: walls outside, crumb inside but negligible (3e-15 m in 10 s). Statement true.
- Whole-Earth ball with the real, slightly flattened Earth: stays nearly round and shrinks by nearly 193 ppm; covered by simplifies and "about".

**Fixes**

- Summary, first entry objective, egg-way takeaway and the tides-squash-the-ball correction: "near a planet" became "near a round planet", since the line-and-half-squeeze picture needs a round planet.
- Egg-way takeaway: after adding 'round', split into short sentences and said 'the line to the planet's centre' to stay within 32 words per sentence and 240 characters; meaning unchanged.
- Egg way: added "The cabin does not turn as it falls." A cabin turning with Earth would add about 19 ppm of growth per minute, overturning the one-minute shrink figure. Summary, check squashed-or-stretched, the common question and the worked example (nonrotating cabin) say the same. Entry explanations now about 999 words, under the cap; nothing dropped.
- Problem cube-around-earth, step 4: replaced "the corner particles fall only about 0.1 m" (true value 96 m, and 287 m at face centres) with "at most about 300 m ... less than a hundred-thousandth of the cube's half-width".
- History, Raychaudhuri 1955: scoped to the freely falling dust of a cosmological model.
- All references set verified after Crossref confirmation; added DOI and arXiv id for Bartelmann and Schneider 2001.
- Bumped the revision to 3.

**Concerns**

- Novice re-read needed for the changed entry sentences: summary, objective, egg-way explanation and takeaway, first check question. The phrase "does not turn" should be checked for a reader who might ask "turn relative to what?".
- Registry prerequisites list only relativistic-tidal-tensor and ricci-tensor; poisson-equation-for-gravity is a registry id (no note yet), is a direct, acyclic prerequisite for the working Gauss-law way, and should be synced with sync_registry.py.
- The conventions file has no symbols for an observer's tidal tensor or the electric and magnetic Weyl parts; this note uses E_ij = R_{i0j0} and B_ij, which should be added there before other notes use them.
- The egg is a symmetric oval with both ends alike to leading order in the ball's size; the proposed visual falling-ring-of-crumbs should draw it that way.
- Web search was unavailable (session budget exhausted); references were confirmed through Crossref DOI records instead, and the GW170814 Bayes factors from the published abstract as known, not re-read in this session.
