# Symmetries and identities of the Riemann tensor

`curvature/symmetries-and-identities` · main track · working depth · physics-reviewed · revision 4 · 2026-09-16

Teaches: `symmetries-of-the-riemann-tensor`, `cyclic-identity`, `number-of-independent-riemann-components`, `flatness-criterion`, `integrability-condition-for-parallel-fields`, `curvature-sign-conventions`

Builds on: `holonomy-and-the-riemann-tensor`, `curves-and-surfaces-in-space`, `curved-surfaces`, `the-levi-civita-connection`, `the-covariant-derivative`, `symmetry-levi-civita-and-the-metric`, `tensors-as-machines`, `local-flatness`, `accelerated-observers`, `the-interval-and-causality`, `the-metric`, `vector-calculus`

**With its first index lowered, the Riemann tensor changes sign when either index pair is swapped, keeps its value when the two pairs trade places, and sums to zero over the cyclic orders of its last three slots. Those rules leave one independent number on a surface, six in space and twenty in spacetime. The tensor vanishes on a region exactly when the region is flat, and another author's table of Riemann components must be calibrated on a ball before its signs are trusted.**

Take a sphere of radius $a$ with the coordinates $\theta$ from the pole and $\phi$ around it, as in *The metric*, and work out every component of its Riemann tensor from the Christoffel formula of *Holonomy and the Riemann tensor*. There are $2^4 = 16$ components. Twelve are zero. The other four are $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$, $R^\theta{}_{\phi\phi\theta} = -\sin^2\theta$, $R^\phi{}_{\theta\theta\phi} = -1$ and $R^\phi{}_{\theta\phi\theta} = 1$. Lower the first index with the metric and all four become $\pm a^2\sin^2\theta$: one number in four disguises. In spacetime the same tensor has $4^4 = 256$ components at every event. This section asks how many of those are disguises of one another, what it means when every one of them is zero, and how to read another author's table of components whose signs differ from ours.

## Three rules for the lowered tensor

The disguises come off when the first index is lowered, $R_{\rho\sigma\mu\nu} = g_{\rho\lambda}R^\lambda{}_{\sigma\mu\nu}$. Pick any event $P$ and use coordinates in which the metric's first derivatives vanish there, as *Local flatness* allows. Every Christoffel symbol is then zero at $P$, so the Christoffel formula keeps only its two derivative terms, $R^\rho{}_{\sigma\mu\nu} = \partial_\mu\Gamma^\rho{}_{\nu\sigma} - \partial_\nu\Gamma^\rho{}_{\mu\sigma}$. Lowering $\rho$ moves $g_{\rho\lambda}$ through the derivatives, because its own derivatives vanish at $P$, and $g_{\rho\lambda}\Gamma^\lambda{}_{\nu\sigma} = \tfrac12(\partial_\nu g_{\rho\sigma} + \partial_\sigma g_{\rho\nu} - \partial_\rho g_{\nu\sigma})$. Of the six second derivatives that appear, the two $\partial_\mu\partial_\nu g_{\rho\sigma}$ terms, one from each half, cancel, and what remains is

$$R_{\rho\sigma\mu\nu} = \tfrac12\big(\partial_\mu\partial_\sigma g_{\rho\nu} + \partial_\nu\partial_\rho g_{\sigma\mu} - \partial_\mu\partial_\rho g_{\sigma\nu} - \partial_\nu\partial_\sigma g_{\rho\mu}\big)\quad\text{at } P.$$

Now read the symmetries off this sum. Swap $\rho$ with $\sigma$: the first term becomes minus the third and the second becomes minus the fourth, so the sum changes sign. Swap $\mu$ with $\nu$: the first term becomes minus the fourth and the second becomes minus the third, with the same result. Trade the pair $\rho\sigma$ for the pair $\mu\nu$: because $g_{\rho\nu} = g_{\nu\rho}$ and partial derivatives commute, the first two terms trade places and the last two land on themselves, so the sum is unchanged. So at $P$, in these coordinates,

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}.$$

Each rule says that a certain tensor, such as $R_{\rho\sigma\mu\nu} + R_{\sigma\rho\mu\nu}$, has every component zero in one basis, and a tensor with every component zero in one basis has every component zero in all of them, as *Tensors as machines* showed. Since $P$ was any event, the three rules hold at every event, in every coordinate system and every basis. Call them antisymmetry in the first pair, antisymmetry in the last pair, and pair exchange. The last-pair rule needs no lowering at all: the Christoffel formula for $R^\rho{}_{\sigma\mu\nu}$ turns into its own negative under $\mu \leftrightarrow \nu$, so the mixed tensor obeys it too, whatever the connection. The first-pair rule is different: it holds only with both indices of the pair at the same level, because raising one of them brings a metric factor that the other does not carry.

*With its first index lowered by the metric, the Riemann tensor changes sign when either index pair is swapped and keeps its value when the two pairs trade places, at every event and in every basis.*

## A fourth rule: the cyclic identity

One more relation hides among the components. Keep the first index up and move the other three one place around a ring, $\sigma \to \mu \to \nu \to \sigma$. The three components so related add to zero:

$$R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0.$$

This is the cyclic identity, also called the first Bianchi identity. To prove it, add the three cyclic copies of the Christoffel formula. The six derivative terms group into $\partial_\mu(\Gamma^\rho{}_{\nu\sigma} - \Gamma^\rho{}_{\sigma\nu})$ and two more brackets like it with $\partial_\nu$ and $\partial_\sigma$ in front, and the six products group into $\Gamma^\rho{}_{\mu\lambda}(\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\lambda{}_{\sigma\nu})$ and two more like it. Every bracket is a Christoffel symbol minus the same symbol with its lower indices swapped, which vanishes for the torsion-free connections of *The Levi-Civita connection*. So the identity uses $\Gamma^\lambda{}_{\mu\nu} = \Gamma^\lambda{}_{\nu\mu}$ and nothing else, and needs no metric.

When does the identity say something new? If two of $\sigma$, $\mu$, $\nu$ are equal, antisymmetry in the last pair makes the sum vanish on its own: with $\mu = \nu$ the first term is zero and the other two are opposites. Now lower $\rho$ and let it equal one of the other three, say $\rho = \sigma = 1$, $\mu = 2$, $\nu = 3$. Then $R_{1123} = 0$, and $R_{1312} = R_{1213} = -R_{1231}$ by pair exchange and last-pair antisymmetry, so the sum is $0 + R_{1231} - R_{1231}$: zero already. A new condition therefore needs four different indices, which a surface and three-dimensional space cannot supply. Spacetime has exactly one set of four, and the one new condition is

$$R_{0123} + R_{0231} + R_{0312} = 0,$$

which links three different components, so that any two of them fix the third.

*Summed over the three cyclic orders of its last three indices, the Riemann tensor gives zero; the rule needs only a torsion-free connection, and it adds a new relation only among components with four different indices.*

## Counting the survivors

The rules turn a count of components into a count of index pairs. Antisymmetry kills every component with a repeated index inside a pair and fixes the rest by their unordered pairs, so in $n$ dimensions each pair is one of $N = n(n-1)/2$ choices, and the tensor becomes an $N \times N$ array $R_{AB}$, with $A$ standing for the first pair and $B$ for the last. Pair exchange makes the array symmetric, like a times table, which leaves $N(N+1)/2$ entries: the $N$ on the diagonal and half of the rest. The cyclic identity then removes one number for each set of four different indices, $\binom{n}{4}$ in all, because a set gives the same relation whichever of its four indices is placed in the first slot, and different sets involve different entries. Altogether the number of independent components is

$$N_R(n) = \frac{N(N+1)}{2} - \binom{n}{4} = \frac{n^2(n^2-1)}{12},$$

which is $0$, $1$, $6$, $20$ and $50$ for $n = 1$ to $5$. A surface keeps one number. Space keeps six. Spacetime keeps twenty: the $21$ entries of a symmetric $6 \times 6$ array, less the one cyclic relation. These twenty are exactly the second derivatives of the metric that Riemann normal coordinates cannot remove, as *Holonomy and the Riemann tensor* found: what a freely falling frame cannot hide.

On a surface the one survivor is the Gaussian curvature $K$ of *Curves and surfaces in space*. *Holonomy and the Riemann tensor* found that a small loop with its region on the walker's left turns a carried vector toward the left by $K$ times the enclosed area, and its small-loop law gives that same turn as $-R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$. In an orthonormal basis with $e_1$ along the first edge and $e_2$ to its left, take $V = e_1$, a first edge of length $\ell_1$ along $e_1$ and a second of length $\ell_2$ along $e_2$. The turn moves $e_1$ toward $e_2$ by $K\ell_1\ell_2$, so $\Delta V^{\hat 2} = K\ell_1\ell_2$. The law gives $\Delta V^{\hat 2} = -R^{\hat2}{}_{\hat1\hat1\hat2}\,\ell_1\ell_2 = R_{\hat1\hat2\hat1\hat2}\,\ell_1\ell_2$, by antisymmetry in the first pair. Matching the two gives $R_{\hat1\hat2\hat1\hat2} = K$. Under a change of surface coordinates $R_{1212}$ and $\det g$ pick up the same factor, the squared Jacobian determinant, because each is antisymmetric in two pairs of indices and in two dimensions each antisymmetric pair transforms by the Jacobian determinant. So in any coordinates

$$R_{1212} = K\det g,\qquad R_{\rho\sigma\mu\nu} = K\big(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}\big).$$

The second form follows from the first: the four rules leave one number on a surface, the tensor $g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu}$ obeys all four, and its $1212$ component is $\det g$, so the whole tensor is $K$ times it. On the sphere of the opening, $R_{\theta\phi\theta\phi} = a^2\sin^2\theta$ and $\det g = a^4\sin^2\theta$, so $K = 1/a^2$, the number the ring test reads.

*The pair rules make the Riemann tensor a symmetric array over index pairs and the cyclic identity removes one entry per set of four different indices: one number on a surface, six in space and twenty in spacetime, the second metric derivatives that no coordinates can remove.*

## When can a vector field be parallel everywhere?

A table of zeros ought to mean flat, and the tool that proves it is a vector field whose carried copies match it everywhere. Picture an arrow painted at every point of a region and a cardboard copy of one of them carried along any path by parallel transport. The painting is a parallel field if the copy always lands on the arrow painted where it stops. In components, $V$ is parallel along every curve, so

$$\nabla_\nu V^\rho = \partial_\nu V^\rho + \Gamma^\rho{}_{\nu\sigma}V^\sigma = 0.$$

These are $n^2$ equations for $n$ unknown functions, so they cannot always be solved. They fix every first derivative, $\partial_\nu V^\rho = -\Gamma^\rho{}_{\nu\sigma}V^\sigma$, and the second derivatives they imply must agree: $\partial_\mu\partial_\nu V^\rho$ must equal $\partial_\nu\partial_\mu V^\rho$. Rather than differentiate the Christoffel symbols by hand, use the covariant form of the same mismatch, the Ricci identity of *Holonomy and the Riemann tensor*, $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$. For a parallel field its left side is zero, because every $\nabla_\nu V^\rho$ is zero and so is the covariant derivative of zero, in either order. So a parallel field must satisfy the integrability condition

$$R^\rho{}_{\sigma\mu\nu}V^\sigma = 0.$$

Read it at one event as linear algebra: for every choice of the loop pair $\mu\nu$, the matrix $R^\rho{}_{\sigma\mu\nu}$ must send $V$ to zero. Two consequences follow.

- A parallel frame, meaning $n$ independent parallel fields, needs every such matrix to vanish, so it needs $R^\rho{}_{\sigma\mu\nu} = 0$ throughout the region.
- On a surface even one parallel field forces the curvature to vanish. With $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$ the condition reads $K(\delta^\rho{}_\mu V_\nu - \delta^\rho{}_\nu V_\mu) = 0$. Taking $\rho = \mu = 1$ and $\nu = 2$ gives $KV_2 = 0$; taking $\rho = \nu = 2$ and $\mu = 1$ gives $KV_1 = 0$. Parallel transport along any curve is invertible, because carrying the copy back along the same curve undoes it, so a parallel field that is nonzero at one point is nonzero on the whole connected region, and then $K = 0$ throughout it. A sphere carries no parallel field on any patch, however small. On Earth, ignoring hills, a loop around one square kilometre still turns a carried copy by $A/R_\oplus^2 = 2.5\times10^{-8}$ radians, about $1.4$ millionths of a degree, and no patch is small enough to make such turns zero.

The condition is necessary. The converse, from zero curvature back to parallel fields, needs the region to be simply connected, meaning that every loop in it can be shrunk to a point without leaving the region. A paper cone with its tip removed is not simply connected: a loop around the missing tip turns a carried vector by the angle of the wedge that was cut from the flat sheet to make the cone, although $R^\rho{}_{\sigma\mu\nu} = 0$ at every point of the cone away from the tip. If $R^\rho{}_{\sigma\mu\nu} = 0$ on a simply connected region, a parallel field passes through every vector at any point of it. That converse is taken on trust here; *Zero curvature means flat* uses it.

*A vector field that is parallel everywhere must be sent to zero by the Riemann tensor on every loop plane; a full parallel frame needs zero curvature, a surface needs zero Gaussian curvature even for one field, and zero curvature on a simply connected region gives such fields back.*

## Zero curvature means flat

Call a metric flat on an open region $U$ if every point of $U$ has coordinates nearby in which $g_{\mu\nu} = \eta_{\mu\nu}$, or $\delta_{ij}$ for a positive-definite metric: the squared paper of *Curved surfaces*, written as a coordinate grid. For the Levi-Civita connection the flatness criterion says

$$R^\rho{}_{\sigma\mu\nu} = 0 \text{ on } U \iff g \text{ is flat on } U.$$

*Flat gives zero.* In constant-metric coordinates every derivative of $g_{\mu\nu}$ vanishes on an open set, so every Christoffel symbol vanishes there, and so do their derivatives. Every term of the Christoffel formula is then zero, and a tensor that is zero in one coordinate system is zero in all. The open set matters: at a single event, free-fall coordinates make every Christoffel symbol vanish in any spacetime, as *Local flatness* showed, and the derivatives $\partial\Gamma$ that survive there carry the curvature.

*Zero gives flat.* Take a point of $U$ and a small coordinate ball around it, which is simply connected. By *When can a vector field be parallel everywhere?*, an orthonormal basis at the point spreads to $n$ parallel fields $e_{(a)}$, and they stay orthonormal because transport preserves inner products. Their dual one-forms $\omega^{(a)}$, defined by $\omega^{(a)}(e_{(b)}) = \delta^a{}_b$, are parallel too, because those contractions are constants and transport preserves contractions. Because the connection is torsion-free, a parallel one-form is curl-free: $\partial_\mu\omega_\nu - \partial_\nu\omega_\mu = (\Gamma^\lambda{}_{\mu\nu} - \Gamma^\lambda{}_{\nu\mu})\omega_\lambda = 0$. A curl-free one-form on a small ball is a gradient, $\omega^{(a)}{}_\mu = \partial_\mu X^{(a)}$, taken on trust here beyond the three-dimensional case of *Vector calculus*. The $n$ functions $X^{(a)}$ serve as coordinates, because their differentials $dX^{(a)} = \omega^{(a)}$ are independent, and the coordinate basis dual to those differentials is the frame $e_{(a)}$ itself, so $g_{ab} = g(e_{(a)}, e_{(b)}) = \eta_{ab}$, or $\delta_{ab}$, everywhere on the ball.

The criterion is about the Riemann tensor on a region, and two things that look like curvature are not.

- *Christoffel symbols that do not vanish.* Polar coordinates on a plane have $\Gamma^r{}_{\phi\phi} = -r$, as *The covariant derivative* found, and the plane is flat.
- *Metric coefficients that change from place to place.* The accelerating rocket of *Accelerated observers*, $ds^2 = -(1 + gx/c^2)^2c^2dt^2 + dx^2 + dy^2 + dz^2$, has a $g_{00}$ that changes with height, clocks that tick at different rates at different heights, and no curvature at all: with $N(x) = 1 + gx/c^2$ for the coefficient of $c\,dt$, the check *A rocket's clocks* finds $R^x{}_{0x0} = NN'' = 0$ because $N$ is linear in $x$. For any metric of the form $ds^2 = -N(x)^2c^2dt^2 + dx^2 + dy^2 + dz^2$, curvature needs the clock-rate profile $N(x)$ to bend, not merely to slope.

*The Riemann tensor vanishes on a region exactly when coordinates near each of its points make the metric constant; nonzero Christoffel symbols, metric coefficients that vary from place to place, and Christoffel symbols that vanish at a single event prove nothing either way.*

## Reading another author's table

Open two books on gravity and the same sphere can have Riemann components of opposite sign, with neither author wrong. A sign convention is a choice about which way counts as plus; it changes how a result is written and never what a carried arrow does. Two such choices touch the Riemann tensor itself, and the course has fixed both: the signature $(-,+,+,+)$ of *The interval and causality*, and the Riemann tensor defined by the Christoffel formula, so that $[\nabla_\mu,\nabla_\nu]V^\rho = R^\rho{}_{\sigma\mu\nu}V^\sigma$. A third choice, which index pair to contract, arises when the tensor is traced in *Ricci, Bianchi and Einstein tensors*. A source may also list the four slots in a different order; that is a relabelling, not a sign, so match its slots to the course's before reading off any sign.

Describe a source by two signs relative to the course. Its metric is $\tilde g_{\mu\nu} = s_g\,g_{\mu\nu}$, and its Riemann tensor is $s_R$ times the course expression built from its own Christoffel symbols. Follow each switch through. A Christoffel symbol holds one inverse metric and one derivative of the metric, so under $g \to -g$ both factors change sign and $\Gamma^\lambda{}_{\mu\nu}$ is unchanged. The mixed tensor is built from $\Gamma$ alone, so it carries only $s_R$; lowering an index brings one more metric factor, and with it one $s_g$:

$$\tilde R^\rho{}_{\sigma\mu\nu} = s_R\,R^\rho{}_{\sigma\mu\nu},\qquad \tilde R_{\rho\sigma\mu\nu} = s_g s_R\,R_{\rho\sigma\mu\nu}.$$

The sign $s_g$ can be read off the source's signature. To find its $s_R$, calibrate on a ball, whose behaviour no convention can change: walkers who start parallel draw together, and a loop walked with its region on the walker's left brings a carried arrow back turned toward the left. With the course conventions that turn gave $R_{\hat1\hat2\hat1\hat2} = K = +1/a^2$ in *Counting the survivors*. A source with $s_R = -1$ writes the small-loop law with a plus sign, $\Delta V^\rho = +\tilde R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, and finds $\tilde R_{\theta\phi\theta\phi} = -a^2\sin^2\theta$ for the same ball; in its table a saddle then comes out positive.

*Two sign choices touch the Riemann tensor, the signature and the overall sign of its definition; the mixed tensor carries the Riemann sign alone and the lowered one carries both, so read the signature off a source's metric and calibrate its Riemann sign on a ball before borrowing a formula.*

## Key equations

**Pair symmetries of the Riemann tensor** (derived-here)

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$$

The lowered Riemann tensor changes sign when the first pair is swapped, changes sign when the last pair is swapped, and is unchanged when the two pairs trade places. The last-pair rule holds for any connection; the first-pair rule needs the metric connection, and both indices of a pair must sit at the same level.

- $R_{\rho\sigma\mu\nu}$: Riemann tensor with all four indices down

Say: R rho sigma mu nu equals minus R sigma rho mu nu, equals minus R rho sigma nu mu, and equals R mu nu rho sigma.

**Cyclic identity** (derived-here)

$$R^\rho{}_{\sigma\mu\nu} + R^\rho{}_{\mu\nu\sigma} + R^\rho{}_{\nu\sigma\mu} = 0$$

Summed over the three cyclic orders of its last three indices, the Riemann tensor vanishes. It follows from the symmetry of the Christoffel symbols in their lower indices alone, and for the Levi-Civita connection it adds a new relation only among components with four different indices.

- $R^\rho{}_{\sigma\mu\nu}$: Riemann tensor with its first index up

Say: R rho sigma mu nu, plus R rho mu nu sigma, plus R rho nu sigma mu, equals zero.

**Number of independent Riemann components** (derived-here)

$$N_R(n) = \frac{N(N+1)}{2} - \binom{n}{4} = \frac{n^2(n^2-1)}{12},\qquad N = \frac{n(n-1)}{2}$$

The pair symmetries leave a symmetric array over the $N$ index pairs, and the cyclic identity removes one entry for each set of four different indices: $0$, $1$, $6$, $20$ and $50$ for $n = 1$ to $5$.

- $N_R(n)$: number of independent Riemann components in n dimensions
- $\binom{n}{4}$: number of ways to choose four different indices

Say: The number of independent components equals N times N plus one over two, minus n choose four, which simplifies to n squared times n squared minus one, over twelve.

**Integrability condition for a parallel field** (derived-here)

$$\nabla_\nu V^\rho = 0 \;\Rightarrow\; R^\rho{}_{\sigma\mu\nu}V^\sigma = 0$$

A vector field that is parallel in every direction must be sent to zero by the Riemann tensor for every loop plane, because the Ricci identity gives the mismatch of its mixed second derivatives and a parallel field has none.

- $V^\rho$: components of the parallel vector field

Say: If nabla nu of V rho is zero everywhere, then R rho sigma mu nu times V sigma is zero.

## Checks

**mixed-index-partner** (numeric): On a sphere of radius $a$, with $\theta$ measured from the pole, $R^\theta{}_{\phi\theta\phi} = \sin^2\theta$. A student applies antisymmetry in the first pair and writes $R^\phi{}_{\theta\theta\phi} = -\sin^2\theta$. Find the correct value of $R^\phi{}_{\theta\theta\phi}$ and say what went wrong.

Answer: $R^\phi{}_{\theta\theta\phi} = -1$. Antisymmetry in the first pair holds for the tensor with both first-pair indices down. Lower $\theta$ in the given component: $R_{\theta\phi\theta\phi} = g_{\theta\theta}\sin^2\theta = a^2\sin^2\theta$. Then $R_{\phi\theta\theta\phi} = -a^2\sin^2\theta$, and raising $\phi$ divides by $g_{\phi\phi} = a^2\sin^2\theta$, which gives $-1$. The student treated the raised index as if it carried the same metric factor as the lowered one.

Key points: Both indices of a pair must sit at the same level; the value is minus one everywhere

Numeric: R phi theta theta phi = -1 1

**a-rockets-clocks** (derive): The accelerating rocket of *Accelerated observers* has the metric $ds^2 = -N(x)^2c^2dt^2 + dx^2$ with $N = 1 + gx/c^2$, the $dy^2 + dz^2$ terms changing nothing here, so clocks at height $h$ above the floor tick faster than floor clocks by the factor $1 + gh/c^2$. Show that $R^x{}_{0x0} = NN''$ for any $N(x)$, evaluate it for the rocket, and then for a cabin in which every height needs the same proper acceleration $g$ to stay put.

Answer: With $x^0 = ct$, $g_{00} = -N^2$ and $g_{xx} = 1$, the nonzero Christoffel symbols are $\Gamma^x{}_{00} = -\tfrac12 g^{xx}\partial_x g_{00} = NN'$ and $\Gamma^0{}_{0x} = \tfrac12 g^{00}\partial_x g_{00} = N'/N$. In the course formula for $R^x{}_{0x0}$ the terms containing $\Gamma^x{}_{x0}$ and $\Gamma^x{}_{xx}$ vanish, leaving $\partial_x\Gamma^x{}_{00} - \Gamma^x{}_{00}\Gamma^0{}_{x0} = (NN')' - N'^2 = NN''$, the one independent component in two dimensions. For the rocket $N$ is linear, so $R^x{}_{0x0} = 0$: flat, whatever the clocks do. An observer held at fixed $x$ has $u^0 = c/N$ and needs the proper acceleration $a^x = \Gamma^x{}_{00}(u^0)^2 = c^2N'/N$; requiring this to equal $g$ at every height gives $N = e^{gx/c^2}$ and $R^x{}_{0x0} = (g/c^2)^2e^{2gx/c^2}$, which at $x = 0$ with $g = 9.81\ \mathrm{m\,s^{-2}}$ is $1.19\times10^{-32}\ \mathrm{m^{-2}}$: tiny, but curved.

Key points: R x 0 x 0 equals N times N double prime: zero for the rocket's linear N, nonzero when the needed acceleration is the same at every height

Numeric: R x 0 x 0 for the rocket, in inverse square metres = 0 1; R x 0 x 0 at the floor of the cabin with the same acceleration at every height, in inverse square metres = 1.19e-32 1

**count-in-five-dimensions** (numeric): In five dimensions, a student counts the index pairs of the lowered Riemann tensor, builds the symmetric array over them, and reports the array's number of entries as the number of independent components. What number does the student report, what is the correct number, and what was left out?

Answer: The student reports $55$; the correct number is $50$; the cyclic identity was left out. With $n = 5$ there are $N = 5 \cdot 4/2 = 10$ unordered pairs, and a symmetric $10 \times 10$ array has $N(N+1)/2 = 55$ entries. The cyclic identity adds one relation for each set of four different indices, and five indices give $\binom{5}{4} = 5$ such sets, so $55 - 5 = 50$, which matches $n^2(n^2-1)/12 = 25 \cdot 24/12 = 50$. The student's count would be right only if the cyclic identity said nothing new, as it does on a surface and in space.

Key points: Ten pairs give a symmetric array with 55 entries; The cyclic identity removes one number per set of four different indices, five sets in five dimensions, leaving 50

Numeric: the student's count = 55 1; independent components in five dimensions = 50 1

**a-strangers-sphere** (predict): A source writes the small-loop law as $\Delta V^\rho = +R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$, with the same slot order as the course, and uses the signature $(+,-,-,-)$. What does it give for $R^\theta{}_{\phi\theta\phi}$ on a sphere of radius $a$ at $\theta = 90^\circ$? For a spacetime, do its lowered components $\tilde R_{\rho\sigma\mu\nu}$ agree with the course's or not?

Answer: Its $R^\theta{}_{\phi\theta\phi}$ is $-1$ at $\theta = 90^\circ$, and its lowered spacetime components agree with the course's. The plus sign in the loop law means $s_R = -1$, so every mixed component is the course's with the sign flipped: $-\sin^2\theta$, which is $-1$ at the equator. The sphere's metric is positive definite for both, so the source's $R_{\theta\phi\theta\phi}$ is $-a^2$ there. In spacetime the signature switch gives $s_g = -1$, and lowered components carry $s_gs_R = +1$, so they match the course's even though the mixed ones are opposite. Neither source is wrong: the arrow turns the same way in both.

Key points: The Riemann sign is minus one, and lowered components carry the product of both signs, plus one here

Numeric: the source's R theta phi theta phi at the equator = -1 1

## Misconceptions

- **mixed-tensor-antisymmetric**: "The Riemann tensor with its first index up is antisymmetric in its first two indices, like the lowered one." — Antisymmetry in the first pair holds with both indices down. Raising one brings a metric factor the other does not carry; on a sphere the theta-phi-theta-phi mixed component is sine squared theta while the phi-theta-theta-phi one is minus one. (diagnosed by mixed-index-partner)
- **pair-rules-finish-the-count**: "The two antisymmetries and pair exchange finish the count, so spacetime keeps the 21 entries of a symmetric 6 by 6 array." — The cyclic identity removes one more number for each set of four different indices: none on a surface or in space, one in spacetime, which leaves 20, and five in five dimensions, which leaves 50. (diagnosed by count-in-five-dimensions)
- **christoffels-mean-curvature**: "Nonzero Christoffel symbols, or metric coefficients that vary from place to place, mean the space is curved." — Polar coordinates on a plane and the accelerating rocket have both, with zero Riemann tensor. Only the Riemann tensor decides, and it must vanish on a region, not merely at an event. (diagnosed by a-rockets-clocks)
- **opposite-sign-means-mistake**: "If two sources give the same sphere Riemann components of opposite sign, one of them has made a mistake." — Which way counts as plus is a convention. Calibrate each source on a ball, where walkers draw together whatever the signs, and translate before comparing. (diagnosed by a-strangers-sphere)

## Glossary

- **pair antisymmetry**: Swapping the two indices of the first pair, or of the last pair, of the lowered Riemann tensor changes its sign; trading the two pairs, called pair exchange, leaves it unchanged. (`symmetries-of-the-riemann-tensor`)
- **cyclic identity**: The Riemann tensor summed over the three cyclic orders of its last three indices is zero; also called the first Bianchi identity. (`cyclic-identity`)
- **parallel field**: A vector field whose covariant derivative vanishes in every direction, so that a copy carried along any path matches the field where it stops. (`integrability-condition-for-parallel-fields`)
- **integrability condition**: The requirement that the Riemann tensor send a vector to zero on every loop plane, which any vector field that is parallel everywhere must satisfy. (`integrability-condition-for-parallel-fields`)
- **simply connected**: A region in which every closed loop can be shrunk to a point without leaving the region; a plane or a ball is, a cone with its tip removed is not. (`integrability-condition-for-parallel-fields`)
- **flatness criterion**: The theorem that the Riemann tensor vanishes on a region exactly when every point of the region has nearby coordinates with constant metric components. (`flatness-criterion`)
- **sign convention**: A choice about which way counts as plus when a result is written down; it changes the writing, never what is measured. (`curvature-sign-conventions`)

## Visuals

- `twenty-of-256-slots` (flagship): The count made visible: the 256 slots of the spacetime Riemann tensor collapsing under each rule to a symmetric 6 by 6 array of pairs and then to 20 survivors. Sketch: A grid of the 256 index slots with toggles that apply one rule at a time: each antisymmetry greys the repeated-index slots and pairs the rest with a sign, pair exchange folds the 6 by 6 array of pairs onto its diagonal, and the cyclic identity links the slots 0123, 0231 and 0312 with a readout of their sum.
- `painted-arrows-that-must-match` (core): The parallel-field test: a painting of arrows that succeeds on flat ground and fails on every patch of a ball, with the failure located on loops. Sketch: A patch of flat ground, a paper tube, a ball or a paper cone. The learner drops one arrow and spreads carried copies along chosen paths; where two routes deliver different copies the arrows double and the loop between them lights up with its turn as a readout.

## Tutor

Opening question: Picture the Riemann tensor of a sphere written out in the usual angle coordinates: sixteen components. Before computing any of them, how many do you expect to be zero, and how many different numbers do you expect the rest to hold? Then guess the same two counts for spacetime, where there are two hundred and fifty-six.

- Q: Why do the symmetries need the first index lowered? A: Because two of the rules compare the slot that holds the carried vector with the slot where its change is read, and those slots match only when both sit at the same level. With one index up and one down, raising and lowering bring different metric factors, so the components are not simply negatives of each other. On a sphere the mixed component is sine squared theta, while its would-be partner is minus one.
- Q: If books disagree about the sign of the Riemann tensor, which one is right? A: Both. The sign is a convention, like choosing whether a turn to the left counts as plus. Find what a book gives for a ball, where walkers who start parallel always draw together, and translate. Then remember that lowering an index also brings the signature into play, so read the signature off the book's metric too.

## Review: novice

Verdict fixed (2026-09-16, revision 4)

Retell attempt: Lower the first index of the Riemann tensor with the metric and three rules appear: swap the first two indices and it changes sign, swap the last two and it changes sign, trade the two pairs and nothing changes. You prove them at any one event in the coordinates where the metric's first derivatives vanish, because the tensor is then half a signed sum of four second derivatives of the metric and the rules can be read off that sum; they are statements that a tensor is zero, so they hold in every basis. A fourth rule, the cyclic identity, says the sum over the three cyclic orders of the last three indices is zero; it uses only the symmetry of the Christoffel symbols in their lower indices, and it says something new only when all four indices differ, so only in spacetime, where it is one relation among R 0123, R 0231 and R 0312. Counting: the pair rules make the tensor a symmetric array over index pairs, N equal to n(n-1)/2 of them, so N(N+1)/2 entries, minus n choose 4 for the cyclic identity: one number on a surface, six in space, twenty in spacetime, and the twenty are the second derivatives of the metric that a falling frame cannot remove. On a surface the one number is the Gaussian curvature, R 1212 equals K times det g. A parallel field is a painting of arrows that a carried copy always matches; it must be sent to zero by the Riemann tensor on every loop plane, so a full parallel frame needs zero curvature, and on a surface even one parallel field forces K to vanish, so no patch of a sphere, however small, carries one. Going back from zero curvature to parallel fields needs a simply connected region, a cone with its tip removed being the counterexample, and is taken on trust. The flatness criterion: the Riemann tensor is zero on a region exactly when coordinates near each point make the metric constant. Flat gives zero because every Christoffel symbol vanishes on an open set; zero gives flat by spreading an orthonormal frame as parallel fields, whose dual one-forms are curl-free and so are gradients of functions that serve as the flat coordinates. Nonzero Christoffel symbols, as in polar coordinates, and metric coefficients that vary from place to place, as in the rocket, are not curvature; the rocket's clock rates slope but do not bend. Sign conventions: two switches touch the Riemann tensor, the signature and the overall sign of the definition; Christoffel symbols do not feel the signature, so the mixed tensor carries only the Riemann sign and the lowered tensor carries both; calibrate another author's sign on a ball, where the course gets R 1212 equal to plus K. Things I could not say back after one reading: why swapping rho and sigma sends the first term to the fourth, when my own try landed it on the third; why R 1212 and det g pick up the same factor; how matching the turn and the loop law gives plus K rather than minus K; why the dual one-forms are parallel and why the functions X are coordinates; what a wedge angle is; and what 'sufficiency' was sufficient for.

16 stumbles

- “Swap $\rho$ with $\sigma$: the first term becomes the fourth and the second becomes the third, so the sum changes sign. Swap $\mu$ with $\nu$: the same trades happen”: Doing the swap by hand, the first term becomes minus the third and the second minus the fourth; the fourth-and-third pairing belongs to the mu-nu swap, so 'the same trades' is also wrong. I reread three times.
- “Of the six second derivatives that appear, two cancel”: Which two is left implicit, and the reader must redo the expansion to find them.
- “with $\mu = \nu$ the first term is zero and the other two are opposites”: This uses last-pair antisymmetry for the tensor with its first index up, but the part before derived all three rules only for the lowered tensor; the key equation's meaning says the last-pair rule holds for any connection, and the text never says why.
- “whichever of its four indices is lowered”: The lowered index is always the first one; the sentence means whichever index sits in the first slot.
- “matching the two for $V = e_1$ gives $R_{\hat1\hat2\hat1\hat2} = K$”: The matching step is left implicit and the sign is the whole point; my own attempt came out as minus K until I used first-pair antisymmetry.
- “pick up the same squared Jacobian factor”: A surprising claim with no reason: why should a Riemann component transform like a determinant?
- “The Ricci identity of *Holonomy and the Riemann tensor* says what the disagreement would be”: The sentence before it talks about mixed partial derivatives disagreeing, then the Ricci identity is about covariant derivatives; the switch is unexplained.
- “On a surface even one field is too much.”: 'Too much' for what? The idea is that one parallel field already forces zero curvature.
- “Sufficiency needs the region to be simply connected”: Sufficiency of what for what? The condition R V = 0 at a point is never sufficient; the converse being discussed is from zero curvature to parallel fields.
- “turns a vector by the wedge angle”: 'Wedge angle' is never defined; the cone was only ever a paper cone.
- “Their dual one-forms $\omega^{(a)}$ are parallel too”: Why are they parallel? A step left implicit.
- “In the coordinates $X^{(a)}$ the coordinate basis is the frame $e_{(a)}$ itself”: Two steps implicit: why the n functions are coordinates at all, and why their coordinate basis is the frame.
- “finds $R^x{}_{0x0} = NN'' = 0$ for its linear $N$”: N is used in the part without being defined there; it is defined only in the check.
- “a stranger's table of curvature”: 'Stranger' and 'table' are metaphors the summary uses before the reader meets them; the part itself says 'two books'.
- “The signature $s_g$ can be read off the source's metric.”: s_g is a sign, not the signature; the two words were used for one idea.
- “simply connected”: A new technical term introduced in a part, used again in the next part, and absent from the glossary.

Fixes:
- Corrected the term-tracking in the first-pair and last-pair swaps of the four-term formula (first becomes minus the third and second minus the fourth under rho-sigma; first-fourth and second-third under mu-nu) and named the two cancelling terms.
- Added to the first part that the last-pair rule holds for the mixed tensor and any connection, and that the first-pair rule needs both indices at the same level, which the cyclic-identity part and the first check rely on.
- Made the calibration R 1212 = K explicit with edge lengths l1 and l2 and the first-pair antisymmetry step, and gave the reason R 1212 and det g share the squared Jacobian determinant.
- Reworded the parallel-field part: bridge from mixed partials to the Ricci identity, 'even one parallel field forces the curvature to vanish', the converse named instead of 'sufficiency', and the cone's wedge angle defined.
- Made the zero-gives-flat argument explicit: why the dual one-forms are parallel, why the functions X are coordinates, and eta or delta for the metric; defined N in the rocket paragraph.
- Replaced 'stranger's table' with 'another author's table' in the summary, opening and part heading; 'sign s_g' read off the 'signature'.
- Added the check count-in-five-dimensions (55 versus 50) with the misconception pair-rules-finish-the-count, as the writer suggested, using the review allowance; added glossary entries for integrability condition and simply connected.
- Revision 1 to 2; status novice-reviewed.

Concerns:
- The back-references to unwritten sections (The metric, Local flatness, Tensors as machines, The Levi-Civita connection, The covariant derivative, Vector calculus, Accelerated observers, The interval and causality) could not be checked; the reader is assumed to know one-forms, dual bases, contractions, curl-free means gradient in three dimensions, the polar Christoffel symbol and the rocket metric from them.
- The physics reviewer should re-check the corrected term-tracking in the first part and the sign chain in the R 1212 = K calibration (course small-loop law with the minus sign, region on the walker's left).
- The rocket check's numeric answers use unit '1' with the unit named in the quantity string, because the unit table has no inverse square metre.
- The two converse statements taken on trust (parallel fields from zero curvature on a simply connected region; curl-free one-forms are gradients on a ball) remain unproved at this depth.

## Review: physics

Verdict fixed (2026-09-16, revision 4)

14 verification items, 9 counterexamples

- Sphere Riemann components in the opening: R^th_ph th ph = sin^2 th, R^th_ph ph th = -sin^2 th, R^ph_th th ph = -1, R^ph_th ph th = 1, twelve of sixteen zero, lowered values +-a^2 sin^2 th: All four values match to 1e-6; exactly 4 nonzero components; R_thphthph / det g = 0.25 = 1/a^2
- Four-term formula for R_rsmn at a point with vanishing first derivatives, and its term tracking under rho-sigma swap (T1 -> -T3, T2 -> -T4), mu-nu swap (T1 -> -T4, T2 -> -T3) and pair exchange (T1 <-> T2, T3 and T4 fixed): Formula and all three swap statements confirmed; the reader reviewer's corrected pairing is right; the formula also satisfies the cyclic identity
- Cyclic identity proof groups derivative and product terms into torsion brackets; with two equal indices among sigma, mu, nu, or with rho equal to one of them, it follows from the pair rules; R_1312 = R_1213 = -R_1231: Confirmed
- Independent components N(N+1)/2 - C(n,4) = n^2(n^2-1)/12 = 1, 6, 20, 50 for n = 2..5, and pair rules alone give 1, 6, 21, 55: Free components 1, 6, 20, 50 exactly; pairs-only counts 1, 6, 21, 55; the check count-in-five-dimensions is right
- Calibration R_1212 (hatted) = K from the course small-loop law with the minus sign and the holonomy section's left-turn rule: Confirmed; the course small-loop law matches the standard holonomy formula for the course Riemann definition
- R_1212 = K det g in any coordinates and R_rsmn = K(g_rm g_sn - g_rn g_sm); its 1212 component is det g: Confirmed
- Integrability condition R^r_smn V^s = 0 from the Ricci identity; on a surface it reads K(delta^r_m V_n - delta^r_n V_m) = 0, giving K V_2 = 0 and K V_1 = 0: Confirmed; the argument that V stays nonzero was fixed (see fixes)
- Earth loop of one square kilometre turns a carried vector by A/R^2 = 2.5e-8 rad, about 1.4 millionths of a degree: 2.46e-8 rad = 1.41e-6 degrees
- Rocket check: Gamma^x_00 = N N', Gamma^0_0x = N'/N, R^x_0x0 = N N''; zero for N = 1 + g x/c^2; proper acceleration c^2 N'/N; N = exp(g x/c^2) gives (g/c^2)^2 exp(2 g x/c^2) = 1.19e-32 m^-2 at x = 0: Confirmed: finite difference 0.52320 versus N N'' = 0.5232; (9.81/c^2)^2 = 1.191e-32; the sign agrees with the course convention since the exponential-N metric is two-dimensional anti-de Sitter with negative Ricci scalar -2 N''/N
- Polar coordinates on the plane: Gamma^r_phph = -r and Riemann zero: Gamma^r_phph = -1.70 at r = 1.7; max Riemann component 1e-7 (discretisation)
- Zero gives flat: dual one-forms of a parallel frame are parallel; a parallel one-form is curl-free for a torsion-free connection; curl-free on a ball gives a gradient; the differentials are independent so the functions are coordinates and their coordinate basis is the frame: Confirmed; both trusted steps are named as such in the text
- Sign conventions: Christoffel symbols unchanged under g -> -g; mixed Riemann carries s_R, lowered carries s_g s_R; a source with a plus-sign loop law has s_R = -1 and gets -a^2 sin^2 th on the sphere; check a-strangers-sphere gives -1 mixed at the equator and lowered spacetime components that agree: Confirmed
- Check mixed-index-partner: R^ph_th th ph = -1 from lowering, first-pair antisymmetry and raising with g^phph = 1/(a^2 sin^2 th): Confirmed, -1.0000007 numerically
- Statements borrowed from earlier sections (small-loop law with minus sign, Christoffel formula, Ricci identity, four-second-derivative form at a point, twenty second derivatives left by normal coordinates, left-turn rule, K as det of the second fundamental form over det g): All present with the same signs and slot order

Fixes:
- Parallel-field part: the claim that a parallel field nonzero at one point stays nonzero was justified by constancy of g(V,V), which fails for null vectors in a Lorentzian metric; replaced by the invertibility of parallel transport along any curve, which holds in every signature.
- Flatness part: scoped the sentence about clock-rate profiles to metrics of the form -N(x)^2 c^2 dt^2 + dx^2 and named N(x); wrote 'coordinate ball' where a solid coordinate ball, not the surface of a ball, is meant.
- Counting part: named the quantity as the number of independent components where the formula is introduced, so the concept is introduced by name.
- Sign-convention part: added that a source may order the four slots differently, which is a relabelling and not a sign, so slots must be matched before signs are read.
- builds_on: added the-metric and vector-calculus, which the opening and the zero-gives-flat argument name.
- Status physics-reviewed; revision 2 to 3.

Concerns:
- Eight named earlier sections (The metric, Local flatness, Tensors as machines, The Levi-Civita connection, The covariant derivative, Vector calculus, Accelerated observers, The interval and causality) are not yet written; the section assumes from them the Riemann-normal-coordinate result, the zero-in-one-basis argument, torsion-freeness, the polar Christoffel symbol, the Rindler metric, one-forms and dual bases, and the three-dimensional curl-free-means-gradient result. Their short names differ slightly from the outline titles.
- Two results are taken on trust at this depth and said to be: parallel fields from zero curvature on a simply connected region, and curl-free one-forms are gradients on a coordinate ball.
- The rocket check reports inverse square metres with unit '1', since the unit table has no inverse square metre.
- The text mentions no slot-order convention beyond the new sentence; sources that write the loop pair first (R_mn rs) need relabelling before the s_R test.
