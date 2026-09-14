---
type: "concept"
schema_version: 2
id: "hawking-radiation"
title: "Hawking radiation"
tagline: "Quantum physics makes black holes glow; without spin or charge, heavier ones glow colder"
domain: "quantum-gravity-and-beyond"
tier: "advanced"
status: "physics-reviewed"
revision: 7
updated: "2026-09-13"
aliases: ["Hawking effect", "Hawking emission", "black-hole radiance"]
prerequisites: ["horizon-pair-creation-picture", "black-body-spectrum", "gravitational-redshift", "unruh-effect", "surface-gravity", "quantum-field-theory-in-curved-spacetime"]
leads_to: ["hawking-temperature", "black-hole-evaporation", "black-hole-thermodynamics", "black-hole-information-problem", "primordial-black-hole"]
visuals: ["thermometer-beside-a-black-hole", "vacuum-pairs-near-a-horizon", "rays-peeling-off-a-forming-horizon"]
---

# Hawking radiation

*Quantum physics makes black holes glow; without spin or charge, heavier ones glow colder*

`hawking-radiation` · quantum-gravity-and-beyond · advanced · physics-reviewed (revision 7)

**Needs:** [[horizon-pair-creation-picture]] (entry) · [[black-body-spectrum]] (entry) · [[gravitational-redshift]] (working) · [[unruh-effect]] (working) · [[surface-gravity]] (formal) · [[quantum-field-theory-in-curved-spacetime]] (formal)  
**Opens:** [[hawking-temperature]] · [[black-hole-evaporation]] · [[black-hole-thermodynamics]] · [[black-hole-information-problem]] · [[primordial-black-hole]]  
**Related:** [[penrose-process]] · [[rindler-kruskal-analogy]] · [[cosmic-microwave-background]] · [[infinite-redshift-at-the-horizon]]  
**Visuals:** ★ [[thermometer-beside-a-black-hole]] · [[vacuum-pairs-near-a-horizon]] · [[rays-peeling-off-a-forming-horizon]]

> Quantum physics predicts that black holes are not perfectly black. A black hole gives off a faint glow, called Hawking radiation, and the energy the glow carries comes out of the hole's mass. For a hole without spin or electric charge, the heavier the hole, the colder the glow. A hole with the Sun's mass glows at about 60 billionths of a degree above absolute zero, far colder than the leftover glow of the early universe that fills space.

## You will be able to

**Entry**
- Explain why quantum physics makes a black hole glow, where the glow is made, and where its energy comes from. `objectives/explain-why-a-black-hole-glows` ← `checks/glow-in-empty-space`, `checks/light-from-behind-the-horizon`
- Predict how the temperature of the glow changes with the mass of a hole that has no spin or charge. `objectives/predict-temperature-from-mass` ← `checks/ten-suns-hole`, `problems/moon-mass-black-hole`
- Explain why real black holes take in more of the leftover glow from the early universe than they give off. `objectives/explain-why-real-holes-grow` ← `checks/real-hole-in-todays-sky`

**Working**
- Compute the Hawking temperature of a hole from its mass and compare it with the cosmic microwave background. `objectives/compute-hawking-temperature` ← `checks/sagittarius-a-star-temperature`, `problems/sky-matching-mass`
- Derive the Hawking temperature from the Unruh temperature of a hovering observer and gravitational redshift, for a static, spherically symmetric horizon. `objectives/derive-temperature-from-surface-gravity` ← `problems/charged-hole-temperature`
- Distinguish what distant, hovering and freely falling detectors record, including the sign of the partner energy. `objectives/distinguish-what-detectors-record` ← `checks/hovering-and-falling-detectors`, `checks/energy-of-the-partner`

**Formal**
- Explain how exponential redshift at a forming horizon produces a Planck spectrum, and state the hypotheses of the result. `objectives/explain-origin-of-planck-factor` ← `checks/what-the-pair-picture-derives`
- Show that tracing out partners from a pure pair state leaves a thermal state, and use this to evaluate claims about unitarity. `objectives/show-thermal-state-from-entanglement` ← `problems/partners-make-it-thermal`, `checks/thermal-but-pure`

**Research**
- Evaluate what analogue-horizon experiments can and cannot test about Hawking radiation. `objectives/evaluate-analogue-experiments` ← `checks/what-analogues-can-test`

## Ways in

### 1. A black hole that glows · entry · picture

*Can a black hole, which light cannot escape, give off anything at all?*

**Recap:** A warm object glows: it gives off light, mostly too red for eyes to see. Light is a wave, and it comes in tiny packets that count as particles. In quantum physics, empty space is never perfectly still: pairs of particles keep appearing for a moment and vanishing again.

In a dark room, a mug of hot water shows no light, yet a palm beside it feels warm. The mug glows with light too red for eyes to see.

A black hole is a region where gravity is so strong that nothing that enters, not even light, can come back out. Its edge is called the event horizon.

Stephen Hawking found that quantum physics makes a black hole glow faintly after all. In the pair picture, one member of a pair of particles near the horizon can cross the horizon before the pair vanishes. The other can then escape. The escaping particles form a faint glow, made outside the horizon. This glow is called Hawking radiation.

The glow carries energy away, and energy has mass. Counted from far away, the partner that fell in brings in negative energy. Take this on trust for now. So a hole alone in dark, empty space slowly gets lighter.

**Try it:** Fill a mug with hot tap water, and wrap half of its side in kitchen foil, shiny side out. Turn off the room light: the mug gives off no light you can see. Hold your palm a few centimetres beside the bare half, not above it and not touching. You feel warmth. Now hold your palm at the same distance beside the foil half. It feels noticeably cooler, although the water behind the foil is just as hot. Both halves warm the nearby air about equally, but shiny foil gives off very little glow. So a large part of the warmth you felt beside the bare half was the mug's invisible glow.

**Takeaway:** Quantum physics makes a black hole glow faintly, and the glow's energy comes out of the hole's mass.

*What this leaves out:* The pair picture is a cartoon, but it gets three things right. The glow is made outside the horizon, each escaping particle has a partner that falls in, and the energy comes out of the hole.

*Builds on:* [[horizon-pair-creation-picture]], [[black-body-spectrum]]<br>*Visuals:* [[vacuum-pairs-near-a-horizon]]

### 2. Mass and the temperature of the glow · entry · calculation

*How does the temperature of a black hole's glow depend on the hole's mass?*

**Recap:** Hawking radiation is the faint glow that quantum physics makes a black hole give off. In the pair picture, one member of a pair of particles near the horizon crosses the horizon, and the other escapes. A warmer object glows with shorter waves: twice as hot, half as long.

Measured from far away, Hawking radiation has a temperature. For a hole without spin or electric charge, the glow's waves grow longer in step with the hole's width. A hole twice as heavy is twice as wide, so its waves are twice as long, and it glows at half the temperature.

A hole with the Sun's mass is about 6 kilometres across. Its glow is about 60 billionths of a degree above absolute zero. Most of the glow's energy comes in waves tens of kilometres long. Waves that long are not made at single spots on the horizon, so the pair picture is only a cartoon.

**Takeaway:** For holes without spin or charge, a heavier hole glows colder: twice the mass, half the temperature.

*What this leaves out:* Spinning or charged holes of the same mass glow more coldly. The curved space around a hole sends part of the glow back in, more of the longer waves than the shorter ones. So the glow's mix of waves differs from a warm object's, although one temperature still sets it.

*Continues:* `ways_in/a-black-hole-that-glows`<br>*Builds on:* [[horizon-pair-creation-picture]], [[black-body-spectrum]]<br>*Visuals:* [[thermometer-beside-a-black-hole]]

### 3. Colder than the sky · entry · contrast

*Why has nobody detected the glow of a real black hole?*

**Recap:** Hawking radiation is the faint glow a black hole gives off because of quantum physics. Measured from far away, a hole with the Sun's mass and no spin or charge glows at about 60 billionths of a degree above absolute zero, the coldest possible temperature. Any heavier hole glows more coldly than that hole. An object takes in more glow from warmer surroundings than it gives off, as a cold stone warms in sunshine.

The early universe was a hot, glowing gas. Its glow cooled as the universe expanded, but still arrives from every direction. This leftover glow is called the cosmic microwave background. It is about 2.7 degrees above absolute zero, more than 40 million times warmer than a Sun-mass hole's glow.

So a Sun-mass hole takes in more glow than it gives off. Energy has mass, so the hole grows.

Every black hole found so far is heavier than the Sun, so its glow is even colder. That faint, cold glow is lost in the warmer leftover glow, so nobody has detected Hawking radiation from a real black hole. Only a hole lighter than about six tenths of the Moon's mass would glow warmer than the leftover glow.

Even without the leftover glow, a Sun-mass hole with no spin or charge glows far too faintly to detect from Earth. Light comes in tiny packets. In 50 years, the hole gives off less energy than one packet of green light carries.

**Takeaway:** Every known black hole glows far more coldly than the leftover glow from the early universe, so it takes in more than it gives off, and its Hawking radiation stays hidden.

*What this leaves out:* Gas and stars falling in usually feed real black holes far more than the leftover glow does. If the universe keeps expanding as it does now, the leftover glow keeps cooling, so in the very distant future even heavy holes will glow warmer than it and shrink.

*Continues:* `ways_in/a-black-hole-that-glows`, `ways_in/mass-and-temperature`<br>*Builds on:* [[black-body-spectrum]]<br>*Visuals:* [[thermometer-beside-a-black-hole]]<br>*See:* `observations/cosmic-microwave-background-temperature`

### 4. The temperature from a hovering thermometer · working · calculation

*Where does the value of the Hawking temperature come from, and why does it fall as one over the mass?*

In "Mass and the temperature of the glow", a Sun-mass hole glows at about 60 billionths of a degree, and a hole twice as heavy, being twice as wide, emits waves twice as long and glows at half the temperature. Dimensional analysis explains that trend. A temperature enters as the energy $k_BT$, and a quantum effect of gravity near a mass $M$ can involve only $\hbar$, $c$, $G$ and $M$. Those four build more than one energy, such as $Mc^2$ and the Planck energy, but a first quantum effect on a classical hole is proportional to $\hbar$. The only rate built from $c$, $G$ and $M$ is $c^3/GM$, so $k_BT_H \propto \hbar c^3/GM$. The number in front needs physics.

Two results, taken on trust here, supply it. The Unruh effect: an observer with constant proper acceleration $a$, in the vacuum of flat spacetime, registers a thermal bath at $k_BT = \hbar a/2\pi c$. The exact redshift law for observers at rest outside a spherical mass: a quantum climbing from radius $r$ to far away has its frequency multiplied by the lapse $N = \sqrt{1 - r_s/r}$, with $r_s = 2GM/c^2$.

The physical input is the quantum state. Long after a star collapses, a freely falling observer crossing the horizon of a large hole finds nothing special: over regions much smaller than $r_s$, the field looks like the vacuum of flat spacetime. The calculation in "Mode mixing across the horizon" shows that collapse produces this state.

Now hold a thermometer at rest outside the horizon. It must accelerate outward with proper acceleration $a = GM/(r^2N)$, which grows without bound as $r \to r_s$. Close to the horizon its surroundings are a small, nearly flat region in vacuum, so it registers the Unruh temperature for the radiation coming up from the horizon. That radiation climbs out with each frequency multiplied by $N$ and the number of quanta in each mode unchanged. So a Planck spectrum at $T$ arrives far away as a Planck spectrum at $NT$, apart from the part scattered back, and

$$k_BT_\infty = \frac{\hbar Na}{2\pi c} = \frac{\hbar}{2\pi c}\,\frac{GM}{r^2}.$$

The Unruh step is trustworthy only where the thermal length $\hbar c/k_BT = 2\pi c^2/a$ is much smaller than $r_s$, which forces $r \to r_s$. In that limit $Na \to GM/r_s^2 = c^4/4GM$. This is the surface gravity $\kappa$: the force per unit mass needed at the far end of a rope that holds an object at rest at the horizon. So

$$k_BT_H = \frac{\hbar\kappa}{2\pi c} = \frac{\hbar c^3}{8\pi GM},$$

which is $6.17\times10^{-8}$ K for one solar mass and scales as $1/M$. Every quantum field sees the same temperature, because it is fixed by the geometry near the horizon rather than by the field. The derivation "Temperature from a hovering thermometer" lists each step.

**Takeaway:** The Hawking temperature is the Unruh temperature of a thermometer hovering at the horizon, redshifted to far away, so it is set by the surface gravity and falls as one over the mass.

*What this leaves out:* Uses the near-horizon limit for a static, uncharged, spherical hole, and ignores the radiation scattered back toward the hole.

*Continues:* `ways_in/mass-and-temperature`<br>*Builds on:* [[unruh-effect]], [[gravitational-redshift]]<br>*See:* `derivations/temperature-from-a-hovering-thermometer`, `worked_examples/a-sun-mass-hole-in-numbers`, `problems/charged-hole-temperature`

### 5. What a distant detector records · working · operational

*What would a detector far from the hole record, and what would detectors closer in record?*

The temperature from a hovering thermometer describes how quanta are shared among modes, not a hot surface. A detector at rest far away counts quanta of each species in each mode: a spherical wave with angular numbers $\ell$, $m$ and a polarization. Taken on trust from the formal mode calculation, the arrival rate per unit angular frequency in one mode is

$$\frac{dN}{dt\,d\omega} = \frac{1}{2\pi}\,\frac{\Gamma_\ell(\omega)}{e^{\hbar\omega/k_BT_H} \mp 1},$$

with $-$ for bosons and $+$ for fermions. The greybody factor $\Gamma_\ell(\omega)$ is the fraction of a wave in that mode, sent in from far away, that the hole absorbs. Waves much longer than $r_s$, and modes with large $\ell$, mostly bounce off the curved space around the hole, so for them $\Gamma_\ell \ll 1$. Short waves are absorbed as if by a disc of area $27\pi G^2M^2/c^4$. The spectrum is therefore a grey body at an exact temperature, not a perfect black body.

For a solar-mass hole, $k_BT_H = 8.5\times10^{-31}$ J, or $5.3\times10^{-12}$ eV with 1 eV $= 1.602\times10^{-19}$ J. The photons are radio waves at kilohertz frequencies, tens of kilometres long, while $r_s = 2.95$ km. Particles whose rest energy far exceeds $k_BT_H$ are exponentially rare in the flux.

The emitted energy comes out of the hole's mass as measured far away: $dM/dt = -L/c^2$ for total power $L$. Since $T_H \propto 1/M$ and the absorbing area scales as $M^2$, $L \propto M^2T_H^4 \propto 1/M^2$.

Who records what:

- A detector at rest far away records the grey-body stream at $T_H$.
- A detector held at rest near the horizon, where the lapse is $N$, records radiation coming up from the horizon with a thermal spectrum at about $T_H/N$, because it accelerates hard.
- A detector falling freely across the horizon of a large hole records nothing special there; the energy density it measures stays finite, on the scale $\hbar c/r_s^4$ set by the hole's size.
- Any real detector also receives the cosmic microwave background at $2.7255$ K, warmer than $T_H$ for every hole heavier than $4.5\times10^{22}$ kg.

**Takeaway:** A distant detector records a grey-body stream at the Hawking temperature, a detector hovering near the horizon records it much hotter, and a freely falling detector finds nothing special at the horizon.

*What this leaves out:* Ignores the slow change of the hole's mass while the flux is recorded, and absorption by matter between hole and detector.

*Continues:* `ways_in/temperature-from-a-hovering-thermometer`<br>*Builds on:* [[black-body-spectrum]]<br>*Visuals:* [[thermometer-beside-a-black-hole]]<br>*See:* `checks/hovering-and-falling-detectors`, `checks/energy-of-the-partner`, `observations/cosmic-microwave-background-temperature`

### 6. Mode mixing across the horizon · formal · structure

*How does gravitational collapse turn the vacuum into a thermal flux, and what does the result assume?*

The temperature from a hovering thermometer rested on an assumption: near the horizon, freely falling observers see the field in its flat-spacetime vacuum. Here both that state and the thermal flux come out of one calculation. Set $G = c = \hbar = k_B = 1$ in this way.

Take a free massless scalar field on the fixed, asymptotically flat spacetime of a star collapsing to a non-extremal black hole. Retarded time $u$ labels future null infinity $\mathscr I^+$, and advanced time $v$ labels past null infinity $\mathscr I^-$. In-modes $f_{\omega'} \propto e^{-i\omega' v}/r$ on $\mathscr I^-$ define the in-vacuum $|0_{\rm in}\rangle$, with no incoming quanta. Out-modes $p_\omega \propto e^{-i\omega u}/r$ on $\mathscr I^+$ define what a distant detector counts. Expanding $p_\omega = \int d\omega'\,(\alpha_{\omega\omega'}f_{\omega'} + \beta_{\omega\omega'}\bar f_{\omega'})$, a Bogoliubov transformation, the in-vacuum contains $\langle N_\omega\rangle = \int d\omega'\,|\beta_{\omega\omega'}|^2$ out-quanta.

Geometry supplies $\beta$. Trace an outgoing ray back from $\mathscr I^+$: it crossed the centre of the star and began on $\mathscr I^-$ as an ingoing ray. Late rays hug the horizon, whose generators left $\mathscr I^-$ at one advanced time $v_0$. Near the horizon a coordinate regular across it, such as the Kruskal $U = -4Me^{-u/4M}$ for Schwarzschild, depends exponentially on $u$, and through the smooth interior of the star it depends smoothly on $v$. Hence $v_0 - v = Ce^{-\kappa u}$ at late $u$, where the surface gravity $\kappa$ is defined on the horizon by $\xi^\nu\nabla_\nu\xi^\mu = \kappa\,\xi^\mu$ for the Killing vector that generates the horizon, normalized so its time part is $\partial_t$ at infinity ($\partial_t + \Omega_H\partial_\phi$ for a rotating hole); $\kappa = 1/4M$ for Schwarzschild.

A late out-mode, traced back, reaches $\mathscr I^-$ as $\exp[(i\omega/\kappa)\ln((v_0 - v)/C)]$ for $v < v_0$ and vanishes for $v > v_0$. Its oscillations pile up without limit as $v \to v_0$, so it is not built from positive frequencies in $v$ alone. The derivation "The Planck factor from exponential redshift" shows $|\beta_{\omega\omega'}| = e^{-\pi\omega/\kappa}|\alpha_{\omega\omega'}|$, and normalization then gives

$$\langle N_\omega\rangle = \frac{\Gamma_\omega}{e^{2\pi\omega/\kappa} - 1},$$

a Planck distribution at $T_H = \kappa/2\pi$ filtered by the greybody factor. Fermions give $+1$ in the denominator. For a Kerr–Newman hole, with $4\pi\varepsilon_0 = 1$, the exponent holds $\omega - m\Omega_H - q\Phi_H$ for a field of charge $q$.

The result rests on these hypotheses:

- The background is classical and fixed, so back-reaction is neglected; this is consistent while $M$ is far above the Planck mass.
- The state is regular across the future horizon; the in-vacuum and any state that looks like vacuum at short distances give the same late flux.
- Retarded times are many multiples of $1/\kappa$ after the horizon forms; earlier transients depend on the collapse, the late flux does not.
- Modes are traced through the region of exponential redshift by geometric optics.
- The hole is non-extremal, $\kappa \ne 0$; an extremal Reissner–Nordström hole has $T_H = 0$.

The global state stays pure. Each late out-packet has a partner packet behind the horizon, and with $\Gamma_\omega = 1$ the in-vacuum restricted to the pair is the two-mode squeezed state $\propto \sum_n e^{-n\pi\omega/\kappa}|n\rangle_{\rm out}|n\rangle_{\rm partner}$. Tracing out the partner leaves a thermal density matrix. The radiation is thermal because it is entangled with quanta no outside detector can reach.

One hypothesis is uncomfortable. A quantum reaching $\mathscr I^+$ at late $u$ with frequency $\omega$ traces back to a frequency of order $\omega e^{\kappa u}$ near the horizon. For a solar-mass hole that passes the Planck frequency about 2 ms after the horizon forms, so the calculation borrows modes from untested scales.

**Takeaway:** Exponential redshift at the horizon mixes positive and negative frequencies, so the in-vacuum holds a late Planck flux at surface gravity over two pi, entangled with partners behind the horizon.

*What this leaves out:* A free, massless test field on a fixed background; interactions between fields and back-reaction on the geometry are left out.

*Continues:* `ways_in/temperature-from-a-hovering-thermometer`<br>*Builds on:* [[quantum-field-theory-in-curved-spacetime]], [[surface-gravity]]<br>*Visuals:* [[rays-peeling-off-a-forming-horizon]]<br>*See:* `derivations/planck-factor-from-exponential-redshift`, `problems/partners-make-it-thermal`, `checks/thermal-but-pure`, `checks/what-the-pair-picture-derives`

### 7. Horizons in flowing fluids · research · bridge

*Can the Hawking effect be tested without a black hole, and does it survive unknown short-distance physics?*

Mode mixing across the horizon used two ingredients: a wave equation on a fixed geometry, and exponential redshift at a horizon. Neither needs Einstein's equations, so the effect can be studied without gravity.

In 1981 Unruh pointed out that sound in a moving fluid obeys such an equation. For an inviscid, irrotational, barotropic flow with velocity $\mathbf v$, density $\rho$ and local sound speed $c_s$, small perturbations of the velocity potential obey the wave equation of the acoustic metric

$$ds^2 = \frac{\rho}{c_s}\left[-(c_s^2 - v^2)\,dt^2 - 2\,\mathbf v\cdot d\mathbf x\,dt + d\mathbf x\cdot d\mathbf x\right].$$

Where a stationary flow speeds up through $c_s$, sound cannot travel upstream: an acoustic horizon. For flow along $x$, the surface gravity is $\kappa = |d(c_s - |v|)/dx|$ at the horizon, a rate in inverse seconds, and the mode analysis predicts phonons at $k_BT = \hbar\kappa/2\pi$. A gradient of $1000\ \mathrm{s^{-1}}$ gives $1.2\times10^{-9}$ K, hopeless in water but within reach of Bose–Einstein condensates.

The analogy also probes the uncomfortable hypothesis: late quanta trace back to arbitrarily short wavelengths. A real fluid has no arbitrarily short wavelengths. In a condensate the dispersion relation $\omega^2 = c_s^2k^2 + (\hbar k^2/2m)^2$ bends upward beyond $k \sim 1/\xi$, with $\xi$ the healing length, so outgoing modes are fed by incoming short-wavelength modes converted near the horizon instead. Analytic and numerical studies of such dispersive models, begun in the mid-1990s, recover the thermal spectrum at $\hbar\kappa/2\pi$ when $\kappa$ is small compared with the dispersive frequency scale, here $c_s/\xi$. This supports the view that the Hawking flux does not depend on unknown physics near the Planck scale, although spacetime need not behave like a fluid with a preferred rest frame.

Experiments now test the kinematics. Water flowing over an obstacle in a flume showed stimulated conversion of surface waves into negative-frequency waves, with a thermal dependence on frequency. Flowing condensates of rubidium atoms have been reported to show spontaneous emission: correlated and entangled phonon pairs across an acoustic horizon, and a spectrum consistent with thermal at the temperature set by the flow's $\kappa$. None of this tests the gravitational parts: back-reaction on the geometry, the end of evaporation, or the fate of information.

**Takeaway:** Sound in flowing fluids has horizons too, so Hawking's kinematics, including its insensitivity to short-distance physics, can be tested in the laboratory, though gravity's own role cannot.

*What this leaves out:* Treats the fluid as inviscid, irrotational and barotropic; real condensates add finite temperature, three-dimensional structure and atom losses.

*Continues:* `ways_in/mode-mixing-across-the-horizon`<br>*Builds on:* [[quantum-field-theory-in-curved-spacetime]]<br>*See:* `observations/analogue-hawking-radiation-in-a-condensate`, `checks/what-analogues-can-test`, `research_horizon/analogue-gravity`, `research_horizon/trans-planckian-problem`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| glow | — | Light and other radiation that an object gives off because of its temperature. The hotter the object, the brighter and bluer the glow, and most glows are invisible to eyes. | [[black-body-spectrum]] |
| black hole | — | A region of space where gravity is so strong that nothing that enters it, not even light, can come back out. | [[black-hole]] |
| event horizon | — | The edge of a black hole. Anything that crosses it can never come back out. | [[event-horizon]] |
| quantum physics | KWON-tum | The physics of atoms, light and other very small things. In it, energy comes in tiny packets and empty space is never perfectly still. | — |
| pair of particles | — | Two particles that appear together in empty space for a brief moment and then vanish again, as quantum physics allows. The member that falls into a black hole is the partner. | [[vacuum-fluctuations]] |
| Hawking radiation | HAW-king ray-dee-AY-shun | The faint glow that quantum physics predicts a black hole gives off. It carries energy away from the hole. | [[hawking-radiation]] |
| pair picture | — | A cartoon of how a black hole glows: one member of a pair of particles near the horizon crosses the horizon, and the other escapes. It helps you imagine the glow, but it is not the calculation that predicts the glow. | [[horizon-pair-creation-picture]] |
| absolute zero | — | The coldest possible temperature, about 273 degrees Celsius below the freezing point of water. Temperatures here count upward from it, in Celsius-sized degrees. | — |
| cosmic microwave background | — | The faint glow left over from the hot early universe, called the leftover glow for short. It arrives from every direction at about 2.7 degrees above absolute zero. | [[cosmic-microwave-background]] |

## Key equations

### Hawking temperature of a non-rotating hole · working

$$
k_BT_H = \frac{\hbar c^3}{8\pi GM}
$$

The temperature, measured far away, of the thermal flux from a non-rotating, uncharged black hole of mass $M$; it falls as $1/M$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $T_H$ | Hawking temperature, measured far from the hole | T H, the Hawking temperature |
| $M$ | mass of the hole | M |
| $\hbar$ | reduced Planck constant | h bar |
| $k_B$ | Boltzmann constant | k B |

**Holds when:** Non-rotating, uncharged hole, long after it forms; test fields on a fixed background, so $M$ far above the Planck mass.  
**Say it:** “k B times T H equals h bar c cubed over eight pi G M.”  
**Justified by:** `derivations/temperature-from-a-hovering-thermometer`

### Temperature from surface gravity · working

$$
k_BT_H = \frac{\hbar\kappa}{2\pi c},\qquad \kappa = \lim_{r\to r_s} Na = \frac{c^4}{4GM}
$$

The temperature is fixed by the surface gravity $\kappa$, the redshifted acceleration of an object held at rest at the horizon.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\kappa$ | surface gravity, an acceleration | kappa, the surface gravity |
| $N$ | lapse $\sqrt{1 - r_s/r}$ of a static observer | N, the lapse |
| $a$ | proper acceleration of a static observer | a |

**Holds when:** The last equality is for a non-rotating, uncharged hole. The first equality also holds for charged and rotating non-extremal holes, as the formal mode calculation shows, with $\kappa$ then defined from the Killing vector that generates the horizon; for a rotating hole no observer stays at rest near the horizon, so the limit of $Na$ does not apply.  
**Say it:** “k B T H equals h bar kappa over two pi c, and for a non-rotating hole kappa is c to the fourth over four G M.”  
**Justified by:** `derivations/temperature-from-a-hovering-thermometer`

### Unruh temperature · working

$$
k_BT_U = \frac{\hbar a}{2\pi c}
$$

An observer with constant proper acceleration $a$ in the vacuum of flat spacetime registers a thermal bath at this temperature.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $a$ | proper acceleration, read on the observer's accelerometer | a |
| $T_U$ | Unruh temperature | T U |

**Holds when:** Uniform acceleration in the vacuum of flat spacetime; near a horizon, only over regions much smaller than the curvature radius.  
**Say it:** “k B T U equals h bar a over two pi c.”  
**Justified by:** `unruh-effect`

### Exponential peeling of outgoing rays · formal

$$
v_0 - v = C\,e^{-\kappa u}
$$

An outgoing ray that reaches far away at late retarded time $u$ left past null infinity at an advanced time exponentially close to $v_0$, where the last ray that forms the horizon began.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $v_0$ | advanced time at which the horizon generators left past null infinity | v zero |
| $u$ | retarded time at future null infinity | u |
| $C$ | positive constant set by the collapse | C |

**Holds when:** $G = c = 1$; late times, $u$ many multiples of $1/\kappa$ after the horizon forms; non-extremal hole. For Schwarzschild $\kappa = 1/4M$.  
**Say it:** “v zero minus v equals C times e to the minus kappa u.”  
**Justified by:** `stated`

### Late-time occupation number · formal

$$
\langle N_\omega\rangle = \frac{\Gamma_\omega}{e^{2\pi\omega/\kappa} - 1}
$$

The expected number of quanta in a late outgoing wave packet of frequency $\omega$: a Planck distribution at $T_H = \kappa/2\pi$ filtered by the greybody factor.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\langle N_\omega\rangle$ | expected number of quanta in a late wave packet of frequency $\omega$ | the expected number N omega |
| $\Gamma_\omega$ | greybody factor, the fraction of the mode absorbed by the hole | gamma omega, the greybody factor |
| $\kappa$ | surface gravity | kappa |

**Holds when:** $G = c = \hbar = k_B = 1$; free massless boson in the in-vacuum on a fixed collapse background; late retarded times; non-extremal hole. Fermions have $+1$; for rotating or charged holes the exponent holds $\omega - m\Omega_H - q\Phi_H$.  
**Say it:** “The expected number N omega equals gamma omega over e to the two pi omega over kappa, minus one.”  
**Justified by:** `derivations/planck-factor-from-exponential-redshift`

## Derivations

### Temperature from a hovering thermometer · working

**Goal:** Show that a non-rotating, uncharged hole radiates at $k_BT_H = \hbar c^3/8\pi GM$, measured far away, from the Unruh temperature and gravitational redshift.

1. Assume that long after the collapse, freely falling observers near the horizon find the field in the vacuum of flat spacetime over regions much smaller than $r_s$. The formal mode calculation justifies this.
2. A static observer at radius $r$ has proper acceleration $a = GM/(r^2N)$, with lapse $N = \sqrt{1 - r_s/r}$ and $r_s = 2GM/c^2$ (stated).
3. In a small, nearly flat region in vacuum, an observer with proper acceleration $a$ registers a thermal spectrum at $k_BT_{\rm loc} = \hbar a/2\pi c$ (the Unruh effect, stated).
4. A quantum climbing from $r$ to far away has its frequency multiplied by $N$, and each mode keeps its number of quanta, so a Planck spectrum at $T_{\rm loc}$ arrives as a Planck spectrum at $NT_{\rm loc}$, apart from the part scattered back.
5. Combining, $k_BT_\infty = \hbar Na/2\pi c = \hbar GM/2\pi cr^2$.
6. Step 3 needs the thermal length $\hbar c/k_BT_{\rm loc} = 2\pi c^2/a$ to be much smaller than $r_s$, which holds only as $r \to r_s$, where $a \to \infty$.
7. In that limit $Na = GM/r^2 \to GM/r_s^2 = c^4/4GM \equiv \kappa$, so $k_BT_H = \hbar\kappa/2\pi c = \hbar c^3/8\pi GM$.

**Result:** $k_BT_H = \hbar\kappa/2\pi c = \hbar c^3/8\pi GM$, with $\kappa = c^4/4GM$.

### The Planck factor from exponential redshift · formal

**Goal:** With $G = c = \hbar = k_B = 1$, show that the in-vacuum contains $\langle N_\omega\rangle = \Gamma_\omega/(e^{2\pi\omega/\kappa} - 1)$ late out-quanta.

1. Out-modes on $\mathscr I^+$ are $p_\omega = e^{-i\omega u}/(r\sqrt{4\pi\omega})$ and in-modes on $\mathscr I^-$ are $f_{\omega'} = e^{-i\omega' v}/(r\sqrt{4\pi\omega'})$, each times a spherical harmonic; positive frequency means $e^{-i\omega t}$.
2. Write $p_\omega = \int_0^\infty d\omega'\,(\alpha_{\omega\omega'}f_{\omega'} + \beta_{\omega\omega'}\bar f_{\omega'})$ on $\mathscr I^-$. Fourier inversion gives $\alpha_{\omega\omega'} = \frac{\sqrt{4\pi\omega'}}{2\pi}\int dv\,e^{+i\omega' v}\,rp_\omega$ and $\beta_{\omega\omega'} = \frac{\sqrt{4\pi\omega'}}{2\pi}\int dv\,e^{-i\omega' v}\,rp_\omega$.
3. Late rays obey $v_0 - v = Ce^{-\kappa u}$. So the part of $p_\omega$ that entered the collapsing star reaches $\mathscr I^-$ as $t_\omega\,e^{(i\omega/\kappa)\ln((v_0 - v)/C)}/(r\sqrt{4\pi\omega})$ for $v < v_0$ and zero for $v > v_0$, with $|t_\omega|^2 = \Gamma_\omega$.
4. Put $x = v_0 - v$. Up to one common factor, $\alpha_{\omega\omega'} \propto e^{i\omega' v_0}\int_0^\infty dx\,x^{i\omega/\kappa}e^{-i\omega' x}$ and $\beta_{\omega\omega'} \propto e^{-i\omega' v_0}\int_0^\infty dx\,x^{i\omega/\kappa}e^{+i\omega' x}$.
5. With a convergence factor $e^{-\epsilon x}$, $\int_0^\infty x^{s-1}e^{-bx}\,dx = \Gamma(s)\,b^{-s}$ for $s = 1 + i\omega/\kappa$, where $b = \epsilon + i\omega'$ for $\alpha$ and $b = \epsilon - i\omega'$ for $\beta$, so $\arg b \to +\pi/2$ and $-\pi/2$.
6. $|b^{-s}| = |b|^{-1}\exp(\operatorname{Im}s\,\arg b) = \omega'^{-1}e^{\pm\pi\omega/2\kappa}$, with the upper sign for $\alpha$. Hence $|\beta_{\omega\omega'}| = e^{-\pi\omega/\kappa}|\alpha_{\omega\omega'}|$.
7. The Klein–Gordon norm of the part that entered the star is $\Gamma_\omega = \int d\omega'\,(|\alpha_{\omega\omega'}|^2 - |\beta_{\omega\omega'}|^2) = (e^{2\pi\omega/\kappa} - 1)\int d\omega'\,|\beta_{\omega\omega'}|^2$.
8. So $\langle N_\omega\rangle = \int d\omega'\,|\beta_{\omega\omega'}|^2 = \Gamma_\omega/(e^{2\pi\omega/\kappa} - 1)$. For plane-wave modes both sides grow with the time elapsed; wave packets make them finite, giving $\Gamma_\omega\,d\omega\,dt/2\pi(e^{2\pi\omega/\kappa} - 1)$ quanta.

**Result:** $\langle N_\omega\rangle = \Gamma_\omega/(e^{2\pi\omega/\kappa} - 1)$, a Planck factor at $T_H = \kappa/2\pi$; in SI units $k_BT_H = \hbar\kappa/2\pi c$ with $\kappa$ an acceleration.

## Worked examples

### A solar-mass hole in numbers · working

**Problem:** For a non-rotating, uncharged hole of one solar mass, with $GM_\odot = 1.327\times10^{20}\ \mathrm{m^3\,s^{-2}}$, find $r_s$, $\kappa$, $T_H$, $k_BT_H$ in eV, and the wavelength at which a black-body spectrum at $T_H$ peaks per unit wavelength. Compare that wavelength with $r_s$.

1. $r_s = 2GM/c^2 = 2\times1.327\times10^{20}/(2.998\times10^8)^2 = 2953$ m.
2. $\kappa = c^4/4GM = c^2/2r_s = 1.52\times10^{13}\ \mathrm{m/s^2}$.
3. $T_H = \hbar\kappa/2\pi ck_B = 6.17\times10^{-8}$ K.
4. $k_BT_H = 8.52\times10^{-31}$ J $= 5.32\times10^{-12}$ eV.
5. Wien's law gives $\lambda_{\rm peak} = 2.898\times10^{-3}\ \mathrm{m\,K}/T_H = 4.70\times10^4$ m $= 47$ km, about $16\,r_s$.

**Answer:** $r_s = 2.95$ km, $\kappa = 1.52\times10^{13}\ \mathrm{m/s^2}$, $T_H = 6.17\times10^{-8}$ K, $k_BT_H = 5.3\times10^{-12}$ eV, and $\lambda_{\rm peak} = 47$ km $\approx 16\,r_s$.

**Takeaway:** The thermal waves are far longer than the hole, so the cartoon of a pair splitting at one point of the horizon should not be taken literally.

## Problems

### `moon-mass-black-hole` · entry · difficulty 1 · estimate

The Sun is about 27 million times heavier than the Moon. Measured from far away, a black hole with the Sun's mass glows at about 60 billionths of a degree above absolute zero. About how warm is the glow of a black hole with the Moon's mass? Neither hole spins or has electric charge. Is the Moon-mass hole's glow warmer or colder than the leftover glow from the early universe, at about 2.7 degrees above absolute zero?

**Hints**

1. A lighter hole glows more warmly: the temperature goes up by the same factor that the mass goes down.
2. Multiply 60 billionths of a degree by 27 million.

**Answer:** About 1.6 degrees above absolute zero. That is still colder than the leftover glow from the early universe.

**Must contain:** A hole 27 million times lighter glows 27 million times more warmly; About 1.6 degrees above absolute zero; Still colder than the leftover glow, so it takes in more than it gives off

**Numeric:** temperature of the glow = 1.67 K (magnitude, ±10%)

**Solution**

1. A hole 27 million times lighter glows 27 million times more warmly.
2. 60 times 27 is 1,620. A billionth times a million is a thousandth. So the glow is 1,620 thousandths of a degree, about 1.6 degrees.
3. The leftover glow is about 2.7 degrees. So the Moon-mass hole is still colder, and it takes in more glow than it gives off.

**Targets:** `heavier-means-hotter`, `every-black-hole-is-shrinking`

### `sky-matching-mass` · working · difficulty 2 · calculation

Find the mass of a non-rotating, uncharged black hole whose Hawking temperature equals the cosmic microwave background temperature, $2.7255$ K. Give it in kilograms and in Moon masses ($7.342\times10^{22}$ kg), and give its Schwarzschild radius.

**Hints**

1. Solve $k_BT_H = \hbar c^3/8\pi GM$ for $M$.
2. Then $r_s = 2GM/c^2$.

**Answer:** $M = 4.50\times10^{22}$ kg, about 0.61 Moon masses, with $r_s = 6.7\times10^{-5}$ m. Every heavier hole is colder than the background and grows.

**Must contain:** M equals h bar c cubed over eight pi G k B T; About 4.5 times ten to the twenty-two kilograms, 0.61 Moon masses; Schwarzschild radius about 67 micrometres

**Numeric:** mass = 4.5e+22 kg (magnitude, ±2%); mass in Moon masses = 0.613 1 (magnitude, ±2%); Schwarzschild radius = 6.69e-05 m (magnitude, ±2%)

**Solution**

1. $M = \hbar c^3/8\pi Gk_BT = (1.0546\times10^{-34})(2.998\times10^8)^3/[8\pi(6.674\times10^{-11})(1.3806\times10^{-23})(2.7255)]$.
2. The numerator is $2.842\times10^{-9}$ and the denominator $6.31\times10^{-32}$ in SI units, so $M = 4.50\times10^{22}$ kg.
3. $M/M_{\rm Moon} = 4.50\times10^{22}/7.342\times10^{22} = 0.613$.
4. $r_s = 2GM/c^2 = 2(6.674\times10^{-11})(4.50\times10^{22})/(2.998\times10^8)^2 = 6.69\times10^{-5}$ m.

**Targets:** `every-black-hole-is-shrinking`

### `charged-hole-temperature` · working · difficulty 3 · calculation

A static observer in the metric $ds^2 = -f(r)\,c^2dt^2 + dr^2/f(r) + r^2d\Omega^2$ has lapse $N = \sqrt f$ and proper acceleration $a = c^2f'/(2\sqrt f)$. (a) Repeat the hovering-thermometer argument at a horizon $f(r_+) = 0$ to find $k_BT_H$. (b) For a Reissner–Nordström hole, $f = 1 - 2GM/rc^2 + GQ^2/4\pi\varepsilon_0c^4r^2$, write $T_H$ using the horizon radii $r_\pm$, and find its ratio to the uncharged value when $q \equiv \sqrt{GQ^2/4\pi\varepsilon_0c^4} = 0.8\,GM/c^2$. (c) What happens when $q = GM/c^2$?

**Hints**

1. The product $Na$ equals $c^2f'/2$ at every radius.
2. Write $f = (r - r_+)(r - r_-)/r^2$ with $r_\pm = m \pm \sqrt{m^2 - q^2}$ and $m = GM/c^2$.

**Answer:** (a) $k_BT_H = \hbar cf'(r_+)/4\pi$, so $\kappa = c^2f'(r_+)/2$. (b) $k_BT_H = \hbar c(r_+ - r_-)/4\pi r_+^2$; for $q = 0.8m$ the ratio is $15/16 = 0.9375$. (c) $r_+ = r_-$, so $T_H = 0$: an extremal hole emits no thermal radiation.

**Must contain:** N times a equals c squared f prime over two; T H equals h bar c times r plus minus r minus over four pi k B r plus squared; Ratio 0.9375 at q equal to 0.8 m; The extremal hole has zero temperature

**Numeric:** ratio to the uncharged temperature = 0.9375 1 (magnitude, ±1%); ratio at extremality = 0 1 (magnitude, ±0.001)

**Solution**

1. $Na = \sqrt f\cdot c^2f'/2\sqrt f = c^2f'/2$, so $k_BT_\infty = \hbar Na/2\pi c = \hbar cf'/4\pi$. The near-horizon limit gives $k_BT_H = \hbar cf'(r_+)/4\pi$.
2. Check: for Schwarzschild $f' = r_s/r^2$, so $f'(r_s) = 1/r_s$ and $k_BT_H = \hbar c/4\pi r_s = \hbar c^3/8\pi GM$.
3. For Reissner–Nordström, $(r - r_+)(r - r_-)/r^2 = 1 - 2m/r + q^2/r^2$ when $r_+ + r_- = 2m$ and $r_+r_- = q^2$, so $f'(r_+) = (r_+ - r_-)/r_+^2$ and $k_BT_H = \hbar c(r_+ - r_-)/4\pi r_+^2$.
4. For $q = 0.8m$: $\sqrt{m^2 - q^2} = 0.6m$, $r_+ = 1.6m$, $r_- = 0.4m$. The ratio to $\hbar c/4\pi(2m)$ is $2m(1.2m)/(1.6m)^2 = 0.9375$.
5. For $q = m$ the radii coincide, $f'(r_+) = 0$, and $T_H = 0$.

### `partners-make-it-thermal` · formal · difficulty 2 · proof

For one late out-packet of frequency $\omega$ and its partner behind the horizon, take $|\psi\rangle = \sqrt{1-x}\sum_{n\ge0}x^{n/2}|n\rangle_{\rm out}|n\rangle_{\rm p}$ with $x = e^{-2\pi\omega/\kappa}$, greybody factor one and $\hbar = k_B = 1$. Show that $|\psi\rangle$ is normalized, find the reduced density matrix of the out-packet, its mean occupation and its von Neumann entropy, and give the entropy of the pair.

**Hints**

1. Sum a geometric series.
2. Tracing over the partner keeps only terms with equal partner occupation.

**Answer:** $\rho_{\rm out} = (1-x)\sum_n x^n|n\rangle\langle n|$, with $\langle n\rangle = 1/(e^{2\pi\omega/\kappa} - 1)$ and $S = -\ln(1-x) - x\ln x/(1-x)$, the entropy of a thermal mode at $T = \kappa/2\pi$. The pair is in a pure state, with entropy zero.

**Must contain:** The norm is a geometric series equal to one; The reduced state is thermal at kappa over two pi; The mean occupation is the Planck factor; The pair has zero entropy, so thermal does not mean mixed globally

**Solution**

1. $\langle\psi|\psi\rangle = (1-x)\sum_n x^n = (1-x)/(1-x) = 1$, since $0 < x < 1$.
2. $\mathrm{Tr}_{\rm p}|\psi\rangle\langle\psi| = (1-x)\sum_{n,n'}x^{(n+n')/2}|n\rangle\langle n'|\,\langle n'|n\rangle_{\rm p} = (1-x)\sum_n x^n|n\rangle\langle n|$.
3. With $x = e^{-\omega/T}$ and $T = \kappa/2\pi$, this is $e^{-\omega\hat n/T}/Z$: a thermal state.
4. $\langle n\rangle = (1-x)\sum_n nx^n = x/(1-x) = 1/(e^{2\pi\omega/\kappa} - 1)$.
5. $S = -\sum_n p_n\ln p_n$ with $\ln p_n = \ln(1-x) + n\ln x$, so $S = -\ln(1-x) - \langle n\rangle\ln x = -\ln(1-x) - x\ln x/(1-x)$.
6. The pair state is a single vector, so its entropy is zero; the out-packet's entropy is entanglement entropy.

**Targets:** `thermal-means-information-lost`

## Observations

- **The temperature of the cosmic microwave background, measured by satellite and balloon-borne spectrometers** (measured, working). A black hole both absorbs the background and emits Hawking radiation, and it loses mass only if $T_H$ exceeds the background temperature. With $k_BT_H = \hbar c^3/8\pi GM$ that requires $M < 4.5\times10^{22}$ kg. Every black hole detected so far is heavier than the Sun, so each one gains more energy than it radiates, even before counting infalling gas. *Numbers:* $T = 2.72548 \pm 0.00057$ K; a solar-mass hole has $T_H = 6.17\times10^{-8}$ K, about $4.4\times10^7$ times colder. *Reference:* D. J. Fixsen (2009), *The Temperature of the Cosmic Microwave Background*, The Astrophysical Journal 707, 916–920, doi:10.1088/0004-637X/707/2/916
- **Searches for Hawking radiation from primordial black holes** (proposed, working). Black holes formed in the early universe with initial mass near $5\times10^{11}$ kg would be finishing their evaporation now, emitting quanta of tens of MeV and more. No such emission has been identified. Measured gamma-ray backgrounds instead limit how much of the universe such holes could make up. *Numbers:* Holes of initial mass about $5\times10^{11}$ kg have lifetimes close to the present age of the universe; at that mass $T_H = 2.5\times10^{11}$ K and $k_BT_H = 21$ MeV. *Reference:* B. J. Carr, Kazunori Kohri, Yuuiti Sendouda, Jun'ichi Yokoyama (2010), *New cosmological constraints on primordial black holes*, Physical Review D 81, 104019, doi:10.1103/PhysRevD.81.104019
- **Spontaneous Hawking radiation from an acoustic horizon in a flowing Bose–Einstein condensate of rubidium atoms** (analogue, research). A condensate flowing faster than its sound speed forms an acoustic horizon. Density correlations across it revealed phonon pairs, and measurements found their spectrum consistent with thermal at the temperature predicted from the flow's surface gravity. This tests the mode-mixing kinematics, not gravity. *Reference:* Juan Ramón Muñoz de Nova, Katrine Golubkov, Victor I. Kolobov, Jeff Steinhauer (2019), *Observation of thermal Hawking radiation and its temperature in an analogue black hole*, Nature 569, 688–691, doi:10.1038/s41586-019-1241-0

## Teaching arc

1. **Ask whether a black hole can give anything off** (entry). Pose the lone black hole in an empty universe, collect a prediction, then tell the glow story. *Why:* Learners expect a perfect trap, so the prediction makes the glow a surprise worth explaining. *Predict:* A black hole with the mass of the Sun sits alone in a dark, empty universe. Will it give off anything at all? *Visual:* [[vacuum-pairs-near-a-horizon]] *Uses:* `ways_in/a-black-hole-that-glows`, `checks/glow-in-empty-space`
2. **Tie the temperature to the mass** (entry). Scale the temperature from the Sun-mass hole to heavier and lighter holes. *Why:* Learners expect heavier to mean hotter, so this rule surprises most of them. *Predict:* Will a hole ten times heavier glow hotter or colder? *Visual:* [[thermometer-beside-a-black-hole]] *Uses:* `ways_in/mass-and-temperature`, `checks/ten-suns-hole`, `problems/moon-mass-black-hole`
3. **Put the hole in the real sky** (entry). Compare the hole's glow with the leftover glow from the early universe and decide whether real holes shrink. *Why:* It explains why the effect is unobserved and blocks the belief that all holes are evaporating. *Predict:* Is a real black hole in today's universe shrinking or growing? *Uses:* `ways_in/colder-than-the-sky`, `checks/real-hole-in-todays-sky`
4. **Build the temperature from acceleration and redshift** (working). Derive the temperature from a thermometer hovering at the horizon, then contrast hovering and falling detectors. *Why:* It turns the formula into two effects the learner already trusts and removes the hot-layer picture. *Uses:* `ways_in/temperature-from-a-hovering-thermometer`, `derivations/temperature-from-a-hovering-thermometer`, `checks/hovering-and-falling-detectors`
5. **Say who records what** (working). Write the grey-body rate, then settle the sign of the partner's energy. *Why:* Operational statements prevent both the perfect-black-body and the negative-local-energy errors. *Visual:* [[thermometer-beside-a-black-hole]] *Uses:* `ways_in/what-a-distant-detector-records`, `checks/energy-of-the-partner`
6. **Derive the Planck factor** (formal). Trace a late out-mode back through the exponential redshift and compute the Bogoliubov ratio, then trace out the partner. *Why:* It shows where thermality comes from and why a thermal flux does not by itself mean lost information. *Visual:* [[rays-peeling-off-a-forming-horizon]] *Uses:* `ways_in/mode-mixing-across-the-horizon`, `derivations/planck-factor-from-exponential-redshift`, `problems/partners-make-it-thermal`, `checks/thermal-but-pure`
7. **Test the kinematics in a fluid** (research). Map the calculation onto a sonic horizon and separate what analogue experiments test from what they cannot. *Why:* It connects the trans-Planckian worry to real measurements. *Uses:* `ways_in/horizons-in-flowing-fluids`, `checks/what-analogues-can-test`

## Analogies

### Twin beams from a pumped crystal · formal

In spontaneous parametric down-conversion, a laser pumping a nonlinear crystal turns pump photons into pairs, one in a signal beam and one in an idler beam. With no input light the beams leave in the two-mode squeezed state $\propto \sum_n \tanh^n r\,|n\rangle_s|n\rangle_i$. Either beam measured alone shows thermal photon statistics, $\langle n\rangle = \sinh^2 r$, although the joint state is pure.

| In the analogy | Stands for |
| --- | --- |
| the signal beam | the late Hawking out-packets |
| the idler beam | the partner packets behind the horizon |
| $\tanh^2 r$ | $e^{-2\pi\omega/\kappa}$ |

*Limits:* The idler can be measured and the correlations checked, while the partners are unreachable from outside. The squeezing is set by pump and crystal, not by one temperature for every frequency. Depletion of the pump is well understood, while back-reaction on a black hole is not.

## Misconceptions

### “Nothing can ever come out of a black hole, so it cannot give off anything.” · entry · `black-holes-cannot-emit`

- **Why it is tempting:** A black hole is described as a place that even light cannot escape.
- **What is true:** Nothing comes back out through the horizon, but quantum effects in the space around the hole make a faint glow there. Its energy comes out of the hole's mass.
- **Exposed by:** `checks/glow-in-empty-space`

### “A bigger black hole must glow hotter, like a bigger fire.” · entry · `heavier-means-hotter`

- **Why it is tempting:** Bigger stars and bigger fires usually give off more heat.
- **What is true:** For holes without spin or charge, the temperature goes down by the same factor that the mass goes up. A hole twice as heavy is twice as wide, with glow waves twice as long, so it glows at half the temperature.
- **Exposed by:** `checks/ten-suns-hole`

### “Hawking radiation is light that was trapped behind the horizon and finally leaks out.” · entry · `glow-escapes-from-behind-the-horizon`

- **Why it is tempting:** The glow seems to come from the black hole, and the hole is what lies behind the horizon.
- **What is true:** Nothing crosses the horizon outward, even with quantum physics. The glow is made in the space outside the horizon while partner particles fall in.
- **Exposed by:** `checks/light-from-behind-the-horizon`

### “Every black hole out there is slowly shrinking because of Hawking radiation.” · entry · `every-black-hole-is-shrinking`

- **Why it is tempting:** Evaporation is usually described for a hole alone in empty space.
- **What is true:** Every known black hole glows far more coldly than the leftover glow from the early universe. So each one takes in more than it gives off and grows.
- **Exposed by:** `checks/real-hole-in-todays-sky`

### “There is a hot, glowing layer at the horizon that would burn anyone who falls in.” · working · `hot-layer-at-the-horizon`

- **Why it is tempting:** The temperature a hovering detector registers grows without bound near the horizon, and the pair cartoon puts the action there.
- **What is true:** The high temperature belongs to detectors that hover and so accelerate hard. A freely falling detector finds only a feeble, finite energy density at the horizon of a large hole.
- **Exposed by:** `checks/hovering-and-falling-detectors`

### “The partner that falls in is a particle with negative energy, as anyone next to it would measure.” · working · `partner-has-negative-local-energy`

- **Why it is tempting:** The hole loses mass, so whatever falls in seems to need negative energy.
- **What is true:** Only the conserved energy built from the time-translation symmetry is negative, allowed where that symmetry's vector is spacelike: behind the horizon, and also just outside a spinning hole. Any local observer measures positive energy for each quantum.
- **Exposed by:** `checks/energy-of-the-partner`

### “The virtual-pair argument with the uncertainty principle derives the thermal spectrum of Hawking radiation.” · formal · `pair-picture-derives-the-spectrum`

- **Why it is tempting:** It produces the right energy scale in a few lines.
- **What is true:** It fixes only the scale. The Planck spectrum comes from mode mixing at the exponentially redshifting horizon.
- **Exposed by:** `checks/what-the-pair-picture-derives`

### “Because the radiation is exactly thermal, Hawking's calculation proves that information is destroyed.” · formal · `thermal-means-information-lost`

- **Why it is tempting:** Thermal states are mixed, and mixed states look like lost information.
- **What is true:** The global state stays pure, and the radiation is thermal because it is entangled with partners behind the horizon. Whether information is lost depends on the end of evaporation, which the calculation does not describe.
- **Exposed by:** `checks/thermal-but-pure`

## Checks

1. **Entry · predict** `checks/glow-in-empty-space`. Imagine a black hole with the Sun's mass, alone in a perfectly dark and empty universe, with nothing falling in. Does quantum physics predict that it gives off anything? If so, what happens to the hole over a very long time?
   - **Hints:** What do pairs of particles do in the space around a hole?
   - **Answer:** Yes. Near the horizon, one member of a pair of particles can cross the horizon before the pair vanishes, and the other can escape. The escaping particles form a faint glow, Hawking radiation, which carries energy away. Counted from far away, the partner that fell in brings in negative energy. Energy has mass, so the hole gets lighter and slowly shrinks.
   - **Must contain:** Yes, it gives off a faint glow; The glow carries energy away; The hole slowly gets lighter and shrinks
   - **Targets:** `black-holes-cannot-emit`
   - **Visual:** [[vacuum-pairs-near-a-horizon]]
2. **Entry · numeric** `checks/ten-suns-hole`. Measured from far away, a black hole with the Sun's mass glows at about 60 billionths of a degree above absolute zero. A second black hole has ten times the Sun's mass. Neither hole spins or has electric charge. How warm is the second hole's glow, measured from far away?
   - **Hints:** Does a heavier hole glow hotter or colder?
   - **Answer:** About 6 billionths of a degree above absolute zero. A hole ten times as heavy is ten times as wide, so its glow's waves are ten times as long, and its temperature is a tenth as much. A tenth of 60 billionths is 6 billionths.
   - **Must contain:** Heavier means colder; Ten times the mass gives a tenth of the temperature; About 6 billionths of a degree
   - **Numeric:** temperature of the glow = 6.17e-09 K (magnitude, ±10%)
   - **Targets:** `heavier-means-hotter`
   - **Visual:** [[thermometer-beside-a-black-hole]]
3. **Entry · evaluate-claim** `checks/light-from-behind-the-horizon`. A friend says: "Hawking radiation is light that was trapped behind a black hole's horizon and finally leaks out." Is your friend right? Explain.
   - **Hints:** Where do the pairs of particles appear?
   - **Answer:** No. Nothing that crosses the horizon ever comes back out, and quantum physics does not change that. The glow is made in the space around the hole, outside the horizon. There, one member of a pair of particles crosses the horizon, and the other escapes. So the glow never was behind the horizon.
   - **Must contain:** No; Nothing comes back out through the horizon; The glow is made outside the horizon while partners fall in
   - **Targets:** `glow-escapes-from-behind-the-horizon`
4. **Entry · predict** `checks/real-hole-in-todays-sky`. A black hole with ten times the Sun's mass sits in today's universe, far from any star or gas. The hole does not spin or have electric charge. The leftover glow from the early universe reaches it from every direction at about 2.7 degrees above absolute zero. Is the hole shrinking because of its Hawking radiation, or growing?
   - **Hints:** Which is warmer, the hole's glow or the leftover glow?
   - **Answer:** Growing. A hole ten times heavier than the Sun glows at a tenth of 60 billionths of a degree, about 6 billionths. The leftover glow is hundreds of millions of times warmer. An object takes in more glow from warmer surroundings than it gives off. So the hole gains energy, and energy has mass, so it grows.
   - **Must contain:** Growing; The hole glows far more coldly than the sky; It takes in more glow than it gives off
   - **Targets:** `every-black-hole-is-shrinking`
   - **Visual:** [[thermometer-beside-a-black-hole]]
5. **Working · numeric** `checks/sagittarius-a-star-temperature`. The black hole at the centre of our galaxy has a mass of about $4.30\times10^6$ solar masses. Treating it as non-rotating, find its Hawking temperature, and the factor by which the cosmic microwave background, at $2.7255$ K, is warmer.
   - **Hints:** Start from the solar-mass value and use the one-over-mass scaling.
   - **Answer:** $T_H = \hbar c^3/8\pi GMk_B$ scales as $1/M$, and one solar mass gives $6.17\times10^{-8}$ K. So $T_H = 6.17\times10^{-8}\ \mathrm{K}/4.30\times10^6 = 1.43\times10^{-14}$ K. The background is $2.7255/1.43\times10^{-14} = 1.9\times10^{14}$ times warmer.
   - **Must contain:** Temperature scales as one over mass; About 1.4 times ten to the minus fourteen kelvin; The background is about two times ten to the fourteen times warmer
   - **Numeric:** Hawking temperature = 1.435e-14 K (magnitude, ±2%); ratio of background to Hawking temperature = 1.9e+14 1 (magnitude, ±3%)
6. **Working · explain** `checks/hovering-and-falling-detectors`. Near a solar-mass black hole, one detector is held at rest where the lapse $N = \sqrt{1 - r_s/r}$ equals $0.01$, and another falls freely across the horizon. Far away, $T_H = 6.17\times10^{-8}$ K. What temperature does the hovering detector assign to the radiation coming up from the horizon? Does the falling detector meet a hot layer at the horizon?
   - **Hints:** How does climbing out change each frequency? / Which of the two detectors is accelerating?
   - **Answer:** The hovering detector assigns about $T_H/N = 6.17\times10^{-6}$ K. Climbing out multiplies frequencies by $N$ without changing occupation numbers, so radiation that arrives far away at $T_H$ was thermal at $T_H/N$ where the detector hovers. Equivalently, its proper acceleration $a = GM/(r^2N) = 1.52\times10^{15}\ \mathrm{m/s^2}$ gives the Unruh temperature $\hbar a/2\pi ck_B = 6.17\times10^{-6}$ K. The falling detector does not accelerate: on scales much smaller than $r_s$ the state looks like vacuum to it, and the energy density it measures stays finite, on the scale $\hbar c/r_s^4$. There is no hot layer.
   - **Must contain:** About a hundred times the Hawking temperature, 6.2 millionths of a kelvin; The hovering detector accelerates hard, so it registers the Unruh temperature; The falling detector finds nothing special at the horizon
   - **Numeric:** temperature at the hovering detector = 6.17e-06 K (magnitude, ±2%)
   - **Targets:** `hot-layer-at-the-horizon`
7. **Working · explain** `checks/energy-of-the-partner`. At a non-rotating black hole, the partner of each escaping Hawking quantum lowers the mass of the hole, so it seems to carry negative energy. Does an astronaut falling alongside the partner, just behind the horizon, measure a negative energy for it?
   - **Hints:** Which vector turns spacelike behind the horizon?
   - **Answer:** No. The negative quantity is the conserved energy $E = -p_\mu\xi^\mu$ built from the time-translation Killing vector $\xi$, the energy counted far away. Outside the horizon $\xi$ is timelike, so $E > 0$ for every quantum there. Behind the horizon $\xi$ is spacelike, so $E$ is a momentum component and can take either sign. The astronaut measures $-p_\mu u^\mu$ with her own four-velocity $u$, which is positive for every future-directed quantum. Separately, the expected energy density of the field near the horizon can be negative in this quantum state; that averaged effect, not a negative-energy particle, lets the horizon shrink.
   - **Must contain:** No, every local observer measures positive energy; The negative quantity is the Killing energy; Behind the horizon the Killing vector is spacelike, so that energy can be negative
   - **Targets:** `partner-has-negative-local-energy`
8. **Formal · evaluate-claim** `checks/thermal-but-pure`. Evaluate: "Hawking's calculation produces an exactly thermal, mixed state of radiation at future null infinity, so it proves that forming a black hole breaks unitarity."
   - **Hints:** What is left over when you trace out half of a pure two-mode state?
   - **Answer:** Mistaken as stated. The in-vacuum evolves unitarily on the fixed background and stays pure. The radiation at $\mathscr I^+$ is a subsystem, thermal because each out-packet is entangled with a partner behind the horizon: tracing out the partner of a two-mode squeezed state leaves $\rho = (1-x)\sum_n x^n|n\rangle\langle n|$ with $x = e^{-2\pi\omega/\kappa}$. A mixed subsystem is not non-unitarity. The puzzle is complete evaporation: with the partners gone, a pure initial state would end as mixed radiation. Earlier still, the entanglement entropy of the radiation in this calculation outgrows the Bekenstein–Hawking entropy of the shrinking hole. Whether correlations restore purity is the information problem, beyond a fixed-background calculation.
   - **Must contain:** The global state on the fixed background stays pure; The radiation is thermal because it is entangled with partners; The real puzzle is complete evaporation, beyond the calculation
   - **Targets:** `thermal-means-information-lost`
9. **Formal · evaluate-claim** `checks/what-the-pair-picture-derives`. Evaluate: "The uncertainty-principle argument, in which a virtual pair straddles the horizon, derives the thermal spectrum of Hawking radiation at $\kappa/2\pi$."
   - **Hints:** Does the pair argument say how many quanta come out at each frequency?
   - **Answer:** Mistaken. That argument estimates the energy scale of escaping quanta, of order $1/M$ with $G = c = \hbar = 1$, and gives no spectrum; its numerical factor is not the thermal one. The Planck factor comes from mode mixing: late out-modes, traced back through $v_0 - v = Ce^{-\kappa u}$, contain negative frequencies in $v$ with $|\beta_{\omega\omega'}| = e^{-\pi\omega/\kappa}|\alpha_{\omega\omega'}|$. That calculation also states what the cartoon hides: it needs a state regular across the horizon, late times and a non-extremal hole, and not the details of the collapse.
   - **Must contain:** The pair argument gives only the energy scale; The Planck factor comes from the Bogoliubov ratio; The derivation states its hypotheses and is independent of the collapse details
   - **Targets:** `pair-picture-derives-the-spectrum`
   - **Visual:** [[rays-peeling-off-a-forming-horizon]]
10. **Research · explain** `checks/what-analogues-can-test`. An experiment finds thermal, entangled phonon pairs emitted from an acoustic horizon in a Bose–Einstein condensate. Which parts of the Hawking prediction does it test, and which does it not?
   - **Hints:** Which equations govern the acoustic metric?
   - **Answer:** It tests the kinematics: that a wave field on a stationary effective geometry with a horizon turns vacuum fluctuations into entangled pairs with a thermal spectrum at $\hbar\kappa/2\pi k_B$, set by the flow's surface gravity, and that this survives a dispersion relation that changes at short wavelengths, which bears on the trans-Planckian question. It does not test gravity. The acoustic metric does not obey Einstein's equations, so back-reaction of the radiation on spacetime, the late stages of evaporation and the fate of information lie outside its reach.
   - **Must contain:** Tests mode mixing and thermality on an effective geometry; Tests robustness against short-wavelength dispersion; Does not test back-reaction, the end of evaporation or information

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Which constants are hidden in the Hawking temperature | Entry and working rungs keep every constant: $k_BT_H = \hbar c^3/8\pi GM = \hbar\kappa/2\pi c$ with $\kappa$ an acceleration. Formal and research rungs set $G = c = \hbar = k_B = 1$ and say so: $T_H = \kappa/2\pi = 1/8\pi M$. | Some texts keep $\hbar$ and $k_B$ but set $G = c = 1$, writing $k_BT = \hbar/8\pi M$; others quote $\kappa$ as an inverse length or an inverse time. Check which constants are hidden before comparing numbers. |
| Which Bogoliubov coefficient counts created quanta | Positive frequency is $e^{-i\omega t}$, and $p_\omega = \int d\omega'(\alpha_{\omega\omega'}f_{\omega'} + \beta_{\omega\omega'}\bar f_{\omega'})$, so $\langle N_\omega\rangle = \int d\omega'\|\beta_{\omega\omega'}\|^2$. | Some texts expand in-modes in out-modes instead, or conjugate the coefficients, or take $e^{+i\omega t}$ as positive frequency. The count is always the squared modulus of the coefficient that mixes positive with negative frequency. |

## Visuals

- ★ [[thermometer-beside-a-black-hole]] (flagship): Makes the inverse law between mass and temperature, and the comparison with the sky, concrete. *Sketch:* A black hole drawn to scale beside a thermometer and a spectrum strip. A mass dial runs from an asteroid to a galaxy centre; readouts give the width, the temperature measured far away, the peak wavelength, and the sky at 2.7 K, with a grow-or-shrink arrow that flips below 0.61 Moon masses. Spin and charge toggles lower the temperature, reaching zero at the extremal limit.
- [[vacuum-pairs-near-a-horizon]] (supporting): The entry cartoon of pairs split near a horizon, labelled as a cartoon. *Sketch:* A spacetime diagram with light cones tipping toward a horizon. Short-lived pair loops appear everywhere; far away they close, near the horizon one member crosses and the other climbs out, stretching as it goes. A readout compares the escaping wave's length with the width of the hole.
- [[rays-peeling-off-a-forming-horizon]] (core): Shows the exponential redshift that makes the late flux thermal. *Sketch:* A collapsing star with outgoing rays launched at equal steps of advanced time just before the last ray that forms the horizon; their arrival times far away spread by $1/\kappa$ for each factor $e$ closer to $v_0$. A second panel Fourier-analyses a traced-back out-mode in advanced time and shows the ratio of negative to positive frequency content approaching $e^{-\pi\omega/\kappa}$, and the occupation number approaching the Planck curve.

## Tutor moves

**Open with**

- Picture a black hole with the mass of the Sun, alone in a perfectly dark, empty universe, with nothing falling in. Do you think it gives off anything at all over a very long time? *(prediction)*
- Suppose black holes that do not spin glow faintly. Would you expect a heavier black hole to glow hotter or colder than a lighter one? *(prediction)*

**If the learner is stuck**

- *The learner is lost in billionths and millions.* → Work in factors of ten: ten times heavier is ten times colder, then compare with the leftover glow at 2.7 degrees. *Uses:* `checks/ten-suns-hole`, `ways_in/colder-than-the-sky`
- *The learner cannot see how giving off a glow lowers the mass of the hole.* → Restate that energy has mass, then follow one quantum: the energy it carries far away is the mass the hole loses. *Uses:* `ways_in/a-black-hole-that-glows`
- *The learner is lost in the Bogoliubov integrals.* → Start from the partner problem, where the thermal factor is a geometric series, then return to the Fourier integral and its two convergence directions. *Uses:* `problems/partners-make-it-thermal`, `derivations/planck-factor-from-exponential-redshift`
- *The learner pictures a burning layer at the horizon.* → Contrast the hovering and the falling detector, and ask which one accelerates. *Uses:* `checks/hovering-and-falling-detectors`

**Common questions**

- *Has anyone ever detected Hawking radiation?* (entry) Not from a real black hole: every one found so far glows far more coldly than the leftover glow from the early universe. Laboratories have seen a look-alike effect, for ripples on flowing water and sound in flowing clouds of ultracold atoms. Where the flow outruns the waves, they cannot get back upstream, as light cannot leave a black hole. This tests the idea, but not gravity itself. *Uses:* `ways_in/colder-than-the-sky`, `observations/analogue-hawking-radiation-in-a-condensate`
- *What happens when a black hole alone in empty space has shrunk to almost nothing?* (entry) As it shrinks it gets hotter, and a hotter glow is brighter, so it shrinks faster and faster. Near the end, the usual calculation predicts a bright burst of energetic particles. The very last instant needs a theory that joins gravity and quantum physics, and nobody has finished one yet. *Uses:* `observations/primordial-black-hole-gamma-rays`, `research_horizon/information-and-the-page-curve`
- *Why does the temperature not depend on what the star was made of or how it collapsed?* (working) Late quanta come from where outgoing rays peel away from the horizon exponentially, at a rate set only by the surface gravity. The details of the collapse affect only early transients, which fade within a few multiples of $c/\kappa = 4GM/c^3$, 20 microseconds for a solar mass. *Uses:* `ways_in/mode-mixing-across-the-horizon`
- *Is Hawking radiation the same thing as the Penrose process?* (working) No. The Penrose process is classical, needs a spinning hole, and uses negative-energy orbits outside the horizon, in the ergoregion. Hawking emission is a quantum effect of the field, occurs for non-spinning holes, and carries negative Killing energy across the horizon. *Uses:* `checks/energy-of-the-partner`

**Switching levels**

- To working when: asks where the number comes from; uses acceleration or redshift formulas. Build the temperature from the Unruh temperature of a hovering thermometer and redshift. *Uses:* `ways_in/temperature-from-a-hovering-thermometer`, `derivations/temperature-from-a-hovering-thermometer`
- To formal when: asks why the spectrum is thermal; knows mode expansions of quantum fields. Derive the Planck factor from exponential redshift, then trace out the partners. *Uses:* `ways_in/mode-mixing-across-the-horizon`, `derivations/planck-factor-from-exponential-redshift`
- To research when: asks about the information problem, analogue experiments or Planck-scale physics. Open the fluid analogue and the research horizon. *Uses:* `ways_in/horizons-in-flowing-fluids`, `research_horizon/information-and-the-page-curve`

**Pronunciations:** Hawking → HAW-king; Unruh → UN-roo; Bogoliubov → bo-go-LYOO-bof; Bekenstein → BEK-en-stine; Reissner–Nordström → RYSE-ner NORD-strurm; Kruskal → KRUSS-kal

**Voice notes:** At entry, say billionths of a degree above absolute zero, never kelvin or powers of ten. After naming the cosmic microwave background once, call it the leftover glow.

## History

- **Leonard Parker (1969).** Showed that a time-dependent gravitational field, an expanding universe, creates particles from the vacuum, the mechanism later found at forming horizons. Leonard Parker (1969), *Quantized fields and particle creation in expanding universes. I*, Physical Review 183, 1057–1068, doi:10.1103/PhysRev.183.1057
- **Jacob D. Bekenstein (1973).** Argued that a black hole carries entropy proportional to its horizon area, suggesting that it should also have a temperature. Jacob D. Bekenstein (1973), *Black holes and entropy*, Physical Review D 7, 2333–2346, doi:10.1103/PhysRevD.7.2333
- **Stephen W. Hawking (1974).** Showed that quantum fields on the spacetime of a collapsing star end up with a late-time thermal flux at $k_BT = \hbar\kappa/2\pi c$, fixing the constant in the entropy–area relation. Announced in 1974 and published in 1975. S. W. Hawking (1975), *Particle creation by black holes*, Communications in Mathematical Physics 43, 199–220, doi:10.1007/BF02345020
- **William G. Unruh (1976).** Reformulated the emission with a quantum state regular on the future horizon and showed that a uniformly accelerated detector in flat spacetime responds as if in a thermal bath. W. G. Unruh (1976), *Notes on black-hole evaporation*, Physical Review D 14, 870–892, doi:10.1103/PhysRevD.14.870
- **William G. Unruh (1981).** Showed that sound in a fluid flowing faster than sound obeys the same wave equation near an acoustic horizon, proposing a laboratory analogue. W. G. Unruh (1981), *Experimental black-hole evaporation?*, Physical Review Letters 46, 1351–1353, doi:10.1103/PhysRevLett.46.1351

## Research horizon

- **Information and the Page curve.** If evaporation is unitary, the fine-grained entropy of the radiation must rise and then return to zero, turning over near the Page time, when the hole has lost about half its initial Bekenstein–Hawking entropy. Hawking's calculation gives only the rising branch. Since 2019, gravitational path-integral calculations with quantum extremal surfaces and islands reproduce the turnover in several models, while the mechanism in a real evaporating hole is still debated. Don N. Page (1993), *Information in black hole radiation*, Physical Review Letters 71, 3743–3746, doi:10.1103/PhysRevLett.71.3743; Ahmed Almheiri, Thomas Hartman, Juan Maldacena, Edgar Shaghoulian, Amirhossein Tajdini (2021), *The entropy of Hawking radiation*, Reviews of Modern Physics 93, 035002, doi:10.1103/RevModPhys.93.035002
- **The trans-Planckian problem.** Late Hawking quanta trace back to exponentially high frequencies near the horizon. Models with modified dispersion relations, motivated by condensed matter, find the late thermal flux insensitive to how the dispersion changes at short distances, provided the short-distance frequency scale lies far above the surface gravity $\kappa$. Ted Jacobson (1991), *Black-hole evaporation and ultrashort distances*, Physical Review D 44, 1731–1739, doi:10.1103/PhysRevD.44.1731; R. Brout, S. Massar, R. Parentani, Ph. Spindel (1995), *A primer for black hole quantum physics*, Physics Reports 260, 329–446, doi:10.1016/0370-1573(95)00008-5
- **Analogue gravity.** Sound, surface waves and light in moving media have effective metrics with horizons and surface gravities. Laboratory versions test the kinematics of Hawking emission, including dispersion and entanglement between the quanta and their partners. Carlos Barceló, Stefano Liberati, Matt Visser (2011), *Analogue Gravity*, Living Reviews in Relativity 14, 3, doi:10.12942/lrr-2011-3; Jeff Steinhauer (2016), *Observation of quantum Hawking radiation and its entanglement in an analogue black hole*, Nature Physics 12, 959–965, doi:10.1038/nphys3863
- **Evaporating primordial black holes.** Holes lighter than about $5\times10^{11}$ kg at formation would have evaporated by now. Gamma-ray backgrounds, the cosmic microwave background and light-element abundances limit how many formed, which constrains early-universe models and the idea that primordial holes are the dark matter. Bernard Carr, Florian Kühnel (2020), *Primordial Black Holes as Dark Matter: Recent Developments*, Annual Review of Nuclear and Particle Science 70, 355–394, doi:10.1146/annurev-nucl-050520-125911

## Review: novice

**Verdict:** fixed (2026-09-13, revision 7)

**Retell attempt:** Hot things give off light you can't see, like a mug of tea. A black hole traps everything, even light, so it should be black. But Hawking found that quantum physics makes it glow anyway: little pairs of particles keep popping up near it, one falls in and the other gets away, and the ones that get away are the glow. Somehow the glow takes energy out of the hole, so it gets lighter, though I don't get that, since half of each pair fell in. Weirdly, bigger black holes are colder, and I don't know why. One with the Sun's mass is 6 kilometres wide and glows at 60 billionths of a degree. I'm not sure how a thermometer far away would read that. Then it says the pair thing is only a cartoon because the waves are longer than the hole, so I don't know what really happens. In space there is leftover glow from the early universe that is warmer, so real black holes soak it up and grow, which is maybe one reason nobody has seen the glow. Only one lighter than about half the Moon, a tenth of a millimetre wide, would shrink. (Compared with the takeaways: the three main claims came through, but there was no reason for heavier-is-colder, a gap in how the hole loses mass, and an impossible thermometer.)

**Stumbles (28)**

- “the energy it carries comes out of the hole's mass”: In the summary, 'it' could be the hole or the glow, and the reader cannot see how energy can come out of a mass.
- “far colder than the sky”: 'The sky' is warm on a sunny afternoon; the reference is never named.
- “it gives off light, mostly invisible”: 'Invisible light' sounds like a contradiction to someone who thinks light is what you see; the recap also gives no link between waves and temperature, which the new reason for heavier-is-colder needs.
- “A mug of hot tea looks dark, yet a palm held beside it feels warm.”: A mug does not look dark in a lit room, and the try-it uses hot water rather than tea, so there are two objects for one scene.
- “In 1974 Stephen Hawking found that quantum physics changes this, although nothing comes back out through the horizon.”: Reread twice: 'this' has several candidates, and 'although' makes it sound as if something should come out.
- “Sometimes one member of a pair falls in, and the other escapes.”: A step is implicit: why would a pair near a hole behave differently from a pair anywhere else, and why doesn't it vanish as pairs normally do?
- “The escaping particles form a faint glow.”: Particles and glow read as two different things; nothing says that light itself comes in particles.
- “Measured by a thermometer far from the hole, the glow has a temperature”: This is a rule the reader cannot follow. A thermometer far away sits in a very thinned-out glow and in the leftover glow of the early universe, so it would read neither temperature.
- “A hole twice as heavy glows at half the temperature.”: The most surprising claim of the entry rung comes with no reason.
- “The glow carries energy away, and energy has mass. So a hole alone in empty space gets lighter and slowly shrinks.”: First what-if: the partner fell in, so why doesn't the hole get heavier? Also 'empty space' contradicts 'Space is not perfectly cold' in the next way.
- “The pair picture is only a cartoon. Almost all of the glow comes in waves longer than the whole hole is wide, so it is not made at single spots on the horizon.”: 'Pair picture' was never named, 'it' is ambiguous, and there is no number for the waves.
- “You feel warmth, and much of it reaches you as the mug's invisible glow.”: A surprise with no test: warm air could explain the warmth just as well.
- “so the mix of colours differs from a perfect warm object's, although the temperature is exact”: 'Exact' has no meaning for this reader, and the sentence runs long.
- “soaks up more of the sky's glow ... the sky's leftover glow ... the cosmic microwave background ... the sky”: One idea has four names, and 'soaks up' duplicates 'takes in'.
- “A faint glow left over from the hot early universe arrives from every direction.”: A surprise with no reason: why was the universe hot, and why is the glow cold now?
- “So the hole soaks up more of the sky's glow than it gives off, and it grows instead of shrinking.”: A step is implicit: taking in glow means gaining energy, and so mass.
- “That is one reason nobody has detected Hawking radiation.”: It promises other reasons and never gives them.
- “It would be about a tenth of a millimetre across.”: A mass bigger than half the Moon squeezed into a tenth of a millimetre is hard to picture without an everyday comparison.
- “As the universe expands, the sky's glow cools, so in the very distant future even heavy holes will shrink.”: 'Will' is unconditional, but it depends on how the expansion continues.
- “The temperature falls in step with the mass”: 'In step' reads as moving the same way, the opposite of what is meant. It appears in the ten-suns answer, the misconception correction, and (as 'in step with how much lighter') the Moon problem's hint.
- “About how warm is the glow of a black hole with the Sun's mass ... Neither hole spins or has electric charge.”: In the Moon problem, 'Neither hole' comes before the second hole is named.
- “A hole ten times heavier glows ten times more coldly.”: 'Ten times more coldly' has no clear arithmetic meaning.
- “When one member of a pair falls in and the other escapes, the escaping particles form a faint glow ... so the hole gets lighter.”: The check answer leaves the same energy gap as the explanation.
- “Scientists have seen the matching effect for sound, in flowing water and in clouds of ultracold atoms, where sound gets trapped”: The water experiments used surface ripples, not sound; 'matching' is vague; and how waves get trapped is not said.
- “As it shrinks it gets hotter, so it shrinks faster and faster.”: A link is missing: why does hotter mean faster shrinking?
- “about 273 degrees below the freezing point of water”: Which degrees? A reader who uses Fahrenheit gets the wrong size.
- “partner”: The entry way now says 'the partner', but the glossary does not define it.
- “The inverse rule is the most counterintuitive number in the topic.”: This entry teaching-arc field is spoken, and 'inverse rule' is jargon.

**Fixes**

- Rewrote both entry explanations, cutting repetition to stay within the 400-word advanced cap: pairs split near the horizon, partner energy counted from far away, heavier-is-colder explained by width and wave length, and a number for the waves (tens of kilometres).
- Replaced 'measured by a thermometer far away' with 'measured from far away' in the entry way and both entry checks.
- Gave the cosmic microwave background one everyday name, 'the leftover glow', across the entry way, checks, problem, objective, misconception, arc, if-stuck move, common question and voice notes.
- Replaced the try-it with a foil-wrapped mug, which separates the invisible glow from warm air.
- Moved what the pair cartoon gets right into simplifies; split a 36-word sentence; scoped the far-future claim.
- Replaced 'in step with' wording for the inverse law in the check, misconception and problem hint; reordered the Moon problem.
- Corrected the common question about analogue experiments (ripples on water, sound in atom clouds) and explained how the flow traps waves.
- Glossary: Celsius-sized degrees for absolute zero, a 'leftover glow' form, and 'partner'.
- Ladder: the working way's first sentence now carries the entry reason (twice as heavy, twice as wide, waves twice as long) into dimensional analysis. The other non-entry ways already refer back by title, and the six ways use six different kinds.
- Trimmed two non-entry check answers of repeated wording to stay within the tutoring cap, with no change to the physics. Bumped revision to 2.

**Concerns**

- Budgets are at their caps: entry explanations are within a word or two of 400, and tutoring is just under 3500. Even this one reason and one number per claim barely fit the advanced entry cap. Consider whether the cap should give way to the novice contract.
- Physics reviewer: please confirm three new entry statements. (a) For a non-rotating, uncharged hole, the glow's wave lengths scale with the hole's width. (b) Most of the emitted energy of a Sun-mass hole comes in waves tens of kilometres long, counting greybody factors and species other than photons; the black-body peak per frequency is about 83 km, and the photon power peak about 46 km. (c) 'Counted from far away, the partner brings in negative energy', which must stay consistent with the working misconception about local energy.
- Physics reviewer: check the foil try-it. Glazed ceramic emits about 0.9 as well as an ideal glowing surface and shiny foil about 0.05, and a mug at 80 degrees Celsius radiates about 450 watts per square metre, so the difference should be easy to feel.
- The working check energy-of-the-partner uses the Killing vector and p-mu u-mu. Index notation is reachable through the prerequisites, but no working-rung prerequisite introduces Killing vectors.
- The prerequisite notes horizon-pair-creation-picture and black-body-spectrum do not exist yet, so the entry recaps (pairs appearing and vanishing, hotter meaning shorter waves, a warm object taking in glow from warmer surroundings) were not aligned with them.
- Still open from the writer: three conventions missing from course-conventions.md (surface-gravity normalization, Bogoliubov expansion and inner-product sign, the null-infinity symbol) and the registry sync for three added prerequisites.

**Re-read** (2026-09-13, revision 3): 6 stumbles in 17 changed passages

- “Near the horizon, one member of a pair of particles can cross the horizon before the pair vanishes. ... A hole twice as heavy is twice as wide, so its waves are twice as long, and it glows at half the temperature.”: Rule 17: 'A black hole that glows' asks the reader to hold two new ideas at once, how a hole can glow at all (pairs, partner energy, mass loss) and why a heavier hole glows colder (width, wave length, temperature), and its takeaway joins them with a semicolon.
- “so its waves are twice as long, and it glows at half the temperature”: Step taken on trust: the recap only says a hotter object has shorter waves, not that twice as long means exactly half the temperature.
- “Counted from far away, the partner that fell in brings in negative energy.”: Surprise with no reason, count or test within two sentences; 'negative energy' is new and cannot be explained at this rung, so the reader stops to wonder what it means.
- “Near the horizon, one member of a pair of particles can cross the horizon before the pair vanishes.”: Once the cartoon caveat moves to its own way, this sentence reads as the literal mechanism to a reader who never sees simplifies, and the later 'the pair picture is only a cartoon' names a picture that was never called that.
- “Every black hole found so far is heavier than the Sun, so its glow is even colder. That is why nobody has detected Hawking radiation from a real black hole.”: Step taken on trust: nothing says why a colder glow cannot be detected; the reader asks why a cold glow could not still be seen.
- “Shiny foil gives off very little glow, so much of the warmth you felt beside the bare half was the mug's invisible glow.”: One link is left to the reader: the conclusion needs the air beside both halves to be warmed about equally, so that the difference cannot be warm air.
- Fix: Split 'A black hole that glows' into two entry ways; new way mass-and-temperature (calculation) carries the temperature paragraph and the Sun-mass numbers paragraph unchanged except its first sentence, which now names Hawking radiation to refer back.
- Fix: 'A black hole that glows': takeaway reduced to the glow and its energy; simplifies keeps the cartoon and other-particles sentences; recap drops the hotter-shorter-waves sentence (moved, with twice as hot, half as long, to the new way's recap) and the energy-has-mass sentence, which the explanation already states.
- Fix: Added 'In the pair picture,' before the pair sentence and 'Take this on trust for now.' after the negative-energy sentence.
- Fix: 'Colder than the sky': added the link from a cold glow to not being detected. To stay within the 400-word entry cap, dropped two lowest-value sentences: 'Space is not perfectly cold.' (its claim is carried by the next three sentences) and 'It would be about a tenth of a millimetre across, a thick hair's width.' (a size picture no check or objective uses).
- Fix: continues: colder-than-the-sky now climbs from both entry ways; temperature-from-a-hovering-thermometer now continues mass-and-temperature, and its first sentence names that way instead of 'A black hole that glows'. Teaching arc mass-sets-temperature uses the new way.
- Fix: Bumped revision to 3.

**Re-read** (2026-09-13, revision 6): 5 stumbles in 9 changed passages

- “So much of the warmth you felt beside the bare half was the mug's invisible glow.”: Reread: 'So much of the warmth' first reads as an exclamation, 'so much warmth!', before it resolves into 'so, much of the warmth'.
- “Both halves warm the nearby air about equally, but shiny foil gives off very little glow.”: Step taken on trust: a reader who thinks foil keeps heat in expects the foil half to warm the air less, and nothing says why the two halves warm the air about equally.
- “Any heavier hole glows more coldly than that.”: Reread: 'that' could be the 60 billionths of a degree, absolute zero, or 'the coldest possible temperature', and 'more coldly than the coldest possible temperature' makes no sense. The sentence before it is also crowded, with the new spin clause set off by commas next to the absolute-zero comma.
- “It helps to picture the glow, but it is not the calculation that predicts the glow.”: One word in two senses: the entry is named 'pair picture', a noun, and the definition then uses 'picture' as a verb.
- “In 50 years, the hole gives off less energy than one packet of green light carries.”: Step taken on trust: the reader has only met 'light comes in tiny packets' and does not know that packet size depends on colour, so 'green' looks arbitrary and the reader stops to wonder whether it matters.
- Fix: a-black-hole-that-glows try_it: 'So much of the warmth' -> 'So a large part of the warmth' (same claim).
- Fix: colder-than-the-sky recap: 'mass, without spin or charge, glows' -> 'mass and no spin or charge glows'; 'more coldly than that.' -> 'more coldly than that hole.' (same scope and comparison).
- Fix: glossary pair-picture: 'It helps to picture the glow' -> 'It helps you imagine the glow'.
- Fix: Two stumbles not applied because they would add claims: the foil-and-air reason, and packet size by colour. Both are proposed in the stage summary.
- Fix: Budgets: other way fields 805 -> 809 of 800 (within the 880 allowance), objectives-to-glossary part unchanged at 3549 of 3500 (within 3850), entry explanations unchanged at 440. Bumped revision 5 -> 6; status kept at physics-reviewed.

**Re-read** (2026-09-13, revision 7): 0 stumbles in 3 changed passages


## Review: physics

**Verdict:** fixed (2026-09-13, revision 7)

**Verification**

- k_BT_H = hbar c^3/8 pi G M; one solar mass gives 6.17e-8 K, k_BT = 8.52e-31 J = 5.32e-12 eV; r_s = 2953 m; kappa = c^4/4GM = 1.52e13 m/s^2.: python with CODATA 2018 constants and GM_sun = 1.32712e20 m^3 s^-2. → 6.1703e-8 K, 8.519e-31 J, 5.317e-12 eV, 2953.25 m, 1.5216e13 m/s^2. Correct.
- Hovering-thermometer derivation: static acceleration a = GM/(r^2 N), Unruh k_BT = hbar a/2 pi c, Tolman factor N, thermal length 2 pi c^2/a, limit N a -> GM/r_s^2 = c^4/4GM.: Hand derivation from the Schwarzschild metric of the conventions (a = c^2 f'/2 sqrt f); occupation numbers invariant under omega -> N omega; python limit at N = 0.01. → All steps correct. At N = 0.01, a = 1.5213e15 m/s^2 and hbar a/2 pi c k_B = 6.169e-6 K versus T_H/N = 6.170e-6 K; the small gap is the finite distance from the horizon.
- Dimensional analysis: "the only energy built from hbar, c, G, M is hbar c^3/GM".: Counterexample search. → False as written: Mc^2 and the Planck energy sqrt(hbar c^5/G) are energies too. Fixed by requiring a first quantum effect proportional to hbar, times the only rate c^3/GM.
- Charged-hole problem: N a = c^2 f'/2, k_BT_H = hbar c f'(r_+)/4 pi, Reissner-Nordstrom f'(r_+) = (r_+ - r_-)/r_+^2, ratio 15/16 at q = 0.8 m, zero at extremality.: Hand algebra with r_+ + r_- = 2m and r_+ r_- = q^2 (conventions RN factor); python. → 0.9375; T = 0 at q = m; Schwarzschild check recovers hbar c^3/8 pi G M. Correct.
- Bogoliubov calculation: p_omega = integral (alpha f + beta fbar), N = integral |beta|^2, peeling v_0 - v = C e^{-kappa u} with Kruskal U = -4M e^{-u/4M}, |beta| = e^{-pi omega/kappa}|alpha|, Gamma = integral(|alpha|^2 - |beta|^2), N = Gamma/(e^{2 pi omega/kappa} - 1).: Re-derived with positive frequency e^{-i omega t} per the conventions plane-wave row: Gamma-function integral with b = epsilon +/- i omega', |b^{-s}| = |b|^{-1} exp(Im s arg b) with arg b -> +/- pi/2. → Signs, factors of pi and branch correct; the alpha branch carries e^{+pi omega/2 kappa}. Kerr-Newman exponent omega - m Omega_H - q Phi_H consistent with the conventions gauge coupling. Surface-gravity definition sharpened to the horizon generator for rotating holes.
- Two-mode squeezed state problem: norm 1, rho_out thermal, <n> = x/(1-x), S = -ln(1-x) - x ln x/(1-x), pair entropy zero; down-conversion analogy <n> = sinh^2 r with tanh^2 r mapped to e^{-2 pi omega/kappa}.: Hand summation of geometric series; standard two-mode squeezed vacuum sinh^2 r = tanh^2 r/(1 - tanh^2 r). → Correct; the analogy mapping reproduces the Planck factor exactly.
- Grey-body rate dN/dt domega = Gamma/2 pi (e^{hbar omega/kT} -/+ 1) per mode; capture area 27 pi G^2 M^2/c^4; L proportional to 1/M^2.: Standard results; Gamma depends only on GM omega/c^3 so L M^2 is constant; capture radius 3 sqrt 3 GM/c^2. → Correct.
- Entry and working: most of a Sun-mass hole's glow energy is in waves tens of kilometres long (novice query b).: python: Regge-Wheeler equation integrated with RK4 for photons (l = 1-4) and gravitons (l = 2-4), greybody factors from the ingoing amplitude, power summed over omega = 0.02-0.80 in units c^3/GM. → Total power 3.75e-5 hbar c^6/G^2 M^2, matching the published photon plus graviton rate. 99.4% of the energy lies at 10-100 km, median 36 km, peak near 39 km (photon l = 1). Neutrinos are not emitted because their rest energies exceed k_BT_H by about ten orders of magnitude. Claim confirmed; the novice concern's 46 km photon peak is closer to 39 km.
- Entry: a hole twice as heavy is twice as wide, its waves twice as long, half the temperature (novice query a); Sun-mass hole about 6 km across.: Wien peak 4.70e4 m = 15.9 r_s for any mass, so the typical wavelength is a fixed multiple of r_s; diameter 2 r_s = 5.9 km. → Correct for holes without spin or charge, as scoped.
- Entry: counted from far away, the partner brings in negative energy (novice query c), and the working check energy-of-the-partner.: E = -p_mu xi^mu with signature (-,+,+,+): positive for future-directed p when xi is future timelike, either sign when xi is spacelike; local energy -p_mu u^mu > 0. → Correct and consistent with the working misconception, which was rescoped because xi is also spacelike in a spinning hole's ergoregion outside the horizon.
- Entry numbers: 40 million times, six tenths of a Moon mass, a tenth of a millimetre, 27 million, 1.6 degrees, 6 billionths.: python. → CMB/T_H = 4.42e7; M = 4.50e22 kg = 0.613 Moon masses; diameter 0.134 mm; M_sun/M_moon = 2.708e7, giving 1.67 K (answer 1.62 by the rounded 27 million, within rel_tol 0.1); ten suns 6.17e-9 K. Correct.
- Foil try-it: the bare half of a hot mug feels warmer than the foil half at a few centimetres.: Glazed ceramic emissivity about 0.9, shiny aluminium about 0.05; water at 50-60 C gives net radiant flux 180-250 W/m^2 from the bare surface; the natural-convection boundary layer beside a vertical wall is under about a centimetre. → A difference of tens of W/m^2 at the palm is detectable, but "much cooler" overstates it for tap water; changed to "noticeably cooler".
- Sky-matching problem: M = hbar c^3/8 pi G k_B T = 4.50e22 kg, 0.613 Moon masses, r_s = 6.69e-5 m.: python. → 4.5016e22 kg, 0.6131, 6.686e-5 m. Correct.
- Sagittarius A* check: mass about 4.15e6 solar masses.: WebSearch: GRAVITY Collaboration stellar-orbit mass (4.297 +/- 0.012)e6 solar masses. → Updated to 4.30e6: T_H = 1.435e-14 K, background ratio 1.90e14; numeric values and key point changed.
- Worked example: Wien peak 47 km = 16 r_s; photons at kilohertz frequencies.: python: 2.8978e-3 m K/T_H; frequency peak 2.821 kT/h. → 46.96 km, 15.9 r_s; frequency-peak wavelength 82.6 km, 3.6 kHz. Correct.
- Trans-Planckian time: a late quantum passes the Planck frequency about 2 ms after the horizon forms; transients fade in multiples of 4GM/c^3 = 20 microseconds.: python: ln(omega_P/omega)/kappa with omega = k_BT/hbar and kappa = c^3/4GM. → 1.79 ms; 19.7 microseconds. Correct.
- Acoustic metric (rho/c_s)[-(c_s^2 - v^2)dt^2 - 2 v.dx dt + dx.dx], kappa = |d(c_s - |v|)/dx|, 1000 s^-1 gives 1.2e-9 K; Bogoliubov dispersion omega^2 = c_s^2 k^2 + (hbar k^2/2m)^2.: Compared with the standard irrotational barotropic derivation; python for the temperature. → 1.216e-9 K. Correct, including the superluminal bend beyond k ~ 1/xi.
- Primordial holes: initial mass about 5e11 kg evaporating now, T_H = 2.5e11 K, 21 MeV.: python and the Carr et al. 2010 abstract (M* about 5e14 g). → 2.45e11 K, 21.1 MeV. Correct.
- Observation: CMB 2.72548 +/- 0.00057 K.: WebSearch of Fixsen 2009 (ADS, IOP, arXiv 0911.1955). → Confirmed.
- Analogue experiments: water flume stimulated conversion with thermal frequency dependence; rubidium condensate spontaneous, entangled, thermal pairs.: WebSearch: Weinfurtner et al. PRL 106, 021302 (2011); Steinhauer Nat. Phys. 12, 959 (2016); Munoz de Nova et al. Nature 569, 688 (2019). → Confirmed; rubidium atoms and ripples on water correct (novice correction accurate).
- References: Fixsen 2009 ApJ 707 916; Carr, Kohri, Sendouda, Yokoyama 2010 PRD 81 104019 (0912.5297); Munoz de Nova, Golubkov, Kolobov, Steinhauer 2019 Nature 569 688; Parker 1969 Phys. Rev. 183 1057; Bekenstein 1973 PRD 7 2333; Hawking 1975 CMP 43 199; Unruh 1976 PRD 14 870; Unruh 1981 PRL 46 1351; Page 1993 PRL 71 3743; Almheiri et al. 2021 RMP 93 035002; Jacobson 1991 PRD 44 1731; Brout, Massar, Parentani, Spindel 1995 Phys. Rep. 260 329; Barcelo, Liberati, Visser 2011 LRR 14 3; Steinhauer 2016 Nat. Phys. 12 959; Carr and Kuhnel 2020 ARNPS 70 355.: WebSearch against publisher pages (APS, IOP, Springer, Nature, Elsevier, Annual Reviews), ADS and arXiv. → All confirmed and marked verified. Added arXiv 0911.1955 (Fixsen), DOI 10.1016/0370-1573(95)00008-5 and arXiv hep-th/9506121 (Brout et al.), DOI 10.1146/annurev-nucl-050520-125911 (Carr and Kuhnel).
- History scope: Parker first showed particle creation by a time-dependent (expanding) gravitational field; Hawking announced 1974, published 1975; Unruh 1976 accelerated detector; Unruh 1981 sonic analogue.: Abstracts of the primary papers. → Scopes accurate.

**Counterexamples tried**

- Spinning or charged hole of the same mass: breaks "heavier means colder" only if unscoped; entry prose and checks scope to holes without spin or charge, and simplifies says spinning or charged holes are colder (Kerr-Newman T is below hbar c^3/8 pi G M for every a, Q). Confirmed.
- Extremal hole: T_H = 0 and no thermal flux; covered in the charged-hole problem and the formal hypotheses.
- Spinning hole and the partner's negative energy: the Killing vector is spacelike in the ergoregion outside the horizon, so the working misconception's "behind the horizon" was too narrow. Rescoped.
- Dimensional analysis with Mc^2 and the Planck energy: broke "the only energy built from hbar, c, G, M". Fixed.
- Rotating hole and "kappa = lim N a": no static observers near a Kerr horizon. Conditions rescoped to the horizon Killing vector.
- Different observer: hovering detector (T_H/N), freely falling detector (finite energy density about hbar c/r_s^4), distant detector (T_H plus the CMB). Statements consistent.
- Massive species at a Sun-mass hole: neutrinos are Boltzmann-suppressed, so "other kinds of particles" means gravitons there; the entry simplifies is general and remains true for lighter holes.
- Hole in today's universe versus alone in empty space: entry shrink claim scoped to a hole alone in dark, empty space; the CMB way covers growth.
- Far future with dark energy: the CMB cools toward zero but a de Sitter horizon temperature of about 3e-30 K remains; "even heavy holes will glow warmer" holds for all known holes (a 1e10 solar-mass hole is about 6e-18 K).
- Lightest known black holes (about 2.5-5 solar masses): "every black hole found so far is heavier than the Sun" holds.
- Planck-mass end state: fixed-background result invalid; stated in the formal hypotheses and the entry common question.
- Non-static (forming) hole at early retarded times: transients depend on the collapse; formal hypotheses and the common question scope the thermal flux to late times.

**Fixes**

- Working way "The temperature from a hovering thermometer": replaced the false "only energy" dimensional argument with one linear in hbar and the rate c^3/GM.
- Formal way: surface gravity defined from the horizon-generating Killing vector, with the rotating case named, so the Kerr-Newman statement is consistent.
- Key equation temperature-from-surface-gravity: conditions note that the N a limit applies only to static holes.
- Objective derive-temperature-from-surface-gravity: "any static horizon" narrowed to static, spherically symmetric.
- Misconception partner-has-negative-local-energy: negative Killing energy also allowed just outside a spinning hole.
- Check sagittarius-a-star-temperature: mass updated to the current 4.30 million solar masses, with answer, key point and numeric values.
- Research horizon trans-planckian-problem: replaced the vague adiabaticity condition with the requirement that the dispersive scale lie far above kappa.
- Entry try-it: "much cooler" softened to "noticeably cooler".
- All 16 references verified; missing DOIs and arXiv ids added.

**Concerns**

- The physics fixes change learner-visible text (one entry try-it word, one working way, one check, one misconception). Revision kept at 2 so both reviews cover the same text; an editor may bump it and ask for a quick novice re-read.
- course-conventions.md does not fix the surface-gravity normalization (Killing vector normalized at infinity, kappa as an acceleration in SI), the Bogoliubov expansion direction and Klein-Gordon inner-product sign, or the symbol for null infinity. The note's choices are standard, but they should be added to the conventions file.
- Registry prerequisites still differ for quantum-field-theory-in-curved-spacetime, surface-gravity and unruh-effect; run sync_registry.py.
- The working check energy-of-the-partner uses Killing vectors, which no working-rung prerequisite introduces; consider a one-sentence gloss or making surface-gravity needed at working.
- Prerequisite notes horizon-pair-creation-picture and black-body-spectrum do not exist yet, so the entry recaps are unaligned.
- Resolved at revision 7: the colder-than-the-sky entry way now states the extreme faintness (less energy in 50 years than one green-light packet, for a Sun-mass hole with no spin or charge).
- Three proposed visuals (thermometer-beside-a-black-hole, vacuum-pairs-near-a-horizon, rays-peeling-off-a-forming-horizon) still need catalog entries.

**Diff check** (2026-09-13, revision 4)

- New recap in mass-and-temperature: 'A warmer object glows with shorter waves: twice as hot, half as long.': Wien displacement lambda_peak T = 2.898e-3 m K in python; the whole black-body spectrum rescales in wavelength by 1/T. → Ratio 0.5 exactly. Correct for thermal glow, which the way assumes through black-body-spectrum.
- mass-and-temperature explanation (moved unchanged): Sun-mass hole about 6 km across, about 60 billionths of a degree, energy mostly in waves tens of kilometres long; twice the mass, half the temperature, for holes without spin or charge.: python, CODATA constants, GM_sun = 1.32712e20 m^3 s^-2; k_BT_H = hbar c^3/8 pi G M. → Diameter 5.91 km, T_H = 6.17e-8 K, Wien peak 47 km (greybody median 36 km from the earlier review). Scoping carried over with the sentences. Correct.
- mass-and-temperature takeaway and simplifies: heavier hole colder for holes without spin or charge; spinning or charged holes of the same mass colder.: Kerr-Newman kappa = (r_+ - r_-)/2(r_+^2 + a^2) scanned over a, q in python, ratio to 1/4M. → Maximum ratio 1 at a = q = 0. Correct.
- colder-than-the-sky: 'That faint, cold glow is lost in the warmer leftover glow, so nobody has detected Hawking radiation from a real black hole.' (replaces 'That is why ...').: Compared a Sun-mass hole's greybody power (about 2e-28 W, flux 1.7e-68 W/m^2 at 1 kpc) with the Rayleigh-Jeans CMB intensity in the same band; checked the first what-if 'without the leftover glow, could we see it?'. → True: the CMB at those wavelengths exceeds the hole's signal by many orders. The sentence names a sufficient reason, as the old one did; it still omits the extreme faintness, so the what-if stays open (existing concern, kept).
- colder-than-the-sky explanation after the drops: CMB 2.7 degrees is more than 40 million times warmer; only a hole lighter than about six tenths of the Moon's mass glows warmer.: python. → Ratio 4.42e7; mass limit 0.61 lunar masses. Correct; the dropped sentences removed no premise used later.
- colder-than-the-sky recap (unchanged by the re-read, flagged by it): 'Measured from far away, a hole with the Sun's mass glows at about 60 billionths ... Heavier holes glow more coldly.': Counterexamples: a 2-solar-mass non-spinning hole (3.1e-8 K) against a 1-solar-mass extremal hole (0 K); a Sun-mass hole with a = 0.9 (3.7e-8 K). → Both sentences false as unscoped universals. Fixed: the Sun-mass value is scoped to no spin or charge, and the second sentence compares any heavier hole with that value, which holds for every spin and charge because Kerr-Newman T is at most the Schwarzschild T of the same mass. This also supports 'Every black hole found so far is heavier than the Sun, so its glow is even colder' for spinning real holes.
- a-black-hole-that-glows hedges: 'In the pair picture, one member ... can cross the horizon before the pair vanishes.' and 'Take this on trust for now.' after the negative Killing energy sentence.: Consistency with simplifies ('the pair picture is a cartoon'), the working misconception partner-has-negative-local-energy, and the mass-and-temperature caveat. → Consistent; claims unchanged apart from the explicit hedge.
- Split-way bookkeeping: continues links, teaching_arc uses, working way's reference to 'Mass and the temperature of the glow', takeaway split.: Read each link target and the working sentence against the new way. → Targets exist and the quoted numbers match the new way.
- Fix: colder-than-the-sky recap: 'a hole with the Sun's mass glows at about 60 billionths' became 'a hole with the Sun's mass, without spin or charge, glows at about 60 billionths'.
- Fix: colder-than-the-sky recap: 'Heavier holes glow more coldly.' became 'Any heavier hole glows more coldly than that.'
- Fix: Budget: other way fields were at 798 of 800, so dropped the lowest-value item, the a-black-hole-that-glows simplifies sentence 'Besides light, the glow includes other kinds of particles.' (no objective or check uses it; at a Sun-mass hole the other kind is essentially only gravitons).
- Fix: Revision bumped to 4; the novice review now lags one revision.

**Diff check** (2026-09-13, revision 7)

- Tagline: 'Quantum physics makes black holes glow; without spin or charge, heavier ones glow colder'.: k_BT_H = hbar c^3/8 pi G M for Schwarzschild; counterexamples: fixed-J or fixed-Q near-extremal holes (T rises with M), extremal holes (T = 0, but superradiant and charged-particle emission remain). → True as scoped; the scope binds the comparison, which is the only clause that needs it. Correct.
- Check real-hole-in-todays-sky now states 'The hole does not spin or have electric charge.'; answer 'Growing', about 6 billionths of a degree, leftover glow hundreds of millions of times warmer.: python: T_H(10 M_sun) = 6.17e-9 K, 2.7255/6.17e-9 = 4.42e8; CMB absorption through the capture area 27 pi (GM/c^2)^2 far exceeds emission. → Correct; the added scope matches the answer's numbers and spin or charge would only lower T, so the answer holds either way.
- Glossary pair-picture: one member of a pair near the horizon crosses, the other escapes; it helps you imagine the glow but is not the calculation that predicts it.: Consistency with the a-black-hole-that-glows simplifies field, the mass-and-temperature sentence on waves tens of kilometres long, and the working and formal ways (Bogoliubov calculation). → Accurate and consistent; the re-read's verb change ('imagine' for 'picture') keeps the claim.
- try_it: 'Both halves warm the nearby air about equally, but shiny foil gives off very little glow. So a large part of the warmth you felt beside the bare half was the mug's invisible glow.': python heat balance: water 55 C, ceramic wall 5 mm (k = 1.5 W/mK), air 20 C, h = 6 W/m^2K; bare emissivity 0.9, foil 0.05 with a 0.3 mm air gap. What-ifs: foil reflects the palm's own glow back; warm air rises rather than flowing sideways. → Surface 53.6 C vs 52.0 C; convection 202 vs 192 W/m^2 (about equal), radiation 205 vs 11 W/m^2. Beside the wall, outside the roughly 1 cm boundary layer, radiation dominates what the palm feels; the reflected palm glow only narrows the difference. True. 'So a large part' claims the same as the old 'so much'.
- colder-than-the-sky recap reworded: 'a hole with the Sun's mass and no spin or charge glows at about 60 billionths ...'; 'Any heavier hole glows more coldly than that hole.': Compared with the revision-4 wording; Kerr-Newman T at most Schwarzschild T of the same mass (scan from the revision-4 diff check). → Same claims; 'that hole' removes the ambiguity without changing the comparison. Correct for every spin and charge of the heavier hole.
- colder-than-the-sky new paragraph: a Sun-mass hole's glow is far too faint to detect from Earth even without the CMB; light comes in packets; in 50 years the hole gives off less energy than one packet of green light carries.: python, CODATA constants, GM_sun = 1.32712e20: E(550 nm) = 3.61e-19 J (450 nm 4.41e-19, 700 nm 2.84e-19). Power: photons plus gravitons with greybody factors 3.75e-5 hbar c^6/G^2M^2 = 1.63e-28 W (70 years per green packet); black body over horizon area 9.0e-29 W (127 years); over capture area 1.52e-28 W (75 years); earlier 2e-28 W estimate (57 years). Counterexample by spin: Page, Phys. Rev. D 14, 3260 (1976), confirmed by WebSearch (APS/ADS abstract), gives power increases with spin up to 107.5 for photons and 26380 for gravitons, about 2000 times in total at maximal spin (a green packet in about 10 days). Counterexample by charge: a Sun-mass hole with Q above about 2e-6 of extremal has a horizon field above the Schwinger field, so its charged-particle emission far exceeds this. Observer: a hovering observer near the horizon measures a hot Tolman-shifted glow, so 'from Earth' is needed. → True for a Sun-mass hole with no spin or charge under every model (margin 1.1 to 2.5). False for a rapidly spinning or noticeably charged Sun-mass hole, and the paragraph did not state the scope (its 'Sun-mass hole' was scoped only by the recap and the previous way). Fixed by scoping the paragraph's first sentence, which 'the hole' then refers to. The faintness sentence remains true for spinning holes too.
- Fix: colder-than-the-sky explanation: 'Even without the leftover glow, a Sun-mass hole's glow would be far too faint to detect from Earth.' became 'Even without the leftover glow, a Sun-mass hole with no spin or charge glows far too faintly to detect from Earth.' A spinning Sun-mass hole can give off up to about 2000 times more power (Page 1976), so the next sentence's 50-year bound needs this scope.
- Fix: Budget: entry explanations were at the 440-word allowance, so the lowest-value item was shortened: 'In 1974 Stephen Hawking found' became 'Stephen Hawking found' in a-black-hole-that-glows; the year stays in the history entry hawking-1974.
- Fix: Concern about the missing faintness at entry marked resolved.
- Fix: Not applied (not errors; left for an editor): the re-read's proposals to give a reason for 'Both halves warm the nearby air about equally' (the premise is true, see verification) and to add 'Bluer light comes in bigger packets.'
- Fix: Revision bumped 6 to 7; the novice sign-off now lags one revision.
