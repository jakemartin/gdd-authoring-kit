# Candidate set — sentences the fixture widening bears on

Generated mechanically from `source/gdd.md` (md5 `1bfae9f169230f3bdcea4fab48b100f8`) by
sentence-splitting a whitespace-collapsed copy, so a sentence that wraps a line is still
visible. A sentence qualifies only if it PREDICATES on the subject; merely naming
`T-INT-02` does not.

**Membership asserts nothing about a sentence's truth.** Some of these are pinned to a
commit and survive untouched; at least one is about a different artifact entirely. Give
each item a disposition — `amended`, `unchanged and still true`, `pinned, so unmoved`,
`outside this round`. A count is not a disposition.

**This list is not the round's scope.** It matched vocabulary, and the claim it is
looking for has spellings this probe cannot match. Sweep by meaning yourself and add
what it missed; say so plainly if it missed nothing.

---

## 1

_matched A. what the committed parity fixture carries or lacks, E. the vendored data commit and the gate over it_

> `sync_stratdata.py` carries the parity fixture from [`5c47cc1`](https://github.com/jakemartin/stratocracy-crew/commit/5c47cc1), and the crew-side stale-claim repair is at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d).

## 2

_matched A. what the committed parity fixture carries or lacks_

> **`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed, and none of them closes.** The parity fixture they run over carries `Move`, `Attack` and `EndTurn` and carries **no `Capture` and no `Build`**;

## 3

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> What their closure waits on is a parity fixture carrying the complete §4.9 command set, and the two commands this fixture lacks are absent for different reasons.

## 4

_matched A. what the committed parity fixture carries or lacks_

> with the parity fixture absent `GATE-REPLAY-FIXTURE` blocks on clauses (b)(c)(e)(f)(g) while (a) and (d) pass, and against the bundled buggy replayer it blocks on (f) and (g) while (a)–(e) pass.

## 5

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> What their closure waits on is a parity fixture carrying the complete §4.9 command set, which rows 4–5 supply and the fixture run there does not carry (§3).

## 6

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), `T-INT-02` and `T-INT-03` having run and passed there at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` without closing, what their closure waits on being a parity fixture carrying the complete §4.9 command set, and `T-INT-05` not having run and lacking those same widgets — its other two having closed and both now credited at `9289c1d`, over the vendored tree at `0897cb5` — T-INT-01 because it asserts identity at `rulesCommit`, which moved to `cb8e12b`, and T-INT-04 because it compiles the vendored copy, whose implementations `Save` and `Replay` joined;

## 7

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> and the **1** left in row 10, whose parts (a), (b) and (c) have all since landed — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), part (b) having run over the command set part (c) requires, and `T-SAVE-07` at [`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e) over a self-play log written in the §4.10 format — leaving `T-SAVE-06`, which ran and passed in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` without closing — it is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, and what its closure waits on is a parity fixture carrying the complete §4.9 command set (§3) | The **† cut line** (§4.7 head;

## 8

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> `Save` and `Replay` were vendored into `Source/StratRules/` at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b`, where the command surface landed with them and `T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed in the editor pass without closing, their closure waiting on a parity fixture carrying the complete §4.9 command set (§3);

## 9

_matched A. what the committed parity fixture carries or lacks_

> `T-INT-02` and `T-INT-03` ran and passed in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b`, over a parity fixture carrying `Move`, `Attack` and `EndTurn` and carrying no `Capture` and no `Build`, which is a run and not a closure (§3).

## 10

_matched A. what the committed parity fixture carries or lacks_

> the parity fixture replayed there carries `Move`, `Attack` and `EndTurn` and carries no `Capture` and no `Build` (§3) | Source/compile gates yes;

## 11

_matched A. what the committed parity fixture carries or lacks, B. the completeness of a command set a log carries, D. what a closure waits on_

> What its closure waits on is a parity fixture carrying the complete §4.9 command set.

## 12

_matched B. the completeness of a command set a log carries_

> **This row does not flip.** Q29 requires the full acceptance set at one commit, and it is applied **per acceptance ID as well as per row** — an ID closes only when its whole written fixture set has run.

## 13

_matched B. the completeness of a command set a log carries_

> rows 4, 5 and 6 are green at [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df), [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) and [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1), so the calendar reason for the split is gone and the gate's log carries the **complete §4.9 command set** — `Move`, `Attack`, `Build`, `Capture` and `EndTurn` — which is what Q29 requires before an acceptance ID may close.

## 14

_matched B. the completeness of a command set a log carries, C. the MECHANISM by which Capture or Build was absent_

> **A self-play log carries four command kinds, not five, and that is a property of the AI rather than of the format.** `cpp_reference/Ai.h` states that capture is deliberately outside the AI's vocabulary — a turn-boundary event the caller runs beside income, the AI's part of it being the move onto the objective (`T-AI-03`) — so `AiCommandKind` has four members where §4.9 has five, and a self-play match emits `Move`, `Attack`, `Build` and `EndTurn` and never `Capture`.

## 15

_matched B. the completeness of a command set a log carries_

> The complete §4.9 command set was exercised by part (b)'s hand-authored log at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6).

## 16

_matched B. the completeness of a command set a log carries_

> `T-SAVE-07` asserts **format compatibility, not command coverage**, so those four are its whole written fixture set, Q29 is satisfied over that set, and the gate asserts the four are present and the fifth absent rather than leaving the absence to be read as a shortfall.

## 17

_matched B. the completeness of a command set a log carries_

> **T-SAVE-01, T-SAVE-02, T-SAVE-03 and T-SAVE-05 are green at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6)** (§3), where row 10's part (b) ran over the complete command set rows 4–5 supply.

## 18

_matched B. the completeness of a command set a log carries, D. what a closure waits on_

> §4.11 rows 9–10 now **run** their gates in week 2 over a `{Move, Attack}` log and re-run them over the complete command set in week 3 (Q20, amended).

## 19

_matched B. the completeness of a command set a log carries, D. what a closure waits on_

> rows 1–3 for week 2's `{Move, Attack}` log, and they re-open on the `Capture`/`Build`/`EndTurn` that rows 4–5 have since added.

## 20

_matched B. the completeness of a command set a log carries_

> it runs T-SAVE-01/02/03/05/06 over week 2's `{Move, Attack}` log.

## 21

_matched B. the completeness of a command set a log carries, C. the MECHANISM by which Capture or Build was absent_

> That log carries the four command kinds row 6's AI emits and not the fifth, `Capture` being outside the AI's vocabulary by design (`T-AI-03`), and `T-SAVE-07` asserts format compatibility rather than command coverage, so its whole written fixture set ran.

## 22

_matched B. the completeness of a command set a log carries_

> row 7's ledger flip, on the Q29 reading applied per acceptance ID as well as per row — an ID closes only when its whole written fixture set has run.

## 23

_matched C. the MECHANISM by which Capture or Build was absent_

> **§4.8's seven bool UStruct fields drop the `b` prefix** — `CanCapture`, `PassLand`, `PassAir`, `PassSea`, `Capturable`, `IsSpawnPoint`, `IsRepairPoint` — measured at engine source:

## 24

_matched C. the MECHANISM by which Capture or Build was absent_

> **`Capture` cannot be produced at all:** `AiCommandKind` is `{Build, Move, Attack, EndTurn}` and has no `Capture` member, so nothing reading that enum can emit one.

## 25

_matched C. the MECHANISM by which Capture or Build was absent_

> **`Build` can be produced, and this fixture's harness never asks for it:** the harness builds its `AiState` without assigning `buildlist`, and `chooseBuild` iterates that list and returns -1 when it is empty, before Fame is consulted;

## 26

_matched C. the MECHANISM by which Capture or Build was absent_

> Fame sufficiency is not what stops it — `startingFame` is 200 a side, Infantry's `CostFame` is 100, side 0 owns the `Factory` hex at column 1 row 4 with `IsSpawnPoint` true, and `queueBuild` refuses only when `fameTotal` is below the cost.

## 27

_matched C. the MECHANISM by which Capture or Build was absent_

> the flag is "a designated Tank") startingFame object per side;

## 28

_matched C. the MECHANISM by which Capture or Build was absent_

> | Column | CSV type | Headless field | UStruct field | Source | |---|---|---|---|---| | `Id` (row name) | string | `id` | RowName | §2.3 | | `MoveCost` | int (0 = impassable) | `moveCost` | `int32 MoveCost` | §2.3 (Plains 1, Woods 2, Mountains 3, Water —, Town 1, Bridge 1, Factory 1) | | `DefensePct` | int, signed | `defensePct` | `int32 DefensePct` | §2.3 (0, 20, 40, 0, 10, **−10**, 15) | | `PassLand`/`PassAir`/`PassSea` | bool ×3 | `passLand/Air/Sea` | `bool PassLand/PassAir/PassSea` | §2.3 Passable column | | `Capturable` | bool | `capturable` | `bool Capturable` | §2.3 (Town, Factory) | | `IncomeFame` | int | `incomeFame` | `int32 IncomeFame` | §2.7 (Factory 100, Town 25, else 0) | | `IsSpawnPoint` | bool | `isSpawnPoint` | `bool IsSpawnPoint` | §2.7 (Factory) | | `IsRepairPoint` | bool | `isRepairPoint` | `bool IsRepairPoint` | §2.7 Repair (Town + Factory) | **Type-effectiveness schema** — `data/effectiveness.csv` → `strat::effectiveness` → UStruct `FEffectivenessRow`.

## 29

_matched D. what a closure waits on_

> §4.11 states that `T-INT-02/03/05` re-open on the `Capture`/`Build`/`EndTurn` rows 4–5 added and close on rows 1–5, and Q29 reports a partial pass as a run and never as a closure.

## 30

_matched E. the vendored data commit and the gate over it_

> **How `b1ea992` and `c2edae0` were authored is deliberately not stated:** no harness claim is made for either, because none was established.* **§4.9 part 2's bridge landed, at `0897cb5` in the Stratocracy UE project repo against the crew half [`cb8e12b`](https://github.com/jakemartin/stratocracy-crew/commit/cb8e12b), and the substance of this round is the defect that landing exposed rather than the three acceptance IDs that ran.** The UE tree there records `dataCommit` [`862a225`](https://github.com/jakemartin/stratocracy-crew/commit/862a225) in `Data/StratData.manifest.json` and `rulesCommit` `cb8e12b` in `Source/StratRules/StratRules.manifest.json`;

## 31

_matched E. the vendored data commit and the gate over it_

> That copy is made by `sync_stratdata.py`, the CSV counterpart of the script that vendors the C++ sources;

## 32

_matched E. the vendored data commit and the gate over it_

> **The manifest's `dataCommit` names the commit the vendored bytes came from, and it advances when and only when those bytes change (ruled 2026-08-06).** A crew commit that does not touch the data directory leaves it where it is, so a `dataCommit` behind the crew commit this document stands at is the **expected** state and not a stale one:

## 33

_matched E. the vendored data commit and the gate over it_

> `GATE-DATA-VENDOR` reads `dataCommit` and logs it;

## 34

_matched E. the vendored data commit and the gate over it_

> What differs is which bytes, by which script, under which gate — the crew's C++ sources into `Source/StratRules/` by `sync_stratrules.py` under `T-INT-01`, and the §4.8 CSVs into the UE project's data directory by `sync_stratdata.py` under `GATE-DATA-VENDOR`.

## 35

_matched E. the vendored data commit and the gate over it_

> **The word is not split, and the reason is that the artifact does not split it:** `sync_stratdata.py`, its manifest note and its crew commit message all say *vendor*, so a rename confined to this document would diverge the document from the thing it describes.
