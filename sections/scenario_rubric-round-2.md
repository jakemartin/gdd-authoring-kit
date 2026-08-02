# Scenario & map design — rubric-round-2 addendum (scenario-designer)

> ✅ **APPLIED ADDENDUM — DO NOT RE-APPLY.**
> All replacement pairs in this file were applied verbatim to the master GDD
> and merged. Re-applying them would fail (the OLD anchors no longer match) or,
> worse, double-apply an insertion. Gate record: run `rubric-round-2d`, PASS,
> zero violations. Later changes to these sections need a NEW addendum file.

## Placement

This is an **addendum to merged §2.13**, not a redraft. It files **three**
replacement pairs, all inside §2.13: against the closing paragraph of **§2.13.7
Scenario-set summary**, against **§2.13.4**'s configuration-ladder row 9–10, and
against **§2.13.6**'s header. Nothing else in §2.13 is touched. §2.10 belongs to
`rules-designer` this round and carries **no pair from me**.

---

## The decision

The brief offered two models. I took the first: **§2.13.7 is the authority on
the stretch condition; every other site carries labels only.**

§2.13.7's cut line is good and the rubric is right to credit it, but it was not
yet *pointable* — for two reasons, both checkable in `source/gdd.md`:

1. **It never claims exclusivity.** It states the condition; it does not say it
   is the only statement of it. §4.11's row-10 paragraph is the working
   counter-example in this document — it ends *"this paragraph deliberately does
   not restate the week numbers a second time"*, and that sentence is what
   stopped the §4.4/§4.11 pair drifting a fourth time. §2.13.7 has the condition
   but not that sentence.
2. **It was incomplete, so a pointer to it would lose a condition.** The set
   carries **four** conditions, not three. §2.13.7's cut line stated three
   (not before week 4 · does not block core · balance eats week 4 → stays on
   paper). The fourth — ***The Causeway* only after *Longwater March*** — lived
   only in §2.13.6's header (`(P2, wk 4, only after P1)`) and §2.13.4's ladder
   row (`Stretch P2 (wk 4, only after P1)`). §2.13.7's own summary-table Status
   cell reads plain `Stretch P2 (wk 4)` and dropped it. A §2.10 row that deferred
   to §2.13.7 as it stood would have deferred to a condition set missing its
   ordering clause.

**Pair 1 alone did not finish the job, and the gate was right to say so.**
Moving the ordering clause *into* §2.13.7 and declaring §2.13.7 its only site is
a contradiction for as long as two other sites still state it. Exclusivity is
not a claim you can make unilaterally; it has to be made true by clearing the
other sites. Pairs 2 and 3 do that. They strip `, only after P1` from §2.13.4's
ladder row and §2.13.6's header and **keep the identifying labels** — `Stretch
P2 (wk 4)` and `(P2, wk 4)` — which is exactly the labels-here / condition-there
split Pair 1's own sentence describes. Nothing is deleted from the document:
the ordering clause is not lost, it is relocated to the one paragraph that owns
it, in the same round, by the same author.

So this is not a no-op, and it is not a one-pair round. The ordering clause
folded into §2.13.7 is copied verbatim in substance from §2.13.6's header and
§2.13.4's table — no new figure, no new week, no new priority. After the three
pairs, `only after P1` appears **once** in the document, in §2.13.7.

---

## Heading-collision check (Caution 1) — clear, and re-run from scratch

Pair 3 edits a `####` heading, so before filing it I checked whether anything
cross-references that heading **by its text**. Nothing does. **This table is a
re-run**: the version filed last round reported seven citation sites and placed
six of them in sections that cite §2.13.6 zero times. Every line number, count
and section attribution below was re-derived against `source/gdd.md` this round.

| Check | Result |
|---|---|
| Markdown anchor links (`](#…`) anywhere in `source/gdd.md` | **0 matches.** The document contains no intra-doc links at all, so there is no `#2136-stretch-scenario-the-causeway-p2-wk-4-only-after-p1` slug to dangle. |
| Table of contents | **None** — and this is now checked in a form that could fail. The string `Stretch scenario` occurs on exactly **two** lines in the whole document, **1124 and 1203**, which are §2.13.5's and §2.13.6's headings themselves. A TOC, index or cross-reference reproducing §2.13.6's title would have shown up here as a third line. It did not. |
| Occurrences of `2.13.6` | **12 occurrences on 11 lines.** One of them is the heading being edited (line 1203), so there are **11 citations, spread over 10 lines** — line 2288 cites §2.13.6 twice. |
| Where those 11 citations live | **§2.13.2 — 1:** line 1073, the "If one side holds both bridges" paragraph of *Ferrum Crossing*, in the bare no-§ form `*The Causeway* (2.13.6)`. **§4.7 — 10:** lines 1854 (T-SCN-08 fixture (a)), 1892 (T-SCN-09), 2000 and 2058 (T-SCN-06/T-SCN-11 Bridge-allowance argument), 2148 (T-SCN-11 fixture (c)) — all Stub 7 invariant and fixture text — plus §4.7's open-questions register at lines 2288 (**Q17, twice**), 2292 (**Q21**), 2295 (**Q24**) and 2296 (**Q25**). |
| Sections that cite §2.13.6 **zero** times | **§2.8** and **§4.11**. Both were named as citing sites in my round-1 filing; neither contains the string. §4.11 (lines 2526–2578) contains no occurrence of `2.13` at all. **Q16 does not cite it either** — its Blocks cell reads *"All three §2.13 maps; the terrain schema"*. |
| Does any citation reproduce the **heading** string? | **No — zero of 11.** Every one is `§2.13.6`, `(§2.13.6)` or `(2.13.6)`. None carries the map name *as heading text*, the `Stretch scenario` prefix, or the `only after P1` clause Pair 3 removes. |
| Does any citation quote §2.13.6's **body**? | **Yes — two, and this is the row the sweep exists for.** Line **1892** (T-SCN-09: *"which is what §2.13.5 and §2.13.6 mean by 'East is the exact ρ-image of West'"*) and register row **Q25** (*"§2.13.6 'East is the exact ρ-image of West'"*) both quote a sentence that sits at **line 1250, inside §2.13.6's body**. Pair 3 replaces **line 1203 only**. Line 1250 does not move, so both quotes survive verbatim. |
| Sites carrying `only after P1` | **Exactly 2**, lines **1115** (§2.13.4 ladder row 9–10) and **1203** (§2.13.6 heading) — the two Pairs 2 and 3 clear. No citation of §2.13.6 anywhere repeats the clause, so removing it strands nothing. |

So Pair 3 moves the heading text and nothing else needs to move with it. Had a
TOC, an anchor, or a citation quoting the heading existed, I would have reported
the collision instead of filing the pair.

**Why the table is longer than it was.** The round-1 version asked only "are
these citations bare?" over a list of sites it had misattributed — which is a
check that would have returned "all bare, nothing dangles" whether or not
anything quoted §2.13.6's prose, because it never looked at the rows where a
quote would be. Two citations **do** quote §2.13.6's prose. The conclusion is
unchanged, because both quote the body rather than the heading and Pair 3 edits
the heading — but that is now a finding rather than a gap the check could not
see. A check has to be able to fail. The round-2 version then made the
mirror-image error one row down: it volunteered what §4.11 *does* cite alongside
what it does not, and the volunteered half was false while the finding it
decorated was sound. A "does not cite" result gains nothing from naming what a
section cites instead, so that clause is **deleted rather than repaired**, and
the positive claims left elsewhere in this file carry the line numbers they were
verified at.

---

## Replacement pairs

### Pair 1 — §2.13.7, closing paragraph (the cut line)

Verified: this OLD block occurs **exactly once** in `source/gdd.md`
(one match, §2.13.7, immediately after the three-row scenario-set table).

**OLD**
```
Neither stretch map may pull work forward of week 4 or block core; if week 4
is consumed by balance (its primary §4.4 purpose), the set stays on paper.
```

**NEW**
```
**The stretch condition — stated here, once.** Neither stretch map may pull
work forward of week 4 or block core; *The Causeway* is attempted only after
*Longwater March* lands; and if week 4 is consumed by balance (its primary
§4.4 purpose), the set stays on paper. Those four clauses are the whole test
for whether either map gets built, and this is the only section that states
it. Everywhere else the set is named — §2.13.4's configuration ladder,
§2.13.5 and §2.13.6's headers, §2.10's scope table STRETCH row — carries the
*labels* (P1/P2, week 4) as identification and defers here for the
*condition*, so tightening or relaxing the scenario set is one edit in one
place. Two sections stating one condition in their own words is exactly the
drift §4.4 and §4.11 produced three times; the repair there was one owner and
one pointer, and for the scenario set the owner is this paragraph.
```

*Changed from the round-1 filing:* the parenthetical `(§2.13.4, §2.13.6)` after
the ordering clause is gone. It was a citation to the two sites Pairs 2 and 3
now clear, so leaving it would have pointed the reader at text that no longer
states the clause. The four clauses and the exclusivity sentence are otherwise
unchanged, per the instruction not to drop them.

### Pair 2 — §2.13.4, configuration-ladder row 9–10

Verified: this two-row OLD block occurs **exactly once** in `source/gdd.md`
(one match, §2.13.4's replayability ladder). Row 7–8 is included as the anchor
so the block cannot match anywhere else — `Stretch P2 (wk 4, only after P1)`
is itself unique, but the P1 row makes the location unambiguous without
enlarging the edit. Row 7–8 is reproduced **unchanged** in the NEW block; only
row 9–10's Status cell moves.

**OLD**
```
| 7–8 | *Longwater March*, Normal → Hard | Stretch P1 (§4.4 wk 4) |
| 9–10 | *The Causeway*, Normal → Hard | Stretch P2 (wk 4, only after P1) |
```

**NEW**
```
| 7–8 | *Longwater March*, Normal → Hard | Stretch P1 (§4.4 wk 4) |
| 9–10 | *The Causeway*, Normal → Hard | Stretch P2 (wk 4) |
```

The Matches and Configuration columns are untouched: the ladder still runs
1–3, 4–6, 7–8, 9–10 with the same maps, seats and difficulty ramps. What the
row loses is a *scheduling condition* it was never the right place to state —
a replayability table's job is to say which configuration a player reaches at
which match number, not to adjudicate build order. The label `Stretch P2 (wk
4)` still tells the reader this row does not exist in shipped scope, which is
the only thing §2.13.4's Ships-in column has to do. It is also
**character-for-character** the Status cell §2.13.7's summary table already
carries for *The Causeway* at line 1303, so after this pair the ladder row and
the summary row are the same string.

### Pair 3 — §2.13.6, section header

Verified: this OLD block occurs **exactly once** in `source/gdd.md`. It is the
only `2.13.6` heading, and the only other `Stretch scenario` heading (§2.13.5)
names *Longwater March*, not *The Causeway*. Collision check above: clear.

**OLD**
```
#### 2.13.6 Stretch scenario — *The Causeway* (P2, wk 4, only after P1)
```

**NEW**
```
#### 2.13.6 Stretch scenario — *The Causeway* (P2, wk 4)
```

The heading keeps both identifying labels — **P2** and **wk 4** — so all
**eleven** citations of §2.13.6 still resolve to a heading that identifies the
map, its priority and its window. Those eleven sit in §2.13.2 (line 1073) and
§4.7 (Stub 7's T-SCN-08/09/11 invariant and fixture text at lines 1854, 1892,
2000, 2058, 2148, and register rows Q17 ×2, Q21, Q24, Q25); **§2.8 and §4.11
cite §2.13.6 nowhere**, and neither does Q16. The heading sheds only the
ordering condition. Two of the eleven citations quote §2.13.6's *body* — line
1892 and Q25 both quote *"East is the exact ρ-image of West"* from **line
1250** — and Pair 3 does not touch line 1250, so those quotes are unaffected.

A useful side effect: the header now reads `(P2, wk 4)`, which **agrees on both
labels** with the Status cell §2.13.7's summary table already carries for this
map, `Stretch P2 (wk 4)` — same priority, same week. The two are *not* the same
string: the table cell carries a `Stretch` prefix that a header inside a section
already titled "Stretch scenario" does not need. The string that matches
§2.13.7's cell character-for-character is **Pair 2's** new ladder cell. So the
mismatch I flagged last round closes here on the labels, and it closes by moving
the header down to the label rather than by pushing the condition up into a
table cell.

---

## Collision report — figures §2.10's new STRETCH row must not contradict

Reported, not changed, except where a pair above is named. Every figure below
already exists in `source/gdd.md`; I moved none of them.

| Figure | Value | Sites that state it |
|---|---|---|
| Stretch window | **week 4** | §2.13.4 ladder (rows 7–8, 9–10) · §2.13.5 header · §2.13.6 header · §2.13.7 table (both Status cells) · §2.13.7 cut line · §4.4 wk 4 cell |
| P1 | ***Longwater March*** | §2.13.4 · §2.13.5 header · §2.13.7 table |
| P2 | ***The Causeway*** | §2.13.4 · §2.13.6 header · §2.13.7 table |
| Ordering | **P2 only after P1** | **After Pairs 1–3: §2.13.7's cut line, and nowhere else.** Was §2.13.4 row 9–10 (line 1115, cleared by Pair 2) and §2.13.6 header (line 1203, cleared by Pair 3) — those two lines are the document's only occurrences of the clause; never in §2.13.7's Status cells |
| Shipped map | ***Ferrum Crossing***, §2.10 IN | §2.13.2 header · §2.13.7 table |

So a §2.10 STRETCH row is consistent with §2.13 only if it says **week 4**,
**P1 = *Longwater March***, **P2 = *The Causeway***. If it wants to say more
than that — including the ordering — it should point at §2.13.7 instead.

**One live inconsistency I am flagging rather than fixing:**

**§4.7 Stub 7 is not stretch-only, and putting it wholly in a STRETCH row
would contradict four places.** This is the sharpest collision in the round
and it lands on `rules-designer`'s half, so it is a flag, not an edit:

- §4.4 **wk 2** requires *"the one scenario loading, validating and
  rendering"* — that is Stub 7's loader on the critical path in week 2.
- §4.11 **row 10(b)** makes the headless replayer depend on *"row 7's
  **structural** half for the `scenarioId`/`scenarioHash` it loads"*
  (line 2550), and §4.10's save header carries both fields.
- §2.8 / §2.13.2 store the **20-turn cap** in Stub 7's `turnCap`; §2.11.6's
  guided opening reads `guidedOpening.infantry` / `guidedOpening.objective`
  from the same file. Both are §2.10 **IN** content under this round's
  ruling.
- §4.11 says *"Row 7 is still not ON the critical path (nothing in the chain
  waits on it)"* (lines 2565–2566) — off-path is not the same as stretch, and
  row 7's ledger row is explicitly scheduled to flip **after movement (row
  3)**, i.e. in core, not week 4.

The genuinely stretch-side scenario item is the **custom MCP scenario
toolset**, which §4.4 wk 3 already defers (*"follow only if the slice lands
early"*) and §2.10 STRETCH already lists as *"map-gen MCP toolset"*.
Recommended wording for the §2.10 STRETCH row, for `rules-designer` to take
or leave: the stretch item is **the 2nd–3rd scenario *authored on* the Stub-7
format**, not the format and validator themselves. Stub 7's structural half
belongs in IN beside the shipped scenario it loads.

*(The second inconsistency reported last round — §2.13.7's Status cells reading
`Stretch P2 (wk 4)` against §2.13.6's header `(P2, wk 4, only after P1)` — is
resolved by Pair 3 and is no longer live. Caution 2 is right that I read the
mismatch correctly and only failed to file it; it is filed now, and resolved in
the direction the authority model requires, by moving the header rather than
the cells.)*

---

## Change requests

| Existing § | Current text | Proposed change | Why |
|---|---|---|---|
| §2.13.7 (closing paragraph) | *"Neither stretch map may pull work forward of week 4 or block core; if week 4 is consumed by balance (its primary §4.4 purpose), the set stays on paper."* | Pair 1 — same three clauses verbatim, plus the P2-after-P1 ordering relocated from §2.13.4/§2.13.6, plus an explicit single-site declaration | A pointer target must be complete and must claim exclusivity, or §2.10's new row silently becomes a second, divergeable statement — the §4.4/§4.11 failure, four times over |
| §2.13.4 (ladder row 9–10, line 1115) | *"\| 9–10 \| *The Causeway*, Normal → Hard \| Stretch P2 (wk 4, only after P1) \|"* | Pair 2 — Status cell becomes `Stretch P2 (wk 4)` | Makes Pair 1's exclusivity claim true rather than asserted. A replayability ladder identifies a configuration's shipping tier; it is not the place that adjudicates build order. The new cell is character-for-character §2.13.7's Status cell for the same map |
| §2.13.6 (section header, line 1203) | *"#### 2.13.6 Stretch scenario — *The Causeway* (P2, wk 4, only after P1)"* | Pair 3 — header becomes `(P2, wk 4)` | Same reason; and it brings the header's labels into agreement with §2.13.7's existing Status cell for this map. Heading-collision check clear: no TOC, no anchors, and none of the 11 citations of §2.13.6 reproduces the heading string |
| §2.10 STRETCH row (**not mine — `rules-designer`**) | *"2nd–3rd scenario; LLM commander; fog/recon; sea/air units; map-gen MCP toolset; 2-player hotseat"* | Name *Longwater March* (P1) and *The Causeway* (P2), week 4, then defer to §2.13.7 for the condition — **including the ordering**; keep Stub 7's format + validator in **IN** | Filed as a change request against another author's section, for the Director to route. `rules-designer` is dropping `, only after P1` from that cell in parallel this round, which is the fourth and last site |

---

## Open questions for the Director

1. **Is the four-site sweep complete?** After Pairs 1–3 plus `rules-designer`'s
   §2.10 edit, `only after P1` appears exactly once in the document. I have
   verified the two sites inside §2.13 by grep — lines 1115 and 1203 are the
   document's only occurrences of the clause today — but I cannot verify §2.10's
   cell because it is not mine to edit. **If `rules-designer`'s pair does not
   land, Pair 1's exclusivity sentence is false again** — the three pairs here
   are correct but not sufficient on their own. Please gate them together.
2. **Is the Stub 7 flag accepted?** If the Director intends Stub 7 *entire*
   to be stretch, then §4.4 wk 2, §4.11 row 10(b), §2.8's `turnCap` and
   §2.11.6's guided-opening fields all need rerouting, and that is a much larger
   ruling than this round.
3. §2.13.5's header cites `§4.4 wk 4`; §2.13.6's says `wk 4` bare — and Pair 3
   leaves it bare, because evening it up would mean adding a citation, not
   removing a condition, and that is outside what the gate asked for. Cosmetic
   asymmetry inside §2.13, still flagged, still unfixed. One pair if you want it.

---

## Handoffs

- **`rules-designer`** — §2.10's new STRETCH row: name the two maps and week 4,
  then defer to §2.13.7 for the condition rather than restating it. We are
  applying the same principle from opposite ends this round: you drop
  `, only after P1` from §2.10's cell, I drop it from §2.13.4 and §2.13.6, and
  §2.13.7 becomes the sole site. Please also keep Stub 7's format + validator in
  **IN** (see the collision above). After Pair 1, §2.13.7 is complete and safe
  to point at.
- **`tech-director`** — no action requested, but one correction to a claim I
  made in this line last round: **§4.11 does not cite §2.13.6 at all** — it
  contains no occurrence of `2.13` anywhere in lines 2526–2578 — so Pair 3
  cannot touch it. What makes Stub 7 core-side is §4.11's row-10 dependency
  cell, *"row 7's **structural** half for the `scenarioId`/`scenarioHash` it
  loads"* (line 2550), and its row-7 paragraph, *"Row 7 is still not ON the
  critical path (nothing in the chain waits on it)"* (lines 2565–2566); nothing
  in §4.11 needs to change for this round. Ten of the eleven §2.13.6 citations
  *are* in your half — §4.7, in Stub 7's T-SCN-08/09/11 invariant and fixture
  text and in the open-questions register (Q17, Q21, Q24, Q25) — and all ten are
  bare `§2.13.6` citations, so Pair 3 leaves them intact. The two that quote
  §2.13.6's prose (line 1892 in T-SCN-09, and Q25) quote its **body** at line
  1250, not the heading, and Pair 3 does not touch line 1250.
- **`ux-onboarding-designer`** — none. §2.11.6's guided opening reads Stub 7
  fields; if the Stub 7 collision resolves the wrong way it becomes your problem
  too.
- **T-SCN-11 not opened.** No invariant, lane cost, deployment hex or map
  geometry is touched anywhere in this file.

---

## Grounding

| Claim | Traced to |
|---|---|
| "week 4" | §2.13.7 existing cut line; §2.13.5/§2.13.6 headers; §4.4 wk-4 milestone row |
| "*The Causeway* only after *Longwater March*" | §2.13.6 header *"(P2, wk 4, only after P1)"* (line 1203); §2.13.4 ladder row *"Stretch P2 (wk 4, only after P1)"* (line 1115) — relocated, not coined |
| "balance is week 4's primary §4.4 purpose" | §4.4 wk 4: *"Self-play balance sims and tuning … scenario polish (additional scenarios only as stretch)"* — unchanged from the existing cut line |
| "does not block core" | §4.5 risk row *"Hard MVP line; 1 scenario + flag win is complete"*; §2.10 IN *"one hand-built scenario"* |
| Pair 2's NEW cell `Stretch P2 (wk 4)` | **Character-for-character** the Status cell §2.13.7's summary table already carries for *The Causeway* (line 1303) — no new priority string is coined |
| Pair 3's NEW header labels `(P2, wk 4)` | The same **labels** as that cell — same priority, same week, minus the `Stretch` prefix the cell carries and a heading under "Stretch scenario" does not. Label agreement, not string identity; the exact-string match is Pair 2's. Parallel form: §2.13.5's header `(P1, §4.4 wk 4)` |
| Pair 3 breaks no reference | **Re-swept from scratch this round.** `](#` → 0 matches document-wide. `Stretch scenario` → 2 lines (1124, 1203), both headings, so no TOC or index reproduces the title. `2.13.6` → **12 occurrences on 11 lines**; subtracting the heading at line 1203 leaves **11 citations on 10 lines** — §2.13.2 line 1073, §4.7 Stub 7 lines 1854, 1892, 2000, 2058, 2148, and §4.7 register rows Q17 (line 2288, twice), Q21 (2292), Q24 (2295), Q25 (2296). **§2.8, §4.11 and Q16 cite §2.13.6 zero times** — §4.11, lines 2526–2578, contains no `2.13` at all. Zero of the 11 reproduce the heading string; the two that quote §2.13.6's prose — line 1892 and Q25, both quoting *"East is the exact ρ-image of West"* — quote **line 1250, in the body**, which Pair 3 does not touch |
| Each OLD block is unique | Grep-verified individually: Pair 1's cut line = 1 match; Pair 2's two-row block = 1 match; Pair 3's heading = 1 match. `only after P1` itself occurs at exactly 2 lines document-wide, 1115 and 1203, both edited here |
| The one-owner-one-pointer pattern | §4.11 row 10: *"§4.4's table and the note under it are the single statement of the schedule, and this paragraph deliberately does not restate the week numbers a second time"*; §4.4's Q23/Q20 note: *"Stated once, so the table stops drifting"* |
| Stub 7 is core-side | §4.4 wk 2; §4.11 row 10(b) (line 2550) and the row-7 paragraph (lines 2565–2566); §2.13.2 `turnCap`; §2.11.6 `guidedOpening.*`; §4.10 save header `scenarioId`/`scenarioHash` |

No new hex, lane cost, deployment position, factory count, town count, week
number or priority appears anywhere in this addendum. Pairs 2 and 3 only
**remove** an existing clause from two sites; they add no text. Every line
number and count above was re-derived against `source/gdd.md` rather than
carried over from an earlier filing, and no negative finding here is supported
by a claim about what a section cites instead.

---

## PLACEMENT

**Three pairs, three destinations, all inside §2.13.**

- **Pair 1** replaces the **final paragraph of §2.13.7** — the two-line cut line
  at lines 1305–1306, immediately below the three-row scenario-set table, and
  the last prose in §2 before the `---` that opens §3. Paragraph-for-paragraph
  substitution.
- **Pair 2** replaces the **last two rows of §2.13.4's configuration table**
  (rows 7–8 and 9–10, lines 1114–1115). Row 7–8 is reproduced unchanged as the
  anchor; only row 9–10's third cell differs. No other row, no table header, no
  surrounding prose moves.
- **Pair 3** replaces the **`#### 2.13.6` heading line itself, line 1203**. The
  heading's section number, map name and both labels are preserved, so all
  **eleven** §2.13.6 citations elsewhere — one in §2.13.2, ten in §4.7 — still
  resolve; §2.13.6's body, including the sentence at line 1250 that two of those
  citations quote, and the `| Spec | Value |` table beneath the heading, are
  untouched.

Order of application does not matter — the three sites do not overlap. Nothing
in §2.13.1, §2.13.2, §2.13.3, §2.13.5 or the bodies of §2.13.4/§2.13.6/§2.13.7
is edited, and no pair is filed against §2.10, §1, §2.11, §3 or §4.

---

## Summary for the Director (relay verbatim)

§2.13.7 is now the **single owner** of the scenario set's stretch condition, and
this round makes that true rather than merely asserted: three pairs, all inside
§2.13. Pair 1 rewrites §2.13.7's closing cut line to state all four clauses —
the existing three word for word, plus *The Causeway* only after *Longwater
March* — and to declare itself the only site; Pairs 2 and 3 then strip
`, only after P1` from the only two lines in the document that still said it,
§2.13.4's ladder row (line 1115) and §2.13.6's header (line 1203), keeping the
identifying labels `Stretch P2 (wk 4)` and `(P2, wk 4)` so nothing loses its
priority or its week — Pair 2's new cell is character-for-character §2.13.7's
Status cell for this map, and Pair 3's header agrees with that cell on both
labels without being the same string, since the cell carries a `Stretch` prefix
a header under "Stretch scenario" does not need. Pair 3 edits a heading, so the
cross-reference sweep was re-run from scratch: there is **no table of contents
and no anchor link anywhere** (`](#` → 0 matches, and `Stretch scenario` occurs
on exactly two lines, both the headings themselves, so no index reproduces the
title), and the string `2.13.6` occurs **twelve times on eleven lines** — the
heading itself plus **eleven citations on ten lines**, one in §2.13.2 (line
1073) and ten in §4.7 (five in Stub 7's T-SCN-08/09/11 invariant and fixture
text at lines 1854, 1892, 2000, 2058 and 2148, and five across register rows
Q17, Q21, Q24 and Q25, Q17 citing it twice). **Not one of the eleven reproduces
the heading string**, so the heading moves with nothing dangling. Two of them do
quote §2.13.6's prose — line 1892 and Q25 both quote *"East is the exact ρ-image
of West"* — but that sentence is in §2.13.6's **body** at line 1250, which Pair
3 does not touch. **§2.8, §4.11 and Q16 cite §2.13.6 zero times**; §4.11, lines
2526–2578, contains no occurrence of `2.13` at all. Three corrections have now
been made to this file's own reporting rather than to its pairs, and the last
two are one mistake in two directions: a check that named what a section *does*
cite in support of a finding about what it *does not*. That clause class is
removed — the zero-citation row is purely negative now, and every positive claim
left in the file carries the line number it was verified at. Each OLD block is
grep-verified as occurring exactly once, with §2.13.4's row anchored to the row
above it. Two things stay in the Director's hands: this only closes if
`rules-designer`'s parallel §2.10 edit lands — if it does not, Pair 1's
exclusivity sentence is false again, so please gate the two together — and
**§4.7 Stub 7 still cannot go wholly into a STRETCH row**, since §4.4 week 2
requires the scenario loading and validating, §4.11 row 10(b) (line 2550) makes
the headless replayer depend on row 7's structural half, and §2.13.2's 20-turn
cap plus §2.11.6's guided-opening fields both live in that file. The stretch
item is the 2nd–3rd scenario authored on the Stub-7 format, not the format
itself.
