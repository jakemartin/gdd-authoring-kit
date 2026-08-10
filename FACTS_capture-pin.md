# FACTS — round `capture-pin`

Every fact below was measured this round, on the working copies named. Facts are
labelled **MEASURED** (read off a file or a git object) or **INFERRED** (follows
from measured facts plus code that was read). Do not promote an INFERRED fact to
a bare assertion in the master.

Append to this file; never trim it. If a fact here is wrong, mark the correction
**in place, beside the original**, rather than editing the wrong claim away.

Repos at the time of measurement:

| repo | branch | HEAD |
|---|---|---|
| `stratocracy-content` | `main` | `9a7197c` |
| `stratocracy-crew` | `main` | `11ef8ce` |
| `Stratocracy` (UE) | `master` | `4ceaf93` |
| `gdd-authoring-kit` | `master` | `7d22faf` |

`source/gdd.md` md5 `454d765e3bac6c02e3491c105328c7be`, matching the merged
master. All sweeps below were run newline-insensitively over that file, because
the master is hard-wrapped and a line-oriented sweep under-counts silently.

---

## Subject nouns — disambiguate these before writing

This round's own vocabulary collides with the document's standing vocabulary.
Each of these means two different things in the master, and the round's prose
must make clear which is meant at every use:

- **"close"** — (a) the close of a *side's turn*, the moment `appendAiTurn`
  acts on; (b) *closure of an acceptance ID*, the ledger sense used throughout
  §3, §4.4, §4.5, §4.9 and §4.11. The sentence this round amends contains sense
  (a) while sitting in a section saturated with sense (b).
- **"Capture"** — (a) the §4.9 command kind recorded in a §4.10 log; (b) the
  §2.7 game action of holding a tile; (c) the `CanCapture` §4.8 unit-table
  column. This round is about (a) and touches (c) only as the emitter's filter.
- **"the tree"** — the master uses this bare form for the *crew* tree and for
  the *vendored* tree both. The explicit form `the vendored tree` is the
  document's dominant convention. Prefer an explicit qualifier.
- **"tip"** — a referent that moves. See FACT 6.

---

## FACT 1 — the parity fixture, as committed

**MEASURED**, from `data/parity_fixture.save` in `stratocracy-crew` at
`11ef8ce`, parsed as JSON:

- The command log holds **169** commands: `Move` 49, `Attack` 74, `Build` 22,
  `Capture` 12, `EndTurn` 12.
- The set of `{turn, side}` pairs carrying a `Capture` is **identical** to the
  set carrying an `EndTurn`: turns 1 through 6, both sides, twelve pairs.
- The log's final entry is `{"turn": 7, "side": 0, "kind": "Attack"}`. **Turn 7
  carries no `EndTurn` and no `Capture`, for either side.**
- Commands per side-turn, in order: 9, 11, 9, 14, 16, 11, 16, 12, 18, 10, 20,
  12, and 11 for turn 7 side 0.
- The twelve `Capture` entries carry `unit` values 2, 7, 2, 7, 2, 7, 3, 7, 3, 7,
  3, 7 in log order.
- The save's `result` field reads `Decisive`. Its `stateHash` is
  `1044f6ec0c455fdd`. There is no `hasResult` key in the committed file.

### CORRECTION to FACT 1 — "at `11ef8ce`" above means *as the file stands there*

Recorded beside the original rather than in place of it. **The ambiguity is
mine.** The header says the fixture was read "in `stratocracy-crew` at
`11ef8ce`", which states where the bytes were read and **not** where they were
committed. The first revision of Pair 1 read it the other way and wrote "the
fixture committed at that same commit".

**MEASURED**: `11ef8ce` changes `cpp_reference/test_replay.cpp` alone. The last
commit to change `data/parity_fixture.save` is **`c2f5860`**, subject `Widen the
parity fixture to the complete command set`; before it, `862a225`.

So the fixture is **committed at `c2f5860`** and unchanged at `11ef8ce`. §3
already says this elsewhere — *"the committed fixture carries the complete §4.9
command set at `c2f5860`"* — and any pair naming a commit for the fixture must
name `c2f5860`. Pinning the **emitter** to `11ef8ce` remains correct: that is
where `test_replay.cpp` stands, and it is a claim about state at a commit.

#### CORRECTION to the CORRECTION to FACT 1 — that quotation is not §3's wording

Recorded beside it rather than in place of it. **The misattribution is mine, and
I wrote it while correcting a different error of my own.** Gate run
`capture-pin-2` filed it as a `dead-reference` against a draft that had lifted it
verbatim and in good faith.

**MEASURED**, per occurrence, with the section taken from the nearest preceding
heading:

- *"the committed fixture carries the complete §4.9 command set at `c2f5860`"* —
  lower-case *the*, bare backticked SHA — occurs at **line 1569 (§4.4)** and
  **line 3281 (§4.11)**. It does **not** occur in §3.
- §3's own wording, at **line 1516**, is *"The committed fixture carries the
  complete §4.9 command set at"* followed by `c2f5860` as a bracketed Markdown
  link — capital *The*, link rather than bare backticks.

**The fact is unaffected**: §3 does name `c2f5860` as the fixture's commit, at
line 1516, so Pair 1 agrees with §3 and the requirement to name `c2f5860` stands.
Only the quotation above was misattributed.

**The general lesson, since it caused this:** the two wordings differ by interior
Markdown markup alone, which is the same thing FACT 7 records as making a literal
search miss a sentence that is present. A quotation carries **two** claims — that
the string exists, and that it exists *where you say it does*. Verifying presence
does not verify attribution, and I verified only presence.

## FACT 2 — the emitter

**MEASURED**, from `cpp_reference/test_replay.cpp` in `stratocracy-crew` at
`11ef8ce`, function `appendAiTurn`:

- The block that appends a `Capture` is entered only when the AI's command is
  `EndTurn` **and** `g.turn.running` is true.
- Inside that block the `unit` written is the lowest `id` among the acting
  side's units whose table row has `canCapture` true. When the side has no such
  unit, nothing is appended.
- The command loop is bounded at 32 iterations per side-turn.

**MEASURED** dispositions of those two conditions on this fixture, from FACT 1:

- The `canCapture` condition was satisfied at every one of the twelve appends —
  each carries a `unit`.
- No side-turn reached the 32-iteration bound; the largest is 20.

**INFERRED**: turn 7 side 0 ends without an `EndTurn` and without a `Capture`
because the match ended during that side-turn, so `g.turn.running` was false
when the AI returned `EndTurn`. This follows from the measured `result`
`Decisive`, the measured absence of both kinds at turn 7, and the measured
11-command count ruling out the iteration bound. It was not observed directly.

### CORRECTION to FACT 2 — the condition list above is incomplete

Recorded here beside the original rather than in place of it. **The omission is
mine**, and the first draft of this round's Pair 1 was built on it in good faith.

**MEASURED**, from the same function: when a unit is found, the emitter does not
append the `Capture` directly. It calls `applyCommand(g, cap, t)` and pushes the
command to the log **only if that call returns `ok`**:

    if (found) {
        const ReplayResult rc = applyCommand(g, cap, t);
        if (rc.ok) log.push_back(cap);
    }

So a `Capture` reaches the log on **three** conditions, not two: the AI's command
is `EndTurn` and `g.turn.running` is true; the acting side has a unit whose table
row has `canCapture`; and the rules accept the resulting command.

**Consequence for the prose:** the conditions above are *necessary*. This fact
block does not establish that they are jointly *sufficient*, and no sentence in
the master may say or imply that they are. Prefer prose that states what governs
the cadence over prose that enumerates a closed condition list.

## FACT 3 — what the master says today

**MEASURED**, quoted from `source/gdd.md`. §3 carries, as one sentence:

> The fixture carries the kind because `appendAiTurn` appends one `Capture` per
> side at the close of that side's turn, outside the AI's choice: `openTurn`
> already ticks capture on an objective the side held, so what the appended
> command catches is an objective the side moved onto during the turn just
> played.

The clause before the colon carries no qualification for a match that ends
during a side-turn.

## FACT 4 — the cadence sweep

**MEASURED.** Every sentence in the master containing the string `Capture` was
read: 49 sentences, distributed §3 13, §4.7 13, §4.4 6, §4.11 5, §2.11.6 3,
§4.8 3, §2.7 2, §2.11.1 2, §2.11.2 1, §4.9 1.

**Exactly one of the 49 asserts a per-side-per-turn `Capture` cadence** — the
sentence quoted at FACT 3.

Two neighbouring sentences state related things and are **not** cadence claims:
§3's *"`Capture` cannot be produced by the AI at all"* and §4.11's *"That log
carries the four command kinds row 6's AI emits and not the fifth"*. Both remain
true under any qualification of the FACT 3 sentence.

## FACT 5 — the Selfplay correction

**MEASURED**, from `git` in `stratocracy-crew`:

- Commit `5072d10`, subject line `Name the unvendored module Balance, not
  Selfplay`, changes `crew/tools.py` alone, 8 insertions and 3 deletions.
- `5072d10` is an ancestor of `11ef8ce`.
- The commits on `main` after `5072d10`, oldest first, are `b5f524d`,
  `c2f5860`, `11ef8ce`.

### CORRECTION to FACT 5 — the commit list is round context, not master material

Recorded beside the original rather than in place of it. **The defect is mine**:
I supplied the three-commit list as my own justification for pinning, and the
first draft of Pair 2 wrote it into the master, reasonably.

A list of what has landed on a branch since a commit is **exhaustive and
unpinned**. It is true today and false at the next crew commit — the same species
this round exists to remove from §3. **No pair writes it.** What the master needs
from FACT 5 is the commit that made the sentence true; the rest of FACT 5 exists
so the Director could see that the referent had already moved.

**MEASURED**, and separate: `e19605e`, subject `Declare the vendored set instead
of inferring it from a glob`, created `ue_module/vendored_set.json` along with
changes to `crew/tools.py`, `spec/integration_spec.md` and `sync_stratrules.py`.
`5072d10` changed `crew/tools.py` alone. **They are different changes**, so §3's
existing clause naming `e19605e` for the vendored-set declaration and this
round's pin to `5072d10` for the correction are both true and do not conflict.
The `e19605e` clause is not amended this round.

## FACT 6 — the moving-referent sweep

**MEASURED.** §3 carries, as one sentence:

> The tree was corrected at the crew tip; the message cannot be.

Sweeping the master for referents that move with a branch: `tip` occurs in that
one sentence. `tip of` occurs 0 times, `HEAD` 0, `latest commit` 0, `as it
stands` 0. The 14 occurrences of `crew half` each stand beside a named commit
(`cb8e12b`), so each is pinned.

## FACT 7 — the second §3 present-tense sentence, and why it is out of scope

**MEASURED.** §3 carries:

> Sentences of the form *"they do not run **here**"* are true of every headless
> suite in that repo and were kept.

It sits inside a commit-pinned record that opens *"Stale claims in the crew repo
were repaired at `9289c1d`: eleven sites said …"*, and its own verb is past
(`were kept`). The Director ruled this round that the enclosure is what a
present-tense clause needs, so **this sentence is not amended this round.**

Note for any sweep: a literal search for `they do not run here` returns zero
against the master, because the master writes it with interior bold —
`*"they do not run **here**"*`. A sweep that reports zero here has found a
property of the sweep.

## FACT 8 — already in the master; do not restate as new

**MEASURED.** The master already states, at §3 and §4.7, that build ties break
by the priority Infantry > Recon > Artillery > Tank, which is **ascending §2.4
cost, 100 / 150 / 200 / 300**, and states in the same §3 paragraph as the FACT 3
sentence that `startingFame` is 200 a side and Infantry's `CostFame` is 100.

**MEASURED**, from `cpp_reference/Ai.good.cpp` at `11ef8ce`: `chooseBuild`
filters the caller's buildlist to the affordable entries and returns the minimum
under `buildPriorityLess`, which compares `costFame` ascending with a pinned
enum order as tiebreak.

The Director ruled this round that the emitter's buildlist composition needs no
addition to the master, the inertness being derivable from what is already
written. **No pair in this round touches the buildlist sentence.**

## FACT 9 — the vocabulary counts behind the Director's "the tree" ruling

**MEASURED.** `the vendored tree` occurs 18 times. Bare `the tree` occurs 5
times: 3 in §3, 2 in §4.9. `crew tree` occurs 0 times; `the crew repo` 30 times.

The Director ruled this round that **no convention is adopted** and **no pair
touches these sites**. The counts are recorded so the next round need not
re-measure them.

---

## What this round changes

Two pairs, both in §3, and nothing else.

1. Qualify the FACT 3 sentence so that it is true of a match that ends during a
   side-turn, on the evidence in FACTS 1 and 2.
2. Pin the FACT 6 sentence to crew `5072d10`, on the evidence in FACT 5.

## Error species forbidden in this round

Named because each has cost a blocking gate run before:

1. **Narrowing a universal.** Do not repair a quantifier by shrinking its scope
   until the counterexample falls outside it. Say what is true of every case.
2. **A locator finer than what was measured.** Address a candidate by quoted
   master text plus a section number and no finer, unless the finer locator was
   measured this round and appears above.
3. **Apparatus beyond the pairs.** The addendum is the pairs, their placement
   and their evidence. No sweep narrative, no coverage claims, no summary of
   what was not changed.
4. **An unpinned present-tense claim about repo contents.** Any new sentence
   asserting what a tree, branch or file holds must name the commit it holds at.
5. **Promoting an INFERRED fact.** FACT 2's last paragraph is inferred. If the
   prose needs it, it must read as what follows from the record, not as an
   observation.

## Standing instruction to the author

If a gate finding rests on a fact that contradicts this file, or on a fact this
file does not contain, **say so in your response and do not repair the prose to
satisfy it.** A gate told a false fact cannot catch it, and a defective claim of
mine lifted in good faith has blocked a round before.
