# FACT BLOCK — round `bridge-scope`

Every fact below was measured in this session against the trees named. Nothing
here is recalled. The author and `continuity-gate` both get this file, unchanged.

---

## Disambiguation — the round's own subject nouns

These collide inside this round specifically. Use the disambiguated form every
time; do not rely on context to carry the distinction.

- **UBT module** vs **rules module.** `StratRules`, `Stratocracy` and the new
  `StratBridge` are *UBT modules* — Unreal build units, each a DLL in an editor
  build. `Combat`, `Replay`, `Save`, `Scenario` … are *rules modules* — the
  `namespace strat` C++ units. This round is about a UBT module boundary, and a
  sentence that just says "module" will be read as the wrong one.
- **the parity fixture** vs **the fixture tables.** *The parity fixture* is
  `data/parity_fixture.save`, one committed §4.10 save. *The fixture tables* are
  the hand-built `UnitDef`/`TerrainDef` vectors inside `test_replay.cpp`, which
  are NOT loaded from `data/`. Both are called "fixture" in existing prose.
- **vendored into `Source/StratRules/`** vs **vendored into `Data/`.** Two
  separate paths, two scripts, two manifests, two `*Commit` fields. `T-INT-01`
  asserts over the first only; `GATE-DATA-VENDOR` over the second only.
- **export.** C++ symbol export from a DLL. Nothing to do with exporting data.
- **the editor pass.** The in-editor Unreal Automation suite (Ruling AF's name).

---

## The commits

| repo | sha | what |
|---|---|---|
| crew | `f5fdb69` | Save and Replay vendored into the UE project |
| crew | `cb8e12b` | `seedFromScenario`; the `rulesCommit` the UE tree records |
| crew | `862a225` | the parity fixture emitted; the `dataCommit` the UE tree records |
| crew | `5c47cc1` | `sync_stratdata.py` carries the parity fixture |
| crew | `9289c1d` | the stale-claim repair (below) |
| UE | `fed8ae9` | the editor pass landed (prior round) |
| UE | `0897cb5` | the bridge, and the editor pass run this round records |

At UE `0897cb5`: `Data/StratData.manifest.json` records `dataCommit` `862a225`;
`Source/StratRules/StratRules.manifest.json` records `rulesCommit` `cb8e12b`.

## What ran, and the result

**The editor pass at UE `0897cb5`: 8 tests, 8 Success.** Three are new:

- `T-INT-02` — `Stratocracy.StratBridge.T-INT-02.ReplayParityWithHeadless`
- `T-INT-03` — `Stratocracy.StratBridge.T-INT-03.RejectionSafety`
- `GATE-BRIDGE-DEFS` — `…GATE-BRIDGE-DEFS.MappedDefsMatchLoaderOrder`

Five already ran at `fed8ae9`: `GATE-DATA-VENDOR`, and `T-DATA-05` in four
tests (unit table, terrain table, effectiveness table, enum mirror).

**`T-SAVE-06` RAN and PASSED jointly with `T-INT-02` at UE `0897cb5`. It did NOT
close, and neither did `T-INT-02` or `T-INT-03`.** An earlier revision of this
block said "closed"; that was wrong and is corrected here. §4.11's row-9 cell
says `T-INT-02/03/05` *"re-open on the `Capture`/`Build`/`EndTurn`"* and *"close
on rows 1–5"*, and Q29's standing ruling says *"a partial pass is reported as a
run and never as a closure"*. The parity fixture carries Move, Attack and
EndTurn and lacks Capture and Build, so this landing is a run.

What closure waits on is a parity fixture carrying the complete §4.9 command
set. `T-SAVE-06` is asserted jointly with `T-INT-02` and is in-engine; no
headless build closes it.

**`GATE-BRIDGE-DEFS` mints no acceptance ID**, on the `GATE-DATA-VENDOR` /
`GATE-AI-SMOKE` / `GATE-CAP-PARTIAL` precedent.

**Headless, at crew `9289c1d` over the UE tree at `0897cb5`:** week-1 gate PASS,
`accepted=True`; integration gate PASS 2/2 — `T-INT-01` reports all **26** files
in `Source/StratRules/` accounted for at `cb8e12b` (24 sources plus
`StratRules.Build.cs` and the manifest; the declared vendored set partitions the
13 crew rules modules as 12 vendored, 1 ruled out), and `T-INT-04` compiles the
**12** vendored rules-module implementations standalone under clang++, outside
UBT. The GDD currently records 22 files, 20 sources and 10 modules at `e19605e`
— see the CORRECTION below.
Row 10 part (b) is 36/36 including seven `GATE-REPLAY-FIXTURE` clauses.

## The defect this round found, and it is the substance of the record

`Source/StratRules/` is a UBT module. An editor target is a **modular** build,
so every UBT module is its own DLL, and Unreal exports only symbols carrying an
`_API` macro. The vendored rules-module sources carry none — §4.9 forbids them
engine headers. Measured with `dumpbin /EXPORTS`:

    UnrealEditor-StratRules.dll  ->  1 export: ThisIsAnUnrealEngineModule

So that UBT module could never satisfy a cross-module call. The first code that
tried — the bridge — failed with **8 × LNK2019**. It had been true and unseen
for four commits, because nothing had ever *called* it.

`T-INT-04` cannot catch this and is not weakened by it: it compiles the rules
modules **standalone, outside UBT**, which is a different question from whether
a UBT module exposes them.

This is the same species as the defect §3 already records — the round that
registered `StratRules` gated that it *compiles* and *links* and never launched
the editor. The repair that followed left it *"still built, still linked"*, and
that sentence was true and still one transition short. Compile → link → load →
**call**.

**The repair:** the bridge is its own UBT module, `StratBridge`, with the
vendored rules-module sources compiled into it by one shim per source (one each
because several rules modules declare same-named helpers in anonymous
namespaces, which collide in a single translation unit). No vendored byte is
edited by the repair — the shims `#include` `Source/StratRules/`.

## CORRECTION — `T-INT-01` and `T-INT-04` DO re-date

An earlier revision of this fact block said they do not. **That was wrong**, and
it was wrong in the direction that matters: it asserted a negative that the
document's own convention contradicts. The corrected facts, measured:

- `Source/StratRules/StratRules.manifest.json` records `rulesCommit`
  `e19605e` → **`cb8e12b`**.
- The vendored set grew when `Save` and `Replay` were vendored at `f5fdb69`:
  **22 files → 26**, **20 sources → 24**, **10 vendored rules modules → 12**.
  `T-INT-04` now compiles **12** implementations standalone, not 10.

§3 states the rationale for the last re-dating in as many words: *"`T-INT-01`
because it asserts identity at `rulesCommit`, which moved there, and `T-INT-04`
because it compiles the vendored copy, whose `Turn.h` bytes changed."* Both
conditions are met again here, so by the document's own stated logic both IDs
re-date.

**Neither re-dating moves any count.** Both are already green; what moves is the
commit each green is credited at. This is a closure movement, not a widening —
neither ID's written text changed.

**The pair measured post-commit is crew `9289c1d` over the UE tree at
`0897cb5`.** Whether the credit should instead pin to the earliest qualifying
pair is not settled here; if the draft cannot state a re-dating target from
measured evidence alone, file it as a change request rather than choosing one.

## Known-bad inputs — the gate was shown to fail

Three, each restored afterwards:

| input | result |
|---|---|
| parity fixture's `stateHash` altered, manifest untouched | `T-INT-02` FAIL and `GATE-DATA-VENDOR` FAIL |
| the same forgery, manifest **updated to match** | `GATE-DATA-VENDOR` passes; **`T-INT-02` FAILS ALONE** |
| `units.csv` row order reversed, manifest updated | `GATE-BRIDGE-DEFS` FAIL |

The second is what shows `T-INT-02` asserting on its own rather than riding the
vendor gate's sha256.

The third recorded something not previously known: **`T-DATA-05`'s unit-table
test PASSED on reversed rows.** It looks each row up **by Id** and never
compares order, so it is structurally order-blind. `GATE-BRIDGE-DEFS` is
therefore the only check in the project standing between a reordered table and a
`defIndex` that silently resolves a Build command to the wrong unit type.

On the crew side the same discipline was applied before the fixture existed:
with the parity fixture absent, `GATE-REPLAY-FIXTURE` blocked on clauses
(b)(c)(e)(f)(g) while (a) and (d) passed; against the bundled buggy replayer it
blocks on (f) and (g) while (a)–(e) pass.

## What did NOT close, and what is NOT true

- **`T-INT-05` did not run.** What it lacks is the real Stratocracy widgets it
  asserts over.
- **The bridge is partly built, not built.** The load mapping and the command
  surface exist. There is still **no event list, no actor and no widget**.
- **`T-INT-02`'s replay exercises Move, Attack and EndTurn only.** The parity
  fixture carries no Capture and no Build command, and no constant can change
  that: `AiCommandKind` is `{Build, Move, Attack, EndTurn}`, so its producer
  cannot emit a Capture at all, and Build never becomes affordable on the
  shipped scenario.
- **The `Balance` rules module is still not vendored.** Use that name: an
  earlier revision of this block called it `Selfplay`, which names no rules
  module. §3 records that it could not be named `Selfplay` — the build
  filesystem is case-insensitive and the tracked `cpp_reference/selfplay.cpp`
  would be the same file — so the module is `Balance`. `selfplay.cpp` is a
  separate tracked file, excluded from vendoring for a different reason (a UBT
  module cannot hold a second `main()`).

  The 2026-08-05 ruling deferred vendoring until §4.9 part 2 supplied a
  consumer; that consumer was built and Save and Replay were vendored at
  `f5fdb69`, so the ruling is *spent* for those two. It still describes the tree
  for `Balance`, and `ue_module/vendored_set.json` says why in as many words:
  the bridge consumes GameState, the command surface and the canonical state
  hash, and consumes no self-play log producer.
- **`StratRules` is still absent from `Stratocracy.uproject`'s `Modules` array**,
  deliberately. `StratBridge` is listed and carries a real `IMPLEMENT_MODULE`.

## The counts (verified against the synced `source/gdd.md` this session)

Currently: **71** written acceptance IDs, **62** green, **9** unclosed — **3** in
row 9 (`T-INT-02`, `T-INT-03`, `T-INT-05`) and **1** in row 10 (`T-SAVE-06`).

**This round closes NOTHING, so NO COUNT MOVES.** Written stays **71**, green
stays **62**, unclosed stays **9**, row 9 stays at **3**, row 10 stays at **1**.
No §3 ledger row is created or flipped. Row 10 is a PROPOSED build-order row
(§4.11) and has no §3 ledger row to flip in any case.

An earlier revision of this block computed green 62→65, unclosed 9→6, row 9 3→1
and row 10 1→0 on three closures. **Those moves are withdrawn**, for the reason
in "What ran, and the result" above: under §4.11's row-9 cell and Q29 this is a
run, not a closure.

If the Director rules the other way on Q29, those are the moves that would
follow — which is why the numbers are kept here, as the quantified content of a
change request rather than as this round's record.

`T-INT-01` and `T-INT-04` re-date (see the CORRECTION above) and this moves no
count either: both were already green, and a closure movement is not a widening.

## The crew-side repair at `9289c1d`

Eleven sites said the bridge did not exist, that `T-INT-02` waited on a vendored
replayer a ruling deferred, that `T-INT-03` waited on an unbuilt command
surface, that no in-editor Automation harness or editor pass existed, or that
`T-INT-02`/`T-INT-03` lacked the subjects they assert over. All repaired.
Sentences of the form *"they do not run **here**"* are still true of every
headless suite in the crew repo and were kept.

---

## Error species this round must not produce

The subject is **closure** and **what a gate can see**. Forbidden:

1. Stating that an ID closed without naming the commit — or, where the closure
   spans both repos, the commit **pair** — it closed at.
2. Any surviving present-tense claim that `T-INT-02`, `T-INT-03` or `T-SAVE-06`
   *waits on*, *lacks*, or *is blocked by* anything.
3. Writing or implying that the editor pass now runs the whole of row 9.
   `T-INT-05` did not run.
4. Writing or implying the bridge is complete.
5. Implying `T-INT-02`'s replay covers all five §4.9 command kinds.
6. Moving the **71** written-ID count.
7. Flipping a §3 ledger row. State the acceptance-set status; if a flip looks
   available, register the question for the Director instead of taking it.
8. Weakening a true negative to make a sentence flow. Where something did not
   close, say so in the negative and name what it lacks.
