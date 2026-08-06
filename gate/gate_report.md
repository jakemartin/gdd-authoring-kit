# Gate report — run `harness-calendar-7`

`source/MANIFEST.txt` present. Its `gdd.md` line reads
`md5=8491e0133cfa04207b909d29785397e0`, matching the value supplied with the
task.

Gated in this run: `sections/tech_harness-calendar.md` only. Every other file
under `sections/` is a sealed addendum from an already-merged round and was not
read as draft material.

Derivation is independent of runs 1–6 and of the coordinator's reading. Probes
ran with widened context windows rather than fixed narrow ones, because a narrow
window under-reports on this file: `in-editor pass` at §4.11 line 3075 and the
§4.7 cut-line phrase wrapped across lines 1649–1650 both read as misses under an
80-character window. Both were confirmed present. Every zero-hit probe reported
below was re-run with a re-worded pattern before being trusted.

---

## `sections/tech_harness-calendar.md` — **PASS**, 0 violations

### Anchors and placement

All three OLD anchors were re-extracted from the master and probed full-file.

| Pair | Anchor probe | Occurrences | Master lines |
|---|---|---|---|
| 1 | `And because a gate that runs green over a subset is not a verified system` | 1 | 1573 (§4.4, Q23/Q20 paragraph) |
| 2 | `vendored StratRules sources + recorded source commit` | 1 | 2901 (§4.9 stub `Inputs:`) |
| 3 | `extra `Sneaky.good.cpp` in that directory FAILs` | 1 | 2897 (§4.9) |

The draft's stated reason for the Pair 2 anchor carrying its `Inputs:` prefix
also verifies: `§4.8 tables imported in-editor` occurs twice, at 2890 and 2902,
so the bare phrase would not have been a unique anchor.

Pairs 1 and 3 are insertions whose NEW begins with the OLD verbatim; Pair 2 is a
replacement of two lines. The three targets are in three distinct places
(§4.4 body, §4.9 body, §4.9 fenced stub). No placement collision, and no
placement is vague — each is byte-anchored.

### Claim-by-claim re-derivation

Pair 1 (§4.4). Every disposition it states was checked against the master's own
cells and against §4.9:

- "wk 3 names it among what `T-SAVE-06` and `T-INT-02` wait on" — §4.4 line
  1567: "`T-SAVE-06` did not close here: among what it waits on are the
  in-editor Automation harness and a vendored replayer … `T-INT-02` did not
  close here either: among what it waits on are that harness and that
  replayer". Confirmed a blocker note, not a goal.
- "No cell above gives it a week" — probed `in-editor (Automation )?(pass|
  harness)` across the whole file; inside the table (1565–1571) the only hit is
  the wk-3 blocker note above. Holds.
- "§4.9 records it among what part 2 is blocked on and states that it is not
  scheduled there either" — §4.9 line 2870: "The harness is recorded here among
  what part 2 is blocked on, and is not scheduled here."
- "the harness by itself closes no acceptance ID (§4.9)" — §4.9 2892–2893:
  "Registering the UBT module closes no acceptance ID, and neither does the
  harness by itself."
- Widget work / command wiring scheduled — §4.4 1565 ("**UI-scaffolder agent
  starts UMG widget skeletons in parallel**"), 1566 ("Engine presentation + UI
  wiring (select/move/attack) onto the wk-1 skeletons", "**Week 2's command set
  is exactly `{Move, Attack}`**", "`Capture`, `Build` and `EndTurn` arrive with
  §4.11 rows 4–5 in wk 3").
- "An in-editor import step for the §4.8 tables has no cell; wk 1 names those
  tables inside the headless core" — §4.4 1565, "Headless C++ core — §4.11
  **rows 1–3** (grid and hex math, the §4.8 tables, movement and pathfinding)".
- "A `UENUM` mirror of the unit type is named in no cell" — `UENUM` occurs at
  exactly three places in the master: 2688, 2882, 2886. None is in §4.4.
- Vendored replayer held out by ruling — §4.9 2878–2879, and the wk-2 cell's
  "**and the §4.10 save/replay format + headless replayer** (Q20, ruled)" is a
  different artifact, as the draft states.
- "None of those subjects exists at `a13626f` (§4.9)" — §4.9 2883–2889. The
  referent is fixed by the paragraph's own topic sentence ("the subjects the
  editor-pass IDs assert against besides it"), which is §4.9's own list; the
  draft does not identify the wk-1 skeletons with the assets measured absent
  there, and the check note's disclaimer is consistent with the prose.

Pair 2 (§4.9 stub). Its assignment reasoning was checked against the invariant
texts it cites: `T-INT-02` at 2914–2918 ("replay parity … the same final
canonical state hash", tripwire "a compiler that rounds differently"),
`T-INT-01` at 2904–2913 (both mechanisms, so the gloss "by whichever mechanism
T-INT-01 puts on a given file" holds), `T-INT-04` at 2921–2925, the `FUnitRow`
→ `strat::UnitDef` mapping at 2835–2836, `Atk`/`Def` at 2679–2680, §4.1's damage
sentence at 1545. The deferral to per-ID subjects is sound because §4.9's list
is introduced by "among what the remaining editor-pass IDs need besides it are"
(2875–2877) — non-exhaustive, so a new requirement is additive rather than
contradictory, and `T-DATA-05` is indeed not an invariant this stub carries.

Pair 3 (§4.9). Each of the three naming forms it cites was probed and found:
"the editor pass" (13 occurrences, including §4.9 2871 and 2938), "an in-editor
Automation pass" (§4.5 1585, §4.7 1650, §4.11 3080), "an in-editor pass" (§3
1531, §4.11 3075). Both printed-output records verify in §3 line 1514: at
`b23823f`, "`T-INT-02`, `T-INT-03` and `T-INT-05` **did not run** — no in-editor
Automation harness exists, and the runner prints that sentence by name before
its tally"; at `41a1452`, "the two `NOT RUN` lines are output lines **76** and
**82** … each names its ID, states that it is in-editor Unreal Automation marked
†, and states that no in-editor pass exists at this commit." "No name is changed
in this revision" is true of all three pairs.

### The cut

The four questions the cut raises were each run:

- **Did the cut strand a claim?** Every substantive claim in the three pairs
  resolves to either an inline section citation or a line-pinned Grounding
  entry. The one claim carrying only a section-level citation — "§4.9 records it
  among what part 2 is blocked on and states that it is not scheduled there
  either" — is true at 2870–2871 and names its section in the prose, so it is
  locatable. Not filed.
- **Is what remains accurate?** Anchor uniqueness verified independently (table
  above). Ruling AD's per-subject dispositions verified above, quotation by
  quotation, including the two the check results scope carefully: the wk-3
  "command surface" phrase is a blocker note rather than a name for the wk-2
  wiring, and wk 4's "T-SAVE-07 (harness compatibility)" is the Balance
  self-play harness (§4.10 stub line 3051: "a Balance Analyst self-play log
  validates and replays as a save file"), a different subject. Ruling AE's
  per-ID grounding verified above.
- **Grounding citations after the material moved.** All fifteen line ranges were
  opened: 1573, 1565–1568, 2892–2893, 2878–2879, 2771–2783, 2883–2889,
  2901–2902, 2914–2918, 2835–2837, 2674–2686 (`Atk` 2679, `Def` 2680), 1545,
  2904–2913, 2921–2925, 2877–2883, 2896–2897, 2871–2875, 2688 / 2882 / 2886,
  3101–3102. Each resolves to the text it claims.
- **New quantified claim?** None. The draft states no count, no ID tally, no
  arithmetic; §4.5's figures, the acceptance register and the §3 ledger are
  untouched by all three pairs.

### Adjacent statements checked for contradiction, and cleared

- §4.11 3164–3165, "an editor pass cut to its marked IDs alone would still owe
  T-INT-03, so this line thins that pass, it never cancels it." Pair 1 says the
  harness is not *on the calendar*, and states the condition under which it
  takes a cell ("the week the thing that consumes it runs"). Deferral is not
  cancellation. No contradiction.
- §4.10 stub 3055, "slot I/O smoke test in the editor pass", beside §4.4 wk 5's
  slot I/O. The wk-5 cell names neither the pass nor the harness, so it gives
  the harness no week; Pair 1's dispositions are explicitly non-exhaustive.
- §4.8 2663 ("the Unreal editor imports the same file into a `UDataTable`") vs
  Pair 1's "An in-editor import step for the §4.8 tables has no cell". The first
  is a design statement, the second a calendar statement. No conflict.
- kb desync: all three pairs land in §4.4 and §4.9. `source/kb_rules.md` is a
  parse of §2 (Units §2.4, Terrain §2.3, Economy §2.7, Victory §2.8) and
  `kb_setting.md` likewise carries no §4 material. Nothing in this round makes
  either wrong.
- Voice: the inserted prose is declarative and present-tense, matching the
  register of the surrounding §4.4 and §4.9 text. No UI strings are added.
- Format: the file carries the house addendum structure — pairs with byte-exact
  OLD/NEW and a per-pair note, Check results, Change requests, Grounding — the
  same structure the sealed rounds in `sections/` use. The pair blocks state
  placement more precisely than a `Placement` heading would, and no open
  question is raised that CR-1 and Pair 3's stated deferral do not carry.

### Not filed — one note for the Director at merge

CR-1 proposes replacing "since the editor pass is not yet due" in the §4.11
row-2 note (3101–3102). The same clause occurs a second time in §3 at line 1514:
"the editor pass is not yet due, so that is the ordinary schedule and not §4.7's
cut line firing." The draft makes no claim about how many sites carry the
phrase, so nothing in it is false, and a change request is the Director's to
scope — but if CR-1 is accepted at §4.11 only, the §3 site will read against it.
This is recorded, not filed as a violation.

---

## Verdict

**PASS**, one section, zero violations. The three pairs re-derive clean against
`source/gdd.md` at md5 `8491e0133cfa04207b909d29785397e0` — anchors unique,
insertions byte-prefixed by their OLD, no placement collision — and the cut from
510 lines to 171 removed apparatus only: every claim the pairs make is still
carried by a Grounding line or an inline section citation, the rewritten Check
results are accurate against the master at each of the passages they quote, all
eighteen Grounding line ranges resolve, and no new quantified claim entered.
Nothing must happen before merge on this gate's account. The Director should
apply the three pairs at their stated anchors, and, when ruling on CR-1, decide
the §3 line-1514 occurrence of the same clause in the same move rather than
leaving the two sites to diverge.
