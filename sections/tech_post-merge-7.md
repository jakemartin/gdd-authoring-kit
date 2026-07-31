> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-7 draft (tech-director)

## Placement

Ten exact edits, all inside §4, closing the Q22 → Q28 chain:

- **§4.7 Stub 7** — T-SCN-11's quantifier (now ruled), asymmetry (iii), a new
  three-entry **Fixtures** block, and the Acceptance line.
- **§4.7 open-questions preamble** — Q28 leaves the *unruled* list, and the
  paragraph that existed only to explain why Q28 could carry no assumption is
  converted into a record of how it closed.
- **§4.7 register** — **Q28 → RULED**, **Q22** re-measured to the fixed map, and
  **Q21**'s Blocks column and closing rationale, which the deployment move
  obliged me to re-check.
- **§4.11** — row 7's cost cell and acceptance IDs, and the closing paragraph's
  written-and-blocked sentence.

§4.7's preamble extent is **already de-pinned** in the merged text (L1455–1458)
— nothing to do there. No map, hex, lane number, terrain figure or turn estimate
is touched anywhere in this draft; every number below is quoted from §2.13.2's
eight-route table or re-derived from it. T-SCN-10 stays reserved and unwritten
(Q26). No ID is renumbered and the register still runs Q1–Q28 — no new gap
qualified.

---

## Draft

### What actually changed, in one line

The rule was ruled strict and **the map moved instead of the rule**. That is the
whole shape of it, and it is the shape a gate is supposed to force: the gate was
written first, it refused a shipped deployment, and the deployment lost the
argument. §4's job now is to stop describing a blocked invariant and start
describing an asserting one — and to keep the refusal it caused, because a
failing case that was actually shipped is worth more than any fixture I could
invent.

### The measurement, re-derived

I re-derived all four decisive figures from §2.13.2's layout rather than
accepting the table, because two of the eight routes changed with the deployment
and both new ones are load-bearing. Odd-r adjacency per §2.13.1; costs per §2.3;
axial floor via `q = col − (row − (row & 1))/2` (§4.7).

| Route | Path | Cost | Axial floor | Optimal? |
|---|---|---|---|---|
| West (1,5) → South (5,7) | (2,6)(3,6)(3,7)(4,7)(5,7) | **5** | 5 | yes — floor met |
| East (9,3) → South (5,7) | (9,4)*F*(8,5)(8,6)(7,7)(6,7)(5,7) | **6** | 6 | yes — floor met |
| East (9,1) → South (5,7) | (9,2)(8,3)(8,4)(7,5)(7,6)*T*(6,7)(5,7) | **7** | 7 | yes — floor met |
| East (9,3) → North (6,2) | (8,3)(7,3)(6,3)*w*(6,2) | **5** | 4 | yes — every land approach to (6,2) other than the Bridge is Woods, so 4 is unreachable |
| West (1,3) → North (6,2) | (2,3)(3,2)(4,2)(4,1)(5,1)*B*(6,2) | **6** | 5 | yes — West's only northern crossing is (5,1), `dist((1,3),(5,1)) = 5`, so 5 + 1 = 6 |
| East (9,1) → North (6,2) | (9,2)(8,2)(7,2)*w*(6,2) | **5** | 4 | yes — same Woods ring |

South is West's: **5 against 6.** North is East's: **5 against 6.** Both strict,
both by 1 MP. That reproduces §2.13.2 exactly and it is the third independent
derivation of the same eight numbers, so I am treating them as settled.

Two things the re-derivation is worth having said out loud, because they are
what a future map edit will trip over:

1. **The margin is 1 MP and it is bought by terrain, not by distance.** Both
   North figures sit *above* their axial floor — East pays a Woods, West pays
   the detour to the only crossing. If a map edit ever adds a second northern
   crossing or opens the Woods ring, the North lane collapses to a tie the same
   way the South lane did. The south is the mirror case: every southern route
   is a plain geodesic, so the southern margin is deployment and nothing else.
2. **The relocation had to be a change of flank.** East's south town (7,6) is 2
   hexes from South (5,7), so by the triangle inequality anything within 3 MP of
   that town is within 5 MP of that factory — the town-cover role and the racer
   role are the same hex. That is `scenario-designer`'s argument and it holds:
   it is why no southern nudge existed, and it is why the gate's verdict here is
   a statement about the map's economy rather than about one careless placement.

### Why (b) is the fixture worth keeping

The pre-fix deployment is the best test case this suite is ever going to get. It
passes **every other invariant in Stub 7** — it is well-formed, connected,
economically valid, structurally distinct under T-SCN-07 — and it is a real
authored artefact rather than a constructed one. It also separates the two Q28
readings by itself: it fails at 5 against 5 under the ruled reading and passes at
5 against 6 under the refused one, so it pins the *quantifier*, not just the
comparison. A suite whose only fixtures pass proves nothing about refusal; this
one now ships with a scenario it must reject.

---

## The edits

### Edit 1 of 10 — §4.7 Stub 7, T-SCN-11's opening clause (L1854–1859)

The quantifier Q28 ruled belongs in the invariant's first sentence, not deferred
to a sub-point — a reader implementing this stub should not have to reach item
(iii) to learn what "cheapest" ranges over. The implementation note is here for
the same reason: the ruled reading looks like it costs one path per enemy unit
and does not, and the reason it does not is Q21.

**OLD**
```
  T-SCN-11  NON-CONTENTION (Q22, ruled): for EACH guidedOpening entry, the
            OPPOSING seat's cheapest land path to that same `objective` costs
            STRICTLY MORE MP than the owning seat's lane, as reported by
            T-SCN-08. This is the gate for §2.13.1's "uncontested, not merely
            reachable" — a promise that until now was a property of the drawn
            map rather than a checkable rule.
```
**NEW**
```
  T-SCN-11  NON-CONTENTION (Q22 ruled; unit set Q28 ruled): for EACH
            guidedOpening entry, the OPPOSING seat's cheapest land path to
            that same `objective` costs STRICTLY MORE MP than the owning
            seat's lane, as reported by T-SCN-08. The opposing route is
            minimised over EVERY CanCapture-row unit that seat deploys
            (Q28), not over that seat's `guidedOpening.infantry` alone:
                min over the opposing seat's Infantry of cost(hex, objective)
                  >  the owning lane's cost
            This is the gate for §2.13.1's "uncontested, not merely
            reachable" — a promise that until this revision was a property of
            the drawn map rather than a checkable rule, and one the map
            failed the first time it was checked (fixture (b)).
            IMPLEMENTATION, because the ruled reading looks more expensive
            than it is: the minimisation is ONE reverse Dijkstra per
            objective, not one path per unit. Root it at the `objective` with
            d(objective) = 0 and relax d(h) = min over neighbours n of
            (MoveCost(n) + d(n)); the result is every hex's cost TO that
            objective under the T-MOVE-01 accounting, so all of the opposing
            seat's Infantry are read off one pass and the cost is independent
            of how many units that seat deploys. That identity holds ONLY
            because Q21 priced the lane on terrain alone — under an "as
            deployed" reading each unit sees a different graph and the budget
            returns to one path per unit.
```

---

### Edit 2 of 10 — §4.7 Stub 7, asymmetry (iii) (L1885–1899)

This is the block that still records *Ferrum Crossing* as failing. It becomes the
record of the ruling and of what the ruling cost, and it keeps the reason the
narrow reading was refused, because that reasoning is the invariant's whole
justification.

**OLD**
```
              (iii) THE UNIT SET IS Q28, AND IT DECIDES THE SHIPPED MAP.
                    "The opposing seat's cheapest Infantry route" admits two
                    readings: (a) over EVERY CanCapture-row unit that seat
                    deploys, or (b) over that seat's own
                    `guidedOpening.infantry` alone. Measured on all three
                    §2.13 maps as drawn, (b) passes all six lanes and (a)
                    FAILS one — on Ferrum Crossing, East's SECOND Infantry at
                    (9,5) reaches West's South objective (5,7) in 5 MP
                    ((9,6),(8,7),(7,7),(6,7),(5,7), all cost 1, and the axial
                    distance is 5 so nothing cheaper exists), exactly TYING
                    West's 5 MP lane from (1,5); from East's guided hex (9,3)
                    the same objective costs 6. So this invariant is WRITTEN
                    AND BLOCKED, in the T-FAME-05 sense: no gate asserts it
                    until Q28 rules. Redrawing a map is not this section's
                    call.
```
**NEW**
```
              (iii) THE UNIT SET IS BROADER THAN THE LANE, per Q28 (ruled).
                    "The opposing seat's cheapest Infantry route" ranges over
                    EVERY CanCapture-row unit that seat deploys, not over
                    that seat's own `guidedOpening.infantry` alone. The
                    narrow reading was available, would have passed the
                    shipped map unchanged, and was refused: the property
                    guarded here is a RACE, and a race does not care which
                    Infantry wins it. T-SCN-06's NAMED-hex quantifier is not
                    a precedent against this — it names a hex because the
                    guided lane must be the one turn-1a actually marks,
                    whereas nothing is being marked on the opposing side and
                    the only question is who can arrive.
                    WHAT THE STRICT READING COST, PAID ONCE: one deployment
                    hex. Ferrum Crossing's East second Infantry was at (9,5),
                    5 MP from WEST's South objective and therefore tied with
                    West's own 5 MP lane; it now deploys at (9,1) (§2.13.2)
                    and the map passes in both seats at 5 against 6. No rule
                    was weakened, no terrain moved, and the tie survives as
                    fixture (b) rather than as an exception.
                    The relocation was forced, not chosen, which is the part
                    worth knowing before anyone edits that map: East's south
                    town (7,6) is 2 hexes from South (5,7), so by the
                    triangle inequality any hex covering that town is within
                    5 MP of that factory. On Ferrum Crossing a southern
                    town-capturer IS a racer for West's southern factory —
                    the conflict is geometric, not a placement slip.
```

---

### Edit 3 of 10 — §4.7 Stub 7, T-SCN-11 gains a Fixtures block (L1900–1903)

Insert only — the four OLD lines are reproduced unchanged and the block is
appended after them, immediately before `Determinism:`. T-SCN-08 is the
precedent for the form; fixture (b) is the one that matters, and it is real
rather than synthetic.

**OLD**
```
            Reported like T-SCN-08: a refusal carries BOTH measured integers,
            owning and opposing, so an author reads "5 against 5" rather than
            "contested" — and a map edit that shortens an enemy approach
            surfaces as a changed number, not a still-green boolean.
```
**NEW**
```
            Reported like T-SCN-08: a refusal carries BOTH measured integers,
            owning and opposing, so an author reads "5 against 5" rather than
            "contested" — and a map edit that shortens an enemy approach
            surfaces as a changed number, not a still-green boolean.
            Fixtures:
              (a) Ferrum Crossing (§2.13.2) PASSES in BOTH seats, reporting
                  5 against 6 each way: West's South lane 5 from (1,5)
                  against East's cheapest 6 from (9,3); East's North lane 5
                  from (9,3) against West's cheapest 6 from (1,3) over the
                  north Bridge (5,1). A 1 MP margin each way — the thinnest
                  in the set, on the one map that declares `symmetry: none`.
                  It is also the fixture that catches ASYMMETRIC PRICING: an
                  implementation that counts the objective hex on the owning
                  lane but not on the opposing route reports 5 against 5 and
                  refuses the shipped map.
              (b) THE FAILING FIXTURE IS REAL, NOT CONSTRUCTED. The same map
                  with East's second Infantry at its PRE-FIX hex (9,5) — one
                  placement changed, nothing else — must FAIL, reporting
                  5 against 5: (9,6),(8,7),(7,7),(6,7),(5,7), five cost-1
                  hexes, and the axial distance from (9,5) to (5,7) is 5, so
                  no cheaper route exists and no implementation detail can
                  make the number anything else. This deployment passed every
                  other invariant in this stub, T-SCN-07's distinctness floor
                  included; T-SCN-11 is the only check in the suite that sees
                  it. It also pins the QUANTIFIER and not merely the
                  comparison: under the Q28 reading REFUSED, (b) passes at
                  5 against 6, so an implementation that minimises over the
                  guidedOpening unit alone fails this fixture and nothing
                  else in the suite.
              (c) The Causeway (§2.13.6) passes 3 against 5 in both seats
                  with the Bridge crossing PERMITTED on the opposing route.
                  It is the fixture for asymmetry (ii): excluding Bridges
                  makes both opposing routes NON-EXISTENT on a bisected map
                  and passes it vacuously, so an implementation that inherits
                  T-SCN-06's Bridge-free clause onto the opposing side
                  reports "no route" here instead of 5.
```

---

### Edit 4 of 10 — §4.7 Stub 7, the Acceptance line (L1911–1915)

The line still says `11 blocked on Q28`. Nothing in this stub is
written-and-blocked any more; T-SCN-10 is reserved-*unwritten*, which is a
different state and is stated as one.

**OLD**
```
Acceptance: T-SCN-01..09 and T-SCN-11 headless (10 reserved-unwritten on Q26;
         11 blocked on Q28). The §4.2 validate_scenario MCP tool wraps the
         same checks in-editor for the Content agent; its manual fallback is
         running the headless validator on the exported file (MCP stays off the
         critical path, §3 guardrails).
```
**NEW**
```
Acceptance: T-SCN-01..09 and T-SCN-11 headless — the whole written suite.
         T-SCN-11 ASSERTS from its first run: Q22 gave it the comparison and
         Q28 gave it the unit set, so this stub carries no written-and-blocked
         invariant. T-SCN-10 is reserved and UNWRITTEN on Q26, which is a
         different state: nothing is asserted, so nothing is waiting.
         T-SCN-11 ships with its three fixtures, one of which — (b), the
         shipped map's own pre-fix deployment — must FAIL, so the suite
         demonstrates refusal and not merely agreement with the repo.
         The §4.2 validate_scenario MCP tool wraps the same checks in-editor
         for the Content agent; its manual fallback is running the headless
         validator on the exported file (MCP stays off the critical path,
         §3 guardrails).
```

---

### Edit 5 of 10 — §4.7, the open-questions preamble (L1965–1972)

Q28 leaves the *unruled* list. The paragraph above it existed only to explain why
Q28 could carry no assumption in force; deleting it would lose the one case that
bounds the register's own convention, so it is kept in the past tense with the
outcome attached. The enumeration sentence above (L1950–1958) is untouched — it
describes how Q28 arose, which is still accurate.

**OLD**
```
**Q28 is the one row where that convention does not hold**, and it is marked
unruled for exactly that reason: its conservative reading REFUSES A SHIPPED
MAP, so no reading could be stated there without either blocking *Ferrum
Crossing* or quietly weakening a rule the Director had just made.
**Rows marked *unruled* state no reading and block their gate outright** (Q4's
interruption semantics, Q5's stacking, Q6, Q8, Q9's target- and build-choice
ties, and Q28); those gates and milestones cannot be settled until the
Director answers.
```
**NEW**
```
**Q28 was the one row where that convention did not hold**, and how it closed
is worth keeping rather than deleting: its conservative reading REFUSED A
SHIPPED MAP, so no reading could be stated there without either blocking
*Ferrum Crossing* or quietly weakening a rule the Director had just made, and
it therefore carried no assumption at all while it was open. It was then ruled
the strict way and **the map was corrected instead of the rule** — one
deployment hex, no terrain and no rules text (Q28; §2.13.2). The limit of the
convention is now known and stated once: **where the conservative reading is
not free, this register states no reading and waits.**
**Rows marked *unruled* state no reading and block their gate outright** (Q4's
interruption semantics, Q5's stacking, Q6, Q8, and Q9's target- and
build-choice ties); those gates and milestones cannot be settled until the
Director answers.
```

---

### Edit 6 of 10 — register, **Q21**: Blocks column and the flagged rationale (L1996)

`scenario-designer` flagged the closing rationale sentence as possibly stale. I
re-measured rather than assumed, because the sentence was stated as a property of
the *drawn deployment* and a deployment has since moved. **It survives** — (9,1)
lies on none of the ten routes *Ferrum Crossing* prices — so the sentence's
conclusion is kept. What is genuinely stale is the **Blocks** column: Q21's
pricing convention is now cited by T-SCN-11 over eight routes on the shipped map,
and the column names only T-SCN-06 and T-SCN-08. Both halves are corrected in
one pair, and the re-check is dated so the next deployment edit knows to redo it.

**OLD**
```
| **Q21** | ~~Opening-capture lane measurement.~~ **RULED.** The lane prices on **terrain alone**, occupancy excluded. The question was whether T-SCN-06 should price it on the board **as deployed** — where, under Q3's blocked-pass-through reading, a seat's own four other starting units can make its own lane unmeasurable? The two readings can disagree by several MP on a crowded deployment. | T-SCN-06's pass/fail and T-SCN-08's reported integers; §2.13.1's three-map lane table if the answer is "as deployed" | Ruled as drafted: terrain alone. It reproduces §2.13.1's measured 5/5, 4/4, 3/3 and matches how the lane is actually played, since the other four units move too. Accepted consequence: a map can pass while a seat's own unit sits in the lane on turn 1 — the player walks around it, which on *Ferrum Crossing*'s 1 MP of slack may cost a turn and is absorbed by beat 2 being a standing directive (§2.11.6-B). **Scope narrowed by the §2.13 symmetry correction:** both stretch lanes are now clear of their own seat's starting units and price identically under either reading, so an "as deployed" ruling could only move *Ferrum Crossing*'s numbers — this is effectively a one-map question. |
```
**NEW**
```
| **Q21** | ~~Opening-capture lane measurement.~~ **RULED.** The lane prices on **terrain alone**, occupancy excluded. The question was whether T-SCN-06 should price it on the board **as deployed** — where, under Q3's blocked-pass-through reading, a seat's own four other starting units can make its own lane unmeasurable? The two readings can disagree by several MP on a crowded deployment. | T-SCN-06's pass/fail and T-SCN-08's reported integers; **T-SCN-11's eight opposing routes on the shipped map**, which price on this same convention; §2.13.1's three-map lane table if the answer is "as deployed" | Ruled as drafted: terrain alone. It reproduces §2.13.1's measured 5/5, 4/4, 3/3 and matches how the lane is actually played, since the other four units move too. Accepted consequence: a map can pass while a seat's own unit sits in the lane on turn 1 — the player walks around it, which on *Ferrum Crossing*'s 1 MP of slack may cost a turn and is absorbed by beat 2 being a standing directive (§2.11.6-B). **Scope, re-checked after the Q28 deployment move rather than assumed.** This row's scope was stated as a property of the drawn deployment, and a deployment has since moved — East's second Infantry (9,5) → (9,1), §2.13.2 — so it was re-measured. It holds, and at a sharper resolution: **no starting unit sits on any of the ten routes *Ferrum Crossing* now prices** (its two guided lanes and §2.13.2's eight T-SCN-11 routes), (9,1) among them, and both stretch lanes were already clear — so an "as deployed" ruling would move **no number on any map as drawn**. It stays a live question rather than a dead one because of slack: *Ferrum Crossing* carries 1 MP against T-SCN-06's ceiling and 1 MP against T-SCN-11's inequality, so it remains the only map where a future deployment edit landing in a priced route flips a gate instead of being absorbed. One further consequence, now that Q22 has widened the surface: terrain-only pricing is what lets T-SCN-11 minimise over a whole seat's Infantry in **one** reverse Dijkstra per objective (§4.7 Stub 7). An "as deployed" ruling would give every unit its own graph and return that cost to one path per unit. |
```

---

### Edit 7 of 10 — register, **Q22**: the measurement, now that the map is fixed (L1997)

The ruling and the demotion of T-SCN-07's clause to a floor stand exactly as
written — I checked both against the merged Stub 7 text and neither needs a word
changed. Three things in the row no longer read true: T-SCN-11 is not "written
and blocked", the sixth lane no longer fails, and the Blocks column's cost claim
("path budget doubles to two lookups per entry") was superseded by the ruled
unit set. The failure is *kept* — it is the reason the row is worth reading — but
as history with an outcome, and the floor sentence gains the one-line statement
of what a structural check cannot see.

**OLD**
```
| **Q22** | ~~Uncontested vs. merely reachable.~~ **RULED (this revision).** The validator asserts non-contention: **the opposing seat's cheapest Infantry route to the same objective must cost strictly more than the owning seat's lane.** T-SCN-07's distinctness clause is now a **floor beneath** that requirement, not the whole of it. Gated as **T-SCN-11** — T-SCN-10 is reserved-but-unwritten for the horizontal mirror and Q26 keeps it that way, so it was not free to take. Original question: §2.13.1 promises the guided lane is "uncontested, not merely reachable," but states it as a property of the shipped map rather than a checkable rule. | T-SCN-07's clause, now a floor; the new **T-SCN-11**; §4.11 row 7's priced half, whose path budget doubles to two lookups per guidedOpening entry | Ruled — and **measured against all three maps before the invariant was written**, which is what the ruling cost. Five of the six lanes clear it outright: *Longwater March* 8 vs 4 in both seats, *The Causeway* 5 vs 3 in both seats, *Ferrum Crossing*'s East lane 6 vs 5. The sixth does not. On *Ferrum Crossing*, East's **second** Infantry at **(9,5)** reaches West's South objective **(5,7)** in **5 MP** — (9,6)→(8,7)→(7,7)→(6,7)→(5,7), all cost 1, and the axial distance is 5 so no cheaper route exists — **exactly tying** West's 5 MP lane from (1,5). From East's *guided* hex (9,3) the same objective costs 6. So the rule's verdict on the shipped map turns entirely on whether "the opposing seat's Infantry" ranges over that seat's Infantry or only over its `guidedOpening.infantry`. That reading is filed as **Q28**, and T-SCN-11 is written and blocked on it. No map is redrawn here: layout is `scenario-designer`'s lane. |
```
**NEW**
```
| **Q22** | ~~Uncontested vs. merely reachable.~~ **RULED.** The validator asserts non-contention: **the opposing seat's cheapest Infantry route to the same objective must cost strictly more than the owning seat's lane.** T-SCN-07's distinctness clause is a **floor beneath** that requirement, not the whole of it: two seats can name DIFFERENT objectives and still race each other to one of them, which is exactly what a structural check cannot see. Gated as **T-SCN-11** — T-SCN-10 is reserved-but-unwritten for the horizontal mirror and Q26 keeps it that way, so it was not free to take. Original question: §2.13.1 promises the guided lane is "uncontested, not merely reachable," but states it as a property of the shipped map rather than a checkable rule. | T-SCN-07's clause, now a floor; **T-SCN-11**, written, unblocked and asserting since Q28 ruled; §4.11 row 7's priced half, which gains one full-board pass per `guidedOpening` entry | Ruled — and **measured against all three maps before the invariant was written**, which is what the ruling cost and where it paid. Five of the six lanes cleared as drawn: *Longwater March* 8 against 4 in both seats, *The Causeway* 5 against 3 in both seats, *Ferrum Crossing*'s East lane 6 against 5. **The sixth failed on an exact tie**: East's second Infantry at (9,5) reached West's South objective (5,7) in 5 MP against West's own 5. That is the case the rule exists to catch, it was on the map that ships, and every other invariant in the suite passed it. **The map was corrected rather than the rule loosened** (Q28): that Infantry now deploys at (9,1), all six lanes pass, and *Ferrum Crossing* reports **5 against 6 in both seats**. The tie is retained as T-SCN-11's fixture (b) — a failing fixture that was authored rather than constructed. |
```

---

### Edit 8 of 10 — register, **Q28** → RULED (L2003)

Closed in the established pattern — struck question, **RULED**, the ruling first,
the original question retained in full, and the ruling column carrying what it
cost and why the alternative was refused.

**OLD**
```
| **Q28** | Whose Infantry the T-SCN-11 opposing route is measured from. Q22 ruled that the opposing seat's cheapest Infantry route to a guided objective must cost strictly more than the owning seat's lane, but not over which units "cheapest" ranges: **(a)** every CanCapture-row unit that seat deploys — the reading that matches what *contested* means at the table, since either Infantry can race — or **(b)** that seat's own `guidedOpening.infantry` alone, the reading that keeps the comparison lane-against-lane and matches how T-SCN-06 quantifies over a NAMED hex rather than an existential. | **T-SCN-11 outright** — it is written and blocked, in the T-FAME-05 sense. Under reading (a) it also blocks *Ferrum Crossing*'s West guided opening, which ties 5 vs 5 as drawn from the §2.13.2 deployment | **Unruled**, and deliberately carrying no assumption in force — this is the one register row where the conservative reading is not free. The two readings do not merely differ in strictness, they differ in **outcome on the shipped map**: (b) passes all six lanes of all three maps as drawn; (a) refuses *Ferrum Crossing* until either East's second Infantry at (9,5) moves or West's guided objective does, and both are `scenario-designer`'s call. Which way the document already leans is genuinely split: T-SCN-06 was written to quantify over the NAMED hex precisely so a lane nobody walks cannot satisfy a gate, which is (b)'s logic — but the property Q22 protects is a *race*, and a race does not care which Infantry wins it, which is (a)'s. A third option is recorded rather than recommended: rule (a) and accept that *Ferrum Crossing* — the one map that declares `symmetry: none` — needs its guided pair re-chosen, which is a scenario edit, not a rules change. |
```
**NEW**
```
| **Q28** | ~~Whose Infantry the T-SCN-11 opposing route is measured from.~~ **RULED (this revision).** Reading **(a)**: the opposing route is minimised over **any Infantry that seat owns**, not over its `guidedOpening.infantry` alone. Original question: Q22 ruled that the opposing seat's cheapest Infantry route to a guided objective must cost strictly more than the owning seat's lane, but not over which units "cheapest" ranges — **(a)** every CanCapture-row unit that seat deploys, since either Infantry can race, or **(b)** that seat's own `guidedOpening.infantry` alone, which keeps the comparison lane-against-lane and matches how T-SCN-06 quantifies over a NAMED hex rather than an existential. | Nothing further. **T-SCN-11 is unblocked and asserting** (§4.7 Stub 7), and §4.11 row 7 carries it in its acceptance set | Ruled the strict way, knowingly and at a stated price. (b) was available and would have passed the shipped map untouched; it was refused because the property Q22 protects is a **race**, and a race does not care which Infantry wins it. T-SCN-06's named-hex quantifier is not a counter-precedent — it names a hex because the guided lane must be the one turn-1a marks, whereas nothing is marked on the opposing side and the only question is who can arrive. **The cost was one deployment move, not a weakened rule.** East's second Infantry moved **(9,5) → (9,1)** (§2.13.2); no terrain, factory or town count, lane cost, home-factory-empty rule or turn estimate moved with it, and the relocation was **forced rather than chosen** — East's south town (7,6) is 2 hexes from South (5,7), so by the triangle inequality any hex covering that town races that factory, and the only free southern hexes clearing 5 MP were the Artillery's and the Flag Tank's. *Ferrum Crossing* now reports **5 against 6 in both seats** — 1 MP each way, the thinnest margin in the set. The pre-fix **5 against 5** is kept as T-SCN-11's fixture (b): a failing case that was actually authored, that passes every other invariant in the suite, and that reading (b) would have passed. |
```

---

### Edit 9 of 10 — §4.11, row 7 of the build-order table (L2243)

Two corrections. The acceptance cell still says `11 blocked on Q28`. And the cost
claim — "T-SCN-11 costs two … two lookups per guidedOpening entry" — was written
under the narrow reading; under the ruled one the naive figure is one path per
opposing Infantry, but the reverse-Dijkstra form is one **pass** per entry
regardless of unit count. The corrected cell states the cost that is actually
achievable and names the shape that achieves it, rather than a number that is
right only for a two-Infantry deployment.

**OLD**
```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08, 11 all cost a path, and **T-SCN-11 costs two** (both seats' cheapest routes to one objective), so the path budget is two lookups per guidedOpening entry rather than one | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09, 11 (10 reserved-unwritten on Q26; 11 blocked on Q28) |
```
**NEW**
```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08, 11 all cost a path, and **T-SCN-11 costs a full-board pass rather than a path**: it minimises over every Infantry the opposing seat deploys (Q28, ruled), which is **one reverse Dijkstra per `guidedOpening` objective** and is therefore independent of that seat's unit count — done naively as one path per opposing unit it scales with the deployment instead | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09, 11 (10 reserved-unwritten on Q26) |
```

---

### Edit 10 of 10 — §4.11's closing paragraph, the row-7 sentences (L2252–2259)

Only the T-SCN-11 sentences change; the row-7 straddle argument before them and
the Q20 row-10 split after them are untouched and are not reproduced. The
paragraph currently tells a reader that row 7 cannot close because an invariant
is blocked, which is now false and is exactly the kind of stale blocker that
gets a row scheduled wrongly.

**OLD**
```
lane — price a Stub-3 path, so row 7 cannot *close* until row 3 does. T-SCN-11
(Q22, ruled) is the newest of the four and the most expensive: it prices a
*second* path per seat — the opposing seat's cheapest route to the same
objective — so row 7's path budget is two lookups per `guidedOpening` entry
rather than one. Its *dependency* is settled even though its *assertion* is not:
the invariant is written and blocked on **Q28**, which asks whose Infantry the
opposing route starts from and which, under its stricter reading, refuses
*Ferrum Crossing* as drawn (§4.7). Row 7 is
```
**NEW**
```
lane — price a Stub-3 path, so row 7 cannot *close* until row 3 does. T-SCN-11
(Q22 and Q28, both ruled) is the newest of the four and the most expensive: it
prices the *opposing* seat's cheapest route to the same objective, minimised
over every Infantry that seat deploys, which is one reverse Dijkstra per
`guidedOpening` objective — a full-board pass rather than a path, and one whose
cost does not grow with the deployment. It **asserts**, as of this revision:
nothing in row 7 is written-and-blocked, and the only unwritten invariant is
T-SCN-10, reserved on Q26. It ships with a **failing** fixture — the shipped
map's own pre-fix deployment, which tied 5 against 5 — so this row's suite
proves it can refuse a real scenario and not merely agree with the repo. Row 7 is
```

---

## Build order

Unchanged in shape. Row 7's marginal cost is restated in the form the ruling
made correct, and its acceptance set is now unblocked. Deltas in bold.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 1 | Hex grid & math (Stub 1) | — (Q1 pins bounds) | Yes | T-HEX-01..07 |
| 2 | Data tables (§4.8) | — (MoveClass blocked on Q2) | Loader yes; import parity in-editor | T-DATA-01..06 |
| 3 | Movement & pathfinding (Stub 3) | 1, 2 | Yes | T-MOVE-01..06 |
| 4 | Capture & Fame economy (Stub 4) | 3 | Yes | T-FAME-01..09 |
| 5 | Turn loop & win/tiebreak (Stub 5) | 4 + Combat @ `5ffa8d6` | Yes | T-TURN-01..09 |
| 6 | Opponent AI (Stub 6) | 5 | Yes | T-AI-01..06 + self-play smoke |
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; 3 for the priced half — T-SCN-04, 06, 08, 11; **T-SCN-11 is one reverse Dijkstra per objective, not one path per opposing unit** | Yes; MCP wraps it, manual fallback stands | **T-SCN-01..09, 11 — no blocked invariant** (10 reserved-unwritten, Q26) |
| 8 | UI binding (Stub 8) | 5, 7 | Contract + queries yes; widgets in-editor | T-UI-01..04 |
| 9 | Presentation bridge — §4.9 | Rows 1–5 | Source/compile gates yes | T-INT-01..05 |
| 10 | Save & replay — §4.10 | 4, 5, 7; format itself has no deps — wk 2, per Q20 | Yes, all but slot I/O | T-SAVE-01..06 from wk 2; T-SAVE-07 closes wk 4; slot I/O wk 5 |

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.2, "Asymmetry and its handicap story" (L1022–1029) | "If §4.1 self-play shows either seat above ~55% win rate, the corrective is the existing §2.9 dial — a per-seat starting-Fame offset — never a terrain rework. This is also the replay lever: the two seats are two different deterministic puzzles (see 2.13.4)." appears **twice in succession**, once with slightly different line breaks | Delete the second occurrence (the sentences beginning "If §4.1 self-play shows either seat above ~55%" at the end of the paragraph). Owner: `scenario-designer` / Director at merge | A merge artefact, not a design question — it is a verbatim duplication inside one paragraph. Flagged rather than edited: §2.13 is not my file. |
| §2.13.2 / §2.13.1 — the two change requests filed in post-merge-6 | "each seat is closer to a different neutral factory"; §2.13.1 fact 3's "the first lesson is not a race" | **No action — both are resolved** by the deployment fix and the §2.13.1 rewrite. East now measures 5 to North against 6 to South, so the asymmetry claim is true as stated and priced; fact 3 now carries the measured inequality and names the (9,5) tie as the reason the deployment reads (9,1) | Recorded so the Director does not carry two closed requests forward. |

## Open questions for the Director

**No new questions. The register still runs Q1–Q28** and no ID was taken.

Three things I checked specifically for a gap and found none worth filing:

- **T-SCN-07's clause.** It already reads as a floor beneath T-SCN-11 and says
  so in the merged text (L1773–1781), including the sentence about two seats
  naming different objectives and still racing. No edit; Q22's row now says the
  same thing in one line so the register does not have to be read against the
  stub to learn it.
- **Q21's flagged rationale.** Re-measured, not assumed. It holds — (9,1) sits
  on none of the ten routes *Ferrum Crossing* prices — so it is kept and dated
  rather than rewritten. Its **Blocks** column was the stale part and is fixed
  (edit 6). Not a rule gap: a citation gap.
- **The reverse-Dijkstra identity.** It follows from Q21's terrain-only pricing
  and needs no new ruling; it is stated as implementation, not as rule.

One residual measurement, flagged as a known limit rather than a question: I
re-derived all ten *Ferrum Crossing* routes, and I did **not** re-price the two
stretch maps' opposing routes under an occupancy reading — their guided lanes
were already established as clear (Q21's row) and their margins are 4 MP and
2 MP, but "no unit sits on any priced route" is asserted in edit 6 for the
shipped map only, which is exactly as far as I checked.

## Handoffs

- **Director:** apply the ten pairs. Edits 1–4 are one contiguous region of
  Stub 7 and should land together; edit 3 is an insert with its OLD lines
  reproduced unchanged. Nothing in `../stratocracy-content/kb/rules.md` parses
  §4, so no KB re-sync is triggered by this draft — the §2.13.2 duplication in
  the change-request table would trigger it if you fix it in the same pass.
- **`scenario-designer`:** the fix verified clean against my own derivation of
  all eight routes, and the two change requests I filed in post-merge-6 are
  closed by it. One item left in your lane: the duplicated paragraph at
  §2.13.2's asymmetry note. Also worth carrying forward — the North lane's 1 MP
  margin is bought by the Woods ring and the single northern crossing, so any
  future edit to rows 0–3 of that map collapses it the same way (9,5) collapsed
  the South one.
- **`rules-designer`:** nothing. No rule, cost, Fame figure or unit stat moves.
- **`ux-onboarding-designer`:** the warning from post-merge-6 is withdrawn. The
  turn-2 directive on the shipped map is no longer walking a first-time player
  into a contested tile: West's South lane is 5 MP against East's cheapest 6,
  and player-first IGOUGO (§2.1) means the shared arrival turn goes to the
  player. The margin is 1 MP, so the guidance copy should not promise more than
  "you get there first" — it does not buy a turn on this map, and §2.13.1 now
  says so explicitly.
- **`continuity-gate`:** three checks that are cheap and decisive. (1) Q28
  appears as RULED once and no longer in the *unruled* list; the list should
  read Q4, Q5, Q6, Q8, Q9. (2) No surviving §4 text says T-SCN-11 is blocked —
  the four sites were L1898, L1911–1912, L2243, L2257. (3) The two decisive
  routes are re-derivable from §2.13.2's ASCII map: East (9,3)→(9,4)(8,5)(8,6)
  (7,7)(6,7)(5,7) = 6 against West (1,5)→(2,6)(3,6)(3,7)(4,7)(5,7) = 5, and
  West (1,3)→(2,3)(3,2)(4,2)(4,1)(5,1)(6,2) = 6 against East (9,3)→(8,3)(7,3)
  (6,3)(6,2) = 5. Fixture (b) is the pre-fix (9,5) route and must remain
  described as failing.

## Grounding

| Claim | Source |
|---|---|
| Current Stub 7 text: T-SCN-11's header, its three asymmetries with (iii) still blocked, the "Reported like T-SCN-08" lines, Determinism and Acceptance | `source/gdd.md` L1854–1915 (md5 `3d9d2700de278f29c473d8e9059c058d`) |
| T-SCN-07 already describes distinctness as a floor and names T-SCN-11 as the asserting gate | L1768–1781 — checked, no edit needed |
| T-SCN-10 reserved and unwritten, blocked on Q26 | L1845–1853; register Q26, L2001 |
| Open-questions preamble, the Q28 exception paragraph and the *unruled* list | L1950–1972 |
| Register rows Q21, Q22, Q28 as currently merged | L1996, L1997, L2003 |
| §4.7's register extent is already de-pinned ("the single place their extent is stated") | L1455–1458 — nothing to do per the de-pinning instruction |
| §4.11 row 7 and the closing paragraph's blocked-on-Q28 sentences | L2243, L2248–2271 |
| *Ferrum Crossing* 11×9 layout, key coordinates, terrain distribution, and the corrected deployment with East Infantry at (9,3) and **(9,1)** | §2.13.2 L885–916 |
| §2.13.2's eight-route table and its 5-against-6 verdict in both seats | L925–945 |
| The forced-relocation argument: (7,6) is 2 hexes from (5,7); only (10,5) and (10,4) clear 5 MP in East's southern quarter | §2.13.2 L958–970 |
| §2.13.1 fact 3 as rewritten: the measured inequality over **every** Infantry, the (9,5) tie named as the reason for (9,1), and "does not buy a turn" on the shipped map | L769–809 |
| *The Causeway* 3-against-5 and *Longwater March* 4-against-8 | §2.13.1 L775–776 |
| Terrain move costs; Water not land-passable | §2.3 table |
| Odd-r → axial `q = col − (row − (row & 1))/2` and the axial metric | §4.7 shared conventions, L1462–1466 |
| Every MP figure in the Draft's re-derivation table | Derived by me from the §2.13.2 layout and §2.3 costs; each path and each axial floor is written out so it can be checked rather than trusted. Reproduces §2.13.2 and the Director's independent Dijkstra run cell for cell |
| The reverse-Dijkstra identity `d(h) = min over n of (MoveCost(n) + d(n))`, `d(objective) = 0` | Standard shortest-path formulation on the reversed graph; sound here only because Q21 (L1996) excludes occupancy, making the graph static |
| Combat @ `5ffa8d6` remains the only gate-verified system; every row this draft touches is still `*pending*` | §3 provenance ledger; §4.11 preamble L2229–2233 |
| §2.13.2's duplicated asymmetry sentences | L1022–1029 |
