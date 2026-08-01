# Continuity gate — run `post-merge-21`

**Top-level verdict: PASS — zero violations.**

Manifest present. `source/gdd.md` md5 `3b9024f384162b32959416b66f5f1137`;
`source/kb_rules.md` md5 `e99ae4ec2c63dcadd6b5e5d5a66067bd` and
`source/kb_setting.md` md5 `b3e9e89daaef1cdeb333e3fb4368d1c0`, both unchanged
and therefore byte-identical to the copies verified in earlier runs. Everything
re-read from disk.

The delta is confined to the two-senses passage as stated: every anchor ahead of
it sits at the same line as last run (§1.6's "nine one-shot" at 69, §2.7's
"AI-only path" at 213, T-FAME-02's "each side's configured" at 1595, T-AI-06's
"ascending §2.4" at 1680), and the register table moved by exactly the three
lines the passage grew.

| Section | Verdict | Violations |
|---|---|---|
| §4.7 — the two-senses-of-*blocked* passage | **PASS** | 0 |
| §4.7 — Blocks-column sentence, provenance chain, preamble, rows Q1–Q31 | PASS | 0 |
| §4.7 stubs + §4.8–§4.11 — the blocked/reserved vocabulary | PASS | 0 |
| §§1–3, §4.1–§4.6 — untouched, anchors re-verified | PASS | 0 |
| `kb_rules.md`, `kb_setting.md`, `sections/` | PASS | 0 |

---

## The separation holds — the collapse did not move one clause along

The two predicates are now complementary rather than shared, which is the whole
test:

| Sense | What the passage says of it | Predicate |
|---|---|---|
| **written-and-blocked** (row states *no reading*) | "it **can be written** and parameterized on the row … but **it cannot assert** until the ruling lands" | can be written · cannot assert |
| **reserved and unwritten** (row states a reading) | "T-MOVE-07 is blocked on it in the sense that **it cannot yet be written**, not in the sense that it fails" | cannot be written · nothing to fail |

"Cannot be written" now belongs to exactly one of the two, and the modal in "can
be written" is what carries the distinction — a weaker and correct claim than the
"is written" it could have overreached to. Adopting the document's own term
rather than striking two words was the better repair: `written-and-blocked` now
appears three times in the document and means the same thing at all three (Stub
7's acceptance note, §4.11 row 7, and here), so the passage defines a term the
rest of §4 already uses instead of inventing a gloss beside it.

I also checked the universals the new clause introduces, since that is where this
paragraph has failed before:

- **"A row that states *no reading* blocks its gate outright"** holds for every
  no-reading row the register has ever carried — Q4, Q5, Q6, Q8, Q9 and Q28 —
  all six of which had a written gate that could not assert. Q28 is the one that
  could have been an exception, and is not: Q22's row records T-SCN-11 as
  "written, unblocked and asserting **since Q28 ruled**", so it was written and
  blocked while Q28 carried no reading. No live counterexample exists either, as
  no row states no reading today.
- **"none of the open rows blocks a gate *outright*"** is true as of this
  revision: gates on open rows either assert their row's reading (T-MOVE-03 on
  Q3, T-HEX-05 on Q1, T-SCN-01 on Q10, T-CAP-05 on Q14, T-SCN-03 on Q19,
  T-SAVE-01/02 on Q12) or are unwritten (T-MOVE-07 on Q2). Nothing is
  written-and-blocked anywhere in the document, which is what Stub 7 and §4.11
  independently assert for row 7.

---

## Your three questions

### 1. The history is right, and naming two of the five implies nothing false

Both claims verify against the sealed addendum's `OLD` blocks, which are the
primary evidence:

- **T-FAME-02**, on Q8 — `OLD`: "income: each held factory pays +100/turn, each
  held town +25/turn (§2.7); **accrual timing per the Q8 ruling**." Written,
  parameterized, unable to assert the timing. Written-and-blocked ✓
- **T-AI-06**, on Q9 — `OLD`: "determinism: same state → same move; every scoring
  tie is broken by a stated deterministic rule (canonical hex order for position
  ties; **remaining tie dimensions per the Q9 ruling**)." Same state ✓

And "before this revision" is right: both rows are marked "RULED (**this
revision**)".

**The other three were in the same state, so naming two is exemplary, not
exclusive.** T-FAME-04's `OLD` ended "waiting-build semantics per Q8";
T-FAME-05's ended "(N per Q4); interruption/reset semantics per Q4"; T-FAME-07's
ended "exact values per Q5/Q6; the gate pins whatever the Director rules". All
three were written and parameterized on their rows. The T-CAP- tally suite is the
same again — T-CAP-01..08 are written out in §2.8 and were blocked by Q6's
unpriced term. So all six items the preamble lists as blocked outright were
written-and-blocked, and "exactly the state T-FAME-02 and T-AI-06 were in"
carries no "only" that would misdescribe the rest.

### 2. "As §4.7's stubs prescribe" is accurate, and not a single sentence inflated

Two independent reasons:

- **The intro sentence is already general in form**, not an instance: "**Where a
  stub needs a rule the GDD does not state**, the gate is parameterized on a
  numbered open question — the Director rules, the gate then pins the ruling."
  It quantifies over stubs, so treating it as a prescription is reading it as
  written.
- **A stub prescribes it in its own invariant text**, which is what makes the
  attribution to "the stubs" correct rather than loose. T-MOVE-03: "Pass-through
  of friendly-occupied hexes: **parameterized on the Q3 ruling; until ruled, the
  gate asserts the conservative reading** (occupied hexes block pathing
  entirely)." That is a stub telling an implementer what to write and what it
  asserts while the row is open.

The only nicety available is that "as §4.7 prescribes" would name both the intro
and the stubs; nothing is wrong as written, and I would not spend an edit on it.

### 3. Leaving the third state out is right — the passage is about *blocked*, and T-SCN-10 is not blocked

Your reasoning is sound and I would not add it. The passage announces two senses
of *blocked* and defines both; T-SCN-10 is not a third sense of blocked but the
absence of blocking, and the document says so at its own site, twice, with the
contrast drawn explicitly rather than left to inference:

> **RESERVED BY DECISION, not blocked on an answer:** Q26 is RULED … **Nothing is
> waiting.** … **Contrast T-MOVE-07 above, which IS blocked, on the unruled Q2.**
> *(§4.7, Stub 7)*
>
> T-SCN-10 is reserved and UNWRITTEN on Q26, **which is a different state:
> nothing is asserted, so nothing is waiting.** *(§4.7, Stub 7 acceptance note)*

Adding a non-instance to a two-sense passage would widen the surface that has
produced the last two violations, for a reader who is already told the answer
where the question actually arises. **Your exclusivity anchor also re-verifies
this round:** searching every "reserved" in the document turns up exactly two
reserved *gates* — T-MOVE-07 and T-SCN-10 — and everything else is a reserved
*field* (`MoveClass`, `seed`). So "Q2 is the current instance" remains exact.

*One site to know about, offered as context and not as a finding — it is
pre-existing, unchanged this round, and correct in its own terms.* §4.11 row 7
says "the only unwritten invariant is T-SCN-10, **reserved on Q26**", and that
preposition is the same one "blocked on Q2" uses. A reader who arrives there
first could read "on" as "waiting on". Stub 7 disambiguates it twice for anyone
who follows the reference, which is why nothing is filed; if §4.11 row 7 is ever
edited for another reason, "reserved by decision under Q26" closes the last gap
in this vocabulary.

---

## Arithmetic and chain — re-derived from the live table

- **Thirty-one rows, Q1–Q31**, one per ID, no gaps or duplicates.
- **Ruled (15):** Q4, Q5, Q6, Q7, Q8, Q9, Q20, Q21, Q22, Q23, Q24, Q25, Q26,
  Q27, Q28.
- **Open (16):** Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31.
- 15 + 16 = 31; the preamble's enumeration is the exact complement. Your figures
  match mine.
- **The chain still covers all 31 exactly once:** Q1–Q10 (10) → Q11–Q13 (13) →
  Q14–Q20 (20) → Q21–Q22 (22) → Q23 (23) → Q24–Q25 (25) → Q26 (26) → Q27 (27) →
  Q28 (28) → Q29 (29) → Q30 (30) → Q31 (31). Contiguous, no overlap, no ID twice.
- **The preamble is untouched** and still carries "none of them blocks a gate
  outright" exactly once, wrapping the same line break.

## Everything else — unchanged and clean

§2.7's economy bullets and Q31 pointer; T-FAME-02's "each side's configured
value"; T-FAME-04; §2.9's economy phase; §2.11.5's Build-button rule; §1.6 row
2's "nine one-shot strings" against §2.11.6-C's nine triggers; Q6's five
cut-statement sites; Q9's two ascending-cost sites with the print-order
disclaimer; Q4 and Q5's figures. The withdrawn "commitment to read before
spending" still appears exactly once, inside the Q8 cell's retraction. Both kb
files correctly did not move — nothing this cycle touched a rule either of them
parses — and no UI string changed.

## Verdict

**PASS.** This is a clean run, and I am recording it as one rather than finding
something to say. The remediation defines the first sense with a predicate the
second does not share, uses the document's own term for it so §4.7, §4.11 and
this paragraph now say `written-and-blocked` and mean one thing, and grounds its
historical claim in evidence that holds for all six blocked-outright gates rather
than only the two it names. "As §4.7's stubs prescribe" is backed by a stub that
prescribes it. Omitting the reserved-by-decision state is the right call, and the
exclusivity it leans on survives another exhaustive search. The register arithmetic
and the provenance chain both re-derive. Nothing is owed before merge: no rule,
number, map, gate, register row or kb re-sync is affected, and `gate/accept.json`
records `post-merge-21` as PASS with every section clean.
