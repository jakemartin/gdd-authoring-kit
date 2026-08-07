# Technical design — af-rename-editor-pass addendum (tech-director)

## Placement
§3 (the provenance ledger, lines ~1516–1543) and §4.4, §4.5, §4.6, §4.7, §4.8,
§4.9, §4.11 — everywhere the in-editor Unreal Automation pass/harness is named
in present-tense prose. Executes the rename Ruling AF (2026-08-06, merged as
`tech_harness-calendar.md` Pair 3) deferred to its own round. No invariant
text, acceptance ID, or §4.5 count moves.

## Draft

Exact OLD→NEW replacement pairs against `source/gdd.md` (md5 `8800bd70`).
No section is redrafted; each pair is a substring replacement in place.

Canonical form: **the editor pass**. Where bare substitution doesn't fit the
sentence, the grammatically adjusted compound **editor-pass** (adjective) is
used, keeping the same noun root.

Grep swept for the exhaustive pattern `in-?editor|Automation harness|Automation
pass|editor pass|Unreal Automation` (case-sensitive, whole document,
occurrences counted per line, not matching lines). That grep returns **126
occurrences total** — the full accounting is in the Check results and
Grounding sections below; every one of the 126 is either one of the 55 pairs
below, or is listed by exact line and reason in the exclusion/canonical lists.

Genuinely unrelated uses of "in-editor" are left alone throughout — the
Unreal MCP plugin's scenario/UMG tooling (§3 table, §4.2, §4.11 row 7),
"in-engine" (a build target, not this name), the §4.1 technology-label use
("Unreal Automation tests" naming the test-framework product, not this
denotation), and the incidental "exercised in-editor via the load UI path"
note — are different subjects and are not touched anywhere in this pass.
(An earlier draft of this addendum also excluded the §4.8/§4.9 "tables
imported in-editor" phrasing and the §4.11 "widgets in-editor" build-order
cell as a fourth category, "manual DataTable/widget construction" — that
category is withdrawn in this round: those are the same import/Automation
subject already renamed elsewhere in this file (e.g. Pair 30), and Pairs
53–55 below now cover them.)

---

### §3 — the ledger (lines 1516, 1527, 1531, 1533)

**Pair 1** (row 2, table cell)
OLD: `T-DATA-05 (in-editor) 4/4`
NEW: `T-DATA-05 (in the editor pass) 4/4`

**Pair 2** (row 2, narrative)
OLD: `T-DATA-05, the in-editor Unreal Automation parity pass, has not run`
NEW: `T-DATA-05, the editor-pass parity check, has not run`

**Pair 3** (row 7/8, at `7c36303`)
OLD:
```
**T-UI-03 and T-UI-04 have not run**: they are in-editor Unreal Automation
over widget bindings, marked † in §4.11, and **no in-editor pass exists at
this commit**.
```
NEW:
```
**T-UI-03 and T-UI-04 have not run**: they are editor-pass Automation
over widget bindings, marked † in §4.11, and **no editor pass exists at
this commit**.
```

**Pair 4**
OLD: `what row 8 lacked after this commit was no longer the in-editor pass alone`
NEW: `what row 8 lacked after this commit was no longer the editor pass alone`

**Pair 5** (at `41a1452`, non-protected sentence — see Pair 6/7 below for the
two sentences left untouched)
OLD: `**T-UI-03 and T-UI-04 did not run**, being in-editor Unreal Automation marked † in §4.11, and **no editor pass exists at this commit**.`
NEW: `**T-UI-03 and T-UI-04 did not run**, being editor-pass Automation marked † in §4.11, and **no editor pass exists at this commit**.`

**Left untouched — pinned quote 1, at `b23823f`:**
`T-INT-02`, `T-INT-03` and `T-INT-05` **did not run** — no in-editor
Automation harness exists, and the runner prints that sentence by name
before its tally.
*Why:* this is the record of the runner's own printed output, cited later
in the document by exact commit (§4.9 §3-reference; see below), not present
tense prose naming the thing. Renaming it would misdescribe what the
gate actually printed at that commit.

**Left untouched — pinned quote 2, at `41a1452`:**
Rebuilt from `Ui.good.cpp` at `41a1452`, the two `NOT RUN` lines are output
lines **76** and **82** and the `34/34 passed` tally is line **101**; each
names its ID, states that it is in-editor Unreal Automation marked †, and
states that no in-editor pass exists at this commit.
*Why:* same discipline — this cites exact output line numbers from a real
run; the words after "states that" are the runner's, not the document's.

**Left untouched — the pointer sentence that follows both:**
"The records above of the runner's printed output at `b23823f` and
`41a1452` describe those commits and are unmoved by the repair." Contains
no non-canonical spelling itself; nothing to change.

**Pair 6** (repair record, `c2edae0`)
OLD: `**The in-editor Automation harness then landed**, at `
NEW: `**The editor pass then landed**, at `

**Pair 7** (repair record, built artifacts)
OLD: `and an in-editor Unreal Automation suite`
NEW: `and an editor-pass Automation suite`

**Left untouched — historical description of the pre-repair state:**
"the gate runner, its test harnesses, two specs and the README asserted
that no in-editor Automation harness exists, at thirteen sites in five
spellings, and each site now names what its ID still lacks." Past tense
("asserted") describing text that *used to* say this before `c2edae0`; not
a present-tense naming of the thing today.

**Pair 8** (row 9, "did not run — no in-editor Automation harness exists — so
row 9... does not close", at `d837fc8`)
OLD: `**still did not run** — no in-editor Automation harness exists — so **build-order row 9's acceptance set still does not close**`
NEW: `**still did not run** — no editor pass exists — so **build-order row 9's acceptance set still does not close**`

**Pair 9** (row 10, `T-SAVE-06` blocker)
OLD: `and the in-editor Automation harness `T-SAVE-06` waits on is untouched by it`
NEW: `and the editor pass `T-SAVE-06` waits on is untouched by it`

**Pair 10** (row 10, `T-SAVE-06` did not close — period variant)
OLD: `it is the only † of row 10's seven, it is asserted jointly with `T-INT-02`, and no in-editor Automation harness exists.`
NEW: `it is the only † of row 10's seven, it is asserted jointly with `T-INT-02`, and no editor pass exists.`

**Pair 11** (row 10, "remains the only ID")
OLD: `**T-SAVE-06` remains the only † of row 10's seven, and among what it waits on are the in-editor Automation harness and a vendored replayer`
NEW: `**T-SAVE-06` remains the only † of row 10's seven, and among what it waits on are the editor pass and a vendored replayer`

**Pair 12** (row 8, line 1531, echo of Pair 3/5 without the "marked †" clause)
OLD: `**T-UI-03 and T-UI-04 have not run**: they are in-editor Unreal Automation over widget bindings and no in-editor pass exists at either commit.`
NEW: `**T-UI-03 and T-UI-04 have not run**: they are editor-pass Automation over widget bindings and no editor pass exists at either commit.`

**Pair 13** (line 1533, the "written and not green" clause)
OLD: `written, unblocked and asserting, in-editor Unreal Automation for which no in-editor pass exists at either of row 8's two commits`
NEW: `written, unblocked and asserting, editor-pass Automation for which no editor pass exists at either of row 8's two commits`

**Pair 14** (line 1533, same paragraph)
OLD: `the in-editor Automation harness they also lacked having landed at `fed8ae9``
NEW: `the editor pass they also lacked having landed at `fed8ae9``

**Pair 15** (line 1533, "for want of")
OLD: `for want of an in-editor pass at that commit and at [`7c36303`]`
NEW: `for want of an editor pass at that commit and at [`7c36303`]`

**Pair 37** (line 1516, "No ID is left uncovered" — row referencing row 2)
OLD: `unlike row 2 there is no in-editor half`
NEW: `unlike row 2 there is no editor-pass half`

**Pair 38** (line 1516, row 5's "No ID is left uncovered")
OLD: `row 5 has no in-editor half and no reserved-unwritten ID`
NEW: `row 5 has no editor-pass half and no reserved-unwritten ID`

**Pair 39** (line 1516, row 6's "No ID is left uncovered")
OLD: `row 6 has no in-editor half and no reserved-unwritten ID`
NEW: `row 6 has no editor-pass half and no reserved-unwritten ID`

**Pair 40** (line 1516, the row that "still does not flip")
OLD: `has no in-editor half and no unrun fixture`
NEW: `has no editor-pass half and no unrun fixture`

**Pair 41** (line 1533, "unlike row 2 it has no...")
OLD: `unlike row 2 it has no in-editor half, and unlike row 3 no reserved ID`
NEW: `unlike row 2 it has no editor-pass half, and unlike row 3 no reserved ID`

**Pair 42** (line 1533, row 5's paragraph, "It leaves **no ID uncovered**:")
OLD: `It leaves **no ID uncovered**: no in-editor half and no reserved ID`
NEW: `It leaves **no ID uncovered**: no editor-pass half and no reserved ID`

**Pair 43** (line 1533, row 6's paragraph, "leaves **no ID uncovered** either:")
OLD: `leaves **no ID uncovered** either: no in-editor half and no reserved ID`
NEW: `leaves **no ID uncovered** either: no editor-pass half and no reserved ID`

**Pair 45** (line 1516, row 10 `T-SAVE-06`, at `d837fc8` — the colon-variant
"did not close" sentence, distinct from the period-variant Pair 10 covers;
both occurrences of the non-canonical form inside it renamed together)
OLD: `and no in-editor Automation harness exists; its other blocker — §4.10's canonical state hash having no implementation — is removed here, and among what it still waits on are the in-editor Automation harness and a vendored replayer`
NEW: `and no editor pass exists; its other blocker — §4.10's canonical state hash having no implementation — is removed here, and among what it still waits on are the editor pass and a vendored replayer`

**Pair 46** (line 1516, row 8, at `41a1452`, "twelve `main()` definitions")
OLD: `No in-editor harness is among the twelve \`main()\` definitions above.`
NEW: `No editor pass is among the twelve \`main()\` definitions above.`

**Pair 47** (line 1516, row 10, at `737f666`, "thirteen `main()` definitions")
OLD: `No in-editor harness is among the thirteen \`main()\` definitions above.`
NEW: `No editor pass is among the thirteen \`main()\` definitions above.`

**Pair 48** (line 1516, row 8, at `7c36303`, "the IDs it lacks")
OLD: `and after it the IDs it lacks are the in-editor \`T-UI-03\` and \`T-UI-04\``
NEW: `and after it the IDs it lacks are the editor-pass \`T-UI-03\` and \`T-UI-04\``

**Pair 49** (line 1516, row 10, at `d837fc8`, "neither an in-editor harness")
OLD: `had at that commit neither an in-editor harness nor a built subject`
NEW: `had at that commit neither an editor pass nor a built subject`

**Pair 50** (line 1516, row 2, at `fed8ae9`, the `GATE-DATA-VENDOR` cell)
OLD: `plus \`GATE-DATA-VENDOR\`, 5/5 in-editor** at \`fed8ae9\``
NEW: `plus \`GATE-DATA-VENDOR\`, 5/5 in the editor pass** at \`fed8ae9\``

**Left untouched — the `a13626f` total-launch-failure sentence (line 1516,
a near-twin of the excluded line-2864 sentence):** "at `a13626f` nothing
in-editor could run — not a commandlet, not an Automation test, not the
editor." *Why:* same reasoning as the line-2864 exclusion below — the
subject is that nothing at all could run inside the editor process at that
commit (the module failed to initialize before any commandlet, Automation
test, or the editor itself could start), not a present-tense naming of "the
editor pass." Renaming it would misstate a total launch failure as a naming
of the specific Automation runner. This twin instance was not disclosed in
either of the first two drafts of this addendum; it is disclosed now.

**Left untouched — quoted text from `spec/integration_spec.md` (line
1516):** *"have no subject even in an editor pass"*. *Why:* a direct quote
of another document's words, cited to show what that spec asserted before
this landing made it false — like the two pinned §3 runner-output quotes
above, renaming it would misattribute words to a source that used different
phrasing. (It already reads "editor pass," not one of the six non-canonical
spellings, so no textual change would occur either way; it is excluded on
citation grounds, not because it needs an edit this pass would otherwise
make.)

---

### §4.4 / §4.5 / §4.6

**Pair 16** (wk-3 record, line 1569)
OLD: `The in-editor Automation harness both of them also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3), in no week this table names.`
NEW: `The editor pass both of them also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3), in no week this table names.`

**Pair 17** (line 1577, calendar note)
OLD: `**The in-editor Automation harness landed off this calendar (ruled 2026-08-06).**`
NEW: `**The editor pass landed off this calendar (ruled 2026-08-06).**`

**Pair 51** (line 1577, calendar note, "import step has no cell")
OLD: `An in-editor import step for the §4.8 tables has no cell`
NEW: `An editor-pass import step for the §4.8 tables has no cell`

**Pair 52** (line 1577, calendar note, "so did the in-editor import step")
OLD: `so did the in-editor import step and the \`UENUM\` mirror named above`
NEW: `so did the editor-pass import step and the \`UENUM\` mirror named above`

**Pair 18** (line 1589, "9 IDs remain unclosed")
OLD: `and for which no in-editor pass exists at either of row 8's two commits`
NEW: `and for which no editor pass exists at either of row 8's two commits`

**Pair 19** (line 1589, same passage)
OLD: `the in-editor Automation pass those two also lacked having landed at `fed8ae9` (§3)`
NEW: `the editor pass those two also lacked having landed at `fed8ae9` (§3)`

**Pair 20** (line 1654, §4.7 cut-line paragraph)
OLD: `or its only unique coverage is an in-editor Automation pass`
NEW: `or its only unique coverage is the editor pass`

---

### §4.7 / §4.8 spec stubs

**Pair 21** (Stub 8 Acceptance line, line 2541)
OLD: `builder are headless functions); T-UI-03..04 in-editor Automation;`
NEW: `builder are headless functions); T-UI-03..04 in the editor pass;`

**Pair 22** (§4.8 DataTable spec, line 2763 — the sixth, previously untracked form)
OLD: `T-DATA-05  (editor, Unreal Automation) every imported DataTable row equals the`
NEW: `T-DATA-05  (the editor pass) every imported DataTable row equals the`

**Pair 44** (§4.8 DataTable spec prose, lines 2693–2694 — the same sixth form
as Pair 22/27, but with the ID placed inside the parenthetical rather than
outside it, which is why the first sweep's grep for the outside-ID pattern
missed it)
OLD:
```
A parity gate (T-DATA-05, Unreal Automation) iterates every
imported row and asserts it equals the CSV field-for-field.
```
NEW:
```
A parity gate (T-DATA-05, the editor pass) iterates every
imported row and asserts it equals the CSV field-for-field.
```

---

### §4.9

**Pair 23** (parity-gates paragraph, lines 2917–2918)
OLD: `the same recorded match is replayed by the headless harness and by an in-editor Automation test through the UBT-compiled module, and both must land on the same canonical state hash.`
NEW: `the same recorded match is replayed by the headless harness and by the editor pass through the UBT-compiled module, and both must land on the same canonical state hash.`

**Pair 24** (part-2 blocker paragraph, line 2926)
OLD: `The **in-editor Automation harness** it waited on landed at `fed8ae9` in the Stratocracy UE project repo (§3)`
NEW: `**The editor pass** it waited on landed at `fed8ae9` in the Stratocracy UE project repo (§3)`

**Pair 25** (the defining sentence itself, lines 2935–2937 — see Open questions)
OLD:
```
**What "the editor pass" denotes, stated once here and cited
elsewhere (ruled 2026-08-05): the in-editor Automation harness this paragraph
names. It is a runner and nothing more, and running it supplies none of the
subjects the IDs scheduled into it assert against — those are separate
requirements.**
```
NEW:
```
**What "the editor pass" denotes, stated once here and cited elsewhere
(ruled 2026-08-05): the specific run this paragraph names — introduced above
as the editor pass that part 2 waited on. It is a runner and nothing more,
and running it supplies none of the subjects the IDs scheduled into it
assert against — those are separate requirements.**
```

**Pair 53** (Integration-parity spec stub, `Inputs` line, line 2956)
OLD: `a §4.10 replay file and the §4.8 tables imported in-editor —`
NEW: `a §4.10 replay file and the §4.8 tables imported in the editor pass —`

**Left untouched — Ruling AF's own naming-variance paragraph (lines
~2969–2977, up to "does not turn on which form a section reaches for"):**
the sentence enumerating *the editor pass*, *an in-editor Automation pass*
and *an in-editor pass* as example spellings, and the clauses citing the
two pinned commits, are self-referential — they exist specifically to
display the variance and to point at the two records above by the same
words those records use. Renaming the examples would make the sentence
assert that a document uses three identical spellings for something, which
is false and defeats its purpose; renaming the two commit-citation clauses
would make this paragraph describe the `b23823f`/`41a1452` records in words
those records themselves (left untouched, per Pair-6/7's rationale above)
no longer use. Both stay as written.

**Pair 26** (the same paragraph's now-stale closing, immediately after)
OLD:
```
The denotation is settled by the ruling above and does not turn on which form
a section reaches for. A rename would have to reconcile with those
commit-pinned §3 records and is deferred to its own round. **No name is
changed in this revision.**
```
NEW:
```
The denotation is settled by the ruling above and does not turn on which form
a section reaches for. **The deferred rename landed in this round (ruled
2026-08-07):** every present-tense denotational use elsewhere in this
document now reads *the editor pass*, or a grammatically adjusted form of
it, reconciling with those commit-pinned §3 records and with this
paragraph's own citation of them, immediately above — by leaving both
untouched.
```

**Pair 27** (Integration-parity spec stub, line 3018 — the same untracked
sixth form as Pair 22/44)
OLD: `T-INT-05  (editor, Automation) presentation statelessness: after any event`
NEW: `T-INT-05  (the editor pass) presentation statelessness: after any event`

**Pair 54** (same stub, restated `Inputs` line, line 2985)
OLD: `file; the §4.8 tables imported in-editor — among this stub's`
NEW: `file; the §4.8 tables imported in the editor pass — among this stub's`

---

### §4.11

**Pair 28** (row 8 landed, line 3167)
OLD: `T-UI-03 and T-UI-04 are the in-editor half and no in-editor pass exists at that commit,`
NEW: `T-UI-03 and T-UI-04 are the editor-pass half and no editor pass exists at that commit,`

**Pair 29** (row 8, line 3173)
OLD: `the in-editor Automation pass those two also lacked landed at `fed8ae9` (§3)`
NEW: `the editor pass those two also lacked landed at `fed8ae9` (§3)`

**Pair 30** (build-order table, row 2 cell)
OLD: `Loader + T-DATA-06 yes; import parity in-editor`
NEW: `Loader + T-DATA-06 yes; import parity in the editor pass`

**Pair 55** (build-order table, row 8 cell, line 3216)
OLD: `Contract + queries yes; widgets in-editor`
NEW: `Contract + queries yes; widgets in the editor pass`

**Pair 31** (build-order table, row 9 cell)
OLD: `Source/compile gates yes; replay parity + statelessness in-editor`
NEW: `Source/compile gates yes; replay parity + statelessness in the editor pass`

**Pair 32** (build-order table, row 10 cell, first clause)
OLD: `T-SAVE-06` waits on the in-editor Automation harness and `T-SAVE-07` on a self-play log written in this format`
NEW: `T-SAVE-06` waits on the editor pass and `T-SAVE-07` on a self-play log written in this format`

**Pair 33** (build-order table, row 10 cell, second clause)
OLD: `The in-editor Automation harness this ID also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3).`
NEW: `The editor pass this ID also lacked landed at `fed8ae9` in the Stratocracy UE project repo (§3).`

**Pair 34** (†-cut-line list, `T-DATA-05` bullet, line 3225)
OLD: `**T-DATA-05** — row 2's only in-editor half, and **closed**, 4/4 at `fed8ae9``
NEW: `**T-DATA-05** — row 2's only editor-pass half, and **closed**, 4/4 at `fed8ae9``

**Pair 35** (†-cut-line list, `T-UI-03, 04` bullet)
OLD: `- **T-UI-03, 04** — in-editor Automation over widget bindings, where a Director`
NEW: `- **T-UI-03, 04** — editor-pass Automation over widget bindings, where a Director`

**Pair 36** (†-cut-line list, `T-INT-02, 05 and T-SAVE-06` bullet, line 3251)
OLD: `- **T-INT-02, 05 and T-SAVE-06** — the in-editor half of the parity pair`
NEW: `- **T-INT-02, 05 and T-SAVE-06** — the editor-pass half of the parity pair`

**Left untouched — two "exercised/asserted...via the load UI path" clauses**
(§4.10 Acceptance line and §4.11's `T-SAVE-05` note): "T-SAVE-05 is *also*
exercised in-editor via the load UI path" and "05 also exercised in-editor
via the load UI path" describe an incidental, additional manual exercise of
an already-headless-green ID, not the gated Automation run. Different
subject from the editor pass; not touched.

## Check results

**Sweep terms used, this (third) draft.** Per the gate's instruction, the
full document was re-swept from scratch against the single exhaustive
pattern `in-?editor|Automation harness|Automation pass|editor pass|Unreal
Automation` (case-sensitive), counting **occurrences, not matching lines** —
several lines carry many hits each, above all source line 1516 (a single
markdown paragraph spanning the whole of §3's row-history prose), which
alone carries 47 of the document's 126 total occurrences.

**The closing equation.**

```
67  (occurrences covered by Pairs 1–44, the first two drafts' work)
+ 14  (occurrences covered by new Pairs 45–55, added this draft)
+ 27  (occurrences explicitly excluded: different subject, a quote, or
       historical past tense — enumerated by line in Grounding)
+ 18  (occurrences already reading the canonical "the editor pass" /
       "an editor pass" and needing no pair)
= 126  (N, the full-document occurrence count of the exhaustive pattern)
```

67 + 14 + 27 + 18 = 126. This matches the independently re-counted N, so
nothing is missing from this accounting by construction — every occurrence
the pattern finds has a stated disposition (pair number, or a named
exclusion/canonical reason) in the Grounding table below.

**Corrections from the two prior gate runs, both now closed:**

1. **First gate run (af-rename-editor-pass):** found a sixth,
   previously-untracked non-canonical spelling — the bare parenthetical
   `(editor, Unreal Automation)` / `(T-DATA-05, Unreal Automation)` — with a
   third occurrence at line 2693 in the reversed (ID-inside) word order my
   original grep didn't also search for, plus seven missed instances of
   "in-editor half" at lines 1516/1533. Closed by Pairs 37–44.
2. **Second gate run (af-rename-editor-pass-2):** found 10 more instances
   at lines 1516 and 1577 that my re-sweep, anchored around the
   already-cited violations rather than re-derived from a full occurrence
   count, missed. Closed by new Pairs 45–52 above (two of the ten, at line
   1516, share one sentence and are closed together by Pair 45). One of the
   ten — "at `a13626f` nothing in-editor could run" — is judged a different
   subject on the same reasoning as the line-2864 exclusion, and is
   disclosed as an exclusion rather than renamed (see the "Left untouched"
   note in the §3 section above).

**A third defect found by this round's own from-scratch re-derivation, not
cited by either gate run:** two occurrences of "the §4.8 tables imported
in-editor" (lines 2956 and 2985) and one occurrence of "widgets in-editor"
(line 3216, the UI-binding build-order cell) were excluded by the first two
drafts as "manual DataTable/widget construction," a fourth category distinct
from the editor pass. That category does not survive scrutiny once the
gate's own line-1577 citations (#9, #10 in its violation list) named the
identical "import step ... in-editor" construction as a violation requiring
rename. Consistent treatment closes all three via new Pairs 53–55, and the
withdrawn category is removed from the Draft's opening paragraph and from
the excluded-sites list below.

**Root cause, stated for the record.** Both prior drafts patched exactly
what the cited violations named and re-swept only the text around those
citations. This draft instead re-derived the full 126-occurrence list from
the raw pattern match before writing anything, which is what surfaced the
withdrawn fourth exclusion category above — a defect neither gate run had
cited, because it was a false exclusion rather than a missed occurrence.

## Change requests

None. This is a rename with no rule, invariant, or count effect; nothing is
proposed to source content beyond the pairs above, which are themselves the
change.

## Open questions for the Director

1. **Pair 25 (the defining sentence) departs from bare synonym substitution.**
   Renaming *only* "the in-editor Automation harness this paragraph names" to
   "the editor pass this paragraph names" would make the sentence circular —
   "What 'the editor pass' denotes ...: the editor pass this paragraph
   names" — since Pair 24 (the sentence just before it) already renames the
   thing being pointed at. I resolved this by writing "the specific run this
   paragraph names — introduced above as the editor pass that part 2 waited
   on," which keeps the defining function intact but is not a pure
   word-for-word swap. If you want the literal repetition instead (accepting
   the circularity as harmless, since the antecedent is one sentence away),
   say so and I'll redo Pair 25 as a straight substitution.
2. **Whether AF's own naming-variance paragraph should itself be updated
   beyond its closing two sentences (Pair 26).** I left its illustrative list
   of three spellings and its two commit-citation clauses untouched, on the
   reasoning that they exist to *display* variance and to match the two
   pinned records' exact words. An alternative reading: since this round
   *is* "its own round" the paragraph deferred to, the whole paragraph could
   be replaced by a shorter pointer to this addendum instead of being partly
   kept, partly patched. I chose the smaller edit; flagging the larger one as
   an option.
3. **No rule gap.** This round changes no invariant, mints no ID, and rules
   on no open Q — it is the text-only rename the brief specified. I found no
   rule gap while doing it.

## Handoffs

None. This is a self-contained rename inside §3/§4; no other author's
section is touched.

## Grounding

- **The exhaustive count.** `rg -o` for the pattern
  `in-?editor|Automation harness|Automation pass|editor pass|Unreal
  Automation` against `source/gdd.md` (md5 `8800bd70`), case-sensitive,
  counted per occurrence rather than per matching line, returns **126**
  total hits, distributed across 47 distinct lines. The full per-line
  occurrence count and disposition:
  - Lines 474, 497, 1435, 1455 — 1 occurrence each (4 total) — **excluded**,
    MCP plugin's map-gen/scenario/UMG tooling wrapper and role-table/
    guardrail prose; a different subject throughout.
  - Line 1516 — **47 occurrences**: 24 covered by Pairs 2, 3 (×3), 4, 5 (×2),
    6 (×2), 7 (×2), 8 (×2), 9 (×2), 10 (×2), 11 (×2); 5 already canonical
    ("the editor pass" / "an editor pass," no pair needed); 5 excluded as
    the two pinned runner-output quotes (2 + 3 occurrences — see the §3
    "Left untouched" notes above); 2 excluded as the historical
    past-tense "asserted" sentence; 1 excluded as the quoted
    `spec/integration_spec.md` text; 1 excluded as the `a13626f`
    total-launch-failure sentence (twin of line 2864, newly disclosed this
    round); 9 covered by new Pairs 45 (×4, one sentence), 46, 47, 48, 49, 50.
    24 + 5 + 2 + 3 + 2 + 1 + 1 + 9 = 47.
  - Line 1527 — 1 occurrence — Pair 1.
  - Line 1531 — 3 occurrences — Pair 12.
  - Line 1533 — 11 occurrences: 9 covered by Pairs 13 (×3), 14 (×2), 15,
    41, 42, 43; 2 already canonical. 9 + 2 = 11.
  - Line 1550 — 1 occurrence — **excluded**, §4.1's "Unreal Automation
    tests" names the test-framework product as a build-tooling label, not
    this denotation.
  - Line 1557 — 1 occurrence — **excluded**, MCP/manual scenario building
    ("the Content agent builds/edits scenarios in-editor").
  - Line 1569 — 2 occurrences — Pair 16.
  - Line 1577 — 4 occurrences: 2 covered by Pair 17; 2 covered by new
    Pairs 51, 52.
  - Line 1589 — 5 occurrences: 2 already canonical; 3 covered by Pairs 18,
    19 (×2).
  - Line 1654 — 2 occurrences — Pair 20.
  - Line 2375 — 1 occurrence — **excluded**, the `validate_scenario` MCP
    tool.
  - Line 2541 — 1 occurrence — Pair 21.
  - Line 2693 — 1 occurrence — Pair 44.
  - Line 2763 — 1 occurrence — Pair 22.
  - Line 2769 — 1 occurrence — already canonical.
  - Line 2864 — 1 occurrence — **excluded**, the editor's total launch
    failure at `a13626f`, unrelated to any pass.
  - Line 2917 — 1 occurrence — Pair 23.
  - Line 2926 — 2 occurrences — Pair 24.
  - Line 2935 — 1 occurrence — already canonical (inside Pair 25's OLD/NEW,
    unmoved by it).
  - Line 2936 — 2 occurrences — Pair 25.
  - Line 2956 — 1 occurrence — new Pair 53 (withdrawn exclusion — see Check
    results).
  - Line 2972 — 4 occurrences — **excluded**, Ruling AF's own
    naming-variance illustrative list (self-referential, displays variance
    by design).
  - Lines 2974, 2975, 2976 — 1 occurrence each (3 total) — **excluded**,
    AF's paragraph citing the two pinned §3 commit records by their own
    words.
  - Line 2985 — 1 occurrence — new Pair 54 (withdrawn exclusion).
  - Line 3030 — 1 occurrence — already canonical.
  - Line 3146 — 1 occurrence — **excluded**, "exercised in-editor via the
    load UI path."
  - Line 3147 — 1 occurrence — already canonical.
  - Line 3167 — 2 occurrences — Pair 28.
  - Line 3173 — 2 occurrences — Pair 29.
  - Line 3195 — 1 occurrence — already canonical.
  - Line 3210 — 1 occurrence — Pair 30.
  - Line 3215 — 1 occurrence — **excluded**, MCP tool wrapping the
    scenario validator.
  - Line 3216 — 1 occurrence — new Pair 55 (withdrawn exclusion).
  - Line 3217 — 1 occurrence — Pair 31.
  - Line 3218 — 5 occurrences: 4 covered by Pairs 32, 33 (×2 each); 1
    already canonical.
  - Line 3225 — 1 occurrence — Pair 34.
  - Line 3245 — 1 occurrence — Pair 35.
  - Line 3251 — 1 occurrence — Pair 36.
  - Lines 3258, 3261, 3266 — 1 occurrence each (3 total) — already
    canonical ("the editor pass" in generic/hypothetical use, e.g. "an
    editor pass cut to its marked IDs alone").
  - Line 3259 — 1 occurrence — **excluded**, "exercised in-editor via the
    load UI path" (the `T-SAVE-05` note).
  - Totals by disposition: 67 pair-covered (Pairs 1–44) + 14 pair-covered
    (new Pairs 45–55) + 27 excluded + 18 already-canonical = **126**.
- Seven additional instances of the fifth-listed construction ("in-editor
  half"), confirmed by direct grep against `source/gdd.md` at the exact
  quoted text: line 1516 — "unlike row 2 there is no in-editor half" (Pair
  37), "row 5 has no in-editor half and no reserved-unwritten ID" (Pair 38),
  "row 6 has no in-editor half and no reserved-unwritten ID" (Pair 39), "has
  no in-editor half and no unrun fixture" (Pair 40); line 1533 — "unlike row
  2 it has no in-editor half, and unlike row 3 no reserved ID" (Pair 41),
  "It leaves **no ID uncovered**: no in-editor half and no reserved ID"
  (Pair 42, row 5's paragraph), "leaves **no ID uncovered** either: no
  in-editor half and no reserved ID" (Pair 43, row 6's paragraph).
- Line 2693–2694 (Pair 44), confirmed by direct read of `source/gdd.md`:
  "A parity gate (T-DATA-05, Unreal Automation) iterates every\nimported row
  and asserts it equals the CSV field-for-field." — the sentence spans a
  hard line break in the source file between "every" and "imported"; the OLD
  block reproduces that break verbatim.
- The 10 instances cited by the second gate run, confirmed by direct grep
  against `source/gdd.md`, each returning exactly one match: "No in-editor
  harness is among the twelve `main()` definitions above." (Pair 46); "No
  in-editor harness is among the thirteen `main()` definitions above."
  (Pair 47); "and after it the IDs it lacks are the in-editor `T-UI-03` and
  `T-UI-04`" (Pair 48); "had at that commit neither an in-editor harness nor
  a built subject" (Pair 49); "and no in-editor Automation harness exists;
  its other blocker" and "among what it still waits on are the in-editor
  Automation harness and a vendored replayer" (one continuous sentence,
  Pair 45); "plus `GATE-DATA-VENDOR`, 5/5 in-editor** at `fed8ae9`" (Pair
  50); "An in-editor import step for the §4.8 tables has no cell" (Pair 51);
  "so did the in-editor import step and the `UENUM` mirror named above"
  (Pair 52); "at `a13626f` nothing in-editor could run — not a commandlet,
  not an Automation t[est], not the editor" — judged excluded, not renamed
  (near-twin of the line-2864 exclusion, both describing total editor
  launch failure; see the §3 "Left untouched" note).
- The two withdrawn-exclusion instances found by this round's own
  from-scratch recount, confirmed by direct grep, each returning exactly one
  match: "a §4.10 replay file and the §4.8 tables imported in-editor —"
  (line 2956, Pair 53); "file; the §4.8 tables imported in-editor — among
  this stub's" (line 2985, Pair 54); "Contract + queries yes; widgets
  in-editor" (line 3216, Pair 55).
- Two pinned quote sites, both in §3 (source line 1516): the `b23823f`
  sentence ("no in-editor Automation harness exists, and the runner prints
  that sentence by name before its tally") and the `41a1452` sentence ("the
  two `NOT RUN` lines are output lines 76 and 82 ... states that no
  in-editor pass exists at this commit"), each confirmed by the pointer
  sentence immediately following them in the same paragraph: "The records
  above of the runner's printed output at `b23823f` and `41a1452` describe
  those commits and are unmoved by the repair."
- Ruling AF's own naming-variance paragraph and its grounding for the two
  pinned commits — `sections/tech_harness-calendar.md`, Pair 3 and its
  Grounding line: "Pair 3 anchor — §4.9 ... The printed-output records — §3,
  at `b23823f` and at `41a1452`." Confirms those two records live in §3
  (source line 1516), not in AF's §4.9 paragraph, which only cites them.
- Section boundaries used to place each pair — `## 3.` at line 1425, `## 4.`
  at 1544, `### 4.4` 1563, `### 4.5` 1579, `### 4.7` 1629, `### 4.8` 2669,
  `### 4.9` 2772, `### 4.10` 3033, `### 4.11` 3150 (headers grepped directly
  from `source/gdd.md`); line 2693 falls inside `### 4.8` (2669–2772); lines
  2956 and 2985 fall inside `### 4.9` (2772–3033); line 3216 falls inside
  `### 4.11` (3150–end).
- `source/gdd.md` md5 confirmed `8800bd70` via `source/MANIFEST.txt` before
  drafting, and reconfirmed unchanged before drafting Pairs 45–55.
