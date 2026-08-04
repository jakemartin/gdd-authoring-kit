# Gate report — run `row5-rebuild-2`

- **Master**: `source/gdd.md`, md5 `9742f695f71d625763d9a3eeef21e70b` (from `source/MANIFEST.txt`).
- **Sync**: `source/MANIFEST.txt` present. Three entries — `gdd.md`, `kb_rules.md`, `kb_setting.md`.
- **Top-level verdict**: **PASS**
- **Total violations**: **0**

---

## `sections/tech_row5-rebuild.md` — **PASS**, 0 violations

### The one finding from `row5-rebuild-1` is cleared

At `row5-rebuild-1` this file carried a single `format-breach`:

> draft: `## Rule gaps found while writing the gates — 4`
> required: `## Change requests`

Both required heading strings are now present verbatim — `## Change requests`
and `## Open questions for the Director` — with their bodies unchanged. The
count of four moved into a body lead-in, which the required-heading rule does
not touch. The breach is repaired.

### Ruling on the question the orchestrator raised: heading *order*

**Order is not part of the convention. Only the heading strings are.**

The required-output rule enumerates the headings a section must carry —
Placement, Draft, Change requests, Open questions, Grounding — and states no
sequence among them. `format-breach` fires on a *missing* required heading, not
on a permuted one. The author's decision to keep Open questions before Change
requests, so that the last Change-requests bullet's "The harness question
**above**" resolves, is therefore permitted, and the cross-reference is in fact
correct as written: the harness question is item 2 under `## Open questions for
the Director`, which precedes `## Change requests` in the file. Nothing is filed
against it, and this is a settled answer for subsequent rounds — do not re-file
heading order, in this file or any other.

### What was verified rather than taken on report

The orchestrator's claim that all fifteen `OLD` blocks are byte-identical to the
`row5-rebuild-1` version was not accepted as a fact; the property that actually
matters — that each `OLD` matches `source/gdd.md` exactly once document-wide —
was re-derived directly against the master at this md5. All fifteen match once:

- Pairs 1–8 resolve inside the §3 status paragraph (`source/gdd.md` line 1511).
  Uniqueness for Pair 3 rests on the substring `row 5 has no in-editor half`,
  which distinguishes it from the row-4 and row-6 copies of the same sentence
  shape; uniqueness for Pair 7 rests on ``the eleven `main()` definitions``,
  which distinguishes it from the row-6 sentence naming *ten*.
- Pair 9 → line 1520 (ledger table, Turn loop cell). Pairs 10 and 11 → line 1528;
  Pair 10 is disambiguated from the Capture & Fame sentence by the leading
  `**Turn loop & win / tiebreak** joined at`.
- Pairs 12, 13, 14 → line 1582 (§4.5, *Specification outruns the build*).
- Pair 15 → lines 2743–2744 (§4.11 prose), including its internal line break.

The Placement header's classification was re-checked and is correct: **Pair 8**
is the only pair whose `NEW` contains its `OLD` verbatim as a prefix, and **Pair
7** is a replacement by the byte test despite appending, because its `OLD`
terminates in the paragraph-closing `*`.

### Arithmetic and blast radius re-derived

- §4.5 green count: source reads `**49** of the 70 are green` with the split
  18 + 9 + 9 + 6 + 7 = 49. Pair 13's `**50**` with 18 + 9 + 9 + 6 + 7 + 1 = 50
  is consistent, and Pair 7 declares the same 49 → 50 move.
- §4.5 unclosed count: source `**21 IDs remain unclosed**` enumerates T-DATA-05,
  three `T-SCN-` IDs, `T-TURN-10`, and 16 in rows 8–10 = 21. Pair 14's `**20**`
  drops `T-TURN-10` alone: 1 + 3 + 16 = 20. Consistent with Pair 7's 21 → 20.
- Written-ID count `**70**` and verified-ledger-row count `**9**` are untouched
  and remain true: row 5 already carried a ✓, so no row flips and §3's
  `**Nine rows carry a ✓**` does not move.
- `T-TURN-10` appears at five sites in the master (§2.8 invariants preamble,
  §4.5 twice, §4.7 Stub 5 `Acceptance: T-TURN-01..10`, §4.11 build-order table).
  The only two that assert its *status* are both in §4.5 and both are repaired,
  by Pairs 12 and 14. No unedited site is left asserting that T-TURN-10 is
  not green.
- `ad77b13` appears at five lines; every one is either edited (Pairs 2, 9, 10,
  13, 15) or retained deliberately as a historical record with a forward
  pointer. No sentence is left claiming row 5's *current* evidence is `ad77b13`.
- The draft's change request that Q8(b)'s renewal boundary is absent from the
  document was checked at its source: §4.7 Stub 5's T-TURN-10 text reads only
  `the owner's turn`, with no per-side-turn/per-round distinction. The gap is
  real, and filing it as a change request rather than editing the invariant is
  the correct disposition.
- The `## Findings my scoping brief did not name` claim about §3's "Six IDs are
  still recorded as **uncovered**" sentence was checked against line 1528: it
  enumerates two unwritten (T-MOVE-07, T-SCN-10) and four written-and-not-green
  (T-DATA-05, T-SCN-08/09/11). With `T-TURN-10` green at `6ccd40b` the sentence
  is correct as written, and correctly no pair touches it.

### Grounding checked claim by claim

Every substantive number, ID range, file path and commit in the fifteen `NEW`
blocks traces either to `source/gdd.md` at this md5 or to the round's standing
fact block: the 14-file modify-only path list, the eleven `main()` definitions,
`T-TURN-01..10` 11/11 with 11 counting printed checks over ten IDs, pass-1 5/11
over five distinct failing IDs, `120 AI commands issued across 6 games`,
`GATE-DRV-01..11` 11/11, the three carried-in Director rulings, and the
GDD-first sequencing (`ff6b78b` / `18fae0a`). The commit-message caution was
honoured: nothing in the draft restates `T-TURN-01` as showing "five checks";
Pair 7 reports two printed lines and names both. No `unverified-claim` arises —
every gate figure is stated with its commit, its compilers and its ID set, and
the unestablished harness for `6ccd40b` is explicitly declared unstated in Pair 7
and filed as Open question 2 rather than asserted.

### Other checks that produced nothing

- **`dead-reference`**: no link to `6ccd40b` is introduced anywhere, which is
  what Pair 11's exception sentence promises and what the unpushed state
  requires; every commit that *is* linked in a `NEW` (`9086d6a`, `ad77b13`,
  `d8284f1`) is already linked in the master.
- **`kb-desync`**: no pair touches §2 rules text, §2.13 map data or §2.11
  screen material, so `kb_rules.md` and `kb_setting.md` are unaffected.
- **`placement-collision`**: one section in this stage; every pair names a
  distinct anchor and each anchor is unique in the master, so the fifteen edits
  are mechanically mergeable in any order.
- **`voice-drift`**: declarative present tense throughout; the tense repairs in
  Pairs 4 and 5 move two present-tense falsehoods to commit-pinned past, which
  is a correction of register, not a drift from it.
- **`scope-breach`**: the §4.4 week-1 "provisionally met" passage is left
  untouched and raised as Open question 1 rather than ruled, which is the
  correct lane.

---

## Verdict

`sections/tech_row5-rebuild.md` **PASSES** with zero violations, and the
top-level verdict for run `row5-rebuild-2` is **PASS**. The single
`format-breach` from `row5-rebuild-1` is repaired by the two heading renames,
and the section order the author preserved is not a breach — the convention
governs heading strings, not their sequence, and that is now settled for
subsequent rounds. Nothing further is required before merge: the Director may
apply the fifteen `OLD` → `NEW` pairs against `Stratocracy_Prototype_GDD.md` at
md5 `9742f695f71d625763d9a3eeef21e70b`, then rebuild the `.pdf` and `.txt`,
re-sync `kb/rules.md`, and re-run `python sync.py`. Three items travel with the
merge as Director business rather than as gate conditions: the four filed change
requests (none of which edits invariant text here), the three open questions —
in particular the unestablished harness for `6ccd40b`, which Pair 7 correctly
declares unstated rather than inventing — and the standing coupling that
pushing `6ccd40b` obliges relinking its citations and retiring Pair 11's
exception sentence in the same edit.
