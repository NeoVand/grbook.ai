---
type: "concept"
schema_version: 2
id: "black-hole-information-problem"
title: "Black-hole information problem"
tagline: "Where the information in a black hole goes when the hole evaporates"
domain: "quantum-gravity-and-beyond"
tier: "frontier"
status: "physics-reviewed"
revision: 3
updated: "2026-09-13"
aliases: ["information loss paradox", "black hole information paradox", "information paradox"]
prerequisites: ["black-hole-evaporation", "unitarity-of-quantum-evolution", "bekenstein-hawking-entropy", "quantum-field-theory-in-curved-spacetime", "penrose-diagram-of-evaporating-black-hole"]
leads_to: ["holographic-principle", "ads-cft-correspondence", "quantum-gravity"]
visuals: ["library-hole-and-rock-hole", "page-curve-of-an-evaporating-hole", "pairs-on-a-nice-slice", "one-late-quantum-two-partners"]
---

# Black-hole information problem

*Where the information in a black hole goes when the hole evaporates*

`black-hole-information-problem` · quantum-gravity-and-beyond · frontier · physics-reviewed (revision 3)

**Needs:** [[black-hole-evaporation]] (entry) · [[unitarity-of-quantum-evolution]] (entry) · [[bekenstein-hawking-entropy]] (working) · [[quantum-field-theory-in-curved-spacetime]] (formal) · [[penrose-diagram-of-evaporating-black-hole]] (formal)  
**Opens:** [[holographic-principle]] · [[ads-cft-correspondence]] · [[quantum-gravity]]  
**Related:** [[generalized-second-law]] · [[hawking-radiation]] · [[planck-mass]] · [[euclidean-quantum-gravity]]  
**Visuals:** ★ [[library-hole-and-rock-hole]] · [[page-curve-of-an-evaporating-hole]] · [[pairs-on-a-nice-slice]] · [[one-late-quantum-two-partners]]

> The quantum rules say that, for anything sealed off from everything else, information is never destroyed, only scrambled. In cold, empty space a black hole evaporates by giving off Hawking radiation. In the simplest calculation, that radiation depends only on the hole's mass, spin and electric charge. So if the hole evaporates completely, the information about what fell in seems destroyed. How this clash is resolved is still open.

## You will be able to

**Entry**
- Explain why a black hole that evaporates completely, with the same Hawking radiation whatever fell in, seems to destroy information. `objectives/explain-the-clash` ← `checks/letter-and-rocks`, `checks/burning-a-letter`
- Explain, with a temperature comparison, why nobody can watch a black hole with the Sun's mass evaporate today. `objectives/explain-why-no-one-can-watch` ← `checks/sun-mass-hole-in-space-microwaves`

**Working**
- Compute the Page time and the mass left at that time from the evaporation law and the entropy bookkeeping. `objectives/compute-page-time` ← `problems/page-time-for-other-entropy-ratios`
- Explain why the conflict begins while the black hole is still large. `objectives/explain-when-the-clash-begins` ← `checks/page-time-hole-is-still-big`

**Formal**
- Derive the radiation's thermal state and entropy by tracing out Hawking's interior partners. `objectives/derive-thermal-radiation-state` ← `problems/entropy-of-one-hawking-mode`
- Use entropy inequalities to show that an old black hole cannot keep both a unitary Page curve and a smooth horizon. `objectives/use-entropy-inequalities` ← `checks/monogamy-for-an-old-black-hole`
- Identify which assumption each proposed resolution gives up, and estimate what a remnant would have to hold. `objectives/classify-proposed-resolutions` ← `problems/which-assumption-each-proposal-gives-up`, `checks/planck-mass-remnant-states`
- Explain why radiation from a unitarily evaporating hole looks thermal until about the Page time. `objectives/explain-early-thermality` ← `checks/thermal-spectrum-is-not-proof`

**Research**
- State what island and replica-wormhole calculations establish and what they leave open. `objectives/scope-island-results` ← `checks/what-island-calculations-show`
- Estimate how soon information thrown into an old black hole can be recovered from its radiation. `objectives/estimate-information-return` ← `problems/hayden-preskill-return-time`

## Ways in

### 1. Throw a letter into a black hole · entry · picture

*What happens to the information about everything that falls into a black hole once the hole evaporates?*

**Recap:** A black hole is a region where gravity is so strong that nothing that enters, not even light, comes back out. Its edge is called the horizon. A black hole gives off a faint glow, called Hawking radiation. Measured from far away, a hole without spin or electric charge is colder the heavier it is. Spin or charge makes a hole colder still. In cold, empty space the glow carries away energy, and energy has mass, so the hole slowly gets lighter. This is called evaporation. The quantum rules are the laws of atoms and light. A thing's state is its complete description at one moment. For anything sealed off, these rules work both ways in time: its state at one moment settles its state at all others.

Write a secret letter and burn it. The words look destroyed, but the quantum rules say they are not. Every different secret leaves the smoke, ash, heat and light arranged a little differently. The rules work backwards too, so someone tracking every piece could recover the words. Physicists call such details information.

Now drop the letter into a black hole. Nothing that crosses the horizon comes back out. That alone breaks no rule, because the information could be stored inside.

In the simplest calculation, Hawking radiation depends only on the hole's mass, spin and electric charge. So two holes with matching numbers give off the same kind of radiation, even if only one swallowed the letter. Count the hole and its radiation as one sealed-off thing. Once the hole has evaporated completely, only that radiation is left. Two different starts end the same, which the quantum rules forbid. This clash is called the black-hole information problem.

Perhaps the radiation carries the information in hidden links between its particles, which the simplest calculation misses. This kind of purely quantum link is called entanglement. Perhaps a tiny leftover keeps the information. Perhaps the quantum rules fail. Many physicists expect hidden links, but nobody knows how they work for a real black hole. Going further needs entanglement and black-hole entropy.

Nobody can watch a black hole evaporate yet. A hole with the Sun's mass glows at only about sixty billionths of a degree above absolute zero. Faint microwaves left from the early universe fill space at about 2.7 degrees above absolute zero. Like a cold drink in a warm room, the hole takes in more than it gives off, so it grows. Every black hole found so far is heavier than the Sun, so even colder.

**Try it:** On paper, write the word CAT. Rule one: replace each letter by the next letter of the alphabet, with Z becoming A. CAT gives DBU, and anyone who knows the rule can step back to CAT. Rule two: replace every letter by X, giving XXX. Now try DOG. Rule one gives EPH, but rule two gives XXX again, so from XXX nobody can tell which word you started with. The quantum rules behave like rule one: they can scramble, but two different starts never end the same. A black hole whose Hawking radiation is the same whatever fell in would behave like rule two.

**Takeaway:** If a black hole evaporates completely and its Hawking radiation is the same whatever fell in, the information seems destroyed. The quantum rules forbid that, and how the clash is resolved is still open.

*What this leaves out:* The simplest calculation treats space and time near the hole as smooth and ordinary. That calculation is expected to fail at the very end, when the hole is tiny. But the clash starts much sooner, while the hole still has most of its mass. So if the quantum rules hold and no tiny leftover keeps the information, the simplest calculation must already be missing something while the hole is big. "Keep the books with the Page curve" shows why with a count.

*Builds on:* [[black-hole-evaporation]], [[unitarity-of-quantum-evolution]]<br>*Visuals:* [[library-hole-and-rock-hole]]<br>*See:* `checks/letter-and-rocks`, `checks/sun-mass-hole-in-space-microwaves`

### 2. Keep the books with the Page curve · working · calculation

*If evaporation loses no information, how must the radiation's entanglement rise and fall, and when does that clash with Hawking's calculation?*

In "Throw a letter into a black hole", Hawking radiation in the simplest calculation was the same whatever fell in, so the letter's information seemed destroyed once the hole evaporated. The hidden links suggested there are entanglement, and keeping the books with entropy, which measures entanglement, shows *when* the trouble starts.

Two entropies are needed. The coarse-grained, or thermodynamic, entropy is $k_B$ times the logarithm of the number of microscopic states compatible with what is measured, such as a spectrum. A density matrix $\rho$ describes a system's quantum state: $\rho = |\psi\rangle\langle\psi|$ for a pure state, and a weighted sum of such terms for a mixed one, such as a part of a larger entangled system. The fine-grained entropy of a system with density matrix $\rho$ is $S = -k_B\,\mathrm{Tr}(\rho\ln\rho)$. It vanishes for a pure state and never exceeds the coarse-grained entropy. A part of a pure whole can still have $S > 0$, because it is entangled with the rest: in the pure two-spin state $(|{\uparrow\downarrow}\rangle - |{\downarrow\uparrow}\rangle)/\sqrt2$, each spin alone has $S = k_B\ln 2$.

In Hawking's calculation each outgoing quantum is created entangled with a partner just inside the horizon. So the fine-grained entropy of the radiation grows as it is emitted, and equals the radiation's thermal entropy $S_{\rm H}(t)$. For ideal black-body emission, the derivation "Page time from the evaporation law" gives $S_{\rm H}(t) = \tfrac43\,[S_{\rm BH}(0) - S_{\rm BH}(t)]$, where $S_{\rm BH} = 4\pi G k_B M^2/\hbar c$ is the Bekenstein–Hawking entropy.

Now impose unitarity. Hole and radiation began in a pure state, so their fine-grained entropies stay equal. Assume the hole has about $e^{S_{\rm BH}/k_B}$ internal states. Its fine-grained entropy cannot exceed $k_B$ times the logarithm of that number, so neither can the radiation's:

$$S_{\rm rad}(t) \le \min\{S_{\rm H}(t),\ S_{\rm BH}(t)\}.$$

For dynamics that scramble like a typical quantum system, $S_{\rm rad}$ stays close to this bound. It rises with Hawking's curve, turns over where the two curves meet, and falls to zero as the hole disappears. This rise and fall is the Page curve, and the turnover is the Page time. Hawking's calculation, taken to the end, instead keeps rising to $\tfrac43 S_{\rm BH}(0)$.

The curves meet when $S_{\rm BH} = \tfrac47 S_{\rm BH}(0)$, at $M = 0.756\,M_0$ and $t = 0.568\,\tau$, where $\tau$ is the lifetime. For a hole of one solar mass, $1.989\times10^{30}$ kg, $S_{\rm BH}(0) = 1.05\times10^{77}\,k_B$. At its Page time the horizon radius $2GM/c^2$ is still 2.23 km, and the radius of curvature there is about 1.2 km, some $10^{38}$ Planck lengths, where the Planck length $\sqrt{\hbar G/c^3} = 1.6\times10^{-35}$ m is the scale at which quantum gravity is expected to matter. Semiclassical physics, quantum fields on a classical spacetime, is expected to fail only near that scale. The conflict therefore begins long before the Planck-scale end.

**Takeaway:** If evaporation is unitary, the entanglement entropy of the radiation must turn over at the Page time, while the hole still has most of its mass, not only at the Planck-scale end.

*What this leaves out:* Treats the emission as ideal black-body photons, ignores how the hole's gravity filters the radiation, which changes the factor $\tfrac43$, and assumes that the Bekenstein–Hawking entropy counts the hole's internal states.

*Continues:* `ways_in/throw-a-letter-into-a-black-hole`<br>*Builds on:* [[bekenstein-hawking-entropy]], [[black-hole-evaporation]], [[unitarity-of-quantum-evolution]]<br>*Visuals:* [[page-curve-of-an-evaporating-hole]]<br>*See:* `derivations/page-time-from-evaporation-law`, `checks/page-time-hole-is-still-big`, `problems/page-time-for-other-entropy-ratios`

### 3. Pairs across the horizon · formal · structure

*What exactly is the state Hawking found, and which assumptions does complete evaporation set against each other?*

The Page curve in "Keep the books with the Page curve" rested on one fact from Hawking's calculation: each outgoing quantum is entangled with a partner behind the horizon. Here that fact is made precise. Set $G = c = \hbar = k_B = 1$.

Consider a free quantum field on the spacetime of a spherical collapse to a black hole of mass $M$ and surface gravity $\kappa = 1/4M$. Take late-time outgoing wavepackets $b_\omega$, peaked at frequency $\omega$ measured at infinity, and their partner packets $c_\omega$ behind the horizon. Neglecting the partial reflection of the packets by the potential barrier around the hole, the state that evolves from the vacuum before collapse is, for these packets,

$$|\Psi\rangle = \bigotimes_\omega \sqrt{1 - e^{-2\pi\omega/\kappa}}\,\sum_{n=0}^{\infty} e^{-\pi n\omega/\kappa}\,|n\rangle_{b_\omega}|n\rangle_{c_\omega}.$$

Tracing out the partners leaves $\rho_b = \bigotimes_\omega (1 - e^{-2\pi\omega/\kappa})\sum_n e^{-2\pi n\omega/\kappa}\,|n\rangle\langle n|$, exactly thermal at $T_{\rm H} = \kappa/2\pi$. Its von Neumann entropy $S(\rho) = -\mathrm{Tr}\,\rho\ln\rho$ is positive for every packet, so each emission adds entanglement between outside and inside.

The argument does not rely on strong curvature. Nice slices are Cauchy slices that pass through the distant radiation, cross the horizon, and stay inside at a radius of order $M$, far from the singularity. Curvature is of order $1/M^2$ everywhere on them, so effective field theory should hold there for a large hole. If the hole evaporates completely and nothing remains, the state on future null infinity is mixed, carrying the total Hawking entropy, although the collapsing matter was in a pure state.

One standard way to state the conflict is that four assumptions cannot all hold:

- (U) evolution from past to future null infinity is unitary;
- (E) effective field theory holds on nice slices and at the horizon of a large hole, up to small corrections;
- (L) the interior partners, the near-horizon quanta and the far radiation are independent subsystems, and each emission leaves the far radiation untouched;
- (R) nothing remains after evaporation to purify the radiation.

The derivation "Small corrections cannot turn the curve over" makes (E) quantitative. If each new pair has $S(bc) \le \epsilon$, then (L) and strong subadditivity give $S(Rb) \ge S(R) + S(b) - 2\epsilon$. The radiation's entropy keeps growing, so a Page curve needs a failure of (E) or (L); if both hold, (U) or (R) must go.

A thermal spectrum is not by itself evidence for loss. For a random pure state on a Hilbert space of dimension $mn$ with $1 \ll m \le n$, the smaller factor has average entropy close to $\ln m - m/2n$, almost maximal. Radiation from a unitary hole is therefore expected to look thermal until about the Page time, with its information stored in correlations among many quanta.

**Takeaway:** Hawking's pairs make the radiation's entanglement grow with each emission, so unitarity, effective field theory at the horizon, locality, and complete evaporation cannot all survive.

*What this leaves out:* Ignores greybody factors, back-reaction during each emission, and interactions among emitted quanta. The split into independent subsystems in (L) is itself subtle in gravity.

*Continues:* `ways_in/keep-the-books-with-the-page-curve`<br>*Builds on:* [[quantum-field-theory-in-curved-spacetime]], [[penrose-diagram-of-evaporating-black-hole]], [[unitarity-of-quantum-evolution]]<br>*Visuals:* [[pairs-on-a-nice-slice]]<br>*See:* `derivations/small-corrections-cannot-turn-the-curve`, `problems/entropy-of-one-hawking-mode`, `checks/thermal-spectrum-is-not-proof`

### 4. One late quantum cannot serve two partners · formal · historical-puzzle

*Can an old black hole keep both a pure final state and a smooth horizon, as complementarity hoped?*

The pair state of "Pairs across the horizon" set unitarity against a smooth horizon. The best-known attempt to keep both is black-hole complementarity, proposed in 1993. Set $G = c = \hbar = k_B = 1$.

Complementarity keeps (U) and (E) and relaxes (L) in a limited way. For an observer who stays outside, information is absorbed by a hot membrane just outside the horizon, the stretched horizon, and returns in the radiation. For an observer who falls in, the same information crosses the horizon without incident. No single observer can hold both copies, so the no-cloning theorem is never violated in any one observer's experiment.

In 2012 Almheiri, Marolf, Polchinski and Sully described one observer who seems to break this. Take an old black hole, past its Page time. Let $R$ be the early radiation, $b$ a late outgoing quantum and $c$ its interior partner. The Page curve requires the radiation's entropy to fall as $b$ joins it: $S(Rb) < S(R)$. A smooth horizon requires $bc$ to be close to the pure pair state of "Pairs across the horizon". If $bc$ is exactly pure, then $\rho_{Rbc} = \rho_R\otimes|\psi\rangle\langle\psi|_{bc}$, so $\rho_{Rb} = \rho_R\otimes\rho_b$ and $S(Rb) = S(R) + S(b) > S(R)$. The two requirements contradict each other. Entanglement is monogamous: a system maximally entangled with $c$ has nothing left to share with $R$.

An observer could distil the relevant part of $R$ outside, then fall in and test whether $b$ and $c$ are entangled, so complementarity's escape seemed not to apply. Harlow and Hayden later argued that this decoding may take far longer than the hole's lifetime. The four authors argued that the least radical option is to give up (E) at the horizon of an old hole, so that an infalling observer meets high-energy quanta: a firewall.

Other responses keep the horizon smooth and give up the independence in (L). After the Page time, the partner $c$ need not be a separate system from $R$; it can be encoded in $R$ itself. Proposals include ER = EPR, in which entangled systems are joined by geometry, and state-dependent reconstruction of the interior. The island calculations make this encoding precise in specific models.

**Takeaway:** For an old black hole, unitarity and a smooth horizon conflict unless the interior partner is encoded in the early radiation instead of being independent of it.

*What this leaves out:* Treats the partner state as exactly pure; with approximate purity the same conclusion follows from strong subadditivity.

*Continues:* `ways_in/pairs-across-the-horizon`<br>*Visuals:* [[one-late-quantum-two-partners]]<br>*See:* `checks/monogamy-for-an-old-black-hole`, `problems/which-assumption-each-proposal-gives-up`, `history/stu-1993`, `history/amps-2012`

### 5. Islands compute the Page curve · research · calculation

*How can a semiclassical gravity calculation produce the Page curve, and what does it establish?*

The Page curve of "Keep the books with the Page curve" was a bound imposed by unitarity, and "One late quantum cannot serve two partners" left open how an interior partner could be encoded in the radiation. Since 2019 both have been addressed by computing the radiation's fine-grained entropy with the gravitational path integral. Set $G = c = \hbar = k_B = 1$.

The setting is a black hole in a gravitating region coupled to a non-gravitating bath that absorbs its radiation $R$: for example a two-dimensional Jackiw–Teitelboim black hole, or an anti-de Sitter black hole with transparent boundary conditions. The entropy of $R$ is given by a rule that extends the quantum extremal surface prescription of holography:

$$S(R) = \min_{I}\,\operatorname*{ext}_{I}\left[\frac{\mathrm{Area}(\partial I)}{4} + S_{\rm bulk}(R\cup I)\right].$$

Here $I$, the island, is a region of the gravitating spacetime, and $S_{\rm bulk}$ is the von Neumann entropy of the quantum fields in $R\cup I$, computed as in "Pairs across the horizon". One extremizes over the island's boundary and takes the smallest extremum.

With no island the rule returns $S_{\rm bulk}(R)$, which grows as in Hawking's calculation. For an evaporating hole, a nontrivial extremum also exists, with $\partial I$ just inside the event horizon. Its area term is close to $S_{\rm BH}$, and $S_{\rm bulk}(R\cup I)$ is small because $I$ contains the partners of most of the radiation. That branch falls as the hole shrinks. The minimum switches branch at the Page time, giving a Page curve.

The rule follows from the replica trick. $\mathrm{Tr}\,\rho_R^n$ is a path integral over $n$ copies of the geometry glued cyclically along $R$. Besides saddles that keep the copies apart, there are replica wormholes that connect them through the gravitating region. Continuing to $n \to 1$ produces the island term.

After the Page time the island lies in the entanglement wedge of $R$. Operators on the partners can then, in principle, be reconstructed from the radiation, which is how $c$ can be part of $R$ without cloning. The same encoding underlies Hayden and Preskill's result: a few qubits thrown into an old hole can be recovered from the radiation after about a scrambling time, $(\beta/2\pi)\ln S_{\rm BH}$, with $\beta = 1/T_{\rm H}$.

The scope matters. The controlled calculations are in two-dimensional gravity, in anti-de Sitter space, and in braneworld models. They compute an entropy, not a mechanism saying which quanta carry which information. Extending them to asymptotically flat, four-dimensional astrophysical holes is argued but less controlled. Replica wormholes also raise puzzles about whether gravity computes averages over many quantum systems.

**Takeaway:** In specific models, adding an island to the entropy rule, justified by replica wormholes, turns Hawking's rising entropy into a Page curve; a mechanism for real black holes is still missing.

*What this leaves out:* Assumes a semiclassical limit in which the area term dominates and the bulk entropy of the matter fields can be computed reliably.

*Continues:* `ways_in/keep-the-books-with-the-page-curve`, `ways_in/one-late-quantum-cannot-serve-two-partners`<br>*Visuals:* [[page-curve-of-an-evaporating-hole]]<br>*See:* `checks/what-island-calculations-show`, `problems/hayden-preskill-return-time`, `research_horizon/islands-and-replica-wormholes`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| information | — | The details of how something started, such as which words were on a letter. For anything sealed off from everything else, the quantum rules scramble information but never destroy it. | — |
| quantum rules | — | The laws that govern atoms and light. For anything sealed off from everything else, they settle its complete description at every moment from its description at any one moment. | [[unitarity-of-quantum-evolution]] |
| horizon | — | The edge of a black hole. Nothing that crosses it, not even light, comes back out. | [[event-horizon]] |
| Hawking radiation | — | The faint glow that quantum physics predicts every black hole gives off. It carries away the hole's energy. | [[hawking-radiation]] |
| evaporation | — | The slow loss of mass of a black hole in cold surroundings, as Hawking radiation carries away its energy. | [[black-hole-evaporation]] |
| entanglement | — | A purely quantum link between particles, in which the particles together hold information that no single particle holds alone. | — |
| entropy | EN-truh-pee | A measure of how many different hidden arrangements fit what can be measured from outside. A black hole's entropy grows with the area of its horizon. | [[bekenstein-hawking-entropy]] |
| absolute zero | — | The lowest possible temperature, about 273 degrees Celsius below the freezing point of water. Temperatures here are counted up from it in degrees the size of Celsius degrees. | — |
| black-hole information problem | — | The clash between a black hole evaporating completely, with Hawking radiation that does not depend on what fell in, and the quantum rule that information is never destroyed. | [[black-hole-information-problem]] |

## Key equations

### Fine-grained (von Neumann) entropy · working

$$
S = -k_B\,\mathrm{Tr}(\rho\ln\rho)
$$

The entropy of a quantum state itself: zero for a pure state, and positive for a part that is entangled with something else.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S$ | fine-grained entropy, in joules per kelvin | the fine-grained entropy |
| $k_B$ | Boltzmann's constant | k B |
| $\rho$ | density matrix of the system, with unit trace | rho |
| $\mathrm{Tr}$ | trace over the system's states | the trace |

**Holds when:** Any quantum system with normalized density matrix, $\mathrm{Tr}\,\rho = 1$; natural logarithm.  
**Say it:** “The fine-grained entropy is minus k B times the trace of rho times the natural log of rho.”  
**Justified by:** `stated`

### Page-curve bound · working

$$
S_{\rm rad}(t) \le \min\{S_{\rm H}(t),\ S_{\rm BH}(t)\}
$$

If evaporation is unitary, the radiation's fine-grained entropy can exceed neither Hawking's value nor the black hole's Bekenstein–Hawking entropy.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $S_{\rm rad}(t)$ | fine-grained entropy of all radiation emitted by time $t$ | the radiation entropy |
| $S_{\rm H}(t)$ | the same quantity in Hawking's calculation, equal to the radiation's thermal entropy | Hawking's entropy |
| $S_{\rm BH}(t)$ | Bekenstein–Hawking entropy of the remaining hole | the black hole entropy |

**Holds when:** Pure initial state and unitary evolution; the hole has about $e^{S_{\rm BH}/k_B}$ internal states; for typical scrambling dynamics the bound is nearly saturated.  
**Say it:** “The radiation entropy is at most the smaller of Hawking's entropy and the black hole entropy.”  
**Justified by:** `unitarity-of-quantum-evolution`

### Page time for black-body emission · working

$$
t_{\rm P} = \left[1 - \left(\tfrac47\right)^{3/2}\right]\tau \approx 0.568\,\tau
$$

For ideal black-body emission, the radiation entropy must turn over after about 57 per cent of the lifetime, when the hole keeps about 76 per cent of its mass.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $t_{\rm P}$ | the Page time, measured from the formation of the hole | the Page time |
| $\tau$ | the lifetime of the hole | the lifetime |

**Holds when:** Emission as ideal black-body photons, so the radiation carries $\tfrac43$ of the entropy the hole loses; $M(t) = M_0(1 - t/\tau)^{1/3}$.  
**Say it:** “The Page time is one minus four sevenths to the power three halves, times the lifetime: about fifty-seven per cent of it.”  
**Justified by:** `derivations/page-time-from-evaporation-law`

### Hawking's pair state · formal

$$
|\Psi\rangle = \bigotimes_\omega \sqrt{1 - e^{-2\pi\omega/\kappa}}\,\sum_{n=0}^{\infty} e^{-\pi n\omega/\kappa}\,|n\rangle_{b_\omega}|n\rangle_{c_\omega}
$$

Each late outgoing packet is entangled with a partner packet behind the horizon, with thermal weights set by the surface gravity.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $b_\omega,\ c_\omega$ | outgoing packet of frequency $\omega$ at infinity, and its interior partner | the outgoing packet and its partner |
| $\kappa$ | surface gravity of the horizon, $1/4M$ for Schwarzschild | kappa, the surface gravity |
| $|n\rangle$ | state with $n$ quanta in the packet | n quanta |

**Holds when:** $G = c = \hbar = k_B = 1$; free field; late-time packets; partial reflection by the potential barrier neglected.  
**Say it:** “The state is a product over packets of a sum over n, weighted by e to the minus pi n omega over kappa, of n quanta outside paired with n quanta inside.”  
**Justified by:** `stated`

### Growth of radiation entropy under small corrections · formal

$$
S(R\cup b) \ge S(R) + S(b) - 2\,S(bc)
$$

When a nearly pure pair is created without touching the far radiation, the entropy of the radiation grows by nearly the entropy of the new outgoing quantum.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $R$ | radiation already emitted | the early radiation |
| $b,\ c$ | a newly created outgoing quantum and its interior partner | the new quantum and its partner |
| $S(X)$ | von Neumann entropy of the reduced state of $X$ | the entropy of X |

**Holds when:** $R$, $b$ and $c$ are independent subsystems, and creating the pair does not act on $R$.  
**Say it:** “The entropy of the radiation plus the new quantum is at least the old radiation entropy plus the new quantum entropy minus twice the pair entropy.”  
**Justified by:** `derivations/small-corrections-cannot-turn-the-curve`

### Island rule for the entropy of radiation · research

$$
S(R) = \min_{I}\,\operatorname*{ext}_{I}\left[\frac{\mathrm{Area}(\partial I)}{4} + S_{\rm bulk}(R\cup I)\right]
$$

The fine-grained entropy of radiation collected outside a gravitating region is the smallest extremum of a generalized entropy that may include an island inside it.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $I$ | candidate island, a region of the gravitating spacetime, possibly empty | the island |
| $\mathrm{Area}(\partial I)$ | area of the island's boundary | the area of the island boundary |
| $S_{\rm bulk}(R\cup I)$ | von Neumann entropy of the quantum fields in $R$ and $I$ | the bulk entropy of the radiation and island |

**Holds when:** $G = c = \hbar = k_B = 1$; semiclassical gravity coupled to matter, with $R$ in a non-gravitating region; established in two-dimensional, anti-de Sitter and braneworld models.  
**Say it:** “The entropy of the radiation is the minimum over islands of the extremum of the island boundary area over four plus the bulk entropy of radiation and island.”  
**Justified by:** `stated`

## Derivations

### Page time from the evaporation law · working

**Goal:** Find when Hawking's radiation entropy equals the remaining Bekenstein–Hawking entropy, for ideal black-body emission.

1. The evaporation law $dM/dt = -K/M^2$, with $K$ constant for a fixed set of emitted particles, integrates to $M(t) = M_0(1 - t/\tau)^{1/3}$, where $\tau = M_0^3/3K$.
2. Since $S_{\rm BH} = 4\pi G k_B M^2/\hbar c \propto M^2$, the hole's entropy is $S_{\rm BH}(t) = S_0(1 - t/\tau)^{2/3}$, with $S_0 = S_{\rm BH}(0)$.
3. For black-body radiation $u = aT^4$. At fixed volume $dS = dU/T = 4aVT^2\,dT$, so the entropy density is $s = \tfrac43 aT^3 = \tfrac43\,u/T$.
4. Radiation streaming out through a surface carries energy flux $cu/4$ and entropy flux $cs/4$, so entropy $\tfrac43\,dE/T$ leaves with energy $dE$.
5. The first law gives the hole's loss as $dS_{\rm BH} = -dE/T_{\rm H}$, and the radiation leaves at $T = T_{\rm H}$. So $dS_{\rm H} = -\tfrac43\,dS_{\rm BH}$, and $S_{\rm H}(t) = \tfrac43\,[S_0 - S_{\rm BH}(t)]$.
6. At the Page time $S_{\rm H} = S_{\rm BH}$, so $\tfrac43(S_0 - S_{\rm BH}) = S_{\rm BH}$, which gives $S_{\rm BH} = \tfrac47 S_0$.
7. Then $M = \sqrt{4/7}\,M_0 = 0.756\,M_0$, and $1 - t/\tau = (4/7)^{3/2} = 0.432$.

**Result:** $t_{\rm P} = [1 - (4/7)^{3/2}]\,\tau \approx 0.568\,\tau$, when $M \approx 0.756\,M_0$ and $S_{\rm BH} = \tfrac47 S_0$.

### Small corrections cannot turn the curve over · formal

**Goal:** Show that if each new pair $(b, c)$ is nearly pure, $S(bc) \le \epsilon$, and its creation does not act on the radiation $R$ already emitted, then $S(R\cup b) \ge S(R) + S(b) - 2\epsilon$.

1. The emission acts only on the hole and its surroundings, not on $R$. So the reduced state of $R$, and hence $S(R)$, is the same after the emission as before.
2. Strong subadditivity for three subsystems reads $S(XY) + S(YZ) \ge S(Y) + S(XYZ)$. With $X = R$, $Y = b$ and $Z = c$ it gives $S(Rb) \ge S(b) + S(Rbc) - S(bc)$.
3. The Araki–Lieb inequality $S(XY) \ge |S(X) - S(Y)|$, with $X = R$ and $Y = bc$, gives $S(Rbc) \ge S(R) - S(bc)$.
4. Substituting, $S(Rb) \ge S(R) + S(b) - 2S(bc) \ge S(R) + S(b) - 2\epsilon$.
5. A nearly thermal outgoing quantum has $S(b)$ of order one, for instance $\ln 2$ for one half of a maximally entangled pair of qubits. With $\epsilon \ll S(b)$, every emission raises the radiation's entropy.

**Result:** $S(R\cup b) \ge S(R) + S(b) - 2\epsilon$. While the pairs stay nearly pure and the far radiation is untouched, the radiation's entropy cannot turn over, so a Page curve requires corrections of order one at the horizon or a failure of independence.

## Problems

### `page-time-for-other-entropy-ratios` · working · difficulty 2 · calculation

How the hole's gravity filters Hawking radiation, and which particles it emits, change the ratio of entropy carried off to entropy lost. Suppose the radiation carries $\beta$ times the Bekenstein–Hawking entropy the hole loses, and the mass still obeys $M = M_0(1 - t/\tau)^{1/3}$. Find $M/M_0$ and $t_{\rm P}/\tau$ at the Page time as functions of $\beta$. Evaluate them for $\beta = 1$ and $\beta = 3/2$. How does the Page time move as $\beta$ grows?

**Hints**

1. Write $S_{\rm H} = \beta\,[S_0 - S_{\rm BH}]$ and set it equal to $S_{\rm BH}$.
2. Use $S_{\rm BH} \propto M^2 \propto (1 - t/\tau)^{2/3}$.

**Answer:** $M/M_0 = \sqrt{\beta/(1+\beta)}$ and $t_{\rm P}/\tau = 1 - [\beta/(1+\beta)]^{3/2}$. For $\beta = 1$: $M/M_0 = 0.707$ and $t_{\rm P} = 0.646\,\tau$. For $\beta = 3/2$: $M/M_0 = 0.775$ and $t_{\rm P} = 0.535\,\tau$. A larger $\beta$ brings the Page time earlier, while more of the mass remains.

**Must contain:** The Page time is where beta times the entropy lost equals the entropy left; The entropy left is beta over one plus beta of the initial entropy; For beta one the Page time is 0.646 of the lifetime; for beta three halves it is 0.535; A larger ratio makes the Page time earlier

**Numeric:** Page time over lifetime for beta 1 = 0.646 1 (magnitude, ±1%); Page time over lifetime for beta 3/2 = 0.535 1 (magnitude, ±1%)

**Solution**

1. Set $\beta(S_0 - S_{\rm BH}) = S_{\rm BH}$, so $S_{\rm BH}/S_0 = \beta/(1+\beta)$.
2. Since $S_{\rm BH} \propto M^2$, $M/M_0 = \sqrt{\beta/(1+\beta)}$.
3. Since $S_{\rm BH}/S_0 = (1 - t/\tau)^{2/3}$, $1 - t_{\rm P}/\tau = [\beta/(1+\beta)]^{3/2}$.
4. $\beta = 1$: $S_{\rm BH}/S_0 = 0.5$, $M/M_0 = 0.7071$, $t_{\rm P}/\tau = 1 - 0.3536 = 0.6464$.
5. $\beta = 3/2$: $S_{\rm BH}/S_0 = 0.6$, $M/M_0 = 0.7746$, $t_{\rm P}/\tau = 1 - 0.4648 = 0.5352$.
6. $\beta/(1+\beta)$ grows with $\beta$, so the turnover comes when the hole is heavier and earlier in its life. The black-body value $\beta = 4/3$ gives $0.568\,\tau$, between the two.

**Targets:** `only-the-final-moment`

### `entropy-of-one-hawking-mode` · formal · difficulty 2 · derivation

Units $\hbar = k_B = 1$. One outgoing packet and its partner are in the state $\sqrt{1-x}\,\sum_n x^{n/2}|n\rangle_b|n\rangle_c$, with $x = e^{-2\pi\omega/\kappa}$. (a) Find the reduced state $\rho_b$. (b) Show that its von Neumann entropy is $S = -\ln(1-x) - x\ln x/(1-x)$. (c) Show that this equals the thermodynamic entropy of an oscillator of frequency $\omega$ at $T = \kappa/2\pi$. (d) Evaluate $S$ for $\omega = \kappa/2\pi$.

**Hints**

1. The partner states $|n\rangle_c$ are orthonormal, so the trace over $c$ removes all off-diagonal terms.
2. Use $\sum_n n\,p_n = x/(1-x)$ for $p_n = (1-x)x^n$.
3. For the oscillator, $Z = 1/(1-x)$ and $S = (E - F)/T$.

**Answer:** (a) $\rho_b = (1-x)\sum_n x^n|n\rangle\langle n|$, thermal. (b) $S = -\ln(1-x) - x\ln x/(1-x)$. (c) The same expression follows from $Z = 1/(1-x)$ with $x = e^{-\omega/T}$ and $T = \kappa/2\pi$. (d) With $x = e^{-1}$, $S = 0.459 + 0.582 = 1.041$.

**Must contain:** Tracing out the partner leaves a diagonal thermal state; The entropy equals the thermal entropy of a bosonic oscillator; The temperature is kappa over two pi; For omega equal to kappa over two pi the entropy is about 1.04

**Numeric:** entropy of the packet = 1.0407 1 (magnitude, ±0.5%)

**Solution**

1. $\rho_b = \mathrm{Tr}_c|\psi\rangle\langle\psi| = (1-x)\sum_{n,m} x^{(n+m)/2}|n\rangle\langle m|\,\langle m|n\rangle_c = (1-x)\sum_n x^n|n\rangle\langle n|$.
2. The eigenvalues are $p_n = (1-x)x^n$, which sum to one.
3. $S = -\sum_n p_n\ln p_n = -\ln(1-x) - \ln x\sum_n n\,p_n = -\ln(1-x) - x\ln x/(1-x)$.
4. For an oscillator at temperature $T$, $Z = \sum_n e^{-n\omega/T} = 1/(1-x)$ with $x = e^{-\omega/T}$, so $F = T\ln(1-x)$ and $E = \omega x/(1-x)$.
5. $S = (E - F)/T = (\omega/T)\,x/(1-x) - \ln(1-x)$, and $\omega/T = -\ln x$, which reproduces (b). Matching $x$ requires $T = \kappa/2\pi$, the Hawking temperature.
6. For $\omega = \kappa/2\pi$, $x = e^{-1}$: $-\ln(1 - e^{-1}) = 0.4587$ and $e^{-1}/(1 - e^{-1}) = 0.5820$, so $S = 1.0407$.

**Targets:** `thermal-means-lost`

### `which-assumption-each-proposal-gives-up` · formal · difficulty 2 · conceptual

Using the assumptions (U) unitarity, (E) effective field theory on nice slices and at the horizon, (L) independent subsystems with emissions that leave the far radiation untouched, and (R) nothing left after evaporation, say which assumption each proposal gives up: (a) information loss with a mixed final state; (b) long-lived Planck-mass remnants; (c) firewalls; (d) fuzzballs, in which horizon-scale structure replaces the smooth interior; (e) islands, with the interior encoded in the radiation after the Page time.

**Hints**

1. Ask of each proposal whether the final state is pure, whether something is left, and whether an infalling observer notices the horizon.

**Answer:** (a) gives up (U). (b) gives up (R). (c) gives up (E) at the horizon of an old hole. (d) gives up (E): the geometry differs at the horizon scale by order-one amounts. (e) gives up the independence in (L): after the Page time the interior partners are not a system separate from the early radiation.

**Must contain:** Information loss drops unitarity; Remnants drop complete evaporation; Firewalls and fuzzballs drop the smooth horizon described by effective field theory; Islands drop the independence of interior and radiation

**Solution**

1. Information loss keeps the semiclassical picture to the end and accepts a mixed final state, so it gives up (U).
2. A remnant keeps (U), (E) and (L) by leaving an object entangled with all the radiation, so it gives up (R).
3. A firewall keeps unitarity and complete evaporation, and puts order-one excitations at the horizon of an old hole, so it gives up (E) there.
4. Fuzzballs replace the horizon and interior by horizon-sized structure with order-one departures from the smooth geometry, which also gives up (E).
5. The island picture keeps a smooth horizon in the semiclassical geometry and a unitary Page curve. Its entropy rule counts the interior partners inside the island as part of the radiation, which denies that they are independent subsystems, so it gives up that part of (L).

**Targets:** `tiny-leftover-holds-it`

### `hayden-preskill-return-time` · research · difficulty 1 · estimate

A black hole of one solar mass, $1.989\times10^{30}$ kg, is past its Page time. Alice throws a diary of a few qubits into it, and Bob already holds the early radiation. Take the time for the hole to scramble the diary to be $t_* = (\hbar/2\pi k_B T_{\rm H})\ln(S_{\rm BH}/k_B)$, with $T_{\rm H} = \hbar c^3/8\pi G M k_B$. Estimate $t_*$, and compare it with the Page time of about $1.2\times10^{67}$ years that the black-body bookkeeping gives for this hole.

**Hints**

1. Show that $\hbar/2\pi k_B T_{\rm H} = 4GM/c^3$.
2. Use $S_{\rm BH}/k_B = 4\pi GM^2/\hbar c$.

**Answer:** $4GM/c^3 = 1.97\times10^{-5}$ s and $\ln(S_{\rm BH}/k_B) = \ln(1.05\times10^{77}) = 177$, so $t_* \approx 3.5$ ms. Past the Page time the hole returns the diary's information to the radiation within milliseconds, an utterly short time compared with its $10^{67}$-year history: it acts like a mirror, though decoding requires the early radiation and a quantum computation.

**Must contain:** h bar over two pi k B T H equals 4GM over c cubed, about 20 microseconds; The logarithm of the entropy is about 177; The scrambling time is about 3.5 milliseconds; Only the order of magnitude is meaningful

**Numeric:** scrambling time = 3.49 ms (magnitude, ±5%)

**Solution**

1. $T_{\rm H} = \hbar c^3/8\pi GMk_B$, so $\hbar/2\pi k_B T_{\rm H} = 8\pi GM/2\pi c^3 = 4GM/c^3$.
2. $4GM/c^3 = 4 \times 6.674\times10^{-11} \times 1.989\times10^{30}/(2.998\times10^8)^3 = 1.970\times10^{-5}$ s.
3. $S_{\rm BH}/k_B = 4\pi GM^2/\hbar c = 1.049\times10^{77}$, and its natural logarithm is $177.3$.
4. $t_* = 1.970\times10^{-5}\ \text{s} \times 177.3 = 3.49\times10^{-3}$ s.
5. The coefficient of $t_*$ is model-dependent, so the meaningful statement is "milliseconds", set by the light-crossing time times the logarithm of the entropy. Compared with $1.2\times10^{67}$ years this return is immediate.

## Observations

- **The temperature of the cosmic microwave background** (measured, working). A black hole whose Hawking temperature is below the microwave background's absorbs more radiation than it emits, and grows. That holds for every hole heavier than about $4.5\times10^{22}$ kg, some 0.6 of the Moon's mass, which includes every black hole observed. Evaporation, and with it the information problem, cannot yet be tested with astrophysical black holes. *Numbers:* $T_{\rm CMB} = 2.72548 \pm 0.00057$ K; $T_{\rm H} = 6.17\times10^{-8}$ K for one solar mass, a ratio of $4.4\times10^{7}$. *Reference:* D. J. Fixsen (2009), *The Temperature of the Cosmic Microwave Background*, The Astrophysical Journal 707, 916–920, doi:10.1088/0004-637X/707/2/916
- **Entangled Hawking and partner phonons at a sonic horizon** (analogue, formal). In a flowing Bose–Einstein condensate of rubidium atoms, the flow turns supersonic, so sound plays the role of light and the sonic horizon the role of the event horizon. Correlations measured between phonons on the two sides were consistent with entanglement between Hawking phonons and their partners, the pairing at the root of the information problem. No gravity is involved, so this tests the pair-creation mechanism, not the fate of information in a black hole. *Reference:* Jeff Steinhauer (2016), *Observation of quantum Hawking radiation and its entanglement in an analogue black hole*, Nature Physics 12, 959–965, doi:10.1038/nphys3863
- **Verified information scrambling on a trapped-ion quantum computer** (analogue, research). A teleportation protocol modelled on the Hayden–Preskill thought experiment distinguished scrambling, which spreads information into many-body correlations where it can still be recovered, from decoherence, which leaks it away. It illustrates the recovery step of the information problem on a few qubits; no gravity is involved. *Reference:* Kevin A. Landsman, Caroline Figgatt, Thomas Schuster, Norbert M. Linke, Beni Yoshida, Norman Y. Yao, Christopher Monroe (2019), *Verified quantum information scrambling*, Nature 567, 61–65, doi:10.1038/s41586-019-0952-6

## Teaching arc

1. **Ask where a burned letter's words go** (entry). Ask whether burning destroys a letter's words, then settle it with the word rules of the try-it. *Why:* It fixes what "information is never destroyed" means before any black hole appears. *Predict:* If you burn a letter, are its words gone for good? *Uses:* `checks/burning-a-letter`, `ways_in/throw-a-letter-into-a-black-hole`
2. **Compare a library hole with a rock hole** (entry). Pose the two matching holes, then reveal that their Hawking radiation and total energy are the same. *Why:* It separates the information account from the energy account. *Predict:* Could the Hawking radiation tell you which hole held the library? *Visual:* [[library-hole-and-rock-hole]] *Uses:* `checks/letter-and-rocks`
3. **Say why no one can watch it** (entry). Compare the Sun-mass hole's temperature with the microwaves that fill space. *Why:* It answers the natural "why not just look?" with a number. *Uses:* `checks/sun-mass-hole-in-space-microwaves`
4. **Keep the entropy books** (working). Build the two entropy curves, find their crossing, and give a solar-mass hole's horizon size there. *Why:* It shows the conflict begins while the hole is large. *Predict:* When must the radiation's entanglement start to fall: at the very end, or much sooner? *Visual:* [[page-curve-of-an-evaporating-hole]] *Uses:* `ways_in/keep-the-books-with-the-page-curve`, `derivations/page-time-from-evaporation-law`, `checks/page-time-hole-is-still-big`
5. **State the conflict precisely** (formal). Trace out Hawking's partners, then run the entropy inequality that lists the assumptions that cannot all hold. *Why:* It replaces a slogan with explicit hypotheses. *Visual:* [[pairs-on-a-nice-slice]] *Uses:* `ways_in/pairs-across-the-horizon`, `problems/entropy-of-one-hawking-mode`, `derivations/small-corrections-cannot-turn-the-curve`
6. **Run the firewall argument** (formal). Pose the old-hole monogamy argument, then sort the proposed resolutions by the assumption each drops. *Why:* It shows why complementarity was not the end of the story. *Predict:* Can one late quantum be fully entangled with both its interior partner and the early radiation? *Visual:* [[one-late-quantum-two-partners]] *Uses:* `ways_in/one-late-quantum-cannot-serve-two-partners`, `checks/monogamy-for-an-old-black-hole`, `problems/which-assumption-each-proposal-gives-up`
7. **Compute the Page curve, with its scope** (research). Show how the island branch turns Hawking's curve over, then ask what the calculation does not establish. *Why:* It links the modern result to the puzzle without overclaiming. *Visual:* [[page-curve-of-an-evaporating-hole]] *Uses:* `ways_in/islands-compute-the-page-curve`, `checks/what-island-calculations-show`

## Analogies

### A secret split into shares · working

A secret-sharing scheme splits a message into many shares, so that any group of shares below a threshold reveals nothing, while any group above it recovers the whole message. Quantum versions exist, and the no-cloning theorem forces their threshold above half of the shares. Radiation from a unitarily evaporating hole is expected to behave similarly, with the Page time as the threshold: small collections of quanta look thermal, and the information appears in correlations once more than about half of the entropy has been collected.

| In the analogy | Stands for |
| --- | --- |
| the shares | the emitted quanta of Hawking radiation |
| the threshold | the Page time |
| the encoding of the message | the black hole's scrambling dynamics |

*Limits:* A scheme is designed and has a sharp threshold; a black hole is only expected to act like a typical scrambler, and its turnover is smooth. The analogy says nothing about the interior partners or the horizon.

## Misconceptions

### “The problem is that the energy of whatever fell in disappears.” · entry · `energy-goes-missing`

- **Why it is tempting:** People hear that something is destroyed and assume it is the stuff itself.
- **What is true:** A hole that evaporates completely sends out all of its energy as Hawking radiation. What seems to vanish is the information, such as which words were on a letter.
- **Exposed by:** `checks/letter-and-rocks`

### “Burning a letter destroys its words too, so a black hole is nothing special.” · entry · `burning-destroys-too`

- **Why it is tempting:** Nobody can rebuild a burned letter in practice.
- **What is true:** Burning only scrambles the words into smoke, ash, heat and light, where they could in principle be traced back. In the simplest calculation, Hawking radiation keeps no such trace.
- **Exposed by:** `checks/burning-a-letter`

### “Astronomers could settle this by watching a black hole evaporate.” · entry · `watch-one-evaporate`

- **Why it is tempting:** Black holes are observed, and evaporation is a clear prediction.
- **What is true:** Every black hole found so far is far colder than the microwaves that fill space, so it takes in more than it gives off and grows. Heavier holes are even colder.
- **Exposed by:** `checks/sun-mass-hole-in-space-microwaves`

### “The trouble only starts at the very end, when the hole is tiny and quantum gravity takes over.” · working · `only-the-final-moment`

- **Why it is tempting:** Semiclassical physics really does fail near the Planck mass.
- **What is true:** If evaporation is unitary, the radiation's entanglement entropy must start falling at the Page time, when a solar-mass hole is still kilometres across. A fix at the end would come far too late.
- **Exposed by:** `checks/page-time-hole-is-still-big`

### “If the radiation has an exactly thermal spectrum, it cannot carry any information.” · formal · `thermal-means-lost`

- **Why it is tempting:** Hawking's calculation gives thermal radiation and loses the information.
- **What is true:** A small part of a random pure state looks almost exactly thermal, so thermal-looking early radiation is expected even under unitarity. The information sits in correlations among many quanta.
- **Exposed by:** `checks/thermal-spectrum-is-not-proof`

### “The information can simply be both inside with the partners and outside in the radiation.” · formal · `information-in-two-places`

- **Why it is tempting:** Complementarity is often summarized as information being in two places at once.
- **What is true:** No-cloning forbids two independent copies, and a late quantum fully entangled with its partner cannot also purify the early radiation. Keeping both requires the partner to be encoded in the radiation.
- **Exposed by:** `checks/monogamy-for-an-old-black-hole`

### “A Planck-mass remnant can easily store the information at the end.” · formal · `tiny-leftover-holds-it`

- **Why it is tempting:** A leftover object seems like the least dramatic change to the story.
- **What is true:** For a hole that starts with the Sun's mass, the remnant would need an entropy whose size in units of Boltzmann's constant has 78 digits, while a black hole of that tiny mass has about 12.6. Such crowded states raise the worry that remnants would be produced copiously.
- **Exposed by:** `checks/planck-mass-remnant-states`

### “Replica wormholes solved the information problem for real black holes.” · research · `solved-in-2019`

- **Why it is tempting:** The island results were widely reported as resolving the paradox.
- **What is true:** They compute a Page curve for the radiation's entropy in specific models. They give no mechanism for which quanta carry the information and no controlled treatment of astrophysical holes.
- **Exposed by:** `checks/what-island-calculations-show`

## Checks

1. **Entry · predict** `checks/letter-and-rocks`. Picture two black holes with the same mass, spin and electric charge. One formed when a library as heavy as a star collapsed, and the other when plain rock collapsed. In the simplest calculation, both evaporate completely by giving off Hawking radiation. Could you tell from the Hawking radiation which hole held the library? Does either hole send out more energy in total?
   - **Hints:** Which three numbers does Hawking radiation depend on in the simplest calculation? / Where does the energy of each hole end up?
   - **Answer:** No, and no. In the simplest calculation, Hawking radiation depends only on the hole's mass, spin and electric charge. The holes match in those three numbers, so they give off the same kind of Hawking radiation. Energy has mass, so each hole's total energy is set by its mass. Each hole evaporates completely, so it sends out all of that energy, and both started with the same mass. What seems to go missing is not energy but information: which books, and which words.
   - **Must contain:** The Hawking radiation cannot tell the holes apart; Both send out the same total energy; What seems lost is information, not energy
   - **Targets:** `energy-goes-missing`
   - **Visual:** [[library-hole-and-rock-hole]]
2. **Entry · explain** `checks/burning-a-letter`. You burn a letter in a fireplace. According to the quantum rules, where is the information about its words now? Then explain what is different if the letter falls into a black hole that evaporates completely.
   - **Hints:** Would two different letters leave exactly the same smoke and light?
   - **Answer:** The information is spread through the smoke, ash, heat and light. Every different letter leaves those arranged a little differently, so someone who tracked every piece could work back to the words. That is impossible in practice, but the information still exists. The black hole is different because, in the simplest calculation, its Hawking radiation is the same whatever fell in. So the information is not in the Hawking radiation. The hole evaporates completely, so nothing is left to hold the information either. It therefore seems destroyed, which the quantum rules forbid.
   - **Must contain:** Burning scrambles the information into smoke, ash, heat and light; Hawking radiation in the simplest calculation does not depend on what fell in; With nothing left, the information seems destroyed
   - **Targets:** `burning-destroys-too`
3. **Entry · numeric** `checks/sun-mass-hole-in-space-microwaves`. A black hole with the Sun's mass glows at about 60 billionths of a degree above absolute zero. The faint microwaves that fill space are about 2.7 degrees above absolute zero. How many times warmer are the microwaves than the hole? Can astronomers watch such a hole evaporate today?
   - **Hints:** Divide the warmer temperature by the colder one. / Does something colder than its surroundings warm up or cool down?
   - **Answer:** 2.7 degrees divided by 60 billionths of a degree is 45 million, so the microwaves are about 45 million times warmer. Something colder than its surroundings takes in more warmth than it gives off, like a cold drink in a warm room. So the hole takes in more energy from the microwaves than it gives off in Hawking radiation, and it grows instead of shrinking. Nobody can watch it evaporate today.
   - **Must contain:** The microwaves are about 45 million times warmer; The hole takes in more than it gives off; So it grows and cannot be watched evaporating
   - **Numeric:** how many times warmer the microwaves are = 4.5e+07 1 (magnitude, ±10%)
   - **Targets:** `watch-one-evaporate`
4. **Working · evaluate-claim** `checks/page-time-hole-is-still-big`. Claim: "The information problem only matters in the last instant, when the hole is Planck-sized and quantum gravity takes over." For a hole that starts with one solar mass, $1.989\times10^{30}$ kg, the black-body bookkeeping puts the Page time at $M = 0.756\,M_0$. Find the horizon radius at that moment, and use it to evaluate the claim.
   - **Hints:** Use $r = 2GM/c^2$ with $M = 0.756\,M_\odot$. / Which curve does the radiation entropy follow after the Page time?
   - **Answer:** The horizon radius is $2GM/c^2 = 2 \times 6.674\times10^{-11} \times 0.756 \times 1.989\times10^{30}/(2.998\times10^8)^2 = 2.23$ km. The claim is false. Unitarity requires the radiation's fine-grained entropy to start falling at the Page time, because it cannot exceed the shrinking $S_{\rm BH}$. The curvature radius near a 2.23 km horizon is about a kilometre, some $10^{38}$ Planck lengths, so semiclassical physics should be excellent there, yet it must already disagree with Hawking's result.
   - **Must contain:** Horizon radius about 2.23 km at the Page time; The entanglement entropy must already be falling then; Curvature there is far below the Planck scale, so the claim fails
   - **Numeric:** horizon radius at the Page time = 2.23 km (magnitude, ±2%)
   - **Targets:** `only-the-final-moment`
   - **Visual:** [[page-curve-of-an-evaporating-hole]]
5. **Formal · evaluate-claim** `checks/thermal-spectrum-is-not-proof`. Claim: "Radiation caught before the Page time is exactly thermal quantum by quantum, so the information must be lost." Evaluate it using the average entropy $\langle S\rangle \approx \ln m - m/2n$ of a subsystem of dimension $m$ in a random pure state of dimension $mn$, with $1 \ll m \le n$. As a test, take 3 qubits out of 10 and compare with the maximum $\ln m$.
   - **Hints:** What are $m$ and $n$ for 3 qubits out of 10?
   - **Answer:** For 3 of 10 qubits, $m = 8$ and $n = 128$, so $\langle S\rangle \approx \ln 8 - 8/256 = 2.048$, against the maximum $\ln 8 = 2.079$: 98.5 per cent. A small part of a pure state is almost maximally mixed, so it looks thermal although the whole holds all the information. Early radiation from a unitary hole should therefore look thermal, with the information in correlations among many quanta, and the claim fails.
   - **Must contain:** Three of ten qubits reach 98.5 per cent of maximal entropy; Small parts of pure states look thermal; The information is in multi-quantum correlations, so early thermality proves nothing
   - **Numeric:** average entropy of 3 qubits out of 10 = 2.048 1 (magnitude, ±0.5%)
   - **Targets:** `thermal-means-lost`
6. **Formal · derive** `checks/monogamy-for-an-old-black-hole`. An old black hole is past its Page time. Let $R$ be the early radiation, $b$ a late outgoing quantum and $c$ its interior partner. The Page curve requires $S(Rb) < S(R)$. A smooth horizon requires $bc$ to be in a pure entangled state. Show that these cannot both hold, and explain why putting the information both in $c$ and in $R$ does not help.
   - **Hints:** What does a pure state of $bc$ imply about correlations between $bc$ and $R$?
   - **Answer:** If $bc$ is pure, the state factorizes as $\rho_{Rbc} = \rho_R\otimes|\psi\rangle\langle\psi|_{bc}$. Tracing out $c$ gives $\rho_{Rb} = \rho_R\otimes\rho_b$, so $S(Rb) = S(R) + S(b)$. Because $b$ is entangled with $c$, $S(b) > 0$, so $S(Rb) > S(R)$, contradicting the Page curve. Independent copies of the information in $c$ and in $R$ are forbidden by no-cloning, and monogamy stops $b$ being maximally entangled with both. The way out is a firewall, or a partner $c$ that is not independent of $R$.
   - **Must contain:** A pure bc factorizes from R; Then S of R b exceeds S of R; No-cloning and monogamy forbid the information in two independent places
   - **Targets:** `information-in-two-places`
   - **Visual:** [[one-late-quantum-two-partners]]
7. **Formal · numeric** `checks/planck-mass-remnant-states`. A solar-mass black hole evaporates as Hawking's calculation says until it reaches the Planck mass, $2.18\times10^{-8}$ kg, then stops, leaving a remnant that must purify all the radiation. In the black-body model the radiation's entropy is then $\tfrac43 S_{\rm BH}(0)$, with $S_{\rm BH}(0) = 1.05\times10^{77}\,k_B$. How large must the remnant's entropy be, in units of $k_B$? Compare it with $S_{\rm BH}$ of a Planck-mass hole.
   - **Hints:** For a pure total state, a subsystem and its complement have equal entropy. / Substitute $m_P^2 = \hbar c/G$ into $S_{\rm BH}$.
   - **Answer:** The whole state is pure, so the remnant's entropy equals the radiation's: $\tfrac43 \times 1.05\times10^{77} = 1.40\times10^{77}\,k_B$. A hole of Planck mass $m_P = \sqrt{\hbar c/G}$ has $S_{\rm BH} = 4\pi G m_P^2/\hbar c = 4\pi k_B \approx 12.6\,k_B$. The remnant would need at least $e^{1.4\times10^{77}}$ internal states in about 22 micrograms. So many states at fixed small mass raise the worry that remnants would be produced copiously, so remnants are strongly constrained, though not ruled out.
   - **Must contain:** Remnant entropy at least 1.4 times ten to the 77 k B; A Planck-mass hole has entropy 4 pi k B, about 12.6; The mismatch is why remnants are strongly constrained
   - **Numeric:** minimum remnant entropy in units of k B = 1.4e+77 1 (magnitude, ±2%); entropy of a Planck-mass hole in units of k B = 12.57 1 (magnitude, ±1%)
   - **Targets:** `tiny-leftover-holds-it`
8. **Research · evaluate-claim** `checks/what-island-calculations-show`. Claim: "Replica-wormhole calculations proved that real astrophysical black holes release their information, and showed which Hawking quanta carry it." Evaluate it.
   - **Hints:** What quantity do the calculations compute, and in which spacetimes?
   - **Answer:** The claim overreaches. The calculations compute the fine-grained entropy of the radiation from the gravitational path integral in specific models: two-dimensional gravity with a bath, anti-de Sitter holes with transparent boundaries, and braneworlds. Because replica wormholes add an island branch, the entropy follows a Page curve, as unitarity requires, and the interior lies in the entanglement wedge of the radiation after the Page time. They do not say which quanta carry which information, they do not control asymptotically flat four-dimensional astrophysical holes, and nothing has been observed.
   - **Must contain:** They compute an entropy in specific models and find a Page curve; They imply the interior is encoded in the radiation after the Page time; They give no microscopic mechanism and no controlled treatment of astrophysical holes
   - **Targets:** `solved-in-2019`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| Units of entropy | Working rung: entropies in joules per kelvin with $k_B$ explicit, $S = -k_B\,\mathrm{Tr}(\rho\ln\rho)$ and $S_{\rm BH} = k_B c^3 A/4G\hbar$. Formal and research rungs set $G = c = \hbar = k_B = 1$ and say so, so entropies are pure numbers and $S_{\rm BH} = A/4$. | Some texts quote entropy in bits, using base-2 logarithms (divide by $\ln 2$), and many keep $G$ explicit and write $A/4G$. |
| Which entropy of the radiation is meant | The Page curve is the fine-grained entropy of the radiation; the coarse-grained entropy is the thermodynamic one, which keeps rising. | "Entanglement entropy", "von Neumann entropy" and "fine-grained entropy" name the same quantity, and some discussions say "radiation entropy" without saying which kind. |

## Visuals

- ★ [[library-hole-and-rock-hole]] (flagship): Entry picture: two holes with matching mass give off the same Hawking radiation and evaporate, with separate tallies for energy and information. *Sketch:* Two holes side by side, one formed from a collapsing library and one from rock, with equal mass, spin and electric charge. Both emit identical Hawking radiation; spectrum readouts overlay exactly. An energy tally balances for both; an information tally shows which books went in and nothing matching coming out. A final switch shows the three ways out: faint links drawn between emitted pieces, a tiny leftover, or a broken tally.
- [[page-curve-of-an-evaporating-hole]] (core): The entropy bookkeeping: Hawking curve, black-hole entropy and the Page curve. *Sketch:* Entropy against time as a fraction of the lifetime: $S_{\rm BH}$ falling as $(1-t/\tau)^{2/3}$, Hawking's entropy rising as $\beta$ times the entropy lost, and the Page curve as their minimum. Sliders for $\beta$ from 1 to 1.6 and the starting mass; readouts for the Page time, the mass fraction and the horizon radius there. A research overlay labels the no-island and island branches.
- [[pairs-on-a-nice-slice]] (core): Where the partners live and why the final state is mixed. *Sketch:* Penrose diagram of collapse and complete evaporation. Outgoing quanta and their interior partners are linked dots; a draggable nice slice crosses the horizon far from the singularity, and a counter shows how many links the horizon cuts. After evaporation the slice meets only outside dots whose links end nowhere.
- [[one-late-quantum-two-partners]] (supporting): The monogamy argument for an old black hole. *Sketch:* Three discs for $R$, $b$ and $c$ with entropy readouts. A slider shares $b$'s entanglement between $c$ and $R$; readouts of $S(bc)$ and $S(Rb) - S(R)$ show that the first cannot be zero while the second is negative.

## Tutor moves

**Open with**

- Picture burning a secret letter in a fireplace. Are its words destroyed forever, or only scrambled so badly that nobody could ever read them in practice? *(reflection)*
- Imagine two black holes with the same mass, spin and electric charge, one made from a crushed library and one from crushed rock. When both evaporate completely, could their Hawking radiation, in the simplest calculation, tell you which one held the books? *(prediction)*

**If the learner is stuck**

- *The learner thinks the puzzle is about lost mass or energy.* → Use the library and rock holes: the same energy comes out of both, but different books went in. *Uses:* `checks/letter-and-rocks`
- *The learner cannot see how the radiation's entropy can fall.* → Use two spins in a pure pair: the pair has $S = 0$, each spin has $k_B\ln 2$. The Page curve falls for the same reason once the radiation is most of the system. *Uses:* `ways_in/keep-the-books-with-the-page-curve`, `key_equations/fine-grained-entropy`
- *The learner is lost in the entropy inequalities.* → Draw $R$, $b$ and $c$ as three discs and do the exactly pure $bc$ case first, where $S(Rb) = S(R) + S(b)$ by factorization. *Uses:* `checks/monogamy-for-an-old-black-hole`, `derivations/small-corrections-cannot-turn-the-curve`

**Common questions**

- *Could the information just stay inside the black hole forever?* (entry) Only if something is left behind. If the hole evaporates completely, no inside is left. A tiny leftover would have to hold the information about everything that ever fell in, which many physicists doubt. *Uses:* `checks/planck-mass-remnant-states`
- *Has anyone solved it?* (entry) Not completely. Since 2019, calculations in simplified model universes have found strong signs that the information comes out in the Hawking radiation, as the quantum rules require. They do not show how, and nobody has done it for a real black hole. *Uses:* `ways_in/islands-compute-the-page-curve`, `checks/what-island-calculations-show`
- *Doesn't the second law forbid the radiation's entropy from falling?* (working) The second law concerns coarse-grained entropy, and that does keep rising: in the black-body model the radiation ends with $\tfrac43 S_{\rm BH}(0)$ of it. The Page curve tracks fine-grained entropy, which for a part of a pure whole measures entanglement with the rest, and it falls once the radiation becomes most of the system. *Uses:* `ways_in/keep-the-books-with-the-page-curve`, `key_equations/page-curve-bound`
- *Why cannot quantum gravity at the Planck-scale end repair everything?* (formal) Because the radiation's fine-grained entropy must already fall from the Page time, when a solar-mass hole is kilometres across. A fix at the end must either purify about $1.4\times10^{77}$ units of entanglement with a Planck-mass object or accept a mixed final state. *Uses:* `checks/page-time-hole-is-still-big`, `checks/planck-mass-remnant-states`

**Switching levels**

- To working when: asks when the problem starts; asks what the entropy of the radiation means. Build the Page curve bookkeeping, then the horizon-size check. *Uses:* `ways_in/keep-the-books-with-the-page-curve`, `checks/page-time-hole-is-still-big`
- To formal when: is comfortable with density matrices; asks why Planck-scale physics cannot fix it. Trace out the partner packets, then run the entropy inequalities. *Uses:* `ways_in/pairs-across-the-horizon`, `derivations/small-corrections-cannot-turn-the-curve`
- To research when: asks about firewalls, islands or replica wormholes. Open the island calculation, then the research horizon. *Uses:* `ways_in/islands-compute-the-page-curve`, `research_horizon/islands-and-replica-wormholes`

**Pronunciations:** Bekenstein → BEK-en-stine; von Neumann → fon NOY-mahn; Araki–Lieb → ah-RAH-kee LEEB; Maldacena → mahl-dah-SAY-nah; Polchinski → pol-CHIN-skee

**Voice notes:** After the entry way names it, always say "information", never "details". Read entropies in units of Boltzmann's constant as "k B".

## History

- **Stephen W. Hawking (1975).** Showed that a black hole formed by collapse emits thermal radiation at a temperature set by its surface gravity, so that it evaporates. Stephen W. Hawking (1975), *Particle creation by black holes*, Communications in Mathematical Physics 43, 199–220, doi:10.1007/BF02345020
- **Stephen W. Hawking (1976).** Argued that complete evaporation turns a pure state into a mixed one, so that gravitational collapse would replace unitary scattering with a map on density matrices. Stephen W. Hawking (1976), *Breakdown of predictability in gravitational collapse*, Physical Review D 14, 2460–2473, doi:10.1103/PhysRevD.14.2460
- **Don N. Page (1993).** Used the average entropy of subsystems of random pure states to show that radiation from a unitarily evaporating hole reveals almost no information until roughly half of the entropy has been radiated; the rise and fall is now called the Page curve. Don N. Page (1993), *Information in black hole radiation*, Physical Review Letters 71, 3743–3746, doi:10.1103/PhysRevLett.71.3743
- **Leonard Susskind, Lárus Thorlacius, John Uglum (1993).** Proposed black-hole complementarity: information is absorbed at a stretched horizon and re-emitted for outside observers, and crosses the horizon unharmed for infalling ones, with no observer able to see both. Leonard Susskind, Lárus Thorlacius, John Uglum (1993), *The stretched horizon and black hole complementarity*, Physical Review D 48, 3743–3761, doi:10.1103/PhysRevD.48.3743
- **Ahmed Almheiri, Donald Marolf, Joseph Polchinski, James Sully (2012).** Argued that unitarity, effective field theory outside the horizon, and a smooth horizon for infalling observers cannot all hold for an old black hole, and proposed a firewall as the most conservative resolution. Ahmed Almheiri, Donald Marolf, Joseph Polchinski, James Sully (2013), *Black holes: complementarity or firewalls?*, Journal of High Energy Physics 2013(2), 062, doi:10.1007/JHEP02(2013)062
- **Geoff Penington, Ahmed Almheiri, Netta Engelhardt, Donald Marolf, Henry Maxfield (2019).** Showed, in two independent papers, that quantum extremal surfaces give the entropy of radiation extracted from an evaporating black hole a Page curve, and that the interior becomes encoded in the radiation after the Page time. Geoff Penington (2020), *Entanglement wedge reconstruction and the information paradox*, Journal of High Energy Physics 2020(9), 002, doi:10.1007/JHEP09(2020)002

## Research horizon

- **Islands and replica wormholes.** Quantum extremal surfaces with islands reproduce the Page curve in models where radiation is extracted into a bath, and replica wormholes in the gravitational path integral justify the rule. Open questions include asymptotically flat holes, the role of ensemble averaging, and how the encoding works dynamically. Ahmed Almheiri, Netta Engelhardt, Donald Marolf, Henry Maxfield (2019), *The entropy of bulk quantum fields and the entanglement wedge of an evaporating black hole*, Journal of High Energy Physics 2019(12), 063, doi:10.1007/JHEP12(2019)063; Ahmed Almheiri, Raghu Mahajan, Juan Maldacena, Ying Zhao (2020), *The Page curve of Hawking radiation from semiclassical geometry*, Journal of High Energy Physics 2020(3), 149, doi:10.1007/JHEP03(2020)149; Ahmed Almheiri, Thomas Hartman, Juan Maldacena, Edgar Shaghoulian, Amirhossein Tajdini (2021), *The entropy of Hawking radiation*, Reviews of Modern Physics 93, 035002, doi:10.1103/RevModPhys.93.035002
- **Firewalls and reconstructing the interior.** The firewall argument sharpened the question of how an old black hole's interior can be described at all. Responses include computational limits on decoding the radiation, ER = EPR, and state-dependent interior operators. Daniel Harlow (2016), *Jerusalem lectures on black holes and quantum information*, Reviews of Modern Physics 88, 015002, doi:10.1103/RevModPhys.88.015002; Juan Maldacena, Leonard Susskind (2013), *Cool horizons for entangled black holes*, Fortschritte der Physik 61, 781–811, doi:10.1002/prop.201300020
- **Scrambling and information recovery.** Past the Page time, information thrown into a black hole returns in the radiation after about a scrambling time, logarithmic in the entropy. Black holes are conjectured to be the fastest scramblers in nature, a link to quantum chaos. Patrick Hayden, John Preskill (2007), *Black holes as mirrors: quantum information in random subsystems*, Journal of High Energy Physics 2007(9), 120, doi:10.1088/1126-6708/2007/09/120; Yasuhiro Sekino, Leonard Susskind (2008), *Fast scramblers*, Journal of High Energy Physics 2008(10), 065, doi:10.1088/1126-6708/2008/10/065
- **Microstates and fuzzballs.** String theory counts the Bekenstein–Hawking entropy of certain extremal black holes as microstates, supporting the assumption that the hole has about that many internal states. The fuzzball proposal replaces the horizon with horizon-sized microstate geometries that radiate information directly. Andrew Strominger, Cumrun Vafa (1996), *Microscopic origin of the Bekenstein-Hawking entropy*, Physics Letters B 379, 99–104, doi:10.1016/0370-2693(96)00345-0; Samir D. Mathur (2005), *The fuzzball proposal for black holes: an elementary review*, Fortschritte der Physik 53, 793–827, doi:10.1002/prop.200410203
- **Information loss as an option.** Hawking's proposal replaces unitary evolution with a map from pure to mixed states. Generic laws of that kind were argued to violate energy conservation or locality, although whether every form of information loss must do so is still debated. Tom Banks, Michael E. Peskin, Leonard Susskind (1984), *Difficulties for the evolution of pure states into mixed states*, Nuclear Physics B 244, 125–134, doi:10.1016/0550-3213(84)90184-6

## Review: novice

**Verdict:** fixed (2026-09-13, revision 3)

**Retell attempt:** If you burn a letter, the quantum rules say the words are not really gone, just scrambled into smoke and light, and someone could in theory work them back out. A black hole gives off Hawking radiation and slowly shrinks. That radiation only depends on a few numbers like the mass, so a hole made of letters and a hole made of rocks glow the same, and once the hole is gone the information about the letters seems gone, which the rules do not allow. Maybe the radiation has hidden quantum links called entanglement, maybe something tiny is left over, or maybe the quantum rules break, and nobody knows yet. We cannot watch it happen because space's microwaves are warmer than the hole, so it grows. I was not sure what a 'state' is, what the other numbers are, why the rules for sealed-off things apply when radiation is leaving the hole, why 'why it is forbidden' follows, how hidden links fit with the radiation being the same, and how a hole can both shrink and grow.

**Stumbles (30)**

- “a couple of other overall numbers”: Summary: which numbers? A reader cannot picture 'overall numbers' and wonders whether size or colour counts.
- “How this clash is resolved is still an open question.”: Summary: 'this clash' names a clash the summary never set up in one sentence, and the long sentences had to be reread.
- “Quantum rules say that, if you keep track of everything, information is never destroyed”: 'Keep track of everything' is not a condition a reader can check, and the rule only holds for something sealed off.
- “a region whose gravity lets nothing, not even light, back out once it crosses the edge”: Recap: 'it' could be the gravity, the region or 'nothing'; the sentence had to be reread.
- “they fix its state at every moment from its state at any one moment”: Recap: 'state' is never defined, and the forwards-and-backwards idea the whole way depends on is buried.
- “So the hole slowly shrinks, and this is called evaporation.”: Recap says every hole shrinks, but the last paragraph says a Sun-mass hole grows. The reader sees a contradiction; 'shrinks' also hides that it is mass being lost.
- “So someone tracking every piece could work back to the words.”: Step left implicit: different arrangements alone do not let you work back; the rules must also run backwards.
- “That alone is no crisis”: 'Crisis', 'clash', 'problem' and 'trouble' all name one idea.
- “In the simplest calculation, it depends only on a few overall numbers, such as the hole's mass.”: 'It' could be the radiation or the calculation, and 'a few overall numbers' gives the reader nothing to hold.
- “Once that hole has evaporated completely, nothing is left to hold that information either. The information seems destroyed, which the quantum rules forbid.”: First what-if: the hole is not sealed off, radiation leaves it, so why do the sealed-off rules apply? And why exactly is destroying information forbidden? Both links were missing.
- “Perhaps the Hawking radiation carries the information in faint links between its pieces.”: 'Pieces' of radiation is unfamiliar, 'faint' suggests weak rather than hidden, and the reader asks how this fits with the radiation being the same whatever fell in.
- “Many physicists now expect the first”: 'The first' points by position.
- “Such links would be purely quantum. This kind of link is called entanglement. Going further needs entanglement and the entropy of black holes.”: Two new terms in one paragraph; entanglement is named after the paragraph that described the links.
- “Nobody can watch this happen yet.”: 'This' could be evaporation or the loss of information.
- “A black hole with the Sun's mass is only about sixty billionths of a degree above absolute zero.”: A hole 'is' a temperature? The reader needs to know it is the glow's temperature.
- “Because the hole is colder than those microwaves, it takes in more than it gives off, and grows.”: Surprising claim with no everyday reason; and the first what-if, a smaller black hole, is left open.
- “replace each letter by the next letter of the alphabet”: Try-it: what does Z become? And rule one does not look like scrambling, so the reader misses the point of the comparison.
- “so a fix at the very end cannot settle it alone”: Simplifies: a what-if fails. A tiny leftover is a fix at the very end that the explanation itself offers, so the sentence contradicts the explanation.
- “"Keep the books with the Page curve" counts why.”: 'Counts why' is unclear.
- “how this is resolved is still open”: Takeaway: 'this' is vague and the sentence runs long for saying back.
- “Picture two black holes that match in every overall number, such as mass. One formed when a huge library collapsed”: Check: which numbers must match is unclear, and a teenager objects that a library cannot become a black hole.
- “Each hole evaporates completely, so it sends out all of its energy, and both started with the same mass.”: Check answer: the link from equal mass to equal energy is missing; the entry way never said energy has mass.
- “So the hole takes in more microwaves than it gives off in Hawking radiation”: Check answer: compares microwaves with radiation rather than energy with energy, and the colder-takes-in rule has no everyday anchor.
- “Are its words destroyed forever, or only scrambled so badly that nobody could read them?”: Opening question: the everyday answer 'destroyed' is right in practice, so the setting must say that in principle is meant.
- “When both evaporate, do you think their Hawking radiation could tell you which one held the books?”: Opening question: does not name the simplest calculation or complete evaporation, so a reader who knows about hidden links could be marked wrong.
- “calculations in simplified model universes have found that the information can come out in the Hawking radiation”: Common answer overstates: the calculations find the radiation's entropy behaving as it must if information comes out, not how it comes out.
- “The details of how something started ... The quantum rules scramble information but never destroy it.”: Glossary: 'never' without the sealed-off condition fails for a letter whose smoke drifts away into a room.
- “A purely quantum link between pieces of a system”: Glossary: 'system' is jargon.
- “The slow shrinking of a black hole as Hawking radiation carries away its energy.”: Glossary: evaporation does not happen in warm surroundings, which the entry way itself says.
- “about 273 degrees below the freezing point of water”: Glossary: degrees of what? The entry way's 2.7 degrees needs the scale.

**Fixes**

- Entry way: named the three numbers (mass, spin, electric charge), defined 'state' and the forwards-and-backwards rule in the recap, and made the sealed-off whole explicit: count the hole and its radiation as one thing, so two different starts ending the same is what the quantum rules forbid.
- Entry way: removed the shrink-versus-grow contradiction by scoping evaporation to cold, empty space in the recap and glossary, and backed the growth claim with a cold drink in a warm room.
- Entry way: one word per idea ('clash' throughout, 'hidden links' for the entanglement option), no 'the first' pointer, no ambiguous 'it' or 'this', and entanglement named in the paragraph that describes the links.
- Simplifies: the claim that a fix at the end cannot settle the clash contradicted the tiny-leftover option; rescoped to 'unless a tiny leftover holds all the information'.
- Try-it: Z wraps to A, and the lesson is stated: the rules may scramble, but two different starts never end the same.
- Summary split into short sentences with the three numbers and the sealed-off condition; takeaway split into two sentences.
- Entry checks, opening questions and the 'is it solved' answer: named settings and numbers, added the energy-has-mass link, and stopped the answer overstating what the 2019 calculations show.
- Ladder: the working way now bridges from the entry way's hidden links to entanglement entropy, defines a density matrix, and defines the Planck length and 'semiclassical' before using them. Each non-entry way's first sentence already names the way it continues; the five ways are genuinely different routes (picture, calculation, structure, historical puzzle, calculation).
- Budgets: to keep the entry way within 300 words and tutoring within 3,500, shortened spoken versions of three formal and working checks and one misconception correction, without changing their content.
- Bumped the revision to 2.

**Concerns**

- The entry way sits at the frontier cap of 300 words and tutoring at the 3,500 cap, so any further entry addition needs cuts elsewhere.
- The related note hawking-radiation says 'event horizon' and 'leftover glow' or 'cosmic microwave background'; this note says 'horizon' and 'faint microwaves'. Align once the black-hole-evaporation prerequisite note fixes the entry vocabulary.
- Physics reviewer: confirm the new entry claim that, in the simplest calculation, Hawking radiation depends only on mass, spin and electric charge, and that every black hole found so far is heavier than the Sun.
- Physics reviewer: the working way's new bridge sentences (density matrix, Planck length 1.6e-35 m, semiclassical physics) and the rescoped simplifies sentence about a tiny leftover should be checked.
- The writer's reported convention gaps stand: the conventions file should state natural-log entropy and the units of surface gravity; reported, not invented here.
- None of the prerequisite notes exist yet, so the recap and glossary could not be aligned with their entry ways.

**Re-read** (2026-09-13, revision 3): 7 stumbles in 12 changed passages

- “a hole without spin or electric charge glows more coldly the heavier it is. Spin or charge only cools a hole.”: Recap, physics-review wording: 'only cools' reads as 'all spin or charge does is cool it', and a glow that is 'more coldly' is an odd phrase the reader has to reread.
- “Write a secret on paper and burn it.”: The next paragraph drops 'the letter' into a black hole; 'a secret on paper' and 'the letter' are two names for one object, so the reader wonders whether it is the same thing.
- “So a letter hole and a rock hole with matching numbers give off the same kind of radiation.”: A 'letter hole' sounds like a hole made from one letter, and no 'rock hole' has been introduced; the reader cannot tell what the two holes are.
- “fill space at about 2.7 degrees.”: Degrees without a reference: the reader may read 2.7 degrees Celsius, which is not cold compared with the hole's temperature counted from absolute zero.
- “In the simplest calculation, that radiation depends only on the hole's mass, spin and electric charge. So if the hole evaporates completely, the information about what fell in seems destroyed.”: Summary: the step from 'depends only on three numbers' to 'the information seems destroyed' is left to the reader; the missing link is that the radiation does not depend on what fell in. Not applied: the summary has a hard limit of 450 characters and the rewrite needs 455; see the major issue raised with this re-read.
- “Imagine two black holes with the same mass, one made from a crushed library and one from crushed rock.”: False first what-if: a reader who learned that Hawking radiation depends on mass, spin and charge answers 'yes, if their spins differ', which the question would mark wrong.
- “Hawking radiation carries away all of the hole's energy.”: False first what-if: the same entry way says a Sun-mass hole in today's space grows, so the radiation does not carry away all its energy; the condition from the check answer (complete evaporation) is missing.
- Fix: Recap: 'glows more coldly' became 'is colder', and 'Spin or charge only cools a hole' became 'Spin or charge makes a hole colder still'; the recap stays within 700 characters.
- Fix: Entry explanation: 'a secret on paper' became 'a secret letter'; the two holes are now 'two holes with matching numbers ... even if only one swallowed the letter'; the microwave temperature says 'above absolute zero'. The explanation stays within 300 words.
- Fix: Opening question library-and-rock: the two holes now match in mass, spin and electric charge, as in checks/letter-and-rocks.
- Fix: Misconception energy-goes-missing: correction scoped to a hole that evaporates completely, matching checks/letter-and-rocks.
- Fix: Budget: tutoring was at its 3,500-word cap, so the entry common question did-hawking-think-it-was-lost was dropped (lowest value: history/hawking-1976 carries the same content, and nothing linked to it). The note is unpublished, so its id is not retired.
- Fix: Not changed: 'In cold, empty space' in the summary and recap; the cold-drink comparison in the explanation shows that 'cold' means colder than the hole.
- Fix: Summary unchanged: adding 'not on what fell in' breaks the 450-character summary limit, and no sentence there is low-value enough to drop, so the missing link is reported instead of compressed.
- Fix: Bumped the revision to 3.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 3)

**Verification**

- S_BH = 4 pi G k_B M^2/(hbar c) from k_B c^3 A/(4 G hbar) with A = 16 pi G^2 M^2/c^4; S_BH(Sun) = 1.05e77 k_B.: Hand algebra; python with G=6.674e-11, c=2.998e8, hbar=1.0546e-34, M=1.989e30. → 1.049e77. Correct.
- Black-body entropy bookkeeping: s = 4u/3T, entropy flux 4/3 dE/T, dS_H = -4/3 dS_BH.: Re-derived from u = aT^4, dS = dU/T, fluxes cu/4 and cs/4, first law dS_BH = -dE/T_H. → Correct for ideal black-body emission into empty space; greybody caveat is in simplifies.
- Page time: S_BH = 4/7 S0, M = 0.756 M0, t_P = [1-(4/7)^(3/2)] tau = 0.568 tau.: python → 0.75593, 0.56804. Correct.
- Problem page-time-for-other-entropy-ratios: beta=1 gives 0.707, 0.646; beta=3/2 gives 0.775, 0.535; larger beta earlier.: python; solved in general form. → 0.70711/0.64645 and 0.77460/0.53524; beta=4/3 reproduces 0.568. Tolerances fine.
- Horizon radius at Page time 2.23 km; curvature radius about 1.2 km, some 1e38 Planck lengths; Planck length 1.6e-35 m.: python; Kretschmann 48G^2M^2/(c^4 r^6) = 12/r_s^4 at r_s, so K^(-1/4) = r_s/12^(1/4). → 2.233 km; 1.200 km; 7.4e37 Planck lengths (order 1e38); l_P = 1.616e-35 m. Correct.
- Hawking temperature of a solar-mass hole 6.17e-8 K (entry: about sixty billionths of a degree); CMB 2.72548 K; ratio 4.4e7; entry check 2.7/60e-9 = 4.5e7 within 10 per cent.: python with T_H = hbar c^3/(8 pi G M k_B). → 6.169e-8 K; 4.42e7; 4.5e7 with rel_tol 0.1 accepts both. Correct.
- Threshold mass for net absorption from the CMB 4.5e22 kg, 0.6 lunar masses.: python → 4.50e22 kg; 0.61 of 7.342e22 kg. Correct for non-rotating holes; spin or charge only lowers T_H, so the growth statement holds for all known holes.
- Entry recap 'a heavier hole glows more coldly' and entry 'every black hole found so far is heavier than the Sun, so even colder'.: Kerr-Newman T = (r+ - r-)/(4 pi (r+^2 + a^2)) evaluated in python at fixed M varying a and Q, and at fixed Q varying M. → At fixed M, spin or charge lowers T (a=0.9M: 0.61 of Schwarzschild). At fixed Q=1, raising M from 1.0 to 1.1 raises T from 0 to 0.030, so the unscoped recap was false for near-extremal holes. Rescoped: heavier is colder for holes without spin or charge, and spin or charge only cools. The entry conclusion then follows for any hole above a solar mass.
- Lightest black holes found are heavier than the Sun.: WebSearch: LIGO GW190814 (2.6 solar-mass object of uncertain nature), GW230529 (2.5-4.5 solar masses), mass-gap reviews. → Confirmed: no black hole below about 2.5 solar masses is known.
- In the simplest calculation, late-time Hawking radiation depends only on mass, spin and electric charge.: No-hair theorems for stationary Kerr-Newman holes plus Hawking's late-time thermal flux with greybody factors and chemical potentials for charge and angular momentum. → Correct for the settled hole; early transients are outside 'simplest calculation' and do not change the entry claim.
- Try-it: CAT to DBU and DOG to EPH under the shift rule.: Letter by letter. → Correct.
- Singlet: each spin has S = k_B ln 2; fine-grained entropy never exceeds coarse-grained entropy.: Reduced density matrix I/2; maximum-entropy definition of coarse-grained entropy. → Correct.
- Hawking pair state normalization and reduced thermal state at T_H = kappa/2pi with kappa = 1/4M.: Sum of (1-x) x^n = 1 with x = e^(-2 pi omega/kappa); trace over orthonormal partner states. → Correct in G=c=hbar=k_B=1.
- Problem entropy-of-one-hawking-mode: S = -ln(1-x) - x ln x/(1-x) equals oscillator entropy; S = 1.0407 at x = 1/e.: Hand derivation from Z = 1/(1-x); python. → 1.04065. Correct.
- Derivation small-corrections-cannot-turn-the-curve: SSA plus Araki-Lieb give S(Rb) >= S(R) + S(b) - 2 S(bc).: Re-derived: S(Rb)+S(bc) >= S(b)+S(Rbc) and S(Rbc) >= S(R)-S(bc). → Correct, including the factor 2.
- Monogamy check: pure bc implies rho_Rbc = rho_R tensor psi_bc, so S(Rb) = S(R) + S(b).: Hand algebra. → Correct.
- Page average entropy ln m - m/2n; 3 of 10 qubits gives 2.048, 98.5 per cent of ln 8.: python, also Page's exact sum over k from n+1 to mn of 1/k minus (m-1)/2n. → Approximation 2.0482, exact 2.0487; both inside rel_tol 0.005. Correct.
- Remnant check: 4/3 x 1.05e77 = 1.40e77; Planck mass 2.18e-8 kg (22 micrograms); S_BH(m_P) = 4 pi k_B = 12.57; 78 digits in the misconception.: python → 1.400e77 (78 digits); 2.1765e-8 kg; 12.566. Correct.
- Scrambling time: hbar/(2 pi k_B T_H) = 4GM/c^3 = 1.97e-5 s; ln(S_BH/k_B) = 177.3; t* = 3.49 ms; black-body lifetime of a solar-mass hole 2.1e67 yr, Page time 1.2e67 yr.: Hand algebra; python with tau = 5120 pi G^2 M^3/(hbar c^4). → 1.9705e-5 s, 177.35, 3.495 ms; tau = 2.10e67 yr and 0.568 tau = 1.19e67 yr. Correct inside the note's black-body model, now said in the statement.
- Island rule, QES just inside the event horizon for an evaporating hole; replica-trick origin; Hayden-Preskill return after a scrambling time.: Compared with Penington 2019/2020 and Almheiri-Engelhardt-Marolf-Maxfield 2019 abstracts and the 2021 review. → Correct; scoped 'just inside the event horizon' to evaporating holes, because for eternal holes coupled to a bath the island can extend outside the horizon.
- Quantum secret-sharing threshold above half the shares.: No-cloning argument for pure-state threshold schemes. → Correct.
- History scope: AMPS called the firewall the most conservative resolution; Harlow-Hayden decoding time; Hawking later worked on information-preserving ideas.: WebSearch of the AMPS abstract; knowledge of Harlow-Hayden 2013 and Hawking's 2005 and 2016 papers. → Confirmed.
- References: Fixsen 2009; Steinhauer 2016; Landsman et al. 2019; Hawking 1975 and 1976; Page 1993; Susskind-Thorlacius-Uglum 1993; AMPS 2013; Penington 2020; AEMM 2019; AMMZ 2020; AHMST 2021; Harlow 2016; Maldacena-Susskind 2013; Hayden-Preskill 2007; Sekino-Susskind 2008; Strominger-Vafa 1996; Mathur 2005; Banks-Peskin-Susskind 1984.: WebSearch against publisher, ADS, arXiv and INSPIRE records. → All authors, years, titles, venues, pages and arXiv ids confirmed; DOIs added; verified set true.

**Counterexamples tried**

- Near-extremal charged hole (fixed charge, mass raised slightly): gets hotter, not colder. Broke the recap 'a heavier hole glows more coldly'; rescoped to holes without spin or charge, with spin or charge only cooling.
- Hole in warm surroundings (CMB at 2.7 K): grows rather than evaporates. Broke the summary's unscoped 'A black hole evaporates'; now 'In cold, empty space'. Recap and glossary were already scoped.
- Information loss as a resolution (non-unitary evolution): the simplifies sentence claimed the simplest calculation must fail unless a remnant holds the information, but if the quantum rules fail it need not. Added 'if the quantum rules hold'. 'Wrong' changed to 'missing something', because island results keep local semiclassical physics and correct only the entropy.
- Rapidly spinning light hole versus slower heavier hole: a lighter hole spinning at a=0.99M is colder than a non-spinning hole of twice its mass, which is why the recap separates the mass rule from the spin-or-charge rule.
- Small primordial holes below 4.5e22 kg: would be warmer than the CMB and evaporate today. None is found, so 'Nobody can watch a black hole evaporate yet' and 'every black hole found so far' stand.
- Eternal black hole in equilibrium with a bath: the island can extend outside the horizon. Research way now says 'For an evaporating hole' before placing the island boundary inside the event horizon.
- Earlier proposals: 't Hooft's S-matrix ideas of the 1980s preceded complementarity, so 'the first attempt' became 'the best-known attempt'.
- Greybody factors and extra species: change 4/3 to about 1.48 or more; covered by the simplifies text and the beta problem. The Page time stays at more than half the lifetime with most of the mass left, so the entry claims survive.
- Partially pure pairs (S(bc) = epsilon > 0): handled by the strong subadditivity derivation; the exactly pure case in the historical way is flagged in simplifies.

**Fixes**

- Summary: scoped evaporation to cold, empty space.
- Entry recap: 'a heavier hole glows more coldly' rescoped to holes without spin or charge, plus 'spin or charge only cools a hole', so 'heavier than the Sun, so even colder' is true. Other recap wording tightened to stay under 700 characters, with no change in meaning.
- Entry simplifies: added 'if the quantum rules hold' and 'missing something' in place of 'wrong'.
- Working way: coarse-grained entropy defined as k_B times the logarithm of the number of states, not the count itself.
- Historical way: 'first attempt' became 'best-known attempt' for complementarity.
- Research way: island boundary inside the event horizon scoped to an evaporating hole.
- Entry check sun-mass-hole-in-space-microwaves: 'is about' became 'glows at about', matching the entry way.
- Hayden-Preskill problem: the 1.2e67-year Page time is labelled as the black-body bookkeeping value.
- All 19 references verified, with DOIs added.

**Concerns**

- Revision kept at 2, following the exemplar, so both reviews cover the same text. The physics fixes change a few learner-visible entry sentences (summary, recap, simplifies, one check), so an editor may bump the revision and ask for a quick novice re-read.
- Convention gaps, reported and not invented: the conventions file does not state natural-log entropy, entropy units, or surface-gravity units.
- The lifetime and Page-time numbers rest on the black-body photon model (lifetime 2.1e67 yr for one solar mass). A greybody treatment with photons and gravitons gives a lifetime of about 1.2e67 yr and a Page time near 0.54 of it. The note labels its model; the Page-curve visual should make the model explicit.
- Vocabulary alignment with hawking-radiation ('event horizon' versus 'horizon', 'leftover glow' versus 'faint microwaves') is still pending, as the novice reviewer said.
- The prerequisites penrose-diagram-of-evaporating-black-hole and quantum-field-theory-in-curved-spacetime differ from the registry. Both are acyclic, but penrose-diagram-of-evaporating-black-hole already has black-hole-evaporation as a prerequisite. Keeping both is acceptable because they are needed at different rungs.
- Steinhauer's 2016 entanglement claim has been debated in later analyses; the note's wording 'consistent with entanglement' is appropriately cautious.

**Diff check** (2026-09-13, revision 3)

- Entry recap: 'Measured from far away, a hole without spin or electric charge is colder the heavier it is.' (was 'glows more coldly the heavier it is').: Schwarzschild k_B T_H = hbar c^3/(8 pi G M), so T_H is proportional to 1/M; compared the old and new wording. → True, and the same claim as before with plainer wording. Sun-mass value 6.17e-8 K, about sixty billionths of a degree.
- Entry recap: 'Spin or charge makes a hole colder still.' (was 'Spin or charge only cools a hole'), read as a comparison at the same mass, which is what 'heavier than the Sun, so even colder' needs.: Kerr-Newman (G = c = 1): T = s/(2 pi ((M+s)^2 + a^2)) with s = sqrt(M^2 - a^2 - Q^2). dT/ds = (M^2 + a^2 - s^2)/D^2 >= 0 at fixed a, and at fixed Q it is (2M^2 - Q^2)/D^2 > 0, so spin or charge at fixed M lowers T. Python: 100000 random (a, Q) at M = 1, none hotter than 1/(8 pi). What-if of spinning a hole up by throwing in matter: dT/da = dT/dQ = 0 at a = Q = 0, so only the added mass matters at first order, and it cools the hole. Extremal limit T = 0 is consistent with 'colder still'. → True, and equally true as the old wording. A comparison between holes of different masses is not claimed; the recap is at 699 of 700 characters, so 'at the same mass' was not added, and the preceding sentence supplies the mass scope.
- Misconception energy-goes-missing correction: 'A hole that evaporates completely sends out all of its energy as Hawking radiation.': Energy conservation for an asymptotically flat hole: its mass is its total energy, and complete evaporation leaves nothing. What-if of a Sun-mass hole in today's microwave background: it grows, but the sentence is now conditioned on complete evaporation. Compared with checks/letter-and-rocks. → True within the simplest calculation, and the condition fixes the false what-if in the old wording. Consistent with checks/letter-and-rocks and the summary.
- Opening question library-and-rock: holes with the same mass, spin and electric charge; their Hawking radiation in the simplest calculation cannot tell which held the books.: Semiclassical Hawking emission from a stationary Kerr-Newman hole depends only on (M, J, Q); with identical starting values the evaporation histories of (M, J, Q), including spin-down and discharge, are identical, so the emission statistics match at every stage. → True, and now consistent with checks/letter-and-rocks. Matching only the mass, as before, allowed the correct answer 'yes, if the spins differ'.
- Entry explanation: 'So two holes with matching numbers give off the same kind of radiation, even if only one swallowed the letter.': Same no-hair argument as the opening question; checked that 'matching numbers' refers to mass, spin and electric charge in the previous sentence, and that the letter's own mass is absorbed into the matching mass. → True within the stated 'simplest calculation' scope. 'Same kind of radiation' correctly avoids claiming identical individual quanta.
- Entry explanation: microwaves 'at about 2.7 degrees above absolute zero'; hole 'about sixty billionths of a degree above absolute zero'.: T_CMB = 2.72548 K (Fixsen 2009); T_H(Sun) computed in python = 6.17e-8 K; glossary defines degrees above absolute zero as Celsius-sized. → Correct; the ratio 4.4e7 agrees with checks/sun-mass-hole-in-space-microwaves (2.7/60e-9 = 4.5e7 within its 10 per cent tolerance).
- Entry explanation: 'Write a secret letter and burn it.' (was 'a secret on paper').: Read in context of the burning paragraph. → Same claim; no physics content changed.
- Removed common question did-hawking-think-it-was-lost.: Searched the vault for the id; confirmed history/hawking-1976 still states the 1976 argument that complete evaporation turns a pure state into a mixed one. → No remaining links to the id; no physics content lost that another item does not carry.
- Fix: No learner-visible text changed, so the revision stays at 3.
- Fix: Author-facing visual proposal library-hole-and-rock-hole: the sketch said the two holes match only in mass; it now says mass, spin and electric charge, matching the opening question and checks/letter-and-rocks. The role still says 'matching mass'; note_diff counts the role as learner-visible, so it was left for an editor rather than bumping the revision.
