# Continuity gate — run `t-cap-alias-4`

`source/MANIFEST.txt` present (no `sync-missing`). `gdd.md` md5
`94c67ebe95a09414485cc2a07822f9b5`. One file gated:
`sections/rules_t-cap-alias.md` (four OLD/NEW replacement pairs) — and no other.

Top-level verdict: **PASS** — 0 violations, in 1 of 1 section.

---

## `sections/rules_t-cap-alias.md` — **PASS** (0 violations)

No violations of any type. What was checked, and against what:

**The four deletions all landed, and each cut site reads as finished prose.**

- Pair 2's T-CAP-05 paragraph now reads
  "**T-CAP-05 is the exception.** No `T-TURN-` ID asserts it. It is discharged
  *structurally* by T-FAME-05 and T-FAME-06 — an objective's owner does not
  change until the capture completes, and the tally counts owners — but **no
  gate asserts it end to end, and it appears in no acceptance set.**"
  Three complete sentences; the second no longer promises a clause that isn't
  there. The run-3 `invented-fact` is gone: `objectivesHeld` occurs zero times
  in the file, as does `caller-supplied`.
- Map row 2 is `| T-CAP-02 | **T-TURN-05** | the mutual-passivity guard |` —
  four `|`, three cells, matching the three-column header. `verbatim` occurs
  zero times in the file.
- Map row 3 is one line, four `|`, three cells; the Why cell now describes
  T-TURN-05's fixture and stops. `which is T-CAP-03's case` occurs zero times.
- The Open-questions row still poses its question with the clause removed:
  "**T-CAP-05 has no gate and no acceptance-set home.** … Whether it gets an
  asserting test is a Director call". `every other` occurs zero times.

**OLD blocks.** All four resolve to exactly one site in `source/gdd.md`:
pair 1 → line 353; pair 2 → lines 369–372 (item 8, blank line, blockquote
opener); pair 3 → line 119; pair 4 → line 2391. Byte-identical, including the
blank line inside pair 2.

**Table mechanics.** Pair 3's NEW line carries five `|` / four cells against
§2.0's `| ID | The player experiences | Rule source | Observable check |`.
Pair 4's NEW line carries five `|` / four cells against §4.7's
`| ID | Question | Blocks | Assumption in force until ruled |`. Neither NEW
cell introduces a `|`. Pair 2's inserted table sits after a blank line at
column 0, so it terminates the numbered list cleanly before the blockquote.

**Every substantive claim in the NEW blocks is grounded in `source/`.**

- "§4.7 Spec Stub 5 gates as `T-TURN-01..09`" ← §4.7 Stub 5, "Acceptance:
  T-TURN-01..09" (line 1760), and §3's ledger row "T-TURN-01..09 (9/9)".
- Row 1 "flag death ends the match at once; the tiebreak is never evaluated"
  ← T-TURN-02 "flag death ends the match immediately" + §2.8 T-CAP-01 "the
  tiebreak procedure is never evaluated".
- Row 2 "the mutual-passivity guard" ← T-TURN-05, that exact phrase.
- Row 3's "4 objectives + zero kills losing to 1 objective + one 50-Fame kill"
  is attributed to T-TURN-05's fixture, not to §2.8; the 50 is T-FAME-07
  ("Infantry 50"). "That combat Fame excludes passive income is **T-FAME-01**"
  ← T-FAME-01 "passive income never touches fameCombat".
- Row 4 "no capped tally can contain the +500, because a flag kill ends the
  match before the cap" ← §2.8 "The flag bonus (+500) can never appear in a
  capped tally: destroying the flag ends the match immediately".
- Rows 6, 7, 8 ← T-TURN-07 ("tiers are categorical"), T-TURN-09
  ("determinism"), T-TURN-03 ("factories only, towns excluded").
- "the tally counts owners" ← §2.8 criterion 2, "Ownership only: a capture in
  progress (§2.7) counts for nobody until the objective flips."
- `T-TURN-04` occurs zero times, as Fact X requires.

**No `stat-drift`:** no number in the file differs from its GDD value, and the
Change-requests section correctly reads "None" because none moves.

**No `unverified-claim`:** the only commit named, `ad77b13`, appears in the
Grounding section as the source of the mapping, not as backing for the ruling,
and §3 already carries `cpp_reference/test_turn.cpp` @ `ad77b13`. No NEW block
cites a commit, per Fact W.

**No `dead-reference`:** §2.0, §2.7, §2.8, §4.7, §4.11, Stub 5, Q14, T-TURN-02
/03/05/07/09, T-FAME-01/05/06 and the kb victory table (`kb_rules.md`,
"## Victory & outcomes (§2.8)") all resolve.

**No `placement-collision`:** four pairs, four disjoint sites, one file.

**No `kb-desync`:** `kb_rules.md` carries no test IDs at all — zero `T-CAP`,
zero `T-TURN` — so an alias map over test IDs cannot falsify it. The routine
§2 re-sync at merge still applies.

---

## Not violations — the highest-risk phrases, named at the orchestrator's request

None of these is filed. None blocks. Listed most to least serious, each with
the deletion that would remove the risk, since a deletion is the preferred
outcome.

1. **The map's caption repeats pair 1's lead-in almost word for word.**
   Pair 1: "The map below names, for each invariant, the ID or IDs that gate
   it; one row names none." Pair 2, roughly ten lines below it in the merged
   §2.8: "*Alias map — the ID or IDs that gate each invariant above; one row
   names none:*". After merge §2.8 says the same sentence twice. **Deletion:**
   drop pair 2's caption line entirely — pair 1 already announces the map, and
   the table's own header column reads `§2.8 | Aliases to | Why`. This is a
   one-line cut inside a NEW block; it needs no new reasoning.
2. **"4 objectives" / "1 objective" sits ten lines under §2.8 item 3's "4
   factories" / "1 factory".** The nouns differ for the same numbers. Run 3's
   cut removed the claim that they are the same case, which was the actual
   error; what remains is correct, because the cell says "T-TURN-05's fixture
   is". The residual risk is a reader inferring the identity the cut removed.
   **Deletion if you want it gone:** cut the sentence "T-TURN-05's fixture is 4
   objectives + zero kills losing to 1 objective + one 50-Fame kill." and let
   the Why cell read only "That combat Fame excludes passive income is
   **T-FAME-01**". The Aliases-to column already carries the mapping.
3. **Standing document tension, not this draft's fault, and not fixable
   inside it.** §4.7's register head says "the gates they blocked outright
   (T-FAME-02, T-FAME-04, T-FAME-05, T-FAME-07, T-AI-06 and the T-CAP- tally
   suite) now assert", and Q6's row says "T-FAME-07 and the T-CAP- tally suite
   unblocked." After merge, §2.8 will say "no gate asserts it end to end" of
   T-CAP-05. These reconcile only via Q14, still open, whose Blocks cell names
   T-CAP-05 — so the document already treats T-CAP-05 as not closed. Not filed:
   the draft's negative is Director-verified (Fact U) and must not be softened,
   the draft does not touch the register head, and the register head is scoped
   to the five ruled rows. **Director action, not author action:** either the
   Open-questions item already filed covers it, or §4.7's two "T-CAP- tally
   suite" phrases get narrowed at a later revision.
4. **"the tally counts owners" is glossed onto T-FAME-06.** T-FAME-06 reads "a
   captured objective's income flips to the new owner" — income, not the
   objectives-held tally. The clause is true and grounded, but in §2.8
   criterion 2 rather than in the invariant it sits beside. Not filed because
   Fact U supplies the T-FAME-05/06 pairing as a standing fact.
5. **"§4.11 row 4" as the locator for T-FAME-01** (Grounding section only).
   §4.11 row 4 exists and lists `T-FAME-01..09`, so the reference resolves —
   but T-FAME-01's *text* lives in §4.7 Stub 4, and §4.11 is the build order.
   Grounding is not merged prose, so this reaches no reader of the GDD.
6. **The file has no heading literally named "Draft".** The four `## Pair N`
   sections with OLD/NEW blocks are the draft, are unambiguously labelled, and
   are mechanically merge-ready, so I do not read this as `format-breach`. It
   is the addendum format, and it was the format in runs 1–3.

---

## Verdict

**PASS.** `sections/rules_t-cap-alias.md` clears the gate with zero violations
and merges as written; nothing must happen before merge. All five phrases run 3
named — the Stub 5 interface claim, "verbatim", "which is T-CAP-03's case", the
"every other `T-CAP-` citation" clause, and the interface clause's tail — occur
zero times in the file, each cut rather than repaired, and each cut site still
reads as whole sentences and parses as whole table cells. The six items named
above are not violations and none of them is worth another round: items 1 and 2
are optional one-line deletions the Director can make at merge time with no
author involvement and no re-gate, item 3 is a pre-existing §4.7 looseness this
addendum neither creates nor can fix, and items 4 through 6 reach no reader of
the merged document. If you want the shortest file, take deletions 1 and 2 by
hand at merge; do not re-spawn the author for them.
