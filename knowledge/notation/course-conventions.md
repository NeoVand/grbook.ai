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
| Sectional curvature sign | $K(X,Y) = R_{\mu\nu\rho\sigma}X^\mu Y^\nu X^\rho Y^\sigma / \big(g(X,X)g(Y,Y) - g(X,Y)^2\big)$, so a sphere has $K = +1/a^2$. For a timelike plane the denominator is negative, so free-fall pairs that draw together have $K < 0$ there, the opposite of converging geodesics on a sphere. A note that compares tides to a ball says it compares behaviour, not the sign of $K$. |
| Extrinsic curvature of a hypersurface | $K_{\mu\nu} = -h_\mu{}^\alpha h_\nu{}^\beta \nabla_\alpha n_\beta$ with $n$ the unit normal (future-pointing for spacelike slices, outward for closed surfaces). For a surface embedded in flat space this is $K_{\mu\nu} = n\cdot\partial_\mu\partial_\nu X$: positive where the surface bends toward $n$. A round sphere of radius $R$ with outward normal has $K_{\mu\nu} = -h_{\mu\nu}/R$; an expanding FLRW slice has $K_{ij} = -H h_{ij}$ and $K = -3H$. Weingarten: $\partial_\mu n = -K^\lambda{}_\mu e_\lambda$. Some texts use the opposite sign ($K_{\mu\nu} = h\nabla n$); record it as a notation trap. |
| Curves in space | Frenet–Serret with $T' = \kappa N$, $N' = -\kappa T + \tau B$, $B' = -\tau N$, $\kappa \ge 0$, and $B = T\times N$; a right-handed helix has $\tau > 0$. Geodesic curvature on a surface is signed with left $= n\times T$ positive. |
| The letter $K$ | $K$ without indices is the Gaussian curvature (sphere $+1/a^2$). $K_{\mu\nu}$ with indices is the extrinsic curvature, and its trace is written $K$ only in 3+1 sections, where Gaussian curvature does not appear. The Kretschmann scalar is written $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$ or $\mathcal K$, never $K$. |
| Orientation and rotation sense | On an oriented surface, a positive rotation turns a walker's direction of travel toward the walker's left, with "left" defined with the walker's head along the chosen unit normal. Seen from the side the normal points to, that is counterclockwise. The holonomy angle of a simple loop bounding a region $S$ on the walker's left is positive in this sense and equals $\iint_S K\,dA$ modulo $2\pi$. This holds whatever the size of $S$: the reversed octant loop on a sphere has $7\pi/2 \equiv -\pi/2$, a turn to the walker's right. Notes state the branch they quote; demos use $(-180^\circ, 180^\circ]$. |

## Derivatives

| Item | Course choice |
| --- | --- |
| Partial derivatives | $\partial_\mu f = \partial f/\partial x^\mu$. When the variables held fixed could be traded (coordinate changes, thermodynamics), write them as a subscript: $(\partial r/\partial x)_y$. |
| Order of repeated derivatives | Operators act right to left: $\partial_\mu\partial_\nu f = \partial_\mu(\partial_\nu f)$ and $\dfrac{\partial^2 f}{\partial x\,\partial y} = \partial_x(\partial_y f)$. |
| Comma and semicolon | Formal and research rungs only. Indices after the comma or semicolon apply left to right: $f_{,\mu\nu} = \partial_\nu\partial_\mu f$ and $V^\rho{}_{;\mu\nu} = \nabla_\nu\nabla_\mu V^\rho$, so $V^\rho{}_{;\nu\mu} - V^\rho{}_{;\mu\nu} = R^\rho{}_{\sigma\mu\nu}V^\sigma$. Name this order wherever it matters. |

## Special relativity, weak fields and orbits

| Item | Course choice |
| --- | --- |
| Speed, Lorentz factor and proper time | $\beta = v/c$ and $\gamma = (1 - v^2/c^2)^{-1/2}$. Proper time is $\tau$, with $d\tau^2 = -ds^2/c^2$ along timelike worldlines. A clock moving at steady speed $v$ in an inertial frame has $d\tau = dt/\gamma$. |
| Frequency | $f$ in hertz at entry and working rungs; angular frequency $\omega = 2\pi f$ at formal rung and in plane waves. $\nu$ is not used for frequency because it is an index. |
| Redshift | $1 + z = \lambda_{\rm r}/\lambda_{\rm e} = f_{\rm e}/f_{\rm r}$, so $z > 0$ is a redshift. The fractional frequency shift is $(f_{\rm r} - f_{\rm e})/f_{\rm e}$, which is negative for light climbing out of a potential well; for small shifts it equals $-z$. |
| Newtonian potential and weak static field | $\Phi = -GM/r$ outside a spherical mass, zero far away. With $x^0 = ct$ the weak static field is $g_{00} = -(1 + 2\Phi/c^2)$, $g_{ij} = (1 - 2\Phi/c^2)\delta_{ij}$. Notes may write $g_{tt}$ for the same dimensionless coefficient of $c^2dt^2$ and say so once. |
| Static redshift factor ("lapse") | In a static spacetime, with Killing vector $\xi$ normalized so $\xi\cdot\xi \to -1$ far away ($c = 1$), $N = \sqrt{-\xi\cdot\xi} = \sqrt{-g_{00}}$ in static coordinates, and static observers find $f_{\rm r}/f_{\rm e} = N_{\rm e}/N_{\rm r}$. Call $N$ the lapse only in static spacetimes, where it equals the lapse of the static slicing. For rotating spacetimes say "Killing norm" or "lapse" explicitly, because they differ. |
| Perihelion advance | $\Delta\phi$ per orbit, in radians inside formulas, positive in the sense of the orbital motion. Observed rates are in arcseconds per Julian century (36 525 days), relative to a non-rotating frame tied to distant quasars unless "equinox of date" is said. |
| Post-Newtonian parameters | Isotropic coordinates, $G = c = 1$: $g_{00} = -1 + 2M/r - 2\beta M^2/r^2$ and $g_{ij} = (1 + 2\gamma M/r)\delta_{ij}$. General relativity has $\beta = \gamma = 1$. Where a Lorentz factor also appears, write $\gamma_{\rm PPN}$. |

## Gravitational waves

| Item | Course choice |
| --- | --- |
| Mass moments | Second mass moment $I_{ij} = \int \rho\, x_i x_j\, d^3x$; trace-free part $Q_{ij} = I_{ij} - \tfrac13\delta_{ij}I_{kk}$. Both give the same transverse-traceless field. Some texts use $\int\rho(3x_ix_j - r^2\delta_{ij})\,d^3x = 3Q_{ij}$, which needs a prefactor three times smaller; record it as a notation trap. In a note that also has electric charge $Q$, write $Q_{ij}$ with its indices every time. |
| Quadrupole formula | $h^{\rm TT}_{ij} = \dfrac{2G}{c^4 r}\,\ddot Q^{\rm TT}_{ij}(t_{\rm r})$ with retarded time $t_{\rm r} = t - r/c$, and radiated power $P = \dfrac{G}{5c^5}\langle \dddot Q_{ij}\dddot Q_{ij}\rangle$. |
| Transverse-traceless projector | $P_{ij} = \delta_{ij} - n_in_j$ and $\Lambda_{ij,kl} = P_{ik}P_{jl} - \tfrac12 P_{ij}P_{kl}$, so $h^{\rm TT}_{ij} = \Lambda_{ij,kl}h_{kl}$. $\mathbf n$ points from the source to the observer. |
| Polarizations | $(\mathbf p, \mathbf q, \mathbf n)$ is a right-handed orthonormal triad. $e^+_{ij} = p_ip_j - q_iq_j$, $e^\times_{ij} = p_iq_j + q_ip_j$, and $h^{\rm TT}_{ij} = h_+e^+_{ij} + h_\times e^\times_{ij}$. For a binary, the inclination $\iota$ is the angle between the orbital angular momentum and $\mathbf n$; a note states its $\mathbf p$ and its phase origin, since they fix the signs of $h_+$ and $h_\times$. |
| Relaxed Einstein equations | $\mathfrak h^{\alpha\beta} = \eta^{\alpha\beta} - \sqrt{-g}\,g^{\alpha\beta}$, harmonic gauge $\partial_\beta\mathfrak h^{\alpha\beta} = 0$, and $\Box\mathfrak h^{\alpha\beta} = -16\pi G\tau^{\alpha\beta}/c^4$ with $\tau^{\alpha\beta} = (-g)(T^{\alpha\beta} + t^{\alpha\beta}_{\rm LL} + t^{\alpha\beta}_{\rm H})$. To first order $\mathfrak h^{\alpha\beta} = \bar h^{\alpha\beta}$, which matches the linearized-gravity row. |

## Black holes and quantum fields

| Item | Course choice |
| --- | --- |
| Surface gravity | $\xi^\nu\nabla_\nu\xi^\mu = \kappa\,\xi^\mu$ on the horizon, where $\xi = \partial_t + \Omega_H\partial_\phi$ generates the horizon and $\partial_t$ is normalized far away. With $G = c = 1$, $\kappa$ has units of inverse length (Schwarzschild: $1/4M$). In SI, $\kappa$ is quoted as an acceleration (Schwarzschild: $c^4/4GM$). |
| Hawking temperature | $k_BT_H = \hbar\kappa/2\pi c$ with $\kappa$ an acceleration; Schwarzschild $k_BT_H = \hbar c^3/8\pi GM$. With $G = c = \hbar = k_B = 1$, $T_H = \kappa/2\pi$. |
| Entropy | Natural logarithm: $S = -k_B\,\mathrm{Tr}(\rho\ln\rho)$, and $S_{\rm BH} = k_Bc^3A/4G\hbar$. With $k_B = 1$ entropies are pure numbers in nats; quote bits only when stated, $S_{\rm bits} = S/(k_B\ln 2)$. |
| Evaporation numbers | Every lifetime or Page time names its emission model: black-body photons only, photons and gravitons with greybody factors, or all particle species. |
| Klein–Gordon inner product | $(f_1, f_2) = i\int_\Sigma(\bar f_1\nabla_\mu f_2 - f_2\nabla_\mu\bar f_1)\,n^\mu\sqrt{h}\,d^3x$ with $n^\mu$ the future-pointing unit normal, so positive-frequency modes $e^{-i\omega t}$ have positive norm. |
| Bogoliubov coefficients | Out-modes in terms of in-modes: $p_\omega = \int d\omega'\,(\alpha_{\omega\omega'}f_{\omega'} + \beta_{\omega\omega'}\bar f_{\omega'})$, so the in-vacuum holds $\langle N_\omega\rangle = \int d\omega'\,|\beta_{\omega\omega'}|^2$ out-quanta. |
| Null infinity | $\mathscr I^+$ (future) and $\mathscr I^-$ (past). |

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
| Spinors, tetrads beyond hatted components, Newman–Penrose, rapidity symbol | Not yet fixed; add them here before writing any note that needs them. |

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
- **Entry vocabulary for geodesics.** At entry depth a geodesic is a *straight walk* (on a surface) or a *straight
  path* (in spacetime); "straight line" is reserved for flat planes. The working rung introduces the word geodesic.
- **Name the frame or basis** when a statement holds only in one, for example "in an orthonormal frame the connection
  one-forms commute in two dimensions".
