---
type: "concept"
schema_version: 2
id: "partial-derivative"
title: "Partial derivative"
tagline: "How something changes when one number it depends on changes and the rest stay fixed"
domain: "mathematical-methods"
tier: "prerequisite"
status: "physics-reviewed"
revision: 5
updated: "2026-09-13"
aliases: ["partial differentiation"]
prerequisites: []
leads_to: ["chain-rule", "gradient", "taylor-series", "jacobian-determinant", "commuting-vector-fields"]
visuals: ["slice-a-hill-along-a-grid-line", "thermometer-on-a-post-and-a-bike"]
---

# Partial derivative

*How something changes when one number it depends on changes and the rest stay fixed*

`partial-derivative` · mathematical-methods · prerequisite · physics-reviewed (revision 5)

**Needs:** nothing beyond everyday experience  
**Opens:** [[chain-rule]] · [[gradient]] · [[taylor-series]] · [[jacobian-determinant]] · [[commuting-vector-fields]]  
**Related:** [[convective-derivative]]  
**Visuals:** ★ [[slice-a-hill-along-a-grid-line]] · [[thermometer-on-a-post-and-a-bike]]

> Stand on a smooth hillside where a straight fence meets a straight hedge at a right angle. Walk parallel to the fence, so that only your distance from the hedge changes. Measure the height you gain per metre over shorter and shorter steps, and the number settles on a slope called a partial derivative. Walking parallel to the hedge gives a second one, and the two can differ: a path can be level while the ground across it is steep.

## You will be able to

**Entry**
- Find the slope for each of the two distances that pin down your place on a hillside. `objectives/find-two-slopes` ← `checks/level-path-on-a-hillside`, `problems/slopes-from-a-height-map`
- Predict how fast the readings of a thermometer on a post and of a moving thermometer change. `objectives/say-what-stays-fixed` ← `checks/rider-heading-to-the-sea`

**Working**
- Compute partial derivatives and use them to estimate small changes. `objectives/compute-partials` ← `checks/cylinder-volume-slopes`, `problems/a-travelling-wave`
- Distinguish partial derivatives that hold different variables fixed. `objectives/track-held-fixed-variables` ← `checks/r-and-x-at-three-four`
- Use mixed partial derivatives to test whether two formulas are slopes of one function. `objectives/test-slopes-with-mixed-partials` ← `checks/slopes-that-fit-no-hill`, `problems/find-the-hill-from-its-slopes`

**Formal**
- State when partial derivatives guarantee continuity and differentiability, with a counterexample. `objectives/state-the-hypotheses` ← `checks/axes-hide-a-jump`

## Ways in

### 1. Walk parallel to a fence on a hill · entry · picture

*How steep is a hillside, when the answer depends on which way you walk?*

Picture a smooth, grassy hillside. A long, straight fence runs across it. A straight hedge meets the fence at a right angle. Two numbers pin down your place on the hill: your distance from the hedge and your distance from the fence. Measure both distances level, the way a map shows them, not along the sloping ground.

Your height above sea level depends on both numbers. So how steep is the ground where you stand? The answer depends on which way you walk.

First, walk parallel to the fence, moving away from the hedge. Your distance from the fence stays the same, and only your distance from the hedge grows. Suppose that over 10 metres, measured level, you climb 2 metres. The ground rises 2 metres for every 10 metres along, or 2 in 10. This number is called a slope.

Now go back to your spot and walk parallel to the hedge, moving away from the fence. This time your distance from the hedge stays the same. Suppose that over 10 metres you go down 1 metre. The slope this way is minus 1 in 10. The minus sign means the ground drops as your distance from the fence grows.

One spot therefore has two slopes, one for each number that pins down your place. Each slope estimates the answer to one question: how much does your height change per metre when one number grows and the other stays fixed? Each slope is only an estimate, because the ground can curve within those 10 metres. The exact answer at your spot is called a partial derivative. Derivative is the mathematicians' word for a rate of change, such as height gained per metre. The word partial means that only part of what pins down your place is changing.

On a curving hill, the slope over 10 metres can differ from the slope over 1 metre. Suppose the ground along your walk curves gently upward. You climb 2 metres over 10 metres, 18.2 centimetres over 1 metre, and 1.802 centimetres over 10 centimetres. Those slopes are 2 in 10, 1.82 in 10 and 1.802 in 10. For example, 18.2 centimetres in 100 centimetres is the same as 1.82 in 10. As the step gets shorter, they settle on 1.8 in 10. On smooth ground the slopes settle like this, and the partial derivative at your spot is the settled number. So the 2 in 10 from your first walk was a close estimate of the partial derivative, not the partial derivative itself.

The two slopes can be very different. Picture a level path cut along a steep hillside, parallel to the fence. The slope along the path is zero, while the ground rises sharply at right angles to the path. So one number cannot say how steep the ground is at a spot. You need a slope for each number that pins down your place.

You meet slopes like this on roads. In many countries, a road sign reading 10 percent warns that the road climbs or drops about 10 metres for every 100 metres along it. That is a slope of 1 in 10. Picture your fence running beside a straight stretch of that road. The road's slope is then one of your two partial derivatives. The hillside's slope across the road can be quite different.

Many quantities depend on several numbers at once. The temperature of the air, for example, depends on where you are and on the time. Partial derivatives describe how such quantities change, one number at a time. The laws of heat, waves and gravity in this course are written with them.

**Try it:** Lay a hardback book on a table, and slide two other books under one of its short edges, so that the cover makes a ramp. With a ruler, measure the height of the cover above the table at the two corners of the raised edge. The heights match, so the slope along the raised edge is zero. Now measure the height at two points 10 centimetres apart on a long edge. For a book 25 centimetres long raised by 5 centimetres, they differ by about 2 centimetres, a slope of about 2 in 10. One spot on the cover has a zero slope one way and a steep slope the other way.

**Takeaway:** A partial derivative is the slope you measure when one of the numbers that pin down your place changes and the others stay fixed.

*Visuals:* [[slice-a-hill-along-a-grid-line]]<br>*See:* `checks/level-path-on-a-hillside`

### 2. What a thermometer on a post measures · entry · operational

*When the temperature depends on both place and time, what does "how fast it rises" mean?*

**Recap:** A partial derivative is the rate at which something changes when one of the numbers it depends on changes and all the others stay fixed. On a hillside, your height depends on two distances, so each spot has two slopes.

On a sunny morning, the temperature of the air depends on two things: where you are, and what time it is. Take a straight road that runs inland from the sea. To keep the numbers simple, suppose two steady rules hold all morning.

First, at any one place, the air warms by 2 degrees Celsius each hour. Second, at any one moment, the air is 1 degree warmer for every 10 kilometres further inland.

A thermometer is bolted to a post beside the road. Its place never changes, so only the time changes. Its reading therefore rises by 2 degrees each hour. That rise is a partial derivative: the change in temperature per hour, with the place fixed. On the hill the step was a metre of ground, and here the step is an hour of time. Weather stations measure temperature in this way, at fixed places.

Now a cyclist carries a second thermometer and rides inland along the road at 20 kilometres per hour. At 9 o'clock she passes the post, and both thermometers show the same temperature. By 10 o'clock the post's reading has risen 2 degrees. The cyclist is then 20 kilometres further inland, which is twice 10 kilometres. At that moment the air around her is 2 degrees warmer than the air at the post. So her reading has risen by 2 plus 2, which is 4 degrees, in that hour.

Both thermometers work perfectly, and at 9 o'clock they even agree. Yet their readings rise at different rates. The post's place stays fixed, while the cyclist's place changes as the time passes. So "how fast does the temperature rise?" has no single answer. You must also say whether the place stays fixed, or how the thermometer moves.

There is a second partial derivative here, with the time fixed instead. Two friends stand at two posts 10 kilometres apart, with watches set to agree. Both read their thermometers at 9 o'clock by their own watches. The thermometer further inland reads 1 degree more. So the temperature changes by 1 degree for every 10 kilometres, with the time fixed.

Many laws of physics, such as the laws of heat and of waves, are written as changes at fixed places, like the post's reading. To predict what a moving thermometer shows, you add the change caused by its motion, as for the cyclist.

**Takeaway:** The rise per hour of a thermometer on a post is a partial derivative, with the place fixed; a thermometer that moves can rise at a different rate.

*What this leaves out:* Real temperatures do not change at steady rates. For them, adding the change at a fixed place and the change caused by the motion works well only over short times and short distances.

*Continues:* `ways_in/walk-one-grid-line-on-a-hill`<br>*Visuals:* [[thermometer-on-a-post-and-a-bike]]<br>*See:* `checks/rider-heading-to-the-sea`

### 3. Freeze the other inputs · working · calculation

*How do you compute a partial derivative, and what does it predict?*

The slopes found in "Walk parallel to a fence on a hill" become exact once the height is a formula and the step shrinks to zero. Call your distance from the hedge $x$ and your distance from the fence $y$, so the height is a function $f(x,y)$, and walking parallel to the fence changes only $x$. For a function $f(x,y)$ of two real variables, the partial derivative with respect to $x$ is defined as

$$\frac{\partial f}{\partial x}(x,y) = \lim_{\Delta x\to 0}\frac{f(x+\Delta x,\,y) - f(x,y)}{\Delta x},$$

with $y$ unchanged throughout; $\partial f/\partial y$ swaps the roles. It is also written $\partial_x f$ or $f_x$, and the curly $\partial$ is read "partial". Geometrically, cut the surface $z = f(x,y)$ with the plane $y = y_0$. The cut is the curve $z = f(x,y_0)$, and $\partial f/\partial x$ is the slope of its tangent line.

Because $y$ is frozen, every rule of one-variable calculus applies with $y$ treated as a constant. For $f = x^2y^3$, $\partial_x f = 2xy^3$ and $\partial_y f = 3x^2y^2$. For a hill of height $z = 120\ \text{m} - x^2/(500\ \text{m}) - y^2/(1000\ \text{m})$, at $x = 50$ m and $y = 200$ m the slopes are $\partial_x z = -x/(250\ \text{m}) = -0.2$ and $\partial_y z = -y/(500\ \text{m}) = -0.4$, in metres of height per metre along.

Together, the partial derivatives predict a small change in all inputs at once. If they are continuous near the point,

$$\Delta f \approx \frac{\partial f}{\partial x}\,\Delta x + \frac{\partial f}{\partial y}\,\Delta y,$$

with an error that shrinks faster than the step, as the derivation "Two small steps, one input at a time" shows. On the hill, a step of $\Delta x = 2$ m and $\Delta y = -1$ m gives $\Delta z \approx -0.4 + 0.4 = 0$, while the exact change is $-9$ mm. The cyclist in "What a thermometer on a post measures" added two effects in this way, and with steady rates the sum is exact. A function of $n$ variables has $n$ first partial derivatives, each holding the other $n-1$ fixed.

**Takeaway:** Differentiate as usual while treating every other variable as a constant; together the partial derivatives predict small changes.

*What this leaves out:* Without continuous partial derivatives the small-change rule can fail; "When partial derivatives are not enough" gives an example.

*Continues:* `ways_in/walk-one-grid-line-on-a-hill`, `ways_in/thermometer-on-a-post`<br>*See:* `derivations/two-small-steps`, `checks/cylinder-volume-slopes`

### 4. Which variables stay fixed? · working · contrast

*Can the same partial derivative have two different values at one point?*

The thermometer on a post and the cyclist's thermometer measured different rates because they kept different things fixed. Formulas hide the same trap. In plane polar coordinates $x = r\cos\theta$ and $y = r\sin\theta$, so $r = \sqrt{x^2+y^2}$. At the point $(3, 4)$, where $r = 5$, ask for $\partial r/\partial x$.

- With $y$ fixed, the point moves parallel to the $x$ axis, and $(\partial r/\partial x)_y = x/r = 0.6$.
- With $\theta$ fixed, the point moves along the ray from the origin, where $r = x/\cos\theta$, and $(\partial r/\partial x)_\theta = 1/\cos\theta = 5/3$.

The subscript names what is held fixed. One function, one point, one variable changed, yet two answers: a partial derivative depends on the whole set of variables in use.

This breaks a one-variable habit. Since $(\partial x/\partial r)_\theta = \cos\theta = 0.6$, it is tempting to call $\partial r/\partial x$ its reciprocal. The reciprocal rule is guaranteed only when both derivatives hold the same variable fixed: $(\partial r/\partial x)_\theta\,(\partial x/\partial r)_\theta = 1$, while $(\partial r/\partial x)_y = 0.6$.

The trap strikes even when the coordinate that varies is the same. Relabel the plane with $u = x$ and $v = y - x$. Holding $v$ fixed while $u$ grows by $\Delta u$ changes both $x$ and $y$ by $\Delta u$, so the small-change rule of "Freeze the other inputs" gives $(\partial f/\partial u)_v = \partial_x f + \partial_y f$. The coordinate $u$ equals $x$, yet $\partial/\partial u \neq \partial/\partial x$, because the other coordinate is different. Relativity changes coordinates constantly, and a derivative with respect to time is defined only once the space coordinates held fixed are named. Thermodynamics meets the same trap: for a gas, heat capacities at fixed volume and at fixed pressure differ.

**Takeaway:** A partial derivative depends on which variables are held fixed, not only on the variable that changes, so name them whenever they could differ.

*Continues:* `ways_in/thermometer-on-a-post`, `ways_in/freeze-the-other-inputs`<br>*See:* `checks/r-and-x-at-three-four`, `observations/speed-of-sound-in-air`

### 5. Mixed partial derivatives agree · working · structure

*Does the order of two partial derivatives matter, and what does the answer let you test?*

Freezing the other inputs, as in "Freeze the other inputs", can be done twice, in either order. Differentiating $f(x,y)$ first with respect to $x$ and then $y$ gives $\partial_y(\partial_x f)$; the other order gives $\partial_x(\partial_y f)$. For $f = x^2y^3$ both equal $6xy^2$. That is no accident. If the second partial derivatives of $f$ are continuous near a point, then there

$$\partial_y(\partial_x f) = \partial_x(\partial_y f).$$

This is Schwarz's theorem, also called Clairaut's theorem, taken on trust here.

The four corners of a small rectangle make it plausible. Form

$$D = f(x+\Delta x,\, y+\Delta y) - f(x+\Delta x,\, y) - f(x,\, y+\Delta y) + f(x,\, y).$$

Grouped as a change across $\Delta y$ at $x + \Delta x$ minus the same change at $x$, $D/(\Delta x\,\Delta y)$ approximates $\partial_x(\partial_y f)$. Grouped as changes across $\Delta x$ at $y + \Delta y$ and at $y$, the same number approximates $\partial_y(\partial_x f)$. Continuity lets both approximations become exact as the rectangle shrinks.

The equality gives a test. If formulas $P(x,y)$ and $Q(x,y)$ are $\partial_x f$ and $\partial_y f$ for one function with continuous second derivatives, then $\partial_y P = \partial_x Q$. For $P = -y$ and $Q = x$ this fails, since $-1 \neq 1$, so no such $f$ exists. For continuously differentiable $P$ and $Q$ on a region with no holes, such as a disc, the test is also sufficient. With a hole it is not: on the plane without the origin, $P = -y/(x^2+y^2)$ and $Q = x/(x^2+y^2)$ pass, and the polar angle has these slopes, but the angle jumps by $2\pi$ once around the origin, so no single-valued $f$ has them.

The same symmetry makes the curl of a gradient vanish, makes the operators $\partial_x$ and $\partial_y$ commute, and is the model for later integrability conditions.

**Takeaway:** For functions with continuous second derivatives the order of partial derivatives does not matter, which tests whether two formulas can be the slopes of one function.

*Continues:* `ways_in/freeze-the-other-inputs`<br>*See:* `key_equations/mixed-partials-commute`, `checks/slopes-that-fit-no-hill`

### 6. When partial derivatives are not enough · formal · structure

*What exactly do partial derivatives guarantee about a function, and what depends on the chart?*

The equality of mixed partial derivatives and the small-change rule both needed continuity, and at this rung the hypotheses are the point. Let $U \subset \mathbb{R}^n$ be open, $f: U \to \mathbb{R}$, and $e_i$ the $i$-th standard basis vector. Then

$$\partial_i f(p) = \frac{d}{dt}f(p + t\,e_i)\Big|_{t=0}$$

is the directional derivative along $e_i$, and $e_i$ is fixed by all the coordinates together. That is why $\partial/\partial u \neq \partial/\partial x$ when $u = x$ but $v = y - x$.

Existence of every $\partial_i f(p)$ does not make $f$ continuous at $p$. For $f = xy/(x^2+y^2)$ with $f(0) = 0$, both partial derivatives vanish at the origin because $f = 0$ on both axes, yet $f = 1/2$ on the rest of the line $y = x$. If the $\partial_i f$ exist near $p$ and are continuous at $p$, then $f$ is differentiable at $p$: $f(p+h) = f(p) + \sum_i \partial_i f(p)\,h^i + o(|h|)$. In particular $C^1$ functions are differentiable.

Schwarz's theorem: if $f \in C^2(U)$, then $\partial_i\partial_j f = \partial_j\partial_i f$ on $U$. Without continuity it can fail. For $f = xy(x^2-y^2)/(x^2+y^2)$ with $f(0) = 0$, one finds $\partial_y(\partial_x f)(0) = -1$ but $\partial_x(\partial_y f)(0) = +1$.

On a manifold with a chart $(x^1, \dots, x^n)$, the operators $\partial/\partial x^i$ at a point are tangent vectors, and Schwarz's theorem says they commute on smooth functions. Each depends on the entire chart, not on the single function $x^i$.

**Takeaway:** Partial derivatives see only the coordinate directions; continuity of the first gives differentiability, continuity of the second makes mixed derivatives commute, and each depends on the whole chart.

*Continues:* `ways_in/mixed-partials-agree`, `ways_in/which-variables-stay-fixed`<br>*See:* `checks/axes-hide-a-jump`

## Glossary

| Term | Say | In plain words | Concept |
| --- | --- | --- | --- |
| slope | — | Height gained per metre moved, measured level. Climbing 2 metres over 10 metres is a slope of 2 in 10; going down gives a minus sign. | — |
| input | — | One of the numbers a quantity depends on. | — |
| partial derivative | — | The rate of change when one number something depends on changes and the others stay fixed, measured over shorter and shorter steps until it settles. | [[partial-derivative]] |

## Key equations

### Definition of the partial derivative · working

$$
\frac{\partial f}{\partial x}(x,y) = \lim_{\Delta x\to 0}\frac{f(x+\Delta x,\,y) - f(x,y)}{\Delta x}
$$

The rate of change of $f$ as $x$ changes with $y$ held fixed.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $f(x,y)$ | a function of two variables | f of x and y |
| $\Delta x$ | a small step in $x$ alone | the step in x |

**Holds when:** The limit must exist; $y$ keeps its value throughout.  
**Say it:** “Partial f by partial x is the limit, as the step in x shrinks to zero, of the change in f divided by the step, with y held fixed.”  
**Justified by:** `stated`

### Small changes from partial derivatives · working

$$
\Delta f \approx \frac{\partial f}{\partial x}\,\Delta x + \frac{\partial f}{\partial y}\,\Delta y
$$

A small change in both inputs changes $f$ by the sum of the two separate effects.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\Delta f$ | the change in $f$ | the change in f |
| $\Delta x,\ \Delta y$ | small steps in the two inputs | the steps in x and y |

**Holds when:** The partial derivatives exist near the point and are continuous at it; the error shrinks faster than the size of the step.  
**Say it:** “The change in f is about partial f by partial x times the step in x, plus partial f by partial y times the step in y.”  
**Justified by:** `derivations/two-small-steps`

### Equality of mixed partial derivatives · working

$$
\partial_y(\partial_x f) = \partial_x(\partial_y f)
$$

Differentiating with respect to $x$ then $y$ gives the same result as $y$ then $x$.

| Symbol | Meaning | Say |
| --- | --- | --- |
| $\partial_y(\partial_x f)$ | the $x$ derivative of $f$, then differentiated with respect to $y$ | partial y of partial x of f |

**Holds when:** The second partial derivatives of $f$ exist and are continuous near the point.  
**Say it:** “Partial y of partial x of f equals partial x of partial y of f.”  
**Justified by:** `stated`

## Derivations

### Two small steps, one input at a time · working

**Goal:** Show that $\Delta f = \partial_x f\,\Delta x + \partial_y f\,\Delta y$ plus terms that shrink faster than the step, when the partial derivatives are continuous near $(x,y)$.

1. Split the change into two moves: $\Delta f = [f(x+\Delta x, y+\Delta y) - f(x, y+\Delta y)] + [f(x, y+\Delta y) - f(x,y)]$.
2. In the first bracket only $x$ changes. The mean value theorem makes it $\partial_x f(x + a\Delta x,\, y+\Delta y)\,\Delta x$ for some $a$ between 0 and 1.
3. In the second bracket only $y$ changes, so it equals $\partial_y f(x,\, y + b\Delta y)\,\Delta y$ for some $b$ between 0 and 1.
4. Continuity of the partial derivatives at $(x,y)$ gives $\partial_x f(x + a\Delta x, y+\Delta y) = \partial_x f(x,y) + \epsilon_1$ and $\partial_y f(x, y + b\Delta y) = \partial_y f(x,y) + \epsilon_2$, with $\epsilon_1, \epsilon_2 \to 0$ as the steps shrink.
5. So $\Delta f = \partial_x f\,\Delta x + \partial_y f\,\Delta y + \epsilon_1\Delta x + \epsilon_2\Delta y$, and the last two terms shrink faster than the step.

**Result:** $\Delta f \approx \partial_x f\,\Delta x + \partial_y f\,\Delta y$, with an error smaller than the step by a factor that tends to zero.

## Problems

### `slopes-from-a-height-map` · entry · difficulty 1 · calculation

On a smooth hillside, a straight fence meets a straight hedge at a right angle. At your spot the ground is 52 metres above sea level. 10 metres away, measured level, walking parallel to the fence and away from the hedge, it is 55 metres. 10 metres away parallel to the hedge, away from the fence, it is 50 metres. Estimate the two slopes. Which walk goes downhill?

**Hints**

1. Divide each change in height by 10 metres.

**Answer:** About 3 in 10 moving away from the hedge, and minus 2 in 10 moving away from the fence, so the walk away from the fence goes downhill.

**Must contain:** 3 in 10 away from the hedge; Minus 2 in 10 away from the fence

**Numeric:** slope moving away from the hedge = 0.3 1 (signed, ±0.02); slope moving away from the fence = -0.2 1 (signed, ±0.02)

**Solution**

1. Away from the hedge, 52 to 55 metres is a climb of 3 metres over 10 metres: a slope of 3 in 10.
2. Away from the fence, 52 to 50 metres is a drop of 2 metres over 10 metres: a slope of minus 2 in 10.
3. On a gently curving hill the partial derivatives are close to these slopes over 10 metres.

### `find-the-hill-from-its-slopes` · working · difficulty 2 · calculation

Show that $P = 2xy + 1$ and $Q = x^2 + 3y^2$ can be $\partial_x f$ and $\partial_y f$ for one function $f$ on the whole plane, find $f$, and check it.

**Hints**

1. Compare $\partial_y P$ with $\partial_x Q$.
2. Integrate $P$ with respect to $x$, adding an unknown function of $y$.

**Answer:** $f = x^2y + x + y^3 + C$ for any constant $C$.

**Must contain:** Both mixed derivatives equal 2x, and the plane has no holes; Integrating P in x leaves an unknown function of y; f equals x squared y plus x plus y cubed plus a constant

**Solution**

1. $\partial_y P = 2x$ and $\partial_x Q = 2x$ agree, and the plane has no holes, so such an $f$ exists.
2. Integrating $P$ with $y$ held fixed gives $f = x^2y + x + g(y)$.
3. Then $\partial_y f = x^2 + g'(y)$ must equal $x^2 + 3y^2$, so $g' = 3y^2$ and $g = y^3 + C$.
4. Check: $\partial_x(x^2y + x + y^3) = 2xy + 1$ and $\partial_y(x^2y + x + y^3) = x^2 + 3y^2$.

**Targets:** `any-slopes-have-a-function`

### `a-travelling-wave` · working · difficulty 1 · calculation

For $f(x,t) = \sin(kx - \omega t)$ with constants $k$ and $\omega$, compute $\partial^2 f/\partial t^2$ and $\partial^2 f/\partial x^2$, and show that $\partial^2 f/\partial t^2 = v^2\,\partial^2 f/\partial x^2$ with $v = \omega/k$.

**Hints**

1. Hold $x$ fixed for the $t$ derivatives, and $t$ fixed for the $x$ derivatives.

**Answer:** $\partial^2 f/\partial t^2 = -\omega^2 f$ and $\partial^2 f/\partial x^2 = -k^2 f$, so $\partial^2 f/\partial t^2 = (\omega/k)^2\,\partial^2 f/\partial x^2$.

**Must contain:** Second t derivative is minus omega squared times f; Second x derivative is minus k squared times f; Their ratio is omega over k, squared

**Solution**

1. With $x$ fixed: $\partial_t f = -\omega\cos(kx - \omega t)$ and $\partial_t^2 f = -\omega^2\sin(kx - \omega t)$.
2. With $t$ fixed: $\partial_x f = k\cos(kx - \omega t)$ and $\partial_x^2 f = -k^2\sin(kx - \omega t)$.
3. Dividing, $\partial_t^2 f = (\omega^2/k^2)\,\partial_x^2 f = v^2\,\partial_x^2 f$.

## Observations

- **The speed of sound in air** (measured, working). The squared speed of sound is a partial derivative of pressure with respect to density, and its value depends on what is held fixed. Holding the temperature fixed gives $p/\rho$ for an ideal gas. A sound wave compresses air too quickly for heat to flow, so the entropy is what stays fixed, giving $\gamma p/\rho$ with $\gamma \approx 1.40$ for dry air. Newton's estimate effectively held the temperature fixed and came out too low; Laplace corrected it in 1816. *Numbers:* At $0\,^\circ\text{C}$: temperature fixed, $\sqrt{RT/M} = 280$ m/s; entropy fixed, $\sqrt{\gamma RT/M} = 331$ m/s; measured, about $331$ m/s. *Reference:* Pierre-Simon Laplace (1816), *Sur la vitesse du son dans l'air et dans l'eau*, Annales de chimie et de physique 3, 238–241

## Teaching arc

1. **Find two slopes at one spot** (entry). Walk parallel to the fence, then the hedge; compare slopes. *Why:* One slope per number, before symbols. *Predict:* If a path along the hillside is level, is the ground level? *Visual:* [[slice-a-hill-along-a-grid-line]] *Uses:* `ways_in/walk-one-grid-line-on-a-hill`, `checks/level-path-on-a-hillside`
2. **Compare a post and a moving thermometer** (entry). Ask for a prediction, then run the post and the cyclist. *Why:* A rate needs what stays fixed. *Predict:* Side by side, do the two readings rise equally fast? *Visual:* [[thermometer-on-a-post-and-a-bike]] *Uses:* `ways_in/thermometer-on-a-post`, `checks/rider-heading-to-the-sea`
3. **Compute, name what is fixed, test** (working). Compute by freezing variables, show one derivative with two values, then test slopes. *Why:* Fluency, then habits that prevent errors. *Predict:* Is partial r by partial x one over partial x by partial r? *Uses:* `ways_in/freeze-the-other-inputs`, `checks/r-and-x-at-three-four`, `checks/slopes-that-fit-no-hill`

## Misconceptions

### “If my path is level where I stand, the ground there is level.” · entry · `level-one-way-means-level`

- **Why it is tempting:** On a floor, level one way means level every way.
- **What is true:** Each direction has its own slope, and the slope across the path can be steep.
- **Exposed by:** `checks/level-path-on-a-hillside`

### “A thermometer on a post and one on a passing bicycle show the temperature rising equally fast.” · entry · `one-rate-for-everyone`

- **Why it is tempting:** As they pass, they read the same.
- **What is true:** The cyclist moves into warmer or cooler air while the post stays put.
- **Exposed by:** `checks/rider-heading-to-the-sea`

### “Partial r by partial x is one over partial x by partial r.” · working · `invert-like-fractions`

- **Why it is tempting:** One-variable derivatives and their inverses are reciprocals.
- **What is true:** Flipping is safe only when both hold the same variable fixed.
- **Exposed by:** `checks/r-and-x-at-three-four`

### “Any two formulas are the x and y partial derivatives of some function.” · working · `any-slopes-have-a-function`

- **Why it is tempting:** In one variable every continuous function is a derivative.
- **What is true:** Slopes of one smooth function must have equal mixed partial derivatives.
- **Exposed by:** `checks/slopes-that-fit-no-hill`

### “If both partial derivatives exist at a point, the function is continuous there.” · formal · `partials-exist-means-smooth`

- **Why it is tempting:** In one variable, a derivative implies continuity.
- **What is true:** Partial derivatives probe only the axes, so the function can jump along other lines.
- **Exposed by:** `checks/axes-hide-a-jump`

## Checks

1. **Entry · predict** `checks/level-path-on-a-hillside`. A level path runs along a smooth hillside. Walking along the path, your height does not change. Walking 10 metres away from the path at a right angle, measured level as on a map, you climb 3 metres. Roughly what are the two slopes where you stand on the path? Is the ground under your feet level?
   - **Hints:** Take each direction separately.
   - **Answer:** Along the path the slope is zero, because your height does not change along it. Away from the path it is about 3 in 10, because you climb 3 metres for every 10. Level ground has zero slope in every direction, and one slope here is not zero, so the ground is not level.
   - **Must contain:** Zero along the path; About 3 in 10 away from it; Not level
   - **Numeric:** slope along the path = 0 1 (signed, ±0.01); slope away from the path = 0.3 1 (signed, ±0.02)
   - **Targets:** `level-one-way-means-level`
   - **Visual:** [[slice-a-hill-along-a-grid-line]]
2. **Entry · predict** `checks/rider-heading-to-the-sea`. A straight road runs inland from the sea. On a sunny morning, the air at every place along it warms steadily by 2 degrees Celsius each hour. At any one moment, the air is 1 degree cooler for every 10 kilometres closer to the sea. At 9 o'clock a cyclist carrying a thermometer passes a thermometer on a post, and both thermometers read the same. She rides toward the sea at 20 kilometres per hour. How much does each reading change by 10 o'clock?
   - **Hints:** How much cooler is air 20 kilometres nearer the sea?
   - **Answer:** The post's reading rises 2 degrees, because its place stays fixed. By 10 o'clock the cyclist is 20 kilometres closer to the sea, twice 10, where the air at that moment is 2 degrees cooler than at the post. So her reading changes by 2 minus 2, which is zero.
   - **Must contain:** Post: up 2 degrees; Cyclist: no change; Only the post's place is fixed
   - **Numeric:** rise of the post's reading = 2 K (signed, ±0.1); rise of the cyclist's reading = 0 K (signed, ±0.1)
   - **Targets:** `one-rate-for-everyone`
   - **Visual:** [[thermometer-on-a-post-and-a-bike]]
3. **Working · numeric** `checks/cylinder-volume-slopes`. A cylinder has radius $R = 0.10$ m, length $L = 0.30$ m and volume $V = \pi R^2 L$. Find $\partial V/\partial R$ and $\partial V/\partial L$, and estimate the volume change when only $R$, or only $L$, grows by 1 mm.
   - **Hints:** Treat $L$ as a constant for the $R$ derivative.
   - **Answer:** With $L$ fixed, $\partial V/\partial R = 2\pi RL = 0.1885$ m², so 1 mm adds about 0.19 litres. With $R$ fixed, $\partial V/\partial L = \pi R^2 = 0.0314$ m², about 0.031 litres.
   - **Must contain:** Two pi R L, 0.1885 square metres; Pi R squared, 0.0314 square metres
   - **Numeric:** partial V by partial R = 0.1885 m^2 (signed, ±1%); partial V by partial L = 0.03142 m^2 (signed, ±1%)
4. **Working · evaluate-claim** `checks/r-and-x-at-three-four`. At $(x, y) = (3, 4)$, a student writes: "$x = r\cos\theta$, so $\partial x/\partial r = \cos\theta = 0.6$, and therefore $\partial r/\partial x = 1/0.6$." Evaluate the claim, and find $\partial r/\partial x$ with $y$ held fixed.
   - **Hints:** Which variable does $\partial x/\partial r = \cos\theta$ hold fixed?
   - **Answer:** The claim mixes two derivatives. $\partial x/\partial r = \cos\theta$ holds $\theta$ fixed, so its reciprocal $5/3$ is $(\partial r/\partial x)_\theta$. With $y$ fixed, $r = \sqrt{x^2+y^2}$ gives $(\partial r/\partial x)_y = x/r = 0.6$.
   - **Must contain:** Partial x by partial r holds theta fixed; With y fixed the answer is 0.6
   - **Numeric:** partial r by partial x at fixed y = 0.6 1 (signed, ±0.01)
   - **Targets:** `invert-like-fractions`
5. **Working · explain** `checks/slopes-that-fit-no-hill`. Is there a function $f(x,y)$ with continuous second partial derivatives and $\partial_x f = -y$, $\partial_y f = x$ everywhere in the plane?
   - **Hints:** Compare the two mixed partial derivatives.
   - **Answer:** No. Such an $f$ would have $\partial_y(\partial_x f) = \partial_x(\partial_y f)$, but $\partial_y(-y) = -1$ while $\partial_x(x) = +1$.
   - **Must contain:** Mixed partial derivatives would disagree
   - **Targets:** `any-slopes-have-a-function`
6. **Formal · explain** `checks/axes-hide-a-jump`. Let $f = xy/(x^2+y^2)$, with $f(0,0) = 0$. Do $\partial_x f$ and $\partial_y f$ exist at the origin? Is $f$ continuous there? What guarantees differentiability?
   - **Hints:** Evaluate $f$ on the axes, then on the line $y = x$.
   - **Answer:** Both are 0, because $f = 0$ on both axes. But $f = 1/2$ on the rest of the line $y = x$, so $f$ is not continuous at the origin. Partial derivatives continuous near a point guarantee differentiability.
   - **Must contain:** Both are zero; One half on the diagonal, so not continuous
   - **Targets:** `partials-exist-means-smooth`

## Notation traps

| Issue | Course choice | Variants you will meet |
| --- | --- | --- |
| What is held fixed often goes unwritten. | Write it as a subscript, $(\partial r/\partial x)_y$, whenever variables could be traded. | Many texts drop it; thermodynamics keeps it. |

## Visuals

- ★ [[slice-a-hill-along-a-grid-line]] (flagship): Shows one slope per input at a spot, and that one zero slope does not make the ground level. *Sketch:* A 3D hill over a square grid with a draggable spot. Two vertical planes through the spot, one per grid direction, cut the hill in two curves, each with its tangent line and a slope readout. The learner shortens the measuring step to watch each slope settle, and loads a hillside with a level path.
- [[thermometer-on-a-post-and-a-bike]] (supporting): Shows that a rate depends on what stays fixed. *Sketch:* A road on a temperature map that warms as a clock runs. A post thermometer and a bicycle thermometer plot readings against time; the learner sets the rider's speed and direction, and the rider's graph goes flat when riding toward the sea at 20 km/h.

## Tutor moves

**Open with**

- A path along a steep hillside is level. Standing on that path, is the ground under your feet level? *(prediction)*

**If the learner is stuck**

- *Cannot treat a variable as a constant.* → Put a number in for the frozen variable, differentiate, then restore the symbol. *Uses:* `ways_in/freeze-the-other-inputs`, `checks/cylinder-volume-slopes`

**Common questions**

- *Why is it called partial?* (entry) Because only part of what pins down your place changes: one of your two distances on the hill, while the other stays fixed. *Uses:* `ways_in/walk-one-grid-line-on-a-hill`

**Switching levels**

- To working when: asks for a formula. Go to the limit definition and the cylinder check. *Uses:* `ways_in/freeze-the-other-inputs`, `checks/cylinder-volume-slopes`
- To formal when: asks whether partial derivatives guarantee smoothness. Show the diagonal jump. *Uses:* `ways_in/when-partials-are-not-enough`, `checks/axes-hide-a-jump`

**Pronunciations:** ∂ → partial; Schwarz → SHVARTS; Clairaut → kleh-ROH

**Voice notes:** At entry say slope, not the symbol.

## Review: novice

**Verdict:** fixed (2026-09-13, revision 5)

**Retell attempt:** On a hill there is a fence and a hedge, and your place is fixed by how far you are from each. If you walk along the fence the ground goes up 2 metres every 10 metres, a slope of 2 in 10, and along the hedge it goes down, minus 1 in 10. Each of those slopes is a partial derivative, and it is called partial because only part of your position changes. I did not get what 'settles on one number' means, why I measure 'level, as a map does', or how I walk along the hedge when I am not standing next to it. I also don't know what a derivative is. With temperature, a thermometer on a post goes up 2 degrees an hour, but a cyclist riding inland goes up 4, because she also moves into warmer air. I did not see why 'different things stay fixed' for her, since nothing seems to stay fixed for her, or why the two effects just add.

**Stumbles (27)**

- “How something changes when you vary one input and hold the others fixed”: The tagline says 'input', but no entry way uses that word; the ways say 'number'. Two words for one idea.
- “only one of the two distances fixing your place changes”: The summary never says what the two distances are measured from, so the reader cannot picture them.
- “Your place on the hill is fixed by two numbers”: 'Fixed' is used in two senses: 'pinned down' here, and 'unchanged' in 'the other stays fixed'. The takeaway, objective and common question repeat it.
- “Measure both distances level, as a map does.”: Reread: 'level, as a map does' is cryptic without the contrast with measuring along the slope.
- “walk alongside the fence, moving away from the hedge”: 'Alongside' suggests walking next to the fence, but your spot is some distance from it; the same problem for 'alongside the hedge'.
- “Your height depends on both numbers.”: Height above what is not said.
- “A slope measured this way is called a partial derivative.”: 'Derivative' is an unfamiliar word and is never explained.
- “how fast does your height change when one number grows”: On a walk, 'how fast' suggests per second, but the slope is per metre.
- “On smooth ground, the measured slope settles on one number as the step gets shorter.”: Reread: 'settles on one number' is abstract, with no numbers the reader can check.
- “a road sign reading 10 percent”: The percent is not connected to the 'in 10' slopes the way uses.
- “A path cut along a steep hillside can be level, while the ground rises sharply at right angles to it.”: It is not said which of the two slopes the path gives, so the link to the fence and hedge is missing.
- “Walk one grid line on a hill”: The way's title speaks of a grid line, but the explanation has only a fence and a hedge.
- “Rest one end of a hardback book on two other books ... The heights differ, so the slope that way is not zero.”: Which end is raised is ambiguous, and the reader is not told how big a difference to expect.
- “When a temperature depends on place and time, what does how fast it rises mean?”: Reread: the embedded question has no quotation marks, so the grammar trips.
- “the air warms by 2 degrees each hour”: Degrees of what scale is not said.
- “That is a partial derivative: the change in temperature per hour”: The hill way made a partial derivative a slope per metre; the jump to a rate per hour is left implicit.
- “Because both rules are steady, the two effects simply add.”: A step taken on trust: why steadiness lets the effects add is not shown.
- “Yet their readings rise at different rates, because different things stay fixed.”: False first what-if: for the cyclist, nothing stays fixed, since both her place and the time change.
- “So the question of how fast the temperature rises has no answer until you say what stays fixed.”: Same problem: for a moving thermometer you name its motion, not something fixed.
- “both at 9 o'clock by the posts' own clocks”: Posts have no clocks, so the measurer of 'the same moment' is unclear, and which post is warmer is not said.
- “A thermometer on a post measures a partial derivative”: A thermometer measures a temperature, not a rate.
- “Then the two effects add correctly only over short times and short distances.”: 'Then' is ambiguous: it could mean 'at that time' or 'in that case'.
- “You stand on a level path along a smooth hillside. Walking 10 metres uphill at right angles to the path”: The starting state does not link the path to the fence of the entry way, 'uphill' gives away the answer, and the answer never says what level ground means.
- “It is also 1 degree cooler for every 10 kilometres closer to the sea. ... The effects are steady, so they add”: 'It' has no clear noun, 'at any one moment' is missing, the road's direction is not given, and the answer uses the same unexplained adding step.
- “At your spot the height is 52 metres ... Which way does the ground drop?”: Height above what is not said, 'alongside' is ambiguous, and 'which way does the ground drop' has several right answers (it also drops toward the hedge).
- “Height gained per step along”: The glossary does not say how the step is measured, or what going down gives.
- “The slopes found by walking one grid line on a hill become exact once the height is a formula”: Ladder jump: the working way starts using x and y without saying which distance each is.

**Fixes**

- Replaced 'fixes your place' with 'pins down your place' in the summary, the hill way, the takeaway, the objective and the common question, so that 'fixed' means only 'unchanged'.
- Replaced 'alongside' with 'parallel to' in the summary, the hill way, the entry problem and the teaching arc.
- Renamed the way 'Walk one grid line on a hill' to 'Walk parallel to a fence on a hill'; its id is unchanged. The working way now names this title and maps the distance from the hedge to x and the distance from the fence to y.
- Hill way: added a worked settling example checked with python (height 0.18s + 0.002s squared gives slopes 0.2, 0.182 and 0.1802 over 10 m, 1 m and 10 cm, tending to 0.18), explained the word derivative, linked 10 percent to 1 in 10, and tied the level path to the fence.
- Try-it: made the ramp doable (books under a short edge) and gave the expected result (a 25 cm book raised 5 cm gives about 2 cm over 10 cm, checked).
- Thermometer way: replaced 'the effects simply add because the rules are steady' with a place-by-place count at 10 o'clock, fixed the false 'different things stay fixed' for the cyclist, gave the time-fixed comparison measurers with agreeing watches, and bridged from metres to hours.
- Rewrote the two entry checks and the entry problem so the starting state is unambiguous, each answer is a chain of because-steps, and the problem's final question has one answer.
- To stay within the tutoring cap of 1,200 and the support cap of 900, trimmed wording in working and formal checks (spoken questions, key points, quantity names), teaching-arc lines, the derivation goal, and the Laplace sentence in the observation. No physics content was removed.
- Bumped the revision to 2 and set the status to novice-reviewed.

**Concerns**

- Budgets are now at their limits: tutoring 1,197 of 1,200, extras 425 of 450, support 887 of 900, and links 197 of 200. The entry explanations total 961 of 1,000 words. Any addition needs a matching cut.
- The summary and the hill way say the partial derivative is the slope over 'a very short step'. The limit itself is left to the working rung, and the entry way scopes 'settling' to smooth ground. The physics reviewer should confirm this wording is honest.
- The obvious what-if of walking diagonally is not addressed at entry. The slope in any direction follows from the two partial derivatives only for smooth ground, through the small-change rule. Adding it would need a reason within two sentences and more budget.
- The proposed visual ids keep 'grid-line' ('slice-a-hill-along-a-grid-line'), while the entry prose now speaks only of a fence and a hedge. When the visual is built, its narration should use fence, hedge and 'parallel to'.
- The writer's reports still stand: there is no conventions row for held-fixed subscripts or the order of mixed derivatives, no ordinary-derivative concept in the registry, and the Laplace 1816 reference is unverified.
- The entry checks give numeric temperature changes in K, as differences of degrees Celsius. This is correct, but a display should say 'degrees'.

**Re-read** (2026-09-13, revision 3): 11 stumbles in 14 changed passages

- “The height you gain per metre, as the step gets very short, settles on a slope called a partial derivative.”: The summary never says what 'the step' is, and the physics edit makes 'the height' the thing that settles on a slope, so the sentence has to be reread.
- “The rate of change, as the step gets very short, when one number something depends on changes and the others stay fixed.”: The glossary entry is read on its own, so 'the step' has no referent, and the inserted clause splits the definition in two.
- “Suppose the ground beside the fence curves gently upward.”: 'Beside the fence' brings back the old 'alongside' problem: your walk runs parallel to the fence, at a distance from it.
- “You climb 2 metres over 10 metres, 18.2 centimetres over 1 metre, and 1.802 centimetres over 10 centimetres. Those slopes are 2 in 10, 1.82 in 10 and 1.802 in 10.”: Step taken on trust: turning 18.2 centimetres over 1 metre into 1.82 in 10 needs a change of units the reader is not shown.
- “A slope like this is called a partial derivative. ... the partial derivative at your spot is the settled number.”: The reader first learns that the 2 in 10 slope is a partial derivative, then that the partial derivative is 1.8 in 10. Is the 2 in 10 a partial derivative or not? The link between the two paragraphs is left to the reader.
- “Lay a hardback book flat on a table”: 'Flat' describes a position here, and the next step tilts the book, so the word seems to be contradicted at once.
- “A partial derivative is how fast something changes when”: 'How fast' suggests per second. The hill way removed it for that reason, but the recap brings it back.
- “For them, adding the two effects works well only over short times and short distances.”: The explanation no longer names 'the two effects', so the reader cannot tell which two are meant.
- “A level path runs along a smooth hillside, like the fence on the hill.”: In the hill way, walking parallel to the fence climbed 2 in 10, so 'like the fence' suggests the fence is level, or makes the reader wonder how a path is like a fence.
- “a cyclist riding toward the sea at 20 kilometres per hour passes a thermometer on a post, and both thermometers read the same. How much does each reading rise by 10 o'clock?”: The cyclist's thermometer is never introduced, so 'both thermometers' has no second noun. 'Rise' also hints at the answer when one reading does not change.
- “Predict how fast a thermometer on a post and a moving thermometer rise.”: Thermometers do not rise; their readings do.
- Fix: Summary and partial-derivative glossary entry: reworded the physics review's 'as the step gets very short' as 'over shorter and shorter steps ... settles', keeping the claim that the partial derivative is the settled value.
- Fix: Hill way: 'beside the fence' became 'along your walk'; added one sentence showing 18.2 cm in 100 cm as 1.82 in 10, and one making explicit that the 2 in 10 over 10 metres is a close estimate of the partial derivative. Entry explanations grew by about 35 words, which stays within the 1,000-word cap.
- Fix: Try-it: removed 'flat' from the resting book.
- Fix: Thermometer way: the recap says 'the rate at which' instead of 'how fast', and simplifies names the two changes that are added.
- Fix: Entry checks: removed the misleading fence comparison from level-path-on-a-hillside; rider-heading-to-the-sea now introduces the cyclist's thermometer and asks how each reading changes. Objective say-what-stays-fixed says 'readings'. Nothing was dropped; the tutoring total stays within its cap.
- Fix: To stay within the tutoring cap of 1,200 after the entry-check wording, shortened the formal level-switch move, which only the tutor sees, from 'Show the function that jumps along the diagonal.' to 'Show the diagonal jump.'
- Fix: The conform-stage diff against f1c17823 was empty, so there was nothing further to read.
- Fix: Not changed: the first sentence, 'A slope like this is called a partial derivative', names the 10-metre slope loosely. The added estimate sentence resolves it without changing its claim. Bumped the revision to 3.

**Re-read** (2026-09-13, revision 5): 1 stumbles in 2 changed passages

- “Each slope estimates the answer to one question: how much does your height change per metre when one number grows and the other stays fixed? The exact answer at your spot is called a partial derivative.”: Step taken on trust: the reader has just measured each slope and is told it only 'estimates' the answer, with no reason. The reason (the ground can curve) arrives four sentences later, in the next paragraph, so the surprise is not backed within two sentences.
- Fix: Hill way: added one sentence giving the reason each 10-metre slope is only an estimate ('because the ground can curve within those 10 metres'). The claim is unchanged: the next paragraph already says the slope over 10 metres can differ from the slope over shorter steps on a curving hill, and 'can' keeps an evenly sloping hill true. The new sentence is 15 words; entry explanations grow by 15 words, past the 1,000 cap but inside the 10% review allowance. Nothing dropped.
- Fix: Check rider-heading-to-the-sea: the reordered question reads cleanly; 'She' is unmistakable and the 9 o'clock passing is now one scene. No stumble, no change.
- Fix: Bumped the revision to 5.

## Review: physics

**Verdict:** fixed (2026-09-13, revision 5)

**Verification**

- Hill way settling example: height 0.18s + 0.002s squared gives 2 m over 10 m, 18.2 cm over 1 m, 1.802 cm over 10 cm, slopes 2, 1.82, 1.802 in 10, settling on 1.8 in 10.: python3 evaluation of h(s) and h(s)/s at s = 10, 1, 0.1 m; limit is the linear coefficient 0.18. → Correct.
- Try-it: a 25 cm book raised 5 cm gives about 2 cm height difference over 10 cm along the long edge, about 2 in 10; zero along the raised edge.: Plane geometry: 10 x 5/25 = 2 cm along the cover; per level distance 2/9.80 = 0.204. → Correct; 'about' covers the 2 percent along-cover versus level difference.
- Thermometer way: T = T0 + 2 t + 0.1 x (degrees C, hours, km inland); post rises 2 per hour, cyclist inland at 20 km/h rises 4, friends 10 km apart differ by 1.: Hand algebra and python: 2 + 0.1 x 20 = 4; linear field so the sum is exact. → Correct.
- Check rider-heading-to-the-sea: toward the sea at 20 km/h, post +2, cyclist 2 - 2 = 0; numeric values 2 and 0 K with abs_tol 0.1.: python3: 2 - 0.1 x 20 = 0; temperature differences in K equal differences in degrees Celsius. → Correct.
- Entry problem slopes-from-a-height-map: 0.3 away from the hedge, -0.2 away from the fence; check level-path-on-a-hillside: 0 and 0.3.: Hand arithmetic (55-52)/10, (50-52)/10, 3/10. → Correct, tolerances sensible.
- Definition of the partial derivative and its geometric reading as the slope of the cut z = f(x, y0).: Standard definition checked against the limit; working-rung stated. → Correct.
- f = x^2 y^3: partial x = 2xy^3, partial y = 3x^2y^2, both mixed partials 6xy^2.: Hand differentiation. → Correct.
- Hill z = 120 - x^2/500 - y^2/1000 at (50, 200): slopes -0.2 and -0.4; step (2, -1) predicts 0 while the exact change is -9 mm.: python3 evaluation of z(52,199) - z(50,200) = -0.009 m and -0.2 x 2 + (-0.4)(-1) = 0. → Correct; the -9 mm is the second-order term -(2 m)^2/(500 m) - (1 m)^2/(1000 m) = -0.008 - 0.001 m.
- Small-change rule and derivation two-small-steps: split into two one-variable moves, mean value theorem, continuity of partials at the point, error (eps1 dx + eps2 dy) is o(|h|).: Re-derived each step; hypotheses (partials exist near the point, continuous at it) match the key equation conditions. → Correct.
- Polar coordinates at (3,4): (dr/dx)_y = x/r = 0.6, (dr/dx)_theta = 1/cos theta = 5/3, (dx/dr)_theta = 0.6, reciprocal rule with the same variable held fixed.: python3 and hand algebra with r = 5. → Correct. 'Holds only when' softened to 'is guaranteed only when' because at theta = 0 the two derivatives coincide by accident.
- u = x, v = y - x: (df/du)_v = partial_x f + partial_y f, so partial/partial u differs from partial/partial x.: Chain rule with x = u, y = u + v. → Correct.
- Four-corner combination D approximates both mixed partials divided by dx dy under either grouping.: Expanded both groupings term by term. → Correct.
- Test P = -y, Q = x fails (-1 vs +1); sufficiency on a region with no holes; angle form P = -y/r^2, Q = x/r^2 passes on the punctured plane and has the polar angle as local potential, which jumps by 2 pi.: Hand derivatives (both mixed partials equal (y^2 - x^2)/r^4) and python finite differences at (0.7, -0.4): -0.78107 both; d atan2/dx = -y/r^2 = 0.61538. → Correct; 'no holes' for an open connected plane region means simply connected, where the Poincare lemma holds.
- Formal way: xy/(x^2+y^2) has zero partials at the origin but equals 1/2 on the line y = x; xy(x^2-y^2)/(x^2+y^2) has partial_y(partial_x f)(0) = -1 and partial_x(partial_y f)(0) = +1.: Hand limits f_x(0,y) = -y, f_y(x,0) = x; python central differences gave -0.999998 and +0.999998; g(0.001,0.001) = 0.5. → Correct, including the order convention partial_y(partial_x f).
- Partials existing near p and continuous at p imply differentiability; C^2 implies Schwarz symmetry; coordinate vector fields commute on smooth functions and depend on the whole chart.: Standard theorems of real analysis and manifold theory. → Correct.
- Problem find-the-hill-from-its-slopes: f = x^2 y + x + y^3 + C.: Differentiated back: 2xy + 1 and x^2 + 3y^2; mixed partials both 2x. → Correct.
- Problem a-travelling-wave: second t derivative -omega^2 f, second x derivative -k^2 f, ratio (omega/k)^2.: Hand differentiation. → Correct.
- Check cylinder-volume-slopes: 2 pi R L = 0.1885 m^2, pi R^2 = 0.03142 m^2; 1 mm gives 0.19 L and 0.031 L.: python3. → Correct; rel_tol 0.01 appropriate.
- Observation: c^2 = (dp/drho) at fixed entropy; isothermal sqrt(RT/M) = 280 m/s and adiabatic sqrt(gamma RT/M) = 331 m/s at 0 C with gamma = 1.40; measured about 331 m/s.: python3 with R = 8.314462618 J/(mol K), T = 273.15 K, M = 0.0289647 kg/mol: 280.0 and 331.3 m/s; ratio sqrt(1.4) = 1.183, Newton's estimate about 15 percent low. → Correct.
- Reference: P.-S. Laplace (1816), 'Sur la vitesse du son dans l'air et dans l'eau', Annales de chimie et de physique 3, 238-241.: WebSearch: French Wikipedia 'Vitesse du son' and an English translation of the paper both give this venue, volume and pages; no DOI exists for this 1816 volume. → Confirmed; verified set true. History scope: Laplace published the adiabatic correction (factor sqrt of cp/cv) in this 1816 paper; 'corrected it in 1816' is accurate.

**Counterexamples tried**

- Fence and hedge meeting at an oblique angle: walking parallel to the fence still keeps the distance from the fence fixed, but height per metre walked is no longer height per metre of distance from the hedge. The summary omitted the right angle; added.
- A sharp ridge or a pointed summit: slopes from the two sides differ and no partial derivative exists. The entry prose scopes settling to smooth ground, so it survives.
- Walking diagonally: the entry prose says one number cannot describe the steepness and a slope is needed for each number; it does not claim the two slopes give every direction, so nothing false. Not addressed at entry (see concerns).
- Non-steady temperature field: the post-plus-motion sum is exact only for steady rates; for smooth real fields it is a good approximation over short times and distances. Simplifies reworded to 'works well only'.
- Water near 4 degrees Celsius: its thermal expansion vanishes, so heat capacities at fixed pressure and fixed volume are equal there. Broke 'heat capacities at fixed volume and at fixed pressure differ'; scoped to a gas.
- Accidental reciprocal at theta = 0: on the positive x axis (dr/dx)_y = 1 = 1/cos 0, so the reciprocal rule is not 'false' whenever held variables differ; reworded to 'guaranteed only when'.
- Punctured plane with the angle form: passes the mixed-partial test but has no single-valued potential; the note already states it.
- xy(x^2-y^2)/(x^2+y^2): mixed partials disagree without continuity; xy/(x^2+y^2): partials exist without continuity. Both stated correctly at formal rung.
- Road grade: a 10 percent sign is rise per horizontal run, differing from rise per distance along the road by 0.5 percent at that grade; the prose says 'about', so it survives.

**Fixes**

- Summary: added 'at a right angle' so that height per metre walked parallel to the fence is the partial derivative, and replaced 'over a very short step, is a slope' with 'as the step gets very short, settles on a slope', matching the settling language of the hill way (a slope over any finite step only approximates the partial derivative).
- Glossary 'partial derivative': 'How much something changes per step, over a very short step' replaced with 'The rate of change, as the step gets very short, ...', since 'per step' is not a rate.
- Thermometer way simplifies: 'works only over short times' to 'works well only over short times', since even short intervals give an approximation.
- Which-variables way: reciprocal rule 'holds only when' to 'is guaranteed only when'; 'the varied coordinate is unchanged' to 'the coordinate that varies is the same'; heat capacities scoped to a gas (water near 4 degrees Celsius has equal heat capacities).
- Misconception invert-like-fractions correction: 'works only' to 'is safe only', for the same accidental-coincidence reason.
- Observation reference verified; status set to physics-reviewed.

**Concerns**

- The notation trap's course_choice (write held-fixed variables as a subscript) and the order convention partial_y(partial_x f) are not rows in the conventions file; an editor should add them.
- The registry has no ordinary-derivative or differentiability concept; the entry rung introduces 'derivative' in passing and the formal rung carries differentiability.
- The diagonal-walk what-if is not covered at entry; directional-derivative exists in the registry but is not linked, because the links budget is at 197 of 200.
- The physics fixes change learner-visible entry text (summary, glossary, simplifies). Revision kept at 2 so both reviews cover the same text; an editor may prefer a quick novice re-read of those sentences.
- The proposed visual ids still say 'grid-line'; the narration of slice-a-hill-along-a-grid-line should use fence, hedge and 'parallel to' and keep the fence at a right angle to the hedge.
- Budgets remain tight; check the validator counts before any addition.

**Diff check** (2026-09-13, revision 3)

- Summary: measuring the height gained per metre over shorter and shorter steps, walking parallel to the fence, settles on a slope called a partial derivative.: Compared with the revision 2 wording ('as the step gets very short, settles on'); tried a sharp ridge, walking back toward the hedge, and an oblique fence. → Same claim, true. The summary already scopes to a smooth hillside with a right angle. Walking toward the hedge gives minus the slope per metre of growing distance, which is still the partial derivative for that direction of measurement, so nothing false.
- Glossary partial-derivative: the rate of change when one number changes and the others stay fixed, measured over shorter and shorter steps until it settles.: Compared with the revision 2 definition; checked that 'settles' matches the hill way's use for the limit. → Same claim as before, true wherever the limit exists; the hill way scopes settling to smooth ground.
- Hill way: on ground along your walk that curves gently upward, 2 m over 10 m, 18.2 cm over 1 m and 1.802 cm over 10 cm give 2, 1.82 and 1.802 in 10, settling on 1.8 in 10; 18.2 cm in 100 cm is 1.82 in 10.: python3 with h(s) = 0.18 s + 0.002 s squared at s = 10, 1, 0.1 and 0.001 m; 18.2/100 = 1.82/10 = 0.182. Checked that upward curving (steepening) ground gives longer-step slopes above the settled value. → Correct: 2.0, 1.82, 1.802, 1.80002 in 10, limit 1.8; the unit conversion is exact; 'along your walk' is the right place for the curving ground.
- Hill way: 'So the 2 in 10 from your first walk was a close estimate of the partial derivative, not the partial derivative itself.': Checked against the curving-ground supposition it follows from: 2 in 10 over 10 m is also the first walk's number, and the settled value at your spot is 1.8 in 10. python3: relative difference (0.2 - 0.18)/0.18 = 11 percent. Tried the what-if of an evenly sloping hillside, where the 10-metre slope equals the partial derivative. → True within its stated scope: the paragraph opens 'On a curving hill' and the sentence follows from 'Suppose the ground along your walk curves gently upward'. An 11 percent overestimate is fairly called a close estimate. On an evenly sloping hillside the sentence would not apply, but the paragraph does not claim that case.
- Try-it: 'Lay a hardback book on a table' with 'flat' removed.: Reread the setup and the measured result. → No change to the geometry; the zero slope along the raised edge and about 2 in 10 along the long edge still hold.
- Thermometer way recap: a partial derivative is the rate at which something changes when one number changes and all the others stay fixed.: Compared with 'how fast something changes when'. → Same claim, true; 'rate' now covers per metre and per hour.
- Thermometer way simplifies: adding the change at a fixed place and the change caused by the motion works well only over short times and short distances, for real temperatures that do not change at steady rates.: python3 with a non-steady field T = 2t + 0.1x + 0.05t squared + 0.01xt (degrees Celsius, hours, km inland) for the rider toward the sea: rate-based sum 2 - 0.1 x 20 = 0, exact change -0.15. Also checked the names against the explanation's final paragraph ('the change caused by its motion'). → True: with changes estimated from rates, the sum is exact for steady rates and only approximate for non-steady ones, and the error shrinks with the interval. The rewording names the same two changes the old 'two effects' meant.
- Objective say-what-stays-fixed: predict how fast the readings of a thermometer on a post and of a moving thermometer change.: Checked that the evidencing check asks for each reading's change in one hour. → Consistent and true.
- Check level-path-on-a-hillside without the fence comparison: along a level path the slope is zero; 10 m away at a right angle, measured level, a 3 m climb gives about 3 in 10; the ground is not level.: Hand arithmetic 3/10; checked that the removed phrase carried no information the answer used, and that a curved level path still has zero slope along its direction at your spot. → Correct; numeric 0 (abs_tol 0.01) and 0.3 (abs_tol 0.02) unchanged and sensible.
- Check rider-heading-to-the-sea as reworded: at 9 o'clock a cyclist carrying a thermometer rides toward the sea at 20 km/h, passes a post thermometer and both read the same; post changes by +2, cyclist by 0 by 10 o'clock.: python3 with T = 2t + 0.1x (x km inland): post T(0,1) - T(0,0) = 2, rider T(-20,1) - T(0,0) = 0. Tried the reading where she passes the post at a later moment: her change from 9 to 10 is still 0 and the post's still 2. Checked that 'change' instead of 'rise' matches signed numeric values 2 and 0 K. → Correct. The sentence order places the passing at 9 o'clock, which the answer's '20 kilometres closer to the sea' step uses; the numeric answers do not depend on it.
- Formal level switch move: 'Show the diagonal jump.': Checked against the formal way and check axes-hide-a-jump: f = xy/(x squared + y squared) is 0 on the axes and 1/2 on the rest of the line y = x. → Accurate shorthand for the tutor.
- Fix: None needed; no learner-visible text changed, and the revision stays at 3.

**Diff check** (2026-09-13, revision 5)

- Hill way: 'Each slope estimates the answer to one question: how much does your height change per metre when one number grows and the other stays fixed?': Checked against the setup: fence and hedge meet at a right angle and distances are measured level, so each metre walked parallel to the fence is one metre of growth in the distance from the hedge while the distance from the fence stays fixed (and likewise for the hedge walk). Checked the sign on the second walk (minus 1 in 10 as distance from the fence grows). Tried the what-if of an evenly sloping hillside. → True. A 10-metre slope is a finite-step estimate of that rate; on an evenly sloping hillside the estimate happens to be exact, which 'estimates' does not deny. The old wording named the 10-metre slope itself as the partial derivative; the new claim is the more accurate one.
- Hill way: 'Each slope is only an estimate, because the ground can curve within those 10 metres.': Checked whether curving is the only reason a forward 10-metre slope can differ from the rate at your spot: if height changes linearly along the walk, the forward difference equals the derivative exactly; python3 with h(s) = 0.18 s + 0.002 s squared gives 2, 1.82, 1.802 in 10 at s = 10, 1, 0.1 m, differing from 1.8 in 10 only through the curving term. → True. Curving along the walk is exactly what makes a finite-step slope differ from the settled value, and 'can' keeps the sentence true on evenly sloping ground. Consistent with the settling paragraph that follows.
- Hill way: 'The exact answer at your spot is called a partial derivative.': Checked scope against a sharp ridge or pointed summit, where the one-sided slopes differ and no exact answer exists; checked consistency with the settling paragraph, the glossary and the summary. → True within its scope: the way opens on a smooth hillside and the next paragraph restates 'On smooth ground the slopes settle like this, and the partial derivative at your spot is the settled number'. Agrees with 'So the 2 in 10 ... was a close estimate of the partial derivative, not the partial derivative itself.'
- Check rider-heading-to-the-sea reordered: at 9 o'clock the cyclist passes the post thermometer with equal readings, and rides toward the sea at 20 km/h; by 10 o'clock the post's reading changes by +2 and hers by 0.: python3 with T = T0 + 2t + 0.1x (degrees Celsius, hours, km inland from the post): post T(0,1) - T(0,0) = 2.0; cyclist T(-20,1) - T(0,0) = 0.0. Checked that the reordering changes no fact, that 'She' refers to the cyclist, that the answer's '20 kilometres closer to the sea' follows from passing the post at 9 o'clock, and that signed numeric values 2 and 0 K with abs_tol 0.1 match (a Celsius difference equals a kelvin difference). → Correct; same claim as before, numeric fields and tolerances sensible.
- Fix: None needed; no learner-visible text changed in this check, and the revision stays at 5.
