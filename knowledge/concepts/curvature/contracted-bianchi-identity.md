---
type: "concept"
id: "contracted-bianchi-identity"
title: "Contracted Bianchi identity"
domain: "curvature"
tier: "core"
aliases: ["twice-contracted Bianchi identity", "divergence-free Einstein tensor", "nabla_b G^ab = 0"]
prerequisites: ["bianchi-identity", "ricci-tensor", "ricci-scalar", "metric-compatibility"]
leads_to: ["einstein-tensor", "einstein-field-equations", "propagation-of-constraints", "equations-of-motion-from-field-equations"]
sources: ["dinverno:ch06", "dinverno:ch10", "dinverno:ch11", "dinverno:ch13", "dinverno:ch15", "dinverno:ch23", "dinverno:ch24", "gifted-amateur:ch13", "gifted-amateur:ch43", "legacy:manuscript-section-09-bianchi-einstein-tensor", "legacy:manuscript-section-12-trace-subtraction-and-reversal", "schutz:ch06", "schutz:ch08"]
review: "fixed"
---

# Contracted Bianchi identity

> If you trace the Bianchi identity twice with the metric, you find that the divergence of the Ricci tensor is exactly half the gradient of the Ricci scalar. Equivalently, the Einstein tensor, Ricci minus half the scalar curvature times the metric, has zero divergence for every possible metric. That built-in balance is why Einstein's equation automatically respects local energy-momentum conservation, and why four combinations of its ten components cannot be independent evolution equations.

## Explanations by level

### Intuition

Think of two account books that must always agree. One belongs to matter: at every place and moment, energy and momentum that flow in must equal what flows out plus what is stored, so its books always balance. The other belongs to geometry. The contracted Bianchi identity says there is one particular way of summarising curvature whose books also balance, automatically, no matter what shape spacetime has. If you want to write a law saying 'geometry equals matter', you had better use that self-balancing summary, otherwise the two books would drift apart and the law would force matter to do strange things. That self-balancing summary is the Einstein tensor. 'Balanced books' here means nothing is created or destroyed at any point; it does not mean the entries are the same everywhere. Curvature can still be large inside a star and small outside, just as water can speed up in a narrow pipe while no water is created. The picture is simplified: in curved spacetime the balance is local, and it does not add up to a single total that stays fixed for the whole universe.

**Picture to hold:** Two ledgers side by side, one labelled geometry and one labelled matter, each with an automatic 'balanced' stamp at every point of spacetime; an equals sign is only allowed between ledgers that both carry the stamp.

**Assumes:** [[curvature]], [[local-conservation-of-energy-momentum]]

### Working

Start from the Bianchi identity ∇_λ R^ρ_σμν + ∇_μ R^ρ_σνλ + ∇_ν R^ρ_σλμ = 0. Contract ρ with μ (first index with the loop-plane index that makes Ricci): using R^μ_σμν = R_σν and R^μ_σλμ = −R_σλ, you get ∇_λ R_σν − ∇_ν R_σλ + ∇_μ R^μ_σνλ = 0. Now raise σ and contract it with ν. Metric compatibility (∇g = 0) lets the inverse metric pass through every covariant derivative, and the pair symmetries of Riemann turn the last term into another −∇_μ R^μ_λ. The result is ∇_λ R − 2∇_μ R^μ_λ = 0, that is ∇_μ R^μ_ν = ½ ∇_ν R. Moving everything to one side: ∇_μ (R^μ_ν − ½ δ^μ_ν R) = 0, or with both indices up, ∇_μ G^μν = 0. These are four equations (one per value of ν) that hold for every metric. Two consequences follow. First, the only combination R^μν + B g^μν R (B a pure number) that is divergence-free for all metrics has B = −½, since its divergence is (½ + B)∇^ν R; adding Λ g^μν changes nothing because ∇g = 0. So once matter obeys ∇_μ T^μν = 0, G^μν + Λ g^μν = 8π T^μν is consistent, while the tempting Ricci guess R^μν = κ T^μν would force the scalar curvature, and hence the trace of T, to be constant everywhere, which a star in empty space violates. Second, the ten Einstein equations obey four differential identities, so they cannot fix all ten metric components; four are coordinate freedom.

**Picture to hold:** A coefficient slider on 'Ricci plus B times R times metric': the divergence residual is proportional to (½ + B) and disappears at a single setting, B = −½, whatever spacetime is loaded.

**Assumes:** [[bianchi-identity]], [[ricci-tensor]], [[ricci-scalar]], [[metric-compatibility]], [[divergence]]

### Formal

For the Levi-Civita connection of any pseudo-Riemannian metric in dimension n ≥ 2, the twice-contracted second Bianchi identity is ∇^μ R_μν = ½ ∇_ν R, equivalently ∇^μ G_μν = 0 with G_μν = R_μν − ½ R g_μν. It follows by contracting the differential Bianchi identity with g^ρμ and then g^σν; the metric is essential here (to contract, and to commute contraction with ∇ via ∇g = 0), unlike the uncontracted identity which needs only zero torsion. It is an identity in the strict sense: it holds off shell, for all metrics, independent of any field equation. Consequences and readings: (i) given the field equation G_μν + Λ g_μν = 8π T_μν, it implies ∇^μ T_μν = 0, so the field equation is consistent only with conserved sources, and for dust or perfect fluids this contains the matter's equations of motion; (ii) among the ten components of the field equations there are four differential relations, matching the four-function coordinate freedom, so the equations determine six geometric functions; in a 3+1 split the four components G_μν n^ν contain no second time derivatives (constraints), and the identity guarantees constraints satisfied initially remain satisfied under the evolution equations; (iii) from the action viewpoint, diffeomorphism invariance of any scalar metric Lagrangian implies its Euler-Lagrange tensor is identically divergence-free, and for √−g R that tensor is proportional to √−g G^μν, giving an independent derivation (a Noether second-theorem identity); (iv) if symmetry forces G_μν = −f g_μν for some function f (as isotropy does for the spatial sections in d'Inverno's cosmology chapter), the identity gives ∇_ν f = 0, so f is constant; for an Einstein space R_μν = f g_μν it gives (1 − n/2)∇_ν f = 0, so for n ≥ 3 the function f and the scalar curvature are constant (a Schur-type result). In n = 2 it is trivial because G vanishes identically; in n = 3 it is equivalent to the full Bianchi identity. With signature (+,−,−,−) the scalar R and mixed components G^μ_ν change sign while R_μν, G_μν and G^μν do not; the identity is unaffected. Lovelock's theorem strengthens the selection argument: in four dimensions a G_μν + b g_μν is the only symmetric, identically divergence-free tensor built locally from the metric and its first two derivatives.

**Picture to hold:** Integrated form: the flux of the Einstein tensor (as a vector-valued 3-form) through the boundary of any infinitesimal 4-cell vanishes, the gravitational counterpart of charge conservation.

**Assumes:** [[levi-civita-connection]], [[diffeomorphism-invariance]], [[constraint-equations]], [[lovelock-theorem]]

## Prerequisites

- [[bianchi-identity]] — It is literally the differential Bianchi identity traced twice.
- [[ricci-tensor]] — The first contraction produces the Ricci tensor, with signs fixed by the course contraction R_μν = R^ρ_μρν.
- [[ricci-scalar]] — The second contraction produces the scalar curvature whose gradient appears on one side.
- [[metric-compatibility]] — Raising indices and contracting inside a covariant derivative is legal only because ∇g = 0.

## Leads to

- [[einstein-tensor]] — The identity singles out Ricci minus half R times the metric as the divergence-free curvature tensor.
- [[einstein-field-equations]] — It fixes the relative coefficient on the geometric side and makes the equations consistent with conserved matter.
- [[propagation-of-constraints]] — In the initial-value problem it guarantees that constraints satisfied on the first slice stay satisfied.
- [[equations-of-motion-from-field-equations]] — Through ∇T = 0 it implies that matter's motion, including geodesic motion of dust, is contained in the field equations.

## Related

- [[covariant-conservation-of-energy-momentum]] — The matter-side statement that the identity mirrors; the field equation links the two.
- [[conservation-law-from-diffeomorphism-invariance]] — An alternative derivation: coordinate invariance of the action forces a divergence-free Euler-Lagrange tensor.
- [[gravitational-degrees-of-freedom]] — Four identities plus four coordinate functions reduce ten metric components to the counting of physical freedom.
- [[cosmological-constant]] — Λ g_μν is also divergence-free, so the identity cannot exclude it.
- [[fluid-equation]] — In cosmology the identity guarantees that the Friedmann equations already contain energy conservation of the cosmic fluid.
- [[ricci-tensor-field-equation]] — The rejected Ricci-equals-matter guess is exposed by this identity.

## Key equations

### Twice-contracted Bianchi identity

$$
\nabla_\mu R^{\mu}{}_{\nu} = \tfrac12 \nabla_\nu R
$$

The divergence of the Ricci tensor equals half the gradient of the Ricci scalar, for every metric. *(SCH ch06 (6.97) §6.6 p.163; GA ch13 (13.29) §13.3 p.146; GA ch43 (43.57) p.475)*

**Convention:** Gifted Amateur writes 2R^α_γ;α = R_;γ; Schutz writes (2R^μ_λ − δ^μ_λ R)_;μ = 0.

### Divergence-free Einstein tensor

$$
\nabla_\mu G^{\mu\nu} = 0, \qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu}
$$

Four identities, one per free index, satisfied by the Einstein tensor of any metric; since G is symmetric, it does not matter which index carries the divergence. *(SCH ch06 (6.99) §6.6 p.163; SCH ch08 (8.11) §8.2 p.187; GA ch13 (13.33) §13.3 p.146; DIV ch06 (6.87) §6.12 p.106; DIV ch13 (13.3) §13.2 p.218)*

**Convention:** Schutz puts the divergence on the second index (G^αβ_;β), Gifted Amateur on the first (G^μν_;μ), d'Inverno writes ∇_b G_a^b ≡ 0 in Chapter 6 and ∇_b G^ab = 0 later.

### Once-contracted step

$$
\nabla_\lambda R_{\sigma\nu} - \nabla_\nu R_{\sigma\lambda} + \nabla_\mu R^{\mu}{}_{\sigma\nu\lambda} = 0
$$

The intermediate result after the first trace: a curl of Ricci plus the divergence of Riemann vanishes. *(SCH ch06 (6.93) §6.6 p.163; GA ch13 (13.28) §13.3 p.146)*

**Convention:** Schutz calls this the contracted Bianchi identities and the final form the twice-contracted ones.

### Why the coefficient is one half

$$
\nabla_\nu\left(R^{\mu\nu} + B\, g^{\mu\nu} R + \Lambda g^{\mu\nu}\right) = \left(\tfrac12 + B\right)\nabla^\mu R
$$

Using the identity and ∇g = 0, the divergence of the general candidate is proportional to the gradient of R; it vanishes for every metric only if B = −½, while Λ is unconstrained. *(SCH ch08 (8.4)-(8.6) §8.1 p.184; legacy:manuscript-section-12-trace-subtraction-and-reversal)*

**Convention:** Schutz uses μ for the coefficient (Eq. 8.4-8.6); we use B to avoid clashing with an index and with the scale factor a(t).

### Conservation implied by the field equation

$$
G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi T_{\mu\nu} \;\Longrightarrow\; \nabla^\mu T_{\mu\nu} = 0
$$

Taking the divergence of the field equation, the left side vanishes identically, so the source must be covariantly conserved. *(SCH ch06 §6.6 p.164; DIV ch13 (13.6) §13.3 p.220; DIV ch24 (24.56) §24.9 p.500)*

**Convention:** G = c = 1; in SI the coupling is 8πG/c⁴. d'Inverno writes the cosmological term as G_ab − Λg_ab in signature (+,−,−,−), the same physics.

### Constraint propagation (structure)

$$
\partial_t G_a{}^0 = -\partial_\beta G_a{}^\beta + \Gamma^c{}_{a0} G_c{}^0 + \Gamma^c{}_{a\beta} G_c{}^\beta - \Gamma^b{}_{b0} G_a{}^0 - \Gamma^b{}_{b\gamma} G_a{}^\gamma
$$

The identity written in coordinates gives the time derivative of the constraint components in terms of spatial quantities; once the evolution equations hold, the right side is linear and homogeneous in the constraints, so zero initial constraints stay zero. *(DIV ch13 (13.31) §13.6 p.228)*

**Convention:** Quoted from d'Inverno, who uses signature (+,−,−,−) and Latin a,b,c = 0..3 with Greek β,γ = 1..3; the structure, not the signs of g, is the point.

## Conventions across the books

| Issue | Schutz | Gifted Amateur | d'Inverno | Course choice |
| --- | --- | --- | --- | --- |
| Naming of the once- and twice-contracted forms | 'Contracted Bianchi identities' for the once-contracted Eq. 6.93; 'twice-contracted Bianchi identities' (often just 'Bianchi identities') for Eq. 6.97 and G^αβ_;β = 0. | 'Contracted Bianchi identity' for the twice-contracted relation 2R^α_γ;α = R_;γ. | 'Contracted Bianchi identities' for ∇_b G_a^b ≡ 0 (plural, one per free index). | 'Contracted Bianchi identity' means the twice-contracted statement ∇_μ R^μ_ν = ½∇_ν R ⇔ ∇_μ G^μν = 0; the intermediate result is called 'once-contracted'. |
| Index placement and which index carries the divergence | (2R^μ_λ − δ^μ_λ R)_;μ = 0 and G^αβ_;β = 0 (divergence on the second upper index). | G^μν_;μ = 0 (first index) and R^α_λ;α = ½R_;λ. | ∇_b G_a^b ≡ 0 with mixed indices in Chapter 6; ∇_b G^ab = 0 in Chapters 10, 13 and 24. | ∇_μ G^μν = 0 and ∇_μ R^μ_ν = ½∇_ν R; note aloud that G is symmetric so the choice of index does not matter. |
| Metric signature and the sign of R and mixed components | (−,+,+,+). | (−,+,+,+). | (+,−,−,−) with MTW Riemann and Ricci index conventions, so R and the mixed components G^a_b have the opposite sign to the course, while R_ab, G_ab and G^ab agree. | (−,+,+,+). The identity is homogeneous, so it is unchanged; only translated numerical values of R or G^μ_ν flip sign. |
| Sign and placement of the cosmological term that shares the zero divergence | G^αβ + Λg^αβ = 8πT^αβ. | R_μν − ½g_μν R = 8πG T_μν − Λg_μν (Λ moved to the right). | G_ab − Λg_ab = 8πT_ab in signature (+,−,−,−), equivalent to the course form after g → −g. | G_μν + Λg_μν = 8πT_μν; positive Λ is repulsive in all three. |
| Identity and special-coordinate markers | Plain equals signs; states in words that the result holds for any metric. | Plain equals signs; calls it a geometric counterpart of conservation. | Triple bar ≡ for identities valid for every metric, starred equals for relations in particular coordinates (Gaussian normal, harmonic). | Plain equals signs with the words 'for every metric'; name special coordinates explicitly when a step uses them. |

## How the sources teach it

### schutz

**Route:** In Chapter 6 contracts the Bianchi identities twice in a few lines, defines the Einstein tensor from the result and previews that G = 8πT makes conservation automatic. In Chapter 8 the identity becomes the engine of the argument for the field equations: write the general second-order candidate R + μgR + Λg, require its divergence to vanish for every metric because T is conserved, compare with Chapter 6 to force μ = −½, and later use the four identities to explain why only six of ten equations are independent and why coordinates can never be fixed by initial data.

**Representation:** Component algebra with explicit notes on metric compatibility and antisymmetry signs; prose counting argument.

**Strengths:** The cleanest logical chain from identity to field equation; the 'must hold for any metric' reasoning shows why conservation selects the geometry; the degrees-of-freedom count sets up gauge and constraints.

**Weaknesses:** The algebra to Eqs. 6.95-6.99 is left to Exercise 6.27; Λ is carried along without much comment on why it survives; no concrete example of what goes wrong with the wrong coefficient. *(SCH ch06 §6.6 p.163; SCH ch08 §8.1 p.184; SCH ch08 §8.2 p.187; SCH ch06 Ex 6.27)*

### gifted-amateur

**Route:** Puts the natural wrong guess, Ricci proportional to T, on the board first. Example 13.3 derives the contracted identity step by step from the quoted Bianchi identity; the Einstein tensor is then defined and shown divergence-free; combining the guess with conservation forces constant scalar curvature and so a constant trace of T throughout the universe, which contradicts lumpy matter, and the Einstein tensor is adopted as the fix. Chapter 43 mentions the identity historically and in exercises on the Weyl field equation and closed-surface flux.

**Representation:** Worked index contraction with margin notes on each symmetry used; a thought experiment about a non-uniform universe; a physics recap in plain words.

**Strengths:** Motivation by failure is memorable and shows why the half-trace term is necessary rather than decorative; every step of the contraction is visible.

**Weaknesses:** The Bianchi identity itself is taken on trust until Chapter 43; Λ enters later without linking it to the divergence argument; the letter G is overloaded (Einstein tensor, Newton's constant, a Green's function). *(GA ch13 §13.3 p.145; GA ch13 Example 13.3 §13.3 p.146; GA ch13 §13.3 p.147; GA ch43 p.467; GA ch43 Ex 43.5)*

### dinverno

**Route:** States the contracted identities with the Einstein tensor in Chapter 6 (proof by exercise). Chapter 10 uses them to suggest G proportional to T. Chapter 11 rederives them from coordinate invariance of an arbitrary metric action, before choosing any Lagrangian. Chapter 13 makes them structural: four identities among ten equations, conservation equations and motion of matter, and the propagation of constraints and of the harmonic gauge condition in the Cauchy problem. Chapters 15, 23 and 24 use them to drop redundant equations (the angular Schwarzschild equation, supplementary conditions at null infinity, and energy conservation inside the Friedmann equations).

**Representation:** Axiomatic and PDE-structural: identity signs, coordinate expansions, Cauchy-Kowalevskaya uniqueness, a variational derivation.

**Strengths:** By far the richest account of what the identity does: equation counting, constraints, gauge propagation and a derivation from general covariance that explains why the identity must exist.

**Weaknesses:** Scattered across many chapters; the first statement has no motivation; Chapter 10 can leave the impression that conservation uniquely forces G = κT (the cosmological term and Lovelock uniqueness come later or not at all). *(DIV ch06 §6.12 p.106; DIV ch10 §10.8 p.184; DIV ch11 §11.2 p.188; DIV ch11 (11.29) §11.4 p.192; DIV ch13 §13.2 p.218; DIV ch13 §13.6 p.228; DIV ch15 §15.5 p.277; DIV ch24 §24.9 p.500)*

### legacy

**Route:** Chapter 9 derives div Ricci = ½ grad R from the normal-coordinate Bianchi proof and warns that divergence-free is not constant; Chapter 12 asks which A Ric + B R g + C g is divergence-free, finds B = −A/2 with an honest note that this does not prove uniqueness, counts 10 − 4 − 4, and Chapter 15 separates the off-shell identity from on-shell matter conservation so that coupling is not circular.

**Representation:** Index derivations, a symbol table for the field equation, and explicit lists of what is derived versus chosen.

**Strengths:** Careful about logic (identity versus equation of motion, local versus global conservation) and about the limits of the uniqueness argument.

**Weaknesses:** The pieces sit in three chapters; no interactive or concrete divergence-free example; Lovelock's theorem is alluded to but not named. *(legacy:manuscript-section-09-bianchi-einstein-tensor; legacy:manuscript-section-12-trace-subtraction-and-reversal; legacy:manuscript-chapter-12-einstein-field-equation; legacy:manuscript-section-15-noether-killing-charges-redshift)*

## Recommended teaching path

1. **1. Motivating failure** — Propose the simplest field equation, Ricci proportional to T, and ask what happens when we take its divergence given that matter conserves energy and momentum. Leave the question open until the identity is in hand. *Why:* Learners need a reason to care about a divergence of curvature; a plausible guess that fails supplies it. *(GA ch13 §13.3 p.145)*
2. **2. Picture of 'divergence-free'** — Show a divergence-free flow whose speed varies (water through a narrowing pipe) and connect it to the matter ledger ∇_μ T^μν = 0. Stress that divergence-free means nothing is created at a point, not that the field is uniform. *Why:* Prevents the constant-versus-conserved confusion before the formalism appears. *(legacy:manuscript-section-09-bianchi-einstein-tensor)*
3. **3. Derive by two contractions** — Starting from the Bianchi identity, contract to Ricci, then contract again, naming the two facts used at each step (∇g = 0 and the antisymmetries). Arrive at ∇_μ R^μ_ν = ½∇_ν R and rewrite as ∇_μ G^μν = 0. *Why:* The derivation is short enough to do together and shows the result is pure geometry. *(SCH ch06 §6.6 p.163; GA ch13 Example 13.3 §13.3 p.146)*
4. **4. Check: the coefficient slider** — In the divergence-residual demo, vary B in R^μν + B g^μν R (and Λ) for several spacetimes; the learner predicts, then sees, that only B = −½ works for all of them and that Λ never matters. *Why:* Turns the selection of the Einstein tensor into a prediction the learner can test, and shows why Λ is allowed. *(SCH ch08 §8.1 p.184; legacy:manuscript-section-12-trace-subtraction-and-reversal)*
5. **5. Close the loop on the failed guess** — Return to Ricci = κT: conservation plus the identity forces ∇R = 0, so the trace of T must be the same everywhere; inside a star the trace is −ρ + 3p, outside it is zero, contradiction. *Why:* Completes the motivating story with a concrete physical contradiction. *(GA ch13 §13.3 p.147)*
6. **6. What the identity does for the field equations** — Count ten equations, four identities, four coordinate functions; show one concrete redundancy (the angular Schwarzschild equation, or the Friedmann equations implying the fluid equation) and, for advanced learners, how constraints propagate. *Why:* Shows the identity is a working tool, not only a consistency check, and prepares gauge freedom and initial-value ideas. *(SCH ch08 §8.2 p.187; DIV ch13 §13.2 p.218; DIV ch15 §15.5 p.277; DIV ch24 §24.9 p.500; DIV ch13 §13.6 p.228)*
7. **7. Why it had to exist** — For advanced learners, show that relabelling points cannot change a scalar action, so the metric Euler-Lagrange tensor must be divergence-free for any Lagrangian; for √−g R this reproduces the identity. *Why:* Replaces 'a lucky identity' with 'a consequence of coordinate invariance', which also explains why Lovelock-type uniqueness is plausible. *(DIV ch11 §11.2 p.188; legacy:manuscript-section-15-noether-killing-charges-redshift)*

## Analogies

- **Two ledgers that may only be equated if both balance** (intuition): Matter's energy-momentum ledger balances at every point. A law 'geometry = matter' needs a geometric ledger that also balances at every point for every geometry; the Einstein tensor is that ledger, and the contracted identity is its balancing rule. *Limits:* Balance here is local; in curved spacetime it does not generally sum to a conserved global total, and the analogy says nothing about the size of the coupling constant. *(SCH ch08 §8.1 p.184; legacy:manuscript-chapter-appendix-b-reference-sheet)*
- **Incompressible flow through a narrowing pipe** (intuition): The flow speed changes along the pipe, yet no fluid is created anywhere: divergence zero, not constant. The Einstein tensor likewise varies (large inside a star, zero outside) while its divergence vanishes. *Limits:* A vector-field divergence is a simpler object than the covariant divergence of a rank-two tensor, which includes connection terms and yields four equations rather than one. *(legacy:manuscript-section-09-bianchi-einstein-tensor)*
- **Charge conservation built into Maxwell's equations** (working): Taking the divergence of ∂_μ F^μν = 4π J^ν gives zero on the left identically (F is antisymmetric), so Maxwell's equations only make sense for conserved currents. Einstein's equation has the same structure: the left side's divergence vanishes identically, so the source must be conserved. *Limits:* In electromagnetism the identity comes from antisymmetry of F and holds in one line; in gravity it needs the full Bianchi identity and metric compatibility, and the conserved quantity is a tensor, not a vector. *(GA ch43 §43.3 p.471; GA ch43 Ex 43.5)*
- **A coordinate relabelling as a variation that cannot change anything** (formal): Sliding the coordinate labels around inside a region changes the metric components but not the action; demanding that the action's response vanish for every such slide yields a divergence-free Euler-Lagrange tensor, without ever choosing the Lagrangian. *Limits:* Requires a genuinely scalar Lagrangian density and discarded boundary terms; it does not apply directly to non-covariant first-order Lagrangians. *(DIV ch11 §11.2 p.188)*

## Misconceptions

- **∇_μ G^μν = 0 means the Einstein tensor is constant (or covariantly constant) throughout spacetime.** — Zero divergence is four equations about a particular combination of derivatives; the components can vary strongly. Inside a star G_tt tracks the density; outside it is zero. Covariantly constant would be ∇_λ G_μν = 0, a far stronger (40-equation) condition. *Why tempting:* Learners hear 'the derivative of G vanishes' and drop the word divergence. *Diagnostic:* For a static star, G_t̂t̂ = 8πρ(r) with ρ largest at the centre and zero outside. Is that compatible with ∇_μ G^μν = 0? What exactly does the identity forbid? *(legacy:manuscript-section-09-bianchi-einstein-tensor)*
- **Energy-momentum conservation uniquely forces G_μν = κ T_μν.** — Conservation only requires the geometric side to be divergence-free. Λ g_μν is also divergence-free, and matching divergences does not by itself imply proportionality; uniqueness of a G + b g among local second-order tensors in four dimensions is Lovelock's theorem, an extra input. *Why tempting:* The chain of identities in textbooks reads like a derivation of the field equation. *Diagnostic:* Name a second symmetric tensor built from the metric alone whose divergence vanishes identically. What does its existence say about the claim that conservation determines the field equation? *(DIV ch10 §10.8 p.184; legacy:manuscript-section-12-trace-subtraction-and-reversal)*
- **Since the Einstein tensor is divergence-free by geometry, matter conservation is a consequence of geometry alone, whatever matter does.** — The identity holds off shell and says nothing about matter until the field equation links G to T. Matter conservation also follows independently from the matter field equations (diffeomorphism invariance of the matter action); the field equation is consistent only because both hold. *Why tempting:* Slogans like 'the Bianchi identity encodes energy conservation' blur identity and equation of motion. *Diagnostic:* Suppose you write down a stress-energy tensor for a fluid that does not obey its equations of motion, and a metric chosen at random. Does ∇_μ G^μν = 0 still hold? Does ∇_μ T^μν = 0? *(legacy:manuscript-section-15-noether-killing-charges-redshift; SCH ch06 §6.6 p.164)*
- **∇_μ T^μν = 0 in curved spacetime means the total energy of a system (or of the universe) is conserved.** — The covariant statement is local. Because of the connection terms it cannot in general be integrated into a conserved global total; conserved charges exist only with symmetries such as Killing vectors, or asymptotically. In an expanding universe the energy in a comoving volume of radiation decreases. *Why tempting:* In flat spacetime ∂_μ T^μν = 0 does integrate to conserved totals, and the notation looks identical. *Diagnostic:* A comoving box of radiation in an expanding universe obeys ρ ∝ a⁻⁴ while its volume grows as a³. Is the energy in the box constant? Does that contradict ∇_μ T^μν = 0? *(legacy:manuscript-chapter-appendix-b-reference-sheet; DIV ch24 §24.9 p.500)*
- **Ten Einstein equations for ten metric components means the equations determine all ten components from initial data.** — The four contracted identities make four combinations of the equations redundant as evolution equations (they become constraints on initial data), and four metric functions are coordinate choices that no equation can fix. Six equations govern six geometric functions. *Why tempting:* Counting equations against unknowns is how one checks well-posedness in simpler theories. *Diagnostic:* If the equations did determine all ten g_μν from initial data, what would that say about our freedom to change coordinates to the future of the initial slice? *(SCH ch08 §8.2 p.187; DIV ch13 §13.2 p.218)*

## Thought experiments

- **A universe obeying Ricci = κT**: Assume the tempting field equation R_μν = κT_μν, conserved matter, and the contracted identity. Apply them to a single star surrounded by empty space. *Lesson:* Conservation kills the divergence of Ricci, so the identity forces ∇R = 0; tracing the guess then forces the trace of T to be the same everywhere. The trace is −ρ + 3p inside the star and zero outside, so the guess is incompatible with any lumpy universe; the half-trace term of the Einstein tensor is what removes the contradiction. *(GA ch13 §13.3 p.147)*

## Visualizations

### Divergence-residual slider · interactive-plot · high priority

The learner builds a candidate geometric side R^μν + B g^μν R + Λ g^μν and loads a spacetime. A plot shows the divergence residual, which equals (½ + B)∇^ν R, across the spacetime; it vanishes everywhere only at B = −½ regardless of Λ.

**Interaction:** Slide B and Λ; switch between an FLRW dust universe (residual as a function of time), a constant-density star interior matched to vacuum (residual as a function of radius), and a user-drawn bump metric. A 'predict first' prompt asks for the value of B before the slider unlocks.

**Model:** For FLRW dust with Λ = 0 the course conventions give R = 8πρ ∝ a(t)⁻³, so the residual's time component is proportional to (½ + B)∂_t R; for the star, R = 8π(ρ − 3p(r)) inside and 0 outside; general metrics use the finite-difference curvature engine.

**Inspired by:** SCH ch08 §8.1 p.184; GA ch13 §13.3 p.145

**Legacy assets:** engine-independent-curvature-checker, manuscript-section-12-trace-subtraction-and-reversal

### The Ricci guess meets a star · interactive-2d · high priority

A density map of a star in empty space with two hypotheses. Under Ricci = κT the app computes the trace of T that the identity would require to be uniform and paints the mismatch; under G = κT the map is consistent.

**Interaction:** Drag the star's radius and central density, add pressure, toggle between the two hypotheses; a readout shows T inside and outside and the implied constant that the Ricci guess demands.

**Model:** Perfect-fluid trace T = −ρ + 3p (course signature), zero in vacuum; the contradiction is the non-constancy of T.

**Inspired by:** GA ch13 §13.3 p.147

### Ten-equation ledger · interactive-2d · medium priority

Ten tiles for the metric components and ten for the Einstein equations. The learner drags four 'identity' tokens onto equation tiles, which turn into constraint tiles attached to the initial slice, and four 'coordinate' tokens onto metric tiles, leaving six evolving pairs.

**Interaction:** Drag tokens; a coordinate-grid inset shows the four free functions changing g_μν to the future of the slice without changing geometry; an optional step animates constraints staying zero under evolution.

**Inspired by:** SCH ch08 §8.2 p.187; DIV ch13 §13.2 p.218; DIV ch13 §13.6 p.228

**Legacy assets:** manuscript-chapter-12-einstein-field-equation

### Friedmann equations already know about energy · interactive-plot · low priority

Two Friedmann equations drive a(t); the app separately integrates the fluid equation ρ̇ = −3H(ρ + p) and overlays both density histories, which coincide because of the identity.

**Interaction:** Choose w for the fluid and Λ; break the identity deliberately by editing the coefficient in G_t̂t̂ and watch the two histories diverge.

**Model:** Flat FLRW: H² = 8πρ/3 + Λ/3 and −2ä/a − H² = 8πp − Λ with p = wρ, G = c = 1.

**Inspired by:** DIV ch24 §24.9 p.500

**Legacy assets:** manuscript-section-19-1-friedmann-derivation

## Worked examples

- **Contracting the Bianchi identity twice** (working): The two traces, the role of metric compatibility and antisymmetry signs, and the rearrangement into the divergence-free Einstein tensor. *(SCH ch06 §6.6 p.163; GA ch13 Example 13.3 §13.3 p.146)*
- **Fixing the coefficient of g R in the field equations** (working): Requiring the divergence of the general candidate to vanish for every metric forces the one-half, while the cosmological term survives. *(SCH ch08 §8.1 p.184)*
- **Refuting Ricci = κT** (working): Conservation plus the identity forces a constant trace of T, contradicting a non-uniform universe. *(GA ch13 §13.3 p.146)*
- **Counting independent Einstein equations** (working): Ten components, four identities and four coordinate functions leave six geometric equations. *(SCH ch08 §8.2 p.187; DIV ch13 §13.2 p.218)*
- **Constraints propagate** (formal): With the evolution equations satisfied, the identity becomes a homogeneous first-order system for the constraint quantities, so vanishing initial constraints remain zero. *(DIV ch13 §13.6 p.228)*
- **The angular Schwarzschild equation comes for free** (working): In solving the spherical vacuum equations, the identity makes the angular component redundant once the other three hold. *(DIV ch15 §15.5 p.277)*
- **Friedmann equations imply the fluid equation** (working): Differentiating the first Friedmann equation and using the second recovers energy conservation of the cosmic fluid, as the identity guarantees. *(DIV ch24 §24.9 p.500; legacy:manuscript-section-19-1-friedmann-derivation)*
- **Contracted identity from coordinate invariance of the action** (formal): Any scalar metric Lagrangian has a divergence-free Euler-Lagrange tensor; for the Einstein Lagrangian this is minus √−g times G. *(DIV ch11 §11.2 p.188; DIV ch11 (11.29) §11.4 p.192)*

## Exercises

- (intro) Fill in the index algebra from the Bianchi identity through the once- and twice-contracted forms to the divergence-free Einstein tensor. *Skill:* contraction with metric compatibility and antisymmetry *(SCH ch06 Ex 6.27; DIV ch06 Ex 6.25)*
- (standard) Show that the angular vacuum equation for the general spherically symmetric metric follows from the other three via the contracted identities. *Skill:* using the identity to eliminate redundant equations *(DIV ch15 Ex 15.9)*
- (challenging) Write the identity in coordinates for the constraint components, show it is a homogeneous first-order system, and argue that zero data give zero solution. *Skill:* constraint propagation *(DIV ch13 Ex 13.10)*
- (challenging) Use the contracted identity and metric compatibility to show that a maximally symmetric curvature tensor must have a constant coefficient. *Skill:* Schur-type argument *(GA ch16 Ex 16.5)*
- (standard) Show that the flux of the dual Einstein tensor through any closed 3-boundary vanishes. *Skill:* Stokes theorem with tensor-valued forms *(GA ch43 Ex 43.5)*
- (challenging) Track which terms of the contracted identities vanish to prove that the trivial and supplementary equations of the characteristic problem need only hold on one surface. *Skill:* structural reasoning with the identity in a null-coordinate problem *(DIV ch23 Ex 23.6)*
- (standard) Recompute the variational derivative of the Einstein Lagrangian with different choices of independent metric variables and state the identity each satisfies. *Skill:* generalized Bianchi identity from the action *(DIV ch11 Ex 11.7)*

## Checks for understanding

- **Q (intuition):** Inside the Sun the Einstein tensor is large and in the space around it essentially zero. Does that violate the statement that the divergence of the Einstein tensor vanishes?
  - **A:** No. Zero divergence means no creation or destruction at any point (four balance equations), not that the tensor is the same everywhere, just as an incompressible flow can speed up in a narrow pipe. The identity would be violated only if the particular combination of derivatives in ∇_μ G^μν failed to cancel, which never happens for any metric. *(targets: ∇_μ G^μν = 0 means the Einstein tensor is constant.)*
- **Q (working):** Show that R^μν + B g^μν R + Λ g^μν, with B a constant, is divergence-free for every metric only when B = −½.
  - **A:** Take ∇_ν. Metric compatibility kills ∇_ν(Λ g^μν) and lets g pass through: ∇_ν(B g^μν R) = B ∇^μ R. The contracted identity gives ∇_ν R^μν = ½∇^μ R. The total is (½ + B)∇^μ R. Since generic metrics have ∇R ≠ 0, the divergence vanishes identically only if B = −½; Λ is unconstrained.
- **Q (working):** Use the flat FLRW equations H² = 8πρ/3 and −2ä/a − H² = 8πp (G = c = 1, Λ = 0) to show ρ̇ = −3H(ρ + p), and say why this had to work.
  - **A:** Differentiate the first: 2HḢ = (8π/3)ρ̇. With ä/a = Ḣ + H², the second gives −2Ḣ − 3H² = 8πp, so Ḣ = −(8πp + 3H²)/2 = −4π(ρ + p) after using 3H² = 8πρ. Then ρ̇ = (3/8π)·2H·(−4π)(ρ + p) = −3H(ρ + p). It had to work because the contracted Bianchi identity makes the divergence of G vanish identically, so the field equations imply ∇_μ T^μν = 0, whose time component for a comoving perfect fluid is exactly this equation.
- **Q (working):** Someone argues: 'T is conserved and G is divergence-free, therefore G must equal κT.' Give the flaw in one or two sentences.
  - **A:** Two divergence-free tensors need not be proportional; for example Λ g_μν is also divergence-free, so G + Λg = κT is equally consistent. Singling out the form a G + b g among local tensors built from the metric and two derivatives requires Lovelock's theorem, not conservation alone. *(targets: Energy-momentum conservation uniquely forces G_μν = κ T_μν.)*
- **Q (formal):** Why does the second contraction need the metric to be covariantly constant, while the uncontracted Bianchi identity does not?
  - **A:** Contracting σ with ν inside ∇_λ R^ρ_σμν requires moving g^σν through the covariant derivative, which is allowed only if ∇g = 0; it also uses the pair symmetry R_ρσμν = R_μνρσ, which holds for the Levi-Civita connection. The uncontracted identity uses only Γ(P) = 0 in suitable coordinates, available for any torsion-free connection.
- **Q (working):** A comoving box of radiation in an expanding universe loses energy (ρ ∝ a⁻⁴ while volume ∝ a³). Does that contradict ∇_μ T^μν = 0?
  - **A:** No. The covariant conservation law is local and includes connection terms; for FLRW it reads ρ̇ = −3H(ρ + p), which for p = ρ/3 gives exactly ρ ∝ a⁻⁴. The energy in the box decreases because the radiation does work p dV on the expanding volume; there is no general global energy conservation in a time-dependent spacetime. *(targets: ∇_μ T^μν = 0 means the total energy of a system is conserved.)*

## Applications

- **Selecting the geometric side of Einstein's equation**: The identity is the step that turns 'curvature proportional to matter' into the specific combination R_μν − ½ R g_μν, with Λ allowed. *(SCH ch08 §8.1 p.184; GA ch13 §13.4 p.147)*
- **Numerical relativity and the initial-value problem**: Because the identity propagates constraints, simulations solve the constraints once on the initial slice and then evolve; in practice numerical errors violate the constraints, and monitoring them is a standard accuracy check. *(DIV ch13 §13.6 p.228; SCH ch08 §8.2 p.187)*
- **Cutting work in exact-solution calculations**: In spherical symmetry and cosmology one component of the field equations can be skipped: the angular Schwarzschild equation and the second Friedmann equation (given the fluid equation) follow from the rest. Schutz uses the same shortcut: the angular static-star equation is redundant, and only the time-time Robertson-Walker component is needed. *(DIV ch15 §15.5 p.277; DIV ch24 §24.9 p.500; SCH ch10 (10.16) §10.2 p.271; SCH ch13 (13.51) §13.3 p.439)*

## History

- **Aurel Voss (1880):** A contracted version of the identity was derived by Voss, decades before its use in gravitation. *(GA ch43 p.467)*
- **Albert Einstein (1915):** Einstein's Prussian Academy papers of 4 and 11 November 1915 equated the Ricci tensor to matter (the Gifted Amateur margin note dates the proposal to October); the version with the half-trace term, compatible with conservation, followed on 25 November. *(GA ch13 §13.3 p.145)*

## Tutor guidance

**Opening questions**

- If energy and momentum are conserved locally, what must be true of anything we set equal to the stress-energy tensor?
- Can a vector field be divergence-free and still change from place to place? Give an example.
- Why might 'Ricci proportional to T' be the first thing anyone would try?

**Common questions**

- *Which contraction is 'the' contracted Bianchi identity?* — In this course it is the twice-contracted one: the divergence of Ricci equals half the gradient of R, which is the same as the divergence of the Einstein tensor vanishing. Schutz reserves 'contracted' for the intermediate once-contracted form, so watch the wording when reading him.
- *Does the identity prove energy is conserved?* — Not on its own. It is true for every metric. Only when we impose Einstein's equation does it force the stress-energy tensor to be conserved; matter theories also conserve their own stress-energy through their equations of motion. The identity makes the two stories compatible.
- *Why doesn't the cosmological constant spoil the argument?* — Because the metric is covariantly constant, its divergence is zero, so Λ times the metric can be added to the Einstein tensor without breaking the balance. Conservation cannot tell us whether Λ is zero; observation does.
- *If four equations are redundant, which ones can I drop?* — The identity relates derivatives of the components, so you usually keep the equations that are easiest to solve and let the identity guarantee the rest, provided some mild conditions hold (for example that the relevant coefficient does not vanish). In spherical symmetry one drops the angular equation; in cosmology one can drop the acceleration equation if the fluid equation is used.

**Pitfalls when explaining**

- Do not say 'the Einstein tensor is conserved' without adding 'its divergence vanishes'; learners hear 'constant'.
- Always name the two ingredients of the second contraction, ∇g = 0 and Riemann's pair symmetry, or the step looks like sleight of hand.
- Do not claim conservation derives the field equation uniquely; mention Λ and, for advanced learners, Lovelock.
- Keep local and global conservation separate; do not let ∇T = 0 slide into 'total energy is conserved'.
- Watch the letter G: say 'Einstein tensor' and 'Newton's constant' in words when both could appear.

**When to show a demo**

- Right after stating the identity, ask the learner to predict the special coefficient and then open the divergence-residual slider.
- When the learner accepts Ricci = κT, show the star demo before explaining why it fails.
- Use the ten-equation ledger when a learner asks how ten equations can fail to determine ten unknowns.

**Saying it aloud:** Say the key relation as 'the divergence of the Ricci tensor equals one half the gradient of the Ricci scalar.' For the Einstein form: 'nabla mu of G upper mu nu equals zero: the Einstein tensor has zero divergence, for every metric.' When deriving, narrate each contraction as 'trace the first index against the third' and 'trace again with the inverse metric, which slides through the derivative because the metric is covariantly constant.' Avoid saying 'G is conserved' alone; say 'G is divergence-free.'

## Sources

- schutz ch06 (developed): p.163 §6.6
- schutz ch08 (core): p.184 §8.1, p.187 §8.2
- gifted-amateur ch13 (developed): p.145 §13.3, p.146 §13.3, p.147 §13.3
- gifted-amateur ch43 (mention): p.467, p.475
- dinverno ch06 (core): p.106 §6.12
- dinverno ch10 (revisited): p.184 §10.8
- dinverno ch11 (revisited): p.188 §11.2, p.192 §11.4, p.193 §11.5
- dinverno ch13 (core): p.218 §13.2, p.222 §13.4, p.228 §13.6, p.230 §13.7
- dinverno ch15 (revisited): p.277 §15.5
- dinverno ch23 (developed): p.467 §23.5, p.470 §23.6
- dinverno ch24 (revisited): p.493 §24.7, p.500 §24.9
- legacy manuscript-section-09-bianchi-einstein-tensor (developed)
- legacy manuscript-section-12-trace-subtraction-and-reversal (developed)

## Review

**Verdict:** fixed

**Fixes**

- Symbol clash: the half-trace coefficient was called a in the same note, demo and FLRW model that use the scale factor a(t); renamed it B throughout (working level, picture, key equation, teaching path, slider demo, check 2).
- History: replaced the 'October 1915' date for the Ricci-equals-matter proposal with the 4 and 11 November 1915 papers (the GA dossier flags the October date as a margin-note error) and gave 25 November for the final equation.
- Formal level (iv) was garbled ('forces the Einstein constant in G = -Λg type situations'); rewrote it as two correct Schur-type statements with the (1 - n/2)∇f = 0 step.
- Summary no longer says only six of ten components are independent; it now says four combinations cannot be independent evolution equations, which matches the misconception entry.
- Added the Schutz uses of the identity from the evidence (redundant angular static-star equation, Eq. 10.16; only the FRW time-time component, Eq. 13.51) to the exact-solution application.

**Concerns**

- Worked every check: the coefficient argument, the flat FLRW derivation of ρ̇ = -3H(ρ + p), the radiation-box answer, and the second-contraction reasoning are all correct. Re-derived the double contraction by hand.
- The constraint-propagation key equation is quoted in d'Inverno's index scheme (Latin 0-3, Greek 1-3); the note says so, and it does not depend on signature.
- The per-domain _index.md was not regenerated in this review.
