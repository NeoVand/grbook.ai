---
type: "concept"
schema_version: 2
id: "perihelion-precession-of-mercury"
title: "Anomalous perihelion precession of Mercury"
tagline: "The tiny turning of Mercury's orbit left over after Newton's law and the planets"
domain: "orbits-light-and-tests"
tier: "core"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["Mercury anomaly", "anomalous perihelion advance of Mercury", "Mercury perihelion problem"]
prerequisites: ["perihelion-precession", "birkhoff-theorem"]
leads_to: ["classical-tests-of-general-relativity", "ppn-parameter-beta", "binary-pulsar-periastron-advance"]
visuals: ["orbit-with-creeping-perihelion-markers", "stacked-bars-of-mercurys-perihelion-budget", "advance-versus-distance-across-orbits"]
---

# Anomalous perihelion precession of Mercury

*The tiny turning of Mercury's orbit left over after Newton's law and the planets*

`perihelion-precession-of-mercury` · orbits-light-and-tests · core · physics-reviewed (revision 5)

**Needs:** [[perihelion-precession]] (entry) · [[birkhoff-theorem]] (formal)  
**Opens:** [[classical-tests-of-general-relativity]] · [[ppn-parameter-beta]] · [[binary-pulsar-periastron-advance]]  
**Related:** [[lense-thirring-effect]] · [[bertrands-theorem]] · [[laplace-runge-lenz-vector]] · [[1919-eclipse-expedition]]  
**Visuals:** ★ [[orbit-with-creeping-perihelion-markers]] · [[stacked-bars-of-mercurys-perihelion-budget]] · [[advance-versus-distance-across-orbits]]

> Mercury's orbit slowly turns, so its closest point to the Sun creeps forward, in the direction Mercury travels. Against distant stars it creeps about 575 arcseconds a century, and an arcsecond is one 3600th of a degree. Newton's law and the other planets' pulls explain all but about 43 of those, which Einstein's general relativity predicts with nothing to adjust.

## You will be able to

**Entry**
- Explain which part of Mercury's perihelion creep needed general relativity, and why the rest did not. `objectives/explain-the-budget` ← `checks/video-says-einstein-explains-all`, `checks/two-tables-disagree`
- Explain why general relativity's account of the leftover creep was more convincing than a hidden planet. `objectives/judge-rival-explanations` ← `checks/vulcan-or-relativity`
- Predict how the extra creep from general relativity compares for a planet farther from the Sun. `objectives/predict-other-planets` ← `checks/earths-extra-creep`
- Estimate how long the creep takes to add up to one full turn. `objectives/estimate-the-timescale` ← `problems/years-for-a-full-turn`

**Working**
- Compute a planet's relativistic perihelion advance per orbit and per century from its orbit. `objectives/compute-the-advance` ← `problems/venus-and-earth`
- Distinguish the reference-frame, planetary, solar-flattening and relativistic parts of Mercury's measured advance. `objectives/separate-the-budget` ← `checks/flattened-sun-needed`, `checks/subtract-or-fit`
- Use the pattern of advances across several orbits to tell a modified inverse-square law from general relativity. `objectives/test-a-modified-force-law` ← `problems/tweaked-force-law`

**Formal**
- State the hypotheses under which Mercury's relativistic advance is a prediction with no adjustable parameter. `objectives/state-the-hypotheses` ← `checks/suns-interior-and-shape`
- Derive and apply the dependence of the advance on the post-Newtonian parameters beta and gamma. `objectives/use-the-parametrized-advance` ← `problems/advance-in-other-theories`, `checks/time-and-space-shares`

## Ways in

### 1. The leftover that would not go away · entry · historical-puzzle

*Why did a tiny unexplained creep in the orbit of Mercury become one of the most famous puzzles in astronomy?*

**Recap:** An orbit is the path a planet follows around the Sun. Its perihelion is its closest point to the Sun. Newton showed that a lone planet pulled only by the Sun, with a pull that weakens with the square of the distance, follows the same oval on every trip. So it comes back to the same perihelion each time. A pull from something other than the Sun, or a pull that weakens in a different way, can spoil that perfect repeat. Then the perihelion shifts a little on each trip.

Picture the Sun, and the small planet Mercury going around it once every 88 days. Mercury's orbit is not a circle but a stretched oval. The Sun sits not at the centre of the oval but off towards one end. So the orbit has one closest point, the perihelion. At its perihelion, Mercury is 46 million kilometres from the Sun. At the far end of the oval, it is 70 million kilometres away.

Mercury's perihelion does not stay put. Compared with the distant stars, each new perihelion lies a tiny bit further around the Sun than the last one, in the direction Mercury travels. This means the whole oval slowly turns. This slow turning of an orbit is called precession.

The turning is far too slow to count in whole degrees. So astronomers split one degree into 3600 equal parts. Each part is called an arcsecond. It is an angle, not a time, named like the minutes and seconds of an hour.

Astronomers measure the creep against very distant stars. Those stars cross the night sky as Earth spins, but they keep almost the same pattern among themselves for centuries. Measured that way, Mercury's perihelion creeps about 575 arcseconds each century. Most of that has an ordinary cause. Venus, Jupiter, Earth and the other planets pull on Mercury too. Those extra pulls stop Mercury from repeating exactly the same oval. Working carefully with Newton's law, astronomers found that the planets' pulls explain about 532 arcseconds per century.

That left about 43 arcseconds per century that nobody could explain. The French astronomer Urbain Le Verrier pinned down such a gap in 1859, and later measurements settled it at about 43. He suggested that an unseen planet, closer to the Sun than Mercury, was adding its own pull. People named it Vulcan. Its size and distance could be chosen to fit the gap, so matching the gap proved little. Astronomers searched for it for decades but never found it. They looked hardest during total eclipses of the Sun, when the Moon blocks the Sun's glare.

In November 1915, Albert Einstein used his new theory of gravity to work out Mercury's orbit. This theory is called general relativity. In this theory the Sun's gravity differs very slightly from Newton's law, and the difference is larger closer to the Sun. Like the planets' pulls, that difference spoils the perfect repeat, and it makes the perihelion creep an extra 43 arcseconds per century. Einstein had nothing to adjust. The number came only from the Sun's mass, the speed of light and Mercury's orbit, all measured beforehand. Today's measurements agree with that number to within a small fraction of one per cent.

General relativity gives every planet's perihelion a little extra creep. Of all the planets, Mercury gets the most because it is closest to the Sun. It also goes around the Sun more often than any other planet, so its extra creep adds up fastest. For Venus the extra is about 9 arcseconds per century, and for Earth about 4.

How small is 43 arcseconds? It is the width of a coin 2 centimetres across, seen from about 100 metres away. At that rate the extra creep would need about 3 million years to add up to one full turn. That is why nobody could notice it without centuries of careful records.

**Try it:** Cut an oval from card and mark a dot inside it, near one end, for the Sun. Push a pin through the dot into a sheet of paper on a cork board. Trace around the card. Turn the card about ten degrees around the pin, measured with a protractor, and trace again. Repeat ten times, always turning the same way. The traced ovals fan out like petals, and their closest points to the pin march around it in the direction you turned. On each trip, Mercury's whole creep turns its orbit by only about one 26,000th of one of your ten-degree steps.

**Takeaway:** Newton's law with the pulls of the other planets explains most of Mercury's perihelion creep, but not the last 43 arcseconds per century, which general relativity predicts.

*What this leaves out:* General relativity does not describe gravity as a pull. It describes how the Sun's mass changes space and time around it. For a planet as far out as Mercury, the result behaves almost exactly like Newton's pull plus a tiny extra part that grows faster toward the Sun.

*Builds on:* [[perihelion-precession]]<br>*Visuals:* [[orbit-with-creeping-perihelion-markers]]<br>*See:* `checks/video-says-einstein-explains-all`

### 2. Timing Mercury against the stars · entry · operational

*How can astronomers on Earth measure a creep of only a few hundred arcseconds per century?*

**Recap:** Mercury's orbit is a stretched oval around the Sun, and its perihelion is its closest point to the Sun. The perihelion creeps slowly around the Sun, about 575 arcseconds each century. An arcsecond is one 3600th of a degree.

The 575 arcseconds per century in "The leftover that would not go away" had to be measured. Yet nobody on Earth can see Mercury's oval. Astronomers see only a bright dot moving across the sky. So how do they find where the perihelion is, and how fast it creeps?

One clue comes 13 or 14 times each century. On those days Mercury passes exactly between Earth and the Sun. Through a telescope with a proper sun filter, Mercury looks like a small black dot crossing the Sun's bright face. Never look at the Sun without such a filter. This event is called a transit.

Mercury overtakes Earth about every 116 days, so why are transits so rare? Mercury's orbit is tilted a little compared with Earth's. On most passes, seen from Earth, Mercury goes just beside the Sun's face instead of across it.

Astronomers time the moments when the black dot touches the edge of the Sun, using clocks on Earth. Mercury moves fastest near its perihelion and slowest at the far end of its oval. So the moment Mercury reaches the line between Earth and the Sun depends on which way the oval points. If the oval had turned a little more, or a little less, the dot would arrive a little earlier or a little later. People have timed transits since 1631. Over centuries, astronomers compared those moments with the timings an oval that never turned would give. The differences record how the oval turns.

Today the clues are far better. Radar sends radio pulses from Earth to Mercury and times the echoes. Radio waves travel at the speed of light. Each pulse travels out and back. So an echo that returns one millionth of a second later means Mercury is 150 metres further away. From 2011 to 2015, the MESSENGER spacecraft went around Mercury, and timing its radio signals pinned down Mercury's orbit very precisely.

Every measurement also needs reference directions that do not drift. Astronomers use very distant stars. Older tables measured from directions tied to Earth's spin. Earth spins around an imaginary line through its two poles, and that line slowly swings around in a circle, like the wobble of a tilted spinning top. One circle takes about 25,800 years. So directions tied to that line drift about 5025 arcseconds per century. Measured from those directions, Mercury's perihelion seems to creep about 5600 arcseconds per century. Against the distant stars it creeps about 575, and that is the number the puzzle is about.

**Takeaway:** Transits, radar echoes and spacecraft signals, timed with clocks on Earth, show how Mercury's orbit turns against the distant stars.

*Picture:* Mercury as a small black dot crossing the Sun's bright face, with the moments it touches the Sun's edge marked beside a clock face.

*What this leaves out:* Real measurements also allow for Earth's own motion and for the time light takes to travel. Today astronomers fit the orbits of all the planets at once, rather than one planet at a time.

*Continues:* `ways_in/the-leftover-that-would-not-go-away`<br>*See:* `observations/transits-of-mercury`

### 3. From one formula to 43 arcseconds per century · working · calculation

*What does general relativity predict for Mercury, and why is Mercury the best planet for the test?*

The extra 43 arcseconds per century in "The leftover that would not go away" comes from one formula of general relativity. For a small body on a bound orbit around a spherical mass $M$, the perihelion advances, in the sense of the orbital motion, by

$$\Delta\phi = \frac{6\pi GM}{c^2 a(1-e^2)}$$

per orbit, where $a$ is the semi-major axis and $e$ the eccentricity. For Mercury's stretched oval, $a = 57.9$ million km and $e = 0.2056$, so the perihelion distance $a(1-e)$ is 46.0 million km and the far distance $a(1+e)$ is 69.8 million km. It holds to first order in the small number $GM/(c^2 a)$. Its derivation belongs to perihelion precession, so here it is taken as given. The worked example "Mercury's 43 from its own orbit" turns it into $0.1035''$ per orbit and $42.98''$ per century, with one arcsecond equal to $1/3600$ of a degree, or $4.848\times10^{-6}$ rad.

Why so small? For Mercury, $GM_\odot/(c^2 a) = 2.55\times10^{-8}$. Because $GM/a = v_c^2$, with $v_c$ the speed of a circular orbit of radius $a$, this is also $v_c^2/c^2$; for Mercury $v_c$ is about 48 km/s, one six-thousandth of $c$. The advance becomes measurable only because it accumulates: 415 orbits per century, over centuries of records. In the limit $GM/(c^2 a) \to 0$ the formula gives no advance, as a pure inverse-square force requires.

Why Mercury? Dividing by the Kepler period $T = 2\pi\sqrt{a^3/GM}$ gives the secular rate, meaning the rate averaged over many orbits, of the longitude of perihelion $\varpi$, the angle of the perihelion direction from a fixed reference direction,

$$\dot\varpi = \frac{3(GM)^{3/2}}{c^2 a^{5/2}(1-e^2)}.$$

The rate falls steeply with distance. Venus, at $0.723$ au, gets $8.6''$ per century, and Earth $3.8''$. Mercury also has the largest eccentricity of the planets, $0.206$, and that matters for measurement. A planet's position along its orbit depends on the perihelion direction only through terms proportional to $e$. So for Venus, with $e = 0.0068$, the perihelion is hard to locate at all, while Mercury's is sharply defined.

**Takeaway:** The advance per orbit is six pi GM over c squared a one minus e squared; it is largest for the closest, most eccentric, fastest-orbiting planet.

*What this leaves out:* Keeps only the first order in GM over c squared a, for a test body around a non-rotating spherical Sun.

*Continues:* `ways_in/the-leftover-that-would-not-go-away`<br>*Builds on:* [[perihelion-precession]]<br>*Visuals:* [[advance-versus-distance-across-orbits]]<br>*See:* `worked_examples/mercury-from-its-own-orbit`, `problems/venus-and-earth`, `key_equations/advance-per-orbit`

### 4. Taking the measured advance apart · working · operational

*Which pieces make up Mercury's measured advance, and relative to which reference?*

The distant stars of "Timing Mercury against the stars" fix the reference, and every term in Mercury's budget depends on that choice. Classical analyses measured longitudes from the moving equinox, the direction along which Earth's equatorial plane crosses the plane of Earth's orbit. Earth's wobbling spin axis moves it. In those coordinates Mercury's perihelion advances about $5600''$ per century, of which about $5025''$ is the general precession of the equinoxes and has nothing to do with Mercury. Relative to a non-rotating frame, realized today by distant quasars, about $575''$ per century remains.

Newtonian secular perturbations by the other planets, the orbit-averaged effects of their pulls, computed with independently measured planetary masses, account for about $532''$ of that: roughly $278''$ from Venus, $154''$ from Jupiter, $90''$ from Earth, and about $10''$ from the rest.

The Sun's rotation flattens it slightly, which is described by its quadrupole coefficient $J_2$. For an orbit in the Sun's equatorial plane, to first order in $J_2$, the flattening adds, as taken here on trust,

$$\Delta\phi_{J_2} = 3\pi J_2\left(\frac{R_\odot}{p}\right)^2$$

per orbit, with $R_\odot$ the solar radius and $p = a(1-e^2)$. Helioseismology, which maps the Sun's interior from its surface oscillations, gives $J_2 \approx 2.2\times10^{-7}$. With $R_\odot/p = 0.0125$ that is about $0.03''$ per century. The Lense–Thirring effect of the Sun's spin is smaller still, about $-0.002''$ per century, where the minus sign means against the orbital motion.

What remains is the relativistic advance, $42.98''$ per century. A reassessment published in 1947 found an unexplained $42.56 \pm 0.94''$ per century, against $43.03''$ predicted with the orbital elements then in use.

Modern tests no longer subtract. Ephemeris programs, which compute planetary positions over time, integrate the whole solar system with post-Newtonian equations of motion, fit decades of optical, radar and spacecraft ranging data, and estimate the relativistic parameters, $J_2$ and the planetary masses together. Ranging to the MESSENGER spacecraft in orbit around Mercury confirmed the relativistic advance to a few parts in $10^5$ of its size.

**Takeaway:** Against distant quasars Mercury advances about 575 arcseconds per century: about 532 from the planets, 0.03 from the flattened Sun, and 43 from relativity.

*What this leaves out:* Rounds the planetary terms and treats the Sun's flattening for an orbit in its equatorial plane.

*Continues:* `ways_in/timing-mercury-against-the-stars`<br>*Visuals:* [[stacked-bars-of-mercurys-perihelion-budget]]<br>*See:* `observations/classical-reassessment-1947`, `observations/messenger-ranging`, `checks/subtract-or-fit`

### 5. Could Newtonian gravity be patched? · working · contrast

*Why do a flattened Sun, a slightly altered force law or hidden matter fail where general relativity succeeds?*

Le Verrier's unseen planet in "The leftover that would not go away" was one of several Newtonian patches. Each can be tested with numbers, and each fails for a reason worth seeing.

*A flattened Sun.* The Sun's rotation flattens it slightly, by an amount described by its quadrupole coefficient $J_2$. Flattening adds $3\pi J_2(R_\odot/p)^2$ per orbit, with $R_\odot$ the solar radius and $p = a(1-e^2)$. Supplying all $0.1035''$ per orbit would need $J_2 \approx 3.4\times10^{-4}$, about 1500 times the helioseismic value of $2.2\times10^{-7}$. In 1967 an optical measurement of the Sun's shape suggested $J_2 \approx 2.5\times10^{-5}$, worth about $3''$ per century, enough to favour a rival scalar–tensor theory, which adds a scalar field to gravity. Later measurements did not confirm that flattening.

*A modified force law.* Suppose gravity fell off as $1/r^{2+\delta}$. A nearly circular orbit then has an apsidal angle, the angle swept from perihelion to the next aphelion, of $\pi/\sqrt{1-\delta}$, so it advances by about $\pi\delta$ per orbit. Matching Mercury needs $\delta \approx 1.6\times10^{-7}$, the exponent proposed in 1894. But $\pi\delta$ per orbit is nearly the same for every orbit, while the relativistic $\Delta\phi$ falls as $1/[a(1-e^2)]$. The two ideas therefore predict different advances for Venus, Earth and the Moon, and one exponent cannot reproduce the relativistic pattern.

*Hidden matter.* A planet or dust ring inside Mercury's orbit can be given whatever mass and radius fit the leftover. That freedom makes the fit weak evidence, and searches found no such body.

What general relativity adds is rigidity. Its correction is fixed by $GM_\odot$ and $c$, both measured elsewhere, and the same $GM_\odot/c^2$ also sets the bending of starlight by the Sun.

**Takeaway:** Each Newtonian patch either needs an unobserved size or predicts the wrong pattern across orbits; relativity fixes the leftover with no free number.

*What this leaves out:* The force-law comparison uses the near-circular apsidal angle, accurate to about one per cent at Mercury's eccentricity.

*Continues:* `ways_in/the-leftover-that-would-not-go-away`<br>*Visuals:* [[advance-versus-distance-across-orbits]]<br>*See:* `checks/flattened-sun-needed`, `problems/tweaked-force-law`

### 6. What the prediction assumes · formal · structure

*Under which hypotheses is the advance a parameter-free prediction, and what does it measure in a wider family of theories?*

Set $G = c = 1$. The $42.98''$ per century of "From one formula to 43 arcseconds per century" and the budget in "Taking the measured advance apart" rest on hypotheses that can each be checked.

- *Vacuum exterior and spherical symmetry.* By Birkhoff's theorem, the vacuum region outside a spherically symmetric body is part of Schwarzschild spacetime, whatever the body's radial structure. Only $M_\odot$ enters, and planetary dynamics measures it to about ten significant figures. Departures from symmetry enter separately, as the quadrupole $J_2$ and the spin terms.
- *Test-body limit.* Mercury's mass is $1.7\times10^{-7}M_\odot$. At first post-Newtonian order the two-body advance is $6\pi m/p$ with $m$ the total mass, so the correction is negligible.
- *An invariant observable.* For a bound equatorial geodesic the azimuth swept per radial period is $\Phi = 2\int_{u_a}^{u_p} du/\sqrt{F(u)}$, where $F(u) = (du/d\phi)^2$ and $u_a$, $u_p$ are its roots at aphelion and perihelion. $\Phi/2\pi$ is the ratio of azimuthal to radial frequency, independent of how time or the radial coordinate is labelled. The elements $a$ and $e$ change at relative order $M/p$ under such relabelling, which changes $\Phi - 2\pi$ only at order $(M/p)^2$.
- *Linear superposition.* The planets advance the perihelion by about $10^{-6}$ of a turn per orbit and relativity by about $8\times10^{-8}$, so their secular rates add, with cross terms far below current precision.
- *A non-rotating reference.* Rates refer to a frame tied to distant quasars; converting from equinox-of-date longitudes is purely kinematic.

In Schwarzschild spacetime the integral for $\Phi$ can be evaluated to first order without solving the orbit. With $E$ and $L$ the conserved energy and angular momentum per unit mass, $F(u) = 2Mu^3 - u^2 + 2Mu/L^2 + (E^2-1)/L^2$. This cubic has three roots $u_a < u_p < u_3$, and its $u^2$ coefficient fixes their sum, $u_a + u_p + u_3 = 1/2M$. Hence $F$ factors as

$$F(u) = (u - u_a)(u_p - u)\,[1 - 2M(u + u_a + u_p)].$$

To first order in $Mu_p$, $1/\sqrt{F}$ is $[1 + M(u + u_a + u_p)]/\sqrt{(u-u_a)(u_p-u)}$. Over $[u_a, u_p]$, $\int du/\sqrt{(u-u_a)(u_p-u)} = \pi$ and $\int u\,du/\sqrt{(u-u_a)(u_p-u)} = \pi(u_a+u_p)/2$. So $\Phi = 2\pi + 3\pi M(u_a + u_p)$, and defining $p$ and $e$ by $u_p = (1+e)/p$ and $u_a = (1-e)/p$ in areal radius gives $\Phi - 2\pi = 6\pi M/p$. The neglected terms are smaller by a further factor of order $M/p$, which is $2.7\times10^{-8}$ for Mercury. The expansion fails in strong fields: as $u_p$ approaches $u_3$, at $p = (6 + 2e)M$, $\Phi$ grows without bound.

A wider family of metric theories describes the static weak field by two post-Newtonian parameters: $\gamma$, the spatial curvature produced by unit mass, and $\beta$, the nonlinearity of $g_{tt}$. In isotropic coordinates, with signature $(-,+,+,+)$,

$$g_{tt} = -\left(1 - \frac{2M}{r} + \frac{2\beta M^2}{r^2}\right),\qquad g_{ij} = \left(1 + \frac{2\gamma M}{r}\right)\delta_{ij},$$

and general relativity has $\beta = \gamma = 1$. The derivation "Orbit equation in a parametrized weak field" gives

$$\Delta\phi = \frac{2 + 2\gamma - \beta}{3}\,\frac{6\pi M}{p}.$$

With $\gamma$ fixed by light-deflection and time-delay measurements, Mercury measures $\beta$. The formula also shows that splitting the advance into a part from time and a part from space is not physical. Keeping $g_{tt}$ but making the spatial metric flat removes one third of the advance in areal coordinates, where $g_{tt}$ has no $M^2$ term, and two thirds in isotropic ones.

**Takeaway:** For a test body in a vacuum, spherically symmetric weak field the advance is (2 + 2 gamma - beta)/3 times 6 pi M/p; only the total, not a time or space share, is physical.

*Picture:* The same precessing orbit drawn twice, labelled with areal and isotropic radius, with the time and space shares shaded differently in each panel but the same total advance.

*What this leaves out:* First post-Newtonian order only; the solar quadrupole and spin terms are treated as separate additive rates.

*Continues:* `ways_in/from-one-formula-to-43`, `ways_in/taking-the-measured-advance-apart`<br>*Builds on:* [[birkhoff-theorem]]<br>*See:* `derivations/orbit-equation-in-parametrized-field`, `checks/suns-interior-and-shape`, `checks/time-and-space-shares`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| orbit | — | The path a planet follows around the Sun, over and over. For Mercury it is a stretched oval. | [[kepler-problem]] |
| perihelion | peh-rih-HEE-lee-un | The point of a planet's orbit closest to the Sun. | [[elliptical-orbit-geometry]] |
| creep | — | The slow movement of the perihelion around the Sun from one trip to the next, in the direction the planet travels. | — |
| precession | pree-SESH-un | The slow turning of a whole orbit, which makes its perihelion creep around the Sun. | [[perihelion-precession]] |
| arcsecond | — | A tiny angle: one degree split into 3600 equal parts gives 3600 arcseconds. | — |
| Newton's law of gravity | — | The rule that every two masses pull on each other. Twice as far apart, the pull is four times weaker. | [[newtons-law-of-universal-gravitation]] |
| general relativity | — | Einstein's theory of gravity, from 1915. It matches Newton's law for weak gravity and low speeds, and adds tiny corrections. | — |
| transit | — | A day when Mercury passes exactly between Earth and the Sun and is seen as a small black dot crossing the Sun's face. | — |
| radar | — | A way to measure distance by sending out radio pulses and timing how long their echoes take to come back. | — |

## Key equations

### Relativistic perihelion advance per orbit · working

$$
\Delta\phi = \frac{6\pi GM}{c^2 a(1-e^2)}
$$

The angle by which the perihelion advances, in the sense of the orbital motion, during one orbit.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta\phi$ | advance of the perihelion per orbit, in radians, positive in the sense of the orbital motion | the advance per orbit |
| $GM$ | gravitational parameter of the central body; for the Sun $1.327\times10^{20}$ m$^3$ s$^{-2}$ | G M |
| $a$ | semi-major axis of the orbit | the semi-major axis |
| $e$ | eccentricity of the orbit | the eccentricity |
| $c$ | speed of light | c |

**Holds when:** Test body on a bound orbit around a non-rotating spherical mass; first order in $GM/(c^2 a)$; other perturbations add separately.  
**Say it:** “The advance per orbit is six pi G M divided by c squared times a times one minus e squared.”  
**Justified by:** `perihelion-precession`

### Secular rate of the relativistic advance · working

$$
\dot\varpi = \frac{3(GM)^{3/2}}{c^2 a^{5/2}(1-e^2)}
$$

The average rate at which the longitude of perihelion grows, which shows how steeply the effect falls with distance.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\dot\varpi$ | time-averaged rate of change of the longitude of perihelion, in radians per second | the rate of the perihelion advance |
| $a$ | semi-major axis | the semi-major axis |
| $e$ | eccentricity | the eccentricity |

**Holds when:** As for the advance per orbit, with the Kepler period $T = 2\pi\sqrt{a^3/GM}$.  
**Say it:** “The rate is three times G M to the three halves, divided by c squared times a to the five halves times one minus e squared.”  
**Justified by:** `derivations/rate-from-advance-per-orbit`

### Advance from the Sun's flattening · working

$$
\Delta\phi_{J_2} = 3\pi J_2\left(\frac{R_\odot}{p}\right)^2
$$

The Newtonian advance per orbit produced by the Sun's quadrupole flattening.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $J_2$ | dimensionless quadrupole coefficient of the Sun's gravitational field | J two |
| $R_\odot$ | solar radius, $6.957\times10^8$ m | the solar radius |
| $p$ | semi-latus rectum $a(1-e^2)$ | the semi-latus rectum |

**Holds when:** Orbit in the Sun's equatorial plane; first order in $J_2$. Mercury's orbit is tilted only a few degrees from that plane.  
**Say it:** “The flattening advance is three pi J two times the solar radius over p, squared.”  
**Justified by:** `stated`

### Advance in a parametrized weak field · formal

$$
\Delta\phi = \frac{2 + 2\gamma - \beta}{3}\,\frac{6\pi M}{p}
$$

In any metric theory whose static spherical weak field has post-Newtonian parameters beta and gamma, the advance per orbit is this multiple of the general relativistic value.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\beta$ | post-Newtonian nonlinearity parameter, the $M^2/r^2$ coefficient of $g_{tt}$ in isotropic coordinates | beta |
| $\gamma$ | post-Newtonian space-curvature parameter, the $M/r$ coefficient of $g_{ij}$ in isotropic coordinates | gamma |
| $M$ | mass of the central body, geometrized | M |
| $p$ | semi-latus rectum | p |

**Holds when:** $G = c = 1$; test body; first post-Newtonian order; static, spherically symmetric, vacuum exterior; isotropic-coordinate definitions of $\beta$ and $\gamma$.  
**Say it:** “The advance is two plus two gamma minus beta, over three, times six pi M over p.”  
**Justified by:** `derivations/orbit-equation-in-parametrized-field`

## Derivations

### From the advance per orbit to a rate · working

**Goal:** Turn $\Delta\phi = 6\pi GM/[c^2 a(1-e^2)]$ into an average rate and see how it depends on distance.

1. Kepler's third law gives the orbital period $T = 2\pi\sqrt{a^3/GM}$.
2. The average rate is the advance per orbit divided by the period: $\dot\varpi = \Delta\phi/T$.
3. Substitute: $\dot\varpi = \dfrac{6\pi GM}{c^2 a(1-e^2)}\cdot\dfrac{\sqrt{GM}}{2\pi a^{3/2}}$.
4. Collect powers: $\dot\varpi = \dfrac{3(GM)^{3/2}}{c^2 a^{5/2}(1-e^2)}$.

**Result:** $\dot\varpi = 3(GM)^{3/2}/[c^2 a^{5/2}(1-e^2)]$, which for Mercury is $6.60\times10^{-14}$ rad/s, or $42.98$ per century.

### Orbit equation in a parametrized weak field · formal

**Goal:** Show that the metric with post-Newtonian parameters $\beta$ and $\gamma$ advances a bound orbit by $[(2+2\gamma-\beta)/3]\,6\pi M/p$ per orbit, with $G = c = 1$.

1. Change from isotropic radius $\rho$ to areal radius $r = \rho(1 + \gamma M/\rho)$. To the needed order this gives $g_{tt} = -A$ with $A = 1 - 2M/r + 2(\beta-\gamma)M^2/r^2$, and $g_{rr} = B = 1 + 2\gamma M/r$.
2. In the equatorial plane the Killing symmetries give conserved $E = A\,\dot t$ and $L = r^2\dot\phi$, with dots meaning $d/d\tau$.
3. The normalization $u_\mu u^\mu = -1$ reads $-E^2/A + B\dot r^2 + L^2/r^2 = -1$.
4. With $u = 1/r$ and $\dot r = -L\,du/d\phi$ this becomes $(du/d\phi)^2 = (E^2/A - 1 - L^2u^2)/(BL^2)$.
5. Expand the metric factors: $1/A \approx 1 + 2Mu + (4 - 2\beta + 2\gamma)M^2u^2$ and $1/B \approx 1 - 2\gamma Mu$.
6. Assign orders: $E^2 - 1$, $Mu$ and $L^2u^2$ are each of order $M/p$. Keep products of two such factors and drop the rest.
7. The result is $L^2(du/d\phi)^2 = (E^2-1) + 2Mu - L^2u^2 + (2-2\gamma)(E^2-1)Mu + (4-2\beta-2\gamma)M^2u^2 + 2\gamma ML^2u^3$.
8. Differentiate with respect to $\phi$ and divide by $2L^2\,du/d\phi$: $u'' + u = M/L^2 + (1-\gamma)(E^2-1)M/L^2 + (4-2\beta-2\gamma)(M^2/L^2)\,u + 3\gamma Mu^2$.
9. In the correction terms insert Newtonian values: $L^2 \approx Mp$ and $u \approx (1 + e\cos\phi)/p$. The constant terms only shift $p$.
10. The term linear in $u$ is $(4 - 2\beta - 2\gamma)(M/p)\,u$. The part of $3\gamma Mu^2$ that oscillates at the orbital frequency is $6\gamma(M/p)\,e\cos\phi/p$, which equals $6\gamma(M/p)(u - 1/p)$; the $\cos 2\phi$ part causes no secular change.
11. Collecting the terms that change the frequency: $u'' + [1 - (4 - 2\beta + 4\gamma)M/p]\,u = \text{constant}$.
12. So $u$ oscillates as $\cos(\omega\phi)$ with $\omega \approx 1 - (2 - \beta + 2\gamma)M/p$, and perihelia recur after $2\pi/\omega \approx 2\pi[1 + (2 - \beta + 2\gamma)M/p]$.

**Result:** $\Delta\phi = 2\pi(2 + 2\gamma - \beta)M/p = \dfrac{2+2\gamma-\beta}{3}\,\dfrac{6\pi M}{p}$, which is $6\pi M/p$ for $\beta = \gamma = 1$.

## Worked examples

### Mercury's 43 from its own orbit · working

**Problem:** Use only Mercury's orbit, $a = 5.7909\times10^{10}$ m, $e = 0.20563$ and sidereal period $T = 87.969$ days, together with $c$, to find the relativistic advance per orbit and per Julian century of 36 525 days.

1. Kepler's third law gives $GM_\odot = 4\pi^2a^3/T^2$, so the Sun's mass need not be looked up.
2. Substitute into $\Delta\phi = 6\pi GM/[c^2a(1-e^2)]$: $\Delta\phi = 24\pi^3a^2/[c^2T^2(1-e^2)]$.
3. Numbers: $T = 7.6005\times10^6$ s, $a^2 = 3.3535\times10^{21}$ m$^2$, $T^2 = 5.7768\times10^{13}$ s$^2$, $1 - e^2 = 0.95772$, and $24\pi^3 = 744.15$.
4. $\Delta\phi = \dfrac{744.15\times3.3535\times10^{21}}{8.9876\times10^{16}\times5.7768\times10^{13}\times0.95772} = 5.019\times10^{-7}$ rad.
5. One arcsecond is $4.8481\times10^{-6}$ rad, so $\Delta\phi = 0.1035$ per orbit.
6. A Julian century holds $36\,525/87.969 = 415.20$ orbits, so the advance is $415.20\times0.1035 = 42.98$ per century.

**Answer:** $5.019\times10^{-7}$ rad, or $0.1035$, per orbit; $42.98$ per century.

**Takeaway:** The prediction needs nothing but Mercury's own orbit and the speed of light, so there is no parameter to tune.

## Problems

### `years-for-a-full-turn` · entry · difficulty 1 · estimate

Measured against distant stars, Mercury's perihelion creeps about 575 arcseconds per century. The extra creep from general relativity is about 43 arcseconds per century. One degree is 3600 arcseconds, and a full turn is 360 degrees. How many years would the whole creep take to add up to one full turn? How many years would the extra creep alone take?

**Hints**

1. First find how many arcseconds make one full turn.
2. Divide that by the creep per century, then turn centuries into years.

**Answer:** About 225,000 years for the whole creep, and about 3 million years for the extra creep alone.

**Must contain:** A full turn is 1,296,000 arcseconds; The whole creep needs about 2250 centuries; The extra creep alone needs about 30,000 centuries

**Numeric:** years for the whole creep = 225391 yr (magnitude, ±3%); years for the extra creep alone = 3.01395e+06 yr (magnitude, ±3%)

**Solution**

1. A full turn is 360 degrees, and each degree is 3600 arcseconds, so a full turn is 1,296,000 arcseconds.
2. The whole creep: 1,296,000 divided by 575 is about 2254 centuries, which is about 225,000 years.
3. The extra creep: 1,296,000 divided by 43 is about 30,140 centuries, which is about 3 million years.

### `venus-and-earth` · working · difficulty 2 · calculation

Mercury's relativistic advance is $42.98''$ per century, with $a = 0.3871$ au and $e = 0.2056$. Using the secular rate $\dot\varpi \propto a^{-5/2}(1-e^2)^{-1}$, find the advance per century for Venus ($a = 0.7233$ au, $e = 0.0068$) and Earth ($a = 1.0000$ au, $e = 0.0167$). Why is Venus's value much harder to test than Mercury's, beyond its size?

**Hints**

1. Scale from Mercury rather than recomputing from scratch.
2. How does a planet's position depend on the direction of its perihelion when $e$ is tiny?

**Answer:** Venus about $8.6''$ and Earth about $3.8''$ per century. Venus's orbit is so nearly circular that its perihelion direction barely affects its position, so it is poorly determined.

**Must contain:** Scale by a to the minus five halves and by the ratio of one minus e squared; Venus about 8.6 and Earth about 3.8 arcseconds per century; A nearly circular orbit has a poorly defined perihelion

**Numeric:** Venus advance per century = 8.63 arcsec (magnitude, ±3%); Earth advance per century = 3.84 arcsec (magnitude, ±3%)

**Solution**

1. The rate from $\dot\varpi = 3(GM)^{3/2}/[c^2a^{5/2}(1-e^2)]$ gives a ratio to Mercury of $(a_M/a)^{5/2}(1-e_M^2)/(1-e^2)$.
2. Venus: $(0.3871/0.7233)^{5/2} = 0.2095$, and $0.9577/1.0000 = 0.9577$, so the ratio is $0.2007$ and the advance is $0.2007\times42.98 = 8.6$.
3. Earth: $(0.3871)^{5/2} = 0.0932$, and $0.9577/0.9997 = 0.9580$, so the ratio is $0.0893$ and the advance is $3.8$.
4. A planet's longitude depends on the perihelion direction only through terms proportional to $e$. With $e = 0.0068$, Venus's perihelion direction is weakly constrained, so its small advance carries a large uncertainty.

**Targets:** `only-mercury-feels-it`

### `tweaked-force-law` · working · difficulty 3 · calculation

Suppose the Sun's gravity fell off as $1/r^{2+\delta}$ instead of relativity being right. For a nearly circular orbit the apsidal angle is $\pi/\sqrt{1-\delta}$. (a) What $\delta$ gives Mercury an advance of $0.1035''$ per orbit? (b) What advance per century would this law give Venus (224.70-day period) and Earth (365.26-day period)? Compare with relativity's $8.6''$ and $3.8''$.

**Hints**

1. The perihelion recurs after twice the apsidal angle.
2. Expand $1/\sqrt{1-\delta}$ to first order.
3. The advance per orbit does not depend on $a$; count orbits per century.

**Answer:** (a) $\delta \approx 1.6\times10^{-7}$. (b) Venus about $16.8''$ and Earth about $10.4''$ per century, roughly twice and nearly three times the relativistic values, so the two laws are distinguishable.

**Must contain:** Advance per orbit is about pi times delta; Delta is about 1.6 times ten to the minus seven; The same advance per orbit for every orbit gives Venus about 16.8 and Earth about 10.4 arcseconds per century

**Numeric:** exponent excess delta = 1.6e-07 1 (magnitude, ±5%); Venus advance per century under the modified law = 16.8 arcsec (magnitude, ±3%); Earth advance per century under the modified law = 10.4 arcsec (magnitude, ±3%)

**Solution**

1. Perihelia recur after $2\pi/\sqrt{1-\delta} \approx 2\pi(1 + \delta/2)$, so the advance per orbit is $\pi\delta$.
2. Mercury: $0.1035'' = 5.019\times10^{-7}$ rad, so $\delta = 5.019\times10^{-7}/\pi = 1.60\times10^{-7}$. The near-circular formula is about one per cent low at Mercury's eccentricity, which changes $\delta$ only in the third figure.
3. Venus completes $36\,525/224.70 = 162.55$ orbits per century, so it would advance $162.55\times0.1035'' = 16.8''$.
4. Earth completes $36\,525/365.26 = 100.00$ orbits per century, so it would advance $10.4''$.
5. Relativity predicts $8.6''$ and $3.8''$ because its advance per orbit falls as $1/[a(1-e^2)]$. A single exponent tuned to Mercury overshoots every planet farther from the Sun.

**Targets:** `a-hidden-planet-fits-as-well`

### `advance-in-other-theories` · formal · difficulty 2 · derivation

Using $\Delta\phi = [(2+2\gamma-\beta)/3]\,6\pi M/p$ and Mercury's general relativistic $42.98''$ per century, find the advance per century for (a) Nordström's 1913 scalar theory, with $\beta = 1/2$ and $\gamma = -1$; (b) a scalar–tensor theory with $\beta = 1$ and $\gamma = (1+\omega)/(2+\omega)$ for $\omega = 6$. (c) Which combination of $\beta$ and $\gamma$ does a perihelion measurement alone constrain?

**Hints**

1. Compute the factor and multiply by the general relativistic value.
2. Keep the sign: a negative advance is against the orbital motion.

**Answer:** (a) $-7.2''$ per century, against the orbital motion. (b) $(4+3\omega)/(6+3\omega) = 0.917$, so $39.4''$ per century. (c) Only $2\gamma - \beta$.

**Must contain:** Nordstrom factor is minus one sixth, a retrograde advance of about 7 arcseconds per century; The scalar tensor factor is (4 + 3 omega)/(6 + 3 omega), giving about 39.4 arcseconds per century; The perihelion alone measures 2 gamma minus beta, so gamma must come from light experiments

**Numeric:** advance per century in Nordström's theory, positive with the orbital motion = -7.16 arcsec (signed, ±0.1, mod 1.296e+06); advance per century in the scalar-tensor theory with omega 6 = 39.4 arcsec (magnitude, ±1%)

**Solution**

1. (a) $(2 + 2(-1) - 1/2)/3 = -1/6$, so $\Delta\phi = -42.98/6 = -7.16$ per century.
2. (b) $2 + 2\gamma - 1 = 1 + 2(1+\omega)/(2+\omega) = (4+3\omega)/(2+\omega)$; dividing by 3 gives $(4+3\omega)/(6+3\omega)$.
3. For $\omega = 6$ the factor is $22/24 = 0.9167$, so the advance is $0.9167\times42.98 = 39.40$ per century.
4. (c) The factor depends on $\beta$ and $\gamma$ only through $2\gamma - \beta$, so $\gamma$ from light deflection or time delay is needed to extract $\beta$.

## Observations

- **Transits of Mercury, when Mercury is seen as a black dot crossing the face of the Sun** (measured, entry). The times when the dot touches the Sun's edge depend on where Mercury is along its orbit. Centuries of timed transits recorded how the orbit turns, and they were the main evidence for the leftover creep. *Numbers:* 13 or 14 transits each century. Recent ones were on 9 May 2016 and 11 November 2019, and the next is on 13 November 2032.
- **Mercury's unexplained perihelion advance, from optical observations reduced with Newtonian planetary theory** (measured, working). Observed advance in equinox coordinates minus general precession and planetary perturbations left a residual that matched the relativistic prediction within its uncertainty. *Numbers:* Observed $5599.74 \pm 0.41$ per century in equinox coordinates; computed without relativity $5557.18 \pm 0.85$; difference $42.56 \pm 0.94''$; relativistic prediction $43.03''$. *Reference:* Gerald M. Clemence (1947), *The Relativity Effect in Planetary Motions*, Reviews of Modern Physics 19, 361–364, doi:10.1103/RevModPhys.19.361
- **Radio ranging to the MESSENGER spacecraft in orbit around Mercury, 2011 to 2015** (measured, working). A full solar-system fit including post-Newtonian dynamics, the solar quadrupole and planetary masses found the perihelion advance consistent with general relativity, with $\gamma$ taken from the Cassini time-delay measurement. *Numbers:* $\beta - 1 = (-2.7 \pm 3.9)\times10^{-5}$ and $J_2 = (2.25 \pm 0.09)\times10^{-7}$. *Reference:* Ryan S. Park, William M. Folkner, Alexander S. Konopliv, James G. Williams, David E. Smith, Maria T. Zuber (2017), *Precession of Mercury's Perihelion from Ranging to the MESSENGER Spacecraft*, The Astronomical Journal 153, 121, doi:10.3847/1538-3881/aa5be2

## Teaching arc

1. **Pose the puzzle** (entry). Show an orbit whose closest point creeps, and ask what could make it turn when the Sun alone would not. *Why:* The learner needs the perfect repeat of a lone inverse-square orbit before a leftover can surprise. *Predict:* If only the Sun pulled on a planet, would its closest point to the Sun land in the same spot on every trip? *Visual:* [[orbit-with-creeping-perihelion-markers]] *Uses:* `ways_in/the-leftover-that-would-not-go-away`
2. **Do the budget** (entry). Ask the learner to guess the relativistic share of the 575 arcseconds per century, then reveal the planets and the leftover. *Why:* It heads off crediting relativity with the whole turning. *Predict:* Of the five hundred and seventy-five arcseconds per century, how much do you think needed Einstein? *Visual:* [[stacked-bars-of-mercurys-perihelion-budget]] *Uses:* `checks/video-says-einstein-explains-all`, `ways_in/the-leftover-that-would-not-go-away`
3. **Weigh the rival explanations** (entry). Compare Vulcan with general relativity by asking which explanation had something to adjust. *Why:* The strength of the test is that the prediction had no free number. *Uses:* `checks/vulcan-or-relativity`
4. **See how it is measured** (entry). Walk through transits, radar and spacecraft ranging, then resolve the 5600 versus 575 puzzle. *Why:* Every number in the budget depends on the reference direction. *Uses:* `ways_in/timing-mercury-against-the-stars`, `checks/two-tables-disagree`
5. **Compute and scale** (working). Work Mercury from its own orbit, then scale to Venus and Earth. *Why:* The steep fall-off with distance explains why Mercury carries the test. *Predict:* Venus is almost twice as far from the Sun as Mercury. Is its extra advance per century about half as big, or much smaller? *Visual:* [[advance-versus-distance-across-orbits]] *Uses:* `worked_examples/mercury-from-its-own-orbit`, `problems/venus-and-earth`
6. **Patch Newton and watch it fail** (working). Try a flattened Sun and a tuned force law against the numbers. *Why:* Failing patches show that relativity succeeds by predicting a pattern, not one number. *Visual:* [[stacked-bars-of-mercurys-perihelion-budget]] *Uses:* `ways_in/could-newtonian-gravity-be-patched`, `checks/flattened-sun-needed`, `problems/tweaked-force-law`
7. **Name what is tested** (formal). State the hypotheses, derive the parametrized advance, and show that the time and space shares depend on coordinates. *Why:* It turns a famous number into a measurement of beta with clear limits. *Uses:* `ways_in/what-the-prediction-assumes`, `derivations/orbit-equation-in-parametrized-field`, `checks/time-and-space-shares`

## Analogies

### Missing cents in a bank account · entry

Imagine checking a year of bank statements. Your pay, your rent and every shop receipt explain almost all of the change in your balance. But 43 cents are missing, and they stay missing however carefully you add. You could guess a lost receipt. Or you could learn about a small bank charge you never knew existed. A lost receipt can be given any amount you like. A charge rule, once you know it, predicts the missing amount with nothing to choose.

| In the analogy | Stands for |
| --- | --- |
| the change in the balance over the year | Mercury's measured creep, about 575 arcseconds per century |
| pay, rent and receipts | the other planets' pulls, about 532 arcseconds per century |
| the 43 missing cents | the leftover 43 arcseconds per century |
| a lost receipt of any size | the hidden planet Vulcan |
| a charge rule you did not know | general relativity |

*Limits:* A bank charge is just one more item added on top. General relativity is not an extra pull added to Newton's law. It replaces the law, and it changes the prediction for every orbit, not only Mercury's.

## Misconceptions

### “Einstein's theory explains all of Mercury's orbit turning, the whole 575 arcseconds per century.” · entry · `all-of-it-is-relativity`

- **Why it is tempting:** Popular accounts call Mercury's turning orbit a proof of relativity without giving the budget.
- **What is true:** The other planets' pulls, worked out with Newton's law, explain about 532 arcseconds per century. Only the leftover of about 43 needed general relativity.
- **Exposed by:** `checks/video-says-einstein-explains-all`

### “Relativity changes only Mercury's orbit; the other planets follow Newton's law exactly.” · entry · `only-mercury-feels-it`

- **Why it is tempting:** Mercury is the only planet whose extra creep is famous.
- **What is true:** Every planet gets an extra creep from general relativity, but it shrinks quickly farther from the Sun. Earth's is about 4 arcseconds per century.
- **Exposed by:** `checks/earths-extra-creep`

### “A hidden planet would explain Mercury's leftover just as well, so Mercury proves nothing about Einstein's theory.” · entry · `a-hidden-planet-fits-as-well`

- **Why it is tempting:** A hidden planet had explained an orbit puzzle before, when Neptune was found from its pull on Uranus.
- **What is true:** A hidden planet can be given whatever mass and distance fit, and none was ever found. General relativity predicted the leftover with nothing to adjust.
- **Exposed by:** `checks/vulcan-or-relativity`

### “Mercury's perihelion really creeps about 5600 arcseconds per century.” · entry · `the-creep-is-5600`

- **Why it is tempting:** Older tables quote that total.
- **What is true:** That total is measured from directions tied to Earth's wobbling spin, which drift about 5025 arcseconds per century by themselves. Against distant stars the creep is about 575.
- **Exposed by:** `checks/two-tables-disagree`

### “The Sun's rotation flattens it, and that flattening could produce most of the 43 arcseconds per century.” · working · `flattened-sun-could-do-it`

- **Why it is tempting:** A flattened Sun does add a Newtonian advance, and in 1967 one measurement suggested a large flattening.
- **What is true:** Helioseismology gives a flattening worth only about 0.03 arcseconds per century. Supplying the whole anomaly would need about 1500 times more.
- **Exposed by:** `checks/flattened-sun-needed`

### “The Mercury test is only as reliable as subtracting a Newtonian planetary model from a measured total.” · working · `test-rests-on-subtraction`

- **Why it is tempting:** The story is usually told as 575 minus 532 equals 43.
- **What is true:** Modern ephemerides build relativity into the equations of motion and fit its parameters together with planetary masses and the solar flattening. That fit confirms the relativistic advance to a few parts in a hundred thousand.
- **Exposed by:** `checks/subtract-or-fit`

### “The predicted advance depends on how the Sun's mass is distributed inside it.” · formal · `depends-on-the-suns-interior`

- **Why it is tempting:** Real stars are dense at the centre and thin at the surface, and that feels as if it should matter.
- **What is true:** Birkhoff's theorem makes the exterior of any spherically symmetric body Schwarzschild, fixed by its mass alone. Only departures from spherical symmetry, such as the quadrupole and spin, add small separate terms.
- **Exposed by:** `checks/suns-interior-and-shape`

### “Two thirds of Mercury's advance comes from warped time and one third from curved space.” · formal · `time-and-space-shares-are-physical`

- **Why it is tempting:** Flattening the spatial part of the Schwarzschild metric in its usual coordinates removes exactly one third.
- **What is true:** In isotropic coordinates the same operation removes two thirds. Only the total advance, a ratio of orbital frequencies, is independent of coordinates.
- **Exposed by:** `checks/time-and-space-shares`

## Checks

1. **Entry · evaluate-claim** `checks/video-says-einstein-explains-all`. A science video says: "Measured against the distant stars, Mercury's orbit turns about 575 arcseconds per century, and Einstein's theory explains all of it." Is the video right?
   - **Hints:** What else pulls on Mercury besides the Sun?
   - **Answer:** No. The other planets pull on Mercury, and those pulls make its orbit turn. Worked out with Newton's law, they explain about 532 of the 575 arcseconds per century. So only the leftover, about 43 arcseconds per century, needed a new explanation, and general relativity predicts that leftover. Einstein's theory therefore accounts for about 43 of the 575, less than a tenth.
   - **Must contain:** No, not all of it; The planets explain about 532 arcseconds per century with Newton's law; Relativity explains the leftover of about 43
   - **Numeric:** part explained by general relativity, per century = 43 arcsec (magnitude, ±2)
   - **Targets:** `all-of-it-is-relativity`
   - **Visual:** [[stacked-bars-of-mercurys-perihelion-budget]]
2. **Entry · explain** `checks/vulcan-or-relativity`. In the 1800s, some astronomers thought an unseen planet, closer to the Sun than Mercury, caused Mercury's leftover creep of about 43 arcseconds per century. They named it Vulcan. In 1915 general relativity explained the same leftover. Give two reasons why the second explanation was more convincing.
   - **Hints:** Could the size of Vulcan be chosen to fit? / What did Einstein have to choose?
   - **Answer:** First, nobody found Vulcan, even after decades of searching, including during total eclipses of the Sun. Second, a hidden planet can be given whatever size and distance make the numbers work, so matching 43 would prove little. General relativity had nothing to adjust, because its 43 came only from the Sun's mass, the speed of light and Mercury's orbit. A theory that could have given a different number, but gave the right one, passed a real test.
   - **Must contain:** Vulcan was never found; A hidden planet can be sized to fit anything; Relativity had nothing to adjust
   - **Targets:** `a-hidden-planet-fits-as-well`
3. **Entry · predict** `checks/earths-extra-creep`. General relativity gives Mercury's perihelion an extra creep of about 43 arcseconds per century. Does it give Earth's perihelion an extra creep too? If so, is Earth's extra creep bigger or smaller than Mercury's?
   - **Hints:** Where is the difference from Newton's law largest?
   - **Answer:** Yes, and it is smaller, about 4 arcseconds per century. Every planet gets the extra creep, because every planet moves in the Sun's gravity. Earth is much farther from the Sun, where gravity differs less from Newton's law. Earth also goes around the Sun fewer times each century, so its extra creep adds up more slowly.
   - **Must contain:** Yes, Earth gets an extra creep too; It is smaller, about 4 arcseconds per century; Earth is farther from the Sun and goes around less often
   - **Numeric:** Earth's extra creep per century = 3.8 arcsec (magnitude, ±1)
   - **Targets:** `only-mercury-feels-it`
4. **Entry · explain** `checks/two-tables-disagree`. An old table says Mercury's perihelion creeps about 5600 arcseconds per century. A modern table says about 575. Does one of the tables have to be wrong?
   - **Hints:** What is each table measuring the creep against?
   - **Answer:** No. A creep has to be measured against some direction. The old table measures from directions tied to the imaginary line Earth spins around. That line swings slowly around in a circle, like a tilted spinning top's wobble, so those directions drift about 5025 arcseconds per century by themselves. The modern table measures against the distant stars, which removes that drift and leaves about 575. So the two tables use different references, and the leftover 43 is part of the 575.
   - **Must contain:** Neither table has to be wrong; The old number includes the drift of directions tied to Earth's wobbling spin; Against the distant stars the creep is about 575
   - **Targets:** `the-creep-is-5600`
5. **Working · numeric** `checks/flattened-sun-needed`. The Sun's flattening adds $3\pi J_2(R_\odot/p)^2$ per orbit to Mercury's advance, for an orbit in the Sun's equatorial plane. With $R_\odot = 6.957\times10^8$ m, $p = 5.546\times10^{10}$ m and 415.2 orbits per century, what $J_2$ would supply the whole $42.98''$ per century? How does it compare with the helioseismic $J_2 \approx 2.2\times10^{-7}$?
   - **Hints:** Convert the per-century target to radians per orbit first.
   - **Answer:** Per orbit the target is $42.98''/415.2 = 0.1035'' = 5.019\times10^{-7}$ rad. Because $(R_\odot/p)^2 = (0.012544)^2 = 1.5735\times10^{-4}$, $J_2 = 5.019\times10^{-7}/(3\pi\times1.5735\times10^{-4}) = 3.38\times10^{-4}$. That is about 1540 times the helioseismic value, which supplies only about $0.03''$ per century. So flattening cannot explain the anomaly.
   - **Must contain:** Target 5.02 times ten to the minus seven radians per orbit; J2 needed is about 3.4 times ten to the minus four; About 1500 times the measured value, which gives only 0.03 arcseconds per century
   - **Numeric:** J2 needed = 0.000338 1 (magnitude, ±3%); ratio to the helioseismic value = 1540 1 (magnitude, ±5%)
   - **Targets:** `flattened-sun-could-do-it`
   - **Visual:** [[stacked-bars-of-mercurys-perihelion-budget]]
6. **Working · evaluate-claim** `checks/subtract-or-fit`. Evaluate the claim: "The Mercury test is only as good as the Newtonian subtraction. You take the measured 575 arcseconds per century, subtract 532 from a planetary model, and hope the model is right."
   - **Hints:** What does a modern ephemeris fit estimate?
   - **Answer:** It describes the classical test, not the modern one. Historically the residual depended on the planetary theory and the adopted masses. Modern ephemerides integrate the solar system with post-Newtonian equations of motion and fit the planetary masses, the solar $J_2$ and the parameters $\beta$ and $\gamma$ together to radar and spacecraft ranging. With $\gamma$ from Cassini, MESSENGER ranging gave $\beta - 1 = (-2.7\pm3.9)\times10^{-5}$, so the relativistic factor $(2+2\gamma-\beta)/3$ is confirmed to a few parts in $10^5$.
   - **Must contain:** True of the classical test only; Modern fits estimate relativistic parameters jointly with masses and J2; The relativistic advance is confirmed to a few parts in ten to the five
   - **Targets:** `test-rests-on-subtraction`
7. **Formal · explain** `checks/suns-interior-and-shape`. Why does the predicted relativistic advance not depend on the Sun's density profile, and which properties of the Sun could still change the measured advance? Give their sizes for Mercury.
   - **Hints:** Which theorem describes the vacuum outside a spherical star?
   - **Answer:** Outside a spherically symmetric body the vacuum field is Schwarzschild by Birkhoff's theorem, fixed by $M$ alone, and $GM_\odot$ is measured from planetary motion. So the radial structure cannot enter. What can enter are departures from spherical symmetry and staticity: the quadrupole $J_2 \approx 2.2\times10^{-7}$ adds $3\pi J_2(R_\odot/p)^2$ per orbit, about $0.03''$ per century, and the Sun's spin adds a Lense–Thirring term of about $-0.002''$ per century.
   - **Must contain:** Birkhoff's theorem fixes the exterior by the mass alone; The quadrupole adds about 0.03 arcseconds per century; Solar spin adds about minus 0.002 arcseconds per century
   - **Targets:** `depends-on-the-suns-interior`
8. **Formal · evaluate-claim** `checks/time-and-space-shares`. Evaluate: "Two thirds of Mercury's advance comes from $g_{tt}$ and one third from the curvature of space, because making $g_{rr} = 1$ in Schwarzschild coordinates removes one third." Use the parametrized advance with isotropic $\beta$ and $\gamma$.
   - **Hints:** Write the areal-coordinate metric in terms of beta and gamma. / What values of beta and gamma keep g t t unchanged in each coordinate system?
   - **Answer:** The split is not physical. In areal coordinates $g_{tt} = -[1 - 2M/r + 2(\beta-\gamma)M^2/r^2]$ and $g_{rr} = 1 + 2\gamma M/r$. Setting $g_{rr} = 1$ while keeping the relativistic $g_{tt}$ means $\gamma = 0$ and $\beta = 0$, so the factor is $2/3$ and one third is removed. In isotropic coordinates, keeping $g_{tt}$ means $\beta = 1$, and flattening space means $\gamma = 0$, so the factor is $1/3$ and two thirds are removed. The two operations describe different spacetimes, so the split depends on the choice of radial coordinate. Only the total, $6\pi M/p$, is invariant.
   - **Must contain:** In areal coordinates flattening space leaves two thirds; In isotropic coordinates flattening space leaves one third; The split is coordinate dependent; only the total is physical
   - **Targets:** `time-and-space-shares-are-physical`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| The advance is quoted per orbit or per century, in radians, degrees or arcseconds, under several symbols | $\Delta\phi$ per orbit in radians in formulas, positive in the sense of the orbital motion; observed rates in arcseconds per Julian century of 36 525 days, with $1'' = 4.848\times10^{-6}$ rad on first use. | Some texts write $\delta\phi$, $\Delta\omega$ or $\dot\varpi$, quote rates per year, or give only the fractional excess $\Delta\phi/2\pi$. |
| Totals of about 5600 and about 575 arcseconds per century both appear for Mercury | Quote rates relative to a non-rotating frame tied to distant quasars, about $575$ per century for the total. | Older tables use longitudes from the moving equinox of date, which include the general precession of about $5025$ per century. |
| The post-Newtonian parameters beta and gamma are written in different radial coordinates | Signature $(-,+,+,+)$; define $\beta$ and $\gamma$ in isotropic coordinates, $g_{tt} = -(1 - 2M/r + 2\beta M^2/r^2)$ and $g_{ij} = (1 + 2\gamma M/r)\delta_{ij}$. | In areal coordinates the same metric has $g_{tt} = -[1 - 2M/r + 2(\beta-\gamma)M^2/r^2]$ and $g_{rr} = 1 + 2\gamma M/r$. Texts with signature $(+,-,-,-)$ flip every metric sign. |

## Visuals

- ★ [[orbit-with-creeping-perihelion-markers]] (flagship): The flagship picture: an orbit whose perihelion markers creep, with each cause of the creep switched on separately. *Sketch:* Top-down view of an eccentric orbit around the Sun, with a marker left at each perihelion. The learner steps orbit by orbit or plays whole centuries, sets the eccentricity, and moves a log-scale magnification slider, always labelled, from true scale (markers overlap) to a million times. Toggles add the advances from the other planets, the Sun's flattening and general relativity separately, each with its own colour and line style. Readouts show the advance per orbit and per century in arcseconds and the orbits elapsed. It proves that a tiny advance per orbit accumulates, and that the relativistic share is a small part of the total; the magnification label prevents reading it as strong gravity.
- [[stacked-bars-of-mercurys-perihelion-budget]] (core): Mercury's advance per century as a budget, with the reference frame and the rival explanations as controls. *Sketch:* A horizontal stacked bar of Mercury's advance per century. A reference switch chooses Earth's equinox, which adds a 5025 arcsecond segment for the wobble, or the distant quasars. Segments for Venus, Jupiter, Earth, the other planets, the Sun's flattening and general relativity sit beside the observed total with its error bar. A J2 slider shows how large the Sun's flattening would need to be to fill the relativistic segment, and a switch that removes relativity leaves a visible gap. It proves that relativity is about 7.5 per cent of the advance against the stars and that no measured flattening closes the gap.
- [[advance-versus-distance-across-orbits]] (supporting): Shows why the pattern across orbits, not one number, decides between relativity and a tuned force law. *Sketch:* Log-log plot of advance per century against semi-major axis, with points for Mercury, Venus, Earth, Mars and the asteroid Icarus. One curve is relativity, falling as $a^{-5/2}(1-e^2)^{-1}$; a second is a $1/r^{2+\delta}$ force law whose $\delta$ the learner drags to match Mercury. Matching Mercury makes the second curve overshoot Venus, Earth and Mars, by about a factor of 2 for Venus and 2.7 for Earth.

## Tutor moves

**Open with**

- Picture a planet pulled only by the Sun, exactly as Newton's law says, going around on a stretched oval. After each trip, does its closest point to the Sun land in exactly the same spot, or a little further around? *(prediction)*
- Measured against the distant stars, Mercury's orbit turns about five hundred and seventy-five arcseconds each century. How much of that turning do you think needed Einstein's theory to explain? *(prediction)*

**If the learner is stuck**

- *The learner cannot picture how small 43 arcseconds per century is.* → Use the coin 2 centimetres across at 100 metres, then the 3 million years for a full turn. *Uses:* `problems/years-for-a-full-turn`
- *The learner mixes up the advance per orbit and per century.* → Write $0.1035$ per orbit next to 415.2 orbits per century, and multiply to reach $42.98$. *Uses:* `worked_examples/mercury-from-its-own-orbit`
- *The learner credits relativity with the whole 575 arcseconds per century.* → Ask what else pulls on Mercury, then show the budget bar with relativity switched off. *Uses:* `checks/video-says-einstein-explains-all`
- *The learner loses track of orders in the parametrized orbit equation.* → Assign orders first: $E^2 - 1$, $Mu$ and $L^2u^2$ are each of order $M/p$; keep products of two. *Uses:* `derivations/orbit-equation-in-parametrized-field`

**Common questions**

- *Does this mean Newton's law of gravity is wrong?* (entry) Newton's law is an excellent approximation when gravity is weak and speeds are far below the speed of light, which covers almost everything in the solar system. Mercury shows where it starts to fall short. General relativity agrees with Newton's law in that everyday range and adds tiny corrections that are larger closer to the Sun. For Mercury those corrections add up to about forty-three arcseconds per century. *Uses:* `ways_in/the-leftover-that-would-not-go-away`
- *Why is Mercury the famous one, if every planet gets an extra creep?* (entry) Mercury is closest to the Sun, where the difference from Newton's law is largest. It also goes around most often, so its extra creep adds up fastest. Its orbit is the most stretched of all the planets, which makes its closest point easy to locate. A circle has no single closest point, and Venus's orbit is nearly a circle, so its closest point is hard to pin down. *Uses:* `checks/earths-extra-creep`, `problems/venus-and-earth`
- *Did Einstein predict the leftover before anyone had measured it?* (entry) No. The leftover had been known since 1859. Einstein explained it in 1915 with nothing he could adjust, so a wrong theory would have given a different number. The bending of starlight by the Sun, measured in 1919, tested a number worked out before the measurement. *Uses:* `ways_in/the-leftover-that-would-not-go-away`
- *Why does the formula contain a times one minus e squared rather than a alone?* (working) $p = a(1-e^2)$ is the semi-latus rectum, fixed by the angular momentum through $h^2 = GMp$. The relativistic term in the orbit equation is smaller than the Newtonian one by a factor of order $GM/(c^2p)$, so $p$, not $a$, sets the size. A more eccentric orbit with the same $a$ dips closer to the Sun and advances more. *Uses:* `key_equations/advance-per-orbit`
- *If a and e depend on coordinates, is the advance itself coordinate independent?* (formal) Yes. The azimuth swept per radial period is $2\pi$ times a ratio of frequencies, so relabelling time or radius cannot change it. *Uses:* `ways_in/what-the-prediction-assumes`

**Switching levels**

- To working when: asks where the 43 comes from; uses the words semi-major axis or eccentricity. Go to the formula, the worked example from Mercury's own orbit, and the scaling to Venus and Earth. *Uses:* `ways_in/from-one-formula-to-43`, `worked_examples/mercury-from-its-own-orbit`
- To formal when: asks whether the result depends on coordinates; asks how other theories of gravity would fare. State the hypotheses and derive the parametrized advance. *Uses:* `ways_in/what-the-prediction-assumes`, `derivations/orbit-equation-in-parametrized-field`
- To research when: asks how well beta is measured today; asks about orbits around black holes or in binary pulsars. Open the research horizon on measuring beta and on precession in strong fields. *Uses:* `research_horizon/measuring-beta-with-mercury`, `research_horizon/precession-in-strong-fields`

**Pronunciations:** Le Verrier → luh veh-RYAY; MESSENGER → MESS-en-jer; BepiColombo → BEP-ee koh-LOM-boh; Nordström → NORD-strurm; Birkhoff → BERK-hoff; Lense–Thirring → LEN-zeh TEER-ing; helioseismology → hee-lee-oh-size-MOL-uh-jee; Schwarzschild → SHVARTS-shilt

**Voice notes:** Always say whether a number is per orbit or per century, and what it is measured against.

## History

- **Urbain Le Verrier (1859).** Found that Newtonian planetary perturbations left Mercury's perihelion advance about 38 arcseconds per century short, and proposed unseen matter inside Mercury's orbit. Urbain Le Verrier (1859), *Lettre de M. Le Verrier à M. Faye sur la théorie de Mercure et sur le mouvement du périhélie de cette planète*, Comptes rendus hebdomadaires des séances de l'Académie des sciences 49, 379–383
- **Simon Newcomb (1882).** Reanalysed transits of Mercury back to the seventeenth century and put the unexplained advance at about 43 arcseconds per century.
- **Asaph Hall (1894).** Proposed that gravity falls off with an exponent slightly larger than 2, about $2 + 1.6\times10^{-7}$, to produce the anomaly. Asaph Hall (1894), *A suggestion in the theory of Mercury*, The Astronomical Journal 14, 49–51, doi:10.1086/102055
- **Albert Einstein (1915).** Computed the advance by successive approximation of the vacuum field of the Sun in his new theory and obtained about 43 arcseconds per century, presented on 18 November 1915. Albert Einstein (1915), *Erklärung der Perihelbewegung des Merkur aus der allgemeinen Relativitätstheorie*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 831–839
- **Karl Schwarzschild (1916).** Found the exact exterior solution, which confirmed that the first-order result for the perihelion advance is correct. Karl Schwarzschild (1916), *Über das Gravitationsfeld eines Massenpunktes nach der Einsteinschen Theorie*, Sitzungsberichte der Königlich Preußischen Akademie der Wissenschaften (Berlin), 189–196
- **Robert H. Dicke, H. Mark Goldenberg (1967).** Reported an optical solar oblateness large enough to supply a few arcseconds per century of Mercury's advance, reopening the test; later measurements and helioseismology found a much smaller flattening. R. H. Dicke, H. M. Goldenberg (1967), *Solar Oblateness and General Relativity*, Physical Review Letters 18, 313–316, doi:10.1103/PhysRevLett.18.313

## Research horizon

- **Measuring beta with Mercury.** With $\gamma$ fixed by spacecraft time-delay measurements, Mercury's advance, proportional to $(2+2\gamma-\beta)/3$, measures $\beta$ once the solar $J_2$ is fitted alongside it. Ranging to MESSENGER brought $|\beta - 1|$ to the $10^{-5}$ level, and the radio science experiment of the BepiColombo mission is designed to improve $\beta$, $\gamma$, $J_2$ and possible time variation of $G$ together. Clifford M. Will (2014), *The Confrontation between General Relativity and Experiment*, Living Reviews in Relativity 17, 4, doi:10.12942/lrr-2014-4; B. Bertotti, L. Iess, P. Tortora (2003), *A test of general relativity using radio links with the Cassini spacecraft*, Nature 425, 374–376, doi:10.1038/nature01997; Andrea Milani, David Vokrouhlický, Daniela Villani, Claudio Bonanno, Alessandro Rossi (2002), *Testing general relativity with the BepiColombo radio science experiment*, Physical Review D 66, 082001, doi:10.1103/PhysRevD.66.082001
- **Precession beyond the solar system.** The same first post-Newtonian advance, with the total mass of the system, appears in binary pulsars, where in tight systems it is tens of thousands of times faster per year and is used to weigh the stars; higher post-Newtonian orders are needed for the tightest systems. Around the Galactic Centre black hole, the star S2 shows a prograde Schwarzschild precession of about 12 arcminutes per orbit, consistent with general relativity. T. Damour, G. Schäfer (1988), *Higher-order relativistic periastron advances and binary pulsars*, Il Nuovo Cimento B 101, 127–176, doi:10.1007/BF02828697; M. Kramer, I. H. Stairs, R. N. Manchester, N. Wex and others (2021), *Strong-Field Gravity Tests with the Double Pulsar*, Physical Review X 11, 041050, doi:10.1103/PhysRevX.11.041050; R. Abuter, A. Amorim and others (2020), *Detection of the Schwarzschild precession in the orbit of the star S2 near the Galactic centre massive black hole*, Astronomy and Astrophysics 636, L5, doi:10.1051/0004-6361/202037813
- **The solar quadrupole and planetary ephemerides.** The solar $J_2$ is partly degenerate with $\beta$ in Mercury's advance, but it also moves the orbital node and scales differently with distance, so joint fits of several planets separate them. Helioseismic inversions of the Sun's differential rotation give an independent $J_2$, and agreement between the two is a consistency test of both solar models and gravity. Ryan S. Park, William M. Folkner, Alexander S. Konopliv, James G. Williams, David E. Smith, Maria T. Zuber (2017), *Precession of Mercury's Perihelion from Ranging to the MESSENGER Spacecraft*, The Astronomical Journal 153, 121, doi:10.3847/1538-3881/aa5be2

## Review: novice

**Verdict:** fixed (2026-09-13, revision 4)

**Retell attempt:** Mercury goes around the Sun every 88 days on a stretched oval, and its closest point creeps forward a bit each trip, so the oval turns. They measure it in arcseconds, which I think are tiny, maybe a kind of second? Against the stars it's 575 a century. The other planets pull on Mercury and explain 532, which leaves 43. Le Verrier said a hidden planet Vulcan did it, but nobody found it. Einstein's general relativity gave 43 with nothing to adjust, though I don't see why the Sun's mass isn't something he could choose. Earth gets 4 and Venus 9. It's like a coin at 100 metres. They measure it by timing Mercury crossing the Sun, and with radar and a spacecraft. Old tables say 5600 because Earth's spin line wobbles. I don't get why a Sun-only orbit repeats exactly, why being a bit different from Newton makes the oval turn, why the stars count as not moving when they cross the sky every night, or how timing a dot shows which way the oval points.

**Stumbles (26)**

- “Mercury's orbit slowly turns, so its closest point to the Sun creeps forward about 575 arcseconds each century”: The summary is read at every rung, but 'arcseconds' is never defined there, and 'forward' has no reference.
- “The tiny leftover turning of Mercury's orbit that Newton's gravity could not explain”: The first what-if fails: Newton's gravity plus a hidden planet could explain it; what failed was Newton's law with the known planets.
- “Suppose the Sun alone pulled on a planet, exactly as Newton's law of gravity says. Then the planet would come back to the same perihelion on every trip.”: A surprising claim with no reason: why would the oval repeat exactly?
- “Any extra pull spoils that perfect repeat, so the perihelion creeps a little further around each time.”: False for the first what-if: extra Sun mass pulling the inverse-square way spoils nothing, and some extra pulls shift the perihelion backwards.
- “Mercury's orbit is not a circle but a stretched oval. At its perihelion, Mercury is 46 million kilometres from the Sun.”: If the Sun sat at the centre of an oval there would be two closest points; the reader is never told where the Sun is.
- “After each trip around the Sun, it lies a tiny bit further around”: 'Further around' compared with what? The reference arrives only two paragraphs later, and 'it' has to be traced back.
- “So over many trips the whole oval slowly turns, and the orbit traces a flower-like pattern.”: The 'so' runs backwards (the oval turning is what moves the perihelion), and a flower needs hundreds of thousands of years, not 'many trips'.
- “Each part is called an arcsecond.”: A reader who hears 'second' thinks of time, and 'arcseconds per century' then reads as time per time.
- “very distant stars, which hardly move across the sky”: False to experience: every star crosses the night sky each night.
- “including during total eclipses of the Sun, but never found it”: Why eclipses? The step is left implicit.
- “Give two reasons why the second explanation was more convincing.”: The check expects 'a hidden planet can be sized to fit anything', but no entry way said so.
- “Near the Sun, its gravity differs very slightly from Newton's law, and the difference grows closer to the Sun. That difference makes the perihelion creep”: 'Its' could be Einstein's or the Sun's, and the link from 'differs from Newton' to 'creeps' is missing.
- “Einstein had nothing to adjust, because the number came from the Sun's mass and Mercury's orbit alone.”: First what-if: could he not choose the Sun's mass? And the speed of light is missing from the list.
- “Today's measurements agree with that number closely.”: No number for 'closely'.
- “Mercury gets the most because it is closest to the Sun.”: What-if: something closer than Mercury, such as a comet? The claim needs a scope.
- “Repeat ten times. The traced ovals make a flower ... Mercury's orbit turns about 26,000 times less than that on each trip.”: Eleven tracings at ten degrees fan through 100 degrees, not a flower; the reader has no way to set ten degrees; and 'that' is unclear, with no word on whether the whole creep or only the extra is meant.
- “It describes how the Sun's mass warps space and time.”: 'Warps' is an unexplained picture word.
- “One clue comes 13 or 14 times each century. On those days Mercury passes exactly between Earth and the Sun.”: First what-if: Mercury laps Earth about every four months, so why so rare? Also no eye-safety warning beside a telescope pointed at the Sun.
- “Those moments depend on where Mercury is along its oval on that day. If the oval had turned a little more, or a little less, the dot would arrive a little earlier or a little later.”: The link between which way the oval points and when the dot arrives is taken on trust.
- “Over centuries, those small timing differences build a clear record”: Differences between what and what?
- “an echo that returns one millionth of a second later means Mercury is 150 metres further away”: Light goes 300 metres in a millionth of a second, so 150 looks like an error until the round trip is mentioned.
- “Every measurement also needs a direction that does not creep.”: 'Creep' is the perihelion's movement; here it names a second idea, a drifting reference.
- “that line slowly wobbles, like a tilted spinning top. Directions tied to that wobbling line drift about 5000 arcseconds per century.”: A surprising number with no count to check, and no hint what 'directions tied to' the line are used for.
- “Venus's orbit is so close to a circle that its closest point is hard to pin down at all.”: Why would a nearly round orbit hide its closest point? No reason is given.
- “It agrees with Newton's law when gravity is weak and adds tiny corrections.”: Incomplete condition: fast motion also matters, and the common question on Newton says so.
- “with a pull that weakens with the square of the distance between them”: 'Weakens with the square' is not something this reader can turn into a number.

**Fixes**

- Summary and tagline: the summary now defines the arcsecond, gives 'forward' its reference (the direction Mercury travels), and scopes 'Newton' to Newton's law with the known planets. The tagline fits 90 characters.
- First entry recap: backed the perfect repeat with Newton's result for a pull weakening with the square of the distance. Replaced 'any extra pull spoils it' with a scoped 'can spoil', because extra inverse-square mass at the Sun changes nothing and some pulls shift the perihelion backwards.
- First entry way: put the Sun off-centre so the perihelion is unique; tied the creep to the distant stars at first mention; said the arcsecond is an angle, not a time; fixed the stars 'hardly move' claim; said why Vulcan could fit anything (which prepares the Vulcan check) and why eclipses; linked relativity's difference from Newton to the spoiled repeat; listed the speed of light and said the inputs were measured beforehand; gave 'closely' a scope; scoped 'gets the most' to planets.
- Try-it: a protractor for the ten degrees, 'fan out like petals' instead of a full flower, and the 26,000 ratio tied to the whole creep per trip (checked with python: 36,000 arcseconds over 575/415.2 is 26,000).
- Second entry way: explained why transits are rare (Mercury's tilted orbit; conjunctions about every 116 days, checked with python), added an eye-safety sentence, gave the speed reason that ties transit timing to the oval's direction, stated the round trip behind 150 metres, used 'drift' for reference directions so 'creep' keeps one meaning, and gave the 26,000-year wobble period (1,296,000 arcseconds over 26,000 years is about 5000 per century, checked with python).
- Glossary: Newton's law gets a doubling example; general relativity's agreement with Newton now names weak gravity and low speeds. Why-Mercury common question now says why a near-circle hides its closest point.
- Ladder: working ways now tie a and e to the entry oval's 46.0 and 69.8 million km (checked with python), define secular, longitude of perihelion, equinox, ephemeris programs and apsidal angle, and give J2 and p their meaning inside 'Could Newtonian gravity be patched', which does not continue the way that defines them.
- Budgets: cut entry repetition and trimmed one teaching-arc 'why' so entry explanations (990) and tutoring (3299) fit core caps. Bumped the revision to 2.

**Concerns**

- Physics reviewer: confirm the new entry claim that today's measurements agree with 43 arcseconds per century 'to within a small fraction of one per cent' (the working way claims a few parts in 100,000).
- Physics reviewer: confirm the recap's scoped wording, that a pull from something other than the Sun or one weakening differently 'can' spoil the repeat, and that the transit-timing explanation (faster near perihelion) is a fair entry account.
- The prerequisite perihelion-precession has no v2 note, so the recap restates Newton's closed orbit. Align glossary terms (perihelion, precession, creep) and the recap when that note is written.
- Entry explanations are at 990 of the 1,000 core cap and tutoring at 3,299 of 3,300, so any later entry addition needs a cut elsewhere.
- The entry ways use 'distant stars' and the second adds 'even more distant galaxies', while working rungs say quasars; the proposed budget visual should label its reference switch consistently with these words.
- The writer's convention questions (symbol and sense of the advance, reference frame for quoted rates, PPN parameters) remain open for course-conventions.md; this review did not change them.
- All three visuals are proposals; the flagship sketch's 'magnification slider' must be labelled so the entry reader does not think the orbit really turns that fast.

**Re-read** (2026-09-13, revision 4): 8 stumbles in 14 changed passages

- “Astronomers measure the creep against very distant stars. They cross the night sky as Earth spins”: Rule 11: 'They' could be the astronomers or the stars, and astronomers are the subject of the previous sentence.
- “and the difference grows closer to the Sun”: 'Grows closer' reads as the difference moving toward the Sun, not getting larger near it.
- “Mercury's whole creep turns its orbit about 26,000 times less than one of your ten-degree steps”: '26,000 times less' is a phrase a beginner has to reread: less by 26,000, or divided by 26,000?
- “Over centuries, comparing those moments with the timings an oval that never turned would give records how the oval turns.”: Garden-path sentence: 'give records' reads as one phrase, so the reader rereads to find the verb, and nobody is doing the comparing.
- “Astronomers use very distant stars, and today even more distant galaxies. Earth spins around an imaginary line through its two poles”: Missing step: after naming the stars as the reference, the paragraph jumps to Earth's spin without saying why, and only its last clause ('and older tables measured from them') reveals that older tables used other directions. The clause reads as squeezed on.
- “Picture a planet going around the Sun on a stretched oval, with nothing else in the universe pulling on it. After each trip, does its closest point to the Sun land in exactly the same spot, or a little further around?”: Rule 16: the opening question does not name its setting. The teaching arc expects 'the same spot', which holds for Newton's law, but a learner who has heard of relativity could answer 'a little further around' and be right.
- “General relativity had nothing to adjust, because its 43 came from the Sun's mass and Mercury's orbit alone.”: The entry way lists the Sun's mass, the speed of light and Mercury's orbit, so 'alone' in the Vulcan check answer contradicts what the reader just read.
- “those directions drift about 5000 arcseconds per century by themselves. The modern table measures against the distant stars, which removes that drift and leaves about 575.”: A reader who subtracts gets 5600 minus 5000 = 600, not 575, and wonders where 25 went. The same arithmetic appears in the second entry way and the misconception the-creep-is-5600.
- Fix: Bumped revision 3 to 4. Changed entry text only: 5 learner-visible strings (two entry explanations, the first way's try_it, opening question lone-planet-repeat, common question is-newton-wrong). No claim, number, condition or sense changed.
- Fix: Second entry way: split the transit-comparison sentence into two, and moved 'older tables measured from' into its own sentence before the Earth's-spin explanation so the wobble paragraph has an explicit link. The 26,000-year wobble stays in this way, because the way's question is how the creep is measured and the reference direction is part of that answer.
- Fix: Budget: entry explanations were at 994 of 1,000, and the fixes needed words, so the low-value clause 'and today even more distant galaxies' was dropped from the second entry way (entry now 996). The opening question was reworded two words shorter so the one-word common-question fix keeps tutoring at 3,300.
- Fix: Validator: only the expected warning that review.physics covers an older revision remains.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Advance per orbit 6 pi GM/[c^2 a(1-e^2)], positive in the sense of the orbital motion, first order in GM/(c^2 a), zero in the Newtonian limit.: Checked against the Schwarzschild orbit equation from the course metric and against the parametrized derivation at beta = gamma = 1; dimensional check. → Correct; prograde; the limit GM/(c^2 a) to 0 gives no advance.
- Worked example: GM from Kepler's third law; Delta phi = 24 pi^3 a^2/[c^2 T^2 (1-e^2)] = 5.019e-7 rad = 0.1035 arcsec per orbit; 415.20 orbits and 42.98 arcsec per Julian century; intermediate values of T, a^2, T^2, 1-e^2 and 24 pi^3.: python3 with a = 5.7909e10 m, e = 0.20563, T = 87.969 d and exact c. → GM = 1.32712e20 (1.1e-6 from the IAU value); 5.0187e-7 rad, 0.10352 arcsec, 415.203 orbits, 42.981 arcsec per century; every intermediate matches.
- Perihelion 46.0 and aphelion 69.8 million km; GM/(c^2 a) = 2.55e-8; about 48 km/s, one six-thousandth of c.: python3. → 46.00 and 69.82 million km; 2.550e-8; sqrt(GM/a) = 47.87 km/s = c/6262. Mercury's time-averaged speed is 47.4 km/s, so 'mean speed of about 48' was loose; now the circular-orbit speed.
- Secular-rate derivation and 6.60e-14 rad/s; Venus 8.6 and Earth 3.8 arcsec per century by scaling with a^(-5/2)(1-e^2)^(-1).: Algebra step by step; python3. → 6.603e-14 rad/s; scaling factors 0.2095 and 0.0932 match; Venus 8.63, Earth 3.84; numeric fields and tolerances fine.
- Parametrized derivation: isotropic to areal radius; A = 1 - 2M/r + 2(beta-gamma)M^2/r^2, B = 1 + 2 gamma M/r; expansion of 1/A; second-order orbit equation; omega = 1 - (2 - beta + 2 gamma)M/p; Delta phi = [(2 + 2 gamma - beta)/3] 6 pi M/p.: Re-derived every step by hand: r = rho + gamma M, the E^2/A - 1 expansion times 1/B, differentiation, Newtonian substitution L^2 = Mp, the first harmonic of 3 gamma M u^2, and the linear coefficient (4 - 2 beta + 4 gamma)M/p. → Every intermediate coefficient is correct and the result is the standard PPN perihelion factor. The signature (-,+,+,+) and isotropic g_tt, g_ij forms agree with the course metric.
- Time and space shares: flattening space removes one third in areal coordinates (beta = gamma = 0) and two thirds in isotropic coordinates (beta = 1, gamma = 0).: Substituted into (2 + 2 gamma - beta)/3. → 2/3 and 1/3 remain; correct. The total, a ratio of azimuthal to radial frequencies, is invariant.
- Nordstrom theory (beta = 1/2, gamma = -1) gives -7.16 arcsec per century; the scalar-tensor theory with omega = 6 gives factor 22/24 and 39.40; only 2 gamma - beta is constrained.: python3; parameter values checked against the standard PPN assignments. → -7.163 and 39.398; signs and tolerances correct.
- Flattening advance 3 pi J2 (R/p)^2 per orbit for an equatorial orbit.: Derived from the azimuthal and epicyclic frequencies of the potential -GM/r - GM J2 R^2/(2 r^3); cross-checked with the secular rates of the argument of perihelion plus the node at zero inclination. → Frequency ratio 1 + (3/2) J2 (R/r)^2, giving 3 pi J2 (R/p)^2; correct. The prose now says it is taken on trust, matching justified_by 'stated'.
- Check flattened-sun-needed: R/p = 0.012544, J2 needed 3.38e-4, 1540 times 2.2e-7; helioseismic J2 gives 0.03 arcsec per century; the 1967 value 2.5e-5 gives about 3.: python3. → 0.0125441, 3.384e-4, 1538, 0.028 and 3.18 arcsec per century; all within tolerance.
- Lense-Thirring term about -0.002 arcsec per century, against the orbital motion.: python3 with a varpi rate of -4GJ/[c^2 a^3 (1-e^2)^(3/2)] for a near-equatorial orbit and J = 1.92e41 kg m^2/s; compared with published estimates. → -0.00204 arcsec per century, matching the published -2 milliarcseconds per century.
- Force law 1/r^(2+delta): apsidal angle pi/sqrt(1-delta), advance pi delta per orbit, delta = 1.60e-7, Venus 16.8 and Earth 10.4 per century; the near-circular formula is about one per cent low at Mercury's eccentricity.: Power law r^(n-3) with n = 1 - delta; python3; Gauss's perturbation equation with radial acceleration GM delta ln r / r^2 gives the first-order advance 2 pi delta (1 - sqrt(1-e^2))/e^2 for any e. → delta = 1.597e-7; 16.83 and 10.35; eccentricity factor 1.0108 at e = 0.2056, so 'about one per cent' holds. Hall's exponent 2.00000016 matches. The sketch's factors 1.95 and 2.70 match.
- Budget: general precession about 5025, total about 5600 in equinox coordinates, about 575 against a non-rotating frame; planets 278 + 154 + 90 + 10 = 532; relativity 7.5 per cent of the total.: Compared with the classical planetary terms (Venus 277.9, Earth 90.0, Mars 2.5, Jupiter 153.6, Saturn 7.3, Uranus and Neptune 0.2; total 531.5) and the MESSENGER-era total of 575.31 arcsec per century; python3. → Correct to the stated rounding; 43/575 = 7.48 per cent.
- 1947 reassessment: observed 5599.74 +/- 0.41, computed 5557.18 +/- 0.85, difference 42.56 +/- 0.94, prediction 43.03.: python3 for the difference and the quadrature error; paper record checked on ADS and APS. → 42.56 and 0.944; consistent.
- MESSENGER fit: beta - 1 = (-2.7 +/- 3.9)e-5 and J2 = (2.25 +/- 0.09)e-7 with gamma from Cassini; the advance is confirmed to a few parts in 1e5; the entry says 'within a small fraction of one per cent'.: Read the abstract from the OSTI record; propagated the beta error and the Cassini gamma = 1 + (2.1 +/- 2.3)e-5 into (2 + 2 gamma - beta)/3. → Values confirmed, with a total of 575.3100 +/- 0.0015 arcsec per century. With gamma's error included, the factor is known to about 2.0e-5, so the check's 1.3e-5 (beta alone) became 'a few parts in 1e5'. The entry claim is true.
- Entry numbers: 225,000 and 3 million years for a full turn; a 2 cm coin at 100 m is about 43 arcsec; the try-it ratio of 26,000; overtaking every 116 days; a 26,000-year wobble giving about 5000 arcsec per century; radar 150 m per microsecond.: python3. → 225,391 and 3.01 million years; 41.3 arcsec; 25,995; 115.9 days; 4985 arcsec per century; 149.9 m. All correct.
- Transit timing depends on which way the oval points because Mercury moves fastest near perihelion.: Compared with the equation of the centre: longitude = mean longitude + 2e sin(mean anomaly) + ..., whose phase is set by the perihelion longitude and which arises from the speed variation. → A true and fair entry account; the same terms proportional to e back the working claim about Venus.
- Formal hypotheses: Birkhoff exterior; Mercury's mass 1.7e-7 solar masses; two-body advance 6 pi m/p with total mass m; planets about 1e-6 of a turn and relativity 8e-8 of a turn per orbit.: python3 and standard results. → 1.66e-7; 9.9e-7 and 8.0e-8; correct (Birkhoff with zero cosmological constant).
- Research horizon: binary pulsars tens of thousands of times faster per year; S2 about 12 arcminutes per orbit.: python3 with 4.23 degrees per year for the Hulse-Taylor pulsar and 16.90 for the double pulsar; GRAVITY abstract on arXiv. → 35,000 and 142,000 times Mercury's rate, but wide binaries are slower, so the claim is now scoped to tight systems. S2 is 12 arcminutes with f_SP = 1.10 +/- 0.19; correct.
- References: Clemence 1947 RMP 19 361; Park et al. 2017 AJ 153 121; Le Verrier 1859 CR 49 379-383; Hall 1894 AJ 14 49-51; Einstein 1915 SPAW 831-839 (18 November); Schwarzschild 1916 SPAW 189-196; Dicke and Goldenberg 1967 PRL 18 313; Will 2014 LRR 17 4; Bertotti, Iess and Tortora 2003 Nature 425 374; Milani et al. 2002 PRD 66 082001; Damour and Schafer 1988 Nuovo Cimento B 101 127; Kramer et al. 2021 PRX 11 041050; GRAVITY Collaboration 2020 A&A 636 L5.: Web search of ADS, APS, Nature, Springer, arXiv and OSTI records; author order checked (Kramer, Stairs, Manchester and Wex are the first four). → All confirmed; DOIs added where they exist, arXiv ids for Kramer et al. and GRAVITY; verified set true.

**Counterexamples tried**

- Extra mass at the Sun itself, against the recap: an inverse-square pull stays closed, so 'any extra pull spoils the repeat' would fail; the novice wording 'can spoil' survives. A Hooke-law pull also closes orbits but does not weaken with distance, so the scoped recap holds.
- Force law versus an orbit closer than Mercury: a near-circular orbit at 0.1 au gets several times Mercury's relativistic advance per orbit but the same pi delta, so 'a single exponent overshoots every other orbit' failed; now scoped to planets farther from the Sun. The near-circular law undershoots the asteroid Icarus (9.2 against 10.1 arcsec per century), so the sketch now names Venus, Earth and Mars.
- Another choice of radial coordinate: the time and space shares change (one third or two thirds) while the total does not; the note handles this correctly.
- Another observer frame, equinox of date versus non-rotating: 5600 against 575; handled at the entry and working rungs.
- Wide binary pulsars: their periastron advance per year is not tens of thousands of times Mercury's; the horizon and leads_to are now scoped to tight systems.
- A comet closer to the Sun than Mercury, against 'Mercury gets the most': the entry sentence is already scoped to planets.
- High-proper-motion stars, against 'distant stars keep the same pattern for centuries': Barnard's star moves about 1000 arcseconds per century; now 'almost the same pattern'.
- Le Verrier's mismatch with transit data in the 1840s, against 'first found such a gap in 1859': now 'pinned down such a gap in 1859'.
- Strong fields (S2 and the double pulsar): the first post-Newtonian formula needs higher orders in the tightest systems, and the horizon says so.

**Fixes**

- First entry way: 'first found such a gap in 1859' became 'pinned down such a gap in 1859', and 'keep the same pattern' became 'keep almost the same pattern'.
- Working way 'From one formula to 43': GM/a is the square of the circular-orbit speed (47.9 km/s), not Mercury's mean speed (47.4 km/s).
- Working way 'Taking the measured advance apart': the flattening formula is now marked as taken on trust, matching justified_by 'stated'.
- Problem tweaked-force-law and the proposed visual advance-versus-distance-across-orbits: the overshoot is scoped to planets farther from the Sun.
- Check subtract-or-fit: the confirmation level is now 'a few parts in 1e5', because 1.3e-5 ignored the Cassini uncertainty in gamma.
- Research horizon and leads_to: binary pulsar rates are scoped to tight systems. Related bertrands-theorem: a leftover advance signals a different law or unseen matter once every known pull is counted.
- All 14 reference entries (13 distinct works; the MESSENGER paper appears twice) are verified, with DOIs added for 10 works and arXiv ids for 2.
- Check subtract-or-fit answer shortened by five words to bring tutoring back under the 3,300-word cap.

**Concerns**

- The fixes change learner-visible entry text in two small places (Le Verrier's gap and the star pattern). The revision stays at 2, so both reviews cover the same text; an editor may prefer a revision bump and a quick novice re-read.
- Budgets are at the limit: entry explanations are at about 995 of 1,000 words and tutoring at about 3,300 of 3,300.
- Gaps in course-conventions.md: the symbol and positive sense of the perihelion advance; the reference frame and century used for quoted rates; and the isotropic-coordinate definitions of the PPN parameters beta and gamma. The note is internally consistent, but the conventions file does not fix these choices.
- The registry lists only perihelion-precession as a prerequisite, while the note adds birkhoff-theorem (it exists in other registries); run sync_registry.py.
- The Nordstrom numeric answer carries a modulo of 1,296,000 arcseconds because the validator requires one for signed angles; for a rate per century this is only a formality.
- The formal way calls the conversion from equinox-of-date longitudes purely kinematic. That is true of the coordinate rotation, but the adopted precession constant includes the relativistic geodetic precession of Earth's orbit, about 1.9 arcseconds per century. The simplification is acceptable; a later edit could mention it.

**Diff check** (2026-09-13, revision 5)

- Formal way: with u = 1/r, F(u) = (du/dphi)^2 = 2Mu^3 - u^2 + 2Mu/L^2 + (E^2-1)/L^2 for Schwarzschild geodesics, E and L per unit mass.: Derived by hand from (dr/dtau)^2 = E^2 - (1-2M/r)(1+L^2/r^2) and dphi/dtau = L/r^2 in the course Schwarzschild metric with G = c = 1. → Correct.
- Root sum u_a + u_p + u_3 = 1/2M and the factorization F = (u-u_a)(u_p-u)[1 - 2M(u+u_a+u_p)], positive between the aphelion and perihelion roots.: Vieta on the cubic; sign analysis with leading coefficient 2M > 0; python3 with constructed roots (M = 0.2, u_a = 0.05, u_p = 0.12), recovering L^2 and E^2 from the coefficients and comparing both sides at three points. → u^2 coefficient -1 reproduced; both sides agree to 1e-16.
- First-order expansion, the integrals pi and pi(u_a+u_p)/2, Phi = 2pi + 3pi M(u_a+u_p) = 2pi + 6pi M/p; neglected terms smaller by a factor of order M/p, 2.7e-8 for Mercury.: Hand algebra; python3 midpoint quadrature of 2 integral du/sqrt(F) with the substitution u = mean - half-width cos chi at M/p = 1e-3 and 1e-4 (e = 0.2); M = GM_sun/c^2 = 1476.6 m and p = a(1-e^2) with a = 5.7909e10 m, e = 0.20563. → Relative residual 4.53 M/p and 4.51 M/p, matching the known second-order coefficient (18+e^2)/4; M/p = 2.66e-8, which rounds to 2.7e-8.
- Strong-field failure: as u_p approaches u_3, at p = (6+2e)M, Phi grows without bound.: With u_p = (1+e)/p and u_a = (1-e)/p, setting u_p = u_3 = 1/2M - u_a - u_p gives p = 2M(3+e); python3 quadrature for e = 0.2 at p/M = 7, 6.6, 6.45, 6.41, 6.401. → Phi/2pi = 2.73, 3.69, 4.96, 6.43, 8.51, a logarithmic divergence at 6.4M. Correct, but the result needs e defined by the roots, which the text did not do; fixed.
- Entry rewordings: 'Those stars cross the night sky'; 'the difference is larger closer to the Sun' and 'corrections that are larger closer to the Sun'; transit comparison split into two sentences; 'Older tables measured from directions tied to Earth's spin'; opening question naming a planet pulled only by the Sun as Newton's law says.: Read in context against the pre-reread snapshot; first what-ifs (the Sun's gravity at larger distance, stars with high proper motion, the planet's own pull on the Sun in Newton's two-body problem, the equinox as a direction set by the spin axis and Earth's orbit). → Each claims the same as before or something equally true. Both the absolute and fractional departures from Newton are larger closer to the Sun; the two-body Newtonian orbit is closed, so the opening question's expected answer holds.
- Try-it: the whole creep per trip is about one 26,000th of a ten-degree step.: python3: 36,000 arcseconds divided by 575/415.2. → 25,995; correct.
- Second entry way, check two-tables-disagree and misconception the-creep-is-5600: a 26,000-year wobble drifts reference directions about 5000 arcseconds per century, against totals of 5600 and 575.: python3: 1,296,000 arcseconds over the period; compared with the general precession in longitude (about 5029 today, 5025.6 in the classical budget) and the working way's 5025. → 26,000 years gives 4985, true as 'about 5000' but 5600 - 5000 does not give 575 and disagrees with the working way's 5025. The precession period is about 25,770 years; 25,800 years gives 5023. Changed to 'about 25,800 years' and 'about 5025' in all three places, so the entry subtraction is exact and matches the working rung.
- Check vulcan-or-relativity answer: the 43 came from the Sun's mass and Mercury's orbit alone (flagged by the re-read).: Compared with the advance formula 6 pi GM/[c^2 a(1-e^2)] and the first entry way's list of inputs. → 'Alone' omits the speed of light, which the formula needs and the entry way lists; fixed.
- Fix: Formal way what-the-prediction-assumes: 'defining $p$ by $2/p = u_a + u_p$ in areal radius' became 'defining $p$ and $e$ by $u_p = (1+e)/p$ and $u_a = (1-e)/p$ in areal radius', because the separatrix $p = (6+2e)M$ holds only for $e$ defined by the roots.
- Fix: Second entry way: 'One circle takes about 26,000 years. So directions tied to that line drift about 5000 arcseconds per century.' became 'about 25,800 years' and 'about 5025 arcseconds per century'. Same drift number changed in check two-tables-disagree and misconception the-creep-is-5600.
- Fix: Check vulcan-or-relativity: 'because its 43 came from the Sun's mass and Mercury's orbit alone' became 'because its 43 came only from the Sun's mass, the speed of light and Mercury's orbit'.
- Fix: Budget: tutoring was at its 3,300 cap, so the formal common question is-it-coordinate-free lost its closing clause about a and e shifting at order (M/p)^2, which the formal way's invariant-observable bullet already states.
- Fix: Bumped revision 4 to 5; the novice stage now lags one revision.
