> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> All 11 replacement pairs in this file **have been applied to the master GDD**.
> Verified 2026-08-10 against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b` (3365 lines): every OLD
> block is absent from the master, matched newline-insensitively. Re-applying is a
> no-op at best.
>
> Its quoted "current" text, register extents and open items are a **snapshot of
> the moment it was written**, not the state of the document.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Technical design — addendum `fixture-widened` (tech-director)

## Placement
Old→new pairs against the merged master (md5 `1bfae9f169230f3bdcea4fab48b100f8`):
§3 (the ledger prose, the `0897cb5` editor-pass record), §4.4 (week 3), §4.5 (the
"Specification outruns the build" risk cell), §4.8 (the `dataCommit` ruling),
§4.9 (part 2's `0897cb5` vendoring paragraph), §4.11 (rows 9 and 10). No section
is redrafted.

## Draft

### The sort this round turns on

A clause about the committed fixture survives crew `c2f5860` only where the
pinning sits inside the clause's own subject and the verb is not a finite present
tense about the file. So a participial modifier on the run — "ran and passed …
over a parity fixture carrying `Move`, `Attack` and `EndTurn`" — describes the
file that run replayed and is unmoved. A finite present-tense predicate — "the
parity fixture … **carries** … and carries no `Capture` and no `Build`" — asserts
of the file as it stands, and is amended by pinning it to the run it was measured
at. Nothing here is repaired by saying the file "has since" changed.

### Dispositions — the 35 candidates

| # | Disposition | Reason |
|---|---|---|
| 1 | outside this round | Predicates on `sync_stratdata.py`'s carrying the fixture from `5c47cc1`. The widening moved the file's bytes, not which script vendors it. |
| 2 | amended — Pair 1 | Finite present tense about the committed file's contents. |
| 3 | amended — Pair 2 | "the two commands this fixture lacks" is a present-tense predicate about the file, and it also states what a closure waits on. |
| 4 | unchanged and still true | Predicates on `GATE-REPLAY-FIXTURE`'s behaviour when the fixture is **absent** and against the bundled buggy replayer, not on the fixture's contents. |
| 5 | amended — Pair 5 | "the fixture run there does not carry" is finite present tense. |
| 6 | amended — Pair 6 | States what `T-INT-02`/`T-INT-03`'s closure waits on. |
| 7 | amended — Pair 7 | States what `T-SAVE-06`'s closure waits on. |
| 8 | amended — Pair 8 | States what the three IDs' closure waits on. |
| 9 | pinned to `0897cb5`, so unmoved | "over a parity fixture carrying …" is a participial modifier on the run at `0897cb5`; it describes what that pass replayed. |
| 10 | amended — Pair 9 | "the parity fixture replayed there **carries**" pins the referent but asserts in the present tense of the file. |
| 11 | amended — Pair 10 | States what `T-SAVE-06`'s closure waits on. |
| 12 | unchanged and still true | Q29's per-ID reading. No ID closes at the widening, so nothing here moves. |
| 13 | outside this round | Predicates on **the gate's log** — row 10 part (b)'s hand-authored log at `ec15be6` — not on `data/parity_fixture.save`. |
| 14 | unchanged and still true | Predicates on the AI. `AiCommandKind` is still `{Build, Move, Attack, EndTurn}` and a self-play match still emits four kinds; the fixture carries `Capture` because the emitter appends it outside the AI's choice, which leaves this sentence's subject untouched. |
| 15 | unchanged and still true | Predicates on part (b)'s hand-authored log, a different artifact, which carried all five kinds before this round and is unchanged by it. |
| 16 | unchanged and still true | Predicates on `T-SAVE-07`'s self-play log and on what that ID asserts. |
| 17 | unchanged and still true | Pinned at `ec15be6`, and about the log rows 4–5 supply. |
| 18 | unchanged and still true | A schedule statement about when rows 9–10 run and re-run their gates. |
| 19 | unchanged and still true | A dependency statement: rows 1–3 for the week-2 log, re-opening on what rows 4–5 added. Rows 4–5 still supply those three kinds. |
| 20 | unchanged and still true | Predicates on the week-2 log the row-9/10 gates ran over. |
| 21 | unchanged and still true | Same subject as 14 and 16 — the self-play log and the AI's vocabulary. |
| 22 | unchanged and still true | Q29's per-ID reading, restated for row 7. |
| 23 | outside this round | §4.8's UStruct bool-prefix measurement; matched on vocabulary only. |
| 24 | amended — Pair 3 | The enum claim survives verbatim; its framing as *the reason the fixture lacks `Capture`* does not, because the log carries the kind without the AI producing it. |
| 25 | amended — Pair 4 | `aiViewOf` now assigns `buildlist`, so "never asks for it" is false of the harness as it stands. |
| 26 | unchanged and still true, but re-tensed inside Pair 4 | Fame sufficiency was never what stopped `Build`, and `startingFame`, `CostFame`, the side-0 `Factory` hex and `queueBuild`'s refusal condition are all untouched. Pair 4 moves its verb to the past so the sentence does not presuppose that something is still stopping `Build`. |
| 27 | outside this round | A §2 `startingFame`/Flag-Unit fragment; matched on vocabulary only. |
| 28 | outside this round | The §4.8 terrain schema table. |
| 29 | unchanged and still true | §4.11's re-open/close condition and Q29's partial-pass reading; both hold. |
| 30 | pinned to `0897cb5`, so unmoved | "The UE tree **there** records `dataCommit` `862a225`" is pinned to that commit, and `4ceaf93` is a later commit rather than a correction of it. |
| 31 | unchanged and still true | Which script makes the copy. |
| 32 | unchanged and still true | §4.8's 2026-08-06 ruling on what `dataCommit` names and when it advances. The illustrative clause that follows the ruling's colon, also in §4.8, is amended at Pair 11; that clause is not among the 35. |
| 33 | unchanged and still true | What `GATE-DATA-VENDOR` reads and what it asserts. |
| 34 | unchanged and still true | Which bytes move by which script under which gate. |
| 35 | unchanged and still true | The *vendor* wording ruling. |

### What my own sweep added

I matched a whitespace-collapsed reading of the master multiline, hunting the
predicate rather than the vocabulary: any finite clause whose subject is the
committed fixture, the vendored data or the manifest, and whose predicate says
what it holds or why it lacks something. That found **one** site the candidate
set does not contain — the illustrative clause after §4.8's `dataCommit` ruling,
which states in the present tense that the manifest records `b1ea992`, and which
is Pair 11. Apart from that clause, the sweep surfaced no site outside the 35
that predicates in the present tense on what the committed fixture carries or on
why a command kind is missing from it.

---

### Pair 1
**Anchor:** §3, ledger prose, the `0897cb5` editor-pass record

**OLD**
```
The parity fixture they run over carries `Move`, `Attack` and `EndTurn` and carries **no `Capture` and no `Build`**;
```
**NEW**
```
The parity fixture they ran over at `0897cb5` carried `Move`, `Attack` and `EndTurn` and **no `Capture` and no `Build`**;
```

---

### Pair 2
**Anchor:** §3, ledger prose, same record, the sentence stating what the three IDs' closure waits on

**OLD**
```
What their closure waits on is a parity fixture carrying the complete §4.9 command set, and the two commands this fixture lacks are absent for different reasons.
```
**NEW**
```
Among what their closure waits on is a further editor pass, and none has run since `0897cb5`. The committed fixture carries the complete §4.9 command set at [`c2f5860`](https://github.com/jakemartin/stratocracy-crew/commit/c2f5860) and is vendored at that commit into the UE project at `4ceaf93`; the two commands it had lacked were absent for different reasons.
```

---

### Pair 3
**Anchor:** §3, ledger prose, same record, the `Capture` mechanism

**OLD**
```
**`Capture` cannot be produced at all:** `AiCommandKind` is `{Build, Move, Attack, EndTurn}` and has no `Capture` member, so nothing reading that enum can emit one.
```
**NEW**
```
**`Capture` cannot be produced by the AI at all:** `AiCommandKind` is `{Build, Move, Attack, EndTurn}` and has no `Capture` member, so nothing reading that enum can emit one, and it gained none at `c2f5860` — `Ai.h` keeps capture completion a turn-boundary event owned by row 4. The fixture carries the kind because `appendAiTurn` appends one `Capture` per side at the close of that side's turn, outside the AI's choice: `openTurn` already ticks capture on an objective the side held, so what the appended command catches is an objective the side moved onto during the turn just played. §4.10's required `unit` field on `Capture` is written as the side's lowest unit id with `canCapture`, and `applyCommand` never reads it.
```

---

### Pair 4
**Anchor:** §3, ledger prose, same record, the `Build` mechanism and the Fame sentence that follows it

**OLD**
```
**`Build` can be produced, and this fixture's harness never asks for it:** the harness builds its `AiState` without assigning `buildlist`, and `chooseBuild` iterates that list and returns -1 when it is empty, before Fame is consulted; `Balance`'s equivalent view does assign a buildlist. Fame sufficiency is not what stops it — `startingFame` is 200 a side, Infantry's `CostFame` is 100, side 0 owns the `Factory` hex at column 1 row 4 with `IsSpawnPoint` true, and `queueBuild` refuses only when `fameTotal` is below the cost.
```
**NEW**
```
**`Build` can be produced, and the harness that emitted the fixture replayed at `0897cb5` never asked for it:** `aiViewOf` built its `AiState` without assigning `buildlist`, and `chooseBuild` iterates that list and returns -1 when it is empty, before Fame is consulted; `Balance`'s equivalent view does assign a buildlist. Fame sufficiency was not what stopped it — `startingFame` is 200 a side, Infantry's `CostFame` is 100, side 0 owns the `Factory` hex at column 1 row 4 with `IsSpawnPoint` true, and `queueBuild` refuses only when `fameTotal` is below the cost. At `c2f5860` `aiViewOf` supplies `Infantry`, looked up by `Id`, and the fixture carries `Build`.
```

---

### Pair 5
**Anchor:** §4.4, the week-3 milestone row

**OLD**
```
What their closure waits on is a parity fixture carrying the complete §4.9 command set, which rows 4–5 supply and the fixture run there does not carry (§3).
```
**NEW**
```
Among what their closure waits on is a further editor pass, none having run since the one at `0897cb5`: rows 4–5 supply `Capture` and `Build`, the fixture that pass replayed did not carry them, and the committed fixture carries the complete §4.9 command set at `c2f5860` (§3).
```

---

### Pair 6
**Anchor:** §4.5, the "Specification outruns the build" risk cell, the row-9 clause

**OLD**
```
what their closure waits on being a parity fixture carrying the complete §4.9 command set,
```
**NEW**
```
among what their closure waits on being a further editor pass, none having run since `0897cb5`,
```

---

### Pair 7
**Anchor:** §4.5, the same risk cell, the row-10 clause

**OLD**
```
and what its closure waits on is a parity fixture carrying the complete §4.9 command set (§3)
```
**NEW**
```
and among what its closure waits on is a further editor pass replaying the widened fixture in-engine, none having run since `0897cb5` (§3)
```

---

### Pair 8
**Anchor:** §4.9 part 2, the `0897cb5` vendoring paragraph

**OLD**
```
without closing, their closure waiting on a parity fixture carrying the
complete §4.9 command set (§3);
```
**NEW**
```
without closing, among what their closure waits on being a further editor
pass, none having run since the one at `0897cb5`; the committed parity fixture
carries the complete §4.9 command set at `c2f5860`, vendored into the UE
project at `4ceaf93` (§3);
```

---

### Pair 9
**Anchor:** §4.11, build-order table, row 9's dependency cell

**OLD**
```
the parity fixture replayed there carries `Move`, `Attack` and `EndTurn` and carries no `Capture` and no `Build` (§3)
```
**NEW**
```
the parity fixture replayed there carried `Move`, `Attack` and `EndTurn` and no `Capture` and no `Build`, and the committed fixture carries the complete §4.9 command set at `c2f5860` (§3)
```

---

### Pair 10
**Anchor:** §4.11, build-order table, row 10's dependency cell, the `T-SAVE-06` clause

**OLD**
```
What its closure waits on is a parity fixture carrying the complete §4.9 command set.
```
**NEW**
```
Among what its closure waits on is a further editor pass replaying the widened fixture in-engine, none having run since `0897cb5`.
```

---

### Pair 11
**Anchor:** §4.8, the `dataCommit` ruling, the illustrative clause after its colon
(source lines 2686–2689; §4.8 spans 2669–2771 and §4.9 begins at 2772)

**OLD**
```
not a stale one: it records
[`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992), and
the three CSVs are byte-identical at that commit and at
[`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) (§3).
```
**NEW**
```
not a stale one. The manifest recorded
[`862a225`](https://github.com/jakemartin/stratocracy-crew/commit/862a225) at
`0897cb5` and records
[`c2f5860`](https://github.com/jakemartin/stratocracy-crew/commit/c2f5860) at
`4ceaf93`, which re-vendored the widened parity fixture; the three CSVs are
byte-identical across those two vendorings.
```

No NEW above contains its own OLD, so none of these eleven is an insertion.

## Change requests

None open.

## Open questions for the Director

1. **Does the emitter's buildlist belong in the document as a ruling?** `aiViewOf`
   supplies `{Infantry}`, looked up by `Id`. The choice was made on
   `test_balance.cpp`'s precedent and measured inert — `{Infantry}`,
   `{Infantry, Tank}` and all four unit types each emit a byte-identical fixture,
   because Q9 orders the affordable set by ascending cost and `Infantry` is the
   cheapest. Pair 4 states it as a measurement. If the fixture's build menu is a
   rule rather than an implementation detail, it needs a ruling and a gate.
2. **Do the appended `Capture` and `kParityTurns = 48` belong in the document?**
   Both were engineering calls, not rulings. `kParityTurns` counts side-turns and
   `turnCap` is 20 game turns, so 40 side-turns is the ceiling no match on this
   scenario can exceed; 48 is that ceiling with headroom, and the widened log uses
   13 of the old 14. Pair 3 states the `Capture` append as a mechanism.
3. **Does `T-INT-03`'s closure wait on the parity fixture at all?** §3, §4.4, §4.5
   and §4.9 all state the three IDs' closure condition jointly, but `T-INT-03`
   asserts over the bridge's command surface — commands submitted in-engine — and
   not over this file. Pairs 2, 5, 6 and 8 use a non-exhaustive "among what …
   waits on" so as not to decide it either way. If the answer is no, the joint
   phrasing wants splitting.
4. **What should §4.8's `dataCommit` illustration point at?** Its clause recorded
   `b1ea992` while §3 records `862a225` at `0897cb5`, so the two disagreed before
   this round and the re-vendoring moved the value again. Pair 11 replaces the
   illustration with the pinned pair of vendorings; if the "a `dataCommit` behind
   the crew commit this document stands at is expected" point is to keep a worked
   example, it needs a commit the Director names.
5. **Crew `b5f524d`.** §3 records that the fourteen closure clauses `9289c1d`
   introduced exist and are false; it does not record their deletion. Not this
   round's subject, and no pair here touches it.

## Grounding

| Pair | Backed by |
|---|---|
| 1 | Fact block §2 (the fixture at crew `5072d10`: no `Build`, no `Capture`) and §1 ("carries" is a present-tense property of the file now); §3's own `0897cb5` editor-pass record supplies the pin |
| 2 | Fact block §2 (all five kinds at `c2f5860`), §4 (UE `4ceaf93` re-vendored it, `dataCommit` `862a225` → `c2f5860`), §5 (`T-INT-02` did not close and has not re-run; no editor pass since `0897cb5`) |
| 3 | Fact block §3, `Capture` paragraph: enum unchanged, `Ai.h`'s turn-boundary ownership, `appendAiTurn`'s per-side append, §4.10's `unit` field written from the lowest capturing unit id and never read by `applyCommand`, and the `openTurn` interaction |
| 4 | Fact block §3, `Build` paragraph: `aiViewOf` never assigned `s.buildlist`, `chooseBuild` returned -1 before Fame was consulted, `aiViewOf` now supplies `Infantry` by `Id`, and Fame sufficiency was never the blocker |
| 5 | Fact block §2 and §5, as Pair 2; the rows-4–5 clause is the master's own and is unmoved |
| 6 | Fact block §5, first bullet (the widening changes what closure waits on and does not supply the in-engine run) |
| 7 | Fact block §5, first bullet, applied to `T-SAVE-06`, which §4.11 asserts jointly with `T-INT-02` |
| 8 | Fact block §2, §4 and §5, first bullet |
| 9 | Fact block §2 (both columns) and §1 (what a pin does and does not preserve) |
| 10 | Fact block §5, first bullet |
| 11 | Fact block §4 (`dataCommit` `862a225` → `c2f5860` at `4ceaf93`; only the fixture moved among the vendored data, the CSVs being byte-identical across the two vendorings); §3 of the master records `862a225` at `0897cb5` |
| Open question 1 | Fact block §3 (buildlist contents measured inert) and §6 (the choice is unruled) |
| Open question 2 | Fact block §4 (`kParityTurns` 14 → 48, side-turns vs `turnCap`) and §6 (engineering calls; the 13-of-14 measurement) |
| Open question 3 | Fact block §5, third bullet (`T-INT-03` is not reached by the widening) |
| Open question 4 | Fact block §4; the master's §4.8 clause and §3 record |
| Open question 5 | Fact block §4, closing note |
