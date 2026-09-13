# Holonomy

`holonomy` · curvature · core

**Needs:** [path-dependence-of-parallel-transport] · [gaussian-curvature] · [angular-excess] · [riemann-curvature-tensor] (for way 3 only)
**Opens:** [riemann-curvature-operator] · [bianchi-identity] · [gauge-field-strength]
**Visuals:** ★ [carry-an-arrow-around-a-loop] · [shrink-the-loop] · [cone-deficit] · [latitude-loop] · [cube-of-loops]

## In one breath

Carry an arrow around a closed loop without ever twisting it, then compare it with how it started. The mismatch is
the loop's **holonomy**. It is how a creature trapped inside a space discovers that the space is curved, and for small
loops the turn per unit of enclosed area *is* the curvature.

## Ways in

### 1. The insider's test · intuition

Walk a closed circuit on a big ball holding a pointer that you never turn relative to the ground. Back at the gate,
the pointer has turned. Fence in twice the ground and it turns twice as much; walk the other way and it turns the
other way. On a flat field, or on paper rolled into a tube, it always comes back unchanged. The turn is something you
measure from inside, without looking at the ball from outside, and that is exactly the situation we are in with
spacetime.

*Picture:* a fenced paddock on a globe, the pointer at the gate before and after one lap.
*Honest about:* surfaces only allow rotations; in spacetime a loop can also return a boost.
*Visual:* carry-an-arrow-around-a-loop, with sphere, plane and cylinder side by side.

### 2. Turning equals enclosed curvature · working

On any surface the return angle is the total curvature inside the loop:
$\Delta\alpha = \iint_S K\,dA$. On a sphere of radius $a$, $K = 1/a^2$, so the turn is area over radius squared.
For a triangle of great-circle arcs this is its angular excess: three right angles on the octant triangle give a
quarter turn. For a circle at colatitude $\theta_0$ it is $2\pi(1-\cos\theta_0)$. The rule is exact for loops of any
size, which makes a surface the best place to build trust before going to four dimensions.

*Visual:* carry-an-arrow-around-a-loop (area readout), latitude-loop.

### 3. Shrink the loop, find Riemann · working → formal

Take a tiny parallelogram with edges $a^\mu$ and $b^\nu$. Transport along the four edges, pair opposite edges so the
first-order pieces cancel, and a second-order remainder survives:

$$\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}\,V^\sigma a^\mu b^\nu \qquad (\text{route } +a,\ +b,\ -a,\ -b)$$

Each feature of the result explains a feature of the Riemann tensor. The change is linear in $V$, so the loop acts as a
matrix. It is linear in each edge, so doubling a side doubles it. It is antisymmetric in the edges, so reversing the
route flips it. It is second order, so it scales with area. Riemann is the machine that turns an oriented little area
into a little rotation.

*Visual:* shrink-the-loop.

### 4. A loop is a transformation · formal

The holonomy of a loop $\gamma$ at $p$ is a linear map on the tangent space,
$\mathrm{Hol}(\gamma) = \mathcal{P}\exp\!\big(-\oint_\gamma \Gamma_\mu\,dx^\mu\big)$. Because the metric connection
preserves lengths and angles, it is a rotation on a surface and a Lorentz transformation in spacetime. All loops at $p$
together form the holonomy group. For an infinitesimal loop, $\mathrm{Hol} = 1 - \epsilon^2\,\mathcal{R}(u,v)$ with
$\mathcal{R}(u,v) = [\nabla_u,\nabla_v] - \nabla_{[u,v]}$. Curvature is the infinitesimal version of holonomy, and the
Ambrose–Singer theorem says curvature generates all of it. Loops that cannot be shrunk away can have holonomy even where
curvature vanishes, as around the tip of a cone.

### 5. The same idea everywhere · bridge

The pattern of carrying something around a loop and finding it changed recurs throughout physics. A charged particle's
quantum phase shifts by the enclosed magnetic flux (Aharonov–Bohm), and the field strength $F_{\mu\nu}$ plays the role
of Riemann. Light in a coiled fibre returns with its polarization rotated by the solid angle its direction swept
(Berry's phase). A Foucault pendulum's swing plane is carried around a circle of latitude. Gravity and gauge fields
share one geometric language, and holonomy is its most tangible word.

## Key equations

| Equation | Meaning | Say it aloud |
| --- | --- | --- |
| $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu}V^\sigma a^\mu b^\nu$ | small loop: change = Riemann fed the vector and both edges | "the change in V is minus Riemann, acting on V and the two edges of the loop" |
| $\Delta\alpha = \iint_S K\,dA$ | surface: turn = enclosed curvature, any size | "the turn equals the curvature summed over the inside" |
| $\Delta\alpha = \alpha_1+\alpha_2+\alpha_3-\pi$ | geodesic triangle: turn = angular excess | "how far the angles overshoot a straight line" |
| $\mathrm{Hol}(\gamma) = \mathcal{P}\exp(-\oint\Gamma_\mu dx^\mu)$ | finite loop: ordered product of connection steps | "the path-ordered exponential of the connection around the loop" |

## Teaching arc

1. **Ask the insider question.** How could a flat creature find out its world is curved without leaving it?
2. **Show one surprise and two controls.** The octant loop on a sphere returns a quarter turn; the same loop on a plane
   and on a rolled cylinder returns nothing. That rules out bending and the transport rule as explanations.
3. **Let them discover the area law.** Resize, reverse and reshape the loop, change the radius, and tabulate the turn
   against area over $a^2$. Only then name angular excess.
4. **Derive the small-loop law** on a parallelogram. Point at linearity and antisymmetry as the reason Riemann has the
   slots it has.
5. **Check it twice.** A unit-sphere coordinate cell gives a turn equal to its area. Polar coordinates on a plane give
   zero, even though the Christoffel symbols are nonzero.
6. **Mark the limits** with the cone, and note that the area law is exact only in 2D.
7. **Transfer.** Gauge phases, then a cube of face loops cancelling, which is the Bianchi identity.

## Analogies

- **Ant on a ball.** An insider detects curvature by comparing an arrow after a round trip. *Limits:* 2D and Riemannian,
  so there is only rotation; triangle angle sums are a second insider test.
- **Foucault pendulum.** In one sidereal day the swing plane is carried around its latitude circle. Measured against
  local north it turns by $2\pi\sin(\text{latitude})$. The holonomy angle $2\pi(1-\cos\theta_0)$ differs by exactly one
  full turn, which is local north's own rotation. *Limits:* dynamics only approximately enforce transport; this is
  Earth's surface curvature, not spacetime's.
- **Polarization in a coiled fibre.** The light's direction traces a loop on the sphere of directions, and its
  polarization returns rotated by the enclosed solid angle. *Limits:* this is a sphere of directions, not physical
  space, and an optical effect, not gravity.

## Misconceptions

| Belief | Correction | Question that exposes it |
| --- | --- | --- |
| Direction of travel doesn't matter. | Reversing the loop inverts the holonomy (antisymmetry in the edges). | "Clockwise gave 2° clockwise. What does counterclockwise give?" |
| Zero curvature along the loop means no turn. | Only for loops that can be shrunk within the flat region. | "A 60° wedge is cut from a paper cone. Every patch the ant crosses is flat. Does the pointer come back unchanged?" |
| You can read the turn partway round. | Arrows at different points can't be compared route-independently; the angle exists only when the loop closes. | "Halfway round, a readout says 45°. Relative to what?" |
| The small-loop formula works for big loops. | It is leading order; big loops need the ordered integral (the 2D area law is special). | "Could Riemann at the north pole alone predict the octant turn?" |
| Holonomy can stretch vectors. | Metric transport preserves lengths and angles, so it is a rotation or boost. | "If ΔV is a small added arrow, how does the length stay fixed?" |
| In spacetime, only the area matters. | The oriented plane matters, and a loop in a plane containing time returns a boost. | "Horizontal vs vertical loop near Earth: same holonomy?" |

## Checks

1. **Intuition.** A small loop turns your pointer 3°. What happens with twice the area? With the loop reversed?
   → About 6°; 3° the other way.
2. **Working.** A great-circle triangle on a sphere of radius 1000 km has angles 100°, 60°, 50°. Find the turn and the
   area. → Excess 30° = π/6 rad; area = (π/6)(1000 km)² ≈ 5.2 × 10⁵ km².
3. **Working.** Transport once around latitude 30° N. → Cap area $2\pi a^2(1-\cos 60°) = \pi a^2$, so a half turn.
4. **Formal.** A cone has a 90° wedge removed. "Every patch is flat, so every loop gives zero holonomy." Evaluate.
   → False for loops around the tip, which return rotated by 90°. Flatness guarantees trivial holonomy only for
   contractible loops.

## Notation traps

- The sign of $\Delta V$ depends on which edge you walk first and on the sign convention for Riemann, and textbooks
  differ on both. Always say the route. Course form: $+a, +b, -a, -b$ gives $-R$.
- Gauge phases: writing $D_\mu = \partial_\mu + iqA_\mu$ or $\partial_\mu - iqA_\mu$ flips the sign in the exponent.
  State the choice whenever the analogy is used.

## Tutor moves

- **Open with:** "If you never turn the arrow, can it come back turned?" Let the learner commit to an answer first.
- **Demo moment:** run the octant loop *after* the learner predicts; hide the angle until the loop closes.
- **When they say "but the arrow did turn, I saw it":** separate turning relative to the room (it does) from turning
  relative to the surface (it never does).
- **Level switch:** learners without calculus stay in ways 1–2 and the cone; learners with tensors go to way 3 within
  two minutes of the demo.

## The giants

- **Gauss (1827), *Disquisitiones generales circa superficies curvas*.** Curvature is intrinsic, and the angle excess
  of a geodesic triangle equals its enclosed curvature.
- **Levi-Civita (1917).** Defined parallel transport on any curved space, turning Riemann's curvature into something
  you can carry an arrow through.
- **Cartan (1926), *Les groupes d'holonomie des espaces généralisés*.** Named and systematized holonomy groups.
- **Ambrose & Singer (1953).** Curvature generates the holonomy group.
- **Aharonov & Bohm (1959); Berry (1984).** Holonomy made physical: phases from enclosed flux, and geometric phases in
  quantum and optical systems.
