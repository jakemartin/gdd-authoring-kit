> # ✅ APPLIED ADDENDUM — DO NOT RE-APPLY
>
> Every replacement pair in this file **has been applied to the master GDD**.
> Verified 2026-08-10 against `source/gdd.md` md5 `1f27e981b623c7af2f6402d9a5b6a62b`
> (3365 lines), matched newline-insensitively: each pair's old text is either
> absent from the master, or present only inside the new text that replaced it —
> the pairs that extend a sentence rather than swap it. No pair is outstanding.
>
> No pair count is stated here deliberately: this file's line-initial markers do
> not reconcile with its own pair headings, because narrative prose that begins a
> line with the word *old* parses as a marker. The verified claim is the one
> above, which is per-pair and needs no total.
>
> Its quoted "current" text, register extents and open items are a **snapshot of
> the moment it was written**, not the state of the document.
>
> **The master GDD is the source of truth** — read `source/gdd.md`. Further changes
> to a merged section go in a *new* addendum file.

# Addendum — build-order row 10 part (b), and Rulings O, P, R, S, T (tech-director)

Exact OLD → NEW pairs against `source/gdd.md`. Every OLD was checked to be a
unique substring of that file before it was written here.

---

### Pair 1 — §3's status line: this round's commit and its ancestry

Re-points the line to this round's crew commit and states the ancestry that was
measured.

**OLD**

```
This draft stands at 2026-08-05, at commit [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) is an ancestor of `737f666`, measured with `git merge-base --is-ancestor` rather than read off a branch, and every crew-repo commit this GDD cites is reachable from `737f666`, measured the same way per sha.
```

**NEW:**

```
This draft stands at 2026-08-05, at commit [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) and [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) are each an ancestor of `ec15be6`, measured with `git merge-base --is-ancestor` per sha rather than read off a branch, and every crew-repo commit this GDD cites is an ancestor of `ec15be6`, measured the same way per sha.
```

---

### Pair 2 — Ruling S, §3's reachability parenthetical

Restates the crew half against a named commit, and bounds the ruling so it is
not read as a document-wide convention.

**OLD**

```
*(Every **crew-repo** commit this section **cites** — `d8284f1`, row 6's, included — is reachable from the head of `main` there, so every commit link above resolves.
```

**NEW:**

```
*(Every **crew-repo** commit this section **cites** — `d8284f1`, row 6's, included — is an ancestor of [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), measured with `git merge-base --is-ancestor` per sha, so every commit link above resolves. That form was ruled on 2026-08-05, and the ruling is confined to this sentence: it matches the §3 status line above, whose substance is unchanged, and restating every reachability claim in this document against a named commit was considered in the same ruling and declined.
```

---

### Pair 3 — the row-9 record's claim about row 10's code

Scopes §3's sentence about `T-INT-03`'s subject to the commit its record is
about.

**OLD**

```
`T-INT-03`'s subject is §4.10's canonical state hash, which build-order row 10 has not built;
```

**NEW:**

```
`T-INT-03`'s subject is §4.10's canonical state hash, which build-order row 10 had not built at that commit;
```

---

### Pair 4 — the record of part (b), carrying Rulings O, P and T

Goes at the end of §3's status paragraph, immediately before its closing italic
marker, following the posture the part (a) record before it holds.

**OLD**

```
**How `737f666` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

**NEW:**

```
**How `737f666` was authored is deliberately not stated:** no harness claim is made for it, because none was established. **Build-order row 10's part (b) then landed**, at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), with the UE project repo unmoved at `9dec48c`. New in the crew repo: `spec/replay_spec.md`, `cpp_reference/Replay.h`, `cpp_reference/Replay.good.cpp`, `cpp_reference/Replay.buggy.cpp` and `cpp_reference/test_replay.cpp`; modified: `cpp_reference/Save.h`, `cpp_reference/Turn.h`, `cpp_reference/test_save.cpp`, `crew/tools.py`, `crew/offline.py`, `spec/save_spec.md`, `spec/integration_spec.md` and `spec/turn_spec.md`. **Part (b) was run against part (c)'s closure conditions rather than after them, on a ruling (2026-08-05).** §4.11 splits row 10's dependencies because week 2's log carried only `{Move, Attack}`, and puts closure in part (c) on rows 4 and 5 completing the command set, row 6 completing `T-SAVE-02`'s determinism composition, and `T-SAVE-07` needing row 6's self-play besides; rows 4, 5 and 6 are green at [`647d4df`](https://github.com/jakemartin/stratocracy-crew/commit/647d4df), [`6ccd40b`](https://github.com/jakemartin/stratocracy-crew/commit/6ccd40b) and [`d8284f1`](https://github.com/jakemartin/stratocracy-crew/commit/d8284f1), so the calendar reason for the split is gone and the gate's log carries the **complete §4.9 command set** — `Move`, `Attack`, `Build`, `Capture` and `EndTurn` — which is what Q29 requires before an acceptance ID may close. **Part (c) is not complete at this commit**, `T-SAVE-06` and `T-SAVE-07` not having closed, for the two reasons recorded below. **A segment of the gate's log is generated by row 6's AI rather than hand-written:** at this commit the AI emits a move, an attack on the opposing flag Tank and an end of turn, so the log crosses a turn boundary under both sides and `T-AI-06` sits inside `T-SAVE-02`'s composition rather than beside it. The new module is registered as registry row `replay` in `crew/tools.py`, so it runs under the `python run.py` gate rather than by an ad-hoc compile, and it is a **second** registry row rather than a widening of the `save` row: §4.11 says part (a) has *no deps at all*, which is encoded as that row's link set — `Save.cpp`, `Hex.cpp` and `test_save.cpp` — so widening it would have falsified §4.11's part-(a) dependency cell silently. The `replay` row's own link set is `Replay.cpp`, `Save.cpp`, `Hex.cpp`, `Data.cpp`, `Move.cpp`, `Economy.cpp`, `Turn.cpp`, `Combat.cpp`, `Ai.cpp` and `test_replay.cpp`; `Scenario.cpp` is in neither link set, `scenarioHash` being compared as an opaque string and never recomputed. `cpp_reference/test_replay.cpp` is a twelfth harness, so **fourteen** tracked sources define `main()` at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) — a figure taken by enumerating them at that commit with `git grep -l` and diffing that list against the thirteen at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) rather than by adding one to a count above: the difference is exactly `cpp_reference/test_replay.cpp`, and nothing was removed. The gate is **`T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` plus `GATE-REPLAY-*`, 29/29 under clang++ and MSVC both** — `g++` is still not installed on this machine. Pass-1 `cpp_reference/Replay.buggy.cpp` is blocked at **21/29** under both compilers — **eight FAIL lines over four distinct IDs, identical under each, and predicted in full before the run**. Its three defects are mechanical edits of `Replay.good.cpp`: `replayLog` applies to the caller's state in place rather than to a copy; the hash walks units in storage order rather than in canonical hex order; and it omits the two per-unit turn flags. Against them `T-SAVE-05` fails clauses (e), (f) and (g) alone — (a) through (d) PASS, because `applied` is a reported field rather than the state — and `GATE-REPLAY-BYTES`, `GATE-REPLAY-ORDER` and all three `GATE-REPLAY-FLAGS` clauses fail, while **`T-SAVE-01`, `T-SAVE-02` and `T-SAVE-03` all PASS against the defective module**, every clause they carry comparing two runs that share the defect on both sides. **`GATE-REPLAY-*` mint no acceptance ID**, on the `GATE-SAVE-PARSE`, `GATE-AI-SMOKE` and `GATE-CAP-PARTIAL` precedent. **No acceptance ID was written**, so §4.5's written-ID count does not move at this landing, its green count moves **56 → 60** and its unclosed count moves **15 → 11**. **Every other row's tally is unchanged from the pre-change baseline, under both compilers** — row 1 7/7, row 2 6/6, row 3 6/6, row 4 9/9, row 5 11/11, row 6 7/7, row 7 12/12, row 8 34/34, row 10's part (a) 25/25, the debug driver 12/12 and the integration gate 2/2. **`strat::GameState` is declared here (ruled 2026-08-05)**, in `cpp_reference/Replay.h`, and the type's NAME was already this document's: §4.9 calls it *the authoritative `strat::GameState`*, §4.10 defines the canonical state hash over it, and `T-UI-05`'s own invariant text names it. At [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) the string `GameState` occurred in the crew repo only inside comments citing this GDD, in `cpp_reference/Save.h`, `cpp_reference/Ui.h` and `spec/turn_spec.md`. **No invariant's text is amended by this landing, so no closure re-dates and no green attribution moves:** `T-UI-05` is green at [`41a1452`](https://github.com/jakemartin/stratocracy-crew/commit/41a1452) before this commit and after it. The type holds the mutable state the rules modules own — board, units, economy, turn — and not the §4.8 tables or the Stub-7 scenario, which arrive as arguments; it is a **fourth composition** beside row 6's `AiState`, row 8's `UiWorld` and the debug driver's `Session`, and none of the four owns a rule. The flag designation lives on it as `flagUnit[side]` rather than as a bool on the unit, because a dead flag is absent from the unit list and a per-unit bool cannot then separate *"the flag died"* from *"this side designates none"*. **§4.10's canonical state hash is implemented here, and its field list was restated into the groups the modules hold (ruled 2026-08-05):** two groups moved — `cpp_reference/Economy.h` holds capture progress on the tile, as `CaptureProgress {hex, unitId, turnsHeld}`, on the stated ground that progress can never transfer (Q4, T-FAME-05), and keys `PendingBuild {factoryHex, side, defIndex}` by the factory hex — and of §4.10's three per-factory names, `hex` survives as a field, **`hasBuiltThisTurn` stops being a field without ceasing to be carried** — the build-allowance group is walked over the turn module's built-this-turn set, so an entry exists for a factory that has taken its build this turn and none exists for one that has not, which is a change of encoding and not of coverage — and **`buildWaiting` alone stops being carried**, on §4.10's own stated omission rule, since it is recomputable from the pending-build group. §4.10 carries the implemented grouping. `canonicalStateBytes` is exposed beside the digest, so a check can assert the serialisation and not only the digest. **`Replay.h::openTurn` runs `beginTurn`, then start-of-turn repair, then income, then the capture tick** — the order the Director ruled on 2026-08-03, the tick after income — and `cpp_reference/Driver.good.cpp`'s `openActiveTurn` performs that same sequence over the driver's `Session`. That is a duplication of a ruled **order** and not of a rule a module owns, and it is filed as a change request in `spec/replay_spec.md`. **Two things this landing found in its own instruments are recorded rather than smoothed over.** The gate's first fixture board carried a single factory: §2.8's domination backstop (`T-TURN-03`) ends a match the moment one side holds every factory, and row 5 checks it at `beginTurn`, so that board's match ended before its first command and every later command was refused; the shipped fixture carries a factory per side. And **the `T-SAVE-05` check was written so that it could not fail** — its bad log replayed from a state in which the log's first entry had already been spent, so entry 0 was refused as a repeat and nothing was applied under any implementation, and it passed against the very defect it exists to catch; running the defective module is what exposed it. It now replays from the initial state, so entries 0 and 1 apply before the refusal at index 2, and it asserts that index by value. **Stale claims in the crew repo were repaired in the same commit**, found with a whitespace-collapsed, case-insensitive sweep: `cpp_reference/Save.h`, `cpp_reference/Turn.h`, `cpp_reference/test_save.cpp`, `crew/tools.py`, `spec/save_spec.md`, `spec/integration_spec.md` and `spec/turn_spec.md` each stated either that §4.10's canonical state hash had no implementation or that `T-SAVE-01/02/03/05` still awaited a replayer. `spec/integration_spec.md`'s is the load-bearing one: it said `T-INT-02` and `T-INT-03` *"have no subject even in an editor pass"*, which this landing makes false. **`T-SAVE-06` did not close.** It is the only † of row 10's seven, it is asserted jointly with `T-INT-02`, and no in-editor Automation harness exists; its other blocker — §4.10's canonical state hash having no implementation — is removed here, so the in-editor Automation harness is now the whole of what it waits on. **`T-SAVE-07` did not close:** `cpp_reference/selfplay.cpp` is a combat-only 1v1 duel harness that prints a table of duel outcomes, and it writes no §4.10 command log. **Row 10's acceptance set therefore does not close**, on the Q29 reading applied per acceptance ID as well as per row, and its unclosed count moves **6 → 2**. **No ledger row is created, flipped or removed by this landing**: §4.11 calls row 10 a *proposed* ledger row, which is row 9's posture and deliberately not the partial-pass posture of rows 2, 7 and 8. **The Director has since named that row without creating it (ruled 2026-08-05), on Ruling K's precedent for row 9:** it is **Save & replay**, its acceptance set is `T-SAVE-01..07`, and it is created as **one** row when that full set closes — which under Q29 is the same condition as its flipping — so parts (a), (b) and (c) resolve to one ledger row rather than to several, and what it waits on is `T-SAVE-06` and `T-SAVE-07`. **How `ec15be6` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

---

### Pair 5 — §4.5's green total

**OLD**

```
**56** of the 71 are green
```

**NEW:**

```
**60** of the 71 are green
```

---

### Pair 6 — §4.5's green-by-commit decomposition

Adds this landing's term.

**OLD**

```
that row having no ledger row to close (§3) — so every row on the critical path has now landed
```

**NEW:**

```
that row having no ledger row to close (§3), and **4** at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), where `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` closed on row 10's part (b), run over the command set part (c) requires, without closing that row's acceptance set either — so every row on the critical path has now landed
```

---

### Pair 7 — §4.5's unclosed total

**OLD**

```
**15 IDs remain unclosed**
```

**NEW:**

```
**11 IDs remain unclosed**
```

---

### Pair 8 — §4.5's row-10 term

The tail of the unclosed enumeration: the term itself, and what the IDs behind
it wait on.

**OLD**

```
and the **6** left in row 10, whose part (a) has since landed and which therefore holds code — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), and the six left wait on the replayer of part (b), on the editor pass, or on row 6's self-play (§3)
```

**NEW:**

```
and the **2** left in row 10, whose parts (a) and (b) have since landed — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), part (b) having run over the command set part (c) requires — leaving `T-SAVE-06` on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in the §4.10 format (§3)
```

---

### Pair 9 — §4.4's week-3 cell

The cell named `T-SAVE-07` as the only one of that group still waiting;
`T-SAVE-06` waits too, and the four that closed are recorded against the commit
that closed them.

**OLD**

```
Only T-SAVE-07 still waits — for wk 4's self-play logs.
```

**NEW:**

```
**T-SAVE-01, T-SAVE-02, T-SAVE-03 and T-SAVE-05 are green at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6)** (§3), where row 10's part (b) ran over the complete command set rows 4–5 supply. **Two still wait**: `T-SAVE-06` on the in-editor Automation harness it is asserted jointly with `T-INT-02` on, and `T-SAVE-07` on a self-play log written in the §4.10 format, which wk 4's self-play is scheduled to produce.
```

---

### Pair 10 — Ruling L's blocker list, one blocker removed

§4.9's part-2 ruling named two blockers; one of them landed.

**OLD**

```
It waits on two named things:
**§4.10's canonical state hash**, which is build-order row 10's part (b) and is
`T-INT-02`'s and `T-INT-03`'s subject, and **an in-editor Automation harness**.
Both are recorded here as blockers and neither is scheduled here.
```

**NEW:**

```
It waits on **an in-editor
Automation harness**. The other blocker recorded here was **§4.10's canonical
state hash**, `T-INT-02`'s and `T-INT-03`'s subject, which build-order row 10's
part (b) built at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) (§3).
The harness is recorded here as the remaining blocker and is not scheduled here.
```

---

### Pair 11 — Ruling R, §4.9's unvendored modules

Ruling N's statement covered one module; the ruling now covers two and gives its
standing reason.

**OLD**

```
**An eleventh crew module exists and is deliberately not
vendored.** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) (§3)
and stays out of `Source/StratRules/` until part (b) gives it a bridge consumer
— a decision rather than an omission, and **nothing re-dates on its account**:
`T-INT-01` stays green at `d837fc8` and `T-INT-04` at `b23823f`, and no UE
project commit was made when it landed. The enumeration above is correct as it
stands and gains only the statement that an eleventh module was left out on
purpose.
```

**NEW:**

```
**Two crew modules exist and are deliberately not
vendored (ruled 2026-08-05).** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) and
`Replay` at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) (§3),
and both stay out of `Source/StratRules/`, where they would be an eleventh and a
twelfth module beside the ten enumerated above. §3 records that no bridge
exists — no load mapping, no command surface, no event list, no actor and no
widget — so §4.9 part 2 is unbuilt and the bridge consumer that would read them
is still hypothetical, while vendoring now would re-date `T-INT-01`'s and
`T-INT-04`'s closures. That is a decision rather than an omission, and
**nothing re-dates on their account**: `T-INT-01` stays green at `d837fc8` and
`T-INT-04` at `b23823f`, and no UE project commit was made at either landing.
The enumeration above is correct as it stands and gains only the statement that
two modules were left out on purpose.
```

---

### Pair 12 — Ruling P, §4.10's field order

Restates the order in the groups the modules hold, names the collections the
canonical hex order is walked over, and says which of the per-factory names
changes encoding and which stops being carried.

**OLD**

```
`GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal`/`fameCombat`, objective ownership, per-unit `{id, side, hex, hp,
isFlag, hasMoved, hasActed, captureProgress, pendingBuilds}` sorted by the
canonical hex order (§4.7 conventions, T-HEX-07), then the per-factory build
record `{hex, hasBuiltThisTurn, buildWaiting}` (T-TURN-10) in that same
canonical hex order — then hash the bytes. Every field is an **integer**, the
four turn and build flags written as 0 or 1 (`eff` and the HP ratio exist only
transiently inside `resolveDamage`), so the hash is platform-stable by
construction; T-INT-02 proves it across compilers. **The flags are hashed
because a save is accepted mid-turn** (Policies below): at hash time a unit may
have spent one of its two flags and a factory may have taken its build for the
turn, so a hash without them is identical across states the rules distinguish,
and T-INT-02 and T-SAVE-06 would both agree over that difference rather than
catch it.
```

**NEW:**

```
`GameState` in a fixed field order — turn counter, side to move, per-side
`fameTotal` and `fameCombat`, objective ownership `{hex, owner}`, per-unit
`{id, side, hex, hp, isFlag, hasMoved, hasActed}`, the per-tile capture record
`{hex, unitId, turnsHeld}`, the per-factory build allowance `{hex}` (T-TURN-10)
and the pending builds `{factoryHex, side, defIndex}` — objective ownership,
the per-unit group, the per-tile capture record, the build allowance and the
pending builds each walked in the canonical hex order (§4.7 conventions,
T-HEX-07), keyed on the hex that group carries, ties within one hex broken by
`id` — then hash the bytes. **The build allowance carries `hasBuiltThisTurn` as
membership rather than as a field:** the group is walked over the turn module's
built-this-turn set, so an entry exists for a factory that has taken its build
this turn and none exists for one that has not, each entry emitting a constant
marker that carries no information its presence does not. Every emitted value
is an **integer** (`eff` and the HP ratio exist only transiently inside
`resolveDamage`), so the hash is platform-stable by construction; T-INT-02
proves it across compilers. The module exposes `canonicalStateBytes` beside the
digest, so a check can assert the serialisation and not only the digest. **The
per-unit turn flags and the per-factory build allowance are carried because a
save is accepted mid-turn** (Policies below): at hash time a unit may have spent
one of its two flags and a factory may have taken its build for the turn, so a
hash without them is identical across states the rules distinguish, and
T-INT-02 and T-SAVE-06 would both agree over that difference rather than catch
it. **The list above was restated into the groups the modules hold (ruled
2026-08-05)**, when row 10's part (b) implemented it: `captureProgress` and
`pendingBuilds` were previously written as members of the per-unit group, while
`cpp_reference/Economy.h` holds the first on the tile — progress can never
transfer (Q4, T-FAME-05) — and keys the second by the factory hex.
```

---

### Pair 13 — §4.10's omission rule and the dropped field

Puts the dropped field under the rule the section already states, and says how
the waiting build the Policies call hashed reaches the hash.

**OLD**

```
above. That is a narrower test than "derived", and deliberately so — the
Policies below call a waiting build and capture-in-progress derived *pending*
state because they are a function of the log, and both are hashed.
```

**NEW:**

```
above. `buildWaiting` (T-TURN-10) is the same case, being recomputable from the
pending-build group, so the hash carries the pending build and not the flag.
That is a narrower test than "derived", and deliberately so — the
Policies below call a waiting build and capture-in-progress derived *pending*
state because they are a function of the log, and both are hashed, the waiting
build as a pending-build entry.
```

---

### Pair 14 — §4.10's costing sentence

The sentence was written against the hash having no implementation.

**OLD**

```
**This hash is still
unbuilt**: row 10's part (a) has landed and defines none of it, carrying
`stateHash` as an opaque required string (§3), so widening the hash still costs
nothing at this revision and would not stay free.
```

**NEW:**

```
**This hash is built**, at
[`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6) on
row 10's part (b), where `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05`
closed over it (§3); part (a), which landed before it, defines none of it and
carries `stateHash` as an opaque required string. Widening the hash now moves a
digest a landed module computes — the cost the sentence this replaces said
would arrive.
```

---

### Pair 15 — §4.11 row 10's cell records part (b)

**OLD**

```
(c) *Closure* — rows **4, 5** complete the command set (T-SAVE-01/03/05/06), row **6** completes T-SAVE-02's determinism composition, and T-SAVE-07 needs row 6's self-play besides.
```

**NEW:**

```
(c) *Closure* — rows **4, 5** complete the command set (T-SAVE-01/03/05/06), row **6** completes T-SAVE-02's determinism composition, and T-SAVE-07 needs row 6's self-play besides. **Part (b) has since landed**, at [`ec15be6`](https://github.com/jakemartin/stratocracy-crew/commit/ec15be6), and was run against these closure conditions rather than after them (ruled 2026-08-05, rows 4, 5 and 6 all being green): `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` are green there under clang++ and MSVC both, beside `GATE-REPLAY-*`, which mint no acceptance ID. `T-SAVE-06` waits on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in this format, so this row holds code without closing its set (§3).
```

---

### Pair 16 — the part-(a) record's unrun-ID clause, pinned to its commit

Two predicates in that clause were written in the present tense and were true of
`737f666`. Pair 3 makes the same move for the row-9 record's sentence. The
sentence's bolded lead-in is a record of that run and is not in this OLD.

**OLD**

```
need the headless replayer of part (b); `T-SAVE-06` is the only † of the seven, is asserted jointly with `T-INT-02`, and has neither an in-editor harness nor a built subject; `T-SAVE-07` needs row 6's self-play, which part (c) reaches.
```

**NEW:**

```
needed the headless replayer of part (b), which was unbuilt at that commit; `T-SAVE-06` is the only † of the seven, is asserted jointly with `T-INT-02`, and had at that commit neither an in-editor harness nor a built subject; `T-SAVE-07` needs row 6's self-play, which part (c) reaches.
```

---

## Arithmetic

- **§4.5 moves 71 / 56 / 15 → 71 / 60 / 11.** No acceptance ID is minted;
  `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` close. Pairs 5, 7 and 8
  carry the three figures, and Pair 4 states the two movements in §3.
- **The green-by-commit decomposition gains a term of 4 at `ec15be6`** (Pair 6).
  Its terms then sum to the total Pair 5 states.
- **§4.5's unclosed enumeration keeps its other terms** — 1 for T-DATA-05, 3 for
  the `T-SCN-` IDs, 2 for T-UI-03/04, 3 for row 9 — and its row-10 term moves
  6 → 2 (Pair 8). Those terms sum to the total Pair 7 states.
- **§3's `main()` count moves 13 → 14** at `ec15be6`,
  `cpp_reference/test_replay.cpp` being a twelfth harness (Pair 4). Enumerated
  at that commit with `git grep -l` and diffed against the list at `737f666`:
  that one addition, no removal.
- **§4.10's per-factory names go 3 → 1 in the field list and 3 → 2 in what the
  hash carries, and the two surviving sets are not the same set.** The field
  list keeps `hex` alone, which is why Pair 12 writes the group as `{hex}`; what
  the hash carries keeps `hex` and `hasBuiltThisTurn`, the second as membership
  rather than as a field; `buildWaiting` leaves both. Pairs 4 and 12 state those
  three dispositions in words and state neither movement as a numeral, so this
  bullet is the only site either figure appears. Pair 13 states the omission
  rule `buildWaiting` falls under.
- **Pair 16 moves no figure.** It changes the tense of two predicates and states
  no quantity; the *six of row 10's seven IDs* its sentence opens with is a
  record of that run and stays as written.
- **9 verified ledger rows — unchanged.** §3's table gains, loses and flips no
  row: §4.11 calls row 10 a *proposed* ledger row, and Ruling T names its
  eventual row without creating it.
- **§3's "Nine rows carry a ✓ in the table above, and three more carry evidence
  without one" does not move**, for the same reason. **No pair touches it.**
- **§3's "eight IDs still recorded as uncovered" does not move.** That
  enumeration lists only IDs belonging to §3 ledger rows — T-MOVE-07 and
  T-SCN-10 unwritten; T-DATA-05, T-SCN-08, T-SCN-09, T-SCN-11, T-UI-03 and
  T-UI-04 written and not green. Row 10 has no ledger row, so no `T-SAVE-` ID
  was ever among the eight. **No pair moves this figure.**
- **The §4.7 register stands at 33 rows, 16 ruled and 17 open.** This round
  mints no `Q` row, and the five rulings are lettered O, P, R, S and T — the
  letter Q skipped so that a ruling letter cannot be read as a register row.
  **No pair touches the register's two extent-bearing sites.**

## Check results

- Every OLD was grepped against `source/gdd.md` and returned exactly one
  occurrence, matches counted with `-o` so that the several anchors sitting
  inside §3's single very long line are counted as occurrences and not as
  lines. The five anchors that span a hard line wrap — Pairs 10, 11, 12, 13 and
  14 — were verified in multiline mode, so the wrap is part of what was
  matched; the other eleven sit inside a single line of the master.
- Pairs 12, 13 and 14 fall in one §4.10 paragraph and do not overlap: Pair 12
  ends at *catch it.*, Pair 13 begins at *above. That is a narrower test* and
  ends at *both are hashed.*, and Pair 14 begins at the sentence after it.
  Pairs 1, 2, 3, 4 and 16 fall in §3's single long line and do not overlap
  either: Pair 16's span ends at *which part (c) reaches.*, and Pair 4's begins
  at the *How `737f666` was authored* sentence, later in that same record.
- **§3's part-(a) record was re-read sentence by sentence**, whitespace-collapsed
  and case-insensitive, for predicates written in the present tense that this
  landing falsifies. It found the two Pair 16 pins and no others. The siblings
  checked and left as written, each with why it survives:
  - *`T-SAVE-07` needs row 6's self-play, which part (c) reaches* — true, and
    what kept it from closing is the log format rather than the schedule.
  - *Row 10's acceptance set therefore does not close* — still true.
  - *It has no row in the table below to leave unflipped … this landing creates
    none* — no row was created.
  - *§4.10's canonical state hash is not defined here — that is part (b)'s* —
    scoped by *here* to part (a), and part (b) is where it landed.
  - *its link set is `Save.cpp`, `Hex.cpp` and `test_save.cpp` and nothing
    else* — part (a)'s link set, which this landing left alone by registering a
    second registry row, as Pair 4 states.
  - *No in-editor harness is among the thirteen `main()` definitions above* —
    scoped to that commit's own enumeration.
  - *`T-INT-01` and `T-INT-04` still pass 2/2 at `rulesCommit` `d837fc8` after
    this module landed* — a claim about that landing, and the integration gate
    is 2/2 at this one too.
- **The "found and left unedited" list below did not reach that clause, which is
  why the site arrived at a gate rather than at a pair.** The list was built per
  search term, and `T-SAVE-01`..`T-SAVE-07` were on the term list; what it did
  not do was read the paragraph those hits sat in. The bullet above is that
  reading, and the list now carries §3's part-(a) record as an entry of its own
  rather than only as term hits.
- **The §4.10 sentence Pair 12 retains was checked against the encoding it now
  describes.** It says a factory may have taken its build for the turn and that
  a hash without that is identical across states the rules distinguish. The
  build allowance distinguishes exactly that state by the presence or absence of
  an entry, so the sentence stands as written and Pair 12 keeps it.
- **Each figure in the Arithmetic section was re-read against the sentence
  beside it**, after a figure and its own explanation were found to disagree
  inside one bullet. The per-factory bullet's two movements are counted off
  Pair 12's written group and the three dispositions the same bullet names,
  which is the same source its prose is taken from.
- **What landed was checked against §4.11 rather than asserted.** That cell puts
  three things in part (c): rows 4 and 5 completing the command set, row 6
  completing `T-SAVE-02`'s determinism composition, and `T-SAVE-07` needing row
  6's self-play besides. `T-SAVE-06` and `T-SAVE-07` did not close, so part (c)
  is not complete, and this file was swept whitespace-collapsed and
  case-insensitive for *landed*, *land*, *complete*, *completed* and *done*
  beside *part (c)*: every site states that part (b) landed and was run against
  part (c)'s closure conditions, which is what Ruling O states and what §4.11
  supports.
- The blast-radius sweep ran whitespace-collapsed and case-insensitive over
  `T-SAVE-01`..`T-SAVE-07`, `T-INT-02`, `T-INT-03`, `T-UI-05`, `GameState`,
  `stateHash`, *canonical state hash*, *part (b)*, *part (c)*, *replayer*,
  *unbuilt*, *proposed ledger row*, *holds no code*, *has not built*,
  *reachable from the head*, `buildWaiting`, `hasBuiltThisTurn`,
  `captureProgress`, `pendingBuilds`, `spawnBlocked`, *self-play* / `selfplay`,
  `737f666`, `41a1452`, `d837fc8`, `9dec48c` and `ec15be6`. Sites found and
  deliberately left unedited, with the reason each survives:
  - **§3's part-(a) record, read whole rather than as term hits** — its two
    falsified predicates are Pair 16, and its siblings are enumerated above.
  - §4.4's week-2 cell, *"T-INT-01/04 and T-SAVE-04 close here, the rest do
    not"* — scoped to what closes in that week over its `{Move, Attack}`
    subset, and the four that closed did so over the complete command set.
  - §4.4's week-2 cell naming *the §4.10 save/replay format + headless
    replayer*, and §2.10's IN row naming the same — schedule and scope
    statements, which a landing satisfies rather than falsifies.
  - §4.4's week-4 cell, *"T-SAVE-07 (harness compatibility) closes here"* — it
    has not closed.
  - §2.10's *"row 10(b)'s replayer reads the `scenarioId`/`scenarioHash` it
    produces"* — it does, and `Scenario.cpp` being outside the link set is a
    statement about recomputation rather than about reading.
  - §3's row-8 rebuild record, both its `stateHash` sentence and its
    *"row 10 held no code then"* — each already scoped to `41a1452`.
  - §3's *"§4.9 part 2 is unbuilt"* in both the `b23823f` and `d837fc8`
    records — no bridge exists.
  - §3's *"Row 8 was the last unbuilt link on §4.11's critical path"* — row 10
    is not on that path.
  - Q29's *"both proposed rows, both unwritten today"* — no row was created.
  - §4.7 Stub 8's and §2.11.5's per-factory snapshot block, which carries
    `hasBuiltThisTurn`, `buildWaiting` and `spawnBlocked` — snapshot fields
    read by the UI, a different subject from what the hash carries, and §2.11.5
    reads `hasBuiltThisTurn` off that block rather than off the hash.
  - §4.7's conventions list, which names the §4.10 canonical state hash among
    the determinism surfaces — a list of surfaces.
  - §4.10's file-layout row for `stateHash` — a header field, which part (a)
    still writes.
  - `T-UI-05`'s invariant text naming `strat::GameState`, and §4.9's
    *authoritative `strat::GameState`* — neither is amended, and Pair 4 states
    that no invariant text moves.
  - §4.11's cut-line bullets for `T-SAVE-06` and for `T-SAVE-01..05` — the
    first prices the editor pass and the second states those five are headless.
  - §3's `main()` sentences at every earlier landing — each scoped to its own
    commit, so Pair 4 extends the series.
  - §3's UE-repo clause in the reachability parenthetical — outside Ruling S's
    scope and filed below.

## Change requests

1. **The §3 parenthetical's UE-project half still states reachability from a
   branch head.** Ruling S restates the crew half against a named commit and
   declines a document-wide convention, so `99fcb84` and `9dec48c` keep the form
   that expired once before in this document, as §3's own record of it says.
   Whether that half gains a durable form is a decision this round did not take,
   and Pair 2 does not touch it.
2. **The ruled start-of-turn order now has two implementations.**
   `Replay.h::openTurn` and `Driver.good.cpp`'s `openActiveTurn` each run
   `beginTurn`, repair, income, capture tick. The crew repo files this in
   `spec/replay_spec.md`; whether the GDD should name one owner for that
   sequence — §4.9's bridge, the replayer, or neither — is a §4.9/§4.11 text
   decision.
3. **`T-SAVE-07`'s producer does not exist in the §4.10 format, and part (c) is
   held open by it.** `cpp_reference/selfplay.cpp` writes a duel table, and
   §4.4's week 4 closes `T-SAVE-07` on self-play output. Re-pointing the
   self-play harness at the §4.10 format is work no build-order row currently
   names.
4. **§4.11's acceptance-ID column for row 10 lists no gate name.** Rows 6 and 8
   list `self-play smoke` and `GATE-CAP-PARTIAL` in that column beside their
   numbered IDs; row 10 now has `GATE-SAVE-PARSE` and `GATE-REPLAY-*`, both
   minting none. Whether the column should carry them is a §4.11 presentation
   decision, and no pair here changes that column.
5. **§3's landing records state their unrun IDs in the present tense.** Pair 16
   pins one such clause after the fact and Pair 3 pinned another, both of them
   current-state claims written inside a record of a past commit. Whether §3
   should state a landing's outstanding IDs in the past tense as a convention,
   so that the next landing has nothing to pin, is a §3 style decision the
   Director owns; no pair here proposes it.

## Grounding

- The commit, its ancestry measurements, the new and modified tracked files, the
  `main()` figure and its enumerate-and-diff method, the registry row `replay`
  and both link sets, the 29/29 result under clang++ and MSVC, the pass-1 block
  and its FAIL distribution, the three defects, the per-clause failure map, the
  unchanged per-row baseline, and `GATE-REPLAY-*` minting no ID:
  `FACTS_ROW10B.md`, sections *The commit*, *The gate run* and *The registry
  row, and why there are two*.
- The four closures, the written/green/unclosed movements, row 10's own
  unclosed movement, `T-SAVE-06`'s and `T-SAVE-07`'s reasons for not closing,
  the register's extent, and that no ledger row is created, flipped or removed:
  `FACTS_ROW10B.md`, *What closed, and the arithmetic*.
- **The two facts Pair 16 pins the part-(a) record against** — `T-SAVE-06`'s
  built-subject blocker being removed by this landing, and `T-SAVE-01`,
  `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` having closed over the replayer:
  `FACTS_ROW10B.md`, *What closed, and the arithmetic*, against the part-(a)
  record's own text in `source/gdd.md` §3.
- Part (c)'s three closure conditions, `T-SAVE-07` being one of them:
  `source/gdd.md` §4.11, row 10's dependency cell.
- `strat::GameState`'s prior naming in §4.9, §4.10 and `T-UI-05`'s text, its
  declaration site, the `737f666` occurrence set, that no invariant text is
  amended and no closure re-dates, its contents, its standing as a fourth
  composition, and `flagUnit[side]`: `FACTS_ROW10B.md`, *`strat::GameState`*.
- The implemented field grouping, the two groups that moved, the id tie-break,
  the integer property and `canonicalStateBytes`: `FACTS_ROW10B.md`, *The hash
  definition — two field groups moved, and what the per-factory group carries*.
- **`hasBuiltThisTurn` being carried as set membership over the turn module's
  built-this-turn set, the constant marker per entry, `buildWaiting` alone
  ceasing to be carried, and the encoding-not-coverage reading of the retained
  §4.10 sentence**: the same section's **CORRECTION issued at gate run
  `row10b-1`**, measured against `canonicalStateBytes` at `ec15be6`.
- **Objective ownership, the per-unit group, the per-tile capture record, the
  build allowance and the pending builds each being walked in canonical hex
  order, keyed on the hex each carries**: the same section's **SECOND
  CORRECTION, same run**, measured at `ec15be6`.
- Rows 4, 5 and 6 being green at `647d4df`, `6ccd40b` and `d8284f1`, the
  complete §4.9 command set in the gate's log, and the AI-generated segment:
  `FACTS_ROW10B.md`, *Why parts (b) and (c) were run together*.
- The `openTurn` sequence, the ruled tick-after-income order, and the driver's
  duplication of it: `FACTS_ROW10B.md`, *The start-of-turn moment*.
- The vendoring ruling, its reasons and its standing: `FACTS_ROW10B.md`,
  *Vendoring*.
- The domination-backstop fixture and the `T-SAVE-05` check's repair:
  `FACTS_ROW10B.md`, *Two things this round found in its own instruments*.
- The repaired crew-repo claims and the load-bearing one in
  `spec/integration_spec.md`: `FACTS_ROW10B.md`, *Six stale claims repaired in
  the crew repo*.
- Rulings O, P, R, S and T in full, the skipped letter, and that no `Q` row is
  minted: `FACTS_ROW10B.md`, *The five Director rulings this round*.
- Q29's per-acceptance-ID reading, the *proposed* row posture and its
  distinction from rows 2, 7 and 8, Ruling K's precedent for naming a row
  without creating it, and the `GATE-SAVE-PARSE` / `GATE-AI-SMOKE` /
  `GATE-CAP-PARTIAL` no-ID precedent: `source/gdd.md` §4.7 register Q29, §3's
  `b23823f` and `737f666` records, and §4.11 row 10.
