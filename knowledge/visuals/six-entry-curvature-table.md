---
type: "visual"
schema_version: 2
id: "six-entry-curvature-table"
title: "Six-entry curvature table"
kind: "interactive-2d"
priority: "flagship"
status: "proposed"
revision: 2
rungs: ["working", "formal"]
serves: ["ricci-tensor", "ricci-scalar", "einstein-tensor", "ricci-flat-spacetime", "einstein-space", "weyl-tensor", "kretschmann-scalar"]
builds_on: ["four-legs-around-a-tiny-loop", "falling-ring-of-crumbs"]
leads_to: ["cube-of-small-loops", "three-gauges-on-a-falling-probe", "circles-behind-a-see-through-star"]
---

# Six-entry curvature table

`six-entry-curvature-table` · interactive-2d · flagship · proposed · rungs: working, formal

> Curvature at one place and moment, written as six numbers, with a switch that lights the numbers each reading adds up.

## What it makes visible

Curvature at one event, in one freely falling observer's orthonormal frame, laid out as six numbers: one for each pair of frame axes. Selecting a readout lights the cells it adds and shows the sign each cell enters with. The Ricci reading adds the three cells that pair the time axis with a space axis; the observer's own Einstein reading adds the three that leave the time axis out, so the tides cancel from it entirely. The same six cells make the Ricci scalar, the Weyl remainder and the Kretschmann scalar, so a learner can hold every trace-and-remainder statement of the chapter in one picture: outside a star every Ricci readout is zero while no cell is, an expanding universe has a zero Weyl table, and one table can be an Einstein space without having constant curvature.

## The picture

A four-by-four grid fills the panel, its rows and columns labelled with the observer's four frame axes. The six cells above the diagonal carry the numbers; each is a slider with a large numeral. Cells that pair the time axis with a space axis have a blue border; cells that pair two space axes have a green border. A positive number sits on an orange fill with a plus badge, a negative number on a violet fill with a minus badge, and the fill deepens with size. The diagonal cells are grey and hatched, because a plane needs two different directions. The cells under the diagonal are faint mirror copies. A readout strip runs under the grid; selecting one readout draws a thick yellow ring around the cells it adds and prints the sign each cell enters with on the ring. A second, smaller grid with a dashed border appears beside the first when the Weyl table is asked for.

| Element | Shows |
| --- | --- |
| Four-by-four grid with frame axis labels | the planes an observer can pick out at one event, one cell per pair of axes |
| Blue-bordered cells in the time row | the three tidal entries a gradiometer reads |
| Green-bordered cells among the space axes | the three space-plane entries a ring test reads |
| Grey hatched cells on the diagonal | pairs that name no plane, so they hold nothing |
| Thick yellow ring with plus and minus badges | which cells a chosen readout adds, and with which sign |
| Dashed second grid | the Weyl table: the same six cells with their trace parts taken out |
| Readout strip | the Ricci components, the Ricci scalar, the Einstein components, the Einstein mismatch and the invariants |

## Book figure

Two panels sharing one filled table, the curvature outside a spherical mass in units of the tidal scale: the time row reads minus two, plus one, plus one and the space planes read plus two, minus one, minus one. Left panel: the three blue time cells are ringed with their plus signs and the Ricci readout under them reads zero. Right panel: the three green space cells are ringed and the Einstein readout under them reads zero, while the Kretschmann readout reads forty-eight. A caption line states that no cell is zero.

Labels: time, toward the centre, across, Ricci reading, Einstein reading, Kretschmann scalar, zero, forty-eight. Aspect 2:1. Alt text: One six-number curvature table shown twice. In the first copy the three time cells are ringed and their total reads zero. In the second the three space-plane cells are ringed and their total also reads zero, while no cell in the table is zero.

## Variants

- **static** `static-card` (fallback): The print figure as an SVG card: the star-exterior table with both readings ringed and both totals zero.
- **interactive-2d** `full-table`: The full widget: six sliders, source presets, readout highlighting, the Weyl table and the invariant readouts.
- **plot** `fall-off-plot`: A companion plot for the star exterior: each cell and the Kretschmann scalar against distance, on logarithmic axes, showing the inverse cube and the inverse sixth power.

## Parameters

| Id | Label | Type | Options or range | Default | Available when | Effect |
| --- | --- | --- | --- | --- | --- | --- |
| `source` | Where the numbers come from | enum | table, schwarzschild, vacuum-family, expanding-universe, constant-curvature, two-factor | "table" | — | Chooses whether the six entries are typed in or filled from a closed formula. Every source fills the same six cells, so the readouts never change their meaning. |
| `r-01` | Time and x plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat0\hat1\hat0\hat1}$, the tidal entry along the first space axis, in the table's own curvature unit. |
| `r-02` | Time and y plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat0\hat2\hat0\hat2}$, the tidal entry along the second space axis. |
| `r-03` | Time and z plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat0\hat3\hat0\hat3}$, the tidal entry along the third space axis. |
| `r-12` | x and y plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat1\hat2\hat1\hat2}$, the curvature of the space plane spanned by the first two space axes. |
| `r-13` | z and x plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat3\hat1\hat3\hat1}$, the curvature of the space plane that leaves the second space axis out. |
| `r-23` | y and z plane | number | -5–5 step 0.1 1 | 0 | source in table | Sets $R_{\hat2\hat3\hat2\hat3}$, the curvature of the space plane that leaves the first space axis out. |
| `radius` | Distance, in horizon radii | number | 1–8 step 0.25 1 | 1 | source in schwarzschild | Moves the static observer outward. Every entry scales as the inverse cube of this distance, so the whole table at distance one is the pattern $(-2, 1, 1)$ for the time cells and $(2, -1, -1)$ for the space cells. |
| `tide-one` | First free tide | number | -5–5 step 0.1 1 | -2 | source in vacuum-family | Sets the first tidal entry of an empty-space table. The third is minus the sum of the first two, and each space cell is minus the time cell across from it, so every Ricci readout stays at zero. |
| `tide-two` | Second free tide | number | -5–5 step 0.1 1 | 1 | source in vacuum-family | Sets the second tidal entry of an empty-space table. These two sliders reach every Ricci-flat table this widget can hold. |
| `equation-of-state` | What fills the universe | enum | dust, radiation, stiff, vacuum-energy | "dust" | source in expanding-universe | Chooses the pressure-to-density ratio $w$ of a spatially flat expanding universe. In units of the Hubble rate squared, each time cell is $(1 + 3w)/2$ and each space cell is one. |
| `sectional-k` | Curvature of a curved plane | number | -3–3 step 0.25 1 | 1 | source in constant-curvature, two-factor | Sets $K$. With one value on every plane, each time cell is $-K$ and each space cell is $+K$. With two curved factors, only the time-and-x cell and the y-and-z cell are filled, at $-K$ and $+K$. |
| `highlight` | Light the cells a readout adds | enum | none, ricci-time-time, ricci-x-x, ricci-scalar, einstein-time-time, einstein-x-x, weyl-time-x, kretschmann | "none" | — | Rings the cells the chosen readout adds and prints the sign each one enters with. Cells left out stay fully visible and unringed. Choosing the Weyl entry turns the Weyl grid on, and choosing the Kretschmann scalar turns the scalar readouts on, so the readout being explained is always on screen. |
| `show-weyl` | Show the Weyl table | boolean | — | false | — | Draws a second, dashed grid holding the same six cells with their trace parts removed, and reveals the Weyl readouts. |
| `invariants` | Show the scalar readouts | boolean | — | false | — | Reveals the Kretschmann scalar, the squared Ricci tensor, the Ricci quotient and the check on the decomposition identity. |
| `axis-names` | Names for the four axes | enum | axes, star (source in schwarzschild, vacuum-family), comoving (source in expanding-universe), factors (source in two-factor) | "axes" | — | Relabels the rows and columns. The numbers and the readouts never change, because the frame is the same. |

## Presets

- `flat` Flat: every cell zero: source="table", r-01=0, r-02=0, r-03=0, r-12=0, r-13=0, r-23=0
- `six-numbers` Six numbers, two readings: source="table", r-01=3, r-02=-1, r-03=-1, r-12=1, r-13=1, r-23=2
- `inside-still-water` Inside still water, in units of four pi G rho over three: source="table", r-01=1, r-02=1, r-03=1, r-12=2, r-13=2, r-23=2
- `tides-only` The star's tides with the space planes emptied: source="table", r-01=-2, r-02=1, r-03=1, r-12=0, r-13=0, r-23=0
- `outside-a-star` Outside a spherical mass, at the horizon radius: source="schwarzschild", radius=1
- `outside-a-star-far` Outside a spherical mass, at twice the horizon radius: source="schwarzschild", radius=2
- `vacuum-two-sliders` Another empty-space table: source="vacuum-family", tide-one=1, tide-two=1
- `dust-universe` Expanding dust universe, in units of the Hubble rate squared: source="expanding-universe", equation-of-state="dust"
- `radiation-universe` Expanding radiation universe: source="expanding-universe", equation-of-state="radiation"
- `stiff-universe` Expanding stiff-matter universe: source="expanding-universe", equation-of-state="stiff"
- `de-sitter` One value on every plane, positive: source="constant-curvature", sectional-k=1
- `anti-de-sitter` One value on every plane, negative: source="constant-curvature", sectional-k=-1
- `two-curved-factors` Two curved factors side by side, positive: source="two-factor", sectional-k=1
- `two-curved-factors-flipped` Two curved factors side by side, negative: source="two-factor", sectional-k=-1

## Readouts

- `ricci-time-time` Ricci reading for this observer (1; visible always; 3 decimals; range (-15, 15]; sense: positive when a small ball of free particles let go at rest starts to lose volume): “the observer's Ricci reading is {value}” / “the observer's Ricci reading is minus {abs}”
- `ricci-x-x` Ricci component along x (1; visible always; 3 decimals; range (-15, 15]; sense: positive when the entry has the same sign as the metric entry along that space axis): “the Ricci component along x is {value}” / “the Ricci component along x is minus {abs}”
- `ricci-scalar` Ricci scalar (1; visible always; 3 decimals; range (-60, 60]; sense: positive when the space planes outweigh the tides, as on a sphere): “the Ricci scalar is {value}” / “the Ricci scalar is minus {abs}”
- `einstein-time-time` Einstein reading for this observer (1; visible always; 3 decimals; range (-15, 15]; sense: positive when the three space planes add to a positive curvature, which for matter at rest means positive energy density): “the observer's Einstein reading is {value}” / “the observer's Einstein reading is minus {abs}”
- `einstein-x-x` Einstein component along x (1; visible always; 3 decimals; range (-15, 15]; sense: positive when the two tides that leave the x axis out outweigh the space plane that leaves it out, which for a fluid at rest means positive pressure): “the Einstein component along x is {value}” / “the Einstein component along x is minus {abs}”
- `einstein-mismatch` Einstein mismatch (1; visible always; 3 decimals): “the largest mismatch between a time cell and the space cell that uses the other two axes is {value}, so this is an Einstein space only when that mismatch reads zero”
- `einstein-constant` Ricci quotient (1; visible on-demand; 3 decimals; range (-15, 15]; sense: positive when the Ricci tensor is a positive multiple of the metric, as in de Sitter spacetime): “the Ricci quotient is {value}, and it is the Einstein constant only while the mismatch reads zero” / “the Ricci quotient is minus {abs}, and it is the Einstein constant only while the mismatch reads zero”
- `weyl-time-x` Weyl entry in the time and x cell (1; visible on-demand; 3 decimals; range (-6.7, 6.7]; sense: positive when the Weyl remainder stretches a falling pair along the x axis in the same sense as a positive tidal entry there): “the Weyl entry in the time and x cell is {value}” / “the Weyl entry in the time and x cell is minus {abs}”
- `weyl-norm` Weyl tensor squared (1; visible on-demand; 4 decimals): “the Weyl tensor squared is {value}”
- `kretschmann` Kretschmann scalar (1; visible on-demand; 4 decimals): “the Kretschmann scalar is {value}”
- `ricci-norm` Ricci tensor squared (1; visible on-demand; 4 decimals): “the Ricci tensor squared is {value}”
- `decomposition-check` Decomposition check (1; visible on-demand; 9 decimals): “the decomposition check is {value}, and it must stay at zero”

## Tours

### `the-ricci-reading` · for [[ricci-tensor]] · working

1. `meet-the-table` (working, await none) state: preset="six-numbers"  
   *The four-by-four grid filled with the check values three, minus one, minus one on the time row and one, one, two among the space planes. No highlight ring.*  
   Say: “This is the curvature at one event, read in one freely falling observer's orthonormal frame. The grid has one row and one column for each of the observer's four axes: time, x, y and z. Only the six cells with two different axes carry a number, because a plane needs two directions, so the diagonal cells are grey and hatched. The three cells with a blue border pair the time axis with a space axis. The three with a green border pair two space axes. An orange fill with a plus badge means the number is positive, and a violet fill with a minus badge means it is negative.”  
   Describe: A four by four table of curvature numbers. Three of them pair time with a space direction and read three, minus one and minus one. Three pair two space directions and read one, one and two.
2. `light-the-tides` (working, await prediction) state: preset="six-numbers", highlight="ricci-time-time"; evidences `ricci-bianchi-and-einstein-tensors/checks/six-numbers-two-readings`  
   *Yellow rings on the three blue time cells, each ring badged plus. The Ricci readout is covered.*  
   Predict: “The three blue cells in the time row are now ringed, each with a plus badge on the ring. Before I add them, what does the observer's Ricci reading come to?”  
   Say: “I select the observer's Ricci reading, and a thick yellow ring appears on exactly the three blue cells in the time row. Each ring carries a plus badge, so all three enter with the same sign. The green cells stay unringed and fully visible. Before I add them, what does the reading come to?”  
   Describe: The three time cells are ringed and each enters with a plus. They read three, minus one and minus one.
3. `read-the-total` (working, await none) state: preset="six-numbers", highlight="ricci-time-time"  
   *The same rings with the Ricci readout uncovered at one.*  
   Say: “Three, take away one, take away one, leaves one. That single number is the whole of what the Ricci tensor says to this observer: the total of the three tidal drifts in a small ball of free particles let go at rest. It is positive here, so the ball starts to lose volume.”  
   Describe: The Ricci reading shows one. It is the total of the three tidal drifts.
4. `outside-a-star` (working, await prediction) state: preset="outside-a-star", highlight="ricci-time-time"; evidences `ricci-tensor/checks/vacuum-table-with-zero-ricci`  
   *The star-exterior table with minus two, plus one, plus one ringed in the time row. Every cell is filled and none is zero.*  
   Predict: “These three tides are as strong as any in the widget. Will their total be zero, or something else?”  
   Say: “Now the numbers come from an observer outside a spherical mass, held at a fixed distance from it, in units of the tidal scale at that distance. The ringed time cells read minus two, plus one and plus one. Every one of the six cells is filled, and none of them is zero. Will the three ringed numbers add to zero, or to something else?”  
   Describe: Outside a spherical mass the three tidal entries read minus two, plus one and plus one, and all six cells carry numbers.
5. `zero-without-flatness` (working, await none) state: preset="outside-a-star", highlight="ricci-time-time"  
   *The same table with the Ricci readout uncovered at zero and every cell still filled and coloured.*  
   Say: “Minus two, plus one, plus one is zero. The reading is zero and the table is not. Nothing dims, nothing greys out: the six numbers are still there, and a ball of free particles still turns into an egg. A zero Ricci reading says the ball keeps its volume, not that the curvature has gone.”  
   Describe: The Ricci reading is zero while all six cells still carry numbers.
6. `inside-matter` (working, await none) state: preset="inside-still-water", highlight="ricci-time-time"  
   *The still-water table with all three time cells at one, ringed, and the Ricci readout at three.*  
   Say: “Here the observer floats inside still water instead, with the numbers in units of four pi G rho over three. Now the three ringed time cells all read one, and the reading is three. Among matter the tides no longer cancel, and the ball of free particles starts to shrink.”  
   Describe: Inside still water the three tidal entries are all one and the Ricci reading is three.

### `one-number-for-the-event` · for [[ricci-scalar]] · working

1. `light-every-cell` (working, await none) state: preset="six-numbers", highlight="ricci-scalar"  
   *All six cells ringed. The three blue time cells carry minus badges on their rings, the three green space cells carry plus badges. The Ricci scalar readout reads six.*  
   Say: “I select the Ricci scalar, and now every one of the six cells is ringed. Look at the badges on the rings. The three green space cells each carry a plus, but the three blue time cells each carry a minus. The inverse metric puts that minus there, because the time entry of the metric has the opposite sign. Twice the space total, take away twice the time total, gives six.”  
   Describe: All six cells are ringed. The three space cells enter with a plus and the three time cells with a minus. The Ricci scalar reads six.
2. `never-the-plain-sum` (working, await none) state: preset="de-sitter", highlight="ricci-scalar"  
   *Constant curvature with the value one: every time cell minus one, every space cell plus one, and the Ricci scalar at twelve.*  
   Say: “Here is a spacetime with one and the same curvature on every plane. Each blue time cell reads minus one and each green space cell reads plus one. A plain diagonal sum of those six numbers would be zero. The scalar reads twelve instead, because the three time cells enter with a minus sign, and twelve is the right answer for four dimensions with the value one.”  
   Describe: Every time cell is minus one and every space cell is plus one, and the Ricci scalar reads twelve.
3. `predict-the-radiation-scalar` (working, await prediction) state: preset="radiation-universe", highlight="ricci-scalar"; evidences `ricci-scalar/checks/radiation-universe`  
   *The radiation table with every cell at one, all six ringed, three minus badges and three plus badges.*  
   Predict: “In this expanding radiation universe all six cells read one, in units of the Hubble rate squared. What does the Ricci scalar come to?”  
   Say: “Now I fill the table from an expanding universe of radiation at one moment, in units of the Hubble rate squared. All six cells read one. The three time cells are ringed with a minus and the three space cells with a plus. What does the Ricci scalar come to?”  
   Describe: In the radiation universe all six cells read one, the three time cells entering with a minus and the three space cells with a plus.
4. `scalar-flat-is-not-empty` (working, await none) state: preset="radiation-universe", highlight="ricci-scalar"  
   *The same table with the Ricci scalar readout at zero and the Ricci reading readout at three.*  
   Say: “The scalar reads zero. The three minuses cancel the three pluses exactly. And yet the Ricci reading beside it says three, so the space is full of radiation and the tides are real. A zero scalar is one number cancelling, not an empty region.”  
   Describe: The Ricci scalar reads zero while the Ricci reading reads three in the same radiation universe.
5. `the-other-sign` (working, await none) state: preset="stiff-universe", highlight="ricci-scalar"  
   *The stiff-matter table with time cells at two and space cells at one, and the Ricci scalar at minus six.*  
   Say: “I stiffen the matter until its pressure matches its energy density. The blue time cells rise to two while the green space cells stay at one, and the scalar swings to minus six. So the scalar takes either sign, and its sign tells you which of the two totals is winning, not whether the region is curved.”  
   Describe: With stiff matter the time cells read two and the space cells one, and the Ricci scalar reads minus six.

### `the-einstein-reading` · for [[einstein-tensor]] · working

1. `light-the-space-planes` (working, await prediction) state: preset="six-numbers", highlight="einstein-time-time"; evidences `einstein-tensor/checks/rings-not-tides`  
   *Yellow rings on the three green space cells only, each badged plus. The blue time cells stay unringed. The Einstein readout is covered.*  
   Predict: “The three green space cells are ringed, each with a plus badge, and the blue time cells are not ringed at all. What does the observer's Einstein reading come to?”  
   Say: “Same table, and now I select the observer's Einstein reading. The ring jumps to the other three cells. The green space cells are ringed, each with a plus badge, and the three blue time cells are not ringed at all. The tides have dropped out. Before I add them, what does the reading come to?”  
   Describe: Only the three space cells are ringed, reading one, one and two. The time cells are not ringed.
2. `the-tides-cancelled` (working, await none) state: preset="six-numbers", highlight="einstein-time-time"  
   *The same rings with the Einstein readout uncovered at four.*  
   Say: “One plus one plus two is four. This is what trace reversal does at the observer's own component: the Ricci reading adds the three tides, and the Einstein reading adds the three space planes instead. Half the Ricci scalar cancels the tides away exactly, which is why the strong tide of three in the time and x cell buys the Einstein reading nothing.”  
   Describe: The Einstein reading is four, the total of the three space planes.
3. `strong-tides-zero-reading` (working, await prediction) state: preset="outside-a-star", highlight="einstein-time-time"; evidences `einstein-tensor/checks/zero-einstein-not-flat`  
   *The star-exterior table with only the three green space cells ringed, reading plus two, minus one, minus one.*  
   Predict: “Outside a spherical mass the tides are as strong as anywhere in this widget. The ringed green cells read plus two in the y and z cell and minus one in each of the other two. Will the Einstein reading be large?”  
   Say: “Outside a spherical mass the blue time cells hold the strongest tides in this widget, and they are unringed. The ringed green cells read plus two in the y and z cell and minus one in each of the other two. Will the Einstein reading be large?”  
   Describe: Outside a spherical mass the three ringed space cells read plus two in the y and z cell and minus one in each of the other two.
4. `vacuum-reading` (working, await none) state: preset="outside-a-star", highlight="einstein-time-time"  
   *The same table with the Einstein readout uncovered at zero.*  
   Say: “Zero. Two, take away one, take away one. Einstein's equation ties this reading to the energy density the observer measures, and outside the star there is none. The tides say nothing about it either way.”  
   Describe: The Einstein reading outside the star is zero, while all six cells still carry numbers.
5. `leave-one-direction-out` (working, await none) state: preset="six-numbers", highlight="einstein-x-x"  
   *Rings on the time and y cell, the time and z cell, and the y and z cell. Their badges read plus, plus and minus. The Einstein component along x reads minus four.*  
   Say: “The pattern carries to the other diagonal components. I select the Einstein component along x, and the ring lands on the three cells that leave the x axis out: the time and y cell, the time and z cell, and the y and z cell. The first two carry a plus badge and the third a minus. Minus one, minus one, take away two, gives minus four.”  
   Describe: The three cells that leave the x axis out are ringed, and the Einstein component along x reads minus four.
6. `the-expanding-reading` (working, await none) state: preset="dust-universe", highlight="einstein-time-time"; evidences `einstein-tensor/checks/flat-universe-not-zero`  
   *The dust universe table with time cells at one half and space cells at one, the three green cells ringed, and the Einstein readout at three.*  
   Say: “Here is an expanding dust universe at one moment, in units of the Hubble rate squared. The three ringed green space cells each read one, and the reading is three. That is the first Friedmann equation, standing in the table: three times the Hubble rate squared equals eight pi G times the density. Space here is flat in the sense that a ruler survey finds no shortfall, yet the reading is not zero, because these are curvatures of spacetime planes.”  
   Describe: In the expanding dust universe each space cell reads one and the Einstein reading is three.

### `vacuum-without-flatness` · for [[ricci-flat-spacetime]] · formal

1. `every-ricci-readout-zero` (formal, await none) state: preset="outside-a-star"  
   *The star-exterior table with no highlight. Ricci reading zero, Ricci component along x zero, Ricci scalar zero, Einstein reading zero, Einstein component along x zero.*  
   Say: “Outside a spherical mass, every Ricci readout on the strip reads zero at once: the observer's reading, the component along x, and the scalar. Because the trace reversal is its own inverse, the Einstein readouts are zero as well. This is a Ricci-flat region, and in four dimensions that is exactly the vacuum equation without a cosmological constant.”  
   Describe: Outside a spherical mass every Ricci and Einstein readout reads zero, while the three time cells read minus two, one and one and the three space cells read two, minus one and minus one.
2. `what-survives` (formal, await prediction) state: preset="outside-a-star", invariants=true, show-weyl=true; evidences `ricci-flat-spacetime/checks/four-regions-two-tests`  
   *The same table with the invariant strip and the dashed Weyl grid revealed. The Kretschmann readout is covered.*  
   Predict: “The scalar readouts are now on. With every Ricci readout at zero, will the Kretschmann scalar be zero too?”  
   Say: “I turn on the scalar readouts and the dashed Weyl grid beside the table. Every entry of the dashed grid matches the entry in the same place in the full grid, because a Ricci-flat table has nothing to subtract. With every Ricci readout at zero, will the Kretschmann scalar be zero too?”  
   Describe: The dashed Weyl grid holds the same six numbers as the full grid, and the scalar readouts are switched on.
3. `forty-eight` (formal, await none) state: preset="outside-a-star", invariants=true, show-weyl=true  
   *Kretschmann readout at forty-eight, Weyl tensor squared at forty-eight, Ricci tensor squared at zero.*  
   Say: “Forty-eight. The Kretschmann scalar and the Weyl tensor squared both read forty-eight and the Ricci tensor squared reads zero, because in a Ricci-flat region the whole Riemann tensor is its Weyl part. In two and three dimensions this could not happen, since there Ricci-flat already forces flat. From four dimensions on, the traces leave something over.”  
   Describe: The Kretschmann scalar and the Weyl tensor squared both read forty-eight while the Ricci tensor squared reads zero.
4. `a-whole-family` (formal, await none) state: preset="vacuum-two-sliders", invariants=true  
   *The two-slider vacuum table reading one, one, minus two on the time row and minus one, minus one, two among the space planes. All Ricci readouts zero, Kretschmann forty-eight.*  
   Say: “Two sliders reach every empty-space table this widget can hold. I set both to one, and the third tidal cell follows to minus two while each green cell takes minus the blue cell that uses the other two axes. Every Ricci readout is still zero. This is a different vacuum from the star's, turned onto another axis, and it happens to share the Kretschmann value of forty-eight.”  
   Describe: A second empty-space table, with the tidal entries one, one and minus two, again has every Ricci readout at zero.
5. `scalar-flat-is-weaker` (formal, await prediction) state: preset="radiation-universe", invariants=true; evidences `ricci-flat-spacetime/checks/radiation-universe-is-scalar-flat`  
   *The radiation table with every cell at one, Ricci scalar zero, Ricci reading three.*  
   Predict: “This radiation universe has a Ricci scalar of zero. Does that make it Ricci-flat?”  
   Say: “Now compare a different region. This expanding radiation universe has a Ricci scalar of zero, the same value the star's exterior gives. Does that make it Ricci-flat?”  
   Describe: The radiation universe has every cell at one and a Ricci scalar of zero.
6. `the-ladder` (formal, await none) state: preset="flat", invariants=true, show-weyl=true  
   *Every cell zero, every readout zero, the dashed Weyl grid empty.*  
   Say: “No. The radiation universe keeps a Ricci reading of three, so it is scalar-flat and not Ricci-flat. Flat is the strictest of the three conditions, and here it is: I empty every cell, and now every readout on the strip is zero and the dashed Weyl grid is empty as well. Flat gives Ricci-flat gives scalar-flat, and neither arrow runs backwards from four dimensions on.”  
   Describe: With every cell emptied, every readout reads zero and the Weyl grid is empty.

### `einstein-without-constant-curvature` · for [[einstein-space]] · formal

1. `the-mismatch-readout` (formal, await none) state: preset="de-sitter", invariants=true, show-weyl=true  
   *Constant curvature at one. Einstein mismatch zero, Ricci quotient three, Weyl tensor squared zero, dashed Weyl grid empty.*  
   Say: “The Einstein mismatch readout takes each blue time cell, adds the green cell that uses the other two axes, and reports the largest size it finds. It reads zero exactly when the Ricci tensor is a constant times the metric. Here every time cell is minus one and every space cell is plus one, so each pair cancels and the mismatch is zero. The Ricci quotient beside it reads three, and in four dimensions that quotient is the cosmological constant. The dashed Weyl grid is empty.”  
   Describe: With one value on every plane the Einstein mismatch is zero, the Ricci quotient is three, and the Weyl grid is empty.
2. `two-curved-factors` (formal, await prediction) state: preset="two-curved-factors", invariants=true, show-weyl=true; evidences `constant-curvature-weyl-and-invariants/checks/two-spheres-side-by-side`  
   *Two curved factors: only the time and x cell at minus one and the y and z cell at plus one are filled, in orange and violet. The other four cells are empty. Readouts covered.*  
   Predict: “Only two cells are filled: the time and x cell at minus one, and the y and z cell at plus one. Every plane that mixes the two pairs reads zero. Is this an Einstein space, and does it have constant curvature?”  
   Say: “Now I build a spacetime out of two curved factors set side by side, with equal curvature radii. Only two cells are filled: the time and x cell at minus one, on a violet fill, and the y and z cell at plus one, on an orange fill. Every plane that takes one direction from each factor reads zero, so those four cells are empty. Is this an Einstein space, and does it have constant curvature?”  
   Describe: Only two cells carry numbers, minus one and plus one, and the four mixed cells are empty.
3. `einstein-yes-constant-no` (formal, await none) state: preset="two-curved-factors", invariants=true, show-weyl=true  
   *Einstein mismatch zero, Ricci quotient one, Weyl tensor squared five point three three three, dashed Weyl grid with entries minus two thirds, one third, one third and their opposites.*  
   Say: “Einstein yes, constant curvature no. The mismatch is zero and the Ricci quotient reads one, so the Ricci tensor is the metric times one. But the four empty cells are planes with zero curvature sitting beside two planes with curvature of size one, so the planes do not share a value. The dashed Weyl grid proves it: the Weyl tensor squared reads five point three three three, which is sixteen thirds. The Einstein condition fixes only the traces, and from four dimensions on a free Weyl tensor is left over.”  
   Describe: The Einstein mismatch is zero, the Ricci quotient is one, and the Weyl tensor squared is sixteen thirds.
4. `flip-the-sign` (formal, await none) state: preset="two-curved-factors-flipped", invariants=true, show-weyl=true  
   *Two curved factors with the curvature at minus one: time and x cell plus one, y and z cell minus one, Ricci quotient minus one, Weyl tensor squared five point three three three.*  
   Say: “I flip the curvature of both factors to minus one. The two filled cells swap colour: the time and x cell turns orange at plus one and the y and z cell turns violet at minus one. The mismatch is still zero and the quotient is now minus one, so this is an Einstein space with a negative constant. The Weyl tensor squared has not moved from sixteen thirds, because it does not know the sign.”  
   Describe: With both factors negative the Ricci quotient reads minus one and the Weyl tensor squared is still sixteen thirds.
5. `zero-counts` (formal, await none) state: preset="outside-a-star", invariants=true; evidences `einstein-space/checks/schwarzschild-is-an-einstein-space`  
   *The star-exterior table with Einstein mismatch zero and Ricci quotient zero.*  
   Say: “The star's exterior is an Einstein space too. Its mismatch reads zero and its quotient reads zero, and zero is an allowed constant. Every Ricci-flat region is an Einstein space with the constant set to nothing.”  
   Describe: Outside the star the Einstein mismatch is zero and the Ricci quotient is zero.
6. `not-every-table` (formal, await none) state: preset="dust-universe", invariants=true  
   *The dust universe table with the Einstein mismatch at one point five.*  
   Say: “The expanding dust universe is the other way round. Each time cell reads one half and each space cell reads one, so every pair adds to one and a half instead of cancelling, and the mismatch reads one and a half. Its Ricci tensor is not a constant times the metric, so it is no Einstein space, however smooth and symmetric the universe looks.”  
   Describe: In the dust universe every time and space pair adds to one and a half, so the Einstein mismatch is one and a half.

### `what-the-traces-leave-free` · for [[weyl-tensor]] · formal

1. `subtract-the-traces` (formal, await none) state: preset="six-numbers", show-weyl=true  
   *The check table with the dashed Weyl grid beside it, holding one, minus one half, minus one half in the time row and their opposites among the space planes.*  
   Say: “The dashed grid beside the table holds the Weyl tensor: the same six cells with their trace parts taken out. Two things are worth watching in it. Its three time entries always add to zero, because the Weyl tensor is trace-free on every pair of slots. And each green space entry in the dashed grid is minus the blue time entry that uses the other two axes, so the whole dashed grid runs on two free numbers.”  
   Describe: A second dashed grid holds the Weyl entries. Its three time entries add to zero and each space entry is minus the time entry that uses the other two axes.
2. `vacuum-leaves-everything` (formal, await prediction) state: preset="outside-a-star", show-weyl=true; evidences `weyl-tensor/checks/vacuum-leftover`  
   *The star-exterior table with the dashed grid covered.*  
   Predict: “Outside the star every Ricci readout is zero. What will the dashed Weyl grid hold?”  
   Say: “Outside a spherical mass every Ricci readout is zero, so there is nothing to subtract. What will the dashed Weyl grid hold?”  
   Describe: The star-exterior table is on screen with the Weyl grid hidden.
3. `all-of-it` (formal, await none) state: preset="outside-a-star", show-weyl=true, invariants=true  
   *The dashed Weyl grid matching the full grid cell for cell: minus two, one, one, two, minus one, minus one. Weyl tensor squared forty-eight.*  
   Say: “All of it. Every dashed cell matches the cell in the same place in the full grid, and the Weyl tensor squared equals the Kretschmann scalar at forty-eight. Einstein's equation fixes the Ricci tensor at an event from the matter there. Ten of the twenty components are what it leaves free, and outside a star they are the entire curvature.”  
   Describe: The Weyl grid matches the full grid cell for cell and the Weyl tensor squared reads forty-eight.
4. `expanding-leaves-nothing` (formal, await none) state: preset="dust-universe", show-weyl=true, invariants=true  
   *The dust universe table with the dashed Weyl grid empty and the Weyl tensor squared at zero.*  
   Say: “The expanding dust universe is the mirror case. Its time cells read one half and its space cells read one, and none of them is zero, yet the dashed grid is completely empty and the Weyl tensor squared reads zero. The curvature here is all trace and no remainder, which is another way of saying the universe is conformally flat: a rescaling of the metric makes it flat.”  
   Describe: In the dust universe the Weyl grid is empty and the Weyl tensor squared reads zero, although the six cells are not zero.
5. `both-parts-at-once` (formal, await none) state: preset="tides-only", show-weyl=true, invariants=true  
   *Time cells minus two, one, one with the space cells emptied. Ricci reading zero, Ricci component along x two, Weyl tensor squared twelve, Ricci tensor squared six.*  
   Say: “Most tables are a mixture. I keep the star's three tides and empty the space planes by hand. The Ricci reading still comes to zero, but the component along x reads two, so the Ricci tensor has not vanished. Both parts are alive here: the Weyl tensor squared reads twelve and the Ricci tensor squared reads six. This table is neither a vacuum nor a conformally flat universe.”  
   Describe: With the space planes emptied the Ricci component along x reads two, the Weyl tensor squared reads twelve and the Ricci tensor squared reads six.
6. `rescaling-does-not-touch-it` (formal, await none) state: preset="de-sitter", show-weyl=true, invariants=true  
   *Constant curvature at one, dashed Weyl grid empty, Weyl tensor squared zero.*  
   Say: “One last case. With one and the same value on every plane, the dashed grid empties again. That is the whole content of the statement that an Einstein space has constant curvature exactly when its Weyl tensor vanishes, and it is the reason the Weyl tensor with one index raised survives any rescaling of the metric.”  
   Describe: With one value on every plane the Weyl grid is empty and the Weyl tensor squared is zero.

### `adding-up-the-squares` · for [[kretschmann-scalar]] · formal

1. `square-every-cell` (formal, await prediction) state: preset="outside-a-star", invariants=true, highlight="kretschmann"; evidences `kretschmann-scalar/checks/ricci-zero-outside-a-star`  
   *The star-exterior table with all six cells ringed and every badge a plus. The Kretschmann readout is covered.*  
   Predict: “Every one of the six cells is ringed, each badged plus, because every cell enters squared. The three time cells read minus two, one and one, and the three space cells read two, minus one and minus one. What does the Kretschmann scalar come to?”  
   Say: “I select the Kretschmann scalar, and all six cells are ringed with a plus badge each, because every cell enters squared and no sign survives. For a table like this one, with no entry pairing two different planes, the scalar is simply four times the total of the six squares. The three time cells read minus two, one and one, and the three space cells read two, minus one and minus one. What does it come to?”  
   Describe: All six cells are ringed with a plus badge. The three time cells read minus two, one and one, and the three space cells read two, minus one and minus one.
2. `forty-eight-again` (formal, await none) state: preset="outside-a-star", invariants=true, highlight="kretschmann"  
   *Kretschmann readout at forty-eight.*  
   Say: “Four, one, one, four, one, one add to twelve, and four times twelve is forty-eight. That is the number behind the standard result for a spherical mass: forty-eight times the mass squared over the distance to the sixth power. The readout is a single number that every observer at this event agrees on, unlike any one cell of the table.”  
   Describe: The Kretschmann scalar outside the star reads forty-eight.
3. `move-out` (formal, await none) state: preset="outside-a-star", invariants=true; animate radius → 2 over 4 s; evidences `constant-curvature-weyl-and-invariants/checks/curvature-length-at-the-horizon`  
   *The radius slider sliding from one to two while every cell shrinks by a factor of eight and the Kretschmann readout falls from forty-eight to nought point seven five.*  
   Say: “Now I slide the observer out from the horizon radius to twice that distance. Every cell shrinks by a factor of eight, because each one falls off as the inverse cube. The Kretschmann readout falls by eight squared, from forty-eight to nought point seven five: a ratio of sixty-four. Nothing here blows up or breaks at the horizon radius, even though the usual radial metric coefficient does.”  
   Describe: As the observer moves from the horizon radius to twice that distance, every cell shrinks eightfold and the Kretschmann scalar falls from forty-eight to nought point seven five.
4. `the-split` (formal, await none) state: preset="two-curved-factors", invariants=true, show-weyl=true  
   *Two curved factors: Kretschmann eight, Weyl tensor squared five point three three three, Ricci tensor squared four, Ricci scalar four, decomposition check zero.*  
   Say: “The scalar splits into a Weyl piece and Ricci pieces. Here are the two curved factors: the Kretschmann scalar reads eight, the Weyl tensor squared reads sixteen thirds, the Ricci tensor squared reads four and the Ricci scalar reads four. Sixteen thirds, plus twice four, take away a third of four squared, is eight. The decomposition check at the end of the strip recomputes that difference on its own and must stay at zero.”  
   Describe: For the two curved factors the Kretschmann scalar is eight, the Weyl tensor squared is sixteen thirds, the Ricci tensor squared is four, and the decomposition check reads zero.
5. `what-this-table-cannot-hold` (formal, await prediction) state: preset="flat", invariants=true; evidences `constant-curvature-weyl-and-invariants/checks/plane-wave-versus-minkowski`  
   *Every cell empty, every readout zero, with the edge note about what the table leaves out.*  
   Predict: “The Kretschmann readout is zero here. In this widget, does a zero reading force every cell to be zero? And would you expect that to hold in every spacetime?”  
   Say: “Last, the empty table, with every readout at zero. In this widget a zero reading does force every cell to zero, because the scalar here is four times a total of squares. Read the note along the edge of the table before you carry that away. This table holds only the six entries that pair a plane with itself, and no entry pairing two different planes, so it cannot be given a passing gravitational wave. Such a spacetime has real tides and every scalar invariant zero, and no widget of six sliders will show you that.”  
   Describe: The table is empty and every readout is zero. A note along the edge says the table cannot hold a passing gravitational wave.

## Design rules

- **Never blank, grey or dim a cell because a readout that adds it has come out zero. Cells change only when their own number changes.** Because: Outside a spherical mass every Ricci and Einstein readout is zero while all six cells are as large as anywhere in the widget, and that contrast is the whole lesson. Prevents `ricci-bianchi-and-einstein-tensors/misconceptions/zero-ricci-means-flat`.
- **When the observer's Einstein reading is selected, the three time cells take no ring and no badge, even when they hold the largest numbers in the table.** Because: The tides cancel exactly out of that component, and a ring on them would say the opposite. Prevents `ricci-bianchi-and-einstein-tensors/misconceptions/tides-set-the-einstein-reading`.
- **Whenever the Ricci scalar is selected, print a minus badge on each of the three time cells and a plus badge on each of the three space cells.** Because: The inverse metric supplies the minus; a plain diagonal sum of the six numbers is not the scalar and in general coordinates means nothing at all. Prevents `ricci-scalar/misconceptions/diagonal-sum`.
- **In any state whose Einstein mismatch reads zero, keep the dashed Weyl grid one click away and never let the mismatch readout alone be presented as a verdict on the geometry.** Because: An Einstein space with a nonzero Weyl tensor, such as two curved factors side by side, is the standard counterexample to reading the Einstein condition as constant curvature. Prevents `constant-curvature-weyl-and-invariants/misconceptions/einstein-means-constant-curvature`.
- **Keep a standing line on the table saying that these are components in one observer's orthonormal frame at one event, and mark which readouts every observer agrees on.** Because: A cell is a component and can be made to grow or shrink by changing observer or chart, while the scalar readouts cannot; taking a component for a verdict on the geometry is the mistake behind reading a diverging chart component as a singularity. Prevents `constant-curvature-weyl-and-invariants/misconceptions/diverging-component-means-singular`.
- **Print along the edge of the table that it holds only the six entries pairing a plane with itself, so no passing gravitational wave can be entered, and never claim that a zero invariant readout means flat.** Because: A vacuum plane wave has real tides and every scalar invariant zero, which no combination of these six sliders can produce; without the note the widget would teach that zero invariants mean flat. Prevents `constant-curvature-weyl-and-invariants/misconceptions/zero-scalars-mean-flat`.
- **Carry the sign of every cell and of every ring on a plus or minus badge as well as in the fill colour.** Because: Colour alone fails for colour-blind learners and in print, and the sign of a cell is the point of most of the readouts.

## Model

The widget holds one algebraic curvature tensor at one event, in one orthonormal frame with signature minus, plus, plus, plus. Its six sliders are the components $R_{\hat a\hat b\hat a\hat b}$ for the six pairs of frame axes; every component pairing two different planes is held at zero. That restriction is consistent: with the mixed components gone, the first Bianchi identity reduces to a sum of three of them and is satisfied automatically, so any six numbers give a legitimate curvature tensor. The restriction also makes the Ricci tensor diagonal and the Weyl tensor purely electric. Every readout is a polynomial in the six numbers, computed in closed form. The numbers carry no fixed physical unit: each preset names the curvature scale its numbers are measured in, and the scalar readouts are in that scale squared.

**The six entries**

$$
R_{\hat a\hat b\hat a\hat b},\qquad \hat a < \hat b,\qquad R_{\hat a\hat b\hat c\hat d} = 0 \ \text{whenever} \ \{\hat a\hat b\} \neq \{\hat c\hat d\}
$$

Holds when: One event, one orthonormal frame, signature minus plus plus plus. The first Bianchi identity in four dimensions has one independent component, $R_{\hat0[\hat1\hat2\hat3]}$, which is built from the discarded mixed components, so it holds for any six numbers.

**Ricci components from the table**

$$
R_{\hat0\hat0} = \sum_i R_{\hat0\hat\imath\hat0\hat\imath},\qquad R_{\hat\imath\hat\imath} = -R_{\hat0\hat\imath\hat0\hat\imath} + \sum_{j \neq i} R_{\hat\imath\hat\jmath\hat\imath\hat\jmath}
$$

Holds when: The minus sign comes from the time entry of the inverse frame metric. Off-diagonal Ricci components vanish because the mixed curvature components do.

**Ricci scalar from the table**

$$
R = -2\sum_i R_{\hat0\hat\imath\hat0\hat\imath} + 2\sum_{i<j} R_{\hat\imath\hat\jmath\hat\imath\hat\jmath}
$$

Holds when: Trace with the inverse metric, not a plain diagonal sum.

**Einstein components from the table**

$$
G_{\hat0\hat0} = R_{\hat1\hat2\hat1\hat2} + R_{\hat2\hat3\hat2\hat3} + R_{\hat3\hat1\hat3\hat1},\qquad G_{\hat1\hat1} = R_{\hat0\hat2\hat0\hat2} + R_{\hat0\hat3\hat0\hat3} - R_{\hat2\hat3\hat2\hat3}
$$

Holds when: Each diagonal Einstein component draws on exactly the three cells that leave its own axis out. Follows from trace reversal, $G_{\mu\nu} = R_{\mu\nu} - \tfrac12 R g_{\mu\nu}$.

**When the table is an Einstein space**

$$
R_{\mu\nu} = \lambda\,g_{\mu\nu} \iff R_{\hat0\hat\imath\hat0\hat\imath} + R_{\hat\jmath\hat k\hat\jmath\hat k} = 0 \ \text{for each} \ i, \qquad \lambda = -\sum_i R_{\hat0\hat\imath\hat0\hat\imath} = \tfrac14 R
$$

Holds when: Here $\{j,k\}$ is the pair of space axes left over by $i$. The mismatch readout reports the largest size of $R_{\hat0\hat\imath\hat0\hat\imath} + R_{\hat\jmath\hat k\hat\jmath\hat k}$; the quotient readout reports $R/4$ whether or not the mismatch is zero.

**Weyl entries from the table**

$$
C_{\hat0\hat\imath\hat0\hat\imath} = \tfrac12\big(R_{\hat0\hat\imath\hat0\hat\imath} - R_{\hat\jmath\hat k\hat\jmath\hat k}\big) - \tfrac16\Big(\sum_m R_{\hat0\hat m\hat0\hat m} - \sum_{m<n} R_{\hat m\hat n\hat m\hat n}\Big),\qquad C_{\hat\jmath\hat k\hat\jmath\hat k} = -C_{\hat0\hat\imath\hat0\hat\imath}
$$

Holds when: From the Schouten decomposition in four dimensions. The three Weyl time entries add to zero, so the dashed grid has two free numbers. The Weyl tensor here has no magnetic part, because the mixed components vanish.

**Kretschmann scalar from the table**

$$
\mathcal K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} = 4\sum_{\hat a < \hat b}\big(R_{\hat a\hat b\hat a\hat b}\big)^2
$$

Holds when: Each unordered pair contributes four index arrangements, and raising the indices of these components costs no sign because each time index appears twice. The plain total of squares holds only for tables of this restricted shape; in general the frame expansion has negative terms.

**How the scalars split**

$$
\mathcal K = C_{\mu\nu\rho\sigma}C^{\mu\nu\rho\sigma} + 2R_{\mu\nu}R^{\mu\nu} - \tfrac13 R^2
$$

Holds when: Four dimensions. The decomposition-check readout is the size of the difference between the two sides, computed from the six entries along two independent routes.

**Outside a spherical mass**

$$
\big(R_{\hat t\hat r\hat t\hat r}, R_{\hat t\hat\theta\hat t\hat\theta}, R_{\hat t\hat\phi\hat t\hat\phi}, R_{\hat\theta\hat\phi\hat\theta\hat\phi}, R_{\hat\phi\hat r\hat\phi\hat r}, R_{\hat r\hat\theta\hat r\hat\theta}\big) = \frac{m}{r^3}\,(-2, 1, 1, 2, -1, -1),\qquad m = \frac{GM}{c^2}
$$

Holds when: A static observer; a slowly moving one reads the same six numbers up to corrections of order $v^2/c^2$. The widget measures the distance in horizon radii $2m$ and states the entries in units of the value at that radius, so every cell falls off as the inverse cube of the distance slider.

**A spatially flat expanding universe**

$$
R_{\hat0\hat\imath\hat0\hat\imath} = -\frac{\ddot a}{a} = \frac{1+3w}{2}H^2,\qquad R_{\hat\imath\hat\jmath\hat\imath\hat\jmath} = \frac{\dot a^2}{a^2} = H^2
$$

Holds when: Comoving orthonormal frame, zero spatial curvature, pressure $p = w\rho c^2$. Dust gives one half and one; radiation gives one and one; stiff matter gives two and one; vacuum energy gives minus one and one, which is the constant-curvature case.

**One value on every plane, and two curved factors**

$$
R_{\hat0\hat\imath\hat0\hat\imath} = -K,\quad R_{\hat\imath\hat\jmath\hat\imath\hat\jmath} = K; \qquad \text{two factors:}\ R_{\hat0\hat1\hat0\hat1} = -K,\ R_{\hat2\hat3\hat2\hat3} = K,\ \text{rest zero}
$$

Holds when: The constant-curvature form follows from $R_{\rho\sigma\mu\nu} = K(g_{\rho\mu}g_{\sigma\nu} - g_{\rho\nu}g_{\sigma\mu})$, so the time cells pick up the sign of $g_{\hat0\hat0}$. The two-factor source is the Lorentzian product of a two-dimensional de Sitter factor and a sphere of the same radius, whose Riemann tensor vanishes on every plane mixing the factors; it shares $\lambda$, $\mathcal K$ and the Weyl norm with the Riemannian product of two equal spheres.

**Method:** Closed-form algebra: no integration and no linear solve. A source fills a six-vector of entries; every readout is then a polynomial in that vector, evaluated in double precision. The decomposition check is computed twice, once as four times the total of squares and once as the Weyl norm plus the Ricci terms, and the readout reports the size of their difference, so an error in either route shows up as a nonzero reading. Values are rendered rounded to each readout's declared decimals but compared at full precision in the tests.

| Test | State | Expect | Hidden | Note |
| --- | --- | --- | --- | --- |
| `flat-table-reads-zero` | preset="flat", show-weyl=true, invariants=true | ricci-time-time = 0 ±1e-12; ricci-x-x = 0 ±1e-12; ricci-scalar = 0 ±1e-12; einstein-time-time = 0 ±1e-12; einstein-x-x = 0 ±1e-12; einstein-mismatch = 0 ±1e-12; einstein-constant = 0 ±1e-12; weyl-time-x = 0 ±1e-12; weyl-norm = 0 ±1e-12; kretschmann = 0 ±1e-12; ricci-norm = 0 ±1e-12; decomposition-check = 0 ±1e-12 | — | The flat limit: an empty table must make every readout, including both remainders, read exactly zero. |
| `six-numbers-two-readings` | preset="six-numbers", show-weyl=true, invariants=true | ricci-time-time = 1 ±1e-09; einstein-time-time = 4 ±1e-09; ricci-x-x = -1 ±1e-09; einstein-x-x = -4 ±1e-09; ricci-scalar = 6 ±1e-09; einstein-mismatch = 5 ±1e-09; einstein-constant = 1.5 ±1e-09; weyl-time-x = 1 ±1e-09; weyl-norm = 12 ±1e-09; kretschmann = 68 ±1e-09; ricci-norm = 34 ±1e-09; decomposition-check = 0 ±1e-09 | — | The section's own check: three, minus one, minus one on the time row gives a Ricci reading of one, and one, two, one among the space planes gives an Einstein reading of four. |
| `scalars-hidden-until-asked` | preset="six-numbers" | ricci-time-time = 1 ±1e-09; einstein-time-time = 4 ±1e-09 | einstein-constant, weyl-time-x, weyl-norm, kretschmann, ricci-norm, decomposition-check | With both switches off, the six always-visible readouts show and the six on-demand ones do not. |
| `outside-a-star-at-the-horizon` | preset="outside-a-star", show-weyl=true, invariants=true | ricci-time-time = 0 ±1e-09; ricci-x-x = 0 ±1e-09; ricci-scalar = 0 ±1e-09; einstein-time-time = 0 ±1e-09; einstein-x-x = 0 ±1e-09; einstein-mismatch = 0 ±1e-09; einstein-constant = 0 ±1e-09; weyl-time-x = -2 ±1e-09; weyl-norm = 48 ±1e-09; kretschmann = 48 ±1e-09; ricci-norm = 0 ±1e-09; decomposition-check = 0 ±1e-09 | — | Ricci-flat and not flat: every Ricci and Einstein readout zero, the Weyl table equal to the full table, and the standard forty-eight for the Kretschmann scalar. |
| `star-fall-off-is-inverse-sixth-power` | preset="outside-a-star-far", show-weyl=true, invariants=true | kretschmann = 0.75 ±1e-09; weyl-norm = 0.75 ±1e-09; weyl-time-x = -0.25 ±1e-09; ricci-time-time = 0 ±1e-09; ricci-scalar = 0 ±1e-09 | — | Doubling the distance divides every cell by eight and the Kretschmann scalar by sixty-four: forty-eight over sixty-four is nought point seven five. |
| `another-vacuum-table` | preset="vacuum-two-sliders", show-weyl=true, invariants=true | ricci-time-time = 0 ±1e-09; ricci-x-x = 0 ±1e-09; ricci-scalar = 0 ±1e-09; einstein-mismatch = 0 ±1e-09; weyl-time-x = 1 ±1e-09; kretschmann = 48 ±1e-09; ricci-norm = 0 ±1e-09 | — | The two-slider vacuum family with both sliders at one gives the tidal entries one, one, minus two and again every Ricci readout zero; the positive branch of the Weyl entry. |
| `dust-universe` | preset="dust-universe", show-weyl=true, invariants=true | ricci-time-time = 1.5 ±1e-09; ricci-x-x = 1.5 ±1e-09; ricci-scalar = 3 ±1e-09; einstein-time-time = 3 ±1e-09; einstein-x-x = 0 ±1e-09; einstein-mismatch = 1.5 ±1e-09; weyl-time-x = 0 ±1e-09; weyl-norm = 0 ±1e-09; kretschmann = 15 ±1e-09; ricci-norm = 9 ±1e-09; decomposition-check = 0 ±1e-09 | — | In units of the Hubble rate squared: time cells one half, space cells one. The Einstein reading of three is the first Friedmann equation, the Weyl table is empty, and zero pressure shows as a zero Einstein component along x. |
| `radiation-universe-is-scalar-flat` | preset="radiation-universe", show-weyl=true, invariants=true | ricci-scalar = 0 ±1e-09; ricci-time-time = 3 ±1e-09; ricci-x-x = 1 ±1e-09; einstein-time-time = 3 ±1e-09; einstein-x-x = 1 ±1e-09; einstein-mismatch = 2 ±1e-09; weyl-norm = 0 ±1e-09; kretschmann = 24 ±1e-09; ricci-norm = 12 ±1e-09 | — | Scalar-flat and not Ricci-flat: the scalar reads zero while the Ricci reading reads three. The Einstein component along x is one, which is eight pi G times the radiation pressure. |
| `stiff-matter-negative-scalar` | preset="stiff-universe", invariants=true | ricci-scalar = -6 ±1e-09; ricci-time-time = 6 ±1e-09; ricci-x-x = 0 ±1e-09; einstein-time-time = 3 ±1e-09; einstein-x-x = 3 ±1e-09; einstein-constant = -1.5 ±1e-09; kretschmann = 60 ±1e-09; ricci-norm = 36 ±1e-09 | weyl-time-x, weyl-norm | The negative branch of the Ricci scalar and of the Ricci quotient, with the Weyl readouts left hidden because the Weyl switch is off. |
| `one-value-on-every-plane` | preset="de-sitter", show-weyl=true, invariants=true | ricci-time-time = -3 ±1e-09; ricci-x-x = 3 ±1e-09; ricci-scalar = 12 ±1e-09; einstein-time-time = 3 ±1e-09; einstein-x-x = -3 ±1e-09; einstein-mismatch = 0 ±1e-09; einstein-constant = 3 ±1e-09; weyl-time-x = 0 ±1e-09; weyl-norm = 0 ±1e-09; kretschmann = 24 ±1e-09; ricci-norm = 36 ±1e-09; decomposition-check = 0 ±1e-09 | — | Constant curvature with the value one: the negative branch of the Ricci reading, a quotient of three matching the cosmological constant three times the curvature, an empty Weyl table, and the Kretschmann value two times four times three. |
| `negative-constant-curvature` | preset="anti-de-sitter", show-weyl=true, invariants=true | ricci-time-time = 3 ±1e-09; ricci-x-x = -3 ±1e-09; ricci-scalar = -12 ±1e-09; einstein-time-time = -3 ±1e-09; einstein-x-x = 3 ±1e-09; einstein-constant = -3 ±1e-09; einstein-mismatch = 0 ±1e-09; weyl-norm = 0 ±1e-09; kretschmann = 24 ±1e-09 | — | The negative branch of the Ricci scalar, the Einstein reading and the Ricci quotient. The Kretschmann scalar does not change sign with the curvature. |
| `einstein-but-not-constant-curvature` | preset="two-curved-factors", show-weyl=true, invariants=true | ricci-time-time = -1 ±1e-09; ricci-x-x = 1 ±1e-09; ricci-scalar = 4 ±1e-09; einstein-time-time = 1 ±1e-09; einstein-x-x = -1 ±1e-09; einstein-mismatch = 0 ±1e-09; einstein-constant = 1 ±1e-09; weyl-time-x = -0.6666666667 ±1e-08; weyl-norm = 5.3333333333 ±1e-08; kretschmann = 8 ±1e-09; ricci-norm = 4 ±1e-09; decomposition-check = 0 ±1e-09 | — | The counterexample the chapter needs: mismatch zero with a Weyl norm of sixteen thirds. Same three numbers as the Riemannian product of two equal spheres, where the check gives lambda times a squared equal to one and the Weyl norm times a to the fourth equal to sixteen thirds. |
| `two-factors-with-the-sign-flipped` | preset="two-curved-factors-flipped", show-weyl=true, invariants=true | ricci-time-time = 1 ±1e-09; ricci-scalar = -4 ±1e-09; einstein-time-time = -1 ±1e-09; einstein-constant = -1 ±1e-09; einstein-mismatch = 0 ±1e-09; weyl-time-x = 0.6666666667 ±1e-08; weyl-norm = 5.3333333333 ±1e-08; kretschmann = 8 ±1e-09 | — | The positive branch of the Weyl entry and the negative branch of the Einstein reading, with the two quadratic invariants unchanged. |
| `tides-with-empty-space-planes` | preset="tides-only", show-weyl=true, invariants=true | ricci-time-time = 0 ±1e-09; ricci-x-x = 2 ±1e-09; ricci-scalar = 0 ±1e-09; einstein-time-time = 0 ±1e-09; einstein-x-x = 2 ±1e-09; einstein-mismatch = 2 ±1e-09; weyl-time-x = -1 ±1e-09; weyl-norm = 12 ±1e-09; kretschmann = 24 ±1e-09; ricci-norm = 6 ±1e-09; decomposition-check = 0 ±1e-09 | — | A mixed table: the Ricci reading and the Ricci scalar are both zero while the Ricci tensor squared is six, so zero on two readouts does not empty the Ricci tensor. |
| `inside-still-water` | preset="inside-still-water", invariants=true | ricci-time-time = 3 ±1e-09; einstein-time-time = 6 ±1e-09; einstein-x-x = 0 ±1e-09; ricci-scalar = 6 ±1e-09; einstein-mismatch = 3 ±1e-09; kretschmann = 60 ±1e-09 | weyl-time-x, weyl-norm | In units of four pi G rho over three the Ricci reading is three, which is four pi G rho, and the Einstein reading is six, which is eight pi G rho; the pressure of water is dropped, so the Einstein component along x reads zero. |
| `every-slider-at-the-top-of-its-range` | preset="flat", r-01=5, r-02=5, r-03=5, r-12=5, r-13=5, r-23=5, show-weyl=true, invariants=true | ricci-time-time = 15 ±1e-09; ricci-x-x = 5 ±1e-09; ricci-scalar = 0 ±1e-09; einstein-time-time = 15 ±1e-09; einstein-x-x = 5 ±1e-09; einstein-mismatch = 10 ±1e-09; weyl-time-x = 0 ±1e-09; kretschmann = 600 ±1e-09; ricci-norm = 300 ±1e-09; decomposition-check = 0 ±1e-09 | — | The boundary case: every slider at its maximum. The Ricci reading and the Einstein reading both reach fifteen, the Kretschmann scalar reaches six hundred, and the readout ranges must hold these without clipping. |

## Serves

- [[ricci-tensor]]: the highlight that rings the three time cells with their signs, and the challenge of finding a table with every Ricci readout zero and no cell zero
- [[ricci-scalar]]: the highlight that rings all six cells with a minus badge on the three time cells, and the radiation and stiff-matter presets, where nonzero cells give a zero and a negative scalar
- [[einstein-tensor]]: the Einstein readouts, whose highlight rings the three cells that leave the chosen axis out, next to the Ricci readouts on the same table
- [[ricci-flat-spacetime]]: the two-slider vacuum source, which reaches every Ricci-flat table the widget can hold, next to the radiation universe, which is scalar-flat but not Ricci-flat
- [[einstein-space]]: the Einstein mismatch and Ricci quotient readouts, with the two-curved-factors preset as an Einstein space that has no constant curvature
- [[weyl-tensor]]: the dashed Weyl grid: equal to the full table outside a star, empty in an expanding universe, and nonzero with a proportional Ricci tensor for two curved factors
- [[kretschmann-scalar]]: the highlight that rings all six cells with a plus badge because each enters squared, the distance slider showing the inverse sixth power, and the decomposition check

## In the visual network

- **Builds on:** [[four-legs-around-a-tiny-loop]], [[falling-ring-of-crumbs]]
- **Leads to:** [[cube-of-small-loops]], [[three-gauges-on-a-falling-probe]], [[circles-behind-a-see-through-star]]

## Accessibility

Every cell is announced as its pair of axis names, its number and its sign word, never by colour alone. Selecting a readout announces which cells it adds and the sign each one enters with, then the total. The Weyl grid and the scalar readouts are separate switches, so a screen reader is never given twelve numbers at once. Every slider, switch and readout is reachable from the keyboard, and each readout can be spoken on demand without changing the state.

Static alternative: A four by four table of curvature numbers for one observer at one event. Six cells carry numbers: three pair the time axis with a space axis and three pair two space axes. Readouts under the table give the Ricci components, the Ricci scalar, the Einstein components and the scalar invariants.

- `Tab and Shift Tab`: move between the six cells, the switches and the readouts
- `Up and Down arrows`: change the selected cell by one step
- `Page Up and Page Down`: change the selected cell by ten steps
- `1 to 6`: choose the source: six numbers by hand, a star's exterior, the vacuum family, an expanding universe, one value on every plane, or two curved factors
- `H`: cycle the readout whose cells are ringed
- `W`: show or hide the Weyl grid
- `S`: show or hide the scalar readouts
- `Enter`: speak the selected readout, its cells and their signs

## Starting material

Earlier course assets: `lesson-contract-curvature-by-hand`, `manuscript-section-10-curvature-invariants-and-summary-table`, `manuscript-chapter-10-tides-geodesic-deviation`

The earlier course already asked for this widget in prose: a six-entry table with sliders and live Ricci, scalar, Weyl and Kretschmann readouts, plus a find-a-vacuum challenge. Its worked star-exterior arithmetic becomes the flagship preset and the static card, and its summary table of what each geometric object measures becomes the readout strip's labels. New work: the highlight-with-signs mechanic, the Einstein mismatch and Ricci quotient readouts, the closed-form sources, and the decomposition check.

## Review: novice

**Verdict:** fixed (2026-09-16, revision 1)

**Retell attempt:** This visual has no entry tour, so I read the first working tour as a strong second-year undergraduate. Here is what I would say back. Curvature at one event, for one observer, is six numbers, one for each pair of that observer's four axes. The diagonal pairs hold nothing, because a plane needs two different directions. Three of the six pair the time axis with a space axis, and those are the tides. Three pair two space axes. The observer's Ricci reading is the total of the three time cells. In the first table they read three, minus one and minus one, so the reading is one, and because it is positive a small ball of free particles let go at rest starts to lose volume. Outside a spherical mass the three time cells read minus two, plus one and plus one, so they total zero while all six cells are still filled and none of them is zero. The ball keeps its volume but still stretches into an egg, so a zero Ricci reading is not the same as no curvature. Inside still water all three time cells read one, the reading is three, and the ball shrinks. Two things I could not keep straight. The observer was freely falling at the start and then static outside the star, and I did not know whether that was one observer or a new one. And the tutor sometimes named cells only by colour, so I was not sure whether the three blue cells and the three cells in the time row were the same three.

- Stumble: “The three blue cells are now ringed, each with a plus badge on the ring.”: The three cells are picked out by colour alone. If I cannot separate blue from green, or if the ring has already changed the colour I am looking at, I do not know which three cells to add. The say line of the same beat gives the second cue, the time row, but the prediction I am being asked for does not.
- Stumble: “Now the numbers come from a static observer outside a spherical mass, in units of the tidal scale there.”: The first beat told me these are components in one freely falling observer's frame. Now the observer is static, with no word about the swap, so I do not know whether the six numbers still belong to the same measurer. And the tidal scale is tied to there, which does not say which distance it belongs to, when the whole point of the next tour is that the scale changes as the observer moves out.
- Stumble: “Three of them are ringed with a minus and three with a plus.”: I am asked to predict the scalar right after this, and I cannot tell which three carry the minus. Every cell reads one here, so the answer happens not to depend on it, but I do not know that while I am predicting.
- Stumble: “One plus two plus one is four.”: The same beat's description lists the three space cells as one, one and two. Reading along the grid I see one, one, two, and I hear one, two, one, so I lose track of which cell holds which number while I am checking the sum.
- Stumble: “The ringed green cells read plus two, minus one and minus one.”: Read along the grid the three space cells go minus one, minus one, plus two, so the spoken order does not match the order on screen and I cannot tell which cell holds the plus two. Naming the cell fixes it without changing the order.
- Stumble: “Every entry of the dashed grid matches the entry across from it in the full grid, because a Ricci-flat table has nothing to subtract.”: Across from it is used in two different senses in this visual. Here it means the same position in the other grid; elsewhere it means the cell built from the other two axes. On top of that, the grid itself has faint mirror copies below the diagonal, so across could just as well mean the mirror cell. Three readings of one phrase.
- Stumble: “the third tidal cell follows to minus two while each green cell takes minus the blue cell across from it”: Same phrase, the other sense: here across from it means the space cell built from the two axes the time cell leaves out, not the cell in the same place in another grid and not the mirror copy. The pairing is never named, and it is the pairing the whole vacuum family rests on.
- Stumble: “The Einstein mismatch readout takes each blue time cell, adds the green cell across from it, and reports the largest size it finds.”: This is the definition of the readout, so the ambiguous phrase is doing the most work here of anywhere. I cannot pair the cells up with certainty, and the mismatch is the whole test the next four beats turn on.
- Stumble: “the largest mismatch between a time cell and the space cell across from it is {value}, so this is an Einstein space only when that reads zero”: The spoken readout carries the same ambiguous pairing, and that reads zero leaves the noun open, so I am not sure whether that is the mismatch or the space cell.
- Stumble: “And each green entry in the dashed grid is minus the blue entry across from it, so the whole dashed grid runs on two free numbers.”: The same pairing again, and the cells are named by colour with no second cue, although the description of this beat calls them space entries and time entries.
- Stumble: “Here is the rung one step down the ladder.”: Two problems in one sentence. There has been no ladder yet, so I do not know what is being stepped down. And calling it a step down tells me the answer to the question at the end of the same beat, which is whether a zero Ricci scalar makes a region Ricci-flat, before I have a chance to answer.
- Stumble: “Flat is the strictest rung of the three, and here it is”: Rung is being used as a picture that was never set up, and the project uses the same word for the depth levels of the writing, so it pulls two ways.
- Stumble: “The cells read minus two, one, one, two, minus one and minus one.”: Six numbers in a row with no break. I have to guess where the time cells stop and the space cells start, and the space three are not in the order I read them off the grid.
- Stumble: “Sixteen thirds, plus twice four, take away a third of sixteen, is eight.”: The sixteen appears from nowhere. The line just told me the Ricci scalar reads four, and I have to square it silently to get the sixteen. That is the one step in the arithmetic that is not on screen.
- Stumble: “In this widget, does a zero reading force every cell to be zero, and does it do so in general?”: The first half I can answer from the screen, since the scalar here is four times a total of squares. The second half I cannot: nothing I have been shown says anything about spacetimes this table cannot hold, and the answer arrives only in the tutor's next sentence. Asking it as a prediction makes me think I have missed something.
- Fixed: Gave the three time cells a position cue as well as their colour wherever a prediction turns on picking them out: tour the-ricci-reading beat light-the-tides, tour one-number-for-the-event beat predict-the-radiation-scalar, tour the-einstein-reading beat the-expanding-reading, tour what-the-traces-leave-free beat subtract-the-traces.
- Fixed: Named the measurer in tour the-ricci-reading beat outside-a-star as an observer held at a fixed distance, and tied the tidal scale to that distance rather than to there.
- Fixed: Replaced across from it throughout. Where it meant the corresponding cell of the other grid it now reads in the same place in the full grid; where it meant the complementary pair it now reads the cell that uses the other two axes. Changed in tours vacuum-without-flatness, einstein-without-constant-curvature and what-the-traces-leave-free, and in the spoken template of the einstein-mismatch readout.
- Fixed: Put the spoken order of the three space cells back in step with the grid in tour the-einstein-reading beat the-tides-cancelled, and named the cell holding the plus two in beat strong-tides-zero-reading rather than reordering the numbers.
- Fixed: Broke the six-number lists into the three time cells and the three space cells in tour vacuum-without-flatness beat every-ricci-readout-zero and tour adding-up-the-squares beat square-every-cell.
- Fixed: Removed the ladder picture where it had not been set up, in tour vacuum-without-flatness beats scalar-flat-is-weaker and the-ladder, and with it the sentence that gave away the answer to that beat's own question.
- Fixed: Made the squaring step explicit in tour adding-up-the-squares beat the-split.
- Fixed: Turned the second half of the prediction in tour adding-up-the-squares beat what-this-table-cannot-hold into an invitation to guess, since nothing on screen can settle it.
- Concern: Who the observer is changes without notice. The title line and tour the-ricci-reading beat meet-the-table say these are components in one freely falling observer's orthonormal frame, then beat outside-a-star uses an observer held at a fixed distance and beat inside-matter one floating in still water. Either fix one observer for the widget or add a sentence saying that these frames read the same six numbers here, which is a claim I cannot make myself.
- Concern: Two superlatives look false as written. Tour the-ricci-reading beat outside-a-star says these three tides are as strong as any in the widget and tour the-einstein-reading beat strong-tides-zero-reading says the blue time cells hold the strongest tides in this widget, but the six-numbers table shown two beats earlier in the same tour has a tidal cell of three against this table's minus two, and the hand-set source reaches further still. The claim needs narrowing, perhaps to the strongest tides of any source with a formula behind it.
- Concern: The three space cells are spoken in two different orders. Grid order, x and y then z and x then y and z, is used in tour the-ricci-reading beat meet-the-table and tour the-einstein-reading beat light-the-space-planes; partner order, each space cell beside the time cell it completes, is used in tour vacuum-without-flatness and tour adding-up-the-squares. Settle one order and say once which it is. While checking this I found that the show line of tour vacuum-without-flatness beat a-whole-family lists the vacuum space planes as minus one, minus one, two, where grid order gives two, minus one, minus one; the show lines are author text so I left them alone.
- Concern: Please confirm, as physics reviewer, that in the star-exterior preset the plus two sits in the y and z cell. My rewrite of tour the-einstein-reading beat strong-tides-zero-reading now states it, on the strength of the partner-order list in tour vacuum-without-flatness beat every-ricci-readout-zero and of the axis names option that calls the x axis toward the centre.
- Concern: The presets and the radius slider speak of the horizon radius while the prose speaks of a spherical mass. A reader who pictures a star will ask how the observer stands at the star's horizon radius. Either name the scale without the word horizon or say that the exterior table is the same for a star and for a black hole.
- Concern: The factor of two in the Ricci scalar is never accounted for. Tour one-number-for-the-event beat light-every-cell explains where the minus sign comes from, but twice the space total and twice the time total arrive unexplained, and that is the first thing I wanted to ask.
- Concern: Spoken numbers and printed numbers disagree in precision. The Weyl tensor squared, the Kretschmann scalar and the Ricci tensor squared carry four decimals, so their templates would speak forty-eight point zero zero zero zero, while the beats speak five point three three three for a value the strip prints as 5.3333.
- Concern: The decomposition check has no say_negative, although it is a signed difference rather than a total of squares. A small negative round-off would leave the tutor with no line to read.
- Concern: Tour adding-up-the-squares beat what-this-table-cannot-hold and the design rule say-what-the-table-leaves-out both send the reader to a note along the edge of the table without saying which edge, so the tutor cannot point at it and I did not know where to look.
