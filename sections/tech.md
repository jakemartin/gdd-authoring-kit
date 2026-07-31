> # ⛔ SUPERSEDED — DO NOT RE-MERGE
>
> This draft was merged into the master GDD and has since been **overtaken by
> Director rulings and gate remediation applied directly to the master**. It is
> kept only as the provenance record of what this author wrote.
>
> **It is not a superset of what is merged.** Its Placement block claims wholesale
> replacement of sections that have since moved on, so re-merging this file would
> silently revert, among others: the Q7 turn-cap ruling, the Q23 week-2/3
> resequencing, the N = 8 scoreboard figures, the Q-register pointer repointings,
> and several closed change requests.
>
> **The master GDD is the only source of truth.** Read `source/gdd.md`
> (md5 `0eedea2dfd7b17a508e162427682ce64`). To change a merged section, author a
> post-merge addendum of exact old→new replacement passages — as
> `sections/tech.md` did for run `post-merge-1` — never a wholesale redraft.
>
> Superseded as of gate run `post-merge-2`.

# Technical design — post-merge-1 addendum (tech-director)

> **Scope note.** The stage-1 and stage-2 drafts of this file are merged into the
> master GDD as §4.7–§4.11 and are **not** reproduced here. This file is a
> surgical addendum against one violation from gate run `post-merge-1`: §2.13.1's
> newly adopted **Opening-capture reachability** invariant cites two Stub-7
> scenario fields — `guidedOpening.infantry`, `guidedOpening.objective` — that
> Stub 7's field list never defined. Every passage below is an exact replacement
> against the merged text. Nothing else in §4 is touched.

## Placement

- **§4.7 Spec Stub 7 (Scenario file & validator)** — two field-block edits, three
  new invariants (T-SCN-06..08), amended `Determinism:` and `Acceptance:` lines.
- **§4.7 Open questions** — two new rows, **Q21** and **Q22**, plus the two
  range citations that name the register's extent (`Q1–Q20` → `Q1–Q22`).
- **§4.11 Build order** — row 7's `Depends on` and test-ID columns, and the
  critical-path paragraph that currently says row 7 runs "in parallel."

**Checked and requiring no change** (the Director asked me to check rather than
assume):

| Location | Enumerates scenario fields? | Verdict |
|---|---|---|
| §4.9 bridge/load bullet | No — cites `strat::loadScenario` and the asset, not fields | No edit |
| §4.10 file-layout table | No — carries `scenarioId` / `scenarioHash` only; the hash covers new scenario fields transitively | No edit |
| §4.8 schemas | No — references `isFlag` as a placement-level field, no field list | No edit |
| §2.13.1's citation `guidedOpening.infantry` | — | **No edit needed.** The field is specified below as an array of per-side entries, so the dotted path reads correctly as the entry's field name. Deliberate: it closes the dead reference without editing another author's section. |

One consequence worth stating and not acting on: adding a field changes every
scenario's `scenarioHash`, which §4.10's version policy treats as grounds to
refuse a save. No scenario file and no save file exists yet (`Source/` is still
the stock template), so the cost of this addition is zero today and rises the
moment the first scenario ships. That is an argument for landing it now.

## Draft

### Amendment 1 — §4.7 Stub 7, the `scenarioHash` field entry

`scenarioHash` is the reason field order is load-bearing rather than cosmetic, so
the ordering policy belongs on that line and nowhere else.

**Old:**

```
           scenarioHash    string  hash of the canonical serialization (fields
                                   in this order, hexes in canonical hex order)
```

**New:**

```
           scenarioHash    string  hash of the canonical serialization (fields
                                   in this order, hexes in canonical hex order).
                                   The order is load-bearing, so NEW FIELDS
                                   APPEND AT THE TAIL of this list: an
                                   append-only preimage means adding a field can
                                   never reorder an existing one (the discipline
                                   that appended `type` last in the combat
                                   addendum, Part A). Serialization order is not
                                   validation order — a field is validated after
                                   whatever it references, wherever it sits here.
```

### Amendment 2 — §4.7 Stub 7, the new `guidedOpening` field

Placed at the tail, after `turnCap`, per the policy Amendment 1 just pinned. It
references both `ownership` and `placements`, so it validates last regardless.

Two design decisions inside the field, both load-bearing:

- **`infantry` and `objective` are hex references, not placement indices.** The
  `placements` array has no per-entry ID — `unitId` is the *type* row name
  (Infantry/Tank/…), not an instance handle — so there is nothing to point at.
  A hex is a sufficient instance reference because **T-SCN-02 already forbids two
  placements sharing a hex**. This adds no new identity concept to the schema and
  makes the scenario field literally the §2.13.1 lane table's row: `(1,5) → (5,7)`.
- **Array of per-side entries, serialized in the module's side enumeration
  order** — not authoring order. Otherwise two files differing only in which seat
  was typed first would hash differently, and `scenarioHash` would stop being a
  content hash.

**Old** (last line of the `Fields:` block):

```
           turnCap         int     the §2.8 cap (value per Q7)
```

**New:**

```
           turnCap         int     the §2.8 cap (value per Q7)
           guidedOpening   array   one entry per side, {side, infantry,
                                   objective} — that seat's opening-capture lane
                                   (§2.13.1). `infantry` and `objective` are HEX
                                   references: the deployment hex of the seat's
                                   marked Infantry (§2.11.6 turn 1a) and the
                                   neutral Factory hex it walks to. A hex
                                   identifies the placement uniquely because
                                   T-SCN-02 already forbids two placements
                                   sharing one, so this adds no instance-ID
                                   concept to the schema. Entries serialize in
                                   the module's side enumeration order, not
                                   authoring order, so the hash is content-only.
                                   Required on every scenario: §2.13.1 declares
                                   the reachability invariant shared by every
                                   map, and §2.11.6's turn-2 directive has no
                                   other source for the pair. The guidance layer
                                   reads this field from the loaded scenario
                                   directly — marked/locked is presentation
                                   state, not rules state, so it stays out of
                                   the Stub-8 snapshot.
```

### Amendment 3 — §4.7 Stub 7, three new invariants

The §2.13.1 guarantee decomposes into three independently assertable rules with
three distinct failure modes, so it gets three invariants, not one.

The gate-design decision that matters: §2.13.1 states an **existential** ("at
least one Infantry deployment hex must have a land path…") *plus* a **naming**
requirement ("the scenario file names that unit… so the turn-1a marked Infantry
is the one already standing on the lane"). Asserting the existential over the
**named** hex collapses both into one check. Written the other way — find any
qualifying hex, then compare it to the named one — the validator can pass a map
whose qualifying lane belongs to a different unit than the one §2.11.6 turn 1a
marks, which is the exact class of bug the §2.11.6 violation was.

**Old** (T-SCN-05 is the current last invariant):

```
  T-SCN-05  coordinate conversion (Shared conventions): odd-r (col, row) → axial
            (q, r) round-trips for every in-bounds hex of the declared
            dimensions, and the loaded map's adjacency matches the authored
            grid's; no authored file stores axial, and no loaded state stores
            (col, row)
```

**New** (T-SCN-05 unchanged; 06–08 appended):

```
  T-SCN-05  coordinate conversion (Shared conventions): odd-r (col, row) → axial
            (q, r) round-trips for every in-bounds hex of the declared
            dimensions, and the loaded map's adjacency matches the authored
            grid's; no authored file stores axial, and no loaded state stores
            (col, row)
  T-SCN-06  opening-capture lane (§2.13.1): for EACH guidedOpening entry, a land
            path exists from `infantry` to `objective` costing
            <= 2 x Move of the capturing unit row — T-DATA-03's single
            CanCapture row, §2.4 Infantry Move 3, so 6 MP — and crossing NO
            Bridge hex. The ceiling is DERIVED from the loaded table, never a
            literal: a §2.4 Move change re-prices the gate instead of silently
            passing it, and the capturing row is found by CanCapture so §2.7's
            Infantry-only rule and this lane can never name different units.
            Cost counts every hex entered including the objective itself
            (Factory MoveCost 1, §2.3) — the same accounting as T-MOVE-01, so
            the validator and the reach highlight cannot price one lane two
            ways. Excluding Bridge (and Water being land-impassable, §2.3)
            confines the lane to the seat's own bank, which is what makes the
            first lesson uncontested rather than a crossing. Asserting the
            existential over the NAMED hex is deliberate — see the note above
            the stub. The gate asserts ARRIVAL ONLY: the turn the tile flips is
            N-dependent (Q4) and is asserted nowhere here, matching §2.13.1's
            "capturing by turn 2, never captured by turn 2."
  T-SCN-07  opening-capture naming (structural; no pathing, so this half of the
            check lands with rows 1-2): exactly one guidedOpening entry per side;
            `infantry` is the hex of a starting placement of THAT side whose
            unitId is the CanCapture row and whose isFlag is false; `objective`
            is a Factory hex that `ownership` leaves neutral (§2.7); and the two
            entries name DIFFERENT objectives — §2.13.1's "the seat's own
            neutral," gated at its distinctness floor. The stronger
            non-contention property §2.13.1 also claims is unruled (Q22) and
            nothing here asserts it.
  T-SCN-08  measured, not inferred: the validator COMPUTES and REPORTS each
            entry's lane cost as an integer, from Stub-3 pathing. The declared-
            symmetry flag (§2.13.1) is not an input and cannot substitute — an
            odd-r row offset lets a mirrored or rotated layout price the two
            seats' lanes differently. Fixtures: a mirror-declared scenario whose
            lanes cost 3 and 4 PASSES and reports both numbers (Longwater March,
            §2.13.1); one whose lanes both cost 7 FAILS. The reported integers
            are the source of truth for §2.13.1's lane table, so a map edit that
            lengthens a lane surfaces as a changed number rather than a still-
            green boolean.
```

### Amendment 4 — §4.7 Stub 7, `Determinism:` and `Acceptance:` lines

Validation now prices a path, so Stub 7's determinism inherits from Stub 3's.
Stated, because an unstated inheritance is how a reported number becomes
compiler-dependent.

**Old:**

```
Determinism: pure parse + validation; any failure refuses the whole file with a
         reason. scenarioHash is platform-stable by canonical ordering.
Acceptance: T-SCN-01..05 headless. The §4.2 validate_scenario MCP tool wraps the
```

**New:**

```
Determinism: pure parse + validation; any failure refuses the whole file with a
         reason. scenarioHash is platform-stable by canonical ordering. The
         T-SCN-06/08 lane costs are Stub-3 path costs and inherit its
         determinism (T-MOVE-04's canonical tie-break, T-MOVE-06), so the
         reported integers reproduce across runs and compilers.
Acceptance: T-SCN-01..08 headless. The §4.2 validate_scenario MCP tool wraps the
```

### Amendment 5 — §4.7, the two Q-register extent citations

**Old** (§4.7 preamble, third sentence):

```
state, the gate is parameterized on a numbered open question (Q1–Q20, Open
questions below) — the Director rules, the gate then pins the ruling.
```

**New:**

```
state, the gate is parameterized on a numbered open question (Q1–Q22, Open
questions below) — the Director rules, the gate then pins the ruling.
```

**Old** (Open-questions preamble, first sentence):

```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), this stage's additions (Q11–Q13), and the rules- and
scenario-side rulings folded in here (Q14–Q20) so that each question carries
exactly one ID across the whole document.
```

**New:**

```
**Open questions (Director rulings owed).** Every gap found while writing the
§4.7 gates (Q1–Q10), the stage-2 additions (Q11–Q13), the rules- and
scenario-side rulings folded in here (Q14–Q20), and the two gaps found while
gating §2.13.1's opening-capture invariant (Q21–Q22) so that each question
carries exactly one ID across the whole document.
```

### Amendment 6 — §4.7, two new rows appended to the Q table

**Old** (last row of the table):

```
| **Q20** | Save/replay milestone split. §4.11 shows §4.4's week-5 save/load placement is one week late in one respect: the format and headless replayer are the instrument for the week-2 integration gate (T-INT-02) and the week-4 self-play logs (T-SAVE-07). Split the row — format + replayer early, save-slot UI stays week 5? | §4.4's milestone table; T-INT-02 and T-SAVE-07 sequencing | Unruled. §4.4 stands as written; §4.11 records the conflict without resolving it. This is a scheduling decision, adjacent to the §4.4-vs-§4.11 critical-path question. |
```

**New** (Q20 unchanged; two rows appended):

```
| **Q20** | Save/replay milestone split. §4.11 shows §4.4's week-5 save/load placement is one week late in one respect: the format and headless replayer are the instrument for the week-2 integration gate (T-INT-02) and the week-4 self-play logs (T-SAVE-07). Split the row — format + replayer early, save-slot UI stays week 5? | §4.4's milestone table; T-INT-02 and T-SAVE-07 sequencing | Unruled. §4.4 stands as written; §4.11 records the conflict without resolving it. This is a scheduling decision, adjacent to the §4.4-vs-§4.11 critical-path question. |
| **Q21** | Opening-capture lane measurement. Does T-SCN-06 price the lane on **terrain alone**, or on the board **as deployed** — where, under Q3's blocked-pass-through reading, a seat's own four other starting units can make its own lane unmeasurable? The two readings can disagree by several MP on a crowded deployment. | T-SCN-06's pass/fail and T-SCN-08's reported integers; §2.13.1's three-map lane table if the answer is "as deployed" | Terrain alone, occupancy excluded — the reading that reproduces §2.13.1's measured 5/5, 3/4, 2/3, and the reading that matches how the lane is actually played (the other four units move too). If the Director rules "as deployed," all three maps need re-measuring and §2.13.1's numbers may move. |
| **Q22** | Uncontested vs. merely reachable. §2.13.1 promises the guided lane is "uncontested, not merely reachable," but states it as a property of the shipped map rather than a checkable rule. Is *distinct objectives per seat* the whole requirement, or must the validator also assert non-contention — e.g. the opposing seat's cheapest Infantry lane to the same objective is strictly longer? | Whether T-SCN-07's distinctness clause is the floor or a further T-SCN invariant is owed | Distinctness only, as gated in T-SCN-07. Consequence stated plainly: a map can pass every §2.13 gate and still hand both seats a race to the same tile, turning the first lesson into a contest. |
```

### Amendment 7 — §4.11 row 7 and the critical-path paragraph

T-SCN-06 and T-SCN-08 both price a path, so both need Stub 3. This does change
row 7's position, and the table must say so.

**Old:**

```
| 7 | Scenario file & validator (Stub 7) | 1, 2 (3 for T-SCN-04) | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..05 |
```

**New:**

```
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..08 |
```

**Old** (critical-path paragraph, first two sentences):

```
**Critical path: 1 → 3 → 4 → 5 → 6/8.** Rows 2 and 7 run in parallel with the
chain (2 immediately; 7 once 1–2 land); 6 and 8 fork after 5.
```

**New:**

```
**Critical path: 1 → 3 → 4 → 5 → 6/8.** Row 2 runs in parallel immediately.
**Row 7 no longer sits beside the chain; it straddles it.** Its structural half
(T-SCN-01..03, 05, 07) starts once 1–2 land, but three of its eight
invariants — T-SCN-04's flag reachability and T-SCN-06/08's opening-capture
lane — price a Stub-3 path, so row 7 cannot *close* until row 3 does. Row 7 is
still not ON the critical path (nothing in the chain waits on it), but
scheduling it as "parallel from week 1" would leave its ledger row un-flippable
and the §2.11.6 guided opening ungated for however long movement slips: the
scenario row flips after movement, not before. 6 and 8 fork after 5.
```

## Build order

Only row 7 moves. Rows 1–6 and 8–10 stand exactly as merged in §4.11.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 7 | Scenario file & validator (Stub 7) | 1, 2 for the structural half (T-SCN-01..03, 05, 07); **3 for the priced half** — T-SCN-04, 06, 08 all cost a path | Yes; MCP tool wraps it in-editor, manual fallback stands | T-SCN-01..08 |

The schedule consequence, stated once: the §2.11.6 guided opening is the first
thing a player touches and the last thing this build order can gate, because its
guarantee is priced in movement points. If Stub 3 slips, the onboarding gate
slips with it — and Q21 sits underneath Stub 3's Q3 pass-through ruling, so a
late Q3 answer can move the measured numbers in §2.13.1 after the maps are drawn.
That chain — Q3 → Stub 3 → Q21 → T-SCN-06/08 → §2.13.1's table → §2.11.6's
turn-2 directive — is the longest unresolved dependency in §4 and the one I'd
watch.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.1, Validation invariants bullet | "every land-passable hex reaches every factory … declared symmetry (mirror/rotation/none) is machine-verified" | Optional: append the gate IDs — connectivity → T-SCN-04, deployment-hex freedom → T-SCN-02, symmetry → T-SCN-08's "not an input" clause | Every other §2.13 claim now names its gate; this bullet is the last one that asserts machine-verification without naming what verifies it. Scenario-designer's lane — filed, not applied. |
| §2.13.1, Opening-capture bullet | "The scenario file names that unit and that factory (`guidedOpening.infantry`, `guidedOpening.objective`, §4.7 Stub 7)" | **No change required** — deliberately. The field is specified above as an array of per-side entries, so the dotted path resolves as the entry's field name. | Recorded here so the Director can see the dead reference was closed from the §4 side only, with no edit to another author's adopted text. |

No other change requests this pass. The nine filed in the stage-2 draft are
merged or superseded and are not restated.

## Open questions for the Director

Both are new this pass and both were found while writing the gate, not before it.

1. **Q21 — lane measurement basis: terrain alone, or the board as deployed?**
   This is the one that can move numbers already printed in §2.13.1. Under Q3's
   in-force reading a unit may not path *through* any occupied hex, and a seat's
   own five-unit deployment (§2.13.1) sits in exactly the region its lane starts
   from. Terrain-only is the reading in force because it reproduces the three
   measured lane tables and matches how the lane is played. If you rule "as
   deployed," the scenario-designer re-measures all three maps and some may fail
   the 6 MP ceiling.
2. **Q22 — is "uncontested" a rule or a description?** §2.13.1 promises the
   guided lane is "uncontested, not merely reachable," then evidences it with a
   property of the shipped map ("West → South, East → North"). T-SCN-07 gates the
   distinctness floor. Anything stronger — the opponent's cheapest lane to the
   same tile is strictly longer — needs a rule from you before it can have a gate.

Neither blocks the field addition or T-SCN-07. Q21 blocks nothing structurally
but determines what T-SCN-06/08 *measure*, so it should be answered before the
maps are frozen rather than after.

## Handoffs

- **scenario-designer** — `guidedOpening` is an authored field, one entry per
  side, both values hexes in your odd-r `(col, row)` space (converted on load,
  T-SCN-05). Your §2.13.1 lane table already *is* the field's content: each row's
  "West lane" / "East lane" cell becomes that map's two entries. T-SCN-08 reports
  the cost back as an integer, so your table and the validator's output should be
  diffable line for line — if they disagree, one of them is wrong and the gate
  says which. Q21 lands in your measurement method; Q22 lands in whether your
  "uncontested" claim gains a gate.
- **ux-onboarding-designer** — §2.11.6 turn 1a's *marked* Infantry and turn 2's
  target both resolve from `guidedOpening[seat]` on the loaded scenario. That is
  presentation-layer guidance state, so it is deliberately **not** in the Stub-8
  view-model snapshot and needs no snapshot change; the guidance layer reads the
  scenario. Your turn-2 directive can now cite a real contract instead of an
  asserted guarantee: T-SCN-06 is what makes it true, and T-SCN-06 promises
  *arrival*, not *flip* — which is why retiring on the pip (as you already
  specify) is the only correct retire condition while Q4's N is unruled.
- **rules-designer** — no command-set or §2 change here. One dependency to know
  about: Q3's pass-through ruling now propagates into scenario validation via
  Q21, so a Q3 answer has a §2.13 consequence it did not have before.
- **Director** — Q21, Q22, and the seven replacement passages above.

## Grounding

- The invariant being gated, its ≤ 6 MP ceiling, its Bridge exclusion, its
  per-seat scope, the three measured lane tables (5/5, 3/4, 2/3), the
  "capturing by turn 2, never captured by turn 2" distinction, and the
  measure-don't-infer requirement: `source/gdd.md` §2.13.1, Opening-capture
  reachability bullet and its three following clauses.
- The two field names and their citation of Stub 7: same bullet, sentence 3.
- Infantry Move 3 (the 2 × Move ceiling's basis): §2.4 unit table. The gate reads
  it from the loaded table via §4.8's `Move` column, not as a literal.
- The capturing unit identified by CanCapture rather than by name: §4.8 unit
  schema `CanCapture` column and T-DATA-03 ("exactly one unit row has CanCapture
  == true"), §2.7 Infantry-only capture.
- Factory MoveCost 1 and Water land-impassable / Bridge as the only crossing:
  §2.3 terrain table; movement-cost accounting: §4.7 Stub 3, T-MOVE-01/02.
- Path determinism inherited by T-SCN-08's reported integers: §4.7 Stub 3,
  T-MOVE-04 (canonical-order tie-break) and T-MOVE-06.
- Hex-as-instance-reference being sufficient: §4.7 Stub 7, T-SCN-02 ("no two
  placements share a hex"). Odd-r → axial conversion on load: Shared conventions
  block and T-SCN-05.
- The turn-1a marked Infantry and turn-2 directive this closes the reference for:
  §2.11.6-B table, rows 1a and 2.
- Capture N = 1 as an assumption in force rather than a settled rule, and the
  unruled interruption semantics: §4.7 Q4 row. **No invariant added here depends
  on N.**
- Q3's blocked pass-through reading, which Q21 sits underneath: §4.7 Q3 row and
  T-MOVE-03.
- Seat-select in scope, which is why `guidedOpening` is per-side rather than
  single-entry: §4.7 Q18 row and §2.13.4.
- Append-last field discipline: `../stratocracy-crew/spec/combat_spec_addendum.md`
  Part A, the appended-last `type` field contract, cited in merged §4.8.
- Project state unchanged by this addendum: four ledger rows verified at
  `5ffa8d6` (17/17 invariants); the eight §4.7 rows including Stub 7 remain
  `*pending*` with **no code**. T-SCN-06/07/08 are specifications, not passing
  tests, and nothing here claims otherwise (§3 ledger).
