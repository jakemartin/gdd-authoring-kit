# Gate report — run `row10c-3`

- `source/MANIFEST.txt` present; `gdd.md md5=a4ea7b331c0e3b024bd2d78bf83dd9f7`.
- Sections gated: `sections/tech_row10c-selfplay-log.md`.
- **Top-level verdict: PASS.** 0 violations.

Everything below was re-derived from the bytes of `source/gdd.md` at the
manifest hash above. Neither the `row10c-1` nor the `row10c-2` report was used
as precedent; both prior findings were re-tested from the master, not from the
prior report's quotes.

---

## `sections/tech_row10c-selfplay-log.md` — PASS (0 violations)

### The two `row10c-2` findings, re-tested

**1. `contradiction` — Ruling T's waiting-set clause (was master line 1514).**
The master still reads, verbatim:

> so parts (a), (b) and (c) resolve to one ledger row rather than to several,
> and what it waits on is `T-SAVE-06` and `T-SAVE-07`.

`rg -o` returns that string exactly once, at line 1514. Pair 16 takes it as its
OLD and replaces it with:

> so parts (a), (b) and (c) resolve to one ledger row rather than to several,
> and what it waits on is `T-SAVE-06` alone, `T-SAVE-07` having since closed at
> [`1ee890e`](…) on part (c).

The one-row-not-several point is reproduced verbatim inside the NEW. The Q29
condition — *"which under Q29 is the same condition as its flipping"* — sits
*before* the anchor and is therefore untouched, which is what the draft's own
Pair 16 note claims ("stay exactly as written") rather than the stronger claim
that it sits inside the NEW. After merge the clause agrees with Pair 12's
*"**`T-SAVE-06` is now the only ID this row lacks**"*. The contradiction is
gone.

**2. `invented-fact` — the reachability parenthetical's sentence count.** The
cardinal is gone from the draft; no count of that parenthetical remains
anywhere in the file. In its place the Check-results section lists eight
dispositions, one per sentence. Counted against line 1531, the parenthetical
holds exactly eight sentences and the draft's list matches them one for one, in
order: the ancestry sentence (Pair 15); *That form was ruled on 2026-08-05…*;
the sentence headed **Not every cited commit is an object in the crew repo**,
whose tail is Pair 2's anchor; *`99fcb84` was the first citation this ledger
made outside the crew repo…*; *The **file** paths resolve too…*; *Those five
citations resolve to two tracked files…*; *The `build/` directory is not
tracked at all.*; *That correction is what the "independently checkable" claim
required, not a cosmetic one.)*. The claim the previous run filed on no longer
exists, and what replaced it is true of the bytes. The remedy diverges from the
one that report suggested — the cardinal was deleted rather than corrected —
and that is accepted: the finding was that an unsupported number stood in for
an enumeration, and an enumeration now stands in its own place.

### Pair 17 — the unfiled scope extension, judged on the merits

`rg -o` returns *"`T-SAVE-07` needs row 6's self-play, which part (c) reaches."*
exactly once, at line 1514, inside the part-(a) landing record's enumeration of
the six IDs that did not run at `737f666`. It is present tense and this round
falsifies it, so it is in scope under the rule the author invoked — scope is
what the round's own edits make false. The tense change is sound at the commit
the record is about: at `737f666` `T-SAVE-07` did need row 6's self-play, so
*needed* is true there, and *"which part (c) reached"* is a forward reference
that became true at `1ee890e` — the same shape the record's sibling clause
already carries (*"needed the headless replayer of part (b), which was unbuilt
at that commit"*). The `737f666` record is not made to claim anything false
about `737f666`.

### The five anchors inside master line 1514

Read in place, they occur in the order the author states — Pair 1, Pair 17,
Pair 3, Pair 16, Pair 4 — and are mutually disjoint, each sitting in a
different sentence: Pair 1 in the status header ending *"…measured the same way
per sha."*; Pair 17 inside the part-(a) record; Pair 3 in the part-(b) record's
`openTurn`/`openActiveTurn` sentence pair; Pair 16 in the Ruling T sentence
after it; Pair 4 at the closing *"How `ec15be6` was authored…"* sentence,
carrying the paragraph's terminal italic marker. Each OLD returns exactly one
`-o` occurrence.

No sentence of line 1514 is left false. The three other `T-SAVE-07` sites on
that line are each pinned to their own commit and survive: *"**Part (c) is not
complete at this commit**, `T-SAVE-06` and `T-SAVE-07` not having closed"*;
*"and `T-SAVE-07` needing row 6's self-play besides"*, which reports what §4.11
says rather than current state; and *"**`T-SAVE-07` did not close:**
`cpp_reference/selfplay.cpp` is a combat-only 1v1 duel harness…"*, still true
of that file. The §4.11 sentence Pair 12 extends — *"`T-SAVE-06` waits on the
in-editor Automation harness and `T-SAVE-07` on a self-play log written in this
format"* — hangs off *"**Part (b) has since landed**, at `ec15be6`"*, a
commit-pinned landing record, so the true-at-that-commit reading does reach it,
which is precisely what did **not** hold for the Ruling T clause; Pair 12
appends the part-(c) record immediately after it in the same shape the (a) and
(b) records already use.

### Unrun-verification claims

Every claim of effect in the file is either a headless gate result or an
explicit negative. Pair 4 states *"**Nothing was compiled by UBT at this
landing, no editor was launched, and no UE project file was touched.**"* and
*"with the UE project repo unmoved at `9dec48c`"*; the closure it claims for
`T-SAVE-07` names a commit (`1ee890e`) and the passing IDs (`T-SAVE-07` plus
`GATE-BALANCE-*`, 12/12 under clang++ and MSVC), so it is not an
`unverified-claim`. No pair asserts anything about what a UE build does or now
permits. Pair 11's added clause — *"both still passing 2/2 at `rulesCommit`
`d837fc8` after the third module landed"* — is a measured result in the fact
block, not a projection.

### Sense-of-"harness" conflation

No pair says a harness now exists. Pair 4 says what landed is *"a producer of
§4.10 command logs"* and in the same sentence that *"the in-editor Automation
harness `T-SAVE-06` waits on is untouched by it"*; Pairs 9, 14 and 16 name
`T-SAVE-06`'s blocker as the in-editor Automation harness alone; Pair 4's
*"thirteenth harness"* / *"thirteen test harnesses"* is §3's own census sense
and extends the master's existing series (twelfth harness / fourteen sources at
`ec15be6`); Pair 10 quotes *harness compatibility* only where §4.4 already
carries it as `T-SAVE-07`'s name. §4.1's *Balance sim harness* line is left
unedited and is filed as change request 2 rather than claimed satisfied.

### Numbers, checked against the master

- §4.5 green: the master's decomposition sums 18+9+9+6+7+1+2+1+1+1+1+4 = **60**,
  matching *"**60** of the 71 are green"*. Pair 6 adds one term of **1** at
  `1ee890e` and Pair 5 states **61**. Consistent.
- §4.5 unclosed: the master's enumeration is 1+3+2+3+2 = **11**, matching
  *"**11 IDs remain unclosed**"*. Pair 8 moves the row-10 term 2 → 1 and Pair 7
  states **10**; the ten named in the Arithmetic section are exactly the ten the
  enumeration then leaves.
- *"**71** written acceptance IDs … against **9** verified ledger rows"* and
  §3's *"Nine rows carry a ✓ … three more carry evidence without one"* and
  *"Eight IDs are still recorded as **uncovered**"* are each unmoved, correctly:
  no ID is minted, no ledger row is created or flipped, and no `T-SAVE-` ID is
  among the eight.
- `main()` census 14 → 15: the master states **fourteen** at `ec15be6`;
  Pair 4's fifteen, and its thirteen/one/one decomposition, follow.
- §4.9 unvendored 2 → 3: Pair 11's OLD matches lines 2757–2771 byte for byte
  across the wrap, and the *eleventh, twelfth and thirteenth* follows the
  master's *eleventh and a twelfth*.

No number in the draft's prose disagrees with the master, and every number that
moves moves through a pair with the movement reconciled in the Arithmetic
section, so there is no `stat-drift`.

### Other checks

- **Anchors.** All seventeen OLDs were re-grepped with `-o` against
  `source/gdd.md`; each returns exactly one occurrence. Pairs 11 and 14 span
  hard wraps and match with their indentation intact.
- **Placement collisions.** One section in this stage, so no cross-file
  collision is possible; within the file the anchors are disjoint, verified per
  shared line (1514: Pairs 1, 17, 3, 16, 4; 1531: Pairs 15 then 2; 1585:
  Pairs 5, 6, 7, 8; 1567/1568: Pairs 9, 10; 2757: Pair 11; 3033: Pairs 12, 13;
  3078: Pair 14). Each placement is an exact unique anchor, which is mechanical.
- **`kb-desync`.** No pair edits §2; the edits fall in §3, §4.4, §4.5, §4.9 and
  §4.11, so `kb_rules.md`, a parse of §2, is unaffected.
- **`dead-reference`.** `1ee890e`, `ec15be6`, `737f666`, `d837fc8`, `9dec48c`
  and `99fcb84` are all cited by the master or measured in the fact block;
  `GATE-BALANCE-*`, `GATE-SAVE-PARSE` and `GATE-REPLAY-*` are the fact block's
  and the master's; §2.0's PX-1 row exists at line 116, inside §2.0
  (106–122), so the corrected change request cites the right section; §4.11
  rows 6 and 8 do carry gate names in the acceptance column, and the master
  itself says *"§4.11 row 6 names it"* of `GATE-AI-SMOKE`. Pair 2's citation of
  *Ruling S* follows the master's own established practice of citing a Director
  ruling letter — line 1514 already cites *"Ruling K's precedent for row 9"*
  with no in-document definition — so it is a citation into the ruling series,
  not a dangling document reference.
- **`voice-drift`.** Declarative, present tense, and in this document's own
  register throughout; no UI strings are written.
- **`format-breach`.** The addendum form carries placement per pair (an exact,
  unique OLD anchor), the draft as the NEW blocks, a Change requests heading
  with the five prior items dispositioned and five new ones filed, and a
  Grounding section that traces each substantive claim to a fact-block section
  or to `source/gdd.md`. Every required element is present in substance.
- **Grounding, claim by claim.** Each substantive claim in the pairs maps to a
  fact-block section or to the master: the commit and its three ancestries (§1),
  the file list and registry row (§1), 12/12 and the 6/12 pass-1 block with its
  six named FAIL lines and the 35-command log over a 6-turn cap (§2), clauses
  (a) and (c) passing against the buggy module (§2), the count movements and the
  ten remaining IDs (§3), the four command kinds and `T-AI-03` (§4),
  `Replay.h::openTurn` (§4 and Ruling V), the three vendoring dispositions and
  `T-INT-01`/`T-INT-04` at 2/2 (§5), the naming constraint (§7), Rulings U, V
  and W with their scope limits (§8), and the register's extent (§9). No
  ungrounded substantive claim was found.

---

## Verdict

**PASS.** `sections/tech_row10c-selfplay-log.md` carries zero violations at
`gdd.md md5=a4ea7b331c0e3b024bd2d78bf83dd9f7`. Both `row10c-2` findings are
resolved against the bytes — the Ruling T clause now has a pair and the
parenthetical's cardinal has been replaced by a sentence-by-sentence
enumeration that matches the eight sentences actually there — and Pair 17, the
extension the gate did not file, is in scope and leaves the `737f666` record
true at `737f666`. Nothing must happen before merge beyond the Director's own
merge procedure: apply the seventeen pairs at their exact anchors, honouring
that Pairs 12 and 13 are insertions and the other fifteen replacements and that
the five anchors inside line 1514 must be applied insertion-aware, then rebuild
the `.pdf` and `.txt`, and re-run `python sync.py`. The `kb/rules.md` re-sync is
not required by this stage, no pair touching §2. The five change requests filed
here — chiefly the unowned `openActiveTurn` retirement condition and the
missing producer for §4.1's distribution-reporting balance sim — are Director
decisions and are not gating.
