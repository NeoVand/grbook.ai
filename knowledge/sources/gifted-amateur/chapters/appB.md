---
type: "source-unit"
book: "gifted-amateur"
book_short: "GA"
unit: "appB"
title: "Conventions and notation"
part: null
printed_pages: [562, 564]
pdf_pages: [579, 581]
math_level: 2
conceptual_level: 2
novice_friendliness: 2
style_tags: ["survey-overview", "conversational-informal", "spiral-revisit"]
concepts: ["Heaviside-Lorentz units", "Maxwell's equations", "natural units with c = 1", "passive transformation", "active transformation", "3-vector notation", "4-vector", "coordinate basis vectors", "1-form", "gradient 1-form and comma notation", "Einstein summation convention", "pairing of a 1-form with a vector", "scalar product via the metric", "covariant and contravariant components", "tensor as slot machine", "tensor valence (n, m)", "component extraction by inserting basis vectors and 1-forms", "tensor product", "wedge product", "symmetrization and antisymmetrization brackets", "trace of a tensor", "ordered index sum notation", "metric tensor", "determinant of the metric", "metric signature (-+++)", "index raising and lowering", "invariant volume elements", "tensor field", "manifold point versus coordinates", "four-velocity", "affine parameter", "displacement-vector description of tangent vectors", "tangent vector as derivative operator", "orthonormal frame components", "vielbein", "square-root rule for diagonal metrics", "covariant derivative", "nabla_mu as a directional label", "semicolon notation", "connection coefficients", "covariant derivative along a curve", "coordinate-free, mixed and coordinate notation", "general matrix notation"]
verification: "fixed"
---

# GA appB · Conventions and notation

> A three-page reference card that fixes the book's unit system (Heaviside-Lorentz for electromagnetism, c = 1), its typography for 3-vectors, 4-vectors, 1-forms, tensors and orthonormal-frame components, its index rules (summation, symmetrization brackets, trace, signature -+++), the two ways it writes tangent vectors, the vielbein bracket notation, and the several interchangeable notations for the covariant derivative.

**Pages:** printed 562–564 · pdf 579–581 · **Difficulty:** math 2/5, conceptual 2/5, novice-friendliness 2/5

No new derivations: every item is a single-line definition. Mathematical content is light, but the appendix is dense, assumes the reader has already met every object in the body of the book, and relies heavily on typography (bold, tilde, script, hats, underlines) that is easy to lose. A handful of printed slips (repeated index in B.3, 'tensors' for vectors in the pairing, 1...4 index range, a dot for a contraction in the directional derivative, a partial for a total derivative in note 9, and the covariant/contravariant naming) can confuse a novice who uses it as an authority.

## Role in the book

Placed after all fifty chapters and the further-reading list, this appendix is not a teaching chapter but a lookup table that stitches together notation introduced piecemeal across the spiral structure: 4-vectors and summation (Part I), slot-machine tensors and the metric (Chapters 4-5), covariant derivatives and D/dtau (Chapter 7), vielbeins and hatted orthonormal components (Chapter 10), the classical displacement-vector picture (Chapter 30), vectors as derivative operators and wedge products (Part V), and Heaviside-Lorentz units for the field-theory chapters of Part VI. Its margin notes also carry clarifications not stated so compactly elsewhere, such as passive versus active transformations, why a tensor field's argument is not a slot, and why nabla_mu is not a component.

## Learning objectives

- Reader can explain how Heaviside-Lorentz units differ from SI and Gaussian units, and rewrite Maxwell's equations and the point-charge potential in Heaviside-Lorentz form, with or without c = 1.
- Reader can distinguish a passive transformation (relabel the event's coordinates) from an active one (move the event) and say which one the book uses.
- Reader can read the book's typography at a glance: arrowed 3-vectors with Roman indices, bold 4-vectors with Greek indices, bold tilded 1-forms with lower indices, hatted orthonormal components, and an underlined bold matrix.
- Reader can expand vectors, 1-forms and a general (n, m) tensor on basis vectors and basis 1-forms, and extract components by filling the slots with basis objects.
- Reader can apply the summation, symmetrization, antisymmetrization, trace and ordered-index conventions, and relate the wedge product to the antisymmetrization bracket (including the factor of 2).
- Reader can state the metric conventions: signature (-+++), eta = diag(-1,1,1,1), g for the determinant rather than the trace, and index raising/lowering with the metric (or eta for hatted indices).
- Reader can explain why a tensor field's position argument is not one of its slots, and why points and their coordinates are not treated as vector components in curved spacetime.
- Reader can write the 4-velocity as the tangent to a world line, check its normalization u.u = -1, and compare the displacement-vector and derivative-operator expressions for a tangent vector.
- Reader can convert components between coordinate and orthonormal frames with the vielbein, and build an orthonormal frame for a diagonal metric using the square-root rule.
- Reader can translate between nabla_u v, (nabla_mu v)^alpha, v^alpha_{;mu} and (Dv/dtau)^alpha, and explain why nabla_mu labels a direction rather than a component.

## Assumed background

- Maxwell's equations in SI form and the Coulomb potential — electromagnetism
- Bases, components and change of basis for vectors; matrices and determinants — linear-algebra
- Partial derivatives and the multivariable chain rule — undergrad-calculus
- 4-vectors, Minkowski metric and the summation convention — earlier-in-this-book (GA ch02)
- 1-forms and tensors as linear slot machines — earlier-in-this-book (GA ch04)
- Metric tensor, its determinant and invariant volume elements — earlier-in-this-book (GA ch05)
- Covariant derivative, connection coefficients, comma and semicolon notation, derivative along a curve — earlier-in-this-book (GA ch07 §7.3-7.4, ch09)
- Orthonormal frames and the vielbein — earlier-in-this-book (GA ch10 §10.2-10.3)
- Classical curve theory with displacement vectors X — earlier-in-this-book (GA ch30 §30.2)
- Vectors as derivative operators, tensor and wedge products, ordered index sums — earlier-in-this-book (GA ch31-32)

## Teaching approach

A compact glossary written in the book's usual chatty register: each convention is stated once with a short equation, while cautions, alternative usages in other books and conceptual clarifications are pushed into ten margin notes. The ordering follows the growth of the objects: units first, then 3-vectors, 4-vectors, 1-forms, products and tensors, then fields on a manifold, frames, and finally derivatives. Coordinate-free (bold) and component forms are always given side by side, and the appendix repeatedly flags where the notation itself can mislead.

**Style:** survey-overview, conversational-informal, spiral-revisit

**Narrative arc**

1. State that the appendix gathers the book's notational choices.
2. Motivate Heaviside-Lorentz units by the wish for uncluttered field-theory equations; contrast Maxwell in SI (B.1) with Heaviside-Lorentz (B.2) and add c = 1.
3. Define 3-vectors by their basis-dependent components and basis-independent length; fix arrow typography, Roman indices and upstairs placement; margin note on passive transformations.
4. Promote to 4-vectors in (3+1) dimensions: bold symbols as basis-free objects, Greek indices, v = v^mu e_mu.
5. Introduce the 1-form as the vector's partner (bold tilde, lower indices, basis omega^mu or dx^mu), with the gradient and comma notation as the familiar example.
6. Fix summation, the pairing bracket and the metric dot product.
7. Describe tensors as slot machines with valence (n, m), component extraction, outer and wedge products, and the full basis expansion (B.3).
8. List index housekeeping: symmetrization (B.4), antisymmetrization (B.5), trace, coordinate versus numeric index labels, ordered index pairs; margin note on the metric, its determinant and the signature.
9. Move to fields on a manifold: a vector field's argument is a point, not a slot; points and coordinates are not vector components; the 4-velocity is the tangent to a world line with u.u = -1; margin note compares the old displacement-vector tangent (B.6) with the modern derivative-operator tangent (B.7).
10. Introduce hatted orthonormal components, raising with eta, vielbein conversion rules (B.8) and the square-root rule for diagonal metrics.
11. Close with the covariant derivative: directional form, nabla_mu as shorthand for a basis direction, component and semicolon forms (B.9-B.10), and the derivative along a curve (B.11), with a margin note sorting out coordinate-free, mixed and coordinate notation.

**Signature moves**

- Pairs every basis-free bold expression with its component counterpart, so notation encodes the difference between an object and its representation.
- Uses a crime-scene joke (attributed to Sidney Coleman) to separate passive 'alias' from active 'alibi' transformations.
- Explicitly warns where the notation lies: nabla_mu looks like a component but is a direction label; Dv^mu/dtau looks like a derivative of a component but is not, so the book writes (Dv/dtau)^mu.
- Separates the round-bracket argument of a field (where it lives) from its empty slots (what it eats).
- Shows two generations of the tangent-vector formalism side by side (displacement vector of Chapter 30 versus derivative operator of Chapter 31) and says why the older one fails in GR.
- Offers a practical shortcut, the square-root rule, for reading off vielbein components of a diagonal metric.
- Flags where other textbooks differ (Jackson and Landau-Lifshitz on units, dOmega for volume, the D/dtau ambiguity) rather than presenting its choices as universal.

## Section by section

### Appendix opening — p.562 (pdf 579)

A single sentence announcing that the appendix records the conventions and symbols chosen throughout the book; the side table of contents lists the three sections.

**Key moves**
- Frames the appendix as a reference summary rather than new material.

### §B.1 Electromagnetic units — p.562 (pdf 579)

Shows Maxwell's equations in SI form and explains that, to keep field-theory equations as clean as possible, the book adopts Heaviside-Lorentz (rationalized Gaussian) units, in which the SI constants epsilon_0 and mu_0 disappear. The point-charge potential keeps its 1/(4 pi) but loses epsilon_0, Maxwell's equations acquire 1/c factors, and the book's additional choice c = 1 removes those too. Margin notes observe that field-theory books nearly all use these units while the classic electrodynamics texts of Jackson and of Landau-Lifshitz do not, and identify Heaviside and Lorentz.

**Concepts:** Heaviside-Lorentz units, natural units with c = 1, Maxwell's equations

**Key moves**
- Write Maxwell's equations in SI units (B.1).
- Justify a different unit system by the simplicity of field-theory equations.
- Describe Heaviside-Lorentz units as obtained from SI by removing epsilon_0 and mu_0, illustrated with the Coulomb potential q/(4 pi |x|).
- Write Maxwell's equations with explicit 1/c factors (B.2), then set c = 1.

### §B.2 Vectors, 1-forms and tensors: 3-vectors, 4-vectors and 1-forms — p.562 (pdf 579)

A vector is characterized by components that change under a rotation of basis while its length does not. Three-vectors carry an arrow, Roman indices i = 1, 2, 3 (or coordinate names x, y, z) and always upstairs indices. A margin note fixes transformations as passive and gives Coleman's alias/alibi image; another comments on the covariant/contravariant naming. In (3+1) dimensions 4-vectors are bold, basis-independent objects with Greek indices mu = 0..3, a timelike 0-component and a spatial 3-vector part, expanded as v = v^mu e_mu with e_mu sometimes written as a partial derivative. The 1-form is introduced as the vector's partner: bold with a tilde, lower-index components, basis 1-forms omega^mu or dx^mu; the gradient of a function, with components partial_mu f = f_{,mu}, is the standard example. The summation convention, the angle-bracket pairing of a 1-form with a vector, and the metric dot product of two vectors close this part. Margin notes fix script V for 4-volume, italic V for 3-volume, dSigma for the invariant 3-volume, and reserve dOmega for the angular line element.

**Concepts:** passive transformation, 3-vector notation, 4-vector, coordinate basis vectors, 1-form, gradient 1-form and comma notation, Einstein summation convention, pairing of a 1-form with a vector, scalar product via the metric, covariant and contravariant components, invariant volume elements

**Key moves**
- Define a vector operationally: components depend on the basis, length does not.
- Encode object type in typography: arrow for 3-vectors, bold for 4-vectors, bold tilde for 1-forms.
- Encode object type in index height: vector components up, 1-form components down.
- Expand on bases: v = v^mu e_mu and A = A_mu omega^mu.
- Give the gradient as the prototype 1-form and introduce the comma for partial derivatives.
- Distinguish the metric-free pairing <A, v> = A_mu v^mu from the metric dot product g_{mu nu} v^mu u^nu.

### §B.2 Vectors, 1-forms and tensors: tensors and index operations — p.563 (pdf 580)

Tensors are slot machines with bold symbols and empty argument slots; a valence (n, m) means n 1-form slots and m vector slots, and filling every slot returns a number. Components come from feeding in basis 1-forms and basis vectors, as illustrated for a (2,2) tensor. Tensors combine by the outer product and by the wedge product, the latter defined without a factor of one half, and any tensor can be expanded over outer products of basis objects (B.3). Round and square brackets denote symmetrization and antisymmetrization with a factor of one half (B.4-B.5). The trace is written with the italic letter of the tensor, indices may be coordinate names or numbers, and a pair of indices inside vertical bars is summed only in increasing order. The margin notes add that general matrices are written as an underlined bold letter, and that the metric is the key (0,2) tensor, whose components are dot products of basis vectors, whose determinant (not trace) is called g, whose signature is (-+++), and which raises and lowers indices.

**Concepts:** tensor as slot machine, tensor valence (n, m), component extraction by inserting basis vectors and 1-forms, tensor product, wedge product, symmetrization and antisymmetrization brackets, trace of a tensor, ordered index sum notation, metric tensor, determinant of the metric, metric signature (-+++), index raising and lowering

**Key moves**
- Specify tensors by what they accept (n 1-forms, m vectors) and what they return (a number).
- Recover components by inserting basis objects into the slots.
- Define v wedge u as v tensor u minus u tensor v.
- Expand a (2,2) tensor on basis products (B.3).
- Fix bracket notation with the factor 1/2 (B.4, B.5).
- Note the exception that g is the metric determinant, not its trace.

### §B.2 Vectors, 1-forms and tensors: fields, world lines and orthonormal frames — p.564 (pdf 581)

Tensor fields depend on position: v(x) is the vector the field assigns to the point x, where x may be the abstract manifold point P or its coordinates x^mu(P), and the bracket is deliberately different from a slot. Because displacement arrows between spacetime points do not survive in curved spacetime, the book specifies points and their coordinates instead, and does not regard coordinates as vector components. The 4-velocity is the key vector field: the tangent to a world line x^mu(tau) with affine parameter tau, normalized to u.u = -1. A margin note contrasts the Chapter 30 approach, which differentiates a displacement vector X to get the tangent and basis vectors (B.6) but fails the tensor transformation law, with the Chapter 31 approach, which writes the tangent as a derivative operator so that e_mu = partial/partial x^mu (B.7). Components in an orthonormal frame wear hats, their indices move with eta, and conversion to a coordinate frame uses vielbein components written in brackets (B.8); for a diagonal metric, the relevant vielbein component is the square root of the modulus of the diagonal metric component.

**Concepts:** tensor field, manifold point versus coordinates, four-velocity, affine parameter, displacement-vector description of tangent vectors, tangent vector as derivative operator, orthonormal frame components, vielbein, square-root rule for diagonal metrics

**Key moves**
- Separate a field's position argument from its slots.
- Replace position vectors with points P and coordinates x^mu(P).
- Define the 4-velocity as the tangent u = (dx^mu/dtau) e_mu with u.u = -1.
- Contrast the displacement-vector tangent (B.6) with the derivative-operator tangent (B.7).
- Give the four vielbein conversion rules for vector and 1-form components (B.8).
- State the square-root rule (e_mu)^{mu-hat} = sqrt|g_{mu mu}| for diagonal metrics.

### §B.3 Covariant derivatives — p.564 (pdf 581)

The covariant derivative nabla_u is the directional derivative along a vector u; along a basis direction it is abbreviated nabla_mu, which the appendix warns is a direction label and not a component index. Expanded on a basis, nabla_mu v has components (nabla_mu v)^alpha, equivalently written with the semicolon v^alpha_{;mu}, defined as the partial derivative plus a connection term (B.9-B.10). Along a curve x^mu(tau) with tangent u the book writes Dv/dtau = nabla_u v, whose components contract u with the semicolon derivative (B.11). A closing margin note sorts the notations into coordinate-free, mixed and coordinate forms and explains that the book writes (Dv/dtau)^mu rather than the ambiguous Dv^mu/dtau used by some authors.

**Concepts:** covariant derivative, nabla_mu as a directional label, semicolon notation, connection coefficients, covariant derivative along a curve, coordinate-free, mixed and coordinate notation

**Key moves**
- Define nabla_u as a directional derivative and nabla_mu as the special case u = e_mu.
- Warn that the mu on nabla_mu is not a component index.
- Write nabla_mu v = (nabla_mu v)^alpha e_alpha = v^alpha_{;mu} e_alpha (B.9).
- Define v^alpha_{;mu} = partial_mu v^alpha + Gamma^alpha_{mu nu} v^nu (B.10).
- Define the derivative along a curve by contracting with the tangent (B.11).
- Resolve the D/dtau ambiguity by bracketing the whole vector before taking a component.

## Concepts

### Heaviside-Lorentz units

*convention · introduced* · also: rationalized Gaussian CGS units, Lorentz-Heaviside units

A system of electromagnetic units in which Coulomb's law carries an explicit 1/(4 pi) but no epsilon_0 or mu_0 appear, so Maxwell's equations have no 4 pi and no permittivity or permeability constants; with c kept, time derivatives and currents carry factors of 1/c.

**How introduced:** Motivated by the desire to simplify field-theory equations; presented by comparing SI Maxwell equations with their Heaviside-Lorentz form and by rewriting the point-charge potential.

**Prerequisites:** Maxwell's equations

$$
V(\vec x)=\frac{q}{4\pi|\vec x|}
$$

$$
\nabla\cdot\vec E=\rho,\ \nabla\times\vec B=\frac{1}{c}\left(\vec J+\partial_t\vec E\right)
$$

**Notes:** The book's recipe of setting epsilon_0 = mu_0 = 1 is shorthand; with c retained the exact conversion rescales fields and charges (E_HL = sqrt(epsilon_0) E_SI, B_HL = B_SI/sqrt(mu_0), q_HL = q_SI/sqrt(epsilon_0)).

**Where:** GA §B.1 p.562 (pdf 579)

### Maxwell's equations

*law · mention* · also: field equations of electromagnetism

The four equations relating the divergence and curl of the electric and magnetic fields to charge density, current density and each other's time derivatives.

**How introduced:** Quoted in SI form (B.1) as the starting point for the change of units.

$$
\nabla\cdot\vec E=\rho/\epsilon_0,\ \nabla\times\vec B=\mu_0\vec J+c^{-2}\partial_t\vec E
$$

**Where:** GA §B.1 p.562 (pdf 579)

### natural units with c = 1

*convention · mention* · also: geometrized units (partial), c = 1

Measuring time and length in the same units so that the speed of light is dimensionless and equal to one, which removes explicit factors of c from equations.

**How introduced:** Mentioned in one line as the book's other choice, applied on top of Heaviside-Lorentz units.

$$
c=1
$$

**Notes:** The appendix does not restate the G = 1 choice used in later parts of the book.

**Where:** GA §B.1 p.562 (pdf 579)

### passive transformation

*definition · introduced* · also: alias transformation

A transformation that changes the coordinate labels assigned to an event while the event itself stays where it is; the contrasting active transformation moves the event (or object) to a new location in the same coordinates.

**How introduced:** Given in a margin note to the claim that a rotation of basis changes components but not length, with Sidney Coleman's criminal analogy: under a passive change the criminal stays at the crime scene but looks different (an alias), under an active change the criminal is moved elsewhere (an alibi).

**Prerequisites:** coordinate system

**Where:** GA §B.2 p.562 (pdf 579)

### active transformation

*definition · mention* · also: alibi transformation

A transformation that physically moves an event or object to a different place (or rotates it) while the coordinate system is held fixed.

**How introduced:** Defined only as the contrast to the passive transformation the book uses, via Coleman's alibi image.

**Prerequisites:** passive transformation

**Where:** GA §B.2 p.562 (pdf 579)

### 3-vector notation

*convention · introduced* · also: three-vector, arrow vector

Spatial vectors are written with an arrow, their components carry a Roman index i = 1, 2, 3 (or coordinate names x, y, z) and that index is always written upstairs.

**How introduced:** Stated after the operational definition of a vector as something whose components change under a basis rotation while its length does not.

$$
A^i=(A^1,A^2,A^3)=(A^x,A^y,A^z)
$$

**Where:** GA §B.2 p.562 (pdf 579)

### 4-vector

*mathematical-object · revisited* · also: four-vector

A vector in (3+1)-dimensional spacetime: its zeroth component is timelike and the remaining three are spatial and together make up a 3-vector. The bold symbol stands for the basis-independent object; referred to a basis, its components carry a Greek index taking values 0 to 3.

**How introduced:** Built up from the 3-vector case by adding a zeroth, timelike component; the basis expansion is written with bold on both sides to stress that it is a basis-free equation.

**Prerequisites:** 3-vector notation, coordinate basis vectors

$$
\boldsymbol v=v^\mu\boldsymbol e_\mu
$$

$$
v^\mu=(v^0,v^i)=(v^0,\vec v)
$$

**Where:** GA §B.2 p.563 (pdf 580)

### coordinate basis vectors

*mathematical-object · revisited* · also: e_mu, partial/partial x^mu

The set of basis vectors e_mu associated with a coordinate system, which in the modern view are the partial-derivative operators along the coordinate lines, e_mu = partial/partial x^mu.

**How introduced:** Written as e_mu with the parenthetical alternative partial/partial x^mu in the 4-vector paragraph; justified in the margin note on tangent vectors (B.7).

**Prerequisites:** tangent vector as derivative operator

$$
\boldsymbol e_\mu=\frac{\partial}{\partial x^\mu}
$$

**Where:** GA §B.2 p.563 (pdf 580); GA §B.2 p.564 (pdf 581)

### 1-form

*mathematical-object · revisited* · also: covector, dual vector, one-form

A linear map from vectors to real numbers; written bold with a tilde, its components carry lower indices and it expands on basis 1-forms omega^mu (equivalently dx^mu).

**How introduced:** Introduced as the vector's natural partner, with the gradient of a function as the familiar instance.

**Prerequisites:** 4-vector

$$
\tilde{\boldsymbol A}=A_\mu\boldsymbol\omega^\mu
$$

$$
\boldsymbol\omega^\mu=\boldsymbol{d}x^\mu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### gradient 1-form and comma notation

*convention · revisited* · also: differential of a function, comma derivative

The gradient of a scalar function is a 1-form whose components are the partial derivatives of the function; these partial derivatives are written partial_mu f or, with a comma, f_{,mu}.

**How introduced:** Offered as the everyday example of a 1-form, which also introduces the comma shorthand that later becomes the semicolon for covariant derivatives.

**Prerequisites:** 1-form

$$
\partial_\mu f=\frac{\partial f}{\partial x^\mu}=f_{,\mu}
$$

**Notes:** The exported text dropped the comma; the printed page shows f_{,mu}.

**Where:** GA §B.2 p.563 (pdf 580)

### Einstein summation convention

*convention · revisited* · also: summation convention

An index that appears once up and once down in the same term is summed over its range without writing a summation sign.

**How introduced:** Stated in one sentence before the pairing and dot product.

$$
A_\mu v^\mu\equiv\sum_{\mu=0}^{3}A_\mu v^\mu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### pairing of a 1-form with a vector

*operation · revisited* · also: inner product of 1-form and vector, contraction, angle-bracket pairing

Feeding a vector into a 1-form yields a number, written with angle brackets and computed as the contraction of lower 1-form components with upper vector components; no metric is needed.

**How introduced:** Given in the same breath as the metric dot product so the two can be contrasted.

**Prerequisites:** 1-form, 4-vector, Einstein summation convention

$$
\langle\tilde{\boldsymbol A},\boldsymbol v\rangle=A_\mu v^\mu
$$

**Notes:** The printed text says the brackets pair 1-forms with 'tensors'; vectors are meant.

**Where:** GA §B.2 p.563 (pdf 580)

### scalar product via the metric

*operation · revisited* · also: dot product, inner product of two vectors

The dot product of two vectors is obtained by contracting both with the metric components.

**How introduced:** Stated alongside the pairing, pointing to the metric described in a margin note.

**Prerequisites:** metric tensor, Einstein summation convention

$$
\boldsymbol v\cdot\boldsymbol u=g_{\mu\nu}v^\mu u^\nu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### covariant and contravariant components

*convention · mention* · also: upstairs and downstairs components

Traditional names for components with upper and lower indices; in standard physics usage upper-index (vector) components are called contravariant and lower-index (1-form) components covariant.

**How introduced:** Mentioned only in two margin notes, which say the names are sometimes used and that the book mostly avoids them.

**Prerequisites:** 4-vector, 1-form

**Notes:** The printed notes attach the names the other way round (upper = covariant, lower = contravariant), opposite to the usual physics convention and to the book's own Chapter 2 (section 2.2), which calls a^mu contravariant and partial_mu phi covariant; see gaps.

**Where:** GA §B.2 p.562 (pdf 579); GA §B.2 p.563 (pdf 580)

### tensor as slot machine

*mathematical-object · revisited* · also: linear slot machine, multilinear map

A tensor is a multilinear machine with empty slots; inserting the appropriate number of 1-forms and vectors produces a real number.

**How introduced:** Recalled as the book's governing image for tensors, with bold symbols showing the empty slots, e.g. T( , ).

**Prerequisites:** 1-form, 4-vector

$$
\boldsymbol T(\ ,\ )
$$

**Where:** GA §B.2 p.563 (pdf 580)

### tensor valence (n, m)

*convention · introduced* · also: tensor type, rank (n, m)

The ordered pair (n, m) counts a tensor's inputs: n of them accept 1-forms and m accept vectors, so its components carry n upper and m lower indices.

**How introduced:** Stated immediately after the slot-machine description; the metric is later labelled a (0,2) tensor.

**Prerequisites:** tensor as slot machine

**Where:** GA §B.2 p.563 (pdf 580)

### component extraction by inserting basis vectors and 1-forms

*technique · revisited* · also: components from slots

The components of a tensor are the numbers obtained by filling its 1-form slots with basis 1-forms and its vector slots with basis vectors.

**How introduced:** Illustrated with a (2,2) tensor S.

**Prerequisites:** tensor as slot machine, coordinate basis vectors, 1-form

$$
\boldsymbol S(\boldsymbol\omega^\mu,\boldsymbol\omega^\nu,\boldsymbol e_\alpha,\boldsymbol e_\beta)=S^{\mu\nu}{}_{\alpha\beta}
$$

**Where:** GA §B.2 p.563 (pdf 580)

### tensor product

*operation · revisited* · also: outer product, otimes

The product that builds a higher-valence tensor from lower ones by letting each factor act on its own slots and multiplying the results; basis tensors are outer products of basis vectors and basis 1-forms.

**How introduced:** Listed as one of two ways to combine tensors, then used to expand a general tensor on a basis (B.3).

**Prerequisites:** tensor as slot machine

$$
\boldsymbol S=S^{\mu\nu}{}_{\alpha\beta}\,\boldsymbol e_\mu\otimes\boldsymbol e_\nu\otimes\boldsymbol\omega^\alpha\otimes\boldsymbol\omega^\beta
$$

**Where:** GA §B.2 p.563 (pdf 580)

### wedge product

*operation · revisited* · also: exterior product

The antisymmetrized tensor product; in this book the wedge of two vectors is their tensor product minus the swapped tensor product, with no factor of one half.

**How introduced:** Stated as a one-line relation to the outer product.

**Prerequisites:** tensor product, symmetrization and antisymmetrization brackets

$$
\boldsymbol v\wedge\boldsymbol u=\boldsymbol v\otimes\boldsymbol u-\boldsymbol u\otimes\boldsymbol v
$$

$$
(\boldsymbol v\wedge\boldsymbol u)^{\alpha\beta}=2\,v^{[\alpha}u^{\beta]}
$$

**Notes:** Because the bracket includes 1/2 and the wedge does not, the components differ by a factor of 2.

**Where:** GA §B.2 p.563 (pdf 580)

### symmetrization and antisymmetrization brackets

*convention · revisited* · also: round and square index brackets

Round brackets around indices denote the average over index orderings with plus signs (symmetric part) and square brackets the average with signs (antisymmetric part); for two indices each includes a factor of one half.

**How introduced:** Given as two short defining equations for two-index tensors.

$$
T^{(\alpha\beta)}=\tfrac12(T^{\alpha\beta}+T^{\beta\alpha})
$$

$$
T^{[\alpha\beta]}=\tfrac12(T^{\alpha\beta}-T^{\beta\alpha})
$$

**Where:** GA §B.2 p.563 (pdf 580)

### trace of a tensor

*operation · revisited* · also: contraction of a (1,1) tensor

The scalar obtained by contracting an upper index with a lower index of a tensor; the book denotes it by the tensor's letter in italic.

**How introduced:** Stated as a notational rule, with a margin note giving the exception that g denotes the metric determinant.

**Prerequisites:** Einstein summation convention

$$
T=T^\mu{}_\mu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### ordered index sum notation

*convention · mention* · also: vertical-bar indices |mu nu|

Indices enclosed in vertical bars are summed only over increasing orderings (mu < nu), avoiding double counting in sums over antisymmetric pairs.

**How introduced:** Mentioned in the sentence about numeric index labels.

**Prerequisites:** wedge product

$$
A_{|\mu\nu|}\,\boldsymbol\omega^\mu\wedge\boldsymbol\omega^\nu=\sum_{\mu<\nu}A_{\mu\nu}\,\boldsymbol\omega^\mu\wedge\boldsymbol\omega^\nu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### metric tensor

*mathematical-object · revisited* · also: metric, g

The symmetric (0,2) tensor whose value on two vectors is their dot product; its components are the dot products of basis vectors, and it is used to raise and lower indices.

**How introduced:** Introduced in a margin note as the most important tensor in the subject.

**Prerequisites:** tensor valence (n, m), coordinate basis vectors

$$
g_{\mu\nu}=\boldsymbol g(\boldsymbol e_\mu,\boldsymbol e_\nu)=\boldsymbol e_\mu\cdot\boldsymbol e_\nu
$$

**Where:** GA §B.2 p.563 (pdf 580)

### determinant of the metric

*physical-quantity · mention* · also: g

The determinant of the matrix of metric components g_{mu nu}, denoted g; it is negative for a Lorentzian metric and enters invariant volume elements through sqrt(-g).

**How introduced:** Flagged as an exception to the rule that an italic letter denotes a trace.

**Prerequisites:** metric tensor

$$
g=\det(g_{\mu\nu})
$$

**Where:** GA §B.2 p.563 (pdf 580)

### metric signature (-+++)

*convention · revisited* · also: mostly-plus signature

The choice that the metric has one negative and three positive eigenvalues, so that the Minkowski components are diag(-1, 1, 1, 1) and timelike vectors have negative squared length.

**How introduced:** Stated in the margin note on the metric, together with the diag notation for diagonal matrices.

**Prerequisites:** metric tensor

$$
\eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1)
$$

**Where:** GA §B.2 p.563 (pdf 580)

### index raising and lowering

*operation · revisited* · also: musical isomorphism

Converting between upper- and lower-index components by contracting with the metric components or their inverse; in an orthonormal frame the Minkowski components play this role.

**How introduced:** One-line statement in the metric margin note, repeated for hatted indices in the orthonormal-frame paragraph.

**Prerequisites:** metric tensor

$$
v_\mu=g_{\mu\nu}v^\nu
$$

$$
A_{\hat\alpha}=\eta_{\hat\alpha\hat\beta}A^{\hat\beta}
$$

**Where:** GA §B.2 p.563 (pdf 580); GA §B.2 p.564 (pdf 581)

### invariant volume elements

*convention · mention* · also: 4-volume element, 3-volume element dSigma

Symbols for integration measures: a script V names a spacetime 4-volume (invariant element d of script V), an italic V names a spatial 3-volume (invariant element dSigma), and dOmega is kept for the solid-angle piece dtheta^2 + sin^2 theta dphi^2 of spherical metrics.

**How introduced:** Given in a margin note attached to the 4-vector paragraph, with a remark that some texts use dOmega for the 4-volume.

**Prerequisites:** determinant of the metric

$$
\mathrm{d}\Omega^2=\mathrm{d}\theta^2+\sin^2\theta\,\mathrm{d}\phi^2
$$

**Where:** GA §B.2 p.563 (pdf 580)

### tensor field

*mathematical-object · revisited* · also: vector field v(x)

An assignment of a tensor to every point of spacetime; the notation v(x) means the vector the field produces at the point x, where x may denote the abstract point or its coordinates.

**How introduced:** Introduced with an explicit warning that the round-bracket position argument must not be confused with the tensor's slots.

**Prerequisites:** tensor as slot machine, manifold point versus coordinates

$$
\boldsymbol v(x),\ x=\mathcal P\ \text{or}\ x^\mu(\mathcal P)
$$

**Where:** GA §B.2 p.564 (pdf 581)

### manifold point versus coordinates

*principle · developed* · also: points are not position vectors

In curved spacetime there is no meaningful arrow from one point to another, so locations are specified as points P of the manifold or by their coordinate values x^mu(P), and these coordinate values are not components of a vector.

**How introduced:** Motivated by stating that position vectors between spacetime points are of little use once spacetime is curved; developed in the margin note comparing displacement and derivative-operator tangents.

**Prerequisites:** 4-vector

$$
x^\mu(\mathcal P)
$$

**Where:** GA §B.2 p.564 (pdf 581)

### four-velocity

*physical-quantity · revisited* · also: velocity field, 4-velocity

The tangent vector to a timelike world line parametrized by proper time, with components dx^mu/dtau; with c = 1 and signature (-+++) it has unit negative norm.

**How introduced:** Singled out as the vector field of greatest importance for relativity, and defined as the tangent to a world line x^mu(tau).

**Prerequisites:** affine parameter, tangent vector as derivative operator, metric signature (-+++)

$$
\boldsymbol u(x)=\frac{\mathrm dx^\mu(\tau)}{\mathrm d\tau}\boldsymbol e_\mu
$$

$$
\boldsymbol u\cdot\boldsymbol u=-1
$$

**Where:** GA §B.2 p.564 (pdf 581)

### affine parameter

*definition · mention* · also: proper time as curve parameter

A parameter along a curve, such as proper time on a timelike world line, related to any other such parameter by a linear transformation; it is the parametrization in which the geodesic equation takes its standard form.

**How introduced:** Mentioned in passing as the kind of parameter used for world lines.

**Where:** GA §B.2 p.564 (pdf 581)

### displacement-vector description of tangent vectors

*technique · mention* · also: classical tangent via X(tau)

Representing points on a curve by a displacement vector X = X^mu e_mu and differentiating it with the chain rule to obtain the tangent, its components dx^mu/dtau and basis vectors partial X/partial x^mu.

**How introduced:** Recalled in a margin note from Chapter 30 and then set aside because the displacement vector does not obey the tensor transformation law.

**Prerequisites:** manifold point versus coordinates

$$
\boldsymbol u=\frac{\mathrm d\boldsymbol X}{\mathrm d\tau}=\frac{\mathrm dx^\mu}{\mathrm d\tau}\frac{\partial\boldsymbol X}{\partial x^\mu}
$$

**Where:** GA §B.2 p.564 (pdf 581)

### tangent vector as derivative operator

*definition · introduced* · also: vectors as directional derivatives, modern tangent vector

A tangent vector at a point is the directional-derivative operator along a curve through that point; the tangent field of a curve is dx^mu/dtau times partial/partial x^mu, so the coordinate basis vectors are the partial derivatives.

**How introduced:** Presented in the same margin note as the modern replacement for the displacement-vector picture, pointing to Chapter 31.

**Prerequisites:** coordinate basis vectors

$$
\boldsymbol u(x)=\frac{\mathrm dx^\mu}{\mathrm d\tau}\frac{\partial}{\partial x^\mu}
$$

**Where:** GA §B.2 p.564 (pdf 581)

### orthonormal frame components

*convention · revisited* · also: hatted indices, local Lorentz frame components

Hats mark components and basis vectors referred to a frame of mutually orthogonal, unit-norm basis vectors; because the metric components in such a frame are exactly eta, hatted indices move up and down with diag(-1, 1, 1, 1).

**How introduced:** Introduced as a notational rule, followed by the vielbein conversions.

**Prerequisites:** metric signature (-+++), index raising and lowering

$$
\boldsymbol A=A^{\hat\alpha}\boldsymbol e_{\hat\alpha}
$$

$$
\boldsymbol e_{\hat\alpha}\cdot\boldsymbol e_{\hat\beta}=\eta_{\hat\alpha\hat\beta}
$$

**Where:** GA §B.2 p.564 (pdf 581)

### vielbein

*mathematical-object · revisited* · also: tetrad, frame field, vierbein

The set of coefficients relating coordinate basis vectors to orthonormal basis vectors, written (e_mu)^{alpha-hat} and its inverse (e_{alpha-hat})^mu, used to convert vector and 1-form components between the two frames.

**How introduced:** Given as four conversion rules in bracket notation, which make the index placement self-explanatory.

**Prerequisites:** orthonormal frame components, coordinate basis vectors

$$
A^{\hat\alpha}=(\boldsymbol e_\mu)^{\hat\alpha}A^\mu
$$

$$
Z_{\hat\alpha}=(\boldsymbol e_{\hat\alpha})^\mu Z_\mu
$$

**Where:** GA §B.2 p.564 (pdf 581)

### square-root rule for diagonal metrics

*technique · revisited* · also: orthonormal frame for a diagonal metric

When the metric is diagonal, each orthonormal basis vector is the coordinate basis vector divided by the square root of the absolute value of its diagonal metric component, so the vielbein component (e_mu)^{mu-hat} equals sqrt|g_{mu mu}| (no sum).

**How introduced:** Offered as a useful shortcut immediately after the vielbein rules.

**Prerequisites:** vielbein, metric tensor

$$
(\boldsymbol e_\mu)^{\hat\mu}=\sqrt{|g_{\mu\mu}|}
$$

**Where:** GA §B.2 p.564 (pdf 581)

### covariant derivative

*operation · revisited* · also: nabla_u, directional covariant derivative

The derivative of a tensor field along a vector u that accounts for the change of basis from point to point, producing a tensor; in components it is the partial derivative plus connection-coefficient corrections.

**How introduced:** Named the most useful derivative in relativity and written first in basis-free directional form, then in components.

**Prerequisites:** connection coefficients, tensor field, gradient 1-form and comma notation

$$
\nabla_{\boldsymbol u}=u^\mu\nabla_{\boldsymbol e_\mu}=u^\mu\nabla_\mu
$$

**Notes:** The printed text writes the expansion with a dot, u . nabla_{e_mu}; the intended meaning is the contraction u^mu nabla_mu.

**Where:** GA §B.3 p.564 (pdf 581)

### nabla_mu as a directional label

*convention · developed* · also: nabla_{e_mu} shorthand

The subscript on nabla_mu names the basis direction e_mu along which the derivative is taken; nabla_mu v is a whole vector, not a component of anything.

**How introduced:** Singled out as confusing and explained explicitly, then reinforced by the mixed notation (nabla_mu v)^alpha.

**Prerequisites:** covariant derivative

$$
\nabla_\mu\equiv\nabla_{\boldsymbol e_\mu}
$$

$$
\nabla_\mu\boldsymbol v=(\nabla_\mu\boldsymbol v)^\alpha\boldsymbol e_\alpha
$$

**Where:** GA §B.3 p.564 (pdf 581)

### semicolon notation

*convention · revisited* · also: v^alpha_{;mu}

A component shorthand in which a semicolon before an index denotes the covariant derivative in that direction, equal to the partial derivative of the component plus a connection term for each index.

**How introduced:** Defined by equation B.10 as the coordinate form of (nabla_mu v)^alpha.

**Prerequisites:** covariant derivative, connection coefficients, gradient 1-form and comma notation

$$
v^\alpha{}_{;\mu}=\frac{\partial v^\alpha}{\partial x^\mu}+\Gamma^\alpha{}_{\mu\nu}v^\nu
$$

**Where:** GA §B.3 p.564 (pdf 581)

### connection coefficients

*mathematical-object · mention* · also: Christoffel symbols, Gamma

The coefficients Gamma^alpha_{mu nu} that describe how basis vectors change from point to point, entering the covariant derivative as correction terms; in the book's ordering the first lower index is the derivative direction.

**How introduced:** Appear without further comment in the semicolon definition.

$$
\Gamma^\alpha{}_{\mu\nu}
$$

**Where:** GA §B.3 p.564 (pdf 581)

### covariant derivative along a curve

*operation · revisited* · also: D/dtau, absolute derivative, intrinsic derivative

The rate of change of a vector field along a curve with tangent u, defined as nabla_u v and written Dv/dtau; its components are the tangent contracted with the semicolon derivative.

**How introduced:** Introduced as a further notation for curves, with a margin note resolving how different books use D/dtau.

**Prerequisites:** covariant derivative, four-velocity

$$
\left(\frac{\mathrm D\boldsymbol v}{\mathrm d\tau}\right)^\alpha=u^\mu v^\alpha{}_{;\mu}
$$

**Where:** GA §B.3 p.564 (pdf 581)

### coordinate-free, mixed and coordinate notation

*convention · introduced* · also: three levels of notation

Three ways of writing the same quantity: fully basis-free bold symbols (nabla_u v), mixed forms that take a component of a basis-free object ((nabla_u v)^mu), and pure component forms (v^alpha_{;mu}).

**How introduced:** Laid out in the closing margin note as the logic behind the covariant-derivative notations.

**Prerequisites:** covariant derivative, semicolon notation

**Where:** GA §B.3 p.564 (pdf 581)

### general matrix notation

*convention · mention* · also: underlined bold X

When an argument concerns an arbitrary matrix rather than a tensor, the matrix is written as a bold letter with an underline.

**How introduced:** A one-line margin note attached to the tensor valence sentence.

**Where:** GA §B.2 p.563 (pdf 580)

## Key equations

### (B.1) Maxwell's equations in SI units · supporting · GA §B.1 p.562 (pdf 579)

$$
\nabla\cdot\vec E=\frac{\rho}{\epsilon_0},\quad \nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\quad \nabla\cdot\vec B=0,\quad \nabla\times\vec B=\mu_0\vec J+\frac{1}{c^2}\frac{\partial\vec E}{\partial t}
$$

Reference form of free-space electromagnetism in SI units, the starting point for the change to Heaviside-Lorentz units.

**Symbols:** E electric field; B magnetic field; rho charge density; J current density; epsilon_0 permittivity and mu_0 permeability of free space; c speed of light

### Point-charge potential, SI to Heaviside-Lorentz · supporting · GA §B.1 p.562 (pdf 579)

$$
V(\vec x)=\frac{q}{4\pi\epsilon_0|\vec x|}\ \longrightarrow\ V(\vec x)=\frac{q}{4\pi|\vec x|}
$$

The factor 1/(4 pi) stays in Coulomb's law while epsilon_0 disappears; this is where rationalized units hide the 4 pi.

**Symbols:** q charge; x position relative to the charge

### (B.2) Maxwell's equations in Heaviside-Lorentz units · central · GA §B.1 p.562 (pdf 579)

$$
\nabla\cdot\vec E=\rho,\quad \nabla\times\vec E=-\frac{1}{c}\frac{\partial\vec B}{\partial t},\quad \nabla\cdot\vec B=0,\quad \nabla\times\vec B=\frac{1}{c}\left(\vec J+\frac{\partial\vec E}{\partial t}\right)
$$

The book's form of Maxwell's equations before setting c = 1: no epsilon_0, mu_0 or 4 pi; setting c = 1 leaves the minimal field-theory form used in Part VI.

**Symbols:** Fields, charge and current in Heaviside-Lorentz units (rescaled relative to SI by powers of sqrt(epsilon_0) and sqrt(mu_0))

### 3-vector components · supporting · GA §B.2 p.562 (pdf 579)

$$
A^i=(A^1,A^2,A^3)=(A^x,A^y,A^z)
$$

Spatial vector components carry a Roman index, always upstairs, labelled by number or by coordinate name.

**Symbols:** i = 1, 2, 3

### 4-vector basis expansion · central · GA §B.2 p.563 (pdf 580)

$$
\boldsymbol v=v^\mu\boldsymbol e_\mu,\qquad v^\mu=(v^0,v^1,v^2,v^3)=(v^0,v^i)=(v^0,\vec v)
$$

A basis-free 4-vector equals its components times basis vectors; the zeroth component is timelike and the rest form a 3-vector.

**Symbols:** mu = 0..3; e_mu basis vectors (also partial/partial x^mu)

### 1-form expansion and gradient components · central · GA §B.2 p.563 (pdf 580)

$$
\tilde{\boldsymbol A}=A_\mu\boldsymbol\omega^\mu,\qquad \frac{\partial f}{\partial x^\mu}=\partial_\mu f=f_{,\mu}
$$

A 1-form expands on basis 1-forms with lower-index components; the gradient of f is the model example, with the comma denoting a partial derivative.

**Symbols:** omega^mu basis 1-forms (also dx^mu); f scalar function

### Pairing and scalar product · central · GA §B.2 p.563 (pdf 580)

$$
\langle\tilde{\boldsymbol A},\boldsymbol v\rangle=A_\mu v^\mu,\qquad \boldsymbol v\cdot\boldsymbol u=g_{\mu\nu}v^\mu u^\nu
$$

A 1-form eats a vector without any metric; two vectors need the metric to produce a number.

**Symbols:** g_{mu nu} metric components

### Component extraction for a (2,2) tensor · central · GA §B.2 p.563 (pdf 580)

$$
\boldsymbol S(\boldsymbol\omega^\mu,\boldsymbol\omega^\nu,\boldsymbol e_\alpha,\boldsymbol e_\beta)=S^{\mu\nu}{}_{\alpha\beta}
$$

Filling the slots of a tensor with basis 1-forms and basis vectors returns its components.

**Symbols:** S a (2,2) tensor: two 1-form slots, two vector slots

### Wedge product of two vectors · supporting · GA §B.2 p.563 (pdf 580)

$$
\boldsymbol v\wedge\boldsymbol u=\boldsymbol v\otimes\boldsymbol u-\boldsymbol u\otimes\boldsymbol v
$$

The wedge is the antisymmetrized outer product with no factor of 1/2, so its components are twice the bracket-antisymmetrized ones.

**Symbols:** otimes outer (tensor) product

### (B.3) Basis expansion of a (2,2) tensor · central · GA §B.2 p.563 (pdf 580)

$$
\boldsymbol S=S^{\mu\nu}{}_{\alpha\beta}\,\left(\boldsymbol e_\mu\otimes\boldsymbol e_\nu\otimes\boldsymbol\omega^\alpha\otimes\boldsymbol\omega^\beta\right)
$$

Any tensor is a sum of components times outer products of basis vectors and basis 1-forms. The printed equation repeats e_mu in the second factor; the second basis vector should carry nu, as written here.

**Symbols:** e_mu basis vectors; omega^alpha basis 1-forms

### (B.4) Symmetrization · supporting · GA §B.2 p.563 (pdf 580)

$$
T^{(\alpha\beta)}=\frac12\left(T^{\alpha\beta}+T^{\beta\alpha}\right)
$$

Round brackets on indices take the symmetric part, including a factor 1/2.

### (B.5) Antisymmetrization · supporting · GA §B.2 p.563 (pdf 580)

$$
T^{[\alpha\beta]}=\frac12\left(T^{\alpha\beta}-T^{\beta\alpha}\right)
$$

Square brackets on indices take the antisymmetric part, including a factor 1/2.

### Trace · supporting · GA §B.2 p.563 (pdf 580)

$$
T=T^\mu{}_\mu
$$

The trace is the contraction of an upper with a lower index and carries the tensor's letter in italic.

### Metric components, signature and determinant · central · GA §B.2 p.563 (pdf 580)

$$
g_{\mu\nu}=\boldsymbol g(\boldsymbol e_\mu,\boldsymbol e_\nu)=\boldsymbol e_\mu\cdot\boldsymbol e_\nu,\qquad \eta_{\mu\nu}=\mathrm{diag}(-1,1,1,1),\qquad g\equiv\det(g_{\mu\nu})
$$

The metric's components are dot products of basis vectors; the sign choice (-+++) shows up as the Minkowski components diag(-1,1,1,1); the symbol g denotes the determinant, not the trace.

**Symbols:** g the (0,2) metric tensor; eta Minkowski components

### Angular line element · supporting · GA §B.2 p.563 (pdf 580)

$$
\mathrm d\Omega^2=\mathrm d\theta^2+\sin^2\theta\,\mathrm d\phi^2
$$

dOmega is reserved for the angular part of spherical line elements rather than a 4-volume.

**Symbols:** theta polar angle; phi azimuthal angle

### 4-velocity and normalization · central · GA §B.2 p.564 (pdf 581)

$$
\boldsymbol u(x)=\frac{\mathrm dx^\mu(\tau)}{\mathrm d\tau}\boldsymbol e_\mu,\qquad \boldsymbol u\cdot\boldsymbol u=-1
$$

The velocity field is the tangent to a world line parametrized by proper time, and in (-+++) signature with c = 1 it has norm -1.

**Symbols:** tau proper time (an affine parameter); x^mu(tau) world line

### (B.6) Tangent from a displacement vector · derivation-step · GA §B.2 p.564 (pdf 581)

$$
\boldsymbol u=\frac{\mathrm d\boldsymbol X(\tau)}{\mathrm d\tau}=\frac{\mathrm dx^\mu}{\mathrm d\tau}\frac{\partial\boldsymbol X(\tau)}{\partial x^\mu},\qquad u^\mu=\frac{\mathrm dx^\mu}{\mathrm d\tau},\quad \boldsymbol e_\mu=\frac{\partial\boldsymbol X}{\partial x^\mu}
$$

The Chapter 30 route: differentiate the displacement vector along the curve with the chain rule to read off tangent components and basis vectors. The margin note prints the components as a partial derivative of x^mu with respect to tau; along a curve it is an ordinary derivative. The displacement vector is not a tensor, so this route is abandoned for GR.

**Symbols:** X = X^mu e_mu displacement vector to points on the world line

### (B.7) Tangent as a derivative operator · central · GA §B.2 p.564 (pdf 581)

$$
\boldsymbol u(x)=\frac{\mathrm dx^\mu}{\mathrm d\tau}\frac{\partial}{\partial x^\mu},\qquad \boldsymbol e_\mu=\frac{\partial}{\partial x^\mu}
$$

The modern (Chapter 31) definition: the tangent field is a directional derivative, and coordinate basis vectors are partial derivatives.

### Vector in an orthonormal frame · supporting · GA §B.2 p.564 (pdf 581)

$$
\boldsymbol A=A^{\hat\alpha}\boldsymbol e_{\hat\alpha}
$$

Hats mark components and basis vectors of an orthonormal frame, whose indices are moved with eta.

### (B.8) Vielbein conversion rules · central · GA §B.2 p.564 (pdf 581)

$$
A^{\hat\alpha}=(\boldsymbol e_\mu)^{\hat\alpha}A^\mu,\quad A^\mu=(\boldsymbol e_{\hat\alpha})^\mu A^{\hat\alpha},\quad Z_\mu=(\boldsymbol e_\mu)^{\hat\alpha}Z_{\hat\alpha},\quad Z_{\hat\alpha}=(\boldsymbol e_{\hat\alpha})^\mu Z_\mu
$$

Vector components and 1-form components are converted between coordinate and orthonormal frames with the vielbein components; the bracket notation reads as 'the hatted component of a coordinate basis vector' and vice versa.

**Symbols:** (e_mu)^{alpha-hat} components of coordinate basis vectors in the orthonormal frame; (e_{alpha-hat})^mu the inverse; A a vector; Z a 1-form

### Square-root rule · central · GA §B.2 p.564 (pdf 581)

$$
(\boldsymbol e_\mu)^{\hat\mu}=\sqrt{|g_{\mu\mu}|}\qquad(\text{no sum})
$$

For a diagonal metric, the only non-zero vielbein component for each coordinate direction is the square root of the modulus of the corresponding diagonal metric component.

**Symbols:** g_{mu mu} diagonal metric components

### Directional covariant derivative · supporting · GA §B.3 p.564 (pdf 581)

$$
\nabla_{\boldsymbol u}=u^\mu\nabla_{\boldsymbol e_\mu}=u^\mu\nabla_\mu
$$

The derivative along u is a combination of derivatives along the basis directions. The printed text writes a dot between u and nabla_{e_mu}; a component contraction is intended.

**Symbols:** u a vector giving the direction

### (B.9) Covariant derivative on a basis · central · GA §B.3 p.564 (pdf 581)

$$
\nabla_\mu\boldsymbol v=(\nabla_\mu\boldsymbol v)^\alpha\boldsymbol e_\alpha=v^\alpha{}_{;\mu}\boldsymbol e_\alpha
$$

The covariant derivative of v along e_mu is a vector whose alpha component can be written in mixed notation or with a semicolon.

### (B.10) Semicolon (covariant derivative) components · central · GA §B.3 p.564 (pdf 581)

$$
v^\alpha{}_{;\mu}=\frac{\partial v^\alpha}{\partial x^\mu}+\Gamma^\alpha{}_{\mu\nu}v^\nu
$$

Components of the covariant derivative are partial derivatives of components plus a connection term correcting for the changing basis.

**Symbols:** Gamma^alpha_{mu nu} connection coefficients (first lower index = derivative direction)

### (B.11) Covariant derivative along a curve · central · GA §B.3 p.564 (pdf 581)

$$
\left(\frac{\mathrm D\boldsymbol v}{\mathrm d\tau}\right)^\alpha=u^\mu\left(\frac{\partial v^\alpha}{\partial x^\mu}+\Gamma^\alpha{}_{\mu\nu}v^\nu\right)=u^\mu v^\alpha{}_{;\mu},\qquad \frac{\mathrm D\boldsymbol v}{\mathrm d\tau}=\nabla_{\boldsymbol u}\boldsymbol v
$$

The rate of change of v along a curve with tangent u; the component is taken after forming the vector derivative, hence the bracketed notation.

**Symbols:** u tangent to the curve x^mu(tau)

### Competing D/dtau conventions · supporting · GA §B.3 p.564 (pdf 581)

$$
\frac{\mathrm D\boldsymbol v}{\mathrm d\tau}=\nabla_{\boldsymbol u}\boldsymbol v\ \ (\text{book's choice})\qquad\text{vs}\qquad \frac{\mathrm Dv^\mu}{\mathrm d\tau}=u^\alpha v^\mu{}_{;\alpha}\ \ (\text{other texts; written }(\mathrm D\boldsymbol v/\mathrm d\tau)^\mu\text{ here})
$$

Some books attach D/dtau to a component symbol; because that reads like a derivative of a component function, the book brackets the vector first.

## Figures

## Worked examples

### Example · intro · GA §B.1 p.562 (pdf 579)

**Problem:** Show how the potential of a point charge changes when moving from SI to Heaviside-Lorentz units.

**Method:** Remove the permittivity constant from the SI Coulomb potential, keeping the geometric 1/(4 pi) that comes from spreading field lines over a sphere.

**Key insight:** Rationalized units keep 4 pi in point-source formulas so that it disappears from the differential field equations.

**Result:** V(\vec x)=q/(4\pi|\vec x|)

**Concepts:** Heaviside-Lorentz units

### Example · intro · GA §B.2 p.564 (pdf 581)

**Problem:** Obtain the components and basis vectors of the tangent to a world line, first from a displacement vector and then in the modern derivative-operator form.

**Method:** Differentiate X(tau) with respect to tau using the chain rule through the coordinates x^mu(tau) (B.6); read off u^mu = dx^mu/dtau and e_mu = partial X/partial x^mu; then replace X by the operator form u = (dx^mu/dtau) partial/partial x^mu (B.7).

**Key insight:** Both routes give the same components dx^mu/dtau, but only the second avoids an object (the displacement vector) that fails to transform as a tensor in curved spacetime.

**Result:** u^\mu=\mathrm dx^\mu/\mathrm d\tau,\ \boldsymbol e_\mu=\partial/\partial x^\mu

**Concepts:** displacement-vector description of tangent vectors, tangent vector as derivative operator, four-velocity


## Analogies and intuitions

### Alias versus alibi (Sidney Coleman's criminal image) → passive transformation · strong · GA §B.2 p.562 (pdf 579)

The event is a criminal at a crime scene. A passive transformation is an alias: the criminal is still at the scene but described differently. An active transformation is an alibi: the criminal is relocated to somewhere other than the scene.

**Where it breaks down:** Only distinguishes the two interpretations; it says nothing about which transformations are symmetries or about the inverse relation between active and passive versions of the same map.

**App idea:** Split-screen: a fixed event dot with a rotatable coordinate grid (alias) beside a fixed grid with a draggable event (alibi); matching the displayed component readouts shows that a passive rotation by +theta equals an active rotation by -theta.

### Tensors as slot machines → tensor as slot machine · strong · GA §B.2 p.563 (pdf 580)

A tensor is pictured as a machine with labelled input slots (1-form slots and vector slots) that returns a number once all are filled; components are what comes out when basis objects are inserted.

**Where it breaks down:** Captures multilinearity and valence but not how the machine changes from point to point or how slots of different kinds are related by the metric.

**App idea:** A drag-and-drop machine with coloured sockets: dropping basis vectors and basis 1-forms into a (2,2) tensor lights up the corresponding component in a 4x4x4x4 table slice; dropping a general vector shows linear combination of columns.

### A field's argument says where, its slots say what it eats → tensor field · useful · GA §B.2 p.564 (pdf 581)

The round bracket in v(x) picks the point of spacetime; the empty slot of the vector at that point is a separate thing that accepts a 1-form.

**Where it breaks down:** Conceptual clarification only; does not address smoothness or how fields at different points are compared.

**App idea:** Hover over a vector field on a curved surface: the cursor selects x and a pop-up machine for v(x) offers a slot where the learner drops a 1-form (drawn as stacked lines) to get a number.

### Directional derivative along a chosen arrow → covariant derivative · useful · GA §B.3 p.564 (pdf 581)

nabla_u is read as 'how fast the field changes as you move in the direction u', with nabla_mu the special case of moving along a coordinate basis direction.

**Where it breaks down:** Hides the connection term, which is precisely what distinguishes the covariant derivative from a naive directional derivative of components.

**App idea:** On polar coordinates in the plane, show a constant Cartesian vector field whose polar components vary; toggling the Gamma term on and off shows partial derivatives of components are non-zero while the covariant derivative vanishes.

### Typography as a type system → 3-vector notation · useful · GA §B.2 p.563 (pdf 580)

Not stated as an analogy in the appendix; it is the implicit logic of its layout. Arrows, bold, tildes, hats and index heights each advertise what kind of object a symbol is, so a reader can check an equation for consistency at a glance, much as units are checked in dimensional analysis.

**Where it breaks down:** Voice tutoring and plain text lose bold, tildes and script letters, so the type information must be spoken explicitly.

**App idea:** A notation decoder: the learner types or clicks a symbol (arrow A, bold v, tilde A, A^{alpha-hat}, v^alpha_{;mu}) and the panel names the object, its valence, its frame and where in the book it is introduced.


## Misconceptions addressed

### The subscript in nabla_mu v is a component index, so nabla_mu v is a component. · GA §B.3 p.564 (pdf 581)

**Correction:** nabla_mu is shorthand for the derivative along the basis vector e_mu; nabla_mu v is a complete vector whose components are (nabla_mu v)^alpha = v^alpha_{;mu}.

**Why tempting:** A lower Greek index normally marks a 1-form component, and nabla_mu f for a scalar coincides with the component partial_mu f.

### Dv^mu/dtau means the ordinary rate of change of the component function v^mu along the curve. · GA §B.3 p.564 (pdf 581)

**Correction:** The covariant derivative along the curve includes a connection term; the book writes (Dv/dtau)^mu to make clear the component is taken of the vector derivative.

**Why tempting:** Placing D/dtau in front of a component symbol looks exactly like differentiating that component.

### The coordinates x^mu of a point are the components of a position vector, just as in flat Cartesian space. · GA §B.2 p.564 (pdf 581)

**Correction:** In curved spacetime there is no vector from an origin to a point; points are labelled by coordinates, which are not vector components and do not obey the tensor transformation law.

**Why tempting:** In Cartesian coordinates in flat space the position vector's components coincide with the coordinates.

### The x in v(x) is one of the vector's slots. · GA §B.2 p.564 (pdf 581)

**Correction:** x is the location at which the field is evaluated; the vector produced there has its own single slot for a 1-form.

**Why tempting:** Both use round brackets: T( , ) for slots and v(x) for position.

### A coordinate transformation moves events around in spacetime. · GA §B.2 p.562 (pdf 579)

**Correction:** The book's transformations are passive: the event stays put and only its coordinate description changes.

**Why tempting:** Many linear-algebra courses present rotations as actively rotating vectors.

### Following the italic-letter rule, g is the trace of the metric. · GA §B.2 p.563 (pdf 580)

**Correction:** g is the determinant of g_{mu nu}; the trace g^mu_mu equals the dimension (4) and is never needed as a symbol.

**Why tempting:** The same paragraph establishes that italic T denotes the trace of T.

### Hatted indices are raised and lowered with g_{mu nu} like any other index. · GA §B.2 p.564 (pdf 581)

**Correction:** In an orthonormal frame the metric components are exactly eta, so hatted indices are moved with diag(-1, 1, 1, 1).

**Why tempting:** The general rule says indices are moved with the metric, and learners forget that the metric's components in an orthonormal frame are eta.

### 'Covariant' always means lower index and 'contravariant' always means upper index, in every source. · GA §B.2 p.562 (pdf 579)

**Correction:** Usage varies: most physics texts call upper-index vector components contravariant and lower-index 1-form components covariant, while this appendix's margin notes attach the words the other way round. The safe course is to say 'vector components' and '1-form components', as the book mostly does.

**Why tempting:** The words sound like standard, fixed technical terms.

*Inferred: the book guards against this implicitly.*

### The wedge product of two vectors has components equal to the antisymmetrized bracket v^{[alpha} u^{beta]}. · GA §B.2 p.563 (pdf 580)

**Correction:** With the book's definition v wedge u = v tensor u - u tensor v, the components are 2 v^{[alpha} u^{beta]}, since the bracket already includes 1/2.

**Why tempting:** Both operations are described as antisymmetrization and appear in consecutive lines.

*Inferred: the book guards against this implicitly.*

### Setting epsilon_0 = mu_0 = 1 directly in the SI equations produces the Heaviside-Lorentz equations with factors of 1/c. · GA §B.1 p.562 (pdf 579)

**Correction:** Literally substituting into B.1 gives no 1/c in Faraday's law; the Heaviside-Lorentz form with c retained requires rescaling fields and charges by powers of sqrt(epsilon_0) and sqrt(mu_0). The shortcut is exact only once c = 1 as well.

**Why tempting:** The appendix summarises the change of units in those words.

*Inferred: the book guards against this implicitly.*


## Thought experiments

_None recorded._

## Applications and observations

_None recorded._

## Historical notes

- **Oliver Heaviside, Hendrik Antoon Lorentz:** The rationalized unit system is named for Oliver Heaviside (1850-1925), the English electrical engineer, and Hendrik Lorentz (1853-1928), the Dutch physicist. — Explains the name of the units the book uses throughout its field-theory chapters. (GA §B.1 p.562 (pdf 579))
- **Sidney Coleman:** The alias/alibi description of passive and active transformations is credited to Coleman. — Source of the book's mnemonic for its passive-transformation convention. (GA §B.2 p.562 (pdf 579))

## Notation and conventions

- **Electromagnetic units:** Heaviside-Lorentz (rationalized Gaussian) units: no epsilon_0 or mu_0; Coulomb potential q/(4 pi r); Maxwell's equations carry 1/c factors that vanish with c = 1. — Differs from SI and from the Gaussian units of Jackson and Landau-Lifshitz; most field-theory books agree with this choice. (GA §B.1 p.562 (pdf 579))
- **Speed of light:** c = 1 throughout, removing c from the Heaviside-Lorentz Maxwell equations. — G = 1 (used later in the book) is not restated here. (GA §B.1 p.562 (pdf 579))
- **Transformations:** Passive: coordinates change, events do not move. (GA §B.2 p.562 (pdf 579))
- **3-vectors:** Arrow over a letter; Roman indices i = 1, 2, 3 from the middle of the alphabet, or coordinate names x, y, z; always upstairs. (GA §B.2 p.562 (pdf 579))
- **4-vectors:** Bold symbols denote basis-free objects; components carry Greek indices mu = 0, 1, 2, 3 with 0 the timelike component; v^mu = (v^0, v^i) = (v^0, arrow v). (GA §B.2 p.563 (pdf 580))
- **Basis vectors:** e_mu, also written partial/partial x^mu; v = v^mu e_mu with bold on both sides. (GA §B.2 p.563 (pdf 580))
- **1-forms:** Bold with a tilde; components always downstairs; basis 1-forms omega^mu, also dx^mu; A = A_mu omega^mu. (GA §B.2 p.563 (pdf 580))
- **Partial derivatives:** partial f/partial x^mu = partial_mu f = f_{,mu} (comma notation). (GA §B.2 p.563 (pdf 580))
- **Summation:** Einstein convention: a repeated index appearing once up and once down is summed. (GA §B.2 p.563 (pdf 580))
- **Pairing and dot product:** <A, v> = A_mu v^mu for a 1-form with a vector; v . u = g_{mu nu} v^mu u^nu for two vectors. — Printed text says '1-forms and tensors' for the pairing; vectors are meant. (GA §B.2 p.563 (pdf 580))
- **Tensors and valence:** Bold symbol with empty slots, e.g. T( , ); valence (n, m) = n 1-form slots, m vector slots; components from inserting basis 1-forms and vectors. (GA §B.2 p.563 (pdf 580))
- **Products:** Outer product otimes; wedge product with v wedge u = v otimes u - u otimes v (no 1/2). (GA §B.2 p.563 (pdf 580))
- **Index brackets:** (alpha beta) symmetrization and [alpha beta] antisymmetrization, each with a factor 1/2 for two indices. (GA §B.2 p.563 (pdf 580))
- **Trace:** Italic letter of the tensor: T = T^mu_mu. — Exception: g is the metric determinant. (GA §B.2 p.563 (pdf 580))
- **Index labels:** Indices may be coordinate names (t, r, theta, phi) or numbers; vertical bars |mu nu| restrict a sum to mu < nu. — The printed example gives numeric labels as 1...4, whereas elsewhere the book numbers 0...3. (GA §B.2 p.563 (pdf 580))
- **Volumes:** Script V is a 4-volume with invariant element dV (script); italic V a 3-volume with invariant element dSigma. — Some texts use dOmega for the 4-volume; here dOmega^2 = dtheta^2 + sin^2 theta dphi^2 is the angular line element. (GA §B.2 p.563 (pdf 580))
- **General matrices:** Bold underlined letter, e.g. X underlined, when a statement concerns an arbitrary matrix rather than a tensor. (GA §B.2 p.563 (pdf 580))
- **Metric:** (0,2) tensor g( , ) with g_{mu nu} = g(e_mu, e_nu) = e_mu . e_nu; g = det(g_{mu nu}); indices raised and lowered with the metric. (GA §B.2 p.563 (pdf 580))
- **Signature:** (-+++), eta_{mu nu} = diag(-1, 1, 1, 1); diagonal matrices specified with diag(...). — Timelike vectors have negative norm, so u . u = -1 for a 4-velocity. (GA §B.2 p.563 (pdf 580))
- **Tensor fields:** v(x): the bracket holds a point P or its coordinates x^mu(P), never a slot. (GA §B.2 p.564 (pdf 581))
- **Points and coordinates:** Points are written P (script) with coordinates x^mu(P); coordinates are not vector components. (GA §B.2 p.564 (pdf 581))
- **4-velocity:** u(x) = (dx^mu(tau)/dtau) e_mu along a world line x^mu(tau) with affine parameter tau (proper time); u . u = -1. (GA §B.2 p.564 (pdf 581))
- **Orthonormal frames:** Hats on indices and basis vectors, A = A^{alpha-hat} e_{alpha-hat}; hatted indices moved with eta. (GA §B.2 p.564 (pdf 581))
- **Vielbein:** Bracket notation (e_mu)^{alpha-hat} and (e_{alpha-hat})^mu; conversion rules B.8; for diagonal metrics (e_mu)^{mu-hat} = sqrt|g_{mu mu}| with no sum. (GA §B.2 p.564 (pdf 581))
- **Covariant derivative:** nabla_u (directional, basis-free); nabla_mu = nabla_{e_mu} (direction label, not a component); (nabla_mu v)^alpha = v^alpha_{;mu} = partial_mu v^alpha + Gamma^alpha_{mu nu} v^nu. — Gamma's first lower index is the derivative direction. (GA §B.3 p.564 (pdf 581))
- **Derivative along a curve:** Dv/dtau = nabla_u v; components written (Dv/dtau)^alpha = u^mu v^alpha_{;mu}, never Dv^alpha/dtau. — Other books use Dv^mu/dtau for the component; the book regards this as ambiguous. (GA §B.3 p.564 (pdf 581))
- **Levels of notation:** Coordinate-free (nabla_u v), mixed ((nabla_u v)^mu, (nabla_mu v)^alpha) and coordinate (v^alpha_{;mu}). (GA §B.3 p.564 (pdf 581))

## Margin notes

- *reference* — Heaviside-Lorentz units are nearly universal in classical and quantum field-theory books, but the well-known electrodynamics texts by Jackson and by Landau and Lifshitz use other units. (GA §B.1 p.562 (pdf 579))
- *biography* — Names the units after O. Heaviside (1850-1925), English electrical engineer, and H. A. Lorentz (1853-1928), Dutch physicist. (GA §B.1 p.562 (pdf 579))
- *clarification* — Transformations in the book are passive (relabel the coordinates of a fixed event) rather than active (move the event); Coleman's crime analogy likens passive to an alias and active to an alibi. (GA §B.2 p.562 (pdf 579))
- *caution* — Remarks that upper-index components are sometimes given the name 'covariant' and that the book mostly avoids this vocabulary (note that standard physics usage calls them contravariant). (GA §B.2 p.562 (pdf 579))
- *technical-detail* — Volume symbols: script V for 4-volume and italic V for 3-volume, invariant elements d(script V) and dSigma; dOmega is kept for the angular line element even though some texts use it for 4-volume. (GA §B.2 p.563 (pdf 580))
- *caution* — Lower-index 1-form components are sometimes given the name 'contravariant' (again opposite to the usual physics usage). (GA §B.2 p.563 (pdf 580))
- *technical-detail* — A general matrix, as opposed to a tensor, is denoted by an underlined bold letter. (GA §B.2 p.563 (pdf 580))
- *clarification* — The metric is the central (0,2) tensor, with components equal to dot products of basis vectors; its determinant (not its trace) is g; the signature is (-+++) with eta = diag(-1,1,1,1); the metric components are what move indices between up and down positions. (GA §B.2 p.563 (pdf 580))
- *backward-pointer* — Compares the Chapter 30 tangent built by differentiating a displacement vector (B.6), which fails the tensor transformation law, with the Chapter 31 tangent built as a derivative operator (B.7), giving e_mu = partial/partial x^mu. (GA §B.2 p.564 (pdf 581))
- *caution* — Explains the notation hierarchy: nabla_u v is coordinate-free, (nabla_u v)^mu and (nabla_mu v)^alpha are mixed, v^alpha_{;mu} is coordinate notation; other authors write Dv^mu/dtau for the component along a curve, which the book finds ambiguous and replaces by (Dv/dtau)^mu. (GA §B.3 p.564 (pdf 581))

## Exercises

About 0 exercises (pdf pages n/a).

**Skills practiced**
_None recorded._


## Cross-references

- *backward* → **GA ch00 §0.6**: Geometrized units and the gentle introduction of c = 1 (and later G = 1).
- *backward* → **GA ch02 §2.1**: 4-vectors, Greek indices and the summation convention are first set up for flat spacetime.
- *backward* → **GA ch02 §2.2**: A margin remark there uses the standard jargon (a^mu contravariant, partial_mu phi covariant), which is the reverse of the labels in this appendix's notes 4 and 6.
- *backward* → **GA ch03 §3.2**: Coordinates are not vectors and the position vector loses meaning in general coordinates.
- *backward* → **GA ch04**: Linear slot machines: 1-forms, tensors, valence and component extraction.
- *backward* → **GA ch05 §5.4**: Metric components, metric determinant and invariant volume element.
- *backward* → **GA ch07 §7.3**: Covariant derivative components and comma/semicolon notation (B.9-B.10).
- *backward* → **GA ch07 §7.4**: Covariant derivative along a parametrized curve, D/dtau (B.11).
- *backward* → **GA ch09**: Connection coefficients Gamma computed from the metric.
- *backward* → **GA ch10 §10.2**: Vielbein, coordinate versus non-coordinate bases, conversion rules (B.8).
- *backward* → **GA ch10 §10.3**: Orthonormal frame for a diagonal metric and the square-root rule.
- *backward* → **GA ch11 §11.3**: Riemann index order and sign convention, which this appendix does not summarize.
- *backward* → **GA ch12 §12.4**: Hypersurface element dSigma and fluxes through 3-surfaces.
- *backward* → **GA ch30 §30.2**: Displacement vector X and basis vectors dX/dx^mu for curves (B.6), cited as Chapter 30.
- *backward* → **GA ch31 §31.2**: Vectors as derivative operators, e_mu = partial/partial x^mu (B.7), cited as Chapter 31.
- *backward* → **GA ch31 §31.4**: Tensors again as (n, m) slot machines and the tensor product.
- *backward* → **GA ch32 §32.2**: Wedge products defined without a factor 1/2 (u wedge v = u otimes v - v otimes u) and p-forms expanded with explicit 1/2 or 1/p! factors.
- *backward* → **GA ch36 §36.1**: First real use of the ordered index sum |alpha beta| (curvature 2-form in terms of Riemann components, eqn 36.20 and its margin note); orthonormal frames revisited.
- *backward* → **GA ch42 §42.2**: Maxwell's equations quoted in natural (Heaviside-Lorentz, c = 1) form and the Lagrangian -F_{mu nu}F^{mu nu}/4 with no 4 pi.
- *backward* → **GA ch40 §40.5**: Maxwell Lagrangian normalized without 4 pi, consistent with Heaviside-Lorentz units.
- *forward* → **GA appC**: Manifolds and bundles: the abstract points P and tangent spaces behind the field notation.
- *external* → **Jackson, Classical Electrodynamics**: Named as a major electrodynamics text that does not use Heaviside-Lorentz units.
- *external* → **Landau and Lifshitz, The Classical Theory of Fields**: Named as a major electrodynamics text that does not use Heaviside-Lorentz units.
- *external* → **Sidney Coleman (lectures on quantum field theory)**: Source of the alias/alibi image for passive and active transformations.

## Teaching gems

### Coleman's alias/alibi image: under a passive transformation the criminal (event) stays at the crime scene with a new description; under an active one the criminal is moved elsewhere. · GA §B.2 p.562 (pdf 579)

**Why it works:** A memorable story fixes an abstract distinction that otherwise causes sign errors when comparing rotations of objects and rotations of axes.

**App idea:** Two-panel interactive: rotate the axes about a fixed event (alias) or drag the event with fixed axes (alibi); a component readout confirms that equal readouts need opposite rotation angles.

### nabla_mu is a direction label, not a component; say (nabla_mu v)^alpha when you mean a component. · GA §B.3 p.564 (pdf 581)

**Why it works:** It names the single most common index-gymnastics confusion and provides a notation that makes the distinction visible.

**App idea:** Notation lens: hovering over each index in nabla_mu v^alpha or v^alpha_{;mu} highlights whether it labels a direction, a component, or a summed dummy, with an arrow drawn on a 2D grid for the direction.

### Bracket the vector before taking a component: (Dv/dtau)^alpha rather than Dv^alpha/dtau. · GA §B.3 p.564 (pdf 581)

**Why it works:** Order of operations is encoded in the notation, reminding learners that the connection term is part of the derivative.

**App idea:** Parallel-transport a vector along a latitude on a sphere: plot dv^theta/dtau (non-zero) beside (Dv/dtau)^theta (zero) as the learner changes latitude.

### Separate the field's position argument from its slots: v(x) says where, the slot says what it eats. · GA §B.2 p.564 (pdf 581)

**Why it works:** Prevents a conflation that becomes serious once tensor fields, derivatives and slot insertions appear in the same expression.

**App idea:** Click a point on a vector field to freeze v(x), then drop a gradient 1-form (drawn as contour lines) onto the frozen arrow to see the pairing number counted as crossings.

### Square-root rule: for a diagonal metric, divide each coordinate basis vector by sqrt|g_{mu mu}| to get the orthonormal frame. · GA §B.2 p.564 (pdf 581)

**Why it works:** Turns the vielbein from abstract machinery into a one-line recipe that learners can apply to Schwarzschild or Robertson-Walker immediately.

**App idea:** Pick a diagonal metric (polar plane, sphere, Schwarzschild at chosen r); the app draws coordinate basis arrows and their rescaled hatted counterparts, with the lengths sqrt|g_{mu mu}| shown as sliders update r.

### Two generations of the tangent vector side by side: differentiate a displacement vector (fails in curved spacetime) versus define the tangent as a derivative operator. · GA §B.2 p.564 (pdf 581)

**Why it works:** Shows why the abstract definition is needed rather than asserting it, and reassures learners that the components dx^mu/dtau are unchanged.

**App idea:** Curve drawn on a sphere: the displacement-chord construction visibly leaves the surface while the derivative-operator tangent stays in the tangent plane; both show identical components.

### Typography encodes object type: arrow (3-vector), bold (basis-free 4-object), tilde (1-form), hat (orthonormal frame), index height (vector vs 1-form). · GA §B.2 p.563 (pdf 580)

**Why it works:** Gives learners a consistency check on every equation, similar to dimensional analysis.

**App idea:** Equation type-checker: learner builds an expression from symbol tiles and the app flags mismatched index heights, unsummed repeated indices or bold/component mixing.


## Gaps and pitfalls

- **Equation B.3 prints e_mu twice in the basis product; the second factor should be e_nu.** — A reader checking index balance finds a repeated free index and cannot match the ordering of components to basis factors. *Suggestion:* Present S = S^{mu nu}_{alpha beta} e_mu otimes e_nu otimes omega^alpha otimes omega^beta and point out the slip.
- **Margin notes 4 and 6 attach 'covariant' to upper-index components and 'contravariant' to lower-index components, the reverse of the standard physics convention and of the book's own usage in Chapter 2 (section 2.2).** — Learners who read other GR or tensor-analysis books will meet the opposite labels and may conclude they misunderstood index placement. *Suggestion:* State the standard usage (upper = contravariant, lower = covariant), note that terminology varies, and prefer 'vector components' and '1-form components'.
- **The pairing sentence says angle brackets pair 1-forms with tensors; the example pairs a 1-form with a vector.** — Suggests a general tensor can be fed to a 1-form directly. *Suggestion:* Say 1-forms and vectors; mention that contraction with tensors requires choosing slots.
- **Numeric index labels are illustrated as mu = 1...4, while the rest of the appendix and book use mu = 0, 1, 2, 3.** — Confusion over which component is timelike when reading a component table. *Suggestion:* Use 0...3 consistently with 0 as the timelike index.
- **The directional derivative is written nabla_u = u . nabla_{e_mu}; the intended expression is u^mu nabla_{e_mu}.** — A dot suggests a metric contraction between a vector and a derivative operator, which is not meaningful here. *Suggestion:* Write nabla_u = u^mu nabla_mu and explain linearity in the direction argument.
- **Margin note 9 writes the tangent components as partial x^mu/partial tau; along a single-parameter curve it is an ordinary derivative.** — Minor, but inconsistent with the main text's dx^mu/dtau. *Suggestion:* Use dx^mu/dtau throughout.
- **Heaviside-Lorentz units are described as SI with epsilon_0 = mu_0 = 1, yet B.2 retains 1/c factors that do not follow from that substitution; the real conversion rescales E, B and charge.** — Learners who try the substitution cannot reproduce B.2 and may distrust their algebra. *Suggestion:* Give the rescalings E_HL = sqrt(epsilon_0) E_SI, B_HL = B_SI/sqrt(mu_0), q_HL = q_SI/sqrt(epsilon_0), and note that with c = 1 the shortcut is exact.
- **The wedge product is defined without a factor 1/2 while the antisymmetrization bracket has one; the relation between them is not stated.** — Factor-of-2 errors in components of 2-forms, field strengths and curvature 2-forms. *Suggestion:* Add (v wedge u)^{alpha beta} = 2 v^{[alpha} u^{beta]} and compare with texts that normalize differently.
- **As a conventions summary it omits several choices a GR reader most often needs: the covariant derivative of 1-forms (minus sign), the Christoffel formula, Riemann and Ricci index order and sign, the sign of the Einstein equation, G = 1, and the Levi-Civita tensor sign.** — Comparing results with other textbooks (for example Wald or Weinberg) requires hunting through the chapters. *Suggestion:* In the app's conventions card, add these rows with links to GA ch07, ch09, ch11 §11.3, ch13 and ch37.
- **Several distinctions are carried only by typeface (script V versus italic V, bold versus italic, underline for matrices, tilde for 1-forms), and the exported text already lost some of them (for example the comma in f_{,mu}).** — In plain text, screen readers or a voice tutor the distinctions vanish, producing ambiguous symbols. *Suggestion:* Speak the type explicitly ('the one-form A', 'script V, the four-volume') and render symbols with clear visual markers in the app.

## Tutor notes

- Treat this appendix as a lookup resource, not a lesson: retrieve an entry when a learner is confused by a symbol, then return to the chapter where the object is taught.
- When a learner asks 'is this a vector or a 1-form?', check index height and typography first (upper index or bold without tilde means vector; lower index or tilde means 1-form), then confirm by asking what the object eats.
- Before discussing covariant derivatives, ask: 'In nabla_mu v, what does the mu tell you?' A correct answer is 'the direction of differentiation'; if the learner says 'a component', walk through B.9 and write (nabla_mu v)^alpha explicitly.
- For voice delivery, always name the type: say 'the one-form A-tilde', 'the hatted, orthonormal-frame component', 'script V, the four-volume', since bold and tildes are inaudible.
- Check sign conventions early when a learner uses another source: confirm signature (-+++), so timelike vectors have negative norm and u.u = -1; learners from particle physics often expect (+---).
- If a learner reads 'covariant components' elsewhere, clarify that most physics sources mean lower-index components and that this book's margin notes label them the other way; recommend saying 'vector components' and '1-form components'.
- A quick check for the vielbein: give ds^2 = -dt^2 + dr^2 + r^2 dtheta^2 + r^2 sin^2 theta dphi^2 and ask for (e_theta)^{theta-hat} and (e_phi)^{phi-hat} using the square-root rule (answers r and r sin theta).
- A quick check for the passive convention: ask whether rotating the axes by +30 degrees changes the components of a fixed vector the same way as rotating the vector by +30 degrees with fixed axes (no: the sense is opposite).
- When electromagnetism appears (Part VI), remind learners that Maxwell's equations there are Heaviside-Lorentz with c = 1, so no epsilon_0, mu_0 or 4 pi appears except in the point-charge potential.
- Common learner question: 'Why not just use position vectors?' Answer with the sphere: the chord between two points leaves the surface, so only points, coordinates and tangent vectors at a point make sense.
- Common learner question: 'Is the wedge product just antisymmetrization?' Answer yes up to normalization: in this book v wedge u has components twice the bracket antisymmetrization.

## Verification

**Verdict:** fixed

**Fixes applied**
- Rewrote prose that tracked source wording too closely: the definitions of tensor valence, invariant volume elements, orthonormal frame components and 4-vector; the how_introduced for four-velocity; the Heaviside-Lorentz historical note; the metric margin-note summary.
- Found that the book contradicts itself on covariant/contravariant: Chapter 2 section 2.2 uses the standard labels, which appendix notes 4 and 6 reverse. Recorded this in the concept note and the gap entry, and added a ch02 section 2.2 cross-reference.
- Corrected the ch32 section 2.2 cross-reference: ordered |mu nu| sums do not appear in ch32; they first appear in ch36 section 36.1 (eqn 36.20). Made the ch36 and ch42 cross-reference reasons concrete, after checking the ch42 natural-units Maxwell equations and the -FF/4 Lagrangian.
- Removed the style tag 'components-first', which contradicts the appendix's practice of pairing coordinate-free and component forms.
- Marked the 'typography as a type system' analogy as an implicit framing, not an analogy the book states.
- Reworded the key-equation meaning for the metric, which wrongly implied the signature holds only in an inertial frame of flat spacetime.

**Residual concerns**
- Several printed slips in the book are recorded in gaps_and_pitfalls and in equation notes, not silently corrected: the repeated e_mu in B.3, 'tensors' for vectors in the pairing sentence, mu = 1...4, the dot in nabla_u = u . nabla_{e_mu}, and the partial derivative in note 9.
- The Heaviside-Lorentz rescalings (E, B, q by powers of sqrt(epsilon_0), sqrt(mu_0)) come from the dossier author, not the book; I checked them algebraically against B.1 and B.2.
- The appendix has no figures, worked examples or exercises. The two worked_examples entries are short calculations embedded in the text and margin note 9, not formal Example blocks.

**Coverage:** toc_sections: 3, sections: 6, inventory_figures: 0, figures: 0, inventory_examples: 0, worked_examples: 2, concepts: 43, key_equations: 26, locators_checked: 40, locators_wrong: 0, pages_rendered: 3
