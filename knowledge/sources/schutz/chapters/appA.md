---
type: "source-unit"
book: "schutz"
book_short: "SCH"
unit: "appA"
title: "Summary of linear algebra"
part: null
printed_pages: [468, 471]
pdf_pages: [486, 489]
math_level: 2
conceptual_level: 2
novice_friendliness: 3
style_tags: ["axiomatic-mathematical", "components-first", "survey-overview", "computational-recipe"]
concepts: ["vector space", "abelian group", "field of scalars", "linear independence", "dimension of a vector space", "basis", "components of a vector", "inner product", "positive-definite inner product", "norm of a vector", "indefinite inner product", "orthogonality", "orthonormal basis", "nonorthogonal basis", "basis dependence of components", "square matrix", "matrix element indexing", "dimension of a matrix", "column vector", "matrix action on a column vector", "vector space of matrices", "Frobenius inner product", "algebra", "matrix multiplication", "associativity and non-commutativity of matrix multiplication", "Kronecker delta", "identity matrix", "determinant", "minor", "cofactor", "cofactor expansion", "matrix inverse", "adjugate formula for the inverse", "invertibility condition", "Einstein summation convention", "metric tensor"]
verification: "fixed"
---

# SCH appA · Summary of linear algebra

> A four-page reference digest of the linear algebra the book leans on: real vector spaces and their axioms, linear independence, bases and components, symmetric bilinear inner products (including the indefinite kind relativity needs), orthonormal versus skew bases, square matrices acting on column vectors, the matrix algebra, cofactor-expansion determinants and the cofactor formula for the inverse.

**Pages:** printed 468–471 · pdf 486–489 · **Difficulty:** math 2/5, conceptual 2/5, novice-friendliness 3/5

Standard first-year linear algebra in compressed reference form. It is easy for anyone who has taken a linear algebra course, but a true novice gets no pictures, no geometric meaning for determinants, no proofs of the asserted facts (row independence, det != 0 criterion, positivity of the matrix inner product), group-theory vocabulary without definitions, a printed typo in the 2x2 product, and index conventions (lower Latin indices, explicit sums) that differ from the main text. Transpose, trace, eigenvalues, det(AB) = det A det B and dual bases, all used or useful later, are absent.

## Role in the book

Appendix A is a look-up sheet, not a chapter to be taught in sequence. The preface advertises it as the place that collects the linear algebra used in the text, and the author openly assumes the reader has met all of it. Its content is quietly load-bearing from Chapter 2 onward: Lorentz transformations are 4x4 matrices whose products and inverses matter (Ch. 2), the metric is a symmetric bilinear but indefinite inner product whose matrix must be invertible to raise indices (Ch. 3), coordinate changes need a nonvanishing Jacobian determinant and polar bases are neither unit nor constant (Ch. 5), the volume element and the derivative of the metric determinant use determinants and cofactors (Ch. 6), and later chapters invert metric blocks and response matrices (Chs. 11-12). The appendix therefore acts as the shared vocabulary that the geometric, one-form-based presentation of tensors rests on, while deliberately staying in plain matrix-and-component language without the arrow/tilde notation, upper indices or summation convention of the main text.

## Learning objectives

- Reader can check whether a proposed set with addition and real scaling satisfies the vector-space axioms, and recognises that column vectors and square matrices both qualify.
- Reader can test a finite set of vectors for linear independence and explain why a basis of an n-dimensional space lets every vector be expanded in n components.
- Reader can state the two defining properties of the book's inner product (symmetry and linearity) and distinguish a positive-definite inner product from an indefinite one.
- Reader can compute the magnitude of a vector under an indefinite inner product using the absolute-value convention and explain what the sign of A.A still tells you.
- Reader can re-express vectors in a nonorthogonal basis and explain why a component changes even when the corresponding basis vector is unchanged.
- Reader can multiply a column vector by a matrix and two matrices together, both in explicit 2x2 form and in index notation, naming which index is summed.
- Reader can explain why n x n matrices form an n^2-dimensional vector space and an algebra, and give an example showing matrix multiplication does not commute.
- Reader can evaluate a 2x2, 3x3 or 4x4 determinant by cofactor expansion along any row, forming the submatrices S_lm and minors D_lm correctly.
- Reader can build the inverse of a small matrix from minors, keeping the transposed index order D_ji, and state that it exists exactly when the determinant is nonzero.
- Reader can connect these tools to their uses in the book: composing and inverting Lorentz matrices, inverting the metric, and Jacobian and metric determinants.

## Assumed background

- Real numbers and their arithmetic (commutativity, distributivity, multiplicative identity) — school-math
- Sets, elements and the idea of a binary operation; the word 'group' for a set with an invertible, associative operation — linear-algebra (The appendix uses 'abelian group' without defining it.)
- Sigma notation for finite sums and double sums — school-math
- Cartesian coordinates and unit basis vectors in the Euclidean plane — school-math (Used in the nonorthogonal-basis practice problem on p.469.)
- Prior exposure to vectors, matrices and determinants; the appendix explicitly hopes nothing in it is new — linear-algebra (Opening sentence, p.468.)
- Indefinite scalar product of four-vectors, with timelike, spacelike and null vectors — earlier-in-this-book (SCH ch2 §2.5; motivates the remark on indefinite inner products on p.469.)

## Teaching approach

A terse, axiom-then-formula reference card. Each topic is introduced by a definition in words, pinned down by an explicit 2x2 (or 3x3) display, rewritten with indices and an explicit sigma, and then generalised to n dimensions. The only pedagogical interruptions are a do-it-yourself problem on a skew basis and short 'notice that' remarks pointing at which index is summed or that multiplication does not commute. The single relativity-specific remark concerns indefinite inner products. There are no figures, no geometric interpretation of determinants, and no exercises section.

**Style:** axiomatic-mathematical, components-first, survey-overview, computational-recipe

**Narrative arc**

1. Reassure the reader that this is a recap of familiar material collected for convenience.
2. Define a real vector space axiomatically (abelian group under addition plus four rules for real scaling) and note that other number fields are possible but unneeded.
3. Build the counting machinery: linear independence, dimension as the maximum independent set, basis, and components as expansion coefficients.
4. Add an inner product as a symmetric bilinear rule, split into positive-definite (norm via square root) and indefinite (norm via absolute value, the relativistic case), and define orthogonality.
5. Recommend but do not require orthonormal bases, then pose a hands-on skew-basis problem that exposes how components depend on the whole basis.
6. Switch to matrices: square arrays, row/column indexing, column vectors, and the matrix-vector product first explicitly, then with a sum over the second index.
7. Observe that matrices themselves form a vector space (dimension n^2) with a natural positive-definite inner product, then elevate multiplication as the important structure and name the resulting algebra.
8. Give the product rule explicitly and in index form, stress the summed index, and state associativity, non-commutativity and the Kronecker-delta identity.
9. Define the 2x2 determinant, then introduce submatrices and minors via a 3x3 example and define the n x n determinant recursively by expansion along any row.
10. Close with the cofactor formula for the inverse and the criterion that it exists precisely when the determinant does not vanish.

**Signature moves**

- Three-step ladder for every operation: an explicit 2x2 display, the same rule as an indexed sum up to 2, then the identical sum up to n.
- Pointed 'notice' remarks that name the position of the summed index (second index of A; second of A and first of B), anticipating index-placement discipline in tensor contractions.
- An embedded try-it-yourself problem in which one new basis vector coincides with a Cartesian one, yet the corresponding components differ, so the learner discovers basis dependence rather than being told it.
- The inner product is defined without positivity, and positivity is then added as an optional extra, so the indefinite spacetime case is structurally on equal footing rather than an exception.
- Reuses the vector-space axioms on non-arrow objects (column vectors, matrices) to show the abstraction pays off immediately.
- Determinant defined recursively, so a 4x4 (the spacetime case) is reduced to 3x3 and then 2x2 determinants, with the claim that the row chosen does not matter.

## Section by section

### Opening and the axioms of a vector space — p.468 (pdf 486)

States that the appendix gathers linear algebra used in the text and assumes it is familiar. A real vector space is defined by requiring that addition makes the set a commutative group with a zero element, and that multiplying by reals distributes over both kinds of sum, composes with real multiplication and leaves vectors unchanged when the factor is 1. Complex or general fields are mentioned only to be set aside.

**Concepts:** vector space, abelian group, field of scalars

**Key moves**
- Package closure, commutativity, associativity, zero and negatives into the single phrase 'abelian group under +'.
- List four compatibility rules between real scaling and addition.
- Restrict attention to the real numbers as scalars.

### Linear independence, dimension, basis and components — p.468 (pdf 486)

Defines independence by the impossibility of a nontrivial linear combination equal to zero, takes the dimension to be the size of the largest independent set, and calls any independent set of that size a basis. Adding any extra vector to a basis produces a dependent set, from which it follows that the extra vector is a linear combination of the basis; the coefficients are its components.

**Concepts:** linear independence, dimension of a vector space, basis, components of a vector

**Key moves**
- Phrase independence negatively: no choice of not-all-zero coefficients gives the zero vector.
- Define dimension as the maximal independent set size, then a basis as an independent set of exactly that size.
- Argue expansion in a basis from the dependence of the enlarged set {B, A_1, ..., A_n}.

### Inner products, norms and orthogonality — p.468 (pdf 486)

An inner product assigns a real number to each ordered pair of vectors, is symmetric, and is linear in its first slot (hence bilinear). If A.A is positive for every nonzero A the product is positive-definite and the norm is the square root of A.A. Relativity instead uses indefinite products where A.A can take either sign, and the magnitude is then taken as the square root of the absolute value. Orthogonality means a vanishing inner product. The section straddles pp. 468-469.

**Concepts:** inner product, positive-definite inner product, norm of a vector, indefinite inner product, orthogonality, metric tensor

**Key moves**
- Define the inner product using only symmetry and linearity, leaving positivity as an optional extra property.
- Introduce the norm only for the positive-definite case, then patch it with an absolute value for the indefinite case used in relativity.
- Define orthogonality purely algebraically, with no appeal to angles.

### Orthonormal and nonorthogonal bases: a practice problem — p.469 (pdf 487)

Orthonormal bases (mutually orthogonal, unit magnitude) are called convenient but optional. Readers new to skew bases are invited to take two Cartesian vectors in the plane and rewrite them in a basis whose first member equals the Cartesian x unit vector while the second is the difference of the y and x unit vectors, and to observe that the first component in the new basis does not match the x component even though the first basis vectors coincide. No answer is printed.

**Concepts:** orthonormal basis, nonorthogonal basis, basis dependence of components, components of a vector

**Key moves**
- Assert that orthonormality is a convenience, not a requirement.
- Choose a skew basis that shares one vector with the Cartesian basis to isolate the effect of the other vector on components.
- Leave the computation to the reader as a self-check.

### Matrices and their action on column vectors — p.469 (pdf 487)

Restricts to square arrays, gives two sample matrices (2x2 and 3x3), calls the number of rows the matrix's dimension, and fixes the convention that A_ij sits in row i and column j. Column vectors are lists of numbers forming a vector space; a matrix turns a column vector into another by summing products along each row, shown explicitly for 2x2 and then as a sum over j running to n, with emphasis that the summation runs over the matrix's second index.

**Concepts:** square matrix, matrix element indexing, dimension of a matrix, column vector, matrix action on a column vector

**Key moves**
- Row index first, column index second.
- Write V = A.W out component by component in 2x2 form.
- Compress to V_i = sum_j A_ij W_j and flag that the sum is on A's second index.

### The matrix algebra: vector space structure and multiplication — p.470 (pdf 488)

Entrywise addition and scaling make n x n matrices an n^2-dimensional vector space, which carries a natural inner product (sum of products of corresponding entries) that is positive-definite. Multiplication matters more; a vector space equipped with a product is an algebra. The 2x2 product is displayed and then written as C_ij = sum_k A_ik B_kj, with the summed index being the second of A and first of B. Multiplication is associative, not commutative, and has the Kronecker-delta matrix as identity. The explicit 2x2 display contains a printed typo in the (1,1) entry.

**Concepts:** vector space of matrices, Frobenius inner product, algebra, matrix multiplication, associativity and non-commutativity of matrix multiplication, Kronecker delta, identity matrix

**Key moves**
- Recognise matrices as vectors in their own right (n^2 components).
- Promote multiplication from a side remark to the central structure, naming the algebra.
- Contract the inner indices: second of A with first of B.
- State associativity and non-commutativity without proof.

### Determinants by cofactor expansion — p.470 (pdf 488)

Gives the 2x2 determinant, then for an n x n matrix defines the submatrix S_lm obtained by deleting row l and column m and its determinant D_lm. A 3x3 example deletes row 1 and column 2 to obtain S_12 and D_12. The general determinant is the alternating-sign sum of entries of any fixed row times their minors; the value is claimed independent of the chosen row, and the rule builds 3x3 from 2x2, 4x4 from 3x3, and so on. Continues onto p.471.

**Concepts:** determinant, minor, cofactor, cofactor expansion

**Key moves**
- Anchor with the familiar 2x2 formula.
- Construct S_lm and D_lm concretely on a 3x3 example.
- Define det recursively along an arbitrary row with sign (-1)^(i+j), and assert row independence.

### The inverse matrix — p.471 (pdf 489)

Because matrices can be multiplied, a multiplicative inverse can be sought. Its (i,j) entry is the signed minor with indices swapped, D_ji, divided by the determinant, and the inverse exists if and only if the determinant is nonzero. The appendix ends here.

**Concepts:** matrix inverse, adjugate formula for the inverse, invertibility condition

**Key moves**
- Motivate the inverse from the existence of a product and identity.
- Write the inverse from transposed signed minors over the determinant.
- Tie existence to a nonzero determinant.

## Concepts

### vector space

*definition · introduced* · also: linear space, real vector space

A set closed under an addition that is commutative, associative, has a zero element and additive inverses, together with multiplication by real numbers that distributes over vector sums and over sums of scalars, satisfies (ab)A = a(bA), and has 1A = A.

**How introduced:** First entry of the appendix, given as two axiom groups: a one-line 'abelian group' requirement for addition and four enumerated rules for real scaling.

**Prerequisites:** abelian group, field of scalars

$$
A + B = B + A \in V,\quad A + 0 = A
$$

$$
a(A+B) = aA + aB,\ (a+b)A = aA + bA,\ (ab)A = a(bA),\ 1A = A
$$

**Notes:** Throughout the main text the four-vectors, one-forms and tensors of each type are all instances; the appendix itself exhibits column vectors and matrices as further examples.

**Where:** SCH p.468 (pdf 486)

### abelian group

*definition · mention* · also: commutative group

A set with a binary operation that is associative and commutative, has an identity element, and gives every element an inverse.

**How introduced:** Used without definition inside the first vector-space axiom; the parenthetical only displays commutativity, closure and the zero element.

$$
A + B = B + A,\quad A + 0 = A
$$

**Notes:** Additive inverses and associativity are hidden inside the word 'group'; learners without abstract algebra may miss them.

**Where:** SCH p.468 (pdf 486)

### field of scalars

*definition · mention* · also: ground field, real versus complex scalars

The number system (here the real numbers) by which vectors may be multiplied; it must allow addition, multiplication and division by nonzero elements. Complex numbers are the other common choice.

**How introduced:** A one-sentence aside after the axioms says the definition could use complex numbers or any field but the book will not need that.

**Notes:** The book's tensors are all real. The only nearby hint of other structures is a Ch. 3 §3.5 aside about a two-dimensional spinor space with an antisymmetric 'metric', which the book declares out of scope; complex numbers otherwise enter only through quantum topics such as the Hawking effect.

**Where:** SCH p.468 (pdf 486)

### linear independence

*definition · introduced* · also: linearly independent set, linear dependence

A set of vectors is linearly independent when the only linear combination of them equal to the zero vector has every coefficient zero; otherwise it is linearly dependent.

**How introduced:** Stated in the negative form: there are no real coefficients, not all zero, making the combination vanish.

**Prerequisites:** vector space

$$
aA + bB + \dots + fF = 0 \;\Rightarrow\; a = b = \dots = f = 0
$$

**Where:** SCH p.468 (pdf 486)

### dimension of a vector space

*definition · introduced* · also: dimension

The largest number of vectors in the space that can be linearly independent; equivalently the number of vectors in any basis.

**How introduced:** Defined immediately after independence as the size of a maximal independent set, before bases are named.

**Prerequisites:** linear independence

**Notes:** Spacetime vectors have dimension 4; the n x n matrices have dimension n^2 (p.470).

**Where:** SCH p.468 (pdf 486)

### basis

*definition · introduced* · also: basis set, basis vectors

A linearly independent set containing as many vectors as the dimension of the space, so that every vector is expressible as a weighted sum of its members (and, though the appendix does not say so, uniquely).

**How introduced:** Defined as any independent set of size n; the spanning property is then derived by noting that adjoining one more vector must create dependence.

**Prerequisites:** linear independence, dimension of a vector space

$$
B = b_1 A_1 + b_2 A_2 + \dots + b_n A_n
$$

**Notes:** Uniqueness of the expansion follows from independence of the basis but is not stated in the appendix.

**Where:** SCH p.468 (pdf 486)

### components of a vector

*definition · introduced* · also: expansion coefficients, components on a basis

The real numbers b_1, ..., b_n such that B = sum_i b_i A_i for a chosen basis {A_i}; they depend on the entire basis, not only on the vector.

**How introduced:** Named right after the basis expansion; revisited on p.469 when the skew-basis problem shows components shifting under a change of basis.

**Prerequisites:** basis

$$
B = \sum_{i=1}^{n} b_i A_i
$$

**Notes:** The appendix writes components with lower indices; the main text writes vector components with upper indices (A^alpha) and reserves lower indices for one-form components.

**Where:** SCH p.468 (pdf 486); SCH p.469 (pdf 487)

### inner product

*definition · introduced* · also: scalar product, dot product, symmetric bilinear form

A rule giving a real number A.B for every pair of vectors that is symmetric (A.B = B.A) and linear in each argument; in the appendix positivity is not part of the definition.

**How introduced:** Defined by just two listed properties, symmetry and linearity in the first slot; the book then labels the map symmetric because of the first and bilinear because of the second (bilinearity in both slots really needs the two together).

**Prerequisites:** vector space

$$
A\cdot B = B\cdot A
$$

$$
(aA + bB)\cdot C = a(A\cdot C) + b(B\cdot C)
$$

**Notes:** Standard treatments of indefinite metrics also demand nondegeneracy (only the zero vector is orthogonal to everything); the appendix omits this, although the invertibility of the metric used in SCH ch3 §3.6 depends on it.

**Where:** SCH p.468 (pdf 486)

### positive-definite inner product

*definition · introduced* · also: Euclidean inner product, positive definiteness

An inner product for which A.A > 0 for every nonzero vector A.

**How introduced:** Introduced as a special property an inner product may or may not have, in order to define the norm.

**Prerequisites:** inner product

$$
A\cdot A > 0\ \ \forall A \neq 0
$$

**Notes:** The natural inner product on matrices (p.470) is asserted to be of this kind.

**Where:** SCH p.468 (pdf 486)

### norm of a vector

*definition · introduced* · also: magnitude, length

For a positive-definite inner product, |A| = (A.A)^(1/2); for an indefinite one the book's convention is |A| = |A.A|^(1/2), which is always real but discards the sign of A.A.

**How introduced:** Defined for the positive-definite case at the foot of p.468 and patched with an absolute value for relativity at the top of p.469.

**Prerequisites:** inner product, positive-definite inner product

$$
|A| \equiv (A\cdot A)^{1/2}
$$

$$
|A| \equiv |A\cdot A|^{1/2}
$$

**Where:** SCH p.468 (pdf 486); SCH p.469 (pdf 487)

### indefinite inner product

*definition · introduced* · also: pseudo-inner product, Lorentzian inner product, non-positive-definite inner product

An inner product for which A.A is positive for some vectors and negative for others (and can vanish for nonzero vectors); the Minkowski scalar product of four-vectors is the key example.

**How introduced:** The appendix's only explicitly relativistic sentence: relativity works with inner products of this kind, so magnitude needs an absolute value.

**Prerequisites:** inner product

$$
|A| \equiv |A\cdot A|^{1/2}
$$

**Notes:** The appendix does not mention that such products allow nonzero vectors of zero magnitude (null vectors), which the main text treats in SCH ch2 §2.5.

**Where:** SCH p.469 (pdf 487)

### orthogonality

*definition · introduced* · also: orthogonal vectors, perpendicularity

Two vectors are orthogonal exactly when their inner product is zero.

**How introduced:** One-line algebraic definition following the norm; no geometric angle is invoked.

**Prerequisites:** inner product

$$
A\cdot B = 0
$$

**Notes:** With an indefinite product a null vector is orthogonal to itself, and spacetime-orthogonal vectors need not look perpendicular on a diagram.

**Where:** SCH p.469 (pdf 487)

### orthonormal basis

*definition · introduced* · also: orthonormal set

A basis whose members are mutually orthogonal and each have magnitude one.

**How introduced:** Recommended for convenience and immediately declared unnecessary, as a lead-in to the skew-basis problem.

**Prerequisites:** basis, orthogonality, norm of a vector

$$
A_i\cdot A_j = 0\ (i\neq j),\qquad |A_k| = 1
$$

**Notes:** Under an indefinite product the condition becomes A_i.A_j = +-delta_ij (eta_ij in spacetime), which the appendix's absolute-value norm hides.

**Where:** SCH p.469 (pdf 487)

### nonorthogonal basis

*definition · introduced* · also: skew basis, oblique basis

A basis whose vectors are not all mutually orthogonal (and possibly not of unit length); it is as valid as an orthonormal one for expanding vectors, but components can no longer be read off as inner products with the basis vectors.

**How introduced:** Through a hands-on problem in the Euclidean plane using e_1 = e_x and e_2 = e_y - e_x.

**Prerequisites:** basis, orthogonality

$$
e_1 = e_x,\qquad e_2 = e_y - e_x
$$

**Notes:** Prepares for the polar-coordinate basis of SCH ch5 whose vectors are orthogonal but not unit, and for general coordinate bases in curved manifolds.

**Where:** SCH p.469 (pdf 487)

### basis dependence of components

*principle · introduced* · also: components depend on the whole basis

The component of a vector along a given basis vector is determined by the full set of basis vectors; changing any other member of the basis can change it even if that basis vector is untouched.

**How introduced:** Made concrete by the practice problem: e_1 equals e_x yet A and B have different 1 and x components.

**Prerequisites:** components of a vector, nonorthogonal basis

$$
A = 5e_x + e_y = 6e_1 + e_2
$$

**Notes:** The explicit numbers are this dossier's solution, not printed in the book. The idea underlies transformation laws of components throughout SCH ch2-ch3 and the dual-basis construction of one-forms.

**Where:** SCH p.469 (pdf 487)

### square matrix

*mathematical-object · introduced* · also: matrix, n x n matrix

A square array of real numbers with the same number of rows and columns.

**How introduced:** Defined as an array of numbers, with only square ones considered; illustrated by a 2x2 and a 3x3 numerical example.

$$
\begin{pmatrix}1 & 2\\ 3 & 1\end{pmatrix},\qquad \begin{pmatrix}1 & 2 & 5\\ -6 & 3 & 18\\ 10^5 & 0 & 0\end{pmatrix}
$$

**Where:** SCH p.469 (pdf 487)

### matrix element indexing

*convention · introduced* · also: A_ij convention, row-column index order

The entry A_ij of a matrix lies in row i and column j; the first index labels the row, the second the column.

**How introduced:** Stated when displaying the general 2x2 matrix.

**Prerequisites:** square matrix

$$
\mathbf{A} = \begin{pmatrix}A_{11} & A_{12}\\ A_{21} & A_{22}\end{pmatrix}
$$

**Notes:** For Lorentz matrices Lambda^alpha-bar_beta in SCH ch2 the upper (row) and lower (column) positions carry the same row-column meaning.

**Where:** SCH p.469 (pdf 487)

### dimension of a matrix

*convention · mention* · also: size of a matrix, order of a matrix

In this appendix, the number of rows (equal to the number of columns) of a square matrix.

**How introduced:** A one-line naming convention after the sample matrices.

**Prerequisites:** square matrix

**Notes:** Clashes in wording with p.470, where the vector space of n x n matrices has dimension n^2; many texts say 'order' or 'size' for the row count to avoid this.

**Where:** SCH p.469 (pdf 487)

### column vector

*mathematical-object · introduced* · also: column matrix, n-tuple of components

An ordered vertical list of n real numbers W_i; such lists form an n-dimensional vector space under entrywise addition and scaling.

**How introduced:** Defined as a set of numbers with a 2-component example, with a parenthetical noting the vector-space structure.

**Prerequisites:** vector space

$$
W = \begin{pmatrix}W_1\\ W_2\end{pmatrix}
$$

**Notes:** In the main text a column of components represents a geometric vector only after a basis is chosen.

**Where:** SCH p.469 (pdf 487)

### matrix action on a column vector

*operation · introduced* · also: matrix-vector product, linear map on components

Multiplying a column vector W by a square matrix A gives the column vector V whose i-th entry is the sum over j of A_ij W_j, i.e. row i of A paired entry by entry with W.

**How introduced:** Displayed in full for 2x2, rewritten as a sum over j to 2, generalised to n, and followed by a remark that the summation runs over A's second index.

**Prerequisites:** square matrix, column vector, matrix element indexing

$$
V_i = \sum_{j=1}^{n} A_{ij} W_j
$$

**Notes:** Same pattern as Lambda^alpha-bar_beta A^beta in SCH ch2 §2.1, where the summation convention drops the sigma.

**Where:** SCH p.469 (pdf 487)

### vector space of matrices

*mathematical-object · introduced* · also: matrix space, space of n x n matrices

The set of all n x n real matrices with entrywise addition and multiplication by reals; it is a vector space of dimension n^2.

**How introduced:** Introduced at the top of p.470 to show matrices obey the same axioms as vectors before turning to their product.

**Prerequisites:** vector space, square matrix

$$
C_{ij} = A_{ij} + B_{ij},\qquad (a\mathbf{A})_{ij} = aA_{ij}
$$

**Notes:** A concrete example that the vector-space axioms apply to objects that are not arrows, useful when learners later meet tensors as vectors in product spaces.

**Where:** SCH p.470 (pdf 488)

### Frobenius inner product

*definition · mention* · also: natural inner product on matrices, Hilbert-Schmidt inner product

The inner product of two real n x n matrices obtained by summing products of corresponding entries; it equals the trace of A^T B and is positive-definite.

**How introduced:** Offered as the natural inner product on the matrix space, with positivity left as an easy claim, then set aside as less important than multiplication.

**Prerequisites:** vector space of matrices, inner product, positive-definite inner product

$$
\mathbf{A}\cdot\mathbf{B} = \sum_{i,j} A_{ij} B_{ij}
$$

**Notes:** The name 'Frobenius' is standard but not used in the book.

**Where:** SCH p.470 (pdf 488)

### algebra

*definition · mention* · also: matrix algebra, algebra over a field

A vector space that also has a bilinear multiplication of its elements; n x n matrices with matrix multiplication are the standard example.

**How introduced:** Named in a parenthetical when matrix multiplication is introduced.

**Prerequisites:** vector space, matrix multiplication

**Where:** SCH p.470 (pdf 488)

### matrix multiplication

*operation · developed* · also: matrix product

The product C = AB of n x n matrices has entries C_ij = sum_k A_ik B_kj: row i of A paired entry by entry with column j of B.

**How introduced:** Displayed in full for 2x2 (with a typo in the (1,1) entry), rewritten with a sum over k, generalised to n, and followed by a remark that the summed index is A's second and B's first.

**Prerequisites:** square matrix, matrix element indexing

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

**Notes:** The printed explicit display gives C_11 = A_11 B_11 + A_12 B_22; the correct entry is A_11 B_11 + A_12 B_21, consistent with the index formula printed right below it.

**Where:** SCH p.470 (pdf 488)

### associativity and non-commutativity of matrix multiplication

*theorem · introduced* · also: AB is not BA, order matters in matrix products

For square matrices, (AB)C = A(BC) always holds, but AB and BA generally differ.

**How introduced:** Stated without proof or example immediately after the index formula for the product.

**Prerequisites:** matrix multiplication

$$
(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C}),\qquad \mathbf{A}\mathbf{B} \neq \mathbf{B}\mathbf{A}\ \text{in general}
$$

**Notes:** Physically important in SCH ch2 Exercise 2.13, where boosts in different directions compose to matrices that depend on the order.

**Where:** SCH p.470 (pdf 488)

### Kronecker delta

*definition · introduced* · also: delta_ij

The symbol delta_ij equal to 1 when i = j and 0 otherwise; as a matrix it is the identity.

**How introduced:** Introduced parenthetically as the entries of the identity matrix.

$$
\delta_{ij} = \begin{cases}1 & i=j\\ 0 & i\neq j\end{cases}
$$

**Notes:** The main text writes it with mixed indices, delta^alpha_beta, once upper and lower indices are distinguished (SCH ch2-ch3).

**Where:** SCH p.470 (pdf 488)

### identity matrix

*mathematical-object · introduced* · also: unit matrix

The square matrix with entries delta_ij, which leaves every matrix unchanged under multiplication from either side.

**How introduced:** Named as the multiplicative identity alongside associativity and non-commutativity.

**Prerequisites:** Kronecker delta, matrix multiplication

$$
(\mathbf{1})_{ij} = \delta_{ij}
$$

**Where:** SCH p.470 (pdf 488)

### determinant

*definition · developed* · also: det

A scalar function of a square matrix, defined for 2x2 as A_11 A_22 - A_12 A_21 and for larger matrices recursively by cofactor expansion along any row; it vanishes exactly when the matrix is not invertible.

**How introduced:** Given first as the 2x2 formula, then generalised using submatrices and minors built on a 3x3 example.

**Prerequisites:** square matrix, minor, cofactor expansion

$$
\det\mathbf{A} = A_{11}A_{22} - A_{12}A_{21}
$$

$$
\det(\mathbf{B}) = \sum_{j=1}^{n} (-1)^{i+j} B_{ij} D_{ij}
$$

**Notes:** No geometric meaning (signed area or volume scaling) and no product rule det(AB) = det A det B is given, although SCH ch6 uses the product rule for the metric determinant.

**Where:** SCH p.470 (pdf 488); SCH p.471 (pdf 489)

### minor

*definition · introduced* · also: D_lm, submatrix S_lm, first minor

For an n x n matrix B, the minor D_lm is the determinant of the (n-1) x (n-1) submatrix S_lm obtained by deleting row l and column m.

**How introduced:** Defined in words, then built concretely by striking row 1 and column 2 of a general 3x3 matrix.

**Prerequisites:** square matrix, determinant

$$
\mathbf{S}_{12} = \begin{pmatrix}B_{21} & B_{23}\\ B_{31} & B_{33}\end{pmatrix},\qquad D_{12} = B_{21}B_{33} - B_{23}B_{31}
$$

**Where:** SCH p.470 (pdf 488); SCH p.471 (pdf 489)

### cofactor

*definition · introduced* · also: signed minor

The signed minor (-1)^(i+j) D_ij associated with entry B_ij; the signs form a checkerboard pattern starting with + in the top-left.

**How introduced:** Not named in the appendix, but appears as the factor multiplying B_ij in the determinant expansion and, transposed, in the inverse formula.

**Prerequisites:** minor

$$
(-1)^{i+j} D_{ij}
$$

**Notes:** SCH ch6 Exercise 6.7 asks for 'the definition of the determinant in terms of cofactors', so the word matters even though the appendix does not use it.

**Where:** SCH p.471 (pdf 489)

### cofactor expansion

*technique · developed* · also: Laplace expansion, expansion by minors, recursive determinant

The determinant of an n x n matrix equals the sum, along any fixed row i, of each entry times its cofactor; the result does not depend on the row chosen, and applying the rule repeatedly reduces any determinant to 2x2 ones.

**How introduced:** Presented as the definition of the general determinant, with the claim of row independence and the recursive ladder 2x2 to 3x3 to 4x4.

**Prerequisites:** minor, cofactor, determinant

$$
\det(\mathbf{B}) = \sum_{j=1}^{n} (-1)^{i+j} B_{ij} D_{ij}\quad \text{(any fixed } i)
$$

**Notes:** Row independence is asserted without proof; expansion along a column also works but is not mentioned.

**Where:** SCH p.471 (pdf 489)

### matrix inverse

*definition · introduced* · also: multiplicative inverse, B^{-1}

The matrix B^{-1} satisfying B B^{-1} = B^{-1} B = 1, when such a matrix exists.

**How introduced:** Motivated as a consequence of having a matrix product (and identity), then given directly by the cofactor formula.

**Prerequisites:** matrix multiplication, identity matrix

$$
\mathbf{B}\mathbf{B}^{-1} = \mathbf{B}^{-1}\mathbf{B} = \mathbf{1}
$$

**Notes:** The defining relation BB^{-1} = 1 is not written out in the appendix; it is implied by the word 'multiplicative inverse'.

**Where:** SCH p.471 (pdf 489)

### adjugate formula for the inverse

*identity · introduced* · also: cofactor formula for the inverse, classical adjoint formula

The entries of the inverse are the transposed cofactors divided by the determinant: (B^{-1})_ij = (-1)^(i+j) D_ji / det B.

**How introduced:** Final displayed formula of the appendix, given without derivation.

**Prerequisites:** cofactor, determinant, matrix inverse

$$
(\mathbf{B}^{-1})_{ij} = (-1)^{i+j} D_{ji}/\det(\mathbf{B})
$$

**Notes:** Note the swapped indices D_ji. For symmetric matrices such as a metric the swap is invisible, which can hide transcription errors.

**Where:** SCH p.471 (pdf 489)

### invertibility condition

*theorem · introduced* · also: nonzero determinant criterion, singular matrix

A square matrix has an inverse if and only if its determinant is not zero; a matrix with zero determinant is called singular.

**How introduced:** Closing sentence of the appendix, read off from the division by det B in the inverse formula.

**Prerequisites:** determinant, matrix inverse

$$
\exists\,\mathbf{B}^{-1} \iff \det(\mathbf{B}) \neq 0
$$

**Notes:** Used in SCH ch3 §3.6 to guarantee the inverse metric eta^{alpha beta} exists (det eta = -1) and in SCH ch5 §5.2 for nonsingular coordinate transformations via the Jacobian.

**Where:** SCH p.471 (pdf 489)

### Einstein summation convention

*convention · mention* · also: summation convention, implied sum over repeated indices

In the main text, an index appearing once up and once down in a term is summed over its range without writing a sigma.

**How introduced:** Not used in this appendix: every sum is written with an explicit sigma and its range, which makes the appendix a useful decoder for the compressed notation of the main text.

$$
V_i = \sum_j A_{ij}W_j \;\longleftrightarrow\; V^{\bar\alpha} = \Lambda^{\bar\alpha}{}_{\beta} V^{\beta}
$$

**Notes:** Introduced in SCH ch2 §2.1; the appendix's Latin lower indices do not follow the up/down pairing rule.

**Where:** SCH p.469 (pdf 487); SCH p.470 (pdf 488)

### metric tensor

*mathematical-object · mention* · also: metric, inner product of spacetime

The symmetric bilinear, nondegenerate and (in relativity) indefinite inner product on vectors, represented by a symmetric matrix of components g_ab in any basis.

**How introduced:** Only alluded to: the appendix's remark that relativity uses indefinite inner products is the linear-algebra shadow of the metric developed in the main text.

**Prerequisites:** inner product, indefinite inner product

$$
A\cdot B = g_{ij}A^i B^j
$$

**Notes:** The component formula is the standard one from SCH ch3, not written in the appendix. In the skew basis of p.469 the metric matrix is ((1,-1),(-1,2)).

**Where:** SCH p.469 (pdf 487)

## Key equations

### Vector addition axioms · supporting · SCH p.468 (pdf 486)

$$
A + B = B + A \in V,\qquad A + 0 = A
$$

Addition keeps you inside the set, is order-independent and has a zero; together with the unwritten associativity and inverses this makes V an abelian group.

**Symbols:** A, B vectors; V the space; 0 the zero vector

### Scalar multiplication axioms · supporting · SCH p.468 (pdf 486)

$$
a(A+B) = a(A) + a(B),\quad (a+b)(A) = a(A) + b(A),\quad (ab)(A) = a(b(A)),\quad 1(A) = A
$$

Real scaling distributes over vector sums and scalar sums, composes with ordinary multiplication and does nothing when the factor is 1.

**Symbols:** a, b real numbers

### Linear independence test · central · SCH p.468 (pdf 486)

$$
aA + bB + \dots + fF = 0 \quad\text{has only the solution}\quad a = b = \dots = f = 0
$$

A set is independent when no nontrivial weighted sum of its members vanishes; the book states the contrapositive form.

**Symbols:** a ... f real coefficients; A ... F vectors

### Expansion in a basis · central · SCH p.468 (pdf 486)

$$
B = b_1A_1 + b_2A_2 + \dots + b_nA_n
$$

Any vector is a linear combination of basis vectors; the coefficients are its components on that basis.

**Symbols:** A_i basis vectors; b_i components of B; n dimension

### Inner product axioms · central · SCH p.468 (pdf 486)

$$
A\cdot B = B\cdot A,\qquad (aA+bB)\cdot C = a(A\cdot C) + b(B\cdot C)
$$

Symmetry plus linearity in the first slot, hence bilinearity; positivity is not assumed.

**Symbols:** A, B, C vectors; a, b reals

### Norm for a positive-definite inner product · supporting · SCH p.468 (pdf 486)

$$
A\cdot A > 0\ \ (A\neq 0)\;\Rightarrow\; |A| \equiv (A\cdot A)^{1/2}
$$

When every nonzero vector has positive self-product the length is its square root.

**Symbols:** |A| norm of A

### Magnitude for an indefinite inner product · central · SCH p.469 (pdf 487)

$$
|A| \equiv |A\cdot A|^{1/2}
$$

Relativity's convention: take the absolute value before the square root so the magnitude is real whatever the sign of A.A.

**Symbols:** |A| magnitude; A.A may be positive, negative or zero

### Orthogonality · supporting · SCH p.469 (pdf 487)

$$
A\cdot B = 0
$$

Definition of orthogonal vectors, independent of any picture of angles.

### Orthonormal basis condition · supporting · SCH p.469 (pdf 487)

$$
A_i\cdot A_j = 0\ \ (i\neq j),\qquad |A_k| = 1\ \ \forall k
$$

Basis vectors are pairwise orthogonal and of unit magnitude; equivalently A_i.A_j = delta_ij in the positive-definite case.

**Symbols:** A_i basis vectors

### Skew-basis practice problem data · derivation-step · SCH p.469 (pdf 487)

$$
A = 5e_x + e_y,\quad B = 3e_y,\quad e_1 = e_x,\quad e_2 = e_y - e_x
$$

The vectors and nonorthogonal basis the reader is asked to use; solving gives A = 6e_1 + e_2 and B = 3e_1 + 3e_2 (solution computed for this dossier, not printed).

**Symbols:** e_x, e_y Cartesian unit vectors; e_1, e_2 skew basis

### 2x2 matrix acting on a column vector · supporting · SCH p.469 (pdf 487)

$$
\begin{pmatrix}V_1\\ V_2\end{pmatrix} = \begin{pmatrix}A_{11} & A_{12}\\ A_{21} & A_{22}\end{pmatrix}\begin{pmatrix}W_1\\ W_2\end{pmatrix} = \begin{pmatrix}A_{11}W_1 + A_{12}W_2\\ A_{21}W_1 + A_{22}W_2\end{pmatrix}
$$

Each output entry is a row of the matrix paired with the input column.

**Symbols:** A_ij matrix entries (row i, column j); W input, V output column vectors

### Matrix-vector product in index form · central · SCH p.469 (pdf 487)

$$
V_i = \sum_{j=1}^{n} A_{ij} W_j
$$

General n-dimensional rule; the summed index is the second (column) index of A.

**Symbols:** i free row index; j summed index

### Matrix addition and scaling · supporting · SCH p.470 (pdf 488)

$$
\mathbf{A}+\mathbf{B} = \mathbf{C} \Rightarrow C_{ij} = A_{ij} + B_{ij},\qquad a\mathbf{A} = \mathbf{B} \Rightarrow B_{ij} = aA_{ij}
$$

Entrywise operations that make n x n matrices a vector space of dimension n^2.

### Natural inner product on matrices · supporting · SCH p.470 (pdf 488)

$$
\mathbf{A}\cdot\mathbf{B} = \sum_{i,j} A_{ij} B_{ij}
$$

Treat the n^2 entries as components and take the Euclidean dot product; it is positive-definite.

### 2x2 matrix product (corrected) · derivation-step · SCH p.470 (pdf 488)

$$
\mathbf{A}\mathbf{B} = \begin{pmatrix}A_{11}B_{11} + A_{12}B_{21} & A_{11}B_{12} + A_{12}B_{22}\\ A_{21}B_{11} + A_{22}B_{21} & A_{21}B_{12} + A_{22}B_{22}\end{pmatrix}
$$

Explicit product of two 2x2 matrices. The book prints A_12 B_22 in the (1,1) entry, a typo; the correct term is A_12 B_21, as the index formula that follows confirms.

**Symbols:** C_ij entries of AB

### Matrix product in index form · central · SCH p.470 (pdf 488)

$$
C_{ij} = \sum_{k=1}^{n} A_{ik} B_{kj}
$$

Row i of A contracted with column j of B; the summed index is second on A and first on B.

**Symbols:** i, j free; k summed

### Associativity, non-commutativity and identity · supporting · SCH p.470 (pdf 488)

$$
(\mathbf{A}\mathbf{B})\mathbf{C} = \mathbf{A}(\mathbf{B}\mathbf{C}),\quad \mathbf{A}\mathbf{B}\neq\mathbf{B}\mathbf{A}\ \text{(in general)},\quad (\mathbf{1})_{ij} = \delta_{ij}
$$

Properties of the matrix algebra stated in words in the book and collected here in symbols.

**Symbols:** delta_ij Kronecker delta

### 2x2 determinant · central · SCH p.470 (pdf 488)

$$
\det\begin{pmatrix}A_{11} & A_{12}\\ A_{21} & A_{22}\end{pmatrix} = A_{11}A_{22} - A_{12}A_{21}
$$

Base case of the recursive determinant.

### Example submatrix and minor · derivation-step · SCH p.471 (pdf 489)

$$
\mathbf{S}_{12} = \begin{pmatrix}B_{21} & B_{23}\\ B_{31} & B_{33}\end{pmatrix},\qquad D_{12} = B_{21}B_{33} - B_{23}B_{31}
$$

Deleting row 1 and column 2 of a 3x3 matrix leaves S_12, whose determinant is the minor D_12.

**Symbols:** S_lm submatrix without row l and column m; D_lm its determinant

### Cofactor expansion of the determinant · central · SCH p.471 (pdf 489)

$$
\det(\mathbf{B}) = \sum_{j=1}^{n} (-1)^{i+j} B_{ij} D_{ij}\qquad \text{for any fixed } i
$$

Recursive definition of the n x n determinant along an arbitrary row; the value is the same whichever row is used.

**Symbols:** i fixed row; j summed; D_ij minors

### Cofactor formula for the inverse · central · SCH p.471 (pdf 489)

$$
(\mathbf{B}^{-1})_{ij} = (-1)^{i+j} D_{ji}/\det(\mathbf{B})
$$

Inverse entries are transposed signed minors divided by the determinant.

**Symbols:** note D_ji, not D_ij

### Existence of the inverse · supporting · SCH p.471 (pdf 489)

$$
\mathbf{B}^{-1}\ \text{exists} \iff \det(\mathbf{B}) \neq 0
$$

A matrix can be inverted exactly when its determinant is nonzero.

## Figures

## Worked examples

### In-text practice problem: components in a skew basis · intro · SCH p.469 (pdf 487)

**Problem:** Starting from the plane vectors A = 5e_x + e_y and B = 3e_y, express each through the skew pair made of e_1 (identical to e_x) and e_2 (equal to e_y minus e_x), then compare the new first components with the Cartesian x components.

**Method:** Write A = a_1 e_1 + a_2 e_2 = (a_1 - a_2) e_x + a_2 e_y and match coefficients of e_x and e_y; repeat for B. The book poses the task but does not carry it out.

**Key insight:** Although e_1 is literally the same vector as e_x, the 1-component of A is 6 while its x-component is 5 (and for B, 3 versus 0), because tilting the second basis vector changes how much of e_1 is needed. Components belong to a whole basis, not to one basis vector.

**Result:** A = 6e_1 + e_2; B = 3e_1 + 3e_2 (computed for this dossier). Check: with g_11 = 1, g_12 = -1, g_22 = 2 in the skew basis, A.B = 18 - 21 + 6 = 3, matching 5*0 + 1*3 in Cartesian components.

**Concepts:** nonorthogonal basis, basis dependence of components, components of a vector, orthonormal basis

### 2x2 matrix times a column vector, then index form · intro · SCH p.469 (pdf 487)

**Problem:** Show how a general 2x2 matrix acts on a two-component column vector and compress the result into an index formula valid in n dimensions.

**Method:** Multiply out row by row, read off V_1 and V_2, recognise both as sums over the column index j, and extend the upper limit from 2 to n.

**Key insight:** The summed index is always the matrix's second index; the free index i on the left matches the row index.

**Result:** V_i = sum_{j=1}^{n} A_ij W_j

**Concepts:** matrix action on a column vector, matrix element indexing, column vector

### Product of two general 2x2 matrices · intro · SCH p.470 (pdf 488)

**Problem:** Multiply two general 2x2 matrices entry by entry and extract the general n x n index rule.

**Method:** Pair each row of A with each column of B, write the four resulting entries, then express entry (i,j) as a sum over the shared inner index k.

**Key insight:** Contraction happens between A's second index and B's first; this ordering is exactly why AB and BA usually differ. The printed (1,1) entry contains a typo (A_12 B_22 for A_12 B_21), which the index formula exposes.

**Result:** C_ij = sum_{k=1}^{n} A_ik B_kj; correct (1,1) entry A_11 B_11 + A_12 B_21.

**Concepts:** matrix multiplication, associativity and non-commutativity of matrix multiplication, matrix element indexing

### Building a 3x3 determinant from minors · standard · SCH p.470 (pdf 488)

**Problem:** For a general 3x3 matrix B, form the submatrix S_12 and its determinant D_12, then use such minors to define det B and larger determinants.

**Method:** Delete row 1 and column 2 to obtain a 2x2 block, take its determinant, and insert all minors of a chosen row into the alternating-sign sum; iterate for 4x4 and beyond.

**Key insight:** Determinants are defined recursively: each size is reduced to the next smaller one, and any row may be chosen for the expansion without changing the answer.

**Result:** S_12 = ((B_21, B_23), (B_31, B_33)), D_12 = B_21 B_33 - B_23 B_31, and det B = sum_j (-1)^(i+j) B_ij D_ij for any i.

**Concepts:** minor, cofactor, cofactor expansion, determinant


## Analogies and intuitions

### Matrices are vectors too: an n x n array can be read as a list of n^2 numbers that adds and scales exactly like an arrow's components. → vector space of matrices · useful · SCH p.470 (pdf 488)

Shown before matrix multiplication to reinforce that the vector-space axioms describe structure, not arrows, and that a natural dot product exists on matrices.

**Where it breaks down:** The matrix product has no counterpart among ordinary vectors, and viewing a matrix as a flat list hides its role as a linear map.

**App idea:** A 2x2 matrix card that flips between a 4-slot 'vector' view (add, scale, dot product) and a 'map' view deforming a unit grid, so learners see both personalities of the same object.

### A magnitude that forgets its sign: taking |A.A| before the square root is like reporting the size of a debt or a credit with the same positive number. → indefinite inner product · weak · SCH p.469 (pdf 487)

The book simply adopts the absolute-value convention for relativity; the intuition (framed here by the dossier) is that magnitude records size while the sign of A.A separately records the vector's type.

**Where it breaks down:** Null vectors have zero magnitude without being zero, which has no analogue in money; and discarding the sign loses the timelike/spacelike distinction unless it is tracked separately.

**App idea:** Drag a vector in a plane with switchable signature (+,+) or (-,+); a meter shows A.A with sign colour and |A| beside it, turning grey on the light-cone lines where both vanish.

### Components as recipe amounts: how much of ingredient e_1 you need depends on what the other ingredient e_2 already contributes. → basis dependence of components · useful · SCH p.469 (pdf 487)

Dossier framing of the p.469 problem: because e_2 = e_y - e_x carries a negative dose of e_x, more e_1 is needed to rebuild A, so its 1-component (6) exceeds its x-component (5).

**Where it breaks down:** Recipe amounts are usually non-negative and ingredients do not overlap; basis vectors can overlap and components can be negative.

**App idea:** Parallelogram builder: learner drags the tip of e_2 while e_1 stays fixed and watches the parallelogram that constructs A reshape and the e_1 coefficient change.

### Russian-doll determinants: every determinant contains smaller determinants nested inside it, down to 2x2. → cofactor expansion · useful · SCH p.471 (pdf 489)

Captures the book's statement that 3x3 is defined through 2x2, 4x4 through 3x3, and so on.

**Where it breaks down:** Suggests a single nesting chain, whereas each level branches into n sub-determinants (n! terms overall), so the method becomes slow for large matrices.

**App idea:** Expandable tree: click a 4x4 determinant to split it into four signed 3x3 children, each of which splits into 2x2 leaves, with the numerical result bubbling back up the tree.


## Misconceptions addressed

### If one basis vector is unchanged, the component of a vector along it stays the same. · SCH p.469 (pdf 487)

**Correction:** Components are determined by the entire basis; replacing e_y by e_y - e_x changes the e_1 component of A from 5 to 6 even though e_1 = e_x.

**Why tempting:** In orthonormal bases a component equals the dot product with one basis vector, which seems to involve only that vector.

### A basis has to be orthonormal to be legitimate. · SCH p.469 (pdf 487)

**Correction:** Any linearly independent set with as many vectors as the dimension is a basis; orthonormality is merely convenient.

**Why tempting:** Introductory physics almost always uses i, j, k, so skew bases feel wrong.

### A.A is always positive, and A.A = 0 forces A = 0. · SCH p.469 (pdf 487)

**Correction:** Only positive-definite products guarantee a positive A.A. The appendix states that relativity's inner products are indefinite, so A.A takes both signs; the further fact that a nonzero vector can have A.A = 0 (null vectors) is not in the appendix and must be supplied from Ch. 2.

**Why tempting:** Every dot product met before relativity is Euclidean.

### Matrix multiplication commutes like ordinary multiplication. · SCH p.470 (pdf 488)

**Correction:** The matrix product is associative but in general AB is not BA; the order of index contraction matters.

**Why tempting:** Numbers commute, and the product of two diagonal or two same-direction boost matrices happens to commute.

### In V_i = sum A_ij W_j (or in C = AB) it does not matter which index of the matrix is summed. · SCH p.469 (pdf 487)

**Correction:** In V = A W the sum runs over the column (second) index of A; in C = AB it pairs A's column index with B's row index. Contracting the wrong slot silently computes A^T W or a different product.

**Why tempting:** The index expressions look symmetric on paper, especially for symmetric matrices where the error goes unnoticed.

### The determinant obtained by expanding along a different row will generally be different. · SCH p.471 (pdf 489)

**Correction:** Cofactor expansion along any row (or column) gives the same value.

**Why tempting:** The individual terms change completely from row to row.

### The inverse's (i,j) entry uses the minor of the (i,j) entry. · SCH p.471 (pdf 489)

**Correction:** It uses D_ji: the cofactor matrix must be transposed before dividing by the determinant.

**Why tempting:** Index order is easy to copy wrongly, and for symmetric matrices like the metric the transposition makes no difference, so the mistake is rarely caught.

*Inferred: the book guards against this implicitly.*

### The component of a vector along a basis vector is always its inner product with that basis vector. · SCH p.469 (pdf 487)

**Correction:** That holds only for orthonormal bases. In the skew basis, A.e_1 = 5 and A.e_2 = -4, while the components are 6 and 1; the dot products are the lowered (one-form) components.

**Why tempting:** Projection by dot product is the standard recipe learned with Cartesian axes.

*Inferred: the book guards against this implicitly.*

### Orthogonal vectors must look perpendicular. · SCH p.469 (pdf 487)

**Correction:** Orthogonality is defined purely by a vanishing inner product; under an indefinite product, orthogonal vectors can look mirror-symmetric about a light-cone line, and a null vector is orthogonal to itself.

**Why tempting:** In Euclidean geometry orthogonal and perpendicular are synonyms.

*Inferred: the book guards against this implicitly.*


## Thought experiments

_None recorded._

## Applications and observations

_None recorded._

## Historical notes

_None recorded._

## Notation and conventions

- **Vectors in the appendix:** Plain italic capitals A, B, ... denote abstract vectors; there are no arrows over them and no tildes for one-forms. — The main text uses arrows for vectors and tildes for one-forms (SCH ch2-ch3); learners moving between the two need to translate. (SCH p.468 (pdf 486))
- **Component index position:** Components carry lower Latin indices (b_1, ..., b_n; W_i; A_ij) running from 1 to n. — The main text writes vector components with upper Greek indices 0-3 and one-form components with lower indices; the appendix makes no up/down distinction. (SCH p.468 (pdf 486))
- **Explicit summation:** Every sum is written with a sigma and its limits; the Einstein summation convention is not used. — Useful for decoding the implicit sums of the main text. (SCH p.469 (pdf 487))
- **Matrix symbols and entries:** Bold capitals A, B denote matrices; A_ij is the entry in row i, column j. (SCH p.469 (pdf 487))
- **Overloaded dot:** The centred dot is used for the inner product of vectors (A.B), for a matrix acting on a column vector (V = A.W), and for the inner product of matrices (A.B = sum A_ij B_ij). — Context decides the meaning; a potential source of confusion. (SCH p.470 (pdf 488))
- **Magnitude with an indefinite inner product:** |A| is defined as the square root of the absolute value of A.A. — The sign of A.A must be tracked separately to know a vector's causal type. (SCH p.469 (pdf 487))
- **Submatrix and minor symbols:** S_lm is the matrix with row l and column m removed; D_lm is its determinant; the cofactor sign is (-1)^(i+j). — The words 'minor' and 'cofactor' are not used in the appendix. (SCH p.470 (pdf 488))
- **Kronecker delta:** delta_ij equals 1 for equal indices and 0 otherwise, with both indices down. — Main text writes delta^alpha_beta once index positions matter. (SCH p.470 (pdf 488))
- **Dimension of a matrix:** The number of rows (equal to columns) of a square matrix. — Distinct from the dimension n^2 of the space of such matrices mentioned one page later. (SCH p.469 (pdf 487))

## Margin notes

- *clarification* — Aside that the vector-space definition extends to complex or arbitrary number fields, which the book never needs. (SCH p.468 (pdf 486))
- *technical-detail* — Parenthetical defining an algebra as a vector space with a multiplication, identifying square matrices as the example under study. (SCH p.470 (pdf 488))
- *clarification* — Opening remark that the appendix is a convenience recap and the reader is expected to know it already. (SCH p.468 (pdf 486))

## Exercises

About 1 exercises (pdf pages 487).

**Solutions:** No solution is printed; the dossier's worked example gives A = 6e_1 + e_2 and B = 3e_1 + 3e_2.

**Skills practiced**
- expanding vectors in a nonorthogonal basis by matching coefficients
- recognising that components depend on the whole basis

- **unnumbered in-text problem (p.469)** (intro): Rewrite two given Cartesian vectors of the plane in a skew basis whose first vector coincides with the x unit vector, and compare the first components with the x components. — *The appendix's only exercise; in two lines it plants the idea, essential for curvilinear and coordinate bases later, that a component is not a property of one basis vector alone.* Skills: change of basis, solving small linear systems, basis dependence of components

## Cross-references

- *backward* → **SCH front (Preface)**: The preface announces an appendix summarising the linear algebra needed in the text.
- *backward* → **SCH ch2 §2.1**: Lorentz transformations are introduced as a 16-entry matrix acting on components with the summation convention, the indexed version of V_i = sum_j A_ij W_j.
- *backward* → **SCH ch2 §2.2**: The inverse Lorentz transformation is identified as the matrix inverse of the forward one, and basis vectors are expanded with components exactly as in the appendix's basis expansion.
- *backward* → **SCH ch2 Exercise 2.13**: Parts (b) and (f): composing a boost along x with a boost along the new y axis is a matrix product, and multiplying in the other order gives a different matrix, a physical instance of non-commuting multiplication.
- *backward* → **SCH ch2 §2.5**: The scalar product of four-vectors is the indefinite inner product whose magnitude convention the appendix records; null vectors and orthogonality in spacetime are treated there.
- *backward* → **SCH ch3 §3.3**: One-forms and dual bases resolve the skew-basis puzzle: inner products with basis vectors give the lowered components, not the expansion coefficients.
- *backward* → **SCH ch3 §3.5**: The metric is recast as a symmetric (0 2) tensor, i.e. the symmetric bilinear inner product of the appendix promoted to a geometric object.
- *backward* → **SCH ch3 §3.6**: Raising an index is framed as applying the inverse of the matrix (eta_ab), conditional on that inverse existing (Eq. 3.43; Exercise 3.19 checks it by multiplication). The appendix's criterion det != 0 settles existence, since det(eta) = -1 (this determinant value is the dossier's remark, not the book's).
- *backward* → **SCH ch3 Exercise 3.33**: Part (b) asks for a proof that every Lorentz matrix has determinant +1 or -1 and part (c) that the +1 ones form a subgroup; this needs det(AB) = det A det B and det(A^T) = det A, which the appendix does not list.
- *backward* → **SCH ch5 §5.2**: A coordinate transformation is nonsingular where its Jacobian determinant is nonzero.
- *backward* → **SCH ch5 §5.5**: The polar coordinate basis vectors are not unit vectors, and orthonormal noncoordinate bases are constructed, applying the orthonormal-versus-general basis distinction.
- *backward* → **SCH ch6 §6.2**: Eqs. 6.11-6.13 write the metric transformation as (g) = (Lambda)(eta)(Lambda)^T and take determinants, using det(AB) = det A det B and det(Lambda) = det(Lambda^T), to obtain the Jacobian and the proper volume element sqrt(-g); neither determinant property is listed in the appendix.
- *backward* → **SCH ch6 §6.3**: Eq. 6.39 gives the derivative of the metric determinant in terms of the inverse metric, a result that rests on the cofactor form of the inverse (worked out in Exercise 6.7).
- *backward* → **SCH ch6 Exercise 6.7**: Asks for the cofactor definition of the determinant and to differentiate a 2x2 determinant, directly exercising the appendix's final page.
- *backward* → **SCH ch11 §11.3**: Eq. 11.87 inverts the symmetric t-phi block of the Kerr metric as a 2x2 matrix divided by its determinant D, an instance of the cofactor inverse formula.
- *backward* → **SCH ch12 §12.3**: Determinants of detector response matrices appear in the analysis of joint detection by two detectors.

## Teaching gems

### The skew-basis problem in which e_1 coincides with e_x yet the 1 and x components of the same vector disagree. · SCH p.469 (pdf 487)

**Why it works:** The surprise is built into the setup: learners expect identical basis vectors to give identical components, and the mismatch forces them to see components as a property of the whole basis, preparing them for coordinate bases, one-forms and index lowering.

**App idea:** Interactive 2D skew-basis lab: e_1 is pinned to e_x while the learner drags e_2; A is drawn as the diagonal of a parallelogram whose sides along e_1 and e_2 update live, with a side panel listing the expansion components alongside the dot products A.e_1 and A.e_2 so the two kinds of component visibly separate once e_2 tilts away from perpendicular.

### Defining the inner product by symmetry and bilinearity alone, with positivity as an optional add-on and the absolute-value magnitude for relativity. · SCH p.469 (pdf 487)

**Why it works:** It makes the Minkowski product a legitimate inner product rather than a broken dot product, so later sign surprises (negative A.A, null vectors) read as features of a known structure.

**App idea:** Signature morph: a slider continuously changes the metric diag(s, 1) from s = +1 to s = -1; the set of unit-magnitude vectors deforms from a circle through parallel lines to a pair of hyperbolas, and a draggable vector shows A.A with its sign and |A|.

### Explicit 2x2 display, then indexed sum to 2, then indexed sum to n, with a pointed note on which index is summed. · SCH p.470 (pdf 488)

**Why it works:** Learners see the index formula emerge from multiplication they can already do by hand, and the 'which index' remark builds the contraction discipline tensor algebra needs.

**App idea:** Animated product explorer: hovering entry C_ij lights row i of A and column j of B, slides them together and fills the sum with the k-values ticking; a toggle swaps A and B to show a different C, and a 'spot the typo' mode displays the book's (1,1) entry for learners to correct.

### Showing that matrices themselves satisfy the vector-space axioms (dimension n^2) before introducing their product. · SCH p.470 (pdf 488)

**Why it works:** The abstraction becomes concrete: vectors are anything obeying the rules, which is exactly how tensors are introduced later as elements of vector spaces.

**App idea:** Two-view card for a 2x2 matrix: 'as a vector' shows four sliders and lets learners add or scale matrices; 'as a map' shows the image of the unit square; changing sliders updates both.

### Recursive determinant with freedom to expand along any row. · SCH p.471 (pdf 489)

**Why it works:** One recursive rule handles every size, including 4x4 metric and Lorentz matrices. The book does not exploit the freedom of row choice, but a tutor can: its own sample 3x3 matrix has a bottom row (10^5, 0, 0), so expanding there needs a single 2x2 minor.

**App idea:** Expansion playground: pick any row of a 3x3 or 4x4 matrix, see the checkerboard signs and minors appear, and watch every choice converge to the same number; add an optional panel (not in the book) showing the determinant as the signed area or volume of the transformed unit cell.

### Ending with the inverse and the criterion det != 0. · SCH p.471 (pdf 489)

**Why it works:** It is the exact fact the main text uses to guarantee index raising (inverse metric) and good coordinates (nonzero Jacobian), so learners can trace later existence claims back here.

**App idea:** Singularity slider: drag the two columns of a 2x2 matrix toward being parallel; the transformed unit square flattens, det tends to zero, and the inverse's entries grow without bound, with a caption linking to 'why the metric must be invertible'.


## Gaps and pitfalls

- **Printed typo in the explicit 2x2 product: the (1,1) entry reads A_11 B_11 + A_12 B_22 instead of A_11 B_11 + A_12 B_21 (confirmed on the page render).** — A reader checking by hand may doubt their understanding of the row-times-column rule or copy the wrong formula. *Suggestion:* Flag the correction explicitly and have learners verify every entry against C_ij = sum_k A_ik B_kj.
- **The inner product is defined without nondegeneracy, and uniqueness of basis components is not stated.** — Learners cannot see why an indefinite metric still has an inverse or why components are well defined. *Suggestion:* Add nondegeneracy (only the zero vector is orthogonal to every vector) and note that independence of the basis makes the expansion unique.
- **The absolute-value magnitude for indefinite products discards the sign and says nothing about null vectors or self-orthogonality.** — Learners may conclude that |A| = 0 means A = 0, or lose track of timelike versus spacelike. *Suggestion:* Always report the sign of A.A alongside |A| and give a null-vector example such as (1, 1) under diag(-1, 1).
- **The orthonormality condition |A_k| = 1 hides that under an indefinite product basis vectors satisfy A_i.A_j = +-delta_ij.** — Confusion when meeting eta_ij = diag(-1, 1, 1, 1) as the 'orthonormal' metric. *Suggestion:* State orthonormality as A_i.A_j = eta_ij in the spacetime case.
- **Index notation differs from the main text: lower Latin indices for vector components, explicit sums, no up/down distinction, and the dot used for three different operations.** — Readers who consult the appendix mid-chapter may mis-map A_ij onto Lambda^alpha-bar_beta or g_ab and lose track of which index is contracted. *Suggestion:* Provide a translation table: V_i = sum_j A_ij W_j corresponds to V^alpha-bar = Lambda^alpha-bar_beta V^beta, with row = upper index, column = lower index.
- **The skew-basis problem has no printed answer, and the appendix never explains what the dot products with basis vectors are when the basis is skew.** — The key payoff, the distinction between expansion components and dot-product (lowered) components, is left implicit. *Suggestion:* Give the answer (A = 6e_1 + e_2, B = 3e_1 + 3e_2), compute A.e_1 = 5 and A.e_2 = -4, and connect those numbers to one-form components and the metric g_ij = ((1,-1),(-1,2)).
- **Determinant properties the book later needs are missing: det(AB) = det A det B, det(A^T) = det A, the geometric volume meaning, and the derivative of a determinant via the inverse.** — Chapter 6's volume element and determinant derivative, and Chapter 3's Lorentz-determinant exercise, cannot be justified from the appendix alone. *Suggestion:* Supplement with the product rule, transpose invariance, the volume-scaling picture, and delta(det g) = det g * g^{ab} delta g_ab.
- **Transpose, trace, eigenvalues and diagonalisation are not covered.** — Readers meet transposes in the metric transformation law (Ch. 6) and eigenvalue ideas for signature and stress tensors without a reference. *Suggestion:* Add a short supplement: transpose, trace, symmetric matrices have real eigenvalues, and signature counts the signs of the metric's eigenvalues.
- **Group-theory language ('abelian group') replaces the explicit additive axioms, and row independence of the cofactor expansion and positivity of the matrix inner product are asserted without argument.** — Novices may not realise additive inverses and associativity are required, and must take key facts on trust. *Suggestion:* Spell out all additive axioms and offer a quick 3x3 numerical check of row independence.
- **The word 'dimension' is used both for the row count of a matrix and for the dimension n^2 of the space of matrices.** — Readers may think a 4x4 matrix lives in a 4-dimensional space. *Suggestion:* Say 'size' or 'order' for the row count and reserve 'dimension' for vector spaces.
- **The inverse formula's transposed minor D_ji is easy to miss, and for symmetric matrices the error is invisible.** — Wrong inverses for non-symmetric matrices such as general Jacobians. *Suggestion:* Test the formula on a non-symmetric 2x2, e.g. ((1,2),(3,1)), and verify B B^{-1} = 1.

## Tutor notes

- Treat this unit as a just-in-time reference: open it when a learner stalls on matrix products (Ch. 2 boosts), the inverse metric (Ch. 3), Jacobians (Ch. 5) or metric determinants (Ch. 6), rather than teaching it front to back.
- Diagnostic opening questions: 'Is the set of all 2x2 matrices a vector space, and what is its dimension?', 'Can A.A be zero for a nonzero vector?', 'If e_1 is the same as e_x, must the 1-component equal the x-component?'
- Suggested order for a learner with gaps: axioms and basis expansion, then the skew-basis problem, then inner products (Euclidean first, then indefinite), then matrix-vector and matrix-matrix products with index forms, then determinants and inverses tied to the metric.
- Use the skew-basis problem actively: have the learner predict A's e_1 component before solving. Answer: A = 6e_1 + e_2, B = 3e_1 + 3e_2. Follow up by computing A.e_1 = 5 and A.e_2 = -4 and asking why they differ from 6 and 1; this is the seed of lowered indices.
- Consistency check worth doing aloud: in the skew basis the metric matrix is g = ((1,-1),(-1,2)); A.B computed as g_ij A^i B^j with A = (6,1), B = (3,3) gives 18 - 21 + 6 = 3, the same as the Cartesian 5*0 + 1*3.
- When presenting the 2x2 product, point out the book's typo in the (1,1) entry (A_12 B_22 should be A_12 B_21) before the learner finds it, and use it as a prompt to re-derive the entry from C_ij = sum_k A_ik B_kj.
- Practice numbers (computed for tutoring, not printed): the sample 3x3 matrix ((1,2,5),(-6,3,18),(10^5,0,0)) has determinant 2.1 x 10^6; expanding along row 3 takes one term (10^5 x (2*18 - 5*3)), expanding along row 1 takes three, and both agree. The sample 2x2 ((1,2),(3,1)) has determinant -5 and inverse (-1/5)((1,-2),(-3,1)).
- Check for understanding on non-commutativity with physics: ask for the product of a boost along x and a rotation about z in both orders, or point to SCH ch2 Exercise 2.13.
- Common learner question: 'Why does relativity define magnitude with an absolute value?' Answer that the sign of A.A is kept separately to classify vectors as timelike, spacelike or null, while |A| gives proper time or proper length.
- Common learner question: 'Why does the inverse need det != 0?' Connect to geometry: a zero determinant squashes the unit square or cube flat, so the map loses information and cannot be undone; for the metric this would mean no way to turn one-forms back into vectors.
- Translate notation explicitly when the learner comes from the main text: appendix A_ij (row i, column j) corresponds to Lambda^alpha-bar_beta with the upper index as row; appendix sums with sigma correspond to repeated up/down indices.
- For advanced learners, add what the appendix omits: det(AB) = det A det B (needed for det g transforming with the square of the Jacobian), det(A^T) = det A, and the derivative of a determinant via the inverse matrix (used in SCH ch6 §6.3).

## Verification

**Verdict:** fixed

**Fixes applied**
- Misconception on positive A.A: clarified that the appendix only states indefiniteness; null vectors (A.A = 0, A != 0) are not in the appendix though the entry was marked explicit.
- Teaching gem on recursive determinants: removed the implication that the book exploits row choice with its 10^5 sample matrix; reframed as a tutor suggestion.
- Cross-reference 'SCH ch3 Exercises' made specific (Exercise 3.33 (b),(c)) and checked against ch03 source.
- Cross-reference SCH ch3 §3.6: the book conditions index raising on the inverse existing (Eq. 3.43, Exercise 3.19); det(eta) = -1 marked as dossier commentary.
- Cross-reference SCH ch2 Exercise 2.13 sharpened to parts (b) and (f), which the source confirms show order-dependent boost products.
- Field-of-scalars note corrected: the Ch. 3 spinor aside is about an antisymmetric metric in spinor space, not about complex scalars.
- Inner-product how_introduced made accurate to what the book says about symmetry (1) and bilinearity (2).
- Reworded basis definition and index-summation misconception correction to move further from source phrasing.

**Residual concerns**
- The appendix has no numbered sections, figures, footnotes or formal examples; section locators are null by design and sections are the dossier's thematic split of the italic run-in headings.
- The skew-basis solution, the 3x3 determinant value 2.1e6, the 2x2 inverse and the skew-basis metric are dossier computations, labelled as such; all were re-checked by hand.
- Only remaining 7-word overlaps with the source are equation transcriptions (allowed).

**Coverage:** toc_sections: 0, sections: 8, inventory_figures: 0, figures: 0, inventory_examples: 0, worked_examples: 4, concepts: 36, key_equations: 22, locators_checked: 40, locators_wrong: 0, pages_rendered: 4
