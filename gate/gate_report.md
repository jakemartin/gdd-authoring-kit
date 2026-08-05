# Gate report — run `row10b-4`

- Master: `source/gdd.md`, MANIFEST md5 `01433f61ba39f63fdac6aaae0ff2b451`.
- `source/MANIFEST.txt` present; all three source files listed. No `sync-missing`.
- Section read: `sections/tech_row10b-replayer-hash.md` — 16 pairs, one file. One
  file this stage, so no cross-section placement collision is possible; the
  sixteen intra-file placements were checked against each other and none collide.
- Top-level verdict: **PASS**. Zero violations.

---

## Disposition of run `row10b-3`'s finding

Re-derived against the master rather than taken on report, and then re-checked
against the repair.

At `row10b-3` the block was one `contradiction`: §3's part-(a) record at
`737f666` stated, without a tense marker, that four T-SAVE IDs

> `T-SAVE-01`, `T-SAVE-02`, `T-SAVE-03` and `T-SAVE-05` need the headless replayer of part (b); `T-SAVE-06` is the only † of the seven, is asserted jointly with `T-INT-02`, and has neither an in-editor harness nor a built subject;

while Pair 4 appended to the same paragraph that those four had closed and that
`T-SAVE-06`'s built-subject blocker was removed.

**Pair 16 repairs it, and repairs it by pinning rather than by deleting.** Its
OLD is the exact clause quoted above, resolved in `source/gdd.md` line 1514 —
the string `need the headless replayer of part (b)` occurs once in the whole
master, and the OLD as written is a unique substring of that line. Its NEW reads

> needed the headless replayer of part (b), which was unbuilt at that commit; `T-SAVE-06` is the only † of the seven, is asserted jointly with `T-INT-02`, and had at that commit neither an in-editor harness nor a built subject; `T-SAVE-07` needs row 6's self-play, which part (c) reaches.

Both falsified predicates are now tensed to `737f666` and both name the commit
explicitly rather than relying on the paragraph's context. That is the move
Pair 3 makes for the row-9 record (`has not built` → `had not built at that
commit`), so the two repairs are one convention rather than two. The bolded
lead-in *"Six of row 10's seven IDs did not run, and each is named in the runner
with its reason"* is correctly left outside the OLD: it is a record of what that
run printed and remains true.

---

## The three checks the brief asked for, each re-derived

### 1. The claim of no further falsified sibling predicates — verified

I read §3's part-(a) record on line 1514 sentence by sentence, from
*"**Build-order row 10's part (a) then landed**, at `737f666`"* to
*"**How `737f666` was authored is deliberately not stated**"*, and sorted its
sentences into commit-scoped records and present-tense predicates.

Commit-scoped records, which this landing cannot falsify: the new-file list and
the `save` registry row; *"**thirteen** tracked sources define `main()` at
`737f666`"* with its diff against the twelve at `7c36303`; the
`T-SAVE-04` + `GATE-SAVE-PARSE` 25/25 gate; the pass-1 18/25 block and its three
defects; and *"its green count moves **55 → 56** and its unclosed count moves
**16 → 15**"*. Each names its own commit or its own landing. Pair 4 extends the
same series with `ec15be6` and states row 10's part (a) as 25/25 in the
unchanged-baseline list, which agrees with this record.

Present-tense predicates, checked one by one:

- *"registered as row `save` in `crew/tools.py`, so this row runs under the
  `python run.py` gate `T-INT-04` names"* — still true; part (b) adds a second
  registry row rather than altering this one, which Pair 4 states in terms.
- *"**`T-INT-01` and `T-INT-04` still pass 2/2 at `rulesCommit` `d837fc8` after
  this module landed**"* — a claim about that landing; the integration gate is
  2/2 at `ec15be6` too, so nothing behind it moved.
- *"**Row 10's acceptance set therefore does not close**"* — still true;
  `T-SAVE-06` and `T-SAVE-07` are open.
- *"**It has no row in the table below to leave unflipped** … and this landing
  creates none"* — still true; Ruling T names the eventual row without creating
  it, and §3's table gains nothing.
- *"**§4.10's canonical state hash is not defined here** — that is part (b)'s"* —
  scoped by *here* to part (a), and part (b) is exactly where it landed.
- *"its link set is `Save.cpp`, `Hex.cpp` and `test_save.cpp` and nothing else"* —
  still true, because the landing registered `replay` as a second row rather
  than widening `save`.
- *"No in-editor harness is among the thirteen `main()` definitions above"* —
  scoped to that commit's enumeration, and still true of the fourteen besides.
- *"`T-SAVE-07` needs row 6's self-play, which part (c) reaches"* — inside
  Pair 16's own OLD span, and carried through unchanged. Its truth value does
  not move on this landing: row 6's self-play landed at `d8284f1`, before
  `737f666`, so what has always been missing is a log in the §4.10 format, not
  the schedule. The draft files that gap as change request 3 rather than
  asserting a repair.

The author's enumeration of seven surviving siblings maps onto this list
exactly. I found no eighth predicate that this landing falsifies. The claim is
sound.

### 2. Pair 16 against Pairs 3 and 4 — no disturbance

All three sit in line 1514, in this textual order:

1. **Pair 3**, in the `b23823f` row-9 record: *"`T-INT-03`'s subject is §4.10's
   canonical state hash, which build-order row 10 has not built;"* — the string
   `has not built` occurs once in the master.
2. **Pair 16**, in the `737f666` part-(a) record, later in the same line.
3. **Pair 4**, at the very end of that record: *"**How `737f666` was authored is
   deliberately not stated:** no harness claim is made for it, because none was
   established.*"* — distinguished from the `6ccd40b`, `e06c44b`/`b23823f` and
   `d837fc8` sentences of the same shape by its sha, so unique.

Neither Pair 16's OLD nor its NEW contains any part of Pair 3's or Pair 4's OLD,
and neither of theirs contains any part of Pair 16's; the three spans are
disjoint and ordered 3 < 16 < 4. I derived the ordering from the master's own
text rather than from the byte offsets supplied, and it agrees with them.
The §4.10 cluster is likewise disjoint: Pair 12's OLD ends at *catch it.* (line
2892), Pair 13's runs *above. That is a narrower test …* to *both are hashed.*
(2897–2899), and Pair 14's begins at *"**This hash is still\nunbuilt**"* on 2899
and ends at *would not stay free.* (2902) — abutting Pair 13 without overlapping
it.

### 3. Pair 16's completeness — nothing left false in its own span

The OLD span carries five clauses. Two are pinned. Of the other three:
*"`T-SAVE-06` is the only † of the seven"* is still true — §4.11 row 10's
acceptance column reads `T-SAVE-01..07 (**T-SAVE-06 †**)`; *"is asserted jointly
with `T-INT-02`"* is unchanged by this landing; and the `T-SAVE-07` clause is
addressed above. No clause inside the span reads falsely after the pin.

---

## Other checks run this round, all clear

- **All sixteen OLD anchors resolve, uniquely, in `source/gdd.md`.** Spot-checked
  against the master: Pair 1 and Pair 2 in §3's status line and reachability
  parenthetical; Pairs 5, 6, 7 and 8 in §4.5 (line 1585); Pair 9 in §4.4's week-3
  cell (line 1567); Pair 10 at lines 2802–2805; Pair 11 at 2757–2765; Pairs
  12–14 at 2879–2902; Pair 15 in §4.11 row 10's cell (line 3003); Pairs 3, 4 and
  16 in line 1514.
- **Arithmetic.** §4.5's green decomposition sums 18+9+9+6+7+1+2+1+1+1+1 = 56 in
  the master; Pair 6's added term of 4 at `ec15be6` takes it to 60, which is what
  Pair 5 writes. The unclosed enumeration sums 1+3+2+3+6 = 15 in the master; with
  Pair 8's row-10 term at 2 it sums to 11, which is what Pair 7 writes. §3's own
  last recorded movement (55 → 56 green, 16 → 15 unclosed) is the baseline Pair 4
  continues. No figure appears outside the Arithmetic section except as prose in
  the pairs the Arithmetic section names.
- **Scope of what landed.** Every site that speaks of part (c) states that
  part (b) landed and was *run against* part (c)'s closure conditions; Pair 4
  states *"**Part (c) is not complete at this commit**"* outright, and Pair 15
  names both IDs still waiting. No sentence claims part (c) completed.
- **Unmeasured universals.** Pair 12's quantifiers are bounded by the implemented
  field grouping — *"Every emitted value is an **integer**"* and the constant
  marker carrying no information its presence does not — both stated in the fact
  set. No wider quantifier appears.
- **Re-dating.** Pair 4 states that no invariant text is amended, that no closure
  re-dates, and that `T-UI-05` is green at `41a1452` before and after; Pair 11
  states that nothing re-dates on the two unvendored modules' account. Nothing
  claims a status flip the round did not make.
- **Negative verification claims.** The `T-SAVE-05` and fixture-board passages are
  past-tense records of what a run exposed, not claims that something has never
  been measured. None expires on the next measurement.
- **Unverified claims.** Every built/green claim carries `ec15be6` and named test
  IDs, and `GATE-REPLAY-*` is stated to mint none.
- **Placement.** Sixteen exact OLD → NEW pairs; each merges mechanically. No
  collision.

---

## Verdict

`sections/tech_row10b-replayer-hash.md` **PASSES** at run `row10b-4` with zero
violations, and the run's top-level verdict is **PASS**. The one
`contradiction` returned at `row10b-3` is closed by Pair 16, which pins both
falsified predicates to `737f666` instead of deleting or hedging them, leaves
the run-record lead-in and the `T-SAVE-07` clause intact, and does not touch
Pair 3's or Pair 4's spans. I re-derived the author's no-further-siblings claim
against §3's part-(a) record sentence by sentence and found no eighth falsified
predicate, and I confirmed that no clause inside Pair 16's own OLD span reads
falsely after the pin. Nothing further must happen before merge: the Director
may apply all sixteen pairs at the placements stated, and should then rebuild
the `.pdf`/`.txt`, re-sync `kb/rules.md` — §2 is untouched by this addendum, so
that sync should be a no-op and is worth confirming rather than assuming — and
re-run `python sync.py`. The five change requests are the Director's to rule on
and none of them blocks this merge.
