# Gate report — run `capture-pin-3`

`source/MANIFEST.txt` is present, re-read this run. `gdd.md` md5
`454d765e3bac6c02e3491c105328c7be`, unchanged across all three runs and matching
the md5 recorded in `source/FACTS_capture-pin.md`. No `sync-missing`.

Sections read this stage: `sections/tech_capture-pin.md`, and only that file.

**Top-level verdict: PASS.** Zero violations. The `dead-reference` from
`capture-pin-2` is closed, and closing it introduced nothing.

---

## `sections/tech_capture-pin.md` — PASS (0 violations)

### The `capture-pin-2` finding is closed

`Grounding` row 6 now reads:

> | The fixture is committed at `c2f5860`, not at `11ef8ce` | CORRECTION to FACT 1 and its CORRECTION; §3 names that commit for the fixture in its own wording, *"The committed fixture carries the complete §4.9 command set at"*, where the commit follows as a Markdown link |

Both claims of that quotation were measured this run, separately:

- **The string exists.** `The committed fixture carries the complete §4.9 command
  set at` occurs in `source/gdd.md`, searched newline-insensitively with no result
  limit.
- **It exists where the row says.** It occurs **exactly once**, on line 1516,
  which falls between the `## 3. AI Architecture` heading at line 1425 and
  `## 4. Technical Strategy` at line 1544 — §3, and §3 only. The capitalised form
  does not appear at line 1569 (§4.4) or line 3281 (§4.11), which is where the
  lower-case bare-backtick wording lives.

The truncation before the commit is correct rather than tolerated: line 1516
continues `[`c2f5860`](https://github.com/…)`, so the row's own note — *"where
the commit follows as a Markdown link"* — is what the master does, and cutting
the quotation at `at` is the only way to quote §3 verbatim.

**The superseded wording is gone from the draft.** Searching
`sections/tech_capture-pin.md` for `command set at `c2f5860`` returns no match, so
the misattributed form survives nowhere in the file. Where the SHA still appears —
row 6's claim column, and Pair 1's `Note:` — it is the draft's own assertion, not
a quotation of the master, and carries no attribution to verify.

### Nothing else moved — verified, not taken

The file was compared line by line against the `capture-pin-2` revision as I read
it in this session. Lines 1–54 and line 56 are identical; line 55 — `Grounding`
row 6 — is the only line that changed, and the file's length is unchanged. That
means the two `OLD` blocks, the two `NEW` blocks, both `Note:` paragraphs, all
five headings and the other six `Grounding` rows are byte-identical to text this
gate has already found clean, so none of it is re-opened.

### The two `OLD` blocks

Re-run this round, newline-insensitively, with no result limit, on the full block
text rather than a prefix. Each matches `source/gdd.md` exactly once, both on line
1516 — inside §3 as bounded above, on the 99,939-character §3 ledger line. Both
placements still merge mechanically, and `## Placement` — *"Both pairs replace
text in §3; nothing outside §3 moves"* — is true of both.

### Every quotation in the draft, under the two-claim rule

Applied as the standing note asks, to each of the six quotations the draft makes.

| Quotation | String | Attribution |
|---|---|---|
| Row 1 — *"The fixture carries the kind because `appendAiTurn` appends one `Capture` per side at the close of that side's turn"* | Occurs, once | Line 1516, §3 — measured |
| Row 2 — *"The tree was corrected at the crew tip; the message cannot be."* | Occurs, once | Line 1516, §3 — measured |
| Row 6 — *"The committed fixture carries the complete §4.9 command set at"* | Occurs, once | Line 1516, §3 — measured |
| Pair 1 `OLD` | Occurs, once | Line 1516, §3 — measured |
| Pair 2 `OLD` | Occurs, once | Line 1516, §3 — measured |
| Pair 2 `NEW` — subject line `Name the unvendored module Balance, not Selfplay`, attributed to `5072d10` | — | **Not measured by me.** Both claims rest on FACT 5, which records that subject for that commit from `git` in `stratocracy-crew`. I have no access to that repo this run and am not reporting it as verified. |

The same limit applies to Pair 1's `{"turn": 7, "side": 0, "kind": "Attack"}`,
attributed to the fixture's command log: string and location both rest on FACT 1's
measurement of `data/parity_fixture.save`, not on one of mine.

Every fact-block label the draft cites exists in `source/FACTS_capture-pin.md`:
FACT 1, FACT 2, FACT 3, FACT 5, FACT 6, the CORRECTION to FACT 1, the CORRECTION
to FACT 2, the CORRECTION to FACT 5, and — new this run and cited by row 6 as
*"its CORRECTION"* — the `CORRECTION to the CORRECTION to FACT 1`.

### Carried forward from the runs that passed these checks

Re-stated rather than assumed, because each was measured against text that has not
changed since.

**Sufficiency.** Pair 1 states *"That append is conditional rather than automatic
— `g.turn.running` must be true at that close, among other conditions the emitter
applies"*, naming one necessary condition and leaving the set open, as the
CORRECTION to FACT 2 requires. Row 3 restates it the same way. Neither the pair
nor the apparatus closes the condition list, in an enumeration or in a summary
sentence.

**The inferred fact.** The turn-7 explanation reads *"what follows from that
record is that the match ended during that side-turn"*, and row 5 labels it
INFERRED as FACT 2 does. Not promoted.

**Numbers.** Twelve `{turn, side}` pairs, turns 1 through 6, the set identity with
`EndTurn`, each append carrying a `unit`, the turn-7 final entry, `result`
`Decisive`, eleven commands at turn 7 side 0, the 32-iteration bound — all match
FACTS 1 and 2. No `stat-drift`.

**Pins.** `c2f5860` occurs 10 times in `source/gdd.md` and the pair agrees with
those sites; `11ef8ce` occurs 0 times and is a new pin on the CORRECTION to
FACT 1; `5072d10` occurs 0 times and is a new pin on FACT 5. Each SHA was probed
on its own term, under the rule adopted after the `capture-pin` correction.

**The since-list.** Pair 2 writes the commit, its subject line and the one file it
changed, and not FACT 5's three-commit list or its ancestry claim, per the
CORRECTION to FACT 5. No unpinned exhaustive claim enters the master.

**Referent.** Pair 2 still calls `5072d10`'s text a *subject line* and reserves
*message* for crew `9289c1d`'s, which is the master's topic message in that
passage.

**Scope, placement, KB, apparatus.** Both pairs sit in §3; one section this stage,
so no `placement-collision`; §2 untouched, so no `kb-desync`; no acceptance ID
minted, closed or re-dated and no test ID claimed as passing, so no
`unverified-claim`; the no-closure finding is untouched, so the pronoun ruling
does not reach this draft. The `Grounding` table is evidence for the pairs and
carries no sweep narrative, no coverage claim and no summary of what was not
changed. All five required headings are present, so the `capture-pin`
`format-breach` stays closed. `Disposition of every candidate` and `Handoffs` are
not in the required list and are not filed.

---

## Standing note — a quotation makes two claims

Recorded because it changed this gate's method mid-round and should outlive it.
A quotation asserts that the string exists **and** that it exists where it is
said to. Verifying presence verifies the first only. In this document the two come
apart routinely, because §3 writes SHAs as Markdown links while §4.4 and §4.11
write the same sentence with bare backticks — so the two wordings differ by
interior markup alone, exactly what FACT 7 records as making a literal search miss
a sentence that is present. Every master quotation in this report was measured for
both claims this run, and the one quotation I could not measure — Pair 2's commit
subject line — is marked as resting on FACT 5 rather than reported as verified.
That marking is the point: an unmeasured claim in a gate report is cheap, and a
falsely measured one is not.

---

## Verdict

`sections/tech_capture-pin.md` is **PASS**, with zero violations, and the
top-level verdict for run `capture-pin-3` is **PASS**. The `format-breach` from
`capture-pin` and the `dead-reference` from `capture-pin-2` are both closed, and
the fix for the second touched one line and no other. Both `OLD` blocks match
`source/gdd.md` exactly once each inside §3, all three of the table's master
quotations were checked for string and section separately and all three resolve to
line 1516 under `## 3. AI Architecture`, every number traces to FACTS 1, 2 and 5,
the sufficiency trap is avoided in the pair and in the apparatus alike, and the
moving `crew tip` referent is replaced by a commit without importing the unpinned
since-list. Nothing must happen before merge: the draft may go to the Director for
merge into §3 at the placement it specifies, with the reminder that the master GDD
is the Director's to edit and that `kb/rules.md` needs no re-sync for this round
because §2 does not move.
