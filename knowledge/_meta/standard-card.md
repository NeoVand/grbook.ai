# Standard card (condensed writing guide)

This card is the binding standard in short form. The full guide (`_meta/writing-guide.md`) has the reasoning and
examples; open the section a validator warning names, or when a rule here is unclear. Section numbers match it.

## 1. Books are teachers, not the subject
Learn from the study evidence; never name, cite, locate or quote the source textbooks. Cite only primary works by
the field's founders and landmark papers, in `references`, and only when `verified` can be set by the physics reviewer.

## 2. Who sees what
`x-audience` on each field: reader (learner-visible at that rung), tutor (spoken; entry items have no math), author
(sketches, model, design rules), internal (provenance, review). Entry items obey the novice contract.

## 3. Depth ladder
Rungs entry (16-year-old, no calculus, words and pictures, at most three math expressions per explanation), working
(second-year undergraduate, calculus and vectors, SI with G and c), formal (graduate: precise definitions,
hypotheses, proof sketches, G = c = 1), research (PhD start: modern forms, open problems, references).
Tiers require: prerequisite entry+working; foundation and core entry+working+formal; advanced all four (entry
150–400 words); frontier entry (150–300, says what the reader needs first) + formal + research. Core and above: 2–5
research_horizon topics; advanced and frontier include a review. Every way after the first lists `continues`, and
its first sentence refers back by picture or result. Never point by position ("above", "earlier"). Every equation is
`justified_by` a derivation at or below its rung, a prerequisite concept, or "stated" (and the prose says so).
Entry ways are self-sufficient: restate borrowed tests or rules in `recap`.

## 4. Novice contract (entry fields)
1 start concrete, never with a definition; 2 sentences average ≤20 words, never >32, one idea per paragraph;
3 make every step explicit ("so", "because"); 4 at most one new term per paragraph, in its own sentence, then in
the glossary; 5 one word per idea and one idea per word (no synonyms, no double senses like "flat", "turn",
"left"); 6 every direction has its reference (whose left, seen from where; no compass words near a pole; name the
region, never "inside the loop" on a closed surface); 7 every measurement has its measurer and instrument; "sees"
is not "measures"; 8 every rule in a thought experiment is physically doable; 9 back every surprise within two
sentences with a reason, a count or a try-it that says what to see; 10 never describe a change with a word that
sounds unchanged; 11 pronouns only when the noun is unmistakable; 12 one real number in everyday units, and why
daily life hides the effect; no radians, scientific notation or bare unit symbols at entry; 13 try the first
what-ifs a teenager would try and make every general sentence true for them or scope it; 14 never "clearly,
obviously, of course, recall that…"; 15 simplifications are true within a stated scope, even without
`simplifies`; 16 entry checks are self-contained, with an unambiguous starting state, specific numbers and a
because-chain answer; 17 one idea per entry way: a second new idea gets its own way or moves to working.
Physics traps to scope: rubber sheet, "light slows near a mass", "escape speed exceeds c", "expands into",
"curved means bent like a tube", "something happens locally at the horizon".

## 5. Accuracy contract (every rung)
Follow `notation/course-conventions.md`; report a missing convention, never invent one. Derive every equation and
check dimensions, signs, index placement, factors of 2 and π, and limits (flat gives zero, weak field gives Newton).
Compute every number with python3 and work every check, example and problem to its answer. Give every universal
sentence its hypotheses. State sense and branch of every angle or phase, intrinsically, with "modulo 2π" where it
applies. Name the frame when a statement holds only in one. Check analogies with signs. Never claim nonexistence
without a theorem. Name objects unambiguously. Try counterexamples: cone tip, hole, Möbius band, great circle,
figure-eight, region larger than half a closed surface, non-commuting case, bent-but-flat surface; nonrelativistic
limit, massless case, non-static case, strong field, other observer or slicing. Record verification. Prefer
leaving something out to including something that might be wrong.

## 6. Formats
`md`: paragraphs, `- ` bullets, `*emphasis*`, `$…$` and `$$…$$`; every symbol inside math. `latex`: bare KaTeX.
`speech`: words a voice can read, numbers spelled as spoken, no `$ \ ^ _ ×`. `plain`: no markup, no math.

## 7. Ids and links
Kebab ids that name the idea, permanent once published (retired ids go to `retired_ids`). `checks[].targets` and
`misconceptions[].diagnosed_by` agree. `objectives[].evidenced_by` lists checks or problems at the objective's own
rung; every check and problem evidences an objective. `refs`, `uses`, `justified_by` use addresses.

## 8. Fields (essentials)
Summary: two or three speakable entry sentences, true for the first what-ifs. Ways: at least two kinds, no kind
for more than half; foundation and core notes with observations include an operational way; `gist` null unless the
spoken opener must differ; `picture` null when a visual is cited. Glossary: every technical term the entry rung
uses. Prerequisites: direct only, with `why` and `needed_for`, no cycles. Derivations: one move per step. Problems:
prerequisite ≥1, foundation ≥2, core and above ≥3, spanning two rungs, with hints, key_points, numeric answers and
solution. Tiers with a formal rung: ≥2 formal checks and ≥1 formal problem. Misconceptions ≤8, correction ≤2
sentences. Numeric answers carry unit, sign, tolerances (abs_tol when the value is 0), modulo for angles.
Lifecycle: draft (rev 1) → novice-reviewed → physics-reviewed (verdict accurate or fixed) → published. Any
learner-visible change bumps the revision; text changed after a review gets the other lens on exactly that text.

## 9. Budgets
Caps are ceilings, not targets. A draft stays within 80% of every cap; a review may go 10% past a cap only for
fixes it records. Never compress sentences to fit: drop or shorten the lowest-value item and say which. Word caps
by tier (prerequisite / foundation / core / advanced / frontier): entry ways 1000/1000/1000/400/300 (minimum
400/400/400/150/150); working 900/900/1000/1000/1000; formal 300/600/900/1100/1100 (minimum –/300/400/400/400);
research –/–/400/900/900; other way fields 450/650/800/800/800; equations+derivations+examples+problems+observations
900/1500/2300/2500/2500; objectives+misconceptions+checks+arc+tutor moves+analogies+glossary+traps
1200/2200/3300/3500/3500; links+visuals+history+horizon 200/300/900/1000/1000; total 5000/7000/9500/10500/10500.

## 10. Visuals
Name visuals after the picture. A proposal in a note gives a `sketch`. A catalog entry is a component contract:
typed params with `available_when`, presets, readouts with sense, branch and speech, tours with beats that link to
checks, tests with expected values and hidden readouts, design rules naming the misconception they prevent.

## 11. Reviews
Novice review: persona strictly; retell_attempt before fixing; every stumble as quote, problem, rewrite; fix and
check the ladder; sign `novice-reviewed`. Physics review: re-derive, recompute, work every item, verify
conventions, sense, frames, conditions and analogies, try counterexamples, confirm every reference, check the
novice rewrites; fix keeping simplicity; record verification; sign `physics-reviewed` only with accurate or fixed.
