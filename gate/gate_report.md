# Gate report — run `t-ui-05-built-3`

Master GDD md5 `5075d853166d99858fd3a5a4b7dfc27c` (`source/MANIFEST.txt`
present, three entries; `kb_rules.md` @ `024523449be1873c9d545dbea6d3bc9d`,
`kb_setting.md` @ `b3e9e89daaef1cdeb333e3fb4368d1c0`). Section read:
`sections/tech_t-ui-05-built.md`, the only file this stage produced.

**Top-level verdict: PASS.** Zero violations, in one section.

---

## `sections/tech_t-ui-05-built.md` — PASS (0 violations)

No violation is filed. Nothing below is a finding; it is the record of what was
put to a test that could have failed, so that a later run does not have to guess
what this one covered.

### Deletion blast radius — the question this run was spent on

The apparatus lost several parentheticals, two OLD-span restatements, the
spellings enumeration, the blast-radius bullet, the grounding bullets' figure
lists and line numbers, restatements inside change requests 1 and 2 and open
question 1, and an inference in open question 2. Each surviving passage that
could have depended on removed text was read against what remains:

- **Change request 1** now supports its ask from two surviving pieces — the
  ledger rule it quotes verbatim (`**Author = human** for anything a human
  hand-wrote or substantially edited`, §3) and Pair 5's record of who wrote the
  code at `41a1452`. The ask (`agent+human`, or a per-commit split) is a value
  the §3 legend already admits (`**Author** ∈ {agent, agent+human, human}`), so
  the "Why" still reaches the ask.
- **Change request 2** quotes §4.10's clause in full rather than by reference,
  so removing the restatement cost it nothing; both limbs of its either/or name
  a site that exists (§4.10's omission clause; §4.7 Stub 8's `spawnBlocked`
  derivation), and its precedent — row 7's Q32 registration — is stated in §3.
- **Change request 3**'s premise `Q32 is the highest registered row` holds: the
  §4.7 register table's last row is **Q32** and §4.8 follows it. Its three
  touched sites are the register's two extent-bearing sites plus the
  authoritative table, which §4.7 itself names.
- **Open question 1** stands alone: it states the amended ruling's two re-opening
  conditions in its own words and cites Pair 5 for the two artifacts it asks
  about, both of which Pair 5 records (the widened `snapshot` render, the new
  `DriverUnit` field).
- **Open question 2** states the candidate convention as a quoted rule rather
  than relying on the deleted inference, and the episode it refers to is
  recorded in Pair 5's merging text, not in deleted apparatus.
- **Substitutions of the form "cites Pair 5"** were checked in the direction that
  matters — the cited pair carries the claim. Pair 5 states the authorship, the
  `DriverUnit` field, the render change and the clause-(b) episode.
- **No dangling comparison or pronoun** was found in the surviving notes. The two
  remaining blast-radius notes (Pairs 14 and 16) each quote the clause they
  displace, so each is intelligible without the deleted bullet.

### Arithmetic — still the sole home of every figure, and still complete

Re-derived rather than re-read, since the sweep moved material into it:

- written **71** unchanged (no acceptance ID minted at `41a1452`);
- green **52 → 53**, and the per-commit list re-sums: 18 + 9 + 9 + 6 + 7 + 1 + 2
  + 1 = 53, against the master's current 18 + 9 + 9 + 6 + 7 + 1 + 2 = 52;
- unclosed **19 → 18**: 1 + 3 + 2 + 12 = 18, and 53 + 18 = 71;
- §3 uncovered **9 → 8** = 2 unwritten + 6 written-and-not-green, and 6 + 12 = 18
  reconciles §3's remainder with §4.5's unclosed list;
- verified ledger rows **9**, rows carrying evidence without a ✓ **3** (rows 2, 7,
  8) — both unmoved;
- field contract **27 = 22 + 5**, recounted off Stub 8: per-hex 2 + per-unit 11 +
  per-factory 5 + per-side 5 + match 4 = 27; DECLARED DERIVED marks
  `isGuidedMarked`, `spawnBlocked`, `objectivesHeld`, `survivingHP`,
  `incomePerTurn` = 5;
- `test_ui` 34/34 with pass-1 21/34 → 13 FAIL, on the same shape §3 already uses
  for `7c36303` (14/14, pass-1 10/14, four FAIL lines);
- output lines **76**, **82**, **101** are stated once, in the arithmetic table,
  and are used once, in Pair 5.

No figure appears in the apparatus outside that table except span-shape counts
in the pair notes ("four master lines", "two master lines", the nine-space
continuation indent, "five unwrapped master lines"), which are properties of the
edit and not figures of the document.

### Standing checks re-run against the pairs

- **Every `T-UI-05` site in the master is accounted for.** The eight sites the
  draft names are the eight the master carries (§3 status paragraph, §3 ledger UI
  row, §3 uncovered-ID paragraph, §4.4 week 3, §4.5 risk row, §4.7 Stub 8, §4.11
  lead-in, §4.11 † bullet). Every unpaired site was read: Stub 8's invariant
  text, its clause-(b) note, its `Acceptance: T-UI-01..02 and T-UI-05 headless`
  line and §4.11's † bullet state kind, subject or cut-line membership, not build
  status, so none is falsified by the closure.
- **The blast radius over the unimplemented claim is closed.** Every occurrence of
  `no code implements` / `implemented by no code` in the master (§3 ×4 across the
  status paragraph, the UI row and the uncovered-ID paragraph; §4.5 ×2; §4.7 Stub
  8; §4.11 lead-in) is inside an OLD span of Pairs 3, 4, 6, 7, 8, 10, 14, 15 or
  16. No occurrence survives the merge.
- **Status vocabulary stays distinct.** *written*, *unblocked*, *asserting*,
  *green*, *unwritten*, *reserved* and *blocked* are used in the master's senses
  throughout; the two *unwritten* IDs (T-MOVE-07 on Q2, T-SCN-10 on Q26) keep
  their state and are not folded into the six *written and not green*.
- **The row does not flip anywhere.** Pair 6 reproduces `| UI | agent | — |`; Pairs
  5, 7, 14 and 16 each state that the in-editor pass is now the whole of what row
  8 lacks; §3's "Nine rows carry a ✓ … and three more carry evidence without one"
  is untouched and stays true.
- **§2 is untouched, and no §2 statement is falsified.** §2.11.5's per-factory
  block reference and §2.11.1's DONE-bit passages name fields and owners, not
  statuses. `kb_rules.md` carries no gate status, no `T-UI-` ID and no commit, so
  nothing in this round makes it wrong: no `kb-desync`.
- **Pairs frame their rulings honestly.** Pair 6's note declares that the Author
  and Agent-verified cells are reproduced unchanged and files the Author question
  as a change request instead of editing it, which is the correct route for a
  value the draft cannot move.

### Examined and deliberately not filed

- **`ahead of the milestone table, not behind it` inside Pair 5's NEW.** The
  Director reports examining it. Concurred: the phrase is §3's own idiom, used
  three times in the same paragraph for rows 4, 5 and 6 in the same construction
  (`§4.4 schedules rows 4–5 for **week 3**, so this row is **ahead of the
  milestone table, not behind it**`), and Pair 5 uses it in a §3 insertion with
  §4.4 named only as where week 3 was scheduled, which §4.4's week-3 cell bears
  out. Run `-2`'s finding was against the *grounding bullet*, which no longer
  makes the claim. Nothing to file.
- **Pair 3's "The two snapshot fields" beside Pair 5's three-item "the snapshot's
  ruled additions".** The two lists are different sets described in their own
  terms: §3's unedited enumeration is the three *known-absent* fields row 8's
  landing left out, two of which became snapshot fields, while Pair 5 lists the
  snapshot fields ruled on 2026-08-04, which Stub 8's `lockedThisTurn` member
  shows includes `isGuidedMarked` (`the guided opening's other half, marked, is
  the snapshot field \`isGuidedMarked\` above and is not in this block`, ruled
  2026-08-04). Neither statement is false on that reading, and the Director's
  fact block groups the guided mark with the two new fields. Not a
  `contradiction`.
- **The arithmetic table's Source cell for the `test_ui` and `test_driver` rows**
  names the fact block, while the *Before* figures (14/14 and 12/12 at
  `7c36303`) come from master §3. The figures are grounded — §3 states both, and
  the Grounding section cites §3 for row 8's landing record — so no violation
  type applies; recorded only so the next sweep does not re-open it.
- **"§4.10's parenthetical"** describes a subordinate clause rather than a
  parenthesis, but the reference resolves to text that exists at the named
  section, in the Director's own words. Not a `dead-reference`.
- **Change request 1's closing clause "Pair 6 reports the authorship without
  pre-empting it"** reads correctly as Pair 6 reproducing the Author cell's
  existing report unchanged — which its own pair note states explicitly — so the
  citation is not filed as dead.

---

## Verdict

**PASS.** `sections/tech_t-ui-05-built.md` carries zero violations: all sixteen
pairs are true against `source/gdd.md` at md5
`5075d853166d99858fd3a5a4b7dfc27c`, every figure the file states is either in
the Director-supplied fact block or re-derivable from the master and is stated
once in the arithmetic table, the blast radius over `T-UI-05`'s unimplemented
status is closed at every site the master carries it, the two change requests
that would move a value the draft may not touch are filed as requests rather
than written into prose, and this run's subtraction sweep left no surviving
sentence depending on deleted support. The section is clear to merge. What must
happen before merge is the Director's own checklist and nothing from this gate:
apply the sixteen pairs at their stated placements, rebuild the `.pdf` and
`.txt`, re-sync `kb/rules.md` (unaffected by this round but rebuilt with the
master), leave §3's row 8 at `*pending*`, and rule on the three items this file
hands up — the UI row's **Author** cell, the `spawnBlocked` occupancy-versus-
terrain discrepancy between §4.7 Stub 8 and §4.10, and whether that discrepancy
is minted as a Q row.
