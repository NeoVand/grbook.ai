# Units and dimensions

`mechanics-and-gravity/units-and-dimensions` · main track · entry depth · physics-reviewed · revision 2 · 2026-09-22

Teaches: `dimensional-analysis`, `relativistic-units`, `geometrized-units`, `restoring-factors-of-c-and-g`, `natural-units`, `heaviside-lorentz-units`, `astronomical-distance-units`

Builds on: nothing

**Every measurement is a number with a unit. In a true formula, only things of the same kind may be added or set equal, and that test throws out wrong formulas. Physicists then choose units that make the speed of light, and sometimes Newton's constant too, come out as the plain number one. A distance can then be quoted as a time and a mass as a length. Nothing measured changes, because only the units have changed, and the constants can always be put back, in one way only.**

Ask how far the shop is and you may be told twenty minutes. A time has been handed over as an answer about distance, and nobody objects, because we all walk at roughly the same pace. Twenty minutes of walking is about one and a half kilometres. Physicists make the same trade on purpose. They hand over a mass as a length, a distance as a time, and a page of formulas with two famous constants missing from it. This section is about what that trade costs, what it buys, and how to get the constants back.

## Only like adds to like

A measurement is never a bare number. Say the shop is one and a half kilometres away, and you have handed over two things: the number one and a half, and the unit kilometre.

Change the unit and the number changes with it. The same walk is one thousand five hundred metres. The shop did not move.

You change from one unit to another by multiplying by a ratio that is really the number one. One kilometre is one thousand metres, so multiplying by one thousand metres for each kilometre changes the wording and nothing else.

Some measurements cannot be traded this way at all. No ratio turns a number of metres into a number of seconds, because a length and a time are not the same kind of thing. The kind of thing a measurement is, rather than the unit it happens to be quoted in, is called its dimension.

The same word is used elsewhere for the number of directions in a space. This book says directions for that, and keeps dimension for the kind of a measurement.

Three kinds carry everything in this chapter: length, time and mass. A speed is a length divided by a time. An area is a length multiplied by a length.

Electricity brings a fourth kind of its own, charge, which this chapter never needs.

Here is the rule that makes kinds useful. In a true formula, any two things added, subtracted or set equal to each other must be of the same kind. Call it the same-kind rule.

Three kilometres plus two hundred metres is a distance you can walk. Three kilometres plus two seconds is nothing at all.

Testing a formula against the same-kind rule is called dimensional analysis. It takes seconds and it catches a great many mistakes.

It also has a hard limit. Two formulas that differ only by a plain number, such as one half, pass or fail the test together. So surviving the test means only that a formula has not yet been ruled out.

*Every measurement has a kind, called its dimension. In a true formula only things of the same kind may be added or set equal. That test rules formulas out but never proves one right.*

## A distance told as a time

Twenty minutes away is an answer that works only among people who share a pace. A cyclist would call the same shop six minutes away, and a driver three. To trade distances for times in physics, everyone needs one agreed pace.

There is one. Light in empty space travels about three hundred thousand kilometres each second, and every careful measurement gives that same figure, whoever makes it and however fast that person is moving. *The principle of relativity and the speed of light* shows how this was found and why it is so surprising. Here it is a measured fact and nothing more.

So a distance can be quoted as the time light takes to cross it. The distance light covers in one second is called a light-second.

The Moon is about one and three tenths light-seconds from Earth. The Sun is about eight and a third light-minutes away, which is eight minutes and nineteen seconds of light travel.

Quote distances this way and every distance is named by a time. Light's own speed becomes one light-second for each second, which is the plain number one, with no unit left to write after it. Units chosen so that the speed of light comes out as one are called relativistic units.

Every other speed then comes out as a fraction of light's. An airliner at nine hundred kilometres an hour is less than one millionth of it.

That tiny fraction is why daily life never pushes anyone into this choice. Nothing we handle moves fast enough for the gap between its speed and light's to show up in a measurement.

Nothing about the Moon changed when its distance became one and three tenths. The number fell because the unit grew, exactly as one thousand five hundred metres becomes one and a half kilometres.

*Light in empty space gives everyone the same pace, so a distance can be quoted as light travel time. In those relativistic units the speed of light is the plain number one.*

## A mass quoted in kilometres

Gravity brings a fixed number of its own. It is called Newton's constant, and it sets how strong the pull of a given mass is. *Newtonian gravity as a field* writes down the formula it sits in.

In the gravity formulas that also carry the speed of light, a mass never appears on its own. It always comes multiplied by Newton's constant and then divided by the speed of light twice over. Take that pattern on trust here.

That whole combination trades a mass for a length. Feed any mass into it and a length comes out. Call the result the body's gravity length.

The Sun's gravity length is about one and a half kilometres. Earth's is about four and four tenths millimetres.

Earth's radius is more than a thousand million times its own gravity length. That lopsided ratio is the measure of how gentle gravity is at the ground, and it is why the trade never comes up at breakfast.

Now two trades are in hand. The first is the light trade read the other way round: a time is quoted as the distance light covers in it. The second quotes a mass as its gravity length. Make both, and Newton's constant and the speed of light drop out of every formula. They drop out because the two trades have already been made: there is no time and no mass left for the constants to convert. Units handled this way are called geometrized units.

This book writes both constants out in full for a long while yet. It turns to geometrized units only where leaving them in would make the formulas unreadable.

*Newton's constant with two divisions by the speed of light trades a mass for a length, its gravity length. It is about one and a half kilometres for the Sun and four and four tenths millimetres for Earth.*

## Putting the constants back

A formula written in geometrized units looks broken at first sight. For a star that is not spinning, one such formula gives a special distance as twice the star's mass.

By the same-kind rule that cannot be read as it stands. There is a length on one side and a mass on the other. The constants were not deleted, though. They were absorbed into the way the mass is being quoted.

To read the formula in everyday units, undo the trade. Replace the mass by its gravity length, which means multiplying by Newton's constant and dividing twice by the speed of light.

$$r = 2M \quad\longrightarrow\quad r = \frac{2GM}{c^2}$$

Now both sides are lengths and the formula gives a number. For the Sun it comes out at about three kilometres. *The Schwarzschild solution* says what that distance means.

Only one way of putting the constants back is possible. The speed of light is the only trade this book has between times and lengths, and Newton's constant with it is the only trade between masses and lengths. So once you say what kind each side must be, the number of each trade is fixed, and nothing was lost by leaving the constants out.

Multiplying Newton's constant and the speed of light together, however often, never leaves a plain number behind. Using neither of them is the only way to get one. So a second, hidden pair of trades cannot be sitting in the formula.

The recipe is short. Write down the kind each side has to be, apply one trade at a time until the two kinds match, and stop.

The recipe runs backwards just as well. Strip the constants out of a formula in everyday units, and anyone who knows the kinds can put them back.

*A geometrized formula is the same physical claim with the trades left unwritten. The kinds fix exactly how many factors of the speed of light and of Newton's constant put them back.*

## Other trades, other ones

Which constant is worth setting to one depends on what a person studies. The choice is about clutter on the page, never about the physics.

People who study the smallest particles carry a different constant. It links how fast something wiggles to the energy it carries, and it is called Planck's constant.

Setting Planck's constant and the speed of light both to one makes a mass and an energy the same kind. A time then comes out as one divided by a mass. Units chosen that way are called natural units. Newton's constant is left alone there, keeping units of its own. Exactly one length can be built from all three constants, and physicists expect it to mark where gravity and the smallest particles must be described together. The chapter *Quantum effects, quantum gravity and beyond* takes that up.

People who study electricity meet a different clutter. Their everyday formulas carry two fixed numbers that describe empty space, and those two travel through every page.

One rearrangement absorbs both of them into the definitions of charge and of field strength, so neither is ever written again. A factor of four times pi stays behind in the law for the field of a single charge, where it comes from the surface of a sphere. Units chosen that way are called Heaviside-Lorentz units. This book keeps the everyday electrical units instead, so its electrical formulas keep those two numbers.

None of this is visible in the formula itself. A page of symbols does not say which constants its writer set to one, and reading it with the wrong guess is the commonest way to lose a factor. Honest work states the choice before the first formula.

*Different fields set different constants to one: natural units take Planck's constant and the speed of light, Heaviside-Lorentz units the two electrical constants of empty space. A formula never states its own choice.*

## Units the sky forces on you

Astronomers have the opposite problem from clutter. Their numbers are too long to hold in mind. The nearest star beyond the Sun is about forty million million kilometres away.

So they name units after things they already know. The average distance from Earth to the Sun is called the astronomical unit, and it is about one hundred and fifty million kilometres.

For wider gaps they use light travel again. The distance light covers in one year is called a light-year, about nine and a half million million kilometres. It is a distance and not a stretch of time, although the name ends in a time word.

The astronomers' own favourite unit comes from a measurement rather than from a definition. As Earth swings from one side of its yearly path around the Sun to the other, a nearby star appears to shift slightly against the far-off ones behind it. That shift is an angle. Astronomers quote half of it. That half is the angle the astronomical unit covers, measured from the star.

Angles this small are quoted in arcseconds. Cut one degree into three thousand six hundred equal parts and each part is one arcsecond. That is about the angle a coin two centimetres across makes when it is four kilometres away.

Now lay the astronomical unit out at a right angle to your line of sight and walk away from it. The distance at which it covers just one arcsecond is called the parsec.

A parsec works out at about three and a quarter light-years. The name is short for parallax of one arcsecond, so the last syllable is an angle and never a time. The nearest star beyond the Sun is about one and three tenths parsecs away.

*Astronomers name units after the sky. The astronomical unit is the Earth to Sun distance, and a light-year is a distance. A parsec, about three and a quarter light-years, is where the astronomical unit covers one arcsecond.*

## Key equations

**Gravity length of a mass** (stated)

$$\ell = \frac{GM}{c^2}$$

The length that Newton's constant $G$ and two divisions by the speed of light $c$ make out of a mass $M$. That a mass always appears in this combination, in every gravity formula that also carries the speed of light, is taken on trust here.

- $\ell$: gravity length of the body
- $G$: Newton's constant, the fixed number that sets the strength of gravity
- $M$: mass of the body
- $c$: speed of light in empty space

Say: The gravity length equals Newton's constant times the mass, divided by the speed of light times itself.

**A geometrized formula with the constants put back** (derived-here)

$$r = 2M \quad\longrightarrow\quad r = \frac{2GM}{c^2}$$

On the left, a formula in geometrized units sets a distance $r$ equal to twice a star's mass $M$, which breaks the same-kind rule. Replacing the mass by its gravity length makes both sides lengths. For the Sun the restored formula gives about three kilometres.

- $r$: the special distance from the centre of a star that is not spinning
- $M$: mass of the star
- $G$: Newton's constant
- $c$: speed of light in empty space

Say: The special distance equals twice the mass, which in everyday units means two times Newton's constant times the mass, divided by the speed of light times itself.

## Worked examples

**the-suns-three-kilometres.** In geometrized units a formula for a star that is not spinning gives a special distance as $r = 2M$. Put Newton's constant and the speed of light back into it, then work the distance out for the Sun.

1. The left side is a length. On the right, $M$ is a mass, so the two sides are of different kinds and the formula cannot be used as it stands.
2. Newton's constant together with two divisions by the speed of light trades a mass for a length, giving the gravity length.
3. Replacing the mass by its gravity length gives $r = 2GM/c^2$, and now both sides are lengths.
4. The Sun's gravity length is about one and a half kilometres.
5. Twice one and a half kilometres is about three kilometres.

Answer: The restored formula is $r = 2GM/c^2$, which is about three kilometres for the Sun.

*A geometrized formula makes the same physical claim as the everyday one; the trades are simply left unwritten.*

## Checks

**braking-distance-by-kinds** (numeric): A car travelling at 20 metres per second brakes steadily, losing 5 metres per second of speed each second. A student guesses that the distance it needs is the speed divided by the braking rate. Test that guess against the same-kind rule. Then build a formula of the right kind using only the speed and the braking rate, and work out the distance it predicts. The true stopping distance is 40 metres. What does the comparison tell you about the same-kind rule?

Answer: The guess has the wrong kind. A speed is a length divided by a time. The braking rate is a length divided by a time and again by a time. So one divided by the other is a time: 20 divided by 5 is 4 seconds, not a distance. Squaring the speed first repairs the kind, because a speed squared divided by the braking rate leaves a length. That formula gives 400 divided by 5, which is 80 metres. The true answer is 40 metres. So the same-kind rule got the shape of the formula right and missed the one half in front of it. Matching kinds is a filter, not a proof.

Key points: Speed divided by braking rate is a time, 4 seconds, so the guess fails the same-kind rule; Speed squared divided by braking rate is a length and gives 80 metres; The true 40 metres differs by a factor of one half, which no test of kinds can supply

Numeric: distance predicted by the formula built from kinds = 80 m; time given by the student's guess = 4 s

**the-moon-in-light-seconds** (numeric): The Moon is about 384,000 kilometres from Earth, and light covers about 300,000 kilometres each second. How long does light take to cross that gap, and what is the Moon's distance in light-seconds? A friend says that quoting the distance this way makes the Moon closer, because 1.3 is a much smaller number than 384,000. What is your reply?

Answer: Light takes about 1.3 seconds, because 384,000 divided by 300,000 is about 1.28. So the Moon is about 1.3 light-seconds away. The friend is wrong: the number fell because the unit grew. One light-second is 300,000 kilometres, so 1.3 light-seconds is the same gap as 384,000 kilometres. One and a half kilometres is the same walk as one thousand five hundred metres, in exactly the same way. A radar flash sent to the Moon and back still takes about 2.6 seconds on the clock, whichever unit anyone writes the distance in.

Key points: 384,000 divided by 300,000 is about 1.28, so the crossing takes about 1.3 seconds and the distance is about 1.3 light-seconds; The number fell because the unit grew; one light-second is 300,000 kilometres; The timed radar flash reads the same whatever unit the distance is quoted in

Numeric: light travel time from Earth to the Moon = 1.28 s

**earths-special-distance** (numeric): Earth's gravity length is about 4.4 millimetres. Use the geometrized formula that gives a special distance as twice the mass, with the constants put back, to find that distance for Earth in millimetres. A friend then says that Earth's mass simply is 4.4 millimetres, so mass and distance are the same thing after all. What is wrong with that?

Answer: Twice 4.4 millimetres is about 8.8 millimetres. The friend is wrong. The gravity length is what comes out after a fixed trade. That trade is the mass multiplied by Newton's constant and divided twice by the speed of light. It can be undone at any time. A balance in a shop still reads kilograms. Writing a mass as a length is only a way of quoting it, like a price given in a second currency.

Key points: Twice 4.4 millimetres is about 8.8 millimetres; The gravity length is the mass after a fixed trade, and the trade can be undone; Kilograms and metres are still different kinds; only the way of quoting changed

Numeric: Earth's special distance = 0.0088 m

**two-names-that-end-in-time-words** (explain): Two sentences from a magazine: "the journey took four light-years" and "the star is two parsecs away, so its light reaches us two seconds after it leaves". Say what has gone wrong in each sentence, and give the star's distance in light-years and the time its light really takes.

Answer: A light-year is a distance. It is how far light travels in one year. So a journey cannot take four of them. It can cover four of them, and light itself needs four years to do that. In the second sentence the last syllable of parsec is not a second of time. It is an arcsecond, an angle one three thousand six hundredth of a degree wide. A parsec is about three and a quarter light-years. So two parsecs is about 6.5 light-years, and the star's light takes about 6.5 years to reach us.

Key points: A light-year measures distance, not elapsed time, so a journey covers light-years rather than taking them; The sec in parsec is an arcsecond, an angle, not a second of time; Two parsecs is about 6.5 light-years, so the light takes about 6.5 years

Numeric: time the star's light takes to reach us = 6.5 yr

## Misconceptions

- **setting-c-to-one-changes-physics**: "Setting the speed of light to one slows light down, or changes what the theory predicts." — It changes only the unit used for distance, so every stopwatch and tape reading stays the same. The constants can always be put back, and in only one way. (diagnosed by the-moon-in-light-seconds)
- **matching-units-proves-formula**: "If the units match on both sides, the formula must be right." — Matching kinds rules formulas out, it does not prove them right. Two formulas that differ by a plain number, such as one half, pass the test together. (diagnosed by braking-distance-by-kinds)
- **mass-really-is-a-length**: "In geometrized units a star's mass really is a distance, so mass and length are the same kind of thing." — The gravity length is the mass after a fixed trade, and the trade can be undone at any time. A balance still reads kilograms. (diagnosed by earths-special-distance)
- **light-year-is-a-time**: "A light-year is a long stretch of time, because its name ends in a time word." — A light-year is a distance: how far light travels in one year. A journey covers light-years rather than taking them. (diagnosed by two-names-that-end-in-time-words)
- **parsec-is-a-time**: "The sec in parsec is a second of time, so a parsec is a short waiting time." — It is an arcsecond, an angle one three thousand six hundredth of a degree wide. A parsec is a distance of about three and a quarter light-years. (diagnosed by two-names-that-end-in-time-words)

## Glossary

- **dimension**: The kind of thing a measurement is, such as a length, a time or a mass, regardless of the unit it is quoted in. This book says directions for the other meaning of the word. (`dimensional-analysis`)
- **same-kind rule**: In a true formula, any two things added, subtracted or set equal to each other must be of the same kind. (`dimensional-analysis`)
- **dimensional analysis**: Testing a formula by checking that every term obeys the same-kind rule. It rules wrong formulas out but never proves one right. (`dimensional-analysis`)
- **light-second**: The distance light covers in one second in empty space, about three hundred thousand kilometres. (`relativistic-units`)
- **relativistic units**: Units in which distances are quoted as light travel times, so the speed of light comes out as the plain number one and every speed is a fraction of it. (`relativistic-units`)
- **Newton's constant**: The fixed number that sets how strong the pull of a given mass is. It appears in every formula about gravity.
- **gravity length**: The length a mass becomes when it is multiplied by Newton's constant and divided twice by the speed of light: about one and a half kilometres for the Sun. (`geometrized-units`)
- **geometrized units**: Units in which times are quoted as light travel distances and masses as gravity lengths, so that Newton's constant and the speed of light drop out of the formulas. (`geometrized-units`)
- **putting the constants back**: Recovering Newton's constant and the speed of light in a formula written without them, by applying the trades until both sides are of the same kind. (`restoring-factors-of-c-and-g`)
- **natural units**: Units in which Planck's constant and the speed of light are both set to one, used by people who study the smallest particles. Newton's constant keeps units of its own there. (`natural-units`)
- **Heaviside-Lorentz units**: Electrical units that absorb the two constants of empty space into the definitions of charge and field strength. A factor of four times pi is left behind in the law for the field of a single charge. (`heaviside-lorentz-units`)
- **astronomical unit**: The average distance from Earth to the Sun, about one hundred and fifty million kilometres. (`astronomical-distance-units`)
- **light-year**: The distance light covers in one year, about nine and a half million million kilometres. It is a distance, not a stretch of time. (`astronomical-distance-units`)
- **arcsecond**: One of the three thousand six hundred equal parts a degree can be cut into. It is about the angle a coin two centimetres across makes when it is four kilometres away. (`astronomical-distance-units`)
- **parsec**: The distance from which the astronomical unit, laid at a right angle to the line of sight, covers one arcsecond: about three and a quarter light-years. (`astronomical-distance-units`)

## Visuals

- `one-distance-on-four-rulers` (flagship): The same gap read by four rulers at once, so the number moves while the gap does not: the picture behind every unit change in this section. Sketch: A single drawn gap with four rulers beneath it, marked in metres, kilometres, light-seconds and light-minutes. Dragging either end moves all four readouts together while the drawn gap keeps its length. Presets: the walk to the shop, Earth to the Moon, Earth to the Sun, Earth to the nearest star, each with a stopwatch for the light travel time. No preset changes the drawn gap, so the belief that light slows when the ruler changes never gets a picture to stand on.
- `mass-dial-with-a-gravity-length` (core): A mass turned into its gravity length and back, beside the body's real size, so the trade is visibly a quoting choice and visibly tiny for everyday bodies. Sketch: A dial runs from a person through Earth, the Sun and a heavy star to a galaxy's central black hole. Two bars drawn to one scale give the body's radius and its gravity length, with readouts for the mass in kilograms and the ratio between the bars. A reverse switch feeds a length in and returns kilograms, so the trade visibly runs both ways.
- `parallax-wobble-and-the-parsec` (supporting): Where the parsec comes from: Earth swinging from side to side, a near star shifting against the far ones, and the angle read in arcseconds. Sketch: Earth circles the Sun while a near star is seen against a fixed far-off field. A gauge reads the half-swing angle in arcseconds and the distance in parsecs and light-years, the two locked together. A slider drags the star from half a parsec out to fifty parsecs, and the shift shrinks to nothing. A side panel holds a two-centimetre coin at four kilometres as the one-arcsecond reference.

## Tutor

Opening question: Someone tells you the shop is twenty minutes away. That is a time, offered as an answer about distance, and nobody objects. Why does that work between the two of you? And what would have to be agreed before a physicist could answer the same way about the Moon?

- Q: If the speed of light is one, does that not make light slow? A: No. The one is one light-second of distance for each second of time. A light-second is about three hundred thousand kilometres, so the pace is exactly what it always was. Only the unit used for the distance changed. Bounce a radar flash off the Moon and the stopwatch still reads about two and six tenths seconds for the trip out and back, whichever unit you write the distance in.
- Q: How can anyone measure a mass in kilometres? A: By quoting it after a fixed trade. Multiply a mass by Newton's constant and divide twice by the speed of light, and what comes out is a length, called the body's gravity length. For the Sun it is about one and a half kilometres, and for Earth about four and four tenths millimetres. The trade can be undone whenever you like, so a balance in a shop still reads kilograms.

## Review: novice

Verdict fixed (2026-09-22, revision 2)

Retell attempt: A measurement is a number plus a unit, and the kind of thing it measures is its dimension: length, time or mass. You can only add or equate things of the same kind, which is the same-kind rule, and checking a formula with it is dimensional analysis. It throws out wrong formulas but cannot find plain numbers like one half, so a car stopping from twenty metres per second comes out at eighty metres by kinds when the truth is forty. Light in empty space goes three hundred thousand kilometres a second for everybody, so a distance can be quoted as light travel time: the Moon is one and three tenths light-seconds, the Sun eight and a third light-minutes, and in those relativistic units the speed of light is just one. Gravity brings Newton's constant, and a mass times it divided twice by the speed of light is a length, the gravity length: one and a half kilometres for the Sun. Do both trades and the two constants vanish from the page, which is geometrized units, and a formula like distance equals twice the mass is put right by writing two G M over c squared, about three kilometres for the Sun. Particle people set Planck's constant to one instead, electricity people absorb two constants of empty space, and astronomers use the astronomical unit, the light-year, which is a distance, and the parsec, about three and a quarter light-years, from a one-arcsecond parallax. Things I could not say back after one reading: why gravity formulas always carry the mass in that one combination, why only one way of putting the constants back exists, what the Sun's three kilometres is the distance to, and whether a mass has really become a length or only been renamed.

12 stumbles

- “It is the plain number one, with no unit left to write after it.”: One light-second for each second still looks like a distance over a time, so why the unit disappears is left implicit.
- “It always comes multiplied by Newton's constant and divided twice by the speed of light.”: Divided twice by reads as one division repeated on paper; nothing says it is a division by the speed of light and then by it again.
- “Quote times as light travel distances and masses as gravity lengths”: The earlier part traded a distance for a time, and this trades a time for a distance; nothing says it is the same trade turned round, so it reads as a third trade.
- “They drop out because every place where they could have appeared has already been used up.”: Used up is vague: what was used up, and by whom?
- “Earth's is about four and a half millimetres.”: The check and the prose give two different numbers for the same length, four point four and four and a half, and the check then doubles one and quotes the other.
- “Twice 4.4 millimetres is about 8.9 millimetres.”: Arithmetic a reader does in their head disagrees with the page: twice four point four is eight point eight.
- “Time a radar flash out to the Moon and the stopwatch still reads about one and three tenths seconds”: A rule that cannot be followed: one stopwatch on Earth cannot time a one-way flash, and the check in the same section times two and six tenths seconds for the round trip.
- “Only one way of putting the constants back is possible.”: A surprising claim with no test behind it; the reader wants to know why an extra pair of constants cannot hide.
- “That shift is an angle.”: The swing goes from one side of Earth's path to the other, but the parsec uses the astronomical unit, which is half of it; the step from one to the other is missing.
- “Three kinds carry everything in this chapter: length, time and mass.”: Two parts later the section talks about charge and field strength, which are none of the three, so the first what-if breaks the sentence.
- “One degree cut into three thousand six hundred equal parts.”: The glossary defines the cutting, not the angle the word names.
- “*Relativity and light* shows how this was found”: No section by that name exists; the outline calls it The principle of relativity and the speed of light, so the reader cannot find it.

Fixes:
- Summary: the false because (nothing measured changes because restoration is unique) replaced by only the units have changed, with uniqueness kept as a separate clause.
- Part distance-told-as-a-time: every distance is named by a time added before the plain number one; the forward reference now uses the outline title of the relativity section.
- Part a-mass-quoted-in-kilometres: divided by the speed of light twice over; the two trades named one at a time; used up replaced by no time and no mass is left to convert; Earth's gravity length made four and four tenths millimetres in prose and takeaway.
- Part putting-the-constants-back: two sentences added giving the reason no hidden pair of trades can exist.
- Part units-the-sky-forces-on-you: the half swing named as the angle the astronomical unit covers, measured from the star.
- Part only-like-adds-to-like: charge named as a fourth kind the chapter never needs.
- Check earths-special-distance: answer, key point and numeric value corrected to 8.8 millimetres.
- Tutor: the one-way radar timing replaced by a round trip of two and six tenths seconds; Earth's gravity length made consistent.
- Glossary: arcsecond defined as one of the parts, not as the cutting.

Concerns:
- Two coinages are load-bearing and are not in course-conventions.md: gravity length for G M over c squared and same-kind rule for the dimensional test. Both are good at this depth, but they must be adopted centrally before gravity-as-curvature, falling-in or The Schwarzschild solution reuse them.
- The section's own disambiguation of dimension (directions for the number of directions in a space) is also not a fixed convention yet; other entry sections will collide with it.
- The reader still leaves not knowing what the Sun's three kilometres is the distance to, by design; the pointer to The Schwarzschild solution is the only payment, and that section is at working depth.
- Prose is now about 2,100 words against a 2,500 cap and the whole section about 4,500 against 5,000, so the review allowance was not needed and nothing was compressed.

## Review: physics

Verdict fixed (2026-09-22, revision 2)

17 verification items, 7 counterexamples

- The gravity length of the Sun is about one and a half kilometres and of Earth about four and four tenths millimetres.: 1.4766 km and 4.435 mm; the prose figures are right, and the earlier four and a half millimetres was replaced by four and four tenths to match the check.
- The restored formula r = 2 G M over c squared gives about three kilometres for the Sun and about 8.8 millimetres for Earth.: correct; the check's stated 8.9 millimetres was an arithmetic slip against its own 4.4 and is now 8.8, with the numeric target set to 0.0088 metres and a five per cent tolerance that still covers the exact 8.870.
- Putting the constants back can be done in only one way.: true; no non-trivial dimensionless combination of G and c exists, so the restoration is unique once each side's kind is fixed. The section now states this reason instead of asserting the result.
- In gravity formulas a mass never appears on its own, always as G M over c squared.: scoped to the gravity formulas of relativity that this book writes down, where the geometrized mass G M over c squared is the combination that appears; the key equation's meaning carries the same scope.
- Setting Planck's constant and the speed of light to one makes masses, energies and times one kind.: false as written; replaced by a mass and an energy are the same kind, and a time comes out as one divided by a mass.
- Exactly one length can be built from Newton's constant, Planck's constant and the speed of light.: true; the further claim that this length marks where gravity and the smallest particles meet is an expectation, so the prose now says physicists expect it and points to The Planck scale and quantum fields in curved spacetime.
- Heaviside-Lorentz units absorb the two constants of empty space and leave a factor of four times pi in the law for a single charge.: true; wording sharpened to the law for the field of a single charge, since a law for a single charge was ambiguous between the force law and the field.
- Three kinds carry everything in this chapter: length, time and mass.: scoped by naming charge as a fourth kind this chapter never needs.
- Light takes about 1.28 seconds to cross to the Moon, and a radar round trip takes about 2.6 seconds.: correct; the tutor's one-way stopwatch was not a doable measurement and now times the round trip at two and six tenths seconds.
- The Sun is eight and a third light-minutes away, or eight minutes and nineteen seconds of light travel.: correct.
- A light-year is about nine and a half million million kilometres; a parsec is about three and a quarter light-years; the nearest star beyond the Sun is about forty million million kilometres, or one and three tenths parsecs; two parsecs is about 6.5 light-years.: all correct.
- A parsec is the distance at which the astronomical unit covers one arcsecond, and one arcsecond is about a two-centimetre coin at four kilometres.: correct; the prose now says astronomers quote half the yearly shift, which is the angle the astronomical unit covers measured from the star, so the parsec's angle is the parallax and not the full swing.
- Braking check: the guess gives 4 seconds, the kind-correct formula 80 metres, the truth 40 metres.: correct, and the factor missed is exactly the one half, which is what the check claims.
- An airliner at nine hundred kilometres an hour is less than one millionth of the speed of light, and Earth's radius is more than a thousand million times its gravity length.: both correct.
- Key equation gravity length, l = G M over c squared, in course conventions.: consistent; no sign, factor of two or pi issue. The second key equation is derived in the section and the first is marked stated, which the prose says.
- Forward references name real sections.: three correct; Relativity and light was not the section's title and was replaced by the outline title.
- Structure: teaches matches the outline, every concept is named in a part, checks and misconceptions link both ways, builds_on is empty.: correct; no source book is named or quoted anywhere, and further is empty, so no reference needed verifying.

Fixes:
- Part a-mass-quoted-in-kilometres and the gravity-length equation's meaning: the mass-appears-only-as-G-M-over-c-squared claim scoped to the gravity formulas of relativity that this book writes down.
- Part other-trades-other-ones: natural units now say a mass and an energy are the same kind and a time is one divided by a mass; the Planck length is stated as the unique length from the three constants, its meaning marked as an expectation and pointed to The Planck scale and quantum fields in curved spacetime.
- Part other-trades-other-ones: four times pi placed in the law for the field of a single charge.
- Part putting-the-constants-back: uniqueness given its reason, that no product of Newton's constant and the speed of light is a plain number.
- Part only-like-adds-to-like: charge named as a fourth kind, scoping the three kinds sentence.
- Part units-the-sky-forces-on-you: the parallax angle identified as half the yearly shift, the angle the astronomical unit covers measured from the star.
- Check earths-special-distance: 8.9 corrected to 8.8 millimetres in answer, key point and numeric value.
- Tutor: one-way radar timing replaced by the two and six tenths second round trip, matching the check.
- Part distance-told-as-a-time: forward reference corrected to the outline title of the relativity section.
- Wording of the physics fixes themselves re-read as the learner and simplified; the claims are unchanged (see review.novice.rereads).

Concerns:
- Ordering debt: geometrized-units and restoring-factors-of-c-and-g need Newton's constant, but newtonian-gravity-as-a-field is the fifth section of this chapter. The section flags the debt in the prose and points forward, but either the outline should move this section after newtonian-gravity-as-a-field, or that section should pay the debt back explicitly.
- Fit: heaviside-lorentz-units needs field laws the reader has not met and natural-units needs Planck's constant, so both can only be named here and neither is gradable by a check. They belong at electromagnetism-as-a-tensor-theory and the-planck-scale-and-quantum-fields respectively; kept here because the outline assigns them.
- Missing conventions, to be adopted in course-conventions.md before other sections reuse them: gravity length for G M over c squared, same-kind rule for the dimensional test, the dimension against directions disambiguation, and how entry sections should name unit systems the course never uses.
- The astronomical unit is described as the average Earth to Sun distance, which is its historical sense; it is now a defined length of 149,597,870,700 metres. The entry wording is kept, and a working-depth section should state the defined value.
- The writer's fourth visual, putting-the-constants-back, a one-trade-at-a-time drill on a geometrized formula, is still the best home for the uniqueness claim and should be built even though the prose now carries the reason.
