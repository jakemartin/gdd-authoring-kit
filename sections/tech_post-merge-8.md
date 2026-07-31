> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**, and
> the master has moved on since. Its Old blocks no longer match, so re-applying is
> a no-op at best; its quoted "current" text, register extents, and any hash it
> names are a **snapshot of the moment it was written**, not the current state.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — post-merge-8 draft (tech-director)

## Placement

Three sites, all in §4:

- **§4.4 Milestones** — weeks 1, 2, 3 and the note under the table (pairs 1–4).
- **§4.11 Build order** — the preamble note and rows 9–10's *Depends on* cells
  (pairs 5–7).
- **§4.7 Open-questions register** — Q20's assumption cell (pair 8), Q21's
  *Blocks* and assumption cells (pairs 9–10), the register preamble and one new
  row **Q29** (pairs 11–12).

No renumbering. No map, lane, terrain or MP figure is touched. T-SCN-10 stays
reserved and unwritten (Q26). No `T-` ID is added, removed or renumbered; the
register goes Q1–Q29 with ten ruled and Q29 open.

---

## Draft

### The ruling behind pairs 1–7 — stated before the edits, because it is the edit

**The technical question the gate asked: can replay parity run over a
Move/Attack-only command set?** It can, and the reason is specific rather than
optimistic.

T-INT-02 replays a **fixed** log. Nothing in the run chooses a command, so the
AI's evaluation, the tiebreak's comparisons and every other decision surface are
outside its scope; what it exercises is the state-mutating math and the hash over
the result. §4.10 already establishes that **every field of the canonical state
hash is an integer**, with `eff` and the HP ratio existing "only transiently
inside `resolveDamage`." So the entire divergence class T-INT-02 was written to
catch — a compiler or CRT rounding `resolveDamage` differently — is reached by
the `Attack` command alone. A `{Move, Attack}` log is not a thin log for this
gate; it is the log that carries the risk.

What a week-2 pass does **not** cover is the second tripwire in the same stub:
an agent that *ports* rather than vendors the module. That one is a property of
the code that exists, and rows 4–5 add code. So the week-2 pass is a real run
over the module as it then stands, and it must be re-run when the module grows.

That gives the rule the seam was missing, and it is a scoping rule rather than a
schedule move:

> **An integration or replay gate is scoped to the command set of the log it
> runs on.** It *runs* as soon as that log can be produced; it *closes* only
> when the log carries every §4.9 command.

Under it, both halves of the contradiction become true at once. §4.4 keeps its
week-2 instrument and a gate that genuinely runs there; §4.11 row 9 keeps its
rows-1–5 requirement — as the requirement to **close**, which is what it always
was. Row 10 splits three ways rather than two: a format spec with no
dependencies at all, a replayer that needs rows 1–3, and a closure that needs
rows 4–6.

Concretely, over the four weeks:

| Week | Log's command set | Gates that **run** | Gates that **close** |
|---|---|---|---|
| 2 | `{Move, Attack}` | T-INT-01..05, T-SAVE-01..06 | T-INT-01, T-INT-04, T-SAVE-04 |
| 3 | `+ Capture, Build, EndTurn` (rows 4–5) | all of the above | T-INT-02/03/05, T-SAVE-01/03/05/06 |
| 3 | (row 6 lands) | T-SAVE-02 | T-SAVE-02 (it composes T-AI-06) |
| 4 | self-play logs | T-SAVE-07 | T-SAVE-07 |

That table is **not proposed as document text** — §4.4's milestone table and the
note under it remain the single statement of the schedule, per Q20's own
convention, and pairs 1–4 put these facts there. It is here so the Director can
check the pairs against one view.

**One thing I did not do:** week 2 has no `EndTurn`, because `EndTurn` belongs
to §4.11 row 5 and row 5 is week 3 under Q23. That follows from the document as
it stands rather than needing a ruling, so I have not filed one — but it has a
visible consequence I have stated in the week-2 cell's neighbourhood: a week-2
log's entries are all `{turn: 1, side: <the one seat>}`, so T-SAVE-01 and
T-SAVE-03 run within a single turn only. See **Open questions** if the Director
wants week-2 debug play to advance turns.

---

### Pair 1 — §4.4, week 2

The cell keeps its Q20 content and gains the command set and the run/close
distinction. The sentence the gate objected to — *"the week-2 integration gate
cannot run without it"* — stays, because it is true; what was missing was the
scope of the run.

**OLD**

```
| 2 | Engine presentation + UI wiring (select/move/attack) onto the wk-1 skeletons, plus the one scenario loading, validating and rendering, **and the §4.10 save/replay format + headless replayer** (Q20, ruled). The format is a *test instrument*, not a feature: T-INT-02's input file is a save, so the week-2 integration gate cannot run without it — and neither can the week-4 self-play logs (T-SAVE-07). No save button, slot, or `USaveGame` wrapper here; those are week 5. **Move + attack only** — no capture, no production, no AI opponent. |
```

**NEW**

```
| 2 | Engine presentation + UI wiring (select/move/attack) onto the wk-1 skeletons, plus the one scenario loading, validating and rendering, **and the §4.10 save/replay format + headless replayer** (Q20, ruled). The format is a *test instrument*, not a feature: T-INT-02's input file is a save, so the week-2 parity gate cannot run without it — and neither can the week-4 self-play logs (T-SAVE-07). **Week 2's command set is exactly `{Move, Attack}`** (§4.9): `Capture`, `Build` and `EndTurn` arrive with §4.11 rows 4–5 in wk 3, so a wk-2 log's entries are all `{turn 1, one side}`. The wk-2 parity and replay gates therefore **run over that subset and re-open when it widens** — T-INT-01/04 and T-SAVE-04 close here, the rest do not (§4.11 rows 9–10). That is a real gate rather than a placeholder: T-INT-02 replays a *fixed* log, so its divergence surface is the state-mutating math only, and every field of the §4.10 hash is an integer except the transients inside `resolveDamage` — which `Attack` already reaches. What it cannot cover is code that does not exist yet, which is exactly why rows 4–5 re-open it. No save button, slot, or `USaveGame` wrapper here; those are week 5. **Move + attack only** — no capture, no production, no AI opponent. |
```

### Pair 2 — §4.4, week 3

Week 3 is where the re-run closes. Naming the IDs here keeps the weeks in one
place and lets §4.11 speak only about dependencies.

**OLD**

```
| 3 | Capture + production (§4.11 rows 4–5), then the baseline objective-seeker AI (row 6) → **working vertical slice.** AI second pass (utility + threat map) and the custom MCP scenario toolset follow only if the slice lands early; both are off the critical path (§4.2, §4.11). |
```

**NEW**

```
| 3 | Capture + production (§4.11 rows 4–5), then the baseline objective-seeker AI (row 6) → **working vertical slice.** Rows 4–5 add precisely the three commands week 2 lacked, so the wk-2 gates re-run over the complete set and **close here**: T-INT-02/03/05 and T-SAVE-01/03/05/06 on rows 4–5, and T-SAVE-02 on row 6, whose determinism gate (T-AI-06) it composes. Only T-SAVE-07 still waits — for wk 4's self-play logs. AI second pass (utility + threat map) and the custom MCP scenario toolset follow only if the slice lands early; both are off the critical path (§4.2, §4.11). |
```

### Pair 3 — §4.4, the note under the table

Anchored on the note's closing sentence; the new text follows it. This is where
the seam is actually repaired, so the failure is described rather than quietly
corrected.

**OLD**

```
Stated once, so the table stops drifting: **a format is a test instrument; slot I/O is a feature.**
```

**NEW**

```
Stated once, so the table stops drifting: **a format is a test instrument; slot I/O is a feature.** One consequence of that principle needed stating too, because the first application of it promised a week-2 gate this document's own build order could not support: **an integration or replay gate is scoped to the command set of the log it runs on.** It *runs* as soon as that log can be produced and it *closes* only when the log carries every §4.9 command — so week 2's `{Move, Attack}` pass is a run, not a closure, and §4.11 rows 9–10 now state those two dependency sets separately instead of one. The seam that repairs: row 9 required "rows 1–5 built" while Q23 had just limited week 2 to rows 1–3, so §4.4 and §4.11 described two schedules for the third time. Neither week number moved to fix it; the gate's scope was named. And because a gate that runs green over a subset is not a verified system, **no §3 ledger row flips on a partial pass** (Q29).
```

### Pair 4 — §4.4, week 1 (separable)

**This pair is separable from the other three and I flag it as such.** The gate
did not cite it and the Director did not ask for it, but it is the same seam:
week 1 claims **win**, which is §4.11 row 5, which depends on row 4, which Q23
placed in week 3. Left alone it is the fourth §4.4/§4.11 disagreement already
queued. Drop this pair if the Director would rather rule on it separately; the
other pairs do not depend on it.

**OLD**

```
| 1 | Headless C++ core (grid, units, move, combat, win) **+ test suite.** Playable via debug commands. **UI-scaffolder agent starts UMG widget skeletons in parallel** — the whole game is played through UI, so it can't wait until wk 2. |
```

**NEW**

```
| 1 | Headless C++ core — §4.11 **rows 1–3** (grid and hex math, the §4.8 tables, movement and pathfinding) on top of the already-verified Combat/Repair at `5ffa8d6` — **+ test suite.** Playable via debug commands. Win and tiebreak detection is **row 5**, bundled with the turn loop and landing wk 3 (Q23); this cell used to name it here, one week ahead of the Capture & Fame row it depends on. **UI-scaffolder agent starts UMG widget skeletons in parallel** — the whole game is played through UI, so it can't wait until wk 2. |
```

### Pair 5 — §4.11, the preamble note above the table

**OLD**

```
Note **row 10's
format spec must exist by the row-9 integration pass**, because T-INT-02's
input file is a §4.10 save.
```

**NEW**

```
Note **row 10's
format spec must exist by the row-9 integration pass**, because T-INT-02's
input file is a §4.10 save. Rows 9 and 10 therefore state their dependencies
in **two parts** — what each gate needs in order to **run**, and what it needs
in order to **close** — because both are scoped to the command set of the log
they replay, and week 2's log carries only `{Move, Attack}` (§4.4). Reading
either row's requirement as a single set is what put a gate in a week this
table could not supply it.
```

### Pair 6 — §4.11, row 9's *Depends on* cell

Row 9's acceptance set (`T-INT-01..05`) and *Headless?* cell are unchanged.

**OLD**

```
Rows 1–5 built; vendoring + T-INT-01/04 can start with any subset
```

**NEW**

```
**Run vs close.** Vendoring and **T-INT-01/04** depend on no rules row at all — the sync script and the standalone gate run *are* the assert — and close as soon as vendoring lands. **T-INT-02/03/05** need only the rows behind the log they replay: rows 1–3 for week 2's `{Move, Attack}` log, and they re-open when rows 4–5 add `Capture`/`Build`/`EndTurn`. They **close on rows 1–5**, which is what this cell used to state as the whole dependency
```

### Pair 7 — §4.11, row 10's *Depends on* cell

Row 10's acceptance set (`T-SAVE-01..07`) and *Headless?* cell are unchanged.

**OLD**

```
4, 5 (command set + turn loop); 7 (scenario format); **format spec itself has no deps — write it first**
```

**NEW**

```
**Three parts, three dependency sets.** (a) *Format spec + header/version machinery* — **no deps at all; write it first**, and T-SAVE-04 (refusal on any header mismatch) closes on it alone, since it never applies a command. (b) *Headless replayer* — rows 1–3, plus row 7's **structural** half for the `scenarioId`/`scenarioHash` it loads; it runs T-SAVE-01/02/03/05/06 over week 2's `{Move, Attack}` log. (c) *Closure* — rows **4, 5** complete the command set (T-SAVE-01/03/05/06), row **6** completes T-SAVE-02's determinism composition, and T-SAVE-07 needs row 6's self-play besides. Slot I/O is week 5 and no headless gate waits on it
```

### Pair 8 — §4.7 register, Q20's assumption cell

Q20's ruling and its week numbers stand. What changes is that *"lands in week
2"* now names a run rather than a closure, so the row describes the schedule
§4.4 and §4.11 actually hold.

**OLD**

```
Ruled, as §4.11 itself proposed. §4.4's weeks 2, 4 and 5 and the note under the table now describe one schedule, and the distinction the split turns on is stated there rather than left to be re-derived: **a format is a test instrument** and ships with the gates that consume it (T-INT-02 wk 2, T-SAVE-07 wk 4); **slot I/O is a feature** and ships with the rest of the UI. Scheduling-adjacent to **Q23** and ruled on the same principle in the opposite direction — a milestone that outran its dependencies moved later; an instrument its own gates outran moved earlier.
```

**NEW**

```
Ruled, as §4.11 itself proposed. §4.4's weeks 2, 4 and 5 and the note under the table now describe one schedule, and the distinction the split turns on is stated there rather than left to be re-derived: **a format is a test instrument** and ships with the gates that consume it (T-INT-02 **first runs** wk 2, T-SAVE-07 wk 4); **slot I/O is a feature** and ships with the rest of the UI. Scheduling-adjacent to **Q23** and ruled on the same principle in the opposite direction — a milestone that outran its dependencies moved later; an instrument its own gates outran moved earlier. **Amended this revision, and the amendment is the useful part of the row.** The ruling was written into §4.4 without re-reading §4.11's dependency table, which required "rows 1–5 built" for row 9 while Q23 had just limited week 2 to rows 1–3 — so the document promised a gate, and its instrument, in a week its own build order could not support them. That is the Q23 contradiction class one layer down, and the third time these two sections have disagreed. It is repaired by **scoping, not by moving**: an integration or replay gate is scoped to the command set of the log it runs on, so T-INT-02 **runs** in week 2 over `{Move, Attack}` — which already reaches the whole compiler-divergence class it exists to catch, since `resolveDamage` holds the only non-integer step in the module — and **closes** in week 3 when rows 4–5 supply the remaining three commands. No week number moved. Whether a partial run may flip a §3 ledger row is registered as **Q29** rather than assumed.
```

### Pair 9 — §4.7 register, Q21's *Blocks* cell

The miscount: **T-SCN-11 prices four opposing routes on this map, not eight.**
§2.13.2's table is a four-Infantry × two-objective cross product; of its eight
cells, two are the seats' own guided lanes (T-SCN-06), four are the opposing
routes T-SCN-11 minimises over, and two are each seat's *other* Infantry to its
*own* objective — asserted by neither invariant, but the cells that make each
seat's minimum well-defined and therefore the "1 MP in each seat" asymmetry
claim in §2.13.2 checkable. All eight price on Q21's convention; only four are
T-SCN-11's.

**OLD**

```
T-SCN-06's pass/fail and T-SCN-08's reported integers; **T-SCN-11's eight opposing routes on the shipped map**, which price on this same convention; §2.13.1's three-map lane table if the answer is "as deployed"
```

**NEW**

```
T-SCN-06's pass/fail and T-SCN-08's reported integers; **T-SCN-11's four opposing routes on the shipped map** — the four cells of §2.13.2's eight-route table that run against a guided lane (East (9,3) and (9,1) → South; West (1,3) and (1,5) → North) — which price on this same convention, as do the table's other four cells: the two guided lanes themselves (T-SCN-06's, not T-SCN-11's) and each seat's second Infantry to its own objective; §2.13.1's three-map lane table if the answer is "as deployed"
```

### Pair 10 — §4.7 register, Q21's assumption cell (the scope re-check)

Same correction on the other side of the row: **ten → eight**, because the
eight-route table already contains the two guided lanes. The rationale after it
is unchanged and reads true — it agrees with §2.13.1 note 2 as the Director
rewrote it: (9,1) sits on none of the priced routes, no map's numbers move under
either reading as drawn, and *Ferrum Crossing* is only the map where a *future*
deployment edit landing in a priced route would flip a gate. The sentence about
1 MP of slack against both T-SCN-06's ceiling and T-SCN-11's inequality is
already in the cell and stays.

**OLD**

```
It holds, and at a sharper resolution: **no starting unit sits on any of the ten routes *Ferrum Crossing* now prices** (its two guided lanes and §2.13.2's eight T-SCN-11 routes), (9,1) among them, and both stretch lanes were already clear — so an "as deployed" ruling would move **no number on any map as drawn**.
```

**NEW**

```
It holds, and at a sharper resolution: **no starting unit sits on any of the eight routes *Ferrum Crossing* now prices** — §2.13.2's four-Infantry × two-objective table *is* the whole priced set, and it already holds the two guided lanes (T-SCN-06) alongside T-SCN-11's four opposing routes and the two same-seat routes that fix each seat's cheaper prize. (9,1) is the origin of two of the eight and lies on the interior of none of them, and both stretch lanes were already clear — so an "as deployed" ruling would move **no number on any map as drawn**. This row previously read "ten," adding the two guided lanes to a table that already contained them, and called all eight T-SCN-11's; the corrected split is 2 + 4 + 2.
```

### Pair 11 — §4.7 register preamble, admitting Q29

**OLD**

```
the one raised by correcting that
correction (Q26), the guided opening's one input-gating constraint (Q27), and
the reading the Q22 ruling exposed the moment its new invariant was measured
against the shipped map (Q28)
```

**NEW**

```
the one raised by correcting that
correction (Q26), the guided opening's one input-gating constraint (Q27), the
reading the Q22 ruling exposed the moment its new invariant was measured
against the shipped map (Q28), and the ledger-flip criterion exposed by
scoping the week-2 parity gate to its command set (Q29)
```

### Pair 12 — §4.7 register, the new Q29 row

Appended after Q28, which is the last row of the table. The anchor is Q28's
closing characters; the new row follows on its own line. Q29 carries a
conservative reading in force, per the register's stated convention — it can
only delay a provenance claim, never overstate one, so a looser ruling
invalidates no passing gate and no gate is blocked while it is open.

**OLD**

```
reading (b) would have passed. |
```

**NEW**

```
reading (b) would have passed. |
| **Q29** | Ledger-flip criterion for a partially-scoped gate. §4.11 rows 9–10 now **run** their gates in week 2 over a `{Move, Attack}` log and re-run them over the complete command set in week 3 (Q20, amended). §3's ledger says a row is verified when it cites "the commit and passing test IDs that back it," and §3's two bars require agent-authored tests that pass plus a human sign-off — but neither says whether *passing* means the acceptance set ran over the system's whole input domain. Without a rule, a green week-2 T-INT-02 could flip a proposed ledger row while the log it replays is missing three of the five §4.9 commands. | §3's ledger rows for §4.9 and §4.10 (both proposed rows, both unwritten today); no gate — every test runs either way, this governs only what may be *claimed* from a run | **Conservative reading in force:** a row flips only when its **full** acceptance set passes over the **complete** §4.9 command set at one commit; a partial pass is reported as a run and never as a closure, and §4.11 rows 9–10 are written in exactly those two parts. Free in the conservative direction — it can only delay a claim, so a later loosening invalidates nothing that passed. The alternative worth weighing, since the information is real and currently discarded: record partial passes in the ledger as a dated *"green over subset X at commit Y"* line, which reports more without claiming more — that is a §3 presentation decision, not a technical one, which is why it is registered rather than assumed. |
```

---

## Build order

The §4.11 table as it reads **after** pairs 5–7. Rows 1–8 are unchanged this
revision and their *Depends on* cells are abbreviated here for review only — the
document's cells are not edited. Rows 9–10 carry the new text verbatim.

| # | System (ledger row) | Depends on | Headless? | Acceptance test IDs |
|---|---|---|---|---|
| 1 | Hex grid & math (Stub 1) | *unchanged* — none (Q1 pins bounds) | Yes | T-HEX-01..07 |
| 2 | Data tables (§4.8) | *unchanged* — none (MoveClass blocked on Q2) | Loader yes; import parity in-editor | T-DATA-01..06 |
| 3 | Movement & pathfinding (Stub 3) | *unchanged* — 1, 2 | Yes | T-MOVE-01..06 |
| 4 | Capture & Fame economy (Stub 4) | *unchanged* — 3 | Yes | T-FAME-01..09 |
| 5 | Turn loop & win/tiebreak (Stub 5) | *unchanged* — 4 + Combat/Repair @ `5ffa8d6` | Yes | T-TURN-01..09 |
| 6 | Opponent AI (Stub 6) | *unchanged* — 5 | Yes | T-AI-01..06 + self-play smoke |
| 7 | Scenario file & validator (Stub 7) | *unchanged* — 1, 2 structural; 3 for the priced half | Yes; MCP wraps it, manual fallback | T-SCN-01..09, 11 (10 reserved on Q26) |
| 8 | UI binding (Stub 8) | *unchanged* — 5, 7 | Contract + queries yes | T-UI-01..04 |
| 9 | Presentation bridge & integration — §4.9 | **Run vs close.** Vendoring + T-INT-01/04: no rules row, close on vendoring. T-INT-02/03/05: rows **1–3** to run over week 2's `{Move, Attack}` log, re-open on rows 4–5, **close on rows 1–5** | Source/compile gates yes; parity + statelessness in-editor | T-INT-01..05 |
| 10 | Save & replay — §4.10 | **Three parts.** (a) format spec: no deps, write first, closes T-SAVE-04. (b) replayer: rows **1–3** + row 7's structural half; runs T-SAVE-01/02/03/05/06 over `{Move, Attack}`. (c) closure: rows **4, 5**, then **6** for T-SAVE-02 and T-SAVE-07 | Yes, all but slot I/O | T-SAVE-01..07 |

Critical path is untouched: `1 → 3 → 4 → 5 → 6/8`. Nothing on it moved; rows 9
and 10 hang off it in two pieces each instead of one.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.1, note 2 | "…moved East's second Infantry to (9,1), which lies on none of **the ten routes** *Ferrum Crossing* prices, **no map's numbers move under either reading of Q21 (§4.7) as drawn**…" | "…which lies on none of **the eight routes** *Ferrum Crossing* prices…" — one word, nothing else in the note changes | Same double-count as Q21's row, and its twin: §2.13.2's table is a 4 × 2 cross product holding eight routes, two of which are the guided lanes. If Q21's row is corrected to eight and this note keeps ten, the document gains a fresh numeric disagreement in the exact place it just closed one. This is §2 text and the Director's own edit, so it is filed rather than drafted. The note's *substance* is right and Q21's row is being made to agree with it. |

---

## Open questions for the Director

Two rule gaps found while writing these gates; one is filed as **Q29**, one is
deliberately not filed.

1. **Q29 — filed.** When may a §3 ledger row flip if its acceptance set has only
   passed over part of its input domain? §3 requires "the commit and passing test
   IDs," and both bars for *agent-verified*, but says nothing about coverage of
   the domain. This gap is created by my own ruling above — partially-scoped
   gates are new to the document as of this revision — and the ledger's honesty
   is the whole point of §3, so the rule belongs to the Director. A conservative
   reading is in force and blocks nothing.

2. **`EndTurn` in week 2 — not filed, and here is why.** §4.11 row 5 bundles
   *turn loop* with *win/tiebreak*, and row 5 is week 3 under Q23. So week 2 has
   no `EndTurn`, its log is single-turn, and T-SAVE-01/03 run inside one turn.
   That follows from the document as written rather than being a gap, so I have
   assumed it rather than registered it. **It becomes a question the moment the
   Director wants week-2 debug play to advance turns or alternate seats** — that
   would require carving turn *alternation* out of row 5 from win *detection*,
   which re-opens the row-5 boundary Q23 just settled and would need an ID
   (Q30). I have not pre-empted that.

3. **Awareness, not a question.** §4.10's platform-stability-by-construction
   claim rests on every hash field being an integer. Rows 4–5 must not introduce
   a non-integer step — a percentage income rate, a ratio in a §2.8 tiebreak key
   — or the divergence class widens and the week-2 argument narrows accordingly.
   The re-open rule in pairs 1–3 covers this mechanically (a widened command set
   re-runs the gate), and Q5/Q6 are the two unruled economy values that would
   decide it, so no new ID. Worth knowing that the two are connected.

---

## Handoffs

- **scenario-designer / Director** — the §2.13.1 note-2 change request above is
  one word in §2 text. No map, lane cost, terrain figure or deployment hex is
  affected, and the eight routes and their MP values are untouched.
- **rules-designer** — nothing new. Q5/Q6 remain the rules-side inputs to the
  integer-field point in Open question 3.
- **ux-onboarding-designer** — unchanged: §4.10's overwrite-confirm surface is
  still recorded as unowned, and the save-slot UI is still week 5. Nothing in
  this revision moves it.
- **§3 provenance ledger (Director)** — Q29 is the ledger's question, not §4's.
  Until it is ruled, §4.11 rows 9–10 are written so that no partial pass reads
  as a closure.

---

## Grounding

| Claim | Backed by |
|---|---|
| Week 2 is rows 1–3, weeks 3 has rows 4–5 | §4.4 note under the milestone table (Q23, ruled); §4.7 register Q23 row |
| Row 9 required "Rows 1–5 built," carving out only T-INT-01/04 | §4.11 build-order table, row 9 *Depends on* |
| Row 10 depended on "4, 5 (command set + turn loop)" | §4.11 build-order table, row 10 *Depends on* |
| §4.4 week 2 delivers the §4.10 format + headless replayer and asserts T-INT-02 runs there | §4.4 milestone table, week 2 (Q20, ruled) |
| T-INT-02 replays a recorded command log headless and in-engine to one canonical hash | §4.9 "Parity gates" and the Integration-parity stub, T-INT-02 |
| The only non-integer computation is inside `resolveDamage`; every hash field is an integer | §4.10 "Canonical state hash" — "`eff` and the HP ratio exist only transiently inside `resolveDamage`… platform-stable by construction" |
| The §4.9 command set is `Move`, `Attack`, `Build`, `Capture`, `EndTurn` | §4.9 §2 "Command in / events out" |
| `Capture` and `Build` are row 4, `EndTurn` is row 5 | §4.11 rows 4–5; §2.7 (capture and production); §2.10 IN row ("these land wk 3, not wk 1–2") |
| T-SAVE-04 is header-only and applies no command | §4.10 stub, T-SAVE-04; the version policy above it |
| T-SAVE-02 composes T-AI-06 among the determinism gates | §4.10 stub, T-SAVE-02 |
| T-SAVE-07 needs self-play logs and closes wk 4 | §4.10 stub, T-SAVE-07; §4.4 week 4 |
| Row 7's structural half lands with rows 1–2 and supplies `scenarioId`/`scenarioHash` | §4.11 row 7 and the paragraph beneath the table; §4.10 file-layout table |
| Combat, Repair and Type-effectiveness are green at `5ffa8d6`; everything else is `*pending*` | §3 provenance ledger (four populated rows, eight pending) |
| Week 1 currently claims "win," which is row 5 | §4.4 week 1 vs §4.11 row 5 ("Turn loop & win/tiebreak", depends on 4) |
| *Ferrum Crossing* prices eight routes: 4 Infantry × 2 objectives | §2.13.2 "Non-contention, measured" table (4 rows × 2 columns) |
| Two of those eight are the guided lanes, priced Bridge-free | §2.13.2 "Bridges permitted on opposing routes and forbidden on the two guided lanes"; §2.13.2 "Guided opening" paragraph (T-SCN-06) |
| T-SCN-11 minimises the *opposing* seat's routes → 4 cells on this map | §4.7 Stub 7, T-SCN-11 (Q22, Q28 ruled); §2.13.2 "checked on **eight** routes" table read per-lane |
| The remaining two cells carry the per-seat minima the asymmetry claim uses | §2.13.2 "West's cheapest Infantry route is **5 MP to South against 6 to North**… (all four figures in the eight-route table above)" |
| No starting unit sits on a priced route; (9,1) among them | §2.13.2 starting-position table vs. the eight listed paths; §2.13.1 note 2 |
| 1 MP of slack against T-SCN-06's ceiling and against T-SCN-11's inequality | §2.13.2 "1 MP of slack against the 6 MP ceiling"; "5 against 6 in both seats" (Q28) |
| §3's ledger states commit + passing test IDs but not domain coverage | §3 "Provenance ledger" paragraph and the three honesty rules |
| The register runs Q1–Q28 with ten ruled before this revision | §4.7 register: Q7, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28 |
