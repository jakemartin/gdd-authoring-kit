# Rubric audit — 2026-07-30 (rubric-auditor)

**Document scored:** `source/gdd.md`, md5 `7367b1961aae90b544f3837a9c7e6cd1` (per
`source/MANIFEST.txt`), 1569 lines.
**Sync check:** `gate/accept.json` records the pre-merge master at
`4cdcff7ad4abbb3c93ad0036ead04faf`. The manifest md5 differs, so the Stage 1 + 2
merge **was** synced. Scoring proceeds.
**Gate context:** `gate/gate_report.md` run `stage-2` returned PASS, 4 sections,
0 violations. Its three declared merge-time alignment notes were **not** applied
during the merge; all three survive in the master and are scored below.

---

## Scores

| Line | Score | Max | Evidence (section + quote) |
|---|---|---|---|
| **Game Specificity** | **2.7** | 3.0 | Earned almost everywhere. §2.13.2 prices the map hex by hex: *"The river deliberately does **not** bisect the map: the southern pass (row 6) is a bridge-free route priced by two Mountains (cost 3, +40%), so it is the *slow* flank, never a free one."* §2.11.3's forecast card carries a worked instance — *"round(10 × 1.0 × 0.8) − 5 = 3; counter 0 because the attacker sits outside the Tank's range 1"*. §4.8 names real columns and real values (*"`DefensePct` … §2.3 (0, 20, 40, 0, 10, **−10**, 15)"*). Lost 0.3 on three generic patches: §2.11.7 Art is the whole visual deliverable in two sentences (*"Flat/low-poly color-coded hexes, simple unit meshes or billboarded icons, generative/agent-assisted"*) and would fit any art-light hex game; §4.5's risk rows are one-line generics (*"AI rabbit hole \| Ship the heuristic; LLM behind a toggle"*); and the shipped UI strings name factions the document never defines — §2.11.4 ships *"Directorate, decisive: `Command directive fulfilled…`"* citing only *"per the setting guide"*, an unnamed, uncited external file. |
| **Revision & Growth** | **1.5** | 2.0 | §1.5 is a strong six-row finding → change → why table and alone clears the bar: *"**Turtle exploit in the tiebreak.** Original cap tiebreak ('most factories held, then total HP') *rewarded* stalling"* → *"Reordered the cap tiebreak around **combat Fame earned**… added a **mutual-passivity → draw** guard"*. Lost 0.5 because it is stale by one full revision cycle. Its heading is *"§1.5 Revision Notes — First Draft → Final Draft"* and its last row predates Stage 1. This merge added §2.0, rebuilt §2.11 into eight subsections, added §2.13, and added §4.7–§4.11 — roughly 800 lines, the largest revision in the document's history — and **not one of them appears in the revision log**. §2.0 exists because a rubric line lost 0.5; the document never says so. Growth that isn't narrated isn't graded. |
| **Agent Role Clarity** | **1.6** | 2.0 | §3's table gives seven roles four columns each — Owner / Responsibility / Instrument / Verifiable output — e.g. *"**Test Engineer** \| Agent \| Write + run the automation/unit-test suite; block merges on failures \| Claude Code + test harness \| Passing test suite (the merge gate)"*. The worked spec block (*"SPEC: Combat resolution (Director → Systems Engineer)"* with Inputs / Formula / Invariants / Acceptance) and the real failure case (*"T-COMBAT-07 … First agent pass → FAIL: the Systems Engineer generalized 'surviving units counterattack'"*) are exactly what this line asks for. Lost 0.4 on **the Director's inputs, which do not exist**: §4.7 says *"the gate is parameterized on a numbered open question (Q1–Q10, Open questions below) — the Director rules, the gate then pins the ruling"*, and there is no "Open questions" list anywhere below. Q1, Q2, Q3, Q4, Q7, Q8, Q9 and Q12 are cited eight times across §4.7–§4.11 and defined zero times. The role that gates the entire build order has an undefined input set. Also uncredited: §1.5's *"agent review crew (an Exploit-Hunter / Consistency / Pacing board)"* appears nowhere in the §3 role table, and the four-author + continuity-gate crew that wrote §2.0, §2.11, §2.13 and §4.7–§4.11 is not described at all. |
| **Scope Realism** | **0.9** | 1.5 | Credit where earned: §2.10 keeps a hard CUT column, and §2.13.7 disciplines the stretch maps — *"Neither stretch map may pull work forward of week 4 or block core; if week 4 is consumed by balance (its primary §4.4 purpose), the set stays on paper."* Lost 0.6 on three counts. **(a) §4.4 and §4.11 contradict each other.** §2.10 says capture + Fame production *"land wk 3, not wk 1–2"*, and §4.4 wk 2 promises *"presentation + UI wiring … baseline objective-seeker AI → **working vertical slice**"* — but §4.11's critical path is *"1 → 3 → 4 → 5 → 6/8"*, making row 4 Capture & Fame a hard prerequisite of row 5 Turn loop, which the wk-2 slice and the wk-2 AI both need. The merge fused two incompatible schedules. **(b) Week 5 is overloaded.** §4.4 wk 5 is *"UI polish, feedback/juice, save/load, onboarding"* — where "save/load" is §4.10's seven-invariant replay format and "onboarding" is §2.11.6's eleven one-shot strings, four-beat scripted opening, briefing overlay and twelve-row concept ledger. §4.11 already concedes save/load is *"one week too late"*, which relieves week 5 only by pushing into the already-contradictory week 2. **(c) Spec volume outran the build.** This stage added ~63 new acceptance-test IDs (T-HEX 7, T-DATA 6, T-MOVE 6, T-FAME 9, T-TURN 9, T-AI 6, T-SCN 4, T-UI 4, T-INT 5, T-SAVE 7) while §3's ledger stayed at *"Hex grid & math \| *pending* … UI \| *pending*"* — eight of twelve rows unbuilt, nothing new shipped. The playable game is 50% of the grade and the pipeline 20%; this stage bought pipeline. |
| **Document Quality** | **0.6** | 1.0 | Structure and cross-referencing are genuinely good — repeated spec-block shape, consistent tables, §2.13.7's summary table, §4.11's dependency table. Lost 0.4 to one structural defect and four live contradictions. **Structural:** §4.7's *"Open questions below"* points at nothing — eight dead Q-references (above). **Contradictions:** §1 still reads *"One polished scenario, four units, **five terrains**"* against §2.3's *"prototype set: 6 movement terrains + the capturable Factory tile"* and §2.10's *"**6 terrains + the Factory tile**"*; §2.11.2 and §2.11.4 both mock *"Objectives 3/6"* while §2.13.2 ships 4 factories + 4 towns, i.e. N = 8; the turn cap holds three positions at once — §2.8 *"20 turns — see change request pinning the value"*, §2.11.4 *"the cap must be fixed before this ships — open change request"*, §2.13.2 *"**20 turns** (fixes §2.8's 'e.g. 20' for this scenario)"*; and capture-N is labelled *"Open question 2"* at §2.13.3 but *"N per Q4"* at §4.7 T-FAME-05, while §4.7's own Q2 is the movement-class question — two authors' registers merged with colliding numbers and neither register present. §2.13.1's odd-r *"(col, row)"* and §4.7's axial *"(q, r)"* also survive unreconciled. |

**Total: 7.3 / 10.0**

---

## The five edits that move the score most

**1. Restore the Q1–Q13 open-questions register to §4. — moves Agent Role Clarity +0.3, Document Quality +0.25, Scope Realism +0.1 (≈ +0.65)**
*Where:* insert a new block after §4.7's Spec Stub 8 and before §4.8, headed
**Open questions (Director rulings owed)**.
*The change:* §4.7 line 1077 promises *"(Q1–Q10, Open questions below)"* and the
list did not survive the merge from `sections/tech.md`. Restore it as a table —
ID, the question, the section blocked, the conservative assumption in force
until ruled. It must at minimum define the eight IDs the merged text already
cites: Q1 (map dimensions / bounds), Q2 (Recon's movement class), Q3
(friendly pass-through), Q4 (capture N and interruption semantics), Q7 (turn
cap value), Q8 (income accrual timing and waiting-build semantics), Q9 (AI tie
order), Q12 (RNG / seed). Renumber §2.13.3's *"Open question 2"* into the same
register so capture-N carries one ID, not two. This is the cheapest large gain
in the document: it converts eight dead references into a defined Director
input set, and it is a copy-forward from a draft that already passed the gate.

**2. Add §1.6 — Revision Notes: Stage 1 + 2. — moves Revision & Growth +0.4**
*Where:* new subsection immediately after §1.5, same three-column
finding → change → why-it's-better format, so the two read as one history.
*The change:* five rows, each naming its prior feedback source explicitly.
(i) *rubric feedback: no stated player-experience goals, −0.5* → §2.0 PX-1..6,
each with an observable check → goals are now testable, not preferences.
(ii) *review board open item: how a first-timer learns hexes, Fame, capture and
the RPS triangle with no manual* → §2.11.6's three teachers, the turn-1–3
guided opening, the twelve-row concept ledger. (iii) *replay cliff at ~3
matches* → §2.13.4's configuration = map × seat × difficulty, moving the cliff
to match ~6 on shipped scope alone. (iv) *eight `*pending*` ledger rows had no
route to a test gate* → §4.7's eight stubs + §4.11's build order, each row
carrying acceptance IDs the way Combat did. (v) *§2 had accumulated drift after
the Conflict fold* → §2.1–§2.10 consolidated. Without this the grader sees a
revision log that stops before the document's largest revision.

**3. Reconcile §4.4's milestones with §4.11's build order. — moves Scope Realism +0.3**
*Where:* §4.4 milestone table, weeks 2, 3 and 5; and §2.10's parenthetical
*"(these land wk 3, not wk 1–2)"*.
*The change:* §4.11 makes Capture & Fame (row 4) a hard prerequisite of Turn
loop & win (row 5), and the wk-2 *"working vertical slice"* plus the wk-2
baseline AI both sit downstream of row 5 — so §2.10's "capture + production land
wk 3" cannot be true. Pick one: either pull Capture & Fame into week 2 and
delete the §2.10 parenthetical, or move the vertical-slice milestone to week 3
and say week 2 delivers move + attack only. Then unload week 5: it currently
carries UI polish, juice, save/load **and** the whole §2.11.6 onboarding
apparatus. Move onboarding to week 6 in place of the LLM-commander stretch, and
adopt §4.11's own split — *"format + replayer early, save-slot UI stays week
5"* — as a milestone edit rather than an open change request.

**4. Rank §4.9/§4.10's parity infrastructure as cuttable, in the text. — moves Scope Realism +0.2**
*Where:* a two-line note at the head of §4.9 and in §4.5's risk table.
*The change:* T-INT-02 (*"the same command log replayed headless and in-engine …
must land on the same canonical state hash"*), T-SAVE-06 and the §4.8
T-DATA-05 import-parity gate are correctness infrastructure for a
cross-compiler divergence risk, specified in the same stage that shipped zero
game systems against eight `*pending*` ledger rows. Say plainly which of the 63
new test IDs are ship-blocking and which are cut if week 4 slips. A named cut
line reads as scope control; 63 undifferentiated invariants read as ambition.
Add a matching §4.5 risk row: *pipeline spec outruns the build*.

**5. Clear the four live contradictions. — moves Document Quality +0.15, Game Specificity +0.1 (≈ +0.25)**
*Where and what, exactly:*
- §1 "Scope at a glance": *"four units, five terrains"* → *"four units, six
  terrains + the capturable Factory tile"*. The change request was filed at the
  gate and not applied; §2.3 and §2.10 already say six.
- §2.11.2 HUD mock and §2.11.4 scoreboard mock: `Obj. 3/6` / `Objectives 3/6`
  → `4/8` and `3/8`, matching *Ferrum Crossing*'s 4 factories + 4 towns
  (§2.13.2). Recompute the chevron line if the leader changes.
- Turn cap: adopt §2.13.2's ruling (20, per-scenario, stored in the Stub-7
  `turnCap` field) and strike the two stale hedges at §2.8 and §2.11.4.
- Coordinates: keep §2.13.1's odd-r for authored maps and §4.7's axial for the
  module, and add one sentence at §4.7's Shared conventions saying so — the
  conversion is the contract, and right now neither section knows the other
  exists.

---

## What would lose points if a grader read closely

- **The ledger's four "built" rows are one file and one commit.** §3 lists
  Combat resolution, Test suite, Repair and Type-effectiveness as four of
  twelve rows, and all four cite `Combat.cpp` / `test_combat.cpp` @ `5ffa8d6`.
  The row count implies breadth the evidence does not have. Say "one headless
  combat module, four gated behaviours" rather than let 4/12 read as a third of
  the game.
- **The audit trail is unreachable.** §3 claims the ledger is *"auditable rather
  than asserted"* and links four GitHub commit URLs — then concedes *"Commit
  `5ffa8d6` is present locally; a `git push` publishes the linked commit for
  external audit."* Every evidence link in the document 404s today. This is the
  most expensive unflagged risk on the page: the pipeline's entire credibility
  claim rests on links a grader will click. Push before submission or the
  claim is worth nothing.
- **The shipped game is about six matches of content, by the document's own
  admission.** §2.13.4: *"by match ~4 a single mirrored map is a solved
  puzzle"* and *"If no stretch lands, the shipped scope alone moves the cliff
  from match ~3 to match ~6."* Honest, and correct to state — but a grader
  weighing the playable game at 50% will read six matches as the ceiling.
  Consider naming what a seventh match offers.
- **Art is unspecified for a product graded on being playable.** §2.11.7 is two
  sentences and the word *"(unchanged)"* in its own heading. §2.11.8's
  must-have list is seventeen UMG items for a solo dev with no art plan behind
  them.
- **Who builds the maps is undefined.** §3 gives Content / Scenario Designer the
  output *"Scenario assets, data tables"* via a *"Custom **MCP toolset**
  in-editor"*, but the MCP toolset is week-3 work and §4.2 calls the plugin
  *"experimental, partly undocumented … not on the critical path"*, while
  §2.13's three maps are hand-authored in the GDD. Nothing states whether the
  agent builds *Ferrum Crossing* or the human does.
- **Two faction names ship in player-facing strings with no definition.**
  Directorate and Vanguard appear only in §2.11.4's result lines, sourced to an
  unnamed *"setting guide"*. Either cite the file by name or define both
  factions in one paragraph — right now the GDD ships dialogue for a world it
  never establishes. This is adjacent to the unowned title/lineage item and
  would be the narrative-designer's first task.
- **The document never states what week the project is in.** §4.6 pins the jam
  to *"Jul–late Aug 2026"* and §3's ledger dates rows to 2026-07-26 and
  07-29, so a careful reader can infer week 1 — but a seven-week plan with
  eight unbuilt systems should say where it stands on its own timeline, in
  §4.4, in one line.

---

## Verdict

**7.3 / 10.0 — do not submit as-is.** The document is strong where it is
strongest: §2.13 and §2.11 are unmistakably about *this* game, §3's role table
and its T-COMBAT-07 failure case are a genuinely well-evidenced pipeline
account, and §2.8's delete-test is the best-argued page in the file. What holds
it back is not writing quality but three specific gaps, and two of them are
cheap. The merge dropped the Q1–Q13 register that §4.7 explicitly promises,
leaving eight dead references and an undefined input set for the one role that
gates the whole build order — restoring it is a copy-forward from an
already-passed draft and is worth roughly 0.65 on its own. The revision log
stops before the largest revision the document has ever had; a §1.6 in §1.5's
existing format is worth another 0.4. Together those two edits, neither of which
requires a design decision, take the document to about 8.4. The third gap is
harder and should not be papered over: §4.4 and §4.11 now describe two
incompatible schedules, week 5 carries four major workstreams, and this stage
added ~63 acceptance-test IDs while the ledger stayed at four built rows in one
file whose evidence links do not resolve. Scope realism is the line where this
document is genuinely exposed, and the fix is a scheduling decision plus a named
cut line, not more specification. **Minimum edit set before submission: edits 1,
2 and 5, plus `git push` so the §3 evidence links resolve.** Edits 3 and 4
should follow before the next milestone review, because the §4.4/§4.11
contradiction will surface as a missed week-2 gate whether or not the document
admits it now.
