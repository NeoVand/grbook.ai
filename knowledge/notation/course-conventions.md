---
type: conventions
status: adopted
decided: 2026-09-12
revised: 2026-09-13
---

# Course conventions

grbook.ai uses one set of conventions everywhere: prose, equations, demos, narration, and the tutor. Translate every
result into these conventions before writing it. When the literature commonly uses a different choice, record it in
the note's `notation_traps` in generic terms ("some texts use…"). Never name a source. A notation trap's
`course_choice` must agree with this file. If a note needs a choice this file does not make, stop and report it;
never invent a note-local convention.

## Gravity and geometry

The gravity conventions are the $(-,+,+,+)$ "plus" conventions standard in modern GR research: a sphere has positive
Ricci scalar, and $G_{\mu\nu} = +8\pi G T_{\mu\nu}/c^4$.

| Item | Course choice |
| --- | --- |
| Metric signature | $(-,+,+,+)$, $\eta_{\mu\nu} = \mathrm{diag}(-1, 1, 1, 1)$ |
| Indices | Greek $\mu, \nu, \dots = 0,1,2,3$ for spacetime; Latin $i, j, \dots = 1,2,3$ for space; Einstein summation. Orthonormal-frame components carry hats: $u^{\hat t}$, $T_{\hat x \hat y}$ |
| Time coordinate | $x^0 = ct$; with $c = 1$, $x^0 = t$ |
| Four-velocity | $u^\mu = dx^\mu/d\tau$, $u_\mu u^\mu = -c^2$ (or $-1$ with $c = 1$) |
| Christoffel symbols | $\Gamma^\lambda{}_{\mu\nu} = \tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$ |
| Covariant derivative | $\nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\lambda} V^\lambda$ |
| Riemann tensor | $R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, so $[\nabla_\mu, \nabla_\nu] V^\rho = R^\rho{}_{\sigma\mu\nu} V^\sigma$ (torsion-free) |
| Small-loop holonomy | Walking $+a, +b, -a, -b$ changes a vector by $\Delta V^\rho = -R^\rho{}_{\sigma\mu\nu} V^\sigma a^\mu b^\nu$ |
| Ricci tensor and scalar | $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, $R = g^{\mu\nu} R_{\mu\nu}$; a sphere of radius $a$ has $R = +2/a^2$ |
| Einstein equation | $G_{\mu\nu} + \Lambda g_{\mu\nu} = \dfrac{8\pi G}{c^4} T_{\mu\nu}$, with $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu}$ |
| Geodesic deviation | $\dfrac{D^2 \xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\, u^\nu \xi^\rho u^\sigma$ |
| Perfect fluid | $T^{\mu\nu} = (\rho + p/c^2)\, u^\mu u^\nu + p\, g^{\mu\nu}$, with $\rho$ the mass density ($c = 1$: $(\rho + p) u^\mu u^\nu + p g^{\mu\nu}$) |
| Schwarzschild metric | $ds^2 = -(1 - 2GM/rc^2)\,c^2dt^2 + (1 - 2GM/rc^2)^{-1} dr^2 + r^2 d\Omega^2$ |
| FLRW metric | $ds^2 = -c^2dt^2 + a(t)^2 \left[\dfrac{dr^2}{1 - k r^2} + r^2 d\Omega^2\right]$ |
| Linearized gravity | $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, $\bar h_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$; Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$ gives $\Box \bar h_{\mu\nu} = -16\pi G T_{\mu\nu}/c^4$ |
| Levi-Civita tensor | $\epsilon_{0123} = +\sqrt{-g}$ in right-handed coordinates ($x^0$ future-directed, $(x^1, x^2, x^3)$ right-handed), so $\epsilon^{0123} = -1/\sqrt{-g}$ |
| Orientation and rotation sense | On an oriented surface, a positive rotation turns a walker's direction of travel toward the walker's left, with "left" defined with the walker's head along the chosen unit normal. Seen from the side the normal points to, that is counterclockwise. The holonomy angle of a simple loop bounding a region $S$ on the walker's left is positive in this sense and equals $\iint_S K\,dA$ modulo $2\pi$. This holds whatever the size of $S$: the reversed octant loop on a sphere has $7\pi/2 \equiv -\pi/2$, a turn to the walker's right. Notes state the branch they quote; demos use $(-180^\circ, 180^\circ]$. |

## Other physics

| Item | Course choice |
| --- | --- |
| Electromagnetism units | SI at entry and working rungs. $A^\mu = (\phi/c, \mathbf{A})$, $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ (so $F^{0i} = E^i/c$), Maxwell $\nabla_\nu F^{\mu\nu} = \mu_0 J^\mu$ with $J^\mu = (\rho c, \mathbf{J})$ |
| Lorentz force | $\dfrac{du^\mu}{d\tau} = \dfrac{q}{m} F^\mu{}_\nu u^\nu$, whose spatial part gives $q\gamma(\mathbf{E} + \mathbf{v}\times\mathbf{B})/m$ |
| Electromagnetic stress-energy | $T^{\mu\nu} = \dfrac{1}{\mu_0}\left(F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14 g^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)$, so $T^{00} = \tfrac12\varepsilon_0 E^2 + B^2/2\mu_0$ |
| Charged black holes | Reissner–Nordström factor $1 - \dfrac{2GM}{rc^2} + \dfrac{GQ^2}{4\pi\varepsilon_0 c^4 r^2}$ |
| Geometrized electromagnetism | Formal and research rungs that set $G = c = 1$ for Einstein–Maxwell results also set $4\pi\varepsilon_0 = 1$ and say so; the Reissner–Nordström factor becomes $1 - 2M/r + Q^2/r^2$. |
| Gauge covariant derivative | $D_\mu = \partial_\mu - i(q/\hbar)A_\mu$ for a field of charge $q$ (minimal coupling $p_\mu \to p_\mu - qA_\mu$). Parallel transport multiplies the field by $\exp\big(+i(q/\hbar)\int A_\mu dx^\mu\big)$. Around a loop the Aharonov–Bohm phase is $+q\Phi/\hbar$, where $\Phi$ is the magnetic flux through a surface bounded by the loop, oriented by the right-hand rule relative to the direction of travel. |
| Plane waves and Fourier transforms | Positive-frequency waves are $e^{i(\mathbf{k}\cdot\mathbf{x} - \omega t)} = e^{i k_\mu x^\mu}$ with $k^\mu = (\omega/c, \mathbf{k})$. $f(\mathbf{x}) = \int \dfrac{d^3k}{(2\pi)^3} \tilde f(\mathbf{k})\, e^{i\mathbf{k}\cdot\mathbf{x}}$ |
| Quantum | $\hbar$ and $k_B$ are explicit at entry and working rungs. Formal and research rungs may set $\hbar = k_B = 1$ and say so. |
| Spinors, tetrads beyond hatted components, Newman–Penrose | Not yet fixed; add them here before writing any note that needs them. |

## Units by rung

| Rung | Units |
| --- | --- |
| Entry | Everyday units in words: degrees, fractions of a turn, kilometres, seconds, years. No symbols without words. |
| Working | SI with $G$ and $c$ explicit. Accepted non-SI units, each with its SI value on first use: degrees, arcseconds, km, years, light-years, parsecs, solar masses, eV. |
| Formal and research | Geometrized $G = c = 1$ inside derivations, stated once per way. Every numerical result restores SI with the factors shown. |

## Practices

- **Name the convention when it matters for a sign:** "with signature $(-,+,+,+)$, a timelike vector has negative norm".
- **Speak equations in words.** Each equation carries `say_aloud` and `symbols[].say`; the tutor never reads raw LaTeX.
- **One symbol, one meaning within a note.** Scope symbols that are commonly reused: $K$ for Gaussian curvature versus
  the Kretschmann scalar, $a$ for a radius versus the scale factor.
- **Name the frame or basis** when a statement holds only in one, for example "in an orthonormal frame the connection
  one-forms commute in two dimensions".
