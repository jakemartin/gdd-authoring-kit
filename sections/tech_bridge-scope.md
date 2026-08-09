# Technical design — addendum `bridge-scope` (tech-director)

## Placement
Old→new pairs against the merged master: §3 (the ledger prose), §4.4, §4.5,
§4.9, §4.11. No section is redrafted.

## Draft

### Pair 1
**Anchor:** §3, ledger prose, the `e06c44b`/`b23823f` registration record

**OLD**
```
**No bridge exists:** no load mapping, no command surface, no event list, no actor and no widget, so §4.9 part 2 is unbuilt.
```
**NEW**
```
**No bridge existed there:** no load mapping, no command surface, no event list, no actor and no widget, so §4.9 part 2 was unbuilt at that commit.
```

---

### Pair 38
**Anchor:** §3, ledger prose, the same `b23823f` first-UBT-build record, what a green UBT build is not evidence for

**OLD**
```
while in-engine compilation is what the editor pass gates, and that pass does not exist.
```
**NEW**
```
while in-engine compilation is what the editor pass gates, and that pass did not exist at that commit.
```

---

### Pair 2
**Anchor:** §3, ledger prose, the row-10-part-(b) record

**OLD**
```
and among what it still waits on are the editor pass and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists.
```
**NEW**
```
and among what it still waited on there were the editor pass and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine and therefore vendored, and `Replay` was then ruled out of vendoring until a bridge consumer existed.
```

---

### Pair 3
**Anchor:** §3, ledger prose, the `Balance` module record

**OLD**
```
**What landed is a producer of §4.10 command logs**, and the editor pass `T-SAVE-06` waits on is untouched by it.
```
**NEW**
```
**What landed is a producer of §4.10 command logs**, and the editor pass `T-SAVE-06` then waited on was untouched by it.
```

---

### Pair 4
**Anchor:** §3, ledger prose, the `Balance` module record, the vendoring ruling it stands on

**OLD**
```
**`Balance` is deliberately not vendored** on the same ruling the other two unvendored modules stand on (§4.9)
```
**NEW**
```
**`Balance` is deliberately not vendored** on the ruling `Save` and `Replay` stood on at that commit, which §4.9 records still describing the tree for `Balance` alone
```

---

### Pair 5
**Anchor:** §3, ledger prose, the `e19605e` re-dating record

**OLD**
```
`T-SAVE-06` remains the only † of row 10's seven, and among what it waits on are the editor pass and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine, and `Replay` is ruled out of vendoring until a bridge consumer exists. Both what *the editor pass* denotes and what running it does not supply are stated at §4.9. `cpp_reference/selfplay.cpp` is untouched. `Save`, `Replay` and `Balance` remain unvendored, and the ruling that keeps them out is now **stated in the declaration** rather than implied by a glob.
```
**NEW**
```
`T-SAVE-06` was then the only † of row 10's seven, and among what it waited on there were the editor pass and a vendored replayer: it is asserted jointly with `T-INT-02`, whose replay runs **in-engine** and so needs the replayer compiled into the engine, and `Replay` was then ruled out of vendoring until a bridge consumer existed. Both what *the editor pass* denotes and what running it does not supply are stated at §4.9. `cpp_reference/selfplay.cpp` is untouched. `Save`, `Replay` and `Balance` were unvendored at that commit, and the ruling that kept them out was **stated in the declaration** rather than implied by a glob.
```

---

### Pair 6
**Anchor:** §3, ledger prose, the `e19605e` repair of the `T-INT-01` check

**OLD**
```
while the vendored set is the ten crew modules §4.9 enumerates, `Save`, `Replay` and `Balance` being ruled out of vendoring.
```
**NEW**
```
while the vendored set was then the ten crew rules modules §4.9 enumerated, `Save`, `Replay` and `Balance` being ruled out of vendoring at that commit.
```

---

### Pair 7
**Anchor:** §3, ledger prose, the `fed8ae9` record of the `.uproject` removal

**OLD**
```
do not re-date: both remain green at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), and the running check reports all 22 files in `Source/StratRules/` accounted for.
```
**NEW**
```
did not re-date there: both were green at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), where the running check reported all 22 files in `Source/StratRules/` accounted for.
```

---

### Pair 8
**Anchor:** §3, ledger prose, the `fed8ae9` landing's "what this landing does not close"

**OLD**
```
It closes no acceptance ID other than `T-DATA-05`. `T-INT-02` still needs a vendored replayer — its replay runs **in-engine**, and `Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03` still needs the command surface, which is part of the unbuilt bridge; `T-INT-05`, `T-UI-03` and `T-UI-04` still need real Stratocracy widgets; and `T-SAVE-06` is asserted jointly with `T-INT-02` and inherits that blocker. Build-order rows 9 and 10 therefore still do not close, and the ledger gains a row for neither.
```
**NEW**
```
It closed no acceptance ID other than `T-DATA-05`. At that commit `T-INT-02` still needed a vendored replayer — its replay runs **in-engine**, and `Replay` was then ruled out of vendoring until a bridge consumer existed; `T-INT-03` still needed the command surface, the bridge being unbuilt there; `T-INT-05`, `T-UI-03` and `T-UI-04` need real Stratocracy widgets; and `T-SAVE-06` is asserted jointly with `T-INT-02` and inherited that blocker. Build-order rows 9 and 10 did not close there, and the ledger gained a row for neither.
```

---

### Pair 9
**Anchor:** §3, ledger prose, the `c2edae0` stale-claim repair

**OLD**
```
at thirteen sites in five spellings, and each site now names what its ID still lacks.
```
**NEW**
```
at thirteen sites in five spellings, and each site named what its ID lacked at that commit.
```

---

### Pair 10
**Anchor:** §3, ledger prose, the deferral of the integration ledger row

**OLD**
```
while the bridge §4.9 part 2 describes is unbuilt, so a row written now would either name a system that half-exists or start a practice of one row per half.
```
**NEW**
```
while the bridge §4.9 part 2 describes is incomplete — its load mapping and command surface are built, and it has no event list, no actor and no widget — so a row written now would either name a system that half-exists or start a practice of one row per half.
```

---

### Pair 35
**Anchor:** §3, ledger prose, the sentence following Pair 10's anchor, the deferral's trigger

**OLD**
```
The row is deferred until the bridge is built, so the ledger later gains a row describing a whole system.
```
**NEW**
```
The row is deferred until the bridge is whole, so the ledger later gains a row describing a whole system.
```

---

### Pair 36
**Anchor:** §3, ledger prose, the naming of the integration row, the same trigger stated forward

**OLD**
```
and it is created as **one** row when §4.9 part 2 lands
```
**NEW**
```
and it is created as **one** row when §4.9 part 2 lands whole
```

---

### Pair 11
**Anchor:** §3, ledger prose, immediately before the Legend

**OLD**
```
because none was established.* Legend: **Author**
```
**NEW**
```
because none was established.* **§4.9 part 2's bridge landed, at `0897cb5` in the Stratocracy UE project repo against the crew half [`cb8e12b`](https://github.com/jakemartin/stratocracy-crew/commit/cb8e12b), and the substance of this round is the defect that landing exposed rather than the three acceptance IDs that ran.** The UE tree there records `dataCommit` [`862a225`](https://github.com/jakemartin/stratocracy-crew/commit/862a225) in `Data/StratData.manifest.json` and `rulesCommit` `cb8e12b` in `Source/StratRules/StratRules.manifest.json`; `Save` and `Replay` entered `Source/StratRules/` at that UE commit, the crew having declared them vendored at [`f5fdb69`](https://github.com/jakemartin/stratocracy-crew/commit/f5fdb69); `sync_stratdata.py` carries the parity fixture from [`5c47cc1`](https://github.com/jakemartin/stratocracy-crew/commit/5c47cc1), and the crew-side stale-claim repair is at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d). **The defect: a UBT module that had compiled and linked for four commits was structurally incapable of satisfying a cross-module call.** An editor target is a **modular** build, so every UBT module is its own DLL and Unreal exports only symbols carrying an `_API` macro. The vendored rules-module sources carry none — §4.9 forbids them engine headers — and `dumpbin /EXPORTS` over `UnrealEditor-StratRules.dll` reports **one** export, `ThisIsAnUnrealEngineModule`. The first code that tried to call across that boundary — the bridge — failed with **8 × LNK2019**. No gate could see it, because nothing had ever *called* it. `T-INT-04` cannot catch it and is not weakened by it: it compiles the rules modules **standalone, outside UBT**, which is a different question from whether a UBT module exposes them. **This is the next transition of the failure recorded above**, where the round that registered `StratRules` gated that it *compiles* and *links* and never launched the editor, and the repair that followed left it *still built, still linked* — true, and still one transition short. The chain is compile → link → load → **call**, and the last three were each reached by a separate landing. **The repair.** The bridge is its own UBT module, `StratBridge`, and the vendored rules-module sources are compiled into it by **one shim per source** — one each because several rules modules declare same-named helpers in anonymous namespaces, which collide in a single translation unit. No vendored byte is edited by that repair: the shims `#include` `Source/StratRules/`. **What §4.9 part 1's link dependency buys is header access, not linkage of `strat::` functions:** the `Stratocracy` module's build rules still list `StratRules` among their public dependency modules at `0897cb5`, and what that supplies is the vendored combat header the parity harness includes so its enum mirror compares against the real enum — no callable symbol, for the one-export reason above. **`T-INT-01` and `T-INT-04` re-date, on the vendoring rather than on the shims.** `rulesCommit` moved `e19605e` → `cb8e12b`, and the vendored set grew when `Save` and `Replay` entered the UE tree at `0897cb5`, the crew declaration having moved them from excluded to vendored at [`f5fdb69`](https://github.com/jakemartin/stratocracy-crew/commit/f5fdb69) — **22 files → 26**, **20 sources → 24**, **ten vendored rules modules → twelve** — so both conditions this ledger states for the previous re-dating are met again: `T-INT-01` asserts identity at `rulesCommit`, which moved, and `T-INT-04` compiles the vendored copy, whose set of implementations changed. Both are green at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d) over the vendored tree at `0897cb5`, where the integration gate passes **2/2**, `T-INT-01` accounting for all 26 files in `Source/StratRules/` at `cb8e12b` — 24 sources beside `StratRules.Build.cs` and the manifest, the declaration partitioning the 13 crew rules modules as 12 vendored and 1 ruled out — and `T-INT-04` compiling the **12** vendored rules-module implementations standalone under clang++, outside UBT. **Neither re-dating moves a count:** both IDs were already green and neither ID's written text changed, so both are closure movements rather than widenings. **No earlier pair qualifies:** `Source/StratRules/` holds 22 files at `a13626f` and at `fed8ae9` and 26 at `0897cb5`, the four added being `Save`'s and `Replay`'s header and implementation, and the recorded `rulesCommit` is `e19605e` at `fed8ae9` and `cb8e12b` at `0897cb5`, so both conditions are first met at `0897cb5` and at no earlier UE tree. `StratBridge` is listed in `Stratocracy.uproject`'s `Modules` array and carries a real `IMPLEMENT_MODULE`; `StratRules` is still absent from that array, deliberately. **The editor pass at `0897cb5`: 8 tests, 8 Success.** Three are new — `Stratocracy.StratBridge.T-INT-02.ReplayParityWithHeadless`, `Stratocracy.StratBridge.T-INT-03.RejectionSafety` and `Stratocracy.StratBridge.GATE-BRIDGE-DEFS.MappedDefsMatchLoaderOrder`. Five already ran at `fed8ae9`: `GATE-DATA-VENDOR`, and `T-DATA-05` in four tests (unit table, terrain table, effectiveness table, enum mirror). Beside them, the week-1 gate PASSes headless at `9289c1d` with `accepted=True`, and row 10's part (b) is 36/36 there, including seven `GATE-REPLAY-FIXTURE` clauses. **`GATE-BRIDGE-DEFS` mints no acceptance ID**, on the `GATE-DATA-VENDOR`, `GATE-AI-SMOKE` and `GATE-CAP-PARTIAL` precedent. **`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed, and none of them closes.** The parity fixture they run over carries `Move`, `Attack` and `EndTurn` and carries **no `Capture` and no `Build`**; §4.11 states that `T-INT-02/03/05` re-open on the `Capture`/`Build`/`EndTurn` rows 4–5 added and close on rows 1–5, and Q29 reports a partial pass as a run and never as a closure. What their closure waits on is a parity fixture carrying the complete §4.9 command set, and the two commands this fixture lacks are absent for different reasons. **`Capture` cannot be produced at all:** `AiCommandKind` is `{Build, Move, Attack, EndTurn}` and has no `Capture` member, so nothing reading that enum can emit one. **`Build` can be produced, and this fixture's harness never asks for it:** the harness builds its `AiState` without assigning `buildlist`, and `chooseBuild` iterates that list and returns -1 when it is empty, before Fame is consulted; `Balance`'s equivalent view does assign a buildlist. Fame sufficiency is not what stops it — `startingFame` is 200 a side, Infantry's `CostFame` is 100, side 0 owns the `Factory` hex at column 1 row 4 with `IsSpawnPoint` true, and `queueBuild` refuses only when `fameTotal` is below the cost. **No acceptance ID was written here and none closed**, so §4.5's written, green and unclosed figures do not move at this landing — **71**, **62** and **9** — row 9's unclosed count stays **3** and row 10's stays **1**. **No ledger row is created, flipped or removed by this landing.** **The suite was proven able to FAIL on three known-bad inputs, each restored afterwards.** The parity fixture's `stateHash` altered with the manifest untouched: `T-INT-02` FAIL and `GATE-DATA-VENDOR` FAIL. The same forgery with the manifest **updated to match**: `GATE-DATA-VENDOR` passes and **`T-INT-02` FAILS alone**, which is what shows that ID asserting on its own rather than riding the vendor gate's sha256. `units.csv` row order reversed with the manifest updated: `GATE-BRIDGE-DEFS` FAIL. The same discipline was applied on the crew side before the fixture existed: with the parity fixture absent `GATE-REPLAY-FIXTURE` blocks on clauses (b)(c)(e)(f)(g) while (a) and (d) pass, and against the bundled buggy replayer it blocks on (f) and (g) while (a)–(e) pass. **The third input recorded something not previously known: `T-DATA-05`'s unit-table test PASSED on reversed rows.** It looks each row up **by Id** and never compares order, so it is structurally order-blind. `GATE-BRIDGE-DEFS` is therefore the only check in the project standing between a reordered table and a `defIndex` that silently resolves a Build command to the wrong unit type, and it mints no acceptance ID. **What this landing does not do is stated so it is not inferred.** **`T-INT-05` did not run**, and what it lacks is the real Stratocracy widgets it asserts over. **The bridge is partly built:** the load mapping and the command surface exist, and there is **no event list, no actor and no widget**. `Balance` is **not** vendored; the bridge does not consume it, so the 2026-08-05 ruling still describes the tree for that module, while for `Save` and `Replay` the ruling is spent — part 2 supplied the consumer it named. **Stale claims in the crew repo were repaired at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d):** eleven sites said that the bridge did not exist, that `T-INT-02` waited on a vendored replayer a ruling deferred, that `T-INT-03` waited on an unbuilt command surface, that no in-editor Automation harness or editor pass existed, or that `T-INT-02` and `T-INT-03` lacked the subjects they assert over. Sentences of the form *"they do not run **here**"* are true of every headless suite in that repo and were kept. **That same commit introduced false claims of its own:** fourteen clauses across **ten** files — two runner modules, three test and harness sources, the README and four spec documents — assert that `T-SAVE-06` and `T-INT-02` **closed** in the editor pass at `0897cb5`. They ran and passed and did not close, so all fourteen are false. In almost every case such a clause sits beside a true negative — that no headless build can close `T-SAVE-06`, that it is marked † and asserted jointly with `T-INT-02` — and the true negative stands. **Two commit messages carry claims measurement contradicts, and neither can be amended.** UE `0897cb5`'s message states that `T-INT-01` and `T-INT-04` do not re-date and cites crew `cb8e12b` as the commit both are green at; both halves are false. Both re-date, on the file-count and `rulesCommit` measurements recorded above, and `cb8e12b` is the `rulesCommit` that UE tree records — the crew commit its sources were vendored **from** — while the crew commit the checks were run at is `9289c1d`. Crew `9289c1d`'s message names the unvendored module `Selfplay` at three places; the vendored-set declaration the identity check reads has named that module `Balance` since [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), which is earlier than `9289c1d`, and the naming record above states why the other spelling is impossible. The tree was corrected at the crew tip; the message cannot be. Each of the two messages was written from a fact block the addendum round had not yet gated. **Where a commit message and this ledger disagree, this ledger is the record.** Legend: **Author**
```

---

### Pair 12
**Anchor:** §4.4, milestone table, wk 2 cell

**OLD**
```
**T-INT-04 and T-INT-01 are green at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e)**, over the vendored tree at `a13626f`, and **T-SAVE-04 at
```
**NEW**
```
**T-INT-04 and T-INT-01 are green at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d)**, over the vendored tree at `0897cb5` against `rulesCommit` `cb8e12b`, and **T-SAVE-04 at
```

---

### Pair 13
**Anchor:** §4.4, milestone table, wk 3 cell

**OLD**
```
`T-SAVE-06` did not close here: among what it waits on is a vendored replayer, it being asserted jointly with `T-INT-02` (§4.9). `T-INT-02` did not close here either: among what it waits on is that replayer, `Replay` being ruled out of vendoring until a bridge consumer exists (§4.9). The editor pass both of them also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3), in no week this table names. Nor did `T-INT-03`: among what it waits on is the bridge's command surface, which is unbuilt (§4.9). Nor did `T-INT-05`: among what it waits on are the real Stratocracy widgets it asserts against, measured absent at `a13626f` (§4.9).
```
**NEW**
```
`T-SAVE-06`, `T-INT-02` and `T-INT-03` did not close here, and have since run and passed without closing, in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` (§3), in no week this table names: `Replay` was vendored into `Source/StratRules/` at that UE commit and the bridge's command surface landed there, and the editor pass all three also lacked had landed at `fed8ae9` in the same repo (§3). What their closure waits on is a parity fixture carrying the complete §4.9 command set, which rows 4–5 supply and the fixture run there does not carry (§3). `T-INT-05` did not close here either, and what it lacks is the real Stratocracy widgets it asserts against, measured absent at `a13626f` (§4.9).
```

---

### Pair 14
**Anchor:** §4.4, the note under the milestone table

**OLD**
```
And a **vendored** replayer is held out rather than merely uncelled: §4.9 rules `Replay` out of vendoring until a bridge consumer exists, a condition no cell here dates
```
**NEW**
```
And a **vendored** replayer was held out rather than merely uncelled: §4.9 ruled `Replay` out of vendoring until a bridge consumer existed, a condition no cell here dated
```

---

### Pair 15
**Anchor:** §4.4, the note under the milestone table, closing sentence

**OLD**
```
The principle stated above — the week the thing that consumes it runs — now governs what is still uncelled beside them: the vendored replayer `T-INT-02` waits on, the command surface `T-INT-03` waits on, and the real Stratocracy widgets `T-INT-05`, `T-UI-03` and `T-UI-04` wait on (§4.9).
```
**NEW**
```
The principle stated above — the week the thing that consumes it runs — governed the two that have since landed off this calendar: the vendored replayer and the bridge's command surface, both at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b`, where `T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed in the editor pass without closing (§3). What is still uncelled is the real Stratocracy widgets `T-INT-05`, `T-UI-03` and `T-UI-04` assert against (§4.9).
```

---

### Pair 37
**Anchor:** §4.4, the same note, what stood between the `fed8ae9` landing and a cell held at it

**OLD**
```
while the subjects the other editor-pass IDs assert against are unbuilt (§4.9)
```
**NEW**
```
while the subjects the other editor-pass IDs assert against were unbuilt at that landing (§4.9)
```

---

### Pair 16
**Anchor:** §4.5, "Specification outruns the build" cell, the closure convention

**OLD**
```
both greens now stand at `e19605e` and are counted there below (§3)
```
**NEW**
```
both greens now stand at `9289c1d`, over the vendored tree at `0897cb5`, and are counted there below (§3)
```

---

### Pair 17
**Anchor:** §4.5, same cell, the by-commit green tally

**OLD**
```
and **2** at [`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e), where `T-INT-01` and `T-INT-04` re-date over the vendored tree at `a13626f` without closing row 9's acceptance set either — `T-INT-01` because it asserts identity at `rulesCommit`, which moved there, and `T-INT-04` because it compiles the vendored copy, whose `Turn.h` bytes changed — neither on a text change, so both are closure movements rather than widenings (§3)
```
**NEW**
```
and **2** at [`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d), where `T-INT-01` and `T-INT-04` re-date over the vendored tree at `0897cb5` without closing row 9's acceptance set either — `T-INT-01` because it asserts identity at `rulesCommit`, which moved to `cb8e12b`, and `T-INT-04` because it compiles the vendored copy, whose implementations `Save` and `Replay` joined at `0897cb5` — neither on a text change, so both are closure movements rather than widenings, and this count does not move on them (§3)
```

---

### Pair 18
**Anchor:** §4.5, same cell, row 9's unclosed IDs

**OLD**
```
the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), `T-INT-02` waiting on a vendored replayer, `T-INT-03` on the bridge's command surface and `T-INT-05` on those same widgets —
```
**NEW**
```
the **3** left in row 9 — T-INT-02, T-INT-03 and T-INT-05, which are scheduled into the editor pass (§4.9), `T-INT-02` and `T-INT-03` having run and passed there at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` without closing, what their closure waits on being a parity fixture carrying the complete §4.9 command set, and `T-INT-05` not having run and lacking those same widgets —
```

---

### Pair 19
**Anchor:** §4.5, same cell, where row 9's two green IDs are credited

**OLD**
```
its other two having closed and both now credited at `e19605e` — T-INT-01 because it asserts identity at `rulesCommit`, which moved there, and T-INT-04 because it compiles the vendored copy, whose `Turn.h` bytes changed; T-INT-04 first passed at `b23823f`, and T-INT-01 first closed at `d837fc8` on the widening of its own text (§3)
```
**NEW**
```
its other two having closed and both now credited at `9289c1d`, over the vendored tree at `0897cb5` — T-INT-01 because it asserts identity at `rulesCommit`, which moved to `cb8e12b`, and T-INT-04 because it compiles the vendored copy, whose implementations `Save` and `Replay` joined; T-INT-04 first passed at `b23823f`, and T-INT-01 first closed at `d837fc8` on the widening of its own text (§3)
```

---

### Pair 20
**Anchor:** §4.5, same cell, row 10's unclosed ID

**OLD**
```
— leaving `T-SAVE-06`, among what it waits on being a vendored replayer — it is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, and `Replay` is ruled out of vendoring until a bridge consumer exists (§3)
```
**NEW**
```
— leaving `T-SAVE-06`, which ran and passed in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` without closing — it is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, and what its closure waits on is a parity fixture carrying the complete §4.9 command set (§3)
```

---

### Pair 21
**Anchor:** §4.9 part 1, the vendored module's state

**OLD**
```
`a13626f` in the UE project repo against `rulesCommit`
[`e19605e`](https://github.com/jakemartin/stratocracy-crew/commit/e19605e)
(§3): the ten modules Combat, Hex, Data, Move, Economy, Turn, Ai, Scenario, Ui
and Driver, each as `X.h` and `X.good.cpp`, beside `StratRules.Build.cs`,
```
**NEW**
```
`0897cb5` in the UE project repo against `rulesCommit`
[`cb8e12b`](https://github.com/jakemartin/stratocracy-crew/commit/cb8e12b)
(§3): twelve rules modules — Combat, Hex, Data, Move, Economy, Turn, Ai,
Scenario, Ui and Driver, joined there by Save and Replay — each as `X.h` and
`X.good.cpp`, beside `StratRules.Build.cs`,
```

---

### Pair 22
**Anchor:** §4.9 part 1, the three deliberately unvendored crew modules

**OLD**
```
**Three crew modules exist and are deliberately
not vendored (ruled 2026-08-05).** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666),
`Replay` at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) and
`Balance` at
[`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e)
(§3), and all three stay out of `Source/StratRules/`, where they would be an
eleventh, a twelfth and a thirteenth module beside the ten enumerated above.
§3 records that no bridge exists — no load mapping, no command surface, no
event list, no actor and no widget — so §4.9 part 2 is unbuilt and the bridge
consumer that would read them is still hypothetical, while vendoring now would
re-date `T-INT-01`'s and `T-INT-04`'s closures. That is a decision rather than
an omission, and **nothing re-dated on their account**: after the third module
landed `T-INT-01` was green at `d837fc8` and `T-INT-04` at `b23823f`, both
still passing 2/2 at `rulesCommit` `d837fc8`, and no UE project commit was made
at any of the three landings. Both closures now stand at `e19605e` (§3) —
`T-INT-01` because `rulesCommit` moved and `T-INT-04` because `Turn.h`'s
vendored bytes changed — and neither moved on these three modules' account,
which leaves the decision recorded here as it was made. The enumeration above
is correct as it
stands, and three modules were left out on purpose.
`cpp_reference/selfplay.cpp` is **not** one of the three and is
excluded for the different reason stated above — a UBT module cannot hold a
second `main()` — and it stays in that exclusion list unchanged.
```
**NEW**
```
**The 2026-08-05 deferral of `Save` and `Replay` is spent, and `Balance`
stays out (ruled 2026-08-05).** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666),
`Replay` at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) and
`Balance` at
[`1ee890e`](https://github.com/jakemartin/stratocracy-crew/commit/1ee890e)
(§3). The ruling held all three out of `Source/StratRules/` until §4.9 part 2
supplied a consumer, no bridge existing when it was written — no load mapping,
no command surface, no event list, no actor and no widget, and none of those
subjects exists at `a13626f` either, measured below — so the consumer it named
was hypothetical. Part 2 has since supplied it — the bridge's load mapping and
command surface are built, and it has no event list, no actor and no widget —
and the crew declared `Save` and `Replay` vendored at
[`f5fdb69`](https://github.com/jakemartin/stratocracy-crew/commit/f5fdb69), the
UE project vendoring them into `Source/StratRules/` at `0897cb5`, which makes
the vendored set twelve: the ten enumerated above plus those two.
`Balance` stays out, where it would be a thirteenth rules module beside them,
the bridge not consuming it, and the declaration partitions the 13 crew rules
modules as 12 vendored and 1 ruled out. **Both `T-INT` closures re-date on that
vendoring** — `T-INT-01` because `rulesCommit` moved `e19605e` → `cb8e12b`, and
`T-INT-04` because the vendored copy it compiles went from 20 sources to 24 —
and both are green at
[`9289c1d`](https://github.com/jakemartin/stratocracy-crew/commit/9289c1d) over
the vendored tree at `0897cb5`, where the integration gate passes 2/2,
`T-INT-01` accounting for all 26 files in `Source/StratRules/` and `T-INT-04`
compiling the twelve vendored implementations standalone under clang++, outside
UBT (§3). Neither re-dating moves a count: both were already green and neither
ID's written text changed.
`cpp_reference/selfplay.cpp` is **not** one of those three rules modules and is
excluded for the different reason stated above — a UBT module cannot hold a
second `main()` — and it stays in that exclusion list unchanged.
```

---

### Pair 23
**Anchor:** §4.9 part 1, what the editor pass gates

**OLD**
```
pass gates, and that pass exists at `fed8ae9` (§3), where it runs `T-DATA-05`
and `GATE-DATA-VENDOR` and no in-engine parity check over the vendored module.
```
**NEW**
```
pass gates, and that pass exists at `fed8ae9` (§3), where it ran `T-DATA-05`
and `GATE-DATA-VENDOR` and no in-engine parity check over the vendored module;
at `0897cb5`, against the crew half `cb8e12b`, it runs eight tests, 8 Success,
three of them new — `T-INT-02`, `T-INT-03` and `GATE-BRIDGE-DEFS`, the last
minting no acceptance ID, and none of the three closing (§3).
```

---

### Pair 39
**Anchor:** §4.9 part 1, the `fed8ae9` removal from the `Modules` array, the re-date clause only — the link-dependency clause in the same sentence is untouched (CR-4)

**OLD**
```
`T-INT-01` and `T-INT-04` do not re-date (§3).
```
**NEW**
```
`T-INT-01` and `T-INT-04` did not re-date on that removal (§3).
```

---

### Pair 24
**Anchor:** §4.9 part 2, the opening lead-in that assigns the bridge's owner

**OLD**
```
**2. Bridge — the only code that knows both worlds.** The game module
(`Stratocracy`) owns:
```
**NEW**
```
**2. Bridge — the only code that knows both worlds.** The bridge UBT module
(`StratBridge`) owns the responsibilities below. The game module
(`Stratocracy`) cannot: an editor target is a modular build, and the vendored
rules module exports nothing a separate UBT module can call (§3). Of these,
the load mapping and the command surface are built at `0897cb5` in the
Stratocracy UE project repo against the crew half `cb8e12b`; the event list is
not (§3):
```

---

### Pair 25
**Anchor:** §4.9 part 2, what part 2 waits on

**OLD**
```
what part 2 waits on is not specification. **The editor pass**
it waited on landed at `fed8ae9` in the Stratocracy UE project repo (§3), so
what part 2 waits on now is the bridge's own code — the load mapping, the
command surface, the event list, the actor and the widget. The other blocker recorded here was **§4.10's canonical
state hash**, `T-INT-02`'s and `T-INT-03`'s subject, which build-order row 10's
part (b) built at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) (§3).
The harness was recorded here among what part 2 was blocked on, and it took no
week on §4.4's calendar; both blockers this paragraph named have since been
removed, and part 2 is blocked on its own unbuilt code.
```
**NEW**
```
what part 2 waited on was not specification. **The editor pass**
it waited on landed at `fed8ae9` in the Stratocracy UE project repo (§3), and
**part 2's bridge landed at `0897cb5`** in that repo, against the crew half
`cb8e12b`, as the UBT module `StratBridge`: the load mapping and the command
surface are built, and there is **no event list, no actor and no widget**. The other blocker recorded here was **§4.10's canonical
state hash**, `T-INT-02`'s and `T-INT-03`'s subject, which build-order row 10's
part (b) built at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) (§3).
The harness was recorded here among what part 2 was blocked on, and it took no
week on §4.4's calendar. What the bridge's first cross-module call found — a
UBT module exporting one symbol, and 8 × LNK2019 — is recorded at §3 with the
one-shim-per-source repair that carries it.
```

---

### Pair 26
**Anchor:** §4.9 part 2, the subjects the editor-pass IDs need

**OLD**
```
editor-pass IDs need besides it are the subjects named here rather than left to
be discovered at the pass: `T-INT-02` needs a **vendored replayer**, and
`Replay` is ruled out of vendoring until a bridge consumer exists; `T-INT-03`
needs the **command surface**, which is part of the unbuilt bridge; `T-INT-05`,
`T-UI-03` and `T-UI-04` need **real Stratocracy widgets**; and `T-SAVE-06`
is asserted jointly with `T-INT-02`.
```
**NEW**
```
editor-pass IDs needed besides it were the subjects named here rather than left to
be discovered at the pass: `T-INT-02` needed a **vendored replayer**, and
`Replay` was then ruled out of vendoring until a bridge consumer existed; `T-INT-03`
needed the **command surface**, which was part of the then-unbuilt bridge; `T-INT-05`,
`T-UI-03` and `T-UI-04` need **real Stratocracy widgets**; and `T-SAVE-06`
is asserted jointly with `T-INT-02`. `Save` and `Replay` were vendored into
`Source/StratRules/` at `0897cb5` in the Stratocracy UE project repo against
the crew half `cb8e12b`, where the command surface landed with them and
`T-INT-02`, `T-INT-03` and `T-SAVE-06` ran and passed in the editor pass
without closing, their closure waiting on a parity fixture carrying the
complete §4.9 command set (§3); the widgets the other three assert over are
not built.
```

---

### Pair 27
**Anchor:** §4.9 part 2, the `a13626f` measurement's live extent

**OLD**
```
The
`a13626f` measurement above is unmoved by that, and it remains the live
statement about every other subject this passage names.
```
**NEW**
```
The
`a13626f` measurement above is unmoved by that, and it remains the live
statement about the real Stratocracy widgets `T-INT-05`, `T-UI-03` and
`T-UI-04` assert over. It is not the live statement about the vendored
replayer or the command surface: both have since landed, as recorded above.
```

---

### Pair 28
**Anchor:** §4.9 part 2, spec-stub `Inputs:` block

**OLD**
```
         load no unit definition. What T-INT-03 and T-INT-05 still need is
         assigned per ID above, and those are different subjects.
```
**NEW**
```
         load no unit definition. What T-INT-03 and T-INT-05 needed when this
         stub was written is assigned per ID above, and those are different
         subjects.
```

---

### Pair 29
**Anchor:** §4.11, row 9's headless half

**OLD**
```
**`T-INT-01` and `T-INT-04` are green at `e19605e`**, over the vendored
tree at `a13626f`, the standalone gate that asserts `T-INT-04` running under
clang++, and not at the landings that first passed them: `T-INT-01` asserts
identity at `rulesCommit`, and `rulesCommit` moved there, while `T-INT-04`
compiles the vendored copy, whose `Turn.h` bytes changed.
```
**NEW**
```
**`T-INT-01` and `T-INT-04` are green at `9289c1d`**, over the vendored
tree at `0897cb5`, the standalone gate that asserts `T-INT-04` running under
clang++, and not at the landings that first passed them: `T-INT-01` asserts
identity at `rulesCommit`, and `rulesCommit` moved to `cb8e12b`, while
`T-INT-04` compiles the vendored copy, whose sources went from 20 to 24 when
`Save` and `Replay` were vendored.
```

---

### Pair 30
**Anchor:** §4.11, row 9's acceptance set

**OLD**
```
**Row 9's acceptance set does not close**, on the Q29 reading rows 7 and
8 stand on: `T-INT-02`, `T-INT-03` and `T-INT-05` did not run, and among what
they wait on besides the harness that has since landed are a vendored replayer,
the bridge's command surface and real Stratocracy widgets, one per ID (§4.9).
```
**NEW**
```
**Row 9's acceptance set does not close**, on the Q29 reading rows 7 and
8 stand on: `T-INT-05` did not run, and what it lacks is the real Stratocracy
widgets it asserts over (§4.9); `T-INT-02` and `T-INT-03` ran and passed in the
editor pass at `0897cb5` in the Stratocracy UE project repo against the crew
half `cb8e12b`, over a parity fixture carrying `Move`, `Attack` and `EndTurn`
and carrying no `Capture` and no `Build`, which is a run and not a closure (§3).
```

---

### Pair 31
**Anchor:** §4.11, build-order table, row 9's *Depends on* cell, where the two greens stand

**OLD**
```
**both greens now stand at `e19605e`**, over the vendored tree at `a13626f`, re-dated there for their own separate reasons (§3).
```
**NEW**
```
**both greens now stand at `9289c1d`**, over the vendored tree at `0897cb5`, re-dated there for their own separate reasons — `rulesCommit` moving to `cb8e12b`, and the vendored copy going from 20 sources to 24 (§3).
```

---

### Pair 32
**Anchor:** §4.11, build-order table, row 9's *Depends on* cell, the closure dependency

**OLD**
```
They **close on rows 1–5**, which is what this cell used to state as the whole dependency
```
**NEW**
```
They **close on rows 1–5**, which is what this cell used to state as the whole dependency. `T-INT-02` and `T-INT-03` ran and passed in the editor pass at `0897cb5` in the Stratocracy UE project repo against the crew half `cb8e12b` without closing: the parity fixture replayed there carries `Move`, `Attack` and `EndTurn` and carries no `Capture` and no `Build` (§3)
```

---

### Pair 33
**Anchor:** §4.11, build-order table, row 10's *Depends on* cell, part (b)

**OLD**
```
`T-SAVE-06` waits on the editor pass and `T-SAVE-07` on a self-play log written in this format, so this row holds code without closing its set (§3)
```
**NEW**
```
`T-SAVE-06` then waited on the editor pass and `T-SAVE-07` on a self-play log written in this format, so this row held code without closing its set (§3)
```

---

### Pair 34
**Anchor:** §4.11, build-order table, row 10's *Depends on* cell, the row's remaining ID

**OLD**
```
**`T-SAVE-06` is now the only ID this row lacks**, and among what that ID waits on is a vendored replayer: `T-SAVE-06` is asserted jointly with `T-INT-02`, whose replay runs **in-engine**, so the replayer has to be compiled into the engine and therefore vendored, and `Replay` is ruled out of vendoring until a bridge consumer exists. The editor pass this ID also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3).
```
**NEW**
```
**`T-SAVE-06` is still the only ID this row lacks**, and it has run without closing: the replayer had to be compiled into the engine and therefore vendored, `Replay` was vendored into `Source/StratRules/` at `0897cb5` in the Stratocracy UE project repo once the bridge consumer existed, and `T-SAVE-06` passed in the editor pass at that commit against the crew half `cb8e12b`, asserted jointly with `T-INT-02`, whose replay runs **in-engine**. What its closure waits on is a parity fixture carrying the complete §4.9 command set. The editor pass this ID also lacked landed at `fed8ae9` in the same repo (§3).
```

## Change requests

None open.

## Open questions for the Director

1. **Is `GATE-BRIDGE-DEFS` owed a written acceptance ID?** It mints none on the
   `GATE-DATA-VENDOR` precedent, and it is the only check between a reordered
   `units.csv` and a `defIndex` resolving a Build command to the wrong unit
   type, `T-DATA-05`'s unit-table test being order-blind.
2. **Who authors a parity fixture carrying `Capture` and `Build`?** Three IDs'
   closure depends on one, and §4.9 assigns no owner for it. `Capture` needs a
   producer that does not read `AiCommandKind`, which has no such member;
   `Build` needs only a harness that assigns the AI a buildlist.

## Grounding

| Claim | Backed by |
|---|---|
| UE `0897cb5` records `rulesCommit` `cb8e12b`, `dataCommit` `862a225` | fact block, "The commits" |
| Editor pass at `0897cb5`: 8 tests, 8 Success; three new (`T-INT-02`, `T-INT-03`, `GATE-BRIDGE-DEFS`); five ran at `fed8ae9` | fact block, "What ran, and the result" |
| `T-SAVE-06` asserted jointly with `T-INT-02`, in-engine, no headless build closing it | fact block, "What ran, and the result"; §4.10 spec stub `T-SAVE-06` |
| `GATE-BRIDGE-DEFS` mints no acceptance ID | fact block; §3 `GATE-DATA-VENDOR` / `GATE-AI-SMOKE` / `GATE-CAP-PARTIAL` precedent |
| One export, `ThisIsAnUnrealEngineModule`; 8 × LNK2019; compiled and linked for four commits with nothing calling it; a modular editor target is why the game module cannot own the load mapping | fact block, "The defect this round found" |
| `T-INT-04` compiles standalone outside UBT and is not weakened | fact block, same section; §4.9 `T-INT-04` invariant text |
| Earlier defect of the same species (compiles-and-links, editor never launched); the `fed8ae9` removal touched no vendored byte and re-dated neither `T-INT` ID, which §3 and §4.9 part 1 now both state in the past, the re-dating that did occur being on the `0897cb5` vendoring | §3 ledger prose, the `fed8ae9` record; fact block, "CORRECTION" |
| The editor pass did not exist at `b23823f` and exists at `fed8ae9`, so the subjects the editor-pass IDs assert against were unbuilt at that landing and the widgets still are | §3 ledger prose, the `b23823f` and `fed8ae9` records; §4.9 part 1's `fed8ae9` statement; §4.9 part 2's `a13626f` measurement |
| The bridge is the UBT module `StratBridge`, holding the load mapping and command surface, built by one shim per source over anonymous-namespace collisions, no vendored byte edited | fact block, "The repair"; fact block, "What did NOT close" |
| `Stratocracy`'s build rules still list `StratRules` as a public dependency module at `0897cb5`, supplying the vendored combat header the parity harness includes and no callable symbol | round `bridge-scope-5` measurement, F3; Director ruling on CR-4 (link-dependency clause unchanged) |
| Crew `f5fdb69` changed one file, `ue_module/vendored_set.json`, moving `Save` and `Replay` from excluded to vendored, and moved no bytes into `Source/StratRules/`; the bytes entered the UE tree at `0897cb5`, whose vendored copy records `rulesCommit` `cb8e12b` | round `bridge-scope-6` measurement |
| `rulesCommit` `e19605e` → `cb8e12b`; 22 files → 26; 20 sources → 24; ten vendored rules modules → twelve; both `T-INT` IDs re-date; no count moves | fact block, "CORRECTION" |
| Crew `9289c1d` over UE `0897cb5` is the earliest pair meeting both re-dating conditions: 22 files at `a13626f` and at `fed8ae9`, 26 at `0897cb5`, the four added being Save's and Replay's header and implementation; `rulesCommit` `e19605e` at `fed8ae9`, `cb8e12b` at `0897cb5` | round `bridge-scope-5` measurement, F2; Director ruling on CR-2 |
| The re-dating rationale both IDs meet again | §3 ledger prose, the `e19605e` record, quoted in the fact block's CORRECTION |
| Headless at `9289c1d` over `0897cb5`: week-1 PASS `accepted=True`; integration 2/2 with 26 files at `cb8e12b`, 24 sources, 12 implementations, declaration partitioning 13 rules modules as 12 and 1; row 10 part (b) 36/36 with seven `GATE-REPLAY-FIXTURE` clauses | fact block, "Headless, at crew `9289c1d`" |
| Three known-bad inputs and their results; `GATE-REPLAY-FIXTURE` clause behaviour | fact block, "Known-bad inputs" |
| `T-DATA-05`'s unit-table test passed on reversed rows; lookup by Id; order-blind | fact block, "Known-bad inputs", third row |
| `T-INT-05` did not run and lacks the real Stratocracy widgets | fact block, "What did NOT close" |
| Bridge has no event list, no actor, no widget; its load mapping and command surface are built, so the system a ledger row would name half-exists now, and the deferral's trigger reads *whole* at both of the master's statements of it — *the bridge is whole* and *§4.9 part 2 lands whole*, the only two sites that state it | fact block, "What did NOT close"; §4.9 part 2's component list; Director ruling on CR-3 (no row) and on this round's approved change request, *built* → *whole*; coordinator's `bridge-scope-6` sweep of the master for that trigger, two sites and no third |
| No bridge at `a13626f`, and the widgets absent there | §4.9 part 2's own `a13626f` measurement |
| `data/parity_fixture.save` carries `Move`, `Attack`, `EndTurn` only | fact block, "What did NOT close" |
| `AiCommandKind` has no `Capture` member; that fixture's harness assigns no `buildlist`, so `chooseBuild` returns -1 before Fame is consulted, while `Balance`'s view assigns one; `startingFame` 200 a side, Infantry `CostFame` 100, side-0 `Factory` hex with `IsSpawnPoint` at column 1 row 4, `queueBuild` refusing only below cost | round `bridge-scope-5` measurement, F1 |
| `Balance` not vendored; the 2026-08-05 ruling spent for `Save` and `Replay` | fact block, "What did NOT close"; §3, the naming record that rules the module `Balance` |
| `StratRules` absent from the `Modules` array; `StratBridge` listed with a real `IMPLEMENT_MODULE` | fact block, "What did NOT close" |
| Counts unmoved at 71 / 62 / 9, row 9 at 3, row 10 at 1 | §4.5's stated figures; Director ruling on CR-1 (no closure) |
| A partial pass is a run and never a closure | §4.7 register, Q29; §4.11 row 9's *Depends on* cell |
| Crew-side repair at `9289c1d`, eleven sites; *"they do not run here"* kept | fact block, "The crew-side repair at `9289c1d`" |
| The same commit introduced fourteen clauses across ten files — two runner modules, three test and harness sources, the README and four spec documents — asserting that `T-SAVE-06` and `T-INT-02` closed, each beside a true negative that stands | round `bridge-scope-5` measurement, F4, its file breakdown re-measured in round `bridge-scope-6` |
| The two unamendable commit messages and what contradicts them: UE `0897cb5` on "do not re-date" and on `cb8e12b` as the green commit; crew `9289c1d` on `Selfplay`, the declaration having named the module `Balance` since `e19605e` | round `bridge-scope-5` correction record, with F2; §3, the naming record; `ue_module/vendored_set.json` modified at two commits only, `e19605e` and `f5fdb69`, with `Balance` among the `excluded` keys at `e19605e` (round `bridge-scope-6`) |
