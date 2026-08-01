# Rubric audit — 2026-08-01 (rubric-auditor)

**Document scored:** `source/gdd.md`, md5 `3b9024f384162b32959416b66f5f1137` (per
`source/MANIFEST.txt`), **2578 lines**.
**Sync check:** the previous audit (2026-07-30) scored md5
`7367b1961aae90b544f3837a9c7e6cd1`. The manifest md5 differs from it, so the
nineteen merge cycles since **were** synced. `gate/accept.json` records run
`post-merge-21` against this same md5 — the gate audited the document I am
scoring, not a predecessor. Scoring proceeds.
**Gate context:** `gate/gate_report.md` run `post-merge-21` returns PASS, 7
sections, 0 violations. Note for the record what that run contained: its entire
delta was **one paragraph in §4.7's register preamble defining two senses of the
word *blocked***. That is the state of the most recent full gate cycle.
**Scope of this report:** part 1 scores the current document from scratch. Part 2
reconciles the old report's five edits. They are kept separate.

---

# Part 1 — Score, from the current document only

## Scores

| Line | Score | Max | Evidence (section + quote) |
|---|---|---|---|
| **Game Specificity** | **2.8** | 3.0 | Deepened well past the last audit. §2.13.2 now prices eight routes as integers and defends a single deployment hex for a page: *"**Why East's second Infantry sits at (9,1) and not (9,5).** At (9,5) it was 5 MP from *West's* South objective — a dead tie with West's own lane, which T-SCN-11 refuses… East's south town (7,6) is only 2 hexes from South (5,7), so by the triangle inequality anything within 3 MP of that town is within 5 MP of that factory."* No other game produces that sentence. §2.11.6's beat schedule is derived from *this* map's margins — *"On *Ferrum Crossing* both lanes cost **5 movement points**… Against the 6 MP budget that is **1 MP of slack**"*. §4.8 still names real columns and real values (*"`DefensePct` … §2.3 (0, 20, 40, 0, 10, **−10**, 15)"*). **Lost 0.2 to two unchanged generic patches, now more conspicuous than before.** §2.11.7 is still titled *"Art (unchanged)"* and is still two sentences — *"Flat/low-poly color-coded hexes, simple unit meshes or billboarded icons, generative/agent-assisted"* — the whole visual deliverable of a product graded on being playable. And §4.5's risk table is the same six one-line rows it carried in the first draft (*"AI rabbit hole \| Ship the heuristic; LLM behind a toggle"*); not one of them names a risk this document has actually run. Third, smaller: §2.11.4 still ships four faction-voiced strings *"(per the setting guide…)"* — `kb/setting.md` defines both the Directorate and the Vanguard, and the GDD never names the file. |
| **Revision & Growth** | **1.8** | 2.0 | The strongest line relative to its ceiling. §1.6 is a five-row finding → change → why table, each row naming its source: *"**No stated player-experience goals** *(rubric feedback, −0.5)*"* → §2.0's PX-1..6 → *"A goal that cannot be checked is a preference, not a goal."* It also documents the authoring method and a real failure: *"It did not pass on the first attempt: the gate filed four violations… the two authors responsible were re-spawned with those violations, and only the corrected drafts merged."* §1.5's six rows stand behind it. Beyond that, §4.7's register narrates self-correction relentlessly — *"an earlier draft of this row asserted the two were the same and they are not"* (Q9), *"**The map was corrected rather than the rule loosened**"* (Q22), *"the second arithmetic fault this table has surfaced by being fully re-derivable"* (§4.6). **Lost 0.2 for placement, not absence.** §1.6's heading is *"Final Draft → Production Draft"* and its five rows describe the Stage 1+2 merge. The ruling cycle since — Q8 rewriting §2.7's income timing across four bullets, Q20 and Q23 rebuilding §4.4's milestones, Q28 moving a shipped map's deployment — appears nowhere in §1. It is all narrated, 2200 lines in, inside a table headed *"Open questions (Director rulings owed)."* Growth filed under "open questions" is not filed under "revision," and a grader reads §1. |
| **Agent Role Clarity** | **1.8** | 2.0 | The gap that cost 0.4 last time is closed. §3's seven-role table still gives four columns each (*"**Test Engineer** \| Agent \| Write + run the automation/unit-test suite; block merges on failures \| Claude Code + test harness \| Passing test suite (the merge gate)"*), the `SPEC: Combat resolution` block still shows the contract shape, and T-COMBAT-07 is still a real failure case. What is new is the Director's **input set**, which did not exist before: §4.7's register runs Q1–Q31 with ID / Question / **Blocks** / Assumption-in-force — *"**Fifteen of the thirty-one rows are ruled; the other sixteen remain open but *readable***"* — and the preamble even defines its own vocabulary of blocking (*"written-and-blocked"* vs *"reserved and unwritten"*). Every Q-reference in §4.7–§4.11 now resolves. **Lost 0.2 on one omission.** §3's role table names seven roles; the crew that produced the most auditable output in this project — the four-author documentation crew and the continuity gate, 24 files in `sections/` and 21 gate runs — has **no row**. §1.6 describes both in prose, including their failure mode, but the table that defines Owner / Responsibility / Instrument / Verifiable output gives them none. §1.5's *"agent review crew (an Exploit-Hunter / Consistency / Pacing board)"* is likewise absent. Also uneven: §4.10 declares *"Overwrite-confirm UX is **unowned**"* and carries no Q ID, while the structurally identical §2.11.5 seam was correctly registered as **Q31**. |
| **Scope Realism** | **0.8** | 1.5 | **Down 0.1. This is the line the document is losing on, and the loss grew.** Real credit first: Q23 and Q20 resolved the §4.4/§4.11 schedule contradiction on a stated principle — *"**a format is a test instrument; slot I/O is a feature**"* — and §4.11 now splits every gate into what it needs to **run** and to **close**. §2.13.7 keeps a hard cut line. Q29 refuses to flip a ledger row on a partial pass. Now the losses. **(a) The ledger held at 4 built / 8 `*pending*` while the calendar moved.** §3's four verified rows all cite one commit, `5ffa8d6`, dated *"2026-07-26"* and *"2026-07-29"*. Today is 2026-08-01. §4.4 week 1 promises *"§4.11 **rows 1–3** (grid and hex math, the §4.8 tables, movement and pathfinding) … **+ test suite.** Playable via debug commands."* All three of those rows read *"Hex grid & math \| *pending* … Movement & pathfinding \| *pending* … Data tables (units/terrain) \| *pending*"*. **The document nowhere states that week 1's milestone is unmet, or what week it is in.** **(b) The specification gap widened.** The written acceptance suites in §4.7–§4.11 now total **69 test IDs** (T-HEX 7, T-DATA 6, T-MOVE 6, T-FAME 9, T-TURN 9, T-AI 6, T-SCN 10, T-UI 4, T-INT 5, T-SAVE 7), up from the ~63 the last audit counted, plus §2.8's eight T-CAP — 77 specified, unbuilt gates against four built rows in one file. **(c) Proportionality.** T-SCN-11, a single invariant of the scenario validator, occupies lines 1925–2154 — **230 lines**. §2.1–§2.6, the entire core rules the game is made of, occupy lines 95–180: **86 lines**. The document spends 2.7× as much page on one invariant of a system §4.11 itself calls off the path (*"Row 7 is still not ON the critical path"*) as on the hex grid, movement, combat, terrain and the core loop combined. **(d) Week 5 was never unloaded.** It still reads *"UI polish, feedback/juice, **the save-slot UI and its slot I/O** … onboarding"* — where "onboarding" is §2.11.6's four-beat strip with a two-rule line-assignment algorithm, three branch schedules, nine one-shot strings, two banners, a briefing overlay and a twelve-row ledger. Week 6 is *"Playtest, bug fix, balance lock"* and absorbed nothing. **(e) §2.10's scope table was never updated.** Its IN row still reads *"heuristic AI; **one hand-built scenario**; win-by-flag; functional UI"* — it names no scenario validator, no save/replay format, no guided opening. The one table a grader checks scope against understates §4's commitments by four systems. |
| **Document Quality** | **0.7** | 1.0 | Up 0.1. **All four live contradictions the last audit named are verifiably cleared:** §1 now reads *"four units, six terrains + the capturable Factory tile"*; both mocks read `4/8` / `3/8` with §2.11.4 stating *"**N = 8** on *Ferrum Crossing* (4 factories + 4 towns), as the mock shows"*; the turn cap is ruled once at Q7 and the widget *"reads `turnCap` from the scenario rather than hardcoding a number"*; and the two coordinate systems are reconciled explicitly — *"**Two conventions coexist deliberately, and the conversion between them is part of this contract**… `q = col − (row − (row & 1)) / 2`, `r = row` — and that conversion is itself gated (T-SCN-05)."* Cross-referencing is disciplined and every question carries exactly one ID. **Lost 0.3, and the defect is now length and proportion rather than contradiction.** §4.7 runs lines 1484–2303 — **820 lines, 32% of the document**; Stub 7 alone is 486 of them. T-SCN-11's asymmetry (ii) spends ~90 lines of capitalised prose on a Bridge-free counterfactual that the document itself says changes nothing: *"a Bridge-free reading does not FAIL Ferrum Crossing in EITHER seat, so no gate in this suite catches it."* Q8's register cell is a single four-column table cell of roughly 700 words; Q21, Q22 and Q30 are comparable. Q30 is an open question about the document's own **prose** conventions. There is no table of contents for 2578 lines. One residual staleness: §2.11.6-B beat 3's constraint reads *"Fame ≥ 100 guaranteed by 200 start + home income (§2.7)"* — Q8 ruled there is **no accrual on turn 1**, and §2.11.6 runs the first match at Easy, where the player opens on 350, not 200. The guarantee survives; its stated reason cites income that does not exist on turn 1 and a baseline that is not the tier in play. |

**Total: 7.9 / 10.0**

---

# Part 2 — Reconciliation against the 2026-07-30 report

| Old edit | Status | Evidence |
|---|---|---|
| **1. Restore the Q1–Q13 open-questions register to §4** | **Landed in full, and then some** | See below. |
| **2. Add §1.6 — Revision Notes: Stage 1 + 2** | **Landed in full** | §1.6 exists at lines 48–72 with exactly the five rows proposed, in §1.5's format, each citing its source: *"(rubric feedback, −0.5)"*, *"(review board open item)"* ×2, *"(§3 provenance ledger)"*, *"(continuity audit)"*. It also does more than was asked — it documents the authoring crew and the gate's four-violation first pass. |
| **3. Reconcile §4.4's milestones with §4.11's build order** | **Landed in part** | The contradiction half **landed in full** and was ruled, not papered: Q23 moves the vertical slice to week 3, §4.4 week 2 is now *"**Move + attack only** — no capture, no production, no AI opponent,"* and the note beneath states *"§2.10's *'these land wk 3, not wk 1–2'* now describes the schedule rather than contradicting it."* Q23 even names §1 as *"the fourth site"* and corrected it. The **week-5 unloading half did not land**: §4.4 week 5 still carries UI polish, juice, save-slot UI, slot I/O *and* onboarding. Q20 moved the §4.10 format and replayer to week 2, which relieved week 5 of one item; onboarding was not moved to week 6 as proposed. |
| **4. Rank §4.9/§4.10's parity infrastructure as cuttable, in the text** | **Not done** | §4.9 has no note at its head. §4.5's risk table is byte-unchanged at six rows and contains no *pipeline spec outruns the build* row. No text anywhere distinguishes ship-blocking from cuttable among the 69 written IDs. The material to do it now exists in §4.11 (*"Row 7 is still not ON the critical path"*; row 10(a) *"no deps at all; write it first"*) and is unused for this purpose. |
| **5. Clear the four live contradictions** | **Landed in full — all four** | Terrain count, both `Obj.` mocks, the turn cap, and the coordinate conventions. Quotes in the Document Quality row above. |

## Edit #1, verified in detail — what the register does and does not cover

It landed where the old report said to put it: a block headed **"Open questions
(Director rulings owed)"** immediately after Stub 8 and before §4.8, as a table
with the exact four columns proposed — ID / Question / Blocks / Assumption in
force. It grew from the 13 rows asked for to **31**, of which **15 are ruled and
16 open**; I re-derived both figures from the table itself and they match.

**What it now covers, beyond the ask:**

- Every Q-reference in the document resolves. The eight dead references the last
  audit found are gone.
- The `Blocks` column supplies the missing scope: each row names the gate, schema
  field or section that waits on it.
- It carries a stated **default posture** — *"where a reading is stated, it is the
  conservative one, and it is what ships and what the gates assert — chosen so
  that a later ruling loosens behavior rather than invalidating a passing gate"* —
  and it records the one case where that posture failed and why (*"**Q28 was the
  one row where that convention did not hold**… its conservative reading REFUSED A
  SHIPPED MAP"*).
- The collision the old report flagged is gone. §2.13.3 now reads *"capture at N=1
  (fixed from §2.7's 'start N=1–2' range — **Q4**, §4.7)"*; capture-N carries one
  ID.
- Several rows are decision records rather than open items — Q22 and Q28 are the
  audit trail of a gate that refused the shipped map and a map that was corrected
  rather than a rule weakened.

**What it does not cover, and should be said plainly:**

- **It is a rules-and-technical register only.** No row exists for art (§2.11.7),
  for the setting/faction fiction §2.11.4 already ships strings against, or for
  the title/lineage item. Those are the document's other unowned surfaces and the
  register's discipline is not applied to them.
- **Its own convention is applied unevenly.** §4.10 states *"Overwrite-confirm UX
  is **unowned**: §2.11 specifies no save/load surface"* and assigns it no ID,
  while the structurally identical §2.11.5 seam correctly became **Q31**.
- **The three rows blocking the current week's work are the three oldest open
  rows.** Q1 (map dimensions), Q2 (movement classes — leaves T-MOVE-07 unwritten
  and §4.8's `MoveClass` column *"reserved … **blocked on Q2**"*), and Q3
  (pass-through) are all inputs to §4.11 rows 1–3, i.e. week 1. They have been
  open since the register was created. The register is excellent at recording
  that; nothing in the document escalates it.
- **Length is now the register's own cost.** Q8, Q21, Q22 and Q30 are each
  roughly a page inside a single table cell.

## Findings from the old report that are now stale — do not repeat them

- *"Eight dead Q-references"* — gone.
- *"Neither register present / colliding IDs at §2.13.3"* — gone; one ID each.
- *"§4.4 and §4.11 describe two incompatible schedules"* — ruled at Q23, both
  sections now cite one principle.
- *"Every evidence link in the document 404s today"* — the document now claims
  otherwise: *"Commit `5ffa8d6` is published: it is an ancestor of `main` at
  [`2fcbf32`] on the public remote, so every link above resolves."* **I graded the
  claim on the page, not the URL.** Verify it before submission; it is the
  pipeline's entire credibility claim.
- *"Two faction names ship with no definition"* — **half stale.** They are defined,
  in `kb/setting.md` (§ "Faction A — The Directorate", § "Faction B — The
  Vanguard"). The remaining defect is one uncited reference, not missing
  world-building. `kb/setting.md` is never named anywhere in the GDD;
  `kb/rules.md` is named only inside two register cells.
- *"§1 still reads five terrains"*, *"Objectives 3/6"*, *"the turn cap holds three
  positions"*, *"odd-r and axial survive unreconciled"* — all four cleared.

## The load-bearing number: has the build gap narrowed?

**It held on the ledger and widened on the spec. That is worse than holding.**

- §3: **4 built / 8 `*pending*`**, identical to the last audit. All four built rows
  cite the same commit `5ffa8d6`, last dated 2026-07-29.
- Written-but-unbuilt acceptance IDs in §4.7–§4.11: **69**, up from ~63. The
  T-SCN suite alone grew from 4 written invariants to 10.
- Elapsed since the last ledger flip: three days, spanning **nineteen merge and
  remediation cycles** (post-merge-2 through post-merge-21).
- §4.4 week 1 is due rows 1–3. All three are `*pending*`.

The most recent gate cycle, `post-merge-21`, was spent in full on a paragraph
defining two senses of the word *blocked*. That is a defensible use of a gate
cycle in isolation. Nineteen of them against zero ledger movement is the ratio a
grader will compute, and the playable game is 50% of the final grade.

---

# The five edits that move the score most from here

**1. State the build's actual position, and give §4.5 the risk it is actually running. — moves Scope Realism +0.3**
*Where:* §3's ledger status line (currently *"the rest land as each system is
built (wk 1–3, §4.4)"*), and §4.5's risk table.
*The change:* two sentences and one table row. (a) In §3, after the existing
dates, state the date this draft stands at and which §4.4 rows are unstarted
against it — rows 1–3 are week 1's goal and all three are `*pending*` — and what
that does to weeks 2–3. (b) Add the risk row: *Specification outruns the build —
69 acceptance IDs written against 4 built ledger rows; mitigated by the named cut
line (edit 2) and by no §4.4 week starting before its predecessor's rows flip.*
A document that names its own slippage reads as scope control; a document that a
grader discovers has silently missed week 1 reads as the failure mode this rubric
line exists to catch. **This is the highest-value edit in the document** because
Scope Realism is the line furthest from its ceiling and the only one whose
remaining loss is still fixable by text rather than by shipping code.

**2. Name the cut line across the 69 written acceptance IDs. — moves Scope Realism +0.2**
*Where:* a three-line note at the head of §4.7, and an asterisk or column in
§4.11's build order table.
*The change:* say which suites are ship-blocking and which die if week 4 slips.
The document already has the answer and never states it: §4.11 says *"Row 7 is
still not ON the critical path"* and row 10(a) has *"no deps at all"*, while the
critical path is *"1 → 3 → 4 → 5 → 6/8"*. So: T-HEX, T-DATA, T-MOVE, T-FAME,
T-TURN, T-AI and T-UI-01/02 are ship-blocking; T-SCN-08/11's priced half,
T-INT-02/05, T-SAVE-06/07 and the in-editor Automation half of T-DATA-05 are
correctness infrastructure and are cut if the calendar bites. Sixty-nine
undifferentiated invariants read as ambition; a named cut line reads as a plan.

**3. Reconcile §2.10's scope table with what §4 now commits to build. — moves Scope Realism +0.1, Document Quality +0.1 (≈ +0.2)**
*Where:* §2.10's IN and STRETCH rows.
*The change:* the IN row still ends *"heuristic AI; one hand-built scenario;
win-by-flag; functional UI"* — written before §2.11.6, §2.13, §4.7 Stub 7, §4.9
and §4.10 existed. Add, explicitly: the scenario file + validator (§4.7 Stub 7);
the §4.10 save/replay format and headless replayer, marked *instrument, not
feature*, per Q20's own principle; and §2.11.6's four-beat guided opening. If any
of them is not in fact IN, say which and move it. Right now the table a grader
uses to check scope and the section that schedules the work disagree by four
systems, and the table is the one that reads smaller.

**4. Add §1.7 — Revision Notes: the ruling cycle. — moves Revision & Growth +0.15**
*Where:* new subsection after §1.6, same three-column finding → change → why
format, so §1.5, §1.6 and §1.7 read as one history.
*The change:* five rows, all lifted from material the register already contains,
none of it newly written. (i) *Q8 — the document said both sides had income from
turn 1; they do not* → no accrual on turn 1, rewriting four §2.7 bullets, §2.9's
economy phase, two gates and `kb/rules.md` → *"no map number moves"*, because the
reading chosen was the one §2.13.2 was already priced on. (ii) *Q23 + Q20 — two
sections described two schedules* → the slice moved later and the format moved
earlier, on one stated principle → the milestone table stopped drifting. (iii)
*Q28 — a new invariant refused the shipped map* → the map was corrected, one
deployment hex, and the failing case was kept as a fixture → *"a failing case that
was actually authored, that passes every other invariant in the suite."* (iv)
*Q6 — an unpriced bonus sat inside the tiebreak's primary sort key* → cut rather
than priced, reaching *"six sites that never cited it."* (v) *§4.6 — the token
budget applied its escalation twice* → re-derived from the per-task lines.
The evidence for this line already exists; the edit moves it from a technical
appendix into the section a grader reads as the revision record. Capped at +0.15
because the line is already at 1.8.

**5. Give §3's role table the two crews that actually ran. — moves Agent Role Clarity +0.1**
*Where:* two new rows in §3's role table, same four columns.
*The change:* **Documentation crew (4 authors)** — Owner: Agent ×4 · Responsibility:
draft assigned GDD sections in parallel against a frozen snapshot; write only
their own file, never the master · Instrument: Claude Code sub-agents over
`source/` · Verifiable output: section drafts under `sections/`. And **Continuity
gate** — Owner: Agent · Responsibility: audit every draft against the live GDD for
contradictions, stat drift, dead references and invented numbers; block merge ·
Instrument: Claude Code · Verifiable output: `gate/accept.json` per-section
verdicts and violation counts. §1.6 already describes both, including a failure
(*"the gate filed four violations… the two authors responsible were re-spawned"*).
This is the crew with the most evidence behind it and the only one with no I/O
contract in the table whose whole purpose is I/O contracts.

## Where not to spend an edit — diminishing and negative returns

- **Document Quality's remaining 0.3 is structural, not editable.** The defect is
  that §4.7 is 820 lines and T-SCN-11 is 230 of them. Trimming it is a multi-day
  rewrite of the most contradiction-dense section in the document, and the gate
  has blocked twice on edits to that exact preamble. A table of contents is worth
  perhaps +0.05 for ten minutes and is the only cheap piece; do that and stop.
  Do **not** open T-SCN-11 to shorten it before submission.
- **Game Specificity's remaining 0.2 mostly needs decisions the project does not
  have.** §2.11.7 needs an art plan, which is a Director call, not a prose edit.
  §4.5's rows will be fixed by edit 1 anyway. The one cheap fragment is the
  faction citation: one clause at §2.11.4 changing *"per the setting guide"* to
  name `kb/setting.md`, which already defines both factions — worth ~+0.05 and not
  worth ranking above the five.
- **Revision & Growth above ~1.9 is not reachable by writing more.** The line is
  near its ceiling; edit 4 relocates existing evidence and that is all that is
  left to do for it.

## Unowned gap — for the Director, not for the four authors

**Title and lineage are in better shape than the standing note assumes, and the
real gap is narrower than a narrative-designer's whole remit.** The title is
resolved on the page (§1 decision 5: *"**RESOLVED: the game is titled
*Stratocracy*.**"*), and lineage is framed twice — §1's *Conflict* paragraph with
the Famitsu criticism it fixes, and §2.12's full kept/diverged/cut extraction. As
a rubric matter that costs roughly **0.05, not a point**. What is genuinely
unowned is the *setting fiction*: §2.11.4 ships four faction-voiced result lines
and a *"generated content to follow these"* commitment against a *"setting guide"*
the GDD never names. Half of that is fixable by the Director in one clause today
(cite `kb/setting.md`). The other half — whether the shipped game states who the
Directorate and the Vanguard are anywhere the player can see — needs the
narrative-designer this kit does not have. Flagging, not assigning.

---

# What would lose points if a grader read closely

- **The build is behind its own week-1 milestone and the document does not say so.**
  §4.4 week 1 is rows 1–3 plus a test suite; §3 marks all three `*pending*`; the
  last verified commit is 2026-07-29 and this draft is 2026-08-01. This is the
  most expensive unflagged fact on the page and edit 1 exists to fix exactly it.
- **Nineteen merge cycles, zero ledger movement.** `post-merge-21`'s entire delta
  was a paragraph defining two senses of *blocked*. The gate reports it honestly.
  A grader weighing the playable game at 50% will read the ratio, not the prose.
- **Four built rows are one file at one commit.** §3 lists Combat resolution, Test
  suite, Repair and Type-effectiveness as four of twelve rows, all citing
  `Combat.cpp` / `test_combat.cpp` @ `5ffa8d6`. 4/12 reads as a third of the game
  and is one headless module with four gated behaviours. Saying so costs nothing
  and buys credibility.
- **The evidence links' resolution is asserted, not demonstrated.** §3 now claims
  `5ffa8d6` *"is an ancestor of `main` at `2fcbf32` on the public remote."* Click
  every link before submission. If one 404s, the ledger's *"auditable rather than
  asserted"* claim inverts.
- **The three questions blocking this week's work are the three oldest open rows.**
  Q1, Q2 and Q3 gate §4.11 rows 1–3 — week 1. Q2 leaves T-MOVE-07 unwritten and
  §4.8's `MoveClass` column *"blocked on Q2"*. The register makes this legible,
  which is to its credit and also means a grader can see it in one glance.
- **2578 lines with no table of contents.** §4.11, the build order, is the last
  thing in the file. Assume a grader reaches §2.13 and stops.
- **Six matches is still the stated content ceiling.** §2.13.4: *"by match ~4 a
  single mirrored map is a solved puzzle"* and *"If no stretch lands, the shipped
  scope alone moves the cliff from match ~3 to match ~6."* Honest and correct to
  state; still the number a grader weighs against 50%.
- **Art is two sentences headed *(unchanged)*** against §2.11.8's seventeen-item
  UMG must-have list, for a solo developer.
- **Q30 is an open question about the document's own prose conventions.** Its
  Blocks column reads *"**Nothing computable.**"* A grader who lands on it sees the
  project adjudicating its own writing style while eight systems are unbuilt.
- **§4.10's overwrite-confirm is declared unowned with no ID** while the identical
  §2.11.5 seam got Q31 — the register's discipline is not uniformly applied.

---

# Verdict

**7.9 / 10.0 — submittable, but not without edits 1 and 3.** The document did the
hard part of what the last audit asked. The Q1–Q31 register is not merely restored
but is now the best single artifact in the file: it converted eight dead
references into a defined, scoped, dated Director input set with a stated default
posture and an honest record of the one time that posture failed. §1.6 landed in
full and clears the Revision line almost outright. All four live contradictions
are gone, verifiably, and Q23 replaced the §4.4/§4.11 schedule collision with a
principle both sections now cite. Those gains are worth +0.7 between them.
They are offset by −0.1 on the one line that decides this project's grade: in the
same nineteen cycles, §3's ledger did not move a row, the written acceptance
suites grew from ~63 IDs to 69, one off-critical-path validator invariant grew to
2.7× the length of the entire core rules, week 1's milestone came due unmet, and
nothing in the document says so. The pipeline is now extraordinarily well
specified and the game is exactly as built as it was three days ago; that is the
20%/50% split running the wrong way, and no amount of further specification
reverses it. **Minimum edit set before submission: edit 1 (state the build's
position; add the risk row), edit 3 (reconcile §2.10 with §4), and verify the §3
commit links resolve.** Edits 2 and 5 are cheap and should follow if there is an
hour. Edit 4 is worth doing but is relocation, not new work. After that, **stop
writing and build rows 1–3** — every further remediation cycle spent on §4.7's
prose is a cycle the 50% line does not get back.

**Score movement: 7.3 → 7.9 (+0.6).** It moved up because the register and §1.6
landed and every named contradiction was cleared; it did not move further because
Scope Realism went backwards — the specification grew, the build did not, and the
calendar did.
