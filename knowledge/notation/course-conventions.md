---
type: conventions
status: adopted
decided: 2026-09-12
---

# Course conventions

grbook.ai uses one set of conventions everywhere: prose, equations, demos, narration, and the tutor. When a source
book differs, notes state the difference in a `conventions` entry and translate to these choices. The per-book
crosswalk is built in the notation phase from the dossiers' `notation_and_conventions` entries; do not assume a
book's conventions without checking its dossier.

## Choices

These follow Misner, Thorne and Wheeler (MTW), which matches the legacy course and is widely used in modern texts.

| Item | Course choice |
| --- | --- |
| Metric signature | $(-,+,+,+)$, $\eta_{\mu\nu} = \mathrm{diag}(-1, 1, 1, 1)$ |
| Indices | Greek $\mu, \nu, \dots = 0,1,2,3$ for spacetime; Latin $i, j, \dots = 1,2,3$ for space; Einstein summation |
| Time coordinate | $x^0 = ct$; with $c = 1$, $x^0 = t$ |
| Units | Geometrized $G = c = 1$ inside derivations; every numerical result is restored to SI with the factors shown |
| Four-velocity | $u^\mu = dx^\mu/d\tau$, $u_\mu u^\mu = -1$ (or $-c^2$ in SI) |
| Christoffel symbols | $\Gamma^\lambda{}_{\mu\nu} = \tfrac12 g^{\lambda\sigma}(\partial_\mu g_{\sigma\nu} + \partial_\nu g_{\sigma\mu} - \partial_\sigma g_{\mu\nu})$ |
| Covariant derivative | $\nabla_\mu V^\nu = \partial_\mu V^\nu + \Gamma^\nu{}_{\mu\lambda} V^\lambda$ |
| Riemann tensor | $R^\rho{}_{\sigma\mu\nu} = \partial_\mu \Gamma^\rho{}_{\nu\sigma} - \partial_\nu \Gamma^\rho{}_{\mu\sigma} + \Gamma^\rho{}_{\mu\lambda}\Gamma^\lambda{}_{\nu\sigma} - \Gamma^\rho{}_{\nu\lambda}\Gamma^\lambda{}_{\mu\sigma}$, so $[\nabla_\mu, \nabla_\nu] V^\rho = R^\rho{}_{\sigma\mu\nu} V^\sigma$ (torsion-free) |
| Ricci tensor and scalar | $R_{\mu\nu} = R^\rho{}_{\mu\rho\nu}$, $R = g^{\mu\nu} R_{\mu\nu}$; a sphere of radius $a$ has $R = +2/a^2$ |
| Einstein equation | $G_{\mu\nu} + \Lambda g_{\mu\nu} = \dfrac{8\pi G}{c^4} T_{\mu\nu}$, with $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R\, g_{\mu\nu}$ |
| Geodesic deviation | $\dfrac{D^2 \xi^\mu}{d\tau^2} = -R^\mu{}_{\nu\rho\sigma}\, u^\nu \xi^\rho u^\sigma$ |
| Perfect fluid | $T^{\mu\nu} = (\rho + p)\, u^\mu u^\nu + p\, g^{\mu\nu}$ ($G = c = 1$) |
| Schwarzschild metric | $ds^2 = -(1 - 2M/r)\,dt^2 + (1 - 2M/r)^{-1} dr^2 + r^2 d\Omega^2$ |
| FLRW metric | $ds^2 = -dt^2 + a(t)^2 \left[\dfrac{dr^2}{1 - k r^2} + r^2 d\Omega^2\right]$ |
| Linearized gravity | $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$, $\bar h_{\mu\nu} = h_{\mu\nu} - \tfrac12 \eta_{\mu\nu} h$; Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$ gives $\Box \bar h_{\mu\nu} = -16\pi T_{\mu\nu}$ |

## Practices

- Name the convention when it matters for a sign ("with signature $(-,+,+,+)$, a timelike vector has negative norm").
- Speak equations in words first, then symbols. The tutor never reads raw LaTeX aloud.
- One symbol, one meaning within a lesson. Scope symbols that the sources reuse (for example $K$ for Gaussian
  curvature versus the Kretschmann scalar).
- When quoting a book's result that uses other conventions, translate it and say so in the note.
