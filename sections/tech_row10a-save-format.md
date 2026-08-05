# Addendum — build-order row 10 part (a), Rulings K–N, and one repair (tech-director)

Exact OLD → NEW pairs against `source/gdd.md`. Every OLD was checked to be a
unique substring of that file before it was written here.

---

### Pair 1 — repair the standing defect: the crew commit stated as ancestry

Replacement, in §3's status line. The cited claim was about branch heads; the
crew commit is restated as ancestry, which is what was measured, and the same
line is re-pointed to this round's commit.

**OLD**

```
This draft stands at 2026-08-04, at commit [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) in the crew repo and at `9dec48c` in the Stratocracy UE project repo, each verified with `git ls-remote` to be the head of its own repo's default branch — `main` in the crew repo, `master` in the UE project — with both working trees clean.
```

**NEW:**

```
This draft stands at 2026-08-05, at commit [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) in the crew repo and at `9dec48c` in the Stratocracy UE project repo. In the crew repo, [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8) is an ancestor of `737f666`, measured with `git merge-base --is-ancestor` rather than read off a branch, and every crew-repo commit this GDD cites is reachable from `737f666`, measured the same way per sha. `9dec48c` is cited as a commit, and this line makes no claim about how it stands to any branch. This line previously said that both commits had been verified with `git ls-remote` to be the head of their own repo's default branch. That was true when it was gated and false within the hour, a concurrent human push having moved one of them — a head expires and a sha does not — so the defect is recorded here rather than quietly overwritten.
```

---

### Pair 2 — the `41a1452` record's dead half

Replacement, inside §3's row-8 rebuild record. The clause about §4.10's
canonical state hash survives untouched; only the row-10 clause moves, and it
moves into the past tense the surrounding record is already scoped to.

**OLD**

```
not implemented at this commit**: row 10 holds no code.
```

**NEW:**

```
not implemented at this commit**: row 10 held no code then.
```

---

### Pair 3 — the record of row 10 part (a)

Goes at the end of §3's status paragraph, immediately before its closing italic
marker. It follows the posture row 9's landing already holds in this
paragraph — a build-order row that holds code, closes part of its acceptance
set, and has no ledger row to flip.

**OLD**

```
**How `d837fc8` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

**NEW:**

```
**How `d837fc8` was authored is deliberately not stated:** no harness claim is made for it, because none was established. **Build-order row 10's part (a) then landed**, at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), with the UE project repo unmoved at `9dec48c`. New in the crew repo: `spec/save_spec.md`, `cpp_reference/Save.h`, `cpp_reference/Save.good.cpp`, `cpp_reference/Save.buggy.cpp` and `cpp_reference/test_save.cpp`, registered as row `save` in `crew/tools.py`, so this row runs under the `python run.py` gate `T-INT-04` names rather than by an ad-hoc compile. The last of those sources is an eleventh harness, so **thirteen** tracked sources define `main()` at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) — eleven test harnesses, one combat duel simulator, and one debug REPL — a figure taken by enumerating them at that commit and diffing that list against the twelve at [`7c36303`](https://github.com/jakemartin/stratocracy-crew/commit/7c36303) rather than by adding one to a count above: the difference is exactly `cpp_reference/test_save.cpp`, and nothing was removed. The gate is **`T-SAVE-04` plus `GATE-SAVE-PARSE`, 25/25 under clang++ and MSVC both** — `g++` is still not installed on this machine. Pass-1 `cpp_reference/Save.buggy.cpp` is blocked at **18/25** under both compilers — **seven FAIL lines over two distinct IDs, identical under each, and predicted in full before the run**. Its three defects are mechanical edits of `Save.good.cpp`: `loadSave` parses into the caller's object and then validates; `checkHeader` compares only `formatVersion` and `rulesCommit`; `onlyKeys` tolerates an unknown key. Against them `T-SAVE-04` (a), (b) and (f) fail the *state untouched* clause alone, (c), (d) and (g) are not refused at all, and `GATE-SAVE-PARSE`'s unknown-key check is tolerated. **`GATE-SAVE-PARSE` mints no acceptance ID**, on the `GATE-SCN-PARSE`, `GATE-AI-SMOKE` and `GATE-CAP-PARTIAL` precedent. **No acceptance ID was written**, so §4.5's written-ID count does not move at this landing, its green count moves **55 → 56** and its unclosed count moves **16 → 15**. **Every other row's tally is unchanged from the pre-change baseline, under both compilers** — row 1 7/7, row 2 6/6, row 3 6/6, row 4 9/9, row 5 11/11, row 6 7/7, row 7 12/12, row 8 34/34 and the debug driver 12/12 — and **`T-INT-01` and `T-INT-04` still pass 2/2 at `rulesCommit` `d837fc8` after this module landed**, which is what makes the no-vendoring decision recorded in §4.9 safe rather than merely convenient. **Six of row 10's seven IDs did not run, and each is named in the runner with its reason** rather than absorbed: `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` need the headless replayer of part (b); `T-SAVE-06` is the only † of the seven, is asserted jointly with `T-INT-02`, and has neither an in-editor harness nor a built subject; `T-SAVE-07` needs row 6's self-play, which part (c) reaches. **Row 10's acceptance set therefore does not close**, on the Q29 reading applied per acceptance ID as well as per row. **It has no row in the table below to leave unflipped**: §4.11 calls row 10 a *proposed* ledger row, and this landing creates none. That is row 9's posture and deliberately not the partial-pass posture of rows 2, 7 and 8, each of which has a ledger row that a partial pass leaves standing unflipped; a row that does not exist has nothing to leave. **What part (a) deliberately does not do is stated so it is not inferred.** No command is applied, so **§4.10's canonical state hash is not defined here** — that is part (b)'s, and part (a) carries `stateHash` as an opaque required string. `dataHash` and `scenarioHash` are **compared as opaque strings and never recomputed**, which is what keeps this part's dependency set empty; its link set is `Save.cpp`, `Hex.cpp` and `test_save.cpp` and nothing else. No in-editor harness is among the thirteen `main()` definitions above. **How `737f666` was authored is deliberately not stated:** no harness claim is made for it, because none was established.*
```

---

### Pair 4 — Ruling K

On §3's sentence that defers the row. The deferral is confirmed and gains a name
and an acceptance set; no row is created.

**OLD**

```
The row is deferred until the bridge is built, so the ledger later gains a row describing a whole system.
```

**NEW:**

```
The row is deferred until the bridge is built, so the ledger later gains a row describing a whole system. **The Director has since named that row without creating it (ruled 2026-08-05):** it is **Headless → Unreal integration**, its acceptance set is `T-INT-01..05`, and it is created as **one** row when §4.9 part 2 lands — which is this deferral's own reason stated forward rather than a second decision.
```

---

### Pair 5 — Ruling M, first cite site

Replacement, in §3's `d837fc8` record. The inline statement of the closure rule
becomes a citation of the convention.

**OLD**

```
so the amended text cannot have been satisfied there, and an ID whose written text widens closes at the commit at which the widened text is met.
```

**NEW:**

```
so the amended text cannot have been satisfied there, and the closure convention §4.5 states governs where the green lands.
```

---

### Pair 6 — §4.5's green total

Replacement, in the *Specification outruns the build* risk row.

**OLD**

```
**55** of the 71 are green
```

**NEW:**

```
**56** of the 71 are green
```

---

### Pair 7 — Ruling M's convention, and the green decomposition's new term

Replacement, in the same risk row. This is where the closure rule is stated, and
after Pairs 5, 15 and 16 it is the only place it is stated; the decomposition
gains its new term in the same sentence.

**OLD**

```
without closing it either — an ID whose written text widens closes at the commit at which the widened text is met, and T-INT-04's text did not change (§3) — so every row on the critical path has now landed
```

**NEW:**

```
without closing it either — under **the closure convention this document states once, here: an ID whose written text widens closes at the commit at which the widened text is met**, `T-INT-04`'s text not having changed (§3) — and **1** at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), where `T-SAVE-04` closed on row 10's part (a) without closing row 10's acceptance set, that row having no ledger row to close (§3) — so every row on the critical path has now landed
```

---

### Pair 8 — §4.5's unclosed total

Replacement, in the same risk row.

**OLD**

```
**16 IDs remain unclosed**
```

**NEW:**

```
**15 IDs remain unclosed**
```

---

### Pair 9 — the tail of §4.5's unclosed enumeration

Replacement. Both halves of this clause move: the count it quantifies over, and
the description of the row it counts.

**OLD**

```
and the **7** in row 10, which holds no code
```

**NEW:**

```
and the **6** left in row 10, whose part (a) has since landed and which therefore holds code — `T-SAVE-04` closed at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666), and the six left wait on the replayer of part (b), on the editor pass, or on row 6's self-play (§3)
```

---

### Pair 10 — §4.4's week-2 cell

Replacement. The cell already names `T-SAVE-04` among the IDs that close in that
week and then lists only the two that were green ahead of it; a third now is.

**OLD**

```
and **T-INT-04 is green at `b23823f`** and **T-INT-01 at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)**, over the vendored tree at `9dec48c` (§3), both ahead of this cell rather than behind it, since neither runs on a command log or needs a rules row, and the vendoring they assert over has landed.
```

**NEW:**

```
and **T-INT-04 is green at `b23823f`** and **T-INT-01 at [`d837fc8`](https://github.com/jakemartin/stratocracy-crew/commit/d837fc8)**, over the vendored tree at `9dec48c`, and **T-SAVE-04 at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666)**, on row 10's part (a) (§3) — all three ahead of this cell rather than behind it, since none of them runs on a command log or needs a rules row: the vendoring the two `T-INT` IDs assert over has landed, and `T-SAVE-04` refuses on the header alone and never applies a command.
```

---

### Pair 11 — Ruling N

In §4.9's module-layout part, immediately after the sentence that says what is
not vendored. The enumeration of vendored modules is left exactly as it stands.

**OLD**

```
and `selfplay.cpp`, and the `*.buggy.cpp` files are pass-1 fixtures, not
shippable code.
```

**NEW:**

```
and `selfplay.cpp`, and the `*.buggy.cpp` files are pass-1 fixtures, not
shippable code. **An eleventh crew module exists and is deliberately not
vendored.** `Save` landed at
[`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666) (§3)
and stays out of `Source/StratRules/` until part (b) gives it a bridge consumer
— a decision rather than an omission, and **nothing re-dates on its account**:
`T-INT-01` stays green at `d837fc8` and `T-INT-04` at `b23823f`, and no UE
project commit was made when it landed. The enumeration above is correct as it
stands and gains only the statement that an eleventh module was left out on
purpose.
```

---

### Pair 12 — Ruling L

After §4.9's parity-gate paragraph and before the spec stub it introduces. It
records what part 2 waits on and schedules nothing.

**OLD**

```
risk — a compiler/CRT divergence in the damage formula's `round` — mechanically
instead of by playtest anecdote.
```

**NEW:**

```
risk — a compiler/CRT divergence in the damage formula's `round` — mechanically
instead of by playtest anecdote.

**No further spec-stub pass is owed for part 2 (ruled 2026-08-05).** The stub
below is already full: its invariants carry the bridge's own — `T-INT-02`,
`T-INT-03` and `T-INT-05` — beside a Determinism line and an Acceptance line, so
what part 2 waits on is not specification. It waits on two named things:
**§4.10's canonical state hash**, which is build-order row 10's part (b) and is
`T-INT-02`'s and `T-INT-03`'s subject, and **an in-editor Automation harness**.
Both are recorded here as blockers and neither is scheduled here.
```

---

### Pair 13 — §4.10's costing of a wider hash

Replacement. The clause this argument rests on survives — nothing computes the
canonical state hash yet — and only the row-10 clause moves.

**OLD**

```
Row 10 holds
no code and no save file exists, so widening the hash costs nothing at this
revision and would not stay free.
```

**NEW:**

```
**This hash is still
unbuilt**: row 10's part (a) has landed and defines none of it, carrying
`stateHash` as an opaque required string (§3), so widening the hash still costs
nothing at this revision and would not stay free.
```

---

### Pair 14 — §4.11 row 10's cell

On the cell's part (a) clause, extended with what landed.

**OLD**

```
and T-SAVE-04 (refusal on any header mismatch) closes on it alone, since it never applies a command.
```

**NEW:**

```
and T-SAVE-04 (refusal on any header mismatch) closes on it alone, since it never applies a command. **Part (a) has since landed**, at [`737f666`](https://github.com/jakemartin/stratocracy-crew/commit/737f666): `T-SAVE-04` is green there under clang++ and MSVC both, beside `GATE-SAVE-PARSE`, which mints no acceptance ID, so this row holds code without closing its set (§3).
```

---

### Pair 15 — Ruling M, second cite site

Replacement, in §4.11's row-9 prose. The inline statement becomes a citation.

**OLD**

```
its written text was widened there, over an
input that did not exist before it, so the widened text is first met at that
commit (§3).
```

**NEW:**

```
its written text was widened there, over an
input that did not exist before it, so it closes there under the closure
convention §4.5 states (§3).
```

---

### Pair 16 — Q33's pointer to where the convention lives

Replacement. Q33 cites two sections for the closure rule and restates it in
passing; after Pair 15 only one section states it.

**OLD**

```
since an ID whose text widens closes where the widened text is met (§4.5, §4.11)
```

**NEW:**

```
under the closure convention §4.5 states
```

---

## Arithmetic

- **§4.5 moves 71 / 55 / 16 → 71 / 56 / 15.** No acceptance ID is minted;
  `T-SAVE-04` closes. Pairs 6, 8 and 9 carry the three figures.
- **The green-by-commit decomposition gains +1 at `737f666`** (Pair 7).
- **Row 10's unclosed count moves 7 → 6**, and row 10 now holds code (Pair 9).
- **§3's `main()` count moves 12 → 13** at `737f666`,
  `cpp_reference/test_save.cpp` being an eleventh harness (Pair 3). Enumerated
  at that commit and diffed against the list at `7c36303`: the difference is
  that one addition and nothing was removed.
- **9 verified ledger rows — unchanged.** §3's table gains no row: §4.11 calls
  row 10 a *proposed* ledger row, so there is nothing to flip and no partial
  pass to record against a row that does not exist.
- **§3's "eight IDs still recorded as uncovered" does NOT move.** That
  enumeration lists only IDs belonging to §3 ledger rows — T-MOVE-07 and
  T-SCN-10 unwritten; T-DATA-05, T-SCN-08, T-SCN-09, T-SCN-11, T-UI-03 and
  T-UI-04 written and not green. Row 10 has no ledger row, so `T-SAVE-04` was
  never among the eight and closing it cannot reduce them. **No pair moves this
  figure.**
- Of the pairs above, four are insertions by substring test — 4, 11, 12 and
  14 — and the rest are replacements.

## Check results

- Every OLD was grepped against `source/gdd.md` and returned exactly one
  occurrence. The four anchors that span a hard line wrap — Pairs 11, 12, 13 and
  15 — were verified in multiline mode, so the wrap is part of what was matched;
  the others sit inside a single line of the master.
- The blast-radius sweep ran over `T-SAVE-04`, `T-SAVE-01..07`, `T-SAVE-06`,
  `T-INT-01`, `T-INT-04`, `737f666`, `d837fc8`, `b23823f`, and the terms
  *unbuilt*, *holds no code*, *last unbuilt*, *proposed*, *unclosed*,
  *uncovered* and *green*. Sites found and deliberately left unedited, with the
  reason each survives:
  - §3's *"Row 8 was the last unbuilt link on §4.11's critical path"* — row 10
    is not on that path.
  - §3's *"§4.9 part 2 is unbuilt"* and its `T-INT-03` sentence — part 2 and the
    canonical state hash are both still unbuilt.
  - Q29's *"both proposed rows, both unwritten today"* — no row was created.
  - §2.10's *"row 10(b)'s replayer reads the `scenarioId`/`scenarioHash`"* —
    part (b) is untouched by this round.
  - §4.11's *"row 10's format spec must exist by the row-9 integration pass"* —
    a requirement, and satisfying it does not falsify it.
  - §3's *"eight IDs still recorded as uncovered"* — see Arithmetic.
  - §3's `main()` sentences at every earlier landing — each is scoped to its own
    commit, so this landing extends the series rather than falsifying any of
    them.
  - §3's reachability parenthetical, which describes both repos by branch head —
    it survives the push on the measurement, and Pair 1 is scoped to the one
    sentence the Director filed, asserting nothing about the UE project commit's
    relation to a branch. Filed below instead.

## Change requests

1. **§3's reachability parenthetical states both repos by branch head.** It
   reads that every crew-repo commit the section cites is reachable *from the
   head of `main`*, and that `99fcb84` and `9dec48c` are each reachable *from
   the head of `master`* in the UE project repo. **Its conclusion is not in
   doubt and this request does not challenge it** — the parenthetical is true as
   this draft stands. What is in doubt is the form the claim takes. **Each half
   now has a durable equivalent that has been established by measurement, and
   the two were established separately**: the crew half as ancestry from a named
   sha, which Pair 1 carries; the UE half as `99fcb84` being an ancestor of
   `9dec48c`, with both reachable from `9dec48c` — measured with `git merge-base
   --is-ancestor` and `git rev-list` for this request, after Pair 1 was written
   and deliberately not folded back into it. **Neither of those measurements is
   the claim the parenthetical makes.** No branch-head reading was taken for
   either repo, on purpose: reachability from a head and reachability from a sha
   are different assertions, and it is the first that expired inside an hour and
   produced the defect Pair 1 repairs. So the question the Director owns is not
   whether the sentence is true but whether the document should assert the
   durable form in place of the expiring one — and whether that becomes a
   document-wide convention rather than a fact about named commits. No pair here
   touches it.
2. **Row 10's eventual ledger row has no name or acceptance set.** Ruling K
   supplies both for the deferred §4.9 row. Row 10 is the other *proposed* row
   and now holds code, so the same two facts will be wanted for it — and with
   them, whether parts (a), (b) and (c) resolve to one ledger row or more. Not
   decided here.
3. **`T-SAVE-06` is row 10's only †, and it now has two blockers rather than
   one.** §4.11's cut-line bullet prices it as the in-editor half of the parity
   pair. Its subject — the canonical state hash — is also unbuilt, so cutting
   the editor pass is no longer the whole of what would leave it unclosed.
   Whether that bullet should say so is a §4.11 text decision.

## Grounding

- Row 10 part (a)'s landing, its files, its registration as row `save` in
  `crew/tools.py`, the `T-SAVE-04` + `GATE-SAVE-PARSE` result under clang++ and
  MSVC, the pass-1 block, the FAIL lines and the IDs they fall on, the three
  mechanical defects, the per-fixture failure map, the unchanged per-row
  baseline tallies, the integration-gate result at `rulesCommit` `d837fc8`, the
  IDs that did not run with their reasons, and the empty dependency and link
  sets: `facts_row10a.md`, sections *What was built and where it stands* and
  *What part (a) deliberately does NOT do*.
- The `main()` figure at `737f666`, the eleventh harness, and the diff against
  the list at `7c36303` showing one addition and no removal: measured this round
  with `git grep -l "int main(" <commit> -- '*.cpp'`, counted and diffed, and
  supplied by the Director with the gate's escalation. The twelve at `7c36303`
  is `source/gdd.md` §3's own figure at that landing.
- `d837fc8` being an ancestor of `737f666`, and every cited crew commit being
  reachable from `737f666`, each measured with `git merge-base --is-ancestor`:
  `facts_row10a.md`, *What was built and where it stands*. Pair 1 asserts no
  ancestry for `9dec48c`, and its UE-repo clause is confined to citing the
  commit.
- The UE-repo ancestry cited in change request 1 — `99fcb84` an ancestor of
  `9dec48c`, both reachable from `9dec48c` — was measured by the Director with
  `git merge-base --is-ancestor` and `git rev-list` and supplied with the
  `row10a-2` gate result, after Pair 1 was gated.
- The `git ls-remote` head claim, its truth when gated and its falsity within
  the hour, and the instruction to restate it as commits and ancestry:
  `facts_row10a.md`, *A standing defect to repair*.
- Rulings K, L, M and N in full, including that no row is created, that no
  current attribution changes, and that nothing re-dates: `facts_row10a.md`,
  *The four Director rulings to be written this round*.
- Every figure in the Arithmetic section other than the `main()` count,
  including the one that must not move and the reason it does not:
  `facts_row10a.md`, *Arithmetic*.
- `GATE-SAVE-PARSE` minting no acceptance ID, on the `GATE-SCN-PARSE` /
  `GATE-AI-SMOKE` / `GATE-CAP-PARTIAL` precedent: `facts_row10a.md`, *What part
  (a) deliberately does NOT do*; those three gates and their no-ID treatment are
  recorded in `source/gdd.md` §3 at `9086d6a`, `d8284f1` and `7c36303`.
- The posture to follow — a *proposed* build-order row holding code with no
  ledger row to flip, and its distinction from the partial-pass posture of rows
  2, 7 and 8: `source/gdd.md` §3, the `b23823f` record, and Q29.
- Q29's per-acceptance-ID reading: `source/gdd.md` §4.7 register, Q29.
- `T-SAVE-06`'s † mark and its joint assertion with `T-INT-02`: `source/gdd.md`
  §4.11's cut-line bullets and §4.10's spec stub.
