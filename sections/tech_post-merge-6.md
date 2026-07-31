> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-6 draft (tech-director)

## Placement

Thirteen exact edits, all inside §4, in two groups:

- **Q20 (save/replay milestone split)** — §4.4's milestone table (weeks 2, 4, 5)
  and the note under it; §4.11's row-7 line and closing paragraph; the register's
  Q20 row; the open-questions preamble's *unruled* list.
- **Q22 (non-contention)** — §4.7 Stub 7's T-SCN-07 tail, a new **T-SCN-11**, the
  stub's Determinism and Acceptance lines; §4.11's row-7 table row; the
  register's Q22 row and one new row, **Q28**.

Plus one de-pinning of §4.7's preamble extent, per instruction.

No map, lane number, terrain count or dimension is changed anywhere. Capture
N = 1 remains an assumption in force under Q4.

---

## Draft

### Q20 — what the split actually turns on

The Director adopted §4.11's own recommendation, so there is no argument left to
make; there is only a distinction to write down once so the table stops drifting:

> **A format is a test instrument. Slot I/O is a feature.**

The §4.10 format and headless replayer are consumed by two gates that run before
any player ever saves a game — T-INT-02 (whose input *file* is a save) in week 2,
and T-SAVE-07 (whose self-play logs *are* saves) in week 4. Neither needs a save
button, a slot, a `USaveGame` wrapper, or an overwrite-confirm dialog. Those are
the week-5 half, and they are the only half a player sees.

This composes with Q23 rather than fighting it. Q23 moved the vertical slice
*later* because a milestone claimed a system its dependencies could not have
delivered. Q20 moves the format *earlier* because a gate needed an instrument the
schedule had parked behind it. Same principle, opposite direction: **each piece
lands in the week the thing that consumes it runs.**

Week 2 now carries presentation, UI wiring, move, attack, scenario
load/validate/render, and the save format + replayer. That is a full week, but
the format is roughly a day of headless work with no engine dependency — §4.10 is
already fully specified, eight header fields plus a command log plus a canonical
state hash whose field order §4.10 fixes — and the replayer is `loadScenario`
+ re-apply the log. The **Move + attack only** fence from Q23 is untouched:
nothing in this split adds a rules system to week 2.

---

### Q22 — the measurement, before the invariant

The Director asked for the rule to be measured against all three shipped maps
before it was written. It was. **One lane fails**, and the failure is not
marginal-and-arguable — it is an exact tie, on the map that ships.

All costs below are Stub-3 cheapest paths under the pricing T-SCN-06 already
uses: terrain alone, occupancy excluded (Q21, ruled), cost counting **every hex
entered including the objective**, Water land-impassable, odd-r adjacency per
§2.13.1. Bridges are *allowed* on the opposing route — see the invariant text for
why, and note that on these three maps that choice changes no verdict. Each
figure is checked against its axial distance floor
(`q = col − (row − (row & 1))/2`, §4.7) so "cheapest" means proven, not found.

**Owning-seat lanes** are §2.13.1's table, unchanged and re-verified.

#### Ferrum Crossing (11 × 9) — West objective **South (5,7)**

| Seat | From | Path | Cost |
|---|---|---|---|
| **West (owning)** | (1,5) | (2,6) → (3,6) → (3,7) → (4,7) → **(5,7)** | **5 MP** (all cost 1) |
| East, `guidedOpening.infantry` | (9,3) | (9,4)*F* → (8,5) → (8,6) → (7,7) → (6,7) → **(5,7)** | **6 MP** |
| **East, second Infantry** | **(9,5)** | **(9,6) → (8,7) → (7,7) → (6,7) → (5,7)** | **5 MP** |

Every hex on that East route is Plains except the objective (Factory, cost 1).
The axial floor confirms it is optimal, not merely found: (9,5) → axial (7,5);
(5,7) → axial (2,7); Δq = −5, Δr = +2, Δq+Δr = −3, so distance = (5+2+3)/2 = **5**,
and a 5-cost path exists. West's own lane sits on the same floor: (1,5) → axial
(−1,5), Δq = 3, Δr = 2, distance = (3+2+5)/2 = 5. Neither seat can do better.

**5 is not strictly longer than 5. This lane fails the ruled rule** — under the
reading where "the opposing seat's Infantry" means any of that seat's Infantry.
It passes 6 vs 5 under the reading where it means only that seat's own
`guidedOpening.infantry`.

Per instruction I am stopping here rather than redrawing: *Ferrum Crossing*'s
deployment is `scenario-designer`'s lane. The reading is filed as **Q28**.

#### Ferrum Crossing — East objective **North (6,2)**

| Seat | From | Path | Cost |
|---|---|---|---|
| **East (owning)** | (9,3) | (9,2) → (8,2) → (7,2)*w* → **(6,2)** | **5 MP** (4 hexes, one Woods) |
| **West, cheapest** | (1,3) | (2,3) → (3,2) → (3,1)*T* → (4,1) → (5,1)*B* → **(6,2)** | **6 MP** |
| West, `guidedOpening.infantry` | (1,5) | (2,4) → (2,3) → (3,2) → (3,1)*T* → (4,1) → (5,1)*B* → **(6,2)** | **7 MP** |

**6 > 5. Passes, by exactly 1 MP.** The margin is thin and it is the river doing
the work: the only northern crossing is the Bridge at (5,1), (5,1) is adjacent to
(6,2), and `dist((1,3),(5,1)) = 5`, so West's floor is 5 + 1 = 6 and it is met.
Any map edit that adds a second northern crossing collapses this lane toward a
tie as well — worth knowing before anyone edits row 0–3 of the shipped map.

#### Longwater March (13 × 8) — both objectives

| Seat | From | Path | Cost |
|---|---|---|---|
| **West (owning)** → (4,1) | (1,2) | §2.13.1's lane | **4 MP** |
| East, cheapest → (4,1) | (11,3) | (11,2) → (10,1) → (9,1) → (8,1)*F* → (7,1) → (6,1) → (5,1) → **(4,1)** | **8 MP** |
| **East (owning)** → (8,6) | (11,5) | §2.13.1's lane | **4 MP** |
| West, cheapest → (8,6) | (1,4) | (1,5) → (2,6) → (3,6) → (4,6)*F* → (5,6) → (6,6) → (7,6) → **(8,6)** | **8 MP** |

**8 > 4 both seats. Passes with 4 MP of margin.** The fourth row is the ρ-image
of the second under ρ(c,r) = (12−c, 7−r) — ρ(11,3) = (1,4), ρ(4,1) = (8,6) — but
it is listed as a *measured* path, not inferred from the declared flag, per
T-SCN-08's standing rule. The two agreeing is the outcome, not the method.

#### The Causeway (9 × 8) — both objectives

| Seat | From | Path | Cost |
|---|---|---|---|
| **West (owning)** → (3,2) | (1,2) | (1,1)*T* → (2,1) → **(3,2)** | **3 MP** |
| East, cheapest → (3,2) | (7,3) | (6,3) → (6,2) → (5,2) → (4,2)*B* → **(3,2)** | **5 MP** |
| **East (owning)** → (5,5) | (7,5) | §2.13.1's lane | **3 MP** |
| West, cheapest → (5,5) | (1,4) | (2,4) → (2,5) → (3,5) → (4,5)*B* → **(5,5)** | **5 MP** |

**5 > 3 both seats. Passes.** This is the map where the Bridge question bites:
with Bridges *excluded* from the opposing route, column 4's full bisection makes
both opposing routes non-existent and both lanes pass vacuously. Allowing Bridges
is the stricter reading and still passes at 5 vs 3, so strictness is free here
and is what T-SCN-11 states.

#### Summary

| Map | Objective | Owning | Opposing — any Infantry | Opposing — guided only | Verdict (a) / (b) |
|---|---|---|---|---|---|
| *Ferrum Crossing* | South (5,7), West | 5 | **5** | 6 | **FAIL on tie** / pass |
| *Ferrum Crossing* | North (6,2), East | 5 | 6 | 7 | pass / pass |
| *Longwater March* | (4,1), West | 4 | 8 | ≥ 9 | pass / pass |
| *Longwater March* | (8,6), East | 4 | 8 | ≥ 9 | pass / pass |
| *The Causeway* | (3,2), West | 3 | 5 | ≥ 6 | pass / pass |
| *The Causeway* | (5,5), East | 3 | 5 | ≥ 6 | pass / pass |

The two `≥` figures are axial distance floors, quoted as bounds because the exact
cost is not needed: both already exceed the owning lane, so refining them cannot
change a verdict. Every figure that *can* change a verdict is an exact measured
path above.

Five of six clear under either reading. The sixth is the whole question, and it
is on the map that ships.

One collateral finding, for the Director and `scenario-designer` rather than for
me: §2.13.2 says *"each seat is closer to a different neutral factory"* and
*"West's fast prize is South; East's is North."* Measured, West is 5 MP to South
and 6 to North — the claim holds for West. **East is 5 to North and 5 to South —
it is equidistant.** The seat asymmetry that map's handicap story rests on is
one-sided as drawn. That is a §2.13 prose claim, not a §4 gate, so it is filed as
a change request rather than edited.

---

## The edits

### Edit 1 of 13 — §4.4, week 2 (L1273)

The format and replayer join week 2. The Q23 fence — move + attack only — is
restated unchanged so the addition cannot be read as smuggling a rules system in.

**OLD**
```
| 2 | Engine presentation + UI wiring (select/move/attack) onto the wk-1 skeletons, plus the one scenario loading, validating and rendering. **Move + attack only** — no capture, no production, no AI opponent. |
```
**NEW**
```
| 2 | Engine presentation + UI wiring (select/move/attack) onto the wk-1 skeletons, plus the one scenario loading, validating and rendering, **and the §4.10 save/replay format + headless replayer** (Q20, ruled). The format is a *test instrument*, not a feature: T-INT-02's input file is a save, so the week-2 integration gate cannot run without it — and neither can the week-4 self-play logs (T-SAVE-07). No save button, slot, or `USaveGame` wrapper here; those are week 5. **Move + attack only** — no capture, no production, no AI opponent. |
```

---

### Edit 2 of 13 — §4.4, week 4 (L1275)

The second consumer of the week-2 format. This edit is the most droppable of the
three table edits — the split survives without it — but naming T-SAVE-07 where it
actually closes is what stops week 5 quietly re-absorbing the format next
revision.

**OLD**
```
| 4 | Self-play balance sims and tuning; scenario polish (additional scenarios only as stretch). |
```
**NEW**
```
| 4 | Self-play balance sims and tuning — every match emitted in the wk-2 §4.10 format, so **T-SAVE-07 (harness compatibility) closes here**, not in wk 5: one format, no dialect drift between a save and a balance log; scenario polish (additional scenarios only as stretch). |
```

---

### Edit 3 of 13 — §4.4, week 5 (L1276)

Week 5 keeps the half a player can see. Rewording is required, not cosmetic:
"save/load" as written now describes work that finished three weeks earlier.

**OLD**
```
| 5 | UI polish, feedback/juice, save/load, onboarding. |
```
**NEW**
```
| 5 | UI polish, feedback/juice, **the save-slot UI and its slot I/O** — the §4.10 format and headless replayer landed in wk 2 (Q20), so what remains here is the player-facing surface only: the single `slot0` file, the `USaveGame` wrapper, and whatever §2.11 decides about overwrite-confirm (§4.10 records that surface as unowned); onboarding. |
```

---

### Edit 4 of 13 — §4.4, the Q23 note's closing sentence (L1280)

Q20 is no longer open, and the note under the table is where a reader learns how
the two rulings relate. Replacing the final sentence only; the rest of the
paragraph is Q23's and stands.

**OLD**
```
The save/replay half of the same question (**Q20**) is still open.
```
**NEW**
```
**The save/replay half of the same question (Q20) is now ruled — and split rather than moved.** The §4.10 *format and headless replayer* go to **week 2**, where T-INT-02 needs a save file as its input, and are therefore in hand by **week 4** for the self-play logs T-SAVE-07 validates; only the **save-slot UI and slot I/O** stay in week 5. The two rulings run on one principle in opposite directions: each piece lands in the week the thing that consumes it runs, so a milestone that outran its dependencies moved *later* (Q23) and an instrument its own gates outran moved *earlier* (Q20). Stated once, so the table stops drifting: **a format is a test instrument; slot I/O is a feature.**
```

---

### Edit 5 of 13 — §4.7 preamble, de-pinning the register extent (L1337–1339)

Per instruction. This extent has gone stale on every revision that added a
question, and this draft adds one; naming Q28 here would only reset the clock.

**OLD**
```
state, the gate is parameterized on a numbered open question (Q1–Q27, Open
questions below) — the Director rules, the gate then pins the ruling.
```
**NEW**
```
state, the gate is parameterized on a numbered open question — the Director
rules, the gate then pins the ruling. The register below is the single place
their extent is stated; nothing else in this document names a range of them,
because every range named elsewhere has gone stale within a revision.
```

---

### Edit 6 of 13 — Stub 7, T-SCN-07's closing clause (L1654–1657)

T-SCN-07 keeps its structural check and its rows-1–2 placement. Only the sentence
disclaiming non-contention changes: the property is now ruled and gated next
door, and distinctness is explicitly demoted to a floor.

**OLD**
```
            entries name DIFFERENT objectives — §2.13.1's "the seat's own
            neutral," gated at its distinctness floor. The stronger
            non-contention property §2.13.1 also claims is unruled (Q22) and
            nothing here asserts it.
```
**NEW**
```
            entries name DIFFERENT objectives — §2.13.1's "the seat's own
            neutral," gated at its distinctness floor. Distinctness is now
            exactly that: a FLOOR, not the requirement. The stronger
            non-contention property §2.13.1 claims is RULED (Q22) and is
            asserted by T-SCN-11, which prices a path and therefore lands
            with row 3 rather than with this check. Two seats can name
            DIFFERENT objectives and still race each other to one of them —
            which is what T-SCN-11 exists to refuse and what this invariant,
            being structural, cannot see.
```

---

### Edit 7 of 13 — Stub 7, T-SCN-11 + Determinism + Acceptance (L1727–1738)

One pair, because the new invariant, the determinism line that must now cover its
path costs, and the acceptance line that must now list it are contiguous. The
T-SCN-10 reserved block is reproduced verbatim and unchanged — Q26 keeps it
unwritten, so T-SCN-11 takes the next free ID rather than a claim on it.

Cost, stated the way T-SCN-06 states its own: T-SCN-11 prices a **second** Stub-3
path per `guidedOpening` entry, so row 7's path budget goes from one lookup per
entry to two. It belongs with the priced half and inherits Stub 3's dependency
and determinism, exactly as T-SCN-04/06/08 do.

**OLD**
```
   permutation: it sends (dq, dr) to (dq+dr, -dr), which permutes the three
   terms of the axial metric and leaves the distance unchanged. Blocked on Q26;
   no gate is written until the schema admits the value.)
Determinism: pure parse + validation; any failure refuses the whole file with a
         reason. scenarioHash is platform-stable by canonical ordering. The
         T-SCN-06/08 lane costs are Stub-3 path costs and inherit its
         determinism (T-MOVE-04's canonical tie-break, T-MOVE-06), so the
         reported integers reproduce across runs and compilers.
Acceptance: T-SCN-01..09 headless. The §4.2 validate_scenario MCP tool wraps the
         same checks in-editor for the Content agent; its manual fallback is
         running the headless validator on the exported file (MCP stays off the
         critical path, §3 guardrails).
```
**NEW**
```
   permutation: it sends (dq, dr) to (dq+dr, -dr), which permutes the three
   terms of the axial metric and leaves the distance unchanged. Blocked on Q26;
   no gate is written until the schema admits the value.)
  T-SCN-11  NON-CONTENTION (Q22, ruled): for EACH guidedOpening entry, the
            OPPOSING seat's cheapest land path to that same `objective` costs
            STRICTLY MORE MP than the owning seat's lane, as reported by
            T-SCN-08. This is the gate for §2.13.1's "uncontested, not merely
            reachable" — a promise that until now was a property of the drawn
            map rather than a checkable rule.
            Both sides of the comparison are priced IDENTICALLY, which is what
            makes the inequality mean anything: Stub-3 cheapest path, terrain
            alone with occupancy excluded (Q21, ruled), cost counting every
            hex entered INCLUDING the objective (Factory MoveCost 1) — the
            T-MOVE-01 accounting T-SCN-06 already uses, so the validator
            cannot price the two routes two different ways.
            EQUALITY FAILS. "Strictly longer" is the ruled comparison, and a
            tie is precisely the race the rule exists to forbid; a >= would
            pass the one lane in the shipped set that a human would call
            contested.
            Three asymmetries with T-SCN-06 are deliberate:
              (i)   NO CEILING. T-SCN-06 is a budget (<= 2 x Move). This is a
                    comparison: the opposing route may cost anything at all,
                    it must merely cost MORE.
              (ii)  BRIDGES ARE ALLOWED on the opposing route. T-SCN-06's
                    Bridge-free clause is a property of the GUIDED lane —
                    what makes the first lesson a walk rather than a
                    crossing — not a constraint the enemy is under.
                    Excluding Bridges would make the opposing route
                    NON-EXISTENT on a bisected map (The Causeway, §2.13.6)
                    and pass that map vacuously, so allowing them is the
                    STRICTER reading and it is the one asserted. Measured, it
                    costs nothing: The Causeway passes 5 against 3 in both
                    seats with the crossing permitted, and no other map in
                    the set has a Bridge on any opposing route.
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
            Reported like T-SCN-08: a refusal carries BOTH measured integers,
            owning and opposing, so an author reads "5 against 5" rather than
            "contested" — and a map edit that shortens an enemy approach
            surfaces as a changed number, not a still-green boolean.
Determinism: pure parse + validation; any failure refuses the whole file with a
         reason. scenarioHash is platform-stable by canonical ordering. The
         T-SCN-06/08/11 lane costs are Stub-3 path costs and inherit its
         determinism (T-MOVE-04's canonical tie-break, T-MOVE-06), so the
         reported integers reproduce across runs and compilers. T-SCN-11
         compares two such integers and introduces no new source of
         nondeterminism.
Acceptance: T-SCN-01..09 and T-SCN-11 headless (10 reserved-unwritten on Q26;
         11 blocked on Q28). The §4.2 validate_scenario MCP tool wraps the
         same checks in-editor for the Content agent; its manual fallback is
         running the headless validator on the exported file (MCP stays off the
         critical path, §3 guardrails).
```

---

### Edit 8 of 13 — the open-questions preamble (L1773–1789)

Three changes in one paragraph: Q28 joins the enumeration, **Q20 leaves the
*unruled* list**, and the "conservative reading" convention gains its one stated
exception — because Q28 is the first row where the conservative reading is not
free, and glossing that would misrepresent why it carries no assumption.

**OLD**
```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and
scenario-side rulings folded in here (Q14–Q20), the two gaps found while
gating §2.13.1's opening-capture invariant (Q21–Q22), the milestone
contradiction the document knowingly carries (Q23), the two raised by the
§2.13 symmetry correction (Q24–Q25), and the one raised by correcting that
correction (Q26), and the guided opening's one input-gating constraint (Q27)
— so that each question
carries exactly one ID across the whole document. Each blocks the gate named beside it;
the Director writes the rule, the gate then pins it. The last column is not
uniform, and the difference matters: **where a reading is stated, it is the
conservative one, and it is what ships and what the gates assert** — chosen so
that a later ruling loosens behavior rather than invalidating a passing gate.
**Rows marked *unruled* state no reading and block their gate outright** (Q4's
interruption semantics, Q5's stacking, Q6, Q8, Q9's target- and build-choice
ties, and Q20); those gates and milestones cannot be settled until the
Director answers.
```
**NEW**
```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and
scenario-side rulings folded in here (Q14–Q20), the two gaps found while
gating §2.13.1's opening-capture invariant (Q21–Q22), the milestone
contradiction the document knowingly carries (Q23), the two raised by the
§2.13 symmetry correction (Q24–Q25), the one raised by correcting that
correction (Q26), the guided opening's one input-gating constraint (Q27), and
the reading the Q22 ruling exposed the moment its new invariant was measured
against the shipped map (Q28)
— so that each question
carries exactly one ID across the whole document. Each blocks the gate named beside it;
the Director writes the rule, the gate then pins it. The last column is not
uniform, and the difference matters: **where a reading is stated, it is the
conservative one, and it is what ships and what the gates assert** — chosen so
that a later ruling loosens behavior rather than invalidating a passing gate.
**Q28 is the one row where that convention does not hold**, and it is marked
unruled for exactly that reason: its conservative reading REFUSES A SHIPPED
MAP, so no reading could be stated there without either blocking *Ferrum
Crossing* or quietly weakening a rule the Director had just made.
**Rows marked *unruled* state no reading and block their gate outright** (Q4's
interruption semantics, Q5's stacking, Q6, Q8, Q9's target- and build-choice
ties, and Q28); those gates and milestones cannot be settled until the
Director answers.
```

---

### Edit 9 of 13 — register, Q20 → RULED (L1812)

Struck question + **RULED** + original text retained, per Q7 and Q23. The Blocks
column stays populated rather than dashed, matching Q23: the two gates it always
named are now the *reason* for the placement rather than its casualties.

**OLD**
```
| **Q20** | Save/replay milestone split. §4.11 shows §4.4's week-5 save/load placement is one week late in one respect: the format and headless replayer are the instrument for the week-2 integration gate (T-INT-02) and the week-4 self-play logs (T-SAVE-07). Split the row — format + replayer early, save-slot UI stays week 5? | §4.4's milestone table; T-INT-02 and T-SAVE-07 sequencing | Unruled. §4.4 stands as written; §4.11 records the conflict without resolving it. This is a scheduling decision, adjacent to **Q23**. |
```
**NEW**
```
| **Q20** | ~~Save/replay milestone split.~~ **RULED (this revision).** The row is **split, not moved**: the §4.10 **format + headless replayer** land in **week 2**, and only the **save-slot UI and slot I/O** stay in week 5. Original question: §4.11 showed §4.4's week-5 save/load placement was one week late in one respect — the format and headless replayer are the instrument for the week-2 integration gate (T-INT-02) and the week-4 self-play logs (T-SAVE-07). Split the row? | §4.4's milestone table; T-INT-02 and T-SAVE-07 sequencing | Ruled, as §4.11 itself proposed. §4.4's weeks 2, 4 and 5 and the note under the table now describe one schedule, and the distinction the split turns on is stated there rather than left to be re-derived: **a format is a test instrument** and ships with the gates that consume it (T-INT-02 wk 2, T-SAVE-07 wk 4); **slot I/O is a feature** and ships with the rest of the UI. Scheduling-adjacent to **Q23** and ruled on the same principle in the opposite direction — a milestone that outran its dependencies moved later; an instrument its own gates outran moved earlier. |
```

---

### Edit 10 of 13 — register, Q22 → RULED (L1814)

The rule, the demotion of T-SCN-07's clause to a floor, the gate ID, and the
measurement — including the one lane that fails, which is the part a ruling row
must not omit.

**OLD**
```
| **Q22** | Uncontested vs. merely reachable. §2.13.1 promises the guided lane is "uncontested, not merely reachable," but states it as a property of the shipped map rather than a checkable rule. Is *distinct objectives per seat* the whole requirement, or must the validator also assert non-contention — e.g. the opposing seat's cheapest Infantry lane to the same objective is strictly longer? | Whether T-SCN-07's distinctness clause is the floor or a further T-SCN invariant is owed | Distinctness only, as gated in T-SCN-07. Consequence stated plainly: a map can pass every §2.13 gate and still hand both seats a race to the same tile, turning the first lesson into a contest. |
```
**NEW**
```
| **Q22** | ~~Uncontested vs. merely reachable.~~ **RULED (this revision).** The validator asserts non-contention: **the opposing seat's cheapest Infantry route to the same objective must cost strictly more than the owning seat's lane.** T-SCN-07's distinctness clause is now a **floor beneath** that requirement, not the whole of it. Gated as **T-SCN-11** — T-SCN-10 is reserved-but-unwritten for the horizontal mirror and Q26 keeps it that way, so it was not free to take. Original question: §2.13.1 promises the guided lane is "uncontested, not merely reachable," but states it as a property of the shipped map rather than a checkable rule. | T-SCN-07's clause, now a floor; the new **T-SCN-11**; §4.11 row 7's priced half, whose path budget doubles to two lookups per guidedOpening entry | Ruled — and **measured against all three maps before the invariant was written**, which is what the ruling cost. Five of the six lanes clear it outright: *Longwater March* 8 vs 4 in both seats, *The Causeway* 5 vs 3 in both seats, *Ferrum Crossing*'s East lane 6 vs 5. The sixth does not. On *Ferrum Crossing*, East's **second** Infantry at **(9,5)** reaches West's South objective **(5,7)** in **5 MP** — (9,6)→(8,7)→(7,7)→(6,7)→(5,7), all cost 1, and the axial distance is 5 so no cheaper route exists — **exactly tying** West's 5 MP lane from (1,5). From East's *guided* hex (9,3) the same objective costs 6. So the rule's verdict on the shipped map turns entirely on whether "the opposing seat's Infantry" ranges over that seat's Infantry or only over its `guidedOpening.infantry`. That reading is filed as **Q28**, and T-SCN-11 is written and blocked on it. No map is redrawn here: layout is `scenario-designer`'s lane. |
```

---

### Edit 11 of 13 — register, new row Q28 (insert after Q27)

The gap the ruling exposed. Filed at the next free ID rather than decided here,
per instruction.

**OLD**
```
§2.11.6-B's turn-1 row gains a footnote. |

### 4.8 Data contract — DataTable schemas
```
**NEW**
```
§2.11.6-B's turn-1 row gains a footnote. |
| **Q28** | Whose Infantry the T-SCN-11 opposing route is measured from. Q22 ruled that the opposing seat's cheapest Infantry route to a guided objective must cost strictly more than the owning seat's lane, but not over which units "cheapest" ranges: **(a)** every CanCapture-row unit that seat deploys — the reading that matches what *contested* means at the table, since either Infantry can race — or **(b)** that seat's own `guidedOpening.infantry` alone, the reading that keeps the comparison lane-against-lane and matches how T-SCN-06 quantifies over a NAMED hex rather than an existential. | **T-SCN-11 outright** — it is written and blocked, in the T-FAME-05 sense. Under reading (a) it also blocks *Ferrum Crossing*'s West guided opening, which ties 5 vs 5 as drawn from the §2.13.2 deployment | **Unruled**, and deliberately carrying no assumption in force — this is the one register row where the conservative reading is not free. The two readings do not merely differ in strictness, they differ in **outcome on the shipped map**: (b) passes all six lanes of all three maps as drawn; (a) refuses *Ferrum Crossing* until either East's second Infantry at (9,5) moves or West's guided objective does, and both are `scenario-designer`'s call. Which way the document already leans is genuinely split: T-SCN-06 was written to quantify over the NAMED hex precisely so a lane nobody walks cannot satisfy a gate, which is (b)'s logic — but the property Q22 protects is a *race*, and a race does not care which Infantry wins it, which is (a)'s. A third option is recorded rather than recommended: rule (a) and accept that *Ferrum Crossing* — the one map that declares `symmetry: none` — needs its guided pair re-chosen, which is a scenario edit, not a rules change. |

### 4.8 Data contract — DataTable schemas
```

---

### Edit 12 of 13 — §4.11, row 7 of the build-order table (L2059)

T-SCN-11 joins the priced half, and the row records that it is the expensive one.

**OLD**
```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09 |
```
**NEW**
```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07, 09); **3 for the priced half** — T-SCN-04, 06, 08, 11 all cost a path, and **T-SCN-11 costs two** (both seats' cheapest routes to one objective), so the path budget is two lookups per guidedOpening entry rather than one | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..09, 11 (10 reserved-unwritten on Q26; 11 blocked on Q28) |
```

---

### Edit 13 of 13 — §4.11's closing paragraph (L2064–2078)

One pair, because both rulings land in this paragraph: the row-7 invariant count
moves with Q22, and the save/replay sentences must now state the split as settled
rather than filed. The Q20 half is rewritten to say what was decided and why, and
deliberately points at §4.4 rather than keeping a second, drift-prone copy of the
week numbers — this paragraph and the milestone table have disagreed once already.

**OLD**
```
**Critical path: 1 → 3 → 4 → 5 → 6/8.** Row 2 runs in parallel immediately.
**Row 7 no longer sits beside the chain; it straddles it.** Its structural half
(T-SCN-01..03, 05, 07, 09) starts once 1–2 land, but three of its nine
invariants — T-SCN-04's flag reachability and T-SCN-06/08's opening-capture
lane — price a Stub-3 path, so row 7 cannot *close* until row 3 does. Row 7 is
still not ON the critical path (nothing in the chain waits on it), but
scheduling it as "parallel from week 1" would leave its ledger row un-flippable
and the §2.11.6 guided opening ungated for however long movement slips: the
scenario row flips after movement, not before. 6 and 8 fork after 5. §4.4's milestone
table currently parks save/load in week 5, and §4.10 shows that is one
week too late in one respect: the *format and headless replayer* are the
instrument for the week-2 integration gate (T-INT-02) and the week-4
self-play logs (T-SAVE-07). Splitting the row — format + replayer early,
save-slot UI stays week 5 — is filed as **Q20** (§4.7) against §4.4's milestone
table, not applied here.
```
**NEW**
```
**Critical path: 1 → 3 → 4 → 5 → 6/8.** Row 2 runs in parallel immediately.
**Row 7 no longer sits beside the chain; it straddles it.** Its structural half
(T-SCN-01..03, 05, 07, 09) starts once 1–2 land, but **four of its ten written
invariants** — T-SCN-04's flag reachability and T-SCN-06/08/11's opening-capture
lane — price a Stub-3 path, so row 7 cannot *close* until row 3 does. T-SCN-11
(Q22, ruled) is the newest of the four and the most expensive: it prices a
*second* path per seat — the opposing seat's cheapest route to the same
objective — so row 7's path budget is two lookups per `guidedOpening` entry
rather than one. Its *dependency* is settled even though its *assertion* is not:
the invariant is written and blocked on **Q28**, which asks whose Infantry the
opposing route starts from and which, under its stricter reading, refuses
*Ferrum Crossing* as drawn (§4.7). Row 7 is
still not ON the critical path (nothing in the chain waits on it), but
scheduling it as "parallel from week 1" would leave its ledger row un-flippable
and the §2.11.6 guided opening ungated for however long movement slips: the
scenario row flips after movement, not before. 6 and 8 fork after 5.
**Row 10 is split, per Q20 (ruled).** Its *format and headless replayer* are not
week-5 content but the instrument two earlier gates run on — T-INT-02's input
file is a save, and the week-4 self-play logs T-SAVE-07 validates are the same
format — so §4.4 now lands them beside the scenario loading they already sit
next to, and leaves only the **save-slot UI and slot I/O** at the end. That is
the split this section proposed and the Director adopted; §4.4's table and the
note under it are the single statement of the schedule, and this paragraph
deliberately does not restate the week numbers a second time.
```

---

## Build order

Unchanged in shape; row 7 gains one invariant and one path lookup per entry, and
row 10 gains a schedule split. Deltas in bold.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 1 | Hex grid & math (Stub 1) | — (Q1 pins bounds) | Yes | T-HEX-01..07 |
| 2 | Data tables (§4.8) | — (MoveClass blocked on Q2) | Loader yes; import parity in-editor | T-DATA-01..06 |
| 3 | Movement & pathfinding (Stub 3) | 1, 2 | Yes | T-MOVE-01..06 |
| 4 | Capture & Fame economy (Stub 4) | 3 | Yes | T-FAME-01..09 |
| 5 | Turn loop & win/tiebreak (Stub 5) | 4 + Combat @ `5ffa8d6` | Yes | T-TURN-01..09 |
| 6 | Opponent AI (Stub 6) | 5 | Yes | T-AI-01..06 + self-play smoke |
| 7 | Scenario file & validator (Stub 7) | 1, 2 structural; **3 for the priced half — T-SCN-04, 06, 08, 11**, and 11 costs two paths per entry | Yes; MCP wraps it, manual fallback stands | **T-SCN-01..09, 11** (10 reserved-unwritten, Q26; **11 blocked on Q28**) |
| 8 | UI binding (Stub 8) | 5, 7 | Contract + queries yes; widgets in-editor | T-UI-01..04 |
| 9 | Presentation bridge — §4.9 | Rows 1–5 | Source/compile gates yes | T-INT-01..05 |
| 10 | Save & replay — §4.10 | 4, 5, 7; **format itself has no deps — wk 2, per Q20** | Yes, all but slot I/O | **T-SAVE-01..06 from wk 2; T-SAVE-07 closes wk 4; slot I/O wk 5** |

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.2, "Asymmetry and its handicap story" / "The tactical question this map asks" | "each seat is closer to a different neutral factory"; "West's fast prize is South (open Plains approach); East's is North (no crossing needed)" | `scenario-designer` / Director to reconcile with the measurement: West is **5 MP to South, 6 to North**; East is **5 MP to North and 5 to South** — East is equidistant, not closer to one. | The seat-asymmetry claim the map's handicap story rests on is one-sided as drawn. Not a §4 edit — measured while gating Q22, but it is §2.13's prose. |
| §2.13.1, fact 3, "Uncontested, not merely reachable" | "The designated lane is the seat's *own* neutral — West → South, East → North on the shipped map — so the first lesson is not a race." | Same owner. Under Q28's stricter reading this sentence is **false for the South lane**: East's second Infantry ties West's 5 MP. It is true under the narrower reading. Reword once Q28 is ruled, whichever way it goes. | §2.13.1 states as a fact the very property T-SCN-11 now tests, and the test does not agree with it on one lane. |
| §4.10, "Policies (prototype)" | "Overwrite-confirm UX is **unowned**" | No change requested; flagged only. The Q20 split dates it — week 5 is where the surface lands, so §2.11 has until then to own it or accept silent overwrite. | The split gives an unowned surface a deadline it previously lacked. |

## Open questions for the Director

**One new gap, filed as Q28** (edit 11): whose Infantry the T-SCN-11 opposing
route is measured from. It is not a stylistic choice — reading (a) refuses
*Ferrum Crossing* as drawn at 5 vs 5; reading (b) passes all six lanes of all
three maps. I have stated **no assumption in force** for it, because for the
first time in this register the conservative reading blocks a shipped map, and
stating it would mean asserting a gate the shipped scenario fails on the day it
is written — the outcome your instruction named as worse than no rule.

Two things I checked *for* new gaps and did not have to file:

- **Whether Bridges are allowed on the opposing route.** Excluding them passes
  *The Causeway* vacuously; including them is stricter and still passes 5 vs 3.
  Strictness is free, so T-SCN-11 states it rather than asking.
- **Whether a tie fails.** Your ruling said *strictly longer*, so it does. No
  latitude was taken — and the tie is exactly where the shipped map lands.

Q20 needs nothing further. Q22 needs only Q28.

## Handoffs

- **Director:** apply the thirteen pairs. Edit 2 (§4.4 week 4) is the only
  optional one; the split holds without it. Nothing in
  `../stratocracy-content/kb/rules.md` parses §4, so the KB re-sync step of the
  merge checklist is not triggered by any of this — the two §2.13 change requests
  above would trigger it if you act on them.
- **`scenario-designer`:** two measurement-driven items, both in your lane,
  neither actionable until Q28 rules — *Ferrum Crossing*'s 5 vs 5 South lane, and
  §2.13.2's one-sided "closer to a different neutral factory" claim. I moved no
  hex, no lane number, and no terrain count.
- **`rules-designer`:** nothing. No rule, cost, or Fame figure moves.
- **`ux-onboarding-designer`:** one thing to know rather than to do — §2.11.6-B's
  guided opening rests on §2.13.1's non-contention promise, and that promise is
  now gated. If Q28 rules strictly and the South lane stays as drawn, the turn-2
  directive on the shipped map is walking a first-time player into a contested
  tile. Separately, the save-slot UI now has a week (5) and still has no owner in
  §2.11 (§4.10 records the surface as unowned).
- **`continuity-gate`:** the six measured lanes are re-derivable from §2.13's
  ASCII maps plus §2.13.1's odd-r adjacency. The one that decides anything is
  East (9,5)→(9,6)→(8,7)→(7,7)→(6,7)→(5,7), five cost-1 hexes, against West
  (1,5)→(2,6)→(3,6)→(3,7)→(4,7)→(5,7). Please check both. Also check that Q20 no
  longer appears in the *unruled* list, that Q28 appears exactly once, and that
  no surviving §4 text names a pinned register extent.

## Grounding

| Claim | Source |
|---|---|
| §4.4's current week 2/4/5 rows and the Q23 note ending "The save/replay half … (**Q20**) is still open" | `source/gdd.md` L1272–1280 (md5 `3c589e1e64c4065c1d03a0b88ede7735`) |
| Q20's content — format + replayer are the instrument for T-INT-02 and T-SAVE-07; the split is §4.11's own proposal | L1812 (register); L2072–2078 (§4.11 closing paragraph) |
| T-INT-02's input file is a save; T-SAVE-07's self-play logs are the same format | §4.10 consumers list L1972–1978; Save-stub invariants L2036–2037; §4.11 preamble L2047–2049 |
| §4.10's format is fully specified already (header fields, command log, canonical state hash field order) | L1980–2001 |
| Stub 7's current T-SCN-07 text, its "unruled (Q22)" disclaimer, and its Determinism / Acceptance lines | L1649–1657, L1730–1738 |
| T-SCN-10 is reserved-but-unwritten, and Q26 keeps it so | L1721–1729; register Q26, L1818 |
| Q21 ruled: lanes price on terrain alone, occupancy excluded | Register Q21, L1813 |
| T-SCN-06's accounting — every hex entered including the objective, T-MOVE-01 parity; its Bridge-free clause and its NAMED-hex quantification | L1620–1648 |
| Terrain move costs (Plains 1, Woods 2, Mountains 3, Town 1, Bridge 1, Factory 1; Water not land-passable) | §2.3 table, L120–128 |
| Infantry Move 3, and Infantry as the only capturing unit | §2.4 L142; §2.7 via T-SCN-06's CanCapture derivation, L1620–1627 |
| Odd-r → axial conversion `q = col − (row − (row & 1))/2`, used for every distance floor quoted | §4.7 Shared conventions, L1349–1351 |
| *Ferrum Crossing* 11×9 ASCII map, key coordinates, Infantry deployment (1,3)(1,5) West / (9,3)(9,5) East | §2.13.2 L848–879 |
| *Ferrum Crossing* guided lanes: West (1,5)→(5,7) 5 MP; East (9,3)→(6,2) 5 MP | §2.13.1 lane table, L749 |
| *Longwater March* 13×8 map, deployment, guided opening (1,2)→(4,1) / (11,5)→(8,6), ρ(c,r) = (12−c, 7−r) | §2.13.5 L982–1026 |
| *The Causeway* 9×8 map, deployment, guided opening (1,2)→(3,2) / (7,5)→(5,5), ρ(c,r) = (8−c, 7−r), full column-4 bisection | §2.13.6 L1061–1114 |
| §2.13.2's "each seat is closer to a different neutral factory" / "West's fast prize is South; East's is North" | L898–908 |
| §2.13.1's "Uncontested, not merely reachable … so the first lesson is not a race" | L769–772 |
| Every MP figure in the measurement tables | Computed by me from the four sources above; each path and each axial distance floor is written out in the Draft so the number can be checked rather than trusted |
| The "written and blocked" convention for an invariant whose rule is unruled; the `(NN reserved on QN)` acceptance form | T-FAME-05 / Q4 at L1441–1442 and L1796; T-MOVE-07 acceptance line at L1421 |
| Combat's 17/17 invariants @ `5ffa8d6` remain the only gate-verified system; every row this draft touches is still `*pending*` | §3 provenance ledger; §4.11 preamble L2045–2049 |
