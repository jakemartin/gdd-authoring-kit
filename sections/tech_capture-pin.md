# Technical design — capture-pin addendum (tech-director)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.** Both pairs were applied to
> `Stratocracy_Prototype_GDD.md`. Re-applying them would fail: each `OLD` block
> is absent from the master, which is the post-check this merge ran.

## Placement
Both pairs replace text in §3; nothing outside §3 moves.

## Draft

### Pair 1

**OLD**

```
The fixture carries the kind because `appendAiTurn` appends one `Capture` per side at the close of that side's turn, outside the AI's choice: `openTurn` already ticks capture on an objective the side held, so what the appended command catches is an objective the side moved onto during the turn just played.
```

**NEW**

```
The fixture carries the kind because `appendAiTurn`, as at crew [`11ef8ce`](https://github.com/jakemartin/stratocracy-crew/commit/11ef8ce), appends a `Capture` at the close of a side's turn, outside the AI's choice: `openTurn` already ticks capture on an objective the side held, so what the appended command catches is an objective the side moved onto during the turn just played. That append is conditional rather than automatic — `g.turn.running` must be true at that close, among other conditions the emitter applies — so the cadence follows the turn loop and not the turn count. In the fixture committed at [`c2f5860`](https://github.com/jakemartin/stratocracy-crew/commit/c2f5860) the append landed at every side-turn of turns 1 through 6, so the set of `{turn, side}` pairs carrying a `Capture` is identical to the set carrying an `EndTurn`: twelve pairs, each carrying a `unit`. Turn 7 carries neither kind for either side — the log's final entry is `{"turn": 7, "side": 0, "kind": "Attack"}`, the save's `result` reads `Decisive`, and that side-turn's eleven commands fall short of the emitter's 32-iteration bound; what follows from that record is that the match ended during that side-turn, so `g.turn.running` was false when the AI returned `EndTurn`.
```

Note: the unqualified per-side-per-turn cadence is replaced by a cadence tied to the turn loop, with `g.turn.running` named as one necessary condition among others rather than as a closed list, per the CORRECTION to FACT 2; the fixture is named at `c2f5860` and the emitter at `11ef8ce` per the CORRECTION to FACT 1; the twelve appends, the turn-7 entry, `result` and the command counts are FACT 1, the 32-iteration bound is FACT 2, the turn-7 explanation is written as what follows from that record because FACT 2 records it as INFERRED, and FACT 3 carries the replaced sentence.

### Pair 2

**OLD**

```
The tree was corrected at the crew tip; the message cannot be.
```

**NEW**

```
The tree was corrected in the crew repo at [`5072d10`](https://github.com/jakemartin/stratocracy-crew/commit/5072d10), subject line `Name the unvendored module Balance, not Selfplay`, which changed `crew/tools.py` alone. The message cannot be corrected.
```

Note: "the crew tip" is a referent that moves, so it is replaced by the commit that made the correction, its subject line and the file it changed — FACT 5 for those three, its CORRECTION for keeping the ancestry and the since-list out of the master, and FACT 6 for the replaced sentence.

## Change requests
None.

## Open questions for the Director
None.

## Grounding

| Claim | Backed by |
|---|---|
| Pair 1's OLD is present in the master | §3, *"The fixture carries the kind because `appendAiTurn` appends one `Capture` per side at the close of that side's turn"* — recorded at FACT 3 |
| Pair 2's OLD is present in the master | §3, *"The tree was corrected at the crew tip; the message cannot be."* — recorded at FACT 6 |
| `appendAiTurn` requires `g.turn.running` true, applies further conditions beyond it, and runs a loop bounded at 32 iterations per side-turn, as at `11ef8ce` | FACT 2 and its CORRECTION, measured from `cpp_reference/test_replay.cpp` in `stratocracy-crew` |
| The fixture's twelve `Capture` appends, the identity of its `Capture` and `EndTurn` `{turn, side}` sets over turns 1 through 6, the final entry `{"turn": 7, "side": 0, "kind": "Attack"}`, the `result` `Decisive` and the eleven commands of turn 7 side 0 | FACT 1, measured from `data/parity_fixture.save` in `stratocracy-crew` |
| The match ended during turn 7 side 0, so `g.turn.running` was false when the AI returned `EndTurn` — written as what follows from that record | FACT 2, labelled INFERRED |
| The fixture is committed at `c2f5860`, not at `11ef8ce` | CORRECTION to FACT 1 and its CORRECTION; §3 names that commit for the fixture in its own wording, *"The committed fixture carries the complete §4.9 command set at"*, where the commit follows as a Markdown link |
| `5072d10` carries the subject line `Name the unvendored module Balance, not Selfplay` and changed `crew/tools.py` alone | FACT 5, measured from `git` in `stratocracy-crew` |
