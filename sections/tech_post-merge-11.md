> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-11 draft (tech-director)

## Placement

Four pairs, all in **§4.7** (Pending-system gate plan): three inside the
**Stub 7** fenced block (T-SCN-11 asymmetry (ii)'s *Ferrum Crossing* bullet,
T-SCN-11 asymmetry (ii)'s `WHY THIS IS STATED AS A REASON` paragraph, T-SCN-11's
`EQUALITY FAILS` clause), one in the **open-questions register** (row **Q17**).

No other section is touched. No map, lane number, terrain figure, week number,
`T-` ID or `Q` ID moves. T-SCN-10 stays reserved and unwritten. The register
stays **Q1–Q29, ten ruled**. Nothing in `sections/` is edited; this file is the
whole delta.

## Draft

### The violation, and the correction the gate's own numbers force

The filed sentence says fixture (a)'s 1 MP margin "evaporates into a
double-digit one." Both halves are wrong, and my own operands one clause
earlier are what convict the first:

| Claim as written | The document's own operands | Verdict |
|---|---|---|
| the new margin is "double-digit" | "14 is still strictly more than the owning lane's 5" → 14 vs 5 | **False.** The margin is **9**. Single-digit. |
| "fixture (a)'s 1 MP margin" (fixture (a) reports 1 MP *each way*) | §2.13.2's route table: East (9,3) → South (5,7) is `6 — (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)` — no `B` glyph | **Overstated.** Only the northern margin moves. |

The second is the one worth having. Fixture (a) prints **two** opposing figures,
and only one of them is a Bridge route:

| Objective | Owning lane | Opposing figure, Bridges permitted | Opposing figure, Bridge-free | Margin |
|---|---|---|---|---|
| **North (6,2)** — East's objective | East 5 from (9,3) | **6** from (1,3), over Bridge (5,1) | **14** | 1 MP → **9 MP** |
| **South (5,7)** — West's objective | West 5 from (1,5) | **6** from (9,3), `(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)` | **6** — unchanged | 1 MP → **1 MP** |

South's opposing route reaches column 5 only at the objective itself, on row 7,
below the river's southern end at (5,5) — §2.13.2 states the river "spans rows
0–5 only." Excluding an edge can only raise a shortest-path cost, and the 6 MP
witness uses no excluded edge, so 6 stands under either reading. The allowance
binds one of this map's two objectives, not the map.

**Which makes my sharpest point sharper, exactly as the gate says.** I claimed
a Bridge-free reading would still pass *Ferrum Crossing*. It passes in **both
seats** — North on 5 against 14, South on 5 against 6 untouched — so there is no
seat, no fixture and no invariant in the suite where the error surfaces. The
argument therefore stops being "the margin collapses into a meaningless number"
(which was one seat's story, told as if it were the map's) and becomes the
stronger one: **the allowance keeps one seat's opposing route honest, the other
seat's margin never depended on it, and neither of those facts is visible to a
gate, because no invariant in this stub reads a margin at all.** That is the
whole reason the allowance is stated as a *reason* rather than a *permission* —
nothing downstream would notice its absence.

### The class, one round on

The last three findings have each been inside a sentence that had just been
corrected, and all three are the same defect at a smaller scale each time:
**a figure measured on one object, asserted over a set of objects.** Round 9:
measured on one map, asserted over the map set. Round 10: measured on one seat's
objective, asserted over both ("fixture (a)'s 1 MP margin"). The repair is the
same each time — print the per-object measurement and delete the quantifier —
and Pair 2 below drops it one level further, to **per objective within a map**.

I re-swept the four sites this file touches plus the three it cites, at that
resolution:

| Site | Quantified over | Verdict |
|---|---|---|
| Stub 7 (ii) *Ferrum* bullet | "The opposing figure in fixture (a)" — implies one; there are two | **Overstated** → **Pair 1** |
| Stub 7 (ii) `WHY` paragraph | "fixture (a)'s 1 MP margin … evaporates" — both margins | **False + overstated** → **Pair 2** |
| Stub 7 (ii) *Causeway* bullet | "passing 3 against 5 in **both seats**" | **Holds** — both seats stated, both measured (§2.13.6, fixture (c)) |
| Stub 7 (ii) *Longwater* bullet | "the ONE map with no Bridge on any opposing route" | **Holds** — the gate re-derived it; Water 0 · Bridge 0 (§2.13.5) is the proof, not a survey |
| Stub 7 `EQUALITY FAILS` | "the one lane in the shipped set" — present tense | **Stale**, not false: Q28 moved that Infantry → **Pair 4** |
| Stub 7 fixture (a) | "A 1 MP margin each way" | **Holds** — literally true of the shipped, Bridge-permitting reading, which is the only reading fixture (a) asserts |
| Register Q17 | "the two river maps price it **per map, not alike**" | **Holds** — per-map, both stated. One dropped word → **Pair 3** |

Fixture (a) is deliberately left alone: its "1 MP each way" is a measurement of
the asserted reading and is correct. The error was importing that phrase into a
paragraph about the *counterfactual* reading, where it is true of one seat only.

---

### The pairs

**Pair 1 — Stub 7, T-SCN-11 asymmetry (ii), the *Ferrum Crossing* bullet.
REQUIRED (violation, scope half).** The bullet is the antecedent of the filed
sentence: it says "The opposing figure in fixture (a)," and fixture (a) has two.
The rewrite names both and measures both, so the paragraph that follows cannot
inherit a singular it never had. **No number is new** — 6, 14, (1,3), (5,1),
(9,3), (5,7) and the route string `(9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)` are all
verbatim from §2.13.2's eight-route table or fixture (a); (5,5) and "rows 0–5"
are §2.13.2's key coordinates and its river description. The 14 MP figure and
its route are unchanged from the current text, including the "from that hex"
scoping, which is deliberate: 14 is measured from (1,3), the hex the shipped
minimum comes from, and is not restated as a minimum over West's whole Infantry
set.

**OLD**

```
                    - Ferrum Crossing (§2.13.2) EXERCISES it. The opposing
                      figure in fixture (a) — West's cheapest route to
                      North (6,2), 6 MP from (1,3) — runs over the north
                      Bridge (5,1). Bridge-free, the cheapest route from
                      that hex to that objective costs 14 MP:
                      (2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w
                      (6,2) — around the river's southern end, then up
                      through the Woods ring. More than double.
```

**NEW**

```
                    - Ferrum Crossing (§2.13.2) EXERCISES it, but on ONE
                      of fixture (a)'s TWO opposing routes, not both.
                      West's cheapest route to North (6,2) — 6 MP from
                      (1,3) — runs over the north Bridge (5,1).
                      Bridge-free, the cheapest route from that hex to
                      that objective costs 14 MP:
                      (2,3)(3,4)(3,5)(4,5)(5,6)(6,6)m(6,5)(6,4)w(6,3)w
                      (6,2) — around the river's southern end, then up
                      through the Woods ring. More than double. The
                      OTHER opposing route in that fixture is already
                      Bridge-free and does not move: East's cheapest
                      route to South (5,7), 6 MP from (9,3), is
                      (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7), which reaches
                      column 5 only at the objective itself, on row 7,
                      below the river's southern end at (5,5) — the
                      river spans rows 0–5 only. Excluding an edge can
                      only RAISE a shortest path, and that 6 MP witness
                      uses no excluded edge, so 6 stands under either
                      reading. The allowance binds ONE of this map's two
                      objectives, the northern one.
```

---

**Pair 2 — Stub 7, T-SCN-11 asymmetry (ii), the `WHY THIS IS STATED AS A REASON`
paragraph. REQUIRED (the filed violation).** "Double-digit" is replaced by the
subtraction the document's own operands give, and the single margin is replaced
by the two, each measured. The argument is not weakened by the correction — it
is the correction: both seats pass under the counterfactual, so the failure is
invisible to every gate, which is a stronger statement of the same claim than
"the margin evaporates." Both integer pairs are printed **owning first and
bare**, per the print convention 80 lines above ("5 against 14," "5 against 6"),
not larger-first. **No number is new**: 5, 6 and 14 all appear in Pair 1 and in
fixture (a); 1 MP and 9 MP are subtractions of those, and 9 is the gate's own
independently-derived figure.

**OLD**

```
                    WHY THIS IS STATED AS A REASON AND NOT A PERMISSION: a
                    Bridge-free reading does not FAIL Ferrum Crossing. 14
                    is still strictly more than the owning lane's 5, so the
                    invariant still passes — it passes on a number that
                    describes a walk around the entire river, and fixture
                    (a)'s 1 MP margin, the thinnest in the set, evaporates
                    into a double-digit one. Nothing in this suite catches
                    an integer that has merely stopped meaning anything.
                    The Bridge is what makes that margin a margin.
```

**NEW**

```
                    WHY THIS IS STATED AS A REASON AND NOT A PERMISSION:
                    a Bridge-free reading does not FAIL Ferrum Crossing
                    in EITHER seat, so no gate in this suite catches it.
                    North still passes, at 5 against 14 — strictly more
                    than the owning lane, on a number that describes a
                    walk around the entire river. South still passes at
                    5 against 6, exactly as drawn, because its opposing
                    route never crossed a Bridge. What the counterfactual
                    changes is ONE margin of the two: North's opposing
                    figure goes from 6 to 14 against an unchanged owning
                    5, widening that margin from 1 MP to 9 MP — a
                    single-digit widening, and an unremarked one, because
                    this invariant asserts a strict inequality and NO
                    CEILING (asymmetry (i)). South's margin stays at 1 MP
                    and never depended on the allowance at all.
                    THE SPLIT IS THE REASON. The allowance is what keeps
                    the NORTHERN opposing route honest, and neither half
                    of the split is gate-catchable, because no invariant
                    in this stub reads a MARGIN — only the strict
                    inequality, which both seats satisfy either way. So
                    the Bridge is what makes the northern margin a
                    margin, and this suite would go on reporting green
                    while that integer stopped meaning anything.
```

---

**Pair 3 — register row Q17, the dropped word. REQUIRED (gate-noted, unfiled).**
"which states as explicitly that" is missing a word. The restoration is
`as much`, punctuated so the quotation reads cleanly. This is a **substring** of
Q17's question cell, unique in the master (the string `states as explicitly`
occurs once). No ruling, dependency, number or map moves; the answer cell is not
touched.

**OLD**

```
(§2.13.2, which states as explicitly that bridge control there is *tempo, not a topological wall*)
```

**NEW**

```
(§2.13.2, which states as much explicitly: bridge control there is *tempo, not a topological wall*)
```

---

**Pair 4 — Stub 7, T-SCN-11's `EQUALITY FAILS` clause. REQUIRED (gate-noted,
unfiled).** The clause says a `>=` "would pass the one lane in the shipped set
that a human would call contested," in the present tense. Q28 moved East's
second Infantry (9,5) → (9,1) and §2.13.2 now reports 5 against 6 in both seats,
so the shipped set contains no such lane; the tie survives only as fixture (b).
Every other site marks that pre-fix — asymmetry (iii) says "its PRE-FIX hex
(9,5)," fixture (b) says "PRE-FIX," Q22 and Q28 both narrate the relocation — so
this is the one site out of tense. The rule does not change and neither does the
comparison: `>` remains the ruled operator and equality still fails. **No number
is new** — (9,5), (9,1) and fixture (b) are all already in this stub.

**OLD**

```
            EQUALITY FAILS. "Strictly longer" is the ruled comparison, and a
            tie is precisely the race the rule exists to forbid; a >= would
            pass the one lane in the shipped set that a human would call
            contested.
```

**NEW**

```
            EQUALITY FAILS. "Strictly longer" is the ruled comparison, and a
            tie is precisely the race the rule exists to forbid; a >= would
            have passed the one lane in the PRE-FIX set that a human would
            call contested — West's South lane against East's second
            Infantry at (9,5), kept as fixture (b). Q28 moved that Infantry
            to (9,1), so the set AS SHIPPED holds no such lane today: the
            failing case survives as a fixture, not as a live refusal, and
            the operator stays > for the next map that needs it.
```

---

### Re-read of the new text, not only the replaced text

Every assertable claim in the four NEW blocks, checked against the source rather
than against the draft it came from — because the last three findings were each
inside a sentence that had just been corrected.

| New text | Check | Source |
|---|---|---|
| "5 against 14" (owning first, bare) | Print convention: owning-first, bare pair = owning-against-opposing. Owning = East's North lane = 5 | Stub 7 print convention; fixture (a) |
| "5 against 6, exactly as drawn" | Owning = West's South lane 5; opposing = East 6 from (9,3) | fixture (a); §2.13.2 table |
| "from 1 MP to 9 MP" | 6 − 5 = 1; 14 − 5 = 9. Single-digit | §2.13.2; the current 14 MP text |
| "no invariant in this stub reads a MARGIN" | T-SCN-11 asserts `>` only; asymmetry (i) states NO CEILING; T-SCN-06's ceiling applies to the **guided lane**, not the opposing route | Stub 7 asymmetry (i), T-SCN-06 |
| "reaches column 5 only at the objective itself" | Route `(9,4)(8,5)(8,6)(7,7)(6,7)(5,7)`: columns 9,8,8,7,6,5 — column 5 once, at (5,7) | §2.13.2 route table |
| "below the river's southern end at (5,5)" | Water is (5,0)(5,2)(5,3)(5,5); Bridges (5,1)(5,4); (5,7) is row 7 | §2.13.2 key coordinates |
| "the river spans rows 0–5 only" | Verbatim claim of §2.13.2 | §2.13.2 terrain paragraph |
| "Excluding an edge can only RAISE a shortest path" | Monotonicity of shortest paths under edge removal; the 6 MP witness uses no Bridge, so it survives the restriction and remains minimal | Standard; witness from §2.13.2 |
| "ONE of fixture (a)'s TWO opposing routes" | Fixture (a) prints East's 6 from (9,3) and West's 6 from (1,3) | fixture (a) |
| "the operator stays >" | T-SCN-11's formula line: `min … > the owning lane's cost` | Stub 7 formula |
| "(9,5) … kept as fixture (b)" | Fixture (b) is the (9,5) deployment reporting 5 against 5 | fixture (b) |

Two things I deliberately did **not** write, having considered both:

- **I did not claim 14 is the Bridge-free minimum over West's whole Infantry
  set.** T-SCN-11 minimises over every CanCapture unit that seat deploys (Q28),
  and the second West Infantry at (1,5) is not measured Bridge-free anywhere in
  the document. The bullet keeps the existing "from that hex" scoping, so the
  14 is what it has always been: a measurement from (1,3). Nothing in the
  argument needs the stronger claim — both seats pass regardless.
- **I did not touch fixture (a)'s "A 1 MP margin each way."** It is true of the
  asserted reading, which is the only reading fixture (a) describes. The defect
  was quoting it inside a paragraph about the counterfactual.

## Build order

Unchanged. No week number, dependency, acceptance set or `T-` ID moves. Row 7's
acceptance set is still `T-SCN-01..09, 11`, with T-SCN-10 reserved-unwritten by
the Q26 ruling. Restated for completeness only:

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3** for the priced half (T-SCN-04, 06, 08, 11) | Yes | T-SCN-01..09, 11 — **unchanged**; T-SCN-10 reserved-unwritten (Q26) |

Nothing here changes what any gate computes. All four pairs change what the
document *claims about* T-SCN-11 — the scope of one allowance, the arithmetic of
one counterfactual, one register word, and the tense of one clause. The
validator's inputs, formula, reported integers and refusal conditions are
identical before and after, and every fixture reports the same pair it reported
before this file.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.7 Stub 7, T-SCN-11 (ii), *Ferrum* bullet | "**The** opposing figure in fixture (a)…" | **Pair 1** | Fixture (a) has two opposing figures. The singular is what let the next paragraph generalise one seat's counterfactual to the map. Both are now named and measured. |
| §4.7 Stub 7, T-SCN-11 (ii), `WHY` paragraph | "…fixture (a)'s 1 MP margin … evaporates into a **double-digit** one." | **Pair 2** | The margin is **9** — 14 − 5, from the document's own operands one clause earlier — and only the northern margin moves at all; South's opposing route crosses no Bridge and stays at 6. Both seats pass the counterfactual, which is the stronger form of the point the paragraph exists to make. |
| §4.7 register, Q17 | "which states **as explicitly that** bridge control there is…" | **Pair 3** | Dropped word. Restored as "states as much explicitly". |
| §4.7 Stub 7, `EQUALITY FAILS` | "a >= would **pass the one lane in the shipped set**…" | **Pair 4** | Present tense, but Q28 moved that Infantry (9,5) → (9,1) and the shipped set no longer contains the lane. Every other site marks it pre-fix; this one now does too. |

## Open questions for the Director

**None new. No ID is filed. The register stays Q1–Q29, ten ruled** (Q7, Q20,
Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28).

All four defects were arithmetic, scope, wording or tense against facts the
document already holds: §2.13.2's eight-route table supplies both opposing
figures and the river's extent, Q28 supplies the relocation, and the subtraction
14 − 5 = 9 needs no ruling. Nothing here waits on the Director.

**One candidate was considered and deliberately not filed.** The Bridge-free
cost of West's *second* Infantry (1,5) → North (6,2) is not measured anywhere in
the document, and under Q28's reading T-SCN-11 minimises over both West
Infantry — so a fully-specified Bridge-free counterfactual would need it. It is
**not a gap**, because the counterfactual is not asserted by any invariant: the
shipped reading permits Bridges, both seats pass with the permitted routes, and
Pair 1 scopes its 14 to "from that hex" rather than claiming a set minimum.
Filing a Q would add an ID for a number no gate will ever compute. Flagged
rather than filed, per the standing rule that the register carries gaps and not
observations. If the Director wants the counterfactual fully priced instead of
scoped, that is a change request to §2.13.2's table (adding a Bridge-free
column), not a rule gap — and it is `scenario-designer`'s to price.

## Handoffs

- **`scenario-designer`** — no action required. §2.13.2's eight-route table is
  again the authority §4.7 was corrected *to*, and no cell of it moves. Both
  facts Pair 1 relies on are read straight out of it: the East (9,3) → South
  cell carries no `B` glyph, and the river "spans rows 0–5 only." One
  observation, unchanged from last round and still needing no edit: the table's
  routes are *witnesses* of a cheapest cost, not unique paths.
- **`rules-designer`** — no action. No rule, cost, comparison, operator or
  ruling changes. `>` stays the ruled comparison and equality still fails; Q17,
  Q21, Q22, Q26 and Q28 keep their rulings verbatim, and Q17's answer cell is
  not touched.
- **`ux-onboarding-designer`** — no action. §2.11.6's guided-opening beats and
  the directive strip are untouched; nothing here reaches a widget.
- **Director** — all four pairs are corrections; none is optional and none needs
  a ruling. Pairs 1 and 2 must land together: Pair 2's "ONE margin of the two"
  reads against the two routes Pair 1 names. One housekeeping item:
  `sections/tech_post-merge-11_tmp.md` is an accidental empty artifact of this
  run, marked VOID in its own first line, and should be deleted — it is not a
  draft and nothing references it.

## Grounding

| Claim | Backed by |
|---|---|
| The margin is 9, not double-digit | §4.7 Stub 7 (ii), current text: "14 is still strictly more than the owning lane's 5" → 14 − 5 = 9; gate's independent Dijkstra, `post-merge-10` finding |
| East's cheapest route to South crosses no Bridge | §2.13.2 eight-route table, East **(9,3)** *guided* → South: `6 — (9,4)F(8,5)(8,6)(7,7)(6,7)(5,7)`, no `B` glyph; the two Bridges are (5,1) and (5,4), neither on that route |
| That 6 MP is unchanged under a Bridge-free reading | The 6 MP witness uses no Bridge, so it survives edge removal; removal cannot lower any other path's cost |
| Fixture (a) prints two opposing figures | §4.7 fixture (a): "West's South lane 5 from (1,5) against East's cheapest 6 from (9,3); East's North lane 5 from (9,3) against West's cheapest 6 from (1,3) over the north Bridge (5,1)" |
| A Bridge-free reading passes in both seats | North: 14 > 5 (owning lane, fixture (a)). South: 6 > 5, unchanged. T-SCN-11 asserts strict inequality only, "NO CEILING" (asymmetry (i)) |
| Bridge-free, West (1,3) → North costs 14 MP | §4.7 Stub 7 (ii), current text and its printed route; gate-verified adjacency-valid and minimal, alternatives 15–16 |
| The river spans rows 0–5 | §2.13.2: "The river spans rows 0–5 only, crossed at two Bridges"; key coordinates Water (5,0)(5,2)(5,3)(5,5), Bridges (5,1)(5,4) |
| No invariant reads a margin | T-SCN-11 formula: `min … > the owning lane's cost`; asymmetry (i) "NO CEILING … it must merely cost MORE" |
| *Longwater March* is the one Bridge-free map | §2.13.5 terrain distribution Water 0 · Bridge 0; gate re-derivation this run |
| Q28 moved East's second Infantry | §2.13.2 starting positions, East Infantry ×2 = (9,3), (9,1); Q28 ruling: "**(9,5) → (9,1)**"; §4.7 asymmetry (iii) |
| The shipped set holds no contested lane | §2.13.2: "Both entries pass, and both report the same pair: 5 against 6"; Q22: "all six lanes pass" |
| Every other site marks the tie pre-fix | §4.7 asymmetry (iii) "its PRE-FIX hex (9,5)"; fixture (b) "with East's second Infantry at its PRE-FIX hex (9,5)"; §2.13.2 "Why East's second Infantry sits at (9,1) and not (9,5)" |
| Q17's dropped word | §4.7 register, Q17 question cell: "which states as explicitly that bridge control there is" — one occurrence in the master |
| Print convention is owning-first and bare | §4.7 Stub 7, PRINT CONVENTION: "the pair is written BARE — '5 against 6' — and always owning first" |
| Register extent | §4.7 register rows Q1–Q29; ruled rows Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 = ten |
| Source is current | `source/MANIFEST.txt`: `gdd.md … md5=8357f9714908bf3a556e7e65d9c7b133`, matching the hash the gate read |
