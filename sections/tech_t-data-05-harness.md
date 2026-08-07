# Technical design — t-data-05-harness addendum (tech-director)

## Placement

Addendum of exact OLD → NEW pairs against `source/gdd.md`. Sites are in §3, §4.4,
§4.5, §4.7, §4.8, §4.9 and §4.11. No section is redrafted.

---

## Pairs

### §3 — status line

**Pair 1**

OLD

```
This draft stands at 2026-08-05, at commit [`031ee20`](https://github.com/jakemartin/stratocracy-crew/commit/031ee20) in the crew repo and at `a13626f` in the Stratocracy UE project repo.
```

NEW

```
This draft stands at 2026-08-06, at commit [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) in the crew repo and at `fed8ae9` in the Stratocracy UE project repo.
```

*Note.* The pair the draft stands at moves with this landing; the ancestry
sentences that follow are measured against `031ee20` and `a13626f` and stand as
the measurements they were.

**Pair 2**

OLD

```
`031ee20` and `a13626f` are cited as commits, and this line makes no claim about how either stands to any branch.
```

NEW

```
`c2edae0` and `fed8ae9` are cited as commits, and this line makes no claim about how either stands to any branch.
```

*Note.* The disclaimer names the current pair; the defect this line records
about head claims is why it is re-pointed rather than upgraded.

**Pair 3**

OLD

```
**How `031ee20` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

NEW

```
**How `031ee20` was authored is deliberately not stated:** no harness claim is made for it, because none was established. **The in-editor Automation harness then landed**, at [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) in the crew repo — over [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992), which vendors the §4.8 CSVs into the UE project — with the Stratocracy UE project repo at `fed8ae9`. New in the UE project: `EUnitType`, a `UENUM` mirroring `strat::UnitType` with the enumerator order pinned; the row structs `FUnitRow`, `FTerrainRow` and `FEffectivenessRow`, each deriving `FTableRowBase`; an `ImportStratData` commandlet that imports the vendored CSVs into `DT_Units` (4 rows), `DT_Terrain` (7 rows) and `DT_Effectiveness` (4 rows); and an in-editor Unreal Automation suite. **All of it lives in the `Stratocracy` module and none of it in `Source/StratRules/`**, which is the constraint §4.9 states: `T-INT-01` accounts for every file in that directory, so a test file placed there would fail a green ID. The gate is **`T-DATA-05`, 4/4, plus `GATE-DATA-VENDOR`, 5/5 in-editor** at `fed8ae9`, and **`T-DATA-01..04, 06` plus `GATE-DATA-HARDFAIL`, 6/6 headless** at [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0), where `python run.py --week1` prints **WEEK-1 GATE PASS** with every row at its full tally and **INTEGRATION GATE PASS 2/2**, under MSVC. **`GATE-DATA-VENDOR` and `GATE-DATA-HARDFAIL` mint no acceptance ID**, on the `GATE-AI-SMOKE`, `GATE-SCN-PARSE`, `GATE-CAP-PARTIAL`, `GATE-SAVE-PARSE`, `GATE-REPLAY-*` and `GATE-BALANCE-*` precedent. **The §4.8 CSVs are vendored, and their bytes are asserted rather than assumed:** they are copied from the crew object store into the UE project beside a manifest recording each file's sha256 and the crew commit it came from, and `GATE-DATA-VENDOR` asserts the bytes on disk are the recorded ones. That is what makes the two halves of row 2's acceptance set halves of one thing — the headless loader and the editor import read the same authored bytes. **Row 2 flips.** Its full acceptance set passes: the headless half at [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) and `T-DATA-05` over the UE tree at `fed8ae9`. Q29's *at one commit* is read across a repo **pair**, in the two-repo pinning form this ledger already uses for `T-INT-01`, registered as **Q34** (§4.7) and written already marked RULED. What answers Q29's concern on its own terms: no fixture went unrun, and `GATE-DATA-VENDOR` establishes that both halves ran against the same data bytes. **The headless IDs' greens do not move:** `T-DATA-01..04` and `06` stay credited at [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825), their run at `b1ea992` being a re-run on the precedent that a re-run is not a re-recording; what `b1ea992` supplies is the crew half of the pair the flip is cited against. **No acceptance ID was minted and none was re-dated**, so §4.5's written-ID count does not move at this landing, its green count moves **61 → 62** on `T-DATA-05`'s closure at `fed8ae9`, and its unclosed count moves **10 → 9**. **No ledger row other than row 2 changes state.** **The suite was proven able to FAIL on six known-bad inputs, each caught by the intended check and only that check**: a perturbed CSV value (parity and vendor both); a corrupted manifest hash (vendor only); an unrecorded file in the data directory (vendor only); a DataTable asset drifted from the CSV (parity only); a fifth enumerator (the runtime mirror check); and swapped enumerator values, which stop the build at a `static_assert`. **A defect in the previous round's registration was found by launching the editor, and is recorded rather than repaired quietly.** `Source/StratRules/` contains no `IMPLEMENT_MODULE`, so with `StratRules` listed in `Stratocracy.uproject`'s Modules array the editor aborted at startup with *"The game module 'StratRules' could not be successfully initialized"* and exited: at `a13626f` nothing in-editor could run — not a commandlet, not an Automation test, not the editor. The round that registered it gated that the module compiles and links, and never launched the editor. `StratRules` is **removed from the Modules array at `fed8ae9`** and remains a **link dependency of the `Stratocracy` module**, still built by UBT and still linked. The removal touches no vendored byte, so `T-INT-01` and `T-INT-04` do not re-date: both remain green at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), and the running check reports all 22 files in `Source/StratRules/` accounted for. **§4.8's seven bool UStruct fields drop the `b` prefix** — `CanCapture`, `PassLand`, `PassAir`, `PassSea`, `Capturable`, `IsSpawnPoint`, `IsRepairPoint` — measured at engine source: `DataTableUtils::GetPropertyImportNames` accepts only `GetName()` and `GetAuthoredName()`, there is no metadata bridge, and `meta=(DisplayName=...)` was tried and failed identically. **The CSV column names and the headless field names are unchanged**, so one canonical CSV is still read by both sides with no transformation between them. **Stale claims in the crew repo were repaired at [`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0):** the gate runner, its test harnesses, two specs and the README asserted that no in-editor Automation harness exists, at thirteen sites in five spellings, and each site now names what its ID still lacks. The records above of the runner's printed output at [`b23823f`](https://github.com/jakemartin/stratocracy-crew/commit/b23823f) and [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) describe those commits and are unmoved by the repair. **What this landing does not close is stated so it is not inferred.** It closes no acceptance ID other than `T-DATA-05`. `T-INT-02` still needs a vendored replayer — its replay runs **in-engine**, and `Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03` still needs the command surface, which is part of the unbuilt bridge; `T-INT-05`, `T-UI-03` and `T-UI-04` still need real Stratocracy widgets; and `T-SAVE-06` is asserted jointly with `T-INT-02` and inherits that blocker. Build-order rows 9 and 10 therefore still do not close, and the ledger gains a row for neither. **How `b1ea992` and `c2edae0` were authored is deliberately not stated:** no harness claim is made for either, because none was established.*
```

*Note.* The landing record, in the form every landing above it uses; it is the
commit-pinned home for rulings AG, AH, AJ and AK.

### §3 — ledger table

**Pair 4**

OLD

```
| Data tables (units/terrain) | agent | — | **Partial pass — not a flip.** `cpp_reference/Data.good.cpp` + `cpp_reference/test_data.cpp` over `data/units.csv`, `data/terrain.csv`, `data/effectiveness.csv` @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825) · T-DATA-01..04, 06 (5/5) headless. **T-DATA-05 (in-editor) has not run**, so the acceptance set is incomplete at this commit and Q29 keeps the row unverified |
```

NEW

```
| **Data tables (units/terrain)** | agent | ✓ | `cpp_reference/Data.good.cpp` + `cpp_reference/test_data.cpp` over `data/units.csv`, `data/terrain.csv`, `data/effectiveness.csv` · T-DATA-01..04, 06 (5/5) headless @ [`c224825`](https://github.com/jakemartin/stratocracy-crew/commit/c224825), re-run green @ [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) · **T-DATA-05 (in-editor) 4/4** over the imported DataTables and the `EUnitType` mirror @ `fed8ae9` in the Stratocracy UE project repo, beside `GATE-DATA-VENDOR`, which mints no acceptance ID. The full set closes across that repo pair, which is how Q29's *at one commit* reads for a two-repo acceptance set (Q34) |
```

*Note.* The flip (AJ). The system name takes the bold the other ✓ rows carry.

### §3 — the paragraph beneath the table

**Pair 5**

OLD

```
Nine rows carry a ✓ in the table above, and three more carry evidence without one
```

NEW

```
Ten rows carry a ✓ in the table above, and two more carry evidence without one
```

*Note.* Row 2 moves from the second group to the first.

**Pair 6**

OLD

```
Eight IDs are still recorded as **uncovered** rather than omitted
```

NEW

```
**Data tables** joined at [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) with `fed8ae9` in the Stratocracy UE project repo — T-DATA-01..04 and 06 headless, **T-DATA-05 in the editor pass**, 4/4 — and it is the first row whose acceptance set closes across a **repo pair** rather than at a single commit, which is what Q34 rules on. Seven IDs are still recorded as **uncovered** rather than omitted
```

*Note.* The uncovered set loses `T-DATA-05`; the joining sentence follows the
form the rows above it use.

**Pair 7**

OLD

```
Six are **written and not green**: **T-DATA-05**, the in-editor Unreal Automation half, which has not run; **T-SCN-08**
```

NEW

```
Five are **written and not green**: **T-SCN-08**
```

*Note.* Same movement, stated in the second of the two states the sentence
separates.

**Pair 8**

OLD

```
among what those two wait on are a harness and real Stratocracy widgets
```

NEW

```
among what those two wait on are real Stratocracy widgets, the in-editor Automation harness they also lacked having landed at `fed8ae9`
```

*Note.* The harness half of that pair is discharged; the widget half is not.

**Pair 9**

OLD

```
T-DATA-05 is why **Data tables** carries evidence without a ✓ — T-DATA-01..04 and 06 are green at the same commit, but Q29 requires the full acceptance set at one commit, so that row records a partial pass and stays unverified — the three
```

NEW

```
T-DATA-05 was why **Data tables** carried evidence without a ✓; it has since run, 4/4 in the editor pass at `fed8ae9`, completing that row's acceptance set across the repo pair Q34 rules on, and that row now carries one. **Two rows still carry evidence without a ✓, each recording a partial pass and staying unverified on Q29:** the three
```

*Note.* Row 2's posture is rewritten by the flip, and the *carries evidence
without a ✓* predicate is kept live because the two *does the same* clauses that
follow refer back to it — without it they would read as saying Content /
scenario and UI now carry a ✓ too. The **two** matches pair 5.

### §4.4 — week 3 cell

**Pair 10**

OLD

```
`T-SAVE-06` did not close here: among what it waits on are the in-editor Automation harness and a vendored replayer, it being asserted jointly with `T-INT-02` (§4.9). `T-INT-02` did not close here either: among what it waits on are that harness and that replayer, `Replay` being ruled out of vendoring until a bridge consumer exists (§4.9).
```

NEW

```
`T-SAVE-06` did not close here: among what it waits on is a vendored replayer, it being asserted jointly with `T-INT-02` (§4.9). `T-INT-02` did not close here either: among what it waits on is that replayer, `Replay` being ruled out of vendoring until a bridge consumer exists (§4.9). The in-editor Automation harness both of them also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3), in no week this table names.
```

*Note.* The blocker record loses the half that landed and keeps the half that
did not.

### §4.4 — the note beneath the milestone table

**Pair 11**

OLD

```
**The in-editor Automation harness is deliberately not on this calendar (ruled 2026-08-06).** No cell above gives it a week — wk 3 names it among what `T-SAVE-06` and `T-INT-02` wait on, which is a blocker record rather than a goal cell — and §4.9 records it among what part 2 is blocked on and states that it is not scheduled there either.
```

NEW

```
**The in-editor Automation harness landed off this calendar (ruled 2026-08-06).** It landed at `fed8ae9` in the Stratocracy UE project repo (§3), and no cell above gives it a week — wk 3 records that landing beside the two IDs that had waited on it, which is a record rather than a goal cell — and §4.9 records the landing where it recorded the blocker.
```

*Note.* The paragraph's subject survives the landing; its head claim does not.

**Pair 12**

OLD

```
Both sections now decline it in the open, so the absence reads as a decision and not as an oversight. Among what stands between it and a cell: the harness by itself closes no acceptance ID (§4.9), so a week that added the runner and nothing else would close none, and the subjects the editor-pass IDs assert against besides it sit differently against this table.
```

NEW

```
Both sections declined it in the open, so the absence read as a decision and not as an oversight. What stood between it and a cell held at the landing: the harness by itself closes no acceptance ID (§4.9), and the landing closed `T-DATA-05` because it carried that ID's own subjects with it — the imported §4.8 DataTables and the `UENUM` mirror of the unit type — while the subjects the other editor-pass IDs assert against are unbuilt (§4.9).
```

*Note.* The reason the harness took no cell is preserved and dated, and the one
ID it closed is attributed to its subjects rather than to the runner.

**Pair 13**

OLD

```
When the harness does take a cell it takes it on the principle stated above: the week the thing that consumes it runs.
```

NEW

```
The harness took no cell and landed anyway, and so did the in-editor import step and the `UENUM` mirror named above, at `fed8ae9` (§3). The principle stated above — the week the thing that consumes it runs — now governs what is still uncelled beside them: the vendored replayer `T-INT-02` waits on, the command surface `T-INT-03` waits on, and the real Stratocracy widgets `T-INT-05`, `T-UI-03` and `T-UI-04` wait on (§4.9).
```

*Note.* The forward-looking sentence is spent; the principle is re-pointed at
what is still uncelled.

### §4.5 — the *Specification outruns the build* row

**Pair 14**

OLD

```
against **9** verified ledger rows
```

NEW

```
against **10** verified ledger rows
```

**Pair 15**

OLD

```
**61** of the 71 are green
```

NEW

```
**62** of the 71 are green
```

**Pair 16**

OLD

```
widenings (§3) — so every row on the critical path has now landed,
```

NEW

```
widenings (§3), and **1** at `fed8ae9` in the Stratocracy UE project repo, where `T-DATA-05` closed in the editor pass and completed row 2's acceptance set across the repo pair whose crew half is [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) (Q34; §3) — so every row on the critical path has now landed,
```

*Note.* The by-commit breakdown gains the entry the green count moves on.

**Pair 17**

OLD

```
**10 IDs remain unclosed**: T-DATA-05, which leaves row 2 unflipped; T-SCN-08,
```

NEW

```
**9 IDs remain unclosed**: T-SCN-08,
```

**Pair 18**

OLD

```
and among what its flip waits on are an in-editor Automation pass and the real Stratocracy widgets `T-UI-03` and `T-UI-04` assert against, which are measured absent at `a13626f` (§4.9); the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), and no in-editor Automation harness exists —
```

NEW

```
and among what its flip waits on are the real Stratocracy widgets `T-UI-03` and `T-UI-04` assert against, which are measured absent at `a13626f` (§4.9), the in-editor Automation pass those two also lacked having landed at `fed8ae9` (§3); the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), `T-INT-02` waiting on a vendored replayer, `T-INT-03` on the bridge's command surface and `T-INT-05` on those same widgets —
```

*Note.* Both clauses named the harness as an outstanding blocker; each now names
what its own IDs still lack.

**Pair 19**

OLD

```
leaving `T-SAVE-06`, among what it waits on being the in-editor Automation harness and a vendored replayer
```

NEW

```
leaving `T-SAVE-06`, among what it waits on being a vendored replayer
```

*Note.* The harness half of the same pair, at the row that states the unclosed
count.

**Pair 20**

OLD

```
Row 2 is now that clause's worked example rather than its hypothetical: its headless suite is green and its ledger row is not
```

NEW

```
Row 2 was that clause's worked example while its editor half was outstanding, and it has since flipped (§3). Row 7 is the clause's live example: three of its written IDs ran only part of their fixture sets, and its ledger row stands unflipped
```

*Note.* The clause needs a live example and row 2 has stopped being one.

### §4.7 — open-questions register

**Pair 21**

OLD

```
runs it, found while widening build-order row 9's integration check (Q33)
— so that each question
carries exactly one ID across the whole document.
```

NEW

```
runs it, found while widening build-order row 9's integration check (Q33), and
how Q29's *at one commit* reads for an acceptance set that spans two
repositories, found when row 2's editor half closed in the UE project repo (Q34)
— so that each question
carries exactly one ID across the whole document.
```

**Pair 22**

OLD

```
**Sixteen of the thirty-three rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and Q32 — each
```

NEW

```
**Seventeen of the thirty-four rows are ruled; the other
seventeen remain open but *readable*** — Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31
and Q32 — each
```

**Pair 23**

OLD

```
**Q33 is registered already marked RULED**, so it enters the ruled side and
the open list above is unchanged.
```

NEW

```
**Q33 and Q34 are registered already marked RULED**, so each enters the ruled side and
the open list above is unchanged.
```

**Pair 24**

OLD

```
the register carries it so the amendment above has a stated cause rather than an unexplained rewrite. |
```

NEW

```
the register carries it so the amendment above has a stated cause rather than an unexplained rewrite. |
| **Q34** | ~~How Q29's *at one commit* reads when an acceptance set spans two repositories.~~ **RULED (this revision), and registered already ruled.** Row 2's acceptance set is `T-DATA-01..04, 06` in the crew repo and `T-DATA-05` in the Stratocracy UE project repo, so no single commit in either repo can carry both halves and Q29's condition is unsatisfiable read literally. Read it across a **repo pair**, or leave every two-repo row permanently unflippable? | §3's row 2, and any later row whose acceptance set spans both repos — build-order rows 9 and 10 among them. No gate waits on the ruling: every ID runs either way, and neither answer mints an acceptance ID. | **Ruled: across a repo pair, in the two-repo pinning form this document already uses for `T-INT-01`** — one crew commit and one UE project commit, cited together. Row 2 flips on the pair [`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992) and `fed8ae9` (§3). What answers Q29's concern on its own terms is that no fixture went unrun, and that `GATE-DATA-VENDOR` establishes both halves ran against the same data bytes. The conservative reading Q29 states is preserved rather than loosened: a pair whose halves disagree about the data closes nothing. **Which IDs a §4.8 CSV edit re-opens is ruled with it:** such an edit re-opens the **whole** pair — `T-DATA-05` and the headless `T-DATA` IDs together — and the flip re-pins to a new pair when the re-run completes. That records the gates' existing behaviour rather than imposing new behaviour: perturbing `units.csv` without re-importing failed both the parity check, on `Infantry.HP` expected 11 and read 10, and `GATE-DATA-VENDOR`, on a sha256 mismatch, while the suite's other three tests stayed green (§3). Re-opening the headless half alone was the alternative, and it is refused for that reason — the bytes both halves read are one file, so a change to them is a change to both halves' subject. **That rules which IDs re-open and nothing about what this ledger shows in the interval** between the edit and the re-run; the pinned record is untouched either way, since *green at `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits, which is what pinning is for. It is registered already marked RULED because the Director ruled it in the session that found it. |
```

*Note.* AJ's extension of Q29, written already ruled on the Q33 precedent, and
AN's re-opening rule filed in the same row because it governs the same object —
the repo pair. AN is scoped to which IDs re-open; the interim display is not
ruled and is registered below. No register row is added by AN, so no §4.7 count
moves on it.

### §4.8 — data contract

**Pair 25**

OLD

```
Each table is one
canonical CSV in the repo (`data/`). The headless loader parses it directly; the
Unreal editor imports the same file into a `UDataTable` whose row struct derives
`FTableRowBase`.
```

NEW

```
Each table is one
canonical CSV, authored in the crew repo (`data/`). The headless loader parses it
directly; the UE project vendors it verbatim beside a manifest recording each
file's sha256 and the crew commit it came from, and the editor imports the
vendored copy into a `UDataTable` whose row struct derives `FTableRowBase`.
`GATE-DATA-VENDOR` asserts that the vendored bytes are the recorded ones, so the
two readers are reading one authored file rather than two that resemble each
other; it **mints no acceptance ID**, on the `GATE-AI-SMOKE` and
`GATE-SAVE-PARSE` precedent (§3). **The manifest's `dataCommit` names the commit
the vendored bytes came from, and it advances when and only when those bytes
change (ruled 2026-08-06).** A crew commit that does not touch the data
directory leaves it where it is, so a `dataCommit` behind the crew commit this
document stands at is the **expected** state and not a stale one: it records
[`b1ea992`](https://github.com/jakemartin/stratocracy-crew/commit/b1ea992), and
the three CSVs are byte-identical at that commit and at
[`c2edae0`](https://github.com/jakemartin/stratocracy-crew/commit/c2edae0) (§3).
`GATE-DATA-VENDOR` reads `dataCommit` and logs it; what it asserts is the file
hashes and not the commit's currency, because the UE project cannot see the crew
repo at test time — the same discipline that makes this document cite commits
rather than heads everywhere else.
```

*Note.* "Read twice" now spans two repos; the gate that keeps the two copies one
file is named where the principle is stated, and AM's `dataCommit` rule is
stated here once because this is where the vendoring is described. The lag is
named explicitly because it is the thing a reader mistakes for staleness.

**Pair 26**

OLD

```
Missing column or unparseable value = hard load failure, never a silent default.
```

NEW

```
Missing column or unparseable value = hard load failure, never a silent default.
**UStruct bool fields carry no `b` prefix, and that is an engine constraint
rather than a style choice (ruled 2026-08-06):** `DataTableUtils::GetPropertyImportNames`
accepts only `GetName()` and `GetAuthoredName()`, there is no metadata bridge,
and `meta=(DisplayName=...)` was tried and failed identically, so a `bCanCapture`
field cannot be fed by a `CanCapture` column. The CSV column names and the
headless field names are unchanged by that, so the transformation between the
two sides stays empty.
```

*Note.* AH's reason, stated once beside the schemas it governs.

**Pair 27**

OLD

```
| `CanCapture` | bool | `canCapture` | `bool bCanCapture` | §2.7 (Infantry only) |
```

NEW

```
| `CanCapture` | bool | `canCapture` | `bool CanCapture` | §2.7 (Infantry only) |
```

**Pair 28**

OLD

```
| `PassLand`/`PassAir`/`PassSea` | bool ×3 | `passLand/Air/Sea` | `bool bPassLand/Air/Sea` | §2.3 Passable column |
```

NEW

```
| `PassLand`/`PassAir`/`PassSea` | bool ×3 | `passLand/Air/Sea` | `bool PassLand/PassAir/PassSea` | §2.3 Passable column |
```

**Pair 29**

OLD

```
| `Capturable` | bool | `capturable` | `bool bCapturable` | §2.3 (Town, Factory) |
```

NEW

```
| `Capturable` | bool | `capturable` | `bool Capturable` | §2.3 (Town, Factory) |
```

**Pair 30**

OLD

```
| `IsSpawnPoint` | bool | `isSpawnPoint` | `bool bIsSpawnPoint` | §2.7 (Factory) |
```

NEW

```
| `IsSpawnPoint` | bool | `isSpawnPoint` | `bool IsSpawnPoint` | §2.7 (Factory) |
```

**Pair 31**

OLD

```
| `IsRepairPoint` | bool | `isRepairPoint` | `bool bIsRepairPoint` | §2.7 Repair (Town + Factory) |
```

NEW

```
| `IsRepairPoint` | bool | `isRepairPoint` | `bool IsRepairPoint` | §2.7 Repair (Town + Factory) |
```

*Note (pairs 27–31).* AH, the seven bool fields, one pair per schema row. The
UStruct column is the only one that moves.

### §4.9 — integration path

**Pair 32**

OLD

```
**The UBT module is registered, and it builds.** `Stratocracy.uproject` lists
`StratRules` at `a13626f`, and building the `StratocracyEditor` target compiles
the vendored crew modules and links `UnrealEditor-StratRules.dll` — sources UBT
had never compiled before (§3).
```

NEW

```
**The UBT module is built and linked, and it is not listed in the `.uproject`
(ruled 2026-08-06).** `Stratocracy.uproject` listed `StratRules` at `a13626f`,
and building the `StratocracyEditor` target compiled the vendored crew modules
and linked `UnrealEditor-StratRules.dll` — sources UBT had never compiled before
(§3). **Listing it made the editor unusable, and the entry was removed at
`fed8ae9`.** `Source/StratRules/` contains no `IMPLEMENT_MODULE`, so at
`a13626f` the editor aborted at startup with *"The game module 'StratRules'
could not be successfully initialized"* and exited: nothing in-editor could run
there — not a commandlet, not an Automation test, not the editor. The round that
registered it gated that the module compiles and links and never launched the
editor, which is the gap that let the defect through. `StratRules` is now a
**link dependency of the `Stratocracy` module** instead: UBT still builds it and
the game module still links it, and the removal touches no vendored byte, so
`T-INT-01` and `T-INT-04` do not re-date (§3).
```

*Note.* AG, at the paragraph that states the module's build status.

**Pair 33**

OLD

```
`T-INT-04` asserts the
**standalone** compile, outside UBT; in-engine compilation is what the editor
pass gates, and that pass does not exist.
```

NEW

```
`T-INT-04` asserts the
**standalone** compile, outside UBT; in-engine compilation is what the editor
pass gates, and that pass exists at `fed8ae9` (§3), where it runs `T-DATA-05`
and `GATE-DATA-VENDOR` and no in-engine parity check over the vendored module.
```

*Note.* The pass exists; what it does not yet carry is stated rather than left
to be read off its existence.

**Pair 34**

OLD

```
what part 2 waits on is not specification. It waits on **an in-editor
Automation harness**.
```

NEW

```
what part 2 waits on is not specification. The **in-editor Automation harness**
it waited on landed at `fed8ae9` in the Stratocracy UE project repo (§3), so
what part 2 waits on now is the bridge's own code — the load mapping, the
command surface, the event list, the actor and the widget.
```

**Pair 35**

OLD

```
The harness is recorded here among what part 2 is blocked on, and is not
scheduled here.
```

NEW

```
The harness was recorded here among what part 2 was blocked on, and it took no
week on §4.4's calendar; both blockers this paragraph named have since been
removed, and part 2 is blocked on its own unbuilt code.
```

*Note (pairs 34–35).* The harness blocker is discharged; the canonical state
hash blocker was already discharged in the sentence between them.

**Pair 36**

OLD

```
which lists what that stub draws on; the imported tables are not among the
DataTable assets measured above.
```

NEW

```
which lists what that stub draws on; the imported tables are not among the
DataTable assets measured above. **`T-DATA-05`'s two subjects have since been
built** (§3): at `fed8ae9` the `UENUM` mirror `EUnitType` and the imported
`DT_Units`, `DT_Terrain` and `DT_Effectiveness` exist, alongside `FUnitRow`,
`FTerrainRow` and `FEffectivenessRow` — all of them in the `Stratocracy` module
and none in `Source/StratRules/`, which is the constraint stated below. The
`a13626f` measurement above is unmoved by that, and it remains the live
statement about every other subject this passage names.
```

*Note.* The `a13626f` measurement is pinned and stands; the two subjects it
counted absent are recorded as built at the later commit, with where they live,
because §4.9's own constraint forbids that directory to the harness. Trimmed
from its earlier form: pair 44 now states that `T-DATA-05` has closed, so this
pair no longer says so a second time in the same paragraph.

**Pair 44**

OLD

```
The harness is **also not sufficient**, and among what the
remaining
editor-pass IDs need besides it are the subjects named here rather than left to
be discovered at the pass: `T-INT-02` needs a **vendored replayer**, and
`Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03`
needs the **command surface**, which is part of the unbuilt bridge; `T-INT-05`,
`T-UI-03` and `T-UI-04` need **real Stratocracy widgets**; `T-DATA-05` needs
**imported DataTables and a `UENUM` mirror of the unit type**; and `T-SAVE-06`
is asserted jointly with `T-INT-02`.
```

NEW

```
The harness is **also not sufficient**, and among what the
other
editor-pass IDs need besides it are the subjects named here rather than left to
be discovered at the pass: `T-INT-02` needs a **vendored replayer**, and
`Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03`
needs the **command surface**, which is part of the unbuilt bridge; `T-INT-05`,
`T-UI-03` and `T-UI-04` need **real Stratocracy widgets**; and `T-SAVE-06`
is asserted jointly with `T-INT-02`. `T-DATA-05` is not one of them, having
closed at `fed8ae9` (§3); what it needed was **imported DataTables and a
`UENUM` mirror of the unit type**, and those stay named here because the
measurement that follows quantifies over every subject this passage names.
```

*Note.* The list is an enumeration keyed on membership of *the editor-pass IDs
that remain*, and `T-DATA-05` leaving that set is what stales it — the same
correction pair 12 makes at its §4.4 counterpart, in the same word. `T-DATA-05`
moves out of the *needs* list without leaving the passage, because the pinned
`a13626f` measurement immediately after quantifies over "those subjects" and its
two named zero-counts, `EUnitType` and `UENUM`, are that ID's. This pair's site
is lines 2877–2885; pair 36's is 2893–2894, after the measurement, and the two
do not overlap.

### §4.11 — build order

**Pair 37**

OLD

```
when this table was written, of which **rows 1, 3, 4, 5 and 6 have since
flipped** (§3).
```

NEW

```
when this table was written, of which **rows 1, 2, 3, 4, 5 and 6 have since
flipped** (§3), row 2 last and across a repo pair (Q34).
```

**Pair 38**

OLD

```
**Row 9's acceptance set does not close**, on the Q29 reading rows 2, 7 and
8 stand on: `T-INT-02`, `T-INT-03` and `T-INT-05` did not run, no in-editor
Automation harness existing. **Row 2 is not green:** T-DATA-01..04 and 06
pass at `c224825` and T-DATA-05 has not run, which is exactly the flip cost its †
bullet below already priced — reached by the ordinary schedule, since the editor
pass is not yet due, and not by the cut line firing.
```

NEW

```
**Row 9's acceptance set does not close**, on the Q29 reading rows 7 and
8 stand on: `T-INT-02`, `T-INT-03` and `T-INT-05` did not run, and among what
they wait on besides the harness that has since landed are a vendored replayer,
the bridge's command surface and real Stratocracy widgets, one per ID (§4.9).
**Row 2 is green:** T-DATA-01..04 and 06 pass headless and T-DATA-05 passed
4/4 in the editor pass at `fed8ae9`, so the full set closes across the repo
pair Q34 rules on and the ledger row flips (§3). Its † bullet below priced that
flip as the cost of losing the pass; the pass ran, so the mark can no longer
fire.
```

*Note.* Both sentences explained a non-flip that has since flipped; row 9's
posture no longer has row 2 beside it.

**Pair 39**

OLD

```
- **T-DATA-05** — row 2's only in-editor half. Fallback is a Director read of
  two frozen tables (4 unit rows × 11 columns, 7 terrain rows × 10). Cost: row
  2's ledger flip, since Q29 requires the full acceptance set at one commit.
```

NEW

```
- **T-DATA-05** — row 2's only in-editor half, and **closed**, 4/4 at `fed8ae9`
  in the Stratocracy UE project repo (§3), so the mark prices nothing the
  calendar can still take. What it priced while it stood: the fallback was a
  Director read of two frozen tables (4 unit rows × 11 columns, 7 terrain rows
  × 10), and the cost was row 2's ledger flip. **The mark is kept (ruled
  2026-08-06):** a closed ID keeps its †, and no rule about marks in general is
  minted by that — what a mark costs is a claim and never a rule, as the head of
  this list says.
```

*Note.* The bullet's price is spent and the mark stays, on the ruling recorded
in the NEW; the fallback is kept in past tense because it is what the mark
bought while it stood.

**Pair 40**

OLD

```
and among what the row's flip
waits on are an in-editor Automation pass and the real Stratocracy widgets
those IDs assert against (§3), the row staying unflipped on them.
```

NEW

```
and among what the row's flip
waits on are the real Stratocracy widgets those IDs assert against, which are
measured absent at `a13626f` (§4.9) — the in-editor Automation pass those two
also lacked landed at `fed8ae9` (§3) — the row staying unflipped on the widgets.
```

*Note.* Row 8's posture, on the same reading pairs 8, 10 and 18 use. The trailing
"unflipped on them" named the two things the flip waited on; with one of them
discharged it names the widgets.

**Pair 41**

OLD

```
**`T-SAVE-06` is now the only ID this row lacks**, and among what that ID waits on are the in-editor Automation harness and a vendored replayer: `T-SAVE-06` is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, so the replayer has to be compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists.
```

NEW

```
**`T-SAVE-06` is now the only ID this row lacks**, and among what that ID waits on is a vendored replayer: `T-SAVE-06` is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, so the replayer has to be compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists. The in-editor Automation harness this ID also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3).
```

*Note.* Row 10's live blocker clause. The sentence after it — that §4.9 states
both what the editor pass denotes and what running it does not supply — points
at §4.9 rather than at the two blockers, and stands.

**Pair 42**

OLD

```
Cost: row 7's ledger flip, on the same
  Q29 reading as row 2.
```

NEW

```
Cost: row 7's ledger flip, on the
  Q29 reading applied per acceptance ID as well as per row — an ID closes only
  when its whole written fixture set has run.
```

*Note.* Stranded by pairs 38 and 39: row 2 no longer stands on that reading and
its own † bullet no longer states it, so the cross-reference is replaced by the
reading itself, in the words §3 uses for row 7's own landing.

**Pair 43**

OLD

```
and unlike rows 2 and 3 it leaves **no ID uncovered**: it has no in-editor half and no reserved ID,
```

NEW

```
and it leaves **no ID uncovered**: unlike row 2 it has no in-editor half, and unlike row 3 no reserved ID,
```

*Note.* Stranded by pair 6: `T-DATA-05` was row 2's only uncovered ID, so the
comparison as drawn is false after the merge. The structural difference is what
survives — row 2 has an in-editor half and row 3 a reserved ID — and it is what
the clause's own explanation already turned on. This is a §3 site; it is filed
here beside the other two the same sweep found.

---

## Arithmetic

| Figure | Site | Old | New | Cause |
|---|---|---|---|---|
| Rows carrying ✓ | §3 (pair 5) | 9 | 10 | Row 2 flips |
| Rows carrying evidence without ✓ | §3 (pairs 5, 9) | 3 | 2 | Row 2 flips |
| Uncovered IDs | §3 (pair 6) | 8 | 7 | `T-DATA-05` closes |
| Written-and-not-green IDs | §3 (pair 7) | 6 | 5 | `T-DATA-05` closes |
| Verified ledger rows | §4.5 (pair 14) | 9 | 10 | Row 2 flips |
| Green acceptance IDs | §4.5 (pair 15) | 61 | 62 | `T-DATA-05` closes at `fed8ae9` |
| Unclosed acceptance IDs | §4.5 (pair 17) | 10 | 9 | `T-DATA-05` closes |
| Register rows | §4.7 (pair 22) | 33 | 34 | Q34 registered |
| Register rows ruled | §4.7 (pair 22) | 16 | 17 | Q34 registered already ruled |
| Register rows open | §4.7 (pair 22) | 17 | 17 | Q34 enters the ruled side |
| Flipped build-order rows | §4.11 (pair 37) | 5 | 6 | Row 2 flips |

Written acceptance IDs stay at **71**: no ID was minted at this landing.
No ID's green re-dates: `T-DATA-01..04` and `06` stay credited at `c224825`,
and `T-INT-01` and `T-INT-04` stay credited at `e19605e`.
**Rulings AL, AM and AN move no figure in this table.** AL mints no rule about
marks and changes no † membership; AM states a manifest field's advance
condition; AN is filed inside the existing Q34 row, so no register row is added
and §4.7's counts stand as pair 22 leaves them.

---

## Check results

- **In-editor at `fed8ae9`:** `T-DATA-05` 4/4 plus `GATE-DATA-VENDOR` — **5/5**.
- **Headless at crew `c2edae0`:** `T-DATA-01..04, 06` plus `GATE-DATA-HARDFAIL` —
  **6/6**. `python run.py --week1` prints **WEEK-1 GATE PASS** with every row at
  its full tally and **INTEGRATION GATE PASS 2/2**, under MSVC.
- **`T-INT-01` and `T-INT-04`:** green at `e19605e`, the running check reporting
  all 22 files in `Source/StratRules/` accounted for. No vendored byte moved
  this round.
- **Fail-proving:** six known-bad inputs, each caught by the intended check and
  only that check — a perturbed CSV value (parity and vendor), a corrupted
  manifest hash (vendor), an unrecorded file in the data directory (vendor), an
  asset drifted from the CSV (parity), a fifth enumerator (runtime mirror), and
  swapped enumerator values (build stops at a `static_assert`). The first of
  those is the control Ruling AN rests on: `Infantry.HP` expected 11 and read
  10, and a sha256 mismatch, with the suite's other three tests green.
- **`dataCommit` lag:** the CSV manifest records `b1ea992`; the three CSVs are
  byte-identical at `b1ea992` and `c2edae0`, so the lag is the expected state
  under Ruling AM and nothing in the document is false on its account today.
- **Pair inventory:** **44** pairs, numbered 1–44 with none absent and none
  duplicated. Three are insertions whose OLD survives inside their NEW — pairs
  24, 26 and 36. Pair 44 sits between 36 and 37 in file order, which is out of
  numeric sequence and deliberate: it belongs to the §4.9 group. Pairs 44 and 36
  edit §4.9's *no further spec-stub pass* paragraph at disjoint sites, 2877–2885
  and 2893–2894, either side of the pinned `a13626f` measurement.
- **OLD strings:** every OLD above was matched against `source/gdd.md`, and each
  returned exactly one match. Rulings AL, AM and AN are recorded by amending the
  NEW of pairs 39, 25 and 24; no OLD moved and no pair was added or removed.
- **§4.11 sweep for live "an editor pass is still awaited" claims**, by meaning:
  every §4.11 site naming a harness, an editor pass, an in-editor pass or
  Automation was read and decided on whether a commit pin encloses it. Paired:
  the row-8 posture clause (pair 40), the row-9/row-2 sentence (pair 38), and
  row 10's *only ID this row lacks* clause (pair 41). Left standing as pinned:
  row 8's *no in-editor pass exists at that commit*, which names `7c36303`, and
  row 10's *`T-SAVE-06` waits on the in-editor Automation harness and
  `T-SAVE-07` on a self-play log*, which sits inside the part-(b) landing record
  at `ec15be6` — the document already lets that sentence's `T-SAVE-07` half
  stand against the later part-(c) closure recorded in the same cell, which is
  the reading applied here. Left standing as unaffected: the four table cells
  naming where a gate runs (rows 2, 7, 8, 9), the † bullets for `T-UI-03, 04`
  and `T-INT-02, 05 and T-SAVE-06`, which state coverage class and mark cost,
  and the † rule sentences about an editor pass cut to its marked IDs.
- **Dependant-sentence sweep, run per pair over the whole list, and what its
  reach now covers.** The question asked per pair is which other sentence
  depends on the clause that pair changes. Its first reach was adjacency and
  shared vocabulary — a back-reference, a cross-reference, a comparison, or a
  tally — and on that reach it found three: the *does the same* back-references
  after pair 9 (repaired inside pair 9), the † list's `T-SCN-08, 09, 11`
  cross-reference to row 2's Q29 reading (pair 42), and row 4's comparison
  against row 2's uncovered ID (pair 43). **It now also covers enumerations and
  lists keyed on membership of a set this landing changes** — *the remaining X*,
  *among what X still need*, *the only X*, *nothing else is X* — at any distance
  from the pair that changes the membership, which is the reach the §4.9
  editor-pass list needed and did not get (pair 44). On the widened reach the
  membership-keyed sites are: §4.9's *the remaining editor-pass IDs* (pair 44);
  §3's uncovered and written-and-not-green sets (pairs 6, 7) and its ✓ tally
  (pair 5); §4.5's unclosed set and its per-row remainders (pairs 17, 18, 19);
  §4.11's flipped-row list (pair 37) and row 10's *only ID this row lacks*
  (pair 41). Cleared on the widened reach, with reasons: §4.7's cut-line
  partition and §4.11's *Unmarked is the default and the majority*, which key on
  an ID's coverage class and mark, neither of which a closure moves; §4.9's
  stub-`Inputs` line *what T-INT-03 and T-INT-05 still need is assigned per ID
  above*, whose referent survives pair 44 intact; §3's *`T-SAVE-06` is the only
  † of row 10's seven* and *remains the only †*, each inside a pinned landing
  record and about a set `T-DATA-05` does not enter; §1's *the remaining four
  weeks* and Q20's *the remaining three commands*, which enumerate weeks and
  commands; and §4.9's *Nothing else is vendored*, whose quantifier ranges over
  the crew **modules** the declared vendored set partitions and over the
  contents of `Source/StratRules/`, which `T-INT-01` still accounts for at 22
  files — the §4.8 CSVs are vendored by a different mechanism into a different
  directory, so that sentence holds as written. The two senses *vendored* now
  carries are filed as a change request rather than repaired here.
- **The same sweep, run over the three ruling amendments and then over the
  narrowing of AN.** Over the amendments it found one, in my own text: pair 39's
  note ended "the change request below asks for the rule", and Ruling AL retires
  that change request, so the note cites the ruling instead. Membership checks on
  the rulings' own sets: AL keeps `T-DATA-05` marked, so §4.11's † membership,
  §4.5's cut-line pointer and row 2's `T-DATA-01..06 (**T-DATA-05 †**)`
  acceptance cell are unmoved and consistent; AM introduces `dataCommit`, which
  no master sentence names, and §4.9's `rulesCommit` sentences govern a different
  manifest and a different directory; AN's re-opening is a different event from
  the *re-open when it widens* that §4.4's wk-2 note and Q20 state about command
  sets, and Q29's own text says nothing about re-opening. Over the narrowing of
  AN the sweep looked for anything that referred to AN's scope: pair 24's own
  note, which now states the scope split; the Arithmetic note, which speaks only
  to AN adding no register row; the Open-questions pointer, which names AN as
  ruling what re-opens and is more exact after the narrowing than before; and
  §3's row-2 evidence cell and §4.5's green count, neither of which says anything
  about re-opening. Nothing else refers to it.

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §4.9 stub `Inputs` | `the §4.8 tables imported in-editor — among this stub's invariants, T-INT-02 requires them (ruled 2026-08-06)` | Confirm that the vendored CSVs satisfy this Inputs line as written; no pair filed. | The tables are now imported from a **vendored** copy rather than from `data/` directly, and the Inputs line predates the vendoring. |
| §4.9 part 1 | `Nothing else is vendored — a UBT module cannot hold a second `main()`` | Confirm that *vendored* here ranges over crew **modules** and the contents of `Source/StratRules/` only, and rule whether the §4.8 CSVs' vendoring needs its own word. No pair filed: the sentence holds on that reading. | This landing gives *vendored* a second referent — sources into `Source/StratRules/` by `sync_stratrules.py` under `T-INT-01`, and CSVs into a data directory under `GATE-DATA-VENDOR`. `dataCommit` beside `rulesCommit` (pair 25) sharpens the distinction without naming it. |

---

## Open questions for the Director

1. **In the interval between a §4.8 CSV edit and the re-run that closes the new
   pair, does §3's row 2 show a live ✓?** Ruling AN settles which IDs re-open —
   `T-DATA-05` and the headless `T-DATA` IDs together — and that the flip
   re-pins to a new pair when the re-run completes. It settles nothing about the
   interval, and the two are separate claims: the pinned record *green at
   `b1ea992` over the UE tree at `fed8ae9`* stays true of those commits
   throughout, so what is in question is the **live mark** and not the evidence
   behind it. The ledger's own rule — a row cites the commit and passing test IDs
   that back it — reads both ways inside that interval: the ✓ cites a pair that
   did close, and the row also describes a system whose current bytes no green
   covers. No gate decides it; it is a §3 presentation matter, which is why it is
   registered rather than assumed.

The three questions this addendum filed earlier were ruled 2026-08-06 and are
recorded in the pairs rather than carried here: the closed † mark (AL, pair 39),
the CSV manifest's `dataCommit` (AM, pair 25), and which IDs a §4.8 CSV edit
re-opens (AN, pair 24).

---

## Grounding

- Row 2's ledger row, its evidence cell, the posture sentences that explain it,
  and row 4's *joined at* sentence — `source/gdd.md` §3 ledger table and the
  paragraph beneath it.
- Q29's "full acceptance set at one commit", read per acceptance ID — §4.7
  register Q29 and §3's row-7 landing record, whose wording pair 42 uses; the
  two-repo pinning form Q29 is extended to — §4.9's `T-INT-01` record and
  §4.11 row 9.
- The unnumbered-gate precedent `GATE-DATA-VENDOR` and `GATE-DATA-HARDFAIL`
  stand on — §3's `GATE-AI-SMOKE`, `GATE-SCN-PARSE`, `GATE-CAP-PARTIAL`,
  `GATE-SAVE-PARSE`, `GATE-REPLAY-*` and `GATE-BALANCE-*` records.
- Citing commits rather than heads, which Ruling AM's lag and Ruling AN's
  untouched pinned record both rest on — §3's own record of the expired-head
  defect, and the parenthetical beneath the ledger that replaced
  reachability-from-`master` with per-sha pinning.
- Row 8's posture, row 10's remaining ID, and the † list's cut-line costs, including
  "what each mark costs is a **claim**, never a rule", which Ruling AL preserves —
  §4.11's prose above the build-order table, row 10's dependency cell, and the
  † bullets beneath it.
- The `.uproject` registration and the UBT build it produced — §4.9 "The UBT
  module is registered, and it builds", and §3's `031ee20` landing record.
- What the editor pass denotes, what each editor-pass ID needs besides it, and
  the `a13626f` measurement over those subjects — §4.9, ruled 2026-08-05 and
  2026-08-06.
- The harness's absence from the calendar — §4.4's note, ruled 2026-08-06.
- The cut line — §4.7 head.
- Commits: crew `b1ea992` and `c2edae0`; Stratocracy UE project `fed8ae9`;
  prior pins `e19605e`, `031ee20`, `a13626f`, `c224825` as cited in §3.
- Snapshot: `source/MANIFEST.txt`, `gdd.md` md5 `46d05e398f5df9d6aefae5eab017a51e`.
