# Gate report — run `bridge-scope-4`

`source/MANIFEST.txt` present. `gdd.md` md5 `417a3ad795303c1012dd84520108499a`.
One section produced this stage: `sections/tech_bridge-scope.md`, 34 pairs.

## sections/tech_bridge-scope.md — PASS (0 violations)

No violation is filed. The record below states what was measured, so that a
later run can tell a clean check from an unrun one.

### The finding carried in from `bridge-scope-3`

The previous run's single violation was that §4.9 part 2's opening lead-in
(`source/gdd.md` lines 2894–2895) read

    **2. Bridge — the only code that knows both worlds.** The game module
    (`Stratocracy`) owns:

while the draft's own record put the load mapping in the `StratBridge` UBT
module. Pair 24 takes that lead-in. Its OLD is verbatim and unique in
`source/gdd.md` (one occurrence, lines 2894–2895). Its NEW assigns the
responsibilities to `StratBridge`, states why the game module cannot own them
— a modular editor target plus a rules UBT module exporting one symbol — and
cites §3.

### The four bullets the lead-in governs

The lead-in ends in a colon and governs four bullets, none of which the draft
edits. Each was checked against the fact block for whether the re-attribution
asserts something the round did not build.

| Bullet (`source/gdd.md`) | Ruling |
|---|---|
| **Load** (2896–2898) | Lead-in states it built at `0897cb5`. Fact block, "What did NOT close": *"The load mapping and the command surface exist."* Same granularity as the source. |
| **The authoritative `strat::GameState`** (2899–2900) | Not claimed built by the lead-in. `ue_module/vendored_set.json`, quoted in the fact block: *"the bridge consumes GameState, the command surface and the canonical state hash"*. |
| **Command in / events out** (2901–2909) | The bullet holds both the command surface and the event list. The lead-in disaggregates them exactly: *"the load mapping and the command surface are built … ; the event list is not (§3)"*. Fact block: *"There is still **no event list**, no actor and no widget."* Forbidden species 4 is not produced. |
| **Threading** (2910–2914) | A runtime-path constraint, carried at the same modality it had under the `Stratocracy` attribution. Nothing measured contradicts it. |

What the re-attribution drags with it was checked at three further sites:

- `source/gdd.md` 2990–2991 (§4.9 spec stub) already reads *"the unit
  definitions the bridge maps from FUnitRow (part 2 above)"* — it attributes
  the mapping to "the bridge" generically, so Pair 24 does not falsify it.
- `source/gdd.md` 2959–2961, *"`FUnitRow`, `FTerrainRow` and
  `FEffectivenessRow` — all of them in the `Stratocracy` module and none in
  `Source/StratRules/`"*, is about the DataTable row structs, not about who
  maps them. Unaffected.
- `source/gdd.md` 2867–2869, *"`StratRules` is now a **link dependency of the
  `Stratocracy` module**"*, is the remaining claim about that module's build
  relationship to `StratRules`. The draft files it as a change request rather
  than restating it in prose, which is the correct disposal for an unmeasured
  claim; a change request is not a violation.

### Checks run across the whole draft

- **Pair OLD blocks.** All 34 located in `source/gdd.md`, each verbatim and
  each occurring exactly once. Multi-line OLDs (Pairs 21, 22, 23, 24, 25, 26,
  27, 28) were checked line-for-line including indentation inside the §4.9
  spec-stub code block (Pair 28, lines 2995–2996). Pair 32's OLD ends at a
  table-cell boundary (` | ` follows on line 3218), so its appended sentence
  merges mechanically.
- **Surviving present-tense blocker claims** (forbidden species 2). Every
  occurrence of `T-INT-02`, `T-INT-03` and `T-SAVE-06` in `source/gdd.md` was
  enumerated with a context window. Every live "waits on / still needs /
  lacks / is blocked by" site is taken by a pair: lines 1516 (Pairs 2, 5, 8),
  1569 (Pair 13), 1577 (Pairs 14, 15), 1589 (Pairs 18, 20), 3219 (Pairs 33,
  34). The remainder are commit-pinned §3 landing records at `b23823f`,
  `d837fc8` and `ec15be6`, or quoted gate-runner output, and were stale before
  this round rather than made so by it.
- **The re-dating sweep.** Every `e19605e` site in `source/gdd.md` was
  enumerated. The live credit sites are taken by Pairs 7, 12, 16, 17, 19, 22,
  29 and 31; the rest are that landing's own §3 record or verbatim PASS-line
  quotes pinned at `d837fc8` and `e19605e`, which the fact block's CORRECTION
  leaves standing. Same for `22 files` / `20 sources` / `ten crew modules`:
  the one live site is Pair 6, the others are pinned verbatim quotes.
- **Counts.** `source/gdd.md` line 1589 reads *"**62** of the 71 are green"*.
  The draft holds 71 / 62 / 9, row 9 at 3 and row 10 at 1, and states it in
  Pair 11. Forbidden species 6 not produced. Pair 17 keeps the by-commit
  figure at **2** and moves only the commit, so §4.5's partition still sums.
- **Ledger rows.** Pair 11 states *"No ledger row is created, flipped or
  removed by this landing"*; the two deferred rows are put to the Director as
  a change request. Forbidden species 7 not produced.
- **Closure discipline.** No ID is stated as closed anywhere in the draft
  (species 1). `T-INT-05` is stated as not having run at Pairs 11, 18, 26 and
  30 (species 3). The bridge is stated partly built with its missing parts
  named in the negative at Pairs 11, 22, 24, 25 (species 4, 8). The fixture's
  command coverage — `Move`, `Attack`, `EndTurn`, and no `Capture` and no
  `Build` — is stated at Pairs 11, 30 and 32 (species 5).
- **Pinning.** Every "has since" construction in the draft (Pairs 13, 15, 27)
  names the commit or commit pair it rests on. The new UE-repo sha `0897cb5`
  is never hyperlinked to the crew repo; the crew shas `cb8e12b`, `862a225`,
  `f5fdb69`, `5c47cc1` and `9289c1d` are. §3's own convention for commits
  cited after `ec15be6` — *"each commit cited since is pinned at the landing
  that cites it"* (line 1533) — is satisfied by Pair 11.
- **Naming.** The unvendored rules module is `Balance` at every site;
  `selfplay` appears only as the file path `cpp_reference/selfplay.cpp`.
- **Arithmetic.** Pair 21's twelve enumerated rules modules × 2 files, plus
  `StratRules.Build.cs` and the manifest, is the 26 files Pair 22 and Pair 11
  report; 24 sources and 12 standalone implementations follow.
- **Grounding.** Every row of the grounding table was matched to a claim in
  the draft, and every substantive claim in the draft to a row or to a
  quotable sentence of `source/gdd.md`. No ungrounded substantive claim found.
- **Format.** Placement, Draft, Change requests, Open questions, Grounding all
  present. One section this stage, so no placement collision is possible; the
  five named anchors do not overlap each other.
- **kb-desync.** The draft touches §3, §4.4, §4.5, §4.9 and §4.11 only.
  `kb_rules.md` is a parse of §2 and `kb_setting.md` of the setting material;
  neither is put wrong by these pairs.

## Verdict

**PASS.** `sections/tech_bridge-scope.md` carries zero violations, so the
top-level verdict for run `bridge-scope-4` is PASS and the draft is clear to
merge. The one finding carried in from `bridge-scope-3` is closed at the
source: Pair 24 replaces the §4.9 part 2 lead-in that named the `Stratocracy`
game module as owner, its OLD is verbatim and unique, and the four bullets it
governs each survive the re-attribution — the load mapping and the command
surface are claimed built and the fact block says they exist, the event list is
named as not built, and the GameState and Threading bullets are carried as
specification without a built-claim. Before merge the Director owes rulings on
the four change requests the draft files, of which two are load-bearing for
this addendum's own numbers: whether `T-INT-02`, `T-INT-03` and `T-SAVE-06`
close on this run under Q29, and whether crew `9289c1d` over UE `0897cb5` is
the right re-dating target for `T-INT-01` and `T-INT-04` rather than the
earliest qualifying pair, which is not measured. Neither ruling is the gate's
to take, and neither blocks the merge of the text as written.
