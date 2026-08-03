# Gate report — run `row7-3`

- `source/MANIFEST.txt`: **present**, resolved against the kit root
  `E:\MultiAgent\gdd-authoring-kit`. No `sync-missing`.
- `gdd.md` md5 at this run: `f456445d516e75e5e31a5b749157bfd2` — matches the
  manifest line. `kb_rules.md` and `kb_setting.md` read. `kb_rules.md` returns
  zero hits for `T-SCN|provenance|ledger|9086d6a|d8284f1|Q3[12]`; `kb_setting.md`
  returns two for `ledger`, both the Fame-flavour noun in §1 prose. No pair
  touches §2 text. No `kb-desync`.
- Files in scope: `sections/tech_row7-scenario-validator.md`, one file and
  nothing else.
- **Top-level verdict: PASS. Total violations: 0.**

---

## `sections/tech_row7-scenario-validator.md` — **PASS**, 0 violations

### The five `row7-2` violations are cleared, each re-checked on the bytes

| # | Was | Now |
|---|---|---|
| V1 | Pair 3 restated §2.13.7's stretch condition and attributed a ruling | Pair 3 now reads *"Each needs a stretch map authored as a scenario file, and **none was replaced by a synthetic map**."* — a run fact about what a fixture needs, not the four-clause test §2.13.7 owns at lines 1381–1392. No ruling attribution survives anywhere in the file. |
| V2 | `the shipped map supplies` in Pairs 6 and 7 | Absent at both sites. Pair 6 reads *"each having run only part of its fixture set"*; Pair 7 reads *"but ran only part of their fixture sets"*. Neither now implies fixture (c) is shipped-map-resident, which §4.11 line 2721 contradicts (*"keeping only the synthetic ceiling refusal (c)"*). |
| V3 | Q32 *Blocks* claimed widening moves the written-ID count | Now *"A ruling that mints an ID for one of the checks would move §4.5's written-ID count"* — minting only. Correct: §4.5 line 1558 counts **written** IDs. |
| V4 | Q32 *Assumption* carried *"nothing that passes today would start failing"* | Sentence gone. The cell ends at *"so the bullet describes more than the suite gates."* No universal remains. |
| V5 | — | As above; the file carries no ungrounded universal. |

The two author-raised items also land as described: Pair 4's trailing
`and neither stretch map is authored as one` is absent, and Pair 13 exists
against `**Reduced and re-scoped at 2026-08-02, not retired:**`.

### Check 1 — anchor disjointness, re-derived

I agree with the orchestrator's conclusion and do not need to show contrary
bytes, because I reached the same one. Located independently by grep against
`source/gdd.md`, every OLD block matches **exactly once**:

| Pair | Site | Count |
|---|---|---|
| 1, 2, 3 | line 1487 (tracker line) | 1 each |
| 4 | line 1501 (ledger table) | 1 |
| 5, 6, 11 | line 1504 (populated-rows paragraph) | 1 each |
| 7, 13 | line 1558 (§4.5 risk cell) | 1 each |
| 8 | lines 2357–2358 | 1 |
| 9 | lines 2398–2400 | 1 |
| 10 | line 2442 (Q31, the table's last row) | 1 |
| 12 | lines 2684–2685 | 1 |

**Pairs 13 and 7, the same §4.5 cell.** Line 1558 reads, in order:
`… **Reduced and re-scoped at 2026-08-02, not retired:**` — Pair 13's whole OLD
— then ` no new ID has been written since \`c224825\` — row 6's GATE-AI-SMOKE is
acceptance that deliberately mints none, so it closes a check without moving
this count — ` — which **no pair touches** — then `and **42** of the 69 are
green`, where Pair 7's OLD begins. The intervening run measures ~160 characters,
consistent with the reported 161-character gap. **Disjoint.**

**Pairs 6 and 11, the closest.** Line 1504 reads `… so that row records a
partial pass and stays unverified. *(Commit \`d8284f1\` is the head of \`main\`; …`.
Pair 6's OLD terminates at `stays unverified.`; Pair 11's OLD opens at `*(Commit`.
One space between them. **Adjacent, disjoint.**

`grep -c "is the head of"` over `source/gdd.md` returns **1** — I ran it, and it
settles E10 in the author's favour: the single site is line 1504, inside Pair
11's OLD. Pair 1's site reads `— the head of \`main\` in the crew repo` and does
not contain that string.

No `placement-collision`.

### Check 2 — seams left by the four mid-sentence deletions

Each surviving sentence was read as a sentence. All four are well-formed; no
dangling conjunction, no orphaned subordinate clause, no double punctuation.

- **Pair 3** — *"Each needs a stretch map authored as a scenario file, and
  **none was replaced by a synthetic map**."* Complete compound sentence; the
  deletion took a whole clause with its conjunction.
- **Pair 4** — *"— the four fixtures that did not run each need a stretch map
  authored as a scenario file — so the acceptance set is incomplete at this
  commit …"* The em-dash pair still closes; the `so` clause still attaches to
  `**T-SCN-08, T-SCN-09 and T-SCN-11 ran only part of their fixture sets**`.
- **Pair 6** — *"each written, unblocked and asserting, each having run only
  part of its fixture set."* Parallel participial appositives; terminal period
  present.
- **Pair 7** — *"which are written, unblocked and asserting, but ran only part
  of their fixture sets, and which leave row 7 unflipped"* The `but` still
  contrasts two finite verbs sharing `which`; the second `which` clause is the
  third item of the `20 IDs remain unclosed` list and its cell continues
  correctly into `; and the **16** in rows 8–10, which hold no code`.
- **Pair 10, Q32 *Blocks*** — two full sentences, the second beginning
  *"A ruling that mints an ID …"*. The unterminated final cell matches Q1's and
  Q31's *Blocks* cells, which also end without a period.
- **Pair 10, Q32 *Assumption*** — ends *"… so the bullet describes more than
  the suite gates."* Complete.

### Check 3 — arithmetic and counts, re-derived, not copied

- **Register size.** `^\| \*\*Q[0-9]+\*\* \|` → **31** rows. `\*\*RULED` → **15**.
  So 16 open today, matching the current preamble. Adding Q32: 32 rows, 15
  ruled, 17 open. Pair 9's list `Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31` + Q32 =
  3 + 10 + 4 = **17**. Consistent, and both extent-bearing sites named at lines
  2362–2365 are updated (Pair 8 the chain, Pair 9 the preamble).
- **§4.5 green.** 18 + 9 + 9 + 6 + 7 = **49**. Unclosed 1 + 3 + 16 = **20**;
  69 − 49 = **20**. Rows 8–10 confirmed at 16 from §4.11's own acceptance
  column (T-UI-01..04, T-INT-01..05, T-SAVE-01..07, lines 2706–2708).
- **§4.5 written stays 69** and *"no new ID has been written since `c224825`"*
  stays true — `GATE-SCN-PARSE` / `GATE-SCN-HASH` mint no numbered ID, on the
  `GATE-AI-SMOKE` precedent §4.7 line 2335 already names.
- **§4.5 verified ledger rows stays 9** — row 7 does not flip.
- **Ledger table ✓ count.** Counted directly at lines 1491–1502: nine ✓
  (Combat, Test suite, Hex, Movement, Economy, Turn, AI, Repair,
  Type-effectiveness). After Pair 4, two rows carry evidence without a ✓ —
  Data tables and Content / scenario — and UI stays `*pending*`. Pair 5's
  *"Nine rows … and two more carry evidence without one"* is correct.
- **Pair 6's six uncovered IDs.** 2 unwritten (T-MOVE-07 on Q2, T-SCN-10 on
  Q26) + 4 written-and-not-green (T-DATA-05, T-SCN-08/09/11) = 6. Q26 at line
  2437 confirms T-SCN-10 stays unwritten; §4.7 line 2292 confirms it is *"a
  different state: nothing is asserted, so nothing is waiting"*.
- **`main()` census.** Ten at `d8284f1` (line 1487) + `test_scenario.cpp` =
  eleven, split nine harnesses / one duel simulator / one REPL. The retained
  row-6 sentence is bound to *"the ten"*; the new record is bound to
  *"the eleven"*. No collision.
- **Twelve checks.** 7 (T-SCN-01..07) + 2 (GATE-SCN-PARSE, GATE-SCN-HASH) +
  3 (T-SCN-08/09/11 partial) = 12.

### Check 4 — citations, each resolved in `source/gdd.md`

Q2, Q22, Q26, Q28, Q29, Q31 all exist. Q28's option **(b)** reads literally
*"that seat's own `guidedOpening.infantry` alone"* at line 2439, so Pair 3's
*"which is reading (b) at Q28 and the one that ruling refused"* is exact.
§2.13.1's validation-invariants bullet at lines 830–835 carries all three of
Q32's quoted checks verbatim, and its fourth check (declared symmetry) is
explicitly gated by T-SCN-05 — so *"three checks"* is the right number.
T-SCN-02 (line 1906) and T-SCN-04 (line 1912) exist and, read as written, gate
none of the three. §4.2 `validate_scenario` exists (lines 830, 2297). §4.11's
† bullet (2718–2728), Stub 7's acceptance block (2289–2296) and the
critical-path paragraph (2755–2772) are all consistent after the merge. No
`dead-reference`.

### Check 5 — grounding, claim by claim

Every substantive claim in the pairs traces to a stated fact: the commit and
its parent (A1/E2), the six tracked sources (A2), the census (A3), the 12/12
and 11/12 results (B1/B2/E5), the twelve checks (B3), the four fixtures (B4),
T-SCN-10's distinct state (B5), the 99-hex transcription (B6), the GATE-* rule
(B7), the Claude Code authorship (B8), the off-critical-path fact (B9), and the
five rulings (C1–C5). C4 is honoured by absence: `[Pp]layable|week-1 goal`
returns **zero** hits in the draft. No `invented-fact`.

### Items considered and deliberately not filed

- **No literal `## Draft` heading.** The thirteen `## Pair N` sections are the
  draft, in the established addendum form this document has merged repeatedly,
  and the material is mechanically locatable. Filing `format-breach` here would
  file something that is not wrong. Recorded so the Director can overrule.
- **§3 line 1487, `row 7 is unbuilt` and `row 7 unbuilt`.** I decline to file
  these a third time; they are commit-bound to `ad77b13` and `d8284f1` and the
  draft reports them under Open questions, which is the correct disposal.
- **`GATE-SCN-PARSE` / `GATE-SCN-HASH` are not written into §4.7 Stub 7's
  acceptance block**, unlike `GATE-CAP-PARTIAL` in Stub 8. B7 places them
  outside the stub deliberately; Stub 7's *"the whole written suite"* refers to
  written `T-SCN-` IDs and is not falsified. An absence, not a false statement.
- **§4.5's mitigation column, *"Row 2 is now that clause's worked example rather
  than its hypothetical"*.** Row 7 becomes a second example; the sentence does
  not claim to be the only one, so it stays true.

---

## Highest-risk remaining phrases

Filed as nothing, listed as what I would check first with one more pass.

1. **§3 line 1487, `rows 4, 5 and 6 have since landed — all three recorded at
   the end of this paragraph`.** No pair touches it, and Pair 2 edits the very
   next clause of the same sentence. It stays true — row 7 is not subtracted
   from it — but it is an enumeration that has been extended at every prior
   landing and was not extended at this one. The next landing inherits the
   question of whether this is a `d8284f1`-scoped narrative or a live list. It
   is the single most likely site of the next stale-enumeration violation.
2. **Pair 3's `A change request out of the build is registered rather than acted
   on: §2.13.1's validation-invariants bullet names three checks no T-SCN- ID
   asserts as written`, against Q32's *Blocks* cell `no T-SCN- ID gates the
   three`.** One fact, two wordings, two sections. §4.7 does not claim sole
   ownership of question statements the way §2.13.7 claims the stretch
   condition, which is why this is not V1 — but it is the same shape, and a
   later edit to one wording will not find the other.
3. **Pair 3's `it is applied per acceptance ID as well as per row`.** New
   document content stated in §3 rather than in Q29's own register row. The
   draft's Open questions correctly flags that it has not been audited against
   rows 1–6. Until the Director rules it into Q29, §3 is the only site holding
   a rule with document-wide reach.
4. **Pair 3's `Those three IDs are written, unblocked and asserting`.** The
   antecedent sits two sentences back, across a four-item fixture list. A
   future insertion between them silently breaks it.
5. **Pair 13's `2026-08-03` and Pair 1's `stands at 2026-08-03`.** Two date
   tokens in two sections that must move together and share no anchor. The
   draft flags the first; the pairing itself is the risk.
6. **Pair 11's `reachable from the head of main`.** Correct now and designed not
   to stale, but it is the only remaining ancestry claim in the document and it
   is unfalsifiable from `source/` alone — it rests entirely on E4/E11.

---

## Verdict

**PASS**, one section, zero violations. All thirteen OLD anchors match
`source/gdd.md` exactly once and their spans are pairwise disjoint — including
Pairs 13 and 7 in the shared §4.5 cell, which I located independently and found
separated by an untouched ~160-character clause. All five `row7-2` violations
are cleared by deletion with no substitute assertion, and the four deletion
seams read as well-formed sentences. Every count in the draft — 49 green, 20
unclosed, 69 written, 9 verified rows, 32 register rows, 15 ruled, 17 open,
nine ✓ and two evidence-only ledger rows, eleven `main()` definitions, twelve
checks, six uncovered IDs — was re-derived from the master rather than taken
from the fact block, and each agrees. Nothing must happen before merge: the
Director may apply all thirteen pairs to
`../stratocracy-content/Stratocracy_Prototype_GDD.md`, then rebuild `.pdf` and
`.txt`, re-sync `kb/rules.md` (unaffected here, but the checklist step stands),
leave the §3 provenance ledger status as the partial pass Pair 4 writes, and
re-run `python sync.py`. The five open questions — the ledger row's label, the
reach of the per-ID Q29 reading, the two dropped shas, the §4.5 date stamp, and
the two line-1487 present-tense sites — are Director decisions, not merge
blockers.
