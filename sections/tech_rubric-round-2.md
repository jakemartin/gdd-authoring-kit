# Technical design — rubric round 2 addendum (tech-director)

Three targets, eleven replacement pairs, all in §3 and §4. Nothing here redrafts a
section. Every **OLD** block below was searched against `source/gdd.md` and
returns exactly one match.

---

## TARGET 1 — state the build's actual position, and give §4.5 the risk it is running

### Pair 1 — §3, the ledger status line

**OLD**
```
gate-verified 2026-07-29; the rest land as each system is built (wk 1–3, §4.4).*
```
**NEW**
```
gate-verified 2026-07-29; the rest land as each system is built (wk 1–3, §4.4). This draft stands at 2026-08-01, three days past the last code commit: §4.4's week-1 deliverable is §4.11 rows 1–3 — grid and hex math, the §4.8 tables, movement and pathfinding — and all three still read `*pending*` in the table below, with no hex-grid, movement or DataTable source in the crew repo, which holds the Combat module alone. Because §4.11's critical path runs 1 → 3 → 4 → 5 → 6/8, nothing §4.4 schedules for weeks 2–3 clears without those three rows — only row 2 itself, row 10(a)'s format spec, T-INT-01/04 and the parallel UMG skeletons proceed meanwhile — so weeks 2–3 move with week 1 one for one rather than absorbing it, which is why §4.5 now carries that as a named risk with a cut line attached rather than as a discovery.*
```

### Pair 2 — §4.5, one new risk row

**OLD**
```
| Agent code quality | Test-first; human review gates; headless module keeps loops fast |
```
**NEW**
```
| Agent code quality | Test-first; human review gates; headless module keeps loops fast |
| **Specification outruns the build** — **69** written acceptance IDs at this revision (§4.7–§4.11) against **4** verified ledger rows (§3), all four inside Combat; §4.4 week 1 is due §4.11 rows 1–3 and all three read `*pending*` at 2026-08-01 | The **† cut line** (§4.7 head; members marked in §4.11's build-order table, which is authoritative for which side an ID is on) separates the IDs the MVP line above needs from the correctness infrastructure that stands down if the calendar takes it — so a slip drops named suites rather than silently thinning every suite. And the discipline Q20 and Q23 already applied holds for the rest of the table — *each piece lands in the week the thing that consumes it runs* (§4.4), and a gate that runs green over a subset does not flip its ledger row (Q29) — so a slip in rows 1–3 moves everything downstream of them rather than being absorbed by calling a row done on a partial pass |
```

---

## TARGET 2 — the cut line across the written acceptance IDs

**Recount, done independently.** T-HEX 7 · T-DATA 6 · T-MOVE 6 (07 reserved,
unwritten) · T-FAME 9 · T-TURN 9 · T-AI 6 (plus the self-play smoke run, which
carries no ID) · T-SCN 10 written (01–09, 11; 10 reserved-unwritten) · T-UI 4 ·
T-INT 5 · T-SAVE 7 = **69**. The Director's figure holds. T-COMBAT-01..10 and
T-REPAIR-01..07 are excluded: they are green at `5ffa8d6` and §4.11 calls them
prerequisites, not work items.

**Where my derivation differs from the auditor's split — three places, each
followed rather than deferred to.** All three are recorded under **Change
requests** below; the reasoning is here and is not repeated there.

1. **T-SAVE-07 moves to the ship side.** It is headless, and §4.4 closes it in
   week 4 on logs week 4 emits anyway — "every match emitted in the wk-2 §4.10
   format, so T-SAVE-07 closes here". Under §2.13.7's own slip condition (week 4
   consumed by balance) self-play still *runs*; it is the stretch maps that stay
   on paper. Cutting T-SAVE-07 therefore buys no calendar. A cut that saves no
   time is not a cut.
2. **T-SCN-09 joins the cut side**, which the auditor did not name. Not for
   cost — it is structural and lands with rows 1–2 — but for coverage:
   §4.7 states `symmetry == none` "asserts nothing and is always well-formed",
   *Ferrum Crossing* declares `none`, and §2.13.7 puts both `rot180` maps in the
   stretch column. On shipped scope alone T-SCN-09's asserting branch never runs
   against a `rot180` map at all.
3. **§4.11's "priced half" is not the cut unit.** That phrase covers T-SCN-04,
   06, 08 and 11. I cut only 08 and 11 and keep 04 and 06: T-SCN-04 (the two
   flags mutually reachable) is the precondition of the win condition §4.5's own
   MVP line calls complete, and T-SCN-06 gates §2.11.6's guided opening, which
   §2.11.8 ranks must-have for a playable first session.

The auditor's split also left 18 of the 69 unassigned (T-SCN-01..07 and 09,
T-UI-03/04, T-INT-01/03/04, T-SAVE-01..05). A line that does not partition the
set is not a cut line, so the marks below assign all 69.

### Pair 3 — §4.7, the three-line head note

**OLD**
```
because every range named elsewhere has gone stale within a revision.

**Shared conventions (Director-owned contract):**
```
**NEW**
```
because every range named elsewhere has gone stale within a revision.

**The cut line, read before adding a suite.** Every acceptance ID in §4.7–§4.11
is either unmarked — the §4.5 MVP line needs it and no human read substitutes
for it — or **†**, correctness infrastructure that does not *close* if the
calendar takes it, because its fixtures live on §2.13.7's stretch maps or its
only unique coverage is an in-editor Automation pass. The † members are marked
in §4.11's build-order table and nowhere else, so that table is authoritative
for the split and no count of it is stated here; what remains fixed is the rule
that no rules-correctness invariant on the critical path §4.11 states is ever
in it — those suites are the game, not the evidence about it.

**Shared conventions (Director-owned contract):**
```

### Pairs 4–8 — §4.11, the marks in the build-order table

Rows 1, 3, 4, 5 and 6 need no edit: every ID in them is unmarked by the rule
above, which is the point of "unmarked = ship".

**OLD**
```
| T-DATA-01..06 |
```
**NEW**
```
| T-DATA-01..06 (**T-DATA-05 †**) |
```

**OLD**
```
| T-SCN-01..09, 11 (10 reserved-unwritten on Q26) |
```
**NEW**
```
| T-SCN-01..09, 11 (10 reserved-unwritten on Q26; **T-SCN-08, 09, 11 †**) |
```

**OLD**
```
| T-UI-01..04 |
```
**NEW**
```
| T-UI-01..04 (**T-UI-03, 04 †**) |
```

**OLD**
```
| T-INT-01..05 |
```
**NEW**
```
| T-INT-01..05 (**T-INT-02, 05 †**) |
```

**OLD**
```
| T-SAVE-01..07 |
```
**NEW**
```
| T-SAVE-01..07 (**T-SAVE-06 †**) |
```

### Pair 9 — §4.11, the legend under the table

**OLD**
```
**Critical path: 1 → 3 → 4 → 5 → 6/8.** Row 2 runs in parallel immediately.
```
**NEW**
```
**† — the cut line (§4.7 head).** A marked ID does not *close* if the calendar
takes it, and what each mark costs is a **claim**, never a rule: no marked ID
guards a rules invariant, so nothing in the game changes behaviour when one
stands down. Unmarked is the default and the majority.

- **T-DATA-05** — row 2's only in-editor half. Fallback is a Director read of
  two frozen tables (4 unit rows × 11 columns, 7 terrain rows × 10). Cost: row
  2's ledger flip, since Q29 requires the full acceptance set at one commit.
- **T-SCN-08, 09, 11** — their fixtures are stretch-map-resident, and §2.13.7
  states the condition plainly: if week 4 is consumed by balance, "the set stays
  on paper." T-SCN-08 then loses fixtures (a) *The Causeway* and (b) *Longwater
  March*, keeping only the synthetic ceiling refusal (c); T-SCN-11 loses fixture
  (c) and keeps its two shipped-map fixtures, including the failing one; and
  T-SCN-09's asserting branch loses both maps, because `symmetry == none`
  asserts nothing and the shipped map declares `none`. T-SCN-01..07 stay
  unmarked — they are what refuses a malformed shipped scenario, T-SCN-04 is the
  precondition of the flag win §4.5 calls a complete MVP, and T-SCN-06 gates the
  §2.11.6 opening §2.11.8 ranks must-have. Cost: row 7's ledger flip, on the same
  Q29 reading as row 2.
- **T-UI-03, 04** — in-editor Automation over widget bindings, where a Director
  reading the screen is a real check. T-UI-01/02 stay unmarked: they are
  headless queries, and T-UI-01 is what makes §2.11.3's forecast equal the
  resolution.
- **T-INT-02, 05 and T-SAVE-06** — the in-editor half of the parity pair
  (T-SAVE-06 is asserted jointly with T-INT-02). This is the most expensive mark
  in the list and its cost is a §3 cost rather than a §1 one: without it the
  shipped engine build is never proven identical to the certified headless
  module, so the ledger's evidence chain stops at the vendoring hash (T-INT-01)
  instead of reaching the artifact that ships. T-INT-01/04 and T-SAVE-01..05
  stay unmarked on **cost** — §4.9 runs T-INT-01/04 on every gate run and §4.10
  takes T-SAVE-01..05 headless, so none of them needs the editor pass in order
  to be asserted (T-SAVE-05 is *also* exercised in-editor via the load UI path,
  which adds coverage rather than owning it). **T-INT-03 stays unmarked on the
  rule, not on cost:** §4.9 does place it in the editor pass, but what it
  asserts — an illegal command leaves the state hash unchanged and returns a
  reason, no partial application — is the bridge behaviour §4.9 contracts ("an
  invalid command returns a rejection reason and changes nothing"), and a marked
  ID may not guard a rules invariant. The consequence is stated rather than
  hidden: an editor pass cut to its marked IDs alone would still owe T-INT-03,
  so this line thins that pass, it never cancels it.
- **T-SAVE-07 is deliberately unmarked**, against the reading that grouped it
  with T-SAVE-06. It is headless and §4.4 closes it on week 4's own self-play
  output; under §2.13.7's slip condition self-play still runs and only the
  stretch maps stand down, so cutting it would buy no calendar.

**Critical path: 1 → 3 → 4 → 5 → 6/8.** Row 2 runs in parallel immediately.
```

---

## TARGET 3 — the two crews that actually ran, in §3's role table

### Pair 10 — two new rows

**OLD**
```
| **Opponent Commander** *(stretch, runtime)* | Agent (LLM) | Play a turn in-product as the enemy | In-game LLM call + move validator | A validated legal move per turn |
```
**NEW**
```
| **Opponent Commander** *(stretch, runtime)* | Agent (LLM) | Play a turn in-product as the enemy | In-game LLM call + move validator | A validated legal move per turn |
| **Documentation crew** *(4 authors)* | Agent ×4 | Draft assigned GDD sections in parallel against a frozen snapshot; write only their own file, never the master (§1.6) | Claude Code sub-agents over a synced read-only snapshot | Section drafts, one file per author |
| **Continuity gate** | Agent | Audit every draft against the live GDD for contradictions, stat drift, dead references and invented numbers; block merge until PASS (§1.6) | Claude Code | Per-section verdicts and violation counts in the gate's accept record |
```

### Pair 11 — the note that places them, and the §1.5 pointer

**OLD**
```
**Pipeline.** Claude Code is the agent client. Two surfaces:
```
**NEW**
```
The last two rows are **document-side** rather than game-side: they authored and
gated this GDD, not the build, and they are the crew §1.6 describes — including
its recorded failure, where the gate filed four violations, the two authors
responsible were re-spawned with them, and only the corrected drafts merged.
They belong in this table because its contract is an I/O contract and those two
were the only roles that had run without one. §1.5's **agent review crew**
(Exploit-Hunter / Consistency / Pacing) gets this pointer rather than a row, for
the opposite reason: its findings were human-adjudicated into §1.5's change
table, so it has no machine-checkable artifact for the last column, and a role
with no verifiable output does not belong in the one table whose purpose is
verifiable outputs.

**Pipeline.** Claude Code is the agent client. Two surfaces:
```

---

## Grounding

| Claim | Backed by |
|---|---|
| Rows 1–3 are §4.4's week-1 deliverable | §4.4 wk 1 cell, verbatim |
| All three read `*pending*` | §3 ledger rows "Hex grid & math", "Data tables (units/terrain)", "Movement & pathfinding" |
| Crew repo holds the Combat module alone; last code commit `5ffa8d6`, 2026-07-29; today 2026-08-01 | Director-supplied, verified |
| Four verified ledger rows | §3, "Four rows are now populated" |
| Critical path 1 → 3 → 4 → 5 → 6/8; row 2 parallel; row 10(a) no deps; T-INT-01/04 depend on no rules row | §4.11 rows 9–10 and the critical-path paragraph |
| UMG skeletons run parallel in week 1 | §4.4 wk 1 cell |
| "Each piece lands in the week the thing that consumes it runs" | §4.4, the Q20/Q23 note, verbatim |
| A gate green over a subset flips no ledger row | §4.4 closing sentence (Q29) |
| 69 written acceptance IDs | Recounted from §4.7 Stubs 1–8, §4.8, §4.9, §4.10, §4.11 |
| Stretch maps stay on paper if week 4 goes to balance; both `rot180` maps are the stretch ones | §2.13.7, the set table and its closing note |
| `symmetry == none` asserts nothing; *Ferrum Crossing* declares `none` | §4.7 Stub 7, T-SCN-09 and the `symmetry` field |
| T-SCN-08's fixtures are (a) *The Causeway*, (b) *Longwater March*, (c) a synthetic both-lanes-7 ceiling refusal | §4.7 Stub 7, T-SCN-08 Fixtures |
| T-SCN-11's fixtures are (a) and (b) *Ferrum Crossing*, (c) *The Causeway* | §4.7 Stub 7, T-SCN-11 Fixtures |
| Unit table 11 columns; terrain table 10 columns (`PassLand`/`PassAir`/`PassSea` is three) | §4.8, the two schema tables, counted row by row |
| T-INT-03 sits in the editor pass | §4.9 Integration parity, Acceptance line |
| An invalid command returns a rejection reason and changes nothing | §4.9, bridge "Command in / events out" bullet |
| T-SAVE-01..05 headless, 05 also in-editor via the load UI path; T-SAVE-06 asserted jointly with T-INT-02 | §4.10 Save & replay, Invariants and Acceptance |
| A row flips only on its full acceptance set | Q29, conservative reading in force |
| T-SAVE-07 closes in week 4 on that week's own logs | §4.4 wk 4 cell |
| T-SCN-06 gates the guided opening; §2.11.8 ranks it must-have | §4.7 T-SCN-06; §2.11.8 must-have list |
| Four gate violations, two authors re-spawned | §1.6 opening paragraph |
| The §1.5 review crew was human-adjudicated | §1.5 opening paragraph |
| No new Q registered here | Deliberate. The register is headed "Open questions (Director rulings owed)" and registering a row is a Director act; the gaps below are filed for ruling, unnumbered, so neither extent-bearing site of the register is touched by this draft |

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.11, critical-path paragraph | "…would leave its ledger row un-flippable and the §2.11.6 guided opening ungated for however long movement slips: **the scenario row flips after movement, not before.**" | Name the second condition alongside movement, in whatever wording you prefer — e.g. "…the scenario row flips after movement, not before; and its **full** acceptance set additionally needs §2.13.7's stretch maps, which may not be pulled forward of week 4." | Movement is necessary for row 7's flip but, under Q29's full-set reading, not sufficient. Three of row 7's ten written invariants have coverage resident on the two maps §2.13.7 keeps in the stretch column and forbids pulling forward of week 4 — itemised below. As drafted, §4.11 names one gating condition where there are two, so a reader watching row 3 land will expect a flip that cannot happen. The draft above asserts none of this: §4.11's legend now states only the fixture facts §4.7 and §2.13.7 already carry, and the rule this observation implies is yours to write, not mine. |

**The three stretch-map-resident invariants, itemised.** All figures from §4.7
Stub 7 and §2.13.7; nothing here is new.

| Invariant | What is stretch-resident | Which map | What survives on shipped scope |
|---|---|---|---|
| **T-SCN-08** | Fixtures (a) and (b) — both of its passing measurements | (a) *The Causeway* §2.13.6 (Stretch P2); (b) *Longwater March* §2.13.5 (Stretch P1) | Fixture (c) only — the synthetic both-lanes-7 refusal against the 6 MP ceiling. A failure case, so the invariant never demonstrates a pass |
| **T-SCN-09** | The whole asserting branch. `symmetry == none` "asserts nothing and is always well-formed"; only `rot180` asserts | Both `rot180` maps are stretch (§2.13.7); the shipped *Ferrum Crossing* declares `none` (§2.13.2) | The well-formedness check on `none`, which asserts nothing about symmetry |
| **T-SCN-11** | Fixture (c), the Bridge-asymmetry case | *The Causeway* §2.13.6 (Stretch P2) | Fixtures (a) and (b), both *Ferrum Crossing* — including the failing pre-fix deployment, so this invariant still demonstrates refusal |

**Departures from the auditor's cut-line split — recorded, not re-argued.** The
reasoning for each is in Target 2 above and is not restated here. The gate did
not overturn any of the three.

| # | Departure | Auditor's placement | Mine |
|---|---|---|---|
| 1 | **T-SAVE-07** | cut side | ship side (unmarked) |
| 2 | **T-SCN-09** | unassigned | cut side (†) |
| 3 | **The 18 unassigned IDs** — T-SCN-01..07 and 09, T-UI-03/04, T-INT-01/03/04, T-SAVE-01..05 | left unassigned | all assigned, per the marks in Pairs 4–8 and Pair 9 |

## Open questions for the Director

Three gaps found while writing the gates above. None is given a Q ID: the
register is headed "Open questions (Director rulings owed)", numbering a row is
a Director act, and both of the register's extent-bearing sites are left
untouched by this draft.

1. **Does a † ID that stands down block its ledger row, or is it waived?** Pair
   9 assumes the blocking reading throughout — "Cost: row 2's ledger flip", and
   the same for row 7 — on Q29's conservative full-set-at-one-commit wording. If
   you instead read a *deliberately deferred* ID as waived rather than absent,
   rows 2 and 7 flip without T-DATA-05 and the T-SCN marks, and every "Cost:"
   line in that legend is wrong. This is the single ruling the whole cut line
   hangs on. **Gate on ruling:** the flip criterion becomes checkable per row —
   `flipped ⇒ every unmarked ID green at one commit`, plus, under the blocking
   reading, `every marked ID green at that same commit`.
2. **May a synthetic `rot180` fixture stand in for a stretch map?** T-SCN-09's
   asserting branch and T-SCN-08's two passing fixtures need a `rot180` *file*,
   not necessarily a playable scenario. §2.13.7 forbids pulling stretch **map**
   work forward of week 4; it says nothing about a fixture-only file. If a
   minimal hand-authored `rot180` grid is admissible as test data, all three
   invariants close on shipped scope and the change request above may be
   unnecessary. If it is not, the coupling is real and permanent. This is a
   scenario call, not a schema one (see Handoffs). **Gate on ruling:** if
   admissible, T-SCN-08/09 lose their † marks and gain a fixture-provenance
   assert — the fixture file is not a shipped scenario and is excluded from the
   scenario manifest; if not, the marks stand as drafted.
3. **Is the in-editor Automation pass optional at all?** The cut line's premise
   is that a marked ID's editor pass can be skipped. But §4.9 leaves T-INT-03 in
   that pass and the rules-invariant rule leaves it unmarked, so the pass is
   thinned, never dropped — which means "the calendar takes the editor pass" is
   not an available move, only "the calendar takes most of it." Either T-INT-03
   needs a headless assertion path (a §4.9 change, not mine to write) or §4.7's
   cut line should say plainly that one editor pass always runs. **Gate on
   ruling:** either way the assertable form is `T-INT-03 green at every commit
   that flips row 9`, and the ruling decides which harness produces it.

## Handoffs

- **rules-designer** — nothing owed. No pair here states or restates a rule.
- **scenario-designer** — the T-SCN-08/09/11 marks say the stretch maps carry
  fixture load, not just replay value. If the set stays on paper, row 7's ledger
  row cannot flip. Whether a synthetic `rot180` fixture (the shape of T-SCN-08's
  fixture (c)) should stand in for the two stretch maps is a scenario question,
  not a schema one, and I have not assumed an answer — it is Open question 2.
- **ux-onboarding-designer** — T-UI-03/04 are marked †, so the production menu
  and scoreboard bindings lose their Automation gate under calendar pressure.
  No layout claim is made; only how those two widgets are *checked*.
- **Director** — the row-7 finding previously stated inside the §4.11 legend is
  now a **change request** against §4.11's "the scenario row flips after
  movement, not before", with the three stretch-resident invariants itemised map
  by map. The legend asserts nothing beyond what §4.7 and §2.13.7 already state.
  Three unnumbered open questions are filed above; each names the gate its
  ruling would produce, so an answer turns straight into an assert.

---

## PLACEMENT

| Pair | Section | Exact site |
|---|---|---|
| 1 | §3 | The italic *Status: live tracker* line above the provenance ledger — two sentences appended inside the closing italic marker |
| 2 | §4.5 | One new row appended to the risks table, after "Agent code quality" |
| 3 | §4.7 | New paragraph between the opening preamble and "**Shared conventions**" |
| 4 | §4.11 | Build-order table, row 2, Acceptance cell |
| 5 | §4.11 | Build-order table, row 7, Acceptance cell |
| 6 | §4.11 | Build-order table, row 8, Acceptance cell |
| 7 | §4.11 | Build-order table, row 9, Acceptance cell |
| 8 | §4.11 | Build-order table, row 10, Acceptance cell |
| 9 | §4.11 | New legend block immediately under the build-order table, above the "Critical path" paragraph |
| 10 | §3 | Two rows appended to the role table, after "Opponent Commander" |
| 11 | §3 | New paragraph between the role table and "**Pipeline.**" |

No pair touches §1, §2, or the Q register. T-SCN-11's text is not opened; pair 5
edits only the Acceptance cell of §4.11 row 7, and pair 9 inserts below the
table. The change request against §4.11's critical-path paragraph is a request,
not a pair: it carries no OLD/NEW block and merges nothing until the Director
writes the wording.

---

## SUMMARY FOR THE DIRECTOR

Eleven replacement pairs across §3, §4.5, §4.7 and §4.11, each OLD block
verified to occur exactly once in the synced source. §3's ledger status line now
dates itself at 2026-08-01, names §4.4 week 1's three unstarted rows and states
that weeks 2–3 move with week 1 one for one because the critical path runs
through all three; §4.5 gains a seventh risk row, *Specification outruns the
build* — 69 written acceptance IDs against 4 verified ledger rows — whose
mitigation is the cut line plus §4.4's own principle that each piece lands in
the week the thing that consumes it runs, and Q29's rule that a subset pass
flips nothing. The cut line itself is a three-line note at the head of §4.7 plus
a **†** mark on nine IDs in §4.11's build-order table, with a legend naming what
each mark costs; I recounted the IDs and got 69, and my three departures from
the auditor's split — T-SAVE-07 to the ship side, T-SCN-09 to the cut side, and
the eighteen unassigned IDs assigned — are now recorded in a Change requests
table rather than left in prose. §3's role table gains the Documentation crew
and Continuity gate rows with full I/O contracts, and §1.5's review board gets a
pointer rather than a row. The row-7 finding is unchanged in substance but moved
to where a finding belongs: §4.11's legend no longer asserts that row 7 cannot
flip on shipped scope, and instead a change request against "the scenario row
flips after movement, not before" itemises the three stretch-resident
invariants — T-SCN-08's fixtures (a) *The Causeway* and (b) *Longwater March*,
T-SCN-09's entire `rot180` asserting branch, and T-SCN-11's fixture (c) *The
Causeway* — for you to rule on. Three unnumbered open questions accompany it,
each with the assert its ruling would produce.
