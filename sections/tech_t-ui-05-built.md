# Technical design — T-UI-05 built and gated addendum (tech-director)

Addendum against the merged master. Exact OLD/NEW pairs only.

---

### Pair 1 — §3 ledger status line: the commit this draft stands at

Replacement. Moves the tracker's standing commit and parent to the commit this
round records.

**OLD**

This draft stands at 2026-08-04, at commit [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) in the crew repo, whose parent is [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b).

**NEW:**

This draft stands at 2026-08-04, at commit [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) in the crew repo, whose parent is [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303).

---

### Pair 2 — §3, the critical-path ID list

Replacement. `T-UI-05` leaves the set of path IDs that are written and
asserting without being green.

**OLD**

the path IDs still written and asserting without being green are **T-UI-03**, **T-UI-04** and **T-UI-05**, and row 8's other dependency is **row 7**

**NEW:**

the path IDs still written and asserting without being green are **T-UI-03** and **T-UI-04**, `T-UI-05` having since closed at `41a1452` as recorded at the end of this paragraph, and row 8's other dependency is **row 7**

---

### Pair 3 — §3, the three ruled-but-unbuilt snapshot additions

Replacement. The sentence asserted, in the present tense, that no code
implements the additions or `T-UI-05`; it now records what was true at
`7c36303` and points at the commit that changed it.

**OLD**

**No code implements any of the three**, and the same rulings minted **`T-UI-05`**, a headless snapshot-fidelity check that no code implements either, so what row 8 lacks after this commit is no longer the in-editor pass alone.

**NEW:**

**No code implemented any of the three at this commit**, and the same rulings minted **`T-UI-05`**, a headless snapshot-fidelity check no code implemented either, so what row 8 lacked after this commit was no longer the in-editor pass alone. The two snapshot fields and `T-UI-05` were built at `41a1452`, recorded at the end of this paragraph; the presentation block is declared there rather than filled.

---

### Pair 4 — §3, the driver's `snapshot` command and the presentation block

Replacement. `at that commit or since` reached forward past `41a1452`, where the
block is declared. The claim is scoped back to the commit it was measured at.

**OLD**

the snapshot and not the whole view-model, whose other half, §4.7 Stub 8's presentation block, is produced by no rules field and implemented by no code at that commit or since,

**NEW:**

the snapshot and not the whole view-model, whose other half, §4.7 Stub 8's presentation block, is produced by no rules field and was implemented by no code at that commit,

---

### Pair 5 — §3, the landing record for `41a1452`

**Insertion.** OLD is the unique anchor sentence that closes the status
paragraph; the new text is appended after it, and the anchor is unchanged.

**OLD**

No in-editor harness is among the twelve `main()` definitions above.

**NEW:**

No in-editor harness is among the twelve `main()` definitions above. **Row 8 was then rebuilt**, at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), whose parent is [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), against the snapshot additions ruled on 2026-08-04 and the `T-UI-05` minted with them — the GDD half of all of them having merged **before any code satisfied them**, as row 5's rebuild did. The commit changes **nine** files: `cpp_reference/Ui.h`, `cpp_reference/Ui.good.cpp`, `cpp_reference/Ui.buggy.cpp`, `cpp_reference/test_ui.cpp`, `cpp_reference/Driver.h`, `cpp_reference/Driver.good.cpp`, `cpp_reference/test_driver.cpp`, `spec/ui_spec.md` and `README.md`; no other file in the repo changed. The gate is **`T-UI-01`, `T-UI-02`, `T-UI-05` and `GATE-CAP-PARTIAL`, 34/34 under clang++ and MSVC both** — `g++` is still not installed on this machine — and **the 34 counts printed checks, not IDs**. Pass-1 `cpp_reference/Ui.buggy.cpp` is blocked at **21/34** under both compilers — **13 FAIL lines over three distinct IDs**, `T-UI-02`, `T-UI-05` and `GATE-CAP-PARTIAL` — while `T-UI-01` is green in both passes. The other eight harnesses are **unchanged** under both compilers — hex 7/7, data 6/6, move 6/6, combat 17/17, economy 9/9, turn 11/11, scenario 12/12, ai 7/7 — their sources being byte-identical to `7c36303`. **`T-UI-05` closes here and the row still does not flip.** It is headless, has no in-editor half and no unrun fixture, so Q29 is satisfied for it; **T-UI-03 and T-UI-04 did not run**, being in-editor Unreal Automation marked † in §4.11, and **no editor pass exists at this commit**. **Both are printed by name with that reason before the tally, and that is measured at this commit rather than inherited** — `cpp_reference/test_ui.cpp` is one of the nine files this commit changes, so the earlier run's behaviour would not establish it. Rebuilt from `Ui.good.cpp` at `41a1452`, the two `NOT RUN` lines are output lines **76** and **82** and the `34/34 passed` tally is line **101**; each names its ID, states that it is in-editor Unreal Automation marked †, and states that no in-editor pass exists at this commit. That is the clang++ run; the MSVC run was verified at 34/34 with zero FAIL lines. **What changed about row 8 is which IDs it lacks, not whether it flips:** before this commit the editor pass was not the whole of what the row lacked, because `T-UI-05` was headless and unimplemented, and now it is — the row keeps the partial-pass posture rows 2 and 7 hold. **No acceptance ID is minted by this commit**, so §4.5's written-ID count does not move at this landing, its green count moves 52 → 53 and its unclosed count moves 19 → 18. §4.4 scheduled `T-UI-05` for **week 3**, so this closure is **ahead of the milestone table, not behind it**. **What was built is the snapshot's ruled additions**: `isGuidedMarked`, the per-factory group `{hex, owner, hasBuiltThisTurn, buildWaiting, spawnBlocked}` and the per-side `incomePerTurn`. The field contract `T-UI-05` runs over is **27 rows — 22 mirrors and 5 DECLARED DERIVED**. `DriverUnit` gained a `placement` field, because `isGuidedMarked` is a property of the placement rather than of the unit's current hex. **The presentation block is declared and deliberately NOT filled** by `buildUiSnapshot`: both its members have owners that are not the rules module, and clause (c) does not reach them because the block is not in this invariant's subject. **The implementation of `T-UI-05`'s clause (b) was rewritten because the first one passed its own pass-1 variant**, and that is recorded rather than smoothed over; the clause's own text is unedited. Clause (b) requires each DECLARED DERIVED field to be recomputed *inside* the check; the first implementation recomputed by calling the **same helpers the projection called**, so for the wrong `incomePerTurn` and the wrong `isGuidedMarked` — both planted in those shared helpers — the check compared each value to itself and returned clean. The three derivations are now **written out a second time inside the check**, which is why a duplication sits there that would otherwise read as an oversight. **A discrepancy is registered rather than acted on.** `spawnBlocked` is implemented on **occupancy alone**, mirroring `cpp_reference/Economy.h::resolveBuilds`, which asks `isOccupied` and never consults terrain — the reading §4.7 Stub 8 states, whose derivation is *no hex at or adjacent to the factory is free*; §4.10's parenthetical instead describes the same field as a function of unit positions **and terrain**. The build followed the stub, no invariant text changed and no acceptance ID was minted; a passability filter would report a factory blocked at a hex the shipped spawner would place on. **`GATE-DRV-12` was extended in the same commit, and the extension is measured to discriminate:** the version at `7c36303`, rebuilt against the pass-1 module, passes **12/12** — it could not see any of the five defects that module carries — while the extended version fails it at **11/12**, the single FAIL being `GATE-DRV-12`. The driver suite is **`GATE-DRV-01..12`, 12/12 under clang++ and MSVC both**, the same ID range as at `7c36303`, and those IDs are still **not** `T-*`: the driver is not a §4.7 stub, has no row in the ledger below, and flips nothing. The driver's `snapshot` render gained the per-factory group, `incomePerTurn` and the guided mark **because its own comment claimed to render the view model and had stopped doing so** once the snapshot widened. **The `stateHash` in `cpp_reference/Driver.h` and `cpp_reference/Driver.good.cpp` is the driver's own debug digest**, gated by `GATE-DRV-06`, and is a different thing from §4.10's canonical state hash, which is **not implemented at this commit**: row 10 holds no code. **How this commit was authored differs from every row above it and is not reported in their words.** The **Director** wrote the code, in the main session; it was **not** authored by an agent crew and it is not the two-pass agent pipeline that produced the earlier rows. The pass-1/pass-2 split was performed **by hand**: `cpp_reference/Ui.buggy.cpp` was rebased on the finished `Ui.good.cpp` and the two original row-8 defects re-injected, rather than preserved in place from `7c36303`.

---

### Pair 6 — §3 ledger, the UI row's evidence cell

Replacement of the whole table row. The Author and Agent-verified cells are
reproduced unchanged: the row does not flip, and its Author value is filed as a
change request below rather than edited here.

**OLD**

| UI | agent | — | **Partial pass — not a flip.** `cpp_reference/Ui.good.cpp` + `cpp_reference/test_ui.cpp` @ [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) · T-UI-01 and T-UI-02 (2/2) headless, plus `GATE-CAP-PARTIAL`, which mints no acceptance ID and which ran on a fixture configured with `captureTurns = 2` — a state the shipped N = 1 scenario cannot reach. **T-UI-03, T-UI-04 and T-UI-05 have not run**: T-UI-03 and T-UI-04 are in-editor Unreal Automation over widget bindings and no in-editor pass exists at this commit; **T-UI-05** was minted 2026-08-04, after this commit, is headless, and no code implements it. The acceptance set is incomplete on both counts and Q29, read per ID, keeps the row unverified |

**NEW:**

| UI | agent | — | **Partial pass — not a flip.** `cpp_reference/Ui.good.cpp` + `cpp_reference/test_ui.cpp` @ [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) · T-UI-01, T-UI-02 and T-UI-05 (3/3) headless — the runner prints **34** PASS lines, which count checks and not IDs — plus `GATE-CAP-PARTIAL`, which mints no acceptance ID and which ran on a fixture configured with `captureTurns = 2`, a state the shipped N = 1 scenario cannot reach. T-UI-01 and T-UI-02 first closed at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303); `41a1452` is the commit at which **T-UI-05** closes, the snapshot additions ruled beside it having been built there. **T-UI-03 and T-UI-04 have not run**: they are in-editor Unreal Automation over widget bindings and no in-editor pass exists at either commit. The acceptance set is incomplete on that count and Q29, read per ID, keeps the row unverified |

---

### Pair 7 — §3, the uncovered-ID enumeration

Replacement. `T-UI-05` leaves the *written and not green* state, so both the
set's total and that sub-total move, and the clause that made row 8's flip
independent of the editor pass goes with it.

**OLD**

Nine IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Seven are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set; **T-UI-03** and **T-UI-04**, written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at row 8's commit; and **T-UI-05**, written, unblocked and asserting, headless, minted 2026-08-04 and implemented by no code — it waits on neither a harness nor a rule but on an implementation.

**NEW:**

Eight IDs are still recorded as **uncovered** rather than omitted, in **two states that are not the same state**. Two are **unwritten**: **T-MOVE-07**, reserved on Q2, and **T-SCN-10**, reserved on Q26 — no invariant text exists for either, so neither asserts and neither is waiting on a run. Six are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**, **T-SCN-09** and **T-SCN-11**, each written, unblocked and asserting, each having run only part of its fixture set; and **T-UI-03** and **T-UI-04**, written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at either of row 8's two commits — those two wait on a harness, and they are now the whole of what row 8 lacks.

---

### Pair 8 — §3, why the UI row carries evidence without a ✓

Replacement. The reason narrows to the in-editor pass alone, and the row's
evidence commit moves with Pair 6.

**OLD**

and T-UI-03, T-UI-04 and T-UI-05 are why **UI** does the same at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) — the first two for want of an in-editor pass, the third because no code implements it.

**NEW:**

and T-UI-03 and T-UI-04 are why **UI** does the same at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), for want of an in-editor pass at that commit and at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) before it.

---

### Pair 9 — §4.4, week 3

Replacement. The cell scheduled `T-UI-05` in the future tense. It is green
before the week it was scheduled in.

**OLD**

**T-UI-05 is scheduled here too** (ruled 2026-08-04), and not as one of those re-runs: it is headless, and it asserts over the per-factory build record, which `Build` reaches and which rows 4–5 supply — the piece landing in the week the thing that consumes it runs, the principle stated below this table.

**NEW:**

**T-UI-05 was scheduled here too** (ruled 2026-08-04), and not as one of those re-runs: it is headless, and it asserts over the per-factory build record, which `Build` reaches and which rows 4–5 supply — the piece landing in the week the thing that consumes it runs, the principle stated below this table. It is **green at `41a1452`** (§3), so it is ahead of this cell rather than behind it; the rows that supply what it asserts over had already landed.

---

### Pair 10 — §4.5, the `T-UI-05` clause of the risk row

Replacement. The ID no longer widens the specification-versus-build gap.

**OLD**

`T-UI-05`, minted 2026-08-04 into Spec Stub 8 for the snapshot-fidelity check row 8's landing left ungated, is **implemented by no code** and **widens this gap by one** — the two movements are counted separately and the second is not absorbed by the first.

**NEW:**

`T-UI-05`, minted 2026-08-04 into Spec Stub 8 for the snapshot-fidelity check row 8's landing left ungated, is **green at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452)**, the commit at which the snapshot additions ruled beside it were built and it was implemented — it widened this gap by one when it was written and closed it again there, and those two movements are counted separately rather than netted, as `T-TURN-10`'s were.

---

### Pair 11 — §4.5, the green total

Replacement. Head of the tally only; the per-commit list is edited by Pair 12.

**OLD**

**52** of the 71 are green

**NEW:**

**53** of the 71 are green

---

### Pair 12 — §4.5, the per-commit green list

Replacement. Adds the `41a1452` term. The written total is unchanged and the
sentence's closing clause is reproduced unchanged.

**OLD**

and **2** at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where T-UI-01 and T-UI-02 closed without closing row 8 — so every row on the critical path has now landed

**NEW:**

**2** at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303), where T-UI-01 and T-UI-02 closed without closing row 8, and **1** at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452), where T-UI-05 closed without closing it either — so every row on the critical path has now landed

---

### Pair 13 — §4.5, the unclosed total

Replacement. Head of the list only; the list body is edited by Pair 14.

**OLD**

**19 IDs remain unclosed**: T-DATA-05

**NEW:**

**18 IDs remain unclosed**: T-DATA-05

---

### Pair 14 — §4.5, the unclosed list body

Replacement. Removes `T-UI-05` from the list. **Blast radius:** the clause *so
row 8 stays unflipped on it whatever the editor pass does* quantified over the
row's non-editor remainder, which is now empty, so it is replaced rather than
kept.

**OLD**

T-UI-03 and T-UI-04, which are written, unblocked and asserting, and for which no in-editor pass exists at row 8's commit; T-UI-05, which is written, unblocked, asserting and headless, and which no code implements — so row 8 stays unflipped on it whatever the editor pass does; and the **12** in rows 9–10, which hold no code

**NEW:**

T-UI-03 and T-UI-04, which are written, unblocked and asserting, and for which no in-editor pass exists at either of row 8's two commits — they are now the whole of what row 8 lacks, so its flip waits on the editor pass alone; and the **12** in rows 9–10, which hold no code

---

### Pair 15 — §4.7 Spec Stub 8, the Acceptance block

Replacement inside the fenced stub. The OLD span is four master lines and
carries the block's nine-space continuation indent; the NEW keeps both.

**OLD**

T-UI-05 was minted 2026-08-04 and NO
         CODE IMPLEMENTS IT: it is written, unblocked and asserting, and it
         is not green — four states this document keeps distinct. Nothing in
         the snapshot additions ruled with it is implemented either.

**NEW:**

T-UI-05 was minted 2026-08-04 and is
         GREEN at `41a1452`, where the snapshot additions ruled with it —
         `isGuidedMarked`, the per-factory group and `incomePerTurn` — were
         built and it was implemented and gated, 34/34 under clang++ and
         MSVC both. The presentation block is declared there and
         deliberately NOT FILLED: both its members have owners that are not
         the rules module, so no rules-side code fills them, and this
         invariant's subject does not reach them.

---

### Pair 16 — §4.11, the build-order lead-in

Replacement. **Blast radius:** the clause *so the editor pass is not the whole
of what this row still lacks* is exactly the sentence this round falsifies. The
OLD span is two master lines, broken after `after that`; the NEW is wrapped at
the width the surrounding paragraph uses.

**OLD**

and **T-UI-05 is headless and unimplemented** — minted 2026-08-04, after that
commit, so the editor pass is not the whole of what this row still lacks.

**NEW:**

and **T-UI-05 was then headless and unimplemented** — minted 2026-08-04,
after that commit. **T-UI-05 is green at `41a1452`** (§3), the rebuild at
which the snapshot additions ruled beside it were built, so the in-editor
pass is now the whole of what this row still lacks and the row stays
unflipped on it.

---

## Arithmetic

Every figure below is either from the fact block or from the master, and the
source is named.

| Figure | Before | After | Source | Check |
|---|---|---|---|---|
| §4.5 written acceptance IDs | 71 | 71 | fact block; master §4.5 | no ID minted at `41a1452` |
| §4.5 green | 52 | 53 | fact block; master §4.5 | 18 + 9 + 9 + 6 + 7 + 1 + 2 + 1 = 53 |
| §4.5 unclosed | 19 | 18 | fact block; master §4.5 | 1 (T-DATA-05) + 3 (T-SCN-08/09/11) + 2 (T-UI-03/04) + 12 (rows 9–10) = 18; and 53 + 18 = 71 |
| §3 uncovered IDs, rows 1–8 | 9 | 8 | master §3 | 2 unwritten + 6 written-and-not-green = 8 |
| §3 written-and-not-green, rows 1–8 | 7 | 6 | master §3 | 6 + the 12 in rows 9–10 = 18, the unclosed figure above |
| §3 unwritten (T-MOVE-07, T-SCN-10) | 2 | 2 | master §3 | unmoved: neither is a `T-UI-` ID |
| §3 verified ledger rows | 9 | 9 | fact block; master §3 | row 8 does not flip |
| §3 rows carrying evidence without a ✓ | 3 | 3 | master §3 | rows 2, 7 and 8, unchanged |
| `test_ui` | 14/14 @ `7c36303` | 34/34 @ `41a1452` | fact block | pass-1 21/34; 34 − 21 = 13 FAIL lines |
| `test_driver` | 12/12 @ `7c36303` | 12/12 @ `41a1452` | fact block | pass-1 11/12; 12 − 11 = 1 FAIL, `GATE-DRV-12` |
| `GATE-DRV` ID range | 01..12 | 01..12 | fact block; master §3 | `GATE-DRV-12` extended, not added |
| Stub 8 field contract | — | 27 = 22 + 5 | fact block | per-hex 2 + per-unit 11 + per-factory 5 + per-side 5 + match 4 = 27; the DECLARED DERIVED marks are `isGuidedMarked`, `spawnBlocked`, `objectivesHeld`, `survivingHP`, `incomePerTurn` = 5; 27 − 5 = 22 |
| `test_ui` output lines cited in Pair 5 | — | 76, 82, 101 | fact block (appended measurement) | the two `NOT RUN` lines precede the tally: 76 < 101 and 82 < 101 |

## Checks

- Every `T-UI-05` occurrence in the master was swept. It appears in §3's status
  paragraph, §3's ledger UI row, §3's uncovered-ID paragraph, §4.4's week-3
  cell, §4.5's risk row, §4.7 Stub 8, §4.11's lead-in and §4.11's † bullet.
  Every occurrence that states a build status is paired above. Left unpaired:
  Stub 8's *T-UI-05 asserts both*, its clause-(b) derivation note, its
  invariant text, its `Acceptance: T-UI-01..02 and T-UI-05 headless` line,
  §4.11's † bullet, and §4.5's *the presentation block and the snapshot fields
  ruled beside T-UI-05 on the same day, which mint no ID at all* — that one
  states a minting rather than a build status, and it is unmoved because
  `41a1452` mints no acceptance ID either.
- Each OLD span was checked twice: for a unique match with `rg -o` over the
  master, and for line breaks against the master's own bytes. Pairs 1–14 are
  copied out of five unwrapped master lines and contain no break. One candidate
  span, `no in-editor pass exists at row 8's commit`, matches twice — in §3 and
  in §4.5 — so Pairs 7 and 14 each widen past it into text that differs between
  the two sites.
- Checked and left unchanged, with the reason. §4.11's build-order table row 8
  reads `| 8 | UI binding (Stub 8) | 5, 7 (snapshot needs full state) |
  Contract + queries yes; widgets in-editor | T-UI-01..05 (**T-UI-03, 04 †**) +
  GATE-CAP-PARTIAL |`, and the acceptance set, the dependency set and the †
  membership are all unmoved. §4.11's † bullet for T-UI-03/04 likewise states
  which side of the cut line each ID sits on, not whether any is green.
- Checked and left unchanged: §4.10's *Row 10 holds no code and no save file
  exists*, and §4.10's `scenarioHash` header sentence. The fact block states
  §4.10's canonical state hash is not implemented at `41a1452`; the digest that
  does exist is the driver's.
- Checked and left unchanged: §4.7 Stub 8's clause (b); its text is not edited
  by any pair above.
- §2 was swept for gate-status vocabulary and none was found, so no §2 pair is
  written. §2.11.5's per-factory-block reference and §2.11.1's DONE-bit
  passages name fields and owners, not statuses.
- The `*pending*` occurrences — row 4 of §1.6's revision-notes table, §4.7's
  heading, §4.10 and §4.11's lead-in — are dated or historical and none is
  falsified. No pair above flips row 8's ledger row.

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §3 ledger, UI row, **Author** cell | `agent` | `agent+human`, or a per-commit split stated in the evidence cell | The ledger's own rule is *Author = human for anything a human hand-wrote or substantially edited*, and Pair 5 records who wrote the code at `41a1452`. I did not edit the cell — whether "the main session" counts as human under that rule is the Director's call, and Pair 6 reports the authorship without pre-empting it. |
| §4.10, the state-hash omission clause | "§4.7 Stub 8's `spawnBlocked` is that case, being a function of the unit positions this hash carries and the terrain the scenario file fixes" | Either narrow §4.10's parenthetical to occupancy, or widen §4.7 Stub 8's derivation to include passability and re-gate it | The two sections describe one field differently, and Pair 5 records which reading the shipped code follows and why the discrepancy is document-side rather than a gate failure. Registered rather than acted on, on the row-7 precedent: no invariant text changed and no acceptance ID minted. |
| §4.7's open-question register | Q32 is the highest registered row | If the `spawnBlocked` discrepancy should be carried as a numbered row rather than as the change request above, mint it | Minting a Q number touches the register's provenance chain, its preamble and its authoritative table at once. That is the Director's edit, not mine. |

## Open questions for the Director

1. **Does `41a1452` re-open §4.4's "Playable via debug commands"?** The amended
   ruling re-opens the goal on each system that lands after it and on a rebuild
   of an already-landed row **that changes what a human can reach at the REPL**.
   Whether the widened `snapshot` render and the new `DriverUnit` field that
   Pair 5 records change what a human can *reach* is a judgement the ruling
   does not settle. No pair above touches the goal.
2. **Should the clause-(b) self-passing episode become a stated convention?**
   Whether *a DECLARED DERIVED recomputation may not call the helpers the
   projection calls* becomes a §4.7 convention is a rule, and rules are the
   Director's.
3. **Does the UI row's Author cell change?** Filed as a change request above; it
   needs a ruling before any pair can touch it.

## Grounding

- Commit `41a1452` and its parent, the changed file list, the `test_ui` and
  `test_driver` tallies and their pass-1 tallies, the unchanged harnesses, the
  absence of `g++`, `T-UI-03` and `T-UI-04` not running, no acceptance ID
  minted, §4.10's hash not implemented and the driver's own digest under
  `GATE-DRV-06`, `spawnBlocked` on occupancy alone, the declared-and-unfilled
  presentation block, `DriverUnit`'s `placement` field, the field contract, the
  hand-performed pass-1/pass-2 split, the rewritten clause-(b) implementation,
  the `GATE-DRV-12` extension and its measurement, the `snapshot` render's
  motive, and this round's arithmetic movements — Director-supplied fact block,
  this session.
- The `NOT RUN` lines and the tally line measured in `test_ui` at `41a1452`,
  what each `NOT RUN` line states, and the extent of that measurement —
  Director-supplied fact block, appended measurement, this session.
- Row 8's landing record, the ledger table and its UI row, the uncovered-ID
  enumeration, the Author rule, and the citation convention — `source/gdd.md`
  §3.
- Week 3's `T-UI-05` line — `source/gdd.md` §4.4.
- The written / green / unclosed tallies and the risk row's wording —
  `source/gdd.md` §4.5.
- Spec Stub 8's snapshot groups, its DECLARED DERIVED marks, clause (b),
  `spawnBlocked`'s stated derivation, the presentation block's two members and
  their owners, and the Acceptance block — `source/gdd.md` §4.7.
- §4.10's state-hash omission clause and *Row 10 holds no code* —
  `source/gdd.md` §4.10.
- The build-order table, its row 8 and the † bullets — `source/gdd.md` §4.11.
- Q29's per-acceptance-ID reading and the Q register's extent rule —
  `source/gdd.md` §4.7 open-question register.
- The `*pending*` occurrence in row 4 of the revision-notes table —
  `source/gdd.md` §1.6.
- Master identity: `source/MANIFEST.txt`,
  `gdd.md md5=5075d853166d99858fd3a5a4b7dfc27c`.
