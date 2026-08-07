# Gate report — run `rulings-ao-ap-5`

Snapshot: `source/MANIFEST.txt` present; `gdd.md` md5
`18555ea139cc70d8026957c4b3b5ef14`, matching the md5 the draft's Placement and
Grounding declare.

Sections gated: `sections/tech_rulings-ao-ap.md` — sole section this stage.

## sections/tech_rulings-ao-ap.md — PASS

Zero violations.

The file was gated as new text throughout. No prior revision was consulted, and
no identity claim from the run brief was accepted; pairs 1 and 3, the four
Check-results bullets, Change requests, the open question and all nine Grounding
bullets were re-derived against `source/gdd.md` from scratch rather than carried
forward from run 4.

### What was checked and what it resolved to

**Run 4's violation is cleared, and the repair leaves nothing dangling.** The
string `against that commit` occurs nowhere in the draft. The merged pair 2
shared sense reads *"Vendored means the same thing in each: bytes copied out of a
named commit's object store into the UE project, and gated for identity."* Both
halves hold of both mechanisms against source: §4.8 states *"the UE project
vendors it verbatim beside a manifest recording each file's sha256 and the crew
commit it came from"* and *"The manifest's `dataCommit` names the commit the
vendored bytes came from"*, so the CSV bytes do come from a named commit; and
§4.8's *"`GATE-DATA-VENDOR` asserts that the vendored bytes are the recorded
ones"* is identity gating. The sentence no longer says what each is gated
against, and no later clause in pair 2, pair 1, pair 3, the Change requests, the
open question or the Grounding leans on the deleted words.

**Pairs anchor and are unique.** Each OLD returns exactly one match in the master
— pair 1 at §4.7 Q34 (line 2661), pair 2 at §4.9 part 1 (line 2791), pair 3 at
§4.8's principle paragraph (line 2669). Pairs 2 and 3 reproduce their OLD
verbatim at the head of their NEW; pair 1 replaces its OLD and keeps verbatim the
half the ruling rests on (*"the pinned record is untouched either way, since
green at `b1ea992` over the UE tree at `fed8ae9` stays true of those commits,
which is what pinning is for"*). `interval` occurs once in the master, wholly
inside pair 1's OLD, and pair 1's NEW names the span in full at first use.

**Ruling AO is grounded on the master's own rule, not a new one.** §3 states
*"each Verified row citing the commit and passing test IDs that back it"*; §3's
row 2 cell cites `b1ea992` and *"T-DATA-05 (in-editor) 4/4 ... @ `fed8ae9`"*. The
loud-failure claim matches §3's known-bad record — *"a perturbed CSV value
(parity and vendor both)"* — and Q34's own *"failed both the parity check, on
`Infantry.HP` expected 11 and read 10, and `GATE-DATA-VENDOR`, on a sha256
mismatch"*. AO does not conflict with Q34's surviving *"such an edit re-opens the
whole pair"*: re-opening governs the new pair, the ✓ cites the old one.

**Ruling AP's placement and scope hold.** Pair 2 sits immediately after §4.9's
*"Nothing else is vendored — a UBT module cannot hold a second `main()` ... the
`*.buggy.cpp` files are pass-1 fixtures, not shippable code."* and immediately
before *"The set is declared, not inferred (ruled 2026-08-05)."* The reason pair
2 attributes to that sentence is that sentence's own stated reason. Nothing
downstream in §4.9 that points backward (*"the different reason stated above"*,
*"The enumeration above is correct as it stands"*) is displaced by the insertion.

**Every dependant-sweep site the draft names exists and reads as claimed.** The
other `re-open` occurrences are §4.4's wk-2 cell (line 1566), §4.11's rows 9–10
cell (line 3195) and §3's *"re-opened by each system that lands after it"* (line
1514) — all a different event. Every `vendored`/`unvendored` site named for AP
resolves to crew C++ modules or `Source/StratRules/`: §4.9's ten-module
enumeration plus `StratRules.Build.cs` and `StratRules.manifest.json`, the
declared-not-inferred partition, *"`Save`, `Replay` and `Balance` remain
unvendored"*, *"ruled out of vendoring until a bridge consumer exists"*, the
*"vendored replayer"* sites in §4.4/§4.11/§3, and `T-INT-01`'s *"every file in
Source/StratRules/"*.

**"No count moves" re-derived, not accepted.** §4.7: *"Seventeen of the
thirty-four rows are ruled; the other seventeen remain open"* — the open list
(Q1, Q2, Q3, Q10–Q19, Q29, Q30, Q31, Q32) counts 17, Q34 is already ruled, and
neither pair adds a register row, so 34 / 17 / 17 stands. §4.5: line 1587 gives
71 written and *"**62** of the 71 are green"*, so 71 / 62 / 9 stands; neither
ruling mints an acceptance ID. §3: *"Ten rows carry a ✓ in the table above, and
two more carry evidence without one"* and *"Seven IDs are still recorded as
uncovered"* — AO keeps row 2's ✓, so ten / two / seven stands. No arithmetic
section is required.

**Apparatus gated at the same standard as the pairs.** The four Check-results
bullets are each true against the master as re-derived above. The Change requests
section closes the two the merged addendum filed without adding a pair: §4.9's
*"Nothing else is vendored"* is left untouched, and §4.9's stub `Inputs` line —
*"a §4.10 replay file and the §4.8 tables imported in-editor"* — is left
untouched and gains no note in the master. The open question quotes `T-INT-01`'s
invariant text, §4.9's *"so neither takes its expectation from the other"*, and
§4.8's *"the UE project cannot see the crew repo at test time"* verbatim; its
reading of *"Neither mechanism"* is fixed by the invariant's own preceding
sentence, as claimed; `GATE-DATA-VENDOR` indeed carries no invariant text, and
the six `T-DATA` invariants are as characterised. Its three answers are proposals
to the Director, not assertions, and it states no measurement it did not take.
All nine Grounding bullets resolve — including the precedent bullet, whose quoted
phrase is §4.9's *"What 'the editor pass' denotes, stated once here and cited
elsewhere"* (line 2913), and the deferred-rename bullet, whose basis is §4.9's
*"A rename would have to reconcile with those commit-pinned §3 records and is
deferred to its own round."* The one claim measured outside this document —
that the script, its manifest note and its crew commit message all say *vendor* —
is labelled as supplied by the round's fact block and pinned to crew `c2edae0`.

## Verdict

`sections/tech_rulings-ao-ap.md` passes with zero violations, and the run's
top-level verdict is **PASS**. Three pairs, numbered 1–3, anchor uniquely against
`gdd.md` at `18555ea1`; no count in §3, §4.5 or §4.7 moves; no acceptance ID is
minted and no register row is added. The file is clear to merge at the placements
it states — pair 1 into §4.7's Q34 answer cell, pair 2 into §4.9 part 1
immediately after *"fixtures, not shippable code."*, pair 3 into §4.8's principle
paragraph — with no other edit to the master. What must happen before merge is
only the standing merge checklist: apply the three pairs at their anchors,
rebuild `.pdf` and `.txt`, re-sync `kb/rules.md`, and re-run `python sync.py` so
the kit sees the new master. One item is for the Director rather than the gate:
the open question on a source-identity invariant for the CSV mechanism is live
and unanswered, and answer (ii) would mint an acceptance ID and move §4.5's
written count, so it must not be actioned as part of this merge.
