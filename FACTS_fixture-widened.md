# Fact block — round `fixture-widened`

One file. The author and the gate are both given this path and nothing else as
supplied fact. It is appended to, never trimmed.

**If a fact in this block looks wrong, say so instead of writing around it.**
Three of the last round's blocking findings were facts of mine that the gate,
holding the same block, was structurally unable to challenge. Only the author
can be this block's adversary. Ask of every negative here: *true of what,
exactly?*

---

## 0. What the round is

Crew `c2f5860` widened the committed parity fixture, and UE `4ceaf93`
re-vendored it. That falsifies present-tense statements in the merged master
about what that file carries and why the two commands were missing from it. The
round amends those statements. It closes nothing and moves no count.

`source/gdd.md` md5 `1bfae9f169230f3bdcea4fab48b100f8`, which is the master as
merged at content `6451309`.

## 1. Disambiguation — the round's own subject nouns

These are not standing vocabulary. They are the words this round turns on, and
two of them name different things in different sentences of the master.

- **"the parity fixture"** in this block always means the committed file
  `data/parity_fixture.save`, which the editor pass replays. It never means the
  hand-authored canonical log inside `test_replay.cpp`, which is a different
  artifact, already carried all five command kinds before this round, and is
  unchanged by it. **The master makes a completeness claim about each of them**,
  and only one of the two is affected here.
- **"carries"** is a present-tense property of the committed file *now*. It is
  not what the `0897cb5` editor pass ran over. That pass ran over the file as it
  then stood, so a sentence pinned to that run states something still true; a
  sentence describing the file in the present does not.
- **"the complete §4.9 command set"** is `Move`, `Attack`, `Build`, `Capture`,
  `EndTurn`. A sentence containing this phrase is not thereby about the parity
  fixture — read which log it predicates on.
- **"waits on"** — what a closure waits on has changed. Whether anything now
  closes has not: see §5.

## 2. The fixture, measured from the committed bytes of each commit

Recomputed by parsing each committed blob, not read off a runner's printout.

| | at crew `5072d10` | at crew `c2f5860` |
|---|---|---|
| bytes | 4,835 | 12,745 |
| commands | 64 | 169 |
| `Move` | 28 | 49 |
| `Attack` | 26 | 74 |
| `Build` | absent | 22 |
| `Capture` | absent | 12 |
| `EndTurn` | 10 | 12 |
| distinct `turn` values | 1–6 | 1–7 |
| `stateHash` | `ae0e12a8dfe66bf0` | `1044f6ec0c455fdd` |
| `result` | `Decisive` | `Decisive` |

The winning side is 0 in both, and the result's tier and cause are unmoved.

## 3. The mechanism of each command's former absence, and what changed

**`Capture`.** `AiCommandKind` was, and still is, `{Build, Move, Attack,
EndTurn}`. It has no `Capture` member and did not gain one: `Ai.h` keeps capture
completion a turn-boundary event owned by row 4. So the statement that nothing
reading that enum can emit a `Capture` is **unchanged and still true**. What
changed is that `appendAiTurn` now appends one `Capture` per side per turn at the
close of that side's turn — the log carries the kind without the AI having
produced it. §4.10 requires a `unit` field on `Capture` that `applyCommand` never
reads; the side's lowest unit id with `canCapture` is written.

**`Build`.** `aiViewOf` never assigned `s.buildlist`, so `chooseBuild` iterated
an empty list and returned -1 **before Fame was consulted**. `aiViewOf` now
supplies `Infantry`, looked up by `Id`. Fame sufficiency was never what stopped
it, and the master's statement to that effect is unchanged.

**What the buildlist holds beyond `Infantry` is measured to be inert here.**
`{Infantry}`, `{Infantry, Tank}` and all four unit types each emit a
byte-identical fixture, because Q9 orders the affordable set by ascending cost
and `Infantry` is the cheapest of the four.

**The appended `Capture` does work rather than decorating the log.**
`captureTurns` is 1 on the shipped scenario and `openTurn` already ticks capture
when a turn opens, so the appended tick changes nothing on an objective the side
already held. What it catches is an objective the side moved onto during the turn
just played.

## 4. The two landings

**Crew `c2f5860`** (on `main`, pushed). Changed `cpp_reference/test_replay.cpp`
and `data/parity_fixture.save`. `kParityTurns` 14 → 48; it counts **side-turns**,
`turnCap` is 20 **game** turns, and 40 side-turns is therefore the ceiling no
match on this scenario can exceed.

**UE `4ceaf93`** (on `master`, pushed). Changed `Data/StratData.manifest.json`
and `Data/parity_fixture.save`, and those two paths only. `dataCommit`
`862a225` → `c2f5860`. `rulesCommit` is `cb8e12b` at both `0897cb5` and
`4ceaf93`. Among the vendored data, only the fixture moved: `units.csv`,
`terrain.csv`, `effectiveness.csv` and `ferrum_crossing.json` are byte-identical
across the two vendorings.

**Also on `main`, and not this round's subject:** crew `b5f524d` deleted the
fourteen false closure clauses that `9289c1d` introduced across ten files. §3
already records that those fourteen exist and are false; it does not record that
they have since been deleted.

## 5. What did NOT happen — stated as negatives, with their extent

- **`T-INT-02` did not close, and has not re-run.** Its in-engine run is the
  editor pass, and no editor pass has been run since `0897cb5`. The widening
  changes what its closure waits on; it does not supply the run.
- **`GATE-DATA-VENDOR` was not run.** What was measured instead, outside the
  harness that asserts it, is that all five `sha256` entries in
  `Data/StratData.manifest.json` equal the vendored bytes at `4ceaf93`. That is
  the invariant that gate asserts. It is not that gate having run.
- **`T-INT-03` is not reached by the widening.** It asserts over the bridge's
  command surface — commands submitted in-engine — and not over this file.
- **`T-INT-01` and `T-INT-04` do not re-date on `4ceaf93`.** No file under
  `Source/StratRules/` changed there and `rulesCommit` did not move.
- **No acceptance ID closed and no count moves.** 71 / 62 / 9 stand, row 9 at 3,
  row 10 at 1.
- **No §3 ledger row is created, flipped or removed.**

## 6. Facts about the work, which no command will re-derive

- I merged the `bridge-scope` addendum first (content `6451309`), then made the
  crew and UE changes. The master therefore states, in the present tense, a set
  of facts that my own later commits falsified. The round exists for that reason
  and not because the merged text was wrong when it was gated.
- **The widening is mine, and no Director ruling authorised its details.** The
  buildlist's contents were chosen on `test_balance.cpp`'s precedent after
  measuring the choice inert; the `Capture` append and the `kParityTurns` value
  were engineering calls. If any of the three belongs in the document as a
  ruling rather than as a measurement, say so and file it as a question.
- **Two premises of the brief I worked from did not survive measurement.**
  It held that `kParityTurns = 14` would truncate the widened log: the widened
  log uses 13 of 14. And it held that the bound had to rise because
  reinforcements push the match past it; the bound was raised because 40
  side-turns is the `turnCap` ceiling, which is a different reason. Neither
  premise is in the master, so neither is a repair target — they are here so
  that a reader of this block does not inherit them.
- **A defect found only by running it:** without a `turn.running` guard the
  emitter logged a `Capture` after the match was already over, because a match
  can end mid-turn on an `Attack` and the AI then returns `EndTurn`, which
  `applyCommand` refuses while `Capture` cannot refuse. Guarded. This is why the
  `Capture` count is 12 and not 13.

## 7. Gate results measured at crew `c2f5860`

- The replay row gate **failed `GATE-REPLAY-FIXTURE` clause (g) alone** against
  the stale committed fixture before the re-emit, and passes **36/36** after.
  That is the pre-change run against the known-bad input: the check can fail.
- Week-1 gate PASS, `accepted=True`. Integration gate 2/2.
- The re-emit reproduces the committed bytes.

## 8. The candidate set

`source/SWEEP_fixture-widened.md` holds 35 sentences from the master, matched
mechanically on a whitespace-collapsed copy. Its own header states what
membership does and does not assert. It is a starting point and not the scope;
the claim it looks for has spellings the probe cannot match.

---

## 9. CORRECTION, added after gate run `fixture-widened-1`

**§3 of this block said of `Build`'s former absence: "Fame sufficiency was never
what stopped it, and the master's statement to that effect is unchanged."** The
second half of that was my call and not a measurement, and the author has
overruled it with reason. The master's sentence asserts nothing false — its
figures are standing data facts and none of them moves — but it is written in the
present tense about a thing that is no longer being stopped, so it sits stranded
after the amendment that says the fixture now carries `Build`. The author
extended a pair's OLD through it and moved one verb to the past.

The original claim is left quoted above rather than edited away, so a later
reader can tell an author's decision from a supply bug. **This one is mine.** The
author was told to challenge this block rather than write around it, and did.

**What is still measured and unmoved:** `startingFame` 200 a side, Infantry's
`CostFame` 100, and side 0's ownership of the `Factory` hex with `IsSpawnPoint`
are properties of the shipped data and are true in the present tense. If an
amendment puts any of those three into the past, that is a new false claim rather
than a repair.
