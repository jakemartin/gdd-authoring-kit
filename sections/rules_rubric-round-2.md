# Rules — rubric-round-2 addendum (rules-designer)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All replacement pairs in this file were applied verbatim to the master GDD
> and merged. Re-applying them would fail (the OLD anchors no longer match) or,
> worse, double-apply an insertion. Gate record: run `rubric-round-2d`, PASS,
> zero violations. Later changes to these sections need a NEW addendum file.

This file is an **addendum**, not a draft. Every section it touches is already
merged. Each change is an exact OLD → NEW replacement pair; each OLD block was
verified to occur **exactly once** in `source/gdd.md` before it was written
here. `sections/rules.md` from the earlier stage is superseded and must **not**
be re-merged — it predates the ruling cycle recorded below.

Two pairs, in file order: **Pair A** inserts §1.7, **Pair B** replaces §2.10's
table. Pair B implements the **corrected** boundary (§4.7 Stub 7 is IN, not
STRETCH); §4.11 rows 7 and 10 were re-read before it was written, and the
reasoning is under *Considered and not filed*.

---

## Pair A — insert §1.7 immediately after §1.6

The OLD block is the last row of §1.6's table (the unique text §1.7 is inserted
*after*). The NEW block reproduces it, then adds §1.7. The `---` divider that
currently follows §1.6 stays where it is, after §1.7.

**OLD**
```
| 5 | **§2 had drifted after the Conflict fold** *(continuity audit)*. Bridge and Factory had been folded into §2.3's terrain set, but §1 and §2.10 still said "five terrains," and §2.8's tiebreak had grown an apparatus nobody had re-justified. | Consolidated **§2.1–§2.10**, reconciled the terrain count across §1/§2.3/§2.10, and subjected the whole Fame/tiebreak apparatus to a **delete-test** — every piece removed in turn to see what breaks (§2.8's closing block). | The tiebreak now survives on evidence rather than inertia: the one piece that failed its delete-test (the floated per-turn Fame decay) was cut, and what remains is a guard, a sort, and an enum over state the game already tracks. |
```

**NEW**
```
| 5 | **§2 had drifted after the Conflict fold** *(continuity audit)*. Bridge and Factory had been folded into §2.3's terrain set, but §1 and §2.10 still said "five terrains," and §2.8's tiebreak had grown an apparatus nobody had re-justified. | Consolidated **§2.1–§2.10**, reconciled the terrain count across §1/§2.3/§2.10, and subjected the whole Fame/tiebreak apparatus to a **delete-test** — every piece removed in turn to see what breaks (§2.8's closing block). | The tiebreak now survives on evidence rather than inertia: the one piece that failed its delete-test (the floated per-turn Fame decay) was cut, and what remains is a guard, a sort, and an enum over state the game already tracks. |

## 1.7 Revision Notes — Production Draft → the ruling cycle

§1.6's four-author crew did not only add sections. Wherever a gate needed a
rule the document did not state, the crew was forbidden to invent one and filed
it instead as a numbered open question in **§4.7's register**, with the
conservative reading it would ship under while the question stayed open. This
revision is the pass in which those questions were **ruled** — one row at a
time, each ruling written into the register beside the question it answers,
together with every site the answer reached. §4.7's register is the
authoritative record of which rows exist and what each was ruled; the five
entries below are the ones that changed the *game* or its evidence, rather than
a gate's wording.

What they have in common is the growth worth reporting: **a ruling is not
finished when the row is answered — it is finished when every site that
depended on the answer has been found and corrected.** Four of the five cost
more edits outside the row than inside it, and in two cases the ruling was
carried out, re-checked, and then amended. Changes are listed as **finding →
change → why it's better**.

| # | Finding (source) | Change | Why it's better |
|---|---|---|---|
| 1 | **Income the document did not have** *(§4.7 register, Q8)*. §2.7 twice asserted that both sides have income from turn 1 — "both players have income from turn 1" and "plus home-factory income from turn 1" — while the shipped scenario priced its own opening the other way: §2.13.2 buys East's turn-1 Infantry with "100 of the 200 starting Fame," not of 300. Two sentences and a map disagreed about the first turn, and two gates (T-FAME-02, T-FAME-04) were written-and-blocked on the disagreement. | Ruled: income accrues at the **start** of the owner's turn and is spendable in that same turn's economy phase, but there is **no accrual on turn 1** — turn-1 buying power is the side's starting Fame alone. The correction rewrote **four §2.7 bullets** (factories, Income, build-and-spawn, starting Fame), §2.9's economy phase, T-FAME-02 and T-FAME-04, and the starting-Fame and build lines in `kb/rules.md`. | The reading chosen was the one the map was **already priced on**, so **no map number moves** — the edit lands on prose that had drifted, not on balance. Both blocked gates now assert, and the shipped scenario's opening turn means what §2.13.2 says it means. |
| 2 | **Two sections, two schedules** *(Q23, Q20)*. §4.4 promised a working vertical slice *with* the baseline AI in week 2, while §4.11's critical path (`1 → 3 → 4 → 5 → 6/8`) and §2.10 both put capture and Fame production in week 3. Separately, §4.10's format sat in week 5 although the week-2 integration gate's input file **is** a save. | Ruled on one principle in opposite directions: the vertical slice moved **later** (week 3; week 2 delivers move + attack only), and the §4.10 **format + headless replayer** moved **earlier** (week 2), leaving only the save-slot UI and slot I/O in week 5. The principle is now stated once, in §4.4: **a format is a test instrument; slot I/O is a feature.** The Q20 ruling was then **amended** — it had been written into §4.4 without re-reading §4.11's dependency table — and repaired by **scoping each gate to the command set of the log it replays**, without moving a week number. | §1, §2.10, §4.4 and §4.11 now describe one schedule, and the rule that settles the next scheduling argument is written down instead of re-derived each time. The amendment is the more useful half: the third disagreement between those two sections was closed by naming a gate's scope rather than by moving work again — and what a partially-scoped gate may claim was registered (Q29) rather than assumed. |
| 3 | **A new invariant refused the shipped map** *(Q22, Q28)*. Gating §2.13.1's promise that the guided lane is "uncontested, not merely reachable" produced **T-SCN-11**, and measuring it across all three maps *before* writing it found five of six lanes clear and one exact tie: West's lane to the South factory cost 5 MP, and East's second Infantry at (9,5) reached that same factory in 5 MP flat. | **The map was corrected rather than the rule loosened.** East's second Infantry deploys at **(9,1)**; no terrain, factory or town count, lane cost, home-factory rule or turn estimate moved with it, and *Ferrum Crossing* now reports **5 against 6 in both seats**. The pre-fix deployment is retained as T-SCN-11's fixture (b). | The suite now owns "a failing case that was actually authored, that passes every other invariant in the suite" — a negative fixture the project produced rather than one a test author constructed, which is the difference between a test that can refuse a real scenario and one that agrees with the repo. It also marked the single row where the register's conservative-reading convention could not hold, and the register now states that limit once. |
| 4 | **An unpriced term inside the primary sort key** *(Q6)*. §2.7's "small bonus" for an undamaged strike had no number, yet combat Fame is the **primary** sort key of §2.8's cap tiebreak — a number nobody had chosen was helping decide capped matches. | Ruled **cut**, not priced: kills already pay half cost and the positional triangle already rewards a clean standoff strike with tempo, so the bonus was paying twice for one thing. The cut reached **six sites that never cited Q6** — §2.8's tally definition, §2.11's standings row and its tooltip, the §2.11.6 one-shot toast, the concept ledger's RPS row (whose receipt is now the range-2–3 one-shot), and two lines in `kb/rules.md`. | Cutting removes the unpriced term from the tiebreak instead of leaving an unchosen number inside it, and it is cheaper than the alternative, which would have made the document carry two Fame totals — one for the pool, one for the cap tally — in both the kb economy block and the T-CAP- suite. The six uncited sites are the transferable lesson: grepping the identifier alone would have found none of them. |
| 5 | **The token budget priced one thing twice** *(§4.6)*. The Opus escalation is a *delta* between two models on the same task. An earlier draft folded it into the dev-time subtotal and then applied it a second time to reach **$225** — which is why three figures in one table disagreed. A second fault in the same table scaled the 1.5× overrun off a *rounded* subtotal. | Re-derived every figure from the two rate lines and the task count, and quoted the escalation delta **unrounded** ($1.035) at every site that uses it. The subtotal is **$178.02**; the overrun case is re-derived rather than scaled, landing at **≈ $266**, with **$303** stated as the ceiling. | Both faults were visible **only because the table is fully re-derivable from its inputs** — the property is what caught them, so it is now the table's stated discipline rather than an accident. A budget that can be recomputed is auditable; one that quotes a total is not. |
```

---

## Pair B — replace §2.10's scope table

**OLD**
```
| | Contents |
|---|---|
| **IN** (core; phased wk 1–3 per §4.4) | Grid; 4 units; **6 terrains + the Factory tile**; move + attack; **multiple factories** (home-per-side + contested neutrals, ~4) + capture + Fame production *(these land wk 3, not wk 1–2)*; heuristic AI; **one hand-built scenario**; win-by-flag; functional UI |
| **STRETCH** (if ahead) | 2nd–3rd scenario; LLM commander; fog/recon; sea/air units; map-gen MCP toolset; 2-player hotseat |
| **CUT** | All 16 original scenarios; campaign/meta; zones of control; elaborate art; anything real-time |
```

**NEW**
```
| | Contents |
|---|---|
| **IN** (core; the playable core phased wk 1–3, the remainder scheduled in §4.4) | Grid; 4 units; **6 terrains + the Factory tile**; move + attack; **multiple factories** (home-per-side + contested neutrals, ~4) + capture + Fame production *(these land wk 3, not wk 1–2)*; heuristic AI; **one hand-built scenario**, with the scenario file and headless validator it loads through (§4.7 Stub 7); win-by-flag; functional UI; the **§2.11.6 guided opening** — four beats, first match only *(onboarding, wk 5)*; the **§4.10 save/replay format + headless replayer** — *instrument, not feature* *(wk 2)*; minimal single-slot save/load *(wk 5)* |
| **STRETCH** (if ahead) | 2nd–3rd scenario authored on that format — *Longwater March* (P1, wk 4) and *The Causeway* (P2, wk 4) — shipping under the conditions §2.13.7 states, which that section states alone; LLM commander; fog/recon; sea/air units; map-gen MCP toolset (§4.2) — the in-editor wrapper only, not the validator it wraps; 2-player hotseat |
| **CUT** | All 16 original scenarios; campaign/meta; zones of control; elaborate art; anything real-time |

**Reading this table.** Four notes, so that a scope question and a schedule
question are answered on the same page:

- **§1's *Scope at a glance* and this table are not the same line.** §1 names
  the smallest set that is already a complete game — §4.5's hard MVP line. This
  table names what is **scheduled**, which is a superset of it.
- **Instrument, not feature.** The §4.10 format and headless replayer are IN
  because two gates run on them, not because a player asks for them: T-INT-02's
  input file is a save, and the week-4 self-play logs T-SAVE-07 validates are
  the same format (§4.4, §4.11 row 10). §4.4 states the rule this turns on —
  *a format is a test instrument; slot I/O is a feature* — so the format is
  core, the save-slot UI is the ordinary week-5 UI half, and no player-facing
  replay is scoped.
- **Off the critical path is not the same as stretch.** §4.11 says nothing in
  its chain waits on row 7, and §4.7 Stub 7 is nonetheless core: §4.4 has the
  one scenario loading, validating and rendering in week 2; §4.11 row 8 (UI
  binding) depends on row 7 because the snapshot needs full state; row 10(b)'s
  replayer reads the `scenarioId`/`scenarioHash` it produces; §2.8's turn cap is
  its `turnCap` field; and §2.11.6's guided opening is driven by its
  `guidedOpening` entries. What is stretch is the **second and third scenarios
  authored on that format**, and the in-editor toolset that wraps the
  validator — the manual fallback stands (§4.11 row 7).
- **A STRETCH row is a promise about cost, not about intent.** Where a section
  already states the condition an item ships under, that section owns it and
  this table does not restate it — for the two stretch maps that section is
  §2.13.7.
```

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.10 IN row label | `**IN** (core; phased wk 1–3 per §4.4)` | `**IN** (core; the playable core phased wk 1–3, the remainder scheduled in §4.4)` — **already implemented in Pair B**, filed here so it is not a silent edit. | The label was already loose (functional UI runs to wk 5), and the two systems this edit adds land in wk 2 and wk 5. Leaving "phased wk 1–3" over a cell containing wk-5 onboarding would recreate exactly the §4.4-vs-table drift Q23 closed. Both week numbers exist in §4.4; §1 supplies "Core playable in weeks 1–3." No new number is introduced. |

**No change request is filed against Q13.** An earlier revision of the STRETCH
cell listed a player-facing replay viewer while the same NEW block stated that
none is scoped — which asserts both readings of Q13 at the one site Q13's
Blocks column names. The entry is removed rather than re-argued: Q13's reading
in force keeps the §4.10 format internal, and the *instrument, not feature*
note already states that outcome once. If the Director wants Q13 ruled open
rather than left on its conservative reading, that ruling belongs in §4.7's
register, and §2.10 would follow it — not lead it.

**Considered and not filed — splitting Stub 7 along its structural/priced
seam.** §4.11 row 7 does draw that seam, so it was tested against the scope
line before Stub 7 was placed whole. It does not carry scope: the priced half
(T-SCN-04, 06, 08, 11) waits on **row 3, movement**, which is week-1 core work
on the critical path, and §4.11 states the consequence as a *flip order* —
"the scenario row flips after movement, not before" — not as a cut. Its own
sentence gives the reason a delay is not a demotion: scheduling row 7 as
parallel-from-week-1 would leave "the §2.11.6 guided opening ungated," and that
guided opening is IN. Both halves are therefore core, and splitting the row
across IN and STRETCH would invent a scope seam out of a dependency seam. Stub
7 is placed **whole, in IN**; only the in-editor MCP wrapper around it is
stretch, which is where §2.10 already had it.

---

## Open questions for the Director

1. **Should §2.10 name single-slot save/load at all?** Pair B's IN cell adds
   `minimal single-slot save/load *(wk 5)*` so the instrument/feature split is
   legible in one cell — the format IN as an instrument, the slot as an ordinary
   feature. It is grounded (§4.1, §4.4 wk 5), but the pre-existing table named
   no save surface at all. If you want the table silent on the feature half,
   strike that clause; the *instrument* clause stands without it. Blocks only
   that clause.
2. **What is this revision called?** §1.5 and §1.6 each name a draft-to-draft
   transition. I titled §1.7 "Production Draft → the ruling cycle" so the three
   read as one history, but the target draft has no name yet. This blocks §1.7's
   heading only, and it is a one-line fix at merge.
3. **Should §1.7 ever state a register count?** It deliberately does not.
   §4.7's own preamble warns that its extent-bearing sites go stale whenever a
   row is registered — which is how one of them staled already — so §1.7 points
   at the register and quotes no total. If you want a headline number in §1, it
   needs an owner who re-derives it at every merge; otherwise §1.7 stays
   countless by design. Blocks nothing today; it is a standing decision.

---

## Handoffs

- **`scenario-designer` (§2.13.7).** Pair B's STRETCH cell defers to §2.13.7 as
  the single statement of the conditions the two stretch maps ship under, and
  states none of them itself — including their ordering. The cell carries only
  identifying labels, and takes them from §2.13.7's own scenario-set summary
  row: *Longwater March* (Stretch P1, wk 4) and *The Causeway* (Stretch P2,
  wk 4). If those labels or that section's conditions move, §2.10 loses its
  referent; if the conditions are reworded, §2.10 needs no edit.
- **`ux-onboarding-designer` (§2.11.8).** §2.11.8's must-have list already
  contains "directive strip with the four beats," and Pair B now names the same
  system IN in §2.10 — one claim, two sites, worth checking together at merge.
  §2.11.8's polish list also calls a dedicated micro-tutorial map "explicitly
  stretch — it would occupy a stretch scenario slot, §2.10"; Pair B leaves that
  slot where it was rather than adding a fifth stretch line, but the pointer now
  aims at a rewritten cell.
- **`ux-onboarding-designer` / `tech-director` (§4.10).** §4.10 records
  overwrite-confirm UX as **unowned** — "either §2.11 gains the surface, or the
  prototype ships silent single-slot overwrite." Pair B names single-slot
  save/load IN without resolving that; it is a §2.11 screen decision, not a rule.
- **`tech-director` (§4.7 register, Q13).** Q13's Blocks column names "the
  §2.10 scope table; a UX handoff if it is scoped." Pair B scopes no viewer, so
  no UX handoff falls out of it, and Q13's conservative reading still holds
  unchanged. If Q13 is ever ruled the other way, §2.10's STRETCH row is the
  site that gains a line.
- **`tech-director` (§4.11 row 7).** §2.10 now states that Stub 7 is core and
  its in-editor wrapper is not. §4.11 row 7's cell already says "MCP tool wraps
  it in-editor, manual fallback stands," so nothing there needs to move — but if
  that clause is reworded this round, the STRETCH cell's "not the validator it
  wraps" is the line that depends on it.
- **Merge checklist.** `kb/rules.md` carries no scope block and no §1 material,
  so neither pair forces a kb re-sync on its own. §1.7 reports rulings already
  merged, so no §3 ledger row changes status because of it.

---

## Grounding

**Pair B — §2.10.**

| Claim in the draft | Source |
|---|---|
| IN gains the §4.10 format + headless replayer, week 2 | §4.4 wk 2 ("**and the §4.10 save/replay format + headless replayer** (Q20, ruled)"); §4.11 row 10; Q20's ruling cell |
| "instrument, not feature"; T-INT-02's input is a save; wk-4 self-play logs are the same format | §4.4 wk 2 and the note beneath the milestone table ("a format is a test instrument; slot I/O is a feature"); §4.10's four consumers, items 2 and 3; §4.11 row 10 |
| Save-slot UI / slot I/O is the wk-5 feature half; minimal single slot | §4.4 wk 5; §4.10 "Policies (prototype) — Single slot" (`slot0`, `USaveGame` wrapper); §4.1 "Save/load: minimal single-slot for the prototype" |
| No player-facing replay is scoped; the STRETCH row lists no viewer | Q13 (§4.7 register): "The format stays internal — saves, gates, and balance logs only"; its Blocks column names §2.10's scope table |
| IN gains §2.11.6's guided opening; four beats; first match only; wk 5 | §2.11.6-B (beats 1a, 1b, 2, 3; "once all four beats have retired"); §2.11.6 ("Any completed match on the save skips all guidance automatically"); §4.4 wk 5 ("onboarding"); §2.11.8's must-have list |
| Scenario file + headless validator IN (§4.7 Stub 7) | §4.4 wk 2 ("plus the one scenario loading, validating and rendering"); §4.11 row 8 depends on "5, 7 (snapshot needs full state)"; §4.11 row 10(b) needs row 7's structural half for `scenarioId`/`scenarioHash`; §4.7 Stub 7's schema rows `turnCap` and `guidedOpening array`; §2.8 and §2.11.4 read `turnCap` from the scenario; §2.11.6 and §2.13.1 drive beat 1a/beat 2 off `guidedOpening.infantry` / `guidedOpening.objective` |
| Off the critical path ≠ stretch; the row flips after movement | §4.11: "Row 7 is still not ON the critical path (nothing in the chain waits on it), but scheduling it as 'parallel from week 1' would leave its ledger row un-flippable and the §2.11.6 guided opening ungated … the scenario row flips after movement, not before" |
| MCP toolset is the stretch in-editor wrapper; manual fallback stands | §4.2 ("Custom MCP toolset … `validate_scenario`"); §4.4 wk 3 ("the custom MCP scenario toolset follow only if the slice lands early; both are off the critical path"); §4.11 row 7 ("MCP tool wraps it in-editor, manual fallback stands") |
| Stretch-map labels: *Longwater March* (P1, wk 4); *The Causeway* (P2, wk 4) | §2.13.7's scenario-set summary, Status column: "Stretch P1 (wk 4)" and "Stretch P2 (wk 4)" |
| §2.13.7 alone states the conditions those two maps ship under; §2.10 states none of them | §2.13.7's scenario-set summary and the paragraph beneath it; the fourth "Reading this table" note, which disclaims restating conditions |
| §1's scope-at-a-glance is the MVP line | §1 "Scope at a glance"; §4.5 "Hard MVP line; 1 scenario + flag win is complete" |
| "playable core phased wk 1–3" | §1 "Core playable in weeks 1–3"; §4.4 wk 1–3 |
| Everything else in the three rows | Unchanged from the existing §2.10 table |

**Pair A — §1.7.**

| Claim in the draft | Source |
|---|---|
| The crew filed gaps as numbered questions with a conservative reading rather than inventing rules | §4.7's stub preamble ("the gate is parameterized on a numbered open question"); the register preamble ("where a reading is stated, it is the conservative one") |
| §4.7's register is authoritative for which rows exist | Register preamble: "the table below is authoritative for which rows exist, and any count must be taken from it" |
| Row 1 — the two §2.7 sentences; no accrual on turn 1; four §2.7 sites; §2.9, T-FAME-02/04, `kb/rules.md`; "no map number moves"; §2.13.2's 100-of-200 pricing | Q8's ruling cell |
| Row 1 — T-FAME-02/04 were written-and-blocked and now assert | Register preamble ("the gates they blocked outright … now assert"); Q8's Blocks column |
| Row 2 — §4.4's week-2 slice vs §4.11's `1 → 3 → 4 → 5 → 6/8` and §2.10's wk-3 clause | Q23's question and ruling cells; §4.4's note "On weeks 2–3 (Q23, ruled)" |
| Row 2 — split not moved; the stated principle; the amendment and its repair by scoping; Q29 registered | Q20's ruling cell; §4.4's note beneath the milestone table; §4.11's closing paragraph |
| Row 3 — T-SCN-11 measured over three maps; five clear, one exact tie; West's 5 MP lane vs East's (9,5) at 5 MP flat | Q22's ruling cell |
| Row 3 — map corrected not rule loosened; (9,5) → (9,1); nothing else moved; 5 against 6 in both seats; fixture (b) | Q28's ruling cell |
| Row 3 — "a failing case that was actually authored, that passes every other invariant in the suite" | Q28's ruling cell (quoted) |
| Row 3 — the one row where the conservative-reading convention could not hold | Register preamble: "**Q28 was the one row where that convention did not hold**" |
| Row 4 — no number; feeds the tiebreak's **primary** sort key; ruled cut; six uncited sites, itemised; two Fame totals avoided; the grep lesson | Q6's ruling cell |
| Row 5 — escalation is a delta; applied twice to reach $225; three figures disagreed; $1.035 unrounded; $178.02; ≈ $266; $303 ceiling; re-derivability caught both faults | §4.6's escalation line, the paragraph "The escalation is priced once," and the Headline paragraph |
| Format: `#` / finding → change → why it's better; the "Finding (source)" column head | §1.5 and §1.6 table headers |

**Deliberately not claimed.** §1.7 states no count of ruled or open register
rows, no test-suite totals, and no week numbers beyond those §4.4 already
prints. Every figure in it — 200, 300, 100, (9,5), (9,1), 5, 6, $225, $1.035,
$178.02, $266, $303 — appears in `source/gdd.md` at the site cited above.
Pair B states no condition of its own for the two stretch maps: it names them,
their P1/P2 order label and their week, and defers.

---

## PLACEMENT

- **Pair A** — `source/gdd.md` line 72, the final row of §1.6's table. The NEW
  block reproduces that row unchanged and appends **§1.7** beneath it. §1.7
  therefore sits between §1.6's table and the existing `---` divider that
  precedes `## 2. Game Mechanics`; that divider does not move. Nothing else in
  §1 is touched.
- **Pair B** — `source/gdd.md` lines 406–410, the whole three-row table under
  `### 2.10 Scope table`. The NEW block replaces the table and appends a
  four-bullet "Reading this table" note beneath it. The `### 2.10 Scope table`
  heading itself is in neither block and does not move; the blank line before
  `### 2.11 UI/UX` is preserved.
- Both OLD blocks were grep-verified as **exactly one** occurrence in
  `source/gdd.md`. Neither OLD block was altered by this revision — the two
  fixes fall entirely inside Pair B's NEW block — and both were re-verified
  against the current `source/gdd.md` after the fixes. No other section is
  edited by this file.

---

## Summary for the Director

§2.10's scope table now agrees with the sections that schedule the work. The IN
row gains three systems that were already week-scheduled and unstated here: the
§4.10 save/replay format and headless replayer, marked *instrument, not
feature* on Q20's own principle; §2.11.6's four-beat guided opening; and §4.7
Stub 7's scenario file and headless validator. The STRETCH row states what had
been sitting unstated — the second and third scenarios authored on that format,
*Longwater March* (P1, wk 4) and *The Causeway* (P2, wk 4), shipping under
conditions §2.13.7 states and this table does not — plus the in-editor MCP
wrapper, now explicitly distinguished from the validator it wraps. Two
corrections were filed by the gate and both are taken as removals: the ordering
clause `only after P1` is gone from the STRETCH cell, because an ordering is a
condition and this table disclaims restating conditions — §2.13.7 is the single
authority and the cell now carries labels only; and the player-facing replay
viewer is gone, because listing it while the same block states none is scoped
asserted both readings of Q13 at the one site Q13 points at. **The one
consequential call:** §4.11 row 7's structural/priced seam is a *dependency*
seam, not a scope seam — its priced half waits on movement, which is week-1
core — so Stub 7 is placed whole in IN rather than split, and the reasoning is
recorded under *Considered and not filed* rather than left implicit. §1.7 lifts
the ruling cycle out of §4.7's "open questions" table into §1, as a five-row
finding → change → why table in §1.5/§1.6's exact format: Q8's turn-1 income,
Q23 + Q20's two schedules, Q28's invariant that refused the shipped map, Q6's
unpriced tiebreak term, and §4.6's double-counted escalation. Every figure is
lifted from the register, no count of the register is stated, and no ruled row
is re-opened. One change request stands, for the IN row's `wk 1–3` label; none
is filed against Q13.
