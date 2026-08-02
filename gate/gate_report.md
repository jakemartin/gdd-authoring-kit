# Gate report — run `row4-playable-3`

- Master: `source/gdd.md`, md5 `6a446c9408cbaf838a57f3326617e4d3` (from
  `source/MANIFEST.txt`, present — no `sync-missing`).
- Sections gated this run: one — `sections/tech_row4-and-provisional-playable.md`.
  Every other `.md` in `sections/` either carries the "✅ APPLIED ADDENDUM — DO
  NOT RE-APPLY" banner (27 files) or is a stage-1/stage-2 original already merged
  (`rules.md`, `scenario.md`, `ux.md`); none was produced by this stage.
- **Top-level verdict: PASS.** Zero violations.

---

## `sections/tech_row4-and-provisional-playable.md` — PASS (0 violations)

The three `row4-playable-2` `contradiction` findings are closed, and closed the
way the finding asked — by deletion, not by substitution.

1. **"No bare *now* remains in §3's status paragraph…"** — the sentence is gone
   from the file. It has no successor: nothing in the front matter now asserts
   the paragraph is clear of unbound markers, and the *now* the table
   deliberately keeps ("that row **now** states the arithmetic") is still carried
   as a **Kept** row with its reason.
2. **The §4.11 row that denied the site** — replaced. The table now reads
   `| §4.11 preamble | "rows 1 and 3 have **since** flipped" | Carried forward,
   not removed: pair 14 rewrites it to "rows 1, 3 and 4 have since flipped"… |`,
   which quotes `source/gdd.md` line 2640 exactly and gives it a disposition
   that matches pair 14's own NEW.
3. **The two undisposed survivors** — both now have rows, and both dispositions
   check out against source. `| §3 status | "the row 2 module, whose ledger row
   is **still** unflipped" | Kept. True of row 2 at 647d4df…` matches line 1466;
   `| §3 populated | "`crew/tasks.py` is **still** written against the Combat
   spec alone" | Kept…` matches line 1483, and its stated reason — the file is
   byte-unchanged `5ffa8d6` → `647d4df` — is Fact I at Fact I's own extent.

### The completeness test, run explicitly

No completeness claim survives in any form. The one sentence that could be read
as a successor is:

> The table records the markers this addendum examined in the four paragraphs it
> moves, and what it did with each.

This is a caption on the table, not an assertion about the document: its scope is
"the markers this addendum examined", so it makes no claim that the four
paragraphs contain no other marker, and it hands the next author no clean bill on
anything the table omits. That distinction matters here, because the paragraphs
do carry unbound present-tense claims the table does not list — "the editor pass
is not yet due" and "T-DATA-05 … has not run" (line 1466), "stays unverified"
(line 1483), "**Row 2 is not green:**" (line 2644). Each remains true at
`647d4df`, none is inside any OLD block, and none is claimed clear. Had the
sentence read "the markers **in** the four paragraphs", it would have been false
against those four and would have blocked. It does not.

The rest of the file's self-account was re-tested against the same standard and
each claim is bounded by a check that exists: "Each **OLD** block … returns
**exactly one** match" (verified, below); "No NEW block contains a fenced block"
(verified — no pair's NEW contains a fence, so three backticks is correct and the
four-backtick ruling does not engage); "every NEW block for pairs 1–13 is a
single line" (verified — GDD lines 1466, 1474, 1483, 1537 are each one source
line); "no pair here deletes, edits or weakens it" of the 2026-08-02 ruling
(verified — the ruling sentence appears in no OLD block); "§4.8's bare
`Combat.h` at line 2440" (verified at line 2440, and exempt by ruling).

### Re-derived from scratch, not taken on report

The author reports the diff as confined to the live-marker section plus two
hedging words. That report is not gate-bindable and was not relied on: all
fifteen pairs were re-derived against md5 `6a446c9408cbaf838a57f3326617e4d3`
independently of what did or did not move.

- **All fifteen OLD anchors match `source/gdd.md` exactly once.** Pairs 1–7 on
  line 1466, pair 8 on 1474, pairs 9–11 on 1483, pairs 12–13 on 1537, pairs 14–15
  on 2639–2644. Each was confirmed verbatim against the source line and its
  distinctive span counted document-wide: one occurrence each. Pair 8's row is
  unique against the two other "Capture & Fame economy" strings (lines 1686,
  2661); pair 12's is unique against the §3 cross-reference to *Specification
  outruns the build* on line 1466.
- **No placement collision.** On line 1466 the seven spans occur in pair order
  and are disjoint (1 → 2 → 3 → 4 → 5 → 6 → 7, pair 5 ending where pair 6 begins,
  with no overlap); likewise 9 → 10 → 11 on line 1483 and 12 → 13 on line 1537.
  Pairs 14 and 15 are separated by lines 2641–2642, untouched. Every OLD is an
  exact string, so every placement merges mechanically. The Placement table's
  fifteen rows agree with the pairs.
- **No dead references.** §3 (line 1375), §4.4 (1513), §4.5 (1527), §4.7 (1577),
  §4.8 (2410), §4.9 (2487), §4.10 (2558), §4.11 (2637) all exist; the §4.7
  heading does read "…that read `*pending*` at 2026-08-01", which is what pair 14
  states in the document; Stubs 1 and 3 (lines 1625, 1658) carry no
  built-annotation, which is what the "Not in scope" note claims of Stub 4;
  §4.11's row-5 cell does read "4 + verified Combat/Repair @ 5ffa8d6", which is
  where pair 15 reads row 5's second dependency; `crew/tasks.py` occurs exactly
  once in the document, inside the paragraph pair 10 extends.
- **No curly quotes** anywhere in the file. No fenced block inside a NEW block.
- **Path form.** Every cited path is full, including pair 7's
  `cpp_reference/Economy.h` where Fact F says only `Economy.h`. The single bare
  name is `Combat.h` in the "Not in scope" note, which quotes §4.8's known
  pre-existing defect and is exempt by ruling.
- **Arithmetic.** 69 unchanged; green 27 = 7 + 5 + 6 + 9, split 18 at `c224825`
  and 9 at `647d4df`; unclosed 42 = 69 − 27; "the 41 in rows 5–10" = 50 − 9;
  verified ledger rows 6 → 7 (pair 12) consistent with pair 8's flip and pair 9's
  "Seven rows carry a ✓ … an eighth carries evidence without one"; pair 10's
  "**Data tables** is the eighth row" agrees with both.
- **Entry points.** Pair 3 binds the document's own **seven** to `9f87ecd`, with
  "that commit" taking its antecedent from the untouched driver sentence
  immediately before it. Pair 7's **eight** at `647d4df` matches Fact K
  set-for-set — the seven listed plus `cpp_reference/test_economy.cpp`, six test
  harnesses, one combat duel simulator, one debug REPL — and is stated at Fact
  K's extent, entry points in the tracked tree at that commit. The eighth is the
  file Fact C probes `EXISTS`.
- **Pair 7's substantive claims** each land on a fact: 9/9 under clang++ and
  MSVC and the no-uncovered-ID/Q29 consequence (Fact B), the five cited sources
  (Fact C), week 3 and therefore ahead of the milestone table (Fact D, confirmed
  in the document at line 1519), "owns the economy and not the turn" and the four
  ruled-question invariants (Fact E), the command list, the debug-setter caveat
  and `GATE-DRV-01..07` still 7/7 and still not `T-*` (Fact F), 18 → 27 and 69
  standing (Fact G), and the shortened list of what still cannot be done —
  turn structure, AI, scenario file — against Fact H. The Q4/Q5/Q6/Q8 readings
  quoted there are the register's own text: T-FAME-02 and T-FAME-04 (Q8),
  T-FAME-05 (Q4), T-FAME-07 (Q5, "500, not 650"; Q6, absence). Stub 4 does carry
  nine invariants.
- **The qualification.** Pair 7's OLD is the eight-word tail plus the italic
  close; the ruling sentence is neither quoted, edited nor weakened, and the
  amendment is written as a dated Director judgement rather than a check result.
- **Row 4's attribution** is the Claude Code session, at pair 10, attached to the
  paragraph's existing second authoring sentence, with the `crew/tasks.py` diff
  written at its own extent — "it is not evidence about what any run did".
- **No `kb-desync`.** No pair touches §2, so the §2 parse in `source/kb_rules.md`
  is unaffected; the Fame figures pair 7 names are quoted from the existing §4.7
  register text, unchanged.
- **Format** is the accepted addendum shape — numbered pairs, Placement,
  Grounding, Open questions, Change requests, Handoffs — as ruled clean on the
  previous two runs. Change requests: none, correctly, since no number moves in
  prose that is not already a Director-supplied fact.

---

## Verdict

**PASS.** The file may merge. The `row4-playable-1` `stat-drift` and all three
`row4-playable-2` `contradiction`s are closed, and closed by deletion rather than
by a tighter assertion: the sweep's completeness claims are gone, the two
surviving `still` clauses and the §4.11 "have since flipped" marker each have a
stated disposition, and the only remaining sentence about the table is a caption
scoped to what the author examined, which asserts nothing about markers the table
omits. Nothing in the front matter was taken on trust — all fifteen OLD anchors
were re-matched against md5 `6a446c9408cbaf838a57f3326617e4d3` and each occurs
exactly once, the spans are disjoint and in order, the arithmetic closes at
69/27/42 and 6 → 7, pair 7's eight entry points match Fact K set-for-set, every
path is full, and no NEW block contains a fence. Nothing further is required
before merge; the Director should apply the fifteen pairs at the placements
listed and then rebuild the derived files and re-run `python sync.py` per the
merge checklist.
